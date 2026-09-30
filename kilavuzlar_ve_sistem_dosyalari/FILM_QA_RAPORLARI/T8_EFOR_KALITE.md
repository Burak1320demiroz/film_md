# 💪 T8 — EFOR KALİTE TABLOSU (risk tetikli tarama)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/8_EFOR_QA_CRITIQUE_PROMPT.md`
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
| **The Counted Turn** | 09.09.2026 | D | 0.0 | 0.0 | 0.0 | 0.0 | — | 0.0 | 0.0 | 0.0 | 0.0 | ⚠️ 0.0 | 🔴 **NOBODY PAYS** — efor faturası ekranda 0; 6 iş olayının altısında da beden yorulmuyor/zorlanmıyor (0:10, 1:10, 1:20, 1:30, 3:00, 3:40) [D184] |
| **The Solar Mirror** Ⓥ ⚠️ | 11.09.2026 | V | 2 | 3 | 3 | 4 | — | 2 | 2 | 4 | 3 | **2,9** | WEIGHTLESS WORK · 8 efor olayının 7'sinde sıfır zorlanma, acil durumda dinlenmiş nefes |
| **The Resonant Strand** ⚠️ | 11.09 | D | 1 | — | 1 | 1 | — | 1 | 1 | — | 1 | **1,0** | ⬜ |
| **The Hard Dock** ⚠️ | 12.09.2026 | D | 6 | 7 | 6 | 7 | — | 6 | 7 | — | 7 | **6,6** | Visor fogging absent under heavy exhalation, no tremor in E10 |
| **The Falling World** B2 ⚠️ | 19.09 | D | 5 | 7 | 6 | 5 | — | 6 | 5 | 7 | 7 | **6,0** | ⬜ |
| **The Slow Rain** B2 | 22.09 | D | 8 | 9 | 8 | 9 | — | 8 | 9 | 9 | 10 | **8,8** | ⬜ |
| **The Inward Fall** ⚠️ | 30.09 | D | 2 | 4 | 2 | 3 | 3 | ⬜ | 2 | 3 | 3 | **2,7** | ⬜ |
| **The Signal Keepers** ⚠️ | 30.09 | D | 4 | 6 | 5 | 4 | — | 4 | 3 | — | 5 | **4,4** | WEIGHTLESS WORK · E4 tek elle küre taşımada omurga asimetrisi sıfır [Desen ⑨] · E2 3.1 bar eldiven dirençsizliği [Desen ⑥] · E8 kol yorgunluk düşüşü yok [Desen ⑤] |
| **The Static Veil** ⚠️ | 30.09 | D | 1 | 1 | 1 | 2 | — | 2 | 2 | 1 | 1 | **1,4** | WEIGHTLESS WORK · EVA giysisi ve 0.16 g Ay çekiminde efor/direnç sıfır, visor buğulanması yok |


> **The Solar Mirror · 11.09.2026 · Ⓥ mod V · ⚠️ ŞARTLI · matrise girmez**
> Kayıt: [`01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md`](01_FILM_RAPORLARI/THE_SOLAR_MIRROR.md)
> · Skor: **2,9/10** (Ⓥ mod V). Verdict: `WEIGHTLESS WORK`.
> · 8 efor olayının 7'sinde bedensel zorlanma/tensing yok (E1-E7); acil durumda nefes rested kalıyor.


⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
