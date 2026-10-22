# 📦 BLACK_ACCORD — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK

<!-- kaynak: plan "Kapak ve yayın paketi — İngilizce" (kapak fikri + kapak görsel promptu birebir). F6 kapak-tasarimcisi turu açılmadı (sahip planı, THE_FURNACE_GATE yolu). -->
```
DENEY SORUSU   — (plan tek kapak verir; B adayı F9'da kapak-tasarimcisi'nden, plan kompozisyonundan tek değişkenle)
DEĞİŞKEN       —
SABİTLER       karakter tarifi (FILM.md §3: 1.NEM · 2.VEKH · 3.ISHRA) · dünya ışığı (8.BLACK_HOLE_STATION) · figür sayısı 3
AN             plan: "Önde Nem'in yabancı yüzü; iki yanda daha geride Vekh ve su başlığındaki Ishra. Arkada tek kara delik ve ince bir masa silueti."
TEK İLİŞKİ     üç ayrı tür + tek kara delik (plan: "Kapak üç ayrı türü ve kara deliği küçük boyda da okutmalıdır.")
BOŞ ALAN       plan: "Leave a clean central-lower title band above the lower-right duration area." (sağ alt süre alanı boş)
KAPAK YAZISI   plan: "Film adı BLACK ACCORD ortada iki satırla, büyük ve okunur biçimde sonradan eklenir." ↔ hat KAPAK_VE_BASLIK "film adı yazılmaz"
               (TERCİH) → plan korundu (sahip talimatı "plandan asla dışarı çıkma"); F9'da sahibe hatırlatılır, karar sahibin
VAAT SINIRI    Nem → C04-C96 · Vekh → C01 C13 … · Ishra → C02 C14 … · kara delik → C01 C17 C40 C96 · masa silueti → 7.ACCORD_CHAMBER (hepsi filmde)
YÜKLEME SIRASI A ilk (plan kapağı)
FİNAL          faz 9: aynı referanslarla ayrı kompozisyon (plan yolu: "Use the approved NEM, VEKH and ISHRA references …")
               → ~/film_medya/BLACK_ACCORD/cikti/kapak_A.png · kareler.py kapak → izleyici/kapak/A/
```

### Kapak A (plan kapak görsel promptu, birebir; hat biçimi — Reference <No> anahtarı — F9'da)
```text
Use the approved NEM, VEKH and ISHRA references for three clearly different alien faces, and the BLACK_HOLE_STATION reference for the astrophysical background. Create a striking photoreal 16:9 political science-fiction film thumbnail. Nem dominates the central foreground, her pale lavender-ivory facial plates and dark-violet eyes sharp and alert. Vekh's rust-red armoured face appears slightly smaller behind her on the left, while Ishra's pearl-teal face inside the clear water dome appears on the right. A single immense black-hole shadow with a lensed golden disk fills the distant background above a thin dark council-table silhouette. Strong face separation, cold charcoal shadows, controlled gold highlights, tactile cinematic 35mm texture and readable forms at small size. Leave a clean central-lower title band above the lower-right duration area. Render artwork without lettering, logos or watermarks; BLACK ACCORD will be added as typography in post-production.
```
EKLE: ref/1.NEM_v1.png · ref/2.VEKH_v1.png · ref/3.ISHRA_v1.png · ref/8.BLACK_HOLE_STATION_v1.png (plan dört referans; KIMLIK §3 "en çok 3" varsayılanı → F9'da sahip/kapak-tasarimcisi)

### Kapak B
```text
— (F9: plan kompozisyonundan tek değişken)
```

### Yayın metni (plan, birebir — YAYIN_PAKETI.md F9'da bu metinden, hat biçimiyle)
```
Ana başlık:  Aliens Came for Peace. Their Translator Declared War. | BLACK ACCORD
Alternatif:  One Missing Word Kept Four Alien Fleets at War | BLACK ACCORD
Açıklama:
He said, “We did not fire first.” The official relay said, “We fired first.”

At a peace summit near a black hole, six alien species trust one voice to carry their words. A young interpreter hears a word disappear—and discovers that the war outside may be built on everything the delegates were never allowed to hear.

BLACK ACCORD is a sixteen-minute, dialogue-driven science-fiction thriller about language, power and the cost of letting someone else decide what you meant.

Created with AI-assisted imagery and video. Produced for Apex AI Cinema.

#SciFi #Alien #ShortFilm
Sabit yorum: Which line changed your mind about the person saying it?
```

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum, Shorts metni ve vaat denetimi orada,
yapıştırmaya hazır İngilizce bloklar hâlinde. Denetim: `film_dogrula.py <FILM> --bolum yayin`.
