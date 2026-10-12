#!/usr/bin/env python3
"""Ham QA raporlarındaki ölümcül (🔴 BLOCKER) satırları türlerine göre kabaca sayar.

Eski hattın raporlarını YALNIZ OKUR. BILINEN_TUZAKLAR.md §B'deki sıralama bu betikten gelir.

    python3 uretim_hatti/araclar/ham_rapor_say.py            # özet tablo
    python3 uretim_hatti/araclar/ham_rapor_say.py --ornek 3  # her türden 3 örnek satır

Sınırlar (dürüst kayıt):
  · satır sayar, tekil bulgu değil — aynı hata birden çok mercekte tekrar yazılmış olabilir
  · anahtar kelime eşlemesidir; bir satır birden çok türe düşebilir, bir kısmı hiçbirine düşmez
  · raporları bir yapay zekâ yazdı; sıralama yön gösterir, kesin ölçüm değildir
"""
import argparse
import re
from collections import Counter
from pathlib import Path

KOK = Path(__file__).resolve().parents[2]
HAM = KOK / "kilavuzlar_ve_sistem_dosyalari" / "FILM_QA_RAPORLARI" / "02_HAM_RAPORLAR"

# özet/sayım satırları ("BLOCKER: 3", "SEVERITY TALLY", "BLOCKER: YOK") bulgu değildir
ATLA = re.compile(r"tally|blocker\W{0,4}\d|blocker\W{0,6}(yok|none)\b", re.I)

TURLER = {
    "el-nesne kaynaşması / içinden geçme":
        r"fuse|fusion|merg|phas|melt|kaynaş|erime|gömül|penetrat|clips? (into|through)"
        r"|passes through|extra (finger|digit)|finger",
    "ortama aykırı ses": r"audio|sound|roar|noise|\bses\b|music",
    "istenmeyen yazı / harf / rakam":
        r"\btext\b|letter|caption|subtitle|metin|yazı|label|\bhud\b|digits|numeral|title card|başlık kart",
    "duman / toz / sıvı / parçacık":
        r"dust|steam|smoke|\btoz|buhar|duman|particle|parçacık|droplet|spark|kıvılcım",
    "kask / kıyafet / ekipman kayması":
        r"helmet|kask|visor|vizör|costume|kostüm|patch|backpack|çanta|gear",
    "yerçekimine aykırı süzülme": r"gravity|yerçekim|float|hover|süzül|weightless",
    "kamera / kesme (bir kısmı rubrik önyargısı)": r"camera|kamera|\bcut\b|kesme|jump|split.?screen|angle",
    "filigran / logo": r"watermark|filigran|logo|\bicon\b",
    "klon / fazla kişi":
        r"clone|klon|duplicate (character|figure|person|astronaut)|kopya karakter"
        r"|extra (person|figure|human)|second (person|figure)|third figure",
    "beden / nesne zemine geçme":
        r"(leg|body|feet|foot|boot|wing).{0,40}(clip|phase|sink|through|terrain|floor|ground)",
    "yüz / kimlik değişimi": r"face (change|swap|morph)|identity|kimlik|different (person|face)|gender",
    "kurgu: tekrar / eksik sahne": r"\bloop\b|repeat|tekrar|recycled|missing scene|eksik sahne",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ornek", type=int, default=0, help="her türden kaç örnek satır basılsın")
    a = ap.parse_args()

    satirlar, klasorler = [], set()
    for f in sorted(HAM.rglob("*.md")):
        for s in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            if "BLOCKER" in s and not ATLA.search(s):
                satirlar.append(s.strip())
                klasorler.add(f.relative_to(HAM).parts[0])

    say, ornek, bos = Counter(), {k: [] for k in TURLER}, 0
    for s in satirlar:
        kucuk, isabet = s.lower(), False
        for tur, desen in TURLER.items():
            if re.search(desen, kucuk):
                say[tur] += 1
                isabet = True
                if len(ornek[tur]) < a.ornek:
                    ornek[tur].append(s[:200])
        bos += not isabet

    print(f"kaynak: {HAM.relative_to(KOK)}")
    print(f"film klasörü: {len(klasorler)} · 🔴 satırı: {len(satirlar)}\n")
    for tur, n in say.most_common():
        print(f"{n:5d}  {tur}")
        for o in ornek[tur]:
            print(f"         · {o}")
    print(f"{bos:5d}  hiçbir türe düşmedi")


if __name__ == "__main__":
    main()
