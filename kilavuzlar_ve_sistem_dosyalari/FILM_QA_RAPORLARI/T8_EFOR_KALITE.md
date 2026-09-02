# 💪 T8 — EFOR KALİTE TABLOSU (risk tetikli tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/8_EFOR_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 01.09.2026 — aksiyon mercekleri sınıfının ikinci yarısı
>
> **Ne ölçer:** "İş bedene neye mal oldu ve faturası ekranda mı." Tek
> yöntemi FATURA CÜMLESİ: "bu işten SONRA bu bedende ne değişti?" Cevap
> "hiçbir şey" ise bulgu odur. Yalnız anlık zorlanma değil, borcun
> BİRİKMESİ ölçülür.
> ⭐ Üretilmiş videonun en sessiz kusuru burada yaşar: beden işi yapar,
> kimse ödemez. ⑥ FİZİK "bu kaldırış sayısal olarak mümkün mü" der ve
> GEÇER; ⑧ "eli hiç sıkılmadı" der ve KALMAZ.
>
> ```
> KATEGORİLER  1 anlık zorlanma · 2 nefes+toparlanma (görünür) · 3 yorgunluk
>              birikimi · 4 yükün bedendeki karşılığı · 5 yaralanmanın
>              işlevsel bedeli · 6 kavrama · 7 ekipman yükü · 8 acı
>              orantısı · 9 toparlanma eğrisinin dürüstlüğü
> ⛔ DÜŞÜK YERÇEKİMİ DÜŞÜK EFOR DEĞİLDİR: ağırlık azalır, kütle ve atalet
>              azalmaz. "0.12g'de kolay olur" mazereti BULGUDUR.
> ⛔ TERS HATA DA CEZALANIR (pattern ⑭): sebepsiz gelen yorgunluk,
>              ödenmeyen fatura kadar sahtedir. Bu mercek "daha çok acı
>              daha iyi" demez.
> TETİKLEYİCİ  KART 3 (kask/vizör/ekipman) · planın YÜK / SÜRE /
>              YARALANMA kilidi · ortamın bedensel bedeli (soğuk · ısı ·
>              ince hava · basınç)
>              📌 dürüst açık: "sürekli iş / yük" için ayrı risk kartı YOK
> MAKİNE ÇIKTISI  COST CURVE — sahne başına bir hane (0-9); her DÜŞÜŞ
>              RESET LOG'da gerekçelenir, gerekçesiz düşüşü
>              rapor_kontrol.py yakalar
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

| Film | Tarih | Mod | Zorlanma | Nefes | Yorgunluk | Yük | Yaralanma | Kavrama | Ekipman | Acı | Eğri | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| *(henüz koşu yok)* | | | | | | | | | | | | | |

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
