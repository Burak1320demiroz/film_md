# 🔴 THE SCOURED GLASS

## Yatay 16:9 · 15 faz × 12 sahne × 10,0 s = **180 sahne · 30:00**

### _"Burada görmeye devam etmenin tek yolu, gördüğün şeyi biraz daha silmektir."_

> **Açıldı:** 07.09.2026 · **Eksen film:** `The Martian` (2015) — bir ÖRNEK,
> şablon değil · **Motor:** OMNI 1.1 Flash · **Tema:** BEDEL

---

## 📁 DOSYALAR

| Dosya | Ne | Durum |
|---|---|:--:|
| `00_PLAN.md` | 15 faz haritası · novum · kilitler · **kilitli bloklar** (karakter/ortam/fizik/negatif) · ışık takvimi · konuşma ve ton eğrisi · referans paketi | ✅ |
| `THE_SCOURED_GLASS_QA_SPEC.md` | QA anında rubrikle **birlikte** yapıştırılır [D117 · D129]. C bloğu TAM — mod V'nin novum'u kusur sayması bu dosyayla engellenir [D166] | ✅ (A/B film alanları ⬜) |
| `FAZ_01_UYANIS/FAZ_01_UYANIS.md` | S1-S12 · 12 imaj + 12 video promptu · B5 omurgası · bilinçli sapma kaydı | ✅ **0 BLOCK** |
| `FAZ_01_UYANIS/FAZ_01_QA_PROMPT.md` | Faz ölçeğinde ölçülemeyen hücrelerin kapısı [D185] | ✅ |
| `REFERANS_PAKETI.md` | RA · RB · RC · RD sayfaları | 🔴 YAZILMADI |
| `FAZ_02` … `FAZ_15` | kalan on dört faz | 🔴 YAZILMADI |

---

## 🧬 FİLM TEK CÜMLEDE

Soğuk bir çöl gezegeninde tek başına kalan bir mühendis, yaşamak için
güneş panelini ve kaskının camını silmek zorundadır — ama bu dünyanın
tozu elektrostatik yüklüdür ve silinince kalkmaz, **yüzeye gömülür ve
çizer.** Her temizlik onun ışığını ve görüşünü kalıcı olarak azaltır.
Doksan sol ötedeki yükseliş aracına vardığında görebilecek gözü kalmış
olmayabilir.

---

## 🔬 NEYE DAYANIYOR

Bu film iki araştırma turunun üstüne kuruldu ve **hiçbir kuralı depo
içi tahminden gelmiyor**:

| Tur | Ne getirdi | Kayıt |
|---|---|---|
| **TUR 13** (3/4 rapor) | Açılış sözleşmesinin üç zaman damgası · muhatap tipolojisi · konuşma yoğunluğu eğrisi · problem zinciri anatomisi · 15 birim için perde matematiği | `04_ARASTIRMA_BULGULARI` §TUR 13 |
| **TUR 14** (4/4 rapor) | Hat ağırlıkları ve bilgi borcu · günlük kamerasının çekim grameri · Mars'ın gerçek sayıları · mizah/gerilim mekanizması (Zillmann · Fiske) | `04_ARASTIRMA_BULGULARI` §TUR 14 |

⭐ **Eksen filmden alınan her tasarım GEOMETRİYE ÇEVRİLDİ** — film adı,
karakter adı ve tescilli tasarım adı hiçbir üretim promptuna yazılmadı
[`04` §T14.3, `MESHUR_SAHNE_KALIPLARI` §4].

---

## 🔴 ÜRETİMDEN ÖNCE KAPANMASI ŞART

```
1. REFERANS PAKETİ (RA · RB · RC · RD) üretilir ve seed'leri yazılır
   ⛔ Onaylanmadan TEK KLİP üretilmez.
2. TEST KLİBİ ölçülür, klip süresi 00_PLAN künyesine yazılır [D124]
   ffprobe -v error -show_entries format=duration -of csv=p=0 <test.mp4>
3. prompt_kontrol.py klasör modunda koşar ve GO verir
   python3 ../../kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py . --rapor
4. ÜRETİM SIRASI: FAZ 1'in kendi §ÜRETİM SIRASI bloğu
   ⛔ S10 TETİK SAHNEDİR [D68] — ilk çıplak yüz doğrulanmadan S11/S12 yok
```

⚠️ **AÇIK BORÇ:** TUR 13'ün dördüncü promptu (metinsiz geçen zaman —
gövde ve mekân merdiveni) **koşulmadı.** KİLİT 4'ün kademe boyu ÖNERİ
etiketlidir. FAZ 1'i etkilemez (0. kademe), **FAZ 4 ve sonrasını
etkiler.** Prompt hazır: `16_...ARASTIRMA_PROMPTLARI.md` §4.
