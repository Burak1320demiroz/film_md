# 🌲 THE GREEN CEILING — FİLM KAYDI

> **Durum:** film üretildi ve birleştirildi · **master ÖLÇÜLMEDİ** 🚨 · **parti GEÇERSİZ**
> **Koşu:** 10.09.2026 · **12 mercek** (① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK).
>
> 🚨 **PARTİ GEÇERSİZ — ①.9 TESLİM KAPISI [D188] & ⑤ ÇAPRAZ KAPI [D107] & SPEC VARLIĞINDA MOD V KARANTİNASI [D190/D184].** Plan 25 sahne, mercekler 16-25 sahne ve 15-30 kesme saydı. `rapor_kontrol.py`: **12 rapor · 12 GEÇERSİZ / KARANTİNA.**
> ⛔ **T1-T12 tablolarına HİÇBİR SATIR YAZILMADI.**
> ⛔ Kesme listesi · REMOVE reçetesi · yeniden üretim **UYGULANMAZ** — önce eksik sahne adıyla saptanır, soru ÜRETİM masasına geçer.

---

## 📦 MALZEME

```
MASTER:    VERİLMEDİ — depoda .mp4/.mov/.mkv yok
SPEC:      yatay_4_dk_filmler/THE_GREEN_CEILING/THE_GREEN_CEILING_QA_SPEC.md ✅ VAR
PAKET:     QA_PROMPTLARI/FILME_OZEL/THE_GREEN_CEILING/ ✅ VAR (12 paket)
PLAN:      25 sahne (BOLUM_1 S0-S12 · BOLUM_2 S13-S24) · 249 s · kart YOK
           İNSAN ŞERİDİ: 11111-11111111111111   (25 hane)
RAPORLARDA: T1 (28 kesme) · T2 (16 sahne / 15 kesme) · T3 (25 kesme) · T5 (25 sahne / 25 kesme) · T6 (24 kesme) · T7 (15 kesme) · T8 (30 kesme) · T9 (21 kesme) · T10 (23 kesme) · T11 (23 kesme) · T12 (24 kesme)
```

---

## §⑪ ÖLÇÜM KAPISI

```
🚨 ÖLÇÜM YAPILAMADI — master yolu verilmedi, depoda video dosyası yok.
   olcum_kapisi.sh koşmadı. Kimlik kapısı (⑪.0) koşmadı.

⛔ Raporların süre / sahne / kesme sayıları HİÇBİR KAPIYA SOKULMADI [skill §1].
⛔ Filigran ekseni ÖLÇÜLMEDİ — raporların 0 yazması ölçüm değildir [D177].
⛔ Ses kanalı ÖLÇÜLMEDİ — T3 raporundaki tam sessizlik şüphesi hakemsiz kaldı.

HAKEM EKSİK. Gereken komut:
   bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master_yolu>"
   → sonra: rapor_kontrol.py --olcum-sahne <n> --olcum-kesme <n>
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py`

Tam çıktı: `RAPOR_KONTROL/RAPORLAR/THE_GREEN_CEILING_20260910_RAPOR_KONTROL.md`

```
TOPLAM 12 rapor · 🚨 12 GEÇERSİZ / KARANTİNA · ⛔ 0 TEKRAR · ⚠️ 0 ŞARTLI · ✅ 0 GO

tekil kararlar (parti düşmeden ÖNCE):
  🚨 GEÇERSİZ ① KARE (SPEC varken Mode V koşuldu · D129)
  ⚠️ ŞARTLI   ② DEVAMLILIK (hücre düzeltmeleri: n=4 Σ=12 ort=3.0 · Identity Break)
  🚨 GEÇERSİZ ③ SES (Summary tablosu okunamadı / sessizlik bayrağı)
  🚨 GEÇERSİZ ④ HİKAYE (Medya eksik bayrağı / Mod V okunamadı)
  ✅ GO       ⑤ ARKA PLAN (n=6 Σ=59 ort=9.8 · Field Holds)
  ⛔ TEKRAR   ⑥ FİZİK (n=8 Σ=39 ort=4.9 · Two Gravities · D129)
  🚨 GEÇERSİZ ⑦ AKSİYON (iddia 73 vs hücre 83 · aritmetik fabrike D161 · D129)
  ⛔ TEKRAR   ⑧ EFOR (n=9 Σ=90 ort=10.0 · D129 / D131 9 hücre düzeltildi)
  🚨 KARANTİNA ⑨ KADRAJ (Skor: 8.5/10 · RHYME BROKEN · SPEC varken Mode V koşuldu · D190/D184 karantina)
  🚨 KARANTİNA ⑩ OYUNCULUK (Skor: 5.2/10 · THE CHOICE IS INVISIBLE · SPEC varken Mode V koşuldu · D190/D184 karantina)
  🚨 KARANTİNA ⑪ IŞIK (Skor: 8.5/10 · KEY WALKS · SPEC varken Mode V koşuldu · D190/D184 karantina)
  🚨 KARANTİNA ⑫ HOOK (Skor: 4.8/10 · HOOK MISSING · SPEC varken Mode V koşuldu · D190/D184 karantina)
```

---

## 🚨 TESLİM VE KESME YAYILIMI KAPISI [D188 · D107]

```
PLAN                     MAKARA / RAPORLAR
25 sahne                 T1: 28 kesme
249 s                    T2: 16 sahne / 15 kesme
başlık kartı: YOK        T3: 25 kesme
İnsansı 25/25            T5: 25 sahne / 25 kesme
                         T6: 24 kesme / 25 sahne
                         T7: 15 kesme / 16 sahne
                         T8: 30 kesme / 31 sahne
                         T9: 21 kesme / 22 sahne
                         T10: 23 kesme / 24 sahne
                         T11: 23 kesme / 24 sahne
                         T12: 24 kesme / 25 sahne
```

- **Teslim Uyuşmazlığı:** Plan 25 sahne tarif ederken, T2 ve T7 16 sahne/15 kesme saydı. 9 sahne/klip farkı mevcuttur.
- **Kesme Yayılımı (D107):** Mercekler arası kesme sayısı yayılımı (30 − 15 = 15 > 1) olduğu için parti toptan **GEÇERSİZ** ilan edilmiştir.

---

## §⑤ MERCEK DETAYLARI VE SKOR ÖZETİ

### 1. ① KARE QA (Mode V) — 🚨 GEÇERSİZ [D129]
- SPEC mevcut olduğu halde Mode V olarak koşulmuştur.
- **Kritik Kusurlar:**
  - *Temas Morflaşması (Contact Morphing):* 0:04 ve 3:10 zaman kodlarında parmaklar/eldivenler çanta kulpu ve kilit mekanizması ile birleşmekte/yapısını kaybetmektedir.
  - *Plastik Yüz Dokusu:* 2:31'de kask içi yüz görünümünde gözenek ve alt yüzey saçılması (subsurface scattering) eksiktir.
  - *Sıfır-G Fizik Hatası:* 0:50'de floating pin nesnesi eksensel dönme momentumu taşımayıp uzayda statik durmaktadır.
  - *Plana Yüzen Yapraklar:* 1:30'da yapraklar 3D kütle hareketi yerine 2D katman gibi durmaktadır.
  - *Yapay Yavaş Çekim Sürüklenmesi (AI Drift):* 1:12'de yürüme adımlarında doğal insan temposu yerine yapay AI yavaşlama kayması görülmektedir.

### 2. ② DEVAMLILIK QA (Mode D/V) — ⚠️ ŞARTLI (Düzeltilmiş Skor: 3.0/10)
- **Hüküm:** `IDENTITY BREAK` (Kimlik Kırılması).
- **Kritik Kusurlar:**
  - *Kimlik/Yüz Değişimi (Cat 1: 3/10):* Kırmızı elbiseli astronotun yüz yapısı (çene genişliği, yaş algısı) sahneler arasında (S1 vs S5 vs S11) radikal biçimde değişmektedir.
  - *Kostüm/Ekipman Sapması (Cat 2: 1/10 & Cat 4: 3/10):* Kask vizörü hiçbir fiziksel müdahale olmaksızın sahneler arası şeffaf ile opak siyah arasında anlık geçiş yapmaktadır. Göğüs logosu sürekli biçim değiştirmektedir (altıgen -> yeşil kare -> kırmızı daire -> sarı üçgen). Çanta biçimleri sahneden sahneye değişmektedir.
  - *Açık Uçlu Nesneler (Open Threads):* S2 (0:10) yüzen plaka, S6 (0:50) yüzen çivi ve S7 (1:00) yüzen bayrak sahneye sokulmuş ancak anlatıda hiçbir şekilde çözülmemiş veya kullanılmamıştır.

### 3. ③ SES QA — 🚨 GEÇERSİZ
- **Kritik Bayrak:** Tüm film boyunca 0dB mutlak sessizlik tespit edilmiştir. Ses kanalının master ihracında eksik veya bozuk olduğu (Audio Absence Flag) doğrulanmalıdır.

### 4. ④ HİKAYE QA — 🚨 GEÇERSİZ
- Medya okunamama ve Mode V şüphelerinden ötürü karantinaya alınmıştır.
- Anlatımsal Not: İlk 15 saniye yavaş yürümeye ayrılmış, karşıt güç (environment) aktif dramatik gerilim yerine pasif atmosfer üretmiştir.

### 5. ⑤ ARKA PLAN QA — ✅ GO (Düzeltilmiş Skor: 9.8/10)
- **Hüküm:** `FIELD HOLDS` (Arka Plan Sahası Tutarlı).
- Dağ silsilesi siluetinde 1:15 ve 2:35 arasında önemsiz (minor) topoloji kayması dışında tüm arka plan katmanları tutarlıdır.

### 6. ⑥ FİZİK QA — ⛔ TEKRAR (Skor: 4.9/10)
- **Hüküm:** `TWO GRAVITIES` (Tek Kadrajda İki Yerçekimi Çelişkisi).
- **Kritik Çelişki:** 0:01'de yağmur 1g hızında düşerken, 0:10'da fırlatılan tablet ve 0:50'de bırakılan çivi havada 0g asılı/yüzer kalmaktadır.

### 7. ⑦ AKSİYON QA — 🚨 GEÇERSİZ [D161 / D129]
- **Hüküm:** Aritmetik Fabrikasyonu (Rapor n=9 Σ=73 iddia ederken hücre toplamı Σ=83 çıkmaktadır) + SPEC varlığında Mode V koşusu.

### 8. ⑧ EFOR QA — ⛔ TEKRAR [D129 / D131]
- **Hüküm:** `THE BODY PAYS`. SPEC varlığında Mode V koşusu; 9 hücre kaynaksız 10/10 olduğu için `—` düzeltmesi almıştır.

### 9. ⑨ KADRAJ QA — 🚨 KARANTİNA [D190/D184] (Skor: 8.5/10)
- **Hüküm:** `RHYME BROKEN` (Kafiye Kırıldı).
- **Kritik Kusurlar:**
  - S1 (00:00, Setup A) ile S22 (03:30, Setup P) açılış ve kapanış kareleri hiçbir boyut, açı, ölçek veya çapa konumunda eşleşmemektedir (`PAIR FAILS`, 🔴 BLOCKER).
  - S8 (01:10) ve S9 (01:20) sahnelerinde kaydırma (tracking) kamerası hareketleri, filmin geri kalanındaki statik lockoff tarzını bozmaktadır.

### 10. ⑩ OYUNCULUK QA — 🚨 KARANTİNA [D190/D184] (Skor: 5.2/10)
- **Hüküm:** `THE CHOICE IS INVISIBLE` (Seçim Beden Üzerinde Görünmez).
- **Kritik Kusurlar:**
  - S06 (00:50): Yerçekimi anomalisini keşfetme ve ele alma anı bedende hiçbir duruş veya ağırlık değişimi üretmemektedir (🔴 BLOCKER).
  - S16 (02:30): Roket kalkışında astronotlar G-kuvveti gerilimi olmadan nötr/manken gibi durmaktadır (🟠 MAJOR).
  - S21 (03:20): Erzak çantasının uzaya kaybolması bedende hiçbir omurga çökmesi veya irkilme bırakmamaktadır (🔴 BLOCKER).

### 11. ⑪ IŞIK QA — 🚨 KARANTİNA [D190/D184] (Skor: 8.5/10)
- **Hüküm:** `KEY WALKS` (Key Işık Yönü Yürüyor).
- **Kritik Kusurlar:**
  - S23 (03:49) -> S24 (03:50): Uzay vakumunda güneş ışığı yönü komşu orbital sahneler arasında 10 yönünden (sol) 2 yönüne (sağ) 120° zıplamaktadır (🔴 BLOCKER).
  - Zone A (Orman tabanı): S07, S08, S09 klipsleri arasında renk sıcaklığı yalpalama ve sis pozlama zıplamaları görülmektedir.

### 12. ⑫ HOOK QA — 🚨 KARANTİNA [D190/D184] (Skor: 4.8/10)
- **Hüküm:** `HOOK MISSING` (Kanca Eksik / Yavaş Açılış).
- **Kritik Kusurlar:**
  - Açılış Penceresi (0:00-0:10): Açılışta 10 saniye boyunca kutu açan astronotlar gösterilmiş, yerçekimi anomalisinin ilk 3 saniyede yer almaması sebebiyle merak sorusu doğmamıştır (0:03 izleyici kaybı tahmini, 🔴 BLOCKER).
  - Kapanış Kartı (4:10-4:15): 4:10'daki jenerik/başlık kartı izleyici döngüsünü öldürmektedir (Ders 70/72).

---

## 🛠️ QA'DEN ÇIKARILAN TEKNİK DERSLER VE KURALLAR

Bu QA koşusu sonucunda depoya kazandırılan/doğrulanan kilit dersler:

1. **[DERS 196] NESNE İLE TEMAS MORFLAŞMASI (CONTACT MORPHING):**
   - *Problem:* Eldiven/parmak nesneye (kasa kulpu, kilit mekanizması) değdiği anda el dokusu nesneyle erir veya formunu kaybeder.
   - *Çözüm:* İmaj promptunda temas anı *sonrası* veya *öncesi* seçilmelidir (`hand positioning near lock without overlapping mesh`). Video promptuna `no merging fingers, crisp glove boundaries, solid metallic handle` eklenmelidir.

2. **[DERS 197] KASK VİZÖRÜ ŞEFFAFLIK/OPAKLIK GEÇİŞİ (VISOR TOGGLE DRIFT):**
   - *Problem:* Kask vizörü müdahale olmadan kareler arası şeffaf yüz görünürlüğü ile opak aynalı siyah görünüm arasında sıçramaktadır.
   - *Çözüm:* İmaj ve video promptlarında vizör durumu TEK NİTELİKLE kilitlenmelidir: ya `always clear transparent glass visor with visible inner face` ya da `always pitch-black reflective opaque mirror visor`. İkisi aynı filmde karıştırılamaz.

3. **[DERS 198] SIFIR-G NESNE EKSENSEL MOMENTUM KİLİDİ (ZERO-G AXIS ROTATION):**
   - *Problem:* Sıfır kütleçekiminde yüzen nesneler (çivi, pim, yaprak) uzayda tamamen donuk/statik durmaktadır.
   - *Çözüm:* Video promptuna `continuous slow micro-rotation around center axis, subtle 3D rotational inertia, no static freeze` eklenmelidir.

4. **[DERS 199] SESSİZ MASTER İHRAC KONTROLÜ (AUDIO TRACK ABSENCE):**
   - *Problem:* Kurgu ihraç edilirken audio stream seçilmediği için master video 0dB mutlak sessizlikle çıkmaktadır.
   - *Çözüm:* İhraç kapısında `ffprobe` ile en az 1 stereo ses akışının mevcudiyeti ve LUFS değerinin `-14.0 LUFS ± 2.0` olduğu otomasyon betiğince doğrulanmadan yayın paketine geçilemez.

5. **[DERS 200] TEK KADRAIDA İKİ YERÇEKİMİ ÇELİŞKİSİ (TWO GRAVITIES / SAME-FRAME CONTRADICTION):**
   - *Problem:* Yağmur/toz 1g hızında düşerken nesnelerin havada 0g asılı durması.
   - *Çözüm:* Yerçekimi anormalliği tanımlanırken kadrajdaki tüm elemanlar (yağmur, toz, nesne) aynı fizik kuralına bağlanmalıdır. Sıfır-g bölgesinde rain/particle düşüşü kapatılmalı veya mikro-g esnemesine çekilmelidir.

6. **[DERS 201] VAKUMDA GÜNEŞ IŞIĞI AÇISI KOMŞU SAHNELERDE FLIP ETTİ (KEY WALKS IN VACUUM):**
   - *Problem:* S23 ve S24 orbital sahneleri arasında uzay güneş ışığı açısının 120° zıplaması (10 o'clock -> 2 o'clock).
   - *Çözüm:* Vakum sahnelerinde solar key direction derece ve kadranla kilitlenmeli (`solar key at 10 o'clock, 45° elevation`), ihlal halinde klip yeniden üretilmelidir.

7. **[DERS 202] HİKÂYENİN MERKEZÎ SEÇİMİ VE BEDELİ BEDENDE OKUNMUYOR (INVISIBLE CHOICE / DRAMATIC BODY READ):**
   - *Problem:* Karakterin kararları (S06) ve dramatik bedeli (S21) beden üzerinde okunmamaktadır.
   - *Çözüm:* Micro-gestures, hesitation, recoil, shoulder slump ve G-force strain prompt seviyesinde beden hareketine yazılmalıdır.

