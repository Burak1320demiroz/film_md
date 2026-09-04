# 🎬 THE PRESSED FIELD — PLAN

> **Bu dosyada PROMPT YOKTUR.** Prompt başlıkları yalnız bölüm dosyalarındadır.

```
FORMAT:        yatay 2-4 dk (16:9)
ORTAM:         İNCE ATMOSFER — KILAVUZ_REHBERI §3.2 (0,38 g · %0,6 basınç)
TÜR:           bilimkurgu (§4.1 — tek açık dal)
KLİP SÜRESİ:   10,0 s HEDEF
               ⬜ ARAÇTAN ÖLÇÜLECEK [D124]: ilk klip üretilince
               ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
               → ölçüm 10,0'dan saparsa SPEC B bloğu ve ızgara YENİDEN yazılır.
SAHNE SAYISI:  10          RUNTIME: 100 s (1:40) = 10 + (10−1) × 10
LOGLINE:       Bir ölçümcü, hattını bitirmeye çalışırken zeminin taşa döndüğü
               bir alan bulur; alan büyür ve o, hattını sökerek uyarı yapar.
```

```
⚠️ BİLİNÇLİ SAPMA #1 — SÜRE [D74 · kaydı olmayan kapı koşulmamış kapıdır]
   Format bandı 12-18 sahne / 2:00-3:00 (KILAVUZ_REHBERI §2.2).
   Sahip kısıtı (03.09.2026): en fazla 10 sahne. Süre bandın 20 s altında.
   Klip süresi UZATILMADI — uzatmak D124 ölçüm kapısını ve ızgara
   aritmetiğini bozar. Sapma burada kayıtlıdır, başka yerde tekrarlanmaz.

⚠️ BİLİNÇLİ SAPMA #2 — NEGATİF ÇEKİRDEK METİN CÜMLESİ
   §5 çekirdeğinin "no survey markers … nothing in this world has been
   measured, marked out or annotated by anyone" cümlesi bu filmle
   ÇELİŞİR: filmin kahramanı tam olarak ovayı işaretleyen kişidir ve
   çubuklar novumun taşıyıcısıdır. A1 çelişkisi (yasak ↔ anlatım)
   ÜRETİMDEN ÖNCE görüldü ve çözüldü: metin yasağı KAPSAMIYLA korunur
   ("no readable text … anywhere in the frame"), "survey marker" yasağı
   ÇIKARILIR, yerine POZİTİF cümle gelir: "the rods are blank metal".
   Kaynak: 03_PLAN_ONCESI A1 · D138 (kapsam) · D50 (yasak anlatımı siler).
```

---

## 🎭 TEMA

```
TEMA: İLK-TEMAS
      (sayaç tokeni TİRELİDİR — boşluklu yazılan etiket sayımdan düşer)
      Bu film, kendini hiç göstermeyen ama kanıtını bırakan bir şeyle
      karşılaşmanın insanı ne yapmaya ittiği hakkındadır.

MOTİF SAHNELERİ: S4 · S5 · S7 · S9
      (TEMA_MUHENDISLIGI §5 · İlk temas satırı: motif = ÖLÇEK UYUŞMAZLIĞI,
       kinesik = başın ani kalkışı + gövdenin donması, nesne = izin kendisi)
      S4  ölçek uyuşmazlığı — alan ufka kadar, figür kadrajın ~%4'ü
      S5  kinesik — baş ani kalkar, gövde bir saniye tam durur
      S7  ölçek uyuşmazlığı ② — kurduğu halka alanın yanında gülünç küçük
      S9  nesne = izin kendisi — iz sayısı ikiden sıfıra düşer
      ⭐ B3 çapraz kontrolü: BEDEL sahnesi (S7) bu listededir ✅ —
        tema olay örgüsüne bağlıdır, süsleme değildir.
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ:          fiziksel yasa (§1 birinci tercih)
NOVUM:               Bir şeyin geçtiği yerde gevşek toz kalıcı olarak taşa
                     sıkışır — ve sıkışma o geçtikten SONRA da yayılmaya
                     devam eder.
NOVUM TAŞIYICISI:    ölçüm çubuğu × tokmakla zemine sürme jesti → çubuk
                     sertleşmiş alanda hiç girmez, bir adım ötede dize
                     kadar gömülür
TEK KARE (§4①):      Aynı kadrajda yan yana iki ölçüm çubuğu: biri dize
                     kadar gömülü, öteki yüzeyde duruyor ve ucu bükülmüş
                     (S6 · taşıyıcı nesne karenin içindedir [D157①])
KİNETİK BAĞIMSIZLIK: kural yalnız eylemle kanıtlanır — çubuk girer / girmez,
                     bot iz bırakır / bırakmaz. Replik yok, dış ses yok,
                     ekran metni yok ✅
BAŞLIK ŞEMASI:       "THE PRESSED FIELD" — 3 kelime ≤5 ✅ ve izleyiciye
                     nereye bakacağını söyler: ZEMİNE
```

```
⛔ D76 NEGATİF NOVUM KURALI — bu filmde YOKLUK İKİNCİ KANALDIR
   Taşıyıcı POZİTİF bir nesnedir (çubuk) ve pozitif bir şey yapar
   (girmez, bükülür). Yokluk (iz oluşmaması) yalnız İKİNCİ kanaldır ve
   D76 reçetesiyle SAYIM olarak yazılır:
     "on the loose side there are exactly TWO boot prints, each pressed
      to half the depth of the sole; on the pressed side the print count
      is ZERO — no dent, no scuff, no rim, no edge line, no object"
   Yokluğun KENARI tarif edilmez; SAYIM tarif edilir (2 ↔ 0).

⛔ D157③ NOVUM SAHNESİNDE İKİNCİ OLAY YOKTUR
   Kuralın kanıtlandığı klipler S0 · S1 · S2 · S6 · S9. Bu beş klipte
   kadrajda başka HİÇBİR ŞEY hareket etmez: toz kalkmaz, gökyüzü sabit,
   uzak çubuklar kımıldamaz. Rakip olay varsa kural değil rakip üretilir.

⛔ D172 TAŞIYICININ ASKISI — çubuk hiçbir şeye BAĞLI DEĞİLDİR
   Prompt her novum sahnesinde çubuğun NE OLMADIĞINI yazar:
     "the rod is a plain solid bar: nothing is attached to it, no cable,
      no cord and no line runs from it, nothing hangs from its top; the
      mallet is a plain hand tool and touches nothing except the rod cap"
   Sebep: boş bir askı yuvası model tarafından DOLDURULUR ve mekanizma
   sanılır (THE LEANING ROOM: sekiz merceğin sekizi kordonu halat okudu).
```

## 👁️ UZAYLI VARLIK — `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` ilk uygulaması

```
VARLIK NİYETİ:  S0-S4 DEHŞET (belirsiz fail · HADD tetiklemesi)
                S5-S9 HUŞU  (ölçek: süreç ufka kadar, insan onun içinde)
                ⛔ Geçiş SIRALIDIR; aynı kadrajda ikisi birden istenmez.

VARLIK KARTI (kılavuz §6 · iki satır zorunlu)
  ÖLÇÜM:       İnce kohezyonlu regolit basınç altında kalıcı olarak
               kompaktlaşır — Apollo bot izlerinin kalıcılığı aynı
               mekanizmanın küçük ölçeğidir. Ve düşük yerçekimi AĞIRLIĞI
               azaltır, KÜTLE ile ATALETİ azaltmaz [D169 · TUR 7 rapor 4].
               → 0,38 g'de bu derinlikte iz bırakmak için gereken kütle
                 Dünya'dakinden yaklaşık 2,6 kat FAZLADIR.
  SPEKÜLASYON: Ayağı olmayan, yükünü tek sürekli temas yüzeyine dağıtan
               bir kütle. Geçtiği yerde toz taşa döner; sertleşme o
               geçtikten sonra da yayılır. Bu yüzden "o nerede?"
               sorusunun cevabı yoktur — ekranda olan şey varlığın
               kendisi değil, bıraktığı SÜREÇTİR.

VARLIK ŞERİDİ (kılavuz §5 · 1 karakter = 1 sahne · K0-K4)
  S0 S1 S2 S3 S4 S5 S6 S7 S8 S9
   0  0  0  0  0  1  1  1  1  1
  K0 = iz (varlık 0 kare, etki var) · K1 = çevre tepkisi (alan BÜYÜYOR)
  ⛔ K2-K3-K4 BU FİLMDE YOK. Varlığın gövdesi, uzvu, gölgesi ve yansıması
    10 sahnenin 10'unda 0 KARE. Gerekçe: 04_ARASTIRMA §T7.5 madde 2 —
    ilk uygulamada KART 2 riski asgariye indirilir, kılavuzun yarısı
    (iz · çevre · ses · anlatı) yine sınanır; tam form ikinci filme kalır.
    Sıçrama yok, iniş yok: şerit tek kademe tırmanır ve S5'te tırmanır.
```

---

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Ölçüm hattını kapatmak — ovanın karşı ucuna kadar çubukları
              saplayıp hattı bitirmek. Film başlamasa da süren bir iştir;
              ilk çubuk daha kadraj açılmadan saplanmıştı.
   □ ENGEL:   Hattın üstünde zeminin taşa döndüğü bir alan var; çubuk
              oraya girmiyor ve alan büyüyor.
   □ BEDEL:   Hattı bitirmekten VAZGEÇİYOR — saplı çubukları söküp
              uyarı halkası olarak yeniden diziyor. Geldiği sebebi,
              yaptığı işi ve dönüş güzergâhının işaretini kaybediyor.
              · S7 ⭐ (sökme) · sonucu S8'de kadrajda görünür
   □ MUHATAP: ORTAMIN KALICI DEĞİŞEN PARÇASI — sökülüp yeniden dizilen
              çubuk halkası. S8 ve S9'da kadrajda durur; filmden sonra da
              orada kalacak tek insan işareti odur.
B5b □ AYRILIK: YOK — tek insanlı film (madde yalnız iki insanlı planda)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  referans karesi (S6 iki çubuk) → S7 DORUK/merkezî seçim → S9 kapanış
  → S0 hook → S5 orta nokta → S4 ölçek → S8 → S2 → S3 → S6 → S1
```

```
⭐ D158 SAYIMLARI — plan aşamasında, üretimden önce
  B2a MERKEZÎ SEÇİMDEN SONRAKİ SEÇİM SAYISI: 1
      (S8 — halkanın NEREYE dizileceği; alanın kenarına değil, bir
       çubuk boyu DIŞINA. Bilerek yutulacak bir işaret koyar.)
      Koda uzunluğu: 2 sahne (S8-S9) — 3-5 bandının altında ✅
  B2b BAŞARISIZ DENEME SAYISI: 2
      S1 çubuk taştan sekip elinden çıkar · S2 zorlar, çubuk BÜKÜLÜR
      ⭐ Bükük çubuk filmde KALICI nesnedir: S6'da ölçüt, S8'de halkanın
        ilk parçası. Başarısızlık atılmaz, alete dönüşür.
```

---

## 🗺️ SAHNE HARİTASI

| S | Kurulum | Ölçek · açı tipi | Vuruş | İçerik | Palet | Ses dokusu | Varlık |
|:-:|:-:|---|---|---|---|---|:-:|
| 0 | **C** | ECU · tepe (90°) | açılış imajı + kanca | Bot ökçesi sınıra basar: toz tarafta iz oluşur, taş tarafta hiçbir şey olmaz | gri-devetüyü, tek kontrast | nefes + kuru toz hışırtısı | K0 |
| 1 | **E** | CU · göz hizası | kurulum + katalizör (≤0:15) | Çubuğu toza sürer: girer. Bir adım öteye sürer: seker, elinden çıkar ⭐VİRAL#1 | lacivert + turuncu şerit | nefes + iki boğuk tokmak | K0 |
| 2 | **B** | MS · alt açı (−25°) · profil | tartışma | Zorlar. Dördüncü vuruş birincisinden yavaş. Çubuk BÜKÜLÜR | tarçın gök bandı + pas zemin | zorlanma nefesi + boğuk vuruş | K0 |
| 3 | **D** | WS · üst açı (+30°) · 3/4 | tartışma ② | Geri çekilir; alanın kenarı kadrajın iki yanından da taşar | düzleşmiş pas + düz gri şerit | rüzgâr yok, yalnız nefes | K0 |
| 4 | **A** | EWS · göz hizası · cephe | ölçek / kapak anı | Ova ufka kadar. Hattı ileri gider, alan onu keser. Figür kadrajın ~%4'ü | tam tarçın gök + ufuk | ince atmosferin boğuk sessizliği | K0 |
| 5 | **D** | WS · üst açı · 3/4 | **ORTA NOKTA** (50 s) | Geriye döner: kendi iki çubuğunun ARASI da artık düz. Alan arkasında da | pas + ikinci gri leke | nefes hızlanır, tempo değişir | **K1** |
| 6 | **B** | MS · alt açı · profil | doğrulama | Yeni çubuğu bükük çubuğun yanına sürer: biri dize kadar girer, öteki durur | yakın pas + iki metal dikey | tek boğuk vuruş, sonra sessizlik | K1 |
| 7 | **E** | CU · göz hizası | **DORUK · MERKEZÎ SEÇİM** (%75) | Kendi hattından bir çubuğu SÖKER. Bedel ödenir ⭐VİRAL#2 | lacivert + turuncu + toz | ⭐ SESSİZLİK BIÇAĞI, sonra çekiş | K1 |
| 8 | **B** | MS · alt açı · profil | seçim ② | Sökülen çubukları alanın bir çubuk boyu DIŞINA yay hâlinde diker | pas + üç dikey + boş kovan | adım + toz + saplama | K1 |
| 9 | **C** | ECU · tepe (90°) | **kapanış imajı** ⚡ŞOK | Aynı kadraj. Ökçe basar, iz YOK. Son çubuğun dibi ucu girmeden durur | tek gri yüzey, kontrast yok | tek nefes, sonra hiç | K1 |

```
⛔ ÖRÜNTÜ KIRICI KAPISI [KURGU_RITMI §2] — ardışık İKİ sahne aynı ölçek +
   aynı palet + aynı ses dokusunda OLAMAZ. Yukarıdaki üç sütun alt alta
   okundu: 9 ardışık çiftin 9'unda ÜÇÜ DE değişiyor ✅
```

## 📐 KURULUM DİZİSİ VE AÇI YAYI (`ACI_YAYI` §3-4 · `KAMERA_ACISI` §2/§5)

```
DİZİ:  C · E · B · D · A · D · B · E · B · C
KURULUM SAYISI: 5  (10 sahne → sahne sayısının yarısını geçmez ✅)
AÇI TİPİ SAYISI: 5 — tepe · göz hizası · alt açı · üst açı · profil
                 (≥3 şartı ✅; üç kurulumun üçü de alttan bakmıyor)

KURULUM KÜNYELERİ (kelimesi kelimesine promptlara geçer)
  A  EWS · 32 mm · göz hizası, cephe        · kamera 60 m · yükseklik 1,6 m
  B  MS  · 50 mm · alt açı 25°, tam profil  · kamera 4 m  · yükseklik 0,5 m
  C  ECU · 100 mm macro · tepe, dik aşağı   · kamera 0,9 m · dik bakış
  D  WS  · 75 mm · üst açı 30°, üç-çeyrek   · kamera 14 m · yükseklik 6 m
  E  CU  · 75 mm · göz hizası, cephe        · kamera 2,2 m · yükseklik 1,6 m

GÜVENLİ BANT DENETİMİ (ardışık çift: ≥1 tam ölçek kademesi VE ≥45°)
  S0→S1 ECU→CU 1 kademe · tepe↔göz hizası 90°        ✅
  S1→S2 CU→MS  1 kademe · cephe göz↔profil alt 115°   ✅
  S2→S3 MS→WS  1 kademe · alt 25°↔üst 30° + azimut    ✅
  S3→S4 WS→EWS 1 kademe · üst 30° + azimut 45°        ✅
  S4→S5 EWS→WS 1 kademe · aynı fark, ters yön         ✅
  S5→S6 WS→MS  1 kademe · üst↔alt + azimut            ✅
  S6→S7 MS→CU  1 kademe · profil alt↔cephe göz        ✅
  S7→S8 CU→MS  1 kademe · cephe göz↔profil alt        ✅
  S8→S9 MS→ECU 2 kademe · alt 25°↔tepe 90°   ⚡ BİLİNÇLİ ŞOK 1/2
        gerekçe: finalin kırılma anı — kamera yerden ayrılıp dik aşağı
        bakar ve izleyici kadının nerede DURDUĞUNU görür (ACI_YAYI §3
        "kozmik keşif" bandı). Şok bütçesi: 1 kullanıldı, 1 kullanılmadı.

DERECE DENETİMİ [KAMERA_ACISI §5 abartı eşikleri]
  alt açı 25° (15-30 meşru ✅) · üst açı 30° (15-30 meşru ✅) ·
  tepe 90° AYRI AÇI TİPİDİR, 45-60° ölü bölgesine girmez ✅ ·
  eğik/dutch: KULLANILMADI (0 sahne)

S1 ↔ SON SAHNE İLİŞKİSİ: bilinçli KAPANIŞ KONTRASTI (döngü değil).
  S0 ve S9 AYNI kurulum (C), ZIT içerik: iz var ↔ iz yok.
  Açılış-kapanış çifti tek karar olarak verildi [SENARYO_VE_VIRAL §2.3③].
```

---

## 🎯 VURUŞ HARİTASI (`SENARYO_VE_VIRAL_KAMERA` §2.2 · 100 s'ye ölçeklendi)

| Vuruş | Yüzde | Sahne | Saniye |
|---|:--:|:--:|:--:|
| Açılış imajı | %0-10 | S0 | 0-10 |
| Kurulum | %0-20 | S0-S1 | 0-20 |
| Katalizör | ~%12 | S1 (ikinci yarı) | 15-20 ⛔ 0:15 kapısı |
| Tartışma | %20-40 | S2-S3 | 20-40 |
| Orta nokta | ~%50 | S5 | 50-60 |
| Her şeyin kaybı | ~%70 | S6-S7 | 60-80 |
| Umut-önce-düşüş | kayıptan önce | S6 sonu (çubuk girer!) | 68-70 |
| Doruk / merkezî seçim | ~%75 | S7 | 70-80 |
| Final | %85-99 | S8-S9 | 80-100 |
| Kapanış imajı | %100 | S9 | 90-100 |

```
⭐ VİRAL KARE KAPISI [§2.4 · her etiket İKİ satır taşır]

⭐VİRAL S1 · YÜZ:     gözler çubuk ucundan hızla kalkar, kaşlar yükselir
                      (AU2); değişim 1,5 saniyede tamamlanır
             HAREKET: çubuk sertleşmiş yüzeyden sekip elinden çıkar ve
                      kadrajın alt kenarına doğru savrulur

⭐VİRAL S7 · YÜZ:     gözler kapanır ve açılır, çene kilitlenir — karar
                      anı; değişim 2,0 saniyede tamamlanır
             HAREKET: sökülen çubuk tozdan çıkarken üzerinden bir toz
                      kabuğu ayrılır ve tek parça hâlinde düşer

⛔ İkisi de E kurulumundadır (CU, cephe): vizör ardındaki yüz okunur —
   D79 açık vizör kilidi bu kapının ÖN KOŞULUDUR ✅
⛔ İKİSİ DE KESİLEMEZ (SPEC A bloğu VIRAL INTERSTITIALS)
```

## 🪝 HOOK VE FİNAL

```
HOOK TİPİ:  YANLIŞLIK KOMPOZİSYONU [HOOK §4]
            Tamamen normal bir toz yüzeyi + TEK anormal öğe: yüzeyin
            yarısı basıncı almıyor. Anomali TÜRETİLMİŞ DEĞİL somuttur
            (zemin dokusu) → D73'ün tek-kare fizibilite riski YOK.
0. KARE:    tek güçlü görsel fikir — kadrajı çapraz kesen iki doku.
            120 px testi: sınır çizgisi posta pulu boyunda okunur ✅
AÇILIŞ:     hareketin ortasında — ökçe zaten inmekte [HOOK §2.2]
S0 ÇIKIŞ SORUSU (plana yazılır): "Neden yarısı basıncı alıyor?"
S1 GÖREVİ:  soruya CEVAP VERMEZ, BÜYÜTÜR — sorun ayakta değil, ALETTE de
            var. Bilgi eşitliği: karakter de bilmiyor ✅ [HOOK §3②]

FİNAL TİPİ: TERSİNE DÖNÜŞ (twist) + muğlak kuyruk
            Film boyunca alanın DIŞINDA sandığımız kadın, sonda içindedir.
TOHUM BİLGİ [FINAL §3 · pencere 15-22 s → S1]:
            S1'de, odak dışında, sol üst arka planda ~1,5 saniye: geldiği
            hattın iki çubuğu ARASINDAKİ toz artık pürüzsüz. Bakışla
            VURGULANMAZ. Final oraya döner (S5 aynı yer, büyümüş hâli).
            ⛔ Bu bilinçli tohumdur ve SPEC C bloğuna PLANTED DETAIL
              kilidi olarak yazılmıştır [UZAYLI_VARLIK §5 · T7.4③].
```

---

## 🧑‍🚀 CHARACTER BIBLE — kelimesi kelimesine kopyalanır [SAHNE_DEVAMLILIK §2.1]

> ⛔ Özel ad promptta GEÇMEZ [D34/D45]. Milliyet GEÇMEZ [§7 doğrulanmış red].
> ⛔ Kimlik özniteliği bir cümlede EN FAZLA ÜÇ [D167 · ⑲ kimlik yığını]:
> burada yaş + ten + saç ayrı cümlelere dağıtılmıştır, boy/gövde YAZILMAZ.

```
A woman in her mid-thirties in a matte navy pressure suit. Her skin is
medium brown with visible pores; her dark hair is cropped close under the
helmet ring. A bold burnt-orange fabric stripe is wrapped around her RIGHT
forearm and her RIGHT thigh. A textless circular badge with a thick
metallic silver chevron on dark navy sits on her right chest. A shallow
open quiver is clipped at her LEFT hip. The suit has no back-mounted unit:
no backpack, no tank, no hose and no cable — her back silhouette is flat
and the back of the suit is one continuous smooth panel from collar to
hip, carrying nothing. The visor is optically clear glass with zero tint,
zero mirror coating and zero reflection of the environment; her face is
fully readable through it in every frame, at every head angle.
```

**Rol okunurluğu (isim = ROL, ilk %10'da):** turuncu şerit + kalça kovanı +
elindeki tokmak → ölçümcü. Ad gerekmez [KARAKTER_VE_DUYGU §3].

## 🌍 WORLD BIBLE

```
A flat open dust plain on a thin-atmosphere world: 0.38g surface gravity,
0.6% of Earth's pressure. The sky is a cinnamon-ochre haze. Light is
heavily diffused by suspended dust, so shadows are soft-edged but clearly
present and every surface keeps visible texture. The dust is fine, pale
rust-grey and cohesive. HORIZON LOCK: flat open plain to the horizon in
every direction — no cliffs, no canyon walls, no rock walls and no ridge
nearer than the horizon line; nothing stands higher than knee height
within five hundred metres except the survey rods themselves.
```

```
⛔ D145 ALÇAK AÇI KİLİDİ — B kurulumunun (alt açı) her promptu GÖĞÜ yazar:
   "because the camera is low, the horizon sits in the bottom third of the
    frame and everything above it is empty cinnamon-ochre sky"
⛔ D39 TOZ — ince atmosfer: toz YAVAŞ ama KESİN çöker. "swirl" yasak.
⛔ D41 — gölge yumuşak kenarlı MEŞRUDUR; bloom teşhisi DOKU KAYBINA bakar.
⛔ D147 AŞINMA MERDİVENİ (monotonik — toz yalnız EKLENİR, hiç silinmez):
     PHASE 1  S0-S2  dizler ve önkollar hafif tozlu
     PHASE 2  S3-S6  dizler, önkollar ve kalça kovanı gri tozla kaplı
     PHASE 3  S7-S9  önceki her şey + eldivenlerin içi ve göğüs paneli tozlu
   Her prompt kendi faz satırını taşır; faz ASLA geriye gitmez.
```

## 💡 LIGHTING BIBLE

```
A single low sun about 12 degrees above the horizon, behind and to the
camera-left of the field, so the ground relief rakes into long soft-edged
shadow — this raking light is the only reason a pressed surface reads
differently from a loose one. Heavy atmospheric fill from suspended dust.
No bloom, no glow, no haze bloom: texture is preserved everywhere.
```

```
⛔ KART 9 DÖRT KANAL PANZEHİRİ [ışık mıknatısı · D104]
   Tek baskın ışık kaynağı (alçak güneş) VAR. Karakter kadraj içinde yer
   değiştirdiği her sahnede dört kanal birden yazılır:
     ① hedef-dilim + yön ("the boundary holds the right third throughout")
     ② omuz hattı ("her shoulders stay square to the boundary")
     ③ ışığa göre poz ("the low sun is behind her camera-left shoulder —
        it rims her back; she never turns to face it")
     ④ yön negatifi ("no one walks toward the sun, no direction reversal")
   ⛔ İKİ YENİLGİ KURALI: iki redden sonra üçüncü yeniden yazım YOK —
     kamera hedefe taşınır [UZAMSAL §6.8].
```

## ⚖️ PHYSICS BIBLE — sayısal kilitler (C bloğu · ⑥ FİZİK merceği ölçer)

```
GRAVITY LOCK          0.38 g — serbest düşen bir nesne ilk saniyede 1,9 m
                      yol alır, düz yay çizer, havada asılı kalmaz.
MASS ≠ WEIGHT [D169]  0,38 g ağırlığı azaltır, KÜTLE ve ATALETİ azaltmaz:
                      tokmak vuruşu ve çubuğu başlatma/durdurma AYNI eforu
                      ister; basınçlı eldiven kapanmaya direnir.
HUMAN COUNT LOCK      tam 1 insan, 10 sahnenin 10'unda. Mürettebat yok,
                      araç yok, ikinci figür yok, klon yok, yansıma yok.
CREATURE COUNT LOCK   0 kare, 10 sahnenin 10'unda. Varlığın gövdesi, uzvu,
                      gölgesi ve yansıması hiçbir karede YOKTUR.
HELMET STATE SCHEDULE kapalı S0-S9 (10 sahne) · açık 0 sahne
QUIVER ROD COUNT      S2 dört · S3 üç · S5 üç · S8 sıfır (monotonik, hiç
                      artmaz). ⛔ S6 ve S7 EYLEM sahnesidir — kovan sayımı
                      o iki sahnede KİLİTLENMEZ (sahne içinde değişiyor).
ARC ROD COUNT         S8'de yayda tam ÜÇ çubuk dik durur · S9'da kadrajda
                      tek çubuğun dibi
PRINT COUNT [D76]     gevşek tarafta tam İKİ bot izi, her biri taban
                      derinliğinin yarısı kadar · sertleşmiş tarafta
                      iz sayısı SIFIR: çukur yok, sürtme yok, kenar
                      çizgisi yok, hale yok, nesne yok
ROD DEPTH LOCK        gevşek tozda çubuk diz yüksekliğine kadar girer ·
                      sertleşmiş yüzeyde HİÇ girmez, uç bükülür
BOUNDARY LOCK         sınır bıçak gibi keskindir: geçiş bandı bir avuç
                      genişliğinden dardır, ışıkta parlamaz, renk
                      değiştirmez — yalnız DOKU değişir
DUST LOCK [D39]       toz tek tek zerreler hâlinde, ayrı balistik yollarda
                      yavaşça çöker ve yüzeye oturur; girdap yok, kıvrım
                      yok, bağlı kütle yok, su altı hareketi yok
```

> ⛔ **ÖLÇÜ PROMPT GÖVDESİNDE DURMAZ [D138].** Yukarıdaki metre/derece
> değerleri SPEC'te yaşar. Gövde nesne-göreli yazar: *"the pressed ground
> reaches about three body-lengths past her on every side"*.

---

## 🎬 KAMERA VE KURGU

```
CAMERA MOVE:  fixed lockoff — kamera KLİP İÇİNDE hiç hareket etmez.
              Zoom yok, pan yok, tilt yok, track yok, kesme yok [KART 8].
              ⛔ Sahneler ARASI kurulum değişimi bu karardan MUAFTIR ve
                zorunludur (§Kurulum dizisi) — KART 8 kapsam bloğu.
TARGET ASL BAND: 10,0 s (sabit ızgara — eğri yok, bilinçli sapma)
              GEREKÇE [D74]: bu hattın her klibi tek çekimde üretilir ve
              sahne = çekim = klip. Kırpma bütçesi 0 s; ASL eğrisi
              (KURGU_RITMI §1) uygulanamaz çünkü kırpılacak fazlalık ham
              malzeme yoktur. Ritim KADRAJ İÇİNDEN gelir: ölçek her
              sahnede değişir (örüntü kırıcı tablosu).
ASL CURVE:    ①10,0 ②10,0 ③10,0 ④10,0 ⑤10,0  (sabit — yukarıdaki gerekçe)
RAW FOOTAGE:  10 klip × 10,0 s = 100 s · TRIM BUDGET: 0 s
SCREEN TEXT:  0,0 saniye — başlık kartı YOK, jenerik YOK, alt yazı YOK
```

## 🎞️ KARAKTER VE DUYGU BÜTÇESİ [KARAKTER_VE_DUYGU §6 · 10 sahneye ölçekli]

```
👁️ göz görünürlüğü      S1 · S7                     (2 sahne ✅)
🔁 tepki planı           S1 · S3 · S5 · S7           (4 sahne ✅)
✋ el / mikro-jest       S1 · S7                     (2 sahne ✅)
🚶 tam boy yürüyüş       S2 · S8                     (2 sahne ✅)
🎒 kişisel eşya          S6 (bükük çubuk artık eşyadır) (1 sahne ✅)
🌌 ölçek kontrastı 1:10  S4                          (1 sahne ✅)
🔁 Kuleshov döngüsü      S3-S4-S5 · S5-S6-S7 · S7-S8-S9  (3 döngü)
   ⚠️ tablo 15 sahne için ≥5 der; 10 sahnede orantı ≈3,3 → 3 döngü
     yazıldı ve bu bir HESAP çıktısıdır, gevşetme değil.
🔇 "her şey kayboldu"    S7 — sesin sustuğu, yalnız nefesin kaldığı sahne
```

## 🖼️ PAKETLEME

```
KAPAK ANI: S4 · 4,0 s · figür alt-sol üçte birde, sertleşmiş alan ufka
           kadar uzanır · alçak yalpa güneşi · odak figürde, alan yumuşak
           ⛔ Kapak METİNSİZ üretilir (KAPAK_FOTOGRAFI mimarisi).
VAAT:      başlık ZEMİNE bakmayı söyler; teyit S0'ın ilk saniyesindedir.
SPOILER BÜTÇESİ: kapakta çubuk halkası GÖRÜNMEZ (S7-S8 vuruşu korunur).
```

---

## 🃏 RİSK SAYIMI (`02_RISK_KARTLARI` · payda 13)

```
□ Su/sıvı                          YOK ✅        (0 kare su, 0 kare buz)
■ Canlı                            VAR → KART 2 · 0 KARE (aşağıda)
■ Kask/vizör                       VAR → KART 3 · HELMET STATE SCHEDULE
■ İkinci figür                     her filmde → KART 4 · HUMAN COUNT LOCK
■ Ekran/sayaç                      VAR → KART 5 · METİNSİZ (çubuk sayacı)
■ Parçacık/toz                     VAR → KART 6 · DUST LOCK [D39]
□ Katmanlı dünya                   YOK ✅
□ Diyalog                          YOK ✅        (0 replik — aşağıda)
□ Kamera hareketi                  YOK ✅        (klip içi lockoff)
■ Tek baskın ışık + hedefe hareket VAR → KART 9 · dört kanal panzehiri
□ İnsansız sahne                   YOK ✅        (KART 10 hiç doğmaz)
□ Değişken çekim süresi            YOK ✅        (sabit 10,0 s ızgara)
■ Politika yüzeyi                  VAR → KART 12 · B6 satırı (aşağıda)

RİSK SAYISI: 7 / 13     ⚠️ 5+ bandında.
```

```
⚠️ 5+ BANDI OKUMASI — dürüst ayrıştırma
   Yedi riskin üçü BU HATTIN TABANIDIR ve hiçbir uzay filminde
   sıfırlanamaz: kask · ikinci figür · toz.
   İkisinin çözümü PLANDA UYGULANMIŞTIR ve mekanizması nötrlenmiştir:
     · CANLI → 0 kare. KART 2'nin bozulma mekanizması (anatomi kare kare
       değişir · kayarak yürür · temasta geometri erir) hiç tetiklenmez;
       kartın kendi ALTERNATİF satırının tam uygulaması budur.
     · SAYAÇ → metinsiz, fiziksel, monotonik. KART 5'in iki yönlü riski
       (fazla metin ↔ anlatımın silinmesi) A1 taramasıyla kapatıldı.
   Geriye gerçekten AKTİF iki risk kalır: KART 9 (ışık mıknatısı) ve
   KART 12 (politika yüzeyi). İkisinin de panzehiri yazılıdır.
   ⛔ Ve KART 12'nin kendi uyarısı geçerli: "5+ sayarken KART 12'yi say,
     ama malzeme kesme kararını ondan BAŞLATMA."

⭐ GERÇEK MALZEME AZALTMASI — iki tanesi, bilinçli
   ① REPLİK 0. Gerekçe GÜVENLİK DEĞİLDİR (02.09.2026'da "sessizlik en
     güvenli" damgası kaldırıldı ve bu plan onu geri getirmez).
     Gerekçe TASARIM: bu filmin motoru izleyicinin kendi çıkarsamasıdır —
     görünmeyen bir failin varlığını izlerden kurmak. Kayıt/telsiz sesi
     bir anlatıcı koyar ve çıkarsamayı KARAKTERE devreder; o zaman
     izleyici düşünmez, dinler. Sessizlik burada bir araçtır.
     ⚠️ Bedeli kabul edildi: `SES_VE_DIYALOG` yine kullanılmadı ve
       06_HIKAYE_HATTI_TESHISI'nin "replik 0/79" sayacı 0/80 olur.
   ② VARLIK 0 KARE. Gerekçe: 04_ARASTIRMA §T7.5② — yeni kılavuzun ilk
     uygulamasında en ucuz sınav budur.
```

## 🛡️ B6 — POLİTİKA SATIRI VE ANLAM MALİYETİ [`03_PLAN_ONCESI` B6]

```
EN RED-RİSKLİ KARE: S2 — tokmakla zemine vuruş (alete yönelmiş kuvvet +
  zorlanma sözlüğü + alçak açı yakın kadraj).
NÖTR TARİFİ: kuvvet gövdeye değil ALETE ve ZEMİNE yazılır; darbenin
  sonucu malzemede okunur, bedende değil —
  "the flat of the mallet comes down on the rod cap, once, then again;
   the rod tip does not enter and the shaft takes a slow bend"
  ⛔ "strike/hit/slam + gövde parçası" kalıbı hiçbir promptta YOK.

ÖNLEM / MALİYET / TELAFİ [POLİTİKA §4.3 — TELAFİ boşsa önlem alınmamıştır]
  ÖNLEM:   varlığın gövdesi hiç gösterilmiyor (0 kare)
  MALİYET: "canavarı görme" doyumu yok; tek-kare kapak anı zayıflar
  TELAFİ:  aksiyon MALZEME SONUCU kanalına taşındı (§4.1) — zeminin
           taşa dönmesi, bükülen çubuk, kaybolan iz. Üçü de sayılabilir
           ve üçü de kadrajda gerçekleşir.
  ÖNLEM:   replik yok
  MALİYET: istek/bedel sözle söylenemez
  TELAFİ:  istek NESNEYE bağlandı (kovandaki çubuk sayısı = kalan iş),
           bedel EYLEME bağlandı (hattı sökmek) — ikisi de kadrajda sayılır

MİLLİYET · GERÇEK KURUM · GERÇEK KİŞİ ADI: planın hiçbir yerinde YOK ✅
```

## 🔎 A4 — YASAKLI SAHNE TİPİ TARAMASI [D77]

```
□ araç/kapak/airlock biniş-iniş hareketi          YOK ✅ (araç 0 kare)
□ tek ışıklı loş iç mekâna giriş                  YOK ✅ (film tamamen dış)
□ aynalı-yansıtıcı yüzey önünde tek karakter      YOK ✅ (vizör "zero
    mirror coating, zero reflection" — D79 kilidi zaten bunu yasaklar)
□ novum'u TÜRETİLMİŞ optik fenomen taşıyor        YOK ✅ (taşıyıcı SOMUT:
    çubuk + zemin dokusu; gölge/yansıma/kostik değil)
□ novum'u bir YOKLUK taşıyor [D76]                KISMEN → ÇÖZÜLDÜ ✅
    Taşıyıcı POZİTİFTİR (çubuk girmiyor, bükülüyor). Yokluk (iz
    oluşmaması) İKİNCİ kanaldır ve D76 reçetesiyle SAYIM olarak yazıldı
    (PRINT COUNT: 2 ↔ 0). Yokluğun kenarı tarif EDİLMEZ.
□ jenerik / başlık kartı / kapak çıktısı          YOK ✅ (SCREEN TEXT 0,0 s)
```

## ✅ A1-A3 — PLAN KENDİ İÇİNDE ÇELİŞİYOR MU

```
A1 □ "no readable text" yasağı VAR; ekran/gösterge İÇERİĞİ tarif edilen
     tek satır YOK. Bilek göstergesi yalnız "a faint amber pulse" olarak
     geçer — rakam, harf, sembol veya okunur içerik YOKTUR ✅
     ⭐ Ve çekirdeğin "no survey markers" cümlesi ÇIKARILDI (Sapma #2):
       o cümle kalsaydı filmin taşıyıcısını yasaklardı — bu tam olarak
       D50'nin (Tidal Hunt sayacı) tekrarı olurdu.
A2 □ başlıkta 10 sahne · bölüm dosyalarında 10 blok · promptlarda
     "Scene N of 10" — üçü de aynı ✅ (bitişte betikle doğrulanır)
A3 □ 10 sahne × 10,0 s = 100 s = 1:40 = iddia edilen süre ✅
```

## 🎯 B1 — DORUK ANI BİR SAHNENİN İÇİNDE Mİ

```
Doruk S7'nin İÇİNDEDİR ve promptta tarif edilir: çubuğun tozdan çıkışı
0-10 s aralığında, tek kesintisiz klipte. İki sahnenin ARASINA düşen
hiçbir vuruş yok — S6 (kanıt) ve S8 (sonuç) doruğun iki yanıdır ve
doruğun KENDİSİ S7'dedir.
KAYIP GÖRÜNÜRLÜĞÜ: hattın söküldüğü S7'de başlar, S8'de kadrajda
tamamlanır (yayda üç çubuk dik, hattın yeri boş).
```

---

## 📋 QA SPEC BLOĞU → AYRI DOSYADIR

⛔ Bu plan SPEC'i İÇERMEZ. SPEC dosyası: `THE_PRESSED_FIELD_QA_SPEC.md`
(Ders 117 · 129: QA anında operatörün eline rubrik + SPEC birlikte verilir;
paket `rubrik_paketle.sh` ile ÜRETİLDİ, QA anında değil yazım anında).

## 📎 BİTİŞ KONTROLÜ

```
□ 03_PLAN_ONCESI 17 maddesi bu dosyada işaretlendi (A1-A3 · A4 · B1 ·
  B1b yok · B2 · B3 · B4 · B5 · B5b yok · B6 · C · D · E)
□ Promptlar yazıldıktan sonra, TEK KARE ÜRETMEDEN → görev kartı P
  python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
          yatay_2_4_dk_filmler_uzay/THE_PRESSED_FIELD
  ⛔ Çıktıda "📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik" satırı YOKSA
    dizi kapıları (kurulum · açı · tema · B5) KOŞMAMIŞTIR.
```

## 🚪 KAPI KAYDI [D74 — kaydı olmayan kapı koşulmamış kapıdır]

```
✅ KART P ADIM 1 — prompt_kontrol.py · klasör modu · 03.09.2026
   "📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik" satırı ÇIKTI (dizi
   kapıları koştu) · 20 prompt · ⛔ 0 BLOCK · ⚠️ 0 FIX · ✅ 3 GO
   video 2.337-2.599 karakter (bant 2.000-2.600 · TAM İÇİNDE)
   image 2.296-2.972 karakter — image bandı (1.700-2.100) KARARA BAĞLI
     (betiğin kendi notu: "bu bant depodaki hiçbir filmle uyuşmuyor");
     depo emsalleri Holding Field 3.417-4.017 · Third Dune 2.732-4.154 ·
     Heavy Side 6.438-6.670 → bu filmin image promptları emsallerin
     ALTINDA. Üretim durdurmaz, GÖZLEM olarak kayda geçti.
   İlk koşuda 3 FIX vardı ve üçü de düzeltildi:
     ① uzunluk (6 video bandın üstündeydi) → sıkıştırıldı
     ② çapasız "toward" (KART 9 yön negatifi cümlesi) → ekran çapası
       taşıyan, TOWARD tetiklemeyen hâle çevrildi
     ③ ⑳ efor kapısının iki YANLIŞ POZİTİFİ: "eyes lift" ve "dust lifts"
       efor fiili sayılıyordu → "rise" ile değiştirildi (gerçek efor
       sahneleri S2 · S7 · S8 zorlanma kanallarını zaten taşıyor)

⬜ KART P ADIM 2 — PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md
   HENÜZ KOŞULMADI. Betiğin göremediği iki eksen orada ölçülür:
   kilit SAYI mı TARİF mi · §3c KOMPOZİSYON YÜZEYİ (kadraj).
   ⛔ Bu rubrik koşulmadan üretime geçilmez.

⬜ KART P ADIM 3 — KARAR (GO / BLOCK). Adım 2 bitmeden verilmez.
```
