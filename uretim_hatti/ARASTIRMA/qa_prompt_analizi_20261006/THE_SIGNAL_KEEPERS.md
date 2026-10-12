# THE_SIGNAL_KEEPERS
KAYNAK: ham rapor 15 dosya (geçerli 11 · mod V 3 [② DEVAMLILIK · ③ SES · ⑤ ARKA_PLAN — SPEC gereği mod V] · GEÇERSİZ 1 [⑬ UYUM — girdi eksik] · KESİK 0) · bulgu 17 satır (🔴 5 · 🟠 9 · emojisiz 3 [⑨ KADRAJ MISS/NEAR/PAIR FAILS])

## OKUMA NOTLARI (bulgu tablosundan önce)
1. **Eşleme doğru:** QA_SPEC `clip(n) start = (n−1) × 10.0 s` (1-tabanlı, ofset yok); betiğin zaman→klip eşlemesi bu filmde tutuyor (1:47 → K11, 3:45 → K23). Tablodaki "S" sütunu KLİP numarasıdır (6 sahne ≠ 24 klip). `--film` listesi 16 satır verdi (K07 ve K11-KARE üçer kez tekrarlı → 12 tekil bulgu); buraya (listede yok) işaretli 5 satır elle eklendi: ⑫ HOOK 2 · ⑨ KADRAJ 3 (KADRAJ'da 🔴/🟠 emojisi yok, mercek "MISS / NEAR / PAIR FAILS / Requires regeneration" yazdı; şiddet "—").
2. **Promptların yapısı bu filmde 19.09 kurallarına en yakın olanı:** her videoda `AUDIO:` satırı + ortamın ses yasası (24/24), `PHYSICS:` satırı (24/24), `TIMELINE:`, klip bazlı kısaltılmış NEGATIVE. Aşağıdaki hüküm dağılımı bu yüzden öteki iki filmden farklı okunmalı: 🅑 satırları "cümle hiç yok" değil, **tek klipte eksik/belirsiz** kalan cümlelerdir.
3. **SES (③, mod V) raporu 3:00-3:12'de bir MAKİNE sesi duydu** ("Sustained atmospheric pressure at 3.1 bar. The mineral sample shows zero movement … Initiate the manual extraction."); beş mercek (SES · FIZIK · AKSIYON · EFOR · HAREKET) bunu satır olarak kopyaladı. SPEC: HUMAN 0 · MACHINE 0 · RECORDED HUMAN 2. Cümle hiçbir promptta/planda YOK (grep boş); "3.1 bar" yalnız her videonun `PHYSICS:` satırında geçiyor. Hiçbir mercek 🔴/🟠 yazmadığı için tabloya girmedi; kaynağı "PROMPT METNİNİN KENDİ KUSURLARI" madde 6'da.
4. **EFOR (⑧) premise'i SPEC'le çelişiyor:** "surface 1.0g nominal · life-support pack · thin-glove dexterity" yazıyor; SPEC C bloğu 0,42 g + "sırt ünitesi YOK". EFOR "A + C" ister; C bloğu okunmamış görünüyor. Bu premise'e dayanan beklentiler (sırt çantası altında gövde salınımı) 🅒 payı taşır; ilgili satırlarda notlandı.
5. **K17 (insansız klip) için çelişkili tarifler:** KADRAJ S17 "MCU visor close-up in hall", HAREKET M22 / YON V17 "yürüyor" yazıyor; OYUNCULUK ve KARE "boş yuva" diyor ve hepsi PRESENCE `-` kopyalıyor. Bulgu satırı üretilmedi, hüküm yazılmadı.
6. ARKA_PLAN'daki teal `▷` köşe simgesi (00:00–04:00) burada 🟡 LOW — tabloya girmedi (LISTENING_WORLD'te aynı artefakt 🔴 yazılmıştı).

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime alıntı ya da "YOK") | kapanma | not (≤12 kelime) |
|---|---|---|---|---|---|---|---|
| K05 | 🟠 | ① KARE | ışık | 🅐 | image LIGHT: "the low plants are themselves the source of a green-blue light, like lit lamps, not spreading past their edges." | araç ayarı | bloom iki yerde yasak (0% bloom + halo/corona) |
| K07 | 🟠 | ① KARE | diğer | 🅑 | YOK: K07 NEGATIVE kısa; "terrain static, no melting or warping" yok; video: "the leaves close and go dark one after another" | prompt | kasıtlı kısa NEGATIVE terrain-kilidini de attı |
| K10 | 🟠 | ① KARE | el-nesne kaynaşması | 🅑 | IN FRAME: none; video: "one narrow fingertip comes across and taps the piece once and lifts away" | prompt | parmağın sahibi yazılı değil; eldiven/taş-el karıştı |
| K11 | 🔴 | ① KARE | istenmeyen yazı | 🅑+ | "a faint pattern of pale light travels steadily across the outside of the pane"; NEGATIVE: "no environment reflected in it" | prompt | vizöre desen iste, vizör yansımasını yasakla |
| K04 | 🟠 | ⑧ EFOR | efor/beden | 🅐 | "she lets her weight down onto the lower boot, the knee taking it in two stages" | araç ayarı | diz/ağırlık cümlesi yazılıydı; QA 'sırt çantası' varsaydı |
| K05 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | "heavy segmented dark-grey glove"; video: "the fingertip comes down and taps the leaf once" | prompt | eldiven sertliği/yavaş eklem cümlesi yok |
| K11 | 🔴 | ⑧ EFOR | efor/beden | 🅐 | image: sphere "seated in a round brushed-steel seat on her left shoulder"; video: "the sphere does not move" | araç ayarı | prompt küreyi elde tutturmuyor; yük model sapmasından doğdu |
| K20 | 🟠 | ⑧ EFOR | efor/beden | 🅐 | "her forearms lock and her sleeves pull tight"; image: "Her weight is low and back, elbows in." | araç ayarı | efor cümlesi açık yazılıydı; QA 'standart uzanma' gördü |
| K23 | 🟠 | ⑧ EFOR | efor/beden | 🅑 | "the forearm at the frame edge loads"; "the sphere is clear of the seat and held above it" | prompt | küreyi tutan kol/yük hiç yazılı değil |
| K05 | 🟠 | ⑭ HAREKET | oyunculuk | 🅒 | "taps the leaf once, the leaf dips under it and springs back, and the glove lifts away." | QA | SPEC'in HAREKET KİLİDİ 'fingertip TAPS'; dokun-kaldır tasarım |
| K20 | 🟠 | ⑭ HAREKET | oyunculuk | 🅐 | "she works the second ring in one slower turn … and draws the cylinder out into both hands." | araç ayarı | doğrusal hareket yazılıydı; bilek seğirmesi model artefaktı |
| K23 | 🔴 | ⑭ HAREKET | oyunculuk | 🅑+ | "the sphere is clear of the seat and held above it, and the fingertips come off the ring" | prompt | kürenin tutucusu yok; el boşluğu kavradı |
| K03-K04 | 🔴 | ⑫ HOOK (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK; SPEC ⑧: "'Tempo düz' bulgusu ızgaraya yazılamaz" | QA | sabit 10 s ızgara bilinçli; K03 yürüyüş değil, durma |
| K15-K16 | 🟠 | ⑫ HOOK (listede yok) | hikâye/anlatım/kurgu | 🅒 | YOK; SPEC ⑧ + sahne planı (eşik → salon) | QA | yavaş geçiş planlı; 'art arda benzer ölçek' ölçü değil |
| K12 | — | ⑨ KADRAJ (listede yok; emojisiz MISS) | kamera/kesme/kadraj | 🅒 | image CAMERA: "35mm lens on a locked-off camera 1.8 m away, camera height 1.50 m, eye-level medium shot"; "IN FRAME: back · torso" | QA | K12 sırtı dönük E; mercek E'yi 'vizör MCU' sandı |
| K17 | — | ⑨ KADRAJ (listede yok; emojisiz NEAR) | kamera/kesme/kadraj | 🅒 | "IN FRAME: none"; "The aisle beside the cradle is empty" | QA | mercek kendi PRESENCE'ıyla çelişiyor: K17 insansız |
| K01/K24 | — | ⑨ KADRAJ (listede yok; emojisiz PAIR FAILS) | kamera/kesme/kadraj | 🅒 | K24 CAMERA: "the same position, height and lens as Clip 10." | QA | SPEC: K01↔K24 davranış kafiyesi, kamera kafiyesi değil |

## ÖZET
```
BULGU SATIRI    17  (🔴 5 · 🟠 9)
HÜKÜM           🅐 5 · 🅑 4 · 🅑+ 2 · 🅒 6 · 🅓 0
🅑(+🅑+)/(🅐+🅑+🅑+) = 6/11 = 55%   (🅒 ve 🅓 paydadan çıkarıldı)
TÜR (en sık 5)  efor/beden 5 · oyunculuk 3 · kamera/kesme/kadraj 3 · hikâye/anlatım/kurgu 2 · ışık 1
TÜR (hepsi)     efor/beden 5 · oyunculuk 3 · kamera/kesme/kadraj 3 · hikâye/anlatım/kurgu 2 · ışık 1 · diğer 1 · el-nesne kaynaşması 1 · istenmeyen yazı 1
KAPANMA YERİ    prompt 6 · QA 6 · araç ayarı 5
```

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız)
Okunan klip: 24/24 (K01-K24, görsel + video). Her madde: klip · alıntı · neden kusur.

1. **Başka klibe atıf (bağımsız prompt kuralını çiğniyor).** BOLUM başlığı "her prompt tek başına çalışır" diyor; 11 klip numarayla başka klibe gönderiyor: K03 `"— the same position, height and lens as Clip 1."`, K06 → Clip 4, K07 → Clip 5, K11 → Clip 9, K12 → Clip 8, K15 → Clip 13, K19 → Clip 17, K20 → Clip 18, K21 → Clip 19, K22 → Clip 20, K24 → Clip 10. Motor "Clip 10"un ne olduğunu bilmez; atıf yalnızca yazı/anlam gürültüsüdür. Ayrıca 48/48 promptta `Clip N of 24.` meta etiketi var.
2. **"Ten yok" + "yüz tam okunur" (7 klip: K02 · K08 · K09 · K11 · K18 · K20 · K22).** Görsel NEGATIVE: `"No bare skin anywhere — none above the collar, none at the wrists between glove and sleeve"` ile aynı promptun gövdesi: K09 `"Her face fills the frame and is fully readable through a single flat clear pane … the pores and a film of sweat at the temple visible."` Yasak, istenen yüzün kendisini kapsıyor.
3. **İki ışık kaynağı, biri "tek".** K02 LIGHT: `"the only source is the ringed giant planet low over the horizon"`; aynı promptun gövdesi: `"a soft warm 3200K fill from inside the chin of the hard off-white helmet shell"`. K18 ve K20: `"the only sources are points of cold grey light over the nearest cradles"` + aynı 3200K dolgu. SPEC ışık takvimi S01 = "one source (reflected only)". Işık satırı kendi gövdesiyle çelişiyor (yüz klipleri K02 · K18 · K20).
4. **Vizöre desen iste, vizör yansımasını yasakla (K11).** Video: `"a faint pattern of pale light travels steadily across the outside of the pane from left to right"`; NEGATIVE: `"no mirror coating, no tint and no environment reflected in it"` + `"No readable text, letters, digits or symbols on any display"`. Cama yazı/desen oturtan ifade; QA'nın 1:47 "HUD metni" 🔴'si bu cümlenin ürünü.
5. **Tutucusu olmayan nesne (K23).** Video: `"the seat releases and the sphere lifts a finger's width out of it at one slow rate … the sphere is clear of the seat and held above it, and the fingertips come off the ring."` Sonraki klip `"CONTINUOUS ACTION: the dark blue glass sphere is already free of the seat on her shoulder"`. Küreyi kimin/neyin taşıdığı hiçbir yerde yazılı değil; havada asılı kürenin altına el çağrılıyor (PHANTOM 🔴).
6. **Sesli okuma daveti (K19) + PHYSICS satırında sayı.** K19 AUDIO: `"The recorded voice runs on under everything, and nothing else sounds. No dialogue. No music."` — ses isteniyor, sözü yok, "No dialogue" da var; SPEC "cut (no quoted text in the prompt)". Makine sesi 3:00-3:12'de "…atmospheric pressure at 3.1 bar" okudu; "3.1 bar" 24/24 videonun `PHYSICS: Gravity is 0.42 g in a dense cold atmosphere at 3.1 bar and 240 kelvin.` satırında.
7. **Çözülmemiş özne (K10).** `IN FRAME: none` + görsel: `"Nothing in the frame is moving and nothing is touching the hand."` + video: `"one narrow fingertip comes across and taps the piece once"` — insansız klipte (SPEC wall ①) gelen parmak kimin; mineral elin 4 parmağı var ("four equal digits"), "narrow fingertip" beşinci bir uzuv gibi okunuyor.
8. **Kendi kuralını bozan söz (K01 · K03).** SPEC C bloğu: "mist SITS, dust LIFTS AND SETTLES". K01 TIMELINE: `"the upper edge of the mist settles at one slow rate"`; K03: `"the band's edge sharper now that the mist has settled"`.
9. **Havada kalan gönderme.** 21 görsel NEGATIVE'inde `"Particles obey the stated gravity with continuous momentum"` var; görsel promptların hiçbirinde yerçekimi değeri yazılı değil (0/24; değer yalnız videoda, 24/24). Görselin "stated gravity"si yok.
10. **Şişkin NEGATIVE.** İnsanlı 21 klipte görsel NEGATIVE 1038-1237, video 1118-1317 karakter = görsel promptun %42-49'u (ort. %45). İnsansız üç klipte (K07 · K10 · K17) 364-371 / 451-521 karakter — bilinçli (red defteri), ama o kısaltma bu filmde tek terrain-kilidini (K07) de götürdü.
11. **Motorun gösteremeyeceği ifade.** (a) Algılanamayacak derece hareketleri: K01 `"her right shoulder drops half a degree and holds"`, K02/K08/K09/K18 `"her chin comes down one degree"` / `"her head turns one degree toward the valley"` — yarım/bir derecelik baş-omuz hareketi videoda ölçülmez, model ya hiç oynatmaz ya abartır. (b) Nesne olmayan özne: K22 `"the light leaves the top of the frame"`, K10 `"the four digits open with an uneven acceleration, start and hesitate and finish"` (tek hareketin üç evresi). (c) Mekanizması yazılmamış olay: K22 `"the row of frames down the hall tilts up on its mounts"` — ağır iskeletlerin neye bağlı döndüğü yok.

## 19.09 KURALLARI BU FİLMDE
```
kural                         yazılı mı (24 klip)                                            yine de bulgu
🅑1 ses yasası                AUDIO: video 24/24 · ortam yasası ("The cold dense air          0 🔴/🟠 (⚠ SES mod V: K19'da promptta olmayan makine sesi duyuldu,
                              carries low frequencies close and strong and kills the          SPEC MACHINE 0 — hiçbir mercek 🔴/🟠 yazmadı)
                              highs") video 24/24
🅑2 el-yüzey teması           21/24 (K07 · K10 · K17 insansız, bilinçli)                      1 (K10 🅑) + K05 ABANDONED 🅒
🅑2a nesne-nesne teması        genel cümle 0/24; nesneye özel cümle 4 klipte                  0
                              (K05 · K10 · K24 "No hand grips or twists…", K19 "The two
                              hands never touch")
🅑3 giysi birebir             genel "identical throughout" 21/21 insanlı klip; 4 öznitelikli  0 (② DEVAMLILIK "HOLDS", 🔴/🟠 yok)
                              Bible cümlesi görselde TAM 12/21 (K01 K02 K03 K04 K06 K08 K12
                              K13 K18 K19 K21 K22); 9 klipte kısaltılmış/yeniden sıralı
🅑4 ortam sayısı + adı        video PHYSICS satırı 24/24 ("0.42 g … dense cold atmosphere     0 (FIZIK "PHYSICS HOLDS"); ⚠ "3.1 bar" K19'da sesli okundu
                              at 3.1 bar and 240 kelvin") · görselde değer 0/24
🅑5 efor oranı                yük/direnç cümlesi 5/21 insanlı klipte (K04 · K13 · K20 ·       5 (K04 🅐 · K05 🅑 · K11 🅐 · K20 🅐 · K23 🅑): cümle
                              K21 · K23)                                                      yazılı 3 klipte (K04 K20 K23) yine de çıktı
🅑6 büyük harfli jeton yok    PHASE/EVA/S07 türü jeton 0 ✓ · yapı başlıkları (IN FRAME ·     1 🔴 (K11 vizör "HUD": mekanizma jeton değil, "pattern of pale
                              TIMELINE · PHYSICS · AUDIO · NEGATIVE …) 48/48 · "Clip N of     light" cümlesi)
                              24." 48/48
🅑7 ekran/metin çelişkisi     okunacak ekran yok (K02/K03 forearm paneli yalnız ışık atar);   1 (K11 vizör deseni ↔ "no environment reflected")
                              "no readable text … on any display" ile çelişen istek yok
🅑8 dünya çapası              "ringed giant planet" 15/24 görselde · "straight horizon" 5/24   0 (⑤ ARKA PLAN "FIELD HOLDS")
                              · "mist" 5/24 (SPEC: her dış prompta birebir)
🅑13 ışık saat yönü           0/24 ("o'clock" yok; LIGHT satırı kaynağı konumla yazıyor)      0 (⑪ IŞIK "LIGHT HOLDS")
```
Not: bu film 19.09 sonrası sistemle yazılmış (AUDIO + ortam ses yasası + PHYSICS satırı 24/24); 🅑1 ve 🅑4'te bulgu 0 çıkması kuralın işlediğini gösteriyor. Bulguların 🅑'si "cümle yok"tan çok "cümle var ama tek klipte eksik/belirsiz" (K07 terrain, K10 sahip, K11 desen, K23 tutucu) — 19.09 sınıfının uyarısı olan "kısmi" kalıbının aynısı.
