# F5 · Prompt yazım kararı (Fable, 20.10.2026)

> **Kaynak (yalnız bunlar):**
> - `DEAD_LAST_8DK_48_KLIP_FILM_PLANI.md` (sahip planı, birebir);
> - `FILM.md` §3 (referanslar, ORTAK GÖRÜNÜM, ORTAK HAREKET, SAHNE DÜZENİ, DÜNYA KURALLARI, DEVAMLILIK);
> - §4 çekim satırı (Referans sütunu = EKLE);
> - §5 replik Kaynak + saniye.
>
> **Varsayılan:** plandan dışarı çıkılmaz. Yeni olay, kişi, nesne, ışık kaynağı, ekran, yazı, renk ya da sıfat yok. Eklenen her cümle planın kendi malzemesidir.
>
> **Uzunluk** (sahibin BLACK_ACCORD tercihi 18.10.2026: "sanki promtlar kısa" → "plan aynen + sonuna ek"):
> - Görsel hedef 2.000-3.200 karakter;
> - Video hedef 1.000-1.500 karakter;
> - tavan 4.300.

## İki çekim türü

**A — C01-C06:** planın kendi İngilizce Başlangıç görseli ve Video istemi var. Bunlar **AYNEN** girer: kelimesi kelimesine, aynı sıra, aynı sıfat ve sayı. Yalnız aşağıdaki biçim düzeltmeleri uygulanır.

**B — C07-C48:** plan istem yazmadı. Plan şunu açıkça söylüyor: "C07–C48'in tam olay, konuşma ve devamlılık talimatları yukarıdaki 48 kliplik tabloda bulunur." Yazar, plan tablosunun o satırından İngilizce Görsel ve Video yazar:
- **Görüntü / tek ana olay** sütununun her cümlesi İngilizceye çevrilir. Anlam aynen kalır, yeni ayrıntı eklenmez. Her cümle karşılığı promptta olmalı.
- **Devamlılık** sütununun görsel cümleleri girer: hasar, sayı, yön, kim görünür, ne yok. Kurgu notları girmez; bunlar (yazı kurguda, ses, "Axi'ye konuşur") EKLE altındaki `not` satırına Türkçe yazılır.
- **Kadraj ve kamera:** planın sözcüğü varsa o kullanılır ("yakın portre", "geniş plan", "dıştan simetrik geniş plan", "kameraya yakın kokpit portresi", "arkalarından bakılır"). Plan yazmıyorsa yazar en sade kadrajı seçer ve `not` satırına `kadraj: yazar seçimi — <ne>` yazar. Bunlar sahibe liste olarak gider.
- **Planın genel kuralları** çekim türüne göre uygulanır (plan "Ses, kamera ve ritim" + "Yarışın kurgu kuralları"):
  - Dış geniş planda bir veya iki araç ayrıntılı, kalanlar küçük silüet.
  - Yarış yönü geniş dış planlarda soldan sağa.
  - İç planlarda, duvar gibi duran sabit arka görüntü yerine kontrollü hız ışıkları ve bir yönü koruyan çevre akışı.
  - Yakın planda en fazla bir veya iki ayrıntılı yüz.
  - Her 10 saniyelik birimde bir ana olay.
- **Planda tasarımı olmayan şey:** yalnız planın kelimesiyle anılır, yeni tasarım yazılmaz. Örnekler: takip dronları "pursuit drones", yükleyici "an alien loader's plain gloved hands", servis kolu, gösterge. `not` satırına `planda tasarım yok` yazılır.

## Görsel (her çekim)

1. **Referans anahtarları** (M): §4 Referans sütunundaki her referans için bir cümle, `Reference <No> (<rol>): …` biçiminde. Rol sözlüğü:

   | No | Rol |
   |:--:|---|
   | 1 | Raka |
   | 2 | Thren |
   | 3 | Axi |
   | 4 | Sael |
   | 5 | Korv |
   | 6 | Veli |
   | 7 | Kalix |
   | 8 | Needle intact |
   | 9 | Fang intact |
   | 10 | Halo |
   | 11 | Bastion intact |
   | 12 | Sickle |
   | 13 | maintenance tug |
   | 14 | Axi's lost world |
   | 15 | preparation dock |
   | 16 | hanging-root sector |
   | 17 | suspended-ocean sector |
   | 18 | iron-leaf sector and harvest gate |
   | 19 | spectator stands |
   | 20 | Needle with broken left fin |
   | 21 | Fang with dead right engine |
   | 22 | Bastion with dead right engine |

2. **ORTAK GÖRÜNÜM** (FILM §3 = plan "Görsel üretim dili", birebir). Plan "Görsel istemlerinin başına" dediği için anahtarlardan hemen sonra gelir.
3. **Plan metni:** A türünde planın Başlangıç görseli AYNEN; B türünde plan satırının İngilizcesi.
4. **Ek paragraf, plan metninin ardına.** Yalnız plan malzemesi girer:
   - kadrajda görünen her öznenin, plan referans istemindeki kimlik parçaları **birebir** (FILM §3 KİMLİK CÜMLELERİ). Kadrajda görünmeyen parça yazılmaz.
   - araçta o çekimin **hasar durumu**, plan "Hasar ve nesne devamlılığı" tablosundan;
   - mekânın plan M istemi cümleleri, yalnız kadrajda görünen yapılar için;
   - planın sektör/ses dışı kuralları (yukarıdaki liste).
   Planın söylediğini tekrar etmez, onunla çelişmez.

## Video (her çekim)

1. **ORTAK HAREKET** (FILM §3, birebir). Plan "video istemlerinin başına" dediği için ilk gelir.
   ⚠️ §5'te **ağız kadrajda** repliği olmayan çekimlerde şu üç cümle **atılır**, çünkü M kuralı konuşma kelimesine hata verir ve o çekimde modelin söyleyeceği satır yoktur:
   - "One detailed speaking face at a time; other replies may be off-screen communications."
   - "Dialogue is the assigned performance text, not a claim that the selected video model produces audio."
   - "Sound and clean dialogue may be added in editing."
2. **Vuruşlar** (M): 10 s, 2-4 vuruşa bölünür: `0-3 s: … 3-7 s: … 7-10 s: …`. Vuruşlar 0'da başlar, 10'da biter, aralarında boşluk yoktur ve her biri en az 2 s'dir.
   - A türünde planın Video cümleleri aynen ve aynı sırada kalır; yalnız saniye öneki eklenir.
   - B türünde tek ana olay planın sırasıyla yazılır; son vuruş görünür bir sonuçta biter.
   - Repliğin düştüğü vuruş FILM §5 saniyesine uyar.
3. **Diyalog bloğu:** yalnız §5'te **ağız kadrajda** satırı olan çekimlerde. Planın biçimiyle, o klibin bütün replikleri plan sırasıyla yazılır:
   ```
   Dialogue, in order:
   RAKA: "…"
   AXI: "…"
   ```
   - Replik tırnak içinde birebir olur; film_dogrula bunu FILM §5 metniyle karşılaştırır.
   - Ekran dışı cevap varsa planın C04/C06 kalıbıyla yazılır: "Hold on her listening reaction while <X> answers from the communication channel; only <Y>'s own line receives mouth movement."
4. **Yalnız telsiz/makine repliği olan çekim** (§5 Kaynak telsiz | makine): Video'da konuşma, ses ve diyalog kelimesi yoktur. Replik kurguda eklenir; `not` satırına yazılır.
5. **Ek** (isteğe bağlı, hedef uzunluk için): son vuruşta Devamlılık satırının görsel kısmı, yani o çekimde sabit kalanlar.

## Biçim düzeltmeleri (M — yalnız bunlar; NOTLAR KARARLAR'a yazılır)

| Çekim | Blok | Plan metni | Düzeltme | Neden |
|---|---|---|---|---|
| C01 | Görsel | "the one blue inhabited planet from M01" | "the one blue inhabited planet from Reference 14" | referans kodu prompta yazılmaz; anahtar `Reference <No>` |
| C01 | Görsel | "The event must be legible in the very first frame." | "The event must be legible in the frame." | zincir dili "first frame" |
| C06 | Görsel | "The canopy and headrest match C04." | silinir; yerine ek paragrafa C04'teki kabin cümlesi birebir girer ("Inside Needle's compact one-pilot canopy.") | META `C04`, başka çekime atıf |
| C02 · C03 | Video | `Dialogue, in order:` bloğu | Video'dan çıkar; replik kurguda | §5: makine / telsiz, ağız yok |

Ayrıca:
- C03 plan cümlesi "Axi's assigned sentence is heard off-screen." konuşma kelimesi taşımaz; **kalır**.
- Görsel'de kimlik cümlesinde konuşma kelimesi bulunan yerler:
  - Thren "one narrow horizontal speaking mouth" → kare promptunda "one narrow horizontal mouth";
  - Korv "one wide speaking seam" → "one wide mouth seam".
  Referans promptunda plan metni kalır.
- film_dogrula başka bir M hatası verirse: en küçük biçim değişikliği yapılır ve 8 SORU notu yazılır.

## Referans promptları (yalnız G01)

- Plan R01-R07 · V01-V06 · M01-M06 · V01D · V02D · V04D İngilizce istemleri **aynen**, hat adlarıyla (`ref/1.RAKA_v1.png` …; eşleme FILM §3 kod bloğu).
- Plan sırası: önce sağlam araçlar 8 · 9 · 11, sonra onların düzenlemesiyle 20 · 21 · 22. Hasar istemlerindeki "Edit the supplied intact V01 Needle reference" metni aynen kalır; plan kodları hat dosyasına `DOSYA` satırında eşlenir.
- ORTAK GÖRÜNÜM referans promptlarına **eklenmez**; plan R istemleri kendi arka planını taşır ("Neutral dark-gray background").

## Korunacaklar

- Plan "Hasar ve nesne devamlılığı" tablosu.
- Plan pilotu C01 · C16 · C41 ("Önce denenmesi gereken üç çekim").
- Plan C41 yedeği: aynı 10 s birimde sol kilit açılması, sağ kilit açılması ve genel görünüm ayrı kaynak çekimlerden. G06'da `## C41Y` bloğu olarak, dosya adları `kare/ara/C41_y1-3.png` · `ham/C41_d3-d5.mp4`.
- Prompt gövdesine şunlar yazılmaz:
  - çekim kodu (C04);
  - plan referans kodu (R01, M01, V01D);
  - "Clip n of N";
  - başlık satırı;
  - "first/previous/next shot", "the film".

## Teslim (grup dosyası, örnek biçim `yatay_4_dk_filmler/RAIN_THIEF/PROMPTLAR/G01.md`)

Grup dosyası şu sırayla kurulur:
1. Dosya başı not.
2. (Yalnız G01'de) REFERANS PROMPTLARI + KİMLİK CÜMLELERİ.
3. Çekim blokları: FLOW · EKLE · not · `### Görsel` · `### Video`.
4. FLOW İŞ EMRİ.
5. `## 8 SORU` tablosu, "Görsel kr · Video kr" sütunuyla.

> **Ek (20.10.2026, birleştirme 2 L1):** rol sözlüğünde 21 → "Fang with dark right engine", 22 → "Bastion with dark right engine" ("dead" üretim reddi kelimesi). Kayıt silinmedi; uygulanan biçim budur.
