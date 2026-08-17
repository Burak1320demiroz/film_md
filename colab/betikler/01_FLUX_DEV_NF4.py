"""FLUX.1-dev (12B) — 4-bit NF4 ile Colab GPU'sunda gorsel uretimi.

NEDEN NF4: FLUX.1-dev bf16 agirlikla ~24 GB. Ucretsiz T4'un 16 GB'ina
sigmaz. bitsandbytes NF4 (4-bit) kuantizasyonu modeli ~1/4'e indiriyor;
Hugging Face'in kendi diffusers dokumani bu yolun "16 GB'in altinda ve
ucretsiz Colab'da" calistigini soyluyor.

NEDEN fp16: T4 bf16'yi DONANIMDA yapmiyor. PyTorch'un
is_bf16_supported() fonksiyonu "var" der ama emulasyonu sayar; olculdu
(11.08.2026, Colab T4): fp16 23.5 TFLOPS, bf16 2.2 TFLOPS -> 10.9x fark.
Betik YERLI destegi sorar ve yoksa fp16 secer.

NEGATIF PROMPT: FluxPipeline `negative_prompt` parametresini alir ama
`true_cfg_scale > 1` verilmedikce YOK SAYAR (guidance-distilled model).
--true-cfg 4.0 verirsen negatif cekirdek gercekten devreye girer,
bedeli ~2x sure (her adimda iki gecis).

Kullanim (yerelden, tek komut):
    colab run --gpu T4 --timeout 3600 colab/betikler/01_FLUX_DEV_NF4.py \
        --prompt-dosya prompt.txt --out /content/ciktilar/kapak.png

Oturumu ayakta tutup birden fazla kare uretmek icin:
    colab new -s film --gpu T4
    colab exec -s film -f colab/betikler/01_FLUX_DEV_NF4.py
    colab download -s film /content/ciktilar/kapak.png ./kapak.png
    colab stop -s film            # <-- unutulursa CU yakmaya devam eder
"""

import argparse
import json
import os
import subprocess
import sys
import time

# 9:16'yi TAM tutan ve 16'ya bolunebilen olculer (FLUX 16'nin katini ister):
#   720x1280 · 1008x1792 · 1152x2048
VARSAYILAN_PROMPT = (
    "Cinematic photorealistic vertical cover image, 9:16. A wrecked present-day "
    "single-seat re-entry capsule, a blunt white-and-charcoal cone about 4 metres "
    "tall, heat shield scorched matte black, no readable markings, sits tilted in a "
    "gouged trench of torn ferns on a Cretaceous fern plain in golden morning light. "
    "A 38-year-old woman test pilot in a rescue-orange flight pressure suit and white "
    "helmet with a fully transparent closed visor stands pressed back against the hull, "
    "arms at her sides, tiny and still. Photographed as a real person, not CGI. "
    "Full golden morning sunlight from frame right, hard clean shadows, deep green "
    "ferns, the orange figure the only saturated colour in the image. "
    "No bloom, no glow filter, no lens flare."
)

VARSAYILAN_NEGATIF = (
    "grass, birds, flying creatures, fire, smoke, rain, water, mud, miniature, "
    "toy look, CGI look, game-engine look, waxy skin, extra people, text, logo, "
    "watermark, lens flare, god rays, bloom"
)


def paket_kur():
    """Colab VM'inde eksik paketleri kur. uv varsa onu kullan."""
    paketler = ["diffusers", "transformers", "accelerate", "bitsandbytes", "sentencepiece", "protobuf"]
    print(f"[kurulum] {' '.join(paketler)}")
    for komut in (
        ["uv", "pip", "install", "--system", "-q", "-U", *paketler],
        [sys.executable, "-m", "pip", "install", "-q", "-U", *paketler],
    ):
        try:
            subprocess.run(komut, check=True)
            return
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
    raise SystemExit("[hata] paketler kurulamadi")


def token_kontrol():
    """FLUX.1-dev KAPILI (gated) bir depo — HF token sart."""
    if os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN"):
        return
    for yol in ("/root/.cache/huggingface/token", os.path.expanduser("~/.cache/huggingface/token")):
        if os.path.isfile(yol) and open(yol).read().strip():
            os.environ["HF_TOKEN"] = open(yol).read().strip()
            return
    raise SystemExit(
        "[hata] HF token bulunamadi. FLUX.1-dev kapili bir depo.\n"
        "  Yerelden su iki komuttan birini yap:\n"
        "    1) token'i dosyaya yaz, sonra:\n"
        "       colab upload -s <oturum> ~/.hf_token /root/.cache/huggingface/token\n"
        "    2) ya da bu betigi HF_TOKEN ortam degiskeni tanimlandiktan sonra kosur."
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", default=None)
    ap.add_argument("--prompt-dosya", default=None, help="Prompt metnini dosyadan oku")
    ap.add_argument("--negatif", default=VARSAYILAN_NEGATIF)
    ap.add_argument("--genislik", type=int, default=720)
    ap.add_argument("--yukseklik", type=int, default=1280)
    ap.add_argument("--adim", type=int, default=28)
    ap.add_argument("--guidance", type=float, default=3.5)
    ap.add_argument(
        "--true-cfg",
        type=float,
        default=1.0,
        help="1.0 = negatif prompt YOK SAYILIR. 4.0 = negatif cekirdek devreye girer (~2x sure).",
    )
    ap.add_argument("--seed", type=int, default=1320)
    ap.add_argument("--out", default="/content/ciktilar/kapak.png")
    ap.add_argument(
        "--kaynak",
        choices=["nf4pkg", "gated"],
        default="nf4pkg",
        help="nf4pkg: hazir kuantize (~9 GB indirme). gated: 24 GB indir, ucusta kuantize et.",
    )
    a = ap.parse_args()

    if a.prompt_dosya:
        a.prompt = open(a.prompt_dosya, encoding="utf-8").read().strip()
    if not a.prompt:
        a.prompt = VARSAYILAN_PROMPT

    for ad, deger in (("genislik", a.genislik), ("yukseklik", a.yukseklik)):
        if deger % 16:
            raise SystemExit(f"[hata] {ad}={deger} 16'nin kati olmali (720x1280 · 1008x1792 · 1152x2048)")

    paket_kur()
    token_kontrol()

    import torch
    from diffusers import AutoModel, BitsAndBytesConfig as DiffusersBnb, FluxPipeline
    from transformers import BitsAndBytesConfig as TransformersBnb, T5EncoderModel

    if not torch.cuda.is_available():
        raise SystemExit("[hata] GPU yok. --gpu bayragiyla oturum ac.")

    p = torch.cuda.get_device_properties(0)
    # DIKKAT: is_bf16_supported() EMULASYONU da "var" sayar. T4'te bf16
    # emulasyonla yapiliyor ve olculdu: fp16 23.5 TFLOPS'a karsi bf16
    # 2.2 TFLOPS (10.9x yavas). Bu yuzden YERLI destegi soruyoruz.
    try:
        bf16 = torch.cuda.is_bf16_supported(including_emulation=False)
    except TypeError:  # eski torch: parametre yok
        bf16 = torch.cuda.get_device_capability(0) >= (8, 0)
    dtype = torch.bfloat16 if bf16 else torch.float16
    print(f"[gpu] {p.name} · {p.total_memory / 1024**3:.1f} GB · dtype={dtype}")
    if not bf16:
        print("[gpu] bf16 DONANIMDA yok -> fp16 hesap (11x fark, olculdu 11.08.2026)")

    t0 = time.time()
    if a.kaynak == "nf4pkg":
        print("[model] hazir NF4 paketi yukleniyor")
        transformer = AutoModel.from_pretrained(
            "hf-internal-testing/flux.1-dev-nf4-pkg", subfolder="transformer", torch_dtype=dtype
        )
        text_encoder_2 = T5EncoderModel.from_pretrained(
            "hf-internal-testing/flux.1-dev-nf4-pkg", subfolder="text_encoder_2", torch_dtype=dtype
        )
    else:
        print("[model] kapili depodan indirilip ucusta NF4'e kuantize ediliyor (~24 GB)")
        text_encoder_2 = T5EncoderModel.from_pretrained(
            "black-forest-labs/FLUX.1-dev",
            subfolder="text_encoder_2",
            quantization_config=TransformersBnb(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=dtype),
            torch_dtype=dtype,
        )
        transformer = AutoModel.from_pretrained(
            "black-forest-labs/FLUX.1-dev",
            subfolder="transformer",
            quantization_config=DiffusersBnb(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=dtype),
            torch_dtype=dtype,
        )

    pipe = FluxPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-dev",
        transformer=transformer,
        text_encoder_2=text_encoder_2,
        torch_dtype=dtype,
    )
    try:
        pipe.enable_model_cpu_offload()
        print("[bellek] model CPU offload acik")
    except Exception as e:  # bnb + offload surum uyumsuzlugu olursa dogrudan GPU
        print(f"[bellek] offload kurulamadi ({e}); dogrudan cuda'ya tasiniyor")
        pipe.to("cuda")
    yukleme = time.time() - t0
    print(f"[model] hazir · {yukleme:.0f} s")

    kwargs = dict(
        prompt=a.prompt,
        height=a.yukseklik,
        width=a.genislik,
        guidance_scale=a.guidance,
        num_inference_steps=a.adim,
        max_sequence_length=512,
        generator=torch.manual_seed(a.seed),
    )
    if a.true_cfg > 1.0:
        kwargs.update(negative_prompt=a.negatif, true_cfg_scale=a.true_cfg)
        print(f"[negatif] true_cfg_scale={a.true_cfg} -> negatif prompt ETKIN (~2x sure)")
    else:
        print("[negatif] true_cfg_scale=1.0 -> negatif prompt YOK SAYILIYOR")

    torch.cuda.reset_peak_memory_stats()
    t1 = time.time()
    gorsel = pipe(**kwargs).images[0]
    uretim = time.time() - t1
    tepe = torch.cuda.max_memory_allocated() / 1024**3

    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    gorsel.save(a.out)

    kayit = {
        "model": "black-forest-labs/FLUX.1-dev",
        "kuantizasyon": f"NF4 4-bit ({a.kaynak})",
        "dtype": str(dtype),
        "gpu": p.name,
        "vram_gb": round(p.total_memory / 1024**3, 1),
        "olcu": f"{a.genislik}x{a.yukseklik}",
        "adim": a.adim,
        "guidance_scale": a.guidance,
        "true_cfg_scale": a.true_cfg,
        "seed": a.seed,
        "prompt": a.prompt,
        "negatif": a.negatif if a.true_cfg > 1.0 else None,
        "yukleme_saniye": round(yukleme, 1),
        "uretim_saniye": round(uretim, 1),
        "tepe_vram_gb": round(tepe, 2),
    }
    yan = a.out.rsplit(".", 1)[0] + ".json"
    with open(yan, "w", encoding="utf-8") as f:
        json.dump(kayit, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print(f"[bitti] {a.out}")
    print(f"[bitti] kayit: {yan}")
    print(f"[olcum] yukleme {yukleme:.0f} s · uretim {uretim:.0f} s · tepe VRAM {tepe:.2f} GB")
    print(f"[olcum] adim basina ~{uretim / a.adim:.1f} s")
    print("=" * 60)
    print("Indirmek icin:  colab download -s <oturum> " + a.out + " ./")


if __name__ == "__main__":
    main()
