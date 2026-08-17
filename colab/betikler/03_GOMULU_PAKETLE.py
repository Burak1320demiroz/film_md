"""Promptlari betigin ICINE gomup tek dosyalik, kendi kendine yeten uretici yazar.

NEDEN VAR: iki asamali akis (colab new -> colab upload -> colab exec) kirilgan.
11.08.2026'da yasandi: uzun exec surerken oturuma dokunmak yerel kaydi
sildirdi, sonra VM tamamen dustu; inen model de karelerle birlikte gitti.

Bu paketleyici tek dosya uretir; o dosya `colab run` ile TEK komutta kosar:
promptlar icinde, yukleme adimi yok, dokunulacak bir sey yok.

Ayrica ureten dosyaya KALP ATISI konur: uzun model indirmesi sirasinda her
30 saniyede bir satir basar. Sebep: `colab exec/run --timeout` degeri
"cikti bekleme" suresidir; sessiz kalan is baglantiyi dusuruyor.

Kullanim (yerelde):
    python3 colab/betikler/03_GOMULU_PAKETLE.py > /tmp/uret.py
    colab run -s uretim --gpu T4 --keep --timeout 5400 /tmp/uret.py
    colab download -s uretim /content/ciktilar/P1_OLCEK__zimage.png ./
    colab stop -s uretim
"""

import glob
import json
import os

PROMPT_KLASORU = os.path.join(os.path.dirname(__file__), "..", "ornek_uretim", "promptlar")
MODEL = os.environ.get("URETIM_MODEL", "zimage")

GOVDE = '''
import json, os, threading, time

MODEL = {model!r}
PROMPTLAR = {promptlar}
GENISLIK, YUKSEKLIK = 720, 1280   # tam 9:16, 16'nin kati
SEED = 1320
ADIM = {{"zimage": 8, "sdxl": 30}}[MODEL]
CFG = {{"zimage": 1.0, "sdxl": 6.0}}[MODEL]
CIKTI = "/content/ciktilar"

# ── KALP ATISI ────────────────────────────────────────────────────────────
# colab exec/run --timeout = "cikti bekleme" suresi. Model indirmesi sessiz
# gecerse baglanti dusuyor. Bu thread her 30 s bir satir basip hatti acik tutar.
_dur = threading.Event()
def _kalp():
    t0 = time.time()
    while not _dur.wait(30):
        print(f"[kalp] {{time.time() - t0:.0f}} s · surüyor", flush=True)
threading.Thread(target=_kalp, daemon=True).start()

def prompt_ayir(metin):
    for isaret in ("NEGATIVE:", "NEGATIF:"):
        if isaret in metin:
            p, n = metin.split(isaret, 1)
            return p.strip(), n.strip()
    return metin.strip(), ""

print(f"[baslik] model={{MODEL}} · {{len(PROMPTLAR)}} prompt · {{GENISLIK}}x{{YUKSEKLIK}} · seed={{SEED}}", flush=True)

import torch
p = torch.cuda.get_device_properties(0)
try:
    bf16 = torch.cuda.is_bf16_supported(including_emulation=False)
except TypeError:
    bf16 = torch.cuda.get_device_capability(0) >= (8, 0)
dtype = torch.bfloat16 if bf16 else torch.float16
print(f"[gpu] {{p.name}} · {{p.total_memory / 1024**3:.1f}} GB · dtype={{dtype}} (bf16 yerli: {{bf16}})", flush=True)

# KURULUM YOK — Colab'in hazir yigini kullanilir (diffusers 0.39 + transformers 5.13).
# `pip install -U` bu yigini kiriyor: betikler/00_README.md §EN PAHALI DERS
import diffusers
print(f"[yigin] diffusers {{diffusers.__version__}} · kurulum yapilmadi", flush=True)

t0 = time.time()
if MODEL == "zimage":
    from diffusers import DiffusionPipeline
    pipe = DiffusionPipeline.from_pretrained("Tongyi-MAI/Z-Image-Turbo", torch_dtype=dtype)
else:
    from diffusers import StableDiffusionXLPipeline
    pipe = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=dtype, variant="fp16", use_safetensors=True)
try:
    pipe.enable_model_cpu_offload(); print("[bellek] CPU offload acik", flush=True)
except Exception as e:
    print(f"[bellek] offload yok ({{type(e).__name__}}) -> cuda", flush=True); pipe.to("cuda")
for f in ("enable_vae_slicing", "enable_vae_tiling", "enable_attention_slicing"):
    try: getattr(pipe, f)()
    except Exception: pass
yukleme = time.time() - t0
print(f"[model] hazir · {{yukleme:.0f}} s", flush=True)

os.makedirs(CIKTI, exist_ok=True)
ozet = []
for i, (ad, metin) in enumerate(sorted(PROMPTLAR.items()), 1):
    poz, neg = prompt_ayir(metin)
    print(f"\\n[{{i}}/{{len(PROMPTLAR)}}] {{ad}} · negatif {{'VAR' if neg else 'YOK'}}", flush=True)
    kw = dict(prompt=poz, height=YUKSEKLIK, width=GENISLIK, num_inference_steps=ADIM,
              guidance_scale=CFG, generator=torch.Generator("cpu").manual_seed(SEED))
    if neg:
        kw["negative_prompt"] = neg
    torch.cuda.reset_peak_memory_stats()
    t1 = time.time()
    try:
        gorsel = pipe(**kw).images[0]
    except Exception as e:
        print(f"  [HATA] {{type(e).__name__}}: {{str(e)[:200]}}", flush=True)
        ozet.append({{"ad": ad, "durum": f"HATA: {{type(e).__name__}}"}}); continue
    sure = time.time() - t1
    tepe = torch.cuda.max_memory_allocated() / 1024**3
    png = os.path.join(CIKTI, f"{{ad}}__{{MODEL}}.png")
    gorsel.save(png)
    kayit = {{"ad": ad, "model": MODEL, "dtype": str(dtype), "gpu": p.name,
             "olcu": f"{{GENISLIK}}x{{YUKSEKLIK}}", "adim": ADIM, "guidance_scale": CFG,
             "seed": SEED, "negatif_kullanildi": bool(neg), "uretim_saniye": round(sure, 1),
             "tepe_vram_gb": round(tepe, 2), "prompt": poz, "negatif": neg or None}}
    open(png.replace(".png", ".json"), "w").write(json.dumps(kayit, ensure_ascii=False, indent=2))
    print(f"  -> {{png}} · {{sure:.0f}} s · tepe {{tepe:.2f}} GB", flush=True)
    ozet.append({{"ad": ad, "durum": "OK", "saniye": round(sure, 1), "tepe_vram_gb": round(tepe, 2)}})

_dur.set()
print("\\n" + "=" * 60, flush=True)
print(f"BITTI · model {{MODEL}} · yukleme {{yukleme:.0f}} s", flush=True)
for s in ozet:
    print(f"  {{s['ad']:<24}} {{s['durum']}} {{s.get('saniye','')}} s", flush=True)
print("=" * 60, flush=True)
open(os.path.join(CIKTI, f"_ozet_{{MODEL}}.json"), "w").write(
    json.dumps({{"model": MODEL, "yukleme_saniye": round(yukleme, 1), "kareler": ozet}}, ensure_ascii=False, indent=2))
print("[indir] colab download -s uretim /content/ciktilar/<ad>__" + MODEL + ".png ./", flush=True)
'''


def main():
    promptlar = {}
    for yol in sorted(glob.glob(os.path.join(PROMPT_KLASORU, "*.txt"))):
        ad = os.path.splitext(os.path.basename(yol))[0]
        promptlar[ad] = open(yol, encoding="utf-8").read()
    if not promptlar:
        raise SystemExit(f"[hata] prompt bulunamadi: {PROMPT_KLASORU}")
    print(GOVDE.format(model=MODEL, promptlar=json.dumps(promptlar, ensure_ascii=False)))


if __name__ == "__main__":
    main()
