# 🧭 T15 — YÖN KALİTE TABLOSU (yön ve hedef · risk tetikli tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/15_YON_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 14.09.2026 — sahip talebi: *"yanlış yere dönmek, ateş etmek vs."*
> ② DEVAMLILIK "kapak aynı tarafta mı" diye sorar, ⑦ AKSİYON "olay okunuyor mu",
> ⑩ OYUNCULUK "bakış ne anlatıyor", ⑨ KADRAJ "kamera nerede" — **figürün vektörü hedefe
> varıyor mu** sorusu kimsenin değildi.
>
> **Ne ölçer:** "Yönelmiş her eylem (bakış · dönüş · gidiş · uzanma · nişan · ateş/atış ·
> kaçış · itme) hedefine, filmin hedefi KOYDUĞU yere varıyor mu?" Tek yöntemi VEKTÖR
> CÜMLESİ: "0:12'de ekran-solda gösterilen kapağa doğru ekran-sola döner" — cümlede
> "ama" varsa ISKA. Kapalı eşleşme seti: HIT · MISS · UNKNOWN · NO TARGET · FLIP (180°
> kırılması). ⭐ Ürünü **PROMPT ORDERS** tablosudur: her ıska sonraki filmin promptuna
> EKRAN UZAYINDA (screen-left/right) pozitif bir satır olarak girer — pusula kelimesi yok.
>
> ```
> KATEGORİLER  1 hedefin kurulması · 2 bakış yönü · 3 dönüş ve gidiş yönü · 4 uzanma
>              ve nişan · 5 ateş/tetik/atış · 6 kesmeler arası ekran yönü · 7 kameraya
>              göre yön · 8 sonucun hedefe düşmesi
> SINIRLAR     ② "kapak taraf değiştirdi" (aynılık) · ⑦ "olay okunmadı" (okuma) ·
>              ⑭ "neden döndü" (amaç) · ⑩ "bakış ne anlatıyor" (niyet) · ⑨ kameranın
>              vektörü · ⑥ yörünge aritmetiği — ⑮ yalnız "figürün vektörü hedefe vardı mı"
> TETİKLEYİCİ  sabit hedefe hareket / koşu / yanaşma (UZAMSAL_HARITA §4 SPATIAL LOCK
>              taşıyan film) · kovalamaca · ateş/atış/itki içeren sahne · ikinci figür ·
>              dönme yerçekimi (PREMISE REGISTER zorunlu) · ② Spatial Geography ≤ 6
> MAKİNE ÇIKTISI  VECTOR STRING — sahne başına bir hane (H/m/x/-), uzunluk = kesme+1;
>              ACTS MISSED beşlisi = ACTS LOGGED; rapor_kontrol.py doğrular
> HÜKÜM        EVERY VECTOR LANDS / MINOR MISAIMS / FIXABLE IN EDIT / WRONG WAY /
>              AIMED AT NOTHING (rapor_kontrol ①.13 sözlükle kıyaslar)
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
Risk tetikli taramadır (⑤-⑧ sınıfı). Skoru T1-T4 ile TOPLANMAZ ve KARŞILAŞTIRILMAZ.
Mod V koşusu meşrudur (Ⓥ): hedefin yeri filmin KENDİ kurduğu yerdir; SPEC varken
mod V → ⛔ ÖN KOŞU, tabloya girmez [D129].
```

## ⛔ SATIR YAZMADAN ÖNCE

```
1. ⑪ ölçüm kapısı koşuldu mu (master ölçüldü mü)
2. rapor_kontrol.py GEÇERSİZ / TEKRAR / KESİK dönmedi mi
   python3 ../RAPOR_KONTROL/rapor_kontrol.py <rapor> --film <FILM>
3. SPEC varsa rapor MODE D mi [D129]
Biri bile hayırsa satır YAZILMAZ; ham rapor 02_HAM_RAPORLAR/<FILM>/<FILM>_YON_HAM.md'de durur.
⛔ Sayılar bu tabloya ELLE yazılmaz — rapor_kontrol --t-tablo yazar (ortalama hücrelerden).
⚠️ ÖLÇÜM SAPMASI ±1,3 PUAN. 1,5'ten küçük fark, fark değildir. OVERALL ders gerekçesi
   değildir; ders yalnız timecode'lu, ≥2 filmde tekrarlayan bulgudan yazılır (kontrat §2b).
```

---

## 📊 TABLO

| Film | Tarih | Mod | Hedef | Bakış | Dönüş/Gidiş | Uzanma/Nişan | Ateş/Atış | Kesme yönü | Kamera | Sonuç | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **The Falling World** B2 ⚠️ | 19.09 | D | ⬜ | 12 | 9 | — | 7 | — | — | 8 | — | 9 | **8,2** | ⬜ |
| **The Inward Fall** ⚠️ | 30.09 | D | — | — | — | — | — | — | — | — | **—** | ✅ **EVERY VECTOR LANDS** — 24/24 HIT; merkez kovan ve Coriolis savrulma yönleri tam kilitli; 8 kategori kusursuz (10/10 → — uyarınca D186) [D184] |
| **The Signal Keepers** | 30.09 | D | 10 | 10 | 10 | 10 | — | 10 | 10 | 10 | **10,0** | ✅ **EVERY VECTOR LANDS** — 24/24 HIT · sıfır sapma · bakış, el uzatma ve ilerleme mekânsal hedeflere tam kilitli [D184] |
| **The Static Veil** ⚠️ | 30.09 | D | 8 | — | 9 | — | — | 7 | 9 | — | **8,2** | WRONG WAY · V11 (01:50) S11 fener sağdan sola FLIP (Pattern ①/⑩) · 10/11 HIT · kurguda yatay flip ile çözülebilir [D184] |

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO/ŞARTLI döndükten sonra betik yazar [kural ① · D161].
