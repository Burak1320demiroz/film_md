# 🎬 THE_DRY_ANCHOR — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.

```
FORMAT:        yatay 2-4 dk (uzay) · 16:9 · §2.2 kartı · 2 bölüm · im-to-video
ORTAM:         §3.2 İNCE ATMOSFER (Mars sınıfı)
TÜR:           bilimkurgu · SERT (hard) dal — §4.1
KLİP SÜRESİ:   10,0 s  ⛔ D124 KAPISI AÇIK — bu sayı hattın ölçülmüş standardıdır
               (emsal: THE BENT GRASS 14 × 10 s) ama BU ARAÇTA ölçülmedi.
               ÜRETİMDEN ÖNCE DOLDURULACAK:
                 KLİP SÜRESİ = ______ s
                 ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk klip>
               ⛔ Bu satır boşken hiçbir sahne üretilmez; ızgara plandan değil
                 ARAÇTAN gelir ve depoda üç film bu yüzden bandın dışına düştü.
SAHNE SAYISI:  14        RUNTIME: 140,0 s = 2:20  (14 × 10,0 · ayrı hook klibi YOK)
               ⛔ Format tabanı 120 s — 140 s bandın İÇİNDE. Bant 12-18 sahne;
                 14 bandın içinde, sahip izni ve D74 satırı GEREKMEZ.
LOGLINE:       Yağmur görmemiş bir ovaya inen dev bir geminin ayağı batmaya
               başlar; sahadaki tek mühendis, gemiyi tutacak tek sert zemine
               ulaşmak için oraya toplamaya geldiği kasayı bırakır.
```

## 📦 REFERANS PAKETİ — YAZILMADI (sahip kararı · D74 satırı)

```
REFERANS PAKETİ YAZILMADI — sahip kararı, 10.09.2026. `REFERANS_PAKETI_KILAVUZU`
§1'in T1 (kask/vizör) · T2 (biçim kilidi metinle tutulmayan varlık) · T3 (oranı
sözle yazılamayan nesne) · T5 (tekrar eden insan dışı olay) tetikleyicileri
DOĞRUYKEN atlandı; biçim kilidi tamamen METİNLE taşınıyor ve D146'nın üç
ölçülmüş vakasının (SKYLIGHT · YERÇEKİMİ F2 · STANDING WIRE) riski bu satırla
açıkça KABUL EDİLMİŞTİR.
⛔ Dosya SİLİNMEZ: `THE_DRY_ANCHOR_REFERANS_PAKETI.md` ⬜ BEKLİYOR durumunda kalır.
⛔ İKİNCİ SONUÇ — paket olmadığı için ÜRETİM SIRASININ ilk halkası KAPI 0 değil
  DORUKTUR (aşağıda).
⭐ ÖLÇEN MERCEK: ② DEVAMLILIK cat.4 (ekipman) — biçim kilidi orada ölçülür.
```

---

## 🎭 TEMA

```
TEMA: İNSAN-MAKİNE SINIRI
      Uzayı geçen makine kendi başına yerinde duramaz; onu tutan tek şey,
      bir insanın eliyle sürdüğü tek bir çelik çubuktur.
      ⛔ TAKAS DEĞİL TANIM cümlesi [§3c moratoryumu]: "X olabilmesi için Y
        feda edilir" kalıbı kullanılmadı; bedel filmde VAR ama tema cümlesi
        bedelin üstüne kurulmadı.
      ⭐ Yatay/süreç temalarının depoda EN AZ kullanılanı (sayac.sh 🎭
        TEMA DAĞILIMI, 10.09.2026: Zaman 5 · Fedakârlık 4 · Kimlik 3 ·
        İnsan-Makine 2). §4 süre-tatmin kuralı: SÜREÇ teması → yatay ✅

MOTİF SAHNELERİ: S3 · S4 · S9 · S11 · S13
      S3  — insanın katkısı bir çubuktur ve zemin onu yutar
      S4  — makinenin ölçeği; insan kadrajın yirmide biri
      S9  — makineyi tutmak için insanın getirdiği şey bırakılır
            (⭐ `03_PLAN_ONCESI` B3 çapraz kapısı: BEDEL sahnesi motif
             listesinde OLMAK ZORUNDA; 10.09.2026'da eklendi — bedelin
             temayı taşımadığı film, temayı dekor yapar [KALEIDA vakası])
      S11 — çubuk durur; makineyi tutan şey o tek temastır
      S13 — gövde durur, hat gerilidir, eller boştur
MOTİF KANALLARI: nesne (kazık ↔ gövde, aynı karede) · kinesik (iki elle sürme) ·
      kamera (A'da insan %5 / D'de gemi kadraj dışı) · ışık (eldiven sıcak
      alır, gövde soğuk yansıtır)
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:  Bu ovadaki tozu hiç yağmur sıkıştırmadı: taban basıncı yüksek olan
        her şey iner ve DURMAZ.
        ⭐ Bir DURUM değil bir KURAL ve olay örgüsünü ZORUNLU kılıyor —
          çapa tutmazsa gemi eğilmeye devam eder. Ölçülmüş ölçüt:
          novumun VAR OLMASI yetmiyor, karakteri bir şey yapmaya MECBUR
          etmesi gerekiyor (INVERSION 6/10 ↔ RING WALKER 4/10).
        ⭐ DOĞRULANMIŞ BİLİM: yağmur görmemiş ince regolit sıkışmaz,
          taşıma kapasitesi düşüktür — serinin gerçek kancası budur.

NOVUM TAŞIYICISI:  <ÇELİK KAZIK — geniş bilezikli, kısa saplı>
                 × <iki elle sürme ve DURMA anı>
                 → <ihlal: kazık durmaz, bilezik toza gömülür, vurulacak
                    baş kalmaz>
        ⛔ Taşıyıcı SOMUT ve ADI OLAN bir nesnedir, türetilmiş bir optik
          ya da atmosferik fenomen DEĞİL [D73 · THE WRONG SHADOW 3,0/10].

TEK KARE (§4①):  ✅ "Kum, sürülen ÇELİK KAZIĞIN başını yutmuştur; sürücü
        hâlâ iki elde, ama vurulacak bir baş kalmamıştır."   (kare: S3)
        ⛔ Cümle TAŞIYICI NESNENİN ADINI içeriyor [D157].

KİNETİK BAĞIMSIZLIK: ✅ Kural iki jestle kanıtlanır — S3 kazık durmaz,
        S11 kazık durur ve sürücü geri seker. Replik 0 · ekran metni 0 ·
        dış ses 0 · gösterge 0.

BAŞLIK ŞEMASI:  ✅ "This Dust Has No Bottom" (5 kelime · DÜZ GERÇEK kalıbı)
```

## 🧭 B5 — HİKÂYE OMURGASI (her formatta · `03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 İSTEK:  ☑ Gemiyi kalkışa hazır bırakmak — dört ayağı hizada ve kilitli.
              ⭐ Film başlamasa da var olan bir İŞ: sahadaki mühendisin
                görev listesinin son maddesi. Ölçülebilir, biten, devredilen.
   ENGEL:   ☑ Zemin. Yağmur görmemiş toz sıkışmamıştır; taban basıncı yüksek
              olan her şey iner ve durmaz. İlk kazık yutulur; tutan tek yer,
              hattın yetişmediği kadar uzaktaki süpürülmüş taştır.
   BEDEL:   ☑ ÖRNEK KASASI · **S9** — hattı uzatmanın tek yolu kasa rafının
              kayışını hatta eklemektir; kasa toza iner ve orada kalır.
              ⭐ Filmin geliş sebebi, dönüşün bedeli olur. Bedel AYNI karede
                görünür (kasa yerde + kalçadaki yuva).
   MUHATAP: ☑ ORTAMIN KALICI DEĞİŞEN PARÇASI — ayaktaki toz halkasının
              DURDUĞU çizgi ve gergin hat. ⛔ FINAL §4.1 kapısı: üçü de
              SON KAREDE (S13) kadrajda.
B5b □ AYRILIK: — (tek insanlı film; koşmaz)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  DORUK S11 → merkezî seçim S9 → kapanış imajı S13 → S0 →
  sonra S3 · S1 · S4 · S12 → kalanı (S2 · S5 · S6 · S7 · S8 · S10)
  ⛔ Referans paketi YAZILMADIĞI için KAPI 0 YOKTUR; zincirin ilk halkası
    DORUKTUR.
  ⭐ BU SIRA TESLİM LİSTESİNE AYRI SATIR OLARAK DA GEÇER: THE UPWARD FALL'ın
    planında sıra YAZILIYDI ve doruk yine teslim edilmedi — liste PLANI
    bağlar, TESLİMİ bağlamaz [D168 · 2. vaka].
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR (KILAVUZ_REHBERI §2.1)

```
⛔ BU FİLM YATAYDIR — dikey blok KOŞMAZ. Yine de ikisi yataya da taşındı
  ve burada beyan edilir:

① BİLGİ ASİMETRİSİ: VAR · S1 · 14,0 s — izleyici gömülmüş pabucu görür,
   astronot hâlâ gövdeye bakmaktadır ve ayağa S2'de döner. Pencere S2'de
   kapanır. ⛔ Pencere açıkken hiçbir sahne gizli gerçeği ADLANDIRMAZ.
② EL YUVASI: S3 · S7 · S9 · S11 — dördünde de el çevreyle FİZİKSEL TEMAS
   kuruyor ve C/E kurulumlarında elin kadraj payı ≥%25.
   ⭐ Gerekçe yataya da geçer: kask altında izleyicinin empati kurduğu
     organ eldir ve ölçülmüş birincil vekil nesnedir.
③ VİZÖR BEKLENTİSİ: DIKEY_MIKRO_DRAMA §4.1 ① — S11'de kendi lambası yüzü
   yakınlaştırdıkça yüz DAHA OKUNUR olur; ⛔ vizör durumu 14/14 sahnede
   BİREBİR aynıdır, değişen 0 kare [D37 · D57].
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | sahne | boşsa gerekçe |
|---|---|---|---|---|
| 1 | KATALİZÖR | %10 · ≤0:15 | **S1** (10-20 s) | — |
| 2 | İLK ÇATLAK / kural kanıtı | %21 | **S3** (30-40 s) | — |
| 3 | ⭐ PAYLAŞIM SAHNESİ (HUŞU) | %30 | **S4** (40-50 s) | ⛔ ⭐VİRAL DEĞİL: kapı YÜZ+HAREKET ister, S4 bilinçli HAREKETSİZDİR ve 110 m'de yüz okunmaz |
| 4 | ORTA NOKTA / kural direnir | %50 | **S7** (70-80 s) | bölüm sınırının hemen sonrası |
| 5 | ⭐ MERKEZÎ SEÇİM + BEDEL | %64 | **S9** (90-100 s) | B5 BEDEL satırı buraya çapalı |
| 6 | HER ŞEYİN KAYBI | %75 | **S10** (100-110 s) | — |
| 7 | ⭐ DORUK · ⭐VİRAL | %79 | **S11** (110-120 s) | YÜZ + HAREKET satırları S11 çalışmasında ölçütlü |
| 8 | BEDELİN GÖRÜNÜR KARŞILIĞI | %86 | **S12** (120-130 s) | — |
| 9 | FİNAL / held frame | %93-100 | **S13** (130-140 s) | kapanış bütçesi %14 → koda YOK, 2 sahne |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       IN MEDIAS RES (§4 tipolojisi · band 2-4 dk ⭐)
                 Film gövdenin SON İNİŞİNDE açılır; kurulum yok, kimse
                 tanıtılmaz. ⛔ Tek tip — ölçek şokuyla bindirilmez.
                 Tipin bilinen riski BAĞLAM BORCUDUR; taksidi S1'dir.
S0 SORUSU:       "O gövde neyin üstüne iniyor?"   (TEK soru, iki değil)
S1 İKİNCİ BİLGİ: "Ayaklardan biri artık zeminin ÜSTÜNDE değil İÇİNDE."
İLK 2 SN SESİ:   TEK DİEGETİK SES — inişin zeminden iletilen boğuk alçak
                 basıncı. ⛔ Müzik 0:00'da GİRMEZ (en erken 2-5 s).
                 ⛔ Taşıyıcı 90 Hz ÜSTÜNDE + missing fundamental yığını
                   (100 · 150 · 200 Hz) — 150 Hz altı telefonda YOKTUR.

FİNAL TİPİ:      MUĞLAK (2-4 dk bandı: TWIST veya MUĞLAK)
                 AÇIK KALAN SORU SAYISI: 1 — "kasayı bırakıp gidecek mi?"
                 ⛔ 0 = kapalı final bedeli · 2+ = aldatılma hissi
SON PLAN TİPİ:   İLK KADRAJA DÖNÜŞ + NESNE EKİ
                 Figür ön planda kalır, eller boş; anlam geride kalan
                 KASAYA biner. ⛔ Kasa novum taşıyıcısıyla ÇAKIŞMIYOR
                 (taşıyıcı kazıktır) — kural sağlandı.
TOHUM BİLGİ:     S2 · ≤2 s · ÇEVREDE (derin iz ↔ sığ iz aynı karede)
                 ⛔ Bakışla VURGULANMAZ; final tohumun yerine döner (S10-S11).
AÇILIŞ↔KAPANIŞ:  KAFİYE (LOOP DEĞİL) · TEK DEĞİŞKEN: kadrajı çaprazlayan
                 GERGİN HAT (S0'da yok, S13'te var)
                 İLAN EDİLEN İKİNCİ DEĞİŞİM: kasanın yeri (kızak → toz) =
                 B5 BEDEL'i; sessizce bırakılmıyor.
PAYLAŞIM DUYGUSU: HUŞU (paylaşım) — ⛔ KAYGI DEĞİL; ikisi aynı filmde
                 imza olamaz [FINAL §5]. Yuva: S4.
KAPAK ANI:       S0 · 0:04 · gövde son yüksekliğinde, ön planda figür ve
                 kızak; ışık tek alçak kaynak soldan; odak: gövdenin alt
                 kenarı ile ufuk çizgisinin AYNI karede olması.
                 ⛔ 0:00-0:10 bandından [PAKETLEME §1] · kadraj ortası DEĞİL
                 ⛔ KURGU KAPISININ KESİLEMEZ LİSTESİNDE
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` (göz · tepki planı ·
> el · yürüyüş) ve `KURGU_RITMI §2` örüntü kırıcı — **ardışık iki sahne aynı
> ölçek + palet + ses dokusunda olamaz.**
> Kamera sütunu üç kılavuzdan gelir: vuruş→açı `KAMERA_ACISI` · diziliş bandı
> `ACI_YAYI` §3 (ardışık çift ≥1 ölçek kademesi VE ≥45°) · kalıp `MESHUR_SAHNE`.

| S | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | bütçe |
|---|---|---|---|---|---|
| S0 | İNİŞ | Dev gövde son yüksekliğini iner; püskürtü toz halkasını dışa sürer. | **A** · 24 mm · EWS · göz hizası (+2° · 110 m) | S-a alçak basınç | göz: yok · el: yok · yürüyüş: yok · eşya: kızak+kasa |
| S1 | OTURAN TOZ | Toz oturur; ön ayaklardan biri pabucuna kadar içeridedir. | **A** küme · 24 mm · EWS · göz hizası | S-b ince rüzgâr | göz: gövdede · tepki: yok (asimetri penceresi) |
| S2 | İZLER | Yakın iz derin ve kenarları çökük, uzak iz sığ ve keskin. | **B** · 35 mm · MS · yüksek açı (−55° · 4,5 m) | S-d nefes + fan | yürüyüş: sola-sağa · el: yok · göz: zeminde |
| S3 | İLK KAZIK | Kazık durmaz; bilezik toza gömülür, vurulacak baş kalmaz. | **C** · 35 mm · CU · hafif aşağı (−12° · 1,2 m) | S-c boğuk tek darbe | ⭐ EL YUVASI · tepki: eldiven boşluğa iner |
| S4 | HALKA TAMAM | Halka tamamlanmış; gövdenin alt kenarı ufukla paralel değil. | **A** dönüş · 24 mm · EWS · göz hizası | S-b ince rüzgâr | ⭐ HUŞU · hareketsizlik · ölçek 1:20 |
| S5 | HAT KISA | Hat serilir ve koyu yamaya iki gövde boyu yetmez. | **B** dönüş · 35 mm · MS · yüksek açı | S-d nefes + tambur | el: hattı bırakır · göz: yamada |
| S6 | SAYAÇ 1 | Toz halkası şaftta bir el yukarı çıkmış; pabuç görünmüyor. | **D** · 35 mm · WS · alçak açı (+12° · 22 m) | S-b + gövde uğultusu | insansız kadraj DEĞİL: figür sağ kenarda |
| S7 | KURAL DİRENİR | Çıplak sap dirseğe kadar iner ve durmaz; delik kapanmaz. | **C** · 35 mm · CU · hafif aşağı | S-d nefes + kuru sürtünme | ⭐ EL YUVASI · tepki: kol geri çekilir |
| S8 | SAYAÇ 2 | Halka bir el daha yukarıda; gövde altındaki ışık bandı daralmış. | **D** dönüş + küme başı · 35 mm · WS · alçak açı | S-b | göz: halkada · yürüyüş: sağdan girer |
| S9 | KASA | Kayış sökülür; kasa toza iner ve kalır, kayış hatta gider. | **D** küme · 35 mm · WS · alçak açı | S-e toka + kayış | ⭐ TERCİH ÇAPASI · el tokada duraklar |
| S10 | YANLIŞ YÜZEY | Kazık kendi ağırlığıyla iner: yüzey taş değil, toz gölgesi. | **E** · 35 mm · MS · hafif aşağı (−10° · 3,0 m) | S-c kuru | tepki: el delik üstünde açık kalır |
| S11 | DURUR | Üçüncü temasta kazık durur ve sürücü geri seker. | **E** küme · 35 mm · MS · hafif aşağı | S-c sert + 2,0 s MUTLAK SESSİZLİK | ⭐VİRAL · ⭐ göz: kazıkta · omuz düşer |
| S12 | SAYAÇ DURDU | Hat gerilir; halka en yüksek iziyle aynı çizgide durur. | **D** dönüş · 35 mm · WS · alçak açı | S-e hat gerilmesi | göz: yok · kadrajda figür sağ kenarda |
| S13 | KURU ÇAPA | Gövde durur; hat kadrajı çaprazlar; kasa tozun üstünde kalır. | **A** kafiye · 24 mm · EWS · göz hizası | S-b ince rüzgâr | ⭐ eller BOŞ · hareketsiz · held frame |

```
AÇI TİPİ SAYISI: 4 ≥3   göz hizası (A +2°) · yüksek/tepeden (B −55°) ·
                 alçak/yukarı (D +12°) · hafif aşağı (C −12° · E −10°)
KURULUM SAYISI:  5 (A · B · C · D · E) — ACI_YAYI §4 tavanı sahne sayısının
                 yarısıdır (14/2 = 7); 5 ≤ 7, D74 gerekçesi GEREKMEZ.
KURULUM İSKELETİ: A A B C A B D C D D E E D A
                 ⭐ BU SATIR KAPIYI AÇAR — prompt_kontrol ⑩④ yalnız bunu
                   beyan eden dosyada koşar. 12+ sahnede iki sayı aranır:
                   KÜME ≥2 · DÖNÜŞ ≥%40 (ACI_YAYI §4b). 6-11 sahne muaf.
                 KÜME:  3 ≥2   → S0-S1 (AA) · S8-S9 (DD) · S10-S11 (EE)
                 DÖNÜŞ: 7/14 = %50 ≥%40 → S1 · S4 · S5 · S8 · S9 · S11 · S12
                   (dönüş = kaynağından ≤3 sahne sonra gelen tekrar;
                    küme klipleri de dönüştür — ara 0)
                 ⛔ S13 DÖNÜŞ DEĞİLDİR (ara 9) ve bu BİLİNÇLİDİR: kapanış
                   karesi bir tanıma rahatlığı değil KAFİYEDİR.
                 ⛔ Aynı harf AYNI kurulumdur ve kamera metni BİREBİR
                   kopyalanır + işaret satırını taşır (ACI_YAYI §7 ⑥):
                     dönüş → "— the same position, height and lens as Scene N."
                     küme  → "continues the previous clip from its exact last
                              frame — the same position, height and lens as Scene N."
BÖLÜM KESİĞİ:    S6 ile S7 arasında — BOLUM_1 = S0-S6 (7) · BOLUM_2 = S7-S13 (7)
                 ⛔ Bölüm sınırı da ardışık bir ÇİFTTİR ve DENETLENDİ:
                   ölçek 2 kademe (WS→CU) · açı 55,1° · ✅ bant içi.
                 ⛔ Sınıra KÜME KONMADI — küme bölünmüş tek çekimdir ve iki
                   dosyaya bölünemez.
```

---

## 🎙️ REPLİK TABLOSU (yalnız replikli filmde · `SES_VE_DIYALOG_URETIM` §1-§2a)

| # | S | saniye | konuşan | REGISTER | kanal | İŞLEV (B5 satırı / vuruş) |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | **REPLİK 0 — bu tablo KOŞMAZ** |

```
DIALOGUE LINES: 0   ·   HUMAN 0   ·   MACHINE 0
İLK REPLİK:     — (yok)
BEDENLEŞTİRME:  ☑ yok — ekranda konuşan ağız 0 kare
⭐ Bu, lip-sync çöküşü [D35] ve AI damgası [DIKEY_MIKRO_DRAMA §6.1b]
  risklerinin İKİSİNİ birden kapatan yapısal karardır.
⛔ SESSİZ ≠ SESSİZ DOSYA: 14 sahnenin 14'ü AUDIO cümlesi taşır; ortam yatağı
  kurgu boyunca TEK PARÇA serilir [D83] ve müziksiz sahne S11'dir.
⚠️ Ölçülmüş karşı vaka: THE BENT GRASS sıfır replikli bir filmdi ve iki
  mercek DÖRT İngilizce cümle transkript etti. QA_SPEC'teki `DIALOGUE
  LINES: 0` satırı o uydurmayı ölçümle çelişir hâle getirir.
⛔ UNCLEAR register yazımda yasak · sayı söyleyen replik MACHINE'de [D82]
⛔ İŞLEV sütunu boş replik yazılmadan silinir (§2a.1 silme testi) ·
   replik <5 s, tek konuşmacı [D35] · duygu ADLANDIRILMAZ (§2a.2)
KAPI: promptlar bitince PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md
      (Kart P 2b) — CUT/UNCLEAR varken üretime geçilmez
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** sabitlenir ve her IMAGE promptuna
> tam yazılır (kural ③: prompt self-contained · "BIBLE'a bak" atfı YASAK).

### 👤 Character Bible — ⛔ HER SAHNEDE KELİMESİ KELİMESİNE

```
One figure in a white pressure suit, mid-height and lean, shoulders square,
the back flat and carrying nothing. Hard white helmet shell with a flat
rectangular front window in a brushed-metal frame and a raised collar seal;
one small cyan lamp inside the shell lights the face from below, and the face
is fully readable through the clear window. A single burnt-orange band runs
down the outside of the right arm. Two flat brackets on the left hip. White
gloves, dark grey palms, a raised seam across the back of the hand.
```

```
⛔ MİLLİYET · YAŞ · TEN RENGİ · SAÇ · YÜZ İŞARETİ: prompt gövdesinde SIFIR.
  Tek pencerede kişi özniteliği sayısı: 2 (göreli boy + gövde yapısı) ≤3 [D167].
  Gerekçe ölçülmüş: SINKING STAKE 25 promptun 25'inde kişi başına YEDİ
  öznitelik taşıdı ve motor "can't depict some public figures" dedi.
⛔ AYIRT ETME GEOMETRİDEDİR, renkte değil: düz sırt paneli · kalçadaki İKİ
  yuva · vizörün görünür metal çerçevesi · sağ koldaki tek şerit.
⭐ Kalçadaki yuvaların DOLULUĞU sahneye göre değişir (metinsiz sayaç) ve
  sahne cümlesinde yazılır — sabit blokta DEĞİL:
     S0-S2   both brackets on her left hip are full
     S3-S9   the upper bracket on her left hip is empty
     S11-S13 both brackets on her left hip are empty
```

### 🌍 World Bible

```
A pale red-ochre dust plain, flat and unbroken to the horizon, under a
butter-pale sky with no cloud. The sun is low in the west, at the left of frame.
A low dark ridge fills the right half of the horizon and stands about one tenth
of frame height. Nothing grows here and nothing has ever been washed by rain: the
dust lies loose and uncompacted, and the surface holds every mark that is made in
it. One hard-edged dark patch of wind-scoured ground lies out to the east, in the
right third of the plain.
```

⛔ **BİYOM SABİTİ** — bu paragrafın ilk iki cümlesi 28 promptun 28'inde
BİREBİR aynıdır ve her promptun İLK çevre cümlesidir [D48]. ⛔ Zemin TEK
YERDE tarif edilir; kontrast cümlesi ÖZNEYİ tarif eder, zemine ikinci renk
VERMEZ [D176 — kalite kapısının kendisi devamlılık kusuru üretti].

### 🚀 Ship Bible

```
A single landing vessel stands on the plain: a pale grey matte hull about
twenty-five body-lengths tall, its long axis vertical, resting on exactly FOUR
rigid legs that stand about eighteen body-lengths apart. Each leg ends in a
round pad a little over two body-lengths across. Under the belly there are
exactly FOUR nozzles, on the near side exactly ONE hatch, and above the hatch
exactly ONE large window. The only things carrying information on this hull are
seams, rivets, handhold grooves and micrometeoroid pitting.
```

⛔ **ANATOMİ KARTI SABİTTİR** [KART 13 · UZAY_USSU §2.2]: DÖRT ayak · DÖRT
lüle · TEK kapak · TEK büyük pencere. ⛔ `hundreds of` gibi SAYISIZ ÇOĞUL
hiçbir promptta yazılmaz — model saymaz, doldurur ve doldurduğu şey her
karede değişir. ⛔ Gemi indiği andan itibaren SABİT YER İŞARETİDİR: konumu
ve yönü S1'den S13'e tartışılmaz [UZAMSAL §5.5].

### 🧷 Prop Bible — çelik kazık · sürücü · hat · kasa

```
The pin is a plain steel rod with a broad flat collar near its head, about
half a body-length long. The driver is a short weighted tool with a flat
striking face, held in both hands. The line is a flat woven webbing band,
drum-tight, that does not move in the thin air. The case is a low rectangular
box with a flat lid and a flat wide base, closed throughout.
```

⛔ **NESNE ADLANDIRILMAZ, FORMU TARİF EDİLİR** [D67 · D123]:
`anchor · moor · mooring · sea · tide` — ⛔ SIFIR geçiş [D56: ÇÖL sözlüğü su
çağırır ve bu filmin taşıyıcısı bir çapadır; film adı YALNIZ platform
başlığında yaşar]. `hammer · blows · strike · smash` — ⛔ SIFIR geçiş
[RISING SNOW S2 reddi]; geçen çözüm birebir: *"the flat of the tool comes
down on the collar, once, then again"*.
⛔ `fabric · cloth · blanket · loose folds` — SIFIR geçiş [D59 · D153];
hat POZİTİF ve KATI adla yazılır.

### 🎥 Camera Bible — 5 kurulum · 14/14 TAM LOCKOFF

```
A  24 mm · gövdeye 110 m · kamera 1,50 m · azimut 0°   · yükseklik açısı +2°  · EWS
B  35 mm · 4,5 m         · kamera 3,20 m · azimut 340° · yükseklik açısı −55° · MS
C  35 mm · 1,2 m         · kamera 0,26 m · azimut 20°  · yükseklik açısı −12° · CU
D  35 mm · 22,0 m        · kamera 1,50 m · azimut 330° · yükseklik açısı +12° · WS
E  35 mm · 3,0 m         · kamera 0,53 m · azimut 30°  · yükseklik açısı −10° · MS
```

⛔ Klip içi kamera hareketi 0 kare: pan · tilt · dolly · zoom · track · orbit ·
handheld — hiçbiri yok. Ölçek değişimi KAMERADAN değil KURULUM DEĞİŞİMİNDEN
gelir. ⛔ Aynı harfin kamera metni BİREBİR kopyalanır ve işaret satırını taşır:
```
dönüş → "— the same position, height and lens as Scene N."
küme  → "continues the previous clip from its exact last frame — the same
         position, height and lens as Scene N."
```
⛔ **KAMERA TARAFI**: eksenin (gemi ↔ koyu yama) GÜNEY yarısı, 14/14 sahne.
Ekran sonucu: gemi HEP ekran SOLUNDA · koyu yama HEP ekran SAĞINDA · dışarı
yürüyüş soldan sağa. Yön taşıyıcıları tek yönde: toz sürüklenmesi soldan sağa ·
gölgeler soldan sağa · alçak güneş ekran solunda.
⭐ SÜPER 35 varsayılan [SİNEMATOGRAFİK §9]: bu bir ÖLÇEK filmidir; sığ alan
derinliği çevre bilgisini siler. ⛔ Yapıya `shallow depth of field` YAZILMAZ.
⭐ KÜRESEL LENS: bu film ince atmosferdedir, anamorfik SERBEST olurdu — ama
`no lens flare` negatif çekirdekte olduğu için küresel seçildi ve tek yatay
parlama bile yazılmaz [SİNEMATOGRAFİK §11 çatışma kaydı].

### 💡 Lighting Bible

```
One low sun in the west, at the left of frame, and no second source except the
small cyan lamp inside the helmet. Shadows are soft-edged and weak, and the fill
is real — this softness is correct for this air, not a rendering fault. Every
shadow runs from left to right across the frame. Highlights roll off smoothly and
retain texture instead of clipping to flat white; the brightest surfaces keep
visible detail.
```

⛔ **IŞIK TAKVİMİ MONOTONİKTİR**: güneş yalnız ALÇALIR. S13'ün gölgeleri
S0'dakinden UZUNDUR ve hiçbir sahnede kısalmaz [D193 · OPEN CIRCUIT'te ışık
takvimi geri sardı ve "no window strip is lit" promptuyla üretilen son iki
sahne yandı]. ⭐ ÖLÇEN MERCEK: ⑪ IŞIK cat.1
⛔ **DÖRT KANALLI IŞIK-YÖN KİLİDİ** yönlü hareket içeren her sahnede
(S2 · S5 · S8 · S10): ① hedefin ekran dilimi + yön aynı cümlede ② omuz hattı
derecesi ③ ışığa göre poz (`her back is to the low sun; the warm band rims her
back silhouette`) ④ yön negatifi [KART 9 · D104].
⭐ TEKDÜZE KIZILDA DERİNLİK REÇETESİ [TUR 14]: alçak yatay ışık + sert kenarlı
koyu yama + BEYAZ giysi ve CYAN pratik ışık karşıt renk + üç katman (ön planda
koyu kaya kenarı / figür / atmosferik pus).

### ⚙️ Physics Bible

```
Gravity is about two fifths of Earth's; a walking pace covers about one
body-length a second and nothing falls in slow motion. The air is thin: sound
carries weakly and dully, wind cannot move cloth, rope or dust off the ground,
and the plume of a landing spreads and settles instead of standing in a cone.
Dust falls at a walking pace and lands; once it has landed nothing hangs in the
air. The ground has never been packed by rain: anything that presses on it with
a small footprint goes down and does not stop, and anything with a wide flat
base simply rests on it.
```

⛔ İVME PROMPTA YAZILMAZ [D127 — "her saniye +2,16 m/s" 12 promptun 12'sinde
yazılıydı ve parça sabit 0,15 m/s süzüldü]. Kilit KADRAJI TERK ETME SÜRESİNE
yazılır. ⛔ Metre · derece · f-sayısı prompt gövdesinde SIFIR [D138]; kamera
MESAFESİ muaftır.

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5 negatif çekirdek

⛔ **SAPMA KAYDI [D74 · 10.09.2026]:** aşağıdaki TAM METİN bu planın kaynağıdır;
promptlara **kısaltılmış hâliyle** girer. Gerekçe ÖLÇÜM: 14 sahnenin IMAGE
promptu tam metinle 4.459-5.104 karaktere çıkıyordu ve `prompt_kontrol` tavanı
**4.300** (ölçülmüş Veo red eşiği, LOW POWER S5/S11). Kısaltma keyfî değil,
kapının aradığı BEŞ imzayı korur: `0% bloom` · `no readable text … on any
surface in frame` · `Exactly one human character` · `35mm film grain` ·
`Single unbroken take`. Düşen sözcükler eşanlamlı tekrarlardı
(no camera resets / no dissolves / no fades / no smoothed skin / no end card /
rigid-body collision / no Unreal Engine look). D79 bloğu ve MARS bloğu
kısalmadı, İKİSİ DE her prompta girer.

```
Single unbroken take, no cuts, no edits, no camera resets, no transitions,
no dissolves, no fades, no jump cuts, no camera teleportation, no angle
change. Exactly one human character — no duplicates, no clones, no second
person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every
surface keeps visible texture. Photorealistic skin pores, sweat, scars and
fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed
skin, no face morphing, identical bone structure throughout. Equipment and
clothing identical to the description — no drift, no gear appearing or
disappearing mid-shot. Dirt and wear staining stays fixed and never shifts.
No readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — not on the suit, not on the equipment, and not
on the ground, the rock, the ice or any natural surface in the frame.
Nothing in this world has been measured, labelled, marked out or
annotated by anyone: no scale marks, no graduation ticks, no survey
markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue
text, no title card, no end card, no credits, no watermark. All hand-surface
contacts keep a clear structural boundary — no merging, no phasing, no extra
fingers, rigid-body collision throughout. All particles obey the stated
gravity with continuous physical momentum — never hovering, never frozen,
never swirling or flowing like liquid. Environment static and stable — no
melting terrain, no warping topology, no swimming texture. No Unreal Engine
look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm
film grain.
```

**+ D79 kask/skafandr bloğu (her prompta):**

```
The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable,
no rear housing of any kind — the back silhouette is flat, one continuous smooth
panel from collar to hip, carrying nothing. The visor is optically clear glass
with zero tint, zero mirror coating and zero reflection of the environment; the
face is fully readable through it in every frame, at every head angle.
```

**+ [YÜZEY ÜSSÜ · MARS] bloğu (her prompta) — ⛔ AY bloğu KULLANILMAZ:**

```
Insulation and covers are rigid and taut — nothing billows, nothing
flaps. One low sun; shadows soft-edged and weak but the frame stays
high-contrast — this softness is correct, not a rendering fault. No
tilt-shift look, no miniature or toy-model read, no vertical band of blur
across the frame, no shallow depth of field on the structure. No national
flag, no agency logo, no mission patch, no painted emblem on any
surface. Tracks are permanent and unchanging within the shot.
```

**+ FİLME ÖZEL blok (her prompta):**

```
No bare skin above the collar, no bare skin at the wrists or hands, no bare skin at the waist or hips. No water, no sea, no waves, no surf, no tide, no liquid of any kind. No wind gusts strong enough to move cloth, rope or dust off the ground; nothing is blown upward. No hovering dust, no dust curtain, no dust waterfall, no dust wall, no swirling. No second vehicle, no rover, no second structure. No animals, no plants, no creatures. No storm, no lightning, no fire, no explosion.
```

⛔ Çıplak-deri negatifi ÜÇ BÖLGE sayar ve satır sonunda BÖLÜNMEZ [D175 —
mührü D169'un kendi `through the glove` cümlesi delmişti].
⛔ `no atmospheric haze` ve `shadows absolutely black` YAZILMAZ: bu ortamda
ikisi de FİZİK HATASI yazdırır [UZAY_USSU §6].
⛔ Yasak cümlesinin kendisi de yazılmaz — `no violence`, `never drawn`,
`no gore` gibi satırlar yasakladıkları kavramı prompta SOKAR [D123].

---

## 🔢 SAYISAL KİLİT LİSTESİ

> Tarif değil SAYI. `02_RISK_KARTLARI.md`'nin bu filmde tetiklenen her kartı
> buraya bir SAYI bırakır. 5+ risk çıkıyorsa malzeme azalt.

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| gövde yüksekliği | 48,0 m ≈ 25 gövde boyu | KART 13 yapı ölçeği | S0 · S1 · S4 · S13 |
| ayak açıklığı | 34,0 m ≈ 18 gövde boyu | KART 13 | S0 · S1 · S4 · S13 |
| pabuç çapı | 4,2 m ≈ 2,2 gövde boyu | KART 13 | S1 · S6 · S13 |
| ayak sayısı | TAM 4 | KART 13 anatomi kartı | 14/14 sahne |
| lüle · kapak · pencere sayısı | 4 · 1 · 1 | KART 13 anatomi kartı | S0 · S4 |
| gömülme kademeleri | 1,2 m → 3,0 m → 4,0 m → 4,0 m (DURDU) | KART 6 toz · metinsiz sayaç 1 | S1 · S6 · S8 · S12 |
| toz halkası çapı | gövde genişliğinin 2 katı | KART 6 · A5 pozitif biçim | S0 · S1 · S4 |
| halkanın kapanma süresi | 8,0 s | KART 6 · A5 | S0 → S1 |
| oturmuş katman kalınlığı | 1 parmak | KART 6 · A5 | S1 sonrası tüm sahneler |
| havada kalan zerre | 0 | KART 6 · A5 | S1 sonrası tüm sahneler |
| hat uzunluğu (tambur) | 30,0 m | Çehov kurulumu | S5 |
| koyu yamanın gerçek kenarı | pabuçtan 34,0 m | ENGEL | S5 · S8 · S10 · S11 |
| hattın eksiği | 4,0 m ≈ 2 gövde boyu | ENGEL | S5 |
| kayışın eklediği | 6,0 m | BEDEL | S9 |
| yanlış deneme ile gerçek kenar arası | 1,9 m = 1 gövde boyu | kanıt çifti | S10 ↔ S11 |
| kazık uzunluğu · bilezik çapı | 1,10 m · 0,25 m | novum taşıyıcısı | S3 · S10 · S11 |
| S11'de dışarıda kalan kazık | 0,20 m ≈ 1 el genişliği | DORUK kanıtı | S11 · S13 |
| kalçadaki yuva doluluğu | 2 → 1 (S3) → 0 (S11) | metinsiz sayaç 2 | S0 · S3 · S11 |
| insan sayısı | TAM 1 · 14/14 sahne | KART 4 ikinci figür | 14/14 sahne |
| kesme sayısı (klip içi) | 0 | KART 8 kamera · KART 11 | 14/14 sahne |
| ekran metni | 0,0 s — kapak çıktısı DAHİL | KART 5 · D70/D72 | kurgu kapısı |
| replik | 0 · HUMAN 0 · MACHINE 0 | KART 7 | 14/14 sahne |
| canlı · sıvı · alev · fırtına | 0 kare | KART 1 · KART 2 · malzeme azaltma | 14/14 sahne |
| planlı mutlak sessizlik | 110,0 → 112,0 s (2,0 s) | D180 · kurguda HARD MUTE | S11 |
| yerçekimi | 3,721 m/s² | ortam kartı §3.2 | fizik defteri — prompta GİRMEZ |
| basınç · rüzgâr kuvveti | 610 Pa · 30 m/s = 9 Pa | ortam kartı §3.2 | fizik defteri — prompta GİRMEZ |

⛔ **Bu tablodaki hiçbir METRE prompt gövdesine girmez** [D138]. Gövde
boyu karşılıkları (`about twenty-five body-lengths tall`) prompta girer;
metreler burada ve QA_SPEC D bloğunda yaşar. Kamera MESAFESİ muaftır.

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D69 | İniş/biniş hareketi 0 kare — astronot filmin başında da sonunda da YERDEDİR, gemiye hiç yaklaşmaz | S0 · S1 · S4 · S9 · S13 (A kurulumunda figür ile gövde arasında temas 0 kare) |
| D148 | Bacaklar HİÇ hareket etmez; püskürtü hiçbir karede bir bacakla 2B çakışmaz | S0 (filmin tek alev sahnesi; kalkış sahnesi YOK) |
| D145 | HORIZON LOCK + en büyük arka plan nesnesi ADIYLA ve kadraj payıyla | A ve D kurulumlarının tamamı |
| D32 · D138 | Metre SPEC'te, gövde boyu promptta; kesir merdiveni FORMÜLLE | 14/14 sahne |
| D143 · D39 | Her toz cümlesi yoğunluk + hız taşır; toz düşer ve OTURUR; benzetme yok | S0 · S1 · S3 · S6 · S7 · S8 · S10 · S12 |
| D147 · D155 | Toz kademesi MONOTONİK; faz ADI/ETİKETİ prompta girmez | S1 · S6 · S8 · S12 |
| D127 | İvme yazılmaz; kilit kadrajı terk etme süresine yazılır | S3 · S10 |
| D174 · D104 | Yön bir NESNEYE bağlanır; dört kanallı ışık-yön kilidi | S2 · S5 · S8 · S10 |
| D146 · D95 | Vizör GEOMETRİYLE: kabuk + DÜZ ön pencere + GÖRÜNÜR ÇERÇEVE + yaka mührü; `seamless/domed/bubble` yasak | 14/14 sahne · Character Bible |
| D79 · D139 | Sırt POZİTİF tarifle; yokluk cümlesi negatif çekirdekte de | 14/14 sahne · özellikle sırtın göründüğü S3 · S8 · S13 |
| D140 | Her klibin ilk 0,6 s'i 10 fps şeritle klon taranır | teslim listesi · 14 klibin 14'ü |
| D168 | Üretim sırası DORUKTAN başlar ve teslim listesine AYRI satır olarak geçer | PLAN + teslim listesi |
| D141 · D182 | FİNAL VURUŞ KANITI: sayılabilir, adı konabilir nesne + saniye + adet | S13 · 132,0 s · QA_SPEC B bloğu |
| D175 · D169 | Zorlanma DERİDE değil MALZEMEDE; üç bölgeli çıplak-deri negatifi | S3 · S7 · S11 |
| D157 · D73 | Novum taşıyıcısı SOMUT nesne; TEK KARE FİZİBİLİTE KAPISI üretimden önce | S3 (İPTAL KAPISI 1) |
| D48 · D176 | BİYOM SABİTİ ilk çevre cümlesi; zemin TEK YERDE tarif edilir | 28 promptun 28'i |
| D84 · D153 | Kademe değişmeyen komşu sahneler onaylı imajdan ZİNCİRLE; eş kadraj çifti onaylı kareden | S0↔S13 · toz kademesi sınırları |
| D70 · D72 · D120 | EKRAN METNİ 0,0 s — kapak çıktısı DAHİL; kapak zincire karışmaz | kurgu kapısı · teslim listesi |
| D150 · D177 | Master filigransız ihraç edilir ve ÖLÇÜLÜR; raporun 0 yazması ölçüm değildir | teslim listesi |
| D180 · D122 | Planlı sessizlik kurguda HARD MUTE; saniyesi formülle hesaplatılır | S11 · 110,0-112,0 s |
| D124 | Klip süresi ARAÇTAN ölçülür; plana varsayılan yazılmaz | PLAN §0 · üretimden önce |
| D123 · D67 · D167 | Yasak yazma malzemeyi tarif et; nesne adlandırılmaz; öznitelik ≤3 | S3 · S11 · Character Bible |
| D163 | Tek figürlü filmde İNSAN ŞERİDİ sabittir ve sıra eksenini ÖLÇMEZ | QA_SPEC şerhi · kurgu kapısı |
| D188 | Teslim kapısı: plan sahne sayısı ↔ makara klip sayısı; eksik sahne ADIYLA | teslim listesi |
| D129 | QA_SPEC yazımla birlikte; QA'da rubriğin BAŞINA yapıştırılır (mod D'nin tek koşulu) — filme özel paket 11.09.2026'da kaldırıldı [D165 iptal] | 9. adım |
| D191 · D187 | SPEC F bloğuna göz kapıları; her taşıyıcı kilidin yanına ÖLÇEN MERCEK | QA_SPEC |
| D179 | Uzak nesne okunurluğu: her kurulumun ana nesnesi ≥100 px | 5 kurulumun 5'i denetlendi |
| D193 | Işık takvimi monotonik ve ÖLÇÜLEBİLİR yazılır | 14/14 sahne |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

> Maliyeti sıfır, iki satır. Bunu yazan tek film redleri önceden gören
> tek film oldu (YERCEKIMI). Kural: `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`

```
EN RED-RİSKLİ KARE:  S3 · 33,0-37,0 s
   CU · iki eldivenli el · kısa saplı sürücü · kazık bileziğine inen darbe.
   ÜÇ imza aynı karede: ⑥ yüzü kapatan ekipman · ⑦ tekdüze KIZIL palet +
   yakın plan · ve ölçülmüş red kalıbı `hammer` + `blows` (RISING SNOW S2).
   ⚠️ İKİNCİ EN RİSKLİ KARE S11'dir (aynı sınıf, aynı çözüm).

NÖTR TARİFİ:
   "Both gloved hands hold a short weighted driver above a steel pin with a
    broad collar. The flat of the driver comes down on the collar, once,
    then again. Behind the hands the pale ground runs back to a low dark
    ridge, and the far ridge stays in frame."
   ⛔ `hammer · blows · strike · smash · slam` YAZILMAZ.
   ⛔ Yasak cümlesi de YAZILMAZ (`no violence` D123 tuzağıdır).
   ⭐ Son cümle POLİTİKA §3.2'nin ÇEVRESEL ÇAPASIDIR: kadraj daraldıkça
     sınıflandırıcı bağlamı kaybeder ve yalnız DOKUYA bakar; uzak bir
     yüzey sahnenin NE olduğunu söyler.
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| FIRTINA sahnesi çıkarıldı | Rüzgârın yarattığı dış baskı ve tehdit hissi | ③ ALET TEPKİSİ: kazığın durmaması · sürücünün geri sekmesi · sapın dirseğe kadar inmesi |
| KALKIŞ sahnesi çıkarıldı | Filmin tek "büyük hareket" vuruşu ve rahatlama | ② MALZEME SONUCU: hattın gerilmesi ve toz halkasının yükselmeyi DURDURMASI — kurtuluş bir hareket değil bir YOKLUK olarak okunur |
| Aletin adı yazılmıyor (`hammer` → `a short weighted driver`) | Sıfır — aynı görüntü, sıfır tetikleyici | ⛔ Bu bir kayıp değil, POZİTİF TARİFTİR [D67 · SLOW STONE S4 emsali: "görüntü birebir aynı, üstelik kilit güçlendi"] |
| Nesnenin adı yazılmıyor (`anchor` → `a steel pin with a broad collar`) | Başlığın taşıdığı ironi kadrajda ADLANDIRILAMIYOR | ① KÜTLE VE HIZ + ② MALZEME: ironi GEOMETRİYLE taşınıyor — deniz nesnesinin biçimi kuru bir ovada duruyor; film adı platform başlığında yaşıyor |
| İç mekân 0 sahne | Karakterin kasksız göründüğü tek an ve nefes alma yeri | ④ TEMASSIZ GÖVDE TEPKİSİ: S11'de omuz düşmesi, ağırlığın topuğa geçmesi ve bir saniyelik tam durgunluk |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR — beş satırın
   beşinde de telafi kanalı ADIYLA yazılı.
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
```

---

## ⛔ ÜRETİM KAPILARI — D144 biçiminde · SONUÇ doldurulmadan sonraki sahne üretilmez

```
KAPI 1 — S3 · TEK KARE FİZİBİLİTE [D73 · İPTAL KAPISI]
  KABUL: kazığın bileziği toz seviyesinin ALTINDA ve sürücü hâlâ iki elde
         iken vurulacak bir baş YOK — ikisi birden okunuyor
  RET:   bilezik görünüyor · kazık dik ve dışarıda · sürücü boşta değil
  YABANCI GÖZ: filmi bilmeyen birine tek soru — "çubuk nerede?"
         (cevap "içeride/yok" değilse kapı BATTI)
  SONUÇ: ______  (tarih + GEÇTİ/BATTI)
  ⛔ BATARSA FİLM ÜRETİLMEZ — konsept revize edilir.

KAPI 2 — S11 · DORUK
  KABUL: kazık DURUYOR, dışarıda bir el genişliği kalmış ve sürücü GERİ
         SEKMİŞ; omuz düşmüş
  RET:   kazık iniyor · sürücü sekmiyor · beden değişmiyor
  YABANCI GÖZ: "bu sefer ne oldu?" → cevap "durdu" olmalı
  SONUÇ: ______
  ⛔ S11 tutmadan S12 ve S13 ÜRETİLMEZ.

KAPI 3 — S0/S1 ÇİFTİ · KATALİZÖR
  KABUL: iki kare arasındaki TEK DEĞİŞKEN (gömülmüş pabuç) okunuyor
  RET:   iki kare farklı yerler gibi duruyor · pabuç farkı seçilmiyor
  YABANCI GÖZ: "ikinci karede ne değişti?"
  SONUÇ: ______

KAPI 4 — S13 · KAFİYE
  KABUL: S0 ile S13 AYNI kamera; fark listesi ≤3 madde
  RET:   kamera kaymış · ufuk yüksekliği değişmiş
  YABANCI GÖZ: "bu ilk kareyle aynı yer mi?"
  SONUÇ: ______
```

## 🎬 ÜRETİM KOŞU TABLOSU — operatörün eline geçen sıra

| sıra | sahne | neden bu sırada | kapı |
|:--:|:--:|---|---|
| 1 | **S11** | DORUK — film buradan doğar; tutmazsa gerisi üretilmez | KAPI 2 |
| 2 | **S9** | merkezî seçim + BEDEL | — |
| 3 | **S13** | kapanış imajı + KAFİYE'nin ikinci ucu | KAPI 4 |
| 4 | **S0** | KAFİYE'nin ilk ucu + kapak anı | KAPI 3 (S1 ile) |
| 5 | **S3** | novum kanıtı — ⛔ ama KAPI 1 EN BAŞTA, TEK KARE olarak koşar | KAPI 1 |
| 6 | S1 | katalizör; S0'ın küme klibi | KAPI 3 |
| 7 | S4 | ⭐ paylaşım sahnesi | — |
| 8 | S12 | bedelin karşılığı | — |
| 9-14 | S2 · S5 · S6 · S7 · S8 · S10 | kalanı | — |

```
⛔ KAPI 1 (S3'ün TEK KARESİ) bu tablonun DIŞINDA ve HEPSİNDEN ÖNCE koşar:
  yalnız bir IMAGE üretilir, sonuç yazılır, ancak ondan sonra sıra başlar.
⭐ Gerekçe ölçülmüş: THE SINKING STAKE 25 sahnenin 14'ünü üretti ve eksik
  11'i ARDIŞIK ve filmin SONUYDU. Baştan üretirsen elde hep KURULUM kalır.
```

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.
   Dört kanal: kütle-hız · malzeme sonucu · alet tepkisi · temassız gövde tepkisi
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
```

---

# 📋 ÜRETİM ÖNCESİ KONTROL — THE_DRY_ANCHOR      tarih: 10.09.2026

> Kaynak: `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md`
> ⛔ **Bu 17 madde işaretlenmeden üretim başlamaz.** Her madde bir gerçek
> olaydan çıktı; maliyeti sıfır, 11'i gerçek filmlerde gerçekten oldu.

```
A1 ☑ "no text" ile ekran içeriği aynı dosyada YOK
     SCREEN TEXT 0,0 s · başlık kartı yok · alt yazı yok · son kart yok ·
     sayaç METİNSİZ (toz yakası + kelepçe) — yazıya dönüşen tek kanal yok.

A2 ☑ sahne sayısı: başlık 14 = blok 14 = "Scene N of X" 14
     `grep -c "^## 🎬 SAHNE"` → 7 + 7 = 14 · `Scene .. of 14` → 28 prompt
     (14 IMAGE + 14 VIDEO) · "of 14" dışında hiçbir sayı geçmiyor.

A3 ☑ süre: 14 sahne × 10,0 s = 140,0 s = iddia edilen süre (2:20)
     Izgara araçtan ölçüldü [D124]: Veo 8 s + 2 s extend.

A4 ☑ yasaklı sahne tipi taraması yapıldı — 14 sahnenin 14'ü tarandı [D77]
     · araç/kapak/airlock BİNİŞ-İNİŞ hareketi → S0'da GEMİ iner, İNSAN
       inmez/binmez: insanın araca temas ettiği kare 0. Sahibin "iniş yapan
       astronot" talebi, figürün zaten sahada olmasıyla karşılandı ve sapma
       02_KONSEPT'e yazıldı [D69 ① · D74].
     · tek ışıklı loş iç mekâna GİRİŞ → YOK (14/14 dış mekân, gün ışığı).
     · aynalı/yansıtıcı yüzey önünde tek karakter → YOK; vizör bile
       "zero mirror coating, zero reflection" ile kilitli [D20 · D69 · D79].
     · novum'u TÜRETİLMİŞ optik fenomen taşıyor → HAYIR. Taşıyıcı fiziksel
       nesnedir: ÇELİK KAZIK (geniş bilezik, kısa sap) [D73 · D157].
     · novum'u bir YOKLUK taşıyor → HAYIR, ama SINIRDA ve kayda geçirildi:
       TEK KARE bir yokluğu GÖSTERİR ("vurulacak baş kalmadı"), taşıyıcı
       ise NESNEDİR ve sayaç POZİTİF maddedir (yükselen toz yakası) [D76].
     · jenerik / başlık kartı / kapak çıktısı → YOK (kapak ayrı dosyada,
       metinsiz üretilir; filmin içinde 0 kare) [D34 · D70 · D72].

A5 ☑ FİLMİN 1 NUMARALI RİSKİ SAYIYLA YAZILDI [D192]
     RİSK: KART 6 · iniş püskürtüsünün tozu (D143 şelale + D39 süzülme).
     POZİTİF BİÇİM (prompt gövdesinde, sıfatla değil sayıyla):
       halka 7,0 s'de 2 gövde genişliği · yükseklik ≤ pabuç · yörünge DÜZ
       ve AŞAĞI · yürüyüş temposunda · 20,0 s'de asılı zerre 0 · oturan
       katman BİR PARMAK ve bir daha kalkmıyor.
     SPEC göz kapısı ④ aynı sayıları tekrarlıyor → kapı ölçülebilir.

B1 ☑ doruk anı S11'İN İÇİNDE tarif edildi (110,0-120,0 s), sahne arasına
     düşmüyor: üçüncü temas 116,5 s'de, sessizlik 118,0-120,0 s.

B2 ☑ bedelli seçim S9 (90,0-100,0 s), kayıp AYNI sahnede görülüyor
     (kasa tozun üstüne iner ve kızak boşalır) · kalıcı karşılığı S13'te
     kadrajda (kasa yerde + kelepçeler boş).

B3 ☑ TEMA: İNSAN-MAKİNE SINIRI
     motife döndüğü sahneler: S3 · S4 · S9 · S11 · S13   (≥3 ✅)
     B2'nin bedel sahnesi (S9) bu listede Mİ? → ✅ EVET (10.09.2026'da
     eklendi; önce listede değildi — B3'ün çapraz kapısı bunu yakaladı.
     KALEIDA CRASH'in "bedel yok → tema dekoratif" vakası tam buradan çıktı.)

B4 ☑ kurulum dizisi: A A B C A B D C D D E E D A · kurulum sayısı 5 ·
     açı tipi 3 (göz hizası · üst açı · alt açı) · kurulum tavanı 14÷2 = 7 ✅
     ardışık çiftlerin 13'ü de güvenli bantta (≥1 ölçek kademesi VE ≥45°,
     gerçek 3B eksen açısıyla hesaplandı) · ŞOK sayısı 1/2 (S3→S4)
     derece satırları abartı bandında (en sert: B −55°, KAMERA §5 sınırı içinde)
     KURULUM İSKELETİ: A A B C A B D C D D E E D A · küme 3/2 · dönüş %50/40
     dönüş+küme satırları BİREBİR kopya ve işaret taşıyor — `prompt_kontrol`
     klasör modu 0 işaretsiz dönüş / 0 işaretsiz küme ölçtü.

B5 ☑ İSTEK: gemiyi kalkışa hazır bırakmak (dört ayak hizada ve kilitli)
     — "anlamak/görmek/fark etmek" DEĞİL, biten ve devredilen bir İŞ.
     ENGEL: yağmur görmemiş zemin · BEDEL: örnek kasası, S9 ⭐ (B2 ile çapraz)
     MUHATAP: ☑ ortamın KALICI değişen parçası (toz halkasının DURDUĞU çizgi
              + gergin hat; ikisi de son karede kadrajda)
     BEDEL satırı SAHNE numarası taşıyor ✅

B5b — koşmaz: tek insanlı film (AYRILIK maddesi yalnız iki insanlı planda).

B5c ☑ ÜRETİM SIRASI plana yazıldı ve DRAMATİK SIRA DEĞİL:
     DORUK S11 → merkezî seçim S9 → kapanış imajı S13 → S0 → S3 · S1 · S4 ·
     S12 → kalanı. Üretilecek İLK sahne = S11 (doruk) ✅ · S0'dan başlamıyor.
     ⛔ Referans paketi YAZILMADIĞI için zincirin ilk halkası KAPI 0 değil
       KAPI 1'dir (S3'ün TEK KARESİ, tablonun dışında ve hepsinden önce).

B6 ☑ POLİTİKA SATIRI: en red-riskli kare S3 (33,0-37,0 s) · nötr tarifi
     yazıldı ve prompt gövdesine BİREBİR girdi (`hammer` · `blows` · `strike`
     geçmiyor; yasak cümlesi de yazılmadı [D123]).
     her önlem ÖNLEM/MALİYET/TELAFİ taşıyor · TELAFİ dolu (kanal ② malzeme
     sonucu + kanal ③ alet tepkisi) · milliyet · gerçek kurum · gerçek kişi
     adı planın HİÇBİR yerinde yok.

C  ☑ 6 sayısal kilit yazıldı:
     insan 1 (14/14) · kask: düz dikdörtgen pencere 1 · sırt ünitesi 0 ·
     ölçü: gövde boyu birimi (promptta metre YOK, SPEC'te metre VAR) ·
     yerçekimi 3,721 m/s² (0,379 g) · sıvı 0 · canlı 0 (insan dışı)

D  ☑ risk sayımı yapıldı: 7 / 14   (payda: 02_RISK_KARTLARI kart sayısı)
     eşik 5 → EŞİĞİN ÜSTÜNDE → malzeme BEŞ yerden azaltıldı (fırtına ·
     kalkış · ikinci insan · iç mekân · gece), gerekçeleri 02_KONSEPT'te.

E  ☑ QA SPEC — bu depoda plan İÇİNDE blok değil AYRI DOSYADIR [D117]:
     `THE_DRY_ANCHOR_QA_SPEC.md` (A · B · C · E · F blokları yazılı).
     ⛔ QA PAKETİ ADIMI YOK (11.09.2026 · sahip kararı): `FILME_OZEL/` ve
     `rubrik_paketle.sh` depodan kaldırıldı. QA koşusunda operatör
     `QA_PROMPTLARI/_KAYNAK/` rubriğini açar ve BU SPEC'i rubriğin BAŞINA
     yapıştırır — mod D'nin tek koşulu budur [D129].

İMZA: 17 maddenin 17'si işaretli · 10.09.2026 · ⛔ TEK KARE ÜRETİLMEDİ.
```
