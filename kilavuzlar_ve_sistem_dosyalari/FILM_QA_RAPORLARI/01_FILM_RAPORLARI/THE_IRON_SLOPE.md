# 🪜 THE IRON SLOPE — FİLM KAYDI

> **Durum:** film üretildi ve kurgulandı · teslim dosyası `~/Downloads/the ıron slope.mp4`
> **Ölçüm:** 25.08.2026 · **altı mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES · 📖 HİKAYE
> · 🖼️ ARKA PLAN · ⚖️ FİZİK) — **altısı da mod V.**
> ⛔ **SKOR SATIRLARI T1-T6'YA ⚠️ ŞARTLI GİRDİ, TAMLIK MATRİSİ ❌ KALDI.**
> Parti ortak adım ①'de ön koşudur (SPEC dosyası olmalıydı, depoda yok) ve
> ortak adım ④'ten geçmedi (süre 65,0 s ≠ 48,0 ± 2).
>
> ⭐ **BU KOŞUNUN GERÇEK ÇIKTISI SKOR DEĞİL, ÖLÇÜMDÜR.** Master dosya
> ffprobe/ffmpeg ile ölçüldü; kilit çelişkisi defterinin 8 maddesinin 7'si
> ⬜ AÇIK kalmadan kapandı. İki bulgu sınıfı ilk kez **RAPOR UYDURDU**
> damgası yedi ve ikisi de makineyle ölçülebilir alandaydı → **DERS 125**.

---

## 📦 MALZEME VE HAM DOSYALAR

```
MALZEME:  teslim kurgusu · 65,000 s (video akışı) · 720×1280 · 30 fps · AAC ses
MERCEK:   🔧 1_KARE · 🔗 2_DEVAMLILIK · 🔊 3_SES · 📖 4_HIKAYE
          · 🖼️ 5_ARKA_PLAN · ⚖️ 6_FIZIK   (altısı da mod V)
OTURUM:   🚨 ŞÜPHELİ — altı raporun altısı da AYNI ve AYNI ÖLÇÜDE YANLIŞ kesme
          listesini verdi (0:09/0:18/0:29/0:39/0:49/1:00). Gerçek ızgara
          düzgün 10 saniyeliktir. Bağımsız ölçüm olsaydı yanlışların dağılması
          beklenirdi [D110].
HAM:      ../02_HAM_RAPORLAR/THE_IRON_SLOPE_{KARE,DEVAMLILIK,SES,HIKAYE,ARKA_PLAN,FIZIK}_HAM.md
PLAN:     ../../../dikey_shorts_filmler/THE_IRON_SLOPE/THE_IRON_SLOPE_DIKEY_SHORTS.md
SPEC:     ⛔ YOK — `THE_IRON_SLOPE_QA_SPEC.md` 24.08'de yazılmıştı, depoda
          bulunmuyor; 25.08'de plandan yeniden üretildi. Altı koşunun mod V
          olmasının maddi sebebi budur.
KAYNAK KLİPLER: ~/Downloads/Man_climbing_*.mp4 — 6 dosya, HER BİRİ 10,005 s
```

---

## ⭐ ÖLÇÜM KAPISI — master'dan okunan sayılar (rapor sayıları DEĞİL)

> Bu bölüm 25.08.2026'da açıldı ve **DERS 125**'in kaynağıdır. Aşağıdaki
> dört komut ~30 saniye sürer ve raporların sayılarını ezer.

```bash
# ① süre / çözünürlük / fps
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate "$M"
# ② kesme ızgarası (sahne sınırları saniye cinsinden)
ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"
# ③ sessizlik var mı (ambiyans deliği bulgusu ancak bundan sonra kabul edilir)
ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 | grep silence_
# ④ saniyelik RMS (ses seviyesi eğrisi)
ffmpeg -i "$M" -af "aresample=8000,asetnsamples=8000,astats=metadata=1:reset=1,\
ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null -
```

| Ölçülen | Master (ölçüm) | Raporlar (altısı da) | Plan kilidi | Sonuç |
|---|---|---|---|---|
| Toplam süre | **65,000 s** | 1:05 measured ✅ | 48,0 s | 🔴 +17,0 s |
| Sahne süresi | 6 × **10,00 s** = 60,03 s | "~9-11 s" | 6 × 8,0 s | 🔴 klip süresi 10 s |
| Kesme ızgarası | **10,03 · 20,03 · 30,03 · 40,03 · 50,03 · 60,03** | 0:09 · 0:18 · 0:29 · 0:39 · 0:49 · 1:00 | — | 🚨 altı rapor da yanlış |
| Başlık kartı | **60,03-65,00 (4,97 s)** — "THE IRON SLOPE / NO WAY BACK" | 1:00-1:05 ✅ | ekran metni **0,0 s** | 🔴 ihlal [D61a/D70] |
| Sahne sayısı | **6** | 6 ✅ | 6 | ✅ |
| İnsan şeridi | **111111** | 111111 ✅ | 111111 | ✅ |
| En-boy | **720×1280 (9:16)** | 9:16 ✅ | 9:16 | ✅ (1080×1920 değil) |
| Sessizlik | **YOK** — −50 dB/0,3 s eşiğini geçen tek an yok | "S4 tamamen dijital sessizlik" 🔴 | — | 🚨 RAPOR UYDURDU |
| Ses tabanı | saniyelik RMS: sahne bloğunda (0-60 s) min **−26,8 dB** (0. sn), kart saniyesi −31,3 dB · S4 (30-40 s): **−19,7…−22,8 dB** | "S4 dead air / None" | — | 🚨 RAPOR UYDURDU |
| Ses katmanı | 0-60 s kesintisiz geniş bant + düzenli vuruşlu katman (spektrogram) | "no music present" | müzik 120 BPM | ⚠️ şüpheli — 10 sn dinleme |

⚠️ **Sahne süresi ölçümü, kaynak klip dosyalarıyla bağımsız olarak doğrulandı:**
`Man_climbing_*.mp4` altı dosyanın altısı da **10,005 s**. Yani sapma kurguda
değil, **üretim aracının klip süresinde** doğdu → **DERS 124**.

---

## ⛔ ORTAK ADIM KAPILARI — sonuç

| # | Kapı | Sonuç |
|---|---|---|
| ③ | **KİMLİK** [D105] | ✅ **GEÇTİ** — metin olmayan üç çapa: gemi gövdesindeki merdivende kesintisiz tırmanış (planın tek hareket tipi) · S5'te yuvarlak hava kilidi kapağı + turuncu motor jantı (planın S5 kompozisyonu) · sahne sayısı 6 ve insan şeridi 111111. ⛔ Başlık kartındaki "THE IRON SLOPE" yazısı kimlik kanıtı olarak KULLANILMADI — ④ HİKAYE ve ③ SES onu künye sandı [D105 tekrarı, dördüncü vaka] |
| ① | **SPEC** [D94/D117] | ⚠️ **ÖN KOŞU** — SPEC ayrı dosya olacaktı, dosya depoda yoktu; altı merceğin altısı da mod V. Kesme listeleri ve REMOVE reçeteleri **UYGULANMAZ**. Depoda mod D sayısı hâlâ **0** |
| ④ | **KURGU KAPISI** [D109/D118/D120] | 🚨 **(b) DÜŞTÜ** — (a) klip 6 = plan 6 ✅ · (b) süre 65,0 s ≠ 48,0 ± 2 🔴 · (c) insan şeridi 111111 = plan ✅. Film boyuna bakan kategoriler (Yapı · Duygu Yayı · Final · Tutundurma · Ortam Devamlılığı) **SAYI TAŞIMAZ**; başlık kartı sayımın ve sürenin dışında tutuldu |
| ⑤ | **ÇAPRAZ SAYIM** [D107] | ✅ sayısal olarak geçti (altısı da 6 sahne / 6 kesme) — ⛔ **ama kapı bu partide işe yaramadı:** altı rapor da aynı YANLIŞ ızgarayı bildirdi. Uyuşma doğruluk değildir → **DERS 125** |
| ⑦ | **PARMAK İZİ** [D112] | ⚠️ **YAKIN** — künye (65 s · 6 segment · ~10 s sahne · 1:00'da kart) D112'nin tarif ettiği desene (62/63 s · 7 segment · ~10 s · 0:58 kart) çok benziyor. Ama bu kez desen GERÇEK: master ölçümü künyeyi doğruladı. Kapı, ölçüm kapısı koşulduğunda kendiliğinden kapanıyor |
| ⑧ | **FRAGMAN MERCEĞİ** [D111] | ✅ gerekmez — malzeme FİLM |
| ⑨ | **HİZALAMA** [D115] | ✅ koşuldu — ızgara PLANDAN değil MASTER'dan alındı (sessiz film): 6 × 10,00 s. Planın 8 s ızgarası ekranda hiç yok; tohum (0:05,8) ve karşılığı (44,4) gibi bütün zaman kodları geçersiz |
| ⑩ | **ÖNERME** [D87/D116] | ✅ koşuldu — 4 bulgu düştü, bkz. §ÖNERME KAPISI |
| ② | **KİLİT ÇELİŞKİSİ** [D96] | ✅ **8 maddenin 7'si KAPANDI** (master ölçüldü), 1 madde ⬜ AÇIK. Bkz. defter |

---

## 🔒 KİLİT ÇELİŞKİSİ DEFTERİ [D96]

| # | Rapor ne dedi (tc) | Hangi kilit | Çözüm eylemi | Sonuç |
|---|---|---|---|---|
| 1 | "loose panel floats away… constant v, no drop" (0:02-0:09 · ⚖️ L2, 🔧, 🔗, 🖼️) | Motion Bible: düşüş 2,16 m/s², 1 s→1,08 m · 3 s→9,7 m; kavis/süzülme 0 kare | S0'ın 1,0-4,0 s'i 0,6 s aralıklarla kare kare ölçüldü | 🔴 **FİLM SAPTI** — panel gövdeye göre **sabit ~0,15 m/s**, yana-yukarı; 10 saniyenin sonunda hâlâ kadrajda. Kilitli değer 3. saniyede 9,7 m = kadrajın ~2,5 katı. **Novum ekrana gelmedi** |
| 2 | "S4 complete digital silence 0:30-0:39" (🔊 🔴 BLOCKER) | — (ses tasarımı planda: nefes + gövdeden iletilen ses + müzik) | silencedetect + saniyelik RMS | 🚨 **RAPOR UYDURDU** — dosyada sessizlik yok; S4 −19,7…−22,8 dB. Ambiyans skoru geçersiz |
| 3 | "ambience dead air at every cut" (🔊 ×3) | — | aynı ölçüm | 🚨 **RAPOR UYDURDU** — kesmelerde taban düşmüyor |
| 4 | "background morphs: hull → truss → engine" (🔗 🖼️ 📖 ⚖️) | Ship Bible: tek gövde, üç kelepçeli kurulum | 15/25/35/45/55 s kareleri | 🟠 **FİLM SAPTI (kısmen)** — S0/S5 planın kompozisyonu (gövde + jant · kapak + motor); S1-S4 arasında gövde tipi, kapak yeri ve latis yerleşimi tutmuyor. Latisin S3'te olması ise PLANLI (bkz. önerme kapısı) |
| 5 | "Earth/planet in frame" — **hiçbir rapor yazmadı** | Negatif blok (12/12 promptta): `no planet, no moon` | 22/24/25/28 s kareleri | 🔴 **FİLM SAPTI + MERCEK GÖRMEDİ** — S2'de gezegen kadrajın alt üçte birini kaplıyor; ⑤ ARKA PLAN altı sahnenin altısında "FAR FIELD: black space, star field" yazdı → **DERS 126** |
| 6 | "chest pack drift / badges" (🔗 kostüm 3/10) | Negatif blok: `no patch, no logo`; Character Bible: düz sırt [D79], işaretsiz kaplama | 58,9 s karesi | 🔴 **FİLM SAPTI** — göğüste kırmızı + mavi dairesel arma ve yanan amber gösterge var; ikisi de yasak. Kostüm sürüklenmesi bulgusu AYAKTA |
| 7 | "mostly static lockoffs with slight slow pans/tilts" (🔧) | Camera Bible: 6/6 TAM LOCKOFF, "absolutely zero camera movement" | S0 ve S2'nin baş/son karesi farkı | 🟠 **FİLM SAPTI** — S0 farkı yalnız özneyi gösteriyor (kamera duruyor), S2'de merdiven ve gövde kenarları çift çıkıyor (kamera kayıyor). Lockoff 6/6 değil |
| 8 | "airborne sound in vacuum" (🔧 🔴 BLOCKER · 🔊 out-of-scope) | Plan: vakumda ses yok; yalnız gövdeden eldivene İLETİLEN ses + nefes + müzik | ⬜ 10 saniyelik dinleme gerekiyor | ⬜ **AÇIK** — ölçüm sesin VARLIĞINI doğruluyor ama "havadan yayılıyor" hükmü kulakla verilir. ⛔ Bu maddeden ders yazılmadı |

---

## 🧬 ÖNERME KAPISI [D87/D116] — düşen bulgular

```
DÜŞEN 1  "1g ağırlıkla tırmanıyor, biyomekanik yanlış" (⚖️ Biyomek. 4/10,
         🔧 Fizik 2/10) — planın dünyası 0 g DEĞİL, 0,220 g itki
         yerçekimidir; botların basamağa basması ve gövdenin ağır olması
         TASARIMDIR [ortam kartı §3.5]. ⚖️'nin "regenerate with zero-g
         locomotion" reçetesi UYGULANMAZ — filmin novum'unu siler.
DÜŞEN 2  "two gravities" hükmünün ADAM tarafı düşer, PARÇA tarafı ayakta:
         çelişki 1g/0g değil, "0,220 g yazıldı, parça 0 g oynadı"dır.
DÜŞEN 3  "truss/lattice geometry is an AI hallucination" (🔧 Çevre 6/10) —
         S3'ün olayı PLANLI: 6 metrelik anten latisi kök bağlantısında
         devrilir ve iki bağda asılı kalır. Latisin VARLIĞI bulgu değildir;
         yerleşiminin sahneden sahneye değişmesi (madde 4) bulgudur.
DÜŞEN 4  "visor shows warm/orange bounce light" (🔗 🟡) — vizör planda
         BERRAK ve tintsizdir; turuncu jant ışığının vizörde görünmesi
         beklenen davranıştır (yansımasızlık kilidi yalnız AYNA kaplamayı
         yasaklar).
AYAKTA   kostüm/arma sürüklenmesi · coğrafya morphu · gezegen · başlık
         kartı · süre · panelin sabit hızı · kamera kayması.
```

---

## 🔧 ① KARE — Ⓥ ⚠️ ŞARTLI · 5,5/10

Ayakta kalan: temas morphu (0:58 civarı elin raya girip çıkması — 57,6-58,8
karelerinde el/ray kesişimi çamurlu, kavrama karesi yok), şerit klipsi (0:45),
dikey kompozisyon (özne merkezde, alt üçte bir kilidi yok), güvenli alan
(0:11-0:18 baş üst bantta).
Düşen: "sound in vacuum" ⬜ AÇIK (defter 8) · "mixed gravity" önerme kapısından
kısmen düştü · "truss geometry hallucination" düştü (planlı).
⛔ Kamera 10/10 verdi — **ölçüm S2'de kamera kaymasını gösteriyor**; kategori
kaynaksız kaldığı için düşürülmedi ama skor bu yüzden ŞARTLI.

**FLAGS cevapları (plandan):**
- *"Stylized non-literal audio?"* → Hayır. Ses tasarımı: nefes + gövdeden
  iletilen boğuk ses + müzik. Serbest kalan parça **tamamen sessizdir**.
- *"Locomotion mode: walking/climbing or tether-pulling/floating?"* →
  **Basamak tırmanışı, 0,5 m/s (S2'de 0,7)**, botlar basar, süzülme 0 kare.

---

## 🔗 ② DEVAMLILIK — Ⓥ ⚠️ ŞARTLI · 5,9/10

Ayakta: Coğrafya 2/10 (defter 4) · Kostüm 3/10 (defter 6 — ve rapor
armaları "drift" sandı, oysa armaların VARLIĞI da yasak) · Dünya propu 3/10
(panellerin sahne arası kaybolması) · Ekipman 5/10 (tether S5'te yok).
Sayı taşımayan (kapı ④): Kurulum · Nedensellik.
Kimlik 7/10 — 🟡 yüz farkı ışık/açıyla açıklanabilir sınırda, kırılma yok.

**FLAGS cevapları (plandan):**
- *"Vizör tinted/clear/gold?"* → **Berrak, tintsiz, ayna kaplama yok.**
- *"Tek yerde kesintisiz tırmanış mı, dev istasyonda montaj mı?"* →
  **Tek gövde, kesintisiz tek tırmanış**; hava kilidine kalan mesafe
  14 → 12 → 9 → 7 → 6 → 4-2 m sayacıyla iner. Coğrafya morphu bu yüzden
  bulgudur, üslup değil.

---

## 🔊 ③ SES — 🚨 GEÇERSİZ (ambiyans ekseni uydurma)

Dokuz kategorinin altısı N/A (replik yok — planın kısıtı, düşük puan değil
[D113]). Kalan üçün en ağırı **Ambiyans 2/10 ve onun 🔴 BLOCKER'ı ölçümle
çürütüldü** (defter 2-3). SFX senk (5/10) ve Miks (6/10) ayakta kalabilir ama
aynı defterden çıktıkları için ŞARTLI. Toplam 4,3/10 tabloya **üstü çizili**
girer.

**FLAGS cevapları (plandan):** film **repliksizdir** (tasarım) · S4 sessiz
DEĞİLDİR · planın tek sessizlik anı 2,2 saniyelik **yanma arasıdır** ve o da
mutlak sessizlik değildir: nefes ve fan devam eder [D83].

---

## 📖 ④ HİKAYE — Ⓥ ⚠️ ŞARTLI · 2,6/10 · ⭐ bu koşunun EN DEĞERLİ raporu

Kapı ④ düştüğü için **Yapı · Duygu Yayı · Final · Tutundurma sayı taşımaz.**
Ama sayı taşımayan hükümleri bu filmin gerçeğidir ve plana karşı okunduğunda
tek bir cümleye iniyor:

> **"THE ONE THING NOTHING ELSE DOES: none found."**
> Filmin bütün varlık sebebi novum'du (uzayda aşağı var). Novum ekrana
> gelmedi (defter 1) → izleyici 60 saniye boyunca "uzayda merdiven çıkan
> adam" gördü. Rapor bunu doğru okudu.

Kesme listesi ve REMOVE reçeteleri **UYGULANMAZ** (ön koşu). "S2/S3/S5 CUT"
önerisi zaten planın sayaç kanallarını siler.

**FLAGS cevapları (plandan):** doruk **S5'tedir** (motorun 2,2 s susması) ve
ekranda YOKTUR · film **teaser değildir**, tek başına duran bir shorts'tur ·
hedef **hava kilidi**, mesafe sayacıyla üç kanaldan sayılır.

---

## 🖼️ ⑤ ARKA PLAN — Ⓥ ⚠️ ŞARTLI · 3,8/10 · matrise girmez

Ayakta: topoloji (3/10), arka set (3/10), kadraj kenarı smear (4/10).
⛔ **Merceğin kendi varlık sebebi ıskalandı:** altı sahnenin altısında da
`FAR FIELD: Black space, star field` yazıldı; S2'de gezegen var (defter 5).
Envanter genel geçer yazıldığında bu mercek çekirdek merceklerden daha az
görüyor → **DERS 126** ve rubrik yaması.

---

## ⚖️ ⑥ FİZİK — Ⓥ ⚠️ ŞARTLI · 7,5/10 · matrise girmez · mod D olacaktı

⭐ Ana bulgusu (serbest parça hızlanmıyor) **doğrulandı** — ama gerekçesi
yanlış: PREMISE REGISTER'ı "none" yazdı, oysa filmin ilan edilmiş bir dünya
kuralı var (0,220 g itki). Register boş kalınca mercek doğru gözlemi yanlış
hastalığa bağladı ("two gravities" → "zero-g locomotion yaz") ve reçetesi
filmin novum'unu silecekti.
**Mod D koşulsaydı** NUMERIC LOCK VERIFICATION tablosu şu satırı verirdi:

```
LOCK: serbest parça 1 s → 1,08 m · 3 s → 9,7 m (kıça doğru, ölü düz)
ÖLÇÜLEN: ~0,15 m/s sabit, yana-yukarı, 10 s sonunda hâlâ kadrajda
Δ: 3. saniyede 9,7 m yerine ~0,45 m           VERDICT: FAIL
```

---

## 🔁 ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108]

| Gözlem (tc) | Hangi raporlarda | Sahibi | Puanı kim taşıyor |
|---|---|---|---|
| Serbest panel hızlanmıyor (0:02-0:09 · 0:40-0:45) | 🔧 🔗 🖼️ ⚖️ | ⚖️ FİZİK (sayı taşıyor) | ⚖️ · diğerlerinde →⚖️ işaretçisi |
| Coğrafya morphu (0:10 → 0:30 → 0:50) | 🔗 🖼️ 📖 ⚖️ | 🔗 DEVAMLILIK | 🔗 · diğerleri işaretçi |
| Vakumda ses (0:00-1:00) | 🔧 🔊 | 🔧 KARE | ⬜ AÇIK — kimse taşımıyor |
| Panelin 2D dönüşü (0:42-0:45) | 🔧 🖼️ | 🔧 KARE | 🔧 · 🖼️ işaretçi |
| Başlık kartı (1:00-1:05) | altısı da | kurgu kapısı ④ | hiçbir kategori — kapı bulgusudur |

---

## 📚 BU KOŞUDAN ÇIKAN DERSLER

```
DERS 124  ARAÇ 10 SANİYE ÜRETİYOR, PLAN 8 SANİYEYE YAZILIYOR — üç filmde
          üç kez (First Morning 64 s · Wrong Shadow 64 s · Iron Slope 65 s).
          Izgara araçtan yazılır ya da kırpma planda sahne sahne verilir.
DERS 125  MAKİNEYLE ÖLÇÜLEBİLEN SAYIYI MODELE SORMA — altı mercek aynı
          yanlış kesme listesini verdi, biri hiç olmayan sessizlikten
          🔴 BLOCKER üretti. Dört komutluk ÖLÇÜM KAPISI raporlardan ÖNCE.
DERS 126  ARKA PLAN MERCEĞİ ALANI GÖRMEDİ — altı sahnede aynı "black space,
          star field" satırı; S2'de kadrajın alt üçte birinde gezegen.
          Envanter en büyük nesneyi ADLANDIRMAK ZORUNDA.
DERS 127  İVME PROMPT'LA GELMİYOR — "her saniye +2,16 m/s" 12 promptun
          12'sinde yazılıydı; ekranda sabit ~0,15 m/s süzülme çıktı.
          Kilitlenebilen şey ivme değil, KADRAJI TERK ETME SÜRESİDİR.
          ⚠️ 123 numarası aynı gün paralel bir yazım oturumunda
          kullanıldığı için bu ders 127 numarasını aldı.
```

---

## 🧾 KARAR — operatörün önüne konan iş (sipariş değil)

```
⬜ 1  10 saniyelik dinleme: 0:00-0:10 — ses havadan mı yayılıyor
      (defter 8'i kapatır, ① KARE'nin 🔴'sini karara bağlar)
⬜ 2  KARAR: film bu hâliyle YAYINLANMAZ. Sebep tek başına süre ya da kart
      değil, NOVUM'UN EKRANA GELMEMESİ (defter 1) — planın kendi kapısı
      zaten bunu yazıyordu: "üretim S0'dan başlar; panel orada çarpar/
      kavis çizer/SÜZÜLÜRSE film üretilmez" [D74 tekrarı: kapı yazılıydı,
      koşulmadı, altı sahne üretildi]
⬜ 3  Yeniden üretim yapılacaksa: önce S0, DERS 127'ün kilit metniyle;
      S0 temiz çıkmadan diğer beş sahne ÜRETİLMEZ
⬜ 4  Kurgu: başlık kartı kaldırılır (metin 0,0 s) · klipler 8,0 s'e
      kırpılır ya da plan 10 s ızgaraya taşınır [DERS 124]
⬜ 5  Sonraki QA turu MOD D — SPEC dosyası 25.08'de yeniden yazıldı
```

> **Bu kaydın özeti bir cümle:** film teknik olarak izlenebilir çıktı, ama
> ölçüm filmin *fikrinin* üretilmediğini gösteriyor — ve bunu ilk söyleyen
> mercek, en düşük puanı veren HİKAYE oldu.
