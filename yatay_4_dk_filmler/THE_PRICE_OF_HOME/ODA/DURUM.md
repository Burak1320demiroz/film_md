# 🧭 DURUM — THE_PRICE_OF_HOME

> `/yeni-film` her açılışta önce bu dosyayı okur. `ADIM`: faz 3'te `çekim` | `sahneleme`, diğer fazlarda `—`. Faz geçişinde, her ajan çağrısından
> sonra ve sahibe soru sorulduğunda güncellenir. Alanların adını değiştirme
> (`film_dogrula.py` okur).

```
FAZ          7
ADIM         —
TUR          1
SIRADAKI     ⛔ QA REVİZYONU / SES VE KURGU — SAHİPTE. taslak_01 QA raporları değerlendirildi (ODA/QA_DEGERLENDIRME.md). Öncelikli aksiyon: 1) Kurguda video parçalarının gömülü seslerini tamamen susturmak (uzayda rüzgar, uzaylı iç çekişi ve model mırıltılarını yok etmek), 2) Planlanan R01-R27 repliklerini ve iç sesleri eklemek, 3) C02 başına "11 DAKİKA ÖNCE" kartı eklemek, 4) Sahibin onayından sonra gerekli prompt iyileştirmelerini uygulamak.
AJAN_CAGRI   0 / 50
FLOW_KREDI   0
SON_GUNCEL   16.10.2026
```

## AÇIK ÖLÜMCÜL BULGULAR

| Faz | Bulgu | Kaynak (ODA dosyası) | Durum |
|:--:|---|---|---|

## AŞILAN KAPILAR — yayın onayında sahibe gösterilir

| Tarih | Faz | Madde | Denetçi dedi | Fable gerekçesi |
|---|:--:|---|---|---|
| 16.10.2026 | 1-4 | F1 aday turu (senarist · dramaturg · yonetmen · izleyici) · F2 tretman eleştirisi · F3 çekim listesi eleştirisi (teknik · izleyici metin animatiği) · F3b sahneleme · F4 ses/müzik ajanları açılmadı | çağrılmadı | Sahip tam planı verdi ve "gerekli planı hazırla plandan kesinlikle cıkmadan" dedi (THE_MAYDAY_SEA ile aynı yol); hikâye seçimi sahibin onayı sayıldı. §1-§7 plandan birebir yerleşti (ODA/SAHIP_PLANI.md); §6 ORTAM YATAĞI + GEÇİŞ ve §7 MÜZİK PROMPTU planın ses yayı ve müzik taslağından Fable çevirisi. Mekanik kontrol (film_dogrula kunye hikaye cekim replik muzik) geçerli. |
| 16.10.2026 | 5 | F5 prompt eleştiri turu açılmadı (devamlilik · teknik-danisman) | çağrılmadı | Sahip planı birebir uygulandı ve F5 ajansız yazıldı. Bunun sonucunda ortaya çıkan kokpit geometri tuzağı, rozet eksiklikleri ve niyet fiilleri QA raporlarında tespit edilip ODA/QA_DEGERLENDIRME.md'ye not edildi. |
| 16.10.2026 | 6 | F6 kapak konsepti açılmadı | çağrılmadı | Sahip planı üç başlık/kapak adayı veriyor (A sahip tercihi · B · C, YouTube A/B/C testi için); KAPAK_VE_YAYIN §1'e yerleşti. F9'da kapak-tasarimcisi gerçek kareden final türetir. |

## SAHİP CEVAPLARI

| Tarih | Konu | Cevap |
|---|---|---|
| 16.10.2026 | Konu · format · karakter | Sahip hazır planı yapıştırdı: THE PRICE OF HOME, yatay 16:9, 4:00 = 24 × 10 s, iki insan (Eli, Mara) + 1 uzaylı (Vey). "gerekli planı hazırla plandan kesinlikle cıkmadan". |
| 16.10.2026 | Hikâye seçimi (F1 vetosu) | ONAY — planın kendisi; aday turu yok. |
| 16.10.2026 | D1-D10 Açık kararlar | Uygulama planı onaylandı (uygulama_plani.md). Plandaki tercihler korundu; ekran yazıları 4 kelime kuralı için ardışık katmanlara bölündü; model sesi KAPALI kuralı (sesler kurguda). |

## FAZ GÜNLÜĞÜ

| Tarih | Faz | Olay |
|---|:--:|---|
| 16.10.2026 | 0 | Klasör açıldı (`yatay_4_dk_filmler/THE_PRICE_OF_HOME/`, SABLON kopyası) · medya ağacı `~/film_medya/THE_PRICE_OF_HOME/` · sahip planı birebir `ODA/SAHIP_PLANI.md`. |
| 16.10.2026 | 1-4 | FILM.md §1-§7 plandan yerleştirildi (Fable; biçim çevirisi: 7 referans sayfası 1.ELI…7.VEY, 24 çekim 3 grup, replikler kurguda ses, saniye/süre tahmini; §6 yatak Y1-Y3 + geçiş 23 kesme; §7 plan müzik promptu). Ajan çağrısı 0. Kapılar sahip onayıyla aşıldı (AŞILAN KAPILAR). |
| 16.10.2026 | 7 | taslak_01 QA raporları geldi (Anlatım, İzleme A/B simülasyonu, Süreklilik, Tarama). Ham raporlar ODA/HAM_QA_RAPORU.md'ye kaydedildi; değerlendirme ve dersler ODA/QA_DEGERLENDIRME.md ve NOTLAR.md'ye işlendi. |
