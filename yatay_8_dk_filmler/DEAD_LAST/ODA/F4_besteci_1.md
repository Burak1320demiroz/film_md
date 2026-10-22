# F4 · besteci · tur 1 · DEAD_LAST (20.10.2026)

> Kaynak: `DEAD_LAST_8DK_48_KLIP_FILM_PLANI.md` (sahip planı, birebir) · `FILM.md` §1 §4 §5 §6 · `ILK_30_SANIYE_KILAVUZU.md` §5.
> Sahip varsayılanı: "plandan asla dışarı çıkma". Planın ses/ritim/bölüm cümleleri ve 48 klip tablosundaki "Ortam ve müzik." satırları esastır.
> Plan tür, tempo ya da enstrüman vermez; bunlar aşağıda **SAHİBE SORU (F8)** listesinde varsayılanıyla durur.
> Saniyeler F4 yaklaşığıdır: her çekim 10 s, KLIP_SURESI ölçülmedi, replik saniyeleri `FILM.md` §5 tahmini (2,8 kelime/s).
> F8'de vuruş ve susma noktaları `kurgu.py liste --kesmeler` çıktısına göre kesinleşir.

## 1. Planın müzik ve ses cümleleri (tek kaynak)

| Plan yeri | Cümle | Müziğe etkisi |
|---|---|---|
| "Ses, kamera ve ritim" | "İlk gezegen kaybında kısa bir düşük frekans boşluğu ve küçük bir nefes yeterlidir. Büyük patlama sesini sürekli yükselterek Axi'nin cümlesini örtme." | C01-C02 müziksiz; müzik hiçbir yerde repliği örtmez |
| aynı | "Şehir ışıklarının sönmesi ve sonraki hücre kilidinin klik sesi birbirine bağlanabilir." | C02 sonu → C03 başı köprü; müzik ilk notasını klikten sonra, Axi'nin cümlesi bittikten sonra alır |
| C02 video istemi kurgu notu | "Müzik yerine ilk anda kısa bir düşük frekans boşluğu bırak." | C02 başında müzik yok (plan açıkça söylüyor) |
| "Ses, kamera ve ritim" | Üç sektörün işitsel kimliği: kökler tok geçiş + motor yankısı · okyanus basınçlı su + boğuk uğultu · metal fırtınası küçük metal geçişleri + keskin yakın sürtünme | Bunlar ses tasarımının işi. Müzik bu bantları doldurmaz: köklerde alçak ve tok, okyanusta tepe frekanssız, metalde metalik vurgu yok |
| aynı | "Uzay dış planlarının sesleri sinemasal ses tasarımıdır; gerçek boşluk akustiği diye sunulmaz." | Vakum filmi değil (FIZIK_IDDIASI yok): kuru-yankısız müzik kuralı zorunlu değil; yine de replik için kuru tutulur (bkz. soru 8) |
| aynı | "C42'deki kısa emir ilk gerçek kontrol kaybıdır." | C42'de müzik yok; Kalix'in cümlesi çıplak kalır |
| aynı | "Raka ve Thren hızlı ama anlaşılır · Axi sakin, yorgun · Sael sıcak · Korv düşük, sert · Veli hızlı, kuru mizahlı · Kalix ilk yarıda profesyonel sunucu kadar rahat" | Müzik karakterin sesine eşlik eder; Kalix'in ilk yarısında müzik rahat/hafif |
| Tablo | 11 klipte "Ortam ve müzik." (diyalogsuz): C07 C10 C12 C13 C16 C29 C31 C37 C43 C46 C48 | Müziğin yoğun durduğu tek yerler; 37 diyalog klibinde müzik seyrek yatak |
| Ton (belge başı) | "gösterişli yarış aksiyonu, karanlık bir kural ve güçlü bir ortak kurtuluş" | Tür/duygu çizgisi |
| Mekanik | C20 "Same pulse." · C41 iki hücre "aynı darbe" · C40 "Then I match yours." | Müzik yapısı: iki nabız → tek nabız (bkz. §3) |
| Bölüm 7 başlığı | "KAZANMAK İÇİN YAVAŞLA" | Kilitlenme hızlanarak değil yavaşlayarak olur |
| C48 / son | "DEAD LAST son 1,5 saniyede kurguda" · C47 "Somewhere without a finish line." | Müzik 8:00'de çözülmemiş akorla kesilir; "bitiş çizgisi yok" = müzik kadansa varmaz |

## 2. FILM.md §7 MÜZİK PLANI — birebir kopyalanacak blok

```
OKUMA        İzleyici bu filmi, bir dünyanın kaybıyla başlayıp düşmanları ortak kurtuluşa çeviren, hızı üstte yası altta taşıyan karanlık bir uzay yarışı aksiyonu olarak okumalı (plan Ton: gösterişli yarış aksiyonu, karanlık kural, güçlü ortak kurtuluş).
MÜZİKSİZ     0:00–0:24 (C01 gezegen kaybı + C02 boşluk + C03 hücre kliği; plan: düşük frekans boşluğu, müzik yerine) · 6:50–7:00 (C42 beslemeler söner, Kalix "ilk gerçek kontrol kaybı"; doruk sessizliği, F4 önerisi, soru 3)
VURUŞ/SUSMA  ~0:24 tek alçak nota (C03, Axi cümlesinden sonra) · ~0:55 hafif alçak nabız (C06, kalkış titreşimi) · 1:00 ana tema + sürücü nabız (C06→C07 kesme, "tam birinci dakikada beş araç fırlar") · ~1:35 tek armonik dönüş (C10 sol kanat, vuruş değil) · 1:50–2:00 yavaşlama figürü kurulur (C12 sağ kanat) · 2:00 basınçlı alçak zemin (C13) · 2:30 sıcak sabit akor (C16 akış izi) · 3:50 hedef değişir (C24 "We end the race") · ~4:43 tek koyu vurgu (C29) · 5:00 geniş tema (C31 Sael önde) · 5:10–5:30 çıplak, tek alçak çello notası (C32-C33 duygusal merkez) · 6:00–6:30 iki nabız ayrılır (C37-C39) · 6:30–6:40 hızlı nabız yavaşlayıp ikisi tek nabızda kilitlenir (C40) · 6:40–6:50 zirve (C41) · ~6:50 müzik durur (C41→C42 kesmesi; F8'de gerçek ışık-sönme anından 1-2 s önce) · 7:00 geri dönüş tek notayla (C43 kilitler açılır) · 7:50–8:00 son açıklama, kadanssız · 8:00 çözülmemiş asılı akorda kesme, fade-out yok — faz 8'de gerçek kesme noktalarıyla kesinleşir
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md
```

### MÜZİK PROMPTU — Flow Music'e yapıştırılır (F4 taslak, 20.10.2026; kesme noktaları yaklaşık, F8'de kesin)
```text
Instrumental cinematic sci-fi space-racing score, one continuous piece, 8:00 total. Dark, glossy, tense, ending open. [Instrumental]
Palette: low bowed strings, one solo low cello, dark analog synth bass pulse, low plucked ostinato, soft brass-like pad. Two pulses: one around 100 BPM, one around 92 BPM.
0:00-0:24 silence, no music at all. At 0:24 one single low note enters (about 100 Hz with its octave above, audible on a phone speaker), thin dark drone, very quiet, sparse until 0:55.
0:55 a gentle low pulse begins. At 1:00 the main theme and driving 100 BPM pulse hit at full power: bold, fast, dark racing energy. From 1:10 a second 92 BPM pulse runs against the first, a rivalry.
About 1:35 one sharp harmonic turn, then by 1:55 a slowing descending figure that settles and holds.
2:00-2:30 deep pressurized low pad, muffled, no high frequencies. 2:30-2:40 warm steady stable chords.
2:40-4:00 quiet restless low ostinato with very sparse midrange so dialogue stays clear; warmer at 3:40; rising resolve by 3:57.
4:00-5:00 cold flat tension, one dark accent near 4:43, then light dry staccato plucks.
5:00-5:10 wide powerful steady theme. 5:10-5:30 almost bare: one sustained low cello note, grief.
5:30-6:00 rising heavy low ostinato, pulse steadies. 6:00-6:30 the two pulses drift apart.
6:30-6:40 the faster pulse slows to 92 BPM and both lock into ONE shared pulse. 6:40-6:50 that single pulse builds to the loudest peak, then stops dead at 6:50.
6:50-7:00 total silence. At 7:00 one single warm note returns, the only full resolution, opening into a soft warm theme until 7:40.
7:40-7:50 thins to almost nothing. 7:50-8:00 last theme statement rising, never cadencing, hard cut at 8:00 on an unresolved suspended chord. No fade-out.
No vocals, no drums, no riser, no whoosh. Nothing below 60 Hz. Dry, no big reverb.
```

## 3. Müzik planı — gerekçe

**Okuma.** Aynı görüntü (yarış aracı, çatlayan gezegen) drone ile tehdit, çello ile yas, sakin nabızla hayranlık olur. Plan yası (Axi'nin dünyası geri gelmez, C43'te yeniden kurulmaz) ve hızı birlikte ister. Bu yüzden iki katman: üstte hız (sürücü nabız, ostinato), altta yas (alçak yaylılar, C33'te tek çello notası). Film sonunda sıcaklığa açılır ama çözülmez.

**Yapısal fikir (planın mekaniğinden).** Plan filmi bir "aynı darbe" üzerine kurar: C20 "Same pulse.", C41 iki hücre aynı anda, C40 "Then I match yours." Müzik de aynı şeyi yapar. İki nabız (≈100 BPM Raka tarafı, ≈92 BPM Thren tarafı) 1:10'dan 6:30'a birbirine karşı çalar; C40'ta hızlı olan yavaşlayıp yavaşa uyar ve tek nabızda kilitlenir (Bölüm 7 başlığı "Kazanmak için yavaşla"). Aynı fikir C12'de tohumlanır: sağ kanat açılıp hız düşerken yavaşlayan, alçalan bir figür duyulur ("Sağ kanatla hız azaltma finalin hazırlığıdır", plan C12). C40'ta o figür geri gelir. Melodi alıntısı yok; kimliği olan şey bir hareket biçimi.

**Müziksiz anlar (kural 2).**
1. 0:00–0:24 (plan temelli): C01 gezegen kaybı ve C02 plan notu "müzik yerine düşük frekans boşluğu". Müzik C01'de girmez (kılavuz §5). İlk nota C03'te, hücre kliğinden ve "That's my world in your booster." (≈20:01–20:03,5) bittikten sonra gelir.
2. 6:50–7:00 (F4 önerisi, soru 3): C42, doruk. Plan C42'yi "ilk gerçek kontrol kaybı" diye işaretler. Müzik kesmeyle (C41→C42, 6:50) susar, Kalix'in "Stop them! I gave you worlds!" (≈6:51–6:53,5) çıplak kalır, beslemelerin sönüşü yalnız ses tasarımıyla verilir. Geri dönüş **tek nota**: C43 başı (7:00), kilit çemberleri açılırken. Patlama yok.

**Çözülme sayısı (kural 3).** Filmde tek gerçek çözülme: 7:00 C43 (kilitler açılır, ilk nota → sıcak tema 7:40'a kadar). Bitiş: fade-out yok; 8:00'de çözülmemiş asılı akorda sert kesme. DEAD LAST kartı 7:58,5 civarı kurguda (plan C48), müzik kartın üstünde kadanssız yükselir ve kesilir. Gerekçe: C47 "Somewhere without a finish line." müzik de bitiş çizgisine varmaz.

**Açılış (kural 0).** C01 müziksiz, C02 müziksiz, C03'te (≈0:24) tek alçak nota ve çok düşük zemin; tırmanış C06 sonunda (≈0:55 hafif nabız) başlar, 1:00'de tam giriş. Kılavuz "C02 ya da C03'te girer" der: giriş C03'ün içinde, ilk 30 saniye içinde. İlk 2 s'de müzik de insan sesi de yok.

**Telefon (kural 5).** Alçak nota ≈100 Hz ve bir oktav üstü birlikte; 60 Hz altı yok; infrases yok.

**Kuru müzik (kural 6).** Vakum filmi değil (plan: sinemasal ses, FIZIK_IDDIASI yok). Yine de repliği korumak için müzik yankısız/kısa kuyruklu. Mickey-mousing yok: C10 ve C29'daki vurgular karakter hareketini taklit etmez, tek armonik dönüş / tek koyu nota olarak durur; konumu görüntüyü kaydırarak tutturulur.

## 4. Dinamik tablo (yoğunluk 0-5)

Replik zamanları `FILM.md` §5 tahmini. "D" = diyalog klibi (müzik repliğin altında −6…−9 dB, orta bant 300 Hz–3 kHz seyrek).

| Bölüm | Yaklaşık saniye | Çekim | Yoğunluk | Ne giriyor / çıkıyor |
|---|---|---|:--:|---|
| 1 Bir dünyanın bedeli | 0:00–0:24 | C01 C02 C03 başı | 0 | Müzik yok (plan: düşük frekans boşluğu + küçük nefes). Giren yok |
| | 0:24–0:50 | C03 sonu, C04 D, C05 D | 1 | ≈0:24 tek alçak nota (~100 Hz + oktav), ince karanlık drone girer. C05 Kalix "rahat sunucu": müzik hemen hemen yok |
| | 0:50–1:00 | C06 D | 1→2 | Replikler 0:51–0:55,3. ≈0:55,5 hafif alçak nabız (≈100 BPM) başlar, kalkış titreşimiyle büyür |
| 2 Köklerin altında | 1:00–1:10 | C07 (müzik klibi) | 4 | **1:00 kesmede** ana tema + sürücü nabız tam giriş; alçak yaylı + bas nabız + plucked ostinato |
| | 1:10–1:30 | C08 D, C09 D | 2–3 | ≈1:10'dan ikinci nabız (≈92 BPM, Thren) karşıdan girer; replikler 1:11–1:15 ve 1:21–1:27 |
| | 1:30–1:40 | C10 (müzik klibi) | 4 | ≈1:35 tek armonik dönüş (sol kanat kopar; hareket taklidi değil) |
| | 1:40–1:50 | C11 D | 2 | Yoğunluk düşer, ostinato kalır; replikler 1:41–1:46 ve 1:46,3 |
| | 1:50–2:00 | C12 (müzik klibi) | 3→1 | Sağ kanat açılır: yavaşlayan, alçalan figür kurulur (C40'ın tohumu), zemine oturur |
| 3 Göğün okyanusu | 2:00–2:10 | C13 (müzik klibi) | 3 | Basınçlı, boğuk, alçak pad; tepe frekans yok (okyanus uğultusuna yer) |
| | 2:10–2:30 | C14 D, C15 D | 2→1 | Replikler 2:11–2:15, 2:21–2:27. Karar anında (≈2:25–2:27 "No. He's rolling.") müzik inceliyor |
| | 2:30–2:40 | C16 (müzik klibi) | 3 | 2:30'da sıcak, sabit akorlar (akış izi = denge); filmin ilk kararlı armonisi |
| | 2:40–3:00 | C17 D, C18 D | 1–2 | Rakip/ ortak soru. C18 "Look beneath the finish lights" sonunda uzun tutulan bir nota (merak) |
| 4 Bitiş çizgisinin içi | 3:00–3:50 | C19–C23 D | 2 | Sessiz huzursuz alçak ostinato, orta bant en seyrek (5 diyalog klibi üst üste). C22 "cells nearly dry": enerji incelir. C23 Sael ≈3:41: sıcak renk |
| | 3:50–4:00 | C24 D | 2→3 | "We end the race" ≈3:51–3:56: hedef değişir, 3:57'den sonra kararlı yükseliş |
| 5 Başka bir cellat bul | 4:00–4:30 | C25 C26 C27 D | 2 | Veli, Korv: ostinato sürer. C27 Kalix: soğuk, düz, tek ara (sakin ama tehditkâr) |
| | 4:30–4:40 | C28 D | 3 | Korv "Find another executioner" ≈4:31–4:33,5: gerilim |
| | 4:40–4:50 | C29 (müzik klibi) | 4 | ≈4:43 tek koyu vurgu (sağ arka motor kararır), ardından kuru |
| | 4:50–5:00 | C30 D | 3 | Veli, kuru mizah: hafif, kuru, staccato plucked; ağır tema yok |
| 6 Son yakıt | 5:00–5:10 | C31 (müzik klibi) | 4 | Geniş, kararlı tema (Sael önde, akış izi); 2:30 sıcak akorla akraba |
| | 5:10–5:30 | C32 D, C33 D | 0–1 | Çıplak: tek sürekli alçak çello notası. Filmin duygusal merkezi (C33 ≈5:21–5:25,5). Yükselmez |
| | 5:30–5:50 | C34 D, C35 D | 2→3 | Veli kıvrak (≈5:31); Korv kapıyı tutar: ağır alçak ostinato |
| | 5:50–6:00 | C36 D | 3 | "Purge in ten": ilk nabız yeniden net, sayaç taklidi yok |
| 7 Kazanmak için yavaşla | 6:00–6:10 | C37 (müzik klibi) | 3–4 | İki besleme hattı = iki nabız ayrılır (100 / 92 BPM) |
| | 6:10–6:30 | C38 D, C39 D | 2 | Nabızlar kayar: C39 Thren "won't make the pulse" ≈6:21–6:26 |
| | 6:30–6:40 | C40 D | 3 | Raka "Then I match yours." ≈6:31–6:35: hızlı nabız 92'ye yavaşlar, **iki nabız tek nabızda kilitlenir**; C12 figürü geri gelir |
| | 6:40–6:50 | C41 D | 3→5 | "Now." ≈6:41; tek nabız filmin en yüksek noktasına büyür |
| | 6:50–7:00 | C42 D | **0** | **Müzik ≈6:50'de ölü durur** (ışık sönmesinden 1-2 s önce, F8'de gerçek ana göre). Kalix ≈6:51–6:53,5 çıplak |
| 8 Çizginin ötesi | 7:00–7:10 | C43 (müzik klibi) | 2 | **7:00 geri dönüş tek nota** (sıcak). Tek gerçek çözülme: kilit çemberleri açılır, sıcak tema |
| | 7:10–7:30 | C44 D, C45 D | 2 | Sael, Axi, Raka: sıcak yatak; replikler ≈7:11–7:15, 7:21–7:24, 7:24,8–7:26,8 |
| | 7:30–7:40 | C46 (müzik klibi) | 1→3 | "Suskunluk sonrası ayağa kalkar": önce hafif, kalkışla tema sıcak yükselir |
| | 7:40–7:50 | C47 D | 1→0,5 | Axi/Raka son replikler ≈7:41–7:45,3: müzik neredeyse çekilir |
| | 7:50–8:00 | C48 (müzik klibi) | 3→4 | Altı araç ayrılır; son tema açıklaması yükselir, kadans yok. DEAD LAST kartı ≈7:58,5. **8:00 çözülmemiş asılı akorda kesme**, fade-out yok |

Yoğunluk özeti: ilk 24 s sıfır → 1:00'de ilk zirve (4) → 3:00–4:00 dar orta bant (diyalog yoğun) → 5:10 çıplak (duygusal merkez) → 6:50 zirve ve ani sessizlik → 7:00 tek nota.

## 5. Katmanlar (giriş saniyeleriyle)

| Katman | Giriş | Çıkış / durum | Rol |
|---|---|---|---|
| K1 alçak nota + drone (~100 Hz, oktav üstü ~200 Hz) | ≈0:24 | 6:50 durur; 7:00 tek nota olarak döner | zemin, telefonda duyulur |
| K2 alçak yaylılar (yaylı, pad) | ≈0:55 | kalıcı, 6:50 durur; 7:00 sonrası sıcak | yas, gövde |
| K3 sürücü nabız (sentetik bas, ≈100 BPM) | ≈0:55 hafif; 1:00 tam | 6:30–6:40'ta 92'ye iner; 6:50 durur | hız |
| K4 ikinci nabız (plucked alçak ostinato, ≈92 BPM) | ≈1:10 | 6:30'da K3 ile tek nabız; 6:50 durur | rakip |
| K5 tek çello | 5:10–5:30 çıplak; 6:30 ve 7:00 sonrası kısa | — | yas (C33) |
| K6 yumuşak pirinç benzeri pad | 1:00 tam girişte; 5:00; 7:00 sonrası sıcak | seyrek | gösteriş, ortak kurtuluş |

Aynı anda en çok 4 katman duyulur (diyalog klipleri 1–2).
Davul seti, vokal, riser, whoosh yok (YOK listesi). Metalik vurgu yok (ses tasarımının metal fırtınası kimliğini bozmaz).

## 6. Miks

- Final −14 LUFS / −1 dBTP (film miksi; `kurgu.py yukseklik`). Müzik stem'i bunun içinde dengelenir.
- Replik altı −6…−9 dB (37 diyalog klibinde). Orta bant 300 Hz–3 kHz diyalogda seyrek tutulur (müzik zaten orada az yazılı); plan: "Büyük patlama sesini sürekli yükselterek Axi'nin cümlesini örtme."
- Mono uyumlu; stereo genişlik tek başına anlam taşımaz (iki nabız soldan/sağdan değil, ritim farkıyla ayrılır).
- 60 Hz altı yok; K1 ~100 Hz ve oktavı telefonda taşır.
- Müzikli klipler (11) en yüksek yoğunlukta; ses efekti (sektör kimliği) ayrı kayıtta, müzikle bant çakışması F8'de kontrol edilir.
- Mekân başına tek ortam yatağı (kesmeleri aşar): müzik de kesmede sürer (GECIS_VE_SES_SUREKLILIGI); keskin kesmede müzik zaten tek parça, bölünmez.

## 7. Yaklaşık kesme noktaları (F8'de `kurgu.py liste --kesmeler` ile kesin)

Hepsi n × 10 s (klip 10 s). Müzik kararlarına bağlanan kesmeler:

| Kesme | Yaklaşık | Müzik |
|---|---|---|
| C03 içi | 0:20–0:24 | hücre kliği; ≈0:24 tek alçak nota |
| C06→C07 | 1:00 | tam giriş |
| C09→C10 | 1:30 | yoğunluk 4 |
| C11→C12 | 1:50 | yavaşlama figürü |
| C12→C13 | 2:00 | basınçlı pad |
| C15→C16 | 2:30 | sıcak akor |
| C24→C25 | 4:00 | hedef değişimi sonrası |
| C28→C29 | 4:40 | koyu vurgu |
| C30→C31 | 5:00 | geniş tema |
| C31→C32 | 5:10 | çıplak çello |
| C36→C37 | 6:00 | iki nabız ayrılır |
| C39→C40 | 6:30 | tek nabızda kilit |
| C41→C42 | 6:50 | müzik ölü durur |
| C42→C43 | 7:00 | tek nota geri |
| C47→C48 | 7:50 | son açıklama |
| film sonu | 8:00 | asılı akorda kesme |

## 8. Tek parça 8:00 çıkmazsa bölünme önerisi

Flow Music resmî süre ve prompt sınırı depoda belgelenmedi. Süre ya da zaman damgalı yapı tutmazsa, parçalar **müziksiz anlarda** bölünür (müzik zaten orada yok; kesme dikişi duyulmaz):

| Parça | Aralık | Not |
|---|---|---|
| P1 | 0:24 – 6:50 (≈6:26) | Başa sessizlik kurguda eklenir (generator sessizliği güvenilir üretmez). 6:50'de ölü durur. P1 yine tutmazsa P1a 0:24–3:00 · P1b 3:00–6:50 |
| P2 | 7:00 – 8:00 (1:00) | Tek nota ile açılır, 8:00'de asılı akorda kesilir |

P1a/P1b dikişi 3:00 (C18→C19; C19-C23 kesintisiz diyalog bölümü, müzik zaten orta bantta seyrek). Dikiş çaprazı kurguda 0,3-0,8 s. Tempo ve anahtar iki parçada aynı yazılır; ikinci istek ilk parçanın tür/palet cümlesini birebir tekrarlar.

## 9. Kılavuz kontrolü

| Kontrol | Durum |
|---|---|
| Müzik C01'de girmiyor (kural 0, kılavuz §5) | evet, ilk 24 s müziksiz |
| İlk 2 s'de insan sesi/ müzik yok | evet |
| Okuma cümlesi | evet |
| En az bir müziksiz an | 2: 0:00–0:24 (plan) · 6:50–7:00 (öneri) |
| Susma doruk öncesi 1-2 s, geri dönüş tek nota | 6:50 → 7:00 tek nota |
| Fade-out yok, çözülmemiş akor | evet |
| Gerçek çözülme ≤ 2 | 1 (7:00 sonrası) |
| Telefon alt bas ~90-160 Hz, infrases yok | evet (~100 Hz) |
| Mickey-mousing yok | evet (C10/C29 vurguları armonik) |
| Melodi alıntısı yok | evet (hareket biçimi, palet) |
| Prompt İngilizce, `[Instrumental]`, ≥200 karakter, Türkçe karakter yok | evet |
| YOK listesi: vocals, drums, riser, whoosh | evet |

## SAHİBE SORU (F8) — plan söylemiyor; varsayılan uygulandı

| # | Soru | Varsayılan (uygulanan) | Alternatif |
|:--:|---|---|---|
| 1 | Tür, palet, tempo: plan vermiyor (yalnız Ton cümlesi). | Karanlık, parlak melez sci-fi aksiyon: alçak yaylılar, tek çello, sentetik bas nabız, plucked ostinato, yumuşak pad; ≈100 / 92 BPM; davul seti yok | Tam orkestral ya da tamamen elektronik; tempo yükseltilebilir |
| 2 | Müzik 37 diyalog klibinin altında sürer mi? Plan "Ortam ve müzik." satırını yalnız 11 diyalogsuz klibe yazıyor. | Sürekli tek parça yatak: diyalogda seyrek, −6…−9 dB; yoğun müzik yalnız 11 klipte | Müzik yalnız 11 klipte (diyalog klipleri müziksiz, yamalı) |
| 3 | Doruk sessizliği C42 (6:50–7:00). Plan C42'yi "ilk gerçek kontrol kaybı" der ama müzik için bir şey söylemez. | Müzik 6:50'de susar, 7:00'de tek notayla döner | Sessizlik yok; müziksiz an yalnız 0:00–0:24 (plan temelli) |
| 4 | İki nabız → tek nabız yapısı (C20 "Same pulse", C40). Planın mekaniğinden türetildi, müziği plana bağlayan fikir. | Uygulandı | Tek sabit nabız |
| 5 | C12 "yavaşlama figürü" C40'ta geri gelir (kurulum–ödeme). | Uygulandı | Figür yok |
| 6 | Bitiş: 8:00'de asılı çözülmemiş akor, kesme. DEAD LAST kartı ≈7:58,5 (plan C48). Kartta müzik kadanssız. | Uygulandı | Kart anında kısa çözülme (ikinci gerçek çözülme) |
| 7 | Tek parça 8:00 çıkmazsa. | P1 0:24–6:50 + P2 7:00–8:00 (bkz. §8) | 3 parça |
| 8 | Kuru müzik: plan sinemasal ses der, vakum filmi değil. | Müzik repliği korumak için yankısız/kısa kuyruklu | Daha geniş, yankılı arena çalgısı (replik kayıtlarını daha çok bastırır) |
| 9 | C03'te giriş saniyesi (≈0:24) hücre kliğinin ve Axi cümlesinin gerçek süresine bağlı. | F8'de klip sesinden ölçülür | — |
| 10 | Kalix için ayrı renk: plan "ilk yarıda profesyonel sunucu kadar rahat" der. | Ayrı tema yok; müzik C05'te neredeyse çekilir, C27'de soğuk düz ara | Kalix'e kısa, hep aynı soğuk renk motifi |

## YEDEK KISA SÜRÜM (Flow Music uzunluk sınırı çıkarsa; FILM.md'ye kopyalanmaz)

```text
Instrumental cinematic sci-fi space-racing score, 8:00, dark and tense, ending open. [Instrumental] Low bowed strings, solo low cello, dark synth bass pulse (100 BPM), low plucked ostinato (92 BPM). Silence until 0:24, then one low note (about 100 Hz). Full theme hits at 1:00. Sparse and quiet under dialogue from 2:40 to 4:00. Almost bare cello at 5:10. Two pulses drift apart at 6:00 and lock into one pulse at 6:30, peak at 6:45, stops dead at 6:50. Silence until 7:00, then one warm note. Ends 8:00 on an unresolved suspended chord, hard cut, no fade. No vocals, no drums, no riser, no whoosh.
```
