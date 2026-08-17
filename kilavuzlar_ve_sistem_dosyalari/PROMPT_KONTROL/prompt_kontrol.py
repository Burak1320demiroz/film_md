#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
#  PROMPT KONTROL — üretimden ÖNCE koşan tek sıfır maliyetli kapı
# ═══════════════════════════════════════════════════════════════════
#
#  NEDEN VAR:
#  KILAVUZ_REHBERI §6 adım 3.5 bu denetimi 31.07.2026'dan beri çağırıyor
#  ama dosya hiç depoya inmedi (18 commit tarandı, tek iz yok). Bu arada
#  iki film — THE HOLDING FIELD ve THE HERD — denetimin yerine geçen
#  listeyi KENDİ dosyasının içine elle yazdı. Aynı iş, iki ayrı biçim,
#  kalan filmlerde hiç. Sistem bilgisi film dosyasına gömülünce başka
#  filme uygulanamıyor (SHORTS_QA'nın "KULE 7" vakası, 31.07.2026).
#
#  NEDEN BETİK, NEDEN RUBRİK DEĞİL:
#  Diğer yedi rubrik dış modelde, depoyu göremeden koşar (05.08.2026
#  kararı: "göremediğin depoda dosya var deme"). Bu denetimin girdisi
#  ise zaten depodaki .md dosyasıdır. Aşağıdaki kontrollerin hepsi
#  sayılabilir ve tartışmasızdır — modele sorulacak bir yanı yok.
#  Yargı isteyen yarı ayrı dosyada: PROMPT_QA_CRITIQUE_PROMPT.md
#
#  KULLANIM:
#      python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py <dosya|klasör> ...
#      ... --rapor        RAPORLAR/ altına markdown rapor da yazar
#
#  ÇIKTI:  GO / FIX / BLOCK   — BLOCK ise üretme.
#  ÇIKIŞ KODU: 0 = GO · 1 = FIX · 2 = BLOCK   (betikten zincirlenebilir)
# ═══════════════════════════════════════════════════════════════════

import re
import sys
from datetime import date
from pathlib import Path

# ─── EŞİKLER ───────────────────────────────────────────────────────
# Kaynak: KILAVUZ_REHBERI.md §7 BİLİNEN TUZAKLAR · PROMPT UZUNLUĞU
# "Eşiğe değil BANDA yaz. Eşik 'burada kesin patlar' demek,
#  'buraya kadar güvenli' demek değil."
BANT = {
    "image": (1700, 2100),   # §7 hedef bandı — ⚠️ TARTIŞMALI, aşağıya bak
    "video": (2000, 2600),   # §7 hedef bandı
}

# ⛔ TAVAN YALNIZ VİDEO PROMPTUNA UYGULANIR.
# §7'nin cümlesi: "~4.300 karakter → VEO hata veriyor (Low Power S5, S11)".
# Veo video üretir; ölçüm video promptundan alındı. Image promptu başka
# modele gider ve o modelin eşiği bu depoda HİÇ ölçülmedi. Image'a video
# eşiği uygulamak, ölçülmemiş bir sayıyla üretim durdurmak olur.
TAVAN = 4300

# §7'nin image bandı depodaki HİÇBİR filmle uyuşmuyor:
#   Holding Field 3.417-4.017 · Third Dune 2.732-4.154 · Quiet Impact
#   4.577-5.644 — üçü de bandın en az bir katı üstünde.
# Ya bant bayat, ya image için hiç ölçülmedi. Karar verilene kadar image
# uzunluğu BULGU değil GÖZLEM olarak raporlanır; üretim durdurmaz.
IMAGE_BANDI_KARARA_BAGLI = True

# ─── YASAK KELİMELER ───────────────────────────────────────────────
# Her biri bir dersten geldi. Yasağın İÇİNDE geçmesi meşrudur
# (Ders 85: "çalışan yasağı silme önerisi reçete DÜŞER") — bu yüzden
# aşağıda olumsuzlama bağlamı ayrıca kontrol edilir.
YASAK = {
    "glowing":            "D29 · bloom",
    "ethereal":           "D29 · bloom",
    "radiant":            "D29 · bloom",
    "shimmering":         "D29 · bloom",
    "swirl":              "D39 · toz sıvı gibi akıyor",
    "cinematic lighting": "D33 · mumsu cilt + bloom",
}
OLUMSUZ = re.compile(r"(?:\bno\b|\bnot\b|\bnever\b|\bzero\b|\bwithout\b)[^.]{0,40}$",
                     re.IGNORECASE)

# ─── ARANAN KİLİTLER ───────────────────────────────────────────────
# KILAVUZ_REHBERI §5 negatif çekirdeğin ölçülebilir imzaları.
# Çekirdeğin tam metni her promptta birebir aranmaz — filmler sahneye
# özel kısaltılmış negatif blok yazıyor ve bu meşru. Aranan, her
# birinin KARŞILIĞININ bir biçimde bulunması.
# (kalıp, hangi prompt tipinde aranır) — "tek çekim" bir HAREKET kilididir,
# durağan karede karşılığı yoktur; image promptunda aranırsa her film
# yanlış yere bayrak yer.
KILITLER = {
    "tek çekim":     (r"single unbroken take|one continuous|no cuts|single take",
                      ("video",)),
    "bloom yasağı":  (r"0% bloom|no bloom|zero bloom|no glow",
                      ("image", "video")),
    "metin yasağı":  (r"no readable text|never letters|no letters|no subtitles|"
                      r"no digits|never numerals|no numerals",
                      ("image", "video")),
    "insan sayısı":  (r"exactly \d+ human|exactly one human|human count",
                      ("image", "video")),
    "film grain":    (r"film grain|photorealistic",
                      ("image", "video")),
}

# ─── D79 KASK BLOĞU ────────────────────────────────────────────────
# Ders 79 (06.08.2026): Bible'da yasaklamak YETMEDİ — Unbroken City ve
# Starless Circle'ın ikisi de sırt ünitesi + aynalı vizör üretti.
KASK_IZI = re.compile(r"\bhelmet|\bvisor|\bsuit\b|kask|vizör", re.IGNORECASE)
D79_ARKA = re.compile(r"no back-mounted|flat back|back silhouette is flat", re.IGNORECASE)
D79_VIZOR = re.compile(r"zero tint|no tint|optically clear|fully readable through", re.IGNORECASE)

# ─── YÖN KAPISI ────────────────────────────────────────────────────
# Kaynak: UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md sürüm 2 (13.08.2026)
# Kılavuzun §10.1 kontrol listesinin makine tarafı. Üç şeyi arar ve
# üçü de SAYILABİLİR — modele sorulacak bir yanı yok, bu yüzden burada.
#
# ⚠️ Kapı KADEME 2'yi (saat kadranı) zorunlu KILMAZ; yalnız yönelimin
#    bir biçimde yazılmış olmasını arar. Kademe 2 depoda henüz
#    ölçülmedi (kılavuz §11) — ölçülmemiş bir dille üretim durdurulmaz.

# ① Pusula kelimeleri: modelin pusulası yok, bu kelimeler yazı-turadır.
# ⚠️ Yalnız YERLEŞTİRME/HAREKET kullanımı aranır. Depo pusula kelimesini
#    ikinci bir işte de kullanıyor: yer işaretine AD veriyor ("northern
#    crater rim", "the tower's west face", "southern belt"). Ad, kadrajda
#    yön tarif etmez ve Ders 58 kimlik çapasının bir parçasıdır —
#    yasaklanırsa çalışan bir mekanizma bozulur.
PUSULA = re.compile(
    r"(?:\bto\s+the\s+|\bfacing\s+|\bheads?\s+|\bheading\s+|\bruns?\s+|"
    r"\bwalks?\s+|\bmoves?\s+|\bdrifts?\s+|\bleans?\s+|"
    r"\b\d+\s*(?:m|meters?|metres?|km|kilometers?|kilometres?)\s+)"
    r"(north|south|east|west)(ward|wards)?\b"
    r"|\b(north|south|east|west)\s+of\b",
    re.IGNORECASE)
# ⚠️ "-ern" biçimi (northern / western) BİLEREK dışarıda: depo onu yön
#    talimatı olarak değil AD olarak kullanıyor — "the western ridge",
#    "northern crater rim", "the tower's west face". Çıplak biçim
#    ("12 degrees to the north", "forty meters east of the habitat")
#    ise gerçek bir yazı-turadır. İlk sürüm ikisini ayırmadı ve bir
#    manzara adını BLOCK'ladı.

# ② Çapasız "toward": hedefin ekran konumu AYNI CÜMLEDE yoksa
#    "toward the ship" cümlesi geminin nerede olduğunu söylemiyordur.
# ⚠️ Yalnız YOLCULUK fiilleriyle aranır. "hand rises toward the rim",
#    "chain runs toward the hinge", "rotation decaying toward zero" —
#    üçü de yön kilidi istemiyor; özne kadrajda bir yere GİTMİYOR.
# ⚠️ Çıplak "head/heads" fiil listesinde YOK: "her head bowed toward the
#    bowl" cümlesindeki head bir ORGANDIR, yolculuk fiili değil. İlk
#    sürüm bunu fiil sandı ve baş çevirme anlatan her beat bayrak yedi.
TOWARD = re.compile(
    r"\b(runs?|running|walks?|walking|moves?|moving|heading|"
    r"drives?|driving|flies|flying|approach(?:es|ing)?|sprints?|sprinting|"
    r"marches|marching|strides?|striding|advances?|advancing|"
    r"races?|racing|climbs?|climbing|crawls?|crawling)\b[^.;]{0,60}?"
    r"\btowards?\b",
    re.IGNORECASE)
EKRAN_CAPASI = re.compile(
    r"(screen|camera|frame)[\s-]?(left|right)|"
    r"\b(left|right|upper|lower|top|bottom|centre|center)[\s-]"
    r"(third|half|quarter|corner|edge|side)\b|"
    r"\b(foreground|background|midground)\b|o'clock|\bx\s*=|\bdegrees?\b|"
    r"\b(?:the\s+)?(?:camera|lens|viewer)\b|"          # kadran 6/12 = nötr
    r"\b(?:LEFT|RIGHT)\b",                            # promptlarda kapital vurgu
    re.IGNORECASE)

# ③ Nesne-göreli taraf: karakterin solu izleyicinin sağıdır.
# ⚠️ "the frame's left" / "the shot's right" zaten EKRAN-görelidir —
#    kadrajın solu izleyicinin solu demektir. Sahibi kadrajsa muaf.
NESNE_GORELI = re.compile(
    r"\b(?:to|on|at)\s+(?:his|her|their|its|"
    r"the\s+(?!frame|screen|shot|image|picture)\w+'s)\s+(?:left|right)\b",
    re.IGNORECASE)
# ⚠️ ÖZELLİK mi KONUM mu — ayrımı isim listesiyle kovalamak işe yaramadı
#    (nostril · cuff · face · portion · right-facing... liste bitmiyor).
#    Yapıya bağlandı: nesne-göreli taraf bir İSİM TAMLAMASINI sürdürüyorsa
#    ("on her LEFT eyebrow", "a mirror on its LEFT cuff") bu bir KARAKTER
#    ÖZELLİĞİdir ve nesne-göreli olmak ZORUNDADIR — ekran-göreliye
#    çevrilirse yara izi kesmeler arasında taraf değiştirir (Ders 58).
#    Tamlama noktalama ile BİTİYORSA ("To her left, dense foliage";
#    "To its right: two circles") taraf bir KONUM anlatıyordur ve
#    ekran-göreli yazılmalıdır. Bulgu yalnız ikinci hâlde açılır.
NESNE_GORELI_KONUM = re.compile(r"^\s*[,.:;—-]")

# ④ Araç var mı — varsa yönelimi yazılmış olmalı (kılavuz §5.1 soru ①)
ARAC_IZI = re.compile(
    r"\b(ship|lander|shuttle|craft|capsule|rover|buggy|vehicle|hull|"
    r"pod|freighter|transport)\b", re.IGNORECASE)
# Yönelim imzası: saat kadranı, burun/kıç yönü, gövde yönü, yan tarif.
YONELIM_IZI = re.compile(
    r"o'clock|\bheading\b|\bbow\b|stern-?first|"
    r"\bnose\s+(?:point|facing|toward|to\s+screen|at\s+)|"
    r"(?:port|starboard)\s+(?:flank|side|beam)|"
    r"(?:facing|faces|angled|oriented)\s+(?:screen|camera)-?(?:left|right)",
    re.IGNORECASE)
# ⚠️ İmza ARACIN YANINDA aranır. İlk sürüm dosyanın herhangi bir yerinde
#    arıyordu ve Third Dune'da figürlerin "angled camera-right" cümlesi
#    kapıyı kapattı — oysa filmin ARACININ yönelimi hiçbir yerde yazılı
#    değil. Aracın yönelimini figürünki karşılayamaz (kılavuz §2 İLKE 4).
YONELIM_PENCERE = 220     # karakter · araç kelimesinin iki yanı

# ─── A1 ÇELİŞKİSİ ──────────────────────────────────────────────────
# 03_PLAN_ONCESI_KONTROL_LISTESI A1: "EN PAHALI HATA".
# Model her zaman YASAĞI seçer, anlatım sessizce ölür ve QA'da görünmez.
A1_YASAK = re.compile(r"no readable text|never text|no text\b|no digits|no numerals",
                      re.IGNORECASE)
# ⚠️ Desen EKRAN GÖSTEREN bir nesne istemek zorunda. İlk sürüm yalnız
# "shows <sayı>" arıyordu ve Third Dune'un "polished inner section now
# shows 40 centimetres of clean metal" cümlesini ekran metni sandı —
# o bir mekanik betimleme. Yasak↔anlatım çelişkisi ancak bir GÖSTERGE
# ile bir OKUNAN DEĞER yan yana geldiğinde vardır.
# Gösterilen şey OKUNABİLİR bir değer olmak zorunda: tırnak içi dize,
# rakam, ya da BÜYÜK HARF etiket. Bu depo sayaçlarını bilinçli olarak
# METİNSİZ kanallara taşıyor (Ring Light'ın 8 gözlü darbe göstergesi,
# Blind Return'ün gölge boyu) — "the gauge shows eight sockets" bir
# ihlal değil, tam da istenen çözümdür. Değer kısmı bu yüzden
# büyük/küçük harfe DUYARLI kalır; prefix (?i:...) ile duyarsız.
A1_ICERIK = re.compile(
    r"(?i:\b(?:screen|display|readout|monitor|panel|gauge|counter|indicator|"
    r"dial|HUD|timer|clock)\b[^.]{0,40}?"
    r"\b(?:reads?|displays?|shows?|reading|showing)\b)\s*"
    r"(?:[\"“][^\"”]{1,40}[\"”]|\d)")
# ⚠️ BÜYÜK HARF vurgusu değer sayılmaz. Bu depo promptlarda vurgu için
# kapital kullanıyor ("showing ABSTRACT DRIFTING LIGHT SEGMENTS") ve
# o cümle A1'in İHLALİ değil ÇÖZÜMÜdür: bilgi metinsiz kanala taşınmış.
# Aranan imza Tidal Hunt'ınki: "the countdown reads 6:00:00" — yani
# tırnak içi dize ya da rakam.

# ─── PROMPT BAŞLIĞI ────────────────────────────────────────────────
# Yatay filmler:  ### 📸 IMAGE PROMPT   /  ### 🎥 VIDEO PROMPT
# Dikey shorts:   ### 📸 GÖRSEL PROMPT  /  ### 🎥 VİDEO PROMPT
# Yedek sürümler: "### 🎥 VIDEO PROMPT — B SÜRÜMÜ" → sayıma girmez
BASLIK = re.compile(r"^#{2,4}\s*.*?\b(IMAGE|GÖRSEL|VIDEO|VİDEO)\s+PROMPT(.*)$",
                    re.IGNORECASE)
SAHNE_BASLIK = re.compile(r"^##\s+.*\bSAHNE\s+\d+", re.IGNORECASE | re.MULTILINE)
SCENE_N_OF_X = re.compile(r"Scene\s+(\d+)\s+of\s+(\d+)", re.IGNORECASE)
TURKCE = re.compile(r"[ğĞşŞıİçÇöÖüÜ]")


class Bulgu:
    """Tek bir denetim sonucu. seviye: BLOCK · FIX · NOT"""

    def __init__(self, seviye, baslik, ayrinti=""):
        self.seviye = seviye
        self.baslik = baslik
        self.ayrinti = ayrinti

    def __str__(self):
        isaret = {"BLOCK": "⛔", "FIX": "⚠️ ", "NOT": "·"}[self.seviye]
        satir = f"   {isaret} {self.baslik}"
        if self.ayrinti:
            satir += f"\n        {self.ayrinti}"
        return satir


def promptlari_cikar(metin):
    """Prompt başlığını izleyen İLK çitli bloğu al.

    Film dosyalarında prompt olmayan çitli bloklar da var (⚙️ ÇEKİM
    PLANI, ⚠️ ÜRETİM UYARISI, QA SPEC). Yalnız başlığın hemen
    ardındaki blok prompttur.
    """
    satirlar = metin.split("\n")
    promptlar = []
    i = 0
    while i < len(satirlar):
        m = BASLIK.match(satirlar[i])
        if not m:
            i += 1
            continue

        tip = "image" if m.group(1).upper() in ("IMAGE", "GÖRSEL") else "video"
        ek = (m.group(2) or "").strip(" —-·")
        yedek = "SÜRÜM" in ek.upper() and not ek.upper().startswith("A ")

        # başlıktan sonraki ilk ``` çitini bul (en fazla 6 satır boşluk)
        j = i + 1
        while j < len(satirlar) and j < i + 8 and not satirlar[j].startswith("```"):
            j += 1
        if j >= len(satirlar) or not satirlar[j].startswith("```"):
            i += 1
            continue

        k = j + 1
        govde = []
        while k < len(satirlar) and not satirlar[k].startswith("```"):
            govde.append(satirlar[k])
            k += 1

        promptlar.append({
            "tip": tip,
            "etiket": ek,
            "yedek": yedek,
            "satir": i + 1,
            "govde": "\n".join(govde),
        })
        i = k + 1
    return promptlar


def pozitif_govde(govde):
    """NEGATIVE bloğunu ayır.

    Ders 85 mantığı: yasağın içinde geçen kelime ihlal değildir.
    Third Dune'da bir QA önerisi filmin metin yasağını silecekti;
    dize depoda yalnız yasağın içinde vardı.
    """
    parca = re.split(r"^NEGATIVE:", govde, maxsplit=1, flags=re.MULTILINE)
    return parca[0]


def duzles(metin):
    """Satır sarmasını kaldır.

    Promptlar ~78 sütuna sarılmış yazılıyor; "No\\nreadable text" gibi
    bölünen her kalıp desenlerden kaçar. İlk koşuda dört sahne bu
    yüzden "metin yasağı eksik" damgası yedi — yasak yerindeydi,
    satır ortasından bölünmüştü. Karakter sayımı HAM gövdeden alınır,
    desen araması bu düzlenmiş metinden.
    """
    return re.sub(r"\s+", " ", metin)


def repliksiz(govde):
    """Tırnak içindeki replikleri çıkar.

    Replik Türkçedir ve öyle olmalıdır — VEO kılavuzu §3 tırnak
    sentaksı. Türkçe taraması yalnız promptun KENDİ metnine bakar;
    yoksa diyaloglu her film yanlış yere bayrak yer.

    ⚠️ Yalnız ÇİFT tırnak sayılır. Kesme işareti ("the lander's nose")
    tırnak sanılırsa açılan aralık repliği yutar ve replik dışarıda
    kalır — ilk koşuda Ring Light S0 tam bu yüzden bayrak yedi.
    """
    return re.sub(r"[\"“”][^\"“”]{0,300}[\"“”]", " ", govde)


def prompt_denetle(p):
    bulgular = []
    govde = p["govde"]
    govde_d = duzles(govde)                    # desen araması için
    poz_d = duzles(pozitif_govde(govde))
    n = len(govde)                             # sayım HAM gövdeden

    # ① UZUNLUK
    # Yedek sürümlerde (B/C/D) bant UYGULANMAZ: §7'nin yapısal red
    # çözümü zaten "NEGATIVE bloğunu kaldır, minimale in" diyor.
    # Reçeteyi uygulayan promptu reçeteye uymadı diye cezalandırmayız.
    alt, ust = BANT[p["tip"]]
    if p["tip"] == "image" and IMAGE_BANDI_KARARA_BAGLI:
        # Ölçülmemiş eşikle üretim durdurulmaz — yalnız gözlem yazılır.
        if n > ust:
            bulgular.append(Bulgu("NOT", f"uzunluk {n} — image bandının ({alt}-{ust}) üstünde",
                                  "Bu bant depodaki hiçbir filmle uyuşmuyor; karar bekliyor."))
    elif n > TAVAN:
        bulgular.append(Bulgu("BLOCK", f"uzunluk {n} — kanıtlı Veo red eşiğinin ({TAVAN}) üstünde",
                              "Low Power S5/S11 bu eşikte hata verdi. Üretme, kısalt."))
    elif n > ust:
        bulgular.append(Bulgu("FIX", f"uzunluk {n} — video bandının ({alt}-{ust}) üstünde",
                              "Third Dune'un beş reddi de bandın üstündeydi, hiçbiri tavanı aşmamıştı."))
    elif n < alt and not p["yedek"]:
        bulgular.append(Bulgu("FIX", f"uzunluk {n} — video bandının ({alt}-{ust}) altında",
                              "Kısa prompt kilitleri taşımıyor olabilir; kilit listesini kontrol et."))

    # ② YASAK KELİME — yalnız pozitif gövdede, olumsuzlama bağlamı hariç
    for kelime, kaynak in YASAK.items():
        for m in re.finditer(re.escape(kelime), poz_d, re.IGNORECASE):
            onceki = poz_d[max(0, m.start() - 45):m.start()]
            if OLUMSUZ.search(onceki):
                continue          # "no glowing" → yasak, ihlal değil
            cevre = poz_d[max(0, m.start() - 40):m.end() + 30].strip()
            bulgular.append(Bulgu("FIX", f"yasak kelime: \"{kelime}\" ({kaynak})",
                                  f"...{cevre}... · pozitif gövdede, yasak bloğunda değil"))

    # ③ SELF-CONTAINED (kural ③)
    if re.search(r"\[BIBLE|see BIBLE|bkz\.|BIBLE'a bak", govde_d, re.IGNORECASE):
        bulgular.append(Bulgu("BLOCK", "BIBLE atfı var — prompt self-contained değil",
                              "AGENTS.md kural ③: her prompt tek başına çalışmalı."))

    # ④ PROMPT İÇİNDE TÜRKÇE — replikler hariç (VEO §3 tırnak sentaksı)
    temiz = repliksiz(govde_d)
    ornek = TURKCE.search(temiz)
    if ornek:
        cevre = temiz[max(0, ornek.start() - 35):ornek.start() + 35].replace("\n", " ")
        bulgular.append(Bulgu("FIX", "prompt gövdesinde Türkçe metin (replik değil)",
                              f"...{cevre.strip()}... · modele giden gövde İngilizce olmalı"))

    # ⑤ KİLİT VARLIĞI — yedek sürümlerde aranmaz
    # B/C/D sürümlerinin VARLIK SEBEBİ negatif bloğun kaldırılmasıdır.
    if not p["yedek"]:
        eksik = [ad for ad, (kalip, kapsam) in KILITLER.items()
                 if p["tip"] in kapsam and not re.search(kalip, govde_d, re.IGNORECASE)]
        if eksik:
            bulgular.append(Bulgu("FIX", f"negatif çekirdek imzası eksik: {', '.join(eksik)}",
                                  "KILAVUZ_REHBERI §5 · sahneye özel kısaltma meşru, yokluk değil."))

    # ⑥ PUSULA KELİMESİ — modelin pusulası yok (uzamsal kılavuz §4.4)
    for m in PUSULA.finditer(poz_d):
        cevre = poz_d[max(0, m.start() - 40):m.end() + 40].strip()
        bulgular.append(Bulgu(
            "BLOCK", f"dünya-uzayı yön kelimesi: \"{m.group(0).strip()}\"",
            f"...{cevre}... · ekran-uzayına çevir (screen-left/right). "
            "Model pusula bilmez; bu cümle her üretimde yazı-turadır."))

    # ⑦ ÇAPASIZ "toward" — hedefin ekran konumu aynı cümlede olmalı
    for cumle in re.split(r"(?<=[.;])\s+", poz_d):
        if TOWARD.search(cumle) and not EKRAN_CAPASI.search(cumle):
            bulgular.append(Bulgu(
                "FIX", "çapasız \"toward\" — hedefin ekran konumu aynı cümlede yok",
                f"...{cumle.strip()[:120]}... · uzamsal kılavuz §6.1: hedefin "
                "ekran dilimi yazılmazsa koşu yönü serbest kalır."))

    # ⑧ NESNE-GÖRELİ TARAF — karakterin solu izleyicinin sağıdır
    for m in NESNE_GORELI.finditer(poz_d):
        if not NESNE_GORELI_KONUM.match(poz_d[m.end():m.end() + 4]):
            continue          # "on her LEFT eyebrow" — karakter özelliği
        cevre = poz_d[max(0, m.start() - 35):m.end() + 35].strip()
        bulgular.append(Bulgu(
            "FIX", f"nesne-göreli taraf: \"{m.group(0)}\"",
            f"...{cevre}... · ekran-göreli yaz (screen-left / screen-right)."))

    return bulgular


# Şablon ve kılavuz dosyaları film değildir: içlerindeki "prompt" blokları
# yer tutucu ve TALİMAT taşır ("ANTI-GLOW: 'glowing' KULLANMA") — denetime
# sokulursa kendi yasak listesini ihlal sayarlar.
ATLA = re.compile(r"/kilavuzlar/|SABLON|ŞABLON|TEMPLATE", re.IGNORECASE)


def dosya_denetle(yol):
    if ATLA.search(str(yol)):
        return None
    metin = yol.read_text(encoding="utf-8", errors="replace")
    promptlar = promptlari_cikar(metin)
    if not promptlar:
        return None

    sonuc = {"yol": yol, "promptlar": [], "dosya_bulgulari": []}

    for p in promptlar:
        p["bulgular"] = prompt_denetle(p)
        sonuc["promptlar"].append(p)

    # ─── DOSYA SEVİYESİ ────────────────────────────────────────────
    tum_prompt = duzles(" ".join(p["govde"] for p in promptlar))
    poz_tum = duzles(" ".join(pozitif_govde(p["govde"]) for p in promptlar))

    # A1 — yasak ↔ anlatım çelişkisi (en pahalı hata)
    if A1_YASAK.search(tum_prompt):
        icerik = A1_ICERIK.search(poz_tum)
        if icerik:
            cevre = poz_tum[max(0, icerik.start() - 40):icerik.end() + 20].replace("\n", " ")
            sonuc["dosya_bulgulari"].append(Bulgu(
                "BLOCK", "A1 ÇELİŞKİSİ — metin yasağı ile ekran içeriği aynı dosyada",
                f"...{cevre.strip()}... · Tidal Hunt: sayaç ekrana hiç çıkmadı (D50)"))

    # Scene N of X — iddia edilen sahne sayısı dosyayla tutuyor mu
    sahne_sayisi = len(SAHNE_BASLIK.findall(metin))
    iddialar = {int(x) for _, x in SCENE_N_OF_X.findall(tum_prompt)}
    if len(iddialar) > 1:
        sonuc["dosya_bulgulari"].append(Bulgu(
            "FIX", f"\"Scene N of X\" tutarsız — dosyada {sorted(iddialar)} birden geçiyor"))
    elif iddialar and sahne_sayisi and sahne_sayisi not in iddialar:
        sonuc["dosya_bulgulari"].append(Bulgu(
            "FIX", f"\"Scene N of {iddialar.pop()}\" ama dosyada {sahne_sayisi} sahne başlığı var",
            "Kaleida Crash: 13 iddia · 12 blok · SAHNE 3 hiç yok"))

    # D34 — karakter özel adı promptta geçiyor mu (SPEC'teki PROTAGONIST)
    kahraman = re.search(r"^\s*PROTAGONIST:\s*(.+)$", metin, re.MULTILINE)
    if kahraman:
        ad = kahraman.group(1).strip().split(",")[0].split("—")[0].split("(")[0].strip()
        ilk = ad.split()[0] if ad and ad[0].isalpha() else ""
        if len(ilk) > 2 and re.search(rf"\b{re.escape(ilk)}\b", tum_prompt):
            sonuc["dosya_bulgulari"].append(Bulgu(
                "BLOCK", f"karakter özel adı promptta: \"{ilk}\" (D34)",
                "Özel ad jenerik/başlık kartı halüsinasyonu tetikliyor."))

    # D79 — kasklı filmde iki cümle var mı
    if KASK_IZI.search(metin):
        eksik79 = []
        if not D79_ARKA.search(tum_prompt):
            eksik79.append("sırt ünitesi yasağı")
        if not D79_VIZOR.search(tum_prompt):
            eksik79.append("vizör şeffaflığı")
        if eksik79:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", f"D79 bloğu eksik: {', '.join(eksik79)}",
                "Bible'da yasaklamak YETMEDİ — iki filmde de sırt ünitesi üretildi. "
                "⛔ Vizör tasarım gereği renkli/aynalıysa bu bulgu DÜŞER."))

    # YÖN KAPISI ④ — araçlı filmde yönelim hiç yazılmamış
    # Uzamsal kılavuz §5.1 soru ①: "hangi uç önde?" cevapsızsa gemi
    # kıçından yanaşır, burnu geriye bakarak iner. Konum kilidi
    # (right third) bu boşluğu KAPATMAZ — kılavuz §2 İLKE 4.
    # ⛔ Dosya seviyesi bilerek: yönelim tek bir SPATIAL LOCK BIBLE
    #    bloğunda kurulup sahnelerde kısaltılabilir, bu meşru.
    arac_gecisi = list(ARAC_IZI.finditer(poz_tum))
    if arac_gecisi:
        kilitli = any(
            YONELIM_IZI.search(poz_tum[max(0, m.start() - YONELIM_PENCERE):
                                       m.end() + YONELIM_PENCERE])
            for m in arac_gecisi)
        if not kilitli:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", "araç var ama yönelim kilidi yok (uzamsal kılavuz §5.1)",
                f"{len(arac_gecisi)} araç geçişinin hiçbirinin yakınında saat "
                "kadranı / burun yönü / yan tarifi yok. Herd: gemi park yeri "
                "keyfî değişti · Holding Field: giden gemi park hâlinde döndü."))

    return sonuc


def karar(sonuc):
    tum = [b for p in sonuc["promptlar"] for b in p["bulgular"]] + sonuc["dosya_bulgulari"]
    if any(b.seviye == "BLOCK" for b in tum):
        return "BLOCK"
    if any(b.seviye == "FIX" for b in tum):
        return "FIX"
    return "GO"


def yazdir(sonuc):
    asil = [p for p in sonuc["promptlar"] if not p["yedek"]]
    yedek = [p for p in sonuc["promptlar"] if p["yedek"]]
    k = karar(sonuc)
    isaret = {"GO": "✅", "FIX": "⚠️ ", "BLOCK": "⛔"}[k]

    print(f"\n{'═' * 67}")
    print(f"{isaret} {k}  ·  {sonuc['yol']}")
    print(f"   {len(asil)} prompt" + (f" (+{len(yedek)} yedek sürüm, sayıma girmez)" if yedek else ""))
    print("═" * 67)

    for p in sonuc["promptlar"]:
        if not p["bulgular"]:
            continue
        etiket = f" — {p['etiket']}" if p["etiket"] else ""
        yedek_not = "  [yedek]" if p["yedek"] else ""
        print(f"\n  {p['tip'].upper()} · satır {p['satir']}{etiket}{yedek_not} · "
              f"{len(p['govde'])} karakter")
        for b in p["bulgular"]:
            print(b)

    if sonuc["dosya_bulgulari"]:
        print("\n  📄 DOSYA SEVİYESİ")
        for b in sonuc["dosya_bulgulari"]:
            print(b)

    # uzunluk özeti — bant tartışması için ham veri
    for tip in ("image", "video"):
        boylar = [len(p["govde"]) for p in asil if p["tip"] == tip]
        if boylar:
            print(f"\n  📏 {tip}: {min(boylar)}-{max(boylar)} karakter "
                  f"(bant {BANT[tip][0]}-{BANT[tip][1]} · tavan {TAVAN})")


def rapor_yaz(sonuclar, kok):
    hedef = kok / "RAPORLAR"
    hedef.mkdir(exist_ok=True)
    bugun = date.today().strftime("%d.%m.%Y")
    for s in sonuclar:
        ad = s["yol"].stem + "_PROMPT_KONTROL.md"
        satirlar = [f"# 🔎 PROMPT KONTROL — {s['yol'].stem}", "",
                    f"> **Tarih:** {bugun}  ·  **Karar:** {karar(s)}",
                    f"> **Kaynak:** `{s['yol']}`",
                    "> Bu rapor betikten üretildi, elle düzenlenmez.", ""]
        for p in s["promptlar"]:
            if not p["bulgular"]:
                continue
            satirlar.append(f"## {p['tip'].upper()} · satır {p['satir']} · "
                            f"{len(p['govde'])} karakter"
                            + ("  _(yedek sürüm)_" if p["yedek"] else ""))
            for b in p["bulgular"]:
                satirlar.append(f"- **{b.seviye}** — {b.baslik}"
                                + (f"<br>{b.ayrinti}" if b.ayrinti else ""))
            satirlar.append("")
        if s["dosya_bulgulari"]:
            satirlar.append("## 📄 Dosya seviyesi")
            for b in s["dosya_bulgulari"]:
                satirlar.append(f"- **{b.seviye}** — {b.baslik}"
                                + (f"<br>{b.ayrinti}" if b.ayrinti else ""))
        (hedef / ad).write_text("\n".join(satirlar) + "\n", encoding="utf-8")
        print(f"   → RAPORLAR/{ad}")


def main():
    argv = [a for a in sys.argv[1:] if a != "--rapor"]
    rapor = "--rapor" in sys.argv
    kok = Path(__file__).resolve().parent

    if not argv:
        print(__doc__ or "")
        print("KULLANIM: python3 prompt_kontrol.py <dosya|klasör> ... [--rapor]")
        return 1

    hedefler = []
    for a in argv:
        y = Path(a)
        if y.is_dir():
            hedefler += sorted(y.rglob("*.md"))
        elif y.is_file():
            hedefler.append(y)
        else:
            print(f"⚠️  bulunamadı: {a}")

    sonuclar = []
    for y in hedefler:
        s = dosya_denetle(y)
        if s:
            sonuclar.append(s)

    if not sonuclar:
        print("Prompt bloğu olan dosya bulunamadı.")
        print("Aranan başlık: '### 📸 IMAGE/GÖRSEL PROMPT' · '### 🎥 VIDEO/VİDEO PROMPT'")
        return 1

    for s in sonuclar:
        yazdir(s)

    kararlar = [karar(s) for s in sonuclar]
    print(f"\n{'═' * 67}")
    print(f"  TOPLAM {len(sonuclar)} dosya · "
          f"⛔ {kararlar.count('BLOCK')} BLOCK · "
          f"⚠️  {kararlar.count('FIX')} FIX · "
          f"✅ {kararlar.count('GO')} GO")
    print("═" * 67)

    if rapor:
        rapor_yaz(sonuclar, kok)

    if "BLOCK" in kararlar:
        return 2
    if "FIX" in kararlar:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
