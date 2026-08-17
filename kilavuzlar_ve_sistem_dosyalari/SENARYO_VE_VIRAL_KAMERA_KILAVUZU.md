# 🎬 SENARYO VURUŞ HARİTASI + VİRAL KAMERA PSİKOLOJİSİ KILAVUZU

> **Kaynak:** Proje sahibinin senaryo yazımı / kamera açıları / viralite
> araştırması (06.08.2026) — bu dosya o araştırmanın DEPOYA UYARLANMIŞ
> hâlidir. Araştırma geleneksel sinema + sosyal medya için yazılmıştı;
> burada her öğe deponun kurallarına (tek çekim, 0 kesme, metin 0,0 sn,
> tek kamera hareketi, negatif çekirdek) karşı süzüldü. **Çelişen öğeler
> atılmadı, §1'de gerekçesiyle işaretlendi** — bir sonraki ajan "araştırmada
> vardı" diye geri eklemesin.
>
> **Ne zaman okunur:** PLAN yazılırken (sahne haritasından ÖNCE — §2) ve
> kamera/kompozisyon satırları yazılırken (§3-6). QA tarafı değil, üretim
> tarafı kılavuzudur.
>
> İlgili dersler: 62 · 70 · 71 · 72 · 73 · 74 — `LESSONS_LEARNED.md`

---

# 1. ⛔ ARAŞTIRMADAN DEPOYA **GEÇMEYENLER** — dürüst kayıt

| Araştırmadaki öğe | Neden geçmedi |
|---|---|
| Courier 12 punto, 1.5" marj, sayfa/sekizlik dökümü | Depo senaryo PDF'i üretmiyor, prompt üretiyor. İlkenin karşılığı zaten var: **sabit sahne birimi** (8 s/10 s) = deponun "1 sayfa ≈ 1 dakika"sı. |
| SnorriCam | Negatif çekirdek: "no camera shake / no handheld". Karakterin iç kaosu bu seride kamerayla değil geometriyle anlatılır. |
| Jump cut · dissolve · iris · freeze frame | Sahne İÇİ kesme = üretim hatası (Ders 1); sahne SINIRI = yalnız sert kesme (SHORTS_QA §E). Freeze frame ayrıca loop'u öldürür (§5). |
| "Algılanan otantiklik" (titrek el kamerası, ham görüntü estetiği) | Serinin kimliği Kodak Vision3 sinema görüntüsü. Otantiklik dağıtım katmanının işidir (başlık/açıklama), kadrajın değil. |
| Kayıptan-kaçınma metin kancaları ("hâlâ bunu yapıyorsan…") | Ekran metni 0,0 sn [Ders 61/70]. Metin kancası platform açıklama alanına yazılır → `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md`. |
| Whip pan geçişi, crash zoom zinciri | Çekim başına TEK sürekli hareket kuralı. Crash zoom tek başına meşru (bkz. §3); zincirleme agresif kurgu değil. |

---

# 2. 🥁 VURUŞ HARİTASI — Save the Cat'in depo ölçekleri

Araştırmanın 15 vuruşu uzun metraj içindir. Bu bölümdeki eşleme, vuruşları
deponun iki ana formatına indirir. **Kural: her plan, sahne haritasını
yazmadan önce bu tabloyu doldurur** — boş kalan vuruş "bilinçli sapma"
notu ister.

## 2.1 DİKEY SHORTS (6 sahne × 8 s) eşlemesi

| Vuruş | Sahne | Bu depoda karşılığı |
|---|:--:|---|
| Açılış imajı | S0 0-2 sn | Sıradan görünen dünya (viral zamanlama yasasının "merak" bandı) |
| Katalizör | S0 5-7 sn | REVEAL — ikili kilitle girer, analog perdeyle değil [Ders 71] |
| Tartışma | S1-S2 | Karakterin DOĞRULAMA jestleri: bakar, kontrol eder, tekrar bakar — panik değil meslek refleksi |
| **Orta nokta = CENTRAL CHOICE** | **S3** | Karakter bir şey SEÇER ve seçim EKRANDA tamamlanır [Ders 72 kapı maddesi]. "Durup izlemek" bir seçimse, seçimi görünür kılan JEST yazılır — novum render edilmezse jest ölür [Ders 73 · Wrong Shadow] |
| Doruk | S4 | Filmin en pahalı karesi; üretim buradan başlar (üretim-önce kuralı) |
| Kapanış imajı | S5 son 2 sn | **Açılış imajının aynası ya da tersi** — §5 loop bununla birleşir |

## 2.2 YATAY 2-4 DK (~15-18 sahne) eşlemesi

| Vuruş | Yüzde | Sahne bandı | Not |
|---|:--:|:--:|---|
| Açılış imajı | %0-5 | S0 | Kapanış imajıyla ÇİFT tasarlanır |
| Kurulum | %0-10 | S0-S2 | Dünya + karakterin yetkinliği |
| Katalizör | ~%10 | S2 | **İlk 15 saniyeyi geçemez** — araştırmanın "geç katalizör = terk" bulgusu |
| Tartışma | %10-25 | S3-S4 | Atlanırsa karar yapay kalır — atlamak yasak |
| Orta nokta | ~%50 | S7-S8 | Sahte zafer YA DA sahte yenilgi; bahis yükselir |
| Her Şeyin Kaybı | ~%75 | S11-S12 | SOMUT ve geri döndürülemez — "üzgün hissetmek" değil, görünür kayıp |
| Umut-önce-düşüş | kayıptan hemen önce | — | Araştırmanın "up-before-down" kuralı; senaryo rubriği de sorar |
| Final | %85-99 | S13+ | Doruk sahnesi kurguya GİRMEK zorunda [Ders 62 ×5 · 72] |
| Kapanış imajı | %100 | son sahne | Açılışın aynası; temayı taşıyan tek kare |

## 2.3 Vuruş haritasının üç sert kuralı

```
① KAMERA-TAŞIYICI TESTİ her planda: "Karakteri dronla değiştirsek ne
   kaybolur?" Cevap yoksa plan bitmemiştir. (Hikaye tablosundaki tek
   kırılmayan darboğaz KARAKTER sütunudur — 03_HIKAYE_KALITE_TABLOSU.)
② SEÇİMİN BEDELİ YAZILIR: vazgeçilen şey kadrajda görünür bir nesne/
   durumsa tema yapısaldır; cümleyse dekoratiftir.
③ AÇILIŞ-KAPANIŞ ÇİFTİ tek karar olarak verilir: iki imaj yan yana
   konduğunda değişim okunmuyorsa film daha yazılmamıştır.
```

---

# 3. 🎥 KAMERA AÇISI PSİKOLOJİSİ — karar tablosu

> Depo kuralları baki: çekim başına TEK lens, TEK sürekli hareket,
> metre cinsinden mesafe/yükseklik. Bu tablo hangi açının hangi duyguyu
> satın aldığını söyler — promptun COMPOSITION/CAMERA satırına sayıyla iner.

| Açı / hareket | Psikolojik etki | Depoda kullanım | Risk |
|---|---|---|---|
| **Alt açı** (kamera göz seviyesi altı, yukarı bakar) | Özneyi büyütür: güç, tehdit, hayranlık | Dikeyin doğal silahı — karakter alt 1/3, imkansız ölçek üst 2/3 zaten alt açı grameridir. Sayıyla yaz: "camera height 0.6 m, tilted up 15°" | Düşük |
| **Üst açı** | Özneyi küçültür: çaresizlik, önemsizlik | Yatayda karakterin ortama yenildiği vuruşlar (%75 bandı). Dikeyde DİKKAT: yerdeki reveal'i alt köre gömer (güvenli alan) | Orta |
| **Hollanda açısı** (sabit eğik ufuk) | Tekinsizlik, akıl kayması | Lockoff ile uyumlu (eğim sabitse tek karar). Seride emsali yok → kullanan ilk film "bilinçli sapma" olarak yazar; eğim derece ile kilitlenir ("horizon tilted 8°, constant") | Orta — model eğimi "düzeltme" eğiliminde |
| **Dolly zoom** (dolly + zıt zoom) | Gerçekliğin kırılması; bilişsel şok | TEK sürekli hareket sayılır → kurallara uyar. YALNIZ doruk sahnesinde, filmde bir kez. Yazımı sayısal: "slow dolly-in 6 m→4 m while focal length widens 50 mm→32 mm; subject size constant, background expands" | 🔴 YÜKSEK — AI'da en kırılgan hareket; tek-kare/kısa test üretimi şart [Ders 73 kapısı benzeri: önce dene] |
| **Crash zoom** | Ani enerji, şok | Hook'ta scroll durdurucu tek hareket olarak meşru: "one fast crash zoom from 9 m framing to face, 0.5 s, then hold" | Orta — sarsıntıya dönüşürse negatif çekirdeğe takılır |
| **Yavaş dolly/track** | Sinematik ağırlık, beklenti | Deponun varsayılanı — mevcut kılavuzlarda zaten kilitli | Düşük |

**Kural:** Bir sahnenin duygusu değişiyorsa aracı açı değişimidir, kesme
değil — kesme hakkımız yok. Güç el değiştiren filmde alt/üst açı çifti
İKİ AYRI SAHNEYE dağıtılır (aynı çekimde açı değişimi = iki hareket).

---

# 4. 🪝 KANCA — TAŞINDI → `HOOK_VE_ILK_SAHNE_KILAVUZU.md`

> **09.08.2026:** Bu bölümün dört kuralı (0. kare sınavı, ikili kilit
> reveal [D71], 3. saniye kontrolü, vaat-teslim) genişletilerek
> **`HOOK_VE_ILK_SAHNE_KILAVUZU.md`** dosyasına taşındı. Yeni kılavuz
> ayrıca S1 tırmandırma sahnesini, hook tipolojisini, ilk 2 saniyenin
> ses tasarımını ve hook-önce üretim kapısını tanımlar.
> Burada içerik tutulmaz — iki kopya ayrışır. §5 (loop) ve §2 (vuruş
> haritası) bu dosyada kalmaya devam eder; hook kılavuzu ikisine de
> adres verir.

---

# 5. 🔁 KUSURSUZ DÖNGÜ (SEAMLESS LOOP) — bedava tutundurma

Araştırmanın depoya en doğrudan katkısı. Rubrik §15 loop'u zaten ölçüyor;
bu bölüm onu ÜRETİM tarafında tasarlatır. Loop, izleyiciye videonun
bittiğini fark ettirmeden 0:00'a dönmektir — her tekrar izleme algoritmaya
"olağanüstü içerik" sinyalidir.

```
PLAN KURALI — her shorts planına bir LOOP SATIRI yazılır:

① KADRAJ EŞLEŞMESİ: S5'in SON beat'i ile S0'ın İLK beat'i aynı kadraj
   ailesindendir (aynı lens sınıfı, benzer kompozisyon, aynı yön).
   Örn. S5 pull-back geniş düzlükte biter → S0 geniş düzlükte açılır.
② HAREKET DURMAZ: son karede poz verilmez, dondurulmaz — süren ama
   tamamlanmamış bir hareketle kesilir (araştırma: duran hareket =
   "bitti" sinyali = kaydırma).
③ SES: müzik son saniyede çözülmez (kadans yok); ya loop-uyumlu düşük
   katmana iner ya da 1 sn mutlak sessizlikle keser — sessizlik de
   loop'lanır. GOOGLE_FLOW_MUSIC kılavuzuyla birlikte karar verilir.
④ JENERİK KARTI = LOOP KATİLİ: karta harcanan saniye hem metin ihlali
   hem 0:48→0:00 bağlantısının ölümüdür [Ders 70 zaten yasaklıyor].
⑤ Işık sürekliliği loop'la ÇELİŞEBİLİR: gün batımına ilerleyen film
   (örn. Wrong Shadow S5 akşam ↔ S0 öğle) kadrajla değil KOMPOZİSYONLA
   loop'lanır — son kare siluet/geometri olarak ilk kareye benzer,
   renk farkı kesmeyi "aynı günün yeni turu" gibi okutur. Bu bir
   tasarım kararıdır ve plana yazılır; yazılmadıysa loop yok demektir.
```

---

# 6. ✂️ SAHNE SINIRLARI — izinli geçiş grameri

Kurguda tek meşru geçiş sert kesmedir (rubrik §E). Bu, geçiş TASARIMI
yapılamaz demek değildir — tasarım kesmenin İKİ YAKASINA yazılır:

| Teknik | Depoda hâli |
|---|---|
| **Match cut** | İZİNLİ ve önerilen: komşu sahnelerin son/ilk kareleri geometrik eşleşme ile planlanır (S2 son karede dikey jalon → S3 ilk karede dikey figür). Promptlara ayrı ayrı yazılır, kurguda kendiliğinden çalışır. |
| **Smash cut** (kontrast kesme) | Yalnız SES katmanında: yoğun ses → ani sessizlik. Görüntüde ışık/mekan zıtlığı Ders 47/48'e takılır — kullanma. |
| **Ses köprüsü** | Müzik vuruşu sahne sınırına oturur (GOOGLE_FLOW §14 spotting) — hit'ler kesmeyi "görünmez" yapar. |
| Dissolve · fade · wipe · iris | ⛔ Yasak — üretim değil kurgu eklentisidir ve rubrik BLOCKER sayar. |

---

# 7. ✅ PLAN-ÖNCESİ EK KONTROL — bu kılavuzun 6 maddesi

> `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md`'nin yerine
> geçmez; onun ÜSTÜNE senaryo/kamera katmanı ekler.

```
□ Vuruş tablosu (§2) dolduruldu mu — boş vuruşlar "bilinçli sapma" notlu mu?
□ CENTRAL CHOICE hangi sahnede, seçim hangi JESTLE ekranda tamamlanıyor?
□ Novum taşıyıcısı birincil nesne mi? Türetilmiş fenomense (gölge/yansıma)
  tek-kare fizibilite kapısı planlandı mı? [Ders 73]
□ Açılış-kapanış imaj çifti yan yana yazıldı mı; değişim okunuyor mu?
□ LOOP SATIRI yazıldı mı (kadraj eşleşmesi + durmayan hareket + ses)?
□ HOOK_VE_ILK_SAHNE_KILAVUZU.md §8 kontrol listesi (7 madde) dolduruldu mu?
```
