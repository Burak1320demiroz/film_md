# 📋 THE PAYLOAD — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün
> eline rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

> ⛔ **ÖLÇÜM SATIRI DA YAPIŞTIRILIR [Ders 137]:** ⑪ ölçüm kapısının
> `SES KANALI: VAR/YOK · −x LUFS · tepe −y dBTP` satırı rubriğin künyesine
> eklenmeden ses ekseni ÖLÇÜLMEMİŞTİR.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU yapıştırılır            MOD D
④ 📖 HİKAYE      → A BLOĞU yapıştırılır                MOD D
② 🔗 DEVAMLILIK  → ⛔ HİÇBİR ŞEY (baseline: videodan sahne envanteri
                                  + karakter pasaportu)
③ 🔊 SES         → ⛔ HİÇBİR ŞEY (baseline: kurgudan ses defteri)
                   + ⑪ ölçüm satırı künyeye [D137]

⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ şu üç kilidi: mekân ölçüleri /
                   ışık takvimi · ekran yönü · sabit çevre nesneleri
                   (panel sıraları · üs · pist · mast · kasalar ·
                   gemi ve rıhtımlar) [Ders 133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri (g · basınç · fırtına ·
                   kalkış · 0 g · yanaşma · amortisör)
⛔ ⑤ ve ⑥'ya kimlik, kostüm ve olay kilitleri VERİLMEZ — o körlük
   tasarımdır.
⛔ ② ve ③'e belge vermek yasaktır — eksikliği değil, TASARIMI bozar.
   FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⛔ Her mercek AYRI ve TEMİZ sohbette [D110].
⛔ Dördüne de AYNI video dosyası verilir [D75] — filigransız, kartsız,
   −14 LUFS master [D150 · D70/72 · KURGU_RITMI §6].
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:                 THE PAYLOAD
FORMAT:               3-5dk
RUNTIME:              239 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:          24  (S0-S23)
REVIEW INPUT:         video only

LOGLINE (intended):   A man who has spent nine years on Mars packing rock
                      into cases is wiping dust off a solar field when a
                      regional dust storm takes the light row by row. The
                      outpost is finished, and the only ride off the planet
                      is an uncrewed sample-return boat sized for its
                      cargo, not for a person: it lifts a fixed mass, and
                      the mass is already loaded. He walks to the pad, takes
                      the nine sample cases out of the bay one at a time and
                      stands them upright in the dust, lies down in the
                      empty cargo cradle, locks a freight strap across his
                      own chest — and the boat lifts on schedule, leaving
                      nine years of work standing under its exhaust. In
                      orbit an unlit interstellar carrier takes him the way
                      it takes freight: four clamps, in sequence, on the
                      twelfth of twelve identical berths.
THEME (intended):     The human-machine boundary. Sentence: "The machine
                      does not know whom it carries — only how much."
                      (⛔ NOT the trade pattern [TEMA §3c] — the sentence
                      names what the machine knows, not what is sacrificed.)
THEME SCENES:         S5 (a bay with no seat, four identical clamp cradles)
                      · S6 (the mast steps down on its own schedule) ·
                      S10 (the nine cases standing — the mass he traded) ·
                      S11 (he straps himself with a freight strap) ·
                      S12 (the machine lifts the mass, not the man) ·
                      S17 (the carrier is unlit; nothing is waiting) ·
                      S21 (four clamps close on him as freight) ·
                      S23 (one lit port on a dark hull)
INTENDED EMOTION:     pressure and physical urgency (S0-S12), then awe at
                      S18, then a settled, unjudged quiet — not triumph,
                      not grief. The viewer arrives asking "what is he
                      going to save?", stays asking "will he really leave
                      the cases?", leaves asking "nine years or my own
                      life — would I?"
ENDING TYPE:          OPEN (visual dilemma) + seed payoff — S23 mirrors S0:
                      in both, a vast indifferent mass fills the frame and
                      one small human sign sits inside it. His fate is
                      CLEAR (alive, berthed, attached to a ship that is
                      leaving); the open question is what he has become to
                      the machine that carries him. Open questions at the
                      end: 1.

PROTAGONIST:          sample curator, male, 44, unnamed in prompts.
                      Wants: to be on the carrier when it passes.
                      Fears: nothing performed — no panic in any frame; his
                      only hesitation is S10 (two seconds looking down the
                      row of cases).
ANTAGONIST/FORCE:     no villain — a storm that cannot touch him and a mass
                      budget that cannot be argued with. Nothing attacks;
                      the light goes out and the numbers do not move.
CENTRAL CHOICE:       S7-S10 — he takes the nine sample cases out of the
                      cargo bay with his own hands and stands them in the
                      dust. The cost is visible in S10 (the row) and again
                      in S12 (the same row under the exhaust).

DIALOGUE LINES:       0 — the film is fully silent (human 0 · machine 0 ·
                      radio 0)
SILENT SCENES:        24
AUDIO REGISTER:       HUMAN: breath only (all scenes) · MACHINE: 0
MUSIC (post, 31.08): written, two alternative scores — ONE goes into the
                      edit. A-SCORE (THE_PAYLOAD_MUZIK.md): anempathetic
                      counting tick, 72 BPM S1-S11 (twelve beats per scene,
                      the twelfth never played) · 96 BPM S12-S14 and
                      S16-S18 · free-time coda S22-S23. NO MUSIC: 0:00-0:09
                      (hook) · 2:26.5-2:39 (MECO) · 3:06.5-3:39 (last burn,
                      CONTACT and the four clamps). The only resolution is
                      at 3:55.0 — the twelfth tick, on the frame where the
                      port lights. V2 (THE_PAYLOAD_MUZIK_V2_VIRAL.md): one
                      120 BPM grid, drop on the ignition at 2:03.0, MECO
                      cut one bar, silence 3:17-3:39, same coda. Beds are
                      continuous in both, no digital zero [D83/D136].
VIRAL INTERSTITIALS:  S0 · S3 · S10 · S11 · S12 · S18 · S20 · S23
                      ⛔ MAY NOT BE CUT
COVER/THUMBNAIL:      S0 at 0:07 — the storm's shadow edge cutting the
                      twelve panel rows, the tiny man at the near row, the
                      boat small in the right third. Promise: "the light is
                      going out on Mars, and one man has somewhere to be."
                      Inside the 0:00-0:10 band. Plan B = S12 (launch with
                      the nine cases standing) · Plan C = S18 (proportion).
TITLE:                THE PAYLOAD — the film's own rule: what is carried
                      and what is not. The title tells the viewer to watch
                      the cargo; the film answers at S11.
LIBRARY CONTEXT:      3-5 dk shelf siblings: LOW POWER (Mars, greenhouse,
                      sacrifice) · THE SKYLIGHT (Mars, lava tube, time; its
                      PART C is a calm departure coda) · THE FROST LINE
                      (Mars, greenhouse seam, identity) · THE COLD BURN /
                      THE BLACK CRADLE / THE BLUE DRIFT (docking films with
                      two people and radio dialogue). This film differs:
                      the storm cannot touch anything, the vehicle has no
                      seat, the docking is a FREIGHT berthing with no one
                      waiting, the choice is to save himself rather than
                      the work, and nobody speaks at all.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      24          (sahne = çekim = klip; üçü eşit)
SHOT COUNT:      24 · 0 sahne içi kesme
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok; gerekçe: 24 × 10 s
                 tek-çekim disiplini, tek kurgu müdahalesi S0 kırpması
                 10→9) [D74 gerekçe satırı]
GRID:            başlangıç(S0) = 0 · başlangıç(S_n) = 9 s + (n−1) × 10 s
RUNTIME:         239 s   (Hook 9 s + 23 × 10 s) — 3:59
RAW FOOTAGE:     240 s · TRIM BUDGET: 1 s (yalnız S0 10→9)
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı, KAPAK
                 çıktısı YOK; filigran 0 kare [D150]
CAMERA:          24/24 sabit lockoff · klip içi pan/tilt/zoom/dolly 0
SETUP SEQUENCE:  13 kurulum, plandan [ACI_YAYI §4 — promptlarda lens ·
                 yükseklik · mesafe okunur biçimde yazılı]:
                 A 24mm berm 3 m/60 m EWS üst (S0) · B 40mm göğüs/3 m MS
                 göz (S1·S9) · C 32mm bel/12 m WS göz — kamera hedefte
                 (S2) · D 28mm diz/3 m MS alt (S3·S7) · E 50mm diz/0.8 m
                 CU alt (S4·S8) · F 35mm kask/1.2 m MS OTS (S5·S17·S19) ·
                 G 24mm 0.5 m/12 m WS alt (S6·S10) · H 50mm 0.8 m/2 m MS
                 üst (S11·S13·S15·S22) · I 50mm göz/0.6 m CU göz (S14) ·
                 K 32mm 60 m WS göz (S16·S18·S23) · M 32mm bel/80 m WS göz
                 (S12) · N 35mm 12 m WS alt (S20) · O 85mm 3 m CU göz (S21)
                 ⚠️ 13 kurulum, bant 12 — bilinçli sapma, gerekçe planda
                 [D74]: dört ayrı ortam + yanaşmanın zorunlu vuruş seti.
SCALE LADDER:    EWS·MS·WS·MS·CU·MS·WS·MS·CU·MS·WS·MS·WS·MS·CU·MS·WS·MS·
                 WS·MS·WS·CU·MS·WS — her kesme tam 1 kademe; iki bilinçli
                 ŞOK: S0→S1 (EWS→MS) · S20→S21 (WS→CU)
ANGLE ARC:       açı TİPİ 4: üst (A·H) · göz hizası (B·C·I·K·M·O) · alt
                 (D·E·G·N) · omuz üstü (F) [KAMERA_ACISI §2 ✅ ≥3]
EŞ KADRAJ (bilinçli afinite — tek değişken kuralı):
                 S11↔S13↔S15↔S22 (yük yatağı: yatma → ivme → 0 g → temas
                 sonrası) · S17↔S19 (lomboz: gemi uzak → gemi camı
                 dolduruyor) · S16↔S18↔S23 (uzay genişi: tek gövde → iki
                 gövde → kenetli) · S4↔S8 (amortisör: iki parmak → bir el)
REPLİK ZAMANLARI: — (replik 0; hizalama kapısı ⑨ sessiz filmde ızgara
                 dilim birleşimiyle koşulur [D115])
KATALİZÖR:       S0 → 0:02.5 (gölge hattı panel sıralarını söndürür)
NOVUM KURULUM:   S4 → 0:39-0:49 (amortisör: iki parmak)
TOHUM:           S3 → 0:29-0:39 (açık yük kapağı + kasa rafı, ~2 s,
                 vurgusuz) [FINAL §3 penceresi 25-38 s ✅]
NOVUM DOĞRULAMA: S8 → 1:19-1:29 (amortisör: bir el)
ORTA NOKTA:      S12 → başlangıç 119 s (1:59 — formülden [D122]);
                 mastın son adımı T+2.0 ≈ 2:01 · ATEŞLEME T+3.5 ≈ 2:02.5 ·
                 yerden kesilme T+4.5 ≈ 2:03.5 · kadrajı terk T+9 ≈ 2:08
HER ŞEYİN KAYBI: S17 → başlangıç 169 s (2:49); "hiçbir ışık yanmıyor"
                 T+6 ≈ 2:55
HUŞU / PAYLAŞIM: S18 → başlangıç 179 s (2:59)
DÖNÜŞÜ OLMAYAN NOKTA: S19 → 189 s (3:09); iki fren nefesi T+2.5 ≈ 3:11.5
DORUK:           S20 → başlangıç 199 s (3:19 — formülden [D122]);
                 TEMAS T+6.0 ≈ 3:25.0 · oturma ve durma T+7 ≈ 3:26 ·
                 tutulan nefesin bırakılışı T+6.5-7.5
KENET:           S21 → 209 s (3:29); kelepçe 1 T+1.5 ≈ 3:30.5 · 2 T+3.5 ·
                 3 T+5.5 (yarım saniye duraksama) · 4 T+8.0 ≈ 3:37
FİNAL VURUŞ KANITI [Ders 141]: tek kare 235 s (S23 · T+6):
                 · RIHTIM: 12 adet, hepsi kadrajda sayılabilir
                 · DOLU KASA RAFI: 11 adet
                 · KENETLİ TEKNE: 1 adet (on ikinci rıhtımda)
                 · YANAN IŞIK: 1 adet (teknenin lombozu) — gemide başka
                   yanan ışık 0
                 · FİGÜR: 0 adet
                 ffmpeg -ss 235 -i "$M" -frames:v 1 kanit.jpg
                 Kanıt: "on iki rıhtım, on bir dolu, bir tekne, bir ışık,
                 sıfır figür" — beşi sayılamıyorsa final teslim edilmemiştir.
                 DÖNGÜ: uygulanmaz (yatay) — S0/S23 ölçek aynasıdır, kadraj
                 aynası değil; arkasına eklenen her kare (kart dâhil) 🔴
                 [D70/72].
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  111111111111011101010010
       24 karakter — 18 İNSANLI, 6 İNSANSIZ.
       İnsansız: S12 (kalkış) · S16 (yolda tek gövde) · S18 (oran karesi)
       · S20 (temas) · S21 (kenet) · S23 (final).
       ⭐ Altısı da TASARIMDIR, envanter hatası değil: filmin ikinci
       yarısında insan kapalı bir gövdenin içindedir ve kamera onu ancak
       lombozdan ya da yük yatağından görür. İkinci yarı sahne sahne
       almaşır: S13-S15 insan · S16 makine · S17 insan · S18 makine ·
       S19 insan · S20-S21 makine · S22 insan · S23 makine.
       ⚠️ S14 ve S17/S19'da yalnız kask ve omuz kadrajdadır — yine 1.
       "figür yok" bulgusu O sahnelerde envanter hatasıdır.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         tam 1 · 18/24 sahnede görünür · insansız 6 (S12·S16·S18·
              S20·S21·S23) · araca biniş/tırmanma 0 kare (S10 dışarıda
              biter, S11 içeride başlar — kesme tasarımı) · airlock
              geçişi 0 kare · üsse yaklaşma 0 · gemide figür 0
KASK          24/24 KAPALI — İÇERİDE DE (yük yatağı BASINÇSIZ: örnek
              teknesi kargo taşır, insan taşımaz) · kasksız 0 · ara durum
              0 · giyme/çıkarma 0 kare · beyaz sert kabuk + TEK düz ön
              cam, görünür koyu çerçeve [D146] · cam optik berrak,
              renksiz, YANSIMASIZ — yüz okunur; sırt ünitesi YOK, sırt
              silueti DÜZ [D79]
YERÇEKİMİ     0.38 g (yüzey) — yürüyüş GERÇEK ZAMANLI, süzülme 0,
              zıplama 0, AĞIR ÇEKİM 0 [D44]; düşük g yalnız tozun
              çökmesinde ve balistik yaylarda
ATMOSFER      0.6 kPa · −55 °C: ses boğuk, tizsiz, uzak · gölgeler zayıf
              ve yumuşak, S1'den sonra HİÇ YOK (MEŞRU [D41]) · kaldırılan
              toz 3-4 s'de TAM çöker
FIRTINA       cephe 2 km yüksek, mat kahverengi, yüzü DİK: kıvrılma 0,
              köpürme 0, dalga 0, şimşek 0, huni 0, girdap 0 · iç akış
              yatay laminer, ekran SOLUNDAN SAĞA, tek hız
              ⭐ KUVVET SIFIR: kumaş kıpırdamaz, gövde eğilmez, hiçbir
              şey devrilmez ya da uçmaz; şakül ipi S3'te DİK ve
              HAREKETSİZ (kanıt sahnesi) · dokuz kasa S12'de kalkışın
              altında bile devrilmez
              GÖRÜŞ (monotonik): S0 12 km → S3 3 km → S6 800 m →
              S9 300 m → S11 120 m; hiçbir sahnede AÇILMAZ
PANEL SIRASI  12 sıra · S0'da uzak 3'ü söner ve gölge hattı kameraya
              doğru ilerler · S1'de sonuncusu söner ve adamın gölgesi
              de kaybolur · geri yanan sıra 0
ÜS            tarlanın gerisinde: 3 beyaz yatay modül + 5 m düğüm (çanak
              anten + direk), regolit setleri, dar koyu pencere şeridi,
              yuvarlak airlock · dış aydınlatma 0 · yalnız S0 ve S2 arka
              planında · hiç açılmaz, yanında figür 0
PİST · MAST   pist üssün 250 m ekran-SAĞINDA · mast 6 m, ÜÇ EŞİT ADIMDA
              iner: S6 (adım 1, kadrajda) · S8 (adım 2, kadraj dışı ses)
              · S12 (adım 3, tam yatık) — her adım aynı uzunlukta ve aynı
              duraklamayla; geri kalkma 0
TEKNE         9.0 m · 2.4 m çap · 3 bacak · 3 motor çanı · burunda kenet
              halkası · yük kapağı ekran-SOL yanda ve üsse bakar (24/24
              aynı yönelim) · kapağın karşısındaki duvarda 30 cm lomboz ·
              gövdede yazı/rakam/bayrak/logo 0
AMORTİSÖR     ön bacağın cilalı mili, silecek halkası referans yüzey:
              S4 iki parmak · S8 bir el · S12 yine iki parmak. Mil ışığı
              tutar, çevreyi YANSITMAZ. Bu sayaç bilinçli olarak TERSİNE
              DÖNER; dönüş kütle eşitliğinin kanıtıdır.
KASA          9 adet · dizüstü uzunluğunda · mat koyu gri · kapalı ·
              YAZISIZ (etiket, rakam, indeks 0 — raf içeriğini yerinden
              bilir) · S4 dokuzu raftadır → S7 birincisi çıkar → S9
              dokuzuncusu → S10-S12 dokuzu tozda tek sırada dik →
              S23'te kadrajda değil
YÜK YATAĞI    2.2 × 1.1 × 0.9 m · BASINÇSIZ · bir alüminyum raf + DÖRT
              özdeş beden boyu kelepçe tepsisi + örgü kargo kayışı ·
              koltuk 0 · kemer koltuğu 0 · konsol 0 · gösterge 0 · ekran
              0 · tavanda düz gölgesiz iş ışığı (S22'de tek adımda söner
              ve geri yanmaz)
KALKIŞ        ateşleme T+3.5 · yerden kesilme T+4.5 · kadrajı ÜSTTEN
              terk T+9.0 · alev: neredeyse şeffaf mavi-mor, GENİŞ açılan
              koni, kıvrılma 0, duman 0, mantar bulut 0 · toz: DÜZ
              balistik yaylar, ≤2 s'de yerde · ⛔ BACAKLAR HİÇ KIPIRDAMAZ
              [D148]: katlanma 0, geri çekilme 0; alev bacakların
              ARASINDAN geçer ve uzak yüzleri görünür kalır
0 g           S15'ten itibaren: serbest cisimler süzülür (kargo kayışının
              ucu · çekirdek tüpü, ~4 saniyede bir tam dönüş) · BEDEN
              SÜZMEZ — kayış takılı kalır, yalnız kol/baş/göz hareket
              eder [D23·D149] · süzen nesneler ADLI ve avuç boyundadır
GEMİ          260 m · 12 özdeş rıhtım (11'i dolu kasa rafı) · 6 radyatör
              kanadı dar kenarıyla · 4 küresel tank · mat, cilasız · lit
              pencere 0 · fener 0 · seyir feneri 0 · yazı 0 · figür 0 ·
              plume 0 · ORAN: tekne 1/29 (bir güve ve katedral duvarı)
YANAŞMA       burun önde (motor ucu asla rıhtıma dönmez) · 0.2 m/s ·
              TEMAS S20 T+6.0 · oturma 2 cm · sekme 0 · kayma 0 · son
              beş metrede iki gövde de dönmez · kelepçe TAM 4, sırayla,
              üçüncüsü yarım saniye duraksar · kıvılcım 0 · enkaz 0
EKRAN YÖNÜ    YERDE: her hareket SOLDAN SAĞA; fırtına, tarla ve üs
              SOLDA, pist ve tekne SAĞDA; yük kapağı 24/24 ekran-SOLA
              bakar. YÖRÜNGEDE: gemi kadrajın SOLUNU doldurur, rıhtım
              ağzı ekran-SAĞA bakar, tekne sağdan gelir. GEÇİŞ: S12'de
              tekne kadrajı DİKEY olarak üstten terk eder — yatay bileşen
              0, eksen kırılmaz.
SUIT          arduvaz grisi + solgun okra bantlar · yıpranma tam 3 sabit
              bölge (sağ diz aşınması · sol önkol bandı sürtük · sağ
              göğüs sıyrığı) [D42] + KİR MERDİVENİ 4 faz [D147]:
              PHASE 1 S0-S1 (bot+diz) · PHASE 2 S2-S6 (+avuç, önkol, sol
              yüzey filmi) · PHASE 3 S7-S11 (bütün sol yüzey + kask
              çerçevesi solu) · PHASE 4 S13-S23 (PHASE 3 ile AYNI —
              vakumda toz ne silinir ne artar). Toz azalmaz.
IŞIK TAKVİMİ  BÖLGE 1 (S0-S1): alçak güneş ekran-SOLDA, gölgeler
              ekran-SAĞA, karamela gök, güneş diski 0 kare · BÖLGE 2
              (S2-S12): gölgesiz amber → kahverengi loşluk, her sahnede
              bir kademe daha koyu · BÖLGE 3 (S11·S13·S15·S22): yük
              yatağının düz gölgesiz okra iş ışığı; S22'de söner ve
              yerini lombozun sert kenarlı dikdörtgenine bırakır ·
              BÖLGE 4 (S14-S23): kadraj dışından SERT yan güneş, mutlak
              siyah gölge, dolgu 0, yıldızlar keskin, güneş diski 0 kare
              · yapay lamba yalnız yük yatağında · MONOTONİK: yerde ışık
              yalnız azalır; tek artış İRTİFA geçişindedir (S13 T+7.5)
SES REGISTER  HUMAN 0 replik · MACHINE 0 replik · TELSİZ 0 replik —
              duyulan her şey nefes, kumaş, bot, gövde iletimi ve
              fırtına uğultusudur · DIŞ (S0-S11): ince tizsiz uğultu,
              sahne sahne yükselir · S6/S8/S12: mastın tek tok darbesi ·
              S12-S14: gövdeden derin gürleme (filmin en yüksek sesi) ·
              S15: gürleme YOK — nefes + gövde tıkırtısı · S16-S23:
              VAKUM, dış ses 0; yalnız açık telsiz kanalının taşıyıcı
              hışırtısı ve nefes · S20 T+6: nefes yarım saniye TUTULUR ·
              S21: dört tok darbe, üçüncüsü geç · S22: dört darbe, sonra
              yalnız nefes · ⛔ dijital sessizlik 0 [D83/D136] ·
              "eksik diyalog" bulgusu yazılamaz · müzik promptlarda 0
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI [Ders 142 — her kapı KOMUT · DOĞRULANDI · İKAME]

```
M="<master.mp4>"   ·   ffmpeg 8.1 · kuru koşu 31.08.2026: silencedetect ·
ebur128 · crop · tile · select · showinfo · astats · signalstats · scale ·
fps · blackdetect → hepsi `ffmpeg -hide_banner -filters` çıktısında VAR.

E1 SÜRE · EN-BOY · FPS
   KOMUT:      ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate "$M"
   KABUL:      239 ± 2 s · 16:9 · ≥1440p (ihraç kilidi)
   DOĞRULANDI: ffprobe 8.1 · 31.08.2026
   İKAME:      —

E2 SES KANALI + LUFS + TEPE  [D136 · D137 · KURGU_RITMI §6]
   KOMUT:      ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$M"
               ffmpeg -i "$M" -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:"
   KABUL:      audio VAR · −14 ± 1 LUFS · tepe ≤ −1.0 dBTP
   DOĞRULANDI: ebur128 · ffmpeg 8.1 · 31.08.2026
   İKAME:      ebur128 yoksa: astats (RMS) + "ses kanalı var" satırı yeter
   → sonuç satırı rubriğin künyesine YAPIŞTIRILIR: SES KANALI: VAR · −x LUFS · tepe −y dBTP

E3 DİJİTAL SESSİZLİK  [D83 · D136]
   KOMUT:      ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 | grep silence_
   KABUL:      0 aralık. ⚠️ Bu filmde S15 (MECO) ve S16-S23 (vakum)
               "sessiz" GÖRÜNÜR ama sessiz DEĞİLDİR: nefes ve telsiz
               taşıyıcı hışırtısı kesintisiz serilir. Aralık bulunursa
               miks hatasıdır, tasarım değil.
   DOĞRULANDI: silencedetect · ffmpeg 8.1 · 31.08.2026
   İKAME:      astats saniyelik RMS — −60 dB altı saniye 0 olmalı

E4 KESME IZGARASI
   KOMUT:      ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"
   KABUL:      23 kesme · saniyeleri 9 + 10k (±0.3 s)
   DOĞRULANDI: select/showinfo · ffmpeg 8.1 · 31.08.2026
   İKAME:      eşik 0.3 → 0.15. ⚠️ Uzay sahneleri (S16-S23) birbirine
               yakın parlaklıktadır ve eşik onları atlayabilir; ızgaranın
               üç sabit çapası S11↔S12 (iç→dış), S12↔S13 (dış→iç) ve
               S15↔S16 (iç→uzay) sıçramalarıdır — bu üçü bulunmazsa
               kurgu ızgarası bozuktur.

E5 KÖŞE TESTİ — FİLİGRAN  [D150]
   KOMUT:      ffmpeg -i "$M" -vf "crop=360:240:iw-360:ih-240,fps=1/30,tile=6x2" -frames:v 1 kose_SA.png
               (dört köşe için crop x/y değiştirilir)
   KABUL:      8 örnekte aynı köşede aynı şekil YOK
   DOĞRULANDI: crop/fps/tile · ffmpeg 8.1 · 31.08.2026
   İKAME:      —

E6 FİNAL VURUŞ KANITI  [D141]
   KOMUT:      ffmpeg -ss 235 -i "$M" -frames:v 1 kanit_S23.jpg
   KABUL:      B bloğundaki beş sayılabilir öğe (rıhtım 12 · dolu raf 11 ·
               kenetli tekne 1 · yanan ışık 1 · figür 0)
   DOĞRULANDI: ffmpeg 8.1 · 31.08.2026
   İKAME:      —

E7 DORUK KANITI — S20 içi (temas)
   KOMUT:      ffmpeg -ss 202 -i "$M" -frames:v 1 kanit_S20a.jpg   (T+3: temastan önce)
               ffmpeg -ss 207 -i "$M" -frames:v 1 kanit_S20b.jpg   (T+8: oturmuş)
   KABUL:      a: halkalar arasında boşluk var, tekne hareket hâlinde ·
               b: halkalar oturmuş, boşluk 0, gövde durgun, sekme izi yok
   DOĞRULANDI: ffmpeg 8.1 · 31.08.2026
   İKAME:      —

E8 AMORTİSÖR SAYACI — S4 · S8 · S12 (novum kanıtı)
   KOMUT:      ffmpeg -ss 42 -i "$M" -frames:v 1 s04.jpg
               ffmpeg -ss 82 -i "$M" -frames:v 1 s08.jpg
               ffmpeg -ss 120 -i "$M" -frames:v 1 s12.jpg
   KABUL:      s04 iki parmak · s08 bir el (belirgin daha uzun) · s12 yine
               iki parmak; üç karede de referans silecek halkası aynı
   DOĞRULANDI: ffmpeg 8.1 · 31.08.2026
   İKAME:      crop+signalstats ile bant bölgesinin ortalama parlaklığı
               s04→s08 artmalı (ffmpeg -ss <t> -i "$M" -frames:v 1 -vf
               "crop=w:h:x:y,signalstats" -f null - | grep YAVG)

E9 KALKIŞ TEMPOSU — S12 (D127 · D148)
   KOMUT:      ffmpeg -i "$M" -vf "select='between(t,119,129)',fps=2,scale=640:-1,tile=5x4" -frames:v 1 kalkis.png
   KABUL:      20 karede: ateşleme ≈ 3.5. saniyede · yerden kesilme ≈ 4.5 ·
               9. saniyede gövde kadrajın üstünde yok · BACAKLAR HER
               KAREDE AYNI AÇIDA (katlanma yok) · dokuz kasa her karede
               dik ve yerinde
   DOĞRULANDI: select/fps/scale/tile · ffmpeg 8.1 · 31.08.2026
   İKAME:      fps 2 yerine tek tek: ffmpeg -ss <t> -frames:v 1

E10 IŞIK MONOTONİKLİĞİ — yer bölgesi (S0-S12)
   KOMUT:      for t in 4 14 24 34 44 54 64 74 84 94 104 114; do ffmpeg -ss $t -i "$M" \
                 -frames:v 1 -vf "scale=320:-1,signalstats" -f null - 2>&1 | grep -o "YAVG:[0-9.]*"; done
   KABUL:      YAVG dizisi MONOTONİK azalır (±%3 gürültü payı) — hiçbir
               yer sahnesi bir öncekinden parlak değil
   DOĞRULANDI: signalstats/scale · ffmpeg 8.1 · 31.08.2026
   İKAME:      kareler göz kararı sıralanır; artış varsa hangi sahne
               olduğu yazılır (ışık takvimi ihlali)

E11 İNSAN ŞERİDİ ÖRNEKLEMESİ [D118]
   KOMUT:      ffmpeg -i "$M" -vf "select='eq(n\,150)+eq(n\,3600)+eq(n\,4800)+eq(n\,5400)+eq(n\,6000)+eq(n\,6900)',scale=480:-1,tile=3x2" -frames:v 1 serit.png
               (30 fps · S0 T+5 · S12 T+1 · S16 T+1 · S18 T+1 · S20 T+1 · S23 T+1)
   KABUL:      1. karede figür VAR; kalan beşinde figür YOK — şeritle
               birebir uyuşur
   DOĞRULANDI: select/scale/tile · ffmpeg 8.1 · 31.08.2026
   İKAME:      fps farklıysa kare numaraları saniye × fps ile yeniden
               hesaplanır
```
