# 🧭 DURUM — THE_SNAP_LINE

> `/yeni-film` her açılışta önce bu dosyayı okur. `ADIM`: faz 3'te `çekim` | `sahneleme` | `pilot`, diğer fazlarda `—`. Faz geçişinde, her ajan çağrısından
> sonra ve sahibe soru sorulduğunda güncellenir. Alanların adını değiştirme
> (`film_dogrula.py` okur).

```
FAZ          7
ADIM         üretim
TUR          1
SIRADAKI     Flow üretimi: referanslar (ref/), kareler (kare/) ve pilot denemeleri (ham/ C01, C02, C08)
AJAN_CAGRI   30 / 50
METIN_CAGRI  29 / 30
PILOT        C01, C02, C08 hazır (PROMPTLAR/PILOT.md)
MEDYA        TESLİM ref 3/3 · denenen 0/12 · ✅ 0/12 · timeline 0/12 (22.10.2026 12:00)
FLOW_KREDI   0
SON_GUNCEL   22.10.2026 12:00
```

> 16.10.2026: `METIN_CAGRI` = F1-F6 çağrıları (pilot hariç, tavan 30). `PILOT` = F3p çekimleri + tek satır gerekçe (ya da "sahip: yok").
> `MEDYA` = `medya.py durum` TESLİM satırı + tarih; FAZ ≥ 3p'de her oturum güncellenir. Dosyalar DURUM'dan ilerideyse DURUM düzeltilir.

## AÇIK ÖLÜMCÜL BULGULAR

| Faz | Bulgu | Kaynak (ODA dosyası) | Durum |
|:--:|---|---|---|

## AŞILAN KAPILAR — yayın onayında sahibe gösterilir

| Tarih | Faz | Madde | Denetçi dedi | Fable gerekçesi |
|---|:--:|---|---|---|

## SAHİP CEVAPLARI

| Tarih | Konu | Cevap |
|---|---|---|
| 22.10.2026 | Faz 1 Hikâye Seçimi | Aday A (THE SNAP LINE) seçildi |

## FAZ GÜNLÜĞÜ

| Tarih | Faz | Olay |
|---|:--:|---|
| 22.10.2026 | 0 | Film başlatıldı: THE_SNAP_LINE (yatay 2 dk, 12 çekim, doygunluk dalgıcı) |
| 22.10.2026 | 1 | F1 Hikâye odası: senarist 3 aday üretti, 3 paralel eleştiri alındı, Fable Aday A'yı seçti |
| 22.10.2026 | 1 | Sahip onayı alındı: Aday A (THE SNAP LINE) onaylandı → Faz 2'ye geçildi |
| 22.10.2026 | 2 | F2 Tretman: senarist 12 sahne, diyalog-yazarı 6 replik yazdı; paralel eleştiriler alındı; izleyici amaç/sonuç birebir eşleşti; denetçi onayladı → Faz 3'e geçildi |
| 22.10.2026 | 3 | F3 Çekim listesi: 12 çekim, §3 numaralı referanslar ve AÇILIŞ tablosu yazıldı; teknik, izleyici, kurgucu ve bilim danışmanı onayladı; pilot C01, C02, C08 seçildi → F3p'ye geçildi |
| 22.10.2026 | 3p | F3p Pilot promptları: C01, C02, C08 promptları ve Flow iş emri yazıldı (PROMPTLAR/PILOT.md) |
| 22.10.2026 | 4 | F4 Ses ve müzik planı: ses-tasarımcısı ortam yatağı ve geçiş tablosunu yazdı; besteci Flow Music promptunu (887 kr) yazdı; kurgucu ve diyalog-yazarı onayladı; denetçi kapattı → Faz 5'e geçildi |
| 22.10.2026 | 5 | F5 Promptlar: G01 grubu (C01–C12) Görsel ve Video promptları yazıldı; devamlılık (8 soru) ve teknik danışman onayladı; denetçi kapattı → Faz 6'ya geçildi |
| 22.10.2026 | 6 | F6 Kapak konsepti ve yayın paketi hazırlandı (KAPAK_VE_YAYIN.md, YAYIN_PAKETI.md) → Faz 7'ye geçildi |
| 22.10.2026 | 7 | Referans üretimi tamamlandı: 1.MILLER, 2.MEKAN, 3.MAKAS üretildi ve onaylandı (ref/ 3/3, SHA-256 işlendi) |
| 22.10.2026 | 6 | F6 Kapak konsepti: A/B tek değişken (vizör dehşeti vs. makas eylemi) yazıldı; izleyici, yönetmen ve yayın onayladı; Fable onayladı → Faz 7'ye geçildi |
