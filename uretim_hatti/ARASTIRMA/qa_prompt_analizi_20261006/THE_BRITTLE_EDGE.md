# THE_BRITTLE_EDGE
KAYNAK: ham rapor 16 (tool: geçerli 16 · bunların içinde SPEC'li mod D 8 [① ④ ⑥ ⑩ ⑪ ⑫ ⑭ ⑮] · mod V/GEÇERSİZ 6 [② ③ ⑤ tasarım gereği; ⑦ ⑧ ⑨ SPEC verilmesi gerekirken verilmedi] · KESİK/giriş-eksik 2 [⑬ UYUM ×2, 0 bulgu]) · bulgu 31 (🔴 22 · 🟠 9)

> **Nasıl sayıldı.** `--film` başlığı "bulgu 26 → tekil 25", 25 satır listeledi; KARE'nin TOP-3 + ayrıntı tekrarları (0:02 ses ×2, 0:06 duman ×2) birleştirilince 23.
> Listede OLMAYAN 8 bulgu elle eklendi: ⑧ E8 1 · ① KARE bitiş kartı 1 · ⑮ YÖN 01:20 + 01:30 (2) · ⑨ KADRAJ 4 (mod V). ⑮'in 00:40 satırı listede yanlış zamanla (`:10'da sağdaydı`) görünüyor — ayrıştırıcı açıklama metnindeki 00:10'u zaman sandı.
> Yalnız 🔴/🟠 ikonu taşıyanlar sayıldı. Prompt = bölüm dosyaları; ÜRETİM DEFTERİ BOŞ, gönderilen = dosyadaki varsayıldı.

> ⛔ **`--film` / `--sahne` ızgarası bu filmde 1 sahne KAYIK.** SPEC §B `GRID: sahne başlangıcı(n) = 0 hook + (n−1) × 10.0` yazıyor, ama sahneler S00-S11 (0 tabanlı) ve `RUNTIME: 120 s = 10 s + (12−1) × 10 s`. Araç S1'i 0-10 s'ye koyuyor (`--sahne THE_BRITTLE_EDGE 0` → "−10-0 s"). Gerçek: **S00 = 0-10 s … S11 = 110-120 s**; kanıt: ⑧ E1 "kırık parça inceleme" 0:20-0:29 = plan S02 (Teşhis). Bu dosyada S = **gerçek sahne numarası (S00-S11)**; `--film` çıktısındaki S her satırda +1 fazla.
> Videodaki kesme zamanları da 1 s erken (0:09, 0:19 … 1:49 — ① ⑤ ⑦ ⑨) ve S00 içinde 0:05'te bir kesme var; hüküm S'si zaman/10 yuvarlamasıyla verildi.

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime ya da "YOK") | kapanma | not (≤12 kelime) |
|---|---|---|---|---|---|---|---|
| S00 | 🟠 | ① KARE | parçacık/duman/toz | 🅑+ | PHYSICS `Dust lifts and never settles` ↔ NEG `never hovering` | prompt | PHYSICS şablonu 24/24 promptta asılı toz çağırıyor |
| S00 | 🔴 | ① KARE | ortama aykırı ses | 🅐 | AUDIO `No exterior sound at all — only what the suit body carries: breathing inside the helmet` | kurgu-ses | AUDIO tam; plan ise 'çat' sesi bekliyor (çelişki) |
| S00 | 🔴 | ① KARE | parçacık/duman/toz | 🅑+ | PHYSICS `Dust lifts and never settles`; NEG `no airborne smoke clouds` | prompt | çelişen iki cümle; 5-10 s kayma sahnesinde toz tarifi yok |
| S00 | 🔴 | ① KARE | ortama aykırı ses | 🅐 | aynı AUDIO cümlesi; S00'da çalışan motor da yok | kurgu-ses | 0:06 motor ve ezilme sesi; prompt 'dış ses yok' diyor |
| S01 | 🟠 | ① KARE | parçacık/duman/toz | 🅑+ | VIDEO `ejecting dark dust grains in parabolic arcs` ↔ PHYSICS `Dust lifts and never settles` | prompt | parabolik yazılı ama PHYSICS çelişiyor |
| S01 | 🟠 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅐 | CAMERA `high-angle wide perspective lockoff shot` · NEG `no camera resets, no angle change` | araç ayarı | mod V; 'zero movement' ifadesi yok, yalnız lockoff |
| S01 | 🔴 | ⑪ IŞIK | ışık | 🅑 | `Harsh low-angle lunar sunlight cuts across the sharp crater ridge`; saat yönü YOK | prompt | 'o'clock' 0/12; güneş tarafı hiçbir promptta yok |
| S02 | 🔴 | ⑧ EFOR | efor/beden | 🅐 | `Heavy articulated pressurized EVA gloves lift` · `heavy gloved fingers` | araç ayarı | mod V; 0,16 g'de 3-5 kg varsayımı fazla |
| S02 | 🔴 | ⑪ IŞIK | ışık | 🅑 | `Low-angle solar illumination glints off the crystalline facets`; taraf YOK | prompt | kesmede anahtar ışık 10→2 saate dönmüş |
| S03 | 🔴 | ⑧ EFOR | efor/beden | 🅐 | `applying downward leverage with visible shoulder engagement` | araç ayarı | mod V; efor cümlesi promptta var |
| S03 | 🟠 | ⑪ IŞIK | ışık | 🅑 | `stark sunlight highlighting the structural underside framework`; taraf YOK | prompt | kesmede 2→10 saat |
| S04 | 🔴 | ⑧ EFOR | efor/beden | 🅒 | `heavy, deliberate low-gravity motion with clear elbow flexion` | QA | mod V; 6 m sapan 0,16 g'de bel torku vermez |
| S04 | 🟠 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅐 | CAMERA `high-angle wide perspective lockoff shot — the same position, height and lens as Scene 1.` | araç ayarı | mod V; mikro itme 0:44 |
| S04 | 🔴 | ⑮ YÖN | yön/180° | 🅑 | YOK — yalnız `The yellow exploration rover is oriented screen-right`; uçurum/teras tarafı yazılmamış | prompt | SPEC ekran ekseni (uçurum sağda) promptlara inmemiş |
| S05 | 🔴 | ⑧ EFOR | efor/beden | 🅐 | `with visible forearm strain` · `braced in a low three-point crouch` | araç ayarı | D169 efor S05'te zaten istenmişti |
| S05 | 🔴 | ⑪ IŞIK | ışık | 🅑 | YOK — S05'te güneş cümlesi hiç yok; PHYSICS `shadows are absolute black` | prompt | IMAGE promptların 7/12'sinde güneş var; S05'te yok |
| S06 | 🟠 | ① KARE | el-nesne kaynaşması | 🅐 | NEG `Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.` | kadraj kararı | cümle yalnız el-yüzey; karabina-halka kapsamsız |
| S06 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | `crisp tactile click as the glove's textured silicone palm secures the collar tight` | prompt | eldiven direnci, titreme, ince motor zorluğu yok |
| S06 | 🔴 | ⑪ IŞIK | ışık | 🅑 | YOK — S06'da güneş cümlesi hiç yok | prompt | gölge kenarı yumuşadı; yön ve kenar kilitsiz |
| S07 | 🔴 | ⑧ EFOR | efor/beden | 🅑 | `the cable hums under initial pulling torque` — gövde eforu YOK | prompt | kablo gerilimi bedene yansıtılmamış |
| S08 | 🟠 | ① KARE | parçacık/duman/toz | 🅑+ | PHYSICS `Dust lifts and never settles`; NEG sonu `No tumbling rover, no snapping strap.` | prompt | S08'de 'floating dust clouds' negatifi yok (S01 ve S10'da var) |
| S08 | 🔴 | ⑮ YÖN | yön/180° | 🅑 | YOK — `On the distant upper terrace, the lone astronaut stands braced in profile` | prompt | teras sağda mı solda mı yazılı değil |
| S09 | 🟠 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅐 | `dramatic low-angle medium lockoff shot, continues the previous clip from its exact last frame` | araç ayarı | mod V; yavaş sürüklenme 1:32 |
| S09 | 🔴 | ⑪ IŞIK | ışık | 🅐 | VIDEO `START FRAME: continues the previous clip from its exact last frame` | araç ayarı | zincir yazılı ama güneş cümlesi yok; yön döndü, sis belirdi |
| S09 | 🟠 | ⑮ YÖN | yön/180° | 🅑 | YOK — `oriented screen-right` burnu söyler, konumu değil | prompt | S08 ile aynı eksen boşluğu |
| S10 | 🔴 | ⑦ AKSİYON | hikâye/anlatım/kurgu | 🅑+ | IMAGE `rests securely on the level regolit terrace` ↔ VIDEO `rear wheels crest the terrace lip` | prompt | t=0 görseli bitiş durumu; uçurumdan çekme anı yok |
| S10 | 🔴 | ⑧ EFOR | efor/beden | 🅒 | `The astronaut exhales a steady breath inside the helmet` | QA | çekmeyi vinç yapıyor; opak vizörde nefes görünmez |
| S11 | 🔴 | ① KARE | istenmeyen yazı | 🅒 | SPEC `SCREEN TEXT: 0 saniye` · S11 NEG `No end credits, no title cards, no floating text overlay.` | kurgu-ses | kart kurguda eklenmiş (1:59-2:04); ① kapsamı dışı |
| S11 | 🔴 | ⑧ EFOR | efor/beden | 🅒 | `feeling its unyielding frozen weight` | QA | 3-5 kg halka 0,16 g'de omuz yükü vermez |
| S00↔S11 | 🔴 | ⑨ KADRAJ | kamera/kesme/kadraj | 🅐 | iki ucta aynı: `50mm spherical prime lens, distance 1.0 m, height 0.8 m, eye-level close-up lockoff shot` | araç ayarı | mod V; S00 görüntüde alçak açı çıkmış |
| S* | 🔴 | ① KARE | filigran | 🅐 | `no subtitles, no captions, no watermark` · `Output: 16:9, no text, no watermark.` (24/24) | araç ayarı | sağ alt mavi ikon; yalnız KARE gördü |

## ÖZET
```
BULGU          31  (🔴 22 · 🟠 9)
HÜKÜM          🅐 12 · 🅑 10 · 🅑+ 5 · 🅒 4 · 🅓 0
               prompt kaynaklı (🅑 + 🅑+) = 15/31 = %48  ·  önlenebilirlik (🅑+🅑+)/(🅐+🅑+🅑+) = 15/27 = %56
               QA/eşleme kaynaklı (🅒 + 🅓) = 4/31 = %13
TÜR (en sık 5) efor/beden 8 · ışık 6 · parçacık/duman/toz 4 · kamera/kesme/kadraj 4 · yön/180° 3
TÜR (hepsi)    efor/beden 8 · ışık 6 · parçacık/duman/toz 4 · kamera/kesme/kadraj 4 · yön/180° 3 · ortama aykırı ses 2 · filigran 1 · el-nesne kaynaşması 1 · istenmeyen yazı 1 · hikâye/anlatım/kurgu 1
KAPANMA        prompt 15 · araç ayarı 9 · kurgu-ses 3 · QA 3 · kadraj kararı 1
```

Okuma: 31 bulgunun **%48'i promptta önlenebilirdi** (🅑 10 + 🅑+ 5), **%39'u** prompt doğru yazılmışken model/araç tutmadı (🅐 12), **%13'ü** QA/kapsam kaynaklı (🅒 4). 🔴 22'nin dağılımı: 🅑 8 · 🅐 8 · 🅒 4 · 🅑+ 2.
⭐ **Tek cümle 4 bulguyu üretti:** `PHYSICS: … Dust lifts and never settles …` (24/24 prompt) — S00 ×2, S01, S08 toz/parçacık satırları (+ ⑪ S09'daki "hacimsel sis belirdi" gözlemine katkı). Aynı promptun NEGATIVE'i `never hovering` diyor. Aynı cümle `PROMPT_HATA_ONLEME_KILAVUZU` §3.1 vakum şablonunda (30.09) ve THE_STOLEN_SKY · THE_STANDING_WIRE · THE_FALLING_WORLD · LOW_POWER dosyalarında da geçiyor — şablon düzeyinde kusur.
⭐ **Işık + yön 9 satır (6 + 3): 🅑 8 + 🅐 1:** SPEC `sabit tek yönlü güneş` ve `uçurum sağ/alt, teras sol/üst` diyor; 12 promptun hiçbirinde saat yönü ya da uçurum tarafı yok.

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız; 12 sahnenin 24 promptu okundu)
1. **PHYSICS ↔ NEGATIVE çelişkisi — 24/24:** `PHYSICS: Gravity is 0.16 g in hard vacuum. Dust lifts and never settles, shadows are absolute black …` ↔ NEG `Particles obey the stated gravity with continuous momentum, never hovering`. Neden kusur: vakumda toz balistik oturur; "never settles" tam tersini söylüyor ve bulgularda tam bunu ürettik (asılı kalan toz ×4).
2. **`hovering` pozitif metinde — S08 VIDEO, S09 IMAGE:** `hovering completely motionless in mid-air supported entirely by the orange sling` · `all six wheels hovering clear of the rock face` — aynı promptun NEG'i `never hovering`. İki istek çatışıyor; sapan taşıyıcıyı "havada duran" nesneye çeviriyor (🅑+ davet).
3. **S00 insan var/yok çelişkisi:** `IN FRAME: none` ve gövde `No human limbs or figures in frame.`; ama NEG `Exactly one human character, no duplicates, no second person` + `No bare skin on the astronaut` ve AUDIO `breathing inside the helmet`. İnsansız hook karesine tek insan isteniyor. (SPEC insan şeridi `- 1 - 1 …`: S00 doğru, ama S02 de `-` yazılı oysa S02 promptu `Heavy articulated … gloves lift …` ve gövdede diz çökmüş astronot var — ⑭ bunu FAIL saydı; SPEC hatası.)
4. **S00 yapılamaz hareket:** 50 mm / 1,0 m / 0,8 m yakın plan lockoff (plan `0,7 m kadraj`) + `slowly sliding 1.5 meters down the dark basalt slope` + `Single unbroken take, no cuts`. 0,7 m'lik kadrajdan 1,5 m kayan tampon çıkar; videoda 0:05'te kesme var — model ya da kurgu (① KARE 🟡 "S00 5 s'de kesildi"; ⑨ KADRAJ `S2 00:05 WS araç ön görünümü`).
5. **Meta etiket ve KAYIK atıf — 24/24 etiket, 7 prompt hatalı atıf:** etiketler 1 tabanlı (`Scene 1 of 12` = S00), CAMERA atıfları 0 tabanlı: S04 `24mm … distance 12.0 m … — the same position, height and lens as Scene 1.` (Scene 1 of 12 = 50 mm / 1,0 m); S05 `as Scene 3` (=50 mm/0,8 m; kendi satırı 35 mm/2,5 m); S06 `as Scene 2` (=24 mm/12 m; kendi 50 mm/0,8 m); S07 `as Scene 6`; S09 `as Scene 8` (=50 mm/0,8 m; kendi 28 mm/3,5 m); S10 `as Scene 4`; S11 `as Scene 0` (böyle bir etiket yok). Her atıf aynı satırdaki sayılarla çelişiyor. Bu, ⑨'un "rhyme pair" 🔴'sinin zeminini de bulandırır.
6. **S10 IMAGE ↔ VIDEO çelişkisi:** IMAGE `The rover sits fully level on the grey regolit ground … ten meters away from the cliff edge. The winch cable has gone slack` (t=0 = bitiş durumu); VIDEO `The rover's rear wheels crest the terrace lip and touch down … rolls the final two meters onto the level terrace`. Plan D179 "IMAGE eylemin ÖNCESİ t=0'ı gösterir" burada çiğnenmiş; ⑦'nin 🔴 "kurtarma çekimi atlanmış"ı bunun doğrudan sonucu.
7. **Tekerlek sayısı çelişkisi:** prompt `six-wheeled` (S01) · `all six wheels` (S09) · `six heavy wheels` (S10); SPEC §C SAYAÇ `S10 zemin 4 tekerlek` ve hikâye onayı S10 `dört tekerlek`.
8. **IMAGE promptlarında ses ve parçacık hareketi — 12/12:** `AUDIO: No exterior sound at all …` ve `PHYSICS: … exhaust leaves as a straight narrow cone that thins and is gone` hareketsiz kare isteğine giriyor; S00-S11'de egzoz yok.
9. **NEGATIVE ↔ vizör:** `real skin pores and sweat … No bare skin on the astronaut` 12/12 — kask opak aynalı siyah vizörlü (ten hiç görünmez). Ten dokusu isteyen cümle etkisiz; `No face visible through visor` yalnız S03'te var — vizörde yüz çıkarsa iki cümle çatışır.
10. **`EVA` büyük harfli jeton — S02 IMAGE:** `Heavy articulated pressurized EVA gloves lift …` (🅑6; PAYLOAD'da sırta basılan sözcük). Bu filmde basılmadı (0 bulgu) ama kapı dışında.
11. **S01 ölçek:** `Fifty meters away on the stable upper terrace, a lone astronaut … stands rigid` + `IN FRAME: full body` + CAMERA `distance 12.0 m` / plan `12,0 m kadraj`. 50 m'deki figür 24 mm'de kadrajın ≈%4'ü; "okunur astronot" isteği kadrajla uyuşmuyor.
12. **NEGATIVE uzunluğu:** IMAGE 924-956, VIDEO 1013-1037 karakter (VIDEO'da 163-166 kelime = toplam prompt 384-416 kelimenin ≈%41'i); 12/12 aynı çekirdek + sahneye özel 1-2 cümle. İnsansız S00'da bile aynı blok (madde 3).

## 19.09 KURALLARI BU FİLMDE
| kural | yazılı mı (kaç sahnede) | yine de bulgu çıktı mı |
|---|---|---|
| 🅑1 ses yasası | `No exterior sound at all — only what the suit body carries: breathing inside the helmet and a dull knock through the hull.` 12/12 VIDEO + 12/12 IMAGE | 2 🔴 (S00 0:02, 0:06) — ikisi 🅐 (kapanma kurgu-ses). Plan §HOOK `İLK 2 SN SESİ … "çat"` ile AUDIO çelişiyor |
| 🅑2/2a temas | el-yüzey 12/12; nesne-nesne cümlesi 0/12 | 1 🟠 (S06 parmak↔karabina, 🅐); nesne-nesne bulgu 0 |
| 🅑3 giysi birebir | `Equipment and clothing identical throughout` 12/12 · `No bare skin` 12/12; `opaque` vizör sözcüğü 3/12 | 0 (② DEVAMLILIK "HOLDS TOGETHER") |
| 🅑4 ortam sayısı + adı | `Gravity is 0.16 g in hard vacuum` 12/12 (sayı + ad) — **ama aynı satırda `Dust lifts and never settles`** | 4 parçacık/toz bulgusu (🅑+); ⑥ FİZİK 0 bulgu (PASS) |
| 🅑5 efor oranı | nitel efor ipucu 6/8 efor sahnesinde; **sayılı oran düşüşü 0/12** | 8 🔴 (⑧, mod V): 🅐 3 · 🅑 2 · 🅒 3 |
| 🅑6 büyük harfli jeton | `EVA` 1/12 (S02 IMAGE); `Scene n of 12` 24/24; `S0x`/`PHASE` 0 | yazıya basılma: 0 prompt kaynaklı; tek yazı = kurgu kartı (🅒) |
| 🅑7 ekran/metin çelişkisi | ekransız film; metin yasağı 12/12 | 0 |
| 🅑8 dünya çapası | gök/ufuk/yer imi birebir cümlesi **0/12**; `starless/black sky` 4/12, `crater rim/ridge` 6/12, `upper terrace` 7/12, `abyss/chasm` 6/12 | YÖN 3 (🅑) — uçurum/teras tarafı 0/12 |
| 🅑13 ışık saat yönü | `o'clock` 0/12; güneş cümlesi IMAGE 7/12, VIDEO 1/12; `15-degree` IMAGE 3/12 | 6 (⑪): 🅑 5 · 🅐 1 |

⭐ Bu filmde ses (12/12) ve ortam sayısı (12/12) tam yazıldı; ışık yönü (0/12), ekran ekseni (0/12) ve efor oranı (0/12) hiç yazılmadı. Promptta önlenebilir 15 bulgunun (🅑 10 + 🅑+ 5) dağılımı: ışık yönü 5 · ekran ekseni 3 · efor 2 · PHYSICS çelişkisi (asılı toz) 4 · S10 görsel↔video çelişkisi 1 — 15'in 8'i hiç yazılmamış iki kilide (ışık yönü, ekran ekseni), 5'i kendi içinde çelişen iki cümleye düşüyor.

## SAYIMA GİRMEYEN (ikonsuz) — not
- ⑦ AKSİYON B3/B10 ve ⑨ "S2 00:05 WS araç ön görünümü": S00 içindeki klip içi kesme (yukarıda madde 4) — 🟡.
- ⑭ HAREKET `S02 FAIL: SPEC insan şeridi ile çelişki` — SPEC'in kendi hatası (madde 3), 🅒 değil gerçek doküman çelişkisi.
- ⑩ OYUNCULUK `S04, S06, S07 TASK ONLY`, ⑫ HOOK `02:00 kart döngüyü kırıyor` — ikonsuz; kart kurgu eki (SPEC `title card: 0 s`).
