# 🧮 THE_COUNTED_RIVET — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> THE_COUNTED_RIVET S<nn> <ROL>`
> ile damgalanır (`S<nn>_<ROL>.md`, tam şablon). ≤ 8 sahnelik filmde (dikey)
> bu dosya yoktur, her sahne dosya alır.
>
> Kapı: `prompt_kontrol.py` ㉚ — satır sayısı = bölüm dosyalarındaki sahne
> sayısı · beş rol dosyası var. Satırlar betik damgalar (`| S00 |` …); elle
> satır eklenmez/silinmez, sahne sayısı değişirse `--sahne-guncelle`.
>
> 🆕 **22.09.2026 · ÇOK KLİPLİ SAHNE** (`--sahne-plani` ile açılan yatay film): satır
> KLİP başınadır; betik başlığa iki sütun ekler ve satırları `| K07 | S03 | 2/3 · ⬜ |`
> biçiminde damgalar. **ROL n/N** sütununa kapsama şablonundaki rol yazılır (KURULUM ·
> EYLEM · TEPKİ · BELİRİŞ · MÜCADELE · TERSLİK · KARAR · BEDEL · DÖNÜŞ). Klibin
> `OLAY BAŞ → SON` hücresinin SON yarısı, aynı sahnedeki bir sonraki klibin
> `CONTINUOUS ACTION:` satırına kelimesi kelimesine iner [D207]. Aynı sahnenin
> `IŞIK · SES · FİZİK` hücreleri birebir aynıdır (sahne kilidi); "öncekiyle AYNI olamaz"
> kuralı yalnız SAHNELER ARASINDA geçerlidir. ㉚ SAHNE sütununu SAHNE PLANI'yla
> karşılaştırır. Kural: `COK_KLIPLI_SAHNE_KILAVUZU.md`.
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

| K | SAHNE | ROL n/N | OLAY BAŞ → SON | B5 | KURULUM | OPTİK (eni m · px) | IN FRAME | TAŞIYICI | IŞIK · SES · FİZİK | REPLİK | KİLİT / UYARI | İZLEYİCİ CÜMLESİ | KAPI |
|:--:|:--:|---|---|:--:|---|---|---|---|---|---|---|---|:--:|
| K01 | S01 | 1/1 · HOOK | iki eldiven mandal kolunda, çene açık ve yüzeye değmiş → çene kapanmış, iç yüzeyle arasında hiçbir yerde ışık yok | — | **B** · 50mm · 1,2 m · h 1,15 m · CU · üç-çeyrek | 0.86 m · çene 0,30 m = 1333 px | hands | mandal çenesi girer (S7'ye kadar taşınır) | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D157 · D210 · ⚠️1 | Bu ölçünün tutması gerekiyor ve tutmuyor. | ✅ |
| K02 | S02 | 1/3 · KURULUM | eldivenler bağlama kolunun kulpunda, ağırlık geride → kol açılmış, kehribar lamba ikinci kez atmış | İSTEK | **F** · 35mm · 1,4 m · h 0,90 m · MS · alçak orta | 1.44 m · eldiven 0,25 m = 667 px | hands · torso | bağlama kolu + kehribar lamba girer | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D169 · ⚠️5 | Vardiyayı bitirmek istiyor. | ✅ |
| K03 | S02 | 2/3 · EYLEM | botlar güverte çıkıntısına dayalı, çekiç havada → ikinci kazık iki parmak girmiş, gövde ikinci yüklenmenin içinde | İSTEK | **A** · 24mm · 4,0 m · h 1,50 m · WS · göz hizası | 6.00 m · figür 1,70 m = 1088 px | full body | çekiç girer (K04'te bırakılır) · dokuz mandal yuvası girer | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D206 · D209 · D192 | Cephe gelmeden dokuzu bitirmek istiyor. | ✅ |
| K04 | S02 | 3/3 · TEPKİ | eldivenler çenede, ikinci kazık yarı girmiş → çekiç bırakılmış, iki eldiven çenenin iki yanında ve durmuş, omuzlar inmiş | ENGEL | **F** · 🔁 dönüş K02 · 35mm · 1,4 m · h 0,90 m · MS · alçak orta | 1.44 m · eldiven 0,25 m = 667 px | hands · torso | çekiç çıkar · çene taşınır | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D213 · D207 · ⚠️1 | Bir şeyin yanlış olduğunu biliyor ama neyin olduğunu bilmiyor. | ✅ |
| K05 | S03 | 1/4 · BELİRİŞ | geri adım, gövde geriye yatık, plaka kadrajın üstünü kaplıyor → iki adım geride, kask yukarı dönük, plaka hâlâ kadrajın üstünü kaplıyor | ENGEL | **E** · 24mm · 5,0 m · h 0,50 m · WS · alt açı | 7.50 m · perçin başı 0,50 m = 256 px | full body | plaka + perçin sıraları girer | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D209 · D200 · ⚠️4 | Ne kadar büyük olduğunu görmek istiyor ve kenarını bulamıyor. | ✅ |
| K06 | S03 | 2/4 · MÜCADELE | eldivenler çeneyi ikinci kez kapatıyor, ağırlık önde → çene kapalı, boşluk hâlâ yok, sol eldiven kulpu sıkıp bırakıyor | ENGEL | **F** · 🔁 dönüş K04 · 35mm · 1,4 m · h 0,90 m · MS · alçak orta | 1.44 m · eldiven 0,25 m = 667 px | hands · torso | çene taşınır | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D192 · D169 · ⚠️1 | Makinenin ölçüsüne bir kez daha güvenmek istiyor. | ✅ |
| K07 | S03 | 3/4 · TERSLİK | güverte boyunca durmuş, kehribar lamba atıyor → otomasyonun kolu mandalı yeniden germiş, lamba aynı periyotta atıyor, omuz bir nefesle kalkıp iniyor | MUHATAP | **A** · 🔁 dönüş K03 · 24mm · 4,0 m · h 1,50 m · WS · göz hizası | 6.00 m · figür 1,70 m = 1088 px | full body | otomasyon kolu girer · lamba taşınır | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D172 · D202 · ⚠️5 | Makinenin ona katılmasını bekliyor ve makine katılmıyor. | ✅ |
| K08 | S03 | 4/4 · KARAR | sırtı dönük, eldivenler mandal kolunu bırakıyor → botlar kumanda kolunun yanına yerleşmiş, bir eldiven kolda | ENGEL | **G** · 35mm · 2,4 m · h 1,70 m · MS · arkadan/OTS | 2.47 m · sırt 0,55 m = 856 px | back | mandal kolu bırakılır · kumanda kolu girer | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D139 · D202 · ⚠️9 | Makinenin ölçüsünü bırakıp platformu kendisi yürütmeyi seçiyor. | ✅ |
| K09 | S04 | 1/4 · BELİRİŞ | platform kaymaya başlamış, ilk perçin sırası güverte kenarını geçiyor → üçüncü sıra geçiyor, gövde korkuluğa yatık | ENGEL | **E** · 🔁 dönüş K05 · 24mm · 5,0 m · h 0,50 m · WS · alt açı | 7.50 m · perçin başı 0,50 m = 256 px | full body | perçin sıraları taşınır (sayaç 2 açılır) | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D78 · D200 · ⚠️2 | Yüzeyin bir yerde bitmesini istiyor. | ✅ |
| K10 | S04 | 2/4 · MÜCADELE | iki eldiven korkulukta, ağırlık önde → eldivenler korkulukta, başparmak her sıra geçişinde bir kez basıp bırakıyor | ENGEL | **F** · 🔁 dönüş K06 · 35mm · 1,4 m · h 0,90 m · MS · alçak orta | 1.44 m · eldiven 0,25 m = 667 px | hands · torso | korkuluk girer · sayım jesti girer | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D78 · D169 | Sıraları sayarak kenarı buluyor sanıyor. | ✅ |
| K11 | S04 | 3/4 · TERSLİK | sırayla geçen perçinler, gövde korkulukta → kırk saniye geçti, geçen sıra sayısı arttı, yüzey bitmiyor | ENGEL | **E** · 🔁 dönüş K09 · 24mm · 5,0 m · h 0,50 m · WS · alt açı | 7.50 m · perçin başı 0,50 m = 256 px | full body | perçin sıraları taşınır | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D78 · D209 · ⚠️4 | Saydığı şeyin bitmeyeceğini anlamaya başlıyor. | ✅ |
| K12 | S04 | 4/4 · KARAR | sırtı dönük, kumanda kolunda → otomasyonun kolu üçüncü kez germiş, teknisyen kumandayı bırakıp güverte kenarına dönmüş | MUHATAP | **G** · 🔁 dönüş K08 · 35mm · 2,4 m · h 1,70 m · MS · arkadan/OTS | 2.47 m · sırt 0,55 m = 856 px | back | kumanda kolu bırakılır | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D139 · D172 · ⚠️5 | Makinenin kaydına karşı kendi ölçüsünü almaya gidiyor. | ✅ |
| K13 | S05 | 1/3 · KURULUM | eldivenler örtünün kenarına gelmiş, bağ delikleri sıralı, bıraktığı mandal kolu kadrajın kenarında → sağ eldiven bağın ucunu kavramış, sol eldiven kenarı bastırıyor | BEDEL | **H** · 50mm · 0,75 m · h 1,10 m · CU · profil insert | 0.54 m · şerit 0,60 m kadrajı geçer · boşluk eşiği 2 cm = 142 px | hands | örtü kenarı + bağ girer · REDDEDİLEN NESNE (mandal kolu) kadrajda kalır | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | D202 · ⚠️7 · ⚠️6 | Kendi cetvelini almak istiyor ve bedelini biliyor. | ✅ |
| K14 | S05 | 2/3 · EYLEM | iki eldiven bağda kapalı, ağırlık geride, botlar çıkıntıya dayalı → bağ deliklerden boşalmış, örtünün kenarı açık, omuzlar inmiş ve kalkmıyor | BEDEL S5 | **F** · 🔁 dönüş K10 · 35mm · 1,4 m · h 0,90 m · MS · alçak orta | 1.44 m · eldiven 0,25 m = 667 px | hands · torso | bağ çıkar (geri dönmez) · örtünün açık kenarı girer | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | ⛔1 · ⛔2 · D206 | Haklı olmak için kendini havada tutan şeyi açıyor. | ✅ |
| K15 | S05 | 3/3 · SONUÇ | eldivenler çelik şeridi plakaya yatırıyor, şerit kadrajı geçiyor → şerit plakaya yatık, boyunca hiçbir yerde ışık yok, eldivenler şeridin iki ucunda | BEDEL | **H** · 🔁 dönüş K13 · 50mm · 0,75 m · h 1,10 m · CU · profil insert | 0.54 m · şerit 0,60 m kadrajı geçer · boşluk eşiği 2 cm = 142 px | hands | çelik şerit girer (bağdan çıktı) | kubbe okra 0 · alçak uğultu · 0,904 g nötr yüzerlik | — | ⛔3 · ⛔4 · D157 | Haklı çıkıyor ve bunun ne demek olduğunu görüyor. | ✅ |
| K16 | S06 | 1/4 · BELİRİŞ | perçin sıraları geçiyor, gövde korkulukta, omuzlar düşük → sıralar daha sık geçiyor, kubbe bir kademe koyu | BEDEL | **E** · 24mm · 5,0 m · h 0,50 m · WS · alt açı | 7.50 m · perçin başı 0,50 m = 256 px | full body | perçin sıraları taşınır (sayaç 2 hızlanır) | kubbe okra 1 · uğultu bir kademe kalın · 0,904 g, iniş iki kat | — | ⛔8 · ⚠️3 · ⚠️8 | İnişin hızlandığını sıralardan okuyor. | ✅ |
| K17 | S06 | 2/4 · MÜCADELE | eldivenler korkulukta, omuzlar düşük → başparmak sayımı hızlanmış, eldivenler korkulukta | BEDEL | **F** · 🔁 dönüş K14 · 35mm · 1,4 m · h 0,90 m · MS · alçak orta | 1.44 m · eldiven 0,25 m = 667 px | hands · torso | sayım jesti taşınır | kubbe okra 1 · uğultu bir kademe kalın · 0,904 g, iniş iki kat | — | ⛔8 · D78 | Kalan süreyi hesaplıyor. | ✅ |
| K18 | S06 | 3/4 · TERSLİK | çene kapalı, otomasyonun kolu geriliyor → çene aynı periyotta yeniden gerilmiş, kadrajın kenarında örtünün açık kenarı görünüyor | MUHATAP | **B** · 50mm · 1,2 m · h 1,15 m · CU · üç-çeyrek | 0.86 m · çene 0,30 m = 1333 px | hands | çene taşınır · açık kenar taşınır | kubbe okra 1 · uğultu bir kademe kalın · 0,904 g, iniş iki kat | — | D172 · D202 · ⚠️5 | Makinenin hiçbir şey öğrenmediğini görüyor. | ✅ |
| K19 | S06 | 4/4 · KARAR | vizörün ardında yüz, kaşlar düz → kaşlar çatılmış, çene sıkılmış, kask bir derece aşağı dönmüş ve orada kalmış | BEDEL | **D** · 85mm · 1,0 m · h 1,45 m · ECU · cepheden | 0.42 m · yüz 0,25 m = 2267 px | face | yüz tek klipte kadrajda | kubbe okra 1 · uğultu bir kademe kalın · 0,904 g, iniş iki kat | — | D167 · D202 · ⚠️10 | Sayıyı buldu ve ne yapacağını biliyor. | ✅ |
| K20 | S07 | 1/5 · BELİRİŞ | iki kollu makas ilk mandalın boynunda kapalı, ağırlık geride → birinci boyun kesilmiş, makas hâlâ kapalı | SINIR | **B** · 🔁 dönüş K18 · 50mm · 1,2 m · h 1,15 m · CU · üç-çeyrek | 0.86 m · çene 0,30 m = 1333 px | hands | makas girer · dokuz mandal sayacı açılır | kubbe okra 2 · uğultu iki kademe kalın · 0,904 g | — | D206 · D213 · ⚠️7 | Kendi işini geri almaya başlıyor. | ✅ |
| K21 | S07 | 2/5 · MÜCADELE | güverte kenarı boyunca dokuz mandal, üçü kesilmiş → beşi kesilmiş, teknisyen dördüncüden beşinciye geçmiş | SINIR | **C** · 35mm · 2,0 m · h 1,60 m · MS · üst açı 15° | 2.06 m · kesik uç 0,10 m = 187 px | hands · torso | dokuz mandal sayacı taşınır | kubbe okra 2 · uğultu iki kademe kalın · 0,904 g | — | D141 · D212 | Hızlı olmak istiyor ve hız yetmiyor. | ✅ |
| K22 | S07 | 3/5 · TERSLİK | makas yedinci boyunda kapalı → makas duraklamış, gerilimi tutuyor, boyun yarı kesilmiş | SINIR | **B** · 🔁 dönüş K20 · 50mm · 1,2 m · h 1,15 m · CU · üç-çeyrek | 0.86 m · çene 0,30 m = 1333 px | hands | makas taşınır | kubbe okra 2 · uğultu iki kademe kalın · 0,904 g | — | D169 · D206 · ⚠️7 | Yedincinin direnmesine hazırlıklı değil. | ✅ |
| K23 | S07 | 4/5 · KARAR | sekiz kesilmiş uç, dokuzuncu duruyor → dokuz kesilmiş uç sıralı ve sayılabilir, platform yukarı doğru hareketin içinde | BEDEL | **C** · 🔁 dönüş K21 · 35mm · 2,0 m · h 1,60 m · MS · üst açı 15° | 2.06 m · kesik uç 0,10 m = 187 px | hands · torso | dokuz kesik uç = FİNAL VURUŞ KANITI | kubbe okra 2 · uğultu iki kademe kalın · 0,904 g | — | ⛔6 · D141 · D212 | Kurduğu her şeyi kendi elleriyle geri aldı. | ✅ |
| K24 | S07 | 5/5 · BEDEL | son çene kesilmiş ve açık → çene açık kalmış, plaka kadrajdan kesintisiz geçiyor, geçiş sürüyor | BEDEL | **B** · 🔁 dönüş K22 · 50mm · 1,2 m · h 1,15 m · CU · üç-çeyrek | 0.86 m · çene 0,30 m = 1333 px | hands | çene çıkar · plaka geçmeye devam eder | kubbe okra 2 · uğultu iki kademe kalın · 0,904 g | — | ⛔7 · D210 · D211 | Haklı çıktı ve platform iniyor. | ✅ |
