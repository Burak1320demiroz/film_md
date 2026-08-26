# ▶️ SENTEZ KOŞU TALİMATI — 20/20 TAMAM, SENTEZ HAZIR

> 20 partın tamamı işlendi (66 rapor). Sentez artık **meşru olarak
> koşulabilir** — 20 koşuluk erken sentez yasağı bitti.

---

## KOŞU — üç adım

```
1. PROMPTU KOPYALA
   ../../ANALIZ_QA_PROMPTLARI/SENTEZ_ANALIZ_PROMPT.md  → TAMAMINI

2. HEADER'I DOLDUR (promptun 📥 HEADER bloğuna yapıştır)
   FILM:           Nobody Was Alive When We Landed
   TOTAL RUNTIME:  ~01:06:00 (parça sürelerinin toplamından tahmin;
                   kesin süre operatörde yoksa "~66 min (estimated)" yaz)
   INPUT:          CAMERA 20/20 · EVENTS 20/20 · THEME 20/20 ·
                   CHARACTER 5/20 (P09, P10, P11, P12, P13 — optional lens;
                   P14 run returned empty and is excluded; P15-P20 not run)

3. RAPOR GÖVDESİNİ EKLE
   91_SENTEZ_PAKETI_RAPORLAR.md  → TAMAMINI, promptun ALTINA
   (404 KB / ~64.000 kelime — Gemini'nin uzun bağlamına sığar;
    kabul etmezse aşağıdaki B PLANI'na geç)
```

## ⛔ KOŞUDAN ÖNCE BİLİNMESİ GEREKENLER — modele söylenmeli

Bu üç maddeyi HEADER'ın altına ek not olarak yapıştır; yoksa sentez
raporların kendi hatalarını gerçek sanır:

```
OPERATOR NOTES ON REPORT QUALITY (trust these over the reports):
① Part numbers inside the reports are unreliable — most say "(not
   supplied)", and P07, P09, P18 wrongly claim to be "PART 1/20" or
   "PART 4/20". The ⬛ P## headings I inserted above each report are
   authoritative.
② P18 EVENTS has three dialogue lines transcribed in Chinese; the film
   is in English. Treat those three lines as low-confidence.
③ P18's own segment reports describe finding the alien child as a fresh
   discovery, but the child was already with the crew since P16.
   Sequence the reports by my ⬛ P## headings, not by their internal logic.
```

## B PLANI — paket kabul edilmezse

Girdiyi ikiye böl ve İKİ AŞAMALI koş:

```
Aşama 1: prompt + P01-P10 raporları → "PARTIAL synthesis of first half"
Aşama 2: prompt + Aşama 1 çıktısı + P11-P20 raporları
         → header'a not: "the first block below is a partial synthesis
           of P01-P10; the rest are raw part reports for P11-P20"
```

## ⚠️ BU KOŞU OPSİYONELDİR

20 part biter bitmez 66 raporun çapraz okuması ELLE yapıldı
(`50_TAM_FILM_ANALIZI.md`) ve dersler süzüldü (`60_DERS_SECKISI.md`).
Model sentezi **ikinci bir okumadır** — analiz eksik olduğu için değil,
iki okumayı karşılaştırmak için koşulur.

**Karşılaştırmaya değer üç soru** (bizim okumamızda açık kalanlar):
```
① Finalde sağ kalan kadın SATO mu RAIN mi? (defter #22)
② Sinyal yaşı çelişkisi: 4 yıl ↔ 12 yıl — film-içi yalan mı, rapor hatası mı?
③ Kaptanın yara izi: P10 sağ / P11 sol / P12-13 yok — üretim driftti mi?
```

## KOŞU BİTİNCE

Gelen raporu bana ilet → `99_SENTEZ_RAPORU.md`'ye olduğu gibi kaydedeceğim,
sonra `50_TAM_FILM_ANALIZI.md` ile karşılaştırıp ayrıştığı yerleri
işaretleyeceğim; ders seçkisi gerekiyorsa güncellenecek.
