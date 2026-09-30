# ✅ THE_LAST_GATE — ÜRETİM ÖNCESİ KONTROL (`03_PLAN_ONCESI` 18 madde)

> Her satır ÖLÇÜMLE kapanır; "yazdım" kanıt değildir. Koşu: 30.09.2026.

| # | madde | durum | kanıt (ölçüm / komut) |
|:--:|---|:--:|---|
| A0 | hikâye onayı var mı | ✅ | `00_HIKAYE_ONAYI.md` · ONAY 30.09.2026 · 25 sahne satırı · klip toplamı 96 · jargon 0 (㉙ temiz) |
| A1 | yasak ↔ anlatım çelişkisi | ✅ | ⭐ EN PAHALI HATA burada çıktı ve çözüldü: negatif ④ "no symbols" ↔ sahibin "özgün rozetler" çelişkisi. Çözüm sözlük değil DİL değişikliği: `textless` amblem. Artık ikisi aynı yöne bakıyor. |
| A2 | sahne sayısı tutuyor mu | ✅ | `grep -c '^## 🎬 KLİP' *BOLUM*` = 96 · `# 📍 SAHNE` = 25 · SAHNE PLANI toplamı 96 (㉜① temiz) |
| A3 | süre tutuyor mu | ✅ | 96 × 10,000 s = 960,000 s = 16:00 · 24 fps'te 23.040 kare · kurgu kapısı ±0 |
| A4 | yasaklı sahne tipi var mı | ✅ | biniş/iniş hareketin ORTASINDAN [D69]: K13 (omurgada zaten ilerliyor) · K33 (kapıdan geçiş) · K83 (koridorun ortası) · K85 (içeri girer, koltuğa oturur). Binişin TAMAMI hiçbir klipte yok. Kask çıkarma 0 kare. Ceset/yara 0 kare. |
| A5 | 1 numaralı risk SAYIYLA mı | ✅ | risk = kalabalık okuması. Sayıyla: en büyük tek kadraj **8 insan** (K37) · "one to a bay" · panik 0 klip · `04_UYARI_NOTLARI` §1 |
| B1 | doruk bir sahnenin İÇİNDE mi | ✅ | K92 · S24'ün 2/3 klibi. Temas/geçiş iki sahne ARASINA düşmüyor; klip kıç ucu çıkana kadar kesilmiyor (SPEC B FİNAL VURUŞ KANITI) |
| B1b | katmanlı dünya → ışık takvimi | ✅ | ışık yatağı 25 sahnede 25 satır · kaynaklar adlandırılmış · klip içinde geri yanma yok [D193] |
| B2 | bedelli seçim var mı | ✅ | K23 seçim → K30/K32 bedel. Bedel bir ARAÇ (görülür), bir duygu değil. Bedenin karşılığı K88 (eli boşta). |
| B3 | tema hangi klipte EKRANA çıkıyor | ✅ | S06 (K22 kanca) · S17 (K67 bağ) · S23 (K89 kolu Lina indirir) · S25 (K95–K96 selam). Nesne: emniyet bağı/kancası. |
| B4 | açı yayı yazıldı mı | ✅ | 16 kurulum · 5 ölçek · 3 açı tipi · ardışık aynı kurulum 0 çift · 7 bölüm sınırı çifti ≥1 ölçek + ≥45° (`03_SAHNE_SIRALAMASI` §4) |
| B5 | İSTEK · ENGEL · BEDEL · MUHATAP | ✅ | PLAN §B5 · BEDEL klip numaralı (K30–K32 · K69–K72 · K91) · ⑰ kapısı temiz |
| B5b | AYRILIK (iki insanlı) | ✅ | S06 · K21–K23 · nesne emniyet kancası · ikincil ayrılık S17 |
| B5c | üretim sırası | ✅ | PLAN §ÜRETİM SIRASI · referans paketi KAPI 0 · hook EN SON · 4 iptal kapısı |
| B6 | politika satırı ve anlam maliyeti | ✅ | PLAN §POLİTİKA · şiddet sözlüğü 0/184 (negatif blok dâhil) · ⑯ kapısı temiz · silah adlandırılmıyor |
| C | referans paketi | ✅ | 21 sayfa yazıldı, KAPI 0 · 6 tetikleyicinin 5'i ateşliyor · sayfa↔klip bağlaması paket §5'te |
| D | SPEC tamlık | ✅ | 7/7 makine çapası dolu (㉔ temiz) · PART GRID 4 satır + FULL |
| E | makine kapısı | ✅ | `prompt_kontrol.py yatay_16_dk_filmler/THE_LAST_GATE` → **klasör modu ✅ GO · 0 BLOCK** · 184 prompt · image 101-244 · video 199-261 kelime |

## ⚠️ AÇIK BIRAKILAN — kapanmadı, kapanmış GİBİ yazılmadı

```
⬜ KLİP SÜRESİ    araçtan ölçülmedi [D124]; 10 s KURGU birimi olarak sabit
⬜ ⭐VİRAL        8 aday klip ölçülmedi; hedef sayı YAZILMADI
⚠️ DÖNÜŞ %8-33   ölçüldü, hedefin altında, GEREKÇELİ (PLAN §⑩④) — ölçüm randevusu
                  TAM FİLM ⑫+④; rapor "kesmeler kafa karıştırıyor" derse iskelet değişir
⚠️ D79 vizör      BOLUM_1'de vizör cümlesi YOK çünkü K05–K12'de yüz taşıyan klip yok;
                  ㉖ kadrajda olmayan yüzü tarif ETMEYİ yasaklıyor. Yapısal, düzeltilmez.
⚠️ SENKRON        32 repliğin 11'i ekranda ağız — sahibin açık kararı, ölçüm randevusu var
⚠️ RED #13        K19 iki eldiven + CU: kompozisyon reddi sınıfına yakın, İZLENECEK
⬜ ÜRETİM         0 kare. T01–T08 testleri koşulmadı.
```
