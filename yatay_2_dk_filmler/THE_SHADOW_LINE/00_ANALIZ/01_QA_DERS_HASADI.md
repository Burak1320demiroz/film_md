# 🧾 THE_SHADOW_LINE — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D200 | iki yerçekimi / süzülen toz tuzağı | uzay vakumunda parçacık ve hover tozu süzülmez; duman/buhar anında dağılır | S00, S01, S04, S08 |
| D202 | seçim ve bedel bedende ödenmiyor | S10'da mühendis elini bilinçli olarak plazma ışığına sokar; S12'de parmaklar yumruk şeklinde kilitlenir | S09, S10, S11, S12 |
| D206 | bedel beden diliyle okunmuyor | kask vizörü kapalıyken acı ve efor omuzların çökmesi ve titreyen el parmaklarıyla gösterilir | S01, S05, S10, S11 |
| D208 | kimlik dizisi ve giysi sapması | astronot uzay giysisi beyaz sert kabuk, koyu gri esnek eklemler ve altın vizör kask olarak sabit kalır | S00-S12 |
| D209 | dünya çapası ve uzamsal kayma | hareket daima Soldan Sağa (Ekran Solu: Güneş / Ekran Sağı: Soğutma Valfi) yönünde kalır | S00-S12 |
| D211 | ilk 10s / son 10s retention riski | S00 hook eldiven dumanı ile başlar; S12 parmak kilitlenmesi ve gerileyen gölge hattı ile biter | S00, S12 |
| D212 | aynı vuruş ardışık sahnelerde tekrarlandı | S02 nesne erimesi kaldırıldı, doğrudan S02'de istasyon dış yüzeyinde zamana karşı koşu başlar | S02, S03 |
| D213 | aksiyon elipsi ve temas görünürlüğü | S10 mandal kaldırma aksiyonunda elin mandala teması ve açılma hareketi kadraj içinde net gösterilir | S10 |
| D214 | kadrajda olmayan beden tarif edildi | yakın çekimlerde kadraj dışında kalan giysi parçaları (kask, bot) prompta yazılmaz | S00, S06, S10, S12 |
| D215 | ekran metni ve araç ayarları | HUD yazıları ve filigran prompt metnine konmaz; video parametresi olarak işlenir | S00-S12 |
| D216 | ses miksi eksikliği | 5 katmanlı ses miksi: plazma uğultusu, kask içi nefes, telsiz cızırtısı, mekanik tıkırtı ve dip stinger | S00-S12 |
| D146 | biçim kilidi metinle tutulmuyor | astronot donanımı ve mandal mekanizması referans paketi visual seed ile kilitlenir | S00-S12 |
| D174 | ekran yönü ihlali | kask vizörünün yönü ve astronotun ilerleme vektörü sağ taraftaki soğutma valfine sabitlenir | S01-S11 |
| D192 | 1 numaralı risk sayıyla yazılmadı | 1 numaralı risk: Güneş plazma ışığının gölge hattı açısı; her promptta sayıyla yazılır (çapraz bıçak çizgisi) | S00-S12 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D182 | filmde replik/diyalog olmadığı için diyalog senkronizasyon dersi muaf tutuldu |
| D194 | iki kişi arası ayrılık ve muhatap dersi tek karakterli bu filmde muaf tutuldu |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_SOLAR_MIRROR` | ⑤ Arka Plan | uzay arkaplanındaki yıldızlar sert ışıkta kaybolmadı | Güneş plazması doğrudan kadrajda iken uzay siyahı tamamen yıldızsız zifiri yapılır |
| `THE_CRACKED_HELMET` | ② Devamlılık | kask vizöründeki çatık/yansıma kareler arası sıçradı | vizör yansıması ve rengi visual seed ile çapalayarak sabit tutulur |
| `THE_HARD_DOCK` | ⑦ Aksiyon | valf kolu çevirme eylemi kadraj dışında kaldı | S10 ve S11'de valf ve güvenlik mandalı temasları tam orta yakın kadrajda gerçekleşir |
| `THE_LAST_SHIFT` | ⑧ Efor | efor sonrası astronotun duruşu sıfırlandı | S11 sonrası S12'de mühendis soluk soluğa kaportaya yaslanır, efor devamlılığı sağlanır |
| `THE_SILENT_PERIHELION` | ③ Ses | vakum ortamında patlama sesi yapıldı | dış uzay sahnelerinde patlama sesi yerine giysi içi iletilen boğuk titreşim ve nefes kullanılır |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK (Politika) | kask kırılması veya kafa travması kelimeleri | nötr form tarifi: "gold reflective visor with thermal surface tension marks" | S08, S12 |
| YR (Yapısal Red) | alev ve yangın efekti uzayda hover etti | "orange solar radiation haze, blinding thermal glare on metallic hull" | S00, S01, S05 |
| MÇ (Mekanik Çelişki) | havalandırma / soğutma valfinin mantıksız hareketi | mekanik emniyet mandalı (toggle latch) mekanizması açıkça tarif edilir | S09, S10, S11 |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        14 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   1 numaralı riskin sayıyla yazılmaması (D192) · Biçim kilidi sapması (D146) · Aksiyon temasının kadraj dışı kalması (D213)
```
