# 🧮 THE_BRITTLE_EDGE — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> THE_BRITTLE_EDGE S<nn> <ROL>`
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
| S00 | Gergin çelik çekme kulağı → bükülmeden aniden ikiye ayrılır ⚠️ARA | ENGEL | A · 50mm · 1.0 m · CU · eye level | 0.7 m · 420 px | none | Çelik çekme kulağı ve kablo (giriş) → S01 | 15° alçak güneş · keskin metalik çatlama · 0,16g gevrek kırılma | — | D192 · D157 · U-1 | YÜZ: — · HAREKET: Çelik halka bükülmeden kopup geri fırlar | ✅ |
| S01 | Sarı araç geriye kayar → ön tekerlek son kaya çıkıntısına çarpıp durur ⚠️ARA | ENGEL | B · 24mm · 14.0 m · WS · high angle | 12.0 m · 320 px | full body | Sarı keşif aracı (S00'dan) → S02 | Sert gölge sınırı · regolit hışırtısı · 0,16g balistik toz | — | D198 · D174 · U-2 | YÜZ: — · HAREKET: Araç uçuruma düşmemek için son kaya çıkıntısına tutunur | ✅ |
| S02 | Kopan parça yerde durur → astronot eldivenle kaldırıp düz çatlağı inceler ⚠️ARA | ENGEL | C · 50mm · 0.6 m · ECU · low angle | 0.4 m · 550 px | hands | Kırık çelik kulak parçası (S00'dan) → S03 | Metal yüzey parıltısı · kask içi nefes · 0,16g hafifleyen parça | — | D78 · D157 · U-4 | Bu figür metalin neden bükülmeden koptuğunu teşhis etmek istiyor | ✅ |
| S03 | Kopan parça regolitte bırakılır → astronot sağlam alt şasi kirişine dokunur ⚠️ARA | ENGEL | D · 35mm · 2.5 m · MS · low angle | 2.2 m · 380 px | hands, torso, legs | Sarı aracın alt şasi kirişi → S04 | Şasi altı koyu gölge · eldiven alüminyum teması · 0,16g eğilme | — | D176 · D141 · U-12 | Karakter çekme kulağı yerine yükü taşıyacak sağlam kirişi arıyor | ✅ |
| S04 | Astronot terasta doğrulur → sırt çantasından turuncu kompozit sapanı açar ⚠️ARA | İSTEK | B · dönüş S01 · 24mm · 6.0 m · WS · eye level | 5.5 m · 280 px | full body | Kompozit kurtarma sapanı (çanta çıkışı) → S05 | Beyaz giysi turuncu kayış · kumaş fermuar açılma · 0,16g açılan kayış | — | D167 · D59 · U-2 | Karakter doğrudan çekme yerine yükü yayacak yeni aleti devreye sokuyor | ✅ |
| S05 | Astronot uçurum kenarında eğilir → sapanı ana kirişin altından geçirir ⚠️ARA | İSTEK | D · dönüş S03 · 35mm · 2.0 m · MS · low angle | 1.8 m · 360 px | hands, torso, legs | Kompozit sapan şasi altına giriş → S06 | Şasi kenarı parlaması · kayış sürtünme titreşimi · 0,16g diz çökme | — | D169 · D202 · U-2 | YÜZ: — · HAREKET: Karakter sapanı uçurum eşiğinde kirişten geçiriyor | ✅ |
| S06 | Sapanın açık iki ucu → çelik karabinaya geçirilip kilit somunu kapanır ⚠️ARA | İSTEK | C · dönüş S02 · 50mm · 0.8 m · CU · eye level | 0.6 m · 480 px | hands | Kilitlenen karabina ve sapan uçları → S07 | Koyu zemin çelik kilit · mekanik klik sesi · 0,16g kayış gerilimi | — | D172 · D141 · U-10 | Karakter yükü şasiye eşit dağıtan bağlantı kilidini kuruyor | ✅ |
| S07 | Vinç kablosu serbest durur → astronot kancayı sapan karabinasına bağlar ⚠️ARA | İSTEK | C · küme S06 · 50mm · 0.8 m · CU · eye level | 0.8 m · 480 px | hands | Vinç kablosu kancası ve karabina bağı → S08 | 15° alçak güneş · kancanın karabinaya oturma tıkırtısı · 0,16g gerilen kablo | — | D174 · D209 · U-10 | Karakter vinç kancasını karabinaya kilitleyip çekişi başlatmak istiyor | ✅ |
| S08 | Ön tekerlek kayaya dayalıdır → vinç gerilimiyle çıkıntıdan ayrılıp sarkar ⚠️ARA | BEDEL | E · 28mm · 3.5 m · MS · dramatic low | 3.0 m · 340 px | full body, legs | Kaya çıkıntısını terk eden ön tekerlek → S09 | Kaya kenarı gölge sınırı · taş sürtünmesi ve sessizlik · 0,16g temas kaybı | — | D206 · D202 · U-2 | YÜZ: — · HAREKET: Karakter son desteğin kopuşuna kaskını kilitleyerek bakıyor | ✅ |
| S09 | Araç uçurumda askıda durur → sapan tam yükü sırtlar, araç dengede kalır ⚠️ARA | MUHATAP | E · dönüş S08 (KÜME) · 28mm · 3.5 m · MS · dramatic low | 3.0 m · 340 px | full body, legs | Uçurum üstünde askıda sarı araç → S10 | Uçurum siyahlığı · lif gerilme iniltisi · 0,16g asılı kütle | — | D179 · D198 · U-2 | YÜZ: — · HAREKET: Yeni bağlantının koca kütleyi tutup tutmayacağı sınanıyor | ✅ |
| S10 | Araç uçurum kenarından yükselir → dört tekerlek teras zeminine tam oturur ⚠️ARA | İSTEK | B · dönüş S07 · 24mm · 10.0 m · WS · high angle | 9.0 m · 310 px | full body | Güvenli terasa varan sarı araç → S11 | Açık teras aydınlığı · zemine oturma gümbürtüsü · 0,16g regolit çökmesi | — | D210 · D200 · U-1 | Karakter aracın dört tekerlekle güvenli zemine oturmasını sağlıyor | ✅ |
| S11 | Astronot aracın yanında durur → eldeki parçaya, sonra sağlam şasiye bakar ⚠️ARA | İSTEK | A · dönüş S00 · 40mm · 2.2 m · MS/CU · eye level | 2.0 m · 390 px | torso, hands | Kırık çelik parça ve kurtarılmış araç (kapanış) | Sakin krater manzarası · dingin nefes sesi · 0,16g dengeli duruş | — | D62 · D210 · U-3 | YÜZ: — · HAREKET: Karakter doğru yöntemin hayat kurtardığını mühürlüyor | ✅ |
