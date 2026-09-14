# 🎬 THE KEPT LIGHT — PLAN

> _"Burada hiçbir şey geçmişe geçmez; bıraktığın her şey bugünde kalır ve birikir."_
> **Bu dosyada PROMPT YOKTUR.** `### 📸 IMAGE PROMPT` / `### 🎥 VIDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarındadır.

```
FORMAT:        yatay 3-5 dk (16:9)              [KILAVUZ_REHBERI §2.3]
ORTAM:         §3.1 VAKUM  +  §3.5 alt kartı (ASILI/STATİK YERÇEKİMİ)
               Üs, bir kayanın ALT yüzüne asılı ve kayanın uzak yüzündeki
               motorlar onu kara deliğin üstünde SABİT tutuyor. Statik
               gövde tam yerel ağırlığı hisseder: 0,40 g.
               §3.1'in satırları aynen geçerli (toz 0 · gölge mutlak siyah ·
               dolgu YOK · ses yalnız gövdeden · rüzgâr 0 · egzoz 0 kare —
               motorlar kayanın ÖTE yüzünde, hiçbir karede kadrajda değil).
               ⛔ §3.10 (basınçlı iç hacim) TETİKLENMEZ: bu üssün içi de
                 vakumdur, kask 25/25 kapalıdır, hava taşıyan ses yoktur.
TÜR:           bilimkurgu   (tek açık dal — §4.1)
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124] — plan 10,0 s varsayar:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
SAHNE SAYISI:  25            RUNTIME: 249 s = 4:09 = 9 s hook + 24 × 10 s
               ⚠️ DEPODA ÇELİŞKİ VAR ve bu film §2.3'ü izliyor:
               KILAVUZ_REHBERI §2.3 kartı **25 sahne / 4:09** der,
               `yatay_4_dk_filmler/README.md` **24 sahne / 2×12** der.
               Kart A §2.3'e işaret ettiği için bu film 13 + 12 yazar.
               ⛔ Çelişki depoda duruyor; düzeltilene kadar her film
                 hangisini izlediğini YAZAR.
LOGLINE:       Bir kara deliğin üstünde asılı duran bir üste, kapağın altına
               bırakılan hiçbir şey düşmesini bitirmez; ölü bir modülü kesip
               atmakla görevli bekçi, son kelepçenin aynı zamanda aşağıdaki
               tek ışığı tuttuğunu anlayınca onu yine de keser — ve karanlıkta
               kalan alana kendi lambasını bırakır.
```

---

## 🎭 TEMA

```
TEMA: ZAMAN      (TEMA_MUHENDISLIGI §3 · yatay SÜREÇ teması §4)
      — "Burada hiçbir şey geçmişe geçmez; bıraktığın her şey bugünde
        kalır ve birikir."

MOTİF SAHNELERİ: S1 · S10 · S15 · S19 · S21 · S24
      S1  NESNE      — kapağın altındaki asılı alan: yakınlar küçük ve yeni,
                       derinler büyük ve sönük; derinlik = geçen yıl (birikim)
      S10 KAMERA+IŞIK — dışarıdan: kayanın altında tek aydınlık ağız, altında
                       hiç bitmemiş bir sütun (birikim + ölçek kontrastı 1:10)
      S15 NESNE      — makro: pimin başı yıllarca sürtünmekten yuvarlanmış,
                       hattın halkası o başın altında kalmış (aşınma)
      S19 KİNESİK    — ⭐ MERKEZÎ SEÇİM: kesiciyi kapatan avuç (bedelin anı)
      S21 IŞIK       — ⭐ BEDEL GÖRÜLÜR: lamba çok aşağıda, konisi öteye
                       bakıyor; arada asılı olan hiçbir şey aydınlanmıyor
      S24 NESNE+IŞIK — yeni lamba düşerken alan yeniden görünür; ALTI
                       sayılabilir parlak nesne

⛔ Takas kalıbı DEĞİL [§3c moratoryumu]: cümlede "X olabilmesi için Y feda
   edilir" sözdizimi yok — cümle bir TANIM cümlesidir (bu yerde zaman nedir).
   Bedel filmde vardır ve B5'te sahne numarasıyla kayıtlıdır.
⛔ Etiket TEK KELİME ve sayac.sh beyaz listesinde: ZAMAN.
⚠️ DÜRÜST KAYIT — ETİKET TEKRARI: bu formatta ZAMAN'ı 02.09.2026'da
   THE SINKING STAKE de kullandı ve o film de bir kara deliğin yanında
   geçiyor. Etiket aynı, CÜMLE ZIT: orada "hiçbir iz kendi başına kalmaz",
   burada "bırakılan her şey kalır". İki film aynı temanın iki ucudur ve
   bu bilinçlidir. Alternatif FEDAKÂRLIK bir film önce (THE UPWARD FALL,
   04.09) kullanıldığı için seçilmedi; YALNIZLIK ve ENTROPİ §4'e göre
   DİKEY (anlık durum) temalarıdır ve yatayda "uzatılmış içerik" cezası alır.
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ:          FİZİKSEL YASA  (§1 birinci tercih)
NOVUM:               Bu üssün kapağının altında bırakılan hiçbir şey düşmesini
                     BİTİRMEZ. Her nesne aynı yönde inmeye devam eder, ama
                     indikçe daha az iner; derine giden daha yavaş gider ve
                     hiçbir zaman varmaz. Ağır olan durmadan önce daha çok yol
                     alır. Geri alınamaz: aşağı giden hiçbir şey yukarı gelmez.
NOVUM TAŞIYICISI:    kelepçe × eldivenli avucun kapak ağzında açılması
                     → kelepçe iner ama inişi bitmez; bir saniyede bir gövde
                       boyu, sonraki üç saniyede bir karış, sonra daha az
TEK KARE (§4①):      S0 · 0:04 — açık eldivenin bir karış altında, kapak
                     ağzının siyahında az önce sökülmüş kelepçe duruyor ve
                     uzaklaşmıyor; onun altında giderek sönükleşen noktalar
                     dizisi derinlere gidiyor. İzleyici 1 saniyede
                     "buraya bırakılan şey gitmiyor" der.
                     ⛔ D157 gereği bu cümle TAŞIYICI NESNENİN adını taşır:
                       kelepçe. Başka nesneyle geçilen kapı geçilmemiş kapıdır.
KİNETİK BAĞIMSIZLIK: ✅ 0 replik · 0 dış ses · 0 ekran metni · 0 gösterge.
                     Kural yalnız jestle kanıtlanır: bırak → in → durmadan yavaşla.
BAŞLIK ŞEMASI:       "THE KEPT LIGHT" (3 kelime) — izleyiciye NEREYE bakacağını
                     söyler: bir ışığa. Ve o ışığın burada TUTULDUĞUNU.
```

### §3 MAYA EŞİĞİ — tek ihlal

```
KABUK (tanıdık, yenilik KOYULMAZ): basınç giysisi · kask · el kesicisi ·
       kelepçe · el lambası · metal kapak · korkuluk. Hepsi bilinen biçimde
       davranır ve bilinen biçimde bozulur.
İHLAL SAYISI: 1 — "kapağın altında düşme bitmez". İkinci bağımsız kural YOK.
İHLAL DIŞI HER ŞEY normal fizikle: kapağın ÜSTÜNDE düşen alet 0,40 g'de bir
       saniyede bir gövde boyu iner ve GÜVERTEYE ÇARPAR; yürüyüş gerçek
       zamanlı; vakumda toz 0 kare, gölge mutlak siyah, ses yalnız temastan.
       Kuralın kanıtı yanındaki normalin kusursuz çalışmasıdır.
⚠️ DÜRÜST KAYIT: ihlalin gerekçesi filmde SÖYLENMEZ ve söylenmemelidir.
   Depo dışı fizik dili "kütleçekimsel zaman genişlemesi" der; bu film o
   kelimeyi hiçbir yerde kullanmaz, yalnız SONUCUNU çeker.
```

### §5 KURAL TEKRARI — ≥3 sahne · ≥2 farklı nesne

```
KURULUM    S0      kelepçe #1 (nesne 1) — ilk temas, inişi bitmiyor
           S1      asılı alan (nesne yığını) — kural bir TARİH olmuş
DOĞRULAMA  S4      kelepçe #2 (nesne 1 tekrar, yeni parça)
           S8      kelepçe #4 — aynı davranış, dördüncü kez
           S13     hat (nesne 2) — gergin duruyor; yukarı gelmiyor
           S17     hat (nesne 2) — iki eldivenle çekiliyor, bir parmak
                   genişliği bile yükselmiyor (kuralın en sert kanıtı)
SONUÇ      S20-S21 modül + eski lamba (nesne 3) — kural BEDELİ belirliyor
           S24     bekçinin kendi lambası (nesne 4) — kural bilerek kullanılıyor
TOPLAM:    8 sahne · 4 farklı nesne ✅ (kapı ≥3 sahne / ≥2 nesne)
⛔ Bu sahneler kurgu kapısının KESİLEMEZ listesindedir.
```

### ⛔ A4 YASAKLI SAHNE TİPİ DENETİMİ [03_PLAN_ONCESI]

```
· araç / kapak / airlock BİNİŞ-İNİŞ hareketi   → 0 kare. Bu filmde ARAÇ YOK.
  Kapak film boyunca AÇIKTIR; hiçbir sahnede açılmaz ve kapanmaz, hiç
  eşiğinden geçilmez.                                     [D69 ① · D148]
· tek ışıklı loş iç mekâna GİRİŞ               → 0 sahne. Bekçi S0'da zaten
  çalışma hacminin içindedir; hiçbir yere girmez, hiçbir yerden çıkmaz.
  S10'da da dışarıda değildir — o kadrajda kapak ağzının İÇİNDEDİR.
· aynalı-yansıtıcı yüzey önünde figür          → 0 sahne. Vizör optik berrak,
  yansıma SIFIR yazılır.                             [D20 · D69 · D79]
· novum TÜRETİLMİŞ optik fenomende             → HAYIR. Taşıyıcı KATI bir
  kelepçe ve fiziksel bir iniştir; gölge/yansıma/parlama DEĞİL.      [D73]
· novum bir YOKLUK taşıyor                     → HAYIR. Novumun kanıtı bir
  DELİK değil, delikte ASILI DURAN sayılabilir nesnelerdir; final karesinde
  ALTI parlak nesne sayılabilir ve VARDIR.                    [D76 · D141]
· jenerik / başlık kartı çıktısı               → 0 kare (kurgu kapısı ayrıca)
```

---

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Ölü modülü altı kelepçesinden kesip kapaktan bırakmak ve
              yatağı boşaltmak. Bu iş film başlamadan önce başlamıştı: S0'da
              birinci kelepçe çoktan sökülmüş, elinde.
   □ ENGEL:   Altıncı kelepçe yalnız modülü tutmuyor. Aşağıdaki tek ışığın —
              yıllar önce birinin bıraktığı eski lambanın — hattı da o pimden
              geçiyor. Ve bu üsse ait bir yasa var: kapağın altına inen hiçbir
              şey geri alınamaz, yalnız kesilebilir.
   □ BEDEL:   Altıncı kelepçeyi kesince modül iner, eski lamba onunla birlikte
              iner, ve kapağın altındaki her şey karanlıkta kalır · S21
              Kayıp S21'de EKRANDADIR: lamba çok aşağıda, konisi öteye
              bakıyor, arada asılı duran hiçbir şey aydınlanmıyor.
   □ MUHATAP: ortamın KALICI olarak değişen parçası — kapağın altındaki asılı
              alan. S21'de ışığını kaybeder, S24'te yenisini alır, ve ikisi de
              geri alınamaz. İkinci kanal: bekçinin kendi geçmiş kararı —
              o alandaki beş kelepçeyi de, bu vardiyayı da o bıraktı.
B5b □ AYRILIK: YOK — bu filmde tam 1 insan var (madde iki insanlı planda koşar).

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  1. DORUK              S20 → S21   (modül iniyor · bedel görülüyor)
  2. MERKEZÎ SEÇİM      S19         (kesici kapanıyor)
  3. KAPANIŞ İMAJI      S24
  4. HOOK               S0
  5. Kural kanıtı       S1 · S17
  6. Kalanı             S2-S16 · S18 · S22-S23
  ⛔ Sıra S0'dan BAŞLAMAZ. Gerekçe: THE SINKING STAKE'te 25 sahnenin 14'ü
    üretildi ve eksik 11 sahne ARDIŞIKTI ve filmin SONUYDU [D168].
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR

```
⛔ TETİKLENMEZ — bu film YATAY 16:9'dur (KILAVUZ_REHBERI §2.1 dikey karta ait).
   Yalnız ① satırı yatayda da yazılır çünkü HOOK §3.1 formata bağlı değildir:
① BİLGİ ASİMETRİSİ: DRAMATİK İRONİ · taşıyıcı ① ARKA PLAN OKUR ·
   asimetri anı 0:31 (S3 · tohum) · derinleşme S13 · kapanış S14 (bekçi öğrenir)
   ⭐ İzleyici, halkanın uzak yayındaki kelepçeden aşağı inen ince hattı S3'te
     görür; bekçi o sırada halkanın YAKIN yayında çalışıyordur ve kask
     periferi o yanı kapatır. S13'te hat gergin hâle gelip ışığa kalkar,
     bekçi hâlâ sırtı dönük raftadır. S14'te döner ve görür.
   ⛔ SAKİNLİK KORUNUR: bekçinin paniklediği kare sayısı = 0 (mekanizma
     karakterin sakinliğidir — panik ironiyi ÇÖZER).
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2.2, 25 sahneye ölçeklendi)

| # | vuruş | % | saniye | sahne | not |
|---|---|--:|--:|:--:|---|
| 1 | Açılış imajı | 0-4 | 0-9 | S0 | kapanış imajıyla ÇİFT tasarlandı (çift kartı aşağıda) |
| 2 | Kurulum | 0-12 | 0-29 | S0-S2 | dünya + bekçinin yetkinliği (kesme jesti tereddütsüz) |
| 3 | **Tohum bilgi** | 12 | 31 | S3 | uzak yaydaki kelepçeden inen ince hat · 2 s · bakışla vurgusuz [FINAL §3] |
| 4 | **Katalizör** | 14 | 34 | S3 | ikinci kelepçe kesilir, modül ilk kez BİR KARIŞ iner — geri alınamaz. Açılış bütçesi %10-15 bandının içi (25-37 s) ✅ [HOOK §1.1] |
| 5 | Tartışma | 12-32 | 29-79 | S3-S8 | doğrulama jestleri: ölçer, tutar, keser, bırakır |
| 6 | Orta nokta — **SAHTE YENİLGİ** | 52 | 129 | S13 | modül tek kelepçeye kalınca yatar; hat karanlıktan kalkar ve GERGİN durur. Bekçi sırtı dönük. |
| 7 | Umut-önce-düşüş | 64-72 | 159-179 | S16-S18 | iki başarısız kurtarma denemesi |
| 8 | **Her Şeyin Kaybı** | 76-84 | 189-209 | S19-S21 | kesim · modülün inişi · alanın kararması |
| 9 | Final | 84-96 | 209-239 | S21-S23 | boş halka · sap · lambanın çözülmesi |
| 10 | Kapanış imajı | 96-100 | 239-249 | S24 | açılışın aynası; temayı taşıyan tek kare |

```
⭐ VİRAL KARE KAPISI [§2.4] — dört sahne, her biri İKİ satır taşır:

⭐VİRAL S12 · YÜZ:     çene gevşer, göz kapakları bir kez hızlı kapanıp açılır
                       (0,4 s) — beklemediği bir hareket oldu
              HAREKET: modül tek yandan boşalır, bir karış düşüp bir gövde
                       boyu SALINIR; altındaki bütün noktalar kadrajda kayar
⭐VİRAL S14 · YÜZ:     baş dönüşün ORTASINDA durur; ağız kapalı, alt dudak
                       içeri çekilir, bakış aşağı kayar (1,2 s)
              HAREKET: eldiven hattın üstünde kayar; hat gerilip ŞAKLAR ve
                       titremesi kadrajın altına doğru koşar
⭐VİRAL S19 · YÜZ:     gözler bir vuruş kapanır, açıldığında bakış aşağıda
                       değil ileridedir (0,8 s)
              HAREKET: kesicinin çenesi kapanır, pim ayrılır, modül tek
                       karede kadrajın altından çıkar; alttan gelen ışık
                       vizörün üstünden hızla geçip söner
⭐VİRAL S23 · YÜZ:     bir kez uzun ve yavaş nefes verir; kaşlar düşer,
                       bakış sabitlenir (1,5 s)
              HAREKET: lamba klipsinden kurtulup avucun içinde bir tur döner
⛔ Bu dört sahne kurgu kapısının KESİLEMEZ listesindedir [Kaleida vakası].
⛔ Dördünün de ön koşulu D79'un pozitif cümlesidir: vizör optik berrak,
  yüz her baş açısında okunur. Aynasız vizör yoksa ① kanalı fiziksel olarak
  kapalıdır ve etiket düşer.
```

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       YANLIŞLIK KOMPOZİSYONU — tamamen okunur bir sahne (bir adam
                 bir parçayı kapaktan aşağı bırakıyor) ve TEK anormal öğe
                 (parça uzaklaşmıyor). Anomali KATI bir nesnedir, türetilmiş
                 optik fenomen DEĞİL [D73 kapısı geçildi].
HAREKETİN ORTASI: S0'ın ilk cümlesi süren bir eylemi tarif eder — eldiven
                 ZATEN açılmaktadır, kelepçe ZATEN elinden çıkmıştır. İş
                 kadraj öncesinde başladı: birinci kelepçe film başlamadan
                 sökülmüştü.                                    [HOOK §2.2]
0-2 SN:          kadraj normal + TEK öğe yanlış — izleyici neyin yanlış
                 olduğunu tam bilmez ama bir şeyin yanlış olduğunu bilir.
0:03 KONTROLÜ:   0:03'te ilk kareden FARKLI bilgi: kelepçenin ALTINDAKİ
                 noktalar dizisi kadraja girer (derinlik açılır).
REVEAL:          6-8. saniye bandı — kadraj dışı → kadraj içi ikili kilidiyle;
                 sis/mesafe/flu perdesi 0 kare [D71].
S0 SORUSU:       "Bu parça neden gitmiyor — ve altındaki o kadar şey oraya
                 nasıl birikti?"
S1 İKİNCİ BİLGİ: Soruyu BÜYÜTÜR, cevaplamaz: ölçek. Kapağın altı bir kuyu
                 değil bir ARŞİVDİR ve dibinde tek bir sıcak ışık vardır.
BİLGİ EŞİTLİĞİ:  S0-S1'de bekçi bilmiyor değil — o BİLİYOR, ama kural onun
                 için sıradandır; izleyici için değildir. Yapay geciktirme YOK:
                 kuralın kendisi 0. karede görünür, saklanan şey SEBEBİ [D71].
İLK 2 SN SESİ:   giysi fanının dar, sabit yatağı + eldivenin mühür halkasının
                 tek kuru KLİK'i (kelepçe avuçtan ayrılırken). Müzik 0.
                 ⛔ Akış içi videoların ~%85'i sessiz başlar: görsel zemin
                   tek başına ayakta durmak zorunda [HOOK §5].
```

## 🔗 AÇILIŞ-KAPANIŞ ÇİFTİ — ÇİFT KARTI (`ACILIS_KAPANIS_CIFTI_KILAVUZU.md` §5)

```
ÇİFT TİPİ        KAFİYE                          (§1 band kararı: 3-5 dk)
TAŞIYAN TEMA     Aynı avuç, aynı ağız, aynı yasa — değişen tek şey, avuçtan
                 çıkanın ne olduğu.

İLK KARE (S0 · 0:00 · kurulum A)
  kompozisyon    açık eldiven kadrajın sol-üst üçte birinde; kelepçe sağ-alt
                 üçte bir çizgisinde; kapak ağzının siyahı kadrajın alt
                 yarısı; kalçanın üstü kadrajın sağ kenarında
  tohum          bekçinin KENDİ el lambası — sönük, kalçasındaki klipste,
                 kadrajın SAĞ KENARINDA, merkezde DEĞİL, bakışla vurgusuz
  120 px testi   ⬜ koşulmadı — kapak dosyasında koşulacak     (HOOK §2.1)

SON KARE (S24 · 4:07 · kurulum A)
  kompozisyon    İLK KARENİN AYNISI — konum kilidi: eldiven aynı koordinatta
  ödeme          lamba artık kalçada değil AVUÇTA ve YANIYOR; merkeze taşındı

DEĞİŞEN TEK DEĞİŞKEN
  taşıyıcı       ② NESNE
  ne değişiyor   avuçtan çıkan şey: eskimiş bir kelepçe → bekçinin kendi
                 yanan lambası
  nerede         FOVEAL MERKEZ — açık eldiven kadrajın optik merkezindedir
  ⚠️ İkinci bir değişken gibi görünen "aşağının aydınlanması" bağımsız bir
    değişken DEĞİL, bu değişkenin SONUCUDUR: ışığı taşıyan nesne değişti.

DÖNGÜ İSE       — değil (band kararı KAFİYE). Kapanış sinyali serbest.

RİSK KONTROLÜ
  ✅ Değişen değişken sayısı = 1
  ✅ Konum kilidi tutuyor (ilk = son koordinat, aynı kurulum A)
  ✅ Kapanış sinyali meşru (kafiye bandı)
  ✅ Tohum merkezde DEĞİL (sağ kenar)
  ✅ Çift, HOOK §6①'in soru-cevap çiftinden farklı şey söylüyor:
     soru "neden gitmiyor", çift "neyi bırakacağını sen seçiyorsun"
```

## 🔚 FİNAL (`FINAL_VE_PAYLASIM_KILAVUZU.md` §2 · §2.2 · §3)

```
FİNAL TİPİ:      TWIST + TOHUM BİLGİ        (3-5 dk kartının birinci tercihi)
                 Twist: kesilmesi gereken son kelepçe, aşağıdaki tek ışığı
                 tutan kelepçedir. Tohum S3'te (0:31, 2 s) ekilmiştir ve
                 ödemesi S15'te makroda yapılır.
SON PLAN TİPİ:   İLK KADRAJA DÖNÜŞ            (§2.2 · kısıtlı formatta en uygun)
KAPANIŞ BÜTÇESİ: doruk S21'de biter (219 s) → son kare 249 s
                 30 s / 249 s = %12   ✅ 3-5 dk bandı %8-12'nin üst ucu.
GÖRSEL İKİLEM:   İş bitti ve yatak boş — ama aşağıdaki tarihin tamamı artık
                 karanlıkta ve görünen tek şey en yeni altı parçadır.
                 İzleyicinin cevaplayacağı soru: bu bir onarım mı, bir
                 devir teslim mi?
FİNAL MUHATABI:  ortamın kalıcı değişen parçası (B5 MUHATAP ile aynı) —
                 finalin yankısı bir insanda değil, kapağın altındaki alanda
                 görünür.
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` ve `KURGU_RITMI §2`
> örüntü kırıcı — **ardışık iki sahne aynı ölçek + palet + ses dokusunda
> olamaz.** Soru/cevap sütunları `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU` §2-§4.
> Kurulum harfleri: aşağıdaki KURULUM SÖZLÜĞÜ.

| S | başlık | olay | kurulum | palet | ses dokusu | açılan soru | sonrakinin cevabı | bütçe |
|---|---|---|:--:|:--:|:--:|:--:|:--:|---|
| S0 | AVUÇ VE AĞIZ | eldiven açılır, kelepçe #1 iner ve inişi bitmez · 5 kelepçe kalır | **A** | Z2 | ①fan+klik | ③ mekânın sırrı | ⓑ yeni soru | ✋ el #1 · 👁️ göz #1 |
| S1 | ALTIDA NE VAR | kapak ağzından aşağı: asılı alan, derinde tek sıcak nokta | **E** | Z3 | ②ince fan | ③ mekânın sırrı | ⓐ kısmi | 🌌 ölçek |
| S2 | HALKA | yatak, halka, 5 kelepçe, altında modülün gövdesi | **D** | Z1 | ③güverte teması | ② nesnenin akıbeti | ⓐ kısmi | 🚶 yürüyüş #1 |
| S3 | İKİNCİ KELEPÇE | ⭐TOHUM 0:31 · ⭐KATALİZÖR 0:34 — kesilir, modül bir karış iner | **C** | Z1 | ④kesici ısırığı | ① eylemin sonucu | ⓐ kısmi | 👁️ göz #2 |
| S4 | BIRAKMA | 🕰️KÜME#1 (devam) — kelepçe #2 avuçtan çıkar ve iner · 4 kalır | **C** | Z1 | ①fan+klik | ② nesnenin akıbeti | ⓓ yanlış çıkar | ✋ el #2 |
| S5 | DÖRT | halkanın yakın yayı; dört kelepçe sayılır | **D** | Z1 | ③güverte teması | ⑤ zamanın dolması | ⓐ kısmi | 🚶 yürüyüş #2 |
| S6 | ÜÇÜNCÜ | kelepçe #3 kesilir ve iner · 3 kalır | **C** | Z1 | ④kesici ısırığı | ① eylemin sonucu | ⓑ yeni soru | 🔁 tepki #1 |
| S7 | PİM | makro: kesicinin çenesi dördüncü pimin üstünde | **B** | Z1 | ④kesici ısırığı | ② nesnenin akıbeti | ⓐ kısmi | ✋ el #3 |
| S8 | İKİ | kelepçe #4 iner · 2 kalır; modül gözle görülür yatar | **C** | Z1 | ④kesici ısırığı | ④ bedenin sınırı | ⓒ ertelenir | 🔁 tepki #2 |
| S9 | UZAK YAY | bekçi halkanın uzak yayına yürür; 2 kelepçe kadrajda | **D** | Z1 | ③güverte teması | ③ mekânın sırrı | ⓑ yeni soru | 🚶 yürüyüş #3 |
| S10 | KAYA VE AĞIZ | dışarıdan: kayanın altındaki üs, aydınlık ağız, altında sütun | **F** | Z4 | ⑤gövde iniltisi | ③ mekânın sırrı | ⓐ kısmi | 🌌 ölçek 1:10 |
| S11 | GERİ | yatağın uzak yayı; iki kelepçe; modül daha da yatık | **D** | Z1 | ③güverte teması | ② nesnenin akıbeti | ⓑ yeni soru | 🔁 tepki #3 |
| S12 | SALINIM | ⭐VİRAL — kelepçe #5 iner, modül tek yandan boşalır ve salınır · 1 kalır | **C** | Z1 | ④kesici ısırığı | ① eylemin sonucu | ⓐ kısmi | 👁️ göz #3 · 🔁 tepki #4 |
| S13 | GERGİN HAT | **ORTA NOKTA 2:09** — modül yatık durur; ince hat karanlıktan kalkar ve gerilir. Bekçi rafta, sırtı dönük | **D** | Z1 | ②ince fan | ② nesnenin akıbeti | ⓓ yanlış çıkar | 🎒 eşya #1 |
| S14 | GÖRÜR | ⭐VİRAL — döner, eldiven hattın üstünde kayar, baş dönüşün ortasında durur | **C** | Z1 | ③güverte teması | ① eylemin sonucu | ⓐ kısmi | 👁️ göz #4 · 🔁 tepki #5 |
| S15 | PİMİN BAŞI | makro: hattın halkası altıncı pimin yuvarlanmış başının altında | **B** | Z1 | ②ince fan | ② nesnenin akıbeti | ⓑ yeni soru | ✋ el #4 |
| S16 | ÇEKER | başarısız deneme #1 — hattı iki eldivenle tutar ve çeker | **C** | Z1 | ⑤gövde iniltisi | ① eylemin sonucu | ⓐ kısmi | 🔁 tepki #6 |
| S17 | GELMEZ | 🕰️KÜME#2 (devam) — botlar güvertede kayar; hat bir parmak yükselmez | **C** | Z1 | ⑤gövde iniltisi | ④ bedenin sınırı | ⓓ yanlış çıkar | 👁️ göz #5 |
| S18 | HALKA VE BAŞ | başarısız deneme #2 — halkayı pimin başından geçirmeye çalışır; geçmez | **B** | Z1 | ②ince fan | ① eylemin sonucu | — düz cevap | ✋ el #5 |
| S19 | KESER | ⭐MERKEZÎ SEÇİM 3:09 · ⭐VİRAL — kesici kapanır, pim ayrılır, modül kadrajın altından çıkar | **C** | Z1 | ④kesici ısırığı | ② nesnenin akıbeti | ⓑ yeni soru | 👁️ göz #6 · 🔁 tepki #7 |
| S20 | İNİŞ | modül asılı alanın içinden aşağı iner, lamba onunla; geçtiği her şey bir an aydınlanır | **E** | Z3 | ②ince fan | ③ mekânın sırrı | ⓐ kısmi | 🌌 ölçek |
| S21 | KARANLIK | 🕰️KÜME#3 (devam) — ⭐BEDEL GÖRÜLÜR: lamba çok aşağıda, konisi öteye bakıyor; arada hiçbir şey aydınlanmıyor. **MUTLAK SESSİZLİK** | **E** | Z3′ | ⑥sessizlik | ③ mekânın sırrı | ⓐ kısmi | 🔁 tepki #8 |
| S22 | SAP | boş halka; bir sap hâlâ çerçeveye cıvatalı. Bekçi ona dokunmaz — SEÇİM #2 | **D** | Z1 | ③güverte teması | ① eylemin sonucu | ⓑ yeni soru | 🚶 yürüyüş #4 |
| S23 | ÇÖZER | ⭐VİRAL — kendi lambasını kalçasındaki klipsten çıkarır | **C** | Z1 | ①fan+klik | ② nesnenin akıbeti | ⓐ kısmi | 🎒 eşya #2 · 👁️ göz #7 |
| S24 | BIRAKIR | KAPANIŞ İMAJI — eldiven açılır, yanan lamba iner ve inişi bitmez; alan yeniden görünür · ALTI parlak nesne | **A** | Z2′ | ①fan+klik | — terminal | — | ✋ el #6 · 🌌 ölçek |

```
DÜZ CEVAP BÜTÇESİ [SAHNE_ZINCIRI §4]: 24 sınırın en çok %12-15'i = 3.
Kullanılan: 1 (S18→S19). Bant içinde ✅ ve kurulum bloğuna YIĞILMADI.
ARDIŞIK AYNI CEVAP TİPİ: yok — tablo sütunu satır satır okundu ✅
KARAKTER BÜTÇESİ TOPLAMI [KARAKTER §6 · 3-5 dk sütunu]:
  👁️ göz 7 (taban 3-4 ✅) · 🔁 tepki 8 (taban ~6 ✅) · ✋ el 6 (taban ~4 ✅) ·
  🚶 yürüyüş 4 (taban ~3 ✅) · 🎒 eşya 2 (taban ~1 ✅) · 🌌 ölçek 1:10 → S10 ✅
  🔁 Kuleshov döngüsü: 8 (taban ≥8 ✅) — S0·S3·S8·S12·S14·S17·S19·S21
```

### 📐 KURULUM SÖZLÜĞÜ — altı kurulum (`ACI_YAYI` §4 · `KAMERA_ACISI` §2)

| harf | ölçek | açı tipi | lens | konum | ne görür |
|:--:|:--:|---|:--:|---|---|
| **A** | CU (3) | tepe · tam aşağı | 50mm | kapak ağzının 0,6 m üstünde, aşağı bakar | açık eldiven · ağzın kenarı · kalçanın üstü |
| **B** | CU (3) | üst açı 30° | 85mm | pimin 0,9 m üstünde, azimut halkanın dışından | pim · kesicinin çenesi · hattın halkası |
| **C** | MS (2) | profil · göz hizası | 50mm | bekçiden 2,0 m, tam yandan | bekçi bel üstü · halkanın bir yayı · vizör |
| **D** | WS (1) | göz hizası · cepheden | 24mm | yatağın karşı duvarından 5,0 m | bütün yatak · halka · kelepçe SAYISI |
| **E** | EWS (0) | tepe · tam aşağı | 24mm | ağzın 0,4 m üstünde, aşağı bakar | asılı alan · derinlik · eski lamba |
| **F** | EWS (0) | alt açı 20° | 28mm | üssün 9,0 m dışında ve altında, yukarı bakar | kaya tavanı · kutu · aydınlık ağız · kara disk |

```
AÇI TİPİ SAYISI: 5 ✅ ≥3  (tepe A·E · üst açı B · profil C · göz hizası C-D ·
                 alt açı F) — üç kurulumun üçü de aynı yerden bakmıyor.
KURULUM SAYISI:  6  (ACI_YAYI §4 bandı: 25 sahnede tavan 13 · taban 3) ✅
                 ⭐ Bilinçli olarak bandın ALT ucuna yakın: §4b'nin dönüş
                   hedefi az kurulumla kurulur, çok kurulumla kurulamaz.
DERECE SATIRLARI: B üst açı 30° (meşru bant 15-30) · F alt açı 20° (meşru
                 bant 15-30) · dutch 0 sahne. Abartı eşiği aşılmadı ✅
                 [KAMERA_ACISI §5]

KURULUM İSKELETİ: A E D C C D C B C D F D C D C B C C B C E E D C A

  (25 harf = 25 sahne)
  KÜME:   3 ✅ (≥2)   S3-S4 · S16-S17 · S20-S21   — her biri 2 klip (tavan 3)
  DÖNÜŞ:  15/25 = %60 ✅ (≥%40) — kapının kendi ölçümü
          S4 S5 S6 S8 S9 S11 S12 S13 S14 S16 S17 S18 S19 S21 S23
          (elle yapılan ilk sayım %48 idi; betik pencereyi ÖNCEKİ DÖRT
           harf olarak alıyor — kaynağından ≤3 sahne sonra. Betik kazanır.)
  ⛔ Aynı harf AYNI kurulumdur ve kamera metni BİREBİR kopyalanır +
    işaret satırını taşır [ACI_YAYI §7 ⑥]:
      dönüş → "— the same position, height and lens as Scene N."
      küme  → "continues the previous clip from its exact last frame — the
               same position, height and lens as Scene N."
  ⚠️ Model harf iskeletini GÖRMEZ, yalnız metni görür. Lens · yükseklik ·
    mesafe aynı KARAKTERLERLE yazılır ("2.0 m" hep "2.0 m").

ARDIŞIK ÇİFT DENETİMİ [ACI_YAYI §3 · 03_PLAN_ONCESI B4]
  Ölçek merdiveni: EWS(0) – WS(1) – MS(2) – CU(3) – ECU(4)
  A=3 · B=3 · C=2 · D=1 · E=0 · F=0
  24 çiftin 19'u TAM 1 kademe ✅ · 3'ü küme (muaf, işaretli) ✅
  BİLİNÇLİ ŞOK 2/2 [tavan 1-2]:
    ⚡ŞOK#1  S0→S1  A(3)→E(0) = 3 kademe · kozmik keşif: avuçtan arşive
    ⚡ŞOK#2  S19→S20 C(2)→E(0) = 2 kademe · DORUK — en yüksek kontrast
             sıçraması doruk sahnesindedir [ACI_YAYI §9] ✅
  Açı farkı: C↔D aynı pitch (0°) ama azimut 90° (profil ↔ cephe) ✅ ·
  C↔B pitch 30° + azimut 60° ✅ · D↔F pitch 20° + azimut 90° + 9 m konum ✅ ·
  E↔D 90° ✅ · A↔E 0° pitch AMA 3 kademe ölçek (şok, bilinçli) ·
  C↔E 90° (şok) · C↔A 90° ✅

BÖLÜM KESİĞİ:    S12 ile S13 arasında (BOLUM_1: S0-S12 · BOLUM_2: S13-S24)
                 ⛔ Bölüm sınırı da ardışık bir ÇİFTTİR: C(2) → D(1) =
                   1 kademe + azimut 90° ✅ güvenli bantta.
```

### ⚡ ÖRÜNTÜ KIRICI DENETİMİ [KURGU_RITMI §2]

```
Üç sütun (ölçek · palet · ses dokusu) yan yana okundu: ardışık hiçbir çiftte
üçü birden aynı DEĞİL.
  · S3↔S4 · S16↔S17 · S20↔S21 aynı ölçek+palettedir — ama bunlar KÜMEDİR
    (§3 🕰️): tek vuruşun iki klibi, kesme değil bölünmüş çekim. Ses dokusu
    S3↔S4'te ve S20↔S21'de ayrıca değişir; S16↔S17'de vuruş tek olduğu için
    doku bilinçli olarak sürer.
  · MAKRO kırıcı (her 3-4 sahnede mekân/tempo): S10 dışarı · S13 raf ·
    S20 alan · S24 ağız ✅
```

---

## 🎙️ REPLİK TABLOSU

```
⛔ TETİKLENMEZ — REPLİK SAYISI: 0. Film konuşma bakımından tamamen sessizdir
   (insan 0 · makine 0 · telsiz 0 · kayıt 0).

GEREKÇE — ve bu bir "en güvenli" iddiası DEĞİLDİR [KART 7'nin 02.09 kaydı]:
  ① ONERME §4② KİNETİK BAĞIMSIZLIK: kural yalnız jestle kanıtlanmak zorunda
    ve bu filmde kanıtlanıyor. Bir replik kuralı AÇIKLAR ve exposition
    tuzağına düşer.
  ② Ortam kartı: bu üssün dışı da içi de vakumdur. Havadan taşınan ses YOKTUR;
    duyulan her şey gövdeden iletilir. Kadraj dışı bir insan sesi için
    kadrajda olmayan ikinci bir insan gerekir — HUMAN COUNT LOCK bunu kapatır.
  ③ Film 1 insan taşıyor ve muhatabı bir insan değil, ortamın kalıcı değişen
    parçasıdır (B5 MUHATAP). Akuzmatik otorite bu hikâyede bir işe yaramaz.
⛔ Bu karar KART 7'nin merdivenini atlamak DEĞİLDİR: merdivenin 1. basamağı
  (kadraj dışı ses) bile ikinci bir kaynak gerektiriyor ve bu filmde yok.
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** sabitlenir ve her IMAGE promptuna tam
> yazılır (kural ③: prompt self-contained · "BIBLE'a bak" atfı YASAK).

### 👤 CHARACTER BIBLE — bekçi (promptlarda İSİMSİZ [D34])

```
Erkek, elli dört. Geniş omuzlu, koyu kahverengi ten. (⛔ Tek pencerede en çok
ÜÇ kişi özniteliği — yaş · yapı · ten. Boy, saç, yüz hattı EKLENMEZ [D167].)

GİYSİ: mat KOYU ZEYTİN yüzey giysisi; omuzlarda ve inciklerde solmuş kum
beyazı bantlar. Sol ön kol MANŞETİNDE ince soluk bir çizik — yıpranma kilidi
GİYSİ yüzeyinde, gövdede DEĞİL [D175].

KASK: sert kum beyazı kabuk, ÖNDE TEK DÜZ PANEL, görünür koyu bir çerçevenin
içinde. ⛔ Kubbe değil, kavis değil, dikişsiz değil [D146].
Panel optik olarak berrak: sıfır ton, sıfır ayna kaplaması, sıfır çevre
yansıması. Yüzü her karede ve her baş açısında tam okunur [D79].
KASK 25/25 SAHNEDE KAPALIDIR. Vizörsüz kare bir üretim hatasıdır [KART 3].

SIRT: DÜZ. Sırta monte ünite yok, sırt çantası yok, tank yok, hortum yok,
kablo yok, arka muhafaza yok. Sırtın kadraja girdiği her sahnede yokluk
listesi POZİTİF YÜZEYE çevrilir: "yakadan kalçaya kesintisiz tek düz panel,
üstünde hiçbir şey taşımıyor" [D139].

ELDİVENLER: ağır, dilimli, koyu; bilekte giysiyle TEK PARÇA. Zorlanma
ELDİVENİN ÜSTÜNDE okunur: dilimler boğumların üstünde gerilir ve kalkar.
⛔ "through the glove" kalıbı bu filmin hiçbir promptunda geçmez [D175].

TAŞIDIĞI İKİ ŞEY:
  ① kesici — kısa, iki çeneli, tek elle çalışan bir el aleti. S0-S19'da SAĞ
    elinde ya da kalçasının solundaki yuvada.
  ② KENDİ EL LAMBASI — yumruğu kadar, başlıklı, S0-S23 arasında SÖNÜK ve
    kalçasının SAĞINDAKİ klipste. Her karede oradadır ve hiç kullanılmaz.
    S24'te avucundadır ve YANAR. ⭐ Çehov: filmin ilk karesinde vardır.

KİR: S0-S12 yalnız eldivenlerin avuç içleri ve dizler mat. S13-S24 buna sağ
     önkol MANŞETİNİN dış yüzü eklenir (hattı çektiği yer). Klip İÇİNDE sabit,
     sahneler ARASI monotonik, hiç azalmaz [D147].
     ⛔ "Wear state: PHASE n" hiçbir prompta yazılmaz [D155].

DUYGU REGİSTERİ: yetkin, yorgun, telaşsız. Panik kare sayısı = 0. Son cümle:
"o çalışıyor, dayanmıyor."
```

### 🌍 WORLD BIBLE — ASILI ÜS

```
YER: bir kara deliğin üstünde SABİT tutulan bir kayanın ALT yüzü. Kayanın
uzak (üst) yüzündeki motorlar onu orada tutar; o motorlar hiçbir karede
kadrajda DEĞİLDİR ve alevleri, egzozları, kıvılcımları 0 karedir.
Statik gövde tam yerel ağırlığı hisseder: 0,40 g.

YUKARISI = KAYA. Kadrajın üstünde, çukurlarla dolu, mat, koyu taş bir tavan.
AŞAĞISI = KARA DİSK. Kadrajın altında, mutlak siyah, kenarsız bir düzlem;
tek işareti kenarındaki saç inceliğinde beyaz çizgidir — halka değil, hâle
değil, parlama değil: TEK, kesintisiz, ince bir çizgi.
⭐ D174: yön bir koordinata değil NESNEYE bağlanır. Bu filmde "yukarı" KAYA
TAVANIDIR, "aşağı" KARA DİSKTİR; iki yön de adlandırılmış nesnelerdir ve
her prompt onları adıyla yazar.

ÜS: kayanın altına cıvatalanmış, kutu biçimli tek gövde. Üç buçuk gövde boyu
genişliğinde, iki buçuk gövde boyu yüksekliğinde. İçinde tek bir çalışma
hacmi (YATAK) vardır ve o hacim de vakumdur; basınç yoktur, hava yoktur.
Yatağın zemininde kare bir AĞIZ açıktır — bir gövde boyu kenarında. Ağız
film boyunca AÇIKTIR; hiçbir sahnede açılmaz ve kapanmaz.
Ağzın çerçevesinde ALTI kelepçe yuvası vardır ve altı yuva film boyunca
altıdır. Kutunun dışında, ağzın çevresinde, tek bir korkuluk dönüyor —
bekçinin önkolundan biraz uzun.

MODÜL: ağzın altında, altı kelepçeyle çerçeveye asılı ölü bir silindir.
Bekçiden biraz uzun, kalçasının iki katı kalınlığında. Mat, koyu, çıplak;
üstünde YAZI, RAKAM, İŞARET, ÇENTİK YOKTUR.

⭐ ASILI ALAN: ağzın altında, birbirinin altında duran nesneler. Yakındakiler
küçük ve yeni: bir kelepçe, bir kelepçe, bir kelepçe. Derindekiler daha
büyük ve daha sönük. En derindekiler yalnız birer noktadır. Hepsi aynı
yönde, çok yavaş inmeye devam eder. ⛔ Sayısız çoğul YAZILMAZ: kadrajda
sayılabilir olanlar sayılır, gerisi "daha aşağıda daha az ışık alan
biçimler" olarak yazılır [KART 13].

⭐ ESKİ LAMBA: alanın içinde, kapaktan yaklaşık on gövde boyu aşağıda duran,
başlıklı, yumruk büyüklüğünde eski bir el lambası. Konisi AŞAĞI bakar.
Alanın görülebilmesinin TEK sebebi odur. Yıllar önce biri onu bıraktı ve o
da inişini bitiremedi. Hattı yukarı, ağzın çerçevesindeki ALTINCI kelepçenin
pimine bağlıdır.

⭐ RENK TEK YERDE, TEK CÜMLEDE [⛔ D176]: "Ağzın altında ne kadar aşağı
inilirse eski lambanın ışığından o kadar az düşer: yakın nesneler soluk
çelik okunur, derindekiler zayıf kehribar, en derindekiler yalnız nokta."
Bu cümle YALNIZ SCENE/WORLD bloğunda durur. LIGHT bloğu hiçbir yüzeye renk
atamaz; kontrast garantisi ÖZNEYİ tarif eder.

⛔ 0 ekran · 0 kadran · 0 gösterge · 0 tuş takımı. Bu üste bilgi taşıyan tek
  şeyler şunlardır: çerçevede kalan kelepçe SAYISI, modülün YATMA açısı ve
  ağzın altındaki parlak nesnelerin SAYISI.
```

### 🎥 CAMERA BIBLE

```
Klip İÇİNDE kamera hiç hareket etmez: zoom yok, pan yok, tilt yok, track yok,
kesme yok, kamera sarsıntısı yok [KART 8].
Sahneler ARASINDA kurulum değişir ve bu KART 8'in kapsamı dışındadır.
Altı kurulum yukarıdaki sözlükte; harf dizisi KURULUM İSKELETİ satırında.
LENS: küresel. ⛔ Anamorfik yatay parlama YASAK — vakumda atmosferik saçılma
yoktur, parlama fiziksel olarak yanlıştır [SINEMATOGRAFIK §11].
EKRAN YÖNÜ: ağız her yatak kadrajında kadrajın ALT yarısındadır; alan her
zaman ağızdan AŞAĞI gider; kaya her dış kadrajda ÜST üçte birdedir. 25/25
sahnede sabit, ters dönüş 0.
```

### 💡 LIGHTING BIBLE — bölge ışık takvimi [KART 6b]

| bölge | sahneler | kaynak | karakter |
|:--:|---|---|---|
| **Z1 YATAK** | S2 S3 S4 S5 S6 S7 S8 S9 S11 S12 S13 S14 S15 S16 S17 S18 S19 S22 S23 | tavana gömülü İKİ başlıklı çalışma lambası, aşağı bakar | serin nötr beyaz, tepeden; gölgeler mutlak siyah ve jilet kenarlı; ikincil yansıma YOK |
| **Z2 AĞIZ** | S0 | aynı iki lamba yukarıdan eldivenin üstüne; ağzın altında yalnız eski lambanın zayıflayan ışığı | üstte sert beyaz, altta hızla biten zayıf ışık |
| **Z3 ALAN** | S1 S20 | YALNIZ eski lamba, çok aşağıda | tek zayıf kaynak; yukarı doğru hızla azalır; yatak ışığı buraya HİÇ ulaşmaz |
| **Z4 DIŞARI** | S10 | ağızdan taşan yatak ışığı tek parlak dikdörtgen; kayanın altı o taşmayla zar zor yakalanır | tek pratik kaynak, gerisi mutlak siyah |
| **Z3′ ALAN, SÖNÜK** | S21 | kaynak YOK; yalnız çok aşağıda tek nokta, konisi öteye bakar | kadrajın neredeyse tamamı mutlak siyah |
| **Z2′ AĞIZ, YENİ** | S24 | üstte iki lamba; altta bekçinin YENİ lambası, serin ve parlak | üstte ve altta iki ayrı beyaz; alan yeniden okunur |

```
⭐ PLANLI TEK DEĞİŞKEN [ACI_YAYI §7③ · SAHNE_ZINCIRI §1]:
  Değişen tek şey ALANI HANGİ LAMBANIN AYDINLATTIĞIDIR.
  (a) sahne haritasında yazılı ve TEK değişken ✅
  (b) SINIRDA olur, klip İÇİNDE değil: S20'de kaynak HAREKET eder (bu bir
      durum değişimi değil, kaynağın yer değiştirmesidir); bölge değişimi
      S19→S20 · S20→S21 · S21→S22 · S23→S24 sınırlarındadır ✅
  (c) iki promptta ilgili blok BİREBİR aynı kelimelerle, yalnız o
      değişkenle farklı yazılır ✅
⛔ Işık kademesi hiçbir klibin İÇİNDE değişmez. Bir klipte ışık azalıyorsa
  sebebi KAYNAĞIN UZAKLAŞMASIDIR ve o hareket kadrajda görünür (S20).
```

### ⚙️ PHYSICS BIBLE

```
YERÇEKİMİ: 0,40 g. Yürüyüş GERÇEK ZAMANLI; ağır çekim YOK [D44].
  Kanıt sayısı [D127 — ivme YAZILMAZ, SÜRE ve MESAFE yazılır]:
  AĞZIN ÜSTÜNDE (normal): elden bırakılan alet ilk saniyede yaklaşık BİR
  GÖVDE BOYU iner ve güverteye ÇARPAR.
  AĞZIN ALTINDA (tek ihlal): aynı alet ilk saniyede bir gövde boyu iner,
  sonraki ÜÇ saniyede bir KARIŞ iner, ondan sonra daha az iner — ve inmeye
  devam eder. Yön hiç değişmez, hiç yükselmez, hiç durmaz.
  ⭐ AĞIR OLAN DAHA ÇOK YOL ALIR: modül ilk on saniyede yaklaşık YİRMİ gövde
  boyu iner, sonra yavaşlar; film bittiğinde otuz gövde boyu aşağıdadır ve
  hâlâ inmektedir.
  ⛔ GERİ ALINAMAZ: ağzın altına inen hiçbir şey yukarı gelmez. Hat çekilir,
  bir parmak genişliği yükselmez; hareket eden tek şey bekçinin kendi
  botlarının güvertede kaymasıdır.
VAKUM [§3.1]: toz 0 kare · asılı toz, toz perdesi, toz şelalesi 0 kare ·
  gölge mutlak siyah ve jilet kenarlı · dolgu ışığı YOK · rüzgâr 0 ·
  egzoz/alev/kıvılcım/duman 0 kare · pas 0 kare.
  ⚠️ Metal bir yapıda model ikincil yansıma üretmeye çok yatkındır: her
  prompta POZİTİF cümle iner ("metal duvarlar ikinci bir ışık atmaz").
SES [§3.1]: havadan taşınan ses YOKTUR. Duyulan her şey ya giysinin İÇİNDEN
  (fan, nefes) ya da TEMASTAN gelir (bot, eldiven, kesici, çerçeve). Kuru,
  kısa, tınısız.
KESİM: kesici bir pimi AYIRIR. Kıvılcım 0 · ısı parlaması 0 · duman 0 ·
  erimiş metal 0 · uçuşan talaş 0. Kopan yüzey mat ve düzdür.
```

### 🚫 NEGATİF BIBLE

> Tam metin `KILAVUZ_REHBERI` §5 negatif çekirdeği + D79 kask bloğu, bu
> filmin ortam ve yapı eklentileriyle. Bölüm dosyalarının başında yazılıdır
> ve her prompta iner.

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | risk kartı | nerede |
|---|---|---|---|
| HUMAN COUNT LOCK | tam **1** insan, 25 sahnenin **25**'inde | KART 4 | 25/25 prompt |
| HELMET STATE SCHEDULE | kapalı **S0-S24 (25 sahne)** · açık **0 sahne** | KART 3 | 25/25 prompt |
| KELEPÇE SAYACI | çerçevede kalan kelepçe — **S2 5 · S5 4 · S9 2 · S11 2 · S13 1 · S22 0** (kesimler: S3-S4→4 · S6→3 · S8→2 · S12→1). Monotonik, hiç artmaz, her D kurulumunda SAYILABİLİR | KART 5 | D kurulumu + kesim sahneleri |
| PARLAK NESNE SAYACI | ağzın altındaki yeni parlak nesneler: 1→2→3→4→5→**6** | KART 5 | A · E kurulumları |
| MODÜLÜN YATMA AÇISI | düz → bir karış → görünür → tek köşe — monotonik, geri dönmez | KART 5 | D kurulumu |
| YERÇEKİMİ | **0,40 g** — bırakılan alet ilk saniyede bir gövde boyu iner | KART 6 | 25/25 prompt |
| İHLAL BANDI | ağzın altında: 1 s'de bir gövde boyu · 3 s'de bir karış · sonra daha az | KART 6 | A · E kurulumları |
| SIVI TEMASI | **0 sahne** — bu filmde sıvı YOK | KART 1 | — |
| CANLI | **0 sahne** — bu filmde canlı YOK | KART 2 | — |
| YAPI ANATOMİSİ | kutu **1** · yatak **1** · ağız **1** · kelepçe yuvası **6** · yatak lambası **2** · eski lamba **1** · bekçinin lambası **1** · korkuluk **1** · modül **1** · pencere **0** · ekran **0** | KART 13 | 25/25 prompt |
| ÖLÇEK MERDİVENİ | üs kadraj kesri: S10 %35 — tek dış plan olduğu için merdiven tek basamaktır ve bu bilinçlidir | KART 13 | S10 |
| ÖLÇEK ŞAHİDİ | S10'da ağzın içinde figür (1:10 kontrast) · yatak sahnelerinde korkuluk | KART 13 | S10 · D kurulumu |
| İNSANSIZ SAHNE | **0 sahne** — 25/25 sahnede insan var, KART 10 tetiklenmez | KART 10 | — |
| KIRPMA | S0: 10,0 s ham → 9,0 s kurguda (baştan 1,0 s) · diğer 24 klip kırpılmaz | KART 11 | S0 |

```
⛔ ÖLÇÜ SPEC'TE METRE, PROMPTTA GÖVDE BOYU [D138 · KART 13]:
   figür 1,88 m = 1H · kutu 6,5 m = 3,5H · yatak 4,0 m = 2,1H ·
   ağız 1,9 m = 1,0H · modül 2,1 m = 1,1H · kelepçe 0,26 m = 0,14H ·
   korkuluk 0,53 m = 0,28H · lamba 0,20 m = 0,11H
   Prompt gövdesine metre/santim/derece/f-sayısı GİRMEZ.
   ✅ Kamera MESAFESİ muaftır ("from two metres away") [D138 muafiyeti].
```

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D5 · D79 | vizör optik berrak, sıfır ton, sıfır ayna; yüz her açıda okunur; sırt DÜZ | 25/25 prompt |
| D139 | sırtın kadraja girdiği her kurulumda POZİTİF yüzey cümlesi | C kurulumu |
| D23 | sıfır-g süzülme TETİKLENEMEZ — hiçbir kare 0 g'de değil (0,40 g) | plan kararı |
| D24 | temas bütünlüğü: eldiven metale ERİMEZ; her temasta net yapısal sınır | S3-S19 |
| D30 · D39 | vakumda toz 0 kare; asılı toz / toz perdesi / toz şelalesi 0 kare | 25/25 negatif |
| D36 | vakumda duman/egzoz kıvrımı 0 kare — motorlar kadrajda değil | plan kararı |
| D41 | yumuşak ışık ≠ bloom; bloom %0 | 25/25 negatif |
| D44 | 0,40 g'de yürüyüş gerçek zamanlı, ağır çekim yok | S2 S5 S9 S11 S22 |
| D59 | yasak yerine POZİTİF tarif: "iner ve inmeye devam eder" | 25/25 prompt |
| D71 | reveal analog perdeyle gizlenmez; ihlal 0. karede, sebebi sonda | S0 |
| D73 | novum türetilmiş optik fenomende değil, KATI nesnede | plan kararı |
| D76 | novum bir yokluk değil: final karesinde ALTI nesne sayılabilir | S24 |
| D78 | sayaç tek karede kanıtlanır: çerçevedeki kelepçeler sayılabilir | D kurulumu |
| D95 | durum ekranda kanıtlanmazsa ölçülemez — üç metinsiz kanal | plan |
| D104 | tek baskın ışık + hedefe hareket YOK: kaynaklar pratik ve yakın | plan kararı |
| D122 | replik zamanları hesaplatılır — replik 0, madde boş | SPEC |
| D127 | ivme yazılmaz; SÜRE ve MESAFE yazılır | Physics Bible |
| D138 | metin yasağı KAPSAMLI: giysi, alet, çerçeve, modül, kaya, gök | 25/25 negatif |
| D141 | FİNAL VURUŞ KANITI BULUNAN: 4:07'de altı parlak nesne sayılabilir | S24 |
| D143 | zerre SAYISIYLA yazılır — bu filmde zerre 0, perde 0 | 25/25 negatif |
| D146 | kask ÖNDE TEK DÜZ PANEL, görünür koyu çerçeve içinde; kubbe değil | 25/25 prompt |
| D147 | kir MONOTONİK merdiven, klip içinde sabit; faz etiketi yazılmaz | Character Bible |
| D151 | novumun kanıt sahneleri KESİLEMEZ listesinde | ONERME §5 bloğu |
| D155 | "Wear state: PHASE n" hiçbir prompta yazılmaz | Character Bible |
| D157 | TEK KARE testi taşıyıcının ADIYLA koşuldu (kelepçe); kanıt sahnelerinde rakip olay 0 | S0 · S1 |
| D158 | merkezî seçim S19 · seçimden SONRAKİ seçim 2 (S22 · S23-S24) · başarısız deneme 2 (S16-S17 · S18) | plan |
| D160 | dosya adları film adıyla başlar | klasör |
| D167 | tek pencerede en çok ÜÇ kişi özniteliği | Character Bible |
| D168 | ÜRETİM SIRASI plana yazıldı ve S0'dan başlamıyor | B5 bloğu |
| D169 · D175 | zorlanma ELDİVENİN üstünde okunur; "through the glove" 0 kez; çıplak-deri negatifi ÜÇ bölgeli (yaka · bilek · ayak bileği) | 25/25 prompt |
| D174 | yön bir koordinata değil NESNEYE bağlanır: yukarı = KAYA, aşağı = KARA DİSK | World Bible + 25/25 prompt |
| D176 | yüzey rengi TEK cümlede ve YALNIZ WORLD bloğunda; kontrast garantisi özneyi tarif eder | Lighting Bible |
| D179 | imaj promptu 0,0 saniyeyi yazar, sahnenin SONUCUNU değil | S3 S12 S19 S20 S24 |
| D180 | planlı mutlak sessizlik KURGU işidir: MUZIK dosyasında HARD MUTE satırı | S21 · MUZIK |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S19 · 3:12 — iki çeneli bir el aletinin bir pimi
                     ayırdığı yakın an (alet + kuvvet + ayrılan metal).
NÖTR TARİFİ:         "The tool's two jaws close on a metal pin and the pin
                     parts cleanly. The parted faces are matt, flat and cold,
                     and the module simply begins to move downward."
                     ⭐ Yasak listesi (spark · heat glow · smoke · molten
                     metal · chips) YALNIZ NEGATIVE bloğunda durur; pozitif
                     gövde POZİTİF tarif eder [D59 · D123 · ⑯ ölçümü].
İKİNCİ SIRA:         S17 — bir gövdenin bir hattı çekmesi (gövdeye değen
                     kuvvet). Nötr tarifi: kuvvet GÖVDEYE değil ZEMİNE yazılır
                     ("his boots slide on the deck"), gövde tepkisi temassız
                     kalır.
```

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (kanal — POLİTİKA §4.1) |
|---|---|---|
| Kesimde kıvılcım / ısı / duman yazılmadı | Kesimin şiddeti ve "geri dönülmezlik" hissi zayıfladı | **malzeme sonucu**: kopan yüzey mat ve düz; ve **kütle-hız**: modül tek karede kadrajın altından çıkar |
| İkinci insan (önceki bekçi) kadraja hiç girmedi ve cesede dönüşmedi | "Birinin burada yaşadığı" bilgisi doğrudan söylenemedi | **alet tepkisi**: eski lambanın kendisi bir insanın kararıdır — başlığı aşınmış, hattı elle düğümlenmiş, ve kimse onu geri alamadı |
| Kırmızı ton yoğunluğu yazılmadı (derin nesneler için) | Derinliğin "yaş" okuması zayıfladı | **temassız gövde tepkisi** + kaynağa bağlama: renk yüzeye değil IŞIĞA bağlandı ("eski lambanın ışığından az düşer") ve kadrajda her zaman soluk çelik ve kum beyazı referans yüzey var |

```
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
⛔ Prompt yazılınca prompt_kontrol ⑯ koşulur (kelime ekseni · NEGATIVE dâhil).
```

---

## 📋 RİSK SAYIMI  (`02_RISK_KARTLARI.md` RİSK TOPLAMI)

```
□ Su/sıvı teması?             HAYIR — 0 sahne
□ Canlı?                      HAYIR — 0 sahne
■ Kask/vizör?                 EVET  → KART 3  (her uzay filminde) · sayısal kilit yazıldı
■ İkinci figür riski?         EVET  → KART 4  (her filmde) · HUMAN COUNT LOCK 1×25
■ Ekran/sayaç/gösterge?       EVET  → KART 5  · ÜÇ metinsiz kanal · 0 ekran/kadran
■ Parçacık/toz/patlama?       EVET  → KART 6  · toz 0 kare; asılı nesne kuralı POZİTİF yazıldı
■ Katmanlı/bölgeli dünya?     EVET  → KART 6b · altı bölgeli ışık takvimi tabloda
□ Diyalog?                    HAYIR — 0 replik
■ Kamera hareketi?            EVET  → KART 8  · klip içi lockoff; sahneler arası yay zorunlu
□ Tek baskın ışık + hedefe hareket? HAYIR — kadrajda uzak/baskın tek kaynak yok;
                              iki yatak lambası PRATİK ve TEPEDEDİR, bekçi hiçbir
                              sahnede bir ışığa doğru YÜRÜMEZ. KART 9 yapısal olarak zayıf.
□ İnsansız sahne?             HAYIR — 25/25 sahnede insan var, KART 10 tetiklenmez
■ Değişken çekim süresi?      EVET  → KART 11 · yalnız S0 (10,0→9,0 s); kırpma tablosu SPEC'te
■ Politika yüzeyi?            EVET  → KART 12 · yukarıdaki blok
■ Kadrajda büyük YAPI?        EVET  → KART 13 · anatomi kartı + ölçek şahidi

RİSK SAYISI: 9 / 14
```

```
⚠️ DÜRÜST OKUMA — 9 sayısı "5+" bandının üstünde ve gerekçesi yazılmalı:
  · Dokuzun DÖRDÜ her uzay filminde açık olan SABİT karttır (3 · 4 · 8 · 12).
  · Üçü (5 · 6b · 13) bu filmin OMURGASIDIR: metinsiz sayaç, bölge ışığı ve
    bir yapı olmadan bu hikâye yazılamaz.
  · Biri (11) tek bir klibin 1,0 s kırpılmasıdır ve tablosu yazıldı.
  · İKİ 🔴 KART SIFIR: su ve canlı. Ve ölçülmüş en net başarısızlık
    kartlarından KART 9 ile KART 10 da SIFIR — ikisi de tasarımla kapatıldı
    (pratik ışık · insansız sahne yok).
  · Malzeme azaltma kararları FİİLEN ALINDI ve şunlardır: 0 replik ·
    0 ikinci figür · 0 araç · 0 airlock/biniş-iniş · 0 sıvı · 0 canlı ·
    0 alev/egzoz/kıvılcım · 0 toz · 0 ekran.
  ⚠️ Eşik kalibrasyonu deponun kendi kaydına göre AÇIKTIR: "5+" bandı liste
    9 SORULUYKEN ölçüldü, payda bugün 14. Aynı film eski listede 5/9 sayardı.
```

---

## ✅ ÜRETİM ÖNCESİ KONTROL — THE KEPT LIGHT            tarih: 06.09.2026

```
A1 ✅ "no readable text" ile bir ekranın/göstergenin İÇERİĞİ aynı dosyada YOK.
     Bu üste 0 ekran · 0 kadran · 0 gösterge var; bilgi yalnız SAYI ve AÇI ile
     taşınır (kelepçe sayısı · modülün yatma açısı · parlak nesne sayısı).
A2 ✅ sahne sayısı: başlık 25 = blok 25 (BOLUM_1 13 + BOLUM_2 12) =
     "Scene N of 25" 25/25
A3 ✅ süre: 9 s hook + 24 × 10 s = 249 s = 4:09 = iddia edilen süre
A4 ✅ yasaklı sahne tipi taraması yapıldı — bulunan sahne: YOK.
     Karar satırları: "Araç 0 kare — bu filmde araç yoktur [D69 ①]" ·
     "Kapak film boyunca AÇIK; açılma/kapanma 0 kare [D69 ①]" ·
     "Loş iç mekâna giriş 0 sahne — bekçi S0'da zaten içeridedir [D69]" ·
     "Yansıtıcı yüzey önünde figür 0 sahne; vizör yansıması SIFIR [D20·D79]" ·
     "Novum katı nesnede, türetilmiş fenomende değil [D73]" ·
     "Novum yoklukta değil; final karesinde 6 nesne sayılabilir [D76·D141]" ·
     "Jenerik/başlık kartı 0 kare [D34·D70·D72]"
B1 ✅ doruk anı S19 (kesim) ve S20-S21 (iniş + karanlık) İÇİNDE tarif edildi;
     sahne arasına düşmüyor. S19'un video promptu pimin ayrıldığı anı
     saniyesiyle yazar; S20 inişi, S21 sonucu.
B1b ✅ bölge ışık takvimi tabloda; tek planlı değişken ve sınırda değişiyor
B2 ✅ bedelli seçim S19 · kayıp S21 sahnesinde GÖRÜLÜYOR
B3 ✅ TEMA: ZAMAN · motife döndüğü sahneler: S1 · S10 · S15 · S19 · S21 · S24
     (≥3 ✅ · B2'nin bedel sahnesi S21 bu listede ✅)
B4 ✅ kurulum dizisi: A E D C C D C B C D F D C D C B C C B C E E D C A ·
     kurulum sayısı 6 · açı tipi 5 · ardışık çiftlerin 19'u tam 1 kademe,
     3'ü işaretli küme, 2'si bilinçli şok (tavan 2) ·
     derece satırları abartı bandında (üst 30° · alt 20° · dutch 0)
     🆕 KURULUM İSKELETİ yazıldı · küme 3/2 ✅ · dönüş %60/40 ✅
     🆕 dönüş+küme satırları birebir kopya + işaret taşıyor (bölüm dosyaları)
B5 ✅ İSTEK: modülü altı kelepçesinden kesip kapaktan bırakmak
     ENGEL: altıncı kelepçe aşağıdaki tek ışığın hattını da tutuyor ·
     BEDEL: eski lamba modülle iner, alan karanlıkta kalır · S21
     MUHATAP: ortamın KALICI değişen parçası (asılı alan) + kendi geçmiş kararı
B5b ✅ tetiklenmez — tek insanlı plan
B5c ✅ ÜRETİM SIRASI yazıldı; ilk üretilecek sahne S20 (doruk), S0 DEĞİL
B6 ✅ POLİTİKA SATIRI: en red-riskli kare S19 · nötr tarifi yazıldı ·
     üç önlemin üçü de ÖNLEM/MALİYET/TELAFİ taşıyor · milliyet/kurum/kişi adı YOK
C  ✅ 6 sayısal kilit yazıldı (insan · kask · ölçü · yerçekimi · sıvı · canlı)
D  ✅ risk sayımı yapıldı: 9/14 · dürüst okuma yazıldı
E  ✅ QA SPEC bloğu AYRI DOSYADA: THE_KEPT_LIGHT_QA_SPEC.md [D117]
     ✅ QA PAKETİ SPEC ile birlikte üretildi [D165]

İMZA: 17 madde işaretlendi. ⛔ Üretimden önce prompt-kontrol skill'i koşulur.
```

---

## 🧾 QA'YA HAZIRLIK — künye (tam blok `THE_KEPT_LIGHT_QA_SPEC.md`'de)

```
FILM:                 THE KEPT LIGHT
FORMAT:               yatay 3-5 dk · 16:9
SCENE COUNT:          25
RUNTIME:              249 s (9 s hook + 24 × 10 s)
DIALOGUE LINES:       0     · konuşmalı sahne: yok
SILENT SCENES:        25    · MUTLAK SESSİZLİK planlı: S21 (209,0-219,0 s)
VIRAL INTERSTITIALS:  4     · S12 · S14 · S19 · S23   ⛔ KESİLEMEZ
PROTAGONIST:          bekçi (isimsiz) — bir imha yatağının tek görevlisi
CENTRAL CHOICE:       S19   · bedel S21'de görülür
```

## 📏 KAPI BETİĞİ — prompt_kontrol.py KOŞULDU (06.09.2026)

```
python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
        yatay_4_dk_filmler/THE_KEPT_LIGHT

SONUÇ:  ✅ GO · 📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik · 50 prompt
        ⛔ 0 BLOCK · ⚠️ 2 FIX (ikisi de AŞAĞIDAKİ BİLİNEN YANLIŞ POZİTİF)
        📏 image 2.453-3.553 kr · video 2.878-4.211 kr (tavan 4.300)

⛔ İLK KOŞU 2 BLOCK VERDİ — ikisi de kapatıldı ve sebebi kayda değer:
   ㉑ MÜHÜR KAPISI "çıplak-deri negatifi 2/3 bölge" dedi, oysa üç bölge de
   yazılıydı. Sebep: kapı NEGATIVE bloğunun HAM metnine bakıyor ve
   "none above the\ncollar seal" satır sonunda BÖLÜNMÜŞTÜ; "above the
   collar" ibaresi bu yüzden eşleşmedi.
   ⭐ ÇIKAN KURAL: üç bölgeli çıplak-deri negatifi yazılırken
     "above the collar" · "at the wrist" · "at the ankle" ibarelerinin
     hiçbiri SATIR SONUNDA BÖLÜNMEZ. (GOZLEM_DEFTERI adayı: kapı düz
     metne değil ham metne bakıyor.)

KAPATILAN DİĞER BULGULAR:
   ⑳ ZORLANMA KANALI (15 prompt) — "the glove's segments tighten and lift"
     efor fiili sayılıyordu ama gövde tepkisi sözlüğüne girmiyordu.
     Çözüm D175-güvenli: kavrama kanalı adlandırıldı —
     "his grip tightens and the glove's segments lift over the knuckles".
     Çekme sahnelerinde ölçülebilir bedel eklendi: "the second pull is
     slower than the first" · omuz + arka bot yüklenmesi [D169].
   YÖN KAPISI ② çapasız "toward" (6 cümle) — hedefin ekran konumu aynı
     cümleye yazıldı: "the black disc, which fills the lower half of the
     frame" · "toward the far arc in the right third of the frame" [D174].
   ⑯ POLİTİKA SÖZLÜĞÜ T2 yoğunluk (4 prompt) — kesim POZİTİF tarif edildi
     ("the parted faces are matt, flat and cold") ve yasak listesi yalnız
     NEGATIVE bloğunda bırakıldı; "dead" → "disused", "trapped" → "held"
     [D59 · D123].
   ㉑ örtüsüz gövde adı 'forearm' (2 imaj) — aynı cümledeki "bare" kelimesi
     tetikliyordu; modülün tarifi "matte, dark and unmarked" oldu.

⚠️ AYAKTA KALAN İKİ FIX — İKİSİ DE BİLİNEN YANLIŞ POZİTİFTİR:
   "KURULUM İSKELETİ 25 harf ↔ dosyada 13 / 12 video promptu"
   Kapı ⑩④ iskeleti dosya modunda o dosyanın prompt sayısıyla karşılaştırır.
   Film İKİ bölüm dosyasına bölündüğü için 25 ≠ 13 ve 25 ≠ 12 çıkar.
   ⭐ GEÇERLİ KOŞU KLASÖR MODUDUR ve orada 25 = 25'tir: küme ve dönüş
     kapıları KOŞTU ve GEÇTİ (küme 3 · dönüş %60).
   ⛔ İskelet satırı bilerek BOLUM_1'dedir: klasör modu iki bölüm dosyasını
     birleştirir ve iskeleti BİRLEŞİK metinde arar; satır yalnız PLAN'da
     kalsaydı klasör modu onu BULAMAZ ve iki kapı HİÇ KOŞMAZDI.
     (GOZLEM_DEFTERI adayı: bölünmüş filmde ⑩④ dosya modu kaçınılmaz FIX
      üretiyor; kapıya "klasör modunda ölç" kaçışı gerekiyor.)

⬜ KART P'nin İKİNCİ AYAĞI KOŞULMADI: `PROMPT_KONTROL/PROMPT_QA` kompozisyon
   ekseni betiğe inmez, insan gözüyle koşulur. Üretimden önce koşulacak.
⬜ DIALOGUE_CRITIQUE_PROMPT TETİKLENMEZ — bu filmde replik 0.
```

---

## 📎 REFERANS PAKETİ KARARI

```
⬜ YAZILMADI — ve gerekçesi: kural "iki insandan/araçtan fazlası varsa
   ZORUNLU" der. Bu filmde 1 insan ve 0 araç vardır. Tekrar eden varlıklar
   Character Bible ve World Bible içinde sayısıyla sabitlenmiştir
   (kesici 1 tip · lamba 2 adet aynı tip · kelepçe 6 adet aynı tip).
   ⚠️ Üretimde kelepçelerin biçimi sahneden sahneye kayarsa REFERANS_PAKETI
     açılır ve altı kelepçe tek onaylı kareden türetilir [D153].
```
