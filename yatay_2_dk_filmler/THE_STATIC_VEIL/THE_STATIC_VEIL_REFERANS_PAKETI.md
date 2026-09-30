# 🧷 THE_STATIC_VEIL — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK S9 → merkezî seçim S8 → hook S0 → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR. Metin çapası
> aynı CÜMLEYİ okutur, aynı NESNEYİ çizdirmez; modelin girdisi GÖRSELDİR.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Astronot EVA giysisi
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: Kask vizörü ve batarya yuvası
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: Optik fener ve çelik pilon
□ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4 — zaten ZORUNLU)       hangi: —
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: Elektrostatik regolit levitasyonu
□ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: —
```

## 1. 🎫 PAKET KÜNYESİ

```
FİLM: THE_STATIC_VEIL          FORMAT: yatay_2_dk_filmler        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 4K UHD (3840x2160)    SAHNE SAYISI: 12
SAYFA: 2   TOPLAM PANEL: 7   ARİTMETİK: 1 sayfa × 4 panel + 1 sayfa × 3 panel = 7
İMAJ MODELİ + SÜRÜM: Imagen 3       TARİH: 26.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → THE_STATIC_VEIL_KAPAK.md
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | R1 | 4 | Astronot Can — EVA Suit & Kask | 🔴 ZORUNLU | bekliyor | bekliyor | ⬜ TASLAK |
| R2 | R2 | 3 | Pilon & Optik Fener Mekanizması | 🔴 ZORUNLU | bekliyor | bekliyor | ⬜ TASLAK |

```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| A01 | Astronot Can (EVA Giysisi) | insan | S01 | S11 | R1 | Sınıf 1 (Standart EVA) |
| E01 | Optik Fener ve Pilon Montajı | prop / mimari | S00 | S11 | R2 | Sınıf 2 (Mekanik donanım) |
| O01 | Elektrostatik Toz Levitasyonu | olay / ortam | S00 | S09 | R2 | Sınıf 3 (Fiziksel anomali) |

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| A01 | K0 (temel) | Temiz altın vizör, sağlam batarya | S01 | — | R1 p1-p4 |
| A01 | K1 (matlaşma) | Vizör tozla matlaşmış (%40-%80) | S02 | S02 | R1 p4 |
| A01 | K2 (bedel) | Batarya sökük, vizörde 2cm delik, LED'ler sönük | S09 | S09 | R1 p3-p4 |
| E01 | K0 (sönük) | Fener soketi boş, pilon sönük | S00 | — | R2 p1-p2 |
| E01 | K1 (yanan) | Fener kilitli, parlak amber ışık konisi | S11 | S11 | R2 p3 |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 | Dış / Vakum Krater | R2 p1 | Pilon geniş açı | K0 | Dikine yükselen elektrostatik toz partikülleri |
| S01 | Dış / Vakum Krater | R1 p1 | Tam boy arkadan 3/4 | K0 | Adımla havalanan tozun vizöre ilk yapışması |
| S02 | Dış / Vakum Krater | R1 p4 | Vizör yakın plan | K1 | Eldivenle silme ve camın matlaşma sürtünmesi |
| S03 | Dış / Vakum Krater | R1 p2 | Profil MCU | K1 | Parmak uçlarıyla rayı arama kinesik hareketi |
| S04 | Dış / Vakum Krater | R2 p1, R1 p1 | WS genel kurulum | K1 | Pilona varış ve sensör toz birikimi |
| S05 | Dış / Vakum Krater | R2 p2 | ECU soket tırnağı | K0 | Sıkışan soket tırnakları ve el zorlanması |
| S06 | Dış / Vakum Krater | R1 p2 | Göğüs paneli MS | K1 | Topraklama kablosunu sökme eylemi |
| S07 | Dış / Vakum Krater | R2 p2 | ECU şase | K0 | Kablo ucunu sürtme ve zayıf mikro ark |
| S08 | Dış / Vakum Krater | R1 p2, R1 p3 | MCU yandan | K1 | Bataryayı klipsten sökme tereddüdü |
| S09 | Dış / Vakum Krater | R1 p1, R2 p2 | WS doruk vuruşu | K2 | Sert batarya darbesi, 0.3s ark ve ekran sönüşü |
| S10 | Dış / Vakum Krater | R2 p2 | ECU kilit | K1 | Temiz görüş deliğinden bakıp feneri kilitleme |
| S11 | Dış / Vakum Krater | R2 p3, R1 p3 | EWS kapanış | K2 | Yanan amber fener ve kararmış silüetle dönüş |

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · ASTRONOT EVA SUIT

```
IN FRAME: full body, hands, torso, back, face
Scene 1 of 1.
Four-panel character turn-around model reference sheet on neutral neutral-grey backdrop with crisp directional key light and deep geometric shadow.
A single astronaut in a heavy white pressurized composite space suit with dark grey flexible carbon fiber accordion joint seals at shoulders, elbows, and knees. A rigid dark grey chest pack is mounted firmly on the front torso with a mechanical circular gauge on the left wrist cuff. Spherical gold-tinted reflective visor helmet completely concealing the human face under high specular gold mirror reflection with a defined structural composite frame rim, optically clear glass, fully readable through under specular reflection. The back of the suit is one continuous smooth panel from collar to hip, carrying nothing, a flat back silhouette carrying no backpack, no rear pack, no tanks, no oxygen bottles, no hoses. Panel 1: three-quarter full body view. Panel 2: side profile showing suit depth and wrist gauge. Panel 3: direct rear view showing the unbroken smooth flat back panel from neck collar down to waist hem. Panel 4: close-up detail of the gold mirror visor helmet and chest control module.

NEGATIVE: 0% bloom, no lens flare, human count: 1, film grain, photorealistic, no bare skin above the collar, no bare skin at the wrist, no bare skin at the ankle, no human face exposed, no open helmet visor, no back-mounted pack, flat back silhouette, No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark, no CGI render look, no backpack, no air tanks, no rear module, no tools strapped to back, no decals, no flags, no patches.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: bekliyor   SHA-256: bekliyor   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş   p2 · profil — siluet hattı
               p3 · SIRT — düz siluet [D79/D139]   p4 · vizör ardı altın küre [D146]
```

```
KABUL SINAVI (R1):
  KABUL:      Sırt ünitesi sayısı 0, vizör altın yansıtıcı ayna, göğüs paketi tam
  RET:        Sırtta herhangi bir çanta/tüp belirmesi veya vizör arkasında yüz morfolojisi
  YABANCI GÖZ: Paneli göster: "Sırtında çanta var mı?" → Doğru cevap: "Hayır, sırtı tamamen düz panel."
  SONUÇ:      bekliyor
  ⑲ KİMLİK YIĞINI: Kişi başına öznitelik sayısı: 3 (boy/yapı, beyaz kompozit kumaş, altın vizör) ✅
```

---

### 📸 IMAGE PROMPT — SAYFA R2 · PILON & OPTIK FENER

```
IN FRAME: none
Scene 1 of 1.
Three-panel prop and environment reference sheet on dark basalt lunar crater ground with crisp directional solar light and pitch-black vacuum shadow.
A low heavy-duty industrial structural steel pylon anchored into compacted grey regolith on a 20-degree crater slope. A metal ground guide rail made of dark forged steel extends along the basalt terrain. Mounted on top of the pylon is a cylindrical optical beacon housing with hardened mechanical clamp latches and a thick electrical copper grounding terminal. Panel 1: wide angle view of the steel pylon anchored in regolith with fine levitating dust threads rising vertically 1 meter above the ground in vacuum. Panel 2: close-up macro detail of the cylindrical beacon socket, latch teeth, and copper contact terminal coated in fine abrasive grey dust particles. Panel 3: beacon housing activated, projecting a powerful warm amber directional light beam across the dark terrain with zero atmospheric scattering.

NEGATIVE: 0% bloom, no lens flare, human count: 0, film grain, photorealistic, No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark, no CGI render look, no atmospheric haze, no fog, no smoke, no dust falling downward, no wind motion, no fluttering fabric, no soft shadows, no ambient fill light.

Output: 16:9 ratio, 4K resolution, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: bekliyor   SHA-256: bekliyor   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · pilon ve yükselen toz   p2 · mekanik kilit soketi ve tırnaklar   p3 · yanan amber fener
KABUL SINAVI: KABUL pilon oranları ve kilit tırnakları net · RET metin/etiket belirmesi · SONUÇ bekliyor
```

---

## 7. ✅ KABUL KAPISI — üretim başlamadan önce

```
☑ ① PANEL ARİTMETİĞİ  §1 künye toplamı (7) = §2 tablo toplamı (4+3=7)
☑ ② ÇAPRAZ BAĞ        §5'teki her kod (A01, E01, O01) §3'te var; yetim sayfa 0
☑ ③ 120 PX TESTİ      panel 120 px'e inince kask vizörü ve fener soketi ayırt ediliyor
☑ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
☑ ⑤ D79 VİZÖR         altın aynalı vizör kask çerçevesine entegre, kubbe değil [D95/D146]
☑ ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0; pozitif düz kompozit panel tarifli
☑ ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1 (R1), nesne panelinde 0 (R2)
☑ ⑦b GRİ TON          ayrım yüksek kontrast ve parlaklık farkına dayanıyor
☑ ⑧ DURUM ÇİFTİ       merdiven sahneleri tanımlandı
☑ ⑨ ⑲ KİMLİK YIĞINI   öznitelik sayısı ≤3
☑ ⑩ ⑳b DEĞİŞİM        imaj promptları t=0 anını tanımlıyor [D179]
☑ ⑪ ÖLÇEK ŞAHİDİ      pilon ve zemin rayı ölçek şahididir
☑ ⑫ SEED / SHA KAYDI  üretim öncesi tabloya girilecek
☑ ⑬ BAYT AYNILIĞI     paketteki kimlik blokları sahne promptlarıyla uyumlu
☑ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu
```
