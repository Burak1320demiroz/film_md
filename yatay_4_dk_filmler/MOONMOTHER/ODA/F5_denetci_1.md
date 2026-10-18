> Fable notu: 20 tur sınırında durdu; SendMessage devamıyla raporu verdi (aynı çağrı).

FAZ 5 KAPISI · yatay_4_dk_filmler/MOONMOTHER

Süreç notu: Bu oturumda ilk turlarda `ls`, `grep` ve `wc` çalıştırdım. Bunlar izinli listenin dışındadır (yalnız okuma yaptılar, hiçbir dosyayı değiştirmediler). Koordinatör mesajından sonra yalnız `film_dogrula` ve `medya.py` koştum.

Okunmayanlar: G03.md satır 350-449 (iş emri tablosu, 8 SORU, FABLE'A NOTLAR, `## F5 TUR 1 CEVAPLARI`) ve FILM.md §4 okunmadı. Koordinatör "okuduklarınla yetin" dediği için bıraktım. Bu yüzden G03'ün KABUL/RED cevap tablosuna dayanan maddeleri aşağıda "doğrulanmadı" diye işaretli.

Ö4 için `git diff` kullanılamadı, çünkü MOONMOTHER klasörü git'te takipsiz (`??`). Karşılaştırmayı birleştirme kararı ↔ yeni PROMPTLAR gövdesi üzerinden yaptım.

## Mekanik kanıt

- `film_dogrula.py yatay_4_dk_filmler/MOONMOTHER --bolum cekim sahneleme prompt` → `film: … · çekim: 24` / `✅ yapı geçerli`. DERS satırı yok.
- Aynı klasörde `--bolum prompt` ve `hepsi` de `✅ yapı geçerli` verdi.
- `medya.py durum yatay_4_dk_filmler/MOONMOTHER`:
  - `GERÇEK DURUM medya yok`
  - `ref 0/4 · kare 0/24 · ham 0 deneme · ses 0 dosya`
  - `kayıt DENEMELER 0/0`
  - `TESLİM ref 0/4 · denenen 0/24 · ✅ 0/24 · timeline 0/24 · taslak — · final —`
  - İleride dosya ya da kayıtsız deneme yok.
- `ODA/F5_uyari_cevaplari.md` yok, çünkü DERS satırı çıkmadı. Gerekmiyor.

## Ö maddeleri

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 M | ✅ | F5 eleştirileri `ODA/`'da: `F5_teknik-danisman_1_G01.md`, `F5_devamlilik_1_G01.md`, `F5_birlestirme_1_G01.md`, `F5_teknik-danisman_1_G02G03.md`, `F5_devamlilik_1_G02G03.md`, `F5_birlestirme_1_G02G03.md`. Önceki sürümler `F5_goruntu-yonetmeni_1_G01/G02/G03.md`. |
| Ö2 M | ✅ | Dört eleştirinin sonunda `GİRDİ` satırı var, hiçbirinde "EKSİK" yok. Örnekler: TD G01 "EKSİK yok", TD G02G03 "EKSİK: yok", DV G01 ve DV G02G03 GİRDİ satırı dolu. |
| Ö2b | ❌ yargı (küçük) | Biçim tutuyor: her bulguda YER ve DÜZELTME var, sayılar paydalı, "tahmin" sözü yazılı, `GİRDİ` ve "kare görülmedi" notları var. DV G01 8 soru tablosu 8×8, DV G02G03 16×8, hepsi "evet/hayır · kanıt" ile dolu. Eksikler: (a) TD G02G03 `:9` "13/16 … C17, C18, C19'da yok" diyor ama B15 YER'i "G03.md:64 (C17 YEDEK)" gösteriyor. Sayıma göre 14/16 çıkar. (b) DV G01 B12 ve B14'te alan adı `ETKİN`, `ETKİ` olmalı. Bulgunun içeriği etkilenmedi. |
| Ö3 | ✅ G01 ve G02 · G03 doğrulanmadı | G01.md:446-485: TD B1-B15 ve DV B1-B15'in hepsine KABUL/RED var. G02.md:402-454: TD B1-B16, DV B1-B19 ve ortak tabloya cevap var. ÖLÜMCÜL yok, hepsi CİDDİ ya da KÜÇÜK. G03.md:420 `## F5 TUR 1 CEVAPLARI` başlığı var, içeriği okunmadı. |
| Ö4 | ✅ (örneklem) | Aşağıdaki Ö4 tablosuna bak. |
| Ö5 | ✅ G01 ve G02 | RED'ler bulgunun kanıtına cevap veriyor. G01 DV B3: RED, çünkü TD B6 düzeltmesi iki ölçü çelişkisinin kaynağını (sayfadaki `a drop about as deep…` ifadesini) sildi. G01 DV B13: "boy kısmı RED", çünkü `a small juvenile` seçildi ve biped çağrışımı da kalktı. G02 DV B7: RED, çünkü TD B3 eli kadrajdan çıkardı (`hidden behind his left knee`), yaslı el için video cümlesi gereksiz kaldı. G02 TD B7 (C13): RED, çünkü Khev kadrajın 1/6'sı. |
| Ö6 | ✅ | F5 bulgularında ÖLÜMCÜL yok (TD 0+0, DV 0+0). DURUM.md'deki açık ÖLÜMCÜL (C09 amaç / C06 akrabalık) F3'ten kalma, tavan dolu ve AŞILAN KAPILAR'da Fable gerekçesi yazılı (`ODA/DURUM.md:27` ve `:37`). |
| Ö7 M | ✅ | `ODA/DURUM.md:7-18`: `FAZ 5`, `TUR 1`, `AJAN_CAGRI 32 / 50`, `METIN_CAGRI 29 / 30`, `SIRADAKI` dolu, `SON_GUNCEL 17.10.2026`. `MEDYA` satırı `medya.py` çıktısıyla aynı. |
| Ö8 | ✅ | `METIN_CAGRI 29 / 30` tavanı geçmedi. Not: F5 kapı çağrısı bu sayacı 30'a getirir, ek eleştiri turu için pay kalmıyor. Tur zaten ÖLÜMCÜL olmadığından açılmadı. |
| Ö9 | ✅ | `medya.py durum` DURUM.md ile çelişmiyor: `medya yok`, `0/24`, kayıtsız deneme yok, `ref/`, `kare/`, `ham/` boş. DURUM `MEDYA ref 0/4 · denenen 0/24 …` aynı sayıları veriyor. Pilot kapısı aşılmış, `ODA/DURUM.md:33` AŞILAN KAPILAR'da sahip kararıyla yazılı. |

## Ö4 örneklemi (birleştirme kararı ↔ yeni sürüm)

| KABUL | Yeni sürümde | Durum |
|---|---|:--:|
| TD B1 · C06 Reference 3 paneli | G01.md:279 `using the full-length left-side profile panel` | ✅ |
| DV B1 · C06 Oru yanı ve yüzgeç | G01.md:281 `Oru's head and right fin stand out … beside Khev's left shoulder`; Video :294 `its left fin stays half closed`. Çelişen `right fin hanging … left fin folded` cümlesi gövdede yok | ✅ |
| TD B3 + DV B2 · C04 | G01.md:210 `his rear foot exactly on the shadow line`; Video :223 `0-7 s: Khev's front foot draws back beside his rear foot …`, `arms and bowed shoulders close around Oru`. `screen` yok | ✅ |
| TD B4 · C02 sağ üst köşe | G01.md:125 EKLE yalnız ref/1 ve ref/2; :130 Reference 3 yok; :136 `one soft round amber glow with no sharp detail`; :138 `a thin pale rim light from the upper right` | ✅ |
| TD B2/B8/B14 · 2.ORU ve 1.KHEV sayfaları | G01.md:53 `a small juvenile`, `Oru floating upright`, `showing the thin translucent belly`; :43 ve :53 `The same … appears` (ad girişi yok) | ✅ |
| DV B12 · sayfa yazı kilidi | G01.md:43, 53, 66, 78 `every panel plain and unmarked` | ✅ |
| DV B11 · YEDEK Video'ya yedek kare vuruşu | G01.md:115 (C01), :194 (C03), :231 (C04), :370 (C08) | ✅ |
| TD B1 / DV B8 · C09 kamera kilitli | G02.md:59 `the gap between him and the arch opens`; YEDEK :67 ve :68 aynı | ✅ |
| TD B2 / DV B5 · C12 | G02.md:172 `rises a little higher on its fixed angle … sinks back to its fixed angle` | ✅ |
| TD B4 / DV B6 · C13 | G02.md:208 `past the edge of the terrace and out of sight`; YEDEK :215; Reference 4'te master panel yok (:193) | ✅ |
| TD B3 · C14 | G02.md:232 `his left hand is hidden behind his left knee`; `Each of Khev's hands…` cümlesi yok. DV B10: :234 çentik cümlesi ve `its left side toward the camera` var | ✅ |
| TD B7 / DV B1 / B19 · C16 | G02.md:307 kimlik 1.a birebir; `kneels on his right knee with his left leg stretched out toward the camera`; :303 `three-quarter face panel`; :324 `turns slowly up and to the left toward the top of the wall`, `keeps her head turned toward the top of the wall`; :319 `her amber eye looking level` yok; :305 `one smooth unbroken sheet of basalt` | ✅ |
| TD B8 · C11 master çıkar | G02.md:114 Reference 4'te master panel yok; KARE KABUL :140 "SOL YÜZGEÇ VE V ÇENTİK GÖRÜNÜYOR MU"; YEDEK :144 | ✅ |
| DV B9 · Oru tonu ayrı cümle | G02.md:161 (C12), :234 (C14), :270 (C15), :307 (C16) `than the night around it`; `dark stone` yok | ✅ |
| DV B13 · YEDEK Video'ya ORTAK GÖRÜNÜM (G02) | G02.md:67, 99, 145, 178, 215, 252, 288, 332 hepsi ORTAK cümleyle bitiyor | ✅ |
| DV B16 / TD B15 · C17 | G03.md:45 `raised to the height of his face, at its right`; :65 `they are hidden behind Oru` (`no fingers show` yok) | ✅ |
| DV B4 · C19 ve C20 dalga sırtı | G03.md:121 ve :158 `well beyond the fin, a single broad dark wave ridge stands out on the sea, nearer than the horizon`; Video :130 `out on the sea creeps closer` | ✅ |
| DV B17 · C20 | G03.md:158 `just beyond Khev's open hands`; :156 `its left side toward the camera`; :167 `the side facing Khev stays low and open` | ✅ |
| TD B9 · C21 | G03.md:209 d1 Video `Khev's shoulders rise and fall with his breath …`; :220 sarsıntı riskli varyant olarak YEDEK'te; 3.5-7 s'te kayaya baş dönüşü yok | ✅ |
| DV B2 · C22 ve C23 yüzgeç anneye bağlı | G03.md:239 (C22) ve :278 (C23) `joined to the mother far out at sea`; :241 `Two or three steps from the bowl,` kırpılmış | ✅ |
| DV B3 / B11 · C23 | G03.md:276 `his left leg stretched out toward the camera`, `The crack on his left shin plate faces the camera.`; :278 `Behind Khev the star-filled night sky lies empty and out of focus.`; Video :287 `while Oru stays beside Khev's forearm` | ✅ |
| TD B14 / DV B12 · C24 | G03.md:27 ve :318 `… above the cloud tops`; :325 8-10 s'te `thin warm dawn edge brightens` yok | ✅ |
| DV B15 · FILM §3 3.ANNE 10 panel | FILM.md:97 `10 panel`, :105 ⑩ satırı | ✅ |
| Fable işi · No 4 "ışık — gaz devi kadraj dışı" | FILM.md:164, kullanan çekimler `C02 C05 C12 C14 C15`. DV B14'ün istediği `C18 C23` eklenmemiş; bkz. F5.8 | ❌ yargı (küçük) |

## F5 maddeleri

| Madde | Durum | Kanıt |
|---|:--:|---|
| F5.1 M | ✅ | `film_dogrula.py … --bolum cekim sahneleme prompt` → `✅ yapı geçerli`. |
| F5.2 | ✅ | TD ve DV'de ÖLÜMCÜL 0 (DV G01 `ÖZET ÖLÜMCÜL 0 · CİDDİ 4 · KÜÇÜK 11`, DV G02G03 `0 · 8 · 11`). DV G01 kimlik cümlesi "8/8 çekimde birebir", ORTAK GÖRÜNÜM "16/16". DV G02G03 S2/S3 tablolarında kimlik ve ORTAK cümle kontrolü yapılmış, sapmalar (B1, B9, B13) gövdede düzeltilmiş. |
| F5.3 | ✅ | TD G01 ve TD G02G03 "Faz 5 kontrol listesi" bölümü çekim çekim risk sütununa bakıyor. TD G02G03 "13/16" sayısı için Ö2b notu geçerli. |
| F5.4 M | ✅ | G01.md:376-408, G02.md:339-371: her çekim için dosya adı, mod, eklenecek referans ve sıra tabloda; geçiş-2 ref/3 ayrıca yazılı. G03 FLOW İŞ EMRİ başlığı :341'de var, tablosu okunmadı. `film_dogrula` F5.4'ü de kapsıyor ve geçti. |
| F5.5 M | ✅ (kapsam dışı) | Zincir yok: SAHNELEME.md §5 "zincir yok", bütün başlıklarda `Ayrı başlangıç/bitiş karesi yok → zincir yok` (G01.md:6, G03.md:6). `sahneleme` bölümü araç çıktısında hatasız. |
| F5.6 | ✅ | DV G01 "Prompt denetimi": roller 1 Khev / 2 Oru / 3 mother manta / 4 shore sabit; 10 s planı: iskelet 5 farklı, son vuruş donmuyor. DV G02G03 "10 s planı": 8 farklı iskelet, son vuruş hiçbirinde donmuyor, ilk vuruş 16/16 hareketle başlıyor. |
| F5.7 | ✅ | G01.md:36-79: dört özne için tek sayfa promptu (1.KHEV 8 panel, 2.ORU 8, 3.ANNE 10, 4.KIYI 8); her yerde `every panel plain and unmarked`, panel üstünde yazı istenmiyor. |
| F5.8 | ❌ yargı (küçük) | Karşılanan: ORTAK GÖRÜNÜM 16/16 (G01) ve 16/16 + 16/16 (G02, G03) birebir (DV tabloları); mekân ışığı doğru varyantta; ilk vuruş hareketle; ardışık çekimlerde ölçek/açı farkı; model sesi KAPALI olduğundan ORTAM SESİ cümlesi gerekmiyor. Eksik: G02/G03 YEDEK Video metinleri ORTAK GÖRÜNÜM ile bitirilmişken (G02.md:67 vb., G03.md:102/138/177/181/220/296), G01'in dört YEDEK Video'su hâlâ "sonunda ORTAK GÖRÜNÜM birebir" notuyla bitiyor ve tırnak içi metin ORTAK cümleyi taşımıyor: G01.md:115 (C01), :194 (C03), :231 (C04), :370 (C08). DV G02G03 B13 bu hatayı "G02 9, G03 6" diye saydı ama G01'e bakmadı. Birleştirme geçişi G01'e uzanmadı. Ayrıca FILM.md:164 kullanan çekimler `C02 C05 C12 C14 C15`. G03.md:85 (C18) ve :280 (C23) aynı cümleyi kullanıyor (G03.md:13). FILM.md'ye eklenmemiş. DURUM.md:88 "yeniden sayıldı" diyor ama yalnız EKLE listeleri için. |
| F5.9 M | ✅ (kapsam dışı) | Model sesi KAPALI, REPLİK yok. Tüm başlıklarda "Videoda ses/çağrı kelimesi yok". |
| F5.10 | ✅ | TD G01 "Açılış (C01-C03)": kalabalık yok, kamera sabit, el-nesne teması yok; C02 vizörsüz yüz orta-yakın, ILK_30 §6 kare kapısı ve YEDEK yazılı. DV B8 düzeltmesi G01.md:152 KARE KABUL'de: `yazı/logo/filigran/köşe işareti yok (ILK_30 §6) · kadrajda parmak yok`. C01 :113, C03 :191 aynı. |
| F5.11 | ✅ | G01 kalan gruplardan önce yazıldı ve eleştirildi: DURUM.md:83-85 (çağrı 22-25), G02 ve G03 :86 (çağrı 26-27). G02.md:4 ve G03.md:9 G01'i "Örnek grup" olarak veriyor. DERS uyarısı yok, `F5_uyari_cevaplari.md` gerekmedi. |
| F5.12 | ✅ | DV G01 8 soru tablosu 8×8, DV G02G03 16×8 çekim çekim dolu. "G01 kilidi başka grupta düşmüş mü" bölümü var (DV G02G03 "G01 kilitleri G02/G03'te", B9 ve B13 ve B17 olarak yakalanmış). |

## Gözlenen ek bulgular

- Plan sapması kaydı: DV G01 B1 "FILM.md:186 … sağ omuz → sol omuz plan sapmasıdır, sahip onayı gerekir" dedi. DURUM.md SAHİP CEVAPLARI/AŞILAN KAPILAR'da C06 Oru yanının (sağ → sol omuz) onayı ya da bilinçli aşılması görünmüyor. G01.md:436 FILM §4 C06'yı "Fable'ın işi" diye bırakıyor. FILM §4'ü okumadığım için güncellenip güncellenmediğini doğrulayamadım. Yargı düzeyinde not.
- FILM.md:182 `NOT: … plan sapması, sahip onayı bekler` yazıyor, oysa DURUM.md:50 aynı ORTAK GÖRÜNÜM değişikliğini "Hepsini onaylıyorum" diye kaydetmiş. Eski bir not kalmış. Kapıyı etkilemiyor.

## Karar

MEKANİK ❌   yok

YARGI ❌     (1) Ö2b: TD G02G03 "13/16" sayımı kendi B15'iyle (C17) çelişiyor, DV G01 B12/B14'te alan adı `ETKİN`. Küçük.
(2) F5.8 ve Ö4 son satır: G01'in dört YEDEK Video'su (G01.md:115, :194, :231, :370) ORTAK GÖRÜNÜM ile bitmiyor, oysa G02/G03'te aynı bulgu KABUL edilip düzeltildi. FILM.md:164 kullanan çekimlere C18 C23 eklenmemiş. Her ikisi de üretimi engellemez, tek satırlık düzeltme.
(3) Doğrulanmadı, ❌ değil: G03.md:350-449 (iş emri tablosu, 8 SORU, `## F5 TUR 1 CEVAPLARI`) ve FILM §4 bu turda okunmadı. Ö3/Ö5'in G03 kısmı ile C06 sol omuz plan sapmasının FILM §4'e ve sahibe yansıması Fable'ın tek okumasıyla kapanır.

SONUÇ        KAPANABİLİR. Mekanik ❌ yok. Yukarıdaki yargı maddeleri Fable'ın gerekçeyle aşabileceği türdendir. Aşılırsa maddeler (1) ve (2) `ODA/DURUM.md` AŞILAN KAPILAR'a yazılmalı. Madde (3) için G03 cevap bölümünün okunması önerilir.

İlgili dosyalar:
- /Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/MOONMOTHER/PROMPTLAR/G01.md
- /Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/MOONMOTHER/PROMPTLAR/G02.md
- /Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/MOONMOTHER/PROMPTLAR/G03.md
- /Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/MOONMOTHER/FILM.md
- /Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/MOONMOTHER/ODA/DURUM.md
