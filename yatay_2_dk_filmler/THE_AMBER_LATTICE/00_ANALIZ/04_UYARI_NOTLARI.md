# ⚠️ THE_AMBER_LATTICE — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arıza kaydına bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır:
> **hangi sahne · hangi ölçülmüş kayıt · ne yapılacak.** Üçünden biri
> yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S08 | Red Def MÇ (Akışkan Sıvı Reddi) | Amber sarısı enerjinin sıvı gibi aktarılması motor çökmesi ve red üretebilir | Sıvı/plazma ifadesi kaldırıldı; `solid amber crystal light veins` olarak donduruldu | ✅ |
| 2 | S08 | Red Def YR (Overexposed Glare) | Siyah arka planda parlak sarı patlaması detay kaybına yol açar | Negatif prompta `overexposed yellow glare, blinding bloom, blown out highlights` yazıldı | ✅ |
| 3 | S00 | Ders 32 (Ölçek Şahidi Yokluğu) | 120m Obeliskin boyutu ekranda anlaşılamaz ve derinlik kaybolur | EVA-4 astronotu (1H = 1.8m) kadrajın ön koridoruna ölçek şahidi olarak eklendi | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S05 | `THE_CRACKED_HELMET` (T10 Kask Yansıması) | Vizör yansımasının sahneden sahneye değişmesi | `dark gold reflective visor showing glowing amber monolith` kalıbı sabitlendi | ✅ |
| 2 | S04 | `THE_BENT_GRASS` (T2 Devamlılık / Ton Sapması) | Sarı renkte kehribardan limona kayma | Palette `3200K warm amber yellow energy` ve `charcoal biometal` donduruldu | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| `POLITIKA_VE_URETILEBILIRLIK` | Renk ve doku karmaşası | Dar palet kilidi: Mat Siyah Metal (#050505) + Kehribar Sarısı Emisyon (#FFBF00 / 3200K) + Mat Beyaz Astronot Giysisi (#EEEEEE). |
| `SAHNE_ZINCIRI` | Klip içi aksiyon bozulması | Durum değişimleri klip içine yazılmaz; S00-S09 sınır çizgilerine (End/Start) aktarılır. |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 · SKYLIGHT | Uygulanıyor | Astronot EVA-4 ve Obelisk BIBLE metinleri her promptta self-contained donduruldu |
| 2 | Yasak kelime kumaş sanılıp dalgalandırılıyor | D59 · OPEN CIRCUIT | Engellendi | Fabric/cloth kelimeleri tamamen yasaklandı, sert biyo-metal yüzey tanımlandı |
| 3 | Optik aritmetiği yapılmamış | OPEN CIRCUIT denetimi | Uygulanıyor | 24mm lens 60m mesafeden 120m Obeliski tam kadraja alacak şekilde hesaplandı |
| 4 | Uzak nesne ~60 piksel | D179 | Uygulanıyor | S00 kadrajında astronot en az 180 piksel (kadraj yüksekliğinin 1/6'sı) boyutlandırıldı |
| 5 | Ayrım RENKLE kuruldu | BLIND BERTH | Engellendi | Astronot mat beyaz, obelisk mat siyah, enerji hatları kehribar sarısı olarak yüksek kontrasttaayrıldı |
| 6 | Ortam kartının NEGATİF bloğu | UZAY_USSU §6 | Uygulanıyor | Negatif prompta `toy model, tilt-shift lens, miniature replica, blurred studio background` eklendi |
| 7 | Tema yazıldı ama sahne indeksi yok | KALEIDA CRASH | Uygulanıyor | Tema S00 (Sönük), S04 (Kılcal), S08 (Doruk), S09 (Kapanış) sahneleriyle indekslendi |
| 8 | Bedel var ama sahne numarası yok | 03_PLAN_ONCESI B5 | Uygulanıyor | Bedel S08 sahnesinde (aşırı yüklenen tarayıcı ve elin koruma amaçlı geriye çekilmesi) |
| 9 | Yasak cümlesi yazıldı | D123 | Engellendi | "Never/no" yasağı pozitif `solid crystal amber light` tarifi ile aşılmıştır |
| 10 | Politika: nesne ADLANDIRILDI | D67 · red defteri | Engellendi | Form tarif edildi: `octagonal monolithic black biosteel structure with vertical amber channels` |
| 11 | Replik zamanı ELLE yazıldı | D122 | Muaf | Replik bulunmuyor, film tamamen diyalogsuzdur |
| 12 | Klip içi durum değişimi | SAHNE_ZINCIRI §1 | Uygulanıyor | Durum değişimleri sahne geçiş hatlarına (End/Start) yazılmıştır |
| 13 | Prompt "BIBLE'a bak" diyor | kural ③ | Engellendi | Tüm promptlar self-contained hazırlanmıştır |
| 14 | Makine kapısı ffmpeg filtresi | D142 | Uygulanıyor | Ffmpeg komutları varsayılan `crop`, `drawtext` filtreleriyle doğrulandı |
| 15 | Çıplak deri negatifi | D175 | Uygulanıyor | Negatif prompta `bare skin, exposed flesh, human face` eklendi |
| 16 | 1 NUMARALI risk sayıyla yazıldı | D192 · `03_PLAN_ONCESI` A5 | Uygulanıyor | S08 amber ışık hatları genişliği max 0.3 metre, 3200K emisyon parlaklığında tanımlandı |

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
✅ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
✅ tekrar eden arıza tablosunun HER satırı cevaplandı (16 satırın tamamı dolu)
→ hepsi ✅, 05_SAHNE_CALISMALARI/ açılabilir.
```
