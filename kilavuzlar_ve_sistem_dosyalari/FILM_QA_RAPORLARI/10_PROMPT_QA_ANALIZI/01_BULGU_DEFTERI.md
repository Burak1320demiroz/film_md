# 📒 BULGU DEFTERİ — makine çıktısı

> ⛔ Bu dosya ELLE YAZILMAZ. Kaynağı:
> `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/prompt_hata_analizi.py --yaz`
> Hüküm sütunu (🅐/🅑/🅒/🅓) burada YOKTUR — o `02_FILM_ANALIZLERI/` içinde,
> prompt metni okunarak verilir. Burada yalnız bulgunun hangi sahneye
> oturduğu yazar.

```
A · tam eşleşen film   34
B · GRID yok           26
C · eşleşmeyen         6
ham rapor (geçerli)    407   · ✂️ KESİK atlanan 6
🔴/🟠 çapalı bulgu     802 → tekil 781
```

## ③ KİMLİK KAPISI

⛔ **Bugün hiçbir film karantinada değil** — hiçbir filmin raporu sayıdan
çıkarılmadı. Künye izleri her filmin başlığında basılı; okuma notu
gerektiren filmler `③ KİMLİK NOTU` satırı taşır.

## KRONOS_SON_SINYAL

`ızgara hook 0 s · klip 10 s · sahne 48 · ham 30/30 geçerli · bulgu 60 → tekil 59`

`③ kimlik: 2/30 güçlü bayrak · üretim defter: ⬜19 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:01 | ① | :01 — 🔴 BLOCKER — Airborne thruster/mechanical rumble audible in space exterior vacuum. |
| S01 | 🔴 | zaman 0:01 | ① | :01 — 🔴 — Dialogue & Audio — Low-frequency engine rumble and exterior ambient sound present in deep space vacuum. |
| S01 | 🟠 | zaman 0:02 | ① | :02 — 🟠 — Scale & Physics — Vented gas plume from station exterior forms turbulent atmospheric cloud instead of linear ballistic expansion in vacuum. |
| S01 | 🟠 | zaman 0:04 | ① | :04 — 🟠 — Particles & Materials — Vented steam particles exhibit atmospheric drag and hanging behavior in space vacuum. |
| S04 | 🔴 | zaman 0:32 | ② | :32 BODY Kestrel 3 Laceration on left cheek present in S2 disappears completely in S4 🔴 |
| S04 | 🟠 | zaman 0:34 | ⑭ | :34 Male right wrist/fingers · twitching He reaches for the clock controls, but his hand hovers between two knobs without turning either. ABANDONED ⑦ 🟠 |
| S04 | 🟠 | zaman 0:30 | ① | :30 — 🟠 MAJOR — Digital timer numbers morph and flicker illegibly on control panel interface. |
| S04 | 🟠 | zaman 0:30 | ① | :30 — 🟠 — Environment — Digital timer panel displays garbled, swimming numbers (" |
| S06 | 🟠 | B2+ 0:59 | ⑧ | :25 Swinging heavy red hatch door Body counter-rotation in zero-g, core bracing against hatch mass ① 🟠 |
| S07 | 🟠 | zaman 1:00 | ① | :00 — 🟠 — Character — Male astronaut suit drifts from full EVA pressurized suit to orange cloth flight jacket without neck ring. |
| S07 | 🟠 | B2+ 1:04 | ⑧ | :30): Moving heavy hatch door fails to affect center of mass or produce body rotation in zero-g<br><br>🟠 -3 · E8 ( |
| S07 | 🟠 | B2+ 1:08 | ⑧ | :34 Closing and locking heavy hatch Shoulder engagement, two-handed torque, bracing ① 🟠 |
| S09 | 🔴 | zaman 1:21 | ① | :21 — 🔴 BLOCKER — Vented gas explosion roaring sound propagation in exterior space vacuum. |
| S09 | 🔴 | zaman 1:21 | ① | :21 — 🔴 — Dialogue & Audio — High-volume gas venting and hull tearing audio present on exterior space station shot in vacuum. |
| S09 | 🟠 | zaman 1:22 | ① | :22 — 🟠 — Scale & Physics — Vented gas from hull breach forms swirling atmospheric eddies in space vacuum. |
| S09 | 🟠 | zaman 1:25 | ② | :25 WORLD N/A 10 Hull exterior shows intact solar module with light smoke in S1, but torn metal hull crater in S9 🟠 |
| S10 | 🟠 | zaman 1:32 | ⑤ | :32 (S10, "POWER SYSTON" typo on control panel wall) 🟠 |
| S11 | 🟠 | zaman 1:42 | ② | :42 BODY Aras 2 White EVA suit with orange harness in S2/S5 turns into orange/brown fabric jacket in S7, then reverts to white suit in S11 🟠 |
| S14 | 🔴 | zaman 2:12 | ② | :12 BODY Kestrel 1 Kestrel's facial bone structure shifts from narrow jaw in S2 to broad square features in S14 🔴 |
| S14 | 🟠 | zaman 2:17 | ⑭ | :17 Male feet/legs · backward slide He steps backward from the console, but his boots skate across the deck plating without stepping weight. SLIDE ③ 🟠 |
| S15 | 🔴 | ≈S-ref — | ⑧ | Recovery Curve Honesty 3/10 🔴 -4 · Reset between Scene 15 ( |
| S16 | 🟠 | B2+ 2:35 | ⑤ | :35 Far 6 Clean "MODULE B" corridor wall stencils in S5 morph into garbled pseudo-text ("NO HB/4004ET") in S10 🟠 Medium |
| S16 | 🟠 | B2+ 2:34 | ⑧ | :00): Pressurized suit gloves display bare-hand fine dexterity with no bulk resistance or stiffness (Pattern ⑥)<br><br>🟠 -3 · E6 ( |
| S17 | 🟠 | B2+ 2:42 | ⑧ | :08 Turning brass pressure valve knob Wrist torque, gloved hand friction effort, slight tremor ⑥ 🟠 |
| S18 | 🔴 | B2+ 2:50 | ③ | :50 · Line 7 ("Kestrel, do you read me?") spoken by Kestrel's female voice on-screen instead of Aras over comms; BLOCKER defect. |
| S18 | 🔴 | B2+ 2:52 | ③ | :52 Kestrel Kestrel UNASSIGNED 🔴 Line spoken by Kestrel's voice identity calling herself "Kestrel" instead of Aras asking over radio |
| S18 | 🟠 | B2+ 2:54 | ⑧ | :20): Heavy mechanical lever pull and holding against explosive blow-out lack rate decay, core bracing, or multi-channel strain<br><br>🟠 -3 · E3 ( |
| S19 | 🟠 | B2+ 3:04 | ⑧ | :30): Zero visible breath change or recovery effort following explosive hull breach and decompression blow-out (Pattern ⑧, ⑩)<br><br>🟠 -3 · E8 ( |
| S19 | 🟠 | B2+ 3:04 | ⑧ | :30): Immediate reset of body posture after severe physical strain without recovery shown (Pattern ③)<br><br>🟠 -3 · E5 ( |
| S19 | 🟠 | B2+ 3:04 | ⑧ | :30): One-handed hold against atmospheric blow-out shows no forearm tremor or re-grip, instantly resetting to relaxed hands (Pattern ⑤)<br><br>🟠 -3 · E2 ( |
| S19 | 🟠 | B2+ 3:04 | ⑧ | :30): Decompression strain vanishes in one beat with no residual guarding or breathlessness (Pattern ⑦)<br><br>🟠 -3 · E8 ( |
| S19 | 🟠 | B2+ 3:04 | ⑧ | :30): Curve drops from 5 to 3 instantly without shown recovery (Pattern ③)<br><br>🟠 -3 · Reset between Scene 11 ( |
| S20 | 🔴 | B2+ 3:14 | ⑤ | :14 Mid 4 Red rigid circular airlock hatch in S4 morphs into metallic wrinkled mylar padded door in S14 🔴 High |
| S23 | 🔴 | B2+ 3:44 | ⑤ | :44 Far 1 Phantom background astronaut figure appears standing in Module A corridor behind Castrel while Aras is trapped outside 🔴 High |
| S24 | 🔴 | ≈S-ref — | ⑧ | Fatigue Accumulation 1/10 🔴 E1–E13 across 24 scenes — character capability in scene 24 is identical to scene 2 |
| S24 | 🔴 | B2+ 3:58 | ⑤ | :58 Far 4 Red hatch opens to Module B corridor in S3, but opens directly to vacuum of space in S18 🔴 High |
| S24 | 🟠 | zaman 3:54 | ⑭ | :54 Female legs/torso · foot glide She walks down the corridor, but her feet slide along the metal deck grid. SLIDE ③ 🟠 |
| S25 | 🟠 | zaman 4:00 | ⑤ | :00 Edge 9 Four-pointed star sparkle watermark icon anchored permanently in bottom-right corner across all 24 shots 🟠 |
| S26 | 🟠 | B2+ 4:12 | ① | :12 — 🟠 — Particles & Materials — Glove material phases through carabiner latch metal geometry during tether attachment. |
| S27 | 🟠 | B2+ 4:25 | ⑭ | :25 Both arms · splays sideways He splays both arms outward in open air to balance himself while floating through the hatch, though no contact surface is touched. PUPPET ⑨ Marionette 🟠 |
| S27 | 🟠 | B2+ 4:28 | ⑭ | :28 Torso · glides vertically She stands on the floor while her torso glides upward relative to the frame without any leg or foot movement. SLIDE ③ Slide 🟠 |
| S28 | 🔴 | B2+ 4:38 | ① | :38 — 🔴 BLOCKER — Duplicate character: second astronaut suit suddenly spawns on right frame edge inside Module A while closing hatch. |
| S28 | 🔴 | B2+ 4:38 | ② | :38 BODY Aras 12 Aras visible behind circular window in red door AND standing in foreground in Module A BLOCKER |
| S29 | 🔴 | B2+ 4:44 | ⑭ | :44 Legs · pedals in air He kicks his legs in a walking cadence while suspended in mid-air to propel himself forward without contacting a wall or rail. SLIDE ③ Slide 🔴 |
| S30 | 🟠 | B2+ 4:52 | ① | :52 — 🟠 — Lighting — Soft AI bloom/haze around helmet visor rim and interior helmet LED indicators. |
| S31 | 🔴 | B2+ 5:00 | ⑤ | :00 Edge 9 Persistent AI generation sparkle logo artifact in lower right corner across all 24 scenes 🔴 High |
| S32 | 🟠 | B2+ 5:14 | ⑭ | :14 Lever & hands · stutters He pulls down the heavy yellow arming lever, but the handle stutters and snaps back upward 2 cm while his hands remain pulling downward. CONTRADICTION ⑧ Contradiction 🟠 |
| S35 | 🟠 | B2+ 5:42 | ① | :42 — 🟠 — Scale & Physics — Steam/gas leak billows in dense atmospheric clouds inside zero-G cabin without microgravity dispersion dynamics. |
| S35 | 🟠 | B2+ 5:44 | ① | :44 — 🟠 — Lighting — Unmotivated volumetric light bloom emanating from hull gas venting without direct light source. |
| S37 | 🟠 | B2+ 6:03 | ① | :03 — 🟠 — Particles & Materials — Glove material deforms and melts around brass valve knob contour during adjustment. |
| S38 | 🟠 | B2+ 6:12 | ① | :12 — 🟠 — Character — Male astronaut suit wardrobe drift; costume changes to orange-shouldered jacket style compared to white EVA suit in adjacent scenes. |
| S39 | 🔴 | B2+ 6:28 | ⑭ | :28 Torso · remains rigid His body remains fixed in a neutral pose without flinching or bracing as explosive hull debris flies past his suit into space. MISREACTION ⑪ Misreaction 🔴 |
| S39 | 🔴 | B2+ 6:20 | ① | :20 — 🔴 BLOCKER — Airborne hull tearing and explosive decompression sound effect played in vacuum space environment. |
| S39 | 🔴 | B2+ 6:20 | ① | :20 — 🔴 — Dialogue & Audio — Airborne hull tearing and explosion sound effects audible in vacuum exterior environment. |
| S39 | 🟠 | B2+ 6:22 | ① | :22 — 🟠 — Particles & Materials — Debris particles venting into space float without directional momentum vector. |
| S39 | 🟠 | B2+ 6:23 | ① | :23 — 🟠 — Scale & Physics — Hull breach debris fragments lack angular momentum and hover like static 2D assets. |
| S39 | 🟠 | B2+ 6:25 | ① | :25 — 🟠 — Environment — Hull wall breach geometry morphs and shifts jagged edges between frames |
| S42 | 🔴 | B2+ 6:53 | ① | :53 — 🔴 BLOCKER — Mechanical hatch disengagement audio propagating through vacuum during Module B separation. |
| S42 | 🔴 | B2+ 6:53 | ① | :53 — 🔴 — Dialogue & Audio — External mechanical detachment sound propagating through vacuum during Module B release. |

## THE_FALLING_WORLD

> ③ **KİMLİK NOTU** — Ham dosyalar kural dışı adlandırılmış (01_KARE_BOLUM_1_2_TEKRAR.md — <FILM>_<MERCEK>_HAM.md değil) ve 15 dosyanın 9'u künyesiz. **Kimlik OKUNDU ve TUTTU:** rapordaki kayış/kemer halkası, gri sandık, gümüş bant, tekerlekli araç, mercekli parlak halka ve iki giysi (beyaz + kobalt omuz / turuncu + siyah) filmin promptlarıyla eşleşiyor — QA modelinin 'buggy · duct tape · eclipse ring' demesi aynı nesnelerin video dilidir. Zaman damgası da tutuyor: promptlar 18.09.2026 14:32, raporlar aynı gün 22:44. Raporlar filmin İLK YARISI (24 sahne · 240 s). ⚠️ ÜRETİM DEFTERİ ESKİ: defter üretimden ÖNCE yazıldı ve dört referans sayfasını hâlâ ⬜ gösteriyor — teslim satırları güncellenmeli.

`ızgara hook 0 s · klip 10 s · sahne 48 · ham 30/30 geçerli · bulgu 58 → tekil 57`

`③ kimlik: 1/30 güçlü bayrak · üretim defter: ⬜268 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:10 | ⑧ | :10 Pulling crewmate out of chasm Forearm grip tension, pull rate decay, leg bracing flex, post-haul torso slump ①, ⑤, ⑧ 🔴 HIGH |
| S02 | 🟠 | zaman 0:22 | ① | :22 — 🟠 MAJOR — Character — Astronaut glove fingers morph and phase into metal belt buckle during pin removal. |
| S03 | 🟠 | zaman 0:30 | ⑧ | :30 Unbuckling pressurized glove tether Stiff suit glove resistance, re-grip effort, reduced dexterity ⑥, ⑬ 🟠 MEDIUM |
| S04 | 🔴 | zaman 0:40 | ⑧ | :40 Sprinting in suit to buggy Heavy shoulder/torso breathing heave, pace decay ②, ⑩ 🔴 HIGH |
| S04 | 🟠 | zaman 0:42 | ⑥ | :42 8 Buggy shadow casts 80° right despite ring eclipse sun being positioned directly dead-ahead in frame 🟠 MAJOR |
| S05 | 🔴 | zaman 0:50 | ① | :50 — 🔴 BLOCKER — Dialogue & Audio: Full airborne acoustic engine roars and impact explosion SFX propagate through exterior atmospheric vacuum. |
| S05 | 🟠 | zaman 0:52 | ① | :52 — 🟠 MAJOR — Lighting — Unmotivated soft AI bloom and dreamy optical haze around the solar eclipse ring and horizon. |
| S05 | 🟠 | zaman 0:54 | ① | :54 — 🟠 MAJOR — Environment — Ground slab hole pops into existence instantly without structural fracturing physics. |
| S05 | 🟠 | zaman 0:54 | ① | :54 — 🟠 MAJOR — Particles & Materials — Dust geysers erupt in rigid geometric cylindrical plumes lacking realistic particle fluid dispersal. |
| S09 | 🔴 | zaman 1:31 | ① | :31 — 🔴 BLOCKER — Scale & Physics: Solid boulder deforms like rubber/foam upon wheel contact and clips directly through the metal wheel rim. |
| S09 | 🔴 | zaman 1:31 | ① | :31 — 🔴 BLOCKER — Scale & Physics — Rock deforms as soft rubber/foam and clips through buggy wheel assembly under compression. |
| S09 | 🔴 | zaman 1:31 | ① | :31 — 🔴 BLOCKER — Motion Quality — Severe temporal jello artifact and geometry warping on buggy wheel rim during rock collision. |
| S09 | 🟠 | zaman 1:32 | ⑥ | :32 3 50 kg rock falling onto tire produces zero suspension compression or vehicle momentum reaction 🟠 MAJOR |
| S10 | 🟠 | zaman 1:44 | ① | :44 — 🟠 MAJOR — Particles & Materials — Rockslide debris floats with artificial 2D card momentum, lacking mass and gravity arc. |
| S11 | 🟠 | zaman 1:50 | ⑧ | :50 Evasive driving through rockfall Upper body bracing, head/neck muscle tension ①, ⑥ 🟠 MEDIUM |
| S12 | 🔴 | zaman 2:04 | ⑧ | :04 Walking to bunker door Winded posture, slow recovery gait after haul & sprint ③, ⑧ 🔴 HIGH |
| S13 | 🔴 | zaman 2:12 | ⑥ | :12 1 Cliff rockfall falls under g ≈ 4.4 m/s² while platform collapse drops under g ≈ 2.2 m/s² with near-zero acceleration 🔴 CRITICAL |
| S13 | 🟠 | zaman 2:12 | ① | :12 — 🟠 MAJOR — Scale & Physics — Collapsing platform and buggy fall with unnaturally floaty gravity acceleration. |
| S13 | 🟠 | zaman 2:10 | ② | :10 WORLD — 8 S12 enters airlock door; S13 cuts to exterior cliff overhang platform. 🟠 |
| S13 | 🟠 | zaman 2:14 | ⑭ | :14 Both suit torsos · static freeze during collapse They watch the catastrophic platform collapse without flinching or bracing for some reason. MISREACTION ⑪ 🟠 |
| S14 | 🟠 | zaman 2:20 | ② | :20 WORLD — 10 S14 shows buggy plunging into abyss; S15 treats entrance as routine hallway walk. 🟠 |
| S17 | 🟠 | zaman 2:50 | ① | :50 — 🟠 MAJOR — Character — Astronaut glove fingers fuse and melt into duct tape roll during wrist sealing. |
| S18 | 🟠 | B2+ 3:00 | ⑮ | :00'da girildi) MISS ⑧ FLEEING INTO DANGER / GOAL DRIFT 🟠 |
| S19 | 🔴 | zaman 3:10 | ① | :10 — 🔴 BLOCKER — Character: Duplicate/third astronaut suddenly materializes on the canyon ledge alongside the established two-person crew. |
| S19 | 🔴 | zaman 3:10 | ① | :10 — 🔴 BLOCKER — Character — Third astronaut figure materializes on canyon ledge, violating two-character suit continuity. |
| S19 | 🔴 | zaman 3:10 | ② | :10 BODY C3 12 S19 ends with 2 astronauts; S20 introduces a 3rd orange-suit astronaut. 🔴 |
| S22 | 🟠 | zaman 3:43 | ⑭ | :43 Orange suit helmet · rotation to blank wall He turns his head fully toward a bare rock surface with nothing there for some reason. SPIN ④ 🟠 |
| S25 | 🔴 | B2+ 4:12 | ⑧ | :12 Holding dangling suit mass on tether line Shoulder dipping, torso rounding, forearm tendon strain ① 🔴 |
| S25 | 🟠 | B2+ 4:12 | ① | :12 — 🟠 MAJOR — Scale & Physics — Collapsing metal bridge structure drops into canyon like lightweight material without structural mass inertia. |
| S25 | 🟠 | B2+ 4:16 | ① | :16 — 🟠 MAJOR — Particles & Materials — Dust clouds from canyon edge collapse expand as low-density volumetric haze rather than ballistically falling dust/rock particles. |
| S26 | 🟠 | B2+ 4:26 | ① | :26 — 🟠 MAJOR — Particles & Materials — Loose rock and dust trickling down cliff face phase directly through astronaut suit shoulder material without physical collision. |
| S27 | 🟠 | B2+ 4:32 | ⑧ | :32 Climbing rock wall during crumble Rate decay on pulls, foot slipping, bodyweight sag ② 🟠 |
| S29 | 🔴 | B2+ 4:52 | ⑧ | :52 Wrist-to-wrist bodyweight hold over cliff Asymmetric shoulder drop, forearm muscle quiver, re-gripping ⑤ / ⑨ 🔴 |
| S30 | 🟠 | B2+ 5:00 | ① | :00 — 🟠 MAJOR — Lighting — Key light direction flips between wide lander shot and cliff shots relative to the eclipse position in background sky. |
| S30 | 🟠 | B2+ 5:04 | ① | :04 — 🟠 MAJOR — Particles & Materials — Dust kicked up by walking astronauts floats without gravity weight, remaining suspended in thin atmosphere. |
| S31 | 🟠 | B2+ 5:10 | ② | :10 BODY C2 4 Yellow rope tied in knot around rail (S1) vs snap-carabiner clip on anchor (S8) 🟠 |
| S32 | 🔴 | B2+ 5:26 | ⑭ | :26 Gövde/Baş · dönüş Sağ tarafa 90° döner — hedefte hiçbir nesne veya uyarılma yoktur SPIN ④ 🔴 |
| S32 | 🟠 | B2+ 5:20 | ② | :20 WORLD N/A 8 Lander parked on dirt soil (S7) changes to engineered metal platform (S9) 🟠 |
| S32 | 🟠 | B2+ 5:22 | ⑭ | :22 Bacaklar · adımlama Düz zeminde yürür — adımları ilerleme hızıyla eşleşmez ve kayar SLIDE ③ 🟠 |
| S33 | 🟠 | B2+ 5:30 | ① | :30 — 🟠 MAJOR — Metal panel surface texture breathes and swims while the gloved hand operates the hatch latch mechanism. |
| S33 | 🟠 | B2+ 5:30 | ① | :30 — 🟠 MAJOR — Environment — Surface metal plating on machine panel swims/morphs under hand pressure during lever operation. |
| S33 | 🟠 | B2+ 5:32 | ⑧ | :32 Peeling back bent structural metal sheet Bracing stance, shoulder engagement, rate slowing during peel ① 🟠 |
| S35 | 🔴 | B2+ 5:56 | ① | :56 — 🔴 BLOCKER — Catwalk grating collapses beneath astronaut, causing the figure to float/glide unnaturally without realistic gravity acceleration or drop momentum. |
| S35 | 🔴 | B2+ 5:56 | ① | :56 — 🔴 BLOCKER — Scale & Physics — Astronaut falls through collapsed catwalk section with zero-G glide physics instead of gravity acceleration. |
| S35 | 🟠 | B2+ 5:50 | ② | :50 WORLD N/A 10 Metal catwalk floor grating intact (S9) breaks open (S12) and resets intact (S21) 🟠 |
| S35 | 🟠 | B2+ 5:52 | ⑧ | :52 Shock drop through grating onto tether Sudden recoil wince, limb guarding, body distortion on line catch ⑦ 🟠 |
| S37 | 🟠 | B2+ 6:10 | ① | :10 — 🟠 MAJOR — Environment — Background gas giant ring geometry changes scale and tilt angle compared to earlier wide exterior shots. |
| S37 | 🟠 | B2+ 6:10 | ② | :10 WORLD N/A 9 Celestial background shifts from red desert eclipse (S2) to orbital planet view (S14) 🟠 |
| S37 | 🟠 | B2+ 6:12 | ⑧ | :12 Sheer vertical hull climb Forearm tremor, foot friction slipping, climbing speed decay ② 🟠 |
| S40 | 🟠 | B2+ 6:40 | ① | :40 — 🟠 MAJOR — Hand contact morphing and finger fusion when the orange-suited astronaut grabs the white suit wrist during the rescue pull. |
| S40 | 🟠 | B2+ 6:40 | ① | :40 — 🟠 MAJOR — Character — Glove fingers phase and fuse into sleeve fabric during two-person wrist grab. |
| S40 | 🟠 | B2+ 6:45 | ① | :45 — 🟠 MAJOR — Motion Quality — Temporal warping/jello effect on arm pulling motion during airlock entrance rescue. |
| S41 | 🟠 | B2+ 6:52 | ⑧ | :52 Operating precise toggle controls post-climb Fine motor hand tremor, delayed finger placement ⑬ 🟠 |
| S42 | 🟠 | B2+ 7:01 | ① | :01 — 🟠 MAJOR — Character — Astronaut face inside helmet appears noticeably airbrushed/waxy with lost skin pore texture compared to real photoreal footage. |
| S42 | 🟠 | B2+ 7:00 | ② | :00 BODY C1 1 Reflective opaque visor (S3) turns completely transparent displaying face (S19) 🟠 |
| S44 | 🟠 | B2+ 7:21 | ① | :21 — 🟠 MAJOR — Scale & Physics — Lander engine thruster blast creates flat 2D-like floor tile tearing without mass-consistent debris arcs or structural resistance. |
| S44 | 🟠 | B2+ 7:22 | ① | :22 — 🟠 MAJOR — Particles & Materials — Thruster exhaust dust spray lacks momentum density and dissipates like CG particle fog. |

## THE_FROST_LINE

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 13/13 geçerli · bulgu 55 → tekil 51`

`③ kimlik: 9/13 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🔴 | zaman 0:00 | ① | :00 — 🔴 BLOCKER — On-screen watermark. A static blue triangle logo is burned into the bottom right corner of the frame throughout the entire video. |
| S00 | 🟠 | zaman 0:00 | ① | :00 — 🟠 MAJOR — Particles & Materials — The high-pressure geyser eruption falls straight down like heavy salt, lacking gaseous dispersion. |
| S01 | 🔴 | zaman 0:09 | ① | :09 — 🔴 BLOCKER — Scale & Physics — The escaping pressure plume falls straight down heavily like dense salt or sand instead of dispersing like pressurized gas in a thin atmosphere. |
| S01 | 🟠 | zaman 0:10 | ① | :10 — 🟠 MAJOR — Lighting — Unmotivated fill light inside the helmet illuminates the face brightly from the front despite harsh exterior sunlight from behind/side. |
| S02 | 🔴 | zaman 0:20 | ② | :20 Body Astronaut 3 Forearms and knees heavily frosted vs clean grey suit. 🔴 BLOCKER |
| S02 | 🔴 | zaman 0:21 | ⑥ | :21 1 Vent gas falls >1g vs jog hang time <0.4g. 🔴 BLOCKER |
| S02 | 🔴 | zaman 0:21 | ⑥ | :21 1 Venting gas falls at >1g (Earth-normal or heavier), while the astronaut's jog exhibits a <0.4g (Martian) hang time. 🔴 BLOCKER |
| S02 | 🟠 | zaman 0:19 | ② | :19 (S3) BODY Astronaut 4 Astronaut holds a brush in S2; hands are totally empty in S3. 🟠 MAJOR |
| S03 | 🟠 | zaman 0:29 | ① | :29 — 🟠 MAJOR — Motion Quality — The running animation feels like slow-motion gliding ("moonwalking"); footsteps lack planted weight and contact with the dirt. |
| S04 | 🟠 | zaman 0:40 | ② | :40 Body Astronaut 5 Reaches toward leak with left hand vs right hand presses patch in close-up. 🟠 MAJOR |
| S04 | 🟠 | zaman 0:39 | ① | :39 — 🟠 MAJOR — Particles & Materials — Gas spraying from the tear renders as solid white static lines rather than dispersing particulate matter. |
| S04 | 🟠 | zaman 0:39 | ① | :39 — 🟠 MAJOR — Lighting — AI Bloom is highly visible on the white spray emitting from the leak, giving it a soft, dreamy haze. |
| S05 | 🔴 | zaman 0:49 | ① | :49 — 🔴 BLOCKER — Hand-surface fusion; the astronaut's fingers merge and phase completely into the greenhouse hull when pressing the patch. |
| S05 | 🔴 | zaman 0:49 | ① | :49 — 🔴 BLOCKER — Particles & Materials — The rigid/tensile material of the pressurized greenhouse acts like soft dough or snow when the astronaut presses the patch into it. |
| S05 | 🟠 | zaman 0:50 | ② | :50 (S6) BODY Astronaut 2 Thick black back harness appears in S6, absent in S2. 🟠 MAJOR |
| S05 | 🟠 | zaman 0:50 | ② | :50 World N/A 10 Patch is a small grey rectangle vs patch is a massive white/black strip. 🟠 MAJOR |
| S06 | 🟠 | zaman 1:00 | ② | :00 (S7) WORLD N/A 13 The square patch is meticulously applied in S6, but the structure instantly fails and collapses anyway in S7. 🟠 MAJOR |
| S06 | 🟠 | zaman 1:00 | ① | :00 — 🟠 MAJOR — Scale & Physics — The deflated greenhouse collapses like a soft bedsheet, lacking the structural stiffness expected of a thick pressurized polymer. |
| S06 | 🟠 | zaman 1:00 | ③ | :00 SFX Sync 7 The visual shows a massive pressurized structure collapsing; the sound effect is a light fabric rustle lacking low-end weight or structural tearing. 🟠 MAJOR |
| S07 | 🟠 | zaman 1:09 | ① | :09 — 🟠 MAJOR — Environment — Texture swimming. The square black patches and panel lines on the exterior of the greenhouse change completely between the establishing shot and this cut. |
| S07 | 🟠 | zaman 1:09 | ① | :09 — 🟠 MAJOR — Scale & Physics — The greenhouse structure is instantly deflated and crushed, behaving like a thin bedsheet rather than a pressurized hull. |
| S08 | 🔴 | zaman 1:19 | ② | :19 (S9) WORLD N/A 8 The greenhouse completely collapses flat in S7. In S9, the interior is perfectly arched, rigid, and deeply pressurized. 🔴 BLOCKER |
| S08 | 🔴 | zaman 1:20 | ② | :20 World N/A 11 Greenhouse exterior is massively deflated/crushed vs interior is fully pressurized and geometrically perfect. 🔴 BLOCKER |
| S08 | 🔴 | zaman 1:20 | ① | :20 — 🔴 BLOCKER — Character — Visor persistence failure. Helmet glass appears absent (perfectly clear face), then abruptly catches heavy reflections at |
| S08 | 🟠 | zaman 1:19 | ① | :19 — 🟠 MAJOR — Lighting — AI Bloom is present inside the greenhouse, creating a soft, diffuse, dreamy haze. |
| S08 | 🟠 | zaman 1:19 | ① | :19 — 🟠 MAJOR — Motion Quality — Floaty, weightless running motion continues despite the character wearing a heavy suit. |
| S09 | 🔴 | zaman 1:30 | ① | :30 — 🔴 BLOCKER — Texture swimming. The tomato plants and leaves continuously morph, swim, and change geometry as the character walks past them. |
| S09 | 🔴 | zaman 1:30 | ① | :30 — 🔴 BLOCKER — Environment — Texture swimming. Plants and tomatoes morph and shift positions on their vines. (Largest background object: greenhouse walls, full frame). |
| S09 | 🟠 | zaman 1:30 | ② | :30 Body Astronaut 4 Holding roll of tape in right hand vs hands completely empty. 🟠 MAJOR |
| S09 | 🟠 | zaman 1:29 | ① | :29 — 🟠 MAJOR — Particles & Materials — Object phasing. The roll of tape held by the astronaut clips straight through the gloves. |
| S10 | 🔴 | zaman 1:47 | ① | :47 — 🔴 BLOCKER — Character — Hidden cut / Morph inside a single clip. Hands morph and glitch into each other during the clap. |
| S10 | 🟠 | zaman 1:39 | ⑤ | :39 (S10) Midground 6 Texture swimming: The tomato plants and leaves continuously morph, appear, and shift geometry behind the walking subject. 🟠 MAJOR |
| S10 | 🟠 | zaman 1:39 | ⑥ | :39 6 Exterior greenhouse height (~3m) contradicts interior aisle height (~4.5m). 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ② | :50 (S12) BODY Astronaut 3 Glove and suit are heavily dusted with red soil in S5, pristine clean in S12. 🟠 MAJOR |
| S12 | 🟠 | zaman 2:05 | ⑥ | :05 4 Hull yields like soft dough externally, rigid internally. 🟠 MAJOR |
| S12 | 🟠 | zaman 2:05 | ⑥ | :05 4 Greenhouse hull yields like soft, unpressurized dough when patched, but supports rigid internal rigging and tensioned screens later. 🟠 MAJOR |
| S13 | 🟠 | zaman 2:10 | ② | :10 Body Astronaut 2 Flat back with no pack vs large grey backpack/life-support unit present. 🟠 MAJOR |
| S14 | 🔴 | zaman 2:28 | ① | :28 — 🔴 BLOCKER — Severe hand geometry breakdown and extra fingers sprout when the glove touches the plant leaf. |
| S14 | 🔴 | zaman 2:28 | ① | :28 — 🔴 BLOCKER — Character — Contact morphing. Extra fingers appear, glove geometry completely breaks down while touching the plant leaf. |
| S19 | 🟠 | zaman 3:15 | ① | :15 — 🟠 MAJOR — Scale & Physics — The metal bar in the doorway bends flexibly like rubber as the character pushes forward. |
| S20 | 🔴 | zaman 3:23 | ① | :23 — 🔴 BLOCKER — Object phasing. Character touches his helmet and his gloved fingers phase directly through the solid glass/helmet rim. |
| S20 | 🔴 | zaman 3:23 | ① | :23 — 🔴 BLOCKER — Character — Contact morphing. Fingers phase through the solid helmet visor. |
| S21 | 🟠 | zaman 3:30 | ② | :30 (S22) BODY Astronaut 3 Glove is coated in white frost in S21, clean in S22. 🟠 MAJOR |
| S21 | 🟠 | zaman 3:30 | ② | :30 (S22) WORLD N/A 10 Frost heavily accumulates on the plant leaves in S17, but the soil bed in S22 shows fresh, unfrosted green sprouts. 🟠 MAJOR |
| S22 | 🔴 | zaman 3:39 | ⑤ | :39 (S23) Edge 9 A static blue triangle watermark sits in the bottom right corner of every scene in the film. 🔴 BLOCKER |
| S22 | 🔴 | zaman 3:39 | ② | :39 (S23) WORLD N/A 11 The deflated greenhouse in S7 is suddenly covered by a massive, perfectly draped grey thermal tarp in S23 with no on-screen deployment. 🔴 BLOCKER |
| S22 | 🟠 | zaman 3:39 | ⑤ | :39 (S23) Far Field 6 Set architecture drift: S1 shows a habitat hub with three cylinder wings. S23 shows a hub with a large satellite dish and different wing placements. The lander also changes leg designs. 🟠 MAJOR |
| S22 | 🟠 | zaman 3:40 | ⑤ | :40 Far 6 The white habitat module behind the greenhouse sits on the left in S1, but has migrated to the center-left in S23. Its shape (number of attached nodes) also changes completely between the two wide exterior shots. 🟠 MAJOR |
| S22 | 🟠 | zaman 3:39 | ② | :39 (S23) WORLD N/A 9 Shadow direction on the habitat structures flips roughly 180 degrees between S1 and S23. 🟠 MAJOR |
| S23 | 🔴 | zaman 3:50 | ① | :50 — 🔴 BLOCKER — A static cyan triangle watermark/logo is visible in the bottom right corner of every single frame. |
| S23 | 🟠 | zaman 3:49 | ① | :49 — 🟠 MAJOR — Environment — The background base structures (solar panels, habitat modules) shift positions and shapes entirely compared to the establishing shot at |

## SUSMAYAN_NOBETCI

`ızgara hook 0 s · klip 10 s · sahne 48 · ham 29/30 geçerli · bulgu 45 → tekil 44`

`③ kimlik: 2/30 güçlü bayrak · üretim defter: ⬜302 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🔴 | zaman 0:04 | ① | :04 — 🔴 BLOCKER — Explosive acoustic boom audible in space vacuum during craft separation. |
| S00 | 🔴 | zaman 0:04 | ① | :04 — 🔴 BLOCKER — Dialogue & Audio — Acoustic explosion sound carrying through space vacuum. |
| S00 | 🟠 | zaman 0:03 | ⑭ | :03 Sağ el / gövde Mekik camın önünde patlarken pilot gövdesi ve eli tepkisiz kalır. MISREACTION ⑪ 🟠 |
| S00 | 🟠 | zaman 0:04 | ① | :04 — 🟠 MAJOR — Particles & Materials — Debris spray behaves like planar 2D particle layer without 3D rotation. |
| S01 | 🔴 | zaman 0:14 | ⑧ | :14 Flipping toggle switch near helmet visor Resistance from pressurized sleeve joint, glove crease tension, micro-bracing ⑥ 🔴 High |
| S01 | 🟠 | zaman 0:16 | ① | :16 — 🟠 MAJOR — Lighting & Color — Soft dreamy AI bloom around helmet spotlight emitters. |
| S04 | 🟠 | zaman 0:43 | ⑭ | :43 Sol el CRT ekran yüzeyinde şiddetli kıvılcım/patlama olurken el çerçevede sabit durur. MISREACTION ⑪ 🟠 |
| S05 | 🟠 | zaman 0:50 | ① | :50 — 🟠 MAJOR — Camera — Rotating ring station exhibits perspective scale warping relative to horizon. |
| S06 | 🔴 | zaman 1:00 | ⑧ | :00 Opening hatch cover and pulling mechanical panel lever Forearm muscle flex, wrist tightening, slight shoulder engagement against lever force ① 🔴 High |
| S07 | 🔴 | zaman 1:10 | ① | :10 — 🔴 BLOCKER — Dialogue & Audio — Thruster combustion roar audible in vacuum. |
| S08 | 🟠 | B2+ 1:24 | ⑧ | :50 Pulling heavy metal hatch door closed Shoulder rounding, torso lean, rate decay before latch engagement ① Effortless heavy 🟠 High |
| S10 | 🔴 | zaman 1:40 | ② | :40 BODY Pilot 2 White pressure suit toggles to dark tactical suit 🔴 CRITICAL |
| S10 | 🔴 | zaman 1:40 | ⑧ | :40 Flipping dial/switch on console Fine motor effort against stiff glove material, hand tremor or micro-adjustment ⑥ 🔴 High |
| S10 | 🟠 | zaman 1:40 | ② | :40 WORLD — 8 Cockpit console panel layout changes from grey metal to dark padded panel 🟠 MAJOR |
| S11 | 🟠 | zaman 1:52 | ① | :52 — 🟠 MAJOR — Scale & Physics — Decoupled hull plate floats without angular momentum or rotational drift. |
| S12 | 🔴 | zaman 2:00 | ⑧ | :00 Gripping flight joystick and toggling switch Forearm grip tension, glove deformation under pressure ⑤ 🔴 High |
| S14 | 🔴 | zaman 2:20 | ⑧ | :20 Holding flight joystick during maneuver Posture bracing against vehicle movement, grip adjustment ① 🔴 High |
| S15 | 🔴 | zaman 2:33 | ① | :33 — 🔴 BLOCKER — Main engine explosion sound carrying airborne acoustic roar in vacuum. |
| S15 | 🔴 | zaman 2:33 | ① | :33 — 🔴 BLOCKER — Dialogue & Audio — Engine blast explosion produces full acoustic shockwave audio in space. |
| S15 | 🟠 | zaman 2:34 | ① | :34 — 🟠 MAJOR — Particles & Materials — Low-density spark spray lacking physical mass/inertia. |
| S16 | 🟠 | zaman 2:42 | ① | :42 — 🟠 MAJOR — Environment & World — Structure breach geometry shifts edges between wide and close cuts. |
| S16 | 🟠 | zaman 2:40 | ⑤ | :40 far 5 Surface texture scale disagrees across identical distances 🟠 |
| S17 | 🔴 | zaman 2:50 | ⑧ | :50 Pulling heavy main control lever Torso lean, shoulder rounding, visible helmet breath fogging under effort ① 🔴 High |
| S19 | 🟠 | zaman 3:12 | ① | :12 — 🟠 MAJOR — Hanging lamps inside porthole windows sway in 1G pendulum motion despite orbital zero-G. |
| S19 | 🟠 | zaman 3:10 | ① | :10 — 🟠 MAJOR — Lighting & Color — Unmotivated atmospheric haze halo around exterior module portholes. |
| S19 | 🟠 | zaman 3:12 | ① | :12 — 🟠 MAJOR — Scale & Physics — Lantern lamps inside windows show gravitational hanging sway in zero-G. |
| S20 | 🔴 | zaman 3:23 | ① | :23 — 🔴 BLOCKER — Dialogue & Audio — Heavy metallic latch impact sound propagating through vacuum. |
| S21 | 🔴 | zaman 3:30 | ⑤ | :30 edge 9 Persistent four-point star artifact at lower right corner 🔴 |
| S21 | 🟠 | B2+ 3:38 | ⑥ | :50 3 Hard mechanical docking and prybar leverage produce no mass reaction or body recoil vs conservation of momentum 🟠 |
| S24 | 🔴 | B2+ 4:03 | ① | :03 — 🔴 BLOCKER — Airborne thruster audio present in hard vacuum exterior space shot. |
| S25 | 🟠 | B2+ 4:18 | ⑥ | :30 5 Explosion debris decelerates in space vacuum ($a \approx -1.2 \text{ m/s}^2$) vs ballistic constant velocity ($v = \text{const}$) in vacuum 🟠 |
| S27 | 🟠 | B2+ 4:35 | ① | :35 — 🟠 MAJOR — Lighting & Color — AI bloom haze on module windows without physical light source motivation. |
| S30 | 🔴 | B2+ 5:04 | ① | :04 — 🔴 BLOCKER — Module separation in hard vacuum produces loud acoustic collision and debris sound effects. |
| S30 | 🔴 | B2+ 5:04 | ① | :04 — 🔴 BLOCKER — Dialogue & Audio — Airborne metallic collision SFX in vacuum during module separation. |
| S31 | 🟠 | B2+ 5:14 | ① | :14 — 🟠 MAJOR — Scale & Physics — Floating paper tape abruptly stops linear momentum in microgravity. |
| S33 | 🟠 | B2+ 5:32 | ① | :32 — 🟠 MAJOR — Environment & World — Metal plating texture on damaged cylinder swims and morphs during rotation. |
| S34 | 🔴 | B2+ 5:43 | ③ | :43 Voice Identity Speaker Attribution Female voice speaks line; identical phrase repeated by unassigned male voice 🔴 BLOCKER |
| S35 | 🟠 | B2+ 5:52 | ② | :52 WORLD N/A 3 / 10 Target module hull has a severe structural rupture in S10, but appears completely smooth and undamaged in S12 🟠 MAJOR |
| S39 | 🟠 | B2+ 6:33 | ① | :33 — 🟠 MAJOR — Particles & Materials — Vented fluid stream freezes into rigid repeating bead structures with zero momentum drift. |
| S41 | 🟠 | B2+ 6:54 | ① | :54 — 🟠 MAJOR — Character Consistency — Gloved hand fingers morph and clip into crowbar metal handle. |
| S42 | 🟠 | B2+ 7:02 | ① | :02 — 🟠 MAJOR — Particles & Materials — Ice crystals venting from EVA hatch form flat, static 2D particle planes. |
| S45 | 🔴 | B2+ 7:33 | ① | :33 — 🔴 BLOCKER — Spacecraft explosion in vacuum generates atmospheric billowy fire/smoke cloud and loud explosion audio. |
| S45 | 🔴 | B2+ 7:33 | ① | :33 — 🔴 BLOCKER — Scale & Physics — Spacecraft explosion in vacuum exhibits atmospheric smoke expansion dynamics. |
| S45 | 🔴 | B2+ 7:33 | ① | :33 — 🔴 BLOCKER — Dialogue & Audio — Loud atmospheric explosion audio playing in vacuum shot. |

## BENI_HATIRLAMA

`ızgara hook 10 s · klip 10 s · sahne 48 · ham 18/18 geçerli · bulgu 42 → tekil 42`

`③ kimlik: 11/18 güçlü bayrak · üretim defter: ⬜304 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🔴 | hook⟂ 0:09 | ⑧ | :09 Kneeling in pressurized EVA suit Torso/leg suit resistance, weight settling into joint seals Pattern ⑥ 🔴 |
| S03 | 🟠 | zaman 0:43 | ① | :43 — 🟠 MAJOR — Character Consistency — Yellow scarf clips through chest pocket suit fabric during removal movement. |
| S03 | 🟠 | zaman 0:45 | ② | :45 BODY Woman / Astronaut 4 Woman wears yellow scarf on neck in S1; Astronaut pulls duplicate yellow scarf from chest pocket in S5 🟠 MAJOR |
| S04 | 🔴 | zaman 0:59 | ⑧ | :59 Unfolding fine knitted scarf with thick gloves Glove stiffness, lack of tactile feedback, awkward finger spread Pattern ⑥ 🔴 |
| S04 | 🟠 | zaman 0:52 | ① | :52 — 🟠 MAJOR — Motion Quality — Astronaut's boots slide along black sand before planting weight during stride. |
| S05 | 🔴 | zaman 1:09 | ⑧ | :09 Bending & dressing creature in scarf Suit joint resistance, lumbar strain, visor breath fogging Pattern ⑥, ⑩ 🔴 |
| S07 | 🟠 | zaman 1:20 | ⑤ | :20 Far Field 4 Ceiling topology in S1 is closed rock vault; S9 introduces open ceiling chasm to sky 🟠 |
| S08 | 🟠 | zaman 1:30 | ⑥ | :30 6 Scarf is a 1.2 m narrow neck fabric in L6 but becomes a full-body garment covering 1.0 m creature in L10 🟠 |
| S09 | 🟠 | zaman 1:40 | ① | :40 — 🟠 MAJOR — Lighting & Color — Sudden shift to false-color thermal palette without transition or optical justification. |
| S10 | 🔴 | zaman 1:59 | ⑧ | :59 Operating tiny device dial with heavy glove Finger tremor, glove resistance, clumsy contact area Pattern ⑥, ⑬ 🔴 |
| S10 | 🟠 | zaman 1:52 | ① | :52 — 🟠 MAJOR — Scale & Physics: Transparent character legs phase directly through the Tardigrade/seal-like creature without physical weight deformation or collision. |
| S10 | 🟠 | zaman 1:50 | ① | :50 — 🟠 MAJOR — Creatures: Creature slides laterally across sand dune without leg articulation or ground friction planting. |
| S10 | 🟠 | zaman 1:50 | ① | :50 — 🟠 MAJOR — Creatures — Creature slides across terrain surface without limb movement or dune displacement. |
| S10 | 🟠 | zaman 1:52 | ① | :52 — 🟠 MAJOR — Scale & Physics — Character geometry overlays creature body with zero collision or weight response. |
| S14 | 🟠 | zaman 2:32 | ① | :32 — 🟠 MAJOR — Creatures / Character: Female character's fingers melt and fuse with glowing surface patches on the creature during contact petting. |
| S14 | 🟠 | zaman 2:32 | ① | :32 — 🟠 MAJOR — Character Consistency — Hand structure breaks down and merges into bioluminescent skin texture. |
| S14 | 🟠 | zaman 2:35 | ② | :35 WORLD — 10 Wide shot S13 shows clear sand plain between subjects; S16 introduces a large seal-like creature on the same patch of sand without arrival 🟠 MAJOR |
| S15 | 🔴 | zaman 2:44 | ⑥ | :44 1 Cave sand falls at $g \approx 1.11 \text{ m/s}^2$ while wall climbing dust falls at $g \approx 2.48 \text{ m/s}^2$ (2.2x increase) 🔴 |
| S15 | 🔴 | zaman 2:49 | ⑧ | :49 Vertical rock chimney climbing in full suit Forearm grip flex, heavy leg push effort, visor fogging, rate decay Pattern ①, ⑤, ⑥ 🔴 |
| S15 | 🟠 | zaman 2:46 | ① | :46 — 🟠 MAJOR — Motion Quality — Astronaut turns on heel with moonwalk-style pivot glide. |
| S16 | 🔴 | zaman 2:59 | ⑧ | :59 Trekking through loose volcanic sand under storm Deep foot sinking, wind bracing lean, gait asymmetry, rate decay Pattern ①, ⑥, ⑫ 🔴 |
| S16 | 🟠 | zaman 2:51 | ⑭ | :51 Legs & Feet · step forward He steps toward the rover—his boots slide across sand like skating. SLIDE ③ 🟠 |
| S16 | 🟠 | zaman 2:53 | ① | :53 — 🟠 MAJOR — Character Consistency — Astronaut's glove digits warp and elongate while reaching toward small prop. |
| S16 | 🟠 | zaman 2:55 | ① | :55 — 🟠 MAJOR — Scale & Physics — Small floating capsule moves across frame without thruster plume or mass momentum. |
| S17 | 🟠 | zaman 3:05 | ② | :05 BODY Astronaut 2 Blue suit armband is on right upper arm in S13/S17, but mirrored onto left upper arm in S19/S20 🟠 MAJOR |
| S17 | 🟠 | zaman 3:05 | ② | :05 WORLD — 10 Seal creature resting on sand in S16/S18 completely vanishes from the open plain in S19 🟠 MAJOR |
| S17 | 🟠 | zaman 3:09 | ⑧ | :09 Mounting exterior platform rail in wind Forearm strain, suit center-of-mass shift, wind displacement Pattern ⑤, ⑥ 🟠 |
| S20 | 🔴 | zaman 3:39 | ⑤ | :39 N/A Edges 9 Static four-pointed sparkle watermark icon burned into bottom-right corner across all shots 🔴 |
| S20 | 🔴 | zaman 3:31 | ⑥ | :31 1 Cave fissure cascade falls at $g \approx 1.13 \text{ m/s}^2$ while exterior cliff sand falls at $g \approx 0.39 \text{ m/s}^2$ (2.9x decrease) 🔴 |
| S26 | 🔴 | B3+ 4:34 | ① | :34 — 🔴 BLOCKER — Hand contact morphing: gloved fingers merge and lose structural integrity while touching glowing spots on creature skin. |
| S26 | 🔴 | B3+ 4:34 | ① | :34 — 🔴 BLOCKER — Character — Gloved fingers fuse and deform into creature skin texture during contact close-up. |
| S28 | 🟠 | B3+ 4:58 | ① | :58 — 🟠 MAJOR — Non-physical garment interaction: astronaut wraps a heavy knit scarf around his helmet collar seal without clearing suit geometry. |
| S28 | 🟠 | B3+ 4:58 | ① | :58 — 🟠 MAJOR — Character — Scarf wrapping motion clips through suit helmet ring interface. |
| S28 | 🟠 | B3+ 4:55 | ② | :55 BODY Woman / Astronaut 2 Scarf is on woman's neck in S5, inside astronaut's hands/helmet in S6 🟠 |
| S31 | 🟠 | B3+ 5:23 | ① | :23 — 🟠 MAJOR — Lighting — AI bloom and soft unmotivated light halo surrounding root network in cavern background. |
| S34 | 🔴 | B3+ 5:55 | ② | :55 BODY Astronaut 1 Facial structure shifts from older wide jaw (S6) to sharper features (S12) 🔴 |
| S34 | 🟠 | B3+ 5:55 | ② | :55 BODY Astronaut 4 Puck device missing from hands in S11, appears held in S12 🟠 |
| S35 | 🟠 | B3+ 6:02 | ① | :02 — 🟠 MAJOR — Character — Secondary female character transitions to transparent ghosting/hologram artifact without light source origin. |
| S37 | 🔴 | B3+ 6:22 | ① | :22 — 🔴 BLOCKER — Severe creature morphology shift: seal-like organism suddenly sprouts six arthropod/tardigrade-like legs on its lower body. |
| S37 | 🔴 | B3+ 6:22 | ① | :22 — 🔴 BLOCKER — Creatures — Sudden anatomical mutation; creature gains multiple jointed legs not present in earlier scenes. |
| S40 | 🟠 | B3+ 6:54 | ① | :54 — 🟠 MAJOR — Particles & Materials — Sand particles drifting across terrain freeze mid-air and drag with camera motion. |
| S40 | 🟠 | B3+ 6:55 | ② | :55 WORLD N/A 8 Astronaut climbing interior cave wall cuts to flat exterior plain 🟠 |

## LOOK_UP

`ızgara hook 0 s · klip 10 s · sahne 12 · ham 12/12 geçerli · bulgu 37 → tekil 37`

`③ kimlik: 8/12 güçlü bayrak · üretim defter: ⬜19 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:06 | ① | :06 — 🔴 — Creatures — Alien limbs slide across ceiling grating without physical contact points. |
| S01 | 🟠 | zaman 0:09 | ⑧ | :09 Pushing comrade in microgravity Torso bracing & counter-push against inertia ① EFFORTLESS HEAVY 🟠 |
| S01 | 🟠 | zaman 0:02 | ① | :02 — 🟠 — Character — Helmet stripe geometry shifts mid-sequence from double lines to single thick band. |
| S01 | 🟠 | zaman 0:07 | ① | :07 — 🟠 — Camera — Spatial warping on background console panels during camera pan. |
| S02 | 🔴 | zaman 0:10 | ⑭ | :10 legs · kicking empty air He kicks his legs to propel himself, but his body floats on a separate trajectory. PUPPET ⑨ 🔴 |
| S02 | 🔴 | zaman 0:15 | ⑭ | :15 arms · firing rifle He shoots his weapon at the corridor wall — I do not know why; nothing is there. MISREACTION ⑪ 🔴 |
| S02 | 🔴 | zaman 0:11 | ① | :11 — 🔴 — Contradictory gravity physics where crew members float while others walk upright on the floor without magnetic boot indicators. |
| S02 | 🔴 | zaman 0:11 | ① | :11 — 🔴 — Scale & Physics — Inconsistent gravity vectors with simultaneous zero-g floating and grounded walking. |
| S02 | 🔴 | zaman 0:12 | ① | :12 — 🔴 — Motion Quality — Severe jello distortion and temporal warping on floating body physics. |
| S02 | 🟠 | zaman 0:18 | ⑦ | :18 Exact spatial position of the target being fired at down the corridor ⑦ GEOGRAPHY TELEPORT 🟠 Medium |
| S02 | 🟠 | zaman 0:10 | ② | :10 BODY C1 2 Black striped helmet in S1 becomes clear dome helmet in S4 🟠 |
| S02 | 🟠 | zaman 0:17 | ① | :17 — 🟠 — Lighting — Muzzle flash lacks dynamic directional light casting on nearby surfaces. |
| S03 | 🔴 | zaman 0:21 | ① | :21 — 🔴 — Character — Duplicate background crew member spawns near door frame. |
| S03 | 🟠 | zaman 0:28 | ① | :28 — 🟠 — Environment — Hatch vent opening dimensions warp wide to narrow between angles. |
| S04 | 🔴 | zaman 0:35 | ⑥ | :35 Gravity & Free Fall Alien ceiling drop implies g ≈ 1.73 m/s² whereas debris drop implies g ≈ 6.67 m/s² in the same deck module 🔴 |
| S04 | 🟠 | zaman 0:30 | ⑭ | :30 hand · cable bar grab He reaches to pull the tether line, but his gloved hand passes through the metal handle. MISGRIP ⑥ 🟠 |
| S04 | 🟠 | zaman 0:35 | ① | :35 — 🟠 — Particles — Muzzle smoke and ejecta particles float in flat planes without real ballistics. |
| S05 | 🔴 | zaman 0:40 | ⑭ | :40 hands · grasping air He reaches to fight off the creature, but his hands close on empty air 10 cm away from it. PHANTOM ⑤ 🔴 |
| S05 | 🔴 | zaman 0:42 | ① | :42 — 🔴 — Hand-surface fusion and finger morphing during high-tension grip on metal harness. |
| S05 | 🔴 | zaman 0:43 | ① | :43 — 🔴 — Creature geometry clipping directly through astronaut torso armor and helmet collar. |
| S05 | 🔴 | zaman 0:42 | ① | :42 — 🔴 — Character — Hand fusion with metal railing and finger geometry collapse. |
| S05 | 🔴 | zaman 0:43 | ① | :43 — 🔴 — Creatures — Alien limb clips through suit shoulder plate. |
| S05 | 🟠 | zaman 0:46 | ⑦ | :46 Point of impact and physical grab when alien drops onto lever operator's back ① CONTACT / ④ ELLIPSIS 🟠 Medium |
| S05 | 🟠 | zaman 0:41 | ① | :41 — 🟠 — Motion Quality — Motion stutter and ghosting artifacting during rapid creature pan. |
| S06 | 🟠 | zaman 0:50 | ⑧ | :50 Hanging suspended from tether loop Abdominal core tension & grip strain ⑤ GRIP THAT NEVER FAILS 🟠 |
| S06 | 🟠 | zaman 0:50 | ⑭ | :50 body · mid-air 180° spin He rotates 180 degrees upside down while floating — no wall push or force caused it. SPIN ④ 🟠 |
| S06 | 🟠 | zaman 0:53 | ① | :53 — 🟠 — Scale & Physics — Tether line floats rigidly without realistic weight or gravitational arc. |
| S07 | 🟠 | zaman 1:03 | ① | :03 — 🟠 — Environment — Control panel surface textures breathe and swim behind moving subject. |
| S07 | 🟠 | zaman 1:08 | ① | :08 — 🟠 — Lighting — Unmotivated AI bloom haze around orange winch attachment point. |
| S08 | 🔴 | zaman 1:10 | ⑧ | :10 Carabiner clipping with heavy suit gloves Material resistance from pressurized suit gloves ⑥ THE SUIT THAT ISN'T THERE 🔴 |
| S09 | 🔴 | zaman 1:21 | ⑧ | :21 Cutting heavy steel cable with hand shears Two-handed leverage, tool binding, hand tremor ① EFFORTLESS HEAVY 🔴 |
| S09 | 🔴 | zaman 1:21 | ① | :21 — 🔴 — Particles — Metal cutting sparks float upward in zero-g trajectory while characters remain grounded. |
| S09 | 🔴 | zaman 1:23 | ① | :23 — 🔴 — Scale & Physics — Sudden shift between zero-g floating and heavy running without environmental trigger. |
| S10 | 🟠 | zaman 1:30 | ② | :30 BODY C1 3 Three red scratch marks on right sleeve in S11 vanish in S13 🟠 |
| S10 | 🟠 | zaman 1:33 | ① | :33 — 🟠 — Character — Facial feature structure drifts inside helmet visor across shots. |
| S11 | 🟠 | zaman 1:44 | ② | :44 WORLD — 12 Black Xenomorph in S3 changes to pale fleshy mutant in S16 🟠 |
| S12 | 🔴 | zaman 1:50 | ① | :50 — 🔴 — Negative Bible — Burned-in text graphic "LOOK UP" on promotional title card frame. |

## MARS_SON_CIKIS

`ızgara hook 0 s · klip 10 s · sahne 36 · ham 30/30 geçerli · bulgu 36 → tekil 36`

`③ kimlik: 9/30 güçlü bayrak · üretim defter: ⬜19 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🟠 | zaman 0:08 | ① | :08 — 🟠 MAJOR — Glove structure morphs and phases into metal lever handle during mechanical operation. |
| S01 | 🟠 | zaman 0:08 | ① | :08 — 🟠 — Character — Glove fingers deform and merge into mechanical wrench handle. |
| S04 | 🟠 | zaman 0:33 | ① | :33 — 🟠 — Scale & Physics — Liquid water stream flows with standard 1G Earth pour rate. |
| S05 | 🟠 | zaman 0:42 | ① | :42 — 🟠 — Lighting & Color — Soft unmotivated haze bloom surrounding overhead red emergency lights. |
| S09 | 🟠 | zaman 1:21 | ② | :21 BODY Aras 2 Orange shoulder patch on left arm in S1 flips to right arm in S9. 🟠 |
| S10 | 🟠 | zaman 1:34 | ① | :34 — 🟠 — Particles & Materials — Extinguisher foam clips directly through metal floor lattice. |
| S11 | 🟠 | zaman 1:48 | ① | :48 — 🟠 MAJOR — Handheld flare flame materializes directly in glove grip without igniter structure. |
| S11 | 🟠 | zaman 1:48 | ① | :48 — 🟠 — Particles & Materials — Torch flame drifts detached from physical holding device. |
| S13 | 🔴 | zaman 2:01 | ② | :01 WORLD — 8 Clean utility corridor in S12 jumps to narrow burning hatch in S13. 🔴 |
| S13 | 🔴 | zaman 2:08 | ① | :08 — 🔴 BLOCKER — Garbled AI text characters ("RESTRICGET FLTACK 7/") generated on emergency bulkhead door panel. |
| S13 | 🔴 | zaman 2:08 | ① | :08 — 🔴 — Dialogue & Audio — Hallucinated text characters ("RESTRICGET FLTACK 7/") on hatch door. |
| S13 | 🟠 | zaman 2:09 | ⑦ | :09 Yangın kapısının erkek astronotun gövdesine temas ettiği ve ezdiği nokta kapı çerçevesi altında perdeleniyor. Pattern ① 🟠 MODERATE |
| S14 | 🟠 | zaman 2:10 | ② | :10 WORLD — 10 Fire door slams fully shut in S13, then re-opens partially in S14. 🟠 |
| S15 | 🔴 | zaman 2:20 | ② | :20 WORLD — 11 Interior corridor evacuation jumps instantly to outdoor surface run without airlock cycle. 🔴 |
| S15 | 🟠 | zaman 2:22 | ② | :22 BODY Aras 3 Sooted suit from hatch escape resets to clean suit during surface run. 🟠 |
| S19 | 🔴 | B2+ 3:02 | ① | :02 — 🔴 BLOCKER — Dialogue & Audio — Unfiltered airborne voiceover played over vacuum exterior without suit radio acoustic processing. |
| S19 | 🔴 | B2+ 3:02 | ① | :02 — 🔴 — Dialogue & Audio — Clear airborne voice acoustics present during external vacuum shot. |
| S19 | 🟠 | B2+ 3:05 | ① | :05 — 🟠 — Particles & Materials — Dust/ice particles drift with artificial camera-dragged motion. |
| S19 | 🟠 | B2+ 3:07 | ① | :07 — 🟠 — Lighting & Color — Diffuse AI bloom haze present around station solar arrays and module highlights. |
| S23 | 🔴 | B2+ 3:41 | ① | :41 — 🔴 BLOCKER — Negative Bible — On-screen computer HUD text graphics burned directly over video frame. |
| S23 | 🔴 | B2+ 3:41 | ① | :41 — 🔴 — Negative Bible — Burned-in text and numerical readouts overlaying cockpit monitor view. |
| S24 | 🟠 | B2+ 3:58 | ① | :58 — 🟠 — Character — Visor HUD target graphic floats off-plane from glass reflection. |
| S25 | 🟠 | B2+ 4:04 | ① | :04 — 🟠 — Camera & Cinematography — Scope reticle overlay lacks optical depth and lens glass distortion. |
| S26 | 🔴 | B2+ 4:15 | ⑤ | :15 Midground 6 Smooth concentric docking port in S4 morphs into rectangular pin collar in S10 🔴 Critical |
| S26 | 🟠 | B2+ 4:12 | ① | :12 — 🟠 — Scale & Physics — RCS thruster plume expands like dense atmospheric vapor in hard vacuum. |
| S30 | 🔴 | B2+ 4:55 | ⑤ | :55 Midground 6 S10 receiving collar has no clamps; S14 introduces four heavy articulated mechanical claw arms 🔴 Critical |
| S33 | 🔴 | B2+ 5:20 | ② | :20 BODY Both 4 In S16 helmets are sealed on heads; in S17 helmets are carried in hand; in S18 helmets are re-sealed on heads 🔴 Major |
| S33 | 🔴 | B2+ 5:20 | ① | :20 — 🔴 BLOCKER — Character — Suit wardrobe drifts from standard white suit to blue chest paneling mid-sequence. |
| S33 | 🔴 | B2+ 5:20 | ① | :20 — 🔴 — Character Consistency — Copilot suit shifts color scheme to blue torso accents before reverting. |
| S33 | 🟠 | B2+ 5:20 | ② | :20 BODY Female Astronaut 2 In S16 suit is plain tan/beige; in S17 suit has dark blue chest armor; in S18 suit reverts to plain tan 🟠 Moderate |
| S33 | 🟠 | B2+ 5:28 | ⑭ | :28 legs/feet · walks She steps forward to cross the hatch threshold, but her boots glide across the floor grates without traction. SLIDE ③ 🟠 |
| S34 | 🟠 | B2+ 5:35 | ⑤ | :35 Midground 4 S17 circular pressure hatch with central handwheel leads into S18 square stenciled door "R5" 🟠 Major |
| S35 | 🔴 | B2+ 5:41 | ① | :41 — 🔴 — Negative Bible — Text labels ("RADIATION DOSIMETER") rendered on wall monitor prop asset. |
| S35 | 🟠 | B2+ 5:45 | ⑤ | :45 Midground 9 S19 dosimeter screen text garbles into full solid green LED block filling display aperture 🟠 Major |
| S36 | 🔴 | B2+ 5:50 | ② | :50 BODY Male Astronaut 3 In S2, S5, S16, S18 sling is on RIGHT arm; in S20 sling is on LEFT arm 🔴 Major |
| S36 | 🟠 | B2+ 5:55 | ⑤ | :55 Far Field 4 S3 establishes low Earth orbit; S20 rear window displays Mars disk in deep space 🟠 Major |

## THE_RESONANT_STRAND

`ızgara hook 0 s · klip 8.9 s · sahne 14 · ham 13/13 geçerli · bulgu 31 → tekil 31`

`③ kimlik: 10/13 güçlü bayrak · üretim defter: ⬜0 ✅4`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🟠 | zaman 0:00 | ⑧ | :00 🟠 MAJOR — Cost curve sits perpetually at zero despite exertions |
| S00 | 🟠 | zaman 0:00 | ⑫ | :00 🟠 MAJOR — S1–S5 Pacing drags before major anomaly arrives |
| S00 | 🟠 | zaman 0:00 | ① | :00 🟠 MAJOR — Texture swimming on canyon walls during dust storm |
| S01 | 🟠 | ≈S-ref 2:10 | ④ | :10 — 🟠 MAJOR — S2 and S10 floating elements form a bookend frame but feel disconnected from main arc. |
| S01 | 🟠 | zaman 0:09 | ① | :09 — 🟠 MAJOR — Sand whirlwinds exhibit texture swimming on the canyon wall backdrop. |
| S01 | 🟠 | zaman 0:10 | ① | :10 🟠 MAJOR — Unstable debris gravity around rising slab |
| S01 | 🟠 | zaman 0:10 | ① | :10 🟠 MAJOR — Particle clipping on levitating slab |
| S02 | 🟠 | zaman 0:20 | ④ | :20 🟠 MAJOR — Transition to small card slows narrative momentum |
| S02 | 🟠 | zaman 0:20 | ⑫ | :20 🟠 MAJOR — S3–S5 Mid-section stalls on boots, crates, and wrist checks |
| S02 | 🟠 | zaman 0:25 | ① | :25 — 🟠 MAJOR — Suit chest harness geometry shifts slightly between |
| S02 | 🟠 | zaman 0:19 | ① | :19 — 🟠 MAJOR — Debris and rocks around the rising metal plate hover erratically without a clear magnetic or gravitational gradient. |
| S02 | 🟠 | zaman 0:19 | ① | :19 — 🟠 MAJOR — Floating dust particles around the rising slab snap out of existence when colliding with the plate boundary. |
| S03 | 🟠 | zaman 0:35 | ④ | :35 — 🟠 MAJOR — Transition from floating slate to floating card slows narrative momentum. |
| S03 | 🟠 | zaman 0:35 | ⑩ | :35 🟠 MAJOR — S3, S9 Figure retains rigid mannequin-like stance |
| S03 | 🟠 | zaman 0:35 | ⑩ | :35 🟠 MAJOR — S3, S9 Decision points rely on visual events rather than bodily shift |
| S06 | 🟠 | zaman 1:00 | ⑩ | :00 🟠 MAJOR — S1, S3, S12 Hands perform harness adjustments mechanically |
| S07 | 🔴 | zaman 1:10 | ⑧ | :10 🔴 BLOCKER — E2 flare gun held without recoil torque or hand tremor |
| S07 | 🟠 | zaman 1:10 | ⑦ | :10 🟠 MAJOR — B8 shot fired without showing target, impact, or consequence |
| S07 | 🟠 | zaman 1:10 | ⑦ | :10 🟠 MAJOR — B8 flare shot leaves no persistent impact in environment |
| S07 | 🟠 | zaman 1:10 | ⑦ | :10 🟠 MAJOR — B8 target of gun shot is entirely off-screen |
| S07 | 🟠 | zaman 1:10 | ⑧ | :10 🟠 MAJOR — E1, E2 walking gait and arm holding firearm display no suit weight |
| S08 | 🟠 | zaman 1:20 | ⑦ | :20 🟠 MAJOR — B8/B9 threats appear directly overhead without approach trajectory |
| S08 | 🟠 | zaman 1:20 | ⑫ | :20 🟠 MAJOR — S11 Abrupt transition to end title card |
| S09 | 🟠 | zaman 1:21 | ⑨ | :21 🟠 MAJOR — S1 vs S11 setup failure, framing and shot size do not rhyme |
| S10 | 🟠 | ≈S-ref 2:25 | ④ | :25 — 🟠 MAJOR — Title card S11 presents starkly different art style and environment. |
| S13 | 🔴 | zaman 2:00 | ⑧ | :00 🔴 BLOCKER — E1, E2, E3 complete absence of physical effort or recoil |
| S13 | 🔴 | zaman 2:00 | ⑧ | :00 🔴 BLOCKER — E1, E3 suit gloves operate with zero mechanical stiffness |
| S13 | 🟠 | zaman 2:00 | ⑧ | :00 🟠 MAJOR — E1 to E3 physical state remains 100% rested across runtime |
| S13 | 🟠 | zaman 2:00 | ⑪ | :00 🟠 MAJOR — S6→S7 & S11→S12 Environment exposure jumps between shots |
| S13 | 🟠 | zaman 2:00 | ⑪ | :00 🟠 MAJOR — S3, S12 Visor reflection switches between gold chrome and translucent |
| S13 | 🟠 | zaman 2:00 | ① | :00 🟠 MAJOR — Harness detail drift on close-up adjustments |

## THE_SOLAR_MIRROR

`ızgara hook 10 s · klip 10 s · sahne 12 · ham 12/12 geçerli · bulgu 25 → tekil 25`

`③ kimlik: 1/12 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🔴 | zaman 0:09 | ⑧ | :09 Operating heavy cutting tool Forearm strain, glove resistance, posture bracing against torque Pattern ①, ⑥ 🔴 BLOCKER |
| S00 | 🟠 | zaman 0:09 | ① | :09 — 🟠 MAJOR — Hard jump cut between repair shot and tool disconnection without spatial transition. |
| S00 | 🟠 | zaman 0:02 | ① | :02 — 🟠 MAJOR — Diffuse AI bloom and anamorphic lens streak around electrical repair tool. |
| S00 | 🟠 | zaman 0:03 | ① | :03 — 🟠 MAJOR — Sparks from welding arc float smoothly instead of spraying in straight ballistic trajectories in microgravity vacuum. |
| S01 | 🔴 | zaman 0:15 | ⑧ | :15 Applying torque until tool disconnects Body recoil, wrist tensing, momentum transfer upon release Pattern ①, ⑤ 🔴 BLOCKER |
| S01 | 🟠 | zaman 0:19 | ⑦ | :19 Origin and mechanism of the blue energy ring surrounding the lost tool ⑬ Threat With No Approach 🟠 MAJOR |
| S01 | 🟠 | zaman 0:15 | ⑤ | :15 Far Field 4 Space shuttle position jumps from far left in S1 to upper right in S2 🟠 MAJOR |
| S01 | 🟠 | zaman 0:15 | ① | :15 — 🟠 MAJOR — Dislodged tool floats away without realistic momentum preservation or counter-rotation. |
| S02 | 🟠 | zaman 0:29 | ⑧ | :29 Gripping rail against drift/vibration Forearm muscle engagement, re-gripping adjustment, glove stiffness Pattern ⑤, ⑥ 🟠 MAJOR |
| S04 | 🔴 | zaman 0:49 | ⑧ | :49 Latching carabiner clip with suit gloves Glove joint stiffness, reduced fine dexterity, finger resistance Pattern ⑥, ⑬ 🔴 BLOCKER |
| S05 | 🔴 | zaman 0:53 | ① | :53 — 🔴 BLOCKER — White gas/smoke vents and expands in a dense cloud as if within atmospheric pressure rather than dissipating instantly in vacuum. |
| S05 | 🟠 | zaman 0:56 | ⑧ | :56 Pulling heavy mechanical lever Counter-push leverage against hull, shoulder drop, heavy breathing Pattern ①, ⑩ 🟠 MAJOR |
| S06 | 🔴 | zaman 1:02 | ① | :02 — 🔴 BLOCKER — Open atmospheric fire and combustion smoke burning along truss bridge in space vacuum. |
| S06 | 🔴 | zaman 1:04 | ① | :04 — 🔴 BLOCKER — Billowing dark smoke clouds rolling upward over truss structure in zero-atmosphere environment. |
| S06 | 🔴 | zaman 1:02 | ① | :02 — 🔴 BLOCKER — Open flame/fire burning on structure in space vacuum. |
| S06 | 🟠 | zaman 1:02 | ⑤ | :02 Far Field 6 Hexagonal mirror array destroyed/exploded in S5/S6 is fully intact in S7 🟠 MAJOR |
| S06 | 🟠 | zaman 1:05 | ⑤ | :05 — Sky/Mid 8 Atmospheric fire and thick smoke burn along metal truss in hard vacuum 🟠 MAJOR |
| S06 | 🟠 | zaman 1:09 | ⑧ | :09 Traversing truss during explosion Accelerated breathing, posture hurry, muscle fatigue Pattern ②, ⑩ 🟠 MAJOR |
| S08 | 🔴 | zaman 1:25 | ⑤ | :25 Midground 1 Subject duplicate with identical facial features/suit appears opposite primary subject 🔴 BLOCKER |
| S08 | 🟠 | zaman 1:20 | ① | :20 — 🟠 MAJOR — Reflection in hexagonal mirror shows duplicate astronaut figure with desynced head rotation. |
| S09 | 🟠 | zaman 1:30 | ⑤ | :30 — Edge 9 Emergent AI gibberish text ("VI.DLIFE") stenciled on hatch structure 🟠 MAJOR |
| S09 | 🟠 | zaman 1:32 | ① | :32 — 🟠 MAJOR — Decal text "S04" and "VI.DLIFE" warps and distorts across airlock frame movement. |
| S09 | 🟠 | zaman 1:32 | ① | :32 — 🟠 MAJOR — Warping/distorting text on airlock hull ("S04"). |
| S11 | 🟠 | zaman 1:56 | ⑤ | :56 — Midground 2 Background figure on lower truss slides laterally across beam without walking motion 🟠 MAJOR |
| S11 | 🟠 | zaman 1:52 | ⑥ | :52 implies structure frame openings exceed 3.5 m relative to astronaut 🟠 MAJOR |

## THE_STILL_SWARM

`ızgara hook 10 s · klip 10 s · sahne 14 · ham 8/8 geçerli · bulgu 25 → tekil 25`

`③ kimlik: 0/8 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🟠 | zaman 0:19 | ① | :19 — 🟠 MAJOR — Particles & Materials — Floating panels lack continuous momentum. |
| S02 | 🟠 | zaman 0:29 | ⑧ | :29 Pushing floating metal panel Torso bracing, slower deliberate extension ① 🟠 |
| S02 | 🟠 | zaman 0:20 | ① | :20 — 🟠 MAJOR — Environment — Floating panels exhibit texture swimming. |
| S03 | 🟠 | zaman 0:30 | ⑤ | :30 Far 4 Sphere panel structure completely regenerates 🟠 |
| S03 | 🟠 | zaman 0:39 | ① | :39 — 🟠 MAJOR — Scale & Physics — Tool removal physics rigid, minor hand clipping. |
| S04 | 🟠 | zaman 0:49 | ① | :49 — 🟠 MAJOR — Lighting — AI bloom on emitted gas and suit back. |
| S05 | 🔴 | zaman 0:59 | ① | :59 — 🔴 BLOCKER — Camera — Hidden cut/jump inside scene; pose shifts instantly. |
| S05 | 🔴 | zaman 0:58 | ① | :58 — 🔴 BLOCKER — Particles & Materials — Gas emission freezes into static 2D plane. |
| S05 | 🟠 | zaman 0:59 | ② | :59 BODY Astronaut 4 Tether firmly in hand vs totally absent 🟠 MAJOR |
| S05 | 🟠 | zaman 0:52 | ⑥ | :52 5 Gas spray exhibits atmospheric aerodynamic swirling in zero-atmosphere vacuum 🟠 |
| S05 | 🟠 | zaman 0:59 | ③ | :59 SFX 7 Visible high-pressure gas spray vs lack of conductive/suit SFX 🟠 MAJOR |
| S06 | 🟠 | zaman 1:00 | ② | :00 BODY Astronaut 2 Square backpack present vs back is flat/missing pack 🟠 MAJOR |
| S09 | 🟠 | zaman 1:39 | ⑧ | :39 Holding heavy metal box Postural shift, forearm tension, bulk collision ⑥ 🟠 |
| S09 | 🟠 | zaman 1:30 | ⑧ | :30 9 Maximal facial and physical strain pulling the tether (S9) instantly disappears into a completely relaxed, calm posture in the next shot (S10) with no recovery shown 🟠 |
| S10 | 🔴 | zaman 1:40 | ① | :40 — 🔴 BLOCKER — Background debris particles are entirely static/frozen. |
| S10 | 🔴 | zaman 1:40 | ① | :40 — 🔴 BLOCKER — Particles & Materials — Surrounding debris frozen in space. |
| S10 | 🟠 | zaman 1:42 | ① | :42 — 🟠 MAJOR — Character — Hand melting/morphing when interacting with clamp. |
| S11 | 🔴 | zaman 1:59 | ② | :59 BODY N/A 12 1-person mission established vs 2 astronauts visible 🔴 BLOCKER |
| S11 | 🟠 | zaman 1:59 | ② | :59 WORLD N/A 8 Inside cylinder vs hard cut to sphere exterior 🟠 MAJOR |
| S11 | 🟠 | zaman 1:52 | ⑥ | :52 3 L2 push yields zero astronaut recoil; L7 push yields proper reactive recoil 🟠 |
| S12 | 🔴 | zaman 2:00 | ① | :00 — 🔴 BLOCKER — Duplicate character phases out of structure behind main subject. |
| S12 | 🔴 | zaman 2:01 | ① | :01 — 🔴 BLOCKER — Extra limbs/arms appear holding the wall. |
| S12 | 🔴 | zaman 2:00 | ① | :00 — 🔴 BLOCKER — Character — Duplicate head/body spawns in background. |
| S12 | 🔴 | zaman 2:01 | ① | :01 — 🔴 BLOCKER — Character — Three arms visible on subject. |
| S12 | 🔴 | zaman 2:01 | ① | :01 — 🔴 BLOCKER — Scale & Physics — Floating canvas belt clips completely through torso. |

## THE_LOCKED_PULSE

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 12/12 geçerli · bulgu 24 → tekil 24`

`③ kimlik: 4/12 güçlü bayrak · üretim defter: ⬜19 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🔴 | zaman 0:04 | ⑧ | :04 Turning heavy valve wheel Wrist tendon engagement, shoulder drop, leg stance bracing ① Effortless Heavy 🔴 BLOCKER |
| S00 | 🟠 | zaman 0:05 | ① | :05 — 🟠 MAJOR — Soft diffuse AI bloom around linear ceiling light panels reduces optical contrast. |
| S00 | 🟠 | zaman 0:05 | ① | :05 — 🟠 MAJOR — Airbrushed, waxy skin texture under overhead lighting. |
| S01 | 🟠 | zaman 0:15 | ⑧ | :15 Sustained manual valve cranking Visor condensation/fogging, elevated chest rise ⑩ Breath Doesn't Track 🟠 MAJOR |
| S01 | 🟠 | zaman 0:10 | ① | :10 — 🟠 MAJOR — Facial structure and jawline drift between wide profile and close-up angles. |
| S02 | 🟠 | zaman 0:24 | ⑤ | :24 Midground 6 Fabric wall strap hangs on left wall in S1; completely missing from same wall angle in S3 🟠 MAJOR |
| S02 | 🟠 | zaman 0:25 | ⑤ | :25 Midground 6 Floor grate left of subject is bare in S1; silver combination wrench appears lying on grate in S3 🟠 MAJOR |
| S02 | 🟠 | zaman 0:24 | ⑧ | :24 Cranking wheel with heavy wrench Asymmetric torso angle, shoulder dip ⑨ Symmetric under Asymmetric Load 🟠 MAJOR |
| S03 | 🟠 | zaman 0:32 | ① | :32 — 🟠 MAJOR — Glove texture phases into metal wheel rim during manual rotation. |
| S03 | 🟠 | zaman 0:30 | ① | :30 — 🟠 MAJOR — Venting steam particles lack physical mass and dissipate uniformly as flat haze. |
| S03 | 🟠 | zaman 0:32 | ① | :32 — 🟠 MAJOR — Surface clipping on glove contact. |
| S05 | 🔴 | zaman 0:52 | ⑧ | :52 Rising from kneeling & walking Leg tremor, slow rise using wall support, heavy breathing ③ Fresh Reset 🔴 BLOCKER |
| S05 | 🟠 | zaman 0:54 | ⑤ | :54 Midground 6 Right corridor wall is bare metallic paneling in S5; large grey supply cabinet materializes in S6 🟠 MAJOR |
| S05 | 🟠 | zaman 0:50 | ① | :50 — 🟠 MAJOR — Metallic corridor wall panels breathe and shift seam alignment during camera push. |
| S05 | 🟠 | zaman 0:54 | ① | :54 — 🟠 MAJOR — Walk cycle exhibits minor foot sliding against floor grating. |
| S07 | 🔴 | zaman 1:14 | ⑧ | :14 Levering valve with breaker bar Torso arching, foot bracing against floor deck ① Effortless Heavy 🔴 BLOCKER |
| S07 | 🟠 | zaman 1:10 | ① | :10 — 🟠 MAJOR — Red warning beacon creates hazy ambient halo rather than crisp directional falloff. |
| S08 | 🟠 | zaman 1:24 | ⑧ | :24 Maximum torque leverage pull Forearm muscle flex, hand re-gripping/slippage ⑤ Grip That Never Fails 🟠 MAJOR |
| S10 | 🔴 | zaman 1:42 | ⑧ | :42 Secondary valve tightening effort Speed decay compared to early turns, visible strain ② Infinite Stamina 🔴 BLOCKER |
| S11 | 🟠 | zaman 1:55 | ⑧ | :55 Reaching inside valve port mechanism Suit neck restriction, fine-motor hand tremor after gross torque ⑬ Untiring Hand 🟠 MAJOR |
| S12 | 🟠 | zaman 2:02 | ① | :02 — 🟠 MAJOR — Hand distorts and merges into circular port collar metal upon insertion. |
| S13 | 🟠 | zaman 2:09 | ⑦ | :09 Astronotun elinin port deliği içinde neye dokunduğu, neyi kavradığı veya çevirdiği ① Contact without Occlusion / ⑫ Stakes Object Off-Screen 🟠 MAJOR |
| S13 | 🟠 | zaman 2:13 | ③ | :13 7 Audio states "Ring at four revolutions" (4 RPM), but visual exterior shot L14 shows 0.21 RPM rotation (2.1° over 10 s). 🟠 MAJOR |
| S17 | 🟠 | zaman 2:49 | ⑧ | :49 Post-emergency corridor walk Dragging gait, chest heave, suit ventilation recovery ⑧ Recovery Faster Than Exertion 🟠 MAJOR |

## THE_STANDING_WIRE

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 8/8 geçerli · bulgu 24 → tekil 24`

`③ kimlik: 0/8 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🔴 | zaman 0:03 | ① | :03 — 🔴 BLOCKER — Floating particles without gravitational cause near the base plate. |
| S00 | 🔴 | zaman 0:03 | ① | :03 — 🔴 BLOCKER — Particles & Materials — Pebbles float and disappear without cause. |
| S03 | 🟠 | zaman 0:34 | ⑥ | :34) (baseplate cover clips through solid wire) 🟠 |
| S03 | 🟠 | zaman 0:30 | ① | :30 — 🟠 MAJOR — Character — Glove details and thickness shift dramatically between shots. |
| S04 | 🟠 | zaman 0:40 | ⑧ | :40 Climbing giant stairs Torso lean, slower pace, deep breath ① Effortless heavy 🟠 |
| S05 | 🔴 | zaman 0:50 | ⑧ | :50 Scaling sheer cliff Tremor, re-gripping, pauses to search for holds ① Effortless heavy 🔴 |
| S05 | 🟠 | zaman 0:58 | ③ | :58 Delivery 4 Vocal effort (calm, resting) contradicts physical effort (free-climbing a massive vertical rock face in a heavy suit). 🟠 MAJOR |
| S07 | 🟠 | zaman 1:10 | ⑧ | :10 Scaling cliff Grunting/breath, strained face in helmet, forearm tension ⑤ Grip that never fails 🟠 |
| S10 | 🟠 | zaman 1:41 | ② | :41 BODY The Astronaut 2 Gloves are thick ribbed armor (A) vs smooth leather (B) 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ⑧ | :50 Scrambling rocks Suit bulk limiting leg lift, balance shifts ⑥ The suit that isn't there 🟠 |
| S12 | 🟠 | zaman 2:02 | ② | :02 BODY The Astronaut 2 Suit chest panels are thin stripes (A) vs thick white yoke (B) 🟠 MAJOR |
| S14 | 🟠 | zaman 2:22 | ③ | :22 SFX Sync 7 Footfall sound effects do not align with the visible pace of the boots hitting the rock. 🟠 MAJOR |
| S15 | 🟠 | zaman 2:32 | ② | :32 BODY The Astronaut 3 Knees heavily caked with gray mud (A) vs pristine clean blue (B) 🟠 MAJOR |
| S16 | 🟠 | zaman 2:40 | ⑤ | :40 (persistent static vertical line artifact) 🟠 |
| S16 | 🟠 | zaman 2:40 | ⑧ | :40 Pulling cage Bracing the legs, whole-body weight shift ① Effortless heavy 🟠 |
| S18 | 🟠 | zaman 3:00 | ⑧ | :00 Hanging from cage Forearm lock, shoulder extension, body sway ⑤ Grip that never fails 🟠 |
| S18 | 🟠 | zaman 3:00 | ① | :00 — 🟠 MAJOR — Character is completely rigid while floating in zero-g; no micro-motion or limb drift. |
| S18 | 🟠 | zaman 3:00 | ① | :00 — 🟠 MAJOR — Scale & Physics — Rigid character model dragging in zero-g lift. |
| S19 | 🔴 | zaman 3:10 | ⑧ | :10 3 Body performs extreme physical mountaineering for 3 minutes but maintains the exact same resting baseline posture as the opening shot. 🔴 |
| S21 | 🟠 | zaman 3:30 | ⑥ | :30 6 Wire diameter ~2cm at base vs ~20cm at space station 🟠 |
| S21 | 🟠 | zaman 3:36 | ① | :36 — 🟠 MAJOR — Dialogue & Audio — Airborne whoosh sound layered with hatch opening in vacuum. |
| S23 | 🟠 | zaman 3:50 | ① | :50 — 🟠 MAJOR — Scale & Physics — Wire behaves like a 2D ribbon inside the cabin, defying tension logic. |
| S24 | 🔴 | zaman 4:00 | ① | :00 — 🔴 BLOCKER — Title text burned onto the screen. |
| S24 | 🔴 | zaman 4:00 | ① | :00 — 🔴 BLOCKER — Negative Violations — "THE STANDING WIRE" text baked onto screen. |

## THE_DRY_ANCHOR

`ızgara hook 0 s · klip 10 s · sahne 14 · ham 8/12 geçerli · bulgu 23 → tekil 23`

`③ kimlik: 8/12 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:04 | ⑧ | :04 (E5) Lifting heavy equipment crate and rising to standing Spine curvature, quad engagement, shoulder drop under mass ① Effortless Heavy / ⑨ Symmetric Body 🔴 BLOCKER |
| S01 | 🟠 | zaman 0:04 | ⑧ | :04 - Effortless heavy lift of crate without back curve, leg drive, or neck strain); -3 · 🟠 E1 ( |
| S01 | 🟠 | zaman 0:06 | ⑧ | :06 - Visor glass exhibits zero interior moisture/fogging during intense physical tasks); -3 · 🟠 E4/E5 ( |
| S01 | 🟠 | zaman 0:02 | ⑧ | :02 - Pressurized suit gloves display bare-hand dexterity with zero resistance to finger flexion); -3 · 🟠 E1/E4/E5 ( |
| S01 | 🟠 | zaman 0:04 | ⑧ | :04 - Curve drops from 3 to 1 with zero recovery shown or time elapsed); -3 · 🟠 Scene 12 ending ( |
| S01 | 🟠 | zaman 0:05 | ① | :05 — 🟠 MAJOR — Lander thruster dust plumes freeze abruptly mid-shot without fluid dissipation. |
| S01 | 🟠 | zaman 0:05 | ① | :05 — 🟠 MAJOR — Exhaust dust underneath lander lacks physical mass and vanishes instantaneously. |
| S03 | 🔴 | zaman 0:27 | ① | :27 — 🔴 BLOCKER — Footprints are pre-rendered into the soil before the astronaut's boots land on those exact locations. |
| S03 | 🟠 | zaman 0:20 | ① | :20 — 🟠 MAJOR — Airbrushed plastic skin texture on facial features inside helmet with artificial specular highlights. |
| S03 | 🟠 | zaman 0:29 | ① | :29 — 🟠 MAJOR — Ground soil texture swims and morphs around footprints as the boot lifts. |
| S04 | 🔴 | zaman 0:38 | ① | :38 — 🔴 BLOCKER — Gloved fingers fuse and morph directly into the metal handle of the hammer during strokes. |
| S04 | 🟠 | zaman 0:38 | ① | :38 — 🟠 MAJOR — Hammer hits ground stake with zero soil displacement, shockwave, or recoil mass. |
| S04 | 🟠 | zaman 0:30 | ① | :30 — 🟠 MAJOR — Walking locomotion exhibits subtle foot sliding over soil. |
| S06 | 🔴 | ≈S-ref — | ⑧ | Recovery Curve Honesty 2/10 -5 · 🔴 Reset between Scene 7 and Scene 8 ( |
| S06 | 🟠 | zaman 0:58 | ① | :58 — 🟠 MAJOR — Silt texture under the beige strap exhibits procedural surface breathing. |
| S07 | 🔴 | zaman 1:06 | ① | :06 — 🔴 BLOCKER — Ring of dark dust erupts out of air around central lander leg without physical source. |
| S07 | 🟠 | zaman 1:00 | ① | :00 — 🟠 MAJOR — Lander module leg geometry and lower hull proportions shift between wide and close framings. |
| S08 | 🔴 | zaman 1:18 | ① | :18 — 🔴 BLOCKER — Right glove deforms and liquid-morphs into the sand surface while digging. |
| S09 | 🔴 | zaman 1:25 | ① | :25 — 🔴 BLOCKER — Yellow tether strap clips cleanly through the solid metal lander leg structure. |
| S09 | 🔴 | zaman 1:21 | ① | :21 — 🔴 BLOCKER — Geometry clipping (tether passing through solid lander leg). |
| S11 | 🔴 | zaman 1:48 | ① | :48 — 🔴 BLOCKER — Left hand holding the ground pin melts into the metallic shaft. |
| S11 | 🔴 | zaman 1:48 | ① | :48 — 🔴 BLOCKER — Hammer tool morphs from a standard head into a dual-chisel shape mid-strike. |
| S11 | 🔴 | zaman 1:43 | ① | :43 — 🔴 BLOCKER — Multiple instances of mesh merging and finger-to-prop contact morphing. |

## THE_TETHERED_MASS

`ızgara hook 0 s · klip 10 s · sahne 16 · ham 12/12 geçerli · bulgu 22 → tekil 22`

`③ kimlik: 6/12 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🟠 | zaman 0:06 | ① | :06 — 🟠 MAJOR — Snapped steel cable strand coils smoothly and floats away like a rigid wire spring without kinetic uncoiling reaction. |
| S02 | 🟠 | zaman 0:17 | ⑤ | :17 (S5) Far Field 4 Mountain horizon line changes profile from sharp crags to rounded hills 🟠 MAJOR |
| S02 | 🟠 | zaman 0:17 | ⑤ | :17 (S5) Far Field 5 Vessel hull and mountain background move as single flat plate without parallax 🟠 MAJOR |
| S02 | 🟠 | zaman 0:12 | ① | :12 — 🟠 MAJOR — Metallic winch housing paneling displays texture breathing and surface ridge drift. |
| S02 | 🟠 | zaman 0:14 | ① | :14 — 🟠 MAJOR — Unspooling cable tendrils jitter and morph frame-to-frame. |
| S03 | 🟠 | zaman 0:27 | ① | :27 — 🟠 MAJOR — Facial bone structure warps around jaw and mouth during high-g grimace. |
| S04 | 🟠 | zaman 0:35 | ① | :35 — 🟠 MAJOR — Thruster plume forms expanding cloud billows in space vacuum instead of rapid conical dissipation. |
| S06 | 🟠 | zaman 0:55 | ① | :55 — 🟠 MAJOR — Soft AI bloom haze surrounds orange atmospheric horizon line without directional falloff. |
| S08 | 🟠 | zaman 1:15 | ① | :15 — 🟠 MAJOR — Main engine nozzle vents thick billowing steam in vacuum; ejecta particles lack continuous linear trajectories. |
| S08 | 🟠 | zaman 1:12 | ① | :12 — 🟠 MAJOR — Engine nozzle interior displays diffuse glowing fog rather than sharp thermal radiation falloff. |
| S08 | 🟠 | zaman 1:18 | ① | :18 — 🟠 MAJOR — Exhaust particles vanish abruptly frame-to-frame without continuous decay paths. |
| S09 | 🟠 | zaman 1:29 | ⑦ | :29 Whether nozzle venting steam and particles was a thruster pulse or a mechanical failure Pattern ⑩ / ⑪ 🟠 MAJOR |
| S09 | 🟠 | zaman 1:25 | ⑧ | :25 (S20) Standing in expanding reactor blast Defensive crouch/brace stance, face turn, backward momentum from shockwave ① 🟠 MAJOR |
| S10 | 🟠 | zaman 1:39 | ⑤ | :39 (S23) Topology 4 Snow-covered mountain ridge abruptly replaced by flat pine forest basin 🟠 MAJOR |
| S10 | 🟠 | zaman 1:39 | ⑧ | :39 (S23) Sustained walking through forest Heavy chest breathing, posture slackening, shoulder rounding, slower pace ②, ③ 🟠 MAJOR |
| S10 | 🟠 | zaman 1:30 | ⑧ | :30 (S21) Subject absorbs full reactor disintegrating explosion in S20, yet appears unblemished and physically unbothered on snow slope in S21 🟠 MAJOR |
| S10 | 🟠 | zaman 1:39 | ⑧ | :39 (S23–S32) Subject wears heavy multi-layer pressurised suit with zero mobility effort in S1–S21, then switches to bare-headed clothing in S23 with identical weightless movement patterns 🟠 MAJOR |
| S11 | 🟠 | zaman 1:42 | ① | :42 — 🟠 MAJOR — Cockpit UI flight display shows garbled AI pseudo-text and distorted numerical glyphs. |
| S12 | 🔴 | zaman 1:54 | ① | :54 — 🔴 BLOCKER — Shattered glass shards surrounding control lever morph, melt, and reshape between frames. |
| S12 | 🟠 | zaman 1:50 | ⑥ | :50 5 Falling sparks maintain constant 2.08 m/s speed across 1.2 s instead of accelerating under gravity 🟠 MAJOR |
| S12 | 🟠 | zaman 1:50 | ① | :50 — 🟠 MAJOR — Glove mesh deforms and merges into red control lever casing. |
| S13 | 🟠 | zaman 2:07 | ⑥ | :07 6 Blast door height measures 3.2 m in L3 and 5.4 m in L12 relative to operator ruler 🟠 MAJOR |

## THE_CRACKED_HELMET

`ızgara hook 10 s · klip 10 s · sahne 12 · ham 12/12 geçerli · bulgu 22 → tekil 21`

`③ kimlik: 1/12 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🟠 | zaman 0:00 | ⑥ | :00 5 Plumes of smoke rise in thick, convective, buoyant columns (requiring a dense atmosphere), contradicting the stark black sky, lack of atmospheric scattering, and starfield which establish a vacuum. A pressure leak in a vacuum expands as a rapid spherical or linear jet, not a rising chimney plu |
| S01 | 🟠 | zaman 0:10 | ⑧ | :10 Waking to a critical air leak Increased respiratory rate, panicked/jerky movements, visible hypoxia. ⑩ 🟠 MAJOR |
| S02 | 🔴 | zaman 0:20 | ① | :20 — 🔴 BLOCKER — Burned-in HUD text physically stuck on exterior of visor. |
| S02 | 🟠 | zaman 0:20 | ⑤ | :20 Sky 8 Empty black sky contradicts sky with giant ringed planet 🟠 MAJOR |
| S02 | 🟠 | zaman 0:20 | ② | :20 BODY The Astronaut 2 Black space suit contradicts white space suit 🟠 MAJOR |
| S02 | 🟠 | zaman 0:20 | ⑧ | :20 Sitting up in a heavy suit Bracing, slowness, visible weight of the pack. ① 🟠 MAJOR |
| S03 | 🟠 | zaman 0:30 | ② | :30 BODY The Astronaut 2 White space suit contradicts black space suit 🟠 MAJOR |
| S04 | 🟠 | zaman 0:40 | ⑧ | :40 Pinching a crystal in space gloves Clumsiness, stiffness in the fingers. ⑥ 🟠 MAJOR |
| S07 | 🔴 | zaman 1:17 | ① | :17 — 🔴 BLOCKER — Mixed gravity: liquid sphere floats in a 1g environment. |
| S07 | 🔴 | zaman 1:17 | ① | :17 — 🔴 BLOCKER — Scale & Physics — Mixed gravity vectors in single frame. |
| S07 | 🟠 | zaman 1:16 | ① | :16 — 🟠 MAJOR — Liquid forms zero-g sphere despite established gravity. |
| S07 | 🟠 | zaman 1:17 | ① | :17 — 🟠 MAJOR — Lighting — AI Bloom around floating liquid. |
| S07 | 🟠 | zaman 1:16 | ① | :16 — 🟠 MAJOR — Particles & Materials — Liquid ignores 1g physics to form floating sphere. |
| S08 | 🟠 | zaman 1:20 | ⑦ | :20 The transition between holding a floating liquid sphere and applying a solid shard to the glass ④ The Action Ellipsis 🟠 MAJOR |
| S08 | 🟠 | zaman 1:20 | ⑧ | :20 Sealing the helmet with seconds left Tremor, desperate speed, heavy chest heaving. ⑬ 🟠 MAJOR |
| S10 | 🟠 | zaman 1:40 | ② | :40 BODY The Astronaut 4 Plain chest box contradicts larger chest box with ORION text 🟠 MAJOR |
| S10 | 🟠 | zaman 1:40 | ⑧ | :40 2 The suit reports "CRITICAL" pressure loss, but the astronaut's breathing puffs are as calm and steady as they are when the suit is "STABLE". 🟠 MAJOR |
| S11 | 🔴 | zaman 1:50 | ⑧ | :50 Standing up after the ordeal Slumped posture, hands on knees, heavy exhaustion. ③ 🔴 BLOCKER |
| S11 | 🟠 | zaman 1:50 | ⑤ | :50 Sky 8 Black sky with single white sun contradicts orange hazy sky with two yellow suns 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ⑤ | :50 Far field 4 Airless jagged rocky terrain contradicts sprawling canyon plains 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ② | :50 BODY The Astronaut 3 Visor with sealed crack contradicts perfectly smooth gold visor 🟠 MAJOR |

## THE_PAYLOAD

`ızgara hook 9 s · klip 10 s · sahne 24 · ham 6/6 geçerli · bulgu 23 → tekil 21`

`③ kimlik: 4/6 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:10 | ① | :10 — 🔴 BLOCKER — Clear, legible text ("PHASE 1") burned into the character's suit. |
| S01 | 🔴 | zaman 0:10 | ① | :10 — 🔴 BLOCKER — Character — Text "PHASE 1" clearly printed on chest plate. |
| S02 | 🟠 | zaman 0:20 | ⑤ | :20 Far field 4 The massive field of solar arrays filling the left landscape vanishes entirely, replaced by open ground and three rovers. 🟠 MAJOR |
| S02 | 🟠 | zaman 0:20 | ② | :20 WORLD N/A 10 Field of solar arrays beside ship vanishes entirely 🟠 MAJOR |
| S02 | 🟠 | zaman 0:20 | ② | :20 BODY Custodian 2 "PHASE 1" printed on chest disappears 🟠 MAJOR |
| S07 | 🔴 | zaman 1:18 | ① | :18 — 🔴 BLOCKER — Character — Text "EVA" printed on suit back. |
| S07 | 🟠 | zaman 1:15 | ⑥ | :15 5 Dust particles fall at an implied ~0.5 m/s² (cinematic float), while solid objects (cargo case) fall at ~4.0 m/s². 🟠 MAJOR |
| S07 | 🟠 | zaman 1:15 | ⑥ | :15 3 Visually massive cargo case impacts the ground with zero recoil, ground vibration, or dust displacement. 🟠 MAJOR |
| S07 | 🟠 | zaman 1:15 | ⑥ | :15 9 Character carries what appears to be a heavy industrial case but exhibits zero biomechanical lean, counter-swing, or strain. 🟠 MAJOR |
| S07 | 🟠 | zaman 1:15 | ③ | :15 Voice/Foley 4 Character lifts/hauls heavy cases visually, but voice sounds entirely rested and seated. 🟠 MAJOR |
| S08 | 🟠 | zaman 1:20 | ① | :20 — 🟠 MAJOR — Character — Thumb merges into the metal strut upon contact. |
| S10 | 🔴 | zaman 1:45 | ⑤ | :45 Midground 1 A duplicate of the protagonist walks through the background field behind the actual protagonist. 🔴 BLOCKER |
| S10 | 🔴 | zaman 1:45 | ② · ① | :45 BODY Custodian 12 Clone duplicate of character walks past character 🔴 BLOCKER |
| S10 | 🟠 | zaman 1:40 | ⑤ | :40 Midground 6 The long continuous row of cargo cases (approx 15) suddenly drops to exactly 8 cases. 🟠 MAJOR |
| S10 | 🟠 | zaman 1:40 | ② | :40 WORLD N/A 12 Approx 15 cases in line drops to exactly 8 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ② | :50 BODY Custodian 3 Suit heavily dusted outside, pristine clean in bed 🟠 MAJOR |
| S12 | 🟠 | zaman 2:00 | ① | :00 — 🟠 MAJOR — Particles — Rocket exhaust plumes are weightless CGI spray, no ground interaction. |
| S15 | 🔴 | zaman 2:30 | ⑥ | :30 1 Cylinder floats motionless in zero-g, but later falls rapidly to the character's chest with 1g acceleration. 🔴 BLOCKER |
| S15 | 🔴 | zaman 2:30 | ① | :30 — 🔴 BLOCKER — Cylinder displays mixed physics; falls at 1g then randomly hovers in 0g. |
| S15 | 🔴 | zaman 2:30 | ① | :30 — 🔴 BLOCKER — Scale & Physics — Cylinder object falls fast, hits chest, then suspends in zero-g micro-motion. |
| S15 | 🔴 | zaman 2:30 | ① | :30 — 🔴 BLOCKER — Motion Quality — Conflicting speed/vectors in one frame (fast fall vs. weightless float). |

## THE_UPWARD_FALL

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 8/8 geçerli · bulgu 21 → tekil 21`

`③ kimlik: 6/8 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S07 | 🟠 | zaman 1:10 | ⑤ | :10 Far 4 Smooth banyan trunks become textured redwoods 🟠 MAJOR |
| S07 | 🟠 | zaman 1:11 | ⑥ | :11 7 Real-time environment vs slow-motion biomechanics 🟠 MAJOR |
| S10 | 🟠 | zaman 1:40 | ② | :40 BODY The Explorer 4 Canister scale jumps from hand-sized to massive/torso-sized. 🟠 MAJOR |
| S10 | 🟠 | zaman 1:40 | ⑧ | :40 Tossing massive cylinder bracing, back engagement, post-throw breath ① Effortless Heavy 🟠 MAJOR |
| S12 | 🟠 | zaman 2:00 | ⑤ | :00 Mid 6 Axe lodged in trunk disappears in identical environment 🟠 MAJOR |
| S13 | 🟠 | zaman 2:10 | ② | :10 BODY The Explorer 2 Visor frame changes from thin unlit black to thick glowing white. 🟠 MAJOR |
| S14 | 🟠 | zaman 2:20 | ⑧ | :20 Tying vine slower fingers, glove resistance ⑥ The Suit That Isn't There 🟠 MAJOR |
| S14 | 🟠 | zaman 2:23 | ① | :23 — 🟠 MAJOR — Hand geometry breaks down, phasing into grey cylinder and vine. |
| S14 | 🟠 | zaman 2:23 | ① | :23 — 🟠 MAJOR — Character — Hand geometry phases through green vine and container. |
| S15 | 🔴 | zaman 2:31 | ⑥ | :31 1 Upward acceleration triples floor→canopy 🔴 BLOCKER |
| S16 | 🟠 | zaman 2:40 | ② | :40 BODY The Explorer 4 Green vine tied securely around canister is completely missing when next held. 🟠 MAJOR |
| S17 | 🟠 | zaman 2:52 | ⑥ | :52 1 Accelerates in S10, drifts at constant velocity in S17 🟠 MAJOR |
| S17 | 🟠 | zaman 2:51 | ① | :51 — 🟠 MAJOR — Creature jump animation is stiff and lacks natural biological weight. |
| S17 | 🟠 | zaman 2:51 | ① | :51 — 🟠 MAJOR — Motion Quality — Background creature leaps with linear, rigid trajectory. |
| S17 | 🟠 | zaman 2:51 | ① | :51 — 🟠 MAJOR — Creatures — Background alien lacks joint articulation during jump. |
| S19 | 🟠 | zaman 3:10 | ⑧ | :10 Cutting vine forearm tension, grip adjustments ⑤ Grip That Never Fails 🟠 MAJOR |
| S19 | 🟠 | zaman 3:11 | ① | :11 — 🟠 MAJOR — Fingers morph and fuse with knife handle and vine during cut. |
| S19 | 🟠 | zaman 3:10 | ① | :10 — 🟠 MAJOR — Environment — Wood and vine textures swim during close-up interaction. |
| S19 | 🟠 | zaman 3:11 | ① | :11 — 🟠 MAJOR — Character — Left hand fuses with knife handle; blade clips through wood. |
| S20 | 🟠 | zaman 3:20 | ② | :20 WORLD N/A 8 Forest floor abruptly becomes a stark white ash/snow environment. 🟠 MAJOR |
| S21 | 🟠 | zaman 3:30 | ⑤ | :30 Far 4 Ash/snow flatland becomes deep pine forest valley 🟠 MAJOR |

## THE_COUNTED_TURN

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 11/11 geçerli · bulgu 23 → tekil 20`

`③ kimlik: 0/11 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:10 | ⑧ | :10 Running with strap Chest heave, gait change ① EFFORTLESS HEAVY 🔴 BLOCKER |
| S02 | 🔴 | zaman 0:27 | ① | :27 — 🔴 BLOCKER — Left hand fingers severely morph and melt, fusing completely with the strap geometry. |
| S03 | 🔴 | zaman 0:35 | ① | :35 — 🔴 BLOCKER — The right thumb phases entirely through the solid metal of the orange carabiner. |
| S04 | 🟠 | zaman 0:40 | ⑦ | :40 The mechanical connection of the carabiner gate ① Contact Without Occlusion 🟠 MAJOR |
| S07 | 🔴 | zaman 1:10 | ⑧ | :10 Unrolling massive spool Torso brace, leg tension ① EFFORTLESS HEAVY 🔴 BLOCKER |
| S07 | 🟠 | zaman 1:17 | ① | :17 — 🟠 MAJOR — Motion Quality — The astronaut's upward movement as they rise from the spool is unusually stiff, rigid, and mechanical. |
| S08 | 🔴 | zaman 1:20 | ⑧ | :20 Pulling strap taut Forearm engagement, glove folds ⑤ GRIP THAT NEVER FAILS 🔴 BLOCKER |
| S08 | 🔴 | zaman 1:26 | ① | :26 — 🔴 BLOCKER — Particles & Materials — The grey fabric strap passes directly through the palm of the right glove. |
| S09 | 🔴 | zaman 1:30 | ⑧ | :30 Walking dragging strap Asymmetric gait ⑨ SYMMETRIC BODY UNDER ASYMMETRIC LOAD 🔴 BLOCKER |
| S10 | 🔴 | zaman 1:44 | ① | :44 — 🔴 BLOCKER — Particles & Materials — The fabric strap phases through the solid metal floor pin as tension is applied. |
| S11 | 🔴 | zaman 1:50 | ② | :50 BODY The Astronaut 1 Male face with stubble vs smooth female face 🔴 BLOCKER |
| S11 | 🟠 | zaman 1:50 | ⑦ | :50 How the strap seats securely around the pin ① Contact Without Occlusion 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ② | :50 BODY The Astronaut 4 Orange belt clips present vs completely missing 🟠 MAJOR |
| S12 | 🔴 | zaman 2:00 | ② | :00 BODY The Astronaut 2 White bulky spacesuit vs dark ribbed leather jacket 🔴 BLOCKER |
| S16 | 🔴 | zaman 2:44 | ① | :44 — 🔴 BLOCKER — The orange carabiner phases completely through the solid metal of the rail as it is pressed down. |
| S18 | 🔴 | zaman 3:00 | ⑧ | :00 Tightening final clips Reduced dexterity, slower close ⑥ THE SUIT THAT ISN'T THERE 🔴 BLOCKER |
| S18 | 🔴 | zaman 3:05 | ① | :05 — 🔴 BLOCKER — Particles & Materials — The grey strap becomes embedded inside the geometry of the right glove. |
| S19 | 🟠 | zaman 3:16 | ⑥ | :16 1 The initial fall (S0) is visually almost as fast as the late fall (S19/S23), failing to establish the slow 1.69s baseline 🟠 MAJOR |
| S20 | 🔴 | zaman 3:25 | ① | :25 — 🔴 BLOCKER — Character — The fingers of the right hand merge into and fuse with the orange carabiner metal. |
| S22 | 🔴 | zaman 3:40 | ⑧ | :40 Repeated clipping Hand tremor, fatigue ② INFINITE STAMINA 🔴 BLOCKER |

## THE_KEPT_LIGHT

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 8/8 geçerli · bulgu 22 → tekil 20`

`③ kimlik: 3/8 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:10 | ⑥ | :10 1 Floating objects (0G) vs normal human walking gait (1G). 🔴 BLOCKER |
| S01 | 🟠 | zaman 0:10 | ② | :10 WORLD N/A 10 Hatch is wide open, then firmly closed and bolted. 🟠 MAJOR |
| S01 | 🟠 | zaman 0:10 | ② | :10 WORLD N/A 11 Character operates on hatch, then arrives at it. 🟠 MAJOR |
| S01 | 🟠 | zaman 0:10 | ① | :10 — 🟠 MAJOR — Severe mixed gravity vectors: character walks with a heavy 1g Earth terrestrial gait in an environment where loose tools and cargo crates float in zero-g. |
| S01 | 🟠 | zaman 0:12 | ① | :12 — 🟠 MAJOR — Motion Quality — Terrestrial footfall impact dynamics: planted heel-strike impact and knee compression contradict microgravity asset behavior. |
| S01 | 🟠 | zaman 0:11 | ③ | :11 Metal Room No, just floor drop 🟠 MAJOR |
| S03 | 🟠 | zaman 0:30 | ⑤ | :30 Far Field 6 Ceiling-mounted hanging lamps become wall sconces 🟠 MAJOR |
| S03 | 🟠 | zaman 0:29 | ⑧ | :29 Turning hatch crank Bracing, shoulder drop, breathing ①, ② 🟠 MAJOR |
| S04 | 🟠 | zaman 0:44 | ⑤ | :44 Far Field 4 Flat metal wall becomes rough rocky cavern 🟠 MAJOR |
| S04 | 🟠 | zaman 0:44 | ① | :44 — 🟠 MAJOR — Texture swimming/hallucination: rear metal bulkhead panel liquefies and morphs into jagged, organic cave rock mid-shot ( |
| S05 | 🟠 | zaman 0:50 | ② | :50 WORLD N/A 10 Hatch closed, then instantly open again. 🟠 MAJOR |
| S05 | 🟠 | zaman 0:50 | ③ | :50 Metal Room No, just floor drop 🟠 MAJOR |
| S05 | 🟠 | zaman 0:49 | ③ | :49 Ambience 6 Rock cavern tone vs metal room tone levels jump abruptly 🟠 MAJOR |
| S07 | 🔴 | zaman 1:10 | ⑧ | :10 Using small pliers in thick gloves Reduced dexterity, fumbling, visible resistance from glove pressure ⑥, ⑬ 🔴 BLOCKER |
| S08 | 🔴 | zaman 1:19 | ⑧ | :19 7 The visual thickness of the pressurized suit gloves contradicts the bare-hand fine-motor dexterity with which they operate the tiny pliers. 🔴 BLOCKER |
| S08 | 🟠 | zaman 1:20 | ② | :20 BODY The Astronaut 4 Holding pliers, cut to holding a tethered box rig. 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ⑥ | :50 2 Released objects float upward vs dropping slowly downward. 🟠 MAJOR |
| S15 | 🟠 | zaman 2:30 | ⑦ | :30 Could not state what the pliers were achieving or failing to achieve; motion without a readable goal. ⑪ INTENT INVISIBLE 🟠 MAJOR |
| S16 | 🔴 | zaman 2:39 | ⑧ | :39 Pulling heavy rope Forearm engagement, suit deformation under tension, leaning body weight into the pull ①, ⑤ 🔴 BLOCKER |
| S17 | 🟠 | zaman 2:56 | ① | :56 — 🟠 MAJOR — Scale & Physics — Tether physics: horizontal tension cable instantly collapses into a flat, loose spiral on the deck with zero elastic wave propagation. |

## THE_BORROWED_WEIGHT

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 4/4 geçerli · bulgu 20 → tekil 19`

`③ kimlik: 1/4 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🟠 | zaman 0:10 | ③ | :10 Ambience 6 Wind bed drops to digital zero across the cut 🟠 MAJOR |
| S02 | 🟠 | zaman 0:23 | ③ | :23. Prosody and timing are mathematically identical. 🟠 MAJOR |
| S03 | 🟠 | zaman 0:33 | ③ | :33 Voice 2 Exact duplicate sample used for two separate narrative thoughts 🟠 MAJOR |
| S05 | 🔴 | zaman 0:58 | ① | :58 — 🔴 BLOCKER — Character — Contact morphing: Fingers fuse and melt into the metal wrenches as they are picked up. |
| S07 | 🔴 | zaman 1:13 | ① | :13 — 🔴 BLOCKER — Object morphing: The brass scale completely loses structural integrity and dynamically morphs into a different design in the character's hands. |
| S07 | 🔴 | zaman 1:13 | ① | :13 — 🔴 BLOCKER — Scale & Physics — The entire brass scale dynamically morphs, altering its geometry and dial shape mid-shot. |
| S07 | 🔴 | zaman 1:16 | ① | :16 — 🔴 BLOCKER — Character — Contact morphing: Hand holding the upper ring of the scale merges physically with the brass ring. |
| S07 | 🟠 | zaman 1:10 | ② | :10 BODY Astronaut 2 Chest plate changes shape 🟠 MAJOR |
| S10 | 🔴 | zaman 1:43 | ① | :43 — 🔴 BLOCKER — Object phasing: Character's hands push completely through the solid metal geometry of the solar panel. |
| S10 | 🟠 | zaman 1:45 | ① | :45 — 🟠 MAJOR — Particles & Materials — Dust kicked up by the falling panel hovers and freezes statically instead of dispersing. |
| S11 | 🔴 | zaman 1:50 | ② | :50 BODY Astronaut 1 Facial bone structure changes 🔴 BLOCKER |
| S12 | 🔴 | zaman 2:00 | ② | :00 WORLD - 8 Pod scales from tiny to massive 🔴 BLOCKER |
| S13 | 🟠 | zaman 2:10 | ② | :10 BODY Astronaut 4 Brass scale morphs design 🟠 MAJOR |
| S15 | 🔴 | zaman 2:32 | ① | :32 — 🔴 BLOCKER — Character — Contact morphing: Fingers phase through the flat surface of the metal wall being pushed. |
| S18 | 🟠 | zaman 3:04 | ① | :04 — 🟠 MAJOR — Lighting & Color — Severe AI bloom on the small glowing orb, creating a dreamy haze that washes out the suit. |
| S19 | 🟠 | zaman 3:17 | ① | :17 — 🟠 MAJOR — Scale & Physics — The dropped scale falls with balloon-like, low-mass physics that contradicts the established gravity. |
| S20 | 🟠 | zaman 3:20 | ② | :20 BODY Astronaut 3 Dirty knees reset to clean 🟠 MAJOR |
| S21 | 🟠 | zaman 3:30 | ② | :30 WORLD - 9 Daylight instantly becomes night 🟠 MAJOR |
| S23 | 🟠 | zaman 3:51 | ① | :51 — 🟠 MAJOR — Lighting & Color — AI bloom effect present on the glowing cyan hatch in the ground. |

## THE_AMBER_LATTICE

`ızgara hook 0 s · klip 10 s · sahne 10 · ham 12/12 geçerli · bulgu 19 → tekil 18`

`③ kimlik: 3/12 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S02 | 🟠 | zaman 0:10 | ⑧ | :10 Walking in heavy EVA suit Torso lean, heavier stride stance, joint resistance ⑥ 🟠 MAJOR |
| S03 | 🔴 | zaman 0:24 | ① | :24 — 🔴 BLOCKER — Character: Burned-in text visible on the scanner display. |
| S03 | 🔴 | zaman 0:20 | ① | :20 — 🔴 BLOCKER — Character: Hand geometry fuses directly into the scanner casing. |
| S03 | 🔴 | zaman 0:24 | ① | :24 — 🔴 BLOCKER — Character — AI-generated text/symbols appear on the screen. |
| S03 | 🟠 | zaman 0:20 | ⑧ | :20 Pressing scanner into wall Glove tension, forearm muscle flex, shoulder bracing ① 🟠 MAJOR |
| S04 | 🔴 | zaman 0:33 | ⑦ | :33 Whether the astronaut's hand successfully grabbed the exterior panel handle before the edit cut ④ (Action Ellipsis) 🔴 BLOCKER |
| S06 | 🟠 | zaman 0:50 | ① | :50 — 🟠 MAJOR — Camera — Internal reflection on the visor moves independently of head track. |
| S07 | 🟠 | zaman 1:02 | ⑤ | :02 Far Field 4 Open flat plain horizon with distant peaks vs high vertical canyon cliff walls enclosing monolith 🟠 MAJOR |
| S07 | 🟠 | zaman 1:01 | ⑤ | :01 Sky 8 Overcast blue-grey daylight cloud deck in S6 vs deep night sky with stars and nebulae in S7 🟠 MAJOR |
| S07 | 🟠 | ≈S-ref 1:31 | ⑤ | :31 Sky 8 Daytime sky in S8 vs starry night sky overhead in S10 🟠 MAJOR |
| S08 | 🟠 | zaman 1:11 | ⑦ | :11 Whether the drifting tether cable end was successfully secured or missed ⑫ (Stakes Object Off-Screen) / ① (Contact Without Occlusion) 🟠 MAJOR |
| S08 | 🟠 | zaman 1:11 | ⑤ | :11 Sky 8 Deep starry night sky in S7 vs bright daytime sky behind boots in S8 🟠 MAJOR |
| S08 | 🟠 | zaman 1:10 | ① | :10 — 🟠 MAJOR — Particles: Floating rocks lack physical momentum, hanging statically. |
| S08 | 🟠 | zaman 1:10 | ① | :10 — 🟠 MAJOR — Particles & Materials — Suspended debris exhibits frozen, flat 2D behavior. |
| S09 | 🟠 | zaman 1:20 | ⑧ | :20 Bracing against shockwave Torso recoil, leg adjustment, defensive muscle tightening ① 🟠 MAJOR |
| S09 | 🟠 | zaman 1:25 | ⑧ | :25 1 High-energy explosion occurs near feet, but body posture remains identically unbothered as during casual walking 🟠 MAJOR |
| S09 | 🟠 | zaman 1:20 | ① | :20 — 🟠 MAJOR — Character — Right hand holding the emitter shows phantom digits. |
| S09 | 🟠 | zaman 1:25 | ① | :25 — 🟠 MAJOR — Lighting — Excessive AI bloom wash surrounds the energy sphere. |

## THE_SKYLIGHT

`ızgara hook 9 s · klip 10 s · sahne 33 · ham 6/6 geçerli · bulgu 18 → tekil 18`

`③ kimlik: 4/6 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🟠 | zaman 0:14 | ① | :14 — 🟠 MAJOR — Character — Fingers morph and fuse into the rock texture upon contact. |
| S09 | 🟠 | zaman 1:31 | ① | :31 — 🟠 MAJOR — Lighting — The hand lantern emits a diffuse AI bloom rather than directional optical light. |
| S11 | 🟠 | zaman 1:50 | ⑤ | :50 Midground 6 Orange/white striped pole stands next to rock stack; then pole is completely absent from the untouched set. 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ② | :50 WORLD N/A 8 Orange/white pole stands by cairn, then is missing 🟠 MAJOR |
| S12 | 🔴 | zaman 2:07 | ① | :07 — 🔴 BLOCKER — A duplicate astronaut inexplicably spawns on the left side of the frame alongside the original subject. |
| S12 | 🔴 | zaman 2:07 | ① | :07 — 🔴 BLOCKER — Character — Duplicate character appears mid-shot. |
| S13 | 🟠 | zaman 2:14 | ① | :14 — 🟠 MAJOR — Particles & Materials — Falling dust floats and phases through the character's glove instead of colliding. |
| S22 | 🟠 | zaman 3:39 | ① | :39 — 🟠 MAJOR — Motion Quality — Character glides/moonwalks over the terrain without visibly planting feet. |
| S24 | 🟠 | zaman 4:00 | ⑤ | :00 Far field 4 Rocket is on an open plain with distant hills; then rocket is enclosed closely by steep rocky canyon walls. 🟠 MAJOR |
| S24 | 🟠 | zaman 4:00 | ② | :00 WORLD N/A 10 Rocket has single black vertical stripe, then white horizontal band 🟠 MAJOR |
| S25 | 🟠 | zaman 4:10 | ② | :10 BODY Pilot 2 Helmet has opaque sides, then wide clear transparent sides 🟠 MAJOR |
| S25 | 🟠 | zaman 4:10 | ② | :10 BODY Pilot 3 Suit back is heavily soiled, then pristine white 🟠 MAJOR |
| S25 | 🟠 | zaman 4:16 | ① | :16 — 🟠 MAJOR — Character — Hands morph and blend seamlessly into the seatbelt straps. |
| S26 | 🔴 | zaman 4:24 | ① | :24 — 🔴 BLOCKER — Rocket exhaust flames clip entirely through the solid metal landing legs of the vehicle during liftoff. |
| S26 | 🔴 | zaman 4:24 | ① | :24 — 🔴 BLOCKER — Scale & Physics — Exhaust clips through solid objects. |
| S29 | 🟠 | zaman 4:50 | ⑥ | :50 9 Floating bolts indicate a 0g environment, but the astronaut's body, harness, and suit are entirely rigid, reacting to 1g physics without micro-motion. 🟠 MAJOR |
| S29 | 🟠 | zaman 4:52 | ① | :52 — 🟠 MAJOR — The floating bolt indicates a zero-g environment, but the character remains perfectly rigid in the seat with zero limb drift or micro-motion. |
| S29 | 🟠 | zaman 4:52 | ① | :52 — 🟠 MAJOR — Scale & Physics — Rigid 1g character model suspended in zero-g environment. |

## THE_LEANING_ROOM

`ızgara hook 10 s · klip 10 s · sahne 12 · ham 8/8 geçerli · bulgu 19 → tekil 17`

`③ kimlik: 0/8 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🟠 | zaman 0:10 | ① | :10 — 🟠 — Texture hallucination. The icy planet outside fades into existence from empty black space. |
| S01 | 🟠 | zaman 0:10 | ① | :10 🟠 Environment — icy moon fades into existence from empty black. |
| S02 | 🟠 | zaman 0:20 | ② | :20 · BODY · cat 2 · thin left bracelet vs wide right cuff · 🟠 |
| S05 | 🔴 | zaman 0:50 | ② | :50 · WORLD · cat 8 · Saturn-like planet vs giant Jupiter · 🔴 |
| S05 | 🟠 | zaman 0:52 | ① | :52 🟠 Scale & Physics — taut rope bends and clips through the brass lampshade. |
| S06 | 🔴 | zaman 1:00 | ② | :00 · WORLD · cat 8 · giant Jupiter vs eclipse ring · 🔴 |
| S06 | 🟠 | zaman 1:00 | ② | :00 · BODY · cat 2 · wide right cuff vs thin right bracelet · 🟠 |
| S07 | 🔴 | zaman 1:17 | ⑥ · ① | :17 · cat 1 · stone drops at 1g; background object falls diagonally upwards · 🔴 |
| S07 | 🔴 | zaman 1:17 | ① | :17 — 🔴 — Impossible physics. An object in the lower-left background falls diagonally UPWARDS and leftwards, defying the established 1g room gravity. |
| S07 | 🟠 | zaman 1:10 | ② | :10 · BODY · cat 2 · thin right bracelet vs thin left bracelet · 🟠 |
| S07 | 🟠 | zaman 1:10 | ② | :10 · WORLD · cat 10 · flat horizontal dial wheel vs vertical ship's wheel · 🟠 |
| S07 | 🟠 | zaman 1:17 | ① · ③ | :17 🟠 Dialogue & Audio — clatter SFX plays while the object flies upward. |
| S08 | 🔴 | zaman 1:20 | ② | :20 · WORLD · cat 8 · eclipse ring vs giant Jupiter · 🔴 |
| S09 | 🟠 | zaman 1:30 | ⑥ | :30 · cat 4 · rope rigid when pulled, flexible as a pendulum later · 🟠 |
| S10 | 🔴 | zaman 1:44 | ① | :44 — 🔴 — Hand-surface fusion. Fingers of the left hand melt and fuse into the small stones on the table. |
| S10 | 🟠 | zaman 1:44 | ① | :44 🟠 Environment — stones morph and melt into one another. |
| S10 | 🟠 | zaman 1:45 | ③ | :45 · SFX/visual · cat 7 · stone clink delayed vs hand contact · 🟠 |

## THE_GRAVITY_ANCHOR

`ızgara hook 10 s · klip 10 s · sahne 10 · ham 11/11 geçerli · bulgu 16 → tekil 16`

`③ kimlik: 2/11 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🟠 | zaman 0:18 | ⑤ | :18 Sky/Atmosphere 8 S1 heavy falling snow flurries vanish into static fog haze in S4 🟠 MAJOR |
| S01 | 🟠 | zaman 0:10 | ⑧ | :10 Operating wrist device in heavy suit Forearm stiffness, glove resistance, neck bending restricted by helmet ring ⑥ The suit that isn't there 🟠 MAJOR |
| S01 | 🟠 | zaman 0:18 | ① | :18 — 🟠 MAJOR — Suit drift. Wrist device is a rectangular screen. |
| S02 | 🟠 | zaman 0:23 | ① | :23 — 🟠 MAJOR — Environment texture swimming. The rainbow refraction on the monolith morphs and breathes independently of camera movement. |
| S03 | 🔴 | zaman 0:30 | ⑧ | :30 Reaching arm up to alien monolith Shoulder lift compensation, torso tilt, suit joint tightness ① Effortless heavy / ⑥ Suit burden 🔴 BLOCKER |
| S03 | 🔴 | zaman 0:35 | ⑧ | :35 Pressing gloved hand against monolith Forearm tendon tension, finger flex against pressurized glove, bracing ⑤ Grip that never fails / ⑥ Suit burden 🔴 BLOCKER |
| S03 | 🔴 | zaman 0:30 | ① | :30 — 🔴 BLOCKER — Compilation mode. Interior/exterior or radical focal jump. The extreme macro shot of the wrist device breaks the spatial continuum established in the previous wide shots. |
| S03 | 🟠 | zaman 0:32 | ⑤ | :32 Far Field 4 S0 upper horizon pine cluster silhouette does not match S7 wide shot skyline 🟠 MAJOR |
| S03 | 🟠 | zaman 0:30 | ① | :30 — 🟠 MAJOR — Suit drift. Wrist device changes to a circular glowing 'M' or 'W' logo. |
| S04 | 🟠 | zaman 0:41 | ⑤ | :41 Midground 5 S2 background tree depth layer compresses directly against structure wall in S9 🟠 MAJOR |
| S04 | 🟠 | zaman 0:40 | ① | :40 — 🟠 MAJOR — Particle physics violation. Rising rocks move linearly like 2D assets without collision logic or realistic tumbling momentum. |
| S04 | 🟠 | zaman 0:41 | ① | :41 — 🟠 MAJOR — Floating debris lacks micro-rotation. The smaller pebbles rise rigidly without individual axis spin. |
| S05 | 🟠 | zaman 0:50 | ⑧ | :50 Exhaling relief breath at sequence end Visor condensation/fogging, subtle chest/shoulder drop from fatigue ⑩ Breath that doesn't track work / ⑭ Cost without source 🟠 MAJOR |
| S06 | 🟠 | zaman 1:01 | ① | :01 — 🟠 MAJOR — Suit drift. Wrist device vanishes entirely during wide touch shot. |
| S07 | 🟠 | zaman 1:10 | ① | :10 — 🟠 MAJOR — Face drift. Bone structure and skin texture soften significantly compared to wider shots; artificial "AI skin" appearance. |
| S08 | 🟠 | zaman 1:20 | ① | :20 — 🟠 MAJOR — Lighting physics. A single, distinct, hard shadow is cast directly to the right by the astronaut and monolith, but two distinct suns are visible straight ahead. A second shadow is missing. |

## THE_ROSE_COAT

`ızgara hook 0 s · klip 10 s · sahne 13 · ham 5/5 geçerli · bulgu 15 → tekil 15`

`③ kimlik: 0/5 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🔴 | zaman 0:03 | ① | :03 — 🔴 BLOCKER — Impossible physics: Sand pours out of a flat geometric |
| S00 | 🔴 | zaman 0:03 | ① | :03 — 🔴 BLOCKER — Scale & Physics — Sand pours continuously from a narrow |
| S01 | 🔴 | zaman 0:12 | ① | :12 — 🔴 BLOCKER — Motion Quality — The character slides/moonwalks across the |
| S02 | 🟠 | zaman 0:22 | ① | :22 — 🟠 MAJOR — Lighting — Shadow mismatch: The deep shadow cast by the buried |
| S03 | 🟠 | zaman 0:32 | ① | :32 — 🟠 MAJOR — Motion Quality — Pronounced jello/glide effect during the walk |
| S04 | 🔴 | zaman 0:45 | ① | :45 — 🔴 BLOCKER — Scale & Physics — The physical brush phases entirely through |
| S05 | 🟠 | zaman 0:55 | ① | :55 — 🟠 MAJOR — Particles & Materials — Sand falling off the hull behaves as a |
| S06 | 🔴 | zaman 1:05 | ① | :05 — 🔴 BLOCKER — Character — Anatomical breakdown: As the character ascends |
| S07 | 🔴 | zaman 1:18 | ① | :18 — 🔴 BLOCKER — Text visible on screen: The word "rose" clearly appears |
| S07 | 🔴 | zaman 1:18 | ① | :18 — 🔴 BLOCKER — Character — The word "rose" spontaneously generates on the |
| S07 | 🟠 | zaman 1:13 | ① | :13 — 🟠 MAJOR — Scale & Physics — Impact lacks weight: The astronaut's fall |
| S08 | 🔴 | zaman 1:25 | ① | :25 — 🔴 BLOCKER — Particles & Materials — Solid passing through solid: The |
| S09 | 🔴 | zaman 1:33 | ① | :33 — 🔴 BLOCKER — Environment — Texture swimming: As the astronaut brushes the |
| S12 | 🔴 | zaman 2:02 | ① | :02 — 🔴 BLOCKER — Contact morphing: While climbing the ladder, the |
| S12 | 🔴 | zaman 2:02 | ① | :02 — 🔴 BLOCKER — Character — Contact morphing: Hands phase directly through |

## THE_SHATTERED_BREATH

`ızgara hook 0 s · klip 10 s · sahne 12 · ham 12/12 geçerli · bulgu 13 → tekil 13`

`③ kimlik: 0/12 güçlü bayrak · üretim defter: ⬜0 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🟠 | zaman 0:05 | ① | :05 — 🟠 MAJOR — Surface rock texture breathes and swims along glowing magma fissures. |
| S01 | 🔴 | zaman 0:19 | ⑧ | :19 Twisting heavy core into ground cavity Forearm muscle flexing, back rounding, torque resistance, rate decay Pattern ① (Effortless Heavy) 🔴 BLOCKER |
| S02 | 🟠 | zaman 0:29 | ⑤ | :29 Sky 8 Giant planet limb fills upper background in S3, completely absent in S4, S7, S12 🟠 MAJOR |
| S02 | 🟠 | zaman 0:29 | ⑧ | :29 Hovering boots off ground grid Ankle micro-stabilization, knee dampening, core muscle tension Pattern ⑤ (Grip/Stance That Never Fails) 🟠 MAJOR |
| S02 | 🟠 | zaman 0:20 | ① | :20 — 🟠 MAJOR — Steam/smoke drifts upward linearly despite vacuum background and zero-g floating stance. |
| S02 | 🟠 | zaman 0:25 | ① | :25 — 🟠 MAJOR — Volumetric steam around boots lacks realistic dispersion in airless/low-pressure environment. |
| S03 | 🟠 | zaman 0:30 | ① | :30 — 🟠 MAJOR — Suit chest harness morphs into bright glowing orange X-structure, contradicting the earlier suit layout. |
| S03 | 🟠 | zaman 0:30 | ① | :30 — 🟠 MAJOR — Soft AI bloom/haze around suit chest harness and pedestal. |
| S04 | 🟠 | zaman 0:40 | ① | :40 — 🟠 MAJOR — Circular platform edge texture morphs as vortex rotates. |
| S07 | 🔴 | zaman 1:19 | ⑧ | :19 Raising pressurized EVA suit arm Joint resistance in suit elbow/shoulder, shoulder elevation Pattern ⑥ (The Suit That Isn't There) 🔴 BLOCKER |
| S08 | 🟠 | zaman 1:29 | ⑧ | :29 Rotating mechanical chest dial Forearm strain, glove creasing under torque, finger pressure Pattern ⑥ (The Suit That Isn't There) 🟠 MAJOR |
| S10 | 🟠 | zaman 1:49 | ⑧ | :49 Exhaustion eye closure Spine/neck sag, shoulder droop, head tilt Pattern ⑦ (Pain/Fatigue Without Duration) 🟠 MAJOR |
| S11 | 🟠 | zaman 1:59 | ⑤ | :59 Edge 9 Generator logo watermark sits static in bottom-right corner across all shots 🟠 MAJOR |

## THE_GREEN_CEILING

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 11/12 geçerli · bulgu 12 → tekil 12`

`③ kimlik: 6/12 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🟠 | zaman 0:04 | ① | :04 — 🟠 MAJOR — Contact morphing: fingers merge into case handles. |
| S01 | 🔴 | zaman 0:10 | ⑥ | :10 1 Rain falls at real-time speeds while tablet floats mid-air in the same medium. 🔴 |
| S05 | 🔴 | zaman 0:50 | ⑥ | :50 1 Rain falls normally while nail experiences extreme slow-motion/float. 🔴 |
| S05 | 🟠 | zaman 0:50 | ① | :50 — 🟠 MAJOR — Zero-G micro-motion failure: floating pin remains rigidly static in space instead of maintaining continuous subtle axis rotation. |
| S07 | 🟠 | zaman 1:12 | ① | :12 — 🟠 MAJOR — Characters exhibit artificial slow-motion AI drift in their walk cycle rather than natural human gait pacing. |
| S09 | 🟠 | zaman 1:30 | ① | :30 — 🟠 MAJOR — Floating leaves exhibit rigid 2D planar hovering rather than realistic physical momentum. |
| S10 | 🟠 | zaman 1:44 | ① | :44 — 🟠 MAJOR — Suit material lacks proper cloth simulation or creasing during steps on the ramp. |
| S14 | 🟠 | zaman 2:23 | ① | :23 — 🟠 MAJOR — Low-density impact physics: Pod exhaust produces lightweight CGI bloom without terrain deformation or realistic ejecta. |
| S14 | 🟠 | zaman 2:23 | ① | :23 — 🟠 MAJOR — AI Bloom: Pod exhaust and undercarriage emit a soft, diffuse haze instead of sharp directional light. |
| S14 | 🟠 | zaman 2:24 | ① | :24 — 🟠 MAJOR — Exhaust smoke behaves as a planar overlay, lacking volumetric mass and failing to interact with the forest floor. |
| S15 | 🟠 | zaman 2:31 | ① | :31 — 🟠 MAJOR — Airbrushed plastic skin: faces inside the pod lack pore texture and subsurface scattering. |
| S19 | 🟠 | zaman 3:10 | ① | :10 — 🟠 MAJOR — Contact morphing: gloves lose structural integrity upon touching the case lock. |

## THE_HEALING_GROUND

`ızgara hook 9 s · klip 10 s · sahne 14 · ham 7/7 geçerli · bulgu 11 → tekil 11`

`③ kimlik: 0/7 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🟠 | zaman 0:00 | ⑧ | :00 Pressing disk into hard earth Shoulder lock, body weight transfer, braced core ① EFFORTLESS HEAVY 🟠 MAJOR |
| S00 | 🟠 | zaman 0:08 | ⑧ | :08 The action of pushing the disk requires force, but the character's posture (upright, arms casually extended) contradicts the physical requirement of the task. 🟠 MAJOR |
| S03 | 🟠 | zaman 0:37 | ① | :37 — 🟠 MAJOR — Fingers on right hand merge with the chest suit material. |
| S03 | 🟠 | zaman 0:37 | ① | :37 — 🟠 MAJOR — Character — Fingers merge with suit. |
| S06 | 🟠 | zaman 0:59 | ② | :59 BODY Astronaut 2 Suit in S1 has 4 yellow bands and top helmet lights; S7 has 1 yellow band on right arm only and smooth helmet. 🟠 MAJOR |
| S09 | 🟠 | zaman 1:29 | ⑧ | :29 Pushing rod into sand Forearm tension, micro-pauses, wrist adjustment ① EFFORTLESS HEAVY 🟠 MAJOR |
| S10 | 🟠 | zaman 1:39 | ② | :39 BODY Astronaut 2 Suit in S1 has yellow bands and ribbed chest box; S11 has zero yellow bands, flat pad chest box, and different helmet lights. 🟠 MAJOR |
| S11 | 🟠 | zaman 1:50 | ⑤ | :50 Midground 6 S2 establishes a single receding line of domes; S12 shows two symmetrical flanking rows of domes behind the kneeling subject. 🟠 |
| S11 | 🟠 | zaman 1:55 | ① | :55 — 🟠 MAJOR — Lip sync is minimal and stiff; mouth lacks proper articulation. |
| S11 | 🟠 | zaman 1:55 | ① | :55 — 🟠 MAJOR — Dialogue & Audio — Stiff lip sync. |
| S13 | 🟠 | zaman 2:09 | ② | :09 BODY Astronaut 2 Suit in S1 has chest box and helmet lights; S14 lacks the chest box entirely and helmet has no lights. 🟠 MAJOR |

## THE_SILENT_PERIHELION

`ızgara hook 0 s · klip 10 s · sahne 12 · ham 12/12 geçerli · bulgu 11 → tekil 11`

`③ kimlik: 5/12 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S02 | 🟠 | zaman 0:10 | ① | :10 — 🟠 MAJOR — Burned-in HUD text overlay on viewport glass. |
| S03 | 🟠 | zaman 0:22 | ① | :22 — 🟠 MAJOR — Gloved fingers slightly deform and phase into button surfaces during panel interaction. |
| S05 | 🟠 | zaman 0:45 | ① | :45 — 🟠 MAJOR — Hand movement over switches demonstrates micro-flicker and temporal stutter. |
| S06 | 🟠 | zaman 0:52 | ① | :52 — 🟠 MAJOR — Manual lever pulling lacks physical resistance or mechanical mass transfer. |
| S07 | 🟠 | zaman 1:00 | ⑧ | :00 Transition after heavy mechanical pull Visible chest heave, visor breath condensation, resting arm posture ③, ⑩ 🟠 MAJOR |
| S07 | 🟠 | zaman 1:02 | ① | :02 — 🟠 MAJOR — Red internal electrical arc lighting lacks directional cast on cheekbones. |
| S08 | 🟠 | zaman 1:19 | ⑧ | :19 Enduring high thermal shock / visor crack Heavy breathing fog on inner helmet glass ⑩ 🟠 MAJOR |
| S08 | 🟠 | zaman 1:10 | ① | :10 — 🟠 MAJOR — Visor glass cracks instantly generate as a static overlay without impact particles. |
| S09 | 🟠 | zaman 1:27 | ⑤ | :27 Sky / Far Sky & Atmospherics Massive red solar prominence loop behind megastructure dissolves mid-shot into flat red background glow 🟠 MAJOR |
| S10 | 🟠 | zaman 1:36 | ① | :36 — 🟠 MAJOR — Static noise effect maps as a flat 2D texture across rounded helmet visor glass. |
| S11 | 🟠 | zaman 1:40 | ⑤ | :40 Far Field Horizon & Topology Deep space megastructure mutates from a featureless flat black monolithic slab (S9) to a relief-carved geometric octahedron (S11) 🟠 MAJOR |

## THE_BENT_GRASS

`ızgara hook 10 s · klip 10 s · sahne 14 · ham 11/11 geçerli · bulgu 9 → tekil 8`

`③ kimlik: 0/11 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S00 | 🟠 | ≈S-ref — | ⑪ | S1 → S2 PLAIN Key direction lost (9 → ?); temperature cools (warm → neutral); subject exposure drops (bright → mid) no 🟠 MAJOR |
| S01 | 🔴 | ≈S-ref — | ⑪ | S2 → S3 PLAIN Key direction returns but flips sides (3); temperature warms back up; exposure rises no 🔴 BLOCKER |
| S05 | 🟠 | ≈S-ref — | ⑪ | S6 → S7 PLAIN Key direction lost (9 → ?); temperature cools; exposure drops no 🟠 MAJOR |
| S06 | 🟠 | zaman 1:00 | ⑧ | :00 carrying loaded case asymmetric shoulder drop, slower arm swing ⑨ SYMMETRIC BODY UNDER ASYMMETRIC LOAD 🟠 MAJOR |
| S07 | 🟠 | zaman 1:18 | ⑤ · ① | :18 Midground 1 Middle hippo creature in the background has merged/clipping 5-leg geometry that persists through the shot. 🟠 MAJOR |
| S07 | 🟠 | zaman 1:10 | ① | :10 — 🟠 MAJOR — Creatures — The middle hippo creature in the background has a merged or extra fifth leg (Object phasing/clipping). |
| S13 | 🔴 | zaman 2:10 | ① | :10 — 🔴 BLOCKER — Title card with burned-in text appears, replacing the final scene. Text is strictly forbidden. |
| S13 | 🔴 | zaman 2:10 | ① | :10 — 🔴 BLOCKER — Dialogue & Audio — Burned-in text appears on a title card ("THE BENT GRASS HERE REMEMBERS EVERY STEP"). |

## THE_COLD_WELD

`ızgara hook 0 s · klip 10 s · sahne 15 · ham 6/6 geçerli · bulgu 9 → tekil 8`

`③ kimlik: 0/6 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S01 | 🔴 | zaman 0:10 | ① | :10 — 🔴 BLOCKER — Airborne sound propagating in a vacuum (audible footsteps/clanking). |
| S08 | 🟠 | zaman 1:20 | ⑥ | :20 6 Wrench scale shifts from small one-handed tool to massive two-handed lever 🟠 |
| S09 | 🔴 | zaman 1:31 | ① | :31 — 🔴 BLOCKER — Object phasing (wrench head clips entirely through the metal bolt). |
| S09 | 🔴 | zaman 1:31 | ① | :31 — 🔴 BLOCKER — Character — Glove and wrench head phase through the metal surface. |
| S09 | 🟠 | zaman 1:39 | ⑤ | :39 Far 4 Flat horizon becomes vertical wall 🟠 |
| S09 | 🟠 | zaman 1:30 | ② | :30 BODY The Astronaut 4 Wrench orientation and grip change instantly across cut 🟠 |
| S11 | 🟠 | zaman 1:50 | ① | :50 — 🟠 MAJOR — Physics — Heavy metal plates float upwards against established gravity. |
| S14 | 🟠 | zaman 2:20 | ① | :20 — 🟠 MAJOR — Particles & Materials — Dropped disc lacks appropriate low-g momentum/impact. |

## THE_MIRROR_FAUNA

`ızgara hook 9 s · klip 10 s · sahne 15 · ham 8/8 geçerli · bulgu 6 → tekil 6`

`③ kimlik: 0/8 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S07 | 🟠 | zaman 1:11 | ① | :11 — 🟠 MAJOR — The astronaut's left hand fuses and melts into the handle of the flare/laser device during use. |
| S10 | 🟠 | zaman 1:40 | ⑪ | :40 TRAPPIST-1e Right-key → full silhouette backlight No 🟠 MAJOR |
| S11 | 🔴 | zaman 1:50 | ⑪ | :50 TRAPPIST-1e Unmotivated red strobe inside helmet No 🔴 BLOCKER |
| S11 | 🔴 | zaman 1:52 | ① | :52 — 🔴 BLOCKER — Red text and data characters are baked into the glowing visor HUD display, violating the strict no-text rule. |
| S12 | 🔴 | zaman 2:00 | ① | :00 — 🔴 BLOCKER — The edit inserts an exact duplicate of the previous |
| S13 | 🟠 | zaman 2:10 | ⑪ | :10 TRAPPIST-1e Red tint remains on face No 🟠 MAJOR |

## THE_HARD_DOCK

`ızgara hook 0 s · klip 10 s · sahne 24 · ham 12/12 geçerli · bulgu 5 → tekil 5`

`③ kimlik: 1/12 güçlü bayrak · üretim defter: ⬜19 ✅1`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S06 | 🟠 | zaman 0:58 | ⑤ | :58 Far Field 5 Capsule craft and background planet surface move with zero relative parallax displacement. 🟠 MAJOR |
| S12 | 🟠 | zaman 1:55 | ⑤ | :55 Midground 6 Circular porthole window rim changes bolt count from 8 to 10 perimeter bolts. 🟠 MAJOR |
| S13 | 🟠 | zaman 2:05 | ⑤ | :05 Far Field 4 Magma fissure topology shifts from uniform grid to large central volcanic peak. 🟠 MAJOR |
| S21 | 🔴 | zaman 3:20 | ① | :20: BLOCKER spatial orientation cut mismatch, solar panel jitter |
| S22 | 🟠 | zaman 3:37 | ⑦ | :37 The exact physical contact, alignment, and mechanical latching of the docking ring onto the station capture collar ④ THE ACTION ELLIPSIS / ⑫ STAKES OBJECT OFF-SCREEN AT DECISIVE MOMENT 🟠 MAJOR |

## LOSS_OF_LIFT

`ızgara hook 9 s · klip 10 s · sahne 25 · ham 2/2 geçerli · bulgu 1 → tekil 1`

`③ kimlik: 0/2 güçlü bayrak · üretim defter yok`

| S | ş | çapa | gören mercek | bulgu |
|---|:--:|---|---|---|
| S19 | 🟠 | zaman 3:09 | ② | :09 Props The gas rack in S11 has ~12 small nozzles in a row. The rack in S20 has ~6 large cylinders. 🟠 MAJOR |

