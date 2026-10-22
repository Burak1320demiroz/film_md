# F4 · ses-tasarımcısı · tur 1 — RAIN_THIEF

```
GİRDİ    RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md (§7 her klibin "Kurgu sesi" satırı · §9 Ritim, müzik ve ses · §4 M1/M2/M3 · §8 devamlılık) ·
         FILM.md §4 (çekim listesi hazır) · §5 (20 replik) · §6 (sahne tablosu plandan) · GECIS_VE_SES_SUREKLILIGI.md · ILK_30_SANIYE_KILAVUZU §5
KURAL    Sahip varsayılanı: plandan dışarı çıkılmaz. Her çekimin efekti planın "Kurgu sesi" satırıdır; yeni ses olayı eklenmedi.
         Yatak cümleleri yalnız plan kelimelerinden kuruldu (pazar uğultusu · konuşma dokusu/klik/yumuşak boğaz sesi/rezonans (§9) · yukarıdan rüzgâr ·
         kuru rüzgâr · suyun derin uğultusu · yumuşak/dolgun yağmur). Model sesi KAPALI: videonun sesi atılır; replik + efekt + ortam + müzik kurguda.
ÇIKTI    ORTAM satırı · sahne tablosu · KAYIT LİSTESİ (20) · EFEKT LİSTESİ · ORTAM YATAĞI · GEÇİŞ (23 kesme) · açık noktalar
```

## ORTAM

```
ORTAM   Açık hava, nefes alınabilir atmosfer (ay şehri: pazar, çatılar, kule platformu). VAKUM YOK, kask yok, telsiz yok: ses havayla taşınır, dış ses vardır.
        Ortam yatağı ritimsiz ve sürekli; kalp atışı gibi düzenli ritim yatağa girmez (düzenli vuruş yalnız planın C16 demir basamak efektidir, efekt olarak).
        Kask içi / telsiz / makine filtresi yok: 20 replik de açık havada, yakın ve kuru, tek insan kaydı (HUMAN). Sessizlik yalnız planlı üç yerde:
        C02 pazar uğultusunun kısa kesilmesi (≈0,4 s, −30 dB'ye iner, dijital sıfır DEĞİL) · C12 müzikte kısa boşluk · C19 "yalnız su ve nefes".
        Kuru ↔ yağmur karşıtlığı (plan §8): C10'da yağmur yalnız camın arkasından boğuk gelir, dışarısı kuru rüzgâr; C23'te ilk kez açık hava yağmuru (Y4) girer.
        C23'ten önce açık hava yağmur sesi YOK (C22 vana/boru suyu hariç, planlı).
MODEL SESİ  KAPALI → mekân başına "ortam ses cümlesi" yazılmaz (film_dogrula konuşma/ses tarifini hata sayar).
```

## Ses seviyesi çerçevesi (hepsi kısa-dönem LUFS, final −14 LUFS integrated · ≤ −1 dBTP · stereo 48 kHz · mono uyumlu)

```
replik          −15…−16 LUFS(k)         yatak (replik yokken)  −18…−22        yatak (replik altında)  −21…−23
efekt zemin     −20…−24                 efekt vurgu (planın "belirgin" dediği)  −16…−18
müzik yatağı    −16…−18 (replik yokken) · replik altında −6…−9 dB · C23-C24'te müzik diyalogdan VE yağmurdan alçak (plan §9)
Kalibrasyon: kurgu.py yukseklik <taslak> --uygula. Dinamik aralık ezilmez; C21 çıtı ile C19 "su ve nefes" arasındaki fark korunur.
```

## SAHNE TABLOSU (§6 biçimi, köprüler dolu)

Katmanlar ≤4: ortam · efekt · replik · müzik. Müzik notları yalnız planın "müzik" kelimeleri (besteci F8'de yazar). Y1 pazar · Y2 çatılar · Y3 hava tacı · Y4 yağmur hâli.

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | ortam Y1 · efekt: hızlı küçük ayaklar, şişe içinden boğuk gök gürültüsü (ilk 2 s'de), arkadan yaklaşan ağır adımlar · replik R01 (2,2 s'den) · müzik: çok düşük hafif-hızlı ritim zemini (2,5 s'den) | C01→C02: Y1 kesintisiz; ağır adımlar L 0,8 s | M1 pazar · ilk 2 s insan sesi yok |
| S2 (C02) | Y1 · efekt: metal botun taş zemine vuruşu + Y1'in kısa kesilmesi · replik R02 · müzik: ritim sürer, replik altında −6…−9 dB | C02→C03: Y1 sürer; C03 doku katmanı J 1,0 s | M1 pazar |
| S3 (C03) | Y1 · efekt: sekiz ayrı uzaylı türünden konuşma dokusu, uzakta kalkış motoru · müzik: ritim sürer (replik yok, −16…−18) | C03→C04: Y1 sürer; doku L 0,8 s, yükselişte seyrelir | M1 pazar · replik yok |
| S4 (C04) | Y1 · efekt: boş bakır musluğun kuru tıklaması · replik R03 · müzik: ritim sürer, replik altında −6…−9 dB | C04→C05: Y1 sürer; müzikte yumuşama C04 son 0,5 s'de başlar (J) | M1 pazar |
| S5 (C05) | Y1 · efekt: tek su damlası · replik R04 (ekran dışı) · müzik: ilk kez yumuşar | C05→C06: Y1 sürer; müzik yumuşak kalır, damla yankısı L 0,5 s | M1 pazar |
| S6 (C06) | Y1 · efekt: kalkış uyarısı · replik R05, R06 · müzik: ritim kararlı biçimde başlar (R06'dan sonra) | C06→C07: Y1 sürer; müzik kesintisiz | M1 pazar |
| S7 (C07) | Y1 · efekt: mavi borudan düşük su rezonansı · replik R07 · müzik: kararlı ritim, replik altında −6…−9 dB | C07→C08: Y1 sürer; boru rezonansı L 0,8 s | M1 pazar |
| S8 (C08) | Y1 · efekt: uzakta kuru metal kapların sallanması · replik R08, R09 · müzik: kararlı ritim, replik altında | C08→C09: Y1→Y2 çapraz 1,5 s (Y2 J 1,0 s) | M1 pazar |
| S9 (C09) | Y2 (+ Y1 kuyruğu L 1,5 s, aşağıdaki pazar) · efekt: ayakların servis basamaklarına teması · müzik: ritim sürer | C09→C10: Y2 sürer; camın arkası yağmuru J 1,0 s (çok düşük) | M2 çatılar · yukarıdan rüzgâr = Y2 |
| S10 (C10) | Y2 · efekt: camın arkasından boğuk yağmur · replik R10 · müzik: ritim sürer, replik altında | C10→C11: Y2 sürer; gemi motoru J 0,8 s, yağmur L 0,8 s | M2 çatılar · dışarıda kuru rüzgâr = Y2 |
| S11 (C11) | Y2 · efekt: gemi motorunun uzaklaşması, kısa nefes · müzik: ritim sürer | C11→C12: Y2 sürer; ağır bot J 0,8 s | M2 çatılar · replik yok |
| S12 (C12) | Y2 · efekt: ağır bot · replik R11, R12 (ekran dışı) · müzik: kısa boşluk (≈0,6–1,8 s), sonra altta döner | C12→C13: Y2 sürer; bot/merdiven L 0,5 s | M2 çatılar |
| S13 (C13) | Y2 · efekt: gergin kumaş sürtünmesi, hafif metal iniş · müzik: ritim sürer | C13→C14: Y2→Y1 çapraz 1,0 s (Y1 J 1,0 s); iniş kuyruğu L 0,5 s | M2 çatılar · replik yok |
| S14 (C14) | Y1 · efekt: pirinç kolun tok sesi, makara ve gergi kablosu · replik R13 · müzik: ritim sürer, replik altında | C14→C15: Y1→Y2 çapraz 1,0 s; makara/kablo L 1,0 s | M1 pazar (iki M2 klibi arasında) |
| S15 (C15) | Y2 · efekt: tentenin yumuşak esnemesi, aşağıdan şaşkın uzaylı sesleri · müzik: ritim sürer | C15→C16: Y2 sürer; demir basamak J 1,0 s, uzaylı sesleri L 0,8 s | M2 çatılar · replik yok |
| S16 (C16) | Y2 · efekt: demir basamaklarda ağır düzenli vuruşlar · müzik: ritim sürer | C16→C17: Y2→Y3 çapraz 1,5 s (Y3 J 1,5 s); basamak sesi alçalarak C17'ye L 0,5 s | M2 çatılar · replik yok |
| S17 (C17) | Y3 (rezervuarın derin uğultusu) · efekt: uzaktan çok kısık demir basamaklar (C19'daki "kesilir"in kaynağı) · müzik: kısa, geniş açılma | C17→C18: Y3 sürer; müzik açılması L 0,8 s | M3 hava tacı · replik yok |
| S18 (C18) | Y3 · efekt: üç tok mekanik klik, düşük enerji sesi · müzik: açılma çekilir, düşük zemin | C18→C19: Y3 sürer; düşük enerji sesi L 0,5 s | M3 hava tacı · replik yok |
| S19 (C19) | Y3 ("yalnız su") · efekt: merdiven sesi ≈2,0 s'de kesilir, Vorr'un nefesi · replik R14 · müzik: düşük zemin (replik altında −9 dB) | C19→C20: Y3 sürer; nefes L 0,4 s | M3 hava tacı · planlı sessizlik |
| S20 (C20) | Y3 · efekt: kumaşın gerilmesi · replik R15 · müzik: tek bas notaya düşer | C20→C21: Y3 sürer; bas nota kesintisiz | M3 hava tacı |
| S21 (C21) | Y3 · efekt: tokanın belirgin küçük çıtı (≈5,5 s) · replik R16 · müzik: tek bas nota sürer, çıt çevresinde 0,3 s −6 dB | C21→C22: Y3 sürer; çıt kuyruğu L 0,4 s | M3 hava tacı |
| S22 (C22) | Y3 · efekt: çarkın kilit sesi, rezervuarın açılan vanaları, borulara birer birer dolan su · replik R17 (6,5 s) · müzik: çözülür | C22→C23: Y3→Y4 çapraz 1,5 s; vana/boru suyu L 1,0 s, ilk damla bu suyun üstüne düşer | M3 hava tacı |
| S23 (C23) | Y4 (ilk damlalar → dolgun yağmur) · efekt: ilk damlalar bakıra (fincana) vurur, karışık sevinç sesleri · replik R18, R19 · müzik: yağmurdan ve diyalogdan alçak | C23→C24: Y4 sürer (kesintisiz yağmur, kule için hafif kısık); sevinç sesleri L 1,0 s | M1 pazar |
| S24 (C24) | Y4 (yumuşak yağmur) · efekt: küçük nefes gülüşü · replik R20 · müzik: son nota uzar (diyalogdan ve yağmurdan alçak) | Film sonu: yağmur ve son nota 1,0 s'de −40 LUFS'a iner; dijital sıfır yok | M3 hava tacı |

Katman sayımı: replikli sahnelerin hepsi 4 katman (ortam+efekt+replik+müzik); hiçbiri 4'ü aşmaz. Çapraz geçişlerdeki iki yatak tek ortam katmanı sayılır.

## ORTAM YATAĞI (FILM §6'ya girecek tablo)

| Yatak | Mekân | Çekimler (klip sınırlarını aşar) | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | M1 pazar (kuru) | C01-C08 · C14 | `low steady open-air market murmur of many different alien voices, soft layered resonances, no intelligible words, no rhythm, no music, dry dusty air` | −21 LUFS (replik yokken −20…−22; replik altında −23) | `ses/yatak_pazar.wav` (≥ 100 s, döngüsüz tek parça) |
| Y2 | M2 çatılar | C09-C13 · C15-C16 | `dry steady wind from above over copper rooftops, soft and low, with a very faint murmur of a market far below, no rhythm, no music` | −21 LUFS | `ses/yatak_catilar.wav` (≥ 80 s) |
| Y3 | M3 hava tacı | C17-C22 | `deep low continuous hum of a vast body of water overhead, steady, no rhythm, no music` | −20 LUFS | `ses/yatak_hava_taci.wav` (≥ 70 s) |
| Y4 | Yağmur hâli (M1 → M3) | C23-C24 | `first sparse raindrops on dry copper growing into full soft steady public rain, no thunder, no music` | C23 −18 (dolgun) · C24 −21 (yumuşak) | `ses/yatak_yagmur.wav` (≥ 30 s) |

Notlar:
- Y4, C23→C24 mekân değişimini (pazar → kule) yağmurun kesintisizliğiyle taşır; C24'te yalnız EQ kısılır (tizler biraz azalır), yatak kesilmez.
- Y1, C14'te iki Y2 klibi arasına girer. Y2 zaten "çok uzak pazar mırıltısı" taşıdığı için çapraz geçişler 1,0 s'de kalır (ton farkı yalnız rüzgâr).
- Y2/Y3 yataklarında yağmur yoktur; C10 yağmuru yalnız efekttir (boğuk, cam tarafı). Açık hava yağmuru yalnız Y4'tür.

## GEÇİŞ (FILM §6'ya girecek tablo, 23 kesme · F8'de kurgucu kesinleştirir)

Dağılım: kesme 20 · karışım 3 (23'ün dörtte birinden az) · karartma 0 (planda büyük zaman ya da mekân atlaması yok; film sonunda siyah kare yok, plan C24).

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1 kesintisiz; C01'in ağır adımları L 0,8 s; C02 bot vuruşu ≈0,7 s | aynı mekân; Kett'in sağa koşusu → Vorr'un sağa bakışı, hareket üstünde |
| C02→C03 | kesme | Y1 sürer (kısa kesilmeden döner); doku katmanı J 1,0 s | aynı mekân, ölçek büyük sıçrar (orta yakın → yüksek geniş) |
| C03→C04 | kesme | Y1 sürer; doku L 0,8 s kısılır | Kett sağa ilerler → Tula'nın yanında yavaşlar |
| C04→C05 | kesme | Y1 sürer; müzik yumuşaması C04 son 0,5 s'de (J 0,5 s) | fincan/tıklama → çekirdek valfi; damla yumuşamaya düşer |
| C05→C06 | kesme | Y1 sürer; damla yankısı L 0,5 s | makro → orta; kararın başlangıcı |
| C06→C07 | kesme | Y1 + müzik kesintisiz | Kett sağa döner → Mara'nın yukarı işareti |
| C07→C08 | kesme | Y1 sürer; boru rezonansı L 0,8 s; metal kap sallanması C08 başı | Vorr tezgâha varır, aynı mekân |
| C08→C09 | karışım 0,4 | Y1→Y2 çapraz 1,5 s (Y2 J 1,0 s; Y1 L 1,5 s) | M1→M2 (yükseklik), Vorr'un yukarı bakışı → Kett tırmanışta: zaman atlaması, ışık/ton yumuşatılır |
| C09→C10 | kesme | Y2 sürer; cam arkası yağmuru J 1,0 s çok düşük | tırmanış → cam boyunca; ölçek/açı değişir |
| C10→C11 | kesme | Y2 sürer; gemi motoru J 0,8 s; yağmur L 0,8 s | aynı çatı; Kett'in bakışı camdan gemiye döner |
| C11→C12 | kesme | Y2 sürer; ağır bot J 0,8 s | aynı çatı; tehdit sesi görüntüden önce gelir |
| C12→C13 | kesme | Y2 sürer; bot/merdiven L 0,5 s | yüzleşme → kayma hamlesi, hareket üstünde |
| C13→C14 | kesme | Y2→Y1 çapraz 1,0 s (Y1 J 1,0 s); iniş kuyruğu L 0,5 s | Kett'in inişi → Mara'nın kolu: neden-sonuç, paralel eylem |
| C14→C15 | kesme | Y1→Y2 çapraz 1,0 s; makara/kablo L 1,0 s | kol indi → tente tam açık: kablo sesi bağı |
| C15→C16 | kesme | Y2 sürer; demir basamak J 1,0 s; uzaylı sesleri L 0,8 s | Kett karşıya geçti → Vorr'un paralel rotası |
| C16→C17 | karışım 0,5 | Y2→Y3 çapraz 1,5 s (Y3 J 1,5 s) | M2→M3 (6 m → 18 m), kuleye varış; ışık/ölçek sıçraması yumuşatılır; basamaklar alçalarak C17'ye geçer |
| C17→C18 | kesme | Y3 sürer; müzik açılması L 0,8 s | çok geniş → yakın detay; Kett konsola yaklaşır |
| C18→C19 | kesme | Y3 sürer; düşük enerji sesi L 0,5 s | aynı platform; çekirdek yerinde → Vorr gelir |
| C19→C20 | kesme | Y3 sürer; nefes L 0,4 s; kumaş gerilmesi J 0,3 s | Vorr yaklaştı → yakalama, hareket üstünde |
| C20→C21 | kesme | Y3 + tek bas nota kesintisiz | gerilmiş kumaş → toka yakın planı |
| C21→C22 | kesme | Y3 sürer; çıt kuyruğu L 0,4 s; müzik çözülmesi C22 başı | Kett serbest → çarka; hareket üstünde |
| C22→C23 | karışım 0,8 | Y3→Y4 çapraz 1,5 s; vana/boru suyu L 1,0 s, ilk damla üstüne düşer | M3→M1; su borulardan pazara varır: zaman/mekân atlaması, kule → pazar |
| C23→C24 | kesme | Y4 kesintisiz (C24'te hafif kısık); sevinç sesleri L 1,0 s | pazar → kule; yağmur ortak köprü |

## KAYIT LİSTESİ (FILM §5 · plan §7 Voice satırları · 20 replik)

Kayıt: HUMAN, tek kaynak, İngilizce, açık hava, yakın ve kuru. Hepsi **dört ses profilinden** biri, film boyu aynı tını ve aksan (plan §9). Filtre kolonu: `oda` = yakın, kuru, açık hava; ekran dışı satırlarda `oda + mesafe` (2-3 m, tizler hafif kısık, −2 dB). Beden önce ses sonra: jest repliğin 0,1-0,3 s önünde. Saniye ve süre FILM §5 tahminidir; F8'de gerçek klip ve kayıtla kesinleşir.

Ses profilleri (plan "Voice" satırları, ad: tanım):
- **KETT-SES**: Alert adult voice, light and slightly rough, quick wit without a cartoon squeak.
- **VORR-SES**: Deep restrained adult bass, slow authority, no monster growls.
- **MARA-SES**: Warm adult contralto, dry humor, confident calm, not a narrator.
- **TULA-SES**: Soft older adult voice, breath and patience, clear words.

| No | Metin | Konuşan | Ses profili | Ton | Hedef süre | Filtre | Yerleşeceği çekim + saniye |
|:--:|---|---|---|---|:--:|---|---|
| R01 | Just a little bad weather. Worth a whole ship. | Kett | KETT-SES | nefesli | 3,5 s | oda | C01 · 2,2 s (FILM §5'te 1,0 s: ilk 2 s insan sesi yok; açık nokta 1) |
| R02 | Bring back the rain! That forecast belongs to us. | Vorr | VORR-SES | otoriter (bağırma değil, derin nefesten yükselir, homurtu yok) | 3,5 s | oda | C02 · 1,0 s |
| R03 | One drop. Please. The flower can't wait for payday. | Tula | TULA-SES | yalvaran | 3,5 s | oda | C04 · 1,0 s |
| R04 | I was going to sell it. Buy a way out. | Kett | KETT-SES | pişman | 4,0 s | oda + mesafe (ekran dışı) | C05 · 5,0 s |
| R05 | Your ship's leaving. | Mara | MARA-SES | kuru | 1,5 s | oda + mesafe (arkada, ağız oynamaz) | C06 · 1,0 s |
| R06 | Let it. I'm changing the weather. | Kett | KETT-SES | kararlı | 2,5 s | oda | C06 · 3,3 s |
| R07 | Core in. Turn the blue wheel. Once it starts, nobody can stop it. | Mara | MARA-SES | güvenli | 5,0 s | oda | C07 · 1,0 s |
| R08 | Where is he? | Vorr | VORR-SES | sabırsız | 1,5 s | oda | C08 · 1,0 s |
| R09 | Buying an umbrella. You should try it. | Mara | MARA-SES | alaycı | 3,0 s | oda + mesafe (ekran dışı / yumuşak arka plan) | C08 · 3,3 s |
| R10 | So it can rain. Just on the right side of the glass. | Kett | KETT-SES | düşünceli (alçak sesle) | 4,5 s | oda | C10 · 1,0 s |
| R11 | That rain is company property. Don't make this expensive. | Vorr | VORR-SES | soğuk | 3,5 s | oda | C12 · 1,0 s |
| R12 | Little late for that. | Kett | KETT-SES | meydan okuyan | 1,5 s | oda + mesafe (ekran dışı) | C12 · 5,3 s |
| R13 | Free delivery! | Mara | MARA-SES | oyuncu | 1,0 s | oda | C14 · 1,0 s |
| R14 | Step away from the wheel. You don't know what this costs. | Vorr | VORR-SES | uyarıcı | 4,0 s | oda | C19 · 2,5 s |
| R15 | That rain is not yours. You can't just give it away. | Vorr | VORR-SES | ağır | 4,0 s | oda | C20 · 1,0 s |
| R16 | It isn't yours either. You just built a roof over it. | Kett | KETT-SES | cüretkâr | 4,0 s | oda | C21 · 0,5 s |
| R17 | Forecast: everybody. No exceptions. | Kett | KETT-SES | ilan edici | 1,5 s | oda | C22 · 6,5 s |
| R18 | How much? | Tula | TULA-SES | şaşkın | 1,0 s | oda | C23 · 1,0 s |
| R19 | For once? Nothing. | Mara | MARA-SES | sıcak | 1,5 s | oda + mesafe (kadraj dışı, yakın) | C23 · 2,8 s |
| R20 | Keep the coat. You'll need it. | Kett | KETT-SES | yorgun | 2,5 s | oda | C24 · 2,0 s |

Dağılım: Kett 8 · Vorr 5 · Mara 5 · Tula 2 (20). Ekran dışı 5 satır (R04, R05, R09, R12, R19); ağız kadrajda 15 satır: kayıt klibin ağız hareketine kurguda hizalanır (F8). Alışveriş gecikmeleri korunur: C06 R05→R06 aralığı 0,8 s · C08 R08→R09 0,8 s · C12 R11→R12 0,8 s · C23 R18→R19 0,8 s.

## EFEKT LİSTESİ (her çekim ≥1 satır; "Kurgu sesi" = plan §7)

Kaynak sütunu: **hava** (açık hava, ses havadan) · **yapı** (metal/boru/zemin üzerinden, yine hava duyar). Kask içi yok. "Saniye" tahminidir; hareket zamanı klipten F8'de oturur. Seviye = kısa-dönem LUFS.

| Çekim | Saniye | Ses | Kaynak | Katman | Seviye | Nereden |
|:--:|---|---|---|---|---|---|
| C01 | 0,0-10 | hızlı küçük ayaklar (Kett) | yapı (taş zemin) | efekt | −20 | ara: `small fast footsteps running on dusty stone` |
| C01 | 0,5-2,0 (şimşek anı) | şişe içinden boğuk gök gürültüsü, tek kısa yuvarlanma; açılış sorunu ilk 2 s'de duyurur | hava | efekt | −17 | üret: `a short muffled thunder roll heard from inside a glass bottle, close and dry, no echo` |
| C01 | 2,0-10 | arkadan yaklaşan dev muhafızın ağır adımları (plan C01 olay metni), giderek yakın | yapı | efekt | −26 → −20 | ara: `heavy slow footsteps approaching, large creature, stone` |
| C02 | ≈0,7 | metal botun taş zemine vuruşu (+ Y1'in 0,4 s'lik kısa kesilmesi, −30 dB'ye) | yapı | efekt | −16 | ara: `heavy metal boot stomp on stone single` |
| C03 | 0-10 | sekiz ayrı uzaylı türünden konuşma dokusu: klikler, yumuşak boğaz sesleri, farklı rezonanslar, anlaşılır kelime yok (plan §9); kamera yükseldikçe seyrelir | hava | efekt | −23 → −27 | üret: `layered texture of many different alien species vocalizing at a distance, soft clicks, gentle throat sounds, varied resonances, no intelligible words` |
| C03 | 3,0-10 | uzakta kalkış motoru (sol, turuncu gemi) | hava | efekt | −26 | üret: `a distant small skiff engine spooling up for departure, far away, left side` |
| C04 | ≈5,5 | boş bakır musluğun kuru tıklaması; su gelmez | yapı (bakır) | efekt | −18 | üret: `a single dry click of an empty coin-operated copper spout, no water, quiet and close` |
| C05 | ≈2,5 | tek su damlası (çiçeğe/saksıya); çevresinde Y1 1,5 s −4 dB; müzik ilk kez yumuşar | hava | efekt | −18 | ara: `single water drop onto leaf close dry` |
| C06 | 0,0-3,0 | kalkış uyarısı (gemiden, uzak, söz yok) | hava | efekt | −22 | üret: `a distant ship departure warning signal, soft repeating alarm tone, no voice, no melody` |
| C07 | 0-10 | mavi borudan düşük su rezonansı | yapı (boru) | efekt | −24 | üret: `low water resonance inside a thick metal pipe, steady, no rhythm, close` |
| C08 | 0,0-0,9 | uzakta kuru metal kapların sallanması (Vorr'un varışı) | yapı | efekt | −24 | ara: `dry metal containers rattling distant` |
| C09 | 0,5-10 | ayakların servis basamaklarına teması, yavaş ve dikkatli | yapı (metal basamak) | efekt | −20 | ara: `bare feet on metal ladder rungs slow climbing` |
| C09 | 0-10 | yukarıdan rüzgâr | hava | ortam (Y2) | −21 | Y2 yatağı |
| C10 | 0-10 | camın arkasından boğuk yağmur, yalnız cam tarafında | hava | efekt | −22 | üret: `steady rain heard muffled through a thick glass wall, from inside a sealed greenhouse` |
| C10 | 0-10 | dışarıda kuru rüzgâr | hava | ortam (Y2) | −21 | Y2 yatağı |
| C11 | 0,0-7,0 | gemi motorunun uzaklaşması (soldan, azalan) | hava | efekt | −22 → −34 | üret: `a small skiff engine lifting away and fading into the distance` |
| C11 | ≈7,5-8,5 | kısa nefes | hava | efekt | −24 | ara: `short breath exhale adult` |
| C12 | ≈0,6 | ağır bot (merdivenden yürüyüş yoluna tek adım); müzikte kısa boşluk 0,6-1,8 s | yapı | efekt | −16 | ara: `single heavy boot step metal staircase to walkway` |
| C13 | 2,0-6,0 | gergin kumaş sürtünmesi (eğimli tentede oturarak kayma) | yapı (kumaş) | efekt | −20 | ara: `body sliding down taut canvas canopy` |
| C13 | ≈6,0 | hafif metal iniş (alt sahanlık) | yapı | efekt | −20 | ara: `light landing on metal platform small body` |
| C14 | ≈0,8 | pirinç kolun tok sesi | yapı (pirinç) | efekt | −16 | ara: `heavy brass lever pull thunk` |
| C14 | 1,0-10 | makara ve gergi kablosu (tente rayda uzar) | yapı | efekt | −22 | ara: `pulley and tensioned cable winding` |
| C15 | 3,0-8,0 | tentenin yumuşak esnemesi (Kett'in küçük ağırlığı) | yapı (kumaş, kablo) | efekt | −24 | ara: `taut canvas canopy soft flex creak` |
| C15 | 1,0-9,0 | aşağıdan şaşkın uzaylı sesleri: kısa, sözsüz, farklı türler, seyrek | hava | efekt | −26 | üret: `a few different alien beings below gasping in surprise, short non-verbal vocalizations, soft clicks, no words` |
| C16 | 0-10 | demir basamaklarda ağır düzenli vuruşlar (Vorr) | yapı (demir) | efekt | −18 | ara: `heavy steady footsteps on an iron staircase` |
| C17 | 0-10 | rezervuardaki suyun derin uğultusu | hava | ortam (Y3) | −20 | Y3 yatağı |
| C17 | 0-10 | uzaktan çok kısık demir basamak vuruşları (C19 "merdiven sesi kesilir"in kaynağı, açık nokta 4) | yapı | efekt | −32 | C16 efektinin kısık/uzak sürümü |
| C18 | ≈4,0 · 4,5 · 5,0 | üç tok mekanik klik (çekirdeğin oturmasına hizalı, ≈0,5 s arayla) | yapı (bakır) | efekt | −16 | ara: `three solid mechanical clicks seating into a socket` |
| C18 | 5,0-10 | düşük enerji sesi (mavi durum ışığı), yavaşça belirir | hava | efekt | −26 | üret: `a low soft energy hum fading in, steady, no rhythm, no melody` |
| C19 | 0,0-2,0 | merdiven sesi (C16-C17'den süren) ≈2,0 s'de kesilir | yapı | efekt | −22 → kesilir | C16 efektinin sürümü |
| C19 | 2,0-10 | Vorr'un nefesi, yavaş; geri kalan yalnız su (Y3) ve replik | hava | efekt | −25 | ara: `slow deep breathing large creature close` |
| C20 | 0,3-6,0 | kumaşın gerilmesi (ponço yakası) | yapı (kumaş) | efekt | −20 | ara: `heavy fabric stretching tension creak` |
| C21 | ≈5,5 | tokanın belirgin küçük çıtı (yatak ve müzik 0,3 s −6 dB) | yapı | efekt | −16 | ara: `small plastic clasp unsnap click isolated` |
| C22 | ≈6,0 | çarkın kilit sesi (fiziksel durdurucu) | yapı (bakır) | efekt | −16 | ara: `heavy mechanical latch lock clunk` |
| C22 | 6,2-10 | rezervuarın açılan vanaları, borulara birer birer dolan su | yapı (boru) | efekt | −21 | üret: `reservoir valves opening one after another, water rushing into blue pipes one by one` |
| C23 | 0,0-2,5 | ilk damlalar bakıra (fincana) vurur, seyrek | hava | efekt | −20 | ara: `first rain drops on copper sparse` |
| C23 | 1,0-10 | dolgun yağmur (Y4 yatağı, yoğunlaşır) | hava | ortam (Y4) | −18 | Y4 yatağı |
| C23 | 3,0-10 | karışık sevinç sesleri: sözsüz, farklı türler, kıkırdama/klik, kelime yok | hava | efekt | −24 | üret: `many different alien species reacting with joy to rain, non-verbal soft clicks and delighted throat sounds, no words` |
| C24 | 0-10 | yumuşak yağmur (kuleye uyarlanmış) | hava | ortam (Y4) | −21 | Y4 yatağı |
| C24 | ≈5,0 | küçük nefes gülüşü (Kett) | hava | efekt | −24 | üret: `a small tired breathy laugh, adult, close, dry` |

## Model sesi AÇIK ortam ses cümlesi (madde 7)

Uygulanmaz: model sesi KAPALI. goruntu-yonetmeni video promptlarına ses cümlesi yazmaz.

## Açık noktalar (Fable'a)

1. **R01 saniyesi (kural 0).** FILM §5: C01 · 1,0 s; ILK_30 §5: ilk 2 s insan sesi yok. Kayıt listesinde 2,2 s'ye aldım. Sorun: ağız kadrajda; kliptte Kett'in ağzı erken açılırsa kayıt uymaz. Öneri: goruntu-yonetmeni C01 video promptuna ilk 2 s ağız kapalı koşu ekler (plan "says the single assigned line" çerçevesini bozmaz). Aksi hâlde F8'de ağız zamanına göre R01 kayması ya da ilk 2 s ayaklar + gök gürültüsü ile açılış, replik sonra.
2. **Plan §7 C03 video promptu "Atmospheric crowd audio only; no dialogue, no subtitles"** model sesi KAPALI filmde ses tarifi sayılır (`film_dogrula` hata sayar). Plan birebir kalır, ama goruntu-yonetmeni/denetçi bu cümleyi nasıl işleyeceğini Fable'a ya da sahibe sorar. Tavsiyem: yalnız "no dialogue, no subtitles" kalsın, "Atmospheric crowd audio only" çıksın (sahip kararı gerek).
3. **C22 çarkın dönüşü.** Planın C22 efekti yalnız kilit sesi, vanalar ve müziğin çözülmesi; çarkın 0-6 s dönüş sesi planda yok. Yeni ses olayı eklemedim: dönüş boyunca yalnız Y3 + müzik gerilimi. Sessiz dönüş zayıf kalırsa tek "çark dönüş gıcırtısı" eklemek sahibin kararı.
4. **C17-C18 uzaktan basamak sesleri** planda yazılı değil; C19 "merdiven sesi kesilir" ifadesinden çıkarılan çıkarım (C16'dan süren ses). Çok kısık (−32 LUFS). Sahip karşı çıkarsa silinir; C19'daki "kesilir" yine C16'dan C19'a ilk 2 s ile korunur.
5. **C19 planı:** Vorr'un son iki adımı platformda; plan "yalnız su ve nefes kalır" diyor, yani adım sesi yok (üslupla sustu). Plana uydum; kurgucu F8'de dengeyi dinler.
6. **Müzik C01:** plan §9 "başta hafif hızlı ritim" der; ILK_30 §5 "müzik C01'de girmez ya da çok düşük zemin": ritmi çok düşük zemin olarak 2,5 s'den başlattım. C21 müziği (plan yazmıyor): C20'nin tek bas notası sürer. C19: düşük zemin (planın "yalnız" kelimesi efekt için okundu). Besteci F8'de kesinleştirir.
7. **Saniye değerleri** (efekt ve geçiş) tahmindir; hepsi gerçek klip çıktısı gelince F8'de hareket anına oturur.
