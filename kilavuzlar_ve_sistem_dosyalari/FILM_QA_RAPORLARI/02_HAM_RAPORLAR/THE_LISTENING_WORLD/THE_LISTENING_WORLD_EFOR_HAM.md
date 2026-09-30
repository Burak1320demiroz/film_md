INPUT MODE: D
FILM: THE_LISTENING_WORLD
RUNTIME: 02:40 measured (160,0 s · 02:40–02:45 jenerik kartı hariç)
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 16 · CUTS COUNTED: 15
NON-SCENE MATERIAL: 02:40–02:45 (Başlık / afiş kartı)
PRESENCE STRING: 111111111111111-
LINES HEARD: 1 · 02:25 (S14 4.0s): "Hello." — ortam sentezör ses yatağı ve dip ton mevcut
EXERTION EVENTS: 9
EVENTS WITH NO STRAIN SHOWN: 9
BODY: suited human — belgeselden (PREMISE REGISTER)
PREMISE REGISTER:
· yerçekimi / ortam: 0,12g (1,18 m/s²), sert vakum (0 kPa, %100 havasız)
· bedenin giydiği: Basınçlı EVA uzay giysisi, kalın eldivenler, entegre kask, sırt ünitesi düz siluet
· beyan edilen kapasite: Saha araştırmacısı / astronot
· beyan edilen limitler: Oksijen sınırı, kriyojenik aşırı soğuk ortam
· beden insan mı?: Giysili insan

---

## EFFORT LEDGER

| E# | in–out | task | load / resistance | duration | STRAIN SHOWN | RECOVERY SHOWN | debt after (0–9) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 00:00–00:10 | S0: Uçurum kenarında giysi içinde dikilme | Giysi kütlesi (~100kg+ Dünya / ~12kg Niva) | 10,0 s | none | none | 0 |
| E2 | 00:10–00:20 | S1: Telemetri cihazını buza bastırma / tutma | İnce motor direnci, basınçlı eldiven | 10,0 s | none | none | 1 |
| E3 | 00:20–00:30 | S2: Diz çöküp telemetri kutusu kadranlarını ayarlama | Eklemleri bükme, kalın eldivenle hassas ayar | 10,0 s | none | none | 1 |
| E4 | 00:30–00:40 | S3: İniş aracı rampasından yukarı yürüme | 0,12g yerçekiminde giysi içinde yokuş tırmanma | 10,0 s | none | none | 1 |
| E5 | 00:50–01:00 | S5: Buz üzerindeki kutu düğmelerini kumanda etme | İnce motor işi | 10,0 s | none | none | 1 |
| E6 | 01:20–01:30 | S8: Buz tabakasına avuç içiyle basma / diz çökme | Torso bükülmesi, dize yük binmesi | 10,0 s | none | none | 1 |
| E7 | 01:30–01:40 | S9: Bataryası biten cihazın yanında diz üstü bekleme | Statik duruş, efor sonrası bekleme | 10,0 s | none | none | 2 |
| E8 | 01:50–02:00 | S11: Eğilerek elini buza doğru uzatma | Basınçlı giysi kolunu öne esnetme | 10,0 s | none | none | 1 |
| E9 | 02:00–02:10 | S12: Uçurum kenarında ayakta biyolüminesans dalgasını izleme | Giysi içinde statik duruş | 10,0 s | none | none | 1 |

> **Bill Test Cümleleri:**
> * E1: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; omuzlar düşmedi, duruş esnemedi.*
> * E2: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; eldiven eklemlerinde sertleşme veya bilek direnci görülmedi.*
> * E3: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; diz çökme veya kadran çevirme sonrası parmaklarda titreme olmadı.*
> * E4: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; rampayı tırmandıktan sonra adımlar yavaşlamadı veya soluk yükselmedi.*
> * E5: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; ince motor hareketi çırpımsız ve zahmetsizce tamamlandı.*
> * E6: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; buza temas eden kol ve omuz gerilmedi.*
> * E7: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; batarya bitişinde beden çökmedi, duruş bozulmadı.*
> * E8: Çalışma sonrası bu bedende ne değişti? *Hiçbir thing; kol uzatılırken giysi dikişlerinde direnç oluşmadı.*
> * E9: Çalışma sonrası bu bedende ne değişti? *Hiçbir şey; başlangıçtaki ilk kareyle tamamen aynı taze beden duruşu korundu.*

---

## PRESENCE STRING

```
111111111111111-
```

---

## COST CURVE

```
0111010012111110
```

---

## RESET LOG

| Between | Curve fell | Recovery shown? | Time elapsed? | Verdict |
| --- | --- | --- | --- | --- |
| S3–S4 | 1 → 0 | No | No | UNEARNED |
| S5–S6 | 1 → 0 | No | No | UNEARNED |
| S9–S10 | 2 → 1 | No | No | UNEARNED |
| S14–S15 | 1 → 0 | No | Yes (yörünge kadrajına kesme) | EARNED |

---

## EFFORT LOCK VERIFICATION — MODE D ONLY

| Declared exertion | Found at | Strain shown | Verdict |
| --- | --- | --- | --- |
| Telemetri cihazını buza yerleştirme ve çalıştırma (S1, S3, S5) | 00:10, 00:20, 00:50 | none | FAIL |
| İniş aracı rampasından tırmanış (S3) | 00:30 | none | FAIL |
| Kriyojenik buza elle temas ve duruş koruma (S8, S9) | 01:20, 01:30 | none | FAIL |

---

## SCORES SUMMARY

| # | Category | Score | Issue (with ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Strain During the Work | 2/10 | -8 · E1 (00:00), E2 (00:10), E3 (00:20), E4 (00:30), E5 (00:50), E6 (01:20), E7 (01:30), E8 (01:50) kas gerilimi ve direnç göstermiyor |
| 2 | Breath & Recovery | 1/10 | -9 · Hiçbir efor olayında (E1–E9) göğüs kalkışı, siperlik buğulanması veya görünür nefes ritmi değişimi yok |
| 3 | Fatigue Accumulation | 2/10 | -8 · S0'dan (00:00) S14'e (02:20) kadar hareket hızında veya beden formunda hiçbir birikimli yorulma gözlenmiyor |
| 4 | Load in the Body | 3/10 | -7 · Telemetri kutusu kütlesi ve giysi ağırlığı yürüme ve eğilmede duruş değişikliği yaratmıyor (E2, E3, E4) |
| 5 | Injury Persistence & Cost | — | Yaralanma beyan edilmedi ve filmde yer almadı |
| 6 | Grip & the Price of Holding On | 2/10 | -8 · E2 (00:10), E3 (00:20), E5 (00:50) sahnelerinde kalın uzay eldivenleriyle sıfır titreme ve sıfır dirençle hassas ayar yapılıyor |
| 7 | Equipment Burden | 2/10 | -8 · Ağır basınçlı EVA giysisi ve eldivenler tüm sahnelerde ağırlıksız kumaş gibi davranıyor |
| 8 | Pain, Restraint and Proportion | — | Acı / ağrı reaksiyonu gerektiren olay gerçekleşmedi |
| 9 | Recovery Curve Honesty | 2/10 | -8 · S3–S4, S5–S6 ve S9–S10 arasında toparlanma gösterilmeden maliyet eğrisinde hak edilmemiş düşüşler var |

VERDICT: NOBODY PAYS

---

## UNPAID WORK TABLE

| Timecode | The work | What should have shown | Which pattern (①–⑭) | Severity |
| --- | --- | --- | --- | --- |
| 00:10–00:20 | Baza cihaz bastırma | Eldiven dikişlerinde sertlik, ön kol gerilimi, direnç | ⑥, ⑬ | 🔴 |
| 00:20–00:30 | Diz çöküp kadran ayarlama | Giysi eklem direnci, gövde ağırlık transferi | ①, ⑥ | 🔴 |
| 00:30–00:40 | İniş rampasını tırmanma | Eylemsizlik momenti, ağır adım basma, giysi hantallığı | ①, ⑥ | 🔴 |
| 00:50–01:00 | Telemetri düğmelerini çevirme | Eldiven kıvrım gerilimi, parmak zorlanması, efor titremesi | ⑥, ⑬ | 🔴 |
| 01:20–01:30 | Buza avuç içiyle basma | Omuz desteklemesi, gövde ağırlığını kola bindirme | ①, ⑥ | 🔴 |
| 01:30–01:40 | Batarya bitişinde diz üstü bekleme | Duruş çökmesi, omuz düşmesi, kask içi buğulanma | ②, ⑩ | 🔴 |
| 01:50–02:00 | Buza doğru el uzatma | Giysi omuz direnci, yavaşlayan kol erişimi | ⑥ | 🔴 |

---

## CONTRADICTION LOG

| Timecode A | Timecode B | Contradiction |
| --- | --- | --- |
| 00:10 (S1) | 00:20 (S2) | S1'de oldukça kalın ve sert yapıda basınçlı eldiven görünürken, S2'de aynı eldiven sıfır malzeme direnciyle mikro metal kadranları çıplak el hassasiyetinde çeviriyor. |
| 01:30 (S9) | 01:40 (S10) | S9 bataryanın tükenmesiyle tam durğanlık ve çöküş hissiyle biterken, S10 hiçbir dinlenme adımı gösterilmeden karakteri dik ve taze diz çökme pozisyonuna sıfırlıyor. |

---

## THE THREE THAT MATTER

1. **00:10–00:50 (S1–S5) — Kalın EVA Eldivenleriyle Sıfır Dirençli İnce Motor Kullanımı (Desen ⑥/⑬):** Hacimli basınçlı uzay eldivenleri, hiçbir malzeme sertliği veya eklem direnci sergilemeden hassas düğme ve kadranları çalıştırıyor.
*Çözüm:* Eldiven dikişlerinde büzülme, parmak bükülmelerinde yavaşlama ve kadran çevrimlerinde hafif bilek duraksaması ekleyin.
2. **00:30–00:40 (S3) — EVA Giysisi İle Rampada Zahmetsiz Yürüyüş (Desen ①/⑥):** İniş aracı rampasını tırmanırken giysi kütlesinin yarattığı eylemsizlik, adım ağırlığı ve gövde salınımı ekrana yansımıyor.
*Çözüm:* Gövdede hafif öne eğilme, daha geniş basma açısı ve giysi hantallığına uygun daha yavaş diz bükülmesi uygulayın.
3. **01:30–02:20 (S9–S14) — Dondurucu Ortamda Görünür Nefes ve Vizör Buğulanması Eksikliği (Desen ⑩):** Kriyojenik uzay ortamında ve fiziksel efor anlarında kask vizöründe hiçbir nem, buğu veya göğüs kalkış ritmi görülmüyor.
*Çözüm:* Efor ve duygusal doruk sahnelerine (S9, S14) ritmik vizör iç buğulanması ve hafif omuz nefes hareketi entegre edin.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Kurguda Düzeltilebilir (Fixable in the Edit):** S3–S4 ve S5–S6 arasındaki hak edilmemiş eğri düşüşleri, birkaç sahnenin sırası değiştirilerek veya geçişler kısaltılarak yorulma eğrisine uyumlu hale getirilebilir.
* **Yeniden Üretim Gerektirir (Requires Regeneration):** Tüm fiziksel iş sahneleri (S1, S2, S3, S5, S8, S9, S11); giysi eklem direnci, eldiven sertliği, eylemsizlik ve vizör buğulanması gibi bedensel mekanikleri içermediğinden doğrudan AI video üretimi seviyesinde yeniden üretilmelidir. Kurgu katmanı bedene sonradan fiziksel ağırlık ekleyemez.

---

## FLAGS FOR DOCUMENT CHECK

* Plan (SPEC), EVA giysisinin motorize/servo destekli bir dış iskelet (exosuit) olduğunu mu öngörüyor? (Eğer öyleyse düşük efor görüntüsü kurgusal olarak açıklanabilir).
* Niva atmosferinde vizör buğulanma kontrolü kask içi iklimlendirme tarafından %100 engelleniyor mu, yoksa efor anlarında buğulanma olması bekleniyor mu?

---

## OUT-OF-SCOPE FLAGS

* **[PHYSICS Merceği]** 0,12g yerçekiminde iniş aracı ve telemetri kutusunun kütle ve eylemsizlik oranlarının sayısal doğruluğu.
* **[CONTINUITY Merceği]** Telemetri kutusu üzerindeki ışık ve kaplama detaylarının yakın ve geniş açılar arasındaki görsel tutarlılığı.
* **[SOUND Merceği]** Giysi içi soluk ses tasarımı, akustik buz çıtırtıları ve miksteki bas rezonansı dengesi.
