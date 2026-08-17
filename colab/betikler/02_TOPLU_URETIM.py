"""Bir klasordeki prompt dosyalarini sirayla uretir — model BIR KEZ yuklenir.

Neden ayri betik: 01_FLUX_DEV_NF4.py tek kare uretir ve her cagrida modeli
bastan yukler. Bes kare icin bu bes kez yukleme demek. Burada model bir kez
yuklenir, prompt dosyalari uzerinde dongu kurulur.

PROMPT DOSYA BICIMI: duz metin. Icinde "NEGATIVE:" ile baslayan bir satir
varsa, o satirdan sonrasi NEGATIF PROMPT olarak ayrilir ve modele ayri
girdi olarak verilir (deponun negatif cekirdegi burada gercekten calisir).

MODELLER
  zimage  Tongyi-MAI/Z-Image-Turbo   Apache 2.0 · kapisiz · az adim (hizli)
  sdxl    stabilityai/...-xl-base-1.0 kapisiz · T4'te garantili · yedek
  flux    black-forest-labs/FLUX.1-dev NF4 4-bit · KAPILI (HF token sart)

Kullanim:
    colab exec -s ornek --timeout 5400 -f colab/betikler/02_TOPLU_URETIM.py
Parametreler kod icindeki AYAR blogundan degistirilir (exec argv gecmez).
"""

import glob
import json
import os
import subprocess
import sys
import time

# ─── AYAR ────────────────────────────────────────────────────────────────
MODEL = os.environ.get("URETIM_MODEL", "zimage")  # zimage | sdxl | flux
PROMPT_KLASORU = "/content/promptlar"
CIKTI_KLASORU = "/content/ciktilar"
GENISLIK, YUKSEKLIK = 720, 1280  # tam 9:16, 16'nin kati
SEED = 1320                       # sabit — karsilastirma icin sart
ADIM = {"zimage": 8, "sdxl": 30, "flux": 28}
CFG = {"zimage": 1.0, "sdxl": 6.0, "flux": 3.5}
# ─────────────────────────────────────────────────────────────────────────


def paket_kur():
    """Paketleri kur. URETIM_KURULUM=0 ise atla.

    ⚠️ TUZAK (11.08.2026'da yasandi): pip -U ile diffusers/transformers
    yukseltmek Colab'in onceden kurulu numpy/scipy ikili uyumunu bozuyor
    ve `cannot import name '_center' from 'numpy._core.umath'` hatasi
    veriyor. Cozum: kurulumu AYRI adimda yap, sonra kernel'i YENIDEN
    BASLAT, sonra bu betigi URETIM_KURULUM=0 ile kosur.
    """
    if os.environ.get("URETIM_KURULUM") == "0":
        print("[kurulum] atlandi (URETIM_KURULUM=0)", flush=True)
        return
    paketler = ["diffusers", "transformers", "accelerate", "sentencepiece", "protobuf", "numpy", "scipy"]
    if MODEL == "flux":
        paketler.append("bitsandbytes")
    print(f"[kurulum] {' '.join(paketler)}", flush=True)
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


def prompt_ayir(metin):
    """NEGATIVE: satirindan sonrasini negatif prompt olarak ayir."""
    for isaret in ("NEGATIVE:", "NEGATIF:"):
        if isaret in metin:
            pozitif, negatif = metin.split(isaret, 1)
            return pozitif.strip(), negatif.strip()
    return metin.strip(), ""


def main():
    paket_kur()
    import torch

    if not torch.cuda.is_available():
        raise SystemExit("[hata] GPU yok")

    p = torch.cuda.get_device_properties(0)
    try:
        bf16_yerli = torch.cuda.is_bf16_supported(including_emulation=False)
    except TypeError:
        bf16_yerli = torch.cuda.get_device_capability(0) >= (8, 0)
    dtype = torch.bfloat16 if bf16_yerli else torch.float16
    print(f"[gpu] {p.name} · {p.total_memory / 1024**3:.1f} GB · dtype={dtype}", flush=True)
    if not bf16_yerli:
        print("[gpu] bf16 donanimda YOK -> fp16 (T4'te bf16 emulasyon, 11x yavas)", flush=True)

    t0 = time.time()
    if MODEL == "zimage":
        from diffusers import DiffusionPipeline

        pipe = DiffusionPipeline.from_pretrained("Tongyi-MAI/Z-Image-Turbo", torch_dtype=dtype)
    elif MODEL == "sdxl":
        from diffusers import StableDiffusionXLPipeline

        pipe = StableDiffusionXLPipeline.from_pretrained(
            "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=dtype, variant="fp16", use_safetensors=True
        )
    elif MODEL == "flux":
        from diffusers import AutoModel, FluxPipeline
        from transformers import T5EncoderModel

        transformer = AutoModel.from_pretrained(
            "hf-internal-testing/flux.1-dev-nf4-pkg", subfolder="transformer", torch_dtype=dtype
        )
        text_encoder_2 = T5EncoderModel.from_pretrained(
            "hf-internal-testing/flux.1-dev-nf4-pkg", subfolder="text_encoder_2", torch_dtype=dtype
        )
        pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-dev", transformer=transformer, text_encoder_2=text_encoder_2, torch_dtype=dtype
        )
    else:
        raise SystemExit(f"[hata] bilinmeyen model: {MODEL}")

    try:
        pipe.enable_model_cpu_offload()
        print("[bellek] CPU offload acik", flush=True)
    except Exception as e:
        print(f"[bellek] offload kurulamadi ({type(e).__name__}); cuda'ya tasiniyor", flush=True)
        pipe.to("cuda")
    try:
        pipe.enable_vae_slicing()
    except Exception:
        pass
    yukleme = time.time() - t0
    print(f"[model] {MODEL} hazir · {yukleme:.0f} s", flush=True)

    os.makedirs(CIKTI_KLASORU, exist_ok=True)
    dosyalar = sorted(glob.glob(os.path.join(PROMPT_KLASORU, "*.txt")))
    if not dosyalar:
        raise SystemExit(f"[hata] {PROMPT_KLASORU} icinde .txt prompt yok")
    print(f"[kuyruk] {len(dosyalar)} prompt", flush=True)

    ozet = []
    for i, yol in enumerate(dosyalar, 1):
        ad = os.path.splitext(os.path.basename(yol))[0]
        pozitif, negatif = prompt_ayir(open(yol, encoding="utf-8").read())
        print(f"\n[{i}/{len(dosyalar)}] {ad} · negatif {'VAR' if negatif else 'YOK'}", flush=True)

        kwargs = dict(
            prompt=pozitif,
            height=YUKSEKLIK,
            width=GENISLIK,
            num_inference_steps=ADIM[MODEL],
            generator=torch.Generator("cpu").manual_seed(SEED),
        )
        if MODEL == "flux":
            kwargs.update(guidance_scale=CFG[MODEL], max_sequence_length=512)
            if negatif:  # FLUX negatifi ancak true_cfg_scale>1 ile kullanir
                kwargs.update(negative_prompt=negatif, true_cfg_scale=4.0)
        else:
            kwargs.update(guidance_scale=CFG[MODEL])
            if negatif:
                kwargs.update(negative_prompt=negatif)

        torch.cuda.reset_peak_memory_stats()
        t1 = time.time()
        try:
            gorsel = pipe(**kwargs).images[0]
        except Exception as e:
            print(f"  [HATA] {type(e).__name__}: {e}", flush=True)
            ozet.append({"ad": ad, "durum": f"HATA: {type(e).__name__}"})
            continue
        sure = time.time() - t1
        tepe = torch.cuda.max_memory_allocated() / 1024**3

        png = os.path.join(CIKTI_KLASORU, f"{ad}__{MODEL}.png")
        gorsel.save(png)
        kayit = {
            "ad": ad,
            "model": MODEL,
            "dtype": str(dtype),
            "gpu": p.name,
            "olcu": f"{GENISLIK}x{YUKSEKLIK}",
            "adim": ADIM[MODEL],
            "guidance_scale": CFG[MODEL],
            "seed": SEED,
            "negatif_kullanildi": bool(negatif),
            "uretim_saniye": round(sure, 1),
            "tepe_vram_gb": round(tepe, 2),
            "prompt": pozitif,
            "negatif": negatif or None,
        }
        with open(png.replace(".png", ".json"), "w", encoding="utf-8") as f:
            json.dump(kayit, f, ensure_ascii=False, indent=2)
        print(f"  -> {png} · {sure:.0f} s · tepe {tepe:.2f} GB", flush=True)
        ozet.append({"ad": ad, "durum": "OK", "saniye": round(sure, 1), "tepe_vram_gb": round(tepe, 2)})

    print("\n" + "=" * 60)
    print(f"MODEL {MODEL} · yukleme {yukleme:.0f} s")
    for s in ozet:
        print(f"  {s['ad']:<24} {s.get('durum')} {s.get('saniye', '')}")
    print("=" * 60, flush=True)
    with open(os.path.join(CIKTI_KLASORU, f"_ozet_{MODEL}.json"), "w", encoding="utf-8") as f:
        json.dump({"model": MODEL, "yukleme_saniye": round(yukleme, 1), "kareler": ozet}, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
