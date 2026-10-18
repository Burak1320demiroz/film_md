# F4 · ses-tasarimcisi · tur 2 — MOONMOTHER

> Tur 1'in (`ODA/F4_ses-tasarimcisi_1.md`) yerine geçen tam sürümdür; tur 1 silinmez. Yerleşim: §1 sahne tablosu, §2 ORTAM satırı, §6 ORTAM YATAĞI ve §7 GEÇİŞ `FILM.md` §6'ya taşınır; §3-§5 ve §8-§11 `ODA/`'da kalır.
> Girdi: tur 1 · `F4_besteci_1.md` (karşı plan) · `F4_kurgucu_1.md` (B1-B20) · `F4_hakem_1.md` (Fable kararı) · `FILM.md` §4 güncel (C16 ve C20 sahip kararı 17.10.2026) · `NOTLAR.md` KARARLAR · `REPLIK_VE_KLIP_SESI_KILAVUZU.md` · `GECIS_VE_SES_SUREKLILIGI.md`.
> Hakem ilkesi: saat çatışmasında **ses saati esastır**; müzik yalnız tepkisini kaydırır. Bu dosyadaki saatler ses saatleridir; besteci tur 2 bunlara göre kurulur (§8b).
> Saniyeler çekim içidir (0-10) ve **nominaldir**: `FILM.md` §4 vuruş planından alındı. **Mutlak film saati = 10 × (Cxx − 1) + saniye.**
> F8'de seçilen denemenin gerçek adım ve ışık anlarına ±0.3 s kaydırılır; ışık-nota eşleşmeleri (C02 C05 C17 C18 C20 C23) ±0.1 s'de kapanır.
> Seviye ölçeği: **0 dB = C22 dalga darbesinin tepesi**. Yataklar ve müzik LUFS ile yazılır (kural 8). İki ölçek aynı sayı doğrusu değildir:
> yatağın altında kalan her efekt satırı yatağın üstünde duyulacak bantta (1-4 kHz) tutulur; F8'de kulakla doğrulanır. Mutlak seviye (−14 LUFS) son aşamada `kurgu.py yukseklik` ile kurulur.
> S<n> = plan C<n> = `FILM.md` Cxx. Bu filmde telsiz, kask ve vakum yoktur: telsiz filtresi, replik yerleşimi ve kask içi kuralları uygulanmaz.
> Katman tanımı (tur 2'de netleştirildi): **K1** ortam yatağı · **K2** efekt (foley, su, taş, temas, Khev'in nefesi) · **K3** çağrı + Khev klikleri (kasıtlı canlı sinyal; replik yerine) · **K4** müzik.

## 0. KARAR ÖZETİ

```
MODEL SESİ     KAPALI (NOTLAR KARARLAR 16.10.2026). Gemini/Omni klibinin kendi sesi gelir ama kurguda atılır (timeline klip_sesi: false, varsayılan).
               F5 video promptlarına ses satırı da ortak ses kuyruğu da yazılmaz. Bütün ses (ortam, efekt, çağrı, müzik) bu planla kurguda kurulur.
               Planın 24 "Sound:" satırı §4-§5'e taşındı (§11 eşleme). Tur 2'de tek düşen satır: C16 "acılı kitin kliği" (sahip kararı 17.10.2026:
               C16'da doğrulma ve çökme yok, acının sebebi görüntüde kalmadı).
REPLİK         YOK. KAYIT LİSTESİ (§3) sözsüz canlı seslerin listesidir: Oru ve Anne çağrısı + Khev kliği. Hepsi tek kaynaktan. 28 aktif satır (R19 düştü).
ORTAM FİZİĞİ   Açık, nefes alınabilir, SES TAŞIYAN atmosfer (gece, deniz kıyısı). Vakum yok, kask yok, iç hacim yok; C24 de bulut tepelerinin üstünde ama atmosferin
               içinde. Rüzgâr, sörf, sprey, taş takırtısı DUYULUR: görüntü bunları gösteriyor, sessiz dalga görüntüyle çelişirdi.
               "İnce atmosfer boğukluğu" uygulanmaz (çağrılar camsı ve tizdir). Ölçek kuralı: büyük şey = alçak perde + yavaş atak + uzun bırakış.
KATMAN         K1 ortam yatağı · K2 efekt · K3 çağrı (+ Khev klikleri) · K4 müzik. Sahne başına ≤4, hepsi §1 tablosunda.
ÇAĞRI KODU     1) ÜÇ NOTA = ÜÇ IŞIK. Çağrı yalnız ışık yanarken (C20'de: ışık parlarken) notalıdır; ışık önce, nota 0.05-0.1 s sonra. Işık sönükse nota yok:
                  C03 (üç ışık sönük) → tek ton · C16 (ışık sönük) → nota yok, tarama süpürmesi. C01'de ışıklar silüet ölçeğinde görünmez ama Oru'nun notaları duyulur.
               2) TEK KAYNAK. ORU_CAGRI_v1 bir kez üretilir; bütün Oru ve Anne çağrıları ondan işlenir, yeniden üretilmez.
               3) PERDE (hakem B3, tek sözleşme): **D–E–A**. Oru D5 · E5 · A5 (587.3 · 659.3 · 880.0 Hz). Anne iki oktav aşağıda D3 · E3 · A3 (146.8 · 164.8 · 220.0 Hz).
                  Hissedilen alt perde (C20-C21 cevabı) D2 · E2 · A2 (73.4 · 82.4 · 110.0 Hz). Kanonik ritim: nota başları 0 / 0.9 / 1.8 s, üçüncü nota tutulur.
                  D–E–A = Dsus2 duygusu (sus2/add9): çözülmemiş ama sert değil; müziğin D add9 akoru (D F♯ A E) E'yi içerir, çağrı ile çarpışmaz.
                  Besteci başka tonalite seçerse çağrı kaydı tek hamlede ≤3 st kaydırılır (formant sabit). Besteci D'yi seçti: kaydırma yok.
               4) IŞIĞA OTURMA. Işıklı çekimlerde nota başları o denemenin ışık başlarına oturur (nota nota yerleşim: oru_n1/n2/n3.wav); aralık değişse de SIRA ve ORAN
                  (kısa · kısa · uzun) korunur. Işıksız ya da silüet çekimlerde bütün cümle (oru_cagri_tam.wav) kanonik aralıkla yerleşir.
               5) AKRABALIK SESLE OKUNUR (F3 açık ÖLÜMCÜL). C05'te anne SOĞUK: yalnız tek harmonikler, −25 cent düşük, boş salon yankısı.
                  C06'da SICAK: tam harmonikler, tam perde, aynı nota başları, iki oktav aşağıda üst üste: iki ses TEK SES gibi tınlar. Soğuk → sıcak = tanıma.
                  Bu ikisi MÜZİKSİZ duyulur (40.0-58.0, hakem B1).
               6) CEVAP GECİKMESİ güveni taşır: C17→C18 arasında 9.2 s aranma (tonsuz dikkat) · C20'de örtüşme (anne beklemeden cevap verir). Bkz. §3c.
KHEV SESİ      Klik + solungaç nefesi (kuru, kâğıtsı, insan olmayan). İnsan nefesi, iç çekişi, sesi yok. Plan: "tense inhaling click · clicking cry · pained chitin click".
SÖRF SAATİ     Su = film saati (FILM §1 ENGEL "Saat"). Sörf seviyesi çekim çekim yükselir (§5b). İstisna C19: yüzgeç altında su DÜZLEŞİR, sörf −16'dan −28'e iner:
               "hızla gelen kütle sırt doğurur, alçalan kütle doğurmaz" kuralı kulakla da okunur. Sörf düzensizdir; periyodik darbe yok.
NABIZ KURALI   (hakem B2, ses:465'in yeni hâli) Müzikte düzenli nabız İKİ ROLDE ve yalnız orada: (1) deniz saati 66.0-96.0 (tehlike; 96.0'da kuyruksuz durur) ·
               (2) anne kalp atışı 202.6-226.5 (güven; dalga anında 212.5-217.6 P ≤ −9 dB). 156.0 ve 161.0 nabız çıpaları kalktı. Yatakta ve sörfte periyot yok;
               nabız müziğe aittir, ayrı bir saat gibi duyulur.
SERT KESMELER  Yalnız planlı: C13→C14 (0.25 s yatak-tek boşluk, iniş C14 0.0) · C10 7.0-8.6 (kırılma ve düşüş, müzik vuruşu yok) · C22 3.1-3.35 kükreme çöker · film sonu.
İLK 30 S       C01 0.0'da kapak gıcırtısıyla başlar (sorun duyuluyor); insan sesi yok (insan yok); müzik C01-C02'de yok, C03 2.0'da (22.0) çok alçak girer; C01→C02'de yatak sürer.
```

## 0b. KURGUCU BULGULARINA CEVAP (B1-B20) VE HAKEM KARARI

Hakem kararı (`F4_hakem_1.md`) bağlayıcıdır; "ses" ya da "ses + besteci" satırları bu dosyada uygulandı. Besteci satırları §8-§8c'de ses kısıtı olarak yazıldı. Tur 2'de RED yok; ses saatinin hakem metnindeki sayıdan farklı çıktığı dört yerde (B6 B9 B15 ve B11 yedeği) kabul sayıya değil ilkeye verildi, fark açık yazıldı.

| Bulgu | Hakem | Cevap | Bu dosyada | Ses tarafından not |
|:--:|---|:--:|---|---|
| B1 | 40.0-58.0 müziksiz; M ilk kez 58.0'dan sonra, ≤ −12 dB (cam 58.0, çello 59.2) | **KABUL** | §0 ÇAĞRI KODU 5 · §1 S5-S6 K4 · §8 MÜZİKSİZ | Akrabalığın sesli kanıtı (C05 soğuk ↔ C06 sıcak) müziksiz. 56.8-58.0 boşluk temiz kalır; 58.0'dan sonra M rüzgâr-deniz üstünde ve ≤ −12 dB. F8 ANLATIM sesli iki sürüm ölçer (§10 madde 1). |
| B2 | Nabız iki rolde: 66.0-96.0 + anne kalp atışı 202.6'dan; 156.0 ve 161.0 kalkar; S10/S11 K4 "96.0'da durur" | **KABUL** | §0 NABIZ KURALI · §1 S10 S11 S16 S17 S21-S23 · §8c | ses:465 kuralı yeniden yazıldı. S11'deki "6.6'da kırılır" düştü. Anne kalp atışı bandı (≈100-130 Hz) anne alçak cevabının (73-110 Hz) bitişinden sonra, 202.6'da girer (§8b R24). |
| B3 | Tek perde sözleşmesi D–E–A; çağrının 2. notası G → E | **KABUL** | §0 ÇAĞRI KODU 3 · §3 R01-R29 · §3 KAYIT NOTLARI · §4 · §10 AÇIK KARAR 1 | ORU_CAGRI_v1 henüz üretilmedi: üretim promptu ve ANNE zinciri E ile yazıldı. Perde ölçümü 587.3 · 659.3 · 880.0 Hz. "sus4" → "sus2/add9". |
| B4 | Prompt bant satırı: 500-4000 Hz açık; cam 1.2 kHz üstü ve seyrek | **KABUL** (besteci uygular) | §8c BANT | Oru temelleri 587-880 Hz, anne 147-220 Hz (+ 2.-4. harmonik, 900 Hz'e dek). Ses tarafı bant ayrımını bu iki aralıkla verir. |
| B5 | C12: L1 tek D (A yok), pencerelerde ≤ −30 LUFS-S ya da yok; R13 (119.15) besteci tablosuna | **KABUL** | §1 S12 · §8 · §8b R12 R13 | Pencereler 111.0-113.0 ve 119.0-121.0, hakem ile aynı. C12'nin tamamında (110.0-121.0) L1 yalnız tek D, ≤ −30 LUFS-S. D3'ün 4. harmoniği (587.3 Hz) Oru'nun N1'iyle (D5) aynı çizgide: pencerelerde tercih "yok". |
| B6 | Tek D 138.0 → ≈140.0; R17 penceresinde −9 dB; A girişi R18 tarama bitişinden sonra (≥156.5) | **KABUL** (pencere sonu ses saatine çevrildi) | §1 S14-S16 · §8 · §8b R16 R17 R18 | R17 pencere sonu 143.0 → **144.0** (üçüncü nota 143.0'da başlıyor, tutuşu 143.8'e dek sürüyor). R18 saati yeni C16'dan 153.3-155.7; 1 s cevapsız boşluk 156.7'ye dek; **A ≥ 157.0**. R18 penceresinde (153.0-156.7) D yok ya da ≤ −9 dB. |
| B7 | Yeni C16 ve C20: S16 satırları (E09·E26, E25, R19, E19) düşer; R18 baş dönüşüne saatli; C20 sarma satırı (≈ −24); ışık parlaması 8-10 s | **KABUL** | §3 R18 R19 R23 R24 · §4 E35 · §5 C16 C20 C21 · §1 S16 S20 S21 | R19 düştü (numara korundu). C20 sarma için yeni varlık E35. R23/R24 saatleri ışık parlamasına göre yeniden hesaplandı: R23 198.2/198.9/199.6; R24 C21 0.1'de başlar (§3c). |
| B8 | F♯ 178.0 → ≈179.4; 182.0 yükselişi ≥1.5 s sonra | **KABUL** | §1 S18-S19 · §8 · §8b R22 | Anne cevabı 176.8/178.0/179.2 değişmedi. F♯ 179.4'te N3 (A3) üstüne oturur; çağrı penceresinde tek müzik olayı. −9 dB'de duyulmazsa F8 kulak ölçüsü −6'ya çıkar (§10 madde 10). |
| B9 | P 198.5 → 202.6; M BÜTÜN 199.5 → ≈203.5; anne alçak cevabı penceresinde D add9 ≤ −9 dB | **KABUL** (pencere yeniden hesaplandı) | §1 S20-S21 · §8b R23 R24 · §8 | Hakemin 199.0-200.8 penceresi tur 1'in eski R24 saatiydi. Yeni C20 ışık saatleriyle pencere **198.2-203.0**: R23 198.2-200.6, R24 200.1-202.7, DEV kuyruğu 203.0'a dek. P 202.6 anne N3 tutuşunun bitişine (202.7) denk gelir; N3 sonu 202.7'yi aşarsa P N3 sonu + 0.1. Sarma (195.0-198.0) için ayrıca D add9 −6 dB. |
| B10 | Tek çözülme 217.6; 212.5-217.6 A sus ≤ −9 dB ya da yok; dalga anında P ≤ −9 dB | **KABUL** | §1 S22 · §5 C22 · §8 | Çözülme R26'nın (216.6) kurduğu D'nin üstüne iner. 213.1-213.8'de P vuruşu yok. Kükreme zarfı 217.0'da −14, 217.6'da ≈−17: çözülme maskelenmez. |
| B11 | C24: L2 ve yüksek yaylı 233.0 → ≈237.2; 238.8-239.8 şafak parıltısını L2 cam notası taşır (E27 düşer) | **KABUL** (E27'ye koşullu yedek) | §5 C24 · §8 · §10 madde 11 | E27 ana satırdan çıktı. Yedek: L2 cam notası 238.4-239.2 aralığında duyulmuyorsa E27 −28'de geri gelir (Flow Music çıktısı bu hassasiyette garanti değil, besteci:206). Oru A5 (R29) 236.0-237.2; müzik girişi onun bitişinde. |
| B12 | Bitiş: ikinci çözülme 238.0 (A → D); son akor 239.85'e dek söner; "240'a taşan kuyruk yok" | **KABUL** | §5 C24 · §6 geçiş · §8 | Ses yatağı ve çağrı kuyruğu zaten 239.85'e dek doğal (Y2 son 1 s −40'a). 238.0'da çözülme anne N3'ünün (A3, 235.0-239.0) ortak notası üstünde: çarpışma yok. ses:463'ün "C23 5.2 D bağı" beklentisi düştü. |
| B13 | L1 girişi 22.0 | **KABUL** | §8 MÜZİKSİZ | Tur 1'deki ses isteği aynen kaldı: C02 dinleme boşluğu (17.4-18.8) ve gök basıncı (18.8-20.0) tonsuz. |
| B14 | 25.6-29.4'te L1 D'yi bırakır; 180.4-210'da L1 D2'yi bırakır; Y2 perdesiz geniş bant | **KABUL** | §6 Y2 · §8c D SAHİPLİĞİ | Y2 üretim cümlesi perdesiz yazıldı (ses:397 sorusunun cevabı). R26 D'sini 221.5'e dek taşır, sonra D'yi yalnız müzik tutar. |
| B15 | P fazı gerçek adım zamanlarından ≥0.25 s kaydırılır; koyulaşma 84.5 → ≈88.0 | **KABUL** (88.4) | §8b R10 · §5 C09 | R10 (86.6-88.2) penceresi 88.4'te biter; koyulaşma 88.4'ten sonra (ses saati esas). Adımlar 82.0 ve 85.0 nominal; F8'de ölçülür. |
| B16 | M kırık 105.5 → 107.5; E kesmeye dek | **KABUL** | §8b R11 · §5 C11 | Solgun inen ıslık (106.6-109.9) −34 → −30; bu aralıkta M ve L1 ≤ −9 dB, M'nin D–E notaları 500 Hz altında (çello D3–E3). |
| B17 | L1 yükselişi 185.6'dan; L2 E 187.0 | **KABUL** | §8 | Membran gıcırtısı (185.0-185.6, E22) temiz kalır. |
| B18 | Besteci §4 çağrı tablosu ses R-listesinden 29 satır olarak kurulur | **KABUL** (28 aktif) | §8b | Tek kaynak tablo mutlak saatlerle yazıldı. R19 düştüğü için 28 aktif satır; numaralar kaymadı (besteci referansları bozulmasın). |
| B19 | Çağrı altı −9 dB; müzik yatağı −18 LUFS-S | **KABUL** | §8 · §9 | Tur 1'deki "−16…−18" aralığı −18'e sabitlendi (kural 8 aralığı içinde). |
| B20 | Etiket C13 son 4 s · C14 ilk 8 s; ses S13 K4 "6.0'da susar" | **KABUL** | §1 S13 · §8 | Susma 126.0 = C13 6.0. Karar kliği (126.6) sessizlikte duyulur. |

KORU (kurgucu): 130 ve 170 kesmeleri iki planda da sessizlik içinde, yatak sürer · 66.0 nabız girişi · 226.5 nabız çıkışı = Khev'in ilk düzenli nefesi · C01 müziksiz · 168.5-170 dikkat uğultusu perdesiz. Hepsi bu dosyada aynen kaldı.

```
TUR 1 → TUR 2 DEĞİŞENLER (besteci ve Fable için kısa liste)
1  Perde G → E (R01 R03 R07 küme R08 R24 R28 ve üretim promptları)
2  C16: R18 153.3-155.7 (baş dönüşüne saatli) · R19, E19, E09·E26, çatlak çıtırtısı düştü · Khev'in 156.6'da kısa içe çekişi eklendi
3  C20: sarma sesi E35 (195.2-198.0) · R23 198.2/198.9/199.6 · R24 C21 0.1'de · Khev kalkma girişimi düştü (çatlak çıtırtısı C20'de yok)
4  S10/S11 K4: nabız 96.0'da durur · S13 K4: 126.0'da susar · S5/S6 K4: 40.0-58.0 müziksiz, M 58.0'dan
5  Y2 yatağı perdesiz geniş bant · E27 ana satırdan çıktı (koşullu yedek) · sorf_saat.wav süresi düzeltildi (150 → ≈165 s)
6  K3/K2 sınırı netleşti (Khev klikleri K3, Khev nefesi K2) · C17 0-2 sörf −18 → −16 (S16 notu "−2 dB" ile uyumlu)
7  R10 çağrı penceresi 86.5-87.8 → 86.5-88.4 (R10 6.6 + 1.6 s = 88.2; tur 1'de aritmetik hata)
8  §8 müzik kısıtları baştan yazıldı; yeni §8b çağrı–müzik saat tablosu (besteci §4'ün kaynağı) ve §8c bant · D sahipliği · nabız
```

## 1. SAHNE TABLOSU (FILM.md §6'ya taşınır)

K3 = çağrı (replik yerine) + Khev klikleri. Köprü sütunu = o çekimden sonraki kesme. J = sonraki sesin önden girmesi, L = bu sesin taşması. K4 hücreleri hakem kararına göredir; besteci tur 2 kesinleştirir.

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | K1 Y1 · K2 göz kapağı gıcırtısı 0-8.4 + Khev adımları 1.2 / 3.1 + omuz plakaları 3.6 · K3 Oru'nun üç ince ıslığı (D5-E5-A5) 4.6 (uzak) + anne nefesi 7.4 · K4 yok | **L 1.2 s:** anne nefesinin kuyruğu C02'ye | İlk ses 0.0'da kapak gıcırtısı: "ay" kımıldıyor, sorun duyuluyor. Çağrı → nefes: Oru üç nota söyler, gök notasız, devasa bir nefesle cevap verir (kod henüz kurulmadı: belirsiz). |
| S2 (C02) | K1 Y1 · K2 membran titremesi, kitin tıkları, Khev uzun nefes · K3 Oru çağrısı (titrek-ince) ışıklara oturur 3.2 / 4.6 / 6.0 · K4 yok | **J 1.2 s:** gök basıncı (tonsuz yükseliş) C02 8.8'den | 7.4-8.8 dinleme boşluğu: yalnız yatak. Işık = ses kodu burada öğretilir. Müzik 22.0'da (C03 2.0) girer. |
| S3 (C03) | K1 Y1 · K2 yüzgeç havası (0-10, zirve 7.0) + okyanus rezonansı · K3 anne tek harmonik ton 5.6-9.4 (D3 + D2, notasız, ışık sönük) · K4 L1 2.0'dan (22.0), çok alçak; D yok (yalnız A3, B14) | **L 1.0 s:** yüzgeç havası C04 0-1.0'a | Başlık (kurgu) C03 27-30 s'de: ses karşılığı yok, ton sürer. Ses: nefes → tek ton → (C05) üç nota: sesin açılışı kademeli. D'yi bu aralıkta ses taşır. |
| S4 (C04) | K1 Y1 · K2 adım + sürtme 3.3, ikinci ayak 4.8-6.3, kemer tonu 5.6'dan, kabuk kıvrımı 7.7 · K3 uzak anne uğultusu (tonsuz) + Oru korku ıslığı 6.5 · K4 L1 ince (ıslıkta −9 dB); L2 ≈33'te çıkar | **J 1.5 s:** dikkat şişmesi C04 8.5'ten (tonsuz) | Gölge sınırı ses sınırıdır: kemer tonu Khev'in ayakları çizgiyi geçtiği 6.0'da girer (kuru, kapalı, sol ağırlıklı). |
| S5 (C05) | K1 Y1 · K2 bulut telleri · K3 anne SOĞUK çağrı ışıklara 0.9 / 2.5 / 4.1 + üç ışık birlikte küme (D-E-A) 5.0-7.0 + göz bebeği inişi sub kayması 7.2-9.6 · K4 **yok (40.0-58.0 müziksiz, B1)** | **L 0.8 s:** soğuk salon yankısı C06'ya | Cevap tınısı soğuk ve boş (akrabalık burada KANITLANMAZ). Müziksiz: ilk kez üç nota yalnız. |
| S6 (C06) | K1 Y1 · K2 esinti genişlemesi, Oru sağ yüzgeç membranı, boyun plakası · K3 Oru + anne SICAK üst üste 2.0-6.4 · K4 8.0'dan (58.0): M cam 58.0 · çello 59.2, ≤ −12 dB | **J 1.0 s:** su kükremesi C06 9.0'dan | 60. saniye ödülü sesle: iki ses aynı notalarla iki oktav arayla üst üste, tek ses gibi. 6.8-8.0 boşluk (56.8-58.0): yalnız rüzgâr ve deniz, müziksiz; müzik 8.0'dan (58.0) çok alçak girer (M ≤ −12 dB). |
| S7 (C07) | K1 Y1 · K2 sırt kükremesi, basınç harmonikleri (0-4.5), gevşek taşlar, sprey · K3 anne durur: uzun hava bırakışı 4.2-6.0 · K4 L1 + L3 (F, 62.0) · nabız 6.0'dan (66.0, deniz saati) | **L 1.5 s:** sırt kükremesi C08'e | Anne durunca basınç harmonikleri kesilir: "kendini tutuyor" kulakta. Sırt tek ve geniş, sağdan sola yürür. Nabız saati sırtla birlikte başlatır. |
| S8 (C08) | K1 Y1 · K2 kemer tonu (kapalı), sörf çıkıntı kenarına vurur 2.2 / 4.8 / 8.0 (öncekinden yakın), kabuk · K3 Oru küçük çağrı 5.2 (ışık atımı) · K4 nabız + L1 (R09 penceresinde −9 dB) | **Hareket üstünde:** ayak parmağı sesi C08 7.6 → C09 0.6'da adım | Üç seviye sesle de ayrılır: kemer altı kapalı ve kuru, geçit açık, çıkıntıya yakın sörf. |
| S9 (C09) | K1 Y1 · K2 iki ağır adım 2.0 / 5.0, kitin sürtünmesi, kemer tonu 0.8-2.3 solar, sörf yükselir, uzak sırt · K3 Oru ışık atımı 6.6 · K4 nabız (fazı adımlardan ≥0.25 s kaydırılır, B15); armoni koyulaşması 88.4'ten | **J 1.0 s:** taş gıcırtısı C09 9.0'dan | Gölge sınırını geçince kapalı oda kapanır, açık sörf yükselir: "sığınağı bırakıyor" kulakta. |
| S10 (C10) | K1 Y1 · K2 öncü kıvrım (0-3.5), taş gıcırtısı genişler (→7.0), kırılma 7.2, düşüş 7.3-8.1, ağır su çarpması 8.1, sprey çöker · K3 yok · K4 nabız **C10 6.0'da (96.0) durur**; 97.0-98.6 müziksiz (öneri, §8) | **L 1.5 s:** çarpma ve sprey kuyruğu C11'e | Sebep (sırt) ve sonuç (kopuş) aynı çekimde sesle de bağlı. Nabız durur, 1.2 s sonra taş kırılır. Kopuştan sonra boşluk: su çekilirken yatak çıplak duyulur. |
| S11 (C11) | K1 Y1 · K2 Oru kanat çırpışı, Khev ellerini uzatır, Khev uzun yavaş nefes, sörf · K3 Oru "umut → zayıf" çağrısı 1.0-6.6 + solgun inen ıslık 6.6-9.9 · K4 L1 yalnız; **M kırık 7.5'te (107.5)**, E kesmeye dek | **Köprü yok (kesme sesin üstünde):** düşen ıslık C11 9.9'da biter, Oru'nun iniş sesi C12 0.15'te | Motif kırılır: iki nota yükselir, üçüncü yükselmez çöker; yüzgeç taşımıyor. Düşüş kesmede, sesi iniş. Nabız yok (96.0'da durdu). |
| S12 (C12) | K1 Y1 · K2 iniş sesi, membran, Oru nefesi, sprey çizgisi, uzak ağır sörf · K3 Oru zayıf çağrı 1.4 ve 9.15 · K4 L1 tek D ≤ −30 LUFS-S; çağrı pencerelerinde yok | **L 1.0 s:** 9.15'teki zayıf çağrı C13 1.0'a taşar | Fener sönükken çağrı da zayıf: ışık = ses yasası. Sprey kenarı Oru'ya ulaşmaz; ses de yalnız kenara kadar. Filmin en sessiz noktası. |
| S13 (C13) | K1 Y1 · K2 Khev nefesi, boyun plakası, itiş sürtmesi 8.0, düşüş rüzgârı 8.1-9.7 · K3 Khev karar kliği 6.6 · K4 **6.0'da (126.0) susar** | **Sert kesme (planlı):** rüzgâr 9.75'te biter, 0.25 s yalnız yatak, iniş C14 0.0 | DORUK. 7.0-7.9 Khev'in tuttuğu nefes: bu sürede yalnız yatak ve sörf. Klik sessizlikte duyulur. Kemere bakış sessiz, Oru'ya bakış çağrı kuyruğuyla (L). |
| S14 (C14) | K1 Y1 · K2 iniş darbesi 0.0 + plaka çatlağı 0.02 + gerilme gıcırtısı + acılı nefes · K3 Khev acı klik-trili 1.3 + Oru solgun notaları 7.2 / 8.6 · K4 yok (126.0-140.0 müziksiz) | **L 0.8 s:** Khev nefesi ve Oru'nun solgun notası C15'e | BEDEL sesle işaretlenir: çatlak çıtırtısı (E25) bundan sonra sol bacağın yük verme girişiminde duyulur (C14 C15 C21). Tek D 140.0'da girer, R16 izi bitince. |
| S15 (C15) | K1 Y1 · K2 beşik teması, Oru nefesi, çatlak çıtırtısı 5.5, köpük yalaması 6.5-10 · K3 Oru zayıf-düzenli ıslık 0.8 / 1.9 / 3.0 · K4 L1 tek D 0.0'dan (140.0); R17 penceresinde (140.8-144.0) ≤ −9 dB | **J 0.8 s:** sörf yükselişi C15 9.2'den | Çağrı C12'den bir kademe canlı ama zayıf; köpük çizgisi sesle yaklaşır, saat işler. |
| S16 (C16) | K1 Y1 · K2 sörf kükremesi yükselir, sprey geçişi, boyun plakası (iki baş dönüşü), rüzgâr kabarması, kuru çıkıntı daralırken köpük yalaması · K3 anne TARAMA süpürmesi 3.3-5.7 (nota yok, cevap yok) · K4 tek D; R18 penceresinde (153.0-156.7) yok ya da ≤ −9 dB; **A ≥ 157.0** | **Köprü yok:** C17 0.0'da sörf −2 dB iner (Khev'in alımı) | Anne baş dönüşüyle arar ama ışıksız: nota yok, kod çalışmaz. Süpürme biter, 1 s cevapsız yatak ve sörf; anne gözü boş terasta durur, Khev ikinci kez ona bakar (6.5). Doğrulma, çökme ve acı sesi yok (sahip kararı). |
| S17 (C17) | K1 Y1 · K2 sörf bedi büyür, sprey patlamaları · K3 Oru TAM çağrı ışıklara 3.3 / 4.6 / 5.9, N3 → 7.6 · K4 **161.5'te (C17 1.5) çıkar**, 179.4'e dek yok | **L 1.2 s + J 1.6 s:** çağrı yankısı C18 0-1.2; anne dikkati (tonsuz) C17 8.4'ten | 7.6-10 dinleme boşluğu: çağrı yok, müzik yok, Khev sessiz; yalnız kabaran sırt. Filmin en açık Oru'su. |
| S18 (C18) | K1 Y1 · K2 sprey perdesi, sörf altta sürer, alt göz kapağı 9.6 · K3 anne dikkat tonu (gezinir → D'ye kilitlenir 6.2) + anne SICAK cevap 6.8 / 8.0 / 9.2 · K4 yok → **tek F♯ 9.4'te (179.4)** | **L 1.5 s:** N3 kuyruğu C19'a, yüzgeç rezonansına çözülür | Aranma → bulunma: perde gezinir, göz bebeği durunca kilitlenir, ilk nota ışıkla gelir. Güven burada başlar. F♯ A3'ün üstüne oturur (filmin ilk majör üçlüsü). |
| S19 (C19) | K1 Y1 · K2 yüzgeç rezonansı (D), membran gıcırtısı 5.0, sakin su yalaması, ufuk sırtı · K3 yok · K4 F♯; L1 yükselişi 185.6'dan (D2 yok), L2 E 187.0 | **L 1.0 s:** yüzgeç rezonansı C20'ye | KURAL KULAKTA: yüzgeç inerken sörf 0.5-1.5 s'de −16 → −28 düzleşir, altında sakin yalama; uzak sırt ayrı ve alçak. D'yi E21 taşır. |
| S20 (C20) | K1 Y1 · K2 Oru kanat çırpışı, süzülüş ve konma 5.0, **yüzgeç sarması (E35) 5.2-8.0**, Khev'in durgun nefesi, yüzgeç damarları · K3 Oru PARLAK çağrı 8.2 / 8.9 / 9.6 · K4 D add9 (sarma altında −6, R23 penceresinde ≤ −9 dB) | **L 0.6 s:** Oru N3 kuyruğu C21'e; anne cevabı C21 0.1'de girer (kesme cevabın hemen öncesine düşer) | Sarma sesi "yardım" okunmalı, "tuzak" okunmamalı: yavaş, sıcak, açık yanlı, sıkışma yok. Işıklar parlarken nota: ışık = ses. Khev kalkmaya çalışmaz, çatlak çıtırtısı yok. |
| S21 (C21) | K1 Y1 · K2 taş→membran sürtmesi, rahatlama nefesi 3.8, köpük, damar parıltısı, yüzgeç rezonansı · K3 anne alçak cevap 0.1 / 1.0 / 1.9 (N3 → 2.7) + Khev çaba kliği 0.35 · K4 **P (anne kalp atışı) 2.6'da (202.6)** · M BÜTÜN 3.5'te (203.5) | **J 2.0 s:** dalga baskısı C21 8.0'dan | Zemin taştan canlı yüzeye geçer: sürtme sesi gritten yumuşak membrana döner. Anne beklemeden cevap verir (Oru N3 üstüne örtüşür): aranma bitti. P cevabın bitişinde, Khev'in yüzgece oturuşunda başlar. |
| S22 (C22) | K1 Y1 → Y2 çapraz 217-220 · K2 yüzgeç yükselişi, kükreme, DALGA 3.4, yayılan kükreme, sprey, su çekilir · K3 anne sabit alçak ton 6.6'dan (D) · K4 212.8-217.6 yok ya da A sus ≤ −9 dB; P ≤ −9 dB; **çözülme 7.6'da (217.6)** | **L 1.5 s:** sprey kuyruğu C23'e | Film zirvesi 0 dB: yalnız boş kaya vurulurken. 3.1-3.35 darbe öncesi 0.25 s çöküş. Dalga müziktir; çözülme dalgadan 4.2 s sonra, anne tonunun D'si üstüne iner. |
| S23 (C23) | K1 Y2 · K2 yüzgeç damar parıltısı, temas, rahat nefesler, uzaklaşan okyanus kalıntısı · K3 Oru TAMAMLANMIŞ ifade 3.2 / 4.2 / 5.2 · K4 çözülme sürer, L3 220.0'da çıkar, L1 ≤ −9 dB; P 6.5'te (226.5) çıkar | **J 1.0 s:** anne ön nefesi C23 9.0'dan | Khev'in nefesi filmde ilk kez düzenli (226.5): korkunun yerini güven alır, nabız aynı anda çıkar. Çatlak çıtırtısı yok (yük vermiyor). |
| S24 (C24) | K1 Y2 (+ yüksek rüzgâr) · K2 yüzgeç esnemesi, uzak sörf solar · K3 anne motifi tamam 1.0 / 3.0 / 5.0 (N3 → 9.0) + Oru tek nota 6.0 · K4 L1 ≤ −9 dB; **L2 + yüksek yaylı 7.2'den (237.2)**; ikinci çözülme 8.0'da (238.0); 240.0 kesme | Çıkış yok (film sonu) | Yeni tehdit yok; doğal kuyruk. Şafak kademesi (238.8) müziğin L2 cam notasıyla (ses efekti yok; yedek koşullu). Son 1 s yatak solar, çağrı kuyruğu 239.85'e dek doğal biter. |

## 2. ORTAM (FILM.md §6 satırı için)

```
Ortam: Açık, nefes alınabilir, ses taşıyan atmosfer (gece, deniz kıyısı). Vakum yok, kask yok, iç hacim yok; C24 bulut tepelerinin üstünde ama atmosferin içinde.
       Duyulan: rüzgâr, sörf, sprey, taş (hava ile taşınır) · kitin, membran, taş teması (temas) · Oru, Anne ve Khev'in sözsüz sesleri (canlı).
       Ölçek: dev şey alçak ve yavaş, küçük şey tiz ve hızlı. Telsiz ve replik yok. Ortam yatağı Y1 (kıyı) 0.0-220.0, Y2 (yüzgeç-hava, perdesiz geniş bant) 217.0-240.0; dijital sıfır yok.
       Çağrı perdesi D–E–A (Oru D5 E5 A5, anne iki oktav aşağı). Model sesi kullanılmaz (klip sesi atılır; ses kurguda).
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_2.md
```

## 3. KAYIT LİSTESİ (REPLİK yok: sözsüz canlı sesler, tek kaynak)

Ses aracı sahibindir; profil adları araçtan bağımsızdır. Ticari koşul: Flow Music ve Mondo Sónico çıktılarının ticari koşulu BİLİNMİYOR (`FLOW_GERCEKLERI` §6); araç seçimi sahibin.
`model` filtreli satır yok: ağız kadrajında replik yok. Filtre sütunu bu filmde mesafe profilidir: **YAKIN** (kuru, yansımasız) · **ORTA** (kısa açık hava yankısı, RT 1.2 s) · **UZAK** (4 kHz alçak geçiren, uzun yansıma) · **DEV** (RT 3-7 s, geniş stereo).
Üç profil, film boyu aynı: **ORU_CAGRI_v1** · **ANNE_CAGRI_v1** (ORU'dan türetilir) · **KHEV_KLIK_v1**. Nota adları D–E–A sözleşmesine göredir (N1 = D, N2 = E, N3 = A).

| No | Metin (nota / ifade) | Konuşan | Ses profili | Ton | Hedef süre (s) | Filtre | Çekim · saniye |
|:--:|---|---|---|---|:--:|---|---|
| R01 | üç nota D5-E5-A5, ince, cümle | Oru | ORU_CAGRI_v1 | ince-uzak | 3.0 | UZAK | C01 · 4.6 |
| R02 | tonsuz devasa nefes | Anne | ANNE_CAGRI_v1 · nefes | boş-devasa | 3.8 (+1.2 L) | DEV | C01 · 7.4 |
| R03 | üç nota, ışığa oturur, titrek | Oru | ORU_CAGRI_v1 | titrek-ince | 4.2 | ORTA | C02 · 3.2 |
| R04 | tek derin harmonik ton (D3 + D2) | Anne | ANNE_CAGRI_v1 · ton | derin | 3.8 | DEV | C03 · 5.6 |
| R05 | uzak, tonsuz uğultu (D1-D2 bölgesi); 8.5'te dikkat şişmesi | Anne | ANNE_CAGRI_v1 · uğultu | uzak | 10 (+J 1.5) | DEV | C04 · 0.0 ve 8.5 |
| R06 | tek nota N1 (D5), kırılarak iner | Oru | ORU_CAGRI_v1 · korku | korkmuş | 0.7 | ORTA | C04 · 6.5 |
| R07 | üç nota ışığa oturur + küme (D-E-A birlikte, 5.0-7.0) + sub kayma | Anne | ANNE_CAGRI_v1 · soğuk | boş-soğuk | 9.0 | DEV (soğuk salon RT 7 s) | C05 · 0.9 |
| R08 | Oru üç nota + Anne aynı üç nota üst üste | Oru + Anne | ORU_CAGRI_v1 + ANNE_CAGRI_v1 · sıcak | ince + sıcak | 4.4 | ORTA + DEV | C06 · 2.0 |
| R09 | küçük çağrı, kısa N3 | Oru | ORU_CAGRI_v1 · küçük | umutlu-ısrarlı | 1.8 | ORTA | C08 · 5.2 |
| R10 | küçük çağrı, ışık atımı | Oru | ORU_CAGRI_v1 · küçük | ısrarlı | 1.6 | ORTA | C09 · 6.6 |
| R11 | N1-N2 yükselir, N3 yükselmez çöker (A5 → D5, −7 st) | Oru | ORU_CAGRI_v1 · umut→zayıf | umutlu → çöken | 5.8 | ORTA → UZAK | C11 · 1.0 |
| R12 | tek nota N1, nefesli, titrek | Oru | ORU_CAGRI_v1 · zayıf | kırılgan | 1.0 | YAKIN | C12 · 1.4 |
| R13 | tek nota N1, solgun | Oru | ORU_CAGRI_v1 · zayıf | solgun | 0.8 (+1.0 L) | YAKIN | C12 · 9.15 |
| R14 | gergin içe çekiş kliği | Khev | KHEV_KLIK_v1 | gergin | 0.4 | YAKIN | C13 · 6.6 |
| R15 | acı klik-trili: üç hızlanan klik, kesilir | Khev | KHEV_KLIK_v1 | kısıtlı-acılı | 0.9 | YAKIN | C14 · 1.3 |
| R16 | iki solgun nota (+ 9.4'te üçüncü iz) | Oru | ORU_CAGRI_v1 · zayıf | solgun | 0.8 + 0.8 | YAKIN | C14 · 7.2 ve 8.6 |
| R17 | üç nota, zayıf ama düzenli | Oru | ORU_CAGRI_v1 · zayıf-düzenli | zayıf-canlanan | 3.0 | YAKIN | C15 · 0.8 |
| R18 | tonsuz yükselen süpürme, cevapsız biter (anne baş dönüşüne saatli) | Anne | ANNE_CAGRI_v1 · tarama | arayan | 2.4 | DEV | C16 · 3.3 |
| R19 | ~~acılı tek klik~~ **DÜŞTÜ** (sahip kararı 17.10.2026: C16'da doğrulma/çökme yok); numara korunur | Khev | KHEV_KLIK_v1 | — | — | — | — |
| R20 | üç nota ışığa oturur, tam bant, N3 uzun | Oru | ORU_CAGRI_v1 · tam | açık-kararlı | 4.3 | ORTA | C17 · 3.3 |
| R21 | tonsuz dikkat: şişme → gezinme → D'ye kilit | Anne | ANNE_CAGRI_v1 · dikkat | arayan → bulan | 8.4 + 6.2 | DEV | C17 · 8.4 → C18 · 6.2 |
| R22 | üç nota ışığa oturur, sıcak, N3 C19'a taşar | Anne | ANNE_CAGRI_v1 · sıcak | sıcak-devasa | 4.7 (+1.5 L) | DEV | C18 · 6.8 |
| R23 | üç nota parlak, kısa aralık (0.7 s), parlayan ışıklara oturur | Oru | ORU_CAGRI_v1 · parlak | neşeli-rahatlamış | 2.4 | ORTA | C20 · 8.2 |
| R24 | alt perdede üç nota (D2 E2 A2), hissedilen; Oru N3 üstüne örtüşür | Anne | ANNE_CAGRI_v1 · alçak | koruyucu | 2.6 | DEV | C21 · 0.1 |
| R25 | çaba kliği | Khev | KHEV_KLIK_v1 | çabalı | 0.3 | YAKIN | C21 · 0.35 |
| R26 | sabit alçak ton (D), vibratosuz; Y2 altında söner | Anne | ANNE_CAGRI_v1 · ton | güvenli | 3.4 + 1.5 söner | DEV | C22 · 6.6 |
| R27 | tamamlanmış ifade, üç nota ılık | Oru | ORU_CAGRI_v1 · tamamlanmış | huzurlu | 3.0 | YAKIN | C23 · 3.2 |
| R28 | motif tamam: üç nota yavaş (D3 E3 A3), N3 tutulur | Anne | ANNE_CAGRI_v1 · sıcak | çözülmüş-engin | 8.0 | DEV | C24 · 1.0 |
| R29 | tek ince nota A5, anne N3'ü üstünde (oktav kaynaşması) | Oru | ORU_CAGRI_v1 · tamamlanmış | küçük-huzurlu | 1.2 | UZAK | C24 · 6.0 |

```
KAYIT NOTLARI
ORU_CAGRI_v1   Üretim promptu: a tiny alien creature's thin glassy three-note whistle call, notes D5 then E5 then A5 about 0.9 seconds apart, the last note held with slight vibrato,
               pure whistle tone with soft glass harmonics, dry close recording, no reverb, no music, no words.
               Araç perdeyi tutmazsa: üç nota ayrı üretilir ya da cam harmonika / ıslık sentezi ile kurulur; perde ölçülür (587.3 · 659.3 · 880.0 Hz). Çıktı dosyaları:
               oru_cagri_tam.wav (cümle, kanonik aralık) · oru_n1.wav · oru_n2.wav · oru_n3.wav (ışığa oturan çekimler için ayrı notalar, her biri 1.5 s kuyruklu).
ANNE_CAGRI_v1  Zincir: ORU_CAGRI_v1 → pitch −24 st (D3 E3 A3) · formant −8 st · atak 0.25 s · tutuş ×2 · bırakış 2 s · gövde katmanı (a bowed low organic tone with soft breathy formants,
               D2 E2 A2) −6 dB · reverb. SICAK: tam harmonikler, tam perde, açık hava RT 3.5 s, deniz yüzeyinden erken yansıma. SOĞUK (yalnız C05): yalnız tek harmonikler, −25 cent,
               RT 7 s, ön gecikme 120 ms, gövde katmanı yok. ALÇAK (C21): −12 st daha (D2 E2 A2), yalnız hissedilen, −14.
               TELEFON PAYI: temel ≥ 140 Hz (D3 146.8 · E3 164.8 · A3 220.0); 2. ve 3. harmonikler (290-660 Hz) çıplak duyulacak seviyede (kayıttan sonra telefon hoparlöründe dinlenir).
               Yalnız çok alçak bas yetmez: ALÇAK cevapta da 2.-4. harmonikler (147-440 Hz) bırakılır.
KHEV_KLIK_v1   Üretim promptu: a dry restrained chitin click made by a large insect-like alien throat, low body around 200 hertz with a sharp tick, single, no human voice, close and dry.
               Varyantlar: gergin içe çekiş (yükselen, kısa) · acı klik-trili (üç hızlanan klik, kesilir) · çaba kliği (tek, ağır). Aynı oturumda, aynı mikrofon.
               (Acılı tek klik varyantı R19 ile düştü.)
IŞIK ÖNCE      Çekim seçildikten sonra ışık başları kare kare okunur (kareler.py cikar, 24 fps); nota başı ışık başından 0.05-0.1 s sonra. Işık sırası soldan sağa = nota sırası.
               C20'de ışıklar zaten yanıktır ve 8-10 s'de PARLAR: nota başı parlama başlangıcına oturur; model parlamayı sırayla vermezse (hepsi birden) nota aralığı 0.7 s kalır, sıra ve oran korunur.
```

### 3b. Çağrı durumları (yeni kayıt değil, işleme)

| Durum | Çekim | Ne değişir |
|---|---|---|
| ince-uzak | C01 | 4 kHz alçak geçiren, hafif tremolo, uzun yansıma, −20 |
| titrek-ince | C02 | tremolo %12 (5.5 Hz), hafif nefesli, orta mesafe, −10 |
| korku | C04 | yalnız N1; kırılarak iner (−5 st / 0.5 s) |
| küçük | C08 C09 | kanonik, N3 kısa (kuyruksuz), +20 cent yükselişle ısrarlı |
| umut → zayıf | C11 | N1-N2 12 cent yukarı eğimli; N3 yükselmez, −7 st / 2.2 s çöker, seviye −12 → −26 |
| zayıf | C12 C14 | −8 dB, nefesli, ±35 cent titrek; N2 geç ya da eksik |
| zayıf-düzenli | C15 | zayıf ama sıralı ve eşit aralıklı: C12'den "bir kademe canlı" |
| tam | C17 | tam bant, 3 kHz'de +2 dB, N3 uzun; üç ışık yanıkken cam üst harmonikleri (6.2-7.4 s) |
| parlak | C20 | tam + aralık 0.7 s (heyecan; ışık parlaması sırası), N3 uzun, yükselen son |
| tamamlanmış | C23 C24(Oru) | ılık: 4 kHz −3 dB, 700 Hz +2 dB; N3 vibratosuz, yumuşak iniş |

### 3c. Çağrı-cevap gecikmeleri (kural 6: kesme gecikmeyi yemez)

Gecikme = çağrının N3 sonundan cevabın ilk notasına; negatif = örtüşme.

| Alışveriş | Gecikme | Bu planda (mutlak) | Anlamı |
|---|:--:|---|---|
| C01 Oru N3 sonu → anne nefesi | 0.1-0.2 s | 7.2 → 7.4 | hemen ve ağır, ama notasız: kod yok |
| C06 Oru + anne | 0 (örtüşür) | 52.0 / 52.05 | akrabalık: aynı anda aynı notalar |
| C17 Oru N3 sonu → anne ilk nota | **9.2 s** | 167.6 → 176.8 | araya tonsuz dikkat, gezinme, kilit; aranma → bulunma; C16'nın cevapsız taraması (153.3-155.7) bunun başlangıcı |
| C20 Oru N3 sonu → anne ilk nota | **−0.5 s** (örtüşür) | Oru N3 199.6-200.6 · anne N1 200.1 (N3 başı + 0.5 s) | aranma bitti, cevap beklemeden gelir; cevap C21'e düşer (kesme 200.0, cevabın 0.1 s öncesinde) |

## 4. SES VARLIKLARI (E-kodları; §5 satırları bunlara bağlanır)

"Nereden" = tek satır İngilizce üretim ya da arama cümlesi. Hepsi kuru ve temiz üretilir, mesafe/yankı kurguda (§3 profilleri) verilir; ses ve müzik içermeyen kayıt istenir. E04 tur 1'den beri boş (kullanılmaz). Tur 2'de tek yeni kod: **E35**.

| Kod | Ad | Nereden |
|:--:|---|---|
| E01 | göz kapağı | `a colossal organic eyelid slowly peeling open, wet leather creaking over stone, very low and slow, enormous and far away, with a clear midrange creak texture, no voice, no music` |
| E02 | Khev adımı | `one heavy dry footstep of a large clawed biped on gritty basalt, close, fine grit crunch under a muffled thump, no echo, no voice` |
| E03 | kitin plaka | `a soft dry creak and slide of stiff ivory chitin armor plates shifting against each other, close and small, no voice` |
| E05 | anne nefesi | `an immense slow breath from the sky, hollow and low, a vast chamber of air with a faint throat resonance around 400 to 900 hertz, no pitch, no voice, no music` |
| E06 | anne tek ton | `one deep warm harmonic tone of an enormous creature, pitch D3 with a soft D2 underneath, slow swell and long release, bowed-string like texture, no vibrato, no words, no music` |
| E07 | yüzgeç havası | `a vast slow displacement of air as an immense wing rises, broad low rushing roar with midrange body, gradually rising, open air, no voice, no music` |
| E08 | okyanus rezonansı | `distant deep ocean resonance, sub-bass swell with soft irregular rolls, no rhythm, no voices` |
| E09 | ayak sürtmesi | `a dry scrape of a clawed foot sliding across gritty basalt, short, close` |
| E10 | Khev kliği | KHEV_KLIK_v1 (§3 notu) |
| E11 | membran titremesi | `tiny trembling flutter of a thin membrane fin, very quiet and delicate, close` |
| E12 | kemer tonu | `quiet room tone inside a sheltered stone alcove, dry low stone cavity resonance around 150 hertz, wind muffled outside, no echo, no voices` |
| E13 | sörf / sırt | `slow irregular heavy ocean surf on black rock, long swells and slow wash, no rhythm, no voices, no music` · tek sırt: `a single broad dark water ridge building and rolling shoreward, low growing roar with pressure, no foam crackle, no music` |
| E14 | gevşek taş | `loose pebbles and small stones rattling and jumping on rock, sparse and distant` |
| E15 | sprey | `fine sea spray hiss and soft splash droplets in open air, airy, no voices` |
| E16 | taş kopuşu | `a slow widening creak of a heavy stone slab tilting, then one sharp snap` · çarpma: `one heavy slab of rock hitting the sea with a huge splash and falling spray` |
| E17 | Oru kanadı | `soft slow flaps of a wide thin membrane wing, gliding small creature, delicate, close` |
| E18 | düşüş rüzgârı | `wind rushing past a falling body, descending pitch, about one and a half seconds, no voice` |
| E19 | iniş | `a heavy landing of a large biped on rock, one deep body thump with a short gritty skid and low resonance, close` |
| E20 | köpük / yalama | `foam and shallow water creeping over wet rock, soft hiss growing, then one wet slap` · yalama (tokatsız): `foam and shallow water creeping over wet rock, soft hiss growing, no slap` · sakin: `gentle water lapping softly under a surface, flat calm` |
| E21 | yüzgeç rezonansı | `a deep warm organic resonance of an immense living wing surface, soft harmonic hum around D, midrange warmth, slow swell, no voice, no music` |
| E22 | membran gıcırtısı | `a soft creak and flex of a huge warm living membrane, slow, gentle` |
| E23 | taştan membrana | `a gritty scrape on stone changing into a soft damp slide across warm living membrane, short` |
| E24 | dalga | `one enormous dark ocean wave hitting an empty rock ledge, a massive impact with sub-bass thump, then a wide spreading roar of water and spray, four seconds, no voices` |
| E25 | çatlak | `a single dry sharp crack of a hard shell plate, with a faint wet glass shimmer after it, close` · çıtırtı: `faint dry crackle of a cracked shell plate flexing, very small, close` |
| E26 | Khev nefesi | `a dry low papery exhale through gill slits of an alien, non-human, slow, close` |
| E27 | şafak parıltısı | `a tiny bright glass-like harmonic shimmer, warm and resolving, very quiet` (**koşullu yedek**: yalnız L2 cam notası 238.4-239.2'de duyulmuyorsa, §5 C24) |
| E28 | Oru nefesi | `very faint airy breathing of a tiny animal, irregular, close` |
| E29 | yüksek rüzgâr | `thin high-altitude wind, soft and airy, wide stereo, no harsh highs` |
| E30 | bulut telleri | `soft airy hiss of thin cloud strands passing, lateral, very quiet` |
| E31 | yüzgeç damarı | `a soft warm glassy tone swell as glowing veins pulse in a living wing, quiet, irregular` |
| E32 | Oru inişi | `a tiny soft thud and membrane scrape of a small soft body landing on stone` (C20'de yüzgeç yüzeyi için: `a tiny soft pat of a small body settling onto a warm living membrane, no scrape`) |
| E33 | tarama | `a slow low sweeping tone from an immense creature, airy and searching, a rising glide that ends unanswered, no notes, no words` |
| E34 | dikkat | `a slow pitchless low swell of attention from an immense creature, hollow air with slight pitch drift, no notes` |
| E35 | yüzgeç kıvrılması (**yeni**, E22 ailesinden) | `a slow soft creak and curl of the rounded edge of an immense warm living membrane bending gently upward and inward, low and flexing, gentle and open, no squeeze, no wet squelch, no voice, no music` |

## 5. EFEKT LİSTESİ (24/24 çekim)

Kaynak: **hava** (açık atmosferde taşınır: rüzgâr, su, taş) · **temas** (taş, kitin, membran teması) · **canlı** (sözsüz canlı sesi).
Y1 her çekimde sürer (§6; satırlara yazılmaz). Işık-nota satırları "ışığa oturur" diye işaretli. Seviye: 0 dB = C22 dalga tepesi; "yatağa" yazılanlar LUFS değil, ölçek dB'sidir. Müzik (K4) satırları §1 ve §8'dedir.

| Çekim | Saniye | Ses | Kaynak | Katman | Seviye | Nereden |
|:--:|---|---|---|:--:|---|---|
| C01 | 0.0-8.4 | göz kapağı açılır: ıslak deri taş üstünde sürer gibi alçak yavaş gıcırtı; kapak ilerledikçe büyür (ilk ses) | temas | K2 | −20 → −12 | E01 |
| C01 | 1.2 · 3.1 | Khev'in iki adımı; ikincisi ayak basılıyken durur | temas | K2 | −22 · −20 | E02 |
| C01 | 3.6 | omuzlar kalkar, kollar Oru'yu sıkar | temas | K2 | −26 | E03 |
| C01 | 4.6 · 5.5 · 6.4 | Oru'nun üç ince ıslığı (D5-E5-A5, uzak), N3 7.2'ye dek | canlı | K3 | −20 | R01 (ince-uzak) |
| C01 | 7.4-11.2 | anne: tek devasa alçak tonsuz nefes; 8.8-9.2 zirve; kuyruk C02 1.2'ye | canlı | K3 | −12 | R02 · E05 |
| C02 | 0.0-1.2 | anne nefesinin kuyruğu (C01'den) | canlı | K3 | −14 → −30 | R02 (L) |
| C02 | 0.8-3.0 | Oru'nun sol yüzgeci titrer | temas | K2 | −32 | E11 |
| C02 | 1.6 | Khev kolları beşiğe oturur: kuru plaka tıkı | temas | K2 | −28 | E03 |
| C02 | 3.2 · 4.6 · 6.0 | Oru'nun üç notası ışıklara oturur (titrek-ince), N3 7.4'e dek | canlı | K3 | −10 | R03 |
| C02 | 6.9-7.6 | Khev başını kaldırır: boyun plakası; 7.2 uzun nefes | temas | K2 | −28 | E03 · E26 |
| C02 | 7.4-8.8 | dinleme boşluğu: yalnız yatak | — | — | — | — |
| C02 | 8.8-10.0 | J: gök basıncı, tonsuz yükseliş (C03'e) | hava | K2 | −34 → −24 | E34 |
| C03 | 0.0-10.0 | yüzgeç havası: bulut kenarından yükselir, 7.0'da zirve, sonra sabit | hava | K2 | −22 → −12 | E07 |
| C03 | 0.0-10.0 | okyanus rezonansı (alt bant) | hava | K2 | −24 | E08 |
| C03 | 5.6-9.4 | anne tek derin harmonik ton (D3 + D2); notasız, ışık sönük | canlı | K3 | −14 | R04 · E06 |
| C04 | 0.0-1.0 | yüzgeç havası kuyruğu (C03'ten) | hava | K2 | −20 → −40 | E07 (L) |
| C04 | 0.0-10.0 | uzak yetişkin uğultusu (tonsuz); 8.5-10.0 −18'e yükselir (J) | canlı | K3 | −30 → −18 | R05 · E34 |
| C04 | 0.9 | ayak kalkışı: plaka çıtırtısı | temas | K2 | −28 | E03 |
| C04 | 3.3 | ayak bazalta basar, kuru sürtme | temas | K2 | −18 | E02 · E09 |
| C04 | 4.8-6.3 | ikinci ayak çekilir; 6.3'te basar | temas | K2 | −22 | E09 |
| C04 | 5.6-7.0 | kemer tonu girer (gölge sınırı 6.0); C08'e dek sürer | hava | K2 | yok → −28 | E12 |
| C04 | 6.5 | Oru'nun korku ıslığı: tek nota (D5), kırılarak iner | canlı | K3 | −16 | R06 |
| C04 | 7.7-9.0 | ön kollar Oru'nun çevresinde kıvrılır: plaka sürtmesi | temas | K2 | −20 | E03 |
| C05 | 0.0-0.9 | J: dikkat şişmesi ilk nota ışığa açılır | canlı | K3 | −18 | E34 |
| C05 | 0.9 · 2.5 · 4.1 | anne SOĞUK çağrı, ışıklara oturur (−25 cent, tek harmonik, salon RT 7 s) | canlı | K3 | −9 | R07 |
| C05 | 5.0-7.0 | üç ışık birlikte: üç nota birlikte tınlar (D-E-A kümesi, Dsus2), zirve 5.4 | canlı | K3 | −8 | R07 |
| C05 | 7.2-9.6 | göz bebeği iner: alt oktava kayan tonsuz sub inişi | canlı | K3 | −24 | E34 (ters) |
| C05 | 0.0-10.0 | bulut telleri: yatay ince hışırtı | hava | K2 | −34 | E30 |
| C06 | 0.0-2.0 | açık hava genişlemesi: rüzgâr esintisi | hava | K2 | −26 | E29 |
| C06 | 1.2 | Oru sağ yüzgecini kaldırır | temas | K2 | −32 | E11 |
| C06 | 2.0 · 2.9 · 3.8 | Oru çağrısı (kanonik aralık) | canlı | K3 | −12 | R08 |
| C06 | 2.05 · 2.95 · 3.85 | anne SICAK çağrı: aynı notalar iki oktav aşağıda, üst üste; N3 6.4'e dek | canlı | K3 | −8 | R08 |
| C06 | 4.5-7.5 | Khev başını baştan kuyruğa çevirir: boyun plakası | temas | K2 | −30 | E03 |
| C06 | 6.8-10.0 | çağrılar bitti: yalnız rüzgâr ve deniz (boşluk, 6.8-8.0 müziksiz); müzik M 8.0'dan (58.0) girer, ≤ −12 dB | — | — | — | — |
| C06 | 9.0-10.0 | J: su kükremesi başlar (C07'ye) | hava | K2 | −34 → −28 | E13 |
| C07 | 0.0-4.0 | sırt büyür: kükreme | hava | K2 | −32 → −18 | E13 (tek sırt) |
| C07 | 0.0-4.5 | basınç harmonikleri (tonsuz D1-A1 yığını) yükselir, 4.5'te kesilir | hava | K2 | −26 → −16 | E34 (alçak) |
| C07 | 1.0-10.0 | sprey sıçraması | hava | K2 | −28 | E15 |
| C07 | 1.8 · 2.7 · 3.4 · 6.5 · 8.2 | gevşek taş takırtıları (uzak) | hava | K2 | −28 | E14 |
| C07 | 4.2-6.0 | anne durur: uzun yumuşak hava bırakışı; basınç kesilir | canlı | K3 | −18 | E05 (kısa) |
| C07 | 6.0-10.0 | sırt tek başına ilerler (sağdan sola pan), −18 → −14; C08 1.5'e taşar | hava | K2 | −18 → −14 | E13 |
| C08 | 0.0-1.5 | sırt kükremesi kuyruğu | hava | K2 | −14 → −26 | E13 (L) |
| C08 | 0.0-10.0 | kemer tonu (kapalı, kuru) | hava | K2 | −28 | E12 |
| C08 | 1.0-4.0 | Khev başını çevirir: boyun plakası | temas | K2 | −32 | E03 |
| C08 | 2.2 · 4.8 · 8.0 | sörf çıkıntı kenarına vurur (öncekinden yakın) | hava | K2 | −24 | E13 |
| C08 | 5.2-7.2 | Oru küçük çağrı, ışık atımına oturur | canlı | K3 | −16 | R09 |
| C08 | 7.6 | Khev ayak parmağı gölge çizgisine basar | temas | K2 | −24 | E02 (yumuşak) |
| C09 | 0.6 · 3.6 | adım kalkışlarında kitin sürtünmesi | temas | K2 | −28 | E03 |
| C09 | 2.0 · 5.0 | iki ağır kuru adım (açık geçit, bazalt) | temas | K2 | −14 · −13 | E02 |
| C09 | 0.8-2.3 | kemer tonu solar (çizgi geçildi) | hava | K2 | −28 → yok | E12 (fade) |
| C09 | 0.0-10.0 | sörf yatağı yükselir (ana yükseliş 0-3 s) | hava | K2 | −26 → −18 | E13 |
| C09 | 6.5-10.0 | ufuktaki sırt: uzak alçak kükreme | hava | K2 | −26 → −22 | E13 (uzak) |
| C09 | 6.6 | Oru ışık atımı: küçük çağrı (88.2'ye dek) | canlı | K3 | −18 | R10 |
| C09 | 9.0-10.0 | J: taş gıcırtısı başlar (C10'a) | hava | K2 | −30 → −24 | E16 |
| C10 | 0.0-3.5 | sırtın öncü kıvrımı geçidin altına yükselir, taşı yalar | hava | K2 | −22 → −14 | E13 · E15 |
| C10 | 0.0-7.0 | taş gıcırtısı genişler (C09'dan sürer) | hava | K2 | −24 → −12 | E16 |
| C10 | 7.2 | kırılma: tek keskin çatlama | hava | K2 | −6 | E16 |
| C10 | 7.3-8.1 | levha düşer: taş sürtmesi ve dönmesi | hava | K2 | −14 | E16 |
| C10 | 8.1 | denize ağır çarpma + sprey | hava | K2 | −5 | E16 (çarpma) |
| C10 | 8.2-10.0 | sprey çöker, su çekilir (boşluk) | hava | K2 | −14 → −30 | E15 · E20 |
| C11 | 0.0-1.5 | çarpma ve sprey kuyruğu (C10'dan) | hava | K2 | −14 → −34 | E16 (L) |
| C11 | 0.4-4.5 | Oru'nun kanat çırpışı | temas | K2 | −22 | E17 |
| C11 | 1.0 · 2.0 | umutlu yükselen cıvıltı (N1, N2) | canlı | K3 | −10 | R11 |
| C11 | 3.3-6.6 | N3 yükselmez, çöker: inen zayıf ıslık | canlı | K3 | −12 → −26 | R11 |
| C11 | 4.5-7.2 | kanat çırpışı düzensizleşir (sol yüzgeç geride), uzaklaşır | temas | K2 | −22 → −34 | E17 |
| C11 | 4.7 | Khev'in elleri uzanır: kitin sürtmesi | temas | K2 | −28 | E03 |
| C11 | 3.0 · 7.8 | sörf vuruşları (çıkıntı kenarı) | hava | K2 | −24 | E13 |
| C11 | 6.6-9.9 | solgun inen ıslık (kadraj dışı); 9.9'da kesmeyle biter. −34 → **−30** (M kırık 7.5'te bu ıslığın altına binmesin; müzik ≤ −9 dB) | canlı | K3 | −30 | R11 |
| C11 | 8.0-9.4 | Khev boş elleri görür: uzun yavaş nefes | canlı | K2 | −24 | E26 |
| C12 | 0.15 · 0.4-0.9 | Oru'nun inişi: küçük gövde + membran sürtmesi | temas | K2 | −26 | E32 |
| C12 | 1.4 | zayıf tek çağrı (N1), yüzgeç çabasıyla birlikte | canlı | K3 | −20 | R12 |
| C12 | 3.0 | yüzgeç geri düşer: yumuşak vuruş | temas | K2 | −28 | E32 |
| C12 | 4.0 · 4.6 · 5.7 | düzensiz sönük ışık atımları: soluk nota izleri | canlı | K3 | −34 | R12 (N1-N2 izleri) |
| C12 | 6.0-10.0 | Oru nefesi; 7.5'te yüzgeç bir kez titrer | temas | K2 | −30 · −32 | E28 · E11 |
| C12 | 6.5-10.0 | sprey çizgisi kenarda ilerler (Oru kuru) | hava | K2 | −30 → −26 | E15 |
| C12 | 0.0-10.0 | uzak ağır sörf; 2.5 ve 8.0'da vuruş | hava | K2 | −24 | E13 |
| C12 | 9.15 | ikinci zayıf çağrı (N1, solgun); C13 1.0'a taşar | canlı | K3 | −24 | R13 |
| C13 | 0.0-1.0 | Oru'nun zayıf çağrısının kuyruğu | canlı | K3 | −24 → −34 | R13 (L) |
| C13 | 0.8-2.8 | Khev dikkatli nefes | canlı | K2 | −26 | E26 |
| C13 | 3.0-4.2 · 4.5-5.6 | baş sola (kemer), sonra aşağı: boyun plakası | temas | K2 | −30 | E03 |
| C13 | 6.6 | gergin içe çekiş kliği (karar); müzik 6.0'da (126.0) çıkmış, klik sessizlikte | canlı | K3 | −18 | R14 · E10 |
| C13 | 7.0-7.9 | tutulan nefes: Khev sessiz, yalnız yatak ve sörf | — | — | — | — |
| C13 | 8.0 | itiş: pençe taşta sürter | temas | K2 | −12 | E09 |
| C13 | 8.1-9.7 | düşüş rüzgârı, alçalan perde; 9.75'te biter | hava | K2 | −16 → −30 | E18 |
| C13 | 9.75-10.0 | planlı boşluk: yalnız yatak (sert kesme öncesi) | — | — | — | — |
| C13 | 8.5-10.0 | ufuktaki sırt: yükselen alçak uğultu | hava | K2 | −28 | E13 (uzak) |
| C13 | 0.0-10.0 | sörf aşağıda, düzensiz | hava | K2 | −24 → −22 | E13 |
| C14 | 0.0 | iniş: gövde darbesi + kısa sürtme + alçak rezonans (kuyruk 0.6-1.4) | temas | K2 | −6 | E19 |
| C14 | 0.02 | sol kaval plakası çatlar: kuru çatlak + sönük cam parıltısı | temas | K2 | −10 | E25 |
| C14 | 1.0 · 2.4 | sol bacağa yük verme denemesi: gerilme gıcırtısı + çatlak çıtırtısı | temas | K2 | −22 | E03 · E25 (çıtırtı) |
| C14 | 1.3-2.2 | acı klik-trili (kısıtlı), kesilir | canlı | K3 | −14 | R15 · E10 |
| C14 | 3.0-4.2 | baş çatlağa eğilir: boyun plakası | temas | K2 | −30 | E03 |
| C14 | 3.5-6.0 | acılı düzensiz nefes; 6.8'de uzun, gevşeyen nefes (başı Oru'ya çevirirken) | canlı | K2 | −24 · −26 | E26 |
| C14 | 5.0-10.0 | kadraj kenarından ince sis geçer | hava | K2 | −30 | E15 |
| C14 | 7.2 · 8.6 | Oru'nun solgun iki notası; 9.4'te üçüncü iz C15'e taşar | canlı | K3 | −32 · −26 | R16 |
| C14 | 0.0-10.0 | sörf çıkıntıya yakın | hava | K2 | −20 | E13 |
| C15 | 0.3 | beşik sıkılaşır: yumuşak kuru temas | temas | K2 | −28 | E03 |
| C15 | 0.8 · 1.9 · 3.0 | Oru zayıf ıslık, ışıklara oturur (düzenli, soluk); N3 3.8'e dek | canlı | K3 | −18 | R17 |
| C15 | 0.0-10.0 | Oru'nun yavaş nefesi | temas | K2 | −30 | E28 |
| C15 | 4.4 · 5.5 | ağırlık sağ yana: kitin; sol kaval plakası çıtırtısı | temas | K2 | −26 · −30 | E03 · E25 (çıtırtı) |
| C15 | 6.5-10.0 | köpük çizgisi yaklaşır: yalama büyür, 8.7'de ıslak tokat | hava | K2 | −30 → −22 | E20 |
| C15 | 8.0 | Khev başını köpüğe çevirir: boyun | temas | K2 | −30 | E03 |
| C15 | 9.2-10.0 | J: sörf yükselişi (C16'ya) | hava | K2 | −28 → −22 | E13 |
| C16 | 0.0-10.0 | sörf kükremesi sürekli yükselir (dalga sırtı çıkıntıya yaklaşır) | hava | K2 | −22 → −14 | E13 |
| C16 | 0.0-3.0 | sprey kadrajın sağ kenarından geçer | hava | K2 | −26 | E15 |
| C16 | 0.0-2.0 | Khev başını Oru'dan duvarın tepesine kaldırır: boyun plakası | temas | K2 | −32 | E03 |
| C16 | 3.3-5.7 | anne TARAMA süpürmesi, baş dönüşüne saatli (baş 3.0'da döner, ses 0.3 s sonra): tonsuz yükselen süpürme, nota yok, cevap yok; 5.7-6.7 cevapsız 1 s: yalnız yatak ve sörf | canlı | K3 | −16 | R18 · E33 |
| C16 | 5.5-8.0 | dalga basıncı: rüzgâr kabarması | hava | K2 | −26 | E29 |
| C16 | 6.5-7.5 | Khev başını sağa, ufuktaki anneye çevirir: boyun plakası; 6.6'da kısa, kâğıtsı içe çekiş | temas | K2 | −32 · −30 | E03 · E26 |
| C16 | 8.0-10.0 | kuru çıkıntı daralır: köpük yalaması yaklaşır (tokat yok) | hava | K2 | −30 → −26 | E20 (yalama) |
| C17 | 0.0-2.0 | sörf biraz iner (Khev'in alımı; C16 sonu −14 → −16) | hava | K2 | −16 | E13 |
| C17 | 0.5-2.8 | baş kalkar, kollar sabit: plaka | temas | K2 | −30 | E03 |
| C17 | 3.3 · 4.6 · 5.9 | Oru TAM çağrı, ışıklara oturur; N3 7.6'ya dek, üç ışık yanıkken cam üst harmonikleri 6.2-7.4 | canlı | K3 | −8 | R20 |
| C17 | 3.0-7.6 | Khev sessiz (nefes tutuldu) | — | — | — | — |
| C17 | 7.6-10.0 | dinleme boşluğu: çağrı yok, müzik yok, sırt kabarır | hava | K2 | −16 → −13 | E13 |
| C17 | 8.2 · 9.0 | sprey patlamaları | hava | K2 | −22 | E15 |
| C17 | 8.4-10.0 | J: anne dikkati, tonsuz, yükselir | canlı | K3 | −30 → −20 | R21 · E34 |
| C18 | 0.0-1.2 | Oru çağrısının yankısı (C17'den) | canlı | K3 | −24 → −40 | R20 (L) |
| C18 | 0.0-3.0 | dikkat tonu gezinir (perde sürüklenir; boş terasa bakış) | canlı | K3 | −22 | R21 · E34 |
| C18 | 3.0-6.2 | ton daralır, göz bebeği durunca D'ye kilitlenir | canlı | K3 | −22 → −18 | R21 |
| C18 | 6.8 · 8.0 · 9.2 | anne SICAK cevap, ışıklara oturur; N3 C19 1.5'e taşar | canlı | K3 | −8 | R22 |
| C18 | 0.0-10.0 | sprey perdesi: yatay hışırtı; sörf altta sürer | hava | K2 | −32 · −16 | E30 · E13 |
| C18 | 9.6 | alt göz kapağı yumuşar: hafif ıslak iç çekiş | temas | K2 | −30 | E22 |
| C19 | 0.0-1.5 | anne N3 kuyruğu yüzgeç rezonansına çözülür | canlı | K3 | −14 | R22 (L) |
| C19 | 0.4-10.0 | yüzgeç rezonansı (D): 4-7 s'de zirve | temas | K2 | −26 → −14 | E21 |
| C19 | 0.5-1.5 | sörf −16 → −28 düzleşir; altında sakin yalama | hava | K2 | −28 | E20 (sakin) |
| C19 | 5.0-5.6 | yüzgeç çıkıntıyla aynı seviyeye oturur: membran gıcırtısı | temas | K2 | −22 | E22 |
| C19 | 7.0-10.0 | ufuk sırtı: çok uzak alçak uğultu (saat sürüyor) | hava | K2 | −30 → −26 | E13 (uzak) |
| C20 | 0.0-10.0 | yüzgeç rezonansı sürer | temas | K2 | −16 | E21 |
| C20 | 0.0-2.5 | Oru kanat çırpar, kolların biraz üstüne yükselir; sarkık sol yüzgeç titrer | temas | K2 | −24 · −32 | E17 · E11 |
| C20 | 2.5-5.0 | kollardan sıyrılıp kısa, yumuşak süzülüş; çırpış yumuşar | temas | K2 | −26 | E17 |
| C20 | 5.0 | Oru yüzgecin çanak yüzeyine konar: ılık yüzeyde yumuşak "pat" | temas | K2 | −26 | E32 (yüzgeç) |
| C20 | 5.2-8.0 | **yüzgeç sarması**: ucu Oru'nun arkasında ve iki yanında yukarı-içe bükülür; atak yavaş, zirve 6.5-7.5, 7.8-8.0 yumuşak oturma; sıkışma, ıslak ses, sürtme yok (yardım okunur) | temas | K2 | −24 | E35 |
| C20 | 7.4-8.2 | Khev'in kolları açık ve boş, kalkmaz: uzun durgun nefes | canlı | K2 | −26 | E26 |
| C20 | 8.0-8.4 | Oru başını Khev'e çevirir | temas | K2 | −34 | E28 |
| C20 | 8.2 · 8.9 · 9.6 | Oru PARLAK çağrı, parlayan ışıklara oturur (aralık 0.7); N3 C21 0.6'ya dek | canlı | K3 | −8 | R23 |
| C20 | 8.4 · 9.3 | yüzgeç damarları atar: iki yumuşak ton dalgası | temas | K2 | −26 | E31 |
| C20 | 8.0-10.0 | ufuk sırtı çıkıntıya biraz daha yaklaşır | hava | K2 | −24 → −22 | E13 (uzak) |
| C21 | 0.0-0.6 | Oru N3 kuyruğu (C20'den) | canlı | K3 | −8 → −30 | R23 (L) |
| C21 | 0.1 · 1.0 · 1.9 | anne alçak cevap (D2 E2 A2, hissedilen), Oru N3 üstüne örtüşür; N3 2.7'ye dek | canlı | K3 | −14 | R24 |
| C21 | 0.35 | çaba kliği | canlı | K3 | −16 | R25 · E10 |
| C21 | 0.4-2.4 | taş sürtmesi yumuşak membrana döner; 2.6'da gövde yüzeye oturur | temas | K2 | −18 → −24 · −20 | E23 |
| C21 | 1.0-2.0 | sol bacak sürüklenirken (kadraj dışı) çatlak çıtırtısı | temas | K2 | −28 | E25 (çıtırtı) |
| C21 | 0.0-10.0 | yüzgeç rezonansı (anne cevabının sıcaklığı) | temas | K2 | −16 | E21 |
| C21 | 3.8-7.0 | rahatlama nefesi (omuzlar nefesle kalkıp iner) | canlı | K2 | −24 | E26 |
| C21 | 3.5-7.0 | köpük çizgisi ilerler | hava | K2 | −30 → −24 | E20 |
| C21 | 7.2 · 8.9 | yüzgeç damarları sıcak ışıkla atar: iki yumuşak ton dalgası (düzensiz aralık) | temas | K2 | −24 | E31 |
| C21 | 8.0-10.0 | J: dalga baskısı yükselir (C22'ye) | hava | K2 | −28 → −18 | E24 (ön kükreme) |
| C22 | 0.0-3.0 | yüzgeç itişsiz yükselir: hava + membran | hava | K2 | −22 | E07 · E22 |
| C22 | 0.0-3.0 | kükreme −18 → −10 | hava | K2 | −18 → −10 | E24 (ön kükreme) |
| C22 | 3.1-3.35 | darbe öncesi 0.25 s çöküş (kükreme −8 dB) | hava | K2 | −8 dB | — |
| C22 | 3.4 | DALGA boş çıkıntıya çarpar: darbe + sub | hava | K2 | **0** | E24 |
| C22 | 3.4-7.0 | yayılan kükreme: −6 → −14 (7.0'da −14; 7.6'da ≈−17: çözülme maskelenmez) | hava | K2 | −6 → −14 | E24 |
| C22 | 6.6-10.0 | anne sabit alçak ton (D), 7.6'da çözülmenin altına girer; 10.0'dan sonra 1.5 s söner (C23 1.5) | canlı | K3 | −14 | R26 · E06 |
| C22 | 7.0-10.0 | sprey dağılır; 8.0-10.0 su çekilir | hava | K2 | −14 → −28 · −24 | E15 · E20 |
| C22 | 8.0-10.0 | yükseliş rüzgârı | hava | K2 | −30 | E29 |
| C23 | 0.0-1.5 | sprey kuyruğu | hava | K2 | −28 → −40 | E15 (L) |
| C23 | 0.0-1.5 | R26 anne tonunun sönüşü (Y2 perdesiz zemin altında) | canlı | K3 | −14 → −40 | R26 (L) |
| C23 | 0.0-4.0 | uzaklaşan okyanus kalıntısı (aşağıda) | hava | K2 | −30 → −50 | E13 (uzak) |
| C23 | 0.0-10.0 | yüzgeç damar parıltısı, sis akışı | temas | K2 | −26 · −34 | E31 · E29 |
| C23 | 3.2 · 4.2 · 5.2 | Oru TAMAMLANMIŞ ifade (ılık, vibratosuz) | canlı | K3 | −18 | R27 |
| C23 | 3.6 | Oru'nun başı ön kola değer: kuru yumuşak temas | temas | K2 | −28 | E03 |
| C23 | 4.2 · 6.5-10.0 | Khev'in omuzları iner: uzun rahat nefes; sonra düzenli sakin nefes (filmde ilk düzenli) | canlı | K2 | −22 · −28 | E26 |
| C23 | 6.0-10.0 | Oru nefesi | temas | K2 | −34 | E28 |
| C23 | 9.0-10.0 | J: anne ön nefesi (C24'e) | canlı | K3 | −28 → −20 | E05 (kısa) |
| C24 | 0.0-10.0 | yüksek rüzgâr, geniş stereo; kıyı küçüldükçe açılır | hava | K2 | −34 → −28 | E29 |
| C24 | 0.0-3.0 | uzak sörf solar | hava | K2 | −40 → yok | E13 (uzak) |
| C24 | 1.0 · 3.0 · 5.0 | anne motifi tamam (D3 E3 A3): yavaş üç nota, N3 9.0'a dek tutulur | canlı | K3 | −8 | R28 |
| C24 | 4.0 · 6.5 | yüzgeç hafif esner | temas | K2 | −30 | E22 |
| C24 | 6.0-7.2 | Oru'nun tek ince notası (A5), anne N3'ü üstünde: oktav kaynaşması; müzik girişi bunun bitişinde (7.2) | canlı | K3 | −22 | R29 |
| C24 | 8.8-9.8 | şafak kenarı bir kademe parlar: **L2 cam notası taşır (K4); ses efekti yok.** Yedek koşulu: L2 notası 8.4-9.2'de duyulmuyorsa E27 −28'de eklenir (F8 kararı) | hava | K2 | −28 (yedek) | E27 (koşullu) |
| C24 | 9.0-10.0 | doğal kuyruk; 9.85-10.0 kapanış tıkırtısını önleyen hızlı iniş | — | — | −40'a | — |

### 5b. Sörf saati (özet; satırlar yukarıda)

```
C01-C06   yatakta uzak okyanus (yok olarak sayılır)        C14  −20     C19  −28 (düz) ← kuralın kulaktaki yarısı
C07       −32 → −18 → −14 (tek geniş sırt)                  C15  −30 → −22 (köpük)   C20  −24 → −22 (uzak sırt, 8-10 s)
C08       −24 (vuruşlar)                                    C16  −22 → −14           C21  −30 → −24, J: −28 → −18
C09       −26 → −18 · uzak sırt −26 → −22                   C17  −16 → −13           C22  −18 → −10 → 0 (3.4) → −6 → −14
C10       −22 → −14 → kopuş −5                              C18  −16                 C23  −30 → −50 (kalıntı)
C11 C12   −24                                               C13  −24 → −22           C24  −40 → yok
Sörf düzensizdir: vuruş aralıkları 6-14 s arasında değişir, hiçbir yerde periyodik darbe yok. Müzik nabzı (66-96, 202.6-226.5) ayrı bir saattir ve sörfe ait değildir.
Kurgu.py'de `ses` listesine 1 s `solma` ile parçalanmış segmentler olarak girer (ses/sorf_saat.wav, ≈165 s (59.0-224.0), döngüsüz;
30 s'lik altı üretim 3 s çapraz geçişle birleştirilir; tur 1'deki "150 s" C07-C23 aralığına yetmiyordu).
```

## 6. ORTAM YATAĞI (FILM.md §6'ya taşınır)

Mekân = ses mekânı. Kıyı (kemer, teras, geçit, alt çıkıntı, göğün altındaki göz planları) tek denizin ve tek rüzgârın altında olduğundan **tek yatak**tır; kemer altı, alt çıkıntıya yakın sörf ve yüzgeç rezonansı yatağın üstüne **K2 efekti** olarak biner (yatağı değiştirmez, kesmede "yeni oda" doğurmaz). İkinci yatak yalnız mekân gerçekten değişince: anne yüzgecinin üstü ve yukarısı. Yatak ritimsizdir: kalp atışı, nabız, periyodik darbe yok (nabız yalnız müziğe aittir).

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | KIYI: kemer · teras · geçit · alt çıkıntı · gök ve deniz (C05 C18 göz planları dahil) | C01-C22 (0.0-220.0) | `low steady night wind over black basalt and a vast slow ocean swell far away, soft irregular water wash on distant rocks, open air, no rhythm, no birds, no insects, no voices, no music, seamless loop` | −20 LUFS | `ses/yatak_kiyi.wav` |
| Y2 | YÜZGEÇ-HAVA: annenin yüzgecinin üstü, deniz sisinin üstü, bulut tepeleri | C22 7.0 - C24 (217.0-240.0) | `a wide pitchless soft rumble of an enormous living body, airy membrane texture, thin high-altitude wind, faint ocean far below, slow irregular swells, no tonal drone, no pulse, no heartbeat, no voices, no music, seamless loop` | −22 LUFS | `ses/yatak_yuzgec.wav` |

```
Y1  120 s'lik dikişsiz döngü ya da 220 s tek parça; rüzgârda ve uzak sörfte periyot yok. Stereo: iki kanal ilintisiz, sağ biraz ağır (deniz sağda). Mono toplamda ≤2 dB kayıp.
Y2  PERDESİZ geniş bant (hakem B14; tur 1'deki "D çevresinde 73-147 Hz" kalktı). D'yi Y2 değil R26 (216.6-221.5) ve sonra müzik taşır; ses:397'nin sorusu böyle kapandı.
    Mono toplamda ≤2 dB kayıp.
Geçiş  Y1 → Y2: 217.0'da Y2 girer (1 s), Y1 219-220'de solar (1 s); 217-220 arası ikisi üst üste, çapraz geçiş C22 sonuna oturur. Dönüş yok.
       Sprey kuyruğu (K2, L 1.5 s) 221.5'e dek Y2 üstünde biter. Film sonu: Y2 son 1 s solar (−40'a); çağrı ve müzik kuyruğu 239.85'e dek doğal.
timeline.json yataklar:
  {"dosya": "ses/yatak_kiyi.wav",    "baslangic": 0.0,   "bitis": 220.0, "kazanc_db": 0, "gecis": 1.0}
  {"dosya": "ses/yatak_yuzgec.wav",  "baslangic": 217.0, "bitis": 240.0, "kazanc_db": 0, "gecis": 1.0}
Yatak dosyaları −20 / −22 LUFS'ta hazırlanır; kazanç timeline'da değil dosyada. Dijital sıfır hiçbir yerde yok (Y1/Y2 örtüşmesi 217-220; ilk 1 s Y1 fade-in'i K2 göz kapağı gıcırtısı ve 1.2 adımı örter).
Müziksiz anlarda (0-22, 40-58, 126-140, 161.5-179.4) oda tonunu yatak taşır; 130.0 ve 170.0 kesmelerinde yatak kopmaz (KORU 1).
```

## 7. GEÇİŞ (FILM.md §6 taslağı · F8'de kurgucu kesinleştirir)

Ön karar (kurgucu F3): 23 kesmenin 23'ü `kesme`; sahip planı "düz kesmelerle 240 s" der ve her geçiş filmi süresi kadar kısaltır. Ses bunu kabul eder: süreklilik geçişle değil **köprüyle** sağlanır. Müzik hiçbir kesmede kesilmez; müziğin iki sessizliği (126.0-140.0 ve 161.5-179.4) 130 ve 170 kesmelerini kapsar, rastlantıyla düşmez.

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1 kesintisiz · L 1.2 s anne nefesi kuyruğu | XW → MC: ölçek sıçraması; yatak sürer (ILK_30 §5) |
| C02→C03 | kesme | Y1 · J 1.2 s gök basıncı (C02 8.8'den) | MC → XW; sessizlikten (dinleme) dev hareketine hazırlık |
| C03→C04 | kesme | Y1 · L 1.0 s yüzgeç havası; anne tonu 0.6 s taşar | kurgucu önerisi; yön tersi (Khev geri çekilir) sesle yumuşar |
| C04→C05 | kesme | Y1 · J 1.5 s dikkat şişmesi (C04 8.5'ten), ilk nota ışıkla | kurgucu önerisi; renk sıçraması (kemer gölgesi → amber göz) sesle köprülenir |
| C05→C06 | kesme | Y1 · L 0.8 s soğuk salon yankısı; açık hava genişlemesi | gövdenin açığa çıkışı kesmede; ses "kapalı salondan açık denize" |
| C06→C07 | kesme | Y1 · J 1.0 s su kükremesi (C06 9.0'dan) | aşırı benzer açı riski (B6): ses süreği taşır |
| C07→C08 | kesme | Y1 · L 1.5 s sırt kükremesi sörfe akar | açı büyük, ölçek aynı |
| C08→C09 | kesme (hareket üstü) | Y1 · adım sesi C08 7.6 → C09 0.6; kemer tonu C09 0.8-2.3 solar | Khev iki çekimde gölge çizgisinde: kesme hareketin üstüne |
| C09→C10 | kesme | Y1 · J 1.0 s taş gıcırtısı (C09 9.0'dan) | kurgucu önerisi; sebep-sonuç sesle bağlı |
| C10→C11 | kesme | Y1 · L 1.5 s su çarpması ve sprey kuyruğu | kurgucu önerisi; yolun kapanışı boş ellere akar |
| C11→C12 | kesme | Y1 · düşen ıslık 9.9'da kesilir, iniş sesi C12 0.15 | düşüş kesmede: ses öncesi-kesme-sonrası'nı bağlar |
| C12→C13 | kesme | Y1 · L 1.0 s Oru'nun zayıf çağrısı (C12 9.15) | kurgucu önerisi; Khev duyuyor, 0-2.5 s aşağı bakıyor |
| C13→C14 | kesme · **SERT SES KESMESİ (planlı)** | Y1 sürer · rüzgâr 9.75'te biter, 0.25 s yalnız yatak, iniş C14 0.0 | atlayış ve iniş kesmede, ses nedenle sonucu bağlar; kesme müziksizliğin (126.0-140.0) ortasında |
| C14→C15 | kesme | Y1 · L 0.8 s Khev nefesi ve Oru'nun solgun üçüncü izi (139.4-140.2) | jump-cut riski (B1): ses kesmeyi örter; tek D 140.0-140.3'te, iz sönerken girer |
| C15→C16 | kesme | Y1 · J 0.8 s sörf yükselişi (C15 9.2'den) | saat sürüyor |
| C16→C17 | kesme | Y1 · bakış eşleşmesi; sörf C17 0.0-2.0'da −2 dB iner (Khev'in alımı) | sessizlik Oru'nun çağrısına yer açar; müzik 161.5'te (kesmeden 1.5 s sonra) planlı çıkar |
| C17→C18 | kesme | Y1 · L 1.2 s Oru yankısı + J 1.6 s anne dikkati (C17 8.4'ten) | kurgucu önerisi (genişletildi): 9.2 s'lik aranma tonsuz dikkatle taşınır; 170 kesmesi müziksizlikte |
| C18→C19 | kesme | Y1 · L 1.5 s anne N3'ü yüzgeç rezonansına çözülür (aynı perde D) | cevap → köprü; ses "yüzgeç annenin sesidir" der; F♯ 179.4 bu köprünün içinde |
| C19→C20 | kesme | Y1 · L 1.0 s yüzgeç rezonansı | B6 sınır kesmesi: ses sürekliliği taşır |
| C20→C21 | kesme | Y1 · L 0.6 s Oru N3 kuyruğu; anne cevabının ilk notası C21 0.1'de girer (cevap C21'in sesi, taşma değil) | Oru'nun geçişi ve Khev'in geçişi iki ayrı bilgi, tek sesli cümle; kesme cevabın hemen öncesine düşer |
| C21→C22 | kesme | Y1 · J 2.0 s dalga baskısı (C21 8.0'dan) | kurgucu önerisi; saat |
| C22→C23 | kesme | Y1 → Y2 çapraz 217-220 · L 1.5 s sprey · anne sabit tonu 221.5'e dek sürer | tek yatak değişimi; kıyı geride kalır |
| C23→C24 | kesme | Y2 · J 1.0 s anne ön nefesi (C23 9.0'dan); rüzgâr geniş stereoya açılır | MC → XW kasıtlı ölçek sıçraması; ses genişleyerek taşır |

## 8. MÜZİK İÇİN SES KISITLARI (besteci tur 2 bu bölüme göre kurulur)

Hakem kararları işlenmiş hâlidir. Mutlak saniye = 10 × (Cxx − 1) + saniye. Çağrı pencerelerinde müzik **−9 dB** altındadır ya da yoktur; müzik yatağı **−18 LUFS-S** (B19).
Saat çatışmasında ses saati esastır (hakem ilkesi): aşağıdaki sayılar çağrı ve efektin nominal saatleridir; besteci yalnız tepkisini kaydırır. Hakem tablosundaki bir sayıdan ayrılan yerler işaretli.

```
MÜZİKSİZ (zorunlu)
  0.0-22.0         C01 · C02 · C03'ün ilk 2 s: göz, ilk çağrı, tonsuz ses. L1 22.0'da çok alçak girer (B13; ILK_30 §5).
  40.0-58.0        C05 · C06'nın ilk 8 s: soğuk çağrı, akrabalık anı, sıcak üst üste (B1). M ilk kez 58.0'dan sonra, ≤ −12 dB: cam M 58.0, çello M 59.2;
                   60 kesmesine tutulan küme korunur.
  126.0-140.0      C13 6.0'dan C15 0.0'a: karar, atlayış, iniş, bedel (B6, B20). Susma yay-kalkışı gibi 10-30 ms rampa, kuyruk yok. Karar kliği (126.6) sessizlikte duyulur.
                   Tek D 140.0-140.3 arasında, R16'nın üçüncü izi (139.4, L kuyruğu 140.2) sönerken girer.
  161.5-179.4      C17 1.5'ten C18 9.4'e: Oru'nun tam çağrısı, dinleme boşluğu, tonsuz dikkat, anne cevabı (besteci susku 2; hakem B8: F♯ 179.4). 170 kesmesi içinde.

MÜZİKSİZ TERCİH (ses isteği; hakem tablosunda yok ya da yumuşatılmış)
  97.0-98.6        C10 7.0-8.6: kırılma (97.2), düşüş, ağır çarpma (98.1). Nabız 96.0'da durdu; L1'in bu aralıkta çıkması ya da ≤ −12 dB'e inmesi istenir (kurgucu S3 sayımında
                   besteci L1 çalıyor; B listesinde ayrı madde değil, AÇIK KARAR 6). Müzik VURUŞU hiçbir koşulda yok.
  212.8-217.6      C22 2.8-7.6: dalga darbesi (213.4) ve yayılan kükreme (B10). Hakem: A sus ≤ −9 dB ya da yok; P ≤ −9 dB; 213.1-213.8'de P vuruşu yok.
                   Çözülme 217.6'da (sprey dağılışı 217.0 + 0.6), anne tonu D 216.6'da girdikten 1.0 s sonra.

ÇAĞRI PENCERELERİ (müzik ≤ −9 dB, tercih yok; müziksiz bölgelerdekiler ayrıca anılmaz)
  4.6-11.2 · 13.2-17.4 · 40.9-49.6 · 52.0-56.4 · 126.6-127.0 · 131.3-132.2 · 137.2-140.0 (R16 izinin 140.0-140.2 kuyruğunda tek D yumuşak girer) · 163.3-176.2 · 176.8-179.4   zaten müziksiz
  25.6-29.4        C03 R04 anne tek ton (D3 + D2): L1 D'yi bırakır, yalnız A3 (B14); ≤ −9 dB
  36.5-37.2        C04 R06 korku ıslığı
  75.0-77.4        C08 R09 (P + L1, −9 dB)
  86.5-88.4        C09 R10 (86.6-88.2 + 0.2 pay; tur 1'deki "86.5-87.8" aritmetik hataydı; P + L1, −9 dB)
  100.8-107.0      C11 R11 · 106.6-110.0 solgun inen ıslık: M ve L1 ≤ −9 dB, M'nin notaları 500 Hz altında
  111.0-113.0 · 119.0-121.0   C12 R12 R13 (tek D ≤ −30 LUFS-S ya da yok; tercih yok) · 113.8-116.2 sönük nota izleri: D ≤ −30
  140.8-144.0      C15 R17 (hakem 140.8-143.0; üçüncü nota 143.0'da başlar, tutuşu 143.8'e dek sürer → 144.0): tek D ≤ −9 dB
  153.0-156.7      C16 R18 tarama (153.3-155.7) + 1 s cevapsız boşluk: tek D yok ya da ≤ −9 dB; A ≥ 157.0 (hakem: ≥156.5)
  195.0-198.2      C20 yüzgeç sarması (E35, −24): D add9 −6 dB, müzikte vuruş yok
  198.2-203.0      C20-C21 R23 (198.2-200.6) + R24 (200.1-202.7) + DEV kuyruğu: D add9 ≤ −9 dB (hakem 199.0-200.8'i eski R24 saatiyle yazmıştı)
  223.0-226.4      C23 R27: L1 ≤ −9 dB; L3 220.0'da çıktı
  231.0-239.0      C24 R28 anne motifi: L1 ≤ −9 dB (çağrı üstte, harmoni altta); 236.0-237.2 R29 (A5) bitene dek L2 yok
  237.2-239.0      L2 cam + yüksek yaylı girişi: bant ayrımıyla (cam 1.2 kHz üstü, anne ≤ 900 Hz) girebilir; çözülme 238.0'da

SFX ZİRVELERİ (müzik vuruşu yok; seviye ≤ −9 dB ya da yok)
  97.0-99.0 (kırılma, çarpma) · 130.0-131.4 (iniş, çatlak; zaten müziksiz) · 213.1-214.5 (dalga)

MÜZİK ALANI (ses açısından serbest; yukarıdaki pencereler hariç)
  22.0-40.0        C03 2.0 - C04: L1 (A3) çok alçak; L2 ≈24.5-33; D yok (25.6-29.4)
  58.0-97.0        C06 sonu - C10 7.0: M ≤ −12 dB (58-60); L3 F 62.0; nabız 66.0'da başlar (anne durma bırakışı 64.2-66.0'da vuruş yok), 96.0'da durur; koyulaşma 88.4'ten
  98.6-126.0       C10 sonu - C13 6.0: L1 yalnız; M kırık 107.5, E 110.0'a dek; C12 tek D ≤ −30 LUFS-S
  140.0-153.0 ve 157.0-161.5   tek D (140.0'dan); A ≥ 157.0; 157.0-161.5 yalnız 4.5 s'lik pencere (AÇIK KARAR 7)
  179.4-212.8      F♯ 179.4; L1 yükselişi 185.6'dan (D2 yok, A3 + F♯ + E), D add9'a 190.0'da varır; L2 E 187.0; P 202.6'da (anne kalp atışı); M BÜTÜN 203.5'te; IV'e kayış ve D'ye dönüş bir adım sonra
  217.6-240.0      çözülme 217.6; L3 220.0'da çıkar; P 226.5'te çıkar; L2 + yüksek yaylı 237.2'den; ikinci çözülme 238.0; 240.0 kesme (239.85'e dek doğal sönüş, 239.85-240.0 rampa)

MÜZİKSİZ TOPLAM  zorunlu 71.9 s (22.0 + 18.0 + 14.0 + 17.9) · tercihlerle 78.3 s (%32.6). Besteci tur 1'de 45.0 s planlamıştı (hakem B1 B6 ve ses saatleri bunu büyüttü).
```

### 8b. ÇAĞRI–MÜZİK SAAT TABLOSU (besteci §4'ün kaynağı, B18)

Mutlak saniye; 28 aktif satır, R19 düştü. "Pencere" = müziğin ≤ −9 dB ya da yok olduğu aralık; "Müzik" = o anda planlanan durum.

| R | Çağrı (mutlak) | Pencere | Müzik durumu |
|:--:|---|---|---|
| R01 | 4.6 / 5.5 / 6.4 (N3 → 7.2) | 0-22 | müziksiz |
| R02 | 7.4-11.2 (zirve 8.8-9.2) | 0-22 | müziksiz |
| R03 | 13.2 / 14.6 / 16.0 (N3 → 17.4) | 0-22 | müziksiz |
| R04 | 25.6-29.4 | 25.6-29.4 | L1 yalnız A3 (D yok), ≤ −9 dB |
| R05 | 30.0-40.0 (38.5'ten −18'e) | — (tonsuz) | L1 (A3); tonsuz uğultu altında perdeli müzik ince |
| R06 | 36.5-37.2 | 36.5-37.2 | L1 ≤ −9 dB |
| R07 | 40.9 / 42.5 / 44.1 · küme 45.0-47.0 · sub 47.2-49.6 | 40.0-58.0 | **müziksiz** |
| R08 | 52.0 / 52.9 / 53.8 · anne +0.05 (N3 → 56.4) | 40.0-58.0 | **müziksiz** |
| R09 | 75.2-77.0 | 75.0-77.4 | nabız + L1, ≤ −9 dB |
| R10 | 86.6-88.2 | 86.5-88.4 | nabız + L1, ≤ −9 dB; P fazı adımlardan (82.0, 85.0) ≥0.25 s; koyulaşma 88.4'ten |
| R11 | 101.0 / 102.0 / 103.3 (çöker → 106.6) · inen ıslık 106.6-109.9 | 100.8-110.0 | L1 yalnız ≤ −9 dB; M kırık 107.5 (D–E, 500 Hz altı), E 110.0'a dek |
| R12 | 111.4-112.4 · izler 114.0 / 114.6 / 115.7 | 111.0-113.0 · 113.8-116.2 | tek D ≤ −30 LUFS-S ya da yok |
| R13 | 119.15-119.95 (L → 121.0) | 119.0-121.0 | tek D ≤ −30 LUFS-S ya da yok |
| R14 | 126.6-127.0 | 126.0-140.0 | **müziksiz** |
| R15 | 131.3-132.2 | 126.0-140.0 | **müziksiz** |
| R16 | 137.2-138.0 · 138.6-139.4 · iz 139.4 (→ 140.2) | 126.0-140.0 | **müziksiz**; tek D 140.0-140.3'te girer |
| R17 | 140.8 / 141.9 / 143.0 (N3 → 143.8) | 140.8-144.0 | tek D ≤ −9 dB (hakem 143.0; ses saati 144.0) |
| R18 | 153.3-155.7 (+ cevapsız 1 s → 156.7) | 153.0-156.7 | D yok ya da ≤ −9 dB; A ≥ 157.0 |
| R19 | — | — | **DÜŞTÜ** |
| R20 | 163.3 / 164.6 / 165.9 (N3 → 167.6) | 161.5-179.4 | **müziksiz** |
| R21 | 168.4-176.2 (dikkat, tonsuz, D'ye kilit 176.2) | 161.5-179.4 | **müziksiz** |
| R22 | 176.8 / 178.0 / 179.2 (N3 → 181.5) | 176.5-181.5 | müziksiz 179.4'e dek; F♯ 179.4 (≤ −9 dB, N3 üstünde; duyulmazsa −6, §10) |
| R23 | 198.2 / 198.9 / 199.6 (N3 → 200.6) | 198.2-203.0 | D add9 ≤ −9 dB; sarma 195.0-198.2'de −6 dB |
| R24 | 200.1 / 201.0 / 201.9 (N3 → 202.7) | 198.2-203.0 | D add9 ≤ −9 dB; **P 202.6** (N3 sonu 202.7'yi aşarsa N3 sonu + 0.1) |
| R25 | 200.35-200.65 | 198.2-203.0 | ≤ −9 dB |
| R26 | 216.6-220.0 (söner → 221.5) | 212.8-217.6 | A sus ≤ −9 / yok; **çözülme 217.6** R26'nın D'si üstüne; R26 217.6'da −14 → −18 |
| R27 | 223.2 / 224.2 / 225.2 (→ 226.2) | 223.0-226.4 | L1 ≤ −9 dB; P 226.5'te çıkar |
| R28 | 231.0 / 233.0 / 235.0 (N3 → 239.0) | 231.0-239.0 | L1 ≤ −9 dB; L2 + yüksek yaylı 237.2'den; ikinci çözülme 238.0 (A3 ortak nota) |
| R29 | 236.0-237.2 | 236.0-237.2 | L2 girişi bitişinde (237.2); F♯ üst ses 237.2 |

Müzik olaylarına bağlanan ses referansları (SFX, mutlak): ilk ses 0.0 · yüzgeç havası zirvesi 27.0 · başlık (kurgu yazısı) 27-30 · taş kırılması 97.2, çarpma 98.1 · karar kliği 126.6, itiş 128.0, iniş + çatlak 130.0 · yüzgeç oturur 185.0-185.6 (membran gıcırtısı, L1 yükselişi bundan sonra) · sarma 195.2-198.0 · Khev'in yüzgece oturuşu 202.6, rahatlama nefesi 203.8 · dalga 213.4 · sprey dağılışı 217.0 · Khev'in ilk düzenli nefesi 226.5 · şafak kenarı kademesi 238.8-239.8.

### 8c. BANT · D SAHİPLİĞİ · NABIZ · SEVİYE

```
BANT         Oru: temel 587.3-880.0 Hz (E5 659.3), cam üst harmonikleri 4 kHz'e dek. Anne: temel 146.8-220.0 Hz, 2.-4. harmonikler 900 Hz'e dek (telefon payı).
             Müziğin 500-4000 Hz bandı çağrı pencerelerinde çekilir (≤ −9 dB). MÜZİK PROMPTU satırı (B4): "Keep the 500-4000 Hz band open for creature calls and ocean
             sound; glass tones stay sparse and above 1.2 kHz". 55 Hz altı yok, infrases yok. Nabız gövdesi ≈100-130 Hz: anne alçak cevabının (73-110 Hz) üstüne binmez (202.6'dan sonra girer).
D SAHİPLİĞİ  (B14: aynı perde aynı bantta iki kaynak olmasın)
             25.6-29.4    R04 anne tonu (ses) · L1 D yok, A3
             140.0-153.0  L1 tek D (müzik) · ses tarafında D3 harmonikleri R16/R17 N1'iyle (D5) çakıştığı için R17 penceresi −9 dB (140.8-144.0)
             180.4-210.0  E21 yüzgeç rezonansı D (ses) · L1 D2 yok (A3 + F♯ + E üst yapı); gerekirse E21 −3 dB
             216.6-221.5  R26 anne tonu D (ses) · çözülme (müzik) aynı D'ye iner: kasıtlı birleşme
             221.5-240.0  D'yi müzik taşır · Y2 perdesiz geniş bant (D çevresinde değil)
NABIZ        İki rolde (§0). 66.0-96.0 deniz saati: 60 BPM serbest, kuru, tok, 96.0'da kuyruksuz durur. 202.6-226.5 anne kalp atışı: yuvarlak, sıcak, aynı tempo;
             212.5-217.6 ≤ −9 dB; 213.1-213.8'de vuruş yok. 156.0 ve 161.0 çıpaları kalktı. P fazı F8'de seçilen denemenin gerçek adım zamanlarından ≥0.25 s kaydırılır (B15).
SEVİYE       Müzik yatağı −18 LUFS-S; çağrı penceresinde −9 dB (B19). Y1 −20 · Y2 −22 LUFS-S. Müzik vuruş ya da giriş/çıkışları 10-30 ms rampa ile kesilir, fade-out yok.
```

## 9. FİNAL MİKS — YÜKSEKLİK HEDEFİ

```
HEDEF       −14 LUFS integrated · ≤ −1 dBTP · stereo 48 kHz · mono uyumluluğu kontrol edilir.
YÖNTEM      1) taslağı kur (klipler sessiz + yataklar + `ses` parçaları + müzik)
            2) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4>                    (ölç)
            3) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4> --uygula -o final.mp4
            İki aşamalı, doğrusal: sıkıştırma yok; sessizlik ile darbe arasındaki fark ezilmez.
KISA VADE   Y1 −20 LUFS-S · Y2 −22 · Oru ve anne çağrı zirveleri ≈ −12 LUFS-S (yataktan ≥ +8 LU) · C22 dalga ≈ −8 LUFS-S · müzik çağrısız −18 LUFS-S (B19), çağrı altında −9 dB.
ZİRVELER    C22 dalga (0) · C14 iniş (−6) · C10 kırılma (−6) ve çarpma (−5) · çağrı zirveleri (−8). −14'e çıkarken zirve tavana önce varırsa sıkıştırma EKLENMEZ;
            C22 / C14 / C10 efektleri kaynakta en çok 3 dB indirilir, çağrılar korunur.
DİKKAT      Müzik yatağı integrated ölçümü taşır, ama müziksiz bölüm artık 71.9-78.3 s (§8): C01-C03, C05-C06, C13-C14, C17-C18 (ve C10 sonu, C22 ortası). Bu bölümler
            yatak + efektle ~−22 LUFS-S'dir; ölçüm −15'in altında çıkarsa müzik yatağı +1…2 dB yükseltilir (−18 → −16…−17, kural 8 aralığı içinde), sıkıştırma eklenmez.
            Sesi düşük teslim etmek en ölümcül hatadır: platform kısar, açmaz.
KORUNAN     C12 (≈ −26 LUFS-S, yalnız Oru'nun nefesi ve yatak; tek D ≤ −30) ile C22 darbesi (≈ −8 LUFS-S) arasındaki fark ve C19 sörf düşüşü (−16 → −28) ezilmez.
TELEFON     Düşük frekanslı her ses (anne, sörf, yüzgeç rezonansı, okyanus rezonansı) 300-2500 Hz'de ≥ −6 dB orta bant payı taşır; telefon hoparlöründe anne çağrısının
            C06 / C18 / C24'te duyulması şartı (D3 E3 A3 temelleri 147-220 Hz). C20-C21 alçak cevabı (D2 E2 A2) yalnız harmonikleriyle telefonda duyulur; F8'de sınanır.
MONO        Y1 / Y2 ilintisiz stereo: mono toplamda ≤2 dB kayıp. Oru çağrıları merkez (±0.2, kadraj konumunu izler); anne gövde katmanı merkez, yalnız yankı geniş.
            Sörf ve kükreme sağ ağırlıklı (deniz sağda), kemer tonu sol, C07 sırtı sağdan sola yürür, C24 geniş. C20 sarma sesi (E35) sağ, yüzgeç tarafı.
SON KONTROL Final baştan sona kulaklıkta ve telefon hoparlöründe dinlenir. Oru'nun üç hâli (ince / zayıf / tam) ayırt edilmeli; anne SOĞUK (C05) ile SICAK (C06) farkı kulakla okunmalı.
```

## 10. DİNLEME ÖLÇÜLERİ (F8) VE AÇIK KARARLAR

1. **Akrabalık sesle okunuyor mu (C05 → C06):** F3'ün açık ÖLÜMCÜL'ü. F8 ANLATIM_TESTI sesli iki sürüm: 40-58 müziksiz (varsayılan) / L1'li. "Gökteki şey Oru'nun nesi?" Okunmazsa sırayla: C06'da anne +2 dB ve Oru −2 dB (kaynaşma), sonra C05'in soğuk hâli daha belirgin (−25 → −40 cent), son çare C06 çağrısının ikinci tekrarı (6.8-8.0 boşluğuna kısa üçüncü eşleşme).
2. **Işık-nota eşleşmesi (C02 C05 C17 C18 C20 C23):** ±0.1 s. Seçilen denemede ışık anları 24 fps kare kare okunur; ışık sırası soldan sağa değilse (model karıştırırsa) nota sırası ışığa uyarlanmaz, deneme değiştirilir. **C20 özel:** ışıklar zaten yanık ve 8-10 s'de parlar; nota başı parlama başlangıcına oturur (nominal 8.2). Pilot C20 geldiğinde parlamanın gerçek saati ölçülür; ≥0.5 s sapmada R23, R24 ve P 202.6 zinciri birlikte kayar (R24 N3 sonu + 0.1 = P).
3. **C13 → C14 sert kesme (0.25 s boşluk):** "kopuk" mu "nefes" mi? Kopuk duyulursa boşluk 0.1 s'ye iner; yumuşak duyulursa iniş 0.05 s öne alınır.
4. **C19 sörf düşüşü:** "kural" okunuyor mu (yüzgeç altındaki su neden sakin)? Okunmazsa düşüş 1.5 s'ye yayılır, sakin yalama +3 dB.
5. **C22 dalga:** tavan ve kırpma; −14 LUFS'a çıkarken (bkz. §9). Çözülme 217.6'da kükremeye karşı duyuluyor mu: kükreme zarfı 217.0'da −14 → 217.6'da ≈−17.
6. **Khev'in sesi:** klik + solungaç nefesi insan gibi duyuluyorsa (nefes) E26 daha kâğıtsı ve alçak yapılır; insan nefesi film boyu yok (plan: "insan bebek ağlaması ve anlaşılır konuşma yok").
7. **Telefon:** anne çağrısının C06 / C18 / C24'teki orta bandı (§3 TELEFON PAYI); duyulmuyorsa 2. harmonik +3 dB.
8. **C16 cevapsız tarama:** "cevapsız" mı yoksa "bitmeyen" mi duyuluyor? Bitmeyen duyulursa tarama bitişi 0.3 s daha keskin, sonra 1 s boşluk. Tek D pencerede (153.0-156.7) yoksa ve boşluk "arıza" gibi duyuluyorsa D ≤ −9 dB'e geri alınır.
9. **C20 sarma sesi (E35):** "yardım" mı "tuzak" mı duyuluyor? Tuzak duyulursa atak daha yavaş, düşük orta bant (200-600 Hz) +2 dB, 7.8-8.0 oturma daha açık; sıkışma izlenimi veren her yüksek frekans çıkarılır. Müzik −6 dB altında sarma duyulmuyorsa D add9 195.0-198.2'de −9 dB.
10. **F♯ 179.4:** −9 dB'de N3 (A3) altında duyuluyor mu? Duyulmuyorsa −6; yine duyulmuyorsa F♯ 181.5'e (N3 sonu) kaydırılır (kurgucu B8 yedeği, "tek başına" yolu).
11. **C24 şafak kademesi (238.8):** L2 cam notası 238.4-239.2'de duyuluyor mu? Duyulmuyorsa E27 −28'de eklenir (§5 C24 yedek satırı); Flow Music çıktısı bu hassasiyette garanti değil.
12. **R24 ↔ P 202.6:** anne alçak cevabının N3'ü ile P arasında maskelenme var mı? Varsa P N3 sonundan 0.1 s sonra, M BÜTÜN 203.5'te kalır.

```
AÇIK KARARLAR (Fable'a)
1. Tonalite: KAPANDI. D–E–A (hakem B3); besteci D; çağrı kaydı kaydırması yok.
2. C24'te Oru'nun tek ince notası (R29, oktav kaynaşması): hakem B11 bu satıra dayanıyor (müzik girişi R29 bitişinde, 237.2); fiilen kabul edilmiş sayılır.
   Planın "warm adult motif completes" cümlesine ek ses; olay eklemesi değil. Sahip onayı gerekmez ama bilgi olarak PLANDAN SAPMA'ya eklenebilir.
3. Altyazı: FILM §5 "gerekmez", ILK_30 §4 otomatik altyazıdan kaçınmak ister (kurgucu açık soru 2). Ses etiketli altyazı dosyası istenirse bu planın çağrı adları etiket olur:
   [glassy three-note call] · [immense low breath] · [low resonance] · [wave impact]. Sahip kararı.
4. Y1 başlangıç fade-in'i: gecis 1.0 (varsayılan). İlk saniyenin sessiz kalması endişe yaratırsa Y1 gecis 0.5'e iner, K2 göz kapağı gıcırtısı aynı kalır.
5. Ses aracı: çağrılar perde tutan araç ister (§3 notu); yatak ve foley için Flow Mondo Sónico denenebilir (P12 ölçülmedi, ticari koşul BİLİNMİYOR) ya da lisanslı kütüphane. Araç sahibin.
6. (YENİ) 97.0-98.6 müziksiz isteği: besteci L1 yalnız çalıyor (kurgucu S3 sayımı, 1.6 s); hakem tablosunda ayrı madde yok. Ses isteği: vuruş yok, L1 çıkar ya da ≤ −12 dB. Karar Fable'ın.
7. (YENİ) 157.0-161.5 müzik penceresi yalnız 4.5 s: besteci A ve L3 F için fazla kısa bulursa tek D'yi 161.5 susmasına dek taşıyıp A'yı atlayabilir (ses için fark etmez).
8. (YENİ) C20 ışık saatleri modelin vereceği parlamaya bağlı: R23/R24 ve P 202.6 zinciri pilot C20 sonrası kare kare ölçülüp kesinleşir (madde 2).
```

## 11. PLANIN "Sound:" SATIRLARI → BU PLAN (eşleme)

| Çekim | Plan satırı (özet) | Bu planda | Değişiklik |
|:--:|---|---|---|
| C01 | üç camsı ıslık · devasa alçak cevap nefesi · orta frekans dokusu | §5 C01 4.6 R01 · 7.4 R02 · E01 gıcırtısı orta bantta | + kapak gıcırtısı (ilk ses) |
| C02 | ince üç nota · kitin tıkları · ölçülü kıyı rüzgârı | R03 · E03 · Y1 | — |
| C03 | geniş hava yer değiştirmesi · uzak okyanus rezonansı · bir derin harmonik ton | E07 · E08 · R04 | — |
| C04 | bir kuru ayak sürtmesi · korkmuş ıslık · devam eden uzak rezonans | E09 3.3 · R06 · R05 | — |
| C05 | aynı üç nota, geniş sıcak rezonanslı yetişkin tınısı | R07 SOĞUK | **"warm" → soğuk** (F2 ürün notu: S5 soğuk, S6 sıcak) |
| C06 | çağrılar üst üste, sonra okyanus ve rüzgâr için boşluk | R08 · 6.8-10 boşluk | — |
| C07 | büyüyen su kükremesi · basınç alçak harmonikleri · uzak taş takırtıları | E13 · E34 (alçak) · E14 | + annenin durma bırakışı |
| C08 | rüzgâr · uzak yaklaşan sörf · bir küçük çağrı | Y1 · E13 · R09 | + kemer tonu (kapalı) |
| C09 | iki ağır kuru ayak sesi · kitin sürtünmesi · yükselen uzak sörf | E02 · E03 · E13 | — |
| C10 | genişleyen taş gıcırtısı · keskin çatlama · ağır su çarpması | E16 | — |
| C11 | umutlu camsı cıvıltı → zayıf inen ıslık · kanat membranı | R11 · E17 | — |
| C12 | kırılgan çağrı · küçük membran hareketi · uzak ağır sörf | R12 · E32 · E13 | + ikinci çağrı 9.15 (L köprüsü için) |
| C13 | Khev'in gergin içe çekiş kliği · itiş sürtmesi · geçen rüzgâr | R14 · E09 · E18 | — |
| C14 | ağır iniş rezonansı · kuru kitin gıcırtısı · kısıtlı klik çığlığı | E19 · E25 · E03 · R15 | + plaka çatlağı |
| C15 | sessiz canlı nefesi · zayıf ıslık · kitine yumuşak temas | E28 · R17 · E03 | — |
| C16 | acılı kitin kliği · rüzgâr · sürekli artan sörf | E29 · E13 (+ anne taraması R18, F2 önerisi) | **"acılı kitin kliği" DÜŞTÜ** (sahip kararı 17.10.2026: C16'da doğrulma/çökme yok, acının sebebi görüntüde kalmadı; R19 silindi) · tarama baş dönüşüne saatli |
| C17 | sörf yatağı üstünde açıkta Oru çağrısı, sonra küçük dinleme boşluğu | R20 · E13 · 7.6-10 boşluk | — |
| C18 | geniş sıcak üç nota cevap, altta sörf sürer | R22 · E13 | + anne dikkat tonu (aranma) |
| C19 | derin sıcak organik rezonans · yumuşak membran gıcırtısı · yüzgeç altında su | E21 · E22 · E20 (sakin) | + sörf düşüşü (kural kulakta) |
| C20 | Oru'nun daha parlak üç notası, alçak anne rezonansı cevaplar | R23 · R24 (cevap C21 0.1'de) | + yüzgeç sarması E35 (OLAY EKLEME, sahip kararı 17.10.2026) · saatler ışık parlamasına (8-10 s) bağlı |
| C21 | kısa çaba kliği · taştan membrana sürtme · sıcak anne rezonansı | R25 · E23 · E21 (+ R24 cevabı) | — |
| C22 | tam bir su darbesi ve yayılan kükreme, sonra annenin sabit alçak tonu | E24 · R26 | + darbe öncesi 0.25 s çöküş |
| C23 | yumuşak tamamlanmış üç nota · sessiz biyolojik nefes · aşağıda solan okyanus | R27 · E26 · E28 · E13 (uzak) | — |
| C24 | sıcak yetişkin motifi tamamlanır, incelen rüzgâr ve uzak sörf, yumuşak doğal kuyruk | R28 · E29 · E13 (uzak) | + Oru'nun tek notası R29 (AÇIK KARAR 2) · "soft natural tail": 239.85'e dek doğal söner, 240'a taşan kuyruk yok (B12) |

```
ÖZET     24/24 çekimde en az bir efekt satırı (sessiz çekim yok) · 29 kayıt numarası (28 aktif: çağrı 25 + Khev 3; R19 düştü) · 34 ses varlığı kodu (E01-E35, E04 boş) · 2 yatak (Y1 Y2) · 23 geçiş (23 kesme)
         katman ≤4 her sahnede (K1 ortam · K2 efekt · K3 çağrı + Khev klikleri · K4 müzik) · model sesi: KAPALI · vakum: yok (açık atmosfer, ses taşır)
         planlı sert anlar: C13→C14 (0.25 s boşluk + iniş) · C10 7.0-8.6 (müzik vuruşu yok) · C22 3.1-3.35 çöküş · film sonu
         bulgu cevabı: B1-B20 KABUL (RED 0) · hakem kararlarından ses satırları uygulandı · besteci satırları §8-§8c'de ses kısıtı olarak yazıldı
         F4 kontrol: F4.1 ortam ayrımı yazılı (vakum/iç hacim yok) ✅ · F4.2 kayıt listesi (sözsüz) ✅ · F4.5 her çekim efekt satırı + nereden ✅ · F4.4 model sesi kapalı ✅ ·
         F4.6 yatak + geçiş tabloları ✅ · F4.8 ilk 2 s insan sesi yok, C01 müziksiz, C01→C02 yatak sürer ✅ · F4.3 / F4.7 (müzik planı, MÜZİK PROMPTU) besteci tur 2 dosyasında
GİRDİ    yatay_4_dk_filmler/MOONMOTHER/ODA/F4_ses-tasarimcisi_1.md (tam) · ODA/F4_besteci_1.md (tam) · ODA/F4_kurgucu_1.md (B1-B20, tam) · ODA/F4_hakem_1.md (tam)
         FILM.md §1-§5 (§4 güncel: C16 ve C20 sahip kararı 17.10.2026) · ODA/F3p_yonetmen_1.md · ODA/DURUM.md (SAHİP CEVAPLARI) · ODA/SAHIP_PLANI.md (ses ve müzik akışı) · NOTLAR.md KARARLAR
         uretim_hatti/REPLIK_VE_KLIP_SESI_KILAVUZU.md · GECIS_VE_SES_SUREKLILIGI.md · ILK_30_SANIYE_KILAVUZU.md §5 · KABUL_LISTELERI.md F4.1-F4.8
YAPILMADI  kulakla dinleme ve gerçek take/ışık anı ölçümü (medya yok: 24 çekim ⬜; saniyeler FILM §4 vuruş planından) · kurgu.py kontrol / yukseklik / liste --kesmeler koşulmadı
           (bu ajanda kabuk yok; taslak da yok) · film_dogrula koşulmadı · ORU_CAGRI_v1 üretilmedi (araç perdeyi tutar mı bilinmiyor; §3 notundaki yedek yol; E5 659.3 Hz ölçülecek) ·
           C20 ışık parlamasının gerçek saati bilinmiyor (pilot C20 sonrası ölçülür, §10 madde 2) · Flow Music'in 22.0 / 40-58 / 126-140 / 161.5-179.4 boşluklarını izleyip izlemediği
           ölçülmedi (besteci:206 kurguda kesim) · F♯ 179.4, L2 cam notası 238.8 ve P 202.6 gibi saniye hassasiyetli müzik olayları kulakla F8'de doğrulanır
```
