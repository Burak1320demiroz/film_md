# 📊 THE_HARD_DOCK — QA PERFORMANS VE DEĞERLENDİRME RAPORU

> **Format:** Yatay 16:9 · 3-5 dk (24 sahne × 10s = 240s = 04:00)  
> **Klasör:** `yatay_4_dk_filmler/THE_HARD_DOCK/`  
> **Tarih:** 12.09.2026  

---

## 📑 1. KOŞU BİLGİLERİ VE KAPILAR

```
KOŞULAN MERCEKLER:  ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK
MOD:                 Mod D (SPEC var) + Mod V
ÖLÇÜM HAKEMLİĞİ:     Kesme = 24 · Sahne = 24 · Süre = 240s (04:00)
PARTİ DURUMU:        Parti ayakta (0 GEÇERSİZ · 3 GO · 9 ŞARTLI)
```

---

## 📊 2. MERCEK SKORLARI SUITES

| Mercek | Mod | İddia / Ham | Düzeltilmiş Skor | Durum | Ana Bulgular |
|---|---|---|---|---|---|
| **① KARE** | Mod D | 7.4 | **7.4** | ✅ GO | 1:10 Kamera yönelim sıçraması (Blocker) · 0:07 İstasyon dönme ivmesi · 1:35 Eldiven wrist mesh bozulması |
| **② DEVAMLILIK** | Mod V | 9.08 (12 kat) | **9.1** | ⚠️ ŞARTLI | 01:30 vs 02:30 Kol şeridi kayması · 01:35 vs 03:03 Kumanda kolu tasarımı değişimi |
| **③ SES** | Mod V | 8.89 | **8.5** | ⚠️ ŞARTLI | Yapay AI telsiz direktifleri tutarlı · 00:10 vs 00:40 Kabin hum ses seviyesi değişimi |
| **④ HİKAYE** | Mod D | 8.1 | **8.1** | ✅ GO | Tek astronot prosedürel gerilimi · S14 & S15 gereksiz geniş açı orbital tekrar ritmi |
| **⑤ ARKA PLAN** | Mod V | 6.3 | **6.3** | Ⓥ (GO) | 00:05 vs 02:05 Lav gezegeni topoğrafya kayması & yanardağ belirmesi · 00:15 vs 01:55 civata sayısı kayması |
| **⑥ FİZİK** | Mod D | 8.42 | **8.4** | ⚠️ ŞARTLI | 02:00 Güneş paneli kopmasında tepki kuvveti eksikliği · 00:00 vs 00:40 Dönüş hızı yavaşlaması |
| **⑦ AKSİYON** | Mod D | 8.78 | **8.8** | ⚠️ ŞARTLI | 03:30–03:37 B4 kenetlenme darbesi ve kilitlenmesi kesmeyle gizlenmiş (Action Ellipsis) |
| **⑧ EFOR** | Mod D | 6.57 | **6.6** | ⚠️ ŞARTLI | 01:48 & 03:12 Yoğun nefes alışverişinde vizörde buğulanma eksikliği · 03:30 el titremesi eksikliği |
| **⑨ KADRAJ** | Mod D | 8.86 | **8.7** | ⚠️ ŞARTLI | 03:50 S24 final kurulum uyumsuzluğu (B vs A) açılış-kapanış kafiyesini kırıyor |
| **⑩ OYUNCULUK** | Mod D | 7.45 | **7.4** | ⚠️ ŞARTLI | 02:00–02:39 S13-S16 dış uzay çekim dizisi karakter duygusal tırmanış ritmini bölüyor |
| **⑪ IŞIK** | Mod D | 5.51 | **5.5** | ⚠️ ŞARTLI | 01:20 S8->S9 renk sıcaklığı sıçraması (sıcak turuncudan nötr beyaza) · 00:50 ışık açısı kayması |
| **⑫ HOOK** | Mod D | 7.26 | **7.2** | ⚠️ ŞARTLI | 00:10–00:40 & 01:10–01:50 cockpit-dış mekan tekrar döngüsü plateau yaratıyor · 04:00 kart loop'u kesiyor |

---

## 📝 3. ①.5 BETİK KOŞU ÇIKTISI (`rapor_kontrol.py`)

```
SPEC: yatay_4_dk_filmler/THE_HARD_DOCK/THE_HARD_DOCK_QA_SPEC.md  → ①/④/⑥/⑦/⑧ + ⑨-⑫ için MOD D ZORUNLU
PLAN: 24 sahne (THE_HARD_DOCK_BOLUM_1.md + THE_HARD_DOCK_BOLUM_2.md) → ①.9 teslim kapısı koşacak [D188]

✅ GO      ·  ① KARE        · TABLOYA GİRECEK SAYI: 7.4
⚠️ ŞARTLI  ·  ② DEVAMLILIK  · TABLOYA GİRECEK SAYI: 9.1 ⚠️ ŞARTLI
⚠️ ŞARTLI  ·  ③ SES         · TABLOYA GİRECEK SAYI: 8.5 ⚠️ ŞARTLI
✅ GO      ·  ④ HİKAYE      · TABLOYA GİRECEK SAYI: 8.1
✅ GO      ·  ⑤ ARKA PLAN  · TABLOYA GİRECEK SAYI: 6.3 Ⓥ
⚠️ ŞARTLI  ·  ⑥ FİZİK       · TABLOYA GİRECEK SAYI: 8.4 ⚠️ ŞARTLI
⚠️ ŞARTLI  ·  ⑦ AKSİYON     · TABLOYA GİRECEK SAYI: 8.8 ⚠️ ŞARTLI
⚠️ ŞARTLI  ·  ⑧ EFOR        · TABLOYA GİRECEK SAYI: 6.6 ⚠️ ŞARTLI
⚠️ ŞARTLI  ·  ⑨ KADRAJ      · TABLOYA GİRECEK SAYI: 8.7 ⚠️ ŞARTLI
⚠️ ŞARTLI  ·  ⑩ OYUNCULUK   · TABLOYA GİRECEK SAYI: 7.4 ⚠️ ŞARTLI
⚠️ ŞARTLI  ·  ⑪ IŞIK        · TABLOYA GİRECEK SAYI: 5.5 ⚠️ ŞARTLI
⚠️ ŞARTLI  ·  ⑫ HOOK        · TABLOYA GİRECEK SAYI: 7.2 ⚠️ ŞARTLI

  TOPLAM 12 rapor · 🚨 0 GEÇERSİZ · ⛔ 0 TEKRAR · ⚠️ 9 ŞARTLI · ✅ 3 GO
```

---

## 🛠️ 4. DÜZELTME VE REVİZYON SİPARİŞLERİ (FIX LIST)

1. **1:10 Kamera Yönelim Sıçraması (Blocker):** Dış istasyon dönme açısı 1:09 iç pencere perspektifine göre 1:10 kesmesinde ~45 derece aniden sıçrıyor.
2. **1:35 Eldiven Mesh Bozulması:** Hızlı kumanda kolu çekiminde eldiven bilek halkası uzayıp deforme oluyor.
3. **01:35 vs 03:03 Kumanda Kolu Değişimi:** Kumanda kolu tasarımı düz silindirik ile dokulu gaz kolu arasında değişiyor.
4. **00:05 vs 02:05 Gezegen Topoğrafyası:** Lav gezegeni yüzey çatlak ağı düzenli Voronoi deseninden merkezi volkan konisine dönüşüyor (S13 arka plan plakası değiştirilmeli veya kırpılmalı).
5. **00:15 vs 01:55 Pencere Cıvata Sayısı:** Cockpit pencere çerçevesindeki cıvata sayısı 8'den 10'a çıkıyor (vignette / kırpma veya paint-fix).
6. **00:55 Tek Katmanlı Parallaks:** Yaklaşan kapsül ile arka plandaki lav gezegeni yüzeyi aynı katmanda hareket ediyor (S6 çok katmanlı derinlik pası ile re-render edilmeli).
7. **02:00 Panel Kopma Tepkisi:** Güneş paneli koptuğunda geri tepme (recoil) momentumu istasyona yansımıyor (ilk 0.5 saniye kırpılmalı).
8. **03:30–03:37 Kenetlenme Temas Vuruşu (Aksiyon B4):** Kenetlenme halkasının mekanik darbesi ekrana gelmeden kokpit reaksiyonuna kesiliyor (1.5s mekanik kilitlenme insert çekimi eklenmeli).
9. **01:48 & 03:12 Vizör Yoğuşması (Efor):** Ağır nefes alma anlarında vizör iç yüzeyinde hafif buğu/yoğuşma efekti eklenmeli.
10. **03:50 S24 Kapanış Kurulum Uyumsuzluğu (Kadraj):** S24 kapanış sahnesi iç mekân B kurulumu yerine dış mekan A kurulumu ile tamamlanarak açılış-kapanış kafiyesi sağlanmalı.
11. **02:00–02:39 Dış Çekim Süresi (Oyunculuk S13-S16):** Karakterin duygusal tırmanışını korumak için S13-S16 arasına astronotun telemetri takibini gösteren 1'er saniyelik iç reaksiyon kareleri eklenmeli.
12. **01:20 Işık Sıcaklığı Sıçraması (Işık S8->S9):** S9 sahnesi S8'in sıcak turuncu iç mekân tonuna renk kurgusunda hizalanmalı.
13. **04:00 Son Başlık Kartı (Hook Exit):** Videonun başa dikişsiz dönmesi (infinite loop) için 04:00'teki durağan başlık kartı kurgudan çıkarılmalı.
