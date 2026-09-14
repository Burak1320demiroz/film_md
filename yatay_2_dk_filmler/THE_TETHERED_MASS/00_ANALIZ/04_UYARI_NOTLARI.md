# ⚠️ THE_TETHERED_MASS — UYARI NOTLARI VE RİSK KONTROLÜ

> **Girdi:** `01_QA_DERS_HASADI.md` × `03_SAHNE_SIRALAMASI.md`.
> **Çıktı:** Ölçülmüş arızalara bağlı sahne bazlı teknik uyarı notları.

---

## 1. 🔴 KRİTİK KONTROL LİSTESİ

- 🔴 **KONTROL 1 (Vizör Opaklığı - D197):** S02, S04, S07, S09, S11, S12 sahnelerinde astronot kask vizörü kesinlikle matlaşmayacak. `clear transparent visor, visible human eyes inside helmet` ifadesi promptlarda sabitlenecektir.
- 🔴 **KONTROL 2 (Motor Patlama Alevi - MÇ Reddi):** S07 ve S08 sahnelerinde motor iflası anlatılırken kesinlikle ateş/alev çizilmeyecektir. `red glowing thermal stress on engine bell, pressurized white coolant vapor venting in vacuum` kullanılacaktır.
- 🔴 **KONTROL 3 (Sıfır-G Vakum Fizik Reddi - D198/YR Reddi):** S00, S01, S13, S15 sahnelerinde halat lifleri koparken vakumda kıvılcım veya rüzgar efekti olmayacaktır. `rigid steel cable strand curling slowly, micro-vibrations, no sparks, no wind` kullanılacaktır.
- 🔴 **KONTROL 4 (Bedende Okunan Karar - D202):** S11 sahnesinde astronotun kararı ekran okumakla sınırlı kalmayacak; `shaking gloved hand smashing safety acrylic glass cover, physically pulling red manual override lever` aksiyonu yazılacaktır.

---

## 2. 📋 TEKRAR EDEN ARIZALAR YANIT TABLOSU

| Arıza Satırı | Bu Filmde Durum | Alınan Önlem / Gerekçe |
|---|---|---|
| 1. Kask vizörü opaklaşması | Var | D197 pozitif kilit cümlesi tüm kokpit promptlarına eklendi. |
| 2. Motor alevi red riski | Var | MÇ sınıfı red kuralı uygulandı; gaz buharı ve kızarma kullanılacak. |
| 3. Vakumda kıvılcım çizilmesi | Var | D198 sıfır-g fizik kuralı eklendi; mikro tel beyazlaşması kullanılacak. |
| 4. Görünmez seçim hatası | Var | D202 beden aksiyonu kuralı eklendi; cam kırma ve pim çekme. |
| 5. Göğüs paketi tutarsızlığı | Var | Referans pakedi (KAPI 0) yazılıyor ve seed kilitleniyor. |
| 6. İstasyon ölçek kaybı | Var | Uzay üssü kılavuzu uyarınca 1H (1.8m astronot) ölçek şahidi eklendi. |
| 7. Vakumda dış ses | Var | Ses haritasında dış mekan sahneleri tam sessizlik + 28Hz sub-bass yapıldı. |
| 8. Güneş ışığı açısının değişmesi | Var | Sol üst 45 derece sabit orbital ışık kaynağı kilitlendi. |
