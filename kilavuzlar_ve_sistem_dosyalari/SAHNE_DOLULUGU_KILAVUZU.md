# ⏱️ SAHNE DOLULUĞU KILAVUZU — On Saniyelik Birim Nasıl Dolu Yazılır

> **Neden var (15.09.2026):** sahibin sorunu — *"10 saniyenin sahnelerinin
> bazılarında 3 saniyede iş bitiyor, kalan 7 saniye boş geçebiliyor, boş boş
> durabiliyorlar."* 48 × 10 s'lik filmde boş kalan her 7 s filmin %70'idir.
> Depodan ölçüldü (`URETIM_ONCESI_ANALIZ/doluluk_olcum.py` · 15.09.2026
> kesiti): 1440 video promptunun **son vuruşlarının %59'u durgunluk kelimesi
> taşıyor** (settles · holds · stays · nothing else moves); "motionless" 141,
> "stands still" 50, "then stops" 13 promptta. Damga yazılıyor (1313/1440),
> fiil de geç yazılıyor (%69'unda ≥ 8 s) — ama son satıra yazılan şey
> DURGUNLUK. Şablonun kendi kilit örneği bile *"turns one quarter, then
> stops, and nothing else in frame moves"* diyordu. QA korpusu görüyor ama
> adı yoktu: "remains static" 10, "plateau" 31 raporda; *"She breathes, but
> otherwise, nothing happens."*
>
> **Ölçülmüş kök sebep (TUR 19):** model yazılanı üretir. Noktasal fiil
> ("grabs · turns · notices") bir anda biter; motor eylemi ilk saniyelere
> yığar, bitince donar / döngüye biner / boş salınır; görüntüden-videoya
> hattında ilk kareye bağ bunu büyütür. "holds / settles / still" optik
> akışı sıfırlar. Yani kalan 7 saniye "motorun hatası" değil, PLANIN
> BOŞ BIRAKTIĞI YERDİR. Üç bağımsız araştırma (motor · zanaat · senaryo)
> aynı üç cevaba geldi: kilit fiili SÜREÇTİR · başlangıç karesi eylemin
> ORTASIDIR · son üçte bir YERLEŞME değil SÜRDÜRMEDİR.
>
> **Ne zaman okunur:** sahne tablosu (`00_SAHNE_TABLOSU`) ve sahne çalışması
> yazılırken — her sahnede; IMAGE ve VIDEO promptu yazılırken. Bu dosya
> OYUNCULUK_YAZIM'ın (beden NEDEN yapıyor) ve D169'un (beden ÖDÜYOR mu)
> üçüncü ayağıdır: beden ON SANİYE BOYUNCA NE YAPIYOR.
>
> **Kaynak:** `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 19
> (T19.0 · T19.1 · T19.2 #1-15 · T19.3) + `22_SAHNE_DOLULUGU_ARASTIRMA_PROMPTLARI.md`
> teşhisi + ham `TUR19_HAM_RAPORLAR/`. Dış sayılar ETİKETLİDİR; bu kılavuz
> SAYISIZ yazıldı (T19.8 ⑥).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① HİÇBİR KALIP ÜRETİMDE SINANMADI. Üç rapor mekanizmada birleşti, sayıda
   çürüdü (yüzdeler, saniye eşikleri, kare sayıları künyesiz). Burada
   eşik yok; iki tasarım sayısı var: TIMELINE ≤ 3 satır · TEK çevre saati.
   İlk 48 × 10 s filmde ⬜ hareket profili (§5) ve ⑭ HAREKET sınavdır.

② DOLU ≠ HAREKETLİ. Saati çalışan tutulmuş plan doludur; koşan ama amaçsız
   beden boştur (⑭'ün alanı — amaçsız hareket). Bu dosya hareket YOKLUĞUNU
   yazar; hareketin amacını OYUNCULUK_YAZIM §1-§3 yazar; efor bedelini
   D169/⑳ yazar. Aynı sahne üçünde de düşebilir — üç eksen.

③ DURUM DEĞİŞİMİ KURALI KORUNUR. Klip içinde A → B (kapak açılır · lamba
   yanar · ip kopar) ölçülmüş en zayıf eksendir [REHBER §7 · SAHNE_ZINCIRI
   §1]; değişim sınıra yazılır. Bu yüzden doluluk HAREKET ve SÜREÇTEN gelir,
   dünyanın durum değiştirmesinden değil. Kesinti bile DİRENÇTİR, kırılma
   değil (§2 ②).

④ IZGARA SABİTTİR. "Klibi 6 saniyede kes" bir kurgu kararıdır (KURGU_RITMI
   §1 · D100 kırpma tablosu), bu dosyanın çözümü değil. 10 saniye
   doldurulur, kısaltılmaz.

⑤ BU DOSYA ⑫ RETANSİYON DEĞİLDİR. ⑫ filmin platosunu ölçer; burası tek
   birimin içini yazar. 48 birimin tempo dağılımı OYUNCULUK §4'tedir
   (Y/N/H · ≥3 değişim · ardışık üç aynı yok) — burada tekrar edilmez.

⑥ YENİ YASAK YOKTUR. "still / motionless / frozen tek başına yazılmaz"
   OYUNCULUK §4'ün kuralıdır (T15.2 #24); bu tur üç raporla ikinci kez
   doğrulandı ve listesi §4 ⑥'da genişletildi (holds · settles · comes to
   rest · then stops · nothing else moves). Kural aynı, gerekçesi büyüdü.
```

---

> 🆕 **22.09.2026 · ÇOK KLİPLİ SAHNE:** bu kılavuzun birimi KLİPTİR ve o rejimde
> de aynen geçerlidir (üç evre · ≤3 TIMELINE satırı · son satır SÜRDÜRME). Rejimin
> eklediği tek şey: sahne fiili 2-6 klip boyunca SÜRÜP GİDEN bir süreçtir, her klip
> onun bir evresini taşır ve klibin SON'u sonraki klibin `CONTINUOUS ACTION:`
> satırıdır → `COK_KLIPLI_SAHNE_KILAVUZU.md` §5.

# 1. 🔤 FİİL SINIFI — kilit fiili ekranda kaç saniye taşır

Bir birimin üçüncü satırı sahnenin TEK KİLİDİDİR (V3). O kilidin fiili
klibin süresini belirler — sayısı değil, SINIFI (Vendler; T19.2 #2).

```
SINIF          İNGİLİZCE ÖRNEK                 EKRANDA           BİTİNCE BEDEN
─────────────  ──────────────────────────────  ────────────────  ─────────────────────
DURUM          holds · remains · sits ·         süre taşımaz      tam durur → donma /
               stands · waits · stays                              boş salınım
ERİŞME         grabs · turns · notices ·        bir anda biter    donar, döngüye biner
(noktasal)     reaches · drops · steps in ·                       ya da uydurur
               presses · closes
ETKİNLİK       hauls · walks · climbs · drags ·  sınıra kadar      kesmede hâlâ
(süreçli,      pushes · works at · keeps X-ing   sürer             yapıyor
bitişsiz)
TAMAMLAMA      works the seal loose · crosses    doğal sona doğru  sona VARMADAN
(süreçli,      the span · winds the strap ·      ilerler           kesilirse sürer
bitişli)       hauls the crate to the hatch
```

```
⭐ KİLİT FİİLİ KURALI
   □ Kilit ETKİNLİK ya da TAMAMLAMA'dır.
   □ ERİŞME ancak DÖRT EKTEN en az ikisiyle tamamlamaya çevrilirse kilit olur:
        DİRENÇ   paslı · sıkışmış · ağır · kaygan — "it gives a finger's width"
        AŞAMA    üç çentik · iki tur · yarım kol boyu — görünür ilerleme
        ALET     manivela · anahtar · halat — el ile nesne arasında üçüncü şey
        AĞIRLIK  gövde ağırlığı işe biner — "leans his weight into"
     ✗ "He turns the wheel."
     ✓ "He works the stiff wheel a quarter-turn at a time, leaning his
        weight into each pull; by the end it has moved three notches."
   □ DURUM fiili kilit OLAMAZ. "He holds the rail" bir kilit değil, bir
     pozdur; kilit "his grip on the rail tightens and eases with each swell"
     olur (fiille yazılmış tutuş — §3 ③).
   □ TAMAMLAMA'nın SONU klibin İÇİNDE değildir: sona vardığı an klip biter
     (§2 ③ erken çık). "opens the hatch" yazılmaz; "works the hatch wheel;
     it is a hand's width open at the cut" yazılır.
   □ Sıfat/zarf hız vermez, ORAN verir [D169 "sayı yaz, sıfat değil"]:
     ✗ "slowly pulls"  ✓ "pulls at one steady rate, one arm's length every
     two seconds".
```

> 🔗 Kuvvet fiili sözlüğü (heave · strain · lean into · drag · pry) D169'da;
> burada yeni olan SEÇİM kuralıdır: kilit fiili o sözlükten ve süreç
> sınıfından gelir.

---

# 2. 🧱 ON SANİYE İSKELETİ — üç evre, üç TIMELINE satırı

Bir birim üç evredir; TIMELINE ÜÇ SATIRI GEÇMEZ (T19.2 #6: dört ve üstü
vuruş motorda sıkışır ya da yutulur). Her satır bir evre, her evrede ≥1
gövde fiili.

```
EVRE ①  GİRİŞ — EYLEM ZATEN BAŞLAMIŞ                          (kısa)
        İmaj promptu bedeni YÜK ALTINDA yazar: gövde eğik, eldiven kapalı,
        halat gergin. Nötr poz ilk saniyeleri "eyleme giriş"e harcar ve
        motor kalanı boşaltır (T19.2 #3 · "geç gir"). I2V'de imaj = ilk
        kare [D179] → bu, IMAGE promptunun kuralıdır: sahne "ortasından"
        başlar.
        ✗ imaj: "he stands at the valve bay, one hand on the wheel"
        ✓ imaj: "both gloves closed on the rim, torso leaning into the wheel,
           rear boot braced against the deck ridge"
        ⚠️ 16.09.2026 TUR 20 (T20.1 3↔4): ORTASI AMA DENGEDE — iki destek
           noktası yerde (iki bot · diz + bot · el + bot); adım ortası,
           sıçrama, düşüş anı değil (kayan ayak / askıda kalma riski).

EVRE ②  DİRENÇLİ İLERLEME                                     (en uzun)
        Kilit fiili çalışır ve BİR direnç görür: takılma · ağırlık · kayma
        · ikinci deneme. Direnç bir olay değil, işin dokusudur. Kesinti
        varsa DİRENÇTİR, kırılma değil (§0 ③):
        ✗ "the rung snaps"      ✓ "his boot slips off the rung and finds it
                                   again; he climbs on at the same pace"
        ✗ "the wheel jams"      ✓ "the wheel gives a finger's width and grips;
                                   he resets his hands and pulls again"

EVRE ③  SÜRDÜRÜLEN SONUÇ ya da ERTELEME                        (son üçte bir)
        Eylem SÜRERKEN kesilir; beden bitmiş hâlde kapanmaz. Sonuç kısmi
        (üç çentik · yarım el · bir kol boyu) ya da ertelenmiş (sonraki
        birim). Yerleşme dili YASAK — sürdürme dili:
        ✗ "he settles back and rests"
        ✗ "then stops, and nothing else in frame moves"
        ✓ "keeps hauling at the same steady rate through the last second;
           nothing in his grip relaxes"
        ✓ "his shoulders rise once with a slow breath; the strap goes on
           swinging at the same rate"
        Sonraki birim eylemin SONRASINDAN açılır (SAHNE_ZINCIRI §5 sınır
        satırı: End = sürerken · Start = sonrası).
```

```
BİRİM MİKRO-SORUSU (T19.2 #12)
   0 s'de fiziksel bir soru açılır — beden nereye yöneliyor, hangi nesneye
   hangi kuvvet — 10 s'de kısmen cevaplanır ya da ertelenir. Sorusu olmayan
   birim, işi bitince boşalır. Soru sözle değil bedenle: "will the wheel
   move" = eğik gövde + kapalı eldiven + gergin kol.
   SAHNE_ZINCIRI §2'nin AÇILAN SORU'su sınırdadır; buradaki soru birimin
   içindedir — ikisi aynı sahnede olur.
```

## 2.1 Dört iskelet çeşidi — hangi sahneye hangisi

| İskelet | Evre ① · ② · ③ | Son üç saniye ne gösterir | Sahne tipi | İngilizce tek satır (kısıta uyar) |
|---|---|---|---|---|
| **PROSEDÜREL İŞ** | yük altında temas · dirençli ilerleme (aşama + alet) · sürdürülen kısmi sonuç | nesne kısmen yol almış, beden hâlâ işte | tamir · mühür · kilit · kapı zorlama · yükleme | *He works the stiff wheel a quarter-turn at a time, leaning his weight into each pull; it grips and gives; by the cut it has moved three notches and he is still pulling.* |
| **KESİNTİLİ SÜREÇ** | eylem sürüyor · direnç/kayma · aynı tempoda devam | kaymadan sonra eylem aynı oranda sürer | tırmanma · geçit · taşıma · kaçış | *He climbs the ladder at one steady pace; midway his boot slips off a rung and finds it again; he climbs on at the same pace to the cut.* |
| **SAATLİ TUTUŞ** | bedende üçlü başlar · dış saat çalışır, bakış hedefi sabit · tek mikro-ayar | nefes + saat + mikro-ayar; tam durma yok | saklanma · bekleyiş · dehşet · dinleme | *He keeps his chest still but for one slow breath every few seconds; his eyes track the shadow crossing screen-left to screen-right; one glove closes and opens once at his side; the strap behind him swings at one steady rate.* |
| **TOHUM VE ERTELEME** ⬜ | ana iş + kadraj kenarında ikincil öğe · iş sürer · öğe ORAN değiştirir | ikincil öğe hızlanmış, ana iş sürüyor; ödeme SINIRDA | basınç · sızıntı · geri sayım | *While he works the seal, the drip from the valve quickens through the clip, one drop every three seconds at the start, one every second by the end; he does not look up.* (⬜ oran değişimi klip içinde tutar mı — T19.8 ④; tutmazsa ödeme sonraki birime) |

> ⛔ Hiçbir iskelet klip içinde DURUM DEĞİŞTİRMEZ (kopar · patlar · açılır ·
> yanar). Tohum-ödemenin ödemesi de bir SINIR olayıdır; klipte yalnız oran
> hızlanır ve bu bile hipotezdir.

---

# 3. 🕰️ DOLGU KAYNAKLARI — ana eylem bitince göz neden kalır (sıra, sayı yok)

Üç rapor aynı sırayı verdi (T19.2 #7); saniyeleri künyesiz, sıra iner:

```
1. GÖRÜNÜR İLERLEMESİ OLAN İŞ     tek başına ON SANİYE taşıyan TEK kaynak:
                                  direnç + alet + aşama + ikinci deneme
2. SAATLİ TUTUŞ                   bedende üçlü + kadrajda BİR dış saat
3. İKİNCİ GÖREV                   ana iş sürerken öteki el / ayak ikinci işte
4. MOVING HOLD (fiille)           nefes · tutuş gerilimi · ağırlık — TEK BAŞINA KISA
5. SAATSİZ BEKLEYİŞ               en kısa ömürlü: göz kadrajı terk eder (rapor 2)
```

```
① İKİNCİ GÖREV — "sahne işi"nin depo hâli
   Ana iş sürerken ikinci bir şey daha yapılır; ana işi gölgelemez, sahne
   başına BİR tane. Dolgu jesti DEĞİLDİR (OYUNCULUK §6'nın yasak listesi —
   eldiven/kask/omuz düzeltme — burada da yasaktır): ikinci görev işin
   parçasıdır.
   ✓ "his left glove keeps the coil from unwinding while his right works
      the seal"
   ✓ "his rear boot holds the crate from sliding while both hands work
      the strap"

② ÇEVRE SAATİ — TEK, PERİYODİK, ORANLI
   Kadrajda bir şey sabit oranda hareket eder: sallanan kayış · damlayan
   sıvı · yürüyen gölge · dönen çark · nefesle bulanan vizör. Kural:
   □ sahne başına BİR saat (ikincisi gürültü; motorda döngü/doku bedeli —
     T19.1 1↔2)
   □ ana eylemle çelişmez (beden yukarı çekerken kayış aşağı sallanmaz)
   □ ORAN cümlesiyle yazılır: "at one steady rate" · "once every few
     seconds"; sayılı oran SPEC kanıtıysa yazılır [D141] — ⬜ periyot sayımı
     motorda tutmayabilir (T19.8 ③)
   □ "never hovering" çekirdek satırına takılan şeyler saat DEĞİLDİR: toz
     perdesi, süzülen parçacık, "subtle mist" (SAHNE_ZINCIRI §1 uyarısı)
   □ saat kadraj KENARINDADIR; merkez bedenindir

③ TUTULAN PLAN — üçlü + DIŞ SAAT
   OYUNCULUK §4'ün üçlüsü (nefes · sabit bakış hedefi · tek mikro-ayar) tek
   başına KISA taşır (rapor 2: moving hold). Tutulan plan on saniye
   sürecekse dördüncü şart DIŞ SAATTİR (②). Dördü de FİİLLE yazılır; tam
   durma hiçbir karede yoktur:
   ✗ "He holds absolutely still. Nothing moves."
   ✓ "His shoulders rise once with a slow breath and ease; his eyes stay on
      the hatch; his right glove tightens on the rail and eases; behind him
      the strap swings at one steady rate."

④ GÜRÜLTÜ SINIRI
   İkinci saat · ikinci görev + saat + mikro-ayar üst üste · ana işle
   çelişen ikincil hareket → "fidgety noise" (rapor 2 eleştiri sözlüğü) ve
   motorda doku erimesi / kayan ayak (rapor 1). Sahne başına: BİR kilit +
   BİR direnç + (BİR ikinci görev YA DA BİR saat) + nefes. Fazlası çıkar.
```

---

# 4. ✍️ MOTOR TARİF BİÇİMİ — İngilizce kalıplar

```
① KİLİT SATIRI (üçüncü satır, V3) — süreç fiili + oran/aşama
   "He works the stiff wheel a quarter-turn at a time; by the cut it has
    moved three notches."
   "She hauls the crate along the deck at one steady pace, one arm's
    length every two seconds."

② SÜRDÜRME CÜMLESİ — TIMELINE'ın SON satırı, her birimde
   "…keeps hauling at the same steady rate through the last second; nothing
    in his grip relaxes."
   "…goes on turning the wheel at the same pace; his shoulders rise once
    with a slow breath and drop back into the pull."
   ⛔ "settles" · "comes to rest" · "holds still" · "then stops" · "nothing
      else moves" bu satırda YAZILMAZ.

③ ZEMİN BAĞI — ikincil hareket istenen her sahnede
   "Both boots stay planted, his weight on the front foot."
   "Her knees stay on the deck; only the arms and shoulders work."
   (rapor 1: çevre/kumaş hareketi istenince kayan ayak ve süzülme bedeli —
    zemin bağı cümlesi onu keser.)

④ TEK ÇEVRE SAATİ
   "Behind him the loose strap swings at one steady rate."
   "A drop falls from the valve lip once every few seconds."
   (bir tane · kenarda · oranlı · ana eylemle uyumlu)

⑤ MOVING HOLD — yalnız fiille
   "his shoulders rise once with a slow breath and ease"
   "the right glove tightens on the rail and eases"
   "the helmet stays on the horizon" (bakış hedefi — bu "stays" nesnenin
    yönüdür, bedenin durgunluğu değil; tek başına yazılmaz, üçlünün parçası)

⑥ YAZILMAYANLAR — tek başına (OYUNCULUK §4 listesinin genişletilmiş hâli)
   still · motionless · frozen · stationary · paused · holds still ·
   stays still · remains still · settles · comes to rest · then stops ·
   nothing else moves · nothing in frame moves · waits
   Ne yaptığı yazılır: nefes · tutuş · ağırlık · bakış hedefi · saat.

⑦ DAMGA BİÇİMİ — depo biçimi korunur
   "0.0s — … 4.0s — … 8.0s —"  üç satır, her satırda gövde fiili.
   ⬜ "[00:00-00:04]" köşeli parantez A/B (rapor 1 "Veo resmî"; motor
   desteklemezse HUD basar — yazı yasağı [D34 · D45]) — T19.8 ②.
```

## 4.1 Önce / sonra — şablonun kendi örneği (THE_LOCKED_PULSE S0, V3)

```
ÖNCE (TEMPLATES V3 kilit örneği · 5 vuruş · son vuruş yerleşme)
  The wheel turns exactly one quarter, then stops, and nothing else in
  frame moves.
  TIMELINE: 0.0s — … 2.0s — … 4.0s — … 7.0s — his shoulders settle back a
  finger's width, then lean into the wheel again. 9.0s — …

SONRA (üç satır · kilit süreç · son satır sürdürme · tek saat · zemin bağı)
  He works the stiff hand-wheel a quarter-turn at a time, leaning his
  weight into each pull; by the cut it has moved three notches.
  TIMELINE: 0.0s — both gloves closed on the rim, torso already leaning
  into the wheel, rear boot braced on the deck ridge; the loose strap on
  the left swings at one steady rate. 4.0s — the wheel gives a finger's
  width and grips; he resets his hands without letting go and pulls
  again, shoulders rising once with a slow breath. 8.0s — the wheel moves
  its third notch; he keeps pulling at the same steady rate through the
  last second; nothing in his grip relaxes; the strap goes on swinging.
  Both boots stay planted, his weight on the rear foot.
```

> Sayı cümlesi kilitte kalır (quarter-turn · three notches · one steady
> rate); gövdede derece/metre yok [D138]. Kelime bandı V3 ile aynı (§7).

---

# 5. 📏 ÖLÇÜM — "ölü saniye" ve neden ② onu görmez

```
ÖLÜ SANİYE   bir 10 s'lik klipte hareket enerjisinin eşiğin altında kaldığı
             ARDIŞIK saniye sayısı. Bugün depoda ölçülmüyor: sahne_kapisi.sh
             kesme sayar, olcum_kapisi.sh ışık ölçer, ⑭ HAREKET amaçsız
             hareketi etiketler — hareket YOKLUĞUNU hiçbiri saymıyor.

NEDEN ② GÖRMEZ   tutarlılık skoru doluluğu ölçmez: tamamen statik klip özne
             ve arka plan tutarlılığında EN YÜKSEK puanı alır (rapor 1,
             VBench yönü — ÖLÇÜLMÜŞ). ② DEVAMLILIK 10/10 ve ⑫ plato 4/10
             aynı klipte olabilir; ölü saniye ayrı sayılır.

⬜ HAREKET PROFİLİ (makine kapısı adayı — sahip kararı, yazılmadı)
   hareket_profili.sh <klip|master> [klip süresi]
     ffmpeg kare farkı (select/scene skoru ya da tblend fark ortalaması)
     → saniye başına ortalama enerji → klip başına ölü saniye sayısı ve
     yeri (0-3 / 3-7 / 7-10). Eşik ÖNCE ölçülür, sonra konur: ilk 48 × 10 s
     filmin dağılımı basılır, eşik oradan kalibre edilir (sahne_kapisi.sh
     kalıbı; sayı elle yazılmaz).
   Çıktı SPEC E bloğuna "MAKİNE KAPILARI" satırı olarak girer; ⑭ HAREKET
   rubriğine ⬜ "no purposeful motion in–out" satırı (ilk koşudan önce,
   kategori adları donmadan).

⬜ ㉛ DOLULUK KAPISI (prompt_kontrol · yalnız yeni rejim — yazılmadı)
   TIMELINE son satırında (t ≥ 7 s) gövde fiili yok → FIX
   §4 ⑥ listesinden kelime tek başına → FIX
   TIMELINE > 3 damga → NOT (tasarım sayısı; BLOCK değil)
   Fiil listesi §1'den; o zamana kadar doluluk_olcum.py'nin GUCLU listesi.
```

---

# 6. ✅ ÖLÜ SAHNE KONTROLÜ — yazım anında beş soru + bir hücre

Her sahne için, prompt yazılmadan ÖNCE (T19.2 #11):

```
□ 1. FİİL     Kilit fiili ETKİNLİK/TAMAMLAMA mı? ERİŞME ise dört ekten ≥2
              var mı? DURUM fiili mi? → hayır: eylem ilk saniyelerde biter,
              kalan süre donar
□ 2. DİRENÇ   Orta evrede bir direnç (takılma · ağırlık · kayma · ikinci
              deneme) var mı? → hayır: birimin ortası düşer
□ 3. TEK KİLİT  Birimde tek baskın hareket mi; TIMELINE ≤3 satır mı? →
              hayır: vuruşlar sıkışır, sonuncular yutulur
□ 4. SINIR    9-10. saniyede sonraki birime devredilen somut bir beden/nesne
              durumu var mı; kesme eylem SÜRERKEN mi düşüyor? → hayır: birim
              bitmiş bedenle kapanır, zincir sıfırlanır
□ 5. SAAT     Tutulan ya da uzun birimde kadrajda BİR dış saat var mı? →
              hayır: göz kadrajı terk eder
```

```
"SON 3 s" HÜCRESİ — 00_SAHNE_TABLOSU'na sütun (⬜ şablona işlenmedi;
o zamana kadar sahne çalışmasına satır):
   S07 | … | SON 3 s: keeps pulling, wheel on third notch, strap swinging
   Hücre boşsa ya da fiili ERİŞME/DURUM ise sahne yazılmadan yakalanır
   (㉚ tabloyu sayıyor; sütun da sayılabilir — ㉛ adayı).
```

---

# 7. 📋 NEREYE YAZILIR

```
00_SAHNE_TABLOSU   "SON 3 s" hücresi (⬜ sütun) + olay hücresinde SÜREÇ fiili
SAHNE ÇALIŞMASI    §6 beş soru · iskelet çeşidi (§2.1) · dolgu kaynağı (§3)
IMAGE PROMPT       EVRE ①: beden yük altında — sahne "ortasından" (§2 ①);
                   imaj = BEFORE (D179) ile aynı kare, ama nötr poz DEĞİL
VIDEO PROMPT       üçüncü satır = süreç fiilli kilit (§4 ①) ·
                   TIMELINE üç satır, sonuncusu sürdürme (§4 ②) ·
                   zemin bağı (§4 ③) · tek saat (§4 ④)
PLAN               sahne haritası vuruş sütununda fiil sınıfı okunur
                   (D212 ardışık aynı vuruş yasağıyla birlikte)
QA_SPEC            B bloğu FİNAL VURUŞ KANITI oran/adet [D141] — ⬜ "sürdü
                   mü" kalıbına dönebilir (T19.8 ③) · E bloğu ⬜ hareket
                   profili satırı
SINIR SATIRI       SAHNE_ZINCIRI §5: End = eylem sürerken · Start = sonrası
```

---

# 8. ✅ PLAN KONTROLÜ — bu kılavuzun 10 maddesi

```
□ 1.  Her sahnenin kilit fiili ETKİNLİK/TAMAMLAMA mı; ERİŞME'ler dört ekten
      ≥2 taşıyor mu; DURUM fiili kilit değil mi
□ 2.  Her IMAGE promptu bedeni YÜK ALTINDA (eylem başlamış) yazıyor mu
□ 3.  Her TIMELINE ≤3 satır mı; her satırda ≥1 gövde fiili var mı
□ 4.  Her TIMELINE'ın son satırı SÜRDÜRME cümlesi mi; §4 ⑥ kelimeleri tek
      başına yok mu
□ 5.  Orta evrede bir DİRENÇ var mı; kesinti kırılma değil direnç mi
□ 6.  Klip içinde durum değişimi yok mu; değişim sınır satırında mı
□ 7.  Sahne başına en fazla BİR çevre saati, kenarda, oranlı mı
□ 8.  İkinci görev işin parçası mı (dolgu jesti değil); sahne başına ≤1 mi
□ 9.  Tutulan birimlerde üçlü + DIŞ SAAT dördü de fiille yazılı mı
□ 10. "SON 3 s" hücresi her sahnede dolu ve süreç fiilli mi
```

---

# 9. 📚 KAYNAKLAR

```
URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md §TUR 19        süzme kaydı (T19.0 · T19.1 · T19.2 #1-15 · T19.3 · T19.8)
URETIM_ONCESI_ANALIZ/22_SAHNE_DOLULUGU_ARASTIRMA_PROMPTLARI.md   teşhis + üç prompt + ⬜ araştırmasız altı aday
URETIM_ONCESI_ANALIZ/doluluk_olcum.py                            prompt kesiti (son vuruş %59 durgun · damga 1313/1440)
URETIM_ONCESI_ANALIZ/TUR19_HAM_RAPORLAR/                          ham (motor · zanaat · senaryo) + 00_KUNYE
IMAGE_VIDEO_PROMPT_TEMPLATES.md V3                               üçüncü satır kilit · TIMELINE · §4.1'in kaynağı
OYUNCULUK_YAZIM_KILAVUZU.md §4 · §6                              tutulan durgunluk üçlüsü · dolgu jesti yasağı · tempo haritası
SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md §1 · §2 · §5                  durum değişimi sınıra · açılan soru · sınır satırı
KILAVUZ_REHBERI.md §7                                            değişen nitelik (en zayıf eksen) · olumsuz cümle tutmaz
DERSLER/02_KARAKTER_VE_CANLI.md D169                              kuvvet/efor fiili sözlüğü · "sayı yaz, sıfat değil"
DERSLER/06_METIN_VE_PROMPT_DILI.md D179                           imaj = ilk kare (BEFORE)
DERSLER/07_KURGU_VE_ANLATI.md D141 · D212                         final vuruş kanıtı (adet) · ardışık aynı vuruş yasağı
DERSLER/09_SISTEM_VE_SUREC.md D124                                klip süresi araçtan
KURGU_RITMI_VE_IHRAC_KILAVUZU.md §1 · D100                       kırpma bütçesi — bu kılavuzun DIŞI
QA_PROMPTLARI/_KAYNAK/14_HAREKET_QA_CRITIQUE_PROMPT.md           amaçsız hareket (bu dosyanın ölçüm komşusu) · ⬜ hareket-yokluğu satırı
QA_PROMPTLARI/_KAYNAK/12_HOOK_QA_CRITIQUE_PROMPT.md              plato hücresi (film ölçeği)
FILM_QA_RAPORLARI/02_HAM_RAPORLAR/                                "remains static" · "plateau" · "nothing happens" bulguları
```
