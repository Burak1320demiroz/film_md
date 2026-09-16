#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#  doluluk_olcum.py — 22_ dosyasının teşhis kesiti (15.09.2026)
#  Sorun: 10 s'lik sahnede eylem ~3 s'de bitiyor, kalan saniyeler boş.
#  Bu betik DEPODAKİ VİDEO PROMPTLARINI tarar (üretilmiş klibi değil):
#  TIMELINE'ın son vuruşu durgunluk kelimesi mi taşıyor, t ≥ 5 s
#  vuruşlarında fiil var mı, son güçlü fiil kaçıncı saniyede.
#  Kaba bir kesittir; kural değildir. Koşu: depo kökünden
#     python3 kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/doluluk_olcum.py
#  Üretilmiş klibin saniye başına hareket enerjisi bu betiğin işi DEĞİL —
#  o, TUR 19 sonrası kurulacak makine kapısının (hareket profili) işidir.
# ═══════════════════════════════════════════════════════════════════
import re, glob, collections, sys, os

KOK = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(KOK)
files = (glob.glob("yatay_*/*/*_BOLUM_*.md") + glob.glob("yatay_*/*/*_FILM.md")
         + glob.glob("yatay_*/*/FAZ_*/*.md") + glob.glob("dikey_shorts_filmler/*/*.md"))
vp = []
for f in files:
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r"🎥 V[İI]DEO PROMPT[^\n]*\n+```[^\n]*\n(.*?)```", t, re.S):
        vp.append((f, m.group(1)))

DURGUN = re.compile(r"\b(then stops|stops|holds?|stays?|still|motionless|does not move|do not move|"
                    r"remains?|rests?|freezes?|waits?|nothing else (in frame )?moves|settles?|"
                    r"no other movement|unmoving|static)\b", re.I)
GUCLU = re.compile(r"\b(pulls?|pushes?|turns?|grabs?|lifts?|drops?|throws?|climbs?|runs?|steps?|reaches?|"
                   r"opens?|closes?|slams?|strikes?|cuts?|seals?|kicks?|jumps?|falls?|drags?|hauls?|swings?|"
                   r"fires?|presses?|twists?|pries|pry|rips?|tears?|crosses?|walks?|crawls?|leans?|kneels?|"
                   r"rises?|stands? up|sits? down)\b", re.I)
KALIP = ["motionless", "stands still", "nothing else moves", "holds still", "stays still",
         "then stops", "nothing else in frame moves", "remains still", "frozen in place"]
BEAT = re.compile(r"(\d+(?:[.,]\d+)?)\s*s\s*[—–-]+\s*([^\n]*?)(?=(?:\s\d+(?:[.,]\d+)?\s*s\s*[—–-])|$)")

def zaman_blogu(p):
    m = re.search(r"TIMELINE:?(.*?)(?:\n\n|\nCAMERA|\nPHYSICS|\nAUDIO|\nNEGATIVE|$)", p, re.S)
    if m: return m.group(1)
    m = re.search(r"MOTION \([^)]*\):(.*?)(?:\n\n|\[PHYSICS|$)", p, re.S)
    return m.group(1) if m else None

bicim = collections.Counter(); son_durgun = n_beat = gec_toplam = gec_durgun = 0
son_fiil = collections.Counter(); kalip = collections.Counter()
for f, p in vp:
    if re.search(r"TIMELINE", p): bicim["TIMELINE:"] += 1
    elif re.search(r"MOTION \(", p): bicim["MOTION (…):"] += 1
    elif re.search(r"\b\d+\s*s\s*[—–-]", p): bicim["çıplak 0s —"] += 1
    elif re.search(r"\b\d+\s*-\s*\d+\s*s\b|\bat \d+ ?s\b", p, re.I): bicim["aralık / at n s"] += 1
    else: bicim["zaman damgasız düzyazı"] += 1
    for k in KALIP:
        if k in p.lower(): kalip[k] += 1
    blok = zaman_blogu(p)
    if not blok: continue
    bs = BEAT.findall(blok.replace("\n", " "))
    if not bs: continue
    n_beat += 1
    if DURGUN.search(bs[-1][1]): son_durgun += 1
    ts = []
    for t, txt in bs:
        tt = float(t.replace(",", "."))
        if tt >= 5:
            gec_toplam += 1
            if DURGUN.search(txt): gec_durgun += 1
        if GUCLU.search(txt): ts.append(tt)
    if ts: son_fiil["≥8 s" if max(ts) >= 8 else ("5-8 s" if max(ts) >= 5 else "<5 s")] += 1
    else: son_fiil["güçlü fiil yok"] += 1

def yz(a, b): return f"{a} ({100*a/max(b,1):.0f}%)"
print(f"video prompt: {len(vp)} · dosya: {len(set(f for f,_ in vp))} · biçim: " +
      " · ".join(f"{k} {v}" for k, v in bicim.most_common()))
print(f"vuruş satırı ayrıştırılan prompt: {n_beat}")
print(f"  son vuruşu durgunluk kelimesi taşıyan: {yz(son_durgun, n_beat)}")
print(f"  t ≥ 5 s vuruşları: {gec_toplam} · durgunluk kelimeli: {yz(gec_durgun, gec_toplam)}")
print("  son güçlü gövde fiilinin zamanı: " + " · ".join(f"{k} {yz(v, n_beat)}" for k, v in
      sorted(son_fiil.items(), key=lambda x: ["<5 s","5-8 s","≥8 s","güçlü fiil yok"].index(x[0]))))
print("durgunluk kalıbı geçen prompt: " + " · ".join(f"\"{k}\" {v}" for k, v in kalip.most_common() if v))
