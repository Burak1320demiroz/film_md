# ✋ HAREKET VE EFOR KILAVUZU — modelin yapabileceği eylemi, yapabileceği anda yaz

> **Ne için:** ekranda görülen ölümcül hataların en kalabalık iki türü el-nesne kaynaşması (T01, 21/49 film) ve okunmayan efor (T02, 24/49).
> Hatta bunların **kadraj ve kurgu** çözümü var (`GOSTERIM_COZUMLERI`); bu kılavuz **prompt dili** tarafını verir: temas ne zaman kurulur, hangi
> eylem yazılır, efor ve yerçekimi hangi kelimelerle, hangi kelime kadraja sızar.
> **Kim okur:** goruntu-yonetmeni (F3p · F5) · yonetmen (F3, eylem seçimi) · teknik-danisman · devamlilik (F5 denetim).
> **Kaynak:** eski 11 kılavuzun (~3.850 satır) süzmesi → `ARASTIRMA/20_SUZME_HAREKET_PROMPT_MODEL_20261021.md` (48 madde). Sahip kararı 21.10.2026.
> Tamamlayıcı (burada tekrarlanmaz): `PROMPT_HATA_ATLASI` A01-A14 · `GOSTERIM_COZUMLERI` · `UZAY_FIZIGI_GORUNTU_KILAVUZU` · `goruntu-yonetmeni`
> görsel/video kuralları ve 8 soru · `KARAKTER_VE_DIYALOG_KILAVUZU` §3 (beden, kalıntı).
> **Tarih:** 21.10.2026.

**Kural türü (AGENTS §1b):** **KANITLI** satırlar en az iki filmde kayıtlı vakaya ya da çok filmlik ölçüme dayanır; yazar uygular. **HİPOTEZ**
satırlar ölçülmedi; yazar uygular ya da tek cümle gerekçe yazar. Eski ölçümler yapay zekâ QA raporlarından sayıldı; yön gösterir.

---

## 1 · Temas — ne zaman, hangi cümleyle

- **Temas ya başlangıç karesinde kuruludur ya klibin ilk 2 saniyesinde kurulur — KANITLI.** 34 filmde temas bulgularının klip içi dağılımı:
  0-2 s **%5,9** · 2-4 s **%19,4** · 4-6 s %15,2 · 6-8 s %12,1 · 8-10 s %13,8. Uzanma-tutma hareketi vuruş planında 2-4 s'ye düşmez.
  Durum cümlesi kurulu hâli verir — HİPOTEZ: `she is already gripping the lever` (0. saniyede tutuyor) ↔ `she grips the lever` (klip bir uzanmayla açılır).
- **Temas cümlesi yazılmaz — KANITLI.** El kadrajda olan 617 sahnede `Hand-to-surface contact keeps a clear boundary, no merging…` cümlesi
  **yazılıyken** bulgu oranı %11,8, **yazılmamışken** %5,6 (gözlemsel; atlas A03 "önlemez" ile aynı yön, daha güçlü). Olumsuz kavram
  modelde o kavramı çağırıyor olabilir. Çare cümle değil zaman (yukarı) ve kadraj (`GOSTERIM` §1).
- **Nesne-nesne geçişi ayrı bir sınıftır — KANITLI.** 81 geçiş bulgusunun 26'sında el yok: kayış metal bacaktan, karabina rayın içinden, halat
  abajurdan geçti (DRY_ANCHOR · COUNTED_TURN · LEANING_ROOM · STILL_SWARM · LOOK_UP). İki katı cismin birbirine geçmesini isteyen ifade yazılmaz
  (atlas A04); ip, kayış ve kanca da temas anıdır: aynı zaman kuralı uygulanır.
- **Ara katman** — HİPOTEZ: iki cismin arasına adlandırılmış, zıt renkli bir parça koy
  (`the off-white glove closes on the grey cuff, a bright steel ring between the two`).

---

## 2 · Eylem seçimi — modelin yapabileceği boy

- **Mikro → makro — KANITLI** (el-nesne kaynaşması 9 film · kalın eldivenle klavye tuşlama STOLEN_SKY · tokada eriyen eldiven SLOW_RAIN).
  Parmak ucu işi gövdenin yaptığı bir eyleme büyütülür; olay aynı kalır, ölçeği değişir. Çekim listesinde (F3) seçilir:

| ✗ Mikro (yazılmaz) | ✓ Makro (aynı olay) |
|---|---|
| parmakla toka, mandal açmak | iki elle büyük bir kilit koluna ağırlık vermek |
| tornavidayla vida sıkmak | iki elle levyeyi panel aralığına sokup omuzla kanırtmak |
| ince kablo bağlamak | kalın zırhlı bir fişi iki elle yuvasına itmek |
| klavyede tuşlamak | eldivenli avuçla büyük bir panele basıp tutmak |
| küçük düğme çevirmek | büyük bir çarkı iki elle, gövdeyle çevirmek |

  Makro nesne bedene göre boylanır (`a lever as long as her forearm`) — HİPOTEZ. Alet tek rijit parçadır; parmakların alet üzerindeki hareketi
  tarif edilmez — HİPOTEZ. Olay gerçekten küçük bir el işiyse iş kadrajdan çıkar: öncesi bir çekimde, sonucu sonrakinde.
- **Yürüme platosu — KANITLI** (SLOW_RAIN S17-S24: planda kesme, kazıma, saplama vardı, ekranda peş peşe yürüme · ADAY-95 · H03 24/52).
  Model çözemediği işi yürümeye çevirir. Zor iş çekiminde yürüme fiili yazılmaz (`walks · approaches · steps toward · moves to`); alt gövde
  zemine kilitlidir, hareket gövde, omuz ve koldan gelir. Görev tek fiille özetlenmez (`repairs the panel`); evresi yazılır.
  Duruşlar — HİPOTEZ: omuzla panele yüklenmek · iki elle levyeye asılmak (bacaklar geride gergin) · diz çöküp iki elle tutunmak · omuzla kapıya dayanmak.

---

## 3 · Efor — beden öder

Sabitlik sözcüğü (`smoothly`, `at the same rate`) ve zarf (`forcefully`) eforu siler (atlas A01 · A02). Bunlara eklenenler:

- **Ağır çekim tuzağı — KANITLI** (film_dogrula DERS Y10 "slow birikimi"). `slowly`, `gradually`, `in slow motion` efor cümlesinde bütün sahneyi
  yavaşlatır: toz, kumaş, arka plan da yavaş akar. Yavaşlık yazılmaz, **duraksama** yazılır (`halts, holding the strain, then pulls again`).
- **Dört parça** — HİPOTEZ (sorunu D206 yedi filmde doğruluyor; bu biçim sınanmadı):

```text
DESTEK     both boots braced against the hatch rim
GÖVDE      she leans back into the lever, hips low
İŞARET     her shoulders drop into the second pull          (2-3 tane, aynı yöne çalışan)
DURAKSAMA  the lever stops dead; she holds the strain, then pulls again
```

- **Sonuç sayısı yazılmaz** (`the lever moves 4 cm in the first second`): model pürüzsüz yörünge çizer, beden ağırlıksız çıkar — HİPOTEZ.
- **Direnç nesnede:** `the seized wheel` · `jammed` · `bound by frost` · `the hinge stiff with frozen grit`; zayıf: `opens` · `slides` · `easily` — HİPOTEZ.
- **Asimetrik yük tutmaz:** "sağ kol çeker, sol kol gevşek" iki kolu senkronlar; işaretler aynı yöne çalışır — HİPOTEZ.
- **Giysi de yüktür:** `thick pressurized gloves, the fingers stiff and slow to close`; çevik parmak işi yazılmaz — HİPOTEZ.
- **Efor giysinin yüzeyinde yazılır:** `the sleeves pull tight at the elbows` · `the suit creases deep across the shoulders`.
  ✗ `tendons stand out through the glove` — HİPOTEZ *(vaka: D175, eldiven yerine çıplak ön kol çizildi)*.

---

## 4 · Yerçekimi ve fizik

- **İki rejim aynı kadrajdaysa ayrım mekanik sebebe bağlanır — KANITLI** (LOOK_UP · GREEN_CEILING · PAYLOAD · LEANING_ROOM). Ayıran işaretin
  görünmesi (BILINEN_TUZAKLAR §B 7) fiilin sebebiyle yazılır:
  ✗ `an astronaut walks through the bay while tools float around him`
  ✓ `He locks each boot to the floor grating before the next step and pulls himself forward by the rail, while the loose tools drift behind him.`
- **Novumun taşıyıcı olgusu her promptta sayıyla kilitlidir — KANITLI** (5 film: "filmin ana malzemesi kilitsiz" — yüzen panel filminde parçacık
  cümlesi 14 promptun 2'sinde → 6 bulgu). Filmin kendi olgusu neyse (yüzen levha, tel, ivme) davranışı pozitif ve ölçüyle yazılır, rakamla değil:
  `each panel keeps a slow constant drift of about one panel-width every four seconds`. Bkz. `HIKAYE_YAPISI_KILAVUZU` §1.
- **Düşük yerçekiminde düşüş fiili** — HİPOTEZ *(vaka: SLOW_RAIN, kaza düşüşü 4,27 m/s², filmin kendi değeri ~3,7)*: `falls fast` · `free fall` ·
  `plummets` · `crashes down` 1 g çağırır. Düşüşün şekli ve süresi yazılır: `drops toward the ice in a long, low arc, more than a second in the air`.
- **Yerçekimi rakamla değil karşılaştırmayla:** promptta rakam yazılmaz (`UZAY_FIZIGI` §1: model hızı sayıdan anlamaz, rakam kadraja basılabilir) ve sayının faydası
  gösterilemedi (BILINEN_TUZAKLAR §B 7); hız insan ölçüsüyle verilir: `a dropped glove takes a full second to reach the ice` — HİPOTEZ.
- **Çarpışma üç evrede:** yaklaşma → temas (`its steel runner strikes the rock face and stops dead, the rock unmoved`) → iz (ikincil nesne) — HİPOTEZ.
- Toz ve parçacık davranışı yazılmaz (atlas A12); "parçacığa yön ver" eski önerisi bu ölçümle düştü.

---

## 5 · Kadraja sızan kelimeler

- **`tripod` yazılmaz — KANITLI** (SLOW_RAIN S14 · STOLEN_SKY PART1: iki filmde plansız tripod kadraja girdi, ikisinin kamera satırı da
  `on a fixed locked-off tripod` diyordu). ✓ `a locked-off camera`. Değişiklik bedava: kurulum lens, yükseklik ve açıdan kurulur.
- **Zaman bağlacı yok** — HİPOTEZ: `Next scene` · `After that` · `Following shot` dekoru yeniden kurdurur; `Suddenly` sarsıntı, parlama ekler.
  Süreklilik şimdiki zamanlı durum cümlesiyle taşınır.
- **Eşya envanteri pozitif:** `the only equipment in frame is the folded sled and the steel canister at her boots`; yasak listesi yazılmaz — HİPOTEZ.
- **Sabit nesnenin yeri de kimliğidir:** `the folded sled lies flat on the ice behind her, its tow strap taut to her harness` — HİPOTEZ
  *(vaka: SLOW_RAIN, kızak bir çekimde yerde, sonrakinde sırtta, sonra yine yerde)*.

---

## 6 · Gizli geçiş — iki deneme birleşirken — HİPOTEZ

`SECIM_VE_KURGU` §6'nın üçüncü yolu ("aynı çekimin iki denemesini gizli kesmeyle birleştirmek") tasarlanabilir: bir deneme bir perdeyle (kadrajdan
geçen nesne, hızlı bir gövde dönüşü, kameraya yaklaşan omuz) kapanır, öteki aynı perdeyle açılır; kesme perdenin içine düşer. Üç şart birlikte
tutmazsa illüzyon çöker ve düz kesme daha iyidir: **ışık yönü aynı · kir, toz ve hasar aynı · hareket hızı aynı.** Dikiş `kareler.py dikis` ile bakılır.

---

## 7 · Kim, ne zaman

| Faz | Kim | Bu kılavuzdan |
|---|---|---|
| F3 | yonetmen | §2 mikro → makro ve yürüme platosu çekim listesinde seçilir · §4 novum olgusunun çekimleri |
| F3 | teknik-danisman | §1 temas zamanı · §2 parmak ucu işi, yürümeye dönecek zor iş · §4 iki rejim |
| F3p · F5 | goruntu-yonetmeni | §1 temas ilk 2 s / kurulu, temas cümlesi yok · §3 efor dört parça, `slowly` yok · §4 · §5 `tripod` yok |
| F5 | devamlilik | §1 vuruş planında temas 2-4 s'ye düşüyor mu · §3 · §5 sızan kelime · sabit nesnenin yeri |

---

> **Ölçüm:** bu kılavuzla yazılan ilk filmin QA'sında — temas bulguları klibin hangi saniyesinde (§1) · zor iş yürümeye döndü mü (§2) · tripod
> çıktı mı (§5) · efor çekiminde sahne yavaşladı mı (§3). **Bu dosya ne zaman değişir:** yalnız yeni kayıtlı vakayla ya da sahip kararıyla.
