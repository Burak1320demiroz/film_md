# 🔍 3 GEÇİŞLİ QA SİSTEMİ — 7-9 Dakikalık Filmler

> **Neden 3 prompt?** 2-4 dk formatının tek dev QA promptu (`1_KARE_QA_CRITIQUE_PROMPT.md`,
> 11 kategori, 511 satır) 8 saniyelik TEK klip için tasarlandı. 480 saniyelik,
> 60 sahnelik bir filme aynı prompt uygulandığında model:
> - ilk 60-90 saniyeden sonra detay çözünürlüğünü kaybeder,
> - 11 kategoriyi aynı anda takip edemez, en gürültülü hataya kilitlenir,
> - rapor uzunluğu limitine takılır ve son fazları hiç incelemeden bitirir.
>
> Çözüm: **aynı videoyu 3 kez, 3 farklı mercekle** izletmek. Her geçiş dar bir
> alana odaklanır ve diğer iki geçişin alanını AÇIKÇA raporlamaz.

---

## 📊 GEÇİŞ HARİTASI

| # | Dosya | Mercek | Ne arar | Zaman ekseni |
|:-:|---|---|---|---|
| **1** | `QA_1_TEKNIK_BUTUNLUK.md` | Görüntünün kendisi | Gizli kesme, çapa sadakati, kamera, fizik, ışık fiziği, doku yüzmesi, ekran metni | **Sahne içi** (8s'lik pencere) |
| **2** | `QA_2_DEVAMLILIK_VE_KARAKTER.md` | İnsan + süreklilik | Yüz kayması, suit/prop sürüklenmesi, ölçek, mekan coğrafyası, ekipman durumu, zincir dikişleri | **Sahneler arası** (60 sahne boyu) |
| **3** | `QA_3_ANLATI_RITIM_SES.md` | Seyirci deneyimi | 5 fazlık yay, tempo, ölü noktalar, diyalog, lip-sync, ses katmanları, müzik yayı | **Film boyu** (480s) |

### Sınır kuralı (çakışmayı önleyen tek şey bu)

Her prompt kendi bölümünde **"BU GEÇİŞTE RAPORLANMAYACAKLAR"** bloğu taşır.
Bu blokları silme — üç raporun birleştirilebilir olmasının tek garantisi odur.

```
Gizli kesme, kamera, parçacık, bloom, ekrandaki yazı  → SADECE Geçiş 1
Yüz, cilt, kostüm, prop, ölçek, mekan, dikiş          → SADECE Geçiş 2
Hikaye, tempo, diyalog metni, lip-sync, ses, müzik    → SADECE Geçiş 3
```

---

## 🛠 NASIL ÇALIŞTIRILIR

### Adım 1 — SPEC bloğunu doldur
Her promptun başında bir **SPEC BLOCK** var. Filmin `README.md`'sindeki
Bible'lardan ve `REFERANS_PAKETI.md`'den doldurulur. **Boş bırakılan her alan,
o kontrolü `UNVERIFIABLE` yapar** — model tahmin etmez, "doğrulanamadı" der.

> ⚠️ Geçiş 2 SPEC bloğu en uzun olanıdır ve en kritik olanıdır. Karakter/suit/prop
> tarifi olmadan "tutarlı mı?" sorusunun cevabı yoktur.

#### 🚨 BU ADIM ATLANIRSA NE OLUR — The Slow Stone QA'sından ölçüldü

İlk testte üç geçiş de SPEC bloğu **boş** çalıştırıldı. Sonuçlar:

```
1. YAPI UYDURMA — Film 4 kısım × 48 sahne × 10s idi; şablon 5 faz × 60 × 8s
   diyordu. Geçiş 2 ve Geçiş 3, VAR OLMAYAN "Faz 5 / sahne 49-60" için puan
   verdi. İki model de eksikliği bildirmek yerine boşluğu doldurdu.

2. REFERANS TERSİNE DÖNDÜ — Geçiş 2 karakter referansını Bible'dan değil
   VİDEODAN kurdu. Bu, tanım gereği sadece "film kendi içinde tutarlı mı"
   sorusunu cevaplar; "film tasarıma uygun mu" sorusunu cevaplayamaz.
   Bible'daki 4 ayırt edici yüz işaretinin HİÇBİRİ kontrol edilmedi.
   Verdiği "identity holds 7/10" hükmü bir uygunluk belgesi DEĞİLDİ.

3. KASITLI İLERLEME HATA SANILDI — Filmin imzası olan kısım-kısım artan
   mineral kabuk (Bible: "filmin GERİ SAYIMI"), SPEC'siz bakan Geçiş 2
   tarafından "istenmeyen sürüklenme" olarak okundu. Filmin ana anlatı
   aracının ekranda okunup okunmadığı ölçülemedi.

4. NOVUM PUANI ŞİŞTİ — Geçiş 3, Kavrama'ya 8/10 verdi. Bible'la karşılaştırınca
   novum'u yanlış anlattığı görüldü; gerçek puan 4/10 civarı.
```

> Üç prompt da bu dört hataya karşı sertleştirildi (yapı artık parametre,
> referans zorunlu olarak Bible, kasıtlı ilerleme ayrı denetleniyor, novum
> için kısmi puan yasak). Ama **hiçbir prompt boş SPEC'i telafi edemez.**
> SPEC doldurmadan çalıştırmak, QA yapmak değil QA yaptığını sanmaktır.

### Adım 2 — Videoyu yükle, promptu yapıştır
Üç geçişi **ayrı ayrı sohbetlerde** çalıştır. Aynı sohbette arka arkaya
çalıştırırsan model önceki raporunu tekrarlar, taze bakmaz.

### Adım 3 — Cevapları bana at
Üç raporu da bana gönder. Ben:
1. Üç raporu tek tabloda birleştiririm (aşağıdaki şablon),
2. Çakışan bulguları tekilleştiririm,
3. Mevcut 42 derse eşleşenleri işaretlerim,
4. Eşleşmeyenleri **Ders 43+** formatında `LESSONS_LEARNED.md`'ye yazarım,
5. Prompt düzeltmelerini ilgili faz dosyasına uygularım.

---

## 📋 BİRLEŞİK RAPOR ŞABLONU (üç geçiş geldikten sonra doldurulur)

```
FİLM:              [ad]
TOPLAM SÜRE:       [mm:ss]
İNCELENEN SAHNE:   [60 / kısmi]
QA TARİHİ:         [tarih]

## GEÇİŞ SKORLARI
| Geçiş | Kapsam | Skor | 🔴 | 🟠 | 🟡 |
|---|---|:--:|:--:|:--:|:--:|
| 1 — Teknik Bütünlük | | __/10 | | | |
| 2 — Devamlılık & Karakter | | __/10 | | | |
| 3 — Anlatı, Ritim & Ses | | __/10 | | | |
| **FİLM GENEL** | | **__/10** | | | |

## KARAR
[YAYINA HAZIR / DÜZELTME GEÇİŞİ / FAZ YENİDEN ÜRETİMİ]
Yeniden üretilecek sahneler: [liste]

## KISIM/FAZ BAZLI ISI HARİTASI
> Filmin GERÇEK yapısı kadar satır — 4 kısımlık filme 5. satır eklenmez.
| Kısım | Sahne | 🔴 | 🟠 | En ağır hata |
|---|---|:--:|:--:|---|

## DERSE DÖNÜŞENLER
| Bulgu | Geçiş | Mevcut ders? | Aksiyon |
|---|:--:|---|---|
| | | Ders __ / YENİ | prompt güncellemesi / yeni ders |
```

---

## 🎯 TEKRARLAYAN HATA EŞİĞİ — DERS Mİ, TEK SEFERLİK Mİ?

Ders çıkarırken kullanılan kural (`LESSONS_LEARNED.md` disiplini):

```
1 sahnede görüldü          → prompt notu, ders DEĞİL
2-3 sahnede görüldü        → faz dosyasına negatif satır eklenir
4+ sahnede veya 2+ fazda   → YENİ DERS (Ders 43+) — global negatif bloğa girer
Farklı filmde de görüldüyse → derse "PERSISTENT" etiketi
```

Bu eşik olmadan ders listesi şişer ve negatif blok karakter bandını (video
2.000-2.600) patlatır. **Her yeni ders, negatif bloğa kelime ekler — bedava değildir.**

---

## 📚 İLGİLİ DOSYALAR

| Dosya | Konum | Ne için |
|---|---|---|
| 5 Faz Mimarisi | `../5_FAZ_MIMARISI.md` | Geçiş 3'ün yay ölçütü |
| Kesintisiz Üretim Tekniği | `../KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` | Geçiş 1'in çapa ölçütü |
| Faz Dosyası Şablonu | `../FAZ_DOSYASI_SABLONU.md` | Düzeltmelerin uygulanacağı yer |
| Lessons Learned | `../../../kilavuzlar_ve_sistem_dosyalari/LESSONS_LEARNED.md` | 42 ders — eşleştirme kaynağı |
| Tekil klip QA | `../../../kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md` | Tek 8s klip yeniden üretilince |
