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
#
#  ─── 26.08.2026 · DÖRT YENİ DENETİM ────────────────────────────────
#  Sebep: TEMA_MUHENDISLIGI · KAMERA_ACISI_PSIKOLOJISI · ACI_YAYI_VE_SEKANS
#  22.08'de yazıldı ve dört gün HİÇBİR kapıda ölçülmedi. Ölçülmeyen kural
#  uygulanmıyor: en yeni dikey filmde 6 kamera satırının 3'ü birebir
#  kopyaydı ve hiçbir kapı bunu görmüyordu. Sistem neyi ölçüyorsa onu
#  optimize etti — kesmeyi ve fiziği ölçüyordu, temayı ve açıyı değil.
#  ⚠️ Tema kapsama oranı için SAYI YAZMA: `bash ../sayac.sh` → 🎭 bloğu
#  (kural ①). Bu yorumda tutulan her oran bir hafta içinde bayatlar.
#     ⑩ KURULUM ÇEŞİTLİLİĞİ  ardışık ikili aynı kurulum (§3) ·
#                            kurulum sayısı bandı (§4)
#     ⑪ AÇI SÖZLÜĞÜ          kaç farklı açı TİPİ kullanılmış (§2)
#     ⑫ ABARTI EŞİĞİ         dutch 35°+ · alt açı 45°+ · üst açı 45-60° (§5)
#     ⑬ TEMA KAPISI          TEMA satırı + en az 3 sahne indeksi (§5/§9)
#
#  ⛔ BU DENETİMLER LOCKOFF KARARINI GERİ ALMAZ. Lockoff KLİP İÇİDİR
#     (02_RISK_KARTLARI KART 8 kapsam bloğu, 26.08.2026 daraltması).
#     Ölçülen tek şey sahneler ARASINDA kurulumun değişmesi — sahneler
#     zaten ayrı kliplerde üretiliyor, teknik riski sıfır.
#
#  ⚠️ KALİBRASYON NOTU: yeni denetimler 107 eski dosyaya koşuldu ve dört
#     yanlış-pozitif sınıfı bulunup kapatıldı (çanak anten eğimi ↔ kamera
#     eğimi · karakter gövde açısı ↔ kamera pitch'i · "at 12 metres"
#     biçiminin imzadan düşmesi · tek çekimin ikiye bölünmüş hâli).
#     TEMA kapısı eski dosyaların çoğunda BLOCK verir — bu bir hata değil,
#     kapı açılmadan önceki durumun ölçüsüdür.
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

# ─── AÇI VE KURULUM KAPISI ─────────────────────────────────────────
# Kaynak: ACI_YAYI_VE_SEKANS_KILAVUZU.md §3 (güvenli bant) · §4 (çeşitlilik
# bandı) · KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md §2 (sekiz açı) · §5 (abartı
# eşikleri) · §6 (açıyı Veo'da sabit tutan sözcükler).
#
# NEDEN VAR (26.08.2026): Bu üç kılavuz 22.08'de yazıldı ve dört gün boyunca
# HİÇBİR kapıda ölçülmedi. Sonuç sahada göründü: deponun en yeni dikey
# filminde 6 video promptunun kamera satırından yalnız 3'ü benzersizdi
# (S0=S2=S5 ve S1=S3 birebir aynı cümle) ve üç kurulumun üçü de yerden
# bakıyordu. Dosya kendi kontrol bloğunda §4 bandını "tutuyor" ilan
# ediyordu ve HAKLIYDI — §4 ASGARİYİ ölçer, açı TİPİNİ hiç saymaz.
#
# ⛔ BU KAPI LOCKOFF KARARINI GERİ ALMAZ. Lockoff KLİP İÇİDİR
#    (02_RISK_KARTLARI KART 8 kapsam bloğu). Burada ölçülen tek şey
#    sahneler ARASINDA kurulumun değişip değişmediği; sahneler zaten ayrı
#    kliplerde üretiliyor, iki klibi farklı açıdan çekmenin gizli kesme
#    riski sıfır (Slow Stone dersi: kesme sorunu MİMARİ sorunuydu).

# Fragman/kapak FİLM DEĞİLDİR: kendi vuruş bütçesi var (FRAGMAN_KILAVUZU §0)
# ve temayı filmden devralır. Kurulum/açı/tema kapıları onlara koşulmaz.
FILM_DISI = re.compile(r"FRAGMAN|KAPAK|TEASER", re.IGNORECASE)

# Açı ve ölçek YALNIZ KAMERA CÜMLELERİNDE aranır.
# ⚠️ Sebep: "she is looking down at her gloves" bir KARAKTER EYLEMİdir,
#    üst açı değil. Cümle süzgeci olmadan her eğilen baş "üst açı" sayılır
#    ve monoton film çeşitli görünür — kapının tam tersine çalışır.
KAMERA_IZI = re.compile(r"\b(camera|lens|tripod|shot|framing|angle|frame)\b",
                        re.IGNORECASE)

# KAMERA_ACISI §2'nin sekizlisi. Desenler §6 reçetelerinin sözcüklerinden
# alındı — kılavuzun "açıyı Veo'da sabit tutan" dediği kelimeler bunlar.
# ⚠️ Kılavuz sözlüğü DIŞINDA yazılmış açı (örn. "locked-off tripod, low")
#    bilerek sayılmaz: §6'nın tüm iddiası modelin o biçimi tutmadığı.
ACI_TIPLERI = {
    "alt açı":  r"low[- ]angle|pointing\s+up(?:ward)?|aimed\s+[^.;]{0,30}\bup\b|"
                r"from\s+below|worm'?s[- ]eye|\bup\s+at\s+(?:her|him|the)\b",
    "üst açı":  r"high[- ]angle|looking\s+down(?:ward)?|from\s+above|"
                r"aimed\s+[^.;]{0,30}\bdown\b|\bdown\s+at\s+(?:her|him|the)\b",
    "tepe":     r"overhead|bird'?s[- ]eye|top[- ]down|directly\s+down|zenith|"
                r"straight\s+down",
    "eğik":     r"\bdutch\b|tilted\s+(?:exactly\s+)?\d|\bcanted\b",
    "göz hizası": r"eye[- ]level|eye\s+height",
    "OTS":      r"over[- ]the[- ]shoulder|\bOTS\b|over\s+(?:her|his|their)\s+shoulder",
    "profil":   r"\bprofile\b|side[- ]on\b",
    "POV":      r"\bPOV\b|point[- ]of[- ]view|subjective\s+(?:shot|view)",
}

# ACI_YAYI §3 ölçek merdiveni: EWS – WS – MS – CU – ECU.
# Sıra ÖNEMLİ: en dar kalıp önce aranır, yoksa "extreme close-up" CU'ya düşer.
OLCEK_MERDIVENI = [
    ("ECU", r"extreme\s+close[- ]?up|\bECU\b|\bXCU\b"),
    ("CU",  r"close[- ]?up|\bCU\b|\bMCU\b|medium\s+close"),
    ("MS",  r"medium\s+(?:full\s+)?shot|\bMS\b|\bMLS\b|medium\s+long|waist\s+shot"),
    ("EWS", r"extreme\s+wide|extreme\s+long|\bEWS\b|\bXLS\b|establishing"),
    ("WS",  r"wide\s+shot|long\s+shot|\bWS\b|\bLS\b|full\s+shot"),
]

# ⛔ DEVAM KLİBİ MUAFİYETİ: bir çekim iki klibe bölündüğünde ikinci klip
#    AYNI kurulumu taşımak ZORUNDADIR — sürekliliğin kendisi budur
#    (TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU). Muafiyet olmadan kapı, doğru
#    yazılmış iki parçalı çekimi "monoton" sayıyor: bir filmde 20 saniyelik
#    tek çekimin iki yarısı ardışık ihlal olarak raporlandı.
DEVAM_KLIBI = re.compile(
    r"continues?\s+the\s+previous\s+clip|from\s+its\s+exact\s+last\s+frame|"
    r"(?:second|third|fourth|latter)\s+(?:half|part)\s+of\s+a\s+single|"
    r"same\s+lockoff|same\s+altitude,?\s+same|picks?\s+up\s+where\s+the\s+previous",
    re.IGNORECASE)

LENS_MM = re.compile(r"(\d{1,3})\s*mm\b", re.IGNORECASE)
# ⚠️ Yükseklik ve mesafe DÖRT ayrı biçimde yazılıyor ve dördü de imzadır.
#    İlk sürüm yalnız "N metres above the ground" ve "N metres from" biçimini
#    tanıdı; "locked off at 12 metres" ve "low angle at 0.8 meters height"
#    biçimleri imzadan düştü ve İKİ FİLM haksız BLOCK yedi — mesafesi 12 m
#    ile 5 m olan iki sahne "aynı kurulum" göründü. Kurulum imzası eksik
#    ölçerse kapı monotonluğu değil KENDİ KÖRLÜĞÜNÜ raporlar.
YUKSEKLIK = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:m\b|metres?|meters?)\s+(?:above|off)\s+the\s+\w+|"
    r"\d+(?:[.,]\d+)?\s*(?:m\b|metres?|meters?)\s+(?:height|high)\b|"
    r"camera\s+height[:\s]+\d+(?:[.,]\d+)?|"
    r"height\s+(?:of\s+)?\d+(?:[.,]\d+)?\s*(?:m\b|metres?|meters?)|"
    r"(?:waist|chest|knee|eye|shoulder|ground|head|hip)[- ]height",
    re.IGNORECASE)
MESAFE = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:m\b|metres?|meters?)\s+"
    r"(?:from|away|back|behind|in\s+front)|"
    r"(?:at|from)\s+\d+(?:[.,]\d+)?\s*(?:m\b|metres?|meters?)"
    r"(?!\s*(?:height|high|above|off))",
    re.IGNORECASE)

# ─── ABARTI EŞİKLERİ (KAMERA_ACISI §5) ─────────────────────────────
# ⛔ DERECE KAMERAYA AİT OLMAK ZORUNDA. İlk sürüm kamera cümlesindeki HER
#    dereceyi kamera açısı saydı ve iki dosyaya haksız BLOCK verdi:
#      · Starless Circle: "dish tilted at 70 degrees" — eğilen ÇANAK ANTEN,
#        kamera değil (aynı cümlede "frame" geçtiği için kamera cümlesiydi)
#      · Tall Shore: "angled 60 degrees to frame left" — KARAKTERİN gövde
#        yönü; kadraj içi yerleşim, kamera pitch'i değil
#    Bu yüzden genel desen kaldırıldı; yalnız sahibi AÇIKÇA kamera olan
#    iki kalıp ölçülür. Yakalayamadığı biçim olabilir — haksız BLOCK'tan
#    iyidir (kapının inandırıcılığı tek atışlık).
# ⚠️ Pencere [^;] kullanır, [^.;] DEĞİL: kamera cümleleri ONDALIK SAYI
#    taşıyor ("camera height 0.50 metres, pitched up 55 degrees") ve nokta
#    dışlanınca desen tam da ölçmesi gereken cümlede kopuyordu. Cümle
#    sınırı zaten kamera_cumleleri() tarafından çizilmiş durumda.
DERECE_EGIK = re.compile(
    r"(?:\bdutch\b[^;]{0,60}?|tilted\s+exactly\s+|"
    r"\b(?:camera|lens|shot|framing)\b[^;]{0,40}?"
    r"\b(?:tilted|canted|rolled)\s+(?:to\s+the\s+\w+\s+)?)"
    r"(\d+(?:\.\d+)?)\s*[- ]?degrees?", re.IGNORECASE)
DERECE_PITCH = re.compile(
    r"\b(?:camera|lens|tripod)\b[^;]{0,60}?\bpitched\s+(up|down)\s+"
    r"(\d+(?:\.\d+)?)\s*[- ]?degrees?", re.IGNORECASE)
# ⚠️ Kamera cümlesinde de açı DIŞI derece geçer: görüş açısı, sıcaklık,
#    enlem, güneşin yüksekliği. Bunlar eşik denetiminden muaf.
DERECE_MUAF = re.compile(
    r"field\s+of\s+view|\bFOV\b|celsius|fahrenheit|temperature|latitude|"
    r"kelvin|minus\s+\d+\s*degrees|\bsun\b[^.;]{0,30}degrees", re.IGNORECASE)

# ─── TEMA KAPISI ───────────────────────────────────────────────────
# Kaynak: TEMA_MUHENDISLIGI_KILAVUZU.md §9 madde 1 + §5 matrisi ·
# KILAVUZ_REHBERI §6 adım 1: "tema yoksa DURMA, film koreografi olur".
#
# ⚠️ SATIR BAŞI ŞART: depo "IŞIK = TEMA:" / "YAPI = TEMA:" gibi cümle içi
#    kullanımlar da taşıyor (4 dosyada) ve onlar tema BEYANI değil.
# ⚠️ BÜYÜK HARF ŞART ve ara sözcükler yalnız HARF: alan adı ile düz cümleyi
#    ayıran şey bu. Gevşek desen üç şeyi tema sandı — "TEMA → MOTİF ① FIRÇA:"
#    (matris başlığı), "Tema sayacın içinde: ..." (düz cümle) ve "**Tema:**
#    'From Arithmetic to Release'" (MÜZİK teması). Üçü de tema beyanı değil.
# ⚠️ "TEMAS:" (dokunma) bu desene TAKILMAZ: TEMA'dan sonra harf gelemez,
#    yalnız boşluk/parantez/iki nokta gelebilir.
TEMA_SATIRI = re.compile(
    r"^[ \t>*_#·\-]*\**[ \t]*(?:TEMA|THEME)"
    r"(?:[ \t]+[A-Za-zÇĞİÖŞÜ][A-Za-zÇĞİÖŞÜ ]{0,17}|"
    r"[ \t]*\([A-Za-z ]{1,18}\))?[ \t]*[::]",
    re.MULTILINE)
SAHNE_INDEKSI = re.compile(r"\bS\d{1,2}\b")
TEMA_PENCERE = 900        # karakter · tema satırından sonra indeks aranan alan


def kamera_cumleleri(govde):
    """Promptun yalnız KAMERA cümleleri (pozitif gövdeden)."""
    poz = duzles(pozitif_govde(govde))
    return [c.strip() for c in re.split(r"(?<=[.;])\s+", poz) if KAMERA_IZI.search(c)]


def aci_tipleri(cumleler):
    """Kullanılan açı TİPLERİ kümesi (KAMERA_ACISI §2)."""
    bulunan = set()
    for c in cumleler:
        tepe_var = re.search(ACI_TIPLERI["tepe"], c, re.IGNORECASE)
        for ad, kalip in ACI_TIPLERI.items():
            # "looking straight down" hem tepe hem üst açı deseni taşır;
            # kılavuzda tepe AYRI bir açıdır, iki kez sayılmaz.
            if ad == "üst açı" and tepe_var:
                continue
            if re.search(kalip, c, re.IGNORECASE):
                bulunan.add(ad)
    return bulunan


def _ilk(desen, metin):
    m = desen.search(metin)
    return re.sub(r"\s+", " ", m.group(0)).lower() if m else None


def kurulum_imzasi(cumleler):
    """Kurulum = açı + ölçek + kamera konumu (ACI_YAYI §4 tanımı).

    Sahneye özel kelimeler ("from the woman" ↔ "from the lander") imzaya
    girmez; yalnız SAYILABİLİR geometri girer. Böylece aynı kurulumun iki
    farklı cümleyle yazılması çeşitlilik sanılmaz.
    """
    t = " ".join(cumleler)
    olcek = next((ad for ad, k in OLCEK_MERDIVENI if re.search(k, t, re.IGNORECASE)),
                 None)
    return (_ilk(LENS_MM, t), _ilk(YUKSEKLIK, t), _ilk(MESAFE, t),
            olcek, frozenset(aci_tipleri(cumleler)))


def kurulum_ozet(k):
    """İmzayı okunur tek satıra çevir — bulgunun kanıtı budur."""
    lens, yuk, mes, olcek, acilar = k
    parcalar = [x for x in (lens, yuk, mes, olcek) if x]
    if acilar:
        parcalar.append("+".join(sorted(acilar)))
    return " · ".join(parcalar) if parcalar else "kamera geometrisi yazılmamış"


def tema_bul(yol, metin):
    """Tema satırını dosyada, yoksa KLASÖR KOMŞULARINDA ara.

    Tema film dosyasında da, PLAN'da da, <FILM>_QA_SPEC.md'de de yazılabilir
    (25.08.2026'dan beri her film kendi klasöründe). Betik dosya-bazlı koştuğu
    için komşuya bakmazsa doğru yazılmış filme "tema yok" der.
    """
    m = TEMA_SATIRI.search(metin)
    if m:
        return metin, m, yol.name
    for kardes in sorted(yol.parent.glob("*.md")):
        if kardes == yol:
            continue
        try:
            k_metin = kardes.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        m = TEMA_SATIRI.search(k_metin)
        if m:
            return k_metin, m, kardes.name
    return None, None, None


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

    # ⑨ ABARTI EŞİĞİ — KAMERA_ACISI §5 · etkinin kiçe döndüğü sayılar
    for cumle in kamera_cumleleri(govde):
        if DERECE_MUAF.search(cumle):
            continue          # görüş açısı / sıcaklık / enlem / güneş — açı değil
        kisa = cumle.strip()[:110]

        for m in DERECE_EGIK.finditer(cumle):
            d = float(m.group(1))
            if d >= 35:
                bulgular.append(Bulgu(
                    "BLOCK", f"eğik açı {d:g}° — KİÇ EŞİĞİ (§5: 35-45°↑)",
                    f"...{kisa}... · parodi/amatör algısı, illüzyon çöker. "
                    "Deponun ideal bandı 5-15°, stilize üst sınır 30°."))
            elif d > 30:
                bulgular.append(Bulgu(
                    "FIX", f"eğik açı {d:g}° — stilize bandın üstünde (§5)",
                    f"...{kisa}... · 15-30° meşru, 35°+ kiç. Bu değer sınırda."))

        for m in DERECE_PITCH.finditer(cumle):
            yon, d = m.group(1).lower(), float(m.group(2))
            if yon == "up" and d >= 45:
                bulgular.append(Bulgu(
                    "BLOCK", f"kamera {d:g}° yukarı pitch — SOLUCAN BAKIŞI (§5: 45°↑)",
                    f"...{kisa}... · karakter dev robot değilse grotesk çizgi "
                    "roman paneli okunur. Meşru alt açı bandı 15-30°."))
            elif yon == "down" and 45 <= d <= 60:
                bulgular.append(Bulgu(
                    "FIX", f"kamera {d:g}° aşağı pitch — ÖLÜ BÖLGE (§5: 45-60°)",
                    f"...{kisa}... · ne tanrısal ne insani; \"kötü yerleştirilmiş "
                    "güvenlik kamerası\" hissi. 15-30° ya da 90° (tepe) seç."))

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

    # ─── AÇI VE KURULUM KAPISI ─────────────────────────────────────
    # Üç denetim de SAYILABİLİR: kurulum imzası, imza sayısı, açı tipi sayısı.
    # Fragman/kapak muaf (FILM_DISI) · 4 sahneden kısa dosyada yay ölçülmez.
    video = [p for p in promptlar if p["tip"] == "video" and not p["yedek"]]
    if not FILM_DISI.search(yol.name) and len(video) >= 4:
        kurulumlar = [kurulum_imzasi(kamera_cumleleri(p["govde"])) for p in video]
        n = len(kurulumlar)

        # ① ARDIŞIK İKİLİ AYNI KURULUM (ACI_YAYI §3: "aynı kurulum arka arkaya
        #    gelemez" · KURGU_RITMI §2 örüntü kırıcı kapısının betiğe inmişi)
        for i in range(1, n):
            if kurulumlar[i] != kurulumlar[i - 1]:
                continue
            dolu = sum(1 for x in kurulumlar[i] if x)
            if not dolu:
                continue      # kamera hiç yazılmamış — ③ bunu ayrıca söyler
            if DEVAM_KLIBI.search(video[i]["govde"]):
                continue      # tek çekimin ikinci yarısı — aynı kurulum ŞART
            # ⚠️ Zengin imza (≥2 bileşen) tartışmasızdır: iki sahne aynı lens,
            #    aynı yükseklik/mesafe, aynı ölçek ve aynı açı tipiyle yazılmış.
            #    Tek bileşenli imza ölçüm zayıflığı olabilir → yalnız uyarır.
            seviye = "BLOCK" if dolu >= 2 else "FIX"
            sonuc["dosya_bulgulari"].append(Bulgu(
                seviye,
                f"ardışık iki sahne AYNI KURULUM (satır "
                f"{video[i - 1]['satir']} ↔ {video[i]['satir']})",
                f"{kurulum_ozet(kurulumlar[i])} · ACI_YAYI §3 güvenli bant: "
                "ardışık çift ≥1 ölçek kademesi VE ≥45° açı farkı ister. "
                "⛔ Klip içi lockoff korunur; değişen sahneler ARASI kurulumdur."))

        # ② KURULUM SAYISI BANDI (ACI_YAYI §4)
        benzersiz = len(set(kurulumlar))
        asgari = 3 if n >= 6 else max(2, n // 2)
        # ⚠️ ÜST BANT YALNIZ UZUN FORMATTA. §4 "yarısını geçmez" kuralını
        #    12-18 sahne için yazıyor; 6 sahnelik filme yalnız ASGARİ koyar.
        #    İlk sürüm yarı kuralını her formata uyguladı ve 6 sahnede 5
        #    kurulum kullanan filmleri "dağınık" saydı — 57 yanlış gözlem.
        azami = -(-n // 2) if n >= 12 else None
        if benzersiz < asgari:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", f"kurulum çeşitliliği {benzersiz} — {n} sahnede en az "
                       f"{asgari} olmalı (§4)",
                "Altı = güvenlik kamerası hissi, ritim ölür. Kurulum = açı + "
                "ölçek + kamera konumu; yalnız mesafe değiştirmek kurulum "
                "değiştirmek değildir."))
        elif azami and benzersiz > azami:
            # ⚠️ Üst bant GÖZLEM: imza sahneye özel kelimelerden değil
            #    geometriden kurulsa da, yazım biçimi farkı sayıyı şişirebilir.
            #    Ölçülmemiş bir üst sınırla üretim durdurulmaz (image bandı emsali).
            sonuc["dosya_bulgulari"].append(Bulgu(
                "NOT", f"kurulum sayısı {benzersiz} — {n} sahnede üst bant {azami} (§4)",
                "Üstü = mekânsal algı çöker. Bilinçliyse plana tek satır "
                "gerekçe yaz [D74]."))

        # ③ AÇI TİPİ SAYISI (KAMERA_ACISI §2 sekizlisi)
        tipler = set()
        for p in video:
            tipler |= aci_tipleri(kamera_cumleleri(p["govde"]))
        if not tipler:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", "açı HİÇ yazılmamış — kılavuz sözlüğünden tek kelime yok",
                "KAMERA_ACISI §6: açıyı Veo'da sabit tutan sözcükler bellidir "
                "(\"low angle\", \"high angle\", \"Dutch angle\", \"over-the-shoulder\"). "
                "\"locked-off tripod, low\" biçimi modelin tutmadığı biçimdir."))
        elif len(tipler) < 3 and n >= 6:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", f"açı TİPİ {len(tipler)} — {n} sahnede en az 3 olmalı (§2)",
                f"kullanılan: {', '.join(sorted(tipler))} · Kurulum sayısı bandı "
                "tutsa bile üç kurulumun üçü de aynı açıdan bakıyorsa çeşitlilik "
                "yoktur, yalnız mesafe değişir (Bright Tether vakası)."))

    # ─── TEMA KAPISI ───────────────────────────────────────────────
    # TEMA_MUHENDISLIGI §9 madde 1 · §5 matrisi
    # KILAVUZ_REHBERI §6 adım 1: "tema yoksa DURMA, film koreografi olur"
    if not FILM_DISI.search(yol.name):
        t_metin, t_m, t_kaynak = tema_bul(yol, metin)
        if not t_m:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "BLOCK", "TEMA satırı yok (dosyada ve klasör komşularında)",
                "TEMA_MUHENDISLIGI §3'ün sekiz temasından biri + §9: tema "
                "novum kelimesi geçmeden tek cümleyle söylenebilmeli. "
                "⚠️ Depodaki tema kapsama oranı: bash sayac.sh → 🎭 bloğu. "
                "Bu kapı 26.08.2026'da açıldı; ondan önce tema hiçbir yerde "
                "ölçülmüyordu, yani eski dosyaların çoğu BLOCK verir."))
        else:
            pencere = t_metin[t_m.end():t_m.end() + TEMA_PENCERE]
            indeks = set(SAHNE_INDEKSI.findall(pencere))
            if len(indeks) < 3:
                sonuc["dosya_bulgulari"].append(Bulgu(
                    "FIX", f"tema {len(indeks)} sahne indeksi taşıyor — en az 3 "
                           f"olmalı ({t_kaynak})",
                    "TEMA §5 matrisi temayı MOTİFE, motifi SAHNEYE bağlar. "
                    "Sahne numarası yazılmayan tema dekoratiftir — Kaleida "
                    "Crash kaydının tema satırı: \"bedel yok → tema dekoratif "
                    "kalıyor\" (Tema 5/10, aynı kayıtta Karakter 4/10)."))

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
