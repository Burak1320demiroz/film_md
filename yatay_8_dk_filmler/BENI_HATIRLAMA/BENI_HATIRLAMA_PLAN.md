# 🎬 BENI_HATIRLAMA — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.
>
> Kaynak zinciri: `00_ANALIZ/00_HIKAYE_ONAYI.md` (ONAY 17.09.2026 · TUR 1/3) → `01_QA_DERS_HASADI` → `02_KONSEPT_VE_RISK` →
> `03_SAHNE_SIRALAMASI` → `04_UYARI_NOTLARI` → `05_SAHNE_CALISMALARI/` (tablo 48 satır · 5 kilit dosya · B1-B4 kısa çalışma).
> Bu dosya sonucu taşır, hesabı değil. Aşağıdaki İngilizce bloklar promptların KAYNAĞIDIR, kopyası değil.

```
FORMAT:        yatay 8 dk (48) — KILAVUZ_REHBERI §2.7 modül hattı
               ⚠️ 6/8 dk: QA birimi BÖLÜM — SPEC A `PART GRID` satırı dolu (K1 sahip kararına göre)
ORTAM:         §3.4 KALIN ATMOSFER (yüzey: kum düzlüğü · fırtına) + yarık mağara iç hacmi + iniş aracı kokpiti
TÜR:           bilimkurgu · dal YUMUŞAK (hafıza · kayıp · iletişim)
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
               ölçüm gelene kadar 10 s VARSAYIM (SPEC'te ⬜ işaretli)
SAHNE SAYISI:  48        RUNTIME: 48 × klip (hook S0 48'in İÇİNDE) · varsayım 480 s = 8:00
BÖLÜM:         4 × 12 yazım dosyası — BOLUM_1 S0-S11 · BOLUM_2 S12-S23 · BOLUM_3 S24-S35 · BOLUM_4 S36-S47
MOTOR:         OMNI (gemini-omni-1.1-flash) I2V birincil · zincir ① tek başlangıç karesi · S37 için ② başlangıç+bitiş
               karesi ÖNERİSİ ⬜ (K2) · VEO yedek yalnız yüzlü sahnede ÇIKTI reddi gelirse · 360p okunabilirlik → 720p
               seçim → 4K büyütme · seed belgesiz
LOGLINE:       Fırtınadan önce gezegenden kalkması gereken astronot bir baba, ölen kızının görüntüsüne bürünmüş yaralı
               bir canlı bulur; onu yaşatmak için kızını ikinci kez bırakması gerekir.
PROMPT DİLİ:   İngilizce · "Scene n of 48" numarası = S + 1 (S0 → Scene 1) · dönüş işareti de bu numarayı kullanır
```

### 🧭 D74 KAYITLARI — bilinçli sapmalar ve sahip kararları (kaydı olmayan sapma yapılmamış sapmadır)

```
① REFERANS PAKETİ: sahip kararıyla YAZILMADI (17.09.2026). REFERANS_PAKETI §1 altı tetikleyiciden beşi doğru (T1 kask ·
   T2 kask geometrisi · T3 iniş aracı oranı · T4 canlı · T5 fırtına/kir merdiveni); dosya ⬜ BEKLİYOR, silinmez. Risk
   04_UYARI_NOTLARI R2'de; telafi Scene Foundation master kareleri + ilk onaylı varlık kırpımları (paket değil, KAPI 0 değil).
② BÖLÜM YAPISI 4 × 12 (sahip) — kart §2.7 "2 × 24" der. QA birimi ⬜ K1: (a) ⭐ öneri 4 çeyrek `--bolum n/4` ·
   (b) 2 yarım + ①.9 elle düşme (MARS_SON_CIKIS emsali) · (c) birleştirme.
③ REPLİKLER POST-DUB — iki Türkçe kayıt cümlesi, altı kullanım, klipte ÜRETİLMEZ (OMNI İngilizce · tırnak PROBu koşulmadı ·
   kayıttaki ses çocukluk oyununun sesi, ses denetim dalı riski · ses kimliği klipler arası kilitlenemez). SPEC
   `DIALOGUE LINES: 0` (klipte) + `POST-DUB LINES: 6`.
④ MUHATAP TİPİ — "HAYALİ/ÖLÜ yalnız terminal faz" kuralının dışı: görüntü halüsinasyon değil canlının kendisidir, konuşmaz;
   muhatap = kayıt cihazı + görüntünün yönü.
⑤ SON REPLİK DORUKTAN SONRA (S38) — oyunun ikinci yarısıdır, doruğun sonucu değil; final S41-S47 sessiz.
⑥ TEMA KİMLİK (FEDAKÂRLIK depoda 8 kez + logline takas kalıbına yakın).
⑦ İSKELET: dört ısı görüşü çiftinde (S9→S10 · S10→S11 · S13→S14 · S14→S15) azimut şartı MUAF — ısı görüşü adamın kendi
   bakışıdır, kadraj tam kare renk alanı; ölçek kademesi dört çiftte de tutuyor. Üç POV kurulumu (I · J · Y) onaylı
   hikâyenin üç satırıdır — POV süs değil kanıt kanalı.
⑧ MASTER ESTABLISHING S12 (B) — S1 ⭐VİRAL yüz planı; yönelimi S0 (A) + S2 (E) kurar; üretimde B master dış blokta İLK.
⑨ ATKI KURALI — figürün atkısı S0-S28'de; S30'da gerçek atkı canlıya geçer, S33'ten itibaren figür atkısız. Kadrajda aynı
   anda iki sarı atkı hiçbir sahnede yok (kopya nesne = klon arızası görünümü).
⑩ OKUMA KAPSAMI ve 48 SAHNE ÇALIŞMASI — sahip isteğiyle 14.09.2026 reform bütçesinin dışında (02 §0b-①②).
⑪ İNSANSIZ SAHNELER (S14 · S46 · S47): NEGATIVE çekirdeğin insan cümlesi "Human count in frame is zero" biçiminde, blok
   900 karakterin altında + tek pozitif `Style:` satırı (red defteri YR).
```

---

## 🎭 TEMA

```
TEMA: KİMLİK
      TANIM: Birini sevmek, başka birine onun yüzünü giydirmemektir.
      MOTİF SAHNELERİ: S9 · S15 · S28 · S30 · S37 · S39 · S47 (bedel S30 listede)
      motif kanalları: NESNE atkı (görüntünün boynunda → adamın cebinde → canlının üstünde) · KİNESİK "kendi eline yabancı
      gibi bakış" (S34 cihaz avuçta · S40 avuç atkıda) · IŞIK görüntü söndükçe canlının kendi ışığı belirir · PARÇALANMA
      S37 görüntünün kenardan incelmesi · ayna/yansıma motifi 0 (D25)
      tema-final: S39 gerçek canlı · S46-S47 kendi türünden ikinci ışık
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Yaralı yavru canlı, yakınındaki adamın içinde taşıdığı kızın görüntüsüne bürünür; görüntüyü tutmak
                     canlının kendi ışığını tüketir.
NOVUM TAŞIYICISI:    sarı atkı × adamın onu göğüs cebinde saklaması (S4 · S29) → atkı canlıya örtülünce ışık döner (S30-S31)
                     + kayıt cihazı × düğmeye basıp gözlerini kapatması (S36) → görüntü dağılır (S37)
TEK KARE (§4①):      S15 — kasksız, yarı saydam kadın figürü kumda diz çökmüş, sarı atkısı kumda yayılmış, omuzlarının içinden
                     kum tepesi görünüyor; dizlerinin dibinde ışığı geri çekilen küçük canlı → izleyici 1 sn'de işaret eder
                     (ikinci tek kare S33 · kanıt S11 ısı görüşü)
KİNETİK BAĞIMSIZLIK: ✅ S25 gövde siperi → ışık toparlanır · S30 atkı → ışık döner · S33 görüntü döner → ışık düşer ·
                     S36-S37 gözler kapanır → görüntü gider, ışık güçlenir (replik duyguyu taşır, kuralı değil)
BAŞLIK ŞEMASI:       "Close Your Eyes, Dad" (4 kelime — paketlemede ikinci kez koşar)
⛔ SINIR [D183]:     görüntü DIŞINDA her şey normal fizikle: gerçek atkı rüzgârda dalgalanır ve değdiği yere değer · kum
                     adamın botlarına çarpar · botları iz bırakır · görüntünün sesi yalnız kayıttaki İKİ cümle · kask
                     lambaları damara ışık vermez (S24) · S38'den sonra görüntü hiçbir karede yok
```

## 🧭 B5 — HİKÂYE OMURGASI (her formatta · `03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Numune kutusunu fırtına penceresi kapanmadan araca yetiştirip kalkmak (S1 kutuyu taşır · S6 pencere daralır ·
              S12 araca geri yürür)
   □ ENGEL:   Kızının görüntüsü onu düzlükte tutar; görüntünün altındaki yavru canlı yardımsız söner; fırtına pencereyi kapatır.
   □ BEDEL:   S30 kızından kalan son eşya (sarı atkı) canlının üstünde kalır · S37 kızının görüntüsü bir daha gelmemek üzere
              dağılır · S44 güvenli pencere kapandıktan sonra fırtınanın içinde kalkar (+ ön bedel S19: numune kutusu bırakılır)
   □ MUHATAP: kendi geçmiş kararı (kızını bir kez bırakmış olmak — atkı ve kayıt cihazıyla taşınır, anlatılmaz) + ortamın
              kalıcı değişen parçası (S31-S32 damar ağı yanar ve yanık kalır · S46-S47 yuvaya ikinci ışık)
   □ AYRILIK: S7 — adam araca çağırır, görüntü başını eğer ve kıpırdamaz · TERSİNMİŞ S33-S36 — görüntü yaklaşır, adam
              gözlerini kapatarak reddeder

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  referans paketi YOK → 0) K3 PROBU (S15 tek kare) + Scene Foundation (boş mağara master × L1-L4 · boş düzlük + araç master B)
  → 1) DORUK S37 → 2) merkezî seçim S36 → 3) kapanış imajı S47 → 4) S0 (2-3 varyant) → 5) S15 · S30 · S11 · S44
  → 6) bölüm blokları sondan başa B4 → B3 → B2 → B1
  ⛔ İPTAL KAPISI: S37 (tek figür, parçasız, kenardan içe okunmuyorsa ya da adamın yüzü kadınsı/klon) · S36 (göz kapağı
     + omuz düşüşü okunmuyorsa) · S15 (yarı saydam tek figür + içinden kum tepesi tutmuyorsa) → film ÜRETİLMEZ
```

## 👤 KARAKTER KARTI — davranış (kart PROMPTA GİRMEZ · `KARAKTER_KARTI_VE_DAVRANIS` §1)

```
👤 KEMİK BEYAZI GİYSİLİ ADAM (rol etiketi — özel ad yok)
ROL           yüzey numune toplayıcı — numune kutusu, bilek kayıt cihazı, beş lambalı bilek halkası · S1
İSTEK         kutuyu fırtına penceresi kapanmadan araca yetiştirip kalkmak · S1 · S6 · S12
BASKI TEPKİSİ KONTROL EDER · S3 bileğe bakar · S10 ısı görüşü · S24 lamba · S34 ışığa bakar
ALIŞKANLIK    "His right palm presses flat on the chest pocket flap twice." (her tekrarda BİREBİR) · S5 · S16 · S19
              (S19 tek ve kısa) → KIRILMA S29 (avuç kapağa kalkar, bastırmaz, parmaklar kapağı açar)
SINIR         gözlerini kapatmak — S8 oyunu reddeder · S36 çizgiye gelir
ZAAF          diz kiri S18'den · ön kol + omuz S41 · tırmanışta ikinci çekiş birinciden yavaş S41 · fırtınada adım kadansı S42
TEL           sol eldivenin parmakları sağ bilekteki lamba halkasını örter · S6 · S26 · S35
İLK ↔ SON     S1 elindekini (kutu) düşürür ↔ S45 elindekini (cihaz) yerine koyar ve eli üstünde bırakır

🫥 KADIN GÖRÜNTÜSÜ (figür kartı · ≥3 davranış satırında ayrışma)
İSTEK         sıcaklık ve siper (canlının isteği) · S15 doğrulma · S28 atkıya sarılma
BASKI TEPKİSİ GERİ ÇEKİLİR · S5 geri kayar · S17 eldivenden çekilir
ALIŞKANLIK    atkısının ucunu parmaklarına dolar · S0 · S3 · S7 → kırılma S28 (bütün atkıyı omzuna sarar)
TEMPO         hep adamdan ≥1 s SONRA kıpırdar (faz farkı)
YÜZ           hiçbir karede yok · ağız 0
İSTEK ÇAPRAZI adam → görüntüden: araca gelmesi (S7) · görüntü → adamdan: sıcaklık + "gözlerini kapat" (S2 · S36) · NESNE atkı
KİM SOLDA     adam SOL · görüntü SAĞ (film boyu) · TEMAS 0 (S17 eldiven avuç kala durur)

👁️ VARLIK KARTI (UZAYLI_VARLIK §6)
NİYET         EMPATİ (S10-S41 yavru) → HUŞU (S46-S47 büyük canlı) — sıralı, aynı karede değil
ÖLÇÜM         biyolüminesans kimyasal enerji harcar; birçok hayvan ışığı bakım/çağrı sinyali olarak kullanır
SPEKÜLASYON   bu tür yakınındaki bakıcının en güçlü hatırasını onun algısına kendi ışığı bedeliyle yansıtır; yuvası boş kalmış
              yavru çevredeki tek sıcak bedenin kızının görüntüsüne bürünerek siper arar; ışığı bitince görüntü de biter
REVEAL        K0 S0-S9 (etki) · K4-ısı S11 · K3/K2 ara · K4 S39-S40 (anatomi sayısı YALNIZ S11 · S39 · S40) · büyük canlı K2 S46 · K3 S47
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | sahne | boşsa gerekçe |
|---|---|---|---|---|
| 1 | Açılış imajı | %0 | S0 | — |
| 2 | Kurulum | %0-12 | S0-S5 (ROL + İSTEK S1 · sayaç S3 · taşıyıcı S4 · TOHUM S5) | — |
| 3 | Katalizör | %12,5 | S6 | ihlal S0'da ekranda |
| 4 | Tartışma | %15-25 | S7-S12 | — |
| 5 | 1. perde sonu · SEÇİM 1 | %27-40 | S13-S19 | — |
| 6 | Orta nokta — sahte zafer | %50-52 | S24-S25 | — |
| 7 | Bahis yükselir | %54-58 | S26-S27 | — |
| 8 | Umut-önce-düşüş | %65-69 | S31-S32 → S33 | — |
| 9 | Her şeyin kaybı · merkezî seçim · DUYGU DORUĞU | %75-77 | S36-S37 | — |
| 10 | Final · AKSİYON DORUĞU S44 | %79-96 | S38-S46 | — |
| 11 | Kapanış imajı (KAFİYE S0) | %98 | S47 | — |

```
İKİ DORUK:        DUYGU S36-S37 · AKSİYON S44 · kapanış bütçesi S45-S47 = 30 s = %6,25
FİNAL:            MUĞLAK + erken twist (S10-S11) · açık kalan TEK soru: kayıt cihazındaki ses bir daha çalınacak mı (S45)
PAYLAŞIM SAHNESİ: S32 (HUŞU — ışık bacaya tırmanır, adam dipte küçük)
⭐VİRAL:          S1 (YÜZ AU2 + kutu düşer) · S44 (YÜZ AU4 + kokpit sarsılır)
```

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       YANLIŞLIK KOMPOZİSYONU — normal kum düzlüğü + tek anormal öğe (fırtına önünde kasksız kadın) · yabancılık
                 şahidi aynı karede (sol ufukta fırtına duvarı + iniş aracı ≈1/15)
S0 SORUSU:       "Bu kadın bu havada kasksız nasıl duruyor — kim?"
S1 İKİNCİ BİLGİ: giysili adam onu tanıyor — kutu elinden kayar, bir adım geri
İLK 2 SN SESİ:   rüzgârın atkıyı çırpması, müzik yok
AÇILIŞ↔KAPANIŞ:  KAFİYE S0 ↔ S47 — aynı kamera cümlesi (A), atkı aynı koordinatta (sağ üçte bir); değişen tek değişken
                 atkının taşıyıcısı
BİLGİ ASİMETRİSİ: S0-S11 bilgi eşitliği → DRAMATİK İRONİ S33 (≈5:30, taşıyıcı ARKA PLAN: figür yürürken arkadaki ışık düşer)
                 → kapanış S34 (adam ışığa bakar)
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` (göz · tepki planı ·
> el · yürüyüş) ve `KURGU_RITMI §2` örüntü kırıcı — **ardışık iki sahne aynı
> ölçek + palet + ses dokusunda olamaz** (bu iskelette ardışık ölçek hiç aynı değil).
> Kamera sütunu: vuruş→açı `KAMERA_ACISI` · diziliş bandı `ACI_YAYI` §3 (47/47 bant içi —
> hesap `03_SAHNE_SIRALAMASI` §3) · kalıp `MESHUR_SAHNE` (K16 S19/S20 · K12 S42).
> Bütçe kısaltmaları: 👁️ göz · 🔁 tepki · ✋ el · 🚶 yürüyüş · 🎒 eşya.

| S | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | bütçe |
|---|---|---|---|---|---|
| S0 | Fırtına önünde kadın | Kasksız yarı saydam kadın figürü sırtı dönük durur, sarı atkısının ucu rüzgârda kalkıp iner; ufukta koyu fırtına duvarı, uzakta iniş aracı | A (ilk) · 35 · MS (medium long) · alt açı | Y1 — atkı çırpması | — |
| S1 | Kutu kayar | Numune kutusu taşıyan kasklı adam figürü görür; kutu eldivenlerinden kayıp kuma düşer, bir adım geri | C (ilk) · 50 · MCU · göz hizası | Y1 + kum sıçraması | 👁️ 🔁 🎒 |
| S2 | Tanıdık ses | Figürün yönünden kayıttaki ilk cümle gelir; adamın omuzları kalkar, ağırlığı arka bota geçer | E (ilk) · 35 · MS · OTS | Y1 + KAYIT | 🔁 |
| S3 | Kapalı cihaz | Adam sol bileğindeki yuvarlak kayıt cihazına bakar: tek düğme sönük; sağ bilekte beş lamba yanık | D (ilk) · 50 · CU · üst açı | Y1 + nefes | ✋ 🎒 |
| S4 | İkinci atkı | Göğüs cebinden aynı sarı yün atkının ucunu iki parmakla çeker; ucu kapağa takılır, çıkar | D (küme S3) · 50 · CU · üst açı | Y1 + yün hışırtısı | ✋ 🎒 |
| S5 | Kapanmayan mesafe | Adam figüre yürür, botları kuma gömülüp iz bırakır; figür adım atmadan aynı mesafede geri kayar; uzak çıkıntının dibinde kehribar nokta | E (dönüş S2) · 35 · MS · OTS | Y1 + bot adımları | 🚶 |
| S6 | Pencere daralır | Kask içinde uyarı sesi öter; sol eldivenin parmakları sağ bilekteki halkayı örter — beşten dördü yanık | C (ilk) · 50 · MCU · göz hizası | Y1 + UYARI | 👁️ 🔁 ✋ |
| S7 | Gelmez | Adam sağ kolunu araca doğru uzatır, el açık bekler; figür bir saniye sonra başını eğer, yerinden kıpırdamaz | E (dönüş S5) · 35 · MS · OTS | Y1 | — |
| S8 | Oyun bozulur | Adam cihazdan ilk cümleyi çalar, gözleri açık kalır; ikinci cümle beklemeden figürün yönünden gelir; başparmak düğmeden kalkar | C (dönüş S6) · 50 · MCU · göz hizası | Y1 + KAYIT ×2 | 👁️ |
| S9 | Gölgesiz | Rüzgârdaki kum taneleri figürün omzundan girip arkasından çıkar; adamın botlarının altında temas gölgesi var, figürünkünde yok | E (dönüş S7) · 35 · MS · OTS | Y1 + kum hışırtısı | 🔁 |
| S10 | Isı görüşü | Kaşındaki koyu lens açılır: renk alanında figürün ayak dibinde kuma yapışık küçük soğuk şekil; figür ısısız soluk bir hat | I (ilk) · ısı · WS · POV | Y1 boğuk + lens tık | — |
| S11 | Altı bacak | Isı görüntüsünde altı bacaklı küçük canlı nefes ritmiyle titrer; soluk figür hattı aynı ritimle öne eğilir | J (ilk) · ısı · MS · POV | Y1 boğuk + canlı hırıltısı | 🔁 |
| S12 | Kaçış denemesi | Adam araca doğru hızlı geri geri yürür, botu kuma gömülür, çeker; aynı cümle kesik kesik gelir, adımı yarıda kalır | B (ilk) · 24 · WS · göz hizası | Y1 + KAYIT kesik | 🚶 |
| S13 | Diz çöküş | Adamın kaskı figüre döner: figür topuklarının üstüne diz çökmüş, başı eğik, sarı atkısı kuma yayılmış | E (dönüş S9) · 35 · MS · OTS | Y1 | 🔁 |
| S14 | Işığın olmadığı yama | Isı görüşünde canlının sol böğründe soğuk koyu yama; kenarı her nefeste bir parmak ilerler | Y (ilk) · ısı · CU · POV | hırıltı + nefes | — |
| S15 | İçinden kum | Figür doğrulmaya çalışır; her deneyişte dizlerinin dibindeki canlının ışığı kuyruktan başa doğru geri çekilir | E (dönüş S13) · 35 · MS · OTS | Y1 + hırıltı | — |
| S16 | Döner | Kask araca, canlıya, yeniden araca döner — her dönüş daha yavaş; adam canlıya doğru yürür | B (dönüş S12) · 24 · WS · göz hizası | Y1 | 🚶 |
| S17 | Avuç kala | Adam bir dizini sonra ötekini kuma indirir, eldivenini uzatır; figür eğilir, avuç kala geri çekilir | E (dönüş S15) · 35 · MS · OTS | Y1 + diz kuma | 🔁 ✋ |
| S18 | Yarığa | Canlı altı kısa bacağıyla kumda yarığa ilerler; figür onu yarım adım geriden izler | B (dönüş S16) · 24 · WS · göz hizası | Y1 + kum | — |
| S19 | Kutu kalır | Adam numune kutusunu yarığın ağzına bırakır, kaş lambaları yanar, diz çöküp yarığa iner | E (dönüş S17) · 35 · MS · OTS | Y1 → Y2 çapraz | 🎒 |
| S20 | Damarlı duvar | Kaş lambaları kayada bir gövde boyu ileriyi aydınlatır: duvara kök gibi gömülü kehribar damarların çoğu sönük | L (ilk) · 24 · WS · göz hizası | Y2 + nefes | — |
| S21 | Boş kabuk | Damarların bittiği yerde büyük, boş bir yuva kabuğu; başka canlı yok | L (küme S20) · 24 · WS · göz hizası | Y2 | 🔁 |
| S22 | Tek nokta | Canlı bir bacağını sönük damara değdirir; bir kehribar nokta damar boyunca bir el ilerleyip geri döner | M (ilk) · 35 · MS · profil | Y2 + hırıltı | — |
| S23 | Bacadan fırtına | Tepedeki bacadan soğuk akım birkaç düzine kum tanesi indirir; canlının yamaları kısılır | Q (ilk) · 24 · WS · alt açı | Y2 + baca ıslığı | 🔁 |
| S24 | Lamba yetmez | Adam kaş lambalarını damara tutar, damar tepki vermez; canlının değdiği nokta hafifçe ısınır | M (dönüş S22) · 35 · MS · profil | Y2 | — |
| S25 | Siper | Adam lambaları söndürür, canlının baca tarafına oturur; gövdesi akımı keser, canlının yamaları toparlanır | L (dönüş S21) · 24 · WS · göz hizası | Y2 (ıslık kesilir) | — |
| S26 | Kalkamaz | Uyarı yeniden öter; sol eldiven halkayı örter — üç yanık; kalkmaya davranır, akım canlıya çarpar, geri oturur | M (dönüş S24) · 35 · MS · profil | Y2 + UYARI | 🔁 |
| S27 | Eller yetmez | Adam iki elini farklı derinlikte canlının üstüne siper yapar; kum taneleri parmak aralarından geçer, yamalar yine kısılır | S (ilk) · 50 · CU · göz hizası | Y2 + ıslık | ✋ |
| S28 | Üşüyen figür | Figür canlının sağında belirir, atkısını bütünüyle omzuna sarar; adamın kaskı kendi göğüs cebine iner | M (dönüş S26) · 35 · MS · profil | Y2 | 🔁 |
| S29 | Kırılma | Sağ avuç cebin kapağına kalkar, bastırmaz, kapağı açar; atkıyı kat kat açıp vizörün alt kenarına yaslar | S (dönüş S27) · 50 · CU · göz hizası | Y2 + nefes | ✋ 🎒 |
| S30 | Atkı | Adam atkıyı canlının üstüne rüzgâr tarafından örter; parmaklar tek tek açılır, el çekilir, avuçlar yukarı | M (dönüş S28) · 35 · MS · profil | Y2 (ıslık atkının kenarında) | ✋ 🎒 |
| S31 | İlk nokta | Atkının altında yamalar toparlanır; ışık bağlı damarın ilk noktasına geçer | L (ilk) · 24 · WS · göz hizası | Y2 | 🔁 |
| S32 | Tırmanan ışık | Işık noktadan noktaya duvar boyunca bacaya doğru tırmanır; adam duvarın dibinde küçük | Z (ilk) · 24 · EWS · alt açı | Y2 + tek alçak müzik tonu | — |
| S33 | Geri gelir | Figür yeniden belirip adama yürür; arka planda canlının yamaları düşer, adamın kaskı figürde | L (dönüş S31) · 24 · WS · göz hizası | Y2 | 🔁 |
| S34 | Işığa bakar | Kask figürden canlının ışığına döner; kayışı zaten açık cihazı bilekten avucuna alır | M (dönüş S30) · 35 · MS · profil | Y2 | 🔁 ✋ 🎒 |
| S35 | Parmak düğmede | Uyarı susmaz; sol eldiven halkayı örter — tek lamba; başparmak düğmenin üstüne gelir, yarım avuç kala durur | P (ilk) · 50 · MCU · göz hizası | Y2 + UYARI sürekli · müzik sonunda susar | 👁️ ✋ |
| S36 | Gözlerini kapatır | Adam ilk cümleyi çalar; göz kapakları iner, omuzlar bir avuç düşer ve inik kalır | X (ilk) · 35 · MS · göz hizası | Y2 + KAYIT · müzik yok | — |
| S37 | Dağılma | Gözleri kapalıyken figürün dış hattı kenardan içe incelir, arkasındaki kaya giderek belirir; canlının yamaları güçlenir | X (küme S36) · 35 · MS · göz hizası | Y2 + kask içi nefes (müziksiz ≠ sessiz) | — |
| S38 | Gözlerini açar | Adam ikinci cümleyi çalar ve gözlerini açar; bakışı atkının altındaki ışığa kilitlenir | P (dönüş S35) · 50 · MCU · göz hizası | KAYIT — ses smash cut | 👁️ 🔁 |
| S39 | Gerçek canlı | Atkının altında altı bacaklı, iki iri koyu gözlü canlı; yamaları sırt boyunca tam | M (ilk) · 35 · MS · profil | kısa sessizlik → Y2 | — |
| S40 | Üç zar | Canlı başındaki üç ince zarı adama açar; adamın avucu atkının kenarına basar, parmaklar bir an kapanır, açılır | N (ilk) · 50 · CU · göz hizası | tek alçak ötüş | ✋ |
| S41 | Bırakır, tırmanır | Eli atkının kenarından kalkar; kaş lambaları yeniden yanar; bacanın duvarına iki eldiven, bir bot | M (dönüş S39) · 35 · MS · profil | Y2 → Y3 çapraz | 🎒 |
| S42 | Fırtınaya karşı | Yüzeyde fırtına bastırmış; adam rüzgâra eğilip sağdan sola araca yürür, kum yere yakın yatay çizgilerle akar | T (ilk) · 24 · WS · üst açı | Y3 + kaska çarpan kum | 🔁 🚶 |
| S43 | Merdiven dibi | Merdivenin dibinde, bir eldiven en alt basamakta, kask geri döner: yarığın ağzının kenarına kehribar ışık ulaşır | U (ilk) · 50 · MS · OTS | Y3 | — |
| S44 | Fırtına içi kalkış | Kokpit sarsılır, camda karanlık zemin aşağı kayar; adam kolunu panele dayar, cihaz sol avucunda; bilek halkası karanlık | V (ilk) · 50 · MCU · profil | Y4 sarsıntı + gövdeye kum | 👁️ |
| S45 | Cep | Adam cihazı göğüs cebine, atkının boş kalan yerine iter; avucu kapağın üstünde düz kalır; bir yavaş nefes omuzları kaldırır | W (ilk) · 50 · ECU · üst açı | Y4 + tek nefes | ✋ 🎒 |
| S46 | İnen ışık | Yarıkta bacanın dibine büyük bir kehribar ışık iner; kaya kenarında iki uzun uzuv yavruya uzanır | F (ilk) · 50 · CU · alt açı | Y2 + müzik çözülmesi | — |
| S47 | İki ışık | İki kehribar ışık yan yana aynı yavaş ritimle nabız atar; aralarında sarı atkı, ucu akımda kalkar; bacadan soluk gün ışığı | A (kafiye S0) · 35 · MS (medium long) · alt açı | Y2 + atkı ucunun hışırtısı | 🎒 |

```
DAVRANIŞ ŞERİDİ (adam · G görev · T tereddüt · D deneme · K karar · B bedel · R tepki · S sükûnet · - yok):
  -RRGTDRDKR GRDRGTKRGB GRSRDKRDRT BRSRRTKBRS TKRTBK--
  G 5 ≤24 ✅ · K önce D/T ✅ · K sonra B/R ✅ · S 3 ✅ · ilk R ≠ son K ✅
TEMPO (Y/N/H):  NHYNYNHNYN HYHNYNYNNY NYYHNYHNYY NYYNNHYNYY NNHYHYNY
  değişim 40 · ardışık üç aynı 0 · CHOICE S36 Y (S35 H / S37 N) · COST S30 N → S31 Y
GÖRÜNTÜ ŞERİDİ (V kadrajda · h ısı hattı · - yok/dışarıda · D dağılıyor · Y yok oldu):
  V-V--V-V-V hhVV-VVVV- --------V- ---VV-VDYY YYYYYYYY   ⛔ S37'den sonra V yok
VARLIK ŞERİDİ (K0-K4): 0000000000 2402231311 1132333231 3313313314 43010023

AÇI TİPİ SAYISI: 6 ≥3 ✅ — alt açı (A F Q Z) · göz hizası (B C L N P S X) · üst açı (D T W) · OTS (E U) · profil (M V) ·
                 POV (I J Y) · alt açının öznesi adam DEĞİL (figür · büyük canlı · akım · ışık)
KURULUM SAYISI:  21 — tavan ⌈48/2⌉ = 24 ✅
KURULUM İSKELETİ: A C E D D E C E C E I J B E Y E B E B E L L M Q M L M S M S M L Z L M P X X P M N M T U V W F A
                 KÜME 3 (S3-S4 · S20-S21 · S36-S37) ≥2 ✅ · DÖNÜŞ 23/48 = %48 ≥%40 ✅ · şok 0
                 ⛔ Aynı harf AYNI kurulumdur ve kamera metni BİREBİR kopyalanır + işaret satırını taşır (ACI_YAYI §7 ⑥):
                     dönüş → "The same position, height and lens as Scene N."
                     küme  → "This clip continues the previous clip from its exact last frame — the same position,
                              height and lens as Scene N."
                   S0 ↔ S47 (A) dönüş DEĞİL (47 sahne) — KAFİYE: cümle birebir, işaret satırı yok
BÖLÜM KESİĞİ:    S11|S12 (J→B 130°) · S23|S24 (Q→M 60°) · S35|S36 (P→X 60°) — ⛔ bölüm sınırı da ardışık bir ÇİFTTİR
```

### ⚓ ÇAPA ÜÇLÜSÜ (`OYUNCULUK_YAZIM` §2 · aynı kanal · fark ≥⅛ kısa kenar)

| çapa | sahne | BEFORE (imaj t=0) | AFTER (sonraki imaj) | kanal | fark |
|---|---|---|---|---|---|
| CHOICE | S36 | başparmak düğmenin yarım avuç üstünde, kask figüre dönük, omuzlar kalkık | basmış, kask öne bir buçuk avuç, omuzlar bir avuç inik (S37 imajı) | omuz + el | ≈0,25 m ≥ 0,22 m (X 3 m) |
| COST | S30 | atkı iki elde gergin, canlının üstünde havada | eller boş, avuçlar yukarı, atkı canlıda (S31 imajı) | el | ≈0,3 m |
| FINAL | S45 | cihaz sol avuçta, başparmak düğmede | cihaz cepte, avuç kapakta düz (S46 kesmesi) | el | ECU'da kadrajın yarısı |

### 🧍🧍 AYRILIK KARTI · MESAFE EĞRİSİ · KARAR MİMARİSİ

```
AYRILIK S7: nesne araç yönü · hamle sağ kol uzanır, el açık bekler · cevap EYLEM × RET (baş eğilir) · gecikme ≥1,0 s ·
            mesafe 4 → 4 m · yön 0° → 90° · kim solda: adam · bedel S12
TERSİNMİŞ S33-S36: figür yaklaşır · adam gözlerini kapatarak reddeder · çözüm KARŞILIKLI DEĞİŞİM
MESAFE (m): S1 12 · S2 12 · S5 8→6 · S7 4 · S8 4 · S9 4 · S12 4→8 · S13 5 · S15 3 · S16 5→2 · S17 1,2 (→1,5) · S18 3 ·
            S28 1,8 · S33 4→1,8 · S34 1,8 · S36 1,0 · S37 0 · ardışık sahnede ≤1 bant atlama
KARAR:      S36 yaklaşan figür ↔ atkının altındaki canlı (reddedilen dağılır; atkı + baca ağzı sonra da orada) ·
            S30 atkı cepte ↔ canlıda (reddedilen cep boş kalır → S45) · DENEMELER S24 lamba → S27 eller → S33 atkı yetmez
KONUM KİLİDİ (her iki-figürlü promptta, İngilizce): "Exactly one human character in a pressure suit and one
            semi-transparent woman figure, and no third person. The suited man stays in the left third of the frame for the
            whole take; the woman figure stays in the right third. Neither crosses the centre line. They never touch; the
            closest they come is <n> metres."
```

---

## 🎙️ REPLİK TABLOSU (yalnız replikli filmde · `SES_VE_DIYALOG_URETIM` §1-§2a)

| # | S | saniye | konuşan | REGISTER | kanal | İŞLEV (B5 satırı / vuruş) |
|---|---|---|---|---|---|---|
| 1 | S2 | 0:22,0 | kayıt — görüntünün yönünden ("Baba, gözlerini kapat.") | M | kadraj dışı · bant-geçiren | MUHATAP · S1 sorusunu büyütür |
| 2 | S8a | 1:21,5 | bilek cihazı ("Baba, gözlerini kapat.") | M | kadrajdaki cihaz | ENGEL · oyunu adam başlatır |
| 3 | S8b | 1:23,3 | görüntünün yönü, BEKLEMEDEN ("Şimdi açabilirsin.") | M | kadraj dışı | ENGEL çevrilir |
| 4 | S12 | 2:03,0 | görüntünün yönü, kesik ("Baba… gözlerini… kapat.") | M | kadraj dışı | ENGEL · kaçışı keser |
| 5 | S36 | 6:03,0 | avuçtaki cihaz ("Baba, gözlerini kapat.") | M | kadrajdaki cihaz | BEDEL · merkezî seçimin tetiği |
| 6 | S38 | 6:22,0 | avuçtaki cihaz ("Şimdi açabilirsin.") | M | kadrajdaki cihaz | BEDEL tamamlanır |

```
SANİYE FORMÜLÜ [D122]: replik(S_n) = n × klip + TIMELINE ofseti (klip 10 s VARSAYIM · ffprobe sonrası yeniden)
İLK REPLİK:     S2 · 22,0 s · öncesindeki kesintisiz insan-sessizliği ≈22 s · vuruş: S1 sorusunu büyütme
BEDENLEŞTİRME:  ☑ yok — ses film boyu bedensiz, konuşan ağız 0 kare [§1a.1]
KLİPTE:         replik ÜRETİLMEZ (post-dub) · promptta tırnak 0 · Türkçe metin 0 · "Intended line" yalnız saniye + anlam etiketi
⛔ İŞLEV sütunu boş replik yok · sayı söyleyen replik 0 · duygu adı 0
KAPI: promptlar bitince PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md (Kart P 2b) — CUT/UNCLEAR varken üretime geçilmez
```

| S | hamle | cevap kanal × içerik | gecikme | dinleyenin bedeni | DEĞİŞİM |
|---|---|---|:--:|---|---|
| S2 | görüntü → adam: gözlerini kapatmasını ister | EYLEM × RET | 1,5 s | omuzlar kalkar, ağırlık arka bota | BİLGİ+ (bu onun sesi) |
| S8 | adam: oyunu başlatır, sınar | SÖZ × YANLIŞ (beklemeden) | ≤0,3 s (bilinçli ters) | başparmak kalkar, kask bir derece geri | BİLGİ+ (gerçek değil) |
| S12 | adam: gider | SÖZ × ERTELEME (kesik) | — | adımı yarıda kalır | MESAFE |
| S36 | adam: cümleyi kendisi çalar | EYLEM × UYMA | 1,5 s | omuzlar bir avuç düşer | NİYET |
| S38 | adam: ikinci cümle | EYLEM × UYMA | 0,5 s | bakış ışığa kilitlenir | GÜÇ |

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna
> yalnız o karenin `IN FRAME:` satırındaki kısmı gider — hands ise eldiven/bilek/
> kol, face ise yüz + kask, full body ise silüet + renk bandı (14.09.2026 · D214 ·
> `prompt_kontrol.py` ㉖). "BIBLE'a bak" atfı YASAK (kural ③), ama self-contained
> ≠ Bible'ın tamamı: kadrajda olmayan YAZILMAZ. Videoya Bible girmez — `START FRAME:`
> tek satır. Bu blok promptların kaynağıdır, kopyası değil.

### 👤 Character Bible
> kimlik: `ASTRONOT_DONANIM` §9 · görünüş: `UZAY_GIYSISI_SINEMATIK_TASARIM` §11 — arketip E BELGESEL (+ I'dan yalnız iki kare
> kaş lambası) · kask + kalın koyu çerçeve · sırt heykelsi pozitif · kir global F1-F3 · "glow / seamless / no …" yok

```
FACE (yalnız IN FRAME: face):
  a man in his late fifties with a broad square face, a heavy brow ridge over deep-set grey eyes, set lines across his
  forehead, short grey stubble along his jaw
VISOR (yalnız IN FRAME: face):
  The visor is optically clear glass with zero tint, his face fully readable through it. A soft warm fill from inside the
  lower rim of the helmet lights his face, weaker than any amber light in the scene.
HELMET (kask kadrajda olan her prompt):
  a hard off-white helmet shell with a single flat front pane set inside a thick dark-grey rim, seated deep into a raised
  brushed-steel collar ring, two small square lamps set into the brow above the pane and beside them one small dark round lens
FRONT PANE (yüz okunmayan ama kask görünen promptta, dosya başına ≥1): The helmet's front pane is optically clear with zero tint.
SUIT (full body · torso):
  a matte bone-white multilayer nylon surface suit, creased at the elbows and knees, one slate-blue band around the upper
  LEFT arm and one around the LEFT thigh, heavy segmented dark-grey gloves one piece with the sleeves, steel rings at the
  wrist seals, dark-grey boots
BACK (yalnız IN FRAME: back):
  The back of the suit is one continuous sculpted surface from collar to hip, low-profile, a flat back silhouette carrying nothing.
DIRT F1 (S0-S17): a light even dusting of dark grit on the suit
DIRT F2 (S18-S41): an even matte dusting of dark grit on the suit, heavier at the knees
DIRT F3 (S42-S45): the suit coated in dark grit from helmet to boots
WRIST ITEMS (hands):
  on his right wrist seal a steel ring set with five small amber lamps · on his left wrist seal a round palm-sized device
  with one large dark button and a small speaker grille, on a dark strap
  (lamba sayısı: 5 S0-S5 · 4 S6-S25 · 3 S26-S34 · 1 S35-S43 · 0 S44-S45)
POCKET · SCARF: a flat chest pocket with a flap · a long yellow wool scarf, thick knit, with short fringed ends
SAMPLE CASE: a boxy grey sample case with one top handle, about the size of a toolbox (S1-S19)
```

```
🫥 WOMAN FIGURE (yalnız görüntü kadrajdayken · yüz 0 · kimlik öznitelikleri ≤3 tek pencerede):
  exactly one semi-transparent woman figure in her late twenties, slim, about a head shorter than the man, long dark brown
  hair tied low at the nape, a dark navy wool sweater and dark trousers
  SCARF (S0-S28 yalnız): a yellow wool scarf at her neck
  TRANSPARENCY: she is lit by the same flat grey daylight as the sand; her hair and sweater keep ordinary colour and texture;
  the ground behind her shows through her shoulders at about half strength; her feet leave no prints; her face stays turned
  away from the lens
  CAVE: she is lit by the same amber light as the rock around her
  HEAT VIEW: a pale, colourless outline with no heat colour
```

```
🦭 CREATURE — ANATOMY LOCK (tam blok yalnız K4: S11 ısı silueti · S39 · S40):
  a low rounded creature about the length of a forearm, shaped like a seal pup, smooth leathery grey-brown hide, six short
  jointed legs, three on each side, bending forward at the mid-joint, one pair of large round near-black eyes, three thin
  translucent membranes folded flat along the top of its head, patches of amber light under the hide along its back; on
  its LEFT flank one dark cold patch the size of a palm where the light is absent
  SCALE ANCHOR: about the size of the sample case
K3 (sayısız): a low rounded creature the size of the sample case, smooth grey-brown hide, short legs tucked under it,
  patches of amber light under the hide along its back, a dark cold patch on its left flank
K2 (parça): its rounded back · one short leg · the lit patches · (S46) a much larger amber light and two long jointed limbs
  of the same grey-brown hide over the rock edge
⛔ S30'dan sonra sol böğürdeki koyu yama küçülür; S39'da ışıkla dolu. Aynalama yasak (yama hep SOL böğürde).
```

```
🛬 LANDER CARD (UZAMSAL §5.5 — film boyu sabit yer işareti, ekran SOLU):
  a squat four-legged lander about four body-lengths tall, matte grey plating, one square hatch he has to crouch through,
  angled camera-right toward the lens, two lamps beside the hatch, one cockpit window, a ladder down one leg with rungs a hand-span apart;
  its plating is rigid and matte, with no flag, no emblem and no marking on the hull
  ÖLÇEK MERDİVENİ (kare yüksekliği): S0 ≈1/15 · S12-S16 ≈1/10 · S42 ≈1/4 · S43 taşar (monotonik)
```

### 🌍 World Bible

```
YÜZEY (S0-S19 · S42-S43) — dış promptların İLK cümlesi BIOME:
  BIOME       a dark sand plain under a low, still cloud deck
  SKY         a dark slate-brown sky under the low cloud deck, one paler patch of cloud high on screen-left
  HORIZON     the horizon low in the frame, a long dark storm wall standing along it on screen-left behind the lander,
              a dark rock outcrop on screen-right
  GROUND      fist-sized dark stones half-sunk in dark sand, low wind ripples
  FAR         the middle distance softened by the thick air, the far outcrop a flat grey silhouette
  DIRECTION   wind and low streaks of sand move from screen-left to screen-right
  CHANGE      storm wall height changes ONLY at boundaries: S0 a low dark band · S6 a finger higher · S16 a hand higher ·
              S42 filling the lower third of the sky
  ABSENCE     (NEGATIVE havuzu) no vegetation, no water, no second lander
MAĞARA (S20-S41 · S46-S47):
  BIOME       a narrow crevice cave of dark rock, branching amber veins set into its walls like roots
  SHAFT       the shaft mouth a pale slot high on screen-left; the empty rounded nest shell against the far wall
  CHANGE      veins dark S20-S30 · lit and staying lit S31 → · a pale daylight patch on the floor S46-S47 only
KOKPİT (S44-S45): a cramped cockpit of grey panels, one window on screen-left, no readable display
⛔ Tetikleyici kelime 0: epic vista · alien landscape · otherworldly · dramatic sky · mist rolling · volumetric haze ·
   glowing crystals · light shafts
```

### 🎥 Camera Bible

> 21 kurulum. Cümle KARAKTER KARAKTER kopyalanır (sayı biçimi dahil). Her CAMERA cümlesi OMNI katmanıyla biter:
> "In a single continuous shot." Kamera kelimesi aksiyon satırına SIZMAZ; aksiyon satırında metre + kamera kelimesi
> aynı cümlede YOK (imzayı bozar). Mesafe cümlesinde "behind" yok ("back from").

```
A  CAMERA: 35mm lens on a fixed locked-off tripod, 0.5 m above the ground, 4 m from the subject, low angle medium long shot, deep focus, absolutely zero camera movement. In a single continuous shot.
B  CAMERA: 24mm lens on a fixed locked-off tripod, 1.4 m above the ground, 10 m from the man, eye-level wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
C  CAMERA: 50mm lens on a fixed locked-off tripod, 1.7 m above the ground, 1.4 m from his visor, eye-level medium close-up, absolutely zero camera movement. In a single continuous shot.
D  CAMERA: 50mm lens on a fixed locked-off tripod, 1.9 m above the ground, 1 m from his chest, high angle close-up, absolutely zero camera movement. In a single continuous shot.
E  CAMERA: 35mm lens on a fixed locked-off tripod, 1.6 m above the ground, 1 m back from his right shoulder, over-the-shoulder medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
I  CAMERA: point-of-view wide shot through the small heat lens in his helmet brow, 1.7 m above the ground, 6 m from the figure, absolutely zero camera movement. In a single continuous shot.
J  CAMERA: point-of-view medium shot through the small heat lens in his helmet brow, 1.7 m above the ground, 3 m from the figure, absolutely zero camera movement. In a single continuous shot.
Y  CAMERA: point-of-view close-up through the small heat lens in his helmet brow, 1.7 m above the ground, 1.2 m from the creature, absolutely zero camera movement. In a single continuous shot.
L  CAMERA: 24mm lens on a fixed locked-off tripod, 1.2 m above the ground, 4 m from the man, eye-level wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
M  CAMERA: 35mm lens on a fixed locked-off tripod, 0.6 m above the ground, 3 m from the man, side-on profile medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
Q  CAMERA: 24mm lens on a fixed locked-off tripod, 0.4 m above the ground, 4 m from the foot of the shaft, low angle wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
S  CAMERA: 50mm lens on a fixed locked-off tripod, 0.8 m above the ground, 1.2 m from his hands, eye-level close-up, absolutely zero camera movement. In a single continuous shot.
Z  CAMERA: 24mm lens on a fixed locked-off tripod, 0.3 m above the ground, 12 m from the mouth of the shaft, low angle extreme wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
P  CAMERA: 50mm lens on a fixed locked-off tripod, 1.1 m above the ground, 1.2 m from his visor, eye-level medium close-up, absolutely zero camera movement. In a single continuous shot.
X  CAMERA: 35mm lens on a fixed locked-off tripod, 0.7 m above the ground, 3 m from the man, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
N  CAMERA: 50mm lens on a fixed locked-off tripod, 0.3 m above the ground, 1 m from the creature, eye-level close-up, absolutely zero camera movement. In a single continuous shot.
T  CAMERA: 24mm lens on a fixed locked-off tripod, 5 m above the ground, 12 m from the man, high angle wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
U  CAMERA: 85mm lens on a fixed locked-off tripod, 1.5 m above the ground, 1 m back from his right shoulder, over-the-shoulder medium shot, absolutely zero camera movement. In a single continuous shot.
V  CAMERA: 50mm lens on a fixed locked-off tripod, 1.3 m above the cockpit floor, 1 m from his visor, side-on profile medium close-up, absolutely zero camera movement. In a single continuous shot.
W  CAMERA: 50mm lens on a fixed locked-off tripod, 1.6 m above the cockpit floor, 0.4 m from the chest pocket, high angle extreme close-up, absolutely zero camera movement. In a single continuous shot.
F  CAMERA: 50mm lens on a fixed locked-off tripod, 0.3 m above the ground, 2 m from the foot of the shaft, low angle close-up, absolutely zero camera movement. In a single continuous shot.
```

### 💡 Lighting Bible

```
KAYNAK      yüzey: thick cloud deck, diffuse daylight with one brighter patch · mağara: amber light from the creature's lit
            patches and the lit veins (same light family) + his two brow lamps (S19-S24 · S41) · kokpit: cool panel light
YÖN         yüzey: the brighter patch sits high on screen-left · mağara: the source sits low at screen-right, lighting faces
            from below right · kokpit: panel light from screen-left
TAKVİM      yüzey MONOTONİK kararır: S0 · S6 · S12 · S16 · S19 birer kademe → S42-S43 en koyu · mağara EĞRİ (SPEC'te eğri
            ilan edilir): L1 brow lamps on, veins dark (S20-S24) · L2 brow lamps off, only the creature's low patches
            (S25-S30) · L3 veins lit and staying lit, creature patches varying (S31-S41) · L4 L3 + one soft patch of pale
            daylight from the shaft (S46-S47) · seviye değişimi YALNIZ SINIRDA, klip içinde yalnız ilerleyen ışık kenarı
RENK BANDI  yüzey neutral cool grey · mağara amber-yellow, never red · kokpit cool cyan
PRATİKLER   two square brow lamps · five amber wrist lamps (5→4→3→1→0 at cuts) · the lander's two hatch lamps
KONTRAST    yüzey "the shadow side holds soft detail" · mağara "beyond the reach of the amber light the rock falls to deep black"
⛔ LIGHT satırı yüzeye RENK atamaz (renk World'ün işi) · volumetric · god rays · light shafts · glow · rim light 0 ·
   kalın atmosferde uzun gölge YOK: "a soft dark contact shadow pools under his boots"
```

### ⚙️ Physics Bible

```
ATMOSFER    ≈3 atm (SPEC) — promptta "thick air": sound travels strong and low, wind is slow but heavy and pushes, wool swings
            slowly and heavily, nobody is blown off their feet
YERÇEKİMİ   ≈0,7 g (SPEC) — promptta "about two thirds of Earth's weight" · a case dropped from chest height reaches the sand in
            about half a second
KUM         travels in low streaks near the ground, settles within two to three seconds, never hangs in the air · from the shaft
            a few dozen grains at a time
NOVUM       yalnız görüntü: sand passes through her · no prints · no contact shadow · everything else normal physics
KOKPİT      the cockpit shakes; loose things stay put in his grip; through the window the dark ground slides down (takeoff as motion)
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 TAM LİSTE + bu filmin ortam/tür/risk yasakları
> Havuz burada durur, prompta girmez: prompt §5.1 çekirdek (8 cümle) + bu listeden
> sahne başına ≤3 cümle taşır (㉗ · 14.09.2026).

```
§5.3 TAM LİSTE (prompta girmez):
Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera
teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and
fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure
throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt
and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — not on the suit, not on the equipment, and not on the ground, the rock, the ice or any natural
surface in the frame. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no
watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers,
rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering,
never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping
topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm
film grain.

ÇEKİRDEK ② BU FİLMDE (insan sayısı cümlesinin üç hâli):
  adam tek:        Exactly one human character, no duplicates, no second person.
  adam + figür:    Exactly one human character in a pressure suit, no duplicates of him, and one semi-transparent woman figure, no third person.
  insansız:        Human count in frame is zero, and the rock, the sand and the amber light are the whole subject.

SAHNE HAVUZU (sahne başına ≤3):
  N1 deri (adam yakın plan):   No bare skin on the suited man, none above the collar, none at the wrist, none at the ankle.
  N2 figür ışığı:              No light rays, no halo and no haze around the woman figure.
  N3 figür yüzü:               Her face never turns toward the lens.
  N4 iki atkı (S33-S37):       Only one yellow scarf in the frame.
  N5 ısı görüşü:               No interface graphics, no overlay lines, no crosshair and no numbers in the heat view.
  N6 araç:                     No tilt-shift look, no miniature read on the lander.
  N7 diyalog:                  No transcript of the line, no invented on-screen speaker.
  N8 canlı biçimi:             The creature keeps the same number of legs and the same smooth hide throughout, no extra limbs.
  N9 dağılma (S37):            No fragments leave her outline.
  N10 kokpit:                  No readable display, no warning lights flashing red.
  STYLE (insansız · YR):       Style: natural rock texture, photographic, still air, no stylisation.
⛔ Politika sözlüğü NEGATIVE'de de 0: wound · injured · dying · dead · ghost · grave · blood · web · spider (D123)
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

> Tarif değil SAYI. `02_RISK_KARTLARI.md`'nin bu filmde tetiklenen her kartı
> buraya bir SAYI bırakır. 5+ risk çıkıyorsa kilit tavanı (aşağıda), malzeme değil.

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| giysili adam | tam 1 | K4 ikinci figür | 45 sahne |
| kadın figürü | ≤1 · saydamlık yarım · yüz 0 kare | K4 · 1 no. risk | V şeridi · S37'den sonra 0 |
| adam ↔ figür en yakın mesafe | 1,0 m (S36) · temas 0 | K4 | mesafe eğrisi |
| kask | kapalı 48/48 · açık 0 · 2 kaş lambası · 1 ısı lensi | K3 | adamlı tüm sahneler |
| bilek lambaları | 5 → 4 (S6) → 3 (S26) → 1 (S35) → 0 (S44) | K5 sayaç | kesmede düşer |
| canlı anatomisi | 6 bacak · 2 göz · 3 zar · 1 sol böğür yaması | K2 | sayı yalnız S11 · S39 · S40 |
| sarı atkı | kadrajda ≤1 (S33-S37 dahil) · final ×1 | K4 kopya nesne | S0-S47 |
| kehribar ışık (final) | ×2 | FİNAL VURUŞ KANITI | S47 |
| kum çökme süresi | 2-3 s | K6 parçacık | dış sahneler · S23 |
| kutunun düşüş süresi | ≈0,5 s | K13 · fizik | S1 |
| iniş aracı | 4 bacak · 1 kapak · 2 lamba · 1 cam · kare boyu 1/15 → 1/10 → 1/4 | K13 yapı ölçeği | S0 · S12 · S16 · S42-S43 |
| kir kademesi | F1 → F2 (S18) → F3 (S42) | ekipman | geri dönüş 0 |
| S37 dağılma süresi | ≈8 s · son ≥1 s yalnız kaya | 1 no. risk + K2 zincir | S37 |
| ışık durumu (mağara) | L1 S20-S24 · L2 S25-S30 · L3 S31-S41 · L4 S46-S47 | K6b katmanlı dünya | mağara bloğu |
| replik | 6 kullanım · klipte 0 · ağız 0 | K7 diyalog | S2 · S8 ×2 · S12 · S36 · S38 |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — `prompt_kontrol.py` ㉕ KİLİT TAVANI)

> 14.09.2026: yaşayan listeden (`00_YASAYAN_DERSLER.md`) bu filme düşenler. Tavan 20;
> aşan kilit aşağıdaki bloğa iner. Sayı elle değişmez (sabit betikte).
> ⚠️ Satır başına TEK ders numarası — ㉕ bu bölümde farklı D-numarası sayar; kilit metnine başka numara yazılmaz.

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D20 | İki figürlü her promptta sayı ayrı cümleyle: "Exactly one human character in a pressure suit, no duplicates of him, and one semi-transparent woman figure, no third person." Figürsüz mağara sahnesinde boş alan pozitif ("the rock around him is bare"). Biniş kadrajda yok. | V şeridindeki 15 sahne · mağara S20-S41 · S43-S44 |
| D16 | Adamın yüzü yalnız IN FRAME: face promptunda, tek cümle (FACE bloğu, stubble çapasıyla). Kadın figürü ile adamın yüzü aynı kadrajda hiçbir sahnede yok (yüz kurulumları C · P · V figürsüz). | S1 · S6 · S8 · S29 · S35 · S38 · S44 |
| D146 | Kask cümlesi film boyu birebir (HELMET bloğu: kalın koyu çerçeve, düz ön cam, derin yaka halkası, iki kare kaş lambası). Paket yok → ilk onaylı S36 kask kırpımı sonraki imajlara görsel girdi. | adamlı tüm sahneler · en kritik S35-S38 · S44 |
| D157 | TEK KARE S15: yarı saydam figür, kumda yayılmış sarı atkı ve ışığı geri çekilen canlı AYNI karede, ayrı bölgelerde; aynı kural S33'te ikinci kez. | S15 · S33 (kanıt S11) |
| D179 | İmaj t=0 = ÖNCE hâli: S13 figür zaten diz çökmüş · S30 atkı elde havada · S34 kayış açık, cihaz bilekte · S36 başparmak düğmenin önünde · S37 figür hâlâ var · S45 cihaz avuçta. | S13 · S30 · S34 · S36 · S37 · S45 |
| D213 | Temas, değişim ve sonuç aynı klipte ve kadrajda; sonuç ≥1 s ekranda kalır (kutu kumda · atkı canlıda, eller boş · cihaz avuçta · basış ve omuzların inişi). | S1 · S19 · S30 · S34 · S36 |
| D203 | Altı kayıt kullanımı klipte ÜRETİLMEZ, post-dub; promptta tırnak ve Türkçe metin yok; AUDIO satırı düğme tıkı + nefes; SPEC DIALOGUE LINES 0 + POST-DUB LINES 6. | S2 · S8 · S12 · S36 · S38 |
| D35 | Konuşan ağız 0 kare: replik anlarında figürün yüzü kadraj dışında ya da başı eğik; dinleyenin bedeni ses bitmeden tepki verir. | S2 · S8 · S12 · S36 · S38 |
| D193 | İki ışık takvimi sayıyla: yüzey MONOTONİK kararır (S0 → S19 → S42) · mağara EĞRİ (L1-L4), seviye değişimi yalnız sınırda, klip içinde yalnız ilerleyen ışık kenarı; SPEC'te eğri ilan edilir. | S0-S19 · S20-S47 · S42-S43 |
| D50 | Kalkış penceresi metinsiz: sağ bilekte beş kehribar lamba 5 → 4 (S6) → 3 (S26) → 1 (S35) → 0 (S44); sönme kesmede; kayıt cihazı ekransız. | S3 · S6 · S26 · S35 · S44 |
| D56 | Ağ + altı bacak kümesi kurulmaz: damarlar "branching amber veins set into the rock like roots", canlı "shaped like a seal pup"; web/net/spider/insect kelimesi 0. | S11 · S20-S47 canlı ve damar sahneleri |
| D67 | Saydam kadın hayalet kümesine düşmez: "lit by the same flat grey daylight as the sand; her hair and sweater keep ordinary colour and texture"; ghost/spirit/ethereal 0. | V şeridi · S0 · S15 · S37 |
| D29 | Parlama sözlüğü 0 (glowing/luminescent/radiant/shimmering): kehribar ışık KAYNAK + ULAŞTIĞI YÜZEY ile, aydınlanan kaya dokusunu korur. | S10-S47 canlı/damar · S43 · S46-S47 |
| D89 | Çıkarma sahnelerinde tek mühür sayımı: "exactly one thing leaves his suit in this shot: the scarf from the chest pocket; both gloves stay on, the helmet stays sealed at the collar"; S34 kayış açık başlar. | S4 · S29 · S34 |
| D168 | Üretim sırası dramatik sıra değildir: K3 probu + Scene Foundation → S37 → S36 → S47 → S0 → S15 · S30 · S11 · S44 → bölüm blokları sondan başa; ilk KABUL S37 değilse ikinci klip üretilmez. | URETIM_DEFTERI · tüm film |
| D202 | ÇAPA ÜÇLÜSÜ önce/sonra aynı kanalda: SEÇİM S36 omuz + el · BEDEL S30 eller dolu → boş · FİNAL S45 cihaz avuçta → cepte; fark ≥⅛ kısa kenar. | S30 · S36 · S45 · QA_SPEC |
| D210 | S0 ↔ S47 aynı kurulum harfi (A) ve karakter karakter aynı CAMERA cümlesi; sarı atkı iki karede de sağ üçte birde; her CAMERA "absolutely zero camera movement … In a single continuous shot." | S0 · S47 · tüm CAMERA satırları |
| D209 | Dünya çapası her dış promptta: ilk cümle "a dark sand plain under a low, still cloud deck"; iniş aracı ve fırtına duvarı ekran solunda, kaya çıkıntısı sağında; rüzgâr soldan sağa. | S0-S19 · S42-S43 |
| D123 | Yara/ölüm/hayalet sözlüğü NEGATIVE dahil 0: "a dark cold patch where its amber light is absent" · "she kneels low, sitting back on her heels" · "her outline thins from the edges inward". | S11 · S13-S15 · S23 · S27 · S30 · S37 |
| D180 | S37 sessizliği KURGUDA: müzik S35 sonunda (360 s) biter, S36-S37 müziksiz, yatak + kask içi nefes −35/−40 dB kalır, dijital sıfır yok; video AUDIO boş istenmez; MUZIK dosyasında saniyeli satır. | S36 · S37 · MUZIK |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle (boşsa "—")

| ders | neden bu filmde ayrı prompt kilidi olarak uygulanmadı · içeriği nerede |
|---|---|
| D69 · D140 | klon sıcak noktaları (loş iç mekân · klip başı 0,6 s) — içerik #1'e katlandı; klip başı taraması kurgu kapısında |
| D82 | ses kaynağı kilidi — #8'e katlandı |
| D95 · D79 | berrak vizör "kask yok" okunur · sırt pozitif — Character Bible + §5.2 ekleri (her promptta değil, IN FRAME'e göre) |
| D175 | çıplak deri negatifi kadın figürüyle çelişir → negatif "on the suited man" öznesine bağlı; Negative Bible satırı |
| D42 · D147 | kir 3 kademe global, sınırda artar — sahne tablosu "kir" sütunu + SPEC C KİMLİK DİZİSİ |
| D207 · D169 · D206 | yorgunluk 0-6 · efor gövde tepkisi · bedel bedende — sahne tablosu "yorgunluk/efor" sütunu, TIMELINE satırı |
| D59 | still/frozen/holds tek başına yazılmaz — prompt_kontrol ⑧ zaten sayar; SAHNE_DOLULUGU §4 ⑥ |
| D76 | yokluk novumu (gölge yok) → S9 birincil kanıt pozitif olay (kum içinden geçer) — sahne çalışması S9 |
| D88 | sınırlı izin tam izin — saydamlık "at half strength" karşılaştırmalı cümle #12'ye katlandı |
| D128 | metaforun fiziği — S37 "like breath fading from cold glass" (toz metaforu yok), sahne çalışması S37 |
| D43 · D28 | temasla değişim eritir · biyolüminesan temas — geometri sabit, yalnız ışık kenarı hareket eder; adam canlıya dokunmaz (#6 ve SPEC SIFIR KİLİDİ Z7) |
| D90 | milimetrik olay — S22/S24 düğüm ışığı "bir avuç" ulaşım mesafesiyle; sahne tablosu |
| D127 | ivme yerine süre — S1 kutu düşüşü süreyle; sahne çalışması S1 |
| D143 · D39 | toz şelalesi / swirl — S23 bacadan kum "a few dozen grains at a time"; sahne çalışması S23 |
| D154 | tekrar eden doğa olayı VARLIK — fırtına tek sayılı cümle + takvim; World Bible CHANGE satırı |
| D192 | 1 no. risk sayıyla — saydamlık "half strength" + S37 süre cümlesi; SPEC F göz kapısı |
| D200 | tek kadrajda iki yerçekimi — ihlal yalnız görüntüye ait; Physics Bible tek g |
| D141 | FİNAL VURUŞ KANITI S47 (atkı ×1 · kehribar ışık ×2) — SPEC B satırı (prompt kilidi değil) |
| D211 · D212 | ilk 10 s soru / ardışık aynı vuruş — 03_SAHNE_SIRALAMASI vuruş tablosu |
| D138 · D155 | ölçü yüzeye yazılmaz · kapital kısaltma yok — prompt_kontrol ㉑ zaten sayar |
| D167 | kimlik ≤3 öznitelik — #2'nin yüz cümlesi bu sınıra göre yazıldı |
| D174 · D86 | yön nesneyle · kim solda — SPATIAL MAP + KONUM KİLİDİ (IKI_KISI §6) sahne tablosunda |
| D214 · D215 | IN FRAME · araç ayarı — V3 iskeletinin kendisi / üretim defteri üç kutu |
| D216 · D217 · D83 | ses miksi · replik görüneni söylemez · yatak — MUZIK + SPEC; replikler zaten görünmeyeni taşır |
| D122 · D124 · D135 · D204 | saniyeler hesaplatılır · klip süresi ffprobe · iki şerit · SPEC 7 çapa — PLAN künyesi + QA_SPEC |
| D158 · D172 · D176 · D208 | seçim sonrası seçimler · sarkan taşıyıcı yok · zemin tek cümle · kimlik dizisi — sıralama + SPEC |
| D198 · D201 | etiket filme uymuyor (sıfır-g · vakum) — "—" |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

> Maliyeti sıfır, iki satır. Bunu yazan tek film redleri önceden gören
> tek film oldu (YERCEKIMI). Kural: `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`

```
EN RED-RİSKLİ KARE:  S13
NÖTR TARİFİ:         A semi-transparent woman figure in her late twenties kneels low on the dark sand, sitting back on her
                     heels, head bowed toward her knees, her yellow scarf lying spread on the sand beside her; the dune crest
                     behind her shows through her shoulders.
İKİNCİ:              S34 — kayış klip başında açık, cihaz bilekte gevşek; yan açı (M), tek bilek, göğüs ve kask kadrajda
ÜÇÜNCÜ:              S27 — eller siper: göz hizası ¾ yakın plan (S), eller farklı derinlikte, kollar omza doğru kadraj dışına
DÖRDÜNCÜ:            S30 — bedenin üstüne örtü imzası: canlının başı ve gözleri açıkta, nefesi yünü kaldırır
⛔ "riskli sahne yok" geçerli DEĞİLDİR — en riskli kare her filmde vardır.
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| S13 yere yığılma → diz çöküş | çöküşün sertliği | malzeme sonucu: atkı kumda yayılmış · temassız gövde tepkisi: adamın adımı yarıda kalır |
| S34 kayışı klipte çözme → kayış açık başlar | çözme jestinin zorluğu | alet tepkisi: cihaz avuca iner, başparmak düğmeyi bulur (S35) |
| replik klipte → post | dudak/ses senkronunun canlılığı | temassız gövde tepkisi: dinleyenin omzu/bakışı replik bitmeden (S2 · S8 · S36 · S38) |
| "yara" sözcüğü → ışığın olmadığı yama | yaranın somutluğu | malzeme sonucu: koyu yamanın kenarı her nefeste bir parmak ilerler (S14) |
| S29 atkı kask camına → vizörün alt kenarına | yüzün atkıyla örtülmesi | temassız gövde tepkisi: omuzlar bir kez kalkıp iner |
| S30 örtü → baş ve gözler açıkta | örtünün "sarma" yoğunluğu | malzeme sonucu: canlının nefesi yünü kaldırıp indirir |
| S37 "toz gibi" → kenardan incelme | ufalanmanın dramatikliği | kütle-hız: arkadaki kaya giderek belirir, ışık aynı anda güçlenir |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.
   Dört kanal: kütle-hız · malzeme sonucu · alet tepkisi · temassız gövde tepkisi
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez. father · daughter · dad · ghost prompt gövdesinde 0.
```

---

## 🧭 SPATIAL MAP — plana, prompta girmez (`UZAMSAL_HARITA_VE_EKRAN_YONU` §3 · §8)

```
YÜZEY   AKSİYON EKSENİ iniş aracı (ekran SOLU) ↔ kaya çıkıntısı / yarık (ekran SAĞI) · kamera film boyu eksenin aynı yanında ·
        adam hep solda, figür hep sağda · rüzgâr ve kum çizgileri soldan sağa · parlak bulut lekesi sol üst ·
        fırtına duvarı sol ufukta aracın arkasında
YÖN     S1 adamın kaskı sağa (figüre) · S5 adam sağa yürür, figür sağa kayar · S7 sağ kol sola (araca) uzanır ·
        S12 adam SOLA geri geri yürür, yüzü sağa ("walks backward toward screen-left while facing screen-right") ·
        S16 kask sol-sağ-sol, sağa yürür (araç lambaları sırtında) · S18 ışık sağa · S42 adam sağdan SOLA yürür, lambalara ·
        S43 araçta, kask sağa (yarığa) döner
MAĞARA  baca ağzı sol üst (soğuk akım soldan-yukarıdan) · canlı + atkı sağ alt · adam arada, bacanın tarafında (S25 siper) ·
        figür canlının sağında (S28 · S33 · S36) · boş yuva kabuğu uzak duvarda
KOKPİT  cam ekran solu · adam profil sola bakar · panel ışığı soldan
MASTER  dış: B (S12) · mağara: L (S20) — üretimde her mekân bloğunun İLK karesi
⛔ Aynalama YASAK: canlının SOL böğür yaması asimetrik işaret; yatay çevirme ile kurtarma yok.
```

---

## ✅ KAPI KAYDI

```
☑ künye + D74 kayıtları (11) · ☑ TEMA + 7 motif sahnesi · ☑ NOVUM + taşıyıcı + TEK KARE (atkı adıyla) + sınır
☑ B5 + AYRILIK + üretim sırası + iptal kapısı · ☑ karakter kartı + figür kartı + varlık kartı
☑ vuruş tablosu + hook · ☑ sahne haritası 48 satır + şeritler + KURULUM İSKELETİ (KÜME 3 · DÖNÜŞ %48 · 21 kurulum)
☑ çapa üçlüsü · ayrılık kartı · mesafe eğrisi · karar mimarisi · ☑ replik + değiş-tokuş tabloları
☑ Bible'lar (karakter · figür · canlı · araç · dünya · kamera 21 cümle · ışık · fizik · negatif havuz)
☑ sayısal kilitler · ☑ ders kilitleri ≤20 + uygulanmayanlar · ☑ politika satırı + telafi tablosu · ☑ spatial map
☑ prompt_kontrol klasör modu ✅ GO (17.09.2026 · 96 prompt + 3 yedek · 21 kurulum · KÜME 3 · DÖNÜŞ 23/48 · açı tipi 6)
⬜ DIALOGUE_CRITIQUE (Kart P 2b) — dış modelde koşulmadı; promptlarda tırnaklı replik yok (post-dub) → girdi paketi:
   bu dosyanın B5 bloğu + REPLİK TABLOSU + DEĞİŞ-TOKUŞ TABLOSU (rubrik aksi hâlde "NO DIALOGUE FOUND" der)
⬜ SAHİP: K1 QA birimi · K2 S37 zincir modu · K3 figür probu (üretim günü 1) · klip süresi ffprobe
```
