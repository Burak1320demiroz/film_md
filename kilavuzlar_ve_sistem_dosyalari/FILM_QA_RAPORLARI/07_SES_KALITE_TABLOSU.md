# 🔊 SES VE DİYALOG KALİTE TABLOSU  ⛔ KAPALI

> # ⛔ BU TABLO KAPALIDIR — 22.08.2026
>
> **Satırları `SES_VE_DIYALOG_QA` rubriğinin ölçümüdür.** O rubrik aynı gün arşive
> alındı: `../QA_PROMPTLARI/ARSIV_6_MERCEK/`. Yerini `③ 3_SES` aldı ve
> yeni satırlar **başka bir paydayla** ölçülüyor.
>
> ```
> YENİ SATIR BURAYA YAZILMAZ  →  T3_SES_KALITE.md
> ```
>
> ⛔ **Buradaki skorlarla yeni tablonunkiler KARŞILAŞTIRILAMAZ.** Kategori
> sayısı, kategori sınırları ve ortalamanın paydası değişti; aynı filme
> iki sistemde verilen iki puan iki farklı ölçüdür, birinin diğerinden
> yüksek olması bir şey söylemez.
>
> Tablo silinmedi ve silinmeyecek — bu depoda 11 filmin ham raporu bir kez
> kayboldu ve geriye yalnız bu tür özet satırları kaldı. Aşağıdaki her şey
> tarihsel kayıttır ve olduğu gibi durur.

> **Kaynak prompt:** `../QA_PROMPTLARI/SES_VE_DIYALOG_QA_CRITIQUE_PROMPT.md`
> **Oluşturma:** 09.08.2026 — rubriğin ilk çalıştırmasıyla birlikte
> (kart E3 kuralı: ilk çalıştıran ajan tabloyu 06'nın formatını taklit ederek açar)
>
> Projenin **beşinci** skor tablosu. Ne ölçtüğü diğerlerinden farklı:
>
> ```
> LESSONS_LEARNED · KALİTE TAKİP    kare içi teknik    "bu klip doğru mu"
> 03_HIKAYE_KALITE_TABLOSU          dramatik           "kimse umursar mı"
> 04_MANTIK_KALITE_TABLOSU          sahneler arası     "film kendiyle çelişiyor mu"
> 06_KARAKTER_KALITE_TABLOSU        sahneler arası     "karakter aynı karakter mi"
> 07_SES_KALITE_TABLOSU ← bu        film boyu          "doğru ses doğru bedenden mi"
> ```
>
> ⚠️ Bu rubrik **doküman istemez** (baseline = STEP 1 ses defteri, kurgudan
> kurulur) ve **tek klibe koşulmaz** — yalnız TAM KURGU (D75'in ses karşılığı).
> Karşılığında rubrik "senaryodaki replik bu değil" diyemez; çözemediğini
> `FLAGS FOR DOCUMENT CHECK` altına soru yazar, cevaplar film kaydına işlenir.
>
> ⚠️ **REGISTER şerhi:** "Sentetik" sütunu yalnız İNSAN register'lı
> repliklerin insan geçip geçmediğini ölçer. MACHINE register'lı bir sesin
> düz okuması tasarımdır, buraya ceza olarak yazılmaz. Register haritası ↔
> plan karşılaştırması (kart E3 adım 2) yapılmadan satır kesinleşmez.
>
> ⚠️ **KARAKTER_QA ile kesişim:** iki mercek aynı filme koşulduysa ses
> bulguları BU tabloya yazılır, 06'nın Ses sütunu `→🔊` işaretçisine iner.

---

## 📊 TABLO

| Film | Atıf | Sentetik | Ses Kimliği | Performans | Sıra-Akustik | Ortam | SFX | Miks | Müzik | Genel |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **The Cold Burn** | **9** | 6 | 8 | 5 | 6 | **3** | 5 | 4 | 4 | **5/10** AUDIBLE DRIFT |
| **The Banded Deep** | N/A | N/A | N/A | N/A | N/A | 6 | 5 | 7 | 7 | **6.2/10** SOUNDTRACK HOLDS |
| ~~**The Black Cradle**~~ | ~~8~~ | ~~8~~ | ~~9~~ | ~~5~~ | ~~7~~ | ~~8~~ | ~~4~~ | ~~7~~ | ~~8~~ | 🚨 **GEÇERSİZ** |

> 🌑 **Black Cradle (17.08.2026) — 🚨 GEÇERSİZ: ses defteri filmin ses defteri değil.**
> Rapor **2 replik** duydu; plan **14 replik / 12 sahne** diyor ve ölçülen bandın
> içinde bile en az 7 replik var. Ortam haritası 4 satır — oysa bu merceğin ana sorusu
> ("yatak kesmelerde ölüyor mu") ancak kesme sayısıyla sorulabilir ve aynı dosyada
> VIDEO_QA **21 kesme** saydı [DERS 107].
> ⛔ **REGISTER DOĞRULAMASI (kart E3 adım 2) yarı yarıya ters:** 0:30 repliği doğru
> şekilde MACHINE ama **ekrandaki kadına atfedildi** — MİRA GÖVDESİZDİR, atıf başlı
> başına D82 vakasıdır; 1:09 repliği planda **HUMAN (pilot)** iken MACHINE yazıldı.
> Bu iki hücreden (Atıf 8 · Sentetik 8) bulgu ALINMAZ.
> ⛔ **Çapraz fatura [DERS 108]:** Performans 5 · SFX 4 · Miks 7'nin kaynağı 1:09
> dudak senkronu ve 1:45 vakumda ses — ikisi de bu rubriğin ❌ listesinde VIDEO_QA'ya
> verilmiş olaylar. Düşürülünce satırın okuması ~8.8'e çıkıyor.
> ✅ Buna karşılık plandaki **register haritası ALET olarak çalıştı**: raporun hatası
> ancak onun sayesinde görüldü — D82'nin yazılma amacı buydu.
> [`01_FILM_RAPORLARI/THE_BLACK_CRADLE.md`](01_FILM_RAPORLARI/THE_BLACK_CRADLE.md)

```
ÖLÇÜLEN FİLM: 1        ⚠️ tek satırla örüntü çıkarılmaz (±1.3 sapma kuralı)
İLK KOŞUNUN ANA DERSİ:  ATIF TUTUYOR (9), YATAK TUTMUYOR (3).
                       Doğru ses doğru bedenden çıkıyor; ama ortam yatağı
                       her klip sınırında ölüyor (1:20-1:40 mutlak dijital
                       sessizlik) ve miks hiyerarşisi doruğu yutuyor
                       → DERS 83. Bulguların ÇOĞU miks seansıyla çözülür,
                       yeniden üretim gerektirmez — rubriğin "FIXABLE IN
                       THE MIX vs REGENERATION" ayrımı ilk koşuda işledi.
REGISTER UYARISI:      Rapor 7 replik / 7 HUMAN / 0 MACHINE saydı; plan
                       12+ replik / kask telsizi + gövdesiz EKO diyor.
                       Skorlar ekrandaki filme göre GEÇERLİ; ama register
                       haritasının planla farkı, ses MİMARİSİNİN üretimde
                       tersine döndüğünü kanıtladı → DERS 82. Ayrıntı:
                       01_FILM_RAPORLARI/THE_COLD_BURN.md
```

---

## 📥 SATIR EKLEME KURALI

```
1. SES QA çalıştırılır — YALNIZ TAM KURGU verilir, doküman VERİLMEZ
2. Header kontrolü: AUDIO STATE ilan edilmiş mi? STATE C (AUDIO ABSENT)
   ise satır YOK — master'ın ses kanalı doğrulanıp yeniden ihraç edilir
3. Ham çıktı 02_HAM_RAPORLAR/<FILM>_SES_HAM.md olarak kaydedilir
4. ⭐ REGISTER DOĞRULAMASI (kart E3 adım 2): ledger'daki HUMAN/MACHINE
   işaretleri planla karşılaştırılır; MACHINE olması gereken repliğe
   yazılmış "sentetik duruyor" bulgusu DÜŞER
5. Satır bu tabloya yapıştırılır — verdict satıra yazılır
6. FLAGS FOR DOCUMENT CHECK soruları plan/senaryodan cevaplanır,
   cevaplar 01_FILM_RAPORLARI/<FILM>.md içine yazılır
7. KARAKTER_QA aynı filme koşulduysa 06'nın Ses sütunu →🔊 işaretçisine
   iner; VIDEO_QA aynı kurguyu ölçtüyse ses bulguları buraya devredilir
8. "FIXABLE IN THE MIX" listesi 00_INDEX yapılacaklara ayrı blok olarak
   geçirilir — bu merceğin bulguları çoğunlukla ucuz onarımdır
```

---

## 🔗 İLGİLİ

| Dosya | İçerik |
|---|---|
| `00_INDEX.md` | film başına QA kapsamı |
| `06_KARAKTER_KALITE_TABLOSU.md` | bedenin tarafı — kesişimin öbür yakası |
| `../LESSONS_LEARNED.md` | ders arşivi (82-83 bu rubriğin ilk koşusundan çıktı) |
| `../VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md` | üretim tarafı: tırnak sentaksı, katman limiti, tek konuşmacı |
