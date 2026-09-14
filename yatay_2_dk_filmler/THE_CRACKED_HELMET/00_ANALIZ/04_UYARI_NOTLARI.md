# ⚠️ THE_CRACKED_HELMET — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` × `03_SAHNE_SIRALAMASI.md`.
> **Çıktı:** Sahne bazlı risk uyarıları ve kırmızı kilitlerin çözümleri.

---

## 1. 🔴 KRİTİK UYARILAR (ÜRETİM ÖNCESİ KAPANMASI ZORUNLU)

1. 🔴 **S00 & S01 — [DERS 179 · I2V t=0 Bedel Kilidi]:**
   - *Arıza:* I2V start frame'de vizör çatlağının sonradan belirip ilk karede pürüzsüz görünmesi.
   - *Çözüm:* S00 ve S01 için üretilecek görsel promptunda vizördeki kılcal çatlak ve buzlanma hattı `t=0` anından itibaren açıkça yazılacak.

2. 🔴 **S00, S02, S05 — [DERS 176 · Çift Zemin Çelişkisi]:**
   - *Arıza:* Aynı prompt içinde zemin dokusunun hem toz hem obsidyen kayalık olarak çelişkili verilmesi.
   - *Çözüm:* Zemin yalnız "koyu obsidyen mineral kayalığı ve kristalize mor damarlar" olarak sabitlenecektir; toz/toprak kelimeleri kullanılmayacaktır.

3. 🔴 **S08 & S09 — [KART 12 · Politika / Solunum Kısıtlaması Red Riski]:**
   - *Arıza:* Kask içi panik veya oksijensizlik anlatılırken kan/boğulma kelimelerinin kullanılması ve red alınması.
   - *Çözüm:* Solunum güçlüğü yalnız kask içi buğulanma, dijital basınç sayacının düşüşü ve titreyen ellerin stabil eforu olarak nötr/pozitif yazılacaktır.

4. 🔴 **S08 & S09 — [DERS 192 · Doruğun Boşalması Riski]:**
   - *Arıza:* Reçine sürme anının jenerik hareketsiz görüntüye dönüşmesi.
   - *Çözüm:* S08 ve S09 video promptlarında reçine ucunun vizör çatlağına teması ve vakum altında anında saydamlaşması pozitif fiillerle kilitlenecektir.

---

## 2. 🟡 SAHNE BAZLI DERS UYARILARI

| Sahne | Ölçülmüş Kaynak | Arıza / Risk | Yapılacak İşlem |
|---|---|---|---|
| **S00** | `THE_FROST_LINE` QA | Vakumda dumanın Dünya gibi yükselmesi | Buhar ve duman spreyinin vakum ortamında düz hatlar halinde hızla dağılması tarif edilecek. |
| **S01** | `DERS 37/57` | Vizör açık/kapalı belirsizliği | Vizör tam kapalı ve sızdırmazlık contalı olarak kilitlenecek. |
| **S03** | `THE_SINKING_STAKE` QA | Göğüs kontrol paneli ışıklarının sahneler arası kayması | Paneldeki 3 gösterge ışığı ve dijital sayaç ekranının konumu sabitlenecek. |
| **S04** | `DIKEY_MIKRO_DRAMA §4.2` | El temasının kadraj dışında kalması | Parmakların obsidyen mineral kristalini kavrayışı yakın plan makro ile (pay ≥%25) verilecek. |
| **S07** | `DERS 146` | Erüyen reçine renginin değişmesi | Reçine rengi her sahnede "amber rengi saydam sıvı" olarak kilitlenecek. |
| **S10** | `DERS 180` | Mutlak sessizliğin ses modelini bozması | Ses yatağına hafif telsiz statik tonu ve kask içi soluk ritmi verilecek. |
| **S11** | `FINAL_VE_PAYLASIM §2` | Kapanış karesinin açılışla bağlantısız kalması | Kapanışta tamir edilen vizörün yansımasında ufuktaki ikiz yıldız gösterilerek kafiye kurulacak. |

---

## 3. 📋 TEKRAR EDEN ARIZA CEVAP TABLOSU

| Arıza Tipi | Bu Filmde Var mı? | Gerekçe & Önlem |
|---|:--:|---|
| **Çift Zemin Çelişkisi** | Var | S00-S11'de yalnız obsidyen zemin tanımı kullanılacak. |
| **Yasak Kelime Kullanımı** | Var | Promptlarda `camera`, `cinematic` vb. kelimeler temizlenecek. |
| **Monotonik Işık Hataları** | Var | Gezegen yüzey ışığı tek yönlü güneş ve mor mineral ışıması olarak ayrıştırılacak. |
| **ASL Eğrisi Sapması** | Var | Kurguda sahneler 6.0 - 10.0 sn bandında tutulacak. |
