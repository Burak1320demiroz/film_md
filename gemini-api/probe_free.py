"""Erisim testi: bu anahtarla gorsel uretebiliyor muyuz?

Kademeli ve dusuk riskli: hicbir adim tek gorselden fazla uretmez ve
varsayilan olarak sadece EN UCUZ model denenir (--hepsi ile digerleri).

  Kademe 0: anahtar gecerli mi + hangi modeller goruluyor  (gorsel uretmez)
  Kademe 1: en ucuz model ile tek gorsel, 1:1, kisa prompt
  Kademe 2: --hepsi verilirse diger modeller, her biri tek gorsel

Kullanım:
    python probe_free.py [--hepsi]
"""

import pathlib
import sys

from gemini_ortak import anahtari_yukle, gorsel_bilgi, gorsel_uret, hata_yorumla

# Ucuzdan pahaliya. Varsayilan probe sadece ilkini dener.
MODELLER = [
    "gemini-2.5-flash-image",        # eski nesil, en ucuz
    "gemini-3.1-flash-lite-image",
    "gemini-3.1-flash-image",
    "gemini-3-pro-image",
]

PROMPT = "a single red apple on a white table"
KLASOR = pathlib.Path(__file__).parent / "probe_ciktilari"


def main() -> None:
    hepsi = "--hepsi" in sys.argv
    anahtari_yukle()
    from google import genai
    client = genai.Client()

    print("=== Kademe 0: anahtar + görünen modeller (görsel üretmez) ===")
    try:
        adlar = [m.name for m in client.models.list()]
        gorseller = [a for a in adlar if "image" in a]
        print(f"toplam {len(adlar)} model görünüyor")
        print("görsel modelleri:", gorseller or "HİÇBİRİ")
    except Exception as e:
        print("liste alınamadı:", hata_yorumla(e), "\n ", str(e)[:300])
        return

    denenecek = MODELLER if hepsi else MODELLER[:1]
    print(f"\n=== Kademe 1: görsel üretimi ({len(denenecek)} model, her biri 1 görsel) ===")
    KLASOR.mkdir(exist_ok=True)

    basarili = False
    for model in denenecek:
        try:
            veri = gorsel_uret(client, model, PROMPT, oran="1:1")
            hedef = KLASOR / f"probe_{model}.png"
            hedef.write_bytes(veri)
            print(f"  {model}: BAŞARILI — {gorsel_bilgi(veri)} -> {hedef.name}")
            basarili = True
        except Exception as e:
            print(f"  {model}: {hata_yorumla(e)}")
            print(f"      ham: {str(e)[:200]}")

    print("\n=== SONUÇ ===")
    if basarili:
        print("Görsel üretimi ÇALIŞIYOR. Gerçek sahne testine geçilebilir.")
    else:
        print("Üretilemedi. Yukarıdaki hata tipine göre karar ver.")
        if not hepsi:
            print("Sadece en ucuz model denendi; --hepsi ile diğerleri de denenir.")


if __name__ == "__main__":
    main()
