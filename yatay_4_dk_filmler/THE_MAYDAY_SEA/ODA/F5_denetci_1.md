**FAZ 5 KAPISI · yatay_4_dk_filmler/THE_MAYDAY_SEA** (denetci, 12.10.2026, çağrı 6)

Bu turda git diff yok: film klasörünün hepsi untracked (`??`). Ö4'ü ODA'daki `_1_` sürümlerle `PROMPTLAR/` arasında yan yana okuyarak denetledim.

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 **M** | ✅ | AGENTS.md §2'ye göre F5'in eleştirmenleri devamlilik ve teknik-danisman. İkisinin dosyası var: `ODA/F5_devamlilik_1.md` ve `ODA/F5_teknik-danisman_1.md`. |
| Ö2 **M** | ✅ | İki dosyada da GİRDİ satırı var ve "EKSİK" içermiyor (devamlilik s.253-257, teknik s.144-161). Çalıştırılmayan araç YAPILMADI satırına yazılmış; bu protokole uygun. |
| Ö3 | ✅ | 17 CİDDİ bulgunun hepsine cevap var. devamlilik B1-B9 ve teknik B1-B8, üç §K tablosunun en az birinde KABUL ya da RED aldı. Kısmi cevaplar gerekçeli: D8 G03'te KISMEN, T8 G01/G02'de KISMEN ama G03'te KABUL, T2 ise G02'de T2a KABUL ve T2b RED olarak bölündü. |
| Ö4 | ❌ | Çoğu KABUL uygulanmış, iki kalıntı var. (1) **D1/K1, G03 C18 ve C23.** Kimlik tabanı bölünmüş: C18'de `…dark navy shoulder armor, a single circular gold-and-blue mission badge… on her left chest, and a round ivory helmet…`, C23'te `…shoulder armor, narrow burnt-orange forearm bands, white gloves and a single circular… badge…, and a round ivory helmet…`. G01 ise tabanı bölmüyor. C06 ekleri tabandan sonra yazıyor ve G01 §K bunu bilerek düzeltmiş ("önceki sürümde ekler tabanın ortasına gömülüydü"). G03 başlığı s.24 "üç grupta birebir" diyor, metin tutmuyor. (2) **FILM §4 eski metni taşıyor.** C18 hâlâ "kontrollü aceleci bir nefes alır" diyor; T13 KABUL edildi, prompt `draws one controlled breath` oldu. C19 hâlâ "şerit … yavaş sıkılaşır" diyor; T7/K12 KABUL edildi ve aynı satırın Risk sütunu tersini söylüyor. |
| Ö4 (uygulananlar) | ✅ | Hepsini yeni sürümde buldum. G01: C02, C06, C07, C08 replik sonda; C05 `seated flush` ve tek hareket kelepçe; C04 `6-10 s: The glide slows but keeps moving`; sayfa 2 altı panel ve halka durumu ayrı cümle; sayfa 3'te `lever pulled, receiver on panel`; sayfa 4'te `short swept wings`, sayfa 7'de `dark navy rim`; `glove panel`. G02: sekiz çekimin her referansında tek panel adı; C16 yalnız `wreck-cord panel`; EKLE satırı KARE/VİDEO diye ayrı; `Render…` kalktı. G03: `beside her right shoulder`, `A right white glove`, `her left white glove`; C19/C21 bant cümlesi; "tighten" yok; C22 `steady pace`; C24 18 mm, `still held by the closed clamp`, `0-3·3-8·8-10`; video promptlarında "lever" en çok 2 kez. Ses tarifleri üç grupta K7 kalıbında. FILM §5 R18 saniyesi 3.0 oldu. SMOKE_TEST P18 satırına "C02 ↔ C13 · C03 ↔ C22" karşılaştırması eklendi. Vuruş iskeleti en çok 3 çekimde tekrarlanıyor (C06·C07·C11 ve C04·C10·C21). |
| Ö5 | ✅ | Tek RED, G02 T2b. Gerekçe bulgunun kanıtına cevap veriyor: C13 kadrajı "framed from the top of her helmet down to her shoulders", eller kadrajda değil, bu yüzden `white gloves` eklenmedi. |
| Ö6 | ✅ | Her iki eleştiride `ÖLÜMCÜL 0`. DURUM'daki AÇIK ÖLÜMCÜL tablosu boş. |
| Ö7 **M** | ❌ | `film_dogrula --bolum durum` ✅ veriyor; FAZ 5, TUR 1, AJAN_CAGRI 6/50 ve SON_GUNCEL alanları doğru. Ama DURUM.md s.11 SIRADAKI hâlâ fazın açılış adımını gösteriyor: "F5 promptlar: goruntu-yonetmeni G01 · G02 · G03 paralel … → cp PROMPTLAR → ODA → devamlilik + teknik-danisman → …". FAZ GÜNLÜĞÜ s.46'ya göre bu adımların hepsi yapıldı. Sıradaki adım güncel değil. |
| F5.1 **M** | ✅ | `film_dogrula.py … --bolum prompt` çıktısı: "çekim: 24 · ✅ yapı geçerli", EXIT=0. `cekim`, `replik`, `sahneleme` ve `muzik` bölümleri de ✅. |
| F5.2 | ✅ | devamlilik `ÖLÜMCÜL 0`. Not: Ö4'teki kimlik tabanı kalıntısı CİDDİ D1'in artığı, ÖLÜMCÜL değil. |
| F5.3 | ✅ | teknik-danisman GİRDİ satırı "G01-G03 risk sütunu dolu çekimler + 9 sayfa" diyor. Bulgular C05, C18-C24 ve C02'ye bakıyor. |
| F5.4 **M** | ✅ | İş emri G01'de 25, G02'de 16, G03'te 16 satır. Her satırda dosya, mod ve `ref/<No>.<AD>_v1.png` var, yükleme sırası ve panel adıyla. |
| F5.5 **M** | ✅ (yok) | Zincir yok: FILM §4 Zincir sütunu 24/24 "—". film_dogrula `sahneleme` ✅. |
| F5.6 | ✅ | devamlilik üç alt maddeye de bakmış: aynı numara aynı rol (KORU s.242), iskelet tekrarı (B8), donan son vuruş (B11). |
| F5.7 | ✅ | Dokuz özneye dokuz tek sayfa. Çekimlerin andığı her panel G01 sayfa metninde var; örnekler `side view after separation panel`, `lever pulled, receiver on panel`, `glove panel`, `underside panel`, `wreck-cord panel`. Sayfa promptları "plain unmarked surfaces" ile bitiyor. |
| F5.8 | ❌ | devamlilik ortak görünüm cümlesine (KORU 48/48), ortam sesine (24/24) ve mekân ışık sarmalayıcısına (B15) bakmış. "İlk vuruş hareketle başlıyor" ve "ardışık aynı-mekân çekimlerinde ölçek/açı farkı" alt maddeleri için `F5_devamlilik_1.md`'de bulgu, KORU ya da BULGU YOK satırı yok. Bakıldığına dair kanıt dosyada değil. |
| F5.9 **M** | ✅ | film_dogrula prompt ✅. Alıcıdan gelen seste ağız kapalı yazılı: C02 `Her lips stay closed`, C06 `her lips stay closed`, C23 `her mouth stays closed`. Kalan alıcı/telsiz repliklerinde kadrajda kimse yok. |

**Gözlemler (madde değil, kanıtlı)**
- `PROMPTLAR/G03.md` C19 notu hâlâ "C05 karesinde … halka ile soket arasında ince boşluk vardır" diyor. K11'den sonra C05 `seated flush`. Not kod bloğunun dışında, promptu etkilemiyor.
- Tur 2 açılmadı. Yazarın kendi başına yaptığı değişiklikleri (G02 C14 kamera geometrisi, C10 `wall-climb panel`, C15 referans cümlesi) hiçbir eleştirmen görmedi. ELESTIRI_PROTOKOLU §3'teki "yeni ÖLÜMCÜL doğdu mu" kontrolü bu değişiklikler için yapılmadı.
- teknik-danisman GİRDİ satırına göre NOTLAR.md ve DURUM.md'yi okumuş (Fable gerekçeleri orada). Bu, AGENTS ⑧ "bağımsız göz" ilkesine ters.

```
MEKANİK ❌   Ö7 — DURUM.md SIRADAKI güncel değil (s.11). Tek satırlık düzeltme: kapı sonrası adım yazılacak.
YARGI ❌     Ö4 — G03 C18/C23 kimlik tabanı bölünmüş; FILM §4 C18 (nefes) ve C19 ("sıkılaşır") KABUL'den sonra eski metinde.
             F5.8 — devamlilik'in "ilk vuruş hareketle" ve "aynı-mekân ölçek/açı farkı" denetimine dosyada kanıt yok.
SONUÇ        KAPANAMAZ (mekanik: Ö7 / yargı: Ö4, F5.8)
```
