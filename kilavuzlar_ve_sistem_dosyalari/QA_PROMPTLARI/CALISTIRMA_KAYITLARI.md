# 📒 QA RUBRİKLERİ — ÇALIŞTIRMA KAYITLARI VE OPERATÖR DİPNOTLARI

> **Bu dosya nedir:** Rubrik dosyaları 12.08.2026'da SALT PROMPT hâline
> getirildi — bir rubrik .md'si + film, rapor almak için yeterli olmalı ve
> dosyaya Türkçe operatör tarihi karışmamalı. Rubriklerin sonunda biriken
> ders dipnotları ve çalıştırma kayıtları OLDUĞU GİBİ buraya taşındı.
>
> **Yeni kayıt nereye yazılır:** Buraya, ilgili rubriğin bölümünün SONUNA.
> Kart G adım 5'in "kaynak rubriğin dipnotuna yaz" adımı artık bu dosyayı
> hedefler. Rubrik gövdesine ders yaması yazmaya devam edilir (İngilizce,
> kural olarak); tarih/tutanak buraya gelir.
>
> Format: `> 🔎 **DERS <n> (<tarih> · <FİLM>):** ...` ve
> `> Çalıştırma kaydı: N kez çalıştırıldı · son <tarih> · sonuç <özet>`

> **17.08.2026 — SALT-PROMPT TEMİZLİĞİ.** Altı rubriğin gövdesinden
> `[DERS n]` / `[LESSON n]` etiketleri, tarihler, film adları, depo yolları
> ve koşu anlatıları çıkarıldı; kuralların hepsi yerinde kaldı. Sebep:
> operatör videonun yanında yalnızca rubriği veriyor, modelin göremediği
> bir derse yapılan atıf ona doldurulacak bir boşluk gibi görünüyordu.
> Bunun tek bedeli `grep -L "DERS <n>" *_CRITIQUE_PROMPT.md` doğrulamasının
> artık çalışmamasıdır; yerine aşağıdaki iz defteri geçti.

---

# ⭐⭐ 22.08.2026 — ALTI MERCEK DÖRDE İNDİ

> **Eksen değişti: konu değil ZAMAN.** Kusuru söylemek için kaç sahneye
> bakman gerekiyor? Bir sahne → ①. İki sahne → ②. Film boyu → ③ (ses) ve
> ④ (anlatı). Bu eksen depoda zaten vardı: 7-9 dk hattı aynı problemi
> 3 geçişli bir sistemle çözmüş ve MANTIK+KARAKTER'i tek geçişte,
> SENARYO+SES'i tek geçişte birleştirmişti.

```
ÖNCE  6 rubrik · 62 kategori yuvası · 4.266 satır
SONRA 4 rubrik · 45 kategori yuvası
      ① KARE       11 + 3 dikey anahtar
      ② DEVAMLILIK 13   (gövde 1-6 · dünya 7-13)
      ③ SES         9
      ④ HİKAYE     10
```

**Kaybolan kategori yok, kaybolan KOPYA var.** SHORTS_QA'nın 16
kategorisinin 13'ü ölçüm öncesi taramada başka bir rubriğin aynısı çıktı:
1-8 birebir VIDEO_QA · 12 negatif · 13 mantık · 14-15 senaryo · 16 ses.
Gerçekten özgün olan üçü — 9:16 kadraj, güvenli alan, kanca zamanlaması —
üçü de tek kareden okunur, yani KARE düzeyi ölçümdür. Bu yüzden dikey
artık ayrı rubrik değil, ① ve ④ içinde bir **FORMAT ANAHTARI**.

**② birleşmesi neden tuttu:** sınır kuralı zaten yazılıydı — *"üzerindeyse
karakter, dünyaya aitse dünya"*. Birleşmede o kural bir NOT'tan YAPIYA
döndü: gövde 1-6, dünya 7-13, ve aynı tozlu kol iki kez faturalanamıyor.

**En büyük davranış değişikliği:** karakter ve ses artık OPSİYONEL DEĞİL.
Eskiden öyleydiler ve bedeli sayıyla ölçülebilir — 34 film kaydının yalnız
5'inde ses raporu, 10'unda karakter raporu vardı.

**Taşınan yerler:**
```
6 rubrik        → ARSIV_6_MERCEK/ (silinmedi: 83 ham rapor onlarla üretildi
                  ve ancak kendi metinleriyle okunabilirler)
5 skor tablosu  → ⛔ KAPALI (03 · 04 · 05 · 06 · 07)
LESSONS teknik  → ⛔ KAPALI  (kendi kusuru da gerekçenin parçası: başlığı
                  "11 kategori" diyordu, 7 sütun taşıyordu)
4 yeni tablo    → T1_KARE · T2_DEVAMLILIK · T3_SES · T4_HIKAYE (boş açıldı)
tamlık matrisi  → payda 3 → 4, ③ SES sütunu eklendi
AGENTS kartları → C=① · E=② (E2 yutuldu) · E3=③ · D=④
```

⛔ **Eski ve yeni skorlar KARŞILAŞTIRILAMAZ.** Kategori sayısı, kategori
sınırları ve ortalamanın paydası değişti. Matristeki her dolu hücre
arşivlenmiş bir aletin ölçümüdür; ② sütunundaki ✅'ler ise yalnız dünya
yarısının ölçümüdür — gövde yarısı hiç ölçülmemiştir.

⛔ **HİÇBİR FİLM HENÜZ 4/4 DEĞİL.** Dört merceğin hiçbiri henüz hiçbir
filme koşulmadı. Sistem yazıldı, sınanmadı — ilk koşu bunu değiştirir ve
② DEVAMLILIK'in rapor uzunluğu riski (sahne envanteri + karakter pasaportu
aynı çıktıda) ancak orada ölçülür.

---

# ⭐ 22.08.2026 — ORTAK ÇEKİRDEK: SEKİZ KAPI, ALTI RUBRİKTE BİREBİR AYNI

> **Neden:** Kapılar altı rubriğe rastgele dağılmıştı. Ölçüm öncesi tarama:
> MEDIA GATE yalnız VIDEO'da (README onu "yaşayan üç durdurucudan biri"
> sayıyordu) · CUTS COUNTED SHORTS'ta yok · DECLARED ABSENCE VIDEO ve
> MANTIK'ta yok · ARITHMETIC GATE yalnız SHORTS'ta · SCORES SUMMARY ④
> SENARYO'da yok · kapsam sınırı (NOT IN THIS PASS) VIDEO ve SHORTS'ta
> HİÇ YOK — yani en çok kategori taşıyan iki mercek (11 ve 16) başkasının
> kusurunu kendine yazmasını engelleyen bloktan yoksundu.
>
> **Yapılan:** Aşağıdaki sekiz parça kanonik metin hâline getirildi ve
> altı rubriğe BİREBİR AYNI sözcüklerle yayıldı. Bundan sonra yeni ders
> çekirdeğe bir kez yazılır, altı kopyaya birlikte iner.

```
① STEP −2 MEDIA GATE            ← VIDEO'nun sürümü kanonik alındı,
                                  5 rubriğe eklendi (SES'in kısa kuralı
                                  tam kapıya yükseldi)
② CUTS COUNTED zorlama          ← SHORTS ve SENARYO'ya eklendi
③ DECLARED ABSENCE              ← VIDEO ve MANTIK'a eklendi
④ ARITHMETIC GATE (3 sayı)      ← SHORTS'un sürümü kanonik, 5 rubriğe
⑤ SCORES SUMMARY ④              ← SENARYO'ya eklendi
⑥ NOT IN THIS PASS + sınır      ← VIDEO ve SHORTS'a YAZILDI (yeni metin)
⑦ OUT-OF-SCOPE sonuç bloğu      ← VIDEO, SHORTS, SENARYO'ya
⑧ OUT-OF-SCOPE FLAGS çıktısı    ← VIDEO, SHORTS, SENARYO'ya
```

**Aynı turda kapatılan üç çelişki:**

```
🔧 SENARYO — DOKUZ MU ON MU
   Kategori 6 sessiz filmde "dokuz kategori üzerinden ortalama" diyordu,
   tracking row "on kategori skorunun ortalaması" diyordu. Tabloda N/A'lı
   üç satır zaten vardı (Kaleida · Unbroken City · Wrong Shadow) ve hangi
   paydayla hesaplandıkları belirsizdi. İkisi de tek kurala bağlandı:
   sayı taşıyan kategoriler, N/A ortalamanın DIŞINDA, sıfır sayılmaz.

🔧 VIDEO — NEGATİF İHLAL ORTALAMAYA GİRİYORDU
   `Negative Violations | __count` bir SAYI hücresi, ④ ise "sayı taşıyan
   kategorilerin ortalaması" diyor. 4 ihlal, 4/10 gibi ortalamaya
   girebiliyordu. Açıkça ortalama dışına alındı.

🔧 VIDEO — TABLO SATIRI 11 KATEGORİDEN 7'SİNİ TAŞIYORDU
   Parçacık · Diyalog-Ses · Kare Çapası · Negatif İhlal operatör tablosuna
   hiç ulaşmıyordu. SHORTS'taki VERBATIM sütun kapısı buraya da kondu ve
   satır 11 kategoriye tamamlandı.
   ⛔ AÇIK BORÇ: LESSONS_LEARNED · KALİTE TAKİP tablosu hâlâ 7 sütunlu ve
      başlığında "VIDEO_QA · 11 kategori" yazıyor. Bu tablo 4 mercek
      birleşmesinde T1_KARE_KALITE'ye devredilecek; o güne kadar fazla
      hücreler ham raporda durur.
```

**Ölü işaretçi temizliği:** MANTIK ve KARAKTER'in kapsam listesi ile
RING LIGHT'ın OUT-OF-SCOPE bloğu hâlâ `→ KAPAK_QA`'ya yönlendiriyordu;
o rubrik 12.08.2026'da kaldırılmıştı. Üçü de "elle kontrol edilir, rubriği
yok" ile değiştirildi.

**Bu bir hazırlıktır.** Sıradaki adım altı merceğin DÖRDE indirilmesi
(① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE); ortak çekirdek o birleşmenin
önkoşuluydu. Karar kaydı: eski skor tabloları (03 · 04 · 05 · 06 · 07)
DONDURULACAK, dört yeni tablo boş açılacak.

---

# ⭐⭐ 24.08.2026 — DÖRT MERCEĞİN İLK KOŞUSU: THE BORROWED WEIGHT

> 22.08 notu "dört merceğin hiçbiri henüz hiçbir filme koşulmadı" diyordu.
> Bu, o ilk koşudur — ve sistem sınandığı ilk günde **kendi kapısından
> düştü.** Tam kayıt: `../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_BORROWED_WEIGHT.md`

```
MALZEME  teslim kurgusu · 264 s (② ③) / 266 s (① ④)
MOD      dördü de V — SPEC AYRI DOSYA olarak hazırdı, hiçbirine verilmedi
         → D94/D117'nin YEDİNCİ vakası
OTURUM   ⬜ kayıtsız — ayrı oturum olup olmadığı bilinmiyor [D110]
SONUÇ    ⑤ ÇAPRAZ SAYIM 🚨 GEÇERSİZ · dört skor satırının dördü de
         T1-T4'e YAZILMADI · 00_INDEX matrisinde dört hücre ❌ kaldı
```

> 🔎 **① 1_KARE (24.08 · THE BORROWED WEIGHT):** ilk koşu. 26 kesme saydı,
> künyeyi doğru doldurdu, aritmetiği kendi tablosuyla tuttu (7.0 = 56÷8).
> İki kusuru: severity tally 🔴5 diyor, kendi kütüğünde 🔴6 var (skor
> aritmetiği rubriğe yazıldı [D119], **severity aritmetiği yazılmadı** —
> ve verdict'i o sayı sürüyor); kategori 8'i sessiz bir filmde başlık
> kartıyla 5/10'a indirdi (yokluk `N/A` olmalıydı [D113]). ⭐ En değerli
> çıktısı skor değil, PRESENCE STRING'i oldu — ② ile birlikte kurgunun
> fazla ve eksik kliplerini buldu (**DERS 121**).
> Çalıştırma kaydı: 1 kez çalıştırıldı · son 24.08.2026 · sonuç ⚠️ ön koşu,
> parti geçersiz.

> 🔎 **② 2_DEVAMLILIK (24.08 · THE BORROWED WEIGHT):** ilk koşu; 22.08'de
> yazılan "rapor uzunluğu riski" gerçekleşmedi, 13 kategori de doldu.
> Ama **D119'un birinci tekrarı burada çıktı**: dört hücre "no in-scope
> source" yazıp aynı satıra 7/10 koydu; rubriğin gövdesinde D119 yaması
> kelimesi kelimesine duruyor. Yazdığı 4.9 yerine kendi tablosu 6.0 veriyor
> — 1.1 puan. İkinci kusur: sahne haritası 3:59'da bitiyor, künyesi 4:24
> diyor; 25 saniye haritasız kaldı ve bunu hiçbir kapı sormuyordu.
> Çalıştırma kaydı: 1 kez çalıştırıldı · son 24.08.2026 · sonuç 🚨 parti
> geçersiz + D119 tekrarı.

> 🔎 **③ 3_SES (24.08 · THE BORROWED WEIGHT):** ilk koşu ve **en ağır
> ders bu mercekten çıktı.** Filmin dört MACHINE repliğinden ikisini hiç
> duymadı, duyduğu ikisini de yanlış yazdı ("The weight is all we have
> left." — gerçek satır "Beacon signal confirmed. Range: three hundred
> metres."). Register'ı HUMAN okuyup "sentetik duruyor" bulgusuyla
> Sentetik hücresini 4/10'a indirdi → kart E3 adım 2 bulguyu DÜŞÜRDÜ
> (bu adım atlansaydı rubrik çalışan tasarımı bozmaya yönlendirecekti).
> Turn-Taking'e tek ses bildirip puan verdi (N/A olmalıydı).
> ⭐ Buna karşılık **aynı repliğin 0:23 ve 0:33'te — tam bir yuva arayla —
> duyulduğunu kaydetti**; duplike klibin tek kanıtı bu satır oldu (D121).
> Çalıştırma kaydı: 1 kez çalıştırıldı · son 24.08.2026 · sonuç 🚨 parti
> geçersiz + defter iki eksende hatalı.

> 🔎 **④ 4_HIKAYE (24.08 · THE BORROWED WEIGHT):** ilk koşu; partinin
> AYKIRI raporu. 25 kesme sayıp 11 sahne haritası yazdı — rubriğin kendi
> bölme kuralının ihlali, ve şeridini kullanılamaz kıldı. Yanan başlık
> kartından film adını okudu (`FILM: THE BORROWED WEIGHT`) — yasak alanın
> KENDİ SATIRINDA yazılı, yine ihlal edildi → **D105/D65 tekrarı**.
> ⭐ Ama üç MACHINE repliği neredeyse birebir alıntıladı ("Cumulative load
> 1.1 tons", "Cargo secured") — ③'ün kaçırdıklarını bu rapor duydu ve
> kurgunun kuyruk aritmetiği bu alıntılarla kapandı (D121).
> ⛔ "Düz duygu yayı · kriz yok · bedeli düşük final" okuması, planın S24
> TWIST finali kurguda görünmediği için üretildi: rapor olmayan bir finali
> eleştirdi. Kesme listesi ve REWRITE reçeteleri UYGULANMAZ.
> Çalıştırma kaydı: 1 kez çalıştırıldı · son 24.08.2026 · sonuç 🚨 parti
> geçersiz + D105 tekrarı.

⭐ **Partinin net kazancı:** dört geçersiz skor, üç yeni ders (D120 · D121 ·
D122), bir düzeltilmiş yazım paketi (planın replik çizelgesi) ve **teslim
kurgusunun master açılmadan yeniden kurulması** — 26 yuva, ilk perdede +3
fazla klip, kuyrukta −2 eksik sahne, sonda yasaklı başlık kartı.

---

# 🔬 24.08.2026 — DERİN TARAMA SINIFI: ⑤ ARKA PLAN + ⑥ FİZİK YAZILDI

> Dört mercekli sisteme iki KONU merceği eklendi — payda /4'e DOKUNMADAN.
> Karar mekanizması ve koşu tetikleyicileri: `00_README.md` derin tarama
> bölümü. Görev kartları: AGENTS.md **F** ve **F2**. Skor tabloları:
> `../FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` · `T6_FIZIK_KALITE.md`.

```
NEDEN AYRI SINIF   22.08'in ayrım ekseni ZAMAN'dı (kusur kaç sahneden
                   okunur); bu ikisi o eksene oturmuyor. ⑤ zaman ekseninin
                   ikisini birden tarar ama yalnız ÖZNE-DIŞI alanda;
                   ⑥ her yerde ama yalnız SAYI taşıyan bulguda. Beşinci
                   zorunlu mercek yapmak 6→4 kararını geri almak olurdu;
                   opsiyonel bırakıp paydaya sokmamak yetmezdi (eski
                   sistemin ölçülmüş dersi: opsiyonel koşulmaz — 34 kaydın
                   5'inde ses vardı). Çözüm: RİSK TETİKLİ sınıf — koşma
                   kararı tercihe değil, filmin risk kartlarında zaten
                   yazılı satırlara bağlandı.

⑤ 5_ARKA_PLAN      video-only · 9 kategori · baseline = STEP 1 arka plan
                   envanteri (özne yalnız dışlamak için adlandırılır).
                   Yeni ölçüm: kimse özne-dışı alana sistematik bakmıyordu
                   — model sadakat bütçesini özneye harcar, insan gözü de.
                   Verdict tavanı: SUBJECT DUPLICATE IN FIELD (arka planda
                   özne kopyası her skoru ezer).

⑥ 6_FIZIK          mod D/V · 9 kategori · tek SAYISAL mercek. Yeni ölçüm:
                   mod D'de planın sayısal kilitleri NUMERIC LOCK LIST'e
                   kopyalanır ve ekranda tek tek doğrulanır (PASS/FAIL/
                   UNMEASURABLE/NOT EXERCISED) — depoda yazılı kilidi
                   üretilmiş videoya karşı doğrulayan İLK alet. STEP 0
                   PREMISE GATE önerme kapısını (kart eki ⑩) rubriğin
                   içine yapısal taşır: dünya kuralı ilan edilen imkânsız
                   fizik bulgu değildir, yalnız tutarlılığı puanlanır.
                   Cetvel kuralı: tahmini mesafe ±%20 tolerans taşır,
                   mahkumiyet cetvelinden ince olamaz. Verdict tavanı:
                   TWO GRAVITIES.

ORTAK ÇEKİRDEK     22.08'in sekiz kapısı ikisine de birebir kondu: MEDIA
                   GATE · CUTS COUNTED · DECLARED ABSENCE · ARITHMETIC
                   GATE · SCORES SUMMARY disiplin bloğu · NOT IN THIS
                   PASS · OUT-OF-SCOPE sonuç bloğu · OUT-OF-SCOPE FLAGS.
                   + İlk koşuların dersleri doğuştan yamalı: severity
                   tally'nin bulgulardan SAYILMASI (①'in 24.08 kusuru)
                   iki rubrikte de SCORES SUMMARY ⑤ maddesi olarak gövdede.

BULGU SAHİPLİĞİ    D108 derin-tarama eki (kartlarda yazılı): çekirdek
                   mercek her zaman sahiptir; ⑤/⑥ bulgusu çekirdek
                   kapsamına oturuyorsa film kaydına o merceğin bölümüne
                   "⑤/⑥ taraması buldu" notuyla girer. Aynı olayı iki
                   mercek görmüşse tek satır, iki kaynak.
```

> Çalıştırma kaydı ⑤: 0 kez çalıştırıldı — henüz koşulmadı.
> Çalıştırma kaydı ⑥: 0 kez çalıştırıldı — henüz koşulmadı.
> ⚠️ İki rubrik de İLK koşusunu görmemiş alettir: ilk koşular ölçüm
> sapması bandını kurana kadar skorları tek başına karar sürmez
> (dört merceğin 24.08 ilk koşu partisi emsali).

---

# ⭐⭐ 25.08.2026 — ALTI MERCEĞİN İLK KOŞUSU: THE IRON SLOPE (dikey shorts)

> Deponun ilk **altı mercekli** partisi (dört çekirdek + iki derin tarama) ve
> deponun ilk **ÖLÇÜLMÜŞ** partisi: raporlar işlenmeden önce master dosya
> ffprobe/ffmpeg ile ölçüldü. Tam kayıt:
> `../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_IRON_SLOPE.md`

```
MALZEME  teslim kurgusu · ÖLÇÜLEN 65,000 s · 720×1280 · 30 fps
MOD      altısı da V — SPEC dosyası bu kez HAZIR DEĞİLDİ (yazılmıştı,
         depoda bulunamadı) → D94/D117'nin sekizinci vakası, mod D hâlâ 0
OTURUM   🚨 ŞÜPHELİ — altı rapor da AYNI ve AYNI ÖLÇÜDE YANLIŞ kesme
         listesini verdi (0:09/0:18/0:29/0:39/0:49/1:00); gerçek ızgara
         düzgün 10 saniyelik [D110 · yeni vaka]
SONUÇ    ⑤ ÇAPRAZ SAYIM ✅ (altısı da 6 sahne) ama kapı BU PARTİDE İŞE
         YARAMADI: uyuşma doğruluk değildi → DERS 125
         ④ KURGU KAPISI (b) düştü (65,0 s ≠ 48,0) → satırlar ⚠️ ŞARTLI
         ③ SES satırı 🚨 GEÇERSİZ — 🔴 BLOCKER'ı ölçümle çürütüldü
```

> 🔎 **⑥ 6_FIZIK — ilk koşusu, ve merceğin varlık sebebi doğrulandı:** tek
> sayısal mercek, filmin tek gerçek kusurunu (serbest cisim hızlanmıyor)
> bağımsız olarak buldu — ama PREMISE REGISTER'ı "none" yazdığı için doğru
> gözlemi yanlış hastalığa bağladı ve reçetesi ("zero-g locomotion yaz")
> filmin novum'unu silecekti. Mod D koşulsaydı kilit tablosu tek satırda
> `FAIL` verirdi. Çalıştırma kaydı: 1 kez · son 25.08.2026 · ⚠️ ön koşu.
>
> 🔎 **⑤ 5_ARKA_PLAN — ilk koşusu, ve mercek kendi işini ıskaladı:** altı
> sahnenin altısında da `FAR FIELD: Black space, star field` yazdı; S2'de
> kadrajın alt üçte birini bir gezegen kaplıyor ve gezegen planın negatif
> bloğunda yasaklıydı → **DERS 126** + rubrik yaması. Çalıştırma kaydı:
> 1 kez · son 25.08.2026 · ⚠️ ön koşu.
>
> 🔎 **③ 3_SES — deponun ilk UYDURMA çekirdek bulgusu:** "S4 complete digital
> silence" 🔴 BLOCKER'ı ve üç satırlık AMBIENCE HOLE LOG, dosyada var olmayan
> bir sessizliği tarif ediyor (`silencedetect -50 dB/0,3 s` → sıfır sonuç;
> S4 tabanı −19,7…−22,8 dB). Satır 🚨 geçersiz → **DERS 125** + rubrik yaması.
>
> 🔎 **① 1_KARE · ② 2_DEVAMLILIK · ④ 4_HIKAYE:** üçü de ⚠️ ön koşu. ④'ün tek
> cümlesi partinin en değerli çıktısı oldu: `THE ONE THING NOTHING ELSE DOES:
> none found` — filmin novum'u ekrana gelmemişti ve bunu ölçüm doğruladı.

---

# 🧭 DERS → RUBRİK İZ DEFTERİ

```
D123 → PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md · yeni kategori
       "3b. YASAK LİSTESİ POLİTİKA MALİYETİ" + BLOCK eşiğine satır
       (25.08.2026 · kaynak rubrik: bu hatayı üretimden ÖNCE
        yakalayabilecek tek alet oydu)
D123 → 1_KARE · GEREKMEZ — üretilmiş kareyi ölçer, prompt yazmaz
D123 → 2_DEVAMLILIK · 3_SES · 4_HIKAYE · GEREKMEZ — aynı sebep
D123 → 5_ARKA_PLAN · 6_FIZIK · GEREKMEZ — aynı sebep
       ⚠️ Altı merceğin hiçbiri prompt YAZMIYOR; bu dersin ürettiği
       hata yalnız yazım tarafında doğar. Tarama yapıldı, kapsam tek.

D124 → hiçbir rubrik · GEREKMEZ — ders bir ÜRETİM ARACI ayarını (klip
       süresi) plana bağlıyor; rubrikler süreyi ölçmez, artık operatör
       ölçüyor (AGENTS ortak adım ⑪). Kardeş tarama yapıldı: altı
       rubriğin altısı da bu hatayı ÜRETEMEZ.
D125 → 3_SES · "6. AMBIENCE CONTINUITY" altına "A SILENCE CLAIM IS A
       CLAIM ABOUT THE FILE" bloğu (kaynak rubrik — uydurma 🔴 oradan
       çıktı)
D125 → AGENTS.md §3 ORTAK ADIMLAR · yeni ⑪ ÖLÇÜM KAPISI (dersin asıl
       yeri: hata rubriğin kuralında değil, ölçme aletinin yokluğundaydı)
D125 → 1_KARE · 2_DEVAMLILIK · 4_HIKAYE · 5_ARKA_PLAN · 6_FIZIK ·
       GEREKMEZ — altısı da CUTS COUNTED istiyor ve istemekte haklı;
       sayının DOĞRULANMASI operatör tarafında koşuyor
D126 → 5_ARKA_PLAN · STEP 1 envanteri, "FAR FIELD" satırına "NAME THE
       LARGEST NON-EMPTY OBJECT + tekrarlayan satır kendi bayrağıdır"
       (kaynak rubrik)
D126 → 1_KARE · kategori 5 ÇEVRE'ye "NAME THE LARGEST BACKGROUND OBJECT"
       (kardeş tarama: aynı gezegeni o da görmedi)
D126 → 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 6_FIZIK · GEREKMEZ — alanı
       envanterleme görevi yok
D127 → 6_FIZIK · kategori 1'e "CONSTANT-VELOCITY TEST" (kaynak rubrik:
       ivmesizliği ölçebilecek tek alet) · ⚠️ bu ders 123 numarasını
       alacaktı; 123 aynı gün paralel bir yazım oturumunda kullanıldı
D127 → 1_KARE · GEREKMEZ — tek klipte parçacık davranışını zaten sorar,
       ama İVME ölçümü sayısal merceğin işidir
D127 → 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 5_ARKA_PLAN · GEREKMEZ —
       aynı sebep; dersin asıl yeri PROMPT tarafıdır (kilit metni
       DERSLER/03'te)
```

> **Ne işe yarar:** "Bu ders hangi rubriğe işlendi?" sorusunun TEK cevabı.
> Rubrikte aranacak etiket kalmadı; yeni ders işlenince kart G adım 5
> buraya satır ekler. Numarası burada geçmeyen rubrik, dersi almamış
> rubriktir.
>
> Satır formatı: `D<n> → <rubrik> · <kuralın yaşadığı bölüm>`
> Rubrikler: VIDEO · MANTIK · KARAKTER · SES · SENARYO · SHORTS

```
KAPI VE MOD KURALLARI — birden çok rubrikte ortak
D52 · D60  → VIDEO · MANTIK · KARAKTER · SES · SENARYO · SHORTS
             "UNVERIFIABLE etiketi sayı taşımaz" + "durdurma koşulu
             raporun içinde ALAN olamaz"
D61        → VIDEO · mod V kural 2 · kat. 3 kesme mod kapısı ·
             IMPORTANT NOTES spec-bağımlı / spec-bağımsız ayrımı
           → SHORTS · INPUT MODE V kural 2
D65        → VIDEO · MANTIK · KARAKTER · SES · SENARYO · "başlık kartından
             film adı okunmaz → FILM: (not supplied)"
           → SHORTS · mod V kural 4 + TITLE COLLISION GATE
D75        → SENARYO · STEP −0.5 MATERIAL GATE
D80        → VIDEO · STEP −2 MEDIA GATE
           → SES · STEP 0 AUDIO PRESENCE GATE (STATE C bloğu)
D94        → VIDEO · SENARYO · STEP −1 operatöre SPEC uyarısı
D101       → RUBRİĞE GİRMEZ (operatör kapısı): 00_README "ÖNCE KURGU
             KAPISI" bloğu 21.08.2026'da üç birime çıkarıldı (klip =
             CLIP COUNT · çekim = SHOT COUNT · sahne = SCENE COUNT);
             kapının tam listesi ../KURGU_VE_TESLIM_KILAVUZU.md
D102       → altı rubrik · SCORES SUMMARY "her puan hücresi kaynağını
             taşır, hiçbir gözlem iki kez faturalanmaz" bloğu
D107       → SENARYO · MANTIK · KARAKTER · SES · STEP 1 "count the cuts
             before you name the scenes" + klip tavanı × 2 sınırı
D108       → MANTIK · KARAKTER · SES · NOT IN THIS PASS "an out-of-scope
             finding carries no number — and neither does the category
             it would have landed in"
D109       → RUBRİĞE GİRMEZ (operatör kapısı): AGENTS.md kart C/D/E/E2/E3
             ortak adım ③ KURGU KAPISI KAPISI
D117       → RUBRİĞE GİRMEZ (operatör + yazım kapısı): AGENTS.md kart A
             "<FILM>_QA_SPEC.md yazılır" + ortak adım ① SPEC bir DOSYADIR
             · GEREKMEZ · rubrik SPEC'in nereden geldiğini göremez
D118       → VIDEO · MANTIK · KARAKTER · SENARYO · SHORTS · çıktı bloğu
             "## PRESENCE STRING" (sıra parmak izi, sahne tablosundan)
           → SES · GEREKMEZ · bu merceğin defteri replik ekseninde, sahne
             tablosu insan-varlığı sütunu taşımıyor
           → kapının kendisi AGENTS.md ortak adım ④ madde (c)
D119       → MANTIK (kaynak rubrik, önce) · KARAKTER · SES · SHORTS · VIDEO ·
             SCORES SUMMARY bloğu madde ④ "the overall score is arithmetic"
           → SENARYO · GEREKMEZ · aritmetik özdeşlik zaten yazılı ("the total
             must equal the OVERALL... mean of the ten category scores") ve
             bu partide toplamı kendi tablosuyla tutan tek rapor o oldu
D110       → VIDEO · SENARYO · MANTIK · KARAKTER · SES · STEP 1 "build this
             from the media alone; a ledger from earlier in this session is
             not evidence" + operatör kuralı: her mercek TEMİZ oturumda
D120       → ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · çıktı künyesi
             `NON-SCENE MATERIAL` satırı ("not a scene at ANY duration")
           → operatör tarafı: AGENTS.md ortak adım ④ · kart kuralı süreden
             İÇERİĞE çevrildi, ≤ 6 s eşiği KALDIRILDI
D121       → ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · çıktı künyesi
             `LINES HEARD` satırı (birebir alıntı + zaman kodu; tekrarlayan
             replik İKİ kez yazılır — kurgu kanıtı)
           → operatör tarafı: AGENTS.md ortak adım ④ madde (c) Δ tablosu +
             ortak adım ⑤ ikinci satır REPLİK
D122       → HİÇBİR RUBRİĞE GİRMEZ (yazım kapısı): AGENTS.md kart A ·
             "replik zamanları ve doruk saati hesaplanmaz, HESAPLATILIR".
             Sebep: rubrik plan dosyasını görmüyor; bozuk olan ölçülen
             şey değil, ÖLÇÜ ALETİYDİ

VIDEO_QA — kategori içi kilitler
D69  → kat. 1 DUPLICATE CHARACTER (araç/hava kilidi giriş-çıkış noktası)
D89  → kat. 1 SEAL COUNT
D90  → kat. 1 SUB-MILLIMETRE EVENT DELIVERY
D98  → kat. 10 "işaretlenen her kutu bulguya döner"
D103 → kat. 10 ters geçiş (bulgudan kutuya)
L1   → kat. 3 HIDDEN CUTS            L2    → kat. 6 ANATOMY LOCK
L3·29→ kat. 4 AI BLOOM / FILL        L4    → kat. 11 WALKING QUALITY
L5   → kat. 1 VISOR PERSISTENCE      L6·27 → kat. 5 TEXTURE SWIMMING
L11·28→kat. 1 CONTACT MORPHING       L15   → kat. 11 GRAVITY SPEED
L18  → kat. 6 LOCOMOTION             L20   → kat. 1 DUPLICATE CHARACTER
L23  → kat. 2 ZERO-G MICRO-MOTION    L24   → kat. 7 FLUID CONTACT
L25  → kat. 1 REFLECTION SYNC        L26   → kat. 2 ROPE/TETHER PHYSICS
L30  → kat. 7 LOW-GRAVITY ARC        L31   → kat. 2 IMPACT PHYSICS
L32  → kat. 2 VEHICLE SCALE
L33  → KNOWN AI FAILURE PATTERNS 1·2·7·8 · kat. 1 SMALL DETAIL FLICKER ·
       kat. 7 duman satırı · IMPORTANT NOTES "cinematic lighting" uyarısı

KARAKTER_QA
D69 → kat. 7 giriş-çıkış klon noktası
D91 → kat. 1 "aynı taraf değil, aynı ORGAN" satırı
D95 → kat. 5 "OPEN vs INVISIBLE" kanıt kuralı
D97 → STEP 1 EVIDENCE BASE + EVIDENCE FLOOR

SES_QA
D35  → kat. 5 üst üste binen replik yasağı
D35c → kat. 1 INVENTED SPEAKER ayrımı
D40  → NOT IN THIS PASS · altyazı → VIDEO_QA

SENARYO_QA
D60 → MOD D başlık satırının tek yasal değeri
D62 → PEAK PRESENCE CHECK 1 (son sahne kapısı)
D111 → STEP 0.b MATERIAL TYPE GATE (FILM / TEASER · dört madde) +
       "kadraj dışı geçiş eksik sahne değildir" + RANKED CUT LIST ve
       REWRITE PRESCRIPTIONS başlıklarındaki teaser yasağı + OUTPUT
       FORMAT'a `MATERIAL TYPE` satırı
D113 → CRITIQUE CATEGORIES önsözü · DECLARED ABSENCE IS NOT A DEFICIT
       (mekanizma kategori 6'dan alınıp kategori-üstü kurala terfi etti)

D111/D112/D113 KARDEŞ RUBRİK TARAMASI (kart G adım 5c · 17.08.2026)
D111 → MANTIK · OUTPUT FORMAT `MATERIAL TYPE` + teaser atlayarak ilerler,
       yalnız DURUM çelişkisi bulgudur
     → VIDEO  · OUTPUT FORMAT `MATERIAL TYPE` + teaser'a sonuç/çözüm
       önerilmez (yatay fragmanın merceği bu)
     → SHORTS · GEREKMEZ, D106 ile zaten var (STEP 0.b)
     → KARAKTER · SES · GEREKMEZ: teaser olmak bu iki merceğin ölçtüğü
       şeyi (kimlik sürekliliği · ses defteri) değiştirmez
D112 → SENARYO · STEP −0.5 + OUTPUT FORMAT · süre "measured" mı "ESTIMATED"
       mi yazılır; ESTIMATED süre hiçbir kapıya girmez
     → VIDEO · MANTIK · KARAKTER · SES · SHORTS · aynı cümle künye satırında
     → operatör tarafı RUBRİĞE GİRMEZ: AGENTS.md kart C/D/E/E2/E3 ortak
       adım ⑦ ÇAPRAZ FİLM PARMAK İZİ KAPISI
D113 → SENARYO · KARAKTER · SES · SHORTS · künye/önsöz bloğu
     → MANTIK · GEREKMEZ: bu mercek zaten "eksik" raporlayamaz, yokluk
       ölçüsü sayaç kanalıyla korunur [D87]
     → VIDEO · GEREKMEZ: kategori düzeyinde N/A mekanizması yok, ölçtüğü
       şey karede VAR OLANIN kalitesi

D115 → VIDEO · MANTIK · KARAKTER · SES · SENARYO · künye satırında
       `CUTS COUNTED` alanı + "several is not a count" cümlesi (STEP 1'de
       zaten istenen sayının çıktı şablonunda ALANI yoktu, o yüzden yok
       oluyordu)
     → SHORTS · GEREKMEZ: 6 sahnelik sabit ızgara rubriğin gövdesinde
       yazılı, mod B zaten sırayı ve birleşmeyi kendi kapısında ölçüyor
     → operatör tarafı RUBRİĞE GİRMEZ: AGENTS.md kart C/D/E/E2/E3 ortak
       adım ⑨ HİZALAMA KAPISI (ızgara plandan, doğrulama replik zaman
       kodundan — model plan dosyasını görmediği için bu kapı rubrikte
       koşulamaz)
D116 → HİÇBİR RUBRİĞE GİRMEZ (operatör kapısı): AGENTS.md ortak adım ⑩
       ÖNERME KAPISI. Sebep: mod V'de model tasarımı bilemez; "bu tasarım
       mıydı" sorusunu yalnız planı elinde tutan taraf cevaplayabilir.
       Rubrik tarafındaki karşılığı zaten var: FLAGS FOR DOCUMENT CHECK.

SHORTS_QA
D62 → ARITHMETIC GATE + "sütun adı SCORES SUMMARY'de birebir var olmalı"
D63 → STEP 0.5 kapısının rapor içinde ALAN olamaması
D64 → PROMPT UPDATE RECOMMENDATIONS kural 4 (tablo kopyalar, uydurmaz)
D66 → SPEC BLOCK · sahne numaralama tabanı (S0) + sahne başlığı taşıma
D70 → 48 sn montaj aritmetiği + kurgudaki başlık kartı 🔴
D71 → HOOK TIMING · analog perde ≠ merak kilidi
D105 → mod V kural 5 (skordan ÖNCE sahne envanteri, sahne başına tek isim
       cümlesi) + OUTPUT FORMAT · SCENE INVENTORY satır biçimi
D106 → STEP 0 üçüncü eksen `MATERIAL TYPE: FILM / TEASER` + STEP 0.b kapısı
       (kat. 14 tersine döner · kat. 13 atlanan geçişi saymaz · kat. 15
       kapanış devir teslimdir) + "kadraj dışı geçiş eksik sahne değildir"
NOT: SHORTS'un KNOWN AI FAILURE PATTERNS tablosundaki ders numaraları
     dosyanın İÇİNDE duruyor (kendini izler), buraya kopyalanmaz.
```

---

# VIDEO_QA_CRITIQUE_PROMPT.md
> 🔎 **20.08.2026 — THE BLUE DRIFT (mod V, ⛔ ön koşu [D94] · parti 🚨 GEÇERSİZ
> [D107 ikinci vaka]):** SPEC planda hazırdı, verilmedi; beş mercek AYNI oturumda
> koşuldu [D110]. Bu rapor kesme SAYMADI ("multiple scene cuts") — künyeye
> `CUTS COUNTED` alanı bu koşudan sonra eklendi (**DERS 115**). İki 🔴'sinden biri
> filmin ses mimarisiydi (kapalı kask + telsiz → ağız kımıldamaz), bir 🔴'si S8'in
> planlı plazma perdesi, bir 🟠'si S10'un amber verici nabzı: üç bulgu da planda
> yazılı tasarım ve hiçbiri MANTIK'tan gelmediği için D87 kapısını görmedi
> (**DERS 116**). Gerçek olabilecek beş bulgu (0:43 ikiz · 3:04 altı parmak ·
> 1:41 el kaynaması · 2:31 gaz yönü · 0:12 karot teması) kilit çelişkisi
> defterinde ⬜ AÇIK. Kayıt: 01_FILM_RAPORLARI/THE_BLUE_DRIFT.md
> 🔎 **17.08.2026 — THE BLACK CRADLE (mod V, ⛔ ön koşu [D94 ×6]):** SPEC planda
> hazırdı, verilmedi. 232 s kurgu, Ⓥ 6.0 — ⭐ **beş merceğin içinde malzemeyi DOĞRU
> sayan tek rapor bu oldu:** 21 kesmeyi zaman koduyla listeledi, diğer dördü aynı
> dosyaya "4 sahne" dedi (**DERS 107**). Buna karşılık rapor **OVERALL SCORE, VERDICT
> ve tracking row üretmedi**, kategori 11'i hiç yazmadı ve kategori 10'da altı kutuyu
> işaretleyip **kategoriyi puansız bıraktı** (D98/D103'ün devamı: kutular bulguya
> döndü, kategori tabloya girmedi). §8'in üç bulgusu (0:30 · 1:09 dudak senkronu ·
> 1:45 vakumda ses) üç ayrı tabloya daha faturalandı → **DERS 108**; sahibi bu
> rubriktir. Kayıt: 01_FILM_RAPORLARI/THE_BLACK_CRADLE.md


> 🔎 **14.08.2026 — THE BANDED DEEP (mod V, ⛔ ön koşu [D94 ×5]):** SPEC
> §0.15'te hazırken verilmedi. Rapor 186 s kurguya koşuldu, Ⓥ 4.9. STEP −1
> uyarısının öngördüğü her şey oldu: sırt yasağı kilidi "white backpack"
> baseline'ına, toz kilidi "dust hangs" okumasına dönüştü — beşi kilit
> çelişkisi defterinde ⬜ AÇIK. 3:00 yanık başlık kartını doğru yakaladı
> (D70 zinciri 6. vaka). Kayıt: 01_FILM_RAPORLARI/THE_BANDED_DEEP.md

> 🔎 **DERS 72 (06.08.2026 · THE UNBROKEN CITY):** Bu rubrik bir KURGUYU
> değerlendiriyorsa, operatör teslimden önce KURGU KAPISI'nı koşmuş
> olmalıdır: klip sayısı = plan SCENE COUNT · toplam süre = RUNTIME ±2 s ·
> ekran metni 0.0 sn (kapak çıktısı dahil) · CENTRAL CHOICE sahnesi kurguda
> VAR. Mod V koşusu kurgu hatasını içerik zaafı olarak raporlayabilir —
> Unbroken City'de senaryo merceği "zero choices" dedi, gerçek neden
> doruğun kurguya girmemesiydi. Mod V bulgularını tabloya işlerken film
> kaydındaki belge cevaplarıyla birlikte oku.
>
> Çalıştırma kaydı: son 06.08.2026 — THE UNBROKEN CITY (mod V, geçerli
> koşu). DERS 65 TUTTU: rapor `FILM: (not supplied)` yazdı.

> 🔎 **DERS 76 · 79 (06.08.2026 · THE STARLESS CIRCLE):** İki gözlem
> biçimini rapora AYNEN yaz, yorumlama:
> · Gökte/çerçevede bir **YOKLUK** novum'u varsa (yıldızsız yama, delik,
>   boşluk), onu bir NESNE adıyla ("black sphere", "dark disc object")
>   tarif ediyorsan bu başlı başına bulgudur — model yokluğu nesneye
>   çevirmiştir. Taşıyıcı pozitif alanı da say: "sky devoid of stars"
>   gördüysen novum zaten imkânsızdır. [DERS 76]
> · Vizör ve sırt ünitesi: "opaque/tinted/mirrored visor" ve "life-support
>   backpack" bu seride iki filmde üst üste BIBLE'A RAĞMEN çıktı; mod V'de
>   ihlal diyemezsin ama FLAGS'e soru olarak yaz — belge cevabı ihlali
>   ortaya çıkarıyor. [DERS 79]
>
> Çalıştırma kaydı: son 06.08.2026 — THE STARLESS CIRCLE (mod V, **ŞARTLI
> koşu**: operatör 12 saniyelik tek klip yükledi, plan 10 s klip diyor ve
> klibin içinde filmin hiçbir tanımlayıcı öğesi yok — çanak dizisi yok,
> yıldız alanı yok. Klip kimliği doğrulanmadan skor kesin sayılmaz).
> DERS 65 TUTTU: rapor `FILM: (not supplied)` yazdı. Önceki: aynı gün
> THE UNBROKEN CITY (mod V, geçerli koşu).

> 🔎 **DERS 80 (07.08.2026 · THE BLIND RETURN):** STEP −2 MEDYA KAPISI bu
> koşudan doğdu. Operatör videoyu yüklemedi; rapor 11 kategoriyi doğru
> şekilde UNVERIFIABLE bıraktı ama yine de `VERDICT: REGENERATE` + 1 🔴
> BLOCKER + tablo satırı üretti. Medyasız koşunun tek legal çıktısı artık
> `MEDIA MISSING — RUN NOT STARTED` bloğudur.
>
> Çalıştırma kaydı: son 07.08.2026 — THE BLIND RETURN (**GEÇERSİZ koşu:
> girdisiz**; skor tablolarına girmedi → DERS 80). DERS 65 TUTTU: rapor
> `FILM: (not supplied)` yazdı. Tekrar koşusu bekleniyor: gerçek 169 s
> kurgu + §0.15 SPEC (mod D).

> 🔎 **Çalıştırma kaydı: son 09.08.2026 — THE COLD BURN** (mod V, geçerli
> koşu, 5/10 Ⓥ · REGENERATE, 3 🔴: rijit sıfır-g · donmuş yangın
> partikülleri · 3:40 yanık kart). DERS 65 TUTTU. SPEC yine
> yapıştırılmadı — filmin planında hazır §QA SPEC bloğu vardı (operatör
> kuralı ②'nin 2. ihlali; mod D hâlâ hiç denenmedi). Uyum notu: canlı
> yokken kategori "UNVERIFIABLE" yazıldı, doğrusu N/A. [DERS 82 sınırı:
> aynı kurguya SES_QA da koşulduğu için §8'in ses-tarafı bulguları
> 07_SES tablosuna devredildi; burada kare içi olanlar kaldı.]


> 🔎 **DERS 85 (11.08.2026 · THE THIRD DUNE):** Bu rubriğin `PROMPT
> IMPROVEMENT SUGGESTIONS` bölümü mod V'de **görmediği promptu alıntıladı**:
> `REMOVE from video prompt: "title card, cinematic poster"`. Depoda
> "cinematic poster" hiç geçmiyor; "title card" ise 42/42 promptta ama
> YASAĞIN İÇİNDE ("no subtitles, no title card, no watermark"). Reçete
> uygulansaydı raporun kendi bulduğu 4:00 yanık kartına karşı duran tek
> cümle silinecekti.
> ⛔ **Reviewer kuralı:** REMOVE / REPLACE önerisi yazarken tırnak içine
> yalnız **filmde GÖRDÜĞÜN** bir şeyi koyabilirsin; prompt metnini
> göremiyorsan öneriyi ADD biçiminde yaz ya da "REMOVE — operatör
> promptta şu ifadeyi ARARSA" diye koşullu yaz. Prompt dizesi uydurmak,
> D65'in (başlık kartından film adı okumak) prompt tarafındaki eşidir.
> ⛔ **Operatör kuralı (kart C adım 5b):** her REMOVE/REPLACE reçetesi
> uygulanmadan önce grep'lenir; çıktı boşsa ya da yasağın içindeyse
> reçete DÜŞER.
>
> Çalıştırma kaydı: son 11.08.2026 — THE THIRD DUNE (mod V, geçerli koşu,
> Ⓥ 4/10 · REGENERATE, 3 🔴). DERS 65 TUTTU (`FILM: (not supplied)`).
> Üç 🔴'den biri (4:00 yanık başlık kartı) KURGU hatası çıktı — kapak
> başlığının kurguya sızması, D70/72 zincirinin **4. vakası**. Diğer ikisi
> temas kaynaşması ve ikisinde de "clear boundary — no merging" cümlesi
> promptta VARDI → D84'ün teknik taraftaki karşılığı.
> ⚠️ SPEC bloğu planın 856. satırında HAZIRDI ve yine yapıştırılmadı —
> operatör kuralı ②'nin 3. ihlali; mod D bu depoda hâlâ hiç denenmedi.

---

> 🔎 **DERS 102 · 103 (16.08.2026 · THE LAST SHIFT — bu iki dersin KAYNAK
> rubriği budur):** Mod V, ⛔ ön koşu (SPEC §0.15'te hazırdı, verilmedi —
> D94 ×6). Rapor Kamera'yı UNVERIFIABLE yazdı, aynı kesme/geçiş sorusunu
> FLAGS'e soru olarak koydu **ve** Çevre'den puan düşürdü; belge kontrolünde
> iki soru da "filmin önermesi" çıktı (checkerboard = hasat parselleri,
> amberleşme = planlı ışık fazı) ama puanlar yerinde kaldı → gövdeye
> **DERS 102** yaması (skor hücresi kaynağını taşır · bir gözlem tek yerde).
> Negatif sayımı `BOX 2 · LINKED 2 · UNLINKED 0` ile temiz kapandı, oysa
> bulgu listesi 5'ti ve 1:52'nin "2D fluid" tozunun iki kutusu boştu →
> **DERS 103** (denetim iki yönlü koşulur). Doğru yakaladıkları: 2:50 yanık
> kart 🔴 (D70/72 ×7) ve 2:09 el–plaka kaynaşması 🔴 (D11/D28, SPEC'ten
> bağımsız). Kayıt: 01_FILM_RAPORLARI/THE_LAST_SHIFT.md
>
> Çalıştırma kaydı: son 16.08.2026 — THE LAST SHIFT (mod V, ⛔ ÖN KOŞU).
> DERS 65 TUTTU: rapor `FILM: (not supplied)` yazdı.


# MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md
> 🔎 **21.08.2026 — LOSS OF LIFT (mod V · AYNI OTURUMDA İKİ KOŞU · 🚨 GEÇERSİZ):**
> iki koşunun sahne haritası, çelişki defteri ve severity tally'si (🔴0 🟠1 🟡2)
> birebir aynı; **tek yeni gözlem yok, toplam 2.0 puan ayrı** (8/10 · 6/10) ve
> ikisi de kendi hücrelerinin ortalaması değil (9.5 · 6.6). Koşu 2 beş hücreye
> "[no in-scope source]" yazıp 7/10 verdi — rubriğin kendi "kategori tam puanla
> başlar" kuralına rağmen. **DERS 119** buradan doğdu; ④ maddesi bu rubriğe
> (kaynak) ve dört kardeşine yamandı. STEP 1'deki "aynı oturumdaki haritayı
> delil sayma" yasağı okunurken çiğnendi → yasağın yeri operatör tarafı [D110].
> Üç bulgusundan biri (kostüm yakası) planda yazılı tasarım çıktı, üçü de kilit
> çelişkisi defterine ⬜ AÇIK olarak alındı: ders YAZILMADI.
> Kayıt: 01_FILM_RAPORLARI/LOSS_OF_LIFT.md
> 🔎 **20.08.2026 — THE BLUE DRIFT (mod V · parti 🚨 GEÇERSİZ):** 15 blok bildirdi,
> film 25 segment. ⭐ Blokların 15'i de ardışık ızgara dilimlerinin BİREBİR
> birleşimi çıktı (blok 1 = 9 s hook) — ızgara bu yüzden geri alınabildi
> (**DERS 115**). Üç bulgusunun üçü de planda yazılı tasarım: açık yakalama
> yuvası (S24), amber verici kubbesi (S10), başlık kartındaki yüz (film sahnesi
> değil). Bir numaralı reçetesi uygulansaydı filmin PLANLI FİNALİ kesilecekti
> (**DERS 116**). 2b kapısı bu mercekte VARDI ve iki bulguyu yakalayabilirdi;
> koşu tek oturumda yapıldığı için kapı işletilmedi.
> Kayıt: 01_FILM_RAPORLARI/THE_BLUE_DRIFT.md
> 🔎 **17.08.2026 — THE BLACK CRADLE (🚨 GEÇERSİZ koşu):** 232 s kurguyu **4 sahne**
> saydı; aynı dosyada VIDEO_QA 21 kesme saydı ve raporun sahne haritasında 85 s'lik
> bir "sahne" var — 10 s klip tavanlı bu hatta böyle bir sahne üretilemez
> (**DERS 107** buradan doğdu; STEP 1'e kesme sayımı kapısı eklendi). İkinci arıza:
> Fizik 4/10'un tek kaynağı **vakumda ses**, Nedensellik 5/10'un tek kaynağı **dudak
> senkronu** — ikisi de bu rubriğin ❌ listesinde VIDEO_QA'ya verilmiş olaylar
> (**DERS 108**; düzeltilmiş okuma ~8.4). ✅ D87 kapısı iki bulguyu düşürdü (S5 biniş
> kadraj dışı planlı · S8 ışık sınırı planlı tek geçiş). Sayaç yine NONE, planda dört
> sayaç vardı → D78 ×5.


> 📌 **Bu dosya hakkında** — 31 Temmuz 2026'da yazıldı, aynı gün
> **yalnızca video** ile çalışacak şekilde yeniden düzenlendi.
> Yatay formatın üçüncü eleştiri merceği.
>
> ```
> VIDEO_QA      kare içi        tek klip teknik olarak doğru mu
> MANTIK_QA     sahneler arası  film kendi kendisiyle çelişiyor mu  ← bu dosya
> SENARYO_QA    dramatik        hikayeyi kimse umursar mı
> ```
>
> **Neden doküman istemiyor:** 8 kategorinin 8'i de filmin **kendi içindeki**
> çelişkilere bakıyor. Tozlu suit'in temizlenmesi, sayacın geri gitmesi,
> kapının yer değiştirmesi — bunların hiçbiri plan dosyası gerektirmez,
> ekranda görünür. İlk sürümde bir "plan ↔ kurgu uyumu" kategorisi vardı;
> tek gerçekten doküman isteyen oydu ve `SENARYO_QA`'nın zirve kontrolüne
> devredildi.
>
> **Bunun bedeli:** Bu rubrik "planlanan sahne kurguda yok" diyemez.
> Diyemeyeceği de dosyada üç yerde yazılı — "eksik" raporlaması yasak,
> çözemediği her şey `FLAGS FOR DOCUMENT CHECK` altına **soru** olarak
> yazılıyor. O soruları plan dosyalarıyla karşılaştırma işi rapor geldikten
> sonra yapılır.
>
> **Kapsam sınırı bloğunu silme.** Üç yatay raporun birleştirilebilir
> olmasının tek garantisi odur.

> 🔎 **DERS 72 (06.08.2026 · THE UNBROKEN CITY):** Bu rubrik bir KURGUYU
> değerlendiriyorsa, operatör teslimden önce KURGU KAPISI'nı koşmuş
> olmalıdır: klip sayısı = plan SCENE COUNT · toplam süre = RUNTIME ±2 s ·
> ekran metni 0.0 sn (kapak çıktısı dahil) · CENTRAL CHOICE sahnesi kurguda
> VAR. Mod V koşusu kurgu hatasını içerik zaafı olarak raporlayabilir —
> Unbroken City'de senaryo merceği "zero choices" dedi, gerçek neden
> doruğun kurguya girmemesiydi. Mod V bulgularını tabloya işlerken film
> kaydındaki belge cevaplarıyla birlikte oku.
>
> Çalıştırma kaydı: son 06.08.2026 — THE UNBROKEN CITY (mod V, geçerli
> koşu). DERS 65 TUTTU: rapor `FILM: (not supplied)` yazdı.

> 🔎 **DERS 78 (06.08.2026 · THE STARLESS CIRCLE):** `THE COUNTER: NONE`
> yazdığında bu **filmde sayaç olmadığı anlamına gelmez** — üç filmde
> (Dawn Front · Stone Sky · Starless Circle) sayaç PLANLIYDI ve mercek
> göremedi. Starless Circle'da dört çevresel sayaç vardı (çanak eğimi
> 55°→90° · kuşak yaşı 300 m→4 m · daire yüksekliği · ışık takası).
> Ortak sebep: sayacın iki ucu hiçbir karede yan yana gelmiyor. Bu yüzden
> `NONE` satırını FLAGS'e şu soruyla taşı: "planda çevresel bir sayaç var
> mı, varsa iki ucunu tek karede gösteren bir kare yazılmış mı?"
> Aynı kural filmin BEDEL nesnesi için de geçerli (siluetsiz prop = ekranda
> yok). [DERS 78]
>
> 🔎 **DERS 76:** Gökteki bir yokluğu ("yıldızsız daire") NESNE adıyla
> tarif ediyorsan — "black sphere", "dark planet" — bunu Coğrafya
> tutarsızlığı olarak değil, olduğu gibi FLAGS'e yaz: novum'un
> nesneleşmesi üretim hatasıdır, filmin kendi içindeki çelişki değil.
>
> Çalıştırma kaydı: son 06.08.2026 — THE STARLESS CIRCLE (geçerli koşu,
> 5.5/10 · STRUCTURAL PROBLEM). Belge kontrolü bir bulguyu düşürdü
> (dairenin yükselmesi = planlı sayaç), üçünü ayakta tuttu (klon · PRE-DAWN
> kademesinin yokluğu · terk edilmiş kurulumlar). Önceki: aynı gün
> THE UNBROKEN CITY (8.0/10). DERS 65 iki koşuda da TUTTU.

> 🔎 **DERS 80 (07.08.2026):** Bu kural bu rubrikte de geçerlidir —
> oynatılabilir video ekli değilse, süre 0 s okunuyorsa ya da tek kare
> çözülemiyorsa tek legal çıktı `MEDIA MISSING — RUN NOT STARTED` bloğudur:
> skor yok, verdict yok, severity yok, tablo satırı yok. "INPUT MISSING
> yasağı" YALNIZ doküman içindir, medya için değil.
>
> 🔎 **DERS 81 (07.08.2026 · THE BLIND RETURN):** Raporun son-30-saniye
> bulguları ("uzamsal çöküş", art arda çelişen mekânlar) belge kontrolünde
> KURGU hatası çıktı: S0-S14 plan ızgarasına saniyesi saniyesine oturuyordu,
> sonra bir Çehov sahnesi (S15) kurguda yoktu ve S16↔S17 ters sıralanmıştı.
> Mekânlar (hava kilidi · hab · çıkış aracı) üçü de planlıydı. Kural:
> Coğrafya/Nedensellik MAJOR'ları filmin SON bloğunda kümeleniyorsa,
> tabloya işlemeden önce kurgu SIRASI plan haritasından doğrulanır —
> "silinen hasar" görünümü, kurulum sahnesi düşmüş bir ödemenin maskesi
> olabilir. [DERS 81 · kurgu kapısı v2: sıra + kurulum listesi]
>
> Çalıştırma kaydı: son 07.08.2026 — THE BLIND RETURN (geçerli koşu,
> 4.0/10 · STRUCTURAL PROBLEM; dört MAJOR'ın dördü belge kontrolünde kimlik
> değiştirdi — köpük kabuğu tasarım, uzamsal çöküş kurgu → DERS 81).
> ⚠️ Bir kural ihlaliyle: DERS 78'in "`COUNTER: NONE` satırını FLAGS'e
> soruyla taşı" adımı uygulanmadı (planda DÖRT sayaç vardı; ikisi fark
> edilmeden okundu, ikisi hiç). DERS 65 TUTTU: `FILM: (not supplied)`.
>
> Çalıştırma kaydı: son 09.08.2026 — THE COLD BURN (geçerli koşu, 7.0/10 ·
> FIXABLE IN EDIT — serinin 2. en yüksek mantık skoru). DERS 65 TUTTU.
> ✅ DERS 78 adımı İLK KEZ uygulandı: `COUNTER: NONE` FLAGS'e soru olarak
> taşındı; belge cevabı planda İKİ sayaç kanalı buldu (duruş küresi +
> 10 segmentlik yakıt göstergesi — sahneleri kurguda yoktu, D78 ×3).
> ⚠️ Skorun yüksekliği yanıltmasın: kurguda planın 12/30 sahnesi vardı —
> az sahne, az çelişki fırsatı demektir; 7.0 eksik filmin iç tutarlılığıdır.


> 🔎 **DERS 87 (11.08.2026 · THE THIRD DUNE):** Bu rubrik filmin
> **ÖNERMESİNİ çelişki saydı.** Üç MAJOR'ın ikisi belge kontrolünde düştü:
> (a) "araç 1:00'de düz kumda, 2:00'de dik tepeye gömülü" — plan S12
> aracın sancak yanının yeni tepe tarafından yutulmasıyla açılır, filmin
> adı zaten ÜÇÜNCÜ TEPE; (b) "kalkışta dairesel çanak" — plan S22 (ÇANAK)
> 14 m'lik sığ dairesel çukuru tarif ediyor. Coğrafya 4/10 skorunun
> gerekçesinin çoğu bu iki bulguydu.
> ⛔ **Reviewer kuralı:** bir şeyin DEĞİŞMESİ tek başına çelişki değildir.
> İki timecode arasındaki fark, filmin anlattığı süreç olabilir. Değişimi
> raporla ama severity vermeden önce sor: *bu değişim ilerliyor mu
> (süreç), yoksa gidip geliyor mu (çelişki)?* Tek yönlü ilerleyen değişim
> `COUNTER CURVE`'e yazılır, `CONTRADICTION LOG`'a değil.
> ⛔ **Operatör kuralı (kart E adım 2b):** coğrafya/kostüm/zaman-ışık
> bulgusu tabloya işlenmeden önce "bu değişim filmin önermesi mi?" sorusu
> plan dosyasından cevaplanır.
>
> Çalıştırma kaydı: son 11.08.2026 — THE THIRD DUNE (geçerli koşu, 7.0/10 ·
> FIXABLE IN EDIT · 0 BLOCKER). ⭐ **Sayaç kategorisi ilk kez 10/10:**
> fırtına cephesinin yaklaşması monotonik okundu — D78'in üç başarısız
> vakasından sonra çalışan ilk çevresel sayaç, çünkü sayaç ufku kaplayan
> bir DUVAR (ölçeğin iki ucu her karede birlikte). Ayakta kalan bulgu:
> toz sıfırlanması (→ 06 tablosu, D84).

---

> 🔎 **16.08.2026 — THE LAST SHIFT (mod V):** Rapor `FILM:` alanına dosya
> adını yazdı (`Adsız tasarım (22).mp4`) — DERS 65 kuralının hatırlatması:
> künye rapordan alınmaz. Sayaç sütunu **N/A** yazıldı, oysa planda ÜÇ
> metinsiz sayaç var (kalan parsel · kadrajdaki insan sayısı 2→1→0 · amber
> pus yüksekliği) → D78'in 4. vakası: sayaç tek karede kanıtlanmıyorsa
> mercek onu görmüyor. Coğrafya 4/10'un yarısı D87'de düştü (parsel ızgarası
> filmin novum'u), yarısı kilit çelişkisi defterinde ⬜ AÇIK.
> Kayıt: 01_FILM_RAPORLARI/THE_LAST_SHIFT.md


# SENARYO_QA_CRITIQUE_PROMPT.md
> 🔎 **21.08.2026 — LOSS OF LIFT (mod V · ⛔ ÖN KOŞU · Ⓥ7.0 ŞARTLI):** SPEC planda
> hazırdı (satır 738), verilmedi — **6. vaka, mod D hâlâ 0** (**DERS 117**; SPEC
> artık ayrı dosya). Kesme listesinin 4 maddesinin 4'ü de planın omurgasını
> hedefledi: katalizör (pin bir çentik aşağı), filmin tezi, tek şefkat beati ve
> gece geçişi — önerme kapısı [D116] dördünü de düşürdü. ⭐ Buna karşılık mod V'nin
> meşru okuması üç tasarım kararını doğruladı: tek replik **9/10** ve "korunacak üç
> şey"in birincisi, novum tek cümlede okundu (özgünlük 8/10), S0↔S24 çifti
> paylaşılabilir an seçildi. Doruk okuması (2:50) planın doruğuyla (3:19)
> uyuşmuyor → insan şeridi kapısı (**DERS 118**) buradan doğdu.
> Kayıt: 01_FILM_RAPORLARI/LOSS_OF_LIFT.md
> 🔎 **20.08.2026 — THE BLUE DRIFT (mod V, ⛔ ön koşu [D94] · parti 🚨 GEÇERSİZ):**
> SPEC planda hazırken verilmedi; 25 sahnelik filmi 10 blok saydı ve kesme listesi
> filmin dönüm noktasını (S9 ölü araç) + umut vuruşunu (S10 verici nabzı) 40
> saniyelik "tekrarlı kokpit" bloğunun içinde eritip kesmeye aday gösterdi
> (**DERS 115**). ⭐ D94'ün bedelinin en net ölçümü: mercek, üretimde BOZULMUŞ
> olabilecek repliği ("Avanis içimizdedir…", plan: "Havanız iticinizdir…") filmin
> EN İYİ repliği ilan etti ve bozulmamış olanı kesmeyi önerdi. Ayrıca kartta
> gördüğü sloganı ("HE'S NOT TRYING TO SURVIVE. HE'S WAITING.") alıntıladı —
> bu dize depoda hiçbir dosyada geçmiyor. Kayıt: 01_FILM_RAPORLARI/THE_BLUE_DRIFT.md
> 🔎 **17.08.2026 — THE BLACK CRADLE (mod V, ⛔ ön koşu [D94 ×6] · 🚨 GEÇERSİZ):**
> Mercek 26 sahnelik filmin ~23 kliplik kurgusunu **4 sahne** olarak haritalandırdı
> ve iki "sahne"si 85 s / 62 s uzunluğunda çıktı → **DERS 107**. Bedeli doğrudan
> okunuyor: rapor "bedelli seçim yok · umut anı yok · zirve 1:45'te" dedi; üçü de
> yanlıştı (CENTRAL CHOICE S17 · umut-önce-düşüş %66→%72 · DORUK S21), üçü de o
> 85 saniyelik bloğun içindeydi. 🚫 Kesme listesi UYGULANMADI: birinci sırası planın
> KESİLEMEZ viral arası S4'e giriyor — D94 örüntüsünün 4. vakası.


> 🔎 **14.08.2026 — THE BANDED DEEP (mod V, ⛔ ön koşu [D94]):** Ⓥ 7.4 —
> tablonun en yüksek mod V skoru, ama finalsiz kurgunun puanı: S12-S15
> ekranda yok, rapor durak karesini final sandı ("Ends" + Ending 8.0).
> STEP −0.5 malzeme kapısı doğru çalıştı (186 s = FULL RUN). Kesme listesi
> uygulanmadı; 1. sıradaki S5 kesimi planda OLMAYAN bir sahne çıktı.

> 🔎 **DERS 72 (06.08.2026 · THE UNBROKEN CITY):** Bu rubrik bir KURGUYU
> değerlendiriyorsa, operatör teslimden önce KURGU KAPISI'nı koşmuş
> olmalıdır: klip sayısı = plan SCENE COUNT · toplam süre = RUNTIME ±2 s ·
> ekran metni 0.0 sn (kapak çıktısı dahil) · CENTRAL CHOICE sahnesi kurguda
> VAR. Mod V koşusu kurgu hatasını içerik zaafı olarak raporlayabilir —
> Unbroken City'de senaryo merceği "zero choices" dedi, gerçek neden
> doruğun kurguya girmemesiydi. Mod V bulgularını tabloya işlerken film
> kaydındaki belge cevaplarıyla birlikte oku.
>
> 🔎 **DERS 73 (06.08.2026 · THE WRONG SHADOW):** "Camera-carrier / sıfır
> seçim / dead scene" bulguları, novum'u türetilmiş optik fenomen taşıyan
> bir filmde ÜRETİM kaybının belirtisi olabilir — Wrong Shadow'da CENTRAL
> CHOICE planda vardı (S3: adam kendi gölgesinin mili olur) ama çift gölge
> hiç render edilmediği için jest ekranda "adam duruyor"a düştü ve mercek
> serinin en düşük hikaye skorunu (3.0) verdi. Mod V'de karakter/yapı
> bulgularını tabloya işlemeden önce film kaydındaki belge cevaplarına bak:
> ölü olan sahne mi, üretim mi?
>
> 🔎 **DERS 78 (06.08.2026 · THE STARLESS CIRCLE):** "Kurulum var, ödeme
> yok / karakter seçim yapmıyor" bulgularının üçüncü kök nedeni: doruk
> KURGUDA VAR ama bedeli taşıyan nesne siluetsiz üretildiği için okunmuyor.
> Aynı filmde planlı DÖRT çevresel sayaç da mercekte "NONE" olarak göründü.
> Sahneler arası karşılaştırmaya dayanan her anlatım kanalı (sayaç, bedel,
> ters simetri) mod V'de görünmez — bulguyu tabloya işlemeden önce film
> kaydındaki belge cevaplarına bak: kanal yok mu, yoksa kanal tek karede
> hiç kanıtlanmamış mı?
>
> Çalıştırma kaydı: son 06.08.2026 — THE STARLESS CIRCLE (mod V,
> **GEÇERSİZ koşu**: rubrik 12 saniyelik tek klibi film sayıp on kategoriye
> puan verdi → STEP −0.5 MALZEME KAPISI bu koşudan doğdu, **DERS 75**).
> DERS 65 TUTTU: rapor `FILM: (not supplied)` yazdı. Önceki: 06.08.2026
> THE WRONG SHADOW (mod V, geçerli koşu; dikey hattın ilk senaryo satırı —
> Ⓥ ⚠️ ŞARTLI, 3.0/10) ve aynı gün THE UNBROKEN CITY (mod V, geçerli koşu)
> — ikisinde de DERS 65 TUTTU.

> 🔎 **DERS 80 (07.08.2026):** Bu kural bu rubrikte de geçerlidir —
> oynatılabilir video ekli değilse tek legal çıktı `MEDIA MISSING — RUN
> NOT STARTED` bloğudur: skor yok, verdict yok, tablo satırı yok. MALZEME
> KAPISI (STEP −0.5) medyanın YETERSİZ olduğu durumu çözer; DERS 80
> medyanın HİÇ OLMADIĞI durumu — ikisi ayrı kapıdır.
>
> 🔎 **DERS 81 (07.08.2026 · THE BLIND RETURN):** Mod V raporunun kesme
> reçetesi filmin SON sahnelerini hedefliyorsa ("drop the rocket and tube
> scenes"), tabloya işlemeden önce kurgu SIRASI plandan doğrulanır. Bu
> koşuda "üç çelişkili final / REVISE STRUCTURE" bulgusunun kökü içerik
> değildi: bir Çehov sahnesi (S15) kurgudan düşmüş, S16↔S17 ters
> sıralanmıştı — ve reçete, filmin PLANLI FİNALİNİ (kalkış) kesmeyi
> öneriyordu. Kurgu hatası içerik zaafı kılığına girer (D72/73'ün üçüncü
> biçimi: sahneler var, SIRALARI yok). [DERS 81]
>
> Çalıştırma kaydı: son 07.08.2026 — THE BLIND RETURN (mod V, geçerli
> koşu, Ⓥ ⚠️ ŞARTLI 4.0/10 · REVISE STRUCTURE). **DERS 75 MALZEME
> KAPISI'nın ilk başarılı koşusu:** rapor süreyi (169 s) ve kesme sayısını
> (13) ölçüp header'a yazdı, TAM KOŞU olarak devam etti. DERS 65 TUTTU:
> `FILM: (not supplied)`. Belge kontrolü üç reçeteyi reddetti (final
> kesme · "Visor breach" kesme · karakter bulgusu) → film kaydına bak.
>
> Çalıştırma kaydı: son 09.08.2026 — THE COLD BURN (mod V, geçerli koşu,
> Ⓥ ⚠️ ŞARTLI 4.0/10 · REVISE STRUCTURE). DERS 75 kapısı koştu (225 s /
> 12 kesme header'da), DERS 65 TUTTU. Belge kontrolünde raporun üç ana
> bulgusu da kimlik değiştirdi — D72/81 örüntüsünün en ağır vakası:
> "two disjointed shorts" = ikinci tırmanışın (S16-S28) ~%80'i kurguda
> yok · "zirve = patlama" = patlama planın ORTA NOKTASI (S12), gerçek
> doruk (S26 tahliye) ekranda hiç yok · "no central choice" = S19 iptal
> sahnesi ekranda yok. Reçetelerden "S9'a seçim ekle" planın S19+S26'da
> zaten yaptığı şeydi — mod V reçetesi, kurguya girmemiş planı yeniden
> icat etti. Kurgu kapısının 4 maddesi birden ihlaldi (ilk kez) →
> film kaydına bak: `../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_COLD_BURN.md`


> 🔎 **Çalıştırma kaydı: son 11.08.2026 — THE THIRD DUNE** (mod V, geçerli
> koşu, Ⓥ ⚠️ ŞARTLI **7.0/10 · SHOOT WITH TRIMS** — tablonun en yüksek mod
> V skoru). DERS 75 kapısı koştu (245 s / 24 kesme header'da), DERS 65
> TUTTU. ⭐ **Kontrol grubu değeri:** bu filmde planın sahneleri kurguya
> girdi (25 klip = 25 sahne · CENTRAL CHOICE S17 ve DORUK S21 ekranda) ve
> skor 4-5 bandından 7.0'a çıktı — Cold Burn/Blind Return/Unbroken City'nin
> düşük hikaye skorlarının kökünün içerik değil KURGU KAYBI olduğu
> teşhisini (D72/81) destekleyen ilk pozitif vaka.
> ⚠️ Buna karşılık **kesme listesinin ikisi de reddedildi:** her iki öneri
> de plan `VIRAL INTERSTITIALS: S3 · S6 · S12 · S21 (KESİLEMEZ)` listesine
> giriyor ve ikincisi filmin ORTA NOKTA REVEAL'ini siliyor — Kaleida Crash
> tuzağının tekrarı. Üçüncü reçete ("Kum taşınıyor" repliğini kes) de
> düştü: rapor repliğin ikinci yarısını ("Bu zemin dün buranın zemini
> değildi") alıntılamamış, filmin önermesi orada.
> ⛔ Reviewer kuralı: bir repliği kesmeyi önermeden önce **tamamını**
> alıntıla — yarım alıntı, olmayan bir kusuru kanıt gibi gösterir.

---

> 🔎 **DERS 100 · 101 (16.08.2026 · THE LAST SHIFT, mod V ⛔ ön koşu):**
> Rapor filmi 14 sahne olarak saydı ve DOĞRU saydı — ama planın birimi 14
> sahne değil **24 çekim / 27 klip**tir; kurguda ~10 klip yoktu ve mercek
> bunu göremezdi (mod V'de "eksik" raporlanamaz, D3). Ders bu yüzden
> rubriğe değil KURGU KAPISINA yazıldı. Merceğin kesme listesinin 1. sırası
> yine bir KESİLEMEZ viral aradır (S0 kancası) — Third Dune ve Ring
> Light'tan sonra 3. vaka: mod V kesme listeleri UYGULANMAZ.
> ⭐ Diyalog 9/10 tablonun en yükseği: 13/13 gövdesiz makine replik,
> hiçbiri görüntüde olanı anlatmıyor.
> Kayıt: 01_FILM_RAPORLARI/THE_LAST_SHIFT.md

---

> 🔎 **DERS 111 · 112 · 113 (17.08.2026 · THE COLD BURN — FRAGMAN DİKEY,
> mod V ⛔ ön koşu · 🚨 YANLIŞ MERCEK):** Bu rubrik bir FRAGMANA koşuldu.
> `FRAGMAN_KILAVUZU.md` §0 bunu tek satırda yasaklar ("fragmanın merceği
> SHORTS_QA'dır") — ama yasak yalnız KILAVUZDA yaşıyordu ve rubrikte
> teaser'ı tanıyacak hiçbir kapı yoktu. Sonuç: fragmanın işi kusur diye
> faturalandı (Final 3/10 "duruyor, bitmiyor" — oysa borç bırakmak
> tasarımdı), yazılı YÜZ KİLİDİ eksiklik diye faturalandı (Karakter 4/10
> "kamera taşıyıcı" — oysa yüz 0 kare ilan edilmişti) ve düzeltme olarak
> doğrudan bir SPOILER yazıldı ("başlık posterini içerideki yangınla
> değiştir" = kaynak filmin üçüncü perdesi).
> ⚠️ Bu, D106'nın **aynı gün, ikinci rubrikte** birebir tekrarıdır: D106
> yalnız SHORTS_QA'ya işlenmişti → **DERS 111** (kardeş rubrik taraması).
> ⚠️ Rapor 62 s · 7 segment · ~9-10 s sahne · 0:58'de başlık kartı bildirdi;
> kardeş fragman koşusu (Black Cradle, SHORTS_QA, aynı gün) 63 s · 7 segment
> · ~10 s · 00:58'de başlık kartı bildirmişti. İki farklı filmin aynı
> geometrisi → **DERS 112** (mod V'de süre ölçüm değil, çıktıdır).
> ✅ Rubriğin İKİ kapısı doğru çalıştı: `FILM: (not supplied)` yazıldı [D65]
> ve sessiz film Diyalog `N/A` aldı — aynı mekanizmanın yüze ve finale
> uygulanmaması **DERS 113**'ün konusudur.
> ✅ KİMLİK KAPISI [D105] GEÇTİ: iki metin-dışı çapa tuttu (V3 eldiven-konsol
> vuruşu + insan sayımı 2/0/0/1/0/0). Black Cradle'dan farkı budur.
> ⛔ Skor hiçbir tabloya girmedi. Kayıt:
> `01_FILM_RAPORLARI/THE_COLD_BURN_FRAGMAN.md`


# SHORTS_QA_CRITIQUE_PROMPT.md

> 📌 **Bu dosya hakkında** — Bu rubrik 31 Temmuz 2026'da sıfırdan yazıldı.
> Öncesindeki sürüm tek bir yapıma ("KULE 7") gömülüydü: karakter adı, kule
> yüksekliği ve sahne kuralları prompt gövdesine sabitlenmişti, dolayısıyla
> başka hiçbir dikey filme uygulanamıyordu ve o film bu depoda yok.
> Film-özel her şey artık SPEC BLOĞU'ndadır; rubrik boştur ve tekrar
> kullanılabilir. Kategori 1-8 isimleri `VIDEO_QA_CRITIQUE_PROMPT.md` ile
> bilerek aynıdır — dikey ve yatay skorlar aynı kalite tablosunda
> karşılaştırılabilsin diye.
>
> **03.08.2026 — kapsam genişletildi.** Rubrik 12 kategoriyle yalnız tek bir
> 8 saniyelik klibin *kare içi* tekniğine bakıyordu. Yatay hattın üç merceği
> var (VIDEO_QA · MANTIK_QA · SENARYO_QA), dikey hattın yalnız bu dosyası —
> yani sahneler arası kayma, anlatı ve müzik dikeyde **hiçbir rubriğe ait
> değildi.** Eklenenler:
>
> ```
> STEP 0    MOD KAPISI — tek klip / tam kurgu / klip seti. Hangi kategoriyi
>           puanlamaya hakkın olduğunu mod belirler.
> STEP 0.5  SPEC DOĞRULAMA KAPISI — VIDEO_QA ve SENARYO_QA'da 31.07'de vardı,
>           bu rubrikte yoktu. Künye uyuşmazsa puanlama yapılmadan durulur.
> §13       SAHNELER ARASI MANTIK — MANTIK_QA'nın 8 kategorisinin dikeye
>           sığdırılmış hâli. Her bulgu İKİ timecode taşır.
> §14       SENARYO & AKTARIM — 48 saniyede tek soru: novum ulaştı mı?
> §15       TUTUNDURMA — 0-3s / 10s / 30s düşüş noktaları, loop, sessiz izleme.
> §16       MÜZİK & SES — GOOGLE_FLOW_MUSIC kılavuzuna bağlandı. Depodaki
>           kapsam haritasında müzik "rubrik yok" satırıydı; artık burada.
> Ders      Tablo 42'de bitiyordu; 43-59 arası dersler eklendi ve "klip içi" /
>           "sahneler arası" diye ikiye ayrıldı.
> Sapma     DELIBERATE DEVIATIONS alanı — bu dokümanlar kendi sapmalarını
>           açıkça kaydediyor; rubrik onları ihlal diye saymamalı.
> Filtre    Öneri tablosuna içerik filtresi kuralı: filtreler olumsuzlamayı
>           okumaz, kelimeyi eşler. `no zombie` yazmak `zombie` yazmaktır ve
>           bu depoda bir üretim reddine yol açtı (THE SLOW STONE S4).
> ```
>
> **05.08.2026 — İKİ ÇALIŞTIRMA · İKİ BAŞARISIZLIK · DERS 63-66.**
> Bu satır daha önce "bu rubrik hâlâ hiç çalıştırılmadı" diyordu ve **yanlıştı.**
> Rubriği açan ajan "denenmemiş" okuyordu; doğrusu şudur:
>
> ```
> ÇALIŞTIRMA SAYISI : 4
> 03.08.2026  künye ekrandaki jenerik kartından uyduruldu → DERS 60 · 62
> 05.08.2026  aynı dört künye satırı birebir tekrarladı   → DERS 63-66
> 06.08.2026  THE FIRST MORNING · MOD V — İLK GEÇERLİ KOŞU ✅
>             künye uydurulmadı, kendi numaralandırmasını beyan etti,
>             aritmetik kapı tuttu (84.0 ÷ 14 = 6.0). Bulgulardan
>             DERS 70 (kurgu 64 s + jenerik kartı) ve DERS 71 (analog
>             merak perdesi) çıktı.
> 06.08.2026  THE WRONG SHADOW · MOD V — İKİNCİ GEÇERLİ KOŞU ✅
>             künye uydurulmadı (`(not supplied)` ✅ Ders 60/65), aritmetik
>             kapı tuttu (73.0 ÷ 13 = 5.6), FLAGS soruları belgeyle
>             cevaplandı. Bulgulardan DERS 73 (novum türetilmiş fenomene
>             yüklenmez — çift gölge 0 kare, dönme jalonlara transfer) ve
>             DERS 74 (kayıtsız kapı koşulmamış kapıdır) çıktı. DERS 70
>             İKİNCİ vaka: yine 64 s + jenerik kartı. SONUÇ: 2/4 geçti.
> 17.08.2026  THE BLACK CRADLE — FRAGMAN · MOD B + MOD V · 6.5/10
>             REGENERATE. Rubrik kapıları TUTTU: künye uydurulmadı
>             (`FILM: (not supplied)` ✅ D60/65), aritmetik kapı tuttu
>             (97.0 ÷ 15 = 6.47). ⛔ AMA KOŞU ATFEDİLEMEDİ: raporu
>             fragmana bağlayan tek kanıt 00:58'deki başlık kartının
>             yazısıydı; elle eşlemede 6 vuruşun 3'ü sırası bozuk
>             eşleşti, 2'si yok, 2 çekim hiçbir belgede geçmiyor.
>             → DERS 105 (kimlik kapısı) · DERS 106 (rubrik fragmanı
>             film sanıyor: borç bırakmayı cezalandırdı, D69'un kadraj
>             dışı bıraktığı binişi nedensellik hatası yazdı).
>             DERS 70 ÜÇÜNCÜ vaka: 63 s + ~10 s sahneler + başlık kartı.
>             D94'ün 7. vakası (SPEC fragman dosyasında hazırdı).
>             Rapor SCENE INVENTORY yazmadı — D105 yaması tam buna
>             bakıyor. SONUÇ: 3/5 geçti, 1'i atfedilemedi.
> 20.08.2026  LOW POWER — FRAGMAN · MOD B + MOD V · SKOR YOK
>             ✅ MERCEK İLK KEZ DOĞRU: SHORTS_QA + `MATERIAL TYPE: TEASER`
>             beyan edildi (Cold Burn'e SENARYO_QA koşulmuştu → D111).
>             ✅ SCENE INVENTORY yazıldı (D105 yaması tuttu) ve kimlik
>             kapısı 3/2 çapayla GEÇTİ — kartın yazısı kanıt sayılmadı.
>             ⛔ Rapor kategori skoru (n/10) üretmedi: QUALITY TABLE ROW
>             yok, tabloya satır girmedi [D65].
>             🚨 D112 PARMAK İZİ ŞÜPHESİ AÇILDI: künye (64 s · 7 segment ·
>             ~10 s sahne · sonda kart) bu rubriğin son üç koşusuyla ±%5
>             içinde aynı. Süre ve sahne sayısı hiçbir kapıya girdi
>             sayılmadı; operatörden dosyanın kendi süresini okuması
>             istendi. DERS 70'in BEŞİNCİ vakası (64 s + kart).
>             Geçerli bulgular: kart (🔴 ×2) · toz sıvı gibi (belgenin
>             1 numaralı öngörülen riski) · temas erimesi · video-game
>             görünümü. Defterde 7 madde, 5'i ⬜ AÇIK.
>             Rubriğin göremediği asıl sapma operatör tarafında bulundu:
>             son üç vuruş YER DEĞİŞTİRMİŞ → mekanik merdiveni kırık,
>             kapanış soru değil manzara, ZORUNLU loop dikişi imkânsız.
>             Kayıt: FILM_QA_RAPORLARI/01_FILM_RAPORLARI/LOW_POWER_FRAGMAN.md
> ```
>
> **Kök neden (Ders 63):** 03.08'de `eec615c` commit'i Ders 60/61/62'yi yazdı
> ve **dört rubriği** düzeltti — VIDEO_QA · SENARYO_QA · MANTIK_QA · KAPAK_QA.
> Ders 60 ve 62'yi ÜRETEN dosya, yani bu dosya, yamayı almadı
> (`grep -c "DERS"` → 0). İki gün sonra aynı hatayı üretti.
> Bu sürümde eklenenler: STEP 0.5.a arama zorunluluğu · 0.5.b iki dur kodu
> (alan değil) · aritmetik kapı · başlık çarpışma kapısı · öneri tablosunun
> kopyalama kuralı · sıfır tabanlı sahne numaralandırma.
>
> ✅ **Skor tablosu 06.08.2026'da AÇILDI** —
> `../FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md`. QUALITY TABLE ROW
> çıktısı artık oraya yapıştırılır (LESSONS_LEARNED teknik tablosuna DEĞİL —
> o tablo yatay VIDEO_QA'nındır). İlk iki satır: First Morning Ⓥ 6.0 ·
> Wrong Shadow Ⓥ 5.6. Başarısız çalıştırmalar tabloya satır yazamaz. [Ders 65]

> 🔎 **DERS 72:** teslim kurgusu plan sayılarıyla (klip sayısı · süre ±2 s ·
> ekran metni 0.0 sn · CENTRAL CHOICE sahnesi kurguda VAR) doğrulanmadan
> hiçbir mercek koşulmaz — ayrıntı: `../LESSONS_LEARNED.md` DERS 72.
>
> 🔎 **DERS 73 (06.08.2026 · THE WRONG SHADOW):** novum'u türetilmiş optik
> fenomen (gölge · yansıma · kostik) taşıyan bir filmde, fenomen ekranda
> HİÇ yoksa bunu tek bir kayıp bulgu değil KÖK NEDEN olarak raporla:
> imkansız davranışın birincil bir nesneye transfer olup olmadığına bak
> (Wrong Shadow'da "dönen gölge" → "havada dönen jalon" oldu). Mod V'de
> bu transfer, fizik ihlali gibi görünür — FLAGS'e "bu davranış başka bir
> taşıyıcı için mi yazılmıştı?" sorusunu ekle.
>
> 🔎 **DERS 74:** bu rubrik, KAPI KAYDI (tek-kare fizibilite · üretim
> sırası · kurgu kapısı sonuçları) olmayan bir teslime koşulmuşsa skor
> geçerli kalır ama tabloya DERS 72 şerhiyle iner — operatör notu zorunlu.

> 🔎 **DERS 75 (06.08.2026 · THE STARLESS CIRCLE):** Bu rubrik de kendi
> malzemesini ölçmek zorundadır. Kurgu yerine tek klip verilirse — süre
> < 60 s VE kesme 0 — yapı/yay/final/tutundurma sınıfı kategoriler
> UNVERIFIABLE yazılır, ortalamaya girmez ve satır `🚨 KLİP` işaretlenir.
> Yatay senaryo merceği bunu yapmadığı için 12 saniyelik bir çekime
> "no peak located · ends mid-stride" diye üç dakikalık filmin puanını
> verdi. Ayrıntı: `SENARYO_QA_CRITIQUE_PROMPT.md` STEP −0.5.

> 🔎 **DERS 80 (07.08.2026 · THE BLIND RETURN):** Malzemenin YETERSİZ
> olması (D75) ile HİÇ OLMAMASI ayrı kapılardır. Oynatılabilir video ekli
> değilse — süre ölçülemiyor, 0 s okunuyor, tek kare çözülemiyor — tek
> legal çıktı `MEDIA MISSING — RUN NOT STARTED` bloğudur: skor yok,
> verdict yok, severity yok, tablo satırı yok. Yatay VIDEO_QA bu kapı
> olmadan videosuz koşuya REGENERATE verdikti yazdı.
>
> 🔎 **DERS 81 (07.08.2026 · THE BLIND RETURN):** Kurgu kapısı (D70)
> iki madde büyür: ⑤ klip SIRASI = plan sırası (son üç klip elle
> doğrulanır) · ⑥ planın her Çehov halkasının KURULUM sahnesi kurguda
> VAR. Yatayda tek eksik kurulum sahnesi + tek yer değiştirme, üç merceği
> birden "yapısal çöküş"e götürdü ve kesme reçetesi planlı finali hedef
> aldı.

---

# KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md
> 🔎 **20.08.2026 — THE BLUE DRIFT (mod V · parti 🚨 GEÇERSİZ):** Sahne envanteri
> MANTIK raporuyla BİREBİR aynı (15 blok, aynı zaman kodları, aynı üç bulgu) —
> D110'un tarif ettiği ortak defterin en net vakası: iki rapor aynı sayıyı verdi
> ve ikisi de on sahne yanlıştı, yani çapraz sayım kapısı fark 0 görüp ikisini de
> DOĞRULANMIŞ ilan ederdi (**DERS 115**). İki 🔴'sinden biri (4:10 kimlik kırılması
> + yara izi) filmin sahnesi olmayan başlık kartındadır; 3:50 için "yüzler temiz"
> dedi, VIDEO aynı saniye için "iki yüz birden morph" dedi — ⬜ AÇIK.
> Kanıt tabanı: yüz ~%9 (D97 eşiği altında, rapor kendi ölçüsünü yazdı ✅).
> Kayıt: 01_FILM_RAPORLARI/THE_BLUE_DRIFT.md
> 🔎 **17.08.2026 — THE BLACK CRADLE (🚨 GEÇERSİZ koşu):** Rubriğin **KANIT TABANI
> EŞİĞİ ilk kez ihlal edildi** (D97'nin 2. vakası): raporun kendi ölçümü yüz için
> 1/4 sahne · ~25 s / 232 s (%11) diyor, eşik "3 sahneden az VEYA %25'ten az →
> ⚠️ PARTIAL, sayı YOK" diyor, sekiz sütunun yedisi yine puanlandı. Pasaportlar
> 4 sahnelik envanterden kuruldu (**DERS 107**) ve **Ses 5/10** aynı filme SES_QA
> koşulduğu hâlde puanlandı — kart E2 adım 5 gereği →🔊 işaretçisine inmeliydi
> (**DERS 108**). Kilit çelişkisi: altın tonlu vizör ↔ optik berrak kilidi [D79/D95],
> kırık beyaz suit ↔ mat kömür siyahı kilidi; aynı dosyada VIDEO_QA "dark matte +
> orange/teal" yazdı, yani iki rapor birbirini de yalanlıyor.


> 📌 **Bu dosya hakkında** — 05.08.2026'da yazıldı. Yatay formatın karakter
> merceği: MANTIK_QA'nın 5. kategorisinin (kostüm-prop) karakter tarafını
> alır ve derinleştirir — AI üretiminde oyuncu her çekimde yeniden üretilir,
> kimlik her sahnede yeniden kazanılmak zorundadır; bu rubrik o sözleşmeyi
> denetler.
>
> ```
> VIDEO_QA      kare içi         tek klip teknik olarak doğru mu
> MANTIK_QA     sahneler arası   film kendi kendisiyle çelişiyor mu
> KARAKTER_QA   sahneler arası   karakter aynı karakter mi        ← bu dosya
> SES_QA        film boyu        doğru ses doğru bedenden mi çıkıyor
> SENARYO_QA    dramatik         hikayeyi kimse umursar mı
> ```
>
> 🔊 **SES_QA ile sınır (09.08.2026):** beden buranın, ses oranın. 8. kategori
> (Ses) SES_QA ile birlikte koşulduğunda `→ SES_QA` işaretçisine iner ve
> puanlanmaz — aynı kayma iki tabloya iki kez yazılmaz. Yalnız bu mercek
> koşuluyorsa kategori normal puanlanır. Kart E3 adım 6.
>
> **Sınır:** karakterin ÜZERİNDE/ELİNDE olan her şey buranın; dünyaya ait
> olan her şey MANTIK_QA'nın. Kare İÇİ morph VIDEO_QA'nın. MANTIK_QA ile
> birlikte çalıştırılırsa kostüm bulguları burada raporlanır, MANTIK_QA
> raporundaki kesişen satırlar birleştirmede teke indirilir.
>
> **Neden doküman istemiyor:** 8 kategorinin 8'i de karakterin kendi
> geçmişiyle çelişkisine bakıyor; hepsi ekranda görünür. Bible'a uygunluk
> sorusu burada puanlanmaz — `FLAGS FOR DOCUMENT CHECK` altına soru olarak
> yazılır, rapor geldikten sonra plan/bible ile karşılaştırılır.
>
> **Kapsam sınırı bloğunu silme.** Raporların çift sayım olmadan
> birleştirilebilmesinin tek garantisi odur.
>
> Çalıştırma kaydı: 1 kez çalıştırıldı · son 05.08.2026 (THE STONE SKY,
> 6/10 IDENTITY BREAK — klon bulgusu geçerli, DERS 69'u üretti) · sonuç:
> rubrik çalıştı, bir kural ihlaliyle — rapor `FILM:` alanına başlık
> kartından okuduğu adı yazdı; DERS 65 kuralı gövdede yazılıydı, tutmadı.
> Bir sonraki koşuda operatör çıktının FILM satırını kontrol etmeli.

> 🔎 **DERS 72 (06.08.2026 · THE UNBROKEN CITY):** Bu rubrik bir KURGUYU
> değerlendiriyorsa, operatör teslimden önce KURGU KAPISI'nı koşmuş
> olmalıdır: klip sayısı = plan SCENE COUNT · toplam süre = RUNTIME ±2 s ·
> ekran metni 0.0 sn (kapak çıktısı dahil) · CENTRAL CHOICE sahnesi kurguda
> VAR. Mod V koşusu kurgu hatasını içerik zaafı olarak raporlayabilir —
> Unbroken City'de senaryo merceği "zero choices" dedi, gerçek neden
> doruğun kurguya girmemesiydi. Mod V bulgularını tabloya işlerken film
> kaydındaki belge cevaplarıyla birlikte oku.
>
> Çalıştırma kaydı: son 06.08.2026 — THE UNBROKEN CITY (mod V, geçerli
> koşu). DERS 65 TUTTU: rapor `FILM: (not supplied)` yazdı.

> 🔎 **DERS 77 · 79 (06.08.2026 · THE STARLESS CIRCLE):** Klon üçüncü kez
> aynı yerden geldi: **araç/gemi BİNİŞ-İNİŞ anı** (Stone Sky araçtan iniş ·
> Unbroken City loş iç mekân · Starless Circle gemi merdiveni). Kategori
> 7'nin bu maddesini her koşuda kare kare tara; bulursan raporun ilk
> satırına yaz. [DERS 69 ×3 → DERS 77]
> Pasaport yazarken iki alanı ÖZELLİKLE doldur, çünkü belge kontrolünde
> en çok ihlal buradan çıkıyor: (a) sırt silueti — sırt ünitesi/tank/hortum
> var mı, (b) vizörün optik durumu — şeffaf mı, renkli/aynalı mı ve yüz kaç
> sahnede okunuyor. İki filmde de bible bunları YASAKLIYORDU. [DERS 79]
> Ayrıca **karakterin üzerindeki bedel nesnesini** (kalça/göğüs yuvası, ne
> takılı, ne eksik) pasaporta yaz: iki filmde de filmin doruğu bu nesnenin
> yokluğuyla anlatılıyordu ve pasaportta hiç geçmedi. [DERS 78]
>
> Çalıştırma kaydı: son 06.08.2026 — THE STARLESS CIRCLE (geçerli koşu,
> 6/10 · IDENTITY BREAK; klon 2:10 biniş sahnesinde). DERS 65 TUTTU:
> rapor `FILM: (not supplied)` yazdı. Önceki: aynı gün THE UNBROKEN CITY
> (8/10). Üç koşunun üçünde de örüntü aynı: yüz 8-9, SAYI 1.

> 🔎 **DERS 80 (07.08.2026):** Bu kural bu rubrikte de geçerlidir —
> oynatılabilir video ekli değilse tek legal çıktı `MEDIA MISSING — RUN
> NOT STARTED` bloğudur: skor yok, verdict yok, tablo satırı yok.
>
> 🔎 **DERS 81 (07.08.2026 · THE BLIND RETURN):** "Cross-Cut Action"
> MAJOR'ları filmin SON bloğunda kümeleniyorsa ve bir yıpranma izi finalde
> "sıfırlanmış" görünüyorsa, tabloya işlemeden önce kurgu SIRASI plandan
> doğrulanır: bu koşuda "silinen hasar" planlı YENİ vizördü, ama onu kuran
> Çehov sahnesi (S15) kurgudan düşmüştü ve S16↔S17 ters sıralanmıştı —
> üç MAJOR'ın üçü tasarım/kurgu çıktı, devamlılık ihlali değil. [DERS 81]
>
> Çalıştırma kaydı: son 07.08.2026 — THE BLIND RETURN (geçerli koşu,
> 4/10 · DRIFTS BUT RECOVERABLE; klonsuz — tek karakter, Sayı N/A).
> DERS 65 TUTTU: `FILM: (not supplied)`. DERS 79 dipnotunun iki pasaport
> alanı işe yaradı: pasaport `Backpack` + `dual headlamps` yazdı, belge
> kontrolü ikisini de bible ihlali olarak yakaladı (D79'un 3. vakası);
> sağ uyluktaki tüp de ayna adayı çıktı (bible: SOL uyluk).

> 🔎 **DERS 82 (09.08.2026):** SES_QA aynı filme koşulduysa 8. kategori
> `→ SES_QA` işaretçisine iner (yukarıdaki kural) — ilk uygulama bu koşu.
>
> Çalıştırma kaydı: son 09.08.2026 — THE COLD BURN (geçerli koşu, 6/10 ·
> DRIFTS; deponun ilk İKİ karakterli koşusu — KLONSUZ, D69/77 sıcak
> noktası tekrarlamadı, ama planın en riskli sahnesi S25 tünel zaten
> kurguda yoktu). DERS 65 TUTTU. D79 pasaport alanı 4. kez iş gördü:
> iki suitte de `backpack`, bible SIRT DÜZ diyor (üretim zinciri şerhli —
> film kaydına bak). Renk ayrıştırması TUTTU: turkuaz/amber bantlar iki
> karakteri her sahnede ayırdı.


> 🔎 **DERS 84 · 86 (11.08.2026 · THE THIRD DUNE):** Pasaport iki yeni şey
> gösterdi. ① **Yıpranma 3/10'un sebebi eksik cümle DEĞİL:** toz seviyesi
> 3 kademeli sayısal takvimle 42 promptun hepsine, temiz referans şeridi
> çapasıyla birlikte yazılmıştı; 2:29'da kaskatı kumlu iki suit 2:40'ta
> tertemiz. Bant rengi (16 promptta yazılı) 2:10'da kayboldu, sırt ünitesi
> yasağı (42/42) yine tutmadı → **D79'un 5. vakası, ilk kez cümlenin
> VARLIĞINA rağmen.** Sahneler arası durum metinle kilitlenmiyor → D84.
> ② **Kesme 6/10:** iki figür kesmelerde sol/sağ yer değiştiriyor. Ekran
> yönü kilidi yürüyüş yönünü ve araç tarafını kilitliyor ama "kim solda"yı
> kilitlemiyor → D86.
> ⭐ Bu koşu deponun **ikinci iki karakterli** koşusu ve ikincisi de
> KLONSUZ (Sayı 9/10) — D69/77 sıcak noktası (araç biniş-iniş, kargo
> boşaltma) bu filmde tekrarlamadı. Yüz 9/10; örüntü (yüz tutar, sayı
> tutmaz) ilk kez iki koşu üst üste kırıldı.
>
> Çalıştırma kaydı: son 11.08.2026 — THE THIRD DUNE (geçerli koşu, 7/10 ·
> DRIFTS BUT RECOVERABLE). DERS 65 TUTTU. 8. kategori `→🔊`'ye İNMEDİ ve
> puanlandı, çünkü aynı filmin SES_QA koşusu girdisiz kaldı (geçersiz).

---

> 🔎 **16.08.2026 — THE LAST SHIFT (mod V):** ⭐ **DERS 95 ve DERS 97 ilk kez
> ÖLÇÜLEBİLİR biçimde TUTTU.** Rapor yüz sütununu `⚠️ UNVERIFIABLE` bıraktı
> ve kanıt tabanını sayıyla yazdı (kadın 0 s / 14 sahne · erkek ~10 s / 2
> sahne); kaskı "sealed — evidence: solid visor pane and collar lock" diye
> KANITLA kaydetti. Ring Light koşusunda aynı iki sütun 9/10 yazılmıştı.
> ✅ D89 de tuttu: filmin tek ekipman değişimi (S10'da SAĞ eldiven) tam
> olarak görüldü, ikinci mühür açılmadı. 🔴 Kostüm 2/10 (2:20'de bant SOL
> koldan SAĞ kola geçiyor) kilit çelişkisi defterinde ⬜ AÇIK [D96] —
> raporun 0:20 taban okuması kilide birebir uyduğu için ön kabul güçlü.
> Kayıt: 01_FILM_RAPORLARI/THE_LAST_SHIFT.md


# SES_VE_DIYALOG_QA_CRITIQUE_PROMPT.md
> 🔎 **20.08.2026 — THE BLUE DRIFT (mod V · parti 🚨 GEÇERSİZ):** AUDIO STATE A,
> 23 replik zaman koduyla yazıldı. ⭐ **Partinin en değerli belgesi bu ledger
> oldu:** 16 planlı repliğin 14'ü, planın ızgarası + prompt içi replik ofsetiyle
> hesaplanan saniyeye ±2 s içinde oturdu — sıra denetimi master açılmadan yapıldı
> (**DERS 115**). Register: rapor 2 ses / 0 MACHINE dedi, plan 10 replik MACHINE
> (KERTE) diyor → kart E3 adım 2 gereği "sentetik duruyor" bulguları İŞLENMEDİ,
> soru ⬜ AÇIK (Cold Burn D82'nin aynı sorusu, bu kez sigorta 25 promptun
> gövdesinde yazılıydı). Dört replikte metin sapması şüphesi (sayı 1→40, verici→
> itici, metre→pencere, havanız iticinizdir→avanis içimizdedir) + iki replik
> tekrarı: hepsi defterde. Kayıt: 01_FILM_RAPORLARI/THE_BLUE_DRIFT.md
> 🔎 **17.08.2026 — THE BLACK CRADLE (🚨 GEÇERSİZ koşu):** Ses defteri **2 replik**
> içeriyor; plan 14 replik / 12 sahne diyor ve ölçülen bandın içinde bile en az 7
> replik var. Ortam haritası 4 satır — bu merceğin ana sorusu ("yatak kesmelerde
> ölüyor mu") ancak kesme sayısıyla sorulabilir ve aynı dosyada VIDEO_QA 21 kesme
> saydı (**DERS 107**). ⭐ **Kart E3 adım 2 çalıştı ve iki hata buldu:** 0:30 repliği
> doğru şekilde MACHINE ama ekrandaki kadına atfedildi (MİRA gövdesizdir — D82
> sınıfı bir atıf hatası, üstelik rapor Atıf'a 8/10 verdi); 1:09 repliği planda
> HUMAN iken MACHINE yazıldı. Ayrıca Performans · SFX · Miks hücrelerinin kaynağı
> kapsam dışı iki olay (dudak senkronu · vakumda ses) → **DERS 108**, düzeltilmiş
> okuma ~8.8.


> 🔎 **14.08.2026 — THE BANDED DEEP (2. koşu, GEÇERLİ):** STATE B doğru
> teşhis (0 replik TASARIM — rapor sessizliği gap saymadı, FLAGS'e soru
> yazdı ✅). 6.2 SOUNDTRACK HOLDS; üç bulgu da FIXABLE IN THE MIX (ambiyans
> crossfade ×2 · eldiven Foley · iniş gürlemesi). Müzik 0:00'da girmiş —
> plan §3.2'ye aykırı, kurgu/miks kaydına işlendi. OUT-OF-SCOPE sınırı
> tuttu: toz fiziği ve başlık kartını VIDEO_QA'ya devretti.

> 📌 **Bu dosya hakkında** — 09.08.2026'da yazıldı. Yatay ve dikey hattın
> **ses merceği**: VIDEO_QA'nın 8. kategorisinin (Diyalog ve Ses) ses tarafını
> alır ve film boyuna yayar. Gerekçe: VIDEO_QA tek klibe bakar ve ses onun 11
> kategorisinden biridir; oysa bu projenin bilinen en düşük skorlarından ikisi
> tam olarak o kategoridedir (Low Power 3/10 · Dead Approach 3/10) ve ikisi de
> hiçbir özet tabloda görünmüyordu. Konuşmacı atfı, ses kimliği kayması ve
> ortam sesinin her kesmede ölmesi ancak KURGUNUN TAMAMI dinlenerek görülür.
>
> ```
> VIDEO_QA      kare içi         tek klip teknik olarak doğru mu
> MANTIK_QA     sahneler arası   film kendi kendisiyle çelişiyor mu
> KARAKTER_QA   sahneler arası   karakter aynı karakter mi
> SES_QA        film boyu        doğru ses doğru bedenden mi çıkıyor   ← bu dosya
> SENARYO_QA    dramatik         hikayeyi kimse umursar mı
> ```
>
> **İki ana soru:** ① doğru karakter mi konuşuyor · ② insan olması gereken ses
> insan gibi mi, makine olması gereken ses makine olarak mı KALIYOR.
>
> ⭐ **REGISTER SÜTUNU BU RUBRİĞİN OMURGASIDIR.** Bu seri diegetik yapay ses
> kullanıyor — suit AI, gemi bilgisayarı, kayıt oynatma (The Blind Return: 8
> repliğin 8'i SUIT AI, kadın hiç konuşmuyor; The Cold Burn: 12 replik, hepsi
> kask telsizi veya gövdesiz AI). Bir sesin "yapay" duyulması bu filmlerde
> çoğu zaman TASARIM. Register belirlenmeden verilen "AI gibi konuşuyor"
> bulgusu, çalışan tasarımı bozmaya yönlendirir — Low Power senaryo raporunun
> filmde zaten var olan iki şeyi eksik sayması gibi. Register UNCLEAR ise
> kategori 2 o repliği PUANLAMAZ, soruya çevirir.
>
> **Sınırlar — kapsam bloğunu silme:**
> ```
> dudak-fonem uyumu · vakumda ses · altyaz  → VIDEO_QA §8 (D35 · D40)
> bedenin devamlılığı, kostüm, yıpranma      → KARAKTER_QA
> olayın dünya mantığı                       → MANTIK_QA
> repliğin YAZIMI, altmetin, işlev           → SENARYO_QA
> müziğin bestesi/prodüksiyonu               → hiçbiri (kılavuzda kabul kriteri)
> ```
> KARAKTER_QA ile birlikte koşulursa **ses bulguları burada raporlanır**,
> KARAKTER_QA'nın 8. kategorisi (Ses) işaretçiye iner — aynı kayma iki tabloya
> iki kez yazılmaz. Kart E3 adım 5.
>
> **Neden doküman istemiyor:** 9 kategorinin 9'u da ses ile görüntü arasındaki
> çelişkiye bakıyor; hepsi kurguyu dinleyerek duyulur. Senaryoya uygunluk
> burada puanlanmaz — `FLAGS FOR DOCUMENT CHECK` altına soru yazılır, rapor
> geldikten sonra plan dosyasıyla karşılaştırılır (kart E3 adım 2).
>
> **STEP 0 neden var:** bu depodaki filmlerin çoğu bilinçli olarak SESSİZ.
> Sessiz film ile sesi ihraç edilmemiş dosya kulakta aynı — ikisi ayrılmadan
> puanlanırsa ya tasarım cezalandırılır ya teslim hatası kaçar. DERS 80'in
> medya kapısının ses karşılığıdır.
>
> Çalıştırma kaydı: 1 kez çalıştırıldı · son 09.08.2026 (THE COLD BURN,
> 5/10 AUDIBLE DRIFT — yazıldığı gün koşuldu) · sonuç: **rubrik çalıştı.**
> STEP 0 kapısı AUDIO STATE: A ilan etti, ledger + register haritası tam
> dolduruldu, DERS 65 tuttu (`FILM: (not supplied)`), beş mercek aynı 225 s
> kurguyu ölçtü (D75 ✅). İki yeni ders üretti — rubriğin iki ana kategorisi
> ilk koşuda karşılığını buldu:
> `07_SES_KALITE_TABLOSU.md` bu koşuyla açıldı.

> 🔎 **DERS 82 (09.08.2026 · THE COLD BURN):** Register haritası yalnız
> kategori 2'nin kapısı değil, PLANLA KARŞILAŞTIRILACAK bir kanıttır.
> Bu koşuda harita 7 replik / 7 HUMAN / 0 MACHINE dedi; plan 12+ replik /
> tümü kask telsizi + gövdesiz AI diyordu — ses mimarisi üretimde tersine
> dönmüştü (AI silinmiş, replikleri ekrandaki ağızlara devredilmişti) ve
> bunu mod V'de hiçbir skor göremezdi. Operatör: raporu tabloya işlemeden
> önce register haritasını planın DIALOGUE SCHEDULE'ıyla karşılaştır
> (kart E3 adım 2); comms filtresinin kask durumunu değil sahne değişimini
> takip etmesi de aynı ihlalin ses tarafıdır. [DERS 82]
>
> 🔎 **DERS 83 (09.08.2026 · THE COLD BURN):** Kategori 6'nın "signature
> failure" öngörüsü ilk koşuda doğrulandı — 20 s mutlak dijital sessizlik
> (1:20-1:40) + kesmelerde ölen yatak + cümle ortasında kesilen müzik.
> Bulguların çoğu miks seansıyla kapandı; "FIXABLE IN THE MIX" ayrımı
> raporun en işe yarar çıktısıydı. Teslim öncesi SES KAPISI (yatak · sıfır
> yasağı · kesme testi · ducking) kurgu kapısının beşinci maddesidir;
> kapı koşulmadan gelen kurguda bu rubrik aynı bulguları tekrar üretecektir.
> [DERS 83]

> 🔎 **DERS 72 · 80 (bu rubrikte de geçerli):** Değerlendirilen şey bir KURGU
> ise operatör teslimden önce KURGU KAPISI'nı koşmuş olmalıdır (klip sayısı =
> plan · süre ±2 s · doruk sahnesi kurguda VAR). Oynatılabilir video ekli
> değilse tek legal çıktı `MEDIA MISSING — RUN NOT STARTED`; ses kanalı hiç
> yoksa `AUDIO ABSENT — RUN NOT STARTED` (STEP 0).

> 🔎 **DERS 75 (mod V malzeme kapısı) bu mercekte daha da sert:** dört/beş
> mercek AYNI dosyayı ölçmelidir. Ses merceği tek bir klibe koşulursa ortam
> devamlılığı, ses kimliği kayması ve miks sıçraması kategorilerinin dördü
> birden ANLAMSIZDIR — bu rubriğin ölçtüğü şeylerin çoğu yalnızca kesmelerin
> ARASINDA yaşar. Tek klibe koşulan bir SES_QA satırı tabloya girmez.

---

# FILME_OZEL/THE_LAST_SPAN_QA_CRITIQUE_PROMPT.md  ⏸️ DOSYA KALDIRILDI

> **Yazıldı:** 25.08.2026 · **Çalıştırma kaydı:** 0 kez — hiç koşulmadı.
>
> ⏸️ **26.08.2026'da KALDIRILDI (kart H2):** filmi depodan çıktı, zombi
> türü kapandı, depo yalnız UZAY filmleri içindir. Aşağıdaki kayıt
> TARİHSEL olarak duruyor — rubriğin NİYE yazıldığı, uzay hattında
> tekrar edilebilecek bir muhakemedir.
>
> ⭐ **Türden bağımsız yarısı KURTARILDI:** yanlış-pozitif duvarı
> `FILME_OZEL/00_YANLIS_POZITIF_DUVARI_SABLONU.md` dosyasına damıtıldı ve
> uzay hattına uyarlandı. Duvar depoda yalnız üç filme özel rubrikte
> yaşıyordu ve genel rubriklerde karşılığı yoktu; bu kaldırma onu
> yeniden kullanılabilir hâle getirdi. Kalan iki örnek: THE BLUE DRIFT ·
> THE RING LIGHT.

```
NEDEN VAR — genel mercek bu filmde İKİ YÖNDE birden yanılıyor:
  ① YÜRÜYEN ZOMBİ genel rubrik için HATA DEĞİLDİR — türün normalidir
     ve geçer. Oysa bu filmde tek kare yürüyüş premisi SİLER.
     Premis bir YAPAMAMA: formlar kendi başlarına harekete geçemez.
     Bir yokluğu doğrulayacak alet, o yokluğu BİLMEK zorunda.
  ② PASİF KALABALIĞI genel rubrik "tehdit yok / antagonist inert /
     korkutucu değil" diye cezalandırır — yani çalışan tasarımı
     bozmayı önerir. Ring Light emsalinin ("durgun film") daha
     keskin hâli.

ALETİN ÇEKİRDEĞİ — KAPALI HAREKET LİSTESİ
  Bir form yalnız ÜÇ şeyden birini yapabilir:
    ① durma (0 hareket) ② rijit devrilme (taban ekseninde, ayak düz,
    diz düz, kol yanda, 1,1 s, yerde kalır) ③ ≤4 cm omuz salınımı
  Rubrik HAREKET SAYIMI (motion census) kurdurur: her form hareketi
  tek tek loglanır ve üçünden birine atanır. Atanamayan satır
  PREMİS KIRILMASI'dır ve tek satır bile kapıyı düşürür.
  ⭐ Yumuşak odak DETAYI affeder, SİLUET ve KONUMU affetmez.

ÇIKTI    skor değil KARAR: ACCEPT / FIX IN EDIT / REGENERATE
         BLOK A (6 premis kapısı, PASS/FAIL) her şeyi ezer
         BLOK B (12 ölçülmüş kilit) · BLOK C (4 kategori, tek yer
         zevkin bulunduğu: kural OKUNUYOR MU)
         ⭐ C1 KURAL OKUNABİLİRLİĞİ: modele önce "bir izleyici kuralı
         nasıl ifade ederdi" yazdırılır, SONRA gerçek kuralla
         karşılaştırılır. Kuralı okunmayan film zayıf premisli değil,
         PREMİSSİZ filmdir.

YANLIŞ-POZİTİF DUVARI — 13 madde, hepsi tür refleksi:
         pasiflik · kalkmama · sessizlik · yüzsüzlük · kansızlık ·
         sabit kamera · 0 kesme · replik yok · 7 sahnede hiç devrilme
         olmaması · kasksız kadın · tek renk · yapay ışık yok ·
         çözümsüz final. Hepsi TASARIM; hepsi genel rubriğin
         "eksik" diyeceği yerler.

TABLOYA GİRMEZ: /4 paydası ve T1-T6 dokunulmaz. Bu bir üretim
         kapısıdır, mercek değil; genel merceklerin ÖNÜNDE durur.
```

> ⚠️ Bu dosya Ring Light'ın bilinen borcunu TEKRARLAMADAN yazıldı:
> gövde tamamen İngilizce, ders numarası/tarih/film-dışı depo yolu yok,
> ortak çekirdek kapıları yerinde. Türkçe yalnız başlık satırında.

---

# FILME_OZEL/THE_BLUE_DRIFT_QA_CRITIQUE_PROMPT.md

```
0 kez çalıştırıldı · 18.08.2026'da yazıldı · film-özel ÜRETİM KAPISI
(mercek değil; skorları 03-07 tablolarına GİRMEZ, 6'lık sayıma girmez)

NİYE AÇILDI: S1 videosunda figür/iş/araç doğru çıktı, ARKA PLAN değişti.
Kök sebep prompt tarafındaydı — gezegen ve zemin çapa blokları IMAGE
promptunda tam, VIDEO promptunda parafrazdı. Genel rubrikler bu ayrımı
yapamaz: ekranda gördükleri hatayı MODELE fatura ederler. Bu rubriğin tek
yeniliği ATIF KAPISI'dır — her bulgu üç etiketten birini alır:
  🅐 MODEL DRIFT  kilit prompt'ta VAR, ekran uymadı
  🅑 PROMPT GAP   kilit prompt'ta YOK/zayıf — aynı promptla yeniden üretim
                  aynı hatayı üretir (para iki kez yanar)
  🅓 UNATTRIBUTED as-built prompt verilmedi
Bu yüzden rubrik MOD K'ya ek olarak AS-BUILT PROMPT ister; verilmezse
YENİDEN ÜRET kararı yasaktır.

MOD: her zaman D (SPEC gövdeye gömülü) · girdi: 1 klip + sahne no +
as-built prompt · S1 sahne bloğu tam, diğer sahneler için film-geneli
kilitler geçerli (sahne bloğu eklenerek büyütülür).

KOŞU KAYITLARI (her koşu TEK SATIR):
1 kez çalıştırıldı · son 18.08.2026 · S1 klibi (as-built V1) · sonuç:
  GÖZLEM SETİ — rapor çıktı şablonunu kullanmadı (künye/ledger/zaman
  kodu/atıf/skor/karar yok), bu yüzden hiçbir kategoriye sayı yazılmadı
  ve atıf operatör tarafında yapıldı. 5 bulgu: 3'ü 🅑 PROMPT GAP
  (prop boşluğu ×2, vizör görünürlüğü), 2'si 🅐 MODEL DRIFT (ses, temas
  erimesi). ⬜ C2 (arka plan sabitliği) ÖLÇÜLMEDİ — kapının açılış
  sebebi hâlâ açık. Rubrik aynı gün sertleştirildi: FORMAT NOT FOLLOWED
  durdurma koşulu + ledger'da ilk/son kare karşılaştırması zorunlu.
  Kayıt: FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_BLUE_DRIFT.md
```

---

## ⭐ 26.08.2026 — THE ROSE COAT · BEŞ MERCEK · SPEC HAZIRDI, BEŞİ DE MOD V

> Kayıt: [`../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_ROSE_COAT.md`](../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_ROSE_COAT.md)

```
① KARE        Ⓥ mod V · 5,0 · REGENERATE   · SPEC VARDI, verilmedi
② DEVAMLILIK  belgesiz  · 7,2 · STRUCTURAL  · (bu mercek zaten belgesiz koşar)
③ SES         belgesiz  · AUDIO ABSENT — RUN NOT STARTED
④ HİKAYE      Ⓥ mod V · 2,3 · REWRITE PREMISE · SPEC VARDI, verilmedi
⑤ ARKA PLAN   belgesiz  · 6,0 · FIELD DRIFTS
```

> 🔎 **DERS 129 (26.08.2026 · THE ROSE COAT):** SPEC dosyası filmin
> klasöründe hazırdı (`THE_ROSE_COAT_QA_SPEC.md`) ve beş merceğin beşi de
> mod V koşuldu. D117'nin çözümü uygulanmıştı — erişim engeli kalkmıştı.
> Bedeli: ④'ün kesme listesindeki beş adayın beşi de yük taşıyan sahne;
> ikisi SPEC'te "KESİLEMEZ" yazan viral; dördüncüsü filmin DORUĞU +
> KAPAK KARESİ. Rapor doruğu "One last redundant brush. Unnecessary."
> diye tarif etti ve `PEAK LOCATED AT: no peak located` yazdı.
> Çözüm rubriğe değil AGENTS ortak adım ①'e ve SPEC künyesine yazıldı.
>
> 🔎 **DERS 130 (26.08.2026 · THE ROSE COAT):** ⑩ önerme kapısı bulguyu
> düşürüyor, puanı geri vermiyor. ② 7,2 ve ⑤ 6,0 — iki kapıdan sonra
> ayakta kalan kapalı hücre sayısı ikisinde de **0.**
>
> 🔎 **DERS 131 (26.08.2026 · THE ROSE COAT):** ② DEVAMLILIK'ın 12 puanlı
> hücresinden 6'sı "no in-scope source · 10/10". Kaynaklı hücrelerin
> ortalaması 4,3; raporun yazdığı 7,2. Δ = 2,9 puan, sıfır yeni gözlem.
> Aynı partide ⑤ kuralı TERS yönde ihlal etti (7/10 + "no in-scope source").
>
> 🔎 **DERS 132 (26.08.2026 · THE ROSE COAT):** aynı partide A/B kanıtı —
> tally kuralını taşıyan ⑤ tutturdu (0/3/2 = defteri), taşımayan ① sekiz
> 🔴'ü yedi yazdı.
>
> 🔎 **DERS 133 (26.08.2026 · THE ROSE COAT):** ⑤'in altı hücresinin dördü
> tek bir tasarım kararından geldi: pada mesafe 600→0 m monotonik. SPEC
> dağıtım tablosu ⑤ ve ⑥'yı hiç tanımıyordu (24.08'de açıldılar).
>
> 🔎 **DERS 134 (26.08.2026 · THE ROSE COAT):** ② "bot rengi" bulgusunu
> #1 sıraya koydu ama "kostüm sürüklenmesi" diye tarif etti — oysa iki
> figürü ayıran ÜÇ kanaldan biriydi. Aynı rapor filmin ANA SAYACINA
> `Counter Logic: N/A — no counter present` dedi.
>
> 🔎 **DERS 135 (26.08.2026 · THE ROSE COAT):** kurgu kapısı ④c koşulamadı —
> plan `-222222222222`, rubrik yalnız `-111111111111` üretebiliyor.
> Ayrıca ⑤'in şeridi öteki üçüyle VE kendi envanteriyle çelişti; hiçbir
> kapı dört şeridi yan yana koymuyor.
>
> 🔎 **DERS 136 (26.08.2026 · THE ROSE COAT):** ③ `AUDIO ABSENT` döndürdü;
> plan 13 sahnenin 11'inde müzik yazıyor. Şüpheyi partide yalnız ③ dile
> getirdi ve ③'ün stop bloğu hiçbir tabloya satır bırakmıyor.

> Çalıştırma kaydı — ① KARE: son 26.08.2026 · sonuç 5,0 Ⓥ ⛔ ÖN KOŞU
> Çalıştırma kaydı — ② DEVAMLILIK: son 26.08.2026 · sonuç 7,2 ⚠️ ŞARTLI
> Çalıştırma kaydı — ③ SES: son 26.08.2026 · sonuç STATE C, satır yok
> Çalıştırma kaydı — ④ HİKAYE: son 26.08.2026 · sonuç 2,3 Ⓥ ⛔ ÖN KOŞU
> Çalıştırma kaydı — ⑤ ARKA PLAN: son 26.08.2026 · sonuç 6,0 ⚠️ ŞARTLI

---

### 🧭 DERS → RUBRİK İZ DEFTERİ — 129-136 eki

```
D129 → hiçbir rubrik · GEREKMEZ — hata rubriğin kuralında değil,
       operatörün koşu ÖNCESİ adımında. Yama: AGENTS ortak adım ①
       (kapı koşudan öncesine alındı) + 7 SPEC dosyasının künyesi.
       Kardeş tarama yapıldı: altı rubriğin altısı da SPEC'in verilip
       verilmediğini bilemez — bilebilecek tek yer operatördür.

D130 → hiçbir rubrik · GEREKMEZ — ⑩ rapor SONRASI koşan bir operatör
       kapısıdır. Yama: AGENTS ortak adım ⑩ · üçüncü ve dördüncü satır.
       ⚠️ Rubrik tarafındaki eşdeğeri D131'dir ve o yamandı.

D131 → 2_DEVAMLILIK · skor bloğu ④ (KAYNAK RUBRİK — 7,2 oradan çıktı)
D131 → 1_KARE · 3_SES · 4_HIKAYE · 5_ARKA_PLAN · 6_FIZIK · skor bloğu ④
       (kardeş tarama: altısında da aynı cümle vardı, altısı da aynı
        hatayı üretirdi)
D131 → altı rubriğin KAPSAM bloğu · "stays at FULL score" cümlesi de
       değişti — yamalanmasaydı rubrik kendi ④. maddesiyle çelişecekti

D132 → 1_KARE · skor bloğu ⑤ (KAYNAK RUBRİK — 8 🔴'ü 7 yazan koşu)
D132 → 2_DEVAMLILIK · 3_SES · skor bloğu ⑤
D132 → 4_HIKAYE · GEREKMEZ — bu mercek severity etiketi HİÇ kullanmıyor
       (rubrikte 0 adet 🔴/🟠/🟡, SEVERITY TALLY bölümü yok). Kural bir kez
       yazıldı, taramada sayıldı ve GERİ ALINDI: sayılacak şeyi olmayan
       rubriğe sayım kuralı yazmak, uyulmayacak bir kural yazmaktır.
D132 → 5_ARKA_PLAN · 6_FIZIK · GEREKMEZ — kural zaten gövdelerinde vardı
       ve bu partide ⑤ tam da o yüzden tutturdu (A/B kanıtı)

D133 → 5_ARKA_PLAN · kategori 5 (Depth, Parallax & Scale) — KAYNAK RUBRİK
D133 → 2_DEVAMLILIK · kategori 8 (Spatial Geography) — aynı yanlış okuma
       oradan da geldi (Coğrafya 7/10, aynı iki timecode)
D133 → 6_FIZIK · GEREKMEZ — kategori 6 zaten "measure against same-frame
       anchors, not memory" diyor; aletin kendi koruması var
D133 → 1_KARE · GEREKMEZ — tek sahneye bakar, iki sahne arası ölçek
       karşılaştırması yapmaz
D133 → 3_SES · 4_HIKAYE · GEREKMEZ — ölçek ölçmezler
D133 → SPEC dağıtım tablosu · dört SPEC dosyasına ⑤ ve ⑥ satırı

D134 → hiçbir rubrik · GEREKMEZ — belgesiz merceğin körlüğü TASARIMDIR;
       sıralamayı düzeltecek bilgi rubriğe verilirse tasarım bozulur.
       Yama: AGENTS ortak adım ⑩ · beşinci satır (operatör yeniden sıralar).

D135 → hiçbir rubrik · GEREKMEZ — rubriklerin çıktı biçimi DOĞRU; yanlış
       olan planın kapıya o biçimde yazmaması. Yama: SPEC + plan (iki
       şerit) + AGENTS ortak adım ⑤ (üçüncü satır: şerit karşılaştırması).

D136 → AGENTS ortak adım ⑪ · beşinci komut (ses kanalı varlığı)
D136 → 1_KARE · 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 6_FIZIK · künye satırı
       `LINES HEARD` — "none" iki gerçeği ayırmak zorunda
D136 → 5_ARKA_PLAN · GEREKMEZ — künyesinde `LINES HEARD` satırı yok
       (yerine SUBJECTS EXCLUDED var); ses ölçmez
```

---

### 🧭 RUBRİK YAMASI — 26.08.2026 · TEMA VE AÇI KAPILARI (ders numarası YOK)

⚠️ **Bu yama bir DERSTEN gelmiyor.** Kaynağı, 22.08'de yazılıp hiçbir kapıya
bağlanmamış üç kılavuzdur (TEMA_MUHENDISLIGI · KAMERA_ACISI_PSIKOLOJISI ·
ACI_YAYI_VE_SEKANS). AGENTS §8 gereği ders YAZILMADI: bu bir kural ekleme
değil, kapı kurma işidir. Tekrarlarsa ders yazılır (kart Y sırası:
veri → belge revizyonu → ders).

```
TEMA/AÇI → 2_DEVAMLILIK · STEP 1a sahne envanterine "Camera setup" sütunu
       + OUTPUT FORMAT'a "SETUP INVENTORY" ölçüm satırı (KAYNAK RUBRİK).
       ⛔ Envanter SKOR DEĞİL ÖLÇÜMDÜR: hiçbir kategoriyi düşürmez.
       Aynı blokta lockoff koruması da yazılı — sabit kamera bulgu değildir,
       film boyu TEK kurulum bulgudur.

TEMA/AÇI → 1_KARE · GEREKMEZ — kendi kapsam testi ("bulguyu TEK sahneye
       bakarak söyleyebiliyor musun") film-boyu kurulum tekrarını yapısal
       olarak dışlıyor. Yazılsaydı rubrik kendi kuralıyla çelişirdi.

TEMA/AÇI → 4_HIKAYE · GEREKMEZ — "DECLARED ABSENCE IS NOT A DEFICIT"
       bloğu kamera HAREKETİ yokluğunu doğru koruyor, dokunulmadı.
       Tema tarafı zaten kategori 5'te ölçülüyor ve niyetlenen temayı
       SPEC'ten okuyor; eksik olan rubrik değil ŞABLONDU — THEME alanı
       26.08'de QA_SPEC şablonuna zorunlu olarak eklendi (D117 eki).

TEMA/AÇI → 3_SES · 5_ARKA_PLAN · 6_FIZIK · GEREKMEZ — kamera kurulumu da
       tema da hiçbirinin kapsamında değil.

TEMA/AÇI → PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md · yeni kategori 6
       "AÇI VURUŞLA EŞLEŞİYOR MU" — betiğin ölçtüğü SAYININ anlam yarısı.
       Betik kaç açı tipi olduğunu sayar; doğru açı olup olmadığını
       KAMERA_ACISI §3 vuruş tablosuna karşı bu kategori sorar.
```

> **Betik tarafı ayrı kayıt:** `PROMPT_KONTROL/prompt_kontrol.py` dört yeni
> denetim aldı (kurulum çeşitliliği · açı sözlüğü · abartı eşiği · tema
> satırı). 107 eski dosyaya koşuldu, dört yanlış-pozitif sınıfı bulunup
> kapatıldı. Ayrıntı betiğin kendi başlık bloğunda.

---

## ⭐ 28.08.2026 — THE THIN ROOF · ALTI MERCEK · SPEC HAZIRDI, ALTISI DA MOD V

```
MALZEME   dikey shorts teslim kurgusu · 65,030 s · 720×1280 · 30 fps · AAC ses
MERCEK    ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK
MOD       altısı da V   ⛔ SPEC dosyası VARDI ve verilmedi → mod V sayısı 7. filme çıktı
KAYIT     ../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_THIN_ROOF.md
HAM       ../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_THIN_ROOF_*_HAM.md
TABLO     ⛔ HİÇBİR T TABLOSUNA SATIR YAZILMADI [D129]
```

**Bu koşunun bulgusu skor değil, ÖLÇÜ:**

```
18 severity etiketli bulgu  →   4'ü gerçek (kareden doğrulandı)
                                6'sı ⑩ önerme kapısında ya da ölçümde düştü
                                5'i ⬜ AÇIK
filmin ölçülmüş 6 gerçek ihlali  →  6'sı da raporlarda YOK
```

Görülmeyen altı ihlalin dördü TEK KAREDEN okunur ve ikisi rubriklerin kendi
OTOMATİK BLOCKER kutusudur: halkanın içine yazılmış "11 metres" (S2, 2 s) ·
sırt ünitesi (S2, 10 s) · klon (S3, 0,30 s) · havada çakıl (S4) · üretilmemiş
twist (S5) · ölmüş döngü + 4,997 s başlık kartı.

⛔ ① KARE rubriği başlık kartını, kendi metninin AÇIKÇA YASAKLADIĞI biçimde
`FLAGS`'e SORU olarak yazdı ("is this burned-in text intentional?") ve negatif
kutusunu işaretlemedi.

### 🧭 DERS → RUBRİK İZ DEFTERİ — 137-142 eki

```
D137 → 1_KARE · 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 6_FIZIK · künye
       `LINES HEARD` satırı: "no audio information at all" ifadesi
       KALDIRILDI, yerine "nothing audible to me" + rubriğin dosya
       hakkında hüküm veremeyeceği ⛔ satırı.
D137 → 3_SES · STATE C bloğu: stop bloğu artık ÖNKOŞULLU — operatörün
       yapıştırdığı ses akışı probu boş değilse STATE C ilan edilemez.
D137 → 5_ARKA_PLAN · GEREKMEZ — künyesinde `LINES HEARD` satırı yok,
       ses ekseni kapsamında değil.

D138 → 1_KARE · negatif kutu listesine "sahnenin kendi malzemesine gömülü
       karakterler" maddesi (kadrajın ORTASI ve öznenin YÜZEYİ).
D138 → 5_ARKA_PLAN · kategori 9'a aynı madde (emergent text yalnız
       bindirme ve kenar artefaktı değildir).
D138 → 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 6_FIZIK · GEREKMEZ — ekranda
       metin hiçbirinin kapsamında değil (② ④ zaten →🔧 işaretçisiyle
       ①'e yolluyor).
D138 → PROMPT_KONTROL/prompt_kontrol.py · İKİ yeni denetim:
       dosya seviyesi "metin yasağı KAPSAMSIZ" (FIX, dosya başına tek
       satır) + prompt seviyesi "yüzey işaretine bitişik ölçü" (FIX,
       yalnız image). 24 dosyalık taramada ikincisi 4 dosya tetikledi.

D139 → HİÇBİR RUBRİK · GEREKMEZ — bu bir YAZIM dersidir (prompt gövdesi),
       ölçüm dersi değil. ② DEVAMLILIK bulguyu zaten gördü; yanlış olan
       teşhisiydi ve onu düzelten şey rubrik değil SPEC'in mod D'de
       verilmesidir [D129].
D139 → KILAVUZ_REHBERI §5 · D79 bloğunun altına kapsam notu.

D140 → 1_KARE · DUPLICATE CHARACTER kontrolünün üstüne "CLIP-HEAD
       DUPLICATE": her klibin İLK YARIM SANİYESİ kare kare taranır,
       bulgu SANİYE değil KARE ARALIĞI olarak yazılır.
D140 → 2_DEVAMLILIK · kategori 12'ye aynı madde.
D140 → 5_ARKA_PLAN · GEREKMEZ — klon ÖZNENİN üstünde doğdu, özne-dışı
       alanda değil; rubriğin kapsam testi bunu dışarıda bırakıyor
       ve doğru bırakıyor.
D140 → 3_SES · 4_HIKAYE · 6_FIZIK · GEREKMEZ.

D141 → HİÇBİR RUBRİK · GEREKMEZ — kurgu kapısı bir OPERATÖR kapısıdır,
       rubrik değil. Yama AGENTS ortak adım ④'e (dördüncü satır) ve
       QA_SPEC şablonunun B bloğuna (FİNAL VURUŞ KANITI) yazıldı.
       ⚠️ ④ HİKAYE zaten "ENDS OR STOPS" soruyor ve bu filmde DOĞRU
       cevabı verdi; eksik olan rubrik değil, cevabın PLANLA
       karşılaştırılmasıydı.

D142 → HİÇBİR RUBRİK · GEREKMEZ — SPEC yazım dersi. Yama AGENTS Kart A'ya
       (E bloğu kapıları kuru koşuyla doğrulanır + İKAME satırı).

D143 → HİÇBİR RUBRİK · GEREKMEZ — prompt/plan dersi (toz yoğunluk sayısı).
       Yama: REHBER §3.2 "İlgili ders" + §7 tuzak; ⑥ FİZİK zaten "dust
       waterfall" ölçtü, hüküm ("accept it") planla düzeltilir, rubrikle değil.
D144 → HİÇBİR RUBRİK · GEREKMEZ — üretim kapısı (operatör) dersi. Yama:
       09_SISTEM + Skylight PLAN üretim notları (KABUL/RET/YABANCI GÖZ/SONUÇ).
D145 → HİÇBİR RUBRİK · GEREKMEZ — prompt dersi. ⑤ ARKA PLAN kanyonu DOĞRU
       yakaladı; ders rubrikteki "en büyük nesne" kuralını PROMPTA taşır.
       Yama: 04_ISIK + REHBER §3.2 + §7 tuzak.
D146 → HİÇBİR RUBRİK · GEREKMEZ — bible dersi (kask geometrisi). ② DEVAMLILIK
       üç kaskı doğru yakaladı. Yama: 02_KARAKTER + REHBER §7 tuzak.
D147 → HİÇBİR RUBRİK · GEREKMEZ — bible dersi (kir merdiveni). ② doğru yakaladı.
       Yama: 02_KARAKTER + REHBER §3.2.
D148 → HİÇBİR RUBRİK · GEREKMEZ — prompt dersi (kalkış geometrisi). ① KARE
       doğru yakaladı. Yama: 03_FIZIK + REHBER §3.5 + §7 tuzak.
D149 → HİÇBİR RUBRİK · GEREKMEZ — tasarım dersi (0g kemerli beden). ①⑥ rijit
       bedeni yakaladı; bulgu ⑩'da tasarım çıktı ama tasarımın kendisi eksikti.
       Yama: 03_FIZIK + REHBER §3.5.
D150 → 5_ARKA_PLAN · STEP 1 EDGES satırı + kategori 9 filigran kutusu
       ("static mark in the same corner in every scene IS a watermark").
D150 → 1_KARE · kategori 10 negatif liste, watermark kutusu (aynı kural).
D150 → 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 6_FIZIK · GEREKMEZ — filigran kadraj
       kenarı bulgusudur (① ve ⑤'in kapsamı); ölçümü zaten makineye taşındı:
       AGENTS ⑪ köşe testi + olcum_kapisi.sh + KURGU_RITMI §6 ihraç listesi.
⚠️ 3_SES · YAMA ÖNERİSİ (ders değil): rapor "SCORED CATEGORIES: N/A" yazıp yine
       de VERDICT bastı ("AUDIBLE DRIFT, FIXABLE IN THE MIX"). Hiçbir kategori
       sayı taşımıyorsa VERDICT satırı "NO VERDICT — nothing measured" olmalı;
       bir sonraki 3_SES düzenlemesinde eklenir.
```

### 🔧 RUBRİK KOŞU SAYILARI — 28.08.2026 sonrası

```
1_KARE          son koşu 28.08 · THE THIN ROOF · mod V · ön koşu
2_DEVAMLILIK    son koşu 28.08 · THE THIN ROOF · mod V · ön koşu
3_SES           son koşu 28.08 · THE THIN ROOF · STATE C stop bloğu ·
                ⛔ ÖLÇÜM ÇÜRÜTTÜ (dosyada AAC 253 kbit/s ses var) → D137
4_HIKAYE        son koşu 28.08 · THE THIN ROOF · mod V · ön koşu
5_ARKA_PLAN     son koşu 28.08 · THE THIN ROOF · mod V · ön koşu
6_FIZIK         son koşu 28.08 · THE THIN ROOF · mod V · 24 fps varsaydı (gerçek 30)
```

### 🔧 RUBRİK KOŞU SAYILARI — 29.08.2026 sonrası (THE SKYLIGHT partisi)

```
1_KARE          son koşu 29.08 · THE SKYLIGHT · mod V · ön koşu [D129] · şerit 🚨
                (insansız yuva yok, kendi 4:24 bulgusuyla çelişir) · filigran kutusu boş → D150
2_DEVAMLILIK    son koşu 29.08 · THE SKYLIGHT · mod V · ön koşu · şerit 30/31 (1 kısa) ·
                üç kask + kir sıfırlanması DOĞRU yakalandı (D146/D147 kaynağı)
3_SES           son koşu 29.08 · THE SKYLIGHT · STATE B "nothing audible" · ölçüm satırı
                yapıştırılmadı → ses ekseni ÖLÇÜLMEDİ [D137 · 3. vaka]; master −17,0 LUFS
4_HIKAYE        son koşu 29.08 · THE SKYLIGHT · mod V · ön koşu · şerit 31/31 ✅ · "no peak
                located" — doruk 3:03→3:07 ekranda (kareyle) · kesme listesi UYGULANMADI
5_ARKA_PLAN     son koşu 29.08 · THE SKYLIGHT · mod V · ön koşu · ④'ün künye satırlarını
                taşıyor (oturum 🚨 D110) · "EDGES: Clean" ×31, filigran 315/315 s → D150
6_FIZIK         son koşu 29.08 · THE SKYLIGHT · mod V · 24 fps varsaydı (gerçek 30) ·
                g ≈ 3,8 m/s² planın 0,38 g'sini DOĞRULADI · "dust waterfall: accept it" → D143
⑪ ÖLÇÜM         29.08 · ilk TAM koşu (süre · fps · ses · LUFS · tepe · sessizlik · ızgara
                ikamesi · köşe şeridi · 18 kare) — kesme dedektörü karanlık filmde kör (1/33)
```

---

## ⭐ 31.08.2026 — THE FROST LINE · ALTI MERCEK (+⑥ İKİNCİ KOŞU) · SPEC HAZIRDI, ALTISI DA MOD V — 9. FİLM

```
MALZEME   yatay 3-5 dk teslim kurgusu · 235,201 s · 1280×720 · 30 fps · AAC ses
MERCEK    ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK ×2 koşu
MOD       altısı da V  ⛔ SPEC dosyası VARDI ("bu film 9. olmasın" uyarısıyla) ve
          verilmedi → SPEC'li mod V sayısı 9. filme çıktı
KAYIT     ../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_FROST_LINE.md
HAM       ../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_FROST_LINE_*_HAM.md (7 dosya — ⑥ iki koşu)
TABLO     ⛔ HİÇBİR T TABLOSUNA SATIR YAZILMADI [D129]
```

**Bu koşunun bulgusu skor değil, ÖLÇÜ VE KARE:** 2 eksik sahne (S12 · S23) +
kırpılmamış hook · ses kanalı VAR, −21,5 LUFS — 6/6 mercek "nothing audible"
[D137 · 4. vaka], ③'ün 4 🔴'ı ölçümle çürüdü · üç novum vuruşu (S5 yama uçuşu ·
S15/S19 klip içi beyazlama) EKRANDAYDI, mercekler görmedi/tersine okudu → D151 ·
S20 doruk vuruşu ekranda yok · filigran "▷" 235/235 [D150 2. vaka — ① ve ⑤
Thin Roof yamaları sayesinde bu kez GÖRDÜ ✅].

### 🧭 DERS → RUBRİK İZ DEFTERİ — 151-154 eki

```
D151 → HİÇBİR RUBRİK · GEREKMEZ — ① KARE'nin SUB-MILLIMETRE EVENT kuralı ZATEN
       VAR ve model yine kaçırdı: hata örnekleme doğasında, ilaç operatör
       karesidir. Yama: 08_QA + AGENTS ⑪ (a/b kare çifti) + QA_SPEC şablonu
       E bloğu pratiği (E7/E8 çiftleri her kapı sahnesine).
D152 → HİÇBİR RUBRİK · GEREKMEZ — yazım/üretim dersi; ② alet kaybını zaten
       görüyor (brush/tape satırları), yanılan üretimdi. Yama: 05_EKIPMAN +
       üretim kapıları [D144].
D153 → HİÇBİR RUBRİK · GEREKMEZ — üretim dersi; ⑤ mimari kaymayı DOĞRU yakaladı
       (rubrik çalıştı). Yama: 05_EKIPMAN.
D154 → HİÇBİR RUBRİK · GEREKMEZ — ⑥ iki yerçekimini ve adım/kristal ayrımını
       DOĞRU ölçtü; kaynak üretim. Yama: 03_FIZIK.
⚠️ 3_SES · Thin Roof kaydındaki bekleyen YAMA ÖNERİSİ bu koşuda TEKRARLADI
       (kategoriler N/A'yken verdikt basıldı; üstüne ölçülemez "mutlak
       sessizlik"ten 4 🔴 skorlandı) → kural gövdeye İŞLENDİ: bütün kategoriler
       N/A/UNVERIFIABLE ise VERDICT satırı "NO VERDICT — NOTHING MEASURED".
```

### 🔧 RUBRİK KOŞU SAYILARI — 31.08.2026 sonrası (THE FROST LINE partisi)

```
1_KARE          son koşu 31.08 · THE FROST LINE · mod V · ön koşu [D129] · filigranı
                TOP-3'e yazdı (D150 yaması İŞLEDİ ✅) · S4'ü "yama basıyor" okudu
                (avuç sahnesiydi) · S15 beyazlamayı görmedi → D151
2_DEVAMLILIK    son koşu 31.08 · THE FROST LINE · mod V · ön koşu · sırt ünitesi +
                kırağı dalgasını DOĞRU yakaladı (D139/D147 2. vakaların kaynağı) ·
                "dış çökük ↔ iç sağlam" 🔴'ının kökü tek klip (S6 erken çöküş)
3_SES           son koşu 31.08 · THE FROST LINE · "absolute digital silence" + 4 🔴 ·
                ⛔ ÖLÇÜM ÇÜRÜTTÜ (AAC 253 kbit/s · −21,5 LUFS · tek sessizlik = kart)
                [D137 · 4. vaka] → NO VERDICT kuralı gövdeye işlendi
4_HIKAYE        son koşu 31.08 · THE FROST LINE · mod V · ön koşu · S19'u TERSİNE
                okudu ("healthy leaf payoff" — kare: yeşil→beyaz) → D151 · kesme
                listesi UYGULANMADI (S6'yı ve üretimde vuruşu eksik S20'yi kesiyordu)
5_ARKA_PLAN     son koşu 31.08 · THE FROST LINE · mod V · ön koşu · filigranı her
                EDGES satırına yazdı (D150 yaması İŞLEDİ ✅) · üs kaymasını DOĞRU
                yakaladı (D153 kaynağı) · "plume = hata" okuması düştü (t56 yama uçuşu)
6_FIZIK         son koşu 31.08 · THE FROST LINE · mod V · İKİ KEZ koşuldu [D110 ⚠️] ·
                24 fps varsaydı (gerçek 30) · iki yerçekimini DOĞRU ölçtü (kristal
                11,1 ↔ adım 4,0 m/s² — adım planın 0,38 g'sini doğruladı) → D154 ·
                2. koşuda Ölçek/Işık kaynaksız düşürüldü (kendi kural ④ ihlali)
⑪ ÖLÇÜM         31.08 · ikinci TAM koşu (süre · fps · ses · LUFS · tepe · sessizlik ·
                kesme ızgarası · köşe şeridi · 33 kare + a/b çiftleri) — a/b çiftleri
                üç "rapor tersine okudu" vakasını yakaladı [D151'in doğuşu]
```

---

## ⭐ 01.09.2026 — THE FROST LINE · **İKİNCİ PARTİ** · ALTI MERCEK · SPEC YİNE VERİLMEDİ

```
MALZEME   aynı kurgu · 235,201 s · 23 klip + 5,1 s kart · 30 fps · AAC ses
          ⭐ bu kez 4K ihraç da var (3840×2160) — 1. partinin 720p kusuru düzeldi
MERCEK    ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK
MOD       altısı da V  ⛔ SPEC dosyası VARDI ve İKİNCİ KEZ verilmedi
          (film sayısı 9'da kalır — aynı film; ama bu filmde mod V PARTİ sayısı 2)
KAYIT     ../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_FROST_LINE.md · "2. PARTİ" bölümü
HAM       ../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_FROST_LINE_{KARE_2,DEVAMLILIK_2,
          SES_2,HIKAYE_2,ARKA_PLAN_2,FIZIK_3}_HAM.md
TABLO     ⛔ HİÇBİR T TABLOSUNA SATIR YAZILMADI [D129 · aynı filmde 2. kez]
```

**Üç sonuç:**
① **Master yolu verilmedi ve ölçüm bir kimlik arızası buldu:** `~/Downloads`
içinde "the frost lıne" adlı BEŞ dosya var; ikisi (245,120 s · 720p + 4K)
başka bir filmin gövdesini taşıyor ve üstüne BU filmin kapak kartı eklenmiş.
Ad farkı bir boşluk. → **D160**
② **③ SES bu kez ses kanalını DUYDU** (AUDIO STATE B · 8,0 "SOUNDTRACK HOLDS").
1. partinin "mutlak dijital sessizlik + 4 🔴"ı ölçümle çürümüştü [D137 · 4. vaka];
eksen düzeldi. ⛔ Ama ⑪ ölçüm satırı künyeye YİNE yapıştırılmadı → ses ekseni
bu koşuda da ÖLÇÜLMEMİŞ sayılır.
③ **Dört mercek aynı YANLIŞ bulguyu birebir aynı cümleyle yazdı**
(`3:23 fingers phase through the glass visor`). 4K master'dan t202/t203/t204:
el vizörün ÖNÜNDE, cam çerçevesi ve pane kenarı okunur — füzyon YOK. Yanlış 🔴,
①'in REGENERATE hükmünü taşıyan dört 🔴'dan biriydi. → **D159**

**Kareyle KAPANAN iki yeni ihlal:** plan S5'te de sırt harness'ı (t52/t57 —
D139 · 3. vaka, yeni yuva) · plan S22'de tohum EKİLMEDEN önce yatakta çimlenmiş
filiz sırası (t217/t219 — SPEC "filiz 0 kare", D156 · 2. vaka).
**Belgeyle açılan bir ihlal:** iç sahnelerde PEMBE LED yetiştirme şeridi
(a_t104 · ⑤ envanterinde S11/S17) — SPEC "yapay lamba/LED 0 kare"; ⑤ envantere
yazdı ama belgesiz olduğu için bulgu yapamadı.

### 🧭 DERS → RUBRİK İZ DEFTERİ — 159-160 eki

```
D159 → 1_KARE (KAYNAK RUBRİK — yanlış bulgunun doğduğu yer) · 2_DEVAMLILIK ·
       3_SES · 4_HIKAYE · 5_ARKA_PLAN · 6_FIZIK · ALTISI DA YAMANDI:
       kapsam bloğunun hemen ardına "AN OUT-OF-SCOPE FLAG IS SOMETHING YOU
       SAW, NEVER SOMETHING YOU WERE TOLD" bloğu. Kardeş taraması ölçütü
       ("bu rubrik aynı malzemeyi görse aynı hatayı yapar mıydı?") altısında
       da EVET: altısının da OUT-OF-SCOPE mekanizması var ve hiçbiri
       "gözlemlediğin" demiyordu.
D159 → AGENTS ⑤ ÇAPRAZ SAYIM KAPISI · DÖRDÜNCÜ SATIR: METİN ÇAKIŞMASI
       (aynı saniye+nesne+fiil → sahibi dışındakilerden SİL; işaretçi ≥2 →
       oturum 🚨 KOPYA, kareyle doğrulanmadan tabloya girmez)
D160 → HİÇBİR RUBRİK · GEREKMEZ — dosya kimliği bir KONTEYNER özelliğidir;
       hiçbir mercek hangi dosyayı izlediğini gözlemleyemez. D137'nin ses
       kanalı için söylediğinin aynısı burada dosya adı için geçerli.
       Yama: AGENTS ⑪ → ⑪.0 KİMLİK KARESİ (kurgunun ORTASINDAN) + aynı addan
       hepsini ölç + künyeye master yolu · qa-isle SKILL.md adım 1.
```

### 🔧 RUBRİK KOŞU SAYILARI — 01.09.2026 sonrası (2. FROST LINE partisi)

```
1_KARE          son koşu 01.09 · THE FROST LINE (2) · mod V · ön koşu [D129] ·
                kesme sayısı 21 (ölçüm 22) → şerit ekseni 🚨 · `Camera 10/10` +
                "no in-scope source" (kendi ④ kuralı ihlali; düzeltilmiş 5,7) ·
                3:23 vizör füzyonu 🔴 KAREYLE ÇÜRÜDÜ → D159'un kaynağı ·
                filigranı yine GÖRDÜ ✅ · 1:30 doku kaynamasını DOĞRU yakaladı
2_DEVAMLILIK    son koşu 01.09 · THE FROST LINE (2) · mod V · ön koşu ·
                ⭐ partinin en verimli merceği: sırt harness'ı (yeni yuva) ve
                S22 filizi KAREYLE DOĞRULANDI · gölge 180° kilit ihlali ·
                ⛔ `Counter Logic: N/A` — SPEC'te ÜÇ sayaç var → ölçüm boşluğu [D134]
3_SES           son koşu 01.09 · THE FROST LINE (2) · **AUDIO STATE B — sesi DUYDU** ✅
                (1. partinin arızası düzeldi) · ama duyduğu "high-altitude wind"
                SPEC'in "rüzgâr 0" kilidine aykırı ve ledger'ı üç müziksiz
                pencerenin üçünü de göremiyor · ⑪ satırı künyede YOK [D137]
4_HIKAYE        son koşu 01.09 · THE FROST LINE (2) · mod V · ön koşu · kesme
                listesindeki 7 adayın 7'si yük taşıyor (biri ORTA NOKTA, biri
                "MAY NOT BE CUT" viral, biri karakterin tek tereddüdü) →
                UYGULANMADI [D129] · ⭐ tek cümlelik izleyici okumasında SEÇİM
                ve BEDEL yok — sebebi yazım değil, S20/S12/S23'ün teslim edilmemesi
5_ARKA_PLAN     son koşu 01.09 · THE FROST LINE (2) · mod V · özne kapısı ✅ ·
                `Focus 10/10` + "no in-scope source" (kendi ④ kuralı ihlali;
                düzeltilmiş 6,0) · filigran sorusunu FLAGS'e yazdı (otomatik-
                BLOCKER kutusu soruya çevrilemez) · PEMBE LED'i envantere yazdı,
                bulgu yapamadı (belgesiz mercek — mod D görürdü)
6_FIZIK         son koşu 01.09 · THE FROST LINE (2) · mod V (mod kapısı düştü:
                plan sayısal kilit taşıyor) · **24 fps varsaydı, ölçüm 30 der —
                üç koşunun üçünde de aynı hata** · `Impact: —` kuralını
                ALTIDAN TEK DOĞRU UYGULAYAN mercek ✅ · L1/L6 g ölçümleri planın
                0,38 g'sine oturdu → partinin tek gerçek sayısal PASS'i
⑪ ÖLÇÜM         01.09 · üçüncü TAM koşu · ⭐ ilk kez KİMLİK adımıyla: master yolu
                verilmedi, aynı ada uyan 5 dosya ölçüldü, 2'si başka film çıktı
                [D160] · 4K ihraç doğrulandı (720p kusuru düzeldi) · filigran ve
                kart 4K'da da duruyor · −21,2 LUFS / tepe −0,1 (kilit dışı)
```

---

## 📅 02.09.2026 · THE STILL SWARM — DEPONUN İLK SEKİZ MERCEKLİ PARTİSİ

⛔ Sekizi de **mod V** · SPEC dosyası VARDI · master ÖLÇÜLMEDİ →
`rapor_kontrol.py` çıkış **2** · ⛔ 5 TEKRAR · ⚠️ 2 ŞARTLI · ✅ 1 GO.
Hiçbir satır T tablosuna girmedi. Film kaydı:
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_STILL_SWARM.md`

```
1_KARE          son koşu 02.09 · mod V · ⛔ TEKRAR · 3,9 · tally 6/4/3 yazdı,
                etiketler 5/5/2 · BAŞLIK KARTINI gördü ✅ ama FLAGS'e SORU
                olarak yazdı — kendi rubriği ekran metnini otomatik BLOCKER
                sayar ve FLAGS'i YASAKLAR (⑤'in 3. vakası) · 0:59'daki SAHNE
                SINIRINI "gizli kesme 🔴" saydı (compilation kuralını okumadı)
2_DEVAMLILIK    son koşu 02.09 · mod V (tasarım) · ⚠️ ŞARTLI · 7,8 ·
                ⛔ `Counter Logic: N/A` — SPEC'te 8→0 kelepçe sayacı var →
                ölçüm boşluğu [D134 · 2. vaka, ardışık iki filmde]
                · SETUP INVENTORY "11 kurulum / 4 açı tipi" dedi, SPEC 7/6 der
3_SES           son koşu 02.09 · mod V (tasarım) · ✅ GO — **partinin tek temiz
                aritmetiği** · `LINES HEARD: none — nothing audible to me`
                doğru biçimde yazıldı [D136/D137 tuttu] · 1:59'da "absolute
                silence 🔴" — rubriğin kendi kuralı ölçülmemiş sessizliğe
                BLOCKER yasaklıyor; ⑪ koşmadığı için ⬜ AÇIK
4_HIKAYE        son koşu 02.09 · mod V · ⛔ TEKRAR · 2,7 · kesme listesindeki
                4 adayın 4'ü yük taşıyor (biri **S6 = NOVUM TAŞIYICISI + TEK
                KARE**) → UYGULANMADI [D129] · "no peak located" + "I could not
                find one" → novumu adlandıramadı [D166'nın kaynağı]
5_ARKA_PLAN     son koşu 02.09 · mod V + üç kilit · ⚠️ ŞARTLI · 4,3 ·
                ⭐ **partinin en değerli ölçümü**: COUNT LOG S8-S9'da "5 floating
                hand tools in a row" — SPEC'in sayacı da o iki sahnede 5 der
                (kimlik kapısının 3. çapası) · SCENES 13 = CUTS 13 (kendi
                kuralına göre kartsız kurguda sahne = kesme + 1)
6_FIZIK         son koşu 02.09 · mod V · ⛔ TEKRAR · 6,2 · **PREMISE REGISTER'a
                filmin TÜRÜNÜ yazdı ("zero-gravity orbital environment"),
                KURALINI değil** → tek olaydan (planda YAZILI gaz konisi) üç
                kategoride 13 puan düşürdü → **D166'nın kaynağı** ·
                24 fps varsaydı (ölçüm yok, doğrulanamadı)
7_AKSIYON       son koşu 02.09 · mod V · ⛔ TEKRAR · 7,7 (2 kaynaksız hücre
                `—` oldu) · ⭐ **BEAT STRING'de S6 yuvası `-`** = "bu sahnede
                vuruş yok"; S6 filmin NOVUM TAŞIYICISI ve TEK KARE sahnesidir
                · vuruş defterinde TEK BİR ATIŞ yok (film KÜTLE ATARAK ilerler)
8_EFOR          son koşu 02.09 · mod V · ⛔ TEKRAR · 3,6 (1 kaynaksız hücre) ·
                tally 0/8/4 yazdı, etiketler 0/5/3 · COST CURVE'de 1 düşüş,
                RESET LOG'da 0 satır (betik yakaladı) · "weightless work"
                hükmü — oysa filmde efor KÜTLE ATMAKTIR ve register onu
                hiç kaydetmedi [D166]
⑪ ÖLÇÜM         ⛔ KOŞULAMADI — master depoda yok, operatör yol vermedi.
                ffmpeg kurulu; engel araç değil DOSYA [D125 · 3. vaka]
```

### 🧭 DERS → RUBRİK İZ DEFTERİ — 165-166 eki

```
D165 → hiçbir rubriğe işlenmedi · GEREKMEZ · ders rubrik metnine değil
       KART SIRASINA dokunuyor (AGENTS Kart A + yeni-film SKILL §4);
       rubrik operatörün gördüğü tek dosyadır, orada karşılığı yok
D165 → .claude/skills/yeni-film/SKILL.md §4  · "SPEC yazılır yazılmaz paket"
D165 → AGENTS.md Kart A · YAZ bloğu son maddesi

D166 → 6_FIZIK_QA_CRITIQUE_PROMPT.md   · STEP 0 PREMISE GATE
       ("NAMING THE MEDIUM IS NOT NAMING A RULE" + boş register uyarısı)
D166 → 7_AKSIYON_QA_CRITIQUE_PROMPT.md · STEP 0 PREMISE GATE
       (+ "beat string'e `-` yazmadan önce o sahne kuralın gösterildiği
        sahne mi diye sor")
D166 → 8_EFOR_QA_CRITIQUE_PROMPT.md    · STEP 0 PREMISE GATE
       (+ "itilecek şeyin olmadığı dünyada KÜTLE ATMAK eforun kendisidir")
D166 → 1_KARE · 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 5_ARKA_PLAN · GEREKMEZ ·
       bu beş rubrikte PREMISE REGISTER / premise gate YOKTUR (5c taraması
       koşuldu: "aynı malzemeyi görse aynı hatayı yapar mıydı?" → hayır,
       çünkü kural kaydı istenmiyor)
D166 → rubrik_paketle.sh ⑥ enjeksiyonu (süzgeç SATIR değil KAYIT seçer)
D166 → rapor_kontrol.py ①.6 NOVUM KAPISI (⑥⑦⑧ · ateşleme doğrulandı:
       THE STILL SWARM 3/3, THE COLD WELD 0/6)
```

---

### 🧭 DERS → RUBRİK İZ DEFTERİ — 179-180 eki

> Kaynak koşu: THE HEALING GROUND · 04.09.2026 · yedi mercek, **yedisi de mod V**.
> ⛔ **İki dersin ikisi de RAPORDAN gelmiyor** — biri ⑪ ÖLÇÜM KAPISINDAN (ses
> profili, iki film üst üste), biri FİLMİN KENDİ PROMPT DOSYASINDAN (imaj ↔ video
> çelişkisi) + iki kareden. Bu yüzden D63'ün "önce kaynak rubriği yamala"
> maddesinin kaynağı yok: yamalanacak bir kaynak rubrik çalıştırması yok.
> 5c taraması yine de koşuldu.

```
D179 → hiçbir rubriğe işlenmedi · GEREKMEZ · ders BİTMİŞ FİLMİ değil PROMPT
       ÇİFTİNİ denetliyor; rubrik yalnız çıktıyı görür, imaj promptunu hiç
       görmez. Kapı üretimden ÖNCEDİR.
D179 → prompt_kontrol.py ⑳b DEĞİŞİM KAPISI · ⬜ YAZILACAK
       (sahne başlığında `BEDEL SAHNESİ` / `MERKEZÎ SEÇİM` varsa: video
        promptunun `0.0s` satırındaki durum nesnesi alınır, İMAJ promptunda
        `no <nesne>` / `zero <nesne>` / `<nesne> ... dark and still`
        aranır → bulunursa ⛔ BLOCK)
D179 → 03_PLAN_ONCESI_KONTROL_LISTESI.md · ⬜ YAZILACAK — B5 BEDEL maddesine
       iki satır: "bedelin taşıyıcısı kadrajın kısa kenarının ≥1/8'i mi?" +
       "imaj promptu 0,0 saniyeyi mi yazıyor, sonucu mu?"
D179 → 1_KARE · 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 5_ARKA_PLAN · 6_FIZIK ·
       7_AKSIYON · 8_EFOR · GEREKMEZ · 5c taraması koşuldu ("bu rubrik aynı
       malzemeyi görse aynı hatayı yapar mıydı?") → hayır: sekizinin de girdisi
       BİTMİŞ VİDEO'dur, çelişki iki prompt ARASINDA duruyor ve hiçbiri
       promptu görmüyor. ⭐ Ölçüm: ④ HİKAYE mod V'de bu sahneye "REWRITE —
       needs to show why they are pressing it harder. What is failing?" yazdı;
       yani mercek sonucu doğru gördü, sebebi göremezdi.

D180 → 3_SES_QA_CRITIQUE_PROMPT.md · §9 MUSIC & SILENCE ✅ YAMANDI
       ("A DECLARED SILENCE IS A DELIVERY ITEM. VERIFY IT, DO NOT ASSUME IT."
        — beyan edilen saniyeye git · seviyeyi yaz · filmin KENDİ sessiz
        dibiyle karşılaştır · geç gelen sessizlikte İKİ saniyeyi de yaz ·
        mod V'de yalnız dibi bildir)
       Gerekçe: rubrik sessizliği ŞÜPHE olarak tanıyordu ("absolute digital
       silence never appears between clips") ama BEKLENEN sessizliği hiç
       aramıyordu. Gelmemiş bir sessizlik ses çıkarmaz; başka hiçbir kutu
       onu göremez.
D180 → 1_KARE · 2_DEVAMLILIK · 4_HIKAYE · 5_ARKA_PLAN · 6_FIZIK · 7_AKSIYON ·
       8_EFOR · GEREKMEZ · 5c taraması koşuldu → ses yedisinin de kapsamı
       dışında (①'in yalnız "vakumda ses" ve lip-sync kutusu var).
       ⚠️ AMA ④ HİKAYE bu kusurun SONUCUNU gördü ve "no peak located" yazdı —
       yani doruk kaybı hikâye merceğine YANSIYOR, sebebi ③'te duruyor.
D180 → olcum_kapisi.sh · SESSİZLİK satırı ZATEN VAR (−50 dB / 0,3 s) ·
       ⬜ AÇIK: üç eşiğe çıkarılacak (−50 / −40 / −30) ve filmin sessiz DİBİ
       (saniye + dB) da basılacak — bu koşuda elle ölçüldü
D180 → rapor_kontrol.py · ⬜ YAZILACAK `--olcum-sessizlik <baş>-<son>` bayrağı
       ([[D177]]'nin `--olcum-filigran` / `--olcum-lufs` bayraklarının kardeşi)
D180 → MUZIK dosyası şablonu · ⬜ YAZILACAK — SESSİZLİK KARARI bloğuna zorunlu
       satır: `KURGUDA HARD MUTE: sn <baş> – <son>` (ızgaradan hesaplatılır)
```

---

## 🔴 06.09.2026 · YERÇEKİMİ FAZ 8 — DERS 110 İHLALİ, SEKİZ MERCEK TEK OTURUMDA

```
Makara  YERÇEKİMİ faz 8 · ~99-100 s · 10 klip
Koşulan ⑤ arka plan → ⑥ fizik → ① kare → ② devamlılık → ③ ses →
        ④ hikaye → ⑦ aksiyon → ⑧ efor  · HEPSİ AYNI SOHBETTE
Ham     ../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ08_8MERCEK_HAM.md
```

**Kontaminasyon kanıtı dosyanın kendi içinde duruyor ve tek satırda okunuyor:**

```
⑥ FİZİK (erken)  : "LINES HEARD: none — nothing audible to me"
① KARE  (sonra)  : "LINES HEARD: 3" + üç cümle + zaman kodları
②③④⑦⑧ (sonra)  : AYNI üç cümle · AYNI zaman kodları · AYNI sahne
                   haritası · AYNI presence string "-111-1-11-"
```

⛔ **Sekiz ölçüm değil, bir ölçüm ve yedi kopyadır.** "Altı mercek aynı
şeyi gördü" bir doğrulama sanıldı; oysa altısı da ikincinin cümlesini
devraldı. Ve devralınan şey en pahalı iddiaydı: filmin kask takvimini
kıran üç replik.

```
✅ DOĞRULAMA KOMUTU — modele sorulmaz:
   ffprobe -v error -select_streams a -show_entries stream=codec_name,channels -of csv=p=0 <makara>
```

**İKİNCİ İHLAL — YANLIŞ ALET:** faza özgü `FAZ_08_QA_PROMPT.md` dururken
genel sekiz mercek ÇIPLAK koşuldu [D129]. Ölçülebilir bedeli:

```
· ÜÇ YANLIŞ POZİTİF — üçü de belgede yazılı TASARIMI kusur yazdı:
  düz egzoz konisi (D36 tam da bunu ister) · "kalın eldiven" (A
  eldivensiz) · "sabit hızlı enkaz" (⑥ fizik doğru okudu, ① ve ⑧ yazdı)
· FAZIN EN KIRILGAN KİLİDİ HİÇ ÖLÇÜLMEDİ: S88'in bir saniyeden kısa
  ışık geçişi. Sekiz merceğin hiçbiri sormadı; faza özgü rubrik üç
  ayrı yerde soruyor.
· ④ HİKAYE bir FAZ makarasını FİLM sandı → 3,5/10 "REWRITE PREMISE".
  Yüz saniyelik bir faz, yirmi dakikalık bir filmin doruk rampasıdır.
```

**KURAL — kayda geçti:**

```
① FAZ makarasına o fazın KENDİ iki mühürlü rubriği koşulur (D164).
② Genel sekiz mercek TAM KURGUYA koşulur, faza değil.
③ Her mercek TEMİZ OTURUMDA [DERS 110] — istisnasız.
④ Aynı iddia birden çok raporda geçiyorsa, önce SIRAYA bakılır:
   sonraki raporlar öncekinin cümlesini devralmış olabilir.
```

---

### 🧭 DERS → RUBRİK İZ DEFTERİ — 181-183 eki

**Kaynak koşu:** THE KEPT LIGHT · 06.09.2026 · sekiz mercek (Gemini, iki küme
hâlinde tek oturum) · sekizi de mod V · parti 🚨 GEÇERSİZ.
Film kaydı: `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_KEPT_LIGHT.md`

```
D181 → olcum_kapisi.sh · == TESLİM SINIFI [D181] == bloğu ✅ YAZILDI (06.09)
       borç KAPANDI: ders 05.09'da yazıldı, kapısı 06.09'da koda indi.
       İki eksen ÖLÇÜLÜR (LUFS eşiği 3 LU · kuyrukta ≥1,5 s donma),
       iki eksen ⬜ GÖZ / ⬜ SPEC olarak açık kalır (filigran · klip sayısı).
       İlk koşusu: THE KEPT LIGHT → 🚨 HAM ZİNCİR.
D181 → AGENTS.md §3 ⑪ ÖLÇÜM KAPISI ✅ YAMANDI — betiğin satırı + "HAM ZİNCİR
       ise mercek KOŞULMAZ" hükmü.
D181 → .claude/skills/qa-isle/SKILL.md §1 ✅ YAMANDI.
D181 → hiçbir MERCEK rubriğine işlenmedi · GEREKMEZ · ders TESLİM SINIFINI
       ölçer; mercek eline geçen dosyanın kurgulanmış olup olmadığını
       gözleyemez (dosya özelliği, D137'nin aynı ailesi).

D183 → 6_FIZIK_QA_CRITIQUE_PROMPT.md · STEP 0 PREMISE GATE ✅ YAMANDI
       ("EVERY REGISTERED RULE CARRIES ITS BOUNDARY, AND YOU VERIFY THE
        BOUNDARY") — kaynak rubrik, önce burası [D63].
D183 → 7_AKSIYON_QA_CRITIQUE_PROMPT.md · STEP 0 PREMISE GATE ✅ YAMANDI
       (5c taraması: ⑦'nin register'ı aynı biçimde yalnız ortamı yazıyordu —
        aynı malzemeyi görse aynı hatayı yapardı → yamandı)
D183 → 8_EFOR_QA_CRITIQUE_PROMPT.md · STEP 0 PREMISE GATE ✅ YAMANDI
       (aynı gerekçe; ⑧ bu koşuda register'a "1G interior, vacuum exterior"
        yazdı — sınır cümlesi hiç yok)
D183 → 1_KARE · 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 5_ARKA_PLAN · GEREKMEZ ·
       bu beş rubrikte PREMISE REGISTER bölümü YOKTUR; kural kaydı yalnız
       ⑥ ⑦ ⑧'de tutulur.
D183 → rapor_kontrol.py · ①.7 NOVUM SINIR KAPISI ✅ YAZILDI (06.09) —
       SPEC'in NOVUM bloğundaki ⛔ cümlesini basar. ⚠️ Kalibrasyon notu:
       ilk sürüm `^\s*⛔` ile satır BAŞINDA aradı ve Kept Light'ın sınır
       cümlesini KAÇIRDI (cümle "tamamlanması. ⛔ İhlal DIŞINDA…" diye
       satır ORTASINDA başlıyordu) → arama satır İÇİNE alındı.
D183 → AGENTS.md §3 ⑩ ÖNERME KAPISI · ALTINCI SATIR ✅ YAMANDI.
D183 → .claude/skills/qa-isle/SKILL.md §6 ✅ YAMANDI.
D183 → SPEC ŞABLONU · ⬜ YAZILACAK — novumu olan her SPEC'in NOVUM bloğu
       kuralın SINIRINI ⛔ ile yazar; sınır cümlesi yoksa kapı ateşlemez.
       (Kept Light'ın SPEC'i bunu ZATEN doğru yazmıştı; şablon değil, kapı
        eksikti.)
```

⛔ **PAKET TAZELEME BORCU:** üç kaynak rubrik değişti → `FILME_OZEL/` altındaki
paketlerin ⑥ ⑦ ⑧ dosyaları eskidi. Yeniden koşulacak her film için
`rubrik_paketle.sh` YENİDEN ÇALIŞTIRILIR. THE KEPT LIGHT için 06.09'da
çalıştırıldı; diğer filmler için borç açık.

### 🧭 DERS → RUBRİK İZ DEFTERİ — 184 eki (06.09.2026 · DÖRT YENİ MERCEK)

Sahibin sorusu: *"QA promptları yeni filmlerdeki hataları azaltmak için
yeterli mi?"* Ölçülen cevap (Kept Light partisi): 8 gerçek kusurun 2'si
raporlarda; 26 uydurma/yanlış bulgu depo genelinde; 14 kez SPEC hazırken mod V.
Karar: sahip dört eksen seçti (kadraj · oyunculuk · ışık · hook), dördü açıldı.

```
D184 → _KAYNAK/9_KADRAJ · 10_OYUNCULUK · 11_ISIK · 12_HOOK ✅ YAZILDI
       (yeni kaynak rubrikler · 356 · 372 · 348 · 345 satır · İngilizce,
        gövdede ders numarası YOK). Kart G 5 "önce kaynak rubriği yamala"
       burada "kaynak rubrik YOKTU, açıldı" olarak işler.
D184 → 5c KARDEŞ TARAMASI: 1-8 · GEREKMEZ · ders "eksik EKSEN" dersidir,
       mevcut bir rubriğin yanlış davranışı değil. ⑥'nın S6 hatası D183'te
       yamandı; ④'ün 7-blok hatası D107/D118 kapılarında zaten sayılıyor.
D184 → rubrik_paketle.sh · kayit() (C bloğundan etiket desenine göre KAYIT)
       + PAKET_9..12 + 00_PAKET_README satırları + "HAM ZİNCİR → mercek yok" ✅
       ⑨ ← B + C(EŞ KADRAJ · EKRAN YÖNÜ) · ⑩ ← A + C(İNSAN · KASK · EKRAN YÖNÜ)
       ⑪ ← C(IŞIK TAKVİMİ · ATMOSFER · YAPI ANATOMİSİ · KASK) + GRID
       ⑫ ← A + B + <FILM>_KAPAK.md "KAPAK ANI" satırı
D184 → rapor_kontrol.py · MERCEK_IMZA(+4) · MOD_D_MERCEKLER(+4) · gozlem_dizi()
       (`OBSERVED:` satırından — dizi_al burada KULLANILMAZ, "OBSERVED"
        sözcüğü [A-Z]{3,} ile eşleşir) · ⑨⑩⑪ dizi uzunluğu = kesme+1 ·
       ⑨ SETUP STRING ↔ KURULUM İSKELETİ fark listesi (birebir eşleşme NOT:
       kare-önce şüphesi) · ⑫ DROP-OFF üç saniye + sabit sebep ✅
       Sentetik test: ⑨ raporu S24 farkını bastı, ⑫ raporu GO; ikisi de
       Kept Light'ın filigran ölçümüyle parti düzeyinde GEÇERSİZ düştü — doğru.
D184 → T9_KADRAJ · T10_OYUNCULUK · T11_ISIK · T12_HOOK ✅ AÇILDI (0 satır ·
       mod V satırı YOK — "SATIR YAZMADAN ÖNCE" bloğu 4. maddeyi böyle yazar)
D184 → AGENTS.md · kart F5-F8 · depo haritası (7-12 + T7-T12) · kart B
       (HAM ZİNCİR + ⑨-⑫ koşul) · kart Y (⑫ tahmin → §1; |Δ| ≤ 10 s) ✅
D184 → 00_README · 🎯 PLAN SADAKATİ bölümü · "hangi filme hangi mercekler" ·
       kapsam haritası 4 satır + kapak satırı · KAPSAM DIŞI'na ⑫ notu ·
       değişiklik kaydı · NUMARA ÇAKIŞMASI notu (mercek ⑪ ≠ kapı ⑪) ✅
D184 → qa-isle SKILL §0 / §6 / §7 · yeni-film SKILL PAKET_1..12 (2 yer) ✅
D184 → sayac.sh · rubrik hacmi döngüsü 1[0-2]_ ✅
D184 → 08_YAYIN_PERFORMANS_TABLOSU · ⑫ tahmin hücresi (aşağıdaki satır)
D184 → THE KEPT LIGHT paketi PAKET_1..12 ile yeniden üretildi ✅ — dört koşul
       da tutuyor (iskelet var · replik 0 · IŞIK TAKVİMİ var · yayınlanacak);
       film kaydının "SONRA" satırı güncellendi.
D184 → SPEC ŞABLONU · GEREKMEZ · dört mercek mevcut A/B/C kayıtlarını okur
       (KURULUM İSKELETİ · CENTRAL CHOICE · IŞIK TAKVİMİ · VIRAL · KAPAK ANI);
       yeni blok istemez. D183'ün ⛔ sınır cümlesi borcu AYRI durur.
```

⛔ **PAKET TAZELEME BORCU (büyüdü):** diğer filmlerin `FILME_OZEL/` klasörlerinde
PAKET_9..12 YOK ve ⑥⑦⑧ eski; yeniden koşulacak her film için
`rubrik_paketle.sh` YENİDEN çalıştırılır. Kept Light için 06.09'da yapıldı.

⚠️ **Dürüst sınır:** ⑨-⑫ hiç koşulmadı; ilk gerçek koşu Kept Light'ın
kurgulanmış master'ında olacak. Rubriklerin kendi hatası (sayım · tally ·
mod) ancak o koşuda ölçülür; bu ek onların VARLIĞINI kaydeder, işe
yaradığını değil.

---

## 📅 06.09.2026 · YERÇEKİMİ FAZ 9 / DÜŞÜŞ — ON İKİ MERCEK · FAZ RUBRİĞİ YERİNE GENEL MERCEK

```
Makara  "faz 9.mp4" · 12 segment · 120 s · 11 kesme (rapor beyanı)
Mod     on ikisi de V · SPEC yok · FAZ_09_QA_PROMPT.md yok
Ölçüm   ⑪ KOŞULMADI — sahip kararı: depo dışına çıkılmaz, master'a dokunulmaz
Ham     FILM_QA_RAPORLARI/02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ09_12MERCEK_HAM.md
Faz     yatay_10_20_dk_filmler/YERCEKIMI/FAZ_09_DUSUS/FAZ_09_QA_DERSLER.md
Parti   🚨 T tablolarına satır GİRMEZ
⭐ ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK — depoda İLK koşuları [D184]
```

⭐ **DÖRT YENİ MERCEĞİN İLK KOŞUSU — dürüst bilanço:**

```
⑩ OYUNCULUK  ✅ EN ÇOK İŞE YARAYAN. Sahne başına cümle yöntemi çalıştı ve
              S102'de kilidin yarısının eksik olduğunu KİLİDİ GÖRMEDEN
              buldu ("the body is entirely static"). KİLİT 43 "İNSAN DA
              DÜŞER" der; ⑩ semptomu yakaladı.
⑫ HOOK       ⚠️ İKİYE BÖLÜNDÜ. Kapak saniyesi (9/10) ve paylaşım anları
              (8/10) faz ölçeğinde geçerli; hook · plato · çıkış · terk
              tahmini bir ORTA SEGMENTTE anlamsız [D185].
⑨ KADRAJ     ⚠️ ÜÇ HÜCRESİ "kusursuz→7/10" yazdı [D186]; kafiye çifti
              bulgusu faz ölçeğinde geçersiz (film kafiyesi F1↔F10'dur).
              Kalan gerçek katkı: 12 kurulum / 0 dönüş sayımı.
⑪ IŞIK       🔴 FİLMİN RENK TAKVİMİNİ (KİLİT 44) 3/10 ile en düşük
              kategorisi yaptı. Ama AYNI raporda In-Clip Stability 10/10 ve
              Atmosphere Honesty 10/10 verdi — yani kilidin TUTTUĞUNU da
              ölçtü. Mod V'de ⑪ takvimi göremez; ⑪ SPEC'siz koşulmamalıydı
              (kendi rubriği bunu yazıyor).
```

```
D185 → rapor_kontrol.py · ①.8 FAZ KAPISI ✅ YAZILDI (06.09) — faz_mi()
       klasör adı / FAZ_*/ alt klasörleri / raporun FILM satırından tespit
       eder; --faz ile elle beyan edilir. ④/⑨/⑫'nin dokuz film ölçekli
       kategorisi `—` olur, kesme listesi durur.
       ⚠️ Kalibrasyon notu: kapı ilk sürümde SPEC kapısının yanına konmuştu
       ve `rows` henüz yoktu (UnboundLocalError) → skor_tablosu() çağrısının
       ARDINA taşındı.
D185 → 00_README · "hangi filme hangi mercekler" → FAZ bloğu ✅ + değişiklik
       kaydı satırı ✅
D185 → HİÇBİR MERCEK RUBRİĞİNE İŞLENMEDİ · GEREKMEZ · ders merceğin
       davranışını değil OPERATÖRÜN ALET SEÇİMİNİ düzeltir; mercek eline
       geçen makaranın filmin neresi olduğunu gözleyemez (D137 ailesi).
D186 → rapor_kontrol.py · ①.5 ✅ YAZILDI — BOS_ISSUE · TEMIZ_ISSUE ·
       KAYNAK_IZI. Koşu doğrulaması: ⑤'in beş "none" hücresi yakalandı,
       ortalama 6,5 → 4,0. Üçüncü desen ④'ün iki süpürücü kesintisini de
       yakaladı (kaynaksız).
D186 → MERCEK RUBRİKLERİNE İŞLENMEDİ · GEREKMEZ · kural ④ zaten ⑤'in ve
       ⑨'un gövdesinde YAZILI ve tutmadı — bu tam olarak D161'in tarif
       ettiği durum: yazılı kural kapı değildir, kapı çıktıda koşar.
D187 → KAPI LİSTE tarafında · faz rubriği + QA_SPEC C bloğu taşıyıcı
       kilidin yanına ÖLÇEN MERCEK yazacak. ⬜ BETİK yarısı AÇIK.
       ⛔ Mercek rubriklerine "saç kategorisi" EKLENMEDİ ve eklenmeyecek:
       kilit her filmde başkadır, kapsam haritası genel kalır.
D129 → TEKRAR 13 → 15 (THE KEPT LIGHT · YERÇEKİMİ FAZ 9)
D166 → TEKRAR 1 → 2 (⑥ fazın konusunu TWO GRAVITIES ilan etti; rubriğin
       kendi öz-denetim cümlesi ateşlemedi)
```

⛔ **ÖLÇÜM KAPISI HAKKINDA KAYIT (06.09.2026 · sahip kararı):** bu koşuda ⑪
başlatıldı ve sahip DURDURDU — *"sen videoya dokunma, repodan niye dışarı
çıkıyorsun"*. Kayda geçer: ⑪ ölçüm kapısı depo dışındaki bir dosyaya
dokunur ve **sahip istemeden koşturulmaz.** Bu koşunun bütün süre/kesme
sayıları RAPORUNKİDİR.
⭐ Ve bu partide ölçüme ihtiyaç DA olmadı: on iki raporun on ikisi de
`12 sahne · 11 kesme · 120 s · 1111111111-1` yazdı — ⑤ ÇAPRAZ SAYIM KAPISI
depoda ilk kez sıfır sapmayla kapandı [D107].

---

## 07.09.2026 · YERÇEKİMİ FAZ 10 / ZEMİN — ON İKİ MERCEK · 🚨 PARTİ GEÇERSİZ

```
Malzeme  "faz 10.mp4" · 109–111 s (rapor beyanı) · S109–S120 · FİLMİN SON FAZI
Mod      V ×12 · SPEC yok · FAZ_10_QA_PROMPT.md YOK (F9'dan sonra ikinci kez)
Ölçüm    ⑪ KOŞULMADI — sahip kararı yürürlükte
Karar    🚨 GEÇERSİZ [D188] — hiçbir satır T tablolarına girmedi
```

⭐ **BU KOŞUNUN TEK GERÇEK BULGUSUNU HİÇBİR MERCEK YAZMADI:** plan 12 sahne
yazıyor, on iki rapor 11 klip saydı. İçerik eşlemesi eksiği fazın SONUNA
koyuyor — S120 HELD FRAME, filmin son karesi, ⛔ kesilemez. On iki mercek
ayrışmayı oybirliğiyle onayladı; hiçbiri soramazdı da (mod V'de "eksik"
demek yasak, ④'ün son-sahne kapısı MODE D ONLY).
⛔ **KAPI HÜKÜM VERMİYOR:** (a) eksik teslim mi (b) toplu sayım hatası mı —
ölçüm gelmeden ayrılmaz. Aritmetik (a) lehine (12 × 10 s = 120 s ≠ 110 s)
ama karar sahibin tek ölçüm komutunda.

```
D188 → rapor_kontrol.py · ①.9 TESLİM KAPISI ✅ YAZILDI
       plan dosyalarındaki `## 🎬 SAHNE n` başlıklarının BİRLEŞİMİ ↔
       `--olcum-sahne` (varsa) ya da raporların çoğunluğu. İlk koşuşunda
       ateşledi ve partiyi düşürdü.
       ⭐ ÜÇ KONTROL KOŞUSU YAPILDI:
         · F9        plan 12 ↔ rapor 12          → temiz geçti ✅
         · KEPT LIGHT plan 25 ↔ rapor 20         → ateşledi
                      plan 25 ↔ ÖLÇÜM 25         → temiz geçti ✅
           ⛔ Bu vaka kapının iki şıkkını ayırdı: orada teslim TAMDI, beş
           mercek yanlış saymıştı. Kapı "eksik teslim dedektörü" değil,
           plan ile parti arasındaki her sayı ayrışmasının dedektörüdür;
           hangi tarafta olduğunu ÖLÇÜM söyler [AGENTS §3].
         · Çok bölümlü film düzeltmesi: sahne sayısı dosya başına MAX değil,
           numaraların BİRLEŞİMİ (BOLUM_1 13 + BOLUM_2 12 = 25).
D188 → MERCEK RUBRİKLERİNE İŞLENMEDİ · GEREKMEZ · mercek planı görmüyor ve
       mod V'de "eksik" diyemez. Bu operatör/betik tarafı bir kapıdır.

D189 → dört rubrik yamandı ✅ (⑤ cat.6 · ② cat.10 · ⑨ cat.7 · ① kapsam testi)
       Kök: ② "a thing never touched stays put" ile ⑤ "untouched ones are
       yours" aynı nesneyi ters yönde sahipleniyordu — ikisini de ben
       yazmıştım. Ayrım artık nesne SINIFI değil: adı olan nesne ②'nin,
       adsız alan ⑤'in. ⑨'un çapası DÖNÜŞ ister; ①'in testi mekanikleşti
       ("kendi satırındaki zaman kodlarını say").

D185 → TEKRAR 2 · ⛔ KAPI YAZILIYDI AMA BAĞLAMIYORDU. Hücreleri doğru
       adlandırıyor, ortalamadan düşürmüyordu. Düzeltildi.
       Etkisi: ⑫ 7,5 → GEÇERSİZ · ⑨ 4,5 → 5,3 (faz, sahip olmadığı bir
       kafiye çifti yüzünden cezalandırılıyordu — RHYME BROKEN düştü).
       ⭐ Bu, D74'ün ta kendisi: kaydı/koşusu olmayan kapı, kapı değildir.

D186 → TEKRAR 1 · ters uçtan: "kusur bulamadım" bu kez 7/10'a değil
       10,0/10'a yazıldı (⑥, yedi hücrede birebir "no deductions").
       TEMIZ_ISSUE genişletildi → ⑥'nın 10,0'ı `—`'ye düştü.
       ⭐ Altındaki kök CETVELDİ: 0,1 s / 5 cm'lik düşüşten g hesaplanmış.
       ⑥ rubriğine CETVEL TABANI eklendi (0,3 s / 0,5 m).

D110 → TEKRAR 3 · ⭐ İLK BETİK KAPISI (17.08.2026'dan beri operatör kuralıydı)
       `rapor_kontrol.py` ⑦ ORTAK DEFTER: künyesi (kesme·sahne·şerit) birebir
       aynı + çoğunluktan sapan + **kesme ZAMAN KODU basmamış** grup →
       "azınlık İKİ oy değil, BİR oydur". Partide tam bir kez: ⑦ + ⑧.
       ⚠️ İki daraltma gerekti: (1) anahtardan SÜRE çıktı — 109/110/111 aynı
       ölçümün yuvarlaması, süreyle birlikte kapı dört grubu işaretliyordu;
       (2) zaman kodu şartı eklendi — kopyanın imzası künyenin aynı olması
       DEĞİL, sayımın KANITININ olmamasıdır. Zaman kodu basan iki mercek
       gerçekten aynı şeyi saymış olabilir; o mutabakattır.

D187 → TEKRAR 1 · KİLİT 49'un beş kanıtından en fazla biri ölçüldü.
       ⭐ KAPI ADRESLENDİ: FAZ_DOSYASI_SABLONU.md'ye §BU FAZIN KİLİTLERİ
       bloğu eklendi — her kanıtın yanına ÖLÇEN MERCEK. Şablona yazıldı ki
       yeni fazlar doğarken alsın. ⬜ BETİK yarısı hâlâ AÇIK.

D137 → TEKRAR 6 · ilk kez YARIK: ① ve ③ "room tone present" + bağımsız
       olarak aynı saniyede aynı Foley kusuru (1:22); diğer sekizi
       "nothing audible to me". ⛔ Bu bir çelişki değil, iki TANIK ve on
       ÇEKİMSER — çapraz kapı bu satırları oy gibi okuyor.
       ⬜ AÇIK: tek ffprobe komutu, depo dışı, sahibin kararı.
```

⛔ **⑤ ÇAPRAZ SAYIM KAPISININ KÖR NOKTASI BU KOŞUDA GÖRÜLDÜ.** F9'da kapı
depoda ilk kez sıfır sapmayla kapanmıştı ve bunu bir başarı diye yazmıştık.
F10 aynı kapıyı geçti — dokuz mercek aynı şeridi yazdı — **ve şerit bir klip
eksikti.** Mutabakat ne kadar güçlüyse kayıt o kadar ikna edici görünüyor.
Kapı raporları birbirine bakar; parti dışındaki tek referans PLANDIR.

---

## 📅 08.09.2026 · THE OPEN CIRCUIT — ON İKİ MERCEK · SPEC **VE** PAKET HAZIRDI, ON İKİSİ DE MOD V

```
MASTER   : the open cırcuıt (1).mp4 · 235,14 s · 3840x2160 · 30 fps
           (ikiz: the open cırcuıt.mp4 — aynı süre, 1280x720)
PLAN     : 25 sahne · 249,0 s        MAKARA: 23 klip · 230,1 s + 5,0 s kart
KOŞU     : ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ — hepsi INPUT MODE: V
SONUÇ    : parti 🚨 GEÇERSİZ · T1-T12'ye SIFIR satır
```

**Neden bu koşu ayrı yazılıyor:** depoda ilk kez **on iki merceğin on ikisi**
aynı anda ve aynı yönde yanıldı, ve yanıldıkları şey filmin VAR OLUP OLMADIĞIYDI.
Ölçüm koşudan sonra yapıldı; bulduğu her şey rapor dışıdır:

```
· iki sahne makarada YOK — S17 ve S22; S22 filmin DORUĞU
  (iki sahnenin repliği de on iki raporun HİÇBİRİNDE duyulmamış:
   "Counted." · "Ground path is closed.")
· S2 ↔ S3 yer değiştirmiş (replik ekseni: #1/#2 bir klip erken)
· üretici filigranı 230 saniyenin 230'unda, 23/23 klipte
· doruğun boşalması ŞİMŞEK — 25 sahnenin negatifi "no lightning bolt" diyordu
· ışık takvimi geri sardı: sönen şeritler aynı klipte geri yandı,
  "no window strip is lit" promptuyla üretilen son iki sahne yanıyor
· planlı 2 s HARD MUTE hiç uygulanmamış · −16,6 LUFS / 0,0 dBFS
· ABD bayrağı yaması (196 s) · kubbe kask (25/25)
```

### 🧭 DERS → RUBRİK İZ DEFTERİ — 190-193 eki

```
D190 → 9_KADRAJ · 10_OYUNCULUK · 11_ISIK · 12_HOOK  ·  STEP −1 (INPUT MODE)
       YAMANDI: mod V artık bu dört mercekte DURDURUR ("THIS LENS DOES NOT
       RUN IN MODE V. STOP HERE." + üç satırlık LENS NOT RUN çıktısı).
       ⚠️ Gövdedeki mod V yuvaları (GRID GIVEN · N/A in mode V · ⑨'un
       "rhyme pair is run on every film, including in mode V") BIRAKILDI —
       künye satırlarını rapor_kontrol.py ayrıştırıyor. Bağlayıcı kapı
       BETİKTİR: ⑨-⑫ mod V = 🚨 GEÇERSİZ (karantina).
D190 → 1_KARE · 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 5_ARKA_PLAN · 6_FIZIK ·
       7_AKSIYON · 8_EFOR · GEREKMEZ · bu sekizi filmin KENDİSİYLE
       tutarlılığını ölçer; belgesiz koşuda ölçtükleri şey yine gerçektir,
       yalnız plana karşı okunamaz (D129 zaten TEKRAR diyor).
D191 → rubrik yaması YOK · GEREKMEZ · göz kapıları SPEC'in F bloğudur,
       rubriğin değil. Kapı rapor_kontrol.py ①.10'a indi: F bloğu her
       koşuda ⬜ listesi olarak basılır.
D192 → rubrik yaması YOK · kapı PLAN tarafında (03_PLAN_ONCESI A5).
       ⚠️ 6_FIZIK'in "measure it or say you could not" kuralı ŞİMŞEĞİ
       yakalayamadı: ⑥ olayı ölçtü, YÖNÜNÜ ters yazdı ve 10/10 verdi.
       ⬜ AÇIK: yön ölçümünün kanıtı (iki kare, önce-sonra) rubrikte
       zorunlu değil.
D193 → rubrik yaması YOK · kapı olcum_kapisi.sh'a indi (IŞIK TAKVİMİ İZİ).
       ⚠️ 11_ISIK key YÖNÜNÜ ölçüyor, kaynak SAYISINI ölçmüyor; takvim
       ekseni rubrikte hiç yok ve mod D'de de yoktu.
```

### 🔧 RUBRİK KOŞU SAYILARI — 08.09.2026 sonrası (THE OPEN CIRCUIT partisi)

```
1_KARE          · +1 · son 08.09.2026 · sonuç ⛔ TEKRAR (mod V · D129)
2_DEVAMLILIK    · +1 · son 08.09.2026 · sonuç ⚠️ ŞARTLI → parti geçersiz
3_SES           · +1 · son 08.09.2026 · sonuç ⚠️ ŞARTLI → parti geçersiz
4_HIKAYE        · +1 · son 08.09.2026 · sonuç 🚨 GEÇERSİZ (aritmetik fabrike)
5_ARKA_PLAN     · +1 · son 08.09.2026 · sonuç ✅ GO → parti geçersiz
6_FIZIK         · +1 · son 08.09.2026 · sonuç ⛔ TEKRAR
7_AKSIYON       · +1 · son 08.09.2026 · sonuç ⛔ TEKRAR
8_EFOR          · +1 · son 08.09.2026 · sonuç ⛔ TEKRAR
9_KADRAJ        · +1 · son 08.09.2026 · sonuç 🚨 GEÇERSİZ [D190 · yeni kural]
10_OYUNCULUK    · +1 · son 08.09.2026 · sonuç 🚨 GEÇERSİZ [D190]
11_ISIK         · +1 · son 08.09.2026 · sonuç 🚨 GEÇERSİZ [D190]
12_HOOK         · +1 · son 08.09.2026 · sonuç 🚨 GEÇERSİZ [D190]
```

⛔ **BU KOŞUNUN TEK CÜMLESİ:** on iki mercek filmin İÇİNE baktı ve on ikisi de
filmin YARISININ orada olmadığını göremedi. Mercek eklemek görüşü artırmıyor;
**parti dışındaki tek referans plan, plan dışındaki tek referans ölçümdür.**

---

### 🧭 DERS → RUBRİK İZ DEFTERİ — 194-195 eki (09.09.2026 · THE BENT GRASS)

```
D194 → 9_KADRAJ · 10_OYUNCULUK · 11_ISIK · YAMANDI
       `OBSERVED:` şablon satırına `in edit order, no spaces` eklendi —
       PRESENCE STRING bloğunun 22.08'den beri taşıdığı cümlenin aynısı.
       Rubrik boşluklu yazdırıyordu (`A B ? ? D E`), betiğin alfabe
       sınıfları boşluğu içermiyordu, üç mercek de "dizi YOK" sayıldı.
D194 → 7_AKSIYON (BEAT STRING) · 8_EFOR (COST CURVE) · YAMANDI ·
       KARDEŞ TARAMA [D111]: ikisi de "one character/digit per scene, in
       order" diyordu, `no spaces` cümlesi YOKTU — aynı malzemeyi görse
       aynı hatayı yapardı. ⑧'in örnek satırı (`000122334445553`) biçimi
       tesadüfen tutuyordu, ⑦'de o koruma bile yoktu.
D194 → 1_KARE · 2_DEVAMLILIK · 3_SES · 4_HIKAYE · 5_ARKA_PLAN · 6_FIZIK ·
       12_HOOK · GEREKMEZ · bu yedisi dizi ekseni üretmiyor; taşıdıkları
       tek dizi PRESENCE STRING ve o blok `no spaces` cümlesini zaten
       taşıyor (10 raporun 10'unda doğru okundu).
D194 → BETİK · rapor_kontrol.py · `gozlem_dizi()` ve `dizi_al()` boşluğu
       tolere eder. ⛔ Boşluk karakter sınıfının BAŞINA yazılır: sonuna
       eklenirse `OADU-` alfabesinde `U- ` geçersiz aralık olur ve betik
       PatternError ile ÇÖKER (yama sırasında bir kez oldu, düzeltildi).
       Doğrulama: ⑨ `AB??DE??F?G?A` · ⑩ `DOODA-OODODO-` · ⑪ `99?3999?99999`
       — üçü de 13 hane, ve ⑨ artık plan iskeletiyle karşılaştırılıyor
       ("SETUP STRING 13 hane, plan iskeleti 14 hane" = eksik sahne,
       teslim kusurunun BAĞIMSIZ ikinci ekseni).

D195 → rubrik yaması YOK · GEREKMEZ · kapı QA tarafında değil, ÜRETİM
       ÖNCESİ tarafta: prompt_kontrol.py ⑳ ZORLANMA KANALI.
D195 → BETİK · prompt_kontrol.py · `EFOR_PENCERE` iki zaman-çizelgesi
       biçimini de alır:  `^TIMELINE:` (18 dosya)  +  başlıksız
       `0s — / 3s — / 6s — / 8s —` (4 film: BENT_GRASS · COUNTED_TURN ·
       PRESSED_FIELD · STILL_SWARM). Pencere B biçiminde HİÇ açılmıyordu.
       Doğrulama (yama sonrası, daha önce görünmeyen bulgular):
         THE_BENT_GRASS 4 · THE_COUNTED_TURN 3 · THE_STILL_SWARM 2 ·
         THE_PRESSED_FIELD 0     → toplam 9
       Regresyon: A biçimli dosyalarda pencere hâlâ TIMELINE bloğunu alıyor
       (THE_SINKING_STAKE · THE_KEPT_LIGHT ile sınandı).
       ⬜ AÇIK: `EFOR_FIILI` sözlüğü (haul·pull·drag·lift·heave·prise·lever)
       THE_BENT_GRASS'ın işini (taşımak·diz çökmek·paketlemek·devirmek)
       KAPSAMIYOR. Liste altı filmlik ölçümle DARALTILDI; genişletme kararı
       yeni bir kalibrasyon koşusu ister, bu koşuda YAPILMADI.
```

### 🔧 RUBRİK KOŞU SAYILARI — 09.09.2026 (THE BENT GRASS partisi)

```
1_KARE        · +1 · 09.09.2026 · 🚨 GEÇERSİZ (parti · teslim kapısı D188)
2_DEVAMLILIK  · +1 · 09.09.2026 · 🚨 GEÇERSİZ (ayrıca aritmetik fabrike D161)
3_SES         · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: GO · 0 kategori ölçüldü)
5_ARKA_PLAN   · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: ŞARTLI)
6_FIZIK       · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: ŞARTLI · → ADAY-13)
7_AKSIYON     · +1 · 09.09.2026 · 🚨 GEÇERSİZ (10.0/10, 9 hücrenin 9'u kaynaksız)
8_EFOR        · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: GO · 4.0 WEIGHTLESS WORK)
9_KADRAJ      · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: ŞARTLI · → D194 kaynağı)
10_OYUNCULUK  · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: ŞARTLI)
11_ISIK       · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: ŞARTLI)
12_HOOK       · +1 · 09.09.2026 · 🚨 GEÇERSİZ (tekil: ŞARTLI)
4_HIKAYE      ·  0 · KOŞMADI — zorunlu eksen eksik [D111 · TEKRAR 2]
```

⛔ **BU KOŞUNUN TEK CÜMLESİ:** on bir mercek koştu, ikisi kendi kapısından
geçti, on biri de partiyle düştü — ve partiyi düşüren şey merceklerin
GÖRDÜĞÜ değil, ÖLÇÜLMEYEN şeydi. **Master verilmeden koşulan on bir mercek,
bir merceğin on bir katı kadar hakemsizdir.**

---

## 📅 13.09.2026 · THE STATIC SHADOW — ON ÜÇ MERCEK · SPEC HAZIRDI, ON İKİSİ MOD V · ⑬ DOĞRU DURDU · MASTER YOK

```
girdi:      operatör 13 raporu yapıştırdı; master yolu VERİLMEDİ, dosya diskte bulunamadı
            (raporlar "the statıc shadow.mp4" diyor). Ham raporların künyesinde girdi yolu ve
            rubrik sürümü YOK — ①③④ raporlarında rubriğin zorunlu kıldığı SCORES SUMMARY
            bölümü de yok (eski rubrik metni mi, model mi atladı: bilinmiyor).
SPEC:       yatay_2_dk_filmler/THE_STATIC_SHADOW/THE_STATIC_SHADOW_QA_SPEC.md VARDI
            → ①④⑥⑦⑧ TEKRAR [D129 · 17. film] · ⑨⑩⑪⑫ GEÇERSİZ/karantina [D190 · 2. vaka]
            ⛔ ve SPEC'in kendisi KABUK: yedi makine çapasının yedisi yok → D204
⑬ UYUM:     INPUT MODE: MISSING — STEP −1 doğru işledi. Üretim defteri BOŞ (teslim ⬜, 0 klip),
            prompt ve SPEC verilmemiş. "DEFTERSİZ ⑬ KOŞUSU YOKTUR" kuralının ilk vakası: kural tuttu.
betik:      rapor_kontrol.py --film … --hook 10 --klip 10 · ölçüm bayrağı yok
            13/13 🚨 GEÇERSİZ · ①.9 TESLİM ŞÜPHESİ plan 15 / makara 12 [D188 · 3. vaka] ·
            ⑤ SUSKUNLUK (⑤ filigran, ① sustu) İLK KEZ gerçek iddiada ateşledi [D162] ·
            ⑤ SÜRE (bu koşuda yazıldı, D205) ⑩ 60 s ve ⑫ 25 s'yi yakaladı
            ⚠️ ilk koşuda 8 raporun künyesi okunamadı: 02_HAM_RAPORLAR künye bloğu '---' ile
            kapanmalı (govde_al ilk '---'dan başlar); dosyalara ayraç eklendi, koşu tekrarlandı.
belgeden:   plan 7 HELIOS repliği · SPEC "DIALOGUE LINES: 7" · 30 promptta tırnak 0 → D203 (㉓)
            geriye dönük aynı arıza: THE MIRROR FAUNA 11 → 0 (09.09 mod D partisi görmemişti)
```

### 🧭 DERS → RUBRİK İZ DEFTERİ — 203-205 eki

```
D203 → rubrik yaması YOK · GEREKMEZ · kapı ÜRETİM ÖNCESİ tarafta: prompt_kontrol.py ㉓
       REPLİK ENVANTERİ (klasör modu; SPEC DIALOGUE LINES ↔ tırnaklı replik; 0 → BLOCK).
       ③ SES rubriğine SPEC verilmez (tasarım) — 3_SES'e "SPEC N diyor, sen kaç duydun"
       satırı yazılmadı, çünkü mod V'de SPEC yoktur; mod D'de ise ㉓ zaten üretimden önce
       durdurur. Kardeş rubrik taraması: ①②④-⑫ aynı hatayı üretemez (replik yokluğunu
       ölçen tek mercek ③, o da sayıyı SPEC'ten alamaz) → GEREKMEZ.
       Kalibrasyon: 38 SPEC · 2 gerçek pozitif (STATIC SHADOW · MIRROR FAUNA) · 0 yanlış
       pozitif — ilk sürüm satır sonu aşan tırnağı saymıyordu (LOSS OF LIFT · BORROWED
       WEIGHT yanlış BLOCK), 240 karakter sınırlı çok-satırlı desene çevrildi.
D204 → rubrik yaması YOK · GEREKMEZ · kapı yazım tarafında: prompt_kontrol.py ㉔ SPEC TAMLIK.
       rapor_kontrol.py zaten SPEC'i okuyor (①.9 · ①.10); eksik bloğu "hata" değil "yok"
       sayıyordu — ㉔ ondan önce, kart P'de yakalar. Tetik: 00_ANALIZ/ olan klasör.
       Kalibrasyon: 38 SPEC'in 1'i tam (HARD DOCK); 7 yeni-film klasörü FIX/BLOCK.
D205 → rubrik yaması YOK · GEREKMEZ · kapı betikte: rapor_kontrol.py capraz() ⑤ SÜRE satırı
       + --olcum-sure. Rubrikler RUNTIME'ı zaten "measured" yazmak zorunda; ölçemedikleri
       şeyi daha dikkatli ölçmelerini istemek D137'nin kibar hâli olurdu.
       Regresyon: THE UPWARD FALL 8 rapor → "süre ekseni doğrulandı, ortanca 226 s".
D168 → araca çevrildi (KARAR): FILM_KLASOR_SABLONU/FILM_URETIM_DEFTERI.md §4 ilk-KABUL
       maddesi + AGENTS kart B satırı. Rubrik tarafı yok.
```

### 🔧 RUBRİK KOŞU SAYILARI — 13.09.2026 (THE STATIC SHADOW partisi)

```
1_KARE        · +1 · 13.09.2026 · 🚨 GEÇERSİZ (mod V · SPEC var [D129] · SCORES SUMMARY yok)
2_DEVAMLILIK  · +1 · 13.09.2026 · 🚨 GEÇERSİZ (parti · tekil: ŞARTLI 8,7)
3_SES         · +1 · 13.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY yok · 0 replik = prompt boşluğu D203)
4_HIKAYE      · +1 · 13.09.2026 · 🚨 GEÇERSİZ (mod V · SPEC var · harita bir sahne kaymış D135)
5_ARKA_PLAN   · +1 · 13.09.2026 · 🚨 GEÇERSİZ (parti · tekil: ŞARTLI 7,2 · filigran iddiası → SUSKUNLUK)
6_FIZIK       · +1 · 13.09.2026 · 🚨 GEÇERSİZ (tekil: TEKRAR · 1:6 ölçek "tutarlı" — SPEC 1/30 · ADAY-91)
7_AKSIYON     · +1 · 13.09.2026 · 🚨 GEÇERSİZ (tekil: TEKRAR)
8_EFOR        · +1 · 13.09.2026 · 🚨 GEÇERSİZ (tekil: TEKRAR · 1,0 NOBODY PAYS · ADAY-93)
9_KADRAJ      · +1 · 13.09.2026 · 🚨 GEÇERSİZ (mod V karantina D190 · 5 hücre "no in-scope source" D131)
10_OYUNCULUK  · +1 · 13.09.2026 · 🚨 GEÇERSİZ (mod V karantina · RUNTIME 60 s uydurma D205)
11_ISIK       · +1 · 13.09.2026 · 🚨 GEÇERSİZ (mod V karantina)
12_HOOK       · +1 · 13.09.2026 · 🚨 GEÇERSİZ (mod V karantina · RUNTIME 25 s uydurma D205)
13_UYUM       · +1 · 13.09.2026 · ⏸️ KOŞU YOK — INPUT MODE: MISSING, rubrik doğru durdu (defter boş)
```

⛔ **BU KOŞUNUN TEK CÜMLESİ:** on üç mercek koştu, hiçbiri ekran hakkında kullanılabilir bir
şey söyleyemedi (master yok, SPEC verilmedi, teslim eksik) — ve partiden çıkan üç ders üç
BELGEDEN çıktı: plan ↔ prompt (replik) · şablon ↔ SPEC (kabuk) · rapor ↔ rapor (süre).
**Belge, raporun söyleyemediğini söyledi.**

---

### 🔧 RUBRİK KOŞU SAYILARI — 13.09.2026 (THE SILENT PERIHELION partisi)

```
1_KARE        · +1 · 13.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı / Mod V ön koşu [D129])
2_DEVAMLILIK  · +1 · 13.09.2026 · ⚠️ ŞARTLI 8,8 (T2 tablosuna eklendi; verdict: FIXABLE IN EDIT)
3_SES         · +1 · 13.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı)
4_HIKAYE      · +1 · 13.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı / Mod V ön koşu [D129])
5_ARKA_PLAN   · +1 · 13.09.2026 · ✅ GO 7.8 (T5 tablosuna eklendi; verdict: FIELD DRIFTS BUT RECOVERABLE)
6_FIZIK       · +1 · 13.09.2026 · ⛔ TEKRAR 6.0 (Mod V / SPEC var [D129])
7_AKSIYON     · +1 · 13.09.2026 · ⛔ TEKRAR 8.7 (Mod V / SPEC var [D129])
8_EFOR        · +1 · 13.09.2026 · ⛔ TEKRAR 5.9 (Mod V / SPEC var [D129])
9_KADRAJ      · +1 · 13.09.2026 · 🚨 GEÇERSİZ 8.5 (Mod V karantina [D190])
10_OYUNCULUK  · +1 · 13.09.2026 · 🚨 GEÇERSİZ 6.7 (Mod V karantina [D190])
11_ISIK       · +1 · 13.09.2026 · 🚨 GEÇERSİZ 5.6 (Mod V karantina [D190])
12_HOOK       · +1 · 13.09.2026 · 🚨 GEÇERSİZ 6.0 (Mod V karantina [D190])
```

> Çalıştırma kaydı: 12 mercek çalıştırıldı · 13.09.2026 · THE SILENT PERIHELION (Mod V ham raporlar: 1 ✅ GO 7.8, 1 ⚠️ ŞARTLI 8.8, 3 ⛔ TEKRAR, 7 🚨 GEÇERSİZ; ham raporlar 02_HAM_RAPORLAR/THE_SILENT_PERIHELION/ altında saklandı, T2 ve T5 tabloları güncellendi).

---

### 🔧 RUBRİK KOŞU SAYILARI — 14.09.2026 (THE SHATTERED BREATH partisi — 12 mercek tamamlama)

```
1_KARE        · +1 · 14.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı / Mod V ön koşu [D129])
2_DEVAMLILIK  · +1 · 14.09.2026 · 🚨 GEÇERSİZ (aritmetik fabrike D161: metin Σ=71.0, tablo toplamı 75.0)
3_SES         · +1 · 14.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı)
4_HIKAYE      · +1 · 14.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı / Mod V ön koşu [D129])
5_ARKA_PLAN   · +1 · 14.09.2026 · ⚠️ ŞARTLI 8,3 (T5 tablosuna eklendi; verdict: FIELD DRIFTS BUT RECOVERABLE)
6_FIZIK       · +1 · 14.09.2026 · ⛔ TEKRAR 7,0 (Mod V / SPEC var [D129])
7_AKSIYON     · +1 · 14.09.2026 · ⛔ TEKRAR 8,6 (Mod V / SPEC var [D129])
8_EFOR        · +1 · 14.09.2026 · ⛔ TEKRAR 2,7 (Mod V / SPEC var [D129])
9_KADRAJ      · +1 · 14.09.2026 · 🚨 GEÇERSİZ 10,0 (Mod V karantina [D190 · D184])
10_OYUNCULUK  · +1 · 14.09.2026 · 🚨 GEÇERSİZ 4,8 (Mod V karantina [D190] + süre 41s uydurma [D205])
11_ISIK       · +1 · 14.09.2026 · 🚨 GEÇERSİZ 5,0 (Mod V karantina [D190])
12_HOOK       · +1 · 14.09.2026 · 🚨 GEÇERSİZ 5,0 (Mod V karantina [D190])
```

> Çalıştırma kaydı: 12 mercek çalıştırıldı · 14.09.2026 · THE SHATTERED BREATH (Mod V ham raporlar: 12 mercek tamamlandı; 1 ⚠️ ŞARTLI 8.3 [T5], 3 ⛔ TEKRAR [6,7,8], 8 🚨 GEÇERSİZ; ham raporlar 02_HAM_RAPORLAR/THE_SHATTERED_BREATH/ altında saklandı, T5 tablosu güncellendi).

---

### 🔧 RUBRİK KOŞU SAYILARI — 14.09.2026 (THE LOCKED PULSE partisi — 12 mercek tamamlama)

```
1_KARE        · +1 · 14.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı / Mod V ön koşu [D129])
2_DEVAMLILIK  · +1 · 14.09.2026 · 🚨 GEÇERSİZ (parti kesme yayılımı 7 > 1 [D107])
3_SES         · +1 · 14.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı)
4_HIKAYE      · +1 · 14.09.2026 · 🚨 GEÇERSİZ (SCORES SUMMARY okunamadı / Mod V ön koşu [D129])
5_ARKA_PLAN   · +1 · 14.09.2026 · 🚨 GEÇERSİZ (parti kesme yayılımı 7 > 1 [D107])
6_FIZIK       · +1 · 14.09.2026 · 🚨 GEÇERSİZ (parti kesme yayılımı 7 > 1 [D107])
7_AKSIYON     · +1 · 14.09.2026 · ⛔ TEKRAR (Mod V / SPEC var [D129])
8_EFOR        · +1 · 14.09.2026 · ⛔ TEKRAR (Mod V / SPEC var [D129])
9_KADRAJ      · +1 · 14.09.2026 · 🚨 GEÇERSİZ (Mod V karantina [D190 · D184])
10_OYUNCULUK  · +1 · 14.09.2026 · 🚨 GEÇERSİZ (Mod V karantina [D190 · D184])
11_ISIK       · +1 · 14.09.2026 · 🚨 GEÇERSİZ (Mod V karantina [D190 · D184])
12_HOOK       · +1 · 14.09.2026 · 🚨 GEÇERSİZ (Mod V karantina [D190 · D184])
```

> Çalıştırma kaydı: 12 mercek çalıştırıldı · 14.09.2026 · THE LOCKED PULSE (Mod V ham raporlar: 12 mercek tamamlandı; parti kesme yayılımı 7 > 1 [D107 · D188] nedeniyle 12 🚨 GEÇERSİZ; ham raporlar 02_HAM_RAPORLAR/THE_LOCKED_PULSE/ altında saklandı; master video `olcum_kapisi.sh` ile taranmayı bekliyor).

## 🥗 14.09.2026 · RUBRİK DİYETİ — ①-⑥ 25 KB TAVANI (koşu değil, rubrik revizyonu)

```
① KARE         61.054 → 25.681 B   + 1_KARE_DIKEY_EK.md (3,8 KB, yalnız dikey)
② DEVAMLILIK   38.240 → 20.078 B
③ SES          40.118 → 20.316 B
④ HİKAYE       49.519 → 24.646 B
⑤ ARKA PLAN    29.985 → ~16 KB
⑥ FİZİK        33.484 → 19.704 B
DEĞİŞMEYEN: kategori adları · SCORES SUMMARY · başlık alanları · tracking row · MERCEK_IMZA
KESİLEN → ARSIV_CIKTI_KURALLARI.md + ARSIV_RUBRIK_DIYETI/ (tam kopyalar)
⚠️ Bu tarihten sonraki ilk koşu her rubrik için "diyet sonrası 1. koşu" olarak buraya
   yazılır; T tablosu satırına 'diyet sonrası' notu düşer — puan kayması varsa ölçülür.
```

---

## 📉 TABAN ÇİZGİSİ — 14.09.2026 kesiti (rubrik diyeti ve çıktı sözleşmesi ÖNCESİ)

> `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/qa_saglik.py --ozet` çıktısı, olduğu
> gibi (sayı elle yazılmadı; betik bastı). Diyet (14.09 ①-⑥ ≤ 25 KB) ve çıktı sözleşmesi
> (14.09 FAZ 1: model saymaz, betik sayar) sonrası ilk 3 filmde aynı komut koşulur ve bu
> bloğun altına tarihli ikinci kesit eklenir. Dört sayı izlenir: **tekil GO oranı ·
> tally = etiket · ✂️ KESİK · rapor boyutu medyanı** — dördü birden kıpırdamıyorsa
> sözleşme değişikliği işe yaramamıştır. Ayrıntı: `TODO_QA_CIKTI_REFORMU.md`.
> ⚠️ "⑤ çapraz sonrası" satırı: mercekler kesme/sahne sayısında anlaşamayınca parti
> komple düşüyor — 41 filmin 25'i. Makine sayımı (`sahne_kapisi.sh` · ⑬) bu satırın ilacıdır.

```
   336 mercek raporu · 41 film · 29 mercek dışı dosya (faz/kapak/kapı) · tarama 2 s
   tekil karar : ✅ GO 26 (7%) · ⚠️ ŞARTLI 114 · ⛔ TEKRAR 85 · 🚨 GEÇERSİZ 57 · ✂️ KESİK 54
   ⑤ çapraz sonrası (tabloya giren): ✅ GO 3 · ⚠️ ŞARTLI 39 · 🚨 GEÇERSİZ 221 — parti düşen film 25 / 41 [D107 · D121]
   en az bir GO raporu olan film 3 / 41
   ── mercek ──            n   modD    GO  ŞART  TEKR  GEÇ  KESİK  tally=etk  VERDICT  boyut  kaynaksız
   ① KARE            36   13%     0     3     5   16     12    35%       87% satır   5.2KB   19%
   ② DEVAMLILIK      35    2%     1     6     0   26      2    44%       75% satır   8.2KB   13%
   ③ SES             38    0%     1     7     0   16     14    65%       95% satır   5.6KB   15%
   ④ HİKAYE          32    9%     0     2     5   13     12     —       90% satır   7.6KB    2%
   ⑤ ARKA PLAN       34    0%     0     9     0   24      1    43%       69% satır   9.5KB    8%
   ⑥ FİZİK           33   15%     0     3     5   24      1    29%       78% satır   5.6KB   12%
   ⑦ AKSİYON         26   23%     0     1     2   22      1    25%       68% satır   7.0KB   32%
   ⑧ EFOR            25   20%     0     2     2   19      2    36%       65% satır   6.6KB   11%
   ⑨ KADRAJ          19   21%     0     1     0   16      2    43%       47% satır   5.9KB   18%
   ⑩ OYUNCULUK       18   27%     1     1     0   15      1    37%       82% satır   6.3KB    2%
   ⑪ IŞIK            21   23%     0     2     0   15      4    68%       47% satır   7.0KB   10%
   ⑫ HOOK            19   26%     0     2     0   15      2    50%       58% satır   5.1KB    9%
   ⑬ UYUM                 0   —      koşulmamış
```

---

## 📜 14.09.2026 · ÇIKTI SÖZLEŞMESİ — 13 rubrik (QA çıktı reformu FAZ 1)

> Ne değişti (her rubrikte aynı): SEVERITY TALLY bölümü · ARITHMETIC GATE (SCORED /
> SUM / DIVISION) · OVERALL SCORE satırı ÇIKTI; SCORES SUMMARY kuralı ⑤ "do not total,
> average or tally — the library's script counts"; "no in-scope source" → `—` (⑦-⑫'de
> "keeps 10/10" kalktı); VERDICT kapalı listesi başlıktan tablonun ALTINA taşındı;
> tracking row son hücresi `—`. ⑬: SCORED/SUM/DIVISION/OVERALL bloğu çıktı, sahne başına
> karar kaldı. Kategori adları, `MERCEK_IMZA` ifadeleri, başlık alanları DONUK
> (rapor_kontrol 13/13 mercek tanıyor). Çıkarılan metin `ARSIV_CIKTI_KURALLARI.md`.
> Betik tarafı: `rapor_kontrol.py` ①.13 HÜKÜM (VERDICT_SOZLUK) · ✂️ KESİK · `govde_al`
> künye düzeltmesi · `ders_frekans` sözlüğe hizalandı (sözlük dışı hüküm ayrı sayılır).
>
> ⚠️ Bu değişikliğin modelin çıktısına etkisi depoda ÖLÇÜLEMEZ (dış model). Sözleşme
> sonrası ilk 3 filmde `qa_saglik.py --ozet` koşulur; aşağıdaki kesitle karşılaştırılır.
> Betik düzeltmelerinin (KESİK · govde_al · ①.13) ESKİ raporlara etkisi — aynı raporlar,
> yeni betik:

```
   336 mercek raporu · 41 film · 29 mercek dışı dosya (faz/kapak/kapı) · tarama 3 s
   tekil karar : ✅ GO 21 (6%) · ⚠️ ŞARTLI 118 · ⛔ TEKRAR 84 · 🚨 GEÇERSİZ 59 · ✂️ KESİK 54
   ⑤ çapraz sonrası (tabloya giren): ✅ GO 2 · ⚠️ ŞARTLI 32 · 🚨 GEÇERSİZ 229 — parti düşen film 26 / 41 [D107 · D121]
   en az bir GO raporu olan film 2 / 41
   ── mercek ──            n   modD    GO  ŞART  TEKR  GEÇ  KESİK  tally=etk  VERDICT  boyut  kaynaksız
   ① KARE            36   13%     0     3     5   16     12    35%       87% sözlük  5.2KB   19%
   ② DEVAMLILIK      35    2%     0     6     0   27      2    44%      100% sözlük  8.2KB   13%
   ③ SES             38    0%     1     7     0   16     14    65%       83% sözlük  5.6KB   15%
   ④ HİKAYE          32    9%     0     2     5   13     12     —       90% sözlük  7.6KB    2%
   ⑤ ARKA PLAN       34    0%     0     8     0   25      1    43%       90% sözlük  9.5KB    8%
   ⑥ FİZİK           33   15%     0     2     5   25      1    29%       93% sözlük  5.6KB   12%
   ⑦ AKSİYON         26   23%     0     1     2   22      1    25%       88% sözlük  7.0KB   32%
   ⑧ EFOR            25   20%     0     1     2   20      2    36%       91% sözlük  6.6KB   11%
   ⑨ KADRAJ          19   21%     0     0     0   17      2    43%       82% sözlük  5.9KB   18%
   ⑩ OYUNCULUK       18   27%     1     0     0   16      1    37%       88% sözlük  6.3KB    2%
   ⑪ IŞIK            21   23%     0     1     0   16      4    68%       88% sözlük  7.0KB   10%
   ⑫ HOOK            19   26%     0     1     0   16      2    50%       88% sözlük  5.1KB    9%
   ⑬ UYUM                 0   —      koşulmamış
```

---

## 🧍🧭 14.09.2026 · ⑭ HAREKET + ⑮ YÖN YAZILDI (koşu yok — sahip talebi)

> Talep: *"filmlerde saçma sapan hareketler yapıyorlar, yanlış yere dönmek, ateş etmek vs.
> — tespit edelim, ders çıkarabilelim."* İki mercek, iki soru: ⑭ **"beden bunu NEDEN yaptı"**
> (AMAÇ CÜMLESİ · 13 kapalı etiket · PURPOSE STRING · 8 kategori · hüküm: MOTION MAKES SENSE /
> MINOR TWITCHES / FIXABLE IN EDIT / PUPPET MOTION / MOTION WITHOUT PURPOSE) · ⑮ **"vektör
> hedefe vardı mı"** (VEKTÖR CÜMLESİ · HIT / MISS / UNKNOWN / NO TARGET / FLIP · VECTOR STRING ·
> 8 kategori · hüküm: EVERY VECTOR LANDS / MINOR MISAIMS / FIXABLE IN EDIT / WRONG WAY / AIMED
> AT NOTHING). İkisi de yeni çıktı sözleşmesiyle doğdu ve ürünü **PROMPT ORDERS** tablosudur
> (sonraki filmin prompt satırı → kart G). Sınırlar rubrikte tek cümle: ⑦ ne oldu · ⑥ kaç
> saniye · ⑩ ne hissetti · ② aynı mı · ⑨ kamera nerede · ⑭ NEDEN · ⑮ DOĞRU YERE Mİ.
> Betik: `rapor_kontrol.py` imza · mod D · PREMISE (NOVUM) · VERDICT_SOZLUK · PURPOSE/VECTOR
> STRING = kesme+1 · MOVEMENTS/ACTS sayımı; sentetik raporla sınandı (⑭ ŞARTLI D186 · ⑮ ŞARTLI
> D186 — kapılar çalışıyor). Tablolar T14/T15 açıldı, boş.
> ⚠️ Gerçek koşu yok. İlk koşu geldiğinde: `rapor_kontrol.py <rapor> --film <FILM>` · ham
> `<FILM>_HAREKET_HAM.md` / `<FILM>_YON_HAM.md` · PROMPT ORDERS satırları GOZLEM_DEFTERI'ne
> ADAY olarak (tek film) — ikinci filmde aynı etiket → ders.

> Çalıştırma kaydı: henüz koşu yok.
