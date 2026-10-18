# 🧭 DURUM — THE_FURNACE_GATE

> `/yeni-film` her açılışta önce bu dosyayı okur. `ADIM`: faz 3'te `çekim` | `sahneleme`, diğer fazlarda `—`. Faz geçişinde, her ajan çağrısından
> sonra ve sahibe soru sorulduğunda güncellenir. Alanların adını değiştirme
> (`film_dogrula.py` okur).

```
FAZ          7
ADIM         —
TUR          1
SIRADAKI     F7 SAHİPTE (15.10): Flow ses AÇIK · önce SMOKE P14 (referans sayfası) + P18 (model sesi: Leon C03 C07 C11 · Rhea C04 C08 C10 · telsiz C02 C06 C13 · VO C01) → 15 referans sayfası (sıra 10 · 15 önce, PROMPTLAR/G01.md REFERANS PROMPTLARI) → SHA → Fable + devamlilik (kare) → kareler C01-C03 önce (ILK_30 §6) → riskli ilk denemeler C60 C86 C74 C84 (×2) → kalanlar Flow iş emri sırasıyla. Dönüşte /yeni-film. · FRAGMAN dikey 0:40 (17.10): `THE_FURNACE_GATE_FRAGMAN_DIKEY.md` hazır (8 çekim, 16 prompt) — üretimi filmin referans onayından sonra: V1a → dur (Fable + devamlilik) → V4b (V1a.png'den) → kalanlar. · QA P4 (18.10): sahip taslak_01'i hat dışında üretti ve kurdu (medya hatta YOK: ref 0/15, ham 0) → önce `ODA/QA_YENIDEN_TEST_BOLUM_4.md` TEST 0 (/medya-denetle) + TEST 1 (KARE MODU) + TEST 5 (kimlik sayfası → devamlilik) → sahip kararları K1-K6 (`ODA/QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU_BOLUM_4.md` §6) → kurgu 5.1 → yeniden üretim 5.2 (C94 C74 C80 C81 C92 önce). P3 ham raporu (`ODA/HAM_QA_RAPORU_BOLUM_3.md`) NOTLAR'a işlenmedi.
AJAN_CAGRI   31 / 50
FLOW_KREDI   0
SON_GUNCEL   18.10.2026
```

## AÇIK ÖLÜMCÜL BULGULAR

| Faz | Bulgu | Kaynak (ODA dosyası) | Durum |
|:--:|---|---|---|

## AŞILAN KAPILAR — yayın onayında sahibe gösterilir

| Tarih | Faz | Madde | Denetçi dedi | Fable gerekçesi |
|---|:--:|---|---|---|
| 13.10.2026 | 1-4 | F1 aday turu (senarist · dramaturg · yonetmen · izleyici) · F2 tretman eleştirisi · F3 çekim listesi eleştirisi (teknik · izleyici metin animatiği) · F3b sahneleme · F4 ses/müzik ajanları açılmadı | çağrılmadı | Sahip tam planı dosya olarak verdi ve "plana uyarak filmi yapalım" dedi (THE_PLANET_THIEF · THE_MAYDAY_SEA yolu); hikâye seçimi sahibin onayı sayıldı. §1-§7 plandan yerleşti; §3 sabit cümleler, §6 yatak + geçiş, §5 kaynak/saniye Fable çevirisi (NOTLAR KARARLAR). Mekanik kontrol (film_dogrula kunye hikaye cekim replik muzik) geçerli; tek uyarı 95 replik > 70 bandı, gerekçe §5 altında. İstenirse izleyici metin animatiği (1 çağrı) sonradan koşulabilir. |
| 13.10.2026 | 6 | F6 kapak konsepti (kapak-tasarimcisi · izleyici · yonetmen · yayin) açılmadı | çağrılmadı | Plan tek kapak tabanı promptu ve üç başlık verir; KAPAK_VE_YAYIN §1'e yerleşti (referans anahtarı eklendi, olumsuz kuyruk çıkarıldı). Kapak yazısı (plan: film adı) hat kuralıyla çatışır → F9'da sahip seçer. Tek değişkenli B F9'da kapak-tasarimcisi'nden. |
| 15.10.2026 | 5 | F5.7 panel↔çekim uyumu + sayfa yazısı yokluğu · F5.8 C74 ilk vuruş · F5.2 kimlik cümlesi birebir sayımı · Ö4 G04/G06/G08 örneklem dışı K kararları | DOĞRULANAMADI (❌ değil; `ODA/F5_denetci_2.md`) · F5.10 ❌ → Fable düzeltti | F5.10: FILM §4 Risk C03 (vizör/yüz, ILK_30 §6) + telsize çevrilen C02 C13 C17 C19 C24 C36 C79 C90 hücreleri güncellendi. Kalanlar yargı maddesi: 15 sayfa ve 96 kare F7 kare kapısında devamlilik (kare modu) + Fable tarafından görsel olarak denetlenir; kimlik tabanı tur 1'de devamlilik'çe 24/24 KORU, mekanik tarama (ad · kısaltma · kırmızı kelime · ORTAK GÖRÜNÜM 192/192 · replik 95/95) temiz. |
| 18.10.2026 | 9 | F9 yayın paketi F7-F8'den ÖNCE (başlık · açıklama · etiket · sabit yorum · Shorts) | çağrılmadı (denetçi yok) | Sahip isteği: "youtube için başlık ve açıklama full hali için full İngilizce profesyonel". Saniyeler planlanan (FILM §2); F9.1-F9.3 F9.7 (izleme formu, anlatım testi, final kapak, deney defteri) üretimden sonra. `film_dogrula --bolum yayin` ✅. |

## SAHİP CEVAPLARI

| Tarih | Konu | Cevap |
|---|---|---|
| 13.10.2026 | Konu · format · karakter | Sahip hazır planı dosya olarak verdi: THE FURNACE GATE, yatay 16:9, 16:00 = 96 × 10 s, iki görünen/konuşan karakter (Leon · Rhea Vance). "16dk filmle film ismiyle bir klasör oluştur ve o dosyayı da içine koy ve … dosyaya plana uyarak filmi yapalım ama önce" (cümle yarım kaldı). Plan dosyası birebir: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` (SHA-1 597df296…; kaynaktır, düzenlenmez). |

| 13.10.2026 | "ama önce" (yarım cümle) → ne önce | "Plan farklarını düzelterek başla" → hikâye, olaylar ve diyaloglar plandaki gibi; hat kurallarıyla çatışan kalıplar F5 çevirisinde düzelir (NOTLAR KARARLAR sapma listesi 1-7). |
| 13.10.2026 | Replik sesi | "Model sesi: video konuşsun" → §5 Kaynak = model sesi (ağız kadrajda · telsiz · voice-over); planın "kurguda ayrı kayıt" yöntemi yedek. |
| 13.10.2026 | Sıradaki | "sonrasında filmi yapmaya başla" → F5 açıldı. |
| 13.10.2026 | PLANDAN SAPMA — sahip ONAYLADI 14.10.2026 ("sapmaları onaylıyorum devam et"; plan olayları korundu) | (1) R03 ikili ana kare kaldırıldı · (2) hook VO 2,0 s'den · (3) prompt kalıpları (olumsuz kuyruk · araç etiketi · "first frame" · atıf) kalkar · (4) 10 s vuruş planı · (5) son kareden başlatma yok · (6) kapakta film adı yazısı F9'a · (7) C48 taraf notu. Ayrıntı NOTLAR KARARLAR. Sahip "hayır" derse plan metnine dönülür. |
| 14.10.2026 | Plandan sapmalar (1-7) | ONAY: "sapmaları onaylıyorum devam et". |
| 14.10.2026 | dead/dies replikleri (R21 R38 R52 R65) | "Değiştir" → R21 "…even if power fails." · R38 "The gate drive has no power. …" · R52 "… still locked." · R65 "… before the core fails." (FILM §5; plan metni dosyada birebir kalır). |
| 14.10.2026 | C86/C88/C95 iki konuşan aynı klipte | "Önce dene, karışırsa yedek" → plan kompozisyonu; C86 ilk denenir; karışırsa GOSTERIM Örnek C (konuşan başına tek yüz, cevap kadraj dışından). |

## FAZ GÜNLÜĞÜ

| Tarih | Faz | Olay |
|---|:--:|---|
| 13.10.2026 | 0 | Klasör açıldı (`yatay_16_dk_filmler/THE_FURNACE_GATE/`, SABLON kopyası) · medya ağacı `~/film_medya/THE_FURNACE_GATE/` · sahibin planı kökten klasöre taşındı. |
| 13.10.2026 | 1-4 · 6 | FILM.md §1-§7 plandan yerleştirildi (Fable; biçim çevirisi: 15 referans numaralandı + panel adları, 96 çekim 8 grup, 95 replik model sesi, saniye/süre tahmini; §6 yatak Y1-Y9 + 95 kesme geçiş; §7 plan müzik promptu) · KAPAK_VE_YAYIN §1 plan kapağı. Ajan çağrısı 0. film_dogrula kunye hikaye cekim replik muzik ✅ (⚠️ replik bandı). Kapılar sahip kararıyla aşıldı (AŞILAN KAPILAR). |
| 13.10.2026 | 5 | F5 açıldı: goruntu-yonetmeni G01-G08 paralel çağrıldı (çağrı 1-8). |
| 14.10.2026 | 5 | 8 grup yazıldı (G03 · G05 · G08 limit/uyku kesintisiyle SendMessage devamında) → film_dogrula hepsi ✅ (96/96, ⚠️ replik bandı) → ilk sürümler ODA/F5_goruntu-yonetmeni_1_G0x.md → devamlilik ×2 + teknik-danisman ×2 (çağrı 9-12; 96 çekim tek çağrıya sığmadığı için C01-C48 / C49-C96 yarıları): ÖLÜMCÜL 0, CİDDİ 33, KÜÇÜK 39 → tur açılmaz; birleştirme kararları dönüşte. Sahip: sapmalar ONAY; ara. |
| 15.10.2026 | 5 | Birleştirme turu 1b (sahip: üçer üçer, Sonnet): 7 yeni goruntu-yonetmeni (çağrı 13-19) → G04 G08 promptları §K'yla yeniden · G01 G02 G03 G05 G07 §K raporları · yazarların birebir eski→yeni metinleri Fable'ca yerleştirildi (1+13+3+2+7) → FILM §5 saniye/Kaynak, §3/§4 referanslar EKLE'den, P18 notu → film_dogrula hepsi ✅ → denetci (çağrı 20, sonnet) 20 tur sınırı: ❌ yok, KAPANAMAZ (kanıt eksik: G04-G08 Ö3-Ö5, F5.4 FLOW 96/96, F5.6-F5.8 F5.10) → ODA/F5_denetci_1.md → SendMessage devamı → ODA/F5_denetci_2.md KAPANABİLİR (mekanik ❌ yok, yargı F5.10) → Fable §4 Risk düzeltti → **F5 KAPANDI** → FAZ 7 sahipte. |
| 17.10.2026 | fragman | Sahip: "40 saniyelik dikey fragman · 4 sahne · her sahneye max 1 cut" → `THE_FURNACE_GATE_FRAGMAN_DIKEY.md` (FRAGMAN_KILAVUZU §2; film sayımına girmez, PROMPTLAR/ dışında). Kart v1 İKİ IŞIK → izleyici + dramaturg (ÖLÜMCÜL 2: soru filmin ortasında cevaplanıyor, V4 merkez seçim) + teknik-danisman → kart v2 **KISKAÇ** (ateş · kelepçe · alarm · kapı; soru: kapı kapanmadan gemi çıkabilecek mi) → izleyici 2 ("evet, izlerdim") → goruntu-yonetmeni 8 çekim + besteci 40 s cue → devamlilik + teknik 2 (ÖLÜMCÜL 2: V3b siren, V4b açılıyor okunması) → birleştirme (`ODA/FR_birlestirme_1.md`) → yazar tur 2 → Fable yerleştirme + mekanik kontrol (16 blok ≤2.490, yasak 0, çapalar birebir). 9 çağrı (21-29), hepsi sonnet. Üretim 0. |
| 18.10.2026 | 9 (erken) | Sahip: YouTube başlık + açıklama (tam İngilizce). yayin (sonnet, çağrı 30) `YAYIN_PAKETI.md`'yi doldurdu (6 başlık, öneri "4,000 Sleeping People Are Marked as Scrap \| THE FURNACE GATE" 60 kr; plan açıklamasının spoiler cümleleri çıktı; 8 bölüm; #spaceheist #scifishortfilm #space; sabit yorum fizik yerine yapım cümlesi + karar sorusu) → Fable düzeltti (başlık 4 sayımı, şablon yer tutucuları, WATCH NEXT bloğu, Shorts başlığı soru işaretsiz, sabit yorum dili) → izleyici (sonnet, çağrı 31) `ODA/F9_izleyici_1.md` → açıklamanın ilk satırına dört bin uyuyan, "burn cradle" çıktı → `--bolum yayin` ✅. Açık: sabit bloktaki "Made with" satırı bu filmle uyuşmuyor (sahip). İlk sürüm `ODA/F9_yayin_1_YAYIN_PAKETI.md`. |
| 18.10.2026 | 7-8 (hat dışı) | Sahip taslak_01 4. parça (C73–C96) dört QA raporunu getirdi → ham `ODA/HAM_QA_RAPORU_BOLUM_4.md` · Fable işledi (alt ajan yok, çağrı 31/50 değişmedi): QA_OKUMA protokolü, timeline yok → içerik çapası (22 replik saniyesi §5'le örtüşüyor), G07/G08 promptlarından alıntı → 60 birleşik bulgu (geçici 🅐 27 · 🅑 14 · 🅑+ 3 · 🅒 11 · ? 5), anlatım 16 ✅ · 5 ⚠️ · 3 ❌ (C74 C80 C81) → `ODA/QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU_BOLUM_4.md` + `ODA/QA_YENIDEN_TEST_BOLUM_4.md` (TEST 0-7) + NOTLAR P4 satırları. Kaynaklar geçersiz işaretli (>90 s · ne olmalı yok · Türkçe · izleme B simülasyon). Örüntüler: tug kimliği (8 dış çekimde 3-4 araç) · rozet konumu/bayrak (KİMLİK TABANI'nda konum ve "only marking" yok) · klip sesi pencereye kısılmamış · vakumda ateş (C91 C92). Kural ④ sorusu sahipte (K6: araç kimliği PLANET_THIEF + FURNACE). |
