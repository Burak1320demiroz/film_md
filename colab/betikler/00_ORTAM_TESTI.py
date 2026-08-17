"""Colab ortam testi — GPU adi, VRAM, bf16/fp8 destegi, RAM, disk.

Amaci: model indirmeden once "bu makine ne yapabilir" sorusunu cevaplamak.
02_DONANIM_VE_MALIYET.md'deki VRAM tablosunun ve "T4 TUZAGI" bolumunun
olculmus satirlari buradan cikar.

Kullanim (yerelden):
    colab run --gpu T4 --timeout 300 colab/betikler/00_ORTAM_TESTI.py
"""

import os
import shutil
import subprocess
import time
import sys


def satir(ad, deger):
    print(f"{ad:<28} {deger}")


print("=" * 60)
print("COLAB ORTAM TESTI")
print("=" * 60)

try:
    import torch
except ImportError:
    print("torch yok — kuruluyor")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "torch"], check=True)
    import torch

satir("python", sys.version.split()[0])
satir("torch", torch.__version__)
satir("cuda derlemesi", torch.version.cuda)
satir("cuda gorunur mu", torch.cuda.is_available())

if torch.cuda.is_available():
    p = torch.cuda.get_device_properties(0)
    cap = torch.cuda.get_device_capability(0)
    vram = p.total_memory / 1024**3

    print("-" * 60)
    satir("GPU", p.name)
    satir("VRAM (toplam)", f"{vram:.1f} GB")
    satir("compute capability", f"{cap[0]}.{cap[1]}")
    satir("SM sayisi", p.multi_processor_count)

    # Kritik iki soru: modern video/gorsel modelleri bu ikisine dayaniyor.
    # DIKKAT: is_bf16_supported() varsayilan olarak EMULASYONU da sayar.
    # Turing (7.5) bf16'yi tensor cekirdeginde YAPMAZ; emulasyon yavastir.
    # Bu yuzden ikisini ayri sorup ustune olcuyoruz.
    bf16_her = torch.cuda.is_bf16_supported()
    try:
        bf16_yerli = torch.cuda.is_bf16_supported(including_emulation=False)
    except TypeError:  # eski torch: parametre yok
        bf16_yerli = cap >= (8, 0)
    fp8 = cap >= (8, 9)  # FP8 icin Ada (8.9) veya Hopper (9.0) gerekiyor

    print("-" * 60)
    satir("bf16 (emulasyon dahil)", "VAR" if bf16_her else "YOK")
    satir("bf16 (YERLI/donanim)", "VAR" if bf16_yerli else "YOK  <-- fp16 kullan")
    satir("FP8 destegi", "VAR" if fp8 else "YOK  <-- FP8 kuantizasyonu calismaz")

    # Iddiayi olcumle kapat: ayni matmul, iki dtype, hangisi hizli?
    print("-" * 60)
    print("olcum: 2048x2048 matmul x20")
    for ad, dt in (("fp16", torch.float16), ("bf16", torch.bfloat16)):
        try:
            x = torch.randn(2048, 2048, device="cuda", dtype=dt)
            for _ in range(3):  # isinma
                x @ x
            torch.cuda.synchronize()
            t = time.perf_counter()
            for _ in range(20):
                x @ x
            torch.cuda.synchronize()
            sure = (time.perf_counter() - t) / 20 * 1000
            tflops = 2 * 2048**3 / (sure / 1000) / 1e12
            satir(f"  {ad}", f"{sure:.2f} ms/matmul · ~{tflops:.1f} TFLOPS")
            del x
            torch.cuda.empty_cache()
        except Exception as e:
            satir(f"  {ad}", f"CALISMADI: {type(e).__name__}")

    if not bf16_yerli:
        print("\n  >> Bu kart bf16'yi DONANIMDA yapmiyor (Turing/7.5 veya oncesi).")
        print("     Yukaridaki iki sayi arasindaki fark emulasyonun bedelidir.")
        print("     bf16 agirlikli modeller fp16'ya cevrilerek kosulmali.")
        print("     FP8 tabanli dusuk-VRAM akislari BU KARTTA CALISMAZ.")
else:
    print("\n  >> GPU YOK. --gpu bayragi verilmedi ya da hesap katmani")
    print("     hizlandirici vermedi (COLAB_SKILL: 'availability is tier-gated').")

# Sistem tarafi: CPU offload kullanacaksak RAM tavani onemli.
print("-" * 60)
try:
    ram = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 1024**3
    satir("sistem RAM", f"{ram:.1f} GB")
except (ValueError, OSError):
    satir("sistem RAM", "okunamadi")

kullanim = shutil.disk_usage("/content" if os.path.isdir("/content") else "/")
satir("disk (bos)", f"{kullanim.free / 1024**3:.1f} GB")
satir("cwd", os.getcwd())

print("=" * 60)
print("Bu ciktinin ozeti klavuzlar/02_DONANIM_VE_MALIYET.md'ye yazilir.")
