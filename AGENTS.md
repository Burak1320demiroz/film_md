# 🤖 AGENTS.md — Ajan Çalışma Kontratı (üretim hattı)

> **05.10.2026'dan beri geçerli.** Eski kontrat `AGENTS_ESKI_HAT.md`'dedir ve DONDURULMUŞTUR.
> Eski belgelerde geçen "AGENTS.md Kart A / Kart P / §3 …" atıfları o dosyayı kastediyor.
> Bu dosya kısa kalır: akışı, kuralları ve dosyaların yerini söyler. Yöntem `uretim_hatti/`'nda,
> zanaat `.claude/agents/`'ta, prosedür `.claude/skills/`'tedir.
> **16.10.2026 güncellemesi (hat v2, sahip: "araştırma kalsın şimdilik, sen hazırla direkt yeni güncellemeyi"):** Fable teslimi
> sahiplenir · medya hatta `medya.py` ile girer · F3'ten sonra 1-3 çekimlik pilot · kurgucu F3'te · kural türleri · DERS uyarıları. Gerekçe §0.

---

# 0. DURUM — neden yeni hat

```
ESKİ HAT  121 film yazıldı · 63 kılavuz ~27.000 satır · 2.950 satırlık kontrol betiği.
          Kanalda 225 video yayında (apexaic/DIS_SAYILAR.md §1) ama deponun performans
          tablosuna hiçbiri işlenmedi — hiçbir filmin izleyici verisi ölçülmedi.
          Ham QA analizi (05.10.2026 · 49 tam film): hikâye kararı veren raporların çoğu
          "yapıyı yeniden kur / önermeyi baştan yaz" dedi; ölümcül teknik hataların ~%45'i
          NEYİN GÖSTERİLDİĞİNDEN doğdu, yalnız ~%17'si prompt metninden. Kural yazmak tutmadı
          (temas cümlesi 22/25 promptta yazılıyken 7 ölümcül hata). → uretim_hatti/ARIZA_LISTESI.md
YENİ HAT  Uzman alt ajanların yazıp birbirini eleştirdiği, ana ajanın (Fable) denetçiyle faz
          kapılarını onayladığı, insanın SEÇTİĞİ görüntüden kurulan, harcaması sınırlı hat.
          Hata yeni kural doğurmaz; hatanın NEREDE doğduğu bulunur ve orada çözülür (§3).
HAT v2    (16.10.2026) Yeni hattın 5 filmi ölçüldü (ARASTIRMA/16 · 11 §B · sahibin getirdiği dış eleştiri):
          · çağrı sonucu belirlemedi: 50/50 çağrılı film "Kopuk", 7 çağrılı film anlaşıldı; 50 çağrının hepsi ilk kareden önce harcandı;
          · üretim, seçim ve montaj hattın dışında kaldı: ~/film_medya 5/5 boş, DENEMELER 5/5 boş, DURUM montajdan sonra hâlâ F7;
            F7-F8 ajanları hiç çağrılmadı; QA numaraları plan numarası çıkmadı (MAYDAY · SKY);
          · gerçek kusurun %71'i prompta bağlı (152/214); yazılı kural 5/5 filmde çiğnendi (SKY 24/24 ses cümlesi), eleştirmen
            ve denetçi kaçırdı; paralel yazılan gruplar birbirinden kaydı (FURNACE G03 ↔ G04 rozet);
          → medya hatta girer (medya.py) · Fable teslimi dosyadan izler · gerçek görüntü erken (F3p pilot) · kurgucu F3'te ·
            F5'te ilk grup önce, sonra paralel · kural türü belli (§1b) · ölçülemeyen ders kapı değil UYARI, ama cevapsız kalmaz.
          Araştırma (ARASTIRMA/17, 4 prompt) koşulmadı; koşulursa süzmesi bu güncellemeyi sınar.
```

**Klip zinciri (05.10.2026 · sahip kararı):** ardışık klipler gerekçeli yerlerde zincirlenir.
Halka n'nin bitiş karesi, halka n+1'in başlangıç karesidir.
- 22.09.2026'da kaldırılan zincir **prompt diliyle** kuruluyordu ("continues the previous clip"); o dil hâlâ yasak.
- Yeni zincir **gerçek başlangıç + bitiş karesi görselleriyle** kurulur (anahtar kare = B; yedekler A · A′ · A+).
- Seçmeli; zincir başına ≤4 halka.
- Flow davranışı `uretim_hatti/SMOKE_TEST.md` zincir bölümüyle doğrulanmadan zincirli üretim yok.

**Giriş noktası tek:** `/yeni-film`. Yeni film başlatır ya da `ODA/DURUM.md`'den sürdürür.
- Faz skill'leri (`hikaye-odasi` · `sahneleme-odasi` · `ses-muzik` · `cekim-yaz` · `paketleme` · `klip-sec`)
  kendiliğinden açılmaz. Ana ajan onları dosya olarak okur; sahip `/adıyla` çağırabilir.
- Eski hattın skill'leri (`prompt-kontrol` · `qa-isle` · `yeni-film/ESKI_HAT_SKILL.md`) dondurulmuştur.

---

# 1. DEĞİŞMEZ KURALLAR

```
① COMMIT'İ YALNIZ SAHİP ATAR. Ajan commit/push/reset/checkout/stash çalıştırmaz
  (.claude/settings.json deny listesi). İş bitince: değişen dosyalar + önerilen commit mesajı.
② MEDYA REPOYA GİRMEZ. Görsel, video, ses dosyaları ~/film_medya/<FILM>/ altında durur:
     ref/ referans · kare/ başlangıç kareleri · ham/ Flow denemeleri · ses/ replik·efekt·müzik
     cikti/ taslak ve final · kareler/ kontak sayfaları · izleyici/ izleyici ajanına gösterilenler
  Repoya yalnız METİN girer: plan, prompt, seçim (timeline.json), not, ajan çıktısı, ölçüm.
  Tek istisna (sahip kararı 12.10.2026): kök dizindeki README görselleri `readme_*.png` (.gitignore'da tek satır).
③ HİÇBİR ŞEY SİLİNMEZ. Eski hat olduğu yerde kalır; kılavuz ve raporlar düzenlenmez.
④ HATA KURAL OLMAZ. Üretimde görülen hata filmin NOTLAR.md'sine "ret nedeni" satırı olur.
  Yeni ders, yeni kapı, yeni kılavuz YAZILMAZ. Aynı hata iki ayrı filmde, kayıtlı vakayla
  tekrar ederse sahibe "BILINEN_TUZAKLAR'a / ARIZA_LISTESI'ne girsin mi?" diye sorulur.
⑤ KİM NEYİ ONAYLAR
  · Faz kapılarını ANA AJAN (Fable) onaylar — denetçi ajanın raporuyla. Mekanik ❌ (doğrulama
    betiği, kurgu.py kontrol, eksik girdi) aşılamaz; yargı ❌'i gerekçeyle aşılabilir ve
    ODA/DURUM.md "AŞILAN KAPILAR"a yazılır.
  · SAHİBİN iki onayı: hikâye seçimi (faz 1 — veto hakkı) ve yayın (faz 9).
  · Fable göremediğini onaylamaz: video hareketini sahibin işaretlemesi, Gemini taraması ve
    kare sayfaları taşır; yayın onayı izleme formları (sahip + ≥2 dış izleyici) olmadan istenmez.
⑥ YAPAY ZEKÂ PUANI KARAR VERMEZ. Eleştiri bulgudur (kanıt + şiddet), puan değildir.
  Gemini taraması zaman kodu ve kanıt getirir; "bulamadı" "temiz" demek değildir.
⑦ HAM ÇIKTI KORUNUR. Her alt ajan çıktısı ODA/'da olduğu gibi durur; ana ajan yeniden yazmaz.
  Eski hattın ham QA raporu gelirse eski yerine (FILM_QA_RAPORLARI/02_HAM_RAPORLAR/<FILM>/) kaydedilir.
⑧ BAĞIMSIZ GÖZ. Eleştirmene yazarın gerekçesi verilmez; izleyici ajanına plan hiç verilmez
  (görev şablonu: uretim_hatti/AJAN_GOREVLERI.md · okuma kancası: araclar/izleyici_kanca.py).
⑨ FABLE TESLİMİ SAHİPLENİR (16.10.2026). İş "faz kapısı geçti" ile değil, film teslim edilince biter:
  referanslar · kareler · denemeler · seçilen aralıklar · ses · taslak · final · yayın paketi. Durum hafızadan değil dosyadan
  okunur: her açılışta `medya.py durum <FILM>` → dosyalar DURUM.md'den ileriyse DURUM dosyaya göre düzeltilir.
  Sahibin hat dışında yaptığı iş (montaj, başka araçta üretim) hatta geri alınır (`/medya-denetle`), yok sayılmaz.
```

## 1b. KURAL TÜRLERİ (16.10.2026) — her kural hangi türden, kapıda ne yapar

| Tür | Ne | Örnek | Kapıda | Nasıl değişir |
|---|---|---|---|---|
| **SÖZLEŞME** | sahibin kararı, filmin teslim şartı | her çekim 10 s · çekim sayısı · medya repoya girmez · commit sahipte · yayın paketi İngilizce · numaralı referans · model sesi seçimi | **M** — aşılamaz | yalnız sahip |
| **ARAÇ** | belgeyle ya da ölçümle doğrulanmış araç sınırı (`FLOW_GERCEKLERI.md`) | prompt ≤4.300 kr · Veo klibi ≤8 s · mod ↔ model | **M** | kaynak değişince, kaynağıyla |
| **HİPOTEZ** | işe yaraması beklenen, ölçülmemiş teknik | DERS uyarıları Y1-Y13 · kimlik cümlesi birebir · ORTAK GÖRÜNÜM · panel sayfası (P17) · zincir · vuruş iskeleti | **⚠️ UYARI** — yazar her satıra düzeltme ya da tek cümle gerekçe yazar; cevapsız uyarı denetçide ❌ (yargı) | pilot ya da deney ölçer → sahip SÖZLEŞME'ye çevirir ya da emekliye ayırır |
| **TERCİH** | yaratıcı ya da kanal tercihi | replik bandı · müzik · kapak yazısı 0-3 kelime · başlık kalıbı | öneri — sapma gerekçeli serbest | yazar · Fable |

- Yeni kural **türüyle** yazılır. Türü yazılmamış kural HİPOTEZ sayılır.
- Bugünkü M maddelerinin bir kısmı sahip kararıyla M'dir ama etkisi ölçülmedi (vuruş planı · tek referans sayfası · tam 3 hashtag):
  türü sahip değiştirene kadar M kalır.
- HİPOTEZ ölçülmeden SÖZLEŞME olmaz (§1 ④). Ölçüm yeri film başına pilottur (F3p); SMOKE_TEST.md deney kataloğudur.

---

# 2. AKIŞ — `/yeni-film`

| Faz | Ne olur | Yazar | Eleştirenler (paralel) | Kapı |
|:--:|---|---|---|---|
| 0 | `DURUM.md` okunur; yeni filmde 3 soru: konu · format/süre · karakter | — | — | — |
| 1 Hikâye odası | 3 aday | senarist | dramaturg · yonetmen · izleyici (logline) | Fable seçer → **sahip vetosu** |
| 2 Tretman | sahne sahne + replikler | senarist · diyalog-yazari* | dramaturg · izleyici · ses-tasarimcisi | denetci → Fable |
| 3 Çekim listesi | bilgi · ekranda görünen · kadraj · süre · Flow modu · risk | yonetmen | teknik-danisman · izleyici (metin animatiği) · **kurgucu (kurgu gözü, 16.10)** · bilim-danismani* | film_dogrula + denetci → Fable |
| 3b Sahneleme ⏸️ | hangi çekimler zincir · anahtar kareler · mekân haritası · delta kontrolü — **16.10'dan beri yalnız zincir açıkken** (yonetmen ZİNCİR ADAYI yazdı + araç başlangıç/bitiş karesi alıyor + SMOKE zincir bölümü koşuldu); değilse ajansız kapanır | sahneleyici · mekan-haritacisi | mekan-haritacisi · teknik-danisman · yonetmen · izleyici | film_dogrula + denetci → Fable |
| **3p Pilot** (16.10) | en riskli an · açılış · kimlik/konuşma: 1-3 çekimin referansı + karesi + 2 denemesi **gerçekten üretilir**; sonuç F5'e film içi not olur | goruntu-yonetmeni (PILOT.md) · **sahip üretir** | devamlilik (kare) · teknik-danisman (pilot) | film_dogrula --bolum pilot + medya.py durum + denetci → Fable |
| 4 Ses + müzik | katmanlar · kayıt listesi · müzik planı (pilot üretilirken yürür) | ses-tasarimcisi · besteci* | kurgucu · diyalog-yazari* | denetci → Fable |
| 5 Promptlar | **önce G01** (+ §3 KİMLİK CÜMLELERİ, pilot çekimleri) → eleştiri → **sonra** kalan gruplar paralel, G01'i örnek alarak | goruntu-yonetmeni | devamlilik (8 soru, DO-CONFIRM) · teknik-danisman | film_dogrula (DERS uyarılarına cevap) + denetci → Fable |
| 6 Kapak konsepti | A/B tek değişken | kapak-tasarimcisi | izleyici (kapak) · yonetmen · yayin | Fable |
| 7 Üretim | **sahip Flow'da**: referans → kareler + anahtar kareler → kare denetimi → kareli animatik → riskli çekimler → kalanlar → dikiş döngüsü · başarısız çekim döngüsü · **her dönüşte `medya.py al` (DENEMELER) + `durum`** | goruntu-yonetmeni (yeniden tasarım) | devamlilik (kareler) · zincir-bekcisi (anahtar kare + dikiş) · izleyici (animatik) · teknik-danisman (ret) | Fable (kare kanıtıyla) |
| 8 Seçim + kurgu | sahip Gemini taraması → seçim → taslak → müzik finali · hat dışı montaj `medya.py bol` ile geri alınır | kurgucu (Bash: kurgu.py · kareler.py · medya.py) · besteci* | izleyici (kareler) · dramaturg (bitiş) | kurgu.py kontrol + denetci → Fable |
| 9 Paket | final kapak · İngilizce yayın paketi · bilim doğrulaması · izleme formları | kapak-tasarimcisi · yayin | izleyici (160×90) · bilim-danismani* | **sahip yayın onayı** |
| 10 Geri besleme | tutma eğrisi → düşüş saniyesi → çekim (`kurgu.py liste --zaman`) | — | — | not yazılır, kural yazılmaz |

`*` koşullu: diyalog-yazari `REPLIK var` · besteci `MUZIK var` · bilim-danismani `FIZIK_IDDIASI var`.

```
⭐ Faz döngüsü her fazda aynı (yeni-film §2): yazar → eleştirmenler TEK mesajda paralel → tur
   (ÖLÜMCÜL kalmayınca kapanır; tavan hikâye 3, diğerleri 2) → eser FILM.md'ye KOPYALANIR →
   mekanik kontrol → denetci → Fable kararı → DURUM.md + NOTLAR.md kaydı.
⭐ Video üretiminden ÖNCE iki ucuz test: metin animatiği (faz 3) ve kareli animatik (faz 7c).
   Amaç ve sonuç anlaşılmıyorsa pahalı video denemesine geçilmez; çekim listesi değişir.
⭐ PİLOT (16.10.2026, F3p): bütün promptlar yazılmadan önce 1-3 çekim gerçekten üretilir — en riskli an, açılış (C01) ve kimliğin
   ya da konuşmanın okunduğu çekim. Her filmde aynı uzun liste değil (SMOKE 19 maddenin 0'ı koşuldu); filmin kendi riski denenir.
   Pilotun dersi FİLM İÇİ nottur (ODA/F3p_pilot_karar.md → F5 görevine girdi), hat kuralı olmaz (§1 ④). Sahip "pilot yok" derse
   AŞILAN KAPILAR'a yazılır.
⭐ Model sesi KAPALI: taslakta atılır. Replikler tek ses profilinden; ortam, efekt, müzik ayrı katman.
⭐ Her çekim 10 s (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10 (2 dk 12 · 4 dk 24 · 8 dk 48 ·
   16 dk 96); timeline'da her video parçası 10 s. Flow'un Veo klibi 4/6/8 s verir; 10 s'ye nasıl ulaşılacağı
   SMOKE P14'te ölçülür. Ritim süreyle değil çekim içi hareket ve kadraj değişimiyle kurulur (ARIZA H10).
⭐ Referans = numara + ad (sahip kararı 10.10.2026, yeni filmler): FILM §3 "No" sütunu, dosya ref/<No>.<AD>_v<k>.png,
   §4 Referans sütunu "<No>.<AD>", her görsel promptun başında "Reference <No> (<rol>): …" anahtarı, EKLE satırında
   yükleme sırası. Numara film boyunca sabit; yeni özne sona eklenir. film_dogrula M.
   ÖZNE BAŞINA TEK REFERANS SAYFASI: karakterin önden/yandan/arkadan/üstten görünüşü, yüz yakını ve her durum
   değişimi aynı görselde panel; "SELA_yuz" gibi ikinci dosya yok (film_dogrula M). Çekim anahtarı paneli adlandırır.
⭐ Video promptu 10 s'nin planını yazar (sahip kararı 10.10.2026, yeni filmler): 2-4 vuruş "a-b s", 0'dan 10'a
   boşluksuz, vuruş ≥2 s, tek hareketin evreleri, son vuruş donmaz; saniye-altı mikro liste yok. film_dogrula M.
   Eski biçim film (§3 numarasız, örn. THE_WRONG_BURN) ⚠️ ile atlanır, eski kuralıyla sürer.
⭐ Model sesi replik (sahip kararı 12.10.2026, THE_MAYDAY_SEA ile): FILM §5 Kaynak "model sesi (telsiz | voice-over | ağız kadrajda)"
   → replik video promptuna BİREBİR yazılır, Omni konuşmayı videoda üretir; o parçanın sesi filme girer (timeline klip_sesi, yalnız
   replik için; yatak planda kalır); kurgu kaydı yedek. Model sesi KAPALI kuralı diğer filmlerde sürer. film_dogrula M · SMOKE P18.
⭐ Kesme sürekliliği (sahip, 12.10.2026: "geçişler keskin, kesmede arka ses komple değişiyor"): üç katman —
   PROMPT: §3 ORTAK GÖRÜNÜM cümlesi her promptta birebir, mekân ışık cümlesi birebir, ilk vuruş hareketle, aynı-mekân kesmesinde ölçek/açı farkı;
   SES: mekân başına TEK kesintisiz yatak klipleri aşar (timeline yataklar), mekân değişiminde 1-2 s çapraz, J/L zorunlu, müzik kesmede kesilmez;
   KURGU: kesme başına geçiş türü (kesme | karisim 0,3-0,8 | karartma 0,5-1,5 → kurgu.py gecis, xfade), her kesmede kareler.py dikis.
   FILM §6 ORTAM YATAĞI + GEÇİŞ tabloları. Kılavuz: uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md · SMOKE P19.
⭐ Müzik promptu her filmde (sahip kararı 12.10.2026): FILM §7 "### MÜZİK PROMPTU" ```text bloğu (İngilizce); F4 besteci taslağı,
   F8 kesin sürüm (eski altında kalır). film_dogrula --bolum muzik: MUZIK var ise yeni biçim filmde M, eskide ⚠️.
⭐ İlk 30 saniye (sahip, 12.10.2026: "her filmde hook güçlü, amaç ekranda tutmak"): ilk üç çekim C01 sorun + vaadin dünyası ·
   C02 insan en geç burada · C03 kapak anı ya da parçası; ilk 30 s'de logo, siyah ekran, saf manzara, görüntüde yazı yok; ilk 2 s insan
   sesi yok, sesi kapalı okunur (önizleme sessiz + altyazı açık oynar); açılış önce üretilir, kare kapısı ek ölçütlü. FILM §4 AÇILIŞ
   tablosu (yonetmen F3). Ölçüt Studio "Giriş"; hedef kanalın tipik bandı; deney defteri IZLEYICI_VERISI §3b.
   Kılavuz: uretim_hatti/ILK_30_SANIYE_KILAVUZU.md · süzme ARASTIRMA/08 · KABUL F3.7 F4.8 F5.10 F6.3 F7.7 F8.9 F9.7.
⭐ Kapak ve başlık (sahip, 12.10.2026): tek kapak bütün yüzeylerde; tıklama oranı yüzeye göre, kanalın kendisiyle kıyaslanır; ≤ 3 kişi,
   tek ilişki, sağ alt boş, kapak yazısı 0-3 kelime ve film adı yok; varsayılan yol aynı referanslarla ayrı kompozisyon, kapaktaki her varlık
   filmde; 2-3 aday, A ilk yüklenir ("kazanan yok" → ilk yüklenen kalır); başlıkta merak | AD ve QUIET, kanca ilk ~45 kr; eski videoda
   bir kez değiştir, 14 gün bekle. kareler.py kapak (360×202 · 168×94 · 120×68 · gri + bayrak). Kılavuz: uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md ·
   süzme ARASTIRMA/10 · KABUL F6.1 F6.2 F6.4 F9.3 F9.8 · IZLEYICI_VERISI §3c.
⭐ Bütçe: ODA/DURUM.md "AJAN_CAGRI n / 50" — 40'tan sonra yalnız ÖLÜMCÜL bulguya tur açılır.
   16.10.2026: metin fazları (F1-F6, pilot hariç) en çok 30 çağrı; 20 çağrı pilot ve üretim sonrasına (F3p · F7-F9) ayrılır.
   30'a gelen metin fazında yalnız ÖLÜMCÜL'e tur açılır (WRONG_BURN: 50/50 ilk kareden önce bitti, F7-F8 ajansız kaldı).
```

## 2b. Ajanlar ve modeller

**Kadro = 1 ana ajan + 6 rol (16.10.2026).** Ajan dosyaları silinmez; her ajan bir rolün uzmanıdır. Yazan denetlemez:
promptu yazan rol (görsel üretim) ile denetleyen rol (bağımsız göz) ayrı kalır.

| Rol | Ajanlar | Sorumluluk | Ne zaman |
|---|---|---|---|
| **Yapımcı** — Fable | ana ajan · denetci · `medya.py` | iş sırası, bütçe, ortak kayıt (DURUM · NOTLAR · MEDYA_DURUMU), **teslim** | her faz |
| **Hikâye** | senarist · diyalog-yazari* · dramaturg | öykü, karakter kararı, bedel, diyalog | F1-F2 (dramaturg F8 bitiş) |
| **Yönetmen** | yonetmen · sahneleyici ⏸️ · mekan-haritacisi ⏸️ | çekim listesi, kapsam, mekân ilişkisi | F3 (sahneleme yalnız zincir açıkken) |
| **Görsel üretim** | goruntu-yonetmeni | referans, kare ve video promptu, pilot, yeniden tasarım | F3p · F5 · F7 |
| **Kurgu ve ses** | kurgucu · ses-tasarimcisi · besteci* | F3 kurgu gözü, ses planı, seçim, timeline, taslak, müzik | F3 · F4 · F7-F8 |
| **Paketleme** | kapak-tasarimcisi · yayin · bilim-danismani* | kapak, başlık, vaat, yayın paketi | F6 · F9 |
| **Bağımsız göz** | izleyici · devamlilik · teknik-danisman · zincir-bekcisi ⏸️ | anlaşılırlık, kimlik/devamlılık, model riski, kare denetimi | her faz (izleyici plansız) |

`*` koşullu · ⏸️ yalnız zincir açıkken (F3b). Viral ajan yok: vaadi hikâye, açılış, kurgu ve kapak birlikte taşır; "izlenir" diyen ajan
izleyici verisinin yerini tutmaz (IZLEYICI_VERISI.md).

```
ANA AJAN     Fable (.claude/settings.json "model": "fable") — orkestrasyon + faz onayı + teslim
OPUS         senarist · diyalog-yazari · dramaturg · yonetmen · sahneleyici · kapak-tasarimcisi · denetci
SONNET       izleyici · teknik-danisman · goruntu-yonetmeni · devamlilik · mekan-haritacisi ·
             zincir-bekcisi · bilim-danismani · ses-tasarimcisi · besteci · yayin · kurgucu
ARAÇLAR      yazarlar: Read/Grep/Glob + Write (yalnız görev metnindeki {CIKTI} dosyası)
             eleştirmenler: salt okur · izleyici: yalnız Read + okuma kancası
             Bash: denetci (git diff · araçlar) · kurgucu (16.10.2026: kurgu.py · kareler.py · medya.py · ffprobe)
             hiçbir ajan alt ajan açamaz (disallowedTools: Agent)
```

---

# 3. HATA NEREDE DOĞDU — müdahale oraya

Bir hata görüldüğünde önce başlangıç karesi · gönderilen prompt · ham klip · finaldeki kullanım
yan yana açılır. Sonra sınıf seçilir:

| Hatanın doğduğu yer | Belirti | Müdahale |
|---|---|---|
| **Başlangıç karesi** | karakter/nesne karede zaten yanlış | referansı ve kareyi düzelt |
| **Hareket** | kare doğru, hareket sırasında bozuluyor | hareketi sadeleştir · çekimi böl · temas anını kesmeyle atla · başka Flow modu |
| **Seçim** | ham klipte kullanılabilir aralık var, finalde hata görünüyor | giriş/çıkışı düzelt |
| **Kurgu** | doğru klipler yanlış sırada / tekrar kullanılmış / eksik | `timeline.json` + dışa aktarma |
| **Anlatım** | görüntü temiz, olay anlaşılmıyor | çekim listesini yeniden kur (anlatacağı bilgi) |

Ham raporlardan ölçülmüş kapanma yerleri (`uretim_hatti/ARIZA_LISTESI.md` T bölümü):
```
el-nesne kaynaşması    → KADRAJ / KURGU  (cümle yazmak tutmadı)
ortama aykırı ses      → KURGU           (model sesi atılır)
filigran / köşe logosu → ARAÇ AYARI + yeniden dışa aktarma
istenmeyen yazı        → PROMPT KELİMESİ (kısa büyük harfli etiket yok) + KADRAJ (okunacak ekran yok)
kask/kıyafet/kimlik    → REFERANS + BAŞLANGIÇ KARESİ
```

---

# 4. BÜTÇE POLİTİKASI — başarısız tekrar döngüsü durur

```
ilk tur                                → 2 deneme
yeterli kullanılabilir aralık bulundu  → seçime geç
iki deneme de AYNI sebeple bozuk       → başlangıç karesini ya da çekim yaklaşımını değiştir
düzeltilmiş yaklaşım denenmeye değer   → 2 deneme daha
hâlâ kullanılamıyor                    → çekimi yeniden tasarla (§3) — aynı promptu tekrar gönderme
```
Her deneme NOTLAR.md'ye yazılır: çekim · deneme · araç/mod · prompt (dosya + p:sha8) · girdi (kare + referans) · süre · sonuç · kredi.
16.10.2026'dan beri satırı `medya.py al <FILM> --yaz` yazar; sahip yalnız işaretler (✅ aralık / ❌ neden → doğduğu yer).
Kayıt olmadan "model mi tutmadı, referans mı yüklenmedi" sorusu cevaplanamaz (5/5 filmde cevaplanamadı).

---

# 5. KALİTE — karar kanıtla, son söz insanın

```
KESİN (otomatik durdurur)   film_dogrula.py: eksik alan · her çekim 10 s · çekim sayısı = HEDEF_SURE/10 · zihinsel fiil · meta
                            etiket · ≤4.300 karakter · iş emri · zincir (≤4 halka · halka sonu =
                            sonraki başı · süre ≤ KLIP_SURESI · prompt içinde zincir dili yok) ·
                            promptta başka çekime atıf · film geneli ifade · konuşma tarifi (ağız kadrajdaki
                            replik hariç) · "insan yok" + kişi göndermesi · --bolum yayin: YAYIN_PAKETI
                            İngilizce, başlık sayımı, sabit blok, 3 hashtag (06.10.2026)
                            kurgu.py yukseklik: final −14 LUFS · ≤ −1 dBTP
                            kurgu.py kontrol: eksik dosya · bozuk video · geçersiz giriş/çıkış · video parçası 10 s ·
                            zincir halkaları ardışık
UYARI (HİPOTEZ, 16.10.2026) film_dogrula DERS Y1 Y2 Y5 Y6 Y8 Y10 Y13 (ARASTIRMA/16): kapı değil; yazar her satıra düzeltme
                            ya da tek cümle gerekçe yazar (KABUL F5.11), cevapsız satır denetçide ❌
DURUM (dosyadan)            medya.py durum: gerçek durum ↔ DURUM FAZ · adı kurala uymayan dosya · kayıtsız deneme · teslim satırı
BAYRAK (karar değil)        kareler.py dikis (SSIM/PSNR + şerit + fark) · kuyruk (donma · gizli kesme) · medya.py bol (montaj eşlemesi)
ELEŞTİRİ (kanıtlı bulgu)    alt ajanlar · uretim_hatti/ELESTIRI_PROTOKOLU.md — puan yok
SÜREÇ                       denetci · uretim_hatti/KABUL_LISTELERI.md — eleştiri yapıldı mı, girdi
                            aldı mı, KABUL gerçekten uygulandı mı
TAHMİN (kanıt getirir)      Gemini, 3 prompt, ortak bulgu tablosu (# · time · type · what · confidence):
                            QA_PROMPTLARI/TARAMA.md (klip içi · ≤90 sn · kare modu) · SUREKLILIK.md
                            (kesme iki yanı) · ANLATIM_TESTI.md (plansız, sesli)
İNSAN (son söz)             QA_PROMPTLARI/IZLEME_FORMU.md — sahip + hikâyeyi bilmeyen ≥2 kişi
```
Tarama zaman kodu `kurgu.py liste --zaman` ile kesin çekime çevrilir. Final baştan sona,
sesli izlenir.

---

# 6. HARİTA — ne nerede

```
AGENTS.md · CLAUDE.md          kontrat · oturum başı yönlendirme
.claude/settings.json          ana model (fable) · ~/film_medya ek dizin · git deny listesi
.claude/agents/                18 alt ajan (zanaat)
.claude/skills/yeni-film/      yönetici akış (tek otomatik tetik) · ESKI_HAT_SKILL.md (arşiv)
.claude/skills/{hikaye-odasi, sahneleme-odasi, ses-muzik, cekim-yaz, paketleme, klip-sec}   faz prosedürleri
.claude/skills/medya-denetle/  (16.10.2026) medya alımı · gerçek durum · hat dışı montajı geri alma (/medya-denetle)
uretim_hatti/                  ortak metinler · QA promptları · şablon · araçlar · test/ · ARASTIRMA/ (README.md)
<FORMAT>_filmler/<FILM>/      YENİ HAT filmleri süresinin format klasöründe (yatay_2_dk · yatay_4_dk · yatay_8_dk · yatay_16_dk ·
                               dikey_shorts; ayrı `filmler/` kökü 08.10.2026'da sahip kararıyla kaldırıldı) · FILM.md · SAHNELEME.md · KAPAK_VE_YAYIN.md (kapak) ·
                               YAYIN_PAKETI.md (İngilizce) · PROMPTLAR/ (PILOT.md · G01…) · ODA/ (DURUM.md · MEDYA_DURUMU.md) ·
                               NOTLAR.md · timeline.json
~/film_medya/<FILM>/           medya (repo dışı, §1 ②): ref · kare · ham · ses · cikti · analiz · izleyici
                               (anlamı: uretim_hatti/README.md § Medya)

ESKİ HAT (donduruldu, dokunulmaz)
AGENTS_ESKI_HAT.md             eski kontrat — arşiv haritası
kilavuzlar_ve_sistem_dosyalari/ kılavuzlar · eski QA rubrikleri · raporlar · betikler
yatay_* / dikey_* içindeki eski hat filmleri (<FILM>_PLAN.md / BOLUM_*.md) dokunulmaz; yeni hat filmi aynı format
                               klasörüne FILM.md + ODA/ yapısıyla açılır (08.10.2026).
```

---

# 7. ESKİ SİSTEMLE İLİŞKİ

```
ZORUNLU      uretim_hatti/BILINEN_TUZAKLAR.md (yazarlar + teknik eleştirmenler; kim neyi okur:
             AJAN_GOREVLERI.md § AJAN HARİTASI) · ARIZA_LISTESI.md (eleştirmenler) · izleyici hiçbir dosyayı okumaz
SERBEST      eski kılavuzlar SORUYA ÖZEL okunabilir (ajan dosyalarında "istersen bak" satırları)
KOPYALANMAZ  kayıtlı vakası ve bilinen sonucu olmayan hiçbir eski kural yeni hatta taşınmaz
KOŞULMAZ     prompt_kontrol.py · rapor_kontrol.py · okuma çizelgesi · sayac.sh yeni hat filmine
             uygulanmaz; sayac.sh yalnız eski filmlerin sayımı içindir
ARŞİV        eski 15 QA merceği + üç geçişli QA → kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/
             ARSIV_20261006/ (06.10.2026, sahip kararı). Yeni hat: uretim_hatti/QA_PROMPTLARI/ (4 prompt).
             ⑬ UYUM'un işini rapor-prompt karşılaştırma skill'i alacak.
```

---

# 8. DOĞRULAMA — iş bitince

```bash
git status --short                                                   # değişenleri sahibe listele
python3 uretim_hatti/araclar/film_dogrula.py <FILM>                  # yapı (+ DERS uyarıları: cevap yaz)
python3 uretim_hatti/araclar/medya.py durum <FILM> --yaz             # gerçek durum → ODA/MEDYA_DURUMU.md (F3p'den sonra her oturum)
python3 uretim_hatti/araclar/kurgu.py kontrol <FILM>/timeline.json   # timeline'a dokunulduysa
python3 uretim_hatti/test/kos.py                                     # bir ARAÇ (araclar/*.py) değiştiyse: hepsi ✅ (sayı betiğin son satırında)
```

> **Bu dosya ne zaman güncellenir:** akış, kural, ajan kadrosu ya da klasör haritası değişince —
> ve yalnız sahibin kararıyla. Yöntem ve zanaat buraya taşınmaz.
