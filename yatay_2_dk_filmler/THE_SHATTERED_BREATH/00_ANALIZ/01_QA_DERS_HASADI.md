# 🧾 THE_SHATTERED_BREATH — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| DERS 39 | Kriyojenik zemin sıvı su gibi gösterilip ortam kartı ihlal edildi | 88 K zemin siyah metan-etan karışımı sert kabuktur; erime ısı şeridi boyunca turuncu parıltı ve mikro-çatlakla sınırlıdır, sıvı su veya nehir oluşamaz | S00, S02, S04, S07, S11 |
| DERS 41 | Gece sahnesinde astronot ve zemin koyu renkte birleşip siluet kayboldu | Koyu gri mat titanyum zırh, zemin jeotermal damarlarından çıkan 590 nm turuncu kehribar alt ışıkla kilitlenir | S01-S11 |
| DERS 143 | Kriyojenik buğulanma fırtına veya duman gibi yükselip görüşü kapattı | Kriyojenik gaz çıkışı zeminden 10-15 cm yukarıda süzülen mikro-buhar katmanıdır; vizör görüş alanını kapatamaz | S03, S05, S08 |
| DERS 146 | Kask ve zırh tasarımı metinle tutulamadı, sahneler arası biçim değişti | Referans paketi (KAPI 0) ve Seed 9001 kask mimarisini, altın vizör açısını ve titanyum göğüs plakasını sabitler | S00-S11 |
| DERS 175 | Vizör içindeki astronot yüzü karanlıkta kalıp duygu okunamadı | Kask içi mavi-beyaz HUD gösterge ışığı astronotun gözlerini ve nefes buğusunu vizör arkasından görünür kılar | S01, S06, S08, S10 |
| DERS 198 | Statik nesneler havada asılı kaldı veya zeminde tutarsız eridi | Eriyen zemin mikro-adacıklar oluşturur; astronotun 85 kg'lık kütlesi milimetre/saniye hızla batan kompozit kabukta çökme oluşturur | S05, S07, S09, S11 |
| DERS 202 | Seçim ve bedel bedende okunmadı, soyut kaldı | S08'de astronot sol elini göğüs termo-valfine götürüp dış yalıtımı bilinçli olarak kırarken gövde titremesi ve nefes hızlanması belirgindir | S07, S08, S09 |
| DERS 203 | Gösterge veya araç prompta nesne formu verilmeden yazıldı | Göğüs termo-valfi 5 cm çapında döner mat pirinç vana formuyla prompta girer; "gösterge" gibi soyut kelime kullanılmaz | S03, S08 |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_SOLAR_MIRROR | T9 Kadraj | Yakın çekimde astronot elleri kadraj dışına taştı, efor okunamadı | S08 yakın çekiminde 35mm lens kullanılarak astronotun sol eli ve göğüs valfi kadraj merkezine tam yerleştirilir |
| THE_COLD_WELD | T2 Devamlılık | Vizör içi buğulanma karesel sıçradı | Vizör iç yüzeyindeki damlacık ve buğu yoğunluğu S00-S11 boyunca dereceli (%10'dan %70'e) artırılır |
| THE_DRY_ANCHOR | T4 Hikaye | Bedel aksiyonu geç sahnede zayıf kaldı, final tatmin etmedi | S08 bedeli (dış yalıtım sökümü) dramatik zirve olarak S07 ikileminin hemen ardından uygulanır |
| THE_BENT_GRASS | T6 Fizik | Zemin erimesinde zemin yüzeyi aniden kaybolup görsel gürültü üretti | Zemin erimesi kılcal kırılma şeritleri (2-5 cm genişliğinde) ve renk değişimiyle aşamalı gösterilir |
| THE_FROST_LINE | T1 Kare | Arka plan ufuk çizgisi klip değişiminde kaydı | 88 K uydunun arka planındaki gaz devi gezegen silueti ufuk çizgisinde 15 derece sabit açıda kilitlenir |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK (Politika/Kumaş) | `fabric`, `cloth`, `mantle` kelimeleri model tarafından bayrak gibi dalgalandırıldı | Giysi zırhı için `fabric` veya `cloth` kullanılmaz; `rigid composite armor plate`, `titanium thermal shell` yazılır | S00-S11 astronot zırh promptları |
| YR (Yasaklı Red) | "never drawn", "no melt" gibi negatif cümleler yazıldı, model negatif kelimeleri pozitif algılayıp erime üretti | Cümle negatif kurulmaz; pozitif biçim verilir: "solid dark composite methane-ethane ice crust, 88 Kelvin" | S00, S01, S02 zemin promptları |
| MÇ (Mekanik Çelişki) | Cihaz veya vana adı verildi ama geometrisi tarif edilmedi | Göğüs termo-valfi "brass-alloy rotary valve disc, 5cm diameter, 3 notch marks" olarak tam tarif edilir | S03, S08 promptları |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        8 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   DERS 146 (Biçim Kilidi) · DERS 198 (Erime Fiziği) · PK (Kumaş Dalgalanma Yasağı)
```
