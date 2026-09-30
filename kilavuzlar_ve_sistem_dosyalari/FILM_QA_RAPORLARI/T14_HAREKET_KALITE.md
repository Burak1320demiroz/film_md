# 🧍 T14 — HAREKET KALİTE TABLOSU (hareket mantığı · risk tetikli tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/14_HAREKET_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 14.09.2026 — sahip talebi: *"filmlerde saçma sapan hareketler yapıyorlar"*.
> Ölçüm: ① KARE'nin **Motion Quality** kategorisi 24 filmde düşük çıktı ve o örüntünün
> dersi yoktu (`ders_frekans.py`); ⑦ AKSİYON olayın okunup okunmadığını, ⑥ FİZİK sayıyı,
> ⑩ OYUNCULUK niyeti ölçüyordu — **hareketin NEDENİ** kimsenin değildi.
>
> **Ne ölçer:** "Beden bunu NEDEN yaptı — cevabı ekranda mı?" Tek yöntemi AMAÇ CÜMLESİ:
> her hareket için izleyicinin söyleyeceği cümle yazılır ("vizörü parlamadan korumak
> için sol kolunu kaldırır"); cümle "sebepsiz / galiba" olmadan bitmiyorsa hareket
> AMAÇSIZDIR. Kapalı etiket seti: PURPOSEFUL · PURPOSELESS · LOOP · SLIDE · SPIN ·
> PHANTOM · MISGRIP · ABANDONED · CONTRADICTION · PUPPET · DISSOCIATED · MISREACTION ·
> OVERGESTURE. ⭐ Ürünü **PROMPT ORDERS** tablosudur: her bulgu sonraki filmin promptuna
> girecek POZİTİF bir satıra çevrilir — bu tablo Kart G'nin ham maddesidir.
>
> ```
> KATEGORİLER  1 amaç okunurluğu · 2 yürüyüş mantığı · 3 dönüş/rotasyon ·
>              4 el ve nesne · 5 döngü/tekrar · 6 tamamlama · 7 beden bütünlüğü ·
>              8 tepki mantığı
> SINIRLAR     ⑦ "ne oldu" (okuma) · ⑥ "kaç saniye" (sayı) · ⑮ "doğru yöne mi"
>              (vektör) · ⑩ "ne hissetti" (niyet) · ① tek karede anatomi (artefakt)
>              ⑭ yalnız "kol NEDEN kalktı"
> TETİKLEYİCİ  her filmde koşulabilir; öncelik: ① Motion Quality ≤ 6 · ⑦/⑩ OUT-OF-SCOPE
>              flag'inde "amaçsız hareket" · uzun sabit çekim (döngü riski) · el işi
>              yoğun sahne · sıfır-g / dönme yerçekimi (PREMISE REGISTER zorunlu)
> MAKİNE ÇIKTISI  PURPOSE STRING — sahne başına bir hane (P/m/x/-), uzunluk = kesme+1;
>              rapor_kontrol.py doğrular · MOVEMENTS LOGGED ≥ PURPOSELESS MOVEMENTS
> HÜKÜM        MOTION MAKES SENSE / MINOR TWITCHES / FIXABLE IN EDIT / PUPPET MOTION /
>              MOTION WITHOUT PURPOSE (rapor_kontrol ①.13 sözlükle kıyaslar)
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
Risk tetikli taramadır (⑤-⑧ sınıfı). Skoru T1-T4 ile TOPLANMAZ ve KARŞILAŞTIRILMAZ.
Mod V koşusu meşrudur (Ⓥ) — SPEC varken mod V → ⛔ ÖN KOŞU, tabloya girmez [D129].
```

## ⛔ SATIR YAZMADAN ÖNCE

```
1. ⑪ ölçüm kapısı koşuldu mu (master ölçüldü mü)
2. rapor_kontrol.py GEÇERSİZ / TEKRAR / KESİK dönmedi mi
   python3 ../RAPOR_KONTROL/rapor_kontrol.py <rapor> --film <FILM>
3. SPEC varsa rapor MODE D mi [D129]
Biri bile hayırsa satır YAZILMAZ; ham rapor 02_HAM_RAPORLAR/<FILM>/<FILM>_HAREKET_HAM.md'de durur.
⛔ Sayılar bu tabloya ELLE yazılmaz — rapor_kontrol --t-tablo yazar (ortalama hücrelerden).
⚠️ ÖLÇÜM SAPMASI ±1,3 PUAN. 1,5'ten küçük fark, fark değildir. OVERALL ders gerekçesi
   değildir; ders yalnız timecode'lu, ≥2 filmde tekrarlayan bulgudan yazılır (kontrat §2b).
```

---

## 📊 TABLO

| Film | Tarih | Mod | Amaç | Yürüyüş | Dönüş | El/Nesne | Döngü | Tamamlama | Beden | Tepki | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **The Falling World** B2 ⚠️ | 19.09 | D | ⬜ | 23 | 8 | 7 | 8 | — | — | 8 | — | — | **7,8** | ⬜ |
| **The Inward Fall** | 30.09 | D | 6 | 7 | 6 | 6 | 7 | 6 | 7 | 6 | **6,4** | 🔴 **MOTION WITHOUT PURPOSE** — 3 adet x baskın sebepsiz hareket: 0:33 boşta sallanma (Desen ①), 0:53 nedensiz çömelme (Desen ⑧), 2:03 kaskın 180° savrulması (Desen ④) [D184] |
| **The Signal Keepers** ⚠️ | 30.09 | D | 7 | 8 | 8 | 7 | — | 8 | 8 | — | **7,7** | FIXABLE IN EDIT · M27 (3:45) phantom grab · M7 (0:44) abandoned temas · M24 (3:18) wrist twitch · M5/M10 zemin kayması |
| **The Static Veil** ⚠️ | 30.09 | D | — | — | — | — | — | — | — | — | **—** | MOTION MAKES SENSE · 23/23 PURPOSEFUL; Ay yerçekimi ve EVA giysisi kinesik kilitleri tam; 8 kategori kusursuz (10/10 → — uyarınca D186) [D184] |

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO/ŞARTLI döndükten sonra betik yazar [kural ① · D161].
