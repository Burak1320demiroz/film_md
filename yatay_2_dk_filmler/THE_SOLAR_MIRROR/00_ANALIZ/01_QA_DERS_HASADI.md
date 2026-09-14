# 🌾 THE_SOLAR_MIRROR — QA VE DERS HASADI

> **Kaynak:** `00_OKUMA_CIZELGESI.md`  
> ⛔ Ders metni kopyalanmaz; bu filme özel **ne yapılacağı** yazılır.

---

## 1. DERS KİLİTLERİ

| Ders No | Başlık / Konu | Bu Filme Düşen Kilit (Prompt ve Kurgu Kuralı) |
|---|---|---|
| **D197** | Kask Vizörü Şeffaflık/Opaklık Geçişi | Kask vizörü tüm kliplerde %100 optik şeffaf glass olarak tanımlanır; hiçbir sahnede ayna/opak kaplamaya dönüşmez. Mara'nın yüzü ve kask içi HUD yansımaları sürekli okunur. |
| **D198** | Sıfır-G Nesne Momentum Kilidi | Plazma kesici S1'de savrulurken veya S7'de Mara boşlukta savrulurken nesneler durağan/statik kalmaz; sürekli ve doğrusal eksensel momentum korur. Havada asılı kalma yasağı. |
| **D201** | Vakumda Güneş Işığı Açısı | 1 km'lik HELIOSTAT dizisinde Güneş açısı tüm sahnelerde sabittir (sağ üstten sert paralel yörünge ışığı). Komşu sahnelerde ışık yönü flip etmez. |
| **D202** | Seçim ve Bedelin Bedenlenmesi | S5'te Mara'nın O₂ divert kararını vermesi, kask içi CU'da göz temasının RCS koluna kilitlenmesi, ellerin titreşimsiz kararlılığı ve derin kinesik reset ile bedenlenir. "Görünmez seçim" YASAK. |
| **D197b** | Doku & Malzeme Koruması | EVA suit kumaşı, göğüs harness'ı ve metal panel yüzeylerinde %0 bloom, plastiksi/balmumu dokusu yasağı. Fotogerçekçi 35mm film grain ve yüzey mikro-çizikleri retained. |
| **D168** | Üretim Sırası Güvenliği | Üretim dramatik sırayla değil, risk/doruk odaklı sırayla yapılır: Referans Paketi → S5 (Doruk) → S6 (Işın) → S11 (Final) → S0 (Açılış) → Kalanlar. |
| **D157** | Novum Taşıyıcı Cümlesi | Novum taşıyıcısı "HELIOSTAT S04 faz-konjugasyon aynası" olup, S0-S2 ve S8-S9 sahnelerinde net optik projeksiyon ile kadrajda taşınır. |
| **D141** | Final Vuruş Kanıtı | S11 final karesinde suit fanı/pompa sesinin ve nefes ritminin sıfırlanması; uzayda süzülen tekil astronot bedeninin durağanlığı kurgu ve ses kanıtıdır. |
| **D124** | Klip Süresi Araç Standartı | Veo 3.1 için 10s hedef klip süresi: 8s temel üretim + 2s extend. Sahneler arası kırpma tablosu kurgu spec'inde tanımlanır. |
| **D122** | Zaman Hesabı Formülü | Replik ve sayaç zamanları otomatik formülle hesaplanır: `T_event = S0_duration + sum(S_i)`. Real-time 30s geri sayım S3-S6 arasında tam 30.0 saniyeye denk gelir. |

---

## 2. QA ARIZALARI (Ölçülmüş Geçmiş İhlaller)

| Kaynak Film / Rapor | Ölçülmüş Arıza | Önleyici Tasarım (THE_SOLAR_MIRROR) |
|---|---|---|
| `THE_GRAVITY_ANCHOR` | Rhyme Broken (Setup A ile A' uyuşmazlığı) | S0 (açılış EWS) ile S11 (kapanış EWS) tamamen aynı lens (35mm), aynı açı ve aynı HELIOSTAT S04 kadrajıyla çekilir. Yalnızca Mara'nın konumu değişir (Kafiye kuralı). |
| `THE_OPEN_CIRCUIT` | Kadraj Aritmetiği İhlali (Ölçek sığmama) | 1 km'lik HELIOSTAT dizisi yalnız EWS (Setup A) kadrajında tam görünür; S04 segmenti (25m) MS/MCU kadrajlarında ölçek şahidi olarak 1.8m astronot ile oranlanır. |
| `THE_TETHERED_MASS` | Replik-Ses Karışıklığı / Göz Teması Eksikliği | Telsiz diyalogları tamamen kask içi hoparlör karakteratiğinde işlenir; Mara konuşurken ağız hareketi aranmaz, göz kilitlenmesi ana anlatı aracıdır. |
| `THE_CRACKED_HELMET` | Kask Vizör Opaklaşması | Tüm görsel promptlarda `optically clear zero-tint spherical visor, fully visible face inside` negatife ve pozitife eksiksiz yazılır. |
| `THE_MIRROR_FAUNA` | Optik Yansıma Deformasyonu | Ayna yüzeyindeki 30s gelecek görüntüsü eriyen CGI yüzey gibi değil, fotogerçekçi optik faz sapması ve piksel decoherence/reconvergence ile gösterilir. |

---

## 3. ÜRETİM RED DEFTERİ SINIFLARI

| Red Sınıfı | Tetikleyici Sözcük / Kompozisyon | Çözüm ve Prompt Temizliği |
|---|---|---|
| **Şiddet / Kan** | Explosions, violent rupture, tearing skin | Sıfır kan/şiddet. Işın etkisi: metal çelik yüzeyde sessiz turuncu-beyaz ergime ve buharlaşma (thermal evaporation). |
| **Milliyet / Bayrak** | Agency logo, national flag, mission patch | Kask ve suit üzerinde hiçbir bayrak, ülke ismi veya ajans amblemi bulunmaz. Nötr rol şeritleri kullanılır. |
| **Metin / Okunabilirlik** | HUD text in prompt, floating numbers in video | Video/Image promptlarına HİÇBİR HUD metni veya rakam yazılmaz. HUD verileri post-kurgu overlay olarak eklenir. |
| **Patlama / Ateş** | Fireball, flame, smoke plume in space | Vakumda ateş ve duman YASAK. RCS ateşlemesi: görünmez gaz genişlemesi ve ince beyaz kristalize gaz parçacıkları. |
| **Plastik / Balmumu Yüzey** | Airbrushed skin, plastic suit finish, CGI look | Negative prompt'a `airbrushed, plastic skin, cgi, 3d render, video game, smooth skin, synthetic look` zorunlu eklenir. |
