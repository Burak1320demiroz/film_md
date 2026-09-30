# 🧠 THE_SCOURED_GLASS — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md` + `04_ARASTIRMA_BULGULARI` §TUR 13/14/16.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.
>
> ⚠️ **Durum:** film 07.09.2026'da `00_PLAN.md` + `FAZ_01_UYANIS.md` (24 prompt)
> ile yazıldı, üretilmedi. Bu dosya konsepti sıfırdan kurmaz; **yazılmış
> konsepti TUR 16'ya ve okuma turuna karşı yeniden denetler**, çelişkileri
> karara bağlar ve plana taşınacak satırları üretir. Var olan bozulmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     SAHİP VERDİ (07.09.2026 · 00_PLAN §NOVUM): Mars yüzeyinde tek
            adam, hayatta kalma, The Martian ekseni; "The Martian gibi
            hayatta kalmalı" (11.09.2026 talebi). AI seçimi yok.
② FORMAT:   YATAY 16:9 · 10-20 dk hattı, UZUN UÇ → kart §2.5 · bölüm = faz
            dosyası (FAZ_01…FAZ_15) + 00_PLAN
③ SAHNE:    180 (15 faz × 12) · 30:00
   ⛔ BANDIN DIŞINDA (tavan 10 faz · 120 sahne · 20:00). Sahibin açık izni
      VAR: `../README.md` §"15 FAZ / 30 DAKİKA — BANDIN ÜSTÜNE AÇILAN
      SATIR (07.09.2026, sahip kararı)" [D74]. Raporun parçalanma itirazı
      orada kayıtlı; karşı önlem = her fazın son çeyreği BEDEL.
④ REFERANS PAKETİ: YAZILSIN — sahip kararı 07.09 ("üretim bunsuz başlamaz",
   00_PLAN §REFERANS PAKETİ · RA·RB·RC·RD tanımlı, RE F8'de). KAPI 0.
   §5b tablosu yine de dolduruldu: altı tetikleyicinin BEŞİ doğru.
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP (11.09.2026): "yatay_10_20_dk_filmler klasöründe THE_SCOURED_GLASS
  adlı bir film var başlayamadım /yeni-film akışına göre part-1 kısmın ve
  ana planı güncellemeni istiyorum var olanı bozmadan hatta the martian
  filmi gibi hayatta kalmalı olduğu iicn 4 tane 6 cümlelik derin araştırma
  promtuda hazırla sana sonucları verim öyle başla"
  → dört prompt yazıldı (19_…), dört rapor geldi, TUR 16 süzüldü; bu akış
    o süzmenin üstünde koşuyor.
TALEP (07.09.2026 · 00_PLAN künyesi): 15 faz · The Martian ekseni ·
  motor OMNI 1.1 Flash · replikli (günlük + cevapsız telsiz).
REPLİK: VAR (S4 telsiz · S12 günlük · ~24 günlük sahnesi) → AYRI KAPI
  ZİNCİRİ AÇIK: SES_VE_DIYALOG §1a-§2a + DIYALOG_SAHNESI + DIALOGUE_CRITIQUE
  (Kart P 2b) — DEĞİŞ-TOKUŞ TABLOSU plana yazılır.
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**
TUR 16'nın hükmü (T16.2 #17): *önerme harfi harfine savunulamaz; en yakın
savunulabilir ifade aşağıdadır.*

| sahibin isteği / planın satırı | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "Toz triboelektrik yüklüdür; silmek onu kaldırmaz, yüzeye GÖMER ve çizer" (00_PLAN §NOVUM) | Elektrostatik yapışma silmeyi engellemez; matlaştıran şey **kuru mekanik aşındırmadır** (Mohs 5-6,5 bazalt/hematit tozu · polikarbonat Mohs 2-3). Su/solventle silme ÇİZMEZ | **KURU SİLME ÇİZER. Islak silme çizmez — ama su hayattır.** Novum'un ahlaki motoru buradan doğar: görüş ile içme suyu aynı tüpten çıkar | T16.2 #8 · #9 · #14 · #17 → 00_PLAN §NOVUM yeniden yazılır (madde 1) |
| "15 kademe" cam merdiveni (KİLİT 1) | Berrak↔tam mat arası ~10-12 JND; %60'ta yüz okunmaz | **12 kademe** (0-12), vizör kaplama %: 0-2 · 5 · 10 · 15 · 22 · 30 · 40 · 50 · 60 · 70 · 80 · 85+ | T16.2 #11 · #12 → KİLİT 1 tablosu (§8) |
| F4 "yakıt yakıp su üretmek" (modül içinde) | H₂ yakımı kapalı kabinde patlama bandında (%4-75); hidrazin toksik | Yakma hücresi YAŞAM ALANI DIŞINDA; yoğuşan su içeri; bedel = O₂ payı (iğne bir çentik daha kırmızıya) + bir yanık (sol el sırtı) | T16.2 #21 |
| F5 "yiyecek üretmek", F6 "toprağı yıkamak" | İlk mahsul 90-110 sol > filmin 84 sol'ü; perklorat %0,5-1 | F5: filiz 3-7 günde çıkar ve **solar**, hasat YOK; F6: toprak:su 1:5 yıkama, huni altında berrak su + tepside BEYAZ KRİSTAL TUZ; su stoğunun yarısı (100 L) gider ✓ | T16.2 #22 · #23 |
| F7 "filtre tıkandı → bez filtre" | Toz 1-3 µm, kumaş 20-100 µm: bez filtre olamaz | Filtre silindiri ters gazla/vurarak temizlenir; **bez ızgarayı siler** ve gritle dolar — aynı bez sonra vizöre gider (F10) | T16.2 #24 · #30 |
| F8-F13 "araç 90 sol uzakta, yürümek" | Tek EVA 6-8 saat, ≤15-20 km; 90 sol yürüyüş imkânsız | Araç ~**180 km**; gezici PANEL-SINIRLI (10 m² ≈ 2,5 kWh/sol → 6-8 km/sol); gezici F12'de araca **≤15 km kala** ölür; F13 = tek EVA, tek sol | T16.2 #19 · #27 → B5 ENGEL |
| F10 "görüş sıfır" fırtına | Görüş savunulabilir (τ>5: 2-5 m), rüzgâr DEĞİL (30 m/s = 9 Pa, kimseyi itmez) | Fırtına 15-18 sol; görüş 2-5 m, güneş diski kaybolur, pas alacakaranlık; hiçbir şey savrulmaz; yeni ışık bloğu **B1-FIRTINA** | T16.2 #25 · TUR 14 #9 |
| F11 "yanlış yöne sürer" | Pusula yok, kerteriz güneş; mat camda güneş belirsiz halo | Yön kaybının SEBEBİ mat camdaki güneş halosu (perdeleyici parlama) — novum'un ödediği bedel | T16.2 #10 · #26 |
| KİLİT 4 "long unkempt beard" (F10+) | Sakal 0,3-0,4 mm/gün → 84 solde ≤ ~3 cm | Token: F1-F2 "four days of dark stubble" · F3-F5 "a short dark beard" · F6-F9 "a dense short beard" · F10-F12 "a dense beard, cheeks beginning to hollow" · F13-F15 "a dense beard, cheeks hollowed" — "long" hiçbir fazda YOK | T16.2 #2 · #3 |
| BLOK C "fine dust hangs and drifts for a long time" · FAZ 1 KİLİT 5 ③ "toz havada ASILI KALIR" | İnce atm.: toz yavaş çöker, OTURUR; hang/drift = su altı süzülme (Low Power Parçacık 2/10 · D39/D59) | "rises, then settles slowly and surely; each grain on its own path; nothing swirls"; S9 bulutu klip İÇİNDE oturur | D39 · D59 · D143 · YAPI_GRAFI §6 |
| "Güneş her kadrajda EKRAN-SOL" (00_PLAN IŞIK · FAZ 1) | Azimut 000°-290° arasında tek bir dünya-güneşi her kadrajda solda olamaz | Güneş DÜNYA yönü sabit (batı, ufkun 15° üstü); her sahnenin ekran tarafı **azimuttan türetilir** ve prompta yazılır (KEY DIRECTION STRING) | D201 · UZAMSAL §7 kural 5 |
| KİLİT 5 "5 sıra" erzak kulesi | Sayılabilir olmalı; 84 sol × 0,62 kg = 52 kg kuru gıda | **4 sıra × 10 = 40 paket** · F2 = 40 · F5 = 30 · F8 = 20 (geziciye 20 alınır) · F12 = 0 | T16.2 #18 · #29 |
| "S176 seçim" (motif listesi) | F13 = S145-S156; S176 F15'tedir | Merkezî seçim **F13** içinde (S151 · `03_SIRALAMA`); F15'te ikinci bedelli seçim (lombozu silmemek) | D158 B2a |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        YATAY 10-20 dk · UZUN UÇ (§2.5) + README §15 FAZ satırı
ORTAM:         §3.2 İNCE ATMOSFER (Mars: 0,38 g · ~600 Pa · toz yavaş çöker ·
               gölge yumuşak, dolgu VAR · dış ses boğuk/zayıf · mavi gün batımı)
               + §3.10 BASINÇLI İÇ HACİM (hava taşır; fan gürültüsü zemin;
               sessizlik = güç kesildi)
               → zorunlu satırlar: BLOK C toz fiziği (yeniden) · B1/B2/B1-FIRTINA/
                 GECE ışık blokları · UZAY_USSU §6 MARS negatif bloğu (Ay bloğu
                 YAPIŞTIRILMAZ) · MUZIK "kuru, kısa reverb" (vakum değil)
TÜR:           bilimkurgu · dal: SERT UZAY HAYATTA KALMA DRAMASI (§4.1)
               ⛔ Suvin anlamında novum YOK — kuru silme aşındırması GERÇEK
                 fiziktir (UZAY_SENARYO §1 "karar noktası": kulvar bilinçli,
                 adı doğru konuldu). Depo dilinde "novum" = filmin tek
                 görülebilir kuralı; ONERME kapısı ona koşulur.
KLİP SÜRESİ:   10,0 s  ⛔ ÖLÇÜLMEDİ [D124] — tercih. İlk test klibi:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test.mp4>
               → sayı 00_PLAN künyesine; iki ızgaralı film YASAK (YERÇEKİMİ F4)
SAHNE SAYISI:  180    RUNTIME: 1.800 s = 0 hook + 180 × 10,0  (hook ayrı klip DEĞİL)
BÖLÜM SAYISI:  15 faz dosyası (FAZ_01 yazıldı · FAZ_02-15 ⬜) — formattan gelir
MOTOR:         OMNI 1.1 Flash (sahip) · I2V, sahne başına tek imaj = start frame
               ⚠️ POLİTİKA §6.1 hipotezi: OMNI'nin "ünlü kişi" yanlış-pozitifi
               Veo'dan AĞIR ve bu film fotogerçekçi YÜZ + lense bakış taşıyor
               → red gelirse defter satırı MOTOR=OMNI ile açılır; §5 basamak 2.5
               SESSİZ KOŞU teşhisi; motor değişikliği SAHİBİN kararı
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM (yeniden yazılmış — plana madde 1):
   BU GEZEGENDE KURU SİLİNEN HER CAM KALICI OLARAK MATLAŞIR.
   Toz bazalt ve hematittir, camdan serttir; kuru bez onu kaldırmaz, cama
   sürterek yüzeyi aşındırır. Silmek görüşü bir kez daha azaltır ve geri
   gelmez. Çizmeyen tek silme ISLAK silmedir — ve buradaki her damla su
   içilecek sudur. ADAM GÖRMEK İÇİN SİLMEK, SİLMEK İÇİN SU HARCAMAK YA DA
   SİLMEMEYİ SEÇMEK ZORUNDADIR.
NOVUM TAŞIYICISI:    stiff grey wiping pad × tek geçiş jesti → silinen
                     yüzeyin berraklaşmaması, ARDINDA MAT ŞERİT kalması
① TEK KARE:          ✅ S8 (1:10-1:20) — "the wiping pad crosses the visor
                     once; behind it a matte abraded band stays on the glass"
                     (taşıyıcı adıyla [D157]; ped + şerit ~%45 kadraj; değişim
                     tek klip içinde; rakip olay 0 — nefes ve tek baş sallama
                     dışında hareket yok)
② KİNETİK BAĞIMSIZLIK: ✅ S8'de replik/dış ses/ekran metni yok; kural yalnız
                     jest + yüzey sonucuyla kanıtlanır. Sessiz tohum S2
                     (toz dökülmez). Kural F3'te bilinçli ödenir (panel).
③ BAŞLIK ŞEMASI:     ✅ THE SCOURED GLASS — 3 kelime, izleyiciye NEREYE
                     bakacağını söyler (cam); "THE + iki kelime" kanal kalıbı
✅ ÜÇÜ DE GEÇTİ → sıralama yazılabilir.
⛔ KURALIN BİTTİĞİ YER (SPEC NOVUM bloğu, D166/D183): mat şerit BÜYÜR ama
   asla temizlenmez; panel tozu asla kendiliğinden kalkmaz — rüzgâr
   temizliği 0 kare; ıslak silme filmde YALNIZ reddedilen seçenektir
   (F10 su tüpü kadrajda, kullanılmaz).
NOVUM TEKRARI [ONERME §5]: kural ≥3 sahnede, ≥2 nesnede doğrulanır —
   vizör (S8 · F3 · F10) · panel (F3 · F12) · gezici ön camı (S94) ·
   kapsül lombozu (S180). POV YOK (ONERME §7): "cam ardından" kadrajlar
   kamera-cam-adam OBJEKTİF kurulumdur, adam kadrajdadır
   (04 §T16.7'deki "POV" kelimesi bu anlamda okunur).
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ planın etiketi — BEDEL (00_PLAN "TEMA: BEDEL"; sayaç: 5 filmde, ⏸️ §3'te yok)
▸ §3 çapası — ENTROPİ  (§3 sekizlisinde VAR; depoda 3 kullanım, en az
   kullanılanlardan; tanım: "yıkım sonrasının sessiz izlenmesi · payoff =
   kaçınılmazlığın kabulü" = F13 silmeme)
   ⬜ SAHİP KARARI: 00_PLAN'ın etiketi BEDEL kalır mı, ENTROPİ'ye geçer mi?
   Bu akış etiketi DEĞİŞTİRMEZ (var olanı bozmama); plana "§3 çapası:
   ENTROPİ" alt satırı eklenir, "bedel" B5 satırına iner (oraya aittir).
▸ tanım cümlesi — ⛔ takas kalıbı değil ("görmeye devam etmek için
   gördüğünü silmek" takastır): "Bu gezegende düzeni koruyan her hamle
   düzensizliği artırır; aşınan cam geri dönmez ve adam sonunda geri
   dönmeyen şeyi silmeyi bırakır."
▸ depoda kaç kez kullanıldı — BEDEL 5 · ENTROPİ 3 (bash sayac.sh, 11.09.2026)
▸ motif kanalları — NESNE: mat şerit / silme pedi · KİNESİK: Laban ağır +
   sürekli; omuz çöker, kask göğse düşer (F12); F13 el 2-3 cm'de durur ·
   IŞIK: kararan kadraj (F12 panel ölümü, fırtına alacakaranlığı, gezici
   ışıkları söner) · KAMERA: cam ardından objektif kadraj (S94 · S180)
▸ §5 3. derece indeks ≥3 sahne: S8 (nesne) · S31 (kural, F3) · S94 (kamera)
   · S140 (ışık, F12) · S151 (seçim, F13) · S180 (ödeme)
▸ §2 AŞIRI TELAFİ: doruk bloklarında (F12 · F13) ışık + nesne + kinesik
   AYNI klipte
▸ §6 tema-final: ENTROPİ payoff = kabulleniş — S180 lomboz karesi; final
   KAPALI (fiziksel sonuç görülür) ama duygusal cevap "kabul"
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

> ⛔ PLAN YAZILMADAN ÖNCE. 5+ risk çıkıyorsa malzeme AZALTILIR.

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| 1 SU / SIVI | ✅ | F4 yoğuşma damlası · F6 huni suyu + tepside kristal · su tüpü (KİLİT 6) · F10 reddedilen su | Su yalnız KAPALI ŞEFFAF TÜPTE ya da tepside DURGUN; akan su 2 sahne (F4 damla · F6 huni), 0,38 g'de düşer, "floating drop" 0 | 🟡 |
| 2 CANLI | ❌ | Hayvan yok; F5 filizi tek sahnede kadrajda ve solarken (S~55) — bitki, canlı değil | Filiz 1 sahne, sabit, hareket yok | 🟢 |
| 3 KASK / VİZÖR | ✅ | Filmin novum'u vizörün kendisi; kubbe TASARIM; kademe metinle tutulmaz | RA p4 + RO K0/K1/K2 panelleri (KAPI 0); vizör TEK nitelik cümlesi; kademe SINIRDA, klip içinde sabit; KASK TAKVİMİ | 🟠 |
| 4 İKİNCİ FİGÜR | ✅ (her filmde) | 180 klip × klon riski; S9/F8/F12/F14 biniş-iniş sıcak noktaları | "Exactly one human" + D69 (eşik geçişleri kesmede) + D140 (0,6 s tarama SPEC E) | 🟡 |
| 5 EKRAN / SAYAÇ | ✅ | İğne (rakamsız), çentik duvarı, erzak kulesi, su tüpü, kayıt cihazı | Rakam 0 · çentik TEK İSTİSNA cümlesi · tüp çizgisiz · "glowing readout" yalnız F12 panel · ADAY-34 negatifi | 🟠 |
| 6 PARÇACIK / TOZ | ✅ | Her dış sahnede toz; S2/S9/F10-F12 fırtına; Low Power 2/10 emsali | BLOK C yeniden (oturur, swirl yok, zerre sayısı); fırtına = görüş kaybı, savrulma 0; patlama 0 · alev 0 kare (F4 yakma hücresi kadraj dışı, yalnız "faint dull-orange heat tint") | 🟠 |
| 6b KATMANLI DÜNYA | ✅ | Gündüz / gün batımı / GECE (F9·F12) / FIRTINA (F10-F12) / iç modül / gezici kabini | IŞIK TAKVİMİ sol bazlı + LIGHT STATE her promptta; bölge sınırı yalnız planlı kesmede (T11 KEY WALKS önlemi) | 🟡 |
| 7 DİYALOG | ✅ | S4 telsiz · S12 günlük · ~24 günlük sahnesi · F12'de kayıt ölür | Basamak 1 (telsiz, sessiz üretim) + basamak 2 (günlük MCU, OMNI sentaks, PROB B S12'de koşulur); ekranda konuşan ağız yalnız iç mekân; ters-U eğrisi; DEĞİŞ-TOKUŞ tablosu | 🟠 |
| 8 KAMERA | ✅ (iyi haber) | 180/180 fixed lockoff; kesme 0; sabitlik emri iki kez | Kurulum tavanı: F1 12 (bilinçli sapma, kayıtlı) · F2-F8 ≤6 · dönüş ≥%40 · küme ≥2/faz | 🟢 |
| 9 TEK BASKIN IŞIK + HEDEFE HAREKET | ✅ | F9 gece (kask feneri) · F13 alçak güneş + yürüyüş · fırtına içinde gezici farları | Dört kanallı ışık-yön kilidi; iki yenilgide kamera hedefe (araç ön planda, adam kameraya) | 🟠 |
| 10 İNSANSIZ SAHNE + UZUN NEGATİF | ✅ | Kuleshov B planları (kum kabuğu · panel · su tüpü makrosu · boş ufuk F13) | İnsansız promptta NEGATIVE tek satır, "0 human" YAZILMAZ, boş kadraj VARLIK olarak | 🟡 |
| 11 DEĞİŞKEN ÇEKİM / SAHNE İÇİ KESME | ❌ | Sabit ızgara 180 × 10,0; sahne içi kesme 0 | SPEC: "TARGET ASL BAND 10.0 s — sabit, bilinçli" + gerekçe | 🟢 |
| 12 POLİTİKA YÜZEYİ | ✅ | Kask çıkarma (S10) · yara (S6/S11) · kırmızı acil ışık + CU (F12) · fotogerçekçi yüz + OMNI · kısıtlı uzuv makroları (S2/S7/S11) | B6 satırı (§6) · ÖNLEM/MALİYET/TELAFİ üçlüsü · ≤3 öznitelik · şiddet sözlüğü 0 | 🟠 |
| 13 YAPI ÖLÇEĞİ / TEKRAR EDEN BİRİM | ✅ | Modül (10 m) · gezici (6 m) · yükseliş aracı (7 m) · basamaklar · 40 paket · 84 çentik | UZAY_USSU §1 iki dil (metre planda, gövde boyu promptta); kesir tablosu; tekrar eden birim SAYIYLA | 🟡 |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  MAT ŞERİT — KISMİ MAT CAM (kart 3 + kart 5 + kart 12 bileşiği):
                  model ya camı KENDİLİĞİNDEN temizler (T16.2 #15 · ADAY-30),
                  ya şeridi buğu/yansıma/çatlağa çevirir (bleed), ya yüzü
                  kaybedince yüz tespiti/politika düşer (#16).
POZİTİF BİÇİMİ:   "one matte abraded band on the outside of the visor: it
                  starts at the lower corner on the same side as the green
                  arc of the chest dial, runs level, one thumb-width tall
                  (band 1) / up to the line of his jaw (band 8) / up to the
                  bridge of his nose (band 11) / the whole pane (band 12);
                  its upper edge is sharp; 0 droplets, 0 cracks, 0 fog,
                  0 reflections in it; the glass keeps its exact shape;
                  the band never shrinks and never clears."
                  → SAYILAR: kademe adı · yükseklik nirengisi · 0/0/0/0
                  → her dış promptta; imaj = kademenin ÖNCESİ (D179)
TETİKLENEN RİSK:  12 / 14
EŞİK:             5
⛔ EŞİĞİN ÜSTÜNDE — malzeme AZALTILDI (tasarımla SIFIR'a çekilenler):
   · canlı 0 · patlama 0 · alev 0 kare · ikinci insan 0 · sahne içi kesme 0
   · kamera hareketi 0 · akan su ≤2 sahne · uzaylı 0 · HUD 0 · metin 0
   · faz başına TEK problem + TEK yeni nesne (F4 tüp · F5 filiz · F6 tuz ·
     F7 filtre · F8 gezici · F14 basamak) · F2-F8 kurulum ≤6/faz
   ÇIKARILAMAYAN (hikâyenin kendisi): kask/vizör · toz · diyalog · politika
   (kask çıkarma, yara) → KART 12 "malzeme azalt" ile değil ÖNLEM/MALİYET/
   TELAFİ ile ödenir (POLİTİKA §4.3)
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — kayıt için (karar zaten YAZILSIN)

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | RA (kasklı adam) · RB (giysi detayı) · RC (kasksız) — her sahne · 🎨 11.09 akşam: sahip giysiyi RENKLİ + ROZETLİ istedi → v2 "daha modern": `ASTRONOT_DONANIM` §4 yeni nesil gezegen giysisi (iki ton: beyaz sert üst gövde / grafit uzuvlar, cyan eklem biyesi) + §2 rol şeridi (SARI, SOL) + §3 metinsiz amblem seti (3 yama + sırt üçgeni) + grafit sırt; T14.2 hacim sınırı korundu; gerçek logo/harf YOK (D45 · ⑯ MİLLİYET 32). BLOK A/D + paket + SPEC aynı gün · 🎨 v3 turuncu/kömür (aynı gece, "çok kötü") · 🎨 **12.09 v4 KATMANLI SERT PANEL (ajan önerisi, sahip onayı):** inci beyazı yarı parlak paneller + sculpted kapaklar / gunmetal eklem / gümüş rulman halkası / tek aksan elektrik cyan / kontürlü sırt; "corrugated" + "squared" çıktı (eski görünümün kaynağı); toz "rust-orange"a döndü |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ | vizör kubbesi (YERÇEKİMİ F2 6/6) · **cam kademesi** → RA p4 + RO |
| T3 | oranı sözle yazılamayan nesne | ✅ | RD modül (10 m · 5,3 H) · RE gezici (3,2×2,7×2,0 H) · yükseliş aracı (3,7 H) — F8'de açılır |
| T4 | insan dışı canlı | ❌ | yok |
| T5 | tekrar eden insan dışı olay | ✅ | **cam aşınma merdiveni** (RO: K0 berrak · K1 kademe 4-6 · K2 kademe 9-12; ara kademeler METNE devredilir — REFERANS §3 SAYAÇ satırı) · giysi toz merdiveni · fırtına alacakaranlığı |
| T6 | bir varlık tekrar tekrar dönüyor | ✅ | silme pedi (RP) · su tüpü (RP) · çentik duvarı · erzak kulesi · göğüs kadranı · kayıt cihazı |

```
KARAR: YAZILIR — zaten sahip kararı; dosya adı `THE_SCOURED_GLASS_REFERANS_PAKETI.md`
   (D160/⑪.0 film adı önde). KAPI 0: RA·RB·RC·RD onaylı + seed yazılı
   olmadan tek klip üretilmez [D168]. 00_PLAN §REFERANS'a eklenecek:
   RO (cam merdiveni 3 panel) · RP (ped · su tüpü) · RE'ye yükseliş aracı.
⚠️ Kimlik geometriyle: kubbe kask + sırt paketi + tek renk şerit + 4 öznitelik.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S10 (kask çıkarma — COLD BURN S28 ×2 red sınıfı, PB)
NÖTR TARİFİ:         "Inside the pressurised module his head is bare; the
                     white helmet already rests on the bench beside him,
                     visor toward the camera. He does not touch it."
                     (kask START FRAME'de çıkmış — FAZ_01 zaten böyle;
                      klipte kimse hiçbir şey çıkarmaz)
ÖNLEM/MALİYET/TELAFİ (POLİTİKA §4.3):
  ÖNLEM    çıkarma eylemi kadraj dışı        MALİYET  "ilk yüz" jesti
  TELAFİ   yüz reveal'i KESMEDE (S9→S10), ilk maskesiz nefes + kask bench'te
İKİNCİ SIRA: S7 / S11 / S2 kısıtlı-uzuv makroları (YERCEKIMI F1 S8 sınıfı) →
  kadrajda omuz/kask çapası ya da ölçek şahidi; iki red → kamera taşınır
ÜÇÜNCÜ: yara (S6 delik · S11 zımba · F4 yanık) → şiddet sözlüğü 0, POZİTİF
  malzeme cümlesi; "blood/wound/injury" negatif olarak bile YAZILMAZ
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE) — FAZ_01 §B5'in güncel hâli

```
İSTEK:   Yaklaşık yüz seksen kilometre ötedeki yükseliş aracına ulaşmak ve
         onu kalkışa hazır hâle GETİRMEK — taşımak, bağlamak, çalıştırmak.
         Film başlamasa da var olan iştir (görevin dönüş aracı).
ENGEL:   Aracın da gezicinin de modülün de gücü güneş panelinden gelir;
         panel tozla körelir ve kuru silmek onu kalıcı olarak aşındırır.
         Gezici panel-sınırlıdır (günde 6-8 km); yol 25-30 sol sürer ve
         fırtına 15-18 sol'ünü yutar. Aynı bez vizörü de siler.
BEDEL:   Her kuru silme bir kademe görüş/güç götürür ve geri gelmez.
         S8  cam 0 → 1 (farkında değil) · S11 gövde (kendi yarasını kapatır)
         S31 (F3) ilk BİLİNÇLİ silme, panel + cam · S94 (F8) gezici camı
         S140 (F12) panel ölür, gezici durar, kask göğse düşer
         S151 (F13) ⭐ SİLMEMEYİ SEÇER — el 2-3 cm'de durur, ped yere
         S180 (F15) lombozu SİLMEZ, bakar (ikinci bedelli seçim, D158)
MUHATAP: KENDİ BEDENİ (görüş · sakal · yara · adım) + ORTAMIN KALICI DEĞİŞEN
         PARÇASI (vizörün mat şeridi) + KAYIT CİHAZI (S12'de kurulur,
         F12'de ölür). İkinci insan YOK.
AYRILIK: — (tek insan; IKI_KISI kartı yazılmaz — gerekçe: D20 tek karakter)
```

## 8. 🪜 KİLİT 1 — CAM MERDİVENİ, 12 KADEME (plana taşınır)

| kademe | vizör kaplama | yüz nirengisi (prompt) | faz | olay |
|:--:|:--:|---|:--:|---|
| 0 | %0-2 | "the pane is clear; a sparse scatter of grains on the outside" | F1 S1-S7 · F2 | temiz |
| 1 | %5 | "one thumb-width tall at the lower corner" | S8 → F2 | tek geçiş, farkında değil |
| 2 | %10 | "two thumb-widths" | F3 (S31) | ilk bilinçli silme (panel + cam) |
| 3 | %15 | "up to the line of his jaw" | F7 | ızgara bezi cama gider |
| 4 | %22 | "up to the corner of his mouth" | F8 (S94) | gezici camı da matlaşır |
| 5-7 | %30-40 | "up to his lower lip / to his mouth / cheek" | F10 (üç silme) | fırtına |
| 8 | %50 | "up to his cheekbone — the mouth is behind the band" | F11 | yön kaybı (güneş halosu) |
| 9-10 | %60-70 | "up to the bridge of the nose" | F12 | panel ölümü |
| 11 | %80 | "to the eye line; only a thin clear strip at the eyes" | F12 son / F13 baş | son silme |
| 12 | %85+ | "the whole pane is matte; the face behind it is a shape" | F13 (S151 sonrası) · F14 · F15 | SİLMEME kararı, merdiven durur |

```
⛔ KURALLAR: monotonik (asla küçülmez) · kademe yalnız sahne SINIRINDA
   değişir (silme klibinde ped geçer, ŞERİT sonraki imajda büyümüş görünür —
   S8 tek istisna: novum tek karesi, değişim klip içinde) · kademe ≥8'de
   yüz MCU YAZILMAZ (politika #16) — yüz F10 sonrası yalnız kasksız iç
   sahnelerde (gezici kabini F11-F12) ve S180 lombozunda · kademe ≥3'te
   "clear/clean/pristine visor" kelimesi hiçbir promptta yok · ARIZA YÜZÜ
   KAPATAMAZ (T11.5③) ile ÇATIŞMA: kademe 9-12 yüzü kapatır → KARAR: bu
   filmin novum'u budur, sapma [D74] plana yazılır; göz hattı kademe 11'e
   kadar "thin clear strip at the eyes" ile açık tutulur, 12 yalnız F13-F15
   (13 sahne EWS/MS ağırlıklı, yüz gereği yok) · ölçen: ② DEVAMLILIK cat.3
   (kademe) + ① KARE cat.2 (konum) + ⑨ KADRAJ cat.4 (oran)
```

## 9. 🕰️ ZAMAN KANALLARI VE KAYNAK DEFTERİ (TUR 16 #1 · #5 · #18)

```
ANA TAŞIYICI (her sahnede kadrajda): İÇ F2-F8 = çentik duvarı · DIŞ F9-F15 =
  vizör mat şeridi. Faz başına ANA taşıyıcı 1 kademe + ≤2 yan kanal (sakal ·
  erzak · toz · yara · su tüpü · iç ışık); 4+ kanal aynı anda YOK.
KAYNAK DEFTERİ (84 sol · ÖNERİ etiketli, prompta rakam inmez):
  O₂ ~70 kg (iğne) · kuru gıda ~52 kg = 40 paket (kule) · su ~200 L
  (tüp + tank; F6'da 100 L gider) · gezici pil 40 kWh (gece ısıtma %45-60) ·
  panel 10 m² ≈ 2,5 kWh/sol → 6-8 km/sol · fırtına τ>5 → güç %14
SOL SAYACI: F2 çentik 1 → her faz +6 → F15 84. Rakam ekranda YOK.
```

## 10. 🧾 PLANA DÜŞEN KARAR SATIRLARI — kılavuzların istediği tek satırlar

```
HOOK TİPİ:          YANLIŞLIK KOMPOZİSYONU (S1: normal yüz + camın dışı toz
                    kaplı, yalnız göz hizası açık) — tek tip
S1 SORU CÜMLESİ:    "Bu adam buraya kendi ayağıyla mı yattı, yoksa düştü mü?"
                    (FAZ_01 S1 künyesi ✓)
S2 İKİNCİ BİLGİ:    toz elden dökülmüyor (soru büyür: burası neden böyle?)
BİLGİ ASİMETRİSİ:   DRAMATİK İRONİ · taşıyıcı ② ZEMİN/YÜZEY — izleyici S8'de
                    şeridin kalıcı olduğunu görür, adam F3'te (S31) anlar ·
                    asimetri anı 1:20 · panik 0 kare · IRONY LOCK (B1 adayı)
KATALİZÖR:          S11 zımba (1:40 = %5,5) ⚠️ HOOK §1.1 bandı %10-15
                    (S18-S27) — FAZ 1'in araştırma ızgarası (90-120 s) bunu
                    bilerek öne aldı; ikinci katalizör F2 sonu (S24: erzak
                    "kısa çıkar") %13 bandın içinde → plana iki katalizör
                    satırı, gerekçe FAZ_01 §sözleşme
TOHUM:              su tüpü F2 rafta (S≤27, ≤2 s, bakışla vurgulanmaz);
                    silme pedi S8 eldivende ✓
FİNAL TİPİ:         KAPALI (10-20 dk varsayılanı) + tohum (tüp/ped) · twist yok
SON PLAN TİPİ:      İLK KADRAJA DÖNÜŞ — S180 lomboz ↔ S1 vizör (konum kilidi)
ÇİFT TİPİ:          KAFİYE · değişen TEK değişken ② NESNE: cam kademe 0 → 12
                    (foveal merkez) · sakal/yara periferik, gerekçe planda
KAPANIŞ BÜTÇESİ:    doruk F14 (S157-S168) → çözülme F15 = 12 sahne = %6,7
                    (band %7-10'un hemen altı; F15'in ilk 2 sahnesi doruğun
                    kuyruğudur → fiilen ~%8) ✓
OVERVIEW SAHNESİ:   TEK — F13 EWS (adam 1/20, geriye bakış = habitata, sessiz,
                    tam sahne); S180 Overview DEĞİL
PAYLAŞIM SAHNESİ:   KAYGI yuvası — F11-F12 (daralan görüş + sığ nefes);
                    huşu değil → yorum + kaydetme metriği (plana yazılır)
KAPAK ANI:          S1 · 0:04 · ECU vizör, göz hizasında açıklık, camın dışı
                    toz · tek sert yan ışık · odak: göz — prompta SAYIYLA
⭐VİRAL:             S8 (YÜZ: memnun baş sallama, kaş gevşer 2 s / HAREKET:
                    ped geçer, şerit doğar) · S94 · S140 · S151 — her biri
                    YÜZ+HAREKET satırı taşır, biri boşsa etiket düşer
MİMARİ KUTUP:       NOSTROMO (kullanılmış, tozlu, çizik) — Bible'a
ANTAGONİST KANALI:  ÇEVRE + KENDİ SEÇİMİ (değer çatışması: görmek ↔ içmek)
HAUGE %:            fırsat %10 S18 · eşik %25 S45 · dönüşü olmayan %50 S90 ·
                    büyük gerileme %75 S135 (F12) · son itiş %90+ S162 (F14)
D69 KARAR SATIRI:   S9 eşik geçişi kadraj dışı · F8 geziciye biniş kesmede ·
                    F12 iniş kesmede · F14 kapsül girişi kesmede
ZİNCİR MODU:        I2V, sahne başına tek imaj = start frame; end frame yok
                    (OMNI · YERÇEKİMİ KİLİT 1 emsali) — FAZ_DOSYASI_SABLONU'nun
                    start/end zinciri bu motorda uygulanmaz [D74]
LENS OMURGASI:      50 mm (F1'de 4/12; film ≥%60 hedefi F2+'da) · sapmalar:
                    24-35 mm ölçek · 85 mm günlük/insert · 100 mm vizör makro
FRAGMAN MEKANİĞİ:   "SİLME" — her vuruş bir silme, son vuruş silinmez (aday)
AI ALGISI (🔴 kutu): kusur bütçesi kesilmez · etiketleme · konuşan ağız yalnız
                    günlük · fizik defteri sabitlenen yorumda
BAĞIMSIZ FİLM:      evrene bağlı değil; ön bilgi 0 sahne
```

## 11. 🧍 KARAKTER KARTI — "tek adam" (B5'ten hemen sonra · plana Bible'ın ÜSTÜNE)

| satır | içerik | sahne |
|---|---|---|
| ROL | Görev teknisyeni — giysi şeridi, göğüs kadranı, alet kemeri; işi tamir/taşıma | S1-S12 (giysi), S11 (zımba = kendi tamir refleksi) |
| İSTEK | Yükseliş aracına ulaşıp kaldırmak — film başlamadan var olan iş | S5 (yön), S12 (günlük: niyet), F8 (karar) |
| BASKI TEPKİSİ | **KONTROL EDER** (tek kelime, sabit): her uzanmadan önce el bir an durur, nesneye bakar | S7 (tıklatır), S11 (üç zımba, ölçülü), F12 |
| ALIŞKANLIK | KURU SİLME jesti — sağ el, stiff grey pad, tek geçiş, soldan sağa | S8 (1) · S31 (2, daha kısa) · S94 (3, daha yavaş) → KIRILMA S151: el kalkar, 2-3 cm'de durur, iner; ped yere |
| SINIR | Suyu cama harcamamak | F10 (tüp kadrajda, kullanılmaz) · F6 (yarısı toprağa gider — sınırın bedeli) |
| ZAAF | Görünür iz: cam kademesi · sol el sırtı yanığı (F4) · sağ kalça yarası (S6→S11→F4 kabuk→F9 iz) · adım kısalır (F12+) | S11 · F4 · F9 · F13 (adım 60-70 → 30-40 cm) |
| TEL | Baskı altında kask göğse düşer / çene iner (eldiven kontrolü YASAK — ADAY-85) | S4 (kask 1° iner) · F12 (kask göğse) |
| İLK ↔ SON | S1: gözler açılır, el cama gider (S8 siler) ↔ S180: el cama GİTMEZ, bakar | S1 ↔ S180 |

```
KARAR MİMARİSİ (KARAKTER_KARTI §3):
  İKİ SEÇENEK KADRAJDA   F10: su tüpü + ped aynı kadrajda, tüp kullanılmaz ·
                          F13: ped + yol aynı kadrajda, ped yere bırakılır
  BAŞARISIZ DENEME       F5 filiz · F6 yıkama · F10 üç silme · F11 yön
                          (her biri yöntemi değiştirir, bedel bırakır)
  BEDEL PENCERESİ        F12 panel ölümü aynı klipte kask göğse (ilk 3 s)
  HOBSON                 S11 zımba: tek seçenek, seçilen şey TARZ (üç
                          ölçülü tıkırtı, bağırma yok)
DAVRANIŞ ŞERİDİ (F1): G G R T G R G G G R B R  → G 6/12 = %50 (sınır) ·
  K yok (F1'de merkezî seçim yok, D8 tohum) · S yok ⚠️ → S3 boş ufuk = S
  (nefes görünür, sabit hedef ufuk, tek mikro-ayar) → G G S T G R G G G R B R
  (G 5/12 · S 1 · ilk G ≠ son R ✓) — 03_SIRALAMA'da sahne başına
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅ (S8 tek kare · kinetik bağımsız · 3 kelime)
☑ risk sayımı yazıldı (12/14) ve eşik kararı verildi (malzeme azaltıldı,
  çıkarılamayanlar ÖNLEM/MALİYET/TELAFİ ile)
☑ B5 dörtlüsü tam, BEDEL sahne numaraları taşıyor (S8 · S11 · S31 · S94 ·
  S140 · S151 · S180)
☑ KARAKTER KARTI sekiz satır, her satırda sahne numarası
⬜ SAHİP KARARI bekleyen tek madde: tema etiketi (BEDEL ↔ ENTROPİ) —
  akışı durdurmaz, etiket değişmedi
→ 03_SAHNE_SIRALAMASI.md yazılabilir
```
