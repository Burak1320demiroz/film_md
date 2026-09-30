# ⚠️ THE_STILL_POINT — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md` (bu filmde ne var).
> **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S00, S23 | D34 · D70 | Modelin açılış/kapanış jenerik kartı eklemesi | Negatif blokta başlık ve metin yasağı, 240s net süre | ✅ |
| 2 | S09, S11 | D157 · D78 | Arabanın ters gidişinin anlaşılamaması | Merkez aks ve arka plan istasyon kafesi zıt hareketiyle kanıtlanacak | ✅ |
| 3 | S12 | D202 · D206 | Bedelin soyut kalması | Arabanın ray kilidinin sökülüp iki elle boşluğa fırlatılması | ✅ |
| 4 | S17 | D141 · D200 | Durgun Nokta kontrastının kaybolması | Dönen halka kafesi (0.065g) ve sabit merkez modül (0g) aynı anda kadrajda | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S02, S08, S15 | D139 | Arkadan çekimde sırt ünitesinin kontrolsüz büyümesi | Sırt ünitesi kompakt, düz koyu gri kompozit panel olarak pozitif yazılacak | ✅ |
| 2 | S04, S05 | D174 | "Screen-right" referansının modele ters gelmesi | Hareket yönü istasyonun dönme teğeti ve merkez modülüyle adlandırılacak | ✅ |
| 3 | S15-S19 | D198 | Serbest süzülmenin havada asılı kalma sanılması | Sabit hızlı (2 m/s) doğrusal balistik ötelenme yazılacak | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D146 | Vizörün kask kubbesine dönüşmesi | Vizör kaska gömülü opak parlak siyah dışbükey vizör olarak kilitlenecek |
| D193 · D201 | Vakum ışığı ve sert gölgelerin yön değiştirmesi | Sabit Güneş konumu ve derin siyah gölgeler korunacak |
| D214 | IN FRAME dışı uzuvların promptta yer alması | Her prompt ilk satırdaki IN FRAME listesiyle sınırlı tutulacak |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 | Aktif | Referans paketi tanımlandı |
| 2 | Yasak kelime kumaş sanılıp dalgalandırılıyor | D59 · D153 | Aktif | Sert kompozit kabuk tarifi yapıldı |
| 3 | Optik aritmetiği yapılmamış | OPEN CIRCUIT | Aktif | Lens, mesafe ve kadraj eni tablosu kuruldu |
| 4 | Uzak nesne ~60 piksel | D179 | Aktif | Ana nesneler kadrajda ≥100 px planlandı |
| 5 | Ayrım renkle kuruldu | BLIND BERTH | Aktif | Mat beyaz göğüs ve turuncu kol şeridi zıtlığı |
| 6 | Ortam kartının negatif bloğu eksik | UZAY_USSU §6 | Aktif | KILAVUZ_REHBERI §5.3 tam negatif bloğu eklendi |
| 7 | Tema sahne indeksi yok | KALEIDA CRASH | Aktif | Tema S07, S12, S17 sahnelerine bağlandı |
| 8 | Bedel sahne numarası yok | 03_PLAN_ONCESI | Aktif | S12 açıkça bedel sahnesi ilan edildi |
| 9 | Yasak cümlesi modeli tetikledi | D123 | Aktif | Yasak cümleleri pozitif tasarım emirlerine çevrildi |
| 10 | Politika nesne adlandırıldı | D67 | Aktif | Biçim ve fiziksel fonksiyon dili kullanıldı |
| 11 | Replik zamanı elle yazıldı | D122 | Yok | Film diyalogsuzdur |
| 12 | Klip içi durum değişimi | SAHNE_ZINCIRI | Aktif | Durum değişimleri kesme anlarına bağlandı |
| 13 | Prompt self-contained değil | kural ③ | Aktif | Her prompt tüm kilitleri bağımsız taşır |
| 14 | Makine kapısı kurulu değil | D142 | Aktif | Mevcut depo betikleriyle tam uyum sağlandı |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | Aktif | Basınçlı eldiven ve boğum contası kilitlendi |
| 16 | 1 numaralı riskte sayı yok | D192 | Aktif | 8,0 m/s ve 0,08 rad/s sayısal kilitleri konuldu |

---

## 📌 UYARI ÖZETİ

```
⛔ KAPATILAN BLOKAJ:  4 adet
⚠️ İZLEME NOTU:       3 adet
🧯 FİLM GENELİ:       3 adet
TEKRAR EDEN ARIZA:   16 / 16 cevaplandı
```
