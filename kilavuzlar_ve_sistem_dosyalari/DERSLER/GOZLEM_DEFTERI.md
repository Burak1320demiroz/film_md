# 🗒️ GÖZLEM DEFTERİ — kapısız adaylar (ders DEĞİL)

> `00_DERS_YAZIM_KONTRATI.md` §4. Kapısı bulunmayan ya da geçersiz partiden
> gelen aday burada bekler; kapıya bağlanınca ders numarası alır. Sayı:
> `sayac.sh` 🧭 bloğu. Bu dosyada `## … DERS <rakam>` başlığı YAZILMAZ.

> ⭐ **14.09.2026 KÜMELEME (reform FAZ 2).** 93 numaralı 94 kayıt (ADAY-6 çiftti → 6a/6b)
> filmler arası örüntüye göre kümelendi: **84 kayıt** 11 yeni film dersine (D206-D216)
> ya da dört mevcut derse (D193 · D200 · D202 · D151) bağlandı — her birinin başlığı
> `## ✅ ADAY-n` + `**DURUM:** → D…` satırı taşır ve sayaçta AÇIK sayılmaz. Açık kalanlar
> süreç adayları (K15: 2 · 13 · 14 · 15 · 91) ve tek vakalar (21 · 75). Yeni kural: aday ≥ 2 filmde
> tekrarlayınca ders olur (kontrat §2b); tek vaka burada bekler. Gen-B (ADAY-16..90)
> kayıtlarındaki `🔗` bağlantıları şablon üretimidir, ders kaynağı olarak okunmaz.

---

## ✅ ADAY-1 — KAPANDI 01.09.2026 · HİPOTEZ **YANLIŞ** · ders YAZILMADI

> ⑪ ölçüm kapısı koşuldu (`01_FILM_RAPORLARI/THE_COLD_WELD.md` §⑪.3). Kapatma
> kuralı işletildi: **üç kare de EKRANDA VAR** → hipotez çürüdü.
>   S6 avuç makrosu 65 s ✅ · diskli DUVAR 100-120 s ✅ (planın S8'i değil,
>   S10-S11 yuvasında) · S12 doruk jesti 122-125 s ✅
> Sorun ÜRETİM değil **OKUMA**: ② duvarı gördü ve otuz bir diski "wall BUTTONS"
> sandı, ⑤ duvarı gördü ve üstündekileri hiç saymadı. Bu **D151'in 2. vakası**
> (mercek vuruşu görmez / tersine okur) + D129'un maliyeti (SPEC C bloğu
> "31 parlak disk" diyor, verilmedi). Yeni ders GEREKMEDİ — mevcut iki dersin
> tekrar sayacı arttı.
> ⭐ Bu koşunun ürettiği YENİ ders başka yerden çıktı: **D163** (insan şeridi
> tek-figürlü filmde blok takasını göremez) — ⑪.4.
> ⛔ Aşağısı kapanmadan önceki kayıttır, DEĞİŞTİRİLMEDİ.

### (kapanmadan önceki hâli) ADAY-1 — YOKLUKLA KANITLANAN KURAL EKRANDA OKUNMUYOR

**Tarih / kaynak:** 01.09.2026 · THE COLD WELD · altı mercek, altısı mod V
(parti ⑤'ten 🚨 GEÇERSİZ, kilit defteri 9 ⬜ AÇIK → ders YAZILAMAZ).

**Gözlem (raporlardan, doğrulanmamış):** altı merceğin altısı filmin
novum'unu adlandırmadı. ④ izleyici cümlesi *"impossible physical anomalies"*;
⑥ FLAGS *"is the wrench MAGNETIZED?"* (rakip kural); ② avuç diskini gördü,
durum değişimini (2 → 0) hiç kaydetmedi; hiçbir rapor 31 diskli duvarı,
avucun kopmasını ya da S12'nin bilerek kaynamasını anmadı.

**Hipotez:** bu filmdeki kanıtların TAMAMI birer olumsuzlama — düşmeyen
anahtar · kalkmayan avuç · kaymayan levha · yapışmayan bot. Video "bir şeyin
olmaması"nı "hiçbir şey olmaması" diye render eder. Planın A4 satırı D76'yı
(yokluk novumu) "kapalı" saydı çünkü novum DÜNYADA bir varlıktır (kaynak);
ama EKRANDA her kanıtı bir yokluk. A4 yanlış soruyu soruyor:
"novum bir yokluk mu?" değil, **"novumun her KANITI bir yokluk mu?"**

**Kapatma (master gelince, ~2 dk):**
```
ffmpeg -ss 66  -i "$M" -frames:v 1 s6_avuc.jpg    → disk kopuyor mu, geride kalıyor mu
ffmpeg -ss 85  -i "$M" -frames:v 1 s8_duvar.jpg   → duvarda kaç parlak disk var
ffmpeg -ss 122 -i "$M" -frames:v 1 s12_avuc.jpg   → avuç levhaya BASIYOR mu
üçü de VARSA → hipotez yanlış; sorun okuma değil ÖLÇÜM → D151 ailesi (mercek göremez)
biri YOKSA   → hipotez doğru; sorun ÜRETİM → ders olur, kapısı 03_PLAN_ONCESI A4'e yeni soru
```

**Olası kapı:** LİSTE · `03_PLAN_ONCESI_KONTROL_LISTESI.md` A4'e beşinci
soru: "novumun kanıtlarından en az biri POZİTİF bir olay mı (bir şey OLUYOR
mu), yoksa hepsi bir şeyin olmaması mı?"

---

## ADAY-2 — REFERANS PANELİ ÜRETİLMEDEN METİN KİLİDİ TUTMUYOR (D146'nın devamı)

**Tarih / kaynak:** 01.09.2026 · YERÇEKİMİ FAZ 2 · iki mühürlü geçiş
(A kör + B katalog, D164). Parti **mod V** — SPEC yok, master yok →
film-dersi YAZILAMAZ, aday olarak düşer.

**Gözlem (iki bağımsız geçiş, biri katalogsuz):** vizör geometrisi dokuz
promptta ölçüsüyle yazılıydı (`24 by 16 centimetres` + `visible bright metal
frame`), prompt_kontrol.py GO verdi, ve kubbe çıkan altı klibin beşinde tam
tarif vardı. Aynı makarada mekik burnu on iki promptun hepsinde
`nose pointing screen-left` yazılıyken beş klipte ters çıktı — **tek doğru
çıkan klip, burnun kadraj DIŞINDA olduğu ve yönü kompozisyonun taşıdığı
klipti.** REFERANS_PAKETI'nde üretilmiş panel sayısı: **0/15.**

**Hipotez:** metin kilidi, modelin görsel önyargısıyla yarıştığında kaybeder;
sayı yazmak yalnız kilidin VARLIĞINI garanti eder. Bir biçim kilidi ancak
(a) bir REFERANS GÖRSELİ ile, ya da (b) kadrajda YÜK TAŞIYARAK tutar.

**Kapatma (ucuz, ~1 üretim):** RA p4 (yüz CU) üretilir, vizör doğru çıkana
kadar tekrarlanır, seed yazılır; sonra AYNI prompt seed'li referansla bir kez
daha koşulur.
```
referanssız kubbe + referanslı düz  → hipotez DOĞRU → kapı: LİSTE ·
   03_PLAN_ONCESI'ye "biçim kilidi olan her varlığın paneli ÜRETİLDİ mi?"
   (ve prompt_kontrol'a: panel seed'i boşken üretim GO alamaz)
ikisi de kubbe                      → hipotez YANLIŞ, sorun motorda → tasarım değişir
```

**Olası kapı:** BETİK · `prompt_kontrol.py` — REFERANS_PAKETI'nde seed kutusu
BOŞ olan bir sayfaya ÇAPA veren prompt varsa **FIX** (belki BLOCK).

---

## ✅ ADAY-3 — TEK NOKTADA OKUNAN SAYAÇ SAAT DEĞİLDİR

**DURUM:** → D151 not · K14 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Tarih / kaynak:** 01.09.2026 · YERÇEKİMİ FAZ 2 kör geçişi · mod V.

**Gözlem:** kör denetçi on iki klibi sıraladı ve üçünü sıralayamadı. Kendi
gerekçesi: *"4, 7 ve 10'un sırasından emin değilim — üçü de aynı fiziksel
durumu gösteriyor."* O üç klip arasındaki TEK fark oksijen halkasının 6/6 →
4/6 düşüşüydü ve halka o fazda **yalnız tek klipte** okunabiliyor.
Karşılaştırılacak ikinci okuma yok. Aynı film boyunca sayaç 6/6 → 4/6 → 3/6 →
2/6 diye ilerliyor ama faz dosyalarındaki durum notları neredeyse her
seferinde "(kadrajda değil)" / "vurgusuz" diyor.

**Hipotez:** bir sayaç ancak **en az iki farklı zamanda okunabiliyorsa** saat
olur. Tek okuma bir DURUM bildirir, GEÇİŞ bildirmez; izleyici (ve denetçi)
ondan sıra çıkaramaz. Ekimi görünmeyen Çehov silahı gibi.

⭐ Aynı film bunun ÇÖZÜMÜNÜ zaten bir yerde uygulamış: FAZ 3'ün S30 ve S34
sahnelerinde düşüş **sahnenin İÇİNDE** oluyor (4/6 → 3/6 · 1/4 → 0/4). Geçişi
görmek, iki ayrı okumaya gerek bırakmıyor.

**Kapatma:** faz dosyalarında sayaç düşüşü olan her sahne için tek soru —
"düşüş bu kadrajda GÖRÜLÜYOR mu, yoksa yalnız beyan mı ediliyor?"

**Olası kapı:** LİSTE · `03_PLAN_ONCESI_KONTROL_LISTESI.md` — "her sayaç
düşüşü ya kadrajın İÇİNDE olur, ya düşüşün iki yanında birer okunur kadraj
vardır."

---

## ✅ ADAY-4 — DÖNÜM ANI KADRAJIN KENARINDAYDI VE İLK İZLEMEDE GÖRÜLMEDİ

**DURUM:** → D202 TEKRAR · K3 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Tarih / kaynak:** 01.09.2026 · YERÇEKİMİ FAZ 2 kör geçişi · mod V.

**Gözlem:** S18 fazın (ve karakterin) dönüm anıdır: halat kopar. Kör denetçi o
klibi şöyle tarif etti: *"Kaskın içinde bir yüz. Önde turuncu bir ray. Kişi
hafifçe etrafa bakıyor."* Halattan tek kelime yok — ve klibi bu yüzden HASAR
ÖNCESİ kliplerin arasına yerleştirdi. Promptta olay yazılı: halat kadrajın
**alt-sağ kenarında**, ince, 2. saniyede kopuyor; ikinci sinyal (vizördeki
dönme yansıması) de zayıf.

**Hipotez:** olayın kadrajdaki YERİ ve ALANI, promptta yazılı olmasından
bağımsız olarak okunabilirliği belirliyor. Kenarda + ince + kısa = görünmez.
⚠️ Bu, "prompt eksikti" vakası DEĞİL — prompt tamdı. Kadraj kararı eksikti.

**Kapatma:** klibin 2. saniyesinden kare çıkar, halatın kapladığı piksel
alanına bak.
```
ffmpeg -ss <klip başı+2> -i "$M" -frames:v 1 s18_halat.jpg
```

**Olası kapı:** LİSTE · plan aşamasında — "bu sahnenin TEK olayı kadrajın
neresinde ve kaç saniye sürüyor? Kenarda ve ≤1 s ise ikinci bir sinyal var mı?"

---

## 📌 01.09.2026 · ADAY-3 ve ADAY-4 SAYAÇ GÜNCELLEMESİ (YERÇEKİMİ FAZ 3)

```
ADAY-3 (tek noktada okunan sayaç saat değildir) → 3. VAKA
  F3'ün kör geçişi F (eller/halka) ve H (istasyon) girdilerini
  YERLEŞTİREMEDİ. Gerekçesi: "Segment 7'de kime ait olduğu belli
  olmayan bilekler, Segment 8'de kimseyi göremediğim bir istasyon."
  Halka düşüşü (4→3) sıraya yine hiçbir şey katmadı — üstelik bu fazda
  düşüş SAHNE İÇİNDE tasarlanmıştı ve render'da HİÇ OLMADI.
  ⭐ Yeni bilgi: tasarım doğruydu, üretim tutmadı. Yani aday hâlâ açık
     ama sebebi değişti — "okunmuyor" değil, "olmuyor".

ADAY-4 (dönüm anı kadraj kenarında, görülmüyor) → 2. VAKA
  F2: S18'de halatın kopuşu görülmedi.
  F3: G'deki OMUZ VURUŞU görülmedi — fazın PLANLI tek fiziksel teması,
  TEMA sahnesinin karşılığı. Kör denetçiye doğrudan soruldu ("iki insan
  hiç temas ediyor mu?") ve cevabı: "Evet — Segment 12'de EL ELE
  TUTUŞUYORLAR" (bu spec'te YOK; L'de kollar açık, eller boşa kapanır).
  ⭐ İki vaka aynı biçimde: planlı jest okunmuyor, PLANSIZ bir jest
     onun yerini alıyor ve izleyici için asıl an o oluyor.
  Üçüncü vakada ders olur; kapı adayı LİSTE (plan aşamasında jest ölçüsü).

## 📌 06.09.2026 · ADAY-4'E İKİNCİ VAKA — RENDER KUSURU SAHTE SAAT OLDU

**Kaynak:** YERÇEKİMİ FAZ 7 · kör geçiş · sıra skoru 3/12

```
VAKA 1 (F3) : D(S28) ve J(S34)'te kask düştü → kör denetçi bunu
              "hayatta kalma saati" sayıp fazın SONUNA koydu → 8/12'den 5/12'ye
VAKA 2 (F7) : C(S73)'te SAÇ AŞAĞI SARKTI (0g kusuru) → kör denetçi
              bunu bir numaralı tek yönlü saati yaptı:
              "Gravity state: Normal gravity in Seg 1, zero-gravity in
               Seg 2. Confidence: HIGH."
              → fazın tamamı ona göre hizalandı → 3/12
```

**Örüntü:** bir 0g/kimlik/donanım render kusuru, kör denetçinin
kurabileceği EN NET ikili karşıtlığı üretir (var/yok · takılı/çıkmış) —
yani gerçek anlatı saatlerinden daha güçlü görünür ve onları ezer.

```
⭐ ÖLÇÜM SONUCU: sıra skoru düştüğünde ilk sorulacak soru "faz
  bağlamsız mı" DEĞİL, "kör denetçi hangi saati kullandı ve o saat
  GERÇEK Mİ" olmalıdır. Rubrikte cevabı zaten var (STEP 4/c CLOCKS).
⚠️ İki vaka. Üçüncüsünde ders yazılır [00_DERS_YAZIM_KONTRATI].
```

---

## ✅ ADAY-5 — VİVİD KÜÇÜK AYRINTI, KAPSAYAN NESNEYİ EZİYOR

**DURUM:** → D214 · K12 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Tarih / kaynak:** 01.09.2026 · YERÇEKİMİ FAZ 3 · iki mühürlü geçiş · mod V.

**Gözlem:** S28'in video promptunda kask ×4 geçiyor ve tam vizör cümlesi
ölçüleriyle yazılı. Aynı promptta şu cümle var:
`"Her body is never rigid: shoulders lead, legs follow, HAIR LIFTS INSIDE
THE HELMET."` Render'da **saç kalktı, kask gitti** — kadın vakumda kasksız,
saçı uçuşuyor. Aynı kalıp S25'te de yarı düştü: kask kaldı ama kör denetçi
"saç rüzgârdaymış gibi şiddetle uçuşuyor" dedi.

**Hipotez:** bir cümle içinde küçük ve hareketli bir ayrıntı (saç) ile onu
KAPSAYAN katı nesne (kask) birlikte yazıldığında, model hareketli ayrıntıyı
öne alıp kapsayıcıyı düşürebiliyor. "İçinde" ilişkisi, hareket tarifinin
yanında zayıf kalıyor.

**Ölçü:** `hair … in/inside the helmet` kalıbı filmde **8 yerde** —
FAZ_01 3 · FAZ_03 3 · FAZ_04 2. F4 henüz üretilmedi.

**Kapatma (bedava, F4 üretilmeden):** F4'ün iki geçişinde saç, kasktan AYRI
bir cümleye taşınır (ya da silinir). F4 üretilir.
```
saç ayrı cümlede → kask düşmüyorsa  → hipotez DOĞRU → kapı: BETİK
   (prompt_kontrol: aynı cümlede "hair" + "helmet" → FIX)
kask yine düşüyorsa                 → hipotez YANLIŞ, sebep başka
```

**Olası kapı:** BETİK · `prompt_kontrol.py` — kask cümlesiyle aynı cümlede
hareketli beden ayrıntısı varsa FIX. ⚠️ D79 kask bloğunun kardeşi: D79
cümlenin VARLIĞINI ölçüyor, bu KOMŞULUĞUNU ölçer.

---

## ✅ ADAY-6a — THE STILL SWARM: SEKİZ MERCEĞİN SEKİZİ DE NOVUM'U GÖREMEDİ (ADAY-1'in 2. VAKASI)

**DURUM:** → D151 not · K14 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Tarih / kaynak:** 02.09.2026 · THE STILL SWARM · **sekiz mercek, sekizi de
mod V** (①④⑥⑦⑧ D129'dan ⛔ TEKRAR; kilit defterinde **8 ⬜ AÇIK** madde;
master ölçülmedi) → `01_FILM_RAPORLARI/THE_STILL_SWARM.md`.
⛔ Bu partiden **film-dersi yazılamaz** [DERS_YAZIM_KONTRATI §4]. Aşağıdakiler
gözlemdir, bulgu değil; hepsi **tek bir ölçüm koşusuyla** karara bağlanır.

**Gözlem (raporlardan, doğrulanmamış):**

```
① Filmin novum'u (kabuğa giren cisim 0,15 s'de DURUR) hiçbir raporda
   adlandırılmadı. ⑦'nin BEAT STRING'inde S6 yuvası "-" = "bu sahnede
   vuruş yok" — S6 filmin NOVUM TAŞIYICISI ve TEK KARE sahnesidir (1:04).
   ④: "THE ONE THING NOTHING ELSE DOES: I could not find one."
② Sekiz raporun sekizi de hareketi "tether/halat çekerek ilerleme" diye
   okudu. Filmde ilerleme KÜTLE ATMAKLA olur (kelepçe fırlatma, 8→0).
   Hiçbir raporun vuruş/efor defterinde TEK BİR ATIŞ yok.
   ⚠️ Halat planda VARDIR (S0-S3 gergin, S3'te gevşer, S8'de KOPAR —
     B2b başarısız deneme #2). Yani "halat gördüm" bulgusu ⑩'da DÜŞER;
     ayakta kalan soru şu: ATIŞLAR EKRANDA MI?
③ ⑤'in COUNT LOG'u S8-S9'da "5 floating hand tools in a row" saydı.
   SPEC'in sayacı S7 = 5 · S8 = 5 diyor ve kelepçeler DÜZ BİR HAT olur.
   Yani ATILMIŞ KELEPÇE HATTI ekranda olabilir — ve "alet" diye okunmuş.
④ Kurgu 13 klip / ~134 s görünüyor; plan 14 klip / 140 s. ⑨ ızgarası ilk
   13 yuvaya oturuyor (max |Δ| = 1,0 s) → eksik klip KUYRUKTA, yani S13:
   FİNAL VURUŞ + TWIST + LOOP karesi. Yerinde bir BAŞLIK KARTI var
   (SPEC: ekran metni 0,0 s · başlık kartı 0 kare).
```

**Hipotez:** ② ve ③ birlikte okunursa novum EKRANDADIR ve sekiz mercek onu
"alet", "tether işi", "uzay tamiri" diye okumuştur — yani kusur ÜRETİMDE
değil ÖLÇÜMDE. ④ doğruysa filmin payoff'u hiç üretilmemiştir ve o zaman
①'in sebebi de budur: kural kurulur, ama KARŞILIĞI gösterilmez.

**KAPATMA KURALI — iki komut, ~1 dakika:**

```bash
bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"   # süre + ızgara
ffmpeg -ss 64 -i "<master>" -frames:v 1 tek_kare_1-04.jpg        # → BAK

kelepçe eldivenden ~2 m ötede ASILI + süre 140 s + 14 klip
   → NOVUM ÜRETİLDİ, FİNAL ÜRETİLDİ → kusur ÖLÇÜMDE → D166'nın 2. vakası,
     yeni ders GEREKMEZ
kelepçe yok / hareketli   → NOVUM EKRANDA DEĞİL → S6'dan sonrası yeniden üretilir
süre ~134 s + 13 klip     → FİNAL ÜRETİLMEDİ → ayrı ders adayı (kuyruk kaybı,
                            D62/D72 ailesinin yeni vakası)
```

**Olası kapı (kapanışa göre seçilir):** LİSTE · `03_PLAN_ONCESI_KONTROL_LISTESI`
— "novum'un KARŞILIĞI (kuralın kırıldığı/ödüllendiği sahne) kuyrukta mı? Kuyruk
klibi ÜRETİLDİ mi?" · ya da ARŞİV, hipotez çürürse.

> 🔗 ADAY-1 (THE COLD WELD, aynı şekil — kapandı: kusur okumaydı) ·
> Ders 166 (bu partiden çıkan ALET dersi) · Ders 157 (novum taşıyıcısı) ·
> Ders 62/72 (kuyruk = filmin finali) · Ders 141 (final vuruş kanıtı kareyle)

---

## ✅ ADAY-6b — İKİ BİLEK YAN YANA, TEPEDEN MAKRO: BU KADRAJ ÜRETİLEMİYOR

**DURUM:** → D214 · K12 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Tarih / kaynak:** 02.09.2026 · YERÇEKİMİ · **iki bağımsız vaka**, aynı
kadraj tipi, aynı sonuç:
```
S8  (FAZ 1, 31.08) — iki eldivenli bilek, tepeden makro, rayda
                     → üç deneme, üçü de politika reddi → İPTAL
S70 (FAZ 6, 02.09) — iki çıplak bilek yan yana, tepeden makro,
                     sağda siyah kayışlı saat → ısrarla red → İPTAL
```

**Gözlem:** ortak geometri şu: **gövdeden kopmuş iki bilek/el, aynı
kadrajda, tepeden makro, en az birinde bir kayış.** İkisinde de içerik
tamamen masumdu (bir rayda tutunma · durmuş bir saate bakma) ve ikisinde
de kelime düzeltmesi YETMEDİ; kadraj değişikliği de yetmedi.

**Hipotez:** sınıflandırıcı bu geometriyi bedenden ayrılmış bilek + bağ
olarak okuyor. Tek tek hiçbir öğe yasak değil; birleşimleri üretilemiyor.

⚠️ **S69 vakası hipotezi GENİŞLETİYOR:** orada kol tamamen kaldırıldı
(el baştan beri kolçakta, hiçbir şey yükselmiyor) ve YİNE reddedildi.
Demek ki kalan yığın da yetiyor: **yalnız + loş + gözler aşağı + açık
boğaz.** Yani tetikleyici tek bir kadraj tipi değil, bir ATMOSFER
BİLEŞİMİ olabilir. Üçüncü vaka bunu ayıracak.

**Kapatma (bedava, F7-F10 üretilmeden):** aynı bilgiyi taşıyan kadrajı
tek bilekle, YANDAN ve gövdeye bağlı olarak yaz; bir kez üret.
```
geçerse  → hipotez DOĞRU (geometri) → kapı: LİSTE · 03_PLAN_ONCESI'ye
   "aynı kadrajda gövdeden kopuk iki bilek/el var mı?" sorusu
geçmezse → hipotez EKSİK; sorun atmosfer bileşimi → ayrı aday
```

**Olası kapı:** BETİK · `prompt_kontrol.py` — bir promptta "both wrists /
two wrists / two gloves" + "macro/extreme close-up" + "from above/
high-angle" birlikte geçiyorsa **FIX** (üretilemeyecek kadraj uyarısı).
⚠️ Bu, betiğin ilk KOMPOZİSYON kapısı olurdu; şimdiye kadar hep kelime
ölçtü. Politika reddi veren üç vakanın üçü de kelimeyle yakalanamadı.

---

## ✅ ADAY-7 — VİDEO PROMPTUNDA TIRNAK İÇİNDE YAZILAN REPLİK, KAREYE ALTYAZI OLARAK GÖMÜLÜYOR

**DURUM:** → KAPANDI 06.09.2026 — sebep ARAÇ (aşağıdaki kapanış kaydı) · D215 örüntüsünün kaynağı (14.09.2026)

**Tarih / kaynak:** 02.09.2026 · YERÇEKİMİ FAZ 5 · iki mühürlü geçiş · mod V
(film-dersi yazılamaz; prompt dili dersi 06'ya girerdi → aday).

**Gözlem:** F5'in on iki sahnesinden **YALNIZ İKİSİNDE** video promptu
tırnak içinde bir replik taşıyor — S57 (STATION AI) ve S60 (CAPSULE AI).
Kör geçiş makarada **tam iki altyazı** saydı ve ikisi de o iki sahnede:
```
Seg 9  (S57) → "Cabin pressure falling, seal the hatch."
Seg 12 (S60) → "Capsule power nominal."
```
**2/2.** Ve yasak promptta AÇIKÇA vardı: F5 dosyasında `no subtitles` /
`no caption` **24 kez** geçiyor, iki sahnenin ikisinde de `heard only —
never shown as text` yazılı.

**Hipotez:** modelin altyazı üretmesini tetikleyen şey yasağın yokluğu
değil, **promptta tırnak içinde duran cümlenin kendisi.** Yasak
sayılabilir bir engel değil; cümle bir içerik talebi.

**Ölçü — filmin toplam maruziyeti:**
```
Video promptunda tırnak içinde replik taşıyan sahne: 33 / 120
  F1 5 · F2 4 · F3 6 · F4 7 · F5 2 · F6 2 · F7 4 · F8 3
ÜRETİLMEMİŞ olanlar: F7 4 + F8 3 = 7 sahne  ← ücretsiz düzeltme penceresi
```

⭐ **Filmin kendi içinde çözümü zaten var:** F6 KİLİT 27, çobanın sesi
için *"Promptta yabancı dilde CÜMLE YAZILMAZ: 'a man's voice speaking
calmly in a language she does not know' denir"* diyor. Aynı teknik
altyazıyı da engeller — orada D34 için yazılmıştı.

⚠️ **İkinci hipotez, aynı kanıttan:** F1-F3'te altyazı YOKTU ve o üç
makara 8,0 s ızgaradaydı; F4-F5 10,0 s ızgarada ve altyazı F5'te çıktı.
**Izgara değişimi ile altyazı aynı sebepten olabilir: üretim aracı
F3 ile F4 arasında değişti.** Bu tek bir soruyla kapanır (aşağıda).

**Kapatma (bedava, F7 üretilmeden):**
```
① Proje sahibine tek soru: F3 ile F4 arasında üretim aracında/modelinde/
   ayarında ne değişti? (ızgara 8→10 s ve altyazı aynı anda başladı)
② F7'nin dört replikli sahnesinden BİRİNDE tırnaklı cümle silinir,
   yerine "a flat synthetic voice makes a short announcement" yazılır;
   sahne üretilir.
     altyazı ÇIKMAZSA → hipotez DOĞRU → kapı: BETİK
        (prompt_kontrol: video promptunda tırnak içinde cümle → FIX)
     altyazı YİNE ÇIKARSA → sebep araçtadır, prompt değil → ayar sorusu
```

**Olası kapı:** BETİK · `prompt_kontrol.py` — video promptunda `"..."`
içinde bir cümle varsa **FIX** ("replik tırnakla yazılmaz; söyleyeni ve
tonu tarif et, cümleyi post'a bırak").

---

## 📌 02.09.2026 · ADAY-7 GÜNCELLEME — HİPOTEZ YARISINDAN ÇÜRÜDÜ (YERÇEKİMİ FAZ 6)

```
ADAY-7 diyordu ki: "altyazıyı tetikleyen şey promptta TIRNAK İÇİNDE
duran cümledir." F5'te kanıt 2/2 idi.

FAZ 6 ÖLÇÜMÜ — hipotez YETMİYOR:
  F6'da tırnaklı replik taşıyan sahne: 2   (S61 · S71)
  Makarada çıkan altyazı:              3   (Seg 1=S61 · Seg 6=S66 · Seg 9=S71)

⛔ ÜÇÜNCÜSÜ S66 — VE O SAHNEDE TIRNAKLI CÜMLE YOKTU.
   S66 tam olarak KİLİT 27'ye göre yazılmıştı: "a man's voice speaking
   calmly in a language she does not know... The voice never becomes
   intelligible and never addresses her."
   Model o sahneye BİR CÜMLE UYDURDU ve altyazı olarak bastı:
      "Contact confirmed. Please maintain trajectory."
   ⭐⭐ Uydurduğu cümle sahnenin ANLAMINI TERSİNE ÇEVİRİYOR: sahnenin
      tek fikri sesin ANLAŞILMAMASI ve ona HİTAP ETMEMESİDİR. Altyazı
      "sana hitap ediyorum, rotanı koru" diyor.
```

**REVİZE HİPOTEZ:** tetikleyici tırnak değil, **video promptunda BİR SESİN
ANLATILMASI.** Tırnağı kaldırmak gerekli ama YETERLİ DEĞİL.

**Ölçü — filmin gerçek maruziyeti çok daha büyük:**
```
Video promptunda SES TARİF EDİLEN sahne: 115 / 120
  (tırnaklı olan yalnız 33'ü)
```
⚠️ Ama F1-F4'ün 48 sahnesinin hepsinde de ses tarifi vardı ve altyazı
ÇIKMADI. Yani sesin tarifi tek başına da yetmiyor.

**ZAMAN ÇİZGİSİ — asıl değişken burada:**
```
F1 · F2 · F3   8,0 s ızgara   altyazı 0
F4            10,0 s ızgara   altyazı 0
F5            10,0 s ızgara   altyazı 2   (tırnaklı sahne sayısı 2)
F6            10,0 s ızgara   altyazı 3   (tırnaklı sahne sayısı 2)
```
→ Izgara F4'te değişti, altyazı F5'te başladı ve **F6'da tırnak sayısını
AŞTI.** Oran artıyor. Bu bir prompt kusuru değil, **araç davranışı**
gibi görünüyor.

**Kapatma — tek soru + tek üretim:**
```
① Proje sahibine: F3→F4 ve F4→F5 arasında araçta/modelde/ayarda ne
   değişti? (ızgara F4'te, altyazı F5'te başladı — iki ayrı eşik olabilir)
② F7'nin dört sesli beat'inden BİRİNDE ses satırı TAMAMEN silinir
   (yalnız kadında görülen tepki yazılır) ve sahne üretilir.
     altyazı ÇIKMAZSA → kapı: BETİK (video promptunda ses anlatan
        beat satırı → FIX; ses zaten post'ta)
     altyazı YİNE ÇIKARSA → sebep araçtadır; çözüm prompt değil ayar
```

**Olası kapı:** KARAR · video promptunun beat satırları YALNIZ KAMERANIN
GÖRDÜĞÜNÜ anlatır. Ses post'tadır ve filmin kendi kuralı zaten bunu
söylüyor ("on iki sahne SESSİZ üretilir"). Beat "3s — ses şunu der"
değil, "3s — gözleri bir kez oynar ve durur" olur.

---

## 🔴 06.09.2026 · ADAY-7 KAPANDI — HİPOTEZ TAMAMEN ÇÜRÜDÜ, SEBEP ARAÇ

**Kaynak:** YERÇEKİMİ FAZ 7 makarası · kör geçiş · mod V
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ07_KOR_HAM.md`

```
DENEY KOŞULDU VE TEK DEĞİŞKEN DEĞİŞTİ:
  F7'de tırnaklı cümle 0 · sesi anlatan beat satırı 0 · replik 0 yazıldı.
  Negatif blok, uzunluk, kadraj, ışık — hiçbiri değişmedi.

SONUÇ:
  F5  tırnaklı 2 · sesi anlatan beat VAR  → altyazı 2
  F6  tırnaklı 2 · sesi anlatan beat VAR  → altyazı 3
  F7  tırnaklı 0 · sesi anlatan beat 0    → altyazı 7   ⛔⛔

⭐ SAYI DÜŞMEDİ, İKİYE KATLANDI. Ve yedisi de UYDURMA:
   hiçbiri REPLİK DEFTERİ'ndeki cümle değil · ikisi repliksiz sahnede
   (S77 · S82) · ikisi anlamsız ("Officially decisions and" ·
   "Singing have a timed") · biri aynı klipte iki kez basıldı.
```

**SONUÇ — üç hipotez de öldü:**

| hipotez | çürüten |
|---|---|
| tetikleyici TIRNAK | F6 (tırnaksız S66 altyazı bastı) |
| tetikleyici SESİ ANLATAN BEAT | F7 (beat 0, altyazı 7) |
| tetikleyici promptta HERHANGİ BİR ŞEY | F7 |

```
⛔ KAPI YAZILMAZ. prompt_kontrol.py'ye altyazı kapısı eklenirse depo,
  düzeltemeyeceği bir şeyi her fazda kontrol etmiş gibi yapar.
✅ ÇÖZÜM HATTI: ① araç/ayar tarafı  ② üretim sonrası maskeleme/kırpma
✅ ÖLÇÜM SÜRER: her makarada altyazı SAYILIR ve BİREBİR alıntılanır —
  uydurma cümle ile promptta yazılı cümle ancak metin karşılaştırmasıyla
  ayrılır.
```

⭐ **SON AÇIK DEĞİŞKEN — F9/S107'de koşuluyor:** F7'de beat satırları
temizlendi ama `Audio:` PARAGRAFLARI dokunulmadan kaldı ve her biri sesi
uzun uzun anlatıyor. F9'un S107'si (insansız · replik 0 · fazın en
risksiz sahnesi) `Audio:` paragrafı TAMAMEN SİLİNEREK üretilecek; kalan
on bir sahne dokunulmayacak.

```
altyazı S107'de de çıkarsa → sebep kesin ARAÇ, dosya kapanır
altyazı S107'de ÇIKMAZSA  → tetikleyici `Audio:` bloğudur ve kapı
                            BETİĞE ilk kez meşru olarak yazılır
```

---

## ✅ ADAY-8 — WORLD BLOĞU CANLIYI BÜTÜN OLARAK TARİF EDİNCE, TEK-UZUV KADRAJI İKİ BACAK ÜRETTİ

**DURUM:** → D214 · K12 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE UPWARD FALL · ⑪ ölçüm kapısı, 186 s karesi (`q_canli.jpg`)
**Vaka:** 1 (04.09.2026) — kural: 3 vaka olmadan belge revizyonu, ders değil.
**KAPI:** ⬜ yok — bu yüzden ADAY. Aday kapı: `prompt_kontrol.py` KISMİ
REVEAL KAPISI — NEGATIVE'inde `no second limb` / `no body` / `no head`
geçen bir sahnenin WORLD ya da CHARACTER bloğu **uzuv SAYISI yazamaz**.

```
S21 promptu, aynı dosyada, üç yerde:

WORLD    "One large animal lives in that canopy: it has one body and
          FOUR LONG LIMBS, it moves only down and up, and it NEVER
          COMES TO THE GROUND."                          ← bütün anatomi
SCENE    "ONE SINGLE grey-green limb ... comes down out of the top of
          the frame and ends level with his chest"       ← tek uzuv
NEGATIVE "Only one limb is in frame: no body, no head, ... no second
          limb ... Nothing touches him"                  ← yasak

EKRAN (186 s): İKİ kalın sütun uzuv, tabanları kütüğe/zemine BASIYOR,
               ayak gibi genişleyen uçlarla — yani BACAK okunuyor.
               SPEC C: ANATOMY LOCK `0 bacak · 0 baş · YÜRÜME 0 adım`.
```

**Hipotez:** reveal merdiveni (K0-K4) SAHNE bloğunda kurulurken, WORLD
bloğu aynı promptta canlının TAM anatomisini veriyor. Model kadraj dışını
tarif eden cümleyi bir yasak değil bir **envanter** olarak okuyor ve
envanterden çiziyor. Negatif listesi "no second limb" dese de, sayı zaten
promptun içinde yazılı.

**Belge tarafı (önce bu, ders sonra):**
`UZAYLI_VARLIK_TASARIM_KILAVUZU.md` reveal merdiveni bölümüne tek kural —
*K0-K2 sahnelerinde WORLD bloğu canlıdan yalnız KADRAJIN GÖRDÜĞÜ kadarını
tarif eder; uzuv/göz/baş SAYISI yalnız K4 sahnesinde yazılır.*
Kılavuz 03.09.2026'da açıldı; bu onun ilk ölçülmüş vakası.

🔗 [[D175]] (mühür) ve [[D176]] (zemin rengi) ile aynı aile: **aynı promptta
iki cümle, iki sadakat** — [[D174]]'ün mekanizması, bu kez anatomide.

---

## ✅ ADAY-9 — KOLU YAZILMAYAN ELDİVEN **KOPUK** DOĞDU, VE TEK İNSANLI FİLMDE İKİNCİ MÜRETTEBAT GİBİ OKUNDU

**DURUM:** → D214 · K12 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Vaka:** 1 (ders için ≥2 bekleniyor) · **KAPI:** aday — muhtemel BETİK
(`prompt_kontrol.py`, tek-uzuv kadrajında süreklilik cümlesi araması)

**Kaynak:** THE HEALING GROUND S4 · 04.09.2026 · prompt dosyası + kare 45 s.
(② DEVAMLILIK raporu bunu "The Magic Glove" diye yakaladı ama o rapor
🚨 GEÇERSİZ — bulgunun kanıtı rapordan değil PROMPTTAN ve KAREDEN geliyor.)

```
İMAJ  "Only one glove and forearm are in shot ... The glove rests open
       on the floor at the bottom edge of frame."
VİDEO "Only one glove and forearm are in shot ... The glove rests open on
       the floor at the bottom edge of frame." · "0.0s — ... the open
       glove rests on the crust at the bottom edge" · "8.0s — The glove
       has not moved."

EKRAN (45 s): zeminde SAHİBİ OLMAYAN, boş bir eldiven. Kol yok, bilek yok.
              HUMAN COUNT LOCK: 1 × 14.
```

**Hipotez:** *"the glove rests on the floor"* modelde bir NESNE cümlesidir,
bir BEDEN cümlesi değil. "forearm" kadrajın içinde sayılıyor ama fiil
eldivene ait olduğu için model kolu düşürüyor. Sonuç: tek insanlı bir
filmde zeminde duran boş eldiven **ikinci bir insanın bıraktığı ekipman**
gibi okunuyor — ④ HİKAYE onu "Disconnected Stakes / threat vector"
sandı, ② "ikinci mürettebat mı?" diye belgeye soru yazdı. **Filmin en
yüksek sesli cevapsız sorusu bir KAZAYDI.**

**Denenecek kalıp (bir sonraki tek-uzuv kadrajında):**
```
✗ "The glove rests open on the floor at the bottom edge of frame."
✓ "The glove rests on the crust, the wrist and forearm continuing
   unbroken out of the bottom edge of frame."
```
Kural adayı: **kadrajda bir uzuv varsa, o uzvun GÖVDEYE GİDEN YOLU
yazılır.** Kesilmiş uzuv tarif edilirse model kesilmiş uzuv çizer.

🔗 [[ADAY-8]] ile aynı aile (kadraj dışı beden), ters yönden: orada WORLD
bloğu fazla anatomi verdi, burada SCENE bloğu eksik verdi.
[[D179]] ile aynı film.

---

## 📌 05.09.2026 · THE STANDING WIRE — ADAY-2 ve ADAY-7 GÜNCELLEMESİ

Parti 🚨 GEÇERSİZ (sekiz mercek mod V + master filigranlı) → **film-dersi
yazılamaz** [KONTRAT §4]. Aşağıdakilerin kanıtı rapordan değil **ölçümden ve
prompt dosyasından** geliyor; yine de biri kulakla, biri tek üretimle kapanır.

```
ADAY-2 (biçim kilidi referans paneli olmadan tutmuyor) → 2. ÖLÇÜLMÜŞ FİLM
  YERÇEKİMİ FAZ 2 : vizör ölçüsüyle yazılı, prompt_kontrol GO, ekranda KUBBE
  THE STANDING WIRE: aynısı, 24 klipte, REFERANS_PAKETI 0 panel
  → [[D146]] TEKRAR 3'e çıktı ve ⛔ ÇALIŞMIYOR aldı; dönüştürme borcu
    ADAY-2'nin önerdiği araçtır. Aday artık kapanmayı değil YAPILMAYI bekliyor.
```

---

## ✅ ADAY-10 — SIFIR REPLİKLİ FİLMDE DÖRT CÜMLE KONUŞULDU; PROMPTTA NE TIRNAK VAR NE SES TARİFİ (ADAY-7'nin 3. VAKASI, KULAKLA KAPANACAK)

**DURUM:** → D215 · K13a (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE STANDING WIRE · 05.09.2026 · ⑤ çapraz kapı + bant ölçümü.
**KAPI:** aday — muhtemel BETİK (`prompt_kontrol.py`: video promptunda AUDIO
bloğu → FIX). **Vaka:** ADAY-7 ailesinin 3.'sü, ama **kulakla doğrulanmadı.**

```
SPEC       DIALOGUE LINES: 0 · SILENT SCENES: 25/25 · film TAMAMEN SESSİZ
PROMPT     tırnak içinde cümle: 0    ·   "No voice, no music" defalarca yazılı
           AUDIO bloğu ise HER promptta var: "two calm helmet breaths…"

RAPORLAR   ② ③ ④ üçü de AYNI dört cümleyi AYNI saniyelerde yazdı:
           0:50 "Just a little further."      0:52 "The wire is still holding."
           0:55 "Made it this far."           0:58 "Almost at the top."
           ① tek satırda aynı metni yazdı · ⑤ ⑥ ⑦ ⑧ "hiçbir şey duymadım"

ÖLÇÜM      300-3400 Hz pencere RMS:
             40-50 s −41,1 │ 50-60 s −32,4 │ 60-70 s −42,8 │ 100-110 s −44,8
             150-160 s −43,7 │ 200-210 s −62,9
           → 50-60 s filmin TEK konuşma-bandı zirvesi, +9…+10 dB
           −30 dB eşiğinde o pencerede DÖRT ayrık patlama, her biri ~1,2 s:
             51,2-52,3 · 53,1-54,3 · 55,3-56,5 · 58,0-59,4
           → raporların dört zaman kodunun DÖRDÜ de tutuyor
KADRAJ     50-60 s SIRTTAN çekim — ağız hiç görünmüyor, lip-sync ile
           çürütülemez; ses "kaynaksız" kalıyor
```

**Hipotez:** tetikleyici ne tırnak (0) ne de tarif edilmiş bir ses (yok) —
**promptta AUDIO bloğunun var olmasının kendisi.** Yerli sesi olan bir modele
"şu sesler duyulsun, ses YOK" demek, "altyazı yok" ×24 yazmakla aynı yere
düşüyor: yasak sayılabilir bir engel değil, blok bir içerik talebi.

⛔ **BU ADAY DERS DEĞİL, ÇÜNKÜ KULAK YOK.** Ölçüm güçlü ama konuşma duymadı;
üç merceğin ortak transkripti de tek bir oturumdan geliyor [D110].

**KAPATMA — 10 saniye, proje sahibi yapar:**
```
0:50-1:00 arası DİNLE.
  KONUŞMA VAR  → aday DERS olur; kapı: video promptu AUDIO bloğu TAŞIMAZ
                 (ses post'tadır; filmin kendi kuralı zaten "25/25 sessiz")
  KONUŞMA YOK  → üç mercek aynı halüsinasyonu paylaştı → [[D151]]/[[D173]]
                 ailesinin yeni vakası, ve ⑤ replik ekseni bu partide
                 çoğunluğu değil AZINLIĞI doğrular
```
🔗 [[ADAY-7]] (aynı aile, iki YERÇEKİMİ vakası) · [[D110]] · [[D181]]

---

## ✅ ADAY-11 — YAZILAN ZORLANMA KANALI EKRANDA YOK; PROMPT TAM, BEDEN BOŞ

**DURUM:** → D206 · K1 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE STANDING WIRE · 05.09.2026 · 50-60 s kare şeridi (BAKILDI).
**KAPI:** aday. **Vaka:** 1 (ölçülmüş) — ders için ≥2 bekleniyor.

```
SPEC C  ZORLANMA · kanal ELDİVEN YÜZEYİ [D175] · dokuz sahne:
        S1·S3·S4·S7·S9·S16·S17·S18·S20
        ✅ "the glove's ribbed segments tighten and lift over the knuckles"
        ✅ "the sleeve's fabric draws taut along the forearm"
        prompt_kontrol.py ⑧ EFOR kapısı bu cümleleri ARADI ve BULDU → GO

EKRAN   50-60 s (dik kaya duvarı tırmanışı, 20 kare, 0,5 s aralık):
        yürüyüş kadar düzgün, sarsıntısız, tereddütsüz bir tırmanış;
        omuz düşmesi yok, duraklama yok, ağırlık aktarımı okunmuyor
```

**Hipotez:** ⑧ EFOR kapısı [D169] cümlenin VARLIĞINI ölçer, hareketin
GERÇEKLEŞTİĞİNİ değil — [[D146]]/[[ADAY-2]] ile **birebir aynı mekanizma**,
ama BİÇİM yerine HAREKET ekseninde. Biçim tarafında dönüştürme borcu doğdu
(referans paneli); hareket tarafında karşılığı ne olur, bilinmiyor —
hareketin referansı bir panel değildir.

⚠️ ⑧ EFOR raporu bu filme `1,4/10 · NOBODY PAYS` verdi ve gözlem yönü aynı —
**ama o rapor mod V, tally'si tutmuyor ve ham zincir ölçtü [[D181]]**, o yüzden
buradaki kanıt rapor değil KARE.

**Kapatma:** master kurgulanıp yeniden ihraç edildikten sonra aynı şerit
tekrar çıkarılır; efor hâlâ yoksa aday 2. vakasını alır ve ders olur.
🔗 [[D169]] (efor kanalları) · [[D175]] (kanal eldiven yüzeyi) · [[ADAY-2]] · [[D181]]

---

## ✅ ADAY-12 — EFOR MERCEĞİ 2.0/10 "NOBODY PAYS": TAKIM ELBİSELİ İNSAN HİÇ BİR ŞEY ÖDEMEDEN YABANCI GEZEGENİ GEZDİ (ADAY-11'İN 2. VAKASI)

**DURUM:** → D206 · K1 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Tarih / kaynak:** 09.09.2026 · THE MIRROR FAUNA · ⑧ EFOR · **mod D** (QA_SPEC verildi).
**KAPI:** aday — [[ADAY-11]]'in 2. vakasıdır; üçüncüde ders yazılır.

```
FILM       THE_MIRROR_FAUNA · 0.7g · basınçlı kıyafet · ZORLANMA 0 beyan
PROMPT     prompt_kontrol.py ⑧ EFOR kapısı → GO (efor kanal cümleleri bulundu)

EKRAN      4 exertion event, 4'ünde de strain YOK:
  E1 00:00 yürüyüş → moonwalk, suit kütlesiz
  E2 00:50 eldivenle kadranı çevirme → bare-hand dexterity
  E3 01:10 ağır silah atışı → recoil sıfır, merkez kütle sabit
  E4 01:50 enerji darbesiyle fırlatılma → rigid düşüş, sonraki sahnede
           sıfır yara izi, sıfır yürüyüş bozukluğu

COST CURVE: 1111111111144111
RESET:      S13→S14 arası · 4→1 · UNEARNED (toparlanma yok)

MOD D KILIT: 0.7g yerçekimi / kıyafet kütlesi → FAIL (E1)
```

**Bağ ADAY-11 ile:** Orada THE STANDING WIRE tırmanıştı — prompt dolu, ekran boş.
Burada THE MIRROR FAUNA silah atışı ve enerji darbesi — prompt dolu, ekran boş.
İki filmde, iki farklı tür çalışma, aynı çıktı: **bedel ödenmedi.**

⚠️ **Bu ADAY, ADAY-11'den iki noktada ayrılır:**
1. ADAY-11 mod V'ydi (ham zincir + raporun ayrı sorunları); bu **mod D** — SPEC verildi.
2. ADAY-11'in kanıtı KARE'ydi; bu kanıt **rapor** (rapor_kontrol.py kapısı koşulmadı ama
   mod D olduğu için T8 satırı yazılabilir hâle geliyor — koşulunca).

**Hipotez:** Model prompt'ta yazılı EFOR KANAL cümlelerini ("the glove's ribbed segments
tighten", "the sleeve's fabric draws taut") bir **beyan** olarak kaydeder, bir **kamera
komutası** olarak değil. Kapı cümlenin varlığını ölçer ama hareketin GERÇEKLEŞMESİNİ
ölçmez — [[ADAY-2]]'nin biçim eksenindeki karşılığı burada efor ekseninde.

**Üçüncü vaka kapatma:** Başka bir filmde ⑧ EFOR mercek koşulur.
```
NOBODY PAYS verdict YİNE GELIRSE → hipotez doğru →
  kapı: BETİK · prompt_kontrol.py — EFOR KANALI cümlesi VARDIR ama hareketin
  BEDEN'DE OKUNMASI aranmaz → FIX (sahne metnine "body reads the cost" cümlesi)
  ya da KARAR · suitli çekimlerde efor KAMERANIN GÖRDÜKLERİNE yazılır,
  suit anatomisine değil
BLOCKER YOKSA → aday kapanır, sorun başka → D169 ailesi genişlemez
```

**Olası kapı adayı:** BETİK · `prompt_kontrol.py` — EFOR KANALI cümlesi bulunan
sahneye "body reads the cost" / "suit registers the work" ikinci cümle ARANIR.
Yoksa FIX (cümle şablona eklenir). Bu, ①-ADAY-2-ADAY-11 ailesiyle aynı kapı
biçimidir: sadece eksen BİÇİM'den HAREKET'e kaydı.

🔗 [[ADAY-11]] (aynı aile · THE STANDING WIRE · mod V · 1. vaka) ·
🔗 [[D169]] (efor kanalları) · [[D175]] (kanal eldiven yüzeyi)

---

## 📌 09.09.2026 · THE BENT GRASS — ADAY-10 GÜNCELLEME: HİPOTEZ **KARŞI VAKA** ALDI

ADAY-10 diyordu ki: sıfır replikli filmde duyulan/yazılan cümlelerin
tetikleyicisi ne tırnak ne tarif edilmiş ses — **promptta AUDIO bloğunun
var olmasının kendisi.**

THE_BENT_GRASS bu hipotezi doğrudan sınıyor ve **çürütüyor**:

```
PROMPT     "AUDIO" bloğu: 0    (BOLUM_1 ve BOLUM_2'de grep = 0)
           tırnak içinde replik: 0
           "dialogue" geçen 22 yer: HEPSİ negatif çekirdek
                                    ("no burned-in dialogue text")
           "breath" geçen 7 yer:    HEPSİ görsel
                                    ("chest and shoulders rise and fall",
                                     "No breath fog")
           → promptta HİÇBİR ses talebi yok

RAPOR      ⑦ AKSİYON + ⑩ OYUNCULUK, aynı oturum, AYNI dört cümle:
           1:41 "We are ready, proceed eleven."
           1:44 "Emptied on the mark."
           1:45 "Copy that, looks clean, setting it down now."
           1:48 "And that is all of it."
           ⑧ ⑨ ⑪ ⑫ (aynı oturum): "none — room tone present"
           ① ② ③ ⑤ ⑥ (önceki oturum): "none — nothing audible to me"
           ③ SES — eksenin SAHİBİ — "NO VERDICT: NOTHING MEASURED"
```

⭐ **İki filmde ortak olan, AUDIO bloğu değil YER:** THE STANDING WIRE'da dört
cümle tırmanışın ortasına düştü; burada **1:41-1:48 = S10 = filmin MERKEZÎ
SEÇİMİ** (kasanın boşaltılması). İkisinde de ~4 kısa, işlevsel, telsiz
ağzıyla İngilizce cümle ve ikisinde de filmin en ağır vuruşunun üstünde.
Hipotez artık "AUDIO bloğu" değil, "**sessiz bırakılan doruk**" yönünü
gösteriyor — ama ikisi de KULAKLA kapanmadı.

⛔ **Bu aday hâlâ ders değil, çünkü kulak yok** — bu koşuda master
verilmedi, ⑪ ölçüm kapısı hiç koşmadı.

**KAPATMA — 10 saniye, proje sahibi yapar:**
```
THE_BENT_GRASS 1:38-1:52 arası DİNLE.
  KONUŞMA VAR  → ADAY-10'un AUDIO-bloğu hipotezi ÖLÜ; tetikleyici başka
                 (aday yeniden yazılır: "doruk sahnesi ses üretiyor")
  KONUŞMA YOK  → iki mercek aynı oturumda aynı transkripti paylaştı →
                 [[D110]] + [[D159]] ailesi, ve ⑤ replik ekseninde
                 9-2 çoğunluğu bu partide GEÇERSİZDİR (aşağıya bak)
```
🔗 [[ADAY-7]] · [[ADAY-10]] · [[D110]] · [[D159]] · [[D162]]

---

## ADAY-13 — MOD D KİLİT TABLOSUNUN "MEASURED ON SCREEN" SÜTUNU SPEC'İN KENDİ SAYISIYLA DOLDURULDU; PAYDA KENDİ SAHNE SAYISINI TUTMUYORDU VE HİÇBİR KAPI BAKMADI

**Kaynak:** THE_BENT_GRASS · ⑥ FİZİK · **mod D** · 9,8/10 "PHYSICS HOLDS" ·
09.09.2026.
**KAPI:** aday — muhtemel BETİK (`rapor_kontrol.py`: mod D raporunda kilit
tablosunun paydası ≠ `SCENES OBSERVED` → otomatik ŞARTLI). **Vaka:** 1.

```
⑥'nın KENDİ künyesi      SCENES OBSERVED: 13
⑥'nın kilit tablosu      "S0-S12: Shadows point right 14/14 scenes" → PASS
SPEC C · EKRAN YÖNÜ      "güneş 14/14 ekran solunda · gölgeler 14/14 ekran sağına"
                         → 14/14 EKRANIN değil SPEC'İN paydası; kopyalanmış

⑥ IŞIK TAKVİMİ satırı    stated:   "gölge S0 1,5 kat GÖVDE → S13 3 kat GÖVDE"
                         measured: "S0 1.5x body → S12 ~3x LEG height"
                         Δ: 0 · PASS        ← iki AYRI cetvel, fark 0 yazıldı

⑪ IŞIK aynı makarada     S2 key KAYBOLDU · S3 key 9→3 TERS DÖNDÜ · S7 key
                         KAYBOLDU · 3 ışık sıçraması · 6,5/10 "KEY WALKS"
```

**Hipotez:** Mod D'de kilidin metni raporun önünde duruyor ve model "ölçülen"
sütununa **kilidin kendisini** yazıyor; sonra iki özdeş hücreyi karşılaştırıp
Δ=0 · PASS üretiyor. Bu [[D164]]'ün ("rubriğin kendi tarifi rapora dönünce
çapa sanıldı — dört çapanın dördü de yankıydı") kilit tablosundaki karşılığı,
ama burada **tek satırlık makine testi var**: mod D raporunda "measured"
sütununun paydası raporun kendi `SCENES OBSERVED` değerini tutmalıdır.
13 sahne gören bir mercek 14/14 yazamaz.

**İkinci vaka kapatma:** Başka bir mod D filminde kilit tablosunun paydası
`SCENES OBSERVED` ile karşılaştırılır. Yine sapıyorsa hipotez doğru → betik
kapısı yazılır. Tutuyorsa aday kapanır ve bu tek vaka ⑥'ya özel kalır.

⚠️ Bu adayın ekran tarafı **kanıtlanmadı**: master verilmedi, ⑪ ölçüm kapısı
koşmadı. Kanıtlanan tek şey raporun KENDİ İÇİNDE tutmadığıdır — ve o zaten
yeter, çünkü payda hatası ekranı görmeden okunur.

🔗 [[D164]] · [[D184]] · [[D186]] · [[D183]]

---

## ADAY-14 — ⑤ ÇAPRAZ KAPI MERCEK SAYIYOR, OTURUM SAYMIYOR: 9-2'LİK BİR ÇOĞUNLUK ASLINDA 1-1 OLABİLİR

**Kaynak:** THE_BENT_GRASS · 11 mercek · 09.09.2026.
**KAPI:** aday — muhtemel BETİK (`rapor_kontrol.py` ⑤: oy saymadan ÖNCE
künyeye göre öbekle; aynı künyeli mercekler TEK oy). **Vaka:** 1
(ama [[D110]]'un doğrudan devamı).

```
ÖBEK 1   ① ② ③ ⑤ ⑥   süre 2:14 · kart 2:10-2:14 (4 s) · "nothing audible to me"
ÖBEK 2   ⑦ ⑧ ⑨ ⑩ ⑪ ⑫  süre 2:16 · kart 2:10-2:16 (6 s) · "room tone present"

Aynı dosya. İki kuyruk uzunluğu. İki ses durumu.
```

Betik ⑤ replik eksenini şöyle bildirdi:
`⑩ 4 · ⑪ 0 · ⑫ 0 · ① 0 · ② 0 · ③ 0 · ⑥ 0 · ⑦ 4 · ⑧ 0 · ⑨ 0`
— okunuşu "9 mercek 0 dedi, 2 mercek 4 dedi", yani ezici çoğunluk.

⛔ **Ama ses ekseni oturuma göre bölünüyor, mercege göre değil.** "Hiçbir ses
duymadım" diyen BEŞİNİN BEŞİ tek öbekte; "room tone var" diyen ALTININ ALTISI
öteki öbekte. [[D110]] azınlık için kuralı zaten koymuştu — *"aynı oturumda
arka arkaya koşulan iki mercek tek ölçümün iki kılıfı olabilir; azınlık İKİ
oy değil BİR oydur"* — bu koşu aynı kuralın **çoğunluk** tarafını gösteriyor.
Betik ②+⑤+⑥ için ORTAK DEFTER ŞÜPHESİ bastı ama aynı testi ikinci öbeğe
uygulamadı.

⭐ Ve eksenin SAHİBİ (③ SES) 1. öbekte: "NO VERDICT — NOTHING MEASURED".
Sahibi ölçemediğini söylerken sahibi olmayan altı mercek ekseni doldurdu;
ikisi transkriptle. Bu [[D162]]'nin tersyüzü — orada sahibi kördü, sahibi
olmayan gördü; burada da öyle, ama bu kez **gören taraf tek bir oturum.**

**İkinci vaka kapatma:** Başka bir partide iki oturum künyesi ayrışsın ve
⑤ ekseni yine oturuma göre bölünsün. Bölünüyorsa: `rapor_kontrol.py` ⑤ oy
saymadan önce künye öbeklerini kurar, öbek içi mutabakatı 1 oy sayar.

🔗 [[D110]] · [[D112]] · [[D159]] · [[D162]] · [[D177]] · [[ADAY-10]]

---

## ADAY-15 — İKİ MERCEK AYNI MAKARADAN İKİ UYUŞMAZ KURULUM BÖLÜNTÜSÜ ÇIKARDI; ⑤ ÇAPRAZ KAPI BU EKSENE HİÇ BAKMIYOR

**Kaynak:** THE_BENT_GRASS · ② DEVAMLILIK (mod V) + ⑨ KADRAJ (mod D) ·
09.09.2026.
**KAPI:** aday — muhtemel BETİK (`rapor_kontrol.py` ⑤: ②'nin
`SETUP INVENTORY` repeat map'i ile ⑨'un `SETUP STRING`i aynı BÖLÜNTÜyü
vermeli). **Vaka:** 1.

```
②  "distinct setups: 9 · repeat map: A: S0,S12 · B: S1,S2,S7,S9,S10 ·
    C: S3,S8 · D: S4,S6 · E: S5 · F: S11"
⑨  OBSERVED: A B ? ? D E ? ? F ? G ? A
    (S2 ? · S3 ? · S7 ? · S9 ? · S11 ? — plana göre MISS)
```

**Neden bu sadece etiket farkı değil:** ② S1 ile S2'yi AYNI kuruluma koyuyor.
⑨ S1'i plan-B ile eşliyor ama S2'yi HİÇBİR kurulumla eşleyemiyor. İkisi aynı
anda doğru olamaz: S1 ve S2 gerçekten aynı kadrajsa S2 de B'dir; değilse
②'nin repeat map'i yanlıştır. Etiket harfleri farklı olabilir, **bölüntü**
farklı olamaz.

⑤ çapraz kapı bugün dört ekseni karşılaştırıyor: kesme · sahne · şerit ·
replik. Kurulum bölüntüsü iki mercekten birden makine-okunur biçimde çıkıyor
ve karşılaştırılmıyor.

⚠️ Hangisinin haklı olduğu **rapordan çözülemez** [[D96]] — kare ister.

**İkinci vaka kapatma:** Aynı makaraya hem ② hem ⑨ koşan bir sonraki partide
iki bölüntü yan yana konur. Yine uyuşmuyorsa eksen ⑤'e eklenir.

🔗 [[D96]] · [[D107]] · [[D115]] · [[D184]] · [[D194]]

---

## ✅ ADAY-16 — KASK VİZÖRÜ ARDINDAN KİŞİSEL KİMLİK/CİNSİYET DEĞİŞİMİ (D79 + D167 İLİŞKİLİ)

**DURUM:** → D208 · K6 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod D (Karakter / Devamlılık): 2/10 — `00:14 (S2 male face) vs 00:52 (S6 female face)`.
**KAPI:** aday — muhtemel BETİK / LİSTE (`prompt_kontrol.py` ⑲ kimlik / Character Bible vizör kilidi). **Vaka:** 1.

**Gözlem:** Aynı astronot kıyafetini giyen tekil karakterin kask vizör yansımasından görünen yüzü S2'de erkek (bıyıklı, esmer), S6'da ise kadın (açık tenli, kavisli kaşlı) olarak render edilmiştir. Vizör şeffaflığı ve vizör ardı yüz tarifi prompt seviyesinde sabitlenmediğinde model her sahnede farklı bir aktör üretebilmektedir.

**Çözüm Hipotezi:** Character Bible'da vizör arkasındaki yüzün kemik yapısı ve cinsiyeti `single specific astronaut face (or opaque gold tinted visor)` kalıbıyla kilitlenmeli ya da vizör optik koyu reflektif tutulmalıdır.

🔗 [[D79]] · [[D146]] · [[D167]]

---

## ✅ ADAY-17 — SAHNELER ARASI ZAMAN VE IŞIK MONOTONLUĞUNUN BOZULMASI (GÜNDÜZ-GECE SIÇRAMASI)

**DURUM:** → D193 TEKRAR · K4 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod D (Zaman ve Işık): 4/10 — `00:58 (S6 daylight) vs 01:01 (S7 starry night) vs 01:11 (S8 daylight ground) vs 01:31 (S10 starry night)`.
**KAPI:** aday — muhtemel BETİK (`prompt_kontrol.py` Işık Takvimi Monotonluk Denetimi). **Vaka:** 1.

**Gözlem:** Film içi sahneler arasında zaman ve gökyüzü ışığı monotonik ilerlemek yerine gündüzden geceye, ardından tekrar gündüze anlık sıçramalar yapmaktadır. S1-S6 gündüz mavi-gri sky, S7 gece yıldızlı gökyüzü, S8 gündüz zemin ışığı, S9-S10 gece sky.

**Çözüm Hipotezi:** Işık takvimi sahneler arasında strict time-of-day etiketiyle (`continuous overcast daylight` veya `continuous starry night`) kilitlenmeli, geçişler planda aşamalı monotonik (Ders 193) olarak tanımlanmalıdır.

🔗 [[D6]] · [[D176]] · [[D193]]

---

## ✅ ADAY-18 — KADRAJ DIŞINDAN BAŞLAYAN DİYALOGDA TELSİZ/RADYO FİLTRESİ VE UZAMSAL ACOUSTIC KOPUKLUĞU

**DURUM:** → D216 · K13b (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod A (Ses / Konuşmacı): 7/10 — `0:31 pilot line starts over exterior hull shot before cutting to interior helmet view at 0:33 without radio comms processing`.
**KAPI:** aday — muhtemel LİSTE (`SES_VE_DIYALOG_URETIM_KILAVUZU` §1a kadraj dışı ses kuralı). **Vaka:** 1.

**Gözlem:** Dış mekân kurgusu üzerindeyken başlayan pilot repliğinde (0:31-0:33) kask içi radyo telsiz band-pass filtresi uygulanmadığı için kuru/iç mekân sesi duyulmakta, bu da görsel ile akustik uzam arasında uyumsuzluk üretmektedir.

**Çözüm Hipotezi:** Kadraj dışı (OFF-SCREEN / COMMS) repliklerde kask içi telsiz filtresi (high-pass at 300Hz, band-limited comms processing) zorunlu kılınmalıdır.

🔗 [[D99]] · [[D180]]

---

## ✅ ADAY-19 — DİYALOG ALTINDA ALARM/PERKÜSYON DUCKING EKSİKLİĞİ VE KATMAN TAŞMASI

**DURUM:** → D216 · K13b (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod A (Mix Hiyerarşisi): 5/10 — `0:34 & 1:00 layer count reaches 5, alarm klaxon and music un-ducked, masking dialogue by ~3-4 dB`.
**KAPI:** aday — muhtemel LİSTE (`SES_VE_DIYALOG_URETIM_KILAVUZU` §4 Mix Hiyerarşisi kapısı). **Vaka:** 1.

**Gözlem:** Yoğun aksiyon ve alarm sahnelerinde eşzamanlı ses katmanı sayısı 5'e ulaşarak 3-4 katman tavanını aşmakta; perkülatif müzik ve alarm klaksonu diyalog altında otomatik ducking yapılmadığından konuşma anlaşılırlığı 3-4 dB düşmektedir.

**Çözüm Hipotezi:** Diyalog başladığında arka plan müzik ve alarm katmanlarına -6 dB ila -10 dB otomatik ducking uygulanmalı ve eşzamanlı katman sayısı maksimum 4 ile sınırlandırılmalıdır.

🔗 [[D180]]

---

## ✅ ADAY-20 — VİDEO ÇERÇEVESİNDE YAZILIM LOGO VE FİLİGRAN ARTEFAKTI (KÖŞE FİLİGRANI)

**DURUM:** → D215 · K13a (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod B (Arka Plan / Çerçeve Kenarları): 7/10 — `00:01–01:39 persistent teal triangular logo emblem static in bottom-right corner`.
**KAPI:** aday — muhtemel BETİK / LİSTE (`IMAGE_VIDEO_PROMPT_TEMPLATES` Negative Bible filigran bloğu). **Vaka:** 1.

**Gözlem:** Tüm video sahneleri boyunca sağ alt köşede statik bir yeşil/camgöbeği jeneratif model logosu/filigranı belirmiş ve anlatı illüzyonunu bozmuştur.

**Çözüm Hipotezi:** Negatif prompt bloğuna `no watermark, no logo, no corner emblem, no software graphic composited in corner` zorunlu kılınmalı; montaj aşamasında %5 dikey kırpma uygulanmalıdır.

🔗 [[D9]] · [[D34]]

---

## ✅ ADAY-21 — DİYALOGUN GÖRSELİ BİREBİR ANLATMASI (VISUAL NARRATION EXPOSITION)

**DURUM:** → D217 · 15.09.2026 — ikinci film MARS_SON_CIKIS (④ B1 Dialogue 6/10 · ④ B2 8/10, ikisi de mod V) · kontrat §2b FREKANS 2 film

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod H (Hikaye / Diyalog): 5/10 — `0:58 line 5 ("We can't hold this trajectory much longer!") narrating what violently shaking camera frame already shows`.
**KAPI:** aday — muhtemel LİSTE (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU` Replik Yazım Kapısı). **Vaka:** 1.

**Gözlem:** Kokpitin şiddetle sallandığı ve g-force baskısının zaten net göründüğü 0:58'de pilotun "Yörüngeyi daha fazla tutamıyoruz!" demesi görselliği tekrarlamakta (narrating the visible), alt metin ve duygusal derinlik üretmemektedir.

**Çözüm Hipotezi:** Karakter sarsıntı veya fiziksel felaket anında gördüğü tekniği açıklamak yerine kişisel kabulleniş, korku veya içsel tepki vermelidir (örn. durum tespiti değil, kararın bedeli).

🔗 [[D99]] · [[D180]]

---

## ✅ ADAY-22 — MİKROYERÇEKİMİ KIVILCIM VE İTME PARÇACIKLARININ İVME UYUMSUZLUĞU (SPARK ACCELERATION DRIFT)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod 6 (Fizik / Parçacık Hareketi): 9.7/10 — `01:21 spark fall duration 0.60 s over 0.5 m implied g ≈ 2.8 m/s² (0.28 g) vs baseline ground expectation`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Fizik Kapısı). **Vaka:** 1.

**Gözlem:** Tarama cihazından çıkan kıvılcımlar düşerken 0.28g (~2.8 m/s²) yerçekimi ivmesi ölçülmüştür; bu, uzay ortamında Dünya yerçekimi beklentisine kıyasla floaty bir his yaratmaktadır.

**Çözüm Hipotezi:** Mikroyerçekimi veya düşük yerçekimli uzay sahnelerinde kıvılcım ve döküntü sahneleri retrolarda %130 hızlandırma (1.3x speed ramp) ile kurguda Terrestrial beklentiye yaklaştırılmalıdır.

🔗 [[D6]] · [[D16]]

---

## ✅ ADAY-23 — AKSİYON VURUŞLARINDA TEMAS ÖNCESİ KESME VE KADRAJ DIŞI NESNE ETKİLEŞİMİ (ACTION ELLIPSIS)

**DURUM:** → D213 · K11 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod 7 (Aksiyon / Temas Legibility): 7.2/10 — `00:27–00:33 (B3) glove reaches for exterior panel handle but edit cuts away before contact (Pattern ④), 01:05–01:11 (B6) tether clip interaction occurs off-screen at lower frame boundary (Pattern ⑧/⑫)`.
**KAPI:** aday — muhtemel LİSTE (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU` Aksiyon Kurulum Kapısı). **Vaka:** 1.

**Gözlem:** EVA hareketinde el dış panel koluna uzanırken temas gerçekleşmeden hemen önce kesme yapılmış (Action Ellipsis), güvenlik halatı klipsinin takılma anı ise alt kadraj sınırının dışında kalmıştır (Stakes Object Off-Screen).

**Çözüm Hipotezi:** Aksiyon vuruşlarında elin nesneyle buluşma anı (contact moment) ve kilitleme sonucu (resolution) aynı kadraj içerisinde tam olarak gösterilmeli, kesme temas gerçekleşmeden hemen önce yapılmamalıdır.

🔗 [[D127]] · [[D184]]

---

## ✅ ADAY-24 — BEDEN KAS EFORU VE VİZÖR NEFES BUĞULANMASI SIFIRLIĞI (NOBODY PAYS / ZERO STRAIN)

**DURUM:** → D206 · K1 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod 8 (Efor / Bedel Derin Tarama): 2.0/10 — `00:10-01:30 5 exertion events show zero strain, visor fogging static, body posture unbothered by energy shockwave (Verdict: NOBODY PAYS)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Efor ve Bedel Kapısı). **Vaka:** 1.

**Gözlem:** Astronot ağır EVA elbisesinde yürürken, duvarı 10 saniye boyunca bastırarak tararken ve ayağının dibinde enerji patlaması şok dalgası oluşurken beden duruşu sıfır kas eforu gösterilmekte (NOBODY PAYS); kask vizörü nefes buğulanması ve göğüs kalkışı tamamen statik kalmaktadır.

**Çözüm Hipotezi:** Ağır fiziksel efor ve patlama şok dalgası anlarında prompt seviyesinde beden geri tepmesi (`posture recoil, defensive muscle tightening`), ağır eldiven bükülme kıvrımları ve kask vizöründe dinamik nefes buğulanması overlay'i kilitlenmelidir.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-25 — KAPANIS KARESI KAFİYE ÇİFTİ VE KAMERA KAZIK HIZALAMASI KIRILMASI (RHYME PAIR BROKEN)

**DURUM:** → D210 · K7 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod 9 (Kadraj / Plan Sadakati — Mod V): 5.7/10 — `01:29 (S10) closing shot breaks bookend structure by introducing Setup J instead of returning to Setup A (Verdict: RHYME BROKEN)`.
**KAPI:** aday — muhtemel LİSTE (`ACILIS_KAPANIS_CIFTI_KILAVUZU` Kafiye Çifti Kapısı). **Vaka:** 1.

**Gözlem:** Filmin kapanış sahnesi S10 (01:29), başlangıç karesi S1'deki kamera kurulumu Setup A'ya (EWS eye-low çöl düzlüğü) dönmek yerine tamamen yeni bir Setup J açı/kadrajı ve gece atmosferi kullanarak görsel döngü/kafiye yapısını kırmıştır (RHYME BROKEN).

**Çözüm Hipotezi:** Kapanış karesi için video promptu yazılırken ilk sahnenin tüm kamera parametreleri (kadraj yüksekliği, lens açısı, monolit çapalaması) veritabanından `Setup A` olarak birebir kopyalanmalı, yalnızca zaman/ışık değişkeni (`nighttime lighting`) güncellenmelidir.

🔗 [[D184]] · [[D194]]

---

## ✅ ADAY-26 — ŞOK PATLAMALARINDAN SONRA DÜZ BEDEN SIFIRLANMASI VE İYİLEŞME DURUŞU EKSİKLİĞİ (ABRUPT POSTURE RESET)

**DURUM:** → D207 · K2 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod 10 (Oyunculuk / Beden Dili — Mod V): 5.9/10 — `00:57 - 01:03 (S12 to S13) sudden reset from explosive spark blast to calm standing posture erases physical aftermath (Pattern ⑧)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Beden Dili ve İyileşme Kapısı). **Vaka:** 1.

**Gözlem:** S12'de (00:57) elektrik patlamasına karşı koluyla yüzünü siper eden astronot, bir sonraki cut olan S13'te (01:03) anında kurgusal sıfırlama (abrupt reset) yaşayarak sakin bir manken duruşuna geçmekte, patlamanın fiziksel artçı sarsıntısını (posture tremor, residual slouch) bedeninde taşımamaktadır.

**Çözüm Hipotezi:** Patlama ve travma içeren sahnelerin hemen ardından gelen kesmede açılış karesine en az 1 saniyelik sarsıntı ataleti veya hafif bükülme duruşu (`residual posture recoil`) eklenmelidir.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-27 — KESMELERDE PLANSIZ IŞIK BÖLGESİ VE RENK SICAKLIĞI ZIPLAMALARI (LIGHT JUMP / ZONE BROKEN)

**DURUM:** → D193 TEKRAR · K4 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod 11 (Işık / Plan Sadakati — Mod V): 7.7/10 — `00:59 Cut 6 (S6->S7), 01:19 Cut 8 (S8->S9), 01:29 Cut 9 (S9->S10) abrupt jumps between 6500K daylight overcast sky and deep night ambient (Verdict: ZONE BROKEN)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Işık Takvimi Kapısı). **Vaka:** 1.

**Gözlem:** Kesmeler arasında ortam ışığı planlı bir geçiş olmaksızın anlık olarak gündüz mavi-gri sky ile gece yıldızlı sky arasında 3 kez sıçramış (Cut 6, Cut 8, Cut 9), pozlama ve renk sıcaklığında (6500K ↔ 2200K) sert tranzisyon hatası yaratmıştır (ZONE BROKEN).

**Çözüm Hipotezi:** Sahneler arası ışık takvimi ve renk sıcaklığı plan seviyesinde kilitlenmeli, gece/gündüz zıplaması oluşmaması için retrolarda sky replacement ve color grade eşitlemesi uygulanmalıdır.

🔗 [[D6]] · [[D176]] · [[D193]]

---

## ✅ ADAY-28 — TEKNİK PANEL İTKİLERİNDE DÜZ TEMPO VE ERKEN İZLEYİCİ TERKİ (RETENTION DROP-OFF AT 00:21)

**DURUM:** → D211 · K8 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_AMBER_LATTICE QA (10.09.2026) — Mod 12 (Hook & Retention — Mod V): 6.5/10 — `00:05-00:37 (S2-S7) repeated console and wiring interactions plateau, predicting retention drop-off at 00:21 s (Verdict: LEAVES AT 00:21 s)`.
**KAPI:** aday — muhtemel LİSTE (`HOOOK_VE_ILK_SAHNE_KILAVUZU` Tutundurma Kapısı). **Vaka:** 1.

**Gözlem:** S2 ile S7 arasındaki 32 saniyelik blokta üst üste konsol/kablo bypass işlemleri gösterilmiş; aksiyon risk seviyesi ve görsel ölçek değişmediği için izleyici tutundurma eğrisi 00:21. saniyede platoya girerek terk tahmini (LEAVES AT 00:21 s) almıştır.

**Çözüm Hipotezi:** Açılış 10 saniyesinde merak sorusu posed edildikten sonra 00:15-00:30 aralığında durağan panel kurcalama sahneleri elenmeli, doğrudan yüksek risk içeren sahneye (generator core extraction) geçilmelidir.

🔗 [[D4]] · [[D12]]

---

## ✅ ADAY-29 — ASTRONOT ELBİSE RENGİ SIÇRAMASI VE AMBLEM IŞINLANMASI (COSTUME COLOR & PATCH TELEPORTATION)

**DURUM:** → D208 · K6 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 2 (Kostüm Kimliği / Devamlılık): 2.0/10 — `0:00 (S1) black suit vs 0:20 (S3) white suit, patches migrate between shoulders and backpack (Verdict: DRIFTS BUT RECOVERABLE)`.
**KAPI:** aday — muhtemel LİSTE (`SAHNE_DEVAMLILIK_KILAVUZU` Kostüm Kimliği Kapısı). **Vaka:** 1.

**Gözlem:** Astronot elbisesi sahneler arasında siyah ve beyaz renk arasında rastgele zıplamakta (S1, S2, S4, S5, S8, S9, S10 siyah ↔ S3, S6, S7, S11, S12 beyaz); amblem/yamalar (Mavi üçgen, US Flag, ESA logosu) omuzlar, ön kol ve sırt çantası arasında ışınlanmaktadır.

**Çözüm Hipotezi:** Karakter kostüm rengi ve amblem konumları prompt seviyesinde `COSTUME LOCK` olarak kilitlenmeli, retrolarda renk düzeltme (color grading) veya re-generation ile siyah/koyu gri suit kıvamına getirilmelidir.

🔗 [[D3]] · [[D10]] · [[D127]]

---

## ✅ ADAY-30 — TAMİR EDİLMİŞ VİZÖR ÇATLAĞININ FİNAL KAREDE MÜKEMMEL GOLD VİZÖRLE DEĞİŞMESİ (VISOR DAMAGE RESET)

**DURUM:** → D208 · K6 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)
> ⚠️ 14.09.2026: bu kayıt 10.09'da kesik yazılmış (Gözlem/Hipotez satırı yok); Kaynak satırı D208'e yetti.

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 3 (Aşınma, Hasar & Yaralanma): 4.0/10 — `1:30 (S10) sealed liquid crystal crack replaced by an intact gold visor in 1:50 (S12) (Verdict: DRIFTS BUT RECOVERABLE)`.
**KAPI:** aday — muhtemel LİSTE (`SAHNE_DEVAMLILIK_KILAVUZU` Aşınma ve Hasar Kapısı). **Vaka:** 1.

🔗 [[D3]] · [[D18]] · [[D43]]

---

## ✅ ADAY-31 — GÖKYÜZÜ VE GÖK CİSİMLERİ SAHNE GEÇİŞLERİNDE SÜREKLİ DEĞİŞİMİ (SKY & CELESTIAL BODY REPLACEMENT)

**DURUM:** → D209 · K5 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod B (Arka Plan & Çevre): 2.0/10 (Sky & Atmospherics) — `0:00 empty space ↔ 0:20 ringed planet ↔ 0:50 small blue planet ↔ 1:50 dual suns orange haze (Verdict: FIELD DRIFTS BUT RECOVERABLE)`.
**KAPI:** aday — muhtemel LİSTE (`UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU` Gökyüzü ve Uzay Kapısı). **Vaka:** 1.

**Gözlem:** Arka plan gökyüzü ve gök cisimleri sahneler arasında tutarsız şekilde sürekli değişmekte (boş siyah uzay ➔ halkalı dev gezegen ➔ küçük mavi gezegen ➔ iki sarı güneşli turuncu atmosfer), tek bir gezegen/yörünge süreklilik hissini kırmaktadır.

**Çözüm Hipotezi:** Çevresel gökyüzü ve gök cisimleri (celestial body position, sky color, sun count) `ENVIRONMENT LOCK` olarak kilitlenmeli, sahneler arası gökyüzü re-generation ile tek yapıya getirilmelidir.

🔗 [[D6]] · [[D176]] · [[D193]]

---

## ✅ ADAY-32 — ARAZİ TOPOLOJİSİ VE ATMOSFER ZIPLAMASI (TOPOLOGY & ATMOSPHERE JUMP)

**DURUM:** → D209 · K5 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod B (Arka Plan & Çevre): 5.0/10 (Horizon & Topology) — `0:00 vs 1:50 airless jagged rocks jump to sprawling canyon plains under orange atmosphere (Verdict: FIELD DRIFTS BUT RECOVERABLE)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Arazi Topolojisi Kapısı). **Vaka:** 1.

**Gözlem:** S1-S11 boyunca dar, havasız, mor/koyu gri pürüzlü kayalık alan gösterilirken, S12'de karakter aniden atmosferik turuncu puslu, uçsuz bucaksız kanyon ovasına (sweeping canyon plains) ışınlanmış, topoloji bütünlüğü bozulmuştur.

**Çözüm Hipotezi:** Sahne lokasyon topolojisi ve atmosfer varlığı script seviyesinde kilitlenmeli, S12 arka planı S1'in havasız kayalık tepesine sadık kalınarak re-generate edilmelidir.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-33 — AKSİYON ELİPSİ VE NESNE FAZ ÇELİŞKİSİ (ACTION ELLIPSIS & STAKES OBJECT PHASE DRIFT)

**DURUM:** → D213 · K11 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 7 (Aksiyon Okunurluğu Derin Tarama): 9.0/10 — `1:19 floating liquid orb vs 1:21 solid crystal shard pressed to visor glass (Verdict: ACTION READS)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Aksiyon Okunurluğu Kapısı). **Vaka:** 1.

**Gözlem:** Doruk mühürleme sahnesinde S8 (1:19) kristalin eriyerek el üzerinde yüzen sıvı bir küreye dönüştüğünü gösterirken, S9'da (1:21) kesme sonrası karakter kask vizörüne katı kristal bir parça bastırmaktadır (sıvı ↔ katı faz çelişkisi ve aksiyon elipsi).

**Çözüm Hipotezi:** Nesne faz dönüşümü içeren doruk aksiyonlarında kesme yapılırken nesne fiziksel durumu ve uygulama hareketi kadraj içinde açıkça gösterilmeli (`liquid orb application motion lock`), katı parçaya ani kurgu zıplaması engellenmelidir.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-34 — KASK VİZÖR DIŞ YÜZEYİNE YAPIŞAN BURNED-IN HUD METNİ ARTEFAKTI (BURNED-IN VISOR HUD TEXT)

**DURUM:** → D215 · K13a (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod V (Kare & Fizik - Mod V): 5.3/10 — `0:20 (F1) Burned-in HUD text physically stuck on exterior of visor (Verdict: REGENERATE)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Vizör ve Ekran Kapısı). **Vaka:** 1.

**Gözlem:** S2'de (0:20) kask vizöründeki HUD uyarısı/metni, vizörün iç projeksiyonu gibi davranmak yerine camın dış yüzeyine fiziksel olarak basılmış (burned-in text on glass exterior) yapışık bir artefakt olarak belirmiştir.

**Çözüm Hipotezi:** Prompt negatif bloğuna `burned-in text, exterior glass text, subtitles, overlay watermark` eklenmeli, HUD projelendirmesi iç optik kask ekranı seviyesinde `internal HUD projection` olarak kilitlenmelidir.

🔗 [[D72]] · [[D101]]

---

## ✅ ADAY-35 — YERÇEKİMLİ GEZEGENDE ERİMİŞ SIVININ SIFIR YERÇEKİMLİ ASKIDA KÜREYE DÖNÜŞMESİ UYUMSUZLUĞU (MIXED GRAVITY VECTORS)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod V (Kare & Fizik - Mod V): 5.3/10 — `1:17 (F2) Mixed gravity: liquid sphere floats in a 1g environment, ignoring gravity (Verdict: REGENERATE)`.
**KAPI:** aday — muhtemel LİSTE (`SAVAS_SENARYO_KILAVUZU` Yerçekimi ve Sıvı Fiziği Kapısı). **Vaka:** 1.

**Gözlem:** Astronotun duruşu, yürümesi ve duman yükselmesi 1g yüzey yerçekimi gösterirken (S1-S7), S8'de eriyen kristal sıvısı yerçekiminden tamamen bağımsız davranarak havada yüzen sıfır yerçekimi küresi (`zero-g floating liquid orb`) oluşturmuş, kadrajda zıt yerçekimi vektörleri (mixed gravity) yaratmıştır.

**Çözüm Hipotezi:** Uzay elbiseli karakter yüzeyde 1g kütlesiyle hareket ederken nesnelerin sıfır-g davranması istenmiyorsa, eriyen sıvı için `thick viscous liquid dripping down under surface gravity` tarifi kullanılmalıdır.

🔗 [[D37]] · [[D127]]

---

## ✅ ADAY-36 — HAVASIZ VAKUM GÖKYÜZÜ ALTINDA KONVEKTİF DUMAN BACASI YÜKSELMESİ ÇELİŞKİSİ (CONVECTIVE SMOKE IN VACUUM)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 6 (Fizik Derin Tarama): 9.3/10 — `00:00 (L1) Plumes of smoke rise in thick, convective, buoyant columns contradicting vacuum starfield sky (Verdict: MINOR SLIPS)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Atmosfer ve Parçacık Fiziği Kapısı). **Vaka:** 1.

**Gözlem:** S1'de (00:00) uzay kapsülü ve kask sızıntısından çıkan duman, uzayın simsiyah vakum gökyüzü ve yıldızlarına rağmen Dünya benzeri yoğun bir atmosferdeki gibi konvektif baca sütunu şeklinde yukarı doğru süzülmektedir (vakumda duman konveksiyonu çelişkisi).

**Çözüm Hipotezi:** Vakum ve ince atmosfer ortamlarında sızıntı/duman promptları `rapid jet expansion into vacuum, directional gas spray` olarak tanımlanmalı, yükselen duman sütunu kalıbı engellenmelidir.

🔗 [[D37]] · [[D176]]

---

## ✅ ADAY-37 — SIFIR REPLİKSİZ HAYATTA KALMA FİLMİNDE ÜST ÜSTE İNCELEME SAHNELERİYLE URGENCIY/PACING PLATOLAMASI (REDUNDANT ANALYSIS BEATS STALL PACING)

**DURUM:** → D212 · K9 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod H (Hikaye & Anlatı - Mod V): 7.6/10 — `0:50 (S6) & 0:59 (S7) Two consecutive 9-10s shots of staring at crystal stall oxygen clock urgency (Verdict: SHOOT WITH TRIMS)`.
**KAPI:** aday — muhtemel LİSTE (`HOOOK_VE_ILK_SAHNE_KILAVUZU` Kurgu Ritmi ve Oksijen Saati Kapısı). **Vaka:** 1.

**Gözlem:** Oksijen göstergesinin düşüşüyle (S4) zamana karşı yarış kurulmuşken, S6 ve S7'de astronotun 18 saniye boyunca üst üste kristale bakması (wide analysis + CU contemplation) aciliyet ivmesini düşürmüş ve terk riski (retention drop-off) yaratmıştır.

**Çözüm Hipotezi:** Zaman sınırı (ticking clock) kurulan repliksiz kısa filmlerde keşif sonrası inceleme sahneleri tek bir 4-5 saniyelik farkındalık vuruşunda birleştirilmeli (merge S6 & S7 beat), tempoyu durduran ikincil duraklamalar kurguda budanmalıdır.

🔗 [[D4]] · [[D12]]

---

## ✅ ADAY-38 — KRİTİK OKSİJEN SIZINTISINDA SIFIR BEDEN ZORLANMASI VE NEFES DÜZLEŞMESİ (ZERO STRAIN & CALM BREATH UNDER CRITICAL AIR LEAK)

**DURUM:** → D206 · K1 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 8 (Efor & Bedel Derin Tarama): 1.0/10 — `0:10 (E1) calm breathing puffs during critical leak, 1:50 (E5) standing straight erases near-death ordeal (Verdict: NOBODY PAYS)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Efor ve Bedel Kapısı). **Vaka:** 2 (ADAY-24'ün 2. vakası).

**Gözlem:** Kaskında kritik basınca düşen oksijen sızıntısı uyarısı yanan astronotun vizör arkasındaki nefes buğusu son derece sakindir; boğulma tehlikesi atlatıldıktan sonra S11'de (1:50) karakter sıfır efor bedeliyle dik durarak anında baseline'a sıfırlanmıştır (fresh reset).

**Çözüm Hipotezi:** Ölümcül sızıntı/hipoksi sahnelerinde nefes buğusu staccato/hızlı ritme kilitlenmeli (`rapid panicked breath condensation`), kurtuluş finalinde ise karakterin çökmüş/kayaya yaslanmış soluklanma duruşu (`slumped posture catching breath`) verilmelidir.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-39 — AÇILIŞ VE KAPANIŞ KAMERA KURULUM UYUMSUZLUĞU VE KAFİYE ÇİFTİ KIRILMASI (OPENING VS CLOSING SETUP MISMATCH / RHYME BROKEN)

**DURUM:** → D210 · K7 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 9 (Kadraj / Plan Sadakati - Mod V): 2.1/10 — `0:00 (S1) Setup A side-on wide vs 1:40 (S11) Setup H rear wide shatters visual loop (Verdict: RHYME BROKEN)`.
**KAPI:** aday — muhtemel LİSTE (`ACILIS_KAPANIS_CIFTI_KILAVUZU` Kafiye Çifti Kapısı). **Vaka:** 2 (ADAY-25'in 2. vakası).

**Gözlem:** Filmin ilk sahnesi S1 (0:00) yan profil EWS kadrajı (Setup A) ile açılırken, kapanış sahnesi S11 (1:40) arkadan çekilmiş geniş kadraja (Setup H) geçmiş; kafiye çifti (rhyme pair) bozularak dairesel kurgu yapısı kırılmıştır.

**Çözüm Hipotezi:** Kapanış karesi üretilirken açılış karesinin `Setup A` kamera açısı veritabanından kopyalanmalı, yalnızca kaskın mühürlü durumu ve dual sunset ışığı değişkeni güncellenmelidir.

🔗 [[D184]] · [[D194]]

---

## ✅ ADAY-40 — SABİT KADRAJ İSTENDİĞİ HALDE KLİP İÇİNDE İSTENMEYEN YAVAŞ KAYMA/DOLLY SÜRÜKLENMESİ (CREEPING DOLLY / UNPLANNED MOTION)

**DURUM:** → D210 · K7 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 9 (Kadraj / Plan Sadakati - Mod V): 2.1/10 — `6 out of 11 clips feature unmotivated slow push-in, failing lockoff integrity (Verdict: RHYME BROKEN)`.
**KAPI:** aday — muhtemel LİSTE (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU` Kamera Hareketi Kilit Kapısı). **Vaka:** 1.

**Gözlem:** Durağan ve dingin bir kilitli açının (lockoff) beklendiği 11 sahnenin 6'sında (S1, S2, S6, S7, S9, S11) jeneratör model kendiliğinden yavaş bir kameraya yaklaşma (creeping dolly / push-in) hareketi üreterek kadraj stabilitesini bozmuştur.

**Çözüm Hipotezi:** Kamera promptuna `locked-off tripod shot, zero camera movement, completely static frame` ibaresi eklenmeli; hareket gerekmeyen meditasyonel sahnelerde I2V kamera parametresi `motion 0` olarak sabitlemelidir.

🔗 [[D131]] · [[D184]]

---

## ✅ ADAY-41 — ÖLÜM KALIM KARARINDA BEDEN DİLİNDE SIFIR TEREDDÜT VE KARAR SEÇİMİNİN GÖRÜNMEZLİĞİ (INVISIBLE CHOICE / ZERO TREMOR & HESITATION)

**DURUM:** → D202 TEKRAR · K3 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 10 (Oyunculuk / Beden Dili - Mod V): 2.0/10 — `1:20 (S9) applying unknown glowing liquid is performed as a rote task with zero tremor or breath hesitation (Verdict: THE CHOICE IS INVISIBLE)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Beden Dili ve Seçim Anı Kapısı). **Vaka:** 1.

**Gözlem:** Karakterin bilinmeyen yabancı bir parlak sıvıyı yaşam destek kaskının çatlağına sürme gibi ölüm-kalım kumarı olan doruk kararında (S9), ellerinde ve duruşunda hiçbir tereddüt, titreme veya panik görünmemekte; eylem rutin bir temizlik görevi gibi mekanik olarak icra edilmektedir.

**Çözüm Hipotezi:** Kritik seçim anlarında el hareketlerine `hands trembling with hesitation, frozen moment before desperate gamble, rapid heavy breathing` oyunculuk nüansları prompt seviyesinde açıkça yazılmalıdır.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-42 — KESMEDE ANA IŞIK AÇISININ 120 DERECE ZIPLAMASI VE YÜZ GÖLGELERİNİN TERSİNE DÖNMESİ (KEY LIGHT FLIP 10 O'CLOCK ↔ 2 O'CLOCK)

**DURUM:** → D193 TEKRAR · K4 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 11 (Işık / Plan Sadakati - Mod V): 8.7/10 — `01:30 (S10) key light direction flips 120° from 10 o'clock to 2 o'clock across cut S9→S10, inverting facial shadows (Verdict: KEY WALKS)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Işık Takvimi ve Açı Kapısı). **Vaka:** 1.

**Gözlem:** S9'dan S10'a geçerken (01:30) ana güneş ışığı kaynağı saat 10 yönünden (üst sol) saat 2 yönüne (üst sağ) 120 derece zıplamış; karakterin yüzündeki ana gölge yanağı aniden sağdan sola evrilerek (shadow density flip) görsel sıçrama yaratmıştır.

**Çözüm Hipotezi:** Aynı lokasyon/bölgede geçen sahneler için ana ışık yönü `key light angle locked at 10 o'clock high` olarak kilitlenmeli, kesmelerde piksel seviyesinde ışık terslenmesi engellenmelidir.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-43 — VAKUM ORTAMINDA GAZ SIZINTISINDA HACİMSEL IŞIK SAÇILMASI VE BLOOM ARTEFAKTI (VOLUMETRIC LIGHT SCATTER IN VACUUM)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 11 (Işık / Plan Sadakati - Mod V): 8.7/10 — `00:10 & 01:20 (S2 & S9) venting gas displays soft volumetric light scattering and bloom despite vacuum medium (Verdict: KEY WALKS)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Vakum ve Işık Saçılması Kapısı). **Vaka:** 1.

**Gözlem:** Uzayın havasız vakum ortamında geçen S2 ve S9 sahnelerinde kask sızıntı gazı, ortamda atmosferik hava varmış gibi yumuşak hacimsel ışık saçılması (volumetric light scatter) ve aşırı glow/bloom sergilemektedir.

**Çözüm Hipotezi:** Vakum uzay sahnelerinde ışık/gaz etkileşimleri prompt negatif bloğuna `volumetric atmospheric scatter, soft haze, bloom glow` eklenerek sert ışık kırılmalarına (`sharp directional light, hard shadows`) kilitlenmelidir.

🔗 [[D6]] · [[D37]]

---

## ✅ ADAY-44 — GİRİŞ 30 SANİYESİNDE ÜST ÜSTE KURULUM SAHNELERİYLE İZLEYİCİ TERK RİSKİ (RETENTION DROP-OFF AT 00:27 S)

**DURUM:** → D211 · K8 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_CRACKED_HELMET QA (10.09.2026) — Mod 12 (Hook & Retention - Mod V): 6.6/10 — `00:27 s drop-off prediction due to pacing plateau across 4 consecutive setup shots (Verdict: LEAVES AT 00:27 s)`.
**KAPI:** aday — muhtemel LİSTE (`HOOOK_VE_ILK_SAHNE_KILAVUZU` Tutundurma Kapısı). **Vaka:** 2 (ADAY-28'in 2. vakası).

**Gözlem:** İlk 30 saniyelik kurgu penceresinde 4 adet üst üste orta tempolu kurulum ve mekanizma sahnesi sıralanmış; görsel tehdit ve fiziksel eylem geciktiği için izleyici tutundurma eğrisi 00:27. saniyede platoya girerek terk riski almıştır.

**Çözüm Hipotezi:** Kurgu hattında ilk 15 saniyede merak sorusu tetiklendikten hemen sonra orta tempolu kurulum sahneleri budanmalı, doruk aksiyon vuruşu veya görsel nesne dönüşümü doğrudan öne çekilmelidir.

🔗 [[D4]] · [[D12]]

---

## ✅ ADAY-45 — EKRANDA OYNATIM SIRASINDA YAZI/BAŞLIK METNİ GÖRÜNMESİ VE NO-TEXT KURALI İHLALİ (BURNED-IN TITLE TEXT / NO-TEXT RULE BLOCKER)

**DURUM:** → D215 · K13a (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod V (Kare & Fizik - Mod V): 5.3/10 — `1:50 — Burned-in title text ("THE RING WALKER") appears on screen, violating series no-text rule (Verdict: REGENERATE / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`POLITIKA_VE_URETILEBILIRLIK_KILAVUZU` Jeneratör Metin Engeli Kapısı). **Vaka:** 1.

**Gözlem:** Klip/film final karesinde (1:50) ekranda "THE RING WALKER" başlık metni belirmiş (burned-in title text), serinin ekranda yazı bulundurmama (no-text rule) kuralını doğrudan ihlal ederek BLOCKER seviyesinde red almıştır.

**Çözüm Hipotezi:** Video ve kare promptlarının negatif bloğuna `text, title text, burned-in font, subtitles, captions, typography, signature` terimleri kilitlenmeli, jeneratör modelin video üzerine yazı basması tamamen engellenmelidir.

🔗 [[D21]] · [[D161]]

---

## ✅ ADAY-46 — AYNI ORTAMDA ÇİFTE YERÇEKİMİ VE ZIT PARÇACIK VEYA SIVI FİZİĞİ ÇELİŞKİSİ (DUAL GRAVITY READ & CONTRADICTORY PARTICLE DYNAMICS)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod V (Kare & Fizik - Mod V): 5.3/10 — `0:08 vs 1:08 Sand pours at 1g speed, while meteor splash at 1:14 produces low-g fluid droplet behavior; 1:05 particles rise upwards against gravity (Verdict: DRIFTS)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Yerçekimi ve Parçacık Dinamiği Kapısı). **Vaka:** 1.

**Gözlem:** Aynı ay yüzeyi ortamında kum akışı 1g hızında gerçekleşirken, meteor etkisindeki sıvı damlacıkları düşük yerçekimi (low-g) akışkan davranışı sergilemekte; 1:05 saniyesinde ise parlayan tanecikler kum aşağı düşerken yukarı doğru yükselerek fiziksel çelişki üretmektedir.

**Çözüm Hipotezi:** Vakum ve düşük yerçekimli ortamlarda parçacık ve sıvı hareketleri tekil bir yerçekimi vektörüne kilitlenmeli, promptta `consistent low-gravity settling, uniform particle physics, downward particle vector` belirtilmelidir.

🔗 [[D7]] · [[D37]]

---

## ✅ ADAY-47 — DİKİŞ/AMBLEM YAMA POZİSYONUNUN KESMEDE SAĞ/SOL OMUZA MİRORLANMASI VE AKS İHLALİ (PATCH MIRRORING ACROSS CUTS)

**DURUM:** → D208 · K6 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod D (Devamlılık & Kimlik): 7.4/10 — `0:59 (S11) Circular blue mission patch appears on right upper shoulder panel, previously on left shoulder in S02, S04, S06 (Verdict: DRIFTS BUT RECOVERABLE)`.
**KAPI:** aday — muhtemel LİSTE (`SAHNE_DEVAMLILIK_KILAVUZU` Karakter Kıyafet Çapası Kapısı). **Vaka:** 1.

**Gözlem:** Karakterin sol omuz panelinde kilitlenmiş olan dairesel mavi görev amblemi, S11 (0:59) kesmesinde jeneratör simetrisi nedeniyle aniden sağ omuz paneline aynalanarak costume identity tutarsızlığı yaratmıştır.

**Çözüm Hipotezi:** Karakter referans paketinde kıyafet yamaları ve amblemler asymmetric anchor kuralı gereğince strictly fixed side (`circular blue patch strictly on LEFT upper shoulder`) olarak tanımlanmalı ve aksi yöndeki dikişler prompt negatif bloğuna eklenmelidir.

🔗 [[D1]] · [[D15]]

---

## ✅ ADAY-48 — DRAMATİK ANLARDA DENSE SOUNDTRACK CLIFF VE 5 KATMANLI SES YIĞILMASI (SOUNDTRACK LAYER OVERCROWDING & FREQUENCY CLUTTER)

**DURUM:** → D216 · K13b (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod A (Ses & Akustik): 8.1/10 — `00:33, 00:50, 01:22 active sound layer count rises to 5, exceeding the pipeline cap of 3-4 layers and causing frequency clutter under machine dialogue (Verdict: PASS WITH MINOR REVISIONS)`.
**KAPI:** aday — muhtemel LİSTE (`SES_VE_DIYALOG_URETIM_KILAVUZU` Ses Katman ve Frekans Hiyerarşisi Kapısı). **Vaka:** 1.

**Gözlem:** Doruk tırmanma noktalarında (00:33, 00:50, 01:22) aktif ses katmanı sayısı (AI Voice, Siren, Steam Vent, Sub Hum, Synth Pad) 5'e yükselmiş, hat üst sınırı olan 3-4 katmanı aşarak ana diyalog bandı altında frekans kargaşasına yol açmıştır.

**Çözüm Hipotezi:** Kurgu miksinde eşzamanlı aktif ses katmanı sayısı kesin olarak 3-4 katman ile sınırlandırılmalı, yapay zekâ ses bandı (1 kHz - 3 kHz) etrafındaki çakışan synth riser ve alarm efektleri otomatik ducking ve çentik filtreleme ile bastırılmalıdır.

🔗 [[D3]] · [[D171]]

---

## ✅ ADAY-49 — HİKÂYE AKIŞINDA TEKRARLAYAN GÖZLEM VE YÜRÜYÜŞ SAHNELERİYLE ORTA BÖLÜM TEMPO DURGUNLUĞU (REDUNDANT OBSERVATION BEATS & PACING STALL)

**DURUM:** → D212 · K9 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod H (Hikaye): 5.4/10 — `S3, S5, S9 perform identical dramatic functions—showing astronaut staring upward in awe without narrative complication (Verdict: PACING STALLED)`.
**KAPI:** aday — muhtemel LİSTE (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU` Sahne Ritmi Kapısı). **Vaka:** 1.

**Gözlem:** 114 saniyelik kurgu hattında S3, S5 ve S9 sahneleri üst üste benzer yürüyüş ve uzaya hayranlıkla bakma eylemlerini tekrarlamakta, hikâyeye yeni bir engel, tehlike veya karar noktası eklemediği için 0:20-0:45 saniyeleri arasında tempo duraksamaktadır.

**Çözüm Hipotezi:** Üst üste gelen gözlem sahneleri tek bir vuruşta birleştirilmeli, ikinci yürüyüş beat'i yerine numunenin beklenmeyen bir tepki vermesi veya bir uyarı sinyalinin tetiklenmesi gibi narrative complication öne çekilmelidir.

🔗 [[D4]] · [[D12]]

---

## ✅ ADAY-50 — KAMERA KAYMASINDA ARKA PLANIN TEK KATMANLI 2D LEVHA GİBİ SÜRÜKLENMESİ VE PARALLAX YİTİMİ (FLAT SINGLE-PLATE PARALLAX & CARDBOARD DEPTH ERROR)

**DURUM:** → D209 · K5 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 5 (Arka Plan - Derin Tarama): 7.3/10 — `0:17–0:20 (S04) midground rocks and far mountain ridge displace at exact same angular velocity as one flat 2D plate (Verdict: FIELD DRIFTS)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Derinlik ve Parallaks Kapısı). **Vaka:** 1.

**Gözlem:** S04 sahnesinde yanal kamera takibi sırasında uzak dağ silsilesi ile ön plandaki kayalar aynı açısal hızda hareket ederek derinlik hissini yok etmiş ve arka planın karton maket (2D cutout) gibi görünmesine yol açmıştır.

**Çözüm Hipotezi:** Yanal hareket içeren kamera promptlarında arka plan derinliği multi-plane parallax kilitleriyle (`distinct multi-layer depth displacement, distant horizon parallax lag`) tanımlanmalı veya kadraj %15 kırpılarak kenar sürüklenmesi azaltılmalıdır.

🔗 [[D6]] · [[D131]]

---

## ✅ ADAY-51 — AYNI MEKÂNDA DÜŞEN DEBRİS HIZININ DEĞİŞEREK ÇİFTE YERÇEKİMİ HESAPLANMASI (LOCALIZED GRAVITY FLOAT & DRIFT IN FREE FALL)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 6 (Fizik - Derin Tarama): 7.7/10 — `00:49 (L7) fragment drop yields g ≈ 4.94 m/s² vs internal baseline 9.7 m/s² in surrounding shots (Verdict: TWO GRAVITIES / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Serbest Düşüş ve Yerçekimi Kapısı). **Vaka:** 1.

**Gözlem:** 00:33, 00:42 ve 01:12 sahnelerinde serbest düşüş yerçekimi 9.7 m/s² olarak kilitlenmişken, 00:49 sahnelerindeki yıkıntı parçası düşüşü 4.94 m/s² olarak hesaplanmış ve yapay bir sinematik süzülme (cinematic float) oluşturmuştur.

**Çözüm Hipotezi:** Aynı iç mekân/ana sahne bloğunda düşen nesnelerin ivmesi sabit bir yerçekimi katsayısına kilitlenmeli, promptta `realistic heavy free fall gravity, zero artificial floatiness` vurgulanmalı veya montajda klip hızı 1.4x artırılarak süre 1.28 saniyeye çekilmelidir.

🔗 [[D7]] · [[D37]]

---

## ✅ ADAY-52 — GÖRSEL METEOR DÜŞÜŞÜ VEYA TEHDİT ANINDA REAKSİYON VEYA TRAJEKTORİ ANININ EKSİKLİĞİ (THREAT VECTOR APPROACH & STARTLE LAG)

**DURUM:** → D202 TEKRAR · K3 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 7 (Aksiyon): 8.3/10 — `00:32 (B7) meteorite trajectory appears close to contact distance with brief approach; astronaut reaction lacks startle (Verdict: ACTION READS WITH MINOR SLIPS)`.
**KAPI:** aday — muhtemel LİSTE (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU` Tehdit Vektörü Kapısı). **Vaka:** 1.

**Gözlem:** B7 (00:32) sahnesinde düşen meteoritin gökyüzündeki yaklaşma çizgisi (trajectory approach line) kadrajda yeterince kurulmadan aniden yere yakın bölgede belirmiş, astronotun beden dili ise yanı başında gerçekleşen çarpmaya karşı fiziksel irkilme tepkisi üretmemiştir.

**Çözüm Hipotezi:** Tehdit anlarında çarpmadan önce en az 6-12 karelik `high-frame meteor entry streak` yaklaşma vuruşu eklenmeli, astronot beden aksiyonuna `sudden startle, protective arm lift, body recoil` oyunculuğu eklenmelidir.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-53 — AĞIR SIFIRT HAKİKİ KILIF VEYA GÖREV YÜKÜ TAŞINIRKEN BEDEN DURUŞUNDA AĞIRLIK HİSSİZLİĞİ (EFFORTLESS HEAVY & SUIT SKELETON DRIFT)

**DURUM:** → D206 · K1 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 8 (Efor): 6.7/10 — `1:30 (S16) carrying large suit pack along narrow ridge produces zero posture tilt, leg wobble or center-of-gravity compensation (Verdict: WEIGHTLESS WORK)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Beden Bedeli Kapısı). **Vaka:** 1.

**Gözlem:** S16 (1:30) sahnesinde astronot dar dağ sırtında ağır sırt çantasını taşırken beden omurgasında hiçbir eğilme, bacak adım torku veya ağırlık merkezi telafisi (center-of-gravity tilt) görünmemekte, kıyafet/yük ağırlıksız (weightless) durmaktadır.

**Çözüm Hipotezi:** Ağır ekipman ve astronot kıyafeti içeren aksiyonlarda prompt seviyesinde `heavy suit inertia, spine posture forward tilt under back load, deliberate heavy footsteps` eklenmeli, yük taşıma fiziği beden duruşuna yansıtılmalıdır.

🔗 [[D8]] · [[D15]]

---

## ✅ ADAY-54 — AÇILIŞ VE KAPANIŞ SAHNELERİ ARASINDA UÇAK/GEMİ MODELİ DEĞİŞİMİ VE RHYME PAIR ÇÖKÜŞÜ (RHYME PAIR ASSET MORPH & KADRAJ BREAK)

**DURUM:** → D210 · K7 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 9 (Kadraj / Plan Sadakati - Mod V): 4.8/10 — `00:00 (S1) vs 01:05 (S14) Rhyme pair completely fails; lander module morphs from orange/black module ('SAVCI') to silver spaceship in flat desert (Verdict: RHYME BROKEN / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`ACILIS_KAPANIS_CIFTI_KILAVUZU` Açılış/Kapanış Çifti Kilit Kapısı). **Vaka:** 1.

**Gözlem:** S1 açılış karesindeki Setup A (turuncu/siyah lander modülü "SAVCI") ile S14 final karesindeki Setup N (düz çölde duran gümüş uzay gemisi) kamera açısı, araç varlığı ve ortam olarak tamamen uyumsuzlaşmış; açılış-kapanış kafiyesi (rhyme pair) BLOCKER seviyesinde çökmüştür.

**Çözüm Hipotezi:** Filmin açılış ve kapanış kareleri tekil bir referans paketine kilitlenmeli, kapanış sahnesi S1'deki Setup A kamera pozisyonu ve lander varlığı veritabanından çağrılarak `Setup A camera position, exact lander module 'SAVCI'` ile üretilmelidir.

🔗 [[D184]] · [[D194]]

---

## ✅ ADAY-55 — ŞOK/DARBE TEHDİDİ SONRASI DÜZ DURUŞA HIZLI SIFIRLANMA VE REAKSİYON TUTARSIZLIĞI (AFTERMATH RECOVERY RESET & STANCE DRIFT)

**DURUM:** → D207 · K2 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 10 (Oyunculuk): 6.1/10 — `S12 (01:14) impact recoil resets quickly into neutral posture by S13 (01:21) (Verdict: MOSTLY LEGIBLE)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Tepki ve Sonrası Kapısı). **Vaka:** 1.

**Gözlem:** S12 (01:14) sahnesinde meteorit patlamasıyla irkilen astronot, S13'te (01:21) tehlike devam ederken aniden rahat ve nötür bir uzaya bakış duruşuna sıfırlanmış (Pattern ⑧), tehdit sonrası beden dili (aftermath reaction) sürekliliğini kaybetmiştir.

**Çözüm Hipotezi:** Tehdit/şok sahnelerinin hemen ardından gelen kesmede karakter duruşu `caution stance held, rigid posture following shock, steady head tracking toward impact site` şeklinde önceki sahnenin beden dilini taşımalıdır.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-56 — DIŞ MEKÂN SAHNELERİ ARASINDA GÜNEŞ IŞIĞI AÇISI VE RENK SICAKLIĞI DÜZENSİZLİĞİ (EXTERIOR KEY LIGHT DIRECTION WALK & TEMP SEESAW)

**DURUM:** → D193 TEKRAR · K4 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 11 (Işık): 7.0/10 — `0:10–1:39 Zone B key light shifts constantly across cuts (12, 3, 10, 12, 8 o'clock) & temp jumps 6000K → 3000K → 5000K → 2800K (Verdict: KEY WALKS)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Işık Sürekliliği Kapısı). **Vaka:** 1.

**Gözlem:** Dış mekân sekansında (Zone B) ana güneş ışığı açısı sahneler arası saat 12, 3, 10, 12 ve 8 yönlerine zıplamakta, renk sıcaklığı ise 6000K soğuk maviden 2800K sıcak altın rengine dalgalanarak ışık haritası bütünlüğünü bozmaktadır.

**Çözüm Hipotezi:** Aynı dış mekân yürüyüş sekansındaki tüm sahneler için ışık açısı ve renk sıcaklığı `consistent low sun angle from 3 o'clock, locked 4500K daylight balance` olarak prompt seviyesinde kilitlenmeli veya kurguda ortak bir renk derecelendirme (LUT) uygulanmalıdır.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-57 — AÇILIŞTA STATİK METİN KARTI VE JENERİKLE İZLEYİCİ İLK 3 SANİYE TERK RİSKİ (OPENING TITLE CARD RETENTION DROP-OFF AT 00:03 S)

**DURUM:** → D211 · K8 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** THE_RING_WALKER QA (10.09.2026) — Mod 12 (Hook): 6.0/10 — `00:00–00:04 opening window spends 4 seconds on static title typography before scene action begins (Verdict: LEAVES AT 00:03 s / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`HOOOK_VE_ILK_SAHNE_KILAVUZU` İlk 3 Saniye Kapısı). **Vaka:** 1.

**Gözlem:** Videonun ilk 4 saniyesi (00:00–00:04) durağan bir siyah ekran ve jenerik yazısı ile harcanmış, görsel aksiyon ve merak sorusu geciktiği için izleyici akışta henüz sahneyi görmeden (00:03 saniyesinde) videoyu terk etme riski almıştır.

**Çözüm Hipotezi:** Akış (feed) kurgularında açılış metin kartları tamamen kesilmeli, video t=0 anında doğrudan yüksek hareket veya merak görseli içeren sahneyle (`instant action entry at t=0`) başlatılmalıdır.

🔗 [[D4]] · [[D12]]

---

## ✅ ADAY-58 — ALT KADRAJ KENARINDA KENDİLİĞİNDEN BELİREN GÖRSEL NESNE VE ELEMAN SPAWNING (SPONTANEOUS FOREGROUND ELEMENT SPAWNING AT BOTTOM EDGE)

**DURUM:** → D209 · K5 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 1 (Kare - Mod V): 5.4/10 — `00:05 foreground solar array panels spontaneously pop into existence and slide into frame at bottom edge (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Kadraj Kenarı ve Obje Doğma Kapısı). **Vaka:** 1.

**Gözlem:** 00:05 sahnesinde ön plandaki güneş panelleri kadrajın alt kenarında önceden var olmadan aniden belirmiş (spontaneous pop into existence) ve kareden içeri kaymıştır.

**Çözüm Hipotezi:** Kamera takibi veya alt kadraj hareketlerinde ön plan nesneleri prompt kilitlerinde `pre-existing locked foreground elements, zero spontaneous object spawning at camera bounds` şeklinde tanımlanmalı veya kadraj alt sınırı %5 güvenli alana çekilmelidir.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-59 — DERLEME KURGUSUNDA YANLIŞ UYGULANAN KLİP TEKRARI VE TEKRAREN KURGU HATASI (COMPILATION DUP PASS & UNINTENDED SCENE REPETITION LOOP)

**DURUM:** → D212 · K9 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 1 (Kare - Mod V): 5.4/10 — `01:29 Clip repetition error: Greenhouse entry sequence at 01:19 is duplicated verbatim at 01:29 with identical door opening action (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`KURGU_VE_TESLIM_KILAVUZU` Kurgu Tekrar ve Derleme Kapısı). **Vaka:** 1.

**Gözlem:** Serbest derleme kurgusunda 01:19'daki seraya giriş sahnesi 01:29'da birebir aynı kapı açılma aksiyonu ile tekrarlanmış, anlatı döngüsü niyeti olmadan kurgu hatası üretilmiştir.

**Çözüm Hipotezi:** Kurgu aşamasında her sahne kesmesi benzersiz klip kimliğine (`unique clip hash & scene index`) kilitlenmeli, aynı klip pass'ının birleştirme hattına iki kez aktarılması betik denetimi ile engellenmelidir.

🔗 [[D4]] · [[D124]]

---

## ✅ ADAY-60 — ELLERİN GÖĞÜSTE BİRLEŞMESİ ANINDA PARMAKLARIN BİRBİRİNE ERİMESİ VE ŞEKİL BOZULMASI (HANDS-TO-CHEST FINGER FUSION & PALM CONTACT WARPING)

**DURUM:** → D208 · K6 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 1 (Kare - Mod V): 5.4/10 — `01:43 Hands clasped to chest show interlocked fingers warping and fusing into a single mass near knuckles (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Beden ve El Teması Kapısı). **Vaka:** 1.

**Gözlem:** 01:43 sahnesinde karakter ellerini göğsüne kapattığında kenetlenmiş parmaklar boğum bölgesinde birbirine eriyerek kitle hâlinde deforme olmuştur (finger fusion anomaly).

**Çözüm Hipotezi:** Karakter beden dili komutlarında parmakların birbirine kenetlenmesi (`interlocked clasped fingers`) yerine el ayalarının düz temas etmesi (`flat palms resting against chest suit plate, separated finger contours`) istenmeli, negatif bloğa `fused knuckles, finger morphing` eklenmelidir.

🔗 [[D1]] · [[D15]]

---

## ✅ ADAY-61 — SAHNELER ARASI AKTÖR VE YÜZ AMBLEMİ DEĞİŞİMİ VE İZ HOPPING (MULTI-CUT ACTOR IDENTITY MORPHING & FACE MARK HOPPING)

**DURUM:** → D208 · K6 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 2 (Devamlılık): 5.1/10 — `S2, S10, S24, S29 show completely different faces/eyes/skin tones; face smudges jump right to left cheek across S7/S8 (Verdict: IDENTITY BREAK / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SAHNE_DEVAMLILIK_KILAVUZU` Karakter Yüz ve İz Çapası Kapısı). **Vaka:** 1.

**Gözlem:** S2, S10, S24 ve S29 sahneleri arasında oyuncunun yüz kemik yapısı, göz rengi ve ten tonu radikal şekilde değişmiş; S7'de sağ yanakta olan kir izi S8'de sol yanağa zıplamıştır.

**Çözüm Hipotezi:** Karakter referans paketinde yüz anatomisi ve izler `strictly anchored right cheek smudge, face embedding seed match` ile kilitlenmeli, sahneler arası yüz haritası denetimi yapılmalıdır.

🔗 [[D1]] · [[D146]]

---

## ✅ ADAY-62 — ARDIŞIK SAHNELERDE KASK TAKMA/ÇIKARMA HIZLI FLICKER'I VE KİR RESETLENMESİ (CONSECUTIVE CUT HELMET STATE FLICKER & WEAR RESET)

**DURUM:** → D208 · K6 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 2 (Devamlılık): 5.1/10 — `S18 helmet sealed -> S21 helmet off -> S23 helmet sealed -> S24 helmet off; face smudges reset to clean in S14 (Verdict: IDENTITY BREAK)`.
**KAPI:** aday — muhtemel LİSTE (`SAHNE_DEVAMLILIK_KILAVUZU` Kıyafet ve Ekipman Eylemliliği Kapısı). **Vaka:** 1.

**Gözlem:** S18 ile S24 sahneleri arasında kask 4 sahne boyunca takılı ve çıkarılmış olarak ardışık zıplamış; S7-S10'da biriken yüz kirliliği S14'te aniden temizlenmiştir.

**Çözüm Hipotezi:** Kask çıkarma/takma aksiyonları bir geçiş sahnesi (`physical helmet removal action beat`) gösterilmeden değiştirilmemeli; yıpranma tek yönlü kuralı (`one-way wear progression`) gereği yüz ve kıyafet kiri eylem olmadan sıfırlanmamalıdır.

🔗 [[D1]] · [[D189]]

---

## ✅ ADAY-63 — EKRAN SAYAÇ VE METRİK DEĞERLERİNİN GİDİŞATININ TERSİNE DÜŞMESİ (NON-MONOTONIC DISPLAY PROGRESS METRIC DROP ACROSS CUTS)

**DURUM:** → D151 not · K14 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 2 (Devamlılık): 5.1/10 — `Display metric drops from 78% in S11 down to 19% in S16 before reaching 100% in S26 (Verdict: COUNTER LOGIC)`.
**KAPI:** aday — muhtemel LİSTE (`SAHNE_DEVAMLILIK_KILAVUZU` Ekran ve Obje Metrik Kapısı). **Vaka:** 1.

**Gözlem:** S4 (%42) ve S11 (%78) sahnelerinden sonra S16 sahnesindeki ekran değeri %19'a düşmüş, ardından S26'da %100'e çıkarak zamansal sayaç ilerleyiş mantığını bozmuştur.

**Çözüm Hipotezi:** Arayüz ve ekran grafiklerindeki sayısal metrikler senaryo aşamasında monotonik artan (`strictly monotonic increasing values`) olarak kilitlenmeli, sahneler arası sayaç düşüşleri engellenmelidir.

🔗 [[D7]] · [[D169]]

---

## ✅ ADAY-64 — DİALOGUE REPLİĞİNİN HAREKETSİZ VE KAPALI DUDAK ÜZERİNE OYNAMASI (ON-SCREEN DIALOGUE PLAYING OVER MOTIONLESS MOUTH IN MEDIUM CLOSE-UP)

**DURUM:** → D215 · K13a (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 3 (Ses): 4.3/10 — `01:31 Line 7 plays verbatim while the pilot's mouth remains completely motionless on screen in clear medium close-up (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SES_VE_DIYALOG_URETIM_KILAVUZU` Diyalog ve Dudak Uyum Kapısı). **Vaka:** 1.

**Gözlem:** Line 7 (01:31 "If anyone is monitoring this frequency...") repliği oynarken ekrandaki pilotun dudakları orta yakın planda tamamen hareketsiz kalmış ve ses kaynağı uyumsuzluğu yaratmıştır.

**Çözüm Hipotezi:** Kadrajda yüzü ve dudakları açıkça görünen karakterlerin sesli diyalog sahnelerinde `visible active mouth articulation` zorunlu tutulmalı, diyalog oynarken kapalı duran görüntüler iç ses/comms dışı diyalog olarak işaretlenmemelidir.

🔗 [[D3]] · [[D35]]

---

## ✅ ADAY-65 — SAHNE KESMELERİNDE MEKÂN SESİNİN ANİDEN KESİLMESİYLE DİJİTAL SESSİZLİK BOŞLUĞU (MULTI-FRAME DIGITAL SILENCE HOLE ON SCENE CUTS DUE TO MISSING ROOM TONE BRIDGE)

**DURUM:** → D216 · K13b (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 3 (Ses): 4.3/10 — `01:12 ambient bed drops out completely for 3 frames across the cut, creating an unnatural digital silence hole (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SES_VE_DIYALOG_URETIM_KILAVUZU` Ambiyans ve Kurgu Köprüsü Kapısı). **Vaka:** 1.

**Gözlem:** 01:12 sahne kesmesinde ortam sesi bed'i 3 kare boyunca tamamen sıfırlanmış (digital silence hole), diyalog ve ambiyans arasında keskin ses boşluğu oluşmuştur.

**Çözüm Hipotezi:** Kurguda tüm sahne kesmelerinin altına en az -28 dB seviyesinde kesintisiz oda tonu/ambiyans köprüsü (`continuous room tone audio bridge across cuts`) döşenmeli, tam dijital sıfır seviyesine düşüşler engellenmelidir.

🔗 [[D3]] · [[D171]]

---

## ✅ ADAY-66 — EKRANDAKİ FİZİKSEL ZORLANMA VE SARSINTININ SAKİN SES PERFÖRMANSIYLA ÇAKIŞMASI (PHYSICAL EXERTION STRAIN ON SCREEN MISMATCHED WITH CALM SEDENTARY VOCAL PROFILE)

**DURUM:** → D216 · K13b (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 3 (Ses): 4.3/10 — `02:44 Character is physically straining with controls against violent shaking, yet vocal delivery sounds calm and sedentary (Verdict: DELIVERY MISMATCH)`.
**KAPI:** aday — muhtemel LİSTE (`SES_VE_DIYALOG_URETIM_KILAVUZU` Efor ve Ses Eşleşmesi Kapısı). **Vaka:** 1.

**Gözlem:** 02:44 sahnesinde karakter panik ve şiddetli sarsıntı altında kumandalarla fiziksel olarak mücadele ederken ses seslendirmesi son derece sakin, meşgulsüz ve masa başı tonunda duyulmaktadır.

**Çözüm Hipotezi:** Yüksek efor ve sarsıntı içeren sahnelerde ses üretimi promptlarında `breath strain, heavy vocal effort, trembling pitch modulation under physical shaking` parametreleri eklenmeli, efor görseli ile ses uyumlaştırılmalıdır.

🔗 [[D3]] · [[D169]]

---

## ✅ ADAY-67 — TEKRARLAYAN SERA GİRİŞ KUTUSU VE GEREKSİZ GEÇİŞ SAHNELERİYLE TEMPO AKSAMASI (REPETITIVE GREENHOUSE DOOR ENTRANCE BEATS & REDUNDANT TRANSITION SCENES)

**DURUM:** → D212 · K9 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 4 (Hikaye): 7.8/10 — `S9 (1:19) and S10 (1:29) repeat exact same greenhouse doorway entrance; S14 duplicates corridor walking beats (Verdict: PACING DROPS / RETENTION RISK)`.
**KAPI:** aday — muhtemel LİSTE (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU` Sahne Çeşitliliği ve Tempo Kapısı). **Vaka:** 1.

**Gözlem:** S9 (1:19) ve S10 (1:29) sahneleri üst üste sera kapısından içeri giriş aksiyonunu tekrarlamakta, S14 sahnesi ise S4'teki koridor yürüyüşünü yenileyerek anlatı ivmesini düşürmektedir.

**Çözüm Hipotezi:** Benzer geçiş ve kapı giriş sahneleri tekil vuruşa indirgenmeli, tekrarlayan koridor yürüyüşleri kurguda elenerek merkezi karar anına (S12) daha hızlı ulaşılmalıdır.

🔗 [[D4]] · [[D124]]

---

## ✅ ADAY-68 — AÇILIŞTAKİ DURAĞAN PEYZAJ KADRAJIYLA İZLEYİCİ İLK 19 SANİYE TERK RİSKİ (STATIC LANDSCAPE OPENING ESTABLISHING SHOT RETENTION DROP-OFF)

**DURUM:** → D211 · K8 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 4 (Hikaye): 7.8/10 — `0:00–0:19 static opening landscape establishing shot takes 19 seconds before protagonist appears in S2/S3 (Verdict: DELAYED START / RETENTION RISK)`.
**KAPI:** aday — muhtemel LİSTE (`HOOOK_VE_ILK_SAHNE_KILAVUZU` İlk Sahne Kancası Kapısı). **Vaka:** 1.

**Gözlem:** Videonun ilk 19 saniyesi (0:00–0:19) karakter ve durum aksiyonu olmadan durağan çöl/üs peyzaj karesiyle harcanmış, başrol oyuncusu ve kriz 19. saniyede belirmiştir.

**Çözüm Hipotezi:** Genel manzara tanıtım kareleri maksimum 3-4 saniye ile sınırlandırılmalı, karakterin donma ve donuk nefes alma aksiyonu t=3 anına çekilerek kanca güçlendirilmelidir.

🔗 [[D4]] · [[D12]]

---

## ✅ ADAY-69 — VERİCİ VE ANTE KULESİ MİMARİSİNİN SAHNELER ARASI DEĞİŞİMİ VE FORM DEFORMASYONU (TRANSMISSION TOWER ARCHITECTURE MORPHING ACROSS WIDE SHOTS)

**DURUM:** → D209 · K5 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 5 (Arka Plan - Derin Tarama): 5.0/10 — `01:28 (S12) vs 02:02 (S17) vs 02:36 (S22) transmission tower geometry morphs 3 times from lattice frame to solar array to solid spire (Verdict: FIELD DRIFT)`.
**KAPI:** aday — muhtemel LİSTE (`UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU` Yapı ve Kule Anatomi Kapısı). **Vaka:** 1.

**Gözlem:** Filmin ana mimari yapısı olan verici kulesi S12'de kafes kule, S17'de güneş panelli kule ve S22'de masif silindirik kule olarak 3 kez biçim değiştirmiştir.

**Çözüm Hipotezi:** Odak mimari ve kule yapıları tek bir referans kontrol paneline kilitlenmeli, arka plan üretimi `strictly anchored lattice tower geometry` ile yürütülmelidir.

🔗 [[D6]] · [[D131]]

---

## ✅ ADAY-70 — KARLI ZİRVEDEN KURU ÇÖL VADİSİNE ANİ MEKÂN VE ZEMİN DÖNÜŞÜMÜ (INSTANT ENVIRONMENTAL TERRAIN TRANSITION FROM SNOW SUMMIT TO DRY DESERT CANYON)

**DURUM:** → D209 · K5 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 5 (Arka Plan - Derin Tarama): 5.0/10 — `03:00 (S25) snowy mountain summit turns instantly into 03:09 (S27) dry red desert canyon without temporal bridge (Verdict: CONTRADICTION / MAJOR)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Zemin ve Coğrafya Sürekliliği Kapısı). **Vaka:** 1.

**Gözlem:** S25'te kar kaplı dağ zirvesinde olan kule ve zemin, S27'de hiçbir zaman geçişi olmadan aniden kuru kırmızı çöl kanyonuna dönüşmüştür.

**Çözüm Hipotezi:** Çevresel dönüşüm veya zemin değişimi kurguda ara geçiş karesi ile desteklenmeli, kule etrafındaki zemin kaplaması (kar/çöl) sekans boyu kilit tutulmalıdır.

🔗 [[D6]] · [[D189]]

---

## ✅ ADAY-71 — DERİNLİK VE ATMOSFERİK PERSPEKTİFİN TERSİNE DÖNMESİ VE ZITLIK UYUMSUZLUĞU (ATMOSPHERIC PERSPECTIVE INVERSION & REVERSE DEPTH CONTRAST)

**DURUM:** → D209 · K5 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 5 (Arka Plan - Derin Tarama): 5.0/10 — `02:15 (S19) vs 02:38 (S22) atmospheric perspective inverts; distant mountains in S22 are crisper and higher contrast than S19 misty haze (Verdict: FIELD DRIFT)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Atmosferik Sis ve Derinlik Kapısı). **Vaka:** 1.

**Gözlem:** S19'da sisli ve bulanık görünen uzak dağlar, S22 geniş açısında daha net, yüksek kontrastlı ve keskin belirerek gerçekçi derinlik fiziğini bozmuştur.

**Çözüm Hipotezi:** Uzak arka plan katmanlarında mesafe arttıkça kontrast ve netlik `atmospheric haze falloff, depth blur pass` kuralı gereğince azaltılmalı, yapay netlik sıçramaları engellenmelidir.

🔗 [[D6]] · [[D131]]

---

## ✅ ADAY-72 — KABİN İÇİ SERBEST DÜŞÜŞLERDE ÇİFTE YERÇEKİMİ İVMESİ Tutarsızlığı (DUAL GRAVITY ACCELERATION INCONSISTENCY IN CABIN FREE FALLS)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 6 (Fizik - Derin Tarama): 4.6/10 — `01:55 canister drops at g=8.87 m/s² vs 02:41 wrench drops at g=4.13 m/s² (Verdict: TWO GRAVITIES / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Serbest Düşüş Yerçekimi Kapısı). **Vaka:** 1.

**Gözlem:** 01:55 sahnesinde serbest düşen kutu $g = 8.87\text{ m/s}^2$ ivmeyle düşerken, 02:41'de düşen anahtar $g = 4.13\text{ m/s}^2$ ivmeyle süzülmüş; kabin içi çifte yerçekimi hissi yaratmıştır.

**Çözüm Hipotezi:** Aynı kabin içi mekânda düşen tüm nesnelerin serbest düşüş süreleri kurguda hızlandırma/yavaşlatma ile kilit ivme değerine ($g \approx 8.8\text{ m/s}^2$) eşitlenmelidir.

🔗 [[D7]] · [[D37]]

---

## ✅ ADAY-73 — SERBEST ENKAZ VE MALZEMENİN YERÇEKİMSİZ ÇÖZÜLÜMLÜ DÜZ SÜZÜLMESİ (UNACCELERATED CINEMATIC FLOAT DRIFT ON LOOSE DEBRIS)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 6 (Fizik - Derin Tarama): 4.6/10 — `02:22 loose airlock debris drifts horizontally for 2.5 seconds with zero downward gravity acceleration (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Partikül ve Yerçekimi Kapısı). **Vaka:** 1.

**Gözlem:** 02:22 sahnesinde hava kilidinde serbest kalan enkaz parçaları 2.5 saniye boyunca aşağı doğru ivmelenmeden yatay olarak süzülmüştür.

**Çözüm Hipotezi:** Yerçekimli ortamlarda havada süzülen nesnelerin yatay hareketi kesilmeli veya aşağı yönlü düşüş ivmesi dikey vektör komutuyla kilitlenmelidir.

🔗 [[D7]] · [[D39]]

---

## ✅ ADAY-74 — PNÖMATİK KAPI KAPANMA HIZININ ARDIŞIK KESMELERDE YARIYA DÜŞMESİ (PNEUMATIC DOOR CLOSURE RATE DRIFT ACROSS CONSECUTIVE SHOTS)

**DURUM:** → D200 TEKRAR · K10 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 6 (Fizik - Derin Tarama): 4.6/10 — `02:10 bulkhead door closes at 1.50 m/s in shot 1, then slows to 0.75 m/s in shot 2 (Verdict: RATE DRIFT / MAJOR)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Mekanik Hareket Hızı Kapısı). **Vaka:** 1.

**Gözlem:** 02:10 sahnesinde 1.50 m/s hızla kapanan zırhlı kapı, 02:18'deki devam sahnesinde 0.75 m/s hıza yavaşlayarak 2 kat hız sapması göstermiştir.

**Çözüm Hipotezi:** Mekanik ve pnömatik hareket içeren sahnelerin ardışık kesmelerinde hareket hızı ($v$) sabit tutulmalı, kurguda ikinci sahne kırpılarak kapanma süresi eşcellenmelidir.

🔗 [[D7]] · [[D124]]

---

## ADAY-75 — ÇARPMADA SÜRÜCÜ VE BEDEN HAREKETİNİN İNERŞİYEL EYLEMSİZLİK UYUMSUZLUĞU (BIOMECHANICAL INERTIAL DISCONNECT DURING IMPACT DECELERATION)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 6 (Fizik - Derin Tarama): 4.6/10 — `03:25 pilot body exhibits zero forward inertia lean during 2.53 g impact deceleration (Verdict: BIOMECHANICS BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Biyomekanik ve Darbe Eylemsizliği Kapısı). **Vaka:** 1.

**Gözlem:** 03:25 sahnesindeki 2.53g çarpma yavaşlamasında pilotun gövdesi emniyet kemerine doğru öne yatmadan kask ve omurgası dik ve hareketsiz kalmıştır.

**Çözüm Hipotezi:** Ani yavaşlama ve çarpma sahnelerinde pilot beden dili komutuna `forward torso whip inertia, neck strain against harness deceleration` eklenerek darbe fiziği bedene yansıtılmalıdır.

🔗 [[D7]] · [[D169]]

---

## ✅ ADAY-76 — KONSOL ŞALTERİNE DOKUNMA EYLEMİNDE MEKANİK DEĞİŞİM BELİRSİZLİĞİ VE İZOLASYON EKSİKLİĞİ (AMBIGUOUS CONSOLE TOGGLE SWITCH ENGAGEMENT & UNCLEAR MECHANICAL CONTACT)

**DURUM:** → D213 · K11 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 7 (Aksiyon): 8.6/10 — `01:50–01:58 (S12 B9): Commitment and contact are rendered, but mechanical switch state change outcome is left ambiguous (Verdict: MINOR SLIP)`.
**KAPI:** aday — muhtemel LİSTE (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU` Aksiyon Belirginliği Kapısı). **Vaka:** 1.

**Gözlem:** S12 (01:50–01:58) sahnesinde karakter parmaklarını metal şalterin üzerine uzatıp dokunmuş, ancak şalterin fiziksel olarak aşağı atlayıp atlamadığı veya sadece tereddüt edilip edilmediği kadrajda net okunmamıştır.

**Çözüm Hipotezi:** Karar ve şalter değiştirme sahnelerinde makro detay kesmesi (`insert macro CU on toggle switch lever snapping down with status LED color shift`) eklenerek aksiyon netleştirilmelidir.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-77 — TEMİZLENEN GÜNEŞ PANELİ MODÜLÜNDE GÖRSEL VE ELEKTRİKSEL GERİ BİLDİRİM EKSİKLİĞİ (UNCLEAR ELECTRICAL/SENSOR FEEDBACK ON DUST-CLEARED PANEL MODULE)

**DURUM:** → D213 · K11 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 7 (Aksiyon): 8.6/10 — `01:10–01:18 (S8 B7): Unclear electrical feedback on ground solar module when dust line is etched (Verdict: MINOR)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Obje Etkileşim ve Geri Bildirim Kapısı). **Vaka:** 1.

**Gözlem:** S8 (01:10–01:18) sahnesinde astronot eldiveniyle güneş paneli üzerindeki tozu çizerek hattı açtığında modül kenarındaki gösterge ışığı veya hücre canlılığında görsel geri bildirim belirmediği için eylemin sonucu belirsiz kalmıştır.

**Çözüm Hipotezi:** Nesne temizleme ve bakım aksiyonlarında temizlenen yüzeyin aktifliğini kanıtlayan mikro görsel tepkiler (`micro LED pulse upon dust clearance, panel grid backlight shift`) prompta eklenmelidir.

🔗 [[D8]] · [[D15]]

---

## ✅ ADAY-78 — MERDİVEN TIRMANMADA BASAMAK VE TUTUNMA EFORUNUN GÖRSELDE İŞLENMEMESİ (WEIGHTLESS LADDER ASCENT & UNPAID FOREARM GRIP EFFORT)

**DURUM:** → D206 · K1 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 8 (Efor): 4.3/10 — `01:45–01:52 (E4): Climbing vertical steel ladder in heavy EVA suit during blizzard shows zero forearm tension, leg drive effort, or rate decay (Verdict: WEIGHTLESS WORK)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Fiziksel Efor ve Tırmanış Kapısı). **Vaka:** 1.

**Gözlem:** S15 (01:45–01:52) sahnesinde astronot fırtına altında ağır uzay giysisiyle dikey çelik merdiveni tırmanırken ön kol gerilimi, bacak itiş eforu, tutunma tereddüdü veya hız düşüşü görünmemiştir.

**Çözüm Hipotezi:** Dikey tırmanış ve ağır yük aksiyonlarında `heavy suit ladder climb, forearm grip tension, slow deliberate rung pulls, visible leg drive exertion` beden dili prompta işlenmelidir.

🔗 [[D8]] · [[D169]]

---

## ✅ ADAY-79 — MEKANİK AYARLAMA EYLEMİNDE GÖVDE VE AĞIRLIK KALDIRACININ KULLANILMAMASI (EFFORTLESS MECHANICAL ADJUSTMENT & NEUTRAL POSTURE UNDER LOAD)

**DURUM:** → D206 · K1 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 8 (Efor): 4.3/10 — `01:59–02:06 (E5): Manually adjusting heavy antenna dish platform performed with relaxed arms lacking torso torque or leverage (Verdict: UNPAID WORK)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Mekanik Kaldıraç ve Efor Kapısı). **Vaka:** 1.

**Gözlem:** S17 (01:59–02:06) sahnesinde astronot verici anten mekanizmasını elle ayarlarken kolları gevşek durmuş, omurgasında hiçbir dönme torku veya ağırlık kaldıracı yükü okunmamıştır.

**Çözüm Hipotezi:** Ağır mekanizma çevirme ve ayarlama aksiyonlarında `torso torque, two-handed mechanical leverage, shoulder drop under mechanism resistance` efor kalıbı zorunlu tutulmalıdır.

🔗 [[D8]] · [[D169]]

---

## ✅ ADAY-80 — SAHNELER ARASI YORGUNLUK DÜZEYİNİN GEÇİŞSİZ ŞEKİLDE ANİDEN SIFIRLANMASI (UNEARNED PHYSICAL RECOVERY & INSTANT RESTED RESET ACROSS CUTS)

**DURUM:** → D207 · K2 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 8 (Efor): 4.3/10 — `02:48 (S24) vs 03:09 (S27): Body resets from severe exhaustion (level 6 slump) to baseline rested state (level 1) without recovery transition (Verdict: UNPAID RECOVERY)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Yorgunluk İlerleyişi ve Dinlenme Kapısı). **Vaka:** 1.

**Gözlem:** S24'te kule dibinde ağır yorgunluk ve soluk soluğa oturma hâlinde olan astronot, S27'de çöl sırtında aniden tamamen dinlenmiş ve dik bir duruşa (level 1) sıfırlanmıştır.

**Çözüm Hipotezi:** Ağır efor sahnelerinin hemen ardından gelen kesmelerde karakter beden dili `lingering physical fatigue, stooped posture from prior effort` ile korunmalı veya arada dinlenme geçişi gösterilmelidir.

🔗 [[D8]] · [[D189]]

---

## ✅ ADAY-81 — AÇILIŞ VE KAPANIŞ KADRAJLARI ARASINDA KAMERA AÇISI VE UFKUN BOZULMASI (RHYME PAIR MISMATCH & CLOSING FRAME HORIZON DUTCH TILT)

**DURUM:** → D210 · K7 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 9 (Kadraj / Plan Sadakati - Mod V): 5.3/10 — `00:05 Setup A vs 04:12 Setup A': Closing frame fails to return to exact camera position of Setup A, introducing unplanned 10° dutch tilt and 12% anchor Y-shift (Verdict: RHYME BROKEN / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`ACILIS_KAPANIS_CIFTI_KILAVUZU` Açılış/Kapanış Çifti Kadraj Kapısı). **Vaka:** 1.

**Gözlem:** S1 açılış karesi Setup A (düz ufuk hattı) ile S6 final karesi Setup A' arasında %12 çapa kayması ve planlanmamış 10° eğik açı (dutch tilt) oluşmuş; kafiye çifti (rhyme pair) bozulmuştur.

**Çözüm Hipotezi:** Kapanış karesi Setup A'ya dönerken açılış karesinin kamera koordinatları ve açı değerleri `locked Setup A camera coordinates, 0° level horizon` olarak kilitlenmeli veya kurguda dijital döndürme ile eşitlenmelidir.

🔗 [[D184]] · [[D194]]

---

## ✅ ADAY-82 — SABİT KADRAJ KLİBİ İÇİNDE PLANSIZ YAVAŞ YAKINLAŞMA KAYMASI (UNPLANNED CREEPING DOLLY PUSH-IN IN LOCKED-OFF CLIP)

**DURUM:** → D210 · K7 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 9 (Kadraj / Plan Sadakati - Mod V): 5.3/10 — `02:50 (S5): Clip begins as a lockoff but develops an unprompted 5% focal push-in over its final 10 seconds (Verdict: CREEPING DOLLY / FAIL)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Sabit Kamera Kilidi Kapısı). **Vaka:** 1.

**Gözlem:** S5 sahnesi sabit tripod lockoff olarak başlamış ancak klibin son 10 saniyesinde yapay zeka modeli plansız %5 odak yakınlaşması (creeping push-in) üretmiştir.

**Çözüm Hipotezi:** Sabit kadraj kilitlerinde kurgu aşamasında NLE stabilizasyonu ile ölçek sabitlenmeli (`scale lock post-pass`) veya hareket başlayan son saniyeler kırpılmalıdır.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-83 — AYNI KAMERA KURULUMUNA DÖNÜŞTE KAMERA YÜKSEKLİĞİ VE ÇAPA YERİ DEĞİŞİMİ (CAMERA ELEVATION & ANCHOR DRIFT ON SETUP RETURN)

**DURUM:** → D210 · K7 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 9 (Kadraj / Plan Sadakati - Mod V): 5.3/10 — `03:30 (S6): Camera returning to Setup A sits lower than its original height in S1, shifting anchor Y-position by 12% (Verdict: RETURN CONSISTENCY FAIL)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Kamera Kurulum Dönüş Kapısı). **Vaka:** 1.

**Gözlem:** S6 sahnesinde Setup A kamera açısına geri dönüldüğünde kamera irtifası S1'deki seviyeden daha aşağı düşmüş ve ana gösterge paneli kadrajda 12% aşağı kaymıştır.

**Çözüm Hipotezi:** Tekrarlayan kamera kurulumlarında (Setup A -> Setup A) kamera yüksekliği ve lens odağı `strict camera height lock relative to pilot seat` ile sabitlenmelidir.

🔗 [[D6]] · [[D184]]

---

## ✅ ADAY-84 — DUYGUSAL DÖNÜŞ SAHNELERİ SONRASI BEDEN YORĞUNLUĞUNUN ANİDEN RESETLENMESİ (POSTURAL FATIGUE RESET ACROSS CUTS IN EMOTIONAL SCENES)

**DURUM:** → D207 · K2 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 10 (Oyunculuk): 5.8/10 — `S17 (02:40) to S21 (03:20): Postural reset across cut S21—fatigue established after greenhouse loss vanishes when manipulating switch (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` Duygusal Beden Dili Kapısı). **Vaka:** 1.

**Gözlem:** S17'de sera kaybının ardından kurulan ağır beden yorgunluğu ve çökmüş duruş, S21'de şaltere dokunurken aniden yok olmuş ve dik duruşa sıfırlanmıştır.

**Çözüm Hipotezi:** Karakter duygusal bedel ödedikten sonraki sahnelerde beden eylemi `residual emotional posture held, slight shoulder slump before control interaction` kuralı ile korunmalıdır.

🔗 [[D8]] · [[D160]]

---

## ✅ ADAY-85 — EKİPMAN HAZIRLIK SAHNELERİNDE NEDENSİZ HAND LIFT VE GENEREK JESTLER (UNPROMPTED HAND LIFT & GENERIC FILLER GESTURES IN SUIT PREP)

**DURUM:** → D202 TEKRAR · K3 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 10 (Oyunculuk): 5.8/10 — `S5 (00:40) generic filler suit adjustment; S19 (03:06) unnatural hand lift toward helmet without external cause (Verdict: FILLER / MINOR)`.
**KAPI:** aday — muhtemel LİSTE (`KARAKTER_VE_DUYGU_KILAVUZU` El ve Amaca Yönelik Jest Kapısı). **Vaka:** 1.

**Gözlem:** S5'te giysi yaka kontrolü amacsız doldurma jesti olarak kalmış, S19'da ise karakter dış fiziksel bir neden olmadan elini havaya kaldırarak işlevsiz aksiyon üretmiştir.

**Çözüm Hipotezi:** El ve kol hareketleri doğrudan amaca kilitlenmeli (`purposeful hand action, no unprompted arm elevation`), amacsız hareketler kurguda kesilmelidir.

🔗 [[D8]] · [[D15]]

---

## ✅ ADAY-86 — GÖKYÜZÜ ELEKTRİK CİHAZI VE ENERJİ IŞINI PRATİK KAYNAĞININ KESMEDE ANİDEN SÖNMESİ (MISSING PRACTICAL SOURCE LIGHT EMISSION ACROSS CUTS)

**DURUM:** → D193 TEKRAR · K4 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 11 (Işık): 4.9/10 — `02:34 (S22) vs 02:41 (S23): Active skyward energy beam practical source is lit in S22 but missing in S23 tower base shot (Verdict: BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Pratik Işık Kaynağı Sürekliliği Kapısı). **Vaka:** 1.

**Gözlem:** S22 geniş açısında gökyüzüne fışkıran masif mavi ışın sahneyi aydınlatırken, S23 kule dibi kesmesinde ışın ve onun çevreye yaydığı pratik mavi ışık (practical fill) aniden yok olmuştur.

**Çözüm Hipotezi:** Kadrajda veya ortamda aktif pratik ışık kaynakları sahneler arası kesmelerde `baked emission & cast cyan fill on ground structures` olarak kilit tutulmalıdır.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-87 — AYNI DIŞ MEKÂNDA GÜNEŞ IŞIĞI AÇISININ RADİKAL ŞEKİLDE ZIPLAMASI (KEY DIRECTION FLIP & LIGHTING WALK IN SAME SETTING)

**DURUM:** → D193 TEKRAR · K4 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 11 (Işık): 4.9/10 — `00:07 (S1) vs 00:14 (S2) vs 00:21 (S3): Key walks from 9 o'clock to 2 o'clock to 10 o'clock in identical red desert setting (Verdict: KEY WALKS / MAJOR)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Işık Açısı ve Gölge Yönü Kapısı). **Vaka:** 1.

**Gözlem:** Aynı kırmızı çöl mekânındaki ardışık sahnelerde (S1-S3) ana ışık kaynağı saat 9, saat 2 ve saat 10 yönlerine sıçramış, gölge yönleri sahneler arası zıplamıştır.

**Çözüm Hipotezi:** Aynı dış mekân yürüyüş sekansında ana güneş açısı `strictly locked 9 o'clock key direction` şeklinde prompt seviyesinde sabitlenmelidir.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-88 — ARDIŞIK SAHNELERDE AŞIRI RENK SICAKLIĞI VE POZLAMA DALGALANMASI (WILD COLOUR TEMPERATURE & EXPOSURE SWINGS ACROSS CONSECUTIVE SHOTS)

**DURUM:** → D193 TEKRAR · K4 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 11 (Işık): 4.9/10 — `02:48 (S24) vs 02:55 (S25) vs 03:09 (S27): Temperature swings wildly from 6500K blue to 2800K orange to 8500K dark twilight across 20s (Verdict: EXPOSURE SWINGS / MAJOR)`.
**KAPI:** aday — muhtemel LİSTE (`SINEMATOGRAFIK_TEKNIK_KILAVUZ` Renk Sıcaklığı ve Pozlama Kapısı). **Vaka:** 1.

**Gözlem:** 20 saniyelik kurgu aralığında renk sıcaklığı 6500K soğuk maviden 2800K sıcak turuncuya, ardından 8500K karanlık alacakaranlığa zıplayarak ton dengesini bozmuştur.

**Çözüm Hipotezi:** Zaman geçişi olmayan sahneler arası renk sıcaklığı zıplamaları kurguda LUT/renk derecelendirme ile dengelenmelidir.

🔗 [[D6]] · [[D176]]

---

## ✅ ADAY-89 — AÇILIŞ STATİK JENERİK VE YAVAŞ AÇILIŞ NEDENİYLE İLK 10 SANİYE KANCA EKSIKLIGI (SLOW OPENING & STATIC TITLE CARD GATE HOOK DELAY)

**DURUM:** → D211 · K8 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 12 (Hook): 5.5/10 — `00:00–00:10 yields NO QUESTION due to title card and routine readouts (Verdict: HOOK MISSING / BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`HOOOK_VE_ILK_SAHNE_KILAVUZU` İlk 10 Saniye Kanca Kapısı). **Vaka:** 1.

**Gözlem:** Videonun ilk 10 saniyesi static jenerik kartı ve rutin gösterge kontrolleri ile harcanmış, izleyiciye ilk 10 saniyede merak sorusu (hook question) sunulamamıştır.

**Çözüm Hipotezi:** Feed kurgularında açılış metin kartları kesilmeli, doğrudan kriz anı veya alarm uyarısı ile başlanmalıdır (`instant threat hook entry at t=0`).

🔗 [[D4]] · [[D12]]

---

## ✅ ADAY-90 — FİNALDE STATİK KARANLIK VE DÖNGÜ MEKANİZMASI EKSİKLİĞİ (MISSING LOOP MECHANISM & STATIC DARKNESS EXIT TAIL)

**DURUM:** → D211 · K8 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Kaynak:** LOW_POWER QA (10.09.2026) — Lens 12 (Hook): 5.5/10 — `04:05–04:15 ends on static darkness without a loop or forward hook (Verdict: EXIT BLOCKER)`.
**KAPI:** aday — muhtemel LİSTE (`FINAL_VE_PAYLASIM_KILAVUZU` Çıkış ve Döngü Kapısı). **Vaka:** 1.

**Gözlem:** Videonun son 10 saniyesi karanlık bir kokpit kadrajında durağan kalarak bitmiş, başa sorunsuz dönen bir döngü mekanizması (seamless loop) kurulmamıştır.

**Çözüm Hipotezi:** Video çıkış karesi ilk kareyle görsel/anlatısal olarak eşleşen döngü kilitlerine (`seamless loop frame matching back to t=0`) kilitlenmelidir.

🔗 [[D4]] · [[D124]]











## ADAY-91 — BELGESİZ MERCEĞİN "PASS"I DA ÖNERME KAPISINDAN GEÇMELİ: SPEC KİLİDİNİ İHLAL EDEN ŞEYE 10/10 VERİLDİ

**Tarih / kaynak:** 13.09.2026 · THE STATIC SHADOW · ② ③ ⑥ (üçü de mod V) · parti 🚨 GEÇERSİZ,
master yok → ders YAZILAMAZ (kilit defteri 15 ⬜ AÇIK).
**KAPI:** aday — muhtemel LİSTE (`qa-isle` SKILL §6 ⑩ ÖNERME KAPISI'na yedinci satır: "PASS
hücreleri de okunur") ya da BETİK (`rapor_kontrol.py` ⑩: SPEC C sayısal kilitleri ↔ ⑥ ledger
"implied value"). **Vaka:** 1 (üç hücre).

**Gözlem (raporlardan, doğrulanmamış):** ⑩ ÖNERME KAPISI bulguları plana karşı okur ve planlı
olanı DÜŞÜRÜR; PASS'ları hiç okumaz. Bu partide üç PASS SPEC'in yasağına verilmiş övgü:
· ③ SFX senk **9/10** — RCS tıslaması, ark cızırtısı, çarpma sesi DIŞ kamerada "kare kare
  senkron" · SPEC C: dış kamera MUTLAK SESSİZLİK
· ⑥ ölçek **10/10** — "1:6 oranı beş sahnede tutarlı" · SPEC 1/30
· ② fizik **10/10** — "thruster exhaust and spark particulate behaviour consistent" · SPEC C
  "NO melting metal cliché", NEGATIVE "no atmospheric smoke"
Mod V "kendisiyle tutarlı mı" sorar; ihlal tutarlıysa tam puandır. D166 aynanın öteki yüzü
(kural kusur sayıldı); burada KUSUR KURAL SAYILDI ve övüldü.

**Kapatma:** master gelince üç kare/ses bandı (0:41 · 0:55 · 1:42). Üçü de FİLM SAPTI çıkarsa
kapı yazılır: ⑩'a "SPEC C'nin her kilidi için raporun o eksende ne yazdığı — PASS dâhil —
tabloya girer; kilide aykırı PASS 🔴 aday olur".

🔗 [[D166]] · [[D134]] · [[D130]] · [[D183]]

---

## ✅ ADAY-92 — FİLMİN ADI OLAN OLAY ON İKİ RAPORUN HİÇBİRİNDE YOK: "GÖLGE" KELİMESİ YALNIZ BAŞLIK KARTINDA GEÇİYOR

**DURUM:** → D151 not · K14 (14.09.2026 — kümeleme, `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 2)

**Tarih / kaynak:** 13.09.2026 · THE STATIC SHADOW · on iki mercek · master yok → ⬜.
**KAPI:** aday — [[D151]] / [[ADAY-1]] ailesi (novum vuruşu ekranda mı, mercek mi görmedi).
**Vaka:** D151'in 3. vakası OLABİLİR; kareyle ayrılır.

**Gözlem:** Planın S01'i: 500 m kalkan yalpalar, gölge hattı 80 m teleskoptan KAYAR, açığa
çıkan folyo turuncuya döner (TIMELINE 3,0 s · 7,0 s). S15: gölge sabit. On iki rapor S01'i
"telescope/array floats in front of sun flare" diye yazdı; hiçbiri gölge hattını, kaymayı,
ısı rengini anmadı. ④'ün izleyici cümlesi "manuel yanaşma"; ⑫ "no question in first 10 s".
İki ihtimal: (a) gölge üretilmedi/okunmuyor → ÜRETİM · (b) ekranda var, mercek görmedi →
D151 3. vaka (⛔ ÇALIŞMIYOR zaten). Bu filmde novum taşıyıcısı repliksiz kanıtlanacaktı
(KİNETİK BAĞIMSIZLIK satırı); replik de prompta girmediği için (D203) tek taşıyıcı görseldi.

**Kapatma:** `ffmpeg -ss 3 / -ss 7 / -ss 115 -i "$M" -frames:v 1` → gölge hattı teleskop
üstünde görünüyor ve kayıyor mu · S15'te sabit mi.

---

## ✅ ADAY-93 — ⑧ EFOR 1,0/10 "NOBODY PAYS" — ÖLÇÜLEN MAKARA, BEDENİN ÖDEMESİ PLANLANAN SAHNELERİ İÇERMİYOR (ADAY-11/12 ZİNCİRİNİN 3. KAYDI · MOD V · SAYIM DIŞI)

**DURUM:** → D206 · K1 (3. vaka, makara eksik — sayım dışı notu korunur) (14.09.2026)

**Tarih / kaynak:** 13.09.2026 · THE STATIC SHADOW · ⑧ EFOR mod V (⛔ TEKRAR [D129]) · ⑩
OYUNCULUK 1,5 MANNEQUIN (🚨 karantina [D190]).
**KAPI:** aday — [[ADAY-11]] → [[ADAY-12]] zinciri "üçüncüde ders yazılır" diyordu; bu üçüncü
kayıt MOD V partiden geliyor ve kontrat §4 gereği SAYILMAZ. Kayıt kaybolmasın diye burada.

**Gözlem:** ⑧ dört efor olayının dördünde sıfır zorlanma yazdı (0:29 el · 1:09 gövde · 1:29
baş · 1:49 toparlanma). Plan bedenin ödediği anları S10 (hızlı nefes) · S11 (omuz gerilmesi)
· S13 (itki sarsıntısı) · S14 (tutulan nefes) sahnelerine koymuştu; **S11 · S13/S14 makarada
YOK** [D188]. Ölçülen 12 klibin insanlı altısı kurulum ve tereddüt sahneleri — "ödeme yok"
hükmü, ödeme sahneleri olmayan bir makaraya verildi. Yine de S04 (el, 2 tıklatma) ve S10
(hızlı nefes, başın İPTAL koluna dönüşü) makaradaydı ve ⑧/⑩ orada da sıfır gördü → o iki
sahne için hipotez ayakta, kareyle sınanır (0:35 · 1:33).

**Not:** D202 (merkezî seçim bedende okunmuyor) bu filmde ÖLÇÜLEMEZ — seçim sahnesi (S12)
makarada yok; ⑩ seçimi joystick'e (S4) yazdı, bu D190'dır.

🔗 [[ADAY-11]] · [[ADAY-12]] · [[D202]] · [[D195]]

---

---

## ADAY-94 — KRİZ ZİNCİRİ PLANDA VAR, KADRAJDA YOK: HER HALKA BAŞKA YERDE, BAŞKA NESNEDE — İZLEYİCİ DÖRT AYRI ARIZA OKUDU

**Tarih / kaynak:** 15.09.2026 · MARS_SON_CIKIS B1 (S01-S18) · ④ HİKAYE · parti 🚨 GEÇERSİZ (mod V + ⑪ ölçüm yok) → tek film, ADAY.
**MOD:** V · ④ (⑫ HOOK aynı ekseni `Plateau` olarak gördü — ⑫ mod V karantinada, destek diye yazıldı, sayılmadı)
**KAPI:** aday — muhtemel LİSTE (`00_SAHNE_TABLOSU` olay hücresinde kriz sahneleri için `TAŞIYICI` nesne · ya da `03_PLAN_ONCESI` B maddesi: "ardışık kriz sahneleri kadrajda aynı nesneyi gösteriyor mu?"). **Vaka:** 1.

**Gözlem (rapor + plan):** altmış saniyede dört tehdit, her biri kendi on saniyesinde ve kendi mekânında: S05 güneş parçacık uyarısı (kontrol odası penceresi) · S08 havalandırma 4'te yalıtım yanığı (tavan kanalı) · S10 servis kapağı arkasında elektrik arkı (kapı dibi) · S11 ana hat şalteri (pano). ④: *"Cutting every ~10 seconds to a brand-new distinct catastrophe (solar radiation, duct leak, electrical fire, breaker trip) creates an artificial montage effect rather than letting one crisis build organic tension"* (Structure & Pacing 6/10 · Emotional Arc 7/10 · retention 1:42 *"Repeating hazard variants feels synthetic"*). ④'ün FLAG sorusu: *"intentional viral procedural montage, or a single runaway disaster?"* Plan zinciri KURMUŞ: S08 `insulation is burning inside the duct` → S10 `arc flashes flicker through the door keyhole` → S11 `glowing orange insulation fire spreading … inside the channel` + replik `fire is in the duct`. Ama her halka başka bir yerde ve başka bir nesnede duruyor (kanal ızgarası → kapı dibi → pano → yine kanal); bağı taşıyan tek şey replik. Kadrajda sabit kalan bir taşıyıcı (aynı kanal, aynı duman) yok — izleyici dört olay görüyor, bir felaket değil.

**Hipotez:** on saniyelik sabit birimde zincirin halkaları farklı nesnelere dağılınca sebep-sonuç kesmede kaybolur; tehdit tırmanmaz, yenilenir (D212 "aynı vuruş ardışık" yasağının öteki ucu: hep FARKLI nesne). Karşı-kalıp: TEK taşıyıcı nesne, büyüyen hâller, ardışık sahnelerde kadrajda — aynı kanal: sızıntı → duman → alev (D157 novum taşıyıcısının kriz hâli).

**Kapatma:** ikinci film. Bir filmin ④'ü "montage / checklist / repeating hazard variants" derse ve sahne tablosunda ardışık ≥ 3 kriz sahnesinin kadrajda ortak taşıyıcı nesnesi yoksa → ders; DEĞİŞEN SATIR `00_SAHNE_TABLOSU` olay hücresinde `TAŞIYICI` (aynı nesne adı).

🔗 [[D212]] · [[D157]] · [[D211]] · `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU` §2-§4

---

## ADAY-95 — KADRAJDAKİ BEDENE İŞ YAZILMADI: TIMELINE KAPIYI ANLATTI, ASTRONOT BOŞTA DÖNDÜ (⑭ ⑮ İLK GERÇEK KOŞU)

**Tarih / kaynak:** 15.09.2026 · MARS_SON_CIKIS B2 (S19-S36) + B1 · ⑭ HAREKET · ⑮ YÖN (ikisi de mod V; ikisinin de depodaki ilk koşusu) · parti 🚨 GEÇERSİZ → ADAY.
**MOD:** V · ⑭ ⑮
**KAPI:** aday — muhtemel BETİK (`prompt_kontrol.py`: `IN FRAME:` satırı bir beden gösteriyor ama bir TIMELINE satırında o bedene gövde fiili yok → FIX; ㉛ DOLULUK adayıyla aynı tarama) ya da LİSTE (`SAHNE_DOLULUGU_KILAVUZU` §6 soru 1). **Vaka:** 1 film · 4 sahne.

**Gözlem (rapor + prompt):**
· S34 (B2 2:30-2:40) — ⑭ M11 `SPIN` 🟡: *"She rotates her upper torso side to side while standing in place — I do not know why; nothing is there."* Prompt `IN FRAME: full body`; TIMELINE'ın üç satırı da KAPIYI anlatıyor (door slides closed · locking pins · green indicators) — iki astronot kadrajın öznesi, onlara tek fiil yazılmamış. Aynı sahnede ② kaskları geri takılı buldu, S33'te çıkarılmışlardı [D207].
· S08 (B1 1:16) — ⑭ M21 `SPIN` 🟡: gri tulumlu figür dar koridorda hedefsiz 180° dönüyor. Promptun `3.0s - 7.0s` satırı yalnız dumanı ve prob ekranını anlatıyor — o dört saniyede bedene fiil yok; dönüş tam o pencerede.
· S04 (B1 0:37) — ⑭ M12 `PHANTOM` 🟡: kupa elden çıktıktan sonra erkek astronot boş havada parmak büküyor — iş bitti, beden boşta kaldı.
· S36 (B2 2:52) — ⑮ V15 `MISS` 🟠: omza uzanan el havaya iniyor; promptun son satırı *"the room settles into deep peaceful silence … as the scene fades out"*.

**Hipotez:** TUR 19'un "model yazılanı üretir" satırının hareket yüzü: kadrajdaki bedene bir TIMELINE satırında iş yazılmazsa model onu dondurmuyor, AMAÇSIZ hareket uyduruyor — sallanma, dönme, boşa tutuş. `SAHNE_DOLULUGU` son üç saniyeyi bağlar; bu aday satır içindeki fiilsiz bedeni.

**Kapatma:** ikinci filmde ⑭ `SPIN / PHANTOM / SLIDE` bulgusu, promptunda o saniyeye o bedenin fiili yazılmamış bir sahneye düşerse → ders; DEĞİŞEN SATIR: `IN FRAME:` satırındaki her beden TIMELINE'ın her satırında bir gövde fiili taşır.

⚠️ ⑭ B2 PROMPT ORDERS #2 *"the astronaut stands completely still … without rotating her shoulders"* önerdi — bu depoda YAZILMAZ (`OYUNCULUK_YAZIM` §4 · `SAHNE_DOLULUGU` §4 ⑥); reçete olarak inmedi.

🔗 [[D207]] · [[D214]] · `SAHNE_DOLULUGU_KILAVUZU` §3 · §6

---

## ADAY-96 — ÇİFT KULE AYRIMI GÖRSELDE ÇÖKÜYOR: PLANLI İKİ AYRI YAPI KADRAJDA AYRIŞMADI, İZLEYİCİ KULEYİ RESETLENDİ/ZAMANSAL DÖNGÜ SANDI

**Tarih / kaynak:** 21.09.2026 · THE_STOLEN_SKY PART 1 (S00-S23) · ② DEVAMLILIK · parti 🚨 GEÇERSİZ (mod V + ⑪ ölçüm yok) → tek film, ADAY.  
**MOD:** V · ② DEVAMLILIK (① KARE'de de kule çarpışması blocker çıktı)  
**KAPI:** aday — muhtemel LİSTE (`UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU` §2 veya `03_PLAN_ONCESI` mimari kontrast satırı). **Vaka:** 1.  

**Gözlem (rapor + plan):**  
- S00 (00:04): İnsan tahliye gemisi kafese çarpıp yamacın altındaki boş servis kulesine (`one empty service tower taller than the rest`) çarpar ve kuleyle birlikte çöker.  
- S12/S13 (02:00): Çatı tareti savunma kulesinden (`Roof turret / defence grid tower`) gökyüzü kafesine lazer sıkar.  
- ② DEVAMLILIK raporu: *"Launch tower destroyed by ship impact at 00:04 (S1) is intact at 02:00 (S13)... The short film is structured as a non-linear concept teaser... Launch tower collapsing in S1 but standing intact in S13. Fix: Re-order S13/S14 to open the reel as establishing shots prior to the S1 crash."*  
- Planda hikâye kesinlikle doğrusaldır; S00'daki servis kulesi ile S12'deki savunma taret kulesi iki tamamen ayrı yapıdır. Ancak video promptlarında iki kulenin mimari dili, silueti ve malzemesi yeterince zıtlaştırılmadığı için AI her ikisini de benzer metal kule yapısı olarak üretmiş; izleyici/denetçi kuleyi tekil nesne sanarak kurgunun resetlendiği veya non-linear teaser olduğu sonucuna varmıştır.

**Hipotez:** Aynı dünyada geçen sahnelerde birden fazla büyük dikey yapı (kule, anten, baca, gantry) varsa, malzeme dili (ör. açık kafes çelik iskelet ↔ masif monolitik beton blok) ve siluet geometrisi en baştan zıtlaştırılmalıdır. Aksi takdirde difüzyon modeli jenerik 'kule' varlığı çağırır ve izleyici iki ayrı yapıyı tek bir nesnenin durum sıfırlanması (causality break) olarak okur.

**Kapatma:** İkinci filmde iki farklı mimari yapı kadrajda birbirine karıştırılıp 'dünya durumu resetlendi' bulgusu üretirse → ders; DEĞİŞEN SATIR: `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU` mimari kontrast kuralı.

🔗 [[D209]] · [[D208]] · `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU` §2 · §5

---

## ADAY-98 — "TRIPOD" KELİMESİ KADRAJA DÜŞÜYOR: CAMERA SATIRININ KENDİ JETONU PLANSIZ KAMERA SEHPASI ÜRETİYOR (JETON SIZINTISI SINIFI)

**Tarih / kaynak:** 22.09.2026 · TUR 24 süzgecinde depo verisinden bulundu (`URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 24 ⑤) · THE_SLOW_RAIN PART 1 + THE_STOLEN_SKY PART 1.
**MOD:** ⑤ ARKA PLAN ✅ GO (SLOW_RAIN) · ⑮ YÖN ⛔ TEKRAR mod V (SLOW_RAIN V14) · ① KARE out-of-scope flag (STOLEN_SKY) → sayım dışı bulgular karışık; **2 film**.
**KAPI:** aday — muhtemel BETİK (`prompt_kontrol.py` CAMERA satırında `tripod` → NOT) ya da LİSTE (`IMAGE_VIDEO_PROMPT_TEMPLATES` V3 CAMERA kalıbı). **Vaka:** 2.

**Gözlem (rapor + prompt):**
- THE_SLOW_RAIN S14 (02:10): *"zemin düzlüğünde plansız kamera tripodu beliriyor"* (⑤) · V14 0:28 *"kaza düşüşünde kadrajda daha önce kurulmamış tripod"* (⑮). QA kaydının cevabı: *"tripod yapay zeka modelinin 'camera/setup' kelimelerinden türettiği dışsal bir görsel halüsinasyondur."*
- THE_STOLEN_SKY PART 1 ① 00:39: *"Camera tripod visible in foreground near cave entrance between scene cuts."*
- İki filmin CAMERA satırı `… on a fixed locked-off tripod …` taşıyor: SLOW_RAIN 96/96 CAMERA satırı · STOLEN_SKY 94/192.
- Karşı kanıt: "tripod" depo bölüm dosyalarında 440 kez geçiyor; tripod bulgusu yalnız bu iki filmde. Ötekilerde (LOW_POWER · STONE_SKY · LISTENING_WORLD · BLUE_DRIFT · BLIND_RETURN) "tripod" ya plandaki bir nesne ya rubrik dilidir.

**Hipotez:** PROMPT_HATA §6 JETON SIZINTISI — promptun kendi kelimesi kadraja yazılıyor (`PHASE 1` · `EVA` · `S04` emsali). Kamera cümlesindeki nesne adı, kadrajın içine bir nesne olarak düşebiliyor; özellikle geniş dış planda boş zemin varken.

**Öneri (ÖNERİ · maliyeti sıfır):** CAMERA satırında `a locked-off camera` — kurulum imzası (lens · yükseklik/mesafe · ölçek · açı tipi) değişmez; `prompt_kontrol.py` KAMERA_IZI `camera` kelimesini zaten tanır.

**Kapatma:** "tripod"suz CAMERA satırıyla üretilen ilk iki filmde ⑤/⑮ plansız tripod 0 ise ve "tripod"lu bir filmde yeniden çıkarsa → ders; DEĞİŞEN SATIR: `IMAGE_VIDEO_PROMPT_TEMPLATES` V3 CAMERA kalıbı + `KILAVUZ_REHBERI` örnek cümleleri.

🔗 PROMPT_HATA_ONLEME §6 · `MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU` §4.2 · [[D59]]

---

## ADAY-99 — ORTAM KARTININ NEGATİF SATIRI HİKÂYE NESNESİYLE ÇAKIŞIYOR: YASAK KALKMAZ, KAYNAK İÇİN POZİTİF KURAL YAZILIR (ARŞİMET KALIBININ İKİNCİ VAKASI)

**Tarih / kaynak:** 28.09.2026 · THE_SIGNAL_KEEPERS yazımında `00_ANALIZ/04_UYARI_NOTLARI.md` §4b ADAY-A olarak önerildi; ilk vaka THE_COUNTED_RIVET (§3.6 nötr yüzerlik ↔ `never hovers`).
**MOD:** yazım turu (üretim 0 kare) — henüz ölçülmedi, bu yüzden ADAY.
**KAPI:** aday — muhtemel LİSTE (`PROMPT_HATA_ONLEME_KILAVUZU` §2'nin her ortam kartına bir "ÇAKIŞMA" satırı) ya da KILAVUZ (§3 kartlarının kendi içine). **Vaka:** 2.

**Gözlem (yazım, iki film):**
- THE_COUNTED_RIVET · §3.6 SÜREKLİ BULUT: kart platformun nötr yüzerlikte olmasını ister, negatif çekirdek ⑧ `never hovering` der. İkisi aynı promptta.
- THE_SIGNAL_KEEPERS · §3.4 KALIN ATMOSFER: hikâyenin bitkileri KENDİ ışığını verir, negatif çekirdek ③ `0% bloom, no glow` der. İkisi aynı promptta. Aynı filmde ikinci çakışma: kart "dolgu ÇOK GÜÇLÜ" der, ③ bloom'u yasaklar.
- İkisinde de geçen çözüm AYNI: **yasak cümle SİLİNMEZ** (silinirse hâle geri gelir ve kapı körleşir); yasağın yanına KAYNAK için pozitif, sayılı bir kural yazılır —
  `the low plants are themselves the source of a green-blue light, like lit lamps, the light not spreading past their edges`
  `the platform floats in neutral buoyancy, settling at a constant rate`
- ⚠️ Ve çözümün İKİNCİ yarısı SPEC'tedir: ⑪ IŞIK (ya da ⑥ FİZİK) merceği bunu çelişki yazarsa bulgu TASARIMDIR ve YANLIŞ-POZİTİF DUVARI'na satır olarak girer. Duvar satırı yazılmazsa aynı bulgu her koşuda yeniden gelir.

**Hipotez:** Negatif çekirdek HÂLE ve HAREKET üzerine yazılmıştır, KAYNAK üzerine değil. Bir hikâye nesnesi kartın yasakladığı fiziksel davranışı TAŞIMAK zorunda olduğunda çatışma kelimede değil KAPSAMDA: yasak "havanın içinde yayılan ışık"ı, pozitif kural "nesnenin kendi yüzeyinde duran ışık"ı tarif eder. İkisi çelişmez ama model için ayırt edilmeleri POZİTİF cümleye bağlıdır.

**Öneri (ÖNERİ · maliyeti sıfır):** `PROMPT_HATA_ONLEME_KILAVUZU` §2'nin her ortam kartı bloğuna tek satır: *"ÇAKIŞMA: bu kartın hangi satırı negatif çekirdekle çarpışır ve pozitif karşılığı nedir."* §3.4 ve §3.6'da o satır bugün yazıldı; kalan yedi kartta YOK.

**Kapatma:** üçüncü vaka farklı bir kartta çıkarsa ve çözüm yine "yasağı koru + pozitif kaynak kuralı" olursa → ders. DEĞİŞEN SATIR: `PROMPT_HATA_ONLEME_KILAVUZU` §2 (dokuz kart) + `KILAVUZ_REHBERI` §5.1'in çekirdek notu.

🔗 PROMPT_HATA_ONLEME §2 §3.4 §3.6 · `KILAVUZ_REHBERI` §3.4 · [[D123]] · [[D29]]

---

## ADAY-100 — ÖLÇEK YÜRÜYÜŞÜ POLİTİKA RİSKİNİ DÜŞÜRDÜ: KOMPOZİSYON KAPISI, POLİTİKA KAPISININ ALETİ OLABİLİR

**Tarih / kaynak:** 28.09.2026 · THE_SIGNAL_KEEPERS yazımında `00_ANALIZ/04_UYARI_NOTLARI.md` §4b ADAY-B olarak önerildi ve `00_ANALIZ/03_SAHNE_SIRALAMASI.md` §7c④'te ölçüldü.
**MOD:** yazım turu (üretim 0 kare) — red sınıfı ekranda sınanmadı, bu yüzden ADAY.
**KAPI:** aday — muhtemel KILAVUZ (`POLITIKA_VE_URETILEBILIRLIK_KILAVUZU` §4'e "ölçek aleti" satırı) ya da LİSTE (`02_RISK_KARTLARI` KART 12'ye çapraz not). **Vaka:** 1.

**Gözlem (tek film, ölçülmüş):**
- `02_KONSEPT_VE_RISK.md` §6 filmin en red-riskli karesini K23 diye yazdı (omuzdaki yuvadan nesne çıkarma · red defteri #3 sınıfı) ve nötr tarifi **ECU** olarak kurdu: *"no body, no face and no suit beyond the panel in frame"*.
- Sonra `ACI_YAYI` §3'ün güvenli bandı (ardışık çift ≥1 ölçek kademesi) o kareyi **CU**'ya çekti: kurulum L · 50 mm · 0,72 × 0,41 m. Kadraja omuz paneli + boyun halkası + kaskın ALT KENARI girdi.
- ⭐ Sonuç bir RİSK DÜŞÜŞÜ: red defteri **#13**'ün (sahne İPTAL edilmişti) üç bileşeninden ikisi kadrajdan çıktı — "yüzsüz izolasyon" ve "tepeden makro". Kalan tek bileşen nesnenin kendisi.
- Yani politika kararı (nötr tarif) ile kompozisyon kararı (ölçek yürüyüşü) BİRBİRİNDEN HABERSİZ alındı ve kompozisyon olan politikayı İYİLEŞTİRDİ. Tersi de olabilirdi: ölçek yürüyüşü bir kareyi ECU'ya ÇEKSEYDİ risk artardı ve hiçbir kapı bunu görmezdi.
- Aynı filmde ikinci gözlem: K10-K11'in (red #13'ün "iki uzuv" bileşeni) iki eli AYRI kliplere düşmesi de politika kararı değil ölçek/dönüş kararıydı.

**Hipotez:** POLİTİKA kapısı (B6) ve AÇI YAYI kapısı (B4) aynı değişkeni — KADRAJDA NE VAR — iki ayrı yerden yazıyor ve birbirlerini okumuyorlar. Red defteri sınıflarının çoğu bir KOMPOZİSYON tarifidir (yüzsüz izolasyon · tepeden makro · iki uzuv yan yana · gövdeden çıkarma), dolayısıyla ölçek merdiveni politikanın en ucuz aletidir.

**Öneri (ÖNERİ · maliyeti sıfır):** `03_PLAN_ONCESI` B6'ya tek satır: *"EN RED-RİSKLİ KARENİN ÖLÇEĞİ B4'ün yürüyüşüyle uyumlu mu — ve yürüyüş o kareyi YAKINLAŞTIRIYOR mu UZAKLAŞTIRIYOR mu?"* Uzaklaştırıyorsa kazanç kayda geçer; yakınlaştırıyorsa politika satırı YENİDEN yazılır.

**Kapatma:** ikinci bir filmde ölçek yürüyüşü en red-riskli kareyi YAKINLAŞTIRDIĞI hâlde politika satırı güncellenmez ve red gelirse → ders (ve o zaman bu aday BLOCK'a döner). DEĞİŞEN SATIR: `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` B6 + `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU` §4.

🔗 `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU` §4 · `ACI_YAYI_VE_SEKANS_KILAVUZU` §3 · `02_RISK_KARTLARI` KART 12 · red defteri #3 · #13

---

## ADAY-101 — OPTİK ARİTMETİĞİ BİR KARE KURTARDI: KURULUM TABLOSU, KADRAJ ENİNİ NESNE BOYUYLA KARŞILAŞTIRMADAN YAZILAMAZ

**Tarih / kaynak:** 28.09.2026 · THE_LAST_TOW yazımında `00_ANALIZ/03_SAHNE_SIRALAMASI.md` §3 kurulum tablosu kurulurken, `00_ANALIZ/05_SAHNE_CALISMALARI/K01_HOOK.md` OPTİK satırında yakalandı.
**MOD:** yazım turu (üretim 0 kare) — hata ekranda sınanmadı, üretimden ÖNCE düştü, bu yüzden ADAY.
**KAPI:** aday — muhtemel LİSTE (`03_PLAN_ONCESI` B4'e tek satır). **Vaka:** 1.

**Gözlem (ölçülmüş):**
- Filmin HOOK klibi (K01) bir nesnenin tek karelik bilmecesidir: 56 cm'lik çelik bir anahtar bir metal levhanın üstünde DİK duruyor.
- Kurulum önce **D** seçildi: 85 mm · 1,1 m → kadraj eni **0,47 m**, kadraj yüksekliği 0,26 m.
- ⛔ 56 cm'lik bir nesne 0,47 × 0,26 m'lik bir kadraja SIĞMAZ. Filmin en önemli karesi, hesap yapılmadan yazıldığı için ÜRETİLEMEZ bir karedi.
- Yakalayan şey rubrik değil, sahne çalışma şablonunun `KADRAJ ENİ: ⬜ m ⛔ HESAPLANDI` satırıydı — yani şablon zaten soruyordu, ama soru KURULUM TABLOSU kurulurken sorulmuyordu.
- Düzeltme: kurulum C'ye taşındı (50 mm · 2,4 m → 1,73 m), anahtar 1242 px. Zincirleme sonuç: K01→K02 şoku Δ3'ten Δ2'ye indi ve iskeletin ilk harfi değişti.

**Hipotez:** Kurulum tablosu (lens + mesafe + yükseklik + ölçek + azimut) bir GEOMETRİ tablosudur ama İÇERİK bilgisi taşımaz. Kadraj eni ile o klibin ANA NESNESİNİN boyu ayrı yerlerde yazıldığı sürece, ikisinin çelişmesi ancak sahne çalışma dosyası yazılırken — yani kurulum kararı verildikten SONRA — görünür. Bu deponun `OPEN CIRCUIT` denetimindeki "5 kurulumun 5'i tutmuyordu" bulgusu aynı boşluğun daha ağır hâli olabilir.

**Öneri (ÖNERİ · maliyeti sıfır):** kurulum tablosuna **iki sütun daha**: `kadraj eni (m)` ve `bu kurulumda en küçük/en büyük ana nesne (m)`. Tablo kurulurken sığmayan eşleşme kırmızı görünür. `03_PLAN_ONCESI` B4'e tek satır: *"her kurulumun kadraj eni, o kurulumu kullanan kliplerin EN BÜYÜK ana nesnesinden büyük mü?"*

**Kapatma:** ikinci bir filmde aynı çelişki sahne çalışma dosyasına kadar yakalanmadan geçerse ve üretimde kare kırpılırsa → ders. DEĞİŞEN SATIR: `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` B4 + `ACI_YAYI_VE_SEKANS_KILAVUZU` §4.

🔗 `ACI_YAYI_VE_SEKANS_KILAVUZU` §4 · `KILAVUZ_REHBERI` §5.2 · [[D179]] · THE_OPEN_CIRCUIT denetimi

---

## ADAY-102 — ORTAM KARTININ SAYISI HANGİ MALZEMEYİ VARSAYDIĞINI YAZMIYOR

**Tarih / kaynak:** 28.09.2026 · THE_LAST_TOW'un `00_ANALIZ/06_URETIM_ONCESI_KONTROL.md` §GENLEŞME SAYISININ DÜRÜST KAYDI bölümünde hesaplandı.
**MOD:** yazım turu · aritmetik denetimi (ekranda sınanmadı). **KAPI:** aday — muhtemel KART NOTU (`KILAVUZ_REHBERI` §3.8). **Vaka:** 1.

**Gözlem (aritmetik):**
- Kart §3.8 şöyle diyor: *"Gölgede ~100 K'de duran bir levha ışığa girince ~370 K'ye çıkar ve metrede yaklaşık 1,3 mm uzar."*
- ΔT = 270 K. Bu sayı α = 4,8 × 10⁻⁶ /K anlamına gelir — tungsten (4,5) ya da Kovar sınıfı **düşük genleşmeli** bir alaşım.
- Yapı çeliği α ≈ 12 × 10⁻⁶ /K → aynı ΔT'de **3,2 mm/m**. Alüminyum α ≈ 23 × 10⁻⁶ /K → **6,2 mm/m**.
- Yani kartın sayısı yanlış değil ama **hangi malzeme için** doğru olduğu yazılı değil; ve bu kartın kendi zemini "işlenmiş metal" diyor, alaşım demiyor.
- THE_LAST_TOW kartın sayısını KULLANDI (tek kaynak kuralı) ve sonucu hikâye için güvenli: 18 m'lik dizi 23 mm büyüyor, kapanması gereken boşluk 20 mm. Çelik değeriyle 58 mm olurdu — mekanik **daha güçlü** çalışır, yani hikâye hiçbir yönde kırılmıyor.

**Hipotez:** §3 kartlarının sayıları ortamı (basınç · yerçekimi · sıcaklık) kilitliyor ama MALZEME sabitlerini kilitlemiyor. Malzemeye bağlı bir sayı (genleşme · iletkenlik · ses hızı) kartta malzeme adı olmadan durduğunda, ikinci film onu başka bir malzeme için kullanır ve iki film aynı kartta çelişir.

**Öneri (ÖNERİ · maliyeti bir satır):** malzemeye bağlı her sayının yanına malzeme adı: *"metrede ~1,3 mm (düşük genleşmeli alaşım; yapı çeliği için ~3,2 mm)"*. ⛔ Kartı DEĞİŞTİRMEK sahip kararıdır — bu aday yalnız aritmetiği kayda geçirir.

**Kapatma:** ikinci bir §3.8 filmi çelik varsayıp 3,2 mm/m yazarsa iki film aynı kartta iki sayı taşır → ders. DEĞİŞEN SATIR: `KILAVUZ_REHBERI` §3.8 ikinci kural bloğu.

🔗 `KILAVUZ_REHBERI` §3.8 · `PROMPT_HATA_ONLEME` §2 §3.8 · [[D127]]

---

## ADAY-103 — SAHİBİN YASAĞI SÖZLÜKLE DEĞİL DEPONUN KENDİ DİLİYLE ÇÖZÜLÜYOR

**Tarih / kaynak:** 30.09.2026 · THE_LAST_GATE'in SAPMA 1 kaydı (`THE_LAST_GATE_PLAN.md` §Rozet Bible · §SAPMA).
**MOD:** yazım turu · iki kılavuzun kesişimi (ekranda sınanmadı). **KAPI:** aday — muhtemel AKIŞ NOTU (`yeni-film` adım 4). **Vaka:** 1.

**Gözlem:**
- Sahip "özgün rozetler korunur" dedi. Negatif çekirdek ④ ise *"no readable text, letters, digits or **symbols** … on any … patch"* diyor. Çelişki gerçekti.
- **İlk çözümüm** rozeti KÜÇÜLTMEK oldu: "blank raised relief, shape only" — yani rozet var ama tasarımı yok. İsteği karşılamıyordu, yalnız kapıyı geçiyordu.
- **Doğru çözüm depoda zaten yazılıydı ve okumamıştım:** `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU` §3 **METİNSİZ AMBLEM DİLİ** — `textless` + TEK geometrik motif + sayılabilir öğe + doku kelimesi (`embossed embroidery`), kılavuzun kendi ölçtüğü risk **"çok düşük"**.
- Aynı klipte hem sahibin isteği tam karşılanıyor (rozetin görünür bir tasarımı var) hem ④ ile çelişki kalkıyor (`textless` ile `no readable text` aynı yöne bakıyor).

**Hipotez:** Sahip talebi ↔ kapı çatışmasında ilk refleks **talebi kısmak** oluyor. Ama bu depoda çatışmaların çoğu daha önce çözülmüş ve çözüm bir kılavuz bölümünde duruyor. Çatışma anında sorulacak soru "talebi nasıl küçültürüm" değil, **"bu çatışmanın adı hangi kılavuzda geçiyor"**.

**Öneri (ÖNERİ · maliyeti bir satır):** `yeni-film` adım 4'ün (`02_KONSEPT_VE_RISK` §1 sapma tablosu) yanına tek satır: *"Sapma yazmadan önce `KILAVUZ_REHBERI` §1'in ORTAMA/TÜRE GÖRE EK OKUMA tablosunda o çatışmanın adını ara — sapma son çare, ilk çare değil."*

**Kapatma:** ikinci bir filmde sahip talebi bir kapıyla çarpışır ve çözüm yine mevcut bir kılavuz bölümünde bulunursa → ders. DEĞİŞEN SATIR: `yeni-film/SKILL.md` adım 4 · `03_PLAN_ONCESI` A1.

🔗 `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU` §3 · `KILAVUZ_REHBERI` §5.1 ④ · [[D138]] · [[D74]]

---

## ADAY-104 — YASAK KELİME NEGATİFİN İÇİNDE İKİ KEZ DAHA GERİ GELİYOR

**Tarih / kaynak:** 30.09.2026 · THE_LAST_GATE · üretim öncesi tam sözlük taraması.
**MOD:** yazım turu · 40 kelimelik grep taraması (ekranda sınanmadı). **KAPI:** aday — muhtemel KAPI EKLEMESİ (`prompt_kontrol.py` ⑯). **Vaka:** 2 (D123'ün LAST_SPAN vakası + bu).

**Gözlem:**
- D123 zaten şunu söylüyor: *"Politika sınıflandırıcısı öneki değil kelimeyi okur."* Bu filmde o dersi **bilerek uyguladım** ve yine iki kez ihlal ettim:
  - Kalabalık riskini kapatmak için negatife *"never a crowd and never a mass of **bodies**"* yazdım. Yani **kalabalığı yasaklamak için "crowd" kelimesini 10 kez, "bodies" kelimesini 15 kez prompta soktum** — tam D123'ün LAST_SPAN'de ölçtüğü mekanizma.
  - `"The ship never stops **dead** in space"` — bir DEYİM içinde, `POLITIKA_T2`'nin `\bdead\b` deseni.
- İkisi de `prompt_kontrol.py` ⑯ kapısından **geçti**: ⑯ T1/T2 sayımı YOĞUNLUK arıyor ve 10 geçiş bandın altında kaldı.
- Elle grep bulduktan sonra çözüm D123'ün kendi reçetesiydi: yasağı SİL, MALZEMEYİ TARİF ET → *"spaced apart with clear deck between them, and every one of them stays at a bay."*

**Hipotez:** D123'ü BİLMEK yetmiyor, çünkü ihlal **yasağı yazma anında** doğuyor: yazan kişi riski kapattığını sanırken riski prompta taşıyor. Kapının bandı (yoğunluk) bu kalıbı göremez — 10 geçiş "az" sayılıyor ama 10 geçişin **hepsi negatif bloğunda** ve hepsi aynı kelime.

**Öneri (ÖNERİ · maliyeti bir regex):** ⑯'ya alt kontrol: *bir T1/T2 kelimesi promptta yalnız NEGATIVE bloğunda geçiyor ve gövdede 0 kez geçiyorsa* → bu bir YASAK YAZMA kalıbıdır, yoğunluktan bağımsız FIX. Ek olarak `crowd` ve `mass of bodies` T2 sözlüğüne aday (şu an ikisi de listede YOK; `bod(y|ies)` var ama `crowd` yok).

**Kapatma:** ikinci bir film aynı kalıpla (yasağı yazarken kelimeyi taşıyarak) yakalanırsa → ders + kapı. DEĞİŞEN SATIR: `prompt_kontrol.py` `POLITIKA_T2` + ⑯ alt kontrolü.

🔗 `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI` #8 · [[D123]] · [[D59]]
