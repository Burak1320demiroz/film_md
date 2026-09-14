# 🧾 THE_LOCKED_PULSE — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu (120/120 ✅ · 13.09.2026).
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 205 ders ve
> 58 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.
>
> ⚠️ Sahne numaraları `03_SAHNE_SIRALAMASI.md`'de kesinleşen iskelete göredir
> (S0 hook · S1-S12 BOLUM_1 · S13-S24 BOLUM_2 · doruk S20 · bedel S22 · kafiye S0↔S24).

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D1 · D68 | klip içi kesme, sahne içi montaj | 25 sahne = 25 klip; her video promptu "No cuts." ile biter; küme klipleri "continues the previous clip from its exact last frame" | 25/25 |
| D3 · D29 | bloom / glow / lens flare | kırmızı alarm lambası "a red lamp above the bay, its light on the panels, no halo, no bloom"; 'glowing' hiç yazılmaz, 'lamp light / cast' | 24/25 iç sahne |
| D5 · D37 · D57 | kask/eldiven durumu sahneler arasında açılıp kapandı | HELMET STATE SCHEDULE: kask KAPALI 25/25 · SAĞ ELDİVEN: giyili S0-S21 · kolda değil, KOLLARDA seated S22-S24 (tek durum değişimi, sınırda) | 25/25 · S22 |
| D12 · D44 | düşük g'de yavaş çekim hissi, kadans yok | "real time, normal human pace"; adım/nefes KADANS sayısı: S5 yürüyüş 10 s'de 8 adım · S7 7 adım (ağırlaşma) | S5 · S6 · S21 |
| D13 · D50 · D78 | ekran metni sızması, sayaç okunmadı | sayaç METİNSİZ ve sayılabilir: 7 yuvalı lamba dizisi (6 yanık + 1 sönük → S24'te 7 yanık); alarm periyodu; kayış salınım süresi — sayacın iki ucu tek karede (lambalar + kayış aynı kadrajda A ve C'de) | S0 · S2 · S10 · S22-S24 |
| D16 · ADAY-16 | vizör ardında yüz değişimi (COUNTED_TURN S12/S14 erkek↔kadın) | yüz cümlesi + "a man" + giysi bloğu 50 promptta kelimesi kelimesine; MCU/CU'da da kısaltılmaz | 25/25 |
| D20 · D69 · D140 | klon / ikinci insan (loş iç mekân sıcak noktası, Unbroken City 0:40) | "exactly one human figure" + yansıtıcı yüzey 0 (paneller mat) + biniş/iniş/kapı geçişi 0 kare; kriyo kapsülleri kadrajda YOK (yalnız lambaları) | 25/25 |
| D23 · D149 · D198 · D200 | aynı karede iki yerçekimi / 0 g rijitlik | hub 0 g sahnesi YOK (malzeme azaltıldı); tek dış sahne (S13) insansız; iç sahnelerde tek g, MONOTONİK ↑ (0,25 → 1,00 g) | S13 · NOVUM DURUMU sütunu |
| D32 · D58 · D138 | yapı oranı kaydı, ölçü nesnenin üstüne basıldı ("11 metres") | metre yalnız SPEC/PLAN fizik defterinde; promptta GÖVDE BOYU ("the corridor a little over one body-length wide", "a port collar the width of his wrist ring"); rakam+birim nesneye bitişik YAZILMAZ | 25/25 |
| D34 · D45 · D155 | özel ad / köşeli etiket / "PHASE 1" ekrana basıldı | 'Lars' düşer → "the engineer"; `[CHARACTER BIBLE]` etiketi gövdede yok; PHASE/EVA/STATE büyük harf etiketi yok; kamera düz cümle | 25/25 |
| D35 · D82 · D99 | telsiz repliği ekrandaki ağza yapıştı; sayı insan ağzından | 6 replik hepsi MACHINE (tavan hoparlörü, düz sentetik); sayı YALNIZ makine söyler; her replikli promptta "lips closed behind the visor, no mouth movement"; sessiz sahnenin AUDIO bloğu konuşmanın yokluğunu sayar | S1 · S6 · S9 · S12 · S13 · S18 |
| D36 · D39 · D143 · D154 | jet/duman girdaplandı, sıvı gibi aktı | soğutucu jeti: "a thin white vapour jet, straight as a ruler, a hand-span long, from the open port collar" — swirl/billow yok; yalnız S3 · S8 (incelmiş) · S10 (biter); tekrar eden olay = varlık → RO referans paneli | S3 · S8 · S10 |
| D40 · ADAY-7/10 | altyazı / ekran metni araçtan | NEGATIVE'de "no subtitles, no captions, no on-screen text"; replikli sahne SESSİZ üretilir, ses post'ta | S1 · S6 · S9 · S12 · S13 · S18 |
| D42 · D147 · D84 | aşınma/kir takvimi sahneler arası kırıldı | kir GLOBAL ve sabit: "an even matte dusting of grey grit" — takvim yok, değişmez | 25/25 |
| D47 · D48 · D193 | ışık durumu geri sardı; takvim ölçülmedi | LIGHT STATE her sahnede numarayla: alarm periyodu S0-S5 2,0 s · S6-S12 1,5 s · S14-S24 1,0 s (yalnız sınırda değişir, ↑ monotonik); SPEC'e IŞIK TAKVİMİ | 25/25 · S5\|S6 · S13\|S14 |
| D49 | novum durumu sahneden sahneye izlenmedi | sahne haritasına NOVUM DURUMU sütunu: RPM · g · kayış periyodu · yıldız süpürmesi (monotonik) | 03_SIRALAMA §2 |
| D55 | Bible yok → kostüm 1/10 | Character Bible tek İngilizce blok (yüz + giysi + kimlik), World Bible (pencere parçası), Lighting Bible 6 satır, Prop kartı (vana çarkı · port yakası · fren vanası · kayış · lamba dizisi) | PLAN |
| D59 · D153 | pozitif tarifte hang/float/suspend/hover → süzüldü; 'fabric/cloth' dalgalandı | kayış "a stiff woven webbing strap clipped at the top, it swings as one straight line"; 'hangs/dangles/floats' YOK; 'fabric/cloth' 0 geçiş | S0 · S2 · S7 · S21 · S24 |
| D62 · D72 · D141 · D182 | final kurguda yok / kart / vuruş kanıtı sayılamadı | FİNAL VURUŞ KANITI: 249,0 s'de tam 7 yanık lamba · 1 eldiven port yakasında · 0 el çarkta (İngilizce adıyla SPEC'e); S24 KESİLEMEZ; kart 0,0 s | S24 · SPEC B |
| D67 · D123 · D128 · D175 | yasak cümlesi üretildi; "through the glove" çıplak deri üretti; crush/injury | bilek "the right wrist ring seats into the port collar; the collar latch closes over the ring with a click; the glove stays seated" — crush/injury/pain/trapped YOK; "never/no + fiil" yasak cümlesi YOK; anatomi eldiven yüzeyinde ("the glove's ribbed segments tighten"); çıplak deri negatifi ÜÇ BÖLGE tek satırda (S22-S24'te sağ el ÇIPLAK planlı → o üç sahnede negatif "no bare skin above the collar or at the left wrist" olarak DARALTILIR) | S10-S12 · S14-S15 · S22-S24 |
| D73 · D76 · D157 · D172 | taşıyıcı okunmadı; tek kare testi başka nesneyle | NOVUM TAŞIYICI = düşen alet × bırakma → yana iner (kadrajın ≥1/10'u, rakip olay yok, tek klip); TEK KARE cümlesi "wrench" adıyla; salınan kayış ikinci taşıyıcı; kural ≥3 sahne ≥2 nesne (S2 anahtar · S15 levye · S0/S24 kayış · S1/S18 yıldız) | S2 · S15 · S0 · S24 · S1 · S18 |
| D74 · D144 | üretim kapısı yazıldı, koşulmadı, sahneler üretildi | URETIM_DEFTERI boş doğar ama her kapının KABUL / RET / YABANCI GÖZ / SONUÇ alanı hazır; İPTAL KAPISI S2 (anahtar yana inmiyorsa film üretilmez) | PLAN §ÜRETİM · S2 |
| D79 · D95 · D139 · D146 · ADAY-2 | vizör kubbe/aynalı; sırt ünitesi bible'a rağmen geldi; biçim kilidi metinle tutulmadı | kask: "a single flat front pane inside a thick dark rim, the rim visible at every head angle"; sırt "one continuous ribbed surface from collar to hip, closed and smooth"; REFERANS PAKETİ RK1 (kask/vizör/arka) KAPI 0 — panel onaysız sahne üretilmez | 25/25 · RK1 |
| D83 · D180 | ambiyans yatağı kesmede öldü; sessizlik modelden istendi | fan uğultusu cümlesi 24 iç promptta AYNI; kurguda tek yatak; doruk sessizliği KURGUDA hard mute (203,0-205,0 s) — video promptundan istenmez | 24/25 · S20 · SPEC E |
| D89 · D196 | ikinci mühür açıldı; eldiven-kol teması belirsiz | TEK MÜHÜR: film boyu dokunulan tek mühür SAĞ BİLEK HALKASI; kask 25/25 kapalı; S22'de "exactly one seal opened: the right wrist ring" | S12 · S22 |
| D90 · D127 | milimetrik olay / ivme promptla gelmedi (0,15 m/s süzülme) | ivme/derece yazılmaz; ölçen kenar SÜREYLE: "the wrench is on the floor before the hand closes, a palm's width to the left of where it left the glove"; yıldız "a third of a turn / two thirds of a turn during the shot"; kayış "one full swing in four seconds / in two seconds" | S2 · S15 · S1 · S18 · S0 · S24 |
| D100 · D101 · D122 | sabit ızgara gerekçesi yok; replik saniyesi elle | SPEC'e "TARGET ASL 10,0 s — sabit ızgara, gerekçe: lockoff + I2V"; replik(S_n) = 9 + (n−1)×10 + ofset formülle | SPEC A · replik tablosu |
| D104 · D174 | yön koordinatla yazıldı; kamera hedefte değil | yön KADRAJDAKİ NESNEYLE ("toward the valve bay on the right"); bilek/vana insertlerinde kamera HEDEFTE (yaka), mühendisin eli kameraya gelir; ekran-uzayı sol/sağ, dünya-uzayı yön 0 | S3 · S8 · S12 · S14 · S20 |
| D117 · D129 · D165 · D204 | SPEC kabuk; mod V; yedi makine çapası kayıp | QA_SPEC yedi çapa DOLU (GRID · CLIP COUNT 25 · FİNAL VURUŞ KANITI · İNSAN ŞERİDİ · NOVUM ⛔ sınır · KASK 25/25 · E DOĞRULANDI) + "rubriğin BAŞINA yapıştır" satırı; ㉔ temiz | SPEC |
| D124 | araç 10 s üretti, plan 8 s'e yazıldı | KLİP SÜRESİ 10,0 s — PLAN'a "ffprobe ile ölç, ilk klipten sonra doldur" satırı; ızgara 9 + 24×10 | PLAN · SPEC |
| D142 | makine kapısı kurulu olmayan filtreye yazıldı | E bloğu her kapı: KOMUT · DOĞRULANDI (ffmpeg sürümü · tarih) · İKAME; `ffmpeg -filters` kuru koşu 9. adımda | SPEC E |
| D152 · D160 | eldeki küçük alet buharlaştı; master yanlış adla | alet BÜYÜK: "a forearm-long steel bar" (S6-S8 · S15); anahtar S2'de yalnız düşer (tutulmaz); SPEC künyesine master dosya adı satırı `the locked pulse.mp4` | S2 · S6-S8 · S15 · SPEC |
| D156 | planın SIFIR dediği beşi düştü | SPEC SIFIR KİLİTLERİ: insan repliği 0 · ekran metni 0,0 s · kart 0 · klon 0 · pencere 1 (yalnız B) · müziksiz pencere 3 (S0 · S20-S21 · S24) · sıvı temas 0 | SPEC B |
| D158 · D202 · ADAY-41 | seçimden sonra 0 seçim; seçim bedende görünmedi (THE CHOICE IS INVISIBLE) | seçim ÖNCESİ 3 başarısız deneme (S3 · S4 · S14 · S15); seçim S20 bedende: el fren çarkına "stops a palm's width short, holds two seconds, then returns to the knee"; seçimden SONRA ikinci seçim S22 (mühür); ÇAPA ÜÇLÜSÜ BEFORE/AFTER aynı kanalda | S3 · S4 · S14 · S15 · S20 · S22 |
| D163 · D135 · D188 | tek figürde şerit kör; sahne başlıkları ≠ plan | İNSAN ŞERİDİ `1111111111111-11111111111` (S13 insansız bilinçli); bölüm dosyalarında tam 25 `## 🎬 SAHNE n` başlığı | SPEC C · BOLUM_1/2 |
| D167 · D169 · ⑲ | 7 kimlik özniteliği × 25 prompt → kişi tanımlama reddi (SINKING STAKE) | kimlik ≤3 öznitelik gövdede (yüz biçimi · kaş kemiği · ten değeri); kesin boy/yaş sayısı PLAN'da kalır; yüz cümlesi yalnız yüzün konu olduğu sahnelerde TAM, diğerlerinde giysi+silüet | 25/25 |
| D168 | üretim sırası plana yazıldı, teslim baştan üretildi (3. vaka) | URETIM_DEFTERI §4: İLK KABUL EDİLEN KLİP = S20 (doruk) değilse defter kırmızı; sıra PAKET → S20 → S22 → S24 → S2 (iptal kapısı) → S0 → kalanı | PLAN · DEFTER |
| D176 | zemin rengi iki blokta iki türlü | zemin tek cümle WORLD'de: "a dark grey ribbed deck"; LIGHTING kontrast cümlesi ÖZNEYİ tarif eder, zemini yeniden tarif etmez | 25/25 |
| D179 · ADAY-… | imaj promptu değişimin SONRASINI yazdı (I2V t=0) | imaj = BEFORE (t=0); video = BEFORE→AFTER gövde fiiliyle; sonraki sahnenin imajı = AFTER; durum değişimi (jet biter · lamba yanar · eldiven çıkar) klip içinde ise TIMELINE'da saniyesiyle | S3 · S10 · S12 · S22 · S23 |
| D183 · D187 · D191 | novum sınırı sınanmadı; kilidin ölçen merceği yok; göz kapıları ekranda ihlal | SPEC NOVUM bloğuna ⛔ SINIR: "kural DÜŞEN nesneye uygulanır; sabit duran kayış eğik DEĞİLDİR, dik sarkar ve salınır"; her kilide ölçen mercek (⑥ FİZİK · ② DEVAMLILIK · ⑧ EFOR · ⑬ UYUM); F bloğu 12 göz kapısı | SPEC C · F |
| D192 · A5 | 1 numaralı risk yalnız sıfatla korundu | 1 NUMARALI RİSK = düşen aletin YANA inmesi (novum) → sayıyla: iniş noktası bırakma noktasından bir avuç genişliği (≈ 10 cm) ekran-SOLDA · düşüş süresi S2 0,9 s / S15 0,4 s · alet 0,3 m (anahtar) / 0,5 m (levye) · yön film boyu tek | S2 · S15 · 02_KONSEPT A5 |
| D197 · T11.5③ | vizör opak/şeffaf gidip geldi | vizör BERRAK 25/25 tek cümle "optically clear, no tint, no mirror coating, his face readable through it"; kask içi fill "a soft neutral fill from inside the rim" | 25/25 |
| D203 · ㉓ | 7 replik prompta hiç girmedi | 6 MACHINE repliği bölüm promptlarında TIRNAKLA; `grep -c '"'` ≥ 6; SPEC DIALOGUE LINES'la birebir | S1 · S6 · S9 · S12 · S13 · S18 |
| D205 | ⑤ çapraz süreyi karşılaştırmadı | SPEC RUNTIME 249,0 s ± 2 · GRID 9 + 24×10 | SPEC A |
| ADAY-3 · ADAY-63/74 | sayaç tek zamanda okundu; mekanik hız sabit değil | her sayaç ≥2 zamanda okunur: kayış 4,0 s (S0) · 2,7 s (S7) · 2,0 s (S21/S24); yıldız 1/3 tur (S1) · 2/3 tur (S18); lamba 6 (S2) · 7 (S24) | S0 · S1 · S2 · S7 · S18 · S21 · S24 |
| ADAY-6b · imza ① | iki ön kol tepeden makro ÜRETİLEMİYOR (YERCEKIMI S8 iptal) | bilek kilidi TEK bilek, YANDAN, kamera yaka hizasında, omuz+kask kadrajda (kurulum D); tepeden makro iki kol 0 kare | S12 · S14 · S22-S23 |
| ADAY-11/12/24 · T8 NOBODY PAYS | efor faturası ekranda 0 (COUNTED_TURN 0,0) | COST CURVE 25 hane PLAN'a; g arttıkça beden öder: adım kısalır (S7), omuz düşer (S11 · S16), levye elden kayar (S15), diz kırılır (S21), tek elle iş (S22) | S7 · S11 · S15 · S16 · S21 · S22 |
| ADAY-26/55/80/84 | travma sonrası duruş taşınmadı | kalıntı duruş ≥2 sahne: S21 · S23 · S24'te sağ omuz düşük, çıplak sağ el göğüs plakasına bastırılmış | S21 · S23 · S24 |
| ADAY-40/82 | lockoff'ta kamera kaydı (IRON SLOPE S2) | her video promptu "fixed lockoff, absolutely zero camera movement" (cümle başı VE sonu) | 25/25 |
| ADAY-64 | kadrajda ağız varken replik | replikli 6 sahnede ağız KAPALI ve ya sırttan (B) ya alt açıdan (H) ya dış (X) ya insert (D) | S1 · S6 · S9 · S12 · S13 · S18 |
| ADAY (NOBODY WAS ALIVE A1 · B3 · B4 · T-A) | — aday dersler, kart G'siz | A1: kötü haber SIRTTAN (S1 · S18 kurulum B); B3: bilgi ışık durumu değişimiyle (S6 alarm periyodu kısalır → anons); B4: BEFORE/AFTER çifti S0↔S24 aynı prompt tek kelime farkı; T-A: fren vanası kurulumu S0 (kenar) → ödeme S20 (reddedilir) | S0 · S1 · S6 · S18 · S20 · S24 |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_HARD_DOCK (① aynı format) | ⑨ KADRAJ 2/10 kafiye | 03:50 S24 kapanış kurulumu B iken açılış A → açılış-kapanış kafiyesi kırık | S24 = S0 harfi **A**, kamera cümlesi BİREBİR + "the same fixed framing as Scene 0"; tek değişken nesne (eldiven yakada · 7 lamba · kayış 2 s) |
| THE_HARD_DOCK | ⑪ IŞIK 5,5 | 01:20 S8→S9 yüzde renk sıcaklığı sıcak turuncudan nötr beyaza sıçradı; 00:50 ışık açısı kaydı | kask içi fill cümlesi 25 promptta AYNI ("a soft neutral fill from inside the rim"); KEY DIRECTION STRING kurulum başına sabit; alarm kırmızısının yüze düşme payı sabit ("the red lamp light reaches only his shoulder") |
| THE_HARD_DOCK | ⑧ EFOR 6,6 | 01:48 & 03:12 ağır nefeste vizörde buğu yok, 03:30 el titremesi yok | buğu yasak (vizör berrak) → efor GÖRÜNÜR nefes = göğüs/omuz kalkışı + eldivende görünür titreme cümlesi S15 · S20 · S22 |
| THE_HARD_DOCK | ⑦ AKSİYON 8,8 | 03:30-03:37 kenetlenme darbesi kesmeyle gizlendi (Action Ellipsis) | kilit anı (S12 · 123,0 s) ve mühür açılışı (S22 · 224,0 s) klip İÇİNDE, TIMELINE'da saniyesiyle; sınıra taşınmaz |
| THE_HARD_DOCK | ⑩ OYUNCULUK 7,4 · ⑫ HOOK 7,2 | S13-S16 dış dizi duygu tırmanışını böldü; 00:10-00:40 kokpit-dış tekrar platosu; 04:00 kart | dış sahne TEK (S13, bölüm sınırı); aynı mekân/kurulumda ≥3 ardışık sahne yok; kart 0,0 s |
| THE_HARD_DOCK | ① KARE · ② DEVAMLILIK | 1:10 dış istasyon dönüş açısı ~45° sıçradı; 01:30↔02:30 kol şeridi kaydı; 01:35↔03:03 kumanda kolu tasarımı değişti; cıvata 8→10 | dış görünüm yalnız S13 (tek kurulum X, dönüş SÜREYLE); şerit "one amber band on the LEFT upper arm" 25/25; vana çarkı/levye/fren çarkı tek tarif + RP paneli; sayılabilir nesne ≤7 (lamba dizisi) |
| THE_COUNTED_TURN (② aynı ortam §3.7) | ⑥ FİZİK 8,6 (1 FAIL) | S0 00:05 ilk düşüş 1,1 s, kilit 1,69 s; kayış 02:50 lastik gibi dalgalandı (Material Amnesia) | S0'da düşüş YOK (hook 9 s'de sayısal kilit sınanmaz); düşüş kilitleri S2 0,9 s · S15 0,4 s ± %20 (⑥ ölçer); kayış "stiff woven webbing … swings as one straight line, never ripples" |
| THE_COUNTED_TURN | ② DEVAMLILIK 3,0 KİMLİK KIRILMASI | S12 (1:50) · S14 (2:10) MCU'da sakallı erkek ↔ pürüzsüz kadın yüzü; S13 (2:00) beyaz giysi ↔ koyu deri ceket | yüz cümlesi + "a man in his forties" + giysi bloğu MCU/CU dâhil 50 promptta kelimesi kelimesine; RK1 vizör ardı yüz CU paneli KAPI 0 |
| THE_COUNTED_TURN | ① KARE 5,3 · ⑦ temas 4/10 | 0:27 · 3:25 parmak erimesi; 0:35 · 2:44 başparmak karabiner içinden; 1:26 · 1:44 · 3:05 kayış eldiven içinden | karabiner 0; kayış-el teması 0 sahne (kayış yalnız salınır, dokunulmaz); el-nesne teması S2 · S7 · S10 · S12 · S20 · S22'de "the glove closes around the wheel rim, the rim stays outside the glove" |
| THE_COUNTED_TURN | ⑧ EFOR 0,0 NOBODY PAYS · ⑩ 3,4 THE CHOICE IS INVISIBLE | 6 iş olayında beden yorulmadı; S20 kararında tereddüt/ağırlık sıçraması yok, manken postürü; 1:17 kalkış rijit | COST CURVE 0-9 PLAN'da; ÇAPA ÜÇLÜSÜ (S20 el yarım yolda 2 s · S22 tek elle mühür · S24 çıplak el göğüste); kalkış S4→S5 "weight goes onto the left boot first, then he rises" |
| THE_COUNTED_TURN | ⑪ IŞIK KEY WALKS · ④ 5,6 boş vuruş · ⑫ hook 10 s | S12/S14 MCU'da ana ışık 3→9 saat; S7 boş koridor · S8 oturma · S15 diz çökme tekrarı; hook kırpılmamış; S7-S9 plato; 4:10 kart | ışık yönü kurulum harfine bağlı ve BİREBİR; boş vuruş 0 (her sahnede THE STATE CHANGE cümlesi); aynı jest ≤2 (diz çökme S0'da var, sonra yok); hook 9,0 s kurgu kapısı; kart 0 |
| THE_PAYLOAD (③ aynı tema) | ④ HİKAYE 3,4 · plan kusuru D158 | 24 sahnede tutmayan deneme YOK; bedelden sonra 13 sahne 0 seçim; novum taşıyıcısı (el genişliğinde bant) rakip olayla aynı promptta okunmadı | başarısız deneme ×4 (S3 · S4 · S14 · S15); bedelden (S12 kilit) sonra iki seçim (S20 · S22); taşıyıcı tek klipte rakipsiz (S2'de yalnız anahtar düşer, kayış S2'de KADRAJ DIŞI) |
| THE_PAYLOAD | ① · ② · ③ (mod V) | "PHASE 1" göğüste, "EVA" sırtta (defter etiketi giysiye basıldı); 4 replik "gördüğümüzü anlatıyor"; 1:40 klon; kasa 9→8; müziksiz pencere 3→0; hook 10 s; kuyrukta başka filmin kartı | etiket 0; replik İŞLEV sütunu — görüneni anlatan replik yok ("the ring is speeding up" YAZILMAZ, makine SAYI söyler); klon 0 cümlesi; lamba 7 yuva 25/25; SPEC SIFIR KİLİTLERİ + müziksiz pencere 3 |
| THE_IRON_SLOPE (④ en düşük skor T4 2,6) | ④ · ⑥ · ⑤ · ① | serbest panel sabit 0,15 m/s süzüldü (kilit 9,7 m/3 s) → "THE ONE THING NOTHING ELSE DOES: none found"; S2 yasaklı gezegen kadrajda; göğüste arma; S2 kamera kaydı; kart | novum kanıtı SÜREYLE (D127) ve İPTAL KAPISI S2 (anahtar yana inmiyorsa üretim durur — kapı koşulmadan diğer sahne üretilmez); iç kadrajda pencere yalnız B (yıldız, gezegen 0); arma/bayrak 0; "zero camera movement" cümle başı+sonu |
| THE_STATIC_SHADOW (⑤ en yakın konsept) | ⑬ · ③ · D203 · D204 · D205 | 7 HELIOS repliği promptlara hiç girmedi (tırnak 0); SPEC yedi makine çapasını kaybetmiş kabuk; ⑩ 60 s · ⑫ 25 s süre uydurdu; üretim defteri boş, karar bloğu (S11-S14) makarada yok [D168 3. vaka] | 6 replik bölüm promptlarında tırnakla (㉓); SPEC yedi çapa dolu (㉔); RUNTIME 249,0; DEFTER §4 ilk-KABUL = S20; üretim sırası doruk önce |
| THE_STATIC_SHADOW | ② · ⑪ · ⑥ · ⑤ | kask S1'de yok; vizör şeffaf ↔ opak; ölçek 1:6 (SPEC 1/30); dönüş 1,5°/s (SPEC 0,46); dış kamerada RCS tıslaması (SPEC mutlak sessizlik); kuyruk kartı + filigran 12/12 | kask 25/25 tek cümle; vizör berrak 25/25 (RK1 paneli); dış S13 ölçeği gövde-boyuyla + SPEC'te R 56 m; dönüş SÜREYLE ("two thirds of a turn in the shot"); dış S13 AUDIO: yalnız makine anonsu (telsiz, yatak yok); F bloğu köşe testi + freezedetect |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PB (vaka 13 · YERCEKIMI S8 · SAHNE İPTAL) | kelimeler temizdi; kompozisyon: yan yana iki ön kol + tepeden makro + yüzsüz izolasyon | sözcük değişimi YETMEDİ → kadraj değişti (ray hizası, nesneler ard arda) | S12 · S14 · S22-S23 bilek: TEK bilek, YANDAN, kamera yaka hizasında, kask+omuz kadrajda; tepeden makro 0 kare; iki yenilgi kuralı: red gelirse sözcük değil KAMERA değişir (D → C) |
| PK (vaka 15 · SINKING STAKE · OMNI kişi tanımlama) | tek kişide 7 kimlik özniteliği × 25 prompt + "face fully readable at every angle" | ⬜ önerilen: kimlik yığını sökülür, kesin boy → göreli, ten/saç/yaş PLAN'da, yüz tarifi yalnız yüzün konu olduğu ≤4 sahnede | ⑲ ≤3 öznitelik gövdede; tam yüz cümlesi yalnız C ve J kurulumlarında (yüz konu), D/G/H/B/X'te giysi+silüet; "readable at every angle" YAZILMAZ |
| PB (vaka 3 · COLD BURN S28) | kask ÇIKARMA eylemi | kasklar baştan rafta, kimse bir şey çıkarmıyor | kask 25/25 ON, çıkarma 0; S22 mühür açılışı KASK değil BİLEK: "the wrist ring turns a quarter turn and the glove stays seated in the collar as the hand draws back" — çıkarma fiili yok, eldiven yerinde kalır |
| PK+PB (vaka 4 · COLD BURN S26) | tehlike çerçevesi sözlüğü: 'wounded ship' · 'dull orange glow' + replik | replik değişti, tehlike sözlüğü ayıklandı | alarm "a red lamp above the bay" (emergency/danger/failure/warning yok); makine repliklerinde "leak persists" var — 'leak' T2 mi? ⑯ koşulunca bakılır, gerekirse "coolant loss continues" |
| YR (vaka 2 · COLD BURN S8) | insansız sahne + uzun NEGATIVE + "Exactly 0 human figures" | NEGATIVE tek pozitif Style satırına indi | S13 dış insansız sahne: NEGATIVE KISA (yörünge bloğu yalnız gerekli 3 cümle), "0 human" yerine pozitif kadraj ("the ring, its four spokes and the hub against a flat black sky") |
| PK+PB (vaka 10 · RISING SNOW) | 'LIP-SYNC REQUIRED' başlığı · '44-YEAR-OLD MAN' + '3cm scar' · 'hammer'+'blows' | dördü kaldırıldı | başlık/etiket 0; yaş sayısı yok ("a man in his forties"); yara/ben yok; alet "a steel bar" ve fiil "levers" — 'hammer/strike/blow' 0 |
| PK (vaka 11-12 · SLOW STONE · LOW POWER) | dead/body/decay; milliyet ifadesi | sözlük arındırıldı; milliyet silindi | kriyo kapsülü kadrajda yok → 'frozen/body/sleep pod' 0; milliyet 0; ⑯ sözlüğü klasör modunda koşar |
| TK 0-başarı kuralı (vaka 5-6) | aynı oturumda hiç geçen prompt yok | 3. yeniden yazımdan ÖNCE PROB_KOSUSU | DEFTER'e satır: 2 red / 0 başarı → prompt değil ÜRETİM tarafı; MOTOR + İLERLEDİ sütunu red günü doldurulur |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
   Bu filmde: fren vanası "a second wheel, smaller, with a yellow-and-black
   band, at floor level on the right" (fonksiyon adı 'brake' promptta YOK);
   bilek durumu "the wrist ring seats / stays seated" (kilit=eylem değil durum).
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        48 satır (§1)
QA ARIZASI:         16 satır (§2 · beş kayıt)
RED SINIFI:         8 satır (§3)
⛔ EN PAHALI ÜÇÜ:
  ① NOVUM EKRANA GELMİYOR (IRON SLOPE D127 · PAYLOAD D157) → düşen alet
     SÜREYLE + yön sabit + İPTAL KAPISI S2; 1 numaralı risk SAYIYLA (A5)
  ② BİLEK KİLİDİ KOMPOZİSYONU RED (YERCEKIMI S8 PB · imza ①) → tek bilek
     YANDAN, kamera yaka hizasında, kask+omuz kadrajda; iki yenilgi = kamera
  ③ BEDEL BEDENDE OKUNMUYOR (COUNTED_TURN ⑧ 0,0 · ⑩ 3,4 · D158) → COST CURVE
     + ÇAPA ÜÇLÜSÜ + 4 başarısız deneme + seçimden sonra ikinci seçim
  (üçü 04_UYARI_NOTLARI'nda ⛔ satırıdır)
```
