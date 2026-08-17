"""Gemini API ile tek gorsel uretir (hizli deneme icin).

Kullanım:
    python ornek_uret.py "prompt metni" [cikti.png] [--oran 9:16]
"""

import argparse

from gemini_ortak import anahtari_yukle, gorsel_bilgi, gorsel_uret, hata_yorumla

MODEL = "gemini-3.1-flash-image"  # Nano Banana 2


def main() -> None:
    p = argparse.ArgumentParser(description="Gemini ile görsel üret")
    p.add_argument("prompt")
    p.add_argument("cikti", nargs="?", default="cikti.png")
    p.add_argument("--oran", default="9:16", help="1:1, 9:16, 16:9, 21:9 ...")
    p.add_argument("--model", default=MODEL)
    args = p.parse_args()

    anahtari_yukle()
    from google import genai
    client = genai.Client()

    try:
        veri = gorsel_uret(client, args.model, args.prompt, args.oran)
    except Exception as e:
        raise SystemExit(f"{hata_yorumla(e)}\n{str(e)[:300]}")

    with open(args.cikti, "wb") as f:
        f.write(veri)
    print(f"Yazıldı: {args.cikti}  {gorsel_bilgi(veri)}")


if __name__ == "__main__":
    main()
