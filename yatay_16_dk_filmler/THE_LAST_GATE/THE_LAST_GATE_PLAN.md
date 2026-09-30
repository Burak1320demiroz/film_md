# 🎬 THE_LAST_GATE — PLAN

> **Bu dosyada PROMPT YOKTUR.** Prompt başlıkları YALNIZ bölüm dosyalarındadır.
>
> ⭐ **KANONİK KAYNAK BU DOSYA DEĞİL:** hikâyenin, zaman kodlarının, açıklık
> çizelgesinin, yolcu sayılarının ve replik yerleşiminin tek sahibi klasördeki
> **`00_ANALIZ/00_ON_PLAN/THE_LAST_GATE_KAPSAMLI_PLAN.md`** (sahip · 30.09.2026 · 724 satır). Bu dosya
> o planı ÜRETİME taşır: Bible'lar, kurulum iskeleti, kapı kayıtları. Çelişkide
> kapsamlı plan kazanır ve bu dosya düzeltilir.
>
> Sahibin talimatı: *"kapsamlı planı referans al, sahnelere tek tek çalış, o
> dosyanın dışına çıkmadan yap."* Üç uygulama sapması `00_ANALIZ/00_HIKAYE_ONAYI.md`
> SAPMA bölümünde ve aşağıda §SAPMA'da tek tek yazılı.

```
FORMAT:        yatay 16 dk · 96 KLİP × tam 10,000 s = 960,000 s · 8 BÖLÜM × 12 klip
               (KILAVUZ_REHBERI §2.8 · bu klasörün 2. filmi) · çok klipli sahne rejimi (§2.0b)
               QA birimi PART: PART n = BOLUM_{2n−1} + BOLUM_{2n} (24 klip · 4:00) · 4 PART + TAM FİLM
ORTAM:         §3.1 VAKUM (dış: liman · gövde · geçit · gaz devi) + §3.10 BASINÇLI İÇ HACİM
               (mikrogravite · ~1 atm: kokpit · servis omurgası · hücre/modül omurgası · köprü · M24)
               ⭐ Depoda §3.10'un BASKIN kart olduğu İLK film — ölçüldü: kart 04.09'da açıldı,
               8 filmde geçti, hepsinde ikincildi. Bu film kartın referansı olur.
               ⛔ §3.7 (dönme yerçekimi) KULLANILMAZ — gemi dönmez (kapsamlı plan §7.3).
TÜR:           bilimkurgu · dal: hapishane gemisi kaçırma + kaçış aksiyonu (§4.1)
               §4.3 SAVAŞ kartı ⏸️ RAFTA — yalnız KİLİTLERİ ödünç (SAPMA 4)
MOTOR:         I2V — her klip kendi onaylı başlangıç karesinden (IMAGE promptu = o kare)
               ⛔ son kare zinciri YOK (22.09.2026) · CAMERA satırı locked-off
KLİP SÜRESİ:   10,000 s HEDEF · ⬜ ARAÇTAN ÖLÇÜLECEK [D124]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
               kurgu birimi 24 fps'te TAM 240 kare · kurgu kapısı 960,000 s ±0 · 23.040 kare
SAHNE SAYISI:  25 sahne / 96 klip   RUNTIME: 960,000 s (hook K01–K04, 96'nın İÇİNDE)
ÜRETİLEN KLİP: 92 — K01–K04 kurgu bloğudur, kendi görüntüsü üretilmez (kapsamlı plan §9 · §16)
PROMPT SAYISI: 184 (92 klip × kare + hareket) — kapsamlı plan §16'nın yazdığı sayı
PROTAGONIST:   Mara (34 · eski askerî keşif pilotu) — ⛔ ad promptlarda 0 kez [D34]
LOGLINE:       Eski bir askerî pilot, tutsak kardeşini kurtarmak için hapishane gemisine yanaşır; kardeşi diğerlerini bırakmayı reddedince kapanan geçitten iki yüz kırk yetişkini çıkarmak zorunda kalır.
```

---

## 🎭 TEMA

```
TEMA: DAYANIŞMA  (⏸️ aday etiket — TEMA_MUHENDISLIGI §3b'ye tarihli satır gerekir;
      kanonik ebeveyni FEDAKÂRLIK · emsal GÜVEN ve SORUMLULUK aday etiketleri)
      TANIM CÜMLESİ: "Kendi çıkışını söken, herkesin çıkışını kurmuş olur."
      (TANIM cümlesidir; §3c TAKAS kalıbı DEĞİL)
      Sahibin kendi ifadesi (kapsamlı plan §3): "Dayanışmayla kazanılan özgürlük."

MOTİF SAHNELERİ: S06 · S08 · S17 · S18 · S25
  S06 — iki koltuklu çıkış gösterilir ve REDDEDİLİR (kanca kapıya takılır)
  S08 — kendi aracı dikkat dağıtmaya gider ve kaybedilir (ilk bedel)
  S17 — emniyet bağı uzatılır: tek kişinin kurtulmadığı ilk fizik kanıtı
  S18 — gövde sığmaz; amaç "gemiyi geçirmek"ten "insanları geçirmek"e döner
  S25 — karşılıklı selam: kurtarılan kişi de artık kendi işini yapıyor

MOTİF NESNESİ: emniyet bağı / kanca — S06'da Lina kancasını kapıya takar (reddediş) →
  S17'de Mara bağını uzatır (karşılık) → S23'te bırakma kolunu Lina indirir (devralma)
KİNESİK: tek elle gösterilen çıkış (S06) → iki ucu tutulan bağ (S17) → kaldırılan açık el (S25)
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               SON GEÇİT — sabit bir halkanın içindeki etkin alan, kapanış döngüsü
                     başlatıldığında merkeze doğru MONOTONİK küçülür ve bu film süresince
                     bir daha açılmaz; geçebilecek şeyi belirleyen, geçtiği ANDAKİ açıklık
                     ile cismin hareket doğrultusuna dik dış profilidir. (kapsamlı plan §7.4)
NOVUM TAŞIYICISI:    ETKİN AÇIKLIĞIN PARLAK KENARI × geminin sabit dairesel kesiti →
                     kenar kesitin içine girer ve gemi artık geçemez (K69)
                     İKİNCİ TAŞIYICI: transfer aracının dış profili × aynı kenar (K92)
TEK KARE (§4①):      ✅ K69 · gate ekseninden tek kare — ana basınç gövdesinin dairesel
                     profili ile ETKİN AÇIKLIĞIN PARLAK KENARI çakışıyor, kenar profilin
                     içinde. Taşıyıcının adı cümlede [D157]. K69'da ikinci olay yok.
KİNETİK BAĞIMSIZLIK: ✅ kenarın içe yürümesi (K49) · gemi–kenar çakışması (K69) ·
                     aracın tam geçişi (K92) · alanın sıfırlanması (K93) — hiçbiri replik/metin
BAŞLIK ŞEMASI:       ✅ "The Last Gate" — 3 kelime, izleyici kapanan bir açıklığa bakar
KURAL TEKRARI (§5):  KURULUM K48–K49 · DOĞRULAMA K64 (gemi hâlâ sığar) · İHLAL K69 (sığmaz) ·
                     İKİNCİ NESNE K87 (takip araçları da sığmaz) · SONUÇ K92–K93 → ≥3 sahne · ≥2 nesne ✅
NOVUM KİLİDİ SAYIYLA (metinsiz, monotonik — ekranda GEOMETRİ, promptta ölçü YOK [D138]):
                     K49 açıklık gövdeden çok geniş → K64 hâlâ geniş → K69 gövdeden DAR →
                     K87 takip araçlarından DAR → K92 araçtan bir parça geniş → K93 sıfır
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Kardeşini hapishane gemisinden CANLI çıkarmak — film başlamadan var olan İŞ
              (servis gemisi yolda, geçici erişim anahtarı konsolda, K05'te zaten yanaşıyor)
   □ ENGEL:   kimlik doğrulaması (S04) · içerideki iki muhafız (S04 · S15) · üç araçlı takip
              kuvveti (S12 · S14) · itki hasarı (S14) · kapanan geçit (S13 → S24)
   □ BEDEL:   ⭐ BİRİNCİL — KENDİ ÇIKIŞI · S08 · K30–K32: boş servis aracını dikkat
              dağıtmaya yollar, bir önleme aracı itkisini devre dışı bırakır; iki koltuklu
              özel kaçışı biter ve o an henüz MECBUR DEĞİLDİ.
              İKİNCİL — ELE GEÇİRDİĞİ GEMİ · S18 · K69–K72: gövde sığmaz, terk edilir,
              yalnız siper olarak kullanılır. ÜÇÜNCÜL — gövdenin kıç yapısı · S24 · K91.
              ⛔ Destek karakter ölümü YOK (kapsamlı plan §3 kararı).
   □ MUHATAP: komuta gemisindeki komutan — her insan hamlesine karşı hamle (K14 · K47 · K48 ·
              K53 · K66) + Lina (istek çaprazı: Mara "şimdi çık" ister, Lina "gemiyi uçur" ister)
   □ AYRILIK: S06 · K21–K23 — B5b · aynı fikirde OLMADIKLARI an. Mara iki koltuklu çıkış şemasını
              açar (K21), Lina kancasını hücre kapısına takıp "daha büyük bir gemi" der (K22),
              Mara şemayı kapatıp paneli ona çevirir (K23). Nesne: emniyet kancası.
              İkincil ayrılık S17 · K65–K67 (Lina yüzeyden bilerek ayrılır, Mara bağı uzatır).
İSTEK ÇAPRAZI: Lina, Mara'dan PİLOTLUK ister (K22 · K24); Mara, Lina'dan ÇIKMAK ister (K20 · K21).
              Veyr, Mara'dan pilot olmasını ister (K25). Komutan, tutsakları CANLI ister (K47).
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR

```
— yatay film; bu blok uygulanmaz. Bilgi asimetrisi yine yazılı: DRAMATİK İRONİ —
izleyici komutanın hamlelerini (K14 · K47 · K48) ekipten ÖNCE görür.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| vuruş | klip | ne değişir |
|---|---|---|
| HOOK | K01–K04 | özet açılış: ölçek, gerçek kenetlenme, kardeş, takip, kapanan geçit (dış ses H1–H4) |
| NOVUM KURULUMU | K07 | boş transfer aracı kendi iticileriyle rayına oturur — finalin aracı EKİLİR |
| GERİ DÖNÜLEMEZ EYLEM | K11 | dört sert kenet kapanır; gemiler artık birbirine göre hareket etmez |
| İLK KAYIP | K16 | sol ön kol plakası çizilir — 80 klip boyunca kadrajda kalan tek hasar |
| AYRILIK | K22 | Lina kancasını kapıya takar |
| MERKEZÎ SEÇİM | K23 | "bütün hücreleri aç" — iki kişilik plan kapanır |
| BEDEL 1 | K32 | kendi kaçış aracı devre dışı |
| BÜYÜK KARŞILIK | K41 | 2.400 m gövde beşikten çıkar |
| KARŞI HAMLE | K48 | komutan geçidi kapatır |
| NOVUM İHLALİ | K69 | gemi artık sığmaz |
| BEDEL 2 | K72 | gövde terk edilir, siper olur |
| İLK ÇIKIŞ | K80 | ilk araç raydan ayrılır |
| DORUK | K92 | son araç açıklıktan bütünüyle geçer |
| KAPANIŞ | K93 | etkin geçit sıfırlanır |
| FİNAL | K95–K96 | karşılıklı selam — tema ödenir |

## 🪝 HOOK MİMARİSİ

```
K01–K04 · 0:00–0:40 · DÖRT KURGU BLOĞU — kendi görüntüsü ÜRETİLMEZ (SAPMA 2)
  K01 ← K06                    (ölçek ve yaklaşma)         H1
  K02 ← K10 + K11 · 5+5 s      (gerçek kenetlenme)         H2
  K03 ← K20 + K36 + K46 · 3+4+3 s (kardeş · ekip · takip)  H3
  K04 ← K52 + K53 · 7+3 s      (kaçış ekseni · itki darbesi) H4
HOOK'UN SORUSU: "Bu küçük ekip bütün bu insanları kapanan geçitten nasıl çıkaracak?"
⛔ GÖSTERİLMEYEN: son araç çözümü · yerel bırakma kolu · güvenli taraftaki selam
⭐ Hook en SON monte edilir (kapsamlı plan §17) — kaynakları ana kurgudan gelir,
  böylece hook karakterleri ile film karakterleri ayrışamaz.
```

---

## 🗺️ SAHNE HARİTASI

```
SAHNE PLANI: 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3
             (25 sahne · toplam 96 klip · B1–B7 4+4+4 · B8 3+3+3+3 — kapsamlı plan §10)
             ⛔ hiçbir sahne bölüm dosyası sınırını aşmaz; QA part masterı sahne ortasından kesilmez

BÖLÜM       KLİP      SAHNE     SÜRE            PART
BOLUM_1     K01–K12   S01–S03   0:00–2:00       PART 1
BOLUM_2     K13–K24   S04–S06   2:00–4:00       PART 1  (sınır K24↔K25)
BOLUM_3     K25–K36   S07–S09   4:00–6:00       PART 2
BOLUM_4     K37–K48   S10–S12   6:00–8:00       PART 2  (sınır K48↔K49)
BOLUM_5     K49–K60   S13–S15   8:00–10:00      PART 3
BOLUM_6     K61–K72   S16–S18   10:00–12:00     PART 3  (sınır K72↔K73)
BOLUM_7     K73–K84   S19–S21   12:00–14:00     PART 4
BOLUM_8     K85–K96   S22–S25   14:00–16:00     PART 4
⛔ PART SINIRI KÖR NOKTASI: K24↔K25 · K48↔K49 · K72↔K73 — ② DEVAMLILIK hiçbir part
  masterda yan yana göremez → SPEC B'ye sınır satırı + ELLE KARE.
```

```
KURULUM İSKELETİ (film geneli · 92 harf · K01–K04 harf TAŞIMAZ):
B1  C A B C  ·  E H J E
B2  F M F B  ·  G D E D  ·  J D J F
B3  D C G E  ·  G J A B  ·  F G C I
B4  G E B N  ·  A C B A  ·  I A M J
B5  K I E A  ·  B I C A  ·  F G F G
B6  I J C K  ·  F G F E  ·  K C E C
B7  G J A C  ·  N E L N  ·  A C F K
B8  L J K  ·  L J N  ·  A K P  ·  A O L
16 kurulum (A–P) · 5 ölçek kademesi (EWS · WS · MS · CU · ECU) · 3 açı tipi
(eye-level · low-angle · high-angle) · ardışık aynı kurulum 0 ÇİFT (⑩① temiz)
```

### ⚠️ ⑩④ DÖNÜŞ VE KURULUM SAYISI — ölçülmüş, hedefin ALTINDA, gerekçesi yazılı [D74]

```
ölçülen DÖNÜŞ    B2 %33 · B3 %8 · B4 %25 · B5 %33 · B6 %25 · B7 %8 · B8 %25   (hedef ≥%40)
kurulum sayısı   B2 7 · B3 9 · B4 9 · B5 8 · B6 8 · B7 9 · B8 8               (üst bant 6)
```

İkisi de bilinçlidir ve kaynağı sahibin kendi kararıdır. Kapsamlı plan §13 birebir
şöyle diyor: **"Aynı çerçeveye dönüş, değişimi görünür kılmak için kullanılır. Sırf
oran hedefi tutturmak için rastgele kamera imzası aranmaz."** Ölçülmüş yapısal sebep:
bu film 16 dakikada **on bir ayrı mekân** geziyor (servis kokpiti · yuva dışı · yanaşma
tüneli · servis koridoru · hücre omurgası · modül omurgası · köprü · komuta gemisi ·
dış açık uzay · geçit ekseni · son araç içi) ve `ACI_YAYI` §4b'nin %40 hedefi 12-24
klipte **tek-iki mekânlı** filmlerden ölçülmüştür. On bir mekânı 12 kliplik bir bölüm
dosyasına sıkıştıran bir part, aynı kuruluma üç klip içinde dönemez — döndüğü yerde
mekân değiştirmiş olur.

⭐ Bunun yerine kullanılan araç, kapsamlı planın kendi endişesini karşılıyor: **eş
kadraj çiftleri**, ikisi de "değişimi görünür kılmak" için:
`K05 ↔ K08` (hiza bozuk → oturmuş · `YANASMA` §1.3 emsali) · `K14 ↔ K47` (komuta rayı) ·
`K49 ↔ K64 ↔ K69 ↔ K84 ↔ K87 ↔ K92` (aynı geçit ekseni, yalnız açıklık değişiyor) ·
`K41 ↔ K44` (liman → gezegen) · `K57 ↔ K59` (koridor) · `K65 ↔ K67` (bölme) ·
`K75 ↔ K81` (dış ölçek) · `K77 ↔ K80 ↔ K90` (ray) · `K85 ↔ K96` (son araç içi).
Dönen her klip metinde de işaretlidir: *"— the same position, height and lens as Clip N."*
⛔ ÖLÇÜM RANDEVUSU: bu sapma TAM-FİLM koşusunun ⑫ HOOK ve ④ HİKAYE merceğiyle sınanır.
Rapor "kesmeler kafa karıştırıyor" derse iskelet değişir, kart değişmez.

### 📐 ÖLÇEK ANLATIMININ BEŞ DURAĞI (kapsamlı plan §6 · `YANASMA` §1.2 vuruş seti)

```
K06  küçük servis gemisi ↔ dev gövde     V1/V3 · gövde kadrajı aşar, oran cümlesiyle
K17  insan ↔ koridor/hücre omurgası      G kurulumu · gövde boyu cetveli insan
K41 · K44  bütün gemi ↔ liman ↔ gezegen  A kurulumu · tek ana ölçek karesi
K62 · K69  gövde profili ↔ açıklık       J ve K · iki sade çember, aynı eksen
K94  küçük araçlar ↔ halkalı gezegen     A kurulumu · final
⛔ İKİ GÖVDELİ GENİŞ KARE (V3) film boyunca EN ÇOK İKİ KEZ: K06 ve K92.
⛔ Promptta METRİK ÖLÇÜ YOK [D138] — ölçek GEOMETRİK ilişkiyle yazılır
   ("the hull's ribs run past both edges of the frame"), sayıyla değil.
   Bütün sayılar (18 m · 480 m · 6 m · 30 km · 60 km) kapsamlı plan §6'da durur.
```

---

## 🎙️ REPLİK TABLOSU (`SES_VE_DIYALOG_URETIM` §1-§2a · kapı ㉓)

```
DİEGETİK REPLİK: 32 tırnaklı satır, 32 klipte (kapsamlı plan §11'in D01–D33'ü)
  ⛔ D03 (K18) İSTİSNA: sahibin metni tek bir ÖZEL AD ("Lina."). Özel ad prompta
     giremez [D34] → promptta cümle olarak yazıldı ("the pilot names her sister and
     nothing more is said"), tırnaklı satır olarak YAZILMADI. Post-dub'da söylenir.
     → SPEC A: DIALOGUE LINES: 32 (+1 post-dub ad satırı)
DIŞ SES (VO): H1–H4 · 44 İngilizce kelime · YALNIZ K01–K04 kurgu bloklarında.
  Kurgu blokları prompt taşımadığı için VO promptlarda 0 kez geçer; metni §HOOK'ta.
```

| klip | konuşan | REGISTER | kanal | yerleşim | İŞLEV (B5) |
|---|---|---|---|:--:|---|
| K05 | Lina (kayıt) | HUMAN | telsiz · kadrajda yok | ① | İSTEK — girişin nasıl açılacağı |
| K14 · K47 · K48 | komutan | HUMAN | gemi kanalı · ağız kadrajda | ③ | MUHATAP — karşı hamle |
| K18 | Mara | HUMAN | kask içi · yüz kadrajda | ③ | İSTEK (ad — post-dub) |
| K19 · K22 · K45 · K71 · K82 | Lina | HUMAN | telsiz | ②/③ | istek çaprazı · çözüm |
| K21 · K23 · K30 · K67 · K69 · K76 | Mara | HUMAN | telsiz | ②/③ | AYRILIK · BEDEL · KARAR |
| K25 · K51 · K55 · K68 · K72 · K78 · K88 | Veyr | HUMAN (çevirici) | giysi ünitesi | ② | ENGEL sınırı · çözüm |
| K27 · K58 · K73 · K79 · K83 | Edda | HUMAN | ekip kanalı | ①/② | toplu iş — tema |
| K36 · K50 · K61 · K62 | sistem / Mara / Lina | MACHINE + HUMAN | konsol · telsiz | ① | ENGEL — sayı 2. kanalda |
| K49 | gemi sistemi | MACHINE | gemi kanalı · kadrajda insan yok | ① | novum kuralının ilanı |

```
⭐ SAYI KURALI [D82]: açıklık/mesafe söyleyen her replik GÖVDESİZ makinededir
  (K49 "Gate closure confirmed." · K61 "Clearance decreasing.") — insana devredilmedi.
⚠️ SENKRON RİSKİ AÇIK VE SAHİBİN KARARI (kapsamlı plan §2 md.3 · §5): vizör berrak,
  yüz okunur, telsiz olmak senkron riskini SIFIRLAMAZ. 32 repliğin 11'i ③ yerleşimde
  (ekranda ağız). Ölçüm randevusu: TAM-FİLM ③ SES merceği + POST-DUB tablosu.
  Sorun çıkarsa replik reaksiyon planına ya da mekanik inserte taşınır (plan §14).
```

---

## 📖 BIBLE'LAR

### 👤 Character Bible — özel ad promptta 0 kez [D34] · ≤3 kişi özniteliği [D167 · ⑲]

| kod | prompt kimliği (İngilizce · birebir) | promptta |
|---|---|---|
| C01 Mara 34 · pilot | *The pilot wears a satin off-white ceramic chest shell with champagne-gold frame lines at the joints, three raised blank ribs across the right chest, a single neck ring and heavy white gloves.* | 46 klip |
| C02 Lina 28 · mühendis | *The engineer wears a white technical suit with cobalt shoulder and forearm panels and two fixed tool sockets on the belt.* | 24 klip |
| C03 Veyr · sistem mühendisi | *The tall systems engineer stands a head and a half above the humans in white elongated armour with copper joints and two neck rings, four fingers on each hand, and two symmetrical bony plates on the face behind a clear helmet.* | 18 klip |
| C04 komutan 45–55 | *The commanding officer wears sharp-edged white military pressure armour with one dark red band running the full length of the left arm and a narrow visor.* | 4 klip |
| C05 Edda 42 · ekip sorumlusu | *The crew lead wears a white pressure suit with a grey shoulder stripe and a short visor frame.* | 6 klip |
| G1/G2 muhafız | *The guard wears white protective pressure gear with a single red mark on one upper arm.* | 5 klip |
| diğer tutsaklar | *The other adults wear the same white main suit with measured blue and grey duty panels and closed helmets.* | 9 klip |

```
⛔ BOY · TEN RENGİ · SAÇ · YAŞ promptta 0 KEZ [D167 · red defteri #15 — yedi öznitelik
  üst üste "public figure" sınıflandırıcısını tetikledi]. Hepsi bu tabloda ve referans
  paketinde durur. Veyr'in boyu GÖRELİ yazılır ("a head and a half above the humans").
⛔ ÇOCUK YOK: child · kid · boy · girl · young → 0/184 prompt (sahibin md.1 kuralı).
⭐ AYIRT ETME GEOMETRİDE: omuz kaburgası sayısı (3) · boyun halkası sayısı (1 ↔ 2) ·
  parmak sayısı (5 ↔ 4) · vizör genişliği (geniş ↔ dar) · kol bandı (tek koyu kırmızı).
  Renk ikinci taşıyıcıdır, ilk değil.
```

### 🎖️ Rozet Bible — SAPMA 1'in uygulanmış hâli · **METİNSİZ AMBLEM DİLİ**

⭐ `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU` §3 deponun kendi **metinsiz amblem dilini**
tanımlıyor ve riskini "çok düşük" ölçüyor: `textless` + TEK geometrik motif + sayılabilir
öğe + doku kelimesi (`embossed embroidery`). Sahibin "özgün rozetler korunur" isteği bu
dille **tam olarak** karşılanıyor — rozetin görünür bir tasarımı var, yalnız HARF yok.

```
PROMPTA GİREN ROZET CÜMLESİ (klibin ÖNDEKİ kimliğine göre, yakın/orta planda):
  pilot    On the right chest is a textless three-winged pilot badge in embossed embroidery,
           and on the left upper arm a textless circular survey patch.
  mühendis On the left chest is a textless compass-form survey badge, and on the right upper
           arm a textless patch with two parallel bars.
  Veyr     On the chest is a textless three-part technical badge in embossed embroidery.
  komutan  On the chest is a textless angular rank patch in embossed embroidery.
  ekip     On the chest is a textless rectangular duty badge in embossed embroidery.
GENEL CÜMLE (geniş planda · rozet okunmuyorsa):
  Every badge and patch is textless, a single geometric motif in embossed embroidery, with
  nothing written on any of them.
NEGATİF ÇEKİRDEĞİN 4. CÜMLESİ (artık çelişmiyor — ikisi aynı yöne bakıyor):
  No readable text, letters, digits or numerals on any surface in frame — every badge and
  patch is textless — no subtitles, no captions, no watermark.

⭐ SAYILABİLİR ÖĞE = ANLATI VERİSİ (§3 kuralı): üç kanat · iki çubuk · üç parça — sayılar
  kilit olarak yazıldı; model sayıyı şaşırırsa ① mercek yakalar.
⛔ Yama başına en fazla 2-3 renk, TEK motif. Karakter başına amblem yükü: yakın planda
  2 öğe, geniş planda yalnız genel cümle.
POST KATMANI: renk, ince çizgi ve nihai amblem ayrıntısı üretimden SONRA bindirilir
  (kapsamlı plan §5: "Özgün amblemler ayrı tasarım katmanları olarak saklanır").
⛔ İnsanlara ait GERÇEK kurum amblemi 0 kez (NASA · ESA · ordu · bayrak — ⑯ sözlüğü).
```

### 🌍 World Bible — üç çapa, film boyunca değişmez [D209]

```
① EKSEN:   the escape axis runs screen-left to screen-right and the ship's nose points
           to screen right for the whole film
           → 76 promptta: her bölümün ilk klibi + araç yöneliminin kayabildiği 31 insansız
             dış klibin hepsi (image + video). Kapı dosyada BİR tane arıyor; sayı bir
             taneyle bırakılmadı çünkü model her karede yeniden karar veriyor [D174].
② GEZEGEN: Aster — banded copper cloud belts with one large pale storm, filling the
           background and never fitting the frame   (S02–S24)
③ GEÇİT:   a fixed outer ring that never changes size, with an active opening inside it
           that only ever draws inward   (S13–S24)
FİNAL DEĞİŞİMİ: Neris — a pale blue ringed planet with the rings tilted open (S25 · K94–K96)
⛔ Aster bir anda renk değiştirmiş gibi sunulmaz; iki sistem GEÇİTLE bağlıdır.
```

### ⚙️ Physics Bible — 92 klibin 92'sinde AYNI SATIR

```
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised
hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is
pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting
straight while turning slowly on its own axis.
```

```
⛔ GEMİ DÖNMEZ (kapsamlı plan §7.3). Eski sürümün 0,6 RPM · 0,40 g · 0,62 m düşüş
   sayıları bu filmin parçası DEĞİLDİR. Manyetik taban eşyaya/gövdeye yerçekimi vermez.
⭐ 2b REJİM AYRIMI uygulandı: fiil MEKANİK SEBEBE bağlı ("locks each boot before the next
   step", "pulled forward by a rail") — model "yürümek"i 1 g verisinden çekmesin.
⭐ AÇISAL MOMENTUM ayrı yazılı: "drifting straight while turning slowly on its own axis".
⛔ İTKİ/DARBE ANLARI ayrıca yazılır (K54 · K66): göreli hareket ARACIN ivmesinden gelir,
   yerçekimi değişiminden değil. "no change of gravity occurs in this shot" o kliplerde negatifte.
```

### 🔊 Audio Bible — 92 klibin 92'sinde AYNI İLK CÜMLE

```
AUDIO: Nothing at all is heard through the vacuum, so every sound is carried by a hull or a
suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet.
```

```
2. cümle klibe özel (temas · valf · kenet · alarm · telsiz) · 3. cümle replik ya da
"No dialogue in this shot."
⛔ DIŞ VAKUMDA hava yoluyla gelen patlama/motor sesi 0 klip. Köprü: telsiz, müzik ya da
  içeriden başlatılmış titreşim.
MÜZİK (kapsamlı plan §14): 0–4 dk merak/baskı · 4–8 dk hazırlık/kaçış · 8–12 dk daralma ·
  12–15:30 kontrollü yükseliş · son 30 s çözülme. SESSİZLİK: kenetlenme öncesi (K09) ·
  K64 başarısız hızlanma sonrası · K93 kapanış sonrası.
⛔ Zafer müziği SON ARAÇ GEÇMEDEN tamamlanmaz (K92'den önce yok).
```

### 📷 Camera Bible — 16 kurulum · aynı harf = BİREBİR aynı satır

| harf | CAMERA satırı (promptta birebir) | ölçek · açı |
|---|---|---|
| A | 24mm · 40 m from the hull · on the approach axis | EWS eye-level |
| B | 35mm · 8.0 m from the subject · 0.9 m | WS low-angle |
| C | 35mm · 1.5 m behind the seat · 1.45 m | MS eye-level |
| D | 85mm · 1.2 m from the helmet · 1.55 m | CU eye-level |
| E | 85mm · 3.0 m from the mechanism · 1.30 m | CU eye-level |
| F | 50mm · 2.4 m along the corridor axis · 1.50 m | MS eye-level |
| G | 24mm · 9.0 m from the spine · 2.60 m | WS high-angle |
| H | 32mm · 12 m out from the berth mouth · on the berth axis | WS eye-level |
| I | 50mm · 3.0 m from the consoles · 2.20 m | MS high-angle |
| J | 100mm · 0.55 m from the glove · 1.20 m | ECU high-angle |
| K | 24mm · 60 m back on the gate axis | EWS eye-level |
| L | 35mm · 2.0 m from the seat row · 1.40 m | MS eye-level |
| M | 50mm · 1.4 m from the console rail · 1.15 m | MS low-angle |
| N | 32mm · 20 m out along the rail · 0.8 m above the rail line | WS low-angle |
| O | 85mm · 1.0 m from the window · 1.35 m | CU eye-level |
| P | 50mm · 120 m back on the gate axis | WS eye-level |

### 🚫 Negative Bible — §5.1 çekirdeği · ④ bu filmde uyarlanmış (SAPMA 1)

```
① Single unbroken take, no cuts, no dissolves, no camera resets, no angle change.   (yalnız VIDEO)
② Exactly <N> human character(s) in a suit / in suits[, and exactly <M> tall figure(s) with two
   arms, two legs and one head], no duplicates, no extra person.        ⛔ RAKAMLA [KRONOS]
③ 0% bloom, no glow, no soft focus, every surface keeps visible texture.
④ No readable text, letters, digits or numerals on any surface in frame — the raised badge shapes
   stay blank relief with nothing written on them — no subtitles, no captions, no watermark.
⑤ Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat,
   no airbrushing, no waxy texture, no face morphing.
⑥ Equipment and clothing identical throughout, no drift, no gear appearing or disappearing.
⑦ Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.
⑧ Particles obey the stated microgravity with continuous one-way momentum, never stopping in
   mid-air, never swirling like liquid, structures static, no melting or warping.
+ en çok 3 sahneye özel cümle (㉗ tavan 11)

⭐ İNSANSIZ KLİP (26 klip) KISA NEGATİF TAŞIR — 4-5 cümle, blok < 900 karakter
  [⑯b · red defteri #2 Cold Burn S8: insansız sahne + uzun yokluk listesi = yapısal red].
  ② o kliplerde: "Exactly 0 human characters in frame, no people, no figures, no silhouettes
  of people." ⑤ kısalır, ⑥⑦⑧ düşer.
```

---

## 🔢 SAYISAL KİLİT LİSTESİ (promptta SAYILABİLİR, ölçü birimi YOK)

```
kenet         4 sert kenet (K11 · ters sırada K30) — "exactly four clamps, no more and no fewer"
liman kenedi  6 taşıyıcı kilit (K40) — altıncı açılmadan gövde hareket etmez
gövde kaburga 6 uzun dış kaburga (K41 · K43)
takip kuvveti 3 araç: 1 uzun + 2 kısa (K46 · K56 · K87) — "no fleet"
göbek bağı    2 grup: güç + akışkan (K39)
modül kenedi  4 kenet (K80 · K89)
transfer aracı 24 araç · rayda iki banka 12 (K73 · K94)
hücre bayı    K17'de 6 ayrı bayda 6 ayrı yetişkin · K27'de 6 mandalda 6 kişi
yolcu         K73'te 4 + 1 · K37'de 7 + 1 · K79'da 4 + 1 (kalabalık 0 klip)
üç koltuk     M24: önden sol Mara · orta Lina · sağ Veyr (K85 → K96 değişmez)
parmak        insan 5 · Veyr 4 (her Veyr klibinde)
boyun halkası insan 1 · Veyr 2
ön kol çiziği 1 tek eğik iz — K16'da doğar, K17–K96 kadrajda
```

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır · ㉕)

| ders | bu filmde ne yapılacak | kapsama (ölçülmüş) |
|---|---|---|
| D34 | özel ad promptta 0 kez; kimlik referans sayfası + giysi geometrisiyle taşınır | 184/184 |
| D138 | metrik ölçü promptta 0 kez; ölçek geometrik ilişkiyle yazılır | 184/184 |
| D167 | boy/ten/saç/yaş promptta 0 kez — yedi öznitelik yığını sökülü | 184/184 |
| D79 | vizör "optically clear glass with zero tint" — yüz kadrajdaki her klipte | 44 klip |
| D139 | düz sırt cümlesi — sırt kadrajdaki her klipte, yokluk listesi değil pozitif yüzey | 14 klip |
| D124 | klip süresi ARAÇTAN ölçülür; 10 s kurgu birimidir, ham süre değil | ⬜ ölçüm |
| D169 | efor fiili varsa gövde kanalı aynı TIMELINE satırında (mikrogravite kütleyi azaltmaz) | 11 klip |
| D175 | "through the glove/suit" 0 kez — saydamlık tarifi deriyi çizdirir | 184/184 |
| D123 | yasak SİLİNDİ, malzeme TARİF edildi: gore/blood/corpse/weapon/victim 0 kez | 184/184 |
| D127 | ivme yazılmaz, süre ve mesafe yazılır — TIMELINE üç satır | 92/92 |
| D200 | tek kadrajda iki yerçekimi yok: TEK rejim + itki/darbe klibinde açık cümle (K54 · K66) | 92/92 + 4 |
| D154 | yerçekimi cümlesi klibin içini kilitler, arasını kilitlemez → 92 promptta BİREBİR | 92/92 |
| D209 | dünya çapası üç satır: eksen · gezegen · geçit — eksen 76 promptta, gezegen/geçit ışık yatağında | 76 prompt |
| D214 | kadrajda olmayan beden tarif edilmez; IN FRAME satırı belirleyici | 184/184 |
| D217 | görüneni söyleyen replik silindi; 32 repliğin her biri İŞLEV taşır | 32/32 |
| D59 | yasak yerine pozitif hâl: kapanan kapak, ayrılan kenet, kopan yapı POZİTİF yazılı | 26 klip |
| D207 | ön kol çiziği kesmede sıfırlanmaz — K16'dan K96'ya kadar kimlik cümlesinde | 80 klip |
| D157 | novum taşıyıcısının adı TEK KARE cümlesinde: "the bright edge of the opening" | K69 |
| D104 | yanaşmada kamera HEDEFTE durur, araç kameraya gelir (H kurulumu · K10) | 4 klip |
| D38 | patlama sayılı ve yerel; ateş topu/şok dalgası/mantar bulutu 0 klip | 5 klip |

### ⛔ UYGULANMAYAN KİLİTLER

| ders/kart | neden uygulanmadı |
|---|---|
| D146 vizör biçimi sayıyla | referans paketi yazıldı ve KAPI 0 oldu; biçim kilidi metinle değil SAYFA ile tutuluyor |
| D175 çıplak deri üç bölge negatifi | iç hacim basınçlı ve ~1 atm; çıplak deri bu filmde fizik hatası değil — üç bölgeli negatif yazılmadı |
| §3.7 dönme yerçekimi kartı | gemi dönmüyor (kapsamlı plan §7.3) — kart açılmadı |
| KÜME ≥2 | çok klipli sahne rejiminde küme yoktur (zincir kaldırıldı 22.09.2026) |
| ⭐VİRAL ara sahne 16 hedefi | ölçülmemiş hedef yazılmaz; §2.3 bandı bu estetikte 0-3 ölçüldü → aday klipler SPEC'te tek tek ÖLÇÜLECEK |
| D180 planlı mutlak sessizlik | sessizlik KURGUDA kurulur, modelden istenmez — üç sessizlik penceresi §Audio Bible'da |
| dikey kırpma | ana film 16:9; sosyal kesit ayrı kadrajlanır (kapsamlı plan §19) |

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
① ŞİDDET SÖZLÜĞÜ 0 KEZ (negatif blok DÂHİL — ⑯ kapısı): gore · blood · corpse · wound ·
   injury · kill · dead · victim · weapon · gun · rifle · explosion · flames · smoke · panic.
   Silah ADLANDIRILMAZ: "a short dark handheld unit". Atış PANELE/SİPERE gider, gövdeye asla.
② KAYIP ÜÇ İŞARETLE: yoktur — bu filmde destek karakter ölümü YOK (sahibin kararı).
   Muhafızlar K34 ve K60'ta KAPAKLA ayrılır, ikisi de AYAKTA ve basınçlı bölmede.
③ KALABALIK 0 KLİP [red defteri #8: "crowd of figures" + kaçan insan = doğrulanmış red].
   İnsan kütlesi her klipte SAYILI ve AYRI: "six adult astronauts at six separate bays,
   one to a bay". Panik/koşma 0 klip; hareket GÖREVLİ ve sıralı.
④ MİLLİYET · GERÇEK KURUM · BAYRAK · RÜTBE HARFİ 0 kez.
⑤ İNSANSIZ KLİPTE KISA NEGATİF (26 klip · <900 karakter) — yapısal red profili kapatıldı.
⑥ VİZÖR BERRAK: yüzü kapatan ekipman anonimlik/deepfake imzasına yakın okunuyor
   (POLİTİKA §3 imza ⑥); berrak vizör red riskini DÜŞÜRÜR ve sahibin kararıyla uyumlu.
```

---

## ⚠️ SAPMA — sahibin planı ile üretim kapıları arasındaki dört kayıt [D74]

| # | kapsamlı planın satırı | çarpıştığı kapı | uygulanan |
|:--:|---|---|---|
| 1 | §5 "Özgün rozetler korunur… Uzun yazılar görüntü modeline yazdırılmaz" | negatif çekirdek ④ metin/simge yasağı [D138] | ⭐ **ÇÖZÜLDÜ, SAPMA KÜÇÜLDÜ:** `ASTRONOT_DONANIM` §3'ün **metinsiz amblem dili** kullanıldı — rozetin görünür TASARIMI var (üç kanat · pusula · iki çubuk · üç parça · köşeli), yalnız HARF yok. `textless` + tek motif + `embossed embroidery`; kılavuzun ölçtüğü risk "çok düşük". Rozet SİLİNMEDİ, KÜÇÜLTÜLMEDİ. |
| 2 | §9 · §16 "K01–K04 kaynak kliplerden monte edilir… temel yük 184 prompt" | format kartı 96 klip × 2 prompt | K01–K04 **kurgu bloğu**: prompt 0, üretilen yeni kare 0. Zaman çizgisi 96 blok, üretilen klip 92, prompt 184. Kapı ㉜ prompt taşımayan klibi atlar — ölçüldü. |
| 3 | §2 md.9 "İsimler karakter kayıtlarında açıkça bulunur" | D34 özel ad promptta | adlar bu dosyada, hikâye onayında, sahne tablosunda ve referans paketinde AÇIK; promptta 0 kez. K18'in tek adlık repliği promptta cümleye çevrildi, post-dub'da söylenir. |
| 4 | §11 koridor çatışması ve güvenlik birliği | §4.3 SAVAŞ kartı ⏸️ RAFTA | tür bilimkurgu kaldı, savaş kartının KİLİTLERİ ödünç alındı (isabet panele · kan/ceset/yara 0 kare · silah adlandırılmaz · patlama sayılı ve yerel). Emsal: THE_STOLEN_SKY SAPMA 2. |

⛔ Bu dört satır dışında olay, sıra, zaman kodu, açıklık çizelgesi, yolcu sayısı ve
replik yerleşimi **kapsamlı planın kendisidir**; bu dosya onları yeniden yazmaz.

---

## 🏭 ÜRETİM SIRASI (kapsamlı plan §17 · [D168] — dramatik sıra DEĞİLDİR)

```
0  REFERANS PAKETİ · 21 sayfa  [KAPI 0] — sayfası onaylı olmayan varlığın klibi üretilmez
1  MEKÂN/ÖLÇEK ANİMATİĞİ (96 blok · süre ve ölçek sözleşmesi)
2  ODAKLI TESTLER  T01 K05/K20 · T02 K09–K11 · T03 K17/K27 · T04 K25 · T05 K41/K44 ·
                   T06 K65–K67 · T07 K64/K69 · T08 K90/K92/K93
3  MEKÂN SIRASI    yuva/servis → hücre/koridor → köprü → araç içleri → dış liman/takip → geçit/final
4  SINIR ÇİFTLERİ  K24↔K25 · K48↔K49 · K72↔K73 (elle kare)
5  HOOK EN SON     K01–K04 ana kurgudan monte edilir
İPTAL KAPILARI: T02 (hiza→temas→sert kenet sırası okunmuyorsa yanaşma yeniden kurulur) ·
  T07 (900'de sığan gövde 420'de sığmıyor okunmuyorsa novum çöker → film ÜRETİLMEZ) ·
  T03 (figürler yetişkin okunmuyorsa ya da kalabalık hissi doğuyorsa sahne sadeleşir) ·
  T08 (araç tam geçmeden alan kapanıyorsa doruk çöker → film ÜRETİLMEZ)
⛔ Başarısız test yaratıcı isteği SİLMEZ: ışık, kamera, hareket bölme ya da kompozit değişir.
```
