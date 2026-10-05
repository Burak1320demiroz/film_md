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
#     ① SPEC KAPISI     film klasöründe *_QA_SPEC.md varken ①/④/⑥/⑦/⑧/⑨-⑫
#                       mod V ise → TEKRAR (tabloya satır YOK)        [D129]
#                       ⑨-⑫ mod V ise → GEÇERSİZ (karantina)          [D190]
#     ⑨⑩⑪ DİZİ         SETUP / GAZE / KEY DIRECTION STRING uzunluğu = kesme+1;
#                       ⑨'da dizi SPEC'in KURULUM İSKELETİ ile kıyaslanır  [D184]
#     ⑫ TAHMİN          DROP-OFF PREDICTION üç saniye + sabit listeden sebep  [D184]
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
#     ⑤ ÇAPRAZ          birden çok rapor: kesme yayılımı · şerit · replik · SÜRE [D205] ·
#                       ⭐ SUSKUNLUK (film boyu iddia + sahibin sessizliği)
#                                                                [D107·D162]
#     ①.11 BÖLÜM        --bolum n/m (13.09.2026 · 6/8 dk hattı): QA birimi
#                       BÖLÜM olan filmde yarım masterın rapor(lar)ı. ①.9
#                       teslim kapısı YALNIZ o parçanın bölüm dosya(lar)ını
#                       sayar (19.09.2026 · §2.8: k dosya / m parça eşlemesi,
#                       16 dk = 8 dosya / 4 PART → bolum_dosyalari()); uç
#                       kategoriler (baş bölümde final, son bölümde hook,
#                       hepsinde bütün-film dörtlüsü) `—` olur — D185'in
#                       yarım-film uzantısı. Kural: KILAVUZ_REHBERI §2.6/§2.7
#     ⑭ ⑮ (14.09.2026)  HAREKET (hareket mantığı) · YÖN (yön/hedef): PURPOSE / VECTOR
#                       STRING uzunluğu = kesme+1 · MOVEMENTS/ACTS sayımı · PREMISE
#                       REGISTER (SPEC NOVUM'luysa) · VERDICT_SOZLUK · mod D listesi
#  ─── 14.09.2026 · QA ÇIKTI REFORMU (FAZ 0-1) ─────────────────────────
#     ✂️ KESİK          SCORES SUMMARY yok / hücre yok / MEDIA MISSING → koşu DEĞİL:
#                       tabloya, ⑤ çaprazına, frekansa girmez; yeniden koşulur
#     ①.13 HÜKÜM        VERDICT: satırı var mı · rubriğin KAPALI listesinde mi
#                       (VERDICT_SOZLUK — tek kaynak; ders_frekans buradan okur)
#     ①.5 (yeni sözleşme) rubrik artık tally/toplam/ortalama İSTEMEZ; model
#                       yalnız hücre + etiket + timecode yazar, bu betik sayar.
#                       Eski raporlarda iddia varsa yine kıyaslanır (kayıt).
#     govde_al          '---' künye değil raporun başlık bloğunu kapatıyorsa
#                       atlanmaz (mod "?" sahte bulgusu kapandı)
#
#  KULLANIM:
#      python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
#              <rapor.md> [<rapor.md> ...] [--film <film klasörü>] \
#              [--hook 10] [--klip 10] [--rapor] [--bolum n/m]
#
#  ÇIKTI:   rapor başına GO / ŞARTLI / TEKRAR / GEÇERSİZ / ✂️ KESİK + TABLOYA GİRECEK SAYI
#  ÇIKIŞ:   0 = hepsi GO · 1 = en az bir ŞARTLI · 2 = TEKRAR, GEÇERSİZ ya da KESİK var
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
    # ─── PLAN SADAKATİ MERCEKLERİ [D184 · 06.09.2026] ───
    ("⑨ KADRAJ",     re.compile(r"SETUP LEDGER|SETUP STRING|RHYME PAIR|LOCKOFF VERIFICATION|"
                                r"Setup Fidelity|SETUPS REGISTERED", re.I)),
    ("⑩ OYUNCULUK",  re.compile(r"PERFORMANCE LEDGER|GAZE STRING|THE CHOICE ON THE BODY|"
                                r"CHANNEL REGISTER|SCENES TASK ONLY|Hands as Intent", re.I)),
    ("⑪ IŞIK",       re.compile(r"LIGHT LEDGER|KEY DIRECTION STRING|LIGHT JUMP LOG|"
                                r"ZONE REGISTER|ZONES REGISTERED|Key Direction Continuity", re.I)),
    ("⑫ HOOK",       re.compile(r"HOOK LEDGER|INTERSTITIAL CHECK|DROP-OFF PREDICTION|"
                                r"WINDOW REGISTER|OPENING WINDOW|Cover Second", re.I)),
    # ─── HAREKET MANTIĞI + YÖN/HEDEF [⑭ ⑮ · 14.09.2026 · sahip talebi] ───
    # "saçma sapan hareketler · yanlış yere dönmek/ateş etmek" — ders çıkarabilmek için
    ("⑭ HAREKET",    re.compile(r"MOTION LEDGER|PURPOSE STRING|PURPOSELESS MOVEMENTS|MOTION SENSE|"
                                r"Purpose Legibility|Locomotion Sense|Turn & Rotation Logic|"
                                r"MOVEMENTS LOGGED", re.I)),
    ("⑮ YÖN",        re.compile(r"TARGET LEDGER|VECTOR STRING|VECTOR LOCK|MISSED VECTORS|"
                                r"DIRECTION & TARGET|Target Establishment|Reach & Aim|"
                                r"Screen Direction Across Cuts|ACTS LOGGED|ACTS MISSED", re.I)),
    # ─── ÜRETİM SADAKATİ MERCEĞİ [⑬ · 11.09.2026] ───
    # Sahne ↔ PROMPT. ⑨-⑫ planı okur, bu mercek modele GÖNDERİLEN metni okur.
    ("⑬ UYUM",       re.compile(r"CONFORMANCE LEDGER|CONFORMANCE STRING|ATTRIBUTION SUMMARY|"
                                r"LESSON ORDERS|CONFORMANCE COUNT|LOCKS CHECKED|"
                                r"PROMPT GAP|MODEL DRIFT", re.I)),
]
ZORUNLU_FILM = ("① KARE", "② DEVAMLILIK", "③ SES", "④ HİKAYE")
ZORUNLU_FRAGMAN = ("① KARE",)
FRAGMAN_IZI = re.compile(r"FRAGMAN|TEASER|TRAILER", re.IGNORECASE)
MOD_D_MERCEKLER = ("① KARE", "④ HİKAYE", "⑥ FİZİK",
                   "⑦ AKSİYON", "⑧ EFOR",
                   "⑨ KADRAJ", "⑩ OYUNCULUK", "⑪ IŞIK", "⑫ HOOK",
                   "⑬ UYUM", "⑭ HAREKET", "⑮ YÖN")   # yalnız bunların MODE D bölümü var
# ⑨-⑫ planı ekrana karşı okur: SPEC varken mod V koşusu tanım gereği BOŞTUR
PLAN_SADAKATI_MERCEKLER = ("⑨ KADRAJ", "⑩ OYUNCULUK", "⑪ IŞIK", "⑫ HOOK")   # [D190] mod V = 🚨 GEÇERSİZ
# ⑬ promptu ekrana karşı okur: PROMPT METNİ GİRDİNİN KENDİSİDİR.
# ⑨-⑫'de belgesiz koşu "geçersiz"dir; burada daha sert — mod V diye bir hâli YOKTUR.
URETIM_SADAKATI_MERCEKLER = ("⑬ UYUM",)   # [11.09.2026] promptsuz koşu = KOŞU DEĞİL
DIZI_MERCEKLER = {   # mercek → (dizi başlığı, alfabe) — "OBSERVED:" satırından okunur [D184]
    "⑨ KADRAJ":    ("SETUP STRING",         "A-Z?"),
    "⑩ OYUNCULUK": ("GAZE STRING",          "OADU-"),
    "⑪ IŞIK":      ("KEY DIRECTION STRING", "0-9TEW?-"),
    # ⛔ tire SONDA: sınıf `[ \t{alfabe}]` diye kuruluyor; tire başa yazılırsa
    #    `\t-K` bir ARALIĞA dönüşür ve dizi yerine rakam/noktalama da yutulur
    #    (11.09.2026'da ölçüldü; D194'ün aynası).
    "⑬ UYUM":      ("CONFORMANCE STRING",   "KTPY-"),
}
ISKELET_ETIKET = re.compile(r"^KURULUM İSKELETİ\s*[:：]\s*([A-Z](?:\s*[A-Z])+)", re.M)
DUSUS_SEBEP = re.compile(r"slow open|no stakes yet|plateau|repeated setup|unreadable beat|card", re.I)

# ─── ①.6 NOVUM KAPISI [D166] ───────────────────────────────────────
# PREMISE REGISTER / PREMISE GATE taşıyan mercekler
NOVUM_MERCEKLER = ("⑥ FİZİK", "⑦ AKSİYON", "⑧ EFOR", "⑭ HAREKET", "⑮ YÖN")
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


# ─── ①.7 NOVUM SINIR KAPISI [D183] ─────────────────────────────────
# ⑩ ÖNERME KAPISI yalnız DÜŞÜRÜR: kaynağı planda yazılı bulgunun puanını
# geri verir. Kuralın NEREDE BİTTİĞİNİ hiçbir kapı sormuyordu — ve düşen
# bulgunun altındaki SINIR İHLALİ onunla birlikte gömülüyordu.
# SPEC'in NOVUM bloğundaki ⛔ satırları kuralın sınırını yazar; kapı onları
# ekrana basar ve kareyle sınanmalarını ister.
NOVUM_SINIR_SATIRI = re.compile(r"⛔\s*(.+?)\s*$")
ETIKET_SATIRI = re.compile(r"^[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜ′\s]{2,}\S")


# ─── ①.10 GÖZ KAPILARI KAPISI [D191] ───────────────────────────────
# SPEC'in F bloğu (GÖZ KAPILARI) filmin KENDİ kapılarıdır: makineye inmeyen,
# tek kareyle kapanan maddeler. Hiçbir merceğin kapsamında değiller ve bu
# yüzden hiç koşulmuyorlardı — THE OPEN CIRCUIT'te on iki maddenin BEŞİ
# ekranda ihlal edildi (ağız · kubbe kask · şimşek · şerit geri yandı ·
# metin+filigran) ve on iki merceğin on ikisi sıfırını yazdı.
# Kapı bulgu üretmez: maddeleri EKRANA BASAR, kareyle kapatılmalarını ister.
GOZ_BLOK = re.compile(r"GÖZ KAPILARI(.{0,2500}?)(?:\n##|\Z)", re.S)
GOZ_MADDE = re.compile(r"^\s*□\s*(.+?)\s*$", re.M)


def goz_kapilari(spec_metin):
    """SPEC F bloğundaki □ maddeleri — her biri TEK KAREYLE kapanır."""
    m = GOZ_BLOK.search(spec_metin or "")
    if not m:
        return []
    return [g.strip() for g in GOZ_MADDE.findall(m.group(1))]


def novum_sinir(spec_metin):
    """NOVUM bloğundaki ⛔ satırları: kuralın nerede bittiğini yazan cümleler."""
    out = []
    m = NOVUM_ETIKET.search(spec_metin or "")
    if not m:
        return out
    satirlar = spec_metin[m.start():].split("\n")[1:30]
    i = 0
    while i < len(satirlar):
        satir = satirlar[i]
        if ETIKET_SATIRI.match(satir):
            break
        g = NOVUM_SINIR_SATIRI.search(satir)
        if g:
            cumle = g.group(1)
            j = i + 1
            while j < len(satirlar):
                dev = satirlar[j]
                if (not dev.strip() or ETIKET_SATIRI.match(dev)
                        or dev.lstrip()[:1] in ("⛔", "⭐", "·")):
                    break
                cumle += " " + dev.strip()
                j += 1
            out.append(re.sub(r"\s+", " ", cumle).strip()[:200])
            i = j
            continue
        i += 1
    return out[:2]


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

# ─── ✂️ KESİK KOŞU [14.09.2026 · QA çıktı reformu FAZ 0] ─────────────────
# Ölçüm: 336 mercek raporunun 56'sında hiç skor hücresi yok — medya yüklenmemiş,
# koşu erken durmuş, çıktı kesilmiş. Bunlar GEÇERSİZ değil KOŞU DEĞİLDİR: parti
# çaprazına (⑤) girmez, tabloya girmez, frekans sayımına girmez, "yeniden
# koşulacak" listesine girer. Ham dosya silinmez/yeniden adlandırılmaz — ayrım
# İÇERİKTEN yapılır; yeni gelen kesik koşu `_KESIK_HAM.md` adıyla kaydedilir.
KESIK_IZI = re.compile(r"MEDIA MISSING|INPUT MODE\s*[:：]\s*MISSING|RUN NOT STARTED|"
                       r"AUDIO ABSENT\s*[—-]\s*RUN|no media (?:was )?(?:readable|attached)|"
                       r"nothing (?:was )?played", re.I)
SKOR_BASLIK = re.compile(r"SCORES?\s+SUMMARY", re.I)   # "SCORE SUMMARY" (tekil) de kabul


# ─── ①.13 HÜKÜM SÖZLÜĞÜ [14.09.2026 · QA çıktı reformu FAZ 1] ────────────
# 13 rubriğin 13'ü kapalı VERDICT listesi tanımlıyordu; 232 raporda 56 farklı hüküm
# metni çıktı — model listeden sapıyor, betik bakmıyordu. Liste rubriklerin KENDİ
# listesidir (rubrik metni değişmedi); tek kaynak burasıdır: ders_frekans ve qa_saglik
# buradan okur. ⑬'ün film düzeyi hükmü yoktur (sahne başına ACCEPT / FIX IN EDIT /
# LOCK FOR NEXT FILM / REGENERATE) → None = kapı koşmaz.
VERDICT_SOZLUK = {
    "① KARE":       ("ACCEPT", "ACCEPT WITH FIX PASS", "REGENERATE"),
    "② DEVAMLILIK": ("HOLDS TOGETHER", "DRIFTS BUT RECOVERABLE", "FIXABLE IN EDIT",
                     "STRUCTURAL PROBLEM", "IDENTITY BREAK"),
    "③ SES":        ("SOUNDTRACK HOLDS", "AUDIBLE DRIFT, FIXABLE IN THE MIX",
                     "WRONG VOICE — REGENERATE", "NO VERDICT — NOTHING MEASURED"),
    "④ HİKAYE":     ("SHOOT AS IS", "SHOOT WITH TRIMS", "REVISE STRUCTURE", "REWRITE PREMISE"),
    "⑤ ARKA PLAN":  ("FIELD HOLDS", "FIELD DRIFTS BUT RECOVERABLE", "FIXABLE IN EDIT",
                     "FIELD COLLAPSES", "SUBJECT DUPLICATE IN FIELD"),
    "⑥ FİZİK":      ("PHYSICS HOLDS", "MINOR SLIPS", "FIXABLE IN EDIT", "INCONSISTENT WORLD",
                     "TWO GRAVITIES"),
    "⑦ AKSİYON":    ("ACTION READS", "MINOR BLUR", "FIXABLE IN EDIT", "BEATS ILLEGIBLE",
                     "ACTION NEVER RENDERED", "N/A — NO ACTION BEATS"),
    "⑧ EFOR":       ("THE BODY PAYS", "MINOR DEBT", "FIXABLE IN EDIT", "WEIGHTLESS WORK",
                     "NOBODY PAYS", "N/A — NO EXERTION EVENTS"),
    "⑨ KADRAJ":     ("CAMERA HELD", "MINOR DRIFT", "SETUP BROKEN", "RHYME BROKEN", "CAMERA WANDERED"),
    "⑩ OYUNCULUK":  ("THE BODY TELLS IT", "MOSTLY LEGIBLE", "TASK WITHOUT FEELING",
                     "THE CHOICE IS INVISIBLE", "MANNEQUIN"),
    "⑪ IŞIK":       ("LIGHT HOLDS", "GRADEABLE DRIFT", "KEY WALKS", "ZONE BROKEN", "LIT FROM NOWHERE"),
    "⑫ HOOK":       ("THE STRANGER STAYS", "LEAVES AT <n> s", "HOOK MISSING", "EXIT FLAT"),
    "⑬ UYUM":       None,
    "⑭ HAREKET":    ("MOTION MAKES SENSE", "MINOR TWITCHES", "FIXABLE IN EDIT", "PUPPET MOTION",
                     "MOTION WITHOUT PURPOSE", "N/A — NO HUMAN MOTION"),
    "⑮ YÖN":        ("EVERY VECTOR LANDS", "MINOR MISAIMS", "FIXABLE IN EDIT", "WRONG WAY",
                     "AIMED AT NOTHING", "N/A — NO DIRECTED ACTS"),
}
VERDICT_SATIR = re.compile(r"^[ \t>*#]*VERDICT\s*[:：]\s*\**\s*([^\n]+?)\s*\**\s*$", re.M | re.I)


def verdict_normal(v):
    v = re.sub(r"[\[\]`]", "", v).strip().rstrip(".").upper()
    v = re.sub(r"[\u2014\u2013-]+", "—", v)                # her tire tek uzun tireye
    v = re.sub(r"\s+", " ", v).replace(" — ", " — ")
    v = re.sub(r"^(?:VERDICT\s*:\s*)", "", v)
    return v


def verdict_oku(metin):
    """Rapordaki VERDICT: satırı → normalize edilmiş hüküm | None (satır yok)."""
    m = VERDICT_SATIR.search(metin)
    return verdict_normal(m.group(1)) if m else None


def verdict_sozlukte(metin, mercek):
    """→ True (sözlükte) · False (sözlük dışı / satır yok) · None (bu mercekte kapı yok)."""
    liste = VERDICT_SOZLUK.get(mercek)
    if not liste:
        return None
    v = verdict_oku(metin)
    if v is None:
        return False
    for k in liste:
        kn = verdict_normal(k)
        if kn.startswith("LEAVES AT"):
            if re.match(r"^LEAVES AT\s*~?\d+(?::\d{2})?([.,]\d+)?\s*S?\b", v):
                return True
        elif v == kn or v.startswith(kn + " ") or v.startswith(kn + " —"):
            return True
    return False


def kesik_mi(metin, rows):
    """Koşu hiç başlamamış / yarıda kesilmiş mi? → (True, sebep) | (False, None)."""
    if KESIK_IZI.search(metin) and not rows:
        return True, KESIK_IZI.search(metin).group(0)
    if not SKOR_BASLIK.search(metin):
        return True, "SCORES SUMMARY başlığı yok"
    if not rows:
        return True, "SCORES SUMMARY var, skor hücresi yok"
    return False, None

# ─── D186 · "KUSUR YOK" HÜCRESİ SAYI TAŞIYAMAZ ─────────────────────
# YERÇEKİMİ F9 (06.09.2026): ⑤ beş hücreye, ⑨ üç hücreye "none" /
# "flawless … mapped to 7" yazıp 7/10 verdi. İki rubrikte de kural ④
# yazılı ("keeps 10/10… absence of evidence is not evidence of
# perfection"). 7 bir ölçüm değil, ortalamaya dönüş refleksidir; ve
# düzeltme TEK YÖNLÜDÜR — yalnız TEMİZ eksen cezalanır.
BOS_ISSUE = re.compile(r"^(?:none|yok|—|–|-|n/?a|\.|\s)*$", re.I)
TEMIZ_ISSUE = re.compile(r"flawless|mapped to \d|stable\b|no distinct|no defects?\b|"
                         r"nothing (?:found|observed)|clean\b|not (?:attempted|observed)|"
                         r"no deductions?\b|no (?:in-scope )?issues?\b|"
                         r"holds? (?:exceptionally|perfectly)|remains? established", re.I)
# bir kesintinin kaynağı: zaman kodu · sahne no · defter satırı
KAYNAK_IZI = re.compile(r"\d{1,2}:\d{2}|\bS\d{1,3}\b|\b[BELF]\d{1,2}\b|\bpattern\b", re.I)

# ─── D185 · FAZ FİLM DEĞİLDİR ──────────────────────────────────────
FAZ_IZI = re.compile(r"\bfaz[\s_]*\d+", re.I)
# bir ORTA SEGMENTTE ölçülemeyen kategoriler: hook filmin başında, final
# sonunda, tutundurma eğrisi filmin tamamınındır.
FAZ_OLCULEMEZ = {
    "④ HİKAYE":  re.compile(r"^(hook|structure|ending|retention)", re.I),
    "⑫ HOOK":    re.compile(r"^(hook question|stakes|plateau|peak placement|exit)", re.I),
    "⑨ KADRAJ":  re.compile(r"^rhyme", re.I),
}
# ─── 13.09.2026 · BÖLÜM FİLM DEĞİLDİR — D185'in yarım-film uzantısı ───
# 36/48 sahnelik hatta (yatay_6_dk_filmler · yatay_8_dk_filmler) QA birimi
# BÖLÜMDÜR: on iki mercek iki yarım mastera ayrı koşulur. Faz gibi bir ORTA
# segment değil, bir UÇ segmenttir — baş bölüm hook'u görür ama finali
# göremez, son bölüm tersi; bütün filmi isteyen dörtlü hiçbirinde sayı taşımaz.
#   --bolum n/m  →  n == 1: BAŞ · n == m: SON · 1 < n < m: ORTA (= FAZ maskesi)
BOLUM_ARG = re.compile(r"^(\d+)\s*/\s*(\d+)$")
BOLUM_BAS_GOREMEZ = {    # BAŞ bölümün göremediği: filmin SONU + bütün-film dörtlüsü
    "④ HİKAYE":  re.compile(r"^(structure|retention|ending)", re.I),
    "⑫ HOOK":    re.compile(r"^(plateau|peak placement|exit)", re.I),
    "⑨ KADRAJ":  re.compile(r"^rhyme", re.I),
}
BOLUM_SON_GOREMEZ = {    # SON bölümün göremediği: filmin BAŞI + bütün-film dörtlüsü
    "④ HİKAYE":  re.compile(r"^(structure|retention|hook)", re.I),
    "⑫ HOOK":    re.compile(r"^(plateau|hook question|stakes)", re.I),
    "⑨ KADRAJ":  re.compile(r"^rhyme", re.I),
}
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
    """seviye: KESİK · GEÇERSİZ · TEKRAR · ŞARTLI · NOT"""
    def __init__(self, seviye, baslik, ayrinti=""):
        self.seviye, self.baslik, self.ayrinti = seviye, baslik, ayrinti

    def __str__(self):
        isaret = {"KESİK": "✂️", "GEÇERSİZ": "🚨", "TEKRAR": "⛔", "ŞARTLI": "⚠️ ", "NOT": "·"}[self.seviye]
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
            # 14.09.2026: '---' künyeyi değil raporun kendi başlık bloğunu kapatıyorsa
            # (öncesinde INPUT MODE / VERDICT / FORMAT satırı var) HİÇBİR ŞEY atlanmaz —
            # aksi hâlde mod "?" ve "hüküm yok" sahte bulguları doğuyordu (33 TEKRAR).
            bas = "\n".join(satirlar[:i])
            if re.search(r"^[ \t>*#]*(INPUT MODE|VERDICT|FORMAT)\s*[:：]", bas, re.M | re.I):
                return metin
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
    """BEAT STRING (⑦) / COST CURVE (⑧) — sahne başına bir hane.
    ⛔ BOŞLUK TOLERE EDİLİR [D194 · kardeş tarama]: ⑨⑩⑪ diziyi boşluklu
    yazdığı için okunamamıştı; ⑦ ve ⑧ aynı arızayı üretebilir (rubrikleri
    'no spaces' cümlesini D194'e kadar taşımıyordu). Boşluk sınıfın BAŞINA."""
    d = re.search(rf"{baslik}[^\n]*\n(?:[^\n]*\n)??[ \t]*`?([ \t{alfabe}]{{3,}}?)`?[ \t]*$",
                  metin, re.M) or \
        re.search(rf"{baslik}[:\s`]*([ \t{alfabe}]{{3,}}?)`?[ \t]*$", metin, re.M)
    if not d:
        return None
    g = re.sub(r"[ \t]+", "", d.group(1))
    return g if len(g) >= 3 else None


def gozlem_dizi(metin, baslik, alfabe):
    """⑨/⑩/⑪ dizileri — başlığın altındaki `OBSERVED:` satırından, [D184].
    dizi_al burada KULLANILMAZ: `OBSERVED` sözcüğünün kendisi [A-Z]{3,} ile eşleşir.
    ⛔ BOŞLUK TOLERE EDİLİR [D194]: rubrikler diziyi `A B ? ? D E` diye boşluklu
    yazıyordu; alfabe sınıfı boşluğu içermediği için ÜÇ merceğin ÜÇÜ de
    okunamadı ve betik suçu rapora yazdı ("dizisiz rapor"). Satır önce
    alınır, boşluklar SONRA silinir — sıra ters olursa kapı yine körleşir."""
    # ⛔ boşluk sınıfın BAŞINA yazılır: sonuna eklenirse `OADU-` gibi tire ile
    #    biten alfabede "U- " geçersiz aralık olur ve betik ÇÖKER [D194].
    m = re.search(rf"{baslik}(?:[^\n]*\n){{0,4}}[ \t`]*OBSERVED\s*[:：][ \t]*`?([ \t{alfabe}]{{3,}}?)`?[ \t]*$",
                  metin, re.M)
    if not m:
        return None
    g = re.sub(r"[ \t]+", "", m.group(1))
    return g if len(g) >= 3 else None


def plan_iskelet(spec_metin):
    m = ISKELET_ETIKET.search(spec_metin or "")
    return re.sub(r"\s+", "", m.group(1)) if m else None


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
    bas = next((i for i, s in enumerate(satirlar) if SKOR_BASLIK.search(s)), None)
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
def faz_mi(film_dir, metin):
    """Girdi bir FAZ mı (uzun filmin orta segmenti) — klasörden ya da rapordan [D185]."""
    if film_dir is not None:
        if FAZ_IZI.search(film_dir.name):
            return f"film klasörü {film_dir.name}"
        if any(d.is_dir() and FAZ_IZI.search(d.name) for d in film_dir.iterdir()):
            return f"{film_dir.name} FAZ mimarisiyle yazılmış (FAZ_*/ alt klasörleri)"
    ad = alan(metin, "FILM") or ""
    if FAZ_IZI.search(ad):
        return f"raporun FILM satırı: \"{ad[:40]}\""
    return None


def rapor_denetle(yol, spec_metin=None, hook=10.0, klip=10.0, faz=None, bolum=None):
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
    R["purpose_dizi"] = dizi_al(metin, "PURPOSE STRING", "Pmx-")     # ⑭
    R["vector_dizi"] = dizi_al(metin, "VECTOR STRING", "Hmx-")       # ⑮
    R["bedel_dizi"] = dizi_al(metin, "COST CURVE", "0-9")
    R["plan_dizi"] = None
    if R["mercek"] in DIZI_MERCEKLER:
        b, a = DIZI_MERCEKLER[R["mercek"]]
        R["plan_dizi"] = gozlem_dizi(metin, b, a)
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

    # ①.11 ÜRETİM SADAKATİ KAPISI [⑬ UYUM · 11.09.2026]
    # ⑬'ün girdisi SPEC değil, modele GÖNDERİLEN PROMPT METNİDİR. Bu yüzden
    # kapı SPEC'in varlığından BAĞIMSIZ koşar: promptsuz koşu "eksik" değil,
    # KOŞU DEĞİLDİR — ekrandan prompt uyduran mercek ekrana her zaman uyar.
    if R["mercek"] in URETIM_SADAKATI_MERCEKLER and R["mod"] != "D":
        B.append(Bulgu("GEÇERSİZ",
                       f"⑬ UYUM mod {R['mod'] or '?'} koşulmuş → KOŞU DEĞİL [11.09.2026]",
                       "Bu merceğin mod V'si yoktur: sahne↔prompt karşılaştırmasının bir tarafı "
                       "eksikse karşılaştırma da yoktur. T13'e satır girmez, ders siparişi üretmez. "
                       "Koşu dört girdiyle tekrarlanır: kurgu · sahne promptları (birebir) · QA_SPEC · "
                       "sahne_kapisi.sh çıktısı + üretim defteri satırları."))

    # ①.12 ALINTI KAPISI [⑬ UYUM] — alıntısız bulgu DÜŞER
    # ⑬'ün tek ayırt edici aracı alıntıdır: 🅐 iddiası promptun cümlesini,
    # 🅑 iddiası "promptta bunun yerine ne yazıyor"u taşımak zorundadır.
    # Alıntısız satır bir gözlem olabilir ama ATIF değildir ve ders üretemez.
    if R["mercek"] in URETIM_SADAKATI_MERCEKLER:
        m_led = re.search(r"CONFORMANCE LEDGER(.*?)(?=\n#|\Z)", metin, re.S)
        if m_led:
            satirlar = [l for l in m_led.group(1).split("\n")
                        if l.strip().startswith("|") and "---" not in l]
            veri = [l for l in satirlar[1:] if l.count("|") >= 5]
            # 🅑'nin meşru cevabı alıntı DEĞİLDİR: "promptta karşılığı yok" da bir
            # beyandır ve rubrik onu açıkça istiyor. Kapı ikisini de kabul eder,
            # HİÇBİRİNİ taşımayan satırı düşürür.
            BEYAN = re.compile(r"no corresponding line|instead|karşılığı yok|yerine", re.I)
            alintisiz = [l for l in veri
                         if not re.search(r"[\"'\u201c\u201d\u2018\u2019`]\s*\S", l)
                         and not BEYAN.search(l)]
            if veri and alintisiz:
                B.append(Bulgu("ŞARTLI",
                               f"CONFORMANCE LEDGER: {len(alintisiz)}/{len(veri)} satır ALINTISIZ",
                               "Alıntısız satır ATIF taşıyamaz: 🅐 promptun cümlesini, 🅑 promptun "
                               "bunun yerine ne dediğini yazmak zorundadır. Bu satırlar düşer; "
                               "ders siparişine de girmez."))
            if veri and len(alintisiz) == len(veri):
                B.append(Bulgu("GEÇERSİZ", "⑬ raporunda HİÇBİR bulgu alıntı taşımıyor",
                               "Bu, promptla değil ekranla konuşan bir rapordur. T13'e satır girmez."))

    # ①.13 DERS SİPARİŞİ KAPISI [⑬ UYUM] — kilit cümlesi FİLME ÖZEL olamaz
    # Bu merceğin ürünü sonraki filmin kilididir; "S07'deki gibi" diye yazılan
    # bir kilit, o filmi görmemiş birine hiçbir şey söylemez ve derse dönüşemez.
    if R["mercek"] in URETIM_SADAKATI_MERCEKLER:
        m_ders = re.search(r"LESSON ORDERS(.*?)(?=\n#|\Z)", metin, re.S)
        if m_ders:
            d_satir = [l for l in m_ders.group(1).split("\n")
                       if l.strip().startswith("|") and "---" not in l and l.count("|") >= 4]
            ozel = [l for l in d_satir[1:] if re.search(r"\bS\d{1,2}\b", l)]
            if ozel:
                B.append(Bulgu("ŞARTLI",
                               f"DERS SİPARİŞİ: {len(ozel)} satır SAHNE NUMARASI taşıyor",
                               "Kilit cümlesi sonraki filmin yazarına gider; o kişi bu filmi görmedi. "
                               "Sahne numarası, film adı ve 'S07'deki gibi' ifadesi kilit satırından "
                               "çıkarılır — kanıt sütununda kalabilir."))

    # ① SPEC KAPISI
    if spec_metin is not None and R["mercek"] in MOD_D_MERCEKLER and R["mod"] != "D":
        if R["mercek"] in PLAN_SADAKATI_MERCEKLER:
            # ⑨-⑫ MOD V'DE BOŞ DEĞİL, TERSİNE ÇALIŞIR [D190]: bu dörtlü planı
            # ekrana karşı okumak için vardır; belge yokken ekrandan bir plan
            # UYDURUR ve uydurduğu plan filme her zaman uyar. THE OPEN CIRCUIT'te
            # ⑫ makarada olmayan bir doruğa "Peak Placement 9/10" verdi.
            B.append(Bulgu("GEÇERSİZ",
                           f"⑨-⑫ PLAN SADAKATİ MERCEĞİ mod {R['mod'] or '?'} koşulmuş → koşu GEÇERSİZ [D190 · D184]",
                           "Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp "
                           "puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, "
                           "hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır."))
        else:
            B.append(Bulgu("TEKRAR", f"SPEC dosyası VAR, rapor mod {R['mod'] or '?'} → koşu TEKRARLANIR [D129]",
                           "ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / "
                           "yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta."))
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

        # ①.7 NOVUM SINIR KAPISI [D183] — kural NEREDE BİTİYOR?
        for sinir in novum_sinir(spec_metin):
            B.append(Bulgu("NOT", "⑩ SINIR SORUSU — novum nerede BİTİYOR? [D183]",
                           f"SPEC: \"{sinir}\" · ⑩ bu cümle KAREYLE sınanmadan KAPANMAZ: "
                           "düşen novum bulgusunun ALTINDA bir sınır ihlali olabilir"))

    # ①.5 ARİTMETİK — raporun kendi tablosundan
    rows = skor_tablosu(metin)
    # ①.8 FAZ KAPISI [D185] — orta segmentte film ölçekli kategori ölçülemez
    faz_rx = None
    if faz:
        rx = FAZ_OLCULEMEZ.get(R["mercek"])
        faz_rx = rx
        if rx:
            vuran = [r["ad"] for r in rows if r["tip"] == "sayi" and rx.match(r["ad"])]
            if vuran:
                B.append(Bulgu("ŞARTLI",
                               f"FAZ KAPISI — {len(vuran)} kategori bir ORTA SEGMENTTE ölçülemez [D185]",
                               f"{faz} · sayı taşıyamaz: {' · '.join(vuran)}. Hook filmin BAŞINDA, final "
                               "SONUNDA, tutundurma eğrisi filmin TAMAMINDADIR. Bu hücreler `—` olur, "
                               "ortalama yeniden hesaplanır; kesme listesi ve yeniden sıralama UYGULANMAZ."))
        else:
            B.append(Bulgu("NOT", f"FAZ girdisi [D185] — {faz}",
                           "bu merceğin kategorileri faz ölçeğinde geçerli; ④ ⑨ ⑫ ise değildir"))
        B.append(Bulgu("NOT", "⛔ FAZ'ın kendi rubriği var mı? [D185]",
                       "10-20 dk hattında QA birimi FAZDIR: `<FAZ>/FAZ_nn_QA_PROMPT.md`. "
                       "Varsa genel mercek yerine O koşulur; yoksa önce O yazılır."))
    # ①.11 BÖLÜM KAPISI [13.09.2026 · KILAVUZ_REHBERI §2.6/§2.7] — yarım masterda
    # uç kategoriler ölçülemez. Faz kapısıyla aynı mekanizma, farklı maske:
    # bölümün KONUMU hangi ucun dosyada olmadığını söyler.
    bolum_rx = None
    if bolum:
        b_n, b_m = bolum
        if b_n == 1 and b_m > 1:
            sozluk, konum = BOLUM_BAS_GOREMEZ, "BAŞ bölüm — filmin SONU bu dosyada değil"
        elif b_n == b_m:
            sozluk, konum = BOLUM_SON_GOREMEZ, "SON bölüm — filmin BAŞI bu dosyada değil"
        else:
            sozluk, konum = FAZ_OLCULEMEZ, "ORTA bölüm — ne baş ne son bu dosyada"
        bolum_rx = sozluk.get(R["mercek"])
        if bolum_rx:
            vuran = [r["ad"] for r in rows if r["tip"] == "sayi" and bolum_rx.match(r["ad"])]
            if vuran:
                B.append(Bulgu("ŞARTLI",
                               f"BÖLÜM KAPISI — {len(vuran)} kategori BÖLÜM {b_n}/{b_m}'de ölçülemez [§2.6]",
                               f"{konum} · sayı taşıyamaz: {' · '.join(vuran)}. Bu hücreler `—` olur, "
                               "ortalama yeniden hesaplanır; kesme listesi ve yeniden sıralama UYGULANMAZ "
                               "(kesme filmin kurgusudur, bölüm raporunun yetkisi değil)."))
            else:
                B.append(Bulgu("NOT", f"BÖLÜM {b_n}/{b_m} girdisi — {konum}",
                               "uç kategoriler zaten sayı taşımıyor; maske uygulanacak hücre yok"))
        else:
            B.append(Bulgu("NOT", f"BÖLÜM {b_n}/{b_m} girdisi — {konum}",
                           "bu merceğin kategorileri bölüm ölçeğinde geçerli; ④ ⑨ ⑫'nin uç kategorileri değildir"))
        if R["mercek"] == "② DEVAMLILIK":
            B.append(Bulgu("NOT", "⛔ BÖLÜM SINIRI KÖR NOKTASI [§2.6]",
                           "② sınır çiftini (son sahne ↔ sonraki bölümün ilk sahnesi) hiçbir yarım masterda "
                           "yan yana GÖREMEZ. Çift SPEC B'nin sınır satırından ELLE KAREYLE kapanır "
                           "(①.10 göz kapısı kalıbı); kapanmadan parti kapanmaz."))
    R["rows"] = rows
    kesik, sebep = kesik_mi(metin, rows)
    if kesik:
        B.append(Bulgu("KESİK", f"KESİK KOŞU — {sebep}",
                       "Koşu değil: medya yüklenmemiş / çıktı yarıda kesilmiş. Tabloya girmez, partiyi "
                       "düşürmez, frekansa girmez; aynı mercek YENİDEN koşulur. Yeni gelen kesik çıktı "
                       "`<FILM>_<MERCEK>_KESIK_HAM.md` adıyla kaydedilir [14.09.2026]."))
        R["karar"] = "KESİK"
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
        if faz_rx is not None and faz_rx.match(r["ad"]):
            # [D185] kapı ARTIK BAĞLIYOR: 07.09.2026'ya kadar hücreyi yalnız
            # adlandırıyordu, ortalama değişmiyordu — yazılı ama bağlamayan kapı.
            r["tip"], r["not"] = "dash", "faz ölçeği→—"
            duzeltme.append(f"{r['ad']} {r['deger']:g}/10 → — "
                            f"(faz ölçeğinde ölçülemez: hook/final/tutundurma) [D185]")
        elif bolum_rx is not None and bolum_rx.match(r["ad"]):
            # [§2.6 · 13.09.2026] aynı bağlayıcılık, bölüm maskesiyle
            r["tip"], r["not"] = "dash", "bölüm ölçeği→—"
            duzeltme.append(f"{r['ad']} {r['deger']:g}/10 → — "
                            f"(bölüm {bolum[0]}/{bolum[1]}: bu uç dosyada yok) [§2.6]")
        elif KAYNAKSIZ.search(r["issue"]):
            r["tip"], r["not"] = "dash", "kaynaksız→—"
            duzeltme.append(f"{r['ad']} {r['deger']:g}/10 → — (issue: \"no in-scope source\") [D131]")
        elif BOS_ISSUE.match(r["issue"] or "") or TEMIZ_ISSUE.search(r["issue"]):
            # D186: "kusur bulamadım" ya 10/10'dur ya `—`. Asla 7.
            r["tip"], r["not"] = "dash", "kusursuz→—"
            duzeltme.append(f"{r['ad']} {r['deger']:g}/10 → — "
                            f"(issue: \"{(r['issue'] or 'boş')[:28]}\" — kusur yok, sayı taşıyamaz) [D186]")
        elif r["deger"] < 10 and not KAYNAK_IZI.search(r["issue"]):
            B.append(Bulgu("ŞARTLI", f"{r['ad']} {r['deger']:g}/10 — kesintinin KAYNAĞI yazılı değil [D186]",
                           f"issue: \"{r['issue'][:60]}\" · kural ④: kaynağı listelenmeyen kesinti "
                           "UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz."))
        elif R["replik"] == 0 and DIYALOG_YALNIZ.match(r["ad"]):
            r["tip"], r["not"] = "na", "0 replik→N/A"
            duzeltme.append(f"{r['ad']} {r['deger']:g}/10 → N/A (0 replik — sessizlik tasarımdır)")
        elif R["replik"] == 0 and DIYALOG_VE_SES.match(r["ad"]):
            B.append(Bulgu("NOT", f"{r['ad']} {r['deger']:g}/10 · film 0 replikli — hücrenin kaynağı SES FİZİĞİ "
                                  "(vakumda ses / senkron) olmalı; replik kaynaklıysa N/A'ya çevir (insan kararı)"))
    if duzeltme:
        B.append(Bulgu("ŞARTLI", f"{len(duzeltme)} hücre düzeltildi", " · ".join(duzeltme)))

    # ④ KURGU — ④ HİKAYE haritası kesme sayısıyla çelişiyor mu (ÇOK KLİPLİ SAHNE filminde sahne ≠ klip [COK_KLIPLI_SAHNE §0])
    cok_klipli = bool(spec_metin and re.search(r"SAHNE PLANI:", spec_metin))
    if not cok_klipli and R["mercek"] == "④ HİKAYE" and R["kesme"] and R["sahne"] and R["sahne"] < R["kesme"] - 1:
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

    # ①.13 HÜKÜM [14.09.2026 · FAZ 1] — VERDICT satırı var mı, rubriğin kapalı listesinde mi
    R["verdict"] = verdict_oku(metin)
    R["verdict_sozlukte"] = verdict_sozlukte(metin, R["mercek"])
    if R["verdict_sozlukte"] is False:
        if R["verdict"] is None:
            B.append(Bulgu("ŞARTLI", "①.13 HÜKÜM yok — `VERDICT:` satırı bulunamadı",
                           "Rubrik kapalı liste verir; hükümsüz rapor frekans sayımına girmez, tabloya ŞARTLI girer"))
        else:
            B.append(Bulgu("ŞARTLI", f"①.13 HÜKÜM sözlük dışı: \"{R['verdict'][:60]}\"",
                           f"{R['mercek']} listesi: " + " / ".join(VERDICT_SOZLUK[R["mercek"]]) +
                           " — ders_frekans yalnız listedeki hükmü sayar"))

    # ①.5 TALLY
    if R["tally"]:
        y = R["yazili"]
        yz = (y["🔴"], y["🟠"], y["🟡"])
        if yz != R["tally"]:
            B.append(Bulgu("ŞARTLI", f"SEVERITY TALLY {R['tally']} ≠ yazılı etiketler {yz} (🔴,🟠,🟡)",
                           "verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]"))
    # tally satırı yoksa: 14.09.2026 sözleşmesi — model saymaz, betik sayar; NOT bile yok

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

    # ⑭ PURPOSE STRING · ⑮ VECTOR STRING — uzunluk = kesme + 1 (14.09.2026)
    for ad, dizi in (("PURPOSE STRING", R["purpose_dizi"]), ("VECTOR STRING", R["vector_dizi"])):
        if dizi and R["kesme"]:
            bek = R["kesme"] + 1
            if len(dizi) not in (bek, bek - 1, bek - 2):
                B.append(Bulgu("ŞARTLI", f"{ad} {len(dizi)} hane, kesme+1 = {bek}",
                               "dizi sahne başına bir hanedir; tutmuyorsa defter ya da kesme sayımı yanlış"))
    if R["mercek"] == "⑭ HAREKET":
        m_top = ilk_sayi(alan(metin, "MOVEMENTS LOGGED"))
        m_x = ilk_sayi(alan(metin, "PURPOSELESS MOVEMENTS"))
        if m_top is not None and m_x is not None and m_x > m_top:
            B.append(Bulgu("ŞARTLI", f"PURPOSELESS MOVEMENTS {m_x} > MOVEMENTS LOGGED {m_top}", "ikisinden biri yanlış"))
    if R["mercek"] == "⑮ YÖN":
        a_top = ilk_sayi(alan(metin, "ACTS LOGGED"))
        m_am = re.search(r"ACTS MISSED[:\s]*(\d+)\D+(\d+)\D+(\d+)\D+(\d+)\D+(\d+)", metin)
        if a_top and m_am:
            parca = sum(int(g) for g in m_am.groups())
            if parca != a_top:
                B.append(Bulgu("ŞARTLI", f"ACTS MISSED toplamı {parca} ≠ ACTS LOGGED {a_top}",
                               "HIT + MISS + UNKNOWN + NO TARGET + FLIP, defterdeki satır sayısını vermeli"))

    # ⑨⑩⑪ PLAN DİZİLERİ — uzunluk = kesme + 1 · ⑨'da plan iskeletiyle kıyas [D184]
    if R["mercek"] in DIZI_MERCEKLER:
        b, _ = DIZI_MERCEKLER[R["mercek"]]
        if not R["plan_dizi"]:
            B.append(Bulgu("ŞARTLI", f"{b} YOK ya da `OBSERVED:` satırı okunamadı",
                           "bu merceğin makine çıktısı dizidir; dizisiz rapor sahne sahne sınanamaz"))
        elif R["kesme"]:
            bek = R["kesme"] + 1
            if len(R["plan_dizi"]) not in (bek, bek - 1, bek - 2):
                B.append(Bulgu("ŞARTLI", f"{b} {len(R['plan_dizi'])} hane, kesme+1 = {bek}",
                               "dizi sahne başına bir hanedir; tutmuyorsa defter ya da kesme sayımı yanlış"))
        if R["mercek"] == "⑨ KADRAJ" and R["plan_dizi"] and spec_metin:
            plan = plan_iskelet(spec_metin)
            if plan:
                g = R["plan_dizi"]
                if len(g) == len(plan):
                    fark = [f"S{i}" for i, (x, y) in enumerate(zip(g, plan)) if x != y]
                    if not fark:
                        B.append(Bulgu("NOT", "SETUP STRING plan iskeletiyle BİREBİR aynı",
                                       "kare-önce kuralı ledger'dan doğrulanır: her satırda gözlenen boyut/açı "
                                       "yazılı mı? Yalnız harf yazan ledger planı kopyalamıştır"))
                    else:
                        B.append(Bulgu("NOT", f"SETUP STRING plandan {len(fark)} yerde sapıyor: {' '.join(fark)}",
                                       f"gözlenen {g} · plan {plan} → bu sapmalar ⑨'un bulgusudur, rapor kusuru değil; "
                                       "her biri kareyle kapanır (⑪ tek kare)"))
                else:
                    B.append(Bulgu("ŞARTLI", f"SETUP STRING {len(g)} hane, plan iskeleti {len(plan)} hane",
                                   "iki dizi aynı sahne sayısını saymalı; uzunluk tutmadan sapma okunamaz"))

    # ⑫ DROP-OFF PREDICTION — üç saniye, sabit listeden sebep [D184]
    if R["mercek"] == "⑫ HOOK":
        blok = re.search(r"DROP-OFF PREDICTION(.*?)(?=\n#{1,3}\s|\Z)", metin, re.S)
        if not blok:
            B.append(Bulgu("ŞARTLI", "DROP-OFF PREDICTION YOK",
                           "bu merceğin tek kalıcı çıktısı üç saniyelik tahmindir; tahminsiz rapor yayın tablosuna giremez"))
        else:
            g = blok.group(1)
            sn = re.findall(r"\d{1,2}:\d{2}|\b\d{1,3}(?:[.,]\d)?\s*s\b", g)
            sebep = DUSUS_SEBEP.findall(g)
            if len(sn) < 3:
                B.append(Bulgu("ŞARTLI", f"DROP-OFF PREDICTION {len(sn)} saniye yazmış, 3 ister",
                               "aralık/hedge kıyaslanamaz; üç saniye, üç sebep"))
            if len(sebep) < 3:
                B.append(Bulgu("ŞARTLI", f"DROP-OFF PREDICTION sebep {len(sebep)}/3 sabit listeden",
                               "sebep listesi: slow open · no stakes yet · plateau · repeated setup · unreadable beat · card"))

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
# 22.09.2026 · çok klipli sahne rejimi: birim başlığı `## 🎬 KLİP n` (makara klip
# sayar, plan da klip sayar). Üst birim `# 📍 SAHNE n — … (k klip)` SAYILMAZ.
SAHNE_BASLIK = re.compile(r"^#{1,4}\s(?![^\n]*📍).*\b(?:SAHNE|KL[İI]P)\s+(\d{1,3})\b", re.M)
# QA / ders / rapor dosyaları sahne SAYMAZ — onlar sahneden BAHSEDER
PLAN_DISI = re.compile(r"QA_|DERSLER|RAPOR|_QA|README|INDEX", re.I)


def bolum_dosyalari(film_dir, bolum):
    """[19.09.2026 · §2.8] QA parçası ↔ bölüm dosyası eşlemesi.

    6/8 dk hattında parça sayısı = bölüm dosyası sayısı (2 = 2), parça n =
    BOLUM_n. 16 dk hattında dosya 8, QA parçası 4: PART n = BOLUM_(2n−1) +
    BOLUM_(2n). Genel kural: k dosya / m parça tam bölünüyorsa parça n,
    dosyalar (n−1)·k/m+1 … n·k/m'dir. Bölünmüyorsa (MARS_SON_CIKIS 3 × 12 ↔
    2 yarım vakası) eski davranış + uyarı: yalnız BOLUM_n sayılır ve ①.9
    yanlış ateşleyebilir — yapı uyuşmazlığı PLAN'a yazılır."""
    n, m = bolum
    tumu = sorted(Path(str(film_dir)).glob("*_BOLUM_*.md"),
                  key=lambda f: int(re.search(r"_BOLUM_(\d+)\.md$", f.name).group(1))
                  if re.search(r"_BOLUM_(\d+)\.md$", f.name) else 0)
    tumu = [f for f in tumu if re.search(r"_BOLUM_(\d+)\.md$", f.name)]
    k = len(tumu)
    if k and k % m == 0:
        per = k // m
        secim = tumu[(n - 1) * per: n * per]
        if per > 1:
            print(f"BÖLÜM DOSYASI: {k} dosya / {m} parça → PART {n} = "
                  + " + ".join(f.name for f in secim) + "  [§2.8 · 19.09.2026]")
        return secim
    if k:
        print(f"⚠️  YAPI UYUŞMAZLIĞI: {k} bölüm dosyası, {m} QA parçası — tam bölünmüyor; "
              f"①.9 yalnız *_BOLUM_{n}.md'yi sayar ve YANLIŞ ATEŞLEYEBİLİR (MARS_SON_CIKIS 3×12↔2 vakası)")
    return sorted(Path(str(film_dir)).glob(f"*_BOLUM_{n}.md"))


class SahnePlaniSayisi(int):
    """ÇOK KLİPLİ SAHNE filminde sahne sayısı (dramatik) ve klip sayısı (fiziksel).
    Merceklerin bir kısmı dramatik sahne (S01-S06 = 6), bir kısmı klip (K01-K24 = 24)
    sayabilir; her iki sayım da meşrudur ve teslimi doğrular [D188 · COK_KLIPLI_SAHNE §0]."""
    def __new__(cls, sahne_sayisi, klip_sayisi, plan_str=""):
        obj = super().__new__(cls, sahne_sayisi)
        obj.sahne_sayisi = sahne_sayisi
        obj.klip_sayisi = klip_sayisi
        obj.plan_str = plan_str
        return obj

    def __eq__(self, other):
        return other == self.sahne_sayisi or other == self.klip_sayisi

    def __repr__(self):
        return f"{self.sahne_sayisi} sahne ({self.klip_sayisi} klip · SAHNE PLANI: {self.plan_str})"

    def __str__(self):
        return f"{self.sahne_sayisi} sahne ({self.klip_sayisi} klip)"

    def __sub__(self, other):
        if isinstance(other, int):
            if abs(other - self.sahne_sayisi) <= abs(other - self.klip_sayisi):
                return self.sahne_sayisi - other
            return self.klip_sayisi - other
        return super().__sub__(other)

    def __rsub__(self, other):
        return -(self.__sub__(other))


def plan_sahne_sayisi(film_dir, bolum=None):
    """[D188] Planın kendi sahne başlıklarını sayar: `## 🎬 SAHNE 109 — ...`

    Raporlar birbirini doğrular ama HEPSİ aynı makarayı izler; eksik teslim
    oybirliğiyle onaylanabilir. Planın sahne sayısı, parti dışındaki TEK
    referanstır.

    22.09.2026 · ÇOK KLİPLİ SAHNE [COK_KLIPLI_SAHNE_KILAVUZU §0]:
    PLAN veya QA_SPEC'te `SAHNE PLANI: 3 4 5 3 5 4` varsa sahne sayısı (dramatik)
    ve klip sayısı (üretim) ayrıdır. SahnePlaniSayisi ikisini birden taşır;
    mercekler sahne ya da klip saydığında teslim kapısı doğru doğrular.

    bolum=(n, m) [13.09.2026 · §2.6]: QA birimi BÖLÜM olan filmde makara yarım
    masterdır; plan tarafı da YALNIZ o parçanın bölüm dosya(lar)ı olur. Bütün
    dosyalar sayılsaydı kapı her yarımda YANLIŞ ateşlerdi (plan 36, makara 18).
    19.09.2026 · §2.8: parça ≠ dosya olabilir (16 dk: 8 dosya / 4 parça) →
    bolum_dosyalari() eşler."""
    if not film_dir or not Path(str(film_dir)).is_dir():
        return None, None

    # Önce SAHNE PLANI satırını ara (ÇOK KLİPLİ SAHNE)
    for f in sorted(Path(str(film_dir)).glob("*.md")):
        if PLAN_DISI.search(f.name) and not f.name.endswith(("_QA_SPEC.md", "_PLAN.md")):
            continue
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
            m = re.search(r"SAHNE PLANI:\s*([\d\s]+)", txt)
            if m:
                sayilar = [int(x) for x in re.findall(r"\d+", m.group(1))]
                if sayilar:
                    if bolum:
                        n, m_bol = bolum
                        k = len(sayilar)
                        if k and k % m_bol == 0:
                            per = k // m_bol
                            secim = sayilar[(n - 1) * per: n * per]
                            return SahnePlaniSayisi(len(secim), sum(secim), " ".join(map(str, secim))), f.name
                        elif sum(sayilar) % m_bol == 0:
                            # 16 dk hat (§2.8): sahneler eşit bölünmeyebilir (6+6+6+7=25) ama klipler tam bölünür (24+24+24+24=96)
                            hedef_klip = sum(sayilar) // m_bol
                            parcalar = []
                            cur_k, cur_s = 0, []
                            for s in sayilar:
                                cur_s.append(s)
                                cur_k += s
                                if cur_k == hedef_klip:
                                    parcalar.append(cur_s)
                                    cur_s, cur_k = [], 0
                            if len(parcalar) == m_bol:
                                secim = parcalar[n - 1]
                                return SahnePlaniSayisi(len(secim), sum(secim), " ".join(map(str, secim))), f.name
                    return SahnePlaniSayisi(len(sayilar), sum(sayilar), " ".join(map(str, sayilar))), f.name
        except OSError:
            continue

    # Standart sahne başlığı sayımı
    tum, kaynaklar = set(), []
    if bolum:
        dosyalar = bolum_dosyalari(film_dir, bolum)
    else:
        dosyalar = sorted(Path(str(film_dir)).glob("*.md"))
    for f in dosyalar:
        if PLAN_DISI.search(f.name):
            continue
        no = {int(m) for m in SAHNE_BASLIK.findall(
            f.read_text(encoding="utf-8", errors="replace"))}
        if no:
            tum |= no
            kaynaklar.append(f.name)
    return (len(tum) or None), (" + ".join(kaynaklar) or None)


def capraz(sonuclar, olcum=None, plan_sahne=None, plan_kaynak=None):
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

    # ⑤ SÜRE SATIRI [D205 · 13.09.2026] — ⑩ 60 s · ⑫ 25 s · on mercek 124 s yazdı,
    # kapı ✅ verdi: kesme · sahne · şerit · replik karşılaştırılıyordu, SÜRE hiç.
    # Süre bir DOSYA özelliğidir; aynı makaraya bakan iki mercek %10'dan fazla
    # ayrışamaz. Ölçüm (--olcum-sure) hakemdir; yoksa ORTANCA referanstır.
    o_sur = olcum.get("sure")
    sur = [(r["mercek"], float(r["sure"])) for r in sonuclar if r["sure"]]
    if sur and (len(sur) >= 2 or o_sur):
        vals = sorted(v for _, v in sur)
        ref = float(o_sur) if o_sur else vals[len(vals) // 2]
        ref_ad = "ÖLÇÜM" if o_sur else f"ortanca ({len(sur)} mercek)"
        tol = max(5.0, 0.10 * ref)
        sapan = [(m, v) for m, v in sur if abs(v - ref) > tol]
        satir = " · ".join(f"{m} {v:g}" for m, v in sur)
        if sapan:
            for r in sonuclar:
                if r["sure"] and abs(float(r["sure"]) - ref) > tol:
                    r["bulgular"].append(Bulgu(
                        "ŞARTLI",
                        f"süre {float(r['sure']):g} s ≠ {ref_ad} {ref:g} s (tolerans ±{tol:g}) → ZAMAN EKSENİ uydurma sayılır [D205]",
                        "zaman kodları, DROP-OFF saniyeleri ve sahne aralıkları bu rapordan ALINMAZ; "
                        "mercek temiz oturumda yeniden koşulur [D112 · D125]"))
                    if r["karar"] == "GO":
                        r["karar"] = "ŞARTLI"
            B.append(Bulgu("ŞARTLI",
                           f"⑤ SÜRE — {ref_ad} {ref:g} s; sapan: " +
                           " · ".join(f"{m} {v:g}" for m, v in sapan) + " [D205]",
                           satir + "\n        süre bir DOSYA özelliğidir; aynı makaraya bakan iki merceğin süresi "
                                   "%10'dan fazla ayrışamaz — sapan merceğin zaman ekseni 🚨, parti düşmez"))
        else:
            B.append(Bulgu("NOT", f"⑤ süre ekseni doğrulandı — {len(sur)} mercek, {ref_ad} {ref:g} s (±{tol:g})"))

    # ⑦ ORTAK DEFTER KAPISI [D110] — künyesi birebir aynı iki rapor tek ölçümdür
    kunye, kodsuz = {}, set()
    for r in sonuclar:
        if not r.get("kesme_tc"):
            kodsuz.add(r["mercek"])
        # SÜRE anahtara GİRMEZ: 109/110/111 aynı ölçümün yuvarlamasıdır.
        # Ayırt edici olan SAYIMLARDIR — onları devralmak kopyanın imzasıdır.
        k = (r.get("kesme"), r.get("sahne"), r.get("serit"))
        if any(x is None for x in k):
            continue
        kunye.setdefault(k, []).append(r["mercek"])
    for k, ms in kunye.items():
        if len(ms) < 2:
            continue
        # çoğunluğun künyesi zaten aynıdır; KOPYA şüphesi AZINLIK için geçerli
        if len(ms) * 2 > len(sonuclar):
            continue
        # ⛔ KOPYANIN İMZASI: künye aynı OLMAKLA kalmayıp sayımın KANITI da yok.
        # Rubrikler kesme ZAMAN KODLARINI ⛔ zorunlu kılar; basılmamışsa sayım
        # yapılmamış, devralınmıştır. Zaman kodu basan iki mercek gerçekten
        # aynı şeyi saymış olabilir — o mutabakattır, kopya değil.
        if not all(m in kodsuz for m in ms):
            continue
        B.append(Bulgu("ŞARTLI",
                       f"⑦ ORTAK DEFTER ŞÜPHESİ — {' + '.join(ms)} künyeleri BİREBİR aynı [D110]",
                       f"kesme {k[0]} · sahne {k[1]} · şerit {k[2]} — ve bu künye "
                       "çoğunluktan sapıyor. Aynı oturumda arka arkaya koşulan iki mercek tek "
                       "ölçümün iki kılıfı olabilir: azınlık İKİ oy değil, BİR oydur. "
                       "⛔ Doğrulama: iki raporun kesme ZAMAN KODLARI var mı? Yoksa sayım "
                       "yapılmamış, devralınmıştır — o mercekler temiz oturumda yeniden koşulur."))

    # ①.9 TESLİM KAPISI [D188] — plan kaç sahne yazdı, makarada kaç sahne var
    if plan_sahne and sah:
        say = {}
        for _, k in sah:
            say[k] = say.get(k, 0) + 1
        cog = max(say, key=lambda k: say[k])
        # ⭐ ÖLÇÜM HAKEMDİR [AGENTS §3]. Verilmişse plan ONA karşı okunur;
        # verilmemişse çoğunluk yalnız bir ŞÜPHE üretebilir, hüküm değil.
        olculen = olcum.get("sahne")
        ref, ref_ad = (olculen, "ÖLÇÜM") if olculen else (cog, f"{say[cog]} merceğin çoğunluğu")
        if ref == plan_sahne:
            B.append(Bulgu("NOT", f"①.9 teslim ekseni doğrulandı — plan {plan_sahne} sahne, "
                                  f"{ref_ad} {ref} [D188] · kaynak: {plan_kaynak}"))
        elif olculen:
            eksik = plan_sahne - olculen
            B.append(Bulgu("GEÇERSİZ",
                           f"🚨 TESLİM EKSİK — plan {plan_sahne} sahne, ÖLÇÜLEN {olculen} [D188]",
                           f"kaynak: {plan_kaynak} · fark {eksik:+d} sahne. Ölçüm hakemdir: "
                           "bu bir rapor sayım hatası DEĞİL, teslim eksiğidir. ⛔ Kesme listesi, "
                           "REMOVE reçetesi ve yeniden üretim UYGULANMAZ; önce hangi sahnenin "
                           "makarada olmadığı ADIYLA yazılır [D46 süre muhasebesi]."))
        else:
            eksik = plan_sahne - cog
            B.append(Bulgu("GEÇERSİZ",
                           f"🚨 TESLİM ŞÜPHESİ — plan {plan_sahne} sahne yazıyor, "
                           f"{say[cog]} mercek {cog} sahne saydı [D188]",
                           f"kaynak: {plan_kaynak} · fark {eksik:+d} sahne (≈ {abs(eksik)} klip). "
                           "⛔ İKİ ŞIK VAR ve rapor tarafından ayrılamaz: "
                           "(a) makara eksik teslim edildi · (b) mercekler yanlış saydı. "
                           "Merceklerin birbirini doğrulaması hiçbirini elemez: hepsi aynı "
                           "makarayı izliyor, ve hem eksik makara hem ortak sayım hatası "
                           "OYBİRLİĞİYLE onaylanır. Parti dışındaki tek referans plandır, "
                           "hakem ise ölçümdür: "
                           "`bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>` "
                           "→ `--olcum-sahne <n>`. ⛔ O gelene kadar kesme listesi, REMOVE "
                           "reçetesi ve yeniden üretim UYGULANMAZ [D46 süre muhasebesi]."))
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
    # ─── MERCEK YOKLAMASI [Ders 111 · D178 · 05.09.2026] ───────────
    # Kapı "yanlış mercek koşuldu"yu görüyordu, "mercek HİÇ koşmadı"yı
    # görmüyordu. 04.09.2026 YERÇEKİMİ FRAGMAN: fragmanın zorunlu merceği
    # (①) hiç koşmadı ve onun yerinde BAŞKA BİR FİLMİN raporu duruyordu.
    kosan = {r["mercek"] for r in sonuclar}
    fragman = any(FRAGMAN_IZI.search(str(r["yol"])) for r in sonuclar)
    zorunlu = ZORUNLU_FRAGMAN if fragman else ZORUNLU_FILM
    eksik = [m for m in zorunlu if m not in kosan]
    if eksik:
        B.append(Bulgu("GEÇERSİZ" if fragman else "ŞARTLI",
                       f"MERCEK YOKLAMASI — {len(eksik)} zorunlu mercek HİÇ koşmadı",
                       f"Eksik: {' · '.join(eksik)}. Koşan: "
                       f"{' · '.join(sorted(kosan)) or '—'}. "
                       f"{'FRAGMAN' if fragman else 'FİLM'} için zorunlu küme: "
                       f"{' · '.join(zorunlu)} [D111]. Eksik mercek 'bulgu yok' "
                       "DEĞİLDİR; ölçülmemiş eksendir ve tamlık matrisine giremez."))

    # ─── FİLİGRAN HAKEMLİĞİ [Ders 177 · 05.09.2026] ────────────────
    # ⑤ SUSKUNLUK kapısı MUTABAKATSIZLIĞI ölçer: "iddia var + sahip sustu".
    # Sekiz mercek BİRDEN susunca ortada mutabakatsızlık yok, sadece sessizlik
    # var — ve sessizlik kapının girdisi değil. D150 bu yüzden dördüncü kez
    # tekrarladı. Çözüm: sıfır iddiada kapıyı ÖLÇÜM ateşler, rapor değil.
    fil = olcum.get("filigran")
    if fil is None:
        B.append(Bulgu("ŞARTLI", "filigran ekseni ÖLÇÜLMEDİ",
                       "⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). "
                       "Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu "
                       "bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten "
                       "var olan hakemliğin aynısı: "
                       "`bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`"))
    elif str(fil).upper().startswith("V"):
        B.append(Bulgu("GEÇERSİZ", "🔴 TESLİM KUSURU — filigran ÖLÇÜMLE doğrulandı",
                       "Master üzerinde sabit köşe işareti var. Hiçbir mercek "
                       "yeniden koşulmaz; önce master YENİDEN İHRAÇ EDİLİR "
                       "[D150 · D177]. ⛔ %3 crop yetmez: temizlik kadraj "
                       "genişliğinin %12'sini götürür."))

    return B


# ─── ÇIKTI ─────────────────────────────────────────────────────────
def tabloya(r):
    if r["karar"] in ("KESİK", "GEÇERSİZ", "TEKRAR"):
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
    isaret = {"GO": "✅", "ŞARTLI": "⚠️ ", "TEKRAR": "⛔", "GEÇERSİZ": "🚨", "KESİK": "✂️"}[r["karar"]]
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


def rapor_yaz(sonuclar, cb, kok, film_adi, bolum=None):
    hedef = kok / "RAPORLAR"
    hedef.mkdir(exist_ok=True)
    bugun = date.today().strftime("%d.%m.%Y")
    # [§2.6] bölüm koşusu kendi dosyasına yazılır — B1 ile B2 aynı gün
    # birbirinin üstüne yazmasın (sayac.sh `<FILM>_*_RAPOR_KONTROL.md` ile bulur)
    ek = f"_B{bolum[0]}" if bolum else ""
    ad = f"{film_adi or 'RAPOR'}{ek}_{date.today().strftime('%Y%m%d')}_RAPOR_KONTROL.md"
    L = [f"# 🧮 RAPOR KONTROL — {film_adi or '(film adı verilmedi)'}"
         + (f" · BÖLÜM {bolum[0]}/{bolum[1]}" if bolum else ""), "",
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


DERS_DONUSU = re.compile(r"^##\s+🔁\s+DERS DÖNÜŞÜ", re.M)


def ders_donusu_kontrol(film_adi):
    """①.12 DERS DÖNÜŞÜ [14.09.2026 · reform FAZ 4 · kontrat §4].

    Her QA koşusunun film kaydı iki satırla biter: hangi ESKİ ders tekrar etti
    (TEKRAR sayacı +1) ve TEK yeni aday (ya da "yok — gerekçe"). Bölüm yoksa NOT —
    eski kayıtlar kırılmaz; yeni koşuda kayıt zinciri tamamlanmamış sayılır.
    """
    kayit = Path(__file__).resolve().parent.parent / "FILM_QA_RAPORLARI" / "01_FILM_RAPORLARI" / f"{film_adi}.md"
    if not kayit.exists():
        print(f"  · ①.12 DERS DÖNÜŞÜ: film kaydı yok ({kayit.name}) — kayıt zinciri adım 2 bekliyor")
        return
    metin = kayit.read_text(encoding="utf-8", errors="replace")
    if DERS_DONUSU.search(metin):
        blok = metin[DERS_DONUSU.search(metin).end():].split("\n## ", 1)[0]
        tekrar = re.search(r"^\s*(?:[-*]\s*)?\**TEKRAR:?\**\s*[:：]?\s*(.+)$", blok, re.M)
        aday = re.search(r"^\s*(?:[-*]\s*)?\**ADAY:?\**\s*[:：]?\s*(.+)$", blok, re.M)
        eksik = [a for a, m in (("TEKRAR", tekrar), ("ADAY", aday)) if not m]
        if eksik:
            print(f"  · ①.12 DERS DÖNÜŞÜ: bölüm var ama satır eksik: {' · '.join(eksik)} (kontrat §4)")
        else:
            print(f"  ✅ ①.12 DERS DÖNÜŞÜ: TEKRAR {tekrar.group(1).strip()[:60]} · ADAY {aday.group(1).strip()[:60]}")
    else:
        print(f"  · ①.12 DERS DÖNÜŞÜ bölümü yok: {kayit.name} — kayıt zinciri adım 2: "
              f"`## 🔁 DERS DÖNÜŞÜ` (TEKRAR · ADAY) ÜÇ SATIRLIK SONUÇ'tan önce [kontrat §4]")


def main():
    argv = sys.argv[1:]
    if not argv or "-h" in argv or "--help" in argv:
        print(__doc__ or "")
        print("KULLANIM: rapor_kontrol.py <rapor.md> [...] [--film <klasör>] [--hook 10] [--klip 10] [--rapor]")
        print("           [--t-tablo]  ← GEÇEN satırı T tablosuna BETİK yazar [④ · 04.09.2026]")
        print("           [--olcum-kesme <n>] [--olcum-sahne <n>] [--olcum-sure <s>]  ← ⑪ ölçümü hakem yapar")
        print("           [--olcum-filigran VAR|YOK] [--olcum-lufs <n>]  ← D177 · verilmezse eksen ÖLÇÜLMEDİ")
        print("           [--bolum n/m]  ← 6/8/16 dk hattı: QA birimi BÖLÜM/PART — ①.9 yalnız o parçanın")
        print("                            bölüm dosya(lar)ını sayar (k dosya / m parça · 16 dk: 8/4), ①.11 uç")
        print("                            kategorileri `—` yapar (KILAVUZ_REHBERI §2.6/§2.7/§2.8)")
        return 1
    hook, klip, film_dir, rapor, dosyalar = 10.0, 10.0, None, False, []
    t_yaz = False
    faz_zorla = None
    bolum = None
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
        elif a == "--t-tablo":
            t_yaz = True; i += 1
        elif a == "--olcum-kesme":
            olcum["kesme"] = int(argv[i + 1]); i += 2
        elif a == "--olcum-sahne":
            olcum["sahne"] = int(argv[i + 1]); i += 2
        elif a == "--olcum-sure":
            olcum["sure"] = float(argv[i + 1].replace(",", ".")); i += 2
        elif a == "--olcum-filigran":
            olcum["filigran"] = argv[i + 1]; i += 2
        elif a == "--olcum-lufs":
            olcum["lufs"] = argv[i + 1]; i += 2
        elif a == "--faz":                                   # [D185] elle beyan
            faz_zorla = argv[i + 1] if i + 1 < len(argv) and not argv[i + 1].startswith("-") \
                        else "operatör beyanı"
            i += 2 if faz_zorla != "operatör beyanı" else 1
        elif a == "--bolum":                                 # [§2.6 · 13.09.2026]
            m_b = BOLUM_ARG.match(argv[i + 1] if i + 1 < len(argv) else "")
            if not m_b or int(m_b.group(1)) < 1 or int(m_b.group(1)) > int(m_b.group(2)):
                print("⛔ --bolum n/m biçiminde olmalı (örn. 1/2 · 2/2), 1 ≤ n ≤ m"); return 2
            bolum = (int(m_b.group(1)), int(m_b.group(2))); i += 2
        else:
            dosyalar.append(Path(a)); i += 1

    spec_metin, film_adi = None, None
    if film_dir:
        film_adi = film_dir.name
        specs = sorted(film_dir.glob("*_QA_SPEC.md"))
        if specs:
            spec_metin = specs[0].read_text(encoding="utf-8", errors="replace")
            print(f"SPEC: {specs[0]}  → ①/④/⑥/⑦/⑧ + ⑨-⑫ için MOD D ZORUNLU")
            goz = goz_kapilari(spec_metin)
            if goz:
                print(f"①.10 GÖZ KAPILARI [D191] — SPEC'te {len(goz)} madde · hiçbir merceğin kapsamında DEĞİL,")
                print("      her biri TEK KAREYLE kapanır; kapanmadan parti kapanmaz:")
                for g in goz:
                    print(f"      ⬜ {g[:150]}")
        else:
            print(f"SPEC: yok ({film_dir}) → mod V bilinçli; ama [D117] film 'yazımı tamam' değil")

    faz = None
    if film_dir is not None or dosyalar:
        ilk = dosyalar[0].read_text(encoding="utf-8", errors="replace") if dosyalar and dosyalar[0].is_file() else ""
        faz = faz_zorla or faz_mi(film_dir, govde_al(ilk))
    if faz:
        print(f"FAZ: {faz}  → ④/⑨/⑫'nin film ölçekli kategorileri SAYI TAŞIMAZ [D185]")
    if bolum and faz:
        print("⛔ --bolum ile FAZ girdisi aynı anda olamaz: bölüm bir UÇ segmenttir, faz bir ORTA segment."); return 2
    if bolum:
        uc = "BAŞ" if bolum[0] == 1 and bolum[1] > 1 else ("SON" if bolum[0] == bolum[1] else "ORTA")
        print(f"BÖLÜM: {bolum[0]}/{bolum[1]} ({uc})  → ①.9 yalnız bu parçanın bölüm dosya(lar)ını sayar · "
              f"①.11 uç kategoriler SAYI TAŞIMAZ [KILAVUZ_REHBERI §2.6 · §2.8]")

    sonuclar = []
    for y in dosyalar:
        if not y.is_file():
            print(f"⚠️  bulunamadı: {y}"); continue
        sonuclar.append(rapor_denetle(y, spec_metin, hook, klip, faz, bolum))
    if not sonuclar:
        return 1
    plan_sahne, plan_kaynak = plan_sahne_sayisi(film_dir, bolum)
    if plan_sahne:
        print(f"PLAN: {plan_sahne} sahne ({plan_kaynak}) → ①.9 teslim kapısı koşacak [D188]")
    elif bolum and film_dir:
        print(f"⚠️  PLAN: *_BOLUM_{bolum[0]}.md'de `## 🎬 SAHNE n` / `## 🎬 KLİP n` başlığı yok → ①.9 teslim kapısı KOŞMAYACAK")
    # ✂️ KESİK koşular ⑤ çaprazına girmez: yarım raporun sahne/kesme sayısı partiyi düşüremez
    tam = [r for r in sonuclar if r["karar"] != "KESİK"]
    cb = capraz(tam, olcum, plan_sahne, plan_kaynak) if len(tam) >= 2 else []
    for r in sonuclar:
        yazdir(r)

    if cb:
        print(f"\n{'═' * 67}\n  ⑤ ÇAPRAZ KAPI — {len(sonuclar)} rapor\n{'═' * 67}")
        for b in cb:
            print(b)
        if any(b.seviye == "GEÇERSİZ" for b in cb):
            for r in tam:
                r["karar_tekil"] = r["karar"]
                r["karar"] = "GEÇERSİZ"
            print("   ▶ parti GEÇERSİZ: hiçbir satır tabloya girmez; ŞERİT ve REPLİK eksenleri yine de okunur [D121]")

    kararlar = [r["karar"] for r in sonuclar]
    if any("karar_tekil" in r for r in sonuclar):
        print("   tekil kararlar (parti düşmeden önce): " +
              " · ".join(f"{r['mercek']} {r.get('karar_tekil', r['karar'])}" for r in sonuclar))
    print(f"\n{'═' * 67}\n  TOPLAM {len(sonuclar)} rapor · 🚨 {kararlar.count('GEÇERSİZ')} GEÇERSİZ · "
          f"⛔ {kararlar.count('TEKRAR')} TEKRAR · ⚠️  {kararlar.count('ŞARTLI')} ŞARTLI · ✅ {kararlar.count('GO')} GO"
          + (f" · ✂️ {kararlar.count('KESİK')} KESİK (koşu değil — yeniden koşulur)" if 'KESİK' in kararlar else "")
          + f"\n{'═' * 67}")
    if t_yaz:
        import t_tablo
        kok = Path(__file__).resolve().parent.parent / "FILM_QA_RAPORLARI"
        print(f"\n{'═' * 67}\n  ④ T TABLOSU — betik yazıyor (elle kopyalama yok)\n{'═' * 67}")
        for r in sonuclar:
            k = t_tablo.satir_kur(r, film_dir, spec_var=spec_metin is not None,
                                  tarih=date.fromtimestamp(r["yol"].stat().st_mtime).strftime("%d.%m"),
                                  bolum=bolum)
            if k is None:
                print(f"   ⛔ {r['mercek']}: {r['karar']} → satır YAZILMADI (tablo okuma kuralı)")
                continue
            print("   " + t_tablo.tabloya_yaz(kok, *k))

    if rapor:
        p = rapor_yaz(sonuclar, cb, Path(__file__).resolve().parent, film_adi, bolum)
        print(f"  rapor yazıldı: {p}")
    if film_adi:
        ders_donusu_kontrol(film_adi)
    if any(k in ("GEÇERSİZ", "TEKRAR", "KESİK") for k in kararlar):
        return 2
    if "ŞARTLI" in kararlar:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
