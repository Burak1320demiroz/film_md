# 🖼️ T5 — ARKA PLAN KALİTE TABLOSU (derin tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 24.08.2026 — DERİN TARAMA sınıfının ilk iki merceğiyle birlikte
>
> **Ne ölçer:** "Ön plan sahneyi taşırken arka alan yerinde duruyor mu."
> Öznenin ÜZERİNDEKİ hiçbir şey buraya girmez — rubrik özneyi yalnız
> dışlamak için adlandırır. Model sadakat bütçesini özneye harcar; bu
> mercek bir koşuyu tamamen ÖZNEYE BAKMAMAYA harcar.
>
> ```
> KATEGORİLER  1 figür bütünlüğü · 2 figür davranışı · 3 kalabalık sayısı
>              · 4 ufuk+topoloji · 5 derinlik/paralaks/ölçek · 6 arka set
>              · 7 odak dürüstlüğü · 8 gökyüzü · 9 kadraj kenarları
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
Bu bir DERİN TARAMA merceğidir, dört zorunlu merceğin (①-④) yanına
BEŞİNCİ zorunlu olarak eklenmemiştir:
· 00_INDEX tamlık matrisi /4 kalır; bu tablonun satırı matrise İŞLENMEZ
· Skorları T1-T4 skorlarıyla TOPLANMAZ ve KARŞILAŞTIRILMAZ — ayrı alet
  sınıfı, ayrı skor evreni
· Ne zaman koşulur: film arka plan riskini taşıyorsa — kalabalık /
  ikinci figür (risk kartı 4) · katmanlı-bölgeli dünya (kart 6b) ·
  yoğun set/şehir dokusu. Ya da bir çekirdek mercek arka alanda bir
  şey sezip OUT-OF-SCOPE FLAG bıraktıysa.
· Bulgu sahipliği: çekirdek merceğin kapsamına da oturan bulgu film
  kaydına ÇEKİRDEK SAHİBİN bölümüne yazılır ("⑤ taraması buldu" notuyla);
  yalnız bu merceğin kapsamındaki bulgu ⑤ bölümünde kalır. İki mercek
  aynı olayı gördüyse bu çifte fatura değil ÇAPRAZ DOĞRULAMADIR —
  film kaydında tek satır, iki kaynak.
```

## 📏 BU TABLOYU OKUMA KURALLARI

```
Ⓥ   Bu rubrik HER ZAMAN video-only koşar; bütün satırlar fiilen Ⓥ'dir
    ve ayrıca işaretlenmez.
🚨   GEÇERSİZ — koşu bir kapıdan geçmedi (sahne sayısı tutmadı, yanlış
    materyal). Satır üstü çizili durur.
—    Kategori N/A veya UNVERIFIABLE: boş bırakılır. ASLA 0 yazılmaz.
⚠️P  ⚠️ PARTIAL — kanıt 3 sahneden az; bulgu durur, sayı girmez.
```

⚠️ **ÖLÇÜM SAPMASI:** bu mercek için henüz ölçülmedi (0 koşu). Çekirdek
merceklerde aynı film iki koşuda 2 puana kadar oynadı; 1.5'ten küçük
farkı burada da fark sayma.

---

## 📊 SKOR TABLOSU

| Film | Tarih | Figür Büt. | Figür Dav. | Kalabalık | Ufuk | Derinlik | Arka Set | Odak | Gökyüzü | Kenarlar | Toplam | Verdict |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|

| **The Iron Slope** Ⓥ ⚠️ | 25.08.2026 | — | — | — | 3 | 3 | 3 | 4 | (6) | 4 | **3,8** | FIELD COLLAPSES |

| **The Rose Coat** ⚠️ | 26.08.2026 | — | — | — | (5) | (7) | ⬜ | ⬜ | (6) | — | **—** | ⑩'DAN GEÇMEDİ |
| **The Payload** Ⓥ ⛔ ⚠️ | 01.09 | 2 | — | — | 4 | 8 | 4 | 9 | 7 | 10 | **6,3** | ⬜ |
| **The Skylight** Ⓥ ⛔ | 29.08 | — | — | — | 5 | 10 | 6 | 10 | 8 | 10 | **8,2** | ⬜ |
| **The Still Swarm** Ⓥ ⛔ ⚠️ | 02.09 | 3 | 4 | — | 4 | 5 | 5 | — | — | 5 | **4,3** | ⬜ |
| **The Thin Roof** Ⓥ ⛔ ⚠️ | 28.08 | — | — | — | 7 | — | 7 | — | — | 8 | **7,3** | ⬜ |
| **The Upward Fall** Ⓥ ⛔ ⚠️ | 04.09 | 6 | 5 | 6 | 3 | 5 | 4 | 5 | 6 | 6 | **5,1** | ⬜ |
| **The Healing Ground** Ⓥ ⛔ ⚠️ | 04.09 | — | — | — | 10 | 10 | 4 | 10 | 10 | 10 | **9,0** | ⬜ |
| **The Counted Turn** ⚠️ | 09.09.2026 | — | — | — | — | 7 | — | — | — | — | **7,0** | FIELD HOLDS |
| **The Solar Mirror** Ⓥ ⚠️ | 11.09.2026 | 3 | 4 | — | 4 | 5 | 4 | 6 | 4 | 5 | **4,4** | SUBJECT DUPLICATE IN FIELD |
| **The Resonant Strand** Ⓥ ⛔ ⚠️ | 11.09 | — | — | — | 9 | 9 | 9 | 10 | 8 | 6 | **8,5** | ⬜ |
| **The Hard Dock** Ⓥ ⚠️ | 12.09.2026 | — | — | — | 5 | 6 | 6 | 7 | 7 | 7 | **6,3** | FIELD DRIFTS BUT RECOVERABLE |
| **The Silent Perihelion** Ⓥ ⛔ | 13.09 | — | — | — | 7 | 8 | 8 | 8 | 7 | 9 | **7,8** | ⬜ |
| **The Shattered Breath** Ⓥ ⛔ ⚠️ | 13.09 | — | — | — | 8 | 9 | 8 | 10 | 8 | 7 | **8,3** | ⬜ |
| **The Locked Pulse** Ⓥ ⛔ ⚠️ | 14.09 | — | — | — | 8 | 8,5 | 4 | 8,5 | — | 6 | **7,0** | ⬜ |


> **The Rose Coat · 26.08.2026 · belgesiz koşu · ⚠️ ŞARTLI · matrise girmez**
> Kayıt: [`01_FILM_RAPORLARI/THE_ROSE_COAT.md`](01_FILM_RAPORLARI/THE_ROSE_COAT.md)
> · Raporun toplamı 6,0 · hükmü `FIELD DRIFTS BUT RECOVERABLE`.
> · **Altı hücrenin dördü tek bir tasarım kararından geldi** [D133]: bu bir
> YAKLAŞMA filmi ve planın metinsiz sayaçlarından biri **pada mesafe
> 600 → 0 m, monotonik.** Ufuk (0:30 = 500 m ↔ 1:00 = 30 m) · Derinlik
> (120 m ↔ 30 m) · Arka Set (120 m ↔ 0 m) — üçü de "kamera yaklaştı".
> · **Gökyüzü (6)** ①'in 0:22 bulgusuyla AYNI GÖZLEM; sahibi ① [D108].
> · **Kenarlar `—`:** hücre "no in-scope source" yazıp 7/10 koymuştu;
> D119'un tahkim cümlesi uygulanmamıştı, artık kaynaksız hücre sayı
> taşımıyor [D131].
> · ⭐ SPEC dağıtım tablosu ⑤ ve ⑥'yı hiç tanımıyordu (24.08'de açıldılar);
> yedi SPEC dosyasının dördüne satır eklendi [D133].
> · **Şerit çelişkisi:** ⑤ `1111111111111` yazdı, öteki üçü
> `-111111111111`; ⑤'in KENDİ envanterinde S1'de figür yok [D135].

> **The Iron Slope · Ⓥ mod V · ⚠️ ŞARTLI** — matrise İŞLENMEZ (/4 payda korunur)
> Kayıt: [`01_FILM_RAPORLARI/THE_IRON_SLOPE.md`](01_FILM_RAPORLARI/THE_IRON_SLOPE.md)
> · ⛔ **Merceğin kendi işi ıskalandı:** envanter altı sahnenin altısında da
> `FAR FIELD: Black space, star field` yazdı; S2'de (20-30 s) kadrajın alt
> üçte birini bir GEZEGEN kaplıyor ve gezegen planın 12 negatif bloğunun
> 12'sinde yasaklıydı. **Gökyüzü (6)** hücresi bu yüzden parantezlidir.
> → **DERS 126** + rubrik yaması (en büyük nesne adlandırılır).

> **The Counted Turn · 09.09.2026 · MOD D · ⚠️ ŞARTLI · matrise girmez**
> Kayıt: [`01_FILM_RAPORLARI/THE_COUNTED_TURN.md`](01_FILM_RAPORLARI/THE_COUNTED_TURN.md)
> · `rapor_kontrol.py` ile düzeltildi: Kusur bildirilmeyen 4 kategori (10/10) `—` hücresine çekildi [D186]. Düzeltilmiş ortalama: **7,0** (Ham: 9,4/10).
> · Verdict: `FIELD HOLDS`. Tek kusur 00:40 ve 01:30'da düz-plaka paralaks (starfield ve kemerlerin aynı hızda kayması).

> **The Solar Mirror · 11.09.2026 · Ⓥ mod V · ⚠️ ŞARTLI · matrise girmez**
> Kayıt: [`01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md`](01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md)
> · Skor: **4,4/10** (Ⓥ mod V). Verdict: `SUBJECT DUPLICATE IN FIELD`.
> · S9 (01:20) visual anomaly: Mirror reflection contains duplicate astronaut figure with desynced head rotation / identical second suit opposite primary astronaut.
