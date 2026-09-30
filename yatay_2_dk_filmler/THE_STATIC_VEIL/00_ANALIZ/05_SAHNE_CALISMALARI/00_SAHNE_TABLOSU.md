# 🧮 THE_STATIC_VEIL — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> THE_STATIC_VEIL S<nn> <ROL>`
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

---

## 📋 TABLO

| S | OLAY BAŞ → SON | B5 | KURULUM | OPTİK (eni m · px) | IN FRAME | TAŞIYICI | IŞIK · SES · FİZİK | REPLİK | KİLİT / UYARI | İZLEYİCİ CÜMLESİ | KAPI |
|:--:|---|:--:|---|---|---|---|---|---|---|---|:--:|
| S00 | Zemin sakin → Toz taneleri dikine parlak iplikler gibi yükselir | MUHATAP | A · 24mm · 12m · EWS · Düşük Açı | 16m · 240px | none | Toz iplikleri in (S00) / vizör (S01) | Zifiri gölge + sert tepe güneş · Mutlak sessizlik + zemin titreşimi · 0.16g vakum | — | D200 · D211 · U-1 | YÜZ: none · HAREKET: havada asılı tozların doğurduğu merak | ✅ |
| S01 | Adım atma → Havalanan toz altın vizöre yapışıp bulanıklaştırır | ENGEL | B · 50mm · 3.5m · MS · Göz Hizası (arkadan 3/4) | 3.2m · 480px | hands, torso, full body, back | Vizör altın kaplama in (S00) / matlaşma (S02) | Sert düşük güneş · Ritmik bot adım tınısı · 0.16g yavaş adım | — | D139 · D208 · U-2 | YÜZ: none · HAREKET: hedefe yürürken görüşün bozulmasını fark etme | ✅ |
| S02 | Eldiven vizöre uzanır → Silme hareketi camı zımparalar ve matlaştırır | ENGEL | C · 85mm · 1.2m · CU · Hafif Üst Açı | 0.9m · 720px | hands, torso, face | Eldiven in (S01) / ray arayışı (S03) | Dolaylı kask yansıması · Eldiven-cam sürtünme gıcırtısı · 0.16g vakum | — | D146 · D175 · U-2 | YÜZ: altın vizör matlaşması · HAREKET: camı silmeye çalışırken körleşme | ✅ |
| S03 | Duraksama → Eldiven parmak uçlarıyla metal kılavuz rayını bulur | İSTEK | C · 85mm · 1.2m · CU · Hafif Üst Açı (KÜME 1 devam) | 0.9m · 720px | hands, torso, face | Kılavuz rayı in (S02) / pilon (S04) | Sert teğet ışık · Eldivenin metale mekanik tıkırtısı · 0.16g temkinli duruş | — | D169 · D174 · U-3 | he wants to find the guide rail to not get lost | ✅ |
| S04 | Pilona varış → Fener yuvası sensörünün tozla kaplandığını görür | ENGEL | D · 50mm · 2.0m · MCU · Göz Hizası (yandan) | 1.8m · 540px | hands, torso | Çelik pilon in (S03) / fener modülü (S05) | Sert kontrastlı silüet · Botun pilon tabanına çarpması · 0.16g vakum | — | D192 · D209 · U-4 | he wants to reach the beacon mounting safely | ✅ |
| S05 | Feneri sokete itme → Tırnakların tozla sıkışıp kalması | ENGEL | E · 85mm · 0.6m · ECU · Detay / Üst Açı | 0.4m · 800px | hands | Fener montajı in (S04) / topraklama kablosu (S06) | Fener kenarından yansıyan sert ışık · Metal sıkışma gerilim tınısı · 0.16g vakum | — | D179 · D213 · U-4 | he wants the beacon to click into place | ✅ |
| S06 | Diz çökme → Göğüs plakasından bakır topraklama kablosunu çözme | İSTEK | D · dönüş S04 · 50mm · 2.0m · MCU · Göz Hizası (yandan) | 1.8m · 540px | hands, torso | Bakır kablo in (S05) / sürtme (S07) | Göğüs LED yansıması · Klips açılma çıtırtısı · 0.16g stabil çöküş | — | D139 · D202 · U-5 | he wants to clear the static charge with grounding | ✅ |
| S07 | Kablo ucunu şaseye sürtme → Zayıf yetersiz mikro kıvılcım | ENGEL | C · dönüş S03 · 85mm · 1.2m · CU · Hafif Üst Açı | 0.9m · 720px | hands, torso, face | Bakır uç in (S06) / kask bataryası (S08) | Anlık zayıf mor kıvılcım parıltısı · İnce statik çıtırtı · 0.16g vakum | — | D192 · D212 · U-5 | he wants the static charge to drain completely | ✅ |
| S08 | Elin kask bataryasına gitmesi → Tereddüt ve sökme kararı | BEDEL | C · dönüş S07 · 85mm · 1.2m · CU · Hafif Üst Açı (KÜME 2 devam) | 0.9m · 720px | hands, torso, face | Harici batarya modülü in (S07) / çarpma (S09) | Göğüs panelinden süzülen soluk ışık · Derin kask içi nefes veriş · 0.16g duraksama | — | D202 · D206 · U-3 | YÜZ: mat vizör arkasında tereddüt · HAREKET: bataryayı sökerken titreyen el | ✅ |
| S09 | Bataryayı pilona vurma → Güçlü beyaz-mavi ark, toz fırlaması, ekranların sönüşü | BEDEL | D · dönüş S06 · 50mm · 2.0m · MCU · Göz Hizası (yandan) | 1.8m · 540px | hands, torso, face | Şase kıvılcımı in (S08) / temiz delik (S10) | 0.3s beyaz-mavi elektriksel ark parlaması · Sert çarpma + gösterge bipi kesilmesi · 0.16g vakum | — | D192 · D206 · D213 · U-1 | YÜZ: anlık parlayan ark · HAREKET: darbeyi vurup ekranlar kararınca geriye yaslanma | ✅ |
| S10 | Temiz görüş deliğinden bakma → Feneri yerine tam oturtup çevirme | İSTEK | E · 85mm · 0.6m · ECU · Detay / Üst Açı | 0.4m · 800px | hands | Oturtulan montaj tırnağı in (S09) / yanan fener (S11) | Metalden tek nokta yansıma · Mekanik montaj oturma klik sesi · 0.16g vakum | — | D179 · D213 · U-4 | he wants the latch to seat permanently | ✅ |
| S11 | Fenerin yanışı → Astronotun kararmış kaskla karanlığa doğru dönüşü | MUHATAP | A · dönüş S00 · 24mm · 12m · EWS · Düşük Açı | 16m · 240px | full body, back | Yanan optik fener in (S10) / son kare | Yanan amber fener ışığı ve karanlık krater · Uzaklaşan bot zemin titreşimi · 0.16g yavaş yürüyüş | — | D210 · D211 · U-5 | YÜZ: none · HAREKET: bedeli ödemiş olarak kör göstergelerle karanlıkta geri dönüş | ✅ |
