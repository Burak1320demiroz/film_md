# 🎬 RAIN_THIEF — Yağmur Hırsızı

```
FILM           RAIN_THIEF
FORMAT         yatay 16:9
HEDEF_SURE     4:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/RAIN_THIEF/
URETIM         sahip planı: başlangıç karesi GPT Image → aynı kare image-to-video 10 s (plan §7 "Uygulama") · replikler videoda oyunculuk ve ağız ipucu, temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması": modelin ses ürettiği varsayılmaz) · QA Gemini uygulaması
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `REPLIK` ve `MUZIK` varsayılan **var**: filmlerde akıcı diyalog, ses ve efekt olur (sahip kararı, 06.10.2026).
> `yok` yalnız hikâye bunu istiyorsa, gerekçesi §5'in altına yazılarak.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.
>
> **KAYNAK: `RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md` (sahibin verdiği plan, 19.10.2026, birebir; düzenlenmez).**
> **Varsayılan (sahip 18.10.2026, BLACK_ACCORD: "plandan asla dışarı çıkma"; aksi söylenmedikçe sonraki planlarda da geçerli):** olay, sıra,
> kadraj, özne, eylem, nesne durumu, 20 replik, ses davranışı, kapak ve yayın metni **planın kendisidir**. Fable'ın eklediği yalnız biçimdir:
> sütunlar, referans numaraları (R01→1 … R09→9), §5 saniye/süre tahmini, kaynak sütunu (plan §7 "ekran dışı cevap"), §6 tablo düzeni.
> Hat kuralıyla plan çatışırsa: SÖZLEŞME/ARAÇ (film_dogrula M) yalnız biçim olarak uygulanır; HİPOTEZ/TERCİH plan lehine bırakılır
> (`NOTLAR.md` KARARLAR); plan içi çelişki sahibe sorulur (`ODA/DURUM.md` SAHİP CEVAPLARI).
> Faz 1-4 ajan turu açılmadı (plan = seçim, tretman, çekim listesi; THE_FURNACE_GATE · BLACK_ACCORD yolu; `ODA/DURUM.md` AŞILAN KAPILAR).

---

## 1. HİKÂYE

```
LOGLINE   Yağmurun yalnızca zenginlerin kapalı bahçelerine verildiği bir uzaylı pazarında küçük bir hırsız, çaldığı hava kontrol çekirdeğini satıp kaçmak yerine herkes için bir yağmur çevrimi başlatmayı seçer.
AMAÇ      Kett önce çekirdeği satıp kendine gemi almak ister (C01, C05: "I was going to sell it. Buy a way out."); C06'dan sonra çekirdeği kuledeki yuvaya takıp mavi çarkı çevirmek (C07 talimatı, C18 yuva, C22 çark).
ENGEL     Vorr'un takibi (C02, C08, C12 geçidi kapatır, C16 paralel merdiven, C19 platform, C20 ponçodan yakalar) · kamusal dağıtım kapalı: kuru pazar, ücretli musluk, camın arkasındaki özel yağmur (C03, C04, C10).
KARAR     C06 — Kett sola, kalkan kaçış gemisine değil sağdaki mavi borulara, hava kulesine yönelir: "Let it. I'm changing the weather."
SONUÇ     C22 çark son konuma döner, kilide oturur; C23 kuru pazar yağmur alır, Tula'nın boş fincanı dolmaya başlar; C24 Vorr ponçoyla durur, avucunu yağmura açar.
BEDEL     kaçış gemisi ve onun aldırdığı yeni hayat (C11: gemi uzaklaşır, biniş pulu cebe girer) · ponço (C21, Vorr'un elinde kalır) · sahne 11 · 21
TEK SORU  Kett, Vorr yetişmeden çekirdeği yuvaya takıp mavi çarkı çevirebilecek mi?
SEÇİM     sahip planı (F1 aday turu yok) · 19.10.2026 · gerekçe: RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md
SAHİP     ONAY (planın kendisi) · 19.10.2026
```

## 2. TRETMAN

<!-- sahne başına bir satır; her satır öncekinden doğar (seçim ya da başarısız deneme) -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | Çalınmış hava: Kett kuru çeşmenin önünden koşar; sağ elindeki saydam çekirdeğin içinde küçük bir şimşek parlar. Arkada dev bir muhafızın ağır ayak sesleri yaklaşır. | Ponço kapalı; çekirdek sağ elde; hava kuru. |
| S2 | 0:10–0:20 | Takipçi: Vorr, kalabalığın açtığı koridorda durup Kett'in arkasından seslenir. | Vorr silahsız; Kett ekran dışı sağda. |
| S3 | 0:20–0:30 | Dünyanın kuralı: Kett aşağıdaki kuru pazarı geçerken kamera, yukarıdaki mavi su rezervuarını ve yalnızca kapalı özel bahçelerde çalışan yağmuru gösterir. | Kamusal alan kuru, özel sera ıslak; kaçış solda, kule sağda. |
| S4 | 0:30–0:40 | Bir damlanın bedeli: Yaşlı Tula boş fincanını tek damla satan bakır sayacın altına tutar. Kett onun yanında yavaşlar. | Tek saksı ve tek fincan kurulur; çekirdek sağ elde. |
| S5 | 0:40–0:50 | Hırsızın durması: Kett sol başparmağıyla küçük yan valfi yoklar. Bir damla saksıya düşer; çiçeğin tek soluk yaprağı renklenir. | Çekirdek sağlam; yan test valfi kapanır; çiçekte bir yaprak renklenir. |
| S6 | 0:50–1:00 | Kaçıştan vazgeçiş: Mara gemiyi işaret eder. Kett sola kaçmak yerine sağdaki mavi borulara yönelir. | Kett kuleyi seçer; Mara tezgâhta; çekirdek sağ elde. |
| S7 | 01:00–1:10 | Çözümün kurulması: Mara mavi borunun yukarıya giden hattını işaret eder; tezgâhının tente kolu da kadrajda kalır. | Mara'nın bilgisi ve tente kolu önceden gösterilir. |
| S8 | 01:10–1:20 | Kuru mizah: Vorr tezgâha ulaşır. Mara, Kett'in rotasını söylemeden sakin biçimde cevap verir. | Mara yerini terk etmez; Vorr Kett'in çatı rotasını görür. |
| S9 | 01:20–1:30 | Pazarın üstü: Kett dış yüzeyinde sabit basamaklar olan mavi servis borusuna tırmanır; çekirdek sağ elde korunur. | Kett 6 m çatı seviyesine çıkar; çekirdek sağ elde. |
| S10 | 01:30–1:40 | Yağmur zaten var: Kett, camın öte yanında yağmurla yıkanan lüks bitkilere bakar. Dışarıdaki çatısı toz içindedir. | Yağmurun yokluğu değil, dağıtımın kapalı oluşu anlaşılır. |
| S11 | 01:40–1:50 | Bedelin görünmesi: Kett kaçırdığı gemiye bakıp kemerindeki küçük turuncu biniş pulunu cebine iter. | Biniş pulu cebe girer ve tekrar kullanılmaz; gemi gider. |
| S12 | 01:50–2:00 | Çatıda yüzleşme: Vorr'un pazar dış cephesindeki metal merdivenden daha kısa yoldan geldiği görülür; çatı geçidini kapatır. | Vorr'un yetişmesi merdivenle açıklanır; alternatif mavi tente rotası görünür. |
| S13 | 02:00–2:10 | İlk kaçış hamlesi: Kett yakındaki eğimli pas turuncusu tente üzerinden kayıp bir alt seviyedeki servis sahanlığına iner. | Kett alt servis sahanlığında; ponço sağlam; çekirdek sağ elde. |
| S14 | 02:10–2:20 | Pazar yardım ediyor: Aşağıda Mara, önceden gördüğümüz pirinç kolu tek hamlede indirir; kendi güçlendirilmiş tentesi uzamaya başlar. | C07'de kurulan tente sistemi devreye girer; Mara tezgâhta. |
| S15 | 02:20–2:30 | Mavi köprü: Tam açılmış, gergi kablolu mavi teslimat tentesi iki servis sahanlığını birleştirir. Kett karşı tarafa geçer. | Kett kule tarafındaki sahanlığa ulaşır; mavi köprü bağlı kalır. |
| S16 | 02:30–2:40 | Takip henüz bitmedi: Vorr kendi ağırlığını taşımayacak tenteye girmek yerine paralel demir servis merdiveninden kuleye yönelir. | Vorr demir merdivenden gelir; Kett'e yetişmesi mümkün bir rota gösterilir. |
| S17 | 02:40–2:50 | Manzaranın zirvesi: Kett hava kulesinin üst platformuna çıkar. Önünde çekirdeğe uyan üç oluklu yuva ve büyük mavi el çarkı vardır. | Yuva ve mavi çark net; kurgu çözümü C07'deki talimatla aynı. |
| S18 | 02:50–3:00 | Çekirdek yerine: Kett çekirdeği sağ eliyle uyumlu yuvaya oturtur. Üç gümüş kaburga yuvadaki oluklara denk gelir. | Çekirdek C18'den finale kadar yuvada; Kett'in elleri artık boş. |
| S19 | 03:00–3:10 | Son engel yaklaşır: Vorr, kurulan demir merdivenin son basamaklarından platforma çıkar. | Vorr fiziksel olarak platformda; çekirdek yuvada; çark kapalı. |
| S20 | 03:10–3:20 | Yakalanma: Vorr sağ eliyle Kett'in ponçosunun arka yakasını kavrayıp onu mavi çarka varmadan durdurur. | Vorr yalnız ponço kumaşını tutar; boyna/el bileğine temas yok. |
| S21 | 03:20–3:30 | İlk sahnedeki toka: Kett göğsündeki beyaz tokayı açar. Ponço Vorr'un elinde kalır; Kett koyu turkuaz tulumuyla serbest kalır. | C21 sonunda Kett ponçosuz; ponço Vorr'un sağ elinde; çekirdek yuvada. |
| S22 | 03:30–3:40 | Yağmur açılır: Kett iki eliyle büyük mavi çarkı son noktasına kadar çevirir. Mavi borulara birer birer su dolar. | Çark açık konumda kilitlenir; genel yağmur dağıtımı açılır; Kett ponçosuz. |
| S23 | 03:40–3:50 | Uzaylıların yağmuru: Yağmur kuru pazara ulaşır. Tula fincanını kaldırır; arkasındaki farklı türler suyu şaşkınlıkla karşılar. | Pazar ilk kez ıslanır; Tula'nın fincanı dolmaya başlar; mevcut çiçek canlanır. |
| S24 | 03:50–4:00 | Son espri ve kapanış: Kett çarkın öteki yanında nefeslenir. Vorr elindeki ponçoyu gevşetip diğer avucunda yağmuru hisseder. | Kett ponçosuz; ponço Vorr'da; çark açık ve çekirdek yuvada; yağmur sürer. |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Kett — başlangıç kostümü (plan R01; hardal ponço + beyaz oval toka + koyu turkuaz tulum) | `1.KETT_v1.png` | v1 | | ⬜ | C01 C03 C04 C05 C06 C09 C10 C11 C12 C13 C15 C17 C18 C20 C21 |
| 2 | Kett — C21 sonrasındaki kostüm (plan R02; R01 üzerinden düzenleme, yalnız ponço ve toka çıkar) · SAHİP İSTİSNASI 19.10.2026 (özne başına tek sayfa kuralına istisna: plan iki dosya ister) | `2.KETT_TULUM_v1.png` | v1 | | ⬜ | C21 C22 C24 |
| 3 | Mara — sokak aşçısı (plan R03) | `3.MARA_v1.png` | v1 | | ⬜ | C06 C07 C08 C14 C23 |
| 4 | Vorr — hava şirketinin muhafızı (plan R04) | `4.VORR_v1.png` | v1 | | ⬜ | C02 C08 C12 C16 C19 C20 C21 C24 |
| 5 | Tula — çiçek satıcısı (plan R05; elinde düz bakır fincan) | `5.TULA_v1.png` | v1 | | ⬜ | C04 C05 C23 |
| 6 | M1 — kuru pazar ve dünya coğrafyası (plan R06) | `6.PAZAR_v1.png` | v1 | | ⬜ | C01 C02 C03 C04 C06 C07 C08 C14 C23 |
| 7 | M2 — çatılar ve iki takip rotası (plan R07) | `7.CATILAR_v1.png` | v1 | | ⬜ | C09 C10 C11 C12 C13 C15 C16 |
| 8 | M3 — hava kulesinin üstü (plan R08) | `8.HAVA_TACI_v1.png` | v1 | | ⬜ | C17 C18 C19 C20 C21 C22 C24 |
| 9 | Tek çekirdek (plan R09) | `9.CEKIRDEK_v1.png` | v1 | | ⬜ | C01 C05 C09 C13 C15 C17 C18 C22 |

```
Plan dosya adları → hat adları: R01_KETT_COAT → 1.KETT · R02_KETT_NO_COAT → 2.KETT_TULUM · R03_MARA → 3.MARA · R04_VORR → 4.VORR ·
R05_TULA → 5.TULA · R06_MARKET → 6.PAZAR · R07_ROOFS → 7.CATILAR · R08_WEATHER_CROWN → 8.HAVA_TACI · R09_WEATHER_CORE → 9.CEKIRDEK.
Plan: önce 1, sonra 1'in üzerinden düzenlemeyle 2 (ponçosuz Kett sıfırdan başka yüz olarak üretilmez). Dokuz referans her görüntüye topluca yüklenmez.
SHA-256: shasum -a 256 ~/film_medya/RAIN_THIEF/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
ÖZNE BAŞINA TEK SAYFA: bir karakterin açıları, yüz yakını ve durum değişimleri aynı görselde paneldir; "SELA_yuz",
"SELA_arka" gibi ikinci dosya açılmaz (film_dogrula hata). Yeni panel gerekirse sayfa yeniden üretilir, sürüm artar.
```

### KİMLİK CÜMLELERİ (16.10.2026 · F3p'de goruntu-yonetmeni yazar, pilot yoksa F5 G01 · Görsel promptta BİREBİR)

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | Kett · yüz + beden | Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. |
| 1 | Kett · eller + bacaklar | Exactly two arms, two legs and three fingers on each hand. |
| 1 | Kett · giysi (ponço + toka + tulum) | Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. |
| 1 | Kett · ayaklar | Broad padded feet. |
| 1 | Kett · işaret † | The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. |
| 1 | Kett · eller (makro) † | Kett has cobalt-blue skin and three fingers on each hand. |
| 2 | Kett · ponçosuz yüz + beden † | The identical cobalt-blue skin, flattened head, two amber eyes, two folded ear fins, three fingers per hand and padded feet. |
| 2 | Kett · ponçosuz giysi † | Kett wears only the already established plain dark teal utility under-suit with one small belt pocket, with no poncho, no neck clasp and no body markings. |
| 3 | Mara · yüz + beden | Mara, an adult nonhuman street cook, one hundred seventy-five centimeters tall, coral-red skin with a subtly ridged head, four small dark eyes permanently arranged in a two-by-two square, one narrow vertical mouth below the eyes, a short rigid fan-shaped crest, no hair, no human ears. |
| 3 | Mara · kollar | Exactly two arms and two legs. |
| 3 | Mara · giysi | Indigo work clothes beneath a worn cream cook's apron, practical cloth belt, empty hands. |
| 4 | Vorr · yüz + beden | Vorr, an adult alien weather-company security officer, two hundred thirty centimeters tall, broad heavy basalt-dark body, block-shaped nonhuman face with mineral skin plates, two narrow pale-gold eyes and one small horizontal mouth. |
| 4 | Vorr · kollar + eller | Exactly two arms and two legs, five thick fingers per hand. |
| 4 | Vorr · giysi | Wears a dark brown practical uniform with rigid copper shoulder armor and heavy metal boots; no helmet, no cloak, no handheld weapon and no holster. |
| 5 | Tula · yüz + beden | Tula, an elderly adult nonhuman flower seller, one hundred twenty centimeters tall, broad pearl-lilac shell-ridged head, two dark oval eyes, one small mouth, a few short sensory filaments beneath the cheeks, no human hair or ears. |
| 5 | Tula · gövde + cüppe | Compact mature body with a slightly stooped adult posture, two arms and two legs, simple muted green robe. |
| 5 | Tula · fincan | Holds one plain small copper cup in both hands. |
| 6 | Pazar · genel | A bustling entirely alien open-air market stands on a dusty copper-built moon city. |
| 6 | Pazar · çeşme † | One dry copper fountain stands at the center of the market. |
| 6 | Pazar · çiçek tezgâhı † | At the lower right, a small flower stall holds one pale closed alien flower and a dry coin-operated water spout. |
| 6 | Pazar · yemek tezgâhı † | Adjacent to the flower stall, a food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. |
| 6 | Pazar · iskele † | At the far left, a dock holds one small orange commuter skiff. |
| 6 | Pazar · kule + rezervuar † | At the upper right, a copper weather tower is reached by blue service pipes and exterior iron stairs, and a huge transparent blue water reservoir curves above the district. |
| 6 | Pazar · sera + kuru yüzey † | Sealed luxury greenhouse terraces receive rain inside, while every public surface is dry. |
| 6 | Pazar · kalabalık † | Eight different nonhuman crowd silhouettes stand in layered depth. |
| 6 | Pazar · gezegen † | One pale planet with a thin gold ring hangs in the warm late-afternoon sky. |
| 6 | Pazar · yemek tezgâhı (çiçek tezgâhı kadrajda yok; C07 C08) † | A food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. |
| 7 | Çatılar · cam bahçe † | A sealed glass luxury garden has rain strictly inside. |
| 7 | Çatılar · pas turuncusu tente † | A short sloping reinforced rust-orange canopy drops less than two meters to a lower service landing. |
| 7 | Çatılar · mavi yük tentesi † | A separate folded blue delivery canopy on visible rails and tension cables is able to bridge two nearby service landings. |
| 7 | Çatılar · demir merdiven † | A continuous exterior iron service staircase provides a parallel route to the weather tower. |
| 7 | Çatılar · borular + yüzey † | Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. |
| 8 | Hava tacı · konsol + yuva + çark † | A single central copper console has one empty weather-core socket with three vertical alignment grooves, and one large blue manual handwheel directly beside it. |
| 8 | Hava tacı · konsol, dolu yuva (C20-C24; çekirdek yuvada) † | A single central copper console has one weather-core socket with three vertical alignment grooves, now holding the core, and one large blue manual handwheel directly beside it. |
| 8 | Hava tacı · kilit † | A simple physical end-stop latch sits on the wheel, with no electronic screen or readable writing. |
| 8 | Hava tacı · merdiven girişi † | An exterior iron staircase entrance is visible on the near left. |
| 8 | Hava tacı · borular + rezervuar † | Existing blue distribution pipes connect the console to the large transparent water reservoir arc overhead; closed public rain outlets are visible along the reservoir. |
| 8 | Hava tacı · zemin + korkuluk † | Low copper safety rails, dry metal floor, same pale ringed planet and warm late-afternoon light. |
| 9 | Çekirdek · gövde | A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. |
| 9 | Çekirdek · bulut | Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. |
| 9 | Çekirdek · taban | The base has three alignment ridges matching a mechanical socket. |
```
ORTAK GÖRÜNÜM (plan §6 "Ortak görünüm", birebir; plan: Görsel istemlerinin BAŞINA):
  Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character.
ORTAK HAREKET (plan §7, birebir; plan: Video istemlerinin BAŞINA):
  Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.
SAHNE DÜZENİ (plan §4): M1 pazar — kuru bakır çeşme, Tula'nın çiçek tezgâhı, yanında Mara'nın yemek tezgâhı; kaçış gemisi solda, kule ve mavi borular sağ yukarıda ·
  M2 çatılar — ≈6 m, cam özel bahçe, servis sahanlıkları; Kett'in tente rotası ve Vorr'un demir merdiveni aynı kuleye çıkar ·
  M3 hava tacı — ≈18 m tek platform, tek yuva, tek mavi çark; merdiven girişi görünür; rezervuar aynı yönde.
  C13 pas turuncusu kısa eğimli tente ≠ C14-C15 Mara'nın mavi yük tentesi (rayları ve gergi kabloları görünür).
DÜNYA KURALLARI (plan §4): su var, kamusal dağıtım kapalı (rezervuar baştan görünür, yağmur özel seralara satılır) · çekirdek fiziksel anahtar
  (minik bulut, tek damla veren yan test valfi; kırılmaz, canlı değil, çoğalmaz) · yuva + mavi çark = bir tam yağış çevrimi, kilide oturur, geri kapanmaz.
DEVAMLILIK (plan §8): ODA/DURUM.md değil, planın §8 tablosu esastır — çekirdek C01-C17 sağ elde, C18 yuvada → C24 · ponço C01-C20 kapalı, C21 Vorr'un sağ elinde ·
  mavi çark C18-C21 hareketsiz, C22 kilitlenir · kamusal pazar C01-C22 kuru, C23 yağmur başlar · Tula'nın tek fincanı, tek saksısı · Vorr silahsız ·
  turuncu gemi C03 C06 solda, C11 kalkar · aynı sıcak akşamüstü.
Kadrajda görünen her parça çekimin Görsel promptuna kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz (5/5 filmde
kimlik kayması, ARASTIRMA/16 Y1-Y3). İşaret: sayı + taraf + konum + "the only marking". Nesne: biçim + ölçü + taraf.
film_dogrula DERS Y2: referansı eklenen çekimde hiçbir parçası birebir geçmeyen özneyi gösterir (uyarı).
ORTAK GÖRÜNÜM cümlesi (varsa) yalnız film boyu değişmeyeni taşır: kimlik + doku/stil. Işık, su, gezegen, ses mekân ya da çekim
cümlesine gider (DERS Y6).
```

## 4. ÇEKİM LİSTESİ

| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Çalınmış hava: Kett kuru çeşmenin önünden koşar; sağ elindeki saydam çekirdeğin içinde küçük bir şimşek parlar. Arkada dev bir muhafızın ağır ayak sesleri yaklaşır. | Kett kuru çeşmenin önünden koşar; sağ elindeki saydam çekirdeğin içinde küçük bir şimşek parlar. Arkada dev bir muhafızın ağır ayak sesleri yaklaşır. | Alçak, yakın takip; Kett kadrajın solundan sağına koşar. | M1 pazar · Ponço kapalı; çekirdek sağ elde; hava kuru. | 10 | Frames to Video | plan pilotu (üretim sırası 1): çekirdek tutuşu — çekirdek sağ elde sabit, tek nesne, kırılmaz (T01 el-nesne) | 1.KETT · 6.PAZAR · 9.CEKIRDEK | G01 | ⬜ | — | — | — |
| C02 | Takipçi: Vorr, kalabalığın açtığı koridorda durup Kett'in arkasından seslenir. | Vorr, kalabalığın açtığı koridorda durup Kett'in arkasından seslenir. | Vorr'a hafif alttan orta yakın; arka planda bulanık iki farklı uzaylı. | M1 pazar · Vorr silahsız; Kett ekran dışı sağda. | 10 | Frames to Video | — | 4.VORR · 6.PAZAR | G01 | ⬜ | — | — | — |
| C03 | Dünyanın kuralı: Kett aşağıdaki kuru pazarı geçerken kamera, yukarıdaki mavi su rezervuarını ve yalnızca kapalı özel bahçelerde çalışan yağmuru gösterir. | Kett aşağıdaki kuru pazarı geçerken kamera, yukarıdaki mavi su rezervuarını ve yalnızca kapalı özel bahçelerde çalışan yağmuru gösterir. | Yüksek geniş; pazar, soldaki turuncu servis gemisi ve sağdaki hava kulesi aynı coğrafyada. | M1 pazar · Kamusal alan kuru, özel sera ıslak; kaçış solda, kule sağda. | 10 | Frames to Video | — | 1.KETT · 6.PAZAR | G01 | ⬜ | — | — | — |
| C04 | Bir damlanın bedeli: Yaşlı Tula boş fincanını tek damla satan bakır sayacın altına tutar. Kett onun yanında yavaşlar. | Yaşlı Tula boş fincanını tek damla satan bakır sayacın altına tutar. Kett onun yanında yavaşlar. | Tula ve Kett iki kişilik orta; bir soluk çiçek ve boş fincan ön planda. | M1 pazar · Tek saksı ve tek fincan kurulur; çekirdek sağ elde. | 10 | Frames to Video | — | 1.KETT · 5.TULA · 6.PAZAR | G01 | ⬜ | — | — | — |
| C05 | Hırsızın durması: Kett sol başparmağıyla küçük yan valfi yoklar. Bir damla saksıya düşer; çiçeğin tek soluk yaprağı renklenir. | Kett sol başparmağıyla küçük yan valfi yoklar. Bir damla saksıya düşer; çiçeğin tek soluk yaprağı renklenir. | Makro; çekirdeğin yan valfi, tek damla ve saksının bir kısmı. | M1 pazar · Çekirdek sağlam; yan test valfi kapanır; çiçekte bir yaprak renklenir. | 10 | Frames to Video | tek damla, tek yaprak renklenir; bulut kaçmaz, çiçek çoğalmaz (plan) | 1.KETT · 5.TULA · 9.CEKIRDEK | G01 | ⬜ | — | — | — |
| C06 | Kaçıştan vazgeçiş: Mara gemiyi işaret eder. Kett sola kaçmak yerine sağdaki mavi borulara yönelir. | Mara gemiyi işaret eder. Kett sola kaçmak yerine sağdaki mavi borulara yönelir. | Kett önde; Mara'nın tezgâhı arkada; sol uzakta gemi, sağ yukarı kule. | M1 pazar · Kett kuleyi seçer; Mara tezgâhta; çekirdek sağ elde. | 10 | Frames to Video | — | 1.KETT · 3.MARA · 6.PAZAR | G01 | ⬜ | — | — | — |
| C07 | Çözümün kurulması: Mara mavi borunun yukarıya giden hattını işaret eder; tezgâhının tente kolu da kadrajda kalır. | Mara mavi borunun yukarıya giden hattını işaret eder; tezgâhının tente kolu da kadrajda kalır. | Mara yakın; arkasında mavi boru, önünde pirinç tente kolu. | M1 pazar · Mara'nın bilgisi ve tente kolu önceden gösterilir. | 10 | Frames to Video | — | 3.MARA · 6.PAZAR | G01 | ⬜ | — | — | — |
| C08 | Kuru mizah: Vorr tezgâha ulaşır. Mara, Kett'in rotasını söylemeden sakin biçimde cevap verir. | Vorr tezgâha ulaşır. Mara, Kett'in rotasını söylemeden sakin biçimde cevap verir. | Vorr ön planda keskin; Mara arka planda yumuşak. | M1 pazar · Mara yerini terk etmez; Vorr Kett'in çatı rotasını görür. | 10 | Frames to Video | — | 3.MARA · 4.VORR · 6.PAZAR | G01 | ⬜ | — | — | — |
| C09 | Pazarın üstü: Kett dış yüzeyinde sabit basamaklar olan mavi servis borusuna tırmanır; çekirdek sağ elde korunur. | Kett dış yüzeyinde sabit basamaklar olan mavi servis borusuna tırmanır; çekirdek sağ elde korunur. | Yandan geniş; altta uzaylı kalabalığı, üstte köprü ve rezervuar. | M2 çatılar · Kett 6 m çatı seviyesine çıkar; çekirdek sağ elde. | 10 | Frames to Video | — | 1.KETT · 7.CATILAR · 9.CEKIRDEK | G02 | ⬜ | — | — | — |
| C10 | Yağmur zaten var: Kett, camın öte yanında yağmurla yıkanan lüks bitkilere bakar. Dışarıdaki çatısı toz içindedir. | Kett, camın öte yanında yağmurla yıkanan lüks bitkilere bakar. Dışarıdaki çatısı toz içindedir. | Cam boyunca yanal orta; Kett dışarıda, özel bahçe içeride. | M2 çatılar · Yağmurun yokluğu değil, dağıtımın kapalı oluşu anlaşılır. | 10 | Frames to Video | — | 1.KETT · 7.CATILAR | G02 | ⬜ | — | — | — |
| C11 | Bedelin görünmesi: Kett kaçırdığı gemiye bakıp kemerindeki küçük turuncu biniş pulunu cebine iter. | Kett kaçırdığı gemiye bakıp kemerindeki küçük turuncu biniş pulunu cebine iter. | Kett'e yakın; sol arka planda uzaklaşan turuncu gemi. | M2 çatılar · Biniş pulu cebe girer ve tekrar kullanılmaz; gemi gider. | 10 | Frames to Video | — | 1.KETT · 7.CATILAR | G02 | ⬜ | — | — | — |
| C12 | Çatıda yüzleşme: Vorr'un pazar dış cephesindeki metal merdivenden daha kısa yoldan geldiği görülür; çatı geçidini kapatır. | Vorr'un pazar dış cephesindeki metal merdivenden daha kısa yoldan geldiği görülür; çatı geçidini kapatır. | Vorr'a orta yakın; Kett kadraj kenarında arkadan. | M2 çatılar · Vorr'un yetişmesi merdivenle açıklanır; alternatif mavi tente rotası görünür. | 10 | Frames to Video | — | 1.KETT · 4.VORR · 7.CATILAR | G02 | ⬜ | — | — | — |
| C13 | İlk kaçış hamlesi: Kett yakındaki eğimli pas turuncusu tente üzerinden kayıp bir alt seviyedeki servis sahanlığına iner. | Kett yakındaki eğimli pas turuncusu tente üzerinden kayıp bir alt seviyedeki servis sahanlığına iner. | Yandan sabit geniş; kısa eğimli tente ve alt servis sahanlığı. | M2 çatılar · Kett alt servis sahanlığında; ponço sağlam; çekirdek sağ elde. | 10 | Frames to Video | tek oturarak kayma, kısa düşüş; atlama/takla yok (plan) | 1.KETT · 7.CATILAR · 9.CEKIRDEK | G02 | ⬜ | — | — | — |
| C14 | Pazar yardım ediyor: Aşağıda Mara, önceden gördüğümüz pirinç kolu tek hamlede indirir; kendi güçlendirilmiş tentesi uzamaya başlar. | Aşağıda Mara, önceden gördüğümüz pirinç kolu tek hamlede indirir; kendi güçlendirilmiş tentesi uzamaya başlar. | Mara ve pirinç kola orta yakın; üst kenarda katlı mavi tente. | M1 pazar · C07'de kurulan tente sistemi devreye girer; Mara tezgâhta. | 10 | Frames to Video | — | 3.MARA · 6.PAZAR | G02 | ⬜ | — | — | — |
| C15 | Mavi köprü: Tam açılmış, gergi kablolu mavi teslimat tentesi iki servis sahanlığını birleştirir. Kett karşı tarafa geçer. | Tam açılmış, gergi kablolu mavi teslimat tentesi iki servis sahanlığını birleştirir. Kett karşı tarafa geçer. | Geniş yanal; tente üzerinde Kett, altta büyük ve küçük uzaylılar. | M2 çatılar · Kett kule tarafındaki sahanlığa ulaşır; mavi köprü bağlı kalır. | 10 | Frames to Video | tente raylar ve kablolarla gergin; Vorr tenteye çıkmaz (plan) | 1.KETT · 7.CATILAR · 9.CEKIRDEK | G02 | ⬜ | — | — | — |
| C16 | Takip henüz bitmedi: Vorr kendi ağırlığını taşımayacak tenteye girmek yerine paralel demir servis merdiveninden kuleye yönelir. | Vorr kendi ağırlığını taşımayacak tenteye girmek yerine paralel demir servis merdiveninden kuleye yönelir. | Uzun odaklı orta; Vorr ayrı metal merdivende, kule arkada. | M2 çatılar · Vorr demir merdivenden gelir; Kett'e yetişmesi mümkün bir rota gösterilir. | 10 | Frames to Video | — | 4.VORR · 7.CATILAR | G02 | ⬜ | — | — | — |
| C17 | Manzaranın zirvesi: Kett hava kulesinin üst platformuna çıkar. Önünde çekirdeğe uyan üç oluklu yuva ve büyük mavi el çarkı vardır. | Kett hava kulesinin üst platformuna çıkar. Önünde çekirdeğe uyan üç oluklu yuva ve büyük mavi el çarkı vardır. | Kett arkadan çok geniş; su halkası, halka gezegen ve pazar aynı ölçekte. | M3 hava tacı · Yuva ve mavi çark net; kurgu çözümü C07'deki talimatla aynı. | 10 | Frames to Video | — | 1.KETT · 8.HAVA_TACI · 9.CEKIRDEK | G03 | ⬜ | — | — | — |
| C18 | Çekirdek yerine: Kett çekirdeği sağ eliyle uyumlu yuvaya oturtur. Üç gümüş kaburga yuvadaki oluklara denk gelir. | Kett çekirdeği sağ eliyle uyumlu yuvaya oturtur. Üç gümüş kaburga yuvadaki oluklara denk gelir. | Yakın detay; sağ el, üç oluklu yuva ve çekirdek. | M3 hava tacı · Çekirdek C18'den finale kadar yuvada; Kett'in elleri artık boş. | 10 | Frames to Video | tek çekirdek, tek yuva; çekirdek kırılmaz (plan) | 1.KETT · 8.HAVA_TACI · 9.CEKIRDEK | G03 | ⬜ | — | — | — |
| C19 | Son engel yaklaşır: Vorr, kurulan demir merdivenin son basamaklarından platforma çıkar. | Vorr, kurulan demir merdivenin son basamaklarından platforma çıkar. | Vorr'a orta; platforma açılan merdiven kapısı kadrajda. | M3 hava tacı · Vorr fiziksel olarak platformda; çekirdek yuvada; çark kapalı. | 10 | Frames to Video | — | 4.VORR · 8.HAVA_TACI | G03 | ⬜ | — | — | — |
| C20 | Yakalanma: Vorr sağ eliyle Kett'in ponçosunun arka yakasını kavrayıp onu mavi çarka varmadan durdurur. | Vorr sağ eliyle Kett'in ponçosunun arka yakasını kavrayıp onu mavi çarka varmadan durdurur. | Yandan orta; Kett çarka uzanmış, Vorr arkasında. | M3 hava tacı · Vorr yalnız ponço kumaşını tutar; boyna/el bileğine temas yok. | 10 | Frames to Video | Vorr yalnız ponço kumaşını tutar; boğma, kaldırma, vurma yok (plan) | 1.KETT · 4.VORR · 8.HAVA_TACI | G03 | ⬜ | — | — | — |
| C21 | İlk sahnedeki toka: Kett göğsündeki beyaz tokayı açar. Ponço Vorr'un elinde kalır; Kett koyu turkuaz tulumuyla serbest kalır. | Kett göğsündeki beyaz tokayı açar. Ponço Vorr'un elinde kalır; Kett koyu turkuaz tulumuyla serbest kalır. | Kett'e yakın; tek beyaz toka, arka planda Vorr'un kumaşı tutan eli. | M3 hava tacı · C21 sonunda Kett ponçosuz; ponço Vorr'un sağ elinde; çekirdek yuvada. | 10 | Frames to Video | plan pilotu: ponço çıkarma — tek ponço, tek toka; plan yedeği: tek üretimde bozulursa aynı 10 s birimde toka detayı + ponçosuz Kett tepkisi iki kısa görüntüden (plan §10) | 1.KETT · 2.KETT_TULUM · 4.VORR · 8.HAVA_TACI | G03 | ⬜ | — | — | — |
| C22 | Yağmur açılır: Kett iki eliyle büyük mavi çarkı son noktasına kadar çevirir. Mavi borulara birer birer su dolar. | Kett iki eliyle büyük mavi çarkı son noktasına kadar çevirir. Mavi borulara birer birer su dolar. | Yan orta; Kett ve büyük mavi el çarkı; yuva görünür. | M3 hava tacı · Çark açık konumda kilitlenir; genel yağmur dağıtımı açılır; Kett ponçosuz. | 10 | Frames to Video | çark yarım tur, fiziksel durdurucu; konsol planında yağmur yok (plan) | 2.KETT_TULUM · 8.HAVA_TACI · 9.CEKIRDEK | G03 | ⬜ | — | — | — |
| C23 | Uzaylıların yağmuru: Yağmur kuru pazara ulaşır. Tula fincanını kaldırır; arkasındaki farklı türler suyu şaşkınlıkla karşılar. | Yağmur kuru pazara ulaşır. Tula fincanını kaldırır; arkasındaki farklı türler suyu şaşkınlıkla karşılar. | Önde Tula ve Mara; geniş derinlikte sekiz farklı uzaylı türü. | M1 pazar · Pazar ilk kez ıslanır; Tula'nın fincanı dolmaya başlar; mevcut çiçek canlanır. | 10 | Frames to Video | plan pilotu: çok türün bulunduğu yağmur planı — sekiz tür yumuşak odakta katmanlı, çoğalma yok | 3.MARA · 5.TULA · 6.PAZAR | G03 | ⬜ | — | — | — |
| C24 | Son espri ve kapanış: Kett çarkın öteki yanında nefeslenir. Vorr elindeki ponçoyu gevşetip diğer avucunda yağmuru hisseder. | Kett çarkın öteki yanında nefeslenir. Vorr elindeki ponçoyu gevşetip diğer avucunu yağmura açar. | Kett önde sağda; Vorr solda yumuşak, aralarında çark; yağmur ve şehir arkada. | M3 hava tacı · Kett ponçosuz; ponço Vorr'da; çark açık ve çekirdek yuvada; yağmur sürer. | 10 | Frames to Video | — | 2.KETT_TULUM · 4.VORR · 8.HAVA_TACI | G03 | ⬜ | — | — | — |

```
Süre: her çekim 10 (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10; toplam = HEDEF_SURE.
  Ritim süreyle değil çekim içi hareket ve kadraj/ölçek değişimiyle kurulur (ARIZA H10).
Flow modu: Frames to Video · Ingredients to Video · Text to Video (yalnız kimliksiz çekim).
Risk: ARIZA_LISTESI T kodu → "nasıl gösterilir" (örn. T01 → temas kadraj dışı, sonrası C05).
Grup: PROMPTLAR/<Grup>.md (8-12 çekim). Durum: ⬜ · ✍️ prompt · 🖼️ kare onaylı · 🎥 deneme · ✅ seçildi.
Zincir · Baş. karesi · Bitiş karesi: yönetmen "—" bırakır; sahneleme odası (§F3b) doldurur.
  Zincirli çekim: Zincir = Z1 · Baş. = Z1.0 · Bitiş = Z1.1 (B) — ya da Baş. = "son:C02" (A) / "t:C02@4.2" (A′).
  Zincirli çekim de 10 s'dir → zincir yalnız KLIP_SURESI ≥ 10 ölçülürse kurulur; zincir en çok 4 halka; her halka yeni bir bilgi taşır.
DELTA BÜTÇESİ (her halka, Zk.n → Zk.n+1): aynı objektif · ışık · set │ en çok bir basit kamera
  hareketi │ özne yalnız ulaşabileceği mesafede │ kadraja nesne/kişi girip çıkmaz │ el-nesne
  teması değişmez │ durum değişimi küçük ve tek. Aşılırsa model iki kareyi eritir (morf).
```

### AÇILIŞ — ilk 30 saniye (`uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §2 · yonetmen F3'te doldurur)

| Saniye | Çekim | Sorun ya da beklenmedik hareket | İnsan (beden · el · yüz) | Replik · ekran yazısı | Kapak bağı | Sesi kapalı okunur mu |
|---|:--:|---|---|---|---|:--:|
| 0-10 | C01 | Doğrudan koşunun içinde: Kett'in elindeki saydam kapsülde şimşek çakıyor; arkada dev muhafızın ağır ayak sesleri (plan §1). | beden + yüz: Kett (koşu, yakın takip) | KETT: "Just a little bad weather. Worth a whole ship." · yok | çalınan nesne ve tehlike: Kett + fırtına kapsülü (kapak fikri plan §11) | evet: kapsül + koşu |
| 10-20 | C02 | Muhafız kalabalığı yararak bağırıyor: "Bring back the rain!" (plan §1) | yüz: Vorr | VORR: "Bring back the rain! That forecast belongs to us." · yok | kapakta arkada küçük Vorr | evet: takipçi |
| 20-30 | C03 | Yukarıda özel bahçelerde yağmur, aşağıda kupkuru pazar; dünyanın adaletsiz kuralı tek geniş planda (plan §1) | beden: küçük Kett | yok · yok (film adı yalnız son planın son ≈1,5 s'sinde, plan §1) | kuru ↔ yağmurlu bakır pazar (kapak plan §11) | evet: kuru pazar + camın içinde yağmur |

```
Plan §1: başlangıçta kanal logosu, açıklama metni ya da uzun uzay manzarası yok; film adı son planın son ≈1,5 s'sinde görüntünün üstüne, toplam süreye yeni kart eklenmez.
İlk 60 saniye (plan): tek damla solan çiçeğe renk verir (C05) · Kett kalkan gemi yerine kuleye döner (C06).
```

## 5. REPLİKLER

<!-- REPLIK yok ise tablo boş kalır -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R01 | C01 | 2.2 | Kett | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Just a little bad weather. Worth a whole ship. | 3.5 |
| R02 | C02 | 1.0 | Vorr | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Bring back the rain! That forecast belongs to us. | 3.5 |
| R03 | C04 | 1.0 | Tula | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | One drop. Please. The flower can't wait for payday. | 3.5 |
| R04 | C05 | 5.0 | Kett | kadraj dışı (plan: "off-screen") | HUMAN | I was going to sell it. Buy a way out. | 4.0 |
| R05 | C06 | 1.0 | Mara | kadraj dışı — arkada yumuşak odak, dudak oynamaz (plan) | HUMAN | Your ship's leaving. | 1.5 |
| R06 | C06 | 4.5 | Kett | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Let it. I'm changing the weather. | 2.5 |
| R07 | C07 | 1.0 | Mara | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Core in. Turn the blue wheel. Once it starts, nobody can stop it. | 5.0 |
| R08 | C08 | 1.0 | Vorr | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Where is he? | 1.5 |
| R09 | C08 | 3.3 | Mara | kadraj dışı ya da yumuşak arka plan, dudak oynamaz (plan) | HUMAN | Buying an umbrella. You should try it. | 3.0 |
| R10 | C10 | 1.0 | Kett | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | So it can rain. Just on the right side of the glass. | 4.5 |
| R11 | C12 | 1.0 | Vorr | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | That rain is company property. Don't make this expensive. | 3.5 |
| R12 | C12 | 5.3 | Kett | kadraj dışı (plan: "heard off-screen") | HUMAN | Little late for that. | 1.5 |
| R13 | C14 | 1.0 | Mara | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Free delivery! | 1.0 |
| R14 | C19 | 2.5 | Vorr | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Step away from the wheel. You don't know what this costs. | 4.0 |
| R15 | C20 | 1.0 | Vorr | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | That rain is not yours. You can't just give it away. | 4.0 |
| R16 | C21 | 0.5 | Kett | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | It isn't yours either. You just built a roof over it. | 4.0 |
| R17 | C22 | 6.5 | Kett | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Forecast: everybody. No exceptions. | 1.5 |
| R18 | C23 | 1.0 | Tula | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | How much? | 1.0 |
| R19 | C23 | 2.8 | Mara | kadraj dışı (plan: "from just off-screen") | HUMAN | For once? Nothing. | 1.5 |
| R20 | C24 | 2.0 | Kett | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan §7 "Ses uygulaması") | HUMAN | Keep the coat. You'll need it. | 2.5 |

```
Kaynak: telsiz · kadraj dışı · kask içi · makine · kayıt → ses kurguda eklenir, ≤ 8 s
        ağız kadrajda (son çare) → model dudak senkronu, ≤ 5 s, sayı yok, video promptunda tırnak içinde birebir
        model sesi (telsiz | voice-over | ağız kadrajda) → replik video promptuna BİREBİR yazılır, Omni konuşmayı videoda
        üretir (sahip kararı 12.10.2026); ≤ 8 s (ağız kadrajda ≤ 5 s); klip sesi filme girer (timeline klip_sesi), kurgu kaydı yedek
Kayıt: HUMAN | MACHINE · bant: 2 dk 6-12 · 4 dk 12-24 · 8 dk 20-40 · 16 dk 40-70 replik
Konuşma ve ses profilleri: plan §3 + §7 "Voice" satırları (Kett: Alert adult voice, light and slightly rough, quick wit without a cartoon squeak ·
  Vorr: Deep restrained adult bass, slow authority, no monster growls · Mara: Warm adult contralto, dry humor, confident calm, not a narrator ·
  Tula: Soft older adult voice, breath and patience, clear words). Plan §10: dört ayrı ses kimliği, İngilizce kayıt; iki konuşanlı
  sahnede ekran dışı cevap. Saniye ve süre Fable tahmini (2,8 kelime/s), F8'de kayıtla kesinleşir. Kayıt: HUMAN varsayılan — ses kaynağını sahip seçer.
20 replik: 4 dk bandı 12-24 içinde.
```

## 6. SES PLANI — model sesi kullanılmaz (istisna: §5 Kaynak = model sesi, yalnız replik)

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | Hızlı küçük ayaklar, şişe içinden boğuk gök gürültüsü. (plan) | — (F8) | M1 pazar |
| S2 (C02) | Metal botun taş zemine vuruşu, pazar uğultusunun kısa kesilmesi. (plan) | — (F8) | M1 pazar |
| S3 (C03) | Sekiz ayrı uzaylı türünden konuşma dokusu; uzakta kalkış motoru. (plan) | — (F8) | M1 pazar |
| S4 (C04) | Boş bakır musluğun kuru tıklaması. (plan) | — (F8) | M1 pazar |
| S5 (C05) | Tek su damlası; müzik ilk kez yumuşar. (plan) | — (F8) | M1 pazar |
| S6 (C06) | Kalkış uyarısı; ritmin kararlı biçimde başlaması. (plan) | — (F8) | M1 pazar |
| S7 (C07) | Mavi borudan düşük su rezonansı. (plan) | — (F8) | M1 pazar |
| S8 (C08) | Uzakta kuru metal kapların sallanması. (plan) | — (F8) | M1 pazar |
| S9 (C09) | Ayakların servis basamaklarına teması; yukarıdan rüzgâr. (plan) | — (F8) | M2 çatılar |
| S10 (C10) | Camın arkasından boğuk yağmur; dışarıda kuru rüzgâr. (plan) | — (F8) | M2 çatılar |
| S11 (C11) | Gemi motorunun uzaklaşması; kısa nefes. (plan) | — (F8) | M2 çatılar |
| S12 (C12) | Ağır bot; müzikte kısa boşluk. (plan) | — (F8) | M2 çatılar |
| S13 (C13) | Gergin kumaş sürtünmesi; hafif metal iniş. (plan) | — (F8) | M2 çatılar |
| S14 (C14) | Pirinç kolun tok sesi; makara ve gergi kablosu. (plan) | — (F8) | M1 pazar |
| S15 (C15) | Tentenin yumuşak esnemesi, aşağıdan şaşkın uzaylı sesleri. (plan) | — (F8) | M2 çatılar |
| S16 (C16) | Demir basamaklarda ağır düzenli vuruşlar. (plan) | — (F8) | M2 çatılar |
| S17 (C17) | Rezervuardaki suyun derin uğultusu; kısa, geniş müzikal açılma. (plan) | — (F8) | M3 hava tacı |
| S18 (C18) | Üç tok mekanik klik; düşük enerji sesi. (plan) | — (F8) | M3 hava tacı |
| S19 (C19) | Merdiven sesi kesilir; yalnız su ve nefes kalır. (plan) | — (F8) | M3 hava tacı |
| S20 (C20) | Kumaşın gerilmesi; müzik tek bas notaya düşer. (plan) | — (F8) | M3 hava tacı |
| S21 (C21) | Tokanın belirgin küçük çıtı. (plan) | — (F8) | M3 hava tacı |
| S22 (C22) | Çarkın kilit sesi; rezervuarın açılan vanaları, müziğin çözülmesi. (plan) | — (F8) | M3 hava tacı |
| S23 (C23) | İlk damlalar bakıra vurur; sonra dolgun yağmur ve karışık sevinç sesleri. (plan) | — (F8) | M1 pazar |
| S24 (C24) | Yumuşak yağmur, küçük bir nefes gülüşü; son notanın uzaması. (plan) | — (F8) | M3 hava tacı |

```
Ortam: açık hava, nefes alınabilir atmosfer (ay şehri pazarı, çatılar, kule platformu); ses havayla taşınır. Model sesi kullanılmaz:
       plan §7 "modelin ses ürettiği varsayılmaz" → klip sesi atılır; replik + efekt + ortam + müzik kurguda.
Plan §9: dört ana sesin tınısı ve aksanı sabit · arka plan uzaylıları tek tip insan kalabalığı gibi bağırmaz (klikler, yumuşak boğaz sesleri,
       farklı rezonanslar, konuşma dokuları) · ana repliğin altında anlaşılır kelimeler yarışmaz · son iki klipte müzik diyalogdan ve bakıra vuran yağmurdan alçak.
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_<n>.md (her çekim en az bir efekt satırı)
```

<!-- 12.10.2026 sahip kararı: klipler arası keskin kesme ve kesmede komple değişen arka ses → uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md.
     Yatak mekân başına TEK dosya, klip sınırlarını aşar (timeline.json yataklar). Geçiş kesme başına: kesme | karisim 0,3-0,8 s | karartma 0,5-1,5 s. -->
### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

<!-- 19.10.2026: ODA/F4_ses-tasarimcisi_1.md'den birebir (F4 tur 1). Efekt listesi + kayıt listesi ODA dosyasında. -->
| Yatak | Mekân | Çekimler (klip sınırlarını aşar) | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | M1 pazar (kuru) | C01-C08 · C14 | `low steady open-air market murmur of many different alien voices, soft layered resonances, no intelligible words, no rhythm, no music, dry dusty air` | −21 LUFS (replik yokken −20…−22; replik altında −23) | `ses/yatak_pazar.wav` (≥ 100 s, döngüsüz tek parça) |
| Y2 | M2 çatılar | C09-C13 · C15-C16 | `dry steady wind from above over copper rooftops, soft and low, with a very faint murmur of a market far below, no rhythm, no music` | −21 LUFS | `ses/yatak_catilar.wav` (≥ 80 s) |
| Y3 | M3 hava tacı | C17-C22 | `deep low continuous hum of a vast body of water overhead, steady, no rhythm, no music` | −20 LUFS | `ses/yatak_hava_taci.wav` (≥ 70 s) |
| Y4 | Yağmur hâli (M1 → M3) | C23-C24 | `first sparse raindrops on dry copper growing into full soft steady public rain, no thunder, no music` | C23 −18 (dolgun) · C24 −21 (yumuşak) | `ses/yatak_yagmur.wav` (≥ 30 s) |

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1 kesintisiz; C01'in ağır adımları L 0,8 s; C02 bot vuruşu ≈0,7 s | aynı mekân; Kett'in sağa koşusu → Vorr'un sağa bakışı, hareket üstünde |
| C02→C03 | kesme | Y1 sürer (kısa kesilmeden döner); doku katmanı J 1,0 s | aynı mekân, ölçek büyük sıçrar (orta yakın → yüksek geniş) |
| C03→C04 | kesme | Y1 sürer; doku L 0,8 s kısılır | Kett sağa ilerler → Tula'nın yanında yavaşlar |
| C04→C05 | kesme | Y1 sürer; müzik yumuşaması C04 son 0,5 s'de (J 0,5 s) | fincan/tıklama → çekirdek valfi; damla yumuşamaya düşer |
| C05→C06 | kesme | Y1 sürer; damla yankısı L 0,5 s | makro → orta; kararın başlangıcı |
| C06→C07 | kesme | Y1 + müzik kesintisiz | Kett sağa döner → Mara'nın yukarı işareti |
| C07→C08 | kesme | Y1 sürer; boru rezonansı L 0,8 s; metal kap sallanması C08 başı | Vorr tezgâha varır, aynı mekân |
| C08→C09 | karışım 0,4 | Y1→Y2 çapraz 1,5 s (Y2 J 1,0 s; Y1 L 1,5 s) | M1→M2 (yükseklik), Vorr'un yukarı bakışı → Kett tırmanışta: zaman atlaması, ışık/ton yumuşatılır |
| C09→C10 | kesme | Y2 sürer; cam arkası yağmuru J 1,0 s çok düşük | tırmanış → cam boyunca; ölçek/açı değişir |
| C10→C11 | kesme | Y2 sürer; gemi motoru J 0,8 s; yağmur L 0,8 s | aynı çatı; Kett'in bakışı camdan gemiye döner |
| C11→C12 | kesme | Y2 sürer; ağır bot J 0,8 s | aynı çatı; tehdit sesi görüntüden önce gelir |
| C12→C13 | kesme | Y2 sürer; bot/merdiven L 0,5 s | yüzleşme → kayma hamlesi, hareket üstünde |
| C13→C14 | kesme | Y2→Y1 çapraz 1,0 s (Y1 J 1,0 s); iniş kuyruğu L 0,5 s | Kett'in inişi → Mara'nın kolu: neden-sonuç, paralel eylem |
| C14→C15 | kesme | Y1→Y2 çapraz 1,0 s; makara/kablo L 1,0 s | kol indi → tente tam açık: kablo sesi bağı |
| C15→C16 | kesme | Y2 sürer; demir basamak J 1,0 s; uzaylı sesleri L 0,8 s | Kett karşıya geçti → Vorr'un paralel rotası |
| C16→C17 | karışım 0,5 | Y2→Y3 çapraz 1,5 s (Y3 J 1,5 s) | M2→M3 (6 m → 18 m), kuleye varış; ışık/ölçek sıçraması yumuşatılır; basamaklar alçalarak C17'ye geçer |
| C17→C18 | kesme | Y3 sürer; müzik açılması L 0,8 s | çok geniş → yakın detay; Kett konsola yaklaşır |
| C18→C19 | kesme | Y3 sürer; düşük enerji sesi L 0,5 s | aynı platform; çekirdek yerinde → Vorr gelir |
| C19→C20 | kesme | Y3 sürer; nefes L 0,4 s; kumaş gerilmesi J 0,3 s | Vorr yaklaştı → yakalama, hareket üstünde |
| C20→C21 | kesme | Y3 + tek bas nota kesintisiz | gerilmiş kumaş → toka yakın planı |
| C21→C22 | kesme | Y3 sürer; çıt kuyruğu L 0,4 s; müzik çözülmesi C22 başı | Kett serbest → çarka; hareket üstünde |
| C22→C23 | karışım 0,8 | Y3→Y4 çapraz 1,5 s; vana/boru suyu L 1,0 s, ilk damla üstüne düşer | M3→M1; su borulardan pazara varır: zaman/mekân atlaması, kule → pazar |
| C23→C24 | kesme | Y4 kesintisiz (C24'te hafif kısık); sevinç sesleri L 1,0 s | pazar → kule; yağmur ortak köprü |

## 7. MÜZİK PLANI

<!-- 19.10.2026: ODA/F4_besteci_1.md'den (F4 tur 1, sonnet; yalnız plan §9 + §7 "Kurgu sesi" satırları). Vuruş tablosu ve miks notları ODA dosyasında. -->
```
OKUMA        İzleyici bu filmi yağmurun satıldığı bir şehirde küçük bir hırsızın renkli, esprili kaçış masalı olarak okumalı.
MÜZİKSİZ     C12 1:49-1:57 (plan C12 "müzikte kısa boşluk") · C19 2:58,5-3:10 (plan C19 "yalnız su ve nefes kalır"; C20 "tek bas notaya düşer")
VURUŞ/SUSMA  0:00 C01 çok kısık zemin · 0:10 hafif hızlı ritim (C02) · 0:41,5 yumuşama (C05) · 0:55,5 kararlı ritim (C06) · 2:00 ritim geri (C13) ·
             2:40,5 geniş açılma (C17) · 3:10 tek bas notası (C20) · 3:35,5 çözülme D majör (C22) · 3:55 son nota (C24) · 4:00 kuru kesme — F8'de gerçek kesmelerle kesinleşir
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md · risk: Flow Music parça süresi 30 s - 3 dk (FLOW_GERCEKLERI §6, ◐) → 4:00 tek parça çıkmazsa iki parça, sahibe sorulur
```

<!-- 12.10.2026 sahip kararı: her filmde müzik promptu burada durur. F4'te besteci taslağı, F8'de gerçek kesme noktalarıyla
     kesin sürüm (eski sürüm altına tarihle kalır, silinmez). İngilizce, tek parça, süre + açılış + yükseliş/susma + palet + [Instrumental] + YOK listesi.
     film_dogrula --bolum muzik: MUZIK var ise zorunlu (≥200 karakter, Türkçe karakter yok). -->
### MÜZİK PROMPTU — Flow Music'e yapıştırılır
```text
[Instrumental] One continuous 4:00 piece, 120 BPM, 4/4, tonal center D (D dorian, one release into D major at 3:35). Colorful sci-fi caper chase with dry humor and a small fable at its heart: light, playful, warm, never menacing. Palette: pizzicato cello and upright bass, marimba, vibraphone, kalimba, tuned copper bowls, hand percussion (shaker, wood block, finger snaps), warm strings, a small friendly brass group late. No drum kit.
Structure (approximate mm:ss):
0:00-0:10 almost nothing: a very quiet, distant ticking pulse, barely audible, no melody.
0:10 light, quick, bouncy rhythm enters: pizzicato bass and marimba ostinato with hand percussion. 0:20-0:30 same pulse, a wide warm pad and a simple curious vibraphone motif open up.
0:30-0:40 thin and light. 0:41 the pulse drops out for the first time: soft held pad, one sparse vibraphone note at 0:43.
0:55 a steady, determined rhythm begins on a downbeat: walking pizzicato bass, marimba, firm shaker, same tempo, more resolved. 1:00-1:30 steady under dialogue, dry and lower; a climbing line at 1:20. 1:30-1:48 very sparse: bass, soft pad, single notes.
1:49 music stops dead, no tail. Total silence until 1:57, then one single low pizzicato note alone.
2:00 playful, energetic rhythm returns for an escape across awnings; small warm brass joins at 2:11; 2:20-2:30 fullest, whole ensemble, the main motif. 2:30-2:40 heavy but calm low register, cello and bass clarinet, steady, not menacing.
2:40 a short wide musical opening for four seconds, open chords, then hush. 2:50-2:58 sparse pad and single notes.
2:58 music stops dead. Total silence until 3:10, then one single low bass note (D2 doubled by D3) held alone for twenty-five seconds, no build, no riser.
3:35 that note blooms into a warm D major chord with strings and vibraphone: the only true resolution. 3:40-3:55 gentle sustained chord, sparse vibraphone, very quiet.
3:55 one final open fifth (D and A, no third) enters and sustains; the piece ends abruptly at 4:00 mid-note, no fade-out.
Bass has an octave double around 90-160 Hz, no sub bass below 60 Hz, mono compatible, dry and close. The last 30 seconds stay very quiet.
NO vocals, NO drums, NO riser, NO whoosh, NO choir, NO drone.
```
