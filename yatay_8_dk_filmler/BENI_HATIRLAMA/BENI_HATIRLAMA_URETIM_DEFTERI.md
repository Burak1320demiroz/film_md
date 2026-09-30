# 🧾 BENI_HATIRLAMA — ÜRETİM DEFTERİ

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

## 0. 🧭 ÜRETİM SIRASI VE ÖN KOŞULLAR — ilk klipten ÖNCE [D168 · PLAN §B5]

```
ARAÇ AYARI [D215] — ilk klipten ÖNCE işaretlenir:
   □ altyazı/caption: KAPALI     □ filigran: YOK     □ konuşan ağız: kadraj dışı (48/48 — replikler post-dub)
MOTOR: OMNI (gemini-omni-1.1-flash) I2V · zincir ① tek başlangıç karesi · S37 ② başlangıç+bitiş ⬜ K2 sahip kararı
       VEO yalnız yüzlü sahnede (S1 · S6 · S8 · S29 · S35 · S38 · S44) ÇIKTI aşamasında red gelirse — satırda MOTOR değişir
İŞ AKIŞI: 360p okunabilirlik denemesi → 720p SEÇİM → 4K büyütme · SEED: OMNI'de belgesiz → "belgesiz" yazılır, uydurulmaz [D142]
KLİP SÜRESİ: ilk KABUL klibinde ffprobe → PLAN / SPEC / MUZIK ızgarası aynı formülle güncellenir [D124]
⛔ İLK KABUL satırı S37 değilse İKİNCİ KLİP ÜRETİLMEZ.
⛔ İPTAL KAPISI: S37 · S36 · S15 (PLAN) — biri tutmuyorsa film üretilmez; karar bu deftere tarihli satır olarak yazılır.
```

| adım | iş | çıktı | durum | not |
|:--:|---|---|:--:|---|
| P0 | K3 PROBU — S15 tek kare, saydamlık cümlesinin iki biçimi (BOLUM_2 S15 görsel promptu + "the dune crest is clearly visible through her shoulders and sweater") | 2 × 4 kare · hangisi tek, yarı saydam, yüzsüz kadın figürü veriyor | ⬜ | depoda saydam insan figürü hiç üretilmedi (C7) |
| P1 | SCENE FOUNDATION — boş mağara master × 4 ışık durumu (L1 kaş lambaları · L2 kısık canlı · L3 yanık damarlar · L4 + gün ışığı lekesi), kurulum L açısından | 4 master kare | ⬜ | insansız: NEGATIVE yerine Style satırı |
| P2 | SCENE FOUNDATION — boş düzlük + iniş aracı (hatch angled camera-right) + çıkıntı master, kurulum B açısından | 1 master kare | ⬜ | tüm dış karelerin görsel çapası |
| P3 | İlk onaylı varlık kırpımları: kask (S36/S38 karesinden) · canlı (S37/S39) · atkı (S30) · araç (P2) | 4 kırpım | ⬜ | paket değil, KAPI 0 değil — sonraki imajlara görsel girdi |

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
SÜRE:            ⬜ s      ← ölçülen, planlanan değil (ffprobe)
SAHNE SAYISI:    ⬜        ← sahne_kapisi.sh çıktısı
PROMPT SAYISI:   48 (+ S37 yedek 1 video · 2 görsel sürüm, sayıma girmez) ← bölüm dosyalarındaki 🎥 VİDEO PROMPT sayısı
⛔ SAHNE ≠ PROMPT ise TESLİM UYUŞMAZLIĞI: hiçbir mercek koşulmaz, önce bu kapanır.
İHRAÇ:           ⬜ çözünürlük · ⬜ fps · ⬜ LUFS · ⬜ dBTP
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır (satırlar ÜRETİM SIRASIYLA dizildi, dramatik sırayla değil)

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.
> Satır numaraları 17.09.2026 yazımındaki bölüm dosyası satırlarıdır (📸 görsel · 🎥 video başlığı).
> MOTOR · ÇÖZÜNÜRLÜK · İLERLEDİ (üretim ilerleyip sonda mı düştü: E/H) · AŞAMA (red hangi aşamada: İSTEK/ÇIKTI) —
> red defteri TK/MÇ sınıfının ölçüm ayağı (`09_URETIM_RED_DEFTERI.md`).

| sıra | sahne | prompt kaynağı (dosya · satır) | MOTOR | ÇÖZÜNÜRLÜK | seed | araç ayarı ☑ | deneme | durum | İLERLEDİ | AŞAMA | kabul tarihi | as-built sapma |
|:--:|---|---|---|---|---|:--:|:--:|---|:--:|---|---|---|
| 1 | S37 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 62 · 🎥 79 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 2 | S36 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 18 · 🎥 34 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 3 | S47 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 564 · 🎥 581 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 4 | S00 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 26 · 🎥 42 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 5 | S15 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 153 · 🎥 170 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 6 | S30 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 290 · 🎥 307 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 7 | S11 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 518 · 🎥 533 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 8 | S44 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 432 · 🎥 448 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 9 | S38 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 163 · 🎥 180 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 10 | S39 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 208 · 🎥 224 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 11 | S40 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 252 · 🎥 268 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 12 | S41 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 296 · 🎥 313 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 13 | S42 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 342 · 🎥 358 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 14 | S43 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 387 · 🎥 403 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 15 | S45 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 475 · 🎥 491 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 16 | S46 | `BENI_HATIRLAMA_BOLUM_4.md` · 📸 518 · 🎥 535 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 17 | S24 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 16 · 🎥 33 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 18 | S25 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 62 · 🎥 79 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 19 | S26 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 109 · 🎥 126 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 20 | S27 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 155 · 🎥 171 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 21 | S28 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 199 · 🎥 216 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 22 | S29 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 245 · 🎥 262 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 23 | S31 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 336 · 🎥 352 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 24 | S32 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 380 · 🎥 396 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 25 | S33 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 424 · 🎥 441 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 26 | S34 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 470 · 🎥 487 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 27 | S35 | `BENI_HATIRLAMA_BOLUM_3.md` · 📸 516 · 🎥 532 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 28 | S12 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 18 · 🎥 34 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 29 | S13 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 62 · 🎥 79 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 30 | S14 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 109 · 🎥 125 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 31 | S16 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 200 · 🎥 217 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 32 | S17 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 246 · 🎥 263 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 33 | S18 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 294 · 🎥 311 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 34 | S19 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 340 · 🎥 357 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 35 | S20 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 387 · 🎥 403 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 36 | S21 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 431 · 🎥 448 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 37 | S22 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 477 · 🎥 493 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 38 | S23 | `BENI_HATIRLAMA_BOLUM_2.md` · 📸 521 · 🎥 537 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 39 | S01 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 70 · 🎥 86 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 40 | S02 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 114 · 🎥 130 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 41 | S03 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 159 · 🎥 175 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 42 | S04 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 202 · 🎥 219 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 43 | S05 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 247 · 🎥 264 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 44 | S06 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 294 · 🎥 310 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 45 | S07 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 337 · 🎥 354 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 46 | S08 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 384 · 🎥 401 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 47 | S09 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 429 · 🎥 446 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |
| 48 | S10 | `BENI_HATIRLAMA_BOLUM_1.md` · 📸 476 · 🎥 491 | OMNI | ⬜ | belgesiz | ⬜ | 1 | ⬜ | ⬜ | ⬜ | ⬜ | NONE |

```
DURUM:   KABUL · RET (sebep tek kelime: kurulum · negatif · sayım · okunurluk · fizik · politika · yüz · figür · kask)
SEED:    OMNI'de alan belgesiz → "belgesiz" [D142]; VEO'ya geçilirse araçta alan VAR mı önce sınanır
ARAÇ:    OMNI · VEO — sürüm biliniyorsa yazılır
S37:     ANA sürüm (başlangıç+bitiş) ya da B SÜRÜMÜ (yedek) — hangisi üretildiyse "as-built sapma" sütununa sürüm adı
AS-BUILT SAPMA:
   NONE                          → gönderilen metin, dosyadaki metinle BİREBİR aynı
   ARŞİV: BENI_HATIRLAMA_S<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
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

## 4. ✅ DEFTER KAPANIŞ KONTROLÜ

```
□ İLK KABUL satırı = PLAN'daki ÜRETİM SIRASI'nın ilk halkası (doruk / merkezî seçim).
  Değilse İKİNCİ KLİP ÜRETİLMEZ — sıra baştan başladıysa elde hep KURULUM kalır ve
  eksik sahneler filmin karar bloğu olur [D168 · 3 vaka · KARAR 13.09.2026]
□ her kabul edilen klibin satırı var (master'daki sahne sayısı = KABUL satırı sayısı)
□ teslim satırı dolu ve SHA-256 yazılı
□ sahne_kapisi.sh koşuldu, çıktısı ⑬ koşusuna verilmek üzere duruyor
□ as-built sapması olan her klip için arşiv dosyası VAR
⛔ Bu dört madde kapanmadan ⑬ UYUM merceği koşulmaz; koşulursa ATIF sütunu
  boş kalır ve mercek kendi varlık sebebini kaybeder.
```
