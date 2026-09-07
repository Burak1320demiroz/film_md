# ⚖️ T6 — FİZİK KALİTE TABLOSU (derin tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/6_FIZIK_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 24.08.2026 — DERİN TARAMA sınıfının ilk iki merceğiyle birlikte
>
> **Ne ölçer:** "Dünyanın davranışı ÖLÇÜMDEN sağ çıkıyor mu." Tek sayısal
> mercek: düşüş süreleri kare kare ölçülür, görünür yerçekimi hesaplanır,
> mod D'de planın SAYISAL KİLİTLERİ ekranda tek tek doğrulanır (PASS /
> FAIL / UNMEASURABLE / NOT EXERCISED). ⭐ Depoda planlara yazılan onlarca
> sayısal kilidi üretilmiş videoya karşı doğrulayan İLK alet budur.
>
> ```
> KATEGORİLER  1 yerçekimi+düşüş · 2 balistik · 3 çarpma+momentum
>              · 4 malzeme · 5 parçacık+atmosfer · 6 ölçek+ölçüm
>              · 7 hız+zamanlama · 8 ışık+gölge fiziği · 9 biyomekanik
> ÖNERME KAPISI rubriğin İÇİNDE yapısal (STEP 0 PREMISE GATE): filmin
>              dünya kuralı ilan ettiği imkânsız fizik bulgu DEĞİLDİR,
>              yalnız tutarlılığı puanlanır — D87/D116 kapısının rubrik
>              tarafındaki karşılığı.
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
Bu bir DERİN TARAMA merceğidir, dört zorunlu merceğin (①-④) yanına
BEŞİNCİ zorunlu olarak eklenmemiştir:
· 00_INDEX tamlık matrisi /4 kalır; bu tablonun satırı matrise İŞLENMEZ
· Skorları T1-T4 skorlarıyla TOPLANMAZ ve KARŞILAŞTIRILMAZ
· Ne zaman koşulur: filmin novum'u bir fizik iddiasıysa, planı sayısal
  kilit taşıyorsa (mod D ile), parçacık/toz riski varsa (risk kartı 6)
  ya da bir çekirdek mercek fizikte bir şey sezip OUT-OF-SCOPE FLAG
  bıraktıysa. Mod D bu merceğin varlık sebebidir: SPEC'in sayı satırları
  NUMERIC LOCK LIST'e kopyalanır.
· Bulgu sahipliği: ① KARE "toz sıvı gibi akıyor" DESENİNİN, ② DEVAMLILIK
  "orada hızlı burada yavaş" KARŞILAŞTIRMASININ sahibidir; ⑥ yalnız
  SAYI taşıyan bulgunun ("14 m'lik düşüş 3.2 s sürüyor — kurulu g'de
  2.0 olmalıydı"). Çekirdek kapsamına da oturan bulgu film kaydına
  çekirdek sahibin bölümüne yazılır ("⑥ taraması buldu" notuyla).
  İki mercek aynı olayı gördüyse film kaydında tek satır, iki kaynak.
```

## 📏 BU TABLOYU OKUMA KURALLARI

```
Ⓥ   MOD V — kilit listesi verilmeden koşuldu; film kendisiyle + gerçek
    fizikle ölçüldü. GRAVITY ESTIMATE raporun kendi hesabıdır.
(D) MOD D — plan kilitleri verildi; satırın yanına NUMERIC LOCK sonucu
    yazılır: "12 kilit: 9 PASS · 2 FAIL · 1 NOT EXERCISED" gibi.
🚨   GEÇERSİZ — koşu bir kapıdan geçmedi. Satır üstü çizili durur.
—    Kategori N/A veya UNVERIFIABLE: boş bırakılır. ASLA 0 yazılmaz.
⚠️P  ⚠️ PARTIAL — kanıt 3 olaydan az; bulgu durur, sayı girmez.
TWO GRAVITIES verdikti her skoru ezer ve satırın ilk kelimesi olur.
```

⚠️ **ÖLÇÜM SAPMASI:** bu mercek için henüz ölçülmedi (0 koşu). 1.5'ten
küçük farkı burada da fark sayma.

---

## 📊 SKOR TABLOSU

| Film | Tarih | Mod | Yerçekimi | Balistik | Momentum | Malzeme | Parçacık | Ölçek | Hız/Zaman | Işık/Gölge | Biyomek. | Toplam | Kilit Sonucu | Verdict |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|---|

| **The Iron Slope** Ⓥ ⛔ ⚠️ | 25.08.2026 | V (D olacaktı) | 3 | — | — | 10 | — | 8 | 10 | 10 | (4) | **7,5** | mod V — kilit tablosu yok | TWO GRAVITIES |

> **The Iron Slope · Ⓥ mod V · ⛔ ÖN KOŞU · ⚠️ ŞARTLI** — matrise İŞLENMEZ
> Kayıt: [`01_FILM_RAPORLARI/THE_IRON_SLOPE.md`](01_FILM_RAPORLARI/THE_IRON_SLOPE.md)
> · Bu mercek **mod D için vardır** ve kilitli bir filme mod V koşuldu; plan
> 20'den fazla sayısal kilit taşıyordu. · **Biyomekanik (4)** ortak adım ⑩'dan
> düştü: adamın ağır olması TASARIMDIR (0,220 g itki), 0 g değil — raporun
> "zero-g locomotion yaz" reçetesi filmin novum'unu silerdi.
> · Yerçekimi 3/10 **AYAKTA ve ölçümle doğrulandı**: serbest parça sabit
> ~0,15 m/s süzülüyor; kilit 3. saniyede 9,7 m istiyordu → mod D'de
> `VERDICT: FAIL`. → **DERS 127**
