# 📒 THE_FALSE_SUN — Notlar

> Bu filmde olan her şeyin günlüğü. Hata burada **ret nedeni** olur, kural olmaz
> (`AGENTS.md` §1 ④). Satır olay olduğu gün yazılır.

---

## İŞARETLEME (sahip · Flow / Gemini'de üretirken)

> Sahip her denemeyi izler ve işaretler: ✅ kullanılabilir (aralıkla) · ❌ değil (tek cümle neden).
> Bu bir onay değil, iş adımıdır; Fable hareketi göremez, seçim bu işaretten başlar.

| Tarih | Deneme dosyası | İşaret | Aralık / neden |
|---|---|:--:|---|

## DENEMELER

| Tarih | Çekim | Deneme | Flow modu | Prompt sürümü | Sonuç | Kredi |
|---|:--:|:--:|---|:--:|---|:--:|

```
Ret nedeninin sonuna hatanın DOĞDUĞU YER yazılır (AGENTS.md §3):
  → kare · → hareket · → seçim · → kurgu · → anlatım
İki deneme AYNI sebeple bozuksa üçüncüsü aynı promptla gönderilmez (AGENTS.md §4).
```

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

Duyulan replikler ↔ `FILM.md` §5:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|

## İZLEME (insan · `IZLEME_FORMU.md`)

| Tarih | Kim | Sürüm | Cevaplar |
|---|---|---|---|

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 12.10.2026 | Sahip planı temel alındı | Sahip hazır ve eksiksiz planı verdi: 2 dk, 12×10 s, tek sabit kokpit kamerası, Nia Ward + ORION AI. ODA/SAHIP_PLANI.md oluşturuldu. |
| 12.10.2026 | Model sesi KAPALI | Sahibin planına uygun olarak tüm konuşmalar kurguda eklenir (dudak senkronu istenmez). |
| 12.10.2026 | Tek sabit kamera sürekliliği | Kamera 28mm sabit göz hizasında sol duvara kilitlidir; zoom/pan/tilt/dış çekim yoktur. |
| 12.10.2026 | Gemini son kareden devam | Sahne uzatma / son kareden devam yöntemi; Flow B zinciri yerine onarım karesi ve bağımsız 10 s parça yaklaşımı uygulandı. |
| 12.10.2026 | 10 s vuruş planı ve ortak görünüm | film_dogrula mekanik kapıları gereği her video promptuna 2-3 vuruşlu zaman planı ve ortak görünüm cümlesi eklendi. |

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 12.10.2026 | 1-5 | Fable | — | SAHIP_PLANI | FILM.md, PROMPTLAR/G01.md, YAYIN_PAKETI.md | Yerleştirildi, kontrol edildi |
