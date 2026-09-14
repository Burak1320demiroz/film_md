# 🔵 THE BLUE DRIFT — FİLM KAYDI

> **Durum:** film üretildi ve kurgulandı (20.08.2026 · ~4:14 teslim dosyası).
> **Ölçüm:** iki koşu var —
> **KOŞU 1** (18.08) filme özel S1 üretim kapısı,
> **KOŞU 2** (20.08) beş mercek (🔧 📖 🧩 🧍 🔊), hepsi tek oturumda, hepsi mod V.
> ⛔ **HİÇBİR SKOR SATIRI TABLOYA GİRMEDİ.** KOŞU 2 ortak adım ⑤'ten
> geçemedi (sahne sayıları 10 / 15 / 15 · film 25 segment) ve ortak adım
> ①'de ön koşudur (SPEC planda hazırken mod V koşuldu). Gerekçe aşağıda.

---

## 🚪 KOŞU 1 — S1 tek klip kapısı

```
MALZEME:  1 klip (~10 s), as-built prompt = S1 VIDEO V1
RUBRİK:   FILME_OZEL/THE_BLUE_DRIFT_QA_CRITIQUE_PROMPT.md
HAM:      02_HAM_RAPORLAR/THE_BLUE_DRIFT/THE_BLUE_DRIFT_S1_KAPI_HAM.md
MOD:      D (SPEC gömülü)
```

⛔ **KOŞU EKSİK BİÇİMLİDİR — GÖZLEM SETİ SAYILIR.** Rapor rubriğin çıktı
şablonunu kullanmadı: künye, gözlem defteri, zaman kodu, atıf etiketi,
skor tablosu ve karar yok. Sonuç: bulgular gerçek ve işlenir, **ama**
① hiçbir kategoriye SAYI yazılmaz, ② atıf operatör tarafında yapılmıştır
(aşağıdaki tablo modelin değil, as-built metniyle yapılan karşılaştırmanın
sonucudur), ③ **C2 (arka planın zaman içinde sabitliği) ÖLÇÜLMEDİ** —
kapının açılış sebebi olan "arka plan değişti" şikâyeti hâlâ AÇIK.

### Bulgu → atıf defteri

| # | Bulgu | Atıf | Kanıt (as-built metninde) | Eylem |
|---|---|---|---|---|
| 1 | Telsiz konuşması / insan sesi duyuluyor | 🅐 MODEL DRIFT (prompt tarafı ağırlaştırıcı) | Yasak yazılıydı ama yalnız `AUDIO:` paragrafında ("No voices, no music"); NEGATIVE'de ses maddesi YOKTU. Ayrıca "on the radio channel" ifadesi çekim yapıyordu | Yasak NEGATIVE'e taşındı (25 video promptu); "radio channel" → "closed comms channel — carrier hiss only" |
| 2 | Pilotun elinde istenmeyen tablet/pano, sonra kayboluyor | 🅑 **PROMPT GAP** | Promptta pilotun 0.0–6.0 s arası eli HİÇ tarif edilmemişti; boşluğu model doldurdu | TIMELINE'a t=0 el durumu yazıldı ("both gloves empty and open at his sides — he carries nothing at any point") + `No unnamed prop…` negatifi 25 promptta |
| 3 | Numune kutusu yerde kendiliğinden beliriyor | 🅑 **PROMPT GAP** | Kutunun 6.0 s'den önceki yeri tanımsızdı | t=0 durumu yazıldı: kutu zaten pilotun ayağının dibinde, kapağı kapalı; 3.5 s'de kapak KOLDAN kaldırılıyor |
| 4 | Eller karota ve kutuya eriyor (merging) | 🅐 MODEL DRIFT | Kilit promptta VARDI: "Hand contacts keep clear structural boundaries — no merging" | Kural değil TASARIM değişti [AGENTS §8]: karota **işlenmiş uç kapak** eklendi, eldiven artık buza değil metale tutunuyor; negatif buna göre yeniden yazıldı |
| 5 | Vizör camı YOK gibi görünüyor (yüz açıkta okunuyor) | 🅑 **PROMPT GAP** | Promptta yalnız "optically clear … zero reflection" vardı — bu modele "cam çizme" demektir. D95'in üç görünürlük işareti (çerçeve + yaka mührü + tek parlama çizgisi) yalnız REFERANS PAKETİNDE yazılıydı, sahne promptlarında YOKTU | VİZÖR KİLİDİ 10 prompta gövdeye, 29 prompta negatife işlendi |
| ✅ | Kamera/kadraj · 2 insan · suit + turkuaz/amber · planetshine + bantlı dev · landerin yeri | 🅒 NOT A FINDING | — | korunur |

### Kapının kazandırdığı

```
🅑 PROMPT GAP sayısı: 3 / 5 bulgu.
Yani bu klip aynı promptla yeniden üretilseydi bulguların ÜÇÜ aynen
tekrarlardı — para iki kez yanardı. Kapının varlık sebebi tam olarak bu.
```

### ⬜ AÇIK MADDELER

```
⬜ C2 arka plan sabitliği ölçülmedi (rapor şablonu kullanılmadı) —
   operatörün "arka plan değişti" şikâyeti raporda DOĞRULANMADI:
   rapor tersine "environment flawless" dedi. İki olasılık ayrışmadı:
   ① kayma kare-içi (ilk kare ↔ son kare) idi ve rapor bakmadı,
   ② şikâyet IMAGE ile VIDEO arasındaki farktı.
   → Kapatma yolu: yeni koşuda şablon zorunlu; ledger'ın
     "first-frame vs last-frame" satırı doldurulmadan koşu kapanmaz.
⬜ Ses bulgusu 🅐 mı 🅑 mi tam ayrışmadı: yasak vardı ama yanlış blokta.
   Yeni koşu bunu ayırır (yasak artık NEGATIVE'de).
```

---

## 🎬 KOŞU 2 — BEŞ MERCEK · TAM KURGU (20.08.2026)

```
MALZEME:  teslim kurgusu · ~254 s (raporların hepsi TAHMİNİ süre verdi)
MERCEK:   🔧 VIDEO · 📖 SENARYO · 🧩 MANTIK · 🧍 KARAKTER · 🔊 SES
MOD:      beşi de V — SPEC planda §QA SPEC BLOĞU'nda HAZIRDI, verilmedi
OTURUM:   beşi de AYNI dış model oturumunda arka arkaya koşuldu
HAM:      02_HAM_RAPORLAR/THE_BLUE_DRIFT_{TEKNIK,SENARYO,MANTIK,KARAKTER,SES}_HAM.md
```

### ⛔ ORTAK ADIM KAPILARI — sonuç

| # | Kapı | Sonuç |
|---|---|---|
| ③ | **KİMLİK** [D105] | ✅ **GEÇTİ** — metin olmayan beş çapa: 9 s'lik hook bloğu · sahne şeridinin 4:09'da bitmesi · ızgaraya oturan 14 replik · sayısal kilitler ("kabin yüzde kırk" %40 ibre · "altmış" 60 m) · 3:50-3:59'da filmin TEK kasksız sahnesi. ⛔ Başlık kartı kimlik kanıtı olarak KULLANILMADI |
| ① | **SPEC** [D94] | ⚠️ **ÖN KOŞU** — SPEC hazırdı, mod V koşuldu. Skor satırları Ⓥ ⚠️ ŞARTLI olurdu; ⑤ nedeniyle zaten yazılmadı. Kesme listeleri ve REMOVE reçeteleri UYGULANMAZ |
| ④ | **KURGU** [D109] | ⚠️ **YARIM** — sahne şeridi: 25 klip ✅ (ızgara geri alma ile doğrulandı), 249 s ✅ (son sahne 4:09'da bitiyor, plan RUNTIME birebir). Teslim dosyası 254 s ❌ — fark, sahne olmayan başlık kartıdır. **Kart çıkarılınca kapı 4/4 kapanır** [D93 mekanizması: kapı önce ayıklar, sonra sayar] |
| ⑤ | **ÇAPRAZ SAYIM** [D107] | 🚨 **DÜŞTÜ** — 📖 10 sahne · 🧩 15 · 🧍 15 · 🔧 saymadı · 🔊 saymadı. Fark 5 > 1 → partinin TÜM satırları GEÇERSİZ: **hiçbir tabloya skor yazılmadı, bulgudan ders yazılmadı** |
| ⑤b | **AYNI OTURUM** [D110] | 🚨 **KOPYA** — 🧩 ve 🧍 aynı 15 bloğu, aynı zaman kodlarını, aynı üç bulguyu bildirdi. Bu doğrulama değil, ortak defterdir |
| ⑥ | **ÇAPRAZ GÖZLEM** [D108] | tablo aşağıda — dört gözlem birden çok mercekte, her biri TEK sahibe bağlandı |
| ⑦ | **PARMAK İZİ** [D112] | ✅ temiz — önceki mod V partisi (Black Cradle, 232 s) ile süre/segment geometrisi tutmuyor |
| ⑧ | **FRAGMAN** [D111] | ✅ malzeme FİLM (25 sahnelik ızgara doğrulandı), mercek seçimi doğru |
| ② | **KİLİT ÇELİŞKİSİ** [D96] | defter aşağıda — **21 madde, hepsi ⬜ AÇIK** |

---

### ⭐ IZGARA GERİ ALMA — SAHNE SIRASI DENETİMİ

> **Soru:** videodaki sahne sırası doğru mu?
> **Yöntem:** raporlar sahne saymayı beceremedi, ama **replik zaman kodu
> verdiler**. Planın ızgarası (9 s hook + 24 × 10 s) ve prompt
> TIMELINE'larındaki replik ofsetleri belgede yazılı. İkisini toplamak
> her repliğin ekranda kaçıncı saniyede duyulması gerektiğini verir:
> `beklenen = ızgaradaki sahne başlangıcı + prompt içi replik ofseti`
> Master'a bakmadan, yalnız iki belgeyle çalışır.

| Plan | Izgara | Prompt ofseti | Beklenen | 🔊 ledger | Δ |
|---|---|:--:|:--:|:--:|:--:|
| S2 KERTE | 0:19-0:29 | 2.5 s | 0:21.5 | 0:22 | +0.5 ✅ |
| S6 PİLOT | 0:59-1:09 | 1.5 s | 1:00.5 | **0:51** | **−9.5** ⚠️ |
| S6 KERTE | 0:59-1:09 | 4.5 s | 1:03.5 | **0:54** | **−9.5** ⚠️ |
| S9 KERTE | 1:29-1:39 | 2.0 s | 1:31 | 1:33 | +2 ✅ |
| S10 MÜHENDİS | 1:39-1:49 | 6.5 s | 1:45.5 | 1:47 | +1.5 ✅ |
| S11 KERTE | 1:49-1:59 | 7.0 s | 1:56 | 1:55 | −1 ✅ |
| S13 KERTE | 2:09-2:19 | 3.0 s | 2:12 | 2:13 | +1 ✅ |
| S14 KERTE | 2:19-2:29 | 2.0 s | 2:21 | 2:21 | 0 ✅ |
| S14 PİLOT | 2:19-2:29 | 7.5 s | 2:26.5 | 2:28 | +1.5 ✅ |
| S16 KERTE | 2:39-2:49 | 3.0 s | 2:42 | 2:43 | +1 ✅ |
| S17 KERTE | 2:49-2:59 | 2.0 s | 2:51 | 2:51 | 0 ✅ |
| S17 PİLOT | 2:49-2:59 | 7.0 s | 2:56 | 2:56 | 0 ✅ |
| S19 MÜHENDİS | 3:09-3:19 | 5.0 s | 3:14 | 3:14 | 0 ✅ |
| S20 KERTE | 3:19-3:29 | 2.0 s | 3:21 | 3:20 | −1 ✅ |
| S21 KERTE | 3:29-3:39 | 8.5 s | 3:37.5 | 3:39 | +1.5 ✅ |
| S22 PİLOT | 3:39-3:49 | 7.5 s | 3:46.5 | 3:46 | −0.5 ✅ |

```
16 repliğin 14'ü ±2 s içinde. Tek sapma S6'nın İKİ repliği, ikisi de
tam −9.5 s — yani bir ızgara dilimi erken.
```

**Üç bağımsız doğrulama daha (hepsi raporların kendi sayılarından):**

```
① 🧩 envanterinin 15 bloğunun 15'i, ardışık ızgara dilimlerinin BİREBİR
   birleşimidir. Blok 1 = 0:00-0:09 → planın 9 saniyelik hook'u, tam.
      blok 2 = S1+S2 · 3 = S3+S4 · 4 = S5+S6 · 5 = S7+S8 · 6 = S9+S10+S11
      7 = S12+S13 · 8 = S14+S15+S16 · 9 = S17 · 10 = S18+S19+S20
      11 = S21 · 12 = S22 · 13 = S23 · 14 = S24 · 15 = KART
② Sahne şeridi 4:09'da bitiyor = 249 s = planın RUNTIME'ı, birebir.
③ 🔧'ün 2:31'deki gaz boşalması, planın S15 (VİRAL #3 NEFES) penceresine
   (2:29-2:39) düşüyor — 🧩 o kareleri "kokpit" diye 30 s'lik bloğa gömdü.
```

#### İKİNCİ, BAĞIMSIZ DOĞRULAMA — 🔧'ün zaman kodlarının İÇERİĞİ

> Replik hizalaması sesi kullanır. Bu tablo hiç ses kullanmaz: 🔧'ün her
> bulgusunun ne GÖSTERDİĞİ, o saniyedeki ızgara diliminin planda ne
> göstermesi gerektiğiyle karşılaştırılır. On bir bulgunun on biri tutuyor.

| 🔧 zaman kodu | Raporun gördüğü | Izgara dilimi | Planda o sahne |
|---|---|:--:|---|
| 0:12 | parmaklar karot numunesinde | S1 (0:09-0:19) | KAROT — azot buzu karotu çekiliyor ✅ |
| 0:43 | koşu, ikiz siluet | S4 (0:39-0:49) | VİRAL #1 PERDE — kameraya doğru koşu ✅ |
| 0:52 | konuşma var, dudak yok | S5/S6 (0:49-1:09) | telsiz repliği ✅ (⚠️ 🔊 ledger'ıyla aynı erken saniye) |
| 1:15 | dikey jetler kayboluyor | S7 (1:09-1:19) | KALKIŞ — 20 m'de karın lüleleri kesilir, kuyruk devralır ✅ |
| 1:20 | gemiyle yan yana giden perde | S8 (1:19-1:29) | PERDENİN KENARI — perdenin alt kenarını sıyırarak geçiş ✅ |
| 1:41 | el/eldiven teması | S10 (1:39-1:49) | NABIZ — mühendis mekanik kolu çeviriyor ✅ |
| 2:10 | gövdede amber kubbe | S13 (2:09-2:19) | DÖNÜŞ SORUNU — dış yakın, verici nabzı çalışıyor ✅ |
| 2:31 | airlock'tan gaz boşalması | S15 (2:29-2:39) | VİRAL #3 NEFES — 6 puf × 1.5 s ✅ |
| 3:04 | konsolda eldivenli el yakın çekim | S18 (2:59-3:09) | BEKLEYİŞ — iki eldiven konsolda yan yana ✅ |
| 3:50 | kasksız yüzler | S23 (3:49-3:59) | İLK YÜZLER — filmin TEK kasksız sahnesi ✅ |
| 4:10 | başlık kartı | — | planda YOK ❌ |

⭐ 🧩'in blok içerikleri de aynı sırayı veriyor: yüzey → kokpit → kalkış →
yörünge → istasyon → hangar → kasksız güverte → dış manzara. 🧩'in
"parlayan kutu rafta" notu, planın S23'ündeki **karot kutusu yuvasında**
ayrıntısıdır — yani kurulum (S1'de çekilen karot) karşılığını ekranda alıyor.

#### ✅ HÜKÜM: SIRA DOĞRU — bir tek 20 saniyelik pencere hariç

```
25 sahnenin sırası plandaki sırayla birebir örtüşüyor. Eksik sahne
YOK, yer değiştirmiş blok YOK, süre birebir.

⬜ TEK AÇIK NOKTA — 0:49-1:09 (20 saniye, tek kontrol):
   S6'nın replikleri bir ızgara dilimi erken duyuluyor. Üç ihtimal:
     H1  S5 (BİNİŞ) ile S6 (ATEŞLEME) yer değiştirmiş →
         önce ateşleme, sonra kayışların bağlanması görülür
     H2  S5 düşmüş, yerini başka bir 10 s doldurmuş
     H3  ledger'ın o bölgedeki zaman kodu kaymış — EN ZAYIF İHTİMAL:
         diğer 14 nokta ±2 s tuttu, üstelik 🔧 de bağımsız olarak
         0:52'de "konuşma var" dedi (iki mercek, aynı erken saniye)
   KAPATMA: 0:49-1:09 arası izlenir. Önce kayışlar mı kilitleniyor
   (S5, sessiz, tamamen arkadan), yoksa önce pilotun eli kola mı
   gidiyor + "Kalkıyoruz" mı (S6)? Doğru sıra: önce S5, sonra S6.

⛔ 4:09'DAN SONRASI FİLMİN SAHNESİ DEĞİLDİR: ~5 saniyelik başlık kartı.
   Plan bunu iki yerde yasaklıyor (PLAN §D72 kapısı "ekran metni 0.0 sn
   — başlık kartı DAHİL" · PART_B kurgu kapısı). Kartın kaldırılması
   sıra denetimini de, süre kapısını da (254 → 249) kapatır.
```

---

### 🔒 KİLİT ÇELİŞKİSİ DEFTERİ [D96] — 21 madde, hepsi ⬜ AÇIK

> Kural: rapor **planda yazılı bir kilide** aykırı bir şey söylüyorsa, o
> bulgu bulgu listesinden ALINIR ve buraya gelir. "Film mi saptı, rapor
> mu uydurdu" sorusu rapordan çözülemez; master'ın O SANİYESİNE bakılır.
> ⛔ ⬜ AÇIK madde varken: skor şartlı, **bulgudan ders yazılmaz**,
> yeniden üretim siparişi verilmez.

**A · REPLİK METNİ — plandaki cümleyle rapordaki cümle tutmuyor**

| # | Kontrol | Rapor ne dedi | Plandaki kilit | Sonuç |
|---|---|---|---|---|
| K1 | **2:12-2:18** | "Saniyede **kırk** derece dönüyor**uz**. Böyle kavrayamay**ız**." | S13: "Saniyede **bir** derece dönüyor**sunuz**. Böyle kavrayama**m**." · sayısal kilit: dönüş **1°/s → 0** | ⬜ |
| K2 | **1:45-1:51** | "**İtici** sağlam. **Yörüngeye oturmamız** yeter." | S10: "**Verici** sağlam. **Görünür olmamız** yeter." — filmin TEZİ bu cümlededir | ⬜ |
| K3 | **2:20-2:26** | "**Avanis içimizdedir.** Ben sayarım, sen **çekersin**." | S14: "**Havanız iticinizdir.** Ben sayarım, sen **çevir**." — MERKEZİ SEÇİM repliği | ⬜ |
| K4 | **3:19-3:25** | "Altmış **pencere**." | S20: "Altmış **metre**. Motorlarım kapalı. Geliyorum." | ⬜ |
| K5 | **3:20-3:30** | aynı replik İKİ kez (3:22 + 3:26) | S20: bir kez | ⬜ |
| K6 | **2:38-2:47** | "Dönüş sıfır" İKİ kez (2:40 + 2:43) | S16: bir kez | ⬜ |

```
⚠️ K1-K4 doğrulanırsa bu, depoda ilk kez ölçülen bir hata sınıfıdır:
   Türkçe repliğin ÜRETİMDE bozulması — sayı kayması (1→40), kişi
   kayması (2. şahıs → 1. çoğul), anahtar sözcük kayması (verici→itici,
   metre→pencere) ve kelime uydurma (havanız iticinizdir → avanis
   içimizdedir). Ders yazımı K1-K4 kapanmadan BAŞLAMAZ.
⚠️ 📖 merceği K3'ün BOZUK hâlini filmin en iyi repliği ilan etti
   ("hints at a wider world") ve K1'in bozuk hâlini "cut this line"
   diye reçeteledi. Mod V, bozulmayı ödüllendirdi.
```

**B · SES MİMARİSİ**

| # | Kontrol | Rapor ne dedi | Plandaki kilit | Sonuç |
|---|---|---|---|---|
| K7 | **0:22 · 1:33 · 2:13 · 2:43 · 3:39** | 2 ses, ikisi de HUMAN, **0 MACHINE**; KERTE'nin cümleleri iki insan sese bölünmüş | AUDIO REGISTER: 10 replik MACHINE (KERTE, gövdesiz, uzaktaki gemiden, telsizle) · sayı söyleyen HER replik KERTE'nindir | ⬜ |
| K8 | **2:21 · 3:14 · 3:46** | ledger'da "Mouth visible: **Yes**" | kokpit tamamen ARKADAN çekilir, ağız hiçbir karede okunmaz [D82 sigortası] | ⬜ |
| K9 | **1:19-1:29** | "vakumda motor sesi 🔴" | S7 AUDIO: zeminden iletilen boğuk gümbürtü (2% atmosfer) · S8 AUDIO: **5. saniyede sert vakum sessizliği** | ⬜ |

```
⚠️ K7 kapanmadan 🔊'nin "sentetik/duygusuz okuma" bulguları İŞLENMEZ
   [kart E3 adım 2]: KERTE'nin düz okuması tasarımın kendisidir.
   Raporun kendi FLAGS sorusu ("bunlar android mi?") bunun kanıtıdır —
   mercek, makine sesini insan sanmış olabilir.
   D82 (Cold Burn) TAM OLARAK bu hataydı: mimari üretimde tersine döndü.
   Blue Drift'te sigorta hem plana hem 25 promptun gövdesine yazıldı
   ("radio-only from the distant ship — no body, no avatar").
   K7 "film saptı" derse: D82 sigortası YAZILI OLDUĞU HÂLDE tutmadı.
   K7 "rapor uydurdu" derse: sigorta tuttu, ölçüm aleti göremedi.
   İkisi de derstir; hangisi olduğunu 30 saniyelik dinleme söyler.
```

**C · TASARIM MI, HATA MI — "önerme" kapısı** [D87]

> Bu dört madde raporlarda **bulgu** olarak yazıldı. Dördünün de planda
> yazılı bir tasarım kaynağı var. Kapı yalnız 🧩 kartında koşuyor;
> üçü 🧩 dışından geldiği için hiçbir kapı görmedi.

| # | Kontrol | Rapor ne dedi | Plandaki tasarım | Sonuç |
|---|---|---|---|---|
| K10 | **1:19-1:29** | 🔧 🔴 "aurora, geminin yanında vakumda sürükleniyor" | S8 PERDENİN KENARI: araç plazma perdesinin ALT KENARINI sıyırarak geçer | ⬜ tasarım |
| K11 | **1:55-2:15** | 🔧 🟠 + 🧩 🟡 "gövdede turuncu kubbe belirdi" | S10'dan itibaren **verici kubbesinin amber nabzı** — filmin umut sembolü, S12'de "nabız düzenli" | ⬜ tasarım |
| K12 | **3:29-3:39 + 3:59-4:09** | 🧩 🟠 "tünelin içine girdi ama sonra dış gövdede duruyor" · **reçete: 4:00 çekimini kes** | S21 hangar İÇİNDEN + S24: omurgadaki **AÇIK yakalama yuvası** dışarıdan görünür; lander kollarda durur | ⬜ tasarım |
| K13 | **0:49-0:59** | 🔧 🔴 "ses var, dudak kımıldamıyor" | kapalı kask + telsiz + arkadan kadraj: ağzın kımıldamaması TASARIMIN KENDİSİDİR | ⬜ tasarım |

```
⛔ K12'nin reçetesi uygulansaydı filmin PLANLI FİNALİ (S24) kesilecekti.
⛔ K13, 🔧'ün iki 🔴'sinden biridir ve filmin ses mimarisini hata sayar.
```

**D · GERÇEK OLABİLECEK BULGULAR — master'da 10'ar saniye**

| # | Kontrol | Rapor ne dedi | Neden önemli | Sonuç |
|---|---|---|---|---|
| K14 | **0:39-0:49** | 🔧 🔴 + 🧍 🔴 "0:43 saydam ikiz siluet" | S4 = VİRAL #1, kameraya koşu [D104]. İkiz gerçekse viral kare gider | ⬜ |
| K15 | **2:59-3:09** | 🔧 🔴 "3:04 sol elde 6 parmak, konsola giriyor" | S18 = BEKLEYİŞ, filmin en sessiz sahnesi ve **iki eldivenin yakın çekimi**. Doğruysa filmin taşıyamayacağı kare | ⬜ |
| K16 | **1:39-1:49** | 🔧 🔴 "1:41 eller anatomik yumruya kaynıyor" | S10 = mühendis mekanik kolu çeviriyor; temas kilidi | ⬜ |
| K17 | **0:09-0:19** | 🔧 🔴 "0:12 parmaklar karota eriyor" | KOŞU 1'in 4 numaralı bulgusu; çözüm TASARIM değişikliğiydi (karota işlenmiş uç kapak). **Teslim edilen S1 düzeltilmiş sürüm mü?** | ⬜ |
| K18 | **2:29-2:39** | 🔧 🔴 "2:31 boşalan gaz aşağı düşüyor" | S15 = VİRAL #3 NEFES · kilit: 6 puf × 1.5 s, **DÜZ** çıkar. Doğruysa viral kare gider | ⬜ |
| K19 | **1:09-1:19** | 🔧 🟠 "1:15 dikey jetler kaybolurken gizli morph kesme" | S7 kilidi: 20 m'de ayaklar katlanır, karın lüleleri KESİLİR, kuyruk motorları devralır — geçiş tasarımlı; "kesme" mi geçiş mi? | ⬜ |
| K20 | **3:49-3:59** | 🔧 🔴 "3:50 iki yüz birden morph" ↔ 🧍 "3:50 yüzler TEMİZ ve tutarlı" | S23 = filmin TEK kasksız sahnesi, ilk çıplak yüzler. **İki mercek aynı saniye için zıt şey söylüyor** | ⬜ |
| K21 | **4:09-4:14** | 🔧 🔴 metin · 🧍 🔴 kimlik kırılması + yara izi · 🧩 🟠 · 📖 "film fragmana dönüyor" | Kart planın hiçbir yerinde yok. 📖'ün alıntıladığı slogan ("HE'S NOT TRYING TO SURVIVE. HE'S WAITING.") **depoda hiçbir dosyada geçmiyor** ve "HE" tekil — film iki kişilik. Kart bizim mi, modelin mi, raporun uydurması mı? | ⬜ |

```
⭐ K21 tek başına dört mercekte bulgu üretti ve süre kapısını düşürdü.
   5 saniyelik, sahnesi olmayan malzeme; kaldırılması 5 saniyelik iş.
```

---

### 🔁 ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108]

| Gözlem (timecode) | Hangi raporlarda | Sahibi | Puanı kim taşır |
|---|---|---|---|
| 4:10 ekran metni / başlık kartı | 🔧 🧍 🧩 📖 | 🔧 (metin serinin negatif çekirdeğinde) | 🔧 — diğer üçü işaretçiye iner (→🔧) |
| 3:50 yüz durumu | 🔧 🧍 | 🧍 (yüz kimliği bu merceğin konusu) | 🧍 — 🔧 hücresi kaynaksız kalır |
| 0:43 ikiz siluet | 🔧 🧍 | 🧍 (Sayı ve Ayrışma) | 🧍 |
| dudak-fonem / vakumda ses | 🔧 🔊 (out-of-scope) | 🔧 | 🔧 |
| ortam yatağı delikleri, replik tekrarı | 🔊 | 🔊 | 🔊 |

---

### 📋 FLAGS FOR DOCUMENT CHECK — plandan cevaplar

> Kart C/D/E/E2/E3 adım 2: mod V raporlarının soruları plan dosyasından
> cevaplanır. Cevaplar bulgu değildir; soruyu kapatırlar.

| Soru (hangi mercek) | Plandan cevap |
|---|---|
| 🔧 "vizörler açık mı, yüzey solunabilir mi?" | **Hayır.** Kask takvimi: 17 sahne KAPALI / 1 sahne kasksız (S23, basınçlı hangar güvertesi). Yüzey %2 atmosfer. Vizörün görünmemesi D95'in bilinen tuzağı — S1 kapısında da çıktı, çözüm 10 prompta çerçeve + yaka mührü + tek parlama çizgisi olarak işlendi |
| 🔧 "ses var, dudak yok — telsiz mi?" | **Evet.** Tüm insan replikleri KAPALI KASK telsizinden; kokpit arkadan çekilir, ağız hiçbir karede okunmaz. Bu tasarımdır (K13) |
| 🔊 "karakterler android mi? sıfır duygu, sıfır nefes" | **Kısmen: 16 repliğin 10'u MACHINE'dir** (KERTE, gövdesiz gemi AI'ı). Düz okuma o 10 replikte doğrudur. İnsan replikleri: pilot 4, mühendis 2 |
| 🔊 "3:22 ve 3:26 tekrarı senaryoda var mı?" | **Yok.** S20'de replik bir kez söylenir → K5 |
| 🧩 "tripod taşınıyor, bir daha görünmüyor" | Plan bir tripod tanımlamıyor; S3 TOPLAMA'da ekipman kutulanır ve **karot kutusu S23'te yuvasında görünür** — kurulum karşılığını alır. Elde kalan cismin ne olduğu ⬜ (K17 ile aynı bakışta görülür) |
| 🧩 / 📖 "bu bir film mi, fragman mı?" | **Film.** 25 sahne × ızgara doğrulandı. Kart plana ait değildir → K21 |
| 🧍 "vizör mühürlü mü, çıkarılmış mı?" | **Mühürlü** (S23 hariç). Raporun "okunamıyor" demesi doğru refleks [D95] |
| 📖 "seri kuralı 'tek karakter' bilerek mi kırıldı?" | **Evet, planlı.** İki kişilik ekip bilinçli karardır (KART 4 insan sayısı kilidi: 2). Rubriğin seri DNA'sı 2-4 dk uzay ailesi içindir |

---

### 📚 DERS HASADI

```
⛔ ⑤ DÜŞTÜĞÜ İÇİN BULGUDAN DERS YAZILMADI.
   Yazılan iki ders, filmin bulgularından değil, ÖLÇÜMÜN KENDİ
   GEOMETRİSİNDEN çıkarıldı (raporların sayıları + deponun kendi
   kartları). İkisi de master'a bakmadan doğrulanabilir:

   DERS 115 — ızgara geri alma / hizalama kapısı
              kaynak: 10 / 15 / 15 sahne bildirimi vs 25 segmentlik ızgara
   DERS 116 — "önerme" kapısının yalnız tek kartta koşması
              kaynak: K10-K13 · dört tasarım öğesi dört mercekte bulgu oldu

   TEKRAR KAYDI (yeni numara AÇILMADI — AGENTS §8):
   · D107 tekrarladı — rubrik yaması yerindeydi, raporlar yine blok saydı
   · D110 tekrarladı — beş mercek tek oturumda koşuldu, iki rapor kopya
   · D93 mekanizması genel kapıya taşındı (kart ④: önce ayıkla, sonra say)
   · D72 tekrarladı — kart yasağı planda İKİ yerde yazılıydı, kart geldi

   BEKLEYEN DERS ADAYLARI (K1-K4 ve K7 kapanınca yazılır):
   A1 · Türkçe replik üretimde bozuluyor: sayı, kişi ve anahtar sözcük
        kayması + kelime uydurma (kırk/bir · verici/itici · metre/pencere)
   A2 · Replik kliple birlikte tekrarlanıyor: aynı cümle iki kez
   A3 · D82 sigortası prompt gövdesinde yazılı olduğu hâlde tutmadıysa,
        register kilidi metinle değil ÜRETİM AYRIMIYLA korunmalı
        (KERTE'nin repliği ayrı ses geçişi olarak üretilir)
```

---

### ⬜ AÇIK MADDELER — operatörün iş listesi (toplam ~4 dakika master)

```
1. 0:49-1:09  (20 s) → S5/S6 sırası           [sıra denetiminin tek açığı]
2. 0:22 · 1:33 · 2:13 · 2:43 · 3:39 (30 s) → KERTE sentetik mi, insan mı  [K7]
3. 2:12-2:18 · 1:45-1:51 · 2:20-2:26 · 3:19-3:25 (25 s) → replik metinleri [K1-K4]
4. 2:38-2:47 · 3:20-3:30 (20 s) → replik tekrarları  [K5 K6]
5. 0:39-0:49 · 2:59-3:09 · 1:39-1:49 · 0:09-0:19 · 2:29-2:39 (50 s) → el/ikiz/gaz [K14-K18]
6. 3:49-3:59  (10 s) → yüz durumu, iki mercek zıt      [K20]
7. 4:09-4:14  (5 s)  → kart nereden geldi              [K21]

Bu yedi bakış kapanınca:
   · kart kaldırılır → ④ kapısı 4/4 kapanır (25 klip · 249 s · metin 0.0 sn)
   · K1-K4/K7 sonucuna göre ders adayları (A1-A3) yazılır
   · SPEC bloğu kopyalanıp mercekler MOD D'de yeniden koşulur
     ⭐ depoda mod D hiç denenmedi; SPEC bu filmde hazır
```
