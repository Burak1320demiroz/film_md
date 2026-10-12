"""Bütün filmlerin görsel/video promptları — mekanik kusur taraması (salt okuma)."""
import re, collections, statistics, json
from pathlib import Path

KOK = Path("/Users/dai/github/apex_md/film_md")
klasorler = sorted(p for p in KOK.glob("yatay_*_filmler/*") if p.is_dir()) + \
            sorted(p for p in KOK.glob("dikey_*/*") if p.is_dir()) + \
            sorted(p for p in (KOK / "kilavuzlar_ve_sistem_dosyalari/ARSIV").glob("yatay_*_filmler/*") if p.is_dir())

BLOK = re.compile(r"###[^\n]*(GÖRSEL|VİDEO|VIDEO|IMAGE)[^\n]*\n+```[^\n]*\n(.*?)```", re.S | re.I)
IZINLI = set("IN FRAME CAMERA PHYSICS AUDIO NEGATIVE TIMELINE START FRAME END OUTPUT CONTINUOUS ACTION SUBJECT "
             "SCENE STYLE LIGHTING LIGHT SETTING SHOT ACTION ENVIRONMENT DIALOGUE VOICE MOOD COLOR LENS "
             "FRAMING MOTION SOUND HDR CGI NASA ISS LED UV HUD EVA".split())

def kontroller(t):
    k = t.lower()
    c = {}
    c["meta: Scene n of N"] = bool(re.search(r"\bscene \d+ of \d+", k))
    c["meta: S07/R3/K12/PHASE etiketi"] = bool(re.search(r"\b(S\d{2}|R\d|K\d{2}|PHASE \d|C\d{2}|Z\d\.\d)\b", t))
    jeton = [w for w in re.findall(r"\b[A-Z]{3,}\b", t) if w not in IZINLI]
    c["büyük harfli jeton"] = bool(jeton)
    c["Türkçe kelime prompt içinde"] = bool(re.search(r"[çğışöüÇĞŞÖÜ]|\b(YOK|TEK|SAYIYLA|YAZILMAZ|KONUM|KANITI|VURUS|sahne|klip|kurulum)\b|<[a-zçğışöü_ ]+>|⬜", t))
    c["ekran kelimesi büyük harfle (WARNING/ERROR…)"] = bool(re.search(r"\b(WARNING|ERROR|OVERLOAD|ALERT|DANGER|CRITICAL|TELEMETRY|OXYGEN|LOW|FAIL\w*)\b", t))
    c["video promptunda IMAGE prompt atfı"] = bool(re.search(r"IMAGE prompt|image prompt", t))
    c["çelişki: yüz gizli ↔ cam berrak/okunur"] = bool(re.search(r"conceal\w* (the |his |her )?(human )?face|face (is |stays |remains )?(hidden|concealed|invisible)|opaque visor|(gold|mirror)[- \w]{0,25}reflective visor|mirrored visor", k) and
                                                      re.search(r"optically clear|fully readable|clear glass|see[- ]through|visible face|face visible", k))
    c["çelişki: deri yok ↔ 'real skin pores'"] = bool(re.search(r"no bare skin", k) and re.search(r"skin pores", k))
    c["çelişki: ekran/okuma ↔ metin yasağı"] = bool(re.search(r"\b(display|monitor|readout|gauge|timer|hud|countdown|screen(?![- ](left|right|edge|space)))\b(?!-)", k.split("negative")[0])
                                                  and re.search(r"no (readable )?text|no letters|no digits", k))
    vakum = re.search(r"vacuum|airless", k)
    audio = re.search(r"audio:([^\n]*)", k)
    c["vakum + AUDIO'da dış ses tarifi"] = bool(vakum and audio and re.search(
        r"roar|hiss|whoosh|rumble|boom|crunch|wind|thunder|blast|scrape", audio.group(1)) and
        not re.search(r"through the (suit|helmet|glove|boot|chest)|transmitted|inside the helmet|no exterior", audio.group(1)))
    c["zihinsel/soyut fiil"] = bool(re.search(r"\b(realiz(e|es|ing)\b|realis(e|es|ing)\b|remember|decid|understand|hopes?|feels?|thinks?|knows?|wonders|regret|fear)\w*\b",
                                              k.split("negative")[0]))
    neg = re.search(r"negative:(.*)", t, re.S | re.I)
    c["_neg_len"] = len(neg.group(1)) if neg else 0
    c["_len"] = len(t)
    tl = re.findall(r"^\s*\d+(\.\d+)?s?\s*[-–]\s*\d+(\.\d+)?s", t, re.M)
    c["_tl_adim"] = len(tl)
    c["_neg_metni"] = neg.group(1).strip()[:2000] if neg else ""
    c["_jeton"] = jeton[:5]
    return c

satir = []
for d in klasorler:
    dosyalar = sorted(d.glob("*_BOLUM_*.md")) or sorted(d.glob("*_PROMPT*.md"))
    ps = []
    for f in dosyalar:
        for m in BLOK.finditer(f.read_text(encoding="utf-8", errors="replace")):
            tur = "video" if re.search(r"VİDEO|VIDEO", m.group(1), re.I) else "gorsel"
            ps.append((tur, m.group(2)))
    if not ps:
        continue
    cs = [kontroller(t) for _, t in ps]
    negler = collections.Counter(c["_neg_metni"] for c in cs if c["_neg_metni"])
    en_sik_neg = negler.most_common(1)[0][1] if negler else 0
    r = dict(film=d.name, format=d.parent.name, prompt=len(ps),
             ort_len=int(statistics.mean(c["_len"] for c in cs)),
             neg_pay=round(sum(c["_neg_len"] for c in cs) / max(1, sum(c["_len"] for c in cs)), 2),
             neg_ayni=round(en_sik_neg / len(cs), 2),
             tl_adim=round(statistics.mean(c["_tl_adim"] for (t, _), c in zip(ps, cs) if t == "video") if any(t == "video" for t, _ in ps) else 0, 1))
    for key in cs[0]:
        if not key.startswith("_"):
            r[key] = sum(1 for c in cs if c[key])
    r["jeton_ornek"] = sorted({j for c in cs for j in c["_jeton"]})[:8]
    satir.append(r)

json.dump(satir, open(Path(__file__).with_name("prompt_denetim.json"), "w"), ensure_ascii=False, indent=1)
anahtarlar = [k for k in satir[0] if k not in ("film", "format", "prompt", "ort_len", "neg_pay", "neg_ayni", "tl_adim", "jeton_ornek")]
print(f"film {len(satir)} · prompt {sum(r['prompt'] for r in satir)} · ort uzunluk {int(statistics.mean(r['ort_len'] for r in satir))} kr")
print(f"NEGATIVE payı ortanca {statistics.median(r['neg_pay'] for r in satir)} · aynı NEGATIVE bloğu ortanca {statistics.median(r['neg_ayni'] for r in satir)}")
for k in anahtarlar:
    f = [r for r in satir if r[k]]
    print(f"{k:42s} film {len(f):3d}/{len(satir)} · prompt {sum(r[k] for r in satir):5d}")
print()
print(f"{'film':24s} {'n':>4s} {'uzun':>5s} {'NEG%':>5s} {'aynı':>5s} {'TL':>4s} " + " ".join(f"{i+1:>3d}" for i in range(len(anahtarlar))))
for r in sorted(satir, key=lambda r: r["film"]):
    print(f"{r['film'][:24]:24s} {r['prompt']:4d} {r['ort_len']:5d} {r['neg_pay']:5.2f} {r['neg_ayni']:5.2f} {r['tl_adim']:4.1f} " +
          " ".join(f"{r[k]:3d}" for k in anahtarlar))
print("sütunlar:", {i + 1: k for i, k in enumerate(anahtarlar)})
