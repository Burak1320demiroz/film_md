# 📒 <FILM_ADI> — Notlar

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
