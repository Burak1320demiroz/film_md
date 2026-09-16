# 🧾 MARS_SON_CIKIS — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20)

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D1 | AI kesme hataları | Kesmeler 2 plan veya tek sürekli plan olarak kurulacak | S01-S36 |
| D16 | Kask arkasında yüz morph | Vizör yarı şeffaf, kask içinde yüz hatları sabit tutulacak | S01-S03, S09-S36 |
| D34 | Model başlık kartı ekliyor | Prompta başlık/metin kartı eklenmeyecek | S01-S36 |
| D42 | Yıpranma her karede yenileniyor | S01 Mars tozu ve S14 yangın isi S15-S36 boyunca korunacak | S01-S36 |
| D45 | Prompt iskeleti sızıyor | `[LESSON n]` ve prompt etiketleri gövdeden temizlenecek | S01-S36 |
| D62 | Kurguda final düşüyor | S36 rahatlama ve Mars manzarası kurguda kesilmeyecek | S36 |
| D139 | Düz sırt kilidi bozuluyor | Giysi sırtı "smooth continuous panel from collar to hip" verilecek | S01-S36 |
| D146 | Visor biçimi bozuluyor | Vizör eğriliği ve şerit oranları sayıyla kilitlenecek | S01-S36 |
| D157 | Novum tek karede okunmuyor | Kenetlenme halkası ve port yuvası görünür nesne olacak | S22-S32 |
| D167 | Ünlü benzerliği çıkıyor | Lena 4, Aras 4 temel görsel especialmente sınırlanacak | S01-S36 |
| D169 | Zorlanma tek sahnede kalıyor | Aras'ın sol kol sakatlığı S15-S36 boyunca sürdürülecek | S14-S36 |
| D174 | Screen-right/left şaşırtıyor | Yön Kestrel burnu, Horizon portu ve Mars yüzeyiyle verilecek | S01-S36 |
| D175 | Basınç giysisi deliniyor | S14 hasarı dış zırh ve doku zorlanmasıdır, elbise delinmez | S14-S36 |
| D180 | Mutsuz sessizlik çıkıyor | Uzay mekanik sesleri ve kask içi solunumla ses canlı tutulacak | S01-S36 |
| D192 | Risk sıfatla korunuyor | Manuel kenetlenme yaklaşma hızı 7.5m -> 1.5m -> 0.15 m/s (0m temas) verilecek | S26-S32 |
| D198 | Sıfır-G momentum kayboluyor | Kestrel/Horizon bağıl ivmelenmesi mekanik sönümlemeyle duracak | S29-S32 |
| D200 | İki yerçekimi karışıyor | Yüzeyde 0.38g, yörüngede mikro-g kinematiği tutarlı kalacak | S01-S36 |
| D206 | Bedel bedende ödenmiyor | S14 sakatlığı S15-S36 boyunca askıda kalacak (Kapatılamaz Bedel) | S14-S36 |
| D209 | Dünya çapası kayboluyor | Mars kızıl ufku ve Horizon omurgası sabit çapa olacak | S01-S36 |
| D210 | Kafiye çifti unutuluyor | S01 kasa pimi <-> S31 kenetlenme leveri kafiye oluşturacak | S01, S31 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar

| ders | neden bu filmde uygulanmadı |
|---|---|
| D201 | Vakum güneş açısı tek yönde sabit tutulduğu için ek önlem gerektirmedi |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_LAST_SHIFT | ⑮ YÖN VE HEDEF | Uzay yanaşmasında aracın dönme ekseni sapıyordu | Kestrel burun vektörü ve Horizon port ekseni visual anchor ile kilitlenecek |
| THE_HOLLOW_COUNT | ⑭ HAREKET MANTIĞI | Hasarlı kol kesme sonrasında aniden açılıyordu | Aras'ın sol kolu S14 sonrasında askı kayışına sabitlenecek |
| THE_LOCKED_PULSE | ⑨ KADRAJ SADAKATİ | Dar iç mekânda kamera duvar dışına çıkıyordu | Habitat ve kokpit sahnelerinde 28mm/35mm iç mekân lens sınırı konacak |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK (Politika Kapısı) | Patlama/ateş görseli red riski taşıyabilir | "Yangın" yerine "servis kabininde elektrik arkı ve yoğun siyah duman" nötr tarifi | S10, S11 |
| YR (Yüz Reddi) | Kask içi kapalı anonim yüz görünümü | Yarı saydam vizör ve iç kask aydınlatması ile yüz net görünür kılınacak | S01-S03, S09-S36 |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet
QA ARIZASI:         3 adet
RED SINIFI:         2 adet
⛔ EN PAHALI ÜÇÜ:   D192 (Mesafe/Hız Sayısal Kilidi) · D206 (Bedelin Bedende Ödenmesi) · D139 (Düz Sırt Kilidi)
```
