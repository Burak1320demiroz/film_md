# 🛡️ PROMPT HATA ÖNLEME KILAVUZU

> **Kaynak:** `FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/` — 31 filmin 357 ham QA
> raporu, her bulgu o sahnenin prompt metnine karşı okundu (19.09.2026).
> **Ne zaman okunur:** prompt YAZILIRKEN, her prompt için. Ders arşivi değildir.
> **Ölçü birimi:** 688 tekil 🔴/🟠 bulgu · 🅐 293 (kilit vardı, tutmadı) ·
> 🅑 343 (kilit hiç yoktu) · 🅒 29 (bulgu düşer) · 🅓 23.

---

## 0. 🔍 BU KILAVUZ NEDEN VAR — kural yokluğundan değil, KURALIN ULAŞMAMASINDAN

`KILAVUZ_REHBERI` §5.1 sekiz cümlelik negatif çekirdeği **14.09.2026'da**
tanımladı ve içinde temas · giysi · parçacık cümleleri ZATEN var. Ölçüm:

```
ÇEKİRDEK KAPSAMASI ↔ ÖNLENEBİLİR HATA ORANI   (31 film · 19.09.2026)

  kapsama %78 olan 10 film   →  🅑 oranı ortalama %41
  kapsama %37 olan 10 film   →  🅑 oranı ortalama %79

  en yüksek beş:  FALLING_WORLD %91 (🅑 %15) · DRY_ANCHOR %83 (%26) ·
                  BENI_HATIRLAMA %83 (%21) · SUSMAYAN %80 (%13) ·
                  COUNTED_TURN %77 (%16)
```

⛔ **Ama reformdan SONRA yazılan iki film çekirdeği hiç kullanmadı:**
KRONOS_SON_SINYAL (15.09 · kapsama %41 · 🅑 **%93**) ve MARS_SON_CIKIS
(15.09 · %43 · 🅑 %64). KRONOS'un 96 promptunun **hiçbirinde** `AUDIO:` satırı yok.

> **Sonuç:** depo bilgi eksikliğinden kaybetmiyor. Bilgi Türkçe kartlarda duruyor,
> prompta İngilizce cümle olarak ulaşmıyor. Bu kılavuz o çeviriyi **hazır verir**;
> kopyala-yapıştır dışında bir iş bırakmaz.

---

## 1. ⭐ HER PROMPTTA BULUNMASI GEREKEN ON KİLİT

Sekizi NEGATIVE'de (§5.1), ikisi gövdede. **Onu da eksiksiz olan film bu depoda
en düşük hata oranını verdi.**

### 1a · NEGATIVE — sekiz cümle [`KILAVUZ_REHBERI` §5.1'den birebir]

```
Single unbroken take, no cuts, no dissolves, no camera resets, no angle change.
Exactly one human character, no duplicates, no second person.
0% bloom, no glow, no soft focus, every surface keeps visible texture.
No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark.
Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing.
Equipment and clothing identical throughout, no drift, no gear appearing or disappearing.
Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.
Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping.
```

⛔ **İnsan sayısı RAKAMLA yazılır** (`Exactly 2 human characters`) — `no extra
characters` bir TARİFTİR ve KRONOS'ta iki BLOCKER ürettiği ölçüldü.

⚠️ **TUR 22 · 19.09.2026 — YEDİNCİ CÜMLE (temas sınırı) TARTIŞMAYA AÇILDI.**
Hem dış literatür taraması hem deponun kendi 771 bulgusu **aynı yönde** çıktı:
negatif temas cümlesi arızayı azaltmıyor, işaret artırdığı yönde.
```
el/eldiven kadrajda olan 617 sahne · 34 film   (maruziyet kontrollü)
  cümle VAR : 41/349 = %11,8      cümle YOK : 15/268 = %5,6   → RR 2,10 · z ≈ +2,77
  yalnız EL karışan bulgularda                                → RR 2,30 · z ≈ +2,57
  betik: prompt_hata_analizi.py --temas-testi
```
⛔ **Cümle HENÜZ ÇIKARILMADI** — `KILAVUZ_REHBERI` §5.1 sahibin çekirdeğidir ve
tek bir gözlemsel ölçümle sökülmez. Karar için gereken şey `04 §TUR 22 ⑤`'te
yazılı: aynı sahne, aynı seed, tek fark cümle — iki koşu. Ayrıntı: §3 sınıf 2.
⛔ Cümleler **sahne sahne elle yazılmaz**, film başına bir kez yazılıp her prompta
BİREBİR kopyalanır. Ölçüm: temas cümlesi **17 filmde kısmi** — yani filmde var,
bulgunun düştüğü sahnede yok.

### 1b · GÖVDE — iki cümle · ⭐ BU KILAVUZUN EKLEDİĞİ ŞEY

```
PHYSICS:  <ortam cümlesi — §2'den, ADIYLA ve SAYISIYLA>
AUDIO:    <ses yasası cümlesi — §2'den>
```

⛔ **Çekirdeğin sekizinci cümlesi `the stated gravity` diyor ve §5 o değerin
YAZILMASINI hiçbir yerde istemiyor.** Ölçülmüş bedeli: BENI_HATIRLAMA çekirdeği
%83 kapsamayla taşıyor, yerçekimini **tarifle** yazıyor (`about two thirds of
Earth's weight`) ve ekranda 0,39 · 1,11 · 1,13 · 2,48 m/s² ölçüldü — **2,9×
tutarsızlık, iki BLOCKER**. "the stated gravity" ancak o sayı gerçekten
yazıldıysa bir şeyi kilitler.

---

## 2. 🌍 ORTAM CÜMLELERİ — kopyala, yapıştır, sayıyı değiştir

`KILAVUZ_REHBERI` §3 kartları ortamı **Türkçe** anlatır. Aşağıdakiler o kartların
prompta giren İngilizce karşılığıdır. **Filmin ortam kartı seçilince bu iki satır
PLAN'a yazılır ve her prompta aynen girer.**

### §3.1 VAKUM
```
PHYSICS: Gravity is <0.16> g in hard vacuum. Dust lifts and never settles, shadows are absolute black with razor edges, and exhaust leaves as a straight narrow cone that thins and is gone.
AUDIO:   No exterior sound at all — only what the suit body carries: breathing inside the helmet and a dull knock through the hull. No dialogue. No music.
```

### §3.2 İNCE ATMOSFER (Mars · %0,6 basınç)
```
PHYSICS: Gravity is 0.38 g and the air is thin at under one percent of Earth pressure. Dust falls slowly but certainly and settles within <3> seconds, shadow edges are soft, and nothing is blown over by wind.
AUDIO:   A low muffled rumble with no high frequencies, thin and close, two breathing rhythms inside the helmets. No dialogue. No music.
```

### §3.4 KALIN ATMOSFER (3-5 atm · düşük yerçekimi)
```
PHYSICS: Gravity is <0.20> g under a dense atmosphere of <4> atmospheres. Dust falls fast and clumps to the ground within <3> seconds with no hanging veil, shadows are soft-edged but deep, and exhaust is a short thick cone.
AUDIO:   Sound is strong, low and close — low frequencies carry well and highs are damped. No dialogue. No music.
```
**SİSLİ + BİYOIŞIKLI alt bandı** (sisli vadi + kendi ışığını veren alçak bitkiler) 🆕 28.09.2026
```
PHYSICS: Gravity is <0.42> g in a dense cold atmosphere at <3.1> bar and <240> kelvin. Lifted dust settles again within three seconds and clumps as it lands, the slow wind moves only fine dust along the ground, and anything she lets go reaches the ground in about a second.
AUDIO:   The cold dense air carries low frequencies close and strong and kills the highs, so everything sounds heavy and near. <sahnenin tek ses olayı>. No dialogue. No music.
```
Sis KONDENSATtır ve PHYSICS'te DEĞİL, **DÜNYA ÇAPASI'nda** durur (D209 üç cümlesinin
ufuk cümlesi) — çünkü PHYSICS satırı 24/24 promptta birebir olmak zorunda ve iç
mekân kliplerinde sis cümlesi yanlış olur (㉜⑥ sahne kilidi):
```
HORIZON: black stone valleys to a straight horizon, low mist sitting in the hollows
```
Kendi ışığını veren canlı için POZİTİF kaynak kuralı — `0% bloom / no glow` satırı KALKMAZ:
```
the low plants are themselves the source of a green-blue light, like lit lamps, the light not spreading past their edges
```
> ⭐ **Bu çift THE_SIGNAL_KEEPERS yazılırken (28.09.2026) yazıldı.** Kart §3.4 dört
> filmde kullanılmıştı ve yukarıdaki genel çift bir ŞABLONDU; bu alt bandın
> İngilizce karşılığı hiç yazılmamıştı.
> ⛔ **ÜÇ TUZAK:**
> ① **SİS ve TOZ AYNI CÜMLEDE YAZILAMAZ.** Kartın "asılı toz perdesi YOK" satırı
>   AYNEN geçerlidir; sis toz DEĞİL kondensattır, zeminde DURUR ve yükselmez. İki
>   madde, iki kural: sis OTURUR · toz KALKAR ve üç saniyede yeniden OTURUR. Aynı
>   promptta karıştırılırsa model ikisini tek bir asılı perde yapar.
> ② **BİYOIŞIK negatif çekirdeği KALDIRMAZ.** `0% bloom, no glow` satırı kalır ve
>   çözüm §3.6'nın Arşimet kalıbının aynısıdır: yasağı HÂLE için koru, KAYNAK için
>   pozitif kural yaz. Yukarıdaki cümle o pozitif kuraldır. ⚠️ ⑪ IŞIK merceği bunu
>   çelişki yazarsa bulgu TASARIMDIR — SPEC'in yanlış-pozitif duvarına satır olarak
>   girer. Yeryüzü çapası: okyanusta ölçülen ışıldayan canlı oranı %76'ya çıkıyor
>   (Martini & Haddock, Scientific Reports, 2017).
> ③ AUDIO satırı tizleri öldürür ve bu **bir imkândır**: THE_SIGNAL_KEEPERS'ta filmin
>   tamamında yalnız İKİ tiz olay var (kaydın ünsüzleri · camdan çıkan ton) ve ikisi
>   de dramaturjik. Ortam kartı ile ses tasarımı aynı gerekçeyi paylaşır.
> ⚠️ Kartın "dolgu ÇOK GÜÇLÜ" satırı bloom DAVETİYESİDİR. Çözüm dolguyu MOTİVE
>   etmektir: kaynak büyük ve yumuşak bir gök cismi olsun (halkalı dev gezegenden
>   yansıyan ışık, güneş diski YOK) ve LIGHT satırı bunu SÖYLESİN —
>   "the fill strong and soft, the shadows deep inside".

### §3.6 SÜREKLİ BULUT / NÖTR YÜZERLİK (55 km bandı · ~0,5 atm yoğun CO₂) 🆕 25.09.2026
```
PHYSICS: Gravity is <0.904> g in a dense carbon-dioxide cloud layer at about half an Earth atmosphere; the platform floats in neutral buoyancy, settling at a constant rate, and it never hovers, never hangs motionless, never rises. No ground, no horizon and no wind, so nothing lifts and nothing is blown about; anything let go falls a glove's height in about a third of a second.
AUDIO:   The dense air carries a low close hum and takes the high frequencies out of everything. Her breathing sits under it. No dialogue. No music.
```
> ⭐ **Bu çift THE_COUNTED_RIVET yazılırken (25.09.2026) yazıldı** — §2 beş ortam
> kartı için hazır cümle veriyordu ve §3.6 listede YOKTU. Kart 21.08.2026'dan beri
> vardı, İngilizce karşılığı iki film boyunca her seferinde yeniden yazıldı.
> ⛔ **ÜÇ TUZAK, üçü de bu kartta:**
> ① Kaldırma GERÇEK (Arşimet) → gövde havada DURUR. Bu, negatif çekirdeğin
>   `never hovering` yasağıyla çakışır gibi görünür. Çözüm POZİTİF kural
>   cümlesidir: `floats in neutral buoyancy, settling at a constant rate` —
>   yasak PARÇACIKLAR içindir ve kadrajda serbest parçacık yoktur.
> ② Ufuk ve zemin İKİSİ DE yok → D209'un "gök · ufuk · yer imi" üçlüsü BU KARTTA
>   YAZILAMAZ. Uyarlanmış üçlü: ① kaynaksız parlak kubbe, güneş diski 0 kare
>   ② aşağıda derinlik, ufuk çizgisi yok ③ yer imi YAKIN NESNENİN kendisi.
> ③ Gölge YOK ve bu MEŞRUDUR (dolgu her yönden). Işık takvimi yön ve Kelvin ile
>   yazılamaz — güneş diski olmadığı için yön diye bir şey yoktur; takvim TEK
>   PARLAKLIK DİZİSİ olur ve monotonik kalır [D193 uyarlaması].
> ⚠️ Platform bir noktada SERBEST kalıp yükseliyorsa PHYSICS satırı o sahnede
>   değişir ve `never rises` düşer — sahne içinde birebir aynı kalmak koşuluyla
>   (㉜⑥). THE_COUNTED_RIVET'in S7'si bu biçimi taşıyor.

### §3.7 VAKUM + DÖNME YERÇEKİMİ
```
PHYSICS: The deck holds <0.30> g from rotation with a radius of <60> metres, and objects dropped near the rim drift <along the spin direction> as they fall. Outside is hard vacuum.
AUDIO:   No exterior sound. The structure rings: every contact carries through the metal as a low bell note that fades in about <1.5> seconds. No dialogue. No music.
```

### §3.8 VAKUM + TEMİZ METAL · SOĞUK KAYNAK 🆕 28.09.2026
```
PHYSICS: Gravity is <0.30> g in hard vacuum. Lifted dust rises in a flat arc and lands without settling again, shadows are absolute black with razor edges, and anything she lets go reaches the plate in about <one> second.
AUDIO:   There is no sound in the vacuum outside, so everything heard is contact carried through the metal and the suit — dry, short, with no echo. No dialogue. No music.
```
**ASİMETRİ CÜMLESİ — bu kartın ZORUNLU üçüncü satırı** (temasın konu olduğu her klipte):
```
Bare metal that touches bare metal stays joined, and the ceramic-coated boots, gloves and outer fabric do not join.
```
**METİN KARŞI ÖNLEMİ — zemin İŞLENMİŞ METAL olduğu için** (metal yüzey kadrajdaysa):
```
The only marks on the metal are weld seams eight millimetres wide, rivet lines forty millimetres apart and meteorite pits.
```
> ⭐ **Bu dörtlü THE_LAST_TOW yazılırken (28.09.2026) yazıldı.** Kart §3.8 01.09.2026'da
> açıldı ve İKİ film boyunca (THE_COLD_WELD · THE_LAST_TOW) İngilizce karşılığı
> §2 listesinde YOKTU; ikisi de elden yeniden yazdı.
> ⛔ **DÖRT TUZAK:**
> ① **Kuralı YASAK olarak yazmak.** "does not weld" / "never welds" / "no cold weld"
>   cümlesi modele o olayı çizdirir [D59 · D123]. Yukarıdaki asimetri cümlesi yasağın
>   yerine geçer: bir yarısı POZİTİF (bare metal stays joined), öteki yarısı da POZİTİF
>   (ceramic-coated … do not join — bu bir yasak değil, MALZEME ayrımı).
> ② **Kanıtların hepsinin YOKLUK olması.** Bu kartın park edilmiş ders adayı bu:
>   THE_COLD_WELD'de altı merceğin ALTISI kuralı adlandıramadı, çünkü bütün kanıtlar
>   olumsuzlamaydı (düşmeyen anahtar · kalkmayan avuç · kaymayan levha) ve video
>   "olmayan bir şeyi" "hiçbir şey" diye render etti. ⛔ Karşı önlem: her sahnede
>   kuralı bir **DEĞİŞİMLE** kanıtla (kopan dikiş · kopan bot · yapışan kama).
>   THE_LAST_TOW dört zorunlu kanıt klibi ilan etti ve SPEC'e "kesilemez" yazdı.
> ③ **Bağı GEOMETRİK sanmak.** Kaynak ATOMİKTİR: iki yüzey ayrı ayrı görünür ve
>   aralarında NET sınır kalır. "El metale eriyor/batıyor" bir ÜRETİM HATASIDIR [D24].
>   Her kaynak klibinde pozitif sınır cümlesi gerekir: `the two surfaces stay separate
>   with a clean visible boundary between them, nothing melts, nothing sinks in`.
> ④ **Toz.** Bu kartın zemini metaldir ve göktaşı bombardımanı onu temizlemiştir:
>   metalin üstünde 0 kare toz. Toz YALNIZ metal DIŞINDAKİ regolitte görünür —
>   pozitif hâlde yazılır, yoksa model ya her yere serper ya hiç koymaz.

⭐ **YALAYAN IŞIK ALT BANDI** (yıldız ufka yakınken · THE_LAST_TOW 28.09.2026):
```
LIGHT: grazing light from outside the frame on the left strikes every upright metal face and leaves the ground dark; shadows are absolute black with razor edges and there is no fill.
```
> Gerekçe SAYIYLA: yıldız 2,3° yükseklikte ise yatay zemin 1361 × sin(2,3°) ≈ 55 W/m²
> alır (denge ~180 K), yıldıza BAKAN dikey yüzey tam 1361 W/m² alır (~370-390 K).
> → Aynı köşenin iki yüzü arasında ~190 K fark. **Bu kartta ısı farkı bir OLAY
> kaynağıdır** (kaynağı koparır), dekor değil. Ayrım DİKEY/YATAY olduğu için
> kompozisyon da ondan çıkar: dikey yüzeyler parlar, zemin karanlık kalır.
> ⚠️ Genleşme sayısı: kart "metrede ~1,3 mm" diyor ve bu α ≈ 4,8 × 10⁻⁶ /K demektir
> (düşük genleşmeli alaşım). Yapı çeliği 12 × 10⁻⁶ /K ile aynı ΔT'de 3,2 mm/m verir.
> ⬜ Kartın hangi alaşımı varsaydığı YAZILI DEĞİL — aday gözlem olarak kaydedildi.

### §3.9 KRİYOJENİK ORTA BASINÇ (95 K · 0,90 bar · 0,38 g) 🆕 26.09.2026
```
PHYSICS: Gravity is <0.38> g in a dense cryogenic atmosphere at <0.90> bar and <95> kelvin. Lifted frost settles within half a second, the slow wind never moves cloth, and anything let go reaches the ground in about a second.
AUDIO:   The cold dense air carries low frequencies close and strong and kills the highs. No dialogue. No music.
```
**KURU + BERRAK alt bandı** (uzun gece pusu yağdırdı) — PHYSICS'e TEK cümle eklenir:
```
No haze: shadows are hard, fill is weak.
```
> ⭐ **Bu çift GUNES_MEZARI yazılırken (26.09.2026) yazıldı.** Kart §3.9 iki filmde
> (THE_HEALING_GROUND · THE_SLOW_RAIN) kullanılmıştı ve İngilizce karşılığı her
> seferinde elden yeniden yazıldı; §2 listesinde YOKTU.
> ⛔ **ÜÇ TUZAK:**
> ① Kartın kendi satırı *"gölge yumuşak ve SIĞ"* der (pus dolgu yapar). Pus YOKSA
>   bu satır DÜŞER ve gerekçesi yazılır [D74] — yukarıdaki tek cümle o gerekçenin
>   prompt karşılığıdır. ⛔ İki satır aynı filmde birlikte yazılamaz.
> ② *"Rüzgâr kumaşı kıpırdatmaz"* cümlesi hikâyeyle çakışabilir: GUNES_MEZARI'nde
>   yarı açık bir kapı oynuyor. Çözüm rüzgârı güçlendirmek DEĞİL, kapıyı OYNATAN
>   ŞEYİ değiştirmektir — kapıyı kadının geçişi oynatır, rüzgârın tek işi zeminde
>   ince kuru karı sürüklemektir. Ortam kartı hikâyeye uydurulmaz.
> ③ AUDIO satırı tizleri öldürür; **replikli filmde bu bir imkândır, arıza değil**:
>   kayıt/telsiz repliği 300-3400 Hz band-pass'la yazılınca ortam kartı ile ses
>   tasarımı aynı gerekçeyi paylaşır (GUNES_MEZARI: kayıt iki kez duyulur).
> ⚠️ Küre/ısı kaynağı gibi bir NOVUM varsa SINIRI aynı PHYSICS satırına yazılır
>   ("yalnız küre yukarıda kalır") — THE_KEPT_LIGHT'ta sınır sızdı ve sekiz mercek
>   kaçırdı. Sınır cümlesi sahne içinde BİREBİR aynı kalır (㉜⑥).

### §3.10 BASINÇLI İÇ HACİM (istasyon/üs içi · ~1 atm)
```
PHYSICS: Inside a pressurised hull at about one atmosphere, gravity is <0.30> g. Loose particles move with continuous momentum and settle, never hovering and never swirling like liquid.
AUDIO:   A steady low cabin hum, air moving through a vent, and her breathing inside the helmet. No dialogue. No music.
```

#### §3.10b TAM MİKROGRAVİTE ALT BANDI 🆕 30.09.2026 — kartın 0 g hâli
> Kart `gravity is <0.30> g` diyor ve bu **dönme g'si olan** bir gövde içindir. Gövde
> DÖNMÜYORSA (yörüngede serbest düşüş) sayı 0'dır ve o zaman §2b'nin rejim ayrımı
> cümlesi **zorunlu olur**: model "yürümek" fiilini 1 g verisinden çeker. Ölçülmüş
> çözüm — fiili MEKANİK SEBEBE bağla, sayıyı değil:
```
PHYSICS: Everything is in orbital free fall — continuous microgravity inside the pressurised hull and hard vacuum outside. A boot locks to the deck grating before the next step, a body is pulled forward by a rail, and a released object keeps exactly the motion it was given, drifting straight while turning slowly on its own axis.
AUDIO:   Nothing at all is heard through the vacuum, so every sound is carried by a hull or a suit — a steady low cabin hum, air moving through a vent, and breathing inside the closed helmet.
```
> ⭐ Bu satır İÇ ve DIŞ hacmi TEK cümlede birleştirir; sahnesi iki hacme yayılan
> filmde (kokpit + dış yanaşma aynı sahnede) ㉜⑥'nın "PHYSICS sahne içinde birebir"
> kuralını sayı uydurmadan karşılar. **Emsal: THE_LAST_GATE, 92/92 promptta aynı satır.**
> ⛔ AUDIO'nun sonundaki `No dialogue. No music.` REPLİKLİ filmde yazılmaz — replik
> varsa 2. cümlede tırnaklı satır, yoksa `No dialogue in this shot.` gelir.
> ⛔ MANYETİK TABAN UYARISI: manyetik bot eşyaya, saça ya da gövdeye yerçekimi VERMEZ;
> yalnız botu yüzeye bağlar. Aynı karede bağlı bot + süzülen alet YAZILIR, bağlı bot +
> düşen alet YAZILMAZ.

⭐ **AÇISAL MOMENTUM AYRI YAZILIR [TUR 22].** Çekirdeğin parçacık cümlesi yalnız
**doğrusal** momentumu söylüyor. Serbest cisim kadrajdaysa dönme ayrıca yazılır:

```
⛔ the panel drifts across the frame
✅ the panel drifts straight across the frame while turning slowly on its own axis
```
Deponun kanıtı: THE_GRAVITY_ANCHOR — *"floating debris lacks micro-rotation; the
smaller pebbles rise rigidly without individual spin"* (parçacık cümlesi 10/10'da yazılı).

> `< >` içindeki her sayı filme göre doldurulur ve **filmin bütün promptlarında
> AYNI KALIR**. İki farklı sahne iki farklı sayı taşıyorsa ⑥ FİZİK merceği onu
> bulur: bu deponun ölçülmüş en tekrar eden 🔴'larından biri.

⚠️ **19.09.2026 DÜZELTME — sayının faydası ÖLÇÜLEMEDİ.** İlk ölçüm "sayı yarıya
indiriyor" diyordu (tarifle 2 🔴 ↔ sayıyla 1 🔴). THE_FALLING_WORLD'ün ikinci
yarım raporları gelince sayısal filmin 🔴'sı **3'e** çıktı: iki film, aynı sahne
sayısı, **2 🔴 ↔ 3 🔴**. Sayı yine de yazılır — çünkü sayı yazılmadan çekirdeğin
`the stated gravity` cümlesi hiçbir şeyi kilitlemez — ama **"yarıya indirir"
iddiası geri çekildi** ve `25_` §3'ün araştırma sorusuna dönüştü.

---

## 2b. ⚖️ İKİ REJİM AYNI KADRAJDA — ayıran işaret adlandırılır [TUR 22]

Model "yürümek" fiilini 1 g verisinden, "süzülmek" fiilini 0 g verisinden çeker
ve ikisini aynı kareye koyar. Çözüm fiili **mekanik bir sebebe** bağlamaktır:

```
⛔ an astronaut walks through the bay while tools float around him
✅ PHYSICS: Microgravity. He locks each boot to the floor grating before the next
   step and pulls himself forward by the rail, while the loose tools drift
   weightlessly behind him.
```
Kaynak: TUR 22 rapor 3 · ÖLÇÜLMÜŞ (arXiv 2609.11242 — *"penalizing violations such
as objects interpenetrating solid meshes, reversing gravity…"*).
Deponun kanıtı: LOOK_UP 2 🔴 · GREEN_CEILING 2 🔴 · PAYLOAD 3 🔴 · LEANING_ROOM 2 🔴.

🆕 22.09.2026 · TUR 24: kaza/çarpma anında düşük g'de "falls · free fall · crashes"
kelimelerinin 1 g'yi çağırdığı hipotezi (THE_SLOW_RAIN 0,49 ↔ 4,27 m/s²), yerçekimi
sözlüğü ve çarpışmanın üç evresi → `FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU.md` §2.

---

## 3. 📋 ON BEŞ HATA SINIFI — ölçüm · önleyen cümle

> Her satır **≥ 2 filmden** kanıt taşır (`00_DERS_YAZIM_KONTRATI` §2b eşiği).
> Tam dökümü: `FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/03_PROMPT_HATA_SINIFLARI.md`

| # | sınıf | ölçüm | önleyen şey |
|:--:|---|---|---|
| 1 | ortamın ses yasası yok | **24/31 filmde hiç yok**, hiçbirinde tam | §2'nin `AUDIO:` satırı |
| 2 | temas füzyonu ⚠️ **TUR 22'de yeniden yazıldı** | 9 film hiç · 17 kısmi · 20+ 🔴 · cümle VARKEN de oluyor | §3b — cümle değil KADRAJ + ZAMANLAMA |
| 3 | giysi/donanım devamlılığı yok | 12 hiç · 13 kısmi | §1a ⑥ + Bible cümlesi birebir |
| 3a | asimetrik işaret hangi kolda yazılmamış | 3 film (askı · yama · bileklik kol değiştirdi) | `on his **left** upper arm` |
| 4 | ortam tarifle yazılmış | **14 film sayısız** | §2 PHYSICS satırı |
| 4a | sayı var, ortamın adı yok | 6 film | §2 — ad VE sayı birlikte |
| 4b | iki yerçekimi aynı kadrajda | 6 film [D200] | ayıran işaret **mekanik sebebe bağlanır** — §2b |
| 5 | eforun ŞİDDETİ sayısız | **29 film kısmi** · ⑧ tek başına **99 bulgu** | ⚠️ **TUR 22 bunu değiştirdi** — bkz. §5b |
| 6 | jeton sızıntısı | 2 film · 4 🔴 | §6 |
| 7 | metin yasağı ekranlı tasarımla çelişiyor | 6 film · 8 🔴 | sayaç metinsiz çözülür [D50/D78] ya da yasak o sahnede kalkar |
| 8 | dünya çapası yok — gök sahne sahne değişiyor | 8 film [D209] | dünya cümlesi film başına bir kez, her dış sahneye birebir |
| 9 | filmin ANA MALZEMESİ kilitsiz | 5 film | §5 |
| 10 | sayılabilir nesne rakamla yazılmamış | 5 film [D78·D151] | `four yellow bands across the chest` |
| 11 | arka plan envanteri kurulumla dönmüyor | 6 film | aynı kurulum harfi = aynı arka plan cümlesi BİREBİR |
| 12 | aksiyonun hedefi ve izi kadraj dışında | 6 film [D213] | atışın/darbenin İZİ ortamda kalır |
| 13 | ışık yönü saat yönüyle yazılmamış | 4 film [D193] | `one hard sun out of frame at 9 o'clock` |
| 14 | ses ile görüntü arasında zaman/sayı köprüsü yok | 5 film | replik bir SAYI söylüyorsa o sayı görsel prompta da girer |
| 15 | canlı anatomisi | 4 film | iki yönlü temas cümlesi + **referans paneli** [D168] |

---

## 3b. ✋ TEMAS — cümle yetmiyor, ÜÇ KARAR yetiyor [TUR 22 · 19.09.2026]

Deponun en ağır çözülmemiş sınıfı. İki bağımsız kaynak aynı şeyi söylüyor:
**negatif cümle yazmak temas füzyonunu durdurmuyor.**

```
DEPO ÖLÇÜMÜ (34 film · el kadrajda 617 sahne)   cümle VAR %11,8 ↔ YOK %5,6 · RR 2,10
LİTERATÜR (TUR 22 rapor 1)                      "avoiding a concept requires recognizing it"
                                                — negasyon, kavramı latent uzayda AKTİVE eder
MEKANİZMA (aynı rapor)                          VAE 8× uzamsal sıkıştırma: temas noktasının
                                                yüksek frekanslı sınırı aynı latent yamaya düşer
```

### ① ZAMANLAMA — temas klibin İLK 2 SANİYESİNDE kurulur ⭐ ölçülmüş

```
klip içi konum ↔ temas bulgusu payı (deponun 34 filmi)
  0-2 s   % 5,9   ⭐ buraya koy
  2-4 s   %19,4   ⛔ en kötü bant
  4-6 s   %15,2
  6-8 s   %12,1
  8-10 s  %13,8
```

**Kural:** temas ya **ilk karede zaten kuruludur** (I2V çıpası — eldiven nesneyi
tutuyor hâlde başlar) ya da **ilk iki saniyede** kurulur. TIMELINE satırının
`0.0s` girdisi temas taşır; `3.0s` ve sonrası taşımaz.
⚠️ Raporun "sona doğru daha da kötüleşir" tezi depoda **doğrulanmadı** — tepe
2-4 s'tedir, son bantlar ondan iyidir. Kritik olan **ilk iki saniye**dir.

### ② POZİTİF ARA KATMAN — yasak yerine görünür sınır

Negatif cümle kavramı çağırıyorsa, işi pozitif gövdede yaptır: iki cismin arasına
**görünür, adlandırılmış bir katman** koy.

```
⛔ NEGATIVE: … no merging, no phasing, no extra fingers …
✅ POZİTİF gövde:
   an off-white glove closes on the hard grey cuff, a bright steel ring between
   the two, the glove's ribbed cuff stopping a finger's width short of the metal
```
Renk zıtlığı + adlandırılmış ara parça (halka · sap kılıfı · toka · bant) o
bölgenin doku matrisini ayırır. ⬜ **Ölçülmedi** — ÖNERİ [TUR 22].

### ④ CÜMLE TEK YÖNLÜ — nesne-nesne geçişini HİÇBİR ŞEY kapsamıyor ⭐ yeni sınıf

Promptlardaki cümle **`hand-surface contacts`** diyor. 81 temas/geçiş bulgusunun
**26'sı el karışmayan** geçiştir ve hiçbir cümlenin kapsamında değildir:

```
"Yellow tether strap clips cleanly through the solid metal lander leg"   THE_DRY_ANCHOR S09
"the fabric strap phases through the solid metal floor pin"              THE_COUNTED_TURN S10
"the orange carabiner phases completely through the solid metal rail"    THE_COUNTED_TURN S16
"taut rope bends and clips through the brass lampshade"                  THE_LEANING_ROOM S05
"Floating canvas belt clips completely through torso"                    THE_STILL_SWARM S12
"Alien limb clips through suit shoulder plate"                           LOOK_UP S05
```

**Bunlar 🅐 değil 🅑'dir** — yazımla önlenebilir. Cümle **iki yönlü** yazılır:

```
✅ Hand-to-surface and object-to-object contacts both keep a clear structural
   boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout.
```

⚠️ Ama ①'in ölçümü hatırlanmalı: cümlenin kendisi koruyucu çıkmadı. Bu satırın
gerekçesi "kapsam boşluğunu kapatmak", "arızayı durduracağı" değil. Asıl çare
yine ① (zamanlama) ve ② (ara katman).

---

### ③ KADRAJ — temas anı perdelenir ya da atlanır

Okunurluk bedeli ağırdır ve **filmin olayı elle yapılan bir işse ödenemez**
(THE_COUNTED_TURN kayış-karabina filmi: cümle 22/25'te yazılı, **7 🔴**).
O zaman sıra ①'e döner: temas ilk karede kurulu başlar.

🆕 22.09.2026 · TUR 24: çok klipli sahnede ③'ün "an atlanır" çaresi **uygulanabilir**
hâle geldi — temas iki klibe bölünür (hazırlık / `CONTINUOUS ACTION:` ile sonuç).
Mikro el işlerinin gövde eylemine dönüşüm tablosu ve yürüme platosu:
`MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md` §1-§3 · `COK_KLIPLI_SAHNE_KILAVUZU.md` §3.6.

---

## 4. ⛔ PROMPTUN KAPATAMADIĞI ÜÇ SINIF — buraya emek harcama

Bu üçü **ölçüldü** ve yazımla kapanmıyor. Prompt cilası boşa emektir; her birinin
kapanma yeri farklı bir masadır.

| sınıf | kanıt | nerede kapanır |
|---|---|---|
| **vakumda ses** | SUSMAYAN `AUDIO:` 96/96 + `no exterior sound at all` → 4 🔴 · KRONOS 0/96 → 4 🔴 · depo ölçümü: AUDIO satırı RR **1,04** (etkisiz) | ⛔ **KURGU** — TUR 22 sebebi verdi: ses metinden değil **görüntünün anlamından** türüyor. Reçete: NLE'de **low-pass < 300-400 Hz** (tiz çarpışma/patlama kesilir, kalan boğuk alt uç ince atmosfer/kask estetiğine oturur) + **noise gate eşiği yüksek**. Ayrı ses kanalı (stem) alınamıyor. |
| **temas füzyonu** | COUNTED_TURN temas cümlesi 22/25 → **7 🔴** · DRY_ANCHOR 14/14 → **6 🔴** | ⛔ **KADRAJ KARARI** — temas anı perdelenir · eldivenle nesne arasına görünür ara katman (halka · sap kılıfı) konur · ya da öncesi ve sonrası gösterilip an atlanır. Karar **sahne haritasında** verilir, promptta değil |
| **filigran / köşe artefaktı** | 5 filmde `no watermark` neredeyse her promptta → hepsinde köşede | ⛔ **ARAÇ AYARI** [D150·D215] — KAPI 0'da ayar, sonra yeniden ihraç |

> ⭐ Ayrıca **durum merdiveni metinle tutmuyor**: FROST_LINE PHASE 1-4'ü kusursuz
> yazdı ve altı devamlılık bulgusu aldı; BENI_HATIRLAMA `creature keeps the same
> number of legs` cümlesini 34 promptta taşıdı ve yaratık altı bacak çıkardı.
> Bu kilit **REFERANS PANELİ** ister [D168], cümle değil.

---

## 5. 🎯 NOVUM KİLİDİ — filmin kendi olgusu en sık kilitsiz kalan şey

Ölçülmüş örüntü: **filmin ana malzemesi neyse, o kilitsiz.**

```
THE_STILL_SWARM      yüzen panel filmi   · parçacık cümlesi  2/14  → 6 bulgu, 2 🔴
THE_RESONANT_STRAND  yüzen levha filmi   · parçacık cümlesi  0/14  → 4 bulgu
THE_STANDING_WIRE    tel filmi           · telin kalınlığı sayısız → 2 bulgu
THE_UPWARD_FALL      ivme filmi          · ivme değişimi yazısız   → 1 🔴
THE_HARD_DOCK        kenetlenme filmi    · kenetlenme anı perdeleniyor
```

**Kural:** `02_KONSEPT_VE_RISK`'te novum kartı bir satır daha taşır —
**"taşıyıcı olgunun davranışı hangi SAYIYLA kilitli ve hangi sahnelerin
promptunda geçiyor"**. Negatif çekirdek bu işi yapmaz: çekirdek genel davranışı
yasaklar, novum ÖZEL davranışı ister ve pozitif gövdede sayıyla yazılır:

```
each panel keeps a slow constant drift of about one panel-width every four seconds
```

---

## 5b. 💪 EFOR — sonuç sayısı DEĞİL, beden + duraksama [TUR 22]

Kılavuzun ilk sürümü `the lever moves 4 cm in the first second and 1 cm in the
last` diyordu. TUR 22 bunun **ters** çalıştığını söylüyor: sonuç odaklı cümle
modeli pürüzsüz bir kinematik yörünge çizmeye iter ve figürü **ağırlıksız**
render eder; kuvvet hesabı yapan bir iç mimari yok.

```
⛔ sonuç sayısı      the lever moves 4 cm in the first second and 1 cm in the last
⛔ düz yavaşlama     he pulls the lever slowly        → ağır çekim ARIZASI: toz da,
                                                        kumaş da, arka plan da yavaşlar
✅ beden + duraksama he pulls the lever, halts abruptly holding the tension,
                     then pulls again; his forearm tightens through the suit and
                     his shoulders drop into the second pull
```

```
KLİPTE EN ÇOK 2-3 BEDEN İŞARETİ. Fazlası "özellik kanaması" üretir.
✅ tutan  : aynı yöne çalışan çift   "leans back heavily while pulling"
⛔ tutmaz : asimetrik yük            "right arm pulls hard while left arm hangs loose"
            → difüzyonun simetri önyargısı iki kolu senkronlar
OPAK VİZÖRDE tek okunur işaret GÖVDEdir; orta plan en güvenli ölçektir.
```

⬜ **Etiket: ÖNERİ.** Bu biçim tek değişkenle sınanmadı; deponun ⑧ EFOR
bulgularıyla (99) uyumlu ama A/B'si yok.

🆕 22.09.2026 · TUR 24: bu bölümün SÖZLÜĞÜ (destek · gövde · işaret · duraksama ·
direnç sıfatları · eldiven · saydamlık tuzağı [D175] · çok klipli sahnede ödeme) →
`FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU.md` §1. TUR 24 rapor 2A'nın "two inches over eight
seconds" kalıbı bu bölümle çeliştiği için REDDEDİLDİ; çelişkide bu bölüm kazanır.

---

## 6. 🔤 JETON SIZINTISI — promptun kendi kelimesi kadraja yazılıyor

| film | promptta | ekranda |
|---|---|---|
| THE_PAYLOAD | `PHASE 1` (durum merdiveni etiketi) | **göğüs plakasına basıldı** 🔴 |
| THE_PAYLOAD | `EVA` (teknik kısaltma, 10 promptta) | **sırta basıldı** 🔴 |
| THE_ROSE_COAT | `rose` (renk adı, **139 kez**) | **ekrana yazıldı** 🔴 ×2 |
| **THE_SOLAR_MIRROR** | **`S04` — SAHNE ETİKETİ** | **hava kilidi gövdesine basıldı** 🟠 ×2 |
| **THE_CRACKED_HELMET** | `ORION` | **göğüs kutusuna yazıldı** 🟠 |

Metin yasağının 12/13 ve 21/24 oranında yazılı olması kurtarmadı; THE_SOLAR_MIRROR'da
yasak **12/12'de** yazılıydı ve `S04` yine basıldı.

⭐ **Sahne etiketi yasağı ölçüldü:** bu kural aşağıda önce VARSAYIM olarak yazılmıştı
(`ne S07, ne R3`); THE_SOLAR_MIRROR onu **ölçülmüş vakaya** çevirdi (19.09.2026).

**Kural:** prompt gövdesinde **BÜYÜK HARFLİ kısa jeton yazılmaz** — ne `PHASE 1`,
ne `EVA`, ne `S07`, ne `R3`. Defter dili prompta girmez; durum düz cümleyle yazılır:

```
⛔ PHASE 2  red dust on both knees
✅ red dust on both knees and glove palms, a thin matte white rime on the suit
```

Ayırt edici kelime **tek başına bırakılmaz**, her geçtiği yerde bir nesneye bağlanır
(`rose-pink` değil `a rose-pink quilted coat`).

> ⚠️ **Dürüst kayıt:** THE_FROST_LINE `Wear state: PHASE 2` cümlesini 25 promptta
> taşıyor ve **hiç sızdırmadı**. Ayıran şeyin ne olduğu bilinmiyor; sınanmamış
> hipotez, FROST_LINE'ın jetonu bir cümlenin içine gömmesi, PAYLOAD'ın satır
> başında yalnız bırakmasıdır. Kural bu yüzden yasak değil **uyarıdır**.

🆕 **22.09.2026 · ADAY-98 — KAMERA SATIRININ KENDİ KELİMESİ:** THE_SLOW_RAIN S14 ve
THE_STOLEN_SKY PART 1'de kadraja **plansız kamera tripodu** girdi; iki filmin CAMERA
satırı da `… on a fixed locked-off tripod …` diyordu. ÖNERİ (bedava, ölçülmedi):
`a locked-off camera`. → `MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md` §4.2 ·
`DERSLER/GOZLEM_DEFTERI.md` ADAY-98. Aynı sınıfın durum tarafı: hasar/durum
**köşeli büyük harfli blokla** yazılmaz (`[SPEC DAMAGE STATE: …]` — TUR 24 R3) →
`POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU.md` §2.

---

## 7. 📏 ÖLÇÜM — yazdıktan sonra, üretmeden önce

```bash
# filmin çekirdek kapsaması — hangi cümle hangi sahnede düşmüş
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/prompt_hata_analizi.py --kilit <FILM>
```

⛔ `HİÇ YOK` satırı varsa üretime girilmez. `KISMİ` satırı varsa hangi sahnede
düştüğü bulunur ve kapatılır — bu deponun 🅑'sinin en büyük kaynağı budur.

**QA partisinden sonra** aynı betik filmin karnesini verir:

```bash
python3 .../prompt_hata_analizi.py --film <FILM>     # 🅐 / 🅑 dağılımı
```

```
🅑 ORANI HEDEFİ: %20 altı ulaşılabilir — ölçüldü.
   SUSMAYAN %13 · THE_FALLING_WORLD %15 · THE_COUNTED_TURN %16 · BENI_HATIRLAMA %21
   %50 üstü çıkan filmde soru tek: HANGİ CÜMLE EKSİKTİ. Cevabı --kilit verir.
```

---

## 8. ⚠️ BU KILAVUZUN SINIRI

```
· Kapsama %74 olan THE_BENT_GRASS 🅑 %83 verdi (n=6, küçük örneklem).
  Çekirdek kapsaması GEREK şarttır, YETER şart değildir.
· Ölçüm 31 filmden geldi; 29 film (QA_SPEC GRID yok) ve 6 film (prompt sahne
  başlığı yok) kapsam dışında — 05_ESLESMEYENLER.md'de adlarıyla duruyorlar.
· 🅒 29 bulgu MERCEK tarafındaki kusurdu (SPEC okunmadan koşan mercek · başlık
  kartını ① merceğine bulgu yazmak · tasarım kararını kusur saymak). Onlar bu
  kılavuzun değil, qa-isle akışının işidir.
```
