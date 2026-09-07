# 📐 DIŞ REFERANS ÖLÇÜMÜ — 10 klip · süre · kurulum · ölçek şahidi

> **Tek seferlik ölçüm çıktısı — 05.09.2026.** Sahibin depo DIŞINDAKİ
> referans klasöründen (`video/`, `.gitignore`) alınan iki tablo.
>
> ⛔ **BU BİR ANALİZ HATTI DEĞİLDİR.** Dış film analiz hattı aynı gün sahip
> kararıyla kapatıldı (`DIS_FILM_ANALIZI/00_README.md`). Bu dosya o hattın
> yeniden açılması değil: kaynak klipler ve ham raporlar depoya GİRMEDİ,
> yalnız aşağıdaki iki tablo kurtarıldı. Yeni referans gelirse buraya satır
> eklenir; **klip, kare veya ham rapor depoya alınmaz.**
>
> **Neden bu ikisi kurtarıldı:** kart G elemesinden geçtiler — (a) üretim
> hattımıza uygulanabilir, (b) sayısal kilide çevrilebilir, (c) bilinen bir
> açığı kapatıyorlar. Elenenler §4'te, gerekçeleriyle.

---

## 1. 📏 NASIL ÖLÇÜLDÜ

```
Süre · çözünürlük · fps  →  ffprobe kapsayıcı verisi (elle yazılmadı)
Kurulum sayısı           →  klip başına kesme sayımı
İçerik okuması           →  sahibin kendi kare analizinden (depo dışı)
Ham dosya                →  11 dosya, 10 benzersiz (biri byte-eş ikiz:
                            md5 84f5fe74… iki kez kopyalanmış)
```

⚠️ Kare ve piksel okuması bu depo tarafından YAPILMADI. İçerik sütunları
sahibin okumasıdır; süre/fps/çözünürlük ise makineyle doğrulandı.

---

## 2. ⭐ SÜRE VE KURULUM TABLOSU — `ACI_YAYI §4b`'nin saha kanıtı

| # | Konu | Süre | Çözünürlük | fps | Kurulum | Kesme |
|---|---|---|---|---|---|---|
| V01 | Kristal gemi · fırtına gözü | 68,6 sn | 720×1280 · 9:16 | 30 | **1** | 0 |
| V02 | Katmanlı kozmik panorama | 10,1 sn | 720×1280 · 9:16 | 24 | **1** | 0 |
| V03 | Satürn'den ayrılış | 22,2 sn | 1276×718 · 16:9 | 30 | **1** | 0 |
| V04 | Kara delik · akresyon diski | 10,5 sn | 720×1280 · 9:16 | 30 | **1** | 0 |
| V05 | Sisli orman yolu | 90,8 sn | 1204×720 · 16:9 | 30 | **1** | 0 |
| V06 | Yörüngede su küresi | 30,2 sn | 1280×720 · 16:9 | 30 | **1** | 0 |
| V07 | Cyberpunk dikey megakent | 10,1 sn | 720×1280 · 9:16 | 24 | **1** | 0 |
| V08 | Pencereden megastrüktür | 10,1 sn | 720×1280 · 9:16 | 24 | **1** | 0 |
| V09 | Süper hücre fırtınası | 10,2 sn | 720×1280 · 9:16 | 30 | **1** | 0 |
| V10 | Uzay-zaman ışık koridoru | 8,1 sn | 720×1280 · 9:16 | 30 | **1** | 0 |

```
10 klip · 271,0 sn · TOPLAM KESME: 0
Hiçbiri açı değiştirmiyor. Hiçbiri ölçek kademesi atlamıyor.
Bir klip = bir kurulum.
```

### 2.1 ⚠️ Tablonun iki tuzağı — bunlar okunmadan tablo YANLIŞ okunur

```
⛔ V05 (90,8 sn) AI ÜRETİMİ DEĞİLDİR. Bir Steam oyun tanıtımıdır —
   motor içi görüntü. Kendi prompt kopyası "Unreal Engine 5 render"
   yazıyor. En uzun ve en etkileyici satır, bir video modelinin ne
   tutabileceği hakkında HİÇBİR ŞEY söylemez. Kanıt sayılmaz.

⛔ V01 ve V03 AYNI SERİDİR. İkisinin de kaynak adında "Halide" geçiyor
   (biri gemi geliyor, öteki Satürn'den ayrılıyor). Tek yaratıcının tek
   işi; iki bağımsız örnek DEĞİL.
```

**Bu ikisi düşülünce geriye 8 bağımsız AI klibi kalır:**

```
ortanca süre        10,1 sn
en kısa / en uzun    8,1 / 68,6 sn
8-11 sn bandında     6 / 8 klip
```

### 2.2 ⭐ ÇIKAN DERS — §4b bunun için var

Doğru okuma **"uzun tek çekim çalışıyor"** DEĞİLDİR; o okumayı yalnız
oyun promosu ile aynı serinin ikinci klibi destekler. Doğru okuma şudur:

```
BİR ÜRETİM = BİR KURULUM, ve yaratıcılar KESMİYOR.
Bağımsız AI kliplerinin ortancası 10,1 sn — tam bir üretim boyu.
```

Bizim tarafımızda ise `ACI_YAYI §3` her kesme sınırında kurulum
değiştirmeyi ZORUNLU kılıyor. Sahibin şikâyeti — *"durmadan 10 saniyede
bir bambaşka bir kamera açısına geçmesi kafa karıştırıyor"* (05.09.2026) —
bu tablonun doğrudan karşılığıdır: **beğenilen referansların hiçbiri açı
değiştirmiyor.**

⭐ `§4b` (küme ≥2 · dönüş ≥%40) bu tablodan doğdu. Kural sorgulanırsa
gerekçe burasıdır.

⚠️ Ama tablo §3'ü İPTAL ETMEZ. §3'ün güvenli bandı bir halüsinasyon
kalkanıdır (benzer iki kurulum AI'ın mikro farklarını sırıtır). Referanslar
kesmediği için o riski hiç almıyor; biz kesmek zorundayız. Tablonun
söylediği tek şey: **kestiğimiz her yerde değil, DÖNMEDİĞİMİZ yerde
hata yapıyoruz.**

---

## 3. 🔭 ÖLÇEK ŞAHİDİ SÖZLÜĞÜ — `UZAY_USSU §5.3`'e işlenmiş örnek listesi

> §5.3 ölçek şahidi kuralını ZATEN kuruyor (bant merdiveni + üç araç) ve
> `02_RISK_KARTLARI:509` ile `HOOK_VE_ILK_SAHNE §252` onu tekrarlıyor.
> **Buradaki katkı yeni bir prensip değil, kuralın 10 işlenmiş vakasıdır:**
> her satırda şahidin ADI konmuştur. Kapı yazılacaksa kelime havuzu budur.

| # | ŞAHİT (bilinen boy) | ÖLÇÜLEN (devasa olan) | §5.3 aracı | Kilitli kamerada? |
|---|---|---|---|---|
| V01 | ince asansör/kablo hattı | kasırga gözü | ③ taşan kenar | ✅ |
| V02 | ön plandaki asteroit kayaları | gezegen şehir ışık ağı → nebula | ① ön plan nesne | ✅ |
| V03 | iğne biçimli gemi (kadrajın ~%1'i) | Satürn halka sistemi | ① + ③ | ✅ |
| V04 | küçük gezegen silueti | akresyon diski | ① ön plan nesne | ✅ |
| V05 | yol levhası + elektrik direkleri | yutucu sis derinliği | ② tekrar eden birim | ✅ |
| V06 | koşan astronot gövdesi | dev su küresi + balinalar | ① ön planda figür | ✅ |
| V07 | "40" numaralı bipedal mecha | kilometrelik dikey kuleler | ① + ③ | ✅ |
| V08 | **pencere kasası + iç mekân zemini** | bulutlardan çıkan küresel yapı | ⭐ §5.3'te YOK | ✅ |
| V09 | kaçışan kuş sürüsü + telefon direkleri | süper hücre bulutu | ② + ① | ✅ |
| V10 | — (soyut; şahit yok) | uzay-zaman koridoru | — | ❌ |

### 3.1 ⭐ ADAY: dördüncü statik araç — çerçeve içinde çerçeve

§5.3 kilitli kamerada çalışan **üç** araç sayıyor: ① ön planda figür ·
② tekrar eden birim · ③ kadrajı taşan kenar. V08 dördüncüsünü gösteriyor:

```
④ ÇERÇEVE İÇİNDE ÇERÇEVE — kadrajın kenarını bilinen bir insan yapısı
   tutar (pencere kasası, kapı boşluğu, luka, vizör kenarı). Şahit
   sahnenin İÇİNDE değil, KADRAJIN KENARINDADIR; izleyicinin kendi
   bakış noktasını insan ölçeğine çakar, dışarısı ne kadar büyürse
   büyüsün ölçek kaçmaz.
```

⚠️ **Bu bir ADAYDIR, kural değildir.** Üretimde ölçülmedi. §5.3'e girmesi
için yol `AGENTS.md` görev kartı **G**'dir. Dış kaynaklı derslerde kart G
adım 5 (*"önce kaynak rubriği yamala"*) geçersizdir — yamanacak rubrik yok,
ders doğrudan `UZAY_USSU §5.3`'e işlenir.

### 3.2 ⛔ SÖZLÜĞÜN SINIRI — referanslar bizim yapamadığımız şeyi yapıyor

Bu 10 klibin hepsi ölçeği **kamera hareketiyle** kuruyor: paralaks
süzülüş, vinç tırmanışı, ileri dolly. `UZAY_USSU §5.3` bunu açıkça
yasaklıyor:

> ⛔ *Paralaks ve yavaş dönüş bu depoda KULLANILAMAZ (kamera kilitli).*

Bu yüzden tablonun **"Kilitli kamerada?"** sütunu zorunludur: taşınabilir
olan şey klibin HAREKETİ değil, ŞAHİDİN KENDİSİDİR. On vakanın dokuzunda
şahit kamera dursa da işini görür; onuncusunda (V10) hiç şahit yoktur ve
o klip bu depoya hiçbir şey vermez.

---

## 4. ⛔ NE TAŞINMADI — ve neden

| Elenen | Gerekçe |
|---|---|
| Prompt şablon bankası | `Unreal Engine 5 render` · `Octane render quality` negatif çekirdekle **doğrudan çelişiyor**: çekirdek `No Unreal Engine look, no CGI aesthetic, no video game aesthetic` diyor (`KILAVUZ_REHBERI §5`) |
| `(worst quality, low quality:1.4)` | Stable Diffusion / A1111 ağırlık sözdizimi — Veo ayrıştırmaz, düz metin olarak yutar |
| Şablonların kendi negatif blokları | Negatif çekirdek zorunlu ve TEKTİR; ikinci bir kaynak iki doğruluk kaynağı yaratır |
| `static camera` negatifi | Depo `fixed lockoff` planlarını meşru kurulum olarak kullanıyor; bu negatif kendi çekimlerimizi vurur |
| Saniye saniye TC tabloları | Tek sürekli hareketi 3-4 satıra bölüp her satıra farklı açı yazıyorlar — **shot list sanılırsa şikâyet edilen sorunu öğretirler** |
| `1:100.000` · `1:1.000.000` ölçek oranları | Ölçülmemiş, elle yazılmış sayılar — kural ① ihlali |
| Kaynak dosya işaretçileri | 10 raporun 9'unda "Orijinal Dosya" adı klasörde yok; geri izlenemiyor |
| Kare setleri | `frames/` numaraları ikiz dosya yüzünden raporlardan bir kayıyor (rapor V08 ← kare seti v09, V09 ← v10, V10 ← v11) |
| fps / çözünürlük iddiaları | V02·V07·V08 "30 fps" diyor, üçü de 24 · V03 ve V05 çözünürlükleri yanlış — bu dosyadaki tablo makineyle yeniden ölçüldü |

⚠️ **Ham raporlarda çözülmemiş bir madde var:** V10 raporu kaynağını
"solucan deliği" diye okuyup "kara delik" etiketini reddediyor, ama o
dosyanın kendi başlığı *"the matter inside a black hole's accretion
disk"* diyor — ve akresyon diski tarifi V04'e yazılmış. İkisi yer
değiştirmiş olabilir. **Karar sahibindedir**; bu depo kareye bakmadı ve
yukarıdaki iki tabloya bu şüpheden hiçbir satır girmedi.

---

## 5. 🔗 NEREYE BAĞLI

```
ACI_YAYI_VE_SEKANS_KILAVUZU.md §4b  → §2 süre tablosu (kuralın gerekçesi)
UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md §5.3 → §3 şahit sözlüğü
DIS_FILM_ANALIZI/00_README.md       → kapalı hattın kaydı (bu dosya onun
                                       yeniden açılması DEĞİLDİR)
AGENTS.md kart G                    → §3.1 adayının kural olma yolu
```

---

## 📝 DEĞİŞİKLİK KAYDI

```
05.09.2026  Açıldı. Sahibin depo dışı referans klasöründen (10 benzersiz
            klip · 271,0 sn) iki tablo kurtarıldı: süre/kurulum ölçümü ve
            ölçek şahidi sözlüğü. Prompt bankası, TC tabloları, ölçek
            oranları ve kaynak işaretçileri ELENDİ (§4). Klipler
            .gitignore'a alındı — depo yalnız PROMPT tutar.
```
