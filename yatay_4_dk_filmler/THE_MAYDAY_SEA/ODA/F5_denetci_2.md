FAZ 5 KAPISI · yatay_4_dk_filmler/THE_MAYDAY_SEA (denetçi, 2. denetim, 12.10.2026, çağrı 7)

Film klasörü hâlâ untracked (`git status`: `?? yatay_4_dk_filmler/THE_MAYDAY_SEA/`). Ö4'ü bu yüzden ODA'daki `_1_` sürümleri, §K tabloları ve `PROMPTLAR/` metniyle yan yana okuyarak denetledim. Gerekli yerde `git diff --no-index` de kullandım.

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 **M** | ✅ | `ODA/F5_devamlilik_1.md` ve `ODA/F5_teknik-danisman_1.md` yerinde. Ek geçiş `ODA/F5_devamlilik_1b.md` dosyası da var. |
| Ö2 **M** | ✅ | 1b s.108-113'te GİRDİ satırı var: `PROMPTLAR/G02.md (yeni sürüm, tam)`, G01/G03 grep, FILM §4 s.144/146/149. "EKSİK" geçmiyor. Kısmi okuma YAPILMADI satırına açıkça yazılmış, protokole uygun. Önceki iki dosya 1. denetimdeki gibi ✅. |
| Ö3 | ✅ | 1b'de yeni CİDDİ ya da ÖLÜMCÜL bulgu yok (`ÖLÜMCÜL 0 · CİDDİ 0 · KÜÇÜK 2`). İki KÜÇÜK bulgu da cevaplanmış. B16 için G02 §K s.26'da KABUL var. B17 FILM §6 s.253'te işlenmiş. Önceki 17 CİDDİ bulgunun cevapları 1. denetimdeki gibi tam. |
| Ö4 | ✅ | **Önceki ❌'lerin dördü de kapandı.** (1) Kimlik tabanı artık bölünmüyor. G03 s.79'da C18 şöyle: `…dark navy shoulder armor, and a round ivory helmet with a completely clear closed visor, strapped into the navy seat. A single circular gold-and-blue mission badge…` (rozet ayrı cümlede). G03 s.188'de C23 şöyle: `…completely clear closed visor, strapped into the navy seat, fills the left half of the frame. She wears narrow burnt-orange forearm bands, white gloves and a single circular…`. Taban, G01 s.22 ve G02 s.19'daki tabanla harfi harfine aynı. G03 başlığı s.24'te artık "BÖLÜNMEZ" yazıyor. (2) FILM §4 C18 (s.144) "kontrollü bir nefes alır (… F5 teknik B13)" diyor. `aceleci`/`urgent` sözcüğü FILM'de de G03'te de yok. (3) FILM §4 C19 (s.145) tarifi "su toplanır, halkanın parlak yüzeyi parlaklaşır, boyutu değişmez" diyor. Risk sütunu da aynı yönde: "'sıkılaşma' yerine … toplanma + parlaklaşma". (4) G03 C19 notu (s.95) "halka sokete ZATEN oturmuş (seated flush) ve kelepçe AÇIK" diyor; eski "ince boşluk" metni gitti. **Yeni KABUL'ler:** B16 G02 s.188'de uygulanmış: `0-3 s: The camera stays locked at a great distance; the surface ripples drift slowly rightward while…`. B17 FILM §6 Y5 s.253'te uygulanmış: `heard from outside the water … diegetik değil, tasarım (F5 devamlilik B17)`. |
| Ö5 | ✅ | Yeni RED yok. Tek RED G02 T2b; gerekçesi kanıta cevap veriyor (1. denetimdeki gibi; G02 §K s.29). |
| Ö6 | ✅ | Üç eleştiri dosyası da `ÖLÜMCÜL 0`. 1b de 0 veriyor (s.107). DURUM'daki AÇIK ÖLÜMCÜL tablosu boş (s.19-20). |
| Ö7 **M** | ✅ | `film_dogrula --bolum durum` çıktısı `✅ yapı geçerli`, EXIT=0. DURUM s.8-14'te FAZ 5, TUR 1 ve SON_GUNCEL 12.10.2026 doğru. SIRADAKI (s.11) artık açılış adımını değil kapı sonrası zinciri gösteriyor ve şu anki adım olan "denetci 2"yi içeriyor. AJAN_CAGRI 7/50 sayılmış çağrılarla tutuyor: çağrı 1-5 yazarlar ve eleştirmenler, 6 denetçi 1, 7 bu denetim. SendMessage devamları NOTLAR s.82-89'da "sayılmaz" diye yazılı. Gözlem 1'e bakın. |
| F5.1 **M** | ✅ | `film_dogrula … --bolum prompt` çıktısı `çekim: 24 · ✅ yapı geçerli`, EXIT=0. `cekim`, `replik`, `sahneleme` ve `muzik` bölümleri de ✅ ve EXIT=0. |
| F5.2 | ✅ | devamlilik 1 ve 1b `ÖLÜMCÜL 0`. 1b s.91-101'e göre "G03 C18 ve C23 kimlik cümleleri: BULGU YOK", kokpit yönü tutarlı. |
| F5.3 | ✅ | Değişiklik yok, 1. denetimdeki kanıt geçerli (teknik GİRDİ: "risk sütunu dolu çekimler + 9 sayfa"). |
| F5.4 **M** | ✅ | İş emrinde G01 9 ref, 8 kare ve 8 ham satırı taşıyor. G02 ve G03'te 8 kare ve 8 ham satırı var. Toplam 9 ref, 24 kare, 24 video. Örnek: G02 s.232 `kare/C15.png · ref/4.OKYANUS_v1.png (canlı ağ paneli) · ref/9.CANLI_SU_v1.png (zar paneli; bu sırayla)`. |
| F5.5 **M** | ✅ (zincir yok) | FILM §4 Zincir sütunu 24/24 "—". `--bolum sahneleme` ✅. |
| F5.6 | ✅ | 1. denetimdeki kanıt geçerli. G02 §K s.18'e göre sekiz çekimin her biri ayrı iskelet. G03 §K s.18'e göre de sekizi birbirinden farklı. |
| F5.7 | ✅ | 1. denetimdeki kanıt geçerli. 1b s.81-89 G02'deki yeni panel adlarını sayfa metniyle doğruladı: `wall-climb panel`, `underside panel` ve `living network panel`. |
| F5.8 | ✅ | **Önceki ❌ kapandı.** "İlk vuruş hareketle" maddesi: 1b s.3-43'te 24 çekimin tablosu var; tek bulgu B16 (C15) ve düzeltildi. Kendim de 24 ilk vuruşu grep ile çıkardım; hepsinde kamera ya da nesne hareketi var. Örnekler: C10 `the single dark teal ribbon begins to creep upward`, C15 `the surface ripples drift slowly rightward`. "Aynı-mekân ölçek/açı farkı" maddesi: 1b s.45-58. Çift listesi FILM §6 ORTAM YATAĞI ile tam örtüşüyor (Y1 C03→C04→C05 ve C21→C22, Y3 C06→C07→C08, Y4 C11→C12→C13). Lensleri dosyada doğruladım: G01 s.187/208/230 28/50/85 mm, s.252/274/296 24/100/85 mm; G02 s.94/116/138 24/100/85 mm; G03 s.145/167 50/35 mm. Ortak görünüm, ışık ve ortam sesi kısmı 1. eleştiride KORU ve B15 ile denetlenmişti. |
| F5.9 **M** | ✅ | `--bolum prompt` ✅. Ağız kapalı satırları duruyor: G01 s.172 (C02), G01 s.257 (C06), G03 s.193 (C23). |

**Gözlemler** (madde değil, kanıtlı):
1. DURUM s.11 SIRADAKI, yapılmış düzeltmeleri ("DURUM SIRADAKI · FILM §4 C18/C19 · G03 C18/C23 · devamlilik F5.8 ek geçişi") hâlâ yapılacak gibi sıralıyor. Bu işler dosyalarda tamam. FAZ GÜNLÜĞÜ'nde (s.39-46) denetçi 1, düzeltmeler ve 1b için satır yok; bu kayıtlar yalnız NOTLAR s.85-89'da. Kapı kapanınca bu satırların güncellenmesi gerekiyor.
2. `PROMPTLAR/G03.md` C24 notu (s.203) ve G03 §K s.57 hâlâ "FILM §5 R18 saniyesi 4.0 → 3.0 olmalı (Fable'ın işi)" diyor. FILM §5 s.190 zaten 3.0. Notlar kod bloğunun dışında, promptu etkilemiyor.
3. 1. denetimdeki "G02 yazar değişikliklerini eleştirmen görmedi" gözlemi kapandı. 1b (3), s.60-89, C14 geometrisini, C10 `wall-climb panel`ı ve C15 referans cümlesini denetledi; yeni ÖLÜMCÜL bulmadı. B16 sonrası C15 değişikliğine (KÜÇÜK, tek vuruş) ayrıca eleştirmen bakmadı.
4. 1b'nin devamlilik ajanı yazar cevap dosyalarını açmamış (s.113, YAPILMADI). Bağımsız göz ilkesi korunmuş.

```
MEKANİK ❌   yok
YARGI ❌     yok
SONUÇ        KAPANABİLİR (mekanik: yok / yargı: yok)
```
