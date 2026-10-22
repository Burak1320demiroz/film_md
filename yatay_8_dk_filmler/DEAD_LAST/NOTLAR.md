# 📒 DEAD_LAST — Notlar

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

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

| Tarih | Sürüm | Kesme no · zaman | Çekimler (önce → sonra) | Tür (S1-S7) | Önce → sonra | Gemini | Karar (düzeltildi · kabul · yanlış alarm) |
|---|---|---|---|---|---|:--:|---|

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|

Duyulan replikler (madde 7) ↔ `FILM.md` §5 · A3/A4 satırları:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|

## İZLEME (insan · `IZLEME_FORMU.md`)

| Tarih | Kim | Sürüm | Cevaplar |
|---|---|---|---|

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 20.10.2026 | Plan ↔ hat: içerik planın; hat M kuralları yalnız biçim (referans numarası, `Reference <No>` anahtarı, 10 s vuruş öneki, `"<line>"` tırnağı, ≤4.300, zincir dili ve başka çekime atıf yok); HİPOTEZ/TERCİH çatışırsa plan korunur | Sahip varsayılanı (BLACK_ACCORD 18.10.2026 "plandan asla dışarı çıkma"; hafıza feedback-sahip-plani-sapma-yok). |
| 20.10.2026 | 22 referans: plan kodu → hat numarası (FILM §3); hasar varyantları 20-22 ayrı dosya, SAHİP İSTİSNASI (RAIN_THIEF emsali) · plan M01 → 14.ESKI_DUNYA (AXI kökü 3.AXI ile çakışmasın diye) | Plan "Raka, Thren ve Korv'un hasar varyantları ilgili sağlam araç görselinden düzenlenerek üretilir"; film_dogrula kök kuralı. |
| 20.10.2026 | Model sesi kullanılmaz; §5 Kaynak üç tür (ağız kadrajda · telsiz · makine) | Plan ortak hareket metni; "Ekran dışı iletişim, ikinci yüzü aynı klipte oynatma ihtiyacını azaltır." |
| 20.10.2026 | 50 replik (8 dk bandı 20-40 dışı) · plan korundu | Plan "Toplam 50 İngilizce konuşma sırası, 352 konuşulan sözcük". |
| 20.10.2026 | ILK_30: C01 ilk 2 s yazı (PREVIOUS RACE), C02 insansız yörünge planı · plan korundu | Plan "İlk 10, 30 ve 60 saniye". R01 saniyesi 2,2 (yazı ilk iki saniyede). |
| 20.10.2026 | Biçim düzeltmeleri (M): C01 Görsel "from M01" → "from Reference 14" · "in the very first frame" → "in the frame" · C06 Görsel "The canopy and headrest match C04." silinir (C04 kabin cümlesi ek paragrafta birebir) · C02 · C03 Video'dan diyalog bloğu çıkar (kurguda) · ORTAK HAREKET'in üç konuşma cümlesi ağız repliği olmayan çekimlerde atılır · Thren "speaking mouth" → "mouth", Korv "speaking seam" → "mouth seam" (kare promptunda) | film_dogrula M: referans kodu · zincir dili · META/atıf · konuşma kelimesi (`ODA/F5_yazim_karari.md`). |
| 20.10.2026 | C07-C48 istemleri plan tablosundan yazılır (plan: "bu sonraki 42 klip için … istem çiftleri bu pakette yazılmamıştır"); kadraj planda yoksa yazar seçimi `not` satırında, sahibe liste | Plan istem yazmadığı yerde hat yazar; içerik plan satırı. |
| 20.10.2026 | Biçim/yazım (birleştirme 2): rol etiketlerinde "dead" yerine "dark"; kokpit portrelerinde ekran yönü sabit (pilot sağa bakar, ışık sağdan sola); planda olmayan el temasları kaldırıldı (C24, C45); tek nesne tek ad (flow trail · lock ring/lock circle · link indicators) | `ODA/F5_fable_birlestirme_2.md` L1-L36; plan eylemleri ve replikleri korundu (SK10-SK13). |
| 20.10.2026 | Kapak: planın tek kapak fikri ve yazısız istemi birebir (A/B açılmadı); kapak yazısı DEAD LAST (plan) | Plan "Kapak ve İngilizce yayın paketi"; KAPAK_VE_BASLIK §6 "film adı yazılmaz" tercihi plan lehine. F6 ajansız. |
| 20.10.2026 | Prompt uzunluğu: plan metni aynen + ardına plan malzemesi (Görsel 2.000-3.200 · Video 1.000-1.500) | Sahibin BLACK_ACCORD tercihi; plan C01-C06 istemleri 380-560 / 330-480 karakter. |

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 20.10.2026 | F4/1 | besteci (çağrı 2) | sonnet | plan "Ses, kamera ve ritim" + bölümler + klip tablosu · FILM §1 §4-§6 | ODA/F4_besteci_1.md | müzik planı + İngilizce MÜZİK PROMPTU (tek parça 8:00, iki nabız ~100/92 BPM → C40'ta tek nabız; müziksiz 0:00-0:24 plan C02 notu + 6:50-7:00 C42 öneri); FILM §7'ye birebir; film_dogrula muzik ✅; sahibe 10 F8 sorusu (DURUM) |
| 20.10.2026 | F4/1 | ses-tasarimcisi (çağrı 3) | sonnet | plan ses/ritim + C01-C06 kurgu notları · FILM §3-§6 · GECIS_VE_SES_SUREKLILIGI | ODA/F4_ses-tasarimcisi_1.md | ORTAM YATAĞI 6 (Y1-Y6) + GEÇİŞ 47 (44 kesme · 3 karışım) FILM §6'ya birebir; kayıt listesi 50 + efekt 48/48 ODA'da; §5 saniye: R24 4,5 · R36 4,0 · R38 6,0 · R41 5,5 uygulandı (R01 2,2 zaten); plan dışı 8 öneri uygulanmadı (sahibe); R47 Kaynak FILM'de telsiz kaldı (plan C45 yüz tarif etmiyor) |
| 20.10.2026 | F5/1 | goruntu-yonetmeni G01 (çağrı 4; 25 tur sınırında durdu, dosya tamam) | sonnet | plan · FILM §3-§5 · ODA/F5_yazim_karari.md · RAIN_THIEF G01 biçimi | PROMPTLAR/G01.md | C01-C08 + 22 referans promptu (plan aynen) + KİMLİK 82 satır (FILM §3'e birebir); sadakat betiği: C01-C06 plan cümleleri birebir (izinli biçim farkları + C05 "no humans" → "no human beings": INSANSIZ↔"His" M çakışması); film_dogrula G01 hata yok (DERS Y5 C01 uyarı); Görsel 1.414-2.825 (C01-C04, C06 hedefin altında) · Video 912-1.132 kr |
| 20.10.2026 | F5/1 | devamlilik G01 + teknik-danisman G01 (çağrı 5-6, paralel) | sonnet | PROMPTLAR/G01.md · FILM.md | ODA/F5_devamlilik_1_G01.md · ODA/F5_teknik-danisman_1_G01.md | TD ÖLÜMCÜL 0 · CİDDİ 9 · KÜÇÜK 6 · DV ÖLÜMCÜL 0 · CİDDİ 11 · KÜÇÜK 10; birebir kaydedildi (transkriptten). Birleştirme `ODA/F5_fable_birlestirme_1.md`: KABUL K1-K13 · RED (plan) SK3-SK9 + P10 · F7 4 madde |
| 20.10.2026 | F5/1c | goruntu-yonetmeni G01 revizyon (çağrı 7, SendMessage; bilgisayar uykusu → ajan API hatasıyla düştü, dosya 00:34'te tamamlanmıştı) | sonnet | ODA/F5_fable_birlestirme_1.md + 2 eleştiri | PROMPTLAR/G01.md | K1-K12 uygulandı, 36 bulguya cevap (dosya sonu F5 TUR 1 CEVAPLARI); sadakat C01-C06 temiz; film_dogrula C01-C08 hata yok; Görsel 1.862-3.296 · Video 916-1.105 kr |
| 20.10.2026 | F5/1 | goruntu-yonetmeni G02 · G03 · G04 · G05 · G06 (çağrı 8-12, paralel; auto mod denetimi 5 kez sonuçsuz kaldı, 04:08'de başladı) | sonnet | ODA/F5_grup_gorevi.md (yazım kararı + birleştirme K3-K9 + G01 örnek) | PROMPTLAR/G02-G06.md | 5 ajan ağ kopmasıyla (ENOTFOUND) düştü → SendMessage ile sürdürüldü (aynı çağrı); 40 çekim + C41Y yedeği; ajanların Bash'i yoktu → film_dogrula Fable koştu: 48/48 ✅ (uyarı Y2 C32·20 · Y5 C01 C14 C20 C33 C45 plan renk/su adları); Fable biçim: G02 C10 "engines are sound" → "intact" (ses kelimesi, ajan önerisi) · G03 iş emri notu düzeltildi; Görsel 1.412-3.451 · Video 757-1.303 (bir kısmı hedefin altında → eleştiri sonrası) |
| 20.10.2026 | F5/1 | devamlilik G02-G04 · devamlilik G05-G06 · teknik-danisman G02-G04 · teknik-danisman G05-G06 (çağrı 13-16, paralel) | sonnet | PROMPTLAR/G02-G06 · FILM.md | ODA/F5_devamlilik_1_G02-G04.md · …_G05-G06.md · ODA/F5_teknik-danisman_1_G02-G04.md · …_G05-G06.md | 4 rapor birebir (transkriptten; TDb 15 tur sınırı → SendMessage teslim): TDa 0/11/5 · DVa 0/13/12 · TDb 0/10/6 · DVb 0/10/12 (ÖLÜMCÜL/CİDDİ/KÜÇÜK). Birleştirme `ODA/F5_fable_birlestirme_2.md`: KABUL L1-L36 · RED (plan) SK4 SK8 genişledi + SK10-SK13 · F7 3 madde. FILM §3 KİMLİK G01'den yeniden eşlendi (+2 satır: Raka kollar · eski dünya hâl, DVa B17) |
| 20.10.2026 | F5/1c | goruntu-yonetmeni G02-G06 birleştirme geçişi (çağrı 17-21, SendMessage, paralel) | sonnet | ODA/F5_fable_birlestirme_2.md + 4 eleştiri | PROMPTLAR/G02-G06.md | 5 yazar L maddelerini uyguladı, her bulguya cevap (dosya sonu F5 TUR 1 CEVAPLARI); Fable: FILM §4 Referans C17 C21 C44 C48 + §3 kullanan çekimler · §4 Kadraj sütunu prompt ilk cümlesinden (K13) · rol sözlüğü eki; film_dogrula hepsi ✅ 48/48 (uyarılar `ODA/F5_uyari_cevaplari.md`); sadakat C01-C06 temiz, ağız replikleri birebir; risk kelimesi taraması: yalnız C26 plan repliği "kill" (SK10); Görsel 1.862-3.456 · Video 887-1.350 kr |
| 20.10.2026 | F5 kapı | denetci (çağrı 22) | sonnet | KABUL Ö + F5 · ODA F5/F4 dosyaları · G01-G06 · uyarı cevapları | ODA/F5_denetci_1.md | KAPANABİLİR (mekanik yok · yargı F5.7 F5.8 F5.10 → AŞILAN KAPILAR); Fable 3 doğrulanmamış maddeyi kontrol etti; F5 KAPANDI |
