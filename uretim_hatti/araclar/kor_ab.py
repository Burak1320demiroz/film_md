#!/usr/bin/env python3
"""Kör A/B: denemeleri rastgele adlarla kopyala, izle, seçtikten sonra eşleşmeyi aç.

    python3 uretim_hatti/araclar/kor_ab.py karistir <dosya …> --hedef <klasör>
    python3 uretim_hatti/araclar/kor_ab.py ac <klasör>

Anahtar <klasör>/.anahtar.json'a yazılır (gizli dosya). Seçimini NOTLAR.md'ye rastgele adla
yazmadan `ac` çalıştırma — amaç, hangi prompt sürümünü izlediğini bilmeden karar vermek.
Kaynak dosyalara dokunulmaz; yalnız kopyalanır.
"""
import argparse
import json
import random
import secrets
import shutil
import sys
from pathlib import Path

ANAHTAR = ".anahtar.json"


def karistir(args):
    hedef = Path(args.hedef).expanduser()
    if (hedef / ANAHTAR).exists():
        print(f"⛔ {hedef / ANAHTAR} zaten var — başka bir hedef klasör seç")
        return 1
    kaynaklar = [Path(d).expanduser().resolve() for d in args.dosyalar]
    eksik = [str(k) for k in kaynaklar if not k.is_file()]
    if eksik:
        print("⛔ dosya yok:\n  " + "\n  ".join(eksik))
        return 1
    if len(set(kaynaklar)) != len(kaynaklar):
        print("⛔ aynı dosya iki kez verildi")
        return 1
    hedef.mkdir(parents=True, exist_ok=True)
    random.shuffle(kaynaklar)
    anahtar, kullanilan = {}, set()
    for k in kaynaklar:
        kimlik = secrets.token_hex(3)
        while kimlik in kullanilan:
            kimlik = secrets.token_hex(3)
        kullanilan.add(kimlik)
        ad = f"{kimlik}{k.suffix.lower()}"
        shutil.copy2(k, hedef / ad)
        anahtar[ad] = str(k)
    (hedef / ANAHTAR).write_text(json.dumps(anahtar, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ {len(anahtar)} dosya → {hedef}")
    for ad in sorted(anahtar):
        print(f"   {ad}")
    print("İzle, seçimini bu adlarla yaz, sonra: kor_ab.py ac", hedef)
    return 0


def ac(args):
    hedef = Path(args.hedef).expanduser()
    try:
        anahtar = json.loads((hedef / ANAHTAR).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"⛔ anahtar okunamadı: {hedef / ANAHTAR} — {e}")
        return 1
    for ad in sorted(anahtar):
        print(f"{ad}  →  {anahtar[ad]}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="kör A/B karıştırma")
    alt = ap.add_subparsers(dest="komut", required=True)
    k = alt.add_parser("karistir")
    k.add_argument("dosyalar", nargs="+")
    k.add_argument("--hedef", required=True)
    k.set_defaults(fn=karistir)
    a = alt.add_parser("ac")
    a.add_argument("hedef")
    a.set_defaults(fn=ac)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
