# 🪝 T12 — HOOK KALİTE TABLOSU (plan sadakati · yayın öncesi)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/12_HOOK_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 06.09.2026 — plan sadakati mercekleri sınıfı [D184]
>
> **Ne ölçer:** "Filmi SEÇMEMİŞ bir yabancı kalır mı — ve nerede gider." Üç pencere: AÇILIŞ (hook penceresinde SORU oluşuyor mu), PAYLAŞIM ANLARI (viral ara sahneler tek başına seyahat ediyor mu), ÇIKIŞ (son kare ilk kareye mi dönüyor, karta mı). Tek kalıcı çıktısı DROP-OFF PREDICTION: yabancının gittiği ÜÇ SANİYE, sabit listeden sebeple — yayın sonrası gerçek tutundurma eğrisiyle kıyaslanır. ⭐ Bu mercek KESME ÖNERMEZ; saniye söyler. ④'ün kesme listesi filmin doruğunu kesmeyi önerdi; bu mercek "3:12'de kalır" der.
>
> ```
> KATEGORİLER  1 hook sorusu · 2 kapak saniyesi · 3 ilk paylaşım anına kadar risk · 4 paylaşım anları tek başına · 5 plato · 6 doruk yerleşimi · 7 çıkış ve dönüş · 8 format uyumu
> TETİKLEYİCİ  yayınlanacak her film (kart Y) — yayından ÖNCE koşulur, tahmini 08_YAYIN_PERFORMANS_TABLOSU'na kopyalanır
> MAKİNE ÇIKTISI  DROP-OFF PREDICTION — üç saniye + sebep; rapor_kontrol.py üç saniye ve sabit-liste sebebini sayar
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

| Film | Tarih | Mod | Hook|Kapak|Risk|Paylaşım|Plato|Doruk|Çıkış|Format | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| *(henüz koşu yok)* | | | | | | | | | | |  | |

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
