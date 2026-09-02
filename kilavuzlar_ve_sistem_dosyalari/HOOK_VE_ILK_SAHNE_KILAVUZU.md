# 🪝 HOOK VE İLK SAHNE KILAVUZU — İlk İki Sahnenin Tutundurma Mimarisi

> **Kaynak:** 09.08.2026 web araştırması — platform tutundurma verisi
> (YouTube Shorts / TikTok / uzun form), merak psikolojisi (Loewenstein
> bilgi boşluğu kuramı) ve cold open senaryo geleneği; hepsi deponun
> kurallarına (tek çekim, 0 kesme, metin 0,0 sn, negatif çekirdek) karşı
> süzüldü. Kaynak listesi §9'da.
>
> **Bu dosya `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §4'ün yerini alır** —
> o bölümün dört kuralı (0. kare sınavı, ikili kilit reveal, 3. saniye
> kontrolü, vaat-teslim) buraya taşındı ve genişletildi. §4 artık buraya
> adres verir; içerik iki yerde tutulmaz.
>
> **Ne zaman okunur:** PLAN yazılırken — vuruş tablosu
> (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2) doldurulduktan SONRA, sahne
> haritasından ÖNCE. S0-S1 promptları yazılırken tekrar açılır.
>
> İlgili dersler: 71 (analog perde) · 73 (türetilmiş novum) —
> loop tasarımı: `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §5 —
> paketleme: `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md`

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① HİÇBİR FİLM YAYINLANMADI. Buradaki her sayı dış araştırmadan gelen
   HİPOTEZDİR, bu serinin ölçülmüş sonucu değildir. İlk gerçek retention
   verisi geldiğinde §1 o veriyle revize edilir — dış sayı gerçek sayıya
   direnemez.

② ⭐ DÜZELTİLDİ (27.08.2026) — "İKİ KANITLI AVANTAJ FEDA EDİLİYOR"
   KAYDI YANLIŞTI. Biri hiç feda edilmiyormuş.

   • Metin kancası (+%30 bandı) → ⛔ AÇIK DEĞİL. Araştırma 2 katkıyı
     kaynağına kadar ayrıştırdı: +%30, harflerin ekranda olmasından
     DEĞİL, metnin üreticiye dayattığı "ilk saniyede net vaat"
     disiplininden geliyor. Vaadi görsel taşıyan metinsiz içerik aynı
     bandı yakalıyor (Marketing LTB · Viralish 2025 · Mishra, 46.605
     TikTok kancası). Metin yasağı bir handikap DEĞİL, bir ödeme
     biçimi: vaat harfle değil kadrajla yazılır.
     ⚠️ BEDELİ VAR VE TEKTİR: yükün tamamı 0. karenin vaadi okunabilir
     kılmasına biner → §2.1 **120 px testi artık tek taşıyıcıdır** ve
     bugüne kadar fiilen hiç koşulmadı.

   • Hızlı açılış kesmeleri (+%36) → ✅ HÂLÂ AÇIK ve bilinçli.
     Tek çekim / lockoff seri kimliği. Bu açığı KOMPOZİSYON + HAREKET
     + SES kapatmak zorunda (§2, §5).
     ⚠️ Araştırma 4 bu açığın büyüklüğünü ölçtü: yüksek performans
     gösteren AI bilim-kurgu dikey içeriğinin TAMAMI 2,5-4,0 saniyede
     bir kesiyor. Depo 8-10 saniyede, sahne içi 0 kesmeyle çalışıyor —
     rakip setten 2-4 KAT sapma. Bu ya deponun imzası ya mezarıdır ve
     YAYIN OLMADAN ÇÖZÜLEMEZ. (Rakip tablosunun yapı sütunları ölçüm
     değil çıkarımdır — yön olarak alınır, sayı olarak alınmaz.)

   Bir sonraki ajan "araştırmada vardı" diye ekran metni eklemesin:
   yasağın gerekçesi değişti ama yasak DEĞİŞMEDİ [D13/D45/D61/D70].

③ ÖLÇÜLMÜŞ PLATO: Kanca skoru bugüne kadarki tüm satırlarda 5-6 bandında
   (03_HIKAYE ve 05_SHORTS tablolarının Kanca sütunları). Bu kılavuzun
   başarı ölçütü o platonun kırılması — skor aynı bantta kalıyorsa
   kılavuz çalışmıyor demektir ve revize edilir.
```

---

# 1. 📊 SAYISAL GERÇEKLER — neden İKİ sahne

```
KARAR PENCERESİ
  Mobilde ortalama devam/terk kararı:            1,7 saniye
  İlk 3 saniyede karar verenler:                 %71
  Terk edenlerin ilk 3 saniyede gidenleri:       %50-60

EŞİKLER (shorts)
  3 sn tutundurma hedefi:                        %70+
  Viral bant:                                    %85+
  Algoritmik ölüm:                               %60 altı
  %60 ile %85 arasındaki izlenme farkı:          2,8 KAT

DÜŞÜŞ ZİNCİRİ — iki sahnenin matematiği
  3. saniyeyi geçenlerin 10. saniyeye ulaşanı:   %65
  10. saniyeye ulaşanların 30'a ulaşanı:         %45
  → İkinci düşüş dalgası S1'in bandında yaşanır.

YATAY / UZUN FORM
  İlk 30 sn'de %70 tutmak:                       "kazanan intro"
  %50-70 bandı:                                  sağlam
  Güçlü intro ↔ ortalama izlenme süresi:         +%58 korelasyon

LOOP (31 Mart 2025'ten beri)
  Her tekrar izleme ayrı view sayılır; algoritmanın en güçlü sinyali
  İLK TURDA sonuna kadar izlenme + rewatch. %30 loop oranı izlenme
  süresini fiilen 1,3× çarpar. → S0 aynı zamanda DÖNÜŞ KARESİDİR
  (bkz. §6 + SENARYO_VE_VIRAL_KAMERA §5).

RETENTION EĞRİSİNİN ÜÇ ŞEKLİ
  CLIFF    ilk 3 sn'de %30-50 düşüş  → erişim ölür     (S0 hatası)
  HUMP     ortada %60+ tutar         → yüksek paylaşım
  PLATEAU  %70+ düz + loop dostu son → algoritma favorisi (hedef bu)
```

**Sonuç:** İlk iki sahne aynı işin iki kopyası değil, iki AYRI işin
sahibidir:

```
S0 = KARAR SAHNESİ       kaydırma kararını kazanır      (0-8 sn)
S1 = TIRMANDIRMA SAHNESİ hayatta kalanı 10-30'a taşır   (8-16/20 sn)
```

Aynı işi iki kez yapan iki sahne = ikinci düşüş dalgası. Serinin kanca
platosunun (5-6) en olası sebebi S1'in hiç tanımlanmamış olmasıydı.

---

# 2. 🎬 S0 — KARAR SAHNESİ: dört kilit

## 2.1 · 0. KARE SINAVI

Hook'un İLK karesi tek başına scroll durdurmalı — reveal'siz ama
kompozisyonu "yanlış" hissettiren bir kare (ölçek, boşluk, simetri).
"Adam yürüyor" 0. kare olamaz.

```
ÖRÜNTÜ KESİNTİSİ FORMÜLÜ: tek güçlü görsel fikir + tek anlam ipucu.
  İki fikir üst üste = sıfır fikir. Yüksek kontrast, net odak noktası.

120 PX TESTİ: 0. kare, Shorts feed'inde fiilen KAPAKTIR. Kapak
  mimarisinin posta pulu testi buraya da uygulanır: 120 px'te
  yüz/anomali/ölçek okunmuyorsa 0. kare geçmez.
```

## 2.2 · HAREKETİN ORTASINDA AÇILIŞ

Video, hareketin ORTASINDA açılır — asla poz, statik kare veya kurulum
karesiyle değil. Duran görüntü "bitti" sinyalidir ve kaydırtır. Cold open
kuralı: sahne, izleyici geldiğinde ÇOKTAN başlamış olmalı; izleyici
yetişmeye çalışırken bağlanır.

```
PROMPT KARŞILIĞI: S0'ın ilk cümlesi süren bir eylemi tarif eder
("mid-stride", "already reaching", "halfway through") — eylemin
başlangıcı kadraj öncesinde kalır. Bu, loop kuralının (§5②
SENARYO_VE_VIRAL) açılıştaki aynasıdır: son kare durmaz, ilk kare
başlamaz — ikisi de AKIŞIN İÇİNDEDİR.
```

## 2.3 · MERAK BANDI = KISMİ BİLGİ BANDI

Loewenstein: merak, bilgi BOŞLUĞUNDAN doğar — ve boşluk ancak kısmi
bilgiyle hissedilir. Kısmi bilgi, tam bilgisizlikten daha fazla merak
üretir. Bu yüzden zamanlama yasasının "0-2 sn merak (normal görünüm)"
bandı PASİF BEKLEME DEĞİLDİR:

```
0-2 sn = kadraj normal + TEK öğe yanlış. İzleyici neyin eksik/yanlış
olduğunu tam bilemez ama BİR ŞEYİN yanlış olduğunu bilir. Tamamen
normal iki saniye = boşa harcanmış karar penceresi (karar 1,7 sn'de
veriliyor).
```

## 2.4 · REVEAL İKİLİ KİLİTLE GİRER [Ders 71]

Reveal, kadraj dışı → kadraj içi ikili kilidiyle girer. Sis / mesafe /
flu / yoğunluk perdesi YASAK — model analog perde tutmuyor; perde
arkasındaki nesne fiilen 0:00'da reveal olmuş sayılır. I2V'de start
frame reveal'siz kilitlenir.

## 2.5 · S0 kapıları

```
□ 3. SANİYE KONTROLÜ: 0:03'te ekranda ilk kareden FARKLI bir bilgi
  var mı? Yoksa ipucu beat'i gecikmiş demektir — hook yeniden yazılır.
□ S0 ÇIKIŞ TESTİ: sahne bittiğinde izleyicinin KELİMELERLE sorabildiği
  ama cevaplayamadığı bir soru oluştu mu? Soru cümlesi PLANA yazılır.
  Cümle yazılamıyorsa hook yoktur.
```

> Zamanlama yasasının sayıları (0-2 merak → 2-5 ipucu → 5-7 reveal →
> 7-8 tutulan kare) format kartında ve SHORTS_QA §C'de durur; bu bölüm
> sayıların MEKANİZMASINI anlatır. Yatayda aynı yasa S0'ın 10 saniyesine
> orantıyla yayılır (reveal ~6-8. sn bandı).

---

# 3. 📈 S1 — TIRMANDIRMA SAHNESİ

> Serinin en büyük tanımsız alanı buydu. S1'in görevi cevap vermek
> DEĞİLDİR — açık döngüyü (open loop) BÜYÜTMEKTİR. Açık döngü ortalama
> izlenme süresini %40-60 artırır; erken kapanan döngü izleyiciyi
> bırakır, hiç beslenmeyen döngü de bırakır.

```
① İKİNCİ BİLGİ ZORUNLU
   S1, S0'ın sorusuna cevap VERMEYEN ama soruyu BÜYÜTEN tam bir yeni
   bilgi taşır: ölçek büyür, sayı artar, yön değişir, ikinci bir öğe
   girer. 0:08-0:16 bandında yeni bilgi yoksa izleyici 3→10 sn
   zincirinin %35'lik kaybına düşer.

② CEVAP YASAĞI + GÜVEN KURALI
   Reveal'in AÇIKLAMASI finale kadar kapanmaz. Ama yapay geciktirme
   güven cezası doğurur — izleyici "cevap bilerek saklanıyor" hissini
   cezalandırır. Çözüm bilgi eşitliği: KARAKTER DE BİLMİYOR olmalı.
   Karakterin bildiğini izleyiciden saklamak clickbait'tir; karakterle
   izleyicinin aynı anda öğrenmesi dramaturjidir.
   ⭐ 27.08.2026 — SUİSTİMAL EŞİĞİ ÖLÇÜLDÜ: yapay geciktirme 25.
   saniyede güven cezasına çarpıyor; o saniyeden sonra izleyici kancayı
   "izlenme süresi çalma" olarak okuyup terk ediyor. Bilgi eşitliği bu
   eşiği dakikalarca öteliyor — kuralın gerekçesi artık sayıyla duruyor.
   ⚠️ AMA BİLGİ EŞİTLİĞİ TEK ARAÇ DEĞİL — bkz. §3.1.

③ KARAKTER EYLEM HÂLİNDE
   S1 bir tepki sahnesi değildir (bakakalma yasak). Karakter meslek
   refleksiyle DOĞRULAMA eylemi yapar: ölçer, kontrol eder, yaklaşır,
   aleti çevirir. (Vuruş tablosundaki "tartışma" beat'inin karşılığı —
   kamera-taşıyıcı testi burada da geçerli.)
```

```
S1 ÇIKIŞ TESTİ: S1'in sonunda (0:16 shorts / ~0:20 yatay) izleyicinin
sorusu DEĞİŞMİŞ ya da BÜYÜMÜŞ mü? Soru aynen duruyorsa S1 bir tekrar
sahnesidir — yeniden yazılır.

YATAY EK KAPISI: katalizör 0:15'i geçemez (vuruş tablosu §2.2) —
katalizör S1'in içinde ya da sonunda patlar, S2'ye sarkmaz.
```

---

## 3.1 ⭐ İKİ AYRI ARAÇ: BİLGİ EŞİTLİĞİ ve DRAMATİK İRONİ

> **Eklendi 27.08.2026 (araştırma 3).** Depo bugüne kadar bu ikisini tek
> araç sandı ve yalnız birincisini kullandı: **16 dikey filmin 16'sı da
> bilgi eşitliği filmidir.** İkisi zıt değil, farklı iş yapar — ve
> ikincisi deponun kanca platosunun (5-6, §0③) en olası açıklamasıdır.

**Ölçüm:** Cabañas, Senju & Smith (2023), *Frontiers in Psychology*, N=42.
Dramatik ironi sahneleri göz izleme, fMRI ve deri iletkenliğiyle ölçüldü.
Bulgu: **karakter sakinliğini korudukça izleyicinin fizyolojik uyarımı
PARABOLİK olarak artıyor.** Tetikleyen mekanizma Spontan Zihin Kuramı
(SToM): izleyici karakterin bilmediğini fark ettiği anda gerilim doğuyor.

```
┌─ BİLGİ EŞİTLİĞİ ─────────────  karakter de bilmiyor
│  SATIN ALDIĞI     güven · ortak keşif · 25 sn Zeigarnik eşiğinin
│                   dakikalara uzaması
│  KORUDUĞU         izleyicinin "kandırılmıyorum" hissi
│  ZAYIF YANI       bahis yok → orta bölümü tek başına taşıyamaz
│
└─ DRAMATİK İRONİ ────────────  İZLEYİCİ biliyor, karakter bilmiyor
   SATIN ALDIĞI     orta bölüm tutundurması · parabolik fizyolojik gerilim
   KORUDUĞU         karakterin sakinliği — panik yasağı MEKANİZMANIN
                    KENDİSİDİR, engeli değil [SHORTS_SISTEM_PROMPTU md.5]
   BEDELİ           reveal erken harcanır; açık döngü "bu ne?"den
                    "ne zaman görecek?"e döner — ve o sorunun SÜRESİ var
```

### Hangisi ne zaman

```
S0-S1'de   BİLGİ EŞİTLİĞİ  → soru kurulur, güven kurulur (② aynen geçerli)
S2-S4'te   DRAMATİK İRONİ  → izleyiciye karakterin göremediği bir şey verilir
```

⚠️ **İkisi aynı anda aynı nesne üstünde çalışmaz.** İroni ikinci bir
nesne/olgu üstünden kurulur: karakterin çözmeye çalıştığı şey değil, onu
çözerken FARK ETMEDİĞİ şey.

### Metinsiz, diyalogsuz, lockoff bir kadrajda ironi nasıl kurulur

Depo kısıtları (0 metin · 0 replik · 1 sabit çekim · vizör kilidi) ironiyi
yasaklamaz — **sadece kadrajın karakterin görüş alanından GENİŞ olmasını
şart koşar.** Beş meşru taşıyıcı:

```
① ARKA PLAN OKUR       değişim karakterin ARKASINDA/ÜSTÜNDE; kask periferi
                       kapatıyor. Kamera görüyor, o görmüyor.
② ZEMİN OKUR           karakterin BASTIĞI yüzeyin altında/içinde bir şey
                       (Open Seam'in berrak buzu bunun hazır zeminidir)
③ VİZÖR TERSİNE ÇALIŞIR  yansıma izleyiciye bilgi verir; karakter yansımaya
                       değil ileriye bakıyor [DIKEY_MIKRO_DRAMA §4]
④ CETVEL İZLEYİCİDE    ölçek/mesafe/saat kadrajda okunur, karakterin
                       aletinde okunmaz — ölçüyü izleyici yapar
⑤ BEDEN DİLİ GECİKMESİ  karakter hâlâ önceki duruma göre davranıyor;
                       gecikme kinesik komutla yazılır [§4 kinesik dil]
```

```
SAYISAL KİLİT — dramatik ironi kullanan planda
  □ ASİMETRİ ANI     hangi saniyede izleyici karakterden ÖNE geçiyor
  □ TAŞIYICI         yukarıdaki beşten hangisi (tek tane — ikisi bölünür)
  □ KAPANIŞ          karakter hangi sahnede öğreniyor; öğrenmiyorsa
                     bunun bilinçli olduğu ve neyi satın aldığı yazılır
  □ SAKİNLİK KORUNUR  karakterin paniklediği kare sayısı = 0 (mekanizma
                     karakterin sakinliğidir — panik ironiyi ÇÖZER)
```

### Neden bu bölüm yazıldı — bahissiz huşunun eğrisi

⚠️ **Kaynaksız ama mekanik olarak tutarlı bulgu (araştırma 3):** bahis ya
da görünür saat taşımayan saf huşu/saf merak içeriğinin tutundurma eğrisi
**8-12. saniyede uçurum** yapıyor; görünür bir geri sayım/tehdit taşıyan
içerik ise kademeli düşüşle **25-30. saniyeye** kadar taşıyor.

> Deponun ızgarası 6 × 8 s. Bu sayı doğruysa uçurum **tam S0/S1 sınırına**
> düşüyor — ve dikey hattın ölçülmüş en düşük hikâye skoru (Wrong Shadow
> 3.0, Tutundurma 3) ile kanca platosu bununla hizalanıyor. Hizalanma
> kanıt değildir; sayı ilk gerçek retention eğrisiyle sınanacaktır (§0①).

### Plana yazılan satır

```
BİLGİ ASİMETRİSİ: [YOK / DRAMATİK İRONİ · taşıyıcı ① - ⑤ · asimetri anı 0:XX]
```

Satır **zorunludur**; "YOK" yazmak meşru bir karardır ama yazılmamış olması
değildir — çünkü depo 16 filmde 16 kez farkında olmadan "YOK" yazdı.

---

# 4. 🗂️ HOOK TİPOLOJİSİ — plana "HOOK TİPİ" satırı yazılır

> Şimdiye kadar tüm filmler tek hook tipini (görsel reveal) varsaydı.
> Tip seçimi bilinçli bir plan kararıdır ve plana yazılır. Bir S0'da
> TEK tip kullanılır — iki tipi üst üste bindirmek ikisini de öldürür.
> §2.2'deki "hareketin ortasında açılış" tip değil ZEMİNDİR: her tipin
> altında zorunludur.

| Tip | Mekanizma | En iyi format/tür | Risk |
|---|---|---|---|
| **Ölçek şoku** | Tanıdık nesne + imkansız ölçek AYNI karede | Dikeyin doğal silahı (karakter alt 1/3, kozmik ölçek üst 2/3) | Model ölçeği şişirir → oran SAYIYLA yazılır ("the object spans 40× her height") |
| **Yanlışlık kompozisyonu** | Tamamen normal sahne + TEK anormal öğe; beyin tamamlamak için durur | Günümüz-Dünya konseptleri (Winter Line, Wrong Shadow sınıfı) | ⚠️ Anomali türetilmiş fenomense (gölge, yansıma) [D73]: tek-kare fizibilite kapısı ŞART — novum render edilmezse hook doğmaz |
| **In medias res** | Olay ortasından açılış; kurulum yok, bağlam sonradan | Aksiyon konseptleri (Quiet Impact sınıfı), yatay 2-4 dk | Bağlam borcu birikir — S1'deki ikinci bilgi bağlam TAKSİDİ olarak tasarlanır |
| **Yetkinlik / süreç** | Karakter alışılmadık bir işi ustalıkla yaparken açılır → "bu ne işi?" | Keşif filmleri (Unbroken City, Starless Circle sınıfı) | En yavaş tip — 0. kare sınavını İŞİN tuhaflığı geçmek zorunda, karakterin değil |
| **Ses-önce** | Görüntü sakin, ses "yanlış" — ya da mutlak sessizlik | Diyaloglu/AI sesli filmler, gece konseptleri | Sessiz izlenen feed'de görsel zemin tek başına ayakta kalmalı (§5) |

---

# 5. 🔊 İLK 2 SANİYENİN SESİ

> Hiçbir kılavuz bu ekseni tasarlamıyordu; scroll durduran şeyin yarısı
> sestir. Hook sesi PLANA yazılır ve müzik kılavuzuyla birlikte karara
> bağlanır (`GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §10 müziksiz sahne ·
> §14 spotting).

```
① MÜZİK 0:00'DA GİRMEZ. İlk 1-2 saniye ya TEK diegetik ses taşır
   (adım, rüzgar, telsiz cızırtısı, metal gıcırtısı) ya da MUTLAK
   SESSİZLİK. Müzik en erken ipucu beat'inde (2-5 sn) girer.
② GÖRÜNTÜ-SES UYUŞMAZLIĞI meşru kancadır: normal görüntü + yanlış ses,
   "yanlışlık kompozisyonu"nun işitsel ikizidir.
③ MUTLAK SESSİZLİK de örüntü kesintisidir — feed gürültülüdür, iki
   saniyelik gerçek sessizlik durdurur. (Sessizlik kararı da plana
   yazılır; yazılmamış sessizlik eksik miks sanılır.)
④ TELEFON HOPARLÖRÜ: sub-bass tek başına duyulmaz — hook sesi 90 Hz
   üstü bir taşıyıcı ister (müzik kılavuzu §15.1 ile aynı kural).
   ⭐ 27.08.2026 — SAYI VE TEKNİK: telefon sürücüsü 150 Hz altını
   fiziksel olarak üretmiyor; sinematik etki için konan 20-60 Hz
   vuruşlar telefonda YOK hükmünde ve vuruculuk ~%40 düşüyor.
   Çözüm MISSING FUNDAMENTAL: üretilemeyen temelin üst armonikleri
   (50 Hz için 100/150/200 Hz) sese yoğun biçimde eklenir; beyin
   duymadığı temeli "duyduğunu" varsayar. Tam uygulama:
   GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU §15.1.

⑥ SESSİZ İZLEME PAYI ÖLÇÜLDÜ: akış içi videoların ~%85'i sessiz
   başlıyor (Manchester Digital 2025-26); TikTok istisna — orada
   ses açık oranı %93 bandında. Yani ses tasarımı bu seride
   İKİNCİ kanaldır, birinci değil: anlam sessiz okunmalı
   [DIKEY_MIKRO_DRAMA §4], ses açık izleyici için ÜSTÜNE kurulur.
   ⚠️ Erken müzik girişi ölçülen en kötü seçenek: uzun enstrümantal
   giriş (intro buildup) izleyiciye "reklam" sinyali veriyor ve
   3. saniyeden önce kaydırtıyor. Sıralama: tek diegetik ses >
   mutlak sessizlik > erken müzik.
⑤ FEDA DENGESİ: metin kancası yasak olduğu için (bkz. §0-②) sesin
   kanca yükü bu seride ortalamadan BÜYÜKTÜR. Sessiz filmde bile ilk
   2 saniyenin ses tasarımı "yok" değil "bilinçli sessizlik" olmalı.
```

---

# 6. 🤝 VAAT-TESLİM + LOOP BAĞLANTISI

```
① VAAT-TESLİM SÖZLEŞMESİ: Hook'taki soru ile kapanış imajı aynı
   cümlenin iki yarısıdır — değilse ya hook ya final yanlıştır.
   (Açılış-kapanış çifti kuralıyla birlikte çalışır:
   SENARYO_VE_VIRAL_KAMERA §2.3-③.)
② PAKETLEME SÖZLEŞMESİ: başlık/kapak neyi vaat ediyorsa ilk 5 saniye
   ONU teslim eder. Clickbait açığı erken terk üretir ve algoritmik
   cezadır — VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md ile ÇİFT YÖNLÜ kontrol:
   paket hook'a, hook pakete bakılarak yazılır.
③ LOOP: 31 Mart 2025'ten beri her tekrar izleme ayrı view; en güçlü
   sinyal ilk turda tam izlenme + rewatch. S0 aynı zamanda DÖNÜŞ
   KARESİDİR: 0. kare tasarımı loop satırıyla (SENARYO_VE_VIRAL §5)
   AYNI kararda verilir — son sahnenin çıkışı S0'ın girişine akar.
```

---

# 7. 🏭 HOOK-ÖNCE ÜRETİM KAPISI

> Deponun kanıtlı ilkesine ("üretim en pahalı/riskli sahneden başlar")
> ikinci kapı. Hook, filmin EN UCUZ test edilebilir sahnesidir: 6-10
> saniyelik tek klip.

```
SIRA:
1. Doruk / risk kapısı sahneleri temiz çıkar (mevcut kural)
2. S0, 2-3 FARKLI hook-tipi varyantıyla üretilir (aynı konsept,
   §4 tablosundan farklı tipler)
3. En iyi varyant seçilir, filmin geri kalanı ONA kilitlenir
   (ışık/kadraj/hareket sürekliliği S0'dan türer)
4. Varyantlar ve seçim gerekçesi film dosyasının üretim notlarına
   yazılır — hangi tip hangi konseptte tuttu, zamanla serinin kendi
   verisi olur (§0-① revizyonunun iç kaynağı)
```

---

# 8. ✅ PLAN KONTROLÜ — bu kılavuzun 7 maddesi

> `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §7 listesinin hook maddesinin
> yerine geçer; diğer maddeler orada kalır.

```
□ HOOK TİPİ satırı planda mı — tek tip mi? (§4)
□ S0 soru cümlesi plana YAZILDI mı? (§2.5)
□ 0. kare tarifi: örüntü kesintisi + süren hareket + 120 px
  okunurluğu (§2.1-2.2)
  ⛔ 120 px testi artık TEK yük taşıyıcıdır (§0②) ve GÖZLE değil
     MAKİNEYLE koşulur: kare 120 px'e indirilir, kontrast/entropi
     ölçülür. Koşulmadıysa madde işaretlenmez.
□ Reveal ikili kilitte mi [D71]; 0:03'te yeni bilgi var mı? (§2.4-2.5)
□ S1'in İKİNCİ BİLGİSİ tanımlı mı; S1 sonunda soru değişiyor mu —
  yatayda katalizör ≤0:15 mi? (§3)
□ ⭐ BİLGİ ASİMETRİSİ satırı yazıldı mı (§3.1)?
  [YOK / DRAMATİK İRONİ · taşıyıcı ①-⑤ · asimetri anı 0:XX]
  "YOK" meşru karardır; yazılmamış olması değildir.
□ İlk 2 sn ses kararı yazılı mı (diegetik tek ses / bilinçli
  sessizlik)? Erken müzik girişi elendi mi? (§5)
□ Hook sorusu ↔ kapanış imajı çifti kuruldu mu; S0, loop satırıyla
  tutarlı mı? (§6)
```

---

# 9. 🔗 KAYNAKLAR (09.08.2026 araştırması)

```
PLATFORM VERİSİ
  opus.pro/blog/youtube-shorts-hook-formulas — 3 sn tutundurma eşikleri
  aibrify.com/blog/youtube-shorts-retention-curve-playbook — eğri şekilleri
  humbleandbrag.com/blog/youtube-audience-retention-benchmarks — bantlar
  dynamoi.com — TikTok 3 saniye kuralı, %70 eşiği
  insights.ttsvibes.com — %71 karar, 2,8× fark
  retentionrabbit.com — 2025 uzun form intro benchmark (+%58)
  socialchamp.com · fliki.ai — Shorts algoritması 2026, loop/view kuralı
  virvid.ai — looping structure, retention graph okuma

PSİKOLOJİ / SENARYO
  cmu.edu (Golman & Loewenstein) — bilgi boşluğu kuramı
  sciencedirect.com — merakın nörobilimi
  masterclass.com · studiobinder.com — cold open teknikleri
  socialync.io — hook/body/payoff, open loop yapısı
  cloudixdigital.com · greenfroglabs.com — görsel kanca kalıpları
```
