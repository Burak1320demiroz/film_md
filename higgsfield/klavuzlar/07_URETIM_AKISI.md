# 🏭 ÜRETİM AKIŞI — iterasyon disiplini ve maliyet

> **Kaynak:** Kullanıcının hazırladığı araştırma raporu — *"Higgsfield AI
> Ekosisteminde Hatasız Görüntü ve Video Üretimi"* (sohbete yapıştırıldı)
> **Alındığı tarih:** 03.08.2026
> **Doğrulama:** ❌ denenmedi
> **Kapsam:** Yazılmış `.md` filmden bitmiş klibe giden yolun **araç tarafı**:
> hangi sırayla üretilir, hata çıkınca ne değiştirilir, para nasıl harcanmaz.
> **CEVAPLAMADIĞI şeyler:** CLI komutlarının kendisi (→ `03_KOMUT_REFERANSI.md`,
> henüz yazılmadı), kuyruk süresi, eşzamanlı iş limiti, çıktının nereye indiği.

---

## 🚨 BU DOSYANIN VAR OLMA SEBEBİ

03.08.2026'da THE HOLDING FIELD üretildi ve 6 sahne yeniden üretilmek zorunda
kaldı. Rapor, bu israfın **tamamen önlenebilir** olduğunu söyleyen üç kural
içeriyor ve üçü de bu depoda **yazılı değildi.**

```
DEPODA OLMAYAN ÜÇ KURAL
  1. Tek değişken kuralı  — bir seferde tek şey değiştirilir
  2. Ucuz taslak          — pahalı modelde ilk deneme yapılmaz
  3. Tohum sabitleme      — seed sabitlenmezse her üretim yeni başlangıç
```

---

## 1. 🔬 İTERASYON KURALI — tek değişken

> **Rapor:** *Bir şeyler ters gittiğinde modeli, referans görseli ve metin
> istemini AYNI ANDA değiştirmeyin. Her seferinde tek bir değişkeni
> değiştirin. Aksi hâlde sorunun hangi düzeltmeyle çözüldüğü asla
> anlaşılamaz ve bilimsel, tekrarlanabilir bir iş akışı sağlanamaz.*

Bu, depodaki en pahalı boşluk. `01_DERS_ETKINLIK_RAPORU.md` zaten şunu
ölçmüştü: **50 dersin 36'sı ÖLÇÜLEMEDİ.** Sebep tam olarak bu — dersler
tek tek değil, toplu hâlde uygulandı, hangisinin işe yaradığı bilinmiyor.

```
DOĞRU İTERASYON — bir kerede bir şey
  Deneme 1  : orijinal prompt                     → sonuç kaydedilir
  Deneme 2  : YALNIZ kamera satırı değişti        → sonuç kaydedilir
  Deneme 3  : kamera geri alındı, YALNIZ kıyafet  → sonuç kaydedilir

YANLIŞ İTERASYON — bu depoda şimdiye kadar yapılan
  Deneme 1  : prompt + model + negatif blok aynı anda değişti
  → Düzeldi ama neden düzeldiği bilinmiyor → ders yazılamaz
```

**Kayıt zorunluluğu:** her denemede ne değiştiği yazılmazsa kural işe
yaramaz. Üretim notu bloğuna (AGENTS görev kartı B) satır eklenir:

```
DENEME KAYDI
| # | Değişen tek şey | Sonuç | Karar |
|---|---|---|---|
| 1 | — (temel)       | yükselme hatası | ret |
| 2 | "hang" → "descend" | düzeldi     | kabul |
```

---

## 2. 💸 UCUZ TASLAK — pahalı modelde ilk deneme yapılmaz

> **Rapor:** Premium modeller (Sora 2, Veo 3.1) video başına ~40-70 kredi;
> Kling 3.0 ve Wan 2.6 çok daha düşük. Yüksek maliyetli render almadan önce
> kompozisyonu ve promptun çalışıp çalışmadığını görmek için Turbo/Fast
> varyantları ya da 720p düşük çözünürlüklü testler kullanılmalı.
> İstem kilitlendiğinde tam çözünürlüklü asıl model çalıştırılır.

```
BU DEPODA NE DEMEK
  14 sahnelik bir film × ortalama 3 deneme = 42 üretim.
  Hepsi Veo 3.1'de (~55 kredi) = ~2.310 kredi
  Taslaklar Kling 3.0'da (~6 kredi), yalnız onaylananlar Veo'da:
     28 taslak × 6  =   168
     14 final  × 55 =   770
                      ─────
                       938 kredi   → ~%60 tasarruf

⚠️ Sayılar RAPORDAN, doğrulanmadı. Oran gösterge amaçlı.
```

**Depodaki mevcut kural zaten uyumlu:** `KILAVUZ_REHBERI §6 adım 5` —
*"önce imaj, onaylanınca video; onaylanmamış imajdan video üretme, boşa
gider."* Rapor bunu bir adım öteye taşıyor: **onaylanmamış promptdan pahalı
video üretme.**

---

## 3. 🌱 TOHUM SABİTLEME (seed)

> **Rapor:** Nesiller arası kompozisyonu ve kimliği korumanın temel
> tekniklerinden biri rastgele "seed" değerini sabit tutmaktır. Aksi hâlde
> model her seferinde farklı bir başlangıç noktası alır.

```
DEPODAKİ DURUM
  SAHNE_DEVAMLILIK_KILAVUZU.md seed'den bahsediyor ama hiçbir film
  dosyasında kayıtlı bir seed YOK. 41 filmin 41'inde boş.
  → Üretim notu bloğuna zorunlu alan olarak eklenmeli:
    SEED: <değer>   ·   her sahnede aynı mı, farklı mı
```

⚠️ Higgsfield'de seed parametresinin var olup olmadığı **bilinmiyor** —
rapor genel difüzyon pratiğinden bahsediyor. Kurulumda kontrol edilecek.

---

## 4. ⏱️ 5-8. SANİYE KURALI — ölçümle çakışıyor

> **Rapor:** *Oluşturulan bir videonun sadece ilk bir saniyesine bakıp
> başarılı saymak hatadır. Çoğu kalite problemi (morfolojik bozulmalar,
> kaymalar) 5 ila 8. saniyeler arasında ortaya çıkar.*

```
BU DEPODAKİ DOĞRULAMA — bağımsız ve tam isabet
  Ders 57 (Deep Pressure): "00:00 vs 00:07 — yedi saniye sonra AYNI
  kesintisiz çekimde maske, regülatör ve sırt tüpü belirdi."
  Ders 46/49 (Inversion):  bozulma orta klipte.
  → Rapor bunu genel bir model davranışı olarak doğruluyor.

BİZİM KLİPLERİMİZ 10 SANİYE → tehlike bandı kliplerin %30-80'i.
```

**Uygulanacak kontrol — üretim sonrası, her klip için:**

```
□ 0. saniye ile 10. saniye karesini YAN YANA koy
□ Kıyafet/ekipman farkı var mı  (Ders 57)
□ Yüz kemik yapısı aynı mı      (Ders 16)
□ Kir/yıpranma yer değiştirdi mi (Ders 42)
□ 5-8 arası bandı ayrıca izle — hata en sık burada doğuyor

⚠️ Ders 57'nin ucuz çözümü hâlâ geçerli: morph başladığı yerden klibi kes.
   10 saniyelik klibin son 2 saniyesini atmak çoğu zaman bedelsiz.
```

---

## 5. 📋 ÖNERİLEN AKIŞ — kurulumdan sonra

```
0. FİLM DOSYASI HAZIR      .md yazılmış, prompt QA'sı geçmiş
1. TASLAK  (ucuz model)    1 sahne · 1 deneme · kompozisyon doğru mu
2. PROMPT KİLİDİ           hata varsa TEK değişken değiştir, tekrar dene
3. TASLAK SETİ             14 sahnenin 14'ü ucuz modelde
4. ONAY                    sahne haritası ekranda tutuyor mu
5. FİNAL RENDER            yalnız onaylananlar pahalı modelde
6. 0/10 KARE KARŞILAŞTIRMA her klip için (§4)
7. MONTAJ
8. QA                      VIDEO_QA → MANTIK_QA → SENARYO_QA
9. ÜRETİM NOTU             model · seed · deneme kaydı · red sebepleri
                           → AGENTS.md görev kartı B
```

---

## 6. 🔗 FİLM TARAFINA YAZILACAKLAR

Bu dosyadaki üç kural araç-bağımsız — yani Higgsfield'e geçilmese bile
geçerli. Kurulumdan sonra ilk denemede doğrulanırlarsa **film tarafına**
taşınacaklar:

```
□ LESSONS_LEARNED.md          → tek değişken kuralı bir DERS adayı
                                (ölçülemeyen 36 dersin kök nedeni)
□ AGENTS.md görev kartı B     → üretim notuna SEED + DENEME KAYDI alanı
□ KILAVUZ_REHBERI §6          → adım 5'e "ucuz taslak → pahalı final"
```

Ters yön yasak: bu dosya film kurallarını kopyalamaz, işaret eder.
