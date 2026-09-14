# 📊 THE_GRAVITY_ANCHOR — FİLM QA KAYDI

> **Format:** `yatay_2_dk_filmler`
> **Kayıt Tarihi:** 10.09.2026
> **SPEC:** `yatay_2_dk_filmler/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_QA_SPEC.md` (VAR)

---

## 🗂️ HAM RAPOR KAYITLARI
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_KARE_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_DEVAMLILIK_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_SES_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_HIKAYE_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_ARKA_PLAN_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_AKSIYON_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_EFOR_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_KADRAJ_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_OYUNCULUK_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_ISIK_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_HOOK_HAM.md`

---

## ①.5 BETİK KOŞUSU (`rapor_kontrol.py`)

```
SPEC: yatay_2_dk_filmler/THE_GRAVITY_ANCHOR/THE_GRAVITY_ANCHOR_QA_SPEC.md → ①/④/⑥/⑦/⑧ + ⑨-⑫ için MOD D ZORUNLU
PLAN: 10 sahne (THE_GRAVITY_ANCHOR_BOLUM_1.md)

① KARE       🚨 GEÇERSİZ  (SPEC var, rapor MOD V koşulmuş [D129] + SCORES SUMMARY tablosu okunamadı)
② DEVAMLILIK ✅ GO        (Mod V tasarımdır · Skor: 5.5/10)
③ SES        🚨 GEÇERSİZ  (SCORES SUMMARY tablosu okunamadı)
④ HİKAYE     🚨 GEÇERSİZ  (SPEC var, rapor MOD V koşulmuş [D129] + SCORES SUMMARY tablosu okunamadı)
⑤ ARKA PLAN  ✅ GO        (Mod V tasarımdır · Skor: 5.7/10)
⑦ AKSİYON    ⛔ TEKRAR    (SPEC var, rapor MOD V koşulmuş [D129])
⑧ EFOR       ⛔ TEKRAR    (SPEC var, rapor MOD V koşulmuş [D129] + SEVERITY TALLY uyuşmazlığı [D161])
⑨ KADRAJ     🚨 GEÇERSİZ  (SPEC var, PLAN SADAKATİ merceği MOD V koşulmuş [D190])
⑩ OYUNCULUK  🚨 GEÇERSİZ  (SPEC var, PLAN SADAKATİ merceği MOD V koşulmuş [D190])
⑪ IŞIK       🚨 GEÇERSİZ  (SPEC var, PLAN SADAKATİ merceği MOD V koşulmuş [D190])
⑫ HOOK       🚨 GEÇERSİZ  (SPEC var, PLAN SADAKATİ merceği MOD V koşulmuş [D190])

⑤ ÇAPRAZ KAPI:
🚨 KESME YAYILIMI 12 > 1 → Parti GEÇERSİZ (DEVAMLILIK 21, ARKA PLAN 21, AKSİYON 9, KADRAJ 9, OYUNCULUK 9, IŞIK 9, HOOK 9)
🚨 TESLİM EKSENİ — plan 10 sahne, 4 merceğin çoğunluğu 10 sahne [D188] (DEVAMLILIK & ARKA PLAN 22 sahne sapması)
▶ Parti GEÇERSİZ: hiçbir satır T tablolarına girmez (D107 / D129 / D188 / D190).
```

---

## 📝 RAPOR BULGULARI VE DERS DEĞERLENDİRMESİ

### ① KARE & FİZİK BULGULARI (HAM)
- **Beden & Giysi Tutarsızlığı:** Bilek ekranı/cihazı 0:18 (dikdörtgen), 0:30 (dairesel 'M'/'W' logosu) ve 1:01 (tamamen kaybolma) sahnelerinde geometri değiştiriyor.
- **Fizik İhlali:** 0:40 yükselen kayalar 2D asset gibi düzlemsel hareket ediyor; mikro dönme ve kütle ivmesi eksik.
- **Işık & Gölge:** 1:20'de gökyüzünde ikili güneş olmasına rağmen astronot ve monolit tek sert gölge düşürüyor (ikinci gölge eksik).
- **Negatif Kural İhlali:** 1:40'ta ekranda gömülü yazı ("THE GRAVITY ANCHOR") beliriyor (Seri negatif çekirdek ihlali).

### ② DEVAMLILIK BULGULARI (HAM - 5.5/10)
- **Karakter İncelenmesi:** 00:04 (Doğu Asya yüz yapısı) ile 00:14 / 00:50 (Kafkas yüz yapısı) arasında belirgin kimlik ve kemik yapısı kayması (Identity Break).
- **Dünya & Nesne Değişimi:** Monolit ve kapsül dış panelleri sahneler arası şekil ve modül değiştiriyor.

### ④ HİKÂYE VE PACING BULGULARI (HAM - 3.6/10)
- **Hook & Başlangıç:** İlk 40 saniye boyunca hiçbir dramatik durum veya fiziksel anomali gelişmiyor.
- **Bedel & Risk:** Ana karakter hiçbir risk almıyor, hiçbir bedel ödemiyor ("discovery requires contact" teması bedelsiz kalıyor).

### ⑤ ARKA PLAN BULGULARI (HAM - 5.7/10)
- **Horizon & Topology:** 00:00 (S0) ile 00:32 (S7) arasında siluet kayması; sol ağaç kümesinde belirgin çift tepe çam ağacı S7'de düzleşiyor.
- **Depth, Parallax & Scale:** 00:09 (S2) ile 00:41 (S9) arasında ağaç ölçeği derinliği sıkışıyor.
- **Sky & Atmospherics:** S1 (00:04) yoğun kar yağışı S4 (00:18) içinde durgun sise dönüşüyor, S7 (00:32)'de tekrar kar yağışı başlıyor.

### ⑦ AKSİYON BULGULARI (HAM - 9.4/10)
- **Action Beat Ledger:** 7 eylem vuruşu tespit edildi (tümü okunabilir).
- **Tempo & Escalation:** B1-B7 arası (00:00-01:30) monoton fiziksel tempo; vuruşlar arası ivme/temposuzluk eksik.
- **Interface UI:** Bilek HUD arayüzünde S2 (00:18) ile S4 (00:37) arasında yerleşim yönelimi değişimi.

### ⑧ EFOR BULGULARI (HAM - 2.0/10)
- **Strain & Load:** E1-E3 (0:05-0:35) boyunca EVA giysisi içinde hareket ederken sıfır kas zorlanması ve kas yükü (Pattern ⑥ The suit that isn't there).
- **Breath & Recovery:** E4 (0:45) nefes verme sesi/görseli öncesinde hiçbir fiziksel efor sarf edilmemiş (Pattern ⑭ Cost without source).

### ⑨ KADRAJ BULGULARI (HAM - 5.7/10)
- **Rhyme Pair Failure:** S1 (00:00) Setup A kurgusu ile kapanış S10 (01:30) Setup J kurgusu uyuşmuyor, görsel kafiye kırılıyor.
- **Setup String:** ABCDEFGHIJ — 10 farklı kamera pozisyonu.

### ⑩ OYUNCULUK BULGULARI (HAM - 6.3/10)
- **Tempo & Stillness:** S1-S10 (00:00-01:35) boyunca monoton hareket temposu; S6 tereddüdünde yavaşlama eksik.
- **The Central Choice on the Body:** S6-S7 (00:58-01:01) tereddüt ile temas arası geçiş hızlı.
- **Gaze String:** ODUOD OOO DO.

### ⑪ IŞIK BULGULARI (HAM - 5.1/10)
- **Key Direction Continuity:** S1->S2 (00:10) ikiz güneşler arka planda 10:00'dan 01:00'e zıplıyor fakat yüz ana ışığı solda kalıyor.
- **Atmosphere Honesty:** S1, S3 havasız vakum ortamında güneş etrafında volumetric bloom çelişkisi.
- **Exposure Jump:** S7->S8 (01:10) yakın planda kask içi ve yüz 0.5 EV daha parlak zıplıyor.

### ⑫ HOOK BULGULARI (HAM - 7.8/10)
- **Exit & Return:** S10 (01:30-01:40) durağan; 01:40 son jenerik kartı döngü akışını kesiyor.
- **Plateau:** S1-S2 (00:00-00:20) peş peşe yürüme çekimleri tempoları düşürüyor.
- **Share Moments:** S3, S7, S9 bağımsız görsel etkiye sahip.

---

## ⛔ SONUÇ VE AKSİYON
- Raporlar `02_HAM_RAPORLAR/` dizininde saklandı.
- SPEC bulunduğu ve raporlar `MOD V` koşulduğu için [D129 / D190] gereğince T1-T12 tablolarına skor **YAZILMADI**.
- Plan-makara sahne sayısı uyuşmazlığı ve kesme yayılımı farkı [D107] nedeniyle teslim geçersiz sayıldı; yeniden üretim ve MOD D formatında SPEC eşliğinde QA koşusu gerekmektedir.
