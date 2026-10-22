# 📒 THE_SNAP_LINE — Notlar

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

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 22.10 | F1/t1 | senarist | opus | Brif: 310m sualtı, 2 dk, 1 karakter | `ODA/F1_senarist_1.md` | 3 aday üretildi (A/B/C) |
| 22.10 | F1/t1 | dramaturg | opus | 3 aday | `ODA/F1_dramaturg_1.md` | EN SAĞLAM: Aday A |
| 22.10 | F1/t1 | yonetmen | opus | 3 aday | `ODA/F1_yonetmen_1.md` | A üretilebilir, kesme kurgusu notu |
| 22.10 | F1/t1 | izleyici | sonnet | 3 logline | `ODA/F1_izleyici_1.md` | Seçim: Aday A |
| 22.10 | F2/t1 | senarist | opus | FILM §1 | `ODA/F2_senarist_1.md` | 12 sahne tretman + Karakter 5 satırı |
| 22.10 | F2/t1 | diyalog-yazari | opus | Tretman | `ODA/F2_diyalog-yazari_1.md` | 6 model sesi replik + profiller |
| 22.10 | F2/t1 | dramaturg | opus | Tretman + replikler | `ODA/F2_dramaturg_1.md` | Neden-sonuç sağlam, bedel bedende |
| 22.10 | F2/t1 | izleyici | sonnet | Olay akışı ("ne olur") | `ODA/F2_izleyici_1.md` | Amaç ve sonuç tam anlaşıldı |
| 22.10 | F2/t1 | ses-tasarimcisi | sonnet | Tretman + replikler | `ODA/F2_ses-tasarimcisi_1.md` | Replik haritası + kesintisiz yatak |
| 22.10 | F2/t1 | denetci | opus | F2 kabul listesi | `ODA/F2_denetci_1.md` | F2 kapısı ONAYLANDI (0 hata) |
| 22.10 | F3/t1 | yonetmen | opus | Tretman + replikler | `ODA/F3_yonetmen_1.md` | 12 çekim listesi + AÇILIŞ tablosu |
| 22.10 | F3/t1 | teknik-danisman | sonnet | Çekim listesi | `ODA/F3_teknik-danisman_1.md` | Riskler ve Flow modları onaylandı |
| 22.10 | F3/t1 | izleyici | sonnet | Ekranda görünen sütunu | `ODA/F3_izleyici_1.md` | Görsel akış kusursuz kavrandı |
| 22.10 | F3/t1 | kurgucu | sonnet | Çekim listesi | `ODA/F3_kurgucu_1.md` | 7 kurgu sorusu onaylandı (%100) |
| 22.10 | F3/t1 | bilim-danismani | sonnet | Çekim listesi | `ODA/F3_bilim-danismani_1.md` | Doygunluk fiziği ve dekompresyon doğrulandı |
| 22.10 | F3/t1 | denetci | opus | F3 kabul listesi | `ODA/F3_denetci_1.md` | F3 kapısı ONAYLANDI (0 hata) |
| 22.10 | F3p/t1 | goruntu-yonetmeni | sonnet | C01, C02, C08 | `PROMPTLAR/PILOT.md` | Pilot promptları ve iş emri yazıldı |
| 22.10 | F4/t1 | ses-tasarimcisi | sonnet | FILM §1–§5 | `ODA/F4_ses-tasarimcisi_1.md` | Yataklar, SFX listesi, geçişler |
| 22.10 | F4/t1 | besteci | sonnet | FILM §1–§5 | `ODA/F4_besteci_1.md` | Flow Music promptu (887 kr), sessizlik anı |
| 22.10 | F4/t1 | kurgucu | sonnet | F4 ses/müzik planı | `ODA/F4_kurgucu_1.md` | Doruk susması ve kesmeler onaylandı |
| 22.10 | F4/t1 | diyalog-yazari | opus | F4 ses/müzik planı | `ODA/F4_diyalog-yazari_1.md` | Replik netliği onaylandı |
| 22.10 | F4/t1 | denetci | opus | F4 kabul listesi | `ODA/F4_denetci_1.md` | F4 kapısı ONAYLANDI (0 hata) |
| 22.10 | F5/t1 | goruntu-yonetmeni | sonnet | FILM §3–§4 + PILOT.md | `PROMPTLAR/G01.md` | C01–C12 Görsel ve Video promptları yazıldı |
| 22.10 | F5/t1 | devamlilik | sonnet | PROMPTLAR/G01.md | `ODA/F5_devamlilik_1.md` | 8 devamlılık sorusu onaylandı (%100) |
| 22.10 | F5/t1 | teknik-danisman | sonnet | PROMPTLAR/G01.md | `ODA/F5_teknik-danisman_1.md` | Riskler, modlar ve perdeleme onaylandı |
| 22.10 | F5/t1 | denetci | opus | F5 kabul listesi | `ODA/F5_denetci_1.md` | F5 kapısı ONAYLANDI (0 hata) |
| 22.10 | F6/t1 | kapak-tasarimcisi | opus | FILM §1–§5 | `ODA/F6_kapak-tasarimcisi_1.md` | A/B tek değişken kapak konsepti |
| 22.10 | F6/t1 | izleyici | sonnet | Kapak A/B metinleri | `ODA/F6_izleyici_1.md` | 168x94 ve 120x68 okunurluk onaylandı (Seçim: A) |
| 22.10 | F6/t1 | yonetmen | opus | Kapak A/B | `ODA/F6_yonetmen_1.md` | Vaat sınırı ve ilk 30 saniye teslimi onaylandı |
| 22.10 | F6/t1 | yayin | sonnet | Kapak A/B | `ODA/F6_yayin_1.md` | Önerilen videolar kutusu CTR potansiyeli onaylandı |
