# 🗣️ ELEŞTİRİ PROTOKOLÜ — bütün eleştirmen ajanların ortak biçimi

> Okuyan: dramaturg · izleyici (kısaltılmış hâli kendi dosyasında) · teknik-danisman ·
> devamlilik · bilim-danismani · denetci · ve eleştirmen olarak çağrılan her ajan.
> Ana ajan bu biçimde gelmeyen eleştiriyi bir kez geri gönderir; ikinci kez gelmezse
> eleştiri `ODA/`'ya "biçim dışı" notuyla kaydedilir ve kullanılmaz.

## 1. Bulgu biçimi

**v2 (16.10.2026 — bundan sonraki bütün eleştiriler).** Neden: bugüne kadarki "kök neden" cümlelerinin bir kısmı prompta bakılmadan
yazılmıştı ve çürüdü (WRONG_BURN C11 "yanlış klip seçildi" denmişti, prompt o hareketi istiyordu); "devamlılık kötü" gibi yeri ve
düzeltmesi olmayan bulgu kimseye iş vermedi.

```
### B<n> · <ÖLÜMCÜL | CİDDİ | KÜÇÜK> · <kısa başlık>
YER       çekim + saniye (C07 3-4 s) · kare adı · ya da dosya:satır — bulgunun tam yeri
KANIT     eserden BİREBİR alıntı (prompt, tablo, replik) ya da karede görülen (kare adıyla); alıntısız bulgu geçersizdir
ETKİ      izleyici ya da üretim için ne bozulur — tek cümle
DOĞDUĞU   metin · kare · hareket · seçim · kurgu · anlatım · ses · araç (AGENTS §3; F1-F6'da çoğunlukla "metin")
KURAL     dayandığı yazılı kural: dosya:satır + tür [SÖZLEŞME | ARAÇ | HİPOTEZ | TERCİH] (AGENTS §1b) · yoksa "—"
ARIZA     uretim_hatti/ARIZA_LISTESI.md'den eşleşen madde (H01…/T01…) ya da "yeni"
DÜZELTME  en küçük değişiklik: `eski metin` → `yeni metin` · ya da "kesme 3.2 s'den önce" · "çekimi ikiye böl"
          (aynı uzunlukta ya da daha kısa; "daha iyi yaz" düzeltme değildir)
```
v1 biçimi (`KANIT · NEDEN · ARIZA · ÖNERİ`) 16.10.2026'dan önceki ODA dosyalarında geçerli kalır; NEDEN = ETKİ, ÖNERİ = DÜZELTME.

**Şiddet:**
- **ÖLÜMCÜL:** bu hâliyle film izlenmez, anlaşılmaz ya da üretilemez. Tur kapanmaz.
- **CİDDİ:** belirgin kalite kaybı. Yazar ya düzeltir ya da gerekçeyle reddeder.
- **KÜÇÜK:** cila. Ana ajan yeni tur açmadan birleştirebilir.

## 2. Yasaklar

- **Puan yok.** Ölçüldü: aynı rubrik aynı filmi iki kez ölçünce ±1,3 puan oynadı.
- **"Genel olarak iyi" yok.** Övgü bulgu değildir. Korunması gereken bir şey varsa
  `KORU:` satırıyla, kanıtıyla yazılır.
- **Kota yok.** "Mutlaka üç sorun bul" kuralı yoktur. Bulgu yoksa: `BULGU YOK — çünkü …`
  (neye baktığını ve neden temiz bulduğunu yaz).
- **Yazarın gerekçesine itibar yok.** Yalnız eseri değerlendir. Gerekçe sana verilmez;
  verilmişse yok say.
- **Kapsam dışına çıkma.** Kendi listende olmayan konuyu `KAPSAM DIŞI:` satırıyla tek
  cümle bırak, bulgu yazma.
- **(16.10.2026) Liste varsa hepsi cevaplanır.** Dosyanda numaralı soru listesi olan eleştirmen (devamlilik F5 8 soru · kurgucu F3
  7 soru) her soruyu ayrı cevaplar: `evet/hayır · kanıt`. Olmayan cümle de bulgudur: "rozet tutarlı" demek, rozet konumunun hiç
  yazılmadığı 12 çekimi kaçırdı (FURNACE G04). Atlanan soru = eksik eleştiri.
- **(16.10.2026) Sayı sayımdan gelir.** Oran ve yüzde yalnız sayılmış bir kümeden yazılır, paydasıyla (`7/24`). Tahmin `≈` ve
  "tahmin" sözüyle. Paydası olmayan yüzde biçim dışıdır (değerlendirme raporlarında uydurma yüzdeler bulundu).
- **(16.10.2026) Görülmeyen temiz değildir.** Kareyle çalışan eleştiri hangi kareleri gördüğünü `GİRDİ`'ye yazar. Birkaç temiz kare,
  videonun hareket boyunca temiz olduğunu kanıtlamaz: hareket için "görülmedi" yaz.
- **(16.10.2026) Simülasyon insan değildir.** Ajanın "izleyici şöyle hisseder" tahmini İZLEME tablosuna ya da dış izleyici
  satırına yazılmaz (WRONG_BURN ve SKY_CATCH'in İZLEME tablosunda "dış izleyici" satırları AI simülasyonuydu, 11_SUZME §B).

## 3. Tur kuralı

- Tur, ÖLÜMCÜL bulgu kalmayınca kapanır.
- Yazar her bulguya cevap verir:
  - `B<n> KABUL — ne değişti`
  - `B<n> RED — gerekçe`
- 2. ve sonraki turda eleştirmene yalnız değişen kısım + önceki bulgular + yazarın
  cevapları gider. Eleştirmen yalnız şuna bakar: KABUL edilenler gerçekten uygulanmış mı,
  RED gerekçesi tutuyor mu, değişiklik yeni bir ÖLÜMCÜL doğurmuş mu.
- Tavan: hikâye odası 3 tur, diğer fazlar 2 tur. Tavanda hâlâ ÖLÜMCÜL varsa karar ana
  ajanındır (Fable); gerekçe `ODA/DURUM.md`'ye yazılır ve yayın onayında sahibe gösterilir.

## 4. Çıktının sonu

```
ÖZET     ÖLÜMCÜL n · CİDDİ n · KÜÇÜK n
KARAR    TUR KAPANABİLİR | TUR KAPANAMAZ (ÖLÜMCÜL: B…)
GİRDİ    bu eleştiri hangi dosyaları/metni gördü (eksik girdi varsa: "EKSİK: …")
YAPILMADI  (isteğe bağlı) görevin girdisi olmayan ya da bu fazda henüz var olmayan şeyler, yapılamayan ek kontroller
```

`GİRDİ` satırı zorunludur. Eski hattın uyum merceği 20 koşunun 20'sinde girdisiz çalıştı
ve bunu kimse görmedi. Eksik girdiyle yapılan eleştiri denetçi tarafından geçersiz sayılır.

**EKSİK ne demek (07.10.2026):** yalnız görev metninin verdiği bir girdi açılamadıysa ya da eksik geldiyse yazılır.
Denetçi bunu mekanik ❌ sayar (KABUL Ö2). Şunlar EKSİK değildir, `YAPILMADI` satırına yazılır:
- görevin girdisi olmayan dosyalar (öteki eleştirmenlerin çıktıları dahil; onları okumamak bağımsızlığın gereği);
- bu fazda henüz var olmayanlar (faz 2'de çekim listesi, faz 4'ten önce müzik planı);
- yapılamayan ek kontroller (kulakla dinleme, çalışmayan bir tarama).

Kanıt: HELMET_TO_HELMET'te iki eleştiri (F2 ses-tasarimcisi, F3 teknik-danisman) bu maddeleri EKSİK diye yazdı ve kapı mekanik olarak düştü.
