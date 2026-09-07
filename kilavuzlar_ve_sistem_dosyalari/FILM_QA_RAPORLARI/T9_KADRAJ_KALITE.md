# 🎯 T9 — KADRAJ KALİTE TABLOSU (plan sadakati)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/9_KADRAJ_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 06.09.2026 — plan sadakati mercekleri sınıfı [D184]
>
> **Ne ölçer:** "Kamera planın koyduğu yerde mi, o lenste mi, orada KALIYOR mu." Tek yöntemi: kare önce tarif edilir, harf sonra atanır; SETUP STRING planın KURULUM İSKELETİ ile yan yana konur. Kafiye çifti (ilk kare ↔ son kare) her filmde koşulur. ⭐ Diğer bütün mercekler kameranın İÇİNDEN özneye bakar; bu mercek kameranın kendisine bakar — Kept Light'ta S24'ün yanlış açısını sekiz merceğin hiçbiri yazmadı.
>
> ```
> KATEGORİLER  1 kurulum sadakati · 2 lockoff bütünlüğü · 3 kafiye çifti · 4 dönüş tutarlılığı · 5 küme dikişleri · 6 açı yayı + bilinçli şok · 7 ekran geometrisi
> TETİKLEYİCİ  SPEC'te KURULUM İSKELETİ satırı (yeni-film şablonu her filmde yazar)
> MAKİNE ÇIKTISI  SETUP STRING — sahne başına bir harf; rapor_kontrol.py uzunluğu ve plan iskeletiyle farkı basar
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
①-④ dört zorunlu merceğin yanına zorunlu olarak eklenmemiştir.
KOŞUL TETİKLİ plan sadakati taramasıdır: SPEC'te ilgili kayıt varsa koşulur.
Skoru T1-T4 ile TOPLANMAZ ve KARŞILAŞTIRILMAZ — ayrı eksen, ayrı tablo.
⛔ SPEC'siz (mod V) koşusu tanım gereği BOŞTUR: bu mercek planı ekrana karşı
okur; plan yoksa okuyacak şey yoktur. Mod V satırı bu tabloya YAZILMAZ.
```

## ⛔ SATIR YAZMADAN ÖNCE

```
1. ⑪ ölçüm kapısı koşuldu mu (master ölçüldü mü) · TESLİM SINIFI HAM ZİNCİR değil mi
2. rapor_kontrol.py GEÇERSİZ / TEKRAR dönmedi mi
   python3 ../RAPOR_KONTROL/rapor_kontrol.py <rapor> --film <FILM>
3. ARITHMETIC GATE tutuyor mu (n · Σ · Σ/n rapordan yeniden hesaplandı mı)
4. Rapor MODE D mi [D129] — bu tabloda mod V satırı yoktur
Biri bile hayırsa satır YAZILMAZ; ham rapor 02_HAM_RAPORLAR/'da durur.
```

---

## 📊 TABLO

| Film | Tarih | Mod | Kurulum|Lockoff|Kafiye|Dönüş|Dikiş|Açı yayı|Geometri | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| *(henüz koşu yok)* | | | | | | | | | |  | |

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
