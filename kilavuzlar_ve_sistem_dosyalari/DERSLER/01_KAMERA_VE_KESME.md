# 📚 DERSLER — Kamera ve Kesme

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Kamera ve Kesme** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🔴 DERS 1: TEK ÇEKİM KURALI — AI KESIYOR

**Kaynak:** Canopy World 2/10 | Deep Root 3/10 | Slow Tide 3/10
**Sorun:** AI video modelleri sahne içinde kesme yapıyor. 3 filmde de tekrarladı — EN YAYGIN HATA. "No cuts" yazmak yeterli değil.

**ÇÖZÜM — Her video prompt'una eklenecek:**
```
CONTINUITY LOCK: This is a SINGLE UNBROKEN CAMERA TAKE. The camera must not
teleport, jump-cut, reset position, change angle suddenly, or transition to a
different setup. Every frame must flow directly and continuously from the
previous frame. The camera moves only as specified in the MOTION description
below — no additional movements, no resets, no edits.

ANTI-CUT NEGATIVE: No cuts, no transitions, no dissolves, no fades, no jump
cuts, no montage, no editing, no multiple camera angles, no scene changes, no
camera teleportation, no video game chase-cam.
```

**NOT:** Her sahne AYRI bir 10 saniyelik video olarak üretilmeli. Sahneler birleştirilip tek bir uzun video olarak üretilMEMELİ.

---

## 🔴 DERS 22: AKSİYON SÜREKLİLİĞİ — İMKANSIZ GEÇİŞLER

**Kaynak:** The Kaleida Crash QA — Kamera: 3/10, Hareket: 4.5/10
**Sorun:** 1:10'da karakter bir yerde yürürken aniden bambaşka bir yerde zıplıyor — arka plan tamamen değişiyor, fiziksel olarak imkansız bir konum değişikliği oluyor. Özellikle aksiyon sahnelerinde (atlama, koşma, tırmanma) AI sahne bağlamını kaybediyor.

**ÇÖZÜM — Aksiyon/hareket değişimi içeren her sahneye eklenecek:**
```
ACTION CONTINUITY RULE: During any physical action (jumping, climbing,
running, crossing), the background environment must remain SPATIALLY
CONSISTENT from the start to the end of the action. The character
cannot teleport to a new location mid-action. The ground, sky,
surrounding objects, and spatial relationships visible at the START of
the action must still be visible and consistent at the END of the
action. No sudden background swaps, no environment teleportation, no
new terrain appearing mid-jump.
```

---

## 🔴 DERS 33: COMPILATION CUTS AND ZERO-G PHYSICS (THE LAST CROSSING BLACK HOLE FILM)

**Kaynak:** THE_LAST_CROSSING_BLACK_HOLE_FILM.md Compilation QA (Overall 4/10)
**Sorun:** Model tek çekim (single-cut) kuralını ihlal ederek dışarıdan içeriye veya çevreye hard cut yapıyor. Ayrıca sıfır yerçekimindeki kargo dumanı, enkaz ve kokpit içi süzülen nesneler momentumdan yoksun, statik (2D asset gibi) asılı kalıyor. "Cinematic lighting" gibi ifadeler bloom efektine (waxy/smoothed skin) yol açıyor. Karakter teması ve kıyafet konumları (rozet, yakalık) frame-rate dalgalanmalarına maruz kalıyor.

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**
1. **Camera / Negative:** Negatif promptlara sadece "No cuts" demek yetmiyor. Şunlar eklenmeli:
```
cuts, edits, camera resets, dissolves, multiple shots
```
2. **Lighting / Skin:** "Cinematic lighting" veya "No bloom" yerine çok daha keskin ışık ve doku ifadeleri kullanılmalı:
```
sharp directional light, photorealistic skin pores, 0% bloom
```
3. **Physics / Particles:** Süzülen obje ve duman tariflerinde sadece "floating debris" veya "volumetric" demek momentumu sağlamıyor. Fiziksel atalet açıkça belirtilmeli:
```
particles moving with continuous physical momentum, volumetric dispersing smoke
```

---

## 🔴 DERS 68: KESME PROMPTUN İÇİNDE TUTMADI — PLANLI KESME ÇIKMADI, PLANSIZ KESME SIZDI

**Kaynak:** THE DAWN FRONT teknik QA (05.08.2026) — Kamera 3/10 ·
`0:15 — 🔴 unplanned cut in S1` · `0:23 — 🔴 unplanned cut in S2` ·
`0:02.5 — 🟠 camera tracks rover (lockoff planlıydı)` · ayna sayacının
3. vuruşu "full at N/A" · S10 geri vites beati iki mercekte de okunamadı

**Sorun:** Bu, deponun ilk "kesme promptun içinde" denemesiydi (plan §0.2 —
12 kesme, saniyeleri yazılı, CUT SCHEDULE bloklarıyla). Sonuç üç yönlü
başarısızlık:

```
① Planlı kesmeler yazıldığı kadrajla ÇIKMADI — kesme sonrası kadrajlar
  (ayna 3. vuruşu, geri vites eli) hiç üretilmedi
② Kesme İZNİ tek çekimli sahnelere SIZDI — "single unbroken take" yazan
  S1 ve S2'ye model kendi kesmesini koydu
③ Sabit lockoff yerine tracking geldi — kesme serbestisi kamera
  serbestisi olarak genellenmiş görünüyor
```

Ve en sinsi belirti: **süre tutarken içerik kaydı.** 141 s ≈ plan 140 s,
ama S6 (motor kapatma) · S9 (tekerlek çökmesi) · S10 (SEÇİM) · S12
(overview) beat'leri slotlarının içinde yok. Ders 62 finalin düştüğünü
ölçmüştü; bu onun orta-film hâli — **slot dolu, beat boş.** Süre kontrolü
içerik kontrolü değildir.

Plan §0.2.2 bu riski açıkça yazmıştı ve §0.20 PLAN B tetiği tanımlıydı:
"karar İLK SAHNE üretildikten sonra verilir... test sahnesi S0." **Test
adımı atlandı, film komple üretildi** — mimari arızası 14 sahneye ödetildi.

**ÇÖZÜM — PROMPT DEĞİL, KARAR:**

```
① PLAN B DEVREDE: çok çekimli 7 sahne SEGMENT BAŞINA AYRI üretilir
  (26 klip), kesme kurgu masasında atılır. Segment blokları zaten
  self-contained yazıldığı için yeni metin gerekmiyor (plan §0.20).
② TEST ADIMI ATLANAMAZ: mimari denemesi içeren her filmde tetik sahnesi
  üretilip DOĞRULANMADAN kalan sahneler üretilmez. Tetik, planın
  kendisine yazılır ve teslim kapısına eklenir.
③ TESLİM KAPISINA EK (Ders 62 kapısının 5. maddesi): her sahnenin PLAN
  beati kurguda OKUNUYOR mu — süre değil, beat sayılır.
```

> 🔗 Ders 1 ailesinin kapanışı: kesmeyi yasaklamak tutmadı (1), kesmeye
> izin verip saniyesini yazmak da tutmadı (68). Ölçülmüş tek çözüm hâlâ
> aynı: **sahneleri/segmentleri ayrı üret, kesmeyi kurguda al** — 7-9 dk
> formatının Kamera 7/10 kanıtı (Slow Stone satırı).

---

## 🟡 DERS 86: İKİ KİŞİLİK KADRAJDA "KİM SOLDA" KİLİDİ YOK — EKRAN YÖNÜ KİLİDİ BUNU KAPSAMIYOR

**Kaynak:** THE THIRD DUNE QA (11.08.2026) — 🧍 KARAKTER Kesme 6/10 ·
`0:10 erkek solda / kadın sağda ↔ 0:20 kadın solda / erkek sağda`

**Sorun:** Filmin SPATIAL LOCK bloğu dört sabit tanımlıyor ve dördü de
tuttu: araç hep sağ üçte bir · yürüyüş hep sola-sağa · kum sürüklenmesi
hep sola-sağa · fırtına ve güneş hep solda. Ama kilit **iki figürün
birbirine göre dizilimini** hiç söylemiyor. Sonuç: karakterler kesmeler
arasında sol/sağ yer değiştirdi. Tek başına küçük bir kusur; iki
karakterli bir filmde ise seyircinin "hangisi jeolog" refleksini
her kesmede sıfırlar — bant rengi ayrıştırması (çalışan çapa) bu yüzden
tek başına yetmiyor.

Uzamsal kılavuz tek özneli filmler için yazıldı: özne bir kişiyken
"ekran yönü" ile "dizilim" aynı şeydir. İki kişide ayrışır.

**ÇÖZÜM — prompt'a eklenecek** (iki insanlı her sahnenin SPATIAL LOCK
satırına, sahneye göre sol/sağ atamasıyla):

```
The ICE-BLUE figure stays on the screen-left side of the pair and the
DEEP-VIOLET figure on the screen-right side in every shot; their
left-right order never swaps.
```

Kadrajın öznesi tek kişiyse (detay, tek kol, tek figür) cümle düşer.
Sıralamanın bilinçli değiştiği sahne varsa — biri öne geçer, biri
geride kalır — o sahnede cümle yerine değişimi TARİF ET; kilit
sessizce bırakılmaz, açıkça devredilir.

---

## 🔴 DERS 104: EN PARLAK IŞIK YÖN MIKNATISIDIR — HEDEF-DİLİM + YÖN CÜMLESİ YETMEDİ, GÖVDE YÖNELİMİ YAZILMAYINCA KOŞUCU IŞIĞA DÖNDÜ

**Kaynak:** THE BLACK CRADLE S4 (ŞAFAK DUVARI) üretim gözlemi — proje sahibi, 16.08.2026. Kadrajda soldan yükselen şafak seti (tek baskın ışık) + sağda lander; astronotlar landera değil, TERSİNE — ışığa doğru — koştu.
**Sorun:** Prompt, uzamsal kılavuzun §6.1 kuralına UYGUNDU: hedefin ekran dilimi ve koşu yönü aynı cümledeydi ("sprint from screen-left toward frame RIGHT... lander frame right"), `prompt_kontrol` yön kapısından geçmişti. Yine de yön ters çıktı. Mekanizma: İLKE 4'ün üçüncü ekseni (KONUM ≠ YÖNELİM ≠ HAREKET) promptta boştu — **gövde yönelimi (omuz hattı) hiç yazılmamıştı** ve model onu serbest seçerken kadrajın EN PARLAK / EN ANLAMLI öğesine yöneldi. İki bilinen refleks üst üste bindi: ① portre refleksi (koşan figürü kameraya/ışığa döndürme, §6.2 uyarısı) ② "ışığa koşan insan" eğitim klişesi (gün doğumuna koşu). Siyah-üstü-siyah filmde risk katlanır: hedef (lander) neredeyse görünmez bir siluet, dikkat çekici tek şey ışıktır.
**Betik notu:** `prompt_kontrol.py` yön kapısı KONUM+HAREKET'i arar ("çapasız toward"); YÖNELİM eksenini aramaz — bu ders betiğin göremediği sınıftadır, denetim insan gözüyle yapılır.

**ÇÖZÜM — DÖRT KANALLI YÖN KİLİDİ (baskın ışık kaynağı olan her hareket sahnesine):**
```
① HEDEF-DİLİM + YÖN (zaten vardı): "the lander at frame right; they run
   from screen-left to screen-right toward it"
② GÖVDE YÖNELİMİ: "shoulder lines square to screen-right, matching the
   direction of travel; no runner faces the camera or turns back"
③ IŞIĞA GÖRE POZ (mıknatısı etkisiz kılan kanal): "their BACKS are to
   the dawn light — the warm band rims their back silhouettes; their
   faces and the ground ahead are lit only by their own lamps"
   → ışık-gölge kanıtı yönle AYNI ŞEYİ söyler; model ikisini birden
   ters çeviremez
④ NEGATİF: "no one runs toward the light; no direction reversal; no
   figure faces screen-left while moving; no mirrored composition"
```
**Genelleme:** Kural yalnız koşu değil, HER yönlü hareket için geçerlidir — araçlar dahil (kıç önde yanaşan araçta "hangi uç önde" cümlesi + "never nose-first" negatifi aynı dört kanaldır, uzamsal kılavuz §5.1 ①). Baskın ışık hangi taraftaysa, hareketin ışıkla ilişkisi (ışığa doğru / ışıktan uzağa / ışığa paralel) promptta AÇIKÇA yazılır.

**⭐ İKİNCİ VAKA VE KAÇIŞ BASAMAĞI (aynı gün, aynı sahne):** Dört kanallı kilit yazıldıktan sonra ikinci deneme de düştü — model bu kez gemiyi ARKA PLANA atıp koşucuları KAMERAYA döndürdü: frontal/portre refleksi, dört yazılı kanala rağmen kompozisyonu ele geçirdi. Ölçülen sonuç: **yanal (profil) koşu, baskın-ışıklı kadrajda iki denemede de tutmadı.** Kaçış basamağı refleksle SAVAŞMAK değil, HİZALANMAKTIR: kamera hedefin (landerin) yanına taşındı — kameraya koşu = hedefe koşu; nötr çekim (uzamsal kılavuz §6.3, dizide en fazla bir). "Gemi arkada" hatası yapısal olarak kapandı: ön plan gövde kenarı + "the lander is NEVER behind the runners; no craft appears in the background" negatifi.
```
KURAL: Dört kanallı kilit bir sahnede İKİ kez yenilirse üçüncü
yeniden yazım denenmez — kamera hedefe taşınır ve hareket kameraya
doğru kurulur (nötr çekim). Modelin frontal refleksi yanlış cevaptan
doğru cevaba çevrilir.
```
**SONUÇ (17.08.2026):** V3 kompozisyonu İLK denemede tuttu (operatör
onayı). Ders, UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU'na **Sürüm 3**
olarak işlendi — mekanizmalar §6.7 (ışık mıknatısı) ve §6.8 (frontal
refleks + iki yenilgi kuralı + V3 kompozisyon şablonu); kanıt zinciri
§0.1 ve §11'de. Tam denetim maddeleri kılavuz §10.1-10.2'de.

---

## 🔴 DERS 174: NOVUM GELDİ, İŞARETİ YUVARLANDI — "SCREEN-RIGHT" MODELDE BİR REFERANS DEĞİLDİR; YÖN BİR KOORDİNATA DEĞİL, KADRAJDAKİ BİR NESNEYE BAĞLANIR

**KAPI:** ⬜ AÇIK — betik tarafı yok. `prompt_kontrol.py`'nin yön kapıları
KONUMU arar, YÖNELİMİN İŞARETİNİ aramaz (D104'ün "betik göremez" satırının
aynısı, bu kez yatma ekseninde).
**TEKRAR:** 0 · 02.09.2026 THE LEANING ROOM

**Kaynak:** THE LEANING ROOM QA (02.09.2026) — kare 2280-2340 (1:16-1:18)
çıkarıldı ve BAKILDI. Filmin novum'u ekrana GELDİ: tavandan sarkan pirinç
sarkaç lamba altı karede kesintisiz, tek yönde, salınmadan yatıyor ve duruyor.
Prompt ne istediyse o oldu — **yönü hariç.**

```
PLAN (Camera Bible + SPEC C bloğu, 12/12 sahnede geçerli):
   "SANCAK bant penceresi HER kadrajda SCREEN-RIGHT'tadır.
    YATMA HER ZAMAN SCREEN-RIGHT'a doğrudur. Ters dönüş YOKTUR."

EKRAN:
   S7 · 1:18  siyah daire SCREEN-RIGHT ✅   lamba SCREEN-LEFT'e yatıyor ✗
   S9 · 1:35  gevşek eşyalar SCREEN-RIGHT korkulukta ✅

   → Aynı film, iki sahne, iki zıt "aşağı". Novum bir YÖNDÜR; yönü
     yuvarlanınca izleyici onu yön değil SALINIM olarak okur — nitekim
     sekiz merceğin dördü lambayı "swinging lamp" diye yazdı.
```

⭐ **MEKANİZMA — "SCREEN-RIGHT" BİR NESNE DEĞİL, BİR KOORDİNATTIR.** Model
kadrajı koordinatla değil, İÇİNDEKİ ŞEYLERLE kurar. Aynı promptta iki cümle
vardı ve model ikisine iki farklı sadakat gösterdi:

```
✅ "a perfect black circle ... holds in the right third of the frame"
   → NESNE + konum. TUTTU, göründüğü her sahnede.
✗ "the lamp lies far over toward screen-right"
   → yalnız KOORDİNAT, referans nesne YOK. İşaret yazı-tura.
```

Yatma DAVRANIŞI (tek yönlü, salınımsız, durup kalan) kusursuz üretildi çünkü
o cümle FİZİKSEL bir tarifti. Yatma YÖNÜ üretilmedi çünkü o cümle bir kroki
koordinatıydı. **Model davranışı öğrenir, koordinatı öğrenmez.**

⛔ **VE BU D104'ÜN TERSİ, AYNI AİLEDEN.** D104'te model özneyi en parlak ışığa
ÇEVİRİYORDU — yönü bir NESNE belirliyordu, yanlış nesne. Burada hiçbir nesne
belirlemiyor, o yüzden işaret serbest kalıyor. İkisinin ortak dersi: **yönü hep
bir nesne belirler; onu sen seçmezsen model seçer.**

**ÇÖZÜM — ÜÇ SATIR, ÜÇÜ DE PROMPT TARAFINDA:**

```
① YÖN CÜMLESİ HEDEF NESNEYİ AYNI CÜMLEDE ADLANDIRIR.
   ✗ "the lamp leans over toward screen-right, sixty-eight degrees off vertical"
   ✓ "the lamp leans toward the window that carries the black circle — the
      same side of the frame the black circle is on — sixty-eight degrees off
      vertical, and its lower edge points at that circle"
   Nesne kadrajda görünmüyorsa yön cümlesi de yazılmaz: görünmeyen hedefe
   yön verilemez.

② İKİNCİ BİR CİSİM AYNI YÖNÜ TEYİT EDER, AYNI KLİPTE.
   Tek gösterge tek yazı-turadır. "every loose object on the table slides the
   same way the lamp leans, toward that same window" — iki bağımsız nesne
   aynı yöne giderse model işareti tek seferde çözer.

③ NEGATİF KOORDİNATLA DEĞİL NESNEYLE YAZILIR.
   ✗ "no direction reversal"        (neyin tersi belli değil)
   ✓ "nothing ever leans or slides away from that window; the lamp never
      points at the panelled wall"
```

⚠️ **PLAN TARAFI YETMEZ.** Bu filmde yön kilidi Camera Bible'da, SPEC'in C
bloğunda ve sahne haritasında YAZILIYDI — üç yerde. Model üçünü de okumaz;
okuduğu tek şey o sahnenin prompt gövdesidir [kural ③].

> 🔗 Ders 104 (ışık mıknatısı — yönü yanlış nesne belirler) · Ders 157 (novumun
> taşıyıcısı) · Ders 172 (aynı filmde taşıyıcının kordonu) · Ders 127 ·
> UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU §6.1


---

## 🔴 DERS 210: KAFİYE ÇİFTİ VE LOCKOFF PROMPTTA DEĞİL NİYETTE KALDI — KAPANIŞ AÇILIŞIN KAMERA CÜMLESİNİ TAŞIMADI, SABİT KAMERA KLİBİN SON SANİYELERİNDE KENDİLİĞİNDEN YAKLAŞTI

**FREKANS:** 4 film · THE AMBER LATTICE (mod V · ⑨ 5,7 — kapanış Setup J, açılış A) · THE CRACKED HELMET (mod D · ⑨ 2,1 — A ↔ H; 11 klibin 6'sında plansız push-in) · THE RING WALKER (mod V · ⑨ 4,8 — açılış lander ≠ kapanış gemi) · LOW_POWER (mod V · ⑨ 5,3 — A' 10° dutch, çapa %12 kaymış; S5 son 10 s'de %5 push-in)
**DEĞİŞEN SATIR:** Kapanış sahnesinin CAMERA satırı = açılış sahnesinin CAMERA satırı **BİREBİR** (kurulum iskeletinde aynı harf) + SPEC B `DÖNGÜ KANITI` satırına harf çifti `A ↔ A`; her video promptunun TIMELINE son satırı `hold — the frame does not move` ve CAMERA satırında `absolutely zero camera movement`
**KAPI:** BETİK · `prompt_kontrol.py` ⑩④ (iskelet — aynı harf, aynı cümle) · LİSTE · ⑨ KADRAJ raporunun `LOCKOFF HELD n / n` ve `RHYME PAIR` satırları
**TEKRAR:** 0

**Kaynak:** THE CRACKED HELMET QA (10.09.2026, ⑨ mod D) — `0:00 (S1) Setup A side-on wide vs 1:40 (S11) Setup H rear wide shatters visual loop` · `6 out of 11 clips feature unmotivated slow push-in`. Zincir ADAY-25 · 39 · 54 · 81 · 83 · 40 · 82. ⚠️ Dördünün üçü mod V ⑨ — plan uydurma riski [[D190]]; CRACKED HELMET mod D ile doğrulanmış.

**Örüntü:** Kafiye çifti PLAN'da niyet olarak yazıldı ("açılış-kapanış çifti"), kapanış promptunda açılışın kamera cümlesi kopyalanmadı; model yeni bir kurulum üretti. Lockoff'ta ise "fixed camera" cümlesi var ama klip sonunda motorun varsayılan yavaş yaklaşması yazılı bir "hold" ile bastırılmadı. AGENTS §8'in üç kalite kararından biri "sabit lockoff kamera" — kararın prompt satırı yoktu.

**ÇÖZÜM:**
1. Kurulum iskeletinin ilk ve son harfi aynıdır (`A … A`); betik ⑩④ aynı harfin cümlesini birebir ister — kafiye çifti bu kuralın alt kümesidir.
2. Video TIMELINE'ının son satırı her zaman `… — hold: <kadraj değişmez>`; CAMERA satırı `absolutely zero camera movement` (`KILAVUZ` §7 §IMAGE_VIDEO şablonu).
3. ⑨ raporunda `LOCKOFF HELD` = klip sayısı olmalı; eksik her klip 🔴.

🔗 [[D131]] · [[D184]] · [[D194]] · `ACILIS_KAPANIS_CIFTI` · AGENTS §8
