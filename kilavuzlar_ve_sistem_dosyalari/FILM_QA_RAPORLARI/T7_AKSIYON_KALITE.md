# 🎯 T7 — AKSİYON KALİTE TABLOSU (risk tetikli tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/7_AKSIYON_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 01.09.2026 — aksiyon mercekleri sınıfının ilk yarısı
>
> **Ne ölçer:** "İzleyici ne olduğunu anlatabilir mi." Tek yöntemi ANLATIM
> CÜMLESİ: her beat için izleyicinin söyleyeceği cümle yazılır; cümle
> "sanırım / galiba" olmadan bitmiyorsa beat OKUNMUYOR demektir.
> ⭐ En pahalı deseni **AKSİYON ELİZYONU**: kesme hamlenin başında düşüp
> sonrasında açılır — beat hiç üretilmemiştir, kurgu üreticinin
> yapamadığını saklar. Bu tek bulgu ortalamadan bağımsız olarak verdict'i
> ACTION NEVER RENDERED yapar.
>
> ```
> KATEGORİLER  1 beat anatomisi · 2 hareket hâlinde coğrafya · 3 tehdit
>              yönü+yaklaşma · 4 temas okunabilirliği · 5 sonucun
>              görünürlüğü · 6 kameranın aksiyonla sözleşmesi · 7 niyet
>              · 8 bahis nesnesi · 9 fiziksel tempo+tırmanma
> ⑥ İLE SINIR  ⑥ "bu düşüş 1,1 s, öteki 2,8 s" (ARİTMETİK)
>              ⑦ "vuruşun bağlandığını göremedim" (OKUMA)
> TETİKLEYİCİ  KART 11 (sahne içi kesme) · KART 4 (ikinci figür) ·
>              KART 2 (canlı temas) · KART 6 (parçacık) · KART 8 (kamera)
> MAKİNE ÇIKTISI  BEAT STRING — sahne başına bir hane, uzunluk = kesme+1;
>              rapor_kontrol.py doğrular
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
①-④ dört zorunlu merceğin yanına BEŞİNCİ zorunlu olarak eklenmemiştir.
Risk TETİKLİ taramadır: filmin risk kartlarında yazılı satır varsa koşulur.
Skoru T1-T4 ile TOPLANMAZ ve KARŞILAŞTIRILMAZ — ayrı eksen, ayrı tablo.

⚠️ "Opsiyonel mercek koşulmaz" (34 kaydın 5'inde ses vardı). Bu merceğin
farkı: tetikleyicisi tercih değil, risk kartında ZATEN yazılı satırdır.
```

## ⛔ SATIR YAZMADAN ÖNCE

```
1. ⑪ ölçüm kapısı koşuldu mu (master ölçüldü mü)
2. rapor_kontrol.py GEÇERSİZ / TEKRAR dönmedi mi
   python3 ../RAPOR_KONTROL/rapor_kontrol.py <rapor> --film <FILM>
3. ARITHMETIC GATE tutuyor mu (n · Σ · Σ/n rapordan yeniden hesaplandı mı)
4. SPEC varsa rapor MODE D mi [D129]
Biri bile hayırsa satır YAZILMAZ; ham rapor 02_HAM_RAPORLAR/'da durur.
```

---

## 📊 TABLO

| Film | Tarih | Mod | Beat anat. | Coğrafya | Tehdit | Temas | Sonuç | Kamera | Niyet | Bahis | Tempo | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| *(henüz koşu yok)* | | | | | | | | | | | | | |

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
