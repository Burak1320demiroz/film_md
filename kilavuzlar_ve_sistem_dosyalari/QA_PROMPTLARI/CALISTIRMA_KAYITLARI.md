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

# 🧭 DERS → RUBRİK İZ DEFTERİ

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
