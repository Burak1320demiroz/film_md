# 🎥 OMNI 1.1 FLASH — Görüntüden-Videoya Üretim Kılavuzu

> **Ne bu dosya:** OMNI (Gemini Omni 1.1 Flash) ile tek onaylı başlangıç
> karesinden on saniyelik klip üretirken promptun, karenin ve iş akışının
> motora özgü katmanı. `IMAGE_VIDEO_PROMPT_TEMPLATES.md` V3 iskeletinin
> **ÜSTÜNE biner, yerine geçmez**; `VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md`'nin
> kardeşidir. Doluluk (fiil sınıfı · TIMELINE · sürdürme) `SAHNE_DOLULUGU_KILAVUZU.md`'de,
> politika `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`'de kalır — burada tekrar edilmez.
>
> **Kaynak:** TUR 20 (16.09.2026) — `URETIM_ONCESI_ANALIZ/23_…` dokuz prompt →
> `TUR20_HAM_RAPORLAR/` (9/9 birebir + künyede canlı kaynak kontrolü) →
> `04_ARASTIRMA_BULGULARI.md` §TUR 20. Satır sonundaki `[T20.2 #n]` süzme
> kaydındaki satırdır. **Kural buradan okunur; gerekçe 04'ten.**

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① İKİ KATMAN VAR, KARIŞTIRILMAZ.
   RESMÎ   — Google'ın duyurusu ve Gemini API Omni sayfası. Künye, modlar,
             sınırlar, beş prompt ipucu. Sağlam. (§1 · §2'nin ✅ satırları)
   GÖZLEM  — üçüncü taraf inceleme / tek bağımsız ölçüm / raporun
             mekanizması. Yön iner, kural ancak PROB'la kapı olur. (⬜)

② HİÇBİR KALIP ÜRETİMDE SINANMADI. Depoda henüz tek OMNI klibi QA'dan
   geçmedi. §9 şablonları iskelettir; ilk filmde ① KARE · ② DEVAMLILIK ·
   ⑭ HAREKET ve PROB'larla (§10) sınanır.

③ SAYISIZ. Yüzde, saniye eşiği, "uyum oranı" yok — TUR 20'nin bütün sayı
   katmanı kaynağıyla eşleşmedi. Yalnız resmî sayılar (§1) durur. Fiyat
   yazılmaz (değişir; tarihli hâli künyede).

④ ÜÇ SÖZDİZİMİ SORUSU AÇIK: replikte tırnak · prompt uzunluğu · damga
   biçimi. Kapı değil; §10 PROB ①②⑥.

⑤ Resmî satırlar bir özetleme aracıyla okunan sayfalardan geldi. İlk
   üretim günü sahip arayüzde bir kez teyit eder (§10 ③).
```

---

# 1. 🪪 KÜNYE — resmî (G1 blog.google 27.08.2026 · G2 ai.google.dev Omni sayfası)

| alan | değer | not |
|---|---|---|
| ad · kimlik | **Gemini Omni 1.1 Flash** · API `gemini-omni-1.1-flash` | önceki `gemini-omni-flash-preview`; depoda `OMNI`, sahibin "Osmi"si [T20.2 #1] |
| görevler | text_to_video · **image_to_video** · reference_to_video · edit · extend | hat: image_to_video |
| kare modları | yalnız başlangıç karesi · **başlangıç + bitiş karesi** (`<FIRST_FRAME> <LAST_FRAME>`) | bitiş karesi VAR [T20.2 #2] — kullanımı §8, sahip kararı |
| çözünürlük | 360p · **720p (varsayılan)** · 1080p · 4K | 1080p/4K = 720p'nin büyütmesi (gözlem) → §7 |
| oran | **16:9 (varsayılan)** · 9:16 | kare aynı oranda üretilir (§3 ①) |
| uzatma | önceki **10 s** okunur · 10 s adımlarla **40 s**'ye · yalnız SONA | hat dışı; §8 |
| video referansı | en çok 3 klip × 3 s; referanstaki ses yok sayılır | hat dışı |
| ses | **her klipte üretilir**; kapatma anahtarı belgesiz; ses referansı yüklenemez; ses düzenlenemez | §5 |
| olumsuzlar | ayrı negatif alanı YOK — prompt gövdesine ("Do not do X" · "No X") | V3 `NEGATIVE:` bloğu doğru yerde |
| dil | İngilizce tam destekli; diğerleri değerlendirilmemiş | depo zaten İngilizce |
| kişi | tanınmış kişi içeren görsel yüklenemez; reşit olmayan görünümü EEA/CH/UK'da yüklenemez; filtre hem girdide hem üretilen videoda, bölgeye göre değişir | §6 |
| **belgesiz** | seed · süre alanı · kare hızı · `thinking_level` | seed'e ve `thinking_level`'a dayanan her öneri düşer [T20.4] |

---

# 2. 🧩 PROMPT İSKELETİ — V3 + OMNI KATMANI

V3 VIDEO iskeleti AYNEN kullanılır (`IN FRAME` · `Scene n of N. Duration` ·
`START FRAME` · 3. satır tek kilit · `TIMELINE` · `CAMERA` · `PHYSICS` ·
`AUDIO` · `NEGATIVE` · `Output`). OMNI'de değişen yalnız şu yedi satırdır:

```
① START FRAME satırı kalır — görünüm YENİDEN TARİF EDİLMEZ.            ✅ ZATEN VAR
   OMNI'de de geçerli: yeniden tarif kaymayı hızlandırır; resmî belge
   düzenleme için "overly descriptive prompts can lead to unintended
   changes" diyor [T20.1 2↔3].

② CAMERA satırı ŞART ve şu cümleyle biter:                              ⭐ OMNI
      In a single continuous shot.
   Resmî ipucu. Kamera cümlesi olmayan promptta model kendi hareketini
   ve kesmesini ekleyebilir [T20.2 #6 · #17]. NEGATIVE çekirdek ①
   ("Single unbroken take, no cuts …") ayrıca kalır — biri pozitif,
   biri olumsuz; ikisi aynı işi iki yerden yapar.

③ AUDIO satırı HER klipte; sessiz klipte şu iki cümle:                   ⭐ OMNI
      No dialogue. No music.
   Ses her klipte üretilir; "No dialogue" resmî ipucudur. Yazılmazsa
   model konuşma ya da müzik uydurabilir [T20.2 #3 · #4].

④ Video promptunda TIRNAK İŞARETİ YOK.                                  ⭐ OMNI
   Model istenen metni "doğru ve okunur" çizer (resmî). Depo ekranda
   yazı istemez [D34 · D45]; tırnaklı her dize yazı adayıdır.
   Replikli klipte biçim §5 ② — PROB ① koşulmadan ÜRETİLMEZ.

⑤ Olumsuzlar gövdede — V3 NEGATIVE bloğu.                              ✅ ZATEN VAR
   Resmî kalıplar serbest: "No scene cuts" · "No dialogue" · "No extra
   sound effects" · "Do not …". Artefakt adı taşıyan olumsuzlar ("no
   morphing") için ek kural yok [T20.4].

⑥ TIMELINE ≤ 3 satır, son satır SÜRDÜRME (SAHNE_DOLULUGU §2).          ✅ ZATEN VAR
   Biçim: depo "0.0s — …" ya da OMNI'nin resmî biçimi "[0-3s] …" /
   "After 3 seconds, …". Bir filmde TEK biçim; hangisinin iyi tuttuğu
   PROB ⑥ [T20.2 #7].

⑦ Bütçe V3'ün bandıdır (VIDEO pozitif gövde 120-300).                  ⬜ PROB ②
   Üçüncü taraf bir deneyci 30-80 kelime diyor; resmî belge düzenleme
   için "basit prompt" öneriyor. Bant PROB ② sonucuna kadar değişmez.
```

---

# 3. 🖼️ BAŞLANGIÇ KARESİ — IMAGE promptuna yazılanlar

Video promptu kareyi değiştiremez; kare kuralları IMAGE promptuna iner.

```
① ORAN = ÇIKIŞ ORANI. Kare 16:9 ise video 16:9 (ya da ikisi 9:16). Farklı
   oranda kareyi motorun nasıl uydurduğu belgesiz (kırpma mı, dolgu mu,
   kenar üretimi mi) — hiç sorulmaz.                          [T20.1 2↔3]

② EYLEMİN ORTASI AMA DENGEDE. Beden işin içinde, yük altında (SAHNE_
   DOLULUGU §2 ①) — ve İKİ destek noktası yerde: iki bot · diz + bot ·
   el + bot. Adım ortası, sıçrama, düşüş anı, tek ayak havada DEĞİL
   (kayan ayak / askıda kalma riski).                          [T20.2 #13]
     ✗ "mid-stride, left boot lifted off the regolith"
     ✓ "both boots planted, weight on the front foot, gloves already on
        the sled strap, the strap taut"

③ YÜZ YALNIZ GEREKTİĞİNDE. IN FRAME `face` yalnız yüzün sahneyi taşıdığı
   planda; kimlik ≤3-4 öznitelik [D167 · ⑲]. Yüzü gizleyerek (parlama,
   gölge) filtreden geçirmek yapılmaz — yüzün gerekmediği sahnede yüz
   YAZILMAZ, gizlenmez.                                        [T20.3]

④ GÖRÜNMEYENİ AÇIĞA ÇIKARMA YOK. Karede arkası dönük yüzün klipte dönmesi,
   kapalı kapağın açılması, kadraj dışı nesnenin girmesi = uydurma + durum
   değişimi. Yeni görünüm SONRAKİ sahnenin karesidir [REHBER §7].

⑤ İNCE TEKRARLAYAN AYRINTI İKİNCİL. Izgara, kablo demeti, perçin sırası
   arka planda baskın olursa hareketle titreyebilir. Kural değil, risk
   notu: bu yüzeyler kadrajın odağı yapılmaz.                  ⬜ [T20.2 #18]

⑥ OKUNUR YAZI YOK — kare temizse video yazı "bulmaz" [D34 · D45 · D138].
```

---

# 4. 🎬 HAREKET VE KAMERA — OMNI'ye özgü üç satır

Fiil sınıfı, üç evre, dolgu sırası, ölü sahne kontrolü → `SAHNE_DOLULUGU_KILAVUZU.md`.
Kamera hareket listesi → TEMPLATES. Burada yalnız motorun gözlenen zayıflığı:

```
① KİMLİK HAREKETLE KAYAR, ARKA PLAN KAYMAZ. Karakter animasyonu ve nesne
   kalıcılığı motorun zayıf yanı; arka plan sağlam (tek bağımsız test).
   Kilit fiili YÜZÜN AÇISINI değiştirmez, yüzü elle/nesneyle KAPATMAZ,
   yüzü kadrajdan ÇIKARIP geri SOKMAZ. Baş dönüşü gerekiyorsa sahne
   başlangıç karesi zaten dönmüş hâlde kurulur.                [T20.2 #12]

② KAMERA CÜMLESİ YAZILIR, HAREKET TEKTİR. Kamera satırı yoksa motor
   kendi hareketini seçer (§2 ②). Kamera hareketi + karmaşık özne eylemi
   birlikte istenirse biri söner — ya kamera sabit ya özne işi basit.

③ SABİT KAMERA CÜMLESİ ÖZNEYİ DONDURABİLİR. "absolutely zero camera
   movement" türü katı kilit ile "mounted on a fixed tripod" çerçevesi
   arasındaki fark ölçülmedi. Şablon değişmedi; PROB ⑤.        ⬜ [T20.1 4↔5]
```

---

# 5. 🔊 SES VE REPLİK

```
① SES HER KLİPTE. AUDIO satırı her promptta, kaynağa bağlı, ≤3 katman
   (VEO §7 ile aynı): zemin (fan · pompa · rüzgâr) · eylemin sesi (as/when
   ile bağlı) · beden (nefes). Sessiz klipte "No dialogue. No music."

   İÇ, SESSİZ     AUDIO: a steady low fan hum; a dry metal creak with each
                  pull; his breathing inside the helmet. No dialogue. No music.
   DIŞ, İNCE ATM. AUDIO: muffled — only his breathing inside the helmet and
                  the suit fan; wind heard faintly through the shell. No
                  dialogue. No music.
   TELSİZ (post)  AUDIO: one short burst of radio static from the helmet
                  speaker, no words. No dialogue. No music.
                  → telsiz sözü klipte ÜRETİLMEZ, post'ta biner [04 §T13 #10]

② REPLİK — PROB ① KOŞULMADAN ÜRETİLMEZ.
   Açık soru: tırnak mı, iki nokta mı. Resmî belge susuyor; bir kaynak
   "iki nokta = konuşma, tırnak = ekran yazısı" diyor (sınamamış), bir
   başkası "dudak senkronu için tırnak" diyor; depo Veo hattında tırnaklı
   replikten 2/2 gömülü altyazı ölçtü [D40].
   PROB ① iki kolu (aynı kare, MCU, basınçlı iç, aynı cümle):
     A   He says: The leak is closed and the habitat holds pressure.
     B   He speaks the line: "The leak is closed and the habitat holds pressure."
   İki kolda da AUDIO: "The line is heard only, never shown as text. No
   subtitles. No music." Kazanan: ekranda yazı YOK + dudak senkronu var.
   Kazanan kalıp bu satıra ve DIYALOG_SAHNESI BASAMAK 2'ye yazılır.

③ REPLİK KOŞULLARI — ZATEN VAR, OMNI'de de: basınçlı iç · kasksız ya da
   açık yüz · MCU'dan geniş değil · tek konuşmacı · <5 s · ≤20-25 kelime /
   10 s · kapalı vizörde replik yok [04 §T13 #8-10 · SES_VE_DIYALOG].

④ SES KİMLİĞİ KLİPLER ARASI KİLİTLENEMEZ. Ses referansı ve ses düzenleme
   yok; her I2V klibi karakterin sesini yeniden üretir. Aynı karakter
   birden fazla klipte konuşuyorsa ses rengi değişebilir → film planında
   karar satırı: POST-DUB ya da "değişim kabul".              [T20.2 #5]
   ⚠️ THE_SCOURED_GLASS (24 günlük) bu kararı üretimden ÖNCE alır.
```

---

# 6. 🛡️ KİMLİK VE POLİTİKA — OMNI yüzeyi

Genel sözlük, imzalar ve red basamakları → `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`.

```
① RESMÎ SINIR: tanınmış kişi içeren görsel yüklenemez. Kurgusal ama
   fotogerçekçi yüz bu sınıra YANLIŞLIKLA düşebilir.

② BİLİNEN VAKA (birinci el, 14.08.2026, önizleme sürümü, API): kurgusal
   yapay zekâ üretimi yetişkin sunucu karesi + ağız hareketi istendi →
   ÇIKTI aşamasında engellendi ("The video was filtered out because it
   violated Google's Generative AI Prohibited Use policy"). Kullanıcı
   karakterin kurgusal olduğunu açıklayınca da iki kez engellendi.
   → "Promptun başına 'fictional character' yaz" bir çözüm DEĞİLDİR.
                                                              [T20.2 #14]

③ İKİ AŞAMA, İKİ TEŞHİS:
   GİRDİ  istem gönderilir gönderilmez döner, üretim başlamaz → prompt ya
          da kare sınıflandırıcısı → sözlük / öznitelik yığını / kare
   ÇIKTI  üretim bittikten sonra "filtered out" → üretilen videonun kendisi
          → hareket (ağız hareketi, yakın yüz), ses (replik) — önce SESSİZ
          KOŞU teşhisi [POLITIKA §5 basamak 2.5]
   Red defteri satırına MOTOR ile birlikte AŞAMA yazılır (⬜ sütun adayı).
                                                              [T20.2 #15]

④ YAPILMAYANLAR: yüzü parlama/gölgeyle örtmek · kareye gürültü eklemek ·
   kareyi filtre için düzenleyip üretimden sonra kırpmak — hepsi ATLATMA,
   depoda yok [07_ ilkesi · T20.3].

⑤ MOTOR SEÇİMİ: "yüzlü I2V → VEO" (POLITIKA §6.1) ⬜ HİPOTEZ KALIR — OMNI'de
   yüz reddi var ama Veo'dan AĞIR olduğu karşılaştırmayla gösterilmedi.
   Red geldiği gün MOTOR + AŞAMA yazılır; üç vaka kuralı kesinleştirir.
```

---

# 7. 🔁 İŞ AKIŞI — deneme, seçim, kayıt

```
① 360p = OKUNABİLİRLİK SINAVI, SEÇİM DEĞİL. 360p başka bir üretimdir;
   360p'de beğenilen çekim 720p'de yoktur (tek bağımsız ölçüm: 360p ↔ 720p
   kare korelasyonu düşük, 1080p/4K ↔ 720p neredeyse birebir).
     360p   → prompt okunuyor mu: kilit, kamera, tek plan, ses tipi
     720p   → ÇEKİM SEÇİMİ burada
     4K     → seçilen çekimin büyütmesi (yeni üretim değil)  [T20.2 #10]

② SEED'E GÜVENİLMEZ. Resmî API'de belgesiz. "Aynı prompt + aynı kare
   yeniden üret" bir VARYANS aracıdır, tekrar üretim değil. Flow'da seed
   alanı varsa bile tekrar üretilebilirliği sınanmadan kullanılmaz [D142].
                                                              [T20.2 #11]

③ BOZUK KLİPTE TEŞHİS SIRASI (tek değişken):
   1. aynı kare + aynı prompt, bir kez daha (varyans mı?)
   2. hâlâ bozuksa PROMPT: kilidi sadeleştir, TIMELINE'ı ≤3 satıra indir,
      kamera cümlesini kontrol et, tırnak var mı bak
   3. hâlâ bozuksa KARE: denge (§3 ②), oran (§3 ①), yüz (§3 ③), baskın
      ince ayrıntı (§3 ⑤) → IMAGE yeniden üretilir
   Her adımda YALNIZ bir şey değişir; değişen şey kayda yazılır.

④ KAYIT (her üretim): MOTOR `OMNI` · model kimliği arayüzden · ÇÖZÜNÜRLÜK ·
   tarih · kare dosyası · prompt dosyası/satırı · sonuç (kabul / red +
   AŞAMA / bozuk + belirti). Sürüm arayüzde değişirse o günden sonraki
   klipler ayrı işaretlenir.

```

---

# 8. 🔗 ZİNCİR MODU VE UZATMA — ⬜ sahip kararı

> 🆕 **22.09.2026 · SAHİP KARARI — yatay filmde ZİNCİR KULLANILMAZ.** Son kare zinciri
> tamamen devreden çıktı. Her klip yalnız ① TEK BAŞLANGIÇ KARESİ ile, **kendi**
> onaylı imajından üretilir. ② ve ③ yeni yatay filmde açılmaz. Klipler arası
> süreklilik metinle (durum kilidi · sahne kilidi) ve kare onayıyla kurulur →
> `COK_KLIPLI_SAHNE_KILAVUZU.md` §3. Aşağıdaki blok faz hattının (§2.5) ve tarihsel
> kaydın içindir.

```
OMNI'de üç yol var; depo bugün yalnız ① kullanıyor.

① TEK BAŞLANGIÇ KARESİ (bugünkü hat)
   her sahne kendi onaylı karesinden; zincir KESMEDE kurulur.
② BAŞLANGIÇ + BİTİŞ KARESİ (`<FIRST_FRAME> <LAST_FRAME>`)
   faz hattının start/end zinciri OMNI'yle de kurulabilir
   (KESINTISIZ_VIDEO_URETIM_TEKNIGI · D69: biniş/iniş videonun İÇİNE
   yazılmaz). Flow arayüzünde kutunun görünürlüğü sınanmadı.
③ UZATMA (extend) — önceki 10 s okunur, 40 s'ye kadar, yalnız sona
   ızgara sahne = klip = 10 s olduğu için hat dışı; konuşan videoya
   diyalog eklenemez (resmî).

⚠️ THE_SCOURED_GLASS/00_PLAN "end frame yok (OMNI)" yazıyor — 1.1 için
   YANLIŞ. Plan ya ② ile güncellenir ya ① için "bilinçli tek kare"
   gerekçesi alır. Film dosyasına bu kılavuz dokunmaz.
```

---

# 9. 📝 ŞABLONLAR — V3 + OMNI katmanı (sınanmamış iskelet)

> `NEGATIVE:` bloğu `KILAVUZ_REHBERI` §5.1 çekirdeğinin 8 cümlesidir, burada
> yer tutucu olarak durur (kopyası V3 örneğinde). Pozitif gövde 120-300 kelime.
> ⭐ işaretli satırlar OMNI katmanıdır (§2).

### 9.1 Sessiz iç mekân — prosedürel iş (en güvenli tip)

```
IN FRAME: torso · hands
Scene 7 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
His right glove works the stiff valve wheel a quarter-turn at a time, and by the cut it has moved three notches.

TIMELINE: 0.0s — both gloves on the rim, his weight already leaning into the wheel; it gives a finger's width and grips again. 4.0s — he resets his right hand higher on the rim and pulls again, left forearm braced flat against the bulkhead. 7.0s — he keeps pulling at the same slow rate, each breath lifting his chest plate under the harness; nothing in the grip relaxes through the last second.

CAMERA: 35mm lens on a fixed locked-off tripod 1.8 m from the valve bay, camera height 1.30 m, eye-level medium shot, side-on to him, fixed lockoff. In a single continuous shot.   ⭐

PHYSICS: normal gravity inside the module; real time, normal human pace; the wheel resists and moves only while he pulls; both boots stay planted on the deck.
AUDIO: a steady low fan hum; a dry metal creak with each pull; his breathing inside the helmet. No dialogue. No music.   ⭐

NEGATIVE: <REHBER §5.1 çekirdek — 8 cümle> <+ ≤3 sahneye özel>

Output: 16:9, no text, no watermark.
```

### 9.2 Replikli günlük — MCU, basınçlı iç (⛔ PROB ① sonrası)

```
IN FRAME: face · torso
Scene 12 of 180. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; face, light and room carried from the frame, nothing re-described.
He speaks one short sentence to the lens and keeps his eyes on the lens for the whole clip.

TIMELINE: 0.0s — his right hand comes off the record button on the table and rests flat beside it, eyes on the lens. 2.0s — <PROB ① kazanan kolu: A "He says: The leak is closed and the habitat holds pressure." · B "He speaks the line: "…"">. 6.0s — he keeps looking into the lens, his shoulders rising and falling with each slow breath, his thumb rubbing the edge of the table at one steady rate.

CAMERA: 28mm lens on a fixed mount 0.6 m from his face, eye level, medium close-up, the lens looked into directly, fixed lockoff. In a single continuous shot.   ⭐

PHYSICS: normal gravity inside the habitat; real time, normal human pace.
AUDIO: close microphone; the low hum of life support behind him; one mechanical click at 0.0s. The line is heard only, never shown as text. No subtitles. No music.   ⭐

NEGATIVE: <REHBER §5.1 çekirdek — 8 cümle> <+ §5.2 diyalog satırı>

Output: 16:9, no text, no watermark.
```

### 9.3 Sessiz dış mekân — ince atmosfer, süreç yürüyüşü

```
IN FRAME: full body
Scene 31 of 48. Duration 10 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and terrain carried from the frame, nothing re-described.
He hauls the loaded sled up the slope one braced step at a time, and by the cut he has covered a third of the frame width.

TIMELINE: 0.0s — both boots planted, weight on the front foot, the tow strap taut over his right shoulder; he leans forward and takes the first step. 4.0s — the sled runner catches on a rock; he plants both boots, leans harder into the strap and it slides free. 7.0s — he keeps climbing at the same slow rate, one step for every two seconds, the strap staying taut through the last second.

CAMERA: 50mm lens on a fixed locked-off tripod 12 m away, camera height 1.50 m, eye-level wide shot, the slope rising left to right, fixed lockoff. In a single continuous shot.   ⭐

PHYSICS: about a third of Earth's weight; thin cold air; each boot lifts a small puff of fine dust that drops straight back within a second; the sled keeps its momentum only while the strap is taut; both boots touch the ground on every step, never hovering.
AUDIO: muffled — only his breathing inside the helmet and the suit fan; the scrape of the runner on rock, faint through the shell. No dialogue. No music.   ⭐

NEGATIVE: <REHBER §5.1 çekirdek — 8 cümle> <+ ≤3 sahneye özel>

Output: 16:9, no text, no watermark.
```

---

# 10. 🧪 AÇIK PROB'LAR VE SAHİP KARARLARI

```
PROB  ① TIRNAK — §5 ② iki kol, 2 klip. THE_SCOURED_GLASS S12'den ÖNCE.
PROB  ② UZUNLUK — aynı sahne ~80 ↔ ~250 kelime pozitif gövde, 2 klip.
      Ölçüt: kilit tuttu mu · kayma · ölü saniye.
      ARAYÜZ ③ Flow ekran görüntüsü: seed alanı · bitiş karesi kutusu ·
      süre seçenekleri · çözünürlük · ses anahtarı. 0 kredi.
ÖLÇÜM ④ İlk OMNI klibinde ffprobe süre ve kare hızı → D124 satırı.
PROB  ⑤ SABİT KAMERA — "absolutely zero camera movement" ↔ "mounted on a
      fixed tripod", 2 klip; özne mikro hareketi söner mi.
PROB  ⑥ DAMGA — "0.0s —" ↔ "[0-3s]", 2 klip; ① KARE metin bayrağı +
      hareket. (TUR 19 ② ile tek koşu.)
KARAR ⑦ Zincir modu (§8): ① tek kare mi, ② başlangıç + bitiş karesi mi.
KARAR ⑧ Ses kimliği (§5 ④): post-dub mı, değişim kabul mü.
```

---

# 11. ✅ PLAN KONTROLÜ — OMNI motorlu film üretime girmeden

```
□ Film planında MOTOR satırı OMNI ve ZİNCİR MODU açık yazılı (§8)
□ Her video promptunda CAMERA satırı var ve "In a single continuous shot." ile bitiyor
□ Her video promptunda AUDIO satırı var; sessiz klipte "No dialogue. No music."
□ Video promptlarında tırnak işareti yok (replik PROB ①'e bağlı)
□ START FRAME satırı var; görünüm yeniden tarif edilmiyor
□ Başlangıç kareleri çıkış oranında; eylemin ortası AMA iki destek noktası yerde
□ Kilit fiili yüzü döndürmüyor, kapatmıyor, kadrajdan çıkarmıyor
□ Replikli klip varsa: PROB ① koşuldu · MCU · basınçlı iç · ses kimliği kararı (§5 ④) yazılı
□ İş akışı: çekim seçimi 720p'de; seed'e dayanan adım yok
□ Kayıt şablonunda MOTOR · ÇÖZÜNÜRLÜK · AŞAMA sütunları var
```

---

# 12. 📚 KAYNAKLAR

```
Süzme      URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md §TUR 20
Ham        URETIM_ONCESI_ANALIZ/TUR20_HAM_RAPORLAR/ (9 rapor + 00_KUNYE §🔎)
Promptlar  URETIM_ONCESI_ANALIZ/23_OMNI_1_1_FLASH_I2V_ARASTIRMA_PROMPTLARI.md
Resmî      G1 blog.google — "Gemini Omni 1.1 Flash lets you build with more control" (27.08.2026)
           G2 ai.google.dev/gemini-api/docs/omni — "Generate and edit videos with Gemini Omni Flash"
Gözlem     segmind (çözünürlük korelasyonu) · mindstudio (tek prompt testi, arena sırası) ·
           promptslove (sözdizimi iddiaları, sınanmamış) · the-decoder (fiyat, taslak hızı) ·
           discuss.ai.google.dev #178261 (red vakası)
Depo       IMAGE_VIDEO_PROMPT_TEMPLATES V3 · SAHNE_DOLULUGU · VEO_3_1_FAST §6B/§7 ·
           POLITIKA §5/§6 · DIYALOG_SAHNESI BASAMAK 2 · SES_VE_DIYALOG · D34 · D40 ·
           D45 · D69 · D79 · D124 · D142 · D167
```
