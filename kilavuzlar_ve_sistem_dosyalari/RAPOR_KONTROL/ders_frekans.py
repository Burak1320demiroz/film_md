#!/usr/bin/env python3
"""
ders_frekans.py — filmler arası BULGU FREKANSI (14.09.2026 · reform FAZ 4)

Ders tek koşunun değil, örüntünün üstüne yazılır (00_DERS_YAZIM_KONTRATI §2b:
ders = ≥ 2 filmde görülen örüntü + sonraki filmde değişen tek satır). Bu betik
02_HAM_RAPORLAR/<FILM>/<FILM>_<MERCEK>_HAM.md dosyalarını tarar ve üç tablo basar:

  ① VERDICT × farklı film sayısı        (NOBODY PAYS · TWO GRAVITIES · KEY WALKS …)
  ② düşük kategori (≤ 6/10) × farklı film sayısı   (SCORES SUMMARY satırlarından)
  ③ KÜME SÖZLÜĞÜ: verdict/kategori → hangi ders (D…) — dersi olmayan örüntü ADAY adayıdır

Mod D ve mod V ayrı sütunda sayılır (mod V ⑨-⑫ "plan uydurma" riski taşır [D190]);
② ③ ⑤ tasarım gereği hep V'dir. Betik DOSYA YAZMAZ — sayı tek yerde durur (sayac.sh 🔁).

Kullanım:
  python3 ders_frekans.py --ozet          # ilk 10 satır (sayac.sh çağırır)
  python3 ders_frekans.py --tam           # üç tablonun tamamı
  python3 ders_frekans.py --tam --esik 5  # düşük kategori eşiği (varsayılan 6)
"""
import re
import sys
from collections import defaultdict, Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rapor_kontrol as rk  # govde_al · alan · skor_tablosu · mercek_bul

KOK = Path(__file__).resolve().parents[1] / "FILM_QA_RAPORLARI" / "02_HAM_RAPORLAR"

VERDICT = re.compile(r"^[ \t>*]*VERDICT\s*[:：]\s*\**([^*\n]+?)\**\s*$", re.M | re.I)
OVERALL = re.compile(r"^[ \t>*]*OVERALL(?: STORY)? SCORE\s*[:：]\s*\**\s*(\d+(?:[.,]\d+)?)", re.M | re.I)
MOD = re.compile(r"INPUT MODE\s*[:：]\s*([DV])", re.I)
LEAVES = re.compile(r"^LEAVES AT\b", re.I)

# Verdict / kategori → ders. Eşleşmeyen örüntü ADAY adayıdır (sayaçta ⬜ olarak görünür).
KUME_SOZLUK = [
    (re.compile(r"NOBODY PAYS|WEIGHTLESS WORK|UNPAID", re.I),           "D206 bedel bedende ödenmiyor"),
    (re.compile(r"UNPAID RECOVERY|RESET", re.I),                         "D207 şok/yorgunluk sıfırlanması"),
    (re.compile(r"IDENTITY BREAK", re.I),                                "D208 kimlik dizisi"),
    (re.compile(r"FIELD DRIFT", re.I),                                   "D209 dünya çapası"),
    (re.compile(r"RHYME BROKEN|CREEPING DOLLY|RETURN CONSISTENCY", re.I), "D210 kafiye çifti / lockoff"),
    (re.compile(r"HOOK MISSING|LEAVES AT|EXIT BLOCKER|DELAYED START", re.I), "D211 ilk 10 s / son 10 s"),
    (re.compile(r"PACING (?:STALLED|DROPS)|SHOOT WITH TRIMS", re.I),     "D212 tempo platosu"),
    (re.compile(r"ACTION ELLIPSIS|UNREADABLE", re.I),                    "D213 aksiyon elipsi"),
    (re.compile(r"TWO GRAVITIES|PHYSICS BREAK|RATE DRIFT", re.I),        "D200 iki yerçekimi"),
    (re.compile(r"KEY WALKS|ZONE BROKEN|EXPOSURE SWINGS", re.I),         "D193 ışık takvimi"),
    (re.compile(r"THE CHOICE IS INVISIBLE|TASK WITHOUT FEELING", re.I),  "D202 seçim bedende"),
    (re.compile(r"COUNTER LOGIC", re.I),                                 "D78/D151 sayaç tek karede"),
    (re.compile(r"DELIVERY MISMATCH|AUDIBLE DRIFT|SOUNDTRACK", re.I),    "D216 ses miksi"),
    # ── ⑭ HAREKET · ⑮ YÖN (14.09.2026 · sahip talebi) — dersi henüz YOK; ≥2 filmde tekrarlayınca yazılır ──
    (re.compile(r"MOTION WITHOUT PURPOSE|PUPPET MOTION|MINOR TWITCHES|PURPOSELESS|Purpose Legibility|"
                r"Locomotion Sense|Turn & Rotation|Object Handling|Loop & Repetition|Commitment & Completion|"
                r"Body Coherence|Reaction Sense", re.I),                          "⬜ ⑭ hareket mantığı — ders yok"),
    (re.compile(r"WRONG WAY|AIMED AT NOTHING|MINOR MISAIMS|EVERY VECTOR LANDS|Target Establishment|"
                r"Look Direction|Turn & Travel|Reach & Aim|Fire · Trigger|Screen Direction Across|"
                r"Camera-Relative|Consequence on Target", re.I),                   "⬜ ⑮ yön/hedef — ders yok"),
    # ── SCORES SUMMARY kategori adları (düşük kategori tablosu) ──
    (re.compile(r"Fatigue|Recovery|Breath|Grip|Biomechanic|Strain", re.I),   "D206/D207 bedel ödenmiyor · sıfırlanma"),
    (re.compile(r"Posture|Weight of Decision|Hands as Intent|Gaze|Agency|Intent", re.I), "D202 seçim bedende"),
    (re.compile(r"Plateau|Tempo|Stillness|Escalation", re.I),                 "D212 tempo platosu"),
    (re.compile(r"Share Moment|Stakes|Cover Second|Peak Placement|Curiosity", re.I), "D211 ilk 10 s / son 10 s · HOOK §8"),
    (re.compile(r"Proportion|Scale & Measurement|Measurement", re.I),         "D138 ölçü gövde boyu cinsinden"),
    (re.compile(r"Atmosphere Honesty|Material Behaviour|Physical Consistency|Rates & Timing", re.I), "D200 iki yerçekimi / ortam kartı"),
    (re.compile(r"Depth|Parallax|Frame Edges|Emergent|Field Collapse", re.I), "D209 dünya çapası / D131 kenar"),
    (re.compile(r"Practical Source|Shadow", re.I),                            "D193 ışık takvimi"),
    (re.compile(r"SFX|Sync|Turn-Taking|Acoustic", re.I),                      "D216 ses miksi"),
    (re.compile(r"Cross-Cut|Consequence|Threat Vector|Stakes Object", re.I),  "D213 aksiyon elipsi"),
    (re.compile(r"Angle Arc|Cluster Seam|In-Clip Stability|Screen Geometry", re.I), "D210 / ACI_YAYI §3-4"),
    (re.compile(r"Creature", re.I),                                           "D2 canlı morph"),
    (re.compile(r"^Character$|Emotional Arc|Interiority|Performance|Body", re.I),  "D202/D206 seçim ve bedel bedende"),
    (re.compile(r"Structure & Pacing|Pacing|Redundan", re.I),                 "D212 tempo platosu"),
    (re.compile(r"Retention|^Hook\b|Opening|First 10", re.I),           "D211 ilk 10 s / son 10 s"),
    (re.compile(r"^Ending$|Exit|Loop", re.I),                                 "D141/D211 son kare · döngü"),
    (re.compile(r"Scale & Physics|Particle|Gravity|Ballistic|Free Fall|Momentum", re.I), "D200 iki yerçekimi / D198"),
    (re.compile(r"Spatial|Geography|Horizon|Topology|Environment|World|Background|Set & Props|Sky", re.I), "D209 dünya çapası / D174 yön"),
    (re.compile(r"^Theme|Meaning", re.I),                                     "— TEMA_MUHENDISLIGI (kılavuz)"),
    (re.compile(r"Light|Colou?r|Exposure|Key Direction|Zone", re.I),         "D193 ışık takvimi"),
    (re.compile(r"Costume|Wear|Damage|Identity|Face|Hair|Build|Helmet|Visor|Equipment|Gear", re.I), "D208 kimlik dizisi"),
    (re.compile(r"Dialogue|Voice|Audio|Sound|Speaker|Mix|Ambien|Music|Silence", re.I), "D216 ses miksi / D203 replik"),
    (re.compile(r"Camera|Cinematograph|Setup|Lockoff|Rhyme|Frame Anchor", re.I), "D210 kafiye / lockoff"),
    (re.compile(r"Premise|Clarity|Novum|Originality", re.I),                  "D157 tek kare / ONERME kılavuzu"),
    (re.compile(r"Contact|Legib|Beat|Ellipsis|Effort|Cost|Exertion|Burden|Strain", re.I), "D213 elips / D206 bedel"),
    (re.compile(r"Quantity|Counter|Count|Display|Readout", re.I),             "D78/D151 sayaç tek karede"),
    (re.compile(r"Text|Subtitle|Watermark|Negative Violations", re.I),        "D215 araç ayarı"),
    (re.compile(r"REGENERATE|STRUCTURAL PROBLEM|REVISE STRUCTURE|REWRITE PREMISE", re.I), "— genel hüküm (ders değil)"),
    (re.compile(r"HOLDS|READS|LEGIBLE|MINOR SLIPS|FIXABLE|RECOVERABLE|STAYS", re.I),      "— geçer hüküm"),
]


def kume(ad):
    for rx, d in KUME_SOZLUK:
        if rx.search(ad):
            return d
    return "⬜ dersi yok"


def tara(esik=6.0):
    verdict = defaultdict(lambda: {"D": set(), "V": set()})
    dusuk = defaultdict(lambda: {"D": set(), "V": set()})
    dosya, film_sayisi, kesik = 0, set(), 0
    disi = Counter()
    for ham in sorted(KOK.glob("**/*_HAM.md")):
        film = ham.relative_to(KOK).parts[0]
        try:
            metin = ham.read_text(encoding="utf-8")
        except Exception:
            continue
        govde0 = rk.govde_al(metin)
        if rk.kesik_mi(govde0, rk.skor_tablosu(govde0))[0]:
            kesik += 1
            continue                     # ✂️ KESİK koşu: sayılmaz (14.09.2026 FAZ 0)
        dosya += 1
        film_sayisi.add(film)
        mod = MOD.search(metin)
        mod = mod.group(1).upper() if mod else "V"      # önsöz yoksa video-only rubrik → V
        govde = rk.govde_al(metin)
        # 14.09.2026 FAZ 1: hüküm yalnız rubriğin KAPALI listesinden sayılır (rk.VERDICT_SOZLUK);
        # sözlük dışı metin ayrı sayaca düşer — ders sayımını kirletmez, ama görünür kalır
        mercek = rk.mercek_bul(govde)
        liste = rk.VERDICT_SOZLUK.get(mercek)
        for v in VERDICT.findall(govde):
            vn = rk.verdict_normal(v)
            if liste is None:                          # ⑬ / mercek okunamadı → eski yol
                if LEAVES.match(vn):
                    vn = "LEAVES AT <t>"
                verdict[vn][mod].add(film)
                continue
            kanon = None
            for k in liste:
                kn = rk.verdict_normal(k)
                if kn.startswith("LEAVES AT") and re.match(r"^LEAVES AT\s*~?\d", vn):
                    kanon = "LEAVES AT <t>"; break
                if vn == kn or vn.startswith(kn + " ") or vn.startswith(kn + " —"):
                    kanon = kn; break
            if kanon:
                verdict[kanon][mod].add(film)
            else:
                disi[(mercek, vn[:50])] += 1
        for r in rk.skor_tablosu(govde):
            if r.get("tip") == "sayi" and r.get("deger") is not None and r["deger"] <= esik:
                ad = re.sub(r"^\W+|\W+$", "", r["ad"]).strip()
                ad = re.sub(r"\s+", " ", ad)[:48]
                if ad:
                    dusuk[ad][mod].add(film)
    return verdict, dusuk, dosya, len(film_sayisi), kesik, disi


def satirla(tablo, n=None):
    rows = sorted(tablo.items(), key=lambda kv: -(len(kv[1]["D"] | kv[1]["V"])))
    if n:
        rows = rows[:n]
    out = []
    for ad, m in rows:
        top = len(m["D"] | m["V"])
        out.append(f"      {top:3d} film  (D {len(m['D']):2d} · V {len(m['V']):2d})  {ad:<44s} → {kume(ad)}")
    return out


def main():
    args = sys.argv[1:]
    esik = 6.0
    if "--esik" in args:
        esik = float(args[args.index("--esik") + 1])
    tam = "--tam" in args
    verdict, dusuk, dosya, filmler, kesik, disi = tara(esik)
    print(f"   {dosya} ham rapor · {filmler} film · ✂️ {kesik} kesik koşu sayılmadı · düşük kategori eşiği ≤ {esik:g}/10 · sayı = FARKLI film")
    if disi:
        print(f"   ⚠️ sözlük dışı hüküm {sum(disi.values())} rapor (rubriğin kapalı listesinde yok — sayılmadı; ①.13 ŞARTLI)"
              + ("" if tam else " · liste: --tam"))
    print("   ── ① VERDICT frekansı ──")
    for s in satirla(verdict, None if tam else 10):
        print(s)
    print("   ── ② düşük kategori frekansı ──")
    for s in satirla(dusuk, None if tam else 10):
        print(s)
    if tam:
        if disi:
            print("   ── ⚠️ sözlük dışı hükümler (mercek · metin · rapor sayısı) ──")
            for (m, v), n in disi.most_common(15):
                print(f"      {n:3d}  {m:14s} {v}")
        acik = sorted({ad for ad in list(verdict) + list(dusuk) if kume(ad) == "⬜ dersi yok"})
        print(f"   ── ③ dersi olmayan örüntü ({len(acik)}) — ≥ 2 filmde tekrarlıyorsa ADAY → ders (kontrat §2b) ──")
        for ad in acik:
            m = verdict.get(ad) or dusuk.get(ad)
            print(f"      {len(m['D'] | m['V']):3d} film  {ad}")


if __name__ == "__main__":
    main()
