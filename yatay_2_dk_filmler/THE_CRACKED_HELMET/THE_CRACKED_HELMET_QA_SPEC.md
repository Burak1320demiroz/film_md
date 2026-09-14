# 📑 THE_CRACKED_HELMET — QA SPECIFICATION

---

## A. HİKÂYE VE B5 DOĞRULAMASI

- **İSTEK:** Kask vizörü sızıntısını durdurmak ve oksijeni sabitlemek.
- **ENGEL:** Kask basınç düşüşü (04:12 -> 00:30 bar) ve vakum soğuğu.
- **BEDEL:** Sahne 08'de titreyen parmaklarla kızgın reçine çubuğunu çatlağa sürmek.
- **MUHATAP:** Çakılan kaçış modülü enkazı ve obsidyen mineral kayalığı.
- **İNSAN SAYISI:** 1 (Tek astronot).

---

## B. KURGU GEOMETRİSİ VE İNSAN ŞERİDİ

- **KLİP SAYISI:** 12 Video Klip
- **KLİP SÜRESİ:** 10.0 saniye
- **TOPLAM KURGU SÜRESİ:** 120.0 saniye (02:00)
- **TARGET ASL BAND:** 6.0s - 10.0s
- **ASL CURVE:** Dengeli ritmik dağılım
- **İNSAN ŞERİDİ:** S00-S11 boyunca tek astronot silueti ve koyu gri basınç giysisi kilitlidir.
- **FİNAL VURUŞ KANITI:** Sahne 11'de tamir edilen vizörün üzerinde parlayan amber şerit ve yansıyan ikiz yıldız ışığı (t=115-120s, 1 adet tamir şeridi).

---

## C. MERCEK KİLİTLERİ VE FLAGS

- **KADRAJ FLAGS:** 35mm anamorfik lens ölçeği, kadraj payı ≥%25, abartı zoom yasağı.
- **IŞIK FLAGS:** Tek yönlü soğuk güneş ve zemin mor obsidyen yansıması, monotonik azalım çelişkisi yok.
- **FİZİK FLAGS:** Vakumda toz kalkmama kuralı, püsküren gaz buharının konik hatta yayılması.

---

## E. MAKİNE KAPILARI (FFMPEG DOĞRULAMALARI)

1. **SÜRE VE KADRAJ KAPISI:**
   `KOMUT:` `ffprobe -v error -show_entries format=duration -of csv=p=0 <input.mp4>`
   `DOĞRULANDI:` ffmpeg 6.0 · 09.09.2026
   `İKAME:` ffprobe manuel süre doğrulaması.

2. **ASL BAND KAPISI:**
   `KOMUT:` `ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=noprint_wrappers=1 <input.mp4>`
   `DOĞRULANDI:` ffmpeg 6.0 · 09.09.2026
   `İKAME:` Manuel kare sayımı.
