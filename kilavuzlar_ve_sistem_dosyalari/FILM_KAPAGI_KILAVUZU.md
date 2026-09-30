# 🖼️ FİLM KAPAĞI KILAVUZU — her filme İKİ aday, TEK deney

> **Ne bu dosya:** YouTube film kapağının (küçük resim) seçilmesi, yazılması, üretilmesi,
> kontrolü, yayın testi ve öğrenme kaydı — bu deponun filmlerine (yüzsüz astronot · opak
> vizör · 10 s klip · Bible ile kilitli kimlik) göre. Her film `<FILM>_KAPAK.md`'de **iki
> aday prompt** (A · B) taşır; ikisi tek bir deney sorusunu sınar ve YouTube'un başlık/kapak
> testine birlikte girer.
>
> **Kaynak:** sahibin araştırması `URETIM_ONCESI_ANALIZ/26_YOUTUBE_FILM_KAPAGI_KILAVUZU_VE_SABLONLAR.md`
> (20.09.2026 · 7 YouTube yardım sayfası + 2 W3C belgesi · 24 bölüm · doldurulabilir şablonlar).
> O belge KAYNAK ve tam şablon setidir; bu dosya onu deponun akışına indirir. Eski
> `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` kanıt olarak durur, ölçü değildir (§0 ③).
>
> **İşaretler (kaynaktaki dört düzey):** **Y** YouTube'un yayımladığı özellik · **D**
> okunabilirlik/erişilebilirlik dayanağı (W3C) · **U** uygulama önerisi · **H** doğrulanmamış varsayım.

---

# 0. ⚠️ DÜRÜST KAYIT

```
① KAPAK = platforma yüklenen küçük resim. Filmin süresine eklenen jenerik ya da klip DEĞİL.
② HİÇBİR KAPAK BU KANALDA ÖLÇÜLMEDİ (08_YAYIN_PERFORMANS_TABLOSU boş). Sayı, oran, "yüz
   %25-40 CTR artırır", "%7 CTR viral" gibi eşikler ÖLÇÜ DEĞİLDİR (Y: CTR içerik · izleyici ·
   gösterim yerine göre değişir — answer/7628154). Karşılaştırma birimi kendi benzer videoların.
③ ESKİ KILAVUZUN SAYI KATMANI KAPANDI (20.09.2026): KAPAK_FOTOGRAFI_MIMARISI §2 yüz/13 ms/%60
   kadraj · §7 CTR skalası · 1280×720 teslim · "A/B altyapısı yok" — hepsi kanıt, ölçü değil.
   Dosya silinmedi (dışarıdan atıf alıyor: PAKETLEME §0 · YAYIN §2.2 · 08 §5).
④ SAYI BURADA DURMAZ: çözünürlük · alt sınır · dosya boyutu · test varyant sayısı · CTR
   → apexaic/DIS_SAYILAR.md §1 (tarihli). Bu dosya adres verir.
⑤ PROMPT METİNSİZDİR. Film adı kapakta VARSAYILANDIR ama ayrı yazı katmanında, post'ta
   eklenir [Ders 9/34/45 · D138]. Prompt tek harf istemez; metin üreten araç kullanılırsa
   harf harf kontrol (kaynak §17).
⑥ İKİ ADAY, ÜÇ DEĞİL. YouTube testi üçe kadar varyant alır (Y); depo iki ile başlar — üçüncü
   aday yalnız ilk iki testin sonucu okunduktan sonra, o sonucun sorusuyla açılır.
```

---

# 1. 🧭 ÇALIŞMA SIRASI — sekiz adım, depoda nerede

| # | adım (kaynak §02) | depoda | ne zaman |
|---|---|---|---|
| 1 | hedef izleyici + gösterim yüzeyi | `<FILM>_YAYIN_PAKETI` `AUDIENCE:` · yüzey: YouTube yatay (Shorts kapağı ayrı, §9) | yazım adım 11 |
| 2 | kapak + başlık ortak vaadi | `<FILM>_KAPAK.md` VAAT bloğu ↔ `YAYIN_PAKETI` TITLE ①②③ (PAKETLEME §4 vaat büyütme sınırı) | adım 10–11 |
| 3 | vaadi taşıyan AN + gerçek görsel öğeler | PLAN sahne haritası + vuruş tablosu → `<FILM>_KAPAK.md` AN tablosu (üç aday, iki üretilir) | adım 10 (PLAN'dan sonra) |
| 4 | yerleşim · ölçek · bakış/yön | prompt COMPOSITION satırı · PAKETLEME §2 üç odak · UZAY_USSU ölçek şahidi | prompt yazımı |
| 5 | ışık · renk · yazı | prompt LIGHTING satırı · ışık = filmin o sahnedeki ışığı (Lighting Bible) · yazı post katmanı | prompt yazımı |
| 6 | küçük boyut + gerçek arayüz kontrolleri | §7 — 320×180 · 160×90 · gri · açık/koyu arayüz · telefon · süre etiketi | üretimden sonra |
| 7 | anlamlı farklı adaylar | §4 — A ve B, tek değişken | prompt yazımı |
| 8 | yayın testi + öğrenme | §10–§11 → 08_YAYIN_PERFORMANS_TABLOSU · Kart Y | yayın |

⛔ Kapak anı **PLAN'dan sonra, prompt üretiminden önce** seçilir; üretilmiş klipler arasında
"en güzel kare" aranmaz (PAKETLEME §1 · D114). Üretim sırası D168: kapak karesi DORUK →
merkezî seçim → kapanış → S0'dan sonraki dördüncü üretim halkasıdır.

---

# 2. 🔒 SABİT KARARLAR — aday üretilmeden yazılır (kaynak §03)

`<FILM>_KAPAK.md` başlığındaki SABİTLER bloğu. İki aday arasında bunlar DEĞİŞMEZ:

```
FİLMİN RESMÎ ADI          PLAN başlığı — kısaltılmaz, farklı yazılmaz
KAPAK METNİ               varsayılan: film adı (İngilizce) · post katmanı · dil sürümleri ayrı (Y: çok dilli kapak, uzun video)
FİGÜR SAYISI              anın kadrosu — NEGATIVE count cümlesiyle aynı sayı
VİZÖR KURALI              Character Bible'dan: opak → yüz/göz yok, yansıma da yok; berrak → D79 cümlesi (kaynak §10)
KİMLİK REFERANSLARI       Character/Vehicle Bible cümleleri BİREBİR (renk · işaret · ekipman ≤3)
MEKÂN                     World Bible çapa cümleleri; gök kadrajdaysa ② cümlesi
KORUNACAK HİKÂYE BİLGİSİ  spoiler bütçesi (PAKETLEME §5): finalde cevaplanan şey kapakta gösterilmez
TUVAL                     16:9 · teslim ölçüsü DIS_SAYILAR §1 (kaynak 3840×2160; küçültme serbest, büyütme ayrıntı üretmez)
```

---

# 3. 🎯 KAPAK ANI — üç aday, iki üretim (kaynak §06)

Adaylar PLAN'dan gelir, klipten değil: **vuruş tablosu** (açılış imajı · orta nokta · her
şeyin kaybı · doruk · kapanış imajı) + **İPTAL KAPISI** sahneleri + HOOK/DORUK/FINAL kilit
sahneleri. Her aday için tablo:

| aday | sahne · saniye | anlaşılan olay | açık kalan soru | küçük boyut riski | spoiler |
|---|---|---|---|---|---|
| A | S⬜ | | | | |
| B | S⬜ | | | | |
| C | S⬜ (yedek) | | | | |

Seçim ölçüsü, sırayla: **① küçük boyutta okunan TEK ilişki** (iki leke ve aralarındaki
boşluk — THE_FALLING_WORLD emsali) · ② filmle birebir bağ (aynı Bible cümleleri, aynı ışık)
· ③ açık kalan soru (başlık kapağı tekrar etmez, tamamlar) · ④ spoiler bütçesi. "Temasın
öncesi / anı / sonrası" her filmde ayrı karardır; kural yok, kayıt var.

---

# 4. 🅰️🅱️ İKİ ADAY KURALI — tek değişken

**U:** İki aday aynı fikrin dekor varyasyonu değildir; **bir deney sorusunu** sınar. Sabitler
(§2 + palet + ışık dili + oran) aynı kalır, TEK şey değişir. Değişken menüsü:

| değişken | A | B | sorduğu soru |
|---|---|---|---|
| **vaat tipi** | tehlike (kapanan gök · kopan geçit · yaklaşan figür) | çözüm/görev merakı (daralan koridordan geçen araç · uzanan kol) | izleyici tehlikeye mi, çıkışa mı tıklıyor |
| **zaman** | temasın öncesi (gerilim) | temasın sonucu (bedel) | merak mı, sonuç mu |
| **odak** | insan öne (silüet, ölçek şahidi) | engel/araç öne (yapı, gemi, koridor) | kimlik mi, dünya mı |
| **ölçek** | yakın (MS/MCU — eller, nesne) | geniş (WS — ölçek farkı) | ayrıntı mı, ihtişam mı |

Kurallar:
- Deney sorusu KAPAK dosyasına yazılır (`TEK DENEY SORUSU:`); soru yoksa ikinci aday yoktur.
- A ve B **aynı başlıkla** test edilir (başlık sabit) — ya da başlık×kapak birleşimi sınanıyorsa
  sonuç BİRLEŞİMİN sonucudur, tek başına kapağa mal edilmez (kaynak §18).
- İkisi de §6 biçiminde, ikisi de Bible cümleleriyle, ikisi de 120 px/160×90 sınavından geçer.
- Eski "Plan B kapağı" bu B adayıdır: Kart Y "yayından önce hazır" şartı aynen sürer.

---

# 5. 🧱 GÖRSEL KARARLAR — depo adresleriyle (kaynak §07–§12)

| karar | kural | adres |
|---|---|---|
| hiyerarşi | birincil öğe · onu açıklayan ikinci bilgi · mekân bağlamı; öncelik boyut · yerleşim · açık-koyu · netlik · boşlukla — nesne sayısı sınırı yok, eşit dikkat isteyen nesne yok | kaynak §07 |
| kompozisyon | özne · eylem yönü · hedef; yön tarafında boşluk; silüetler birleşmez; temas noktası kenarda kesilmez; koordinat yüzdeyle (sol üst 0,0) | kaynak §08 · PAKETLEME §2 RET ŞARTI |
| kadraj/ölçek | kamera kararının gerekçesi "izleyici hangi ilişkiyi görecek"; ölçek okunan öğeler arası ilişkiyle (1H = kasklı gövde) | kaynak §09 · UZAY_USSU §5 · KAMERA_ACISI |
| beden dili (yüzsüz) | duygu = kask yönü + omuz + kol + el + gövde; anlam yüz ayrıntısına bağlanmaz; yüz gizliyse yansıma ve iç ışık da gizli | kaynak §10 · PAKETLEME §2 üç odak · KARAKTER_VE_DUYGU §6 |
| ışık/renk | **D:** yazı-zemin açık-koyu ayrımı; anlam yalnız renge yüklenmez (gri ton kontrolü) · ana figürün sınırı zeminde kaybolmaz · kapak ışığı = sahnenin Lighting Bible ışığı, yeni ışık icat edilmez | kaynak §11 · ISIK_SENARYOSU |
| tipografi | film adı ayrı katman; uzun adda satır bölümü; küçükte kapanan harf iç boşlukları düzeltilir; evrensel kelime/yüzde/punto yok; ad kısaltılmaz | kaynak §12 |

---

# 6. 📝 KAPAK PROMPT BİÇİMİ — İngilizce, metinsiz, Bible cümleleriyle

Kaynak §17'nin üretim şablonu deponun V3 diline indirildi. Her aday bu biçimde, kod bloğunda:

```
COVER <A|B> — <FILM_ADI> · S<nn> · <deney değişkeninin bu adaydaki değeri>
IN FRAME: <face · hands · torso · legs · full body · back | none>
Exactly <N> human character(s) [and exactly <M> tall figure(s)] in frame.
<THE ONE RELATIONSHIP the cover must read at thumbnail size, with a number where one exists>

<BODY — subject as IN FRAME allows, Bible strings verbatim; the object/obstacle/goal; scale in object-relative units;
 the damage/wear state of this scene number; sky/world anchor if the sky is in frame; no motion, one balanced pose>
COMPOSITION: <primary element x,y as % from top-left · secondary element · direction of action/gaze and the space left for it ·
 empty region reserved for the title overlay · nothing story-critical in the bottom-right duration-badge corner or the bottom band>
CAMERA: <shot size, lens mm, angle word, height, distance in metres — the scene's own letter sentence when the moment is a scene>
LIGHTING: <sources and shadow quality from the Lighting Bible; the tonal separation that keeps the main figure's edge off the background>
NEGATIVE: <7 core sentences, film scope> No text, letters, numbers, logos, HUD or watermark anywhere. <≤2 cover-specific sentences>

Output: 16:9, 3840×2160, no text, no watermark.
```

Kurallar (prompt kapılarıyla aynı): kimlik cümleleri Bible'dan birebir · IN FRAME dışı tarif yok ·
opak vizörde yüz/göz/yansıma yok · yasak sözlük (glowing · ethereal · radiant · shimmering · swirl ·
cinematic lighting · şiddet sözlüğü · isim · pusula) · nesne-göreli ölçek · "nose pointing …" · tek
dengeli poz, hareket yok · kilit + gövde 100–250 kelime (COMPOSITION · CAMERA · LIGHTING satırları bandın dışında; kapak prompt_kontrol'e girmez, FILM_DISI deseni KAPAK'ı atlar) · NEGATIVE ≤10 cümle. `📸 GÖRSEL PROMPT` başlığı
KULLANILMAZ (kapak sahne değildir; dizi kapılarına girmez).

---

# 7. 🔍 KONTROLLER — üretimden sonra, elle (kaynak §13)

| kontrol | soru | sonuç |
|---|---|---|
| kaynak çözünürlük | kenar · el · temas · ekipman düzgün mü; figür sayısı ve kimlik doğru mu | |
| **320×180** | ana olay + (post'ta eklenecek) ad birlikte okunuyor mu | |
| **160×90** (≈120 px sınavı) | TEK ilişki ayırt ediliyor mu — iki leke ve boşluk | |
| gri ton | açık-koyu hiyerarşisi duruyor mu | |
| açık / koyu arayüz | görselin sınırı kayboluyor mu | |
| gerçek telefon · masaüstü | başlıkla birlikte hangi vaat oluşuyor | |
| süre etiketi / rozet örtüşmesi | sağ alt köşe ve alt bant hikâye kritik bir şey taşıyor mu | |
| liste görünümü | çevredeki içeriklerden ayrışıyor mu | |

Küçükte kaybolan bilgi ana fikrin tek taşıyıcısıysa **yeniden üretilir**; hiçbir şey kapağı
kurtarmaz. 160×90 ve 320×180 bu kılavuzun kontrol boyutlarıdır, YouTube'un sabit ölçüsü değil.

---

# 8. 👥 İZLEYİCİ ÖN TESTİ — isteğe bağlı (kaynak §14)

Beş kişi, 3 s tek başına → gizle → "ne gördün, ne oldu, ne bekliyorsun" → sonra başlıkla birlikte.
Kayıt: aday · sunum sırası · ilk hatırlanan öğe · anlaşılan olay · beklenen video · başlık sonrası
değişen yorum. Beğeni ve "tıklardım" sayılmaz; anlam ve okunurluk sayılır. Yayın testinin yerine geçmez.

---

# 9. 📦 TESLİM VE DOSYALAMA (kaynak §15 · §22)

- Ölçüler DIS_SAYILAR §1: yatay 3840×2160 (alt sınır 640 px genişlik) · Shorts 2160×3840 (masaüstü
  Studio) · JPG/PNG · masaüstü 50 MB · mobil 2 MB · özel kapak = doğrulanmış hesap · çok dilli kapak
  uzun videoda (Y). Depo kaynak 3840×2160 üretir, küçültür; büyütmez.
- Shorts/dikey kapak yatayın ortasından KIRPILMAZ (FRAGMAN §1.1 ilkesiyle aynı): ayrı kompozisyon,
  KAPAK dosyasında ayrı satır.
- Dosya adı: `<FILM>_<YUZEY>_<DIL>_<A|B>_v<n>.<png|jpg>` — teste giren dosya üzerine yazılmaz;
  ham üretim · katmanlı çalışma · teslim üç ayrı sürüm.

---

# 10. 🧪 YAYIN TESTİ — Studio A/B (kaynak §18 · §20)

**Y:** uygun videoda ≤3 varyant · izlenme süresi payıyla seçer · masaüstü + gelişmiş özellik ·
Shorts'ta yok · birkaç gün–iki hafta · test sırasında elle değişiklik testi durdurur (answer/16391400).
Sonuç: açık kazanan · benzer · belirsiz — belirsiz kazanan sayılmaz.

Depo uygulaması: A + B aynı başlıkla girer → Kart Y TEK DEĞİŞKEN KİLİDİ → 08_YAYIN_PERFORMANS_TABLOSU
§1'e `Kapak var.` A/B + deney sorusu; §4'e platform sonucu + yorum sınırı. Özellik erişimi yoksa
elle değişim tarihli GÖZLEM olarak yazılır, deney diye değil. Ölçüm ve teşhis:
`YOUTUBE_VIRAL_SANS_KILAVUZU` §7 (kanal-içi karşılaştırma, evrensel eşik yok).

---

# 11. 📚 ÖĞRENME KAYDI (kaynak §22)

Test bitince KAPAK dosyasının sonuna: seçilen aday · gerekçe · desteklenen bulgu · belirsiz
kalan · geçerli olduğu koşullar · **sonraki kapakta denenecek değişken**. Tek kapaktan tür kuralı
çıkarılmaz; üç filmde tekrarlayan bulgu ders adayıdır (Kart G).

---

# 12. ✅ KONTROL LİSTESİ — yayından önce (kaynak §19)

```
 □ Kapak anı filmde karşılık buluyor (sahne · saniye); olay ve sonuç filmle çelişmiyor
 □ Başlıkla aynı vaat; kapak başlığı tekrar etmiyor, tamamlıyor; spoiler bütçesi aşılmadı
 □ A ve B tek değişkenle ayrışıyor; TEK DENEY SORUSU yazılı
 □ Figür sayısı · kimlik cümleleri · vizör kuralı · hasar/yıpranma durumu sahne numarasıyla aynı
 □ Eller · uzuvlar · temaslar tutarlı; silüetler birleşmiyor; temas noktası kenarda kesilmemiş
 □ 160×90'da TEK ilişki, 320×180'de olay + ad okunuyor; gri tonda hiyerarşi duruyor
 □ Film adı tam ve doğru (post katmanı); yazı zeminden ayrılıyor; anlam yalnız renge bağlı değil
 □ Süre etiketi / rozet alanı boş; açık ve koyu arayüzde sınır kaybolmuyor
 □ Teslim ölçüsü/format DIS_SAYILAR §1; dosya adı ve sürüm belli; teste giren dosya korunuyor
 □ 08 tablosu §1 satırı yayından ÖNCE açıldı (Kart Y)
```

---

# 13. 📚 KAYNAKLAR

Tam kaynak kaydı ve doldurulabilir 24 şablon: `URETIM_ONCESI_ANALIZ/26_YOUTUBE_FILM_KAPAGI_KILAVUZU_VE_SABLONLAR.md`
(kontrol 20.09.2026): answer/12340300 (kapak-başlık) · 72431 (özel kapak, ölçüler) · 16391400 (A/B) ·
7628154 (CTR) · 9314415 (tutma) · 16559651 (öneriler) · 13338784 (çok dilli) · W3C contrast-minimum ·
W3C use-of-color. Sayılar DIS_SAYILAR §1'de tarihli.
