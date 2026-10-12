# THE_STILL_POINT
KAYNAK: ham rapor 12 (geçerli 9 · mod V/GEÇERSİZ 3 [⑦ ⑧ ⑨ `INPUT MODE: V`; tool 12/12 geçerli sayıyor] · KESİK 0) · bulgu 42 (🔴 13 · 🟠 29)
SAYIM KURALI: satır = (mercek, olay, sahne). `--film` listesi 24 satır verdi (① S04·S08 ikişer kez); çok sahneli tek ham satır (⑨ Lockoff 11 sahne, ⑩ Hands/Posture/Cost) sahneye bölündü, filigran iki mercekte ayrı sayıldı → 42 satır. 14'ü `(listede yok)`: ① filigran · ⑤ filigran · ⑨ 12 satır (mod V olduğu için tool dışarıda bıraktı). ⑩ 11 satırı listede 5 ham satırdı.
MASTER SORUNU: ⑦ ⑧ ⑩ kısa/farklı master'ı ölçtü (⑦ ~187 s/19 sahne, ⑧ 245 s/20 sahne [03:05 sonrası siyah ekran], ⑩ 196 s/20 sahne; tool ③ künye uyarısı verdi), ⑨ 04:05'te 24 "sahne" sayıyor ama S18'den sonra zamanlar ızgaraya oturmuyor (02:50, 02:57, 03:00, 03:10…). Çapa olarak zaman damgası kullandım; S16 sonrası içerik ② ⑤ ⑩'da plandan 1-2 sahne kaymış → o satırlar 🅓.
TOOL ÇAPASI: 0-tabanlı filmde `≈S-ref` çapaları −1 kaymış (⑩: tool S01/S03/S08/S11/S18 → ham metne göre S02·S09·S12 / S04·S07·S10·S12 / S09 / S12·S13 / S19). Ham metne göre yazdım.
S = SAHNE no (plan S00-S23, 1 sahne = 1 klip = 10 s). ② ③ ④ ⑥ ⑪ ⑫: 0 adet 🔴/🟠 (⑪ 3 🟡 ışık sıçraması; ① S07 bloom 🟡; ⑤ S06/S08 dikme sayısı 🟡 ve S07/S10 kadran sahte rakamı şiddetsiz).
SPEC: yeni rejim (00_HIKAYE_ONAYI 20.09.2026); bilinçli kararlar: opak vizör, repliksiz, kafiye nesne ile (kurulum ile değil), S01+S05 insansız.

## BULGULAR
| S | şiddet | mercek | tür | hüküm | promptta ne yazıyor (≤20 kelime alıntı ya da "YOK") | kapanma | not (≤12 kelime) |
|---|---|---|---|---|---|---|---|
| S00-S23 | 🔴 | ① KARE (listede yok) | filigran | 🅐 | NEG: "no subtitles, no captions, no watermark" (IMG+VID 24/24; "Output: ... no watermark") | araç ayarı | Sağ alt köşe logosu 240 sn; yazılı yasak tutmadı |
| S04 | 🟠 | ① KARE | el-nesne kaynaşması | 🅐 | NEG: "Hand-to-surface contact keeps a clear boundary, no extra fingers" | kadraj kararı | Bırakma anı 15 m EWS'de; QA "sol el", prompt sağ el |
| S06 | 🟠 | ① KARE | yerçekimi/süzülme | 🅑 | PHYSICS: "magnetic sole grip releases with clean mechanical detachment at every step" | prompt | Kalkış yazılı; basış/sürtünme kilidi yok (moonwalk) |
| S08 | 🟠 | ① KARE | el-nesne kaynaşması | 🅑+ | IMG: "pull the clamping lever down" ↔ VID: "pull the cam-lock restraint lever upward" | prompt | Kol yönü çelişkisi; VID özeti de "slams ... down" diyor |
| S00-S23 | 🔴 | ⑤ ARKA PLAN (listede yok) | filigran | 🅐 | NEG: "no subtitles, no captions, no watermark" (24/24) | araç ayarı | ① ile aynı artefakt, ikinci mercek |
| S05 | 🟠 | ⑤ ARKA PLAN | sayı/nesne sayısı | 🅑 | S05 IMG: "the rotating perimeter girders sweep along the left frame edge" | prompt | İstasyon göbeği eksen sayısı hiçbir promptta rakamla yok |
| S04 | 🟠 | ⑤ ARKA PLAN | ışık | 🅑 | S03: "Stark contrast lighting." · S04: "Direct sunlight edge highlight." | prompt | Güneş yönü saat/açı yok; LIGHT satırı hiç yok |
| S09 | 🟠 | ⑤ ARKA PLAN | arka plan/dünya çapası | 🅒 | S09 IMG: "The station's structural ribs blur past in the background." | QA | Hız bulanıklığı; QA kendi çözümü "Kabul Et" |
| S12 | 🟠 | ⑤ ARKA PLAN | arka plan/dünya çapası | 🅒 | S11 "35mm ... distance 2.5 m" ↔ S12 "24mm ... distance 3.5 m" | QA | Lens değişti (D→F); farklı kurulumda ölçek ölçülmez |
| S12 | 🟠 | ⑦ AKSİYON (mod V) | hikâye/anlatım/kurgu | 🅑+ | IMG: "The cart floats free of the rail heads" ↔ VID 0.0s: "both gloved hands push hard ... separating it" | prompt | Start-frame itme sonrası; kopma anı klipte yok |
| S15 | 🔴 | ⑦ AKSİYON (mod V) | kamera/kesme/kadraj | 🅑+ | IMG: "launching cleanly off the gantry beam ..., legs trail straight behind" ↔ VID 0.0s: "legs thrust straight backward against the beam" | prompt | Still havada; itiş anı video başında isteniyor |
| S00 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅒 | VID: "the gloved fingers spread apart as the orange wrench clears the grip" | QA | Bırakma/uzanma iş sayılmaz; plan bütçesi eşya |
| S02 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅒 | PHYSICS: "Low apparent gravity of zero point six four metres per second squared; gentle ballistic gait" | QA | 0,065 g'de ağır adım beklentisi SPEC'e ters |
| S03 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅑 | VID: "the right gloved hand releases the girder and reaches down to unclip a utility telemetry radio" | prompt | Eldiven sertliği/parmak direnci cümlesi yok |
| S04 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅒 | VID: "The fingers spread fully open, letting the radio fall freely away from the palm" | QA | QA "sürünen çantaya uzanma" anlatıyor; prompt radyo bırakma |
| S06 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅒 | PHYSICS: "Consistent low gravity footing; magnetic sole grip releases ..." | QA | 0,065 g yürüyüşü; "hız düşüşü/hantallık" beklentisi yersiz |
| S07 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅒 | VID: "thumb depresses the safety locking dog on the handle top" | QA | Hafif iş; "pazı/omuz kasılması" beklentisi yersiz |
| S08 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅐 | VID: "forearm muscles tensing noticeably beneath the ballistic fabric ... twenty-degree forward torso lean" | araç ayarı | Efor cümlesi + 20° sayı yazılı; gösterilmedi |
| S12 | 🔴 | ⑧ EFOR (mod V) | efor/beden | 🅑+ | PHYSICS: "the astronaut absorbs minimal recoil through braced deck footing" | prompt | "Minimal recoil" tepkisizliği bizzat istiyor |
| S00 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅐 | CAMERA: "locked-off tripod, medium close-up, Dutch angle tilted 15 degrees. In a single continuous shot." | araç ayarı | Kilit yazılı 24/24; 00:03 yavaş sürüklenme |
| S01 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅐 | CAMERA: "locked-off tripod, extreme wide shot, high-angle looking downward" | araç ayarı | 00:12 yavaş itme; yazılı kilit tutmadı |
| S02 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅐 | CAMERA: "locked-off tripod, medium shot, eye-level angle" | araç ayarı | 00:22 ileri kayma; yürüyen figürü takip etti |
| S06 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅐 | CAMERA: "locked-off tripod, medium shot, low-angle looking upward" | araç ayarı | 01:03 yana itme |
| S08 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅐 | CAMERA: "locked-off tripod, medium shot, low-angle looking upward" | araç ayarı | 01:24 dikey yeniden ortalama |
| S09 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅑+ | CAMERA: "locked-off tripod, close-up" ↔ IMG: "cart accelerates rapidly down the curved steel railway" | prompt | Hareketli araçta "tripod"; kamera nerede? Çelişki |
| S11 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅑+ | CAMERA: "locked-off tripod, medium shot" ↔ IMG: "the astronaut riding the speeding cart" | prompt | 01:53 dolly-out; araçtan çekim tripodla çelişir |
| S16 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅐 | CAMERA: "locked-off tripod, extreme wide shot, eye-level angle" | araç ayarı | 02:43 yavaş yaklaşma |
| S19 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅓 | CAMERA: "locked-off tripod, wide shot, low-angle looking upward" | QA | Rapor "S21 03:14"; içerik plandan 1-2 sahne kaymış |
| S20 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅓 | CAMERA: "locked-off tripod, medium shot, low-angle looking upward" | QA | Rapor "S22 03:25 push-in"; içerik plandan kaymış |
| S22 | 🟠 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅓 | CAMERA: "locked-off tripod, wide shot, low-angle looking upward" | QA | Rapor "S24 03:45 dolly-back"; ızgara dışı |
| S00·S23 | 🔴 | ⑨ KADRAJ (mod V · listede yok) | kamera/kesme/kadraj | 🅑 | S00 "35mm ... distance 2.0 m, height 1.5 m ... Dutch angle" ↔ S23 "35mm ... distance 2.5 m, height 1.1 m, low-angle" | hikâye/plan | SPEC "EŞ KADRAJ S00↔S23" diyor; plan harfleri A≠D |
| S04 | 🟠 | ⑩ OYUNCULUK (Hands as Intent) | oyunculuk | 🅐 | VID 10.0s: "hold on the motionless open glove" | araç ayarı | Bırakış sonrası bekleme yazılı |
| S07 | 🟠 | ⑩ OYUNCULUK (Hands as Intent) | oyunculuk | 🅐 | VID: "the glove taps the brass casing of the dial twice in calculated assessment" | araç ayarı | Tereddüt vuruşu yazılı |
| S10 | 🟠 | ⑩ OYUNCULUK (Hands as Intent) | oyunculuk | 🅐 | VID: "forearm grip loosens by five millimetres as the vibration noticeably dampens" | araç ayarı | Bırakma 5 mm yazılı |
| S12 | 🟠 | ⑩ OYUNCULUK (Hands as Intent) | oyunculuk | 🅐 | VID: "the astronaut lowers her arms, standing completely alone" | araç ayarı | İtiş ve sonrası yazılı |
| S02 | 🟠 | ⑩ OYUNCULUK (Posture & Weight) | oyunculuk | 🅐 | VID 0.0s: "the figure shifts weight onto the left leg, adjusting balance" | araç ayarı | Ağırlık aktarımı yazılı |
| S09 | 🟠 | ⑩ OYUNCULUK (Posture & Weight) | oyunculuk | 🅐 | VID: "the astronaut leans fifteen degrees forward into the acceleration vector, arms rigid" | araç ayarı | 15° sıkılaşma yazılı |
| S12 | 🟠 | ⑩ OYUNCULUK (Posture & Weight) | oyunculuk | 🅑 | PHYSICS: "absorbs minimal recoil through braced deck footing" | prompt | Karar sonrası omuz/ağırlık değişimi yok (plan TELAFİ) |
| S09 | 🔴 | ⑩ OYUNCULUK (Central Choice) | oyunculuk | 🅑 | S08 sonu: "her hands rise to grasp the twin steering throttles" · S09 IMG: "stands braced ..., hands gripping the control yoke tightly" | prompt | Önce/sonra aynı poz yazılı; tereddüt→taahhüt farkı yok |
| S12 | 🟠 | ⑩ OYUNCULUK (Cost & Aftermath) | oyunculuk | 🅑 | VID: "standing completely alone on the edge of the severed catwalk sill" | prompt | Bedelin bedende ağırlığı yok; plan TELAFİ'si inmemiş |
| S13 | 🟠 | ⑩ OYUNCULUK (Cost & Aftermath) | oyunculuk | 🅒 | VID 0.0s: "her arms extended outward slightly to stabilize roll in zero-g" | QA | S13 = dinginlik atışı; bedel S12'de ödendi |
| S19 | 🟠 | ⑩ OYUNCULUK (Final Beat) | hikâye/anlatım/kurgu | 🅓 | YOK | kurgu-ses | Master 03:16'da kesik; S23 kafiyesi hiç ölçülmedi |

## ÖZET
hüküm: 🅐 16 · 🅑 8 · 🅑+ 6 · 🅒 8 · 🅓 4 (42 satır) → prompt payı (🅑+🅑+)/(🅐+🅑+🅑+) = 14/30 = %47 · QA yanılgısı + eşlenemeyen 12/42 = %29. 🅐'nın 16'sı: 2 filigran + 6 lockoff + 6 ⑩ "cümle var" + S04 temas + S08 efor.
mercek: ① 4 · ⑤ 5 · ⑦ 2 · ⑧ 8 · ⑨ 12 · ⑩ 11.
tür (en sık 5): kamera/kesme/kadraj 13 · oyunculuk 10 · efor/beden 8 · filigran 2 · el-nesne kaynaşması 2 (eşit: arka plan/dünya çapası 2 · hikâye/anlatım/kurgu 2; ayrıca yerçekimi/süzülme 1 · sayı/nesne sayısı 1 · ışık 1).
kapanma yeri: araç ayarı 15 · prompt 13 · QA 11 · kadraj kararı 1 · hikâye/plan 1 · kurgu-ses 1.
Okuma: ⑧'in 8 🔴'sinin 5'i 🅒 (mod V mercek 0,065 g'yi ve işin hafifliğini bilmeden "kimse ödemiyor" yazdı); gerçek prompt boşluğu S03 (eldiven sertliği) ve S12 ("minimal recoil" davetli). ⑨ mod V'nin 12 satırı: lockoff 6 🅐 (kilit 24/24 yazılı) + 2 🅑+ (araçtan çekim ↔ tripod) + 3 🅓 + rhyme 🅑. İki filigran 🔴 prompt işi değil, araç ayarı.

## PROMPT METNİNİN KENDİ KUSURLARI
(24 sahnenin tamamı, IMAGE+VIDEO, okundu.)
1. **Meta etiket + kayık numaralama** — 24/24 IMAGE ve VIDEO: `Scene 3 of 24.` SAHNE 2 için (S00 → "Scene 1 of 24", S23 → "Scene 24 of 24"). Atıflar ise dosya numarasıyla: SAHNE 3 CAMERA "… — the same position, height and lens as Scene 01" (dosyada S01, ama prompt içi numarayla Scene 01 = S00). Aynı promptta iki numaralama.
2. **Başka prompta atıf** — 14 sahne (S03·S04·S05·S08·S09·S10·S11·S15·S16·S17·S20·S21·S22·S23): "… locked-off tripod, extreme wide shot, high-angle looking downward — the same position, height and lens as Scene 03." Model Scene 03'ü görmez; tam kamera cümlesinin ARKASINA eklenmiş (çift kayıt).
3. **İki ayrı start-frame emri** — S04, S10, S16, S22 VID CAMERA: "…; continues the previous clip from its exact last frame — the same position, height and lens as Scene 03" ama aynı promptun 3. satırı: "START FRAME: the approved still from this scene's IMAGE prompt". Hangisi geçerli?
4. **IMG ↔ VID çelişkisi** — S00 IMG: "The gloved right hand ... reaches forward toward a dislodged steel mounting bracket" ↔ VID: "the gloved hand pulls backward toward the suit torso". S08 IMG: "pull the clamping lever down" ↔ VID: "pull the cam-lock restraint lever upward" (VID'in kendi özeti "slams the foot restraint lever down"). S12 IMG: "The cart floats free of the rail heads" ↔ VID 0.0s: "both gloved hands push hard against the yellow cart chassis"; ayrıca konum S11 "tünel" → S12 "outer sill of the open gantry". S15 IMG: havada "legs trail straight behind" ↔ VID 0.0s: "legs thrust straight backward against the beam". S04 IMG: "In the open right palm sits ... telemetry box" ↔ VID 0.0s: "fingers remain cupped around the telemetry unit".
5. **Ekran isteyip metni yasaklamak (🅑7)** — S07 IMG: "analog speedometer dial ... mechanical needle indicators"; S10 IMG: "needle aligns precisely with the eight metres per second marker", VID: "the needle climbs steadily past the six and seven metre marks on the gauge face". NEG (S07 ve S10, IMG+VID): "No readable text, letters, digits, numbers or symbols on any display". ⑤ raporu bu iki sahnede "gösterge kadran rakamları AI pseudotext" gördü.
6. **Kendi plan kuralını çiğneyen yön dili** — PLAN D174: "Yönler screen-right yerine merkez aks, halka yayı ve ray ekseniyle verilir (S00-S23)". Promptlar: "The vehicle is oriented facing screen-left, its bow heading along the counter-rotation track" 14× (S07–S12, IMG+VID; aracın görünmediği S07 gösterge CU'sunda bile), S05 IMG: "drifting rapidly sideways toward screen-right".
7. **SPEC ile PHYSICS çelişkisi** — SPEC YERÇEKİMİ: S00–S11 0.065 g, S12: 0.065→0, S13+: 0. S10 VID PHYSICS: "apparent centrifugal gravity drops to absolute zero, causing loose suit straps to float"; S11 AUDIO: "weight drops to microgravity". Fizik doğru (teğet hız sıfırlandı) ama SPEC'te bu iki sahne hâlâ 0.065 g; ⑥ hiçbir şey yakalamadı (PHYSICS HOLDS).
8. **Hareketli araçta tripod** — S09–S12 CAMERA: "50mm macro prime lens, distance 1.0 m ... locked-off tripod, close-up" ile IMG "cart accelerates rapidly down the curved steel railway", "structural ribs blur past". Kamera ya araçla gider ya sabit durur; ⑨ iki yerde (S09, S11) kamera oynaması ölçtü.
9. **Sayı tutarsızlığı** — PLAN: t_cross = 92,5 m / 2 m/s = 46,25 s, S15–S19. S17 VID 10.0s: "closing within twenty metres of the target" (S15 başından 30 s × 2 = 60 m gitti → 32,5 m kalır); S19 VID 0.0s: "closing the final three metres of void" (40 s → 80 m → 12,5 m kalır).
10. **Kimlik bir kez yazılıp kopyalanmamış** — gri gövde + beyaz göğüs + turuncu bant üçlüsü insanlı 22 sahnenin yalnız 5'inde birlikte (S02·S03·S06·S09·S16); turuncu bandın TARAFI ("right") 6/22; opak vizör cümlesi 6/22. S23 IMG: "suit unlatched at the collar ring" — SPEC KİMLİK DİZİSİ "kask hep kapalı (K)"; "unlatched" açık kask/yüz riski doğurur.
11. **Büyük harfli jeton** — "ORISON" 6× (S00·S01·S13·S17·S23×2), "EVA" 7×, "LED" 2×; "ORION" gibi büyük harfli ad göğse yazıldığı ölçülmüş (THE_CRACKED_HELMET). Bu filmde kadraja yazı basıldığına dair 🔴/🟠 yok.
12. **NEGATIVE şişkinliği** — IMG 644 / VID 693 karakter (insanlı 22 sahne), IMG 471 / VID 520 (insansız S01·S05); prompt toplamının %42 ve %35'i. İçinde kamera oynamasını yasaklayan tek cümle yok (⑨ 11 lockoff 🟠) ve ortam/yerçekimi cümlesi yok.
13. **Dünya çapası** — "Saturn" IMG gövdesinde yalnız 11/24 sahnede (S00·S01·S03·S04·S05·S15·S16·S17·S18·S20·S23); boşluk sahneleri S12·S13·S14'te yok. LIGHT satırı yok; ışık cümlesi her CAMERA'nın son yarım cümlesi ("Stark contrast lighting.", "Clean cabin LED lighting.") — 24 ayrı metin.

## 19.09 KURALLARI BU FİLMDE
| kural | yazılı mı (kaç sahnede) | yine de bulgu çıktı mı |
|---|---|---|
| 🅑1 ses yasası | AUDIO satırı 24/24; ortam adı ("vacuum") yalnız 4/24 (S01·S04·S05·S16); iletim yolu cümlesi ~8/24; S22 hava geçişi doğru ("conduction to airborne") | ③ SES: 0 🔴/🟠 (SOUNDTRACK HOLDS); ⑦ yalnız out-of-scope "ağır sesler duyuluyor" |
| 🅑2/2a temas | el-yüzey cümlesi 22/22 insanlı sahne (IMG+VID); nesne-nesne 0/24 | 2 🟠 (① S04 bırakma, ① S08 eldiven↔kol) — cümle varken; ⑦ yakalama belirsizliği 🟡 |
| 🅑3 giysi birebir | genel "Equipment and clothing identical throughout" 22/22; Bible üçlüsü birlikte 5/22; turuncu bandın tarafı 6/22; opak vizör 6/22 | 0 🔴/🟠 (② HOLDS 13×10/10; ② S03 vizörde yüz silueti yalnız not) |
| 🅑4 ortam sayısı+adı | yerçekimi SAYISI yalnız S02 (0.065 g · 0.64 m/s²); S06 "low gravity" sayısız; "vacuum" adı ~8/24 (NEG dahil); S10–S11 PHYSICS SPEC'ten ayrı | 0 🔴/🟠 (⑥ PHYSICS HOLDS) — ama ⑥ L5 kendi ölçümünü (0,069 m/s²) 0,637 m/s² ile "Tutarlı" saymış (şiddetsiz hata) |
| 🅑5 efor oranı | sayı VAR 6 sahnede (S08 20° · S09 15° · S10 5 mm/10 kg · S14 2° · S21 15° · S22 10 kg); oran düşüşü 0/24 | 8 🔴 (⑧, tümü mod V): 1 🅐 · 1 🅑 · 1 🅑+ · 5 🅒 |
| 🅑6 büyük harfli jeton yok | "ORISON" 6×, "EVA" 7×, "LED" 2×; "Scene n of 24" meta 24/24 | kadraja basılan yazı: 0 🔴/🟠 |
| 🅑7 ekran/metin çelişkisi yok | İHLAL: S07 ve S10 (2/24) — gösterge okuması + NEG "digits, numbers" | 0 🔴/🟠 ama ⑤ S07/S10 kadranda "AI pseudotext" (şiddetsiz, "Recovered: Hayır") |
| 🅑8 dünya çapası | Saturn 11/24; S12·S13·S14 yok; "ORISON ring" S01·S13·S17·S23 | 3 🟠 (⑤ S05 eksen sayısı · S09 kaburga sıklığı [🅒] · S12 ölçek [🅒]) |
| 🅑13 ışık saat yönü | 0/24; LIGHT satırı yok | 1 🟠 (⑤ S04 gölge üst-sağ→üst-sol); ⑪ 3 🟡 ışık sıçraması (S12/S14/S16 geçişleri) |

Ölçüm notu: 19.09'un en net iki yazım kuralı bu filmde ya hiç yok (🅑13 saat yönü 0/24, nesne-nesne temas 0/24) ya kısmi (🅑3 kimlik üçlüsü 5/22); 🅑7 doğrudan ihlal edilmiş ve ⑤ raporu bunu şiddetsiz gözlemlemiş. Bulgu üreten asıl yük (filigran, lockoff, mod V efor) 19.09 kurallarıyla kapanmıyor: ikisi araç ayarı, biri QA/master girdisi. Yeni sınıf adayları: (1) "kamera sabit" cümlesi hareketli aracın içinde, (2) IMG start-frame'i VID'in 0. saniyesinin SONRASINI gösteriyor (S12·S15), (3) prompta "Scene n of 24" + dosya numarası + "Scene 03'le aynı" üç numaralama.
