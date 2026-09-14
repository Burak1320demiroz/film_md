# 🧾 THE_STATIC_SHADOW — QA + DERS HASADI

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D197 | Vizör içinden yüz görünmesi, nitelik sıçraması | Opak siyah aynalı TEK kilit vizör — yüz ve vizör içi asla görünmez. | S03, S10 |
| D139 | Arka kadrajda sırt ekipman karmaşası | Suit sırtı düz tek parça pürüzsüz paneldir, hiçbir çanta/askı taşımaz. | S02, S08, S11, S15 |
| D32/D78 | İki gövde oran kayması | Pod kalkanın 1/30'u boyuttadır, V3 oran karesinde tek kez kilitlenir. | S06 |
| D201 | Yıldız ışık yönü flip | Mavi dev yıldız ışığı sol üstten sabittir. | Tüm sahneler |
| Vakum Ses | Dış kamerada ses hatası | Dış kameralar mutlak sessizliktedir, yalnızca iç kamera contact vibration taşır. | S01, S05, S07, S09, S13, S14 |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_DEAD_APPROACH | ① KARE | Vizör transparanlığı sahneden sahneye değişti | D197 kuralı ile `opaque black mirrored visor` kelimesi tüm kask promptlarına eklendi |
| THE_HARD_DOCK | ⑥ FİZİK | Vakumda çarpışma metalik ses çıkardı | Dış kamera promptlarına `absolute quietness in vacuum` kilidi çakıldı |
| RINGWORLD | ⑨ KADRAJ | 1/30 oran tutarsızlığı | S06 tek oran karesi V3 olarak kilitlendi |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| TK | "Cold weld" jargonu ret | Galling + plastik deformasyon + vakum adhesion tanımı | S14 |
| FİZİK | 0.8 rad/s aşırı dönüş hızı | ~0.008 rad/s yavaş yalpalama tanımı | S01 |
| FİZİK | Metal erimesi jargonu | Radiative flux beyond thermal qualification | S02 |

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        5 adet
QA ARIZASI:         3 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   Opak Vizör Kilidi (D197) · Vakum Sessizlik Kilidi · Scaled Ratio (1/30)
```
