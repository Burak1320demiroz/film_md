# 🧭 KILAVUZ REHBERİ — Buradan Başla

> **Bu dosya içerik anlatmaz, ADRES verir.** Detay kaynak kılavuzlarda kalır;
> burada özetlenirse ikisi ayrışır ve hangisinin doğru olduğu kaybolur.
> **Tek istisna:** Bölüm 5'teki negatif çekirdek — onu her sahnede fiilen
> kullandığın için burada tam metin olarak duruyor.
>
> Yapıyı tek bakışta görmek için: `YAPI_GRAFI.md`

---

# 1. 🎯 DÖRT SORU → OKUMA LİSTEN

Yeni bir filme başlarken **sırayla** cevapla. Her cevap bir sonrakini daraltır.
(Ağaç hali: `YAPI_GRAFI.md` Bölüm 1)

```
① YÖN?    dikey (9:16) ──► SHORTS — dal burada biter, süre §2.1'den
                                 ÖLÇÜLÜR (araçtan, D124 — sabit değil)
          yatay (16:9) ──► ② ye devam
② SÜRE?   2-4 dk / 3-5 dk / 7-9 dk / 10-20 dk           → YAPI
③ TÜR?    bilimkurgu — TEK AÇIK TÜR (26.08.2026)          → İÇERİK
          ⛔ Bu depo yalnız UZAY filmleri içindir. ③ artık bir seçim
             değil bir DOĞRULAMADIR: "bu gerçekten uzay filmi mi?"
             Değilse konsept reddedilir, klasör açılmaz.
          ⏸️ zombi RAFTA (26.08.2026 — klasör ve dört film kaldırıldı,
             kartı §4.2'de duruyor)
          ⏸️ savaş RAFTA (12.08.2026 — klasörü kaldırıldı, kartı §4.3'te
             duruyor)
④ ORTAM?  karasal türler  → Dünya atmosferi (SABİT, sorma)
          bilimkurgu      → §3'ün ON KARTINDAN biri (ya da birkaçı)
                            3.1 vakum · 3.2 ince atm. · 3.4 kalın atm. ·
                            3.5 itki g · 3.6 nötr yüzerlik · 3.7 dönme g ·
                            3.8 soğuk kaynak · 3.9 kriyojenik ·
                            3.10 basınçlı iç hacim 🆕          → FİZİK
          ⚠️ Sahne İÇERİDE geçiyorsa kart 3.10'dur, dışarıdaki kart
             DEĞİL: iç hacimde §3.1'in üç kuralı birden ters döner.
```

> ④ ayrı bir eksen değil, ③'ün sonucudur. Sadece bilimkurguda gerçek seçim var.

### Her filmde okunacaklar (değişmez)

> ⭐ **14.09.2026 — bu liste artık HAVUZDUR, çizelge değil.** Yeni film için
> zorunlu okuma iki yerden üretilir: `DERSLER/00_YASAYAN_DERSLER.md` (≤ 40 ders)
> + `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` (≤ 30 dosya manifesti) —
> `okuma_cizelgesi.sh` ikisinden çizelge basar, her satırdan kilit çıkmaz ("—"
> meşru, `prompt_kontrol.py` ㉘). Aşağıdaki kutulardan manifestte OLMAYANLAR
> filmin türü/ortamı gerektirdiğinde açılır ve çizelgeye "havuzdan açıldı"
> satırıyla eklenir. Ölçüm: eski "hepsi" çizelgesi 126 dosya / ~42.000 satır,
> 126/126 sahte kilit (THE_LOCKED_PULSE).

```
□ Bölüm 5 — NEGATİF ÇEKİRDEK  (bu dosyada — 14.09: prompta §5.1 8 cümle,
  tam liste §5.3 PLAN'a)                                        [manifest]
□ Bölüm 7 — BİLİNEN TUZAKLAR  (bu dosyada, tam metin)          [manifest]
□ VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md
□ OMNI_1_1_FLASH_I2V_URETIM_KILAVUZU.md 🆕 (MOTOR OMNI ise ZORUNLU — V3 üstüne
  yedi satırlık katman: tek-plan cümlesi · "No dialogue" · tırnak yok · kare
  dengede · 720p'de seçim · seed'siz iş akışı · zincir modu ⬜ · 16.09.2026 · TUR 20)
□ COK_KLIPLI_SAHNE_KILAVUZU.md 🆕 (yatay filmde ZORUNLU — sahne 2-6 klip ·
  kapsama şablonu · CONTINUOUS ACTION durum kilidi · sahne kilidi · zincir yok ·
  ㉜ · 22.09.2026 sahip kararı · §2.0b)                           [manifest]
□ SAHNE_DEVAMLILIK_KILAVUZU.md   (karakter çapalama, seed)
□ UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md (kuşbakışı harita → ekran
  yönü çevirisi · sabit hedefe hareket/koşu/yaklaşma varsa ZORUNLU)
□ YANASMA_VE_KENETLENME_KILAVUZU.md (iki gövdenin yanaşma/kenetlenme
  sekansı varsa ZORUNLU · güvenli kadraj seti + ses/dramaturji kalıbı —
  17.08.2026, kanıt tabanı: Cold Burn · Ring Light · Black Cradle)
□ IMAGE_VIDEO_PROMPT_TEMPLATES.md (V3 iskelet — IN FRAME · bütçe · START FRAME;
  V2 eski klasörler için · 14.09.2026)                          [manifest]
□ SINEMATOGRAFIK_TEKNIK_KILAVUZ.md §17 (karar tablosu: hangi teknik
  prompta yazılır / post'ta yapılır / hiç girmez)
□ TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md §5 (sahne sınırları: gizli
  geçiş mi, bilinçli sert kesme mi — sahne haritası yazılırken karar)
□ HIKAYE_FIKIR_TURU_KILAVUZU.md 🆕 (yeni-film 0.7a — klasör açılmadan,
  başka hiçbir dosya okunmadan: gerilim → üç yöntem × 8-12 logline → beş
  evet/hayır eleme → üç aday → sahip onayı; creative-director'dan damıtıldı,
  CC BY 4.0 atıflı · MANİFESTTE DEĞİL, çizelgeden önce koşar · 21.09.2026 · TUR 23)
□ ONERME_VE_NOVUM_KILAVUZU.md (KONSEPT kapısı: novum tipi + taşıyıcı
  satırı + üç kabul testi — vuruş tablosundan da sahne haritasından da
  ÖNCE; geçmeyen konsept plana dönüşmez · 22.08.2026)
□ SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md (vuruş haritası §2 sahne
  haritasından ÖNCE doldurulur · loop/kamera psikolojisi)
□ HOOK_VE_ILK_SAHNE_KILAVUZU.md (ilk iki sahne: S0 karar + S1
  tırmandırma · hook tipi plana yazılır — vuruş tablosundan SONRA,
  sahne haritasından ÖNCE)
□ FINAL_VE_PAYLASIM_KILAVUZU.md (final tipi + tohum bilgi + görsel
  ikilem — hook'un karşı ucu; tohum ilk %10-15'e düştüğü için filmin
  BAŞINI da değiştirir · 22.08.2026)
□ SES_VE_DIYALOG_URETIM_KILAVUZU.md (filmde replik VEYA ses tasarımı
  varsa ZORUNLU · register haritası + replik bütçesi + AUDIO kalıpları —
  yazım tarafı; ölçüm tarafı 7c'de kalır)
□ KARAKTER_VE_DUYGU_KILAVUZU.md (bağ kurma bütçeleri: göz · Kuleshov
  döngüsü · el/nefes/yürüyüş/eşya · isim-istek-bedel saati — SAHNE
  HARİTASI yazılırken dağıtılır, üretimden sonra eklenemez · 22.08.2026)
□ KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md 🆕 (B5'ten SONRA, sahne haritasından
  ÖNCE — Character Bible görünüşü, KART davranışı kilitler: sekiz satır ·
  alışkanlık ≥3 tekrar + 1 kırılma · karar mimarisi (reddedilen nesne
  kadrajda) · DAVRANIŞ ŞERİDİ · 11.09.2026 · TUR 15)
□ OYUNCULUK_YAZIM_KILAVUZU.md 🆕 (⑩ OYUNCULUK rubriğinin YAZIM ikizi —
  sahne çalışması ve TIMELINE yazılırken her sahnede: izleyici cümlesi ·
  ÇAPA ÜÇLÜSÜ (SEÇİM/BEDEL/FİNAL önce-sonra beden çifti → QA_SPEC) ·
  sekiz niyet kanalı sözlüğü · tempo kontrastı · anti-RESET ·
  11.09.2026 · TUR 15)
□ IKI_KISI_VE_AYRILIK_KILAVUZU.md 🆕 (YALNIZ ikinci insan varsa — iki kart
  ≥3 satırda ayrışır · faz farkı (aynı anda aynı şey YOK) · cevap ızgarası
  kanal × içerik · gecikme bandı · mesafe eğrisi · AYRILIK KARTI ·
  temassız anlaşmazlık · 11.09.2026 · TUR 15)
□ DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md 🆕 (YALNIZ replik varsa — replik
  tablosundan SONRA, DIALOGUE_CRITIQUE'ten ÖNCE: muhatap tipolojisi ·
  DEĞİŞ-TOKUŞ tablosu (hamle · cevap · gecikme · dinleyenin bedeni ·
  DEĞİŞİM) · sessizlik cevaptır · dinleyen kadrajı · değer kayması testi ·
  11.09.2026 · TUR 15)
□ KURGU_RITMI_VE_IHRAC_KILAVUZU.md §1-2 (ASL bandı SPEC'e yazılır ·
  örüntü kırıcı kapısı sahne haritasında koşulur · 22.08.2026)
□ PAKETLEME_VE_VAAT_KILAVUZU.md (KAPAK ANI sahnesi plana yazılır ·
  vaat-teyit penceresi · dört yüzeyli spoiler bütçesi [D114] — sahne
  haritası yazılırken · 22.08.2026)
□ TEMA_MUHENDISLIGI_KILAVUZU.md (PLAN adım 1'de logline yazılırken —
  tema seçimi + format-süre uyumu + tema→motif→sahne matrisi · 22.08.2026)
□ KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md (sahne haritasında kamera satırları
  yazılırken — vuruş→açı tablosu + abartı eşikleri · 22.08.2026)
□ ACI_YAYI_VE_SEKANS_KILAVUZU.md (kamera satırları TOPLUCA dizilirken —
  sıçrama bandı + kurulum sayısı + yay şablonları · 22.08.2026
  🆕 05.09.2026: §3 🕰️ KÜME · §4b DÖNÜŞ HEDEFİ · §7 ⑥ birebir yazım —
  sıçrama kalkanı verir, DÖNÜŞ haritayı verir)
  ⭐ §4b'nin saha kanıtı → DIS_REFERANS_OLCUMU.md §2 (zorunlu okuma DEĞİL;
    kural sorgulanınca veya yeni referans gelince açılır)
□ SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md 🆕 (iki sahnenin ARASI — sahne
  haritasına açık kalan SORU ve cevap TİPİ sütunlarını yazdırır ·
  ardışık aynı cevap tipi yasağı · sınır satırı (End/Start) ·
  ⛔ durum değişimi klibe değil SINIRA yazılır · 04.09.2026)
□ SAHNE_DOLULUGU_KILAVUZU.md 🆕 (birimin İÇİ — sahne tablosu ve TIMELINE
  yazılırken her sahnede: kilit fiili SÜREÇ (erişme ancak dirençle) · imaj
  eylemin ORTASINDAN · TIMELINE ≤3 satır, son satır SÜRDÜRME ("settles /
  then stops" yazılmaz) · tek çevre saati · ölü sahne beş sorusu ·
  15.09.2026 · TUR 19)
□ ACILIS_KAPANIS_CIFTI_KILAVUZU.md 🆕 (ilk kare ile son kare TEK karar —
  çift kartı sahne haritasından ÖNCE doldurulur · kanca ve final tipini
  seçmez, ikisinin BAĞINI yazar · 04.09.2026)
□ UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md 🆕 (kadrajda istasyon, üs
  ya da büyük yapı varsa ZORUNLU — ölçek birimi + anatomi kartı + mesafe
  kesir tablosu + iki ayrı negatif blok · 04.09.2026)
□ REFERANS_PAKETI_KILAVUZU.md 🆕 (⚠️ **İSTEĞE BAĞLI** 🆕 08.09.2026 · sahip
  kararı — eskiden altı tetikleyiciden biri doğruysa ZORUNLU'ydu. §1 tablosu
  yine okunur; T1 "kask/vizör/basınç giysisi" bu deponun neredeyse her
  filminde doğrudur, yani tetikleyici genelde AÇIKTIR ve atlanıyorsa PLAN'a
  TEK SATIR gerekçe yazılır [D74 kalıbı]. Paket YAZILDIYSA kapı sertliğini
  korur: KAPI 0, onaysız sayfanın varlığı geçtiği sahne üretilmez. PROMPT
  yazılmadan ve İLK KARE ÜRETİLMEDEN önce okunur: KAPI 0. Kapı kartı 31
  satır; gövde yalnız ① yeni film · ② biçim iki klipte sapmış · ③ üretim
  ortasında tasarım değişmiş · ④ insan dışı canlı/tekrar eden olay varsa
  açılır · 06.09.2026 · TUR 12)
□ MESHUR_SAHNE_KALIPLARI_KILAVUZU.md (vuruşa görsel karşılık veya kapak
  anı aranırken — 20 hazır kalıp + homage/telif sınırı · 22.08.2026)
□ FILM_KAPAGI_KILAVUZU.md 🆕 (akış adım 10 — her filme İKİ kapak adayı A·B, tek deney
  sorusu; an PLAN'dan; metinsiz prompt + Bible cümleleri; 160×90/320×180 kontrolleri;
  Studio A/B → 08 tablosu; sayılar DIS_SAYILAR §1 · 20.09.2026 · kaynak
  URETIM_ONCESI_ANALIZ/26_ sahip araştırması)
□ YOUTUBE_VIRAL_SANS_KILAVUZU.md 🆕 (konu → paket → açılış → ilerleme → ölçüm
  çalışma düzeni: 15 madde → depo adresi · VİRAL KART (satır başına ev) · klip
  kontrol sorusu · 7/14/28. gün takvimi · teşhis tablosu · ⭐ evrensel CTR eşiği
  KAPANDI, görüntülenme sayımı 24.08.2026'da değişti — sayılar DIS_SAYILAR §1 ·
  20.09.2026 · sahip metni)
```

### Formata göre ek okuma

| Format                                     | Ek okuma                                                                                                                                                             |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **dikey shorts**                           | **`DIKEY_MIKRO_DRAMA_KILAVUZU.md`** (9:16 dramaturjisi — sistem promptundan ÖNCE; §4.1 vizör döngüsü · §4.2 vekil nesneler · **§6.1 AI algısı kapısı, konsept seçilirken**) + `HOOK_VE_ILK_SAHNE_KILAVUZU.md` **§3.1 (dramatik ironi — 27.08.2026'da eklendi, dikey hattın en yeni zorunlu bölümü)** + `SHORTS_SISTEM_PROMPTU.md` + Bölüm 2.1 |
| **fragman (dikey 3-6 / yatay 8-12 vuruş)** | **`FRAGMAN_KILAVUZU.md`** + kaynak filmin format kartı · emsal: `THE_COLD_BURN/THE_COLD_BURN_FRAGMAN_DIKEY.md` (dikey) · `THE_SECOND_SHIP/FRAGMAN.md` (çift format)  |
| **2 dk · 12 sahne** (eski adı 2-4 dk)     | Bölüm 2.2 + `yatay_2_dk_filmler/README.md` + referans film: `THE_DEAD_APPROACH`                                                                                                                       |
| **4 dk · 24 sahne** (eski adı 3-5 dk)     | Bölüm 2.3 + `yatay_4_dk_filmler/README.md` + referans: `LOW_POWER/` · çok varlıklı filmde referans paketi örneği: `THE_COLD_BURN/THE_COLD_BURN_REFERANS_PAKETI.md` |
| **6 dk · 36 sahne** 🆕 13.09.2026          | Bölüm 2.6 + `yatay_6_dk_filmler/README.md` (⭐ QA birimi BÖLÜM — tek fark) + 3-5 dk satırının tamamı (yazım aynı)                                     |
| **8 dk · 48 sahne** 🆕 13.09.2026          | Bölüm 2.7 + `yatay_8_dk_filmler/README.md` (⭐ QA birimi BÖLÜM) + 3-5 dk satırının tamamı · ⚠️ faz hattı DEĞİL — 8 dk'da iki hat var, ayrım §2.7/§2.5   |
| **16 dk · 96 sahne** 🆕 19.09.2026         | Bölüm 2.8 + `yatay_16_dk_filmler/README.md` (⭐ QA birimi PART = 2 bölüm dosyası + TAM-FİLM koşusu) + 3-5 dk satırının tamamı (yazım aynı) |
| **32 dk · 192 sahne** 🆕 22.09.2026        | Bölüm 2.9 + `yatay_32_dk_filmler/README.md` (⭐ QA birimi PART = 2 bölüm dosyası [8 PART] + TAM-FİLM koşusu) + 3-5 dk satırının tamamı |
| **64 dk · 384 sahne** 🆕 22.09.2026        | Bölüm 2.10 + `yatay_64_dk_filmler/README.md` (⭐ QA birimi PART = 2 bölüm dosyası [16 PART] + TAM-FİLM koşusu) + 3-5 dk satırının tamamı |
| **7-20 dk**                                | Bölüm 2.5 (kısa uç bloğu dâhil) + `5_FAZ_MIMARISI.md` · `FAZ_DOSYASI_SABLONU.md` · `KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` · emsal: kısa uç `THE_SLOW_STONE/` (üretilmiş tek film) · uzun uç `YERCEKIMI/` |

### Ortama göre ek okuma

| Ortam                                | Ek okuma                                                             |
| ------------------------------------ | -------------------------------------------------------------------- |
| **Vakum**                            | Bölüm 3.1 + Ders 30, 31, 36, 39                                      |
| **Vakum + itki yerçekimi** 🆕        | Bölüm 3.5 (3.1'in alt kartı) + Ders 36 · Ders 23 burada TETİKLENEMEZ |
| **İnce atmosfer**                    | Bölüm 3.2 + Ders 39, 41                                              |
| **Dünya atmosferi**                  | Bölüm 3.3 + Ders 39, 41                                              |
| **Kalın atmosfer**                   | Bölüm 3.4 + Ders 36, 39 (ikisi de TERS çalışır)                      |
| **Sürekli bulut / nötr yüzerlik** 🆕 | Bölüm 3.6 + Ders 41, 59; Ders 39 tetiklenemez (toz yok)              |
| **Vakum + dönme yerçekimi** 🆕       | Bölüm 3.7 + Ders 30, 31, 127; Ders 23 burada ELENİR (hiçbir kare sıfır-g değil) |
| **Vakum + temiz metal (soğuk kaynak)** 🆕 | Bölüm 3.8 + Ders 24, 30, 31, 127, 138; Ders 23 burada ELENİR (sıçrama 0 kare) |
| **Kriyojenik orta basınç (95 K)** 🆕 | Bölüm 3.9 (3.3'ün alt kartı) + Ders 39, 41, 143, 175; Ders 36 ve 24 burada TETİKLENEMEZ |

### Türe göre ek okuma

| Tür                               | Ek okuma                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bilimkurgu**                    | Bölüm 4.1 + Ders 5, 23, 26, 32 + **`UZAY_SENARYO_KILAVUZU.md`** + **`ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md`** 🆕 (kadrajda basınç giysili karakter varsa — Character Bible yazılmadan ÖNCE · 03.09.2026) + **`UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md`** 🆕 (aynı anda, DONANIM ile birlikte — DONANIM kimlik, bu görünüş: arketip · kask · malzeme · renk · sırt tarifi · 12.09.2026 · TUR 17) + **`UZAYLI_VARLIK_TASARIM_KILAVUZU.md`** 🆕 (filme uzaylı/insan-dışı varlık eklenecekse — PLAN yazılmadan ÖNCE, risk kartlarıyla aynı adımda · 03.09.2026 · TUR 7)                                                                                                                                                                                                                                                                                                                     |
| **Zombi** ⏸️ RAFTA (26.08.2026) | Bölüm 4.2 · Kart H2 ile kapatıldı — depo yalnız UZAY filmleri içindir. Dört referans filmin dördü de kaldırıldı; kart bilgi olarak duruyor ama **bu kartla film yazılmaz**. Geri açılırsa kart H + §4.2'nin ALTI SATIRLIK BÜTÇESİ şarttır |
| **Savaş** ⏸️ RAFTA                | Bölüm 4.3 + Ders 38 + **`SAVAS_SENARYO_KILAVUZU.md`** — 12.08.2026'da klasörü ve referans filmi kaldırıldı (dikey `THE_DULL_EDGE` bu kartı kullanmaya devam eder)                                                                                                                                                                                                                   |
| **Yeni tür**                      | Bölüm 4.4 (boş şablon)                                                                                                                                                                                                                                                                                                                                                              |

### Politika yüzeyine göre ek okuma 🆕 01.09.2026

| Tetikleyici (filmde varsa) | Ek okuma |
| --- | --- |
| gövdeye değen kuvvet · kalabalık + kaçan kişi · ateş/duman · tehlike çerçevesi · bedenden bir şey çıkarma · yüzsüz izolasyon + kısıtlanmış uzuv | **`POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`** (kapı kartı 20 satır; gövde yalnız tetikleyici varsa) + `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` **KART 12** |
| bir prompt RED aldı | aynı kılavuz **§1 sınıflandırma → §5 merdiven** + `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` satır aç |

### Ölçülmüş prompt hatalarına göre zorunlu okuma 🆕 19.09.2026

| Ne zaman | Okuma |
| --- | --- |
| **her filmde · prompt YAZILIRKEN** | **`PROMPT_HATA_ONLEME_KILAVUZU.md`** — 31 filmin 357 ham QA raporundan çıkarılmış 15 hata sınıfı + ortam cümlelerinin kopyala-yapıştır İngilizce karşılığı (§2) + promptun kapatamadığı üç sınıf (§4). Kaynak: `FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/` |
| prompt dosyası bitti, üretim başlamadı | aynı kılavuz **§7** — `prompt_hata_analizi.py --kilit <FILM>`; `HİÇ YOK` satırı varsa üretime girilmez |
| 🆕 filmde **efor** (çekme · itme · çevirme · sürükleme) ya da **düşüş/çarpma** var | **`FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU.md`** — destek·gövde·işaret·duraksama sözlüğü [D206] · düşük g'de düşüş dili [D200] · çarpmanın üç evresi (TUR 24 · 22.09.2026) |
| 🆕 filmde **darbe · kaza · hasar** ya da kadrodan **çıkan figür** var | **`POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU.md`** — toparlanma merdiveni = D207 eğrisi · hasar düz cümle + referans sayfası · kadro sayı kilidi (TUR 24) |
| 🆕 filmin olayı bir **el işi** ya da uzun bir **yol/görev** dizisi | **`MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md`** — mikro→makro eylem · yürüme platosu · temasın iki klibe bölünmesi · filigran = araç · ADAY-98 tripod (TUR 24) |

---

# 2. 📐 FORMAT KARTLARI

## 2.0 ⭐ FİLM KLASÖRÜ İSKELETİ — her formatta aynı (01.09.2026)

> Kartların `DOSYA:` satırları buraya işaret eder. **Sekiz dosya, sekiz ayrı iş**
> — artı yazımdan ÖNCEKİ işi taşıyan `00_ANALIZ/` klasörü (🆕 08.09.2026).
> Kopyalanabilir hâli: `FILM_KLASOR_SABLONU/` — ve kopyalama da tarif değil,
> BETİK:
>
> ```bash
> bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
>      <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]
> ```
> ⛔ Elle `cp -r` YAPILMAZ. Betik ayrıca sahne çalışma dosyalarını damgalar
> ve okuma çizelgesini üretir; elle kopyalamada bu ikisi kaçıyordu.

```
<FORMAT_KLASORU>/<FILM_ADI>/
├── <FILM>_PLAN.md          konsept · TEMA + sahne indeksleri · vuruş tablosu ·
│                           hook · sahne haritası · Bible'lar · sayısal kilitler
│                           ⛔ PROMPT YOK
├── <FILM>_BOLUM_1.md       sahne bloğu 1 — yalnız ## SAHNE + 📸 + 🎥
├── <FILM>_BOLUM_2.md       sahne bloğu 2
├── <FILM>_KAPAK.md         sabitler + an adayları + İKİ prompt (A·B, tek deney) + kontroller + test kaydı
├── <FILM>_MUZIK.md         §17 künyesi + tek global tema + ses yatağı
├── <FILM>_YAYIN_PAKETI.md  ⭐ TAMAMEN İNGİLİZCE · YouTube + Shorts + IG + TikTok
├── <FILM>_QA_SPEC.md       A/B/C/E blokları — ad DEĞİŞMEZ (üç betik arar)
├── <FILM>_URETIM_DEFTERI.md   🆕 11.09.2026 · ÜRETİM doldurur, yazım değil
│                           klip başına: prompt kaynağı · seed · deneme · kabul
│                           + TESLİM SATIRI (master SHA-256 · süre · sahne sayısı)
│                           ⛔ ⑬ UYUM merceğinin ön koşulu: as-built bilinmeden
│                           "kilit promptta mı yoktu" sorusu cevaplanamaz.
├── <FILM>_REFERANS_PAKETI.md  ⚠️ İSTEĞE BAĞLI (08.09.2026 · sahip kararı)
│                           REFERANS_PAKETI_KILAVUZU §1'in ALTI tetikleyicisi
│                           okunur; doğruyken atlanıyorsa PLAN'a TEK SATIR
│                           gerekçe [D74 kalıbı] — sessizce atlanmaz.
│                           ⛔ Yazıldıysa KAPI 0'dır: sayfası ONAYLI olmayan
│                           ve seed'i yazılmayan varlığın geçtiği hiçbir
│                           sahne üretilmez [D168].
│                           ⛔ Yazılmasa da dosya SİLİNMEZ, ⬜ BEKLİYOR durur.
│                           Karşı kayıt duruyor: D146'nın üç ölçülmüş vakası
│                           (SKYLIGHT · YERÇEKİMİ F2 · STANDING WIRE) ve
│                           SINKING STAKE'in "referans paketi HİÇ ÜRETİLMEDİ
│                           → çapa yok" QA kaydı. Sahip maliyeti üstlendi.
└── 00_ANALIZ/              🆕 yazımdan ÖNCEKİ iş — altı adım, altı dosya (+ onay)
    ├── 00_HIKAYE_ONAYI.md       ⭐ 14.09.2026 — sahibin onayladığı hikâye (LOGLINE ·
    │                            NEDEN İZLENİR · BEDEL · sahne satırları · ADAYLAR (21.09,
    │                            fikir turunun elediği B/C) · ONAY tarihli).
    │                            YENİ REJİM İŞARETİ: bu dosya varken prompt_kontrol.py
    │                            ㉕-㉚ koşar; 14.09'dan önceki klasörlerde yoktur.
    ├── 00_OKUMA_CIZELGESI.md    yaşayan 40 ders + çekirdek manifest (≤30 dosya) +
    │                            QA raporu defteri (betikten: okuma_cizelgesi.sh;
    │                            manifest FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt)
    ├── 01_QA_DERS_HASADI.md     okunanlardan BU filme düşen kilitler — tavan 20 (㉕)
    ├── 02_KONSEPT_VE_RISK.md    ortam/tür · risk kartları · novum · B5
    ├── 03_SAHNE_SIRALAMASI.md   X sahnenin sırası · kurulum iskeleti
    ├── 04_UYARI_NOTLARI.md      ölçülmüş arızalara bağlı uyarılar
    └── 05_SAHNE_CALISMALARI/    ≤8 sahne: S00.md … Snn.md — sahne sahne çalışma
                                 >8 sahne: 00_SAHNE_TABLOSU.md (satır başına sahne)
                                 + 5 kilit sahne S<nn>_<ROL>.md (HOOK · NOVUM ·
                                 DORUK · BEDEL · FINAL — --kilit-sahne; ㉚)
    ⛔ prompt_kontrol.py'nin ATLA deseni 00_ANALIZ'i atlar; klasör adı
      DEĞİŞTİRİLMEZ. Bu klasörde prompt ve "## SAHNE <n>" başlığı yazılmaz.
```

**Neden 00_ANALIZ ayrı bir klasör:** analiz PLAN'ın içine gömülünce plan
1.200 satır oluyor ve kimse geri dönüp bakmıyor — D117'nin ölçtüğü kalıp
(*blok okunmuyor, dosya okunuyor*) analiz için de geçerli. Ayrıca sahne sahne
çalışma ancak sahne başına bir DOSYA olduğunda yapılıyor — ⭐ 14.09.2026
düzeltmesi: 8 sahneye kadar. LOCKED_PULSE'ta 25 dosya × 120 satır yazıldı ve
film üretilmedi; sahne sayısı 8'i geçince çalışma TABLOYA iner, dosya yalnız
beş kilit sahneye kalır.

**Neden yedi dosya:** her dosyanın tüketicisi ve saati farklı. Müzik promptu
Suno'ya, kapak promptu imaj modeline, yayın paketi platform formuna gider;
bölüm dosyaları video modeline. Hepsi tek dosyadaysa operatör 1.200 satır
kaydırıp doğru bloğu arıyor. **Ve D117'nin ölçtüğü şey:** planın *içindeki*
SPEC bloğu dokuz filmde bir kez bile koşulmadı, ayrı dosyaya çıkınca koşuldu.
Blok okunmuyor, dosya okunuyor.

```
ADLANDIRMA   <FILM>_<ROL>.md — film adı ÖNDE.
             Sebep D160/⑪.0: aynı adı taşıyan beş dosyanın ikisi başka bir
             filmdi. Dosya klasörden çıktığında (QA'ya yapıştırılınca, indirilince)
             adı tek kimliğidir. Numara öneki KULLANILMAZ.
             BUYUK_HARF_ALT_CIZGI · Türkçe karakter yok.
             ⚠️ BOLUM_1/BOLUM_2 = eski PART_A/PART_B. Eski filmler
             YENİDEN ADLANDIRILMAZ; yeni filmler BOLUM yazar.

BÖLÜM SAYISI formattan gelir, tercih değil:
  dikey shorts   2   (S0-S2 · S3-S5)
  yatay 2-4 dk   2   (ortadan)
  yatay 3-5 dk   2   (13 + 12 — bugünkü PART_A/PART_B'nin aynısı;
                      13.09.2026 modül beyanıyla 12 + 12 — §2.3)
  yatay 6 dk     2   (18 + 18 — §2.6 · 🆕 13.09.2026)
  yatay 8 dk     2   (24 + 24 — §2.7 · 🆕 13.09.2026)
  yatay 16 dk    8   (8 × 12 — §2.8 · 🆕 19.09.2026 · QA parçası = 2 dosya)
  yatay 32 dk    16  (16 × 12 — §2.9 · 🆕 22.09.2026 · QA parçası = 2 dosya)
  yatay 64 dk    32  (32 × 12 — §2.10 · 🆕 22.09.2026 · QA parçası = 2 dosya)
  yatay 7-9 dk   faz sayısı kadar (BOLUM_1..n) — ikiye ZORLANMAZ
  yatay 10-20    faz alt klasörleri korunur (THE_SECOND_SHIP emsali)

⛔ FORMAT KLASÖRÜNÜN KÖKÜNE .md BIRAKMA — orada yalnız 00_README durur;
   sayaç kökteki her girdiyi BİR FİLM sayar.
⛔ BOŞ DOSYA SİLİNMEZ, `⬜ BEKLİYOR` satırıyla durur. Var olan boş dosya
   görünür borçtur; olmayan dosya borç değil, unutmadır.
```

### ⚠️ Bölmenin bedeli — ve ödendiği yer

Sahneleri iki dosyaya ayırmak `prompt_kontrol.py`'nin **dizi kapılarını dosya
sınırında körleştirir**: 6 sahnelik dikey film ikiye bölününce dosya başına 3
video promptu kalır ve `len(video) >= 4` eşiği yüzünden AÇI VE KURULUM KAPISI
hiç koşmaz; bölüm sınırındaki ardışık çift (S2↔S3) hiçbir dosyada yan yana
gelmez; ⑭ NOVUM satırı PLAN'da kaldığı için bölüm dosyasında "satır yok" der.
Üçü de **bu depoda zaten oluyordu** — THE_BLUE_DRIFT iki bölüm dosyasında da
"NOVUM TAŞIYICISI satırı yok" aldı, oysa satır PLAN'da yazılıydı.

Bedel 01.09.2026'da betiğe ödendi: **klasör modu** bölüm dosyalarını sahne
sırasına göre birleştirip kapıları film boyunca bir kez daha koşar.

```
⛔ ARTIK FİLM KLASÖRÜ VERİLİR, TEK BÖLÜM DEĞİL:
   python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
           <FORMAT_KLASORU>/<FILM_ADI>
   Çıktıda `📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik` satırı YOKSA
   dizi kapıları koşmamıştır.
```

## 2.0b 🎞️ ÇOK KLİPLİ SAHNE — yatay filmin sahne birimi (🆕 22.09.2026 · sahip kararı)

> Tam kural: **`COK_KLIPLI_SAHNE_KILAVUZU.md`**. Bu blok yalnız adres verir.
> Son kare zinciri kalktı. Klip bağımsız ve **tam 10 s** kalır, her klibin kendi
> IMAGE promptu vardır. Bir SAHNE aynı mekânda ve aynı eylemde **2-6 klip** sürer.
> Kapsam: yeni yatay filmler (§2.2-§2.10); dikey shorts ve eski filmler aynen kalır.

```
BİRİM:       SAHNE (S01…) = dramatik birim · KLİP (K01…) = 10 s dosya · ÇEKİM = KLİP
             format kartındaki "N sahne" bu rejimde N KLİPTİR; süre/bölüm/QA birimi aynı
AÇILIŞ:      film_klasoru_ac.sh <FMT> <FILM> <KLİP> --sahne-plani "1 3 4 4 2 4 6 …"
             (toplam = KLİP · her sahne 1-6 · sahne bölüm sınırını aşamaz)
PLAN:        SAHNE PLANI: 1 3 4 … satırı → ㉜ kapısı açılır, ⑩④ KÜME hedefi kapanır
DOSYA:       # 📍 SAHNE nn — AD  (k klip · aralık)   ← tek '#'
             ## 🎬 KLİP nn — Snn · j/k · ROL — BAŞLIK · promptta "Clip n of N."
KİLİT:       sahnenin 2.+ klibi IMAGE+VIDEO'da CONTINUOUS ACTION: <önceki klibin SON durumu>
             LIGHT / PHYSICS / AUDIO-ilk-cümle sahne içinde BİREBİR · zincir dili BLOCK
TABLO:       00_SAHNE_TABLOSU satır = KLİP (| K07 | S03 | 2/3 · EYLEM |) · hikâye onayı satır = SAHNE
QA:          SPEC SCENE COUNT ≠ CLIP COUNT · "sahne içi kesmeler" listesi ② DEVAMLILIK'e
```

---

## 2.1 DİKEY SHORTS (9:16)

```
YAPI:        6 sahne (Hook + 5) × KLİP SÜRESİ
             ⛔ 25.08.2026: klip süresi bir TERCİH değil, ARACIN AYARI.
             Plan yazılmadan önce tek bir test klibi ölçülür ve ızgara
             O SAYIDAN üretilir [Ders 124]:
                ffprobe -v error -show_entries format=duration \
                  -of csv=p=0 <test klibi>
             Depoda ölçülmüş üç teslim de 10 saniyelik klip verdi
             (First Morning 64 s · Wrong Shadow 64 s · Iron Slope 65 s =
             6 × 10,005 s + kart). 8 saniye ısrarla isteniyorsa KIRPMA
             planda sahne sahne yazılır [Ders 100]; yazılmazsa kurgu
             kırpmaz ve 48 saniyeye yazılmış bütün zaman kodları
             (müzik düşüşleri · tohum · karşılık · döngü noktası) kayar.
DOSYA:       §2.0 iskeleti · BÖLÜM 2 (S0-S2 · S3-S5)
             ⚠️ 01.09.2026'ya kadar TEK dosyaydı (plan + Bible + 6 sahne +
             müzik + kapak + başlık paketi, ~1.200 satır). Eski filmler
             OLDUĞU GİBİ kalır; yeni filmler klasör iskeletiyle yazılır.
İMAJ:        6
KLİP:        araçtan ÖLÇÜLEN süre (Veo native, extend GEREKMEZ ✅)
ÜRETİM:      text-to-video
ŞABLON:      SHORTS_SISTEM_PROMPTU.md (hazır sistem promptu)
QA:          QA_PROMPTLARI/1_KARE_QA_... (FORMAT: DİKEY) ✅ 22.08.2026'da
             sıfırdan yazıldı — LESSONS_LEARNED dersleri, SPEC bloğu, güvenli alan, hook
             zamanlaması. Kategori 1-8 video QA ile aynı (karşılaştırılabilir).

KRİTİK FARK: Dikey sadakat — karakter ALT kısımda, kozmik ölçek ÜST kısımda.
             Hook zamanlaması sabit: 0-2sn merak → 2-5sn ipucu →
             5-7sn tam reveal → 7-8sn tek güçlü görüntü.
             Karakter bloğu her IMAGE promptunda tam yazılır; VIDEO
             promptunda gerekmez (bu formatın kendi kuralı).

İlgili ders: 70 — kurgu kapısı: klip sayısı = 6, toplam = klip sayısı ×
             klip süresi, ekran metni = 0,0 sn (jenerik kartı dahil;
             üretim kilitleri kurguyu bağlamaz, kurgu ayrı denetlenir)
İlgili ders: 124 — ızgara plandan değil ARAÇTAN yazılır (yukarıdaki YAPI
             satırı); D70'in üç kez tekrarlayan ihlalinin sebebi buydu
İlgili ders: 125 — kurgu kapısının sayıları master'dan ÖLÇÜLÜR, rapordan
             okunmaz (AGENTS ortak adım ⑪)
İlgili ders: 71 — hook reveal'i analog perdeyle (sis/mesafe/flu)
             gizlenmez; nesne 0-5 sn kadraj DIŞI, start frame
             reveal'siz kilitlenir (I2V)
İlgili kılavuz: HOOK_VE_ILK_SAHNE_KILAVUZU.md — zamanlama yasasının
             mekanizması + S1 tırmandırma + hook tipolojisi (09.08.2026)
```

### ⭐ 27.08.2026 — DİKEY KARTA EKLENEN ÜÇ ZORUNLU PLAN SATIRI

> Kaynak: dört dış araştırma turu ve süzme kaydı →
> `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md`

```
① BİLGİ ASİMETRİSİ: [YOK / DRAMATİK İRONİ · taşıyıcı ①-⑤ · anı 0:XX]
   Depo 16 dikey filmin 16'sında farkında olmadan "YOK" yazdı.
   Karakter sakin kaldıkça izleyici uyarımının parabolik arttığı
   ölçüldü (Cabañas, Senju & Smith 2023, N=42) — panik yasağı
   engel değil MEKANİZMADIR, ama izleyicinin karakterden fazla
   bilmesi şarttır.  → HOOK §3.1
   ⛔ SHORTS_SISTEM_PROMPTU md.5'ten "TEHLİKE YOKTUR" cümlesi
      KALDIRILDI; panik yasağı kaldı. Görünür saat/geri sayım meşru.

② EL YUVASI: [hangi sahne · kadraj payı ≥%25]
   Yüz kask ardındayken izleyicinin empati kurduğu organ eldir; el/POV
   yüzün ölçülmüş birincil vekilidir. Character Bible'ın "eller her
   zaman boş" kuralı gevşetildi: 6 sahnenin ≥1'inde fiziksel temas.
   → DIKEY_MIKRO_DRAMA §4.2

③ VİZÖR BEKLENTİ SATIRI: [§4.1'in ①-④'ünden hangisi · hangi sahne]
   Kask/maske açık döngü aracıdır (+%22 sona kadar bekleme) ama depo
   yalnız maskeyi taşıyıp döngüyü kullanmadı. Vizör durumu 6 sahnede
   de DEĞİŞMEZ [D37·D57] — değişen izleyicinin beklentisidir.
   → DIKEY_MIKRO_DRAMA §4.1

⚠️ AYRICA — SÜRE KARARI ARTIK TEK BAŞINA ALINMAZ:
   platform önce seçilir, süre ondan türer. Shorts=VSA (süre konu dışı,
   tek kapı 0. kare) · TikTok=CR (kısa avantajlı) · IG=sends (uzun
   avantajlı). 48 s ızgarası KIRILMADI, ama artık gerekçesi yazılıyor.
   → YAYIN_VE_PERFORMANS §2.0

⚠️ AI ALGISI KAPISI (konsept seçilirken): "kırılgan insan duygusu +
   fotogerçekçi insan" kutusu ölçülen en ağır cezayı alıyor (güven
   ~%50 düşüyor, gerçekten AI olması gerekmiyor).
   → DIKEY_MIKRO_DRAMA §6.1
```

## 2.2 YATAY 2 DK — 12 SAHNE (eski adı "2-4 dk")

> 🔁 **13.09.2026 · KLASÖR YENİDEN ADLANDIRILDI:** `yatay_2_4_dk_filmler_uzay/`
> → **`yatay_2_dk_filmler/`** (sahip kararı; `_uzay` soneki düştü). Depodaki
> tarihli kayıtlarda geçen "2-4 dk" ifadesi BU formatın eski adıdır ve
> değiştirilmez — kayıt tarihtir. Süpürme: 269 adres · kart H2 altıncı tur.
>
> 🆕 **13.09.2026 · SAHİP BEYANI — 12-SAHNE MODÜLÜ.** Bu klasör artık
> **12 sahne × 10 s = 2:00** modülüdür; merdivenin ilk basamağı
> (12 → 24 → 36 → 48 · §2.2 → §2.3 → §2.6 → §2.7). Yeni filmin varsayılanı
> 12'dir; aşağıdaki 12-18 bandı ESKİ filmlerin gerçeğidir ve olduğu gibi
> kalır — 13-18 sahneyle yazılmış filmler yeniden bölünmez/adlandırılmaz.
> 12'nin dışına çıkmak bandın dışına çıkmaktır: sahibin açık izni + plana
> gerekçe [D74].

```
YAPI:        12 sahne × 10 s = 2:00  (modül · 13.09.2026)
             eski bant: 12-18 sahne × 10s = 2:00-3:00
             (Hook + ana gövde + 2-4 viral ara; 14+ sahnede opsiyonel
             insansız ayrılış kodası — örnek: UNBROKEN_CITY S14-S15,
             STARLESS_CIRCLE S14-S17. Viral ara süreyle ölçeklenir:
             ~2:00'de 2 → 3:00'te 4)
DOSYA:       §2.0 iskeleti · BÖLÜM 2 (ortadan; 15 sahnede 8 + 7)
             ⚠️ eski filmler tek dosya — yeniden bölünmez
İMAJ:        sahne sayısı kadar (12-18)
KLİP:        10s → Veo'da 8s üret + 2s extend ⚠️
ÜRETİM:      im-to-video
REFERANS:    THE_DEAD_APPROACH (V2 self-contained)
             güncel tam örnek: THE_STARLESS_CIRCLE (18 sahne, koda dahil)
VURUŞ:       SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md §2.2 (yüzde bantları)

ALT DALLAR:  bilimkurgu — TEK DAL, sayılar: bash sayac.sh
             (⏸️ zombi dalı 26.08.2026'da kapandı: klasör ve dört film
              kaldırıldı, kartı §4.2'de rafta duruyor.
              ⏸️ savaş dalı 12.08'den beri rafta; kartı §4.3'te)

İlgili ders: 72 + 101 — kurgu kapısı: teslimden önce klip sayısı =
             CLIP COUNT (sahne değil), çekim sayısı = SHOT COUNT,
             süre ±2 s, ekran metni 0.0 sn, ASL hedef bantta,
             CENTRAL CHOICE sahnesi kurguda VAR (Unbroken City: doruk
             kurguya girmedi · Last Shift: 10 klip kurguya girmedi)
İlgili ders: 100 — değişken çekim süresi varsa KIRPMA TABLOSU zorunlu
İlgili kılavuz: HOOK_VE_ILK_SAHNE_KILAVUZU.md — S0-S1 görev ayrımı,
             katalizör ≤0:15 kapısı, ilk 30 sn %70 hedefi (09.08.2026)
```

## 2.3 YATAY 4 DK — 24 SAHNE (eski adı "3-5 dk")

> 🔁 **13.09.2026 · KLASÖR YENİDEN ADLANDIRILDI:** `yatay_3_5_dk_filmler/`
> → **`yatay_4_dk_filmler/`** (sahip kararı). Tarihli kayıtlardaki "3-5 dk"
> ifadesi BU formatın eski adıdır ve değiştirilmez. Eski filmler (25 sahneli
> dâhil) klasörle birlikte taşındı, yeniden bölünmedi/adlandırılmadı.
>
> 🆕 **13.09.2026 · SAHİP BEYANI — 24-SAHNE MODÜLÜ.** Bu klasör artık
> **24 sahne × 10 s = 4:00** modülüdür (2 × 12; hook 24'ün İÇİNDE, ayrı
> sahne değil — THE_HARD_DOCK kalıbı). Klasör README'sinin ② SAHNE SAYISI
> ÇELİŞKİSİ (24 ↔ 25) bu beyanla **24 lehine kapandı**. 25-sahneli (9 s +
> 24 × 10 s = 4:09) yazılmış filmler OLDUĞU GİBİ kalır ve planlarında hangi
> sayıyı izledikleri yazılıdır; yeni filmin varsayılanı 24'tür.
> Bir sonraki basamak: §2.6 (36 · 6 dk) — yazımı aynı, tek fark QA birimi.

```
YAPI:        24 sahne × 10 s = 4:00  (modül · 13.09.2026 · 2 × 12)
             13.09.2026'ya kadar: 25 sahne × 10s = 4:09 (Hook 9s + 24 × 10s)
DOSYA:       §2.0 iskeleti · BÖLÜM 2 (BOLUM_1 12 + BOLUM_2 12 · eski filmlerde 13 + 12)
             — bu format iskeleti zaten yaşıyordu; 01.09.2026'da yalnız
             MUZIK + YAYIN_PAKETI eklendi ve PART_A/PART_B adı BOLUM oldu
             (+ REFERANS_PAKETI — tetikleyici REFERANS_PAKETI_KILAVUZU §1
              tablosudur, sayım DEĞİL [06.09.2026]. THE_COLD_BURN'de metin
              çapası tek başına aracı sabitlemedi (07.08.2026); THE SINKING
              STAKE tam iki insan/iki araç taşıyordu, eski kural
              tetiklenmiyordu ve paket yine yazıldı — gerekçe o dosyanın
              §0'ında: ayırt etme kanalı renk değil GEOMETRİ)
İMAJ:        25
KLİP:        10s → 8s + extend ⚠️
ÜRETİM:      text-to-video
REFERANS:    LOW_POWER/ (klasör yapısı dahil)

KRİTİK FARK: Part A tüm Bible'ları taşır; Part B sadece referans verir
             ama promptlar yine self-contained kalır.
             Viral ara sahne: 4 adet.
```

> 🆕 **25.09.2026 · ÇOK KLİPLİ SAHNE bu karta indi** (`COK_KLIPLI_SAHNE_KILAVUZU.md`).
> İlk film: **THE_COUNTED_RIVET** — 24 KLİP × 10 s = 4:00, **7 SAHNE** (1-5 klip),
> `SAHNE PLANI: 1 3 4 4 3 4 5`. Kartın "24 sahne"si bu rejimde **24 KLİP** okunur;
> SAHNE sayısı hikâyeden gelir ve sorulmaz. Bölüm dosyası sınırı sahneyi BÖLMEZ:
> 1+3+4+4 = 12 (BOLUM_1) · 3+4+5 = 12 (BOLUM_2). KÜME ARANMAZ (son kare zinciri
> kaldırıldı); ardışık aynı kurulum ⑩① ile BLOCK'tur ve DÖNÜŞ ≥%40 aynen koşar.
> ⛔ **"Viral ara sahne: 4 adet" bir HEDEF değil bir BANTTIR** ve ilk ölçümde
> tutmadı: THE_COUNTED_RIVET 0 ⭐viral kliple yazıldı, çünkü §2.4 kapısı İKİ
> kanalı birden istiyor (okunan yüz + hızlanan hacim) ve kilitli kamera + sakin
> yüz + iş kadrajı estetiğinde ikisi tek klipte birleşmiyor. Üç aday tek tek
> ölçüldü (K14 hareket ✅/yüz ⛔ · K16 hareket ✅/yüz ⛔ 128 px · K19 yüz ✅/hareket ⛔)
> ve sapma [D74] biçiminde kaydedildi. Bu estetikte 4 adet isteyen bir sonraki
> film YÜZÜ TAŞIYAN bir kurulum (kamera yüksekliği ≥1,40 m) eklemek zorundadır.
> ☑ **İKİNCİ ÖLÇÜM GELDİ (26.09.2026 · GUNES_MEZARI): 2 ⭐viral klip.**
> İki film, iki ölçüm: **0** (THE_COUNTED_RIVET) ve **2** (GUNES_MEZARI). Aradaki
> farkın nedeni ölçüldü, tahmin edilmedi: GUNES_MEZARI yüz taşıyan kurulum SAYISINI
> artırdı (4 klip · kamera yüksekliği ≥1,40 m · yüz 374-902 px) ve bunların ikisinde
> hareket kanalı da doldu (K12 levhadaki görüntü avucun altında ölüyor · K17 çekirdek
> yataktan çıkarken arkada üç lamba sırayla sönüyor). Düşen iki aday tek kanalda kaldı:
> K03 yüz ✅/hareket ⛔ · K21 hareket ✅/yüz ⛔ (o klipte kadrajda insan YOK).
> ☑ **ÜÇÜNCÜ ÖLÇÜM GELDİ (28.09.2026 · THE_SIGNAL_KEEPERS): 3 ⭐viral klip.**
> Üç film, üç ölçüm: **0** (THE_COUNTED_RIVET) · **2** (GUNES_MEZARI) · **3**
> (THE_SIGNAL_KEEPERS). ⭐ Ve bu ölçüm BELİRLEYİCİ DEĞİŞKENİ değiştirdi: sorun yüz
> taşıyan kurulumun SAYISI değil, o kurulumun KAÇ KLİBİNDE kadrajda ikinci bir
> hacim hareketi olduğu. THE_SIGNAL_KEEPERS'ta yüz taşıyan kurulum yalnız 3'tür
> (B · E · F) ama 8 klibe yayılıyor ve üçünde ikinci kanal dolu: K11 (vizörün
> üstünden geçen ışık deseni + parmak ucunun teması) · K20 (çekirdek yuvadan
> çıkıyor + ses cümlenin ortasında kesiliyor) · K22 (arkada yuva dizisi yukarı
> dönüyor, ışık kadrajın üstünden çıkıyor). Düşen iki aday tek kanalda kaldı:
> K09 yüz 1735 px ✅ / hareket ⛔ · K18 yüz ✅ / hareket ⛔ (klibin işi DİNLEMEK).
> ⭐ **KARAR ÖNERİSİ (güncellendi): "4 adet" bir BANT DEĞİL. Kilitli kamera +
> sakin yüz + iş kadrajı estetiğinin bandı 0-3'tür** ve bandın üst ucuna çıkmanın
> yolu kurulum EKLEMEK değil, YÜZ TAŞIYAN kurulumun klibine ikinci bir hacim
> olayı yerleştirmektir — bu açı yayını (⑩①) hiç sıkıştırmaz.
> ⛔ Kartın "4 adet" satırı SİLİNMEDİ: uzun formatlarda (§2.5 · §2.8) hiç ölçülmedi.
> Karar sahibindir; burada üç ölçüm ve gerekçesi duruyor.
> ☑ **DÖRDÜNCÜ ÖLÇÜM GELDİ (28.09.2026 · THE_LAST_TOW) ve İLK KEZ UZUN FORMATTA:
> 48 klipte 3 ⭐viral aday.** Bu, kartın bir satır önce "hiç ölçülmedi" dediği şeydir.
> Dört film: **0** (24 klip) · **2** (24 klip) · **3** (24 klip) · **3** (48 klip).
> ⭐ **SONUÇ: BANT SÜREYLE ÖLÇEKLENMİYOR.** `yatay_8_dk_filmler/README.md` kartı
> "viral ara sahne süreyle ölçeklenir: 24 sahnede 4 → 48 sahnede 8" diyor; ölçüm
> 48 klipte **3** buldu. Sebebi tahmin değil, sayım: THE_LAST_TOW'da **yüz kadrajda
> olan klip sayısı 5'tir** (48'de 5 — grep ile ölçüldü: `fully readable through the
> clear pane` 5 klipte). Ölçütün birinci kanalı YÜZ olduğu için tavan süreden değil
> KADRAJ KARARINDAN geliyor: yüzü 5 klipte olan bir film, 96 klip uzunluğunda da
> 5'ten fazla ⭐viral üretemez.
> ⭐ **KARAR ÖNERİSİ (güncellendi): "süreyle ölçeklenir" satırı bu estetikte
> GEÇERSİZ.** Doğru bağımlı değişken YÜZ TAŞIYAN KLİP SAYISIDIR ve o da açı yayının
> değil, hikâyenin kararıdır (bu filmde işin 43 klibi ellerde ve yüzeylerde geçiyor).
> ⛔ Yine SİLİNMİYOR: 96 klipte (§2.8) hâlâ ölçülmedi. Karar sahibindir; burada
> DÖRT ölçüm ve gerekçesi duruyor.

## 2.4 YATAY 7-9 DK — ⏸️ KAPANDI, §2.5'E KATILDI (04.09.2026)

```
⛔ yatay_7_9_dk_filmler/ klasörü sahip kararıyla KALDIRILDI.
   Bandın tamamı §2.5'in içindedir — o kartın SÜRE satırı 7-20 dk'dır.
   Tek filmi THE_SLOW_STONE → yatay_10_20_dk_filmler/THE_SLOW_STONE/
   Kendi kilavuzlar/ dizini → kilavuzlar_ve_sistem_dosyalari/
       5_FAZ_MIMARISI · FAZ_DOSYASI_SABLONU · KESINTISIZ_VIDEO_URETIM_TEKNIGI
       QA_PROMPTLARI/UC_GECISLI_QA/ (3 geçişli sistem)

   Kart SİLİNMEDİ, çünkü altındaki dürüst kayıt gerçek bir filme ait
   ve hâlâ ödenmemiş bir borcu tarif ediyor.
```

> ⚠️ **DÜRÜST KAYIT (21.08.2026 · adresi 04.09.2026'da güncellendi):**
> Bu formatın kartı TEORİK tanımdı ve gerçekle hiç buluşmadı. Eski
> referans THE_WAKING_GROUND depoda YOK (yalnız adı geçiyordu).
> Formatta yazılmış tek film **THE_SLOW_STONE** ve üç tanımlayıcı
> kuraldan üçünde de GEREKÇELİ saptı: 4 kısım × 12 sahne (5 faz değil) ·
> 10 s sahne + extend (8 s native değil) · start/end frame zinciri
> REDDEDİLDİ (48 sahne ≈ 60 imaj maliyeti). Gerekçeler:
> `yatay_10_20_dk_filmler/THE_SLOW_STONE/README.md`.
>
> ⛔ **Klasörün kapanması bu borcu ÖDEMEDİ, taşıdı.** Kartın üç kuralı
> da tek filmde çöktüğü için 5 faz / 8 s / start-end üçlüsü §2.5'e
> ÖLÇÜLMÜŞ olarak değil, ÖNERİ olarak girer. Bandın kısa ucunda ikinci
> film yazılırken şablon THE_SLOW_STONE'dur, kart değil.


## 2.5 YATAY 10-20 DK (10 DK) — ⏸️ ARŞİV / KAPANDI (22.09.2026)

> ⛔ **22.09.2026 · SAHİP KARARIYLA KAPATILDI VE ARŞİVLENDİ.** 10-20 dakikalık
> uzun faz mimarisi (3 perde / 10 faz / 120 sahne) üretimi sonlandırıldı; stüdyo
> odağı 8 dk (§2.7) ve 16 dk (§2.8) modül sistemlerine kaydırıldı. Klasör
> tüm içeriğiyle birlikte (`THE_SCOURED_GLASS`, `THE_SECOND_SHIP`, `THE_SLOW_STONE`,
> `YERCEKIMI`, `README.md`) `kilavuzlar_ve_sistem_dosyalari/ARSIV/yatay_10_dk_filmler/`
> altına taşındı. Ham QA raporları (`02_HAM_RAPORLAR/`) silinmedi, yerinde korundu.
> Bu kart ve aşağıdaki kurallar tarihsel metodoloji kanıtı olarak saklanmaktadır.

```
SÜRE:        7-20 dk (420-1200 s) — alt sınır 04.09.2026'da 10 dk'dan
             7 dk'ya indirildi (sahip kararı; 7-9 klasörü kapandı, §2.4).
             ⚠️ 13.09.2026: 8 dk MODÜL hattı §2.7'de — yukarıdaki not.
             ⚠️ KLASÖR ADI DEĞİŞMEDİ: yatay_10_20_dk_filmler/
                Ad ile bant artık örtüşmüyor. Bilinçli — yeniden
                adlandırma depoda ~40 adres daha kırardı; ölçülmüş
                hiçbir sorunu da çözmezdi.
YAPI:        faz alt klasörleri · ölçülmüş tek örnek:
             3 perde / 10 faz (perde dağılımı 3-4-3) × 12 sahne
             = 120 sahne × 8 s = 960 s = 16:00
DOSYA:       §2.0 iskeleti · faz başına alt klasör (BOLUM yerine FAZ_nn)
İMAJ:        sahne sayısı kadar
KLİP:        8 s — Veo native
ÜRETİM:      faz bazlı; her fazın kendi Bible referansı
REFERANS:    YERÇEKİMİ (yatay_10_20_dk_filmler/) — yazıldı, üretilmedi
             ikinci örnek: THE_SECOND_SHIP (faz yapısı aynı)

KISA UÇ (7-10 dk) — PERDE KATMANI YOK, yalnız faz
             5 faz × 12 sahne = 60 sahne × 8 s = 8:00 · 75 imaj
             (faz başına 3 çapa + 12 bitiş karesi)
             Perde katmanı 5 fazlık yayı böler; 8 dakikada gerekmez.
             Perde EŞİĞİ: 7 fazın üstüne çıkan film perdeye geçer
             (§2.5 faz tablosu). Altı faz ve aşağısı düz fazdır.
             ⚠️ Bu üçlü (5 faz · 8 s · start/end zinciri) ÖNERİDİR,
                ölçüm değil — bandın tek üretilmiş filmi üçünden de
                saptı. Gerekçe ve borç: §2.4 dürüst kaydı.
             EMSAL: THE_SLOW_STONE — 4 kısım × 12 = 48 sahne × 10 s
                = 8:00 planlı / 7:35 gerçek · ✅ ÜRETİLDİ · QA 5/10.
                Bandın ÜRETİLMİŞ tek filmi budur; uzun ucun iki filmi
                (YERÇEKİMİ · THE_SECOND_SHIP) yazıldı, üretilmedi.

ORAN SETİ — kaynağı TUR 2, DOĞRULAMASI YERÇEKİMİ 00_PLAN
             §Oran doğrulaması. Üç bant filmde tuttu, İKİSİ TUTMADI:
             ✅ katalizör %10-15   → S16 = 2:00 = %12,5
             ✅ feda %30-35        → S43 = 5:36 = %35,0
             ✅ doruk başlangıcı %78-80 → S94-97 = 12:24-12:48
             ⚠️ her şey kaybedildi: TUR 2 seti ~%73 diyor, film
                S72-78 = %60-65 ölçtü — 8-13 puan sapma
             ⚠️ çözülme: TUR 2 seti %93+ diyor, film %90+ ölçtü
             ⛔ Bu iki satırda geçerli olan FİLMİN ÖLÇÜMÜDÜR
                (%60-65 · %90+); TUR 2 değerleri ÖNERİ olarak kalır.
             ⚠️ Ve aynı vuruş için depoda ÜÇÜNCÜ bir sayı var:
                `SENARYO_VE_VIRAL` §2.2 "her şeyin kaybı ~%75".
                Üç sayının tek eve indirilmesi SAHİBİN KARARIDIR.

İlgili kılavuz: HOOK §1.1 (açılış bütçesi) · FINAL §2 ve §2.1
             (final tipi = KAPALI · kapanış bütçesi %7-10)
```

> ⚠️ **DÜRÜST KAYIT (04.09.2026):** Bu kart, 12 ve 13 numaralı araştırma
> turları üç dosyadan birden "10-20 dk format kartı"na atıf verince
> açıldı — o güne dek §2'de böyle bir kart YOKTU ve atıflar boşluğa
> gidiyordu. Kart TEK filmden (YERÇEKİMİ) türetilmiştir; ikinci film
> yazılmadan önce sahne/faz sayısı yeniden değerlendirilmelidir.

## 2.6 YATAY 6 DK — 36 SAHNE · 2 BÖLÜM ⏸️ ARŞİV / KAPANDI (22.09.2026)

> ⛔ **22.09.2026 · SAHİP KARARIYLA KAPATILDI VE ARŞİVLENDİ.** 36 sahne / 2 bölüm
> modül formatı sonlandırıldı; klasör tüm içeriğiyle (`MARS_SON_CIKIS`, `README.md`)
> `kilavuzlar_ve_sistem_dosyalari/ARSIV/yatay_6_dk_filmler/` altına taşındı.
> Ham QA raporları (`02_HAM_RAPORLAR/MARS_SON_CIKIS/` 30 rapor) ve film kaydı
> silinmedi, yerinde korundu. Bu kart tarihsel metodoloji kanıtı olarak saklanmaktadır.

```
YAPI:        36 sahne × 10 s = 6:00 — hook 36'nın içinde, ayrı sahne değil
             (2 × 18 · viral ara süreyle ölçeklenir: 6)
DOSYA:       §2.0 iskeleti · BÖLÜM 2 (BOLUM_1 = S00-S17 · BOLUM_2 = S18-S35)
             betik: film_klasoru_ac.sh yatay_6_dk_filmler <FILM> 36
İMAJ:        36
KLİP:        10 s → 8 s + extend ⚠️ · ⛔ ARAÇTAN ölçülür [D124]
ÜRETİM:      text-to-video (§2.3 ile aynı)
REFERANS:    henüz film yok — §2.3'ün referansı (THE_HARD_DOCK 24 × 10 s) +
             bölüm sınırı için SAHNE_ZINCIRI_VE_SINIR_KILAVUZU
KURULUM:     12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 (ACI_YAYI §3 🕰️ · §4b)

⭐ KRİTİK FARK — QA BİRİMİ BÖLÜMDÜR (sahip kararı · 13.09.2026)
             Film TEK master olarak kurgulanır ve yayınlanır; QA için İKİ
             YARIM MASTER ihraç edilir (3:00 + 3:00) ve on iki mercek her
             yarıya AYRI koşulur → 24 rapor. ⑬ UYUM bölümden etkilenmez.
             · rubriğin başına SPEC + "THIS FILE IS PART n OF 2" beyanı
             · rapor_kontrol.py … --bolum n/2  ⛔ ZORUNLU (①.9 teslim kapısı
               yalnız BOLUM_n'i sayar · ①.11 BÖLÜM KAPISI uç kategorileri
               `—` yapar — D185'in yarım-film uzantısı)
             · B1'de sayı taşımaz: ④ Ending · ⑫ Peak Placement · ⑫ Exit
               B2'de sayı taşımaz: ④ Hook · ⑫ Hook Question · ⑫ Stakes
               hiçbirinde: ④ Structure · ④ Retention · ⑫ Plateau · ⑨ Rhyme Pair
               ⬜ bütün-film dörtlüsünün ölçümü SAHİP KARARI (README'de üç şık)
             · kayıt etiketi: ham `<FILM>_B1_<MERCEK>_HAM.md` · T satırı
               `**<Film>** B1` · matris `**<FILM>** (B1)` · 01 kaydı TEK dosya
             · ② DEVAMLILIK bölüm sınırı çiftini (S17↔S18) GÖREMEZ →
               SPEC B'ye sınır satırı + elle kare (①.10 göz kapısı kalıbı)
             ⛔ Kesme listesi / yeniden sıralama bölüm raporundan UYGULANMAZ.
             ⛔ Kurgu kapısı TAM master'a: 36 klip · 360 s ±2 s.
```

## 2.7 YATAY 8 DK — 48 SAHNE · 2 BÖLÜM 🆕 13.09.2026

> **Klasör:** `yatay_8_dk_filmler/` · **README:** `yatay_8_dk_filmler/README.md`.
> Merdivenin dördüncü basamağı. **Yazım §2.3 ile birebir aynı; tek fark QA
> birimidir** — ve her yarım, §2.3'ün bir filmi büyüklüğündedir (24 × 10 s).
>
> ⚠️ **8 DAKİKADA İKİ HAT — karıştırılmaz.** Bu kart MODÜL hattıdır (12-sahne
> modülü · 2 bölüm dosyası · 10 s · perde/faz YOK). Faz mimarisinin kısa ucu
> (§2.5: 5 faz · 8 s · start/end zinciri · THE_SLOW_STONE) `yatay_10_20_dk_filmler/`'de
> kalır. Klasör seçimi MİMARİYE göre yapılır, süreye göre değil.
> ⬜ §2.5'in alt sınırı (7 dk) sahip kararı bekliyor (Kart H2 ④).

```
YAPI:        48 sahne × 10 s = 8:00 — hook 48'in içinde, ayrı sahne değil
             (2 × 24 · viral ara süreyle ölçeklenir: 8)
             ⚠️ ORAN SETİ §2.5'in ölçülmüş bantlarıyla sınanır (katalizör ·
               feda · doruk başlangıcı) — 8 dakikada tema-tatmin kuralı
               ağırlaşır (TEMA_MUHENDISLIGI süre-tatmin); plana yüzde satırı.
DOSYA:       §2.0 iskeleti · BÖLÜM 2 (BOLUM_1 = S00-S23 · BOLUM_2 = S24-S47)
             betik: film_klasoru_ac.sh yatay_8_dk_filmler <FILM> 48
İMAJ:        48
KLİP:        10 s → 8 s + extend ⚠️ · ⛔ ARAÇTAN ölçülür [D124]
ÜRETİM:      text-to-video (§2.3 ile aynı)
REFERANS:    henüz film yok — §2.3'ün referansı (THE_HARD_DOCK 24 × 10 s);
             ⚠️ THE_SLOW_STONE (48 × 10 s) SÜRE emsalidir, MİMARİ emsali
               DEĞİL (4 kısım · faz hattı · QA 5/10 · §2.4 dürüst kaydı)
KURULUM:     12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 (ACI_YAYI §3 🕰️ · §4b)
             🆕 22.09.2026 · SAHNE PLANI'lı filmde (ÇOK KLİPLİ SAHNE) KÜME YOK — sahne
             2-6 klip · DÖNÜŞ %40 sürer · kapı ㉜ (COK_KLIPLI_SAHNE_KILAVUZU · §2.0b)

⭐ KRİTİK FARK — QA BİRİMİ BÖLÜMDÜR (sahip kararı · 13.09.2026)
             §2.6 ile aynı mekanizma, yarım = 4:00 · 24 klip:
             · iki yarım master → 12 mercek × 2 = 24 rapor · ⑬ etkilenmez
             · rubriğin başına SPEC + "THIS FILE IS PART n OF 2" beyanı
             · rapor_kontrol.py … --bolum n/2  ⛔ ZORUNLU (①.9 · ①.11)
             · sayı taşımayan kategoriler ve ⬜ bütün-film dörtlüsü: §2.6
             · kayıt etiketi B1/B2: §2.6 · ② sınır çifti S23↔S24 elle kare
             ⛔ Kesme listesi / yeniden sıralama bölüm raporundan UYGULANMAZ.
             ⛔ Kurgu kapısı TAM master'a: 48 klip · 480 s ±2 s.
```

> ⚠️ **DÜRÜST KAYIT (13.09.2026):** iki kart da SIFIR filmle açıldı — tek
> kaynakları sahibin beyanı ve §2.3'ün ölçülmüş tek 24-sahnelik koşusudur
> (THE_HARD_DOCK · on iki mercek · 12.09.2026). "Yarım master = bir 24-sahne
> filmi ölçeği" cümlesi bir TASARIM kararıdır, ölçüm değil; ilk 6/8 dk film
> QA'dan geçince ①.11 kategori maskesi o filmle sınanır ve gerekirse burada
> düzeltilir (Kart G — ders değil, önce belge revizyonu).

## 2.8 YATAY 16 DK — 96 SAHNE · 8 BÖLÜM · QA 4 PART + TAM FİLM 🆕 19.09.2026

> **Klasör:** `yatay_16_dk_filmler/` · **README:** `yatay_16_dk_filmler/README.md`
> (QA akışının tam tarifi orada; bu kart adres verir, tekrar etmez).
> 12-sahne modül merdiveninin BEŞİNCİ basamağı. **Yazım §2.3 ile birebir aynı;
> fark QA birimidir:** iki bölüm dosyası = bir PART (24 klip · 4:00 = §2.3'ün bir
> filmi = THE_HARD_DOCK'un on iki mercekle ölçüldüğü ölçek) **+ tam-film koşusu**.

```
YAPI:        96 sahne × 10 s = 16:00 — hook 96'nın içinde, ayrı sahne değil
             (8 × 12 · viral ara süreyle ölçeklenir: 16)
             ⚠️ ORAN SETİ §2.5 bantlarıyla sınanır; 16 dk'da ölçüm YOK — ilk film ölçer
DOSYA:       §2.0 iskeleti · BÖLÜM 8 (BOLUM_n = S(12n−12)…S(12n−1))
             betik: film_klasoru_ac.sh yatay_16_dk_filmler <FILM> 96
İMAJ:        96 (I2V zincir klipleri imaj promptu taşımaz — sayı film başına düşer)
KLİP:        tam 10,000 s — ham ARAÇTAN ölçülür [D124], kurgu birimi seçilen kare
             hızında TAM 10 s'e sabitlenir (KIRPMA satırı SPEC A'ya); zaman kodları değişmez
ÜRETİM:      text-to-video / I2V (§2.3 ile aynı; motor filmin PLAN'ında)
REFERANS:    henüz film yok — §2.3'ün referansı (THE_HARD_DOCK) + 8 dk hattının
             sahip-yazımı emsali (THE_FALLING_WORLD) · ilk film: THE_STOLEN_SKY
KURULUM:     12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 (ACI_YAYI §3 🕰️ · §4b) —
             sekans içi I2V devam klipleri ardışık çift bandından MUAF (aynı harf)
             🆕 22.09.2026 · SAHNE PLANI'lı filmde (ÇOK KLİPLİ SAHNE) KÜME YOK — sahne
             2-6 klip · DÖNÜŞ %40 sürer · kapı ㉜ (COK_KLIPLI_SAHNE_KILAVUZU · §2.0b)

⭐ KRİTİK FARK — QA BİRİMİ PART (2 bölüm dosyası) + TAM FİLM (sahip kararı · 19.09.2026)
             · 4 PART masterı (4:00 · 24 klip) → 12 mercek × 4 = 48 rapor · ⑬ etkilenmez
             · rubriğin başına SPEC + "THIS FILE IS PART n OF 4 — scenes Sxx–Syy" beyanı
             · rapor_kontrol.py … --bolum n/4  ⛔ ZORUNLU — betik 8 dosya / 4 parça
               eşlemesini kendisi yapar (bolum_dosyalari · 19.09.2026)
             · maske: PART 1 BAŞ · PART 2-3 ORTA (hook VE final `—`) · PART 4 SON
             · ⭐ TAM-FİLM KOŞUSU (8 dk'nın ⬜ seçeneği (a) burada uygulanır): ④ HİKAYE +
               ⑫ HOOK tam master'a maskesiz ("THIS FILE IS THE FULL FILM — 96 scenes");
               Structure · Retention · Plateau · Rhyme burada SAYI TAŞIR; ③ SES nihai
               SESLİ master'a — ses kabulü yalnız burada (part ③ teknik ön bulgudur;
               part masterlar sesli masterdan kesilmediyse ③ hücresi `uygulanmadı`)
             · kayıt etiketi: ham `<FILM>_B<n>_<MERCEK>_HAM.md` (n=1..4) + `<FILM>_FULL_…` ·
               T satırı `**<Film>** B1…B4` + `**<Film>** FULL` · matris `(B1)…(B4)` + `(FULL)`
             · ② DEVAMLILIK üç sınır çiftini (S23↔S24 · S47↔S48 · S71↔S72) göremez →
               SPEC B'ye sınır satırı + elle kare
             ⛔ Kesme / yeniden sıralama PART raporundan UYGULANMAZ; TAM-FİLM raporundan
               sahip kararıyla uygulanır.
             ⛔ Kurgu kapısı TAM master'a: 96 klip · 960 s (±0 — "tam 10 s" koşulu).
```

> ⚠️ **DÜRÜST KAYIT (19.09.2026):** kart SIFIR filmle açıldı; kaynağı sahibin
> beyanı (2/4/6/8 mantığı · 8 bölüm · 4 QA parçası) ve §2.7'nin ölçülmemiş
> tasarımıdır. 16 dk'da oran seti, ①.11 ORTA maskesi ve tam-film koşusu ilk
> filmle sınanır; gerekirse önce bu kart düzeltilir (Kart G).

---

## 2.9 YATAY 32 DK — 192 SAHNE · 16 BÖLÜM · QA 8 PART + TAM FİLM 🆕 22.09.2026

> **Klasör:** `yatay_32_dk_filmler/` · **README:** `yatay_32_dk_filmler/README.md`
> (QA akışının tam tarifi orada; bu kart adres verir, tekrar etmez).
> 12-sahne modül merdiveninin ALTINCI basamağı. **Yazım §2.3 ile birebir aynı;
> fark QA birimidir:** iki bölüm dosyası = bir PART (24 klip · 4:00) **+ tam-film koşusu**.

```
YAPI:        192 sahne × 10 s = 32:00 — hook 192'nin içinde, ayrı sahne değil
             (16 × 12 · viral ara süreyle ölçeklenir: 32)
DOSYA:       §2.0 iskeleti · BÖLÜM 16 (BOLUM_n = S(12n−12)…S(12n−1))
             betik: film_klasoru_ac.sh yatay_32_dk_filmler <FILM> 192
İMAJ:        192 (I2V zincir klipleri imaj promptu taşımaz)
KLİP:        tam 10,000 s — ham ARAÇTAN ölçülür [D124], kurgu birimi seçilen kare
             hızında TAM 10 s'e sabitlenir; zaman kodları değişmez
ÜRETİM:      text-to-video / I2V (§2.3 ile aynı; motor filmin PLAN'ında)
KURULUM:     12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 (ACI_YAYI §3 🕰️ · §4b)
             🆕 22.09.2026 · SAHNE PLANI'lı filmde (ÇOK KLİPLİ SAHNE) KÜME YOK — sahne
             2-6 klip · DÖNÜŞ %40 sürer · kapı ㉜ (COK_KLIPLI_SAHNE_KILAVUZU · §2.0b)

⭐ KRİTİK FARK — QA BİRİMİ PART (2 bölüm dosyası) + TAM FİLM (sahip kararı · 22.09.2026)
             · 8 PART masterı (4:00 · 24 klip) → 12 mercek × 8 = 96 rapor · ⑬ etkilenmez
             · rubriğin başına SPEC + "THIS FILE IS PART n OF 8 — scenes Sxx–Syy" beyanı
             · rapor_kontrol.py … --bolum n/8  ⛔ ZORUNLU — betik 16 dosya / 8 parça
               eşlemesini kendisi yapar (bolum_dosyalari)
             · maske: PART 1 BAŞ · PART 2–7 ORTA (hook VE final `—`) · PART 8 SON
             · ⭐ TAM-FİLM KOŞUSU: ④ HİKAYE + ⑫ HOOK tam master'a maskesiz ("THIS FILE IS THE FULL FILM — 192 scenes");
               Structure · Retention · Plateau · Rhyme burada SAYI TAŞIR; ③ SES nihai
               SESLİ master'a — ses kabulü yalnız burada
             · kayıt etiketi: ham `<FILM>_B<n>_<MERCEK>_HAM.md` (n=1..8) + `<FILM>_FULL_…` ·
               T satırı `**<Film>** B1…B8` + `**<Film>** FULL` · matris `(B1)…(B8)` + `(FULL)`
             · ② DEVAMLILIK yedi sınır çiftini (S023↔S024, S047↔S048 ... S167↔S168) göremez →
               SPEC B'ye sınır satırı + elle kare
             ⛔ Kurgu kapısı TAM master'a: 192 klip · 1920 s (±0 — "tam 10 s" koşulu).
```

---

## 2.10 YATAY 64 DK — 384 SAHNE · 32 BÖLÜM · QA 16 PART + TAM FİLM 🆕 22.09.2026

> **Klasör:** `yatay_64_dk_filmler/` · **README:** `yatay_64_dk_filmler/README.md`
> (QA akışının tam tarifi orada; bu kart adres verir, tekrar etmez).
> 12-sahne modül merdiveninin YEDİNCİ basamağı. **Yazım §2.3 ile birebir aynı;
> fark QA birimidir:** iki bölüm dosyası = bir PART (24 klip · 4:00) **+ tam-film koşusu**.

```
YAPI:        384 sahne × 10 s = 64:00 — hook 384'ün içinde, ayrı sahne değil
             (32 × 12 · viral ara süreyle ölçeklenir: 64)
DOSYA:       §2.0 iskeleti · BÖLÜM 32 (BOLUM_n = S(12n−12)…S(12n−1))
             betik: film_klasoru_ac.sh yatay_64_dk_filmler <FILM> 384
İMAJ:        384 (I2V zincir klipleri imaj promptu taşımaz)
KLİP:        tam 10,000 s — ham ARAÇTAN ölçülür [D124], kurgu birimi seçilen kare
             hızında TAM 10 s'e sabitlenir; zaman kodları değişmez
ÜRETİM:      text-to-video / I2V (§2.3 ile aynı; motor filmin PLAN'ında)
KURULUM:     12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 (ACI_YAYI §3 🕰️ · §4b)
             🆕 22.09.2026 · SAHNE PLANI'lı filmde (ÇOK KLİPLİ SAHNE) KÜME YOK — sahne
             2-6 klip · DÖNÜŞ %40 sürer · kapı ㉜ (COK_KLIPLI_SAHNE_KILAVUZU · §2.0b)

⭐ KRİTİK FARK — QA BİRİMİ PART (2 bölüm dosyası) + TAM FİLM (sahip kararı · 22.09.2026)
             · 16 PART masterı (4:00 · 24 klip) → 12 mercek × 16 = 192 rapor · ⑬ etkilenmez
             · rubriğin başına SPEC + "THIS FILE IS PART n OF 16 — scenes Sxx–Syy" beyanı
             · rapor_kontrol.py … --bolum n/16  ⛔ ZORUNLU — betik 32 dosya / 16 parça
               eşlemesini kendisi yapar (bolum_dosyalari)
             · maske: PART 1 BAŞ · PART 2–15 ORTA (hook VE final `—`) · PART 16 SON
             · ⭐ TAM-FİLM KOŞUSU: ④ HİKAYE + ⑫ HOOK tam master'a maskesiz ("THIS FILE IS THE FULL FILM — 384 scenes");
               Structure · Retention · Plateau · Rhyme burada SAYI TAŞIR; ③ SES nihai
               SESLİ master'a — ses kabulü yalnız burada
             · kayıt etiketi: ham `<FILM>_B<n>_<MERCEK>_HAM.md` (n=1..16) + `<FILM>_FULL_…` ·
               T satırı `**<Film>** B1…B16` + `**<Film>** FULL` · matris `(B1)…(B16)` + `(FULL)`
             · ② DEVAMLILIK 15 sınır çiftini göremez → SPEC B'ye sınır satırı + elle kare
             ⛔ Kurgu kapısı TAM master'a: 384 klip · 3840 s (±0 — "tam 10 s" koşulu).
```

---

# 3. 🌍 ORTAM KARTLARI

> Aynı dersin doğru cevabı ortama göre **ters dönüyor**.
> Ders 36, 39 ve 41 kendi içlerinde "diğer ortamda geçersiz" uyarısı taşır.

## 3.1 VAKUM (ay, kuyruklu yıldız, açık uzay)

```
Toz              yükselir ve GİTMEZ — asla yere oturmaz
Gölge            MUTLAK SİYAH, jilet gibi keskin kenar
Dolgu ışığı      YOK — gölgede kalan yüzey gerçekten siyah
Ses              dışarıda hiç yok; sadece gövdeden iletilen
Egzoz            düz keskin koni, hızla seyrelir — kıvrılmaz, kabarmaz
Rüzgar           yok
Lens             KÜRESEL — anamorfik yatay parlama YASAK (sinematografik §11)
                 vakumda atmosferik saçılma yok, parlama fiziksel olarak yanlış
Hareket          yerçekimine göre: 0.0004g halat çekme / 0.12g temaslı adım
İlgili ders      30 (parçacık), 31 (çarpma), 36 (vakum dumanı), 39 (sıvı toz)
Referans film    THE_DEAD_APPROACH, THE_COLD_WELD
```

## 3.2 İNCE ATMOSFER (Mars, %0.6 basınç)

```
Toz              YAVAŞ ama KESİN çöker, yüzeye oturur
Gölge            zayıf ve yumuşak kenarlı — MEŞRU, hata değil
Dolgu ışığı      VAR ve motivasyonlu (atmosferik saçılma)
Ses              boğuk, zayıf, yüksek frekanslar yok (240 m/s)
Rüzgar           hiçbir şeyi deviremez — kumaş çırpmaz, kimse savrulmaz
Gökyüzü          kahve-tarçın; gün batımında güneşin ÇEVRESİ mavi
İlgili ders      39 (toz yönü), 41 (yumuşak ışık ≠ bloom), ⭐ 143 (ışık sütunu
                 tozu ZERRE SAYISIYLA yazılır — perde/şelale yasak), 145 (alçak
                 açıda ufuk kilidi — ova kanyona dönmesin), 147 (tozlu odada
                 kir MONOTONİK merdiven, faz satırı her prompta)
Referans film    LOW_POWER · THE_SKYLIGHT (üretildi 29.08.2026 — D143-150'nin kaynağı)
```

## 3.3 DÜNYA ATMOSFERİ ⏸️ ŞU AN KULLANIMDA DEĞİL (26.08.2026)

> ⛔ Bu ortam kartı KARASAL türlere bağlıydı (zombi · savaş) ve ikisi de
> §4.2/§4.3'te RAFTA. Depo yalnız UZAY filmleri içindir; bugün açık olan
> ortamlar §3.1 (vakum) ve §3.2'dir (ince atmosfer). Kart silinmedi —
> Dünya benzeri atmosferi olan bir GEZEGEN konsepti bu fiziği kullanır.

```
Toz              hızlı çöker ve yere oturur
Gölge            hava durumuna göre; kapalı havada yumuşak — MEŞRU
Dolgu ışığı      VAR
Ses              normal yayılım
Rüzgar           gerçek kuvvet — ama abartma, model fırtınayı şişiriyor
Nefes            soğukta görünür buhar
İlgili ders      39 (toz sıvı gibi davranmasın), 41 (yumuşaklık ≠ bloom)
Referans film    ⛔ YOK — bu ortamın dört referans filminin dördü de
                 26.08.2026'da depodan kaldırıldı (zombi türü kapandı).
                 Dürüst kayıt: kartın fizik satırları duruyor ama artık
                 DOĞRULANABİLİR bir örneği yok. Bu ortamda film yazılırsa
                 ilk film yeni referans olur.
                 (Arşiv: film_md_ZOMBI_ARSIV_2026-08-26.tar.gz, depo dışı)
```

## 3.4 KALIN ATMOSFER (3-5 atm, düşük yerçekimi)

> 🆕 THE_HERD ile açıldı. Bu kart **kilometre ölçekli canlı** veya
> **havada yüzen gövde** olan her filmin ön şartıdır: kare-küp yasası bu
> ölçeği yalnız düşük yerçekimi + yüksek hava yoğunluğu ile kapatır.

```
Toz              HIZLI çöker ve KÜMELENİR — 3 saniyede yere oturur.
                 Asılı toz perdesi YOKTUR (vakumun tam tersi)
Gölge            yumuşak kenarlı ama DERİN — dolgu güçlü, kontrast korunur
Dolgu ışığı      ÇOK GÜÇLÜ ve motivasyonlu (yoğun saçılma) — bloom değil
Ses              GÜÇLÜ, ALÇAK, YAKIN — düşük frekanslar iyi taşınır
Egzoz            KISA, KALIN, hızla yayılan koni
                 ⚠️ Ders 36 burada TERSİNE döner: vakumun düz keskin
                   konisi bu ortamda fizik hatasıdır
Rüzgar           var ama yavaş; kumaşı kıpırdatır, kimseyi savurmaz
Kaldırma         ⭐ GERÇEK. Nötr yüzerlikte gövdeler havada durabilir.
                 Bu anti-gravite DEĞİL, Arşimet kuvvetidir — ve negatif
                 çekirdeğin "never hovering" yasağıyla çakışır.
                 ÇÖZÜM: yasağı toz/enkaz için koru, canlı için POZİTİF
                 kural yaz ("continuous self-powered motion at X m/s")
Kask             solunamaz bileşim → vizör %100 kapalı, ara durum yok
İlgili ders      36 (TERS), 39 (TERS), 41 (geçerli), 59 (pozitif isim)
Referans film    THE_HERD
```

## 3.5 VAKUM + İTKİ YERÇEKİMİ (yanan bir geminin yanı/içi)

> 🆕 THE UPHILL DARK ile açıldı (17.08.2026). Bu kart, **sürekli itki
> altındaki** bir gövdenin yanında ya da içinde geçen her sahnenin ön
> şartıdır. 3.1'in (vakum) alt kartıdır: oradaki her kural geçerlidir,
> yalnız **tek bir kural tersine döner** — ve o kural depodaki en dirençli
> hatalardan birini (Ders 23) yapısal olarak kapatır.

```
Toz              vakumdaki gibi: kaldıracak hava yok, DIŞARIDA 0 kare
Gölge            MUTLAK SİYAH, jilet keskin (3.1 ile aynı)
Dolgu ışığı      YOK — tek istisna motorun alevi: 400 m'lik gerçek bir
                 YAYICIDIR, alttan aydınlatır. "Dolgu" değil kaynaktır;
                 gölgenin ALT kenarı yumuşar, ÜST kenarı mutlak siyah kalır
Ses              dışarıda yok; içeride yalnız gövdeden iletilen
Egzoz            düz keskin koni, seyrelir — kıvrılmaz [D36]

⭐ TERSİNE DÖNEN KURAL — SÜZÜLME YOK
   İtki altındaki gövdenin yanındaki her SERBEST cisim, gövdeye göre
   kıça doğru DÜŞER: a = itki ivmesi. 0.220 g'de 1 saniyede 1.08 m,
   3 saniyede 9.7 m, 10 saniyede 108 m.
   → "yukarısı" pruva, "aşağısı" motor. Uzayda yokuş vardır.
   → Ders 23 (süzülen beden rijit çıkıyor) TETİKLENEMEZ: hiçbir kare
     sıfır-g'de değildir. Bu, prompt cümlesiyle değil KARARLA kapatılmış
     bir risktir.

KANIT NESNELERİ  Durum ekranda kanıtlanmazsa ölçülemez [D95 mantığı].
                 Üç ucuz kanıt: (a) sarkan bir kordon/zincir — itki varsa
                 gergin ve dikey, (b) atılan/kopan her parçanın kadrajın
                 ALTINA hızlanarak gitmesi, (c) kabin içinde kemer
                 gerginliği ve gövdenin koltuğa çökmesi.

İTKİ DEĞİŞİMİ    Ağırlık değişimi görünür: itki artarsa gövdeler koltuğa
                 çöker ve kemer gerilir; azalırsa kemer gevşer ve gövde
                 yükselir. Sahnede itki değişiyorsa bu iki cümle yazılır.
⛔ 25.08.2026 — KARTIN İLK ÖLÇÜLEN FİLMİ, TERSİNE DÖNEN KURALI EKRANA
   GETİREMEDİ. THE IRON SLOPE (dikey) üretildi: 12 promptun 12'sinde
   "2,16 m/s² · 1 s → 1,08 m · 3 s → 9,7 m" yazılıydı; ekranda serbest
   panel gövdeye göre SABİT ~0,15 m/s süzüldü ve 10 saniyelik klibin
   sonunda hâlâ kadrajdaydı. Kartın kanıt nesnesi (b) — "kopan parçanın
   kadrajın ALTINA hızlanarak gitmesi" — bu yüzden ARTIK BİR SAYIYLA
   YAZILIR: parça kadrajı ≤ 1 saniyede terk eder [Ders 127]. Kanıt (a)
   da düştü: şakül şeridi kıvrıldı.
İlgili ders      36 (alev · geçerli) · 23 (elenir) · 30/39 (parçacık) ·
                 ⭐ 127 (ivme yazılmaz, kadrajı terk etme süresi yazılır —
                 bu kartın tersine dönen kuralının prompt hâli) ·
                 ⭐ 148 (kalkışta bacak HİÇ hareket etmez; alev bacakların
                 ARASINDA ve arkası görünür — "legs folding" yazılmaz) ·
                 149 (0g'de kemerli insanın kolları da yüzer: önkol 5-8 cm
                 havada; kanıt nesnesi ADLI ve ≥ 10 cm, "toz zerresi" cıvata olur)
Referans film    THE UPHILL DARK (yatay_4_dk_filmler/) · ölçülmüş
                 karşı-örnek: THE IRON SLOPE (dikey_shorts_filmler/)
```

## 3.6 SÜREKLİ BULUT / NÖTR YÜZERLİK (Venüs bulut katmanı, 55 km bandı)

> 🆕 LOSS OF LIFT ile açıldı (yazım 20.08.2026 · kart 21.08.2026'da
> plandaki öneriden terfi etti). Zemin yerine BULUT içinde, yüzen bir
> gövdede geçen her filmin ön şartıdır. 3.4'ün (kalın atmosfer)
> akrabasıdır ama üç kuralı ayrışır: toz YOK · gölge YOK · bağıl rüzgâr 0.

```
Toz              YOK — yüzey yok, kaynak yok. D39 tetiklenemez.
Gölge            YOK ya da neredeyse yok; ışık her yönden gelir.
                 Gölgesizlik MEŞRUDUR, hata değil.
Dolgu ışığı      ÇOK GÜÇLÜ ve motivasyonlu (bulut içi çoklu saçılma)
                 ⚠️ Ama bloom yine YASAK: yumuşak ışık ≠ parlama halkası [D41]
Güneş            DİSK YOK, ışın demeti yok, lens parlaması yok
                 → D104 (ışık mıknatısı) yapısal olarak zayıflar
Ufuk/zemin       İKİSİ DE YOK — yukarısı parlak kubbe, aşağısı okra uçurum;
                 ölçek yakın nesneyle kurulur
Ses              yoğun CO2: iyi taşır, tınılar ALÇALIR
Rüzgar           BAĞIL 0-2 m/s — akıntıyla sürükleniyorsun (süper-rotasyon).
                 Kumaş kıpırdamaz, hiçbir şey savrulmaz.
Kaldırma         ⭐ GERÇEK (Arşimet). Gövde havada DURUR.
                 ⚠️ Negatif çekirdeğin "never hovering" yasağıyla çakışır.
                 ÇÖZÜM [3.4 kartıyla aynı]: yasağı PARÇACIK için koru,
                 gövde için POZİTİF kural yaz —
                 "the station floats in neutral buoyancy and is settling
                  at a constant 30 metres per hour; it never hovers,
                  never hangs motionless, never rises"
Kask             dışarısı solunamaz (CO2 + asit) → vizör %100 kapalı,
                 ara durum YOK
Yerçekimi        0.904 g — yürüyüş Dünya gibi, süzülme yok
İlgili ders      39 (elenir) · 41 (geçerli) · 59 (pozitif isim) ·
                 104 (zayıflar) · 79 (vizör/sırt)
Referans film    LOSS OF LIFT (yatay_4_dk_filmler/)
```

---

## 3.7 VAKUM + DÖNME YERÇEKİMİ (dönen bir halkanın iç güvertesi) 🆕

> 🆕 THE HEAVY SIDE ile açıldı (29.08.2026). Bu kart, **dönerek kendi
> ağırlığını üreten** bir gövdenin içinde geçen her sahnenin ön şartıdır.
> 3.1'in (vakum) alt kartıdır — oradaki her kural geçerlidir — ama
> §3.5'ten (itki yerçekimi) farklı biçimde **iki kural birden** tersine
> döner ve ikisi de aynı denklemden çıkar: **a = (v ± u)² / R.**

```
Toz              vakumdaki gibi: kaldıracak hava yok, 0 kare
Gölge            MUTLAK SİYAH, jilet keskin (3.1 ile aynı)
Dolgu ışığı      YOK. Metal bir yapıda model ikincil yansıma üretmeye
                 çok yatkındır — pozitif cümle her prompta yazılır
Ses              dışarıda yok; ama YAPI bir ÇANDIR: alüminyumda 5.100 m/s,
                 her temas çevreyi milisaniyelerde dolaşıp çok yansımalı
                 uzun bir kuyrukla geri gelir. Duyulan her şey TEMASTIR
Rüzgar           yok · egzoz/alev/kıvılcım yok

⭐ TERSİNE DÖNEN KURAL 1 — AĞIRLIK YÖNE BAĞLIDIR
   Etkin ağırlık gövdenin MERKEZE GÖRE toplam teğetsel hızından gelir:
     a = (v_çember ± u)² / R
   Dönüşle aynı yöne koşmak ağırlığı ARTIRIR, ters yöne koşmak
   AZALTIR; ters yöne v_çember hızıyla koşan gövde ağırlıksızdır.
   → Aynı güvertede, aynı adım, iki farklı ağırlık. Süreklilik
     hatası DEĞİL, ortamın kuralıdır.
   → İLERİ SIÇRAYIŞIN MATEMATİKSEL TAVANI VAR: menzil = 2wR·u/(v+u)²
     ve u = v'de maksimumdur → menzil_max = wR / (2v). Bir insanın
     ileri sıçrayışı bu sayıyı GEÇEMEZ, ne kadar hızlı koşarsa koşsun.

⭐ TERSİNE DÖNEN KURAL 2 — BIRAKILAN ŞEY YANA İNER
   Serbest cisim atalet çerçevesinde DÜZ gider; güverte altından
   döner. Sapma dönüşün TERSİNEDİR ve h yüksekliğinden bırakılan
   cisim için tam olarak hesaplanır (kiriş/atalet yöntemi):
     r0 = R − h · kiriş d = √(R²−r0²) · v0 = ω·r0 · t = d/v0
     sapma = R · (ω·t − arctan(d/r0))
   Örnek (R = 9,00 m · T = 9,90 s · h = 1,40 m): t = 0,97 s,
   sapma = 0,62 m. ⭐ Ortamın en ucuz ve en okunaklı KANITIDIR.

⭐ ÜÇÜNCÜ SONUÇ — İÇERİ TIRMANMAK YANA İTER
   Merkeze doğru v hızıyla tırmanan gövdeye 2ωv Coriolis ivmesi
   biner; yerel ağırlık a = ω²r yükseldikçe düştüğü için yalpalama
   açısı YUKARI ÇIKTIKÇA BÜYÜR. Merdiven düz, gövde değil.

KANIT NESNELERİ  Durum ekranda kanıtlanmazsa ölçülemez [D95 mantığı].
                 Üç ucuz kanıt: (a) bırakılan küçük bir KATI cismin
                 yana inmesi — SÜRE ve MESAFE ile yazılır [D127],
                 (b) aynı gövdenin iki yönde iki farklı ağırlıkta
                 görünmesi (katlanan diz / yerden kesilen adım),
                 (c) sarkan bir halatın SARKMA DERİNLİĞİ — doğrudan
                 bir gravimetredir ve metinsiz bir sayaçtır [Kart 5].

COĞRAFYA         Halkanın içinde OKLÜZYON YOKTUR: güverte içbükeydir,
                 karakterin önü ve arkası yukarı kıvrılır ve başının
                 üstünde kapanır. "Tavan" alttan görülen AYNI
                 güvertedir. ⛔ Bu yüzden kadrajın üst bandında her
                 zaman ikinci bir güverte görünür ve model oraya
                 İKİNCİ BİR İNSAN koymaya yatkındır: "no one is
                 standing on it" cümlesi Kart 4'ün bu ortamdaki
                 zorunlu hâlidir.
                 ⚠️ VE SABİT KAMERA MENZİLİ SINIRLIDIR: güverte
                 düzeyindeki bir mercek halkanın ancak üçte birini
                 görür. Uzun mesafeli hareket planlanırken kadraj
                 menzili ÖNCE hesaplanır, sonra sahne yazılır.
IŞIK             Dönme ekseni yıldıza bakıyorsa ışık eksene paralel
                 gelir ve güverteyi YALAYARAK aydınlatır; bu geometri
                 halkanın dönüşüyle DEĞİŞMEZ. ⭐ Altı klibin ışık
                 sürekliliği böylece fizikle garanti altına alınır —
                 bu kartın bedava kazancıdır ve tasarımda tercih edilir.
İlgili ders      30/39 (parçacık · geçerli) · 23 (gövde hiçbir karede
                 sıfır-g'de değilse ELENİR) · 26 (halat) · 127 (ivme
                 yazılmaz, süre ve mesafe yazılır) · 104 (ışık eksende
                 ise mıknatıs yapısal olarak zayıflar) · 79 · 138
Referans film    THE HEAVY SIDE (dikey_shorts_filmler/) — yazıldı,
                 üretilmedi (29.08.2026)

⭐ DEVİR SAYISI — 04.09.2026'da eklendi (TUR 9)
   1 g üretmek için gereken yarıçap (a = ω²r):
       1 RPM → 895 m    2 RPM → 224 m    4 RPM → 56 m    6 RPM → 25 m
   Tasarım ölçütü 1-2 RPM'dir; üstü adaptasyon gerektirir.
   ⚠️ Bu bir fizyolojik yasa değil ÖLÇÜTTÜR.

   ⛔ VE BU KARTIN KENDİ ÖRNEĞİ ÖLÇÜTÜN TAMAMEN ÜSTÜNDE:
      THE HEAVY SIDE'ın halkası SABİT DÖNMÜYOR, HIZLANIYOR —
      periyot 60 saniyede 13,00 s'den 8,00 s'ye iniyor (R = 9,00 m):
          başlangıç  T = 13,00 s → 4,6 RPM → 2,10 m/s² = 0,21 g
          son        T =  8,00 s → 7,5 RPM → 5,55 m/s² = 0,57 g
      Bandın tamamı 1-2 RPM ölçütünün üstünde. Bu bir kusur DEĞİL —
      hızlanma filmin KONUSUDUR — ama plana yazılır: bu ortamda kimse
      adapte olmuş sayılmaz. (Sayılar filmin QA_SPEC'inde durur.)

   ARKA PLAN SÜPÜRME HIZI = RPM × 6 °/s
       2 RPM → 12 °/s   ·   4 RPM → 24 °/s   ·   6 RPM → 36 °/s
       8 saniyelik planda: 96° · 192° · 288°.
       ⭐ Sabit kamerada dönmenin en ucuz kanıtı budur ve SÜREYLE
         yazılır: "the starfield sweeps most of the way around the
         frame during the shot" — derece YAZILMAZ [D138].
```

---

## 3.8 VAKUM + TEMİZ METAL — SOĞUK KAYNAK (havasız bir ayda metal enkaz) 🆕

> 🆕 THE COLD WELD ile açıldı (01.09.2026). §3.1'in (vakum) alt kartıdır —
> oradaki her kural geçerlidir — ve §3.5/§3.7 gibi **tek bir kuralı**
> tersine çevirir. Kartın ön şartı basittir: kadrajın zemini **oksitsiz,
> çıplak metal** olmalıdır.

```
Toz              vakumdaki gibi kaldıracak hava yok — ⭐ AMA BU KARTTA
                 ZEMİN METALDİR ve göktaşı bombardımanı onu temizlemiştir:
                 metalin üstünde 0 kare toz. Toz yalnız metalin DIŞINDAKİ
                 regolitte görünür.
Gölge            MUTLAK SİYAH, jilet keskin (3.1 ile aynı)
Dolgu ışığı      YOK. ⚠️ Metal bir yapıda model ikincil yansıma üretmeye
                 çok yatkındır — pozitif cümle her prompta yazılır
Ses              dışarıda yok; YAPI bir PLAKADIR: duyulan her şey temastır,
                 gövdeden iletilir, kuru ve kısa
Rüzgâr           yok · egzoz/alev/kıvılcım yok · pas 0 kare (oksijen yok)

⭐ TERSİNE DÖNEN KURAL — DEĞEN ŞEY BİRLEŞİR
   Oksit ve adsorbe gaz katmanı olmayan iki metal yüzey temas ettiği anda
   ATOMİK olarak birleşir: ısı yok, kaynak yayı yok, temas KAYNAKTIR. Bu
   uydurma değil, belgelenmiş bir uzay mühendisliği sorunudur (kilitlenen
   menteşeler, açılmayan mekanizmalar; yüzeyler bu yüzden kaplanır).
   → Bu ortamda "gevşek parça" YOKTUR. Düşen alet düştüğü yerde KALIR.
   → Yıllar içinde bir enkaz enkaz olmaktan çıkar: parçalar birbirine
     kaynayıp TEK GÖVDEYE dönüşür.
   ⛔ Bağ ATOMİKTİR, GEOMETRİK DEĞİL: iki yüzey ayrı ayrı görünür kalır ve
     aralarında net bir sınır vardır. "El metale eriyor / batıyor" bir
     ÜRETİM HATASIDIR [D24 temas bütünlüğü], kartın kuralı değil.

⭐ İKİNCİ KURAL (BİRİNCİNİN SONUCU) — IŞIK KAYNAĞI BOZAR
   Gölgede ~100 K'de duran bir levha ışığa girince ~370 K'ye çıkar ve
   metrede yaklaşık 1,3 mm uzar. Karşı taraf hâlâ gölgedeyse dikiş bunu
   kaldıramaz ve KOPAR. → Işık çizgisi ilerledikçe yıllardır tek parça
   olan şey saniyeler içinde ayrı parçalara ayrılır. Kopuş SOĞUKTUR:
   kıvılcım 0 · ısı parlaması 0 · duman 0 · erimiş metal 0.
   ⚠️ Maya eşiği korunur [ONERME §3]: film başına 1 ihlal; bu ikinci
     kural birincinin SONUCUDUR, bağımsız ikinci kural değildir.

ASİMETRİ ŞART    Kaynak yalnız TEMİZ metal-metal temasında olur. Seramik
                 kaplı yüzey, kumaş ve cam kaynamaz. ⭐ Bu asimetri
                 karakterin bütün hareket dilbilgisini kurar (botla
                 yürünür, avuçla tutulmaz) ve her prompta POZİTİF hâlde
                 yazılır [D59]; yazılmazsa model ya her şeyi yapıştırır
                 ya hiçbir şeyi.
KANIT NESNELERİ  Durum ekranda kanıtlanmazsa ölçülemez [D95 mantığı].
                 Üç ucuz kanıt: (a) uçan bir levhanın üstünde DİK duran
                 bir alet — gevşek değil, kaynamış; (b) bir avucun
                 kalkmaması ve kalkınca YERDE bir iz bırakması;
                 (c) tekmelenen bir parçanın düştüğü yerde SAPLANIP
                 kalması, kaymaması.
⚠️ METİN RİSKİ   Bu kartın zemini İŞLENMİŞ METALDİR ve model metal yüzeye
                 numara, seri işareti, ölçü çentiği ve uyarı damgası
                 basmaya en yatkın olduğu yer burasıdır [D138]. Karşı
                 önlem POZİTİFTİR: "bilgi taşıyan tek şey dikiş, perçin
                 ve göktaşı çukurudur".
İlgili ders      30/39 (parçacık) · 23 (gövde sıfır-g'de değilse ELENİR) ·
                 24 (temas bütünlüğü) · 26 · 31 · 59 (pozitif isim) ·
                 104 (tek baskın ışık) · 127 (ivme yazılmaz, süre ve
                 mesafe yazılır) · 138 (metin yasağının KAPSAMI) · 79 · 139
Referans film    THE COLD WELD (yatay_2_dk_filmler/) — yazıldı,
                 üretilmedi (01.09.2026)
```

---

## 3.9 KRİYOJENİK ORTA BASINÇ (95 K · 0,90 bar N₂+CH₄ · 0,38 g) 🆕

> 🆕 THE HEALING GROUND ile açıldı (04.09.2026). **§3.3'ün (Dünya benzeri
> basınç) alt kartıdır** — o kartın kendi notu bu kapıyı açık bırakmıştı:
> *"Dünya benzeri atmosferi olan bir GEZEGEN konsepti bu fiziği kullanır."*
> Oradaki her satır geçerlidir; **üç satır 95 K'de tersine döner.** Kartın
> ön şartı basittir: dış sıcaklık gövde sıcaklığının 200 K'den fazla ALTINDA
> ve atmosfer yoğun.
>
> ⚠️ **Fizik gerekçesi (kartın kendi savunması):** 0,38 g'lik bir gövde
> 0,90 bar azotu TUTAR, çünkü tutan şey yerçekimi değil SOĞUKTUR — Titan
> 0,14 g'de 1,45 bar taşıyor (Cassini–Huygens, 2005). Bu kart yazılırken
> "küçük gezegen kalın atmosfer tutamaz" refleksi bir kez sınandı ve düştü.

```
Toz/kar          HIZLI çöker: yoğun hava (~3,2 kg/m³) taşımaz, kalkan kırağı
                 0,4 saniyede oturur. Asılı toz perdesi YOKTUR.
                 → Ders 39 geçerli · Ders 143 geçerli (zerre SAYISI yazılır)
Gölge            yumuşak kenarlı ve SIĞ; dolgu her yönden gelir.
                 Mutlak siyah gölge YOK — hata değil, ortamın kuralı.
Dolgu ışığı      ÇOK GÜÇLÜ ve motivasyonlu (sürekli pus).
                 ⚠️ Ders 41 burada KRİTİK: yumuşak ışık ≠ bloom.
Güneş            DİSK YOK, hüzme yok, lens parlaması yok
                 → KART 9 (ışık mıknatısı) yapısal olarak ZAYIF.
Ses              199 m/s (95 K azotta): alçak frekanslar GÜÇLÜ ve YAKIN
                 taşınır, tizler anında ölür. Ses Dünya'dan daha iyi taşır,
                 daha AĞIR duyulur.
Rüzgâr           1-2 m/s; kumaşı bile kıpırdatmaz, kimseyi itmez.
Nefes            dışarıda görünür buhar YOK (gövde mühürlü). Giysinin
                 VENT'inden çıkan sıcak gaz anında ince KURU KAR olur ve
                 düşer — ⭐ metinsiz bir sayaç olarak kullanılabilir.
Sıvı             yüzeyde YOK (bu kartın seçtiği bant); metan yalnız gaz
                 hâlinde. → KART 1 açılmaz, açılırsa kart değişir.

⭐ TERSİNE DÖNEN KURAL — SICAK OLAN İZ BIRAKMAZ
   95 K'lik bir yüzeye değen 310 K'lik bir gövde, temas noktasını gaza
   çevirir: ince beyaz bir buhar yakası kalkar, 0,5 m yükselir ve 2 saniyede
   ince kuru kar olarak geri düşer. Bu ortamda bir yüzeye "iz bırakmak"
   ısıtmakla değil SOĞUMAKLA olur.
   → Ders 36 (vakum dumanı) TETİKLENEMEZ: atmosfer var, koni kabarır.
   → Ders 24 (sıvı temasında el erir) tetiklenemez: sıvı yok.
   → Ders 23 (sıfır-g süzülme) ELENİR: hiçbir kare 0 g'de değil.

KANIT NESNELERİ  Durum ekranda kanıtlanmazsa ölçülemez [D95 mantığı].
                 Üç ucuz kanıt: (a) sıcak bir nesnenin çevresinde DİK duran
                 buhar yakası — SÜRE ve YÜKSEKLİKLE yazılır [D127];
                 (b) giysinin vent tüyünün uzunluğu (ısı bütçesinin metinsiz
                 sayacı, monotonik yazılır); (c) ortam sıcaklığındaki eski
                 bir nesnenin çevresinde HİÇBİR ŞEY olmaması — kuralın ters
                 kanıtı ve en ucuzu.
Kask             solunamaz bileşim + 95 K → vizör %100 kapalı, ara durum YOK
                 (cam optik BERRAK — D79; kapalı olmak tintli olmak değildir)
⚠️ ÇIPLAK DERİ   Bu kartta çıplak deri bir devamlılık hatası değil, bir FİZİK
                 hatasıdır: 95 K'de açıkta kalan bilek saniyeler içinde iş
                 göremez. Negatif ÜÇ BÖLGELİ yazılır [D175].
İlgili ders      39 · 41 · 143 · 145 (ufuk kilidi) · 175 (mühür) · 176
                 (kontrast garantisi zemine renk vermez) · 79 · 127
Referans film    THE HEALING GROUND (yatay_2_dk_filmler/) — yazıldı,
                 üretilmedi (04.09.2026)
⭐ 22.09.2026    THE_SLOW_RAIN (yatay_8_dk_filmler/) bu kartın SIVI BANDINI açtı:
                 metan yağmuru (bilye boyu damla ~3 m/s), göl yatağının dolması,
                 giysili temas 5 sahne (KART 1 açık). "Sıvı yüzeyde YOK" satırı o
                 filmde D74 sapması olarak kayıtlı (02_KONSEPT §1); kartın ikiye
                 bölünmesi (§3.9 kuru / §3.9b sıvı) SAHİP KARARI ⬜ — burada yalnız
                 rapor ediliyor, satır değiştirilmedi.
```

---

## 3.10 BASINÇLI İÇ HACİM (istasyon/üs iç mekânı · ~1 atm · 0 g veya dönme g) 🆕

> 🆕 TUR 9 ile açıldı (04.09.2026). Bu kart, **basınçlı bir gövdenin
> İÇİNDE** geçen her sahnenin ön şartıdır. §3.1'in (vakum) alt kartı
> DEĞİLDİR — tam tersidir: burada hava vardır ve §3.1'in üç sert kuralı
> birden tersine döner. Mimari tarafı `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md`
> §4'tedir; bu kart yalnız ORTAMI tanımlar.

```
Toz              ⚠️ EN TEHLİKELİ SATIR BUDUR — negatif çekirdek ve
                 Ders 39 ile çarpışma riski taşır ve KAPSAMLA çözülür.
                 Çekirdek "never hovering, never frozen, never swirling
                 or flowing like liquid" der ve bu YASAK AYNEN GEÇERLİDİR:
                 zerre asılı DURMAZ, savrulmaz, akıntı gibi kıvrılmaz.
                 Değişen tek şey ŞU: 0 g'de zerre YERE DE OTURMAZ.
                 ✅ Doğru hâli TEK YÖNLÜ VE SÜREKLİ hareket [D59 pozitif
                    isim]: "a single mote drifts in one straight line
                    across the frame at a constant slow pace, carried by
                    the vent flow, and leaves the frame"
                 ⛔ Kadrajda birden çok serbest zerre YAZILMAZ; sayıları
                    her karede değişir. Bir tane, tek yön, sabit hız.
                 ⛔ "yere oturan toz" da fizik hatasıdır (yerçekimi yok).
Gölge            ⭐ TERSİNE DÖNEN KURAL 1 — MUTLAK SİYAH BİTTİ.
                 İç yüzeyler açık renklidir ve çok yansımalıdır; dolgu
                 ışığı VAR ve motivasyonludur. §3.1'in "gölgede kalan
                 yüzey gerçekten siyah" satırı BURADA GEÇERSİZDİR.
Dolgu ışığı      VAR — panel yüzeylerinden gelen ikincil yansıma.
Ses              ⭐ TERSİNE DÖNEN KURAL 2 — HAVA TAŞIR.
                 §3.1/3.7/3.8'in "duyulan her şey TEMASTIR" kuralı
                 burada geçmez: nefes, fan, panel tıkırtısı havadan
                 duyulur. Sürekli fan gürültüsü ortamın zeminidir ve
                 sessizlik ANLAMLIDIR (güç kesildi demektir).
Rüzgar           yok, ama havalandırma akımı var — kumaş/kablo ucu
                 tek yönde ve YAVAŞ kıpırdar, dalgalanmaz.
Işık             ~4500 K nötr beyaz, parlamasız, tavana gömülü.
                 Kaynak doğrudan göze gelmez.
Lens             KÜRESEL. Dar hacimde anamorfik yatay parlama yasağı
                 §3.1'le aynı gerekçeyle sürer (§11).

⭐ TERSİNE DÖNEN KURAL 3 — "YUKARI" GÖRSELDİR, BİYOLOJİK DEĞİL
   Mikro yerçekiminde yukarı/aşağı yoktur; RENKLE kurulur ve film
   boyu değişmez:
       tavan  beyaz        duvar  krem        zemin  koyu (zeytin/kahve)
       ışık   yalnız tavandan aşağı
   Bu üç satır yazılmazsa izleyici yönünü kaybeder ve model her
   karede yeni bir "aşağı" icat eder.
   ⚠️ Dönme g varsa yerel dikey FİZİKSELDİR ve kart §3.7'dir; bu kart
      yalnız 0 g içindir.

GEOMETRİ         Yaşanabilir kesit ~2 × 2 m'lik KARE bir tüneldir;
                 dört yüzey de raf sırasıdır, köşeler tesisat kamasıdır.
                 "Zemin" yoktur, dört duvar vardır.
                 Kapak iki sınıftır: geniş yanaşma (~1,27 m, yuvarlatılmış
                 kare) ve dar kenetlenme (~0,80 m, daire). Ayrımı ve
                 prompt karşılıkları: UZAY_USSU kılavuzu §2.3.

METİN RİSKİ      ⛔ EN YÜKSEK RİSKLİ ORTAM BUDUR. Gerçek iç mekân
                 etiket, barkod ve ekranla KAPLIDIR; model eğitim
                 verisinden bunu getirir. Negatif çekirdeğin kapsamlı
                 metin cümlesi (§5) bu kartta ZORUNLU ve kısaltılamaz
                 [D138]. Panel yüzeyleri renk kodlu ve BOŞ yazılır.
                 Ekranlar kapalı ya da salt geometrik desenlidir.

İlgili ders      138 (metin yasağı kapsamı) · 45 (dizge riski) ·
                 30/39 (parçacık — burada TERS) · 79 (sırt ünitesi) ·
                 153 (gevşek kumaş tarifi ayrı nesne doğurur)
İlgili kılavuz   UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md §4
Referans film    ⛔ YOK — bu kart TUR 9 ile açıldı, henüz film yazılmadı.
                 İlk yazılan film bu kartın referansı olur.
⚠️ AÇIK          İç mekânda gövde boyu cetveli YOK (karakter kasksızdır);
                 iç oranlar bugün yalnız NİTELİKSEL yazılır. TUR 9 bunu
                 ölçmedi, bir sonraki tura kaldı.
```

---

# 4. 🎭 TÜR KARTLARI

## 4.1 BİLİMKURGU

```
KİLİTLER
  Vizör kalıcılığı [D5]      her karede görünür, tam şeffaf, HUD yok
  Gemi ölçek kilidi [D32]    kapı/kanat/ayak geometrisi sahneler arası sabit
  Sıfır-g mikro hareket [D23] süzülen beden rijit değil — eksen dönüşü, uzuv sürüklenmesi
  Halat fiziği [D26]         gergin halat düz, katı cisim çarpışmasına uyar
KARAKTER    VARSAYILAN tek kâşif, yalnız. Diyalog varsa AI sesi veya kayıt.
            İkinci figür YASAK DEĞİL, BÜTÇELİ: ancak novum onu gerektiriyorsa
            ve plana altı satırlık ayrım bütçesi yazıldıysa gelir — üç kanal
            (siluet · kostüm · hareket), yüze bağlı OLMAYAN.
            Emsal: THE_ROSE_COAT §0.8b (12 sahne iki figür, kadraj kilidi tuttu).
            Gerekçesiz ikinci figür = iki yarım karakter [Kart 4 · D20 · D69].
            YETKİNLİK KURALI: hata bilgi eksikliğinden, aptallıktan değil.
TON         Huşu ve varoluşsal huzur ("Overview Effect"). Korku değil.
SENARYO
  → UZAY_SENARYO_KILAVUZU.md (Novum, bilişsellik etkisi, exposition
    tuzağı, mimari psikoloji, Çehov, antagonist kanalları)
```

## 4.2 ZOMBİ ⏸️ RAFTA — 26.08.2026'da KAPANDI (kart H2)

> ⛔ **BU TÜR KAPALIDIR. Depo yalnız UZAY filmleri içindir.** 26.08.2026'da
> zombi klasörü ve dört zombi filminin dördü birden kaldırıldı — ikisi
> `yatay_2_4_dk_filmler_zombi/` içindeydi (THE HELD HEAT · THE LAST SPAN),
> ikisi `dikey_shorts_filmler/` içinde duruyordu (THE SHORT WAY DOWN ·
> THE STRAIGHT LINE). Aşağıdaki kart SİLİNMEDİ çünkü kılavuz bilgisi ucuz,
> yeniden yazmak pahalı (kart H2 kuralı) — ama **bu kartla film yazılmaz.**
>
> ⚠️ **Kart geri açılırsa** kart H koşulur ve açılış şartı aşağıdaki ALTI
> SATIRLIK BÜTÇEdir. Ayrıca bu turun dersi eklenir: tür klasöre eşit
> değildir — zombi filmlerinin yarısı zombi klasöründe değildi. Türü
> kapatmak, klasörü silmekle bitmez (AGENTS kart H2, üçüncü tur notu).
>
> ⏸️ Aşağıdaki metin 23.08.2026'daki AÇIK hâlinden korunmuştur:

> Kart 12.08.2026'da tamamen rafa kalkmıştı (klasör ve referans film
> silindi). Önce DİKEY hatta geri açıldı —
> `dikey_shorts_filmler/THE_SHORT_WAY_DOWN/THE_SHORT_WAY_DOWN_DIKEY_SHORTS.md` (merdiven) ve
> `dikey_shorts_filmler/THE_STRAIGHT_LINE/THE_STRAIGHT_LINE_DIKEY_SHORTS.md` (açık yol,
> 23.08.2026) — sonra
> **23.08.2026'da YATAY hat da geri açıldı**: klasör
> `yatay_2_4_dk_filmler_zombi/` kart H ile yeniden kuruldu, referans film
> `THE_LAST_SPAN_VIADUCT_FILM.md` (12 × 10 s = 2:00, 0 kesme, 12/12
> lockoff, 0 replik, risk 5/12).
>
> ⭐ **Kartı geri açan kararın mekanizması, çünkü tekrarlanabilir:** türün
> rafa kalkma sebebi olan üç kilidin (canlı anatomisi [D2] · yürüyüş
> eklemlenmesi [D18] · sürü sayısı) üçü de **HAREKETLİ figür** sorunudur —
> ve bir KOVALAMACA filminde bu sorun elenemez, yalnız **bütçelenebilir.**
> Dikey hattın İKİ filmi bunu iki ayrı yoldan yaptı ve ikisinin de
> sayıları kartın parçası sayılmalı:
>
> **① THE SHORT WAY DOWN (dikey · merdiven · 22.08.2026)**
>
> ```
> HAREKET BİÇİMİ DEĞİŞTİRİLDİ   takipçiler merdivenden inmez, korkuluğu
>                               aşıp DÜŞER. Düşüş balistiktir ve model
>                               onu doğru üretir; D18 yalnız eklemli
>                               yürüyüşte tetiklenir.
> YÜRÜME BÜTÇESİ  4,5 sn / 48   kalan 43,5 saniyede takipçiler düşüyor,
>                               iniyor, kalkıyor ya da korkuluğu aşıyor
> TEMAS           0 kare        en yakın mesafe 2,5 m → D17/D28 elendi
> YÜZ             0 kare        figürler beton tozuyla kaplı →
>                               D16 morph + D20 klon zemini birlikte elenir
> YARA            0 kare        kartın "2-3 KAPALI yara" bütçesi SIFIRA
>                               indi; toz doğal sansürdür
> ```
>
> ⛔ Bu bütçeye rağmen film **risk 6/12 ile eşiğin ÜSTÜNDEDİR** ve dosyası
> bunu gizlemez.
>
> **② THE STRAIGHT LINE (dikey · açık yol · 23.08.2026)** — aynı türün
> ikinci denemesi; MEKÂN değiştirilerek risk 6/12'den **4/12'ye** indi:
>
> ```
> KOŞU BİÇİMİ SEÇİLDİ   takipçiler SALLANMAZ, TAM SPRINT koşar. Ölçülmüş
>                       gözlem: model tam sprinti, sallanan/sürünen
>                       yürüyüşten çok daha iyi üretir. Türün klasik
>                       "shambling" imgesi promptlarda YASAKLANDI.
> YÖRÜNGE DÜZ           dönüş, kavis, yalpalama, fren 0 kare — modelin
>                       en çok bozduğu hareket konseptten çıkarıldI.
>                       Novum'un kendisi zaten "dönememek"tir.
> KONTRA IŞIK           güneş takipçilerin ARKASINDA: hepsi silüet →
>                       uzuv detayı azalır ve YÜZ 0 KARE olur
>                       (D16 morph + D20 klon zemini birlikte elenir)
> TEMAS           0 kare  en yakın mesafe 1,2 m → D17/D28 elendi
> YARA            0 kare  kartın "2-3 KAPALI yara" bütçesi SIFIRA indi;
>                       kontra ışık doğal sansürdür
> MEKÂN SEÇİMİ    ⭐      aynı konseptin BİNA İÇİ denemesi 6/12 ile
>                       eşiğin üstündeydi; AÇIK YOLA taşınınca Kart 6b
>                       (katmanlı dünya) ve Kart 8 (kamera) düştü →
>                       4/12. Mekân, prompt iyileştirmesinden daha
>                       etkili bir risk aracıdır.
> ```
>
> ⛔ Tür geri açıldı ama BEDELSİZ açılmadı: aksiyon isteyen her yeni
> zombi filmi bu altı satırı yeniden bütçelemek zorundadır.
>
> ⭐ **YATAY HATTIN BÜTÇESİ — THE LAST SPAN (23.08.2026).** Şart
> uygulandı ve altı satır yeniden yazıldı. Dört değer SIFIRA indi;
> mekanizma yine HAREKET BİÇİMİNİ değiştirmekti, prompt iyileştirmek
> değil — ve bu sefer değiştirilen şey **figürün harekete geçebilmesi**:
>
> ```
> HAREKET BİÇİMİ  figürler kendi başlarına HİÇ harekete geçmez. Kapalı
>                 liste: ① ayakta durma (0 hareket) ② devrilme (rijit
>                 gövde, ayak bileğinden, 1,1 s, YERDE KALIR) ③ temas
>                 sonrası omuz salınımı (≤4 cm, 0,5 s)
> YÜRÜME BÜTÇESİ  0,0 sn / 120 sn  — D18 TETİKLENEMEZ: tetiklenmesi için
>                 bir adım gerekir, film boyunca hiçbir figür adım atmaz
> TEMAS           0 kare · en yakın 40 cm · figür-figür teması VAR ve
>                 filmin novum'udur (iki temas türü promptlarda AYRI yazılır)
> YÜZ             0 kare · filmde tam 1 yüz ve o kasksız/maskesiz
> YARA            0 kare · gore bütçesi yine sıfır (toz doğal sansür)
> SAYI            sahne başına yazılı · yakın alanda hiçbir sahnede
>                 14'ten fazla ayrık figür; gerisi sığ odakta kütle
> ```
>
> ⛔ İki filmin ortak dersi: **bu türde çözüm prompt cümlesinde değil,
> figürün NE YAPABİLDİĞİNİ tanımlayan KAPALI LİSTEDEDİR** [AGENTS §8].
> Short Way Down düşüşü seçti (balistik), Last Span devrilmeyi seçti
> (rijit); ikisi de modelin doğru ürettiği hareketlerdir ve ikisi de
> eklemli yürüyüşü kadrajdan tamamen çıkarır.
> ⭐ **ÜÇÜNCÜ YOL — THE STRAIGHT LINE (23.08.2026):** eklemli yürüyüşü
> çıkarmadı, YÖNÜ çıkardı. Takipçiler tam sprint koşar (model bunu
> sallanan yürüyüşten daha iyi üretir) ama dönemez ve frenleyemez;
> "shambling" promptlarda yasaktır ve yörünge her sahnede POZİTİF
> yazılır ("a perfectly straight line"). Yani kapalı liste her zaman
> hareketi SİLMEK zorunda değildir — bir SERBESTLİK DERECESİNİ silmek
> de yeter. Kartın açılış şartı bu üçüncü biçimi de kabul eder.
>
> ⭐ **DÖRDÜNCÜ YOL — THE HELD HEAT (26.08.2026):** hareketi de yönü de
> silmedi, **YER DEĞİŞTİRMEYİ** sildi. Figürler topukları üzerinde
> döner (90° / 2,0 s) ve döndükleri yerde kalır; yer değiştirme 0,00 m.
> Böylece kalabalık bir tehdit değil **tek yönlü çevrilebilen bir
> KAPI** olur: dönmüş sıra omuz omuza kilitlenir (0,45 m aralık,
> geçit kapalı), sırtını dönen sıra 0,60 m açar.
>
> ```
> HAREKET BİÇİMİ  tek madde: topuk üzerinde 90° dönme, 2,0 s.
>                 Ayak yerden kalkmaz · diz bükülmez · kol kalkmaz ·
>                 baş gövdeden bağımsız dönmez · yer değiştirme 0,00 m ·
>                 geri dönüş 0 kare (dönüş KALICIDIR)
> YÜRÜME BÜTÇESİ  0,0 sn / 140 sn — D18 tetiklenemez
> TEMAS           0 kare · İKİ YÖNLÜ (kadın figüre değmez, figür kadına
>                 değmez) · mesafe kilidi her karede ≥1,20 m
> YÜZ             0 kare · kırağı kabuğu YALNIZ baş ve boyunda
> YARA            0 kare · giysiler bütün ve temiz, yalnız kırağılı
> SAYI            sahne başına yazılı · koridor 78 + terminal 40 = 118 ·
>                 tek karede en fazla 40
> ```
>
> ⛔ **BU BÜTÇENİN ANLAM MALİYETİ KAYDI — kartın en pahalı dersi.**
> LAST SPAN, D123 politika düzeltmesinde figürleri **baştan ayağa**
> toz mühürledi. Red gitti; türün anlam sermayesi de gitti. Zombi
> tematik olarak güçlüdür çünkü **gitmiş bir insandır**; toz mühürlü
> bir levha mobilyadır ve mobilya deviren film fizik demosudur.
> HELD HEAT kabuğu **yalnız başa** indirir ve gövdeye sıradan kış
> giysisi giydirir (parka, iş montu, kurye yeleği, okul çantası):
> *"bir zamanlar insandı"* bilgisi **giysiden** okunur, yüzden değil.
> Politika yüzeyi aynı kalır, anlam geri gelir.
> ⭐ Ayrıca aksiyonun cinsi değişti: LAST SPAN bir kalabalığı
> **HARCIYORDU** (400 temas, iki sahne politika reddi); HELD HEAT bir
> kalabalığı **YÖNLENDİRİYOR** (0 temas). Kimseye hiçbir şey olmuyor.
> ⛔ Bundan sonra bu karta gelen her film **anlam maliyetini de**
> bütçelemek zorundadır: altı satır fiziği kısıtlar, yedinci soru
> "geriye ne kaldı" sorusudur.

```
KİLİTLER
  Canlı anatomi kilidi [D2]  her figür ilk karesindeki siluetini korur, morph yasak
  Yürüyüş eklemlenmesi [D18] her adım kalkar-sürüklenir-basar; ASLA kayma
  Sayı kilidi                sürü sayısı prompta yazılır (1 → 3 → 60+), model şişirmesin
  Gore sınırı [D38 mantığı]  figür başına 2-3 KAPALI yara; organ/kopma/damlama yok
İPTAL OLAN KURAL
  ⚠️ VIDEO_QA'daki "no horror tone (should be awe/wonder)" maddesi
     BU TÜRDE GEÇERSİZ. Yerine: "no jump scares, no gore" korunur.
ARKA PLAN   Kalabalıktaki figürler sığ alan derinliğinde yumuşak tutulur —
            morph riski odak dışında eritilir.
REFERANS    ⛔ YOK — dört referans filmin dördü de 26.08.2026'da depodan
            kaldırıldı (kart H2, tür kapandı). Eski yolları yazmıyorum:
            kırık yol, olmayan dosyayı varmış gibi gösterir [AGENTS §6].
            Kart geri açılırsa ilk film yeni referans olur.
            Arşiv (depo dışı): film_md_ZOMBI_ARSIV_2026-08-26.tar.gz
```

## 4.3 SAVAŞ ⏸️ RAFTA (12.08.2026)

> Klasörü (`yatay_2_4_dk_filmler_savas/`) ve referans filmi kaldırıldı;
> yatay hat şimdilik üretilmiyor. Kart ve `SAVAS_SENARYO_KILAVUZU.md`
> duruyor — dikey `THE_DULL_EDGE` (savaş/tarihsel shorts) ikisini de kullanır.

```
KİLİTLER
  Düşman görünmezliği        ASLA net yüz, yakın çekim, isabet anı, ceset
                             Sadece: uzak namlu parlaması, dumanda siluet, çevresel sonuç
  Patlama sınırı [D38]       SAYILI ve yerel: "3m gri toz sütunu"
                             Ateş topu, mantar bulutu, şok dalgası YASAK
  Namlu parlaması            kısa keskin yönlü koni — parlayan top değil
  Mermi izi                  neon/lazer YASAK; gündüz neredeyse görünmez
  Kovan                      sağa ejeksiyon, yerçekimine uyar, yere düşer
POLİTİKA GÜVENLİĞİ
  Ceset/kan/yara/isabet = 0 prompt. Ateş çevreye yönelir, insana değil.
  Kayıp görsel değil İŞİTSEL anlatılır (telsize cevap gelmemesi).
  Bayrak, rütbe, gerçek ordu sembolü, silah markası YOK.
SENARYO
  → SAVAS_SENARYO_KILAVUZU.md (dramaturji, ahlaki yaralanma,
    savaşın sisi, aksiyon oranı, Truffaut testi)
```

## 4.4 YENİ TÜR ŞABLONU

```
KİLİTLER            [bu türe özel, model bozulan yerler]
İPTAL OLAN KURAL    [çekirdek/QA'daki hangi madde bu türde geçersiz?]
POLİTİKA RİSKİ      [üretim reddine yol açabilecek içerik ve çözümü]
REFERANS FİLM       [kurulduktan sonra doldur]
```

---

# 5. 🚫 NEGATİF ÇEKİRDEK — 8 CÜMLE her prompta (14.09.2026) · tam liste PLAN Negative Bible'da

> ⭐ **14.09.2026 REFORM — sahip kararı** (`TODO_AKIS_VE_DERS_REFORMU.md` FAZ 7).
> Bu başlık "tam metin — her prompta yapıştır" idi. Ölçüm (THE_LOCKED_PULSE, 13.09):
> IMAGE promptu ortalama 3.984 karakter / 719 kelime, **%57'si her promptta aynen
> tekrar**; tarif kilidi %0, sayısal kilit %100 tuttu — yani uzun blok tutmuyor,
> kısa sayı tutuyor. Prompta yalnız aşağıdaki **8 cümle** girer (+ en çok **3**
> sahneye özel cümle); eski tam metin §5.3'te durur ve PLAN'ın Negative Bible'ına
> iner, prompta girmez. Kapı: `prompt_kontrol.py` **㉗** (NEGATIVE > 11 cümle →
> FIX; sayı betikte, `NEGATIF_CUMLE_TAVANI`) — yalnız `00_ANALIZ/00_HIKAYE_ONAYI.md`
> taşıyan, 14.09'dan sonra açılan klasörlerde; eski klasörler eski kuralla kalır.
> ⑤ KİLİT'in beş imzası (tek çekim · bloom · metin · insan sayısı · grain) aranmaya
> devam eder — sekiz cümle beşini de taşır.
>
> Bu, `DERSLER/00_HIZLI_REFERANS.md` direktif bloğunun tür-bağımsız özüdür.
> Ortam ve tür kartlarından gelen maddeler prompta değil PLAN Negative Bible'a eklenir;
> prompta yalnız o sahnenin ≤3 cümlesi girer (§5.2).

## 5.1 ÇEKİRDEK — 8 cümle (VIDEO) · 7 cümle (IMAGE: ① düşer — tek çekim bir HAREKET kilididir)

```
Single unbroken take, no cuts, no dissolves, no camera resets, no angle change.
Exactly one human character, no duplicates, no second person.
0% bloom, no glow, no soft focus, every surface keeps visible texture.
No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark.
Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing.
Equipment and clothing identical throughout, no drift, no gear appearing or disappearing.
Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.
Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping.
```

```
① tek çekim (yalnız video)  ② insan sayısı  ③ bloom  ④ metin yasağı + KAPSAM [D138]
⑤ grain / fotogerçekçilik   ⑥ ekipman sabit  ⑦ el/sınır  ⑧ parçacık-yerçekimi + çevre
14.09.2026 ölçümü: 886 karakter / 139 kelime (eski tam metin 1.650 karakter).
⛔ Cümle sınırı NOKTA ile. Betik noktalı virgülü de cümle sayar (㉗); cümle içinde
   virgül ve uzun tire kullan. `Output:` satırı sayıma girmez.
```

## 5.1b ⛔ ÇEKİRDEĞİN SEKİZİNCİ CÜMLESİ BİR SAYI İSTER — 19.09.2026

Sekizinci cümle `Particles obey **the stated gravity**` diyor. §5 bugüne kadar
o değerin YAZILMASINI hiçbir yerde istemedi; cümle kendi kendine gönderme yapıyor
ve hiçbir şeyi kilitlemiyordu. Ölçüm (`FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/`):

```
ortam SAYISI    14/31 filmde HİÇ YOK
ortam ADI        6/31 filmde HİÇ YOK
ses yasası      24/31 filmde HİÇ YOK — hiçbir filmde tam değil

BENI_HATIRLAMA  çekirdeği %83 kapsamayla taşıyor, yerçekimini TARİFLE yazıyor
                ("about two thirds of Earth's weight") → ekranda 0,39 · 1,11 ·
                1,13 · 2,48 m/s² ölçüldü. 2,9× tutarsızlık, İKİ BLOCKER.
THE_FALLING_WORLD  "Gravity is 0.30 g" 48/48 promptta → BİR blocker.
→ sayı yarıya indiriyor ama sıfırlamıyor. Yine de yazılır.
```

⭐ **Bu yüzden çekirdek sekiz DEĞİL ON kilittir:** sekizi NEGATIVE'de, ikisi gövdede.

```
PHYSICS: <ortam ADI ve SAYISI — her promptta AYNI sayı>
AUDIO:   <ortamın ses yasası — dışarıda ne duyuluyor, ne duyulmuyor>
```

İkisinin ortam kartı başına hazır İngilizce karşılığı:
**`PROMPT_HATA_ONLEME_KILAVUZU.md` §2** (kopyala-yapıştır).

> ⚠️ Kural yokluğu değil ULAŞMAMA sorunu olduğu da ölçüldü: bu §5.1 çekirdeği
> 14.09.2026'da yazıldı, ama 15.09'da yazılan KRONOS_SON_SINYAL kapsamayı %41'de
> bıraktı (96 promptun hiçbirinde `AUDIO:` satırı yok) ve **🅑 oranı %93** çıktı.
> Aynı çekirdeği %80-91 kapsamayla taşıyan SUSMAYAN · FALLING_WORLD · BENI_HATIRLAMA
> %13-21 bandında kaldı.

## 5.2 SAHNEYE ÖZEL EKLER — en çok 3 cümle, IN FRAME satırına göre

> Prompt artık kadrajda olmayanı yazmaz (㉖ IN FRAME · D214). Ekler de öyle: yüz
> kadrajda değilse vizör cümlesi, sırt kadrajda değilse sırt cümlesi YOK.

| ek | ne zaman | nereye · cümle |
|---|---|---|
| **D79 vizör** | kasklı film · `IN FRAME: face` | POZİTİF gövde: *The visor is optically clear glass with zero tint, her face fully readable through it.* |
| **D79/D139 sırt** | `IN FRAME: back` ya da kamera arkada / OTS | POZİTİF gövde: *The back of the suit is one continuous smooth panel from collar to hip, a flat back silhouette carrying nothing.* (yokluk listesi arkadan çekimde tutmaz [D139]) |
| **diyalog** | sahnede replik varsa | POZİTİF (TIMELINE): konuşan ekrandaysa *lips match the words, mouth closed before and after* · ekran dışıysa *voice off-screen only, no mouth in frame*. NEGATIVE'e tek cümle: *No transcript of the line, no invented on-screen speaker.* |
| **sahne riski** | PLAN'ın Negative Bible'ından o sahneyi tetikleyen kilit (su · canlı · sıfır-g · ateş …) | NEGATIVE'e ≤3 cümle — havuz PLAN'da, seçim sahnede |

> D79'un DOSYA düzeyi kapısı değişmedi: kasklı filmde iki cümle dosyada en az bir
> kez bulunmalı — yüzün kadrajda olduğu prompt vizörü, sırtın kadrajda olduğu prompt
> sırtı taşır. Bütün promptlara ikisini de yazmak 14.09'dan sonra HATADIR (㉖ NOT).
> ⛔ Filmin vizörü tasarım gereği renkli/aynalıysa vizör cümlesi eklenmez ve
> PLAN'daki karşıt cümle silinir; ikisinin arası hata üretir.

## 5.3 TAM LİSTE — PLAN `### 🚫 Negative Bible` için (prompta GİRMEZ · 14.09.2026'dan önceki tam metin)

> Eski klasörler (00_HIKAYE_ONAYI.md yok) bu bloğu eskisi gibi her prompta yazmaya
> devam eder — sahip kararı, yeni kapılar yalnız yeni klasörlerde. Yeni klasörde bu
> blok PLAN'a bir kez yazılır; §5.2'nin "sahne riski" satırı buradan seçer.

```
Single unbroken take, no cuts, no edits, no camera resets, no transitions,
no dissolves, no fades, no jump cuts, no camera teleportation, no angle
change. Exactly one human character — no duplicates, no clones, no second
person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every
surface keeps visible texture. Photorealistic skin pores, sweat, scars and
fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed
skin, no face morphing, identical bone structure throughout. Equipment and
clothing identical to the description — no drift, no gear appearing or
disappearing mid-shot. Dirt and wear staining stays fixed and never shifts.
No readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — not on the suit, not on the equipment, and not
on the ground, the rock, the ice or any natural surface in the frame.
Nothing in this world has been measured, labelled, marked out or
annotated by anyone: no scale marks, no graduation ticks, no survey
markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue
text, no title card, no end card, no credits, no watermark. All hand-surface
contacts keep a clear structural boundary — no merging, no phasing, no extra
fingers, rigid-body collision throughout. All particles obey the stated
gravity with continuous physical momentum — never hovering, never frozen,
never swirling or flowing like liquid. Environment static and stable — no
melting terrain, no warping topology, no swimming texture. No Unreal Engine
look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm
film grain.
```

> ⛔ **METİN YASAĞININ KAPSAMI, YASAĞIN KENDİSİ KADAR ÖNEMLİDİR [Ders 138].**
> Depodaki filmlerin tamamı bu cümleyi KISALTARAK yazdı ve kısaltırken
> öznesini değiştirdi: *"The suit carries no patch, no flag, no lettering,
> no digits and no symbol anywhere."* O cümle KOSTÜMÜ korur; zemini, kayayı
> ve gökyüzünü korumaz. Bir filmde model kaldırımdaki halka çatlağın iç
> yayına **"11 metres" + gradasyon çentikleri** yazdı; prompt kapısı
> `no digits` kalıbını görüp geçirmişti (imza KELİMEYİ arıyordu, KAPSAMI
> değil) ve altı QA merceğinin altısı da görmedi. `prompt_kontrol.py`
> 28.08'de dosya başına tek satırlık bir **"metin yasağı KAPSAMSIZ"**
> denetimi aldı.
>
> ⛔ **VE ÖLÇÜ PROMPT GÖVDESİNDE DURMAZ [Ders 138].** Kadrajdaki bir yüzey
> işaretine (çatlak, halka, çizgi, oluk) bitişik yazılan ölçü — *"a curved
> fracture, eleven point six metres across"* — model tarafından o işaretin
> ÜSTÜNE basılan bir ETİKET olarak çizilebiliyor. Ölçü SPEC'in kilit
> listesinde yaşar; gövde nesneyi NESNE GÖRELİ ölçekle anlatır
> (*"about four body-lengths out from her on every side"*).

**Kaskı/skafandrı olan her filmde ayrıca [DERS 79 · 06.08.2026]** (eski rejim: her prompta; yeni rejim: §5.2 — IN FRAME'e göre, pozitif hâliyle)**:**

```
The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable,
no rear housing of any kind — her back silhouette is flat. The visor is
optically clear glass with zero tint, zero mirror coating and zero
reflection of the environment; her face is fully readable through it in
every frame, at every head angle.
```

> ⭐ 12.09.2026 · Bu bloğun KARARI (sırt kaymaz · vizör berrak) sabittir; sırtın
> POZİTİF cümlesinin "boş levha" yerine heykelsi ve kapalı yazılabilir hâli
> ile çekirdekteki "no CGI / no video game aesthetic" cümlesiyle ÇEKİŞMEYEN
> sert kabuk yazımı (mat · aşınmış kenar · tekstil eklem — üçü birden):
> `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` §5 · §8.
>
> ⚠️ Bu iki cümle Character Bible'da YETMİYOR. Unbroken City ve Starless
> Circle'ın bible'ları ikisini de açıkça yasaklıyordu ("No back-mounted
> tank, no hose, no cable" · "no tint, no coating") ve **iki filmde de
> sırt ünitesi + aynalı vizör üretildi** — model prompt gövdesini çiziyor,
> referans belgeyi okumuyor. Pozitif hâl ("flat back silhouette", "face
> fully readable") yasak cümlesinden daha iyi tutar (Ders 59).
> ⛔ **VE KAMERA ARKAYA GEÇEN SAHNEDE BU DA YETMEZ [Ders 139].** Yokluk
> kilidi, o yüzey kadrajın KONUSU olmadığı sürece çalışır. Bir filmde
> aynı blok altı promptun altısında gövdedeydi ve 6 sahnenin 5'inde
> tuttu; düştüğü tek sahne, kameranın kadının ARKASINA geçtiği tek
> sahnedir — orada altın renkli bir sırt ünitesi doğdu ve on saniye
> kaldı. Model boş bir sırtı DOLDURMAK zorundadır ve "no backpack"
> ona ne KOYACAĞINI söylemez. Kurulum azimutu özneyi arkadan ya da
> tepeden gösteriyorsa, o sahnenin promptunda yokluk listesi POZİTİF
> YÜZEY TARİFİNE çevrilir: *"the back of the suit is one continuous
> smooth panel from collar to hip, unbroken, carrying nothing"*.
> ⛔ Filmin vizörü tasarım gereği renkli/aynalıysa bu blok EKLENMEZ —
> o zaman da bible'daki karşıt cümle silinir; ikisinin arası hata üretir.

**Diyaloglu sahnelerde ayrıca** (yeni rejimde §5.2 diyalog satırı — tek negatif cümle)**:**

```
The spoken line is heard only — never shown as text. No subtitles, no
captions, no transcript. [Konuşan ekrandaysa:] her lip movements match the
words exactly, mouth closed before and after. [Ekran dışıysa:] the voice is
off-screen only — no mouth in frame, no invented on-screen speaker.
```

## 🆕 04.09.2026 · ZORUNLU BLOK ARİTMETİĞİ VE KONUM — TUR 11

> Kayıt: `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 11 · T11.4.
> ⛔ TUR 11'in raporu bu beş bloğun beşi için de "SİLİNEBİLİR" hükmü verdi
> ve hükümlerini "Ölçülmüş Etkisi" başlığı altında sundu. Hiçbiri için
> ablation yok — beş karar da ÖNERİ'dir. Deponun ölçtüğü bir ders dış
> benchmark'la silinmez. **Aşağıda hiçbir blok silinmiyor.**

```
① ARİTMETİK — ölçüldü, bu dosyanın kendi metni üzerinde
     §5 negatif çekirdek           1.650 karakter
     Ders 79 kask/vizör bloğu      +320
     ─────────────────────────────────────
     kasklı sahne kalıbı            1.970
     + diyalog bloğu (§5 sonu)      +288  →  2.258

   VIDEO bandı 2.000-2.600 (§7).
   → Kasklı ve diyaloglu bir sahnede, o sahneye ait TEK KELİME
     yazılmadan bandın 2.258'i dolmuş oluyor; bandın ÜST UCUNA
     342 karakter kalıyor. (TAVAN ayrı bir sayıdır — ~4.300, §7 ·
     `prompt_kontrol.py` TAVAN sabiti.) Depo bandı biliyordu, bandın ne kadarının KALIP
     olduğunu hiçbir yerde yazmıyordu.
   ⚠️ Bu bir silme gerekçesi değil, bir BÜTÇE uyarısıdır: sahneye
     ait metin bu kadar dar bir alana sığmıyorsa sorun sahnededir,
     çekirdekte değil.

② KONUM — depoda prompt İÇİ sıralama kuralı yoktu.
   Tek istisna `VEO_3_1_FAST…` §10'un "kamera ilk cümlede" satırıydı;
   hiçbir şablona genellenmemişti. Ölçüldü (04.09.2026 ANLIK GÖRÜNTÜSÜ ·
   depoya film klasörü eklendikçe kayar): depodaki 11.639 kod bloğunun
   200 karakterden uzun ve `NEGATIVE:` etiketi taşıyan 1.920'sinde
   etiket, bloğun ortalama %75,1 · medyan %74,4 konumunda başlıyor —
   yani zorunlu kilitlerin tamamı son çeyrekte duruyor.
   Sayımın kendisi tek satırdır ve yeniden koşulabilir: tüm `.md`
   dosyalarındaki ``` blokları, 200 karakterden uzun olanlarda
   `NEGATIVE:` etiketinin bloğa göre konumu.
   Difüzyon metin kodlayıcılarında erken konumun daha güçlü bağladığı
   yönü ölçülmüştür; SAYISAL eşik (raporun "ilk 50 token / 200 token
   sonrası" iddiası) ölçülmemiştir ve yazılmadı.
   → KURAL (nitel · ⚙️ SINANMAMIŞ): o sahnenin TUTMASI GEREKEN tek
     kilit, gövdenin İLK CÜMLESİNDE durur. Çekirdek kuyrukta
     kalabilir; sahneye özel kilit kuyrukta kalamaz.
   ⚠️ Bu kural bugün HİÇBİR ŞABLONA inmedi ve mevcut şablonla
     çarpışıyor: `IMAGE_VIDEO_PROMPT_TEMPLATES.md` VIDEO şablonu
     `MOTION (...)` + `0s — [başlangıç durumu]` ile, IMAGE şablonu
     `SCENE:` ile açılıyor. Şablona inmeden bu kural ölü doğar;
     kararı PROB D'ye bağlandı (`URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md`).

③ YASAK SİLİNMEZ — TAŞINIR.
   Olumsuzlamanın düzyazı gövdesinde zayıf olduğu ölçüldü
   (NegBench · CVPR 2025 "Vision-Language Models Do Not Understand
   Negation") ve depo bunu zaten kendi filminde ölçtü [D59 · D123].
   Ama bu "yasak işe yaramaz" demek DEĞİLDİR: ayrı negatif alan +
   CFG üretimde standarttır ve Veo'nun kendi kılavuzu negatif alana
   EMİR CÜMLESİ değil İSİM LİSTESİ yazmayı söylüyor — "no walls" ya
   da "don't show walls" değil, "wall, frame". Wan 2.1 kendi
   varsayılan negatif promptuyla geliyor ve o varsayılanın içinde
   字幕 (altyazı) terimi duruyor.                          [ÖLÇÜLMÜŞ]
   → Ayrı negatif alanı olan bir arayüzde çalışılıyorsa: yasaklar
     oraya İSİM olarak yazılır (text, subtitles, caption, watermark,
     bloom, glow).
   ⛔ DÜRÜST KAYIT: gövdede kalan hâli BUGÜN HÂLÂ BİR YASAK LİSTESİDİR
     — yukarıdaki 1.650 karakterlik çekirdekte 50 adet no/never/not/
     nothing/zero geçiyor. D59 uyarınca pozitif tarife çevrilmesi
     AÇIK İŞTİR; PROB C ile aynı kuyrukta durur.
   ⚠️ Deponun fiili hattı (Veo 3.1 Fast / Google Flow) tek gövde
     kullanıyorsa bu satır bir HAZIRLIKTIR, uygulama değil.

④ "35mm film grain" — DEPONUN HİÇ ÖLÇÜMÜ YOK.
   Çekirdeğin kapanış cümlesidir ve her prompta gidiyor. TUR 11
   raporu "zararlı, çürütüldü" dedi; o hükmün arkasında da ölçüm
   çıkmadı. Ama mekanizma sağlam ve doğrulandı: Wan/HunyuanVideo
   3D nedensel VAE 8× uzamsal, 4× zamansal sıkıştırma yapıyor ve
   yüksek frekanslı ince detay (tel, saç teli, metin çizgisi, gren)
   bu kodlamada kayboluyor — yani grenin titremeye dönüşmesi
   beklenebilir.                          [mekanizma ÖLÇÜLMÜŞ, etki DEĞİL]
   → Satır DURUYOR. Karar bir proba bağlandı:
     `URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md` · PROB C.
```

> ⭐ **14.09.2026 KAPANIŞ NOTU (reform FAZ 7).** Yukarıdaki dört maddenin ikisi
> kapandı, ikisi açık:
> ① ARİTMETİK — bütçe uyarısı yerine BÜTÇE geldi: çekirdek 1.650 → 886 karakter
>   (8 cümle, §5.1), bant karaktere değil POZİTİF gövde KELİMESİNE bağlandı (§7 ·
>   `prompt_kontrol.py` KELIME_BANDI), NEGATIVE ≤ 11 cümle (㉗). Kasklı ve
>   diyaloglu sahnede kalıp artık bandın dışında sayılır; sahne metnine bant tam kalır.
> ② KONUM — şablona indi: yeni iskelet promptun ilk satırını `IN FRAME:` yapar,
>   ikinci satır sahne numarası, ÜÇÜNCÜ satır o sahnenin tutması gereken TEK kilit
>   cümlesidir (`IMAGE_VIDEO_PROMPT_TEMPLATES.md` · `FILM_BOLUM_1.md`). Ölçüm yok;
>   kural hâlâ ⚙️ SINANMAMIŞ, ama artık "ölü doğmuş" değil.
> ③ pozitif tarife çevirme ve ④ "35mm film grain" AÇIK — PROB C/D aynen.
> Yalnız yeni rejim klasörlerinde (00_HIKAYE_ONAYI.md var); eski klasörler eski metinle.


---

# 6. 🏭 ÜRETİM AKIŞI

```
-1. FİKİR TURU   HIKAYE_FIKIR_TURU_KILAVUZU.md  ⭐ 21.09.2026 (yeni-film 0.7a)
                 → klasör açılmadan, hiçbir ders/kılavuz/QA okunmadan: gerilim
                   cümlesi → üç yöntem × 8-12 logline → beş evet/hayır eleme →
                   üç aday → A'ya karşı argüman → sahip onayı (beşinci soru:
                   ONAY · ADAY B · ADAY C · RED). Puan yok, soru eklenmez.
                 → Çıktı 00_HIKAYE_ONAYI (A + ADAYLAR) ve 02_KONSEPT §0⑥ + §5
                   ÖN-OTOPSİ'ye iner; aşağıdaki kapılar onaylı hikâyeyi
                   İYİLEŞTİRİR, üretmez.

0. RİSK OKUMASI  URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md
                 → PLAN YAZILMADAN önce: filmde su/canlı/kask/sayaç/diyalog
                   var mı? Her malzemenin geçmişte kaç filmde ne kadar
                   bozulduğu ve plana yazılacak SAYISAL kilit orada.
                 → 5+ risk çıkıyorsa KİLİT TAVANI (≤ 20 ders kilidi, 14.09.2026);
                   malzeme azaltılmaz, dışarıda kalan kilit PLAN'a gerekçeyle
                   yazılır (02_RISK_KARTLARI §RİSK TOPLAMI · prompt_kontrol ㉕).

0.5 KONSEPT KAPISI  ONERME_VE_NOVUM_KILAVUZU.md §4 — ÜÇ KAPI
                 ⛔ 26.08.2026'da AKIŞA ADIM OLARAK GİRDİ. Kapı 22.08'den
                   beri yazılıydı ama yalnız "her filmde okunacaklar"
                   listesinde duruyordu — okuma listesi kapı değildir ve
                   hiçbir konsept bu üç testten fiilen geçirilmedi.
                 → ① TEK KARE TESTİ: tek donmuş karede izleyici anomaliyi
                      1 saniyede işaret edebiliyor mu
                   ② KİNETİK BAĞIMSIZLIK: kural yalnız 8-10 s'lik sabit
                      planlardaki EYLEMLE kanıtlanabiliyor mu (replik,
                      dış ses, ekran metni olmadan)
                   ③ BAŞLIK ŞEMASI: önerme ≤5 kelimelik başlığa çevrilip
                      izleyiciye nereye bakacağını söylüyor mu
                 → Üçü de ✅ değilse KONSEPT REDDEDİLİR, plan yazılmaz.
                   Kapı ③ paketlemede ikinci kez koşar (PAKETLEME §1).

1. PLAN          → `<FILM>_PLAN.md`  (klasör iskeleti: §2.0)
                 konsept, tema, farklılaşma gerekçesi, sahne haritası
                 → tema yoksa DURMA, film koreografi olur — tema seçimi,
                   format-süre uyumu, tema→motif→sahne matrisi:
                   TEMA_MUHENDISLIGI_KILAVUZU.md (22.08.2026)
                 → sahne haritasından ÖNCE vuruş tablosu doldurulur:
                   SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md §2 — boş vuruş
                   "bilinçli sapma" notu ister; açılış-kapanış imajı
                   ÇİFT olarak tasarlanır, loop satırı yazılır (shorts)
                 → vuruş tablosundan SONRA hook mimarisi:
                   HOOK_VE_ILK_SAHNE_KILAVUZU.md §8 (7 madde) —
                   HOOK TİPİ + S0 soru cümlesi + S1 ikinci bilgi +
                   ilk 2 sn ses kararı plana yazılır
                 → sahne haritasının KAMERA SATIRLARI üç kılavuzdan:
                   vuruş→açı: KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md ·
                   diziliş bandı + yay: ACI_YAYI_VE_SEKANS_KILAVUZU.md
                   (🆕 KURULUM İSKELETİ satırı PLAN'a — küme ≥2 ·
                    dönüş ≥%40 · birebir kopya; 12+ sahne) ·
                   🆕 22.09.2026 yatay: SAHNE PLANI satırı + sahne başına kapsama
                    şablonu (COK_KLIPLI_SAHNE_KILAVUZU §1-§2) — küme YOK ·
                   hazır kalıp / kapak anı: MESHUR_SAHNE_KALIPLARI_KILAVUZU.md

2. BIBLE         world / character / ortam / tür / negatif
                 → karakter bloğu KELİMESİ KELİMESİNE sabitlenir

2.5 PLAN KONTROL URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md
                 → 18 madde, ~20 dk, maliyet sıfır. 12'si gerçek filmlerde
                   gerçekten oldu ve hepsi üretimden SONRA bulundu.
                 → ⭐ 14.09.2026: A0 HİKÂYE ONAYI her şeyden önce —
                   00_HIKAYE_ONAYI.md ONAY tarihli mi (yeni-film adım 0.7 · ㉙)
                 → En kritik ikisi: (A1) "no text" yasağı ile ekran içeriği
                   aynı dosyada mı — model yasağı seçer, anlatım ölür.
                   (B1) filmin doruğu bir sahnenin İÇİNDE mi, yoksa iki
                   sahnenin arasına mı düşüyor.
                 ⭐ 26.08.2026'da iki madde eklendi (12 → 14):
                   (B3) tema hangi SAHNELERDE motife dönüşüyor — sahne
                        numarası yazılı mı (Kaleida Crash kaydı:
                        "bedel yok → tema dekoratif kalıyor")
                   (B4) sahne-kurulum dizisi + güvenli bant + kurulum
                        sayısı + AÇI TİPİ sayısı (≥3) yazılı mı

3. PROMPT        → `<FILM>_BOLUM_1.md` · `<FILM>_BOLUM_2.md`  (§2.0)
                 image + video, self-contained
                 → ⭐ 14.09.2026 yeni rejim (00_HIKAYE_ONAYI.md olan klasör):
                   POZİTİF gövde KELİME bandı image 100-250 · video 120-300
                   (`prompt_kontrol.py` KELIME_BANDI · üstü BLOCK) + NEGATIVE
                   8 çekirdek + ≤3 cümle (§5) + ilk satır `IN FRAME:` (㉖);
                   eski klasörde ~2.500 karakter bandı (§7)
                 → [BIBLE] atfı YASAK, her prompt tek başına çalışmalı —
                   ama self-contained ≠ Bible'ın tamamı: yalnız KADRAJDAKİ
                   yazılır (AGENTS §2 kural ③ · D214)
                 → bölüm SINIRI da ardışık bir çifttir: son sahne ↔ ilk sahne
                   ≥1 ölçek kademesi VE ≥45°

3.5 PROMPT QA    PROMPT_KONTROL/   ✅ 12.08.2026'da açıldı
                 → ÜRETİMDEN ÖNCE çalışır, maliyeti sıfır
                 → İKİ ADIM, ikisi de gerekir:
                   ① python3 .../PROMPT_KONTROL/prompt_kontrol.py <FİLM KLASÖRÜ>
                      ⛔ KLASÖR verilir, tek bölüm değil (01.09.2026 klasör
                        modu — §2.0). Çıktıda `📁 FİLM KLASÖRÜ · n bölüm
                        dosyası birleşik` satırı yoksa dizi kapıları koşmadı.
                      sayar: uzunluk · yasak kelime · çekirdek imzası ·
                      "Scene N of X" tutarlılığı · yön kapısı ·
                      ⭐ kurulum çeşitliliği · açı sözlüğü · abartı eşiği ·
                      TEMA satırı + sahne indeksi (26.08.2026).
                      Çıkış kodu 2 = BLOCK.
                   ② PROMPT_QA_CRITIQUE_PROMPT.md
                      yargılar: kilit SAYI mı TARİF mi, sahne hangi dersi
                      tetikliyor, A1 çelişkisi anlam düzeyinde var mı
                 → tarif kilitlerini SAYIYA çevirtir (kanıtlı tek mekanizma)
                 → GO / FIX / BLOCK döner. BLOCK ise üretme.
                 ⚠️ Betik ilk koşusunda (69 dosya) Low Power'ın eşik üstü
                    5 promptunu ve Kaleida Crash'in sahne sayısı hatasını
                    bağımsız buldu — ikisi de belgelenmiş vakalar.

4. REFERANS      7-9 dk formatında BU ADIM 2'DEN SONRA GELİR
                 (diğerlerinde bu aşama yok)

5. ÜRETİM        önce imaj, onaylanınca video
                 → onaylanmamış imajdan video üretme, boşa gider

5.5 KURGU        KURGU_VE_TESLIM_KILAVUZU.md   🆕 21.08.2026
                 → birim sözlüğü (SAHNE ≠ ÇEKİM ≠ KLİP) + 10 maddelik
                   kurgu kapısı + kırpma bütçesi + tek grade/gren
                 → kapıyı geçmeyen filme koşulan QA ÖN KOŞU sayılır [D109]

5.7 QA PAKETİ    ⛔ QA'DAN ÖNCE, iki betik  🆕 01.09.2026
                 ① bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>
                   süre · ızgara · ses kanalı · köşe · KUYRUK KART (freezedetect)
                   · son kare        [⑪ · D125 · D136 · D150 · D70/72]
                 ② bash .claude/skills/qa-isle/scripts/sahne_kapisi.sh <master> 10 <prompt_sayısı>
                   ızgara · sahne sahne kesme/donma/gölge · TESLİM KAPISI [D188]
                   → ⑬ UYUM merceğinin makine yarısı; 🚨 uyuşmazlıkta mercek koşulmaz
                 ③ ⛔ PAKET BETİĞİ KALDIRILDI (11.09.2026): `rubrik_paketle.sh`
                   ve `QA_PROMPTLARI/FILME_OZEL/` silindi. Operatör
                   `QA_PROMPTLARI/_KAYNAK/<n>_*.md` rubriğini açar ve
                   `<FILM>_QA_SPEC.md`'yi rubriğin BAŞINA yapıştırır [D129].
                   Mod D'nin tek koşulu budur; yapıştırılmazsa koşu mod V.

6. ① KARE QA     1_KARE_QA_CRITIQUE_PROMPT.md
                 → künye bloğunu DOLDUR, yoksa rapor UNVERIFIABLE döner
                 → ⛔ STEP 0: künyeyi PROMPT DOSYASINDAN kopyala ve doğrula.
                   Uyuşmazsa rapor puanlanmadan durur.

7. ④ HİKAYE QA   4_HIKAYE_QA_CRITIQUE_PROMPT.md
                 → teknik 9/10 olup dramatik olarak ölü olabilir
                 → PLAN verilirse MOD D (sahne sayısı · süre · diyalog plana
                   karşı doğrulanır); plansız MOD V, satır Ⓥ ⚠️ ŞARTLI.
                   Skor satırı FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md'ye yazılır.

7b. ② DEVAMLILIK 2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md
                 → film VE içindeki insan kendisiyle çelişiyor mu (13 kat.:
                   gövde 1-6 kimlik/kostüm/yıpranma/ekipman, dünya 7-13)
                 → ⛔ TERSİ KURAL: bu rubriğe DOKÜMAN VERİLMEZ, yalnız video.
                   Baseline = kendi içinde tutarlılık. Skor satırı
                   FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md'ye yazılır.
                 → ⭐ Rapor gelince FLAGS FOR DOCUMENT CHECK sorularını plan
                   dosyasından cevapla. Rubriğin ikinci yarısı bu adımdır.
                   Şimdiye kadarki en değerli bulgular oradan çıktı.

7c. ③ SES QA     3_SES_QA_CRITIQUE_PROMPT.md
                 → filmde replik veya ses tasarımı varsa koşulur:
                   doğru karakter mi konuşuyor · sentetik ses damgaları ·
                   ses kimliği kayması · ortam sesi kesmede ölüyor mu · miks
                 → ⛔ TERSİ KURAL: doküman VERİLMEZ, yalnız video.
                 → ⛔ TEK KLİBE KOŞULMAZ — TAM KURGU verilir. Ölçtüğü şeyin
                   çoğu kesmelerin ARASINDA yaşar; tek klip koşusu geçersiz.
                 → ⭐ Rapor gelince ÖNCE REGISTER doğrula: bu seri diegetik
                   yapay ses kullanıyor (suit AI, telsiz, kayıt). MACHINE
                   olması gereken bir repliğe "sentetik duruyor" bulgusu
                   yazıldıysa bulgu DÜŞER — tasarımı cezalandırmak olur.
                 → Skor satırı FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md
                   (09.08'de açıldı). Görev kartı: AGENTS.md kart E3.
                 → İlk koşu (Cold Burn): ATIF tuttu (9), YATAK tutmadı (3)
                   — bulguların çoğu miks seansı, yeniden üretim değil.

7d. RAPOR KONTROL RAPOR_KONTROL/rapor_kontrol.py  🆕 01.09.2026
                 → HER rapor işlenmeden önce, elle değil betikle:
                   n·Σ·ort yeniden hesap · tally · şerit · ⑨ ızgara ·
                   ④ harita↔kesme · ② sayaç boşluğu · çoklu raporda ⑤
                   (kesme · sahne · şerit · replik · SUSKUNLUK)
                 → GEÇERSİZ / TEKRAR → T tablosuna satır YAZILMAZ [D161 · D162]
                 → İlk koşu (01.09.2026): iki partinin on iki raporundan
                   dokuzu düştü — üçü fabrike/yuvarlama, altısı mod V.

8. YENİ DERS     QA yeni hata bulduysa DERSLER/ tematik dosyasına ekle
                 → ⛔ KAPI satırı olmayan ders YAZILMAZ — dört kader (BETİK ·
                   LİSTE · KARAR · ARŞİV): DERSLER/00_DERS_YAZIM_KONTRATI.md
                   (01.09.2026). Kapısız aday → DERSLER/GOZLEM_DEFTERI.md
                 + LESSONS_LEARNED.md dizin tablosuna satır (AGENTS.md kart G)
                 → DERSLER/00_HIZLI_REFERANS.md kilit havuzunu ve ilgili QA rubriğini
                   güncelle (iz: QA_PROMPTLARI/CALISTIRMA_KAYITLARI.md)
                 → Ders 46-50 hepsi MANTIK QA'dan çıktı ve hiçbiri prompt
                   cümlesiyle çözülmüyor: kurguda, planda veya sahne
                   haritasında çözülüyor (bkz. DERSLER/07_KURGU_VE_ANLATI.md)

9. MÜZİK         → `<FILM>_MUZIK.md`
                 GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md §7-19
                 → ÖNCE §17 künyesi: "izleyici bu novum'u ___ olarak
                   okumalı" cümlesi yazılmadan müzik promptu yazılmaz
                 → tempo sahne uzunluğuna hizalanır (§14: 10s sahne →
                   48/72/96/120/144 BPM), sub-bass'a 90-160 Hz oktav
                   eşlikçisi eklenir (§15.1 — telefon hoparlörü)
                 → her filmde EN AZ BİR müziksiz sahne seçilir (§10)

10. KAPAK        → `<FILM>_KAPAK.md`
                 FILM_KAPAGI_KILAVUZU.md (20.09.2026 · eski KAPAK_FOTOGRAFI kanıt)
                 → İKİ aday (A·B) + TEK DENEY SORUSU; an PLAN'dan (vuruş · İPTAL KAPISI)
                 → metinsiz üret, film adı post katmanı; Bible cümleleri birebir
                 → elle 160×90 (≈120 px) + 320×180 sınavı: TEK ilişki okunuyor mu
                   okunmuyorsa geri kalan hiçbir şey kapağı kurtarmaz
                 → A + B aynı başlıkla Studio A/B'ye (Kart Y) · sayılar DIS_SAYILAR §1
                   (KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç
                    çalıştırılmamıştı; test manuel yapılır)

11. PAKETLEME    → `<FILM>_YAYIN_PAKETI.md`  ⭐ TAMAMEN İNGİLİZCE
                 VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md (kural) +
                 apexaic/<platform>/PAKETLEME_SABLONU.md (kanalın doldurulmuş
                 hâli: sabit bloklar · hashtag kademeleri · yükleme listesi) +
                 apexaic/CAPRAZ_YAYIN.md §7 (çapraz kontrol)
                 ⛔ Sabit blok per-film dosyaya KOPYALANMAZ, oradan
                   birebir yapıştırılır — ikinci kopya ikinci sürümdür
                 → YouTube + Shorts + Instagram + TikTok ayrı ayrı —
                   üç platforma aynı metin yazıldıysa iş yapılmamıştır
                 → ⛔ DİL: kanal §3.3 kararı "her şey İngilizce". Türkçe
                   yazılıp yükleme anında çevrileceği varsayılan paket
                   çevrilmiyor: 01.09.2026 taramasında dikey hattın her
                   filminin başlık paketi TÜRKÇE yazılmıştı, oysa kanaldaki
                   başlıkların hepsi İngilizce (apexaic §1). Yani o paketler
                   yükleme anında yeniden yazılıyor — ve yeniden yazan şey
                   kılavuzu okumuyor.
                 → ⬜ AFTER THE CUT alanları (RUNTIME · paylaşılabilir an ·
                   dikey kesit) yazımda BOŞ bırakılır, uydurulmaz
                 → ⭐ seri/evren kararı ve başlık mimarisi:
                   SERI_VE_KANAL_STRATEJI_KILAVUZU.md §3 (bölüm numarası
                   başlığın BAŞINA yazılmaz · kapak aile kimliği)

12. İHRAÇ        KURGU_RITMI_VE_IHRAC_KILAVUZU.md §6   🆕 22.08.2026
                 → 1440p+ · BT.709 · 48 kHz · −14 LUFS · −1,0 dBTP
                 → sesi DÜŞÜK teslim etmek en pahalı hata: platform
                   yüksek sesi kısar, düşük sesi YÜKSELTMEZ

13. YAYIN        YAYIN_VE_PERFORMANS_KILAVUZU.md       🆕 22.08.2026
                 → ⛔ satır yayından ÖNCE açılır:
                   FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md
                 → ilk 48 saatte TEK değişken oynatılır (kapak VEYA başlık)
                 → 24/48/72 saat ölçümü · retention eğrisi SAHNEYE çevrilir
                 → ⭐ AKIŞ BURADA KAPANIR: gerçek veri hangi kılavuzu
                   yanlışlıyorsa o kılavuz revize edilir (§6 geri besleme).
                   Bu adım koşulmadan depodaki hiçbir viral hipotez
                   test edilmiş sayılmaz.
```

---

# 7. ⚠️ BİLİNEN TUZAKLAR

> Bu bölüm hiçbir kılavuzda yok — üretim denemelerinden çıktı.
> Rehberin en pahalı bilgisi burada.
> ⚠️ 04.09.2026 istisnası: bölümün İLK bloğu (DEĞİŞEN NİTELİK) bir DIŞ
> ölçümdür ve deponun kliplerinde koşulmadı; gerisi üretim denemesidir.
>
> ⭐ **01.09.2026 — POLİTİKA TARAFI AYRI DOSYAYA TAŞINDI.**
> Aşağıdaki `HATA MESAJLARI AYRIMI` · `YASAK LİSTESİ TUZAĞI` · `YAPISAL RED`
> blokları **kaynak** olarak burada durur; işleyen hâli, sözlüğü,
> kompozisyon ekseni ve kurtarma merdiveni artık tek yerde:
> **`POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`**
> Red SAYILARI hiçbirinde değil, tek defterde:
> **`FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md`** (14 vaka).
> Kelime ekseni artık bir KAPIDIR: `prompt_kontrol.py ⑯`.

## 🆕 04.09.2026 · DEĞİŞEN NİTELİK — ölçülmüş en zayıf eksen

> Kayıt: `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 11 · T11.4.
> Bu, TUR 11'in depoya inen en geniş kapsamlı tek satırıdır: her formatı,
> her ortamı ve her türü kesiyor.

```
T2V-CompBench (CVPR 2025) yedi ekseni ölçtü. Modellerin EN KÖTÜ olduğu
eksen sayısal kesinlik değil — DYNAMIC ATTRIBUTE BINDING: bir niteliğin
klip İÇİNDE durum değiştirmesi. En iyi modelin skoru 0,0687.
(Karşılaştırma: aynı süitte sayısal kesinliğin en iyisi 0,607 — on kat.)
                                                          [ÖLÇÜLMÜŞ]

⛔ TEK KLİBE DURUM DEĞİŞİMİ YAZILMAZ — model başlangıç ya da bitiş
   durumunu donduruyor, ikisini birden donduruyor, ya da arada
   morfoloji bozuyor.

⭐ İŞLEYEN KURAL TEK YERDE: yazılmaz listesi, hareket ↔ durum değişimi
   ayrımı ve değişimin sınıra taşınması —
   `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` §1.
   Burada yalnız SAYI, MEKANİZMA ve deponun üç arızası durur.

⭐ VE BU, DEPONUN ÜÇ ÖLÇÜLMÜŞ ARIZASINI AYNI ANDA AÇIKLIYOR:
   D143 toz şelalesi · D148 bacağın alevden geçmesi · D95 vizörün
   görünmez olması — üçü de klip içinde bir niteliğin değişmesini
   ya da iki durumun aynı anda tutulmasını istiyordu.
   ⚠️ Bu bir AÇIKLAMA, doğrulama değil: benchmark deponun kliplerinde
     koşulmadı. Etiket ÖLÇÜLMÜŞ (dış), uygulama SINANMAMIŞ (iç).
```

```
PROMPT UZUNLUĞU
  ⛔ TEK KAYNAK `prompt_kontrol.py` başındaki sabitlerdir (BANT · TAVAN ·
     KELIME_BANDI · NEGATIF_CUMLE_TAVANI); buradaki sayılar o sabitlerin
     kopyasıdır, bir sayı değişirse önce betikte değişir.
  ⭐ 14.09.2026 YENİ REJİM (klasörde 00_ANALIZ/00_HIKAYE_ONAYI.md varsa) —
     bant KARAKTER değil KELİME, ve yalnız POZİTİF gövde (NEGATIVE: öncesi):
       IMAGE 100-250 kelime · VIDEO 120-300 kelime → üstü BLOCK, altı NOT
       NEGATIVE ≤ 11 cümle (8 çekirdek + ≤3 · §5) → üstü FIX (㉗)
       toplam karakter tavanı 4.300 aynen (BLOCK)
     Gerekçe: LOCKED_PULSE image ort. 719 kelime, %57'si tekrar; tarif kilidi
     %0 tuttu. Kelime sayan bant kalıbı değil SAHNEYİ ölçer.
  ─── eski rejim (14.09'dan önce açılan klasörler) ───────────────────
  ~4.300 karakter → Veo hata veriyor (Low Power S5, S11 doğrulandı)
  ~2.500 karakter → sorunsuz
  → VIDEO hedef bandı: 2.000-2.600 (tavan ~4.300 yalnız video için ölçüldü)
  → IMAGE bandı ÖLÇÜLMEDİ (21.08.2026 düzeltmesi): eski "1.700-2.100"
    bandı depodaki hiçbir filmle uyuşmuyordu — Holding Field 3.417-4.017 ·
    Third Dune 2.732-4.154 · Quiet Impact 4.577-5.644, üçü de üretildi/
    reddedilmedi. Image uzunluğu bulgu değil GÖZLEMDİR; prompt_kontrol.py
    de böyle davranır (kaynak: betiğin başlık yorumu).
  ⚠️ 10-11.08.2026 · THIRD DUNE ilk üretim turu — BEŞ RED, beşi de
     eşiğin altında: S1 3.842 · S7 3.917 · S5 3.155 · S9 4.065 ·
     S12 4.288 karakter. Dördü "I encountered an error", biri "I seem
     to be encountering an error" (beşi de aşağıdaki tabloda
     teknik/geçici sınıfında). Aynı turda GEÇEN prompt sayısı: 0.
     ⛔ Bir filmde arka arkaya red gelip HİÇ geçen prompt yoksa, sayı
        artık promptu değil ÜRETİM TARAFINI işaret eder. Altıncı
        yeniden yazımdan önce probu çalıştır (aşağıda, adım 4).
     → Eşiğe değil BANDA yaz. Eşik "burada kesin patlar" demek,
       "buraya kadar güvenli" demek değil.
     ⚠️ AMA uzunluk tek başına açıklamıyor: en kısa olan (3.155) da
        battı ve bu filmden bugüne kadar GEÇEN prompt yok. Aynı filmin
        üç promptu üst üste battığında promptu kısaltmadan ÖNCE
        aşağıdaki 3 satırlık probu çalıştır (adım 4) — sorun oturum
        tarafındaysa hiçbir yeniden yazım işe yaramaz.

PROMPTTA YAZILMAYACAKLAR
  ✗ Karakter özel adı  → jenerik/başlık kartı halüsinasyonu [D34]
  ✗ Milliyet ifadesi   → üretim reddi ("Israeli-American" doğrulandı)
  ✗ Gerçek ülke ordusu/polisi sembolü, bayrak, rütbe
  ✗ "cinematic lighting" → mumsu cilt ve bloom [D33]
  ✗ "swirl" → toz sıvı gibi akıyor [D39]
  ✗ "glowing / ethereal / radiant / shimmering" → bloom [D29]
  ✗ "seamless visor" / "bubble" / "dome"  → kask geometrisi serbest, kubbe [D146]
  ✗ "legs folding" (kalkış klibinde)      → bacak alevin içinden geçer [D148]
  ✗ sayısız "new dust entering from above" → toz şelalesi [D143]

TOZ ŞELALESİ — POZİTİF CÜMLE SAYISIZSA PERDE OLUR  [Ders 143 · Skylight S3/S6/S13, 29.08.2026]
  "fine dust drifts steadily down … new dust entering from above" → 60 m'lik ışın
  beyaz toz/duman perdesi oldu, kıvrıldı; çekirdeğin "never swirling" yasağı
  pozitif cümleye yenildi (D59'un bilinen yüzü).
  → Zerre SAYISI + hız yazılır: "no more than a few dozen motes visible … each a
    separate point … falling at about half a metre per second … the far wall
    stays visible through it". Kapı ②: zerreler tek tek sayılamıyorsa RET.

ALÇAK AÇI = BOŞ ÜST ALAN = MODEL DOLDURUR  [Ders 145 · Skylight S26, 29.08.2026]
  Düz ovadaki gemi, alçak açılı klipte iki yanı dik kanyon duvarıyla çıktı; göz
  hizası kadrajlar (S25 · S28) ovayı korudu — ufku içeriyorlardı.
  → HORIZON LOCK + "above the ship there is only sky" + en büyük arka plan
    nesnesi PROMPTA yazılır (⑤ merceğinin kuralı prompt tarafına taşındı).

FİLİGRAN — RUBRİK DEĞİŞİM ARAR, FİLİGRAN DEĞİŞMEZ  [Ders 150 · Skylight, 315/315 s]
  Üretici ikonu her karede duruyordu; altı mercek görmedi (⑤ "EDGES: Clean" ×31).
  → ⑪ köşe testi (olcum_kapisi.sh) TESLİMDEN ÖNCE; filigranlı master master değildir.

IŞIK MIKNATISI — YÖN TERSLENMESİ  [Ders 104 · Black Cradle S4, 16.08.2026]
  Kadrajda TEK BASKIN ışık kaynağı varken (şafak, patlama, projektör)
  model hareketli özneyi ona DÖNDÜRÜYOR — hedef-dilim + yön cümlesi
  yazılıyken bile (astronotlar landera değil şafağa koştu; prompt
  uzamsal kılavuz §6.1'e uygundu ve betik kapısından geçmişti).
  → Panzehir DÖRT KANAL birden: hedef-dilim+yön · omuz hattı ·
    IŞIĞA GÖRE POZ ("their backs are to the light — it rims their
    back silhouettes") · yön negatifi ("no one runs toward the
    light, no direction reversal"). Ders 104'te tam metin.
  ⚠️ Araç sahnesinde aynı tuzağın karşılığı "hangi uç önde"dir:
    kıç önde yanaşan araca "never nose-first — the canopy end never
    faces the ship" negatifi yazılmadan model burnu çevirir.
  ⚠️ Betik bunu GÖREMEZ: yön kapısı konum+hareketi arar, yönelimi
    aramaz. Denetim insan gözüyle.
  ⚠️ İKİNCİ VAKA (aynı sahne, aynı gün): dört kanal da yanal koşuda
    yetmedi — model hedefi arkaya atıp koşucuları KAMERAYA döndürdü.
    KAÇIŞ BASAMAĞI: iki yenilgiden sonra üçüncü yeniden yazım yok;
    kamera HEDEFE taşınır, hareket kameraya doğru kurulur (nötr
    çekim §6.3) — frontal refleks doğru cevaba dönüşür. Ders 104.
  ✅ 17.08.2026: V3 (kamera hedefte) İLK denemede GEÇTİ. Tam mekanizma
    ve şablonlar artık UZAMSAL kılavuzda: Sürüm 3 · §6.7 (ışık
    mıknatısı, dört kanal) · §6.8 (iki yenilgi kuralı + kompozisyon
    şablonu) · §10.1 yeni denetim maddeleri.

KOPYALAMA
  ✓ SADECE kod bloğunun içini kopyala
  ✗ Türkçe başlık ekleme
  ✗ İki promptu birleştirme  → politika reddi aldı, doğrulandı
  ✗ Yarım kalmış/bozuk yapıştırma → reddin gerçek sebebi bu olabilir

KURGU / TESLİM  → TEK KAYNAK: KURGU_VE_TESLIM_KILAVUZU.md (21.08.2026'da
  bu bloktan + DERSLER/07'den + TEK_CEKIM §8'den konsolide edildi)
  Çekirdek gerçekler (ayrıntı ve 10 maddelik kapı orada):
  ✗ Kapak/başlık kartı klip zincirine KARIŞMAZ — yazılı yasak 6 vakada
    tutmadı (Unbroken City 2:40 · Banded Deep 3:00 ...); tek çözüm
    teslim öncesi KURGU KAPISI [D70/72]
  ✗ Kapı ÜÇ BİRİM sayar: klip = CLIP COUNT · çekim = SHOT COUNT · sahne
    = SCENE COUNT [D101 · Last Shift: "14=14" ✅ verdi, 27 klibin ~17'si
    ekrandaydı] — süre tek başına ALDATIR [D100]
  ✗ Değişken çekim süresi = KIRPMA BÜTÇESİ zorunlu: RAW FOOTAGE +
    TRIM BUDGET satırları; yoksa kurgu kırpmaz, KLİP DÜŞÜRÜR [D100]

HATA MESAJLARI AYRIMI
  ⛔ 01.09.2026 [TUR 3] · AŞAĞIDAKİ "TEKNİK" ETİKETLERİ TEK BAŞINA YETMİYOR.
     Ayırt edici soru MESAJ DEĞİL, DAVRANIŞ: üretim GÖRÜNÜR ŞEKİLDE
     ilerleyip sonda mı düştü? İlerlediyse bu MASKELİ ÇIKTI REDDİDİR
     (görüntü üretildi ve silindi) — tekrar denemek işe yaramaz.
     Tam ağaç: ../POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md §1 · §1.0②
  "I can't generate that video"        → POLİTİKA reddi (içerik/ifade)
  "Sorry, something went wrong"        → TEKNİK/geçici VEYA maskeli
                                         ÇIKTI reddi (yukarıdaki soruyla ayır)
  "I encountered an error"             → TEKNİK/geçici (aynı soru)
  "I seem to be encountering an error. Can I try something else
   for you?"                           → TEKNİK/geçici (Starless
                                         Circle S12, 06.08.2026)
                                         ⚠️ 12.08.2026 · RING LIGHT S2:
                                         aynı mesaj, prompt 2.565
                                         karakterle bandın İÇİNDE.
                                         Uzunluk elenince geriye tek
                                         profil kalıyor → aşağıdaki
                                         YAPISAL RED tetikleyicisi.
                                         Bu mesaj "geçici" sınıfında
                                         olsa da, insansız + uzun
                                         NEGATIVE profiline uyan
                                         sahnede İKİNCİ redde
                                         yapısal muamele gör.
                                         ⛔ AYNI GÜN 3 RED / 0 BAŞARI:
                                         S2-A (2.565), yapısal red çözümü
                                         uygulanmış S2-B (2.492) ve
                                         S4-A (2.600) — üçü de aynı mesaj.
                                         Elendi: uzunluk bant içinde ·
                                         yapı düzeltilmiş · iki ayrı
                                         sahne, tek mesaj. Kalan tek aday
                                         üretim tarafı → adım 4 probu
                                         ÜÇÜNCÜ yeniden yazımı beklemeden
                                         koşulur. Third Dune deseni
                                         (5 red / 0 başarı) ikinci kez
                                         görüldü: SIFIR BAŞARI varken
                                         prompt kısaltmak boşa emektir.
  "I'm having a hard time fulfilling your request. Can I help you
   with something else instead?"       → YAPISAL red — tekrar
                                         denemek İŞE YARAMAZ
                                         (Cold Burn S8, 07.08.2026)
  "I can't make videos of real people in situations like that."
                                       → POLİTİKA reddi · KELİME
                                         sınıflandırıcısı (Last Span
                                         S8, 25.08.2026)
  "I can't make videos that could relate to dangerous situations."
                                       → POLİTİKA reddi · KELİME
                                         sınıflandırıcısı (Last Span
                                         S9, aynı gün)
                                         ⛔ İKİSİ DE aşağıdaki
                                         YASAK LİSTESİ TUZAĞI'na bak:
                                         tekrar denemek işe yaramaz,
                                         prompt KISALTMAK da işe
                                         yaramaz — çözüm SÖZLÜK

YASAK LİSTESİ TUZAĞI — negatif blok politika reddi ÜRETİYOR 🆕 25.08.2026
  ⭐ TAM İŞLEYİŞ + SÖZLÜK: ../POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md §2
  Ne demek: `NEGATIVE:` bloğuna yazılan yasak, yasakladığı kavramı
  PROMPTUN İÇİNE SOKAR. Politika sınıflandırıcısı "no" önekini değil
  KELİMEYİ okur. Filmde hiç olmayan bir şiddet, onu yasaklayan cümle
  yüzünden prompta girer.
  Vaka (THE LAST SPAN, 25.08.2026): film 0 kare gore taşıyor —
  tasarımı gereği yara/kan/ceset/temas SIFIR. Prompt dosyası ise
  "gore" 29 · "blood" 26 · "wounds" 26 · "corpse" 18 kez yazıyordu,
  hepsi yasak olarak. İki sahne reddedildi, ikisi de aksiyon doruğu.
  ⛔ TEŞHİS SIRASI — bu üçü sırayla elenmeden prompt kısaltma:
   1. Reddedilen promptta yasakladığın için YAZDIĞIN bir şiddet/
      tehlike kelimesi var mı? (gore · blood · wound · corpse ·
      injury · jump scare · horror · weapon · victim)
      → varsa sebep BU. Kısaltmak işe yaramaz; SİL.
   2. İnsan kütlesini nasıl adlandırıyorsun? "crowd of figures" +
      kaçan/kovalanan bir insan = model için KİTLESEL KAZA.
      → filmin tasarımı zaten heykel gibiyse ÖYLE adlandır
   3. Fiil şiddetli mi? "hurls X into the chest" · "strikes his head"
      → aynı fiziği taşıyan nötr hâl var mı ("at hip height",
        "against the base")
  ⛔ ÇÖZÜM YASAK DEĞİL TARİFTİR [Ders 59'un politika tarafı]:
      yasak:  "no visible faces, no eyes, no open mouths, no teeth"
      tarif:  "the head is a smooth dust shell with no readable
               features, like a plaster cast left standing in the open"
      İkincisi hem sınıflandırıcıyı tetiklemez hem DAHA İYİ çalışır:
      yasak yüzü yasaklar, tarif yüzü ORTADAN KALDIRIR.
  ✅ 01.09.2026 DÜZELTMESİ — bu satır artık YALNIZ YARISI DOĞRU.
     Eski hâli: "prompt_kontrol.py bunu göremez ve göremez de."
     KELİME ekseni için YANLIŞTI ve bedeli ölçüldü: LAST SPAN'in
     dosyasında "gore" 29 kez geçiyordu — bir SAYIM bunu üretimden
     önce yakalar. Kapı açıldı: `prompt_kontrol.py ⑯ POLİTİKA SÖZLÜĞÜ`
     (T1/T2 sayımı · NEGATIVE bloğu DÂHİL · şiddet fiili · milliyet).
     Açılış ölçümü: 140 kaydın 60'ında politika sözcüğü var.
     KOMPOZİSYON ekseni için hâlâ DOĞRU (YERCEKIMI S8: kelimeler
     temizdi, kadraj reddedildi) — o eksenin kapısı insan gözüdür:
     PROMPT_QA_CRITIQUE_PROMPT.md · POLİTİKA §3.
  ⚠️ Sınıflandırıcı promptu BÜTÜN olarak okur: tek tek masum üç
     cümle (kalabalık + koşan insan + devrilen gövdeler) birlikte
     bir felaket sahnesi tarif eder. Reddi tek kelimede arama.

YAPISAL RED — "having a hard time fulfilling your request"
  Ne demek: içerik politikası değil, istem sınıflandırıcısı promptu
  "yerine getirilemez" sayıyor. Aynı sahne önce "something went
  wrong", sonra bu mesajı verdiyse sebep GEÇİCİ DEĞİLDİR.
  Tetikleyici (Cold Burn S8'de doğrulandı): İNSANSIZ sahnede uzun
  `NEGATIVE:` bloğu + "Exactly 0 human figures" kalıbı. Yokluk
  listesi ("no ... no ... no ...") istek olarak okunamıyor. Aynı
  blok insanlı sahnelerde sorun çıkarmıyor — orada istenen bir
  VARLIK.
  Çözüm sırası:
   1. `NEGATIVE:` bloğunu tamamen kaldır → tek satır pozitif
      `Style:` satırına indir
   2. SCENE/TIMELINE/AUDIO etiketlerini kaldır → düz betimleyici
      paragraf, zaman damgaları cümlenin içinde
   3. "human" kelimesini promptdan çıkar; boş kadrajı VARLIK olarak
      tarif et ("the cabin around it is empty and unlit") [D59]
   4. Hâlâ reddediyorsa: 3 satırlık mini prompt probu (geçerse
      sorun yapı/uzunluk, geçmezse hesap/oturum tarafı)
      ⭐ AYNI FİLMDE ÜÇÜNCÜ RED GELDİYSE bu adım BAŞA alınır —
        kısaltmadan önce çalıştır. PROB METNİ (10.08.2026'da Third
        Dune'da yazıldı; 21.08.2026'da film dosyasından buraya terfi
        etti — sistem bilgisi film dosyasında yaşayamaz, KULE 7 dersi):

        8-second single unbroken shot, 16:9, photorealistic. A fixed
        locked-off camera looks at rippled orange desert sand under a
        pale yellow sky. Wind moves a thin layer of sand across the
        ground. The desert stretches empty to the horizon in every
        direction.

        Prob da hata veriyorsa → sorun hesap/oturum/kota tarafındadır;
        hiçbir yeniden yazım işe yaramaz, kısaltmayı bırak.
        Prob geçiyorsa → sorun promptun yapısı/uzunluğudur; revize
        sürümle devam et, o da batarsa MİNİMAL sürüme in.
   5. ⛔ I2V — 01.09.2026'da YENİDEN YAZILDI [TUR 3]. Eski satır
      "son çare I2V: kurtarır" diyordu; YANLIŞTI.
      Start frame vermek metin denetimini KALDIRMAZ, üstüne PARALEL
      BİR GÖRÜNTÜ DENETİMİ EKLER (kare hash'lenip ünlü/telif/çocuk
      veri tabanlarıyla eşleşir). I2V bir kurtarma değil, RİSK TAKASI:
      metin riski ↓ · yüz/kadraj riski ↑.
        ✅ dene   → red KELİME ekseninden geldiyse ve karede yüz yoksa
        ⛔ deneme → red KOMPOZİSYON ekseninden geldiyse (reddedilen
                    kadrajı start frame yapmak onu ikinci denetime sokar)
      → tam reçete: POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md §5 basamak 6
      → teknik tarif: KESINTISIZ_VIDEO_URETIM_TEKNIGI.md
        (start/end frame zinciri)

QA KULLANIMI
  Künye bloğu boşsa rapor "UNVERIFIABLE" döner ve işe yaramaz.
  QA'nın önerisi filmin fiziğiyle çelişebilir — Low Power'da eleştirmen
  Mars'a "sert gölge" önerdi, bu YANLIŞTI. Öneriyi körü körüne uygulama.
```

---

# 8. 📊 MEVCUT FİLM MATRİSİ

| Film                                     | Format             | Ortam                                      | Tür                                 | Durum                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------- | ------------------ | ------------------------------------------ | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| THE DEAD APPROACH                        | 2-4 dk             | Vakum                                      | Bilimkurgu                          | QA: 3/10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| THE REMEMBERING DUST                     | 2-4 dk             | Vakum                                      | Bilimkurgu (yumuşak)                | Yazıldı, üretilmedi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| LOW POWER                                | 3-5 dk             | İnce atm.                                  | Bilimkurgu                          | QA: 4/10 (S14)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| THE WAKING GROUND                        | 7-9 dk             | Vakum                                      | Bilimkurgu                          | Sadece README                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| THE LAST SPAN                            | 2-4 dk             | Dünya atm.                                 | **Zombi** (aksiyon)                 | Yazıldı, üretilmedi — 23.08.2026 · yatay hattın ilk zombi filmi · 12 × 10 s = 2:00 · 0 kesme · 0 replik · risk 5/12                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| THE HELD HEAT                            | 2-4 dk             | Dünya atm. (kış, −24 °C, kapalı hava)      | **Zombi** (kaçış / taktik aksiyon)  | Yazıldı, üretilmedi — 26.08.2026 · yatay hattın **ikinci** zombi filmi · 14 × 10 s = 2:20 · 0 kesme · 0 replik · 14/14 sabit lockoff · 4 viral ara (S3·S7·S9·S11) · ⭐ **DEPODA PLAN SIRASINI DEĞİŞTİREN İLK FİLM: TEMA §0.2, NOVUM §0.3.** Tema (FEDAKÂRLIK) mekanikten ÖNCE seçildi ve mekanik onun taşıyıcısı olarak kuruldu; gerekçe §0.2'deki **İKİ YÖNLÜ DEĞİŞTİRME TESTİ**dir (A: novumu değiştir, tema ayakta kalıyor mu · B: temayı değiştir, sahne haritası değişmek zorunda mı — 14 sahnenin 4'ü çöküyor). Tema cümlesi novum kelimesi içermez: *"Koruduğun şey seni görünür kılar. Yine de koruyorsun."* [TEMA_MUHENDISLIGI §9] · novum bir yaratık değil **KAPI MEKANİĞİ**: buhar çağırır, figürler topuk üzerinde döner (90°/2,0 s, yer değiştirme 0,00 m) ve **döndükleri yerde kalır**; dönmüş sıra geçidi kapatır (0,45 m), sırtlar açar (0,60 m) · bilim çapası ortam kartı §3.3'ün kendi satırıdır (*"nefes — soğukta görünür buhar"*) · üç metinsiz sayaç ve üçünün **sahibi ayrı**: kırağı şeridi (yükün) 9 kademe · buhar sütunu yüksekliği (aracın) 1,5→0,9→0 · maske kırağısı (kadının) 0→%100 · doruk S9 = kutuyu yaşatan ısı torbasını ATMAK + kutuyu **kendi göğsüne** almak; **bedel AYNI karede** (o andan sonra buhar veren tek şey odur) · final GENİŞLEME + görsel ikilem (kurtardı ve kendini mühürledi) · ⭐ tür kartının altı satırı yeniden bütçelendi — **DÖRT SIFIR** (yürüme 0,0 s · temas **0 kare İKİ YÖNLÜ** · yüz 0 kare · yara 0 kare) ve ⛔ **anlam maliyeti de bütçelendi**: kırağı kabuğu yalnız BAŞTA, gövde sıradan kış giysisi — LAST SPAN'in bütün gövdeyi mühürleyip türün anlamını silmesinin düzeltmesi · ⚠️ risk 6/12 tetiklendi, **2'si tek kapalı öğeye indirildi** (su → tek erime nefesle, çıplak el ↔ sıvı **0 sahne** · parçacık → **TEK tür: su buharı**) ve **2'si tasarımla ELENDİ**: Kart 9 ışık mıknatısı (güneş yok, tek baskın kaynak yok, hedef bir ışık değil bir YOKLUK — istasyonun çevresinde buhar yok; S11-S12'de kamera HEDEFTE ve kadın kameraya koşar) + Kart 11 (14×10 s sabit) · ⭐ **D128 doğru uygulandı**: tek benzetme *"like a weather vane on a fixed post"* — metaforun fiziği mekaniğin aynısıdır; LAST SPAN'i batıran alçı/kabuk ailesi promptta HİÇ geçmez · ✅ prompt_kontrol.py: **0 BLOCK**; dört bulgu kapatıldı (D79 false positive · metin yasağı imzası · açı tipi 2→3 · **tema sahne indeksi**) ve iki bilinçli sapma §0.15b'de yazılı (video 2.391-3.267, **tavan aşımı 0/14** · kurulum 13, gerekçesi filmin tek yönlü coğrafyası + iki eş kadraj çifti S2≡S10, S3≡S9) · ⛔ SPEC AYRI DOSYA (`THE_HELD_HEAT_QA_SPEC.md`) — **MOD D koşulacak, mod V ön koşudur [D94/D117/D129]** |
| ~~THE LAST ROAD~~                        | 2-4 dk             | Dünya                                      | Zombi                               | ⏸️ 12.08.2026'da silindi — tür rafta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ~~THE LAST BLOCK~~                       | 2-4 dk             | Dünya                                      | Savaş                               | ⏸️ 12.08.2026'da silindi — tür rafta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| GLASS WORLD / LAST ARCHIVE               | shorts             | —                                          | Bilimkurgu                          | Eski format                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| THE SLOW TIDE (dikey shorts)             | shorts 9:16        | Okyanus dünyası                            | Bilimkurgu                          | Yazıldı, üretilmedi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| THE HOLDING FIELD                        | 2-4 dk             | İnce atm.                                  | Bilimkurgu                          | Yazıldı, üretilmedi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| THE SECOND SHIP                          | 10-20 dk           | İnce atm.                                  | Bilimkurgu (yumuşak)                | Plan + Bible + senaryo + kapak + müzik + referans paketi · Faz 1 TAM + Faz 2 S13-S20 promptu yazıldı, üretim yok                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| THE HERD                                 | 2-4 dk             | 🆕 Kalın atm.                              | Bilimkurgu (canlı)                  | Yazıldı, üretilmedi · ⚠️ risk 6/9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| THE DAWN FRONT                           | 2-4 dk             | İnce atm.                                  | Bilimkurgu (aksiyon)                | Yazıldı, üretilmedi · 🆕 depoda ilk SAHNE İÇİ KESME'li film: 14 sahne × 10 s / 26 segment / 12 kesme, kesmeler promptun içinde                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| THE STONE SKY                            | 2-4 dk             | İnce atm.                                  | Bilimkurgu (aksiyon)                | Yazıldı, üretilmedi · sahne içi kesme V2: 14 sahne × 10 s / 21 segment / 7 kesme (sahne başına en çok 1) · 5 replik AI diyaloğu · ⚠️ risk 5/9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| THE SLOW STONE (dikey shorts)            | shorts 9:16        | İnce atm.                                  | Bilimkurgu                          | Yazıldı, üretilmedi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| THE SINKING HOUR (dikey shorts)          | shorts 9:16        | 🆕 İnce atm. buz                           | Bilimkurgu                          | Yazıldı, üretilmedi · ⚠️ risk 2/9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| THE DULL EDGE (dikey shorts)             | shorts 9:16        | Dünya atm.                                 | 🆕 Savaş (tarihsel)                 | Yazıldı, üretilmedi · ⚠️ risk 3/9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| THE HALF SKY (dikey shorts)              | shorts 9:16        | Vakum (yörünge)                            | Bilimkurgu                          | Yazıldı, üretilmedi · ⚠️ risk 4/9 · ✅ 6 promptun 6'sı Veo eşiğinin altında                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| THE WINTER LINE (dikey shorts)           | shorts 9:16        | 🆕 Dünya atm. (günümüz, 2026)              | Bilimkurgu (çağdaş anomali)         | Yazıldı, üretilmedi · ⚠️ risk 2/9 · ✅ 6 promptun 6'sı Veo eşiğinin altında · dikey hattın ilk günümüz-Dünya konsepti                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| THE LOW MOON (dikey shorts)              | shorts 9:16        | İnce atm. (solunabilir)                    | Bilimkurgu                          | Yazıldı, üretilmedi · ⚠️ kart riski 2/9 ama gerçek risk kartlarda yok: sürekli hareket eden merkez nesne (yörüngedeki taş) · ✅ 6 promptun 6'sı Veo eşiğinin altında                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| THE UNBROKEN CITY                        | 2-4 dk             | İnce atm.                                  | Bilimkurgu (keşif)                  | 🎬 ÜRETİLDİ + 4 mercek QA (06.08: 🔧5.0Ⓥ · 🧩8.0 · 📖5.0Ⓥ · 🧍8.0) — ⛔ yeniden kurgu gerekli: doruk S9 kurguda yok, yanık başlık 2:40, kurgu 165≠160 s (DERS 72) · ⚠️ risk 4/9 · 16 sahne × 10 s = 2:40, 0 kesme (Stone Sky'ın kesme mimarisinin bilinçli tersi) · tamamen sessiz + tehditsiz dramaturji, doruk = bedelli seçim (S9) · 06.08: S14 biniş + S15 fırlatma koda'sı eklendi (S15 insansız) · ✅ 32 promptun 32'si Veo eşiğinin altında                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| THE STARLESS CIRCLE                      | 2-4 dk             | İnce atm. (🆕 GECE)                        | Bilimkurgu (keşif)                  | Üretim başladı (06.08: S12 teknik hata → prompt V2) · ⚠️ risk 4/9 · 18 sahne × 10 s = 3:00, 0 kesme, 4 viral ara (S3·S6·S16·S17) · deponun ilk baştan sona GECE yatay filmi · Unbroken City'nin ters aynası (bırakılan kayıt ↔ verilen güç) · doruk = ışık takası (S9) · 06.08: S14 biniş + S15 fırlatma + 🆕 S16-S17 uzay viral kodası eklendi (S15-S17 insansız; S16 gökten tek alet, S17 daireye doğru — kamera ilk kez yerden ayrı ama kadraj kilitli) · ✅ 36 promptun 36'sı Veo eşiğinin altında                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| THE FIRST MORNING (dikey shorts)         | shorts 9:16        | Dünya atm. (Geç Kretase, solunabilir)      | Bilimkurgu (zaman kazası)           | Yazıldı, üretilmedi · ⚠️ risk 4/9 — **Kart 2 (canlı) bilinçli ihlal: seride ilk megafauna** · 1 numaralı tuzak ağır çekim [Ders 12/44] · üretim S4'ten başlar, temiz çıkmazsa iptal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| THE WRONG SHADOW (dikey shorts)          | shorts 9:16        | Dünya atm. (günümüz)                       | Bilimkurgu (çağdaş anomali)         | Yazıldı, üretilmedi · ⚠️ kart riski 1/9 ama gerçek risk kartlarda yok: **çift gölge geometrisi** (kaynaksız ikinci gölge seti, 1,5°/sn) · sayısal GÖLGE TAKVİMİ 70°→0°→-20° · üretim S4'ten (hizalanma) başlar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| THE QUIET IMPACT (dikey shorts)          | shorts 9:16        | Vakum (yörünge, gece tarafı)               | 🆕 Bilimkurgu (aksiyon)             | Yazıldı, üretilmedi · ⚠️ risk 4/9 ama gerçek risk kartlarda yok: **iki büyük gövdenin katı-cisim teması** [Ders 17/38] · dikey hattın ilk aksiyon konsepti ve **novumu gerçek fizik olan ilk film** (imkansızlık yok, ölçek-hız uyuşmazlığı var) · sayısal kilitler: 12 m/s · tampon 12→3 m / 1,5 sn · 0,25 g · serbest nesne TAM 6 · **ateş TAM 1,0 sn** · 6 sahnenin 5'i lockoff · üretim S4'ten (temas) başlar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| THE COLD BURN                            | 3-5 dk             | 🆕 İnce atm. buz (0.9g) + vakum/0g         | Bilimkurgu (uçuş/yanaşma)           | Yazıldı, üretilmedi · ⚠️ risk 5/9 (kask · **2 insan** · ekran · patlama · diyalog) · ⚠️ bilinçli sapma: 30 sahne (klasör standardı 25) = 4:59 · deponun ilk İKİ İNSANLI ekip filmi + ilk docking sekansı · 12 replik / 10 sahne, hepsi kask telsizi / gövdesiz AI · doruk = S21 temas (0.2 m/s) · CENTRAL CHOICE = S19 iptal · üretim dört kapıyla başlar: S12 → S21 → S22 → S25 · 07.08 denetim turu: Ders 79 bloğu 32 prompta girdi, A4 taraması yapıldı, yıldız yayı fiziği düzeltildi · 07.08 ikinci tur: 4 varlık kanonik çapa bloklarına alındı (60 promptta birebir aynı tanım) + tasarım modernizasyonu · 07.08 üçüncü tur: kalkış geometrisi düzeltildi — yatay gövde, karın altında 4 kaldırma lülesi, sıra: motorlar→yükselme→ayaklar kapanır→kuyruk motorları · 🆕 REFERANS_PAKETI.md eklendi (6 sayfa / 28 panel) — 3-5 dk formatında ilk kez; metin çapası tek başına aracı sabitlemedi · 07.08 dördüncü tur: kalkış sonrası bacak durumu 18 promptta kilitlendi + ana gemi 65 m → 140 m yıldızlararası gövde (lander'ın 15 katı, oran karşılaştırmayla yazıldı)                                                                                                                                                                                                                                                                                                                                                                                    |
| THE SECOND SHIP — FRAGMAN (iki formatlı) | shorts 9:16 + 16:9 | İnce atm. (0.9g / 0.6 atm)                 | Bilimkurgu (fragman/teaser)         | Yazıldı, üretilmedi · **deponun ikinci FRAGMANI ve ilk İKİ FORMATLI dosyası** — aynı dosyada 9:16 (6 × 10 s = 60 s, ana teslim) ve 16:9 (9 × 10 s = 90 s) kesim · dosya kaynak filmin klasöründedir (`yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN.md`), shorts klasöründe değil · mekanik **SAYIM MERDİVENİ** 1 çizgi → 1 delik → 2 insan → 2 gemi → çok + 1 · kaynak filmin yalnız ilk %40'ı kullanılır; Bekçi'nin sırrı, Kaptan'ın kopyası, kule içi, doruk ve final **0 kare** · ⚠️ risk 4/9 (kaynak film daha yüksek; düşen kartlar **diyalog** ve **patlama** — atış bir delik açar) · ⛔ shorts standardından **iki bilinçli sapma**: sahne 8 s değil **10 s** (kaynak filmin tempo imzası + 96 BPM'de tam 4 ölçü) ve müzik **anempatik değil**, build + tek sub darbe taşır — sapmanın sınırı yazılı: tam beşli Sol–Re fragmanda HİÇ açılmaz, filmin tek çözülmesi harcanmaz · yatay varyant kırpma değil: dikeyde okunmayan üç vuruşu (çift enkazlar · iki yüz · çift çift tarla) ekler · üretim dört kapıyla başlar, ilki S5/Y8 Bekçi dönüşü                                                                                                                                                                                                                                                                                                                                                                                                          |
| THE COLD BURN — FRAGMAN (dikey teaser)   | shorts 9:16        | İnce atm. buz (0.9g) + vakum/0g            | Bilimkurgu (fragman/teaser)         | Yazıldı, üretilmedi (17.08.2026) · ⭐ dosya kaynak filmin klasöründedir (`yatay_4_dk_filmler/THE_COLD_BURN/THE_COLD_BURN_FRAGMAN_DIKEY.md`) ve **film sayımına GİRMEZ** — 17.08'de dikey klasördeki ÖLÇEK MERDİVENİ fragmanı silindi, filmin tek fragmanı bu · kaynak filmi yeniden anlatmaz, ilk %70'inden altı vuruş seçer ve cevabı vermez (doruk S26 + final S29 bilinçli olarak dışarıda) · mekanik **KAPANAN KAPILAR** (zemin → gezegen → zaman → araç → gemi → yanaşma; her vuruş bir çıkışı siler) · kaynak sahneler S2·S8·S10·S11·S17·S19 · ⚠️ risk 5/9 (kaynak film 6/9; düşen tek kart **diyalog** → Ders 82'nin yüzeyi kalmadı) · **patlama 0 kare · açık alev 0 kare · yüz 0 kare · temas 0 kare** · **6/6 tam lockoff** · 0 replik · ⛔ 1 numaralı risk kartlarda yok: **16:9 masterı kırpma tuzağı** — altı sahne 9:16 sıfırdan üretilir (dikeyde geometri de döner) · iki kadraj sapması kayıtlı: V5 85mm/6 m → 32mm/40 m, V4 ön cam → gövdeye monte kamera [FRAGMAN_KILAVUZU §1.3c] · çapa blokları kaynak filmden birebir [SAHNE_DEVAMLILIK §2.1] · müzik ÇIKARMA kürü (8,0 s'de hava kesilir) · üretim V4 (afiş) ile başlar                                                                                                                                                                                                                                                                                                                  |
| THE BLIND RETURN                         | 2-4 dk             | İnce atm. (Mars, 🆕 FIRTINA İÇİ)           | Bilimkurgu (sert gerilim)           | Yazıldı, üretilmedi · ⚠️ risk 5/9 TAM EŞİKTE (kask+durum değişimi · AI diyaloğu · toz) · 18 sahne × 10 s = 3:00 (15 gövde + 3 koda: pencere/çıkış/kalkış), 0 kesme · 8 replik hepsi SUIT AI, kadın hiç konuşmaz → dudak riski 0 · dört sayaç metinsiz (oksijen SESLİ, çatlak GEOMETRİ, görüş MESAFE, işaretçi NESNE) · doruk = kendini mühürleme (S11, bedel aynı sahnede) · S2↔S12 kadraj tekrarı · fırtına kuvvetsizliği fizik imzası (%0.6 basınç) · üretim S6→S11→S4 kapılarıyla başlar · ✅ 36 promptun 36'sı Veo hata eşiğinin altında                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| THE RING LIGHT                           | 2-4 dk             | 🆕 Vakum (halkalı gaz devi yörüngesi, 0 g) | Bilimkurgu (sert gerilim / yanaşma) | Yazıldı, üretilmedi · ⚠️ risk 5/9 TAM EŞİKTE (kask · 2 insan · sayaç · parçacık · diyalog) · **THE COLD BURN PART_B yanaşma zincirinden türetildi ama mekaniği değiştirildi:** gemi yanmıyor, sağlam ve BEKLİYOR; dönüş 2°/s pasif termal rulo (hata değil tasarım); ateş 0 kare · 14 sahne × 10 s = 2:20, 0 kesme, 14/14 lockoff, 2 viral ara (S2·S9) · **7 replik hepsi gövdesiz gemi AI'ı — iki insan da HİÇ konuşmaz, anlaşma EL İŞARETİYLE** (Ders 82'nin yapısal panzehiri: yüz görünen 2 sahnede replik yok) · kask 14/14 kapalı, durum değişimi 0 · iki sayaç metinsiz: 8 gözlü darbe göstergesi (8→0, sönen yuva görünür kalır) + göbek kaburgalarındaki GÜNEŞ SAATİ gölgesi · doruk = S8 buz karotunu bırakmak (bedel aynı karede, iki kez daha görünür) · ışık ekseni güneş → sıyırma → tutulma → **HALKA IŞIĞI** (ringshine, gerçek fizik) · ⛔ D69 ① kaydı plana yazıldı: biniş hareketi 0 kare, film eşiğe varmadan biter · üretim S11→S8→S9→S1 kapılarıyla başlar · ✅ 28 promptun 28'i Veo bandının içinde                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| THE BANDED DEEP                          | 2-4 dk             | İnce atm. (🆕 KANYON, %2 basınç)           | Bilimkurgu (keşif)                  | 🎬 KISMEN ÜRETİLDİ — 14.08: 186 s kurgu + üç QA koşusu (🔧Ⓥ4.9 · 📖Ⓥ7.4 · 🔊6.2; 🔧/📖 ⛔ ÖN KOŞU [D94] — SPEC §0.15'te hazırdı, mod V koşuldu) · ⛔ kurgu kapısı 3/4 ihlal: 12 klip ≠ 16 · 186 ≠ 160 s (ASL 15.5 ≠ 10 s) · 3:00 yanık başlık kartı (D70/72 zinciri 6. vaka) · S12-S15 (bedel+fırlatma+final) kurguda YOK — Ending 8.0 finalsiz kurgunun puanı · kilit çelişkisi defteri 5 ⬜ AÇIK (sırt ünitesi · toz şeritleri · gemi çıkışı · vizör CU · 1g) → master kontrolü bekliyor, ders yazımı D96 ile kilitli · ⚠️ risk 4/9 (kask · ikinci figür · toz · katmanlı dünya) · 16 sahne × 10 s = 2:40, 0 kesme, 16/16 sabit çerçeve, 3 viral ara (S1·S6·S15) · STARLESS/UNBROKEN iskeletinin üçüncü ölçümü ama eksen DİKEY (980 m kanyon inişi) ve serinin en renkli GÜNDÜZ paleti · tamamen sessiz · novum = 940 m'de terazide dümdüz 20 cm kara katman (gezegenin tek günlük güncesi — K-Pg bandı sınıfı) · dört sayaç metinsiz (kuşak RENGİ, çizgi KALINLIĞI, güneş YAYI, ankraj DURUMU) · doruk = S10 el ayası ölçümü, CENTRAL CHOICE = S9 tek cıvatanın harcanması (bedel S12 uzun yol + S13 boş yuva) · beyaz gemi çifti: 18 m ok başı inici + yalnız IŞIK NOKTASI olan ana gemi (ölçek riski sıfır) · kara bant DEAD MATTE kilidi (D20/D69 ③ ayna tuzağına panzehir) · D69 ① kaydı: biniş-iniş hareketi 0 kare (S3/S13) · üretim S9→S10→S2→S0 kapılarıyla başlar · ✅ 14.08.2026 prompt_kontrol.py: 32/32 GO, video 2019-2584 karakter bandın içinde |

| THE TALL SHORE | 2-4 dk | İnce atm. (🆕 KURU OKYANUS HAVZASI, 0.09 atm) | Bilimkurgu (keşif / ölçek) | Yazıldı, üretilmedi · ⚠️ **risk 6/9 — depodaki en yüksek sayım, eşiğin ÜSTÜNDE** (kask · ikinci figür · toz · katmanlı dünya · **diyalog** · sayaç); iki 🔴 kart (su · canlı) SIFIR ve gerçek ağırlık tek kartta: kadın konuşuyor · 18 sahne × 10 s = 3:00, 0 kesme, 18/18 sabit lockoff, 4 viral ara (S3·S7·S10·S15) · **konu ÖLÇEK:** 9.000 m'lik kıyı basamağından 1.100 km'lik kuru tuz havzasına iniş; ölçeğin tek taşıyıcısı **hava perspektifi sayısal kilidi** (kontrast 10 km'de dörtte bir düşer) — bu yüzden ortam Mars'ın %0.6'sı değil %9 basınç (bilinçli sapma, gerekçe planda) · ⛔ **depo standardından ikinci bilinçli sapma: kadın ÜÇ KEZ konuşur** (Ring Light/Blind Return 0 insan repliği) — panzehir TURN LOCK: 9 diyaloglu sahnenin 9'unda TEK konuşmacı, karşılıklı konuşma yalnız SAHNE SINIRINDAN geçer (S12 AI sorar → S13 kadın cevaplar) · ⭐ **HAZIR DÜŞÜŞ metni planda:** S2 kapısı batarsa üç kadın repliği üç AI repliğiyle değişir, risk 5/9'a iner, yeniden yazım yok · dört sayaç metinsiz (zaman SESLİ · mesafe YEDİ SEKİ · perspektif SIRT SAYISI 9→7→5→3→2→1 · geri sayım GÖLGE ETEĞİ 25 m/dk) · doruk S13 = kanıtı tuza gömmek (bedel aynı sahnede, S17'de hâlâ kadrajda) · **Canopy World'ün battığı madde omurga yapıldı:** LAYER LIGHT SCHEDULE irtifaya göre sıralı ve monotonik · üretim S2→S13→S7→S0→S17 kapılarıyla başlar (ilki tek İPTAL kapısı) · ⚠️ 14.08.2026 prompt_kontrol.py: **36/36 prompt, 0 BLOCK, FIX** — tek açık bulgu uzunluk (14 video promptu bandın üstünde, tavanın altında), kapatma yolu dosyada |

| THE SLOW LIGHT | 2-4 dk | İnce atm. (🆕 YILDIZINA KİLİTLİ — sabit alacakaranlık) | Bilimkurgu (keşif) | Yazıldı, üretilmedi · ⚠️ risk 4/9 (kask · ikinci figür · sayaç · toz); iki 🔴 kart SIFIR — gezegen kuru, ovayı boşaltan güç 0 kare · 16 sahne × 10 s = 2:40, 0 kesme, 16/16 sabit lockoff, 3 viral ara (S1·S6·S15), tamamen sessiz · ⭐ **depoda novum'u ÇALIŞAN BİR CİHAZ olan ilk film**: 600 karanlık röle direği arasında altı yıldır yanıp sönen tek verici; sinyal 12 ışık yılı gidecek ve şu an yolun yarısında · ⭐ **yeni alt-ortam: gelgit kilitli gezegen** — yıldız ufkun 4° üstünde SABİT, gölgeler 30 m ve film boyunca hiç kımıldamıyor; bu KART 6b'yi (katmanlı dünya ışık salınımı) YAPISAL olarak eler, Canopy World hatası imkânsızlaşır · üç sayaç metinsiz: ⭐ NABIZ ARALIĞI (3.0→4.5→6.0→9.0→3.0 s — dramatik saat, kaynak film dersi B2) · ızgara yoğunluğu (600 direk → kesilmiş kaideler) · güç hücresi (dolu → vericide → boş yuva) · doruk S11 = kendi güç hücresini ölülerin vericisine takmak; bedel AYNI karede (kask lambası 7.0 s'de söner, kadın karanlıkta döner) · ⭐ **dış film analizinden tema devri** — `kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` (kaynak klasör 05.09.2026'da kaldırıldı, seçki kurtarıldı) (20 parça / 66 rapor): ulaşmayan mesaj ironisi (B1), çizgi halinde alan görünmez güç (A2), kötü haberi sırttan çekmek (A1); devralınan 11 dersin uygulandığı sahneler §0.19'da satır satır işaretli · üretim S11→S6→S9→S0 kapılarıyla başlar · ✅ 15.08.2026 prompt_kontrol.py: **0 BLOCK**, 32/32 prompt tavanın altında — tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi ve ilk-red protokolü §0.14b'de |
| THE HOLLOW COUNT | 2-4 dk | İnce atm. (🆕 EVAPORİT TERASI — çökme havzası, %4 basınç, 0.7 g) | Bilimkurgu (keşif / sert gerilim) | Yazıldı, üretilmedi · ⚠️ risk 4/9 (kask · ikinci figür · toz · katmanlı dünya); iki 🔴 kart SIFIR ve **filmde YAPAY IŞIK YOK** (yalnız alçalan güneş + S13 jeti) · 14 sahne × 10 s = 2:20, **16 segment · 2 kesme yalnız S11'de**, 14/14 sabit lockoff, 5 viral ara (S0·S3·S5·S11·S13), tamamen sessiz · ⭐ **novum gerçek jeoloji**: yürünen zemin çözünmüş tuz boşluğunun TAVANIDIR ve kusursuz düz bir çizgi hâlinde, 20 saniyede bir 2 metrelik levha vererek çöküyor (14 m / 2.0 s) — tehdit yaklaşmıyor, YAYILIYOR · ⭐ **dış film analizinden ikinci tema devri** — `kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` (kaynak klasör 05.09.2026'da kaldırıldı, seçki kurtarıldı) (66 rapor): ironi tersine çevrildi (uyarı gecikmedi, kapı 90 saniyede kapandı; insanlar zaten aşağıdaydı), toplu ölüm **60 boş diskle** anlatılır (ceset·kan·rakam 0 kare), ifşa sırttan çekilir (S8, 10 s hold), devralınan 13 dersin sahne eşlemesi §0.19'da · ⭐ **depoda iki ilk**: eşleştirilmiş kadraj çifti (S2↔S12 aynı SETUP/CAMERA, tek değişken) ve kesmenin tek kullanımlık HIZ KARTI olarak kullanılması (S11, üç segment 3.4/3.4/3.2 s, filmin %79-86 aralığı) · üç sayaç metinsiz (kazık 12→0 · çizgi uzunluğu · ayak izi hattı) · doruk S9 = tek atımlık kap vince, kapı yuvası boş · final çözüm değil GENİŞLEME · üretim dört kapıyla başlar (levha → disk → eşleştirme → kesme) · ✅ 15.08.2026 prompt_kontrol.py: **0 BLOCK**, 32/32 prompt tavanın altında — tek FIX (uzunluk bandı) bilinçli sapma, gerekçesi ve ilk-red protokolü §0.14b'de |
| THE LAST SHIFT | 2-4 dk | 🆕 Solunabilir ama SPORLU atmosfer, kapalı hava (0.9 g / 0.8 atm) | Bilimkurgu (keşif / sert gerilim) | 🎬 **ÜRETİLDİ + KURGULANDI (16.08) — dört QA koşusu aynı gün:** 🔧Ⓥ5.0 · 🧩5.0 · 📖Ⓥ6.0 · 🧍6.0 (🔧/📖 ⛔ ÖN KOŞU [D94 ×6] — SPEC §0.15'te hazırdı, mod V koşuldu) · ⛔ **kurgu kapısı: plan 27 klip / 24 çekim / 190 s / ASL 7.9 → kurgu 17 × 10 s + 4 s kart = 174 s**; ~10 klip ekranda yok (S5 İFŞA 1 · S8 · S11 aksiyon ritmi) çünkü 80 s'lik kırpma bütçesi yazılmadı → **DERS 100**, kapı "14 sahne = 14 segment" diye geçirdi → **DERS 101** · 🔴 2:50 yanık başlık kartı (D70/72 zinciri **7. vaka**, alt satırı §5.3 kapak tipografisi) · 🔴 2:09 el–plaka kaynaşması (D11/D28) · ⛔ **BEŞ üretim kapısının beşi de kayıtsız** ve bulgular kapı 1-2-3-4'ün üstüne düştü (D74 ×2); KAPI 5 birleşik hold **TUTTU** (20 s'lik S7 dört raporda tek sahne) · ✅ D89/D95/D97 tuttu · kilit çelişkisi defteri 7 ⬜ AÇIK [D96] → onarım ve belge cevapları `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_LAST_SHIFT.md` · ⚠️ **risk 6/9 — eşiğin üstünde**, gerekçe §0.8 + HAZIR DÜŞÜŞ planı §0.8b · ⭐ **depoda ilk: bir DIŞ FİLMİN hikâyesi VE ölçülmüş kamera grameri devralındı** (`kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` (kaynak klasör 05.09.2026'da kaldırıldı, seçki kurtarıldı), 66 rapor) — ölü koloni, dışarıdan elle mühürlenmiş kapılar, pençe+kurşun adli kanıtı, çevirmenden gelen kırık ifşa ("savaş değil / hasat"), ricat ve çözümsüz genişleme finali; part-sahne eşlemesi §0.1b · ⛔ **sabit 10 s sahne ızgarası YOK**: 14 sahne · 24 çekim · 27 klip · 190 s · **ASL 7.9 s** (kaynak 9.0) · 10 kesme · 24/24 sabit kilitli kadraj · üç ritim modu (§0.9b) · ⭐ **esirgeme haritası** (§0.9c): sekiz zirvede yakın plan/ters açı/tepki çekimi bilinçli olarak YOK · ⭐ **birleşik hold** (iki klip = tek çekim) depoda ilk kez · ölçek yayı 75mm ECU → 30 km EWS · 2 insan, 13 replik hepsi gövdesiz makine, iki figür de hiç konuşmaz · **insan sayısı sayaçtır** (2→1→0), ölüm 0 kare · yaratık bütçesi 1 çekim / 3.0 s / tek uzuv / 300 m · ✅ 16.08.2026 prompt_kontrol.py: **0 BLOCK**, 51/51 prompt tavanın altında; tek FIX (uzunluk) gerekçesi §0.14b'de |

| THE BLACK CRADLE | 3-5 dk | 🆕 İnce atm. karbon gezegeni (0.8g, gece) + vakum/0g | Bilimkurgu (uçuş/yanaşma) | PLAN + PART_A + PART_B + KAPAK (A yüz %60 "sırtı dönük yanaşma" / B "katedrale geri geri") + MUZIK (§17 künye · 3 cue: 96/72/72 BPM · müzik S20'de MOTORLARLA birlikte susar, tek çözülme S23 · D83 telsiz yatağı) + MUZIK_V2_HAREKETLI (alternatif yüksek enerjili skor: 120/120/96 BPM, ters enerji eğrisi, aynı ızgara/kapılar — kurguya tek skor girer) yazıldı (16.08.2026; referans paketi sırada) · ✅ prompt_kontrol: 50/50 prompt, 0 BLOCK, FIX yalnız uzunluk (çapa blokları — gerekçe + kapatma yolu dosyalarda) · ⚠️ risk 5/9 TAM EŞİKTE (kask · 2 insan · sayaç · parçacık-dar · diyalog) — Cold Burn 6/9'dan bilinçli azaltım: ateş ve patlama 0 kare · **THE COLD BURN mantığının SİYAH TERSİ:** ışık yutan kara gezegen (albedo ~%1, DEAD MATTE), saten siyah gemiler, mat siyah suitler; tehdit sis duvarı değil YÜRÜYEN ŞAFAK HATTI (7 m/s) — ışık kovalar, karanlık evdir · ⭐ depoda üç ilk: tümü-siyah palet · **GERİ GERİ (kıç önde) kızak yanaşması** (fren = ana motorlar, 40 m içinde motor YASAK — plume kuralı) · pilotun hedefi HİÇ görmediği kör yanaşma işbölümü (mühendis göz, MİRA sayı, pilot el) · ⚠️ bilinçli sapma (17.08): 26 sahne — +S19b kanat kamerası ara sahnesi (Hook 9 s + 25 × 10 s = 4:19), 26/26 sabit kamera, 4 viral ara (S4·S7·S15·S21) · 14 replik / 12 sahne — 7'si MACHINE (MİRA), sayı söyleyen her replik MACHINE [D82 sigortası] · CENTRAL CHOICE = S17 iptal (bedel S18 tek segment) · doruk = S21 temas (%85-88, bant içi; Third Dune'un kurgu kapısını geçen S17/S21 iskeletiyle aynı) · kartlarda olmayan 1 numaralı risk: SİYAH-ÜSTÜ-SİYAH okunurluk — üç siyah doku ile ayrışır + HAZIR DÜŞÜŞ planda · üretim S15 → S21 → S7 → S0 kapılarıyla başlar |

| THE BLACK CRADLE — FRAGMAN (dikey teaser) | shorts 9:16 | İnce atm. karbon (0.8g, gece) + vakum/0g | Bilimkurgu (fragman/teaser) | Yazıldı, üretilmedi (16.08.2026) · ⭐ 17.08: dosya kaynak filmin klasöründedir (`yatay_4_dk_filmler/THE_BLACK_CRADLE/THE_BLACK_CRADLE_FRAGMAN.md` — Second Ship emsali, dikey klasörde değil) ve **film sayımına GİRMEZ** · kaynak filmi yeniden anlatmaz; ilk %70'ten 6 vuruş, **doruk S21 temas + iptal + final 0 kare** (kör yanaşmanın mekanizması da dışarıda: lomboz/üç ışık hiza anı fragmanda yok) · mekanik **TERS KURALLAR** (ışık öldürür → karanlık kurtarır → görmek=örtmek → ileri=geri → yanaşmak=geri geri → varmak=bakmamak) — Cold Burn fragmanının KAPANAN KAPILAR mekaniğinden farklı, sahne kesişimi ayrı film olduğundan 0 · **0 replik** (D82 yüzeyi kapalı) · 6/6 tam lockoff · risk 4/9 (kaynak 5/9; düşen kart diyalog) · gerçek 1 numaralı risk: SİYAH-ÜSTÜ-SİYAH (kaynak filmin azaltımı + HAZIR DÜŞÜŞ devralındı) · loop: V5 son kare → V0 (%80 siyah + tek sıcak ışık formu) · müzik tek cue 90 BPM loop-uyumlu · ⛔ kaynak film üretilip kurgu kapısından geçmeden fragman üretime alınmaz · ✅ prompt_kontrol: 12/12, 0 BLOCK, FIX yalnız uzunluk · üretim V4 (afiş — siyah-üstü-siyah kapısı) ile başlar |

| THE BLUE DRIFT | 3-5 dk | 🆕 Mavi dev uydusu: azot kırağısı (0.4g, gece yüzü — yalnız MAVİ planetshine) + vakum/0g | Bilimkurgu (yanaşma/kurtarılma) | Yazıldı, üretilmedi (17.08.2026) · PLAN + PART_A + PART_B + KAPAK + REFERANS_PAKETI (5 sayfa × 4 panel; üç durum çifti aynı sayfada: bacaklar · kollar · ölü/canlı panel) · prompt_kontrol: 50/50 film promptu 0 BLOCK (FIX yalnız uzunluk, gerekçeli) · KAPAK ✅ GO · üretim KAPI 0 (referans + §4 kapısı) → S21 → S15 → S4 → S0 sırasıyla başlar · **Cold Burn + Black Cradle ailesinin MAVİ üçüncüsü — palet üçlemesi kapanır: beyaz → siyah → MAVİ** · ⭐ novum: **ÖLÜ ARACIN YAKALANIŞI** — plazma perdesinin kenarı iticileri öldürür, araç balistik elipste; depodaki beş yanaşma filminde manevrayı hep küçük araç yaptı, ilk kez aktif taraf ANA GEMİDİR ve doruk EDİLGENDİR (sahibi AI: "Tuttum.") · tehdit depoda ilk kez GÖKTEN iner: aurora perdesi (taban 90°→40°, 10 s'de tek dalga, yalnız mavi-menekşe — YEŞİL NEGATİFTE) ve öldüren ışık değil, ışığın habercisi olduğu parçacık yağmuru · 25 sahne (Hook 9 s + 24 × 10 s = 4:09) — klasör standardı, sapma yok · 0 kesme, 25/25 sabit lockoff, 4 viral ara (S4 perde · S7 kalkış · S15 NEFES · S21 yakalayış) · 16 replik / 13 sahne, 10'u MACHINE (KERTE **ana gemidedir**, S9-S11 bağlantı kopuk → atışma yapısal imkânsız [D82]) · CENTRAL CHOICE S14 = kabin havasını itki olarak harcamak (6 düz puf × 1.5 s ile despin 1°/s→0; bedel S16'da mekanik ibrede %40) · doruk S21 %84-88 · ⚠️ risk 5/9 TAM EŞİKTE (kask · 2 insan · sayaç · parçacık-dar · diyalog); su·canlı·ateş·patlama 0 · kartlarda olmayan iki risk planda: MAVİ-ÜSTÜ-MAVİ (beş mavi ton/doku skalası + amber istisna ailesi + HAZIR DÜŞÜŞ) ve AURORA KLİŞESİ · üretim S21 → S15 → S4 → S0 kapılarıyla başlar |
| THE UPHILL DARK | 3-5 dk | 🆕 Vakum + İTKİ YERÇEKİMİ (0.220 g) | Bilimkurgu (sert gerilim / yanaşma) | Yazıldı, üretilmedi (17.08.2026) · PLAN + PART_A + PART_B + KAPAK + REFERANS_PAKETI · ⚠️ risk 4/9 (kask · 2 insan · sayaç · parçacık); iki 🔴 kart (su·canlı) SIFIR, diyalog kartı SIFIR (0 replik) · ⭐ **yeni ortam kartı: vakum + itki yerçekimi** — vakumun bütün kuralları geçerli (ses yok, gölge mutlak siyah, dolgu yok, alev düz koni) ama "her şey süzülür" GEÇERSİZ: gemi 0.220 g ile yandığı için yanındaki her serbest cisim kıça doğru 2.16 m/s² ile DÜŞER · ⭐ **D23 (sıfır-g rijitliği) yapısal olarak elendi** — filmde 0 kare sıfır-g var; prompt cümlesiyle değil KARARLA kapatıldı · novum'un taşıyıcısı üç KATI NESNE (sarkan kordon · düşen kartuş kovanı · düşen yük) — D73/D76 tuzaklarının ikisi de kapalı · 25 sahne (Hook 9 s + 24 × 10 s = 4:09), 0 kesme, 25/25 sabit lockoff, 4 viral ara (S4·S10·S19·S23), **0 replik** (Ring Light'ın panzehiri bir adım ileri: kaynak kilidi gereken tek replik bile yok → D82 yüzeyi 0) · ikisi de 25/25 sahnede KEMERLİ ve OTURUYOR → biniş/iniş 0 kare [D69 ①] · dört metinsiz sayaç (pencere merdiveni · sarkan kordon · 6→0 kartuş yuvası · 40 dolu→40 boş yük kızağı) · **aritmetik filmin kendisidir**: sabit itkili motor kısılamaz, tırmanmanın tek yolu 6 kartuş (3 çift × 40 m = 120 m), radyatör kanadı tırmanış 2'yi 12 s erken kestirir (22 m) → 16 m açık / 0 kartuş → tek çözüm 900 kg yükü atmak (0.220 g → 0.277 g) · CENTRAL CHOICE S19 %75.7, bedel AYNI KAREDE · doruk S21 temas 0.20 m/s (3:37.9 = %87.5) · turuncu TAM ÜÇ YERDE (iki skafandr · yük kayışı · atma kolu), S19'dan sonra kadrajda kalan tek turuncu iki insandır · ⭐ **REFERANS PAKETİ: varlık başına TEK SAYFA, sayfa başına TAM 4 PANEL** (5 sayfa / 20 panel; 17.08.2026'da 13 tek görselden indirildi) — iki durum çifti (yanaşma açık↔kapalı, kapsül yüklü↔boş) bilerek aynı sayfada, gerekçe ve bedeli dosyanın §0'ında · ✅ prompt_kontrol.py: 0 BLOCK, 50/50 prompt tavanın altında; tek FIX (uzunluk) gerekçesi + İLK RED PROTOKOLÜ PART_A §Üretim Notları'nda · üretim KAPI 0 (referans) → S19 → S21 → S4 → S1 sırasıyla başlar |
| LOSS OF LIFT | 3-5 dk | 🆕 Sürekli bulut / nötr yüzerlik (Venüs 55 km: 0.53 bar CO2, 0.904 g, bağıl rüzgâr 0-2 m/s) | Bilimkurgu (hayatta kalma / devretme) | **YAZIM: PLAN + PART_A + PART_B (20.08.2026)** — 25 sahne / 50 prompt, insanlı 21 videonun 21'i I2V (karakter videoda kompakt kilit satırı, çevre çapaları birebir); tek replik S22 ("Ağırlık bende kalsın.", telsiz, ağız kadraj dışı); 7 eş kadraj çifti (S0↔S24 · S2↔S17 · S3↔S18 · S9↔S16 · S10↔S20 · S12↔S21 · S11↔S23); prompt_kontrol iki dosyada 0 BLOCK, FIX yalnız uzunluk, tavan aşımı 0 · KAPAK ✅ GO (A: yüz + varmayan yağmur · B: S24 aynası; metin 0, tipografi post'ta) · MUZIK ✅ (§17 künye · TEK TEMPO 48 BPM = 2 ölçü/sahne · skor = kaldırma gazı: katmanlar SÖKÜLEREK ilerler, yalnız CUE C'de eklenir · motif inversiyonu: alçalan iki nota S23'te yükselerek tamamlanır · 30 s sessizlik penceresi S20-S22 — doruk, bedel ve tek replik müziksiz; S20 ıslık takası çıplak [D83]) · YAZIM PAKETİ TAM (PLAN+A+B+KAPAK+MUZIK+**QA_SPEC** [D117]) · ⚡ **21.08.2026 ÜRETİLDİ + 3 QA koşusu — üçü de mod V → ÖN KOŞU [D94]**: 📖 Ⓥ7.0 ŞARTLI (diyalog **9/10**, novum tek cümlede okundu, S0↔S24 çifti paylaşılabilir an seçildi) · 🧩 iki koşu 🚨 GEÇERSİZ (aynı defter, 8/10 ve 6/10 → **D119**) · kurgu kapısı: klip sayısı ✅ süre ✅ **SIRA ⛔** (insan şeridi slot 19/20 ters — doruk yuvası şüpheli → **D118**) · 🔴 4:10-4:15 başlık kartı = ekran metni 0.0 s kilidinin ihlali [D70/72] · kilit çelişkisi defterinde 6 madde ⬜ AÇIK, içerik dersi YAZILMADI [D96] · ⭐ **LOW POWER'ın kardeşi** — aynı motor, yeni malzeme: güç yerine KALDIRMA, toz yerine ASİT, karanlık yerine AŞAĞI · 🆕 **ortam kartı önerisi §3.6** (toz YOK → D39 tetiklenemez · gölge YOK, gölgesizlik MEŞRU → D41 zemini kalkar · güneş diski YOK → D104 zayıflar · kaldırma GERÇEK → çekirdeğin "never hovering" yasağıyla çakışır, çözüm 3.4 emsali: yasak parçacıkta kalır, gövdeye POZİTİF cümle [D59]) · novum = yüzen istasyonun kendisi (katı gövde; D73/D76 kapalı) · 25 sahne × 10 s = 4:09 standart, 0 kesme, 25/25 lockoff, 4 viral ara (S5·S13·S19·S23) · **1 replik** (S22, ağız kadraj dışı) · dört metinsiz sayaç (pin yayı 24 çentik × 250 m · buğu · kaçak ıslığı · sonda feneri) · aritmetik: kaçak 322 kg/s → 30 m/s batış; son tüp 600 kg = zarfa 70 metre ya da sondayı doldurup kolonu asidin üstüne çıkarmaya tam yeter · CENTRAL CHOICE S20, bedel aynı karede · ⚠️ risk 5/9 tam eşikte; su · canlı · parçacık SIFIR (toz/ateş/patlama/egzoz 0 kare) · kartlarda olmayan iki risk planda: okra-üstü-okra tekdüzelik + hovering çakışması |
| THE SKYLIGHT | 3-5 dk | İnce atm. (Mars 0.38 g · Arsia lav tüpü odası: 180 m çap / 60 m tavan / 40 m gök deliği) | Bilimkurgu (keşif / zaman) | **YAZIM TAMAM (27.08.2026): PLAN + PART_A + PART_B + KAPAK + QA_SPEC [D117] · ⭐ 28.08: PART_C AYRILIŞ eklendi (S25-S32, 16 prompt + SHIP BIBLE) → 33 sahne / 5:29 — ⚠️ FORMAT SAPMASI kayıtlı [D74]: sahip talebi, 3-5 dk bandı 29 s aşılır; çift kapanış (S24 oda · S32 gezegen — S0'ın ölçek aynası) · kalkış fiziği sayıyla: T+2 kalkış · 8 s'de kadraj-terk · toz düz balistik ≤2 s · metalox şeffaf mavi-mor geniş koni · biniş 0 kare · S31 0g nesneyle (insan kemerli) · 6 viral (S28 kalkış · S30 Tharsis+limb eklendi) · risk 5→6/12 (S28 tek insansız) · ⭐ KAPAK ANI S30'a TAŞINDI (sahip kararı 28.08 — ⚠️ PAKETLEME §1 sapması kayıtlı: 0:00-0:10 bandı dışı; S0 Plan B kapağı [KAPAK §7.2]; yayın-sonrası karar kuralı KAPAK dosyasında) · 🎵 MUZIK ✅ 28.08 (§17 künye · 2 cue: CUE A "SAAT" 48 BPM S3-S19 — anempatik nabız 2,5 s hiç değişmez, yalnız ton kararır = gün çekilir · CUE B "AYRILIŞ" 120 BPM S25-S30 — kalkış downbeat 4:41 = ölçü 16, S30 manzarada davullar düşer/akor GENİŞLER yükselmez [§7.1], MECO'da tam kesiş, S32 koda = tek çözülme · 3 sessizlik: hook 0:29 · 3:14-4:09 doruk+oda kapanışı (55 s, deponun en uzunu — yedek CUE A kuyruğu) · 5:09-5:19 MECO · §15.1a yığın cümlesi ilk uygulama · gürleme dükme kuralı) · ⚡ **29.08 ÜRETİLDİ + 6 MERCEK MOD V — hepsi ÖN KOŞU [D129, 8. film], SPEC verilmedi, tablo satırı YOK.** Teslim 31 klip + 5 s KAPAK kartı = 315 s (plan 33 / 329: 2 oda sahnesi eksik, aday S11+S14 · hook 9'a kırpılmamış) · ⑪ ölçüm: ses VAR (AAC 253 kbit/s · −17,0 LUFS · tepe −0,0 dBTP — ihraç kilidi dışı) ama 6/6 mercek "nothing audible" [D137 · 3. vaka] · 🔴 üretici filigranı 315/315 s, altı mercek görmedi [D150] · kareyle doğrulanan: klon S13 (2:07) · toz şelalesi S3/S6 · kanyon S26 · alev/bacak S28 · üç kask · kir sıfırlanması · cıvata S31 · ✅ S20 sönüş EKRANDA (④ "no peak" = rapor) · ✅ S32 final ekranda · ⑥ g≈3,8 m/s² Mars'ı doğruladı → **DERS 143-150** · kayıt `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_SKYLIGHT.md` · sonraki tur: filigransız/kartsız/−14 LUFS master → yeniden üretim (sahip onayı; önce bible'a kask geometrisi + kir merdiveni) → MOD D** — yatay hattın ilk yeraltı filmi (⚠️ ÇAKIŞMA KAYDI 27.08: aynı gün dikey hatta THE THIN ROOF bağımsız olarak aynı lav tüpü olgusunu seçti; üç eksende tam ayrım — format · kamera konumu · novum — tablo THE THIN ROOF dosyasının başında, karar sahibin) · novum ÖLÇEK, fizik ihlali yok (fener 25 m / duvar 90 m — ışın duvara ulaşamaz · taş 1,2 m → 0,8 s [0.38 g]) · TEMA: ZAMAN (⛔ takas kalıbı değil [TEMA §3c]) — ışık sütunu odanın tek saati: dik → eğik → kopuk → S20 klip İÇİNDE söner, monotonik · 25 × 10 s = 4:09 · 0 kesme · 25/25 lockoff · TAM SESSİZ (replik 0 · MACHINE 0 — kart 7 yapısal düşer) · insansız 0 sahne (25/25 insanlı — kart 10 düşer) · sayaçlar metinsiz: sütun eğimi · cairn 1→4 · RAKAMSIZ pusula (iğne hiç durmaz — Mars'ta kuzey yok, gerçek) · 4 viral (S3·S13·S19·S20) + S0 eski kapak anı (→ Plan B, 28.08) · eş kadraj S0↔S24 (ışığın sahibi değişir: göğün ışığı → insanın bıraktığı) · S2↔S23 · S6↔S18 (9↔5 adım, tek değişken saat) · CENTRAL CHOICE S20: son taş KARANLIKTA konur, bedel aynı karede, panik yok · ⚠️ risk 5/12 (eski 9'luk ölçekle 3/9 — eşik kalibrasyonu açık); su · canlı · diyalog · ekran · insansız SIFIR · kartlarda olmayan üç risk çözümlü: karanlık pozlama (true black MEŞRU cümlesi) · sütun tozu ↔ çekirdek (pozitif sürekli-düşüş cümlesi, S3 üretim kapısı) · oda geometrisi (üç sabit çapa + sayılar) · ✅ prompt_kontrol: PART_A 26 + PART_B 24 prompt — **2× GO · 0 BLOCK** (image bant-dışı sapmalar gerekçeli [D74]) · ⛔ SPEC AYRI DOSYA (`THE_SKYLIGHT_QA_SPEC.md`) — MOD D koşulacak · üretim kapı sırası: S0 → S3 → S5 → S20 |
| THE FROST LINE | 3-5 dk | İnce atm. (Mars 0.38 g · Arcadia Planitia, 39° K · şişirilebilir sera tüneli 32 m, 3 bölüm, İÇİ 30 kPa hipobarik — kask içeride de kapalı) | Bilimkurgu (hayatta kalma AKSİYONU / kimlik) | **YAZIM TAMAM (29.08.2026): PLAN + PART_A + PART_B + KAPAK + QA_SPEC [D117 · D142 E bloğu 9 makine kapısı, kuru koşu ffmpeg 8.1]** — 25 sahne / 50 prompt, 25/25 I2V · sahip talebi: *"daha aksiyonlu · yemek yetiştiren, uzun zamandır Mars'ta hayatta kalan adam · ultra gerçekçi"* · novum GERÇEK FİZİK (NEAR PASS sınıfı): kaçak KAR yağdırır (nemli sera havası 0.7 kPa'ya fışkırınca buz kristaline döner), havasız kalan yaprak saniyeler içinde BEYAZLAR — taşıyıcılar dikiş×avuç (S4) · dış yama×basınç (S5: 1 s'de kadraj dışı — dıştan yama TUTMAZ, içten tutar S10) · yaprak×mühür (S15·S19·S20); 7 sahne · 4 nesne · TEMA: KİMLİK ("Kazazede günleri sayar; bahçıvan sıraları." — ⛔ takas kalıbı değil; depoda ilk Kimlik filmi [TEMA §3c]) · sahne indeksleri S2·S8·S9·S13·S20·S21·S22·S24 · üç METİNSİZ sayaç: kar sütunu boyu · tavan sarkması (basınç saati, S6→S20 monotonik, S20'de bir karış GERİLİR) · yeşil sıra 9→6 / kırağı hattı · doruk S20 (3:19-3:29): kelepçe + zar ŞİŞER + son yeşil beyazlar + tavan gerilir AYNI klipte [B1/B2] · her şeyin kaybı S19 (kırağı hattı kendi bölümüne girer) · orta nokta S10 (iç yama tutar, dikiş yamanın ötesinde açılır: delik değil HAT) · hook YANLIŞLIK KOMPOZİSYONU (S0: adam tozu süpürürken 2.5 s'de dikiş yarılır; katalizör 0:02.5) · ⭐ KAPAK ANI S0 · 0:07 — PAKETLEME §1 bandının İÇİNDE · dramatik ironi ① arka plan (0:37 yarık ucu uzar, S6'da görür; panik 0 kare) · final MUĞLAK + tohum (kaygı hattı → yorum/kaydetme; görsel ikilem: en eski bitkileri kesti — tohum S3 bölüm bandı → S24 yeşil/beyaz sınırı) · S0↔S24 aynı kadraj, aynı fırça, sütun yok, üçte bir beyaz · 25 × 10 s = 4:09 · 0 kesme · 25/25 lockoff · TAM SESSİZ (replik 0) · insansız 0 · 12 kurulum / 5 açı tipi · ölçek merdiveni her kesmede tam 1 kademe, 2 şok (S0→S1 · S12→S13) · ⚠️ risk 7/12 (su-yarım: buz/kırağı KATI, sıvı 0 · kask · figür · parçacık · katmanlı · kamera · mıknatıs) — EŞİĞİN ÜSTÜNDE, kabul edilmiş maliyet (aksiyon talebi); azaltım listesi + kartlarda olmayan 4 risk (jet→duman · bitki dokusu · suit kırağısı · yaprağın klip içi beyazlaması) planda; üretim kapıları D144 biçiminde KABUL/RET/SONUÇ (S3 jet → S8 kırağı → S0 3 hook varyantı → S15 yaprak → S20 doruk) · KİR MERDİVENİ 4 faz [D147] · kask geometrisi [D146] · D143/D145 dersleri promptlarda (sayılı jet cümlesi, ufuk/gök) · ✅ prompt_kontrol.py: **0 BLOCK**, video 25/25 bandın içinde (2.35-2.60k), image gözlem; kurulum/açı/tema kapıları geçti · LOW POWER'dan ayrışma tablosu (aynı gezegen, aynı sera — ani/gür kriz ↔ yavaş toz; budama kararı ↔ fedakârlık; erkek 52 ↔ kadın 44; hipobarik) + THE MARTIAN'dan ayrışma (koli bandı şeması ters kanıtla kırılır) · 🏗️ **29.08 GÜNCELLEME (sahip talebi "modern Mars üssü + modern uzay gemisi"):** höyük yerine MODERN ÜS (4 beyaz yatay modül + 6 m düğüm, regolit setli, pencere şeridi, radyatörler, çanak anten, güneş tarlası) ve 120 m ötede 24 m'lik dik MÜRETTEBAT İNİŞ ARACI (kargo kapağı ekran-sağa — yönelim kilidi) — yalnız S0·S2·S24 arka planında, hiç yaklaşılmaz, biniş 0; tematik: gemi = kazazedenin nesnesi, S2'de ona sırtını dönüp yaraya koşar · 🎵 **MUZIK ✅ 29.08** (§17 künye · CUE A "BASINÇ" 72 BPM S1-S12: nabız hiç değişmez, yalnız üst band kapanır = incelen hava · CUE B "MÜHÜR" 120 BPM S13-S18 aksiyon sürüşü, 3:07'de STOP DEAD, S19 müziksiz, 3:24.0'ta TEK damped darbe = kelepçe ve uğultuyla birlikte kesilir, koda S22-S24 motif 3:59'da tamamlanır — tek çözülme · 3 sessizlik · §15.1a yığın · uğultu dükme kuralı · 3 sahip kararı ⬜) · ⚡ **31.08 ÜRETİLDİ + 6 MERCEK MOD V [D129 · 9. film] — tablo satırı YOK.** Master 235,2 s · **720p** · ses VAR −21,5 LUFS (6/6 mercek "duymadım" [D137 · 4. vaka]) · 23 klip + 5 s kapak kartı: **S12 + S23 EKSİK**, hook kırpılmamış, filigran "▷" 235/235 [D150 · 2. vaka] · kareyle doğrulanan: S5 yama uçuşu + S15/S19 klip içi beyazlama EKRANDA (mercekler görmedi/ters okudu → D151) · ⛔ S20 doruk vuruşu YOK (E7-b) · S24 fırçasız, çökük film BRANDA (E6) → D152/D153 · S6 erken tam çöküş · sırt ünitesi yuva 13 [D139] · kırağı iki yönde dalgalı [D147] · iki yerçekimi → D154 · üretim kapıları yazılı, SONUÇ ⬜×5 [D144] · **DERS 151-154** · kayıt: `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_FROST_LINE.md` · sonraki tur: S12/S23 üretimi + S20·S24·S6·S0 yeniden + filigransız/kartsız/−14 LUFS/≥1440p master → MOD D |
| THE BORROWED WEIGHT | 3-5 dk | İnce atm. (adsız gri gezegen: %1.2 bar, 0.92 g, sürekli örtü — güneş diski 0 kare) | Bilimkurgu (fedakârlık / devretme) | **YAZIM PAKETİ TAM (22.08.2026): PLAN + PART_A + PART_B + KAPAK + QA_SPEC [D117]** — 25 sahne / 50 prompt + 2 kapak · 🆕 depoda ilk kez novum İNSANDA yaşıyor: yerden kesilen parça ağırlığını taşıyana devreder (fiziksel yasa tipi; kural 6 sahnede 5 katı nesneyle kanıtlanır — ONERME üç kapısı ✅) · TWIST + tohum finali [FINAL kılavuzu 3-5 dk kuralı]: hafifleyen enkaz gece rüzgârıyla gider, S24'te ova BOŞ · sayaç metinsiz İZ DERİNLİĞİ 2→23 cm + adım eş kadrajı S6↔S18 + rakamsız kantar · 4 replik hepsi MACHINE, dördü ağız-dışı kadraj (lip-sync yapısal imkânsız; HUMAN 0) · 23/23 kask kapalı · ⚠️ risk 5/9 tam eşikte (su·canlı·katman SIFIR) · prompt_kontrol 3 dosyada 0 BLOCK · üretim kapıları S0→S1(kayma)→S5→S20 |
| THE BORROWED WEIGHT — FRAGMAN (dikey teaser) | shorts 9:16 | İnce atm. (adsız gri gezegen: 0.92 g, %1.2 bar) | Bilimkurgu (fragman/teaser) | Yazıldı, üretilmedi (22.08.2026) · ⭐ dosya kaynak filmin klasöründedir (`yatay_4_dk_filmler/THE_BORROWED_WEIGHT/THE_BORROWED_WEIGHT_FRAGMAN_DIKEY.md`) ve **film sayımına GİRMEZ** · kaynak filmi yeniden anlatmaz; ilk %70'ten 6 vuruş (S0·S2·S5·S14·S13·S11), **doruk S20 + kasa S21-22 + iki ışık S23 + twist S24 + kantar/ibre 0 kare** · mekanik **TERAZİ** (her vuruş kefe değiştirir: dünya hafifler ↔ adam ağırlaşır; kaldırış→sürüklenme nedensellik çifti tek vuruşta 0 — novumun görüntüsü girer, mekanizması girmez) · **0 replik** (filmin 4 MACHINE bildirimi fragmana alınmadı — D82 yüzeyi kapalı) · 6/6 tam lockoff · risk 3/9 (kask · sayaç · toz; kaynak film 5/9 — düşen kartlar diyalog ve ikinci yüzey riskleri) · gerçek riskler kartsız: kırpma tuzağı + çekirdek-kayma çakışması (V4, filmin S1 kapısıyla AYNI cümleyi test eder [D59]) + gri-üstü-gri · ekran yönü kilidi dikeyde DERİNLİK eksenine çevrildi (kaynak planın D104 basamağı — kamera hedef yanında, kameraya yürüyüş = hedefe yürüyüş) · loop: V5 ilk adım → V0 yürüyüş (kirişin belirmesi tasarım — 'nereden aldı?' sorusu ikinci izlemeyi satar) · prompt yapısı kaynak filmin **I2V hattı** (Cold Burn T2V emsalinden bilinçli ayrım: yüz-ağırlıklı çapa) · müzik tek cue 60 BPM loop-uyumlu, tek yapısal olay 32,0 s'de boşalma (V4 insansız) · ✅ prompt_kontrol: 12/12, 0 BLOCK, 0 FIX, GO (image bandı üstü gözlem — gerekçe dosyada) · üretim V4 (afiş — kayma kapısı) ile başlar |
| THE SHORT WAY DOWN (dikey shorts) | shorts 9:16 | Dünya atm. (günümüz, kışın ortası, −4 °C — bitmemiş 14 katlı bloğun çekirdek merdiveni) | 🆕 **Zombi / kaçış aksiyonu** (rafta olan §4.2 kartı dikey hatta geri açıldı) | Yazıldı, üretilmedi (22.08.2026) · ⛔ **risk 6/12 — EŞİĞİN ÜSTÜNDE, kabul edilmiş maliyet** (canlı · ikinci figür · parçacık · katmanlı dünya · kamera · ışık mıknatısı); gerçek risk kartlarda yok: **düşüp AYAĞA KALKAN gövde** — modelin dört bozulma modu dosyada yazılı · ⭐ **depodaki ilk gerçek KOVALAMACA ve klasörün ilk DEVAM ZİNCİRLİ dosyası**: 6 sahne bağımsız an değil tek kesintisiz iniş, 5/5 kesme gizli geçişle (perde) tasarlandı, her sahnenin ayrıca I2V DEVAM sürümü var (TEK_CEKIM §5'in dikeydeki ilk uygulaması) · mekanik **GÜZERGÂH EŞİTSİZLİĞİ**: kadın merdivenden iner, takipçiler korkuluğu aşıp düşerek iner (12,0 m / 1,56 s) ve düştükleri yerden kalkar — filmin TEK fizik ihlali o kalkıştır · novum taşıyıcısı KATI (korkuluk × aşma jesti) → D73 tuzağı elendi · sayaç metinsiz tek kanalda: MESAFE 9→6→11→7→2,5→14 m · temas 0 kare · yüz sayısı 1 · takipçi yürüme bütçesi TOPLAM 4,5 sn · yara/kan/silah/patlama/su 0 kare · kamera 5/6 tam lockoff (aksiyon Z ekseninden ve kadrajı kesen geçişten) · doruk S5 = kadının onların yolunu kullanması, bedel aynı karede (5,5 m düşüş, sol bacak tutmaz) · final DÖNGÜ + TWIST · üretim S0'dan (düşüş+kalkış) başlar · ✅ prompt_kontrol.py: **0 BLOCK / 0 FIX — GO**, 6 video promptu 2.006-2.337 karakterle bandın içinde |
| THE IRON SLOPE (dikey shorts) | shorts 9:16 | 🆕 Vakum + itki yerçekimi (§3.5 — kartın DİKEY hattaki ilk filmi; 0,220 g sürekli yanma) | Bilimkurgu (hayatta kalma aksiyonu) | ⛔ **ÜRETİLDİ VE ÖLÇÜLDÜ (25.08.2026) — YAYINLANMAZ:** altı mercekli QA + master ölçümü; teslim 65,0 s (6 × 10,005 s klip + 4,97 s başlık kartı) ve **serbest parça hızlanmıyor** (sabit ~0,15 m/s) → novum ekrana gelmedi. Kartın tersine dönen kuralı ilk kez ölçüldü ve tutmadı → **DERS 124 · 125 · 126 · 127**; kayıt: `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_IRON_SLOPE.md` · yazım 24.08.2026 · risk 4/12 (Kart 3·4·5·9; Kart 6 TASARIMLA kapatıldı: toz/duman/alev/çarpma 0 kare) · novum ALGISAL ve gerçek fizik (Quiet Impact emsalinin ikincisi): "uzayda aşağı var — aşağısı motor"; her gevşek parça kıça doğru 2,16 m/s² ile düşer · aksiyon: 48 saniyelik kesintisiz merdiven tırmanışı + ölçülü geçişler (1,4/1,2/1,1/1,0/0,8 m — temas 0 kare) · 6/6 TAM LOCKOFF, üç kurulum gemiye kelepçeli · sayaç metinsiz üç kanal: gevşek parça 3→0 · hava kilidi 14→2 m · turuncu motor jantı · merkezi seçim S4: karabineri açar, korunmayı zamana takas eder (bedel aynı karede: şakül gibi asılı şerit) · doruk S5: 6 m latis 1,0 m yanından geçer, sonra MOTOR SUSAR (2,2 s yanma arası = twist; tohum S0 0:05,8 jant kararması) · final DÖNGÜ + TWIST, kinesik reset (S5 son jest = S0 ilk jest) · gerçek risk kartlarda yok: TIRMANAN GÖVDENİN EKLEMLENMESİ [D18 akrabası], bütçelendi · üretim S0'dan başlar · ✅ prompt_kontrol.py: GO, 0 BLOCK / 0 FIX; video 2.236-2.586 bandın içinde · SPEC ayrı dosyada [D117] |
| THE NEAR PASS (dikey shorts) | shorts 9:16 | 🆕 İnce atmosferli kayalık gezegen yüzeyi, gündüz (9 kPa · 0,62 g · saçılma yok) | Bilimkurgu (keşif — huşu) | 🆕 25.08.2026 · **ÇOK YAKIN UYDU** — kullanıcı talebi. **6 × 10 s = 60 s: ızgara D124'ten sonra ilk kez ARAÇTAN yazıldı** (klip süresi 10,005 s ölçümü künyede) · novum ALGISAL ve tamamen gerçek yörünge mekaniği (Quiet Impact / Iron Slope emsallerinin üçüncüsü): **"gün batmaz, KAPANIR"** — 52 km'lik uydu 150 km irtifada, 4.965 m/s, batıdan doğuyor, ufuktan ufuğa 8 dk 05 sn, günde 19 geçiş; yıldızdan 18 kat geniş olduğu için gündüz **1,2 saniyede kapanıyor**, **19,1 saniye** kapalı kalıyor, **0,94 saniyede** açılıyor (asimetri gerçek: uydu uzaklaşıyor) · gölge düzlüğü 5.351 m/s = **Mach 23,7** ile geçtiği için önünde hiçbir şey gelmiyor ve **ışık kapanırken SES HİÇ DEĞİŞMİYOR** · ⭐ **D127'nin İLK KARŞI TASARIMI:** açısal hız hiç yazılmadı; tırmanış SÜRE + PİKSEL + KENDİ ENİ olarak yazıldı (her sahnede kendi eninin %34-55'i, oran monoton büyüyor) ve ikinci sabit cetvel gökyüzüne çivili yıldızdır (aralık 236→159→67→0 px) · S0 kapısı MAKİNEYLE koşuluyor [D125]: 0 ve 10. saniye karelerinde alt kenar farkı <100 px ise film üretilmez · 6/6 TAM LOCKOFF, üç kurulum da yere oturuyor; 2 kurulum sıkıntısı yok, ölçek Z ekseninden geliyor (S2'de 8 m yürüyüş) · lens 24mm + 75mm KÜRESEL — 32mm GEOMETRİK OLARAK ÇALIŞMIYOR ve hesabı dosyada · sayaç metinsiz ÜÇ kanal: PALL'ın boyu/yüksekliği · yıldız aralığı · ışık seviyesi (ikili, tam iki geçiş) · risk 4/12 (Kart 3·4·5·9); **Kart 6 TASARIMLA kapatıldı** — toz/duman/enkaz/düşen cisim 0 kare, ilk taslaktaki toz filamenti ÇIKARILDI · merkezi seçim S4 42,8-43,2: kask lambasını söndürür, bedel aynı karede (ışık dairesi ve yarık çizgisi birlikte söner) · doruk S5: ışık 0,94 s'de dönüp KANITI SİLER (bakır gider, çatlak ağı soluk lekeye iner) · final DÖNGÜ + GERİ ALMA, kinesik reset · ⭐ **prompt_kontrol.py ilk koşuda BLOCK verdi:** 12 promptta dünya-uzayı yön kelimesi (pusula) — hepsi ekran uzayına çevrildi; ikinci koşu **GO — 0 BLOCK / 0 FIX**, video 2.402-2.594 bandın içinde, image 5.486-5.857 (emsal bandının 188 karakter üstünde, gerekçesi dosyada) · SPEC ayrı dosyada [D117] |
| THE OPEN SEAM (dikey shorts) | shorts 9:16 | 🆕 **OKYANUS DÜNYASI** — karasız, 60 km derinliğinde küresel okyanus, üstünde 60 metrelik BERRAK (tek kristal) buz kabuğu; ince N₂+CO₂, 8 kPa, 232 K, 1,08 g | Bilimkurgu (keşif — huşu) | 🆕 26.08.2026 · kullanıcı talebi üç turda netleşti (yakın uydu → bol renk → **okyanus + üç ay + keşif**) · **6 × 10 s = 60 s**, ızgara araçtan [D124] · ⭐ **DEPONUN İLK ÜÇ AYLI FİLMİ ve ilk ÜÇ IŞIK KAYNAKLI kadranı:** ARDE 7,04° kendi lavıyla yanan turuncu (Roche'un 166 km dışında, gelgit ısınması 66 W/m² = Io'nun 26 katı) · NIVE 2,33° keskin mavi-beyaz buz ayı · VELUM 1,86° kenarsız menekşe-gül puslu ay · güç oranı 5:3:1 · novum ALGISAL, ZEMİN TERSİNMESİ: *"üstünde durduğun şey bir tavan"* — taşıyıcı KATI ve BİRİNCİL (60 m'lik cam kabuk) [D73 tuzağı elendi] · sayaç metinsiz ÜÇ kanal: **üç gölgenin yelpazesi** (35°→3°→−4°, ortadaki 2,52 m ile 6/6 sabit referans) · **üç kordonun derinliği** (turuncu 10 m · menekşe 29 m · mavi-beyaz 60 m'yi geçip suya girer — buz kırmızıyı önce yer) · **dikişin genişliği** (0,15→1,4→2,8 m) · keşif üç adımda ve gözle: çatlaklar düz değil YAY (sikloid) → üç yay ailesi kesişiyor → kesişmede kabuk 9 m ve dikiş NEFES ALIYOR · üç gelgit 41,4+5,1+8,2 m, hizalı toplam 54,7 m · ⛔ **KART 1 (SU/SIVI · 🔴 deponun en kötü ölçülen malzemesi: Tidal Hunt 2/10) DOSYANIN MERKEZİNDE ve SAYIYLA BÜTÇELENDİ:** su 6 sahnenin 2'sinde ve toplam 14,0 s görünüyor · temas 0 kare · en yakın 1,5 m · dalga/kırışık/sprey/damla/köpük/akıntı 0 kare (ölü durgun ayna) · **suda insan yansıması 0 kare** [D20] · donma yalnız S5'te ve bir YÜZEY değişimi olarak [D14] · ⭐ **KART 9 YAPISAL OLARAK KAPALI** — kadranda tek baskın ışık yok, ÜÇ tane var; üç aylı gökyüzü bir renk tercihi olduğu kadar bir risk çözümü · Kart 6 tetiklenmiyor (toz/sprey/kırıntı/duman 0 kare; buz ufalanmıyor, bloklar YANAL ATIMLA kayıyor: 1,2 m/0,5 s · 2,2 m/1,1 s) · risk **4/12** · merkezi seçim S3: geri çekilmeyip dudağa diz çökmek (bedel aynı karede: levha 6° yatıp 40 cm düşüyor, üç gölge bire iniyor) · doruk S4: arada cam olmadan açık okyanus ve suda ÜÇ RENKLİ DİSK · final DÖNGÜ + GERİ ALMA (dikiş kapanıyor, geriye süt beyazı şerit kalıyor; yelpaze TERS tarafa açılıyor) · ⚠️ gerçek 1 numaralı risk kartlarda yok: **berrak buzun cam gibi üretilmemesi** — beş maddelik geometrik karşı önlem + S0 kapısı makineyle · ⚠️ film gerçek zamanlı DEĞİL (117 dakikadan altı an; gerekçe dosyada) · sert kesme 5 (bandın üstünde, bilinçli) ama **5/5 ses köprülü — depodaki en yüksek oran** · ✅ prompt_kontrol.py: **GO — 0 BLOCK / 0 FIX, İLK KOŞUDA**; video 2.175-2.433 bandın içinde, image 5.742-5.965 (emsallerin ~%5 üstünde, gerekçesi dosyada) · SPEC ayrı dosyada [D117], filmle aynı gün |
| THE THIN ROOF (dikey shorts) | shorts 9:16 | 🆕 **MARS** — ince atmosfer (610 Pa · 0,379 g · 243 K), toz sıyrılmış kömür grisi bazalt kaldırımı, geç ikindi (§3.2 kartının DİKEY hattaki ilk filmi) | Bilimkurgu (keşif — huşu) | 🆕 27.08.2026 · kullanıcı talebi: *"Mars'ta geçen baya gerçekçi bir dikey shorts"* · **6 × 10 s = 60,03 s**, ızgara araçtan [D124] · ⭐ **deponun İLK DİKEY MARS FİLMİ ve İLK DRAMATİK İRONİ FİLMİ** — HOOK §3.1 27.08'de eklendi ve 16 dikey filmin 16'sı farkında olmadan "YOK" yazmıştı; bu dosya taşıyıcı ② (ZEMİN OKUR) ile ilk kez kullanıyor, asimetri anı **0:22,4** · novum ALGISAL ve tamamen gerçek jeoloji/geometri (Quiet Impact · Iron Slope · Near Pass emsallerinin DÖRDÜNCÜSÜ): **"eğri, ancak yukarıdan eğridir"** — 5,8 m yarıçaplı halka çatlağın görünen 2,0 m'lik yayı yalnız **8,7 cm** sapar (sagitta hesabı dosyada), yani 0,40 m göz yüksekliğinde DÜZ, 9,00 m'den KAPALI HALKA · ⭐ **açı TİPİ novumun taşıyıcısıdır** ve THE NEAR PASS'in açık maddesini (6/6 alt açı) yapısal olarak kapatır: üç kurulum üç yükseklik ve üç açı tipi — **0,35 m ALT AÇI · 1,55 m GÖZ HİZASI · 9,00 m ÜST AÇI** (A-B-C-B-C-A) · pit 74 × 61 m, taban 46 m ve **hiçbir kurulumdan görünmez** (ışın hesapları dosyada: A 2,57 m · B 25,5 m · C 41,4 m) · ⭐ **GÖLGE İÇİ DOLGU** ilk kez bir KAPI: Mars saçılma yapar, gölgeler yumuşak kenarlı ve İÇİ DOLUDUR [§3.2] — deponun son beş filmi vakumdu ve "mutlak siyah" yazıyordu; E bloğunda ffmpeg ile ölçülüyor (YAVG < 18/255 → sahne reddedilir) · sayaç metinsiz ÜÇ kanal: kenara mesafe 3,4→1,1→0,9→0,7→1,9→7,4 m · 62 mm'lik çakıl (durur → sallanır 25° → 0,40 m / 3,6 s / 0,060 m/s² yuvarlanır → çatlağa girer) · halkanın kadrajda okunabilirliği · risk **4/12** (Kart 3·4·5·9); **Kart 6 TASARIMLA kapatıldı** — Mars filmi olmasına rağmen hareket eden tek toz tanesi yok (zemin rüzgârın temizlediği kaldırım, toz yalnız eklemlerin içinde ve durgun); ilk taslaktaki "kayayı fırçalama" jesti ÇIKARILDI ve el yuvası düz avuç basınç testine çevrildi, risk 5/12'den 4/12'ye indi · gerçek 1 numaralı risk kartlarda yok ve dosyada tanımlı: **kavisin üretilmesi** (A/B promptlarında DÜZ, C promptlarında KAPALI HALKA — zıt talimat aynı prompta girmiyor) ve **gölge içi dolgunun kaybolması** · ⛔ **ÜRETİM SIRASI NORMAL DEĞİL: S2 İLK ÜRETİLİR** — halka orada kapanmıyorsa film üretilmez · tema **YALNIZLIK** (§3c moratoryumundan sonra HİÇ KULLANILMAMIŞ listeden ilk seçim; tek cümle TAKAS kalıbı DEĞİL) · merkezi seçim S4 48,1-49,3: yüzükoyun uzanma — bedel aynı karede, göğüs konsolu kayaya kapanır ve yüz tek sıcak çene kenarına iner (vizör beklenti satırı ④, vizör durumu 6/6 aynı) · doruk S5 56,5-58,0: **AYAĞA KALKAR** ve gördüğü şeyin sebebi ışık değil KENDİ GÖZ YÜKSEKLİĞİDİR (0,40 → 1,62 m); ovada aynı hatta üç çöküntü daha (210 · 480 · 790 m), ufuk 3,31 km · final DÖNGÜ + TWIST, kinesik reset (60,03 = 0,00) · ✅ prompt_kontrol.py: **GO — 0 BLOCK / 0 FIX** (ilk koşu 1 FIX: açı tipi 2 + ekran uzayı + uzunluk — kapı kaydı dosyada); video 2.537-2.600 bandın TAM içinde, image 5.960-6.455 (emsallerin üstünde, sebebi ve kısaltma sırası dosyada) · ⛔ **SPEC AYRI DOSYADA: `THE_THIN_ROOF_QA_SPEC.md`** [D117] — filmle AYNI GÜN indi |
| THE HEAVY SIDE (dikey shorts) | shorts 9:16 | 🆕 **VAKUM + DÖNME YERÇEKİMİ** — yarıçapı 9,00 m olan, hiç basınçlandırılmamış bir dönme modülünün iç güvertesi; dönme periyodu 60 saniyede 13,00 s → 8,00 s (§3.7 kartının İLK filmi, kart bu dosyayla açıldı) | Bilimkurgu (keşif — **aksiyon kulvarı**) | 🆕 29.08.2026 · kullanıcı talebi tek kelimeydi: ***aksiyonlu*** · **6 × 10,005 s = 60,03 s**, ızgara araçtan [D124] · ⭐ **deponun İLK DÖNME YERÇEKİMİ filmi ve ilk ENTROPİ temalı filmi** (sayac.sh tema dağılımında ENTROPİ satırı yoktu; §3c'nin HİÇ KULLANILMAMIŞ listesinden, tek cümle TAKAS kalıbı DEĞİL: *"biriktirilmiş her şeyin er geç dağılması"* — göbekteki fren volanının açısal momentumu halkaya dağılıyor, volan durdukça halka hızlanıyor) · novum FİZİKSEL YASA ve tamamen gerçek mekanik (Quiet Impact · Iron Slope · Thin Roof emsallerinin BEŞİNCİSİ): **a = (v ± u)² / R** — dönüşle aynı yöne 2,60 m/s koşmak ağırlığı 270 N'dan 621 N'a çıkarıyor (2,30×), ters yöne 3,30 m/s gitmek altıda birine indiriyor ve tek itişle güverteyi bıraktırıyor (1,15 s · 3,80 m · tepe 8,7 cm) · ⭐ **filmin ekseni bir EŞİTSİZLİK**: ileri sıçrayışın matematiksel tavanı wR/(2v) = **1,97 m**, boşluk **3,50 m** — hangi hızla koşarsa koşsun ileri yönde geçemez, ve daha hızlı koşmak durumu KÖTÜLEŞTİRİR · çözüm güvertenin ALTINDAN el ele geçiş, doruk ise **kendini hafifletmek**: asılıyken kollarına 499 N biniyor, gövdesini ters yöne 3,00 m/s salladığı 0,9 saniyelik pencerede 157 N'a iniyor ve kendini o pencerede yukarı atıyor · sayaç metinsiz ÜÇ kanal: adım boyu/gövde çöküşü · emniyet halatının SARKMA DERİNLİĞİ (doğrudan gravimetre) · göbekteki volanın parlak çentiği (S2'de 1,5 tur / 10 s, S4'te yarım tur, S5'te DURUYOR) · dramatik ironi taşıyıcı **② ZEMİN OKUR**, asimetri anı **0:24,6** (güvertede beş kayıp cıvata, beşi de yuvasından 60 cm AYNI yöne yatmış; o kendi botlarına bakıyor) · ikinci görsel şok S3: kendi bıraktığı cıvata 0,97 s'de düşüp **62 cm yana** iniyor · merkezi seçim S4 40,4-41,6: emniyet halatını açmak — bedel aynı karede (serbest uç 58 cm yana iner ve artık hiçbir şeye bağlı değil) · final DÖNGÜ + TWIST: merdivene tırmandıkça Coriolis onu yandan itiyor, **merdiven dümdüz, gövdesi 11,7° eğik** · risk **4/12** (Kart 3·4·5·9); **Kart 6 tasarımla kapalı** (vakum + işlenmiş metal: toz/duman/kıvılcım/enkaz 0 kare) ve **Kart 9 YAPISAL olarak kapalı** (yıldız dönme EKSENİNDE, kadraj dışı; adamın bütün hareketi eksene DİK — ışığa doğru koşmak güverteden çıkmak demek) · ⛔ **İLK TASLAKTAN ÇIKARILAN ŞEY DERSİ KAPATTI**: halkanın etrafında altı uzun sıçrayış (her biri 1,87 s havada) ÇIKARILDI, çünkü 60 saniyenin 16'sında havada duran gövde D23 + D12/D44'ün doğrudan tetikleyicisidir; yerine güverte altı el ele geçiş kondu ve havada geçen toplam süre **2,1 saniyeye** indi · ⚠️ gerçek 1 numaralı risk kartlarda yok ve dosyada tanımlı: **güvertenin başın üstünde KAPANMASI** (model "koridor" görünce düz koridor üretir; "corridor/tunnel/hallway/trench" kelimeleri 18 promptun hiçbirinde geçmiyor, kapanma her promptta SAYIYLA ve KANITIYLA yazılı) ve **gölge içine dolgu girmesi** (vakum: mutlak siyah, E bloğunda ffmpeg ile ölçülüyor — YAVG > 16/255 → sahne reddedilir; ⚠️ bu eşik THE THIN ROOF'un TERSİDİR) · lens kilidi **24 mm + 75 mm küresel** (32 mm geometrik olarak yetmiyor, hesap dosyada) · kurulum A-B-C-B-C-A, 3 açı tipi, ölçek merdiveni WS·MS·WS·CU·WS·EWS · ⛔ **ÜRETİM SIRASI: S0 İLK** (halka kapanmıyorsa film üretilmez), sonra S4 · ✅ prompt_kontrol.py: **GO — 0 BLOCK / 0 FIX** (ilk koşu 1 FIX: nesne-göreli taraf + metin yasağının KAPSAMI [D138] — kapı kaydı dosyada); video 2.474-2.580 bandın TAM içinde, image 6.438-6.670 (**depodaki en yüksek değer**; sebebi ve kısaltma sırası dosyada) · ⭐ **PROMPT_QA rubriği üç GERÇEK bulgu verdi ve biri depoda YENİ bir vakadır:** aksan renginin adı **"oxblood"** idi ve 18 promptun 14'ünde POZİTİF tarifin içinde geçiyordu — YASAK LİSTESİ TUZAĞI'nın [REHBER §7] ilk **RENK ADI** vakası; sınıflandırıcı "no" önekini değil KELİMEYİ okur, renk **"deep maroon"** yapıldı. Ayrıca karakter bloğundaki **"no weapon"** silindi (0 kare silah taşıyan bir yasak, koruduğu şeyi üretilemez kılar) ve video promptlarına **açı sözlüğü** (LOW-ANGLE / EYE-LEVEL / HIGH-ANGLE) eklendi — imaj promptlarında vardı, videolarda yalnız YÜKSEKLİK yazılıydı ve model kelimeyi okur · ⛔ **SPEC AYRI DOSYADA: `THE_HEAVY_SIDE_QA_SPEC.md`** [D117] — filmle AYNI GÜN indi |
| THE STRAIGHT LINE (dikey shorts) | shorts 9:16 | Dünya atm. (günümüz, kış ikindisi, −2 °C — henüz açılmamış çevre yolu; güneş ufkun 4° üstünde ve kadraj DIŞINDA) | 🆕 **Zombi / kaçış aksiyonu** (rafta olan §4.2 kartı dikey hatta geri açıldı) | Yazıldı, üretilmedi (23.08.2026) · ⭐ **risk 4/12 — EŞİĞİN ALTINDA, ve bunu MEKÂN SEÇİMİ sağladı**: aynı konseptin bina içi denemesi 6/12'ydi, açık yola taşınınca Kart 6b (katmanlı dünya) ve Kart 8 (kamera) düştü · ⭐ **depodaki ilk gerçek KOVALAMACA ve klasörün ilk DEVAM ZİNCİRLİ dosyası**: 6 sahne tek kesintisiz koşu, 5/5 kesme gizli geçişle (perde), her sahnenin ayrıca I2V DEVAM sürümü var · ⭐ **6/6 TAM LOCKOFF — depodaki en yüksek oran**, filmde tek kamera hareketi yok; aksiyon Z ekseninden ve kadrajı kesen geçişten gelir · mekanik **EKSİK SERBESTLİK DERECESİ**: takipçiler daha hızlı (5,8'e karşı 4,4 m/s) ama DÖNEMEZ ve FRENLEYEMEZ; kadın onları geçmez, 0,9 m'lik yanal adımla ıskalatır · novum taşıyıcısı KATI (beton bariyer bloğu × etrafından dönme jesti) → D73 tuzağı elendi · sayaç metinsiz ve KALAN BLOK sayısıdır: 3→3→3→2→1→**0** · gerçek risk kartlarda yok: **koşan figürün eklemlenmesi [D18]** — elenemez, bütçelendi (tam sprint + kontra ışık + düz yörünge; shambling 6/6 yasak, yüz 0 kare) · temas 0 kare (en yakın 1,2 m) · araç/su/yara/kan/silah/patlama 0 kare · ekranda metin 0,0 sn KONSEPTLE kapatıldı (yol açılmamış: şerit çizgisi, levha, reflektör yok) · merkezi seçim S4 (uzanan elin geri çekilmesi, bedel aynı karede) · doruk S5 = dördü birden son bloğa, hepsinin başı ona dönük (S0 tohumunun karşılığı) · final DÖNGÜ + TWIST, çıplak yolda · üretim S0'dan (ıskalama) başlar · ✅ prompt_kontrol.py: **0 BLOCK / 0 FIX — GO**, 6 video promptu 2.090-2.257 karakterle bandın içinde; image promptları 5.421-5.669 ile depodaki en uzunlar (kayıt ve kısaltma sırası dosyada) |
| **THE ROSE COAT** | 2-4 dk | İnce atm. (🆕 GÜL RENGİ TOZ OVASI: %1,2 basınç, 0,40 g, 40 saatlik gün — yıldız 6,0°→10,2°, EKRAN-SOLDA) | Bilimkurgu (keşif / bakım işi) | Yazıldı, üretilmedi (25.08.2026) · 13 × 10 s = 2:10 · 0 kesme · 13/13 sabit lockoff · 0 replik · risk 5/12 · ⭐ **deponun İKİ FİGÜRLÜ ikinci uzay filmi ve §4.1'in "tek kâşif" kilidini BİLEREK kıran ilk film**: novum "kendi sırtına ulaşamamak"tır ve tek kişiyle kurulamaz; bedeli §0.8b'de altı satırlık İKİ FİGÜR BÜTÇESİ (kadro kanalı · kadraj ayrımı · ortak yüz bütçesi · temas · biniş/koşu · yüz sayısı) · ⭐ palet = sayaç (tek doygun renk iki giysi) · SPEC ayrı dosyada [D117] |

| **YERÇEKİMİ** | 10-20 dk | Vakum (alçak yörünge 410 km · L1-L6 ışık takvimi gündüz→terminatör→gece→şafak→giriş) + F10 Dünya atm. zemin (kuru göl yatağı, SU 0) | Bilimkurgu (**sert uzay gerilimi** — novum yok, DURUM; §1 karar noktası bilinçli) | 🆕 28.08.2026 · 00_PLAN (ADIM 1) + README (ADIM 2) yazıldı; REFERANS_PAKETI → fazlar TEK TEK → SPEC sırada · 120 × 8 s = 16:00 · 3 perde × 10 faz (3-4-3) — format varsayılanı, Second Ship'in 10 s sapması ALINMADI · yapı kaynağı: Gravity (2013) dört raporlu yapı sökümü (`URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 2 — oran seti · bayrak yarışı iskeleti · sayaç kadansı · zaman sıkıştırması dersi) · ⭐ **formatın ilk İKİ KARAKTERLİ→TEK KARAKTERLİ filmi**: feda S43 (5:36 = %35,0; gövdenin son karesi S45), sonra tek insan; kadro "2" sahnesi 14/120 · TEMA FEDAKÂRLIK (S30 · S43 · S84 · S117) · 39 replik (sayının tek yeri film README §REPLİK LİSTESİ), A yalnız kask kapalıyken (6), kasksız replik 0, sayılar MACHINE'de, ekranda ağız 0 · ⚠️ altı bilinçli sapma planda yazılı: iki karakter (tür kartı) · B'nin MMU sırt çerçevesi (D79) · iç fazlarda kasksızlık (YANASMA §2.2⑤) · kapalı final bedeli · sert kulvar · kapak anı S1 · ⚠️ **Gravity'nin ölçülmüş fizik ihlali KOPYALANMADI**: feda gerilimi istasyonun **6°/s** dönüşünden (merkezkaç) + sökülen halat demeti sayacıyla (3→2, üçüncü düşüş YOK) kurulur — ⭐ 29.08'de F4 yazılırken hesap yapıldı ve ilk sayı (2°/s) reddedildi: 12 m halatın ucundaki 120 kg'a ~2 N düşüyordu, halat katını sökmez, yani o sayıyla sahne kopyalanmayacağı yazılan ihlalin kendisi olurdu; 6°/s ~16 N verir ve aynı kuvvet gövdeye yakın olan A'ya ~2 N düşer → **feda karakterden değil KONUMDAN doğar**; kalan iki katın TUTMASI (S46) hesabın kanıtıdır · su 0 · ateş 0 (yangın → basınç kaybı; atmosfere giriş içeriden) · canlı 0 · patlama 0 · risk 7/12 tetiklendi (Kart 3·4·5·6·7·9·10) → Kart 9 tasarımla kapalı (kamera hedefte), Kart 10 prompt kuralı → çekirdek 5/12 TAM EŞİK (Blue Drift profili) · kartlarda olmayan 1 numaralı riskler planda: iki gövdeli sıfır-g (tek vektör) · D23 rijitlik · dalga anı · politika sözlüğü · doruk S94-96 rampası, imza S102 YERÇEKİMİ YAĞMURU (8 varyasyon), tek Overview S68, final S120 held frame |
| **THE PAYLOAD** | 3-5 dk | İnce atm. (Mars 0.38 g · Acidalia güney kenarı, düz ova, geç ikindi · BÖLGESEL TOZ FIRTINASI CEPHESİ 2 km · 40 km/s) + vakum/0g (alçak Mars yörüngesi) | Bilimkurgu (ayrılış / insan-makine sınırı) | **YAZIM TAMAM (31.08.2026): PLAN + PART_A + PART_B + KAPAK + QA_SPEC [D117 · D142 E bloğu 11 makine kapısı, kuru koşu ffmpeg 8.1]** — sahip talebi: *"Mars'ta geçsin, 24 sahne; ilk partta fırtına çıksın, adam hızlıca üsse gidip hazırlansın, part 2'de uzay gemisiyle çıkıp yıldızlararası gemiye bağlansın"* · ⚠️ **SAHNE SAYISI 24 (12+12), klasör README'sinin sayısı** — §2.3 kartı 25/4:09 der, ikisi çelişir ve çelişki depoda duruyor; bu film README'yi izler: 9 s + 23 × 10 s = **239 s = 3:59**, orta nokta (S12 · 1:59) filmin matematiksel ortası · novum FİZİKSEL YASA, gerçek mühendislik (NEAR PASS / FROST LINE sınıfı): **kütle bütçesi korunur** — insansız örnek-dönüş teknesi kişi değil KÜTLE taşır; taşıyıcı ön iniş bacağının CİLALI MİLİ × kaldırma jesti: iki parmak (S4) → bir el (S8, dokuz kasa çıktı) → yine iki parmak (S12, adam yattı); 6 sahne · 3 nesne (amortisör · kasa · beden) · TEMA: **İNSAN-MAKİNE SINIRI** — depoda İLK (§3c'nin hiç kullanılmamış listesinden; §4'e göre YATAY/süreç teması) · cümle *"Makine kimi taşıdığını bilmez; yalnız ne kadar taşıdığını bilir."* ⛔ takas kalıbı değil, SINIR cümlesi · sahne indeksleri S5·S6·S10·S11·S12·S17·S21·S23 · motif: ÖZDEŞ TEKRAR EDEN BİRİM (12 panel sırası → 4 kelepçe yuvası → mastın 3 eşit adımı → 12 rıhtım) + STAKATO(makine) ↔ SÜREKLİ(insan) + ETİKETSİZ DÜNYA (metin yasağının POZİTİF hâli: raf içeriğini YERİNDEN bilir [D59]) · üç METİNSİZ sayaç: gölge cephesi (12 panel sırası sırayla söner, geri yanan 0) · mastın üç eşit adımı · amortisörün parlak bandı (tek TERSİNE DÖNEN sayaç, dönüşü kanıt) · cihaz ekranı/gösterge 0 → KART 5 düşer · ⭐ fizik imzası **FIRTINA İTEMEZ**: %0.6 basınçta kuvvet yok — S3 kanıt sahnesi (masttan sarkan ip akan gökyüzünün önünde DİK ve HAREKETSİZ), dokuz kasa kalkışın altında bile devrilmez; THE BLIND RETURN'ün kuralı burada NOVUMUN yanındaki kanıt olarak sahneleniyor · CENTRAL CHOICE S7-S10: dokuz yıllık numune kasasını kendi eliyle çıkarıp toza dizer — **kendini işin yerine koyar** (LOW POWER'ın fedakârlık kalıbının TERSİ; kamera yargısız) · bedel S10'da ve S12'de ateşin altında görünür · doruk S20 (3:19-3:29): TEMAS T+6.0 · 0.2 m/s · 2 cm oturma · sekme 0 · dış ses SIFIR · tutulan nefes bırakılır [YANAŞMA §1.2 V5, kamera RIHTIMDA · D104 panzehri] · kenet S21: TAM 4 kelepçe, üçüncüsü yarım saniye duraksar · yanaşma seti V1-V6 uygulandı ve **iki gövde tek karede yalnız S18'de** (oran cümlesi + hangi-uç-önde + kesir merdiveni; tekne 1/29 — güve ve katedral duvarı) · kalkış S12 [D127 · ⛔ D148]: ateşleme T+3.5 · kesilme T+4.5 · kadrajı üstten terk T+9 · **bacaklar HİÇ kıpırdamaz, alev aralarından geçer** (SKYLIGHT S28'in ölçülmüş hatası yapısal olarak kapatıldı) · aynı karede İKİ TOZ REJİMİ (balistik yay ≤2 s ↔ yatay laminer akış) · 0 g nesneyle [D23·D149]: kargo kayışı ucu + çekirdek tüpü süzülür, BEDEN kayışlı kalır · hook ÖRÜNTÜ KESİNTİSİ + YAKLAŞAN KÜTLE (katalizör 0:02.5 gölge hattı) · KAPAK ANI S0 · 0:07 (PAKETLEME §1 bandının İÇİNDE) · dramatik ironi ① arka plan, asimetri anı 0:04 · tohum S3 (0:29-0:39 açık yük kapağı + kasa rafı → final o kapağın lombozu) · final MUĞLAK + tohum, huşu S18'de ödenir (⚠️ §2'nin 3-5 dk için önerdiği TWIST bilinçli olarak alınmadı, gerekçe planda [D74]) · S0↔S23 ölçek aynası (kadrajı dolduran kahverengi kütle ↔ kara gövde; tek insan işareti = lomboz) · 24 × lockoff · 0 kesme · TAM SESSİZ (insan 0 · makine 0 · TELSİZ 0) · **insansız 6 sahne** (S12·S16·S18·S20·S21·S23 — ikinci yarıda insan/makine sahne sahne almaşır; KART 10'un bu filmdeki maliyeti kayıtlı) · 13 kurulum / 4 açı tipi / 2 bilinçli şok (S0→S1 · S20→S21) · eş kadraj S11↔S13↔S15↔S22 · S17↔S19 · S16↔S18↔S23 · S4↔S8 · ⚠️ risk 7/12 (kask · figür · parçacık · katmanlı · kamera · mıknatıs · insansız) — EŞİĞİN ÜSTÜNDE, kabul edilmiş maliyet (talebin kendisi bu malzeme); su · canlı · diyalog · ekran · değişken süre SIFIR; kartlarda olmayan 6 risk çözümlü (amortisör render'lanmama · cephe dalgalaşması · fırtınanın itmesi · D148 bacak · dört boş yuvada ikinci figür · gemi ölçeği) · ✅ **prompt_kontrol.py: 3 dosya · 0 BLOCK · 0 FIX · 3 GO** — video 24/24 bandın içinde (2.414-2.600), image gözlem; tek gözlem kurulum sayısı (dosya başına 8 ve 7, bant 6) ve gerekçesi PART dosyalarının ⑫ maddesinde [D74] · ⛔ SPEC AYRI DOSYADA (`THE_PAYLOAD_QA_SPEC.md`) — MOD D koşulacak · 🎵 **İKİ MÜZİK ✅ 31.08** (sahip talebi "iki müzik, viral olacak" — kurguya TEK skor girer, ikisi AYNI ızgarada, A/B karşılaştırması bedava): **A-SKOR** `THE_PAYLOAD_MUZIK.md` — ⭐ deponun ilk TAM ANEMPATİK skoru [§9]: sayan tık hiçbir olaya tepki vermez, ateşleme bile BİLEREK ızgara dışı; 72 BPM'de her sahne 12 vuruş ve **on ikincisi hiç çalınmaz** (filmin 12 panel sırası ↔ 12 rıhtım düzinesi), 96 BPM B1/B2, ızgarasız koda; üç sessizlik: hook · MECO 2:26.5-2:39 · **doruk 3:06.5-3:39 (32.5 s — temas ve dört kelepçe müziksiz** [YANAŞMA §2.1]); tek çözülme 3:55.0 = on ikinci vuruş, lombozun yandığı kare · **V2 VİRAL** `THE_PAYLOAD_MUZIK_V2_VIRAL.md` — 120 BPM tek grid (ızgara sıfırı 1.0 s, bütün sahne sınırları ölçü çizgisi), 12'lik ostinato kesmeye karşı kayar ve üç sahnede bir hizalanır (7 kez), katman EKLER, **tek hit point 2:03.0 ateşleme düşüşü** [§13'ün izin verilen tek istisnası], MECO tek ölçü, doruk sessizliği 22 s, koda A ile birebir + **dikey/kısa kesit penceresi ×3** (1:59-2:09 kalkış · 3:19-3:29 temas · 0:00-0:09 hook) · ⚠️ "ne satın alıyor" tablosu dış araştırmadır [FINAL §5], bu depoda ölçülmedi · ⏳ üretim yok |

| **THE COLD WELD** | 2-4 dk | 🆕 **VAKUM + TEMİZ METAL (soğuk kaynak)** — havasız ay yüzeyi (0,30 g · atmosfer yok · gölge içi mutlak siyah · yıldız 4,2° EKRAN-SOLDA sabit · krater gölgesinin kenarı 0,40 m/s ile ilerler) → §3.8 | Bilimkurgu (keşif / aksiyon) | Yazıldı, üretilmedi (01.09.2026) · 15 × 10 s = 2:30 · 0 kesme · 15/15 sabit lockoff · 0 replik · risk 5/12 · ⭐ **deponun EN YÜKSEK AÇI ÇEŞİTLİLİĞİ: 8 kurulum / 7 AÇI TİPİ** (önceki en yüksek 4'tü; 26.08 taramasında 107 dosyanın 43'ü 3'ün altındaydı) · ⭐ **YALNIZLIK** temasının depodaki ilk YATAY kullanımı (dikey THE THIN ROOF'tan sonra ikinci film), takas kalıbı kullanılmadan · novum SOĞUK KAYNAK: değen temiz metal tek parça olur, batık gemi tek bir metal resife dönüşmüştür · sayaç 2 avuç → 0 · SPEC ayrı dosyada [D117] · prompt_kontrol: 0 BLOCK |
| **THE STILL SWARM** | 2-4 dk | Vakum (§3.1) — açık boşluk, serbest düşüş 0 g · atmosfer yok · TEK baskın yıldız kadrajın sağ üst köşesi DIŞINDA, hedefle AYNI yönde (→ KART 9 ışık mıknatısı yapısal olarak elendi) | Bilimkurgu (aksiyon / ilk temas) | Yazıldı, üretilmedi (01.09.2026) · 14 × 10 s = 2:20 · 0 kesme · 14/14 sabit lockoff · 0 replik · risk **4/13** (eski skalada 4/9) · ⭐ **İLK TEMAS temasının depodaki İLK kullanımı** — §3c'nin "hiç kullanılmamış" listesinde kalan tek tema; §4 süre-tatmin kuralına BİLİNÇLİ SAPMA (dikey tema, yatay film), gerekçe ve panzehir planda · ⭐ deponun **ilk 0 g / serbest düşüş** 2-4 dk filmi · novum FİZİKSEL YASA: kabuğa giren her katı cisim hızının tamamını 0,15 s'den kısa sürede kaybeder ve asılı kalır — etki-tepki çalışmaya devam eder, o yüzden ilerlemenin tek yolu kütle atmaktır · NOVUM TAŞIYICISI 30 cm çelik kelepçe × geriye fırlatma jesti, TEK KARE S6 · 1:04 (taşıyıcı kadrajın 1/7'si, rakip olay 0) [D157] · metinsiz sayaç 8 kelepçe → 0 (monotonik) · doruk S11 = geldiği şeyi fırlatmak, bedel aynı karede · final TWIST + LOOP, S0 ↔ S13 eş kadraj çifti D153 protokolüyle (S13 imajı S0'ın ONAYLI karesinden türetilir) · **uzaylı ANATOMİ olarak 0 kare** — KART 2 (canlı 🔴) ve uzay operası yasağı birlikte elendi; varlık yalnız kuralla ve S13'teki yönle vardır · 7 kurulum / **6 açı tipi** · 2 bilinçli ölçek şoku (S6→S7 orta nokta · S10→S11 doruk) · SPEC ayrı dosyada [D117] · ✅ prompt_kontrol.py: **0 BLOCK**, iki FIX uzunluk bandı, gerekçesi planın PROMPT KAPISI bloğunda |

| **THE BENT GRASS** | 2-4 dk | ⭐ **§3.3 DÜNYA ATMOSFERİ — kartın İLK FİLMİ** (0,95 g · 0,90 atm solunabilir · +14 °C · tek güneş · gerçek rüzgâr): kart 26.08.2026'dan beri ⏸️ "kullanımda değil" damgalıydı ve **doğrulanabilir referans filmi YOKTU** — kartın kendi satırı "bu ortamda film yazılırsa ilk film yeni referans olur" diyor [D74]. Ufka kadar tek tür ot ovası; toz hızlı çöker · gölge YUMUŞAK ve bu MEŞRU [D41] · dolgu ışığı VAR · dış ses NORMAL. ⛔ Vakum negatif bloğu bu filme YAPIŞTIRILMAZ | Bilimkurgu (sert uzay gerilimi / ilk temas) | Yazıldı, üretilmedi (09.09.2026) · 14 sahne / 28 prompt / 2:20 (10 s hook + 13 × 10 s) · 0 kesme · 14/14 lockoff · **0 replik** · novum FİZİKSEL YASA: *ezilen ot bir daha kalkmaz; ezik sap gümüşe döner ve o hat sürünün yemek yoludur* — taşıyıcı EZİK OT ÇİZGİSİ, kanıt HAREKETSİZLİK (dalga geçer, hat kıpırdamaz) · TEMA **ZAMAN** · risk **9/14**, eşik aşıldı → malzeme 4 kalemde azaltıldı (parçacık 0 · tek biyom · 0 replik · sabit ızgara), 2 kart tasarımla sıfırlandı · ⭐ **DEPONUN İLK ÇOĞUL UZAYLISI**: `UZAYLI_VARLIK` §0① TEK VARLIK kuralından bilinçli sapma [D74] — çoğul TÜR değil BİREY olarak çözüldü (tek şablon · tek ihlal · sayı kilidi: S7:3 · S11:1 · S12:3 · tam gövde ≤2 çekim ve ≤6 s · yörünge yayı 0°) · ⛔ REFERANS PAKETİ sahibin kararıyla YAZILMADI (T1 ve T4 doğru; biçim kilidi METNE indi, gerekçe planda [D74]) · ✅ `prompt_kontrol.py` klasör modu **0 BLOCK · GO** (kapı 6 gerçek hata yakaladı, altısı da düzeltildi — biri D79 ↔ sırt paketi ÇELİŞKİSİYDİ; video 2.998-3.875 bandın üstünde, aritmetik gerekçe planda) · SPEC AYRI DOSYADA + `QA_PROMPTLARI/FILME_OZEL/THE_BENT_GRASS/` paketi ÜRETİLDİ [D165] → **MOD D koşulacak** |

| **THE GREEN CEILING** | 3-5 dk | 🆕 **İKİ ORTAM KARTI SIRAYLA** — §3.4 KALIN ATMOSFER (3,2 atm ≈ 3,9 kg/m³ · 0,42 g · solunamaz → vizör %100 kapalı ama optik BERRAK) S0-S21, sonra §3.1 VAKUM S22-S24; ⛔ SINIR SAHNESİ S21'dir ve orada §3.4 GEÇERLİDİR (araç hâlâ atmosferin içinde). Kapalı kanopi bir KAPAK gibi çalışır; yatay rüzgâr kartın dediği gibi YAVAŞ, kimseyi savurmaz | Bilimkurgu (hayatta kalma / kaçış) | **YAZIM TAMAM (10.09.2026): §2.0'ın SEKİZ dosyasından YEDİSİ yazılı + REFERANS_PAKETI `⬜ BEKLİYOR`** — PLAN + BOLUM_1 + BOLUM_2 + KAPAK + MUZIK + YAYIN_PAKETI + QA_SPEC [D117 · D165 QA paketi PAKET_1..12 ÜRETİLDİ] · sahip talebi: *"bol ormanlı bir gezegende iki astronot, bir anda sert bir fırtına, acil kalkış, yıldızlararası gemiye bağlanıp gidiyorlar; havalı modern astronot kıyafetleri"* · 25 sahne (13+12) · 50 prompt · 9 + 24×10 = **249 s = 4:09** (§2.3) · 0 kesme · 25/25 lockoff · **0 replik** · **0 canlı** · ekran metni 0,0 s · ⭐ **NOVUM'UN DOĞUŞU BİR D74 YENİDEN TANIMIDIR:** sahibin "sert fırtına"sı §3.4'ün *"rüzgâr YAVAŞ, kimseyi savurmaz"* satırıyla çakıştı; fırtınanın şiddeti YATAY eksenden **DİKEY eksene taşındı** ve aynı kartın *"Kaldırma ⭐ GERÇEK — Arşimet"* satırı yeni tanımı zaten meşru kılıyordu. Novum İCAT EDİLMEDİ, kartın kendi sayılarından türedi (emsal: THE COUNTED TURN §3.7) · **NOVUM: zemin bıraktığını geri vermez, YUKARI verir** · taşıyıcı **düz gri YÜK KASASI × avuçtan bırakma jesti** [D157] · kural 8 sahnede 4 nesnede kanıtlanır ve KARŞIT KANIT aynı karede: toz 3 saniyede yere oturur, levha yükselir · ⭐ aritmetik ÖLÇÜLDÜ, yazılmadı: ½ρv²C_dA = mg → v_Dünya/v_gezegen = √[(1/0,42)×(3,9/1,225)] = **2,75**, yani ~10 m/s burada ~27,5 m/s'nin işini yapar (ilk elle yazılan "26 m/s ↔ 2,8×" çifti birbirini tutmuyordu, formülle koşturulunca yakalandı) · TEMA **ENTROPİ** — *"Bu ormanda zemin hiçbir şeyi tutmaz."* ⛔ TAKAS kalıbı değil, TANIM cümlesi [§3c] · motif S1 · S9 · S19 · S24 · **B5:** İSTEK üç yük kasasını gemiye TESLİM ETMEK (bir İŞ) · ENGEL ① süre ② kütle (aynı engelin iki yüzü DEĞİL) · **BEDEL S19**, ekranda **S20** · MUHATAP ikinci insan, son karede kadrajda · **AYRILIK S19** ve ayrılık novum taşıyıcısıyla AYNI NESNEDE · B2a/B2b S23 (ilk yanaşma tutmaz) · çift **KAFİYE** S0↔S24, değişen tek değişken NESNE (avuçtaki levha VAR ve gidiyor ↔ avucun altındaki kelepçe BOŞ) · final **TWIST + tohum**, **FİNAL VURUŞ KANITI BULUNMAYAN: 245 s'de tam 3 kelepçe ve tam 2 kasa** [D141] · ⭐ **KURULUM İSKELETİ** A B A B D C D F F D E E E G H G H D H J H D I M L → 12 kurulum / 5 açı tipi / **küme 2 ✅ · dönüş %45,8 ✅** / bilinçli şok 1 (S21→S22 ortam sınırı) · ⭐ **İKİ FİGÜRÜN AYRIMI RENKLE DEĞİL GEOMETRİYLE** kuruldu (komutan: düz sırt + tek dikey dikiş + paket YOK; mühendis: dikdörtgen sırt bloğu + U profil) çünkü referans paketi yok ve BLACK CRADLE'ın renk-tek ayrımı ölçülmüş olarak çöktü; dizilim kilidi komutan screen-LEFT 16/16 sahnede · öznitelik pencere başına EN ÇOK 3 [D167] · risk **11/14** eşiğin üstünde, dokuz kalem SIFIRA indirildi ve üçü gerekçeyle kabul edildi · 🎵 MUZIK ✅ (48 BPM = 10 s başına tam 2 ölçü · ⭐ızgara 0'a değil **9,0 s'ye çapalandı** çünkü hook 9 s · ⭐ **ANEMPATİK** skor — deponun hiç kullanmadığı araç; tek istisna S17 · müziksiz sahne **S21**, müzik **207,5 s**'de BİTER yani sahne başlamadan 1,5 s önce, kurguda HARD MUTE [D180 · D122 ile hesaplatıldı] · 45 Hz + 90/135 Hz missing-fundamental eşlikçi) · 📣 YAYIN_PAKETI ✅ tamamen İngilizce (VERIFIED SCIENCE: NOAA/NWS Vivian SD 23.07.2010 dolu tanesi 20 cm / 0,88 kg · sürükleme-yoğunluk türetmesi · Cassini-Huygens Titan 1,45 bar / 0,14 g · kapalı kanopi %1-2 ışık geçirimi) · ✅ **prompt_kontrol.py KLASÖR MODU: 50 prompt · 0 BLOCK · GO** — ilk koşu 3 BLOCK verdi: ㉑ çıplak-deri negatifi 2/3 bölge (34 prompt) · ⑳b *"there is no open sky"* cümlesi DEĞİŞİM KAPISI'nı 'open' üstünden ateşliyordu · ⑰ B5 satırları VARDI ama biçim okunmuyordu ("B5 ✅ İSTEK:" — ✅ kapının ön ek sözlüğünde yok). FIX olarak kapatılanlar: *"bare wrists"* mühürlü filmde çıplak deri okutuyordu [D175] · insan sayısı imzası ("human count locked at two") · metin yasağının KAPSAMI §5 biçimine çevrildi [D138] · insansız sahnelerin TEK POZİTİF Style satırına iki imza eklendi (KART 10'un uzun-NEGATIVE yasağı korunarak) · ⑮ D139 sırt POZİTİF yüzeyi · ⑪ çapasız "toward" · ㉒ IŞIK bloğunun yüzeye renk atması [D176] · ve **aynı harf aynı kurulum**: 'D' beş sahnede iki imza ölçtü çünkü kamera cümlesindeki ÖZNE UZAKLIĞI değişiyordu (20/60/45 m) — uzaklık ölçek cümlesine taşındı · ⚠️ ayakta kalan tek uyarı BİLİNEN YANLIŞ POZİTİF: dosya modunda ⑩④ 25 harfi 13/12 promptla karşılaştırıyor (THE KEPT LIGHT emsali) · 📏 image 2.167-6.066 · video 1.499-4.008, tavan 4.300 AŞILMADI · ⏳ üretim yok — **ÜRETİM SIRASI planda [D168]: S0 novum kanıtı → S21 doruk → S19 seçim → S24 kapanış → S23 temas → kalanı**; İPTAL KAPISI S0 (levha yukarı gitmiyorsa film üretilmez) |
| **THE TETHERED MASS** | 2-4 dk | §3.2 UZAY / YÖRÜNGE KARTI — Düşmekte olan koloni-tarım istasyonunun periapsisi Dünya atmosferine girmiştir. Çekici astronotu momentum aktarım halatıyla kendi gemisini feda ederek istasyonu kurtarır. | Bilimkurgu (yörünge fiziği / fedakarlık) | **YAZIM TAMAM (10.09.2026): SEKİZ DOSYA TAM + REFERANS PAKETİ KAPI 0 ONAYLI** — PLAN + BOLUM_1 + BOLUM_2 + KAPAK + MUZIK + YAYIN_PAKETI + QA_SPEC + REFERANS_PAKETI · 16 sahne · 32 prompt · **160 s = 2:40** · 0 replik · TEMA **BEDEL + İNSAN-MAKİNE** · NOVUM: **Momentum Exchange Tether** · B5 S11 seçim · prompt_kontrol 0 BLOCK. |
| **THE DRY ANCHOR** | 2-4 dk | 🆕 **§3.2 İNCE ATMOSFER — kartın YATAY hattaki İLK filmi** (610 Pa · %95 CO₂ · 3,721 m/s² = 0,379 g · gün ışığı %43 · toz ~1,5 µm · 30 m/s rüzgâr = 9 Pa): yağmur görmemiş toz ovası; saha mühendisi geminin dört ayağını hizalamak için çapa çakar, kazık her seferinde iner ve DURMAZ — tutan tek yer, hattın yetişmediği süpürülmüş taştır. | Bilimkurgu (zemin mekaniği / bedel) | **YAZIM TAMAM (10.09.2026): YEDİ DOSYA TAM · REFERANS PAKETİ ⬜ BEKLİYOR (sahip kararı, PLAN'da gerekçe satırı)** — PLAN + BOLUM_1 + BOLUM_2 + KAPAK + MUZIK + YAYIN_PAKETI + QA_SPEC · 14 sahne · 28 prompt · **140 s = 2:20** · 0 replik · TEMA **İNSAN-MAKİNE SINIRI** (S3·S4·S9·S11·S13) · NOVUM: **taban basıncı — yağmursuz toz sıkışmaz** · B5 BEDEL S9 (örnek kasası) · KURULUM İSKELETİ A A B C A B D C D D E E D A (küme 3 · dönüş %50 · açı tipi 3) · prompt_kontrol klasör modu **0 BLOCK** · QA paketi üretildi (aile: yatay). |
| **THE SOLAR MIRROR** | 2-4 dk | 🆕 **§3.1 VAKUM (YÖRÜNGE, 0 g)** — Düşük Dünya yörüngesinde HELIOSTAT S04 ayna segmentinin bakımını yapan astronot Mara, ayna yüzeyinde +30.000 saniye geleceği gösteren optik evre-konjugasyon anomalisi keşfeder. | Bilimkurgu (zaman / bedel / paradoks) | **YAZIM TAMAM (11.09.2026): YEDİ DOSYA TAM + REFERANS PAKETİ KAPI 0 ONAYLI** — PLAN + BOLUM_1 + BOLUM_2 + KAPAK + MUZIK + YAYIN_PAKETI + QA_SPEC + REFERANS_PAKETI · 12 sahne · 24 prompt · **120 s = 2:00** · 0 replik · TEMA **BEDEL + ZAMAN** · NOVUM: **30-Second Phase-Conjugate Optical Anomaly** · B5 S06 seçim · prompt_kontrol 0 BLOCK. |
| **THE SCOURED GLASS** | 10-20 dk (uzun uç, bant dışı — sahip izni 07.09) | §3.2 İNCE ATMOSFER (Mars 610 Pa · 0,38 g · 30 m/s = 9 Pa · toz elektrostatik) + §3.10 BASINÇLI İÇ (modül · gezici · yükseliş aracı) | Bilimkurgu (**sert uzay hayatta kalma draması** — The Martian ekseni; Suvin novum'u YOK: "kuru silme cama sürterek aşındırır" gerçek triboloji, ıslak silme çizmez ama su hayattır) | 🔧 **11.09.2026 · `yeni-film` akışıyla yeniden kuruldu** (ilk yazım 07.09 tek partta): TUR 16 dört derin araştırma (zaman merdiveni · triboloji · Mars bütçesi · kademeli görüş kaybı) → `00_ANALIZ/` (okuma 109/109 + 5/5 kayıt · hasat · konsept/risk 12/14 · sıralama · uyarı 🔴10 · S01-S12 çalışmaları) → `00_PLAN.md` + FAZ_01 (24 prompt satır düzeyinde düzeltildi, yeniden yazılmadı) + QA_SPEC güncellendi · **15 faz × 12 sahne × 10,0 s = 180 sahne = 30:00** (deponun ilk 30 dakikalık filmi) · OMNI 1.1 Flash I2V · tek insan, kadraj 180/180 · replik 2 (S4 telsiz post · S12 günlük OMNI) · ⭐ novum karesi S8 (klip içi 0→1 kademe, D157 tek istisna) · 12 kademeli cam merdiveni, faz sınırında · ÇAPA ÜÇLÜSÜ S151/S140/S180 · güneş tarafı sahne başına δ=90°−θ [D201] · kuşbakışı modül 215°/150 m · `prompt_kontrol` 0 BLOCK / 1 FIX (uzunluk bandı + D79 + kurulum 12 — üçü gerekçeli) · referans paketi ⬜ BEKLİYOR (KAPI 0) · FAZ 2-15 yazılmadı · üretim yok |
| **THE HARD DOCK** | 3-5 dk (24 × 10 s = 4:00, hook ayrı sahne değil) | §3.1 VAKUM (yörünge, volkanik gezegen üstü) + §3.10 kokpit (mühürlü giysi) | Bilimkurgu (sert) · yanaşma hattı (YANASMA V1-V6) | Yazıldı, üretilmedi — 11.09.2026 · tek pilot + akuzmatik gemi bilgisayarı (makine 8 replik, insan 0) · novum: SERT KENET — yaylı halka nominalin 5 katıyla porta sürülür, dört dikme çöker, kilit geri alınamaz · 7 kurulum, küme 2, dönüş %46, V3 1 kez, doruk port-kilitli (D104), vizör BERRAK düz panel · ⚠️ ilk taslak kart P'de BLOCK aldı ve aynı gün baştan yazıldı; prompt_kontrol klasör modu ✅ GO (dosya modu 2 FIX: uzunluk, D74) · referans paketi ⬜ TASLAK (KAPI 0) |
| **THE LOCKED PULSE** | 3-5 dk (9 s + 24 × 10 s = 4:09, hook S0 ayrı sahne) | §3.7 **VAKUM + DÖNME YERÇEKİMİ** — R 56,0 m basınçlı halka koridoru; otomasyon halkayı 2,0 → 4,0 RPM'e çıkarır (0,25 → 1,00 g, yalnız sahne sınırında kademeli, D200) + 1 dış vakum sahnesi (S13 hub'dan Overview, insansız, yıldız 24 °/s) | Bilimkurgu (sert) · tek mühendis + akuzmatik halka otomasyonu (makine 6 replik, insan 0) | Yazıldı, üretilmedi — 13.09.2026 · `/yeni-film` TAM akış (120/120 dosya · 5 film kaydı · 25 sahne çalışması); 12.09 taslağı (21 sahne) baştan yazıldı · tema **İNSAN-MAKİNE** (sayaçta en az kullanılan; motif S2 S10 S12 S18 S22 S24) · novum FİZİKSEL YASA, tamamen gerçek: dönen halkada bırakılan nesne bırakıldığı noktanın SOLUNA iner (Coriolis; yana sapma ⅓·(2h)^1,5/√R — dönme hızından BAĞIMSIZ; S2 anahtar 0,11 m · S15 levye 0,08 m) + ağırlık = spin (kayış T = 2π√(L/a) 4,0 → 2,0 s; alarm 2,0 → 1,0 s; hidrostatik baş → makine döngü basıncını hızla tutar) · B5: port sızıntısını kapatmak, altı kapsülü soğuk tutmak / otomasyon halkayı hızlandırır, port yakasının basınç kilidi yumruğunu soktuğu bileğe kapanır (S12 · 123,0 s) / BEDEL S22 · 224,0 s — kendi bilek halkasını açar, çıplak sağ el çıkar, eldiven yakada kalır / MUHATAP ortamın kalıcı parçası: 4,0 RPM TUTULUR + 7 yuvalı lamba dizisi 6 → 7 (S2 tohum → S23 · 233,0 s: makine eldiveni yedinci mühürlü kapsül sayar) · doruk S20 · 203,0 s: el fren çarkının bir avuç önünde durur, 2 s, geri çekilir (kurguda HARD MUTE 203,0-205,0; müzik 72 BPM anempatik nabız 19,0-197,5, doruk-bedel sessiz) · 10 kurulum (D74 ②), küme 3, dönüş %44, açı tipi 6, iskelet A B C D C E E C D H C G D X D G G J B J M A C C A, S24↔S0 kafiye · şerit G R G D T G G G G R G G R - D D S T R S K R B R B · prompt_kontrol KLASÖR modu ✅ GO · 0 BLOCK (dosya modu 2 FIX: uzunluk 3,2-3,8k + bölünmüş-film artefaktı, D74 ① ⑩) · PROMPT_QA_CRITIQUE FIX → 2 bilinçli sapma (S20 makro üçlüsü · S22 bedenden çıkarma = bedel; D74 ⑪ ⑫) · DIALOGUE_CRITIQUE ✅ GO · 03_PLAN_ONCESI 17/17 · üretim sırası REFERANS → S20 → S22 → S24 → S2 → S12 → S0 → S13 → S10 → kalanı · referans paketi 5 sayfa / 19 panel ⬜ TASLAK (KAPI 0) · YAYIN_PAKETI İngilizce · QA yok |
| **THE BURNING ENTRY** | 2 dk (12 × 10 s = 2:00, S00-S11) | §3.4 KALIN ATMOSFER (sert yörünge çöküşü, atmosferik giriş sürtünmesi, 1200 °C plazma ateşi) + §3.10 kokpit (yüksek G, plazma ışığı, siperlik çatlağı) | Bilimkurgu (sert acil hayatta kalma / yörünge çöküşü aksiyonu) | **YAZIM TAMAM (14.09.2026): SEKİZ DOSYA TAM + REFERANS PAKETİ KAPI 0 ONAYLI** — PLAN + BOLUM_1 + BOLUM_2 + KAPAK + MUZIK + YAYIN_PAKETI + QA_SPEC + REFERANS_PAKETI · 12 sahne · 24 prompt · **120 s = 2:00** · 0 replik · 0 tamir sahnesi · TEMA **BEDEL + DİRENÇ** · NOVUM: **Single Thruster Atmospheric Entry Stability** · B5 S08 acil fırlatma kararı · 4 kurulum (A-A-C-D-A-C-C-B-B-A-B-A), küme 3, dönüş %66.6 · `prompt_kontrol.py` KLASÖR modu ✅ GO · 0 BLOCK errors |
| **BENI_HATIRLAMA** | 8 dk (48 × 10 s VARSAYIM = 8:00, hook S0 içinde · 4 × 12 yazım dosyası — sahip kararı, kart 2 × 24 der) | §3.4 KALIN ATMOSFER (≈3 atm · 0,7 g · kum düzlüğü + fırtına) + yarık mağara iç hacmi + iniş aracı kokpiti | Bilimkurgu (yumuşak — hafıza · kayıp · iletişim) · tema KİMLİK · novum İLİŞKİ (yarı saydam kadın figürü = yavru canlının adamın hatırasından yansıttığı görüntü) | 17.09.2026 yeni rejim /yeni-film ile BAŞTAN yazıldı (hikâye onayı TUR 1/3) · 48 sahne tablosu + 5 kilit sahne + 43 kısa çalışma · 21 kurulum · KÜME 3 · DÖNÜŞ %48 · replikler post-dub (6) · prompt_kontrol klasör modu GO · referans paketi YAZILMADI (5/6 tetikleyici) · ⬜ K1 QA birimi · K2 S37 zincir modu · K3 figür probu · üretim 0 kare |
| **SUSMAYAN_NOBETCI** | 8 dk (48 × 10 s VARSAYIM = 8:00, hook S0 içinde · 4 × 12 yazım dosyası — sahip kararı, kart 2 × 24 der) | §3.1 VAKUM (alçak yörünge · 0 g · gezegen kenarı) + §3.10 BASINÇLI İÇ HACİM (çekici kokpiti · kaçış kapsülü · tahliye bölmesi) | Bilimkurgu (sert uzay gerilimi / yanaşma — aksiyon kulvarı) · tema İNSAN-MAKİNE · novum FİZİKSEL YASA (savaştan kalma uydu motoru yanan her şeyi 3,0 s'de vurur; iki soğutma kanadı açıkken ≈15 s ateş edemez) | 18.09.2026 yeni rejim /yeni-film ile yazıldı (hikâye onayı TUR 1/3) · 48 sahne tablosu + 5 kilit sahne · 18 kurulum · KÜME 4 · DÖNÜŞ 20/48 · kural 6 nesnede 6 farklı sonuçla kanıtlanır · 18 yanaşma sahnesinin her biri bir koşulu değiştirir · replikler post-dub (8) · prompt_kontrol klasör modu GO · referans paketi YAZILMADI (5/6 tetikleyici, D74 ⑥) · ⬜ K1 QA birimi · K2 S36-S37 zincir modu · K3 klip süresi · üretim 0 kare |
| **THE_FALLING_WORLD** | 8 dk (48 × 10 s VARSAYIM = 8:00, hook S0 içinde · 4 × 12 yazım dosyası — sahip kararı, kart 2 × 24 der) | §3.2 İNCE ATMOSFER (yüzey · taş ocağı · platform) + §3.10 BASINÇLI İÇ HACİM (galeri · gemi kabini) — ikisi de **0,30 g** (D74: kart Mars 0,38 g der, §3.10 0 g der) | Bilimkurgu (hayatta kalma / tahliye — halat kulvarı) · tema **GÜVEN** (depoda 0 kez · §3b'ye üçüncü aday etiket) · novum **İLİŞKİ TİPİ — deponun İLKİ**: bu dünyada kimse kendini kurtaramaz, her kurtuluş birini bağlayan hattın BAŞKASI tarafından ayrılmasıdır | 18.09.2026 yeni rejim /yeni-film ile yazıldı · ⭐ **hikâyeyi SAHİP yazdı** — 48 klibin olayı, sırası ve devamlılık notları birebir korundu, tek ekleme S40 AYRILIK (SAPMA 1, onaylı) · 48 sahne tablosu + 5 kilit sahne · **24 kurulum (tavanda)** · KÜME 9 · DÖNÜŞ 20/48 = %41,7 · 4 açı tipi · ardışık çift 47/47 bant içi · ⛔ **VİZÖR TAMAMEN OPAK** (D79 sapması — sahibin sert kısıtı): yüz 0 kare, lip-sync riski fiziken sıfır, kimlik yığını hiç doğmuyor, ⭐VİRAL'in YÜZ satırı YAZILAMIYOR · ⛔ iki SIRT ÜNİTESİ kimlik taşıyıcısı (D79/D139 sapması, sırt POZİTİF yüzey cümlesiyle yazıldı) · 1 numaralı risk S42 (hangi hattın ayrıldığı) A5'in beş sayılı kilidiyle kapatıldı · replikler post-dub (8) · **referans paketi 4 SAYFA YAZILDI** (sahip: "8 9 değil 4, ve hangi referans hangi sahnede") · prompt_kontrol klasör modu 0 BLOCK · ⬜ K1 QA birimi · K2 zincir modu · K3 klip süresi · üretim 0 kare |
| **THE_SLOW_RAIN** | 8 dk (48 × 10 s VARSAYIM = 8:00, hook S0 içinde · 4 × 12 yazım dosyası — sahip kararı, kart 2 × 24 der) | §3.9 KRİYOJENİK ORTA BASINÇ (95 K · 0,90 bar N₂+CH₄ · 0,38 g) — ⭐ **SIVI BANDI bu filmle açıldı** (kart "sıvı yüzeyde YOK" diyordu; metan yağmuru + göl yatağının dolması; kart notu sahip kararı ⬜) + §3.10 iç hacim (üs · istasyon, kask kapalı) | Bilimkurgu (hayatta kalma / taşıma) · tema **KİMLİK** · novum **YAVAŞ YAĞMUR** (fiziksel yasa: iri seyrek damla Dünya yağmurunun ~1/3 hızıyla iner, cephe gökte görünür; uçuş aynı fiziğin sonucu) | 22.09.2026 yeni rejim /yeni-film ile yazıldı · ⭐ **deponun İLK FİKİR TURU filmi** (HIKAYE_FIKIR_TURU 0.7a: 12 logline · 5 eleme · 3 aday · ONAY A TUR 1/3 · 2 SAPMA yeniden onaylı) · 48 sahne tablosu + 5 kilit sahne · 22 kurulum · KÜME 7 · DÖNÜŞ 20/48 = %42 · 6 açı tipi · ardışık çift 37/37 + 10 küme · şok 1 · 8 ⭐VİRAL (yüz+hareket) · referans paketi YAZILMADI (sahip) — kanat/kızak biçim kilidi ilk onaylı karelerle (S1 · S15), üretim sırası oradan · ⚠️ fizik dürüstlüğü: "asılı damla" yok, bilye boyu ~3 m/s (02_KONSEPT §3) · prompt_kontrol klasör modu 0 BLOCK / GO · ⬜ K1 QA birimi · K2 klip süresi · K3 §3.9 sıvı bandı kart notu · üretim 0 kare |
| **THE_STOLEN_SKY** | 16 dk (96 × 10 s = 16:00 · 8 BÖLÜM × 12 sahne · QA 4 PART + TAM FİLM · KILAVUZ §2.8) | §3.3 DÜNYA ATMOSFERİ (0,9 g · 1,0 atm) + §3.10 iç hacim + §3.1 vakum | Bilimkurgu (işgal altında tahliye / aksiyon) · tema **SORUMLULUK** · novum **Yörünge Kafesi** (kehribar lattice) | Yazıldı (20.09.2026) · OMNI 1.1 Flash I2V · 96 sahne / 192 prompt · 20 kurulum · KÜME 10 · DÖNÜŞ %37,5 · 8 post-dub replik · **VİZÖR TAMAMEN OPAK** · PART 1 (S00–S23 / 240 s) QA değerlendirildi (21.09.2026): ① KARE ⛔ TEKRAR (mod V), ② DEVAMLILIK ⚠️ ŞARTLI (7.6), ③ SES ✅ GO (8.9); master ölçümü verilmediği için ⑤ kesme yayılımı partiyi 🚨 GEÇERSİZ kıldı [D107] |
| **THE_LAST_GATE** | 16 dk (96 klip × tam 10 s = 16:00 · 8 BÖLÜM × 12 klip · 25 SAHNE · QA 4 PART + TAM FİLM · KILAVUZ §2.8) | §3.1 VAKUM (dış) + **§3.10 BASINÇLI İÇ HACİM — kartın BASKIN kullanıldığı İLK film, kartın referansı** (mikrogravite · gemi DÖNMEZ) | Bilimkurgu (hapishane gemisi kaçırma / kaçış aksiyonu) · tema **DAYANIŞMA** (aday etiket) · novum **SON GEÇİT** (sabit halkanın içindeki etkin açıklık monotonik daralır) | Yazıldı (30.09.2026) · ⭐ **hikâye SAHİBİN**: 724 satırlık `THE_LAST_GATE_KAPSAMLI_PLAN.md` referans alındı ve `00_ANALIZ/00_ON_PLAN/` altına taşındı · **96 klip / 92 üretilen / 184 prompt** (K01–K04 kurgu bloğu, yeni kare 0) · 16 kurulum · 5 kimlik + 1 varlık · **32 replik + 4 dış ses satırı** · vizör BERRAK · 21 sayfalık referans paketi (KAPI 0) · dört SAPMA kayıtlı (rozet → **metinsiz amblem dili** · kurgu bloğu · özel ad · savaş kartı kilitleri ödünç) · prompt_kontrol.py **klasör modu ✅ GO · 0 BLOCK**, 8 gerekçeli FIX (DÖNÜŞ %8-33 · kurulum 7-9 — on bir mekân, kapsamlı plan §13 "oran hedefi için rastgele imza aranmaz") · üretim 0 kare |
| **THE_FALSE_EARTH** | 32 dk (192 × 10 s = 32:00 · 16 BÖLÜM × 12 KLİP · 50 SAHNE (2-6 klip) · QA 8 PART × 24 klip + TAM FİLM · KILAVUZ §2.9) — ⭐ **deponun İLK 32 dk filmi** ve **ÇOK KLİPLİ SAHNE rejiminin ilk filmi** (22.09.2026 sahip kararı: son kare zinciri kalktı, SCENE ≠ CLIP) | §3.1 VAKUM (0 g · 0 kPa) + §3.3 GEZEGEN YÜZEYİ (0,98 g · solunamaz) + §3.10 BASINÇLI İÇ HACİM (1 g dönüşten · 101 kPa) — **üç rejim, asla aynı kadrajda** [D200] | Bilimkurgu (kurtarma / ilk temas — yanlış Dünya) · tema **FEDAKÂRLIK** (depoda 6. kez · sahip kararıyla bilinçli istisna, K7) · novum **İLİŞKİ TİPİ**: yapı gördüğü her şeyi yeniden kurabiliyor, görmediği hiçbir şeyi kuramıyor — ve geçidi açan eşleme görünmez bir iç durumdur; kanıtı MADDİ (kopyalanan lambanın camında FOTOĞRAF FLAŞININ lekesi) | 24.09.2026 yeni rejim /yeni-film ile yazıldı · ⭐ **hikâyeyi SAHİP yazdı** (`00_ON_PLAN/` tretmanı → 0.7a fikir turu atlandı, gerekçe onay dosyasında; ONAY 23.09.2026 TUR 1/3, SAPMA yok) · 192 satırlık sahne tablosu + 5 kilit klip · **SAHNE PLANI beyanı** (㉜ kapısı bu klasörde koşan ilk film) · dosya başına ayrı kurulum iskeleti (7 istasyon ailesi) · KÜME **YOK** (rejim gereği, ⑩④ küme dalı koşmuyor) · DÖNÜŞ dosya başına %42-%75 · her dosyada ≥3 açı tipi · ardışık aynı kurulum 0 · **VİZÖR OPTİK BERRAK** (D146: tek düz panel + görünür koyu çerçeve; D79 sırt düz) · ağzı okunan YALNIZ 4 klip (K057 · K059 · K163 · K164 — bilinçli istisna, PROB B kapısı) · 47 replik / 3 kanal (oda · telsiz · kayıt) · tek tam sessizlik K143 (kurguda HARD MUTE, modelden İSTENMİYOR) · **referans paketi 5 SAYFA / 18 PANEL YAZILDI** (PLAN 4 diyordu; 5. sayfa LAMBA, ölçülmüş biçim sapmasından — sahip onayı bekliyor) · QA SPEC ㉔ 7/7 makine çapası + ffmpeg 8.1 ile DOĞRULANMIŞ 3 kapı · 18/18 üretim öncesi kontrol · prompt_kontrol klasör modu **0 BLOCK / 0 FIX / 18 GO** · ⬜ K1b (10 s altı klip) · K9 (yaşlar) · K10 (anne ekranda) · P1 kapsamı · üretim 0 kare |
| **THE_COUNTED_RIVET** | 4 dk (24 × 10 s = 4:00 · 2 BÖLÜM × 12 KLİP · **7 SAHNE** (1-5 klip) · KILAVUZ §2.3) — ⭐ **ÇOK KLİPLİ SAHNE rejiminin ilk 4 dk filmi** ve deponun ikinci ㉜ klasörü | §3.6 SÜREKLİ BULUT / NÖTR YÜZERLİK (55 km bandı · 0,904 g · ≈0,5 atm yoğun CO₂) — ⭐ **kartın İKİNCİ filmi** (ilki LOSS_OF_LIFT, 21.08.2026); ufuk YOK · zemin YOK · güneş diski YOK · gölge YOK · toz YOK | Bilimkurgu (ölçüm işi / sert gerilim) · tema **İNSAN-MAKİNE** (S3·S5·S6·S7 · yatayda yasal dört temanın en azı: 6 kez, bu filmle 7 — Kimlik 7 · Fedakârlık 8 · Zaman 10) · novum **ÖLÇEK** (depoda 1/21 → 2/22): bağlandığı yüzey bir gövde değil, gövdenin bir DETAYIDIR ve bunu ancak düz bir kenarın altından ışık sızıp sızmadığı söyler — taşıyıcı çelik şerit (kol boyu) × şeridi yüzeye yatırma jesti | 25.09.2026 yeni rejim /yeni-film ile yazıldı · **konuyu SAHİP seçti** (üç aday ölçüyle sunuldu), hikâye fikir turundan geldi (12 logline · 5 eleme · 3 aday · ONAY TUR 1/3 + S5 SAPMASI TUR 2/3) · 24 satırlık klip tablosu + 5 kilit klip · **SAHNE PLANI: 1 3 4 4 3 4 5** · KÜME YOK (rejim) · DÖNÜŞ 14/24 = **%58,3** · 8 kurulum · 5 açı tipi · ardışık çift 23/23 bant içi · şok 1 (K15→K16) · ardışık aynı kurulum 0 · **VİZÖR OPTİK BERRAK** tek düz pane + kalın koyu çerçeve [D146] · **0 replik** (tırnak 0 karakter) · **0 ⭐VİRAL** — ⛔ kartın 4 adedinden ÖLÇÜLMÜŞ SAPMA [D74]: kapı iki kanalı birden ister (okunan yüz + hızlanan hacim), üç aday tek tek ölçüldü ve üçü tek kanalda kaldı · **referans paketi YAZILMADI** (sahip kararı, 6 tetikleyiciden 5'i doğru — biçim kilidi 24 klip boyunca yalnız METİNLE tutulacak, risk AÇIK) · ⭐ **filmin merkezî iddiası aritmetikle kapandı**: sagitta s ≈ c²/8R — 0,60 m şerit 2 m çaplı direkte 45,0 mm = 267 px, gerçek yüzeyde (R≈15 km) 0,003 mm = 0 px; mandalın kendi 0,30 m'lik çenesi yalnız 11,3 mm = 50 px gösterir ve dramanın fizik gerekçesi budur · ⭐ kanıt YALNIZ bu ortamda mümkün (gölgesiz her-yönden dolgu) · üç metinsiz sayaç (kanıt merdiveni · iniş hızı 40→25→18 s · ışık kademesi 0→1→2 monotonik) · **§3.6 kartının İngilizce PHYSICS/AUDIO cümle çifti bu filmde yazıldı** (PROMPT_HATA_ONLEME §2'de yoktu) · QA SPEC ㉔ 7/7 çapa + ffmpeg 8.1 ile DOĞRULANMIŞ 5 makine kapısı + 5 GÖZ KAPISI · 18/18 üretim öncesi kontrol · prompt_kontrol klasör modu **0 BLOCK / GO** (3 dosya-düzeyi FIX: ikisi bölünmüş-film artefaktı, biri yazılmamış referans şablonu — üçü de kayıtlı) · ⬜ K1 klip süresi [D124] · K2 vizör biçim kilidi üretimde ölçülecek · K3 K15 İPTAL KAPISI · üretim 0 kare |
| **GUNES_MEZARI** | 4 dk (24 × 10 s = 4:00 · 2 BÖLÜM × 12 KLİP · **7 SAHNE** (2-6 klip) · KILAVUZ §2.3) — ÇOK KLİPLİ SAHNE rejiminin **üçüncü** klasörü, 4 dk formatının ikincisi | §3.9 KRİYOJENİK ORTA BASINÇ (95 K · 0,90 bar · 0,38 g) — ⭐ **kartın KURU+BERRAK alt bandı bu filmde açıldı**: üç satırı gerekçeli tersine döndü [D74] — ① PUS YOK (uzun gece fotokimyasal pusu yağdırdı → dolgu ZAYIF, gölge SERT ve DERİN; kartın "yumuşak ve sığ" satırı düşer) ② GÜNEŞ DİSKİ VAR ama yalnız S7'de, hüzme ve lens parlaması yine YOK ③ ufuk KESKİN, yıldızlar ve parçalanmış ay görünür. Sıvı 0 · toz 0 (yalnız kuru kar sürüklenmesi) · buhar yakası VAR | Gotik bilimkurgu (sessiz iş / onarım) · tema **FEDAKÂRLIK** (K17·K20·K23 · tanım cümlesi: "Bir şeyi geri veren, geri veremediklerinin önünde bekler" — TAKAS kalıbı DEĞİL) · novum **ÖLÇEK** (üst üste ikinci ÖLÇEK film, not düşüldü): taşıyıcı **üç halkalı kafes** × anahtar çubuğunu çevirmesi — bir şehrin güneşi kafeste TAŞINABİLİR | 25-26.09.2026 · **hikâye SAHİBİN** (tretman + sekiz maddelik yönetmen kritiği; 0.7a fikir turu KOŞMADI, gerekçe onay NOT'unda · ONAY TUR 2/3) · 24 satırlık klip tablosu + 5 kilit klip · **SAHNE PLANI: 3 6 3 2 3 4 3** · KÜME YOK (rejim) · DÖNÜŞ 10/24 = **%41,7** · 7 kurulum · 5 açı tipi · ardışık çift 23/23 bant içi · şok 1 (K20→K21) · **VİZÖR OPTİK BERRAK** tek düz pane + KALIN KOYU ÇERÇEVE [D146] — tretmanın "dar vizör"ü ⛔ yasaklı olduğu için M arketipinden K'ya geçildi, gotik ağırlık çerçeve kalınlığı + derin yaka + kare omuz kapakları + sayılı alın lambaları ile taşındı · **1 replik, 2 kez duyulur** (kayıtlı insan sesi, 24,0 s ve 90,0 s · kadrajda konuşan ağız 0) · **2 ⭐VİRAL** (K12 · K17) — ⭐ kartın ⬜ İKİNCİ ÖLÇÜMÜ BU FİLMDE TAMAMLANDI: iki filmde 0 ve 2, yani **4 bir bant değil**, bu estetiğin bandı 0-2 · **referans paketi YAZILDI** (sahip kararı · 6 sayfa / 25 panel · KAPI 0) · ⭐ novum'un SINIRI her PHYSICS satırında yazılı ("yalnız küre yukarıda kalır") — THE_KEPT_LIGHT'ta sınır sızmış ve sekiz mercek kaçırmıştı · ⭐ ölçek kanıtı TEK KAREDE (K02: küre 922 px + kapı boyunda aydınlık pencere 205 px, D78 iki kare ezberi olmadan) · ⭐ doruk D127 ile ölçülebilir (çıkış süresi: alt kenar 6. saniyede üst kadraj çizgisini geçer, 8. saniyede yok) · **§3.9 kartının İngilizce PHYSICS/AUDIO cümle çifti bu filmde yazıldı** (PROMPT_HATA_ONLEME §2'de yoktu; THE_HEALING_GROUND ve THE_SLOW_RAIN ikisi de elle yazmıştı) · QA SPEC ㉔ + ffmpeg 8.1 ile DOĞRULANMIŞ 6 makine kapısı + 5 GÖZ KAPISI + 10 satırlık YANLIŞ-POZİTİF DUVARI · 18/18 üretim öncesi kontrol (4 gerçek hata üretimden ÖNCE yakalandı: insan şeridi 23→24 karakter ve insansız klip 4→6 · davranış şeridinde bedensiz iki harf · yüzsüz kliplerde "real skin pores" ↔ "no bare skin" çelişkisi · nesne-göreli fener konumu) · DİYALOG KRİTİĞİ **GO** (rewrite 0 · cut 0) · prompt_kontrol klasör modu **0 BLOCK / GO** · ⬜ K1 klip süresi [D124] · K2 vizör biçimi 2. klipte (kubbe çıkarsa ÜRETİM DURUR, karar sahibe) · K3 K21 İPTAL KAPISI · üretim 0 kare |
| **THE_SIGNAL_KEEPERS** | 4 dk (24 × 10 s = 4:00 · 2 BÖLÜM × 12 KLİP · **6 SAHNE** (3-5 klip) · KILAVUZ §2.3) — ÇOK KLİPLİ SAHNE rejiminin **dördüncü** klasörü, 4 dk formatının üçüncüsü | §3.4 KALIN ATMOSFER (240 K · 3,1 bar · 0,42 g · solunamaz) — ⭐ **kartın SİSLİ + BİYOIŞIKLI alt bandı bu filmde açıldı**: iki satır eklendi, biri AYNEN korundu [D74] — ① SİS VAR ama TOZ PERDESİ YOK: sis KONDENSATtır, hollowlarda OTURUR ve yükselmez; toz KALKAR ve üç saniyede yeniden OTURUR + kümelenir — ikisi aynı promptta asla karıştırılmaz ② BİYOIŞIK VAR: alçak bitki bandı kendi kaynağıdır, ama `0% bloom / no glow` satırı KALKMAZ — kartın Arşimet kalıbının aynısı uygulandı (yasak HÂLE için, pozitif kural KAYNAK için: "the low plants are themselves the source, like lit lamps, not spreading past their edges") ③ ses GÜÇLÜ/ALÇAK/YAKIN satırı filmin BÜTÜN dramaturjisi oldu: filmde yalnız İKİ tiz olay var ve ikisi de anlamlı (kaydın ünsüzleri · camdan çıkan ton). Işık kaynağı gökteki HALKALI DEV GEZEGEN — yansıyan ışık, güneş diski YOK, hüzme YOK; ısı kaynağı gelgit ısıtması (Peale, Cassen & Reynolds 1979 · Voyager 1) | Bilimkurgu (keşif / ilk temas) · tema **UMUT** (K01·K11·K24 · tanım cümlesi: "Karşılık beklemeden gönderilen şey, karşılığını sen görmesen de bulur" — ⭐ yüzeydeki etiket İLK-TEMAS olurdu ve o deponun EN ÇOK işlediği tema (10/62), bilerek alınmadı) · novum **İLİŞKİ** (depoda ikinci İLİŞKİ filmi — üst üste ÜÇÜNCÜ ÖLÇEK filmi olma tekrarı böyle kırıldı): taşıyıcı **kırık mavi cam parçası** × varlığın avucunun açılması — insan yapımı bir nesne yabancı bir avuçta 41 yıl ÖZENLE saklanmış | 26-28.09.2026 · **hikâye SAHİBİN** (kendi tretmanı; 0.7a fikir turu KOŞMADI, gerekçe onay NOT'unda · ONAY TUR 1/3) · 24 satırlık klip tablosu + 5 kilit klip · **SAHNE PLANI: 3 4 5 3 5 4** · KÜME YOK (rejim) · DÖNÜŞ 10/24 = **%41,7** · **12 kurulum** · 4 açı tipi · ardışık çift 23/23 bant içi ve **23/23 TAM 1 ÖLÇEK KADEMESİ** · ⚡**ŞOK 0** (tavan 2) — ⭐ ve bu bir EKSİKLİK DEĞİL TERCİH: filmin kopuşu SES kanalındadır (K20 · 192,6 s), meşru tek şok (K20→K21 MS→EWS) ÖLÇÜLDÜ ve ALINMADI, gerekçesi 03 §3'te yazılı · **VİZÖR OPTİK BERRAK** tek düz pane + KALIN KOYU GRİ ÇERÇEVE [D146] · arketip **E BELGESEL** (`UZAY_GIYSISI` §2 varsayılanı — kırık beyaz gövde siyah bazaltta DEĞER olarak ayrılıyor) · **1 replik, 2 kez duyulur** (41 yıllık kayıt: 12,0 s bozuk · 173,0 s net · kadrajda konuşan ağız 0 · üçüncü duyum YOK, K20 yalnız KESİLMEYİ taşır → ㉓ envanteri tutar) · **3 ⭐VİRAL** (K11 · K20 · K22) — ⭐ kartın **ÜÇÜNCÜ ÖLÇÜMÜ BU FİLMDE** ve belirleyici değişkeni değiştirdi: yüz taşıyan kurulum SAYISI değil, o kurulumun klibinde İKİNCİ HACİM OLAYI olup olmadığı; bant 0-2'den **0-3**'e açıldı (§2.3) · **referans paketi YAZILDI** (sahip kararı · 6 sayfa / 19 panel · KAPI 0 · 6 tetikleyiciden 5'i doğru) · ⭐ **UZAYLI VARLIK deponun ilk KADEMELİ ANATOMİ filmi**: merdiven MONOTONİK (iz → siluet → parça → TAM FORM → parça), tam form yalnız S04-S05, anatomi SAYISI yalnız o iki sahnenin promptlarında, kamera yayı ≤90°, orbit 0, arka görünüm hiç açılmıyor · ⛔ **GÖZ FİLM BOYUNCA HİÇ ANILMIYOR** — ne pozitif ne negatif olarak [D123]; empati kanalı GÖZ değil EL (avuç açılır K10 · panele iner K19 · kalkar K20) ve bu sapma sahibe ayrı soruyla onaylatıldı · ⛔ **TEMAS 0 KARE** 24/24 (ret gecikmesi 0,8 s · konum kilidi kadın SAĞ / varlık SOL · merkez çizgisi 0 klipte geçilir) · ⭐ **"yüzlerce sonda" hiçbir promptta YOK**: salonun derinliği IŞIKSIZ, çokluk izleyicinin çıkarımı (KART 13) · ⭐ metin yasağı bir YASAK değil DÜNYANIN KURALI oldu (bu medeniyet yazmaz, duyar ve saklar) · **§3.4 kartının İngilizce PHYSICS/AUDIO cümle çifti bu filmde yazıldı** (PROMPT_HATA_ONLEME §2'ye indi) · QA SPEC ㉔ + ffmpeg 8.1 ile DOĞRULANMIŞ 6 makine kapısı + 5 GÖZ KAPISI + 12 satırlık YANLIŞ-POZİTİF DUVARI · 18/18 üretim öncesi kontrol (**6 gerçek hata üretimden ÖNCE yakalandı**: yüzsüz 13 klipte "real skin pores" ↔ "no bare skin" çelişkisi · D59 kökü "stopped" altı yerde duruş beyanı · K10'un IŞIK satırı camı ışık kaynağı yapıyordu (⑥ ekipman aynılığı çelişkisi) · PLAN'da 23 ders kilidi (tavan 20) · K23 image'da CONTINUOUS ACTION eksik · K22'de "behind her" ⑮ yanlış-pozitifi) · DİYALOG KRİTİĞİ **GO** (rewrite 0 · cut 0 · üç KİLİT: üçüncü duyum yazılmaz · replik göndericisini ADLANDIRMAZ · ağız 7 yüz klibinde de kapalı) · prompt_kontrol klasör modu **0 BLOCK / GO** · ⬜ K1 klip süresi [D124] · K2 varlığın anatomisi K13-K16'da (göz/ikinci uzuv çıkarsa ÜRETİM DURUR, HAZIR DÜŞÜŞ siluete) · K3 ton kanalı K10-K11 (tutmazsa Plan B tanımayı K17'ye taşır) · üretim 0 kare |
| **THE_LAST_TOW** | 8 dk (48 × 10 s = 8:00 · 2 BÖLÜM × 24 KLİP · **12 SAHNE** (3-5 klip) · KILAVUZ §2.7) — ÇOK KLİPLİ SAHNE rejiminin **beşinci** klasörü ve **8 dk hattındaki İLKİ**; ⭐ bu hattın dört filmlik 4 × 12 sapmasını KAPATTI: dramatik birim SAHNE (12), dosya birimi BÖLÜM (2), ikisi artık çatışmıyor ve kartın "2 × 24"ü olduğu gibi tuttu | §3.8 VAKUM + TEMİZ METAL · SOĞUK KAYNAK (0,30 g · hard vakum · gölge mutlak siyah · dolgu 0) — ⭐ kartın **İKİNCİ filmi ve ilk UZUN filmi**; İngilizce PHYSICS/AUDIO çifti + asimetri cümlesi + metin karşı önlemi bu filmde yazıldı ve `PROMPT_HATA_ONLEME` §2'ye indi (kart 01.09'da açılmıştı, iki film boyunca §2'de karşılığı YOKTU). ⭐ **YALAYAN IŞIK alt bandı açıldı:** yıldız 2,3°'de SABİT (yükselme 0,17°/saat → 8 dakikada 0,023°, ölçülemez), hareket eden şey 40 m'lik sırtın **GÖLGE KENARI** ve saniyede 2,0 cm (72 m/saat · bu sahadan 44 günde bir geçer). Ayrım DİKEY/YATAY: yıldıza bakan dikey çıplak metal 370 K, yatay zemin 1361 × sin(2,3°) ≈ 55 W/m² ile 180 K → aynı köşenin iki yüzü arasında **190 K fark** ve kaynağı koparan şey bu. Kompozisyon da ondan çıkıyor: dikey yüzeyler parlar, zemin karanlık. Bilim çapası belgelenmiş: soğuk kaynak bir uzay mühendisliği arızasıdır (en çok anılan vaka Galileo'nun açılmayan yüksek kazançlı anteni, 1991 · NASA/JPL) ve airless yüzey sıcaklık salınımı ~100 K ↔ ~390 K (LRO Diviner) | Bilimkurgu (keşif / kurtarma) · tema **YALNIZLIK** (S01·S04·S06·S09·S11·S12 · kanonik sekizlinin EN AZ işlenmişi, depoda 3 · tanım cümlesi TAKAS kalıbı değil bir İLK↔SON dönüşü: "Yıllardır her şeyi birbirinden ayrı tutan kadın, sonunda bir şeyi bir daha ayrılmayacak biçimde kendine bağlar") · novum **FİZİKSEL YASA** (son iki filmin ÖLÇEK/İLİŞKİ tekrarı kırıldı): taşıyıcı **56 cm'lik çelik anahtar** × tekme → kaymıyor, düştüğü yerde saplı kalıyor | 28.09.2026 · hikâye **0.7a FİKİR TURUNDAN** (üç yöntem · 11 logline · ilk üçü ısınma · üç aday A/B/C · A'ya üç satır karşı argüman) · ONAY TUR 1/3 + **S6 mekanizması için AYRI onay** (onaylı satır filmin kendi kuralıyla çelişiyordu: kabin resife kaynamış, döndürülemez → yerine 2,4 m'lik levha dikine kaldırılıp ayağı kaynatılıyor, gölgesi dikişin yarısını soğuk tutuyor) · 48 satırlık klip tablosu + 5 kilit klip · **SAHNE PLANI: 4 3 5 4 4 4 4 5 3 4 5 3** · KÜME YOK (rejim) · DÖNÜŞ 21/48 = **%43,8** · **11 kurulum** · 3 açı tipi · ardışık çift **47/47 bant içi** · ⚡**ŞOK 1** (K01→K02 · Δ2 · tavan 1-2 · filmin tek tanıtım kesmesi) · bölüm sınırı K24↔K25 bant içi (Δ1 · 150°) ve palet de orada KENAR→IŞIK dönüyor · **VİZÖR tek düz pane 22 × 14 cm** + kalın koyu gri çerçeve [D146] · arketip **E BELGESEL** · **REPLİK 0 · KAYIT 0** — ⭐ tasarım gerekçesi ortam kartının kendi satırı: "dışarıda ses yok, duyulan her şey TEMASTIR"; konuşan bir insan kuralı ilk saniyede çürütürdü · **3 ⭐VİRAL aday** (K16 · K27 · K40) — ⭐ kartın **DÖRDÜNCÜ ÖLÇÜMÜ ve İLK UZUN FORMAT ölçümü**: 48 klipte 3 çıktı, `yatay_8_dk_filmler/README` "süreyle ölçeklenir: 48 sahnede 8" diyordu → **satır bu estetikte GEÇERSİZ**, bağımlı değişken YÜZ TAŞIYAN KLİP SAYISI (bu filmde 5/48, grep ile ölçüldü) · **referans paketi YAZILMADI** (sahip kararı · 6 tetikleyiciden 4'ü doğru → biçim kilidi YALNIZ metinde; karşı önlem dört sayı + yasak kelime listesi + ikinci klipte elle kontrol + ÜRETİM DURUR kapısı) · ⭐ **KURALIN DÖRT POZİTİF KANIT KLİBİ** ilan edildi ve SPEC'e "kesilemez" yazıldı (K03 tekmelenen anahtar saplanıyor · K25 dikiş kopuyor · K37 botlar kopuyor · K44 kesici kafası değiyor ve kalıyor) — gerekçe ölçülmüş: §3.8'in ilk filminde (THE_COLD_WELD) altı merceğin ALTISI kuralı adlandıramadı, çünkü bütün kanıtlar YOKLUKTU ve video "olmayan bir şeyi" "hiçbir şey" diye render etti · ⭐ **ikinci basınç giysisi bir NESNE olarak yazıldı** (`body`·`dead`·`corpse`·`remains` **0/96**; omuz düz, kemer yok, panel koyu) → `Exactly one human character` cümlesi 46/48 klipte DOĞRU kaldı ve red defterinin sözlükle ÇÖZÜLMEYEN tek sınıfı (#3 PB) tasarımda kesildi · ⛔ kaynak kuralı hiçbir promptta YASAK olarak yazılmadı (0/96), karşılığı 17 klipte pozitif asimetri · üç metinsiz sayaç, üçü de monotonik (ışık kenarının mesafesi · kesicinin dört durumu · açıklığın 20→4 mm'si) · QA SPEC ㉔ + ffmpeg 8.1 **kuru koşuyla doğrulanmış 6 makine kapısı** + 5 GÖZ KAPISI + 9 satırlık YANLIŞ-POZİTİF DUVARI · 18/18 üretim öncesi kontrol (**5 gerçek hata üretimden ÖNCE yakalandı**: K01'in optiği — 56 cm'lik anahtar 85 mm/1,1 m kadrajına (0,47 m) SIĞMIYORDU, kurulum D'den C'ye taşındı [ADAY-101] · iskelet DÖNÜŞ'ü kapının ölçtüğü biçimde tutmuyordu (%10 → %43,8, iskelet aramayla baştan kuruldu) · "at chest height" ifadesi kamera yükseklik imzasını bozup aynı harfi iki kurulum gösteriyordu · PLAN üç kilidin kapsamasını 48/48 diye İDDİA ediyordu, ölçüm 17/36/13 dedi → sayılar düzeltildi · kartın genleşme sayısı hangi alaşımı varsaydığı yazılı değil [ADAY-102]) · DİYALOG KRİTİĞİ koşulmadı (replik 0) · prompt_kontrol klasör modu **0 BLOCK / GO** (image 161-250 · video 196-267 kelime) · ⬜ 8 ölçüm randevusu AÇIK (klip süresi · vizör biçimi · K31 yüz · K44 atomik sınır · ⭐viral · orta bölüm düşüşü · gölge YAVG · fener px) · üretim 0 kare |



> **Yeni film yazarken:** kendi kombinasyonuna en yakın satırı bul, o filmi
> şablon olarak aç. Aynı format = aynı yapı. Aynı ortam = aynı fizik.

---

# 9. 🔧 BAKIM NOTLARI

```
BU REHBER NE ZAMAN GÜNCELLENİR
  □ Yeni format eklenince      → Bölüm 2'ye kart
  □ Yeni ortam eklenince       → Bölüm 3'e kart
  □ Yeni tür eklenince         → Bölüm 4'e kart (4.4 şablonundan)
  □ Yeni film bitince          → Bölüm 8 matrisine satır
  □ Üretimde yeni tuzak        → Bölüm 7 (en değerli bölüm, besle)

BİLİNEN BORÇLAR
  • ✅ ÇÖZÜLDÜ — 1_KARE_QA_CRITIQUE_PROMPT.md (FORMAT: DİKEY) yeniden yazıldı (31.07.2026).
    Eski sürüm tek bir yapıma ("KULE 7") gömülüydü ve o film depoda yok.
  • Tür eki klasör adında (`_uzay`) — ölçeklenmiyor (12.08.2026: `_zombi`
    ve `_savas` klasörleri kaldırıldı, tür rafta)
  • 3-5 dk README'si düz dosya yapısı tarif ediyor, LOW_POWER klasörde
  • ✅ ÇÖZÜLDÜ (07.08.2026) — LESSONS_LEARNED üç işi tek dosyada yapıyordu;
    dersler DERSLER/ klasörüne tematik bölündü, LESSONS_LEARNED.md artık
    dizin + teknik kalite tablosu
  • Derslerin tamamı bilimkurgudan geldi; yeni bir tür açılırsa kendi
    hatalarını üretecek, ders numaralarına tür etiketi gerekebilir
  • ✅ ÇÖZÜLDÜ (21.08.2026) — üç rakip "her prompta yapıştır" bloğu vardı
    (§5 çekirdek · 00_HIZLI_REFERANS v8 8.4k karakter "hepsini ekle" ·
    IMAGE_VIDEO_PROMPT_TEMPLATES v4 ölü blok). v4 silindi, v8 "kilit
    havuzu"na çevrildi, tek zorunlu blok §5 kaldı.
  • 7-9 dk kartı ↔ tek gerçek film (THE_SLOW_STONE) çelişkisi AÇIK —
    dürüst kayıt §2.4'te; ikinci filmden önce format kararı gerekli
  • URETIM_ONCESI_ANALIZ/01 ders-etkinlik raporu bayat (01.08.2026):
    yalnız o kesitteki 50 dersi ölçtü (01.08.2026); D51-119 hiç
    ölçülmedi — rapor yeniden koşulmalı
```
