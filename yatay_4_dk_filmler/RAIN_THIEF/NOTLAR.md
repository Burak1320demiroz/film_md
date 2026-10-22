# 📒 RAIN_THIEF — Notlar

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
| 2026-10-22 | video | 00:04 - 00:09 | C01 | T13 SLIDING / EMPTY GRIP | Karakter taş zeminde koşuyor ancak ayakları kayıyor, arka plan akmıyor (yerinde koşma) | SURE | Doğrulandı (kurguda kırpılacak) |
| 2026-10-22 | video | 00:31 - 00:40 | C04/C05 | T1 HAND-OBJECT FUSION | Makro yakın çekimde parmaklar metal vana ve tüpün cam çeperiyle hafifçe kaynaşıyor | LIKELY | Doğrulandı |
| 2026-10-22 | video | 01:11 - 01:20 | C10 | T13 SLIDING / EMPTY GRIP | Merdivende tırmanma animasyonu var ancak 9 saniye boyunca aynı basamakta yerinde sayıyor | SURE | Doğrulandı (izleyici terk noktası) |
| 2026-10-22 | video | 01:34 - 01:36 | C12 | T6 LOOK CHANGE | Sol elde fırtına tüpü varken sağ elde aniden yoktan ikinci bir metal silindir beliriyor | SURE | Doğrulandı (çift tüp hatası) |
| 2026-10-22 | video | 01:51 - 02:00 | C14 | T6 LOOK CHANGE | Tenteden kayarken kafa yapısı, kulak boyu ve pelerin kısa yeleğe dönüşüyor | SURE | Doğrulandı (kıyafet morfu) |
| 2026-10-22 | video | 02:01 - 02:08 | C15 | T3 TEXT | Satıcı tezgâhındaki yapı üzerinde bozuk yabancı/alfasayısal yazılar parlıyor | LIKELY | Kabul |
| 2026-10-22 | video | 02:57 - 03:04 | C21 | T12 WEIGHTLESS EFFORT | İri muhafız uzaylıyı tek elle havada tutuyor; pelerinde ve bedende yerçekimi/ağırlık hissi sıfır | SURE | Doğrulandı (ağırlıksız kaldırış) |
| 2026-10-22 | video | 03:13 - 03:18 | C23 | T13 SLIDING / EMPTY GRIP | Mavi vana çarkını çevirirken eller metal yüzeyde kayıyor, fiziksel kavrama zayıf | LIKELY | Doğrulandı |

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

| Tarih | Sürüm | Kesme no · zaman | Çekimler (önce → sonra) | Tür (S1-S7) | Önce → sonra | Gemini | Karar (düzeltildi · kabul · yanlış alarm) |
|---|---|---|---|---|---|:--:|---|
| 2026-10-22 | raın_thıef_01 | Kesme 01 · 00:10.0 | C01 → C02 | S4 WORLD JUMP | Gökyüzünde tek halkalı gezegen ve bakır çeşme → iki gezegen ve taş çeşme | SURE | Kabul (açılış akışı) |
| 2026-10-22 | raın_thıef_01 | Kesme 02 · 00:17.5 | C02 → C03 | S4 WORLD JUMP | İki gezegen sağ üstte → tek halkalı gezegen sol üstte | SURE | Kabul |
| 2026-10-22 | raın_thıef_01 | Kesme 03 · 00:24.5 | C03 → C04 | S1 LOOK JUMP | Düz cam kavanoz tüp → metal dikmeli fener/kapsül tasarımı | SURE | Referans sabitleme notu |
| 2026-10-22 | raın_thıef_01 | Kesme 04 · 00:31.5 | C04 → C05 | S1 LOOK JUMP | Çıplak mavi el → dokulu mavi eldiven ve vanalı tüp ucu | SURE | Makro çekim farkı, kabul |
| 2026-10-22 | raın_thıef_01 | Kesme 06 · 00:48.5 | C06 → C07 | S7 SOUND JUMP | Ekranda çarpışma yokken patlayan yüksek metalik çarpma/uğultu sesi | SURE | Kurguda ses efekti silinecek |
| 2026-10-22 | raın_thıef_01 | Kesme 11 · 01:30.5 | C11 → C12 | S1 LOOK JUMP | Düz cam tüp → pirinç fener kafesli tüp (ve 01:34'te 2. silindir çıkması) | SURE | Yeniden üretim / kırpma |
| 2026-10-22 | raın_thıef_01 | Kesme 13 · 01:50.5 | C13 → C14 | S1 LOOK JUMP | Sarı pelerinli uzun kulak → sarı yelekli ve düz kafa yapılı morf | SURE | Yeniden üretim adayı |
| 2026-10-22 | raın_thıef_01 | Kesme 17 · 02:26.5 | C17 → C18 | S7 SOUND JUMP | 02:21'de aniden kesilen müzik kesmeyle birlikte aniden tekrar başlıyor | SURE | Kurguda müzik çapraz geçişi yapılacak |
| 2026-10-22 | raın_thıef_01 | Kesme 18 · 02:36.5 | C18 → C19 | S7 SOUND JUMP | Tüp yuvaya takılırken çalan müzik kesmeyle bıçak gibi kesiliyor | SURE | Kurguda müzik sürekliliği sağlanacak |
| 2026-10-22 | raın_thıef_01 | Kesme 20 · 02:56.5 | C20 → C21 | S5 STATE RESET | Küçük fırtına tüpü ve yatay çark → dev cam silindir ve dikey dümen çarkı | SURE | Öncelikli yeniden üretim (çark yönü) |
| 2026-10-22 | raın_thıef_01 | Kesme 21 · 03:04.5 | C21 → C22 | S5 STATE RESET | Dikey dümen çarkı → tekrar yatay vana çarkı ve küçük tüpe dönüş | SURE | C21 çark yönü düzeltmesiyle çözülür |
| 2026-10-22 | raın_thıef_01 | Kesme 22 · 03:12.5 | C22 → C23 | S1 LOOK JUMP | Pelerinsiz düz yeşil tunik → kahverengi deri askılı/kayışlı gömlek | SURE | Kurguda devamlılık kabulü |
| 2026-10-22 | raın_thıef_01 | Kesme 23 · 03:22.5 | C23 → C24 | S1 LOOK JUMP | Yaşlı uzaylının yüz rengi ve formu C04 sahnesine göre pembe/mora dönmüş | SURE | Renk düzeltme / kabul |

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|
| 2026-10-22 | raın_thıef_01 | C01-C03 | Kett'in çaldığı hava tüpüyle şehirden kaçmak istemesi | Çaldığı tüple gemiye binip kaçmak istediği net anlaşıldı | Evet |
| 2026-10-22 | raın_thıef_01 | C04-C05 | Tula'nın çiçeğine acıyıp bir damla su vermesi | Kuruyan çiçeğe bir damla su verip canlandırdığı anlaşıldı | Evet |
| 2026-10-22 | raın_thıef_01 | C06-C09 | Kaçış gemisinden vazgeçip havayı değiştirmeye karar vermesi | Gemiyi feda edip şehre yağmur yağdırmayı seçtiği anlaşıldı | Evet |
| 2026-10-22 | raın_thıef_01 | C10-C14 | Kuleye tırmanış ve Vorr'dan kaçış | Kuleye tırmandığı ve muhafızdan kaçtığı anlaşıldı | Kısmen (01:11 tırmanışta yerinde sayma) |
| 2026-10-22 | raın_thıef_01 | C15 | Satıcının dikkat dağıtıp destek olması | Satıcının "Free delivery!" demesi ve kol çekmesi anlaşılamadı | Hayır (A1) |
| 2026-10-22 | raın_thıef_01 | C18-C23 | Fırtına tüpünü konsola kilitleyip vana çarkını çevirmesi | Pelerinini feda edip çarkı çevirerek sistemi başlattığı anlaşıldı | Evet |
| 2026-10-22 | raın_thıef_01 | C24-C25 | Herkes için bedava yağmur yağması ve adaletin sağlanması | Halkın sevinci, adalet hissi ve muhafızın şaşkınlığı tam anlaşıldı | Evet |

Duyulan replikler (madde 7) ↔ `FILM.md` §5 · A3/A4 satırları:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|
| 2026-10-22 | raın_thıef_01 | 00:42 | A3 | "Your ship's leaving" duyuluyor ancak satıcının ağzı kıpırdamıyor | R03 | ADR / kadraj dışı ses kabulü |
| 2026-10-22 | raın_thıef_01 | 00:48 | A4 | Yüz yakınlaşırken aksiyonsuz patlayan yüksek metalik çarpma/uğultu | — | Kurguda ses efekti silinecek |
| 2026-10-22 | raın_thıef_01 | 00:51 | A3 | "Pour in" ("Four in" gibi) ifadesi eylemle (tüpü yuvaya takmak) uyuşmuyor | R04 | Kurguda miks/replik revizyonu |
| 2026-10-22 | raın_thıef_01 | 01:05 | A3 | "Buying an umbrella..." repliğinde arka plandaki satıcının ağzı kapalı | R05 | ADR / ses miksi |
| 2026-10-22 | raın_thıef_01 | 03:24 | A3 | "How much? For once... nothing" aynı ses söyledi, ağız kapalı | R09 | Soru ve cevap iki ayrı sese bölünecek |
| 2026-10-22 | raın_thıef_01 | 03:34 | A3 | Muhafız pelerini tutarken replik "coat" yerine "note" olarak duyuluyor | R10 | TTS revizyonu: "coat" |

## İZLEME (insan · `IZLEME_FORMU.md`)

| Tarih | Kim | Sürüm | Cevaplar |
|---|---|---|---|
| 2026-10-22 | A (Sahip Ön Denetim) | raın_thıef_01 | 1: Kısmen (01:34, 02:01 anlaşılmıyor) · 2: Hayır (01:51 yelek, 03:08 kıyafet değişimi) · 3: 00:04 ve 01:11 yerinde sayma, 01:34 çift tüp · 4: Dudaklar oynamıyor (00:42, 01:05, 03:24, 03:34), 02:57 ağırlıksız kaldırış · 5: "Pour in", "note" telaffuz hatası · 6: 00:48 darbe sesi, 02:21 ve 02:37 müzik kesintisi · 7: 00:04 ve 01:11 · 8: Adalet hissi görsel olarak tatmin edici, ses/kurgu kusurları var |
| 2026-10-22 | B0 (AI İzleyici) | raın_thıef_01 | 1: Mavi uzaylı kaçmak yerine kuleye çıkıp şehre yağmur yağdırıyor · 2: Gemiyi bırakıp herkese bedava su vermek · 3: İri muhafız ve yüksek kule · 4: Evet, yağmur yağdırdı ama gemisini ve pelerinini kaybetti · 5: Ağızlar oynamıyor, "note" duyuluyor · 6: 01:34 eldeki tüp değişimi, 02:01 "Free delivery" kol çekme · 7: 01:11 merdivende yerinde sayma · 8: Umutlu (fakat teknik pürüzlü) |

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 19.10.2026 | Plan ↔ hat: içerik planın; hat M kuralları yalnız biçim (referans numarası, `Reference <No>` anahtarı, 10 s vuruş öneki, `"<line>"` tırnağı, ≤4.300, zincir dili ve başka çekime atıf yok); HİPOTEZ/TERCİH çatışırsa plan korunur | Sahip varsayılanı (BLACK_ACCORD 18.10.2026 "plandan asla dışarı çıkma"; hafıza feedback-sahip-plani-sapma-yok). |
| 19.10.2026 | Kett iki referans: 1.KETT (plan R01) + 2.KETT_TULUM (plan R02, R01 düzenlemesi); §3 satırında SAHİP İSTİSNASI; `film_dogrula.py` bu işarette ikinci sayfayı hata değil uyarı sayar (araca tek satır, tarihli yorumla) | Sahip cevabı "Plan geçerli" (19.10.2026). Plan C22/C24'te yalnız R02'yi ister: ponçolu panel o karelere gitmesin. |
| 19.10.2026 | Model sesi kullanılmaz; §5 Kaynak "ağız kadrajda — temiz replik ayrı kayıt" (videodaki replik oyunculuk ve ağız ipucu) · ekran dışı cevaplar "kadraj dışı" | Plan §7 "Ses uygulaması" + "Ekran dışındaki replikte görünür başka bir ağzı hareket ettirme". |
| 19.10.2026 | Biçim düzeltmeleri (M): C01 Görsel "The first frame already reveals" → "The frame already reveals" · C05 Görsel "from the previous shot" silinir · C05 Video'dan kadraj dışı konuşma cümlesi ve diyalog bloğu çıkar (R04 kurguda) · ORTAK HAREKET'in "spoken lines … recorded separately" cümlesi repliksiz çekimlerde ve C05'te atılır · Mara "speaking mouth" → kare promptunda "mouth" | film_dogrula M: zincir dili · başka çekime atıf · Görsel/Video'da konuşma kelimesi (model söylemeyecekse). Planın anlamı değişmez (`ODA/F5_yazim_karari.md`). |
| 19.10.2026 | DERS Y6 (ORTAK GÖRÜNÜM'de "one pale ringed planet", ışık paleti) · plan korundu | Plan §6 ortak görünüm birebir; HİPOTEZ uyarısı plan lehine bırakılır. |
| 19.10.2026 | Kapak: planın tek kapak fikri ve yazısız istemi birebir (A/B açılmadı); kapak yazısı RAIN THIEF (plan) | Plan §11; KAPAK_VE_BASLIK §6 "film adı yazılmaz" tercihi plan lehine. F6 ajansız. |
| 19.10.2026 | §5 R01 saniyesi 1,0 → 2,2 (ses-tasarimcisi; ILK_30 "ilk 2 s insan sesi yok") | Saniye Fable tahminiydi (biçim); planın repliği ve çekimi aynı. |
| 19.10.2026 | Biçim (M): C19 Video plan cümlesi "End with him within a few steps of the console, reaching distance in the next shot." → "… within reaching distance." | film_dogrula ATIF ("next shot"); anlam aynı. |
| 19.10.2026 | FILM §5 R06 saniyesi 3,3 → 4,5 (TD1 B7: önce gemiye bakış) · §3 KİMLİK'e 8 numara "konsol, dolu yuva" satırı (DV2 B21; G03'te 6 promptta aynı cümle) | Biçim (Fable tahmini saniye) · birebir denetlenebilirlik. |
| 19.10.2026 | Prompt uzunluğu: plan metni aynen + ardına plan malzemesi (Görsel 2.000-3.200 · Video 1.000-1.500) | Sahibin BLACK_ACCORD tercihi ("sanki promtlar kısa" → "plan aynen + sonuna ek"); plan istemleri 330-530 / 230-420 karakter. |

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 19.10.2026 | F5/1 | goruntu-yonetmeni (çağrı 1) | sonnet | plan · FILM §3-§5 · ODA/F5_yazim_karari.md | PROMPTLAR/G01.md | C01-C08 + 9 referans + KİMLİK 39 satır (FILM §3'e birebir); film_dogrula G01 temiz; Görsel 1.815-2.921 · Video 783-1.182 kr. Sadakat betiği: 9 plan cümlesi birebir değil (uzatılmış/birleşmiş/silinmiş) + C05 ref 5 düşürülmüş + C03 plan ses cümlesi silinmiş → revizyon (önceki sürüm ODA/F5_goruntu-yonetmeni_1_G01.md) |
| 19.10.2026 | F4/1 | besteci (çağrı 2) | sonnet | plan §1 §7 §9 · FILM §4-§6 | ODA/F4_besteci_1.md | müzik planı + İngilizce MÜZİK PROMPTU (tek parça 4:00, 120 BPM, D) yalnız plan §9 + §7 ses satırlarından; müziksiz C12 ve C19; FILM §7'ye birebir; film_dogrula muzik ✅; sahibe 5 F8 sorusu (DURUM) |
| 19.10.2026 | F4/1 | ses-tasarimcisi (çağrı 3) | sonnet | plan §4 §7 §9 · FILM §4-§6 · GECIS_VE_SES_SUREKLILIGI | ODA/F4_ses-tasarimcisi_1.md | ORTAM YATAĞI 4 (Y1 pazar · Y2 çatılar · Y3 hava tacı · Y4 yağmur) + GEÇİŞ 23 kesme (20 kesme · 3 karışım) FILM §6'ya birebir; kayıt listesi 20 + efekt listesi 24/24 ODA'da; R01 2,2 s'ye (ILK_30 ilk 2 s) → FILM §5 güncellendi; plan dışı: C17-C18 uzak demir basamak sesi (sahibe) |
| 19.10.2026 | F5/1b | goruntu-yonetmeni G01 revizyon (çağrı 4, SendMessage) | sonnet | sadakat listesi (7 madde) | PROMPTLAR/G01.md | 7/7 uygulandı; sadakat betiği: yalnız izinli 3 biçim farkı (C01 "first frame" · C05 "previous shot" · C05 kadraj dışı konuşma); film_dogrula G01 hata yok, DERS Y2 C05·5 (Tula kadraj dışı, plan referansı) · Y6 · Y8 uyarı |
| 19.10.2026 | F5/1 | goruntu-yonetmeni G02 (çağrı 5) | sonnet | plan · FILM §3-§5 · F5_yazim_karari + "plan cümlesi karakteri karakterine" · G01 örnek | PROMPTLAR/G02.md | C09-C16; sadakat betiği: plan cümleleri birebir (fark yok); film_dogrula G02 hata yok. Plan korundu (DERS Y13 uyarısı plan lehine): C11 "Let the engine fade without dialogue." · C16 "heavy metallic footsteps" · C14 "previously shown" (ATIF değil). C12'de iki tente birlikte: plan Video (pas turuncusu) + plan Devamlılık (mavi rota) — M2'de ikisi de var, çelişki değil |
| 19.10.2026 | F5/1 | goruntu-yonetmeni G03 (çağrı 6) | sonnet | aynı + pilot C21 (plan yedeği) · C23 | PROMPTLAR/G03.md | C17-C24 + C21 plan yedeği (iki kısa görüntü); sadakat: plan cümleleri birebir. film_dogrula 2 M hatası Fable biçim düzeltmesi: C18 ajan eki "from here to the end of the film" → "seated in the socket" · C19 PLAN cümlesi "reaching distance in the next shot" → "within reaching distance" (başka çekime atıf) · yedek dosya adları medya.py kuralına (kare/ara/C21_y1-2 · ham/C21_d3-d4). Sonra 24/24 ✅ |
| 19.10.2026 | F5/1 | devamlilik G01 + devamlilik G02-G03 + teknik-danisman G01 + teknik-danisman G02-G03 (çağrı 7-10, paralel) | sonnet | PROMPTLAR/G01-G03 · FILM §3 | ODA/F5_devamlilik_1_*.md · ODA/F5_teknik-danisman_1_*.md | 4 rapor birebir kaydedildi (transkriptten): ÖLÜMCÜL 0 · CİDDİ 9+9+14+15 · KÜÇÜK 6+13+4+9. Birleştirme `ODA/F5_fable_birlestirme_1.md`: plan cümlesine dokunan öneriler RED (plan) P1-P10 → sahibe; bizim eklerimiz, vuruş sınırları, notlar KABUL |
| 19.10.2026 | F5/1c | goruntu-yonetmeni G01 · G02 · G03 birleştirme geçişi (çağrı 11-13, SendMessage, paralel) | sonnet | ODA/F5_fable_birlestirme_1.md + 4 eleştiri | PROMPTLAR/G01-G03.md | 3 yazar KABUL maddelerini uyguladı, her bulguya cevap (dosya sonu "F5 TUR 1 CEVAPLARI"); sadakat: yalnız izinli 4 biçim farkı; film_dogrula 24/24 ✅; Görsel ort 2.485 (1.731-3.063) · Video ort 973 (655-1.283); son hâl ODA/F5_goruntu-yonetmeni_1c_G0x.md; FILM §3 KİMLİK'e 6 "yemek tezgâhı" satırı (G01 eki) |
| 19.10.2026 | F5 kapı | denetci (çağrı 14) | sonnet | KABUL Ö + F5 · ODA F5 dosyaları · G01-G03 · uyarı cevapları | ODA/F5_denetci_1.md | KAPANAMAZ (mekanik Ö7 · yargı Ö5 F5.7 F5.8 F5.10 F5.11) → Fable: Ö7 düzeltildi, yargılar AŞILAN KAPILAR'da; F5 KAPANDI |
