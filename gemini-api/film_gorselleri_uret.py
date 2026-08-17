"""Bir filmin tum sahne gorsellerini prompts.json'dan toplu uretir.

Akış:
  1. promptlari_cikar.py film .md dosyasindan prompts.json uretir.
  2. Bu betik her prompt icin bir gorsel uretir, cikti klasorune yazar.
  3. Var olan dosyalar atlanir — yarida kesilirse kaldigi yerden devam eder.

Kullanım:
    python film_gorselleri_uret.py prompts.json cikti_klasoru/
    python film_gorselleri_uret.py prompts.json cikti_klasoru/ --kuru   # deneme
    python film_gorselleri_uret.py prompts.json cikti_klasoru/ --sahne 04

--kuru: API'ye hic gitmez, ne uretilecegini ve tahmini maliyeti yazar.
"""

import json
import pathlib
import sys
import time

from gemini_ortak import anahtari_yukle, gorsel_bilgi, gorsel_uret, hata_yorumla

# Gorsel basi yaklasik USD (2K civari) — sadece tahmin icin.
FIYAT = {
    "gemini-2.5-flash-image": 0.039,
    "gemini-3.1-flash-lite-image": 0.034,
    "gemini-3.1-flash-image": 0.10,
    "gemini-3-pro-image": 0.15,
}


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        sys.exit(f"Kullanım: {sys.argv[0]} prompts.json cikti_klasoru/ [--kuru]")

    kuru = "--kuru" in sys.argv
    tek = None
    if "--sahne" in sys.argv:
        tek = sys.argv[sys.argv.index("--sahne") + 1]

    plan = json.loads(pathlib.Path(args[0]).read_text(encoding="utf-8"))
    cikti = pathlib.Path(args[1])
    model = plan.get("model", "gemini-2.5-flash-image")
    oran = plan.get("oran", "9:16")
    boyut = plan.get("boyut", "2K")

    sahneler = plan["sahneler"]
    if tek:
        sahneler = [s for s in sahneler if s["id"] == tek]
        if not sahneler:
            sys.exit(f"Sahne {tek} bulunamadı.")

    yapilacak = [s for s in sahneler if not (cikti / f"{plan['film']}_{s['id']}.png").exists()]

    print(f"Film   : {plan['film']}")
    print(f"Model  : {model}   Oran: {oran}   Boyut: {boyut}")
    print(f"Sahne  : {len(yapilacak)} üretilecek, "
          f"{len(sahneler) - len(yapilacak)} zaten var")
    print(f"Tahmini: ~${len(yapilacak) * FIYAT.get(model, 0.10):.2f}\n")

    if kuru:
        for s in yapilacak:
            print(f"  [kuru] {plan['film']}_{s['id']}.png  <- {s.get('baslik','')} "
                  f"({len(s['prompt'])} karakter)")
        print("\n--kuru: hiçbir istek gönderilmedi.")
        return

    if not yapilacak:
        print("Yapılacak bir şey yok.")
        return

    anahtari_yukle()
    from google import genai
    client = genai.Client()
    cikti.mkdir(parents=True, exist_ok=True)

    basarili, basarisiz = 0, []
    for s in yapilacak:
        hedef = cikti / f"{plan['film']}_{s['id']}.png"
        try:
            veri = gorsel_uret(client, model, s["prompt"], oran, boyut)
            hedef.write_bytes(veri)
            print(f"  ✓ {hedef.name}  {gorsel_bilgi(veri)}")
            basarili += 1
        except Exception as e:
            print(f"  ✗ {hedef.name}  {hata_yorumla(e)}")
            print(f"      {str(e)[:200]}")
            basarisiz.append(s["id"])
        time.sleep(6)  # dakika basi istek sinirina takilmamak icin

    print(f"\nBitti: {basarili} üretildi, {len(basarisiz)} başarısız "
          f"{basarisiz if basarisiz else ''}")
    if basarisiz:
        print("Betiği tekrar çalıştır — mevcut dosyalar atlanır, "
              "yalnız eksikler denenir.")


if __name__ == "__main__":
    main()
