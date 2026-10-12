# 🎬 GÖSTERİM ÇÖZÜMLERİ — modelin bozduğu fiziksel anı kadraj, kesme ve sesle göstermek

> **Ne için:** ölümcül teknik hataların ~%45'i neyin gösterildiğinden doğdu (`ARIZA_LISTESI.md` T, "kadraj/hareket %45").
> ARIZA_LISTESI hatanın **nerede** kapandığını söyler (KADRAJ · KURGU · TASARIM); bu sayfa **nasıl** kapandığını an türü
> başına örnek ve kanıtla verir. Bu bilgi beş ajana dağınıktı: yonetmen · teknik-danisman · goruntu-yonetmeni ·
> devamlilik · kurgucu.
> **Kim okur:** yonetmen (faz 3, `Risk → nasıl gösterilir` sütunu) · teknik-danisman (faz 3 ve 5 eleştirisi, faz 7 ret) ·
> goruntu-yonetmeni (faz 5, başlangıç karesi ve video promptu) · kurgucu (faz 8, giriş/çıkış ve ses köprüsü).
> **Ne değildir:** kural, kapı ya da kontrol listesi değildir; `film_dogrula.py` denetlemez. Prompt yazım kuralları
> (`.claude/agents/goruntu-yonetmeni.md`) ve risk kontrol listesi (`.claude/agents/teknik-danisman.md`) burada tekrar
> edilmez. Örnek ve kanıt kataloğudur (AGENTS §1 ④): yeni satır ancak iki ayrı filmde kayıtlı vakayla ve sahibin kararıyla girer.
> **Tarih:** 07.10.2026 · **Kaynak:** `ARASTIRMA/04_SUZME_20261007.md` R9 + §F V5-V11 · `ARASTIRMA/qa_prompt_analizi_20261006/`
> (12 film, 698 bulgu, `OZET_topla.txt`) · `ARIZA_LISTESI.md` T · `BILINEN_TUZAKLAR.md` §B ·
> `HELMET_TO_HELMET/ODA/F1_yonetmen_1.md` (B1-B13) · `F3_yonetmen_1.md` (C01-C59) — film klasörü 08.10.2026'da sahip
> kararıyla silindi (71 çekimlik değişken süreli plan, 10 s kuralıyla uyumsuz); yedek `~/film_medya/_yedek/filmler_20261008/`.

**Kanıt etiketleri**
- **ALGI:** insan algısı araştırması (04 §F V9 · V10).
- **KIYAS:** model kıyas makalesi (V6b · V8a · V11a). Veo'yu ölçmez; yalnız yön gösterir.
- **DEPO:** kayıtlı vaka. Zaman, ham raporun PART içi zaman kodudur. Raporları yapay zekâ yazdı ve çoğu mod V ya da
  geçersiz; sayılar yön gösterir. Hüküm: 🅐 cümle promptta yazılıydı, model tutmadı · 🅑 cümle yoktu ·
  🅑+ prompt kusuru çağırdı (`qa_prompt_analizi_20261006/GOREV.md`).
- **UYGULAMA:** kaynak yok ya da yalnız HELMET_TO_HELMET planı. Sonucu ölçülmedi.

⏳ **Bugünkü uygulama:** HELMET_TO_HELMET (faz 3, tur 1, Flow kredisi 0). İki kasklı kişi var; kask kaska ve kask-çelik
teması var. Aşağıdaki "HELMET Cxx" ve "F1 Bn" çözümleri o filmde **uygulanıyor, sonucu henüz ölçülmedi.** Sonuç filmin
`NOTLAR.md`'sine yazılır; bu sayfaya ancak AGENTS §1 ④ yoluyla girer.

---

## 1 · ANA TABLO — an türü başına

| An | Bozulma biçimi · depo vakası (film · sahne · zaman) | Kadraj çözümü | Kurgu çözümü | Ses çözümü | Kanıt | En kısa okunur süre |
|---|---|---|---|---|---|:--:|
| **El-nesne teması** (kavrama · takma · çevirme · kol) | Parmak nesneye erir, el aletten ya da koldan geçer, fazla parmak çıkar. THE_LAST_GATE PART4 00:51 (K78) *"Gloved hands phase into cable connector tool during insertion"* · 02:43 (K89) *"Control lever shaft clips through gloved palm during actuation"* (temas cümlesi yazılı, 🅐) · THE_STOLEN_SKY PART2 01:33 (S33) eldiven panel kilidine kaynadı (🅐) · THE_SLOW_RAIN PART1 2:35 (S15) eldiven tokaya eridi (🅐) | Temas anı kadrajda yok. Üç yol: çekim temasa bir avuç kala biter · el temas kurulu başlar ve kıpırdamaz (sabit insert) · sonuç elsiz insert (takılı kanca, açılmış kenet). Kol ya da mandal hiç kadraja girmeyebilir: yüz → omuz tek sert çekişle sarsılır → elsiz insert (F1 B8) | Öncesi → kesme → sonrası; kesme temasın kurulacağı karede. Sonrası eylemin izini taşır (açık avuç hâlâ uzanmış · F1 B5), yoksa izleyici kaza okur (T14). Bilinen hataya ±0,3 s'den yakın kesilmez (kurgucu kural 3) | Temas ya da kilit sesi (tık) kesmeyle aynı karede, kurguda; vakumda gövdeden iletilen ses. Sayılan vuruş sesle verilir, eldiven kadraja girmez (F1 B13). Model sesi atılır | DEPO: el-nesne 43 satırın 29'u 🅐 · THE_COUNTED_TURN 22/25 → 7 🔴 · KIYAS: VideoPhy-2 %22 · ALGI: Levin & Simons %33 · ses ve iz: UYGULAMA | — |
| **İki kişi arasında temas** (tutma · itme · kask-kask · omuz) | El ötekinin giysisinden geçer, el temas etmeden havada kalır, temas sürerken üçüncü figür belirir. THE_LAST_GATE PART4 01:02 (K79) *"Standing astronaut hand clips through seated astronaut suit shoulder harness"* (🅐) · THE_STOLEN_SKY PART1 00:34 (S03) 10 s'lik kavramada parmak giysiye kaynadı, 00:39 üçüncü figür · PART3 01:40 (S58) el omza ulaşmadan havada kaldı. S03 ve S58'de temas başlangıç karesi promptunda kuruluydu (`already closed`) | Kadrajda temasın tek tarafı net: dinleyenin tekli, öteki yalnız flu kask kenarı. Temas çizgisi yakındaki kabuğun arkasında, kamera boş taraftan ¾. Eller kadraj dışında. "Zorla bastırma" yerine tek temas başka yüzeye (kask → sırt çantası ya da kiriş · F1 B2). Hareketli temas zorunluysa çok uzak geniş plan (F1 B4) | Temas başka bir çekimin ardında kurulur (HELMET C29: insansız kapsül çekimi). Sonraki çekim temas sürerken başlar, temas değişmez. Ayrılma tek küçük hareket (C37) | İki kaskın tok vuruşu ara çekimde duyulur; temasla açılan iç ses ayrılma karesinde kesilir (C37) | DEPO (bozulma; kurulu temas da bozuldu) · çözüm UYGULAMA | — |
| **Havada tutulan ya da taşınan nesne** | Nesne tutansız asılı kalır, el boşluğu kavrar, el ya da kask gövdesiz süzülür. THE_SIGNAL_KEEPERS 3:45 (K23) *"fingers curl inward as if grabbing an unseen object"* (küreyi taşıyan yazılı değil, 🅑+) · THE_STOLEN_SKY PART4 1:44 (S82) *"Disembodied gloved hand and suit helmet floating in mid-air"* · PART3 01:00 (S54) *"identical detached gauntlets rest on a workbench"* (ikisi de yalnız-eller kadrajı; 17 klipte kol-gövde bağı yazılı değil, 🅑+) | Tutan kadrajda: el + ön kol + kolun girdiği kenar (goruntu-yonetmeni, görsel prompt). Tutan yoksa bağ görünür: nesne kancayla ya da iple bir yapıya bağlı süzülür (HELMET anten · F1 B1) | Taşıma yolu gösterilmez: nesne A'da → kesme → nesne B'de. Kaldırma (yuvadan çıkma) kesmede | — | DEPO (bozulma: tutan yazılmayınca) · çözüm UYGULAMA | — |
| **Ağır iş ve efor** | Ağır kol ya da kapak kâğıt gibi oynar, gövde yükü taşımaz, nefes değişmez. THE_LAST_GATE PART4 02:41-02:49 (K89) *"pulling a heavy mechanical console lever produces no shoulder drop, core bracing, or breath change"* (yük ve duruş yazılı, 🅐; aynı klipte el kola geçti) · THE_STOLEN_SKY PART2 01:30 (S33) panel açıp çekirdek çekme *"Suit That Isn't There"* 🔴 (🅑) | Efor elde değil gövdede okunur: tek büyük gövde hareketi (ağırlık geriye, omuz sarsılır), orta ya da geniş plan; el-alet yakını yok. Kısa çekim (ARIZA T02). Bedeli ayrı çekim taşır: nefesle inen göğüs | İş bölünür: başlangıç → kesme → yükün yer değiştirdiği sonuç. Aynı eylem ikinci kez gösterilmez (H01 · H04) | Kask içi nefes ve zorlanma, kurguda (UYGULAMA) | DEPO: efor/beden 126 satır, 🔴 90 (🅑 63 · 🅐 25 · 🅒 29) · T02 24/49 film · çözüm UYGULAMA | — |
| **Benzer giyimli iki kişi aynı karede** | Gövdeler birleşir, klon ya da üçüncü figür belirir. THE_LAST_GATE PART2 00:24-00:28 (S27) *"Fig 4/5 merged torso/3 legs"* ve 02:02-02:07 (S37) oturanların gövdesi birleşti (aralık cümlesi yazılı, 🅐) · PART3 01:32 (S58) *"Duplicate clone characters … marching in corridor line"* (altı kişiye tek "same white main suit" cümlesi, 🅑+) · THE_STOLEN_SKY PART1 00:39 (S03) iki ayrı renk giysi ve sayı kilidi yazılıyken üçüncü figür sol kenardan çıktı (🅐) · THE_SECOND_SHIP S30 üçüncü beyaz figür | Çekim başına tek özne. İkinci kişi yalnız konum ya da mesafe bilgisi için kalır; o zaman küçük, ayrık ve farklı ölçekte. İki kişiye ayrı renk işareti (omuz bandı · eldiven bileği · ip). Aradaki boşluk düz zemin önünde okunur (Dünya'nın parlak yüzü ya da siyah · F1 B6) | Karşı çekim: A'nın tekli → B'nin tekli, her birinde ötekinin flu kenarı (HELMET C33-C37) | Konuşanı ses odası ayırır (kimin kaskı · telsiz · ortak); ağız görünmez (F3 §2 oda sütunu · UYGULAMA) | DEPO: klon 11 satır, 🔴 8 · T15 9/49 · cümle ve sayı kilidi yazılıyken bozuldu · renk işareti UYGULAMA | — |
| **Durum değişimi** (kapak · ışık · kanca · kenet) | Değişim çekimin içinde çağrılınca nesne bozulur ya da yan etki çıkar. THE_STOLEN_SKY PART2 02:53 (S41) *"Heavy blast door phases directly through alien creature's torso"* (inen kapağın altından geçiş, 🅑+) · THE_LAST_TOW PART2 1:10 (K32) kapak açılırken asılı toz (toz yasağı yazılı, 🅐) · 🅐5: durum merdiveni metinle tutmadı (FROST_LINE · BORROWED_WEIGHT) | Her durum ayrı başlangıç karesi (F3 §5: KOL_elde/elsiz · KANCA_takili/bosta · CANTA_kavrama/acik). İki durum aynı kadraj ilişkisiyle çekilir (C17 ↔ C27 · C31 ↔ C41). Çekim içinde durum sabit kalır | Değişim kesmede; araya tetikleyen bakış ya da yüz girer (C25 → C27). Işık rengi (kehribar → kırmızı) iki ayrı kare, değişim kesmede (F1 B12) | Değişimin sesi (tık · gümleme · uğultunun kesilmesi) kesmede, kurguda (UYGULAMA) | KIYAS: T2V-CompBench dinamik nitelik en iyi 0,0687 · ALGI: Levin & Simons · DEPO | — |
| **Zemine ya da yüzeye geçme** | Bacak ya da gövde zemine gömülür, kanat yere geçer, ayak geri kayar. THE_SLOW_RAIN PART2 0:39 (S27) *"lower legs and thighs clip through the dark terrain/liquid surface plane while pulling the sled tether"* · PART1 2:14 (S13) kanat yere geçti (🅑+) · THE_STOLEN_SKY yürüyüş ve adım çekimleri S20 · S32 · S49 · S55 · S60 · S61 · S75 (🔴, 🅑) | Geniş temas (diz çökme, yaslanma) kısa tutulur ya da bölünür (BILINEN §B 10). Ayak-zemin çizgisi ya kadraj dışında (bel üstü) ya da uzak geniş planda küçük | Yolculuk kesmeyle kısalır (H03): çıkış → kesme → varış. İniş ya da çarpma anı kesmede, sonrası duruş | — | DEPO: 21 satır, 🔴 15; 14'ü 🅑, 🅐 yalnız 2, yani cümlenin işe yaradığı da ölçülmedi · çözüm UYGULAMA | — |
| **Sıfır yerçekiminde süzülme** | Sebepsiz süzülme; aynı kadrajda iki yerçekimi rejimi. THE_LAST_GATE PART1 02:10 · 02:30 (S15/S17) *"foreground astronaut floating horizontally in zero-g alongside a grounded background soldier"* (gardiyana 1g deyimi `holds his ground`, 🅑+) | Aynı kadrajda tek rejim (ARIZA T08). Süzülenin bağı görünür (ip · kanca · tutamak). Süzülme tek ve sebepli; itiş ya da çarpma kadraj dışında. Sabit kamera ve sabit referans (kiriş, tırabzan). "Kaskını çevirir" yerine gövde dönüşü (F1 B11) | İtiş anı kesmede; sonrası tek küçük sürüklenme (HELMET C03) | — | DEPO: yerçekimi/süzülme 28 satır, 🔴 13 · T08 15/49 · çözüm UYGULAMA | — |
| **Vakumda kıvılcım, duman, egzoz** | Kıvılcım pus ve duman doğurur, egzoz havadaki gibi kabarır, temasta toz bulutu çıkar. THE_LAST_GATE PART4 01:14 (K80) *"Pod rocket exhaust billows like atmospheric smoke in vacuum space"* · THE_STATIC_VEIL 1:13 (S07) *"Electrical spark arc generates atmospheric smoke and volumetric haze"* (`without vapor … no vapor plumes` yazılı, 🅐) · THE_LAST_TOW PART2 0:00 (K25) temasta toz bulutu (🅑+) | Olay taşıyıcı an yapılmaz (ARIZA T03). Kaynak (çarpma · itici · kıvılcım) kadraj dışında, yalnız sonucu görünür: gövde sarsılır, ışık söner ya da kırmızıya döner, katı parça süzülür. Araç uzakta yalnız ışık noktasıdır (F1 B7-B8 · HELMET C02 · C04 · C57) | Olay kesmeyle sınırlanır (BILINEN §B 4: kısaltmanın etkisi HİPOTEZ) | Dışarıda ses yok; olay gövdeden ya da kask içinden duyulur, kurguda. Model sesi atılır (DEPO: BILINEN §B 3) | DEPO: T03 22/49 · parçacık 38 satırın 15'i 🅐 (yasak yazılıyken çıktı) · çözüm UYGULAMA | — |

**Süre sütunu:** hiçbir an türü için ölçülmüş en kısa okunur süre yok; hepsi `—`. Ham araştırmadaki "saniyenin altında
okuma" ve "≈1,4 alternasyon" doğrulanmadı (§5). HELMET planındaki süreler uygulamadır: insert 1,5-3 s · sürekli temas ≤3 s ·
temas değişmezken ≤8 s.

---

## 2 · TEMEL İLKELER

| # | İlke | Kanıt | Sınır · karşı vaka |
|:--:|---|---|---|
| 1 | **Öncesi → kesme → sonrası.** Modelin bozduğu an üretilmez; öncesi ve sonrası iki ayrı çekimdir | ALGI: Levin & Simons 1997, Deney 2A: kesmede oyuncunun değiştiğini 40 kişiden yalnız %33'ü fark etti · ALGI (kuram): Swallow, Zacks & Abrams 2009, olay sınırında etkin bellek "boşalır". Bu kuramın iddiası; veri daha temkinli ve yalnız bakılan nesnede gösterildi · KIYAS: VideoPhy-2, en iyi açık model Wan2.1-14B zor eylemlerde %22 (tüm sette %32,6) · DEPO: ARIZA T01 | Kesme, iki ayrı üretimin küçük farklarını saklar. İstenen yeni durumu ise sonrası çekim açıkça göstermeli ve eylemin izini taşımalı (F1 B5 · T14) |
| 2 | **Temas başlangıç karesinde zaten kurulu; hareket temastan sonrasıdır** | UYGULAMA (04 R9) · goruntu-yonetmeni: "çekim listesi temas anını atlıyorsa video da onu istemez" | Tek başına yetmedi: THE_STOLEN_SKY S03 ve S58'de kurulu temas, büyük hareketli 10 s'lik çekimde bozuldu. İlke 5 ile birlikte uygulanır |
| 3 | **Çekim başına tek özne** | UYGULAMA · DEPO: T15 9/49 · THE_LAST_GATE PART2 00:24 ve 02:02, aralık cümlesi yazılıyken gövdeler birleşti (🅐) | İkinci kişi konum ya da mesafe bilgisi taşıyorsa kalır: küçük ve ayrık (HELMET C01 · C15 · C23) |
| 4 | **İki kişiye ayrı renk işareti** | UYGULAMA (HELMET: kırmızı ve mavi omuz bandı, bilekli eldiven, ip) · DEPO: THE_LAST_GATE PART3 01:32, altı kişiye tek beyaz giysi cümlesi → klon | Kimliği ayırır, fazla figürü önlemez: THE_STOLEN_SKY PART1 00:39 |
| 5 | **Sürekli temas kısa; temas sırasında hareket küçük** | UYGULAMA (F1 B1 ≤3 s · B3 ≤2 s insert) · DEPO: THE_STOLEN_SKY S03, 10 s'lik kavrama ve sendeleme → 00:34 kaynaşma | HELMET'te 6,6-8 s'lik temas çekimleri var (C33 · C35 · C46), ama yalnız temas değişmezken ve çizgi kabuğun arkasındayken. Sonucu ölçülmedi |
| 6 | **Durum değişimi kesmede** | KIYAS: T2V-CompBench dinamik nitelik bağlamada en iyi skor 0,0687, çoğu 0,005-0,025 (V8a) · ALGI: Levin & Simons · DEPO: 🅐5 · THE_LAST_TOW PART2 1:10 · THE_STOLEN_SKY PART2 02:53 | Her durum ayrı kare ister (ARIZA T05 · T09); metindeki durum merdiveni tutmadı |
| 7 | **Temas çizgisi bir kabuğun arkasında, kamera boş taraftan ¾** | UYGULAMA (F1 B1 · HELMET C03 · C10 · C30 · C33 · C39) | Sonucu ölçülmedi |
| 8 | **Promptta temas cümlesini ayrıntılandırmak önlemez** | DEPO: temas cümlesi 25 promptun 22'sinde yazılıyken 7 ölümcül hata (THE_COUNTED_TURN) · 14/14'te 6 🔴 (THE_DRY_ANCHOR) · 06.10 analizi: el-nesne 43 satırın 29'u 🅐 · KIYAS: T2VPhysBench'e göre fizik ipucu çoğu yasada işe yaramıyor, bazen zarar veriyor (V11a) | Yasak cümlesi de önlemedi: `no vapor` (THE_STATIC_VEIL S07) · `no dust hanging` (THE_LAST_TOW K32) · `Exactly 2 … no extra person` (THE_STOLEN_SKY S03) |

---

## 3 · ÖRNEK DİZİLER — üç çekim

Süreler HELMET planındandır, ölçülmedi. Dört dizide de vakumda görünür gaz ya da egzoz yok.

**A · El-nesne: kancayı takmak** (HELMET C50 · C51 · C54'ten sadeleştirildi)
```
Ç1  ÖNCESİ   yakın insert · sabit · Frames to Video. Başlangıç karesinde kırmızı bilekli eldiven kancayı zaten
             tutuyor; kancayı tırabzana götürür, tırabzana bir avuç kala çekim biter                     2,5 s
    KESME    tek "tık" bu karede (kurguda; vakumda gövdeden gelen ses)
Ç2  SONRASI  elsiz insert · aynı ölçek · Ingredients to Video. Kanca tırabzana takılı, hafifçe sallanıyor  2,5 s
Ç3  SONUÇ    yakın · ¾ önden. Öteki kişinin yüzü: gözleri yavaşça kapanır, omuzları iner                8 s
```
Takma anı hiç üretilmez: Ç1'de kavrama baştan kurulu, Ç2'de el yok.

**B · İki kişi teması: kask kaska** (HELMET C28 · C29 · C30)
```
Ç1  ÖNCESİ   geniş-orta · yandan · sabit. B dikmeden dikmeye A'nın arkasına geçer; ikisi ayrık          2 s
Ç2  ARA      insansız çekim: uzaklaşan kapsül. İki kaskın tok vuruşu bu çekimin 1. saniyesinde duyulur;
             temas görülmez                                                                          2 s
Ç3  SONRASI  yakın-orta · boş taraftan ¾ önden · sabit. A tek; solda B'nin kaskının flu kenarı A'nın
             kaskına dayalı. Çekim temas sürerken başlar, temas değişmez                              2,5 s
```
Temas kurulurken iki giysi aynı karede değildir; kurulu temasta da yalnız bir kişi nettir.

**C · Benzer iki figür: aynı yer, ayrı kareler** (HELMET C15 · C33 · C34)
```
Ç1  KONUM    geniş-orta · derinlik · sabit. Mavi bantlı A önde solda, kırmızı bantlı B uzakta sağda küçük  4,5 s
Ç2  A TEKLİ  yakın · ¾ önden. A; sağ kenarda B'nin flu kask kabuğu. B konuşur, kadraj dışında;
             A dinler, ağzı görünmez                                                                  6,6 s
Ç3  B TEKLİ  yakın · ¾ önden. B; sol kenarda A'nın flu kaskı. Aynı kadraj ilişkisi, ters taraf         3,8 s
```
Kasklar temastaysa çizgi flu kabuğun arkasında kalır. Konuşanı ses odası ayırır.

**D · Durum değişimi: el koldan çekilir** (HELMET C32 · C47 · C48; C32 ile C47 arasında başka çekimler var)
```
Ç1  DURUM A  sabit insert. Kırmızı bilekli eldiven açık kumanda kolunun üstünde, kıpırdamıyor
             (durum karesi KOL_elde)                                                                  1,5 s
Ç2  TETİK    yakın · önden. Aynı kişinin yüzü: çenesi gevşer, gözleri dikmede kalır                    6 s
    KESME    ayrılma burada olur. Değişimin sesi varsa bu karede; yoksa ortam yatağı kesmeden geçer (J/L)
Ç3  DURUM B  sabit insert, Ç1'in kadrajı. Eldiven koldan bir avuç uzakta süzülür, kol boş
             (durum karesi KOL_elsiz)                                                                 6 s
```

---

## 4 · SEÇENEK — EVA kamera alışkanlığı (kanıtsız, yönetmenin seçimi)

04 R9: NOT · PROB; SMOKE_TEST'te satırı yok. Delta bütçesindeki "en çok bir basit kamera hareketi" ile uyumlu (teknik-danisman).
- **Kilitli dış istasyon kamerası:** kirişe ya da gövdeye sabit, geniş, kişiler küçük; kamera hiç kıpırdamaz. Bu ölçekte
  el teması okunmaz (HELMET C16 · C28). Bedeli: iki kişi aynı karede kalır (T15); yüz ve tepki görünmez.
- **Kask POV'u:** kask kenarı kadrajda, geniş açı. Bedeli: kişinin kendi elleri kadraja girer, yani T01 geri gelir. Model
  vizöre HUD ve yazı basmaya da yatkın (BILINEN §B 2: "vizörde HUD"). Sarsıntı istenmez (§5).

---

## 5 · ÇÜRÜTÜLENLER — çözüm diye yazılmaz

Süzmede **RED**:
- "Veo 3.1 %35 · Sora 2 %40 kütle merkezi doğruluğu": PhysicsMind'da bu, kaldıraç denkleminde son durum doğruluğu. Üç
  seçenekli görevde şans zaten ≈%33 (V5 ◐).
- "Wan2.2 %47,7 eylem başarısı": makalede yok; 47 civarı sayılar değerlendirici modele ait (V6a ❌). Doğru sayı:
  Wan2.1-14B tüm sette %32,6, zor sette %22 (V6b).
- Ağır yükü sırt iticisinden gaz püskürtmesiyle anlatmak: vakumda görünür egzoz deponun bilinen arızası
  (THE_LAST_GATE PART4 01:14 · ARIZA T03).
- Fiziksel olayın doğal sonucunu prompta yazınca fiziğin düzelmesi: T2VPhysBench'e göre ipucu çoğu yasada işe yaramıyor,
  bazen zarar veriyor (V11a ❌ · 04 R6).

Süzmede **NOT** (kanıtsız ya da başka bir şeyi ölçüyor):
- Bozulmayı kamera sarsıntısı ve hareket bulanıklığıyla gizlemek: kanıtsız. Üstelik TARAMA T14 kamera kaymasını ayrıca arar.
- "%23-47 atılma oranı fizik ihlalidir": Morpheus'ta bu, analize giremeyen videoların atılma oranı (V7).

Ham raporda geçen, süzmede **doğrulanmayan** (kanıt sütununa girmedi):
- kesmeden sonra "saniyenin altında" okuma süresi · "≈1,4 alternasyon" · "~20 s altı kesintiler";
- benzer giysilerde kimlik sızıntısı için T2V-CompBench atfı. Yalnız dinamik nitelik satırı doğrulandı (V8a ◐);
  "%93,18 insan uyumu" bulunamadı (V8b);
- Smith'in dikkat kuramı ve Kuleshov etkisi: ham raporda gerekçe olarak geçiyor, kaynağı açılmadı;
- "temas başlangıç karesinde kuruluysa 8 s'lik çekim bozulmaz": ham raporun kendisi de "doğrulanamadı" diyor. Depodaki karşı
  vaka THE_STOLEN_SKY S03.

---

## 6 · HATTA NEREDE KULLANILIR — AGENTS §3 · §4

- **Faz 3 · yonetmen:** risk sütunu `T kodu → çözüm` biçimindedir (yonetmen.md kural 4); çözüm bu tablonun kadraj ve kurgu
  sütunundan seçilir. Kritik olay çekimlere bölünür (kural 3).
- **Faz 3 ve 5 · teknik-danisman:** risk sütunundaki çözüm buradakiyle uyuşuyor mu, promptta riskli an hâlâ isteniyor mu?
- **Faz 5 · goruntu-yonetmeni:** başlangıç karesi temasın kurulu hâlini ya da temasın öncesini gösterir; video promptu
  yalnız temastan sonraki hareketi yazar. Durumu değişen her nesnenin her durumu ayrı karedir.
- **Faz 7 · devamlilik:** her durum karesi kendi durumunu taşıyor mu (renk işareti, kanca, kol)?
- **Faz 7 · ret döngüsü:** teknik-danisman hatanın doğduğu yeri seçer (AGENTS §3). Yer `hareket` ise ve iki deneme aynı
  sebeple bozulduysa (§4), "çekim yaklaşımını değiştir" adımının seçenekleri bu tablodan gelir: anı kesmeyle atla · tek özneye
  indir · durumu kesmeye taşı · olayı sonucuyla göster. Prompta cümle eklemek yaklaşım değişikliği sayılmaz (ilke 8).
- **Faz 8 · kurgucu:** kesme, temasın ya da durum değişiminin karesine konur; bilinen hataya ±0,3 s'den yakın kesilmez.
  Temas sesi ve oda değişimi kesmeye bağlanır (kurgucu kural 7: J/L köprüsü).
