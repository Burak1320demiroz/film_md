# 📚 FAZ 9 / DORUK — QA DERSLERİ VE AKSİYON RAPORU (1. KOŞU)

> Koşu: 12.08.2026 · Girdi: **1 birleşik reel (~100 s) · MODE R** ·
> Rubrik: `FAZ_09_QA_PROMPT.md` · Ham çıktı:
> `../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP/THE_SECOND_SHIP_FAZ09_HAM.md`
>
> **SKOR 5.7 · ⚠️ ŞARTLI — filmin İLK TAM FAZ ÖLÇÜMÜ.** Dört fazdır
> (F6 · F7 · F8) teslimat yüzünden hiçbir faz taban üretememişti. Bu
> koşuda sıra KAYMADI: on segmentin onu da kendi satırıyla eşleşti,
> MAPPING COLLAPSE tetiklenmedi, ortalama hesabı doğrulandı
> (3+10+4+10+10+6+2+4+3+5 = 57 → 5.70 ✅).
>
> Şartlılığın tek sebebi teslimat: protokol 10 ayrı klip (MODE T),
> gelen 1 reel. Skor kullanılabilir, ama **faz ölçümüdür** — 03/04/06
> tablolarına ve 00_INDEX sayacına GİRMEZ.
>
> ⭐ **Fazın en pahalı üç kararının ikisi ilk denemede tuttu:** vizör
> istisnası (KARAR 4) 10/10, kontrollü büyüme (KARAR 3) 10/10.
> Batan taraf tek bir cümlede toplanıyor: **model bir istisnayı
> öğrendiği anda onu ÇOĞALTIYOR.**

---

## 1. NE TUTTU — üç kilit, ilk denemede

| Karar | Ne isteniyordu | Sonuç |
|---|---|---|
| **KARAR 4 · VİZÖR İSTİSNASI** | S85'te ton TEK YÖNDE, tüm camda aynı anda boşalsın; S86'nın ilk 2 saniyesinde geri dönüp bir daha açılmasın | **10/10.** Ledger: 0:42→0:45 eşit boşalma, yamasız; 0:50→0:52 eşit dönüş; S86 ve S90 boyunca opak. Ders 37'nin (ekipman durum geçişi) iki sahneye bölünmesi işe yaradı. |
| **KARAR 3 · KONTROLLÜ BÜYÜME** | Hat VAR olsun ama oynatımda KIPIRDAMASIN | **10/10.** "The relief is present and did NOT visibly move at any second." F7 S68'in tersi başarıldı: modele bir şeyi *görünmez* yaptırmak, *milimetrik* yaptırmaktan kolay. |
| **KARAR 2 · CEVAP IŞIKTIR** | Plaka ölü kalsın, oda ışığı bir kez kabarsın | **10/10.** Plaka üç sahnede de hiçbir şey yapmadı; kabarış 0:06–0:09'da kaynaksız bir SEVİYE olayı olarak geldi. Zemin kotasının kapalı kalması on sahnede de tuttu. |
| **İKİ AYNI YÜZ (KARAR 1'in yüz tarafı)** | İki figürün YÜZÜ birebir aynı olsun | **Tuttu.** "Are these the same face? **Yes.**" F7 S65'te ikizler mühürlüydü, yüz yoktu; bu, yüz düzeyindeki ilk delme ve kimlik eşleşti. Batan taraf yüz değil, RENK ve SAYI. |

---

## 2. ⛔ KİLİT ÇELİŞKİSİ DEFTERİ [AGENTS.md C/D/E ortak adım ②]

| # | Rapor ne dedi | Hangi kilit | Çözüm eylemi | Sonuç |
|---|---|---|---|---|
| 1 | S90'da **dördüncü figür** + başını çeviriyor | üç figür · "no head turns" | Master 1:30–1:40 | ⬜ AÇIK |
| 2 | S84'te gri kopyada **turuncu panel** | kopyada renk YOK | Master 0:30–0:40 · sol üst kol | ⬜ AÇIK |
| 3 | S86'da **5 hane** | dört hane | Master 0:56 · avuç açık, merkezde | ⬜ AÇIK |
| 4 | S85'te **ağız açılıp konuşuyor** | ağız kapalı · tek ifade göz kapağı | Master 0:48 | ⬜ AÇIK |
| 5 | S87'de kamera **gemiyi takip ediyor** | lockoff · "no pan following the ship" | Master 1:00–1:10 | ⬜ AÇIK |
| 6 | S82 · S87'de gemide **egzoz alevi**; S88'de **ikinci gemi** | kuyruksuz · tek nesne | Master 0:12 · 1:05 · 1:13 | ⬜ AÇIK |
| 7 | S83'te **sol eldiven yok** | tek mühür zinciri | Master 0:20 | ⬜ AÇIK — ama §3 D-BL'ye bak |
| 8 | S89'da **sağ el ELDİVENLİ** | çıplak el zinciri S81→S90 | Master 1:26 | ⬜ AÇIK |
| 9 | S81'de elin üstünde **metalik işaret/logo** | metin/işaret yasağı | Master 0:02 | ⬜ AÇIK |
| 10 | S89'da **yara izi YOK** | sol kaş · her karede | Master 1:20–1:30 · tek kare dondur | ⬜ AÇIK |

⚠️ **Madde 10 rapor tutarsızlığıdır:** "Shows no facial scar in the
close-up (S89)" cümlesi yalnız PASSPORTS bölümünde duruyor; sahne
bulgularına ve kategori 7'nin gerekçesine hiç girmedi. 85mm'lik bir
yakın planda kaybolan yara izi RED'dir — rapor onu bir pasaport
satırına gömdü. Rubrik yaması §5 ②.

⚠️ **Madde 3 · D-BB'nin devamı:** F8'de aynı sınıf GENİŞ kadrajda
raporlanmıştı ve güvenilirliği tartışmalıydı. Burada el **kadrajın
merkezinde, açık, avuç yukarı** — yani sayım bu kez güvenilir. Sınıf
dokuz vakada dokuz kez battı.

---

## 3. DERSLER (numaralar F8'den devam)

### D-BG 🔴 LİSANSLI KOPYA ÇOĞALIYOR — istisna öğrenilince genelleşiyor

S90'ın promptu figür sayısını iki ayrı yerde yazıyor:

```
IMAGE : "Exactly three figures ... this pairing is intended; no fourth figure."
VIDEO : "Exactly three figures — no fourth ever appears"
```

Rapor dört figür gördü ve dördüncüsü İKİNCİ BİR GRİ KOPYAYDI.

```
F7 S65'te aynı risk yazılıydı ("a third copy breeding, because the
frame has taught the model that copies exist here") ve orada TUTTU.
Fark iki tane:
  ① F7 S65 = 85mm, iki figür, yakın kadraj
  ② F9 S90 = 32mm, üç figür, 12→15 m pull-back, geniş oda
Geniş kadraj + boş zemin + "kopya var" bilgisi = model boşluğu kopyayla
dolduruyor.

YAMA — pozitif, konumlu ve sayılı doluluk tarifi:
  "EXACTLY THREE BODIES ARE IN THIS ROOM: one at ten meters walking
   away from camera, two standing side by side at four meters. The
   ENTIRE REST OF THE FLOOR IS EMPTY — no figure, no silhouette, no
   shape stands anywhere else in the volume at any second."
```

⭐ Aynı sahnede "No head turns" da delindi (kopya başını çevirdi) —
iki bulgu tek kök: **negasyon, modelin baştan kurduğu sahneyi
düzeltmiyor.**

### D-BH 🔴 KOPYA MALZEME DİLİ GİYSİLİ BEDENDE ÇÖKÜYOR

F8'de aynı dil ("every form present, every colour absent") dört sahnede
**10/10** tuttu: gemi gövdesi, kabuk, çekirdek parçası. F9'da kopya bir
BEDEN ve **sol üst kolda turuncu panel çıktı.**

```
AYIRT EDİCİ DEĞİŞKEN: nesnenin GİYSİ olarak tanınması.
  taş gövde / kabuk / makine parçası → renk sızması SIFIR
  giysili insan bedeni               → panel rengi geri geliyor
Model "basınç giysisi" önselini çiziyor ve o önselin içinde takviye
panelleri RENKLİDİR. Malzeme cümlesi bedeni kapsıyor ama giysiyi
kapsamıyor.

YAMA — parça parça sayan negatif + pozitif ikilisi:
  "Every panel, seam, cuff, stripe, patch and reinforcement on this
   figure is THE SAME matte bone-grey as its face — the suit is not
   painted, it is CARVED. No orange, no teal, no blue, no skin tone,
   no warm hue exists anywhere on its body, at any size, on any panel."
```

⚠️ Bu yama S90 ve F10'un üç kopya sahnesi için de geçerlidir — kopya
çapası S84'te kilitleniyor, hata oradan yayılır.

### D-BI 🔴 YÜZ GÖSTERİLDİĞİ AN KONUŞUYOR

KARAR 4 lip-sync riskini sıfırlamak için repliği S86'ya taşımıştı ve
mühürlü vizörün arkasına koymuştu. Risk hesabı doğruydu — **ama yanlış
sahne için.** Replik S86'da güvende; konuşan S85'in kendi yüzü oldu.

```
S85'in negatifi "no teeth, no snarl, no open mouth" diyor; ağzın
KAPALI OLDUĞU pozitif olarak bir kez yazılı ("a narrow horizontal
lipless line, closed"), ama ağzın AÇILAMAZ olduğu hiç yazılmıyor.

YAMA — ağız bir açıklık değil, bir YÜZEY olarak tarif edilir:
  "The mouth is a shallow closed seam in the skin — a line, not an
   opening: there is no gap, no lip, no cavity and no jaw behind it,
   and it CANNOT open. It stays exactly as it is in every frame."
+ tek ifade kilidi sayıya bağlanır:
  "The face makes EXACTLY ONE movement in these ten seconds: the
   eyelids close and open once, over about one second, at ~7s.
   Nothing else on the face moves at any other second."
```

⭐ Ders sınıfı geniş: **bir yüz gösterildiği anda model ona performans
veriyor.** F7 S67'de aynı sınıf "acıma yüzü" olarak çıkmıştı, F8 S79'da
mimik performansı riski yazılmıştı. Burada uzaylı yüzünde konuşma
olarak çıktı. Yüz = performans daveti.

### D-BJ 🔴 HAREKETLİ ÖZNE PAN'I DAVET EDİYOR — negasyon yazılıydı ve battı

S87 fazın en net kamera kilidiydi ve promptta **açıkça** yazılıydı:

```
"It never moves for the whole ten seconds — it does not pan to follow
 anything."
"...no shake, no pan following the ship, no zoom."
```

Rapor: kamera gemiyi takip etti.

```
F8 D-AX ile birleştiğinde sınıf iki katmanlı:
  F8 S71 → "no pan" fazın hiçbir promptunda YOK (eksik yazım)
  F9 S87 → "no pan following the ship" YAZILI, yine battı (yetmezlik)
Yani kamera kilidini yazmak gerekli ama yeterli değil.

⭐ PLAN KATMANI ÇÖZÜMÜ [AGENTS.md §8]: bu sahnenin konusu KULENİN
HİÇBİR ŞEY YAPMAMASIDIR. Gemi anlatının öznesi değil, kulenin
tepkisizliğinin ölçüsüdür.
  → Gemi kadrajda ÇOK KÜÇÜK tutulur (kadrajın %2'si) ve kulenin
    üstünden değil, kadrajın ÜST KENARINDAN geçer.
  → Kamera kulenin gövdesine kilitlenir; geminin geçişi kadrajın
    kenarında bir olaydır, merkezinde değil.
Takip edilecek bir özne bırakılmazsa takip edilmez.
```

### D-BK 🔴 GEMİ BİÇİMİ = EGZOZ ÖNSELİ — sınıf dört vakalı

```
F7 S70 · gökte NOKTA          → temiz geçti (kuyruk yok, ikinci nesne yok)
F8 S78 · "elongated hull"     → iz + ikinci nesne [D-BF]
F9 S82 · "plainly a ship now" → egzoz alevi
F9 S87 · gövde net            → egzoz alevi
F9 S88 · uzaklaşan gemi       → gökte İKİNCİ gemi

Nesneye biçim verildiği andan itibaren model "uzay gemisi" önselini
çiziyor ve o önselde egzoz VARDIR. Negasyon listesi (no tail, comet
trail, flame, exhaust, streak, halo, starburst, lens flare, twinkle)
dokuz kelimeyle yazılı ve üç sahnede de yetmedi.

YAMA — pozitif tahrik tarifi:
  "The ship moves with NO VISIBLE PROPULSION: its engine pods are
   dark, cold and closed — matte metal caps with nothing coming out
   of them. The space behind the ship is empty sky, the same colour
   as the sky in front of it."
+ S88'e sayım: "EXACTLY ONE ship and ONE moon are in this sky. No
  other object, craft, star or light exists anywhere in the frame."
```

### D-BL 🔴 S83'TE SOL ELDİVEN HİÇ KİLİTLENMEMİŞ — depo kanıtlı boşluk

Rapor S83'te sol elin çıplak olduğunu söylüyor (defter madde 7).
Bulgu ⬜ AÇIK, **ama promptun boşluğu açık değil — kanıtlı:**

```
S83'ün IMAGE + VIDEO promptlarında "glove" kelimesi TEK KEZ geçiyor
ve o da YERDEKİ eldiveni tarif ediyor:
  "A dark grey-blue glove lies on the floor near the plinth."
Kadının SOL ELİ hiçbir yerde tarif edilmiyor: ne eldivenli olduğu, ne
kadrajda olduğu, ne olmadığı. Tek mühür zincirinin taşındığı sahnede
zincirin yarısı yazılmamış.

⚠️ Aynı boşluk F8 S80'de de vardı [D-BE] ve orada da aynı bulgu çıktı.
Sınıf iki fazda iki kez: ÇIPLAK EL SAHNELERİNDE ÖBÜR EL YAZILMIYOR.
```

```
YAMA — S83 · S84 · S89 · S90'a (çıplak elin göründüğü her sahne):
  "Her LEFT hand stays GLOVED and sealed throughout: a dark grey-blue
   pressure glove covering every finger, with a worn ORANGE cuff. The
   ONLY bare skin anywhere in this shot is her RIGHT hand and wrist."
```

### D-BM 🔴 ÇIPLAK/ELDİVENLİ DURUMU SAHNEDEN SAHNEYE TAŞINMIYOR

S89'da promptun dili doğrudur ve nettir:

```
"Her BARE right hand has risen into the bottom of frame, open, fingers
 loose — free."   +   NEGATIVE: "Five bare fingers, fixed anatomy."
```

Rapor: yükselen el ELDİVENLİ. Prompt hatası yok; **durum sürekliliği
hatası var.**

```
DERS: bir karakterin ekipman DURUMU (eldiven var/yok) sahneler arasında
kendiliğinden taşınmıyor. Faz boyunca dokuz sahnede sabit kalması
gereken tek şey buydu ve iki sahnede iki farklı yöne bozuldu
(S83'te fazla çıplak, S89'da fazla giyinik).

ÇÖZÜM ÜRETİM KATMANINDA: çıplak elin göründüğü BEŞ sahne (S81 S83
S84 S89 S90) tek bir onaylı EL KARESİNDEN üretilir — S80'in son karesi
zaten bu iş için kilitlenmişti [F8 · S80 → S81 eylem sürekliliği].
Aynı kare S89 ve S90 için de start-frame olarak verilir.
```

### D-BN 🟡 S89 KÜÇÜK BULGU: sahne kapalı gözle açılıyor

Satır 0s'de "eyes level, mouth closed" diyor; rapor gözlerin kapalı
başladığını söylüyor (YELLOW). Tek başına kurguda kırpılabilir, ama
S89 zaten D-BM yüzünden yeniden üretilecek — aynı render'da düzelir.

---

## 4. SKOR OKUMASI — hangi sayı ne anlatıyor

```
10 · VİZÖR İSTİSNASI            ilk denemede geçti [KARAR 4]
10 · PLAKA + IŞIK CEVABI        ilk denemede geçti [KARAR 2]
10 · ZEMİN SESSİZLİĞİ + BÜYÜME  ilk denemede geçti [KARAR 3]
 6 · OLAY TESLİMİ               S87 (pan) ve S88 (ikinci gemi) düştü
 4 · BEKÇİ'NİN YÜZÜ             anatomi tuttu, ağız battı
 4 · KAMERA                     tek sahne (S87) tüm kategoriyi düşürdü
 3 · LİSANSLI KOPYA             yüz tuttu, renk ve sayı battı
 3 · GÖK/KULE/IŞIK/METİN        kule tertemiz, GEMİ battı
 2 · KİMLİK + TEK MÜHÜR ZİNCİRİ fazın en zayıf halkası
 5 · FAZ ZİNCİRİ + HİJYEN       reel teslimatı + S89/S90 kırıkları
```

**Okunuşu:** fazın YENİ ve pahalı kilitleri (vizör, büyüme, ışık
cevabı) tuttu; batan her şey ESKİ ve tekrar eden sınıflardan geldi —
hane sayısı, renk sızması, kamera kilidi, ekipman sürekliliği, gemi
egzozu. Bu, F9'un tasarımının değil, **sekiz fazdır kapanmayan beş
sınıfın** raporudur.

---

## 5. RUBRİĞİN BATAN TARAFI → YAMALANACAK

```
① ÜÇ İSTİSNANIN KORUNMASI ÇALIŞTI, ÇOĞALMA UYARISI YETMEDİ
   Rubrik "üçüncü kopya batırır" diyordu ve rapor onu doğru yakaladı.
   Ama DUPLICATE LEDGER yalnız S84 ve S90'ı soruyor; "kadrajda başka
   hiçbir figür yok" sorusu her sahneye sorulmuyor.
   → YAMA: FIGURE COUNT satırı on sahneye birden, tek tablo.

② PASSPORT SATIRINA GÖMÜLEN BULGU
   "S89'da yara izi yok" cümlesi PASSPORTS'ta kaldı, bulgu listesine
   ve skora hiç girmedi. Rubrik pasaport bölümünü "karşılaştırma
   ÖNCESİ gözlem" diye tanımlıyor ve rapor onu bir çöp kutusu gibi
   kullandı.
   → YAMA: "PASSPORTS AS SEEN bölümünde SPEC'ten sapan her satır,
     SCENE-BY-SCENE'e bir bulgu olarak KOPYALANIR. Pasaportta kalan
     sapma yok sayılır."

③ MODE R'DA SKOR YAYIMLANDI
   Rapor protokol sapmasını doğru ilan etti ama ortalamayı yine de
   yayımladı. Bu doğru davranıştır (kayma yoktu), ancak skorun
   ŞARTLI olduğu raporun kendisinde yazmıyor.
   → YAMA: "MODE R'da hesaplanan ortalamanın yanına her zaman
     '⚠️ CONDITIONAL — merged reel delivery' etiketi yazılır."
```

---

## 6. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ ⛔ MASTER TARAMASI (10 madde · ~3 dakika) — §2 defteri
     Yeniden üretim siparişi ve global ders bundan SONRA.

2. □ PROMPT YAMALARI — depo kanıtlı olanlar beklemez:
     a) S83 S84 S89 S90 → SOL ELDİVEN pozitif cümlesi [D-BL] ⭐ hemen
     b) on sahneye PAN/TILT yasağı [F8 D-AX ile aynı yama]
     Diğerleri master taramasından sonra:
     c) S84 → panel panel renk yasağı + "carved, not painted" [D-BH]
     d) S90 → konumlu ve sayılı doluluk tarifi [D-BG]
     e) S85 → ağız "açıklık değil dikiş" + tek ifade sayımı [D-BI]
     f) S82 S87 S88 → soğuk/kapalı motor kapsülü + tek nesne sayımı [D-BK]
     g) S87 → gemi kadrajın %2'sine küçültülür, üst kenardan geçer,
        kamera kule gövdesine kilitlenir [D-BJ · plan katmanı]

3. □ ⛔ TETİK KAPILARI — ikisi de bu fazda:
     a) S84 KOPYA ÇAPASI: renk sızması düzeltilmeden S90 ve F10'un üç
        kopya sahnesi ÜRETİLMEZ [Ders 68]. 8 varyasyonun seçimi
        rapordan önce insan gözüyle yapılır.
     b) R3 BEKÇİ EL KARESİ: dört hane sayılmadan S86 ve S90 yeniden
        üretilmez [D-BB · dokuz vakada dokuz kez battı].

4. □ EL KARESİ ZİNCİRİ [D-BM]: S81 S83 S84 S89 S90 tek onaylı çıplak
     el karesinden, start-frame ile üretilir.

5. □ RUBRİK YAMALARI [§5 ① ② ③].

6. □ 2. KOŞU: MODE T, 10 ayrı dosya — 5.7 bir TABAN DEĞİL, şartlı bir
     ilk ölçümdür.
```

---

## 7. FLAGS — dokümandan/operatörden cevaplanacak

```
· Raporun sorusu: "gri kopyanın asset'inden texture map'ler global
  olarak sıyrılabilir mi?" → Kopya S84'te 8 varyasyonla üretiliyor;
  varyasyonlardan HERHANGİ BİRİ renksiz çıktıysa çapa o olmalı.
  Hangi varyasyon seçildi ve neye göre?
· R3 BEKÇİ plakasının kendisi kaç haneli? [F8 flags ile aynı soru —
  dokuz vakalık sınıfın kaynağı referans olabilir]
· S85'in AYRI SEED'i tutuldu mu — yüz 8 varyasyonun hangisinden geldi?
· S89'un start-frame'i S80'in son karesinden mi verildi? (D-BM'nin
  kök nedeni buna bağlı)
```

---

## 8. F10 VE SİSTEME TAŞINANLAR

> ⛔ Global DERS numarası (100+) HENÜZ AÇILMADI: §2'deki on madde
> ⬜ AÇIK. F8'in üç ders adayı bu koşuda bağımsız olarak tekrarlandı;
> master taraması sonrası ikisi kesinleşir.

```
ADAY DERS 100 · NEGASYON DURUM KURMAZ  [F8 D-BA · D-BE · F9 D-BG · D-BL]
  Dört sahnede dört kez: yasak yazılı, model durumu BAŞTAN yanlış
  kuruyor, yasak devreye girmiyor. Bu koşunun en güçlü adayı.

ADAY DERS 102 · BİÇİM VERİLEN UÇAN NESNE EGZOZ ÜRETİR  [F8 D-BF · F9 D-BK]
  Dört vaka. Nokta güvenli, gövde güvensiz.

ADAY DERS 103 · YÜZ = PERFORMANS DAVETİ  [F7 S67 · F8 S79 · F9 D-BI]
  Bir yüz kadrajda büyüdüğü anda model ona bir eylem veriyor: acıma,
  mimik, konuşma. Tek ifade SAYIYLA kilitlenmeli.

⛔ F10 ÜRETİMİNE DOĞRUDAN GEÇEN İKİ KİLİT:
  · F10'un veda bandı (S95-S97 · S99) S84 kopya çapasından üretilecek.
    ÇAPA HENÜZ ONAYLANMADI — renk sızması açık [D-BH].
  · F10'un son üç-figür kontenjanı (kopya Bekçi'nin yanına geçiyor)
    S90'ın aynı kadraj sınıfıdır ve S90 dördüncü figür üretti [D-BG].
    Konumlu-sayılı doluluk tarifi F10 promptuna DA yazılır.
```
