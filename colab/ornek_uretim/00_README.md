# 🧪 ÖRNEK ÜRETİM — beş prompt, bir hat testi

> **Son güncelleme:** 11.08.2026
> **Amaç:** Colab hattının uçtan uca çalıştığını **beş kareyle** göstermek ve
> deponun bilinen dört zayıf noktasını tek oturumda sınamak.
> **Bölüm kapısı:** `../README.md` · **Betikler:** `../betikler/`

Bu klasör bir film değil. Filmler `dikey_shorts_filmler/` ve
`yatay_*` klasörlerinde durur — burada **motor sınanır.**

---

## 📦 KLASÖR

```
ornek_uretim/
├── 00_README.md          ← BU DOSYA · ne sınanıyor, sonuç tablosu
├── promptlar/            5 prompt · düz metin · "NEGATIVE:" ile ikiye bölünür
│   ├── P1_OLCEK.txt
│   ├── P2_KARAKTER_YAKIN.txt
│   ├── P3_KOSTUM_ARKA.txt
│   ├── P4_DUSUK_ISIK.txt
│   └── P5_NEGATIF_STRES.txt
└── ciktilar/             üretilen PNG + yanında provenance .json
```

**Prompt dosya biçimi:** `NEGATIVE:` satırından sonrası **negatif prompt**
olarak ayrılır ve modele **ayrı girdi** olarak verilir. Deponun negatif
çekirdeği ilk kez prompt metnine gömülü bir dilek listesi değil, gerçek bir
parametre. (FLUX'ta ek koşul var → `../klavuzlar/03_MODEL_ADAYLARI.md`.)

---

## 🎯 HER PROMPT NEYİ SINIYOR

| # | Dosya | Sınav | Neden bu |
|:--:|---|---|---|
| P1 | `P1_OLCEK.txt` | **Ölçek** — 4 m'lik kapsül, 8 m'de sauropod, minik turuncu figür | 120 px testi: küçültünce üç kütle ayrı ayrı okunmalı |
| P2 | `P2_KARAKTER_YAKIN.txt` | **Yüz sadakati** — gözenek dokusu, köstek, asimetri, şeffaf vizör | Vizör şeffaf olduğu için morph yüzeyi geniş; "photographed as a real person" burada test edilir |
| P3 | `P3_KOSTUM_ARKA.txt` | **Kostüm tutarlılığı** — arkadan, yazısız sırt, boş eller, takı yok | Deponun EN DÜŞÜK ölçülen kategorisi Kostüm-Prop |
| P4 | `P4_DUSUK_ISIK.txt` | **Tek kaynak ışık** — gece, sert düşüş, ezilmiş siyahlar, parlama yok | Model gece sahnesine ay/yıldız/ışık huzmesi eklemeye meyilli |
| P5 | `P5_NEGATIF_STRES.txt` | **Negatif çekirdek** — insan YOK, hayvan YOK, çim YOK, metin YOK | En zor sınav: modelin eklemeye en meyilli olduğu her şey yasak |

Beşi de **9:16 · 720×1280** (tam oran, 16'nın katı) ve **aynı seed (1320)**
ile üretilir. Tek değişken model.

---

## ▶️ TEKRAR ÜRETME

```bash
colab new -s ornek --gpu T4

# 1) klasörleri aç + kurulumu KAPAT (hazır yığın yeterli, -U yığını kırıyor)
echo 'import os
os.makedirs("/content/promptlar", exist_ok=True); os.makedirs("/content/ciktilar", exist_ok=True)
os.environ["URETIM_KURULUM"]="0"; os.environ["URETIM_MODEL"]="zimage"' | colab exec -s ornek

# 2) promptları yükle (kernel durumu exec'ler arasında KORUNUR)
for f in colab/ornek_uretim/promptlar/*.txt; do
  colab upload -s ornek "$f" "/content/promptlar/$(basename $f)"
done

# 3) üret (tek exec — oturum ölürse inen model de gider)
colab exec -s ornek --timeout 5400 -f colab/betikler/02_TOPLU_URETIM.py

# 4) indir ve kapat
colab download -s ornek /content/ciktilar/P1_OLCEK__zimage.png ./
colab stop -s ornek      # ⛔ unutma
```

Model değiştirmek için betiğin başındaki `MODEL` ayarı: `zimage` · `sdxl` · `flux`.

> ⚠️ `colab upload` hedef klasör yoksa **500 döner** — Contents API ara dizin
> oluşturmuyor. Yüklemeden önce `os.makedirs` şart. (11.08.2026'da yaşandı.)

---

## 📊 SONUÇ TABLOSU — ölçümle doldurulur

Her satır bir `.json` provenance kaydından gelir. Tahmin yazılmaz.

| Prompt | Model | Süre | Tepe VRAM | Sınavı geçti mi | Not |
|---|---|--:|--:|:--:|---|
| P1 ÖLÇEK | — | — | — | — | — |
| P2 KARAKTER | — | — | — | — | — |
| P3 KOSTÜM | — | — | — | — | — |
| P4 DÜŞÜK IŞIK | — | — | — | — | — |
| P5 NEGATİF | — | — | — | — | — |

**Değerlendirme, 120 px posta pulu testiyle elle yapılır** (yüz, duygu,
eylem okunuyor mu — KAPAK_QA rubriği 12.08.2026'da kaldırıldı; kaynak:
`../../kilavuzlar_ve_sistem_dosyalari/KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md`).

---

## 🔀 İKİ MOTOR KARŞILAŞTIRMASI — planlanan

```
ŞİMDİ   Z-Image-Turbo (Apache 2.0, kapısız, ücretsiz T4)
        → hat çalışıyor mu, negatif prompt tutuyor mu
SONRA   FLUX.1-dev NF4 (HF token gelince, aynı 5 prompt, aynı seed)
        → kalite farkı ÖLÇÜLÜR, tek değişken model
```

İkisi de aynı klasöre `__<model>.png` sonekiyle yazıldığı için karşılaştırma
dosya adından okunur.
