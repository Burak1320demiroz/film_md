# 💡 T11 — IŞIK KALİTE TABLOSU (plan sadakati)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/11_ISIK_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 06.09.2026 — plan sadakati mercekleri sınıfı [D184]
>
> **Ne ölçer:** "Işık klipten klibe kendiyle uyuşuyor mu, ve yalnız planın dediği sınırda mı değişiyor." Tek yöntemi: her kesmede çıkan klibin son karesi ile giren klibin ilk karesi yan yana — "ışıkta ne değişti?" Aynı bölge içinde değişim = IŞIK SIÇRAMASI; ilan edilmiş sınırdaki değişim = PASS. ⭐ Ortam yasayı koyar: vakumda pus, bloom, kaldırılmış gölge bulgudur. Lambanın VARLIĞI ②/⑤'in, YANIP yanmadığı ve düşürdüğü ışık bu merceğin.
>
> ```
> KATEGORİLER  1 anahtar ışık yönü · 2 gölge kalitesi + dolgu · 3 renk ısısı · 4 pratik kaynaklar (sayı · yanık/sönük) · 5 kesmede pozlama · 6 klip içi kararlılık · 7 bölge sınırları · 8 atmosfer dürüstlüğü
> TETİKLEYİCİ  SPEC'te IŞIK TAKVİMİ kaydı · ya da ≥12 klipten kurulu her kurgu
> MAKİNE ÇIKTISI  KEY DIRECTION STRING — sahne başına saat konumu; LIGHT JUMP LOG kesme başına
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

| Film | Tarih | Mod | Yön|Gölge|Isı|Kaynak|Pozlama|Klip içi|Sınır|Atmosfer | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| *(henüz koşu yok)* | | | | | | | | | | |  | |

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
