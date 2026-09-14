# ⚠️ THE_SHATTERED_BREATH — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S08 | DERS 202 · RED PK | Termo-valf sökümünde kumaş dalgalanması sanılması veya eforun soyut kalması | Göğüs pirinç termo-valfi disk formuyla yazılır, kumaş kelimesi kullanılmaz, sol el titremesi ve valf dönme hareketi net tarif edilir | ✅ |
| 2 | S00 | DERS 39 · RED YR | 88 K zemininin sıvı su veya nehir sanılıp erimesi | Pozitif form verilir: "solid dark composite methane-ethane ice crust, 88 Kelvin, razor-sharp hairline frost cracks" | ✅ |
| 3 | S04 | DERS 198 | Mikro-adacık erimesinde statik zemin sıçraması | Erime hızı sayıyla yazılır: "3mm per second widening thermal fissures forming a 1.8-meter diameter isolated ice disc" | ✅ |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S01 | THE_SOLAR_MIRROR T9 | Konnektör takarken el kadraj dışı kalabilir | 50mm lens alçak açı ile astronotun sol eli ve konnektör kadraj merkezinde kilitlenir | ✅ |
| 2 | S05 | THE_COLD_WELD T2 | Vizör buğulanmasında aniden aşırı buğu sıçraması | Vizör buğu oranı S00'de %10, S05'te %40, S08'de %70, S10'da %20 olarak dereceli yazılır | ✅ |
| 3 | S11 | ACILIS_KAPANIS §2 | S00 ile S11 kafiye açısının bozulması | S11 promptuna "— the same position, height and lens as Scene 0." kilit cümlesi birebir eklenir | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| DERS 146 | Kask ve zırh sahneler arası biçim değiştirebilir | Referans Paketi (KAPI 0) kask, vizör ve titanyum göğüs plakasını görsel ve metinsel olarak tüm sahnelerde sabitler |
| UZAY_GIYSISI §3 | Gece sahnesinde astronot silueti kaybolabilir | Koyu gri mat titanyum zırh, zemin jeotermal damarlarından çıkan 590 nm kehribar alt ışıkla her sahnede kontrastlandırılır |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör kare kare değişiyor) | D146 · SKYLIGHT | Kask/vizör T1 tetikleyicisi mevcut | Referans Paketi (KAPI 0) yazılır ve Seed 9001 kilitlenir |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT | Zırh yalıtım katmanı tarif edilirken risk var | `fabric` veya `cloth` kelimeleri kesinlikle kullanılmaz; `rigid titanium armor plate` ve `composite insulation layer` yazılır |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi | Yakın el ve termo-valf sahneleri mevcut | S01, S08'de 50mm ve 100mm lens kadraj sınırları optik olarak hizalanır |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | S00 ve S11 geniş çekimleri mevcut | 1.8m astronot silueti kadraj yüksekliğinin en az 1/3'ünü kapsayacak şekilde 35mm lensle hizalanır |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH | Koyu gri zırh + siyah buz zemini | 590 nm kehribar jeotermal damar ışığı ve kask içi mavi HUD ışığı çift renkli kontrast sağlar |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket okuması) | UZAY_USSU §6 | Kriyojenik ortam kartı (§3.9) kullanılıyor | Ortam kartının NEGATIVE bloğu ("no liquid water, no trees, no miniature scale") promptlara eklenir |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | BEDEL teması seçildi | BEDEL teması S08 sahnesine çakıldı (dış yalıtım sökümü) |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | Bedel tanımlandı | BEDEL sahne numarası S08 olarak kilitlendi |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | Olumsuz tarif riski | Negatif cümle yazılmaz; pozitif biçim ve boyut verilir ("solid ice crust, 88 Kelvin") |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | Termo-valf ve jeotermal hat | "Rotary brass valve disc, 5cm diameter, 3 notch marks" şeklinde formu tarif edilir |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | Repliksiz film | Replik yok, uyuşmazlık riski yok |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench · SAHNE_ZINCIRI | Erime ve buharlaşma klip içi aksiyonudur | Durum değişimleri klip içine değil sahneler arası sınır satırlarına (End/Start) yazılır |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | Prompt yazımı | Tüm promptlar self-contained yazılır, harici referans metni prompta konmaz |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı | D142 | QA_SPEC denetimi | Yalnız varsayılan ffmpeg parametreleri kullanılır |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | Astronot giysisi sökümü var | "No bare skin exposed, fully sealed pressurized suit interior" pozitif formda korunur |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | D192 · OPEN CIRCUIT | Zemin erime riski var | Erime hızı ve boyutu sayıyla yazıldı: "3mm per second widening thermal fissures, 1.8m diameter" |

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi
☑ tekrar eden arıza tablosunun 16 satırının HER BİRİ cevaplandı
→ üçü de ✅, 05_SAHNE_CALISMALARI/ açılabilir.
```
