# ❄️ THE FROST LINE — FİLM KAYDI

> **Durum:** film üretildi ve kurgulandı · **İKİ QA PARTİSİ koşuldu, ikisi de mod V.**
>
> | | 1. PARTİ | 2. PARTİ |
> |---|---|---|
> | tarih | 31.08.2026 | 01.09.2026 |
> | mercek | ① ② ③ ④ ⑤ ⑥ (⑥ ×2) | ① ② ③ ④ ⑤ ⑥ |
> | mod | 6/6 **V** | 6/6 **V** |
> | T satırı | **YOK** [D129] | **YOK** [D129 · aynı filmde 2. kez] |
> | raporların toplamı (referans) | ① 5,4 · ② 6,8 · ③ 1,0 · ④ 5,7 · ⑤ 7,6 · ⑥ 5,6 | ① 6,3* · ② 6,2 · ③ 8,0 · ④ 6,2 · ⑤ 6,7* · ⑥ 6,9 |
>
> `*` = raporun kendi aritmetiği hatalı; düzeltilmişi ① 5,7 · ⑤ 6,0 (aşağıda).
>
> ⛔ **HİÇBİR SKOR SATIRI T1-T6'YA GİRMEDİ.** Film klasöründe `THE_FROST_LINE_QA_SPEC.md`
> **VARDIR** (üstünde "bu film 9. olmasın" uyarısıyla) ve altı raporun altısı
> `INPUT MODE: V` → ortak adım ① gereği koşu TEKRARLANIR; ham raporlar 02/'ye düştü,
> T tablosuna satır yazılmadı, kesme listesi ve REMOVE reçetesi UYGULANMADI [D129].
> **SPEC yazılmış olduğu hâlde mod V koşulan film sayısı 9.**
>
> ⭐ **BU KOŞUNUN GERÇEK ÇIKTISI SKOR DEĞİL, ÖLÇÜM VE KARELERDİR.** Master ffprobe/ffmpeg
> ile ölçüldü, 33 kanıt karesi çıkarılıp gözle bakıldı. Üç sonuç her şeyi değiştirdi:
> ① **iki sahne eksik** (S12 tohum kutusu · S23 iç geniş ayna) + hook kırpılmamış;
> ② **ses kanalı VAR** (−21,5 LUFS, yatak 0-230 s kesintisiz) — altı merceğin altısı
> "nothing audible" yazdı [D137 · 4. vaka] ve ③'ün 4 🔴'lı raporu ölçümle GEÇERSİZ;
> ③ **filmin üç novum vuruşu EKRANDAYDI ve mercekler üçünü de görmedi ya da tersine
> okudu**: S5 yama uçuşu (t56) · S15 klip içi beyazlama (t141→t147) · S19 "her şeyin
> kaybı" beyazlaması (t181→t187 — ④ bunu "healthy leaf payoff" diye puanladı).
> Dört yeni ders buradan çıktı: **D151-D154**. Sahip beyanı "bir sahne eksik ürettim"
> — ölçüm **iki** diyor; ikincisi (S23) kuyruktadır [D121 ③: kuyruk filmin finalidir].
>
> ---
>
> ⚡ **2. PARTİNİN ÜÇ BAŞLIĞI** (ayrıntı: bu belgenin sonundaki 2. PARTİ bölümü)
> ① **`~/Downloads` içinde "the frost lıne" adlı BEŞ dosya var ve İKİSİ BU FİLM DEĞİL.**
>    245,120 s'lik çift (720p + 4K) THE PAYLOAD'un gövdesini taşıyor ve üstüne
>    THE FROST LINE kapak kartı eklenmiş. Dosya adı kimlik değildir → **D160**.
> ② **③ SES merceği bu kez ses kanalını DUYDU** (AUDIO STATE B) — 1. partinin
>    "mutlak dijital sessizlik + 4 🔴"ı ölçümle çürümüştü [D137]. Eksen düzeldi;
>    ama ⑪ satırı yine künyeye yapıştırılmadı, o yüzden yine ÖLÇÜLMEMİŞ sayılır.
> ③ **Dört merceğin dördü aynı YANLIŞ bulguyu birebir aynı cümleyle yazdı**
>    ("3:23 parmaklar vizörden geçiyor"). 4K master'dan t202/t203/t204 kafa
>    kırpması: el vizörün ÖNÜNDE, cam çerçevesi ve pane kenarı okunuyor —
>    füzyon YOK. Bu yanlış 🔴, ①'in REGENERATE hükmünü taşıyan dört 🔴'dan
>    biriydi. Kopya bulgu, kopya sayıdan tehlikelidir → **D159**.

---

## 📦 MALZEME VE HAM DOSYALAR — 1. PARTİ (31.08.2026)

```
MALZEME:  teslim kurgusu · 235,201 s · 1280×720 (!) · 30 fps · video 2,03 Mbit/s
          AAC 253 kbit/s 48 kHz stereo
MERCEK:   🔧 1_KARE · 🔗 2_DEVAMLILIK · 🔊 3_SES · 📖 4_HIKAYE · 🖼️ 5_ARKA_PLAN
          · ⚖️ 6_FIZIK (AYNI rubrik AYNI dosyaya İKİ KEZ — 2. koşu Ölçek 10→7 ve
          Işık 10→7'yi Issue gözü "none" ile düşürdü: kendi kural ④'üne aykırı,
          kaynaksız düşüş; işlemede 1. koşu esas alındı)
OTURUM:   🚨 ŞÜPHELİ [D110] — altı merceğin kesme listesi, şeridi ve sahne
          envanteri birebir aynı (film gerçekten 10 s ızgaralı olduğu için tek
          başına kanıt değil; şüphe kaydı düşüldü, parti düşürülmedi)
HAM:      ../02_HAM_RAPORLAR/THE_FROST_LINE_{KARE,DEVAMLILIK,SES,HIKAYE,
          ARKA_PLAN,FIZIK,FIZIK_2}_HAM.md
PLAN:     ../../../yatay_4_dk_filmler/THE_FROST_LINE/THE_FROST_LINE_PLAN.md
SPEC:     ✅ VAR — THE_FROST_LINE_QA_SPEC.md (A/B/C/E blokları) — ⛔ operatöre VERİLMEDİ
MÜZİK:    THE_FROST_LINE_MUZIK.md yazılı (29.08); kurgudaki sesin cue'larla
          ilişkisi kulakla doğrulanmadı (sahip dinler) — ölçüm yalnız "ses VAR" der
KARELER:  scratchpad/qa/t4…t234 (33 kare) + kose_SA.png (sağ alt köşe 12 örnek)
```

---

## ⭐ ⑪ ÖLÇÜM KAPISI — 1. PARTİ · master'dan okunan sayılar (rapor sayıları DEĞİL) [D125]

| Ölçüm | Değer | Raporlar ne dedi | Sonuç |
|---|---|---|---|
| Süre (container) | **235,201 s** | 6/6 "~235 ESTIMATED" | ✅ |
| Çözünürlük · fps | **1280×720 · 30 fps** · video 2,03 Mbit/s | ⑥ iki koşuda da "24 fps assumed" | ⑥'nın süreleri ×0,8 kayık · ⛔ **720p — ihraç kilidi ≥1440p** [KURGU_RITMI §6] |
| Ses kanalı | **VAR** — AAC 253 kbit/s · 48 kHz · 2 kanal | 6/6 "nothing audible to me" · ③ "absolute digital silence" + 4 🔴 | ⛔ **D137 · 4. vaka** — ölçüm satırı künyeye yapıştırılmadı; ③'ün raporu ölçümle GEÇERSİZ |
| Loudness | **−21,5 LUFS** · mean −25,3 dB · **tepe −0,1 dBFS** · LRA 21,0 | — | ⛔ ihraç kilidi −14 LUFS · ≤ −1,0 dBTP: **7,5 LU kısık, tepe sınırın üstünde** |
| silencedetect −50 dB / 0,3 s | **tek aralık: 230,11 → 235,22 (5,1 s) = kart** | ③ "0:00-3:55 mutlak sessizlik" | yatak 0-230 s **kesintisiz** ✅ [D83 delik yok] — ③'ün tek 🔴 ambiyans deliği iddiası da çürüdü |
| Kesme ızgarası | scene>0,3: 10,03 · 30,03…230,13 (10 s katları) + 235,13 · **20,03 yalnız eşik 0,10'da** | 6/6 aynı 23'lü liste | ✅ 23 sahne + 5 s kart · ⛔ **hook 10 s — 9'a KIRPILMAMIŞ** (SPEC: TRIM BUDGET 1 s) · benzer paletli S1→S2 kesmesi 0,3 eşiğinde görünmez (not) |
| Köşe şeridi (crop 360×240 sağ alt) | **camgöbeği "▷" 12/12 örnekte** | ① TOP-3'e yazdı · ⑤ her EDGES satırına yazdı | 🔴 **üretici filigranı 235/235 s** [D150 · 2. vaka] — Skylight'la AYNI "▷" ikonu; **D150'nin Thin Roof yamaları ① ve ⑤'te İŞLEDİ** ✅ (geçen ay altı mercek görmüyordu) |
| Kanıt kareleri | 33 kare + köşe şeridi | — | aşağıdaki ızgara tablosunun kanıtı |

> Rapor ile ölçüm çelişen her yerde ÖLÇÜM kazanır [D125]. Ses ekseni bu partide
> raporlardan değil yalnız ölçümden okunur [D137].

---

## ⛔ ④ KURGU KAPISI — 1. PARTİ · önce ayıkla, sonra say [D93 · D109 · D118 · D120]

```
SAHNE-DIŞI MALZEME:  230,11-235,22 · 5,1 s · KAPAK görseli + "THE FROST LINE" +
                     "A HIGHER PRESSURE / A DEEPER PURPOSE" tipografisi (t231)
                     → kurgunun SONUNDA · sayımın ve sürenin DIŞINDA · 🔴 loglandı
                     ⛔ kapak çıktısı kurguya EKLENMEZ [D34/D70/D72 — Skylight'tan
                     sonra zincirin bir sonraki vakası] · ekran metni kilidi 0,0 s'ydi

a) KLİP SAYISI   23                ≠ plan 25            ⛔  (−2 klip)
b) SÜRE          230,1 s (kartsız) ≠ plan 249 s         ⛔  (Δ −18,9 s = −2 klip −20 s
                                                            + kırpılmamış hook +1 s)
c) SIRA          şerit uzunluğu tutmuyor — aşağıda      ⛔
d) FİNAL VURUŞ   t222/t227 (S24 yuvası): gergin bölüm 2 ✓ · kar sütunu 0 ✓ ·
   [D141 · E6]   çökük bölüm VAR ama kırağılı film değil BRANDA/örtü olarak ⚠️ ·
                 FIRÇALI FİGÜR YOK — adam tünel ucunda koyu bir panel tutuyor ⛔
                 → E6 kanıtının 4 öğesinden 2'si tam: FİNAL TESLİM EDİLMEMİŞ
e) DORUK KANITI  t193 (T+3) ve t198 (T+8): kelepçe çubuğu iki elde HAVADA, perde
   [E7]          İNİK DEĞİL, zar şişmesi yok, son yeşilin beyazlaması yok →
                 E7-b FAIL: DORUK VURUŞU (mühür + bedel + ödeme) EKRANDA OKUNMUYOR
```

### 🧬 İNSAN ŞERİDİ — Δ okuması [D118 · D121]

```
PLAN (25)      1111111111111111111111111
6/6 RAPOR (23) 11111111111111111111111     23 yuva, hepsi insanlı — altı mercek aynı
ÖLÇÜM (23)     33 karenin hepsinde figür var ✓ şerit ekseni doğrulandı

Δ = 230 − 249 = −18,9 s → −2 klip (−20 s) + kırpılmamış hook (+1 s)
· insansız yuva yok → şerit eksiği YERİ söyleyemez; yer İÇERİK hizalamasından
  okundu (aşağıdaki ızgara tablosu, kare kanıtlı):
· EKSİK ①: **S12 (TOHUM KUTUSU — Çehov kurulumu)** — yuva 11 (t115/t118) kutusuz
  yürüyüş, yuva 12 (t121) zaten S13'ün perdesi; kutunun İLK görünüşü S22 ödemesi
  (t215) → kutu kurulumsuz kaldı, ② bunu "grey box/monitor" diye yazdı
· EKSİK ②: **S23 (BÜTÜN TÜNEL — S13 aynası, iç geniş)** — yuva 21 = S22 (t215),
  yuva 22 = S24 dış aynası (t222) → iç geniş ayna EKRANDA HİÇ YOK; kuyruk eksiği
  [D121 ③ kuyruğa önce bak — kuyruk filmin finalidir]
· Sahip beyanı "bir sahne eksik" ↔ ölçüm İKİ diyor. Raporların ESTIMATED süresi
  eksik sahne İLAN EDEMEZ (rubrik kuralı) — burada hüküm container süresi +
  ızgara + içerik hizalamasından, yani ölçümden [D125].
```

---

## 🧭 ⑨ HİZALAMA KAPISI — IZGARA GERİ ALMA [D115] (kare kanıtlı)

Izgara plandan: `9 + (n−1)×10`; üretimde hook kırpılmadığı için `10 + (yuva)×10`.
Raporların kendi sahne haritaları bu tabloyla DEĞİŞTİRİLİR (rapor "S7" derken
planın S6'sını kastediyor vb. — bütün rapor bulguları aşağıda plan numarasına
çevrilmiştir).

| Yuva | Zaman | Plan | Kanıt (kare) |
|:--:|---|:--:|---|
| 0 | 0:00-0:10 | S0 | t4: üs + gemi + tünel + jet kompozisyonu ✓ — ama jet KIVRIMLI DUMAN gibi ⛔ (kapı ① ölçütü "düz sütun, tek tek kristal"), süpürme jesti örnek karede yok ⚠️ |
| 1 | 0:10-0:20 | S1 | t14: yüz + fırça sağ elde ✓ · jet sağ omuz üstünde ✓ · önkollarda ERKEN kırağı ⛔ (PHASE 1 = yalnız bot) [D147] |
| 2 | 0:20-0:30 | S2 | t23: koşu, arkada ekran-solda üs+gemi ✓ · yön ⬜ (②④ "sağdan sola" yazdı; plan soldan sağa; kareden tek başına hüküm yok) |
| 3 | 0:30-0:40 | S3 | t34: önkol boyu yarık + jet + kırağı eteği + zeminde beyaz halka ✓ · jet EĞİK çift bıçak ⛔ (kapı ① "düz") · kristaller iri pul ⚠️ |
| 4 | 0:40-0:50 | S4 | t44/t46.5: **salt AVUÇ, yama YOK** ✓ — ①②'nin "0:40-0:50 yama basıyor" okuması DÜŞTÜ · film avucun altında esniyor ⚠️ (⑥ L3) |
| 5 | 0:50-1:00 | S5 | t51 yama basılı → **t56 YAMA HAVADA, jet geri çıkıyor** → t58 yama yok, iki avuç boş filmde ✓✓ — T+6, planın 5,6-6,0 formülüne oturuyor. **ALTI MERCEĞİN HİÇBİRİ GÖRMEDİ** → D151 |
| 6 | 1:00-1:10 | S6 | t63: bölüm 1 **TAMAMEN çökük** ⛔ (plan: iki kaburga arası BİR KARIŞ ilk sarkma) — raporların "dış çökük ↔ iç sağlam" çelişkisinin tek kaynağı bu klip |
| 7 | 1:10-1:20 | S7 | t75: kamera AIRLOCK KAPAĞINDA, adam kameraya koşuyor, jet arkada ayakta ✓✓ [UZAMSAL §6.8 V3 uygulanmış] |
| 8 | 1:20-1:30 | S8 | t82: bölüm 2 içi, fasulye solda, sarı rulo tepede ✓ · kırağı çiçeği (3 s'de bağlanma) örnek karede görünmüyor ⬜ |
| 9 | 1:30-1:39 | S9 | rapor: arkadan koridor yürüyüşü ✓ (kare çıkarılmadı) · rulo elde mi ⬜ |
| 10 | 1:39-1:50 | S10 | t107: bölüm 1 koridoru + tepede PEMBE yarık ✓ · yama basışı örnek karede yok; ① 1:47'de "el morfu (clap)" gördü ⬜ |
| 11 | 1:50-2:00 | S11 | t115/t118: kameraya YÜRÜYÜŞ — planın "yatak çerçevesinde tepki planı" duruşu yürüyüşe inmiş ⚠️ · **S12 imzası (raf/kutu/CU) YOK** |
| 12 | 2:00-2:10 | S13 | t121/t125: sarı perde/rulo baş üstünde, çekiyor ✓ → **S12 bu yuvada olmalıydı: EKSİK** |
| 13 | 2:10-2:20 | S14 | t134: perde ipiyle uğraşıyor ✓ · **SIRT ÜNİTESİ (beyaz çanta + kayışlar)** ⛔ [D139 · 2. vaka] · üst açı yerine göz hizası ⚠️ |
| 14 | 2:20-2:30 | S15 | **t141 yaprak YEŞİL → t147 aynı yaprak GRİLEŞMİŞ** ✓✓ klip içi beyazlama EKRANDA (E8 sınıfı kanıt) · eldiven DEĞMİYOR, boşluk görünür ✓ — ① "dokunuyor + fazla parmak" ⬜, ②④ "donuk yaprağa dokunuyor" diye okudu → D151 |
| 15 | 2:30-2:40 | S16 | t155: kol bölüm 1'e uzanmış, perde kenarı ipte ✓ · önkol kalın kırağı (PHASE 4) ✓ · **sırt DÜZ** ✓ (çanta yalnız yuva 13'te) |
| 16 | 2:40-2:50 | S17 | t165: ölen bölüm — çoğu asma beyaz, biri yeşil ✓ · üst açı yerine göz hizası ⚠️ |
| 17 | 2:50-3:00 | S18 | t175: perde/rulo elde, baş öne düşmüş ✓ (Kuleshov A' duruşu) |
| 18 | 3:00-3:10 | S19 | **t181 fasulye yaprağı YEŞİL → t187 aynı yaprak BEYAZ** ✓✓ "HER ŞEYİN KAYBI" EKRANDA — ④ bunu "Payoff: healthy leaf, rig worked" diye TERSİNE puanladı ve ③. viral sahneyi övdü sanarak yanlış nedenle korudu → D151 |
| 19 | 3:10-3:20 | S20 | t193/t198: çubuk iki elde havada, perde İNİK DEĞİL, zar şişmesi yok, beyazlanan asma yok ⛔ **DORUK VURUŞU TESLİM EDİLMEMİŞ** (E7-b FAIL) — ④'ün "stands there looking, CUT" okuması bu kez üretimle uyumlu ama reçetesi yine uygulanmaz [D129]: çözüm kesmek değil S20'yi yeniden üretmek |
| 20 | 3:20-3:30 | S21 | t204: kırağılı sağ eldivene bakış ✓ · cam ÇERÇEVESİ ve pane görünür ✓ · ②'nin "el yüze değiyor" iddiası bu karede yok ⬜ |
| 21 | 3:30-3:40 | S22 | t215: kutu elde, diz çökmüş, tohum jesti ✓ (kurulumu S12 ile birlikte kayıp) |
| 22 | 3:40-3:50 | S24 | t222/t227: üs + gemi + tünel S0 aynası ✓ · jet 0 ✓ · beyaz halka ✓ · çökük bölüm **BRANDA/örtü nesnesi olarak** üretilmiş ⚠️ · **FIRÇA YOK** — elde koyu panel ⛔ (E6 FAIL) → **S23 iç geniş ayna EKRANDA HİÇ YOK: EKSİK** |
| — | 3:50-3:55 | kart | t231: kapak görseli + başlık + tagline tipografisi 🔴 [D70/72] — metin kilidi 0,0 s'ydi |

---

## 🪪 ③ KİMLİK KAPISI — 1. PARTİ [D105] — ✅ GEÇTİ (5 çapa, gereken 2)

```
① VURUŞ    iç yama rulosu/bant + sarı sert perde tepede rulodan iner, yarıda
           takılır, ipten kurtarılır (plan S13-S16) — ②'nin S13-S16 satırları +
           t121/t134/t155 ✓
② SAYISAL  üs: beyaz yatay modüller + çanak antenli düğüm + güneş tarlası; gemi
           EKRAN-SOLDA ayrı pistte, 4 bacak (plan ÜS/GEMİ kilidi) — ⑤ envanteri
           S1/S23 + t4/t222 ✓
③ VURUŞ    tohum kutusu: diz çökmüş adam + avuç boyu mat kutu + tohum jesti
           (plan S22) — ② "grey box" + t215 ✓
④ SAYISAL  jet: beyaz sütun + film üstünde kırağı eteği + zeminde beyaz halka
           (plan JET kilidi) — t34 ✓
⑤ VURUŞ    doruk bölgesinde kelepçe ÇUBUĞU + sarı perde + iki bölüm (plan S20)
           — ④②⑤ "doorway bar" + t193 ✓
```
⛔ 3:52'deki başlık kartı ve ③'ün `FILM: THE FROST LINE` satırı çapa olarak
KULLANILMADI [D105] — o satır karttan/dosya adından okumadır, kanıt değildir.

---

## 🔁 ⑤ ÇAPRAZ SAYIM KAPISI — 1. PARTİ [D107 · D121 · D135]

```
KESME     ① 23 · ② 23 · ③ 23 · ④ 23 · ⑤ 23 · ⑥ 23 · ⑥' 23   fark 0 ✅
REPLİK    6/6 "none — nothing audible to me"   ✅ kendi içinde tutarlı — ama
          ölçüm: ses kanalı VAR, −21,5 LUFS [D137] → ses ekseni raporlardan okunmaz
ŞERİT     6/6 `11111111111111111111111` (23) ✅ birbirleriyle; plan 25 ile ⛔ (④ kurgu kapısı)
⑦ PARMAK İZİ  önceki koşu THE SKYLIGHT (315 s · 31 seg · kart 5:10) ↔ bu parti
          (235 s · 23 seg · kart 3:50) → şüphe YOK ✅
⚠️ D110   altı merceğin kesme listesi/şerit/severity dağılımı birebir; iki ⑥
          koşusu aynı ledger'ı taşıyor → bağımsızlık ŞÜPHELİ; parti düşürülmedi
          (film gerçekten sabit ızgaralı), şüphe kayda geçti
```

---

## 📓 ② KİLİT ÇELİŞKİSİ DEFTERİ — 1. PARTİ [D96] — rapor bulgusu × kilit × KARE

| # | rapor ne dedi (timecode) | hangi kilit | kanıt | sonuç |
|:--:|---|---|---|---|
| 1 | ①⑥ 🔴 0:03 "gaz, tuz gibi dümdüz düşüyor; yatay dağılmalıydı" | C JET: kristal jeti (gaz görünümü ihlal), kristal düz iner, 3 s'de yerde, 0,38 g | t4 (S0 jeti kıvrımlı duman ⛔) · t34 (eğik çift bıçak, iri pul) · ⑥ ölçümü 11,1 m/s² | ⚠️ **YARI** — "gaz gibi dağılmalı" beklentisi TASARIM DIŞI (⑩ düşer; novum kristal jet); ama S0 jetinin duman okunması + kristal düşüşünün 0,38 g'yi katbekat aşması **FİLM SAPTI** → D154 |
| 2 | ① 🔴 0:41-0:49 el-yüzey füzyonu, "yama basarken" | S4 = salt avuç; yama yalnız S5 | t44/t46.5: yama YOK, parmaklar bütün, film avuç altında esniyor | ⚠️ **YARI** — "yama" kısmı RAPOR YANILDI; füzyon iddiası ⬜ (kare aralığı izlenir); esneme ⑥ L3 ile birleşik → yumuşak film TASARIM sınırında |
| 3 | ②④⑤⑥ 🔴 1:00↔1:20 "dış tamamen çökük ↔ iç sapasağlam" | SARKMA sayacı: S6 = iki kaburga arası BİR KARIŞ | t63 (bölüm tam çökük) ↔ t107/t115 (iç dimdik) | 🔴 **FİLM SAPTI** — S6 erken TAM çöküş; çelişki tek klibin abartısından. ④'ün "S6'yı (rapor dilinde S7) kes" reçetesi UYGULANMAZ [D129]: S6 sayaç ①'in 1. adımı, çözüm yeniden üretim |
| 4 | ② 🔴 0:10↔0:20 kırağı sıfırlanıyor; 3:10↔3:20 yine | KİR MERDİVENİ [D147]: PHASE 1 S0-S1 yalnız bot → PHASE 4 | t14 (S1'de önkolda ERKEN kırağı) ↔ t23 (temiz) ↔ t193 (hafif) ↔ t204 (yoğun) | 🔴 **FİLM SAPTI — İKİ YÖNDE** [D147 · 2. vaka]: faz satırı 50/50 promptta yazılıyken kırağı hem erken geldi hem dalgalandı |
| 5 | ② 🟠 2:10 sırt çantası doğdu, 2:40'ta yok | D79/D139: düz sırt, 25/25 | t134 (beyaz sırt ünitesi + kayışlar) ↔ t155 (sırt DÜZ) | 🔴 **FİLM SAPTI** [D139 · 2. vaka] — "flat back" beyanı her promptta vardı; kamera arkayı gören sahnede yine doldu; D139'un POZİTİF YÜZEY TARİFİ kapısı bu filmde yazım sırasında koşulmamış |
| 6 | ② 🟠 fırça 0:10→0:20 kayboluyor | FIRÇA kilidi: S1'de düşer (kadraj dışı), S24'te geri | plan | ✅ **TASARIM** — kayboluş planlı; asıl ihlal S24'te fırçanın GERİ GELMEMESİ (satır 12) |
| 7 | ② 🟠 bant/rulo 1:20→1:30 kayboluyor | plan: S8 alır, S9 arkadan yürüyüş | — | ⬜ **AÇIK** — S9'da rulo elde mi, master 1:30-1:39 izlenir (~10 s) |
| 8 | ② 🟠 0:40 küçük gri yama ↔ 0:50 dev şerit | S4 avuç · S5 yama | t44 (yama yok) · t51 (40×40 kare) | ✅ **RAPOR YANILDI** — S4'te yama hiç yok; "iki farklı yama" tek yamadır |
| 9 | ②⑤ 🟠 üs mimarisi S0↔S24 kayıyor | ÜS/GEMİ: 25/25 aynı yerleşim | t4 ↔ t222: sınıf aynı (gemi solda · çanaklı düğüm · panel tarlası), modül dizilimi/sayısı ve panel yerleşimi farklı | ⚠️ **YARI — FİLM SAPTI (düşük şiddet)**: raporun "tamamen değişti"si abartı, ama iki uç aynı metinden farklı mimari üretti → D153 |
| 10 | ④ S19 = "Payoff: healthy leaf" · KEEP "rig worked" | S19 = VİRAL #3 · HER ŞEYİN KAYBI: yaprak klip içinde BEYAZLAR | **t181 yeşil → t187 beyaz** | 🔴 **RAPOR TERSİNE OKUDU** — vuruş ekranda; mod V merceği 10 s'lik klibin başından örnekleyip duygusal yönü ters çevirdi → D151 |
| 11 | ⑤ 🟡 "S7'de (yuva 7) plume duruyor — yama başarılıydı, hata" | YAMA kilidi: dıştan yama TUTMAZ, 1 s'de uçar | **t56: yama havada** | ✅ **RAPOR YANILDI** — uçuş ekranda, plume'un sürmesi tasarımın kendisi |
| 12 | d) FİNAL: ②④⑤⑥ "dev branda çekiyor" | S24: fırça + süpürme + kırağılı çökük film; branda diye bir nesne YOK | t222/t227 | 🔴 **FİLM SAPTI** — çökmüş yarı saydam film "örtü/branda" nesnesine dönüşmüş, fırça jesti panele dönüşmüş; E6 FAIL → D152 · D153 |
| 13 | ③ 4×🔴 "mutlak dijital sessizlik / ambiyans deliği 0:00-3:55" | E2/E3 + ölçüm | ffprobe: ses VAR · silencedetect: tek aralık = kart | 🔴 **RAPOR ÖLÇÜMLE ÇÜRÜDÜ** [D137 · 4. vaka] — ③'ün skoru ve 4 🔴'ı geçersiz; ses ekseni ölçülmemiş sayılır, koşu miks sonrası TEKRARLANIR |
| 14 | ①⑥ 🟠 0:21/1:11 süzülen "ay yürüyüşü" koşu | D44: 0,38 g GERÇEK ZAMANLI, süzülme 0 | ⑥'nın kendi ölçümü g≈4,0 m/s² (adım) · ① iki sahnede | 🔴 **FİLM SAPTI** — koşu klipleri D44 kilidine rağmen süzüldü → D154 (kadans sayısı) |
| 15 | ① 🟠 0:30-0:39 jet üstünde bloom | %0 bloom kilidi | t34: jet parlak ama dokulu | ⬜ **AÇIK** — video izlenir; kare tek başına hüküm vermez |
| 16 | ① 🔴 1:47 "clap" el morfu | S10 iç yama basışı | ② de aynı saniyeyi gördü | ⬜ **AÇIK** — kare aralığı (10 fps şerit) çıkarılmadı |
| 17 | ② 🟠 0:30 sol el ↔ 0:40 sağ el | S3/S4: sağ eldiven | t34'te sağ el yukarıda görünüyor | ⬜ **AÇIK** — S3 içi izlenir |
| 18 | ② 🟠 "S21'de eldiven yüze DEĞİYOR / vizör hâli düzensiz" | KASK: 25/25 kapalı, tek düz cam, görünür çerçeve [D146] · ⛔ C kilidi "YANSIMASIZ" da diyor | t204: çerçeve + cam okunur, el kaskın önünde · t134/t115: cam okunamıyor | ⚠️ **YARI** [D95 · 2. vaka] — "yansımasız berrak" kilidi kendi kanıtını yine sildi; değme iddiası karede yok ⬜ |

**Kapalı:** 13 (1-6 · 8-14 · 18 yarıları dahil) · **Açık:** 5 (7 · 15 · 16 · 17 + 2'nin füzyon yarısı).
⛔ Açık maddeler skorsuz kalır; **dersler yalnız KAPALI satırlardan ve ölçümden yazıldı.**

---

## 🔴 ÖLÇÜMÜN VE KARENİN SÖYLEDİĞİ, RAPORLARIN SÖYLEMEDİĞİ

| # | İhlal / gerçek | Kanıt | Kilit |
|:--:|---|---|---|
| 1 | **2 sahne eksik** (S12 · S23) + Çehov kutusu kurulumsuz | Δ −18,9 s · ızgara tablosu · t115/t121/t215/t222 | kurgu kapısı a/b · D100 sınıfı |
| 2 | **Ses kanalı VAR, yatak kesintisiz** — 6/6 mercek kör | AAC 253 kbit/s · −21,5 LUFS · silencedetect tek aralık=kart | D136/D137 · 4. vaka |
| 3 | **S5 yama uçuşu EKRANDA** (novumun gerçekçilik kanıtı) | t56 | ⑤ tersini "hata" diye yazmıştı → D151 |
| 4 | **S15 + S19 klip içi beyazlama EKRANDA** (E8 sınıfı kanıt) | t141→t147 · t181→t187 | ④ S19'u tersine okudu → D151 |
| 5 | **S20 doruk vuruşu EKRANDA YOK** (E7-b) | t193/t198 | plan CENTRAL CHOICE — yeniden üretim listesi 1. sıra |
| 6 | **Hook kırpılmamış** (S0 10 s) | kesme 10,03 | SPEC TRIM BUDGET 1 s — Skylight'la aynı |
| 7 | **720p · −21,5 LUFS · tepe −0,1 dBFS** | ffprobe · ebur128 | ihraç kilidi ≥1440p · −14 · ≤−1,0 [KURGU_RITMI §6] |
| 8 | **Kapak kartı kurguda** (5,1 s, tipografili) | t231 | D34/D70/D72 zinciri · SCREEN TEXT 0,0 |
| 9 | Üretim kapıları YAZILIYDI, SONUÇ satırları ⬜×5 — koşulmadan 23 klip üretilmiş; kapı ① (S3 jet) ve ④ (S20) RET verirdi | PLAN "ÜRETİM KAPI SIRASI" + PART_B "KAPI KAYITLARI (boş)" | D144 · 2. vaka / D74 |
| 10 | S1→S2 kesmesi scene>0,3'te görünmez (benzer palet) — ızgara ikamesi gerekmedi ama eşik notu | 20,03 yalnız 0,10'da | ⑪ ikame satırı |

## ✅ RAPORLARIN DOĞRU YAKALADIĞI (kareyle onaylanan)

```
filigran ▷ (① TOP-3 + ⑤ her satırda — D150 Thin Roof yamaları İŞLEDİ) ·
sırt ünitesi yuva 13 (②) · kırağı dalgalanması (②) · S6 erken çöküş çelişkisi
(dört mercek) · iki yerçekimi (⑥ — g≈4,0 adım ölçümü planın 0,38 g'sini
DOĞRULADI; sapan kristal) · kart NON-SCENE ayrımı (6/6) · süzülen koşu (①⑥)
```

---

## 🔍 ⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME — 1. PARTİ [D108]

| gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
|---|---|---|---|
| dış çökük ↔ iç sağlam (1:00↔1:20) | ② 🔴 cat11 · ④ CUT · ⑤ flag · ⑥ L4 | ② | ② — ama satır tabloya girmiyor [D129]; üretim kararı: S6 yeniden |
| filigran (0:00-3:50) | ① 🔴 · ⑤ 🔴 cat9 | ① (kare) | teslim kusuru — puan değil [D150] |
| kırağı sıfırlanması | ② 🔴 cat3 · ① envanter | ② | ② [D147] |
| "tuz gibi jet" (0:03) | ① 🔴 · ⑥ L1 | ⑥ (sayı taşıyor) | ⑥ — ①'e işaretçi; yarısı ⑩'da düştü |
| "branda" finali (3:40) | ②④⑤⑥ | ② (dünya propu) | tabloya girmez; üretim kararı: S24 yeniden |
| el morfu 1:47 | ① 🔴 · ② flag | ① | ⬜ açık |

---

## 🧮 ⑩ ÖNERME KAPISI — 1. PARTİ [D87 · D116 · D130] — bilgi amaçlı; tabloya satır girmiyor [D129]

```
DÜŞEN bulgular (kaynağı planda/SPEC'te yazılı):
  "gaz yatay dağılmalıydı" (novum: KRİSTAL jeti — ①'in DERS ADAYI ve "horizontal
  dispersion, zero solid particles" reçetesi REDDEDİLDİ: uygulanırsa filmin
  novumu silinir) · "S8'de plume hatası" (dıştan yama TUTMAZ — t56) · fırça
  S1'de kaybolur (planlı düşüş) · "iki dünya / perde bölünmesi" (tema motifi) ·
  koşunun kendisi 0,38 g'de (⑥'nın g tahmini planı doğruladı; sapan SÜZÜLME) ·
  "sessiz film mi" soruları (film sesli tasarlandı ve ses VAR — soru ölçümle
  kapandı)
5b REÇETE GREP'İ [D85]: ①'in REMOVE önerisi "watermark, logo, signature" —
  dize film dosyalarında YALNIZ NEGATİF yasağın içinde ("no watermark") →
  reçete DÜŞER (çalışan yasağı silme önerisi; filigran üretici filigranıdır,
  prompt meselesi değil [D150])
AYAKTA kalanlar (üretim kararı ister): S6 erken çöküş · kırağı dalgalanması ·
  sırt ünitesi (yuva 13) · S0 duman-jet + S3 eğik jet · süzülen koşu ·
  S20 doruk yokluğu · S24 branda/fırçasızlık · üs ayrıntı kayması ·
  kırpılmamış hook · kart · filigran · 720p/−21,5 LUFS ihracı
④ HİKAYE kesme listesi (S6 · S9 · S11 · S20 rapor dilinde S7/S10/S12/S20):
  UYGULANMAZ [D129] — S6 sayaç ① adım 1 · S20 DORUK (rapor doruğu keserdi
  çünkü doruk üretimde yok — hastalığı değil belirtiyi kesiyor) · S19'u
  "payoff" sanıp koruması doğru sonuç yanlış gerekçe
```

---

## ⭐ ④ HİKAYE MERCEĞİ — ne doğru gördü, ne göremedi (mod V okuması = ilk izleyici)

```
GÖRDÜ    · "patch a leak + rig thermal insulation" — İZLEYİCİ OKUMASI BU:
           budama/kimlik hikâyesi ekrana "yalıtım rigging'i" olarak geçiyor;
           S20 vuruşsuz kalınca "en eski bitkileri feda etti" cümlesi kayboldu
         · S6 erken çöküşünün seyirci kaybettireceği doğru (1:00 drop-off)
         · yürüyüş yuvaları (S9/S11) gerçekten yük taşımıyor — S11'in tepki
           planı üretimde yürüyüşe indiği için (kare t115)
GÖREMEDİ · S19'un yön değişimi (yeşil→beyaz EKRANDA) — tersine okudu
         · S15'in klip içi beyazlaması (novum doğrulama) — "donuk yaprak" dedi
         · yama uçuşu (S5 T+6)
AÇIK     ⬜ "iki dünya" bölünmüş kadraj motifi ilk izleyiciye geçiyor mu —
           tek mod-V okuma veri değil; mod D + yayın verisi bekler
```

---

## 📊 SKOR SATIRLARI — 1. PARTİ

```
T1-T6: SATIR YOK [D129]. Raporların kendi toplamları (referans, ölçüm değil):
  ① 5,4 · ② 6,8 · ③ 1,0 (ÖLÇÜMLE GEÇERSİZ [D137]) · ④ 5,7Ⓥ · ⑤ 7,6 ·
  ⑥ 5,6 / ⑥' 4,8 (2. koşu kaynaksız düşüşlü — esas 1. koşu)
Tamlık matrisi: 0/4 KALIR.
```

---

## ✅ BİR SONRAKİ KOŞU İÇİN — sırayla (sahip)

```
1. EKSİK + BOZUK KLİPLER (üretim; kapı kayıtları bu kez DOLDURULUR [D144]):
   □ S12 (tohum kutusu — Çehov kurulumu) ve S23 (iç geniş ayna) ÜRETİLİR
   □ S20 yeniden: kelepçe ÇARPILIR + zar şişer + son yeşil beyazlar + tavan
     gerilir AYNI klipte (E7 a/b kareleriyle kabul) — filmin doruğu şu an yok
   □ S24 yeniden: fırça elde, süpürme jesti, çökük bölüm KIRAĞILI FİLM
     (branda değil) — S0'ın onaylı karesi imaj tabanı yapılır [D153]
   □ S6 yeniden: BİR KARIŞ sarkma, çöküş yok · S0 yeniden: jet DÜZ sütun
     (duman değil) + süpürme; S5'in onaylı jet karesi referans [D154]
   □ S2 yön kontrolü (izle) · yuva 13 (S14) sırt ünitesi [D139 pozitif tarif]
   □ kırağı fazları: PHASE satırı + imaj çapası [D147 eki]
2. MASTER YENİDEN İHRAÇ:
   □ filigransız kaynak ("▷" 235/235) · kart YOK · hook S0 10→9 s
   □ ≥1440p (şu an 720p!) · −14 LUFS integrated (şu an −21,5) · tepe ≤ −1,0 dBTP
   □ MUZIK cue'ları serildi mi + üç sessizlik penceresi — kulakla (ses VAR ama
     içeriği ölçülmedi)
3. AÇIK MADDELER (~1 dk izleme): S9 rulo · 1:47 morf · 0:30-0:39 bloom ·
   S3 el · S2 yön · S21 değme
4. MOD D KOŞUSU: ①'e A+B, ④'e A, ⑤'e C'nin üç kilidi, ⑥'ya C'nin sayısal
   kilitleri; ⑪ satırı KÜNYEYE: "SES KANALI: VAR · −x LUFS · tepe −y dBTP"
   [D137]; her mercek TEMİZ oturumda [D110]; ⑥ TEK koşu
```

---

## 📚 BU KAYITTAN ÇIKAN DERSLER

```
YENİ   D151 üç novum vuruşu ekrandaydı, mercekler görmedi/ters okudu — kapı
       sahnelerinin a/b kare çifti ⑪'de zorunlu; karesiz "olay yok/ters"
       hükmü işlenmez (08_QA)
       D152 eldeki alet klip içinde buharlaşıyor, yüklü jest nötr duruşa
       iniyor — fırça 2/2, kelepçe çarpışı 0/1 (05_EKIPMAN)
       D153 eş kadraj çifti aynı metinle aynı seti üretmiyor — S24 üs ayrıntısı
       kaydı, çökük film brandaya dönüştü; ayna sahnesinin imajı kaynak
       sahnenin ONAYLI karesinden türetilir (05_EKIPMAN)
       D154 tekrarlayan doğa olayı bir VARLIKTIR — dört klip dört jet biçimi,
       iki yerçekimi; ilk onaylı kare sonraki sahnelere imaj referansı +
       kapı ölçütü her jet sahnesine (03_FIZIK)
TEKRAR D129 (9. film) · D137 (4. vaka — bu kez ses TAM VARDI) · D95 (2. vaka,
       "yansımasız" kilidi) · D139 (2. vaka, kareyle) · D147 (2. vaka, iki
       yönde) · D150 (2. vaka — ama ① ve ⑤ yamalar sayesinde GÖRDÜ ✅) ·
       D144/D74 (kapılar yazılı, SONUÇ ⬜×5) · D70/72 (kapak kartı) ·
       D44 (süzülen koşu)
```

---
---

# ⚡ 2. PARTİ — 01.09.2026 · altı mercek, altısı YİNE mod V

## 📦 MALZEME VE HAM DOSYALAR — 2. PARTİ

```
MALZEME:  aynı kurgu · 235,201 s · 23 klip + 5,1 s kart · 30 fps
          ⭐ bu kez İKİ ihracı var: 720p (1. partininki) ve YENİ 4K
             (`the frost lıne (2).mp4` · 3840×2160 · 13,8 Mbit/s)
MERCEK:   🔧 ① · 🔗 ② · 🔊 ③ · 📖 ④ · 🖼️ ⑤ · ⚖️ ⑥  (her biri bir koşu)
OTURUM:   🚨 KOPYA [D110 · yeni kanıt biçimi] — ④ ⑤ ⑥'nın OUT-OF-SCOPE
          satırları ①'in bulgusunu BİREBİR AYNI CÜMLEYLE taşıyor
          ("3:23 fingers phase through the glass visor → FRAME lens").
          Üç merceğin kapsamı o bulguyu dışlar; üçü de aynı saniyeyi aynı
          kelimelerle yazamaz. Kanıt: bulgu YANLIŞ ve yanlışıyla kopyalandı.
HAM:      ../02_HAM_RAPORLAR/THE_FROST_LINE_{KARE_2,DEVAMLILIK_2,SES_2,
          HIKAYE_2,ARKA_PLAN_2,FIZIK_3}_HAM.md
SPEC:     ✅ VAR — ⛔ operatöre YİNE VERİLMEDİ (2. kez)
KARELER:  scratchpad/qa2/ — kose_A · kose_B · kimlik_5dosya · ev_sirt
          (t52·t57) · ev_filiz (t164·t217·t219) · ev_head (t202·t203·t204)
          · a_t104 · B_sheet1 · B_sheet2
```

---

## ⭐ ⑪ ÖLÇÜM KAPISI — 2. PARTİ [D125] · **master yolu VERİLMEDİ, ölçümle bulundu**

Sahip master yolu vermedi. `~/Downloads` içinde **"the frost lıne" adlı beş
dosya** duruyor; hepsi ölçüldü ve içerik karesiyle kimliklendirildi.

| dosya | süre | çözünürlük | t105 karesi = hangi film | hüküm |
|---|---|---|---|---|
| `the frost lıne.mp4` | 235,201 s | 1280×720 | sera tüneli, domates | ✅ **THE FROST LINE** (1. partinin master'ı) |
| `the frost lıne (1).mp4` | 235,201 s | 1280×720 | sera tüneli, domates | ✅ aynı kurgunun ikinci indirmesi |
| `the frost lıne (2).mp4` | 235,201 s | **3840×2160** | sera tüneli, domates | ✅ **aynı kurgunun 4K ihracı — bu partinin master'ı** |
| `the frost lıne .mp4` | **245,120 s** | 1280×720 | **toz fırtınası · kasa dizisi · kalkış · hibernasyon · kenetlenme** | 🔴 **BU FİLM DEĞİL** |
| `the frost lıne  (1).mp4` | **245,120 s** | 3840×2160 | aynı yabancı gövde | 🔴 **BU FİLM DEĞİL** |

```
⛔ 245,120 s'lik ÇİFT: gövdesi başka bir filmin (24 yuva × 10 s + 5 s kart;
   kasaları toza dik dizen adam · toz duvarı · dikey iniş aracı · ranza ·
   yörünge · kenetlenme), ama sonuna THE FROST LINE KAPAK KARTI eklenmiş
   ve THE FROST LINE adıyla ihraç edilmiş. Künye THE PAYLOAD'a oturuyor
   (plan: 24 sahne · 239 s · "BİRİNCİ KASA — kasayı toza DİK diker";
   D155'in kaynağı olan göğüsteki "PHASE 1" dizgesi de bu gövdede).
   → Bu dosyalardan birine QA koşulursa parti THE FROST LINE adına
     kaydedilir ve iki filmin kaydı birden zehirlenir. → D160
```

### Bu partinin master'ı (4K ihraç) — okunan sayılar

| Ölçüm | Değer | 1. partiye göre | Sonuç |
|---|---|---|---|
| Süre | **235,201 s** · 23 klip + 5,1 s kart | aynı | kurgu DEĞİŞMEDİ |
| Çözünürlük · fps | **3840×2160 · 30 fps** · 13,8 Mbit/s | 720p → **4K** | ✅ **ihraç kilidi ≥1440p KARŞILANDI** — 1. partinin 720p kusuru düzeldi |
| Ses kanalı | **VAR** — AAC 253 kbit/s · 48 kHz | aynı | ③ bu kez DUYDU (AUDIO STATE B) ✅ |
| Loudness | **−21,2 LUFS** · **tepe −0,1 dBFS** · LRA 15,8 | −21,5 / −0,1 / LRA 21,0 | ⛔ ihraç kilidi −14 LUFS · ≤−1,0 dBTP: **7,2 LU kısık, tepe sınırın üstünde** — DÜZELMEDİ |
| silencedetect | 4K'da **hiç aralık yok** · 720p'de tek aralık 230,11-235,22 (kart) | 720p ile aynı | yatak kesintisiz ✅ [D83] |
| Kesme ızgarası | 10,03 · 20,03 … 230,13 (10 s katları) | aynı | ⛔ **hook 10 s — 9'a YİNE KIRPILMAMIŞ** |
| Köşe şeridi (sağ alt) | camgöbeği **"▷" 12/12 örnekte · 4K'da da** | aynı | 🔴 **üretici filigranı DÜZELMEDİ** [D150 · 3. vaka] |
| Kart | 230,13-235,20 · kapak görseli + başlık + tagline (t242 eşdeğeri) | aynı | 🔴 **kart DÜZELMEDİ** [D70/72] · ekran metni kilidi 0,0 s |

> **İki ihraç kusurundan biri düzeldi (720p → 4K), üçü durmakta:
> filigran · kapak kartı · −21 LUFS/tepe.** Kurgunun kendisine
> dokunulmamış: 23 klip, S12 ve S23 hâlâ yok, hook hâlâ kırpılmamış.

---

## 🪪 ③ KİMLİK KAPISI — 2. PARTİ [D105] — ✅ GEÇTİ (5 çapa, gereken 2)

```
① VURUŞ    sarı sert perde tepede ruloda; indirilir, ipe takılır, bağlanır
           (plan S13-S16) — ②④⑤ 1:59/2:09/2:30/2:49 satırları ✓
② SAYISAL  tünel bölüm 1'de "bir düzine eski koyu kare yama" (plan TÜNEL) —
           t52/t57 karesinde sayılabilir hâlde ✓
③ VURUŞ    diz çökmüş adam + avuç boyu mat kutu + tohum jesti (plan S22) —
           ② "kneeling and planting in soil bed" + t217/t219 ✓
④ SAYISAL  üs: beyaz yatay modüller + çanak antenli düğüm + güneş tarlası;
           gemi EKRAN-SOLDA ayrı pistte (plan ÜS/GEMİ) — ⑤ envanteri S1/S23 ✓
⑤ VURUŞ    doruk bölgesinde kelepçe ÇUBUĞU + kapı çerçevesi (plan S20) —
           ①②④⑤⑥ 3:10-3:20 ✓
```
⛔ 3:50'deki başlık kartı ve ②/③'ün `FILM: The Frost Line` satırı çapa olarak
KULLANILMADI [D105] — bu partide o satırın ne kadar tehlikeli olduğu ölçümle
görüldü: **aynı kart başka bir filmin kuyruğunda da duruyor.**

---

## ⛔ ④ KURGU KAPISI — 2. PARTİ

Kurgu 1. partiden beri değişmedi; kapı aynı sonucu veriyor ve tekrar edilmez.

```
a) KLİP SAYISI   23 ≠ plan 25    ⛔   (S12 tohum kutusu · S23 iç geniş ayna yok)
b) SÜRE          230,1 s ≠ 249 s ⛔   (Δ −18,9 s)
c) SIRA          23 ≠ 25         ⛔
d) FİNAL VURUŞ   E6: 4 öğeden 2'si — FIRÇA YOK, çökük film "branda" ⛔
e) DORUK         E7-b FAIL — S20 vuruşu ekranda yok ⛔

→ KOŞU **ÖN KOŞU**'dur. Film boyuna bakan kategoriler SAYI TAŞIMAZ:
  Yapı · Duygu Yayı · Final · Tutundurma · Ortam Devamlılığı · Kimlik Sürekliliği
```

### 🧭 ⑨ HİZALAMA — raporların sahne numarası → PLAN numarası

Raporlar S1'den başlıyor, plan S0'dan. Eksik S12 yüzünden eşleme ortada bir
kayıyor. **Bu partideki her rapor bulgusu aşağıdaki tabloyla çevrilmiştir:**

```
rapor S1..S12  →  plan S0..S11        (rapor Sn = plan S(n−1))
rapor S13..S22 →  plan S13..S22       (rapor Sn = plan S(n) — S12 eksik olduğu için hiza döndü)
rapor S23      →  plan S24            (S23 iç geniş ayna hiç üretilmemiş)
```

---

## 🔁 ⑤ ÇAPRAZ SAYIM KAPISI — 2. PARTİ [D107 · D121 · D135]

```
KESME     ① 21 · ② 22 · ③ 22 · ④ 22 · ⑤ 22 · ⑥ 22        fark 1 → ✅ işlenir
          ⛔ ÖLÇÜM 22 der. ① 1:39 ve 3:30 kesmelerini atladı → ①'in sayısı 🚨
ŞERİT     ① `1111111111111111111111` (22)  ← 🚨
          ② ④ ⑤ ⑥ `11111111111111111111111` (23) · ③'te şerit satırı yok (rubrik)
          ⛔ D135 gereği önce ①'in KENDİ envanteriyle karşılaştırıldı:
             ① 21 kesme → 22 sahne → 22 karakter. Kendi içinde TUTARLI;
             hata sayımda, şeritte değil. Parti düşmedi, ①'in ekseni 🚨.
REPLİK    ① ② ③ ④ ⑥ "none — room tone present" · 6/6 tutarlı ✅
          ⭐ VE ÖLÇÜMLE DE TUTARLI: ses kanalı VAR, yatak kesintisiz.
             1. partide bu satır 6/6 "nothing audible" idi ve ölçüm çürütmüştü.
             ⛔ Ama ⑪ satırı künyeye yapıştırılmadı → D137 gereği ses ekseni
                bu koşuda da ÖLÇÜLMEMİŞ sayılır (SPEC'in kendi uyarısı).
⑦ PARMAK İZİ  Aynı rubriğin son iki koşusu AYNI DOSYAYA koşuldu (235 s · 23 seg
          · kart 3:50) → künyelerin birebir aynı olması beklenendir; kapı bu
          partide AYIRT EDİCİ DEĞİL. Yerine D110 koşuldu (aşağıda).
🚨 D110   ⛔ YENİ VE DAHA SERT KANIT: sayılar değil BULGU METNİ kopyalanmış.
          ④ ⑤ ⑥ OUT-OF-SCOPE satırlarında ①'in 3:23 bulgusu birebir duruyor.
          Üçünün de kapsamı o bulguyu dışlar, üçü de aynı saniyeyi aynı
          kelimelerle bulamaz — ve bulgu KAREYLE YANLIŞ çıktı. → D159
```

---

## 📓 ② KİLİT ÇELİŞKİSİ DEFTERİ — 2. PARTİ [D96] · rapor × kilit × KARE

| # | rapor ne dedi (timecode · mercek) | hangi kilit | kanıt | sonuç |
|:--:|---|---|---|---|
| 1 | ①④⑤⑥ 🔴 `3:23 parmaklar vizörden geçiyor` | KASK: tek düz cam + görünür koyu çerçeve [D146]; TEMA S21 "el kask kenarına" | **t202/t203/t204 (4K kafa kırpması)**: el vizörün ÖNÜNDE, çerçeve ve pane kenarı okunur, füzyon yok | ✅ **RAPOR YANILDI** — ve yanlış dört mercekte kopyalandı → **D159**. ①'in REGENERATE'ini taşıyan dört 🔴'dan biri düştü |
| 2 | ② 🟠 `0:50 kalın siyah sırt harness'ı beliriyor` (rapor S6 = plan S5) | KASK: "sırt ünitesi YOK, sırt silueti DÜZ" [D79] | **t52 · t57**: omuz üstünden geçen siyah kayış iki karede de net | 🔴 **FİLM SAPTI** [D139 · **3. vaka**] — 1. partide yuva 13'teydi, şimdi yuva 5'te de var: iki ayrı yuva |
| 3 | ② 🟠 `2:40 kırağılı yapraklar ↔ 3:30 toprakta taze yeşil filizler` | YEŞİL SIRA: "S22 yeni tohum … **filiz 0 kare**" | **t164** (S17 tünel kırağılı) ↔ **t217/t219** (S22'de tohum HÂLÂ ELDE ve önündeki yatakta çimlenmiş bir SIRA duruyor) | 🔴 **FİLM SAPTI** — ödemenin kanıtı ödeme jestinden ÖNCE ekranda; "sıfır" kilidi yine kimse aramadı → **D156 · 2. vaka** |
| 4 | ① 🟠 `0:00 jet tuz gibi düz iniyor, gaz gibi dağılmıyor` · ⑥ L2 | C JET: kristal jeti, "kristaller düz iner, 3 s'de yerde", "duman/buhar okunuşu 0" | plan | ⚠️ **DÜŞER** ⑩ — beklenti tasarım ihlali (novum kristal jet). 1. partide de düşmüştü |
| 5 | ①⑥ `sera yatak çarşafı gibi çöküyor` (1:00 · rapor S7 = plan S6) | SARKMA sayacı: S6 = iki kaburga arası BİR KARIŞ | 1. parti t63 (bölüm tam çökük) | 🔴 **FİLM SAPTI** — 1. partinin 3. maddesiyle aynı; iki parti bağımsız olarak aynı klibi işaret etti ✅ |
| 6 | ② 🟠 `0:39 kızıl tozlu ↔ 1:50 tertemiz` · `3:20 kırağılı eldiven ↔ 3:30 temiz` | KİR MERDİVENİ [D147]: "Toz azalmaz, kırağı silinmez", PHASE 1-4 | 1. parti t14/t23/t193/t204 | 🔴 **FİLM SAPTI — İKİ YÖNDE** [D147 · **3. vaka**] |
| 7 | ②⑥ 🟠 `gölge yönü 0:00 ↔ 3:39 arasında 180° dönüyor` | IŞIK TAKVİMİ: "güneş ekran-sol-arkada, gölgeler ekran-sağa … MONOTONİK" | ⑥'nın L7/L8 satırı (cetvel yok) | 🔴 **FİLM SAPTI** — kilit açık ve tek yönlü; sahibi ② (sahneler arası eşleşme), ⑥'ya işaretçi |
| 8 | ⑤ envanteri: `S11 ve S17 tavanında PEMBE LED yetiştirme şeridi` | IŞIK TAKVİMİ: "**yapay lamba/LED 0 kare**" | **a_t104** (1:44 · plan S10): tavan kaburgasında pembe şerit net | 🔴 **FİLM SAPTI — YENİ.** ⑤ bunu envantere yazdı ama bulgu yapamadı (belgesiz mercek). Mod D görürdü → ⑩'un tersi: **belge OLSAYDI puan düşerdi** |
| 9 | ⑤ 🟠 `üs mimarisi S1 ↔ S23 kayıyor` · COUNT LOG "3 pod → 2 pod + çanak" | ÜS: **4** beyaz yatay modül + çanak antenli düğüm, 25/25 aynı | ⑤ envanteri + 1. parti t4/t222 | ⚠️ **YARI — FİLM SAPTI**: iki uç birbirinden de, kilitten de sapıyor (3 ve 2 ≠ 4). 1. partinin 9. maddesiyle aynı → **D153 · 2. vaka** |
| 10 | ⑥ 🟠 `dış sera ~3 m ↔ iç koridor ~4,5 m` (L9/L10) | TÜNEL: **32 × 4,5 × 3,2 m** (4,5 = GENİŞLİK, 3,2 = YÜKSEKLİK) | ⑥ ölçümü | ⚠️ **YARI — FİLM SAPTI**: ⑥'nın DIŞ ölçümü (3 m) kilide oturuyor ✓, İÇ ölçümü (4,5 m) sapıyor. Cetvel zayıf (astronot boyu SPEC'te yok) → şiddet düşük |
| 11 | ③ ambiyans yatağı: `high-altitude wind` (bütün dış sahneler) | ATMOSFER dış: "**rüzgâr 0** — hiçbir şey kıpırdamaz, kumaş çırpmaz"; ses "ince tıslama" | ③'ün AMBIENCE MAP'i | 🔴 **FİLM SAPTI — YENİ, VE TERS OKUNMUŞ.** ③ rüzgârı YATAK sanıp EQ sıçramasını bulgu yazdı; ihlal EQ değil rüzgârın VAR OLMASI |
| 12 | ③ MUSIC LEDGER: `tek kesintisiz Drone A · 0:00-3:50` | MÜZİK: 2 cue + **üç MÜZİKSİZ pencere** (0:00-0:09 · 3:07-3:20 · 3:24-3:39) + 3:24,0 kelepçe darbesi | ③'ün ledger'ı | ⬜ **AÇIK** — ölçüm cue ayırt edemez; **sahip dinler**: üç pencere müziksiz mü, 3:24'te darbe var mı |
| 13 | ② `Counter Logic: N/A — no in-scope source` | SPEC üç metinsiz sayaç yazar: SARKMA · KIRAĞI HATTI · YEŞİL SIRA 9→6 | — | ⬜ **AÇIK — ÖLÇÜM BOŞLUĞU** [D134], bulgu yokluğu değil. Filmin bütün sayaçları ②'nin ölçmediği eksende |
| 14 | ① 🔴 `1:20 vizör yok gibi → 1:44 ağır yansıma` | KASK: "cam optik berrak, renksiz, **YANSIMASIZ**" | a_t104 (1:44): vizör var, yüz sönük | ⚠️ **YARI** [D95 · 3. vaka] — "cam yok gibi" kısmı kilidin KENDİ sonucu; "ağır yansıma" kısmı kilit ihlali, ⬜ AÇIK (1:44 ±2 s izlenir) |
| 15 | ① 🔴 `1:30 domates bitkileri kaynıyor` · ⑤ 🟠 aynı saniye | seri negatif çekirdeği (texture swimming) | iki mercek bağımsız (⑤'in kendi kadraj katmanı) | 🔴 **AYAKTA** — sahibi ① [D108], ⑤'te işaretçi. Rapor S10 = **plan S9** (tema sahnesi: eldiven yaprağa değmeden geçer) |
| 16 | ①⑥ 🟠 `3:15 metal çubuk lastik gibi büküyor` | S20 kelepçe çubuğu | ⑥ L5 (>30° bükülme) | 🟠 **AYAKTA** — sahibi ⑥ (sayı taşıyor). Doruğun kendisi zaten teslim edilmemiş (E7-b) |
| 17 | ① 🟠 `0:10 kask içinde motivasyonsuz dolgu` · `1:19 AI bloom` | IŞIK: iç "gölgesiz ılık-beyaz gün ışığı" TASARIM; C "parlama/glow 0" | — | ⬜ **AÇIK** — 0:10 ve 1:19 ±3 s izlenir |
| 18 | ① 🟠 `0:39 gazdan katı beyaz statik çizgiler` | JET: kristaller **düz iner ve 3 s'de yerde** (hareketli) | — | ⚠️ **YARI**: "düz" tasarım (düşer), "**statik**" ihlal olur → ⬜ AÇIK, 0:39-0:49 izlenir |
| 19 | ② 🟡 `1:59 levhayı çekiyor ↔ 2:09 zaten tepede bağlıyor` | PERDE: S13 yarıda sıkışır → S16 serbest | — | ⬜ **AÇIK** — plan S14'ün jesti okunur, sonra 2:09 izlenir |
| 20 | ② 🟡 `0:10 ↔ 3:20 sakal yoğunluğu artıyor` | SPEC'te sakal kilidi yok | — | 🟡 **AYAKTA** (düşük şiddet) |
| 21 | ② 🟠 `fırça 0:10'da var, 0:19'da yok` | FIRÇA: "S0 elde · **S1'de düşer** · S24 elde" | plan | ✅ **TASARIM — DÜŞER** ⑩ (1. partide de düşmüştü). Asıl ihlal S24'te fırçanın GERİ GELMEMESİ |
| 22 | ②④ 🔴 `S23'te dev branda; kim serdi?` | S24: "tünelin sağ üçte biri, **kırağılı çökük FİLM**"; branda diye nesne YOK | 1. parti t222/t227 | 🔴 **FİLM SAPTI** — nedensellik değil ÜRETİM sapması; ②'nin "eklenmeli bir sahne" gerekçesi ⑩'da düşer → **D152/D153 · 2. vaka** |
| 23 | ② 🟠 `yama basıldı ama yapı yine de çöktü` | YAMA: dış yama **TUTMAZ**, ≤1 s'de uçar | 1. parti t56 (yama havada) | ✅ **TASARIM — DÜŞER** ⑩ |
| 24 | ② 🟡 `dış toz hızlı çöküyor ↔ iç toz asılı` | ATMOSFER: dış "3-4 s'de TAM çöker" · iç "hava ölü sakin" | plan | ✅ **TASARIM — DÜŞER** ⑩ (iki farklı atmosfer kilitli) |
| 25 | ①⑥ `0:20 koşu süzülüyor` ↔ ⑥ `yürüyüş low-G için ağır` | YERÇEKİMİ: koşu GERÇEK ZAMANLI, süzülme 0 [D44] | iki mercek TERS yönde | ⬜ **AÇIK** — 0:20-0:30 ve 1:29-1:59 izlenir; biri yanılıyor |

**Toplam 25 madde: 18 KAPALI** (1-11 · 15 · 16 · 20 · 21-24) · **6 ⬜ AÇIK**
(12 · 13 · 17 · 18 · 19 · 25) · **1 YARI, açık yarısıyla** (14).
⛔ Açık maddeler skorsuz kalır; **dersler yalnız kapalı satırlardan ve
ölçümden yazıldı.**

---

## 🔍 ⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME — 2. PARTİ [D108]

| gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
|---|---|---|---|
| `3:23 vizör füzyonu` (YANLIŞ) | ① 🔴 · ④ · ⑤ · ⑥ | ① | **hiç kimse** — kareyle çürüdü, dördünden de silindi |
| filigran ▷ (0:00-3:50) | ① 🔴 · ⑤ 🔴 | ① (kare) | teslim kusuru — puan değil [D150 · 3. vaka] |
| bitki dokusu kaynaması (1:29) | ① 🔴 · ⑤ 🟠 | ① | ① · ⑤'te işaretçi |
| sera çöküşü ↔ iç sağlam (1:00↔1:19) | ② 🔴 · ⑥ L3 · ③ (ses) | ② | ② — üretim kararı: plan S6 yeniden |
| gölge 180° (0:00↔3:39) | ② 🟠 · ⑥ L7/L8 | ② | ② · ⑥'da işaretçi |
| metal çubuk bükülmesi (3:15) | ① 🟠 · ⑥ L5 | ⑥ (sayı) | ⑥ |
| üs mimarisi kayması | ⑤ 🟠 · (1. partide ②) | ⑤ | ⑤ |

---

## 🧮 ⑩ ÖNERME KAPISI — 2. PARTİ [D87 · D116 · D130] · **bilgi amaçlı; tabloya satır girmiyor [D129]**

```
DÜŞEN bulgular (kaynağı planda YAZILI):
  jet "gaz gibi dağılmalı" (novum: KRİSTAL jeti) · fırça S1'de kaybolur
  (planlı düşüş) · dış yama tutmaz (t56 kanıtlı) · dış/iç toz farkı (iki
  atmosfer kilitli) · sarı perdenin SERT olması (SPEC "sert") · low-G'de
  yürüyüşün "ağır" görünmesi (süzülme 0 kilidi) · "film sessiz mi" sorusu
  (SPEC: DIALOGUE LINES 0, SILENT SCENES 25 — evet, tasarım)
KAREYLE ÇÜRÜYEN bulgu: 3:23 vizör füzyonu (dört mercekte)
5b REÇETE GREP'İ [D85]:
  ①'in `ADD "sharp, clear visor glass with realistic environmental
  reflections at all times"` önerisi → ⛔ **REDDEDİLİR**: SPEC KASK kilidi
  "cam optik berrak, renksiz, **YANSIMASIZ**" der; öneri çalışan kilidi
  ters çevirir.
  ①'in `REPLACE "cinematic lighting"` önerisi → dize film dosyalarında
  grep'lendi, **YOK** → reçete DÜŞER (rapor promptu görmedi).
  ①'in `ADD "solid, inflexible metal bar"` → ADD önerileri muaf, ayakta.
AYAKTA kalanlar (üretim/teslim kararı ister):
  sırt ünitesi (yuva 5 VE yuva 13) · S22'de kurulumdan önce duran filiz ·
  PEMBE LED şeridi · dış rüzgâr sesi · gölge 180° · S6 erken çöküş ·
  kırağı/toz dalgalanması · üs ayrıntı kayması · iç tünel yüksekliği ·
  metal çubuk · bitki dokusu kaynaması · filigran · kart · hook · −21 LUFS
④ HİKAYE kesme listesi: ⛔ **UYGULANMAZ [D129]** — gerekçesi aşağıda
```

### ⑩ SONRASI TOPLAMLAR — referans (T tablosuna GİRMEZ [D129])

| mercek | raporun toplamı | rapor aritmetiği düzeltilmiş | ⑩ sonrası | ayakta hücre |
|---|---|---|---|---|
| ① KARE | 6,3 | **5,7** (Camera hücresi "no in-scope source" ile 10 yazılmış; rubriğin kendi ④ kuralınca `—` olmalı) | 6,8 | 4 |
| ② DEVAMLILIK | 6,2 | 6,2 ✓ | 5,9 | 7 |
| ③ SES | 8,0 | 8,0 ✓ | 7,0 | 2 |
| ④ HİKAYE | 6,2 | 6,2 ✓ | 6,6 | 5 (Yapı·Yay·Final·Tutundurma ④ kapısınca SAYI TAŞIMAZ) |
| ⑤ ARKA PLAN | 6,7 | **6,0** (Focus hücresi "no in-scope source" ile 10 yazılmış) | 7,3 | 3 |
| ⑥ FİZİK | 6,9 | 6,9 ✓ (`Impact: —` kuralı DOĞRU uygulanmış) | 7,0 | 4 ⚠️ fps beyanı yanlış (24 ↔ ölçüm 30) |

> ⚠️ Altı sayının hiçbiri bir tabloya girmez ve hiçbiri 1. partinin sayılarıyla
> karşılaştırılamaz: ikisi de mod V, aradaki farkların hepsi 1,5'un altında —
> yani **gürültü** (kural ⑥).

---

## ⭐ ④ HİKAYE — "hikâyesi berbat" iddiasının ölçülmüş karşılığı

```
İZLEYİCİNİN OKUDUĞU (④, tek cümle):
  "Yalnız bir astronot, gayzer patlamasından sonra Mars serasını
   yalıtmak için yarışıyor."
PLANIN VAAT ETTİĞİ (SPEC A · logline + INTENDED EMOTION):
  "En eski bitkilerini ölüme mühürleyerek kalanı kurtarır, sonra ölü
   sıraya yeni tohum eker ve süpürmeye döner. İzleyici şunu sorarak
   çıkar: 'ben olsam yapar mıydım?'"

⛔ ARADAKİ FARKIN ADI: SEÇİM · BEDEL · TEMA ekrana GEÇMEMİŞ.
   ④ ikisini de doğru raporluyor: "kişisel bahis yok" ve "karakter
   kamera taşıyıcısı". Bu, YAZIMIN değil ÜRETİMİN sonucudur ve sebebi
   ÖLÇÜLMÜŞTÜR:

   · **S20 (DORUK) ekranda YOK** — E7-b FAIL, 1. parti t193/t198:
     çubuk 8 saniye havada; mühür yok, zar şişmesi yok, son yeşilin
     beyazlaması yok, tavan gerilmiyor. Filmin TEK seçimi bu klipte
     olacaktı ve klip onu teslim etmedi.
   · **S12 EKSİK** — tohum kutusunun Çehov kurulumu hiç üretilmemiş;
     S22 ödemesi kurulumsuz kalıyor.
   · **S23 EKSİK** — mühürlenmiş tünelin iç geniş aynası yok; "iki dünya,
     tek zar" motifinin kapanışı ekranda hiç görünmüyor.
   · **S22'de filiz kurulumdan ÖNCE ekranda** (t217/t219) — ödemenin
     kendisi de kendi kurulumunu geçersiz kılıyor.

   Yani ④'ün 6,2'si "senaryo kötü" demiyor; **"ekrandaki film, yazılan
   filmin seçim yapmayan hâli" diyor.** Aynı plan, S20 · S12 · S23
   teslim edildiğinde ④'ün ölçtüğü Karakter/Tema/Final hücrelerinin
   üçü de aynı kurguda değişir.

⛔ ④'ÜN KESME LİSTESİ UYGULANMAZ [D129] — ne çıkarmak istediği:
   rapor S10·S11·S12 = plan **S9 (TEMA sahnesi) · S10 (ORTA NOKTA) · S11**
   rapor S16·S18     = plan **S16 · S18 (karakterin TEK tereddüdü, 2 sn)**
   rapor S19 (MERGE) = plan **S19 — SPEC'te "VIRAL INTERSTITIALS … MAY NOT
                              BE CUT" ve HER ŞEYİN KAYBI vuruşu**
   rapor S5  (MERGE) = plan S4 (kırağı hattı sayacının 2. adımı)
   Yedi adayın yedisi de yük taşıyor; biri filmin orta noktası, biri
   kesilemez ilan edilmiş viral, biri karakterin tek tereddüdü.
   Bu, THE ROSE COAT'ta ölçülmüş bedelin birebir tekrarıdır.
   ⚠️ Doğru gözlem: 1:29-1:59 gerçekten yük taşımıyor — ama sebebi
   sahnelerin gereksizliği değil, plan S10'un ORTA NOKTA vuruşunu
   (iç yama tutar → dikiş yamanın ötesinde açılır) teslim etmemesi.
   a_t104 (1:44): adam koridorda kolları yanda DURUYOR. Çözüm kesmek
   değil, S10'u yeniden üretmek.
```

---

## 📊 SKOR SATIRLARI — 2. PARTİ

```
T1-T6: SATIR YOK [D129 · aynı filmde 2. kez].
Tamlık matrisi: 0/4 KALIR.
⛔ SPEC yazılmış olduğu hâlde mod V koşulan film sayısı 9'da kalıyor
   (aynı film ikinci kez sayılmaz), ama bu filmde mod V PARTİ sayısı 2.
```

---

## ✅ BİR SONRAKİ KOŞU İÇİN — 2. PARTİ SONRASI (sahip)

```
0. ⛔ ÖNCE DOSYA TEMİZLİĞİ (yeni, en ucuz iş — 2 dakika):
   □ `~/Downloads/the frost lıne .mp4` ve `the frost lıne  (1).mp4`
     THE FROST LINE DEĞİL (THE PAYLOAD gövdesi + Frost Line kartı).
     Yeniden adlandır; kartı o kurgudan çıkar.
   □ Bundan sonra master tek ada bağlanır ve QA'ya verilen dosyanın
     yolu raporun künyesine yazılır [D160]

1. EKSİK + BOZUK KLİPLER — 1. partinin listesi AYNEN geçerli, üstüne üç yeni:
   □ S12 · S23 üretilir · S20 (doruk) · S24 (fırça+kırağılı film) ·
     S6 (bir karış sarkma) · S0 (düz jet sütunu) yeniden
   □ 🆕 **S22: filiz 0 kare** — tohum ekilmeden önce yatakta çimlenmiş
     sıra OLMAYACAK (t217/t219 bunu gösteriyor)
   □ 🆕 **İÇ SAHNELERDE PEMBE LED ŞERİDİ YOK** — "yapay lamba/LED 0 kare"
     (a_t104; ⑤ envanterinde S11 ve S17'de de var)
   □ 🆕 **plan S5'te de sırt ünitesi var** (t52/t57) — D139 pozitif yüzey
     tarifi yalnız yuva 13'e değil, sırtı gören HER kadraja yazılır
   □ 🆕 dış ses yatağında RÜZGÂR YOK — "ince tıslama" (③'ün duyduğu
     "high-altitude wind" kilit ihlali); mikste düzeltilir

2. MASTER YENİDEN İHRAÇ — biri düzeldi, üçü duruyor:
   ✅ ≥1440p (4K ihraç yapılmış)
   □ filigransız kaynak ("▷" 235/235 s — 4K'da da duruyor)
   □ kart YOK (kapak çıktısı kurguya eklenmez)
   □ hook S0 10 → 9 s
   □ −14 LUFS integrated (şu an −21,2) · tepe ≤ −1,0 dBTP (şu an −0,1)

3. AÇIK MADDELER (~2 dk izleme/dinleme): 0:10 kask dolgusu · 0:39-0:49 jet
   statik mi · 1:19 bloom · 1:44 vizör yansıması · 2:09 perde jesti ·
   0:20 koşu ↔ 1:29 yürüyüş (biri yanılıyor) · **müzik: üç sessizlik
   penceresi (0:00-0:09 · 3:07-3:20 · 3:24-3:39) ve 3:24 kelepçe darbesi**

4. MOD D KOŞUSU — ÜÇÜNCÜ KEZ isteniyor, iki kez atlandı:
   ①'e A+B · ④'e A · ⑤'e C'nin üç kilidi · ⑥'ya C'nin sayısal kilitleri
   + ⑪ satırı KÜNYEYE: `SES KANALI: VAR · −x LUFS · tepe −y dBTP` [D137]
   + her mercek TEMİZ oturumda [D110/D159] · ⑥ TEK koşu · fps 30 verilir
```

---

## 📚 2. PARTİDEN ÇIKAN DERSLER

```
YENİ   D159 aynı oturumda koşulan mercekler birbirinin BULGU CÜMLESİNİ
       kopyalıyor ve kopyalanan bulgu YANLIŞ olabilir — "3:23 parmaklar
       vizörden geçiyor" dört mercekte birebir aynı cümleyle çıktı,
       kareyle çürüdü, ve ①'in REGENERATE'ini taşıyan dört 🔴'dan
       biriydi. ⑤ kapısı SAYILARI karşılaştırıyor, METNİ değil (08_QA)
       D160 master DOSYA ADI kimlik değildir — "the frost lıne" adlı beş
       dosyanın ikisi başka bir film, üstelik bu filmin kapak kartını
       taşıyor. ⑪ kapısı süreyi ölçüyor ama kimliği doğrulamıyor (08_QA)
TEKRAR D129 (aynı filmde 2. parti) · D137 (ölçüm satırı yine yapıştırılmadı)
       · D139 (3. vaka — yeni yuva) · D147 (3. vaka) · D150 (3. vaka —
       4K ihraçta da duruyor) · D153 (2. vaka) · D156 (2. vaka — "filiz 0
       kare" sıfır kilidi yine aranmadı) · D95 (3. vaka) · D44 (⬜ açık) ·
       D70/72 (kart hâlâ kurguda) · D134 (② sayaçları N/A yazdı)
```
