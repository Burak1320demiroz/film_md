# 🧾 SUSMAYAN_NOBETCI — ÜRETİM DEFTERİ

> **Kim doldurur:** ÜRETİM (görev kartı B). Yazım değil — bu dosya film klasörü
> açılırken BOŞ doğar, her kabul edilen klipte bir satır uzar.
>
> **Neden var (11.09.2026):** ⑬ UYUM merceği "bu klip kendi promptunun dediği şey mi"
> sorusunu sorar ve ikinci bir soruyu daha sorar: **kilit prompt'ta hiç yok muydu,
> yoksa model mi uymadı?** İkinci soru ancak *gönderilen* prompt biliniyorsa
> cevaplanır. Bu defter olmadan mercek, gönderilmemiş olabilecek bir metinle
> kıyaslar ve bulgularının yarısı sahte olur.
>
> ⛔ **DEFTERSİZ ⑬ KOŞUSU YOKTUR.** Rubriğin STEP −1'i bu dosyayı ister.
> ⛔ **Prompt dosyaları ÜRETİMDEN SONRA GÜNCELLENMEZ** — ne bu filmde ne başkasında.
> Üretilmiş filmin promptu kanıttır; ⑬ onu ölçer, değiştirmez. Kazanç bir sonraki
> filmin dersinde toplanır.

---

## 0. 🎛️ ARAÇ AYARI — ilk klipten ÖNCE [D215 · 14.09.2026]

```
□ altyazı/caption: KAPALI     □ filigran: YOK (ücretli katman/ayar)     □ konuşan ağız: kadraj dışı
   (bu üçü prompt cümlesiyle değil ARAÇ AYARIYLA çözülür — ADAY-7 kapanışı;
    kurgu kapısı ④ üç sayıyı masterda ölçer)
⛔ İşaretsiz kutuyla üretilen klip KABUL EDİLMEZ.

MOTOR:        OMNI 1.1 Flash (I2V) · zincir modu ① tek başlangıç karesi
              ⬜ K2 — S36-S37 için mod ② (başlangıç + bitiş karesi) denenecek mi? sahip kararı
KLİP SÜRESİ:  ⬜ K3 — ilk KABUL klibinde ÖLÇÜLÜR [D124], plandaki 10 s VARSAYIMDIR:
              ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
              ⛔ Ölçüm 10 s'den saparsa MUZIK dosyasındaki bütün saniyeler ve YAYIN_PAKETI
                 bölüm zamanları yeniden hesaplanır — plan saniyeleri elle düzeltilmez.
QA BİRİMİ:    ⬜ K1 — 4 çeyrek (`--bolum n/4`) mü, 2 yarım mı; QA_SPEC A bloğu PART GRID satırı
```

---

## 0b. 🔬 İLK GÜN PROBLARI — kliplerden önce, üçü de tek tek

```
P1  KURAL PROBU (S0 gövdesi):      dikişinden ayrılan gövde + ≤2 s düz buz kristali konisi + dönüşün korunması
                                   tek karede okunuyor mu? Okunmuyorsa 1 no. risk açıktır, S45'e gidilmez.
P2  VURUŞ DİLİ PROBU (S45):        ateş topu / ışın / duman geliyor mu? Üç denemede malzeme dili tutmuyorsa
                                   İPTAL KAPISI işler (novumun görüntüsü yok).
P3  TEMAS PROBU (S36):             iki halka ÇARPIP GERİ SEKİYOR mu, yoksa gövdeler iç içe mi geçiyor?
P4  KASK BİÇİM PROBU (A kurulumu): referans paketi YAZILMADI [D74 ⑥] — telafi, ilk günün Scene Foundation
                                   karelerinde kask/vizör biçiminin üç yönde (A · C · E) aynı çıkması.
                                   Üç kare aynı biçimi vermiyorsa D146 riski açılır, 04_UYARI R2'ye işlenir.
```

---

## 1. 📦 TESLİM SATIRI — master kimliği

> Bir kere yazılır, kurgu bittiğinde. D188'in (teslim şüphesi) ölçüm ayağı budur:
> "plan 16 sahne yazıyor, dört mercek makarada 32 sahne saydı" krizi bu satır
> yazılmadığı için çözülemedi.

```
MASTER DOSYA:    ⬜ (ad + yol)   ⛔ DEPO DIŞINDA durur — bu repoda image/video
                 bulunmaz [.gitignore · 08.09 + 11.09 sahip kararı]. Buraya
                 dosyanın KENDİSİ değil, KİMLİĞİ yazılır.
SHA-256:         ⬜        ← shasum -a 256 <master>
SÜRE:            ⬜ s      ← ölçülen, planlanan değil (ffprobe) · plan ızgarası 480 s
SAHNE SAYISI:    ⬜        ← sahne_kapisi.sh çıktısı · plan 48
PROMPT SAYISI:   48        ← bölüm dosyalarındaki 🎥 VİDEO PROMPT sayısı (12 + 12 + 12 + 12)
⛔ SAHNE ≠ PROMPT ise TESLİM UYUŞMAZLIĞI: hiçbir mercek koşulmaz, önce bu kapanır.
İHRAÇ:           ⬜ çözünürlük · ⬜ fps · ⬜ LUFS · ⬜ dBTP   (hedef: 1440p+ · BT.709 · −14 LUFS · −1,0 dBTP)
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır (satırlar ÜRETİM SIRASIYLA dizildi, dramatik sırayla değil)

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.
> Satır numaraları 18.09.2026 yazımındaki bölüm dosyası satırlarıdır (📸 görsel · 🎥 video başlığı).
> MOTOR · ÇÖZÜNÜRLÜK · İLERLEDİ (üretim ilerleyip sonda mı düştü: E/H) · AŞAMA (red hangi aşamada: İSTEK/ÇIKTI) —
> red defteri TK/MÇ sınıfının ölçüm ayağı (`09_URETIM_RED_DEFTERI.md`).
>
> **Sıfırıncı halka — Scene Foundation ana kareleri (üretim günü 1, klip değil, kare):**
> boş kokpit A · C · E yönleri · dış çapa Z (gezegen kenarı + uydunun tarayan ışığı) ·
> tahliye gemisi tek gövde J · çekici tek gövde I. Referans paketi YAZILMADIĞI için
> biçim kilidinin tek telafisi bu altı karedir; hepsi kabul edilmeden 1. satıra geçilmez.

| sıra | sahne | prompt kaynağı (dosya · satır) | MOTOR | ÇÖZÜNÜRLÜK | seed | araç ayarı ☑ | deneme | durum | İLERLEDİ | AŞAMA | kabul tarihi | as-built sapma |
|:--:|---|---|---|---|---|:--:|:--:|---|:--:|---|---|---|
| 1 | S36 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 28 · 🎥 44 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 2 | S37 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 72 · 🎥 88 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 3 | S44 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 380 · 🎥 396 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 4 | S45 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 424 · 🎥 440 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 5 | S29 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 248 · 🎥 264 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 6 | S30 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 292 · 🎥 308 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 7 | S47 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 512 · 🎥 528 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 8 | S46 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 468 · 🎥 484 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 9 | S00 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 28 · 🎥 44 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 10 | S03 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 160 · 🎥 176 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 11 | S04 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 204 · 🎥 220 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 12 | S15 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 160 · 🎥 176 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 13 | S16 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 204 · 🎥 220 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 14 | S38 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 116 · 🎥 132 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 15 | S39 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 160 · 🎥 176 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 16 | S40 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 204 · 🎥 220 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 17 | S41 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 248 · 🎥 264 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 18 | S42 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 292 · 🎥 308 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 19 | S43 | `SUSMAYAN_NOBETCI_BOLUM_4.md` · 📸 336 · 🎥 352 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 20 | S24 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 28 · 🎥 44 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 21 | S25 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 72 · 🎥 88 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 22 | S26 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 116 · 🎥 132 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 23 | S27 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 160 · 🎥 176 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 24 | S28 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 204 · 🎥 220 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 25 | S31 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 336 · 🎥 352 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 26 | S32 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 380 · 🎥 396 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 27 | S33 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 424 · 🎥 440 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 28 | S34 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 468 · 🎥 484 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 29 | S35 | `SUSMAYAN_NOBETCI_BOLUM_3.md` · 📸 512 · 🎥 528 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 30 | S12 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 28 · 🎥 44 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 31 | S13 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 72 · 🎥 88 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 32 | S14 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 116 · 🎥 132 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 33 | S17 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 248 · 🎥 264 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 34 | S18 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 292 · 🎥 308 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 35 | S19 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 336 · 🎥 352 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 36 | S20 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 380 · 🎥 396 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 37 | S21 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 424 · 🎥 440 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 38 | S22 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 468 · 🎥 484 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 39 | S23 | `SUSMAYAN_NOBETCI_BOLUM_2.md` · 📸 512 · 🎥 528 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 40 | S01 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 72 · 🎥 88 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 41 | S02 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 116 · 🎥 132 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 42 | S05 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 248 · 🎥 264 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 43 | S06 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 292 · 🎥 308 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 44 | S07 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 336 · 🎥 352 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 45 | S08 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 380 · 🎥 396 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 46 | S09 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 424 · 🎥 440 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 47 | S10 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 468 · 🎥 484 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 48 | S11 | `SUSMAYAN_NOBETCI_BOLUM_1.md` · 📸 512 · 🎥 528 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |

```
DURUM:   KABUL · RET (sebep tek kelime: kurulum · negatif · sayım · okunurluk · fizik · politika · yüz · figür · kask)
SEED:    OMNI'de alan belgesiz → "belgesiz" [D142]; VEO'ya geçilirse araçta alan VAR mı önce sınanır
ARAÇ:    OMNI · VEO — sürüm biliniyorsa yazılır
S36-S37: zincir modu ① (tek başlangıç karesi) ile mi ② (başlangıç+bitiş) ile mi üretildi → "as-built sapma" sütununa mod no
AS-BUILT SAPMA:
   NONE                          → gönderilen metin, dosyadaki metinle BİREBİR aynı
   ARŞİV: SUSMAYAN_NOBETCI_S<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
                                    §3'e birebir kopyalanır (emsal: THE_BLUE_DRIFT_S1_ASBUILT_V1)
⛔ "hatırlamıyorum" bir cevap değildir: o klip için ATIF sütunu ⑬'te
   "🅑 doğrulanamadı" olur ve o sahne kilit sayımına GİRMEZ.
```

---

## 3. 🗄️ AS-BUILT ARŞİVİ — yalnız sapma varsa

> Dosya başına bir giriş; gönderilen metin **birebir**, parafraz değil.
> ⛔ Bu arşiv prompt dosyasının yerine geçmez, onun YANINDA durur: dosyadaki metin
> filmin tasarımı, buradaki metin o klibi gerçekten üreten metindir.

```
| arşiv dosyası | sahne | neden farklı (tek cümle) |
|---|---|---|
| ⬜ | ⬜ | ⬜ |
```

---

## 3b. ⛔ İPTAL KAPISI — üç sahne, üçer deneme

```
S36 — çekicinin halkası tahliye halkasına ÇARPIP GERİ SEKMİYORSA (içinden geçiyor / gövdeler birleşiyor)
      ya da temas kesmeye düşüyorsa üç denemeden sonra film ÜRETİLMEZ (doruk yok)
S45 — vuruş ateş topu / ışın / duman olarak geliyorsa ve üç denemede malzeme dili tutmuyorsa film ÜRETİLMEZ
      (novumun görüntüsü yok)
S0  — ilk 10 s'de ayrılma okunmuyorsa hook yok → varyant (HOOK §7); iki varyant da düşerse film durur
⛔ Kapı işlerse satır SİLİNMEZ: deneme sayısı ve RET sebebi defterde kalır, sonuç buraya tek satır yazılır.
```

---

## 4. ✅ DEFTER KAPANIŞ KONTROLÜ

```
□ ARAÇ AYARI üç kutusu ilk klipten ÖNCE işaretlendi (§0)
□ P1-P4 probları koşuldu ve sonuçları yazıldı (§0b)
□ İLK KABUL satırı = PLAN'daki ÜRETİM SIRASI'nın ilk halkası — bu filmde **S36**.
  Değilse İKİNCİ KLİP ÜRETİLMEZ: sıra baştan başladıysa elde hep KURULUM kalır ve
  eksik sahneler filmin karar bloğu olur [D168 · 3 vaka · KARAR 13.09.2026]
□ klip süresi ilk kabul klibinde ÖLÇÜLDÜ ve 10 s varsayımı doğrulandı/düzeltildi [D124 · K3]
□ her kabul edilen klibin satırı var (master'daki sahne sayısı = KABUL satırı sayısı)
□ teslim satırı dolu ve SHA-256 yazılı
□ sahne_kapisi.sh koşuldu, çıktısı ⑬ koşusuna verilmek üzere duruyor
□ as-built sapması olan her klip için arşiv dosyası VAR
⛔ Bu sekiz madde kapanmadan ⑬ UYUM merceği koşulmaz; koşulursa ATIF sütunu
  boş kalır ve mercek kendi varlık sebebini kaybeder.
```
