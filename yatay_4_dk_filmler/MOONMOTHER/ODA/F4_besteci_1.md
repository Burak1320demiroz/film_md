# F4 · besteci · tur 1 (plan) — MOONMOTHER

```
GİRDİ      FILM.md §1 (hikâye) · §2 (tretman) · §4 (çekim listesi, saniye işaretleri, AÇILIŞ) · §5 (REPLİK yok, model sesi KAPALI) · §6/§7 şablonları
           ODA/SAHIP_PLANI.md "Ses ve müzik akışı" + "Müzik briefi" (birebir kaynak) · NOTLAR.md KARARLAR · ODA/DURUM.md
           ODA/F3_kurgucu_1.md (çağrı vuruşları, ses köprüsü önerileri, B9 C24 bitişi)
           uretim_hatti/ILK_30_SANIYE_KILAVUZU.md §4-§5 · GECIS_VE_SES_SUREKLILIGI.md · FLOW_GERCEKLERI.md §6
           GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md: yalnız bölüm başlıkları tarandı (§7-19 gövdesi bu turda okunmadı)
           Biçim örneği: yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F4_besteci_1.md
KESMELER   24 × 10 s → 23 kesme: 10 · 20 · 30 · … · 230 (mutlak film saniyesi). `kurgu.py liste --kesmeler` bu turda koşulmadı;
           faz 8'de gerçek çıktıyla kesinleşir. Aşağıdaki tüm saniyeler MUTLAK: Cn içi saniye + (n−1) × 10.
DURUM      PLAN. Saniyeler yaklaşık (±0,5 s). Çağrı (efekt) zamanları F4 ses-tasarimcisi_1 ile birleştirmede kesinleşir.
```

---

## 1. FILM.md §7'ye YERLEŞTİRİLECEK BLOK

```
OKUMA        İzleyici bu filmi, korkunun merhamete dönüşmesi — dev ölçeğin tehdit olmaktan çıkıp barınak olması — olarak okumalı.
             Kozmik korku, felaket ya da zafer marşı olarak değil. Müzik korkuyu ilan etmez: ilk dakikada yalnız ölçeğe eşlik eder,
             tehlikede denizin saatini tutar (karakterlere bakmadan), iki kritik anda (atlayış, yavrunun çağrısı) susar ve ancak
             anne cevap verdikten sonra tek bir notayla, ilk majör üçlüyle döner.
MÜZİKSİZ     (0) AÇILIŞ 0,0–16,5 s (C01 + C02'nin ilk 6,5 s): kural 0; Oru'nun çağrısı ve gökten gelen alçak nefes müziğin
             değil gözün sesi olsun. Müzik C02'de, Oru'nun ışık dizisi bittikten sonra girer.
             (1) ANA — 126,0–138,0 s (C13 son 4 s · C14 · C15'in ilk 8 s): Khev'in kemere ve yavruya bakışı bittikten sonra,
             atlayıştan ≈1,5 s ÖNCE müzik susar; atlayış, 130,0 sert kesme ve iniş, çatlak, "bacağı değil yavruya bakış" sessizlikte olur.
             Geri dönüş: Khev gözünü bacağından yavruya çevirdikten ≈1,5 s sonra TEK NOTA (D).
             (2) 161,5–178,0 s (C17 son 8,5 s · C18): Oru'nun tam çağrısı ve annenin cevabını bekleme. Müzik çağrıdan 1,5 s önce
             susar; kesme 170,0 sessizlikte; geri dönüş annenin cevabı bittikten sonra TEK NOTA (F diyez, filmin ilk majör üçlüsü).
             (3) Bitiş: müzik 240,0'da KESİLİR (fade-out yok, kuyruk yok).
VURUŞ/SUSMA  ≈16,5 L1 girer (açık beşli D+A) · ≈24,5 L2 seyrek cam armonikleri · ≈45,0 motif M ilk kez (düşük çello, armonisiz) ·
             ≈56,0 M yüksek (Oru boyu) · ≈58,0 M alçak (anne boyu) · ≈62,0 L3: alçak F (minör üçlü, tehlike rengi) ·
             ≈66,0 NABIZ girer (60 BPM, denizin saati) · ≈84,5 armoni koyulaşır · ≈94,0 tonal katmanlar çekilir ·
             ≈96,0 NABIZ durur (levha düşmeden ≈1,5 s önce) · ≈105,5 M kırılır (iki nota, üçüncü gelmez) ·
             ≈126,0 SUSMA 1 · ≈138,0 TEK NOTA D · ≈147,0 beşli geri · ≈156,0 NABIZ geri (dalga saati) · ≈161,0 son vuruş ·
             ≈161,5 SUSMA 2 · ≈178,0 TEK NOTA F♯ · ≈182,0 yaylılar F♯'nin altına yükselir (D add9) ·
             ≈198,5 NABIZ geri, bu kez annenin kalp atışı · ≈199,5 M BÜTÜN ve armonize (D majör renk) ·
             ≈212,5 her şey tek asılı akora incelir (A sus) · ≈214,5 TEK ÇÖZÜLME (A → D majör, bütün topluluk) ·
             ≈226,5 nabız çıkar · ≈233,0 son cümle · 240,0 KESME.
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md (taslak: bu dosya §5 ve FILM.md §7 `### MÜZİK PROMPTU`)
```

---

## 2. KÜNYE (kılavuz §17) — faz 8'in girdisi

```
FİLM                  MOONMOTHER · 4:00 · 24 × 10 s · yatay 16:9 · diyalogsuz · model sesi KAPALI
NOVUM OKUMASI         bkz. OKUMA (yukarıda). Önce bu yazıldı.
MÜZİK-GÖRÜNTÜ İLİŞKİSİ 0–60 s: empatik, ölçeğe (hayranlık, korku değil). 60–126 s: ANEMPATİK nabız: deniz saati Khev'in kararına bakmaz;
                      müzik Khev'in adımlarına vuruş yapmaz. 126–178 s: yokluk (iki kritik an yalnız sesle ve bedenle taşınır).
                      178–240 s: empatik-sıcak (koruyucu armoni), ama dalga ve Khev'in yarası müzikle "silinmez".
TEMPO                 ≈60 BPM, SERBEST. Nabız metronom değil, insan vuruşu; 1 vuruş ≈ 1 s. Izgara yok: giriş ve çıkışlar olaya oturur
                      (kural 4). Kesmeler zaten 10 s katı; nabız kesmeye vurgu yapmaz.
TONALİTE              Merkez D. Açık beşli D+A (üçlü yok) = belirsiz niyet. Minör üçlü (F) yalnız 62–96 ve 158–161,5 (tehlike).
                      Majör üçlü (F♯) 178'e kadar HİÇ yok; ilk kez tek nota olarak gelir. Kadans (A → D) filmde bir kez: 214,5.
MOTİF M               D–E–A: yükselen ikili, sonra beşli sıçrama (üç nota; yapısal ögedir, melodi alıntısı değil).
                      Anne ve yavru aynı motifi iki boyda söyler: yavru boyu ≈600–900 Hz cam tınısı, anne boyu ≈150–220 Hz çello.
                      Yolculuk: bütün (45–58) → kırık, iki nota (105,5) → bütün ve armonize (199,5) → son cümlede yüksek (233–240).
                      Efekt çağrısı (Oru/anne üç nota) FILM'in ses imzasıdır, müzik değildir: ses-tasarimcisi çağrıyı bu perdelere
                      (D–E–A) ya da perdesiz cam/çıtırtı olarak kurar; müzik çağrının üstüne binmez, çağrıdan SONRA söyler.
SESSİZLİK             0–16,5 (açılış) · 126,0–138,0 (ANA, doruk) · 161,5–178,0 (çağrı ve cevap). Toplam 45,0 s (%18,75).
ÇÖZÜLEN CÜMLE         YALNIZ BİR: 214,5 (A sus → D majör). 100–126'daki kırık motif, 105,5'te söylenip tamamlanmaz;
                      tamamlanışı 199,5'tedir. 178–198'deki D add9 asılıdır, çözülme sayılmaz. Son akor (233–240) kadans değil.
KAPANIŞ               fade-out YOK. Son akor açık D add9 (kadans yok), 240,0'da hard-stop. FILM §4 C24: 8–10 s kamera durur,
                      film "kesilmiş" bitmez (kurgucu B9); müzik de kuyruksuz biter.
FREKANS TABANI        Kök D2 (73 Hz) yalnız çok yumuşak; D3 (147 Hz) oktav eşi EŞİT seviyede (90–160 Hz içinde, telefonda duyulur).
                      55 Hz altına inilmez, infrases yok (kural 5). Nabız (frame drum) gövdesi ≈100–130 Hz.
                      Orta bant (300–1500 Hz) temiz: sahip briefi "telefon hoparlöründe duyulan orta frekans dokusu".
KATMANLAR             L1 pedal/yay (alçak yaylılar, sordino; D3+A3, ara sıra D2) · L2 cam (cam armonika/cam armonikleri, yüksek, seyrek)
                      · L3 alçak ses (solo çello/viyola: motif ve F) · P nabız (büyük frame drum, yumuşak tokmak).
                      Aynı anda en çok 3 katman (66–96: L1+L3+P; 214,5–220: L1+L3+L2; P ile L2 aynı anda çok seyrek).
LUFS HEDEFİ           nihai −14 LUFS / −1 dBTP · müzik yatağı −18…−20 LUFS kısa süreli · REPLİK yok; yerine ÇAĞRI pencerelerinde
                      (bkz. §4) müzik −6 dB, çağrı kendi başına okunur · dalga/su darbesi anlarında (97–99, 213–217) müzik SFX'in altında.
REVERB                Dünya atmosferli (deniz, rüzgâr): vakum filmi değil, "kuru" kuralı zorunlu değil. Yine de küçük-orta doğal oda,
                      uzun yıkama yok: çağrılar ve okyanus efekti için boşluk (sahip briefi). Nabız kuru.
MONO                  alt uç ve motif merkezde; mono fold-down'da düşme olmamalı.
```

---

## 3. DİNAMİK TABLO

Yoğunluk 0–5 (0 = müzik yok, 5 = film bu müzikle olabileceği en dolu hâli). Film içinde en yüksek yoğunluk 4'tür (iki kez:
214,5 çözülme ve 238 son cümle); 5'e çıkılmaz çünkü Khev'in yarası kalıcı ve kapanış "tamamlanmış ama kapanmamış".

| # | Bölüm | Çekim | Yaklaşık saniye | Yoğ. | Ne giriyor / çıkıyor | Altında / üstünde ne var |
|:--:|---|:--:|---|:--:|---|---|
| 1 | AÇILIŞ | C01 · C02 ilk | 0,0–16,5 | 0 | hiçbir şey (kural 0) | C01: Oru'nun üç camsı ıslığı, gökten tek alçak nefes (≈2–9, SFX); rüzgâr, deniz. C02: Oru çağrısı 12–16,5 (ışıklar 13–16,5) |
| 2 | GİRİŞ | C02 son · C03 | 16,5–30,0 | 1→2 | **L1 girer** 16,5 (D+A, sordino yay, açık beşli, üçlü yok); **L2** ≈24,5 (tek tük cam armonikleri); 28'e dek L1 +3 dB | Oru'nun çağrısı bitti (girişin sebebi bir SES olayı: ışık dizisinin bitişi). C03 yüzgeç hava sesi, uzak okyanus rezonansı. Başlık yazısı (kurguda, 27–30) görsel; müzikle çakışmaz |
| 3 | SIĞINAK | C04 | 30,0–40,0 | 1 | L2 çıkar ≈33 (doğal sönüm); **L1 yalnız**, açık beşli | Korku müzikte değil Oru'nun ıslığında ve Khev'in bedeninde. Kesme 40,0'da L1 kesmeye karışmaz |
| 4 | CEVAP | C05 | 40,0–50,0 | 1→2 | ≈45,0 **M ilk kez**: tek düşük çello D–E–A, armonisiz (anne ışıklarının üçüncüsünden ≈0,5 s sonra); 47–50 L1 yavaş +2 dB | Anne cevabı üç nota 41–46 (sıcak, büyük tını, SFX). Müzik cevabı taklit etmez, SONRA söyler |
| 5 | AKRABALIK | C06 | 50,0–60,0 | 3 | 52–55: yalnız L1, −6 dB (iki çağrı üst üste). ≈56,0 **M yüksek** (cam, Oru boyu) · ≈58,0 **M alçak** (çello, anne boyu); 58–60 L1 +3 dB, D–E–A kümesi, üçlü yok. Kesmede (60) tutulur | İki çağrı 52–55 (SFX); 55–56 okyanus + rüzgâr boşluğu. Film açılışının ilk yoğunluk 3'ü: ödül hayranlık, korku değil |
| 6 | SIRT | C07 ilk 6 s | 60,0–66,0 | 2 | **L3 girer** ≈62,0: alçak F (minör üçlü); L2 yok | Büyüyen su kükremesi, taş takırtısı (SFX). Annenin ilerleyişine vuruş yok |
| 7 | NABIZ | C07 son – C10 | 66,0–96,0 | 3 | **P girer** 66,0 (mantanın durup sırtın tek başına yürümeye başladığı an; kuru, tok, 60 BPM); vuruş şiddeti 96'ya dek yavaşça +4 dB; ≈84,5 armoni koyulaşır (Dm add9 rengi); ≈94,0 L3 ve L2 çekilir, yalnız L1 + P; **≈96,0 P durur** (son vuruş kuyruksuz) | C08 Oru çağrısı 75–76 (müzik −6 dB). C09 ayak sesleri 80–86, adımlara vuruş yok. C10 taş gıcırtısı kesmeden ≈1 s önce (89) başlar, sırt 90–93,5, levha eğilir 93,5–97, kırılma + su darbesi ≈97–99 (SFX tek başına) |
| 8 | KAPANAN YOL | C10 son – C11 | 96,0–110,0 | 1 | **L1 yalnız**; ≈105,5 L3: M kırık, D–E, üçüncü (A) GELMEZ; E 108'e dek tutulur, sonra yalnız L1 | Levha düşüşü 97–99; C11 Oru'nun cıvıltısı → zayıf inen ıslık 100–107 (SFX); müzik cıvıltının üstüne binmez, düşüşten SONRA söylenir |
| 9 | YALNIZ | C12 · C13 ilk 6 s | 110,0–126,0 | 1 | L1 yalnız, −3 dB, açık beşli | Oru'nun zayıf çağrısı 111–113; sprey; C13: Khev'in kemere ve yavruya bakışı (120–127), yalnız ortam |
| 10 | **SUSKU — doruk (1)** | C13 son · C14 · C15 ilk 8 s | 126,0–138,0 | **0** | **her şey çıkar** 126,0 (yay kalkışı, 10–30 ms rampa, kuyruk yok) | atlayış itişi ≈127,5, beden kadrajdan çıkar ≈128–129,5 · **sert kesme 130,0 sessizlikte**, iniş rezonansı C14'ün 0. saniyesinde · acı tıkırtısı, çatlağa bakış 133–136,5 · gözün yavruya dönüşü 136,5 |
| 11 | TEK NOTA | C15 | 138,0–147,0 | 1 | **L1: tek D** (D2+D3 eşit seviye), başka hiçbir şey | Oru'nun üç ışığı 140–144 (hafif, SFX); beşik, nefes, kitine temas |
| 12 | SAAT | C15 son · C16 | 147,0–161,5 | 2→3 | ≈147,0 A girer (açık beşli); ≈156,0 **P geri** (Khev'in çöküşünden sonra; bu kez dalganın saati); ≈158 L3 alçak F; **≈161,0 P son vuruş** | Köpük bir karış yaklaşır 147–150; duvar tepesine bakış 150–152; doğrulma ve çöküş 152–156; dalga sırtı yaklaşır (artan kükreme, SFX) |
| 13 | **SUSKU — çağrı (2)** | C17 son 8,5 s · C18 | 161,5–178,0 | **0** | **her şey çıkar** 161,5 (çağrıdan ≈1,5 s önce) | Oru'nun tam çağrısı 163–167 (tek ses, SFX) · dinleme boşluğu 167–170, perdesiz alçak "dikkat" uğultusu SFX (168,5–170) · **kesme 170,0 sessizlikte** · anne gözü yukarı → aşağı 173–176,5 · anne cevabı (üç nota + ışıklar) 176,5–179 · artan sörf kükremesi dalga saatini tutar |
| 14 | TEK NOTA 2 | C18 son · C19 | 178,0–190,0 | 1→2 | ≈178,0 **tek F♯** (sıcak, cam+yay karışımı; filmin ilk majör üçlüsü; annenin cevabının bittiği an); ≈182,0 L1 (D+A) F♯'nin altına yavaşça yükselir (≈4 s) → D add9 asılı akor; ≈184 L2 seyrek E | Yüzgeç ucu alçalır 180–184, oturur 184–187 (membran gıcırtısı, altında düz su, SFX); ufukta dalga sırtı 187–190 |
| 15 | KÖPRÜ | C20 ilk 8,5 s | 190,0–198,5 | 2 | D add9 + F♯ tutulur; yeni katman yok | Oru'nun kanat çırpışı ve kısa süzülüşü 193–197: müzikte vuruş YOK. Oru'nun parlak çağrısı + annenin alçak rezonansı ≈196,5–198 (SFX; müzik −6 dB) |
| 16 | NABIZ (ANNE) | C20 son 1,5 s – C22 ilk 2,5 s | 198,5–212,5 | 3 | ≈198,5 **P geri**: artık annenin kalp atışı (yuvarlak, sıcak, daha uzun çınlama, aynı 60 BPM); ≈199,5 **L3: M BÜTÜN ve armonize** (D majör renk, F♯); ≈204,5 armoni IV'e (G add9) kayar (köpük, zaman daralıyor), ≈208 D'ye döner | Khev'in efor tıkı, taştan membrana sürtünme 200–203,5; köpük 203,5–207; yüzgeç damarları atar 207–210; dalga uğultusu 208'de başlar (J köprüsü, SFX) |
| 17 | DALGA | C22 | 212,5–214,5 | 1 | **P çıkar** 212,5; topluluk tek asılı akora incelir (A sus, L1) | Dalga cephesi boş çıkıntıya 213–217: müzik yolu açar, dalga tam şiddetle SFX'e ait |
| 18 | **ÇÖZÜLME** | C22 son | 214,5–220,0 | **4** | ≈214,5 **TEK ÇÖZÜLME**: A sus → D majör, bütün topluluk (L1 + L3 + L2), **P geri** (anne nabzı); 217–220 sürer | Su patlamasının kükremesi yayılır (müzikten ≈3 dB üstte), sprey dağılır 217–220, annenin sabit alçak tonu |
| 19 | YAKINLIK | C23 | 220,0–230,0 | 2→1 | L3 çıkar 220; L2 cam notaları seyrek; **≈226,5 P çıkar** (Khev'in omuzları indiği an); 226,5–230 yalnız L1 D add9 + tek tük cam | Oru'nun tamamlanmış üç notalı cümlesi ≈223–226,5 (SFX; müzik yalnız L1, −6 dB); biyolojik nefes; sis ve yüzgeç damarları |
| 20 | SON CÜMLE | C24 | 230,0–240,0 | 3→4 | 230'dan L1 yavaş +3 dB; ≈233,0 L2 yüksek yaylı + cam armonikleri; annenin SFX motifinin üçüncü notasından sonra (≈237) üst ses F♯ yükselir; **240,0 KESME** (D add9, kadans yok) | İnce rüzgâr, uzak sörf; ufuktaki şafak kenarı 238'de bir kademe parlar: görüntü olayı, müzik vuruşu YOK |

Toplam: müzikli ≈195,0 s (%81) · müziksiz ≈45,0 s (%19: 16,5 + 12,0 + 16,5).

**Kesmelerin müzikle ilişkisi** (23 kesme, hepsi `kesme`; müzik kesmede kesilmez, yalnız planlı iki sessizlik kesmeyi kapsar):

| Kesme | Müzik durumu | | Kesme | Müzik durumu |
|---|---|---|---|---|
| 10 | yok (açılış) | | 130 | **sessizlik (1) kapsar**; iniş SFX 0. s |
| 20 | L1 çalıyor, karışmaz | | 140 | tek D köprüsü |
| 30 | L1 (+L2 seyrek) | | 150 | D+A |
| 40 | L1 yalnız | | 160 | P + L1 + L3 (hâlâ çalıyor; susma 161,5'te, kesmede değil) |
| 50 | L1 + M köprü | | 170 | **sessizlik (2) kapsar**; dikkat uğultusu J (SFX) |
| 60 | tutulan küme, çözülmeden C07'ye | | 180 | tek F♯ + yükselen L1 |
| 70 | P + L1 | | 190 | D add9 asılı |
| 80 | P + L1 | | 200 | P (anne) + L1 + L3, kesmeye karışmaz |
| 90 | P + L1 (tonal çekilme 94'te) | | 210 | P + L1, dalga uğultusu J (SFX) |
| 100 | L1 yalnız (P 96'da durdu) | | 220 | çözülme sürüyor, L3 çıkar |
| 110 | L1 yalnız | | 230 | L1 yavaş yükselir |
| 120 | L1 yalnız | | | |

---

## 4. ÇAĞRI–MÜZİK ÇAKIŞMA TABLOSU (efekt çağrıları; REPLİK yok)

Çağrılar (Oru ve anne, üç nota) filmin ses imzasıdır ve efekt katmanındadır. Zamanlar FILM §4 ve F3 kurgucu tablosundan; ses-tasarimcisi_1 ile birleştirmede kesinleşir.

| Çekim | Çağrı (mutlak) | Müzik durumu |
|:--:|---|---|
| C01 | Oru ıslıkları ≈2–5, gökten nefes ≈5,5–9 | **müziksiz** |
| C02 | Oru çağrısı 12–16,5 | **müziksiz** (L1 16,5'te girer) |
| C05 | anne cevabı 41–46 | L1 yalnız (−6 dB); M 45'te, cevaptan sonra |
| C06 | iki çağrı üst üste 52–55 | L1 yalnız, −6 dB; M 56'dan sonra |
| C08 | Oru küçük çağrı 75–76 | P + L1, −6 dB |
| C11 | cıvıltı → inen ıslık 100–107 | L1 yalnız (P 96'da bitti); M kırık 105,5'te, ıslıktan SONRA |
| C12 | Oru zayıf çağrı 111–113 | L1 yalnız, −3 dB |
| C17 | Oru tam çağrı 163–167 | **müziksiz** |
| C18 | anne cevabı 176,5–179 | **müziksiz** (F♯ 178,0'da, cevap bitince) |
| C20 | Oru parlak çağrı + anne rezonansı ≈196,5–198 | D add9, −6 dB; M 199,5'te |
| C23 | Oru tamamlanmış cümle ≈223–226,5 | yalnız L1, −6 dB |
| C24 | anne motifi tamamlanır ≈233–237 | L1 + L2 altında; müzik üçüncü notadan sonra yükselir |

---

## 5. MÜZİK PROMPTU TASLAĞI (FILM.md §7 `### MÜZİK PROMPTU` altına, F4 taslağı)

Taslak tarihi: 16.10.2026. Saniyeler yaklaşık; faz 8'de `kurgu.py liste --kesmeler` çıktısıyla kesinleşir.

```text
Four-minute instrumental score for a dialogue-free alien science-fantasy short: a tiny wounded creature, a lone alien guardian, and a colossal mother who looks like a moon. Slow, spacious, organic, serious but tender. About 60 BPM, felt not counted, free time. Tonal center D. No cadence until second 214.

Timeline in seconds:
0-16 silence.
16 soft bowed low strings enter on a bare open fifth, D and A, no third.
24 a few sparse single glass harmonics high above.
45 solo cello states a three-note motif: D, E, A (a step up, then a leap). At 56 the same motif answers high in glass tones, at 58 low in cello: one voice in two sizes.
62 a low F darkens the fifth. 66-96 a soft, round, low frame drum pulse at 60 BPM under dark strings; it grows steadily and stops dead at 96.
100-125 the motif breaks off after two notes; strings thin to one bare fifth.
126-138 total silence.
138 one low D returns alone. 147 the fifth joins. 156 the pulse returns and tightens.
161-178 total silence.
178 one single warm F sharp alone, the first major third. From 182 strings rise under it into a hovering D major add9 chord.
198 the pulse returns as a warm heartbeat; the motif returns whole, harmonized and protective.
212-214 everything thins to one suspended chord; at 214 a single full release into D major.
226 the pulse leaves; solo cello and glass tones, intimate.
233 one expansive final phrase, high strings and glass harmonics over an open D add9 chord, no cadence, held until a hard stop at 240.

Palette: bowed low strings, solo cello, glass harmonica, soft low frame drum. Clear midrange detail. Bass root doubled one octave above, nothing below 55 Hz. Keep the 1-4 kHz band open for creature calls and ocean sound. Small dry natural room, no long reverb wash. No fade out.

[Instrumental]
No vocals, no drum kit, no riser, no whoosh, no sub bass.
```

Kısaltma sırası (resmî prompt uzunluk sınırı belgelenmedi; kabul edilmezse): önce palet cümlesinin ikinci yarısı, sonra 100-125 ve 226 satırları, sonra 62/147 ayrıntıları. Dayanak satırlar (susma saniyeleri, motif, çözülme 214, bitiş 240, YOK listesi) kısaltılmaz.

---

## 6. KURAL KONTROLÜ

| Kural | Durum | Nerede |
|---|:--:|---|
| 0 Açılış: C01'de müzik yok, tırmanışla C02/C03'te girer | ✔ | 0–16,5 müziksiz; L1 C02'de 16,5'te, C03'te büyür |
| 1 Okuma cümlesi önce | ✔ | §1 OKUMA |
| 2 En az bir müziksiz an, ideali doruk; 1–2 s önce susar; dönüş tek nota | ✔ | doruk 126,0–138,0 (itişten ≈1,5 s önce, dönüş tek D); ikinci 161,5–178,0 (çağrıdan 1,5 s önce, dönüş tek F♯) |
| 3 Fade-out yok; 1–2 gerçek çözülme | ✔ | tek çözülme 214,5; bitiş 240,0 hard-stop, son akor kadansız. Sahip briefi "resolved final phrase" ister: bkz. §7 açık karar 1 |
| 4 Vuruşlar olaya; kesmeler `kurgu.py liste`'den; faz 4'te tempo yaklaşık | ◐ | ≈60 BPM serbest; girişler olaya (SFX olayı, nabız, nesne olayı) oturur. Liste faz 8'de koşulacak; 10 s katı kesmelerden sapma beklenmiyor |
| 5 Telefon: alt bas oktav eşi, infrases yok | ✔ | D2 (73) + D3 (147 Hz) eşit seviye; 55 Hz altı yok; nabız ≈100–130 Hz |
| 6 Vakum filmi kuru; görüntü kaydırılır; mickey-mousing yok | ✔ | Vakum filmi DEĞİL (atmosfer), reverb kısıtlı tutuldu. Karakter adımına, süzülüşe, atlayışa, yüzgeç oturuşuna vuruş yok; girişler çağrı bitişi / nesne olayı / bakıştan sonra |
| 7 Miks: −14 LUFS / −1 dBTP; replik altı −6…−9 dB; mono | ✔ | §2 (REPLİK yok; çağrı pencerelerinde −6 dB) |
| 8 Melodi alıntısı yok | ✔ | D–E–A motifi özgün; doku betimi (yaylı + cam armonikleri) isim anmadan |

---

## 7. DİĞER AJANLARA / FAZ 8'E NOTLAR · AÇIK KARARLAR

1. **Açık karar 1 (Fable/sahip): bitiş.** Sahip briefi "Finish with a resolved, expansive final phrase" ister; besteci kuralı 3 fade-out yasaklar ve kesme ya da çözülmemiş akorla bitirir. Plan ikisini böyle uzlaştırdı: gerçek çözülme 214,5'te (dalga ödemesinden sonra), son cümle (233–240) geniş ve sıcak ama kadanssız açık D add9 ve 240,0'da hard-stop. Yedek (daha "tamamlanmış"): 238,0'da ikinci çözülme (A → D), sayı 2'ye çıkar (kural sınırı); bitiş yine kesme.
2. **Açık karar 2: ikinci susku uzunluğu** (161,5–178,0 = 16,5 s). Çok uzun bulunursa yedek: L1 çıplak D, 170,0 kesmesinde geri döner (J), F♯ yine 178,0'da gelir; izleyici testi (F7c/F8 ANLATIM) karar verir.
3. **Flow Music süre sınırı.** FLOW_GERCEKLERI §6: "30-second clips to three-minute tracks" (◐, Vids yazısı); 4:00 tek üretimde garanti değil. F8 stratejisi: üç parça, dikişler SUSKULARIN içinde: A 16,5–126,0 · B 138,0–161,5 · C 178,0–240,0. Aynı anahtar (D), aynı tempo, aynı palet sözcükleri. Tek-parça kuralı yazım düzeyinde korunur; dikişler duyulmaz çünkü sessizliğe düşer.
4. **Susmalar kurguda kesilir, üretimde garanti edilmez** (saniye hassasiyetli boşluk belgelenmedi). 126,0 · 161,5 · 240,0'da yay-kalkışı gibi 10–30 ms rampa, kuyruk yok; ara rampa 30 ms'yi geçmez. Fade-out yasağı bitiş içindir.
5. **ses-tasarimcisi_1:** (a) çağrı perdeleri D–E–A ya da perdesiz cam/çıtırtı; (b) 130,0 ve 170,0 kesmelerinde ortam yatağı kopmaz, dijital sıfır yok (müzik yokken oda tonu kulağı taşır); (c) 168,5–170 "dikkat" uğultusu perdesiz olmalı (müzik yok, tonal olursa F♯'nin anlamını yer); (d) dalga saatini 161,5–178'de yalnız artan sörf kükremesi taşır; (e) sahip planının C24 "soft natural tail" ifadesi bu filmde YOK: film 240,0'da biter, süreye eklenti yok.
6. **kurgucu (F8):** kurgucu_1 vuruş tablosu eski zamanlı (C17 2–6,5 · C18 4–7); bu plan FILM §4'ü (daha yeni) esas aldı: C17 ışıkları 163–167, C18 ışıkları 176,5–179. F7c/F8'de gerçek klip ses/ışık zamanları değişirse yalnız 161,5 · 178,0 · 214,5 oynar.
7. **Vuruş oynarsa görüntü kayar, müzik değil** (kural 6'nın ruhu): klip başında/sonunda pay yoksa 214,5 çözülmesi dalga çarpışmasının ≈1 s sonrasına, 178,0 F♯ annenin cevap bitişine bağlı kalır; bu iki bağ görüntü zamanından türer, müzik sabit kalmaz.
8. **Haklar:** Flow Music çıktısı için açık ticari kullanım cümlesi yok (FLOW_GERCEKLERI §6, BİLİNMİYOR); haklar satırı sahibin kontrolünde.

```
ÖZET      MÜZİKSİZ AN 3 (açılış 16,5 s + doruk 12,0 s + çağrı 16,5 s = 45,0 s, %19) · TEK ÇÖZÜLME 1 (214,5) · KESME İLE BİTİŞ (240,0)
          KATMAN 4 (L1 · L2 · L3 · P), aynı anda en çok 3 · MÜZİKLİ %81 · TEMPO ≈60 BPM serbest · MERKEZ D
AÇIK      bitiş akoru (§7 madde 1) · ikinci susku uzunluğu (madde 2) · Flow Music 3 dk sınırı ve 3 parçalı üretim (madde 3)
          faz 8: gerçek kesme listesi · ses-tasarimcisi çağrı zamanları · F7c/F8 ANLATIM sonucu
```
