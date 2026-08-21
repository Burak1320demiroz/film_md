# 🔋 LOW POWER — Düşük Güç

**Mars kolonisinde geride kalan son mürettebat üyesi, kalan gücü kendi yaşam desteğiyle sera arasında paylaştıramayacağını fark eder.**

> _"Bir şeyin yaşaması için senin yaşaman gerekmiyor."_

---

## 📁 DOSYALAR

| Dosya | İçerik |
|---|---|
| **LOW_POWER_PLAN.md** | Konsept, tema, farklılaşma gerekçesi, gerçeklik çıpaları, 25 sahne haritası, alınan 4 karar |
| **LOW_POWER_PART_A.md** | Tüm Bible'lar (World, Station, Character, Camera, Lighting, Physics, Negative) + **S0-S12** (13 sahne × IMAGE + VIDEO promptu) |
| **LOW_POWER_PART_B.md** | **S13-S24** (12 sahne × IMAGE + VIDEO promptu) + müzik promptları + film özet tablosu |
| **LOW_POWER_KAPAK.md** | Kapak A (mavi gün batımı + yüz), Kapak B (tek yeşil pencere), tipografi spesifikasyonu, A/B test planı |
| **LOW_POWER_FRAGMAN_DIKEY.md** | **FRAGMAN (teaser)** — 9:16 dikey, 6 vuruş × 8 s = 48 s, mekanik **ÖRTÜLME**. Kaynak vuruşlar: S0·S6·S7·S14·S8·S10. Ayrı teslim; film sayımına girmez. Merceği SHORTS_QA |

---

## 📊 KÜNYE

```
FORMAT:      16:9 yatay, 3-5 dakika formatı
SÜRE:        Hook 9s + 24 sahne × 10s = 249 saniye = 4 dakika 09 saniye
SAHNE:       25 (Part A: 13, Part B: 12)
VİRAL ARA:   4 (S5, S14, S19, S23)
DİYALOG:     5 sahne (S2, S10, S11, S20, S22) — 20 sahne sessiz
             Hepsi tek konuşmacı kayıt. Karşılıklı diyalog YOK.
KARAKTER:    1 — Dr. Selin Aras (promptlarda isimsiz, Ders 34)
MEKAN:       Mars, Hellas İstasyonu, Sol 187
RENK:        Kızıl-kahve (Mars) + Yeşil (sera). Üçüncü renk YOK.
             Mavi sadece S14'te — bilimsel gerçek (Mars gün batımı).
İMZA SAHNE:  S20 — anahtarın çevrilmesi
KAPAK ADAYI: S14 — mavi gün batımı
ÜRETİM:      25 imaj + 25 video
```

---

## ⚠️ ÜRETİM DURUMU VE BİLİNEN SORUN

```
DURUM: Promptlar yazıldı, üretim başlamadı.

BİLİNEN SORUN — PROMPT UZUNLUĞU:
Dosyalardaki promptlar ortalama ~3.900 karakter. S5 ve S11 denendi,
ikisi de Veo'da hata verdi. Kısaltılmış sürümler (~1.500-2.400 karakter)
hazırlandı ve konuşma geçmişinde mevcut.

→ Toplu kısaltma yapılmadı. Yapılırsa yöntem: her prompta gömülü
  ~1.400 karakterlik negatif bloğu, filme özel tek çekirdek sete indirmek
  (Mars için 3 kritik kural + evrensel 6 madde).

MARS'A ÖZEL 3 KRİTİK RİSK (her üretimde ilk kontrol edilecek):
1. Model mavi gökyüzü yapar — Mars göğü kahve-tarçın, asla mavi.
2. Model Dünya fırtınası yapar — atmosfer %0.6, hiçbir şey devrilmez,
   kumaş çırpınmaz, ses uğuldamaz.
3. Model tozu uzaya gönderir — burada TERSİ: toz düşer ve yere oturur.
   Filmin trajedisi tam olarak budur.
```

---

## 🔗 İLGİLİ KILAVUZLAR

| Kılavuz | Ne için |
|---|---|
| `../README.md` | 3-5 dk format kuralları |
| `../../kilavuzlar_ve_sistem_dosyalari/LESSONS_LEARNED.md` | 38 ders — negatif blokların kaynağı |
| `../../kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md` | Üretim sonrası teknik QA |
| `../../kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/SENARYO_QA_CRITIQUE_PROMPT.md` | Üretim sonrası senaryo eleştirisi |
| `../../kilavuzlar_ve_sistem_dosyalari/VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` | YouTube/Instagram/TikTok paketlemesi |
| `../../kilavuzlar_ve_sistem_dosyalari/KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | Kapak tasarım kuralları |
