# 📚 FAZ 4 / TARLA — QA DERSLERİ VE AKSİYON RAPORU

> Koşu: 09.08.2026 · Model: Gemini · Girdi: tek 93 s reel (6×10.0 s +
> 3×8.0 s + 1×9.0 s) · MODE R · Rubrik: `FAZ_04_QA_PROMPT.md` · Ham çıktı:
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP/THE_SECOND_SHIP_FAZ04_HAM.md`
>
> **Skor 5.2/10 — F3'ün 3.7'sinden farklı olarak ÇOĞU GERÇEK.** Bu kez
> takas yalnız iki segmenti (S32/S33) kirletti; kalan sekizi kendi
> satırına karşı ölçüldü. Yani 5.2 karşılaştırma tabanı olarak
> kullanılamaz ama **bulguların çoğu tartışmasız üretim hatasıdır.**
>
> ⛔ **Fazın iki fikri de ekranda yok.** Bu fazın var oluş sebebi iki
> kareydi: S35 (afiş karesi — filmin tek görüntülük fikri) ve S34
> (tarla kuralı — her enkazın yanında ikizi). S35 gerçek çelik gemi
> çıktı, S34 yanlış kamera açısından çekildi. **İkisi de yeniden
> üretim; bu faz şu hâliyle teslim edilemez.**

---

## 1. KÖK NEDEN #1 — MONTAJ: YİNE REEL, YİNE TAKAS (üçüncü tekrar)

```
Reel'deki gerçek sıra:   S31 · S33 · S32 · S34 … S40
Olması gereken:          S31 · S32 · S33 · S34 … S40
                                ↑ ikili takas ↑
```

F1'de S4-S7 rotasyonu, F3'te ikili takas + üçlü rotasyon, F4'te ikili
takas. **Aynı sınıf hata dört fazın üçünde.** Üstelik bu kez rubrik
MODE T'yi (10 ayrı dosya, dosya adında sahne numarası) *tercih edilen
mod* ilan etmişti ve F3 dersi ④ tam bunu söylüyordu — koşu yine reel
ile yapıldı.

**Bedeli sınırlı ama tam yerinden vurdu:** takas edilen iki klip, fazın
malzeme çapası (S32) ve mekanizma sahnesi (S33). Sonuç:
- S32'nin **kendi satırına karşı** malzeme denetimi YAPILAMADI,
- S33'ün **kök damarları** (mat mı, parlıyor mu) ölçülemedi — rapor
  "not visible in mapped segment" diyor,
- iki klibin gerçek bulguları (metalik bacak · kum şelalesi) doğru
  ama **sahne atfı ters**.

**Çözüm (bedava, kurguda):** 2↔3 takası.
**Kalıcı önlem — artık öneri değil KAPI:**

```
F5'ten itibaren reel ile QA koşusu YAPILMAZ. 10 klip, dosya adında
sahne numarasıyla (s41.mp4 … s50.mp4), MODE T'ye yüklenir. Elinde
yalnız reel varsa koşuyu BAŞLATMA — önce klipleri ayır.
Gerekçe: dört fazın üçünde reel sırası karıştı; hiçbirinde MODE T
denenmedi. Denenmemiş bir çözümün maliyeti sıfır.
```

---

## 2. TUTAN TARAF — bu fazın gerçek kazanımları

| Kilit | Skor / Kanıt |
|---|---|
| **Işık geçiş kilidi [KARAR 1]** | **9/10** — "dawn to locked daylight transition is highly successful and holds direction". Şafak S31'de kaldı, S32-S40 sabit, key HEP sol. Dört fazın en temiz ışık skoru. |
| **Beyaz figür kilidi [KARAR 3 · F3 D-L]** | WHITE FIGURE LEDGER'ın **dokuz satırı da "No"** — S31-S39'da tek bir beyaz figür yok. F3'te Bekçi erken doğmuştu; negasyon bloğu taşındı ve TUTTU. |
| **Kopya malzeme dili [KARAR 2]** | S38 için: *"flawless execution of the Copy Material Law — solid, matte, dusty, and perfectly still"*. S37 ve S39 da geçti. **Dil yanlış değil** — S32/S35'te bozan başka bir şey (§3 D-O, D-P). |
| **Bekçi hareket dili [KARAR 3]** | *"fluid, continuous rotation… obeys the movement lock beautifully"*. Dönüş tek, kesintisiz, tamamlanmamış. Kostüm battı, HAREKET tuttu. |
| **Roket negasyonu [F3 D-K]** | Hiçbir kadrajda koni/fin/silindir yok. F3'ün en pahalı klişesi taşındı ve kapandı. |
| **Sıfır konuşma** | On sahnenin onunda ağız kapalı. S36 için: *"lack of emotion, 0 speech"* — Ders 35 (abartılı mimik) da tuttu. |

⚠️ **Skor okuma uyarısı:** "THE WHITE FIGURE LOCK: 4" satırı yanıltıcı.
O 4, dokuz sahnede tutan erken-figür kilidini değil, S40 Bekçi spec'inin
batışını ölçüyor. Rubrik iki farklı şeyi tek kategoride topluyor —
§4'te düzeltiliyor.

---

## 3. KÖK NEDEN #2 — ÜRETİM: dokuz ders

### D-O 🔴 S35 AFİŞ KARESİ GERÇEK GEMİ ÇIKTI — fazın en pahalı hatası

Filmin tek görüntülük fikri. Çıkan: gerçek çelik kargo gemisi —
**pencereler, radar direkleri, menfezler, pas ve boya**, üstelik kumla
buluştuğu yerde **belirgin taban çizgisi**: gömülü görünüyor, büyümüş
değil. Kopya malzeme yasasının beş maddesinin üçü birden düştü.

Rubriğin MOST LIKELY FAILURE satırı bunu birebir öngörmüştü
(*"a ship half-BURIED in rubble instead of half-GROWN"*) — öngörü
tuttu, prompt tutmadı.

**Kök neden — iki katmanlı:**

```
① ÖZNE ADI GEMİ. Prompt "a mid-sized BOXY cargo ship … rendered in
   matte bone-grey stone" diyor. Model önce GEMİ kuruyor, sonra taşa
   boyamaya çalışıyor — ve gemi mantığı (pencere, radar, menfez,
   pas) beraberinde geliyor. F3 D-J'nin ("transmission" → waveform)
   nesne versiyonu: ADLANDIRDIĞIN ŞEYİN KLİŞESİNİ ALIRSIN.
② IŞIKSIZ PENCERE DE PENCEREDİR. Negatif blokta "no lit windows"
   vardı — model ışıksız pencere çizerek negasyonu teknik olarak
   ihlal etmedi. Yasak ışığa yazılmıştı, DELİĞE değil.
```

**Yeniden üretim dili — özne taş, gemi sıfat:**

```
A MONOLITH OF SOLID ROCK, shaped like a boxy cargo hull. It is a
rock formation first and a ship-shape second: one single piece of
matte bone-grey stone, carved by nothing, quarried from nothing.
The hull SHAPE is readable - flat slab sides, blunt rectangular
bow, the suggestion of plate seams as shallow relief in the rock.
NO WINDOWS AT ALL - no glass, no ports, no openings of any kind,
lit or unlit. No radar dish, no antenna, no sensor mast, no vents,
no grilles, no hatches, no rust, no paint, no metal sheen.
Where the stone meets the ground there is NO LINE, NO SEAM, NO
SAND PILED AGAINST IT and NO SHADOW GAP: the rock widens and
becomes the basalt floor in one unbroken surface, the way a
mountain becomes a plain. It is not buried, not sunk, not
half-covered - it is GROWN, and the ground is the same material.
```

⛔ **En az 4 varyasyon bütçesi zaten yazılıydı (ÜRETİM SIRASI §3).
Kaç varyasyon denendi?** → doküman sorusu §5.

---

### D-P 🔴 S32 MALZEME ÇAPASI METALİK ÇIKTI — ve zinciri kirletti

Gerçek S32 klibi (rapor takas yüzünden S33 satırına yazdı) iki hata
taşıyor:

```
① Bacak "metallic/plastic" okunuyor — TAŞ DEĞİL.
② Bacaktan SÜREKLİ KUM ŞELALESİ akıyor (0:20).
```

②'nin ağırlığı ①'den fazla: prompt *"a thin, weak drift of low dust…
a few grains trickle off"* diyordu; model bunu şelaleye çevirdi. Sürekli
akan malzeme, kopyanın **hareket ettiği ve büyüdüğü** izlenimini verir —
NO-REAL-TIME-GROWTH yasasının ihlal edilme biçimi budur. Kopya yerine
"kumla kaplı bir enkaz" okunuyor.

**Zincir bedeli:** S32 fazın malzeme ÇAPASIYDI (KARAR 2, üretim sırası
1. madde: *"bu karede onaylanan doku, fazın kalan bütün kopyalarının
çapasıdır"*). Çapa metalik çıkınca S35'in de aynı yöne kaymasına
şaşırmamak gerekir — **iki hata bağımsız değil, aynı zincirin iki
halkası.** Sıra kuralı işletilmemiş: S32 onaylanmadan S35 üretilmiş.

**Yeniden üretim dili:**

```
The leg is CARVED FROM ONE PIECE OF DRY GREY ROCK - the material of
a cliff face, not of a machine: no metal sheen, no plastic
smoothness, no reflection, no specular highlight anywhere on it.
Dust sits ON it in the hollows, static, undisturbed - the dust does
NOT pour, stream, run, cascade or fall from the object at any
second. In the whole ten seconds the only movement in frame is one
thin low drift of dust crossing the FLOOR of the frame, and a few
single grains tipping off the pad edge and coming to rest.
```

---

### D-Q 🔴 S39 VİZÖRDE YÜZ — negasyon vardı, yetmedi

Oyukta *"fully sculpted, detailed stone human face (eyes closed, nose,
lips)"*. Prompt negatifinde **"no glass, no reflection, no eyes, no
face, no skull"** ZATEN VARDI.

Bu, F4'ün en genellenebilir dersi:

```
BOŞLUĞU YASAKLAMAK BOŞLUĞU KORUMAZ. Model bir oyuk görürse doldurur;
"içine şunu koyma" listesi ne kadar uzarsa uzasın, oyuk hâlâ
doldurulacak bir yer olarak duruyor. Çözüm yasak değil, POZİTİF
DOLDURMADIR: orada bir boşluk olmadığını söyle.
```

**Yeniden üretim dili:**

```
The helmet has NO CAVITY. Where a visor would be, the surface is
FILLED FLUSH WITH SOLID ROCK - one continuous stone plane running
from cheek to cheek, the same material and the same dusty texture
as the rest of the helmet shell. There is no recess, no opening,
no window, no hollow, nothing behind anything: this is a solid
lump of stone in the shape of a helmet. Nothing can be inside it
because there is no inside.
```

⚠️ Prompt sahne kartı ve rubrik "deep visor recess / oyuk" diyordu —
**tarifin kendisi hatayı davet ediyordu.** Rubriğin S39 satırı da
düzeltilir (§4).

---

### D-R 🔴 S40 BEKÇİ: TETİK KAPISI ATLANMIŞ — F5'in ön koşulu yandı

Bekçi spec'inin yedi maddesinden **beşi battı**:

| Spec | Ekranda |
|---|---|
| 2.10 m, insandan belirgin uzun | normal insan boyu |
| dikişsiz, tozsuz, kusursuz beyaz | çizik, kirli, panel çizgili, dikişli |
| sırt DÜZ, çıkıntısız | **sırt çantası + oluklu hortumlar** |
| diz hizasına inen uzun kollar | standart kol |
| üç parmak + başparmak | doğrulanamadı (eller görünmüyor) |
| koyu gri-yeşil opak vizör | beyaz/açık gri opak vizör |
| tek, kesintisiz, tamamlanmayan dönüş | ✅ **TUTTU** |

Ekranda görünen şey Bekçi değil, **jenerik bir astronot**. Sırt çantası
+ hortum, modelin "beyaz suit" isteğine verdiği hazır cevabı — yani R3
master plakası kullanılmamış.

⛔ **Prompt dosyasında bu sahnenin başında açık bir kapı vardı:**

> `S40 — BEKÇİ İLK KARE. ⛔ TETİK SAHNE: R3 master plakası üretilip
> onaylanmadan bu sahne üretilmez [Ders 68 ②] — F5'in 7 Bekçi sahnesi
> bu karenin çapasına yaslanacak.`

**Kapı atlanmış.** F3'te de F2'nin 1. aksiyonu açıkken üretime
başlanmıştı (D-G) ve o fazın 10 sahnesinin 6'sı yeniden üretime
girmişti. **İkinci tekrar.** Bedeli bu kez daha büyük: F5'in yedi Bekçi
sahnesi çapasız kalıyor.

```
YENİDEN ÜRETİM KAPISI: S40 ve F5'in hiçbir Bekçi sahnesi, R3 master
plakası üretilip İNSAN GÖZÜYLE onaylanmadan üretilmez. R3 promptunda
kilitlenecekler:
"exactly 2.10 m tall, a full head taller than a 1.81 m man beside
it · seamless one-piece pearl-white shell: no panel lines, no
seams, no zips, no fabric joints · absolutely clean: no dust, no
scuffs, no dirt in any crease · the BACK IS SMOOTH AND FLAT: no
backpack, no life-support pack, no hoses, no tubes, no antenna,
no protrusion of any kind · arms noticeably LONG, fingertips
hanging at knee level · each glove has exactly THREE FINGERS AND
A THUMB · a single visor of opaque DARK GREY-GREEN, nearly black,
matte - never white, never mirrored, nothing visible behind it"
```

---

### D-S 🔴 S34 KAMERA ARKADAN — tarla kuralı ölçülemedi

Spec: 20 metreden **yanal (side-on)** kaydırma. Ekranda: yürüyenlerin
**arkasından**, koridora bakan takip.

Bu bir kadraj tercihi değil, **fikrin kendisinin kaybı**. EŞLEŞME
YASASI (her enkazın YANINDA ikizi, aynı eksende) ancak yandan bakınca
okunur — arkadan bakıldığında çiftler üst üste biner ve tarla
"eşleşmemiş hurdalık" olur. Seyircinin geminin başına geleceği anlaması
bu tek kadraja bağlıydı.

**Yeniden üretim dili — hareket cümlesi başa alınır:**

```
CAMERA POSITION IS THE SUBJECT OF THIS SHOT: the lens is BESIDE the
walkers, twenty meters to their SIDE, perpendicular to their path,
at head height. It NEVER stands behind them and NEVER looks down
their path. The frame is a moving side elevation: the walkers cross
it left to right in profile, and behind them each wreck and its grey
twin stand SIDE BY SIDE across the frame width, both fully visible,
neither hidden behind the other. If you can see the walkers' backs,
the shot is wrong.
```

---

### D-T 🔴 S37 ARKA PLANDAKİ ORİJİNAL DÜŞTÜ — sahne bilgisiz kaldı

Rapor: *"the background blurred orange stripe is entirely missing.
There is no original behind the copy to teach the limit of the rule."*

Kadraj teknik olarak temiz (el yüzeye batmıyor, taş deforme olmuyor,
renk sızmıyor) ama sahnenin **BİLGİSİ** yok. RENK YASASI karşılaştırma
gerektirir: gri şerit yuvası + arkada aynı panel dizisinin turuncu
şeridi. Orijinal düşünce, sahne "gri duvara dokunan el" oluyor.

Bu, F3 D-I ile aynı aile ve artık bir sınıf:

```
SAHNENİN BİLGİ TAŞIYICI ÖĞESİ DÜŞÜYOR, DEKORU KALIYOR.
F3 S22: eldiven hiç çıkmadı, kadraj kaldı → Ç7 kurulumsuz.
F4 S37: karşılaştırma öğesi yok, dokunuş kaldı → renk yasası
        öğretilmedi.
Karşı önlem: bu tür sahnelerin promptu "THE ONLY EVENT OF THIS SHOT
IS ___" cümlesiyle AÇILIR ve o öğe negatif blokta da tekrarlanır.
```

**Yeniden üretim dili:**

```
THE ONLY POINT OF THIS SHOT IS A COMPARISON, and both halves must be
in frame: sharp in the foreground, the grey stone flank with the
raised edge lip of a stripe that has NO COLOUR; and behind it, soft
but UNMISTAKABLY VISIBLE and unmistakably ORANGE, the same panel run
on the weathered original. If the orange stripe is not in the frame,
the shot has failed.
```

---

### D-U 🟡 S36 AYNA ŞÜPHESİ — F3 D-H'nin ikinci vakası, aynı test

Rapor: yara izi SAĞ kaşta (spec: SOL). Ama raporun kendi pasaport
satırı şerh düşüyor: *"a visible scar on her RIGHT eyebrow (viewer's
left)"* — yani denetçi **özne-solu / ekran-solu** ayrımında tereddütlü.

F3'te bu tam olarak yaşandı ve kural yazıldı: **karar tek kare insan
gözüyle verilir, rapora güvenilmez.**

```
TEK KARE TESTİ (ücretsiz, 30 saniye):
S36'dan bir kare al. Kadraj onun SOLUNDAN üç-çeyrek yakın plandır.
Yara izi hangi kaşta? Aynı karede ORANGE takviye omuzda mı duruyor?
  → İkisi birden ters ise: klip yatay FLIP yemiş. Kurguda geri
    çevir, yeniden üretim GEREKSİZ.
  → Yalnız yara ters ise: R1 çapasının kendisi kontrol edilir;
    S36 yeniden üretim listesine girer.
  → İkisi de doğru ise: rapor bulgusu düşer, hiçbir şey yapılmaz.
Bu test D-H'de de yapılmadı — iki fazın açık sorusu aynı testle
kapanır.
```

---

### D-V 🟡 S31 GHOSTING + EXTEND YİNE ATLANDI (dört segment kısa)

**İki bulgu, muhtemelen tek kök:**

```
① S31 0:04'te "transparent duplicates of the walkers split off and
   overlay the frame" — figür üremesi DEĞİL, temporal artefakt.
② Süreler: S31 8 s · S34 8 s · S35 8 s · S40 9 s. Toplam 93 s.
   A yolunun 9 sahnesinin HEPSİ 10.00 s'ye tamamlanacaktı [KARAR 4 ③].
```

Ghosting tipik olarak **kare interpolasyonlu extend/retime** artefaktıdır.
S31 hem ghosting taşıyor hem 8 s ölçülüyor — yani ya extend denendi ve
bozuldu (klip geri alındı ama artefakt kaldı), ya da başka bir işlem
uygulandı. Teşhis edilmeden yeniden üretim kararı verilmez.

⚠️ **Süre ölçümü şerhi (F3 §4):** modelin süre ölçümü rapor verisi
değil, yalnız mod seçimi girdisidir — F3'te aynı dosya iki koşuda 87 s
ve 96 s ölçülmüştü. Dört segmentin kısa çıkması tutarlı bir örüntü ama
**kesin süre NLE'de doğrulanır.**

D-N (F3) böylece kapanmadı, ikinci kez açıldı: **extend adımı üretim
akışında bir kontrol maddesi değil, bir alışkanlık olarak duruyor.**
Montajdan önce zorunlu kontrol: `10 klip × 10.00 s`.

---

### D-W 🟡 S38 KOMPOZİSYON KAYMASI — flu omuz sırta döndü

*"The woman is mostly in frame from behind, rather than just a soft
foreground shoulder."* Sahne çalışıyor (taş figür kusursuz: *"flawless
execution"*), ama ön plan büyüdükçe gerilim düşüyor: kadraj "bir kadın
bir şeye bakıyor"a dönüyor, oysa istenen "biz onun omzundan bakıyoruz".

YELLOW — S39'un yeniden üretimiyle birlikte değerlendirilir; tek başına
yeniden üretim bütçesi hak etmiyor. Düzeltme dili:

```
Only her SHOULDER and the rim of her helmet enter the frame at the
extreme near LEFT edge, heavily out of focus, occupying less than a
fifth of the frame width. Her back is NOT in frame; her body is NOT
in frame; we are looking past her, not at her.
```

---

## 4. RUBRİK İŞLEYİŞİ — ne çalıştı, ne düzeltilecek

**Çalışanlar:**
- **İçerik-satır çelişki kuralı ÜÇÜNCÜ kez yakaladı** (F1 rotasyonu →
  F3 beş misfile → F4 ikili takas). Sessiz düzeltmeye kaçmadı, iki
  segmenti de bulgu olarak yüzeye çıkardı. Bu tasarım artık kanıtlanmış
  sayılır.
- **MOST LIKELY FAILURE satırları üç sahnede birebir gerçekleşti**
  (S35 gömülü gemi · S39 vizörde yüz · S40 kirlenen beyaz suit). Bu
  satırlar artık yalnız denetçi uyarısı değil, **prompt düzeltmesinin
  doğrudan girdisi** — F5 rubriğinde bu satırlar yazılırken "en olası
  hata" değil "geçen sefer olan hata" listesi kullanılır.
- **WHITE FIGURE LEDGER** ilk koşuda amacını verdi: dokuz satır temiz,
  onuncu satır spec kontrolü. Erken figür kilidinin tuttuğunu tek
  bakışta gösterdi.
- **COPY MATERIAL TABLE** malzeme sapmasını sahne sahne verdi ve
  S35'in üç yasadan birden düştüğünü ayrıştırdı.
- FLAGS üç doğru soru üretti (klip sırası · S35 gemi anahtar kelimeleri ·
  S39 negatif ağırlık) — üçü de §5 aksiyonlarına dönüştü.

**Düzeltilecekler (F5 rubriğine taşınır):**

```
① KATEGORİ 3 İKİYE BÖLÜNÜR
   Şu hâlde "beyaz figür erken göründü mü" ile "Bekçi spec'i tuttu mu"
   aynı skorda toplanıyor; koşu 9/9 temiz erken-kilide ve tamamen
   batmış bir Bekçi'ye tek sayı (4) verdi. İki ayrı ölçüm:
     3a. ERKEN FİGÜR KİLİDİ  (S31-S39, ledger'dan)
     3b. BEKÇİ SPEC UYGUNLUĞU (S40, yedi maddelik kontrol)
② MODE R ARTIK KAPI
   "MODE T tercih edilendir" yetmedi. F5 rubriğinde: tek reel gelirse
   rubrik REEL RECEIVED — SPLIT REQUIRED yazıp durur; MODE R yalnız
   operatörün ilk satıra yazdığı açık bir izinle çalışır.
③ S39 SATIRINDAKİ "RECESS" DİLİ DEĞİŞİR
   Rubriğin kendisi "deep visor recess" diyerek oyuğu meşrulaştırıyor.
   Yeni dil: "the visor area is SOLID, FLUSH STONE - no recess exists;
   a visible cavity of any depth is itself the finding."  [D-Q]
④ KAMERA POZİSYONU KENDİ SATIRINI ALIR
   S34'ün yanlış açısı kategori 6'nın (kamera disiplini) içinde eridi
   ve "kesme yok, hız sabit" ile aynı torbaya girdi. Oysa yanlış açı
   fikri öldürüyor. Sahne satırlarına zorunlu "CAMERA POSITION" ilk
   maddesi + rapora KAMERA POZİSYON TABLOSU eklenir.  [D-S]
⑤ SÜRE ÖLÇÜMÜNE ŞERH RUBRİĞE YAZILIR
   Model süre ölçümünü rapor verisi sanıyor; F3'te aynı dosyayı 87 ve
   96 s ölçtü. Rubrik satırı: "your duration measurement selects the
   mode; it is not evidence. Report it, do not conclude from it."
```

---

## 5. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ KURGU (bedava): 2↔3 takasını düzelt. Klip dosya adlarına sahne
     numarası yaz (s31.mp4 … s40.mp4) ve klipleri AYRI tut.
2. □ TEK KARE TESTİ (D-U): S36'da yara izi + ORANGE omuz aynı karede
     hangi tarafta? Flip ise kurguda geri çevir (bedava); değilse S36
     yeniden üretime girer. ⭐ Aynı test F3 D-H'yi de kapatır.
3. □ SÜRE DOĞRULAMASI (D-V): NLE'de gerçek süreler ölçülür. Kısa
     çıkan her klip 10.00 s'ye extend edilir; S31'in ghosting'i
     extend/retime kaynaklı mı, üretim kaynaklı mı teşhis edilir.
4. □ ⛔ ÇAPA KAPILARI — bunlar açıkken hiçbir yeniden üretim başlamaz:
     a) R3 BEKÇİ MASTER plakası üretilir ve insan gözüyle onaylanır
        [D-R · Ders 68 ②] — F5'in yedi Bekçi sahnesinin ön koşulu
     b) S32 TAŞ MALZEME ÇAPASI yeniden üretilir ve onaylanır [D-P]
        → S35 bu çapa onaylanmadan denenmez (zincir kuralı, KARAR 2)
5. □ YENİDEN ÜRETİM (kırmızılar, çapa sırasına göre):
     S32  taş malzeme + kum şelalesi temizliği [D-P]  ← ÖNCE BU
     S35  taş monolit dili + pencere/radar negasyonu + taban çizgisi
          [D-O] · en az 4 varyasyon, bütçe zaten yazılı
     S34  yanal kamera pozisyonu [D-S] + 10.0 s
     S37  arka planda turuncu şeritli orijinal [D-T]
     S39  vizör oyuğu → dolu taş [D-Q]
     S40  R3 çapasıyla Bekçi [D-R] + 10.0 s
     S31  ghosting teşhisi sonrası karar [D-V] + 10.0 s
     S36  D-U sonucuna göre (flip ise üretim yok)
6. □ İKİNCİ KOŞUDA KARAR (şimdilik yeniden üretme):
     S33  kök damarları mat mı — gerçek klip kendi satırında
          ölçülmedi (takas)
     S38  ön plan omuz kadrajı [D-W] — YELLOW, S39 ile birlikte
7. □ RUBRİK YAMASI: §4'teki beş madde `FAZ_04_QA_PROMPT.md`'ye ve
     F5 rubriğine işlenir.
8. □ Düzeltilmiş 10 klip ile İKİNCİ KOŞU, MODE T ile — 5.2 skoru
     karşılaştırma tabanı değildir, taban ikinci koşudur.
9. □ Tutan prompt sürümlerini (S38 malzemesi, S40 hareket dili, ışık
     bloğu) `FAZ_04_TARLA.md`'ye işle.
```

---

## 6. F5+ VE SİSTEME TAŞINANLAR

```
① MODE T KAPISI            Reel ile QA koşusu yapılmaz. Dört fazın
                           üçünde reel sırası karıştı; MODE T hiç
                           denenmedi. [§1 · F3 dersi ④'ün sertleşmişi]

② ÖZNE = MALZEME,          "taştan gemi" değil, "gemi biçiminde taş".
   NESNE = SIFAT           Adlandırdığın şeyin klişesini alırsın:
                           gemi dersen pencere/radar/pas gelir.
                           [D-O · F3 D-J'nin nesne versiyonu]

③ IŞIKSIZ PENCERE DE       Negasyon ışığa değil DELİĞE yazılır:
   PENCEREDİR              "no lit windows" → "no windows at all,
                           no openings of any kind, lit or unlit".
                           [D-O]

④ BOŞLUĞU YASAKLAMA,       Model oyuk görürse doldurur. "İçine şunu
   DOLDUR                  koyma" listesi uzatmak işe yaramıyor;
                           "orada oyuk yok, dolu taş var" işe yarıyor.
                           En genellenebilir F4 dersi. [D-Q]

⑤ KAMERA POZİSYONU         Yanlış açı = fikrin kaybı, kadraj tercihi
   FİKRİN KENDİSİDİR       değil. Bir sahnenin anlamı pozisyona
                           bağlıysa prompt o cümleyle AÇILIR ve
                           "if you can see X, the shot is wrong"
                           testiyle kapanır. [D-S]

⑥ SAHNENİN BİLGİ           F3 S22 eldiven · F4 S37 orijinal şerit:
   TAŞIYICISI DÜŞÜYOR      dekor üretiliyor, olay üretilmiyor.
                           Karşı önlem: "THE ONLY EVENT OF THIS SHOT
                           IS ___" açılışı + negatif blokta tekrar.
                           [D-T]

⑦ ÇAPA ZİNCİRİ VE          "X onaylanmadan Y üretilmez" kapıları
   TETİK KAPILARI          ÜÇÜNCÜ kez atlandı (F2→F3 D-G, F4 S40
                           D-R, F4 S32→S35 D-P). Her atlamada faz
                           maliyeti ikiye katlanıyor. Kapı artık
                           üretim öncesi kontrol listesinde madde
                           olarak durur, prompt içinde not olarak
                           değil. [Ders 68 ②]

⑧ EXTEND BİR ADIM,         D-N ikinci kez açıldı. Montaj öncesi
   ALIŞKANLIK DEĞİL        zorunlu kontrol: "10 klip × 10.00 s".
                           Ghosting artefaktı bu adımın nasıl
                           uygulandığıyla ilgili olabilir. [D-V]

⑨ ÖNGÖRÜLEN HATA =         Rubriğin MOST LIKELY FAILURE satırları üç
   PROMPT MADDESİ          sahnede birebir gerçekleşti. Bir hatayı
                           öngörüp yalnız denetçiye söylemek onu
                           engellemiyor — aynı cümle PROMPTA da
                           girmeli. [§4]
```

**Sisteme (depo geneli) aday dersler:** ④ (boşluğu doldur) ve ② (özne =
malzeme) tür-bağımsızdır ve `LESSONS_LEARNED.md` dizinine girmeye
adaydır — AGENTS.md kart G ile işlenir, önce kaynak rubrik
(`FAZ_04_QA_PROMPT.md`) yamalanır.

F3'ün bekleyen aksiyonlarıyla birleşik durum: `../FAZ_03_IMDAT/
FAZ_03_QA_DERSLER.md` §5 (D-H tek kare testi · hasar çapası · altı
yeniden üretim) hâlâ açık; D-H artık D-U ile aynı testle kapanabilir.

---

> **Bu dosya ne zaman güncellenir:** tek-kare testi (D-U) sonuçlanınca,
> R3 Bekçi çapası ve S32 malzeme çapası onaylanınca, yeniden üretimler
> bitince ve düzeltilmiş 10 klip MODE T ile ikinci kez koşulduğunda.
