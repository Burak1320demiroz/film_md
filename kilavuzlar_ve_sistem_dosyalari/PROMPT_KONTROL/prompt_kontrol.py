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
#  ⭐ FİLM KLASÖRÜNÜ VER, TEK BÖLÜMÜ DEĞİL (01.09.2026 · klasör modu):
#      film bölüm dosyalarına ayrıldığından beri dizi kapıları dosya
#      sınırında körleşiyor. Klasör verilince (tek dosya verilse bile onun
#      klasörü) bölümler sahne sırasına göre BİRLEŞTİRİLİP kapılar film
#      boyunca bir kez daha koşar. Gerekçe: aşağıdaki "KLASÖR MODU" bloğu.
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
#  ─── 05.09.2026 · ⑩'A DÖRDÜNCÜ AYAK (sahip kararı — dört soru onaylandı) ──
#  Teşhis sahibin: "durmadan 10 saniyede bir bambaşka bir kamera açısına
#  geçmesi kafa karıştırıyor." Ölçüm: 1.406 sahne / 1.287 kesme, kesmelerin
#  neredeyse tamamı YENİ bakış noktasına; 87 uzun dosyanın 63'ü §4 üst
#  bandının üstünde ve hiçbiri durmuyor (üst bant NOT'tu). Üç kapı
#  çeşitliliğe itiyordu, dönüşe iten sıfır kapı vardı.
#     ⑩④ KURULUM İSKELETİ    küme ≥2 · dönüş ≥%40 · işaret satırları ·
#                            aynı harf = aynı ölçülen kurulum (§3 🕰️ · §4b · §7 ⑥)
#                            ⛔ YALNIZ 'KURULUM İSKELETİ:' beyan eden dosyada koşar
#     ⑪ AÇI SÖZLÜĞÜ          kaç farklı açı TİPİ kullanılmış (§2)
#     ⑫ ABARTI EŞİĞİ         dutch 35°+ · alt açı 45°+ · üst açı 45-60° (§5)
#     ⑬ TEMA KAPISI          TEMA satırı + en az 3 sahne indeksi (§5/§9)
#  ─── 01.09.2026 · İKİ DENETİM DAHA (Ders 157 · Ders 139 — ikisi de kapısızdı) ──
#     ⑭ NOVUM TAŞIYICI       taşıyıcı nesne TEK KARE satırında geçiyor mu (ONERME §4①)
#     ⑮ SIRT POZİTİF        kamera arkada/OTS ise pozitif sırt yüzeyi cümlesi var mı
#  ─── 02.09.2026 · İKİ DENETİM DAHA (Ders 167 · Ders 169) ──────────────────
#     ⚠️ NUMARA ÇAKIŞMASI: ⑰ aynı gün B5 HİKÂYE OMURGASI'na verildi
#        (başka koşu, 15:18). Bu ikisi ⑲/⑳'ye taşındı — numara ilk gelenindir.
#     ⑲ KİMLİK YIĞINI       tek pencerede ≥4 kişi özniteliği (boy·ten·saç·yaş·yüz)
#                           → "ünlüyü tarif ederek isteme" kalıbı; OMNI reddetti
#     ⑳ ZORLANMA KANALI     efor fiili var ama gövde tepkisi cümlesi yok
#     ⑳b DEĞİŞİM KAPISI     imaj promptu değişimin SONRASINI yazıyor (I2V'de
#                           imaj t=0'dır) — 05.09.2026 [D179]
#     ㉑ MÜHÜR KAPISI       mühürlü filmde uzva ANATOMİ ayrıntısı yazılıyor ama
#                           ±12 kelimede örtü adı yok · çıplak-deri negatifi
#                           üç sınırı birden yazmıyor — 05.09.2026 [D175]
#     ㉒ YÜZEY RENK KAPISI  IŞIK bloğu biyom düzlemine (floor/ground/wall) RENK
#                           atıyor; renk ENVIRONMENT'ın işidir — 05.09.2026 [D176]
#  ─── 01.09.2026 · POLİTİKA KAPISI (Ders 123 — "betik göremez" denilen yer) ──
#     ⑯ POLİTİKA SÖZLÜĞÜ     T1/T2 tetikleyici sayımı (NEGATIVE bloğu DÂHİL) ·
#                            gövdeye yönelmiş şiddet fiili · milliyet · kurum ·
#                            insansız sahne + uzun NEGATIVE (yapısal red profili)
#     ⛔ D123 "betik bunu göremez ve göremez de" diyordu. KOMPOZİSYON ekseni
#        için doğru (YERCEKIMI S8: kelimeler temizdi, kadraj reddedildi) →
#        o eksen PROMPT_QA_CRITIQUE'in insan yarısındadır. KELİME ekseni için
#        yanlış: LAST SPAN'in dosyasında "gore" 29 kez geçiyordu ve iki aksiyon
#        doruğu reddedildi. Bir sayım bunu üretimden ÖNCE yakalar.
#     Kılavuz: ../POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md
#     Defter:  ../FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md  ← bant oradan gelir
#  ─── 02.09.2026 · HİKÂYE KAPISI (03_PLAN_ONCESI B5 · üç gün "ayrılmış" kaldı) ──
#     ⑰ B5 HİKÂYE OMURGASI  İSTEK · ENGEL · BEDEL · MUHATAP satırları +
#                           İSTEK niteliği ("anlamak" istek değildir) +
#                           BEDEL niteliği (kaybın GÖRÜLDÜĞÜ sahne numarası) +
#                           iki insanlı planda AYRILIK sahnesi (B5b)
#     ✏️ 02.09.2026 · "ORTAM hasım değildir" denetimi GERİ ÇEKİLDİ (yazıldığı
#        gün): insan-hasım ↔ doğa-hasım farkının izleyici tarafında ölçülmüş
#        karşılığı yok. Yerine BEDEL sahne denetimi geldi — ölçülmüş olan o.
#        Kayıt: ../URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md T4.0
#     ⛔ NEDEN BETİĞE İNDİ: 05_DIKEY_HAT_TESHISI §5① bu satırı 30.08'de
#        sıfır maliyetli BİRİNCİ madde olarak yazdı, listeye inmedi ve üç
#        günde beş film yazıldı → ENGEL satırı 79 filmin 2'sinde çıktı.
#        Deponun kendi dersi: yazılan ama koşulmayan kapı, koşulmamış kapıdır.
#     Kaynak: ../URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md §3.1 · §4①-②
#     ⚠️ ⑰ KALİBRASYONU · 02.09.2026 · 80 film klasörü:
#        koştu 69 · atlandı 11 (eski sahne başlığı biçimi — ⑭ ile AYNI sınır)
#        koşan 69'un 69'unda en az bir B5 satırı EKSİK. Bu bir hata değil,
#        kapının açıldığı günkü durumun ölçüsüdür (TEMA kapısının 26.08
#        tablosuyla aynı okuma). En yakın film THE LEANING ROOM: yalnız
#        HASIM eksik — B5'i kapı inmeden kendi yazmıştı.
#        ⛔ SAYIYI BURADA GÜNCELLEME: bayatlar. Yeniden ölçmek için
#           prompt_kontrol'ü format klasörlerine koş ve "B5 satırı yok" say.
#
#  ⚠️ ⑯ KALİBRASYONU · 01.09.2026 · 5 format klasörü, 140 kayıt:
#     60 kayıtta (%43) politika sözcüğü bulundu — T1 119 · T2 746 · şiddet
#     fiili 7 · milliyet 32 (3 film) · kurum 1 · yapısal red profili 20.
#     ⛔ KARARI DEĞİŞEN DOSYA: 0. Hepsi zaten başka kapıdan FIX/BLOCK'tu.
#        Yani ⑯ bugün üretim DURDURMUYOR, BİLGİ ÜRETİYOR — ve ürettiği ilk
#        bilgi şu: THE_DEAD_APPROACH · THE_HOLLOW_STATION · THE_KALEIDA_CRASH
#        canlı promptlarında §7'nin DOĞRULANMIŞ red tetikleyicisini taşıyor.
#     Dört yanlış-pozitif sınıfı kapatıldı; listesi POLITIKA_T1'in üstünde.
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

# ─── ⑯ POLİTİKA SÖZLÜĞÜ [Ders 123 · 01.09.2026] ─────────────────────
#
# ⛔ BU SÖZLÜK YUKARIDAKİ `YASAK` SÖZLÜĞÜNÜN MANTIKSAL TERSİDİR.
#    D29 kelimelerinde olumsuzlama MEŞRUDUR ("no glowing" bir çözümdür).
#    Politika kelimelerinde olumsuzlama HASTALIĞIN TA KENDİSİDİR:
#    politika sınıflandırıcısı "no" önekini değil KELİMEYİ okur, ve
#    yasakladığın kavram promptun İÇİNE girer [D123].
#
# NEDEN BETİK — D123 "betik bunu göremez ve göremez de" diyordu:
#    Kompozisyon ekseni için doğru (YERCEKIMI S8: kelimeler temizdi,
#    kadraj reddedildi → o eksen PROMPT_QA_CRITIQUE'in insan yarısında).
#    KELİME ekseni için YANLIŞ ve bedeli ölçüldü: THE LAST SPAN'in
#    prompt dosyasında "gore" 29 · "blood" 26 · "wounds" 26 · "corpse"
#    18 kez geçiyordu, HEPSİ yasak olarak, ve iki aksiyon doruğu
#    reddedildi. Bir `grep` bunu üretimden ÖNCE, sıfır kare harcayarak
#    yakalardı. Ölçülmeyen kural uygulanmıyor.
#
# ⚠️ KAPI SAYAR, ÜRETİM DURDURMAZ — sayı ölçülene kadar.
#    `IMAGE_BANDI_KARARA_BAGLI` ile aynı gerekçe: bu depoda "kaç
#    tetikleyici redde yol açar" HİÇ ölçülmedi. LAST SPAN'de 99 geçiş
#    vardı ve reddedildi; 3 geçişin ne yaptığı bilinmiyor. Ölçülmemiş
#    bir eşikle üretim durdurmak, ölçülmemiş bir sayıyla karar vermektir.
#    Bant RED DEFTERİ'nden gelir (FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md);
#    defterde ≥5 vaka biriktiğinde bu bayrak kapanır ve T1 BLOCK'a çıkar.
#    ⛔ İSTİSNA: MİLLİYET. O ölçüldü (§7 "doğrulandı", LOW POWER) → BLOCK.
POLITIKA_BANDI_KARARA_BAGLI = True

# ─── KALİBRASYON · 01.09.2026 · 5 format klasörü, 137 dosya ──────────
# Dört yanlış-pozitif sınıfı bulundu ve kapatıldı:
#   ① "wound"    → bu depo GEMİ GÖVDESİ için kullanıyor ("a still-glowing
#                  deep-orange reactor wound in the hull", 6 geçiş tek
#                  filmde). Yara değil delik. → T2'ye indi.
#   ② "skeleton" → iki meşru kullanım: "the proportions follow a human
#                  skeleton" (oran tarifi) ve yapı iskeleti. → T2'ye indi.
#                  ⚠️ NEGATIVE'deki "no skeleton, no body, no remains"
#                  gerçek bulgudur ve T2 yoğunluk sayacında görünür.
#   ③ "stab"     → 24 geçişin 24'ü MÜZİK terimi ("orchestral stabs",
#                  "string stab"). → listeden ÇIKTI; yönelmiş bıçaklama
#                  zaten POLITIKA_FIIL'de.
#   ④ "drives his" → "drives his boot sole against the strut" kendi
#                  uzvudur, şiddet değil. → fiil kapısı yalnız NESNE
#                  konumundaki kişiyi ve GÖVDE PARÇASINI arar.

# T1 — bu depoda POLİTİKA DIŞI meşru kullanımı ÖLÇÜLMEMİŞ kelimeler.
#      Kaynak: D123 teşhis listesi + THE SLOW STONE S4 sözlük kilidi.
POLITIKA_T1 = {
    r"\bgore\b":                    "D123 · LAST SPAN'de 29 kez",
    r"\bblood(?:y|ied|ing)?\b":     "D123 · LAST SPAN'de 26 kez",
    r"\bcorpses?\b":                "D123 · LAST SPAN'de 18 kez",
    r"\bcadavers?\b":               "D123 ailesi",
    r"\bmutilat\w*\b":              "D123 ailesi",
    r"\bdismember\w*\b":            "D123 ailesi",
    r"\bdecapitat\w*\b":            "D123 ailesi",
    r"\bamputat\w*\b":              "D123 ailesi",
    r"\bstrangl\w*\b":              "D123 ailesi",
    r"\bsuffocat\w*\b":             "D123 ailesi",
    r"\btortur\w*\b":               "D123 ailesi",
    r"\bvictims?\b":                "D123 teşhis listesi",
    r"\bjump scare\b":              "D123 teşhis listesi",
    r"\bhorror\b":                  "D123 · SLOW STONE S4 negatif bloğu",
    r"\bzombie\w*\b":               "SLOW STONE S4 · red aldı",
    r"\brotting\b|\bdecompos\w*\b": "SLOW STONE S4 ailesi",
    r"\bweapons?\b":                "D123 teşhis listesi",
    r"\bguns?\b|\brifles?\b":       "§7 · gerçek ordu/silah",
}

# T2 — bağlama duyarlı. Tek geçiş normaldir; YOĞUNLUK bulgudur.
#      "body" deseni deponun KENDİ çözümünü ("four body-lengths across")
#      dışarıda bırakır — yoksa kapı en iyi uygulamayı cezalandırır.
POLITIKA_T2 = {
    r"\bwound(?:s|ed|ing)?\b":      "D123 · LAST SPAN'de 26 kez (kalibrasyon ①)",
    r"\bskeletal\b|\bskeletons?\b": "SLOW STONE S4 (kalibrasyon ②)",
    r"\bdead\b|\bdeath\b|\bdying\b":          "SLOW STONE S4 · red aldı",
    r"\bbod(?:y|ies)\b(?!\s*[-–—]?\s*lengths?)": "SLOW STONE S4 · red aldı",
    r"\binjur\w*\b":                          "D123 teşhis listesi",
    r"\bkill(?:s|ed|ing)?\b":                 "D123 ailesi",
    r"\bdanger(?:ous)?\b":                    "LAST SPAN S9 red mesajı",
    r"\bpanic\w*\b":                          "SHORTS md.5 · panik yasağı",
    r"\bterror\w*\b":                         "D123 ailesi",
    r"\bscream\w*\b":                         "D123 ailesi",
    r"\bsuffer\w*\b":                         "D123 ailesi",
    r"\bdecay\w*\b":                          "SLOW STONE S4 · red aldı",
    r"\bexplo(?:sion|de|des|ding|sive)\w*\b": "D56/D67 · ateş sözlüğü",
    r"\bblasts?\b":                           "D56/D67 · ateş sözlüğü",
    r"\bflames?\b|\bburning\b|\bablaze\b":    "D56/D67 · ateş sözlüğü",
    r"\bsmoke\b":                             "YERCEKIMI KİLİT 8",
    r"\btrapped\b":                           "YERCEKIMI KİLİT 8 ailesi",
    r"\bdrown\w*\b":                          "D56 · dalış sözlüğü",
    # TUR 3 · çift anlamlı — YALNIZ bu biri eklendi. Ölçüm (01.09.2026):
    # naked 6 · fire 496 · strike 154 · shot 3.605 geçiş. Üçü eklenseydi
    # depodaki her video promptu yanlış bayrak yerdi; "shot" zaten negatif
    # çekirdeğin kendi cümlesinde ("single unbroken shot"). Bedava nötr
    # hâli olan tek kelime bu: naked → bare (depo `bare`'i 1.048 kez
    # kullanıyor, yani ikame zaten deponun kendi deyimi).
    # ⚠️ "naked eye" MUAF: görme keskinliği deyimi, çıplaklıkla ilgisi yok
    #    (kalibrasyon ⑤ · 4 dosyada geçiyor). "naked blade" muaf DEĞİL —
    #    THE_DULL_EDGE'de 3 kez geçiyor ve o film zaten T1 taşıyor.
    r"\bnaked\b(?!\s+eye)":                   "TUR 3 · nötr hâli bedava: bare",
}

# Şiddetli fiil GÖVDEYE yönelmiş: "debris strikes her" [YERCEKIMI KİLİT 8].
# Aynı fiziği taşıyan nötr hâl her zaman vardır ("fragments cross the frame").
# ⚠️ Kalibrasyon ④: "his" NESNE değil İYELİKtir — "drives his boot sole
#    against the strut" karakterin KENDİ uzvudur ve şiddet değildir.
#    Aranan iki imza: ① fiil + kişi zamiri NESNE konumunda ·
#    ② fiil + (ön ek) + GÖVDE PARÇASI adı.
GOVDE_PARCASI = (r"chest|head|face|skull|throat|torso|neck|spine|ribs?|"
                 r"stomach|groin|armpit|jaw|temple|abdomen")
POLITIKA_FIIL = re.compile(
    r"\b(?:strikes?|struck|hits?|slams?|smash(?:es)?|crush(?:es)?|hurls?|rams?|"
    r"punch(?:es)?|kicks?|stabs?|drives?)\s+"
    r"(?:(?:her|him|them)\b"
    rf"|(?:\w+\s+){{0,4}}?(?:into|against|through|at)\s+(?:the|his|her|its|"
    rf"another'?s?|the\s+other'?s?)?\s*(?:\w+\s+){{0,2}}?(?:{GOVDE_PARCASI})\b)",
    re.IGNORECASE)

# Milliyet — §7'de DOĞRULANMIŞ üretim reddi ("Israeli-American", LOW POWER).
# Yüksek isabet için: sıfat, bir İNSAN adının hemen yanında olmalı.
MILLIYET_SIFAT = (r"American|Israeli|Palestinian|Russian|Ukrainian|Chinese|"
                  r"Iranian|Turkish|Syrian|Afghan|Iraqi|Korean|Japanese|German|"
                  r"French|British|English|Indian|Pakistani|Mexican|Brazilian|"
                  r"Nigerian|Egyptian|Saudi|Polish|Italian|Spanish|Canadian|"
                  r"Australian|Soviet")
MILLIYET = re.compile(
    rf"\b(?:{MILLIYET_SIFAT})[-–]\w+\b|"
    rf"\b(?:{MILLIYET_SIFAT})\s+(?:woman|man|male|female|engineer|pilot|"
    r"astronaut|commander|geologist|technician|crew|figure|scientist|"
    r"officer|soldier|worker)\b")

# Gerçek kurum/rütbe — §7 "gerçek ülke ordusu/polisi sembolü, bayrak, rütbe"
KURUM = re.compile(
    r"\b(NASA|ESA|SpaceX|Roscosmos|JAXA|ISRO|NATO|Pentagon|CIA|FBI|KGB|"
    r"U\.?S\.? (?:Army|Navy|Air Force|Marines|Space Force))\b")

# ⑯b YAPISAL RED PROFİLİ [02_RISK_KARTLARI KART 10 · Cold Burn S8]
# İnsansız sahne + uzun NEGATIVE bloğu: yokluk listesi İSTEK olarak
# okunamıyor. Aynı blok insanlı sahnede sorun çıkarmıyor — orada
# istenen bir VARLIK vardır.
INSANSIZ = re.compile(
    r"exactly\s+(?:0|zero|no)\s+human|no\s+human\s+(?:figures?|beings?)|"
    r"\bno\s+people\b|\bno\s+person\b|\bunmanned\b|no\s+figures?\s+in\s+frame",
    re.IGNORECASE)
# Bant kalibrasyonla kondu (aşağıdaki NOT'a bak); tek kaynak burasıdır.
NEGATIF_BLOK_BANDI = 900

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

# ─── D138 YÜZEY İŞARETİNE BİTİŞİK ÖLÇÜ ─────────────────────────────
# Rakamla VE yazıyla yazılmış ölçüler; ikisi de ekrana etiket olarak düştü.
OLCU_SAYISI = re.compile(
    r"\b(?:\d+(?:[.,]\d+)?|one|two|three|four|five|six|seven|eight|nine|ten|"
    r"eleven|twelve|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|"
    r"hundred)\s*(?:point\s+\w+\s+)?"
    r"(?:m|cm|mm|km|metres?|meters?|centimet(?:re|er)s?|millimet(?:re|er)s?)\b",
    re.IGNORECASE)
TEXT_YASAK_IZI = re.compile(
    r"no readable text|no letters|no lettering|no digits|no numerals", re.IGNORECASE)
# ⚠️ Kapsam kalıbı DAR tutulur: "on the ground" / "on the rock" gibi
#    sıradan düzyazı ifadeleri kapsam SAYILMAZ — yoksa her film sahte geçer.
TEXT_KAPSAM = re.compile(
    r"on any display, surface, patch or sign|on any surface|"
    r"anywhere in the frame|nowhere in the frame|no surface in frame|"
    r"nothing in the frame carries|on any surface in frame", re.IGNORECASE)

BOYUT_KELIMESI = re.compile(
    r"\s*(across|wide|in width|in diameter|thick|deep|in depth|long)\b",
    re.IGNORECASE)
# ⚠️ 04.09.2026 (TUR 9 denetimi): sözlüğe YAPI ADLARI eklendi.
#    Sebep ölçülmüş bir kör noktaydı: Ders 32 image prompta
#    "door height = 2.1m · ramp angle = 25 degrees" yazdırıyordu ve bu
#    dizge sözlükte OLMADIĞI için kapıdan 0 FIX ile geçiyordu — D138'in
#    kendi anlattığı "imza KELİMEYİ arıyordu, KAPSAMI değil" arızasının
#    tekrarı. Ders 32 aynı gün nesne-göreli birime çevrildi.
ISARET_ADI = re.compile(
    r"\b(fracture|crack|ring|circle|arc|groove|seam|joint|marking|stripe|"
    r"band|line|scar|score|furrow|scratch|etch|"
    r"hatch|hull|door|ramp|panel|truss|module|port|handrail|handhold|"
    r"window|airlock|radiator|strut|mast|antenna|berm)\b", re.IGNORECASE)

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

# ─── ⑰ B5 HİKÂYE OMURGASI KAPISI [03_PLAN_ONCESI B5 · 02.09.2026] ──
# Kaynak: 05_DIKEY_HAT_TESHISI §5① + 06_HIKAYE_HATTI_TESHISI §3.2 · §4①-②
# TEMA_SATIRI ile AYNI sertlik: satır başı + büyük harf. Sebep aynı —
# "isteksizlik", "bedeli ödendi" gibi cümle içi kullanımlar beyan değildir.
# ⚠️ KALİBRASYON 02.09.2026 · gerçek iki plan üstünde koşuldu:
#    · Satır "B5 □ İSTEK:" diye de yazılıyor → B5 ve □ ön ekleri opsiyonel.
#    · ENGEL/BEDEL/HASIM İSTEK'in devam satırında SATIR ORTASINDA geçiyor
#      ("...disk). ENGEL: yolun üstündeki kütleler") → onlarda satır başı
#      şartı yok, İKİ NOKTA şartı var. Yanlış pozitif riski düşük: depodaki
#      cümle içi kullanımlar iki nokta TAŞIMIYOR ("BEDEL GÖRÜNÜR ·",
#      "SEÇİMİN BEDELİ NESNEDİR"). İSTEK ve HASIM ise TEMA sertliğinde
#      kalır — ikisi kapının çapasıdır.
def _b5_satiri(ad, satir_basi=True):
    on = r"^[ \t>*_#·\-]*\**[ \t]*(?:B5[ \t]*)?(?:□[ \t]*)?" if satir_basi \
         else r"(?:^|[\s>*_·\-(])"
    return re.compile(on + ad + r"[ \t]*[::]", re.MULTILINE)

ISTEK_SATIRI = _b5_satiri(r"[İI]STEK")
ENGEL_SATIRI = _b5_satiri(r"ENGEL", satir_basi=False)
BEDEL_SATIRI = _b5_satiri(r"BEDEL", satir_basi=False)
MUHATAP_SATIRI = _b5_satiri(r"(?:MUHATAP|HASIM)")   # HASIM: 02.09 öncesi ad, kabul edilir
AYRILIK_SATIRI = _b5_satiri(r"AYRILIK")
B5_PENCERE = 260          # karakter · satırdan sonra içerik okunan alan

# İSTEK niteliği: film başlamasa da var olan bir İŞ olmalı. Seyir değil.
# THE THIN ROOF: kadın "bir çukura bakmaya" gelmişti → ENDS OR STOPS: Stops.
ISTEK_SEYIR = re.compile(
    r"\b(anla(?:mak|ma)|görmek|görme|fark\s*et(?:mek|me)|izlemek|bakmak|"
    r"gözlemle(?:mek|me)|keşfetmek|understand|see|observe|notice|realis|realiz|watch)\b",
    re.IGNORECASE)
# İş fiili varsa seyir bulgusu düşer: "bakmaya geldi AMA işaret dikecek".
ISTEK_IS = re.compile(
    r"\b(dik(?:mek|me)|kur(?:mak|ma)|onar(?:mak|ma)|taşı(?:mak|ma)|"
    r"getir(?:mek|me)|götür(?:mek|me)|bırak(?:mak|ma)|kurtar(?:mak|ma)|"
    r"değiş(?:tirmek|tirme)|bağla(?:mak|ma)|kapat(?:mak|ma)|aç(?:mak|ma)|"
    r"topla(?:mak|ma)|çıkar(?:mak|ma)|ödemek|teslim|yerleştir)\b",
    re.IGNORECASE)
# ✏️ 02.09.2026 · GERİ ÇEKİLEN DENETİM — kayıt: 04_ARASTIRMA_BULGULARI T4.0
#    Burada bir HASIM_ORTAM deseni vardı ve "ORTAM hasım değildir" diye FIX
#    veriyordu. Dış araştırma turu iki bağımsız raporu çapraz okudu: insan-hasım
#    ile doğa-hasım arasında izleyici tarafında BELGELENMİŞ nicel fark YOK; fark
#    çatışmanın türünden değil BEDELİN büyüklüğünden geliyor. Desen kaldırıldı.
#    Yerine gelen denetim BEDEL'in bir SAHNE numarası taşıyıp taşımadığıdır —
#    "umursamadım" tepkisinin üç belgelenmiş sebebinden ölçülebilir olan budur.
BEDEL_SAHNE = re.compile(r"\bS\d{1,2}\b")
# İki insanlı film: CHARACTER BIBLE'ın pozitif sayım cümlesi.
IKI_INSAN = re.compile(
    r"exactly\s+two\s+human|two\s+(?:figures|people|astronauts)\b|"
    r"both\s+figures\b|iki\s+(?:figür|astronot|kişi)\b", re.IGNORECASE)


# ⚠️ KURAL SATIRI PENCEREYE GİRMEZ · 02.09.2026 kalibrasyonu.
#    Planlar kapının KENDİ uyarısını da yazıyor:
#      "⛔ \"anlamak · görmek · fark etmek\" İSTEK DEĞİLDİR — …"
#    Bu satır pencerede kalırsa kapı, kuralı doğru uygulayan filmi kuralın
#    metniyle düşürür (THE LEANING ROOM'da tam olarak bu oldu). Deponun
#    D59 dersinin betik hâli: yasağın METNİ, yasağın KONUSU değildir.
B5_KURAL_SATIRI = re.compile(r"^[ \t]*[⛔⚠️✅❌]|DEĞİLDİR|DEGILDIR", re.MULTILINE)
B5_SONRAKI_MADDE = re.compile(r"^[ \t]*(?:B\d|C|D|E)[ \t]*[□·]", re.MULTILINE)


def _b5_pencere(metin, bas):
    """Beyanın kendi içeriği — kural satırları ve sonraki madde dışarıda."""
    p = metin[bas:bas + B5_PENCERE]
    kesim = B5_SONRAKI_MADDE.search(p)
    if kesim:
        p = p[:kesim.start()]
    return "\n".join(l for l in p.split("\n") if not B5_KURAL_SATIRI.search(l))


def b5_bul(yol, metin, desen):
    """B5 satırını dosyada, yoksa KLASÖR KOMŞULARINDA ara (tema_bul ile aynı
    gerekçe: satır PLAN'da yazılır, kapı bölüm dosyasında koşar)."""
    m = desen.search(metin)
    if m:
        return _b5_pencere(metin, m.end()), yol.name
    for kardes in sorted(yol.parent.glob("*.md")):
        if kardes == yol:
            continue
        try:
            k_metin = kardes.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        m = desen.search(k_metin)
        if m:
            return _b5_pencere(k_metin, m.end()), kardes.name
    return None, None

# ─── ⑭ NOVUM TAŞIYICI KAPISI [Ders 157 · 01.09.2026] ───────────────
# ONERME §4①: tek kare testi novumun KENDİ taşıyıcısıyla koşulur. Payload'da
# taşıyıcı "amortisör bandı"ydı, tek kare "dört boş kelepçe yuvası" — başka
# nesne. Kural ekrana hiç gelmedi, iki mercek onu "tekrar" sayıp kesme
# listesine yazdı. Ders 27.08-01.09 arasında hiçbir kapıda değildi ve aynı
# gün yazılan bir sonraki film onu okumadı. Kapı: taşıyıcı satırındaki nesne
# adı TEK KARE satırlarından en az birinde geçmeli.
# ⚠️ Ayraç ":" YA DA en az iki boşluk — planlar bu satırı sütun hizalı da yazıyor
#    ("NOVUM TAŞIYICISI    9 cm parlak avuç diski × …"); ilk sürüm yalnız iki
#    nokta arıyordu ve kapıyı yazan filmin kendisini "satır yok" saydı.
NOVUM_TASIYICI = re.compile(r"NOVUM\s+TA[ŞSşs]IYICI(?:SI|si)?\s*(?:[:：]|\s{2,})\s*([^\n×x→—–(]+)", re.IGNORECASE)
TEK_KARE_SATIR = re.compile(r"^.*\bTEK\s+KARE\b.*$", re.IGNORECASE | re.MULTILINE)
TASIYICI_STOP = {"the", "and", "with", "bir", "ile", "için", "olan", "olarak", "üzerinde", "cm", "mm",
                 "metre", "metrelik", "santim", "parlak", "büyük", "küçük", "uzun", "kısa", "eski",
                 "yeni", "tek", "her", "jest", "jesti", "yere", "into", "onto", "from"}

# ─── ⑮ SIRT POZİTİF YÜZEY KAPISI [Ders 139 · 01.09.2026] ────────────
# D79'un yokluk listesi ("no backpack") kamera özneyi ARKADAN gösterdiğinde
# yetmez: model boş sırtı doldurmak zorundadır ve yasak ona ne KOYACAĞINI
# söylemez (bir filmde altın sırt ünitesi doğdu, 10 s kaldı). Kamera arkada
# ya da omuz üstündeyse aynı promptta POZİTİF yüzey tarifi aranır.
KAMERA_ARKADA = re.compile(
    r"from\s+behind|behind\s+(?:her|him|them)\b|back\s+to\s+(?:the\s+)?camera|"
    r"seen\s+from\s+(?:the\s+)?(?:back|rear)|over[- ]the[- ]shoulder|\bOTS\b|rear\s+three[- ]quarter",
    re.IGNORECASE)
SIRT_POZITIF = re.compile(
    r"(?:one|a\s+single|single)\s+continuous[^.]{0,60}(?:panel|surface)|continuous\s+smooth\s+panel|"
    r"back\s+(?:of\s+(?:the|her|his|their)\s+suit\s+)?is\s+(?:one|a\s+single)[^.]{0,50}(?:panel|surface)|"
    r"flat\s+back\s+silhouette|back\s+silhouette\s+(?:is|stays)\s+flat|carrying\s+nothing",
    re.IGNORECASE)


# ─── ⑲ KİMLİK YIĞINI KAPISI [Ders 167 · 02.09.2026] ────────────────
# THE SINKING STAKE (motor OMNI) çok sahnede reddedildi:
#   "There are a lot of people I can help with, but I can't depict some
#    public figures. Do you have anyone else in mind?"
# Filmde gerçek kimse yok, özel ad yok, milliyet 0, ⑯ temiz, kapı GO'ydu.
# Tetikleyici BİÇİMDİ: tek kişide yedi kimlik özniteliği tek cümlede —
# kesin boy + gövde + ten + saç rengi + saç biçimi + yüz işareti + yaş.
# "Ünlüyü adını yazmadan tarif ederek isteme" kalıbının birebir şekli.
# ⚠️ Sınıflandırıcı niyeti değil YOĞUNLUĞU okur; eşik yoğunluktadır.
KIMLIK_OZNITELIK = {
    "kesin boy":   r"\b(?:one|two)?\s*hundred\s+\w+(?:[- ]\w+)?\s+centimet"
                   r"|\b\d{2,3}\s*cm\b|\bmetres?\s+tall\b|\b\d\.\d{2}\s*m\s+tall\b",
    "ten rengi":   r"\b(?:dark|light|pale|deep|warm|olive|brown|black|white|"
                   r"tan|freckled)[- ]?(?:brown\s+)?skin\b",
    "saç rengi":   r"\b(?:grey|gray|black|blonde?|red|red-brown|brown|white|"
                   r"silver|auburn|ginger)\s+hair\b",
    "saç biçimi":  r"\b(?:close-cropped|cropped|shaved|braided|tied|knotted|"
                   r"pulled\s+back|pressed\s+flat|shoulder-length|long|short)"
                   r"[^.]{0,20}\bhair\b",
    "yaş":         r"\b(?:mid|early|late)[- ](?:twenties|thirties|forties|"
                   r"fifties|sixties)\b|\b(?:aged\s+)?\d{2}\s+years?\s+old\b"
                   r"|\b(?:forty|fifty|sixty|thirty)[- ]\w+\b(?=,)",
    "yüz işareti": r"\b(?:scar|mole|freckles|deep\s+lines|creases|birthmark|"
                   r"stubble|beard)\b[^.]{0,30}\b(?:cheek|brow|eyes?|jaw|chin|"
                   r"temple|face)\b|\bdeep\s+lines\s+at\s+the\s+outer\s+eyes\b",
}
KIMLIK_PENCERE = 240      # karakter · tek "kişi tarifi" bölgesi sayılır
KIMLIK_ESIK = 4           # bu kadar öznitelik bir arada = tanımlama kalıbı


def kimlik_yiginlari(poz):
    """Aynı pencerede >= KIMLIK_ESIK kimlik özniteliği taşıyan bölgeler."""
    vurus = []
    for ad, kalip in KIMLIK_OZNITELIK.items():
        for m in re.finditer(kalip, poz, re.IGNORECASE):
            vurus.append((m.start(), ad))
    vurus.sort()
    yiginlar, i = [], 0
    while i < len(vurus):
        pencere = [v for v in vurus if vurus[i][0] <= v[0] < vurus[i][0] + KIMLIK_PENCERE]
        adlar = sorted({ad for _, ad in pencere})
        if len(adlar) >= KIMLIK_ESIK:
            yiginlar.append((vurus[i][0], adlar))
            i += len(pencere)
        else:
            i += 1
    return yiginlar


# ─── ⑳ ZORLANMA KANALI KAPISI [Ders 169 · 02.09.2026] ──────────────
# THE SINKING STAKE'in 25 promptunda: strain 0 · tremor 0 · heave 0 ·
# "grip tighten" 0 · braced 1 · "working breath" 2 — hepsi TEK sahnede.
# 24 sahnede fiziksel iş yapılıyor ve gövde hiçbir şey ödemiyor.
# 0,40 g AĞIRLIĞI azaltır, KÜTLE ve ATALETİ azaltmaz; giysi maliyeti de
# hiç azalmaz. Mercek ⑧ bunu "NOBODY PAYS" diye ölçer — bu kapı önce sorar.
EFOR_FIILI = re.compile(
    r"\b(?:hauls?|hauling|pulls?|pulling|drags?|dragging|lifts?|lifting|"
    r"heaves?|heaved|prises?|prised|levers?|levering)\b", re.IGNORECASE)
# ⚠️ KALİBRASYON (02.09.2026 · 6 filme koşuldu, ÜÇ yanlış-pozitif sınıfı kapatıldı):
#   ① "carries/carry" bu depoda TAŞIMAK değil SAHİP OLMAK demek — "the glove
#      carries a nine-centimetre disc", "the suit carries no patch". Çıkarıldı.
#   ② "push" kamera sözlüğüne çarpıyor: "no push-in" negatif çekirdekte. Çıkarıldı.
#   ③ "press" saça çarpıyor: "hair pressed flat under the helmet ring". Çıkarıldı.
#   ④ "wrench" COLD_WELD'de NESNEDİR (bir İngiliz anahtarı), fiil değil. Çıkarıldı.
# Kalan yedi fiil tek anlamlıdır ve hepsi bir YÜKE karşı iş tarif eder.
EFOR_PENCERE = re.compile(r"^TIMELINE:.*?(?=^[A-Z⭐][A-Z ]{2,}:|\Z)",
                          re.IGNORECASE | re.MULTILINE | re.DOTALL)
ZORLANMA_IZI = re.compile(
    r"\bforearm[^.]{0,40}\b(?:tendon|stand out|tighten|cord|strain|work)|"
    r"\b(?:grip|hands?)\b[^.]{0,40}\b(?:slips?|re-?tak|tighten|shak|tremor)|"
    r"\bleans?\s+into\b|\bshoulders?\s+(?:below|drop|low|round)|"
    r"\b(?:rear|back)\s+boot\s+loads?\b|\bknee\s+bends?\s+before\b|"
    r"\bbreaths?\s+per\b|\b(?:slower|shorter)\s+than\s+the\s+first\b|"
    r"\bworking\s+breath\b|\bagainst\s+the\s+glove'?s?\s+own\s+stiffness\b|"
    r"\bbraced?\b[^.]{0,30}\b(?:boot|leg|hip|weight)\b|"
    # 04.09.2026 · TUR 11 — GÖRÜNÜR NEFES (KARAKTER_VE_DUYGU §4.2):
    # giysinin omuz/göğüs kafesinin periyodik yükselişi de bir gövde
    # tepkisidir; kılavuz bu kalıbı emrediyordu, sözlük tanımıyordu.
    r"\b(?:chest|shoulders?)\b[^.]{0,40}\b(?:rise|rises|rising|lift|lifts|lifting)\b",
    re.IGNORECASE)



# ─── ㉑ MÜHÜR KAPISI [Ders 175 · 05.09.2026] ────────────────────────
# THE UPWARD FALL S22: 3,2 atm solunamaz atmosferde, kaskı 25/25 kapalı
# adamın ÖNKOLU bilekten yukarısı ÇIPLAK DERİ üretildi. Sekiz merceğin
# sekizi gördü, hiçbiri yazmadı.
# ⭐ MEKANİZMA: dersin kendi reçetesi arızayı üretti. D169 efor sözlüğünün
#    ÖNKOL satırı "the forearm tendons stand out THROUGH THE GLOVE" —
#    bu bir eldiven tarifi değil, bir SAYDAMLIK tarifidir. Model tendonu
#    görünür kılmak için eldiveni değil DERİYİ çizdi.
MUHUR_BAGLAM = re.compile(
    r"\b(?:sealed|pressuris|pressuriz|unbreathable|vacuum|"
    r"surface suit|pressure suit|helmet)\b", re.IGNORECASE)
# ⚠️ KALİBRASYON (05.09.2026 · üç hatta koşuldu, 720 → 12 vaka):
#   ① shoulder/arm/neck ÇIKARILDI — kadraj ve ışık cümlelerinin sabit
#      malzemesi ("the light rims his shoulders"), mühürle ilgisi yok: 411 vaka.
#   ② Kalan üç uzuv MÜHÜR SINIRIDIR: eldiven↔kol, yaka↔boyun, bot↔ayak.
#   ③ Tetik uzvun ADI değil, uzva yazılan ANATOMİ AYRINTISIDIR — D175'in
#      mekanizması tam buydu: "tendons stand out" modele DERİYİ çizdirdi.
#      Anatomi ayrıntısı olmayan uzuv adı ("his wrist turns") deri üretmez.
GOVDE_ADI = re.compile(r"\b(forearms?|wrists?|ankles?)\b", re.IGNORECASE)
ANATOMI_IZI = re.compile(
    r"\b(?:tendons?|skin|veins?|muscles?|flesh|knuckles?|pores?|hairs?|"
    r"bare|naked|freckle|scar|goose|sinew)\b", re.IGNORECASE)
ORTU_ADI = re.compile(
    r"\b(?:sleeves?|cuffs?|suits?|gloves?|gloved|seals?|sealed|"
    r"ring|collar|fabric|shell)\b", re.IGNORECASE)
# çıplak-deri negatifinin ÜÇ sınırı — biri eksikse mühür delinir
DERI_BOLGELERI = {
    "yaka":  re.compile(r"above the collar|at the collar|neck seal", re.IGNORECASE),
    "bilek": re.compile(r"at the wrist|wrist seal|between glove and sleeve", re.IGNORECASE),
    "bilek_ayak": re.compile(r"at the ankle|ankle seal|boot cuff", re.IGNORECASE),
}
SAYDAMLIK_TUZAGI = re.compile(
    r"\bthrough the (?:glove|sleeve|suit|shell|fabric)\b", re.IGNORECASE)


# ─── ㉒ YÜZEY RENK KAPISI [Ders 176 · 05.09.2026] ───────────────────
# THE UPWARD FALL: WORLD bloğu zemini renksiz bıraktı, LIGHTING bloğu
# "the PALE GREY FLOOR" dedi. Model ilk yarıda birine, ikinci yarıda
# ötekine sadık kaldı — film ortasında biyom değişti. Kusur 25 promptun
# 25'indeydi ve üç mercek bunu SAHNE kusuru sanıp S20/S21'i kesmeyi önerdi.
# ⭐ Kontrast garantisi yüzeyin RENGİNİ değil, ÖZNENİN OKUNURLUĞUNU söyler.
YUZEY_ADI = re.compile(r"\b(floor|ground|wall|walls|sky|hull|ceiling)\b", re.IGNORECASE)
# ⚠️ KALİBRASYON (05.09.2026): "aynı yüzey iki renk taşıyorsa BLOCK" kuralı
#   D176'NIN KENDİ VAKASINI KAÇIRIYOR — orada renk cümlesi TEKTİ (WORLD
#   zemini renksiz bıraktı, LIGHTING "PALE GREY FLOOR" dedi). Yakalanabilir
#   olan asıl kural BLOK YETKİSİDİR: yüzeyin rengi ENVIRONMENT/WORLD'ün
#   işidir; LIGHTING bloğu ışığı tarif eder, yüzeye RENK ATAMAZ.
#   Ayrıca renk çatışmasında DEĞER kelimeleri (dark/pale/bright) sayılmaz —
#   bir duvar hem "pale grey" hem gölgede "dark" olabilir; çatışma HUE ister.
ISIK_BLOGU = re.compile(r"^(?:LIGHTING|LIGHT|ISIK|IŞIK)\s*:.*?(?=^[A-Z⭐][A-Z ]{2,}:|\Z)",
                        re.IGNORECASE | re.MULTILINE | re.DOTALL)
DEGER_KELIMESI = {"pale", "dark", "bright", "light", "deep"}
BIYOM_YUZEYI = re.compile(r"\b(floor|ground|walls?)\b", re.IGNORECASE)
RENK_SIFATI = re.compile(
    r"\b(black|white|grey|gray|brown|red|blue|green|amber|ochre|rust|"
    r"pale|dark|bright|charcoal|slate|ash|sand|copper|golden|silver|"
    r"olive|violet|crimson|umber|beige|ivory|tan)\b", re.IGNORECASE)


# ─── ⑳b DEĞİŞİM KAPISI [Ders 179 · 05.09.2026] ─────────────────────
# THE HEALING GROUND: sahnenin VIDEO promptu değişimi doğru yazdı
# (0.0s "a short white vapour plume stands at his hip" → 2.0s "the plume
# thins, drops and goes out"). Aynı sahnenin İMAJ promptu ise
# "There is no vapour plume at his hip" diyordu — yani değişimin
# SONRASINI. I2V hattında imaj t=0'dır: modelden başlangıç karesinde
# BULUNMAYAN bir tüyü söndürmesi istendi. Göğüs kapağı hiç açılmadı,
# bedel hiç ekrana gelmedi, film "kamera taşıyıcı" olarak okundu.
IMAJ_YOKLUK = re.compile(
    r"\bthere is no ([a-z][a-z \-]{2,28}?)\b|"
    r"\bno ([a-z][a-z \-]{2,28}?) (?:at|on|under|around) (?:his|her|their|the)\b",
    re.IGNORECASE)
# ⚠️ KALİBRASYON (05.09.2026): kapı AYRIK NESNE arar. Soyut adlar
#   ("no fill light" · "the ground" · "the surface") sönen bir şey değildir
#   ve 26 ateşlemenin 9'unu üretiyordu.
SOYUT_AD = {"fill", "light", "ground", "surface", "shadow", "sound", "air",
            "wind", "motion", "movement", "colour", "color", "detail", "texture",
            "background", "foreground", "space", "area", "edge", "line"}
SONME_FIILI = re.compile(
    r"\b(?:goes? out|go out|went out|thins?|dies?|fades?|drops? and|"
    r"stops?|closes?|shuts?|seals?|empties|drains?|clears?)\b", re.IGNORECASE)

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


# ─── SAYI NORMALİZASYONU (yalnız kurulum imzası için) ──────────────
# ⛔ 05.09.2026 · ÖLÇÜLMÜŞ ARIZA. Depo mesafeyi/yüksekliği İKİ biçimde
#    yazıyor: "3 metres away" ve "three meters away". YUKSEKLIK/MESAFE
#    desenleri yalnız RAKAM tanıyor, yazıyla yazılanı görmüyor. Sonuç:
#    THE SECOND SHIP FAZ_03'te dört metreden ve üç metreden çekilmiş iki
#    sahne "aynı kurulum" göründü ve BLOCK yedi; FAZ_07'de sabit bir plan
#    ile bir push-in aynı sayıldı. İmza karşılaştırmadan önce sayılar
#    rakama çevrilir — "two and a half metres" ile "2.5 m" aynı yerdir
#    [ACI_YAYI §7 ⑥: dönüş ancak geometri BİREBİR aynıysa dönüştür].
_SAYI_BIRIM = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
    "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100,
}
_SAYI_KELIME = "|".join(sorted(_SAYI_BIRIM, key=len, reverse=True))
_SAYI_OBEGI = re.compile(
    rf"\b(?:{_SAYI_KELIME})(?:[-\s]+(?:point|{_SAYI_KELIME}))*"
    rf"(?:\s+and\s+a\s+half)?\b", re.IGNORECASE)


def _obek_degeri(s):
    """"twenty-five" → 25 · "one point two" → 1.2 · "two and a half" → 2.5"""
    yarim = bool(re.search(r"\s+and\s+a\s+half$", s, re.IGNORECASE))
    s = re.sub(r"\s+and\s+a\s+half$", "", s, flags=re.IGNORECASE)
    parcalar = re.split(r"\s+point\s+", s, maxsplit=1, flags=re.IGNORECASE)

    def topla(bolum):
        toplam = 0
        for kelime in re.split(r"[-\s]+", bolum.strip().lower()):
            if kelime not in _SAYI_BIRIM:
                return None
            deger = _SAYI_BIRIM[kelime]
            toplam = toplam * deger if deger == 100 and toplam else toplam + deger
        return toplam

    tam = topla(parcalar[0])
    if tam is None:
        return None
    if len(parcalar) == 2:                       # ondalık: "one point two"
        kesir = topla(parcalar[1])
        if kesir is None:
            return None
        return float(f"{tam}.{kesir}")
    return tam + 0.5 if yarim else tam


def sayilari_rakama(metin):
    """Yazıyla yazılmış sayıları rakama çevir (imza karşılaştırması için)."""
    def degistir(m):
        v = _obek_degeri(m.group(0))
        return m.group(0) if v is None else f"{v:g}"
    return _SAYI_OBEGI.sub(degistir, metin)


def geometri_cumleleri(cumleler):
    """Kamera GEOMETRİSİNİ taşıyan cümleler (lens · yükseklik · mesafe).

    ⛔ 05.09.2026 · ÖLÇÜLMÜŞ ARIZA. `kamera_cumleleri` pozitif gövdedeki
    kamera kelimesi geçen HER cümleyi döndürüyor — aksiyon cümleleri dahil.
    Aksiyon metnindeki bir kamera ifadesi imzaya AÇI TİPİ olarak sızıyor ve
    özdeş iki kurulumu ikiye bölüyordu:
      THE THIN ROOF S0 ↔ S5 — geometri BİREBİR aynı (32mm · 0.35 m · 9.0 m,
      prompt ayrıca "the same position, height and lens as Scene 0" diyor),
      ama S5'in aksiyon satırındaki "side on to the lens" imzaya "profil"
      ekledi ve iki sahne İKİ KURULUM sayıldı. Filmin gerçek kurulum sayısı
      3'tü, betik 5 ölçtü.
    ⚠️ Bu daraltma YALNIZ İMZA içindir. ⑪ açı SÖZLÜĞÜ denetimi geniş kümeyi
      kullanmaya devam eder: orada aranan şey "açı kelimesi yazılmış mı",
      hangi cümlede yazıldığı önemli değil.
    """
    g = [c for c in cumleler
         if LENS_MM.search(c) or YUKSEKLIK.search(c) or MESAFE.search(c)]
    return g or cumleler


def kurulum_imzasi(cumleler):
    """Kurulum = açı + ölçek + kamera konumu (ACI_YAYI §4 tanımı).

    Sahneye özel kelimeler ("from the woman" ↔ "from the lander") imzaya
    girmez; yalnız SAYILABİLİR geometri girer. Böylece aynı kurulumun iki
    farklı cümleyle yazılması çeşitlilik sanılmaz.
    """
    cumleler = [sayilari_rakama(c) for c in cumleler]
    t = " ".join(cumleler)
    # ⚠️ ÖLÇEK de geometri cümlelerinden okunur (05.09.2026). Tam metinden
    #    okununca aksiyon satırındaki ölçek kelimesi imzaya giriyordu:
    #    THIN ROOF S3'ün "its gas bubbles ... readable close up" cümlesi
    #    imzaya CU ekledi ve S1 ile özdeş olması gereken kurulumu ayırdı.
    g = " ".join(geometri_cumleleri(cumleler))
    olcek = next((ad for ad, k in OLCEK_MERDIVENI if re.search(k, g, re.IGNORECASE)),
                 None)
    return (_ilk(LENS_MM, t), _ilk(YUKSEKLIK, t), _ilk(MESAFE, t),
            olcek, frozenset(aci_tipleri(geometri_cumleleri(cumleler))))


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


# ─── KURULUM İSKELETİ [ACI_YAYI §3 🕰️ · §4b · 05.09.2026] ──────────
# ⛔ TETİK — SAHİP KARARI 05.09.2026: küme ve dönüş kapıları YALNIZ
#    iskeletini BEYAN EDEN dosyada koşar. Gerekçe: kural yeni, eski 119
#    dosya onunla yazılmadı; hepsine uygulamak 118 FIX demekti ve sahip
#    "eskiler dokunulmadan kalsın" dedi. Yeni filmler alanı FILM_PLAN /
#    FILM_QA_SPEC şablonundan alır → kapı kendiliğinden açılır.
# ⚠️ Tetik SETUP SEQUENCE DEĞİL: o alan bugün 32 dosyada var ve hiçbiri
#    küme kuralıyla yazılmadı. Ayrı bir satır olması, kapının yalnız
#    yeni sözleşmeyi kabul etmiş dosyalarda koşmasını garanti eder.
ISKELET_SATIRI = re.compile(
    r"^[^\S\n]*(?:[⬜✅🔁]\s*)?KURULUM\s+İSKELET[İI]\s*:(.*)$", re.MULTILINE)


def iskelet_bul(yol, metin):
    """KURULUM İSKELETİ harflerini dosyada, yoksa klasör komşularında ara."""
    adaylar = [(yol.name, metin)]
    for kardes in sorted(yol.parent.glob("*.md")):
        if kardes == yol:
            continue
        try:
            adaylar.append((kardes.name,
                            kardes.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            continue
    for ad, k_metin in adaylar:
        m = ISKELET_SATIRI.search(k_metin)
        if m:
            harfler = re.findall(r"\b([A-Z])\b", m.group(1))
            if harfler:
                return harfler, ad
    return None, None


# ⭐ DÖNÜŞ İŞARETİ (ACI_YAYI §7 ⑥): dönen sahne geometriyi birebir
#    kopyalar ve bu satırı taşır. Küme klibi AYRICA devam cümlesini
#    (DEVAM_KLIBI) taşır — ikisi farklı iş yapar, §3 🕰️.
DONUS_ISARETI = re.compile(
    r"same\s+position,?\s+height\s+and\s+lens\s+as\s+scene|"
    r"same\s+(?:position|setup|camera|framing)\b[^.;]{0,60}\bas\s+scene\s+\d+",
    re.IGNORECASE)


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


def negatif_govde(govde):
    """NEGATIVE bloğunun KENDİSİ. Boşsa "".

    ⑯'nın varlık sebebi: `pozitif_govde` yasağın içini KORUR (D85), ama
    politika ekseninde korunması gereken şey tam tersidir — sınıflandırıcı
    yasak bloğunu da okur [D123]. Bu iki fonksiyon aynı ayrımı iki zıt
    amaçla kullanır ve ikisi de doğrudur.
    """
    parca = re.split(r"^NEGATIVE:", govde, maxsplit=1, flags=re.MULTILINE)
    return parca[1] if len(parca) > 1 else ""


def politika_say(metin, sozluk):
    """Sözlükteki her deseni say. → {desen: (adet, kaynak, ilk_eşleşme)}"""
    bulunan = {}
    for desen, kaynak in sozluk.items():
        eslesmeler = re.findall(desen, metin, re.IGNORECASE)
        if eslesmeler:
            ilk = re.search(desen, metin, re.IGNORECASE).group(0)
            bulunan[desen] = (len(eslesmeler), kaynak, ilk)
    return bulunan


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

    # ⑤b YÜZEY İŞARETİNE BİTİŞİK ÖLÇÜ [Ders 138 · 28.08.2026]
    # Kadrajdaki bir YÜZEY İŞARETİNE (çatlak, halka, çizgi, oluk, iz)
    # bitişik yazılan ölçü, model tarafından o işaretin ÜSTÜNE BASILAN BİR
    # ETİKET olarak çizilebiliyor: bir filmin S2 promptu halkayı iki kez
    # "eleven point six metres across" diye tarif etti ve ekranda halkanın
    # iç yayına "11 metres" + gradasyon çentikleri yazıldı. Diyagram,
    # teknik çizim ve arazi ölçüm fotoğrafı eğitim verisinde tam olarak
    # böyle görünür. Ölçü SPEC'in kilit listesinde durur; prompt gövdesi
    # nesneyi NESNE GÖRELİ ölçekle anlatır ("four body-lengths across").
    # ⚠️ Boy/mesafe ölçüleri (1.68 metres tall) bu denetime GİRMEZ —
    #    aranan, ölçünün bir YÜZEY İŞARETİ adıyla aynı pencerede olması.
    if p["tip"] == "image":
        for m in OLCU_SAYISI.finditer(govde_d):
            # ① ölçüden SONRA bir BOYUT kelimesi olmalı (across/wide/…);
            #    yoksa bu bir mesafe ya da boy ölçüsüdür, etiket riski yok.
            if not BOYUT_KELIMESI.match(govde_d[m.end():m.end() + 25]):
                continue
            # ② işaret adı, ölçüyle AYNI CÜMLEDE ve ÖNCESİNDE olmalı.
            #    Cümle sınırı geriye doğru tarama penceresini kapatır —
            #    "…fine dark lines. Her shadow is 2.83 metres long" bu
            #    yüzden bulgu DEĞİLDİR.
            bas = max(0, m.start() - 60)
            geri = govde_d[bas:m.start()]
            kesik = max(geri.rfind("."), geri.rfind("!"), geri.rfind("?"))
            if kesik != -1:
                geri = geri[kesik + 1:]
            isaret = ISARET_ADI.search(geri)
            if isaret:
                cevre = govde_d[bas:m.end() + 45].replace("\n", " ").strip()
                bulgular.append(Bulgu(
                    "FIX",
                    f"yüzey işaretine bitişik ölçü: \"{isaret.group(0)}\" → \"{m.group(0).strip()}\"",
                    f"...{cevre}... · [D138] ölçüyü SPEC'e taşı, gövdede "
                    f"nesne göreli ölçek yaz (\"four body-lengths across\")."))

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

    # ⑯ POLİTİKA SÖZLÜĞÜ [Ders 123 · 01.09.2026]
    # ⛔ ②'nin tersi: burada NEGATIVE bloğu MUAF DEĞİL, ağırlıklıdır.
    neg = duzles(negatif_govde(govde))
    t1_poz, t1_neg = politika_say(poz_d, POLITIKA_T1), politika_say(neg, POLITIKA_T1)
    t2_poz, t2_neg = politika_say(poz_d, POLITIKA_T2), politika_say(neg, POLITIKA_T2)

    def _ozet(d):
        return " ".join(f"{v[2].strip()}×{v[0]}" for v in
                        sorted(d.values(), key=lambda x: -x[0]))

    t1_top = sum(v[0] for v in t1_poz.values()) + sum(v[0] for v in t1_neg.values())
    t2_top = sum(v[0] for v in t2_poz.values()) + sum(v[0] for v in t2_neg.values())

    if t1_top:
        nerede = []
        if t1_neg:
            nerede.append(f"NEGATIVE bloğunda: {_ozet(t1_neg)}")
        if t1_poz:
            nerede.append(f"pozitif gövdede: {_ozet(t1_poz)}")
        seviye = "FIX" if POLITIKA_BANDI_KARARA_BAGLI or t1_top < 3 else "BLOCK"
        bulgular.append(Bulgu(
            seviye, f"politika sözlüğü T1 · {t1_top} tetikleyici",
            " · ".join(nerede) + " · [D123] sınıflandırıcı \"no\" önekini "
            "okumaz. Yasağı SİL, yerine malzemeyi TARİF et "
            "(POLITIKA_VE_URETILEBILIRLIK_KILAVUZU §2)."))

    if t2_top >= 5:
        nerede = []
        if t2_neg:
            nerede.append(f"NEGATIVE: {_ozet(t2_neg)}")
        if t2_poz:
            nerede.append(f"pozitif: {_ozet(t2_poz)}")
        bulgular.append(Bulgu(
            "FIX", f"politika sözlüğü T2 · {t2_top} tetikleyici (yoğunluk)",
            " · ".join(nerede) + " · tek geçiş normaldir, yığılma değil. "
            "Sınıflandırıcı promptu BÜTÜN olarak okur [D123]."))

    for m in POLITIKA_FIIL.finditer(govde_d):
        cevre = govde_d[max(0, m.start() - 45):m.end() + 30].strip()
        bulgular.append(Bulgu(
            "FIX", f"gövdeye yönelmiş şiddet fiili: \"{m.group(0).strip()}\"",
            f"...{cevre}... · [YERCEKIMI KİLİT 8] aynı fiziği taşıyan nötr "
            "hâl yaz: \"fragments cross the frame\" · \"at hip height\"."))

    for m in MILLIYET.finditer(govde_d):
        bulgular.append(Bulgu(
            "BLOCK", f"milliyet ifadesi: \"{m.group(0).strip()}\"",
            "§7'de DOĞRULANMIŞ üretim reddi (LOW POWER · \"Israeli-American\"). "
            "Yalnız fiziksel tanım yazılır."))

    for m in KURUM.finditer(govde_d):
        bulgular.append(Bulgu(
            "FIX", f"gerçek kurum adı: \"{m.group(0).strip()}\"",
            "§7: gerçek ülke ordusu/kurumu/rütbesi yazılmaz — hem politika "
            "yüzeyi hem D34 jenerik halüsinasyonu. (Milliyetin aksine bu "
            "kural bu depoda ÖLÇÜLMEDİ → FIX, BLOCK değil.)"))

    # ⑯b YAPISAL RED PROFİLİ [KART 10 · Cold Burn S8]
    if p["tip"] == "video" and not p["yedek"] and INSANSIZ.search(govde_d) \
            and len(neg) >= NEGATIF_BLOK_BANDI:
        bulgular.append(Bulgu(
            "FIX", f"yapısal red profili: insansız sahne + {len(neg)} karakter "
                   f"NEGATIVE bloğu (bant {NEGATIF_BLOK_BANDI})",
            "[KART 10 · Cold Burn S8] yokluk listesi İSTEK olarak okunamıyor. "
            "§7 çözüm sırası: NEGATIVE'i tek pozitif Style satırına indir, "
            "boş kadrajı VARLIK olarak tarif et."))

    # ─── ⑲ KİMLİK YIĞINI KAPISI [Ders 167 · 02.09.2026] ───────────
    # Tek pencerede >= 4 kişi özniteliği = "ünlüyü adını yazmadan tarif
    # ederek isteme" kalıbı. THE SINKING STAKE bu biçimle reddedildi
    # (motor OMNI, red defteri 15) — ⑯ temizdi, kapı GO vermişti.
    for _, adlar in kimlik_yiginlari(poz_d):
        bulgular.append(Bulgu(
            "FIX", f"kimlik yığını: {len(adlar)} kişi özniteliği bir arada "
                   f"({' · '.join(adlar)})",
            "Bir ünlüyü adını yazmadan TARİF EDEREK isteme kalıbıdır ve kişi "
            "sınıflandırıcısını tetikler [D167 · red defteri 15, OMNI]. Yığın "
            "PLAN'da ve referans paketinde yaşar; prompta yalnız SİLUET iner. "
            "Boy göreli yazılır ('a head taller'), yüz tarifi yalnız yüzün "
            "KONU olduğu sahnede kalır."))

    # ─── ⑳ ZORLANMA KANALI KAPISI [Ders 169 · 02.09.2026] ─────────
    if p["tip"] == "video":
        # ⛔ YALNIZ TIMELINE BLOĞU: efor bir OLAYDIR, kamera satırında ya da
        #    negatif blokta geçen fiil iş değildir (kalibrasyon ②).
        m_tl = EFOR_PENCERE.search(pk_govde := pozitif_govde(p["govde"]))
        tl = duzles(m_tl.group(0)) if m_tl else ""
        if tl and EFOR_FIILI.search(tl) and not ZORLANMA_IZI.search(pk_govde):
            bulgular.append(Bulgu(
                "NOT", "efor fiili TIMELINE'da var, gövde tepkisi yok",
                "Çekme/kaldırma/sürükleme yazılmış ama önkol · kavrama · gövde "
                "eğimi · bacak yüklenmesi · nefes kadansı kanallarının hiçbiri "
                "yok. Düşük yerçekimi AĞIRLIĞI azaltır, KÜTLE ve ATALETİ "
                "azaltmaz [D169]. Sayı yazılır, sıfat değil: 'the fourth pull "
                "is slower than the first' ölçülebilir, 'he strains' değil. "
                "⚠️ Bu satır GÖZLEMDİR, üretim durdurmaz: zorlanma sözlüğü "
                "ölçülene kadar bant yok (⑯ ve image bandı emsali)."))

    # ─── ㉒ YÜZEY RENK KAPISI [Ders 176 · 05.09.2026] ──────────────
    # Aynı yüzey iki ayrı yerde İKİ AYRI renk taşıyorsa model ikisine de
    # sadık kalır: ilk yarıda birine, ikinci yarıda ötekine.
    poz_yr = duzles(pozitif_govde(p["govde"]))
    m_isik = ISIK_BLOGU.search(p["govde"])
    if m_isik:
        isik = duzles(m_isik.group(0))
        # ⚠️ KALİBRASYON (05.09.2026): sky · hull · ceiling ÇIKARILDI —
        #   gökyüzü zaten bir IŞIK KAYNAĞIDIR, gövdeye vuran ışığın rengiyle
        #   tarif edilmesi meşrudur (52 yanlış-pozitif). Kalanlar BİYOMU
        #   TANIMLAYAN düzlemdir: D176'nın kırdığı yüzey tam olarak `floor`du.
        for m in BIYOM_YUZEYI.finditer(isik):
            pen = isik[max(0, m.start() - 45): m.end() + 25]
            hue = [r.group(1).lower() for r in RENK_SIFATI.finditer(pen)
                   if r.group(1).lower() not in DEGER_KELIMESI]
            if hue:
                bulgular.append(Bulgu(
                    "BLOCK", f"IŞIK bloğu yüzeye renk atıyor: {m.group(1)} = {'/'.join(sorted(set(hue)))}",
                    "Yüzeyin rengi ENVIRONMENT/WORLD'ün işidir; IŞIK bloğu "
                    "ışığı tarif eder [D176]. İki blok aynı yüzeyi tarif "
                    "edince model ilk yarıda birine, ikinci yarıda ötekine "
                    "sadık kalır ve film ortasında dünya değişir. Kontrast "
                    "garantisini renk vermeden yaz: 'reads as a clean dark "
                    "silhouette against the floor'."))
                break
    # ⛔ İKİNCİ ALT-DENETİM SİLİNDİ (05.09.2026, kalibrasyonda düştü):
    #   "aynı yüzey iki ayrı HUE taşıyorsa BLOCK" denendi ve üç hatta ~180 kez
    #   ateşledi; ezici çoğunluğu MEŞRU (gövdenin bir yanı amber, gölgede siyah;
    #   gökyüzü uzun promptta birkaç renkle tarif edilir). Kaldı ki D176'nın
    #   mekanizması bu DEĞİLDİ — orada renk cümlesi TEKTİ, sorun yazıldığı BLOKTU.
    #   Ölçüm geçmeyen denetim kapıya girmez [00_DERS_YAZIM_KONTRATI §2].

    # ─── ㉑ MÜHÜR KAPISI [Ders 175 · 05.09.2026] ───────────────────
    if MUHUR_BAGLAM.search(p["govde"]):
        if SAYDAMLIK_TUZAGI.search(poz_yr):
            bulgular.append(Bulgu(
                "FIX", "saydamlık tuzağı: 'through the glove' mühürü deler",
                "Bu bir eldiven tarifi değil, bir SAYDAMLIK tarifidir; model "
                "tendonu görünür kılmak için eldiveni değil DERİYİ çizer "
                "[D175 · THE UPWARD FALL S22, önkol bilekten yukarısı çıplak]. "
                "Yerine gövde tepkisini ÖRTÜNÜN ÜSTÜNDE yaz: 'the glove's "
                "fabric draws tight over the tendons'."))
        for c in re.split(r"(?<=[.;])\s+", poz_yr):
            m = GOVDE_ADI.search(c)
            if not m:
                continue
            kelimeler = c.split()
            idx = len(c[:m.start()].split())
            pencere = " ".join(kelimeler[max(0, idx - 12): idx + 12])
            if not ANATOMI_IZI.search(pencere):
                continue                      # uzuv adı var ama deri riski yok
            if not ORTU_ADI.search(pencere):
                bulgular.append(Bulgu(
                    "FIX", f"mühürlü filmde örtüsüz gövde adı: '{m.group(1)}'",
                    "Solunamaz atmosferde geçen filmde bir uzuv adı, ±12 kelime "
                    "içinde bir ÖRTÜ adı (sleeve · cuff · suit · glove · seal) "
                    "olmadan yazılmaz — yoksa model uzvu çıplak çizer [D175]. "
                    f"Cümle: “{c[:90]}…”"))
                break
        neg_yr = p["govde"][len(pozitif_govde(p["govde"])):]
        if re.search(r"\b(?:bare|exposed|uncovered)\s+skin\b", neg_yr, re.IGNORECASE):
            var = [ad for ad, kalip in DERI_BOLGELERI.items() if kalip.search(neg_yr)]
            if len(var) < 3:
                eksik = [ad for ad in DERI_BOLGELERI if ad not in var]
                bulgular.append(Bulgu(
                    "BLOCK", f"çıplak-deri negatifi {len(var)}/3 bölge yazıyor",
                    "Mühür ÜÇ SINIRDA birden delinir; tek bölge yazan negatif "
                    "yalnız yakanın üstünü kapatır ve önkol açıkta kalır "
                    f"[D175]. Eksik bölge(ler): {', '.join(eksik)}. Üçü de "
                    "yazılır: 'above the collar' + 'at the wrist' + 'at the ankle'."))

    return bulgular


# Şablon ve kılavuz dosyaları film değildir: içlerindeki "prompt" blokları
# yer tutucu ve TALİMAT taşır ("ANTI-GLOW: 'glowing' KULLANMA") — denetime
# sokulursa kendi yasak listesini ihlal sayarlar.
#
# 08.09.2026 · `00_ANALIZ` eklendi. Film klasörü artık yazımdan ÖNCEKİ işi
# taşıyan bir alt klasörle geliyor (okuma çizelgesi · QA hasadı · sahne
# sıralaması · uyarı notları · sahne sahne çalışma) ve o dosyalar TASLAK
# metin taşır. İki somut arıza kapatıldı:
#   ① `klasorleri_bul` ağaçtaki her klasöre bakar; 05_SAHNE_CALISMALARI'na
#      iki sahne başlığı düşse o klasör AYRI BİR FİLM sayılırdı.
#   ② `rglob("*.md")` her analiz dosyasını tek tek denetime sokar; sahne
#      çalışmasına yazılan taslak prompt kendi yasak listesini ihlal eder.
# D117'nin kalıbı: "plandaki örnek bir prompt sahne dizisine karışır."
# Desen eklenirken ölçüldü: mevcut hiçbir dosyayı FAZLADAN atlamıyor (0).
ATLA = re.compile(r"/kilavuzlar/|SABLON|ŞABLON|TEMPLATE|00_ANALIZ", re.IGNORECASE)


def sahneli_dosyalar(klasor):
    """Klasörde DOĞRUDAN duran, sahne başlığı taşıyan .md dosyaları."""
    bulunan = []
    for f in sorted(klasor.glob("*.md")):
        if FILM_DISI.search(f.name) or ATLA.search(str(f)):
            continue
        try:
            if SAHNE_BASLIK.search(f.read_text(encoding="utf-8", errors="replace")):
                bulunan.append(f)
        except OSError:
            continue
    return bulunan


def bolunmus_film(yol):
    """Bu dosya, sahneleri BAŞKA dosyalara da yayılmış bir filmin parçası mı?"""
    return yol.is_file() and len(sahneli_dosyalar(yol.parent)) >= 2


def dosya_denetle(yol):
    if ATLA.search(str(yol)):
        return None
    return metin_denetle(yol, yol.read_text(encoding="utf-8", errors="replace"))


def metin_denetle(yol, metin, promptlar=None):
    """Bir METİN gövdesini denetler. `yol` yalnız ad ve komşu araması içindir.

    01.09.2026'da `dosya_denetle`den ayrıldı. Sebep: film artık klasöre
    bölünüyor (PLAN + BOLUM_1 + BOLUM_2 + …) ve DİZİ kapıları dosya
    sınırında KÖRLEŞİYOR — gövde tek satır değişmedi, yalnız girdisi
    dosyadan metne çevrildi. Birleştirilmiş koşu: klasor_denetle().
    """
    if promptlar is None:
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

    # METİN YASAĞININ KAPSAMI [Ders 138 · 28.08.2026] — DOSYA BAŞINA TEK SATIR
    # "metin yasağı" imzası KELİMEYİ arıyor, KAPSAMI değil: depodaki her
    # filmin metin yasağı bir GİYSİ ya da GÖVDE listesidir ("no patch, no
    # flag, no lettering, no digits and no symbol anywhere"). O cümle
    # kostümü korur; zemini, kayayı, gökyüzünü korumaz. Bir filmde model
    # kaldırımdaki çatlağın iç yayına "11 metres" + gradasyon çentikleri
    # yazdı ve altı QA merceğinin altısı görmedi.
    # ⚠️ Bulgu DOSYA BAŞINA BİR KEZ yazılır: her prompta bir satır yazan
    #    kilit, kilit değil duvardır (AGENTS §8).
    if TEXT_YASAK_IZI.search(tum_prompt) and not TEXT_KAPSAM.search(tum_prompt):
        sonuc["dosya_bulgulari"].append(Bulgu(
            "FIX", "metin yasağı KAPSAMSIZ — yalnız kostümü/gövdeyi koruyor",
            "[D138] KILAVUZ_REHBERI §5'in kapsam biçimini kullan: "
            "\"No readable text, letters, digits, numbers or symbols on any "
            "display, surface, patch or sign\" — zemin ve kaya da kadrajdadır."))

    # A1 — yasak ↔ anlatım çelişkisi (en pahalı hata)
    if A1_YASAK.search(tum_prompt):
        icerik = A1_ICERIK.search(poz_tum)
        if icerik:
            cevre = poz_tum[max(0, icerik.start() - 40):icerik.end() + 20].replace("\n", " ")
            sonuc["dosya_bulgulari"].append(Bulgu(
                "BLOCK", "A1 ÇELİŞKİSİ — metin yasağı ile ekran içeriği aynı dosyada",
                f"...{cevre.strip()}... · Tidal Hunt: sayaç ekrana hiç çıkmadı (D50)"))

    # Scene N of X — iddia edilen sahne sayısı dosyayla tutuyor mu
    # ⚠️ BÖLÜNMÜŞ FİLMDE DOSYA MODUNDA KOŞMAZ [01.09.2026]: BOLUM_1'de 3 sahne
    #    başlığı vardır ama promptlar DOĞRU biçimde "Scene 1 of 6" der. Bu kapı
    #    o filmde parçanın tamamını gören KLASÖR MODUNDA koşar; dosya modunda
    #    koşarsa her bölünmüş filme iki uydurma FIX yazar ve gerçek bulguyu
    #    gürültüye gömer. Aynı DOSYA içindeki çelişki (iddialar > 1) her hâlde
    #    ölçülür — o, parçalanmadan bağımsızdır.
    sahne_sayisi = len(SAHNE_BASLIK.findall(metin))
    iddialar = {int(x) for _, x in SCENE_N_OF_X.findall(tum_prompt)}
    if len(iddialar) > 1:
        sonuc["dosya_bulgulari"].append(Bulgu(
            "FIX", f"\"Scene N of X\" tutarsız — dosyada {sorted(iddialar)} birden geçiyor"))
    elif bolunmus_film(yol):
        pass
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
                "⛔ Vizör tasarım gereği renkli/aynalıysa bu bulgu DÜŞER. "
                "⭐ 01.09.2026 [TUR 3]: vizör şeffaflığı artık YALNIZ devamlılık "
                "kilidi değil, ÜRETİLEBİLİRLİK kilidi — yüzü kapatan ekipman "
                "anonimlik/deepfake imzasına yakın okunuyor "
                "(POLİTİKA §3 imza ⑥). Açık vizör red riskini de düşürür."))

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

        # ④ KURULUM İSKELETİ — KÜME · DÖNÜŞ · BİREBİR YAZIM
        #    [ACI_YAYI §3 🕰️ · §4b · §7 ⑥ · sahip kararı 05.09.2026]
        # Teşhis: depoda 1.406 sahne / 1.287 kesme vardı ve kesmelerin
        # neredeyse tamamı YENİ bir bakış noktasına geçiyordu. Üç kapı
        # çeşitliliğe itiyordu (⑩① BLOCK · ⑩② az kurulum · ⑪ açı tipi),
        # dönüşe iten SIFIR kapı vardı — üst bant "NOT"tu, 87 uzun dosyanın
        # 63'ü onu aşıyordu ve hiçbiri durmuyordu. Bu blok o boşluğu kapatır.
        iskelet, i_kaynak = iskelet_bul(yol, metin)
        if iskelet and len(iskelet) != n:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", f"KURULUM İSKELETİ {len(iskelet)} harf ↔ dosyada {n} "
                       f"video promptu ({i_kaynak})",
                "İskelet sahne sahne okunur; harf sayısı sahne sayısına EŞİT "
                "olmalı. Eşit değilse hangi sahnenin hangi kuruluma döndüğü "
                "ölçülemez ve küme/dönüş kapıları kör kalır [ACI_YAYI §4b]."))
        elif iskelet:
            # küme = ardışık aynı harf öbeği (≥2 klip)
            kumeler, i = [], 1
            while i < n:
                if iskelet[i] == iskelet[i - 1]:
                    bas = i - 1
                    while i < n and iskelet[i] == iskelet[bas]:
                        i += 1
                    kumeler.append((bas, i - 1))
                else:
                    i += 1
            kume_klipleri = {j for bas, son in kumeler
                             for j in range(bas + 1, son + 1)}
            # DÖNÜŞ = kaynağından EN ÇOK 3 sahne sonra gelen tekrar (§3).
            # Daha uzağı YENİDEN TANITIMDIR: izleyicinin kısa süreli görsel
            # belleği o kadar beklemez, kurulum yeni gibi okunur.
            donusler = [j for j in range(1, n)
                        if iskelet[j] in iskelet[max(0, j - 4):j]]

            if n >= 12:
                # ⛔ 6-11 sahne ve dikey shorts MUAF (§4b): kısa formatta iki
                #    küme filmin üçte ikisini iki kuruluma bağlar, §4 alt bandı
                #    ile çakışır.
                if len(kumeler) < 2:
                    sonuc["dosya_bulgulari"].append(Bulgu(
                        "FIX", f"KÜME {len(kumeler)} — {n} sahnede en az 2 olmalı "
                               f"(ACI_YAYI §4b)",
                        "Küme = tek vuruş sürerken ardışık 2-3 klibin AYNI "
                        "kurulumda kalması; sahne sayısını ve süreyi değiştirmez, "
                        "yalnız kesme sayısını düşürür. Kümesiz film hiç "
                        "DİNLENMEZ — depoda 1.287 kesmenin tamamı yeni bakış "
                        "noktasına geçiyordu. İskelet: " + " ".join(iskelet)))
                oran = len(donusler) / n
                if oran < 0.40:
                    sonuc["dosya_bulgulari"].append(Bulgu(
                        "FIX", f"DÖNÜŞ oranı %{oran * 100:.0f} — {n} sahnede en az "
                               f"%40 olmalı ({len(donusler)}/{n}, hedef "
                               f"{-(-n * 2 // 5)}) [ACI_YAYI §4b]",
                        "Sıçrama kalkanı verir, DÖNÜŞ haritayı verir. Dönüş = "
                        "kaynağından en çok 3 sahne sonra gelen tekrar; daha "
                        "uzağı yeniden tanıtımdır ve sayılmaz. Üst banda uymak "
                        "yetmez: A B C D E F A B C D E F 12 sahnede 6 kurulum "
                        "kullanır, tavana uygundur ve dönüş oranı %0'dır. "
                        "İskelet: " + " ".join(iskelet)))

            for bas, son in kumeler:
                if son - bas + 1 > 3:
                    sonuc["dosya_bulgulari"].append(Bulgu(
                        "FIX", f"KÜME {son - bas + 1} klip uzunluğunda "
                               f"({bas + 1}-{son + 1}. video promptu) — tavan 3",
                        "3 klipten (~30 s) uzun küme güvenlik kamerası hissine "
                        "döner [ACI_YAYI §3 🕰️ · §4 alt bandıyla aynı gerekçe]."))

            # ⭐ İŞARET, bilinçli beklemeyi monotonluktan ayıran TEK şeydir.
            isaretsiz = [j for j in sorted(kume_klipleri)
                         if not DEVAM_KLIBI.search(video[j]["govde"])]
            if isaretsiz:
                sonuc["dosya_bulgulari"].append(Bulgu(
                    "BLOCK", f"küme klibinde DEVAM işareti yok: "
                             + ", ".join(f"satır {video[j]['satir']}"
                                         for j in isaretsiz[:4]),
                    "Küme bir kesme değil BÖLÜNMÜŞ TEK ÇEKİMDİR. İşaretsiz iki "
                    "benzer klip yan yana konursa §3'ün kalkanı TERSİNE döner: "
                    "mikro farklar tam kesme anında görünür (jump cut). Şart: "
                    "\"continues the previous clip from its exact last frame — "
                    "the same position, height and lens as Scene N.\""))

            isaretsiz_donus = [j for j in donusler if j not in kume_klipleri
                               and not DONUS_ISARETI.search(video[j]["govde"])]
            if isaretsiz_donus:
                sonuc["dosya_bulgulari"].append(Bulgu(
                    "FIX", f"dönüş işareti yok ({len(isaretsiz_donus)} sahne): "
                           + ", ".join(f"satır {video[j]['satir']}"
                                       for j in isaretsiz_donus[:4]),
                    "Model SPEC'teki harf iskeletini GÖRMEZ, yalnız metni görür "
                    "[ACI_YAYI §7 ⑥]. Dönen sahne kamera geometrisini birebir "
                    "kopyalar ve sonuna şunu ekler: \"— the same position, "
                    "height and lens as Scene N.\""))

            # ⑥ BİREBİR YAZIM: aynı harf → aynı ölçülen imza olmak ZORUNDA.
            #    Uymuyorsa ikisinden biri yanlıştır: ya metin kaymıştır
            #    (§7 ⑥ ihlali) ya iskelet harfi yanlış konmuştur. İkisinin de
            #    çözümü aynı: geometriyi kaynak sahneden KOPYALA.
            harf_sahne = {}
            for j, h in enumerate(iskelet):
                harf_sahne.setdefault(h, []).append(j)
            for h, idx in sorted(harf_sahne.items()):
                imzalar = {kurulumlar[j] for j in idx}
                if len(imzalar) > 1:
                    ornek = sorted(idx)[:3]
                    sonuc["dosya_bulgulari"].append(Bulgu(
                        "FIX", f"iskelet '{h}' {len(idx)} sahnede ama "
                               f"{len(imzalar)} farklı kurulum ölçüldü",
                        " ⇄ ".join(f"satır {video[j]['satir']}: "
                                   f"{kurulum_ozet(kurulumlar[j])}"
                                   for j in ornek)
                        + " · Aynı harf aynı kurulumdur; geometri kelimesi "
                          "kelimesine kopyalanır (aynı sayı biçimiyle: \"2.5 m\" "
                          "hep \"2.5 m\", bir yerde rakam bir yerde yazı olmaz) "
                          "[ACI_YAYI §7 ⑥]."))

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

    # ─── ⑰ B5 HİKÂYE OMURGASI KAPISI [03_PLAN_ONCESI B5 · 02.09.2026] ──
    # 06_HIKAYE_HATTI_TESHISI §3.2: engel parkuru gerilim üretir, hikâye
    # üretmez. Fizik kuralı hiçbir şey İSTEMEZ — istemeyen bir engel bir
    # engeldir, bir hasım değildir.
    if not FILM_DISI.search(yol.name) and sahne_sayisi >= 6:
        i_metin, i_kaynak = b5_bul(yol, metin, ISTEK_SATIRI)
        b_metin, b_kaynak = b5_bul(yol, metin, BEDEL_SATIRI)
        eksik = [ad for ad, d in (("İSTEK", ISTEK_SATIRI), ("ENGEL", ENGEL_SATIRI),
                                  ("BEDEL", BEDEL_SATIRI), ("MUHATAP", MUHATAP_SATIRI))
                 if b5_bul(yol, metin, d)[0] is None]
        if eksik:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "BLOCK", f"B5 satırı yok: {' · '.join(eksik)}",
                "03_PLAN_ONCESI B5 — İSTEK (film başlamasa da var olan bir iş) · "
                "ENGEL (bunu ne engelliyor) · BEDEL (alırsa ne kaybediyor + SAHNE no) · "
                "MUHATAP (eylemin yankısı nerede görünüyor: ikinci insan / kendi geçmiş "
                "kararı / kendi bedeni / ortamın kalıcı değişen parçası). "
                "⚠️ Bu kapı 02.09.2026'da açıldı; ondan önceki dosyaların çoğu "
                "BLOCK verir — depo ölçümü: İSTEK 8/79 · ENGEL 2/79 "
                "(06_HIKAYE_HATTI_TESHISI §1.1)."))
        if i_metin and ISTEK_SEYIR.search(i_metin) and not ISTEK_IS.search(i_metin):
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", f"İSTEK bir SEYİR gibi yazılmış ({i_kaynak})",
                "\"anlamak\" · \"görmek\" · \"fark etmek\" İSTEK DEĞİLDİR [05 §5①]. "
                "İstek, film başlamasa da var olan bir iştir. THE THIN ROOF: kadın "
                "\"bir çukura bakmaya\" gelmişti → ④ merceği ENDS OR STOPS: Stops yazdı."))
        if b_metin and not BEDEL_SAHNE.search(b_metin):
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", f"BEDEL satırı SAHNE numarası taşımıyor ({b_kaynak})",
                "Kaybın GÖRÜLDÜĞÜ sahne yazılmazsa bedel bir cümledir, bir olay değil "
                "(B2 ile çapraz oku). İzleyici tarafında ölçülmüş olan budur: "
                "\"umursamadım\" tepkisinin üç sebebinden biri bedelin yokluğu, "
                "\"güzel ama boş\" şikâyeti ise insanî bedelin görsele yenildiği "
                "filmlerde çıkıyor [04_ARASTIRMA_BULGULARI TUR 4]."))
        if IKI_INSAN.search(metin) and b5_bul(yol, metin, AYRILIK_SATIRI)[0] is None:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", "iki insanlı film ama AYRILIK sahnesi yazılmamış",
                "İki figürün AYNI FİKİRDE OLMADIĞI sahne (jest · duraklama · yön · "
                "temas reddi) plana yazılır; ikisi de aynı anda aynı şeyi yapıyorsa "
                "kadroda iki gövde vardır, tek kişi. THE SINKING STAKE 25 sahne "
                "boyunca iki insanı yan yana tuttu, merkezî seçimi \"biri onaylar, "
                "öteki karar verir\" oldu (06_HIKAYE_HATTI_TESHISI §1.5)."))

    # ─── ⑭ NOVUM TAŞIYICI KAPISI [Ders 157] ───────────────────────
    # Yalnız film dosyaları (fragman/kapak muaf) ve 6+ sahne.
    if not FILM_DISI.search(yol.name) and sahne_sayisi >= 6:
        m_t = NOVUM_TASIYICI.search(metin)
        if m_t:
            nesne = m_t.group(1).strip()
            kelimeler = [w for w in re.findall(r"[a-zçğıöşü]{4,}", nesne.lower()) if w not in TASIYICI_STOP]
            # ⚠️ Plan nesri ~72 sütunda SARILIR (duzles() ile aynı sebep): "…7,0 s
            #    karesi: mat karanlık\nbir avuç ve…" — nesne alt satıra düşer. Satır
            #    + izleyen iki satır tek parça okunur; ilk sürüm kapıyı yazan filmi
            #    bu yüzden düşürdü.
            satirlar = metin.split("\n")
            tek_kare = [" ".join(satirlar[i:i + 3]) for i, s in enumerate(satirlar)
                        if TEK_KARE_SATIR.search(s) and not NOVUM_TASIYICI.search(s)]
            if kelimeler and tek_kare:
                if not any(w in s.lower() for w in kelimeler for s in tek_kare):
                    sonuc["dosya_bulgulari"].append(Bulgu(
                        "FIX", f"novum taşıyıcısı TEK KARE testinde geçmiyor: \"{nesne[:60]}\" [D157]",
                        "ONERME §4①'e yazılan kare §2'nin taşıyıcı nesnesini İÇERMEK zorunda; başka "
                        "nesneyle geçilen kapı geçilmemiş kapıdır. Payload: taşıyıcı bant, tek kare "
                        "kelepçe yuvası → kural ekrana gelmedi, iki mercek kesme listesine yazdı."))
            elif kelimeler and not tek_kare:
                sonuc["dosya_bulgulari"].append(Bulgu(
                    "FIX", "NOVUM TAŞIYICISI yazılmış ama TEK KARE satırı yok (ONERME §4①) [D157]"))
        else:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "NOT", "NOVUM TAŞIYICISI satırı yok (ONERME §2 · 22.08.2026 sonrası filmlerde zorunlu)",
                "Eski dosyalarda gözlemdir; yeni filmde <nesne> × <jest> → <ihlal> satırı plana yazılır."))

    # ─── ⑮ SIRT POZİTİF YÜZEY KAPISI [Ders 139] ───────────────────
    # ⚠️ Bulgu DOSYA BAŞINA TEK SATIR (kalibrasyon 01.09.2026: prompt başına yazınca
    #    80 dosyada satır yağmuru — kilit değil duvar, AGENTS §8). Karar değişmez.
    if KASK_IZI.search(metin) and not FILM_DISI.search(yol.name):
        arkada = []
        for p in promptlar:
            if p["yedek"]:
                continue
            kam = " ".join(kamera_cumleleri(p["govde"]))
            if KAMERA_ARKADA.search(kam) and not SIRT_POZITIF.search(duzles(p["govde"])):
                arkada.append(str(p["satir"]))
        if arkada:
            sonuc["dosya_bulgulari"].append(Bulgu(
                "FIX", f"{len(arkada)} promptta kamera ARKADA/omuz üstünde, sırt için POZİTİF yüzey "
                       f"tarifi yok [D139] (satır {', '.join(arkada[:8])}{'…' if len(arkada) > 8 else ''})",
                "\"the back of the suit is one continuous smooth panel from collar to hip, "
                "carrying nothing\" — yokluk listesi arkadan çekimde tutmaz; model boş sırtı "
                "doldurur (altın sırt ünitesi, 10 s)."))


    # ─── ⑳b DEĞİŞİM KAPISI [Ders 179 · 05.09.2026] ─────────────────
    # I2V hattında İMAJ t=0'dır. İmaj promptu değişimin SONRASINI yazarsa
    # modelden, başlangıç karesinde BULUNMAYAN bir şeyi söndürmesi istenir —
    # THE HEALING GROUND'da göğüs kapağı hiç açılmadı, tüy kalçada değil
    # zemindeki diskte çıktı, filmin BEDELİ hiç ekrana gelmedi.
    # Eşleme: bir imaj promptu ile ONU İZLEYEN ilk video promptu aynı sahnedir.
    for idx, ip in enumerate(promptlar or []):
        if ip["tip"] != "image":
            continue
        vp = next((q for q in (promptlar or [])[idx + 1:] if q["tip"] == "video"), None)
        if not vp:
            continue
        v_govde = duzles(pozitif_govde(vp["govde"]))
        i_govde = duzles(pozitif_govde(ip["govde"]))
        for m in IMAJ_YOKLUK.finditer(i_govde):
            nesne = (m.group(1) or m.group(2) or "").strip()
            if len(nesne) < 4:
                continue
            cekirdek = nesne.split()[-1]                 # 'vapour plume' → 'plume'
            if cekirdek.lower() in SOYUT_AD:
                continue
            if len(cekirdek) < 4 or cekirdek not in v_govde:
                continue
            pen_i = v_govde.find(cekirdek)
            if SONME_FIILI.search(v_govde[pen_i: pen_i + 220]):
                sonuc["dosya_bulgulari"].append(Bulgu(
                    "BLOCK", f"imaj promptu değişimin SONRASINI yazıyor: '{nesne}'",
                    f"Video promptu '{cekirdek}' nesnesinin SÖNDÜĞÜNÜ tarif "
                    f"ediyor; imaj promptu ise onu BAŞTAN YOK sayıyor. I2V'de "
                    "imaj t=0'dır: başlangıç karesinde bulunmayan bir şey "
                    "söndürülemez, model onu BAŞKA BİR YERE koyup söndürür "
                    "[D179 · THE HEALING GROUND]. İmaj promptu değişimin "
                    f"ÖNCESİNİ yazar; sönme video TIMELINE'ının işidir. "
                    f"(imaj promptu satır {ip['satir']})"))
                break

    return sonuc


# ─── KLASÖR MODU [01.09.2026] ──────────────────────────────────────
# NEDEN VAR: film klasöre bölününce (PLAN + BOLUM_1 + BOLUM_2 + KAPAK +
# MUZIK + YAYIN_PAKETI) bu betiğin DOSYA SEVİYESİ kapılarının üçü sessizce
# kapanıyor — üçü de dosya sınırını göremediği için:
#
#   · AÇI VE KURULUM KAPISI  eşiği `len(video) >= 4`. 6 sahnelik dikey film
#     ikiye bölününce dosya başına 3 video promptu kalır → kapı HİÇ koşmaz.
#   · BÖLÜM SINIRINDAKİ ARDIŞIK ÇİFT (S2↔S3 · 3-5 dk'da S13↔S14) hiçbir
#     dosyada yan yana gelmez → "aynı kurulum" denetimi o çiftte kördür.
#   · ⑭ NOVUM TAŞIYICI  satırı PLAN'da, TEK KARE satırı da PLAN'da; bölüm
#     dosyasında ikisi de yok → kapı "satır yok" der. Bu depoda ZATEN oluyor:
#     THE_BLUE_DRIFT (PART_A/PART_B) iki dosyada da "NOVUM TAŞIYICISI satırı
#     yok" aldı, oysa satır PLAN'da yazılıydı.
#
# Bu mod klasördeki bölüm dosyalarını SAHNE SIRASINA göre birleştirip aynı
# denetimleri film boyunca bir kez daha koşar. Prompt seviyesi bulgular
# dosya modunda zaten yazıldığı için burada TEMİZLENİR — aynı bulgu iki kez
# raporlanmaz (AGENTS §8: "kilit değil duvar" olmasın).
#
# ⚠️ DÜRÜST SINIR: birleştirme klasörün DOĞRUDAN altındaki .md'leri kapsar.
#    7-9 ve 10-20 dk formatının FAZ ALT KLASÖRLERİ birleşmez (THE_SECOND_SHIP:
#    faz başına tek dosya × 10 sahne). O formatlarda dosya modu zaten tam
#    koşuyor; kör kalan tek yer FAZ SINIRINDAKİ ardışık çifttir. Format dizini
#    (dikey_shorts_filmler gibi) bilerek birleştirilmez — 18 filmi tek film
#    saymak ölçüm değil gürültü üretir.
def ilk_sahne(metin):
    """Dosyadaki en küçük sahne numarası — birleştirme sırası budur."""
    nolar = [int(n) for n in re.findall(r"^##\s+.*\bSAHNE\s+(\d+)", metin,
                                        re.IGNORECASE | re.MULTILINE)]
    return min(nolar) if nolar else -1


def klasor_denetle(klasor):
    """Bir FİLM klasörünü tek gövde gibi denetler. Film değilse None."""
    # Bölüm dosyası tek ise film zaten tek gövdedir; dosya modu tamdır.
    if len(sahneli_dosyalar(klasor)) < 2:
        return None
    # Sahnesiz dosyalar (PLAN · REFERANS) da gövdeye girer: TEMA, ⑭ NOVUM ve
    # TEK KARE satırları orada durur ve bölüm dosyasında hiç yoktur.
    dosyalar = [f for f in sorted(klasor.glob("*.md"))
                if not ATLA.search(str(f)) and not FILM_DISI.search(f.name)]

    parcalar, promptlar, sahneli = [], [], 0
    for f in sorted(dosyalar, key=lambda p: (ilk_sahne(
            p.read_text(encoding="utf-8", errors="replace")), p.name)):
        metin = f.read_text(encoding="utf-8", errors="replace")
        parcalar.append(metin)
        if SAHNE_BASLIK.search(metin):
            sahneli += 1
            # Satır numarası DOSYASIYLA birlikte taşınır: birleşik koşuda
            # çıplak "satır 990" hiçbir dosyada bulunamaz, operatör aramayı
            # bırakır ve bulgu ölür.
            kisa = f.stem.replace(klasor.name + "_", "") or f.stem
            for p in promptlari_cikar(metin):
                p["satir"] = f"{kisa}:{p['satir']}"
                promptlar.append(p)
    if not promptlar:
        return None

    sonuc = metin_denetle(klasor, "\n\n".join(parcalar), promptlar)
    if not sonuc:
        return None
    sonuc["klasor"] = True
    sonuc["parca"] = sahneli
    for p in sonuc["promptlar"]:
        p["bulgular"] = []
    return sonuc


def klasorleri_bul(kok):
    """Ağaçta doğrudan ≥2 sahneli .md taşıyan her klasör bir film adayıdır."""
    adaylar = [kok] + [d for d in sorted(kok.rglob("*")) if d.is_dir()]
    return [d for d in adaylar
            if not ATLA.search(str(d)) and len(sahneli_dosyalar(d)) >= 2]


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
    if sonuc.get("klasor"):
        print(f"   📁 FİLM KLASÖRÜ · {sonuc['parca']} bölüm dosyası birleşik · "
              "yalnız DİZİ ve DOSYA seviyesi kapıları")
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

    hedefler, klasorler = [], []
    for a in argv:
        y = Path(a)
        if y.is_dir():
            hedefler += sorted(y.rglob("*.md"))
            klasorler += klasorleri_bul(y)
        elif y.is_file():
            hedefler.append(y)
            # Tek dosya verildiyse de filmin KLASÖRÜ birleşik koşulur —
            # bölünmüş filmde tek bölüme bakmak dizi kapılarını kör bırakır.
            klasorler += klasorleri_bul(y.parent)
        else:
            print(f"⚠️  bulunamadı: {a}")

    sonuclar = []
    for y in hedefler:
        s = dosya_denetle(y)
        if s:
            sonuclar.append(s)
    for k in dict.fromkeys(klasorler):
        s = klasor_denetle(k)
        if s:
            sonuclar.append(s)

    if not sonuclar:
        print("Prompt bloğu olan dosya bulunamadı.")
        print("Aranan başlık: '### 📸 IMAGE/GÖRSEL PROMPT' · '### 🎥 VIDEO/VİDEO PROMPT'")
        return 1

    for s in sonuclar:
        yazdir(s)

    kararlar = [karar(s) for s in sonuclar]
    n_klasor = sum(1 for s in sonuclar if s.get("klasor"))
    print(f"\n{'═' * 67}")
    print(f"  TOPLAM {len(sonuclar) - n_klasor} dosya"
          + (f" + {n_klasor} film klasörü (birleşik)" if n_klasor else "") + " · "
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
