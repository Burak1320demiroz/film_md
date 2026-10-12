"""Bütün ham raporlar (geçersizler dahil): 🔴/🟠 bulgu satırları → tür · mercek · geçerlilik."""
import re, sys, collections, json
from pathlib import Path
sys.path.insert(0, "/Users/dai/github/apex_md/film_md/kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL")
import qa_saglik as q

ATLA = re.compile(r"tally|sayım|legend|lejant|severity\s*:|🔴\s*[=:]|🔴\s*\d|\d\s*🔴|🔴\s*blocker\s*[=:/]|"
                  r"blocker\s*\W{0,4}\d|category\s*[|/]\s*score|critical issues?\s*\|?\s*$|lines heard|(yok|none)\s*$|🔴 ?/ ?🟠|🔴 BLOCKER ·|^\|?\s*[-:| ]+\|?$", re.I)
KIRMIZI = re.compile(r"🔴|\bBLOCKER\b|\bCRITICAL\b|\bKritik\b", re.I)
TURUNCU = re.compile(r"🟠|\bMAJOR\b|\bHIGH\b|\bORTA\b|\bMedium\b", re.I)

# öncelik sırasıyla tek ana tür
TURLER = [
 ("filigran/logo", r"watermark|filigran|\blogo\b"),
 ("istenmeyen yazı", r"\btext\b|letter|caption|subtitle|\bmetin\b|\byazı|stencil|\bhud\b|digits?\b|numeral|glyph|title card|başlık kart"),
 ("klon/fazla kişi", r"clone|klon|duplicate|extra (person|figure|human|astronaut)|second (person|figure|astronaut)|third figure|ghost|fazla kişi|ikinci (kişi|figür)"),
 ("hareket: kayma/hayalet tutuş", r"slid(e|es|ing)\b|moonwalk|skat|glid|phantom|grasp(ing|s)? (empty )?air|teleport|\bkayar|kayma\b|foot ?slid|SLIDE|PHANTOM"),
 ("el-nesne kaynaşması", r"fuse|fusion|fused|merg|phas|melt|kaynaş|\berim|gömül|penetrat|clips? (into|through)|pass(es)? through|içinden geç|extra (finger|digit)|six fingers|interpenetrat|clipping"),
 ("zemine geçme", r"(leg|body|feet|foot|boot|knee|wheel).{0,40}(sink|through|into the|terrain|floor|ground|zemin)"),
 ("ortama aykırı ses", r"audio|sound|roar|noise|\bses\b|music|müzik|whoosh|hiss|thud|clank|silence|sessiz"),
 ("parçacık/duman/toz", r"dust|steam|smoke|\btoz|buhar|duman|particle|parçacık|droplet|spark|kıvılcım|haze|debris|plume|vapou?r|fog|sis"),
 ("yerçekimi/süzülme", r"gravity|yerçekim|float|hover|süzül|weightless|buoyan|slow.?mo|m/s"),
 ("kütle/momentum", r"\bmass\b|momentum|inertia|kütle|ivme|weightless object|lacks (realistic )?(weight|mass)"),
 ("efor/beden", r"effort|efor|effortless|strain|weight(less)? (of|lift)|heavy|ağır|stamina|recoil|flinch|resistance|direnç|fatigue|yorgun|exertion"),
 ("kask/giysi/ekipman", r"helmet|kask|visor|vizör|suit|giysi|costume|kostüm|patch|backpack|çanta|\bgear|glove|eldiven|harness|strap|kayış|tether|sling|askı|cuff|bracelet|bileklik|sleeve|kol band|armband|ekipman|equipment|tool|alet"),
 ("yüz/kimlik", r"\bface\b|yüz\b|identity|kimlik|different (person|face)|gender|skin|ten\b"),
 ("ışık", r"light|ışık|shadow|gölge|bloom|glow|exposure|pozlama|lens flare|key light|anahtar ışık|o.?clock|practical|colou?r temp|renk sıcak|power trip"),
 ("yön/180°", r"180|screen.?(left|right)|eksen|axis|direction|yön\b|flip|mirror(ed)?"),
 ("kamera/kesme/kadraj", r"camera|kamera|\bcut\b|kesme|jump|split.?screen|angle|açı|framing|kadraj|zoom|pan\b|dolly|dissolve"),
 ("arka plan/dünya", r"background|arka plan|sky|gök|horizon|ufuk|planet|gezegen|terrain|arazi|environment|ortam|set\b|wall|duvar|room|oda"),
 ("sayı/nesne sayısı", r"count|sayı|number of|\bkaç\b|bolts?|cıvata"),
 ("hikâye/anlatım/kurgu", r"story|hikâye|hikaye|stakes|bedel|goal|amaç|ending|son\b|loop|repeat|tekrar|recycled|pacing|ritim|plot|clarity|confus|motivation|replace the|consequence|scene \d+:"),
 ("oyunculuk", r"acting|oyunculuk|performance|emotion|duygu|gesture|jest|posture|duruş|reaction|tepki|stiff|central choice|on the body|bodily|expression"),
]
TURLER = [(a, re.compile(b, re.I)) for a, b in TURLER]
TC = re.compile(r"\b(\d{1,2}):(\d{2})\b")

def tur_bul(s):
    for ad, d in TURLER:
        if d.search(s):
            return ad
    return "diğer"

def grup(karar):
    if karar == "KESİK": return "KESİK"
    if karar in ("GO", "ŞARTLI"): return "GO/ŞARTLI"
    return "TEKRAR/GEÇERSİZ"

hepsi, _ = q.tara()
satir = []
for r in hepsi:
    karar = r.get("karar_tekil") or r["karar"]
    g = grup(karar)
    metin = Path(r["yol"]).read_text(encoding="utf-8", errors="replace")
    gorulen = set()
    for s in metin.splitlines():
        s2 = s.strip()
        if len(s2) < 25 or ATLA.search(s2):
            continue
        k = "🔴" if KIRMIZI.search(s2) else ("🟠" if "🟠" in s2 else None)
        if not k:
            continue
        tc = TC.search(s2)
        anahtar = (tc.group(0) if tc else s2[:50], tur_bul(s2))
        if anahtar in gorulen:
            continue
        gorulen.add(anahtar)
        satir.append(dict(film=r["film"], mercek=r["mercek"], grup=g, sid=k, tur=anahtar[1],
                          tc=tc.group(0) if tc else None, s=s2[:300]))

json.dump(satir, open(Path(__file__).with_name("korpus.json"), "w"), ensure_ascii=False)
C = collections.Counter
print(f"rapor {len(hepsi)} · bulgu satırı {len(satir)} (🔴 {sum(x['sid']=='🔴' for x in satir)} · 🟠 {sum(x['sid']=='🟠' for x in satir)})")
print("geçerlilik:", dict(C(r_grp for r_grp in (grup(r.get('karar_tekil') or r['karar']) for r in hepsi))))
print("bulgu/geçerlilik:", dict(C(x["grup"] for x in satir)))
print("\n── tür (🔴 · 🟠 · film sayısı) ──")
for t, n in C(x["tur"] for x in satir).most_common():
    k = sum(1 for x in satir if x["tur"] == t and x["sid"] == "🔴")
    f = len({x["film"] for x in satir if x["tur"] == t and x["sid"] == "🔴"})
    gg = C(x["grup"] for x in satir if x["tur"] == t)
    print(f"{n:5d}  🔴{k:4d} 🟠{n-k:4d}  🔴film {f:2d}  {t:24s} geçerli%{100*gg['GO/ŞARTLI']//max(n,1):3d}")
print("\n── mercek ──")
for m, n in C(x["mercek"] for x in satir).most_common():
    top = C(x["tur"] for x in satir if x["mercek"] == m).most_common(3)
    print(f"{n:5d}  {str(m):14s} {top}")
print("\n── film (🔴) ──")
for f, n in C(x["film"] for x in satir if x["sid"] == "🔴").most_common(15):
    print(f"{n:5d}  {f}")
