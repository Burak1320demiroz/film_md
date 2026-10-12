# THE_SLOW_RAIN
KAYNAK: ham rapor 27 dosya (geçerli 9 [PART2 ①④⑥⑦⑧⑨⑩⑪⑫, mod D] · mod V 6 [② ③ ⑤ × iki yarım — SPEC gereği mod V] · GEÇERSİZ 11 [PART1'in ①④⑥⑦⑧⑨⑩⑪⑫⑭⑮'i: "INPUT MODE: V", SPEC verilmemiş, FILM: (not supplied)] · KESİK 1 [PART1_13 ⑬ UYUM — "GİRDİ MODU: EKSİK"; PART2'de ⑬ dosyası yok]) · bulgu 48 satır (🔴 20 · 🟠 28)

## OKUMA NOTLARI (bulgu tablosundan önce)
1. **PART1 (S0-S23) 15 raporun hepsi mod V.** `FILM: (not supplied)`, `SPEC BLOCK PROVIDED: no`, ⑥ FİZİK "Numeric Lock Verification skipped". SPEC ①④⑥-⑫⑭⑮ için MOD D ister; bu yarımın merceklerinden hiçbiri SPEC görmedi. Bu yüzden PART1 satırlarının çoğu "tasarımı bilmeyen mercek" (🅒) ya da "prompta bakmadan sayılmış" satırdır; yine de hükmü prompttan verdim.
2. **PART2 dosyaları B2 = S24-S47 görüntüsüdür ama başlıkları S00-S23 diyor.** PART2_KARE `SCENE: Compilation (S00-S23)`, PART2_KADRAJ `FILM: THE_SLOW_RAIN (Part 1 of 2 — S00–S23)` + B1'in kurulum harfleri (`A C R J R B B G I K I G G N O P O P O Q O N R`). İçerik B2: S3 "sled tether … liquid" = S27, S11 "frost flakes" = S35 (SPEC: "S35'te ÖN kabuk dökülür"). Yerel S00-S23 → global S24-S47 olarak (+24) eşlendi. KADRAJ PART2 yanlış planla kıyasladığı için 5 🔴 MISS/seam + 1 🟠 kafiye satırı 🅒.
3. **PART1 mercekleri sahneyi 1-tabanlı sayıyor** (kendi "S1" = 0:00-0:10 = film S0). Bu dosyadaki S, zaman damgasından (floor(t/10)) hesaplandı; "S11|S12" gibi çift yazım bulgunun iki ucudur (hata ikinci sahnede).
4. **Betiğin `--film` listesi bu filmde de hatalı eşliyor:** PART2_ARKA_PLAN satırlarını S09/S10/S29'a koymuş (gerçek S27/S26|S28/S24-S47); PART2 satırlarının zaman sütunu "B2+ 1:35" gibi bozuk. PART1_15_YON'u künye kapısı (süre 46 s) yüzünden listeden düşürmüş; YON mercek 240 s'lik makarayı ~46 s sanıp 2 s/sahne saymış (V18 = 18. eylem = film S17).
5. **⑬ UYUM iki yarım için de koşmadı** (PART1: "EKSİK"; PART2: dosya yok). Prompt ↔ ekran karşılaştırması yapan tek mercek olmadığı için bu filmde "prompt yazıldığı gibi çıkmadı" hükmü hiçbir mercekte doğrudan yok.
6. EFOR (⑧) PART1 "MINOR DEBT", PART2 "THE BODY PAYS" — hiç 🔴/🟠 satırı üretmedi; 19.09 efor oranı cümlesi bu filmin 7 klibinde var (S11 · S18 · S27 · S28 · S31 · S37 · S45; S43 sınırda).

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime alıntı ya da "YOK") | kapanma | not (≤12 kelime) |
|---|---|---|---|---|---|---|---|
| S0 | 🟠 | ① KARE (mod V) | ışık | 🅐 | "0% bloom, no glow, no soft focus, every surface keeps visible texture"; video: "flashes into a white puff" | araç ayarı | bloom yasağı yazılı; 'flashes' fiili parlama çağırmış olabilir |
| S0 | 🟠 | ① KARE (mod V) | parçacık/duman/toz | 🅒 | "The drop lands on the raised glove and flashes into a white puff that rises to knee height and falls back as dry snow" | QA | damla→puf→kuru kar novum; mod V bilmiyor |
| S1 | 🔴 | ① KARE (mod V) | yerçekimi/süzülme | 🅑+ | görsel: "gliding level over the lakebed at one steady rate"; video: "losing height slowly, about a body-length every two seconds" | prompt | düz süzülme ↔ alçalma çelişkisi; sıfır paralaks, hız referansı yok |
| S2 | 🟠 | ① KARE (mod V) | yüz/kimlik | 🅐 | "real skin pores and sweat, no airbrushing, no waxy texture, no face morphing" | araç ayarı | yüz yasakları yazılı; nefeste doku düzleşti |
| S5 | 🟠 | ① KARE (mod V) | diğer | 🅐 | "terrain static, no melting or warping" | araç ayarı | 'okyanus kıyısı' = göl yatağı; doku yüzmesi |
| S6 | 🟠 | ① KARE (mod V) | kask/giysi/ekipman kayması | 🅑 | video: "the wings open to twice her arm-span as she drops away below" | prompt | açılma mekanizması (mafsal/sıra) yok; QA yönü ters okumuş olabilir |
| S8 | 🟠 | ① KARE (mod V) | parçacık/duman/toz | 🅐 | NEG: "Particles obey the stated gravity with continuous momentum"; PHYSICS: "dust settles at once, no wind" | araç ayarı | prompt sıçrama istemiyor; yine de ağırlıksız sprey |
| S9 | 🔴 | ① KARE (mod V) | parçacık/duman/toz | 🅑+ | "the band of drops hangs lower over the lakebed than before"; NEG: "never hovering" | prompt | 'hangs' ↔ 'never hovering'; SPEC: asılı perde YOK |
| S13 | 🔴 | ① KARE (mod V) | zemine geçme | 🅑+ | "she drops at twice the glide rate and meets the lakebed frost on her side, one wing folding under her" | prompt | kanat gövde altına kıvrılıyor; nesne-nesne temas cümlesi yok |
| S15 | 🔴 | ① KARE (mod V) | el-nesne kaynaşması | 🅐 | "Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers." | kadraj kararı | cümle 48/48; tokaya iki eldiven kaynaştı |
| S17 | 🟠 | ① KARE (mod V) | parçacık/duman/toz | 🅑 | "Two drops land on the wet membrane at a slow jogging pace"; kaynak yok, yukarıdan çekim | prompt | damlanın kareye giriş yolu yazılı değil; 'metalden fışkırdı' okundu |
| S20 | 🟠 | ① KARE (mod V) | yerçekimi/süzülme | 🅑 | "She hauls on toward the dome at one steady rate … the sled trailing her" | prompt | kızak–zemin sürtünme/iz cümlesi yok |
| S23 | 🟠 | ① KARE (mod V) | arka plan/dünya çapası | 🅑 | "The base dome on the ridge in the right third, three body-lengths tall" | prompt | mesafe yazılı değil; yaklaşırken boyut sabit |
| S11/S12 | 🟠 | ② DEVAMLILIK | kask/giysi/ekipman kayması | 🅐 | S11 ve S12 görselinde: "one teal band across the chest" | referans/panel | S12 16 m'lik plan; bant yazılı, küçük |
| S13/S14 | 🟠 | ② DEVAMLILIK | kask/giysi/ekipman kayması | 🅑 | YOK (S13-S14'te çarpılma sonrası kar/kırağı durumu yazılı değil) | prompt | giysi durum merdiveni S22'den başlıyor |
| S16/S19 | 🔴 | ② DEVAMLILIK | kask/giysi/ekipman kayması | 🅐 | S19: "the wing rig laid flat on the frost … the core strapped on top" | araç ayarı | QA kanadı sırtta gördü; prompt yerde |
| S17/S18 | 🟠 | ② DEVAMLILIK | kask/giysi/ekipman kayması | 🅐 | S18: "She holds a pale grey wing-spar in both gloves over the sled … the core strapped on top" | araç ayarı | QA kutuyu elde gördü; prompt kızakta |
| S18/S21 | 🟠 | ② DEVAMLILIK | kask/giysi/ekipman kayması | 🅐 | S21: "the core strapped on top sliding past" | araç ayarı | QA kutuyu kayıp saydı; prompt kızakta (yukarıdan çekim) |
| S9/S14 | 🔴 | ② DEVAMLILIK | arka plan/dünya çapası | 🅒 | S9: "The station door is a dark panel"; S14: "The base dome on the ridge in the right third" | QA | iki ayrı yapı tasarım: istasyon SOL, üs SAĞ |
| S14/S15 | 🟠 | ② DEVAMLILIK | hikâye/anlatım/kurgu | 🅑 | YOK (S14→S15 arasında kanatları sırttan çıkarma adımı hiçbir promptta yok) | prompt | CHOICE elipsi; 'sırttan çıkarır' hiçbir promptta yazılı değil |
| S5-S7 | 🟠 | ⑤ ARKA PLAN | arka plan/dünya çapası | 🅑+ | S5: "the rain front hangs over the lakebed as a band of pale beads"; S6: cephe YOK; S7: "The band of drops hangs above her." | prompt | cephe 'asılı bant' yazıldı, S6'da düştü; QA 'geyser' sandı |
| S1-S23 | 🟠 | ⑤ ARKA PLAN | filigran | 🅐 | "no subtitles, no captions, no watermark" (96/96) | araç ayarı | dört köşeli yıldız simgesi; yasak yazılıydı |
| S2/S13 | 🔴 | ⑥ FİZİK (mod V) | yerçekimi/süzülme | 🅒 | PHYSICS: "the dense air slows the rain … while any solid thing let go falls fast" | QA | 0,38 g düşüş tablosu SPEC'te; QA iniş sıçramasını düşüş saydı |
| S7/S20 | 🟠 | ⑥ FİZİK (mod V) | diğer | 🅒 | S7: "spanning twice her arm-span"; S19: "parts the outer wing section" | QA | S19'da dış kanat kesildi; kızak küçülür (plan) |
| S1 · S12 | 🟠 | ⑨ KADRAJ (mod V) (listede yok) | kamera/kesme/kadraj | 🅐 | "fixed locked-off tripod … absolutely zero camera movement" (48/48) | araç ayarı | kilit her promptta; kayma/pan çıktı |
| S0/S23 | 🔴 | ⑨ KADRAJ (mod V) (listede yok) | kamera/kesme/kadraj | 🅒 | YOK; SPEC: "RHYME … S47 ↔ S0"; "S23 ↔ S24 = KÜME" | QA | yarım masterın son karesi kafiye kapanışı değil |
| S3 · S10 | 🔴 | ⑩ OYUNCULUK (mod V) (listede yok) | oyunculuk | 🅐 | S10: "The glove rests on the scratched wing-mark for two full seconds, then slides to the carry handle" | araç ayarı | tereddüt S3/S10'da yazılıydı; QA 'mekanik' dedi |
| S17 · S18 · S19 | 🔴 | ⑩ OYUNCULUK (mod V) (listede yok) | oyunculuk | 🅑 | S19: "The wrist cutter parts the outer wing section along its spar within the first two seconds" | prompt | karar (K) anında beden tereddüdü yazılı değil |
| S13/S14 | 🔴 | ⑩ OYUNCULUK (mod V) (listede yok; 🟠 ③ + 🔴 ⑦ aynı olay) | efor/beden | 🅐 | S14: "she pushes up onto one hip, shoulders lifting into the push and dropping" | araç ayarı | çarpılma bedeli yazılı; beden sıfırlandı |
| S17-S19 | 🟠 | ⑩ OYUNCULUK (mod V) (listede yok) | oyunculuk | 🅑+ | "she keeps … at the same rate through the last second" (27 videoda) | prompt | kapanış formülü tempo değişimini bastırıyor |
| S0/S1 | 🟠 | ⑪ IŞIK (mod V) (listede yok) | ışık | 🅐 | LIGHT (S0 ve S1 birebir): "even amber haze fill from the whole sky, shadows soft and shallow" | araç ayarı | kesmede gri→amber ton sıçraması; satır aynı |
| S3-S5 | 🔴 | ⑫ HOOK (mod V) (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK; SPEC: SAYAÇ ① kırağı çizgisi (S2 · S3) ve ② damla perdesi | QA | tehdit görünür sayaçla taşınıyor; 'tehlike yok' demek yanlış |
| S15-S20 | 🟠 | ⑫ HOOK (mod V) (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK; SPEC: FAILED ATTEMPTS S18 · CHOICES S15 · S19 | QA | başarısız-deneme merdiveni plan kararı |
| S23 | 🔴 | ⑫ HOOK (mod V) (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK; SPEC: "DÖNGÜ KANITI … S0 ↔ S47" | QA | S23 yarım masterın sonu; kapanış S47 |
| S1 | 🟠 | ⑭ HAREKET (mod V) | yerçekimi/süzülme | 🅑+ | görsel: "gliding level"; video: "losing height slowly" (S1 satırı ile aynı kök) | prompt | kukla gibi asılı: düz süzülme ↔ alçalma |
| S17 | 🟠 | ⑮ YÖN (mod V) (listede yok; saat damgası ~46 s'e sıkışık) | parçacık/duman/toz | 🅑 | "Two drops land on the wet membrane at a slow jogging pace" | prompt | S17 satırıyla aynı olay: 'varilden döküm' sanıldı (V18 = S17) |
| S27 | 🔴 | ① KARE | zemine geçme | 🅑 | TIMELINE: "boots dug in"; NEG: "Hand-to-surface contact keeps a clear boundary" (yalnız el) | prompt | bacak/bot–zemin–sıvı sınır cümlesi yok |
| S35 | 🟠 | ① KARE | parçacık/duman/toz | 🅐 | "the pale crust … comes off in flakes … falling away below the frame"; NEG: "continuous momentum" | araç ayarı | pul düşüşü yazılıydı; havada eridi |
| S27 | 🟠 | ⑤ ARKA PLAN | arka plan/dünya çapası | 🅑 | S27 görselinde kubbe cümlesi YOK ("The base dome on the ridge in the right third" 10/48 görselde) | prompt | dış sahnede kubbe birebir cümlesi düşmüş |
| S26/S28 | 🟠 | ⑤ ARKA PLAN | arka plan/dünya çapası | 🅑 | S27: "one pale spar tip and the core's top showing above the liquid" (yer/açı yok) | prompt | batan çubuk ucunun konumu yazılı değil |
| S24-S47 | 🔴 | ⑤ ARKA PLAN | filigran | 🅐 | "no subtitles, no captions, no watermark" (96/96) | araç ayarı | beyaz dört köşeli yıldız; yasak yazılıydı |
| S30 | 🔴 | ⑨ KADRAJ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK; mercek B1 planını kullanmış (A C R J R B B G …); B2 planı: R S T T T Y T V V V O Y O Z E … | QA | yanlış parça beyanı: 'Part 1 of 2 — S00–S23' |
| S35 | 🔴 | ⑨ KADRAJ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK; aynı yanlış plan (I yerine P iddiası) | QA | B2'nin S35'i Y; mercek B1 harfiyle kıyasladı |
| S36 | 🔴 | ⑨ KADRAJ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK; aynı yanlış plan (G yerine N iddiası) | QA | B2'nin S36'sı O |
| S37 | 🔴 | ⑨ KADRAJ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK; aynı yanlış plan (G yerine N iddiası) | QA | B2'nin S37'si Z |
| S29/S30 | 🔴 | ⑨ KADRAJ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK; "küme" B1 harfi B ile yazılmış (S05↔S06) | QA | B2 küme sınırı S31-S33'te; S29/S30 küme değil |
| S24/S47 | 🟠 | ⑨ KADRAJ (listede yok) | kamera/kesme/kadraj | 🅒 | YOK; SPEC: "RHYME … S0 ↔ S47" | QA | B2 içinde S0 yok; kafiye bütün-film kapısı |
| S31-S33 · S36-S38 | 🟠 | ⑫ HOOK (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK; SPEC KÜME: "S31-S32-S33" · sabit 10 s ızgara | QA | küme ve eğimli tırmanış planlı; 'plato' ölçü değil |

## ÖZET
```
BULGU SATIRI    48  (🔴 20 · 🟠 28)
HÜKÜM           🅐 16 · 🅑 11 · 🅑+ 6 · 🅒 15 · 🅓 0
🅑(+🅑+)/(🅐+🅑+🅑+) = 17/33 = 52%   (🅒 ve 🅓 paydadan çıkarıldı)
TÜR (en sık 5)  kamera/kesme/kadraj 8 · parçacık/duman/toz 6 · kask/giysi/ekipman kayması 6 · arka plan/dünya çapası 5 · hikâye/anlatım/kurgu 5
TÜR (hepsi)     kamera/kesme/kadraj 8 · parçacık/duman/toz 6 · kask/giysi/ekipman kayması 6 · arka plan/dünya çapası 5 · hikâye/anlatım/kurgu 5 · yerçekimi/süzülme 4 · oyunculuk 3 · ışık 2 · diğer 2 · zemine geçme 2 · filigran 2 · yüz/kimlik 1 · el-nesne kaynaşması 1 · efor/beden 1
KAPANMA YERİ    prompt 17 · QA 15 · araç ayarı 14 · kadraj kararı 1 · referans/panel 1
```

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız)
Okunan sahne: 48/48 (S0-S47, görsel + video). Her madde: sahne · alıntı · neden kusur.

1. **Kendi novumunu yasaklayan "asılı bant" (S5 · S7 · S9 · S11 · S14).** S5 görsel: `"the rain front hangs over the lakebed as a band of pale beads halfway between the haze and the ridge height."` S9: `"the band of drops hangs lower over the lakebed than before"`; S14: `"the band of drops hangs at her head height"`. Aynı promptların NEGATIVE'i `"never hovering"`; S0/S17/S32 novum cümlesi `"none streaking, none hanging still"`; SPEC: "çizgi YOK, asılı perde YOK". Motor "asılı boncuk bandı" çizdi → PART1 🔴 (S9) ve geyser/plume (S5-S6).
2. **Görsel promptta "Continues the previous clip from its exact last frame" (10 sahne: S6 · S8 · S13 · S24 · S27 · S28 · S32 · S33 · S43 · S44).** Örn. S8 görsel CAMERA: `"… Continues the previous clip from its exact last frame — the same position, height and lens as Scene 8."` Bir IMAGE promptu klibi sürdüremez; videoda ise aynı prompt hem `"START FRAME: the approved still from this scene's IMAGE prompt — animate it"` hem `"Continues the previous clip from its exact last frame"` diyor (iki başlangıç karesi komutu, 10/48).
3. **Düz süzülme ↔ alçalan süzülme (S1 görsel↔video).** Görsel: `"gliding level over the lakebed at one steady rate"`; video: `"losing height slowly, about a body-length every two seconds, no flapping."` Arka plan düz amber sis + düz göl yatağı (sıfır paralaks) ve hız birimi yok → izleyen 3 mercek (KARE · AKSIYON · HAREKET) "asılı kaldı" dedi.
4. **Kanat gövdenin altına kıvrılır (S13).** `"she drops at twice the glide rate and meets the lakebed frost on her side, one wing folding under her."` Nesnenin başka nesnenin altına girmesi isteniyor; temas cümlesi `"Hand-to-surface contact"` yalnız el için, nesne-nesne 0/48.
5. **Parlama iste, parlamayı yasakla.** S0/S7/S24/S47 video: `"flashes into a white puff"` ve S44 görsel: `"the round lamp in the socket rim is lit as one warm point"` — NEGATIVE: `"0% bloom, no glow, no soft focus"` (48/48). Işık olayı olan her klipte çelişen iki komut.
6. **Şişkin NEGATIVE.** Görselde 1071-1165, videoda 1151-1245 karakter; görsel promptun %44-58'i (ort. %48). Elin dışında hiçbir şey görünmeyen kliplerde (S3 · S10 · S15 · S17 · S19 · S34, `IN FRAME: hands`) `"real skin pores and sweat, no airbrushing, no waxy texture, no face morphing"` hâlâ var.
7. **Meta etiket.** `Scene n of 48.` 96/96 prompt; S+1 numaralaması dönüş atıflarında tutarlı (`as Scene 3` = S2) ama "Scene 48 of 48" meta etiketi kadraja basılabilir (THE_SOLAR_MIRROR "S04" vakası, 🅑6).
8. **Sayı/ölçü istemek.** `"Her glove tugs the buckle exactly twice"` (S6 · S12), `"the third pull shorter than the first"` (S27-S28), `"her first steps are half a boot shorter"` (S31), `"one drop every few seconds"`; saymayı ve oran ölçmeyi motor yapamaz (efor oranı cümlesi 7 klipte yazılı olmasına rağmen bir kısmında ölçülemiyor). `"at one steady rate"` 27 videoda hız birimi olmadan.
9. **Mekanizması yazılmayan olay.** S6: `"the wings open to twice her arm-span as she drops away below"` — sırtta katlı "iki membran + çubuk + tek toka" nasıl açılıyor yok → KARE 1:03 "kumaş gibi morf". S19: `"The wrist cutter parts the outer wing section along its spar"` — kesicinin ne olduğu bileğe "hooked cutter" diye iliştirilmiş, kesme geometrisi yok.
10. **Görselde olmayan gönderme.** NEGATIVE'lerde `"Particles obey the stated gravity"`; görsel promptların 0/48'inde yerçekimi değeri yazılı (g yalnız videonun `PHYSICS:` satırında, 48/48).
11. **Büyük/küçük harf ve bölünmüş cümle.** S1 görsel: `"… a thick dark rim. her wing rig open, two taut dark smoke-grey membranes …"`; S2 · S4 · S23 · S24 görsel bölümleri küçük harfle başlıyor (`"her close-fitting pale grey ribbed pressure suit"`) — şablon birleştirme izi; özne eksik cümle.
12. **Ortam bilgisi çelişkisi (iç mekân).** S4 video PHYSICS: `"any meltwater drips fall fast"`; S10 video PHYSICS: `"frost coats every surface and nothing drips"`. Aynı üs içinde iki kural.

## 19.09 KURALLARI BU FİLMDE
```
kural                         yazılı mı (48 sahne)                                               yine de bulgu
🅑1 ses yasası                AUDIO: video 48/48 · ortam yasası 48/48 (dış: "sound carries low,   0 🔴/🟠 (③ SES mod V; PART1/PART2 ikisinde ses bulgusu yok)
                              heavy and close in the dense cold air … no high frequencies" · iç:
                              "near silence inside")                                              → kural işledi
🅑2 el-yüzey teması           48/48 (görsel + video)                                              1 (S15 🔴 eldiven-toka 🅐)
🅑2a nesne-nesne / ayak-zemin  0/48                                                                2 (S13 🔴 kanat-zemin 🅑+ · S27 🔴 bot/bacak-sıvı 🅑)
🅑3 giysi birebir             "identical throughout" 48/48; Bible giysi cümlesi birebir 34/48       7 satır ②: S11|S12 🅐 · S13|S14 🅑 · S16|S19 🅐 · S17|S18 🅐 ·
                              görselde; KANAT/KIZAK/SIRT cümleleri bölümlere göre yazılı             S18|S21 🅐 · S9|S14 🅒 · S14|S15 🅑
🅑4 ortam adı + sayısı        video PHYSICS 48/48 ("0.38 g … 0.9 bar and 95 kelvin"); görselde 0/48 2 (⑥ mod V F1/F2, ikisi 🅒); PART2 FİZİK 🔴/🟠 0
🅑5 efor oranı                7/48 (S11 · S18 · S27 · S28 · S31 · S37 · S45; S43 sınırda)          0 EFOR 🔴/🟠 (⑧ "MINOR DEBT" / "THE BODY PAYS") → kural işledi;
                                                                                                    ⑩ OYUNCULUK mod V'de 1 efor satırı (S13|S14 🅐)
🅑6 büyük harfli jeton yok    PHASE/EVA/S07 türü jeton 0 ✓; yapı başlıkları 96/96;                 0 içerik yazısı bulgusu (istenmeyen yazı 0); 2 filigran 🅐
                              "Scene n of 48." 96/96
🅑7 ekran/metin çelişkisi     "No screen, no readout, no digits on the socket or the lamp"         0
                              (S3 · S4 · S10 · S42-S46)
🅑8 dünya çapası              gök cümlesi 40/48 · göl yatağı cümlesi 40/48 görselde; "base dome"   5 (S5-S7 🅑+ · S9|S14 🅒 · S23 🅑 · PART2 S27 🅑 · PART2 S26|S28 🅑)
                              cümlesi 10/48 (SPEC: 22 dış sahnede birebir); "old station" 6/9
🅑13 ışık saat yönü           0/48 ("o'clock" yok; SPEC: saat yönü yok, pus dolgusu)                1 (S0|S1 ton sıçraması 🅐)
```
Not: SLOW_RAIN 22.09.2026'da yazıldı (19.09 sınıf belgesinden 3 gün sonra) — AUDIO + ortam ses yasası + PHYSICS satırı + sayı/oran cümleleri sistematik olarak yazılı; bulgular 🅐 (filigran, el-yüzey, yasak yazılı bloom/doku) ve dünya çapası/nesne-nesne/asılı-bant boşluklarında toplanıyor.
