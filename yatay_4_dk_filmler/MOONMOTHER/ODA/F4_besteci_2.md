# F4 · besteci · tur 2 (plan) — MOONMOTHER

> Tur 1'in (`ODA/F4_besteci_1.md`) yerine geçen tam sürümdür; tur 1 silinmez. Yerleşim: §1 `FILM.md` §7 bloğu, §6 `### MÜZİK PROMPTU` taslağı; §2-§5 ve §7-§8 `ODA/`'da kalır.
> Saat esası: **ses saati** (hakem ilkesi). Bu dosyadaki bütün saniyeler MUTLAK film saniyesidir (= 10 × (Cxx − 1) + çekim içi saniye) ve ses-tasarimcisi_2 §8 / §8b ile birebir aynı sayı doğrusundadır. Ondalık nokta ile yazılır (ses dosyasıyla çapraz okuma için). Saniyeler nominaldir, ±0.3 s; ışık-nota eşleşmeleri F8'de kapanır.

```
GİRDİ      ODA/F4_besteci_1.md (önceki eser) · ODA/F4_ses-tasarimcisi_2.md (§8 müzik kısıtları, §8b çağrı–müzik tablosu 28 R satırı, §8c D sahipliği · bant · nabız · seviye, §3c, §6, §7)
           ODA/F4_kurgucu_1.md (B1-B20) · ODA/F4_hakem_1.md (+ Ek: üç açık karar) · FILM.md §4 güncel (C16 ve C20: sahip kararı 17.10.2026) · ODA/SAHIP_PLANI.md "Ses ve müzik akışı" + "Müzik briefi"
           uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md (§2.4 müzik kesilmez, müziksiz anlar plandadır) · ILK_30_SANIYE_KILAVUZU.md §4-§5 (müzik C01'de yok, tırmanışla C02/C03'te girer; ilk 2 s insan sesi yok)
           GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md bu turda OKUNMADI (görev kapsamı dışı); FLOW_GERCEKLERI.md §6 tur 1'de okundu.
KESMELER   24 × 10 s → 23 kesme: 10 · 20 · … · 230. `kurgu.py liste --kesmeler` bu turda koşulmadı (timeline şablon); faz 8'de gerçek çıktıyla kesinleşir.
DURUM      PLAN, tur 2. Kabul/ret tablosu (§0), FILM.md §7 bloğu (§1), künye (§2), dinamik tablo (§3), çağrı–müzik tablosu 28 satır (§4), kesme tablosu (§5), MÜZİK PROMPTU taslağı (§6).
```

---

## 0. BULGULARA CEVAP (kurgucu B1-B20 · hakem kararı · hakem Ek)

Hakem kararı bağlayıcıdır. 20 bulgunun 19'u KABUL, 1'i KISMEN RED (B11, tek madde). Kabul edilen her satır §1-§6'ya işlendi. Ses tur 2 ile çakışma kalmadı; üç yerde hakem metninin kendi içindeki bir belirsizlik besteci notu olarak açıldı (§0b).

| Bulgu | Hakem kararı (özet) | Cevap | Bu planda (mutlak) |
|:--:|---|:--:|---|
| B1 | 40.0–58.0 müziksiz; M ilk kez 58.0'dan sonra, ≤ −12 dB (cam 58.0, çello 59.2); 60 kesmesine tutulan küme | **KABUL** | L1 **38.5**'te çıkar (kesmeden 1.5 s, R07'nin ilk notasından 2.4 s önce: sessizliğin fark edilmesi için süre). Cam M 58.0/58.6/59.2 (D·E·A), çello M 59.2/60.6/62.0, ikisi ≤ −12 dB. 60.0'da cam D·E·A + çello D çalıyor = küme, çözülmeden C07'ye. L1 beşli geri 60.6. |
| B2 | Nabız iki rolde: 66.0–96.0 ve 202.6'dan; 156.0 / 161.0 kalkar | **KABUL** | P yalnız **66.0–96.0** ve **202.6–226.5**. 212.5–217.6 P ≤ −9 dB; 213.1–213.8 vuruş yok. P fazı x.5 (aşağıda B15). |
| B3 | Tek perde sözleşmesi D–E–A | **KABUL** | M = D–E–A (cam D6·E6·A6, çello D3·E3·A3). Müzikte G yok: tur 1'deki IV (G add9) kayışı kalktı (N3). D add9 (D F♯ A E) E'yi içerir, çağrıyla çarpışmaz. |
| B4 | Prompt bant satırı: 500-4000 Hz açık, cam 1.2 kHz üstü seyrek | **KABUL** | §6 promptunda birebir. §2 künye "orta bant (300–1500 Hz) temiz" → 500–4000 Hz. Not: cam M'nin D6'sı 1175 Hz (sınırın 25 Hz altı); M ≤ −12 dB ve çağrı penceresinde değil, kabul edilebilir sapma. |
| B5 | C12: L1 tek D (A yok), pencerelerde ≤ −30 LUFS-S; R13 besteci tablosuna | **KABUL** | 110.0–121.0'ın tamamı tek D ≤ −30 LUFS-S (yatağın 12 dB altı). A 110.0'da çıkar. R13 §4'te. |
| B6 | Tek D ≈140.0; R17'de −9 dB; A, R18 sonrası | **KABUL** | Tek D **140.2** (R16 izi sönerken; pencere 140.0–140.3). 140.8–144.0 ≤ −9 dB. R18 penceresinde (153.0–156.7) D ≤ −9 dB (kesilmez). A **157.0**. F8 dikişi: 3 → **2 parça** (§6 notu). |
| B7 | Yeni C16 ve C20 | **KABUL** | C16'da P çıpası ve doğrulma satırları yok. C20 sarma (E35) 195.0–198.2: D add9 −6 dB, vuruş yok. C20 ışık saati ölçülünce zincir birlikte kayar (§0b E3). |
| B8 | F♯ 178.0 → ≈179.4; yükseliş ≥ 1.5 s sonra | **KABUL** | Tek F♯ **179.4**, anne N3 (A3) üstünde ≤ −9 dB; N3 bitince (181.5) yatak seviyesine açılır. L1 yükselişi 185.6 (6.2 s sonra). |
| B9 | P 202.6; M BÜTÜN ≈203.5; 198.2–203.0 D add9 ≤ −9 dB | **KABUL** | P **202.6** (R24 N3 sonu 202.7'yi aşarsa N3 sonu + 0.1), M **203.5**. 198.2–203.0 ≤ −9 dB; sarma 195.0–198.2 −6 dB. Hakemin "IV'e kayış bir adım sonraya" maddesi: **IV yerine Bm eğilimi** 206.0, D'ye dönüş 209.0 (N3: IV–I dönüşü plagal kadans gibi okunur, çözülme sayısı sınırı 2). |
| B10 | Tek çözülme 217.6; A sus ≤ −9 dB ya da yok; P ≤ −9 dB | **KABUL** | A sus 212.5–217.6 **≤ −9 dB, kesintisiz** ("yok" değil: çözülmenin "çözüldüğü şey" izleyicinin kulağında kalsın). P ≤ −9 dB, 213.1–213.8 vuruş yok. Çözülme R26'nın (216.6) D'sinin üstüne iner. Bu hakemin "tek çözülme" cümlesi B12 ile ikiye çıkar: 217.6 ve 238.0. |
| B11 | L2 + yüksek yaylı 233.0 → ≈237.2; 238.8–239.8 şafağı L2 cam notası taşır (E27 düşer); üst ses F♯ 237.2 | **KISMEN RED** | **KABUL:** L2 + yüksek yaylı **237.2** (R29 bitişi); şafak parıltısını cam nota taşır (238.4–239.2); E27 ana satırdan düşer (yedek ses tarafında). **RED (tek madde):** üst ses F♯ 237.2 → **238.0**. Gerekçe N1: F♯ majör üçlünün üçüncüsüdür, 237.2'de girerse B12'nin 238.0 çözülmesini 0.8 s öne çeker ve "A → D" bir olay olmaktan çıkar. |
| B12 | İkinci çözülme 238.0 (A → D); son akor 239.85'e dek söner; 239.85–240.0 rampa | **KABUL** | 238.0 A sus → D majör (anne N3 = A3 ortak nota). Son akor 239.85'e dek doğal söner, 239.85–240.0 ≤ 150 ms rampa (tıkırtı önleme), 240.0 KESME. Fade-out yok: bitiş **kesmeyle**. Çözülme sayısı **2** = kural 3 sınırı. |
| B13 | L1 girişi 22.0 | **KABUL** | **22.0** tek A3, çok alçak. C02'nin dinleme boşluğu (17.4–18.8) ve gök basıncı (18.8–20.0) tonsuz kalır. |
| B14 | 25.6–29.4 L1 D'yi bırakır; 180.4–210 L1 D2'yi bırakır; Y2 perdesiz | **KABUL** | 22.0–31.0 L1 yalnız A3 (D3 31.0'da, açık beşli tamamlanır). 185.6–212 L1 = A3 + F♯ + E (kök yok); D'yi E21 taşır. 216.6–221.5 R26 + çözülme kasıtlı birleşme; 221.5'ten sonra D'yi müzik taşır. |
| B15 | P fazı gerçek adımlardan ≥ 0.25 s; koyulaşma ≈88.0 | **KABUL** | Koyulaşma **88.4**. P ilk vuruşu 66.0 (olay: anne durma bırakışı biter), 70.0'a dek tek 1.5 s'lik aralıkla faz **x.5**'e geçer: 70/80/90 kesmeleri ve nominal adımlar 82.0 / 85.0 vuruşa denk gelmez (≥ 0.5 s). F8'de gerçek adım saatleriyle ≥ 0.25 s doğrulanır. |
| B16 | M kırık 105.5 → 107.5; E kesmeye dek | **KABUL** | Çello D3 **107.5**, E3 108.4, A gelmez; E 110.0'da biter. 106.6–109.9 inen ıslık penceresi: M ve L1 ≤ −9 dB, notalar 500 Hz altında. |
| B17 | L1 yükselişi 185.6'dan; 190.0'da D add9; L2 E 187.0 | **KABUL** | Birebir. 185.0–185.6 membran gıcırtısı temiz. |
| B18 | Çağrı tablosu ses R-listesinden, her satıra müzik durumu | **KABUL** | §4: 28 aktif satır (R19 düştü, numaralar kaymadı). |
| B19 | Çağrı altı −9 dB; yatak −18 LUFS-S | **KABUL** | Her yerde −9 dB / −18 LUFS-S. Tek istisna (ses §8): C20 sarma 195.0–198.2'de −6 dB. Yerel zirveler: 217.6 çözülme ≈ −15, 238.0 ≈ −16 LUFS-S (kısa süreli; kükreme zarfı 217.6'da ≈ −17). |
| B20 | Etiket `C13 son 4 s · C14`; susma 126.0 kalır | **KABUL** | Doruk susması **126.0–140.2** = C13 6.0 → C15 0.2. Karar kliği (126.6) sessizlikte. Ses S13 K4 "6.0'da susar". |

**KORU (kurgucu) — hepsi aynen korundu:** 130 ve 170 kesmeleri sessizliğin içinde, yatak sürer · 66.0 nabız girişi · 226.5 nabız çıkışı = Khev'in ilk düzenli nefesi · C01 müziksiz · 168.4–176.2 "dikkat" tonsuz (müzik yok).

### 0a. Hakem Ek — üç açık karar

| Konu | Hakem | Cevap | Bu planda |
|---|---|:--:|---|
| E1 | 97.0–98.6 müziksiz; L1 96.0'da P ile bırakır, 98.6'dan sonra döner | **KABUL** | P ve L1 **96.0**'da birlikte ölür (kuyruksuz). Müziksiz **96.0–98.6** (2.6 s; ses yalnız 97.0–98.6 istemişti, ek 1.0 s hakem metninden: "L1 96.0'da P ile birlikte"). Kırılma 97.2'den 1.2 s önce susmuş olur. Dönüş 98.6'da **tek A3**. (Soru: N2) |
| E2 | 157.0–161.5: besteci seçer, yalnız A ya da müziksiz | **KABUL — yalnız A** | Tek D sürer (153.0–156.7 ≤ −9 dB), **A 157.0**'da girer, açık beşli D+A, 161.5'te kuyruksuz susar. Tur 1'in 158'deki minör F'si **düştü** (F yalnız 62.0–96.0). |
| E3 | C20 ışık parlaması saati: pilot C20 seçilen denemeden ölçülür | **KABUL** | Zincir kuralı: R23 başı Δ kayarsa → R24 Δ → **P = R24 N3 sonu + 0.1** → **M = P + 0.9** → Bm eğilimi = M + 2.5 → D'ye dönüş = eğilim + 3.0. 212.5 incelme ve 217.6 çözülme C22'nin gerçek sprey dağılışından (217.0 + 0.6) türer; 237.2 = R29 bitişi, 238.0 = R28 N3 başı (235.0) + 3.0. |

### 0b. Besteci notları — Fable'a / ses'e / F8'e (yeni; bulgu değil)

| No | Not | Öneri |
|:--:|---|---|
| N1 | Hakem içinde belirsizlik: B11 "üst ses F♯ 237.2" ↔ B12 "238.0 çözülme (A → D)". F♯ = D majörün üçüncüsü. | 237.2'de yüksek yaylı + cam **A ve E** üstünde girer (A sus sürer), F♯ **238.0**'da çözülmeyle gelir, şafak parıltısı 238.4–239.2'de cam F♯. (B11 KISMEN RED'in sebebi.) Fable onayı. |
| N2 | E1 metni "L1 96.0'da P ile birlikte bırakır" ↔ ses isteği "97.0–98.6". | 96.0 seçildi (müziksiz 96.0–98.6). Fable "L1 97.0'a dek sürsün" derse P durduktan sonra 1.0 s tek A3 kalır; kırılma 97.2'ye 0.2 s kalır, "susmanın fark edilmesi" kuralı (1–2 s önce) zayıflar. Öneri 96.0. |
| N3 | Tur 1'deki IV (G add9) → D dönüşü plagal kadans gibi okunur; çözülme sayısı 217.6 + 238.0 ile zaten 2. | IV kalktı: 206.0–209.0 Bm (vi) eğilimi, V yok, "kadans değil". Tek V → I'ler 217.6 ve 238.0. |
| N4 | 185.6–212'de müzikte D kökü yok (B14); D'yi yalnız E21 yüzgeç rezonansı taşır. Kural 5: kök telefonda 90–160 Hz'de oktav eşiyle duyulmalı. | F8 dinlemesi (telefon hoparlörü): 190–212 kök duyuluyor mu. Duyulmuyorsa yedek: L1'e **D3 (147 Hz) −12 dB** (D2 yine yok), ya da E21 +3 dB (ses). |
| N5 | Müziksiz toplam **76.2 s (%31.8)**: 22.0 + 19.5 + 2.6 + 14.2 + 17.9. İkinci susku (17.9 s) doruk susmasından (14.2 s) uzun; "doruk en uzun sessizlik" değil. Kural 2 karşılanıyor (doruk susması var, 1.5–2.0 s önce, tek nota dönüş), ama algı sulanabilir. | F7c/F8 ANLATIM: izleyici hangi susmayı "boşluk/hata", hangisini "doruk" okuyor. Müzik eklemek ses/hakem kararına aykırı; bu not yalnız ölçü sorusudur. |
| N6 | Flow Music saniye hassasiyeti ve 3 dk sınırı belgelenmedi (FLOW_GERCEKLERI §6 ◐). | §6 notu: 2 parça, dikiş 161.5–179.4 susku içinde; iç susmalar kurguda maske (10–30 ms rampa) ile garanti edilir. |
| N7 | 140.2 D girişi kesme 140'ın 0.2 s sonrasında (hakem penceresi 140.0–140.3). | 140.2 seçildi: kesme sessizlikte, giriş R16 izi sönerken. |

---

## 1. FILM.md §7'ye YERLEŞTİRİLECEK BLOK

```
OKUMA        İzleyici bu filmi, korkunun merhamete dönüşmesi — dev ölçeğin tehdit olmaktan çıkıp barınak olması — olarak okumalı.
             Kozmik korku, felaket ya da zafer marşı olarak değil. Müzik korkuyu ilan etmez: ilk 22 saniyede hiç girmez (göz, çağrı ve gök sesle okunur),
             akrabalığı kendisi kanıtlamaz (soğuk → sıcak çağrı farkını sese bırakır), tehlikede denizin saatini tutar (karakterlere bakmadan),
             üç yerde (atlayış, yavrunun çağrısı, levhanın kırılışı) susar ve ancak anne cevap verdikten sonra tek bir notayla, ilk majör üçlüyle (F♯) döner.
MÜZİKSİZ     (0) AÇILIŞ 0.0–22.0 s (C01 · C02 · C03'ün ilk 2 s): kural 0, ILK_30 §5; göz, Oru'nun çağrısı, gökten nefes ve gök basıncı müziğin değil sesin işi.
             (1) AKRABALIK 38.5–58.0 s (C04 son 1.5 s · C05 · C06'nın ilk 8 s): soğuk → sıcak çağrı farkı (anne = Oru'nun akrabası) YALNIZ sesle okunur;
                 müzik kesmeden 1.5 s önce çıkar; geri dönüş cam D ile, ≤ −12 dB (hakem B1).
             (2) KOPUŞ 96.0–98.6 s (C10 6.0–8.6): nabız ve L1 birlikte ölür; levha 97.2'de kırılır, 98.1'de çarpar; müzik vuruşu yok (hakem Ek).
             (3) DORUK 126.0–140.2 s (C13 son 4 s · C14 · C15'in ilk 0.2 s): müzik atlayıştan 2.0 s önce susar; karar kliği, itiş, iniş ve çatlak, bacağa bakış ve
                 yavruya dönüş sessizlikte; geri dönüş TEK NOTA D (140.2), Oru'nun solgun notası sönerken.
             (4) ÇAĞRI 161.5–179.4 s (C17 son 8.5 s · C18): Oru'nun tam çağrısı (163.3), 9.2 s'lik aranma, annenin cevabı; müzik çağrıdan 1.8 s önce susar,
                 170 kesmesi sessizliğin içinde; geri dönüş TEK NOTA F♯ (179.4), annenin cevabının üçüncü notası (A3) üstüne.
             Toplam 76.2 s (%31.8). Bitiş: müzik 240.0'da KESİLİR (fade-out yok); son akor 239.85'e dek doğal söner, 239.85–240.0 ≤ 150 ms rampa.
VURUŞ/SUSMA  22.0 L1 tek A3 · 23.6 L2 tek cam · 31.0 D3 (açık beşli) · 32.0 L2 tek cam · 38.5 L1 ÇIKAR · 58.0 cam M (D·E·A) ≤ −12 dB · 59.2 çello M (D·E·A) ·
             60.6 L1 beşli geri · 62.0 L3 F (Dm rengi) · 66.0 P girer (deniz saati, 60 BPM; faz x.5) · 88.4 armoni koyulaşır · 94.0 L3 çekilir ·
             96.0 P + L1 ÇIKAR (kuyruksuz) · 98.6 tek A3 · 107.5 M kırık (D·E, A gelmez) · 110.0 E biter, tek D ≤ −30 LUFS-S · 121.0 beşli kabarır ·
             126.0 SUSMA · 140.2 TEK NOTA D · 157.0 A (açık beşli) · 161.5 SUSMA · 179.4 TEK NOTA F♯ · 185.6 L1 yükselir (kök yok) · 187.0 L2 E ·
             190.0 asılı D add9 · 195.0–198.2 sarma altında −6 dB · 202.6 P (anne kalp atışı) · 203.5 M BÜTÜN, armonize · 206.0 Bm eğilimi · 209.0 D'ye dönüş ·
             212.5 her şey tek asılı A sus akoruna incelir (≤ −9 dB) · 217.6 ÇÖZÜLME 1 (A sus → D majör, bütün topluluk) · 221.0 L3 çıkar · 226.5 P çıkar ·
             231.0 L1 ≤ −9 dB · 237.2 L2 + yüksek yaylı · 238.0 ÇÖZÜLME 2 (A → D) · 238.4 cam F♯ (şafak) · 239.85 rampa · 240.0 KESME.
FLOW MUSIC   Taslak: aşağıda `### MÜZİK PROMPTU` (17.10.2026, tur 2; tur 1 taslağı 16.10.2026 ODA/F4_besteci_1.md §5'te kalır). Kesin sürüm faz 8: ODA/F8_besteci_<n>.md
```

---

## 2. KÜNYE — faz 8'in girdisi

```
FİLM                   MOONMOTHER · 4:00 · 24 × 10 s · yatay 16:9 · diyalogsuz · model sesi KAPALI
NOVUM OKUMASI          bkz. OKUMA (yukarıda). Önce bu yazıldı.
MÜZİK-GÖRÜNTÜ İLİŞKİSİ 0–22 s: yok (sesle okunan açılış). 22–38.5 s: empatik-eşlik, ölçeğe (hayranlık). 38.5–58 s: yok (akrabalığı ses kanıtlar).
                       58–126 s: ANEMPATİK nabız: deniz saati Khev'in kararına bakmaz; adımlara, süzülüşe vuruş yok. 126–179.4 s: yokluk (üç kritik an
                       sesle ve bedenle taşınır). 179.4–240 s: empatik-sıcak (koruyucu armoni), ama dalga ve Khev'in yarası müzikle "silinmez".
TEMPO                  ≈60 BPM, SERBEST. Nabız metronom değil, insan vuruşu; 1 vuruş ≈ 1 s. Izgara yok: girişler ve çıkışlar olaya oturur (kural 4).
                       Deniz saati fazı x.5 (kesmeler ve nominal adımlar vuruşa denk gelmez); anne kalp atışı 202.6'ya sabitli. Kesmeler 10 s katı; nabız kesmeye vurgu yapmaz.
TONALİTE               Merkez D. Açık beşli D+A (üçlü yok) = belirsiz niyet. Minör üçlü (F) yalnız 62.0–96.0 (tehlike). Majör üçlü (F♯) 179.4'e kadar HİÇ yok;
                       ilk kez tek nota olarak gelir. Bm eğilimi (206.0–209.0) kadans değildir. Kadans (V → I) filmde İKİ kez: 217.6 ve 238.0 (kural 3 sınırı).
MOTİF M                D–E–A: yükselen ikili, sonra beşli sıçrama (yapısal öge, melodi alıntısı değil). Yavru boyu: cam D6·E6·A6 (≈1175–1760 Hz, bir oktav üstte).
                       Anne boyu: çello D3·E3·A3 (147–220 Hz, daha yavaş: büyük şey = yavaş atak). Yolculuk: ikili cam + çello (58.0/59.2, ≤ −12 dB) → kırık, iki nota
                       (107.5) → bütün ve armonize (203.5) → son cümlede yüksek, E→A sıçraması genişler (237.2–239.85).
                       Efekt çağrıları (Oru/anne üç nota) ses imzasıdır, müzik değil: müzik çağrının üstüne binmez, çağrıdan SONRA söyler.
SESSİZLİK              0.0–22.0 · 38.5–58.0 · 96.0–98.6 · 126.0–140.2 · 161.5–179.4. Toplam 76.2 s (%31.8); müzikli 163.8 s (%68.3).
ÇÖZÜLEN CÜMLE          İKİ: 217.6 (A sus → D majör, bütün topluluk, dalga ödemesi) ve 238.0 (A → D, son cümle). 107.5'teki kırık motif tamamlanmaz (tamamlanışı 203.5'te).
                       190–212 asılı D add9 çözülme sayılmaz. Bm eğilimi V'siz.
KAPANIŞ                fade-out YOK. Son akor sıcak D (add9), 239.85'e dek doğal söner, 239.85–240.0 ≤ 150 ms rampa (tıkırtı önleme, ses:371), 240.0 hard-stop.
                       FILM §4 C24: 8–10 s kamera durur; film "kesilmiş" bitmez; müzik de kuyruksuz biter. "240'a taşan kuyruk yok" (hakem B12).
FREKANS TABANI         Kök D2 (73 Hz) yalnız çok yumuşak; D3 (147 Hz) oktav eşi EŞİT seviyede (90–160 Hz, telefonda duyulur). 55 Hz altına inilmez, infrases yok.
                       D kökü yok (22.0–31.0 ve 185.6–212): A3 (220 Hz) ve üst yapı taşır. P gövdesi ≈100–130 Hz. 500–4000 Hz bandı çağrı pencerelerinde çekilir (≤ −9 dB);
                       cam yalnız seyrek ve ≥ 1.2 kHz.
KATMANLAR              L1 pedal/yay (alçak yaylılar, sordino) · L2 cam (cam armonika; 237.2'den yüksek yaylılar) · L3 alçak ses (solo çello: M; viyola: F) · P büyük frame drum,
                       yumuşak tokmak. Aynı anda en çok 3 SÜREKLİ katman (66–96: L1+L3+P; 217.6–221: L1+L3+P, L2 yalnız tek tük cam); L2 sürekli sayılmaz.
LUFS HEDEFİ            nihai −14 LUFS / −1 dBTP · müzik yatağı −18 LUFS-S · çağrı pencerelerinde −9 dB (C20 sarma −6 dB) · C12 tek D ≤ −30 LUFS-S ·
                       dalga/su darbesi anlarında müzik SFX'in altında. Müziksiz oran %31.8: ölçüm −15'in altında çıkarsa müzik yatağı +1…2 dB (ses §9), sıkıştırma yok.
REVERB                 Dünya atmosferli: vakum filmi değil, "kuru" kuralı zorunlu değil. Yine de küçük kuru doğal oda, uzun yıkama yok. Nabız kuru.
MONO                   alt uç ve motif merkezde; mono fold-down'da düşme olmamalı.
```

---

## 3. DİNAMİK TABLO

Yoğunluk 0–5 (0 = müzik yok, 5 = film bu müzikle olabileceği en dolu hâli). Film içinde en yüksek yoğunluk 4'tür ve iki kez (217.6 ve 238.0, iki çözülme); 5'e çıkılmaz çünkü Khev'in yarası kalıcıdır. Ses saatleri ses-tasarimcisi_2 §8b'dendir.

| # | Bölüm | Çekim | Mutlak saniye | Yoğ. | Ne giriyor / çıkıyor | Altında / üstünde ne var (ses) |
|:--:|---|---|---|:--:|---|---|
| 1 | AÇILIŞ | C01 · C02 · C03 ilk 2 s | 0.0–22.0 | 0 | hiçbir şey (kural 0, ILK_30 §5) | Y1 0.0'dan; göz kapağı gıcırtısı 0.0–8.4; R01 4.6–7.2; R02 7.4–11.2; R03 13.2–17.4; dinleme boşluğu 17.4–18.8; tonsuz gök basıncı 18.8–20.0 |
| 2 | GİRİŞ | C03 2.0 – C04 8.5 | 22.0–38.5 | 1 | **L1 tek A3** 22.0 (≈3 s'de yükselir, sordino yay) · L2 tek cam ≈23.6 · **D3** 31.0 (açık beşli) · L2 tek cam ≈32.0 (≈33.5'te söner) · **L1 çıkar 38.5** (yay bırakışı ≤ 0.4 s, kuyruk yok) | R04 25.6–29.4 (L1 yalnız A3, ≤ −9 dB, D yok) · başlık yazısı 27–30 (kurgu, müzikle çakışmaz) · R06 36.5–37.2 (≤ −9 dB) · R05 tonsuz uğultu 38.5'ten şişer |
| 3 | AKRABALIK | C04 son 1.5 s · C05 · C06 ilk 8 s | 38.5–58.0 | **0** | hiçbir şey (hakem B1) | R07 40.9–49.6 (soğuk, boş salon) · R08 52.0–56.4 (sıcak, iki ses tek ses) · 56.8–58.0 rüzgâr-deniz boşluğu |
| 4 | M İLK | C06 son 2 s · C07 ilk 6 s | 58.0–66.0 | 1→2 | **cam D·E·A** 58.0 / 58.6 / 59.2 (≤ −12 dB) · **çello D·E·A** 59.2 / 60.6 / 62.0 (≤ −12 dB, 60 sonrası serbest) · 60.6 L1 beşli geri · **62.0 L3 F** (Dm rengi) | 60 kesmesinde küme tutulur · C07 sırt kükremesi, taş takırtısı; anne durma bırakışı 64.2–66.0'da vuruş yok |
| 5 | NABIZ (deniz saati) | C07 son 4 s – C10 ilk 6 s | 66.0–96.0 | 3 | **P girer 66.0** (kuru, tok, 60 BPM, faz x.5; şiddet 96.0'a dek +4 dB) · **88.4 armoni koyulaşır** (Dm add9 rengi) · 94.0 L3 çekilir (L1 + P) · **96.0 P + L1 ÇIKAR** (kuyruksuz) | R09 75.2–77.0 (P + L1 −9 dB) · adımlar 82.0 / 85.0 (P ≥ 0.25 s uzakta) · R10 86.6–88.2 (−9 dB) · taş gıcırtısı 89–97 |
| 6 | KOPUŞ | C10 6.0–8.6 | 96.0–98.6 | **0** | hiçbir şey (hakem Ek E1) | kırılma 97.2, düşüş 97.3–98.1, ağır su çarpması 98.1; SFX tek başına |
| 7 | KAPANAN YOL | C10 8.6 – C11 | 98.6–110.0 | 1 | **tek A3** 98.6 → ≈101 beşli (hepsi ≤ −9 dB) · **107.5 M kırık** (çello D3, 108.4 E3; A GELMEZ) · 110.0 E biter | R11 101.0–103.3 + inen ıslık 106.6–109.9 (L1 ve M ≤ −9 dB, M < 500 Hz); su çarpması/sprey kuyruğu |
| 8 | YALNIZ | C12 · C13 ilk 1 s | 110.0–121.0 | 1 (eşik) | **tek D** ≤ −30 LUFS-S (A yok) | R12 111.4–112.4 · izler 114.0–115.7 · R13 119.15–121.0; filmin en sessiz noktası |
| 9 | KALKIŞ | C13 1.0–6.0 | 121.0–126.0 | 1→2 | D3+A3 beşlisi −30'dan −18 LUFS-S'e ≈3 s'de kabarır (karar öncesi tereddüt) | Khev kemere ve yavruya bakar; Y1 ve sörf |
| 10 | **SUSKU — doruk** | C13 son 4 s · C14 · C15'in ilk 0.2 s | 126.0–140.2 | **0** | **126.0 her şey çıkar** (10–30 ms, kuyruk yok) | karar kliği 126.6 · itiş 128.0 · düşüş rüzgârı 128.1–129.7 · **sert kesme + iniş 130.0** · R15 acı klik-trili 131.3–132.2 · R16 Oru'nun solgun iki notası 137.2 / 138.6 (iz 139.4→140.2) |
| 11 | TEK NOTA | C15 · C16 ilk 7 s | 140.2–157.0 | 1 | **tek D** 140.2 (D2 + D3 eşit) · 140.8–144.0 ≤ −9 dB · 144.0–153.0 yavaşça +3 dB'e nefes alır · 153.0–156.7 ≤ −9 dB (kesilmez) | R17 140.8–143.8 · köpük yalaması · sörf yükselir · R18 anne tarama süpürmesi 153.3–155.7 + 1 s cevapsız boşluk |
| 12 | SAAT | C16 son 3 s – C17 ilk 1.5 s | 157.0–161.5 | 2 | **A 157.0** (D+A açık beşli) · **161.5 ÇIKAR** (kuyruksuz) | Khev ikinci kez ufuktaki anneye bakar; dalga sırtı yaklaşır; nabız YOK |
| 13 | **SUSKU — çağrı** | C17 1.5 – C18 9.4 | 161.5–179.4 | **0** | **161.5 her şey çıkar** (çağrıdan 1.8 s önce) | R20 Oru tam çağrı 163.3 / 164.6 / 165.9 (N3→167.6) · dinleme boşluğu · R21 dikkat 168.4→176.2 (tonsuz) · **kesme 170 sessizlikte** · R22 anne cevabı 176.8 / 178.0 / 179.2 |
| 14 | TEK NOTA 2 | C18 9.4 – C19 | 179.4–190.0 | 1→2 | **tek F♯ 179.4** (arşe viyola F♯3 + F♯4, cam F♯ ince tını; N3 üstünde ≤ −9 dB, 181.5'ten yatak seviyesine) · **185.6 L1 yükselir** (A3 + F♯ + E, kök yok) · 187.0 L2 E · **190.0 D add9 varış** | R22 N3 → 181.5 · yüzgeç ucu alçalır · 185.0–185.6 membran gıcırtısı (temiz) · E21 yüzgeç rezonansı D kökünü taşır |
| 15 | KÖPRÜ | C20 ilk 8.2 s | 190.0–198.2 | 2 | D add9 tutulur, yeni katman yok; 195.0–198.2 −6 dB | Oru kanat çırpışı 193–197 (müzikte vuruş YOK) · yüzgeç sarması E35 195.0–198.2 |
| 16 | ANNE NABZI | C20 8.2 – C22 2.5 | 198.2–212.5 | 2→3 | 198.2–203.0 D add9 ≤ −9 dB · **202.6 P** (anne kalp atışı: yuvarlak, sıcak, uzun çınlama) · **203.5 M BÜTÜN** (çello D3 203.5 / E3 204.4 / A3 205.3; yaylı armonizasyonu D majör renk) · 206.0 Bm eğilimi · 209.0 D'ye dönüş | R23 198.2–200.6 · R24 200.1–202.7 · R25 · Khev yüzgece oturur 202.6, rahatlama nefesi 203.8 · köpük · dalga baskısı J 208.0'dan |
| 17 | DALGA | C22 2.5–7.6 | 212.5–217.6 | 1 | **her şey tek asılı A sus akoruna incelir** (L3, L2 çıkar); A sus ve P ≤ −9 dB; 213.1–213.8 P vuruşu yok | dalga 213.4 (SFX zirvesi 213.1–214.5) · yayılan kükreme · sprey dağılışı 217.0 · R26 anne tonu D 216.6'dan |
| 18 | **ÇÖZÜLME 1** | C22 7.6 – C23 1.5 | 217.6–221.5 | **4** | **217.6 A sus → D majör**, bütün topluluk (L1 + L3 + P; L2 iki tek tük cam) R26'nın D'sinin üstüne; P 3 vuruşta normal seviyeye · 221.0 L3 çıkar | kükreme zarfı 217.0'da −14, 217.6'da ≈ −17 (çözülme ≈ −15 LUFS-S, maskelenmez) · R26 −14→−18 söner → 221.5 · sprey kuyruğu 221.5 |
| 19 | YAKINLIK | C23 1.5 – C24 1.0 | 221.5–231.0 | 2→1 | 221.5 L1'de D2 geri (D'yi artık müzik taşır) · L2 tek cam ≈227.4 ve ≈228.8 · **226.5 P çıkar** (son vuruş, kuyruksuz) | R27 223.2–226.2 (L1 ≤ −9 dB) · Khev'in ilk düzenli nefesi 226.5 · yüzgeç damarları, sis |
| 20 | **SON CÜMLE / ÇÖZÜLME 2** | C24 1.0–10.0 | 231.0–240.0 | 1→3→**4** | 231.0 L1 ≤ −9 dB (D add9 → A sus, yavaş) · **237.2 L2 + yüksek yaylı** (≥ 1.2 kHz, A/E) · **238.0 A → D majör** (üst ses F♯) · 238.4–239.2 cam F♯ · 239.85 rampa · **240.0 KESME** | R28 anne motifi 231.0 / 233.0 / 235.0 (N3→239.0) · R29 Oru A5 236.0–237.2 · şafak kademesi 238.8–239.8 (müzik taşır, SFX yok) |

Toplam: müziksiz **76.2 s** (22.0 + 19.5 + 2.6 + 14.2 + 17.9) · müzikli **163.8 s**. P çalan süre 53.9 s (30.0 + 23.9).

---

## 4. ÇAĞRI–MÜZİK TABLOSU (ses §8b, 28 aktif satır; R19 düştü)

Çağrı saatleri ve pencereler ses-tasarimcisi_2 §8b'den aynen; "Müzik durumu" bu planın kararıdır. Saat çatışmasında ses saati esastır; müzik yalnız tepkisini kaydırır. Pencerede müzik ≤ −9 dB ya da yoktur.

| R | Çağrı (mutlak) | Pencere | Müzik durumu |
|:--:|---|---|---|
| R01 | 4.6 / 5.5 / 6.4 (N3 → 7.2) | 0–22 | **müziksiz** |
| R02 | 7.4–11.2 (zirve 8.8–9.2) | 0–22 | **müziksiz** |
| R03 | 13.2 / 14.6 / 16.0 (N3 → 17.4) | 0–22 | **müziksiz**; L1 girişi 22.0 (N3 sonundan 4.6 s, gök basıncından 2.0 s sonra) |
| R04 | 25.6–29.4 | 25.6–29.4 | L1 **yalnız A3**, ≤ −9 dB; D yok; ≈23.6 cam tonu pencereye taşmaz; D3 31.0'da |
| R05 | 30.0–40.0 (38.5'ten −18'e), tonsuz | — | L1 (A3, 31.0'dan + D3) çok yumuşak; **38.5'te çıkar**; uğultunun şişmesi müziksiz |
| R06 | 36.5–37.2 | 36.5–37.2 | L1 ≤ −9 dB |
| R07 | 40.9 / 42.5 / 44.1 · küme 45.0–47.0 · sub 47.2–49.6 | 40.0–58.0 | **müziksiz** |
| R08 | 52.0 / 52.9 / 53.8 · anne +0.05 (N3 → 56.4) | 40.0–58.0 | **müziksiz**; 56.8–58.0 boşluk temiz; cam D 58.0 (N3 sonundan 1.6 s) |
| R09 | 75.2–77.0 | 75.0–77.4 | P + L1 (+ L3) ≤ −9 dB |
| R10 | 86.6–88.2 | 86.5–88.4 | P + L1 ≤ −9 dB; P fazı adımlardan (82.0, 85.0) ≥ 0.25 s; koyulaşma 88.4'ten |
| R11 | 101.0 / 102.0 / 103.3 (çöker → 106.6) · inen ıslık 106.6–109.9 | 100.8–110.0 | L1 yalnız ≤ −9 dB (98.6'dan); **M kırık 107.5** (çello D3–E3, < 500 Hz, ≤ −9 dB), E 110.0'da biter; A gelmez |
| R12 | 111.4–112.4 · izler 114.0 / 114.6 / 115.7 | 111.0–113.0 · 113.8–116.2 | **tek D ≤ −30 LUFS-S** (110.0–121.0'ın tamamı) |
| R13 | 119.15–119.95 (L → 121.0) | 119.0–121.0 | tek D ≤ −30 LUFS-S; 121.0'dan sonra D+A kabarır |
| R14 | 126.6–127.0 | 126.0–140.0 | **müziksiz** (126.0'da susar; klik sessizlikte duyulur) |
| R15 | 131.3–132.2 | 126.0–140.0 | **müziksiz** |
| R16 | 137.2–138.0 · 138.6–139.4 · iz 139.4 (→ 140.2) | 126.0–140.0 | **müziksiz**; tek D 140.2'de iz sönerken girer |
| R17 | 140.8 / 141.9 / 143.0 (N3 → 143.8) | 140.8–144.0 | tek D ≤ −9 dB |
| R18 | 153.3–155.7 (+ cevapsız 1 s → 156.7) | 153.0–156.7 | tek D ≤ −9 dB (kesilmez); **A 157.0**'da (≥ 157.0) |
| R19 | — | — | **DÜŞTÜ** (numara korundu) |
| R20 | 163.3 / 164.6 / 165.9 (N3 → 167.6) | 161.5–179.4 | **müziksiz** (161.5'te susmuş; çağrıdan 1.8 s önce) |
| R21 | 168.4–176.2 (dikkat, tonsuz, D'ye kilit 176.2) | 161.5–179.4 | **müziksiz** (168.4–170 "dikkat" perdesiz, müzik tonal olsa anlamı yer) |
| R22 | 176.8 / 178.0 / 179.2 (N3 → 181.5) | 176.5–181.5 | müziksiz 179.4'e dek; **F♯ 179.4** N3 (A3) üstünde ≤ −9 dB (duyulmazsa −6, F8; yine duyulmazsa 181.5); 181.5'ten sonra yatak seviyesi |
| R23 | 198.2 / 198.9 / 199.6 (N3 → 200.6) | 198.2–203.0 | D add9 ≤ −9 dB (sarma 195.0–198.2'de −6 dB) |
| R24 | 200.1 / 201.0 / 201.9 (N3 → 202.7) | 198.2–203.0 | D add9 ≤ −9 dB; **P 202.6** (N3 sonu + 0.1'den önce değil); M BÜTÜN 203.5 |
| R25 | 200.35–200.65 | 198.2–203.0 | D add9 ≤ −9 dB |
| R26 | 216.6–220.0 (söner → 221.5) | 212.8–217.6 | A sus ≤ −9 dB; **çözülme 217.6** R26'nın D'si üstüne (kasıtlı birleşme); R26 217.6'da −14 → −18; L3 221.0'da çıkar |
| R27 | 223.2 / 224.2 / 225.2 (→ 226.2) | 223.0–226.4 | L1 ≤ −9 dB; P 226.5'te çıkar (R27 bittikten 0.3 s sonra) |
| R28 | 231.0 / 233.0 / 235.0 (N3 → 239.0) | 231.0–239.0 | L1 ≤ −9 dB; L2 yok 237.2'ye dek; **238.0 ikinci çözülme** (A3 ortak nota, çarpışma yok) |
| R29 | 236.0–237.2 | 236.0–237.2 | müzik yok (L1 ≤ −9 dB); **237.2'de L2 + yüksek yaylı** girer |

**SFX pencereleri** (müzik vuruşu yok, ses §8): levha kırılma/çarpma 97.0–99.0 → müziksiz 96.0–98.6 · iniş + çatlak 130.0–131.4 → müziksiz · dalga 213.1–214.5 → A sus ≤ −9 dB, P vuruşu yok 213.1–213.8 · membran gıcırtısı 185.0–185.6 → L1 yükselişi 185.6'dan · sarma E35 195.0–198.2 → D add9 −6 dB, vuruş yok.

---

## 5. KESMELER (23) — müzik durumu

Müzik hiçbir kesmede kesilmez (GECIS §2.4). Sessizliğe giriş/çıkış kesmeden ≥ 1.5 s uzak (38.5, 96.0, 126.0, 161.5). Kesme 10, 20, 40, 50, 130, 170 sessizliğin içinde ve bu planlıdır. Kaynak: `kurgu.py liste --kesmeler` (faz 8'de koşulacak); burada 10 s katı.

| Kesme | Müzik durumu | Kesmeye en yakın müzik olayı |
|:--:|---|---|
| 10 | müziksiz (açılış) | — |
| 20 | müziksiz | L1 girişi +2.0 (22.0) |
| 30 | L1 (A3; D3 henüz yok) | D3 +1.0 (31.0) |
| 40 | müziksiz (akrabalık) | L1 çıkışı −1.5 (38.5) |
| 50 | müziksiz (gövdenin açığa çıkışı sessizlikte) | — |
| 60 | **tutulan küme**: cam D·E·A + çello D; çözülmeden C07'ye | cam A −0.8 (59.2), çello E +0.6, L1 +0.6 (60.6) |
| 70 | P + L1 + L3 (P faz x.5: vuruş kesmeye ≥ 0.5 s uzak) | — |
| 80 | P + L1 + L3 | — |
| 90 | P + L1 + L3 | L3 çıkışı +4.0 (94.0) |
| 100 | L1 yalnız, ≤ −9 dB (98.6'da döndü) | A −1.4 |
| 110 | M'nin E'si **biter**; tek D ≤ −30 LUFS-S'e geçer | **0.0** (hakem B16 "E kesmeye dek") |
| 120 | tek D ≤ −30 LUFS-S | kabarma +1.0 (121.0) |
| 130 | müziksiz (doruk susması kapsar); iniş SFX 0.0 | −4.0 (126.0) |
| 140 | müziksiz → tek D | D girişi +0.2 (140.2) |
| 150 | tek D (nefes alıyor) | — |
| 160 | D+A açık beşli | A −3.0 (157.0), susma +1.5 (161.5) |
| 170 | müziksiz (çağrı susması kapsar); dikkat tonsuz | — |
| 180 | F♯ (179.4'te girdi, N3 üstünde ≤ −9 dB) | **−0.6** (ses saati: R22 N3 179.2) |
| 190 | L1 yükselişi **varır**: asılı D add9 (kök yok) | **0.0** (hakem B17) |
| 200 | D add9 ≤ −9 dB (R23 penceresi) | P +2.6 (202.6) |
| 210 | P + L1 + L3 (D'ye dönüş 209.0) | −1.0 |
| 220 | çözülme sürüyor; P normale döndü | L3 çıkışı +1.0 (221.0) |
| 230 | L1 D add9 + tek tük cam | L2 cam −1.2 (228.8), L1 ≤ −9 dB +1.0 (231.0) |

Kesmenin ±1 s'sinde müzik olayı olanlar: 60 · 110 · 140 · 180 · 190 (+ sınırda 210 · 220 · 230). Hepsi hakem ya da ses saatine bağlı (B1, B16, B6, B8, B17); keyfî olan yok.

---

## 6. MÜZİK PROMPTU TASLAĞI (FILM.md §7 `### MÜZİK PROMPTU` altına, F4 taslağı)

Taslak tarihi: 17.10.2026 (tur 2). Tur 1 taslağı (16.10.2026) `F4_besteci_1.md` §5'te kalır, silinmez. Saniyeler nominal; faz 8'de `kurgu.py liste --kesmeler` ve seçilen denemelerin gerçek ışık/adım saatleriyle kesinleşir.

```text
Four-minute instrumental score for a dialogue-free alien science-fantasy short: a tiny wounded creature, a lone alien guardian and a colossal mother who looks like a moon. Slow, spacious, organic, serious but tender. About 60 BPM, felt not counted, free time. Tonal center D. Very sparse: the long silences are part of the music. No cadence before second 217.

Timeline in seconds:
0-22 silence.
22 one very low soft bowed note, A, alone. 31 D joins it: a bare open fifth, D and A, no third. A few single high glass harmonics at 23 and 32.
38-58 silence.
58 a tiny three-note motif in glass tones, D E A (a step up, then a leap), very quiet. At 59 the same motif answers in a low solo cello, slower: one voice in two sizes. At 60 soft strings return on the fifth. At 62 a low F darkens it.
66-96 a soft, round, dry low frame drum at 60 BPM under dark strings, loose and human, growing steadily. At 88 the harmony darkens. At 96 drum and strings stop dead together.
96-98 silence. 98 one low A returns alone, then the bare fifth, very quiet. At 107 the cello motif breaks off after two notes, D and E; the third never comes.
110-121 an almost inaudible single low D. 121-126 a bare fifth swells slowly, then stops dead at 126.
126-140 total silence.
140 one low D returns alone and holds, breathing. 157 A joins. 161 stops dead.
161-179 total silence.
179 one single warm F sharp alone, bowed, with a faint glass overtone: the first major third in the piece. From 185 strings rise under it into a hovering chord of A, F sharp and E, without a root note.
202 a warm round heartbeat on frame drum, 60 BPM. 203 the motif returns whole in solo cello, harmonized by strings, protective, D major color. 206-209 a brief lean to B minor, then home.
212 everything thins to one very quiet suspended A chord. 217 one full release into D major by the whole ensemble: the first cadence.
221 the cello leaves. 226 the heartbeat stops. Intimate strings with sparse glass tones.
231 a quiet held chord. 237 high strings and glass rise into one expansive final phrase. 238 the second cadence, A to D major, warm and open. The chord rings until 239.85, then a hard stop at 240. No fade out, no tail.

Palette: bowed low strings with mutes, solo cello, glass harmonica, soft low frame drum. Bass root D doubled one octave above at equal level, nothing below 55 Hz. Keep the 500-4000 Hz band open for creature calls and ocean sound; glass tones stay sparse and above 1.2 kHz. Small dry natural room, no long reverb wash.

[Instrumental]
No vocals, no drum kit, no riser, no whoosh, no sub bass.
```

**Kısaltma sırası** (resmî prompt uzunluk sınırı belgelenmedi; kabul edilmezse): önce 23/32 cam notaları ve "Intimate strings…" cümlesi, sonra 206-209 eğilimi, sonra 110-121 ve 121-126 satırlarının birleştirilmesi ("110-126 a nearly inaudible low D swelling into a bare fifth, stops dead at 126"), sonra 98 satırı. **Kısaltılmaz:** susma saniyeleri (0-22, 38-58, 96-98, 126-140, 161-179), motif, iki kadans (217, 238), bitiş (239.85 / 240), bant satırı, YOK listesi.

**F8 üretim stratejisi (öneri, tur 1'in 3 parçasından 2'ye indi):** Parça A = 22.0–161.5 (139.5 s) · Parça B = 179.4–240.0 (60.6 s). Dikiş 161.5–179.4 susku içinde (17.9 s, yatak ve sesler taşır; duyulmaz). İki parça da 3 dk altında (FLOW_GERCEKLERI §6 ◐ "30 s – 3 dk"). A'nın iç susmaları (38.5–58.0, 96.0–98.6, 126.0–140.2) promptta yazılıdır ama Flow'un saniye hassasiyeti belgelenmedi: kurguda maske (10–30 ms rampa) esastır, prompt niyettir. Tek-parça kuralı yazım düzeyinde korunur: tek skor, aynı anahtar, aynı tempo, aynı palet sözcükleri. Haklar: Flow Music çıktısı için açık ticari kullanım cümlesi yok (FLOW_GERCEKLERI §6, BİLİNMİYOR), sahipte.

---

## 7. KURAL KONTROLÜ

| Kural | Durum | Nerede |
|---|:--:|---|
| 0 Açılış: C01'de müzik yok, tırmanışla C02/C03'te girer · ILK_30 §5: ilk 2 s insan sesi yok, C01→C02'de ses kopmaz | ✔ | 0.0–22.0 müziksiz; L1 C03 2.0'da (22.0) tek A3; yatak Y1 sürer (ses §6) |
| 1 Okuma cümlesi önce | ✔ | §1 OKUMA |
| 2 En az bir müziksiz an, ideali doruk; 1–2 s önce susar; dönüş tek nota | ✔ | doruk 126.0–140.2 (itişten 2.0 s önce, dönüş tek D); çağrı susması 161.5 (çağrıdan 1.8 s önce, dönüş tek F♯); kopuş 96.0 (kırılmadan 1.2 s önce, dönüş tek A3); akrabalık 38.5 (R07'den 2.4 s önce, dönüş cam D) |
| 3 Fade-out yok; 1–2 gerçek çözülme; kesme ya da çözülmemiş akorla biter | ✔ | çözülme **2** (217.6 · 238.0) = sınır; bitiş 240.0 hard-stop (239.85–240.0 ≤ 150 ms declick, fade değil). 190–212 asılı, Bm eğilimi kadans değil |
| 4 Vuruşlar olaya; kesmeler `kurgu.py liste`'den; faz 4'te tempo yaklaşık | ◐ | ≈60 BPM serbest; girişler olaya (SFX bitişi, nesne olayı, çağrı bitişi). Liste faz 8'de; 10 s katı kesmelerden sapma beklenmiyor |
| 5 Telefon: alt bas oktav eşi, infrases yok | ✔ / N4 | D2 (73) + D3 (147 Hz) eşit; 55 Hz altı yok. Kök yok bölgeleri (22–31, 185.6–212): A3 220 Hz duyulur; 190–212 kök E21'dedir, F8 telefon dinlemesi (N4) |
| 6 Vakum filmi kuru; görüntü kaydırılır; mickey-mousing yok | ✔ | Vakum filmi DEĞİL; küçük kuru oda. Adıma, süzülüşe, atlayışa, yüzgeç oturuşuna vuruş yok; P fazı adımlardan ≥ 0.25 s uzak; girişler çağrı/nesne olayından sonra |
| 7 Miks: −14 LUFS / −1 dBTP; replik altı −6…−9 dB; mono | ✔ | §2; replik yok, çağrı pencerelerinde −9 dB; sarma −6 dB; C12 ≤ −30 LUFS-S |
| 8 Melodi alıntısı yok | ✔ | M özgün (D–E–A); doku betimi isim anmadan |
| GECIS §2.4 Müzik kesintisizdir, kesmede kesilmez; müziksiz anlar plandadır | ✔ | §5: 23 kesmenin hiçbirinde susma/giriş yok; sessizliğe giriş ≥ 1.5 s uzak |
| Sahip briefi (SAHIP_PLANI) | ✔ | sparse suspended tones + cam armonikler (22–38.5) · üç nota motifi iki boyda (58–62) · nabız tehlike boyunca (66–96) · "space for sacrifice and hard landing" (126–140.2) · motif sıcak koruyucu armoniye döner (203.5) · "resolved, expansive final phrase" (237.2–239.85, çözülme 238.0) · organik perküsyon + yaylı · çağrı ve okyanus için boşluk (500–4000 Hz) · tamamen enstrümantal |

---

## 8. DİĞER AJANLARA / FAZ 8'E NOTLAR · AÇIK KARARLAR

1. **Fable:** N1 (F♯ 238.0) ve N2 (L1 96.0) onayı. İkisi de hakem metninde iki cümlenin gerilimidir; seçimim yukarıdadır.
2. **ses-tasarimcisi:** (a) 239.85–240.0 rampa ve Y2 son 1 s solması aynı pencerede; çağrı kuyruğu 239.85'e dek doğal. (b) N4: 190–212 D kökü yalnız E21'de; telefon dinlemesinde duyulmuyorsa E21 +3 dB ya da L1'e D3 −12 dB. (c) 217.6'da R26 D'si ile müziğin D'si kasıtlı birleşir; R26 −14 → −18 inişi çözülmeyi maskelemesin (ses §10 madde 5). (d) 168.4–176.2 "dikkat" perdesiz kalmalı.
3. **kurgucu (F8):** `kurgu.py liste --kesmeler` koşulunca §5 tablosu gerçek çıktıyla kesinleşir. Kesmeye ±1 s müzik olayları: 60 · 110 · 140 · 180 · 190. KESME NOKTALARI tablosu F8 dosyasında (hangi vuruş hangi kesmeye).
4. **F7c / F8 ANLATIM:** (a) N5 müziksiz oran ve susku uzunlukları; (b) F♯ 179.4 duyuluyor mu (−9 → −6 → 181.5); (c) 98.6 tek A3 dönüşü "arıza" gibi mi duyuluyor; (d) 121.0–126.0 kabarma doruk susmasını güçlendiriyor mu, zayıflatıyor mu (kabarmayı çıkarmak 126.0'ı tek D ≤ −30'dan sessizliğe indirir, aralık 110.0–140.2 kesintisiz sessiz-yakın olur); (e) 38.5–58.0 müziksizliği "boşluk" mu "doğru yoğunluk" mu okunuyor.
5. **C20 zinciri (E3):** ışık saati ölçülünce R23 → R24 → P → M → Bm → D'ye dönüş birlikte kayar; 217.6 ve 238.0 kendi ses olaylarından türer, C20'ye bağlı değildir.
6. **Vuruş oynarsa görüntü kayar, müzik değil** (kural 6 ruhu): 202.6 P, Khev'in yüzgece oturuşuna; 217.6 çözülme sprey dağılışı + 0.6; 179.4 F♯ annenin üçüncü notasına bağlıdır. Bu üç bağ görüntü zamanından türer.
7. **Haklar:** Flow Music çıktısı için açık ticari kullanım cümlesi yok; haklar satırı sahibin kontrolünde.

```
ÖZET      MÜZİKSİZ AN 5 (açılış 22.0 · akrabalık 19.5 · kopuş 2.6 · doruk 14.2 · çağrı 17.9 = 76.2 s, %31.8) · ÇÖZÜLME 2 (217.6, 238.0) · KESME İLE BİTİŞ (240.0)
          KATMAN 4 (L1 · L2 · L3 · P), aynı anda en çok 3 sürekli · MÜZİKLİ 163.8 s (%68.3) · TEMPO ≈60 BPM serbest · MERKEZ D · YOĞUNLUK ZİRVESİ 4 (iki kez)
CEVAP     B1-B20: 19 KABUL · 1 KISMEN RED (B11: üst ses F♯ 237.2 → 238.0) · hakem Ek E1-E3 KABUL
AÇIK      N1 F♯ 238.0 (Fable) · N2 L1 96.0 (Fable) · N4 D kökü telefonda (F8 dinleme) · N5 müziksiz oran (ANNE) · Flow Music 2 parça ve saniye hassasiyeti (F8, sahip)
          faz 8: gerçek kesme listesi · seçilen denemelerin ışık/adım saatleri · F7c/F8 ANLATIM sonucu
```
