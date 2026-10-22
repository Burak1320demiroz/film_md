# 📒 MOONMOTHER — Notlar

> Bu filmde olan her şeyin günlüğü. Hata burada **ret nedeni** olur, kural olmaz
> (`AGENTS.md` §1 ④). Satır olay olduğu gün yazılır.

---

## İŞARETLEME (sahip · Flow'da üretirken)

> Sahip her denemeyi izler ve işaretler: ✅ kullanılabilir (aralıkla) · ❌ değil (tek cümle neden).
> Bu bir onay değil, iş adımıdır; Fable hareketi göremez, seçim bu işaretten başlar.

| Tarih | Deneme dosyası | İşaret | Aralık / neden |
|---|---|:--:|---|

## DENEMELER

> 16.10.2026: satırı **`medya.py al <FILM> --yaz`** yazar (ham/'daki her yeni `Cxx_dN` için); elle yazılmaz.
> Prompt sütunundaki `p:<sha8>` çekimin o günkü Görsel + Video metninden üretilir: prompt sonradan değişirse kimlik de değişir.
> Girdi = EKLE satırındaki kare + referans numaraları. Sahip başka bir şey yüklediyse (başka referans, düzeltilmiş kare) satırı düzeltir.
> Sonuç sütununu sahibin işareti doldurur (İŞARETLEME); Fable oradan kopyalar.

| Tarih | Çekim | Deneme | Araç · mod | Prompt (dosya · p:sha8) | Girdi (kare · ref) | Süre · ses | Sonuç | Kredi |
|---|:--:|:--:|---|---|---|---|---|:--:|

```
Örnek (medya.py al çıktısı, sonra işaretle):
| 16.10 | C01 | d1 | Frames to Video | G01 · p:3f9a1c20 | kare/C01 + ref 1,5 | 10.0 s · sessiz · 1920x1080 | ✅ kullanılabilir 01.2–04.6 | |
| 16.10 | C01 | d2 | Frames to Video | G01 · p:3f9a1c20 | kare/C01 + ref 1,5 | 8.0 s · sessiz · 1920x1080 | ❌ el tokaya eriyor 03.1 → hareket | |
Ret nedeninin sonuna hatanın DOĞDUĞU YER yazılır (AGENTS.md §3):
  → kare · → hareket · → seçim · → kurgu · → anlatım · → ses · → araç
İki deneme AYNI sebeple bozuksa üçüncüsü aynı promptla gönderilmez (AGENTS.md §4).
```

## MONTAJ EŞLEMESİ (hat dışı montaj · `medya.py bol`)

> Montaj hat dışında yapıldıysa (`cikti/` altında taslak/final dışı bir video) `medya.py bol <montaj> <FILM>` kesmeleri bulur.
> QA raporları çekimi **kesme sırasıyla** sayar; plan numarası değildir. Her QA bulgusu bu tablodan plan çekimine çevrilir.

| Kesme sırası (QA no) | Zaman | Plan çekimi | Deneme | Nasıl doğrulandı (kare · benzerlik) |
|:--:|---|:--:|:--:|---|

## RED (üretim reddi)

| Tarih | Çekim | Mesajın BİREBİR metni | İlerleyip sonda mı düştü | Değişen şey | Sonuç |
|---|:--:|---|:--:|---|:--:|

## TARAMA (Gemini · `uretim_hatti/QA_PROMPTLARI/TARAMA.md`)

| Tarih | Video / kare modu | Zaman | Çekim (`kurgu.py liste`) | Tür (T1-T14) | Ne görüldü | Gemini | İnsan doğrulaması |
|---|---|---|:--:|---|---|:--:|:--:|
| 2026-10-22 | video | 00:22 - 00:29 | C03 | T2 BODY-GROUND CLIPPING | Dev yaratığın sol kanadı bulut kütlesini yarmak yerine bulutun içinden hayalet gibi geçiyor | LIKELY | Doğrulandı |
| 2026-10-22 | video | 00:36 - 00:39 | C04 | T1 HAND-OBJECT FUSION | İnsansı karakterin sağ el parmakları yavrunun alt gövdesiyle kaynaşıp şekil değiştiriyor | LIKELY | Doğrulandı |
| 2026-10-22 | video | 00:51 - 00:53 | C06 | T6 LOOK CHANGE | Kucaktaki yavru yaratığın sırtından aniden ejderha/yarasa benzeri iki büyük mavi kanat açılıyor | SURE | Doğrulandı (yeniden üretim önceliği) |
| 2026-10-22 | video | 01:21 - 01:26 | C09 | T13 SLIDING / EMPTY GRIP | Karakter taş iskelenin üzerinde yürürken ayak tabanları ıslak zeminde ağırlıksız kayıyor | LIKELY | Doğrulandı |
| 2026-10-22 | video | 01:33 - 01:38 | C10 | T9 WRONG FLOATING | Dalga çarptığında iskelenin ucundaki dev kaya bloğu köpük gibi hafifçe havaya kalkıp devriliyor | SURE | Doğrulandı |
| 2026-10-22 | video | 01:41 - 01:47 | C11 | T13 SLIDING / EMPTY GRIP | Yavru uçup gittikten sonra karakter ellerini 6 saniye boyunca kaskatı açık tutmaya devam ediyor | SURE | Doğrulandı |
| 2026-10-22 | video | 01:52 - 01:57 | C12 | T8 WRONG SOUND | Yalnızca yerde yatan yavru varken mikrofona çok yakın yetişkin insan nefes alma/iç çekme sesi duyuluyor | SURE | Doğrulandı (kurguda sessize alınacak) |
| 2026-10-22 | video | 02:01 - 02:02 | C13 | T8 WRONG SOUND | Ağzı olmayan uzaylı çömelirken çok net ham insan hıçkırık/iç çekme sesi ("Hıı-ah") duyuluyor | SURE | Doğrulandı (kurguda sessize alınacak) |
| 2026-10-22 | video | 02:06 - 02:09 | C13 | T6 LOOK CHANGE | Yerde yatan yavrunun kafasından aniden parlayan iki adet anten uzuyor | SURE | Doğrulandı (yeniden üretim önceliği) |
| 2026-10-22 | video | 02:13 - 02:14 | C14 | T8 WRONG SOUND | Ağzı olmayan uzaylı yavruyu okşarken tamamen doğal insan "Hmm" mırıldanması duyuluyor | SURE | Doğrulandı (kurguda sessize alınacak) |
| 2026-10-22 | video | 03:05 - 03:09 | C19 | T2 BODY-GROUND CLIPPING | Yavru yaratık kanada konduğunda alt gövdesi ve sol yüzgeci kanadın içine gömülüp kaynaşıyor | LIKELY | Doğrulandı |
| 2026-10-22 | video | 03:11 - 03:18 | C20 | T8 WRONG SOUND | Karakter kanada yaslanmışken mikrofona çok yakın insan nefes sesi ve "Hmm" mırıldanması duyuluyor | SURE | Doğrulandı (kurguda sessize alınacak) |
| 2026-10-22 | video | 03:21 - 03:29 | C21 | T11 OTHER | Kanat yükselirken sol uçurumun kuru üst yüzeyinden yoktan var olan dev şelale akıyor | SURE | Doğrulandı |
| 2026-10-22 | video | 03:34 - 03:39 | C23 | T8 WRONG SOUND | Bulutlar üzerinde uçulurken mikrofona çok yakın oda akustiğinde insan nefes ve "Hmm" sesi duyuluyor | SURE | Doğrulandı (kurguda sessize alınacak) |
| 2026-10-22 | video | 03:50 - 03:55 | C24 | T3 / T10 | Ekranın ortasında MOONMOTHER başlık kartı yer alıyor (son 5 saniye) | SURE | Kabul (başlık kartı) |

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

| Tarih | Sürüm | Kesme no · zaman | Çekimler (önce → sonra) | Tür (S1-S7) | Önce → sonra | Gemini | Karar (düzeltildi · kabul · yanlış alarm) |
|---|---|---|---|---|---|:--:|---|
| 2026-10-22 | moonmother_01 | Kesme 01 · 00:10.0 | C01 → C02 | S4 WORLD JUMP | Bulutlar ve halkalı gezegen → turuncu ay/güneş yansıması | SURE | Kabul (açılış akışı) |
| 2026-10-22 | moonmother_01 | Kesme 01-23 | Tüm kesmeler | S7 SOUND JUMP | Her 10 saniyelik klip geçişinde dalga ve müzik sesi bıçak gibi kesilip sıfırdan başlıyor | SURE | Kurguda kesintisiz yatak döşenecek |
| 2026-10-22 | moonmother_01 | Kesme 04 · 00:40.0 | C04 → C05 | S5 STATE RESET | Anne yaratığın göz altı ışıkları C04'te yanarken C05'te sönük başlayıp yeniden yanıyor | SURE | Kabul |
| 2026-10-22 | moonmother_01 | Kesme 05 · 00:50.0 | C05 → C06 | S1 LOOK JUMP | Kucaktaki yavru yüzgeçli formdan aniden ejderha/yarasa kanatlı forma dönüşüyor | SURE | Yeniden üretim adayı |
| 2026-10-22 | moonmother_01 | Kesme 05 · 00:50.0 | C05 → C06 | S6 PHYSICS MISMATCH | Gökyüzünde dağ/gezegen ölçeğindeki yaratık denizde aşırı küçülüyor | SURE | Yeniden üretim |
| 2026-10-22 | moonmother_01 | Kesme 06 · 01:00.0 | C06 → C07 | S3 DIRECTION FLIP | Yaratık sağdan sola süzülürken kesmede aniden soldan sağa dönüyor | SURE | Kurguda yön kontrolü |
| 2026-10-22 | moonmother_01 | Kesme 07 · 01:10.0 | C07 → C08 | S1 LOOK JUMP | Yavrudaki ejderha kanatları kayboluyor, yavru tekrar küçük yüzgeçli formuna dönüyor | SURE | C06 düzeltmesiyle çözülür |
| 2026-10-22 | moonmother_01 | Kesme 08 · 01:20.0 | C08 → C09 | S5 STATE RESET | Karakter iskelenin henüz başındayken kesmede bir anda en uç noktasına varmış yürüyor | SURE | Kurguda kısaltma |
| 2026-10-22 | moonmother_01 | Kesme 09 · 01:30.0 | C09 → C10 | S5 STATE RESET | Karakter iskelenin ucundayken kesmede iskele boş görünüyor ve dalga ucu yıkıyor | SURE | Kurguda bağlantı yumuşatılacak |
| 2026-10-22 | moonmother_01 | Kesme 10 · 01:40.0 | C10 → C11 | S5 STATE RESET | İskele yıkılmışken karakter kesmede tekrar sağlam ve yüksek uçurumda duruyor | SURE | Kabul |
| 2026-10-22 | moonmother_01 | Kesme 11 · 01:50.0 | C11 → C12 | S5 STATE RESET | Yavru uçarak uzaklaşmışken kesmede hiçbir düşüş olmadan ıslak kayalarda bitkin yatıyor | SURE | Kurgusal geçiş yumuşatılacak |
| 2026-10-22 | moonmother_01 | Kesme 13 · 02:10.0 | C13 → C14 | S1 LOOK JUMP | Yavrunun kafasındaki iki anten ve karın ışığı kesmede aniden tamamen kayboluyor | SURE | C13 düzeltmesiyle çözülür |
| 2026-10-22 | moonmother_01 | Kesme 16 · 02:40.0 | C16 → C17 | S6 PHYSICS MISMATCH | Denizden orta boyda çıkan yaratık yakın çekimde tekrar bulutlar arasında devasa ölçekte | LIKELY | Kabul |
| 2026-10-22 | moonmother_01 | Kesme 20 · 03:20.0 | C20 → C21 | S5 STATE RESET | Karakter kıyıda kanada yaslanıp veda ederken kesmede bir anda kanadın üstüne binmiş havalanıyor | SURE | Kanada biniş kurguda düzeltilecek |
| 2026-10-22 | moonmother_01 | Kesme 22 · 03:40.0 | C22 → C23 | S2 LIGHT JUMP | Gece mavisinden bir anda sağ ufukta parlak altın gün doğumuna ve aydınlanan kanada geçiş | SURE | Dramatik ışık geçişi, kabul |

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|
| 2026-10-22 | moonmother_01 | C01-C05 | Zırhlı karakterin yavruyu koruması ve gökteki dev anneyle kurulan ışık bağı | Dev yaratıkla yavrunun aynı türe ait olduğu ve çağrı bağı net anlaşıldı | Evet |
| 2026-10-22 | moonmother_01 | C06-C10 | Karakterin yavruyu iskeleye taşıması ve dalganın iskeleyi yıkması | Yavruyu göndermek istediği anlaşıldı ancak iskelenin yıkılmasıyla ilişki kısmen havada kaldı | Kısmen (A1) |
| 2026-10-22 | moonmother_01 | C11-C14 | Yavrunun uçurulduktan sonra düşüp kayalıklarda bitkin kalması ve karakterin şefkati | Düşüş anı gösterilmediği için şaşırtıcı oldu ama şefkat ve bağ çok iyi anlaşıldı | Kısmen |
| 2026-10-22 | moonmother_01 | C15-C19 | Dev annenin kıyıya yaklaşıp kanadını uzatması ve yavrunun kanada konması | Annenin yardıma gelişi ve yavrunun yuvaya dönüşü tam anlaşıldı | Evet |
| 2026-10-22 | moonmother_01 | C20-C23 | Karakterin de kanada binip bulutların üstüne, halkalı gezegene uçması | Mutlu son ve adalet duygusu anlaşıldı; ancak veda jestinden sonra ani biniş kafa karıştırdı | Kısmen (A1) |

Duyulan replikler (madde 7) ↔ `FILM.md` §5 · A3/A4 satırları:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|
| 2026-10-22 | moonmother_01 | 01:52 | A4 | Yerde yatan yavru ekrandayken işlenmemiş insan nefes/iç çekişi | — | Kurguda sessize alınacak (Mute) |
| 2026-10-22 | moonmother_01 | 02:01 | A4 | Ağzı olmayan uzaylı çömelirken ham insan iç çekmesi/hıçkırık ("Hıı-aah") | — | Kurguda sessize alınacak (Mute) |
| 2026-10-22 | moonmother_01 | 02:13 | A4 | Yavruyu okşarken mikrofona çok yakın insan mırıldanması ("Hmm") | — | Kurguda sessize alınacak (Mute) |
| 2026-10-22 | moonmother_01 | 02:22 | A4 | Dalgalar çarparken insan iniltisi/seslenmesi ("Huuu...") | — | Kurguda sessize alınacak (Mute) |
| 2026-10-22 | moonmother_01 | 03:11 & 03:17 | A4 | Kanada yaslanmış bakarken ham insan nefesi ve "Hmm" sesi | — | Kurguda sessize alınacak (Mute) |
| 2026-10-22 | moonmother_01 | 03:34 - 03:38 | A4 | Bulutlar üstünde uçulurken mikrofona yakın insan nefes ve "Hmm" sesi | — | Kurguda sessize alınacak (Mute) |

## İZLEME (insan · `IZLEME_FORMU.md`)

| Tarih | Kim | Sürüm | Cevaplar |
|---|---|---|---|
| 2026-10-22 | A (Sahip Taslak) | taslak_01 | 1: Kısmen (01:30 iskele, 01:50 düşüş, 03:20 biniş kopuk) · 2: Hayır (00:52 ejderha kanadı, 02:07 anten, 02:23 ölçek) · 3: 00:10 gezegen kaybı, 00:52 kanat, 02:07 anten · 4: Şefkat sahneleri iyi; 01:46 ve 02:01 yapay · 5: Replik yok; 01:52, 02:01, 02:13, 03:17, 03:38 insan nefes/mırıldanmaları yapay · 6: Her 10 sn geçişte ses kesiliyor; uzaylıda ham insan sesi var · 7: 01:10–01:29 arası çift yürüyüş planı · 8: Görsel olarak huzurlu ve epik ama veda ile birlikte gitme çelişiyor |
| 2026-10-22 | B0 (AI İzleyici) | taslak_01 | 1: Koruyucunun yavruyu anneye kavuşturması · 2: Yavruyu doğasına kavuşturmak · 3: Hırçın dalgalar ve yavrunun uçamaması · 4: Yavru kavuştu, karakter de birlikte gitti · 5: İnsan nefes sesleri uzaylıyla uyuşmuyor · 6: Yavrunun düşüşü ve kanada ani biniş · 7: İskelede çift yürüyüş · 8: Epik ve huzurlu (teknik ses kusurlu) |

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 17.10.2026 | Fable birleştirmesi (KÜÇÜK): G01 C01 C03 C04 C08 YEDEK Video metinlerine ORTAK GÖRÜNÜM cümlesi birebir eklendi | denetci F5.8: DV G02G03 B13'ün KABUL'ü (yedek Video ORTAK cümleyle biter) G01'e uygulanmamıştı; metin değişikliği yalnız kanonik cümlenin eklenmesi (yeni-film §2 c). |
| 17.10.2026 | Üretim dosyaları G01-G03; PILOT.md pilot kaydı | Sahip pilotu beklemeden F5'e geçti; C01 · C06 · C20 ve 4 referans promptu F5 eleştirileriyle değişti. |
| 17.10.2026 | F5 girdisi (süreklilik): C21 · C22 · C23 kare promptlarında Oru "yüzgecin sığ kıvrımının içinde dinleniyor"; 3.ANNE ⑩ paneli o çekimlerde anahtar cümleyle adlandırılır | C20 sahip kararı (yüzgeç Oru'yu sarar) C20'nin sonunda kalıyor; yonetmen C21-C23 satırlarına dokunmadı (`ODA/F3p_yonetmen_1.md` not 3). |
| 17.10.2026 | 3.ANNE sayfası 10 panel (⑩ sol yüzgeç ucu kıvrık) | C20 sarma jesti + yedek A/B "kıvrık uç" karesi ister; referans sayfaları henüz üretilmedi → v1'e girer, ek üretim yok. |
| 17.10.2026 | FILM §3 ORTAK GÖRÜNÜM = goruntu-yonetmeni önerisi (planın ortak cümlesinden ışık ve "Clean image without lettering, logos, or watermarks" çıktı; yerine "plain unmarked surfaces") | DERS Y6 (ortak cümle ışık taşımaz; C24 şafak ışığıyla çelişirdi) · BILINEN_TUZAKLAR §C (olumsuz yazı kelimesi kadraja basılabilir). Plan sapması → sahip onayı. |
| 16.10.2026 | F3 animatik sayımları düzeltildi (`F3_animatik_1` 14/9/1 → 15/8/1 · `F3_animatik_2` 15/7/2 → 16/6/2) | Denetçi F3 Ö2b: Fable'ın elle saydığı satır tablonun kendisiyle tutmuyordu; tablodan yeniden sayıldı. |
| 16.10.2026 | Bütün alt ajanlar **Sonnet** (`model: sonnet`), AJAN_GOREVLERI haritasında opus olanlar dahil (senarist · dramaturg · yonetmen · denetci · kapak-tasarimcisi) | Sahip: "bol bol sonnet kulan". |
| 16.10.2026 | Görev metinlerine tek satır "Ek okuma (sahip isteği: kılavuzların hepsi)" + ilgili kılavuz yolları eklenir (yalnız dosya adı ve bölüm; yorum, gerekçe yok). İzleyici şablonuna hiçbir şey eklenmez (AGENTS §1 ⑧) | Sahip: "klavuzların hepsine bakmayı unutma". 16.10 kılavuzlarından KIMLIK_VE_REFERANS · REPLIK_VE_KLIP_SESI · UZAY_FIZIGI_GORUNTU hiçbir ajan ya da skill dosyasında anılmıyor; GPT_IMAGE_OMNI yalnız goruntu-yonetmeni'nde, SECIM_VE_KURGU yalnız kurgucu'da (grep, 16.10.2026). |
| 16.10.2026 | Üretim yolu **GPT Image (referans + kare) → Gemini Omni 1.1 Flash (video, Gemini uygulaması)**; §4 Flow modu sütunu "Frames to Video" (tek başlangıç karesinden video, THE_SKY_CATCH ile aynı) | Sahip planı ("GPT Image'a ekle" · "Omni görüntü girdisi"). Yöntem `uretim_hatti/GPT_IMAGE_OMNI_KILAVUZU.md`; araç olguları `FLOW_GERCEKLERI.md` Ek 2-3. Gemini uygulamasında ayrı başlangıç/bitiş karesi yok → zincir yok (F3b ajansız). |
| 16.10.2026 | REPLIK **yok** | Plan: "Konuşma yazılmadı; sesler nonverbal"; üç canlı da konuşmuyor. Çağrılar (üç notalı motif) efekt katmanıdır: F4 ses tasarımı. Gerekçe FILM §5 altında. |
| 16.10.2026 | Model sesi **KAPALI** — video promptunda ses tarifi yazılmaz; planın her video promptundaki "Sound: …" satırları ve ortak ses kuyruğu F4 efekt listesine taşınır | Hat sözleşmesi (AGENTS §2: model sesi istisnası yalnız §5 replik; film_dogrula DERS Y13 — SKY 24/24). Plan da aynı yönde: "iyi bir çağrıyı sonraki karşılıklarda aynı kayıt veya aynı ses tasarımı olarak kullanmak". → PLANDAN SAPMA listesi (sahip onayı). |

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 16.10.2026 | F2/1 | senarist | sonnet | ODA/SAHIP_PLANI.md + kılavuzlar | ODA/F2_senarist_1.md | §1 kart + S1-S24 tretman + 4 sapma önerisi; 20 tur sınırında durdu, dosya bütün |
| 16.10.2026 | F2/1 | dramaturg | sonnet | F2_senarist_1.md §1-§2 | ODA/F2_dramaturg_1.md | ÖLÜMCÜL 0 · CİDDİ 6 · KÜÇÜK 3 |
| 16.10.2026 | F2/1 | izleyici | sonnet | METİN: §2 "Ne olur" sütunu, 24 satır | ODA/F2_izleyici_1.md | amaç 9-11. satırda · son tuttu · 5-7'de bırakırdı |
| 16.10.2026 | F2/2 | senarist | sonnet | F2_senarist_1 + dramaturg + izleyici + karşılaştırma | ODA/F2_senarist_2.md | 16 bulgu cevaplı (RED: B2 S5 · B6 S15 · K6 · İ6); 12 sapma |
| 16.10.2026 | F2 kapı | denetci | sonnet | KABUL Ö + F2 · ODA F2 dosyaları · FILM §1-§2 | ODA/F2_denetci_1.md | KAPANABİLİR · mekanik ❌ yok · yargı Ö4 (B6-S16) → AŞILAN KAPILAR |
| 16.10.2026 | F3/1 | yonetmen | sonnet | FILM §1-§2 + SAHIP_PLANI + kılavuzlar | ODA/F3_yonetmen_1.md | 24 çekim · 4 ref sayfa · 10 karar · pilot risk sırası |
| 16.10.2026 | F3/1 | teknik-danisman | sonnet | FILM §3-§4 + kılavuzlar | ODA/F3_teknik-danisman_1.md | ÖLÜMCÜL 0 · CİDDİ 8 · KÜÇÜK 7 |
| 16.10.2026 | F3/1 | kurgucu | sonnet | KURGU GÖZÜ: FILM §4-§5 | ODA/F3_kurgucu_1.md | 7 soru · ÖLÜMCÜL 0 · CİDDİ 4 · KÜÇÜK 5 |
| 16.10.2026 | F3/1 | izleyici | sonnet | METİN: §4 "Ekranda görünen", 24 satır | ODA/F3_izleyici_1.md | amaç C09'da tutmadı (ÖLÜMCÜL, F3_animatik_1) · "8-9'da bırakırdım" |
| 16.10.2026 | F3/2 | yonetmen | sonnet | F3_yonetmen_1 + 4 eleştiri dosyası | ODA/F3_yonetmen_2.md | 20 tur sınırı, dosya bütün · ÖLÜMCÜL C09 düzeltildi · 5 yeni sapma |
| 16.10.2026 | F3/2 | izleyici | sonnet | METİN: §4 "Ekranda görünen" tur 2, 24 satır | ODA/F3_izleyici_2.md | tuttu 16 · kısmen 6 · tutmadı 2 [sayım düzeltildi] (C06 akrabalık, C09 amaç) · 14-16'da bırakırdı |
| 16.10.2026 | F3 kapı | denetci | sonnet | KABUL Ö + F3 · ODA F3 dosyaları · FILM §3-§4 | ODA/F3_denetci_1.md | KAPANABİLİR · yargı Ö2b (sayım, düzeltildi) · F3.2 · F3.3 → AŞILAN; 20 tur sınırı, SendMessage devamı |
| 16.10.2026 | F3p | goruntu-yonetmeni | sonnet | PİLOT MODU: C01 C06 C20 + FILM §3-§4 + plan + F3_yonetmen_2 §4 + kılavuzlar | PROMPTLAR/PILOT.md | 25 kimlik cümlesi · ORTAK GÖRÜNÜM önerisi · 4 ref sayfası · 3 çekim · iş emri · film_dogrula ✅; 25 tur sınırı, dosya bütün |
| 16.10.2026 | F4/1 | ses-tasarimcisi | sonnet | FILM §1-§5 + plan ses + F3_kurgucu soru 6 | ODA/F4_ses-tasarimcisi_1.md | §0-§11 (sahne · ortam · çağrı kayıt listesi · E-kodları · efekt 24/24 · yatak · geçiş · müzik kısıtları · miks); API kesintisi yazımdan sonra |
| 16.10.2026 | F4/1 | besteci | sonnet | FILM §1-§5 + plan müzik briefi | ODA/F4_besteci_1.md | §7 + dinamik tablo + MÜZİK PROMPTU taslağı; 3 açık karar; 15 tur sınırı → SendMessage devamı |
| 17.10.2026 | F3p | yonetmen | sonnet | sahip kararı C16 + C20 · FILM §4 | ODA/F3p_yonetmen_1.md | C16 + C20 yeni satır · ⑩ panel önerisi · C21-C23 süreklilik notu |
| 17.10.2026 | F4/1 | kurgucu | sonnet | F4_besteci_1 + F4_ses-tasarimcisi_1 + FILM §4 | ODA/F4_kurgucu_1.md | ÖLÜMCÜL 0 · CİDDİ 12 · KÜÇÜK 8 (iki plan paralel) + hakem önerisi |
| 17.10.2026 | F3p/2 | goruntu-yonetmeni | sonnet | PILOT.md + FILM §3-§4 (C20 yeni) | PROMPTLAR/PILOT.md (önceki: ODA/F3p_goruntu-yonetmeni_1_PILOT.md) | C20 sarma + 3.ANNE ⑩ + kimlik satırı; 25 tur sınırı, diff ile tam |
| 17.10.2026 | F4/2 | ses-tasarimcisi | sonnet | F4_ses_1 + F4_besteci_1 + F4_kurgucu_1 + F4_hakem_1 + FILM §4 | ODA/F4_ses-tasarimcisi_2.md | B1-B20 KABUL · perde D–E–A · §8b 28 R satırı · 3 açık karar |
| 17.10.2026 | F4/2 | besteci | sonnet | F4_besteci_1 + F4_ses_2 + F4_kurgucu_1 + F4_hakem_1 | ODA/F4_besteci_2.md | 19 KABUL · 1 KISMEN RED · müziksiz 76,2 s · prompt taslağı |
| 17.10.2026 | F4 kapı | denetci | sonnet | KABUL Ö + F4 · ODA F4 dosyaları · FILM §6-§7 | ODA/F4_denetci_1.md | KAPANABİLİR · yargı F4-ek (§6↔§7 iki hücre) → AŞILAN; 20 tur sınırı, SendMessage devamı |
| 17.10.2026 | F5/1 | goruntu-yonetmeni | sonnet | G01 (C01-C08) + FILM §3-§4 + PILOT.md (C01 C06 + ref birebir) + kılavuzlar | PROMPTLAR/G01.md | C01-C08 + 4 ref; pilot bölümleri birebir; 25 tur sınırı, dosya bütün |
| 17.10.2026 | F5/1 | devamlilik | sonnet | G01 + FILM §3-§4 | ODA/F5_devamlilik_1_G01.md | 8 soru · ÖLÜMCÜL 0 · CİDDİ 4 · KÜÇÜK 11 |
| 17.10.2026 | F5/1 | teknik-danisman | sonnet | G01 risk sütunu C01-C08 + ref | ODA/F5_teknik-danisman_1_G01.md | ÖLÜMCÜL 0 · CİDDİ 6 · KÜÇÜK 9; 15 tur sınırı, SendMessage devamı |
| 17.10.2026 | F5/1b | goruntu-yonetmeni (G01 yazarı, SendMessage) | sonnet | TD + DV + ODA/F5_birlestirme_1_G01.md | PROMPTLAR/G01.md | 30 bulgu cevaplı · C02 2 ref · yeni ışık satırı |
| 17.10.2026 | F5/1 | goruntu-yonetmeni | sonnet | G02 (C09-C16) + G01 örnek + FILM §3-§4 | PROMPTLAR/G02.md | C09-C16 · iki geçişli kare C09 C11 C16 · 2 yeni kimlik satırı; 25 tur sınırı → SendMessage |
| 17.10.2026 | F5/1 | goruntu-yonetmeni | sonnet | G03 (C17-C24) + G01 örnek + PILOT C20 + FILM §3-§4 | PROMPTLAR/G03.md | C17-C24 · C20 PILOT'tan · 2 yeni kimlik satırı; 25 tur sınırı → SendMessage |
| 17.10.2026 | F5/1 | devamlilik | sonnet | G02 + G03 (8 soru) + gruplar arası G01-G03 | ODA/F5_devamlilik_1_G02G03.md | 16 × 8 soru · ÖLÜMCÜL 0 · CİDDİ 8 · KÜÇÜK 11; 20 tur sınırı → SendMessage |
| 17.10.2026 | F5/1 | teknik-danisman | sonnet | G02 + G03 risk | ODA/F5_teknik-danisman_1_G02G03.md | ÖLÜMCÜL 0 · CİDDİ 10 · KÜÇÜK 6; 15 tur sınırı → SendMessage |
| 17.10.2026 | F5/1b | goruntu-yonetmeni (G02 yazarı, SendMessage) | sonnet | TD + DV + ODA/F5_birlestirme_1_G02G03.md | PROMPTLAR/G02.md | bulgular cevaplı (2 RED) · ≤4.106 |
| 17.10.2026 | F5/1b | goruntu-yonetmeni (G03 yazarı, SendMessage) | sonnet | TD + DV + ODA/F5_birlestirme_1_G02G03.md | PROMPTLAR/G03.md | bulgular cevaplı · gök bulut üstü satırı · ≤4.149 |
| 17.10.2026 | F5 kapı | denetci | sonnet | KABUL Ö + F5 · G01-G03 · ODA F5 dosyaları · FILM §3-§4 | ODA/F5_denetci_1.md | KAPANABİLİR · yargı Ö2b · F5.8 (Fable birleştirdi) · C06 yan notu; 20 tur sınırı → SendMessage |
| 17.10.2026 | F6/1 | kapak-tasarimcisi | sonnet | FILM §1 §3 §4 + plan kapağı + G01 ref + kılavuzlar | ODA/F6_kapak-tasarimcisi_1.md | 3 aday A/B/C · NOT A MOON ya da yazısız · film adı yok |
