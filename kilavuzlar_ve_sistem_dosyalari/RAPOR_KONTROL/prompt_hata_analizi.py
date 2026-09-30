#!/usr/bin/env python3
"""
prompt_hata_analizi.py — ham QA bulgusu × PROMPT METNİ  (18.09.2026)

NEDEN VAR: depoda 564 ham QA raporu var ve hepsi ekranda GÖRÜLEN kusuru yazıyor.
Hiçbiri "bu kusurun kaynağı promptta mıydı" sorusunu toplu olarak cevaplamıyor.
Bu soruyu soran tek mercek ⑬ UYUM ve tablosu bugüne kadar HİÇ koşmadı
(T13_UYUM_KALITE.md). Aynı borç ikinci kez yazılı: URETIM_ONCESI_ANALIZ/
01_DERS_ETKINLIK_RAPORU.md 01.08.2026 kesitinde dondu, D51+ hiç ölçülmedi.

NE YAPAR: her ham raporun ÇAPA TAŞIYAN (zaman damgası ya da sahne no) 🔴/🟠
bulgusunu o filmin PROMPT SAHNESİNE bağlar ve defteri basar. Hükmü (🅐 model
sapması / 🅑 prompt boşluğu) BU BETİK VERMEZ — o okumak ister, sayma işi değil.
Betiğin işi: bulguyu sahneye oturtmak, geçersiz koşuları dışarıda tutmak,
tekilleştirmek ve önerilen kapı regex'inin yanlış-pozitifini ÖLÇMEK.

⛔ DOSYA YAZMAZ — `--yaz` verilmedikçe her şey ekrana basılır.
⛔ Ölçülen filmin promptuna DOKUNMAZ (T13 kuralı: prompt tarihtir).

KULLANIM:
  python3 prompt_hata_analizi.py --ozet                 # kapsam + film başına sayı
  python3 prompt_hata_analizi.py --tam                  # bütün defter
  python3 prompt_hata_analizi.py --film KRONOS_SON_SINYAL
  python3 prompt_hata_analizi.py --sahne THE_FALLING_WORLD 42   # promptun kendisi
  python3 prompt_hata_analizi.py --regex-dene "no third person"  # kapı önerisi ölçümü
  python3 prompt_hata_analizi.py --yaz                  # 10_PROMPT_QA_ANALIZI/01_BULGU_DEFTERI.md
"""
import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rapor_kontrol as rk                      # govde_al · alan · mercek_bul · skor_tablosu

KOK = Path(__file__).resolve().parents[1]                       # kilavuzlar_ve_sistem_dosyalari/
DEPO = KOK.parent
HAM = KOK / "FILM_QA_RAPORLARI" / "02_HAM_RAPORLAR"
CIKTI = KOK / "FILM_QA_RAPORLARI" / "10_PROMPT_QA_ANALIZI"

# ⛔ Format klasörleri SABİT LİSTEDEN okunmaz: qa_saglik.py'deki liste 13.09.2026
#    yeniden adlandırmasından sonra güncellenmedi (yatay_10_20_dk_filmler artık yok).
FORMAT_DESEN = re.compile(r"^(yatay|dikey)_.*filmler$")

# ─── bulgu taşıyan bölümler ────────────────────────────────────────
# ⛔ BEYAZ LİSTE DEĞİL KARA LİSTE. Ham arşiv üç kuşak rubrik taşıyor: yeni
#    raporlarda '## SCORES SUMMARY' var, eskilerde HİÇ '##' başlığı yok
#    (THE_FROST_LINE · THE_PAYLOAD · THE_SKYLIGHT …). Beyaz liste o kuşağı
#    sessizce siliyordu — 13 ham rapor, 0 bulgu.
KARA_BOLUM = re.compile(
    r"OUT-OF-SCOPE|SEVERITY TALLY|PRESENCE STRING|BEAT STRING|SETUP STRING|"
    r"KEY DIRECTION STRING|CONFORMANCE STRING|SCENE INVENTORY|REVIEWER NOTES|"
    r"WHAT THIS FILM DOES WELL|THE THREE THINGS WORTH PROTECTING|"
    r"THE ONE THING NOTHING ELSE DOES", re.I)
BASLIK = re.compile(r"^#{2,3}\s+(.+?)\s*$")
SIDDET = re.compile(r"🔴|🟠|\bBLOCKER\b|\bMAJOR\b")
HAFIF = re.compile(r"🟡|\bMINOR\b")
TC = re.compile(r"\b(\d{1,2}):(\d{2})\b")
SREF = re.compile(r"\b[Ss](\d{1,2})\b|\b[Ss]cene\s+(\d{1,2})\b|\bSAHNE\s+(\d{1,2})\b"
                  r"|\bK(\d{1,2})\b|\b[Cc]lip\s+(\d{1,2})\b|\bKL[İI]P\s+(\d{1,2})\b")   # 22.09.2026 klip rejimi
EFSANE = re.compile(r"BLOCKER\s+[—-]\s+Breaks|MAJOR\s+[—-]\s+Clearly|MINOR\s+[—-]\s+Noticeable")
AYRAC = re.compile(r"^\|?\s*[-:|\s]+\|?\s*$")
TALLY = re.compile(r"^\|?\s*(SEVERITY|🔴|🟠|🟡|BLOCKER|MAJOR|MINOR)\s*\|?\s*\d+\s*\|?\s*$", re.I)
MOD = re.compile(r"INPUT MODE\s*[:：]\s*([DV])", re.I)
PLAN_SADAKAT = ("⑨", "⑩", "⑪", "⑫")      # plan sadakati mercekleri [D190]

# ─── ③ KİMLİK KAPISI · OKUMA NOTU ──────────────────────────────────
# Künye aritmetiği (süre/sahne) yarım ve çeyrek masterları meşru saydığı için
# tek başına hüküm veremez; kelime örtüşmesi de ÖLÇÜLDÜ ve AYIRT ETMEDİ.
# Buraya yalnız OKUNMUŞ notlar girer. KARANTİNA (= sayıya girmez) ayrı bir
# karardır ve ancak raporun anlattığı NESNELER filmin nesneleriyle
# eşleşmediğinde verilir.
KIMLIK_NOTU = {
    "THE_FALLING_WORLD":
        "Ham dosyalar kural dışı adlandırılmış (01_KARE_BOLUM_1_2_TEKRAR.md — "
        "<FILM>_<MERCEK>_HAM.md değil) ve 15 dosyanın 9'u künyesiz. **Kimlik "
        "OKUNDU ve TUTTU:** rapordaki kayış/kemer halkası, gri sandık, gümüş "
        "bant, tekerlekli araç, mercekli parlak halka ve iki giysi (beyaz + "
        "kobalt omuz / turuncu + siyah) filmin promptlarıyla eşleşiyor — QA "
        "modelinin 'buggy · duct tape · eclipse ring' demesi aynı nesnelerin "
        "video dilidir. Zaman damgası da tutuyor: promptlar 18.09.2026 14:32, "
        "raporlar aynı gün 22:44. Raporlar filmin İLK YARISI (24 sahne · 240 s). "
        "⚠️ ÜRETİM DEFTERİ ESKİ: defter üretimden ÖNCE yazıldı ve dört referans "
        "sayfasını hâlâ ⬜ gösteriyor — teslim satırları güncellenmeli.",
}
KARANTINA = {}          # ⛔ bugün boş — hiçbir film sayıdan çıkarılmadı

PROMPT_DESEN = re.compile(r"(_BOLUM_\d+\.md$|_PART_[A-Z]\.md$|_FILM\.md$|^FAZ_\d)")
SAHNE_BASLIK = re.compile(r"^#{2,3}\s+.*?(?:SAHNE|KL[İI]P)\s*#?\s*(\d+)", re.M | re.I)   # 22.09.2026: + KLİP
DURDUR = ("STOPWORDS",)
ETKISIZ = set("""the a an and or of in on at to for with from into onto is are was were be been
    it its this that these those as by not no non one two three four five their his her them they
    he she him we you i but if then than there here when while during after before over under
    bir bu şu ve ile de da ki için gibi olarak var yok""".split())


# ─── depo tarafı ───────────────────────────────────────────────────
def format_klasorleri():
    return sorted(p for p in DEPO.iterdir() if p.is_dir() and FORMAT_DESEN.match(p.name))


def film_klasor(film):
    for f in format_klasorleri():
        p = f / film
        if p.is_dir():
            return p
    return None


def prompt_dosyalari(film_dir):
    out = []
    for p in sorted(film_dir.rglob("*.md")):
        rel = p.relative_to(film_dir)
        ad = p.name
        if PROMPT_DESEN.search(ad) or (len(rel.parts) > 1 and PROMPT_DESEN.search(rel.parts[0])):
            out.append(p)
    return out


def sahne_indeksi(film_dir):
    """{sahne_no: (dosya, başlık, gövde)} — prompt dosyalarındaki '## 🎬 SAHNE n' blokları."""
    idx = {}
    for p in prompt_dosyalari(film_dir):
        try:
            metin = p.read_text(encoding="utf-8")
        except Exception:
            continue
        yerler = [(m.start(), int(m.group(1)), m.group(0).strip()) for m in SAHNE_BASLIK.finditer(metin)]
        for i, (bas, no, baslik) in enumerate(yerler):
            son = yerler[i + 1][0] if i + 1 < len(yerler) else len(metin)
            if no not in idx:                       # ilk yazan kazanır (BOLUM sırası)
                idx[no] = (p, baslik, metin[bas:son])
    return idx


def izgara(film_dir):
    """QA_SPEC GRID satırı → (hook_ofset, klip, taban, kaynak_satırı) — yoksa None.

    Depoda dört yazım birden var:
      'sahne başlangıcı(n) = 9 hook + (n−1) × 10 klip'   → ofset 9 · klip 10 · 1-tabanlı
      'sahne başlangıcı(n) = 0 + (n−1) × 10'             → ofset 0 · klip 10 · 1-tabanlı
      'sahne başlangıcı(n) = 9s + (n-1) x 10s'           → ofset 9 · klip 10 · 1-tabanlı
      'scene start(n) = n × clip · clip = 10 s assumed'  → ofset 0 · klip 10 · 0-tabanlı
    ⬜ ile bırakılmış GRID DOLDURULMAMIŞTIR — film B grubunda kalır, uydurulmaz.
    """
    spec = next(iter(sorted(film_dir.glob("*_QA_SPEC.md"))), None)
    if not spec:
        return None
    for satir in spec.read_text(encoding="utf-8", errors="replace").split("\n"):
        if not re.match(r"^[ \t>*]*GRID\s*[:：]", satir):
            continue
        s = satir.split(":", 1)[1].strip()
        if "⬜" in s:
            return None                      # dolmamış ızgara — sayı uydurulmaz
        taban = 1 if re.search(r"\(\s*n\s*[−–-]\s*1\s*\)", s) else 0
        m = re.search(r"[×x]\s*([\d]+(?:[.,]\d+)?)", s)
        klip = float(m.group(1).replace(",", ".")) if m else None
        if klip is None:
            m = re.search(r"\b(?:clip|klip)\b\s*=?\s*([\d]+(?:[.,]\d+)?)", s, re.I)
            klip = float(m.group(1).replace(",", ".")) if m else None
        if not klip:
            return None
        m = re.search(r"=\s*([\d]+(?:[.,]\d+)?)\s*(?:s\b|hook\b|\+)", s, re.I)
        ofset = float(m.group(1).replace(",", ".")) if m else 0.0
        return ofset, klip, taban, s
    return None


def izgara_olc(fd, idx):
    """QA_SPEC GRID yoksa ızgarayı RAPORLARIN KENDİ ÖLÇÜMÜNDEN türet [19.09.2026].

    ⛔ VARSAYIM DEĞİL ÖLÇÜM: her ham raporun künyesindeki RUNTIME ve SCENES
    OBSERVED bölünür. Kabul için üç şart: (a) en az İKİ rapor aynı değerde
    buluşmalı, (b) klip 8-12 s bandında olmalı (deponun ızgarası), (c) raporun
    saydığı sahne filmin sahne sayısının 1/1, 1/2, 1/3 ya da 1/4'ü olmalı
    (yarım ve çeyrek master meşru). Tutmazsa film B grubunda KALIR.
    """
    import collections
    oran, uyusmaz = collections.Counter(), collections.Counter()
    n = len(idx)
    for ham in sorted(fd.glob("*.md")):
        t = ham.read_text(encoding="utf-8", errors="replace")
        sure, _ = rk.sure_sn(rk.alan(t, "RUNTIME", "VIDEO DURATION") or "")
        sahne = rk.ilk_sayi(rk.alan(t, "SCENES OBSERVED", "SCENE COUNT") or "")
        if not sure or not sahne:
            continue
        if not any(abs(sahne - n / k) <= 1 for k in (1, 2, 3, 4)):
            uyusmaz[sahne] += 1                        # ①.9 TESLİM KAPISI izi [D188]
            continue
        oran[round(sure / sahne)] += 1
    if not oran:
        if uyusmaz:
            sah, kac = uyusmaz.most_common(1)[0]
            # ⛔ HÜKÜM DEĞİL LEAD: ①.9'un kendisi rapor_kontrol.py'de koşar ve kareyle
            #    kapanır. Bilinen yanlış-pozitif kaynakları: FAZ yapılı filmlerde rapor
            #    birimi FAZ'dır (YERCEKIMI · THE_SECOND_SHIP); ondalık sahne numarası
            #    (SAHNE 2.5 gibi ara sahneler) plan sayısını düşük gösterir.
            return ("TESLIM", f"⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — "
                              f"plan {n} sahne, {kac} rapor makarada {sah} sahne saydı "
                              f"({n}/1-4'ün hiçbiri değil)")
        return None
    klip, kac = oran.most_common(1)[0]
    if kac < 2 or not (8 <= klip <= 12):
        return None
    return float(klip), float(klip), 1, f"ÖLÇÜLDÜ · {kac} raporun künyesinden: süre ÷ sahne = {klip:g} s"


def sahne_zamanlari(idx, grid):
    """{sahne_no: (başlangıç, bitiş)} — GRID formülünden, birikimli süreden DEĞİL."""
    if not grid or not idx:
        return {}
    ofset, klip, taban, _ = grid
    ilk = min(idx)
    zaman = {}
    for no in sorted(idx):
        bas = ofset + (no - (taban if taban else ilk)) * klip
        zaman[no] = (bas, bas + klip)
    return zaman


def sahne_bul(zaman, saniye):
    for no, (a, b) in zaman.items():
        if a <= saniye < b:
            return no, "zaman"
    ilk = min(zaman)
    if saniye < zaman[ilk][0]:            # ızgara öncesi: hook kartı / önsöz
        return ilk, "hook⟂"
    return None, "—"


def uretim_durumu(film_dir):
    """Üretim defterinden teslim izi — 'hiç kare üretilmedi' filmin QA raporu OLAMAZ."""
    d = next(iter(sorted(film_dir.glob("*_URETIM_DEFTERI.md"))), None)
    if not d:
        return "defter yok"
    t = d.read_text(encoding="utf-8", errors="replace")
    acik = t.count("⬜")
    kapali = t.count("✅")
    return f"defter: ⬜{acik} ✅{kapali}" + ("  ⚠️ ÜRETİM İZİ YOK" if kapali == 0 else "")


def ad_uyar(ad, film):
    """'the cold weld.mp4' filmin ADIDIR; 'THE LAST CUSTODIAN' başka bir filmdir."""
    def belirtec(x):
        x = x.lower().replace("ı", "i").replace("İ", "i")
        x = re.sub(r"\.(mp4|mov|mkv|avi)\b", " ", x)
        return {w for w in re.findall(r"[a-z0-9]{2,}", x)
                if w not in ("the", "part", "bolum", "bölüm", "film", "final", "yeni", "sahne")}
    a, f = belirtec(ad), belirtec(film)
    if not a or not f:
        return True
    return len(a & f) / len(f) >= 0.5


def kimlik_izleri(fd, film, idx, grid):
    """③ KİMLİK KAPISI'nın MAKİNE yarısı — künye izleri. Hüküm okumayla verilir."""
    _of, klip, _tb, _ = grid
    film_sn = len(idx) * klip
    izler = []
    for ham in sorted(fd.glob("*.md")):
        t = ham.read_text(encoding="utf-8", errors="replace")
        ad = rk.alan(t, "FILM")
        sinif = rk.alan(t, "LENGTH CLASS")
        sure, _ = rk.sure_sn(rk.alan(t, "VIDEO DURATION", "RUNTIME") or "")
        sahne = rk.ilk_sayi(rk.alan(t, "SCENES OBSERVED", "SCENE COUNT") or "")
        bayrak, zayif = [], []
        if not ad or "not supplied" in ad.lower():
            zayif.append("künyesiz")            # eski rubriklerde FILM: alanı yoktu
        elif not ad_uyar(ad, film):
            bayrak.append(f"ad≠{ad.strip()[:28]}")
        if sure and not any(abs(sure - film_sn / k) <= film_sn / k * 0.12 for k in (1, 2, 3, 4)):
            bayrak.append(f"süre {sure:g}s ∉ {film_sn:g}/1-4")
        if sahne and not any(abs(sahne - len(idx) / k) <= 1 for k in (1, 2, 3, 4)):
            bayrak.append(f"sahne {sahne}≠{len(idx)}/1-4")
        izler.append((ham.name, sinif or "—", sure, sahne, bayrak, zayif))
    return izler


# ─── bölüm ofseti ──────────────────────────────────────────────────
# ⛔ 6/8 dk hattında QA birimi BÖLÜMDÜR: ikinci yarımın masterı 0:00'dan başlar
#    ama filmin 240. saniyesidir. Ofset verilmezse ikinci yarının BÜTÜN bulguları
#    birinci yarının sahnelerine yazılır — sessiz ve toptan yanlış eşleme.
#    (19.09.2026 · THE_FALLING_WORLD PART2 raporları geldiğinde yakalandı.)
BOLUM_DESEN = [
    re.compile(r"_PART[_ ]?(\d)(?:[_ ](\d))?(?!\d)", re.I),
    re.compile(r"_BOLUM[_ ]?(\d)(?:[_ ](\d))?(?!\d)", re.I),
    re.compile(r"_B(\d)(?:[_ ](\d))?_", re.I),
]


def bolum_ofseti(ad, film_sn, rapor_sn):
    """Dosya adındaki bölüm etiketinden saniye ofseti. Bilinmiyorsa 0.

    Etiket TEK parça ('PART2') ya da ARALIK ('PART3_4' · 'BOLUM_1_2') olabilir.
    ⛔ Ofset ölçülen süreden DEĞİL, ölçülen süreden türetilen PARÇA SAYISINDAN
    hesaplanır: makara nominalden kısa teslim edilmiş olabilir (THE_FALLING_WORLD
    ikinci yarım 230 s ≠ 240 s) ve ölçüyü doğrudan kullanmak ofseti kaydırır.

        kapsanan parça = b - a + 1 (aralıksa) ya da 1
        parça uzunluğu(ölçülen) = rapor_sn / kapsanan
        Q = round(film_sn / parça_ölçülen)            → filmin kaç parçaya bölündüğü
        parça_nominal = film_sn / Q
        ofset = (a - 1) * parça_nominal
    """
    if not film_sn or not rapor_sn or rapor_sn >= film_sn * 0.9:
        return 0.0, None                      # tam master ya da ölçüm yok → ofset YOK
    for rx in BOLUM_DESEN:
        m = rx.search(ad)
        if not m:
            continue
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        kapsanan = max(1, b - a + 1)
        parca_olculen = rapor_sn / kapsanan
        Q = round(film_sn / parca_olculen) if parca_olculen else 0
        if Q < 2 or a > Q:
            return 0.0, a                     # tutarsız etiket → ofset UYDURULMAZ
        return (a - 1) * (film_sn / Q), a
    return 0.0, None


# ─── rapor tarafı ──────────────────────────────────────────────────
def parcala(satir):
    """Bir satırda birden çok bulgu varsa zaman damgalarından böl."""
    parcalar = [p.strip(" |·,;") for p in re.split(r"(?=\b\d{1,2}:\d{2}\b)", satir) if p.strip()]
    if len(parcalar) > 1:
        iyi = [p for p in parcalar if SIDDET.search(p) or TC.search(p)]
        if iyi:
            return iyi
    return [satir.strip()]


def bulgu_satirlari(govde):
    """[(bölüm, satır)] — kara listedeki bölümler hariç, anlamlı satırlar."""
    cur, out = "—", []
    for satir in govde.split("\n"):
        m = BASLIK.match(satir)
        if m:
            cur = m.group(1).strip()
            continue
        if KARA_BOLUM.search(cur):
            continue
        s = satir.strip()
        if len(s) < 45 or AYRAC.match(s) or TALLY.match(s) or EFSANE.search(s):
            continue
        if re.match(r"^\|?\s*(Observation|Category|Beat|Timecode|Scene|What)\b", s):
            continue
        out.append((cur[:40], s))
    return out


def temizle(s):
    s = re.sub(r"^[\s*|\-–—>\d.]+", "", s)
    s = re.sub(r"\*\*|`|\|", " ", s)
    return re.sub(r"\s{2,}", " ", s).strip(" |")


def imza(s):
    kel = {w for w in re.findall(r"[a-zçğıöşü]{4,}", s.lower()) if w not in ETKISIZ}
    return kel


class Bulgu:
    __slots__ = ("film", "mercek", "mod", "ham", "bolum", "bicim", "siddet", "saniye",
                 "sref", "sahne", "kaynak", "metin", "gorenler")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))
        self.gorenler = kw.get("gorenler") or []


def rapor_bulgulari(yol, film, zaman, taban_farki, sahne_araligi=None, film_sn=None):
    metin = yol.read_text(encoding="utf-8", errors="replace")
    govde = rk.govde_al(metin)
    rows = rk.skor_tablosu(govde)
    # ⛔ rk.kesik_mi 14.09.2026 QA ÇIKTI SÖZLEŞMESİ için yazıldı ve 'SCORES SUMMARY
    #    başlığı yok' diyerek SÖZLEŞME ÖNCESİ kuşağı toptan siliyor. O kuşak kesik
    #    koşu değil, ESKİ BİÇİM: kendi şiddet tablosu var (THE_FROST_LINE 🔴 BLOCKER
    #    satırları). Kesiklik ölçüsü yalnız sözleşmeli raporlara uygulanır.
    if rk.SKOR_BASLIK.search(govde):
        kesik, sebep = rk.kesik_mi(govde, rows)
        if kesik:
            return [], f"✂️ KESİK · {sebep}"
        bicim = "sözleşmeli"
    else:
        if re.search(r"MEDIA MISSING|no media|medya yok", govde, re.I):
            return [], "✂️ KESİK · medya yok"
        bicim = "eski biçim"
    mod = MOD.search(metin)
    mod = mod.group(1).upper() if mod else "V"
    mercek = rk.mercek_bul(govde)
    modv_atlanan = 0
    rapor_sn, _ = rk.sure_sn(rk.alan(metin, "RUNTIME", "VIDEO DURATION") or "")
    ofset, bolum_no = bolum_ofseti(yol.name, film_sn or 0, rapor_sn)
    out = []
    for bolum, satir in bulgu_satirlari(govde):
        for parca in parcala(satir):
            if not SIDDET.search(parca):
                continue
            t = TC.search(parca)
            saniye = int(int(t.group(1)) * 60 + int(t.group(2)) + ofset) if t else None
            sm = SREF.search(parca)
            sref = int(next(g for g in sm.groups() if g)) if sm else None
            sahne, kaynak = None, "—"
            if saniye is not None and zaman:
                sahne, kaynak = sahne_bul(zaman, saniye)
                if ofset and kaynak != "—":
                    kaynak = f"B{bolum_no}+"
            if sahne is None and sref is not None:
                sahne = sref + taban_farki
                kaynak = "≈S-ref"
            if sahne is None:
                continue                      # çapasız satır bu işin kapsamında değil
            if sahne_araligi and not (sahne_araligi[0] <= sahne <= sahne_araligi[1]):
                continue                      # ızgara dışına düşen çapa — uydurulmaz
            govde_metin = temizle(parca)
            if len(imza(govde_metin)) < 5:
                continue                      # tablo kırıntısı, bulgu değil
            if mod == "V" and mercek.startswith(PLAN_SADAKAT):
                continue                      # ⑨-⑫ mod V: plan uydurma riski [D190]
            out.append(Bulgu(film=film, mercek=mercek, mod=mod, ham=yol.name, bolum=bolum, bicim=bicim,
                             siddet="🔴" if re.search(r"🔴|BLOCKER", parca) else "🟠",
                             saniye=saniye, sref=sref, sahne=sahne, kaynak=kaynak,
                             metin=govde_metin[:300], gorenler=[mercek]))
    return out, None


def tekille(bulgular):
    """Aynı filmde aynı sahnede aynı kusuru birden çok mercek yazdıysa tek satır."""
    out = []
    for b in bulgular:
        ib = imza(b.metin)
        esles = None
        for o in out:
            if o.sahne != b.sahne:
                continue
            io = imza(o.metin)
            if not ib or not io:
                continue
            ortak = len(ib & io) / max(1, len(ib | io))
            if ortak >= 0.45:
                esles = o
                break
        if esles:
            if b.mercek not in esles.gorenler:
                esles.gorenler.append(b.mercek)
            if b.siddet == "🔴":
                esles.siddet = "🔴"
        else:
            out.append(b)
    return out


# ─── tarama ────────────────────────────────────────────────────────
def tara(yalniz=None):
    A, B, C = {}, [], []
    kesik_say = 0
    for fd in sorted(HAM.iterdir()):
        if not fd.is_dir():
            continue
        film = fd.name
        if yalniz and film != yalniz:
            continue
        d = film_klasor(film)
        if not d:
            C.append((film, len(list(fd.glob("*.md"))), "film klasörü yok"))
            continue
        idx = sahne_indeksi(d)
        if not idx:
            C.append((film, len(list(fd.glob("*.md"))), "prompt sahne başlığı yok"))
            continue
        grid = izgara(d)
        olculdu = False
        if not grid:
            grid = izgara_olc(fd, idx)
            if grid and grid[0] == "TESLIM":
                B.append((film, len(list(fd.glob("*.md"))), len(idx), grid[1]))
                continue
            olculdu = bool(grid)
        if not grid:
            B.append((film, len(list(fd.glob("*.md"))), len(idx),
                      "QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor"))
            continue
        zaman = sahne_zamanlari(idx, grid)
        taban_farki = min(idx) - 1 if min(idx) == 0 else 0
        aralik = (min(idx), max(idx))
        bulgular, hamlar, kesikler = [], 0, []
        for ham in sorted(fd.glob("*.md")):
            bs, durum = rapor_bulgulari(ham, film, zaman, taban_farki, aralik,
                                        film_sn=len(idx) * grid[1])
            if durum:
                kesik_say += 1
                kesikler.append((ham.name, durum))
                continue
            hamlar += 1
            bulgular += bs
        A[film] = {"dir": d, "idx": idx, "grid": grid, "zaman": zaman, "olculdu": olculdu,
                   "ham": hamlar, "ham_toplam": len(list(fd.glob("*.md"))),
                   "kesik": kesikler, "uretim": uretim_durumu(d),
                   "kimlik": kimlik_izleri(fd, film, idx, grid),
                   "ham_bulgu": bulgular, "bulgu": tekille(bulgular)}
    return A, B, C, kesik_say


# ─── çıktı ─────────────────────────────────────────────────────────
def ozet(A, B, C, kesik):
    ham = sum(v["ham"] for v in A.values())
    hb = sum(len(v["ham_bulgu"]) for v in A.values())
    tk = sum(len(v["bulgu"]) for v in A.values())
    print("🔎 PROMPT HATA ANALİZİ — kapsam")
    a1 = [f for f, v in A.items() if not v.get("olculdu")]
    a2 = [f for f, v in A.items() if v.get("olculdu")]
    print(f"   A1 · belgeli ızgara       {len(a1):3d}   (prompt sahneleri + QA_SPEC GRID)")
    print(f"   A2 · ÖLÇÜLMÜŞ ızgara      {len(a2):3d}   (GRID yok · raporun künyesinden türetildi)")
    print(f"   B · GRID yok              {len(B):3d}   (ikinci tur)")
    print(f"   C · eşleşmeyen            {len(C):3d}   (rapor edilir, zorlanmaz)")
    print(f"   ham rapor (A, geçerli)    {ham:3d}   · ✂️ KESİK atlanan: {kesik}")
    print(f"   🔴/🟠 çapalı bulgu        {hb:4d}  → tekilleştirmeden sonra {tk}")
    print()
    print("   film                        ham  bulgu  tekil  sahne  ızgara")
    for f, v in sorted(A.items(), key=lambda t: -len(t[1]["bulgu"])):
        h, k, tb, _ = v["grid"]
        print(f"   {f:26s} {v['ham']:4d} {len(v['ham_bulgu']):6d} {len(v['bulgu']):6d} "
              f"{len(v['idx']):6d}  hook {h:g}s · klip {k:g}s")


def film_dok(A, film, tam=False):
    v = A[film]
    print(f"# {film}")
    h, k, tb, gs = v["grid"]
    print(f"IZGARA{' ⭐ÖLÇÜLDÜ' if v.get('olculdu') else ''}: hook {h:g} s · klip {k:g} s · sahne {len(v['idx'])} "
          f"({min(v['idx'])}-{max(v['idx'])}) · kaynak: {gs[:90]}")
    print(f"HAM: {v['ham']}/{v['ham_toplam']} geçerli · bulgu {len(v['ham_bulgu'])} → tekil {len(v['bulgu'])}")
    print(f"ÜRETİM: {v['uretim']}")
    bayrakli = [i for i in v["kimlik"] if i[4]]
    kunyesiz = sum(1 for i in v["kimlik"] if i[5])
    print(f"③ KİMLİK İZİ: {len(bayrakli)}/{len(v['kimlik'])} güçlü bayrak · {kunyesiz} künyesiz")
    for ad, sinif, sure, sahne, bayrak, _z in bayrakli:
        print(f"    ⚠️  {ad}  sınıf={sinif}  süre={sure}  sahne={sahne}  → {' · '.join(bayrak)}")
    for ad, durum in v["kesik"]:
        print(f"    ✂️  {ad}  {durum}")
    print()
    for b in sorted(v["bulgu"], key=lambda x: (x.sahne, x.siddet)):
        zaman = f"{b.saniye // 60}:{b.saniye % 60:02d}" if b.saniye is not None else "—"
        print(f"S{b.sahne:02d} {b.siddet} [{b.kaynak:6s} {zaman:>5s}] "
              f"({'·'.join(m.split()[0] for m in b.gorenler)}) {b.metin}")
        if tam:
            print(f"        ← {b.ham} · {b.bolum} · mod {b.mod}")


def sahne_dok(A, film, no):
    v = A[film]
    if no not in v["idx"]:
        print(f"⛔ {film} S{no} yok · mevcut: {min(v['idx'])}-{max(v['idx'])}")
        return
    p, baslik, govde = v["idx"][no]
    a, b = v["zaman"][no]
    print(f"# {film} S{no} · {a:g}-{b:g} s · {p.relative_to(DEPO)}")
    print(govde)


# ─── kilit envanteri — adjudikasyonun makine yarısı ────────────────
# Hüküm (🅐/🅑) okumayla verilir; bu tablo OKUMAYI HIZLANDIRIR, yerine geçmez.
# Her satır: kilit filmin kaç promptunda var VE bulgunun düştüğü sahnede var mı.
KILITLER = [
    ("SES",      r"^AUDIO:"),
    ("dış-ses",  r"no exterior sound|in silence|no sound outside|vacuum carries no"),
    ("sayı",     r"exactly\s+(?:\d+|one|two|three|zero)\s+human"),
    ("temas",    r"no merging|no phasing|clear boundary|no extra fingers"),
    ("giysi",    r"identical throughout|suit identical|no drift|wear (?:state|marks)"),
    ("parçacık", r"particles obey|continuous momentum|never hovering|no floating"),
    ("bloom",    r"0% bloom|no bloom"),
    ("metin",    r"no readable text|no text"),
    ("efor",     r"forearm|shoulders drop|shorter than the first|braced|tremor|breath"),
    ("g-ad",     r"zero gravity|micro-?gravity|zero-?g\b|low gravity|gravity is|gravity of|the stated gravity"),
    ("g-sayı",   r"\d[.,]?\d*\s*g\b(?!\w)|m/s[²2]"),   # SAYI — "about two thirds of Earth" TARİFTİR, sayılmaz
    ("filigran", r"no watermark"),
    ("kamera",   r"locked-off|single continuous shot|single unbroken take"),
]


def kilit_dok(A, film):
    v = A[film]
    korpus = "\n".join(g for _, _, g in v["idx"].values())
    n = len(v["idx"])
    print(f"# {film} — KİLİT ENVANTERİ ({n} sahne)")
    print(f"{'kilit':10s} {'film geneli':>12s}")
    for ad, rx in KILITLER:
        var = sum(1 for _, _, g in v["idx"].values() if re.search(rx, g, re.I | re.M))
        print(f"{ad:10s} {var:6d}/{n:<5d}")
    ilgili = sorted({b.sahne for b in v["bulgu"]})
    print()
    print("S    " + " ".join(f"{ad[:6]:>7s}" for ad, _ in KILITLER))
    for no in ilgili:
        g = v["idx"][no][2]
        print(f"S{no:03d} " + " ".join(
            f"{('+' if re.search(rx, g, re.I | re.M) else '.'):>7s}" for _, rx in KILITLER))


# ─── temas sınıfı · TUR 22 sınaması ────────────────────────────────
# ⛔ 19.09.2026 · sahne sahne okuma iki hata buldu, ikisi de buraya yazıldı:
#   ① "merg" kalıbı EMERGENCY kelimesini yakalıyordu → 12 yanlış bulgu.
#      Kelime sınırı ZORUNLU.
#   ② Temas cümlesi promptlarda "HAND-surface contacts" diyor — yani TEK YÖNLÜ.
#      Nesne-nesne geçişi (kayış ↔ pim, halat ↔ abajur, kemer ↔ gövde) hiçbir
#      cümleyle kapalı DEĞİL ve o bulgular 🅐 değil 🅑'dir.
TEMAS_ARIZA = re.compile(
    r"\bmerg(e|es|ed|ing)\b|\bfus(e|es|ed|ing|ion)\b|\bphas(e|es|ed|ing)\b|"
    r"\bclip(s|ping|ped)?\s+(through|into|directly)|\bmelt(s|ed|ing)?\b|"
    r"\bextra finger|contact morph|passes?\s+(directly\s+)?through|embedded inside|"
    r"interpenetrat|geometry clipping", re.I)
EL_BULGUDA = re.compile(r"\b(glove[ds]?|finger[s]?|hand[s]?|thumb|palm|grip|grasp|knuckle)\b", re.I)
EL_SAHNEDE = re.compile(r"\b(glove[ds]?|finger[s]?|hand[s]?|grip[s]?|grasp|thumb|palm)\b", re.I)


def temas_testi(A):
    """TUR 22 · temas cümlesi koruyor mu — maruziyet kontrollü [19.09.2026]."""
    import math
    rx = dict(KILITLER)["temas"]
    el = [b for v in A.values() for b in v["bulgu"]
          if TEMAS_ARIZA.search(b.metin) and EL_BULGUDA.search(b.metin)]
    ne = [b for v in A.values() for b in v["bulgu"]
          if TEMAS_ARIZA.search(b.metin) and not EL_BULGUDA.search(b.metin)]
    print("🤚 TEMAS SINAMASI — TUR 22")
    print(f"   temas/geçiş bulgusu   {len(el) + len(ne)}")
    print(f"     EL karışan          {len(el):3d}   ← cümlenin KAPSADIĞI")
    print(f"     NESNE-NESNE         {len(ne):3d}   ⛔ hiçbir cümle kapsamıyor → 🅑")
    for ad, yalniz_el in (("tüm temas/geçiş", False), ("yalnız EL karışan", True)):
        a = b = c = e = 0
        for v in A.values():
            bul = {x.sahne for x in v["bulgu"] if TEMAS_ARIZA.search(x.metin)
                   and (not yalniz_el or EL_BULGUDA.search(x.metin))}
            for no, (_p, _x, g) in v["idx"].items():
                if not EL_SAHNEDE.search(g):
                    continue
                var, hata = bool(re.search(rx, g, re.I | re.M)), no in bul
                a, b, c, e = (a + 1, b, c, e) if (var and hata) else \
                             (a, b + 1, c, e) if var else \
                             (a, b, c + 1, e) if hata else (a, b, c, e + 1)
        tv, ty = a + b, c + e
        o1, o2 = a / max(1, tv), c / max(1, ty)
        se = math.sqrt(o1 * (1 - o1) / max(1, tv) + o2 * (1 - o2) / max(1, ty))
        z = (o1 - o2) / se if se else 0
        print(f"   ── {ad} · el kadrajda olan sahneler")
        print(f"      cümle VAR {a:3d}/{tv:<4d} %{100 * o1:5.2f}   "
              f"cümle YOK {c:3d}/{ty:<4d} %{100 * o2:5.2f}   "
              f"RR {o1 / max(o2, 1e-9):.2f} · z≈{z:+.2f}")


def regex_dene(desen):
    """Önerilen kapı regex'ini BÜTÜN prompt korpusunda koştur — yanlış pozitif ÖLÇÜLÜR."""
    # ⛔ BÜYÜK/küçük harf DUYARLI ve çok satırlı: kapı önerilerinin çoğu (jeton
    #    sızıntısı · satır başı çapaları) harf büyüklüğüne bağlıdır. Harf
    #    duyarsızlık isteniyorsa desenin başına (?i) yazılır.
    rx = re.compile(desen, re.M)
    isabet, toplam_sahne, filmler = 0, 0, Counter()
    for f in format_klasorleri():
        for d in sorted(f.iterdir()):
            if not d.is_dir():
                continue
            idx = sahne_indeksi(d)
            if not idx:
                continue
            for no, (_p, _b, govde) in idx.items():
                toplam_sahne += 1
                if rx.search(govde):
                    isabet += 1
                    filmler[d.name] += 1
    print(f"🔬 KAPI DENEMESİ · desen: {desen}")
    print(f"   taranan sahne : {toplam_sahne}")
    print(f"   isabet        : {isabet}  (%{100 * isabet / max(1, toplam_sahne):.1f})")
    print(f"   isabetli film : {len(filmler)}")
    for k, n in filmler.most_common(20):
        print(f"      {n:4d}  {k}")


def defter_yaz(A, B, C, kesik):
    CIKTI.mkdir(parents=True, exist_ok=True)
    yol = CIKTI / "01_BULGU_DEFTERI.md"
    L = ["# 📒 BULGU DEFTERİ — makine çıktısı",
         "",
         "> ⛔ Bu dosya ELLE YAZILMAZ. Kaynağı:",
         "> `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/prompt_hata_analizi.py --yaz`",
         "> Hüküm sütunu (🅐/🅑/🅒/🅓) burada YOKTUR — o `02_FILM_ANALIZLERI/` içinde,",
         "> prompt metni okunarak verilir. Burada yalnız bulgunun hangi sahneye",
         "> oturduğu yazar.",
         "", "```",
         f"A · tam eşleşen film   {len(A)}",
         f"B · GRID yok           {len(B)}",
         f"C · eşleşmeyen         {len(C)}",
         f"ham rapor (geçerli)    {sum(v['ham'] for v in A.values())}   · ✂️ KESİK atlanan {kesik}",
         f"🔴/🟠 çapalı bulgu     {sum(len(v['ham_bulgu']) for v in A.values())}"
         f" → tekil {sum(len(v['bulgu']) for v in A.values())}",
         "```", ""]
    kar = [f for f in A if f in KARANTINA]
    if kar:
        L += ["## ⛔ KARANTİNA — ③ KİMLİK KAPISI", "",
              "Raporları BU filme ait olmayan filmler. Satırları defterde durur ama",
              "sınıf tablosuna GİRMEZ ve ders üretmez.", ""]
        for f in kar:
            L += [f"**{f}** — {KARANTINA[f]}", ""]
    else:
        L += ["## ③ KİMLİK KAPISI", "",
              "⛔ **Bugün hiçbir film karantinada değil** — hiçbir filmin raporu sayıdan",
              "çıkarılmadı. Künye izleri her filmin başlığında basılı; okuma notu",
              "gerektiren filmler `③ KİMLİK NOTU` satırı taşır.", ""]
    for f, v in sorted(A.items(), key=lambda t: -len(t[1]["bulgu"])):
        h, k, _tb, _gs = v["grid"]
        bayrakli = [i for i in v["kimlik"] if i[4]]
        L += [f"## {f}" + ("  ⛔ KARANTİNA" if f in KARANTINA else ""), "",]
        if f in KIMLIK_NOTU:
            L += [f"> ③ **KİMLİK NOTU** — {KIMLIK_NOTU[f]}", ""]
        L += [
              f"`ızgara hook {h:g} s · klip {k:g} s · sahne {len(v['idx'])} · "
              f"ham {v['ham']}/{v['ham_toplam']} geçerli · bulgu {len(v['ham_bulgu'])} → tekil {len(v['bulgu'])}`",
              "",
              f"`③ kimlik: {len(bayrakli)}/{len(v['kimlik'])} güçlü bayrak · üretim {v['uretim']}`",
              "",
              "| S | ş | çapa | gören mercek | bulgu |", "|---|:--:|---|---|---|"]
        for b in sorted(v["bulgu"], key=lambda x: (x.sahne, x.siddet)):
            zaman = f"{b.saniye // 60}:{b.saniye % 60:02d}" if b.saniye is not None else "—"
            gor = " · ".join(m.split()[0] for m in b.gorenler)
            L.append(f"| S{b.sahne:02d} | {b.siddet} | {b.kaynak} {zaman} | {gor} | "
                     f"{b.metin.replace('|', '/')} |")
        L.append("")
    yol.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"✅ yazıldı: {yol.relative_to(DEPO)}  ({len(L)} satır)")

    E = ["# 🚧 EŞLEŞMEYENLER — dürüst borç kaydı", "",
         "> Kaynak: `prompt_hata_analizi.py --yaz` · elle yazılmaz.",
         "> Bu dosyanın işi ZORLAMAK değil, neyin NEDEN dışarıda kaldığını adıyla yazmak.",
         "", "## B · PROMPT VAR, IZGARA YOK", "",
         "`QA_SPEC`'in `GRID:` satırı yok ya da ⬜ ile boş bırakılmış. Zaman damgası",
         "sahneye çevrilemez; ızgara plandan türetilirse ikinci turda girerler.", "",
         "| film | ham | sahne | sebep |", "|---|:--:|:--:|---|"]
    for f, n, sc, sebep in B:
        E.append(f"| {f} | {n} | {sc} | {sebep} |")
    E += ["", "## C · EŞLEŞMEYEN", "",
          "| film | ham | sebep |", "|---|:--:|---|"]
    for f, n, sebep in C:
        E.append(f"| {f} | {n} | {sebep} |")
    E += ["", "```",
          f"B toplamı: {len(B)} film · {sum(x[1] for x in B)} ham rapor",
          f"C toplamı: {len(C)} film · {sum(x[1] for x in C)} ham rapor",
          "```"]
    yolE = CIKTI / "05_ESLESMEYENLER.md"
    yolE.write_text("\n".join(E) + "\n", encoding="utf-8")
    print(f"✅ yazıldı: {yolE.relative_to(DEPO)}")


def main():
    ap = argparse.ArgumentParser(description="ham QA bulgusu × prompt metni")
    ap.add_argument("--ozet", action="store_true")
    ap.add_argument("--tam", action="store_true")
    ap.add_argument("--film")
    ap.add_argument("--sahne", nargs=2, metavar=("FILM", "NO"))
    ap.add_argument("--regex-dene", dest="regex")
    ap.add_argument("--yaz", action="store_true")
    ap.add_argument("--eslesmeyen", action="store_true")
    ap.add_argument("--kilit", metavar="FILM")
    ap.add_argument("--temas-testi", dest="temas", action="store_true")
    a = ap.parse_args()

    if a.regex:
        regex_dene(a.regex)
        return
    if a.temas:
        temas_testi(tara()[0])
        return
    if a.kilit:
        A, *_ = tara(yalniz=a.kilit)
        if a.kilit not in A:
            print(f"⛔ {a.kilit} A grubunda değil")
            return
        kilit_dok(A, a.kilit)
        return
    if a.sahne:
        A, *_ = tara(yalniz=a.sahne[0])
        if a.sahne[0] not in A:
            print(f"⛔ {a.sahne[0]} A grubunda değil")
            return
        sahne_dok(A, a.sahne[0], int(a.sahne[1]))
        return

    A, B, C, kesik = tara(yalniz=a.film)
    if a.film:
        if a.film not in A:
            print(f"⛔ {a.film} A grubunda değil (B/C listesine bak: --eslesmeyen)")
            return
        film_dok(A, a.film, tam=a.tam)
        return
    if a.eslesmeyen:
        print("B · PROMPT VAR / GRID YOK")
        for t in B:
            print(f"   {t[0]:26s} ham={t[1]:3d} sahne={t[2]:3d}  {t[3]}")
        print("\nC · EŞLEŞMEYEN")
        for t in C:
            print(f"   {t[0]:26s} ham={t[1]:3d}  {t[2]}")
        return
    if a.yaz:
        defter_yaz(A, B, C, kesik)
        return
    ozet(A, B, C, kesik)
    if a.tam:
        print()
        for f in sorted(A, key=lambda x: -len(A[x]["bulgu"])):
            print()
            film_dok(A, f, tam=True)


if __name__ == "__main__":
    main()
