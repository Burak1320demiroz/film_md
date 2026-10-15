# F5 denetci — kapı denetimi 1 (15.10.2026, sonnet; 20 tur sınırı → SendMessage devamı)

FAZ 5 KAPISI · THE_FURNACE_GATE

Tur sınırına geldiğim için denetim tamamlanmadı. Bulduğum hiçbir madde ❌ değil. Ama bir kısım maddeyi doğrulayamadım ve onları ✅ saymadım. Klasör git'te izlenmiyor (`??`), bu yüzden `git diff` yok. Ö4'ü ODA raporlarındaki beyanları güncel `PROMPTLAR/` dosyalarıyla grep'leyerek denetledim. Yazarın ya da Fable'ın beyanını tek başına kanıt saymadım.

**Mekanik çıktılar**

`film_dogrula.py yatay_16_dk_filmler/THE_FURNACE_GATE --bolum …`:
- `prompt`: "çekim: 96 · ✅ yapı geçerli"
- `kunye`, `hikaye`, `cekim`, `muzik`, `sahneleme`, `durum`: hepsi "✅ yapı geçerli"
- `replik`: "⚠️ 95 replik — bant 40-70" ve "✅ yapı geçerli". Gerekçe FILM.md §5 altında ("Bant dışı gerekçe: 95 replik > 70…").
- `kurgu.py` bu fazda gerekmiyor.

| Madde | Durum | Kanıt |
|---|---|---|
| Ö1 M | ✅ | `ODA/` içinde var: `F5_devamlilik_1_G01-G04.md`, `F5_devamlilik_1_G05-G08.md`, `F5_teknik-danisman_1_G01-G04.md`, `F5_teknik-danisman_1_G05-G08.md`, `F5_fable_birlestirme_1.md`, `F5_goruntu-yonetmeni_1_G01…G08.md` ve `_2_G01…G08.md`. |
| Ö2 M | ⚠️ doğrulanamadı | Dört eleştirinin dördünde de `GİRDİ` satırı var. Hepsinde "EKSİK" kelimesi geçiyor ama olumsuz biçimde: devamlilik G05-G08 satır 171 "EKSİK: yok (…)", teknik-danisman G01-G04 satır 142 "EKSİK: yok.", teknik-danisman G05-G08 satır 298 "EKSİK: yok (…)". Devamlilik G01-G04'ün GİRDİ satırında "EKSİK" yok. Protokole göre EKSİK yalnızca girdi açılamadıysa yazılır, yani anlamca ✅. Birebir "EKSİK içermiyor" taraması ise eşleşir. Teknik-danisman G01-G04 satır 1'de ayrıca "OKUNMAYAN / EKSİK KISIMLAR" başlığı var. Orada sayılanlar (§6-§7, plan, NOTLAR) görev girdisi değil. Bu yorum Fable'ın ve sahibin kararına kalıyor. |
| Ö3 | ✅ G01-G03 · doğrulanamadı G04-G08 | Dört eleştiride ÖLÜMCÜL 0, CİDDİ 33 (devamlilik 10+8, teknik-danisman 7+8). `F5_fable_birlestirme_1.md` her CİDDİ'yi K/G kararlarına bağlıyor. `_2_G01`, `_2_G02` ve `_2_G03` içinde §K KABUL/KISMEN/değmez tabloları tam okundu. `_2_G04…G08` yalnızca başlıkları okundu. |
| Ö4 | ✅ G01-G03 + FILM §5 · doğrulanamadı G04-G08 | G01: ORTAK satır 67'de 2.RHEA düzeltmesi var ("cutter panel, the tether panel, the grey disc panel and the wrist-link panel"). Gövdede "EMP" yok; yalnızca satır 12'de başlık notunda geçiyor. G02: `_2_G02`'deki yedi bekleyen düzenlemenin hepsi `G02.md`'de var: "woman's right arm rises from her side and her mouth stays closed" (52), "in one short, smooth pull" (96), "two paces ahead of them" (135), "each take a careful first step" ve "Each plants a second careful step" (140), "toward the levers with her mouth staying closed" (184), "toward the core while both their mouths stay closed" (294), başlıkta "C16 · C17 · C18 · C19 · C20" (15). C17'de DIŞ DÜNYA cümlesi ışık cümlesinden önce var. G03: C30'da "fades away" (150), C36'dan "tug docked" çıkmış (272), C27 notu düzeltilmiş (80), `dies/dead` yok. FILM §5 güncel: R29 ve R33 = 2.5, R12 = 2.0, telsiz Kaynak R02 R13 R17 R19 R25 R26 R36 R37, K8'deki tüm saniyeler uygulanmış. Doğrulanamayanlar: `_2_G07` "UYGULANMADI: Rhea'nın SAĞ bilek bağlantısı C73 · C77 · C83" ve "U1–U7" diyor; `G07.md` içinde karşılığını aramadım. G05 ve G08 raporlarındaki "15.10 uygulanamadı" satırlarına da bakmadım. G04 ve G06 içeriğini grep'lemedim. FILM §3 "Kullanan çekimler" ve §4 Referans sütununun K16'ya göre yeniden türetilmesini kontrol etmedim. `_2_G02` madde 8 (not satırlarına "15.10" gerekçesi) yazılmadı; rapor bunu kendisi söylüyor ve bu yalnızca not. |
| Ö5 | ✅ G01-G03 · doğrulanamadı G04-G08 | G01-G03'te RED yok. "değmez" satırları başka grubun işi diye gerekçeli. Diğer gruplara bakmadım. |
| Ö6 | ✅ | `DURUM.md` AÇIK ÖLÜMCÜL tablosu boş. Dört eleştiri de "ÖLÜMCÜL 0 … TUR KAPANABİLİR". |
| Ö7 M | ✅ (not var) | `DURUM.md`: FAZ 5, TUR 1, AJAN_CAGRI 20 / 50, SON_GUNCEL 15.10.2026, SIRADAKI dolu. `--bolum durum` geçerli. Not 1: FAZ GÜNLÜĞÜ'nün son satırı 14.10. 15.10'daki `_2` turu ve Fable yerleştirmesi günlüğe yazılmamış. Not 2: aritmetik 8+4+8=20, ben 21. çağrı olurum. "denetci (çağrı 20…)" ifadesi belirsiz. Sayaç alanı güncel sayılabilir, ama bunu Fable teyit etsin. |
| F5.1 M | ✅ | `--bolum prompt` çıktısı yukarıda: 96 çekim, yapı geçerli. |
| F5.2 | ✅ (ÖLÜMCÜL açık yok) · içerik doğrulanamadı | Devamlilik ÖZET'leri "ÖLÜMCÜL 0". Devamlilik G05-G08 "tarama yarıda kaldı" diyor ve YAPILMADI'da "C74/C75/C77/C81 dış-iç geometrisi tam doğrulanmadı" yazıyor. Düzeltmelerden sonra devamlilik yeniden bakmadı. Güncel promptlarda kimlik/taraf/sayı sorusunu ben bağımsız taramadım. |
| F5.3 | ✅ bakış · doğrulanamadı risk sütunu | Teknik-danisman GİRDİ'leri G01-G08 promptlarını ve FILM §3-§5'i kapsıyor. FILM §4 "Risk → nasıl gösterilir" sütununun 96 satırda dolu olduğunu saymadım. |
| F5.4 M | ⚠️ doğrulanamadı | Her grupta 12 `EKLE` satırı var (toplam 96/96). EKLE satırlarında numaralı dosya adı ve "yükleme sırası" yazılı. G01'de 15 `DOSYA ref/<No>.<AD>_v1.png` satırı var. `FLOW` (mod) satırını yalnızca G01 C02'de gördüm ("FLOW      Frames to Video"). G02-G08'de 96/96 saymadım. |
| F5.5 M | ✅ (zincir yok) | FILM.md satır 185-186 "bu filmde zincir yok (§4 Zincir sütunu '—')", satır 341 aynı. Not: `SAHNELEME.md` doldurulmamış şablon, içinde `Z1 · C02 C03 · <örn. …>` örnek satırı duruyor. Bu faz 3b'nin konusu, F5'i bağlamaz. |
| F5.6 | ⚠️ doğrulanamadı | Yazarların vuruş iskeleti beyanları var (`_2_G01`: aynı iskelet en çok 2 çekimde, `_2_G03`: en çok 3). Bunlar yazar beyanı. Güncel dosyalarda ben saymadım. |
| F5.7 | ⚠️ kısmen | G01'de 15 sayfa promptu var (`DOSYA` × 15). 10.CEKIRDEK'te 7 panelli `PANELLER` satırı ve "plain unmarked surfaces" ifadesi okundu. Çekimlerin istediği her açı ve durumun sayfada panel olması ve panel üstünde yazı istenmemesi tüm sayfalarda kontrol edilmedi. |
| F5.8 | ⚠️ doğrulanamadı | G02 C17'de DIŞ DÜNYA ve ORTAM SESİ cümleleri doğru yerde. ORTAK GÖRÜNÜM'ün 96 çekimde birebir olduğunu ve mekân ışık cümlesini ben saymadım. Yalnızca yazar raporlarında var ("ORTAK GÖRÜNÜM 24/24" `_2_G03`). |
| F5.9 M | ✅ (kısmi örnek) | `film_dogrula --bolum prompt` geçerli. Örnek: G02 C17 videosunda replik "says: Stay inside the pressure line." R17 ile birebir, telsiz kalıbıyla, kadrajdaki "mouth staying closed" yazılı. G02 C13, C19 ve C24'te de ağız-kapalı ifadeleri `grep` ile bulundu (52, 184, 294). |
| F5.10 | ⚠️ doğrulanamadı | C01-C03 promptlarını doğrudan okumadım. Yazı/logo yokluğu ve şeffaf vizör riskinin FILM §4 Risk sütununda yazılı olması yalnızca `_2_G01` raporunda beyan. |

MEKANİK ❌   yok. Doğrulanamayan mekanik maddeler: Ö2 (birebir "EKSİK" taraması eşleşiyor, anlamca temiz), F5.4 (FLOW satırı G02-G08'de sayılmadı).

YARGI ❌     yok. Doğrulanamayan maddeler:
- Ö3 ve Ö5: G04-G08.
- Ö4: G04-G08.
- F5.2, F5.3 (risk sütunu), F5.6, F5.7, F5.8, F5.10.

SONUÇ        KAPANAMAZ. Bunun nedeni ❌ bulmam değil, kanıt eksikliği. Yukarıdaki mekanik iki madde ve G04-G08 Ö4 doğrulanmadan faz kapatılamaz. Ö4'te özellikle `_2_G07` ve `_2_G05` raporlarındaki "UYGULANMADI"/"uygulanamadı" satırları açık bir risk.

Fable için not: G02 madde 8 (not satırlarına "15.10" gerekçesi) yazılmadı. Bu yalnızca not satırı, kapıyı etkilemez.

İlgili dosyalar (hepsi `/Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/THE_FURNACE_GATE/` altında):
- `FILM.md`
- `ODA/DURUM.md`
- `ODA/F5_fable_birlestirme_1.md`
- `ODA/F5_goruntu-yonetmeni_2_G01.md`
- `ODA/F5_goruntu-yonetmeni_2_G02.md`
- `ODA/F5_goruntu-yonetmeni_2_G03.md`
- `ODA/F5_goruntu-yonetmeni_2_G07.md`
- `PROMPTLAR/G01.md`
- `PROMPTLAR/G02.md`
- `PROMPTLAR/G03.md`
- `SAHNELEME.md`
