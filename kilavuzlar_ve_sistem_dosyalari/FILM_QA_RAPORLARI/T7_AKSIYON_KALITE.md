# 🎯 T7 — AKSİYON KALİTE TABLOSU (risk tetikli tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/7_AKSIYON_QA_CRITIQUE_PROMPT.md`
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
| **The Counted Turn** ⚠️ | 09.09.2026 | D | 8 | 9 | — | 4 | 7 | — | 9 | 9 | 8 | **7,7** | MINOR BLUR · 4 temas penetrasyonu (0:31, 1:43, 3:43), S21 eylemsiz beat |
| **The Solar Mirror** Ⓥ ⚠️ | 11.09.2026 | V | 9 | 9 | 8 | — | 9 | — | — | 9 | — | **8,8** | ACTION READS · B3 unmotivated energy ring, S2-S3 spatial jump |
| **The Resonant Strand** ⚠️ | 11.09 | D | 7 | 8 | 7 | 7 | 7 | 9 | 7 | 6 | — | **7,2** | ⬜ |
| **The Hard Dock** ⚠️ | 12.09.2026 | D | 8 | 9 | 9 | 8 | 9 | 10 | 10 | 8 | 8 | **8,8** | B4 docking impact elided by cut to cockpit |
| **The Falling World** B2 ⚠️ | 19.09 | D | 9 | — | — | 9 | — | — | — | — | — | **9,0** | ⬜ |
| **The Slow Rain** B2 ⚠️ | 22.09 | D | — | — | — | — | — | — | — | — | — | **—** | ⬜ |
| **The Inward Fall** ⚠️ | 30.09 | D | — | — | 9 | — | — | — | — | — | — | **9,0** | ⬜ |
| **The Signal Keepers** ⚠️ | 30.09 | D | 8 | 9 | 9 | 8 | 9 | 10 | 10 | 10 | 9 | **9,1** | ACTION READS · B3 (1:05) toz ve zemin engeli temas gizlenmesi · K20 probe yuvası oturumu |
| **The Static Veil** ⚠️ | 30.09 | D | — | — | — | — | — | — | — | — | — | **—** | ACTION READS · 12 vuruş okunabilir, 9 kategori kusursuz (10/10 → — uyarınca D186) [D184] |


> **The Counted Turn · 09.09.2026 · MOD D · ⚠️ ŞARTLI · matrise girmez**
> Kayıt: [`01_FILM_RAPORLARI/THE_COUNTED_TURN.md`](01_FILM_RAPORLARI/THE_COUNTED_TURN.md)
> · `rapor_kontrol.py` ile düzeltildi: Kusur bildirilmeyen 2 kategori (Threat Vector 10/10, Camera's Contract 10/10) `—` hücresine çekildi [D131/D186]. Düzeltilmiş ortalama: **7,7** (Ham: 8,2/10).
> · Verdict: `MINOR BLUR`. Temas okunabilirliği (4/10): B2, B5, B8 temas anlarında el/kumaş/karabiner erimesi ve penetrasyon.

> **The Solar Mirror · 11.09.2026 · Ⓥ mod V · ⚠️ ŞARTLI · matrise girmez**
> Kayıt: [`01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md`](01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md)
> · Skor: **8,8/10** (Ⓥ mod V). Verdict: `ACTION READS`.
> · 4 kusursuz kategori (Contact, Camera Contract, Agency, Tempo) D131 uyarınca `—`'a çekildi. Düzeltilmiş ortalama 8,8/10.



⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
