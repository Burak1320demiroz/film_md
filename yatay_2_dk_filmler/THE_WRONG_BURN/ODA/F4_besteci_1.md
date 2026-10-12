# F4 · besteci · tur 1 (plan) — THE_WRONG_BURN

```
GİRDİ      FILM.md §1 (hikâye) · §4 (çekim listesi, saniye işaretleri) · §5 (12 replik)
           SAHNELEME.md §5 "Okuma notları" (H01 kuyrukları)
           ODA/F2_diyalog-yazari_3.md §2 (alışveriş/gecikme + SES İPİ + MÜZİK önerisi) · §3 · §4
           ODA/F2_ses-tasarimcisi_2.md (F4'e aktarılacak notlar)
           kilavuzlar_ve_sistem_dosyalari/GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md §10 · §11 · §14 · §15 · §16 · §17
KESMELER   12 × 10 s → kesmeler 10,0 · 20,0 · 30,0 · 40,0 · 50,0 · 60,0 · 70,0 · 80,0 · 90,0 · 100,0 · 110,0 (mutlak).
           `kurgu.py liste --kesmeler` bu aşamada koşulmadı; faz 8'de gerçek çıktıyla kesinleşir.
           Aşağıdaki tüm saniyeler MUTLAK film saniyesidir: Cn içi saniye + (n−1) × 10.
DURUM      PLAN. Saniyeler yaklaşık (±0,5 s). Faz 8'de kesme çıktısı ve ses kaydının gerçek süreleriyle kesinleşir.
```

---

## 1. FILM.md §7'ye YERLEŞTİRİLECEK BLOK

```
OKUMA        İzleyici bu filmi, gözün gösterdiği yola değil sesin tarif ettiği yola tutunmayı —
             titrek bir güveni — olarak okumalı. Tehdit, yas ya da zafer olarak değil.
             Müzik güveni ilan etmez: ilk 35 s gözün yalanına eşlik eder, doruk anında susar, güven
             verildikten sonra tek bir notayla yanına döner.
MÜZİKSİZ     (1) ANA — 35,4–54,8 s (C04 sonu · C05 · C06'nın ilk 4,8 s): Bram'ın sözü ("At sunrise"),
             takas ("might" ve "Your call"), gözlerin kapanması, dönüş ve Sela'nın "You be there"i.
             Karar yalnız sesle ve bedenle verilir; müzik üçüncü bir ses olarak araya girmez.
             Susma doruğun 4,6 s öncesinde başlar: sessizliğin fark edilmesi için zaman.
             Geri dönüş: ateşlemeden 1,1 s sonra TEK NOTA.
             (2) 80,0–96,8 s (C09 ve C10'un ilk 6,8 s): ıska, ip atışı, silkinme (89,7) ve Bram'ın
             hattın başına dönüşü. Müzik C08/C09 kesmesinde kesilir, ıskadan 3,5 s önce; geri dönüş
             Bram'ın "I heard you. In the dark."ından ve Sela'nın takılan nefesinden SONRA, tek nota.
             (3) 117,0–120,0 s: film müzik KESMESİYLE biter; son 3 s'yi Sela'nın oturan nefesi taşır.
             Açılış 0–4,2 s de müziksiz (fan, nefes, "Lost my jets.").
VURUŞ/SUSMA  ≈4,2 L1 girer (replik 1 biter 4,1) · ≈14,6 L2 girer (replik 2 biter 14,1) ·
             ≈35,4 SUSMA, her şey kesilir (replik 6 biter 35,3; replik 7 sessizlikte açılır 36,2) ·
             ≈54,8 TEK NOTA, L1 (replik 9 biter 53,0; tıslama sarsıntısı 53,7) ·
             ≈80,0 SUSMA (C08/C09 kesmesi) · ≈96,8 TEK NOTA, L1 (replik 11 ve bitiş tıkı 96,0;
             Sela'nın nefesi takılır 96,3) · ≈100,0 L3 girer (C10/C11 kesmesi) ·
             ≈112,0 TEK ÇÖZÜLME (ışığın yayılması ortası) · ≈117,0 KESME, bitiş (fade-out yok).
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md
```

---

## 2. KÜNYE (kılavuz §17) — faz 8'in girdisi

```
FİLM                  THE_WRONG_BURN · 2:00 · 12 × 10 s
NOVUM OKUMASI         bkz. OKUMA (yukarıda). Önce bu yazıldı.
MÜZİK-GÖRÜNTÜ İLİŞKİSİ 0–35 s: empatik, ama göze (ışık büyür, müzik de "yaklaşır"; yalan bunun içinde).
                      35–55 s: yokluk. 55 s sonrası: anempatik-sıcak (kimse söylemeden yapılan işi
                      kutlamaz; C11'de Sela'nın ateşlemesine vuruş yok).
TEMPO                 ≈60 BPM, SERBEST. Nabız ve vuruş duyulmaz; sürekli (sustained) dokular.
                      60 seçildi çünkü 1 vuruş = 1 s: bu planın saniyeleri doğrudan vuruşa çevrilir.
                      Kılavuz §14'ün 72 BPM ızgara önerisi (10 s = 3 ölçü) benimsenmedi: besteci kuralı
                      4 vuruşları ızgaraya değil olaya oturtur; her kesme zaten 10 s katında.
TONALİTE              La (A) pedalı. Çözülme: 1 (≈112,0). Başka hiçbir yerde kadans yok.
SESSİZLİK             35,4–54,8 (doruk, ana) · 80,0–96,8 · 117,0–120,0 (müzik kesmesi sonrası)
ÇÖZÜLMEYEN CÜMLE      L2 (göz çizgisi): 14,6'da yükselmeye başlar, 35,4'te cümlenin ortasında kesilir,
                      FİLMDE BİR DAHA GELMEZ. Söz verilip tutulmaz; Sela ışığa sırtını döner.
KAPANIŞ               fade-out YOK. 112,0'da çözülen akor 117,0'da yay kalkarak kesilir (kuyruk yok).
FREKANS TABANI        L1: La pedalı 55 Hz + 110 Hz oktavı EŞİT seviyede (telefonda 110 Hz duyulur).
                      38-46 Hz alanı kullanılmaz, infrases yok (kural 5).
KATMANLAR             L1 pedal (kontrbas+çello) · L2 göz çizgisi (tek yüksek keman) · L3 üst dolgu
                      (viyola: Mi ve Si, 165 Hz üstü). En çok 2 katman aynı anda; hiçbir an 3 değil.
LUFS HEDEFİ           nihai −14 LUFS / −1 dBTP · müzik yatağı −16…−18 · müziğin tepesi (112–117 s)
                      kısa süreli −16'yı aşmaz · replik altı −6…−9 dB
REVERB                kuru (vakum). Hiçbir katmanda yankı, kuyruk, hava yok.
MONO                  tüm alt uç merkezde; mono fold-down'da düşme olmamalı.
```

---

## 3. DİNAMİK TABLO

Yoğunluk 0–5 (0 = müzik yok, 5 = film bu müzikle olabileceği en dolu hâli). Film içinde en yüksek müzik
yoğunluğu 3'tür; filmin doruğu (C06) müziğin en alçak noktasıdır, bu kasıtlıdır.

| # | Bölüm | Çekim | Yaklaşık saniye | Yoğ. | Ne giriyor / çıkıyor | Altında / üstünde ne var |
|:--:|---|:--:|---|:--:|---|---|
| 1 | Açılış | C01 | 0,0–4,2 | 0 | hiçbir şey | fan, Bram'ın acılı nefesi (~2,0), replik 1 (3,0–4,1) |
| 2 | SES İPİ | C01–C02 | 4,2–14,6 | 1 | **L1 girer** 4,2 (La pedalı 55+110 Hz, yay, kuru) | ateşleme tıslaması, replik 2 (12,5–14,1) −8 dB duck |
| 3 | GÖZ | C02–C04 | 14,6–35,4 | 2 (↗3) | **L2 girer** 14,6: tek yüksek keman çizgisi, pedalın üstünde çok yavaş yükselir, askıda; **L1 sürer**. 35,4'te ikisi birden kesilir | replik 3–6 −8 dB; 24,4–26,4 arası (Bram'ın ağır nefesi, "utanç boşluğu") ek −3 dB; 21,6 tıslama kesilmesine müzikle tepki YOK |
| 4 | **SUSKU — doruk** | C04 son · C05 · C06 ilk | 35,4–54,8 | **0** | her şey çıkar. Hiçbir katman yok | replik 7, 8, 9 · kesme 40,0 ve 50,0 sessizlikte · nefes, tıslama (53,7) |
| 5 | TEK NOTA | C06 son · C07 · C08 | 54,8–80,0 | 1 | **L1 geri gelir**, tek nota, ateşlemeden 1,1 s sonra; sürer, başka katman YOK. 80,0'da yay kalkar, kesilir | 60,0 ve 70,0 kesmelerini taşır (zaman atlamalarının köprüsü). 61,3–64,0 ("Bram?" ve konuşmaya varmayan nefes) ek −6 dB; telsiz bandına (300 Hz üstü) girmez |
| 6 | **SUSKU — ıska** | C09 · C10 ilk | 80,0–96,8 | **0** | hiçbir şey. C08/C09 kesmesinde çıkar | ıska en yakın nokta ~83,5 · ip silkinmesi 89,7 · hışırtı yükselir 93,5 · toparlanma soluğu ~93,6 · replik 11 (94,0–96,0) · bitiş tıkı 96,0 · Sela'nın nefesi 96,3 |
| 7 | GERİ DÖNÜŞ | C10 son | 96,8–100,0 | 1 | **L1 geri gelir**, aynı nota, tek | — |
| 8 | EVE | C11 | 100,0–110,0 | 2 | **L3 girer** 100,0 (C10/C11 kesmesi): Mi + Si (sus2, üçlü yok); L1 sürer. Sela'nın ateşlemesine (102,5) vuruş, kabarma YOK | başlangıç tıkı 101,8 · Bram'ın nefesi 102,0 · tıslama ~104,5'e kadar · nefes-gülüş ~105,3 · bitiş tıkı ~106,0: hepsi müziğin önünde; L3 bu sürede −4 dB |
| 9 | ÇÖZÜLME | C12 | 110,0–117,0 | **3** | ≈112,0'da L3'ün Si'si Do♯'ya çıkar → La majör açık akor: filmin TEK çözülmesi. Yoğunluğun tepesi; 117,0'da yay kalkar, KESME | başlangıç tıkı 111,0 · replik 12 (114,0–114,8) −8 dB · ışık yayılması 110–116 |
| 10 | Son nefes | C12 | 117,0–120,0 | 0 | müzik yok | Bram'ın sığ nefesi, açık hat; Sela'nın titrek nefesi oturur (118–120) |

Toplam: müzikli ≈76,6 s (%64) · müziksiz ≈43,4 s (%36).
Kesmelerin müzikle ilişkisi: 10,0 / 20,0 / 30,0 → müzik çalıyor, kesmeye karışmıyor · 40,0 / 50,0 → sessizlik
kesmeyi kapsar (A4c, A5: 1,3 s ve 5,2 s gecikmeler korunur) · 60,0 / 70,0 → L1 köprü · 80,0 → müzik SUSAR ·
90,0 → sessizlik · 100,0 → L3 girer · 110,0 → L3 sürer.

---

## 4. REPLİK–MÜZİK ÇAKIŞMA TABLOSU (mutlak saniye)

| No | Replik | Mutlak | Müzik durumu |
|:--:|---|---|---|
| 1 | Lost my jets. | 3,0–4,1 | müziksiz (L1 4,2'de girer) |
| 2 | No, no— don't burn at me! | 12,5–14,1 | L1, −8 dB; L2 14,6'da girer |
| 3 | Cut it! You're climbing… | 21,0–24,4 | L1+L2, −8 dB |
| 4 | Copy. Down to two. | 26,4–27,8 | L1+L2, −8 dB |
| 5 | Turn your back on me— and brake. | 30,8–33,1 | L1+L2, −8 dB |
| 6 | Negative. I can see you. | 33,7–35,3 | L1+L2, −8 dB; müzik 0,1 s sonra kesilir |
| 7 | At sunrise, I'm right in front of you. | 36,2–39,0 | **müziksiz** |
| 8 | At me— you're home… Your call. | 40,3–46,0 | **müziksiz** ("might" telsiz filtresinde en az "reach" kadar duyulur) |
| 9 | Sunrise. You be there. | 51,2–53,0 | **müziksiz** |
| 10 | Bram? | 61,5–62,1 | L1 (tek nota), ek −6 dB |
| 11 | I heard you. In the dark. | 94,0–96,0 | **müziksiz** |
| 12 | Good call. | 114,0–114,8 | L1+L3 (çözülmüş akor), −8 dB |

12 replikten 5'i müziksiz, 7'si −6…−9 dB altında. Hiçbir replik müziğin vuruş noktasına rastlamıyor.

---

## 5. KURAL KONTROLÜ

| Kural | Durum | Nerede |
|---|:--:|---|
| 1 Okuma cümlesi önce | ✔ | §1 OKUMA |
| 2 En az bir müziksiz an, ideali doruk; 1–2 s önce susar; dönüş tek nota | ✔ | 35,4–54,8 (doruk C05–C06); susma kararın 4,6 s öncesinde; dönüş 54,8 tek nota. İkinci: 80,0–96,8 |
| 3 Fade-out yok; 1–2 gerçek çözülme | ✔ | tek çözülme ≈112,0; bitiş yay kalkarak kesme. 96,8–100 arasındaki sus2 çözülme sayılmaz |
| 4 Vuruşlar olaya; kesmeler `kurgu.py liste`'den | ◐ | olaya oturdu; liste faz 8'de koşulacak. Kesmeler 10 s katı olduğundan sapma beklenmiyor |
| 5 Telefon: alt bas oktav eşi | ✔ | 55 Hz + 110 Hz eşit seviye; infrases yok |
| 6 Vakum: kuru; görüntü kaydırılır; mickey-mousing yok | ✔ | reverb yok. Karakter hareketine vuruş yok: 53,7 ateşlemeden 1,1 s sonra, 102,5 ateşlemede hiç, 21,6 tıslama kesilmesinde hiç |
| 7 Miks: −14 LUFS / −1 dBTP; replik altı −6…−9 dB; mono | ✔ | §2 |
| 8 Melodi alıntısı yok | ✔ | pedal + tek çizgi + iki nota; bir bestecinin dokusuna atıf gerekmedi |

---

## 6. NEDEN BU PLAN — kısa gerekçe

1. **Müzik iki ses arasında taraf tutar, sonra çekilir.** Hikâyenin sorusu "göz mü, ses mi?". İlk 35 s'de L2
   göz çizgisi olarak yükselir ve ışık büyürken inandırıcıdır (müzik de gözün yalanına inanır). Sela "I can
   see you" der demez (35,3) çizgi cümlenin ortasında kesilir ve filmde bir daha gelmez. Göz bir daha müzik
   almaz; geri dönen tek şey L1'dir, yani pedal, yani güven.
2. **Doruk sessizdir, çünkü karar sese aittir.** Takas (40,3–46,0), gözlerin kapanması, dönüş ve "You be
   there" müziksiz kalır. Kural bu seçimin bedelini sessizlikte tartar ("seçim sessizlikte tartılıyor",
   tretman S5). Müzik ateşlemeye tepki vermez; ateşlemenin 1,1 s SONRA gelen tek nota, kararı onaylayan
   değil kabul eden bir nottur.
3. **Tek bir nota, aynı nota.** Aynı La pedalı üç yerde başlar (4,2 · 54,8 · 96,8): söz, söz verilmesi,
   söz tutulduktan sonra duyulması. "Sese güven"in müzikal karşılığı.
4. **İkinci sessizlik anlam taşır.** C09 ıskası ve ip atışı (silkinme 89,7, filmin en riskli temas anı,
   sözsüz) müziksiz kalır: silkinme sesi gövdeden gelir, müzik onu örtmemeli. Müzik Bram'ın hattı geri
   gelip sesi duyulduktan sonra (96,8) döner; "Bram yaşıyor mu?" sorusunun cevabını müzik vermez.
5. **Çözülme tek, sonu kesme.** Çözülme (112,0) "ikisi başladıkları kapakta" bilgisinde; ama film
   çözülmüş bir akorla tatlıya bağlanmaz: yay kalkar (117,0) ve son 3 s'yi Sela'nın titreyen nefesi taşır.
   "Titrek gurur" duygusunun titreği müzikte değil nefestedir.
6. **L3 sus2 (100,0–112,0)** C10'dan sonraki rahatlamayı kısmi tutar: Bram yaşıyor ama eve varılmadı. Si'nin
   Do♯'ya çıkışı (üçlünün gelişi) yalnız istasyon kapağında olur.

---

## 7. F4 DİĞER AJANLARA / FAZ 8'E NOTLAR

1. **Hışırtı, tıslama ve nefes anlamdır; müzik bunlara benzememeli.** Faz 8 promptunda "noise-like texture,
   breathy pad, airy flute, shimmer, bow noise vurgusu" YOK. L1 alt bantta (≤ 300 Hz ağırlıklı), telsiz
   hışırtısı mid bantta; ikisi ayrı bantlarda durmalı. L2 çok yüksek ve ince, 6 kHz altında.
2. **Susmalar kurguda kesilir, üretimde garanti edilmez.** Flow Music'in saniye hassasiyetli boşluğu
   tutacağı belgelenmedi (FLOW_GERCEKLERI §6). Faz 8 stratejisi: kesintisiz bir yatak üretilir ve 35,4 ·
   80,0 · 117,0 kesmeleri kurguda yay-kalkışı gibi (10–30 ms rampa, kuyruk yok) açılır; 54,8 ve 96,8'deki tek
   notalar yatağın yeniden açılması ya da ayrı bir tek-nota üretimi olabilir. Fade-out YASAK kuralı bitiş
   içindir; ara rampa 30 ms'yi geçmez.
3. **Vuruş oynarsa görüntü kayar, müzik değil** (kural 6): klip başında 2–6 karelik pay. C05'in sessizliği
   ve C09'un ip silkinmesi bu kayma payına dokunmaz.
4. **Ses-tasarımcısı:** 35,4–54,8 ve 80,0–96,8 aralıklarında müzik yoktur; bu aralıkların sesi tamamen
   telsiz hışırtısı, kask içi nefes, tıslama ve tık dilidir. Bu aralıklarda "oda tonu köprüsü" yoktur
   (vakum, ses kaynağı gövde). Müziğin kesildiği 35,4'te telsiz hışırtısı da yoksa kulak sıfır alır:
   hışırtı/kask fanı kesilmez (dijital sıfır yok).
5. **Kayıt zamanı uyuşmazlığı (müzik planı etkilenmez):** FILM §4 C05 gözlerin kapanmasını 5,6 s (45,6),
   dönüşü 6,0–7,0 s (46,0–47,0) veriyor; diyalog_3 A5 ise gözleri ~47,0'da, omzu ~48,5'te veriyor. Kurgu
   ve ses §4'ü (daha yeni) esas almalı; 35,4–54,8 sessizliği iki yorumu da kapsıyor.
6. **C07'de Bram'ın konuşmaya varamayan nefesi (63,0)** L1'in üstünde duyulmalı. L1 o aralıkta fark
   edilmeyecek kadar alçak tutulur ya da ses-tasarımı isterse 61,3–64,0 arası L1 tamamen çekilir
   (tek kural: pedal kesilip yeniden girmez, yalnız seviyesi düşer).
7. **Açık karar (Fable):** bitiş akoru. Plan: ≈112,0 çözülme + 117,0 kesme. Yedek: çözülme hiç yapılmaz,
   sus2 sonuna kadar sürer, 117,0'da kesilir (daha titrek; "Good call" ile gurur ses/oyunculukta kalır).
   Plan çözülmeli sürümü seçti çünkü kayıtlı tek ödül anı bu kapak gün doğumu; izleyici testi "fazla
   zafer" derse yedeğe dönülür.

```
ÖZET      MÜZİKSİZ AN 2 (+ açılış 4,2 s ve bitiş 3 s) · TEK ÇÖZÜLME 1 · KESME İLE BİTİŞ
          KATMAN 3 (L1 · L2 · L3), aynı anda en çok 2 · MÜZİKLİ %64
AÇIK      faz 8: gerçek kesme listesi · bitiş akoru (§7 madde 7) · susmaların kurguda mı üretimde mi
          kurulacağı (§7 madde 2)
```
