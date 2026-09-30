# 🧮 THE_INWARD_FALL — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> THE_INWARD_FALL S<nn> <ROL>`
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
| K01 | S01 | 1/3 · KURULUM | Çelik pim elden kayar → pim 1.4 m düşüşte 0.6 m yana saparak tırabzan ayağına çarpar | İSTEK | A · 35mm · LS · göz hizası | 3.5 m · 220 px | hands, legs | çelik pim (elde) | Soğuk çelik gri, axial skimming ışık · vakum bas tıkırtısı + 120 Hz inilti · 0.4g dönme yerçekimi | — | D157 · D192 · U-1 | Düşen parçayı tutmak istiyor ama parça beklenmedik şekilde yana fırlıyor | ✅ |
| K02 | S01 | 2/3 · EYLEM | Teknisyen yana devrilen pime uzanır → pimi yakalayamazken gövdesi geriye itilir | İSTEK | B · dönüş K01 · 85mm · CU · solucan bakışı | 0.8 m · 360 px | hands, torso | çelik pim (zeminde) | Soğuk çelik gri, axial skimming ışık · vakum bas tıkırtısı + 120 Hz inilti · 0.4g dönme yerçekimi | — | D200 · D206 · U-1 | Kayarak kaçan parçaya uzanmaya çalışıyor | ✅ |
| K03 | S01 | 3/3 · TEPKİ | Teknisyen kaskını kaldırır → vizörde hızlanan istasyon gölgeleri ve alarm parlar | İSTEK | C · 50mm · MCU · yüksek açı | 0.9 m · 420 px | face, torso | vizör alarm yansıması | Soğuk çelik gri, axial skimming ışık · vakum bas tıkırtısı + 120 Hz inilti · 0.4g dönme yerçekimi | — | D208 · D211 · U-1 | YÜZ: Şokla büyüyen göz bebekleri · HAREKET: Hızlanan gölgelerin kaskta geçişi | ✅ |
| K04 | S02 | 1/4 · BELİRİŞ | Teknisyen servis rayına döner → merdiven sütununa doğru ağır adımlarla bakar | ENGEL | D · 40mm · MLS · alt açı | 2.8 m · 310 px | full body | tırabzan rayı | Titanyum gri ve sarı reflektör, sert yan gölge · metal esneme gıcırtısı + 180 Hz rezonans · 1.0g artan yerçekimi | — | D200 · D209 · U-2 | Artan ağırlık altında servis koridorunun çıkışına ulaşmak istiyor | ✅ |
| K05 | S02 | 2/4 · MÜCADELE | Teknisyen ilk adımı atar → manyetik botu raydan güçlükle söküp kafese ilerler | ENGEL | B · dönüş K02 · 85mm · CU · solucan bakışı | 0.7 m · 380 px | legs | manyetik botlar | Titanyum gri ve sarı reflektör, sert yan gölge · metal esneme gıcırtısı + 180 Hz rezonans · 1.0g artan yerçekimi | — | D200 · D206 · U-2 | Ağırlaşan adımlarını raya yapışan manyetik botlardan tek tek söküyor | ✅ |
| K06 | S02 | 3/4 · TERSLİK | Ray sarsıntısı başlar → emniyet mandalı sıyrılırken teknisyen tırabzana tutunur | ENGEL | D · dönüş K04 · 40mm · MLS · alt açı | 2.6 m · 290 px | torso, legs | emniyet mandalı | Titanyum gri ve sarı reflektör, sert yan gölge · metal esneme gıcırtısı + 180 Hz rezonans · 1.0g artan yerçekimi | — | D207 · D213 · U-2 | Sarsıntıda savrulmamak için tırabzana tüm gücüyle asılıyor | ✅ |
| K07 | S02 | 4/4 · KARAR | Teknisyen tırabzandan toparlanır → iki eliyle kafes merdivenine kenetlenir | ENGEL | C · dönüş K03 · 50mm · MCU · yüksek açı | 1.0 m · 400 px | face, torso | kafes merdiven | Titanyum gri ve sarı reflektör, sert yan gölge · metal esneme gıcırtısı + 180 Hz rezonans · 1.0g artan yerçekimi | — | D202 · D208 · U-2 | Yukarıdaki çıkış aksına tırmanmak üzere merdiven kafesine kenetleniyor | ✅ |
| K08 | S03 | 1/5 · BELİRİŞ | Teknisyen kafese tutunur → başını kaldırıp yukarıdaki merkez kovanına bakar | ENGEL | E · 28mm · LS · kuşbakışı dikey | 4.2 m · 180 px | back, torso | merkez kovanı (uzakta) | Derin uzay siyahı ve gümüş kafes gölgesi · kask içi nefes + kafes rezonansı · 0.8g azalan g + Coriolis yan torku | — | D174 · D209 · U-3 | Merdivenin sonundaki uzaktaki eksen kovanını hedef belirliyor | ✅ |
| K09 | S03 | 2/5 · MÜCADELE | Teknisyen ilk basamakları tırmanır → Coriolis kuvveti gövdeyi yana iter | ENGEL | F · 65mm · CU · eğik açı | 1.1 m · 350 px | full body | tırabzan basamakları | Derin uzay siyahı ve gümüş kafes gölgesi · kask içi nefes + kafes rezonansı · 0.8g azalan g + Coriolis yan torku | — | D200 · D206 · U-3 | Kendini yana savuran kuvvete rağmen basamakları tek tek tırmanıyor | ✅ |
| K10 | S03 | 3/5 · TERSLİK | Yan savrulma artar → teknisyenin sağ omzu tırabzana çarpar ve çanta uçar | ENGEL | E · dönüş K08 · 35mm · MS · yüksek açı | 2.0 m · 320 px | torso, hands | kopan alet çantası | Derin uzay siyahı ve gümüş kafes gölgesi · kask içi nefes + kafes rezonansı · 0.8g azalan g + Coriolis yan torku | — | D207 · D213 · U-3 | Omuz darbesine ve kaybolan alet çantasına rağmen basamağı bırakmıyor | ✅ |
| K11 | S03 | 4/5 · KARAR | Teknisyen basamağa yapışır → gövdesini 15 derece ters yatırarak torku dengeler | ENGEL | F · dönüş K09 · 65mm · CU · eğik açı | 1.2 m · 360 px | hands, torso | tırabzan borusu | Derin uzay siyahı ve gümüş kafes gölgesi · kask içi nefes + kafes rezonansı · 0.8g azalan g + Coriolis yan torku | — | D202 · D206 · U-3 | Gövdesini eğerek dengesini kurup tırmanışı sürdürmek istiyor | ✅ |
| K12 | S03 | 5/5 · BEDEL | Teknisyen çeyrek yüksekliğe ulaşır → uzaklaşan jant zeminine bakıp kafese tutunur | ENGEL | C · dönüş K07 · 50mm · MCU · yüksek açı | 1.0 m · 390 px | face, torso | emniyet kafesi | Derin uzay siyahı ve gümüş kafes gölgesi · kask içi nefes + kafes rezonansı · 0.8g azalan g + Coriolis yan torku | — | D208 · D209 · U-3 | Zeminden uzaklaştığını görerek nefesini toparlamaya çalışıyor | ✅ |
| K13 | S04 | 1/3 · KURULUM | Teknisyen r=30m bölgesine bakar → dönme devrinin hızlandığını fark eder | ENGEL | G · 35mm · LS · göz hizası | 3.8 m · 260 px | full body | merdiven orta sütunu | Endüstriyel beyaz ve aşınmış sarı · telsiz telemetri vızıltısı + hafifleyen metal · 0.5g düşük g + zirve Coriolis | — | D174 · D200 · U-4 | Hafifleyen ağırlığına rağmen yana savrulmanın büyüdüğünü hissediyor | ✅ |
| K14 | S04 | 2/3 · EYLEM | Teknisyen hafifleyen bacaklarıyla atılır → her hamlede yana savrulup basamağa çarpar | ENGEL | F · dönüş K11 · 65mm · CU · eğik açı | 1.2 m · 340 px | full body | tırabzan basamağı | Endüstriyel beyaz ve aşınmış sarı · telsiz telemetri vızıltısı + hafifleyen metal · 0.5g düşük g + zirve Coriolis | — | D206 · D207 · U-4 | Her yukarı itişte tırabzandan kopmamak için direniyor | ✅ |
| K15 | S04 | 3/3 · TEPKİ | Teknisyen basamağı yakalar → vizöründe yaklaşan tahliye kapağı parlar | ENGEL | C · dönüş K12 · 50mm · MCU · yüksek açı | 0.9 m · 410 px | face, hands | kovan kapak silueti | Endüstriyel beyaz ve aşınmış sarı · telsiz telemetri vızıltısı + hafifleyen metal · 0.5g düşük g + zirve Coriolis | — | D208 · D211 · U-4 | Tahliye kapağının siluetini görerek son gücünü topluyor | ✅ |
| K16 | S05 | 1/5 · BELİRİŞ | Merdiven sonuna varılır → kafes biterken son serbest açıklık görünür | BEDEL | G · dönüş K13 · 40mm · MLS · göz hizası | 3.0 m · 280 px | full body | serbest boşluk | Mat grafit ve reflektif turuncu · gerilen çelik tel çınlaması + telemetri alarmı · 0.2g neredeyse sıfır-g + kordon torku | — | D174 · D209 · U-5 | Merdivenin bittiği serbest açıklığı aşmak istiyor | ✅ |
| K17 | S05 | 2/5 · MÜCADELE | Teknisyen son basamakta durur → emniyet kordonu kafes halkasına sıkışıp kilitlenir | BEDEL | F · dönüş K14 · 85mm · CU · eğik açı | 0.8 m · 360 px | torso, hands | sıkışan emniyet kordonu | Mat grafit ve reflektif turuncu · gerilen çelik tel çınlaması + telemetri alarmı · 0.2g neredeyse sıfır-g + kordon torku | — | D215 · D213 · U-5 | Sıkışan kordonun onu aşağı çekmesine karşı koyuyor | ✅ |
| K18 | S05 | 3/5 · TERSLİK | Kordon gerilir → merkezkaç ve kordon bedeni iki zıt yöne çeker | BEDEL | E · dönüş K10 · 35mm · MS · yüksek açı | 2.2 m · 300 px | full body | gerilen çelik tel | Mat grafit ve reflektif turuncu · gerilen çelik tel çınlaması + telemetri alarmı · 0.2g neredeyse sıfır-g + kordon torku | — | D200 · D206 · U-5 | Zıt kuvvetlerin bedenini yırtma gerilimine direniyor | ✅ |
| K19 | S05 | 4/5 · KARAR | Teknisyen kesiciyi çıkarır → kesici aparat sıkışan örgülü tele dayanır | BEDEL | B · dönüş K05 · 100mm · ECU · solucan bakışı | 0.4 m · 450 px | hands | mekanik kesici aparat | Mat grafit ve reflektif turuncu · gerilen çelik tel çınlaması + telemetri alarmı · 0.2g neredeyse sıfır-g + kordon torku | — | D213 · D215 · U-5 | Tutsak kaldığı kordonu keserek kurtulmaya karar veriyor | ✅ |
| K20 | S05 | 5/5 · BEDEL | Teknisyen kordonu keser → manyetik botlar rayda bırakılarak sıfır-g boşluğuna fırlar | BEDEL | G · dönüş K16 · 35mm · MLS · göz hizası | 3.2 m · 290 px | full body | rayda kalan botlar | Mat grafit ve reflektif turuncu · gerilen çelik tel çınlaması + telemetri alarmı · 0.2g neredeyse sıfır-g + kordon torku | — | D206 · D213 · U-5 | Botlarını ve kordonunu feda ederek kendini merkeze fırlatıyor | ✅ |
| K21 | S06 | 1/4 · BELİRİŞ | Teknisyen boşlukta uçar → iki eliyle merkez kovanı tutamağını yakalar | MUHATAP | H · 50mm · MCU · alt açı | 1.1 m · 440 px | face, hands | kovan tutamağı | Sonsuz uzay siyahı ve altın vizör parlaması · mutlak sessizlik + pnömatik tıslama · 0.0g tam ağırlıksızlık | — | D202 · D208 · U-6 | YÜZ: Vizörde çılgınca dönen jantın altın yansıması · HAREKET: İki elle kovan tutamağına kenetleniş | ✅ |
| K22 | S06 | 2/4 · MÜCADELE | Teknisyen kovana kenetlenir → sabit merkezden çevresinde dönen jantı izler | MUHATAP | G · dönüş K20 · 24mm · LS · göz hizası | 4.5 m · 240 px | back, torso | dönen dış jant | Sonsuz uzay siyahı ve altın vizör parlaması · mutlak sessizlik + pnömatik tıslama · 0.0g tam ağırlıksızlık | — | D209 · D210 · U-6 | Sıfır-g ekseninden dönen felaketi dehşetle izliyor | ✅ |
| K23 | S06 | 3/4 · TERSLİK | Teknisyen kovan kapağını çevirir → pnömatik fırlatma pimi kilitlenip patlar | MUHATAP | H · dönüş K21 · 50mm · MCU · alt açı | 1.0 m · 380 px | hands, torso | tahliye kapağı volanı | Sonsuz uzay siyahı ve altın vizör parlaması · mutlak sessizlik + pnömatik tıslama · 0.0g tam ağırlıksızlık | — | D213 · D215 · U-6 | Kapsülü fırlatmak için pnömatik pimi ateşliyor | ✅ |
| K24 | S06 | 4/4 · KARAR | Tahliye kapsülü merkezden ayrılır → dönen jant geride kalarak uzayda küçülür | MUHATAP | J · 20mm · ELS · göz hizası | 12.0 m · 210 px | none | tahliye kapsülü | Sonsuz uzay siyahı ve altın vizör parlaması · mutlak sessizlik + pnömatik tıslama · 0.0g tam ağırlıksızlık | — | D210 · D214 · U-6 | Dönen tuzaktan uzay boşluğuna doğru kurtuluyor | ✅ |
