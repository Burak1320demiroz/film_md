# 🧾 THE_FALLING_WORLD — ÜRETİM DEFTERİ

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

## 0. 🚦 ÜRETİM ÖNCESİ — KAPI 0 ve ARAÇ AYARI

```
KAPI 0 — REFERANS PAKETİ [D168 · ilk halka]
  ⬜ R1 BEYAZ       (4 panel)  → ONAYLI olmadan S00-S46 ÜRETİLMEZ
  ⬜ R2 TURUNCU     (4 panel)  → ONAYLI olmadan S00-S46 ÜRETİLMEZ
  ⬜ R3 HAT AİLESİ  (4 panel)  → ONAYLI olmadan S01·S02·S04-S47 ÜRETİLMEZ
  ⬜ R4 ARAÇ VE GEMİ(4 panel)  → ONAYLI olmadan S03-S13 ve S30-S47 ÜRETİLMEZ
  ⛔ Dördü de 🔴 ZORUNLU: dördü birden ilk üretilen karede (S41) kadrajdadır.

ARAÇ AYARI [D215] — üç kutu, İLK KLİPTEN ÖNCE işaretlenir;
işaretsiz kutuyla üretilen klip KABUL EDİLMEZ:
  ⬜ altyazı/caption: KAPALI
  ⬜ filigran: YOK (ücretli katman/ayar)
  ⬜ konuşan ağız: kadraj dışı — bu filmde FİZİKEN zaten yok (opak vizör),
     yine de araç ayarı işaretlenir

KLİP SÜRESİ ÖLÇÜMÜ [D124 · açık madde K3] — İLK KABUL KLİBİNDE:
  ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
  ÖLÇÜLEN: ⬜ s     (VARSAYIM 10,0 s)
  ⛔ 10,0 s'den saparsa ŞUNLAR YENİDEN HESAPLANIR:
     MUZIK dosyasının DYNAMIC SPREAD'i · sekiz replik saniyesi ·
     YAYIN_PAKETI bölüm zamanları · QA_SPEC B bloğunun GRID ve PART GRID satırları

ZİNCİR MODU [OMNI · açık madde K2]:
  ⬜ ① tek başlangıç karesi (varsayılan — bütün klipler)
  ⬜ ② başlangıç + bitiş karesi — 9 KÜME çifti için denenecek mi:
     S1-S2 · S5-S6 · S10-S11 · S12-S13 · S14-S15 · S16-S17 · S34-S35 · S36-S37 · S43-S44
     SAHİP KARARI BEKLİYOR.

QA BİRİMİ [açık madde K1]:
  ⬜ 4 çeyrek (B1-B4 ayrı koşu)   ⬜ 2 yarım (B1+B2 / B3+B4)
  SAHİP KARARI BEKLİYOR. QA_SPEC A bloğu şu an 4 ÇEYREK varsayıyor.
```

## 0b. 🧪 PROB KLİPLERİ — ilk gün, sıranın DIŞINDA

> Dördü de kabul edilmeden bölüm üretimi başlamaz. Bunlar birer SAHNE değil,
> birer SINAVDIR: reddedilirlerse ilgili sahnenin kamerası taşınır [iki yenilgi kuralı].

| prob | sahne | ne sınanıyor | kabul ölçütü | deneme | durum |
|:--:|---|---|---|:--:|---|
| P1 | S02 | politika yüzeyi — alet nesneye kapanıyor, kayış ayrılıp düşüyor | üretim reddi YOK ve gri kayışın ayrılması tek karede okunuyor | ⬜ | ⬜ |
| P2 | S16 | deponun TEK ÇÖZÜLEMEYEN red profili (yüzsüz izolasyon + kısıtlanmış uzuv) | üretim reddi YOK; ikinci figür kadrajda; hasar manşette okunuyor | ⬜ | ⬜ |
| P3 | S42 | 1 NUMARALI RİSK — hangi hattın ayrıldığı | iki sarı kol açı farkıyla ayrılıyor, ALT kol ayrılıyor, ÜST kol gergin kalıyor | ⬜ | ⬜ |
| P4 | S41 | KART 4 — iki figürün kopyalanması (KRONOS'ta iki ölçülmüş vaka) | kadrajda TAM iki gövde; konum kilidi tutuyor (beyaz sol, turuncu sağ) | ⬜ | ⬜ |

```
⛔ P2 veya P3 İKİ kez düşerse ÜÇÜNCÜ YAZIM DENENMEZ — kamera taşınır:
   S16 → kiriş ve manşet TURUNCU'nun omzu üstünden, aynı L mesafesinde
   S42 → kemer halkası kadrajın merkezinde kalarak 35mm'e geçilir
⛔ İPTAL KAPISI: S41 · S42 · S00 üçünden biri tutmuyorsa FİLM ÜRETİLMEZ.
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
SÜRE:            ⬜ s      ← ölçülen, planlanan değil (ffprobe). PLANLANAN 480 s.
SAHNE SAYISI:    ⬜        ← sahne_kapisi.sh çıktısı. PLANLANAN 48.
PROMPT SAYISI:   48        ← bölüm dosyalarındaki 🎥 VİDEO PROMPT sayısı (12+12+12+12)
⛔ SAHNE ≠ PROMPT ise TESLİM UYUŞMAZLIĞI: hiçbir mercek koşulmaz, önce bu kapanır.
İHRAÇ:           ⬜ çözünürlük · ⬜ fps · ⬜ LUFS · ⬜ dBTP
```

---

## 2. 🎬 KLİP DEFTERİ — klip başına bir satır

> ⛔ Reddedilen deneme SİLİNMEZ, satır olarak kalır (deneme no artar). Bir kilidin
> kaç denemede tuttuğu, o kilidin gerçekten çalışıp çalışmadığının tek ölçüsüdür.

> ⭐ **SATIRLAR ÜRETİM SIRASINDA DİZİLDİ — DRAMATİK SIRADA DEĞİL [D168].**
> İlk halka referans paketidir (§0), ilk KLİP S41'dir.

| # | sahne | prompt kaynağı (dosya · başlık) | araç | seed | deneme | durum | kabul tarihi | as-built sapma |
|:--:|---|---|---|---|:--:|---|---|---|
|  1 | S41 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 41 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  2 | S42 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 42 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  3 | S47 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 47 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  4 | S00 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 0 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  5 | S36 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 36 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  6 | S37 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 37 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  7 | S38 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 38 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  8 | S39 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 39 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
|  9 | S40 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 40 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 10 | S43 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 43 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 11 | S44 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 44 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 12 | S45 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 45 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 13 | S46 | `THE_FALLING_WORLD_BOLUM_4.md` · 🎥 SAHNE 46 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 14 | S01 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 1 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 15 | S02 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 2 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 16 | S03 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 3 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 17 | S04 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 4 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 18 | S05 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 5 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 19 | S06 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 6 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 20 | S07 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 7 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 21 | S08 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 8 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 22 | S09 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 9 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 23 | S10 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 10 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 24 | S11 | `THE_FALLING_WORLD_BOLUM_1.md` · 🎥 SAHNE 11 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 25 | S24 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 24 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 26 | S25 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 25 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 27 | S26 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 26 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 28 | S27 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 27 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 29 | S28 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 28 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 30 | S29 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 29 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 31 | S30 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 30 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 32 | S31 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 31 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 33 | S32 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 32 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 34 | S33 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 33 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 35 | S34 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 34 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 36 | S35 | `THE_FALLING_WORLD_BOLUM_3.md` · 🎥 SAHNE 35 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 37 | S12 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 12 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 38 | S13 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 13 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 39 | S14 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 14 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 40 | S15 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 15 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 41 | S16 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 16 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 42 | S17 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 17 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 43 | S18 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 18 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 44 | S19 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 19 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 45 | S20 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 20 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 46 | S21 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 21 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 47 | S22 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 22 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |
| 48 | S23 | `THE_FALLING_WORLD_BOLUM_2.md` · 🎥 SAHNE 23 | ⬜ | ⬜ | 1 | ⬜ | ⬜ | ⬜ |

```
DURUM:   KABUL · RET (sebep tek kelime: kurulum · negatif · sayım · okunurluk · fizik)
SEED:    araçta alan VAR mı önce sınanır [D142]; yoksa "ALAN YOK" yazılır, uydurulmaz
ARAÇ:    Veo · Flow · <başka> — sürüm biliniyorsa yazılır
ARAÇ AYARI [D215 · 14.09.2026] — üç kutu, ilk klipten ÖNCE işaretlenir; işaretsiz kutuyla üretilen klip KABUL edilmez:
   □ altyazı/caption: KAPALI     □ filigran: YOK (ücretli katman/ayar)     □ konuşan ağız: kadraj dışı
   (bu üçü prompt cümlesiyle değil araç ayarıyla çözülür — ADAY-7 kapanışı; kurgu kapısı ④ üç sayıyı masterda ölçer)
AS-BUILT SAPMA:
   NONE                          → gönderilen metin, dosyadaki metinle BİREBİR aynı
   ARŞİV: THE_FALLING_WORLD_S<nn>_ASBUILT.md → araçta kısaltıldı/değiştirildi; gönderilen metin
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
| — | — | — (henüz sapma yok; ilk sapmada satır açılır) |
```

---

## 4. ✅ DEFTER KAPANIŞ KONTROLÜ

```
□ KAPI 0: R1-R4 dördü de ONAYLI (§0) — değilse hiçbir klip üretilmez
□ ARAÇ AYARI üç kutu işaretli (§0) · P1-P4 prob klipleri KABUL (§0b)
□ İLK KABUL satırı = S41 (bu defterin 1 numaralı satırı) — PLAN'daki ÜRETİM SIRASI'nın ilk halkası.
  Değilse İKİNCİ KLİP ÜRETİLMEZ — sıra baştan başladıysa elde hep KURULUM kalır ve
  eksik sahneler filmin karar bloğu olur [D168 · 3 vaka · KARAR 13.09.2026]
□ her kabul edilen klibin satırı var (master'daki sahne sayısı = KABUL satırı sayısı)
□ teslim satırı dolu ve SHA-256 yazılı
□ sahne_kapisi.sh koşuldu, çıktısı ⑬ koşusuna verilmek üzere duruyor
□ as-built sapması olan her klip için arşiv dosyası VAR
⛔ Bu dört madde kapanmadan ⑬ UYUM merceği koşulmaz; koşulursa ATIF sütunu
  boş kalır ve mercek kendi varlık sebebini kaybeder.
```
