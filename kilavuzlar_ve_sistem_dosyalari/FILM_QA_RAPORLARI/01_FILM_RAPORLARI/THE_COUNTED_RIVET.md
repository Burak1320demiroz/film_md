# 🎬 THE_COUNTED_RIVET — FİLM QA RAPORU

> **Durum:** 15 merceğin tamamı işlendi (30.09.2026). Tamlık 0/4 (① KARE ve ④ HİKAYE ⛔ TEKRAR [D129] olduğu için tamlık matrisine girmedi).
> **15 Mercek Özeti:**
> - ① KARE: `ACCEPT WITH FIX PASS` (⛔ **TEKRAR** · SPEC varken mod V koşuldu [D129] · düzeltilmiş skor: 8.1 · T1'e satır yazılmaz).
> - ② DEVAMLILIK: `FIXABLE IN EDIT` (⚠️ **ŞARTLI: 5.8** · T2 tablosuna işlendi · balyoz/çekiç dönüşümü, kol bandı yön kayması, S13 bulut biyomu sapması ve S14↔S15 mükerrer çekim).
> - ③ SES: `SOUNDTRACK HOLDS` (⚠️ **ŞARTLI: —** · T3 tablosuna işlendi · 0 replik, tasarımlı sessiz; kusursuz 3 kategori D186 uyarınca `—` yapıldı).
> - ④ HİKAYE: `REVISE STRUCTURE` (⛔ **TEKRAR** · SPEC varken mod V koşuldu [D129] · düzeltilmiş skor: 4.7 · T4'e satır yazılmaz · Sisifos mekanik döngüsü, ödenen bedel finali).
> - ⑤ ARKA PLAN: `FIELD DRIFTS BUT RECOVERABLE` (✅ **GO: 6.3** · T5 tablosuna işlendi · 24/24 sahnede sağ alt köşe ✦ filigranı [D150/D162] · S13 bulut denizi morfu · fener direği/braket kayması).
> - ⑥ FİZİK: `TWO GRAVITIES` (⛔ **TEKRAR** · SPEC varken mod V koşuldu [D129] · düzeltilmiş skor: 7.6 · T6'ya satır yazılmaz · $0.33\text{ m/s}^2$ ile $6.67\text{ m/s}^2$ arası 20 kat yerçekimi dalgalanması · kütlesiz balyoz darbesi).
> - ⑦ AKSİYON: `FIXABLE IN EDIT` (⛔ **TEKRAR** · SPEC varken mod V koşuldu [D129] · düzeltilmiş skor: 8.2 · T7'ye satır yazılmaz · B15 duplicate çekim, S5 küre anomalisi).
> - ⑧ EFOR: `THE BODY PAYS` (⛔ **TEKRAR** · SPEC varken mod V koşuldu [D129] · düzeltilmiş skor: 8.5 · T8'e satır yazılmaz · 19 efor olayının tamamında beden maliyeti ekranda · kask içi nefes ve visor buğusu).
> - ⑨ KADRAJ: `RHYME BROKEN` (🚨 **GEÇERSİZ** · SPEC verilmeden mod V koşulduğu için karantinadadır [D190/D184] · düzeltilmiş skor: 7.6 · T9'a satır girmez · S1↔S24 kafiye çifti plan dışı kurulumla kırık).
> - ⑩ OYUNCULUK: `TASK WITHOUT FEELING` (🚨 **GEÇERSİZ** · SPEC verilmeden mod V koşulduğu için karantinadadır [D190/D184] · düzeltilmiş skor: 5.7 · T10'a satır girmez · 17 sahne / 16 kesme sayımıyla ölçümden saptı, mekanik el hareketleri duygu taşımıyor, S16 CU hariç bedensel karar okunmuyor).
> - ⑪ IŞIK: `GRADEABLE DRIFT` (🚨 **GEÇERSİZ** · SPEC verilmeden mod V koşulduğu için karantinadadır [D190/D184] · düzeltilmiş skor: 6.1 · T11'e satır girmez · S13 bulut katmanı soğuk Kelvin kayması, S21 gri doygunluk düşüşü, S23 yetkisiz toz fırtınası).
> - ⑫ HOOK: `HOOK MISSING` (🚨 **GEÇERSİZ** · SPEC verilmeden mod V koşulduğu için karantinadadır [D190/D184] · düzeltilmiş skor: 5.2 · T12'ye satır girmez · açılışta görev icrası merak uyandırmıyor, 03:05 kask içi CU güçlü kapak adayı, 04:00 jenerik kartı döngüyü kırıyor).
> - ⑬ UYUM: `PROMPT GAP` (✂️ **KESİK** · Sahne promptları sağlanmadığı için koşulamadı · tabloya girmez, partiyi düşürmez, yeniden koşulmalıdır).
> - ⑭ HAREKET: `MOTION WITHOUT PURPOSE` (⛔ **TEKRAR** · SPEC varken mod V koşuldu [D129] · düzeltilmiş skor: 7.6 · T14'e satır yazılmaz · 4 amaçsız hareket: 0:30 pandomim el gezinmesi, 1:00 nedensiz 180° dönüş, 1:30 el kararsızlığı, 2:10 cetvel kaydırma döngüsü).
> - ⑮ YÖN: `EVERY VECTOR LANDS` (⛔ **TEKRAR** · SPEC varken mod V koşuldu [D129] · düzeltilmiş skor: — · T15'e satır yazılmaz · 24 HIT / 0 MISS · 8 kategori 10/10 kusursuz kategori kuralı D186 uyarınca `—` yapıldı).

---

## 📦 MALZEME VE DEPO YOLLARI

```
HAM RAPORLAR    kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_COUNTED_RIVET/
                ├── THE_COUNTED_RIVET_1_KARE_HAM.md (① KARE · mod V · 245 s · 23 kesme · ⛔ TEKRAR [D129])
                ├── THE_COUNTED_RIVET_2_DEVAMLILIK_HAM.md (② DEVAMLILIK · mod — · 245 s · 24 sahne · ⚠️ ŞARTLI: 5.8)
                ├── THE_COUNTED_RIVET_3_SES_HAM.md (③ SES · mod — · 244 s · 0 replik · ⚠️ ŞARTLI: —)
                ├── THE_COUNTED_RIVET_4_HIKAYE_HAM.md (④ HİKAYE · mod V · 244 s · 23 sahne · ⛔ TEKRAR [D129])
                ├── THE_COUNTED_RIVET_5_ARKA_PLAN_HAM.md (⑤ ARKA PLAN · mod — · 244 s · 24 sahne · ✅ GO: 6.3)
                ├── THE_COUNTED_RIVET_6_FIZIK_HAM.md (⑥ FİZİK · mod V · 245 s · 24 sahne · ⛔ TEKRAR [D129])
                ├── THE_COUNTED_RIVET_7_AKSIYON_HAM.md (⑦ AKSİYON · mod V · 245 s · 22 kesme · ⛔ TEKRAR [D129])
                ├── THE_COUNTED_RIVET_8_EFOR_HAM.md (⑧ EFOR · mod V · 245 s · 24 kesme · ⛔ TEKRAR [D129])
                ├── THE_COUNTED_RIVET_9_KADRAJ_HAM.md (⑨ KADRAJ · mod V · 245 s · 23 kesme · 🚨 GEÇERSİZ [D190])
                ├── THE_COUNTED_RIVET_10_OYUNCULUK_HAM.md (⑩ OYUNCULUK · mod V · 244 s · 16 kesme · 🚨 GEÇERSİZ [D190])
                ├── THE_COUNTED_RIVET_11_ISIK_HAM.md (⑪ IŞIK · mod V · 240 s · 23 kesme · 🚨 GEÇERSİZ [D190])
                ├── THE_COUNTED_RIVET_12_HOOK_HAM.md (⑫ HOOK · mod V · 245 s · 23 kesme · 🚨 GEÇERSİZ [D190])
                ├── THE_COUNTED_RIVET_13_UYUM_HAM.md (⑬ UYUM · mod MISSING · ✂️ KESİK)
                ├── THE_COUNTED_RIVET_14_HAREKET_HAM.md (⑭ HAREKET · mod V · 240 s · 23 kesme · ⛔ TEKRAR [D129])
                └── THE_COUNTED_RIVET_15_YON_HAM.md (⑮ YÖN · mod V · 244 s · 23 kesme · ⛔ TEKRAR [D129])

PLAN & SPEC     yatay_4_dk_filmler/THE_COUNTED_RIVET/
                ├── THE_COUNTED_RIVET_PLAN.md (24 klip · 7 sahne · 04:00 · SAHNE PLANI: 1 3 4 4 3 4 5)
                ├── THE_COUNTED_RIVET_QA_SPEC.md (A·B·C·E blokları · TARGET ASL: 10.0 s flat)
                ├── THE_COUNTED_RIVET_BOLUM_1.md (K01–K12 · 00:00–02:00)
                ├── THE_COUNTED_RIVET_BOLUM_2.md (K13–K24 · 02:00–04:00)
                ├── THE_COUNTED_RIVET_KAPAK.md
                ├── THE_COUNTED_RIVET_MUZIK.md
                └── THE_COUNTED_RIVET_YAYIN_PAKETI.md

BETİK RAPORU    kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/RAPORLAR/
                └── THE_COUNTED_RIVET_20260930_RAPOR_KONTROL.md (Hakem raporu)
```

---

## 📊 İŞLENEN MERCEKLER ÖZET TABLOSU

| Mercek | Mod | Karar | Skor | Öne Çıkan Blocker ve Kritik Bulgular |
| :--- | :--- | :--- | :--- | :--- |
| **① KARE (Görsel & Fizik)** | Mode V | ⛔ **TEKRAR** | — *(düzeltilmiş 8.1)* | **0:05:** Mengene kolunu sıkarken sol eldiven parmakları metalle kaynaşıp eriyor (hand-surface morphing 🟠 Major).<br>**0:21:** Çelik kirişe balyoz darbesi kütle geri tepmesi ve yapısal titreşim taşımıyor (🟠 Major).<br>**0:40:** Arka plan çelik kirişte perçin ızgara dokusu yüzüyor/hizası kayıyor (🟡 Minor).<br>**1:50:** Branda germe halatı rijit silindir gibi bükülmeden hareket ediyor ve metal halka kenarlarından içe geçiyor (grommet clipping 🟠 Major).<br>**2:20:** 15. çekim, 14. çekimin ufak yapay titremeli doğrudan kopyası/tekrarı (🟠 Major).<br>*Not: SPEC dosyası varken mod V koşulduğu için T1 tablosuna satır yazılmaz [D129].* |
| **② DEVAMLILIK (Karakter & Dünya)** | Mode — | ⚠️ **ŞARTLI** | **5.8** | **0:25 vs 0:35:** S3'te kullanılan ağır balyoz (sledgehammer), S4'te birden kerpeten/marangoz çekicine (claw hammer) dönüşüyor (🟠 Major · Kategori 4: 4/10).<br>**0:15 vs 0:35:** S2'de sol kolda olan sarı/okra kol bandı S4'te sağ kola geçiyor; 1:35'te (S10) ise iki kolda birden beliriyor (🟡 Minor · Kategori 2: 4/10).<br>**1:55 vs 2:05:** S12'de puslu turuncu/kehribar olan atmosfer S13'te aniden beyaz bulut denizine sıçrıyor (biyom kayması 🟠 Major · Kategori 9: 4/10).<br>**2:15 vs 2:25:** S15, S14'teki metal cetvel yerleştirme sahnesinin neredeyse birebir tekrar üretimi take'idir (🟡 Minor · Kategori 5: 5/10).<br>**0:15 vs 1:15:** Kontrol konsolu ana taşıyıcı yapıya göre yer değiştiriyor (Kategori 8: 5/10).<br>**1:05 vs 1:45:** Sabit fener direği mafsallı döner kola dönüşüyor (Kategori 10: 5/10). |
| **③ SES (Diyalog & Audio)** | Mode — | ⚠️ **ŞARTLI** | **—** | **0 Replik:** Film State B (tasarımlı diyalogsuz, non-verbal).<br>**SFX & Foley Senkronu (10/10 → —):** 00:21 balyoz, 00:31 pim, 02:07 metal çubuk düşüşü ve 02:51 ağır kilit kapama temasları tam kare senkronunda [D186 uyarınca kusursuz kategori `—` yapıldı].<br>**Ambiyans (10/10 → —):** Yüksek irtifa rüzgâr uğultusu ve mekanik dip ton kesmeler boyunca kesintisiz akar; dijital oda sessizliği düşüşü sıfır.<br>**Respiratör & Nefes:** Kask içi nefes sesleri foley ile dengeli, mikste boğulma yok. |
| **④ HİKAYE (Dramaturji & Kurgu)** | Mode V | ⛔ **TEKRAR** | — *(düzeltilmiş 4.7)* | **0:50–01:50 (S6–S11):** Kaldıraç, mengene ve yürüyüşlerin arka arkaya tekrarlanması dramatik ilerlemeyi duraksatıyor (Structure 4/10, Retention Risk 3/10).<br>**0:00 (S1):** Açılışta doğrudan mengene sıkma eylemine girilmesi risk/tehdit kurmuyor (Hook 5/10).<br>**3:50 (S23):** Görevin başarılı olup olmadığı veya makinenin çalışıp çalışmadığı gösterilmeden kask içi nefeste ani kesilme (Ending 4/10).<br>**Karakter & Seçim (5/10):** Karakter sadece mekanik iş icra eden taşıyıcı olarak algılanıyor.<br>*Not: SPEC varken mod V koşulduğu için T4 tablosuna satır yazılmaz [D129].* |
| **⑤ ARKA PLAN (Derin Tarama)** | Mode — | ✅ **GO** | **6.3** | **00:00–04:04 (24/24 sahne):** Sağ alt köşede 4 kollu sabit AI sparkle/yıldız filigranı (🟠 Major · Kategori 9: 6/10 [D150/D162 · kurguda crop %3-5 gerekir]).<br>**02:00 vs 02:07 (S13):** Arka plan plakası yeşil çelik panel ve kehribar pustan aniden yüksek irtifa Dünya kümülüs bulut denizine atlıyor (🔴 Blocker · Kategori 6: 5/10, Kategori 8: 5/10).<br>**01:00 vs 01:10 (S7 vs S8):** Kehribar ikaz feneri kaidesi güverte zemin direğinden dikey duvar montajına kayıyor (🟠 Major).<br>**00:20 vs 01:20 (S3 vs S9):** Baş üstü çelik kirişin açısal yönelimi ve rotasyonu güverteye göre uyumsuzlaşıyor (🟠 Major · Kategori 4: 7/10).<br>**00:32–00:37 (S4):** Arka plan panel perçin ızgarasında doku yüzmesi (🟡 Minor). |
| **⑥ FİZİK (Ölçüm & Hız)** | Mode V | ⛔ **TEKRAR** | — *(düzeltilmiş 7.6)* | **Two Gravities (D200):** L5'te (00:41) metal küre serbest düşüşü $g \approx 0.33\text{ m/s}^2$ ($0.03\text{ g}$, cinematic float) ölçülürken; L13'te (02:07) düşen metal çubuk $g \approx 4.08\text{ m/s}^2$ ($0.42\text{ g}$); L22'de (03:36) kopan metal parça $g \approx 6.67\text{ m/s}^2$ ($0.68\text{ g}$) ölçülüyor (20 kat yerçekimi dalgalanması 🔴 Blocker · Kategori 1: 3/10).<br>**00:21 (L3) & 03:17 (L20):** 4-5 kg'lık balyoz ve makas darbelerinde kütle geri tepmesi (zero recoil) ve güverte titreşimi sıfır (🟠 Major · Kategori 3: 7/10).<br>**01:52 (L12):** Ağır branda kumaşı bükülmez rijit levha gibi davranıyor (Kategori 4: 8/10).<br>**02:10 vs 02:20 (L14 vs L15):** 15. çekim, 14. çekimin mükerrer üretilmiş ikizidir.<br>*Not: SPEC varken mod V koşulduğu için T6 tablosuna satır yazılmaz [D129].* |
| **⑦ AKSİYON (Koreografi & Vuruş)** | Mode V | ⛔ **TEKRAR** | — *(düzeltilmiş 8.2)* | **02:20–02:30 (B15):** 15. çekim, B14'ü hiçbir durum değişimi veya anlatısal ilerleme olmadan birebir tekrarlıyor (🟠 Major · Beat Anatomy 8/10, Consequence 8/10).<br>**00:40–00:50 (B5):** Havadan düşen ve durup yukarı süzülen metal küre fiziksel bir temas, yaklaşma vektörü veya zemin izi bırakmıyor (🟡 Minor · Threat Vector 7/10).<br>**03:10–03:50 (B20–B23):** Dört ardışık klipte mekanik mandal kilitleme temposunun tekdüze kalması fiziksel gerilimi tırmandırmıyor (Tempo 8/10).<br>*Not: SPEC varken mod V koşulduğu için T7 tablosuna satır yazılmaz [D129].* |
| **⑧ EFOR (Fiziksel Yük & Beden)** | Mode V | ⛔ **TEKRAR** | — *(düzeltilmiş 8.5)* | **The Body Pays (19 Exertion Olayı):** 19 olayın tamamında beden ödemesi (zorlanma ve toparlanma) ekrana yansıtılmıştır (Events with no strain shown: 0).<br>**Maliyet Eğrisi:** `1133334455556667778889998` monotonik tırmanış gösteriyor; S24-S25 arası 9→8 düşüşü hak edilmiş toparlanmadır.<br>**02:10 (E14):** Balyoz ve halat çekişi sonrasında metal cetveli uzatıp tutarken eldiven parmaklarında mikrotremor eksikliği (-2).<br>**02:00 (E13):** Ağır metal çubuğu tek elle yere bırakırken gövdede asimetrik karşı-denge eğimi eksikliği (-2).<br>**03:50–04:05 (E19):** Kask içindeki vizör buğulanma darbelerinin finalde çok hızlı dağılması.<br>*Not: SPEC varken mod V koşulduğu için T8 tablosuna satır yazılmaz [D129].* |
| **⑨ KADRAJ (Kamera & Kompozisyon)** | Mode V | 🚨 **GEÇERSİZ** | — *(düzeltilmiş 7.6)* | **Plan Sadakati Mod V Karantinası [D190]:** SPEC verilmeden koşulduğu için model ekrandan kamera planı uydurmuş; T9 tablosuna girmez.<br>**Rhyme Pair S1 vs S24 (1/10 🔴 Blocker):** S1 (Setup A) ile S24 (Setup T) kafiye kuramıyor; oysa SPEC K01 ↔ K24 arasında aynı Setup B ve ters jest ile birebir kafiye tanımlamıştır.<br>**00:56 (S6):** Konsol planının son 4 saniyesinde kamerada yavaş sürüklenme/creep (Lockoff Integrity 9/10).<br>**Screen Geometry (10/10 → —):** Kusursuz kategori D186 gereği `—` yapıldı. |
| **⑩ OYUNCULUK (Beden & Niyet)** | Mode V | 🚨 **GEÇERSİZ** | — *(düzeltilmiş 5.7)* | **Plan Sadakati Mod V Karantinası [D190]:** SPEC verilmeden koşulduğu için T10 tablosuna satır girmez.<br>**00:00–02:15 (S1, S4, S12, S14):** Görev niyetsiz icra ediliyor; eller aletleri kusursuz kullanıyor fakat eylem öncesi hiçbir tereddüt veya eylem sonrası rahatlama taşımıyor (Pattern ②, Hands as Intent 5/10).<br>**00:00–04:04 (Film Geneli):** Monoton temposuzluk; balyozdan ip bağlamaya dek tüm hareketler yapay tekdüze ritimde ilerliyor (Pattern ⑤, Tempo 5/10).<br>**03:10 (S17):** Sahneler arası beden sıfırlanması; S16'daki yoğun duygusal krizin ardından S17'de karakter o duyguyu hiç yaşamamış gibi nötr duruşla cıvata kesmeye geçiyor (Pattern ⑧, Cost & Aftermath 6/10).<br>**03:05 (S16):** Yüksek dramatik yüz ifadesi önceki ve sonraki tamamen mekanik görev hareketleriyle orantısız kalıyor (Proportion 5/10, The Central Choice 4/10).<br>*Ölçüm sapması: 16 kesme ≠ 23 ölçüm hakemi.* |
| **⑪ IŞIK (Aydınlatma & Atmosfer)** | Mode V | 🚨 **GEÇERSİZ** | — *(düzeltilmiş 6.1)* | **Plan Sadakati Mod V Karantinası [D190]:** SPEC verilmeden koşulduğu için T11 tablosuna satır girmez.<br>**02:00–02:10 (S12→S13→S14):** Arka plan bulut tabakasına geçerken ışık sıcaklığı sarıdan 4500K soğuk beyaza kayıyor, sonra tekrar sarıya dönüyor (🟠 Major Jump · Colour Temperature 5/10).<br>**03:20 (S20→S21):** Sahnede renk doygunluğu aniden düşüyor ve 5000K soğuk gri tona sıçrama oluyor (🟡 Minor Jump).<br>**03:40 (S23):** Toz fırtınası başlangıcında atmosfer pusu ani yoğunlaşıyor (Atmosphere Honesty 6/10).<br>**Gölge & Dolgu (6/10):** S13 ve S21 sahnelerinde gölge yoğunluğu ve dolgu ışık seviyesi dalgalanıyor.<br>**Key Direction (7/10):** S1-S24 boyunca ana ışık yönü (saat 2) istikrarlı tutulmuş. |
| **⑫ HOOK (Kanca & Viral Tutma)** | Mode V | 🚨 **GEÇERSİZ** | — *(düzeltilmiş 5.2)* | **Plan Sadakati Mod V Karantinası [D190]:** SPEC verilmeden koşulduğu için T12 tablosuna satır girmez.<br>**00:00–00:10 (Hook Question 2/10):** İlk 10 saniyede yalnızca mekanik hazırlık gösteriliyor, hiçbir merak ögesi veya risk oluşmuyor (NO QUESTION · Drop-off: 00:06).<br>**00:30–02:50 (Plateau 3/10):** Art arda gelen benzer tempo ve ölçekteki mekanik eylemler monotonluk yaratıyor (Drop-off: 01:25).<br>**03:58–04:05 (Exit & Return 2/10):** 04:00'daki başlık kartı izleyicinin filmi tekrar izleme (loop) isteğini yok ediyor ve döngüyü kırıyor (Drop-off: 03:58).<br>**03:05 (Cover Second 8/10):** Kask içindeki endişeli yüz yakın planı metinsiz ve odaklı güçlü bir kapak görüntüsü sunuyor.<br>**00:20 & 03:00 & 03:40:** Bağımsız durabilen 3 paylaşım anı (Share Moments Stand Alone 8/10). |
| **⑬ UYUM (Metin & Model Sadakati)** | Mode MISSING | ✂️ **KESİK** | — | **Sahne Promptları Sağlanmadı:** Bu mercek jeneratöre gönderilen metin ile ekrandaki görüntüyü karşılaştırır; prompt veya bölüm dosyası verilmediği için koşulamadı.<br>*Not: Kesik koşu tabloya girmez, partiyi düşürmez, yeniden koşulmalıdır.* |
| **⑭ HAREKET (Beden Mantığı & Amaç)** | Mode V | ⛔ **TEKRAR** | — *(düzeltilmiş 7.6)* | **0:30–0:40 (M4):** Çekiç bırakıldıktan sonra eller yüzey üzerinde pandomim yapar gibi amaçsızca geziniyor (🟡 Minor · Pattern ⑫ The Mime · Purpose Legibility 7/10, Object Handling 7/10).<br>**1:00–1:10 (M7):** Kontrol panelinden ayrılıp arkasındaki boşluğa doğru nedensiz 180° gövde dönüşü (🔴 Blocker · Pattern ④ The Causeless Turn · Turn & Rotation Logic 6/10).<br>**1:30–1:40 (M10):** El korkuluktan kalkıp havada kararsızca duruyor (🟡 Minor · Pattern ② The Idle Loop).<br>**2:10–2:30 (M14–M15):** Metal cetveli sabitlemeden kubbe üzerinde ileri geri kaydırma ve birebir tekrar üretimi döngüsü (🟠 Major · Pattern ② / ⑫ · Loop & Repetition 6/10).<br>*Not: SPEC varken mod V koşulduğu için T14 tablosuna satır yazılmaz [D129].* |
| **⑮ YÖN (Hedef & Vektörler)** | Mode V | ⛔ **TEKRAR** | — *(düzeltilmiş —)* | **24 HIT / 0 MISS (Every Vector Lands):** 24 eylemin tamamında hedef kurulmuş ve uzanılan nesneye tam isabet sağlanmıştır (Acts Missed: 0 · Vector String: 24×H).<br>**Kusursuz Kategori D186:** 8 kategorinin tamamı (Target Establishment, Look Direction, Turn & Travel, Reach & Aim, Fire/Trigger, Screen Direction, Camera-Relative, Consequence) 10/10 kusursuz puanlandığı ve kesinti olmadığı için D186 uyarınca `—` yapılmıştır.<br>*Not: SPEC varken mod V koşulduğu için T15 tablosuna satır yazılmaz [D129].* |

---

## 🔍 FLAGS FOR DOCUMENT CHECK — BELGE KONTROLÜ VE CEVAPLAR

1. **① KARE — 10.0 s Sabit Kadans Sorusu:**
   - **Gözlem / Soru:** *23 compilation cuts counted at exact 10.0 s intervals — Does the edit plan specify a strict 10-second shot cadence for the sequence?*
   - **Cevap:** **EVET, BİLİNÇLİ TASARIM.** `THE_COUNTED_RIVET_QA_SPEC.md` B Bloğu KURGU GEOMETRİSİ: `TARGET ASL BAND: 10,0 s · ASL CURVE: NONE — flat grid · GRID: klip(n) başlangıcı = (n-1) × 10,0 s · RUNTIME: 240,0 s`. Gerekçe: Film bir ölçüm işidir ve ritim makinenin sabit periyoduna karşı kurulur; hızlanma kurgudan değil sayaçtan (perçin aralıkları 40 → 25 → 18 s) gelir [D74].

2. **② DEVAMLILIK — Kol Bandı Hangi Kolda Olmalı?**
   - **Gözlem / Soru:** *Armband switches sleeves across scenes — Which arm is the official armband designated for in the design bible?*
   - **Cevap:** **SOL KOL.** `THE_COUNTED_RIVET_QA_SPEC.md` C Bloğu KİMLİK DİZİSİ: `renk bandı: okra, SOL pazu ve SOL uylukta 360° sarılı`. S4'te sağ kola geçmesi ve S10'da çift kol bandı belirmesi modelin görüntü üretimindeki devamlılık zaafıdır (generator drift).

3. **② DEVAMLILIK — S13 Bulut Denizi Sıçraması Tasarım mı Hata mı?**
   - **Gözlem / Soru:** *Sky jumps to cloud deck in S13 — Is S13 an intended altitude shift or a prompt deviation?*
   - **Cevap:** **PROMPT SAPMASI (HATA).** `THE_COUNTED_RIVET_QA_SPEC.md` C Bloğu DÜNYA ÇAPASI / ATMOSFER: `ufuk YOK · zemin YOK · üstte kaynaksız parlak okra kubbe, güneş diski 0 · aşağıda okra derinlik`. S13'teki beyaz bulut denizi ortam kartına (§3.6 Sürekli Bulut / Nötr Yüzerlik) tamamen aykırıdır; modelin alışıldık uçak/bulut stereotipini halüsinasyon olarak üretmesidir.

4. **③ SES — Filmin Tamamen Repliksiz Oluşu Tasarım mı?**
   - **Gözlem / Soru:** *Fully non-verbal soundtrack (Foley / ambience / breathing only) — Confirm whether film was intended to be non-verbal or if dialogue tracks were omitted in master export.*
   - **Cevap:** **BİLİNÇLİ TASARIM.** `THE_COUNTED_RIVET_QA_SPEC.md` A Bloğu: `DIALOGUE LINES: 0 · register: HUMAN 0 / MACHINE 0 · No dialogue. her AUDIO satırında`. Muhatap konuşmaz; otomasyon sabit periyotlu kehribar lambayla yanıt verir. Film baştan sona repliksiz tasarlanmıştır.

5. **④ HİKAYE — 0:10–1:50 Arası Mekanik Rutin Döngüsü Tasarım mı Kurgu Hatası mı?**
   - **Gözlem / Soru:** *Is the repetitive maintenance loop from 0:10 to 1:50 intended as a thematic Sisyphean montage, or was a specific mechanical failure beat omitted in edit?*
   - **Cevap:** **BİLİNÇLİ TASARIM.** `THE_COUNTED_RIVET_QA_SPEC.md` A Bloğu TEMA: `HUMAN AND MACHINE — a machine can only see magnitudes its catalogue has a name for; a human chooses to measure one it has no name for, and pays for it`. B Bloğu: İlk yarıdaki 10'ar saniyelik mekanik rutin, makinenin değişmez sabit kataloğunu kurar. Karakter K12'de (1:50–2:00 / orta nokta) makinenin kaydına karşı kendi ölçüsüne yönelir. Kurguda atlanan bir arıza planı yoktur.

6. **④ HİKAYE — S23 Finalinde Bir Makine Aktivasyonu / Zafer Göstergesi Bekleniyor mu?**
   - **Gözlem / Soru:** *Does the plan call for a resolved system activation at the end of S23? — because the edit cuts to black on an exhale without showing machine status.*
   - **Cevap:** **HAYIR, AÇIK / ÖDENEN BEDEL FİNALİ.** `THE_COUNTED_RIVET_QA_SPEC.md` A Bloğu ENDING TYPE: `OPEN / COST PAID — she is right, the surface has no edge, and the platform is going down with her on it`. INTENDED EMOTION: `being proved right and paying for it in the same breath (vindication + cost of vindication)`. Yeşil ışık ya da sistem zaferi tasarlanmamıştır; haklı çıkışın bedeli platformun alçalması ve yalnızlıktır.

7. **⑤ ARKA PLAN — S13'te Atmosferik Yükseliş / Bulut Katmanı Geçişi Var mı?**
   - **Gözlem / Soru:** *Does the script specify an atmospheric balloon ascension or high-altitude transition during Scene 13?*
   - **Cevap:** **HAYIR, PROMPT SAPMASI.** Film boyunca platform 55 km nötr yüzerlik bandında sabittir (dikey irtifa değişimi yok). 02:07'de beliren Dünya tipi kümülüs bulut denizi model halüsinasyonudur; okra pus kubbesi korunmalıdır.

8. **⑤ ARKA PLAN — Birden Fazla Fener mi Tek Hareketli Lamba mı?**
   - **Gözlem / Soru:** *Is the structure equipped with multiple amber beacons or a single moveable lamp?*
   - **Cevap:** **TEK OTOMASYON LAMBASI.** SPEC C Bloğu: `Muhatap KONUŞMAZ: bağlama otomasyonu sabit periyotlu (4,0 s) tek kehribar lamba ile cevap verir`. Fener direğinin yer değiştirmesi veya döner kola dönüşmesi modelin nesne sürekliliği zaafıdır.

9. **⑥ FİZİK — S5'teki Metal Kürenin Süzülmesi Düşük Yerçekimi Ayarı mı?**
   - **Gözlem / Soru:** *Sphere drift in Shot 5 (00:41) implies g ≈ 0.33 m/s² — Does the production plan specify a low-gravity planetary setting or zero-g drift effect?*
   - **Cevap:** **HAYIR, PLANLANAN YERÇEKİMİ 0.904 g SABİTTİR.** SPEC C Bloğu YERÇEKİMİ: `0,904 g — 24/24 promptta AYNI sayı, tek değer [D200]. Bırakılan nesne: eldiven boyu ≈ 0,33 s`. S5'teki kürenin 2.2 saniyede 0.8 metre süzülmesi modelin sinematik float/ağır çekim hatasıdır; Two Gravities kusurudur [D200].

10. **⑦ AKSİYON & ⑨ KADRAJ — S14 vs S15 İkiz Çekimi Tasarım mı Hata mı?**
    - **Gözlem / Soru:** *Was Scene 15 intended as a multi-stage hatch clamping sequence, or is it an AI video generation loop artifact?*
    - **Cevap:** **AI ÜRETİM ARTEFAKTI (HATA).** `THE_COUNTED_RIVET_QA_SPEC.md` B Bloğu KURULUM İSKELETİ: `K14 F (MS/ots) · K15 H (CU profil)`. İki klip farklı açılardır; K15'te şerit perçin kubbesine yatırılmalı ve novum kanıtı gösterilmelidir. Ekranda K15'in K14'teki cetvel tutuşunu üst açıdan tekrarlaması modelin mükerrer üretim döngüsüdür (duplicate loop).

11. **⑦ AKSİYON — S5'teki Metalik Küre Tasarımda Var mı?**
    - **Gözlem / Soru:** *Is the metallic sphere in Scene 5 a deliberate low-gravity/buoyant anomaly or an accidental generator physics glitch?*
    - **Cevap:** **MODEL HALÜSİNASYONU (FİZİK İHLALİ).** SPEC C Bloğu: `NOVUM: İHLAL SAYISI: 1 (mandal çenesi kavis yapmaz, yüzey düzdür) · YERÇEKİMİ: 0,904 g tek değer · ANOMALİ/UZAYLI/YÜZEN KÜRE: 0 kare`. SPEC'te havada duran veya yukarı seken gizemli metal küre yoktur; model bilimkurgu klişesi olarak uzayda yüzen küre uydurmuştur.

12. **⑨ KADRAJ — S1 vs S24 Kapanış Kafiyesi Planlandı mı?**
    - **Gözlem / Soru:** *Was a closing camera rhyme explicitly requested to mirror S1 in S24?*
    - **Cevap:** **EVET, BİREBİR KAFİYE ÇİFTİDİR.** SPEC B Bloğu DÖNGÜ KANITI: `K01 (0,0–10,0 s) ↔ K24 (230,0–240,0 s): aynı kurulum harfi (B) · aynı ölçek (CU) · aynı iki eldiven · aynı mandal çenesi · TERS jest (kapatır ↔ kesilmiş) · Kamera cümlesi BİREBİR aynı`. Raporun S24'te Setup T okuması modelin kurulum harfinden sapmasıdır.

13. **⑩ OYUNCULUK — S5 Küre ile S15 Ufuk Bakışı Hikaye Bağlantısı:**
    - **Gözlem / Soru:** *S5'te yukarıdaki küreye bakış ile S15'teki ufka bakış arasındaki hikaye bağlantısı belirtilmiş mi?*
    - **Cevap:** **HAYIR, İKİSİ ARASINDA HİKAYE BAĞLANTISI YOKTUR.** S5'teki yüzen küre SPEC'te bulunmayan, tamamen yetkisiz bir AI generator halüsinasyonudur (SPEC C Bloğu: `ANOMALİ/UZAYLI/YÜZEN KÜRE: 0 kare`). S15 ise K15 novum kanıtı (şeridin kubbe perçin yüzeyine yatırılması ve yüzeyin kavis yapmadığının tespiti) adımıdır. İki an arasında senaryoda hiçbir organik veya tematik bağ tasarlanmamıştır.

14. **⑩ OYUNCULUK — S16'daki Panik / Duygu Patlamasının Tetikleyicisi:**
    - **Gözlem / Soru:** *Karakterin S16'daki ani panik/duygu patlamasının senaryodaki tetikleyici olayı nedir?*
    - **Cevap:** **NOVUMUN KANITLANMASI VE BEDELİN ANLAŞILMASI (HAKLILIK + BEDEL).** Karakter K14–K15'te yüzeyin eğri olmadığını, bağlandıkları devasa yapının ucu bucağı olmayan sonsuz bir plaka olduğunu kanıtlamıştır. Karakterin S16'daki (03:00) yüz ifadesi, haklı çıkış (vindication) ile birlikte platformun alçaldığını ve kendisinin bu yapıyla birlikte batacağını idrak etmenin eşzamanlı çifte duygusudur (`THE_COUNTED_RIVET_QA_SPEC.md` A Bloğu INTENDED EMOTION: `being proved right and paying for it in the same breath (vindication + the cost of vindication)`).

15. **⑪ IŞIK — S13 Bulutlu Ortam Bilinçli Bölge (Zone) Değişikliği mi?**
    - **Gözlem / Soru:** *S13'teki bulutlu atmosferik ortam bilerek planlanmış bir bölge (zone) değişikliği midir?*
    - **Cevap:** **HAYIR, PROMPT SAPMASIDIR (TEK BÖLGE / ZONE 1).** `THE_COUNTED_RIVET_QA_SPEC.md` C Bloğu DÜNYA ÇAPASI ve ATMOSFER: `55 km bandı · nötr yüzerlik · ufuk YOK · zemin YOK · üstte kaynaksız parlak okra kubbe, güneş diski 0 · aşağıda okra derinlik`. Film 24 klip boyunca tek bir bölgede (Zone 1) geçer. S13'teki Dünya tipi beyaz bulut katmanı ve 4500K soğuk ışık sıçraması modelin biyom kaymasıdır.

16. **⑪ IŞIK — S23 Toz Fırtınası Tasarlanmış Atmosferik Değişim mi?**
    - **Gözlem / Soru:** *S23'teki toz fırtınası atmosferik değişim noktası olarak mı kurgulanmıştır?*
    - **Cevap:** **HAYIR, PROMPT SAPMASIDIR.** SPEC C Bloğu ATMOSFER: `bağıl rüzgâr 0 → kumaş kıpırdamaz, hiçbir şey savrulmaz · toz 0`. Yoğun toz fırtınası ortam kartına (§3.6) ve SPEC'e doğrudan aykırıdır; modelin bilimkurgu çöl stereotipini halüsinasyon olarak sahneye eklemesidir.

17. **⑫ HOOK — Planlanan Kanca, Kapak Karesi ve Paylaşım Anları Beyanı:**
    - **Gözlem / Soru:** *Mod V değerlendirmesi yapılmıştır (SPEC dokümanı sunulmamıştır). Planlanan kanca süresi, hedeflenen kapak karesi ve paylaşım anları için SPEC belgesi beyan edilmelidir.*
    - **Cevap:** **SPEC'TE TANIMLANMIŞTIR.**
      - *Kanca (Hook):* K01 (0,0–10,0 s), mandal çenesinin kapanması ve altındaki yüzeyin kavis yapmaması (görev kancası K01). Kırpma bütçesi 0 saniyedir (sabit 10.0 s ızgara içi).
      - *Kapak Karesi:* K19 (03:00–03:10 aralığı, D kurulumu · 85mm · ECU · kask içi yüz yakın planı). Raporda 03:05 karesi Cover Second olarak doğrulanmıştır (8/10).
      - *Paylaşım Anları:* SPEC A Bloğu: `VIRAL INTERSTITIALS: 0 — kartın dört adedinden SAPMA [D74]`. Bu endüstriyel ölçüm ve Sisifos temposunda bağımsız viral ara kesmeler tasarlanmamıştır; raporda değerlendirilen 3 sahne filmin kendi dramatik omurgasının parçalarıdır. 04:00'daki başlık kartı ise SPEC E4 kapısına aykırı bir ihraç kusurudur.

18. **⑭ HAREKET — 0:30'da Çekiç Bırakıldıktan Sonraki El Hareketi Tasarım mı?**
    - **Gözlem / Soru:** *Eller çekiç bırakıldıktan sonra amaçsızca geziniyor — Planlanan sekans klemens üzerinde ince bir ayarlama adımı içeriyor mu?*
    - **Cevap:** **BİLİNÇLİ ALIŞKANLIK KİLİDİ (MODEL SÜZÜLMESİ / OVERGESTURE).** `THE_COUNTED_RIVET_BOLUM_1.md` K04 promptu ve SPEC C Bloğu: `ALIŞKANLIK: mandalı kapatmadan önce çeneyi iki parmakla iki kez yoklamak (S2 · S3 · S6) · K04 TIMELINE: Both gloves come either side of the open jaw and stop a finger-width off the metal`. Plandaki eylem mandalı kavramadan önceki ölçüm yoklamasıdır; model parmakları sabit tutamayıp yüzeyde pandomim gibi gezdirerek saptırmıştır.

19. **⑭ HAREKET — 1:00'deki 180° Dönüşün Senaryoda Bir Tetikleyicisi Var mı?**
    - **Gözlem / Soru:** *Astronot arkasındaki boşluğa dönüyor — Senaryoda kadraj dışı bir ses veya görsel uyaran tanımlanmış mı?*
    - **Cevap:** **HAYIR, MODEL HALÜSİNASYONUDUR (PATTERN ④ THE CAUSELESS TURN).** `THE_COUNTED_RIVET_BOLUM_1.md` K07 TIMELINE: `The automation arm keeps re-tensioning the clamp on its own schedule while she keeps standing where she is... she does not move, and her shoulders rise once with a breath`. Senaryoda kadraj dışı ses veya görsel uyaran yoktur; karakterin sabit durması planlanmışken model sebepsiz 180° dönüş uydurmuştur.

20. **⑭ HAREKET — 2:10'daki Metal Cetvel Bir Yuvaya mı Takılmalı Yoksa Bırakılmalı mı?**
    - **Gözlem / Soru:** *Metal cetvel kubbe camı üzerinde kaydırılıyor — Bu alet bir yuvaya mı takılmalı yoksa yüzeye mi bırakılmalı?*
    - **Cevap:** **YÜZEYE YATIRILMALI (NOVUM KANITI / DÜZ ÇELİK ŞERİT).** `THE_COUNTED_RIVET_BOLUM_2.md` K14–K15 ve SPEC C Bloğu NOVUM TAŞIYICISI: Alet bir takma pimi değil, kol boyunda düz kenarlı bir çelik şerittir (batten). Önce perçin kubbesine yatırılıp iki uçtan ışık sızdığı (alet çalışıyor), ardından plaka yüzeyine yatırılıp hiçbir yerden ışık sızmadığı (yüzey düz) gösterilir. Modelin cetveli sabitlemeden kaydırması fiziksel temas tutarsızlığıdır (Pattern ② / ⑫).

---

## 🔁 DERS DÖNÜŞÜ

**TEKRAR:** D129 · D134 · D186 · D208 · D207 · D146 · D150 · D162 · D200 · D135 · D190 · D184 · D166 · D107 — sayaç +1
- **D129 (Mod V vs SPEC Çakışması):** `THE_COUNTED_RIVET_QA_SPEC.md` depoda hazır bulunmasına rağmen ① KARE, ④ HİKAYE, ⑥ FİZİK, ⑦ AKSİYON, ⑧ EFOR, ⑭ HAREKET ve ⑮ YÖN raporları Mod V (Video-only) olarak gelmiştir. Bu yedi koşu ⛔ TEKRAR sayılır; T tablosuna yazılmaz, kurgu kesme listesi işletilmez.
- **D190 / D184 (Plan Sadakati Mod V Karantinası — ⑨ KADRAJ, ⑩ OYUNCULUK, ⑪ IŞIK, ⑫ HOOK):** Plan sadakati mercekleri SPEC verilmeden Mod V koşulduklarında ekrandan plan uydurur ve kusuru niyet sanıp puanlarlar. Bu dört rapor karantinaya alınmıştır (🚨 GEÇERSİZ); T9-T12 tablolarına girmez, sipariş veya kurgu reçetesi üretemez.
- **D107 (Kesme Yayılımı ve Ölçüm Hakemliği):** ⑦ AKSİYON (22 kesme), ⑧ EFOR (24 kesme) ve ⑩ OYUNCULUK (16 kesme) saptığı için kesme yayılımı ölçüm hakemliğiyle çözülmüş; `--olcum-kesme 23` ile diğer 10 merceğin çoğunluğu (23 kesme) doğrulanarak parti ayakta tutulmuştur.
- **D150 / D162 (Filigran & Suskunluk):** ⑤ ARKA PLAN merceği 24/24 sahnede sağ alt köşede ✦ AI filigranı tespit etmiştir (D150). Sahibi ① KARE bu bulguda susmuştur (D162 suskunluk kapısı tetiklendi). Kurguda %3-5 alt kenar kırpması (crop) zorunludur.
- **D200 (Two Gravities — Çift Yerçekimi):** ⑥ FİZİK merceğinde serbest düşüş ivmesi S5'te $0.33\text{ m/s}^2$ iken S13'te $4.08\text{ m/s}^2$ ve S22'de $6.67\text{ m/s}^2$ ölçülmüş; tek film içinde 20 kata varan yerçekimi tutarsızlığı kaydedilmiştir.
- **D166 (Premise Register Kuralı):** ⑦ AKSİYON ve ⑧ EFOR raporlarının Premise Register bloğunda filmin novum kuralı yazılmamış, yalnız fiziksel ortam listelenmiştir.
- **D135 (Şerit Sapması):** ④ HİKAYE (23), ⑦ AKSİYON (23), ⑧ EFOR (25), ⑩ OYUNCULUK (17), ⑫ HOOK (23) ve ⑭ HAREKET (23) insan varlık şeridinde sapmış; 7 merceğin çoğunluğu (24 hane `1`) planı doğrulamıştır.
- **D134 (Sayaç / Counter Logic Ölçüm Boşluğu):** ② DEVAMLILIK raporunda `Counter Logic` N/A olarak işaretlenmiştir; oysa SPEC açıkça 3 adet monotonik metinsiz sayaç (Kanıt Merdiveni, İniş Hızı, Işık Takvimi) tanımlamıştır. Bu durum bir yokluk değil, ölçüm boşluğudur; kilit defterine ⬜ AÇIK olarak işlenmiştir.
- **D186 (Kusursuz Kategori Skoru & Kaynaksız Kesinti):** ③ SES raporunda 3 kusursuz kategori, ⑨ KADRAJ raporunda Screen Geometry ve ⑮ YÖN raporunda 8 kategorinin tamamı 10/10'dan `—` yapılmıştır. ⑪ IŞIK (In-Clip Stability 7/10) ve ⑫ HOOK (Format Fit 9/10) kesintilerinin kaynağı zaman kodu veya satırla listelenmediği için bu kategoriler D186 kural ④ uyarınca şartlıdır.
- **D208 (Ekipman ve Hasar Sürekliliği):** S3'te kullanılan ağır balyozun S4'te kerpeten/çekice dönüşmesi ve okra kol bandının sol koldan sağ kola atlaması D208 ekipman hafızası ihlalidir.
- **D207 (Sürekli Eylem & Mükerrer Çekim):** S14 ve S15 çekimlerinde cetvel yerleştirme jestinin ufak bir kamera titreşimiyle iki kez art arda üretilmesi (duplicate take) çok klipli sahne rejiminde kurgu fazlalığı olarak tespit edilmiştir.
- **D146 (Referans Paketi Eksikliği):** Referans paketi yazılmadığı için astronotun giysisi (yeşilimsi kapitone yerine kurşun gri olması gerekirken) ve kol bandı kararsızlık göstermiştir.

**PROMPT İYİLEŞTİRME VE DÜZELTME NOTLARI:**
- **Halat Bükülmesi (1:50):** Video promptuna `flexible heavy lacing cord with natural slack, physical sag, and bending through metal eyelets` eklenmeli.
- **Balyoz Kütle Tepkisi (0:21):** Video promptuna `heavy sledgehammer strike with realistic inertial recoil, vibration through metal platform, and micro-sparks on contact` eklenmeli.
- **Atmosfer Sapması (S13 & S23):** S13 promptundaki gökyüzü tanımı SPEC C Bloğundaki okra kubbe tanımına kilitlenmeli, bulut denizi kaldırılmalı; S23'teki savrulan toz fırtınası temizlenip `clear ochre atmosphere, zero dust, zero wind` kuralı yazılmalı.
- **Yerçekimi Sabitliği (S5):** Küre süzülüşünde `drifting at constant low gravity` yerine `descends at steady 0.9g with realistic downward momentum` kuralı korunmalı.
- **Hassas Ölçüm Mikrotremoru (S14):** Video promptuna `fine muscle tremor in gloved fingers while holding rigid metal gauge against curved hull` eklenmeli.
- **Oyunculuk & Tereddüt (S1, S4, S12):** Mekanik el eylemlerine dokunmadan önce `brief 0.5-second hesitation before gripping tools, showing intentional sensory contact` eklenmeli.
- **Amaçsız Dönüşün Engellenmesi (S7 · 1:00):** Promptta `the astronaut remains facing the control console throughout the shot without turning around` kuralı açıkça yazılmalı.

**ADAY:** YOK — ham raporlarda belirtildiği üzere tüm hatalar bilinen desenlere (Desen 2, 4, 5, 6, 7) uymaktadır.

---

## 🎯 ÜÇ SATIRLIK SONUÇ

```
1. FİLM: THE_COUNTED_RIVET 4 dakikalık filminin 15 merceğinin tamamı (①-⑮) işlendi; 24 klip × 10.0 s sabit kurgu ızgarası, 19 efor olayında eksiksiz beden maliyeti (The Body Pays, Efor 8.5), sıfır yön hatası (Every Vector Lands, 24 HIT) ve saat 2 ana ışık yönü korunurken; 24/24 sahnede sağ alt köşe ✦ filigranı (D150), S13 bulut denizi ve S23 toz fırtınası biyom sapmaları, S14↔S15 mükerrer çekim döngüsü, Two Gravities (D200), 1:00 nedensiz 180° dönüşü ve 04:00 başlık kartı kurgu ve prompt revizyon defterine işlendi.
2. QA: ① KARE (8.1), ④ HİKAYE (4.7), ⑥ FİZİK (7.6), ⑦ AKSİYON (8.2), ⑧ EFOR (8.5), ⑭ HAREKET (7.6) ve ⑮ YÖN (—) SPEC mevcudiyetine rağmen Mod V koşulduğu için ⛔ TEKRAR [D129]; ⑨ KADRAJ (7.6), ⑩ OYUNCULUK (5.7), ⑪ IŞIK (6.1) ve ⑫ HOOK (5.2) plan sadakati mercekleri belgesiz koşulduğu için 🚨 GEÇERSİZ [D190/D184]; ② DEVAMLILIK 5.8 ⚠️ ŞARTLI (T2), ③ SES — ⚠️ ŞARTLI (T3) ve ⑤ ARKA PLAN 6.3 ✅ GO (T5) tablolara tescillendi; ⑬ UYUM promptsuz koşulduğu için ✂️ KESİK sayıldı; kesme yayılımı --olcum-kesme 23 hakemliğiyle çözüldü; tamlık matrisi 0/4 seviyesindedir.
3. DERS: D129 ve D190 disipliniyle Mod V kurgu kesme reçeteleri bloke edilmiş; D107 kesme yayılımı master ızgarasıyla aşılmış; D150 filigranı ve D162 suskunluğu tespit edilmiş; D200 fizik tutarsızlığı, D208 ekipman hafızası ve D186 kaynaksız kesinti kuralları tescil edilmiştir.
```
