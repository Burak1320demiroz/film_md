"""Film .md dosyasindan gorsel promptlarini cekip prompts.json uretir.

Depodaki film dosyalari duzenli bir yapida: her sahne "## SAHNE N — BASLIK"
basligiyla acilir, altinda "### GORSEL PROMPT" ve uc tirnakli blok gelir.
Bu betik o bloklari oldugu gibi cikarir — prompt metnine dokunmaz.

Kullanım:
    python promptlari_cikar.py ../dikey_shorts_filmler/THE_FIRST_MORNING_DIKEY_SHORTS.md
    python promptlari_cikar.py <film.md> [cikti.json] [--boyut 2K]
"""

import json
import pathlib
import re
import sys

SAHNE_BASLIK = re.compile(r"^##\s*\S*\s*SAHNE\s+(\S+)\s*[—-]\s*(.+?)\s*$", re.M)
GORSEL_BASLIK = re.compile(r"^###\s*\S*\s*GÖRSEL PROMPT\s*$", re.M)
BLOK = re.compile(r"^```\s*\n(.*?)^```", re.M | re.S)


def oran_bul(metin: str) -> str:
    bas = metin[:800]
    if "9:16" in bas:
        return "9:16"
    if "16:9" in bas:
        return "16:9"
    return "9:16"


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(f"Kullanım: {sys.argv[0]} <film.md> [cikti.json] [--boyut 2K]")

    kaynak = pathlib.Path(args[0])
    metin = kaynak.read_text(encoding="utf-8")
    cikti = pathlib.Path(args[1]) if len(args) > 1 else \
        pathlib.Path(__file__).parent / "prompts.json"
    boyut = "2K"
    for a in sys.argv[1:]:
        if a.startswith("--boyut"):
            boyut = a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]

    basliklar = list(SAHNE_BASLIK.finditer(metin))
    if not basliklar:
        sys.exit("Sahne başlığı bulunamadı — dosya yapısı beklenenden farklı.")

    sahneler = []
    for i, m in enumerate(basliklar):
        son = basliklar[i + 1].start() if i + 1 < len(basliklar) else len(metin)
        bolum = metin[m.start():son]

        g = GORSEL_BASLIK.search(bolum)
        if not g:
            print(f"  ! SAHNE {m.group(1)}: görsel promptu yok, atlandı")
            continue
        b = BLOK.search(bolum, g.end())
        if not b:
            print(f"  ! SAHNE {m.group(1)}: prompt bloğu okunamadı, atlandı")
            continue

        sahneler.append({
            "id": m.group(1).zfill(2),
            "baslik": m.group(2),
            "prompt": b.group(1).strip(),
        })

    plan = {
        "film": kaynak.stem.replace("_DIKEY_SHORTS", "").replace("_YATAY_SHORTS", ""),
        "kaynak": str(kaynak),
        "oran": oran_bul(metin),
        "boyut": boyut,
        "model": "gemini-3.1-flash-image",
        "sahneler": sahneler,
    }
    cikti.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"{plan['film']}: {len(sahneler)} sahne, {plan['oran']}, {boyut} -> {cikti}")
    for s in sahneler:
        print(f"  {s['id']}  {s['baslik'][:45]:<45} {len(s['prompt']):>5} karakter")


if __name__ == "__main__":
    main()
