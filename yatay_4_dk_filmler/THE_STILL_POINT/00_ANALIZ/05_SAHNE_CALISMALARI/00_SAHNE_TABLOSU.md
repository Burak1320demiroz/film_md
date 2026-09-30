# 🧮 THE_STILL_POINT — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır. Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> THE_STILL_POINT S<nn> <ROL>`
> ile damgalanır (`S<nn>_<ROL>.md`, tam şablon).
>
> Kapı: `prompt_kontrol.py` ㉚ — satır sayısı = bölüm dosyalarındaki sahne
> sayısı · beş rol dosyası var.

## Sütunlar — her hücre TEK satır, boş hücre yok ("—" yazılır)

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) | `03_SAHNE_SIRALAMASI` |
| **OLAY BAŞ → SON** | ne değişiyor: `<başta> → <sonda>`; klip içi değişim varsa `⚠️ARA` | çalışma şablonu 🎬 |
| **B5** | İSTEK / ENGEL / BEDEL / MUHATAP / AYRILIK — bu sahne hangi satırı taşıyor | `02_KONSEPT_VE_RISK` |
| **KURULUM** | harf + işaret (`B · dönüş S1`) · lens · mesafe · ölçek · açı tipi | `ACI_YAYI` §3-§4 |
| **OPTİK** | kadraj eni (m) · ana nesne (px) — ⛔ ≥100 px [D179]; sığmıyorsa `⛔` | `KILAVUZ` §5.2 hesabı |
| **IN FRAME** | face · hands · torso · legs · full body · back · none — promptun ilk satırı olur [㉖] | `IMAGE_VIDEO_PROMPT_TEMPLATES` V3 |
| **TAŞIYICI** | devamlılık: giren/çıkan/taşınan nesne + önceki/sonraki sahne | çalışma şablonu 👤 |
| **IŞIK · SES · FİZİK** | üçü tek hücrede `·` ile; palet/ses dokusu öncekiyle AYNI olamaz | ortam kartı · `KURGU_RITMI` §2 |
| **REPLİK** | `—` ya da `<saniye> · konuşan · İŞLEV · ağız okunuyor/okunmuyor` | `DIYALOG_SAHNESI` §2-§3 |
| **KİLİT / UYARI** | bu sahneye düşen kilit(ler) D-no ile + `04_UYARI_NOTLARI` satır no; en çok 3 | `01_QA_DERS_HASADI` |
| **İZLEYİCİ CÜMLESİ** | "bu figür ne istiyor" — seems/probably YASAK; ⭐VİRAL ise `YÜZ:` + `HAREKET:` | `OYUNCULUK_YAZIM` §1 · §3 |
| **KAPI** | ⬜ → ✅ satır tam ve optik tutuyor; ✅ olmadan o sahnenin promptu yazılmaz | — |

---

## 📋 TABLO

| S | OLAY BAŞ → SON | B5 | KURULUM | OPTİK (eni m · px) | IN FRAME | TAŞIYICI | IŞIK · SES · FİZİK | REPLİK | KİLİT / UYARI | İZLEYİCİ CÜMLESİ | KAPI |
|:--:|---|:--:|---|---|---|---|---|---|---|---|:--:|
| S00 | Anahtar yerinden kopar → uzaya doğru teğetsel fırlar | ENGEL | A · 35mm · 1.5m · MCU · dutch angle | 1.8m · 240px | hands | turuncu anahtar çıkış | Sert Güneş · Metal kopma çınlaması · 0.065g→0g | — | D34 · D210 · U1 | İzleyici bu fırlamanın ölümcül bir sapma olduğunu anlar | ✅ |
| S01 | Dönen halka ve kopan geçit görünür → merkez modül uzakta sabit kalır | ENGEL | B · 24mm · 80m · ELS · high angle | 120m · 350px | none | kopan köprü | Siyah-Altın · Düşük kabin uğultusu · 0.065g | — | D1 · D174 · U2 | İzleyici 100 metrelik ölümcül boşluğun aşılamaz olduğunu görür | ✅ |
| S02 | Nora eğri güverteye basar → adımlarıyla dengesini kurar | İSTEK | C · 50mm · 3.5m · MLS · eye level | 2.5m · 480px | full body, back | turuncu kol şeridi | Gri-Beyaz · Manyetik bot tıkırtısı · 0.065g | — | D139 · D167 · U2 | Nora dengesini sağlayarak kopuk kenara doğru ilerlemek ister | ✅ |
| S03 | Nora kopuk kenara yaklaşır → 100 metrelik uçuruma bakar | İSTEK | D · 35mm · 2.2m · MS · low angle | 2.0m · 380px | torso, hands | kopuk korkuluk | Siyah-Gümüş · Kask içi nefes sesi · 0.065g | — | D146 · D200 · U3 | Nora boşluğu doğrudan atlayarak geçip geçemeyeceğini tartar | ✅ |
| S04 | Nora telsizi çıkarır → boşluğa serbest bırakır | ENGEL | E · 50mm · 0.8m · CU · high angle | 0.9m · 320px | hands | telsiz cihazı | Beyaz-Koyu Gri · Mandal tıkırtısı · 0.065g | — | D174 · D175 · U2 | Nora cismin nasıl hareket edeceğini test etmek ister | ✅ |
| S05 | Telsiz boşlukta süzülür → hızla yana sapıp hedeften uzaklaşır | ENGEL | F · 24mm · 12m · LS · eye level | 15m · 180px | none | telsiz (savrulan) | Siyah-Altın · Sessiz boşluk · 0g | — | D157 · D174 · U2 | İzleyici doğrudan atlamanın hedefi ıskalatacağını kesin olarak görür | ✅ |
| S06 | Nora geriye döner → ray hattındaki bakım arabasını görür | İSTEK | G · 35mm · 3.0m · MLS · low angle | 2.8m · 420px | full body | araba rayı | Gri-Sarı · Bot sürtünmesi · 0.065g | — | D139 · D167 · U2 | Nora istasyonda kullanabileceği tek hareketli araca yönelir | ✅ |
| S07 | Nora göstergeye bakar → dönüş hızı ile araba hızını karşılaştırır | İSTEK | H · 85mm · 0.6m · CU · eye level | 0.7m · 360px | hands, torso | hız göstergesi | Koyu Gri-Turuncu · Soluk hızlanması · 0.065g | — | D157 · D169 · U2 | Nora dönüşü sıfırlamak için gereken 8 m/s hızı zihninde onaylar | ✅ |
| S08 | Nora arabaya biner → ayak kilitlerini geçirir | İSTEK | I · 35mm · 1.8m · MCU · low angle | 1.6m · 440px | legs, hands, torso | ayak kilit mandalı | Sarı-Gri · Mekanik kilit çarpması · 0.065g | — | D139 · D169 · U2 | Nora hızlanma sırasında arabadan fırlamamak için kendini sabitler | ✅ |
| S09 | Nora kumandayı iter → araba dönüşün tersine hızlanır | İSTEK | J · 24mm · 2.5m · MS · tracking | 3.2m · 400px | full body | kumanda kolu | Sarı-Siyah · Elektrik motor vızıltısı · 0.065g | — | D78 · D157 · U1 | Nora aracı istasyonun dönüş yönünün tam aksine doğru sürer | ✅ |
| S10 | Araba ivmelenir → istasyon iç duvarları bulanık geriye akar | İSTEK | K · 50mm · 0.9m · CU · eye level | 1.0m · 350px | hands, torso | hız kadranı (8 m/s) | Gri-Beyaz · Gövde rezonansı · 0.065g | — | D138 · D157 · U1 | Nora hız göstergesinin 8 m/s teğet hız sınırına ulaşmasını bekler | ✅ |
| S11 | Araba tam hıza ulaşır → karşıdaki merkez modül hareketsiz donar | İSTEK | L · 35mm · 2.8m · MLS · eye level | 3.0m · 360px | torso, back | merkez modül aksı | Siyah-Gümüş · Titreşim sönümlenmesi · 0g bağıl | — | D78 · D157 · U1 | Nora merkez eksene göre teğet hızını tamamen sıfırladığını anlar | ✅ |
| S12 | Nora kilidi söker → bakım arabasını iki elle boşluğa fırlatır | BEDEL | M · 24mm · 3.5m · LS · low angle | 4.5m · 340px | full body | bakım arabası (ayrılan) | Siyah-Altın · Ray ayrılma yankısı · 0.065g→0g | — | D202 · D206 · U3 | Nora geri dönüş ihtimalini tamamen yok ederek tek köprüsünü bırakır | ✅ |
| S13 | Nora havada tek başına kalır → halka arkasında devasa hızla döner | İSTEK | N · 35mm · 2.0m · MS · eye level | 2.2m · 400px | torso, hands | dönen halka kafesi | Sarı-Siyah · Saf kask içi soluk · 0g | — | D146 · D200 · U4 | Nora boşlukta asılı kalarak hedefe olan doğrusal hattını korur | ✅ |
| S14 | Nora vücudunu yay gibi gerer → kaçış kapsülüne hizalanır | İSTEK | O · 50mm · 1.6m · MCU · low angle | 1.5m · 450px | torso, legs | kapsül kenetlenme burnu | Koyu Gri-Gümüş · Kalp atışı ritmi · 0g | — | D169 · D206 · U3 | Nora son ve kusursuz itiş açısına vücudunu kilitler | ✅ |
| S15 | Nora kenardan ayaklarıyla iter → 2 m/s ile boşluğa fırlar | İSTEK | P · 24mm · 4.0m · MLS · wide | 5.0m · 320px | full body | itiş noktası kenarı | Siyah-Altın · Metalik itiş tınlaması · 0g | — | D139 · D198 · U3 | Nora vücudunu yüz metrelik karanlık boşluğa doğru fırlatır | ✅ |
| S16 | Nora karanlıkta süzülür → istasyon etrafında girdap gibi döner | İSTEK | Q · 35mm · 6.0m · LS · dutch angle | 8.0m · 260px | full body | uzay boşluğu | Siyah-Gümüş · Derin vakum sessizliği · 0g | — | D198 · D200 · U4 | Nora dönen istasyonun çekiminden etkilenmeden düz çizgide ilerler | ✅ |
| S17 | Nora boşluğun tam ortasındadır → arkada çılgınca dönen halka | İSTEK | R · 24mm · 15m · ELS · eye level | 20m · 140px | full body | ORISON halkası ve kapsül | Siyah-Altın-Gri · Mutlak uzay sessizliği · 0g | — | D141 · D200 · U4 | İzleyici durgun noktanın dinginliği ile dönüşün çılgınlığını kıyaslar | ✅ |
| S18 | Turuncu alet yanında süzülür → Satürn halkaları arkada parlar | İSTEK | S · 50mm · 1.8m · MS · low angle | 1.8m · 380px | hands, torso | turuncu anahtar | Altın-Siyah · Düzenli soluk sesi · 0g | — | D42 · D209 · U3 | Nora hedefe yaklaşırken süzülen aletle kader birliği hisseder | ✅ |
| S19 | Kaçış kapsülü kadrajı kaplar → Nora iki kolunu ileri uzatır | İSTEK | T · 35mm · 1.5m · MCU · eye level | 1.8m · 460px | hands, torso | kapsül tutunma demiri | Beyaz-Gümüş · Yaklaşan metal gövde · 0g | — | D174 · D198 · U3 | Nora çarpışma öncesi hızını sönümleyecek tutunma demirine odaklanır | ✅ |
| S20 | Nora demire çarpar → eldivenleriyle demiri sıkarak yakalar | İSTEK | U · 50mm · 0.8m · CU · high angle | 0.9m · 350px | hands | dış korkuluk demiri | Sarı-Gri · Metalik çarpışma tınlaması · 0g | — | D169 · D175 · U3 | Nora boşlukta savrulmadan kapsüle tutunmayı başarır | ✅ |
| S21 | Nora bacaklarını sarar → hava kilidi mandalını kavrar | İSTEK | V · 35mm · 1.8m · MS · low angle | 2.0m · 400px | full body | hava kilidi kolu | Koyu Gri-Sarı · Mekanik sürtünme sesi · 0g | — | D169 · D206 · U3 | Nora gövdesini sabitleyip içeriye giriş emniyetini sağlar | ✅ |
| S22 | Dış kapak açılır → Nora içeri süzülüp kapağı kilitler | İSTEK | W · 24mm · 1.6m · MCU · eye level | 1.8m · 420px | torso, legs | hava kilidi kapağı | Beyaz-Koyu Gri · Hava kilidi mühürlenme sesi · 0g | — | D1 · D213 · U1 | Nora kapsülün güvenli iç hacmine geçerek dış boşluğu mühürler | ✅ |
| S23 | Kapsül içinde anahtar sakince süzülür → istasyon pencereden uzaklaşır | İSTEK | X · 50mm · 2.0m · MS · eye level | 2.2m · 380px | hands, torso | süzülen turuncu anahtar | Beyaz-Altın · Kabin havalandırma uğultusu · 0g | — | D34 · D62 · D210 | Nora ve anahtar kurtulmuştur; korkunun içinde doğru hareket bulunmuştur | ✅ |
