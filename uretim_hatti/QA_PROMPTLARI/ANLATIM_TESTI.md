# 👁️ 3 · ANLATIM TESTİ — planı bilmeyen izleyici

> **Ne için:** filmin **ekranda ve kulakta** ne anlattığını, planda ne yazdığından bağımsız ölçmek.
> Gemini burada yargıç değil, hikâyeyi bilmeyen bir izleyicinin yerine geçer. Son söz yine
> gerçek insanlarındır (`IZLEME_FORMU.md`).
> Eski 15 merceğin şu üçünün işini görür: ④ hikâye · ⑫ hook (bırakma anı) · ③ diyalog anlaşılırlığı.
> **Nerede:** Gemini uygulaması, **yeni bir sohbet**. Önceki sohbette planı görmüşse sonuç kirlenir.
> **Ne verilir:** YALNIZ video (taslak ya da final, **sesli**). ⛔ Plan, logline, çekim listesi, replik
> metni, film adı VERİLMEZ. Dosya adı da nötr olsun (`taslak_01.mp4`).
> 16 dakikayı aşan filmde iki yarıya böl; ikinci yarıyı da yeni bir sohbette, yalnız video ile ver.
> **Sonra:** çıktıyı sohbete yapıştır.
> - 1-9 cevapları `FILM.md`'deki her çekimin "anlatacağı bilgi" sütunuyla karşılaştırılır; farklar
>   `NOTLAR.md` → ANLATIM'a yazılır: `çekim · planlanan bilgi · izleyicinin anladığı · tuttu/tutmadı`.
> - Tablo satırları (A1-A4) rapor-prompt karşılaştırma akışıyla çekime çevrilir.
> - Duyulan replikler §5 replik tablosuyla karşılaştırılır. Yanlış duyulan replik kayıt ya da miks sorunudur.
>
> ⚠️ Modelin anlamaması insanın da anlamayacağını KANITLAMAZ; ama "nerede koptun" cevabı
> dış izleyicilere hangi anı soracağını gösterir.

---

```
Watch this video once, from start to end, with sound. You know nothing about it beyond what you see
and hear. Answer as an ordinary viewer, in plain English. Do not guess what the makers "meant": if
something is unclear, say it is unclear. Do not give scores. Do not suggest improvements.

1. WHAT HAPPENED: in order, with times (MM:SS), one line per moment that changes something.
2. WHO: who is the main character? Is there anyone else, seen or only heard? What is their relationship?
3. WANT: what is the main character trying to do or get? From which moment was it clear (MM:SS)?
4. OBSTACLE: what stands in the way?
5. CHOICE: does the character decide something important? What, and when (MM:SS)?
6. ENDING: how does it end? Did they get what they wanted? What did it cost them?
7. WHAT WAS SAID: every spoken line you heard, as you heard it, with time and who you think said it.
   Write [unclear] for words you could not make out.
8. FEELING: one sentence: what did you feel at the end?

Then fill this table. One row per moment; leave it empty if there is nothing.

| # | time | type | what exactly is seen or heard | confidence |
|---|------|------|-------------------------------|------------|

Types:
 A1 CONFUSED       you lost track of what was happening, who someone was, or why something happened
 A2 WOULD STOP     the moment you would most likely stop watching, and why (at most two rows)
 A3 LINE UNCLEAR   a spoken line you could not understand, or could not tell who said it
 A4 SOUND OFF      music or effects cover a voice, a sudden silence, or a sound that does not fit
                   what you see
Confidence: SURE / LIKELY / UNSURE.
```
