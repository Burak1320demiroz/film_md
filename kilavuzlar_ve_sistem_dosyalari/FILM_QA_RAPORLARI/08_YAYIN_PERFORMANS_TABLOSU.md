# 📡 YAYIN PERFORMANS TABLOSU — gerçek izleyici koşuları

> **Kaynak kılavuz:** `../YAYIN_VE_PERFORMANS_KILAVUZU.md`
> **Oluşturma:** 22.08.2026 — araştırma 1'den çıkan kılavuzla birlikte
>
> Projenin **altıncı** tablosu ve diğer beşinden yapısal olarak farklı:
>
> ```
> LESSONS_LEARNED · KALİTE TAKİP    kare içi teknik    "bu klip doğru mu"
> 03_HIKAYE_KALITE_TABLOSU          dramatik           "kimse umursar mı"
> 04_MANTIK_KALITE_TABLOSU          sahneler arası     "film kendiyle çelişiyor mu"
> 06_KARAKTER_KALITE_TABLOSU        sahneler arası     "karakter aynı karakter mi"
> 07_SES_KALITE_TABLOSU             film boyu          "doğru ses doğru bedenden mi"
> 08_YAYIN_PERFORMANS ← bu          FİLM DIŞI          "izleyici gerçekten izledi mi"
> ```
>
> ⚠️ **Diğer tabloların hepsini bir MODEL doldurur; bu tabloyu İZLEYİCİ
> doldurur.** Bu yüzden çakışma hâlinde bu tablo üstündür: bir film beş
> mercekten yüksek skor alıp burada düşük performans gösteriyorsa,
> yanlış olan RUBRİKTİR — o bulgu
> `../URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md`'ye taşınır.
>
> ⚠️ **Satır yayından ÖNCE açılır.** Geriye dönük açılan kayıt 🚨 GEÇERSİZ
> sayılır: kimlik alanları (hangi kapak, hangi başlık, hangi hook tipi)
> yayın sonrası hatırlanarak yazılamaz.
>
> ⚠️ **Tek değişken kilidi:** ilk 48 saatte yalnız BİR şey değiştirilir
> (kapak VEYA başlık). İkisi birden oynatılırsa satır ⚠️ ŞARTLI girer.

```
GEÇERLİLİK İŞARETLERİ
  ✅ geçerli   — minimum örneklem sağlandı (kılavuz §3)
  ⚠️ ŞARTLI    — örneklem altında VEYA iki değişken birden oynatıldı
  🚨 GEÇERSİZ  — kayıt yayından sonra açıldı
```

---

# 🔢 DURUM

```
YAYINLANMIŞ FİLM SAYISI:  0
İLK KOŞU:                 —
```

> Bu depoda **henüz hiçbir film yayınlanmadı.** `HOOK_VE_ILK_SAHNE_KILAVUZU`
> §0①'in kaydettiği durum budur ve kapanacağı yer burasıdır. İlk satır
> yazıldığı gün, deponun bütün hook/kapak/başlık hipotezleri ilk kez
> gerçek veriyle karşılaşacaktır.

---

# 1. 📋 KİMLİK KAYDI — yayından önce doldurulur

| Film | Format | Yayın (GG.AA.YYYY SS:DD) | Platform | Kapak var. | Başlık var. | Hook tipi | QA (T/H/M) | ⑫ tahmin (3 sn · sebep) |
|---|---|---|---|---|---|---|---|---|
| *(ilk yayınla açılacak)* | | | | | | | | |

> **⑫ tahmin** hücresi ⑫ HOOK raporunun DROP-OFF PREDICTION bloğundan OLDUĞU
> GİBİ kopyalanır — yayından ÖNCE, kart F8 adım 3 [D184]. Üç saniye + sabit
> listeden sebep (`slow open · no stakes yet · plateau · repeated setup ·
> unreadable beat · card`). Bu hücre bu tablodaki tek MODEL sütunudur ve
> yalnız §3'teki gerçek terk saniyesiyle kıyaslanmak için vardır.

---

# 2. 📊 METRİK KAYDI — 24 / 48 / 72 saat

| Film | Saat | VSA / hold | CTR | APV / AVD | Gönderim | Content Loudness | Geçerlilik |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| *(ilk yayınla açılacak)* | | | | | | | |

> `Content Loudness` değeri platformun "Stats for nerds" ekranından
> okunur; hedef bant −1,0 dB … 0,0 dB
> (`../KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §6.2).

---

# 3. 🩺 EĞRİ TEŞHİSİ — terk noktası hangi sahne

| Film | Eğri şekli | Terk saniyesi | Izgara → SAHNE | ⑫ Δ (s · tuttu/tutmadı) | Suçlu değişken | Revize edilen belge |
|---|---|:--:|:--:|:--:|---|---|
| *(ilk yayınla açılacak)* | | | | | | |

> **⑫ Δ:** gerçek terk saniyesi − §1'deki en yakın ⑫ tahmini. |Δ| ≤ 10 s
> TUTTU, ötesi TUTMADI. Üç filmde 0/9 tutarsa yanlış olan ⑫'dir →
> `../URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` [D184].

```
EĞRİ ŞEKİLLERİ (kılavuz §4.1)
  🔻 UÇURUM             ilk 3 sn'de %40-60 düşüş        → S0
  📉 ORTA BÖLÜM ÇÖKÜŞÜ  dakikada %15+ erime            → eğim artan ilk yuva
  🔚 FİNAL ÖNCESİ KAÇIŞ son %20'de kırılma             → doruğun sonraki yuvası

SAHNE ÇEVİRİSİ
  sahne başlangıcı(n) = hook süresi + (n-1) × klip süresi
```

---

# 4. 🚦 KARAR VE DEVAM ADAYLIĞI

| Film | 48. saat kararı | Ne değişti / saat | İlk 10 sn tut. | AVD | Devam kapısı | Evren adayı |
|---|---|---|:--:|:--:|:--:|---|
| *(ilk yayınla açılacak)* | | | | | | |

```
DEVAM KAPISI — indirgenmiş (şu an geçerli olan)
  ilk 10 sn tutunma > %70  VE  AVD > %50
  → üç farklı filmde ölçülmeden dört kriterli tam kapıya geçilmez
  (`../SERI_VE_KANAL_STRATEJI_KILAVUZU.md` §4.2)
```

---

# 5. 📚 İLGİLİ DOSYALAR

| Dosya | İçerik |
|---|---|
| `../YAYIN_VE_PERFORMANS_KILAVUZU.md` | bu tabloyu besleyen kılavuz · karar matrisi · geri besleme yolu |
| `../SERI_VE_KANAL_STRATEJI_KILAVUZU.md` | devam hakkı eşikleri · evren gruplaması |
| `../KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | Content Loudness ve ihraç sayıları |
| `../FILM_KAPAGI_KILAVUZU.md` | 🆕 20.09.2026 · A·B kapak adayları · tek deney sorusu → §1 `Kapak var.` · §4 platform sonucu + öğrenme |
| `../KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | eski CTR skalası (kanıt, ölçü değil) |
| `../YOUTUBE_VIRAL_SANS_KILAVUZU.md` | 🆕 20.09.2026 · kanal-içi karşılaştırma · 7/14/28. gün satırları (§6) · teşhis tablosu (§7) · VİRAL KART (§4: TEST EDİLECEK TEK HİPOTEZ → §1, 7. GÜN → §2, DERS → §3) |
| `00_INDEX.md` | film başına QA kapsamı — bu tablo oraya sütun AÇMAZ |
| `../URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` | QA yüksek + metrik düşük çıkan filmlerin gideceği yer |
