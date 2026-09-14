# 🔗 T2 — DEVAMLILIK KALİTE TABLOSU (sahneler arası)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 22.08.2026 — dört mercekli sisteme geçişle birlikte
> **Selefleri:** `04_MANTIK_KALITE_TABLOSU.md` ve
> `06_KARAKTER_KALITE_TABLOSU.md` — ikisi de aynı gün KAPANDI. İki rubrik
> tek merceğe indi: 16 kategori yuvası 13'e, çift sayım kuralla değil
> YAPIYLA kesildi.
>
> **Ne ölçer:** "Film ve içindeki insan kendiyle çelişiyor mu." Her bulgu
> İKİ sahne gerektirir; tek kareden söylenebilen hiçbir şey buraya girmez.
>
> ```
> GÖVDE   1-6   kimlik · kostüm · yıpranma · ekipman · çapraz kesme · fizik
> DÜNYA   7-13  sayaç · coğrafya · zaman-ışık · dünya propu · nedensellik
>               · nicelik+sayı · kurulum
> ```
> Bir okur bu tabloya bakıp filmin **insanını mı yoksa yerini mi**
> kaybettiğini görebilmeli — ikisi farklı üretim hatasıdır ve farklı
> çözümleri vardır.

---

## 📏 BU TABLOYU OKUMA KURALLARI

```
Ⓥ   MOD V — SPEC verilmeden koşuldu; film kendisiyle + fizikle ölçüldü.
    Gerçek satırdır, eksik satır değildir; ama mod D satırıyla aynı
    ölçüm DEĞİLDİR. İkisi aynı sütunda toplanmaz.
⛔   ÖN KOŞU — planda SPEC hazırdı ama mod V koşuldu. Skor tabloya girer,
    tamlık matrisine GİRMEZ.
    ⚠️ 11.09.2026 · BU TABLODA ⛔ YAZILMAZ: bu mercek SPEC'e göre TASARIM
    GEREĞİ mod V'dir (`FILM_KLASOR_SABLONU/FILM_QA_SPEC.md` §HANGİ RUBRİĞE NE
    VERİLİR → "hiçbir şey (tasarım gereği) MOD V"); "SPEC hazırdı ama
    verilmedi" bu mercek için tanımsızdır. ⛔ yalnız SPEC ALAN merceklerde
    (①④ ve ⑥⑨-⑬) geçerlidir. Ⓥ satırı bu tabloda GEÇERLİ satırdır ve
    tamlık matrisine Ⓥ olarak GİRER; rapor_kontrol.py'nin "TABLOYA" sütunu
    da onu böyle yazar. (Bu tarihe kadarki Ⓥ ⛔ satırlarından ⛔ kaldırıldı.)
🚨   GEÇERSİZ — koşu bir kapıdan geçmedi (sahne sayısı tutmadı, yanlış
    materyal, yanlış mercek). Satır üstü çizili durur, ortalamaya girmez.
—    Kategori N/A veya UNVERIFIABLE: boş bırakılır. ASLA 0 yazılmaz;
    sıfır, ortalamayı temiz bir filmmiş gibi gösterir.
```

⚠️ **ÖLÇÜM SAPMASI ±1.3 PUAN.** Aynı rubrik aynı filmi iki kez ölçtü,
kategoriler 2 puana kadar oynadı. **1.5 puandan küçük fark, fark değildir.**
Bir filmin diğerinden iyi olduğunu söylemek için aradaki farkın 1.5'i
geçmesi gerekir.

⛔ **Bir filme koşulan bütün merceklere AYNI dosya verilir** ve **her mercek
temiz oturumda koşulur.** Aynı oturumda ikinci bir mercek çalıştırılırsa
mercekler birbirinin sahne haritasını devralır; "dört mercek aynı şeyi
gördü" o zaman bir doğrulama değil, tek raporun dört kopyasıdır.

---

## 📊 TABLO

| Film | Kimlik | Kostüm | Yıpranma | Ekipman | Çapraz Kesme | Fizik | Sayaç | Coğrafya | Zaman-Işık | Dünya Propu | Nedensellik | Nicelik+Sayı | Kurulum | Toplam |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

| **The Iron Slope** Ⓥ ⚠️ | ⬜ | 3 | 10 | 5 | 9 | 8 | — | 2 | 7 | 3 | ⬜ | — | ⬜ | **5,9** |

| **The Rose Coat** ⚠️ | — | ⬜ | ⬜ | ⬜ | (7) | — | ⬜ | (7) | — | ⬜ | — | — | — | **—** |
| **The Payload** Ⓥ ⚠️ | 9 | 3 | 4 | 3 | 8 | 8 | — | 6 | 9 | 4 | 9 | 1 | 8 | **6,0** |
| **The Skylight** Ⓥ | 9 | 5 | 4 | 6 | 8 | 7 | — | 7 | 8 | 6 | 9 | 9 | 9 | **7,2** |
| **The Still Swarm** Ⓥ ⚠️ | 10 | 7 | 10 | 4 | 8 | 10 | — | 7 | 10 | 8 | 10 | 3 | 7 | **7,8** |
| **The Thin Roof** Ⓥ ⚠️ | — | — | 8 | 6 | 9 | — | — | 7 | — | — | — | 1 | — | **6,2** |
| **The Upward Fall** Ⓥ ⚠️ | — | 7 | — | 4 | — | — | — | 6 | — | — | — | — | — | **5,7** |
| **The Counted Turn** ⚠️ | 1 | 1 | — | 7 | — | — | ⬜ | — | — | — | — | — | — | **3,0** |
| **The Solar Mirror** Ⓥ ⚠️ | — | 9 | — | — | 9 | 9 | — | — | — | — | — | 9 | 9 | **9,0** |
| **The Hard Dock** Ⓥ ⚠️ | — | 9 | — | 8 | 8 | — | — | 8 | 9 | 9 | — | — | 8 | **9,1** |
| **The Silent Perihelion** Ⓥ ⛔ ⚠️ | 7 | 10 | 4 | 5 | ⬜ | 10 | — | 10 | 10 | ⬜ | ⬜ | 10 | 10 | **8,8** |
| **The Shattered Breath** Ⓥ ⛔ ⚠️ | 8 | 5 | 8 | 7 | ⬜ | 9 | — | 7 | 9 | ⬜ | ⬜ | — | — | **7,7** |
| **The Locked Pulse** Ⓥ ⛔ | 3 | 6 | 10 | 3 | ⬜ | 8 | 10 | 5 | 8 | ⬜ | ⬜ | 2 | 6 | **5,4** |

> **The Hard Dock · 12.09.2026 · Ⓥ mod V (tasarım gereği) · ⚠️ ŞARTLI**
> Kayıt: [`01_FILM_RAPORLARI/THE_HARD_DOCK.md`](01_FILM_RAPORLARI/THE_HARD_DOCK.md)
> · `rapor_kontrol.py` ile düzeltildi: Kusur bildirilmeyen 5 kategori (10/10) `—` hücresine döndü [D186]. Düzeltilmiş ortalama: **9,1** (Ham: 9,08/10).
> · Kesme sayısı (15) master ölçümünden (24) saptığı için film boyu kategoriler şartlı işaretlendi.

| **The Resonant Strand** Ⓥ ⛔ ⚠️ | — | 8 | 9 | 7 | ⬜ | 9 | — | 8 | 9 | ⬜ | ⬜ | — | 6 | **7,9** |

> **The Rose Coat · 26.08.2026 · belgesiz koşu · ⚠️ ŞARTLI**
> Kayıt: [`01_FILM_RAPORLARI/THE_ROSE_COAT.md`](01_FILM_RAPORLARI/THE_ROSE_COAT.md)
> · Raporun toplamı **7,2** ve raporun kendi hükmü `STRUCTURAL PROBLEM` —
> söz ile sayı zıt yöne bakıyordu. Sebep: 12 puanlı hücrenin **6'sı**
> "no in-scope source · 10/10". Kaynaklı hücrelerin ortalaması **4,3**;
> Δ = 2,9 puan, sıfır yeni gözlem [D131]. O altı hücre artık `—`.
> · Parantezli iki hücre ⑩'dan geçemedi [D130]: **Coğrafya (7)** kaynağı
> pada mesafe sayacıydı (S5 = 120 m ↔ S9 = 0 m — film gemiye YÜRÜYOR) ·
> **Çapraz Kesme (7)** kaynağı SPEC'in temas bütçesiydi ("düşen figüre
> yardım edilmemesi TASARIMDIR").
> · **Sayaç ⬜:** rapor `no counter present` yazdı; filmde ÜÇ metinsiz
> sayaç var ve biri filmin ana mekanizması (sırt durumu, beş görsel
> durum, monotonik). Bu bulgu yokluğu değil ÖLÇÜM BOŞLUĞUDUR [D134].
> · **Kostüm/Yıpranma/Ekipman ⬜:** üçü de "sırt çantası" okumasına asılı;
> SPEC `çanta 0 · sırt DÜZ GÖMME PANEL · silüet 13/13 dümdüz` diyor.
> · ⭐ Raporun #1 bulgusu (bot rengi) doğru yakalandı, YANLIŞ ETİKETLENDİ:
> "kostüm sürüklenmesi" değil, iki figürü ayıran ÜÇ kanaldan biri [D134].

> **The Iron Slope · 25.08.2026 · Ⓥ mod V (tasarım gereği) · ⚠️ ŞARTLI**
> Kayıt: [`01_FILM_RAPORLARI/THE_IRON_SLOPE.md`](01_FILM_RAPORLARI/THE_IRON_SLOPE.md)
> · ⬜ hücreler kapı ④ gereği **sayı taşımaz** (süre 65,0 s ≠ 48,0 ± 2 →
> film boyuna bakan kategoriler: Kimlik sürekliliği · Nedensellik · Kurulum).
> · Kostüm 3/10 ayakta ve **rapordan ağır**: armaların sürüklenmesi bir yana,
> göğüsteki kırmızı/mavi arma ile yanan gösterge planın negatif bloğunda
> yasaklıydı (`no patch, no logo`). · Coğrafya 2/10 ayakta.

> **The Counted Turn · 09.09.2026 · MOD D · ⚠️ ŞARTLI**
> Kayıt: [`01_FILM_RAPORLARI/THE_COUNTED_TURN.md`](01_FILM_RAPORLARI/THE_COUNTED_TURN.md)
> · `rapor_kontrol.py` ile düzeltildi: Kusur bildirilmeyen 9 kategori (10/10) `—` hücresine döndü [D186]. Düzeltilmiş ortalama: **3,0** (Ham: 8,2/10).
> · 🔴 BLOCKER: 🚨 **KİMLİK KIRILMASI** — S12/S14 yüz değişimi (sakallı erkek ↔ pürüzsüz kadın), S13 kostüm değişimi (hantal uzay giysisi ↔ koyu deri ceket).

> **The Solar Mirror · 11.09.2026 · Ⓥ mod V (tasarım gereği) · ⚠️ ŞARTLI**
> Kayıt: [`01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md`](01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md)
> · `rapor_kontrol.py` ile düzeltildi: Kusur bildirilmeyen 7 kategori (10/10) `—` hücresine döndü [D186]. Düzeltilmiş ortalama: **9,0** (Ham: 9,6/10).
> · SPEC olduğu hâlde ①/③ mercekleri mod V koşulduğu veya okunamadığı için GEÇERSİZ basıldı [D129]. T1 ve T3 tablolarına satır GİRMEDİ. ④ HİKAYE merceği henüz koşmadı.

⛔ **İki bulgu diğer bütün skorları ezer:**
```
KİMLİK KIRILMASI  başka bir yüz, ya da ekranda kopya karakter
SAYAÇ TERSİNMESİ  geri giden sayaç — devamlılık kayması değil,
                  önermenin çöküşü
```
İkisi de verdict'in ilk satırına yazılır; ortalama ne olursa olsun.
