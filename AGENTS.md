# 🤖 AGENTS.md — Ajan Çalışma Kontratı

> **Bu dosyayı her görevden önce oku.** Amacı sana içerik öğretmek değil,
> **nereye yazacağını** söylemek. Ne yaptığını anlatan kılavuzlar ayrı yerde
> durur; burası "hangi olay olduğunda hangi dosyalar değişir" haritasıdır.
>
> **Kural:** Bu dosyaya sayı yazma. Sayı isteyen her cümle kaynağa işaret eder.
> Bir sayıyı iki yerde tutmak, birini yanlış tutmaktır.

---

# 0. İLK 60 SANİYE

Görev ne olursa olsun bu sırayla:

```
1.  bash kilavuzlar_ve_sistem_dosyalari/sayac.sh     → gerçek durum
2.  kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md → üretim bilgisi
3.  bu dosyanın §3 görev kartlarından kendi görevini bul
4.  git status                                        → temiz mi başlıyorsun
```

**Kılavuz okumadan film yazma. Görev kartı okumadan dosya güncelleme.**

---

# 1. DEPO HARİTASI — ne nerede

```
kısafilmler/
│
├── AGENTS.md                      ← BU DOSYA · ajan yönlendirmesi
├── CLAUDE.md                      → bu dosyaya işaret eder
├── README.md                      proje tanıtımı
│
├── .claude/skills/                ajan skill'leri (26.08.2026) — kart sarmalayıcıları
│                                  (yeni-film · prompt-kontrol · qa-isle ·
│                                  yayin-takip) + kurulu dış skill'ler.
│                                  ⭐ ENVANTER VE KULLANIM TEK YERDE:
│                                  kilavuzlar_ve_sistem_dosyalari/SKILL_KULLANIM_KILAVUZU.md
│                                  Skill sırayı taşır, içeriği KOPYALAMAZ;
│                                  çelişkide bu dosya kazanır.
├── .agents/product-marketing.md   kanal kimliği — dış pazarlama skill'lerinin
│                                  işe başlamadan okuduğu ortak bağlam dosyası
├── apexaic/                       📺 KANAL — QA'dan sonrası · ÜÇ HESAP (01.09.2026)
│   ├── README.md                    yapı · okuma sırası · açık işler ·
│   │                                   timelapse_md/apexait eleştiri kaydı
│   ├── 00_KANAL_DENETIMI_VE_PLAN.md 📋 canlı kanal denetimi · sahip kararları S1-S12
│   ├── KANAL_KIMLIGI.md             ⭐ üçünde aynı: tez · negatif çekirdek ·
│   │                                   palet/Λ · dil · Hakkında · handle geçişi
│   ├── YAYIN_PLANI.md               kadans · film+fragman · ortam sırası · playlist
│   ├── CAPRAZ_YAYIN.md              iki master · huni · filigran · C2PA · sıra
│   ├── POLITIKA_VE_RISK.md          yanıltıcı metadata · inauthentic · AI beyanı
│   ├── DIS_SAYILAR.md               ⭐ TEK sayı tablosu (üç platform · tarih · kaynak)
│   ├── APEXAIC_INTRO_PROMPT.md      10 sn logo introsu (image+video prompt)
│   └── youtube/ instagram/ tiktok/  HESAP_KIMLIGI.md · PAKETLEME_SABLONU.md
│
├── kilavuzlar_ve_sistem_dosyalari/   ⭐ SİSTEMİN BEYNİ
│   ├── KILAVUZ_REHBERI.md         ⭐ BURADAN BAŞLA — format/tür/ortam kartları,
│   │                                 negatif çekirdek, üretim akışı, tuzaklar
│   ├── YAPI_GRAFI.md                 karar ağacı + klasör ağacı (görsel özet)
│   ├── LESSONS_LEARNED.md            ders DİZİNİ + teknik kalite tablosu
│   ├── DERSLER/                      ders metinleri — 9 tematik dosya + hızlı
│   │                                 referans bloğu (07.08.2026'da bölündü)
│   ├── sayac.sh                      sayıları dosya sisteminden hesaplar
│   ├── FILM_KLASOR_SABLONU/          🆕 01.09.2026 · film klasörü iskeletinin
│   │                                 KOPYALANABİLİR hâli (7 dosya taslağı).
│   │                                 Tanım KILAVUZ_REHBERI §2.0'dadır;
│   │                                 burası yalnız `cp -r` hedefi.
│   │                                 prompt_kontrol.py yolu atlar (SABLON)
│   │
│   ├── SINEMATOGRAFIK_TEKNIK_KILAVUZ.md   lens/ışık/kamera + §17 karar tablosu
│   ├── SAHNE_DEVAMLILIK_KILAVUZU.md       karakter çapalama, seed
│   ├── UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md  kuşbakışı harita, ekran yönü, ölçek kilidi
│   ├── YANASMA_VE_KENETLENME_KILAVUZU.md  yanaşma vuruş seti + ses/dramaturji kalıbı
│   ├── TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md
│   ├── IMAGE_VIDEO_PROMPT_TEMPLATES.md    V2 prompt iskeleti
│   ├── VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md
│   ├── UZAY_SENARYO_KILAVUZU.md · SAVAS_SENARYO_KILAVUZU.md
│   ├── ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md 🆕 03.09.2026 · giysi
│   │                                  kimliği: rol şeridi · metinsiz amblem ·
│   │                                  bilek/saat · sırt silueti · eşya + AI
│   │                                  risk sınıfları (kaynak: TUR 5)
│   ├── UZAYLI_VARLIK_TASARIM_KILAVUZU.md 🆕 03.09.2026 · TEK uzaylı
│   │                                  varlık: niyet (huşu/dehşet/empati) ·
│   │                                  siluet/hareket · ANATOMY LOCK ·
│   │                                  reveal merdiveni K0-K4 + VARLIK
│   │                                  ŞERİDİ · varlık kelime sözlüğü
│   │                                  (kaynak: TUR 7 · uzay operası
│   │                                  yasağı SÜRER — ırk/filo yok)
│   ├── SHORTS_SISTEM_PROMPTU.md           dikey 9:16 hazır sistem promptu
│   │                                      ⚠️ 27.08.2026: md.5'ten "tehlike yoktur" KALKTI · "eller her zaman boş" GEVŞEDİ
│   ├── GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md
│   ├── KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md
│   ├── VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md paketleme (YT/IG/TikTok)
│   ├── SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md vuruş haritası + loop + kamera psikolojisi
│   ├── HOOK_VE_ILK_SAHNE_KILAVUZU.md      ilk iki sahne: S0 karar / S1 tırmandırma + hook tipolojisi
│   │                                      ⭐ §3.1 DRAMATİK İRONİ — dikeyin en yeni zorunlu bölümü (27.08.2026)
│   ├── FRAGMAN_KILAVUZU.md                fragman: dikey 3-6 / yatay 8-12 vuruş, spoiler kapısı
│   ├── KURGU_VE_TESLIM_KILAVUZU.md        birim sözlüğü + 10 maddelik kurgu kapısı + kırpma bütçesi (21.08.2026)
│   ├── SES_VE_DIYALOG_URETIM_KILAVUZU.md  replik/ses YAZIM tarafı: register + AUDIO kalıpları (21.08.2026)
│   ├── KARAKTER_VE_DUYGU_KILAVUZU.md      bağ kurma bütçeleri: göz · Kuleshov · el/nefes/yürüyüş (22.08.2026)
│   ├── KURGU_RITMI_VE_IHRAC_KILAVUZU.md   ASL eğrisi · örüntü kırıcı · ses köprüsü · ihraç sayıları (22.08.2026)
│   ├── SERI_VE_KANAL_STRATEJI_KILAVUZU.md evren modeli · kapak aile kimliği · devam hakkı (22.08.2026)
│   ├── YAYIN_VE_PERFORMANS_KILAVUZU.md    ⭐ akışın SON adımı: gerçek veri → kılavuz revizyonu (22.08.2026)
│   ├── ONERME_VE_NOVUM_KILAVUZU.md        KONSEPT kapısı: novum tipi + taşıyıcı satırı + üç kabul testi (22.08.2026)
│   ├── FINAL_VE_PAYLASIM_KILAVUZU.md      final tipi → davranış · tohum bilgi %10-15 · görsel ikilem (22.08.2026)
│   ├── DIKEY_MIKRO_DRAMA_KILAVUZU.md      9:16 dramaturjisi: 6×8 vuruş tablosu · kinesik reset (22.08.2026)
│   │                                      ⭐ §4.1 vizör açık döngüsü · §4.2 vekil nesneler · §6.1 AI ALGISI KAPISI (27.08.2026)
│   ├── PAKETLEME_VE_VAAT_KILAVUZU.md      kapak ANI senaryoda seçilir · vaat-teyit · spoiler bütçesi (22.08.2026)
│   ├── TEMA_MUHENDISLIGI_KILAVUZU.md      tema seçimi + tema→motif→sahne matrisi + süre-tatmin kuralı (22.08.2026)
│   ├── KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md  8 açının anlam sözlüğü + vuruş→açı tablosu + abartı eşikleri (22.08.2026)
│   ├── ACI_YAYI_VE_SEKANS_KILAVUZU.md     açı/ölçek sıçrama bandı + kurulum sayısı + yay şablonları (22.08.2026)
│   ├── MESHUR_SAHNE_KALIPLARI_KILAVUZU.md 20 ikonik sahne kalıbı + taşınabilirlik + homage/telif sınırı (22.08.2026)
│   ├── SKILL_KULLANIM_KILAVUZU.md         ajan skill envanteri + akış eşlemesi + öncelik kuralı (27.08.2026)
│   ├── POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md 🆕 01.09.2026 · ÜRETİM REDDİ:
│   │                                      §1 sınıflandırma ağacı · §2 SÖZLÜK (kelime) ·
│   │                                      §3 KOMPOZİSYON YÜZEYİ · §4 AKSİYON BÜTÇESİ +
│   │                                      anlam maliyeti · §5 kurtarma merdiveni · §6 motorlar
│   │                                      ⛔ §4 ATLANMAZ: bu kılavuz beşinci yasak olmamalı
│   │                                         (05_DIKEY_HAT_TESHISI §3 mekanizması)
│   │                                      KAPI: prompt_kontrol ⑯ (kelime) ·
│   │                                            PROMPT_QA §3c (kompozisyon) · 03_PLAN_ONCESI B6
│   │
│   ├── QA_PROMPTLARI/             🔍 RUBRİKLER (girdi) — üretilmiş işi eleştirir
│   ├── RAPOR_KONTROL/             🧮 rapor_kontrol.py — QA raporunun ÇIKTI kapısı (01.09.2026)
│   │                                 n·Σ·ort yeniden hesap · tally · şerit · ⑨ ızgara · ⑤ çapraz + SUSKUNLUK
│   │                                 T tablosuna satır bu betik koşulmadan YAZILMAZ [D161·D162]
│   │   │  ⭐ dördü de SALT PROMPT + TEK DOSYA çalışır: medya + rubrik,
│   │   │     başka hiçbir şey. Rubriğe YAZILMAZ: Türkçe not, tarih,
│   │   │     film adı, [DERS n] etiketi, depo yolu. Ders GÖVDEYE KURAL
│   │   │     olarak girer; numarası CALISTIRMA_KAYITLARI'ndaki iz
│   │   │     defterinde durur (17.08.2026 temizliği).
│   │   │     MOD D = SPEC verildi · MOD V = sadece video (skor `Ⓥ` işaretli)
│   │   ├── 00_README.md              ⭐ klasör rehberi: çalıştırma tarifi,
│   │   │                             mod sistemi, ajan akışı (kart eşlemesi)
│   │   ├── CALISTIRMA_KAYITLARI.md   koşu tarihçesi + ders dipnotları —
│   │   │                             12.08.2026'da rubriklerden taşındı
│   │   ├── FILME_OZEL/               film-özel üretim kapıları (tabloya girmez)
│   │   ├── ARSIV_6_MERCEK/           ⛔ eski 6 rubrik — ÇALIŞTIRILMAZ, kanıt
│   │   ├── 1_KARE_QA_CRITIQUE_PROMPT.md         ① sahne içi · yatay VEYA dikey
│   │   ├── 2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md   ② sahneler arası · dünya+gövde
│   │   ├── 3_SES_QA_CRITIQUE_PROMPT.md          ③ film boyu ses · YALNIZ KURGU
│   │   ├── 4_HIKAYE_QA_CRITIQUE_PROMPT.md       ④ film boyu anlatı · (+PLAN)
│   │   ├── 5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md    ⑤ 🔬 derin tarama · özne-dışı
│   │   │                                        alan · risk tetikli · /4'e girmez
│   │   └── 6_FIZIK_QA_CRITIQUE_PROMPT.md        ⑥ 🔬 derin tarama · sayısal
│   │                                            fizik (+KİLİT LİSTESİ = mod D)
│   │
│   ├── FILM_QA_RAPORLARI/         📊 SONUÇLAR (çıktı) — buraya YAZILIR
│   │   ├── 00_INDEX.md               ⭐ PROJEDEKİ TEK SAYAÇ + tamlık matrisi
│   │   ├── 01_FILM_RAPORLARI/        film başına kalıcı QA kaydı
│   │   ├── 02_HAM_RAPORLAR/          modelin ham çıktısı, dokunulmaz
│   │   ├── T1_KARE_KALITE.md         ① skorları        ⭐ CANLI
│   │   ├── T2_DEVAMLILIK_KALITE.md   ② skorları        ⭐ CANLI
│   │   ├── T3_SES_KALITE.md          ③ skorları        ⭐ CANLI
│   │   ├── T4_HIKAYE_KALITE.md       ④ skorları        ⭐ CANLI
│   │   ├── T5_ARKA_PLAN_KALITE.md    ⑤ skorları · derin tarama, matrise girmez
│   │   ├── T6_FIZIK_KALITE.md        ⑥ skorları · derin tarama, matrise girmez
│   │   ├── 03_ · 04_ · 05_ · 06_ · 07_   ⛔ KAPALI (22.08) — eski 6 mercekli
│   │   │                             sistemin skorları; yeni satır YAZILMAZ,
│   │   │                             yenilerle KARŞILAŞTIRILAMAZ
│   │   ├── 08_YAYIN_PERFORMANS_TABLOSU.md ⭐ tek İZLEYİCİ tablosu — diğer
│   │   │                             dördünü bir model doldurur, bunu
│   │   │                             gerçek veri doldurur (22.08 açıldı)
│   │   │                             (LESSONS_LEARNED teknik tablosu da
│   │   │                              22.08'de KAPANDI → T1)
│   │   └── 09_URETIM_RED_DEFTERI.md  🆕 01.09.2026 · ⭐ RED SAYILARININ TEK
│   │                                 SAYAÇI. Politika/teknik red vakası ·
│   │                                 MOTOR · sınıf · tetikleyici · uygulanan
│   │                                 çözüm · SONUÇ. 14 vaka geriye dönük.
│   │                                 ⛔ Satır RED GELDİĞİ GÜN açılır;
│   │                                    geriye dönük satır GEÇERSİZDİR.
│   │                                 Kural: ../POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md
│   │
│   └── URETIM_ONCESI_ANALIZ/      🧪 META-ANALİZ — üretmeden önce oku
│       ├── 01_DERS_ETKINLIK_RAPORU.md    hangi ders işe yaradı, hangisi yaramadı
│       ├── 02_RISK_KARTLARI.md           malzeme başına geçmiş bozulma oranı
│       ├── 03_PLAN_ONCESI_KONTROL_LISTESI.md  14 madde · ~20 dk · maliyet sıfır
│       │                             (26.08.2026: B3 tema indeksi +
│       │                              B4 açı yayı eklendi)
│       └── 04_ARASTIRMA_BULGULARI.md  ⭐ dış araştırma SÜZME KAYDI: hangi
│                                     bulgu hangi kılavuza indi, hangisi
│                                     GİRMEDİ ve neden (27.08.2026, 1. tur)
│                                     ⛔ kural buradan okunmaz — kuralın
│                                        NEREDEN geldiği buradan okunur
│       └── 05_DIKEY_HAT_TESHISI.md ⭐ 30.08.2026 · HAT TEŞHİSİ (tek filme
│                                     değil, 18 filme birden bakar): dikey
│                                     hattın neden aynı filmi 18 kez yazdığı
│                                     · 0/18 replik · 0/18 ikinci insan
│                                     · dört üretim önleminin hikâye
│                                     formatına dönüşme mekanizması
│                                     ⛔ DİKEY FİLM YAZMADAN ÖNCE OKU
│
├── dikey_shorts_filmler/          9:16 · FİLM KLASÖRÜ (25.08.2026'da tek
│                                  dosyadan klasöre geçti — film + varsa
│                                  QA_SPEC artık kendi klasöründe)
├── yatay_2_4_dk_filmler_uzay/     16:9 · FİLM KLASÖRÜ · bilimkurgu
│   (yatay_2_4_dk_filmler_zombi/ — 26.08.2026'da kart H2 ile KALDIRILDI.
│    Depo yalnız UZAY filmleri içindir; zombi türü de kapandı. Tür kartı
│    KILAVUZ_REHBERI §4.2'de ⏸️ RAFTA duruyor, silinmedi.)
├── yatay_3_5_dk_filmler/          16:9 · FİLM KLASÖRÜ (PLAN + PART_A/B + KAPAK)
├── yatay_7_9_dk_filmler/          16:9 · FİLM KLASÖRÜ + kendi kilavuzlar/ dizini
│   └── kilavuzlar/kalite_kontrol/    ⚠️ bu formatın AYRI 3 geçişli QA sistemi
├── yatay_10_20_dk_filmler/        16:9 · 3 PERDE · FİLM KLASÖRÜ
│   └── THE_SECOND_SHIP/              120 sahne × 10s = 20:00 (8s'den sapma)
│
└── film_analizleri/               🎞️ DIŞ FİLM ANALİZLERİ — bizim yapmadığımız
    │                                 filmler, 20 parça × 3 mercek (KAMERA·OLAY·
    │                                 TEMA) + SENTEZ · film sayımına GİRMEZ
    ├── ANALIZ_QA_PROMPTLARI/         salt promptlar (video + tek dosya)
    └── ANALIZ_EDILEN_FILMLER/        film başına klasör (KUNYE + raporlar)
```

**Format seçimi, tür kilitleri, fizik kuralları → hepsi `KILAVUZ_REHBERI.md`'de.
Burada tekrarlanmaz.**

---

# 2. DEĞİŞMEZ KURALLAR

```
① SAYI TEK YERDE DURUR
   Film/ders/QA sayısı yazacaksan: 00_INDEX.md. Başka hiçbir belgeye yazma,
   kaynağa işaret et. Yazmadan önce: bash .../sayac.sh

② HER FİLM DOSYASI MARKDOWN BAŞLIĞI KULLANIR
   Sahne başlıkları ## ile başlar: "## 🎬 SAHNE 3 — BAŞLIK"
   Emoji ile başlayan düz satır YETMEZ. Gerekçe: sayaç, grep taraması ve
   herhangi bir gelecek parser başlıktan sayar — başlıksız dosya sayımdan
   ve taramadan düşer (4 dosyada oldu — bkz. §6; web paneli döneminde
   film fiilen sistemden kayboluyordu, panel gitti ama kural kalır).

③ PROMPT SELF-CONTAINED'DIR
   "[BIBLE'a bak" atfı yasak. Her prompt tek başına çalışmalı.
   Uzunluk bandı ve yasak kelimeler: KILAVUZ_REHBERI §7.

④ QA RAPORU GELDİĞİNDE HAM ÇIKTI KORUNUR
   Önce 02_HAM_RAPORLAR/ altına olduğu gibi kaydet, sonra özetle.
   Bu depoda 11 filmin ham raporu bir kez kayboldu. Tekrarlatma.

⑤ İŞ BİTİNCE COMMIT
   Yarım bırakma. Commit mesajı formatı: §5.

⑥ ÖLÇÜM SAPMASINI UNUTMA
   Aynı rubrik aynı filmi iki kez ölçtü, kategoriler 2 puana kadar oynadı.
   1.5'tan küçük skor farkları GÜRÜLTÜDÜR — "A filmi B'den iyi" deme.
   Ayrıntı: 00_INDEX.md · URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md §6b
```

---

# 3. GÖREV KARTLARI

> Her kart: **tetikleyici → dokunulacak dosyalar (sırayla) → bitiş kontrolü.**
> Karttaki sırayı bozma; sonraki adım öncekinin çıktısını kullanır.

---

## 🎬 A — YENİ FİLM YAZACAĞIM

**Kılavuz:** `KILAVUZ_REHBERI.md` §1 (dört soru) → §2/3/4 (kartlar) → §6 (akış)

```
OKU
 □ KILAVUZ_REHBERI.md · dört soruyu sırayla cevapla, okuma listeni çıkar
 □ URETIM_ONCESI_ANALIZ/05_DIKEY_HAT_TESHISI.md  ⛔ DİKEY FİLMSE ÖNCE BU
      → §5① İSTEK/ENGEL/BEDEL satırı yazılmadan sahne haritası yazılmaz;
        "anlamak / görmek / fark etmek" İSTEK DEĞİLDİR (30.08.2026)
 □ URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md   ⛔ PLAN YAZILMADAN ÖNCE
      → 5+ risk çıkıyorsa malzeme azalt; prompt iyileştirmek işe yaramıyor
 □ Bölüm 8 film matrisindeki en yakın filmi şablon olarak aç

YAZ
 □ Filmin KLASÖRÜNÜ doğru format klasörüne aç (§1 haritası) —
   25.08.2026'dan beri İSTİSNA YOK: her format film başına klasör
 □ ⭐ İSKELET TEK YERDE TANIMLI: KILAVUZ_REHBERI §2.0 (01.09.2026).
   Buraya kopyalanmaz, oradan okunur. Kopyalanabilir hâli:
      cp -r kilavuzlar_ve_sistem_dosyalari/FILM_KLASOR_SABLONU \
            <FORMAT_KLASORU>/<FILM_ADI>
   Yedi dosya: PLAN · BOLUM_1 · BOLUM_2 · KAPAK · MUZIK ·
               YAYIN_PAKETI (TAMAMEN İNGİLİZCE) · QA_SPEC
   Bölüm sayısı formattan gelir; 7-9 ve 10-20 dk'da faz sayısı kadardır.
   ⛔ Format klasörünün köküne .md BIRAKMA — orada yalnız 00_README
      durur; sayaç kökteki her girdiyi BİR FİLM sayar.
   ⛔ Eski filmler YENİDEN BÖLÜNMEZ/ADLANDIRILMAZ. İskelet YENİ filmler
      içindir; toplu yeniden adlandırma ölçülmüş hiçbir sorunu çözmez ve
      QA kayıtlarındaki dosya adlarını bayatlatır.
 □ Adlandırma: <FILM>_<ROL>.md · BUYUK_HARF_ALT_CIZGI · Türkçe karakter yok
      film adı ÖNDE durur [D160/⑪.0: dosya klasörden çıkınca adı tek kimliği]
 □ Sahne başlıkları ## ile (kural ②) — ve YALNIZ bölüm dosyalarında
      (plandaki örnek bir prompt sahne dizisine karışır)
 □ PLAN → BIBLE → PROMPT sırası (KILAVUZ_REHBERI §6)
 □ ⭐ SAHNE HARİTASI YAZILIRKEN İKİ BÜTÇE DAĞITILIR (22.08.2026) —
      ikisi de üretimden SONRA eklenemez:
      · KARAKTER_VE_DUYGU_KILAVUZU.md §6 — göz · tepki planı · el ·
        yürüyüş · eşya sahnelerinin sayısı formattan hesaplanır
      · KURGU_RITMI_VE_IHRAC_KILAVUZU.md §2 — ardışık iki sahne aynı
        ölçek + palet + ses dokusunda OLAMAZ (örüntü kırıcı kapısı)
 □ ⭐ TEMA SATIRI + SAHNE İNDEKSLERİ (26.08.2026)
      TEMA_MUHENDISLIGI_KILAVUZU.md §3 (sekiz tema) → §5 matrisinden
      motif dağıtılır → §9. Tema EN AZ 3 sahnede motife dönüşür ve o
      sahne numaraları plana yazılır; yazılmayan tema dekoratiftir
      (Kaleida Crash kaydı: "bedel yok → tema dekoratif kalıyor").
      Betik TEMA satırını ve sahne indekslerini arar.
 □ ⭐ SAHNE-KURULUM DİZİSİ (26.08.2026)
      ACI_YAYI_VE_SEKANS_KILAVUZU.md §3 güvenli bant (ardışık çift:
      ≥1 ölçek kademesi VE ≥45°) · §4 kurulum sayısı bandı · §9 kontrol.
      Açı TİPİ sayısı ≥3 (KAMERA_ACISI §2) — üç kurulumun üçü de alttan
      bakıyorsa çeşitlilik yok, yalnız mesafe değişiyor.
      ⛔ Bu, KART 8'in lockoff kararıyla ÇELİŞMEZ: lockoff KLİP İÇİDİR.
 □ ⭐ <FILM>_QA_SPEC.md yazılır — yazım paketinin son parçası [Ders 117]
      A bloğu ④ HİKAYE alanları · B kurgu geometrisi + İNSAN ŞERİDİ ·
      C belgesiz merceklerin FLAGS sorularını cevaplayan kilitler
      + TARGET ASL BAND / ASL CURVE satırları (KURGU_RITMI §1; sabit
        ızgaralı filmde gerekçe satırı ZORUNLU [D74])
      ⛔ REPLİK ZAMANLARI VE DORUK SAATİ HESAPLANMAZ, HESAPLATILIR [D122]:
        replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
        doruk başlangıcı = hook + (doruk_sahne − 1) × klip
        Elle yazılan her kayıt er geç ızgara formülüyle çelişir ve ⑨
        HİZALAMA KAPISI'nın ölçü aletini bozar — bir filmde 4 replik
        kaydının 2'si bir yuva geç yazılmıştı ve kapı doğru bir kurguyu
        "kaymış" okuyacaktı. Yazıldıktan sonra her kayıt formülle
        doğrulanır; sapma varsa yazım paketi TAM DEĞİLDİR.
      ⭐ B bloğuna FİNAL VURUŞ KANITI satırı [Ders 141]: tek karede BULUNAN
        ya da BULUNMAYAN, sayılabilir ve adı konabilir bir nesne + saniyesi
        + kaç tane. Kurgu kapısının dördüncü satırı bunu okur.
      ⭐ E bloğundaki her MAKİNE KAPISI kuru koşuyla DOĞRULANIR [Ders 142]:
        ffmpeg -hide_banner -filters | grep -q " <filtre> " || kapıyı yeniden yaz
        Her kapı üç satır taşır: KOMUT · DOĞRULANDI (<ffmpeg sürümü·tarih>)
        · İKAME (filtre yoksa hangi ölçüm koşulur). DOĞRULANDI satırı
        olmayan kapı YAZILMAMIŞTIR — bir SPEC'in kamera sabitlik kapısı
        kurulu olmayan bir filtreye yazılmıştı ve sessizce hiç koşmadı.
      ⛔ SPEC dosyası yoksa film "yazımı tamam" sayılmaz
 □ ⭐ SPEC YAZILIR YAZILMAZ QA PAKETİ ÜRETİLİR — burada, QA anında DEĞİL
      [Ders 165 · 02.09.2026]
        bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü>
      → QA_PROMPTLARI/FILME_OZEL/<FILM>/PAKET_1..8 (koşması 1 saniye)
      ⛔ Bu klasör yoksa film "yazımı tamam" DEĞİLDİR.
      Sebep: paket yalnız qa-isle §2b'de tarif edilmişti; operatör QA anında
      skill değil RUBRİK açar ve çıplak rubriği yapıştırır. D129'un aracı
      01.09'da yazıldı, ertesi gün yazılan filmin paketi hiç doğmadı ve
      THE STILL SWARM sekiz mercekle mod V koştu — sekizi de tabloya giremedi.
      SPEC değişirse betik yeniden koşulur; paket ELLE düzenlenmez.

KONTROL ET
 □ URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md · 14 madde
      → maliyeti sıfır, 11 maddesi gerçek filmlerde gerçekten oldu
 □ ⭐ PROMPTLAR YAZILDIKTAN SONRA, TEK KARE ÜRETMEDEN → görev kartı P

GÜNCELLE
 □ KILAVUZ_REHBERI.md §8 film matrisine satır ekle
 □ FILM_QA_RAPORLARI/00_INDEX.md → tamlık matrisine "0/4" satırı ekle
 □ Klasörün README.md'si varsa film listesine ekle

BİTİŞ
 □ bash sayac.sh → toplam film sayısı 1 arttı mı
 □ commit
```

---

## 🔎 P — PROMPTLAR YAZILDI, ÜRETİM BAŞLAMADI

**Kapı:** `PROMPT_KONTROL/` · akıştaki yeri: KILAVUZ_REHBERI §6 adım 3.5
*(12.08.2026'da açıldı — 31.07'de yazıldığı söylenen dosya hiç
commit'lenmemişti; 18 commit tarandı, tek iz yok.)*

```
⛔ BU KART ATLANIRSA PARA HARCANIR. Buradaki her denetim üretimden
   ÖNCEdir ve sıfır kare tüketir.

1. BETİĞİ KOŞ — sayıları o hesaplar, sen yazma
     python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py <FİLM KLASÖRÜ>
     ⛔ KLASÖR ver, tek bölüm dosyası değil (01.09.2026 · klasör modu).
        Film bölüm dosyalarına ayrıldığından beri dizi kapıları dosya
        sınırında körleşiyor: 6 sahnelik dikey film ikiye bölününce dosya
        başına 3 video promptu kalır ve AÇI/KURULUM kapısı HİÇ koşmaz.
        Çıktıda `📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik` satırı yoksa
        o kapılar koşmamıştır. Gerekçe: KILAVUZ_REHBERI §2.0
     çıkış kodu 2 (BLOCK) → düzelt, tekrar koş, 2'ye geçme
     çıkış kodu 1 (FIX)   → bulguları oku, bilinçli sapma varsa dosyaya
                            TEK SATIR gerekçe yaz (D74: kaydı olmayan kapı)

2. RUBRİĞİ KOŞ — betiğin göremediği tek şey için
     PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md
     → kilit SAYI mı TARİF mi · sahne hangi dersi tetikliyor · A1
     → ⭐ §3c KOMPOZİSYON YÜZEYİ (01.09.2026): betik kelime sayar,
       KADRAJI okumaz. YERCEKIMI F1 S8 kelimeleri temizken reddedildi
       ve sahne İPTAL EDİLDİ — bu dört soru o vakadan doğdu.

2b. REPLİKLİ FİLMDE İKİNCİ RUBRİK (03.09.2026 · TUR 6)
     PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md
     → girdi: B5 omurgası + replik tablosu (İŞLEV sütunlu) + bölüm
       promptları · satır başına ETİKET üretir, SAYI üretmez
     → CUT / UNCLEAR register / MONOLOGUE bulgusu varken GO YOK
     → kural tarafı: SES_VE_DIYALOG_URETIM_KILAVUZU.md §2a

3. KARAR
     GO    → üretime geç (önce imaj, onaylanınca video)
     BLOCK → üretme. 5+ risk çıkıyorsa malzeme azalt; prompt
             iyileştirmek bu bandda işe yaramıyor.

⚠️ Betik bir SAYI değiştirdiyse (bant, eşik) belgeye elle yazma —
   prompt_kontrol.py başındaki sözlük tek kaynaktır.
```

---

## 🎥 B — FİLM ÜRETİLDİ (video çıktı)

```
 □ Üretim notlarını film dosyasının sonuna ekle
      hangi model · kaç deneme · reddedilen prompt varsa sebebi
 □ ⛔ RED ALDIYSA — SAYI FİLM DOSYASINA YAZILMAZ (01.09.2026):
      FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md → satır aç
      · mesajı BİREBİR kopyala (sınıflandırma kelimeye bakıyor)
      · MOTOR sütununu doldur — NBP / NB2 / OSMI / VEO
        (14 eski vakanın 13'ünde motor yazılmamış; `?` yazmak satırı
         yarım bırakmaktır)
      · çözümü uygula, sonra SONUÇ sütununu DOLDUR
        ⛔ Çözümü kaydedilmeyen red kaydı yalnız bir şikâyettir
      · kurtarma sırası: POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md §5
        ⛔ Aynı kareye ÜÇÜNCÜ sözcük denemesi yok — kamera taşınır
 □ Yeni bir tuzak/red sebebi çıktıysa → KILAVUZ_REHBERI.md §7 BİLİNEN TUZAKLAR
      (rehberin en değerli bölümü, besle) · kelimeyse ayrıca
      prompt_kontrol.py POLITIKA_T1/T2 sözlüğüne
 □ Müzik → <FILM>_MUZIK.md · GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md §7-19
 □ Kapak → <FILM>_KAPAK.md · KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md (metinsiz üret)
 □ Fragman yazılacaksa: FRAGMAN_KILAVUZU.md (dikey 3-6 / yatay 8-12 vuruş)
 □ Paketleme → <FILM>_YAYIN_PAKETI.md · ⭐ TAMAMEN İNGİLİZCE
      kural: VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md
      kanal metni: apexaic/<platform>/PAKETLEME_SABLONU.md (sabit bloklar ·
      hashtag kademeleri · yükleme listesi) + apexaic/CAPRAZ_YAYIN.md §7
      ⛔ Sabit blok film dosyasına KOPYALANMAZ — oradan birebir yapıştırılır
      ⛔ Üç platforma aynı metni yazma; Instagram caption'ın YouTube'da
        değişmeden çalışıyorsa iş yapılmamıştır.
      ⬜ AFTER THE CUT alanları (RUNTIME · paylaşılabilir an · dikey kesit)
        kurgudan ÖNCE doldurulmaz — uydurulmuş süre paketi geçersiz kılar.
 □ İhraç: KURGU_RITMI_VE_IHRAC_KILAVUZU.md §6 (1440p+ · −14 LUFS · −1,0 dBTP)
 □ ⛔ QA'DAN ÖNCE, SIRAYLA (01.09.2026):
      bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>          ⑪ · kuyruk kartı · köşe · ses kanalı
      bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> <master>
                                                                             → QA_PROMPTLARI/FILME_OZEL/<FILM>/ (mod D paketleri)
      Operatör PAKETİ yapıştırır, çıplak rubriği değil [D129 · 9 film mod V koştu]
 □ 00_INDEX.md → filmin durumunu "üretildi" olarak işaretle
 □ Yayınlanacaksa → görev kartı Y
 □ commit
```

---

## 📡 Y — FİLM YAYINLANACAK / YAYINLANDI

**Kılavuz:** `YAYIN_VE_PERFORMANS_KILAVUZU.md` · tablo:
`FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md`
*(22.08.2026'da açıldı — üretim akışı 11. adımda bitiyordu, yayın sonrası
ölçüm hiçbir dosyada yoktu. Deponun bütün hook/kapak/başlık sayıları
DIŞ ARAŞTIRMA hipotezidir ve bu kart koşulmadan test edilmez.)*

```
⛔ SATIR YAYINDAN ÖNCE AÇILIR. Geriye dönük açılan kayıt 🚨 GEÇERSİZDİR:
   hangi kapak, hangi başlık, hangi hook tipi — bunlar sonradan
   hatırlanarak yazılamaz (kimlik kapısının yayın karşılığı).

YAYINDAN ÖNCE
 □ 08_YAYIN_PERFORMANS_TABLOSU.md → §1 kimlik satırı doldur
 □ Paketleme: apexaic/<platform>/PAKETLEME_SABLONU.md (kanal için doldurulmuş
   VIRAL_BASLIK) + apexaic/CAPRAZ_YAYIN.md §7 çapraz liste
 □ Plan B kapağı hazır mı (KAPAK_FOTOGRAFI §7.2)
 □ ⛔ TEK DEĞİŞKEN KİLİDİ: ilk 48 saatte kapak VEYA başlık — ikisi değil
 □ Seri/playlist kararı: SERI_VE_KANAL_STRATEJI_KILAVUZU.md §5.1
      (bir film YALNIZ TEK resmi seride yer alabilir)

24 / 48 / 72 SAAT
 □ §2 metrik satırı · §3 eğri teşhisi · §4 karar satırı
 □ ⭐ Terk saniyesi IZGARA ARİTMETİĞİYLE SAHNEYE çevrilir —
      hizalama kapısıyla (ortak adım ⑨) aynı formül
 □ Suçlu değişken eleme sırası: paketleme → kurgu → ses → sahne →
      plan → format (ucuzdan pahalıya, kılavuz §4.2)

GERİ BESLEME — bu kartın VAR OLMA SEBEBİ
 □ Kılavuz §6 tablosundan hangi belgenin revize edileceğini bul
 □ ⛔ SIRA: veri → BELGE revizyonu → (ancak tekrarlarsa) ders.
      Yeni ders yazmak ilk refleks DEĞİLDİR [AGENTS §8]
 □ ⭐ QA skoru yüksek + gerçek metrik düşük çıktıysa: yanlış olan
      RUBRİKTİR → URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md
 □ Devam adaylığı: SERI_VE_KANAL_STRATEJI_KILAVUZU.md §4.2
      (üç filmde ölçülmeden tam kapıya geçilmez)

BİTİŞ
 □ Tablo satırı geçerlilik işareti taşıyor mu (✅ / ⚠️ / 🚨)
 □ commit
```

---

## ⛔ C/D/E/E3/F/F2'NİN ORTAK ADIMLARI — her rapor işlemede önce bunlar

```
① SPEC KAPISI [Ders 94 · teslim biçimi Ders 117 · ÖNKOŞUL Ders 129]
   ⛔ BU KAPI KOŞUDAN ÖNCE KOŞAR — etiket değil, ÖNKOŞUL [D129]:

        f=$(ls <FILM klasörü>/*_QA_SPEC.md 2>/dev/null)
        [ -n "$f" ] && echo "SPEC VAR → mod D ZORUNLU: $f"

      SPEC dosyası VARSA ve rapor `INPUT MODE: D` yazmıyorsa koşu
      TEKRARLANIR: ham rapor 02/'ye düşer, T tablosuna SATIR YAZILMAZ,
      kesme listesi / REMOVE reçetesi / yeniden üretim UYGULANMAZ.
      Bir koşuyu ŞARTLI diye tabloya almak onu yapılmış saymaktır — ve
      D117'nin çözümü (SPEC'i dosyaya çıkarmak) UYGULANDIĞI HÂLDE mod D
      sayısı 0 kaldı: erişim engeli kalktı, davranış değişmedi.
      Bedeli THE ROSE COAT'ta ölçüldü: ④'ün kesme listesindeki beş
      adayın beşi de yük taşıyan sahne, ikisi SPEC'te "KESİLEMEZ" yazan
      viral, dördüncüsü filmin DORUĞU + KAPAK KARESİ.
   ⛔ SPEC BİR DOSYADIR, BÖLÜM DEĞİL. Aranacak yer önce film klasöründeki
      `<FILM>_QA_SPEC.md`; yoksa planın `📋 QA SPEC BLOĞU` bölümünden ÇIKARILIR
      ve o dosya açılır — QA anında operatörün eline iki dosya verilir:
      rubrik + SPEC. Blok planın içinde kaldığı sürece mod D koşulmuyor:
      SPEC hazır olduğu hâlde mod V koşulan film sayısı **10**, mod D sayısı 0
      (son vaka 02.09.2026 · THE STILL SWARM · SEKİZ mercek birden).
   ⛔ AMA ARTIK OPERATÖRE İKİ DOSYA VERİLMEZ, TEK PAKET VERİLİR [Ders 165]:
      `QA_PROMPTLARI/FILME_OZEL/<FILM>/PAKET_1..8` — rubrik + SPEC'in ilgili
      bloğu tek dosyada, mod D gömülü. Paket FİLMİN YAZIMINDA üretilir
      (Kart A §4), QA anında değil: paket yoksa operatör çıplak rubriği
      yapıştırır ve koşu daha başlamadan mod V olur.
   Filmin planında `📋 QA SPEC BLOĞU` var mı (2-4 dk dosyalarında §0.15)?
   VAR + rapor mod V ise  → koşu bir ÖN KOŞU'dur:
        · skor satırı tabloya Ⓥ ⚠️ ŞARTLI girer,
        · 00_INDEX tamlık matrisinde o mercek hücresi ❌ KALIR,
        · kesme listeleri ve REMOVE reçeteleri UYGULANMAZ.
   Mod D bu depoda hâlâ hiç denenmedi; SPEC hazır olduğu hâlde mod V
   koşulan film sayısı 5 (Slow Stone · Starless Circle · Third Dune ·
   Ring Light · Banded Deep — 14.08, üç mercek birden).

①.5 RAPOR KONTROL BETİĞİ [Ders 161 · 162]  ⛔ ⑤'TEN ÖNCE · RAPOR BAŞINA ~1 sn
     python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
             <ham raporlar…> --film <film klasörü> [--hook 10 --klip 10] [--rapor]
   ⭐ ⑪ ÖLÇÜM HAKEMLİĞİ [AGENTS §3: "rapor ile ölçüm çelişirse ÖLÇÜM kazanır"]
     [--olcum-kesme <n>] [--olcum-sahne <n>]
   Master ölçüldüyse (olcum_kapisi.sh) ölçülen sayıları VER. Ölçüm verilmezse
   kesme yayılımı > 1 partiyi TOPTAN düşürür [D107] — oysa anlaşmazlık çoğu
   zaman ölçümle zaten çözülmüştür. Ölçüm verilince parti AYAKTA kalır ve
   yalnız sapan mercek tekil olarak ŞARTLI olur, sapması adıyla yazılır.
   ⛔ Ölçüm YOKSA bu bayrakları UYDURMA — ölçülmemiş sayı hakem olamaz.
   Raporu KENDİ tablosundan yeniden hesaplar: n · Σ · Σ/n · tally (yazılı
   etiketlerden) · "no in-scope source"+sayı → `—` [D131] · 0 replikte
   diyalog-yalnız hücre → N/A · şerit uzunluğu · ⑨ ızgara · ④ harita ↔ kesme
   · ② sayaç boşluğu [D134] · birden çok raporda ⑤'in beş satırı (kesme ·
   sahne · şerit · replik · ⭐ SUSKUNLUK [D162]).
     GEÇERSİZ / TEKRAR → T tablosuna satır YAZILMAZ · ŞARTLI → düzeltilmiş
     ortalama Ⓥ ⚠️ ŞARTLI girer · çıkış kodu 2/1/0.
   Sebep: altı rubriğin ARITHMETIC GATE'i büyük harfle yazılıydı, hiçbir dış
   kapı denetlemiyordu; bir partide 6 raporun 5'i geçemedi, biri fabrike
   toplam bastı. ⑤ raporları BİRBİRİYLE karşılaştırır; bu betik her raporu
   KENDİSİYLE karşılaştırır ve ⑤'ten geçen bir fabrike toplamı yakalar.
   ⛔ Betik BULGUNUN DOĞRULUĞUNU ölçmez (o iş ⑪ + ② defteri); raporun kendi
      içinde tutup tutmadığını ölçer.

② KİLİT ÇELİŞKİSİ DEFTERİ [Ders 96]
   Raporun, planda YAZILI bir kilide aykırı her bulgusu — bulgu listesinden
   ALINIR ve film kaydına şu deftere yazılır:
     | # | rapor ne dedi (timecode) | hangi kilit (§) | çözüm eylemi | sonuç |
   çözüm eylemi = master'ın O SANİYESİNİ izlemek/dinlemek (~10 sn iş)
   sonuç        = FİLM SAPTI / RAPOR UYDURDU / ⬜ AÇIK
   ⛔ ⬜ AÇIK madde varken: o merceğin skoru ŞARTLI, bulgudan ders
      yazılmaz, yeniden üretim siparişi verilmez.
   Sebep: aynı cümle hem "film bozuldu" (Ring Walker) hem "rapor uydurdu"
   (Low Power) olabilir; rapor tek başına ikisini ayırt edemez.

③ KİMLİK KAPISI [Ders 105]  ⛔ ①'DEN ÖNCE KOŞULUR
   Ham rapor bir film adının altına dosyalanmadan önce: raporun sahne
   listesinden belgeye METİN OLMAYAN en az İKİ çapa eşlenir —
     · bir vuruş/sahne (ne gösteriyor)  ·  bir sayısal kilit (kaç, kaç
       metre, hangi yön)
   eşleşme < 2 → koşu UNATTRIBUTED: ham rapor korunur, film kaydı açılır,
                 ⛔ SKOR SATIRI YAZILMAZ, bulgudan ders yazılmaz
   ⛔ EKRANDAKİ YAZI ÇAPA DEĞİLDİR. Başlık kartı filmin en ağır ihlalidir;
      kimlik kanıtı olarak da geçersizdir — rubrik modele yasaklıyor,
      aynı yasak operatör için de geçerli.
   Sebep: Black Cradle fragmanında 15 kategorilik bir rapor + REGENERATE
   hükmü, altı vuruşun altısı tutmayan bir kurgu için üretildi; raporu
   filme bağlayan tek kanıt yanan başlık kartıydı (Starless Circle'da
   aynı şüphe 06.08'den beri çözülmedi).

④ KURGU KAPISI KAPISI [Ders 109 · 118 · 120 · 121]  ⛔ RAPOR İSTENMEDEN ÖNCE
   ⛔ ÖNCE AYIKLA, SONRA SAY [Ders 93 · eşik Ders 120'de kaldırıldı]:
      sayım yapılmadan önce SAHNE-DIŞI MALZEME ayrılır — ekranda metin
      taşıyan / statik / hiçbir sahnenin parmak izini taşımayan klip.
      ⛔ SÜRE ÖLÇÜT DEĞİLDİR. Eski "≤ 6 s" eşiği kaldırıldı: 14 saniyelik
      bir kart 4 saniyelikten daha az sahne değildir, ve eşik kartı
      büyüdükçe koruyordu.
      Kurgunun başında veya sonundaysa: kayda TEK SATIR yazılır
      ("kart 4 s"), 🔴 loglanır [D70/72] ve hem SAYIMIN hem SÜRENİN
      DIŞINDA tutulur. Ortasındaysa bu başka bir kurgudur, koşu durur.
      Kartın in-out'u raporların `NON-SCENE MATERIAL` satırından okunur;
      raporlar çelişiyorsa kapı koşulmaz, süre master'dan okunur.
      Sebep: eklenen 5 saniyelik bir kart, sahne şeridi plana birebir
      uyarken kapıyı düşürür ve ölçümü iptal ettirir. Ve tersi de oldu:
      6 saniyeyi aşan tek bir kart, dört merceğin dördünde farklı
      yutulup partiyi ⑤'ten düşürdü [D120].
   QA koşulmadan önce ÜÇ satır doğrulanır (sahne şeridi üzerinde):
     a) üretilen klip sayısı = planın SCENE COUNT'u
     b) kurgunun süresi      = planın RUNTIME'ı ± 2 s
     c) kurgunun SIRASI    = planın İNSAN ŞERİDİ  [Ders 118]
        Plandan 1 karakter = 1 sahne yazılır (1 = insan var · - = insansız),
        aynı dize raporun "who is present" sütunundan / PRESENCE STRING
        çıktısından yazılır ve yan yana konur.
        aynı  → sıra doğrulandı
        değil → ⛔ ÖNCE ÇÖZ, SONRA PUANLA — ama "değil" deyip durma,
                FARKI OKU [Ders 121]. Fark bir ölçümdür:

                ① insansız yuvaların MUTLAK saniyeleri eşlenir
                   Δ = rapor saniyesi − plan saniyesi
                ② fazla/eksik klip = Δ ÷ klip süresi
                ③ Δ ilk insansız yuvada zaten büyükse fazlalık ÖNDE ·
                   iki insansız yuva arasında sabitse o aralık birebir ·
                   son insansız yuvadan sonraki yuva sayısı planınkinden
                   AZSA kuyrukta SAHNE EKSİK  ⛔ önce oraya bak: kuyruk
                   filmin finalidir [D62/D72]
                ④ replikli filmde aynı hesap replik ekseninde tekrarlanır
                   (raporların `LINES HEARD` satırı ↔ planın DIALOGUE
                   SCHEDULE'ı). Δ sabitse kurgu hizalı; iki replik arasında
                   SIÇRIYORSA kurgu tam orada malzeme kazanmış; AYNI replik
                   bir yuva arayla iki kez duyulduysa DUPLİKE KLİP vardır
                   (ses bulgusu değil, kurgu bulgusu)
                ⑤ iki eksen aynı sayıyı veriyorsa sonuç ÖLÇÜMDÜR: master'da
                   yalnız işaret edilen yuvalar izlenir (yuva başına ~10 s)

                Sayı ve süre tutarken sıra bozuk olabilir — bir filmin
                doruğu bu yüzden yanlış yuvada ölçüldü. Sıra bozukken de
                Δ okunabilir: bir filmin EKSİK FİNALİ bu yüzden bulundu.

        ⛔ ŞERİDİN ÇÖZÜNÜRLÜĞÜ ÖNCE ÖLÇÜLÜR [Ders 163]:
                insansız sahne / toplam sahne ≤ 1/10 ise şerit SABİTTİR ve
                sıra eksenini ÖLÇMEZ — c satırı "GEÇTİ" değil "ÖLÇMEDİ"
                yazar. Tek kâşifli bu seride varsayılan hâl budur.
                Sıra o zaman YALNIZ ⑪'in SAHNE IZGARASINDAN okunur:
                  olcum_kapisi.sh → sahne_izgarasi.jpg (kesme listesinden
                  türetilmiş sahne ortası kareleri) ↔ SPEC B sahne haritası
                Bir filmde dört sahnelik blok takası şeridi hiç bozmadan
                geçti ve ④c "SIRA DOĞRULANDI" dedi.
   ⭐ DÖRDÜNCÜ SATIR — FİNAL VURUŞ KANITI [Ders 141]  ⛔ KAREYLE KOŞULUR
     a/b/c klip SAYAR; vuruş sayamaz. Bir film üç satırın üçünü de geçip
     (6=6 · 60,033=60,03 · 111111) finalini teslim etmeyebilir: klip tam
     boyunda, doğru yuvada, insan içinde — ve twist arka planda YOK.
     SPEC'in B bloğundaki `FİNAL VURUŞ KANITI` satırı okunur, tek kare
     çıkarılır ve BAKILIR:
       ffmpeg -ss <kanıt saniyesi> -i "$M" -frames:v 1 kanit.jpg
     Kanıt SAYILABİLİR ve ADI KONABİLİR olmalı ("üç çöküntü", "sönmüş
     lamba", "boş kanca"); "final duygusu" kanıt değildir.
     ⭐ DÖNGÜ AYRI KANITTIR (dikeyde zorunlu [FINAL §2]): ilk kare ile son
     kare yan yana konur — aynı kurulum · ölçek · ışık · jest mi? Arkasına
     eklenen HER KARE (başlık kartı dâhil) döngüyü zaten öldürmüştür.
     kanıt YOKSA → koşu ÖN KOŞU'dur, Final ve Duygu Yayı SAYI TAŞIMAZ ve
     o klip yeniden üretilir.

   üçü de tutuyorsa koşu NORMAL. Biri tutmuyorsa koşu ÖN KOŞU'dur:
     · satır tabloya ⚠️ ŞARTLI girer,
     · film boyuna bakan kategoriler (Yapı · Duygu Yayı · Final ·
       Tutundurma · Ortam Devamlılığı · Kimlik Sürekliliği) SAYI TAŞIMAZ,
     · kesme listesi ve yeniden üretim siparişi UYGULANMAZ.
   ⛔ Kapı defteri kurgudan geriyse önce DEFTER güncellenir — kaydı
      olmayan kapı koşulmamış kapıdır [Ders 74].

⑤ ÇAPRAZ SAYIM KAPISI [Ders 107]  ⛔ AYNI DOSYAYA BİRDEN ÇOK MERCEK KOŞULDUYSA
   Raporların sahne/kesme sayıları yan yana yazılır:
     fark ≤ 1 → koşular birbirini doğruluyor, işle
     fark > 1 → o partinin TÜM satırları 🚨 GEÇERSİZ; tabloya girmez,
                bulgudan ders yazılmaz
   ⭐ İKİNCİ SATIR: REPLİK [Ders 121]. Raporların `LINES HEARD` satırları da
     yan yana yazılır — sayı kimin yanıldığını söylemez, alıntı söyler.
     Bir mercek ötekilerin duyduğu bir repliği HİÇ duymadıysa ya da aynı
     repliği farklı yazdıysa, o merceğin defteri o eksende 🚨'dir; partinin
     tamamı düşmez. Replik, iki modelin duymadan üretemeyeceği tek alandır.
     ⛔ Parti geçersiz olsa bile ŞERİT ve REPLİK okunmaya devam eder:
        skorlar çöpe gider, kurgu aritmetiği gitmez [Ders 121].
   ⭐ ÜÇÜNCÜ SATIR: ŞERİT [Ders 135]. Raporların `PRESENCE STRING`
     satırları da yan yana yazılır.
       hepsi aynı  → şerit ekseni doğrulandı
       biri farklı → o merceğin şeridi 🚨'dir; ⛔ önce o merceğin KENDİ
                     sahne envanteriyle karşılaştırılır — çoğu zaman
                     rapor kendi kendisiyle çelişir ve fark oradadır
     (Rose Coat: ⑤ `1111111111111` yazdı, öteki üçü `-111111111111`;
      ⑤'in kendi envanterinde S1'de figür yok. Hiçbir kapı görmedi.)
   ⭐ DÖRDÜNCÜ SATIR: METİN [Ders 159]. Raporların `OUT-OF-SCOPE FLAGS` ve
     `THE THREE THAT MATTER` satırları yan yana konur.
       aynı saniye + aynı nesne + aynı fiil iki rapordaysa → gözlem,
         kapsamı gereği SAHİBİ olan merceğin dışındaki her rapordan SİLİNİR
         (yerine "→ <mercek>" işaretçisi), sonra D108 normal işler
       işaretçi bırakan mercek ≥ 2 → oturum 🚨 KOPYA: o bulgu KAREYLE
         doğrulanmadan hiçbir tabloya, tally'ye ve verdict'e girmez
     Sebep: bir bulgu dört mercekte birebir aynı cümleyle çıktı ve KAREYLE
     YANLIŞ çıktı (örtmeyi füzyon sanmış); sayılar tutmadığı için ⑤ ✅
     vermişti. N mercekte görünen bulgu N kat güvenilir DEĞİLDİR;
     bağımsızlık kanıtlanmadıkça N kat şüphelidir.
   ⭐ BEŞİNCİ SATIR: FİLM BOYU İDDİA — SUSKUNLUK KAPISI [Ders 162].
     Bir raporda HER sahneyi ya da runtime'ın ≥%80'ini kapsayan bir ihlal
     iddiası varsa (filigran · sabit köşe işareti · sürekli metin · her
     sahnede aynı kusur), o iddia SAHİBİ olan merceğin AYNI KUTUSUYLA yan
     yana konur:
       | iddia (mercek · aralık) | sahibi mercek | sahibi ne dedi |
       sahibi AYNI şeyi yazdıysa → gözlem doğrulandı, D108 normal işler
       sahibi SUSTUYSA          → 🚨 SUSKUNLUK: iddia KAREYLE çözülür
                                  (⑪ köşe testi ya da tek kare); çözülene
                                  kadar HER İKİ merceğin de o kategorisi
                                  SAYI TAŞIMAZ
     SAHİPLİK: ekran metni/filigran/altyazı/köşe işareti → ① · arka plan
     figürü/kalabalık/ufuk/kadraj kenarı → ⑤ · kimlik/kostüm/aşınma/taşınan
     nesne → ② · ses kanalı/ambiyans/replik atfı → ③ · ölçülmüş fizik → ⑥
     Sebep: ⑤'in ilk dört satırı da MUTABAKAT arar ("iki rapor aynı şeyi mi
     söyledi"). Hiçbiri "bir rapor söyledi, SAHİBİ SUSTU mu" diye sormaz.
     Bir partide ⑤ 15/15 sahnede sabit köşe işareti bildirdi, sahibi ① kendi
     kutusunu işaretlemedi, ve film boyu 🔴 bir ihlal hiçbir kapıyı
     tetiklemeden partiden çıktı.
     → BETİK: rapor_kontrol.py birden çok rapor verilince beş satırı da basar;
       elle koşulmaz.
   Ölçüm aleti kendi içinde tutarsızken filmin puanı tartışılmaz.
   ⚠️ Ayrıca mercekler AYNI OTURUMDA koşulduysa bağımsız ölçüm değildir
      [Ders 110]: severity sayıları ve sahne sınırları birebir tutuyorsa
      bu doğrulama değil KOPYADIR — her mercek temiz oturumda koşulur.

⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME [Ders 108]
   Birden çok raporda geçen her gözlem film kaydına şu tabloyla yazılır:
     | gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
   Gözlem TEK tabloda puanlanır (sahibi = rubriklerin kapsam listesinin
   gösterdiği mercek); diğer hücreler işaretçiye iner (→🔧) ve o kategori
   kaynaksız kaldığı için DÜŞÜRÜLMEZ.

⑦ ÇAPRAZ FİLM PARMAK İZİ KAPISI [Ders 112]  ⛔ MOD V RAPORLARINDA
   Rapor işlenmeden önce, AYNI rubriğin son iki koşusunun künye satırı yan
   yana konur: SÜRE · SEGMENT SAYISI · ORTALAMA SAHNE SÜRESİ · kart saniyesi.
     üçü de ±%5 içinde aynıysa → 🚨 PARMAK İZİ ŞÜPHESİ: rapor işlenir ama
     SÜRE VE SAHNE SAYISI HİÇBİR KAPIYA GİRDİ SAYILMAZ; operatör dosyanın
     kendi süresini OKUR ve kurgu kapısını (④) O SAYIYLA koşar.
   Sebep: iki farklı filmin iki ayrı raporu 62/63 s · 7 segment · ~10 s
   sahne · 0:58'de başlık kartı bildirdi. ⑤ aynı DOSYAYA koşulan mercekleri
   karşılaştırır; bu kapı FARKLI dosyalara koşulan aynı merceği karşılaştırır.

⑧ FRAGMAN MERCEK KAPISI [Ders 111]
   Malzeme bir FRAGMAN mı? Merceği ① KARE'dir (dikeyse `FORMAT: DİKEY`);
   ④ HİKAYE fragmana koşulmaz [FRAGMAN_KILAVUZU §0] ve fragman satırı FİLM
   tablolarına (T1-T4) girmez. Yanlış mercek koşulduysa: ham rapor korunur,
   film kaydı açılır, ⛔ SKOR SATIRI YAZILMAZ, kesme/reçete UYGULANMAZ.

⑨ HİZALAMA KAPISI [Ders 115]  ⛔ ⑤'TEN SONRA, PLAN ELDEYSE HER KOŞUDA
   Raporun sahne SAYISI hiçbir kapıya girdi sayılmaz; ızgara PLANDAN alınır:
     sahne başlangıcı(n) = hook süresi + (n-1) × klip süresi
   Replikli filmde doğrulama replik zaman koduyla yapılır:
     beklenen = sahne başlangıcı + repliğin prompt TIMELINE'ındaki ofseti
     |Δ| ≤ 2 s → sahne yerinde · |Δ| ≈ klip süresinin katı → sahne kaymış
   Sessiz filmde: raporun blokları ardışık ızgara dilimlerinin birleşimi mi?
   ⭐ Kapı master açılmadan koşar ve kimlik kapısının (③) sayısal biçimidir:
      uydurulmuş zaman kodları ızgaraya oturmaz.
   Sonuç film kaydına IZGARA GERİ ALMA tablosu olarak yazılır; raporun
   kendi sahne haritası o tabloyla değiştirilir.

⑩ ÖNERME KAPISI [Ders 87 · kapsamı Ders 116]  ⛔ HANGİ MERCEKTEN GELİRSE GELSİN
   Coğrafya · Kostüm-Prop · Zaman-Işık · Çevre · Fizik · Ses mimarisi ·
   Ekipman durumu bulguları tabloya işlenmeden ÖNCE planın logline + sahne
   haritası + sayısal kilit listesine karşı okunur:
     kaynağı planda YAZILI → bulgu DÜŞER, film kaydına "önerme" yazılır
     kaynağı yok           → bulgu ayakta

   ⭐ ÜÇÜNCÜ SATIR — PUAN GERİ VERİLİR [Ders 130]. Düşen her bulgunun
      timecode'u hücrenin Issue gözünden SİLİNİR ve hücre kaybettiği puanı
      GERİ ALIR. Issue gözü boşaldıysa hücre kaynaksızdır → `—` (D131).
   ⭐ DÖRDÜNCÜ SATIR — TOPLAM YENİDEN HESAPLANIR. Raporun OVERALL'ı artık
      GEÇERSİZDİR; film kaydına şu satır yazılır:
        | mercek | raporun toplamı | ⑩ sonrası toplam | ayakta hücre |
      T tablosuna ⑩ SONRASI sayı girer. Ayakta, kapalı, sayı taşıyan
      hücre 0 ise satır `—` girer: sıfır hücreli ortalama ölçüm değildir.
      Sebep: Iron Slope satırı "Toplam, rubriğin kendi aritmetiğidir"
      diye yazıyordu — yani ⑩ tabloyu hiç değiştirmiyordu.
   ⭐ BEŞİNCİ SATIR — SPEC'E GÖRE YENİDEN SIRALA [Ders 134], belgesiz
      mercekler (② ③ ⑤) için ZORUNLU. ⑩'dan sağ çıkan her bulgu SPEC'in
      C BLOĞU kilit listesiyle eşlenir:
        | bulgu (timecode) | raporun sırası | hangi kilit | GERÇEK sıra |
      Kilide dokunan bulgu, dokunmayanların ÜSTÜNE çıkar; raporun
      "THE THREE THAT MATTER" listesi kayda YENİDEN SIRALANMIŞ geçer.
      SPEC'te sayaç yazılıyken rapor `Counter: N/A` dediyse bu bulgu
      yokluğu değil ÖLÇÜM BOŞLUĞUDUR → kilit defterine ⬜ AÇIK.
      Sebep: "bot rengi sürüklenmesi" cila notu gibi okunur; oysa filmin
      iki figürü ayıran ÜÇ kanaldan biriydi.
   ⛔ Bulguyu getiren merceğin adı bu kararı değiştirmez. Kapı 12.08'de
      yalnız kart E'ye yazıldı; 20.08'de aynı yanlış okuma dört mercekten
      geldi ve biri filmin PLANLI FİNALİNİ kesmeyi önerdi.

⑪ ÖLÇÜM KAPISI [Ders 125]  ⛔ SIRA BAKIMINDAN EN BAŞTA KOŞAR — ④ ⑤ ⑦ ⑨
   bu kapının sayılarıyla koşar, raporun sayılarıyla değil.
   Rapor işlenmeden önce master dosya ÖLÇÜLÜR (~30 sn):
     M="<master>"
     ⛔ ⑪.0 ÖNCE KİMLİK — HANGİ FİLMİ ÖLÇTÜĞÜNÜ SOR [Ders 160]
        Dosya adı kimlik DEĞİLDİR. Aynı adı taşıyan beş dosyanın ikisi
        başka bir filmdi ve üstünde BU filmin kapak kartı duruyordu; ad
        farkı bir boşluktu. Kapak kartı ne rapor için (D105) ne dosya için
        kimlik kanıtıdır — bu vakada yanlış filmin kuyruğundaydı.
          ffmpeg -ss <süre/2> -i "$M" -frames:v 1 kimlik.jpg   → BAK
        Kurgunun ORTASI: kart/jenerik orada olamaz, gövdenin kendisidir.
        Mekân/kostüm/nesne SPEC'in C bloğuna oturmuyorsa ⛔ KOŞU DURUR.
        Aynı addan birden çok dosya varsa HEPSİ ölçülür (farklı SÜRE =
        farklı kurgu), ve hangisinin ölçüldüğü film kaydına YAZILIR.
        Ham raporun künyesinde `girdi: <tam yol> · <süre> · <çözünürlük>`
        satırı yoksa o koşu, hangi dosyaya koşulduğu BİLİNMEYEN koşudur.
     ffprobe -v error -show_entries format=duration:stream=width,height,\
       r_frame_rate "$M"                                   → süre · en-boy · fps
     ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - \
       2>&1 | grep -oE "pts_time:[0-9.]+"                   → KESME IZGARASI
     ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 \
       | grep silence_                                      → SESSİZLİK var mı
     ffprobe -v error -select_streams a -show_entries stream=codec_type \
       -of csv=p=0 "$M"                                    → SES KANALI var mı
       ⛔ çıktı BOŞSA dosyada ses kanalı YOKTUR [Ders 136]. Plan müzik ya
          da ses tasarımı yazıyorsa 🔴 TESLİM KUSURU: parti DURUR, master
          yeniden ihraç edilir, DÖRT mercek yeniden koşulur — görüntü
          mercekleri de master'ı ölçmemiştir. Plan tamamen sessizse yine
          kayda geçer: ③ satırı `— · ses kanalı yok (doğrulandı)` olur.
          Sebep: `LINES HEARD: none` iki ayrı gerçeği aynı kelimeyle
          yazıyor ve dört mercekten üçü duraksamadan geçti.
     ffmpeg -i "$M" -af "aresample=8000,asetnsamples=8000,astats=metadata=1:\
       reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" \
       -f null -                                            → saniyelik RMS
       ⛔ VE TERSİ [Ders 137]: çıktı DOLU olduğu hâlde raporlar "ses yok"
          diyorsa yanılan RAPORLARDIR. Bir filmde AAC 253 kbit/s'lik,
          −17,3 LUFS'luk, hiçbir yerinde sessizlik aralığı olmayan bir
          yatağı ALTI MERCEĞİN ALTISI "no audio information at all" diye
          yazdı ve ③ bunun üstüne STOP bloğu bastı. Ses kanalının varlığı
          bir DOSYA özelliğidir; hiçbir mercek onu gözlemleyemez, ve
          gözlemleyemediği bir şeyi daha dikkatli gözlemlemesini istemek
          yamalanmış bir hata değil, aynı hatanın kibar hâlidir. Ölçüm
          satırı rubriğin künyesine YAPIŞTIRILIR; yapıştırılmadıysa ses
          ekseni o koşuda ÖLÇÜLMEMİŞTİR.
     ffmpeg -i "$M" -vf "crop=360:240:iw-360:ih-240,fps=1/30,tile=6x2" \
       -frames:v 1 kose_SA.png                              → KÖŞE TESTİ (filigran)
     ffmpeg -i "$M" -vf "freezedetect=n=-60dB:d=1.5" -an -f null - 2>&1 \
       | grep -oE "freeze_(start|end): [0-9.]+"           → KUYRUK/BAŞ KART ŞÜPHESİ
       + son_kare.jpg (son 1 s)                            [D70/D72 · 9 vaka · 01.09.2026]
     ⭐ Hepsi tek koşuda: bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>
       ⛔ Aynı köşede aynı şekil her örnekte duruyorsa FİLİGRAN VAR [Ders 150]:
          🔴 teslim kusuru — master filigransız yeniden ihraç edilir, koşu ona
          yapılır; dört köşe için crop x/y değiştirilir. Altı mercek 315
          saniyelik bir filigranı görmedi: rubrik değişim arar, filigran değişmez.
     ffmpeg -i "$M" -af ebur128=peak=true -f null -          → LUFS + true peak
       (ihraç kilidi −14 LUFS · −1,0 dBTP — KURGU_RITMI §6; −17 LUFS / 0 dBTP
        bir TESLİM kusurudur, rapor bulgusu değil)
     ⚠️ KARANLIK FİLMDE scene>0.3 KESME GÖRMEZ (Skylight: 33 kesmenin 1'i). İkame:
        silencedetect deliklerinin ve kart başının saniyeleri ızgara katına
        oturuyorsa ızgara ODUR; sabit GOP'lu dosyada I-frame'ler işe yaramaz.
   · Rapor ile ölçüm çelişirse ÖLÇÜM kazanır; o merceğin satırı ŞARTLI olur.
   · AMBİYANS DELİĞİ / DİJİTAL SESSİZLİK bulgusu ölçülmeden tabloya GİRMEZ.
   · Ölçülen sayılar film kaydına "§ÖLÇÜM KAPISI" tablosu olarak yazılır.
   Sebep: altı mercek AYNI yanlış kesme listesini verdi (⑤ kapısı "uyuşma"
   gördü ve ✅ verdi), biri de dosyada hiç olmayan bir sessizlikten
   🔴 BLOCKER üretti. Yanıtı bir komut satırında duran soru modele sorulmaz.
```

---

## 🔧 C — ① KARE RAPORU GELDİ

**Rubrik:** `QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md` · girdi: video (+ SPEC)

```
⛔ FORMAT KAPISI (22.08.2026): raporun ilk satırında `FORMAT:` var mı?
   YATAY → kategori 12-14 (9:16 · güvenli alan · kanca) N/A olmalı
   DİKEY → o üçü PUANLI olmalı; boşsa koşu eksiktir, tabloya girmez
   Rubrik aspect'i dosyadan ölçer. Rapor formatı başlıktan aldığını
   söylüyorsa ölçüm yapılmamıştır.
```

```
⛔ ÖNCE KAPI: raporun ilk satırındaki INPUT MODE nedir?
   MOD D → SPEC prompt dosyasından kopyalandı, uygunluk ölçüldü.
   MOD V → SPEC yok; film kendisiyle + fizikle ölçüldü. Geçerli bir
           çalıştırmadır. Skor satırı `Ⓥ` ile işaretlenir, FLAGS FOR
           DOCUMENT CHECK soruları plan dosyasından cevaplanır (adım 2'de).
   Rapor "INPUT MISSING" diyorsa rubrik güncel değildir ya da modele eski
   sürüm verilmiştir — 05.08.2026'dan beri geçersiz bir çıktıdır.

1. HAM RAPORU KAYDET       02_HAM_RAPORLAR/<FILM>_KARE_HAM.md
                           model çıktısı olduğu gibi, düzenlemeden

2. FİLM KAYDINI YAZ/GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md
                           yoksa oluştur · üst blokta dört merceğin durumu,
                           künye, kategori skor tablosu, bulgular
                           (şablon: 01_FILM_RAPORLARI/THE_INVERSION.md)

3. SKOR SATIRINI EKLE      LESSONS_LEARNED.md · teknik kalite tablosu
                           ⚠️ teknik skor BURAYA gider, 03/04 tablolarına DEĞİL
   | Film | Sahne | Karakter | Fizik | Kamera | Işık | Çevre | Canlı | Hareket | Toplam |

4. SAYACI GÜNCELLE         00_INDEX.md · §SAYIM + tamlık matrisi (🔧 sütunu)

5b. ⭐ PROMPT REÇETESİNİ GREP'LE  [Ders 85]
    Raporun her REMOVE / REPLACE önerisi uygulanmadan önce:
       grep -rn "<önerideki tam dize>" <FILM klasörü>/
    çıktı BOŞ                → reçete DÜŞER (rapor promptu görmedi, uydurdu)
    çıktı YASAĞIN İÇİNDE     → reçete DÜŞER (çalışan yasağı silme önerisi)
    ⚠️ Third Dune'da "REMOVE 'title card, cinematic poster'" önerisi filmin
       metin yasağını silecekti; dize depoda yalnız yasağın içinde vardı.
    ADD önerileri bu kapıdan muaf.

5. YENİ DERS VAR MI?       → görev kartı G

6. commit
```

---

## 📖 D — ④ HİKAYE RAPORU GELDİ

**Rubrik:** `QA_PROMPTLARI/4_HIKAYE_QA_CRITIQUE_PROMPT.md` · girdi: video (+ PLAN)

```
⛔ İKİ MOD VAR (05.08.2026'dan beri):
   MOD D — plan dosyası verildi. Sahne sayısı · süre · diyalog sayısı plana
           karşı doğrulanır; tutmazsa skor GEÇERSİZ ve tabloya ~~üstü
           çizili~~ girer (örnek: Low Power satırı). Zirve kontrolü yapılır.
   MOD V — plan yok. Film ekranda göründüğü hâliyle puanlanır; on kategori
           de yazılır, zirve kontrolü SORUYA döner. Satır `Ⓥ` + ⚠️ ŞARTLI.
   Eski "plan olmadan çalıştırılmaz" kuralı kaldırıldı: hiç çalışmayan bir
   senaryo denetimi kimseyi korumuyordu (üç Dawn Front çalıştırması boşa
   gitti).

1. 02_HAM_RAPORLAR/<FILM>_HIKAYE_HAM.md       ham çıktı
2. 01_FILM_RAPORLARI/<FILM>.md                📖 HİKAYE QA bölümü
   ⭐ mod V ise: FLAGS FOR DOCUMENT CHECK sorularını plan dosyasından
      CEVAPLA ve cevapları buraya yaz (kart E adım 2 ile aynı iş)
3. FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md      skor satırı — T1'E DEĞİL
   | Film | Format | Kanca | Önerme | Yapı | Karakter | Tema | Diyalog | Duygu Yayı | Final | Özgünlük | Tutundurma | Toplam |
   geçerlilik işareti:  ✅ geçerli · ⚠️ ŞARTLI · 🚨 GEÇERSİZ
   mod V satırı:  film adının yanına `Ⓥ` + ⚠️ ŞARTLI
4. 00_INDEX.md                                📖 sütunu + sayım
5. Yeni ders → kart G
6. commit
```

---

## 🔗 E — ② DEVAMLILIK RAPORU GELDİ
*(22.08.2026'da eski E + E2 kartları birleşti — rubrikler birleştiği için.
Karakter artık opsiyonel derin mercek DEĞİL, bu merceğin gövde yarısıdır.)*

**Rubrik:** `QA_PROMPTLARI/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video**

```
⛔ TERSİ KURAL: Bu rubriğe DOKÜMAN VERİLMEZ. Baseline STEP 1'de videodan
   kurulan sahne envanteri + karakter pasaportudur. "Eksik sahne" ve
   "eksik karakter" raporlaması bu rubrikte yasaktır.

⛔ İKİ YARI KAPISI: rapor 13 kategoriyi de taşıyor mu?
   GÖVDE 1-6   kimlik · kostüm · yıpranma · ekipman · çapraz kesme · fizik
   DÜNYA 7-13  sayaç · coğrafya · zaman-ışık · dünya propu · nedensellik
               · nicelik+sayı · kurulum
   Gövde yarısı boşsa koşu YARIMDIR — eski MANTIK_QA'nın ölçtüğü kadarını
   ölçmüştür ve tabloya tam satır olarak girmez.

⛔ ⚠️ PARTIAL KAPISI: kanıtı 3 sahneden az ya da sürenin %25'inden azı
   olan kategori numarasız kalır ve ortalamaya girmez. Numaralı bir
   ⚠️ PARTIAL hücresi aritmetik hatasıdır.

1. 02_HAM_RAPORLAR/<FILM>_DEVAMLILIK_HAM.md   ham çıktı
2. ⭐ FLAGS FOR DOCUMENT CHECK sorularını plan dosyasından CEVAPLA
      → rubriğin ikinci yarısı budur; en değerli bulgular buradan çıktı
      → cevapları 01_FILM_RAPORLARI/<FILM>.md içine yaz
2b. ⭐ "BU DEĞİŞİM FİLMİN ÖNERMESİ Mİ?"  [Ders 87 · artık ORTAK ADIM ⑩]
      Coğrafya · Kostüm-Prop · Zaman-Işık bulgusu TABLOYA İŞLENMEDEN önce
      planın logline + orta nokta + sayaç kanalları okunur.
      evet → bulgu DÜŞER, film kaydına "önerme" yazılır, satır ŞARTLI
      hayır → bulgu ayakta
      ⚠️ Third Dune: üç MAJOR'ın ikisi buradan düştü (araç gömülmesi =
         filmin orta noktası · kalkış çanağı = planlı S22)
2c. ⭐ KİMLİK / SAYAÇ KAPISI — diğer bütün skorları ezen iki bulgu
      Rapor IDENTITY BREAK (başka yüz ya da ekranda kopya karakter) veya
      sayaç tersinmesi bildiriyorsa, ortalama ne olursa olsun verdict'in
      ilk satırı odur ve film kaydına ÖNCE o yazılır.

3. FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md   skor satırı
   | Film | Kimlik | Kostüm | Yıpranma | Ekipman | Çapraz Kesme | Fizik |
     Sayaç | Coğrafya | Zaman-Işık | Dünya Propu | Nedensellik |
     Nicelik+Sayı | Kurulum | Toplam |
4. 00_INDEX.md                                ② sütunu + sayım
5. Yeni ders → kart G
6. commit
```

---

## 🧍 E2 — KALDIRILDI (22.08.2026)

> Karakter merceği ② DEVAMLILIK'in **gövde yarısı** oldu; ayrı kartı yok.
> Karakter raporu geldiğinde **kart E**'ye bak. Eski kartın tek kuralı
> oraya taşındı: kesişen kostüm-prop bulguları artık kural değil YAPI
> gereği tekildir — gövde 1-6, dünya 7-13.

---

## 🔊 E3 — ③ SES RAPORU GELDİ

**Rubrik:** `QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video**
*(22.08.2026: artık OPSİYONEL DEĞİL — kurguda ses varsa zorunlu dört
mercekten biri. Eski karakter merceğinin ses/performans yarısı da buraya
geldi: ses bu merceğin, beden ②'nin.)*

```
⛔ TERSİ KURAL: Bu rubriğe DOKÜMAN VERİLMEZ. Baseline STEP 1'de kurgudan
   kurulan ses defteridir. "Eksik replik" raporlaması yasaktır.

⛔ İKİ KAPI, ikisi de koşudan ÖNCE operatörün işi:
   ① MALZEME: tek klip değil, TAM KURGU verilir. Bu rubriğin ölçtüğü şeyin
      çoğu kesmelerin ARASINDA yaşar — tek klip koşusu tabloya girmez
      (DERS 75'in bu mercekteki karşılığı).
   ② SES: raporun header'ında AUDIO STATE var mı?
      A dolu · B sessiz ama ses tasarımlı · C tamamen sessiz → koşu YOK
      · D ses kesintili. Rapor `AUDIO ABSENT — RUN NOT STARTED` döndüyse
      skor yazılmaz; master'ın ses kanalı kontrol edilip yeniden ihraç edilir.

1. 02_HAM_RAPORLAR/<FILM>_SES_HAM.md          ham çıktı

2. ⭐ REGISTER DOĞRULAMASI — bu kartın en kritik adımı
      Raporun dialogue ledger'ındaki HUMAN / MACHINE / UNCLEAR işaretleri
      plan dosyasıyla karşılaştırılır. Seri diegetik yapay ses kullanıyor
      (Blind Return 8/8 suit AI · Cold Burn 12/12 telsiz-AI).
      → MACHINE olması gereken bir repliğe "sentetik duruyor" bulgusu
        yazıldıysa BULGU DÜŞER, tabloya işlenmez.
      → UNCLEAR replikler plandan cevaplanır, cevap film kaydına yazılır.
      ⚠️ Bu adım atlanırsa rubrik çalışan tasarımı bozmaya yönlendirir.

3. ⭐ FLAGS FOR DOCUMENT CHECK sorularını plan/senaryo dosyasından CEVAPLA
      → cevapları 01_FILM_RAPORLARI/<FILM>.md · 🔊 SES QA bölümüne yaz

4. FILM_QA_RAPORLARI/T3_SES_KALITE.md          skor satırı
   | Film | Ses Durumu | Atıf | Sentetik | Ses Kimliği | Aktarım |
     Sıra Alma | Ambiyans | SFX Senk | Miks | Müzik | Toplam |

5. 00_INDEX.md · ③ sütunu + sayım — ③ artık matrisin /4 paydasının
   TAM ÜYESİDİR (22.08'e kadar opsiyonel derin mercekti ve bu yüzden
   34 film kaydının yalnız 5'inde ses raporu vardı)

6. ⚠️ KESİŞİM BİRLEŞTİRME — aynı filme koşulan diğer mercekler:
      ① KARE 8. kategorisi (Diyalog ve Ses) → tek klip ölçüldüyse yerinde
        kalır; AYNI KURGU ölçüldüyse ses bulguları ③'e devredilir
      ② DEVAMLILIK ile kesişim YOK — ses bu merceğin, beden ②'nin;
        ayrım rubriklerin kapsam bloğunda yapısaldır
      OUT-OF-SCOPE FLAGS satırları ilgili merceğin kaydına taşınır
      (dudak-fonem · vakumda ses · altyazı → ① KARE)

7. ⭐ "FIXABLE IN THE MIX vs REQUIRES REGENERATION" tablosunu 00_INDEX
   YAPILACAKLAR listesine iki ayrı blok olarak geçir — bu merceğin
   diğerlerinden farkı, bulgularının çoğunun YENİDEN ÜRETİM GEREKTİRMEMESİ

8. Yeni ders → kart G
9. commit
```

---

## 🖼️ F — ⑤ ARKA PLAN RAPORU GELDİ (derin tarama)

**Rubrik:** `QA_PROMPTLARI/5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video (tam kurgu)**
*(24.08.2026'da açıldı — DERİN TARAMA sınıfı: /4 paydasına girmez,
risk tetikli koşulur. Ne zaman koşulacağı QA_PROMPTLARI/00_README.md
derin tarama bölümünde.)*

```
⛔ TERSİ KURAL: Bu rubriğe DOKÜMAN VERİLMEZ. Baseline STEP 1'de videodan
   kurulan ARKA PLAN ENVANTERİDİR (özne her sahnede yalnız DIŞLAMAK için
   adlandırılır). "Eksik set/kalabalık" raporlaması yasaktır.

⛔ ÖZNE KAPISI: raporun SUBJECTS EXCLUDED satırı dolu mu? Rapor özneyi
   (yüzü, kostümü, hareketi) puanladıysa koşu merceğin varlık sebebini
   ıskalamıştır — o bulgular DÜŞER, ilgili merceğe işaretçi yazılır.

1. ORTAK ADIMLAR ①-⑩ koşulur (kimlik kapısı, kurgu kapısı, önerme
   kapısı... — hepsi bu merceğe de uygulanır)
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>_ARKA_PLAN_HAM.md
3. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🖼️ ARKA PLAN bölümü
   ⭐ BULGU SAHİPLİĞİ (D108 derin-tarama eki): çekirdek mercek her zaman
      sahiptir. Bulgu bir çekirdek kapsamına da oturuyorsa (örn. orta
      planda eriyen figür → ① KARE) film kaydına O merceğin bölümüne
      yazılır, "⑤ taraması buldu" notuyla; yalnız ⑤'e özgü bulgu
      (ufuk kayması, kalabalık sayısı, kadraj kenarı) ⑤ bölümünde kalır.
      Çekirdek mercek aynı olayı zaten görmüşse: TEK satır, iki kaynak —
      çifte fatura değil çapraz doğrulama.
4. SKOR SATIRI            T5_ARKA_PLAN_KALITE.md
   | Film | Tarih | Figür Büt. | Figür Dav. | Kalabalık | Ufuk | Derinlik |
     Arka Set | Odak | Gökyüzü | Kenarlar | Toplam | Verdict |
   ⛔ 00_INDEX tamlık matrisine İŞLENMEZ — payda /4 kalır. 00_INDEX'e
      yalnız film kaydındaki koşu notu düşülür.
5. FLAGS'i plan dosyasından CEVAPLA → film kaydına yaz
6. Yeni ders → kart G
7. commit
```

---

## ⚖️ F2 — ⑥ FİZİK RAPORU GELDİ (derin tarama)

**Rubrik:** `QA_PROMPTLARI/6_FIZIK_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
(+ planın SAYISAL KİLİTLERİ = **MOD D**, bu merceğin varlık sebebi)
*(24.08.2026'da açıldı — DERİN TARAMA sınıfı: /4 paydasına girmez.)*

```
⛔ MOD KAPISI: plan sayısal kilit taşıyorsa (bu depoda neredeyse her plan
   taşır) koşu MOD D olmalıdır — kilitler rubriğin NUMERIC LOCK LIST'ine
   kopyalanır. Kilitli filme mod V koşmak D94'ün bu mercekteki karşılığıdır:
   satır Ⓥ ⚠️ ŞARTLI girer.

⛔ ÖNERME KAPISI BU RUBRİKTE YAPISALDIR (STEP 0 PREMISE GATE): raporun
   PREMISE REGISTER'ı planın novum satırıyla karşılaştırılır.
   · Register filmin novum'unu içeriyor + imkânsızlığı puanlamamış → doğru koşu
   · Register boş ama film novum'lu → rapor önermeyi bulgu yazmış olabilir;
     ortak adım ⑩ her fizik bulgusuna TEK TEK uygulanır
   · Register'da olup planda OLMAYAN madde → model kural uydurmuş; o
     maddenin muaf tuttuğu bulgular geri açılır

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>_FIZIK_HAM.md
3. ⭐ KİLİT TABLOSUNU İŞLE — mod D'nin hasadı
   NUMERIC LOCK VERIFICATION satırları film kaydına aynen geçer:
   · FAIL satırı = planla ekran arasında ölçülmüş sapma → üretim/kurgu
     kararı ister (yeniden üretim REÇETESİ değil; karar operatörün)
   · UNMEASURABLE / NOT EXERCISED satırı skoru ETKİLEMEZ
   · ⚠️ FAIL'in ölçüm cetveli (ruler) raporda yazılı mı? Cetvelsiz FAIL
     düşer — rubriğin kendi kuralı ("a conviction is never finer than
     its ruler"), operatör tarafında da uygulanır.
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · ⚖️ FİZİK bölümü
   ⭐ BULGU SAHİPLİĞİ: ① "desen" sahibi (toz sıvı gibi akıyor), ② 
      "karşılaştırma" sahibi (orada hızlı burada yavaş), ⑥ yalnız SAYI
      taşıyan bulgunun sahibi. Çekirdeğe oturan bulgu o merceğin bölümüne
      "⑥ taraması buldu" notuyla yazılır; GRAVITY TABLE ve RATE TABLE
      her durumda ⑥ bölümünde kalır.
5. SKOR SATIRI            T6_FIZIK_KALITE.md
   | Film | Tarih | Mod | Yerçekimi | Balistik | Momentum | Malzeme |
     Parçacık | Ölçek | Hız/Zaman | Işık/Gölge | Biyomek. | Toplam |
     Kilit Sonucu | Verdict |
   Kilit Sonucu sütunu (yalnız mod D): "12 kilit: 9 PASS · 2 FAIL ·
   1 NOT EXERCISED" biçiminde.
   ⛔ 00_INDEX tamlık matrisine İŞLENMEZ — payda /4 kalır.
6. FLAGS'i plan dosyasından CEVAPLA → film kaydına yaz
7. Yeni ders → kart G
8. commit
```

---

## 🎯 F3 — ⑦ AKSİYON RAPORU GELDİ (risk tetikli tarama)

**Rubrik:** `QA_PROMPTLARI/7_AKSIYON_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
(+ SPEC A ve C blokları = **MOD D**)
*(01.09.2026'da açıldı — /4 paydasına girmez.)*

```
⛔ SIRA KAPISI: rapor ANLATIM CÜMLESİNİ ekrandan mı yazmış, plandan mı?
   Mod D'de plan önce okunursa model "söylenen"i görür ve sahte PASS üretir.
   Rapor cümleleri SPEC'in diliyle birebir örtüşüyorsa koşu ŞÜPHELİDİR —
   bir beat seç, kareyi çıkar, cümleyi kendin yaz ve karşılaştır.

⛔ ELİZYON KAPISI: BEAT LEDGER'da `readable? N` olup sebebi "cut" olan her
   satır kesme listesiyle karşılaştırılır. Beat'in kendisi üretilmediyse
   bu KURGUDA DÜZELMEZ — "fixable in the edit" diyen satır düşer.

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>_AKSIYON_HAM.md
3. BEAT STRING DOĞRULA    uzunluk = kesme + 1; BEATS READABLE toplamı =
   BEATS COUNTED. İkisini de rapor_kontrol.py basar — elle sayma.
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🎯 AKSİYON bölümü
   ⭐ BULGU SAHİPLİĞİ: ① tek kareden okunan artefaktın sahibi · ②
      "aynı mı" karşılaştırmasının · ⑥ SAYININ · ⑦ yalnız OKUNABİLİRLİĞİN.
      Çekirdeğe oturan bulgu o merceğin bölümüne "⑦ taraması buldu" notuyla.
5. SKOR SATIRI            FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md
6. Beat hiç üretilmemişse bu bir ÜRETİM notudur — depo kurgu/birleştirme
   ÜSTLENMEZ, bulguyu yazar ve üretim hattına bırakır.
```

## 💪 F4 — ⑧ EFOR RAPORU GELDİ (risk tetikli tarama)

**Rubrik:** `QA_PROMPTLARI/8_EFOR_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
(+ SPEC A ve C blokları = **MOD D**)
*(01.09.2026'da açıldı — /4 paydasına girmez.)*

```
⛔ YERÇEKİMİ MAZERETİ KAPISI: rapor bir eforu "düşük yerçekimi, kolay"
   diye muaf tuttuysa o muafiyet DÜŞER. Ağırlık azalır; kütle ve atalet
   azalmaz. Muafiyetin kaldırdığı bulgular geri açılır.

⛔ EĞRİ KAPISI: COST CURVE'deki her DÜŞÜŞ RESET LOG'da bir satır ister.
   Gerekçesiz düşüş pattern ③ (taze sıfırlama) ya da ⑪ (hak edilmemiş ikinci
   rüzgâr) demektir ve bulgudur — rapor_kontrol.py sayar.

⛔ TERS HATA: pattern ⑭ (sebepsiz yorgunluk) ödenmeyen fatura kadar
   ağırdır. Bu merceği "daha çok acı = daha iyi puan" diye okuyan rapor
   yanlış koşmuştur.

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>_EFOR_HAM.md
3. ⑥ İLE ÇAPRAZ OKU       ⑥ FİZİK aynı filme koşulduysa: ⑥'nın
   biyomekanik kategorisi ile ⑧'in 1/4/6 kategorileri yan yana yazılır.
   ⑥ PASS + ⑧ FAIL normaldir ve merceğin varlık sebebidir
   ("sayısal olarak mümkün, ama beden ödemedi") — çelişki DEĞİLDİR.
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 💪 EFOR bölümü
5. SKOR SATIRI            FILM_QA_RAPORLARI/T8_EFOR_KALITE.md
```

## 📚 G — YENİ DERS ÇIKTI

```
0. ⛔ KAPI SATIRI OLMAYAN DERS YAZILMAZ  [01.09.2026 · DERSLER/00_DERS_YAZIM_KONTRATI.md]
   Dört kader: BETİK · LİSTE · KARAR · ARŞİV — "prompt cümlesi" kader değildir.
   Kapısı bulunmayan aday → DERSLER/GOZLEM_DEFTERI.md (ADAY-n), numara ALMAZ.
   Başlığın altına iki satır: **KAPI:** … · **TEKRAR:** 0
   Vaka ≥ 3 → ⛔ ÇALIŞMIYOR + dönüştürme borcu (cümleden karara/araca).
   Alet dersi (08/09) yeni-film'in okuma listesine GİRMEZ. Sayı: sayac.sh 🧭.

1. Dersi İKİ yere işle (07.08.2026'dan beri dersler klasörde):
   a) DERSLER/ içindeki uygun TEMATİK dosyanın sonuna ekle
      (kamera/karakter/fizik/ışık/ekipman/metin/kurgu/QA/sistem —
      hangisi olduğuna LESSONS_LEARNED.md'deki dosya tablosundan karar ver)
      ## 🔴/🟡 DERS <n>: BAŞLIK
      **Kaynak:** hangi film, hangi skor
      **Sorun:** kaç filmde tekrarladı
      **KAPI:** … · **TEKRAR:** 0          ← kontrat, 01.09.2026
      **ÇÖZÜM:** karar / araç / liste maddesi (prompt cümlesi yalnız betik ölçüyorsa)
   b) LESSONS_LEARNED.md · DERS DİZİNİ tablosuna satır ekle
      numara dizindeki EN YÜKSEK numaradan devam eder — tematik dosyanın
      içindeki son numaraya BAKMA, numaralar dosyalara dağınık

2. ⭐ TARİF DEĞİL SAYI YAZ
   Kanıtlanmış tek mekanizma sayısal kilit. "Toz yavaş çöksün" değil,
   "toz 3 saniyede yüzeye oturur" yaz. Tarif kilitleri ölçülebilir
   şekilde işe yaramadı — URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md

3. Ders tür/ortama özelse → KILAVUZ_REHBERI §3 veya §4 ilgili kartına
   "İlgili ders" satırına numarayı ekle
4. Tür-bağımsızsa ve her prompta girecekse → §5 NEGATİF ÇEKİRDEK
   ⚠️ Çekirdek 9 film dosyasına kopyalanmış durumda. Değiştirirsen:
      grep -rl "no camera teleportation" --include="*.md" .
5. ⭐ ÖNCE KAYNAK RUBRİĞİ YAMALA [Ders 63]
   Dersin **Kaynak** satırındaki çalıştırma hangi rubrikten çıktıysa yama
   ÖNCE oraya yazılır. Kaynak rubrik yamalanmadan diğerlerine geçilmez.
   ⛔ YAMA SADECE KURALDIR (17.08.2026 salt-prompt temizliği):
      İngilizce · gövdeye · emir kipinde · numara/tarih/film adı YOK.
      Rubriğe girmesi yasak: "[DERS n]" · "12.08.2026'da X filmi..." ·
      "../LESSONS_LEARNED.md" · Türkçe açıklama.
      Sebep: rubrik operatörün videoyla birlikte yapıştırdığı TEK dosya;
      göremediği bir derse atıf, modelin uyduracağı bir boşluktur.
   ⛔ 5c KARDEŞ RUBRİK TARAMASI [Ders 111] — kaynak rubrik yamandıktan sonra
      dersin tarif ettiği hatayı ÜRETEBİLECEK her rubrik açılır. Ölçüt tek
      soru: "bu rubrik aynı malzemeyi görse aynı hatayı yapar mıydı?"
        evet  → yamanır, iz defterine satır girer
        hayır → iz defterine "D<n> → <rubrik> · GEREKMEZ · <sebep>" yazılır
      Tarama yapılmadan kart kapanmaz. D63 SIRA'yı söyler, KAPSAM'ı değil:
      D106 tek rubriğe işlendi ve aynı gün ikinci rubrikte tekrarladı.
   ⭐ Numara, tarih, film ve çalıştırma kaydı ŞURAYA yazılır:
      QA_PROMPTLARI/CALISTIRMA_KAYITLARI.md
        · ilgili rubriğin bölümü → "N kez çalıştırıldı · son <tarih> · sonuç"
        · §DERS → RUBRİK İZ DEFTERİ → "D<n> → <rubrik> · <bölüm adı>"
      ⛔ Ders hangi rubriklere işlendiyse iz defterine O SATIR yazılmadan
         kart kapanmaz — rubrikte artık aranacak etiket yok, tek iz burası.
   ⚠️ 03.08'de Ders 60/61/62 yazıldı ve DÖRT rubrik düzeltildi; 60 ile 62'yi
      ÜRETEN SHORTS_QA atlandı, iki gün sonra aynı hatayı üretti.
6. QA promptunun ders sayısı referansını güncelle
7. bash sayac.sh → boşluk uyarısı var mı
   ⚠️ Betik benzersiz numarayı en büyük numarayla karşılaştırır; ÇİFT
      yazılmış numarayı göremez (çift numara boşluk yaratmaz).
      Ayrıca kontrol et:
      cat kilavuzlar_ve_sistem_dosyalari/DERSLER/*.md \
        | grep -oE "^## .{0,4} DERS [0-9]+" \
        | grep -oE "[0-9]+" | sort -n | uniq -d
      → çıktı SADECE "60 61 62" olmalı (tarihsel çift numaralar, dizinde
        a/b olarak kayıtlı) — başka numara çıkarsa yeni çift açılmış demektir
8. commit
```

---

## 🧱 H — YENİ FORMAT / TÜR / ORTAM EKLENDİ

```
 □ KILAVUZ_REHBERI.md → §2 (format) / §3 (ortam) / §4 (tür) kartı
      yeni tür için §4.4 boş şablonundan başla
 □ YAPI_GRAFI.md → karar ağacına dal + klasör ağacına satır
 □ Yeni klasör açıldıysa → sayac.sh içindeki klasör listesine ekle
 □ commit
```

## 🧱 H2 — FORMAT / TÜR / KLASÖR KALDIRILDI (H'nin tersi)

> Sistem büyümeye hazırdı, küçülmeye değil — 12.08.2026'da zombi/savaş
> klasörleri silindi ve dört harita günlerce silinen klasörü göstermeye
> devam etti. Bir klasör silinince AYNI dört nokta güncellenir:

```
 □ AGENTS.md §1 haritasından satırı sil
 □ YAPI_GRAFI.md → karar ağacındaki dal + klasör ağacındaki satır
 □ sayac.sh içindeki klasör listesinden çıkar
 □ FILM_QA_RAPORLARI/00_INDEX.md → o klasörün bölümü/satırları kaldırılır
 □ KILAVUZ_REHBERI.md → tür/format kartı SİLİNMEZ, başına ⏸️ RAFTA yazılır
      (kılavuz bilgisi ucuz, yeniden yazmak pahalı)
 □ bash sayac.sh → toplam, 00_INDEX ile tutuyor mu
 □ commit (tip: bakim)
```

> ⭐ **GERİ AÇILIŞ EMSALİ (23.08.2026):** `yatay_2_4_dk_filmler_zombi/`
> H2 ile silinmiş bir klasördü ve H ile geri açıldı. Geri açarken aynı
> dört nokta TERS yönde güncellenir + bir beşincisi eklenir: kılavuzun
> ⏸️ RAFTA satırı kaldırılır ve yerine **açılış şartı** yazılır. Bu
> depoda o şart bir bütçedir (KILAVUZ_REHBERI §4.2'nin altı satırı) —
> klasörü geri açmak, türü bedava geri getirmez.
>
> ⭐ **ÜÇÜNCÜ TUR — TÜR KAPANIŞI (26.08.2026):** aynı klasör ikinci kez H2
> ile kaldırıldı, bu kez klasör değil TÜRÜN KENDİSİ kapandı: depo yalnız
> UZAY filmleri içindir. Bu turda iki şey öğrenildi ve ikisi de kartın
> eksiğiydi:
>
> ```
> ① TÜR KLASÖRE EŞİT DEĞİL. Zombi filmlerinin yarısı zombi klasöründe
>    DEĞİLDİ — ikisi dikey_shorts_filmler/ içinde duruyordu ("Tür: Zombi /
>    kaçış aksiyonu"). Klasörü silmek türü kapatmaz.
>    ⛔ H2 koşulmadan ÖNCE: grep -rli "<tür>" ile TÜM format klasörlerini
>       tara; tür kartının referans film listesi (KILAVUZ_REHBERI §8)
>       ikinci kaynaktır.
> ② SİLMEDEN ÖNCE git ls-files. Kaldırılan dört filmin ÜÇÜ hiçbir
>    commit'te yoktu (yalnız çalışma ağacındaydı) — "nasılsa git'te durur"
>    varsayımı yanlıştı ve silme geri alınamaz olurdu. Depo dışına arşiv
>    alındı: film_md_ZOMBI_ARSIV_2026-08-26.tar.gz
> ③ ÖLÇÜM VERİSİ FİLMLE BİRLİKTE SİLİNMEZ. THE LAST SPAN'ın 7 ham raporu
>    ve film kaydı DURUYOR (kural ④). Kayıt ⏸️ başlığıyla METODOLOJİ
>    kaydına çevrildi: skor üretmez, tabloya girmez, kıyas tabanı olmaz.
>    Filme özel rubriğin türden bağımsız yarısı da şablona damıtıldı:
>    QA_PROMPTLARI/FILME_OZEL/00_YANLIS_POZITIF_DUVARI_SABLONU.md
> ```

---

## 🌐 I — WEB PANELİ (KALDIRILDI)

> Panel (`web/`) 21.08.2026'da depodan kaldırıldı — kart H2 bu tarihte
> uygulandı ve dört haritadan panel satırları silindi. Panel geri
> gelirse git geçmişindeki bu kartın eski hâli temel alınır
> (`git log --all -- web/`). O güne dek "panele dokundum" diye bir
> görev yok.

---

# 4. YAZIM STANDARDI

```
DOSYA ADI      BUYUK_HARF_ALT_CIZGI.md · Türkçe karakter yok · ASCII
FİLM BAŞLIĞI   # <emoji> FILM ADI — Türkçe Alt Başlık
SAHNE BAŞLIĞI  ## 🎬 SAHNE <n> — BAŞLIK          ← ## şart (kural ②)
PROMPT         ``` kod bloğu içinde · blok dışına Türkçe açıklama yazma
BIBLE          ## <emoji> WORLD/CHARACTER/SHIP/CAMERA BIBLE — <ad>
TARİH          GG.AA.YYYY (02.08.2026)
```

**Bir sayfayı iki iş yapmaya zorlama.** Rubrik `QA_PROMPTLARI/`'da, sonuç
`FILM_QA_RAPORLARI/`'da, ders `LESSONS_LEARNED.md`'de durur.

---

# 5. COMMIT KURALI

> ⛔ **COMMIT'İ SADECE PROJE SAHİBİ ATAR.** Ajan `git commit` / `git push`
> ÇALIŞTIRMAZ (`.claude/settings.json` deny kuralıyla da engellidir).
> Görev kartlarındaki "commit" adımı = "iş commit'e HAZIR bırakılır" demektir;
> aşağıdaki format, sahibin atacağı commit mesajı içindir.

```
<tip>: <ne değişti>

tipler:  film    yeni/güncellenen film dokümanı
         qa      QA raporu, skor tablosu, film kaydı
         ders    LESSONS_LEARNED
         kilavuz kılavuz/sistem dosyası
         panel   web/
         bakim   temizlik, düzeltme, yapı
```

- QA raporu ve skor satırını **aynı** commit'e koy — ayrılırsa tablo yalan söyler.
- İş bitmeden commit atma; yarım bırakılan güncelleme, hiç yapılmamıştan kötüdür.

---

# 6. BİLİNEN AÇIKLAR — bunlara güvenme

> 02.08.2026 denetiminde bulundu, **25.08.2026 denetiminde güncellendi.**
> Düzeltilene kadar ajanın bilmesi gerekir. Çözülen açık silinmez, ✅ ile
> kapatılır — nasıl çözüldüğü de bir kayıttır.

```
🔴 AÇIK ÇALIŞMA LİSTESİ (01.09.2026): TODO_DERS_KILAVUZ_QA_KAPILARI.md — ders/kılavuz/QA
   kapıları, 8 faz, tarihli ölçüm tablosu. Faz 1 master bekliyor (mod D = 0),
   Faz 2-7 ajanın işi. Bu satır o dosya silinince silinir.

🔴 4 dosya başlık standardı dışında (V1 düz metin — kural ② ihlali):
   THE_BREATHING_STORM · THE_DEEP_PRESSURE · THE_ETERNAL_ENGINE · THE_PULSE
   (panel varken bu dosyalar parser'dan düşüyordu; panel 21.08.2026'da
   kaldırıldı ama başlıksızlık hâlâ tarama/sayaç hatası üretir)
   Ayrıca: THE_DEEP_ROOT puanı var ama 13 sahnenin 0'ı yazılmış ·
   THE_WAKING_GROUND yok — format kartına dürüst kayıt düşüldü
   (KILAVUZ_REHBERI §2.4, 21.08.2026)

🔴 ÖLÇÜM DURMUŞ — deponun bir numaralı açığı (25.08.2026 denetimi)
   Canlı sistemde (T1-T4) ölçülmüş film sayısı için sayac.sh'i çalıştır;
   bu satır sayı taşımaz. Ama ölçeği bilmen gerekiyor: yazılmış film sayısı
   ile ölçülmüş film sayısı arasında iki mertebe fark var ve tek ölçüm
   ⛔ yayınlanmaz çıktı. Sonucu şudur: 127 dersin ve kılavuz gövdesinin
   HİÇBİRİ şu an doğrulanabilir değil — ne çürütülebiliyor ne onaylanabiliyor.
   22.08'de eski tablolar "karşılaştırılamaz" ilan edilince ölçüm tabanı
   sıfırlandı ve yerine yeni taban konmadı.
   ⛔ Yeni film YAZMAK bu açığı büyütür, kapatmaz. Kapatan tek şey:
      elde yazılı duran filmlerden birkaçını ÜRETİP dört mercekten geçirmek.

🟡 URETIM_ONCESI_ANALIZ/01 ders etkinlik raporu 01.08.2026 kesitinde
   (50 ders); D51-119 hiç ölçülmedi — rapor yeniden koşulmalı

✅ sayac.sh bayatlığı — ÇÖZÜLDÜ (25.08.2026)
   Betiğin son değişikliği 17.08'di, QA mimarisi 22.08'de değişti: beş gün
   önceki dünyayı raporluyor, KAPALI tabloları "ÖLÇÜM DURUMU" diye basıyordu.
   Artık ÖLÇÜM DURUMU yalnız T1-T6'yı okur; kapalı tablolar ARŞİV başlığında
   "durum değildir" etiketiyle durur. Üç hata daha çıktı ve düzeltildi:
   (a) tablo ayracı ile ilk veri satırı arasındaki BOŞ SATIR taramayı
       durduruyordu — altı canlı tablo da "0 satır" sayılıyordu,
   (b) 01_FILM_RAPORLARI'ndaki FRAGMAN kayıtları film sayılıyordu (−3),
   (c) "ölçülmemiş" ile "ölçüldü ama tabloya işlenmedi" ayrılmıyordu.

🟡 Ders sayısı üç belgede farklı
   Gerçek kaynak DERSLER/ klasörüdür (sayac.sh sayar).
   URETIM_ONCESI_ANALIZ/00_README bayat sayı taşıyor.
   (yapılcaklar.md 25.08.2026 denetiminde depoda BULUNAMADI — satırdan düştü)

🟡 Kırık dosya referansları
   SUREKLILIK_LEDGERI.md · THE_RISING_SNOW_KAPAK.md
   THE_GLASS_WORLD_SHORTS.md · THE_LAST_ARCHIVE_SHORTS.md

🟡 QA sistemi çatallı
   QA_PROMPTLARI/ (yatay, 8-11 kategori) ve
   yatay_7_9_dk_filmler/kilavuzlar/kalite_kontrol/ (3 geçişli) ayrı sistemler.
   İki sistemden gelen skorlar aynı tabloda karşılaştırılamaz.

✅ araştırmalar/ açığı — KAPATILDI (26.08.2026, sahip kararı)
   Dokuz kılavuzun atıf verdiği araştırma dosyaları depoda ve git'te hiç
   olmadı; sahip 26.08.2026'da geri gelmeyeceklerine karar verdi ve klasör
   beklentisi haritadan kaldırıldı. Karar: kılavuzlar kaynak atfı olmadan
   KENDİ BAŞINA geçerli sayılır; gövdelerdeki "araştırmalar/N.md" satırları
   tarihsel etikettir, dosya beklentisi değil — silinmez, yeni atıf da
   yazılmaz. Kılavuz gövdesinin doğrulaması artık tek yoldan yapılır:
   gerçek yayın verisi (kart Y geri beslemesi → 01_DERS_ETKINLIK_RAPORU).
   (Kardeşi film_analizleri/ 22.08'de sessizce silinmişti — 25.08.2026'da
   `git checkout 15f3d3e^ -- film_analizleri` ile geri alındı, duruyor.)

🟡 KILAVUZ_REHBERI §8 film matrisi bayat — depodaki filmlerin çoğu listede yok.
🟡 dikey_shorts_filmler/ içinde 16:9 YATAY filmler var (klasör adı yanıltıyor).
```

---

# 7. DOĞRULAMA — iş bitince çalıştır

```bash
bash kilavuzlar_ve_sistem_dosyalari/sayac.sh   # sayılar tuttu mu, ders boşluğu var mı
git status                                      # her şey commit'lendi mi
# QA raporu işlendiyse — betik koşulmadan T tablosuna satır yazılmaz [D161]
# python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <ham raporlar> --film <film klasörü>

# başlıksız (panelden düşecek) film dosyası var mı — çıktı boş olmalı
# (25.08.2026: her format klasörlü — glob bir kademe derinleşti)
for f in dikey_shorts_filmler/*/*.md yatay_2_4_dk_filmler_*/*/*.md; do
  [ "$(grep -cE '^#' "$f")" -lt 3 ] && echo "BAŞLIKSIZ: $f"
done

```

---

# 8. AJANA SON SÖZ

```
Bu sistemin ölçülmüş gerçeği: kural eklemek kaliteyi artırmadı.
Kalite yükselten üç olayın üçü de kural değil, karar değişikliğiydi —
sabit lockoff kamera, sahneleri ayrı üretmek, tarif yerine sayısal kilit.

Yeni bir ders yazmadan önce sor: bu prompt cümlesiyle mi çözülüyor,
yoksa planla, sahne haritasıyla veya kurguyla mı? İkincisiyse dersi
LESSONS_LEARNED'a yazmak onu çözmez.

Ayrıntı: URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md
```

---

> **Bu dosya ne zaman güncellenir**
> □ Yeni klasör/format eklenince → §1 haritası + kart H
> □ Yeni QA rubriği eklenince → yeni görev kartı (§3)
> □ §6'daki bir açık kapanınca → satırı sil
> □ Yeni bir "hangi dosyayı güncelleyeceğim" sorusu çıkınca → yeni kart
>
> Bu dosyaya **içerik** taşıma. Adres ver, kaynağa yolla.
