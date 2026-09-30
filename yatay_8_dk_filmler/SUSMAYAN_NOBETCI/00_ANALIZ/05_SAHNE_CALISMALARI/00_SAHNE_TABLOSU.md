# 🧮 SUSMAYAN_NOBETCI — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> SUSMAYAN_NOBETCI S<nn> <ROL>`
> ile damgalanır (`S<nn>_<ROL>.md`, tam şablon). ≤ 8 sahnelik filmde (dikey)
> bu dosya yoktur, her sahne dosya alır.
>
> Kapı: `prompt_kontrol.py` ㉚ — satır sayısı = bölüm dosyalarındaki sahne
> sayısı · beş rol dosyası var. Satırlar betik damgalar (`| S00 |` …); elle
> satır eklenmez/silinmez, sahne sayısı değişirse `--sahne-guncelle`.
>
> ⛔ Bu klasörde `## … SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ
> (kapı betiği o desenleri sahne/prompt sanar). Prompt yalnız bölüm dosyasında.

## Sütunlar — her hücre TEK satır, boş hücre yok ("—" yazılır)

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) | `03_SAHNE_SIRALAMASI` |
| **OLAY BAŞ → SON** | ne değişiyor: `<başta> → <sonda>`; klip içi değişim varsa `⚠️ARA` | çalışma şablonu 🎬 |
| **B5** | İSTEK / ENGEL / BEDEL / MUHATAP / AYRILIK — bu sahne hangi satırı taşıyor | `02_KONSEPT_VE_RISK` |
| **KURULUM** | harf + işaret (`B · dönüş S3`) · lens · mesafe · ölçek · açı tipi | `ACI_YAYI` §3-§4 |
| **OPTİK** | kadraj eni (m) · ana nesne (px) — ⛔ ≥100 px [D179]; sığmıyorsa `⛔` | `KILAVUZ` §5.2 hesabı |
| **IN FRAME** | face · hands · torso · legs · full body · back · none — promptun ilk satırı olur [㉖] | `IMAGE_VIDEO_PROMPT_TEMPLATES` V3 |
| **TAŞIYICI** | devamlılık: giren/çıkan/taşınan nesne + önceki/sonraki sahne | çalışma şablonu 👤 |
| **IŞIK · SES · FİZİK** | üçü tek hücrede `·` ile; palet/ses dokusu öncekiyle AYNI olamaz | ortam kartı · `KURGU_RITMI` §2 |
| **REPLİK** | `—` ya da `<saniye> · konuşan · İŞLEV · ağız okunuyor/okunmuyor` | `DIYALOG_SAHNESI` §2-§3 |
| **KİLİT / UYARI** | bu sahneye düşen kilit(ler) D-no ile + `04_UYARI_NOTLARI` satır no; en çok 3 | `01_QA_DERS_HASADI` |
| **İZLEYİCİ CÜMLESİ** | "bu figür ne istiyor" — seems/probably YASAK; ⭐VİRAL ise `YÜZ:` + `HAREKET:` | `OYUNCULUK_YAZIM` §1 · §3 |
| **KAPI** | ⬜ → ✅ satır tam ve optik tutuyor; ✅ olmadan o sahnenin promptu yazılmaz | — |

Doldurulmuş satır nasıl görünür (örnek; gerçek satırlar aşağıda betik damgalıdır):

```
S03 · glove closes on wheel → wheel stopped, strap slack ·  ENGEL  ·  B · dönüş S1 · 35mm · 1,6 m · MCU · eye level
    · 1,1 m · 340 px  ·  hands, torso  ·  strap in (S02) / out (S05)  ·  neutral ceiling · hum + warble · 0,25 g
    · —  ·  D200 · D216 · U-4  ·  he wants the wheel to move, not to understand it  ·  ✅
```

---

## 📋 TABLO

| S | OLAY BAŞ → SON | B5 | KURULUM | OPTİK (eni m · px) | IN FRAME | TAŞIYICI | IŞIK · SES · FİZİK | REPLİK | KİLİT / UYARI | İZLEYİCİ CÜMLESİ | KAPI |
|:--:|---|:--:|---|---|---|---|---|---|---|---|:--:|
| S00 | mekiğin motor konisi yanıyor, gövde bütün; sağ eldiven motor kolunun bir avuç üstünde → 3,0 s'de gövde ikiye ayrılmış, parçalar dönerek açılıyor; eldiven kolun üstünde donmuş | ENGEL | A · ilk · 35mm · 1 m back · medium shot · over-the-shoulder | 1,03 m · eldiven+kol 373 px · mekik camda nokta, ayrılma hareketi | hands, back | kapsül yuvası kadraj DIŞI (E'de) · yorgunluk 1 · kanatlar kapanık (ekranda değil) | P1 4500K panel + camda sert güneş · Y1 uğultu + nefes · 0 g, eldiven hafif süzülür | — | D192 · D157 · R1 | o kola basarsa aynısı ona olacak — eli bu yüzden duruyor | ✅ |
| S01 | profil pencereye dönük, uzakta üç pencerede fener sallanıyor → sağ eldiven lamba anahtarını bir kez çevirmiş, kokpit ışığı bir kez yanıp sönmüş | MUHATAP | B · ilk · 50mm · 1 m · close-up · profile | 0,72 m · yüz 533 px | face, hands | fener 3 · yorgunluk 1 | P1 + yüzde 4500K rim fill · Y1 + telsiz · — | 12,0 s · yetişkin (telsiz) · MUHATAP · ağız kadraj dışı | D16 · D203 · R7 | orada birileri var ve onu görmelerini istiyor | ✅ |
| S02 | çekici halkaya dönük yaklaşıyor → halka hattın dışına bir gövde boyu kaymış, çekici yanından geçiyor, burun hâlâ gemiye | ENGEL | I · ilk · 35mm · 30 m · medium shot · eye level | 30,9 m · çekici 746 px · kapsül 150 px | torso | kapsül yuvada · pilot kanopide (yüz yok) · mesafe 20 m | P2 sert güneş sol üst kadraj dışı · Y2 hışırtı · soğuk gaz yok | 25,0 s · yetişkin · ENGEL/alt metin · ağız yok | D174 · D200 · Y2 · Y3 | yanaşmak istiyor ama motoru yakamadığı için kayıyor | ✅ |
| S03 | ekranda mekiğin arka yarısı motoru yanarak savruluyor, uydunun iki kanadı açık → kanatlar hâlâ açık, arka yarı vurulmadı; sol eldiven ekranın kenarında | ENGEL | C · ilk · 50mm · 0,8 m · close-up · high angle | 0,58 m · ekran 662 px | hands | ibre ¾ · ayırma kapağı kapalı · yorgunluk 1 | P1 + ekran griliği · Y1 · — | — | D78 · D157 · Y8 | kuralı izliyor: kanatlar açıkken ateş yok | ✅ |
| S04 | S3'ün son karesi: kanatlar açık → kanatlar katlanmış, 3,0 s sonra arka yarı ikinci kez ayrılmış, motoru sönmüş, parçalar sağa doğru dağılıyor | ENGEL | C · küme S3 (DEVAM) | = S3 | hands | parçaların yönü: tahliye gemisine (S11 · S13 tohumu) | P1 · Y1 · ekranda parçalar dönme momentumuyla | — | D213 · D198 · R8 | kanatlar kapanınca ateş geri geliyor — bunu gördü | ✅ |
| S05 | kanatlar yeniden açık, eldiven kola uzanmış → eldiven kolun bir avuç önünde durup bekliyor, camda halka yanından geçip kadrajı sağdan terk ediyor | İSTEK × ENGEL | A · (S0'dan 5 sonra) · aynı kamera cümlesi | = S0 | hands, back | pencere kaçtı · yorgunluk 1 | P1 · Y1 + nefes tutuluyor · — | — | D202 · D206 · Y4 | pencere var ama hesap bitmeden basmıyor — ve kaçırıyor | ✅ |
| S06 | başparmak kapağın üstünde → kapağa iki kez vurmuş, kapak açık kalmış; sol eldiven itici kolunu geri çekmiş, gövde titreşimi | geçmiş karar | C · dönüş S4 | = S3 | hands | TOHUM: ayırma kapağı açık · ibre ¾ · alışkanlık 1/3 | P1 · Y1 + püf gövdeden · püf görünmez | — | D78 · D200 · Y5 | kaçış yolunu açık tutarak geri çekiliyor | ✅ |
| S07 | çekici gemiden 8 m'de → 60 m açılmış, soğuk gaz püfleri ters yönde; arkada pencerelerde fener hızlı hızlı yanıp sönüyor | AYRILIK | I · (S2) · aynı kamera cümlesi | = S2 · tahliye arka planda 290 px | torso | mesafe 8 → 60 m · kapak açık (kadrajda değil) | P2 · Y2 + telsiz · püf düz koni ≤0,25 s | 73,0 s · yetişkin · İSTEK (karşı teklif) · ağız yok | D200 · D217 · Y5 | kendi güvenliğini seçiyor, ötekiler geri çağırıyor | ✅ |
| S08 | coğrafya: gezegen kenarı alt üçte bir, uydu ışığı kenarın ¼ kare yukarısında sağda, kurtarma gemisi ışığı sol kenarda → aynı; uydu ışığı 2 s'de bir tarama yanıp sönmesi sürüyor | İSTEK | Y · ilk · 24mm · 400 m · wide shot · eye level | 600 m · kenar tam genişlik · tahliye 96 px (ikincil) | none | sayaç K4 = 1/4 · yıldız yok | P2 · Y2 hışırtı · — | — | D209 · D78 · Y14 | (insansız) ulaşılacak sınır ve bekleyen el orada | ✅ |
| S09 | üç pencere, üç fener, iki pencerenin iç kenarında buğu → aynı; fenerlerden biri pencereye yaklaşıp uzaklaşıyor | BEDEL (tohum) | F · ilk · 50mm · 12 m · medium shot · eye level | 8,6 m · pencere sırası 670 px | none | fener 3 · buğu t=0'da var (büyümez) | P2 + pencerelerden sıcak iç ışık · Y2 + telsiz · — | 94,0 s · yetişkin · BEDEL/zaman · ağız yok | D193 · R8 · R6 | (insansız) içeridekilerin havası azalıyor | ✅ |
| S10 | sarılı hortum konsol askısında değil → hortumun ucu askıya takılmış; manivela aynı askıda; başparmak kapağa iki kez vurmuş, kapak açık | İSTEK | C · dönüş S6 | = S3 · hortum ucu 540 px | hands | manivela kuruldu (S41) · hortum (S43) · alışkanlık 2/3 | P1 · Y1 · hortum rijit, süzülmez | — | D206 · Y12 · D78 | planı hazırlıyor ama kaçış kapağını yine açık bırakıyor | ✅ |
| S11 | çekici 60 m'de, burun gemiden ayrık → burun gemiye dönmüş, 45 m; arka planda mekik parçaları dönerek tahliye gemisine süzülüyor | ENGEL | I · dönüş S7 | = S2 | torso | parçalar sağda (S4'ün yönü) · mesafe 45 m | P2 · Y2 · parçalar sabit oranla takla | — | D198 · D174 · Y7 | geri dönüyor — enkaz da aynı yöne gidiyor | ✅ |
| S12 | ibre ¾, eldiven itici kolunda → ibre ½, kol kısa kısa üç kez çalışmış; ekranda halka hatta | ZAAF | C · dönüş S10 | = S3 | hands | ibre ½ · mesafe 30 m | P1 · Y1 + püf · — | — | D78 · D206 · Y8 | gazı sayarak kullanıyor, bitmesin diye | ✅ |
| S13 | en büyük enkaz parçası kadraj solunda dönerek yaklaşıyor, pencereler sağda → enkaz pencerelere iki gövde boyu kalmış; fenerler pencereden çekilmiş | ENGEL | F · dönüş S9 | = S9 · enkaz 3 m → 670 px | none | fener 3 · enkaz S16'da geçer | P2 · Y2 hışırtı (nefes kesilir) · enkaz eksen etrafında sabit takla | — | D198 · D213 · R4 | (insansız) bölme eziliyor olabilir | ✅ |
| S14 | eldiven itici kolunda → eldiven kolun üstünde donmuş, parmaklar açılıp kapanmış | MUHATAP | C · dönüş S12 | = S3 | hands | ibre ½ · yorgunluk 2 | P1 · Y1 + telsiz + pilotun tek sözü · — | 141,5 s yetişkin (KARAR) · 144,0 s pilot 'Don't.' (İSTEK ÇAPRAZI) · ağız kadrajda yok | D203 · D217 · R7 | onlara durmalarını söylüyor, elinden başka bir şey gelmiyor | ✅ |
| S15 | tahliye gemisinin motor konisi yanıyor, itici kümesi sağ yanda → 3,0 s'de itici kümesi dikişinden ayrılmış, takla atarak uzaklaşıyor; gövde ters yöne dönmeye başlamış | ENGEL | J · ilk · 35mm · 35 m · medium shot · profile | 36 m · gemi 1600 px · itici 107 px | none | itici kümesi yok (S16+) · enkaz yaklaşıyor | P2 · Y2 dış ses yok · koni düz, çakma ≤6 kare, kristal ≤2 s | — | D192 · D213 · R1 · R4 | (insansız) çarpışmadan kaçtı ama vuruldu | ✅ |
| S16 | S15'in son karesi: gövde dönmeye başlamış → enkaz yaşam bölmesinin bir gövde boyu yanından geçmiş; gemi turunu yirmi saniyede bir tamamlayacak hızla dönüyor | ENGEL | J · küme S15 (DEVAM) | = S15 | none | dönme oranı film boyu sabit (Y6) | P2 · Y2 · dönüş tek yönde | — | D198 · Y6 · D213 | (insansız) bölme kurtuldu, gemi kontrolsüz | ✅ |
| S17 | ekranda kanatlar açılıyor, eldiven itici kolunda → çekici ateşleme yönüne yarı dönmüş, kanatlar katlanıyor, eldiven kolda kalmış | ZAAF | C · dönüş S14 | = S3 | hands | ibre ½ → dibe iki parmak · deneme 1 | P1 + ekran · Y1 + püf · — | — | D78 · R8 · Y8 | pencereyi yakalamaya çalışıyor, hazırlıksız | ✅ |
| S18 | tahliye gemisi dönüyor, halka çekiciden uzakta → halka bir tur sonra çekiciye bakıp yeniden dönüp gidiyor | ENGEL | I · (S11'den 7 sonra) · aynı kamera cümlesi | = S2 | torso | dönme oranı = S16 · mesafe 25 m | P2 · Y2 · — | — | Y6 · D174 · Y2 | halka her turda bir anlığına yakın | ✅ |
| S19 | üç pencere kadrajın altında → üç pencere sırayla aşağıdan yukarı kadrajdan geçiyor, her birinde bir fener sallanıyor | MUHATAP | G · ilk · 85mm · 8 m · close-up · low angle | 3,39 m · pencere 283 px | none | fener 3 (son kez üç) · buğu | P2 + iç sıcak ışık · Y2 + telsizde nefesler · — | — | D193 · R8 · Y6 | (insansız) içeride üç kişi var ve sallanıyorlar | ✅ |
| S20 | halat çekicinin burnundan fırlatılmış, havada düz → halat halkaya takılmış, gerilmiş, çekici halkaya doğru sertçe çekilip savrulmaya başlamış | İSTEK | I · dönüş S18 | = S2 · halat ucu 60 px (hat okunur) | torso | halat · mesafe 15 m · deneme 2 | P2 · Y2 · halat yük altında düz | — | Y11 · D206 · D213 | kapsülsüz bir yol deniyor | ✅ |
| S21 | çekici halatın ucunda savruluyor, eldiven kesici kolda → kol çekilmiş, halat serbest, ibre dibe bir parmak | ZAAF | C · dönüş S17 | = S3 | hands | ibre dibe bir parmak · halat gitti · yorgunluk 3 | P1 · Y1 + gövdeden darbe · savrulma kabine iletilir | — | D78 · D206 · Y4 | deneme bedel bıraktı: gaz neredeyse bitti | ✅ |
| S22 | yüz ön cama dönük → bakış yan penceredeki kapsüle gidip ön cama dönmüş, ikinci kez kapsülde kalmış | BEDEL | E · ilk · 28mm · 1,5 m · medium shot · eye level | 1,93 m · yüz 220 px · yan pencerede kapsül | face, hands | kapsül yan pencerede (reddedilecek seçenek kadrajda) · yorgunluk 3 | P1 + rim fill · Y1 · kollar süzülür | — | D202 · D16 · Y10 | kaçış kapsülünü bir yem olarak görüyor | ✅ |
| S23 | başparmak kapağa vurmak için kalkmış → vurmamış, eldiven kapaktan geri çekilip dizine inmiş | geçmiş karar | C · dönüş S21 | = S3 | hands | sınır: fener 3 → 2 · alışkanlık 3/3 (yarım) | P1 · Y1 · — | — | D78 · D207 · Y4 | o yolu açık tutmayı ilk kez bırakmaya yaklaşıyor | ✅ |
| S24 | çekici burnu gemiden ayrık → son püflerle burun ateşleme yönüne dönmüş ve orada tutuluyor | İSTEK | I · dönüş S20 | = S2 | torso | ibre dibe yarım parmak (kadrajda değil) · fener 2 | P2 · Y2 · püf düz koni | — | D200 · Y5 · Y7 | hazırlanıyor: bir sonraki pencereyi kaçırmayacak | ✅ |
| S25 | pilot kapsülün içinde, eldivenler zamanlayıcı düğmesinde → düğme çevrilmiş; kamera tek boş koltuğu da görüyor | BEDEL | Q · ilk · 35mm · 0,8 m · close-up · high angle | 0,82 m · düğme 234 px | hands | A4: içeride başlar · tek kişilik koltuk | P4 aynı 4500K + turuncu şerit · Y3 kapsül fanı · — | — | D69 · R3 · D179 | kendi kaçışını kendi eliyle hazırlıyor | ✅ |
| S26 | S25'in son karesi: düğme çevrilmiş → eldiven düğmeyi geri, kısa süreye çevirmiş | BEDEL | Q · küme S25 (DEVAM) | = S25 | hands | sınır: fener 2 → 1 · zamanlayıcı kısa (S30 halka) | P4 · Y3 · — | — | D213 · Y13 · R8 | vakit yok, kapsülü yakında patlatmaya razı | ✅ |
| S27 | tek fener pencerede → fener iki kez yanıp sönmüş | MUHATAP | F · (S13'ten 14 sonra) · aynı kamera cümlesi | = S9 | none | fener 1 (son) · buğu | P2 · Y2 + telsiz · — | 272,0 s · yetişkin · TERSİNMİŞ AYRILIK · ağız yok | D217 · D193 · R7 | (insansız) ona gitmesini söylüyorlar | ✅ |
| S28 | sol eldiven kapsül geçit kapağının kolunda → kol kapanmış; eldiven lamba anahtarını üç kez çevirmiş | MUHATAP | H · ilk · 50mm · 0,6 m back · close-up · over-the-shoulder | 0,43 m · eldiven 536 px | hands, back | kapsül geçidi kapalı · yorgunluk 4 | P1 + lamba üç kez · Y1 · — | — | D139 · D213 · Y9 | hayır diyor: kalıyor | ✅ |
| S29 | başparmak kapağın üstünde, kapsül yan pencerede → başparmak vurmamış, eldiven kolu sonuna çekmiş; kapsül yuvadan bir avuç ayrılmış | BEDEL | E · (S22'den 7 sonra) · aynı kamera cümlesi | = S22 | face, hands | ALIŞKANLIK KIRILMASI · kapsül ayrılıyor · yorgunluk 4 | P1 + rim fill · Y1 + gövdeden kilit sesi · — | — | D202 · D179 · Y10 | MERKEZÎ SEÇİM: kaçışı elinden bırakıyor | ✅ |
| S30 | kapsül çekicinin yanından bir avuç ayrılmış → motoru yanmış, 3,0 s'de dikişinden ayrılmış, bir parçası çekicinin kenet halkasına çarpıp halkayı eğmiş | BEDEL | T · ilk · 35mm · 40 m · wide shot · high angle | 41 m · kapsül 112 px · halka 125 px | none | kapsül yok (S31+) · halka eğik (S34) · ekranda kanatlar açılır | P2 · Y2 dış ses yok · çakma ≤6 kare, kristal ≤2 s, parça sabit takla | — | D192 · D213 · R1 | (insansız) kaçış yolu gitti, bedel halkaya da sıçradı | ✅ |
| S31 | yan pencerede boş yuva, ekranda kanatlar açık → motor kolu itilmiş, gövde koltuğa bastırılmış, 3 s sonra kol geri, motor susmuş | İSTEK | E · dönüş S29 | = S22 · yan pencerede boş yuva | face, hands | boş yuva · burn 3 s · yorgunluk 4 | P1 · Y1 + motor titreşimi · itki süresince eşyalar kıça | — | D200 · Y13 · D179 | pencereyi bu kez kullanıyor | ✅ |
| S32 | çekici motorsuz, dönen gemiye doğru süzülüyor → aynı yönde sabit hızla süzülmeyi sürdürüyor; kapsül yuvası boş, uydu ışığı uzakta tarıyor | BEDEL | T · dönüş S30 | = S30 · boş yuva 112 px | none | ekranda kanatlar kapandı (sınır) · mesafe 30 → 10 m | P2 · Y2 · sabit hız, dönüş yok | — | D198 · Y14 · D209 | (insansız) artık geri dönüş aracı yok, yalnız gidiş | ✅ |
| S33 | camda tahliye gemisi dönüyor → son püflerle çekici eşlenmiş, camda gemi dönmüyor gibi duruyor, gezegen kenarı camda süzülüyor; ibre dipte | ZAAF | A · (S5'ten 28 sonra) · aynı kamera cümlesi | = S0 | hands, back | ibre DİP · eşlenik dönüş · yorgunluk 4 | P1 + camda süzülen gezegen · Y1 + son püf · — | — | D78 · Y6 · D206 | son gazıyla dönen gemiye kendini eşledi | ✅ |
| S34 | profil camın alt kenarına dönük → bakış eğik halkaya kilitlenmiş, nefes durmuş, omuzlar kalkık | ENGEL | B · (S1'den 33 sonra) · aynı kamera cümlesi | = S1 | face | halka eğik (S30) · TEL: nefes tutma 1 | P1 + rim fill · Y1 nefes kesilir · — | — | D16 · D202 · Y15 | yanaşacak halkanın eğildiğini gördü | ✅ |
| S35 | çekici eğik halkayla gemiye 10 m'de → 3 m'de, yön değişmeden yaklaşıyor; gezegen kenarı arkada süzülüyor | ENGEL | I · (S24'ten 11 sonra) · aynı kamera cümlesi | = S2 | torso | gaz yok · halka eğik · mesafe 3 m | P2 · Y2 + seyrek nefes · sabit hız | — | D174 · Y2 · R5 | çarpacağını biliyor, düzeltecek gazı yok | ✅ |
| S36 | çekici kameraya gelirken halkalar arasında bir kol boyu → 4,0 s'de temas, eğik halka çarpmış, çekici bir kol boyu geri sekmiş | İSTEK × ENGEL | K · ilk · 35mm · 15 m · wide shot · eye level | 15,4 m · halka 249 px · pilot kanopide 74 px | torso | temas · sekme · dönüş sürüyor | P2 · Y2 temasta dış ses yok, nefes yarım saniye tutulur · parçalar birbirine geçmez | — | D213 · R5 · D179 | DORUK: ilk temas tutmadı | ✅ |
| S37 | S36'nın son karesi: çekici bir kol boyu geride → geminin dönüşü halkaları yeniden buluşturmuş, oturmuş; dört kelepçeden üçü kapanmış | İSTEK | K · küme S36 (DEVAM) | = S36 · kelepçe 0,3 m → 37 px (sayı kadrajda değil, L'de) | torso | 3/4 kelepçe · yorgunluk 5 | P2 · Y2 + gövdeden üç tıkırtı · — | — | D213 · R5 · D202 | umut: neredeyse tuttu | ✅ |
| S38 | camın alt kenarında dördüncü kelepçe yarıda → kelepçe yük altında sıkışmış kalmış, halka titriyor; omuzlar kalkık ve orada | ENGEL | A · (S33'ten 5 sonra) · aynı kamera cümlesi | = S0 · kelepçe camda 190 px | hands, back | sınır: fener 1 → 0 · TEL 2 · yorgunluk 5 | P1 · Y1 + gövdeden gıcırtı · titreşim kabine | — | D206 · D207 · Y4 | son kelepçe tutmuyor ve bedeni geriliyor | ✅ |
| S39 | eğik halkanın kenarı → kenardan düz çizgili ince buz kristali akışı sürüyor | ENGEL | L · ilk · 85mm · 3 m · close-up · high angle | 1,27 m · kelepçe 453 px · akış 200 px | none | sızıntı · geçit kapalı | P2 · Y2 (tıslama yalnız içeriden) · kristal düz çizgide, kıvrılmaz | — | Y5 · D200 · R8 | (insansız) hava kaçıyor, geçit açılamaz | ✅ |
| S40 | pilot gövdenin dışında, iki eldiven tutamakta → gövde dönüşüyle savrulmuş, tek eldivenle tutunmuş, bacaklar süzülüyor | kendi bedeni | M · ilk · 24mm · 8 m · medium long shot · low angle | 12 m · pilot 304 px · sırt görünür | full body, back | A4: dışarıda başlar · manivela kemerde · yorgunluk 5 | P2 · Y4 gövdeden + nefes · ön kol gerilir @1 s | — | D139 · D206 · R3 | dışarı çıkmak zorunda kaldı ve dönüş onu atmaya çalışıyor | ✅ |
| S41 | manivela eğik kenara yerleşmiş → kenar iki çekişte düzlenmiş, kelepçe yuvasına yarıya kadar girmiş | kendi bedeni | N · ilk · 50mm · 1,2 m · close-up · high angle | 0,86 m · eldiven 268 px | hands | manivela (S10 kurulumu) · deneme 3 | P2 · Y4 metal gıcırtı gövdeden · gövde ağırlığı @3 s | — | D213 · Y12 · D206 | halkayı eliyle düzeltiyor | ✅ |
| S42 | eldiven yarı giren kelepçenin üstünde → kelepçe bastırılıp oturmuş, akış kesilmiş; pilot kapağa doğru çekiliyor (eşiği geçmez) | İSTEK | M · dönüş S40 | = S40 | full body, back | sızıntı yok · SAĞ eldiven avucunda parlak sürtünme izi başlar · yorgunluk 6 | P2 · Y4 + gövdeden tık · — | — | D69 · D139 · R3 | kilit tamam: içeri dönüyor | ✅ |
| S43 | kenetli çift, uydu ışığı kenarın 1/12 kare yukarısında, pencereler karanlık → aynı; uydu ışığı 2 s'de bir taramayı sürdürüyor | BEDEL | Z · ilk · 24mm · 30 m · wide shot · eye level | 45 m · kenetli çift 1790 px · motor 170 px | none | fener 0 · K4 = 1/12 · hortum bağlı (kadraj dışı) | P2 · Y2 + gövdeden hortum tıslaması · — | — | D78 · Y14 · D209 | (insansız) kenar hâlâ uzak, hava yetmeyecek | ✅ |
| S44 | yan pencerede boş yuva, ekranda kanatlar kapalı, eldiven kolun başında → kol tek hamlede sonuna itilmiş, gövde koltuğa çakılmış, gevşek eşyalar kıça uçmuş | BEDEL | E · (S31'den 13 sonra) · aynı kamera cümlesi | = S22 | face, hands | İLK↔SON (S0) · pencere YOK · yorgunluk 6 | P1 · Y1 + motor titreşimi · itki süresince tek yön kıç | — | D202 · Y13 · R2 | ⭐ YÜZ: çene kasılır, gözler ön cama kilitlenir 1,0 s · HAREKET: gövde koltuğa çakılır, eşyalar kıça uçar | ✅ |
| S45 | kenetli çift kenara hızlanıyor, motor konisi yanıyor → 3,0 s'de motor bölümü dikişinden ayrılmış, takla atarak geride kalıyor; çift süzülmeyi sürdürüyor | BEDEL | Z · dönüş S43 | = S43 | none | motor bölümü yok (S47) · K4 = 1/20 | P2 · Y2 dış ses yok → kurguda 2 s sessizlik · çakma ≤6 kare, kristal ≤2 s | — | D192 · D213 · R1 | (insansız) bedel 2: artık kendi başına hareket edemez | ✅ |
| S46 | pilot bölmede, kask kucağında, ikinci eldiven omzunun bir avuç yakınında → eldiven omzu kavramış, pilotun sağ eli o eldivenin üstüne kapanmış, omuzlar inmiş | MUHATAP | R · ilk · 35mm · 1,5 m · medium shot · eye level | 1,54 m · yüz 273 px | face, hands, torso | kask AÇIK girer · SAĞ eldivende sürtünme izi · yorgunluk 5 | P5 geçitten 4500K tek kaynak · Y5 bölme + ses · 0 g, kask kucakta süzülür | 465,0 s · yetişkin (telsizsiz) · ÇİFT (R1 cevabı) · ağız kadraj dışı, pilotun dudakları kapalı | R9 · D16 · Y15 | ulaştı: o ses artık yanında | ✅ |
| S47 | kenetli çift kenarı geçmiş, uydu ışığı kenara oturmuş yarısı kesik; kurtarma gemisinin motoru sol kenarda yanıyor → motor yanmayı sürdürüyor, ateş gelmiyor; boş yuva kadrajda | ortamın kalıcı parçası | Z · dönüş S45 | = S43 · boş yuva 102 px | none | FİNAL VURUŞ KANITI: boş yuva ×1 · kurtarma motoru ×1 · uydu ışığı ×1 · K4 = 0 | P2 · Y2 hışırtı · müzik çözülür (kurgu) | — | D141 · D157 · Y1 | (insansız) makine hâlâ tarıyor ama artık göremiyor | ✅ |


---

## ⏱️ SON 3 s — 7-10. saniyede beden/nesne ne yapıyor (`SAHNE_DOLULUGU` §6 · sütun şablonda yok, burada)

```
S00 eldiven kolun üstünde, parçalar camda açılmayı sürdürür      S24 burun yönünde tutulur, son püf düz koni
S01 profil pencerede, lamba ışığı söner, nefes omuzda             S25 eldivenler düğmede, fan uğultusu
S02 çekici yanından geçmeyi sürdürür, halka arkada kalır          S26 düğme kısa konumda, eldiven üstünde kalır
S03 kanatlar açık, arka yarı savrulmayı sürdürür                  S27 fener ikinci sinyalden sonra sallanır
S04 parçalar sağa dağılmayı sürdürür                              S28 eldiven anahtarda, üçüncü çevirmeden sonra
S05 eldiven bekler, halka kadrajı terk etmiş                       S29 kol sonda, kapsül bir avuç ayrık ve ayrılmayı sürdürür
S06 itici kolu geride, püflerin titreşimi                          S30 halka eğik, parça dönmeyi sürdürür
S07 çekici uzaklaşmayı sürdürür, fener sinyali                     S31 gövde koltuktan kalkıp süzülmeye başlar
S08 uydu ışığı tarar (2 s'de bir)                                  S32 süzülme aynı hızda sürer
S09 fener pencerede sallanır                                       S33 gezegen kenarı camda süzülür
S10 başparmak ikinci vuruştan sonra kapağın yanında                S34 bakış halkada, omuzlar kalkık
S11 çekici dönüşü sürdürür, parçalar takla                         S35 yaklaşma sabit hızla sürer
S12 kol üçüncü kısa çalıştırmada                                   S36 sekme sonrası geri süzülme sürer
S13 enkaz takla atarak yaklaşmayı sürdürür                          S37 üçüncü kelepçe kapanmış, gövde titreşimi
S14 parmaklar açılıp kapanır, kol üstünde                          S38 halka titrer, omuzlar kalkık kalır
S15 itici kümesi takla, gövde dönmeye başlar                       S39 kristal akışı sürer
S16 dönüş sürer, enkaz kadrajı terk eder                           S40 tek eldiven tutamakta, bacaklar süzülür
S17 kanatlar katlanır, eldiven kolda                               S41 manivela ikinci çekişte
S18 halka dönüp gider                                              S42 pilot kapağa doğru çekilmeyi sürdürür
S19 üçüncü pencere kadrajdan çıkar                                 S43 uydu ışığı tarar
S20 çekici savrulmayı sürdürür, halat düz                          S44 gövde koltukta, eşyalar kıç duvarında
S21 halat ucu uzaklaşır, eldiven kolda                             S45 motor bölümü takla atarak küçülür
S22 bakış kapsülde kalır                                           S46 eller üst üste, omuzlar nefesle kalkıp iner
S23 eldiven dizinde, başparmak kıpırdar                            S47 kurtarma motoru yanmayı sürdürür, uydu ışığı tarar
```
