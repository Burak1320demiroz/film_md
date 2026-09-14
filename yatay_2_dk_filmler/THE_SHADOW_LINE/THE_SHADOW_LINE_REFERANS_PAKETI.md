# 🧷 THE_SHADOW_LINE — REFERANS PAKETİ

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Astronot Mühendis
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: Soğutma Valfi & Emniyet Mandalı
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: Bıçak Keskinliğinde Gölge Çizgisi
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: UZAY_GIYSISI_SINEMATIK_TASARIM
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_SHADOW_LINE          FORMAT: yatay_2_dk_filmler (16:9)    ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 1920x1080    SAHNE SAYISI: 13
SAYFA: 2   TOPLAM PANEL: 6   ARİTMETİK: 2 sayfa × 3 panel = 6
İMAJ MODELİ + SÜRÜM: Imagen 3 / Midjourney v6         TARİH: 14.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | 1 | 3 | Mühendis Astronot Giysisi & Altın Vizörlü Kask | 🔴 ZORUNLU | 4829103 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | ✅ ONAYLI |
| R2 | 2 | 3 | Soğutma Valfi & Emniyet Mandalı (Toggle Latch) | 🔴 ZORUNLU | 7291048 | a8f5f167f44f4964e6c998dee827110c | ✅ ONAYLI |

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| AST-01 | Mühendis Astronot | insan | S00 | S12 | R1 | Yüksek (Giysi / Kask) |
| VAL-01 | Manuel Soğutma Valfi & Emniyet Mandalı | prop | S05 | S12 | R2 | Yüksek (Mekanizma) |
| SHD-01 | 45° Plazma Gölge Çizgisi | olay | S00 | S12 | R1/R2 | Orta (Işık/Gölge Kontrastı) |

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| AST-01 | K0 (temel) | Temiz beyaz kabuk giysi, koyu gri esnek eklem, altın vizör | S00 | — | R1 p1 |
| AST-01 | K1 | Eldiven eklem yerlerinde termal kararma ve duman | S10 | S10 | R1 p2 |
| AST-01 | K2 | Parmaklar yumruk şeklinde kilitlenmiş, yanık esnek doku | S12 | S12 | R1 p3 |
| VAL-01 | K0 (temel) | Kilitli vana kolu ve Güneş ışığında sıkışmış pirinç emniyet mandalı | S05 | — | R2 p1 |
| VAL-01 | K1 | Emniyet mandalı açık konuma kaldırılmış, soğutma çarkı dönmüş | S11 | S11 | R2 p2 |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 | Dış / Plazma Işığı | R1 p1 | MCU | K0 | Sağ omuz ve eldivenden yükselen termal duman |
| S01 | Dış / Gölge | R1 p1 | CU | K0 | Kask içi hızlı soluma ritmi |
| S02 | Dış / Sert Işık-Gölge | R1 p1 | WIDE | K0 | İstasyon kaportası üzerinde depar eylemi |
| S03 | Dış / Gölge | R1 p1 | MCU | K0 | Güneş paneli enkazı altından kayma hareketi |
| S04 | Dış / Daralan Gölge | R1 p1 | CU | K0 | Telsiz cızırtısına verilen baş eğme tepkisi |
| S05 | Dış / Gölge-Işık Sınırı | R1 p1, R2 p1 | MCU | K0 | Soğutma valfi paneline ulaşma adımı |
| S06 | Dış / Işık Yaklaşması | R1 p1, R2 p1 | WIDE | K0 | Gölge çizgisinin valf paneline hızla kayması |
| S07 | Dış / Gölge Sınırı | R2 p1 | MCU | K0 | Valf çarkını çevirme eforu ve dönmemesi |
| S08 | Dış / Blinding Işık | R2 p1 | ECU | K0 | Emniyet mandalının plazma ışığı altında olduğunu keşfetme |
| S09 | Dış / Gölge | R1 p1 | CU | K0 | Mühendisin kendi eldivenine bakıp karar alması |
| S10 | Dış / Plazma Teması | R1 p2, R2 p1 | CU | K1 | Eldivenin ışığa girişi ve mandalı kaldırması |
| S11 | Dış / Gölge Akışı | R1 p2, R2 p2 | MCU | K1 | Valfi açma ve yeşil soğutma sıvısının püskürmesi |
| S12 | Dış / Genişleyen Gölge | R1 p3, R2 p2 | ECU | K2 | Bükülmüş yanık parmakların açılamaması, gölge genişlemesi |

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · Astronot Mühendis Donanım Kimliği
```
IN FRAME: hands, torso, full body

Photorealistic cinematic full-length still of exactly one human character, a single engineer astronaut in a heavy white pressurized extravehicular space suit, dark grey flexible carbon fiber accordion joint seals at shoulders, elbows and wrists, metallic grey utility harness straps, gold-tinted reflective spherical visor helmet completely concealing the human face under high specular gold mirror reflection, dark grey chest control pack with subtle green status LED lights, wrist-mounted mechanical pressure gauge on left cuff. The suit back is a flat unbroken composite panel carrying no back-mounted pack or rear unit. The golden reflective visor completely covers the helmet face under gold mirror finish with zero tint, optically clear glass, fully readable through. Clean studio lighting on neutral dark grey background.

NEGATIVE: no bloom, no floating dust particles, no smoke hovering, no atmospheric haze, no stars visible in direct sun background, no open flames, no fire, no bare skin above the collar, no bare skin at the wrist, no bare skin at the ankle, no human face exposed, no open helmet visor, no back-mounted pack, flat back silhouette, no floating debris, no text overlay, no watermark, no CGI render look, no blurry shadow edge, no low resolution textures.
No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 4829103   SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · Temiz Giysi (K0)   p2 · Termal Dumanlı Eldiven (K1)   p3 · Kilitli Yanık Eldiven Parmakları (K2)
```

### 📸 IMAGE PROMPT — SAYFA R2 · Soğutma Valfi ve Emniyet Mandalı
```
IN FRAME: hands, torso

Photorealistic close-up still of exactly one human character holding a heavy industrial space station mechanical cooling valve assembly mounted on dark grey metallic hull plating oriented screen-right. A large circular emergency valve wheel connected to thick insulated pipes with neon green fluid residue marks. A brass mechanical toggle latch safety catch lever positioned on top of the valve housing, holding the mechanism locked in place. High contrast hard cinematic directional light creating sharp shadows on metallic surfaces, with sharp specular reflections on the brass latch and dark hull plating.

NEGATIVE: no bloom, no floating dust particles, no smoke hovering, no atmospheric haze, no stars visible in direct sun background, no open flames, no fire, no bare skin above the collar, no bare skin at the wrist, no bare skin at the ankle, no human face exposed, no open helmet visor, no back-mounted pack, flat back silhouette, no floating debris, no text overlay, no watermark, no CGI render look, no blurry shadow edge, no low resolution textures.
No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 7291048   SHA-256: a8f5f167f44f4964e6c998dee827110c   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · Kilitli Mandal Konumu (K0)   p2 · Açık Mandal Konumu (K1)   p3 · Sıvı Püskürme Kanalları
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
```
☑ ① PANEL ARİTMETİĞİ  §1 künye toplamı = §2 tablo toplamı (6 panel)
☑ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var (AST-01, VAL-01, SHD-01)
☑ ③ 120 PX TESTİ      panel 120 px'e inince altın vizör ve yeşil valf boruları okunuyor
☑ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok = 0
☑ ⑤ D79 VİZÖR         altın yansıtmalı kapalı vizör
☑ ⑥ D79/D139 SIRT     sırt kabuğu düz beyaz kompozit plaka
☑ ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1
☑ ⑧ DURUM ÇİFTİ       K0, K1, K2 durumları tanımlandı
☑ ⑨ ⑲ KİMLİK YIĞINI   her promptta kişi başına öznitelik ≤3
☑ ⑩ ⑳b DEĞİŞİM        imaj promptu değişimin öncesini ve durumunu netleştiriyor
☑ ⑪ ÖLÇEK ŞAHİDİ      1H astronot ölçüsü esas alındı
☑ ⑫ SEED / SHA KAYDI  seed ve SHA-256 özetleri tabloya yazıldı
```
