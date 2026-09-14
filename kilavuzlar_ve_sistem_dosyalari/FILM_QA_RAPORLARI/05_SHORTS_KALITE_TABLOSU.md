# 📱 DİKEY SHORTS KALİTE TABLOSU  ⛔ KAPALI

> # ⛔ BU TABLO KAPALIDIR — 22.08.2026
>
> **Satırları `SHORTS_QA` rubriğinin ölçümüdür.** O rubrik aynı gün arşive
> alındı: `../QA_PROMPTLARI/ARSIV_6_MERCEK/`. Yerini `① 1_KARE (FORMAT: DİKEY)` aldı ve
> yeni satırlar **başka bir paydayla** ölçülüyor.
>
> ```
> YENİ SATIR BURAYA YAZILMAZ  →  T1_KARE_KALITE.md
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

> **Kaynak prompt:** `../QA_PROMPTLARI/SHORTS_QA_CRITIQUE_PROMPT.md`
> **Oluşturma:** 06.08.2026 — rubriğin dipnotundaki borç kapandı: "kapıları
> GEÇEN ilk çalıştırma tabloyu açmak zorunda." İlk geçerli koşu (THE FIRST
> MORNING, 06.08) tabloyu açmamıştı; ikinci geçerli koşu (THE WRONG SHADOW,
> aynı gün) ikisini birden işledi.
>
> Projenin **beşinci** skor tablosu. Dikey hattın TEK rubriği 16 kategori
> taşır (teknik + sahneler arası + hikaye + müzik); bu tablo rubriğin
> "QUALITY TABLE ROW" çıktısını (kare içi 9 kategori) tutar, kurgu
> mercekleri (13-16) ayrı tabloya iner. Kategori adları 1-8 bilerek
> `LESSONS_LEARNED` teknik tablosuyla aynıdır — dikey ve yatay skorlar
> karşılaştırılabilir kalır; ama satırlar bu dosyada durur, teknik tabloya
> YAZILMAZ (o tablo yatay VIDEO_QA'nındır).
>
> `Ⓥ` = INPUT MODE V (SPEC'siz koşu; film kendisiyle + fizikle ölçüldü).
> Ⓥ satır gerçek satırdır, eksik satır değil — ama D satırlarıyla aynı
> ölçüm değildir, ayrı tutulur. ⚠️ Ölçüm sapması ±1.3 burada da geçerli:
> 1.5'tan küçük farklar gürültüdür.

---

## 📊 TABLO — kare içi kategoriler (rubrik 1-11)

| Film | Sahne | Karakter | Fizik | Kamera | Işık | Çevre | Parçacık | Dikey | Güvenli Alan | Kanca | Toplam |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| The First Morning Ⓥ | ALL | 6 | 6 | 7 | 6 | 6 | 5 | 7 | 7 | 6 | **6.0/10** |
| The Wrong Shadow Ⓥ | ALL | 6 | **4** | 5 | 6 | 5 | 8 | **9** | 7 | 5 | **5.6/10** |
| The Black Cradle — Fragman Ⓥ 🚨 | ALL | ~~7~~ | ~~6~~ | ~~8~~ | ~~7~~ | ~~8~~ | ~~7~~ | ~~9~~ | ~~5~~ | ~~3~~ | ~~**6.5/10**~~ |

## 📊 TABLO — kurgu mercekleri (rubrik 13-16 · yalnız MATERIAL MODE B)

| Film | Sahneler Arası | Hikaye & Aktarım | Tutundurma | Müzik | Hüküm |
|---|:--:|:--:|:--:|:--:|---|
| The First Morning Ⓥ | 5 | 7 | 6 | 5 | REGENERATE (jenerik kartı · 64 s) |
| The Wrong Shadow Ⓥ | 6 | **3** | **3** | 6 | REGENERATE (3 BLOCKER · novum ekranda YOK) |
| The Black Cradle — Fragman Ⓥ 🚨 | ~~6~~ | ~~7~~ | ~~5~~ | ~~8~~ | REGENERATE (başlık kartı · 63 s) — ⛔ ATIF DOĞRULANMADI |

```
ÖLÇÜLEN FİLM: 3 · ÜÇÜ DE Ⓥ · ÜÇÜ DE REGENERATE
ORTAK BLOCKER (3/3): kurguda jenerik/başlık kartı + 63-64 s / 7 segment —
                     kurgu kapısı (DERS 70) üç teslimde de koşulmamış.
                     Sahne süreleri üçünde de ~10 s (plan: 8 s).
                     ⭐ Örüntü artık tesadüf değil: dikey hatta ÜRETİM
                     ARACI 8 s'e kilitlenmiyor ve kurgu kendi kartını
                     ekliyor. Prompt cümlesiyle çözülmez — araç ayarı.
DİKEY FORMAT:        üçünde de en güçlü kategori (7 · 9 · 9) — 9:16
                     kompozisyon kilitleri ÇALIŞIYOR.
EN DÜŞÜK:            Wrong Shadow Hikaye/Tutundurma 3 — kök neden novum
                     yokluğu (DERS 73), içerik zaafı değil; film kaydına bak.
```

> 🚨 **Black Cradle — Fragman satırı GEÇERSİZ (17.08.2026, mod V):** skorlar
> üstü çizili, çünkü **ölçülen nesnenin kimliği doğrulanmadı.** Raporu bu
> fragmana bağlayan tek kanıt 00:58'deki başlık kartının yazısıdır — rubriğin
> modele okumasını yasakladığı kare. Eşleme elle yapıldı ve tutmadı: 6
> vuruşun 3'ü sırası bozuk eşleşti, 2'si yok, 2 çekim hiçbir belgede geçmiyor,
> yanaşma filmin imzasının tersine BURUN ÖNDE. → **DERS 105** (kimlik kapısı)
> ve **DERS 106** (rubrik fragmanı film sanıyor).
> Ayrıca: SPEC fragman dosyasında hazırdı, yapıştırılmadı → D94'ün 7. vakası.
> Satır ancak operatör master'ın kimliğini doğrularsa ⚠️ ŞARTLI Ⓥ'ye döner.
> Ayrıntı: `01_FILM_RAPORLARI/THE_BLACK_CRADLE_FRAGMAN.md`

> 📌 Belge cevapları ve hüküm gerekçeleri film kayıtlarında:
> `01_FILM_RAPORLARI/THE_WRONG_SHADOW.md` · First Morning'in film kaydı
> henüz yazılmadı (ham raporu `02_HAM_RAPORLAR/THE_FIRST_MORNING/THE_FIRST_MORNING_SHORTS_HAM.md`).
