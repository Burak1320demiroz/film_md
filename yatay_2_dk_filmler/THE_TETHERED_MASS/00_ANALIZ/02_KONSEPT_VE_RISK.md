# 🎯 THE_TETHERED_MASS — KONSEPT VE RİSK ANALİZİ

> **Girdi:** Kullanıcı talebi + `01_QA_DERS_HASADI.md`.
> **Çıktı:** Konsept kapıları, tema eşlemesi, risk kartları değerlendirmesi ve B5 omurgası.

---

## 1. 📋 TALEP VE FORMAT
- **Film Adı:** THE_TETHERED_MASS
- **Format:** `yatay_2_dk_filmler` (16:9, 16 Sahne, 2 Bölüm)
- **Ortam Kartı:** Uzay / Yörünge (§3.2 Uzay Kartı)
- **Klip Süresi:** 10.0 saniye (Araç ayarı: Veo 3.1 Fast / Imagen 3)

---

## 2. 🔑 KONSEPT KAPILARI

| Kapı | Durum | Gerekçe / İnceleme |
|---|:--:|---|
| ① TEK KARE | ✅ PASS | "Karanlık uzayda devasa gergin metal halat ve liflerinin ağır çekimde kopması" — Taşıyıcı nesne: Gergin Metal Halat. |
| ② KİNETİK BAĞIMSIZLIK | ✅ PASS | Halat gerilimi, çekici gemisinin dalışı, istasyonun yükselişi ve serbest kalan halat ucunun dönmesi. |
| ③ BAŞLIK ŞEMASI | ✅ PASS | `THE_TETHERED_MASS` — Mantıksal ve standart 2-3 kelimelik İngilizce isim. |

---

## 3. 🎭 TEMA VE MOTİF MATRİSİ
- **Ana Tema:** BEDEL (Bir insanın kendi yaşamını binlerce koloni kapsülü karşılığında fiziksel bir yörünge takasıyla vermesi).
- **İkincil Tema:** İNSAN-MAKİNE (Otomatik güvenlik sisteminin engeline karşı pilotun manuel olarak koruma pimini sökmesi).
- **Motif:** Beyazlaşan metal lifler, 28Hz sub-bass, yeşil kriyo-kapsül ışıkları, kızaran motor çanı.

---

## 4. ⚠️ RİSK KARTLARI (02_RISK_KARTLARI.md)

1. **Halat Lif Kopma Riski (Yüksek):** Vakum ortamında kıvılcım/ateş çizilmesi fiziksel red verir. *Çözüm:* Kıvılcım yok; metal tel beyazlaşır, kıvrılır, gerilim dalgası ilerler.
2. **Motor İflas/Alev Riski (Orta):** Veo alev gördüğünde magik/fire etiketiyle reddeder. *Çözüm:* Alev yok; kızaran nozzle çanı (red glow), çatlayan soğutma borusundan fışkıran gaz buharı.
3. **Kask Vizör Yansıma Riski (Yüksek):** İç yüzey opaklaşırsa karaktere yabancılaşma olur. *Çözüm:* Vizör %100 şeffaf glass, kokpit ışıkları hafif yansır.
4. **Çoklu Cisim Orantı Riski (Orta):** İstasyon ile çekici aynı kadrajda ölçek kaybedebilir. *Çözüm:* 1H = astronot gövdesi (1.8m) ölçek şahidi olarak istasyon giriş modülünde durur.

---

## 5. 🧱 B5 HİKÂYE OMURGASI (03_PLAN_ONCESI B5)

- **İSTEK:** Düşmekte olan koloni-tarım istasyonunu (12.418 yaşam) güvenli yörüngeye çıkarmak.
- **ENGEL:** Çekicinin itki gücü yetersizdir, motorlar aşırı yüklenmeden çatlamaktadır ve otomatik koruma sistemi manevrayı engellemektedir.
- **BEDEL (+ SAHNE NO):** S11'de çekici gemisini düşüş rotasında kilitleyip halat bağlarını kesmek; kendi gemisiyle atmosfere düşmeyi kabul etmek.
- **MUHATAP:** Gemi Otomatik Güvenlik Sistemi (`CREW SURVIVAL LIMIT`). Pilot, kendisini korumak isteyen makineye karşı manuel override kapağını kırarak kararını dayatır.

---

## 6. 📦 REFERANS PAKETİ KARARI
- **Karar:** `YAZILSIN` (`THE_TETHERED_MASS_REFERANS_PAKETI.md`)
- **Tetikleyiciler:** T1 (Astronot kaskı/basınç giysisi) + T3 (Momentum halat tamburu ve kenetlenme modülü). KAPI 0 uygulanacaktır.
