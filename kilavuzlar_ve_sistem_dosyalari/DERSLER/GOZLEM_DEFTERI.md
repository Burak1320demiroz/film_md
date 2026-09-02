# 🗒️ GÖZLEM DEFTERİ — kapısız adaylar (ders DEĞİL)

> `00_DERS_YAZIM_KONTRATI.md` §4. Kapısı bulunmayan ya da geçersiz partiden
> gelen aday burada bekler; kapıya bağlanınca ders numarası alır. Sayı:
> `sayac.sh` 🧭 bloğu. Bu dosyada `## … DERS <rakam>` başlığı YAZILMAZ.

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

## ADAY-3 — TEK NOKTADA OKUNAN SAYAÇ SAAT DEĞİLDİR

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

## ADAY-4 — DÖNÜM ANI KADRAJIN KENARINDAYDI VE İLK İZLEMEDE GÖRÜLMEDİ

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

## ADAY-5 — VİVİD KÜÇÜK AYRINTI, KAPSAYAN NESNEYİ EZİYOR

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

## ADAY-6 — THE STILL SWARM: SEKİZ MERCEĞİN SEKİZİ DE NOVUM'U GÖREMEDİ (ADAY-1'in 2. VAKASI)

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
