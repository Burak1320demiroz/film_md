# -*- coding: utf-8 -*-
import re, sys, importlib, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

OUT = "/Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_STOLEN_SKY"
BOLUM_ADI = {1:"GÖKYÜZÜ KAPANDI",2:"KULEYİ ELE GEÇİRMEK",3:"ALÇAKTAN GİT",4:"DÜŞMANIN KAPISI",
             5:"DÖRT KİŞİDEN ÜÇE",6:"GÜÇ EL DEĞİŞTİRİYOR",7:"KARŞI SALDIRI",8:"BİR DAKİKALIK GÖKYÜZÜ"}
SINIR = {1:"S11 (C · MCU · OTS) ↔ S12 (A · WS · low angle) · 2 kademe · mekân değişir ✅",
         2:"S23 (T · WS · pan) ↔ S24 (H · MLS · rear-quarter tracking) · açı tipi değişir · ⛔ PART 1|2 sınırı — SPEC B elle kare ✅",
         3:"S35 (O · MLS · from behind) ↔ S36 (F · MLS · eye level) · açı tipi değişir ✅",
         4:"S47 (E · WS · high angle) ↔ S48 (E · küme S47) · Z muaf · ⛔ PART 2|3 sınırı — SPEC B elle kare ✅",
         5:"S59 (R · MS · through mesh) ↔ S60 (J · MS · low angle push-in) · açı tipi + mekân değişir (bilinçli şok) ✅",
         6:"S71 (B · MS · eye level) ↔ S72 (B · küme S71) · Z muaf · ⛔ PART 3|4 sınırı — SPEC B elle kare ✅",
         7:"S83 (F · MLS · eye level) ↔ S84 (L · MCU · low angle) · 1,5 kademe ✅",
         8:"S95 son sahne — kafiye S00 (aynı harf A, aynı CAMERA cümlesi)"}

def words(txt):
    return len(re.findall(r"[A-Za-z0-9'’\-\.]+", txt))

def zaman(n):
    t = n*10
    return f"{t//60}:{t%60:02d},0"

def header(b, first, last):
    return f"""# 🎬 THE_STOLEN_SKY — BÖLÜM {b}  (S{first} – S{last}) · {BOLUM_ADI[b]}

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `THE_STOLEN_SKY_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ —
> her prompt tek başına çalışır (AGENTS §2 kural ③). ⭐ self-contained ≠ Bible'ın
> tamamı — yalnız `IN FRAME:` satırındaki tarif edilir [D214].
>
> ⭐ **YENİ REJİM:** ilk satır `IN FRAME:` (㉖) · POZİTİF gövde IMAGE 100-250 / VIDEO 120-300 kelime (①) ·
> NEGATIVE = §5.1 çekirdek (image 7 · video 8) + ≤3 sahneye özel (㉗) · video tek satır `START FRAME:`.
> ⭐ **OMNI 1.1 Flash I2V katmanı:** CAMERA `In a single continuous shot.` ile biter · PHYSICS + AUDIO her klipte dolu · tırnak 0.
> ⭐ **Promptta `Scene n of 96` = S + 1.** Dönüş ve küme işaretleri de bu numarayı kullanır.
> ⭐ **VİZÖR TAMAMEN OPAK** (SAPMA 3) — `IN FRAME:` satırına `face` YAZILMAZ, D79 vizör cümlesi HİÇ girmez.
> ⭐ **KÜME (Z) klipleri:** imaj promptu önceki klibin SON KARESİNİ tarif eder; üretimde OMNI zincirine
>   gerçek son kare verilir, imaj promptu yalnız yedek/animatik içindir (Z: S13 S35 S37 S41 S48 S49 S72 S74 S82 S90).
> ⭐ **YÖN NESNE-GÖRELİ** [D174]: pusula ve ekran koordinatı yok — halka/kafes konumu kadrajdaki nesneye göre yazılır.
> ⛔ İnsansız sahnelerde NEGATIVE kısadır (<900 karakter) ve "no human figures" kalıbı YAZILMAZ [KART 10].
> ⛔ Replikler klipte ÜRETİLMEZ (post-dub, 8 replik); saniyesi sahne bilgi bloğunda, promptta değil.
> ⛔ Silah ADLANDIRILMAZ (short tool · long tool · a short burst of four bright points); kan · yara · ceset 0 kelime [KART 12].
>
> Bölüm sınırı ardışık bir çifttir: {SINIR[b]}
> Denetim klasör modunda: `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_16_dk_filmler/THE_STOLEN_SKY`

---
"""

LAST = {}
def render_scene(s):
    n = s["n"]; L = s["L"]
    if s.get("Z"):
        kind, ref = "kume", n-1
    elif L in LAST:
        kind, ref = "donus", LAST[L]
    else:
        kind, ref = "ilk", None
    LAST[L] = n
    isa = isaret(kind, ref)
    isa_tr = {"ilk":"ilk kullanım","donus":f"dönüş S{ref:02d}" if ref is not None else "", "kume":f"küme (Z) S{ref:02d}" if ref is not None else ""}[kind]
    cam = f"CAMERA: {CAM[L]}." + (f" {isa}" if isa else "") + " In a single continuous shot."
    vol = s["vol"]
    vol_tr = "→".join(vol) if isinstance(vol, tuple) else vol
    humans = s.get("humans", 0); veyra = s.get("veyra", 0)
    short = (humans == 0 and veyra == 0 and s.get("short_neg", True))
    inframe = s["inframe"]
    replik = s.get("replik", "—")
    # 20.09.2026 · ölçüldü: S02·S35·S47·S72'de figür klip
    # İÇİNDE giriyor — t=0 karesinde yokken IMAGE NEGATIVE "exactly N tall figures" diyordu
    # (model yazılanı kadraja sokar, D214). humans_img / veyra_img yalnız imaj sayısını ezer.
    humans_img = s.get("humans_img", humans); veyra_img = s.get("veyra_img", veyra)
    short_img = (humans_img == 0 and veyra_img == 0 and s.get("short_neg", True))
    img_neg = negative(False, humans_img, veyra_img, s.get("neg", []), short_img)
    vid_neg = negative(True, humans, veyra, s.get("neg", []), short)

    tl = " ".join(f"{t:.1f}s — {txt}" for t, txt in s["timeline"])
    back = s.get("back_of")
    back_line = ""
    if back:
        b0 = CH[back]["back"]
        back_line = "\n" + b0[0].upper() + b0[1:] + "."
    if s.get("hull_back"):
        back_line = "\nThe craft's tail is one continuous flat surface carrying only its engine rings."
    import re as _re
    assert not _re.search(r"\b(floor|ground|walls?)\b", s["light"], _re.I), (n, "LIGHT yüzey adı [D176]")
    TOW = _re.compile(r"\b(runs?|running|walks?|walking|moves?|moving|heading|drives?|driving|flies|flying|approach(?:es|ing)?|sprints?|sprinting|marches|marching|strides?|striding|advances?|advancing|races?|racing|climbs?|climbing|crawls?|crawling)\b[^.;]{0,60}?\btowards?\b", _re.I)
    for k in ("img_lock","img_body","vid_lock"):
        if TOW.search(s[k]): print(f"⚠️  S{n:02d} çapasız toward ({k})")
    if TOW.search(tl): print(f"⚠️  S{n:02d} çapasız toward (timeline)")
    POL = _re.compile(r"\b(body|bodies|dead|death|smoke|blood|kill|killed|corpse|wound|gore|weapon|gun|rifle|bullet|shoot)\b", _re.I)
    for k in ("img_lock","img_body","vid_lock","light","audio"):
        m = POL.findall(s.get(k,""))
        if m: print(f"⚠️  S{n:02d} politika kelimesi {sorted(set(x.lower() for x in m))} ({k})")
    m = POL.findall(tl)
    if m: print(f"⚠️  S{n:02d} politika kelimesi {sorted(set(x.lower() for x in m))} (timeline)")
    for ng in s.get("neg", []):
        m = POL.findall(ng)
        if m: print(f"⚠️  S{n:02d} politika kelimesi {sorted(set(x.lower() for x in m))} (neg)")
    ARK = _re.compile(r"behind\s+(her|him|them)\b|from\s+behind|seen\s+from\s+(the\s+)?(back|rear)", _re.I)
    if not s.get("back_of") and not s.get("hull_back"):
        for k in ("img_lock","img_body","vid_lock"):
            if ARK.search(s[k]): print(f"⚠️  S{n:02d} kamera-arkada imzası ama back_of yok ({k})")
        if ARK.search(tl): print(f"⚠️  S{n:02d} kamera-arkada imzası ama back_of yok (timeline)")
    PUS = _re.compile(r"\b(north|south|east|west)\b", _re.I)
    for k in ("img_lock","img_body","vid_lock","light"):
        if PUS.search(s[k]): print(f"⚠️  S{n:02d} pusula kelimesi ({k})")
    if PUS.search(tl): print(f"⚠️  S{n:02d} pusula kelimesi (timeline)")
    img = f"""IN FRAME: {inframe}
Scene {n+1} of {TOTAL}.
{s['img_lock']}

{s['img_body']}
LIGHT: {s['light']}
{cam}
NEGATIVE: {img_neg}

Output: 16:9, 4K, no text, no watermark."""
    vid = f"""IN FRAME: {inframe}
Scene {n+1} of {TOTAL}. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it, nothing re-described.
{s['vid_lock']}{back_line}

TIMELINE: {tl}

{cam}
{physics(vol)}
{audio(vol, s.get('audio',''))}
NEGATIVE: {vid_neg}

Output: 16:9, no text, no watermark."""

    # kelime bandı (POZİTİF gövde: NEGATIVE ve Output hariç)
    def body_words(p):
        return len(p.split("NEGATIVE:")[0].split())
    iw, vw = body_words(img), body_words(vid)
    s["_iw"], s["_vw"] = iw, vw
    if not (100 <= iw <= 250): print(f"⚠️  S{n:02d} IMAGE kelime {iw}")
    if not (120 <= vw <= 300): print(f"⚠️  S{n:02d} VIDEO kelime {vw}")
    if short:
        assert len(img_neg) < 900 and len(vid_neg) < 900

    blk = f"""## 🎬 SAHNE {n} — {s['title']}

```
SÜRE: 10 s (HEDEF 240 kare @24 fps · ham ffprobe ⬜ D124) · ZAMAN: {zaman(n)} · VURUŞ: {s['vurus']} · {s['sek']}
KURULUM: {L} · {isa_tr} · {CAM_TR[L]} · IN FRAME: {inframe} · HACİM: {vol_tr} · İNSAN: {humans} · REPLİK: {replik}
```

### 📸 GÖRSEL PROMPT

```
{img}
```

### 🎥 VİDEO PROMPT

```
{vid}
```

---
"""
    return blk

def build(b, scenes):
    first, last = scenes[0]["n"], scenes[-1]["n"]
    assert len(scenes) == 12 and first == (b-1)*12 and last == b*12-1
    txt = header(b, first, last) + "\n".join(render_scene(s) for s in scenes)
    path = f"{OUT}/THE_STOLEN_SKY_BOLUM_{b}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"✓ BOLUM_{b}: {len(txt)//1024} KB · image {[s['_iw'] for s in scenes]} · video {[s['_vw'] for s in scenes]}")

if __name__ == "__main__":
    N = int(sys.argv[1])
    for b in range(1, N+1):
        mod = importlib.import_module(f"b{b}")
        build(b, mod.SCENES)
