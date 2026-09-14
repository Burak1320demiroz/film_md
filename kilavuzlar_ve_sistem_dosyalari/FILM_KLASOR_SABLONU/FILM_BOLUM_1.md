# 🎬 <FILM_ADI> — BÖLÜM 1  (S0 – S⬜)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, Bible ve kilitler
> `<FILM_ADI>_PLAN.md`'de durur; buradaki hiçbir prompt oraya ATIF YAPMAZ —
> her prompt tek başına çalışır (AGENTS §2 kural ③). ⭐ 14.09.2026: self-contained
> ≠ Bible'ın tamamı — yalnız `IN FRAME:` satırındaki tarif edilir [D214].
>
> ⭐ **14.09.2026 YENİ REJİM** (bu şablonla açılan her klasör): ilk satır `IN FRAME:`
> (㉖) · POZİTİF gövde IMAGE 100-250 / VIDEO 120-300 kelime, üstü BLOCK (①) ·
> NEGATIVE = `KILAVUZ_REHBERI` §5.1 çekirdek (image 7 · video 8 cümle) + ≤3
> sahneye özel, üstü FIX (㉗) · video Bible'ı tekrar etmez, tek satır `START FRAME:`.
> Sayılar `prompt_kontrol.py` başında; iskelet `IMAGE_VIDEO_PROMPT_TEMPLATES.md` V3.
>
> Sahne başlığı `##` ile yazılır (kural ②): başlıksız dosya sayımdan ve
> her taramadan düşer.
>
> Bölüm sınırı ardışık bir çifttir: bu dosyanın SON sahnesi ile bölüm 2'nin
> İLK sahnesi ≥1 ölçek kademesi VE ≥45° ayrılmak zorundadır. Denetimi
> klasör modu yapar: `python3 .../prompt_kontrol.py <film klasörü>`

---

## 🎬 SAHNE 0 — ⬜ BAŞLIK

```
SÜRE: ⬜ s   ·   VURUŞ: ⬜   ·   KURULUM: ⬜ lens · ölçek · açı tipi
```

### 📸 GÖRSEL PROMPT

```
IN FRAME: ⬜ face · hands · torso · legs · full body · back | none
Scene 1 of <toplam>.
[SAHNENİN TEK KİLİDİ — bu karede tutması gereken şey, SAYIYLA — üçüncü satır]

[ÖZNE — yalnız IN FRAME'dekiler: hands → eldiven · bilek · kol; face → yüz +
 kask + D79 vizör cümlesi (§5.2); back → D139 sırt cümlesi (§5.2); full body →
 silüet + renk bandı, yüz ayrıntısı YOK. Character Bible'ın kalanı YAZILMAZ —
 PLAN'daki blok kaynaktır, kadrajdaki kısmı buraya gelir]
[mekân · ışık · ölçek — bu karede görünen kadarı; ölçü nesne-göreli [D138]]
[CAMERA: lens + mesafe + yükseklik + açı tipi — "low angle" / "high angle" /
 "over-the-shoulder" gibi sözlük kelimesiyle]

NEGATIVE: [KILAVUZ_REHBERI §5.1 çekirdek — IMAGE'de 7 cümle, ① düşer]
[+ ≤3 sahneye özel cümle — §5.2; yoksa boş]

Output: ⬜ oran, ⬜ çözünürlük, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
IN FRAME: ⬜ face · hands · torso · legs · full body · back | none
Scene 1 of <toplam>. Duration <klip> seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
[SAHNENİN TEK KİLİDİ — hareket kilidi, SAYIYLA]

[TIMELINE: 0,0 s … / ⬜ s … — her satırda ≥1 gövde fiili; replik varsa ofseti
 buradan okunur, konuşan/dinleyen bedeni §5.2 diyalog satırı]
[CAMERA: ⛔ I2V'de bu satır ŞART — betik kurulum yayını video promptundan
 ölçer; satır yoksa sahne "kamera yazılmamış" sayılır]
[IN FRAME: back ya da kamera arkadaysa: sırt için POZİTİF yüzey cümlesi — "the
 back of the suit is one continuous smooth panel from collar to hip, a flat
 back silhouette carrying nothing" [D139]; değilse YAZILMAZ (㉖ NOT)]

NEGATIVE: [KILAVUZ_REHBERI §5.1 çekirdek — 8 cümle]
[+ ≤3 sahneye özel cümle — §5.2]

Output: ⬜ oran, no text, no watermark.
```

---

## 🎬 SAHNE 1 — ⬜ BAŞLIK

*(aynı iskelet)*
