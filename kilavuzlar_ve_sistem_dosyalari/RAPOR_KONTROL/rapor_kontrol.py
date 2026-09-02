#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#  RAPOR KONTROL — QA raporunun ÇIKTI tarafındaki tek deterministik kapı
# ═══════════════════════════════════════════════════════════════════
#
#  NEDEN VAR (01.09.2026 · Ders 161 · Ders 162):
#  Girdi tarafında prompt_kontrol.py var; çıktı tarafında HİÇBİR ŞEY yoktu.
#  Altı rubriğin altısında "ARITHMETIC GATE — write these three numbers
#  BEFORE the score" büyük harfle yazılıydı ve hiçbir dış kapı onu
#  denetlemiyordu. Bir partide altı raporun beşi kendi kapısından geçemedi;
#  biri hiçbir hücre kümesinin üretemeyeceği bir toplam bastı (13 kategori /
#  115,0 iddia · 12 / 108,0 gerçek). AGENTS ortak adımları bu kontrolleri
#  PROSE olarak taşıyordu — prose kapıyı bir gün ajan koşar, ertesi gün
#  unutulur. Betik koşulmadan T tablosuna satır yazılamaz.
#
#  NE YAPAR — raporu kendi tablosundan yeniden hesaplar, hiçbir şeyi
#  yorumlamaz:
#     ① SPEC KAPISI     film klasöründe *_QA_SPEC.md varken ①/④/⑥ mod V ise
#                       → TEKRAR (tabloya satır YOK)                  [D129]
#     ①.5 ARİTMETİK     n · Σ · Σ/n hücrelerden; raporun iddiasıyla kıyas.
#                       "no in-scope source" + sayı → hücre `—`       [D131]
#                       0 replikte diyalog-yalnız hücre → N/A
#     ①.5 TALLY         raporda FİİLEN yazılı 🔴🟠🟡 sayılır (timecode ile
#                       tekilleştirilir: TOP 3 ile LOG aynı bulguyu iki
#                       kez yazar)
#     ④ KURGU           şerit uzunluğu = kesme + 1 mi · ④ HİKAYE haritası
#                       kendi kesme sayısıyla çelişiyorsa film boyu hücreler
#                       sayı taşımaz                              [D118·D121]
#     ⑨ HİZALAMA        kesme zaman kodları planın ızgarasına oturuyor mu
#                       (varsayılan 10 s · --hook/--klip ile değiştir) [D115]
#     ② ÖLÇÜM BOŞLUĞU   SPEC sayaç yazarken ② "Counter Logic N/A" dediyse
#                       ⬜ AÇIK                                        [D134]
#     ⑤ ÇAPRAZ          birden çok rapor: kesme yayılımı · şerit · replik ·
#                       ⭐ SUSKUNLUK (film boyu iddia + sahibin sessizliği)
#                                                                [D107·D162]
#
#  KULLANIM:
#      python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
#              <rapor.md> [<rapor.md> ...] [--film <film klasörü>] \
#              [--hook 10] [--klip 10] [--rapor]
#
#  ÇIKTI:   rapor başına GO / ŞARTLI / TEKRAR / GEÇERSİZ + TABLOYA GİRECEK SAYI
#  ÇIKIŞ:   0 = hepsi GO · 1 = en az bir ŞARTLI · 2 = TEKRAR ya da GEÇERSİZ var
#
#  ⛔ Bu betik BULGUNUN DOĞRULUĞUNU ölçmez — o iş kare/ses ister (⑪, ②
#     kilit defteri). Ölçtüğü tek şey raporun KENDİ İÇİNDE tutup tutmadığı
#     ve partinin birbirini tutup tutmadığıdır.
# ═══════════════════════════════════════════════════════════════════

import re
import sys
from datetime import date
from pathlib import Path

# ─── SABİTLER ──────────────────────────────────────────────────────
ARIT_TOLERANS = 0.06        # ortalama karşılaştırma (yuvarlama payı)
IZGARA_TOLERANS = 2.0       # s · ⑨ hizalama (AGENTS: |Δ| ≤ 2 s → yerinde)
FILM_BOYU_HIKAYE = ("structure", "emotional arc", "ending", "retention")

MERCEK_IMZA = [
    ("① KARE",       re.compile(r"Frame Anchor|Negative Violations|Motion Quality|KNOWN AI FAILURE", re.I)),
    ("② DEVAMLILIK", re.compile(r"Wear, Damage|Counter Logic|Setup & Abandonment|CHARACTER PASSPORT", re.I)),
    ("③ SES",        re.compile(r"Speaker Attribution|AUDIO STATE|Synthetic Voice", re.I)),
    ("④ HİKAYE",     re.compile(r"Retention Risk|Premise & Clarity|STORY TRACKING ROW", re.I)),
    ("⑤ ARKA PLAN",  re.compile(r"Focus Honesty|Horizon & Topology|BACKGROUND INVENTORY", re.I)),
    ("⑥ FİZİK",      re.compile(r"Ballistics|GRAVITY TABLE|PHYSICS LEDGER|Human Biomechanics", re.I)),
    ("⑦ AKSİYON",    re.compile(r"ACTION BEAT LEDGER|BEAT STRING|Beat Anatomy|Contact Legibility|"
                                r"UNREADABLE MOMENTS|BEATS READABLE", re.I)),
    ("⑧ EFOR",       re.compile(r"EFFORT LEDGER|COST CURVE|RESET LOG|UNPAID WORK|"
                                r"Equipment Burden|EXERTION EVENTS", re.I)),
]
MOD_D_MERCEKLER = ("① KARE", "④ HİKAYE", "⑥ FİZİK",
                   "⑦ AKSİYON", "⑧ EFOR")   # yalnız bunların MODE D bölümü var

# ─── ①.6 NOVUM KAPISI [D166] ───────────────────────────────────────
# PREMISE REGISTER / PREMISE GATE taşıyan mercekler
NOVUM_MERCEKLER = ("⑥ FİZİK", "⑦ AKSİYON", "⑧ EFOR")
# SPEC'in C bloğunda dünya kuralı kaydı var mı
NOVUM_ETIKET = re.compile(r"^(NOVUM|ÖNERME|İHLAL|PREMISE)\b", re.M)
# raporun register'ı yalnız ORTAMI mı yazıyor (tür), yoksa bir KURAL mı
ORTAM_SOZU = re.compile(r"zero[-\s]?g\b|micro[-\s]?gravity|weightless|vacuum|"
                        r"free[-\s]?fall|orbital|outer space|no atmosphere|"
                        r"\b0\s*g\b|earth gravity|\b1\s*g\b", re.I)
KURAL_SOZU = re.compile(r"stops?\b|halt|hang|frozen|freezes|motionless|never moves|"
                        r"cannot move|loses (all )?(its )?(velocity|momentum|speed)|"
                        r"momentum is not conserved|does not conserve|arrested on entry|"
                        r"impossible|exotic|world rule|declared rule|violates", re.I)


def novum_var(spec_metin):
    return bool(NOVUM_ETIKET.search(spec_metin or ""))


def premise_register(metin):
    """PREMISE REGISTER satırı + altındaki '·' ile başlayan devam satırları."""
    m = re.search(r"^[ \t>*]*PREMISE REGISTER\s*[:：]?\s*(.*)$", metin, re.M | re.I)
    if not m:
        return None
    parcalar = [m.group(1).strip()]
    for s in metin[m.end():].split("\n"):
        t = s.strip()
        if t.startswith("·") or t.startswith("-") or t.startswith("*"):
            parcalar.append(t.lstrip("·-* ").strip())
        elif t:
            break
    return " ".join(p for p in parcalar if p).strip() or None

SKOR = re.compile(
    r"(?P<num>\d+(?:[.,]\d+)?)\s*/\s*10"
    r"|(?P<count>\d+)\s*count\b"
    r"|(?P<na>\bN/?A\b)"
    r"|(?P<unv>UNVERIFIABLE|UNSAFE)"
    r"|(?P<partial>⚠️?\s*PARTIAL)"
    r"|(?P<dash>^[—–-]$)", re.I)
KAYNAKSIZ = re.compile(r"no in[- ]scope source|no source\b|kaynak(?:sız| yok)|no in scope", re.I)
DIYALOG_YALNIZ = re.compile(
    r"^(dialogue|diyalog|speaker attribution|synthetic voice tells|voice identity continuity|"
    r"delivery vs performance|turn-taking & acoustics)$", re.I)
DIYALOG_VE_SES = re.compile(r"^dialogue\s*&\s*audio$", re.I)
NEGATIF_SAYIM = re.compile(r"negative violations", re.I)
COUNTER_LOGIC = re.compile(r"counter logic", re.I)
TC = re.compile(r"\b(\d{1,2}):(\d{2})(?:[.,](\d))?\b")
ETIKET = re.compile(r"(🔴|🟠|🟡)")
BOLUM_SONU = re.compile(
    r"^(#{1,3}\s|PRESENCE STRING|SCENE INVENTORY|SEVERITY TALLY|AUDIO LEDGER|THE THREE|"
    r"DRIFT MAP|BACKGROUND INVENTORY|PHYSICS LEDGER|GRAVITY TABLE|NUMERIC LOCK|SCENE MAP|"
    r"TOP 3|DETAILED ERROR|WHAT WORKED|CHARACTER PASSPORT|APPEARANCE TABLE|ATTRIBUTION MAP|"
    r"FIELD DRIFT|COUNT LOG|CONTRADICTION LOG)", re.I)
BASLIK_SATIRI = re.compile(r"\bcategory\b.*\bscore\b|^\|?\s*#\s*\|", re.I)
AYRAC = re.compile(r"^\|?\s*:?-{2,}")

# ⑤ beşinci satır — FİLM BOYU İDDİA ve SAHİBİ [Ders 162]
# iddia: bir raporda her sahneyi kapsayan ihlal; sahibi: kapsam listesine göre
# o ihlali TİCK'lemesi gereken mercek; anahtar: sahibin raporunda aranacak iz.
FILM_BOYU_IDDIALAR = [
    ("filigran / sabit köşe işareti",
     re.compile(r"(static|persistent|fixed|constant)[^.\n]{0,50}(mark|watermark|logo|icon|triangle|ui remnant)"
                r"|watermark", re.I),
     "① KARE",
     re.compile(r"watermark|corner mark|static mark|ui remnant|static corner|logo", re.I)),
    ("sürekli ekran metni / altyazı",
     re.compile(r"(burned[- ]in|on[- ]screen)\s+(text|subtitle|caption)[^.\n]{0,60}(every|all|throughout|persistent)", re.I),
     "① KARE",
     re.compile(r"subtitle|burned[- ]in|on[- ]screen text|caption", re.I)),
]
FILM_BOYU_IZ = re.compile(r"every scene|all scenes|\b\d{1,2}/\d{1,2}\s+scenes|throughout|persistent|0:00\s*[-–]", re.I)


class Bulgu:
    """seviye: GEÇERSİZ · TEKRAR · ŞARTLI · NOT"""
    def __init__(self, seviye, baslik, ayrinti=""):
        self.seviye, self.baslik, self.ayrinti = seviye, baslik, ayrinti

    def __str__(self):
        isaret = {"GEÇERSİZ": "🚨", "TEKRAR": "⛔", "ŞARTLI": "⚠️ ", "NOT": "·"}[self.seviye]
        s = f"   {isaret} {self.baslik}"
        if self.ayrinti:
            s += f"\n        {self.ayrinti}"
        return s


# ─── OKUMA ─────────────────────────────────────────────────────────
def govde_al(metin):
    """Operatör künyesini (dosya başındaki blok + ilk '---') atla.

    02_HAM_RAPORLAR'daki dosyalar raporun ÜSTÜNE bir künye taşır; künye
    ⛔/🔴 ve 'mod V' gibi izler içerir ve tally sayımını kirletir.
    """
    satirlar = metin.split("\n")
    for i, s in enumerate(satirlar[:60]):
        if s.strip() == "---":
            return "\n".join(satirlar[i + 1:])
    return metin


def alan(metin, *anahtarlar):
    for a in anahtarlar:
        m = re.search(rf"^[ \t>*]*{re.escape(a)}\s*[:：]\s*(.+)$", metin, re.M | re.I)
        if m:
            return m.group(1).strip()
    return None


def ilk_sayi(s, tip=int):
    if not s:
        return None
    m = re.search(r"\d+(?:[.,]\d+)?", s)
    return tip(m.group(0).replace(",", ".")) if m else None


def sure_sn(s):
    if not s:
        return None, False
    tahmin = bool(re.search(r"ESTIMATED|~", s, re.I))
    m = re.search(r"(\d{1,2}):(\d{2})", s)
    if m:
        return int(m.group(1)) * 60 + int(m.group(2)), tahmin
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*s", s)
    return (float(m.group(1).replace(",", ".")) if m else None), tahmin


def kesme_zamanlari(metin):
    """CUTS COUNTED satırı (+ sarmalanmış devamı) → saniye listesi."""
    # ⚠️ satır BAŞI şart değil: rubriklerin kendi biçimi "SCENES OBSERVED: n · CUTS
    # COUNTED: n" — eski desen bunu okumuyordu, ④ şerit ve ⑨ hizalama sessizce ölüydü.
    m = re.search(r"(?:^|[·|•])[ \t>*]*(CUTS COUNTED|Cuts you can see)\s*[:：]\s*(.*(?:\n[ \t]*(?=\d{1,2}:\d{2}|[·,])[^\n]*){0,4})",
                  metin, re.M | re.I)
    if not m:
        return None, []
    blok = m.group(2)
    n = ilk_sayi(blok)
    tcs = [int(a) * 60 + int(b) + (int(c) / 10 if c else 0) for a, b, c in TC.findall(blok)]
    return n, tcs


def serit_al(metin):
    m = re.search(r"PRESENCE STRING[^\n]*\n+\s*`?([-1]{3,})`?", metin) or \
        re.search(r"PRESENCE STRING[:\s`]*([-1]{3,})", metin)
    return m.group(1) if m else None


def dizi_al(metin, baslik, alfabe):
    """BEAT STRING (⑦) / COST CURVE (⑧) — sahne başına bir hane."""
    d = re.search(rf"{baslik}[^\n]*\n(?:[^\n]*\n)??\s*`?([{alfabe}]{{3,}})`?", metin) or \
        re.search(rf"{baslik}[:\s`]*([{alfabe}]{{3,}})", metin)
    return d.group(1) if d else None


def replik_al(metin):
    s = alan(metin, "LINES HEARD", "SPOKEN LINES")
    if s is None:
        s2 = alan(metin, "AUDIO STATE")
        if s2:
            m = re.search(r"SPOKEN LINES:\s*(\d+)", s2)
            if m:
                return int(m.group(1)), s2
        return None, None
    if re.match(r"none|0\b|yok", s, re.I):
        return 0, s
    return ilk_sayi(s), s


def tally_al(metin):
    m = re.search(r"🔴\s*BLOCKER:\s*(\d+)[\s\S]{0,40}?🟠\s*MAJOR:\s*(\d+)[\s\S]{0,40}?🟡\s*MINOR:\s*(\d+)", metin)
    return tuple(int(x) for x in m.groups()) if m else None


def yazili_etiketler(metin):
    """Raporda fiilen yazılmış 🔴🟠🟡 — (etiket, ilk timecode) ile tekilleştirilir."""
    ciftler = set()
    for s in metin.split("\n"):
        if "BLOCKER:" in s and "MAJOR:" in s:
            continue                                     # tally satırı
        if re.match(r"\s*(#+\s*)?SEVERITY TALLY", s):
            continue
        if re.search(r"BLOCKER\s+[—-]\s+Breaks|MAJOR\s+[—-]\s+Clearly|MINOR\s+[—-]\s+Noticeable", s):
            continue                                     # rubrik efsanesi kopyalanmışsa
        for e in ETIKET.findall(s):
            tc = TC.search(s)
            anahtar = tc.group(0) if tc else s.strip()[:60]
            ciftler.add((e, anahtar))
    return {e: sum(1 for x, _ in ciftler if x == e) for e in ("🔴", "🟠", "🟡")}


def mercek_bul(metin):
    puan = {ad: len(rx.findall(metin)) for ad, rx in MERCEK_IMZA}
    ad = max(puan, key=puan.get)
    return ad if puan[ad] else "? (mercek okunamadı)"


def hucre_ayir(satir):
    s = satir.strip()
    if "|" in s:
        hucreler = [h.strip() for h in s.strip("|").split("|")]
    else:
        hucreler = [h.strip() for h in re.split(r"\s{2,}|\t", s) if h.strip()]
        if len(hucreler) < 2:                            # tek boşluklu satır (Payload ④ biçimi)
            m = re.match(r"^(.*?)\s+((?:\d+(?:[.,]\d+)?\s*/\s*10)|N/?A|—|–|UNVERIFIABLE|\d+\s*count|⚠️?\s*PARTIAL)\b\s*(.*)$", s, re.I)
            if not m:
                return None
            hucreler = [m.group(1), m.group(2), m.group(3)]
    return [h for h in hucreler if h != ""]


def skor_tablosu(metin):
    """SCORES SUMMARY bölümünün satırlarını çöz → [dict(ad, tip, deger, issue)]"""
    satirlar = metin.split("\n")
    bas = next((i for i, s in enumerate(satirlar) if re.search(r"SCORES SUMMARY", s)), None)
    if bas is None:
        return []
    rows = []
    for s in satirlar[bas + 1:]:
        if not s.strip():
            continue
        if BOLUM_SONU.match(s.strip()) and rows:
            break
        if BASLIK_SATIRI.search(s) or AYRAC.match(s.strip()):
            continue
        h = hucre_ayir(s)
        if not h or len(h) < 2:
            continue
        # ad: ilk skor-olmayan hücre (başındaki sıra no / kalınlık / emoji temizlenir)
        sira = re.compile(r"^\s*#?\s*\d{0,2}\s*$")
        ad_i = next((i for i, x in enumerate(h) if not sira.match(x) and not SKOR.search(x)), None)
        if ad_i is None:
            continue
        ad = re.sub(r"^[\s#\d.|*_]+|[*_]+$", "", h[ad_i]).strip()
        ad = re.sub(r"^[^\w(]+", "", ad).strip()
        sk = None
        for i, x in enumerate(h):
            if i == ad_i:
                continue
            m = SKOR.search(x)
            if m:
                sk = (i, m)
                break
        if not sk:
            continue
        i, m = sk
        issue = " ".join(h[i + 1:]).strip()
        if m.group("num"):
            tip, deger = "sayi", float(m.group("num").replace(",", "."))
        elif m.group("count"):
            tip, deger = "sayim", int(m.group("count"))
        elif m.group("na"):
            tip, deger = "na", None
        elif m.group("unv"):
            tip, deger = "unv", None
        elif m.group("partial"):
            tip, deger = "partial", None
        else:
            tip, deger = "dash", None
        if not ad or len(ad) > 60:
            continue
        rows.append({"ad": ad, "tip": tip, "deger": deger, "issue": issue, "ham": s.strip()})
    return rows


# ─── TEK RAPOR ─────────────────────────────────────────────────────
def rapor_denetle(yol, spec_metin=None, hook=10.0, klip=10.0):
    metin_tam = yol.read_text(encoding="utf-8", errors="replace")
    metin = govde_al(metin_tam)
    R = {"yol": yol, "bulgular": [], "mercek": mercek_bul(metin)}
    B = R["bulgular"]

    R["mod"] = (alan(metin, "INPUT MODE") or "").strip()[:1].upper() or None
    R["film"] = alan(metin, "FILM")
    R["format"] = alan(metin, "FORMAT")
    R["sure"], R["sure_tahmin"] = sure_sn(alan(metin, "VIDEO DURATION", "RUNTIME", "MEASURED RUNTIME"))
    R["kesme"], R["kesme_tc"] = kesme_zamanlari(metin)
    R["sahne"] = ilk_sayi(alan(metin, "SCENES OBSERVED", "SCENE COUNT"))
    R["kart"] = alan(metin, "NON-SCENE MATERIAL")
    R["serit"] = serit_al(metin)
    R["beat_dizi"] = dizi_al(metin, "BEAT STRING", "Apx-")
    R["bedel_dizi"] = dizi_al(metin, "COST CURVE", "0-9")
    R["replik"], R["replik_ham"] = replik_al(metin)
    R["audio_state"] = (alan(metin, "AUDIO STATE") or "")[:1].upper() or None
    R["tally"] = tally_al(metin)
    R["yazili"] = yazili_etiketler(metin)

    m_n = re.search(r"SCORED CATEGORIES\s*[:：]\s*(\d+)", metin)
    iddia_n = int(m_n.group(1)) if m_n else None
    m_s = re.search(r"SUM OF SCORES\s*[:：]\s*([\d.,]+)", metin)
    iddia_sum = float(m_s.group(1).replace(",", ".")) if m_s else None
    m_div = re.search(r"DIVISION:[^\n=]*=\s*([\d.,]+)", metin)
    iddia_div = float(m_div.group(1).replace(",", ".")) if m_div else None
    m_ov = re.search(r"OVERALL(?: STORY)? SCORE:\s*([\d.,]+)", metin)
    iddia_ov = float(m_ov.group(1).replace(",", ".")) if m_ov else None
    R["iddia"] = (iddia_n, iddia_sum, iddia_div, iddia_ov)

    # ① SPEC KAPISI
    if spec_metin is not None and R["mercek"] in MOD_D_MERCEKLER and R["mod"] != "D":
        B.append(Bulgu("TEKRAR", f"SPEC dosyası VAR, rapor mod {R['mod'] or '?'} → koşu TEKRARLANIR [D129]",
                       "ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / "
                       "yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>"))
    elif spec_metin is not None and R["mercek"] not in MOD_D_MERCEKLER:
        B.append(Bulgu("NOT", "bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır"))

    # ①.6 NOVUM KAPISI [D166] — SPEC bir DÜNYA KURALI yazıyorsa ⑥⑦⑧'in
    #     PREMISE REGISTER'ı onu taşımak zorundadır. Taşımıyorsa mercek
    #     filmin KURALINI kusur olarak puanlar ve düşen puan ⑩'da geri verilir.
    if spec_metin is not None and R["mercek"] in NOVUM_MERCEKLER and novum_var(spec_metin):
        reg = premise_register(metin)
        if not reg:
            B.append(Bulgu("ŞARTLI", "SPEC NOVUM yazıyor, raporda PREMISE REGISTER YOK [D166]",
                           "STEP 0 koşulmamış → filmin kuralı kusur olarak puanlanmış olabilir; "
                           "⑩ ÖNERME KAPISI bu raporda ZORUNLU, kaynağı planda yazılı bulguların puanı geri verilir"))
        elif ORTAM_SOZU.search(reg) and not KURAL_SOZU.search(reg):
            B.append(Bulgu("ŞARTLI", "PREMISE REGISTER yalnız ORTAMI yazıyor, filmin KURALINI değil [D166]",
                           f"kayıtlı: \"{reg[:90].strip()}…\" · SPEC'te NOVUM var → ⑩ ÖNERME KAPISI ZORUNLU; "
                           "novum kaynaklı kesintiler DÜŞER ve ortalama yeniden hesaplanır [D130]"))

    # ①.5 ARİTMETİK — raporun kendi tablosundan
    rows = skor_tablosu(metin)
    R["rows"] = rows
    if not rows:
        B.append(Bulgu("GEÇERSİZ", "SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz"))
        R["karar"] = "GEÇERSİZ"
        return R

    ham_sayi = [r for r in rows if r["tip"] == "sayi" and not NEGATIF_SAYIM.search(r["ad"])]
    ham_n, ham_sum = len(ham_sayi), sum(r["deger"] for r in ham_sayi)
    ham_ort = round(ham_sum / ham_n, 2) if ham_n else None

    if iddia_n is not None and iddia_sum is not None:
        if iddia_n != ham_n or abs(iddia_sum - ham_sum) > 0.05:
            B.append(Bulgu("GEÇERSİZ",
                           f"ARİTMETİK FABRİKE — rapor n={iddia_n} Σ={iddia_sum:g} yazdı; kendi hücreleri "
                           f"n={ham_n} Σ={ham_sum:g} (ort {ham_ort})",
                           "Hiçbir hücre kümesi iddia edilen toplamı üretmiyor. Rubriğin kendi ④ kuralı: "
                           "\"the table is right and the overall is wrong\" — satır tabloya GİRMEZ [D161]."))
        elif iddia_ov is not None and ham_ort is not None and abs(iddia_ov - ham_ort) > ARIT_TOLERANS:
            B.append(Bulgu("ŞARTLI", f"yuvarlama — OVERALL {iddia_ov:g} yazılmış, hücreler {ham_ort} veriyor",
                           "tablo haklıdır; TABLOYA GİRECEK SAYI düzeltilmiş ortalamadır"))
    elif iddia_ov is not None:
        B.append(Bulgu("ŞARTLI", "ARITHMETIC GATE satırları (SCORED/SUM/DIVISION) yok — ortalama yalnız hücrelerden doğrulandı"))

    # düzeltmeler: kaynaksız hücre → `—` · diyalog-yalnız hücre 0 replikte → N/A
    duzeltme = []
    for r in rows:
        if r["tip"] != "sayi" or NEGATIF_SAYIM.search(r["ad"]):
            continue
        if KAYNAKSIZ.search(r["issue"]):
            r["tip"], r["not"] = "dash", "kaynaksız→—"
            duzeltme.append(f"{r['ad']} {r['deger']:g}/10 → — (issue: \"no in-scope source\") [D131]")
        elif R["replik"] == 0 and DIYALOG_YALNIZ.match(r["ad"]):
            r["tip"], r["not"] = "na", "0 replik→N/A"
            duzeltme.append(f"{r['ad']} {r['deger']:g}/10 → N/A (0 replik — sessizlik tasarımdır)")
        elif R["replik"] == 0 and DIYALOG_VE_SES.match(r["ad"]):
            B.append(Bulgu("NOT", f"{r['ad']} {r['deger']:g}/10 · film 0 replikli — hücrenin kaynağı SES FİZİĞİ "
                                  "(vakumda ses / senkron) olmalı; replik kaynaklıysa N/A'ya çevir (insan kararı)"))
    if duzeltme:
        B.append(Bulgu("ŞARTLI", f"{len(duzeltme)} hücre düzeltildi", " · ".join(duzeltme)))

    # ④ KURGU — ④ HİKAYE haritası kesme sayısıyla çelişiyor mu
    if R["mercek"] == "④ HİKAYE" and R["kesme"] and R["sahne"] and R["sahne"] < R["kesme"] - 1:
        dusen = []
        for r in rows:
            if r["tip"] == "sayi" and any(k in r["ad"].lower() for k in FILM_BOYU_HIKAYE):
                r["tip"], r["not"] = "dash", "harita çelişkili→—"
                dusen.append(r["ad"])
        B.append(Bulgu("ŞARTLI",
                       f"sahne haritası ({R['sahne']} sahne) kendi kesme sayısıyla ({R['kesme']}) çelişiyor",
                       "rubriğin STEP 1 kuralı: en kısa kesme aralığının iki katından uzun blok → böl ve yeniden say. "
                       f"Film boyu hücreler sayı taşımaz [AGENTS ④]: {', '.join(dusen) or '—'}"))

    # ② ÖLÇÜM BOŞLUĞU — SPEC sayaç yazıyor, ② "Counter N/A" diyor
    if R["mercek"] == "② DEVAMLILIK" and spec_metin and re.search(r"SAYAÇ|sayaç|COUNTER", spec_metin):
        for r in rows:
            if COUNTER_LOGIC.search(r["ad"]) and r["tip"] in ("na", "dash"):
                B.append(Bulgu("ŞARTLI", "Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]",
                               "kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur"))

    # düzeltme sonrası aritmetik
    son_sayi = [r for r in rows if r["tip"] == "sayi" and not NEGATIF_SAYIM.search(r["ad"])]
    R["son_n"] = len(son_sayi)
    R["son_sum"] = sum(r["deger"] for r in son_sayi)
    R["son_ort"] = round(R["son_sum"] / R["son_n"], 1) if R["son_n"] else None
    R["ham"] = (ham_n, ham_sum, ham_ort)

    # ①.5 TALLY
    if R["tally"]:
        y = R["yazili"]
        yz = (y["🔴"], y["🟠"], y["🟡"])
        if yz != R["tally"]:
            B.append(Bulgu("ŞARTLI", f"SEVERITY TALLY {R['tally']} ≠ yazılı etiketler {yz} (🔴,🟠,🟡)",
                           "verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]"))
    elif any(R["yazili"].values()):
        B.append(Bulgu("NOT", f"SEVERITY TALLY satırı yok; yazılı etiketler {R['yazili']}"))

    # ④ ŞERİT — uzunluk = kesme + 1 (kart hariç)
    if R["serit"] and R["kesme"]:
        beklenen = R["kesme"] + 1
        if len(R["serit"]) not in (beklenen, beklenen - 1, beklenen - 2):
            B.append(Bulgu("ŞARTLI", f"PRESENCE STRING {len(R['serit'])} hane, kesme+1 = {beklenen}",
                           "şerit sahne başına bir hanedir; sayı tutmuyorsa harita ya da sayım yanlış [D118]"))

    # ⑦ BEAT STRING — uzunluk = kesme + 1 · beat sayımı kendi içinde tutuyor mu
    if R["beat_dizi"] and R["kesme"]:
        bek = R["kesme"] + 1
        if len(R["beat_dizi"]) not in (bek, bek - 1, bek - 2):
            B.append(Bulgu("ŞARTLI", f"BEAT STRING {len(R['beat_dizi'])} hane, kesme+1 = {bek}",
                           "dizi sahne başına bir hanedir; tutmuyorsa beat defteri ya da kesme sayımı yanlış"))
    if R["mercek"] == "⑦ AKSİYON":
        b_top = ilk_sayi(alan(metin, "BEATS COUNTED"))
        m_ok = re.search(r"BEATS READABLE[:\s]*(\d+)[^\d\n]+(\d+)[^\d\n]+(\d+)", metin)
        if b_top and m_ok:
            parca = sum(int(g) for g in m_ok.groups())
            if parca != b_top:
                B.append(Bulgu("ŞARTLI", f"BEATS READABLE toplamı {parca} ≠ BEATS COUNTED {b_top}",
                               "okunur + kısmi + okunmaz, defterdeki beat sayısını vermeli"))
        if R["beat_dizi"] and b_top == 0 and re.search(r"[Apx]", R["beat_dizi"]):
            B.append(Bulgu("ŞARTLI", "BEATS COUNTED 0 ama BEAT STRING beat gösteriyor", "ikisinden biri yanlış"))

    # ⑧ COST CURVE — uzunluk + her düşüşün RESET LOG karşılığı [pattern ③/⑪]
    if R["bedel_dizi"]:
        if R["kesme"]:
            bek = R["kesme"] + 1
            if len(R["bedel_dizi"]) not in (bek, bek - 1, bek - 2):
                B.append(Bulgu("ŞARTLI", f"COST CURVE {len(R['bedel_dizi'])} hane, kesme+1 = {bek}",
                               "eğri sahne başına bir hanedir"))
        dusus = sum(1 for i in range(1, len(R["bedel_dizi"]))
                    if int(R["bedel_dizi"][i]) < int(R["bedel_dizi"][i - 1]))
        govde_reset = re.search(r"RESET LOG(.*?)(?=\n#{1,3}\s|\Z)", metin, re.S)
        satir_reset = 0
        if govde_reset:
            satir_reset = sum(1 for s in govde_reset.group(1).split("\n")
                              if "|" in s and re.search(r"EARNED|UNEARNED|UNCLEAR", s, re.I))
        if dusus and satir_reset < dusus:
            B.append(Bulgu("ŞARTLI", f"COST CURVE'de {dusus} düşüş var, RESET LOG'da {satir_reset} satır",
                           "her düşüş toparlanma gösterilerek açıklanır; açıklanmayan düşüş bulgudur [⑧ pattern ③/⑪]"))
        if len(set(R["bedel_dizi"])) == 1 and re.search(r"EXERTION EVENTS[:\s]*[1-9]", metin):
            B.append(Bulgu("ŞARTLI", f"COST CURVE sabit ({R['bedel_dizi'][0]}) ama efor olayı var",
                           "iş yapıldıysa borç ya artar ya toparlanır; düz eğri ÖLÇMEDİ demektir"))

    # ⑨ HİZALAMA — kesme zaman kodları ızgaraya oturuyor mu
    if R["kesme_tc"] and len(R["kesme_tc"]) >= 3:
        sapmalar = []
        for i, t in enumerate(R["kesme_tc"], 1):
            beklenen = hook + (i - 1) * klip
            sapmalar.append(t - beklenen)
        mx = max(abs(x) for x in sapmalar)
        R["izgara_max"] = mx
        if mx <= IZGARA_TOLERANS:
            B.append(Bulgu("NOT", f"⑨ ızgara OTURUYOR — {len(sapmalar)} kesme, max |Δ| = {mx:.1f} s "
                                  f"(hook {hook:g} · klip {klip:g}) → zaman kodları uydurulmamış [D115]"))
        else:
            kotu = [f"{i}:{d:+.0f}s" for i, d in enumerate(sapmalar, 1) if abs(d) > IZGARA_TOLERANS]
            B.append(Bulgu("ŞARTLI", f"⑨ ızgara KAYMIŞ — max |Δ| = {mx:.1f} s · sapan kesmeler: {', '.join(kotu[:8])}",
                           "ya kurgu ızgarada değil ya rapor zaman kodlarını uydurmuş; ⑪ ölçümü karar verir"))

    # karar
    sev = [b.seviye for b in B]
    if "GEÇERSİZ" in sev:
        R["karar"] = "GEÇERSİZ"
    elif "TEKRAR" in sev:
        R["karar"] = "TEKRAR"
    elif "ŞARTLI" in sev:
        R["karar"] = "ŞARTLI"
    else:
        R["karar"] = "GO"
    return R


# ─── ÇAPRAZ (⑤) ────────────────────────────────────────────────────
def capraz(sonuclar, olcum=None):
    """olcum: ⑪ ÖLÇÜM KAPISI sonucu {"kesme": n, "sahne": n}.

    ⛔ AGENTS §3: "Rapor ile ölçüm çelişirse ÖLÇÜM kazanır." Ölçüm VERİLDİYSE
    kesme yayılımı partiyi TOPTAN düşürmez — anlaşmazlık zaten çözülmüştür.
    Ölçümle uyuşmayan mercek TEKİL olarak ŞARTLI olur ve sapması yazılır.
    Ölçüm YOKSA eski davranış aynen sürer (yayılım > 1 → parti geçersiz).
    """
    B = []
    olcum = olcum or {}
    o_kes = olcum.get("kesme")
    kes = [(r["mercek"], r["kesme"]) for r in sonuclar if r["kesme"]]
    if o_kes and kes:
        satir = " · ".join(f"{m} {k}" for m, k in kes)
        sapan = [(m, k) for m, k in kes if abs(k - o_kes) > 1]
        B.append(Bulgu("NOT", f"⑪ ÖLÇÜM HAKEM: kesme = {o_kes} (ölçüldü) · raporlar: {satir}"))
        if sapan:
            for r in sonuclar:
                if r["kesme"] and abs(r["kesme"] - o_kes) > 1:
                    r["bulgular"].append(Bulgu(
                        "ŞARTLI",
                        f"kesme {r['kesme']} ≠ ÖLÇÜM {o_kes} → bu merceğin FİLM BOYU sayıları ŞARTLI",
                        "ölçüm kazanır [AGENTS §3]; kesme/sahne türevi hükümler (REMOVE reçetesi, "
                        "sıra iddiası, film boyu kategori) bu rapordan ALINMAZ"))
                    if r["karar"] == "GO":
                        r["karar"] = "ŞARTLI"
            B.append(Bulgu("ŞARTLI", "⑤ ölçümden sapan mercek(ler): " +
                           " · ".join(f"{m} {k}" for m, k in sapan),
                           "parti AYAKTA — anlaşmazlık ölçümle çözüldü; yalnız sapan mercek şartlıdır"))
        else:
            B.append(Bulgu("NOT", "⑤ her mercek ölçümle uyuşuyor → kesme ekseni doğrulandı"))
    elif len(kes) >= 2:
        v = [k for _, k in kes]
        yay = max(v) - min(v)
        satir = " · ".join(f"{m} {k}" for m, k in kes)
        if yay <= 1:
            B.append(Bulgu("NOT", f"⑤ kesme sayıları birbirini doğruluyor (yayılım {yay}): {satir}"))
        else:
            B.append(Bulgu("GEÇERSİZ", f"⑤ KESME YAYILIMI {yay} > 1 → PARTİNİN TÜM SATIRLARI GEÇERSİZ [D107]",
                           satir + "\n        ⭐ ÇÖZÜMÜ: master'ı ölç (olcum_kapisi.sh) ve --olcum-kesme <n> ile "
                                   "yeniden koş — ölçüm hakemdir, parti ayakta kalır [AGENTS §3]"))
    o_sah = olcum.get("sahne")
    sah = [(r["mercek"], r["sahne"]) for r in sonuclar if r["sahne"]]
    if o_sah and sah:
        sapan_s = [(m, k) for m, k in sah if abs(k - o_sah) > 1]
        if sapan_s:
            B.append(Bulgu("ŞARTLI", f"⑤ sahne — ÖLÇÜM {o_sah}; sapan: " +
                           " · ".join(f"{m} {k}" for m, k in sapan_s),
                           "sapan merceğin sahne haritası ölçümle yeniden okunur [AGENTS §3]"))
        else:
            B.append(Bulgu("NOT", f"⑤ sahne ekseni ölçümle doğrulandı ({o_sah})"))
    elif len(sah) >= 2:
        v = [k for _, k in sah]
        if max(v) - min(v) > 1:
            B.append(Bulgu("ŞARTLI", f"⑤ sahne sayıları ayrışıyor: " + " · ".join(f"{m} {k}" for m, k in sah)))
    ser = [(r["mercek"], r["serit"]) for r in sonuclar if r["serit"]]
    if len(ser) >= 2:
        from collections import Counter
        c = Counter(s for _, s in ser)
        cogunluk, n = c.most_common(1)[0]
        sapan = [m for m, s in ser if s != cogunluk]
        if sapan:
            B.append(Bulgu("ŞARTLI", f"⑤ ŞERİT — çoğunluk `{cogunluk}` ({n} mercek); sapan: {', '.join(sapan)}",
                           "sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]"))
        else:
            B.append(Bulgu("NOT", f"⑤ şerit ekseni doğrulandı — {n} mercek `{cogunluk}`"))
    rep = [(r["mercek"], r["replik"]) for r in sonuclar if r["replik"] is not None]
    if len(rep) >= 2:
        v = set(k for _, k in rep)
        if len(v) == 1:
            B.append(Bulgu("NOT", f"⑤ replik ekseni doğrulandı — {len(rep)} mercek, {v.pop()} replik [D121]"))
        else:
            B.append(Bulgu("ŞARTLI", "⑤ replik sayıları ayrışıyor: " + " · ".join(f"{m} {k}" for m, k in rep),
                           "alıntı kimin yanıldığını söyler; LINES HEARD satırları yan yana okunur"))
    # ⭐ BEŞİNCİ SATIR — SUSKUNLUK [D162]
    metinler = {r["mercek"]: govde_al(r["yol"].read_text(encoding="utf-8", errors="replace")) for r in sonuclar}
    for ad, rx, sahip, sahip_iz in FILM_BOYU_IDDIALAR:
        for m, t in metinler.items():
            if m == sahip:
                continue
            hit = None
            for mm in rx.finditer(t):
                cevre = t[max(0, mm.start() - 200):mm.end() + 200]
                if FILM_BOYU_IZ.search(cevre):
                    hit = t[max(0, mm.start() - 60):mm.end() + 60].replace("\n", " ")
                    break
            if not hit:
                continue
            st = metinler.get(sahip)
            if st is None:
                B.append(Bulgu("NOT", f"{m} film boyu iddia: {ad} — sahibi {sahip} bu partide yok"))
                continue
            sahip_gordu = any(sahip_iz.search(s) and not re.match(r"\s*-?\s*\[\s\]", s) for s in st.split("\n"))
            if sahip_gordu:
                B.append(Bulgu("NOT", f"{m} film boyu iddia ({ad}) — sahibi {sahip} de yazmış, D108 normal işler"))
            else:
                B.append(Bulgu("ŞARTLI", f"🚨 SUSKUNLUK — {m} film boyu iddia: {ad}; sahibi {sahip} SUSTU [D162]",
                               f"\"…{hit.strip()}…\" → kareyle çözülür (⑪ köşe testi / tek kare); çözülene kadar "
                               f"HER İKİ merceğin o kategorisi sayı taşımaz"))
    return B


# ─── ÇIKTI ─────────────────────────────────────────────────────────
def tabloya(r):
    if r["karar"] in ("GEÇERSİZ", "TEKRAR"):
        return "—"
    if r["son_ort"] is None:
        return "— (sayı taşıyan hücre yok)"
    s = f"{r['son_ort']:.1f}"
    if r["mod"] == "V":
        s += " Ⓥ"
    if r["karar"] == "ŞARTLI":
        s += " ⚠️ ŞARTLI"
    return s


def yazdir(r):
    isaret = {"GO": "✅", "ŞARTLI": "⚠️ ", "TEKRAR": "⛔", "GEÇERSİZ": "🚨"}[r["karar"]]
    print(f"\n{'═' * 67}\n{isaret} {r['karar']}  ·  {r['mercek']}  ·  {r['yol'].name}\n{'═' * 67}")
    n, s, o = r.get("ham", (None, None, None))
    i_n, i_s, i_d, i_o = r["iddia"]
    print(f"   mod {r['mod'] or '—'} · süre {r['sure'] or '?'}{'~' if r['sure_tahmin'] else ''} s · "
          f"kesme {r['kesme'] or '?'} · sahne {r['sahne'] or '?'} · replik {r['replik'] if r['replik'] is not None else '?'} · "
          f"şerit {r['serit'] or '—'}")
    if n is not None:
        print(f"   iddia: n={i_n} Σ={i_s} ort={i_o}   │   hücreler: n={n} Σ={s:g} ort={o}   │   "
              f"düzeltme sonrası: n={r['son_n']} Σ={r['son_sum']:g} ort={r['son_ort']}")
    for b in r["bulgular"]:
        print(b)
    print(f"   ▶ TABLOYA GİRECEK SAYI: {tabloya(r)}")


def rapor_yaz(sonuclar, cb, kok, film_adi):
    hedef = kok / "RAPORLAR"
    hedef.mkdir(exist_ok=True)
    bugun = date.today().strftime("%d.%m.%Y")
    ad = f"{film_adi or 'RAPOR'}_{date.today().strftime('%Y%m%d')}_RAPOR_KONTROL.md"
    L = [f"# 🧮 RAPOR KONTROL — {film_adi or '(film adı verilmedi)'}", "",
         f"> **Tarih:** {bugun} · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`", "",
         "| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |",
         "|---|---|:--:|---|---|---|---|"]
    for r in sonuclar:
        n, s, o = r.get("ham", (None, None, None))
        i_n, i_s, i_d, i_o = r["iddia"]
        L.append(f"| {r['mercek']} | `{r['yol'].name}` | {r['karar']} | {i_n}/{i_s}/{i_o} | "
                 f"{n}/{s if s is None else f'{s:g}'}/{o} | {r.get('son_n')}/{r.get('son_sum', 0):g}/{r.get('son_ort')} | {tabloya(r)} |")
    L.append("")
    for r in sonuclar:
        L.append(f"## {r['mercek']} — {r['karar']}")
        for b in r["bulgular"]:
            L.append(f"- **{b.seviye}** — {b.baslik}" + (f"<br>{b.ayrinti}" if b.ayrinti else ""))
        L.append("")
    if cb:
        L.append("## ⑤ ÇAPRAZ KAPI")
        for b in cb:
            L.append(f"- **{b.seviye}** — {b.baslik}" + (f"<br>{b.ayrinti}" if b.ayrinti else ""))
    (hedef / ad).write_text("\n".join(L) + "\n", encoding="utf-8")
    return hedef / ad


def main():
    argv = sys.argv[1:]
    if not argv or "-h" in argv or "--help" in argv:
        print(__doc__ or "")
        print("KULLANIM: rapor_kontrol.py <rapor.md> [...] [--film <klasör>] [--hook 10] [--klip 10] [--rapor]")
        print("           [--olcum-kesme <n>] [--olcum-sahne <n>]  ← ⑪ ölçümü hakem yapar")
        return 1
    hook, klip, film_dir, rapor, dosyalar = 10.0, 10.0, None, False, []
    olcum = {}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--hook":
            hook = float(argv[i + 1]); i += 2
        elif a == "--klip":
            klip = float(argv[i + 1]); i += 2
        elif a == "--film":
            film_dir = Path(argv[i + 1]); i += 2
        elif a == "--rapor":
            rapor = True; i += 1
        elif a == "--olcum-kesme":
            olcum["kesme"] = int(argv[i + 1]); i += 2
        elif a == "--olcum-sahne":
            olcum["sahne"] = int(argv[i + 1]); i += 2
        else:
            dosyalar.append(Path(a)); i += 1

    spec_metin, film_adi = None, None
    if film_dir:
        film_adi = film_dir.name
        specs = sorted(film_dir.glob("*_QA_SPEC.md"))
        if specs:
            spec_metin = specs[0].read_text(encoding="utf-8", errors="replace")
            print(f"SPEC: {specs[0]}  → ①/④/⑥ için MOD D ZORUNLU")
        else:
            print(f"SPEC: yok ({film_dir}) → mod V bilinçli; ama [D117] film 'yazımı tamam' değil")

    sonuclar = []
    for y in dosyalar:
        if not y.is_file():
            print(f"⚠️  bulunamadı: {y}"); continue
        sonuclar.append(rapor_denetle(y, spec_metin, hook, klip))
    if not sonuclar:
        return 1
    cb = capraz(sonuclar, olcum) if len(sonuclar) >= 2 else []
    for r in sonuclar:
        yazdir(r)

    if cb:
        print(f"\n{'═' * 67}\n  ⑤ ÇAPRAZ KAPI — {len(sonuclar)} rapor\n{'═' * 67}")
        for b in cb:
            print(b)
        if any(b.seviye == "GEÇERSİZ" for b in cb):
            for r in sonuclar:
                r["karar_tekil"] = r["karar"]
                r["karar"] = "GEÇERSİZ"
            print("   ▶ parti GEÇERSİZ: hiçbir satır tabloya girmez; ŞERİT ve REPLİK eksenleri yine de okunur [D121]")

    kararlar = [r["karar"] for r in sonuclar]
    if any("karar_tekil" in r for r in sonuclar):
        print("   tekil kararlar (parti düşmeden önce): " +
              " · ".join(f"{r['mercek']} {r['karar_tekil']}" for r in sonuclar))
    print(f"\n{'═' * 67}\n  TOPLAM {len(sonuclar)} rapor · 🚨 {kararlar.count('GEÇERSİZ')} GEÇERSİZ · "
          f"⛔ {kararlar.count('TEKRAR')} TEKRAR · ⚠️  {kararlar.count('ŞARTLI')} ŞARTLI · ✅ {kararlar.count('GO')} GO"
          f"\n{'═' * 67}")
    if rapor:
        p = rapor_yaz(sonuclar, cb, Path(__file__).resolve().parent, film_adi)
        print(f"  rapor yazıldı: {p}")
    if any(k in ("GEÇERSİZ", "TEKRAR") for k in kararlar):
        return 2
    if "ŞARTLI" in kararlar:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
