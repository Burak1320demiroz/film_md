# 06_PROMPT_URETECI — 96 × 2 promptun ve PLAN'ın tek kaynağı

> 20.09.2026. Bölüm dosyaları (`THE_STOLEN_SKY_BOLUM_1…8.md`) ve `THE_STOLEN_SKY_PLAN.md`'nin
> sahne haritası/iskelet/Bible blokları BU klasörden ÜRETİLİR; elle düzeltilmez.
> Sebep: aynı harf = aynı CAMERA metni, aynı hacim = aynı PHYSICS/AUDIO, çekirdek NEGATIVE her
> promptta birebir — 192 promptta elle tutarlılık tutmaz (ACI_YAYI §7 ⑥ · §5.1b · D214).

```
common.py   Bible'lar: CAM (20 harf) · PHYS/AUD (hacim) · NEGATIVE çekirdek · CH (dört insan) · Veyra · araçlar · dünya
b1.py … b8.py   sahne verisi (12 sahne / dosya): olay kilidi · gövde · LIGHT · TIMELINE · AUDIO · ≤2 negatif ek · IN FRAME · kadro
render.py   üreteç + denetimler (kelime bandı · LIGHT yüzey adı D176 · toward/pusula D174 · politika sözlüğü · kamera-arkada/back_of D139)
plan.py     PLAN dosyasını (sahne haritası · iskelet · Bible) veriden yazar
```

Koşum (depo kökünden):
```
cd yatay_16_dk_filmler/THE_STOLEN_SKY/00_ANALIZ/06_PROMPT_URETECI
python3 render.py 8      # BOLUM_1…8 yeniden yazılır (render.py içindeki OUT yolu)
python3 plan.py          # PLAN yeniden yazılır
cd ../../../.. && python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_16_dk_filmler/THE_STOLEN_SKY
```
⛔ Bir sahneyi değiştirmek = ilgili b*.py satırını değiştirip yeniden üretmek. ⛔ Bu klasörde `## 🎬 SAHNE n` başlığı ve 📸/🎥 işareti yoktur (betik .md dışını okumaz).
