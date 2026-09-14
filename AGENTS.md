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
│   │   ├── 00_YASAYAN_DERSLER.md     ⭐ 14.09.2026 · yeni filmin okuduğu TEK ders
│   │   │                             listesi (≤ 40 satır · ETİKET · DEĞİŞEN SATIR ·
│   │   │                             giriş/çıkış defteri). Emeklilik = listeden çıkış.
│   │   │                             okuma_cizelgesi.sh TUR 1'i buradan üretir.
│   │   ├── 00_DERS_YAZIM_KONTRATI.md §2b film dersi = FREKANS (≥2 film) + DEĞİŞEN
│   │   │                             SATIR + KAPI + TEKRAR (14.09); mod V → ADAY
│   │   └── 00_HIZLI_REFERANS.md      arşiv kilit HAVUZU (14.09) — çekirdek okuma değil
│   ├── DIS_FILM_ANALIZI/          🎞️ 05.09.2026 · ⛔ HAT KAPALI — film_analizleri/
│   │                                 kaldırıldı, iki şey buraya kurtarıldı:
│   │                                 · NOBODY_WAS_ALIVE ders seçkisi ⭐ CANLI —
│   │                                   kart H2 ③ (dışarıdan atıf alan dosya
│   │                                   taşınır): THE_LAST_SHIFT ve
│   │                                   THE_HOLLOW_COUNT §0.19 tabloları
│   │                                   buradan devraldı
│   │                                 · dört analiz promptu (KAMERA·OLAY·TEMA·
│   │                                   SENTEZ) — dış atfı YOKTU; H2'nin
│   │                                   "bilgi ucuz, yeniden yazmak pahalı"
│   │                                   gerekçesiyle korundu
│   │                                 Skor üretmez, T tablosuna girmez, sayaç saymaz.
│   ├── sayac.sh                      sayıları dosya sisteminden hesaplar
│   │                                 (14.09: film/alet dersi · YAŞAYAN n/40 ·
│   │                                  🔁 BULGU FREKANSI bloğu · rubrik ≤ 25 KB)
│   ├── film_klasoru_ac.sh            film klasörü AÇAR (elle cp/mv/rm YOK) — 14.09:
│   │                                 >8 sahne → 00_SAHNE_TABLOSU · --kilit-sahne ·
│   │                                 00_HIKAYE_ONAYI kopyası = YENİ REJİM işareti
│   ├── okuma_cizelgesi.sh            okuma çizelgesi — 14.09: yaşayan 40 ders +
│   │                                 OKUMA_CEKIRDEGI.txt manifesti ("—" meşru, ㉘)
│   ├── FILM_KLASOR_SABLONU/          🆕 01.09.2026 · film klasörü iskeletinin
│   │                                 KOPYALANABİLİR hâli (7 dosya taslağı).
│   │                                 Tanım KILAVUZ_REHBERI §2.0'dadır;
│   │                                 burası yalnız `cp -r` hedefi.
│   │                                 prompt_kontrol.py yolu atlar (SABLON)
│   │   └── 00_ANALIZ/                14.09.2026 reformu: 00_HIKAYE_ONAYI.md (sahip
│   │                                 onayı · yeni rejim işareti · ㉙) · OKUMA_CEKIRDEGI.txt
│   │                                 (TUR 2/3 manifesti, ≤30 dosya — film klasörüne
│   │                                 kopyalanmaz) · 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md
│   │                                 (>8 sahnede satır başına sahne · ㉚)
│   │
│   ├── SINEMATOGRAFIK_TEKNIK_KILAVUZ.md   lens/ışık/kamera + §17 karar tablosu
│   ├── SAHNE_DEVAMLILIK_KILAVUZU.md       karakter çapalama, seed
│   ├── REFERANS_PAKETI_KILAVUZU.md 🆕 06.09.2026 · KAPI 0 — biçim
│   │                                  kilidi metinle tutulmuyor [D146]:
│   │                                  §1 altı tetikleyici (eski "iki
│   │                                  insan/araç" sayımı ÖLDÜ) · §2
│   │                                  envanter (belgede kalan ↔ görselde
│   │                                  kilitlenen) · §3 durum merdiveni ·
│   │                                  §4 sayfa kanonu + yükleme kuralı ·
│   │                                  §5 sahne→referans eşleme · §6 kabul
│   │                                  kapısı · §7 geçersizlik
│   │                                  KAPI: LİSTE <FILM>_REFERANS_PAKETI.md
│   │                                        §0/§7 · BETİK ⑲ (FIX) · ⑳b
│   │                                  ⛔ paketin VARLIĞINI ölçen betik
│   │                                     kapısı HENÜZ YOK (TUR 12 · T12.4①)
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
│   ├── UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md 🆕 12.09.2026 · giysinin
│   │                                  GÖRÜNÜŞÜ (DONANIM = kimlik): beş arketip
│   │                                  (film adsız) · kask mimarisi + kask içi
│   │                                  ışık · malzeme sözlüğü + sert kabuk üç
│   │                                  kelime kuralı · zemin→renk · kir global
│   │                                  bitiş · sırt heykelsi pozitif (⬜) ·
│   │                                  kısaltma sırası · üç hazır blok
│   │                                  (kaynak: TUR 17 · sayı katmanı çürük,
│   │                                  sayısız yazıldı · ⬜ mercek adayı ⑭)
│   ├── UZAYLI_VARLIK_TASARIM_KILAVUZU.md 🆕 03.09.2026 · TEK uzaylı
│   │                                  varlık: niyet (huşu/dehşet/empati) ·
│   │                                  siluet/hareket · ANATOMY LOCK ·
│   │                                  reveal merdiveni K0-K4 + VARLIK
│   │                                  ŞERİDİ · varlık kelime sözlüğü
│   │                                  (kaynak: TUR 7 · uzay operası
│   │                                  yasağı SÜRER — ırk/filo yok)
│   ├── UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md 🆕 04.09.2026 ·
│   │                                  kadrajda istasyon/üs/büyük yapı
│   │                                  varsa ZORUNLU: ölçek birimi
│   │                                  (1H = kasklı gövde) · anatomi
│   │                                  kartı · mesafe-kesir tablosu
│   │                                  (16:9 ve 9:16 ayrı) · ölçek
│   │                                  şahidi merdiveni · yörünge ve
│   │                                  yüzey için İKİ AYRI negatif blok
│   │                                  (kaynak: TUR 9 · ⭐ Ders 32'yi
│   │                                  nesne-göreli birime çevirdi)
│   ├── ACILIS_KAPANIS_CIFTI_KILAVUZU.md 🆕 04.09.2026 · ilk kare ile
│   │                                  son kare TEK karar: kafiye mi
│   │                                  döngü mü · tek değişken kuralı ·
│   │                                  konum kilidi · ÇİFT KARTI
│   │                                  ⛔ kanca tipini (HOOK §4) ve final
│   │                                  tipini (FINAL §2) SEÇMEZ; ikisinin
│   │                                  BAĞINI yazar (kaynak: TUR 10)
│   ├── SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md 🆕 04.09.2026 · iki sahnenin
│   │                                  ARASI: beş soru tipi · dört cevap
│   │                                  tipi · ardışık aynı cevap yasağı ·
│   │                                  sınır satırı (End/Start) · hangi
│   │                                  cevap kesilebilir (ara halka /
│   │                                  açıklama / terminal bedel)
│   │                                  ⛔ DURUM DEĞİŞİMİ klibe değil
│   │                                  SINIRA yazılır (dynamic attribute
│   │                                  binding en zayıf eksen —
│   │                                  sayı: KILAVUZ_REHBERI §7)
│   │                                  (kaynak: TUR 11 · 06 §0'ın hedefi)
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
│   ├── KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md 🆕 11.09.2026 · TUR 15 ·
│   │                                  bible görünüş / KART davranış: sekiz satır ·
│   │                                  alışkanlık 3+1 · karar mimarisi · DAVRANIŞ ŞERİDİ
│   ├── OYUNCULUK_YAZIM_KILAVUZU.md 🆕 11.09.2026 · TUR 15 · ⑩ rubriğinin
│   │                                  YAZIM ikizi: izleyici cümlesi · ÇAPA ÜÇLÜSÜ
│   │                                  (SPEC'e) · sekiz niyet kanalı · tempo ·
│   │                                  anti-RESET · ⬜ kapı adayı ㉒ (yazılmadı)
│   ├── IKI_KISI_VE_AYRILIK_KILAVUZU.md 🆕 11.09.2026 · TUR 15 · ikinci insan
│   │                                  varsa: iki kart · faz farkı · cevap ızgarası ·
│   │                                  gecikme bandı · mesafe eğrisi · AYRILIK KARTI
│   ├── DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md 🆕 11.09.2026 · TUR 15 · replik
│   │                                  varsa: muhatap tipolojisi · DEĞİŞ-TOKUŞ
│   │                                  tablosu · sessizlik cevaptır · dinleyen
│   │                                  kadrajı · değer kayması testi
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
│   │                                      🆕 05.09.2026 · §3 🕰️ KÜME · §4b DÖNÜŞ HEDEFİ · §7 ⑥ birebir yazım
│   ├── DIS_REFERANS_OLCUMU.md 🆕 05.09.2026 · dış referans ölçümü (tek seferlik):
│   │                                      §2 süre/kurulum tablosu — ACI_YAYI §4b'nin saha kanıtı
│   │                                      §3 ölçek şahidi sözlüğü — UZAY_USSU §5.3'e 10 vaka
│   │                                      ⛔ ANALİZ HATTI DEĞİL · klip/kare/ham rapor depoya GİRMEZ
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
│   │                                 --film: ①.12 DERS DÖNÜŞÜ bölümü yoksa NOT (14.09)
│   │   └── ders_frekans.py           🔁 14.09.2026 · ham raporlarda VERDICT / düşük kategori ×
│   │                                 FARKLI FİLM sayısı (mod D/V) → hangi örüntü dersleşmemiş;
│   │                                 dosya yazmaz, sayac 🔁 bloğu çağırır (--ozet / --tam)
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
│   │   ├── ARSIV_6_MERCEK/           ⛔ eski 6 rubrik — ÇALIŞTIRILMAZ, kanıt
│   │   ├── ARSIV_RUBRIK_DIYETI/      ⛔ 14.09.2026 rubrik diyeti: altı rubriğin diyet-öncesi
│   │   │                             tam kopyası + kesilen metinler — ÇALIŞTIRILMAZ
│   │   ├── ARSIV_CIKTI_KURALLARI.md  ortak çıktı kalıbının uzun hâli (tek kopya, 14.09)
│   │   ├── 1_KARE_DIKEY_EK.md        ① dikey ek — yalnız dikey filmde rubriğin sonuna
│   │   │                             yapıştırılır (VERTICAL RULES A-D + kat. 12-14)
│   │   ├── 13_UYUM_QA_CRITIQUE_PROMPT.md        ⑬ sahne ↔ PROMPT · üretim sadakati
│   │   ├── 14_HAREKET_QA_CRITIQUE_PROMPT.md     ⑭ 🧍 HAREKET MANTIĞI · "beden bunu NEDEN
│   │   │                                        yaptı" — amaçsız/döngü/kayma/hayalet
│   │   │                                        tutuş (14.09.2026 · sahip talebi)
│   │   ├── 15_YON_QA_CRITIQUE_PROMPT.md         ⑮ 🧭 YÖN VE HEDEF · "vektör hedefe
│   │   │                                        vardı mı" — yanlış yöne dönüş · boşa
│   │   │                                        ateş · 180° kırılması (14.09.2026)
│   │   │                                        ⭐ ikisinin ürünü PROMPT ORDERS tablosu
│   │   │                                          = sonraki filmin ders satırı (kart G)
│   │   ├── 1_KARE_QA_CRITIQUE_PROMPT.md         ① sahne içi · yatay VEYA dikey
│   │   ├── 2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md   ② sahneler arası · dünya+gövde
│   │   ├── 3_SES_QA_CRITIQUE_PROMPT.md          ③ film boyu ses · YALNIZ KURGU
│   │   ├── 4_HIKAYE_QA_CRITIQUE_PROMPT.md       ④ film boyu anlatı · (+PLAN)
│   │   ├── 5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md    ⑤ 🔬 derin tarama · özne-dışı
│   │   │                                        alan · risk tetikli · /4'e girmez
│   │   ├── 6_FIZIK_QA_CRITIQUE_PROMPT.md        ⑥ 🔬 derin tarama · sayısal
│   │   │                                        fizik (+KİLİT LİSTESİ = mod D)
│   │   ├── 7_AKSIYON_QA_CRITIQUE_PROMPT.md      ⑦ 🎯 okunurluk · risk tetikli
│   │   ├── 8_EFOR_QA_CRITIQUE_PROMPT.md         ⑧ 💪 bedel · risk tetikli
│   │   ├── 9_KADRAJ_QA_CRITIQUE_PROMPT.md       ⑨ 🎯 PLAN SADAKATİ · kamera planın
│   │   │                                        koyduğu yerde mi (06.09.2026 · D184)
│   │   ├── 10_OYUNCULUK_QA_CRITIQUE_PROMPT.md   ⑩ 🎭 plan sadakati · niyet/seçim/bedel
│   │   │                                        BEDENDE okunuyor mu
│   │   ├── 11_ISIK_QA_CRITIQUE_PROMPT.md        ⑪ 💡 plan sadakati · ışık klipten
│   │   │                                        klibe · yalnız planlı sınırda değişir
│   │   └── 12_HOOK_QA_CRITIQUE_PROMPT.md        ⑫ 🪝 plan sadakati · açılış/paylaşım/
│   │                                            çıkış + üç saniyelik düşüş TAHMİNİ
│   │                                            ⛔ ⑨-⑫ SPEC'siz koşulmaz; mod V satırı
│   │                                            tabloya girmez · ölçümden SONRA koşulur
│   │
│   ├── FILM_QA_RAPORLARI/         📊 SONUÇLAR (çıktı) — buraya YAZILIR
│   │   ├── 00_INDEX.md               ⭐ PROJEDEKİ TEK SAYAÇ + tamlık matrisi
│   │   ├── 01_FILM_RAPORLARI/        film başına kalıcı QA kaydı
│   │   ├── 02_HAM_RAPORLAR/          modelin ham çıktısı (film klasörleri), dokunulmaz
│   │   ├── T1_KARE_KALITE.md         ① skorları        ⭐ CANLI
│   │   ├── T2_DEVAMLILIK_KALITE.md   ② skorları        ⭐ CANLI
│   │   ├── T3_SES_KALITE.md          ③ skorları        ⭐ CANLI
│   │   ├── T4_HIKAYE_KALITE.md       ④ skorları        ⭐ CANLI
│   │   ├── T5_ARKA_PLAN_KALITE.md    ⑤ skorları · derin tarama, matrise girmez
│   │   ├── T6_FIZIK_KALITE.md        ⑥ skorları · derin tarama, matrise girmez
│   │   ├── T7_AKSIYON · T8_EFOR      ⑦⑧ skorları · risk tetikli, matrise girmez
│   │   ├── T9_KADRAJ · T10_OYUNCULUK · T11_ISIK · T12_HOOK
│   │   │                             ⑨-⑫ skorları · plan sadakati (06.09.2026 ·
│   │   │                             D184) · koşul tetikli · matrise girmez ·
│   │   │                             mod V satırı YOK
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
│       ├── 03_PLAN_ONCESI_KONTROL_LISTESI.md  18 madde (A0 hikâye onayı · 14.09) · ~20 dk · maliyet sıfır
│       │                             (26.08.2026: B3 tema indeksi +
│       │                              B4 açı yayı eklendi)
│       └── 04_ARASTIRMA_BULGULARI.md  ⭐ dış araştırma SÜZME KAYDI: hangi
│                                     bulgu hangi kılavuza indi, hangisi
│                                     GİRMEDİ ve neden (27.08.2026, 1. tur)
│                                     ⛔ kural buradan okunmaz — kuralın
│                                        NEREDEN geldiği buradan okunur
│       ├── TUR9_HAM_RAPORLAR/ · TUR10_HAM_RAPORLAR/ 🆕 04.09.2026 ·
│       │                             uzay üssü ve giriş/final turlarının
│       │                             HAM raporları — düzeltilmez,
│       │                             kısaltılmaz; her dosyanın başında
│       │                             koşulan prompt birebir durur
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
├── yatay_2_dk_filmler/            16:9 · FİLM KLASÖRÜ · 12 sahne × 10 s = 2:00 (modül)
│                                  🔁 13.09.2026 YENİDEN ADLANDIRILDI (sahip kararı):
│                                  eski adı `yatay_2_4_dk_filmler_uzay/` — belgelerdeki
│                                  "2-4 dk" ifadesi AYNI formatın eski adıdır; `_uzay`
│                                  soneki düştü (YAPI_GRAFI borç ① ödendi). 269 adres
│                                  aynı gün süpürüldü (kart H2 altıncı tur). Eski ad
│                                  yalnız bu gibi tarihli notlarda kalır.
│   (yatay_2_4_dk_filmler_zombi/ — 26.08.2026'da kart H2 ile KALDIRILDI.
│    Depo yalnız UZAY filmleri içindir; zombi türü de kapandı. Tür kartı
│    KILAVUZ_REHBERI §4.2'de ⏸️ RAFTA duruyor, silinmedi.)
├── yatay_4_dk_filmler/            16:9 · FİLM KLASÖRÜ · 24 sahne × 10 s = 4:00 (modül)
│                                  🔁 13.09.2026 YENİDEN ADLANDIRILDI: eski adı
│                                  `yatay_3_5_dk_filmler/` — "3-5 dk" ifadesi aynı
│                                  formatın eski adıdır. Sahip beyanı: 24 sahne · 4 dk
│                                  (12-sahne merdiveni: 2 dk = 12 · 4 dk = 24 · 6 dk = 36 · 8 dk = 48)
├── yatay_6_dk_filmler/            🆕 13.09.2026 · 16:9 · 36 sahne × 10 s = 6:00 · 2 × 18
│                                  yazım 3-5 dk ile BİREBİR AYNI · ⭐ TEK FARK: QA birimi
│                                  BÖLÜM — on iki mercek iki yarım mastera ayrı koşulur
│                                  (rapor_kontrol.py --bolum n/2 ZORUNLU) · kart §2.6 ·
│                                  akış: klasörün README.md'si
├── yatay_8_dk_filmler/            🆕 13.09.2026 · 16:9 · 48 sahne × 10 s = 8:00 · 2 × 24
│                                  aynı kural (QA birimi BÖLÜM) · kart §2.7
│                                  ⚠️ 8 dk'da İKİ HAT: bu MODÜL hattı; faz mimarisi
│                                  (THE_SLOW_STONE) 10_20'de KALIR · ⬜ §2.5 alt sınırı
│                                  sahip kararı (H2 ④)
└── yatay_10_20_dk_filmler/        16:9 · 3 PERDE · FİLM KLASÖRÜ · bant 7-20 dk
    ├── THE_SECOND_SHIP/              120 sahne × 10s = 20:00 (8s'den sapma)
    └── THE_SLOW_STONE/               48 sahne × 10s = 8:00 — bandın KISA UCU
    (yatay_7_9_dk_filmler/ — 04.09.2026'da sahip kararıyla KALDIRILDI.
     Tek filmi THE_SLOW_STONE buraya taşındı; kendi kilavuzlar/ dizini
     kilavuzlar_ve_sistem_dosyalari/'na çıktı ve format-bağımsız oldu.
     Format kartı KILAVUZ_REHBERI §2.4'te ⏸️ KAPANDI notuyla duruyor.)

    (film_analizleri/ — 05.09.2026'da sahip kararıyla KALDIRILDI. Dış film
     analiz hattı kapandı; zaten film sayımına girmiyordu. İki şey kurtarıldı
     ve merkeze taşındı → kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/ :
     NOBODY_WAS_ALIVE ders seçkisi (kart H2 ③ — iki canlı film adresliyor) ve
     dört analiz promptu (dış atfı yoktu; pahalı metodoloji olduğu için).
     Analiz edilmiş film klasörü git'te durur — `git show e9bcf36:film_analizleri/…`
     ⛔ DIKEY_4_PARCA/ ve CORAK_TOPRAKLAR analizi HİÇBİR COMMIT'TE YOKTU,
        geri alınamaz — bkz. kart H2, beşinci tur.)
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
   ⭐ 14.09.2026 — self-contained ≠ Bible'ın TAMAMI. Kadrajda olmayan
   YAZILMAZ: promptun ilk satırı `IN FRAME:` (face · hands · torso · legs ·
   full body · back | none) ve yalnız orada yazılan tarif edilir; 75 mm
   insert'te yüz cümlesi yoktur [D214 · ㉖]. Videoda Bible tekrar edilmez —
   tek satır `START FRAME:`. NEGATIVE = §5.1 çekirdek 8 cümle + ≤3 (㉗).
   Bütçe POZİTİF gövde kelimesidir (image 100-250 · video 120-300, ①).
   Yalnız 00_ANALIZ/00_HIKAYE_ONAYI.md taşıyan klasörlerde; eski
   klasörler eski bantla (sahip kararı). Sabitler prompt_kontrol.py başında.

④ QA RAPORU GELDİĞİNDE HAM ÇIKTI KORUNUR
   Önce 02_HAM_RAPORLAR/<FILM>/ altına olduğu gibi kaydet, sonra özetle.
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
**Skill:** `yeni-film` — akışın uygulanabilir hâli. ⛔ Ajan bu kartı değil o
skill'i okur; buraya eklenen her madde ORAYA da eklenir (D165'in ödediği bedel).

```
⭐ 14.09.2026 · SAHİP KARARI — "YAVAŞ OLMASI TASARIMDIR" (08.09.2026) GERİ ALINDI.
   Ölçüm (THE_LOCKED_PULSE): 126 dosya / ~42.000 satır okuma, çizelgede
   126/126 satırdan "kilit" çıkmış, "—" SIFIR (sahte); 25 × 120 satırlık
   sahne dosyası; klasör 747 KB, üretim 0 kare; 17/17 kapı imzası tam,
   hikâye vana tamiri. Uzun akış kapıya göre optimize film üretti.
   Yeni BÜTÇE (TODO_AKIS_VE_DERS_REFORMU.md · yalnız 14.09'dan sonra
   açılan klasörlerde — 00_ANALIZ/00_HIKAYE_ONAYI.md işareti):
     OKUMA   yaşayan 40 ders + ≤30 dosyalık manifest; "—" MEŞRU (㉘)
     SAHNE   ≤8 dosya başına · >8 TABLO + 5 kilit sahne (㉚)
     KİLİT   film başına ≤20 (㉕)   PROMPT  IN FRAME + kelime bandı (① ㉖ ㉗)
     HİKÂYE  dosya okunmadan sahibe ONAYLATILIR (㉙)
   DEĞİŞMEYEN: kapı atlanmaz, tur örneklenmez, alt-ajan açılmaz.
   OPEN CIRCUIT dersi (dört dosya hiç açılmadı → sekiz bulgu) doğru
   kalır; cevabı "hepsini oku" değil, "doğru 30'u GERÇEKTEN oku".
```

```
SORULAR — ⭐ DÖRT soru, TEK turda (AskUserQuestion) 🆕 08.09.2026
 □ ① KONU      "AI karar versin" / "konuyu ben vereceğim"
      AI seçerse HAVADAN seçmez: sayaç 🎭 TEMA DAĞILIMI (en az kullanılan
      tema) + KILAVUZ_REHBERI §8 matrisi (tükenen ortam kartı ve novum
      tipi) okunur, DEPODA EKSİK OLAN seçilir, gerekçe 02_KONSEPT'e yazılır.
 □ ② FORMAT    dikey shorts / 2 dk (12) / 4 dk (24) / 6 dk (36) / 8 dk (48) / 7-20 faz
      ⛔ SORULMAK ZORUNDA — betiğin 1. argümanı ve tek başına dört şeyi
        belirler: bölüm sayısı · süre bandı · sahne bandı · açılacak kart.
        Konudan TÜRETİLEMEZ.
      🆕 13.09.2026: 12-sahne modül merdiveni (§2.2 → §2.3 → §2.6 → §2.7);
        6/8 dk'da yazım 3-5 ile aynı, TEK FARK QA birimi BÖLÜM. 8 dk'da
        iki hat var — modül (§2.7) mi faz (§2.5) mi, mimariye göre.
 □ ③ SAHNE     formatın varsayılanı / bandın üst ucu / kullanıcı sayısı
      §2.1-§2.7: dikey 6 (sabit) · 2 dk 12 · 4 dk 24 (13.09.2026 modül
      beyanı; 25'li eski kayıt kartta tarihli) · 6 dk 36 · 8 dk 48 · 7-20
      kartın bandından. Bandın DIŞI sahibin açık iznini ve plana gerekçe
      ister [D74] — WHITE FLOOD 30'a böyle çıktı, 40 yazılmadı.
 □ ④ REFERANS PAKETİ   yazılsın / yazılmasın / analiz karar versin
      "analiz karar versin" = 02_KONSEPT'te ALTI tetikleyici tek tek ölçülür.
      "yazılmasın" = dosya SİLİNMEZ, ⬜ BEKLİYOR + PLAN'a tek satır gerekçe.

 ⛔ BU DÖRDÜNDEN BAŞKA SORU SORULMAZ.
    Film adı TÜRETİLİR (İngilizce 2-3 kelime, BUYUK_HARF_ALT_CIZGI) ·
    klip süresi ARAÇTAN ÖLÇÜLÜR [D124] · ortam/tür/tema/novum/hook
    karttan ve okumadan çıkar. Akışın uzunluğu OKUMADAN gelir, sorgudan
    değil; ek soru kullanıcıyı açık uçlu mülakata çeker.
 ⭐ TEK TARİHLİ İSTİSNA (14.09.2026 · sahip kararı): BEŞİNCİ SORU = HİKÂYE
    ONAYI — mülakat değil KAPI. Altıncı soru yoktur.
```

```
HİKÂYE — ⭐ 0.7 · dosya okunmadan yazılır, sahip ONAYLAR (14.09.2026)
 Gerekçe: LOCKED_PULSE 17/17 kapı imzasıyla yazıldı, hikâyesi vana
 tamiriydi, sahip onu en sonda gördü — "neden izlensin" kapısı yoktu.
 Dersler hikâyeyi İYİLEŞTİRİR, üretmez; kapıya göre yazılan hikâye
 kapıya benzer.
 □ Hiçbir ders/kılavuz/QA kaydı açılmadan sohbete yazılır, DÜZ TÜRKÇE
   (D-no · "novum" · kurulum harfi · "kilit" YASAK — sahip okur):
     LOGLINE ≤ 25 kelime · NEDEN İZLENİR (tutan TEK soru) · BEDEL
     (ne kaybediyor, hangi sahnede) · SAHNELER S0…Sn ≤ 15 kelime, olay dili
 □ AskUserQuestion, tek soru: ① ONAY ② DEĞİŞTİR (not → yeniden yazılır,
   yama değil) ③ RED (yeni hikâye). En çok 3 tur; üçüncü RED → konu
   değişir (soru 1'e dönülür).
 ⛔ ONAY olmadan klasör açılmaz, dosya okunmaz, hiçbir şey yazılmaz.
 □ Klasör açılınca onaylı metin 00_ANALIZ/00_HIKAYE_ONAYI.md'ye işlenir
   (betik S satırlarını damgalar; ONAY: <tarih> · sahip · TUR n/3).
   Bu dosya klasörü YENİ REJİME sokar (prompt_kontrol ㉕-㉚).
 □ Sıralama/PLAN onaylı satırlardan sapıyorsa SAPMA bölümü + yeniden onay
   [D74]; sahne sayısı değişirse --sahne-guncelle + yeniden onay.
 Kapı: prompt_kontrol ㉙ — ONAY tarihli · satır = sahne · jargon yok.
```

```
KLASÖR — analizden ÖNCE açılır, analiz İÇİNE yazılır
 □ ⭐ İSKELET TEK YERDE TANIMLI: KILAVUZ_REHBERI §2.0 (01.09.2026).
   Kopyalama da tek yerde — 08.09.2026'dan beri BETİK:
      bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh \
           <FORMAT_KLASORU> <FILM_ADI> <SAHNE_SAYISI> [BOLUM_SAYISI]
   Betik: şablonu kopyalar · dosyaları <FILM>_<ROL>.md yapar · ≤8 sahnede
   çalışma dosyalarını damgalar, >8 sahnede 00_SAHNE_TABLOSU.md üretir ·
   okuma çizelgesini üretir · 00_HIKAYE_ONAYI.md'yi kopyalar (yeni rejim
   işareti, 14.09.2026). Kilit sahneler: --kilit-sahne <FMT> <FILM> S<nn> <ROL>.
   ⛔ ELLE cp/mv/rm YAPILMAZ — elle kopyalamada son iki iş kaçıyordu.
   Sahne sayısı sonradan değişirse: --sahne-guncelle (var olanı EZMEZ).
   --analiz-ekle eski klasöre 00_HIKAYE_ONAYI.md KOPYALAMAZ — eski film
   eski rejimde kalır (sahip kararı); yeni rejime almak sahibin elle işi.
   Yedi dosya: PLAN · BOLUM_1..n · KAPAK · MUZIK · YAYIN_PAKETI
               (TAMAMEN İNGİLİZCE) · QA_SPEC     + 00_ANALIZ/
   Bölüm sayısı FORMATTAN gelir; 7-20 dk hattında faz sayısı kadardır.
   ⛔ Format klasörünün köküne .md BIRAKMA — orada yalnız 00_README
      durur; sayaç kökteki her girdiyi BİR FİLM sayar.
   ⛔ Eski filmler YENİDEN BÖLÜNMEZ/ADLANDIRILMAZ. İskelet YENİ filmler
      içindir; toplu yeniden adlandırma ölçülmüş hiçbir sorunu çözmez ve
      QA kayıtlarındaki dosya adlarını bayatlatır.
 □ Adlandırma: <FILM>_<ROL>.md · BUYUK_HARF_ALT_CIZGI · Türkçe karakter yok
      film adı ÖNDE durur [D160/⑪.0: dosya klasörden çıkınca adı tek kimliği]

00_ANALIZ — altı adım, altı dosya (+ 00_HIKAYE_ONAYI.md, 14.09). ⛔ Sırası
            atlanmaz, biri bitmeden diğeri yazılmaz, hepsi bitmeden FİLM YAZILMAZ.

 □ 0 · 00_OKUMA_CIZELGESI.md   ⭐ YAŞAYAN DERSLER + ÇEKİRDEK KILAVUZLAR + QA
      Betikten üretilir (film_klasoru_ac.sh onu da koşar):
         bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>
      ⭐ 14.09.2026: "hepsi" değil — yaşayan 40 ders (00_YASAYAN_DERSLER.md)
        + manifest (FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt, ≤30
        dosya) + QA raporları. Sayı çizelgenin özet bloğunda.
      ⛔ Her satır okununca ⬜ → ✅ VE "bu filme düşen kilit" sütunu dolar;
        kilit çıkmadıysa "—". Boş hücre "okudum" ile "atladım" arasını
        ayırt ettirmez ve ayırt edilemeyen şey yapılmamış sayılır.
      ⭐ "—" MEŞRUDUR: etiketi filme uymayan satır ([kask] · [replik] ·
        [iki-insan] · vakum · düşük-g …) açılmaz, "—" yazılır. Sıfır "—"
        çizelgeyi SAHTE yapar (prompt_kontrol ㉘ BLOCK — LOCKED_PULSE 126/126).
      ⛔ ⬜ kalan satır varken KONSEPT yazılmaz (㉘ FIX).
      TUR 1 00_YASAYAN_DERSLER.md — 40 ders, ETİKET'i uyanın metni açılır
      TUR 2/3 manifest — 02_RISK_KARTLARI · 03_PLAN_ONCESI · 06_HIKAYE_HATTI ·
        KILAVUZ_REHBERI (§2.x · §3 · §4 · §5 · §7) · IMAGE_VIDEO_PROMPT_TEMPLATES V3 ·
        novum · tema · hook · açı yayı · viral · kurgu ritmi · politika ·
        dört oyunculuk kılavuzu · [kask] donanım + giysi · [replik] ses ·
        [dikey] 05_DIKEY_HAT + mikro drama · [faz] faz mimarisi.
        Manifest dışı kılavuz HAVUZDUR (KILAVUZ §1 tablosu); açılan ek dosya
        çizelgeye "havuzdan açıldı" satırıyla eklenir (tek elle-satır istisnası).
      TUR 4 FILM_QA_RAPORLARI/ index · 09_URETIM_RED_DEFTERI · T tabloları
      TUR 5 01_FILM_RAPORLARI/ → BEŞ kayıt seçilir ve seçim gerekçelenir:
        ① aynı format ② aynı ortam kartı ③ aynı tema ④ en düşük skor
        ⑤ en yakın konsept
      ⭐ Kılavuz ne YAPILMASI GEREKTİĞİNİ, QA kaydı NE OLDUĞUNU söyler.
        Red defteri deponun politika/red konusundaki TEK sayacıdır.
      ⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır — bu yüzden
        dosyadır, bellek değil.

 □ 1 · 01_QA_DERS_HASADI.md   okunanlardan BU filme düşen kilitler
      Üç tablo: ders kilitleri · QA arızaları · red defteri sınıfları.
      ⛔ Sıfır satırla ilerlenmez; ders metni kopyalanmaz, bu filmde NE
        YAPILACAĞI yazılır. Kilit prompta ETİKETSİZ girer [D45].

 □ 2 · 02_KONSEPT_VE_RISK.md
      Sahibin talebi BİREBİR; fizikle çelişiyorsa yeniden tanımlanır ve
      sapma AÇIKÇA yazılır [D74].
      Format · ortam kartı §3 · tür §4.1 · KLİP SÜRESİ ARAÇTAN ÖLÇÜLÜR [D124].
      Konsept kapısı ①TEK KARE ②KİNETİK BAĞIMSIZLIK ③BAŞLIK ŞEMASI —
      üçü ✅ değilse KONSEPT REDDEDİLİR, sıralama yazılmaz.
      ⛔ TEK KARE cümlesi TAŞIYICI NESNENİN ADINI içerir [D157].
      TEMA: TEMA_MUHENDISLIGI §3 → §5 → §9; TANIM cümlesi, TAKAS değil [§3c].
      ⛔ 02_RISK_KARTLARI PLAN'dan ÖNCE: 5+ risk çıkıyorsa KİLİT TAVANI ≤ 20
        (14.09.2026 — "malzeme azalt" geri alındı; dışarıda kalan kilitler
        PLAN'a `UYGULANMAYAN KİLİTLER` olarak gerekçeyle; prompt_kontrol ㉕).
      ⭐ B5 DÖRTLÜSÜ sahne haritasından ÖNCE: İSTEK (film başlamasa da var
        olan bir İŞ — "anlamak/görmek/fark etmek" DEĞİL) · ENGEL ·
        BEDEL (+ SAHNE no) · MUHATAP. ⭐ ASIL KAPI BEDEL'dir.
        İki insanlıysa AYRILIK (B5b) zorunlu.
      ⭐ KARAKTER KARTI — B5'ten hemen SONRA [KARAKTER_KARTI_VE_DAVRANIS §1 ·
        11.09.2026]: sekiz satır, her satırda sahne numarası; bible GÖRÜNÜŞÜ,
        kart DAVRANIŞI kilitler, kart PROMPTA GİRMEZ. İki insan varsa iki
        kart ≥3 davranış satırında AYRIŞIR + İSTEK ÇAPRAZI [IKI_KISI §2-§3].
      POLİTİKA SATIRI (B6 · KART 12): en red-riskli kare + nötr tarifi.

 □ 3 · 03_SAHNE_SIRALAMASI.md   ⭐ X SAHNENİN SIRASI
      Vuruş tablosu → hook mimarisi → sıralama → ardışık çift denetimi →
      kurulum iskeleti → replik yerleşimi → metinsiz sayaç → üretim sırası.
      İKİ BÜTÇE burada dağıtılır, üretimden SONRA eklenemez:
        KARAKTER_VE_DUYGU §6 · KURGU_RITMI §2 örüntü kırıcı (ardışık iki
        sahne aynı ölçek + palet + ses dokusunda OLAMAZ).
      ⭐ Haritaya üç satır daha [TUR 15]: DAVRANIŞ ŞERİDİ (G ≤ %50 · K'dan
        sonra G gelmez) [KARAKTER_KARTI §4] · TEMPO sütunu [OYUNCULUK_YAZIM
        §4] · KARAR MİMARİSİ (reddedilen nesne kadrajda) [KARAKTER_KARTI §3].
        İki insan: AYRILIK KARTI + MESAFE EĞRİSİ + FAZ FARKI [IKI_KISI §2·§5·§8].
        Replik: DEĞİŞ-TOKUŞ TABLOSU (DEĞİŞİM boş replik silinir)
        [DIYALOG_SAHNESI §2-§3].
      ACI_YAYI §3 güvenli bant (ardışık çift ≥1 ölçek kademesi VE ≥45°) ·
        §4 kurulum sayısı · AÇI TİPİ sayısı ≥3 (KAMERA_ACISI §2).
      ⭐ KURULUM İSKELETİ satırı — sahne sayısı kadar harf.
        12+ sahnede KÜME ≥2 · DÖNÜŞ ≥%40 [ACI_YAYI §3 🕰️ · §4b].
        6-11 sahne ve dikey shorts MUAF.
        ⛔ BU SATIR KAPIYI AÇAR — prompt_kontrol ⑩④ yalnız onu beyan eden
          dosyada koşar. Aynı harfin kamera metni BİREBİR kopyalanır +
          işaret satırını taşır [§7 ⑥].
      ⛔ REPLİK SANİYELERİ HESAPLANMAZ, HESAPLATILIR [D122].
      ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168]:
        DORUK → merkezî seçim → kapanış imajı → S0 → kalanı
        (referans paketi yazıldıysa ilk halka odur).
        THE SINKING STAKE: 25 sahnenin 14'ü üretildi, eksik 11'i ARDIŞIK
        ve filmin SONUYDU.
      ⛔ İPTAL KAPISI yazılır: hangi sahne tutmuyorsa film üretilmez.

 □ 4 · 04_UYARI_NOTLARI.md   ⭐ hasat × sıralama
      Her satır ÜÇ şeyi taşır: hangi sahne · hangi ÖLÇÜLMÜŞ kayıt · ne
      yapılacak. ⛔ Kaynağı olmayan uyarı yazılmaz; "dikkat edilmeli" bir
      uyarı değildir. Şablondaki TEKRAR EDEN ARIZA tablosunun HER satırı
      cevaplanır (tablo büyür; sayı belgeye yazılmaz) — "bu filmde yok" da GEREKÇE ister.
      ⛔ 🔴 satırları kapanmadan sahne çalışmasına geçilmez.

 □ 5 · 05_SAHNE_CALISMALARI/   ⭐ SAHNE SAHNE — ≤8 sahne DOSYA · >8 sahne TABLO
      ⭐ 14.09.2026: sahne sayısı >8 ise betik 00_SAHNE_TABLOSU.md üretir —
        sahne başına BİR satır, 11 sütun (OLAY BAŞ→SON · B5 · KURULUM · OPTİK
        eni/px · IN FRAME · TAŞIYICI · IŞIK·SES·FİZİK · REPLİK · KİLİT/UYARI ·
        İZLEYİCİ CÜMLESİ · KAPI); yalnız 5 KİLİT SAHNE tam dosya alır:
        film_klasoru_ac.sh --kilit-sahne <FMT> <FILM> S<nn> <ROL>
        (HOOK · NOVUM · DORUK · BEDEL · FINAL, her rol bir kez; ㉚ satır =
        sahne sayısı + beş rol dosyası). IN FRAME sütunu promptun ilk satırıdır.
      Kilit sahne dosyasında (≤8 sahnede her dosyada), filme ve FİLMİN
      KONUSUNA göre: olay
      (BAŞTA/SONDA ayrı) · B5 bağı · OPTİK ARİTMETİĞİ (kadraj eni · nesne
      sığıyor mu · ana nesne ≥100 px [D179]) · kurulum harfi + işaret ·
      devamlılık taşıyıcıları · ışık/ses/fizik · replik · ⭐VİRAL'in
      YÜZ+HAREKET satırları · o sahneye düşen kilit ve uyarılar · politika ·
      ⭐ İZLEYİCİ CÜMLESİ + niyet kanalı (≤2) + TASK ONLY [OYUNCULUK_YAZIM
      §1·§3] · kart bağı [KARAKTER_KARTI §10] · replikli sahnede DEĞİŞİM
      SATIRI (BAŞ ≠ SON) [DIYALOG_SAHNESI §6].
      ⛔ Bir sahnenin ÇALIŞMA DOSYASI (ya da tablo satırı KAPI ✅) kapanmadan
        o sahnenin PROMPTU yazılmaz.
      ⛔ 00_ANALIZ içinde "## ... SAHNE <n>" ve 📸/🎥 başlığı YAZILMAZ.
        (prompt_kontrol'ün ATLA deseni 00_ANALIZ'i atlar; kural yine geçerli.)

YAZ — analizin çıktısı taşınır, yeniden düşünülmez
 □ PLAN → BIBLE → PROMPT sırası (KILAVUZ_REHBERI §6)
 □ Sahne başlıkları ## ile (kural ②) — ve YALNIZ bölüm dosyalarında
      (plandaki örnek bir prompt sahne dizisine karışır)
 □ PLAN'a taşınanlar: TEMA + ≥3 sahne indeksi · B5 · KARAKTER KARTI
      (bible'ın hemen üstüne) · vuruş tablosu · hook · sahne haritası
      (+ DAVRANIŞ ŞERİDİ · TEMPO) · ÇAPA ÜÇLÜSÜ (SEÇİM/BEDEL/FİNAL önce-sonra)
      · [iki insan] AYRILIK KARTI · [replik] DEĞİŞ-TOKUŞ · KURULUM İSKELETİ
      satırı · Bible'lar · sayısal kilitler · politika satırı · ÜRETİM SIRASI
 □ TIMELINE her satırda ≥1 gövde fiili · iki aşamalı eylem iki satıra ·
      hazırlık önce · imaj = ÇAPA'nın BEFORE'u, sonraki imaj = AFTER
      [OYUNCULUK_YAZIM §2·§8 · D179] · dinleyen klibinde replik metni YOK
      [DIYALOG_SAHNESI §7] · iki figürde KONUM KİLİDİ + faz farkı [IKI_KISI §2·§6]
 □ Her prompt self-contained (kural ③) — "BIBLE'a bak" atfı YASAK
 □ Bölüm SINIRI da ardışık bir ÇİFTTİR
 □ ⚠️ REFERANS PAKETİ — İSTEĞE BAĞLI 🆕 08.09.2026 (sahip kararı)
      Kararı SORU ④ verir; "analiz karar versin" seçildiyse
      REFERANS_PAKETI_KILAVUZU §1'in ALTI tetikleyicisi tek tek ölçülür.
      ⚠️ Doğruyken atlanıyorsa PLAN'a TEK SATIR gerekçe [D74 kalıbı] —
        sessizce atlanmaz. Paketin yokluğu artık filmi "yazımı tamam"
        olmaktan ÇIKARMAZ.
      ⛔ YAZILDIYSA kapı sertliğini korur: bir varlığın sayfası ONAYLI
        olmadan ve seed'i yazılmadan o varlığın geçtiği hiçbir sahne
        üretilmez [D168] — üretim sırasının ilk halkası odur.
      ⛔ Yazılmasa da dosya SİLİNMEZ, ⬜ BEKLİYOR ile durur.
      ⛔ KARŞI KAYIT DURUYOR ve silinmedi: D146 ⛔ ÇALIŞMIYOR — biçim kilidi
        METİNLE tutulmuyor, üç ölçülmüş vaka (SKYLIGHT 1 filmde 3 kask ·
        YERÇEKİMİ F2 · STANDING WIRE). Bedel: SINKING STAKE'in QA kaydı
        "referans paketi HİÇ ÜRETİLMEDİ → çapa yok" + "göğüs paketi S13'te
        değişiyor". Sahip bu maliyeti bilerek üstlendi.
 □ ⭐ <FILM>_QA_SPEC.md yazılır — yazım paketinin son parçası [Ders 117]
      A bloğu ④ HİKAYE alanları · B kurgu geometrisi + İNSAN ŞERİDİ ·
      C belgesiz merceklerin FLAGS sorularını cevaplayan kilitler
      + TARGET ASL BAND / ASL CURVE satırları (KURGU_RITMI §1; sabit
        ızgaralı filmde gerekçe satırı ZORUNLU [D74])
      ⛔ REPLİK ZAMANLARI VE DORUK SAATİ HESAPLANMAZ, HESAPLATILIR [D122]:
        replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
        doruk başlangıcı = hook + (doruk_sahne − 1) × klip
        Elle yazılan her kayıt er geç ızgara formülüyle çelişir ve ⑨
        HİZALAMA KAPISI'nın ölçü aletini bozar. Yazıldıktan sonra her
        kayıt formülle doğrulanır; sapma varsa yazım paketi TAM DEĞİLDİR.
      ⭐ B bloğuna FİNAL VURUŞ KANITI satırı [Ders 141]: tek karede BULUNAN
        ya da BULUNMAYAN, sayılabilir ve adı konabilir bir nesne + saniyesi
        + kaç tane. Kurgu kapısının dördüncü satırı bunu okur.
      ⭐ E bloğundaki her MAKİNE KAPISI kuru koşuyla DOĞRULANIR [Ders 142]:
        ffmpeg -hide_banner -filters | grep -q " <filtre> " || kapıyı yeniden yaz
        Her kapı üç satır taşır: KOMUT · DOĞRULANDI (<ffmpeg sürümü·tarih>)
        · İKAME (filtre yoksa hangi ölçüm koşulur). DOĞRULANDI satırı
        olmayan kapı YAZILMAMIŞTIR — bir SPEC'in kamera sabitlik kapısı
        kurulu olmayan bir filtreye yazılmıştı ve sessizce hiç koşmadı.
      ⭐ ÇAPA ÜÇLÜSÜ bloğu [OYUNCULUK_YAZIM §2 · 11.09.2026]: CHOICE/COST/FINAL
        — sahne · saniye · BEFORE · AFTER; ⑩ mod D'nin ANCHOR BEATS satırı
        buradan okunur. + DAVRANIŞ ŞERİDİ · [iki insan] İNSAN 2 kim solda +
        iki GAZE STRING · [replik] cevaplı/cevapsız + dinleyen kadrajı.
        ⬜ FILM_QA_SPEC şablonunda yeri HENÜZ YOK — elle blok; şablon kart G/P işi.
      ⛔ SPEC dosyası yoksa film "yazımı tamam" sayılmaz
      ⛔ ㉔ SPEC TAMLIK [D204 · 13.09.2026]: prompt_kontrol klasör modu yedi makine çapasını
        sayar (GRID · CLIP COUNT · FİNAL VURUŞ KANITI · İNSAN ŞERİDİ PLAN · NOVUM · KASK ·
        E DOĞRULANDI); ⬜ kalan satır eksiktir, yedisi yoksa SPEC KABUKTUR → BLOCK.
        38 SPEC'in 1'i tamdı; yeni-film akışının yedi klasörü FIX/BLOCK aldı.
      ⛔ ㉓ REPLİK ENVANTERİ [D203]: SPEC A `DIALOGUE LINES: N` ile promptlardaki tırnaklı
        replik sayısı eşit olmalı — replik yalnız prompt gövdesinde tırnak içinde üretilir;
        plandaki envanter prompt DEĞİLDİR (STATIC SHADOW 7→0 · MIRROR FAUNA 11→0).
 □ ⛔ QA PAKETİ ADIMI KALDIRILDI [11.09.2026 · proje sahibi kararı]
      `QA_PROMPTLARI/FILME_OZEL/` ve `qa-isle/scripts/rubrik_paketle.sh` depodan
      SİLİNDİ: bu hat artık filme özel QA promptu üretmiyor. QA, çıplak
      `QA_PROMPTLARI/_KAYNAK/` rubrikleriyle koşar ve MOD D'yi taşıyan şey
      operatörün `<FILM>_QA_SPEC.md`'yi rubriğin başına YAPIŞTIRMASIDIR [D129].
      ⭐ Kararın dayanağı deponun KENDİ ölçümüdür: D165 08.09.2026'da
        "ÇALIŞMIYOR" işaretlendi — paket VARKEN de operatör çıplak rubriği
        açtı (OPEN CIRCUIT 12/12 · UPWARD FALL 8/8 mercek mod V). Paketin
        varlığı mod D'yi hiçbir zaman garanti etmedi.
      ⛔ SPEC hâlâ ZORUNLUDUR ve tek kapıdır: SPEC yoksa film "yazımı tamam"
        sayılmaz, koşu mod V'dir, T tablosuna satır yazılmaz.

KONTROL ET
 □ URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md · 18 madde
      → maliyeti sıfır, 12 maddesi gerçek filmlerde gerçekten oldu;
        A0 HİKÂYE ONAYI her şeyden önce (14.09.2026 · ㉙)
 □ ⭐ PROMPTLAR YAZILDIKTAN SONRA, TEK KARE ÜRETMEDEN → görev kartı P

GÜNCELLE
 □ KILAVUZ_REHBERI.md §8 film matrisine satır ekle
 □ FILM_QA_RAPORLARI/00_INDEX.md → tamlık matrisine "0/4" satırı ekle
 □ Klasörün README.md'si varsa film listesine ekle

BİTİŞ
 □ bash sayac.sh → toplam film sayısı 1 arttı mı
 □ commit

"YAZIMI TAMAM" TANIMI
 □ 00_ANALIZ'in altı adımı kapalı (çizelgede ⬜ yok · 🔴 uyarılar kapalı ·
   her sahnenin çalışma dosyası ✅)
 □ PLAN · BOLUM_1..n · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC yazılı
 □ KARAKTER KARTI + ÇAPA ÜÇLÜSÜ yazılı; iki insanlıysa AYRILIK KARTI;
   replikliyse DEĞİŞ-TOKUŞ tablosu (11.09.2026 · TUR 15)
 □ prompt-kontrol klasör modu koştu — ㉓ REPLİK ve ㉔ SPEC TAMLIK temiz [D203 · D204]
 ⚠️ <FILM>_URETIM_DEFTERI.md bu listede DEĞİLDİR: klasörle birlikte BOŞ doğar,
   üretim sırasında dolar (kart B). Yazımı tamam sayılmak için dolu olması
   gerekmez; ⑬ UYUM merceği için gerekir.
 ⚠️ REFERANS_PAKETI bu listede DEĞİLDİR (08.09.2026) — yazılmadıysa
   PLAN'da tek satır gerekçe var mı, ona bakılır.
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
     BLOCK → üretme. 5+ risk çıkıyorsa kilit tavanına (≤ 20) çek, malzemeyi
             değil; prompt cümlesi eklemek bu bandda işe yaramıyor (14.09.2026).

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
 □ ⭐ ÜRETİM DEFTERİ — her KABUL EDİLEN klipte tek satır [11.09.2026]
      <FILM>_URETIM_DEFTERI.md → sahne · prompt kaynağı (dosya·satır) · araç ·
      seed · deneme · kabul tarihi · as-built sapma
      ⛔ Promptu araçta kısalttıysan/değiştirdiysen GÖNDERİLEN metin arşive
        kopyalanır (§3) — yoksa ⑬ UYUM merceği "kilit promptta mı yoktu, model
        mi uymadı" sorusunu SORAMAZ ve o sahne kilit sayımına girmez.
      ⛔ İLK KABUL SATIRI = PLAN'daki ÜRETİM SIRASI'nın ilk halkası (doruk / merkezî
        seçim). Değilse İKİNCİ KLİP ÜRETİLMEZ [D168 · 3 vaka → KARAR 13.09.2026]:
        liste planı bağlıyordu, teslimi bağlamıyordu — üç filmde de eksik kalan
        sahneler sıranın İLK halkalarıydı (STATIC SHADOW: S14 · S12 yok, S01-S10 tam).
      ⛔ Reddedilen deneme satırı SİLİNMEZ: bir kilidin kaç denemede tuttuğu,
        o kilidin çalışıp çalışmadığının tek ölçüsüdür.
      ⛔ Kurgu bitince TESLİM SATIRI doldurulur (master SHA-256 · süre · sahne
        sayısı · prompt sayısı). D188'in teslim şüphesi bu satırla kapanır.
 □ ⛔ QA'DAN ÖNCE, SIRAYLA (01.09.2026 · 11.09.2026'da bir betik eklendi):
      bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>          ⑪ · kuyruk kartı · köşe · ses kanalı
      bash .claude/skills/qa-isle/scripts/sahne_kapisi.sh <master> 10 <prompt_sayısı>   ⑬ · ızgara · sahne sahne ölçüm
      ⛔ sahne_kapisi.sh 🚨 TESLİM UYUŞMAZLIĞI basarsa HİÇBİR mercek koşulmaz:
        ölçülen makara plandaki film değildir, önce O kapanır [D188]
      ⛔ Operatör rubriği AÇAR ve `<FILM>_QA_SPEC.md`'yi AYNI mesajda başa
        yapıştırır [D129 · 9 film SPEC'siz mod V koştu]. Paket betiği yok.
      ⛔ olcum_kapisi.sh TESLİM SINIFI: 🚨 HAM ZİNCİR basarsa HİÇBİR mercek
        koşulmaz — önce kurgu, sonra ölçüm, sonra mercek [D181]
      ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK KOŞUL TETİKLİDİR [D184]:
        koşullar 00_README.md tablosunun son sütununda; dördü de MOD D
        (SPEC'siz koşusu boş). ⑫ yayından ÖNCE koşulur → kart Y
      ⑬ UYUM ÜRETİM TETİKLİDİR [11.09.2026]: üretim defteri dolu + sahne_kapisi.sh
        koşulmuşsa koşulur. Girdisi SPEC değil PROMPT METNİDİR; promptsuz koşusu
        "boş" değil YOKTUR. Çıktısı sonraki filmin dersidir → kart G
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
 □ ⑫ HOOK koşuldu mu (kart F8) — DROP-OFF PREDICTION üç saniyesi
   08_YAYIN_PERFORMANS_TABLOSU §1 "⑫ tahmin" hücresine OLDUĞU GİBİ kopyalandı
   mı [D184]. Tahminsiz açılan satırın eğrisi neyi kalibre edeceğini bilmez.
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
 □ ⭐ Gerçek eğrinin üç düşüş saniyesi ⑫'nin tahmininin YANINA yazılır:
      |Δ| ≤ 10 s tutan tahmin, ötesi tutmayan. Üç filmde 0/9 tutarsa
      yanlış olan ⑫'dir → 01_DERS_ETKINLIK_RAPORU (aleti izleyici kalibre eder)
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
   ⛔ ⑨-⑫ MOD V'DE TEKRAR DEĞİL, **GEÇERSİZ** [Ders 190 · 08.09.2026]:
      Plan sadakati mercekleri belgesiz koşulduğunda ekrandan bir plan TÜRETİR
      ve türettiği plan ekrana her zaman uyar — ⑫ THE OPEN CIRCUIT'te makarada
      OLMAYAN doruğa "peak placement 9/10" verdi. Rapor karantinadadır: T9-T12'ye
      satır girmez, 00_INDEX hücresi ❌ kalır, hiçbir bulgusu ders/sipariş/kesme
      üretmez. Dört rubriğin STEP −1'i de artık mod V'de DURUYOR; bağlayıcı kapı
      betiktir (`rapor_kontrol.py`).
   ⛔ OPERATÖRE İKİ DOSYA VERİLİR, TEK MESAJDA: `QA_PROMPTLARI/_KAYNAK/` rubriği
      + filmin `<FILM>_QA_SPEC.md`'si (SPEC BAŞTA). D165'in "tek paket" çözümü
      11.09.2026'da KALDIRILDI — kendi ölçümü paketin mod D'yi garanti
      ETMEDİĞİNİ gösterdi (OPEN CIRCUIT 12/12 · UPWARD FALL 8/8 mod V, paket
      VARKEN). SPEC yapıştırılmazsa koşu daha başlamadan mod V olur.
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

   ⭐ ①.9 TESLİM KAPISI [D188 · 07.09.2026] — `--film` verildiğinde betik
   PLANIN `## 🎬 SAHNE n` başlıklarını sayar ve raporların ÇOĞUNLUK sahne
   sayısıyla karşılaştırır. Fark varsa parti GEÇERSİZ.
   ⛔ **Merceklerin birbirini doğrulaması TESLİMİ doğrulamaz.** ⑤ çapraz
   sayım kapısı raporları BİRBİRİNE bakar; hepsi aynı makarayı izler ve
   EKSİK MAKARA OYBİRLİĞİYLE ONAYLANIR — mutabakat ne kadar güçlüyse kayıt
   o kadar ikna edici görünür. Parti dışındaki tek referans plandır.
   Vaka: YERÇEKİMİ F10 · plan 12 sahne · makara 11 klip · eksik olan
   FİLMİN SON KARESİYDİ (S120) ve on iki merceğin on ikisi onayladı.
   ⛔ Kapı ateşlerse: kesme listesi · REMOVE reçetesi · yeniden üretim
   UYGULANMAZ. Önce hangi sahnenin makarada olmadığı ADIYLA yazılır ve
   soru QA masasından ÜRETİM masasına geçer.

   ⭐ ①.10 GÖZ KAPILARI [D191 · 08.09.2026] — `--film` verildiğinde betik
   SPEC'in **F bloğundaki** `□` maddelerini ⬜ listesi olarak EKRANA BASAR.
   Bunlar filmin KENDİ kapılarıdır (ağız · kask biçimi · kıvılcım biçimi ·
   ışık takvimi · metin…), makineye inmezler ve **hiçbir merceğin kapsamında
   değildirler**: THE OPEN CIRCUIT'te on iki maddenin BEŞİ ekranda ihlal
   edildi ve on iki merceğin on ikisi sıfır yazdı. Her madde TEK KAREYLE
   kapanır (`ffmpeg -ss <sn> -i "$M" -frames:v 1`); kapanmayan madde kilit
   defterine ⬜ AÇIK girer ve o eksende skor SAYI TAŞIMAZ.

   ⭐ ①.11 BÖLÜM KAPISI [13.09.2026 · KILAVUZ_REHBERI §2.6/§2.7] — 6 ve 8 dk
   hattında (36/48 sahne) QA birimi FİLM değil BÖLÜMDÜR: on iki mercek iki
   yarım mastera AYRI koşulur ve betik `--bolum n/2` ile çağrılır. Bayraksız
   koşu ①.9'u YANLIŞ ateşler (plan 36 sayar, makara 18). Bayrakla: ①.9 yalnız
   `<FILM>_BOLUM_n.md`'yi sayar; baş bölümde final kategorileri (④ Ending ·
   ⑫ Peak Placement · ⑫ Exit), son bölümde hook kategorileri (④ Hook ·
   ⑫ Hook Question · ⑫ Stakes), her ikisinde bütün-film dörtlüsü (④ Structure ·
   ④ Retention · ⑫ Plateau · ⑨ Rhyme Pair) `—` olur — D185'in yarım-film
   uzantısı. ② sınır çiftini GÖREMEZ → SPEC B sınır satırı + elle kare.
   Kayıt etiketi üç yerde: ham `_B1_/_B2_` · T satırı `**Film** B1` · matris
   `**FILM** (B1)`. ⛔ Kesme listesi bölüm raporundan UYGULANMAZ. Tarif: klasör
   README'si. ⬜ Bütün-film dörtlüsünün ölçümü sahip kararı bekliyor.

   ⭐ ①.12 DERS DÖNÜŞÜ [14.09.2026 · reform FAZ 4 · kontrat §4] — koşu on iki
   rapor üretir ama iki satır üretmezse kayıt zinciri tamamlanmamıştır. Film
   kaydı (`01_FILM_RAPORLARI/<FILM>.md`) `## 🎯 ÜÇ SATIRLIK SONUÇ`'tan hemen
   önce `## 🔁 DERS DÖNÜŞÜ` bölümü taşır:
     TEKRAR: D<n> — <bulgu> · sayaç +1 → <ders dosyası>   |  TEKRAR: yok
     ADAY:   ADAY-<n> — <tek cümle> · MOD: D/V              |  ADAY: yok — <gerekçe>
   Betik `--film` ile koşunca bölümü arar; yoksa NOT basar (eski kayıtlar
   kırılmaz). Örüntüyü tek koşudan değil `ders_frekans.py --ozet` tablosundan
   (sayaç 🔁) oku; ≥ 2 filmde tekrarlayan aday ders olur (Kart G).

   ⭐ ⑦ ORTAK DEFTER KAPISI [D110 · 07.09.2026] — künyesi (kesme · sahne ·
   şerit) BİREBİR aynı olan ve çoğunluktan sapan mercek grubu işaretlenir:
   *azınlık İKİ oy değil, BİR oydur.* Aynı oturumda arka arkaya koşulan iki
   mercek tek ölçümün iki kılıfı olabilir. Doğrulama: kesme ZAMAN KODLARI
   basılmış mı? Basılmamışsa sayım yapılmamış, devralınmıştır.

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
   ⭐ ALTINCI SATIR: SÜRE [Ders 205]. Raporların `RUNTIME` satırları yan yana yazılır;
     referans ölçüm (`--olcum-sure`), yoksa ORTANCA; tolerans max(5 s · %10). Sapan
     merceğin ZAMAN EKSENİ uydurmadır: zaman kodu, DROP-OFF saniyesi, sahne aralığı o
     rapordan alınmaz (bir partide ⑩ 60 s, ⑫ 25 s, on mercek 124 s yazdı; kapı ✅ vermişti).
     → BETİK: rapor_kontrol.py birden çok rapor verilince altı satırı da basar;
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
   ⭐ ALTINCI SATIR — SINIR SORULUR, YALNIZ DÜŞÜRÜLMEZ [Ders 183].
      Bir bulgu SPEC'in NOVUM'u yüzünden düştüyse kapı BİTMEDİ: NOVUM bloğu
      kuralın nerede BİTTİĞİNİ de yazar (SPEC'te `⛔` ile başlayan cümle).
      O cümle KAREYLE sınanmadan ⑩ kapanmaz:
        | novum sınır cümlesi (SPEC) | sınandığı saniye | tutuyor mu |
      Sebep: THE KEPT LIGHT'ta ⑥'nın "TWO GRAVITIES" hükmü haklı olarak
      düştü — ve düşerken altındaki GERÇEK ihlali de götürdü: SPEC "kapağın
      ÜSTÜNDE bırakılan alet güverteye ÇARPAR" diyordu, ekranda bırakılan
      kesici üç saniye havada kalıp güverteye hiç çarpmadan ağza kayıyordu.
      Sekiz merceğin hiçbiri yazmadı; ⑥ en yakınına geldi ve yönü ters yazdı.
      → BETİK: rapor_kontrol.py ①.7 sınır cümlesini basar, elle aranmaz.

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
     ffmpeg -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG:\
       file=yavg.txt" -f null -                            → IŞIK TAKVİMİ İZİ [Ders 193]
       ⛔ Işık takvimi olan filmde ZORUNLU: sahne başına YAVG (ort · min · son 2 s).
          ↑ sahne, önceki en karanlık sahneden %20+ parlaksa TAKVİM GERİ SARDI ·
          ⟳ sahnenin SONU kendi en karanlık anından %25+ parlaksa KLİP İÇİNDE
          geri yandı. Takvim monotonikse (şerit n→…→0) her işaret 🔴'dir.
     ffmpeg -i "$M" -vf "crop=360:240:iw-360:ih-240,fps=1/30,tile=6x2" \
       -frames:v 1 kose_SA.png                              → KÖŞE TESTİ (filigran)
     ffmpeg -i "$M" -vf "freezedetect=n=-60dB:d=1.5" -an -f null - 2>&1 \
       | grep -oE "freeze_(start|end): [0-9.]+"           → KUYRUK/BAŞ KART ŞÜPHESİ
       + son_kare.jpg (son 1 s)                            [D70/D72 · 9 vaka · 01.09.2026]
     ⭐ Hepsi tek koşuda: bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>
       ⛔ BETİK SONA "TESLİM SINIFI" SATIRI BASAR [Ders 181]: LUFS sapması
          > 3 LU · kuyrukta ≥1,5 s donma → 🚨 HAM ZİNCİR. Filigran ve klip
          sayısı GÖZLE/SPEC'le kapanır. HAM ZİNCİR çıkarsa MERCEK KOŞULMAZ,
          rapor OKUNMAZ, satır YAZILMAZ — sıra: KURGU → ÖLÇÜM → MERCEK.
          Sebep: iki filmde de teslim edilen dosya kurgu değil, üreticinin
          ham zinciri + bir kart'tı; sekiz mercek onu "film" sanıp puanladı.
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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/1_KARE_QA_CRITIQUE_PROMPT.md` · girdi: video (+ SPEC)
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.

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

1. HAM RAPORU KAYDET       02_HAM_RAPORLAR/<FILM>/<FILM>_KARE_HAM.md
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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/4_HIKAYE_QA_CRITIQUE_PROMPT.md` · girdi: video (+ PLAN)
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.

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

1. 02_HAM_RAPORLAR/<FILM>/<FILM>_HIKAYE_HAM.md       ham çıktı
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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video**
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.

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

1. 02_HAM_RAPORLAR/<FILM>/<FILM>_DEVAMLILIK_HAM.md   ham çıktı
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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/3_SES_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video**
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.
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

1. 02_HAM_RAPORLAR/<FILM>/<FILM>_SES_HAM.md          ham çıktı

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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video (tam kurgu)**
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.
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
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_ARKA_PLAN_HAM.md
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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/6_FIZIK_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.
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
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_FIZIK_HAM.md
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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/7_AKSIYON_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.
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
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_AKSIYON_HAM.md
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

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/8_EFOR_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır. Yapıştırılmazsa koşu mod V'dir ve T tablosuna satır
yazılmaz. ⚠️ Filme özel paket 11.09.2026'da kaldırıldı — mod D'nin taşıyıcısı
artık BETİK değil, operatörün SPEC'i yapıştırmasıdır.
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
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_EFOR_HAM.md
3. ⑥ İLE ÇAPRAZ OKU       ⑥ FİZİK aynı filme koşulduysa: ⑥'nın
   biyomekanik kategorisi ile ⑧'in 1/4/6 kategorileri yan yana yazılır.
   ⑥ PASS + ⑧ FAIL normaldir ve merceğin varlık sebebidir
   ("sayısal olarak mümkün, ama beden ödemedi") — çelişki DEĞİLDİR.
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 💪 EFOR bölümü
5. SKOR SATIRI            FILM_QA_RAPORLARI/T8_EFOR_KALITE.md
```

## 🎯 F5 — ⑨ KADRAJ RAPORU GELDİ (plan sadakati · koşul tetikli)

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/9_KADRAJ_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır (filme özel paket 11.09.2026'da kaldırıldı).
(+ SPEC B bloğu + C'den EŞ KADRAJ · EKRAN YÖNÜ = **MOD D** · mod V koşusu tanım gereği BOŞ)
*(06.09.2026'da açıldı [D184] — /4 paydasına girmez. Koşul: SPEC'te KURULUM İSKELETİ satırı.)*

```
⛔ KARE-ÖNCE KAPISI: SETUP LEDGER'ın her satırında gözlenen boyut/açı/konum
   YAZILI mı, yoksa yalnız harf mi? Yalnız harf yazan ledger planı kopyalamıştır.
   SETUP STRING plan iskeletiyle birebirse rapor_kontrol.py NOT basar — üç
   sahne seç, kareyi çıkar, harfi kendin ata, karşılaştır.

⛔ KAFİYE KAPISI: RHYME PAIR satırı her koşuda okunur. PAIR FAILS ise hüküm
   RHYME BROKEN'dır ve son sahne yeniden üretim listesinin BAŞINA yazılır —
   kurguda düzelmez, kamera post'ta taşınmaz.

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_KADRAJ_HAM.md
3. SETUP STRING DOĞRULA   uzunluk = kesme + 1; plan iskeletiyle FARK listesini
   rapor_kontrol.py basar — elle kıyaslama yok; her fark ⑪ tek kareyle KAPANIR
   (FİLM SAPTI / RAPOR UYDURDU), kapanmadan skor satırı yazılmaz
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🎯 KADRAJ bölümü
   ⭐ BULGU SAHİPLİĞİ: kameranın KONUMU ⑨'un · karenin İÇİ ①'in ·
      ışığı ⑪'in · arkası ⑤'in · nesnelerin aynılığı ②'nin
5. SKOR SATIRI            FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md
6. MISS sahne → ÜRETİM notu: prompt CAMERA satırı DOĞRUYSA (çoğu vakada öyle —
   Kept Light S24'te S0 ile birebir aynıydı) yama prompta değil, yeniden
   üretime yazılır; depo kurguyu üstlenmez
```

## 🎭 F6 — ⑩ OYUNCULUK RAPORU GELDİ (plan sadakati · koşul tetikli)

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/10_OYUNCULUK_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır (filme özel paket 11.09.2026'da kaldırıldı).
(+ SPEC A bloğu + C'den İNSAN · KASK · EKRAN YÖNÜ = **MOD D** · mod V koşusu tanım gereği BOŞ)
*(06.09.2026'da açıldı [D184] — /4 paydasına girmez. Koşul: replik 0 ya da SPEC'te CENTRAL CHOICE.)*

```
⛔ KANAL KAPISI: CHANNEL REGISTER'da yüz "unavailable" ise kategori 1 N/A
   olmalı; 1/10 yazan rapor kask kapalı filmi yüz göstermediği için
   cezalandırmıştır — o puan geri verilir, ortalama yeniden hesaplanır.

⛔ CÜMLE KAPISI: PERFORMANCE LEDGER'daki cümleler SPEC'in sahne haritasıyla
   birebir örtüşüyorsa rapor planı okuyup ekrana yansıtmıştır — bir çapa vuruş
   seç (SEÇİM · BEDEL · FİNAL), öncesi/sonrası karesini kendin çıkar, farkı
   kendin yaz. "Hiçbir şey" ise raporun LEGIBLE'ı düşer.

⛔ SINIR: ⑧ bedeni ÖDEDİ mi, ⑩ bedeni NİYET etti mi. Aynı sahne ikisinde de
   düşebilir; çifte fatura değil, iki eksen.

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_OYUNCULUK_HAM.md
3. GAZE STRING DOĞRULA    uzunluk = kesme + 1 (rapor_kontrol.py basar);
   dizinin U/D'si SPEC EKRAN YÖNÜ'yle okunur — "yukarı bakıyor" dediği yerde
   plan yukarıyı kaya tavanı yapmışsa bulgu, yapmamışsa uydurma
4. ④ İLE ÇAPRAZ OKU       ④ HİKAYE "doruk yok / bedel yok" yazdıysa ⑩'un
   SEÇİM ve BEDEL satırları yanına konur: ⑩ "bedende var" + ④ "sayfada yok"
   = ④'ün harita hatası (Kept Light: 25 sahne 7 blok) · ⑩ "bedende yok" +
   ④ "sayfada var" = ÜRETİM hatası, regen
5. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🎭 OYUNCULUK bölümü
6. SKOR SATIRI            FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md
```

## 💡 F7 — ⑪ IŞIK RAPORU GELDİ (plan sadakati · koşul tetikli)

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/11_ISIK_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır (filme özel paket 11.09.2026'da kaldırıldı).
(+ SPEC C'den IŞIK TAKVİMİ · ATMOSFER · YAPI ANATOMİSİ · KASK + ızgara = **MOD D**)
*(06.09.2026'da açıldı [D184] — /4 paydasına girmez. Koşul: SPEC'te IŞIK TAKVİMİ ya da ≥12 klip.)*

```
⛔ ORTAM KAPISI: ZONE REGISTER "medium: vacuum" yazıp pus/bloom/kaldırılmış
   gölgeyi bulgu YAPMAMIŞSA rapor kendi yasasını okumamıştır — kategori 8
   şartlı. Tersi: vakumda sert siyah gölgeyi "harsh lighting" diye düşüren
   rapor filmin kuralını kusur saymıştır → ⑩ ÖNERME KAPISI, puan geri verilir.

⛔ SINIR KAPISI: LIGHT JUMP LOG'daki her satır SPEC'in "değişim SINIRDA olur"
   listesine karşı okunur; planlı sınırdaki değişim PASS'tır, rapor 🔴 yazdıysa
   düşer. Planlı sınır DIŞINDAKİ her sıçrama kareyle kapanır (komşu çift).

⛔ GRADE / REGEN AYRIMI: ısı · pozlama · doygunluk → kurgu masası (grade);
   yön · dolgu · sönük lamba · klip içi dimmer · vakumda pus → yeniden üretim.
   Rapor "fixable in the grade" dediyse hangi sütunda olduğuna BAK.

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_ISIK_HAM.md
3. KEY DIRECTION STRING DOĞRULA  uzunluk = kesme + 1 (rapor_kontrol.py basar);
   bölge içinde değişen her hane LIGHT JUMP LOG'da satır ister
4. ⑤ İLE ÇAPRAZ OKU       lambanın VARLIĞI ⑤/②'nin, YANIP yanmadığı ⑪'in —
   Kept Light S4 lamba montajı ⑤'in bulgusudur, S4'ün ışık YÖNÜ ⑪'in
5. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 💡 IŞIK bölümü
6. SKOR SATIRI            FILM_QA_RAPORLARI/T11_ISIK_KALITE.md
```

## 🪝 F8 — ⑫ HOOK RAPORU GELDİ (plan sadakati · yayın öncesi)

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/12_HOOK_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
⛔ **RUBRİK TEK BAŞINA YAPIŞTIRILMAZ** [D129]: `<FILM>_QA_SPEC.md` AYNI mesajda,
rubriğin BAŞINA yapıştırılır (filme özel paket 11.09.2026'da kaldırıldı).
(+ SPEC A + B blokları + KAPAK ANI = **MOD D**)
*(06.09.2026'da açıldı [D184] — /4 paydasına girmez. Koşul: film yayınlanacak (kart Y); yayından ÖNCE koşulur.)*

```
⛔ KESME KAPISI: bu mercek KESME ÖNERMEZ. Rapor "cut S-n" yazdıysa o satır
   düşer — ④'ün kesme listesi de ⑩ ÖNERME KAPISI'ndan geçmeden uygulanmıyor;
   ⑫'nin işi saniye söylemek, sahne kesmek değil.

⛔ TAHMİN KAPISI: DROP-OFF PREDICTION üç saniye + sabit listeden sebep
   (rapor_kontrol.py sayar). Aralık, "civarı", "muhtemelen" → ŞARTLI; tahmin
   yayın tablosuna girmez, kıyaslanamaz.

⛔ KART KAPISI: kuyruk kartı varsa ⑫'nin "Exit & Return" 🔴'sı ÖLÇÜMÜN
   bulgusudur (freezedetect + son_kare.jpg) — raporun keşfi değil; kart
   kesildikten sonra ⑫ yeniden koşulur, çünkü çıkış penceresi değişmiştir.

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_HOOK_HAM.md
3. TAHMİNİ KOPYALA        DROP-OFF PREDICTION bloğu OLDUĞU GİBİ →
   08_YAYIN_PERFORMANS_TABLOSU.md "⑫ tahmin" sütunu — yayından ÖNCE.
   Yayından SONRA kart Y gerçek eğrinin üç düşüş saniyesini yanına yazar;
   |Δ| ≤ 10 s tutan tahmin, ötesi tutmayan. Bu depoda aleti izleyiciye karşı
   kalibre eden TEK satır budur (08 tablosu bugüne kadar 0 satır).
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🪝 HOOK bölümü
5. SKOR SATIRI            FILM_QA_RAPORLARI/T12_HOOK_KALITE.md
```

## 🧩 F9 — ⑬ UYUM RAPORU GELDİ (üretim sadakati · sahne ↔ prompt)

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/13_UYUM_QA_CRITIQUE_PROMPT.md` · girdi: kurgu +
**sahne promptları (birebir)** + `<FILM>_QA_SPEC.md` + `sahne_kapisi.sh` çıktısı +
üretim defteri satırları — DÖRDÜ DE zorunlu.
*(11.09.2026'da açıldı — /4 paydasına girmez. Koşul: film üretildi ve defteri dolu.)*

```
⛔ MOD V YOKTUR: bu mercek promptu ekrana karşı okur. Prompt metni girdinin
   KENDİSİDİR; olmadan koşu "eksik" değil KOŞU DEĞİLDİR. rapor_kontrol.py ①.11
   bunu GEÇERSİZ yazar ve T13'e satır girmez.

⛔ IZGARA KAPISI ÖNCE: sahne_kapisi.sh'in saydığı sahne ≠ prompt sayısı ise
   rapor TEK bulgu yazar (DELIVERY MISMATCH) ve durur. Plana karşı okunan
   yanlış makara, her bulgusu çöp olan bir koşudur [D188].

⛔ ALINTI KAPISI: her bulgu ya promptun cümlesini alıntılar (🅐 model sapması)
   ya da promptun bunun yerine ne dediğini yazar (🅑 prompt boşluğu).
   Alıntısız satır düşer — betik sayar (①.12).

⭐ BU MERCEĞİN ÜRÜNÜ DERSTİR, ONARIM SİPARİŞİ DEĞİL:
   ⛔ ÖLÇÜLEN FİLMİN PROMPTU ASLA GÜNCELLENMEZ. Üretilmiş filmin promptu
     kanıttır; değiştirilirse hangi metnin hangi kareyi ürettiği kaybolur.
   🅑 bulguları LESSON ORDERS tablosuna düşer ve oradan kart G'ye gider:
     ders → kapı (BETİK / LİSTE / KARAR / ARŞİV) → SIRADAKİ filmin yazımı.
   Kilit cümlesi film adı ve sahne numarası TAŞIMAZ (betik ①.13 denetler):
   onu okuyacak kişi bu filmi hiç görmedi.

1. ORTAK ADIMLAR ①-⑩ koşulur
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_UYUM_HAM.md
3. ATIF ORANINI OKU        🅐 çok → motor; 🅑 çok → yazım standardı.
   Bu oran kesme listesi değil, YÖN kararıdır: aynı promptla yeniden üretmek
   🅑 vakasında parayı iki kez yakar.
4. DERS SİPARİŞLERİNİ TAŞI  her 🅑 satırı → kart G (ders) ya da gerekçeli ARŞİV.
   Ders KAPI satırı **"ölçen mercek: ⑬"** ibaresini taşır [D187'nin panzehiri].
5. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🧩 UYUM bölümü
6. SKOR SATIRI            FILM_QA_RAPORLARI/T13_UYUM_KALITE.md
   (birincil sayı: LOCKS HELD / LOCKS CHECKED · skor ondan türetilir)
```

## 🧍 F10 — ⑭ HAREKET RAPORU GELDİ (hareket mantığı · risk tetikli tarama)

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/14_HAREKET_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
(+ SPEC A ve C blokları = **MOD D**; mod V meşru, SPEC varken ⛔ ÖN KOŞU [D129])
*(14.09.2026'da açıldı — sahip talebi: "saçma sapan hareketler". /4 paydasına girmez.)*

```
⛔ AMAÇ CÜMLESİ KAPISI: MOTION LEDGER'da etiketi PURPOSEFUL olmayan her satırın
   denenmiş bir amaç cümlesi var mı ("… için" / "— bilmiyorum, orada bir şey yok")?
   Cümlesiz etiket bulgu değildir; satır düşer.
⛔ PREMISE KAPISI: sıfır-g / dönme yerçekimi / sert giysi filminde PREMISE REGISTER
   dolu değilse SPIN ve PUPPET etiketleri şüphelidir — fizik kuralına uyan dönüş
   hareket hatası değildir. rapor_kontrol NOVUM kapısı (⑥⑦⑧ ile aynı).
⛔ ⑭ ⑦ DEĞİLDİR: "olay okunmadı" ⑦'nin, "kol neden kalktı" ⑭'ün. Aynı dönüş iki
   bulgu üretebilir; her mercek kendi türünü yazar. "Yanlış yöne döndü" ⑮'indir.

1. ORTAK ADIMLAR ①-⑩ koşulur (①.5 betik: PURPOSE STRING = kesme+1 · MOVEMENTS
   LOGGED ≥ PURPOSELESS · VERDICT sözlükte)
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_HAREKET_HAM.md
3. PROMPT ORDERS'I TAŞI   tablodaki her satır → kart G'nin ham maddesi: aynı etiket
   (SPIN · LOOP · PHANTOM …) ikinci filmde görülünce ders yazılır (kontrat §2b
   FREKANS ≥ 2). Tek filmde → GOZLEM_DEFTERI ADAY (MOD etiketiyle).
   ders_frekans.py ⑭ etiketlerini "⬜ ⑭ hareket mantığı — ders yok" satırında sayar.
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🧍 HAREKET bölümü
   ⭐ BULGU SAHİPLİĞİ: tek karede anatomi → ① · sayı → ⑥ · okunurluk → ⑦ ·
      niyet → ⑩ · vektör → ⑮. ⑭ yalnız AMACIN sahibidir.
5. SKOR SATIRI            FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md (betik yazar)
```

## 🧭 F11 — ⑮ YÖN RAPORU GELDİ (yön ve hedef · risk tetikli tarama)

**Rubrik:** `QA_PROMPTLARI/_KAYNAK/15_YON_QA_CRITIQUE_PROMPT.md` · girdi: tam kurgu
(+ SPEC C bloğu ekran yönü kilitleri + A bloğu = **MOD D**; mod V meşru: hedefin yeri
filmin KENDİ kurduğu yerdir; SPEC varken ⛔ ÖN KOŞU [D129])
*(14.09.2026'da açıldı — sahip talebi: "yanlış yere dönmek, ateş etmek". /4 paydasına girmez.)*

```
⛔ VEKTÖR CÜMLESİ KAPISI: her MISS satırı hedefin EKRANDA KURULDUĞU zaman kodunu
   taşır mı ("kapak 0:01'de ekran-sağda")? Kuruluş kodu yoksa eşleşme MISS değil
   UNKNOWN'dır; bulgu düşer, FLAGS'e iner.
⛔ EKRAN UZAYI KAPISI: rapor ve PROMPT ORDERS satırları screen-left/right ile
   yazılır; "kuzeye", "onun soluna" yazan satır düşer — prompt da kullanamaz
   (UZAMSAL_HARITA §4).
⛔ PREMISE KAPISI: dönme yerçekimi / yansıma / bilinçli çizgi geçişi PREMISE
   REGISTER'da yoksa FLIP bulgusu şüphelidir.
⛔ ⑮ ② DEĞİLDİR: "kapak taraf değiştirdi" ②'nin (aynılık), "kapağa ters döndü"
   ⑮'in (vektör). İkisi de yazılabilir, sahipleri ayrı.

1. ORTAK ADIMLAR ①-⑩ koşulur (①.5 betik: VECTOR STRING = kesme+1 · ACTS MISSED
   beşlisi = ACTS LOGGED · VERDICT sözlükte)
2. HAM RAPORU KAYDET      02_HAM_RAPORLAR/<FILM>/<FILM>_YON_HAM.md
3. PROMPT ORDERS'I TAŞI   her satır → kart G ham maddesi; aynı desen (FLIP · TURNED
   BACK · SHOT INTO SPACE …) ikinci filmde → ders (kontrat §2b). Tek filmde → ADAY.
   ders_frekans.py ⑮ desenlerini "⬜ ⑮ yön/hedef — ders yok" satırında sayar.
4. FİLM KAYDINI GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md · 🧭 YÖN bölümü
   ⭐ BULGU SAHİPLİĞİ: aynılık → ② · okunurluk → ⑦ · amaç → ⑭ · niyet → ⑩ ·
      kameranın vektörü → ⑨ · yörünge sayısı → ⑥. ⑮ yalnız FİGÜRÜN VEKTÖRÜNÜN sahibidir.
5. SKOR SATIRI            FILM_QA_RAPORLARI/T15_YON_KALITE.md (betik yazar)
```

## 📚 G — YENİ DERS ÇIKTI

```
0. ⭐ 14.09.2026 REFORM [DERSLER/00_DERS_YAZIM_KONTRATI.md §2b · §4]:
   FİLM DERSİ (01-07) = ≥ 2 FİLMDE GÖRÜLEN ÖRÜNTÜ + SONRAKİ FİLMDE DEĞİŞEN TEK SATIR.
   Başlığın HEMEN altına dört satır (Kaynak'tan önce — tek gelenek):
     **FREKANS:** n film · FILM (mod · mercek) · …   ← ≥ 2, yoksa ADAY
     **DEĞİŞEN SATIR:** PLAN sütunu | prompt satırı | liste maddesi | SPEC satırı
     **KAPI:** LİSTE yeter (BETİK varsa yaz)  ·  **TEKRAR:** 0
   Tek vaka → DERSLER/GOZLEM_DEFTERI.md (ADAY-n, **MOD:** D/V etiketiyle), numara ALMAZ;
   ≥ 2 filmde tekrarlayınca koşu modundan bağımsız ders olur. UNATTRIBUTED rapor:
   ne ders ne aday. Ders → 00_YASAYAN_DERSLER.md'ye girer; liste 40'ı aşarsa biri
   çıkar (GİRİŞ/ÇIKIŞ defteri, gerekçeli). Örüntüyü tek koşudan değil
   `RAPOR_KONTROL/ders_frekans.py --ozet` tablosundan (sayaç 🔁) oku.
   ALET DERSİ (08/09): 01.09.2026 kuralı sürer — ⛔ KAPI SATIRI OLMAYAN DERS YAZILMAZ.
   Dört kader: BETİK · LİSTE · KARAR · ARŞİV — "prompt cümlesi" kader değildir.
   Vaka ≥ 3 → ⛔ ÇALIŞMIYOR + dönüştürme borcu (cümleden karara/araca).
   Alet dersi yeni-film'in okuma listesine GİRMEZ. Sayı: sayac.sh 📚 (film/alet ayrı) + 🧭.

1. Dersi İKİ yere işle (07.08.2026'dan beri dersler klasörde):
   a) DERSLER/ içindeki uygun TEMATİK dosyanın sonuna ekle
      (kamera/karakter/fizik/ışık/ekipman/metin/kurgu/QA/sistem —
      hangisi olduğuna LESSONS_LEARNED.md'deki dosya tablosundan karar ver)
      ⛔ Başka bir dersin İÇİNE değil, dosyanın SONUNA — D198/D200 13.09'da D192'nin
         gövdesine girdi ve D192'nin kuyruğu yetim kaldı (14.09'da düzeltildi).
      ## 🔴/🟡 DERS <n>: BAŞLIK
      **FREKANS:** · **DEĞİŞEN SATIR:** · **KAPI:** · **TEKRAR:** 0   ← film dersi, 14.09.2026
      (alet dersi: **KAPI:** · **TEKRAR:** 0)
      **Kaynak:** ilk vaka — hangi film, hangi skor
      **Örüntü/Sorun:** hangi filmlerde, ortak sebep
      **ÇÖZÜM:** karar / araç / liste maddesi (prompt cümlesi yalnız betik ölçüyorsa)
   b) LESSONS_LEARNED.md · DERS DİZİNİ tablosuna satır ekle
      numara dizindeki EN YÜKSEK numaradan devam eder — tematik dosyanın
      içindeki son numaraya BAKMA, numaralar dosyalara dağınık
   c) Film dersiyse 00_YASAYAN_DERSLER.md tablosuna satır (≤ 40; taşarsa biri çıkar)

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
   ⛔ 14.09.2026 RUBRİK DİYETİ: yama yalnız ÖLÇÜLEBİLİR TEK SATIR kontrol maddesidir
      (kategori listesine bir kutu); paragraf, örnek, anekdot girmez. Rubrik 25 KB
      tavanını aşacaksa yama rubriğe değil çıktı kapısına (rapor_kontrol.py) gider.
      Sayı: sayac.sh 🧭 "rubrik hacmi".
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
⛔ SİLME BAŞLAMADAN ÖNCE — bu üçü koşulmadan tek dosya silinmez
   (kural ② üç kez atlandı: 26.08 üç zombi filmi, 05.09 üç içerik daha;
    ikincisinde arşiv de yoktu, kayıp KALICI — beşinci tur)

 □ git ls-files <klasör> | wc -l              → 0 ise DUR, hiçbir şey git'te yok
 □ git status --porcelain <klasör> | grep '^??'  → listelenen her satır
      GERİ ALINAMAZ. Sahibe SÖYLE, varsayma. Değerliyse depo dışına arşiv:
      tar czf ~/film_md_<KLASOR>_ARSIV_<tarih>.tar.gz <klasör>
 □ klasörün içinde FİLM DIŞI ne varsa listele ve her birine depo çapında
      grep at (kural ③). Dışarıdan atıf alan dosya SİLİNMEZ, TAŞINIR —
      hedef kilavuzlar_ve_sistem_dosyalari/ altıdır, format-bağımsız olur.
      ⚠️ Sayıma girmeyen bir klasör, sayıma giren filmlerin GEREKÇESİNİ
         tutabilir (05.09: iki canlı filmin ders kaynağı oradaydı).

SONRA — bir klasör silinince AYNI noktalar güncellenir

 □ AGENTS.md §1 haritasından satırı sil
 □ YAPI_GRAFI.md → karar ağacındaki dal + klasör ağacındaki satır
 □ sayac.sh içindeki klasör listelerinden çıkar
      ⚠️ TEK liste değil: 05.09'da dört ayrı listede geçiyordu (grep -n ile
         hepsini bul, biri kalırsa betik olmayan klasörü saymaya devam eder)
 □ FILM_QA_RAPORLARI/00_INDEX.md → o klasörün bölümü/satırları kaldırılır
      + SAYIM defterine tarihli −n kaydı (kural ①: sayı tek yerde durur)
 □ Silinen filmin TÜREVLERİ: 01_FILM_RAPORLARI, 02_HAM_RAPORLAR,
      T tablosu satırları
      ⚠️ ÖLÇÜLMÜŞ rapor SİLİNMEZ (⏸️ METODOLOJİ kaydına çevrilir);
         hiç koşulmamış paket öksüz kalır, sahibe sorulur
 □ KILAVUZ_REHBERI.md → tür/format kartı SİLİNMEZ, başına ⏸️ RAFTA yazılır
      (kılavuz bilgisi ucuz, yeniden yazmak pahalı)
      ⚠️ İstisna: sahip "iz bırakma" derse kart hiç girmez — bu KARARDIR,
         sorulur (kural ④). 05.09'da dikey 20-25 bandı böyle kapandı.
 □ bash sayac.sh → toplam, 00_INDEX ile tutuyor mu
 □ ölü adres süpürmesi: grep -rn "<klasör adı>" — kalan her isabet ya
      tarihli kaldırma notudur ya da ölü adrestir; üçüncü ihtimal yok
 □ commit (tip: bakim)
```

> ⭐ **GERİ AÇILIŞ EMSALİ (23.08.2026):** `yatay_2_4_dk_filmler_zombi/`
> H2 ile silinmiş bir klasördü ve H ile geri açıldı. Geri açarken aynı
> dört nokta TERS yönde güncellenir + bir beşincisi eklenir: kılavuzun
> ⏸️ RAFTA satırı kaldırılır ve yerine **açılış şartı** yazılır. Bu
> depoda o şart bir bütçedir (KILAVUZ_REHBERI §4.2'nin altı satırı) —
> klasörü geri açmak, türü bedava geri getirmez.
>
> ⭐ **DÖRDÜNCÜ TUR — FORMAT BİRLEŞMESİ (04.09.2026):** `yatay_7_9_dk_filmler/`
> sahip kararıyla kaldırıldı; tek filmi `yatay_10_20_dk_filmler/`'e taşındı ve
> o kartın bandı 10 dk'dan 7 dk'ya açıldı. Bu tur kartın ÜÇÜNCÜ eksiğini
> gösterdi:
>
> ```
> ③ FORMAT KLASÖRÜ DEPO ÇAPINDA KILAVUZ TAŞIYABİLİR.
>    yatay_7_9_dk_filmler/kilavuzlar/ yalnız kendi formatına ait DEĞİLDİ:
>    start/end zinciri, faz şablonu, 5 faz mimarisi ve 3 geçişli QA sistemi
>    10-20 dk kartından, POLITIKA'dan, TEK_CEKIM'den, YAPI_GRAFI'ndan ve
>    FILM_QA_RAPORLARI'ndan adresleniyordu. Klasörle birlikte silinseydi
>    CANLI bir hat üretim tekniğini kaybederdi.
>    ⛔ H2 koşulmadan ÖNCE: klasörün içinde film DIŞI ne varsa listele ve
>       her birine grep at. Dışarıdan atıf alan her dosya SİLİNMEZ, TAŞINIR.
>       (Bu turda dördü merkeze taşındı ve format-bağımsız oldu.)
> ④ BANDIN ADRESİ DE BİR ATIFTIR. Kaldırılan format bir SÜRE BANDIydı ve
>    komşu kart "10 dk'nın altı şu klasöre aittir" diyordu. Klasör gidince
>    o cümle boşluğa bakar. Bandın nereye gittiği KARARDIR — sahibe sorulur,
>    varsayılmaz.
> ```
>
> ⭐ **BEŞİNCİ TUR — İKİ KLASÖR BİRDEN (05.09.2026):** `film_analizleri/`
> (dış film analiz hattı) ve `dikey_20_25_dk_filmler/` (açıldığı gün kapanan
> dikey 20-25 dk bandı) sahip kararıyla kaldırıldı. Bu tur kartın DÖRDÜNCÜ
> eksiğini gösterdi ve ikinci kuralının ÜÇÜNCÜ ihlalini kaydetti:
>
> ```
> ⑤ ⛔ KURAL ② YAZILI OLMAK YETMİYOR — ÜÇÜNCÜ KEZ İHLAL EDİLDİ.
>    "SİLMEDEN ÖNCE git ls-files" 26.08.2026'da yazıldı, çünkü üç zombi
>    filmi izlenmiyordu ve arşiv alınmıştı. 05.09.2026'da AYNI ŞEY üç
>    içerikte tekrar oldu, bu kez arşiv YOK:
>      · dikey_20_25_dk_filmler/THE_OWED_AIR/ — bandın tek filmi. 05.09'da
>        yazıldı, 05.09'da gitti; hiç commit edilmedi.
>      · film_analizleri/…/CORAK_TOPRAKLAR_HAREMININ_HUKUMDARIYIM/ — 16 rapor,
>        THE OWED AIR'in "dört vuruşlu sistem çevrimi" motorunun ÖLÇÜM kaynağı.
>      · film_analizleri/ANALIZ_QA_PROMPTLARI/DIKEY_4_PARCA/ — 4 parça × tek
>        kapsamlı prompt paketi.
>    ⛔ Kural bir CÜMLE olarak çalışmıyor. Kaldırma kararı DUYULUR DUYULMAZ,
>       tek bir şey daha silinmeden önce:
>          git ls-files <klasör> | wc -l     # 0 çıkarsa DUR
>          git status --porcelain <klasör> | grep '^??'   # bunlar geri gelmez
>       Çıktı sıfırdan farklıysa depo dışına tar alınır (26.08 emsali:
>       film_md_ZOMBI_ARSIV_2026-08-26.tar.gz). Sahip "sil" dediğinde
>       silinecek şeyin GERİ ALINABİLİR Mİ olduğu sahibin değil, ajanın
>       söylemesi gereken şeydir.
> ⑥ ANALİZ HATTI DA "FİLM DIŞI" TAŞIR — ama kurtarma gerekçesi İKİ AYRI
>    kuraldır; karıştırılırsa depoya yanlış kayıt düşer:
>      · NOBODY_WAS_ALIVE ders seçkisi → kural ③ (DIŞARIDAN ATIF ALIYORDU:
>        THE_LAST_SHIFT + THE_HOLLOW_COUNT §0.19 tablolarının kaynağı).
>        Sayıma girmeyen bir klasör, sayıma giren filmlerin GEREKÇESİNİ tutar.
>      · dört analiz promptu → kural ③ DEĞİL. HEAD'de depoda hiçbir yerden
>        atıf ALMIYORLARDI (git grep ile doğrulandı). Kurtarılma sebepleri
>        H2'nin kılavuz maddesindeki gerekçe: "bilgi ucuz, yeniden yazmak
>        pahalı" — üç mercekli hattın tek yazılmış metodolojisiydiler.
>    ⛔ Ders: "atıf alıyordu" gerekçesi YAZILMADAN ÖNCE grep'le kanıtlanır.
>       Bu turda ikisi tek cümlede birleştirildi, denetimde yanlış çıktı ve
>       düzeltildi — kaydın kendisi de bir kurala tabidir.
> ```
>
> ⭐ **ALTINCI TUR — YENİDEN ADLANDIRMA (13.09.2026):** iki format klasörü
> silinmedi, ADI DEĞİŞTİ: `yatay_2_4_dk_filmler_uzay/` → `yatay_2_dk_filmler/`
> ve `yatay_3_5_dk_filmler/` → `yatay_4_dk_filmler/` (sahip kararı · 12-sahne
> modül merdiveni 2 · 4 · 6 · 8). Kart bugüne kadar "yeniden adlandırma ~40
> adres kırar" diyordu; ölçüm **269 adres / 185 dosya** çıktı. Tarif:
>
> ```
> ① git mv <eski> <yeni>         — izlenmeyen film klasörleri de taşınır
>                                  (dizin FS'de yeniden adlanır); ⛔ önce
>                                  `git status --porcelain <eski>`'de " D"
>                                  satırı olmadığına bak, yoksa git mv düşer
> ② tam süpürme, tek geçiş:       .md · .sh · .py — bütün depo, .git hariç
>      grep -rn "<eski ad>" . --exclude-dir=.git  → sıfır olana kadar
>    ⛔ komşu eski adlar (yatay_2_4_dk_filmler_zombi/_savas) tarihli kaldırma
>       notlarıdır, DOKUNULMAZ; desen tam ad olmalı, önek değil
> ③ beş betik listesi + AGENTS §7 glob + film_klasoru_ac.sh case satırı
> ④ tarihli AD NOTU dört yere: AGENTS §1 · KILAVUZ_REHBERI kart başlığı ·
>    YAPI_GRAFI · klasör README — "belgelerdeki '2-4 dk' ifadesi aynı
>    formatın eski adıdır": yüzlerce tarihli kayıt o adı taşımaya devam
>    eder ve DEĞİŞTİRİLMEZ (kayıt tarihtir)
> ⑤ eski ad yalnız tarihli notlarda kalır; başka her isabet ölü adrestir
> ```
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
>    Filme özel rubriğin türden bağımsız yarısı da şablona damıtılmıştı:
>    QA_PROMPTLARI/FILME_OZEL/00_YANLIS_POZITIF_DUVARI_SABLONU.md
>    ⛔ 11.09.2026: şablon, FILME_OZEL klasörüyle birlikte SİLİNDİ (filme özel
>    rubrik yazılmıyor). Kayıt tarihtir; dosya git geçmişinde durur.
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
   ⭐ 14.09.2026: FAZ 4 (izleyici okuması) ve FAZ 5 (rubrik diyeti) oradan
   TODO_AKIS_VE_DERS_REFORMU.md'ye taşındı ve orada kapandı (FAZ 9 · FAZ 5).

🟡 REFORM KAYDI (14.09.2026): TODO_AKIS_VE_DERS_REFORMU.md — 10 fazın 10'u ✅,
   commit sahibin. Açık kalanlar: ① KELIME_BANDI image üst ucu (250) ilk yeni
   rejim filmde kalibre edilir (WS kurulum sahnesi sıkı yazımla 250-270'e
   geliyor) ② OKUMA_CEKIRDEGI manifesti ~10.500 satır (hedef 10.000) —
   KILAVUZ_REHBERI'nin yalnız ~1.200 satırı okunuyor ③ ders_frekans'ın
   dersleşmemiş üç örüntüsü: "Causality & Knowledge" (12 film) · "Motion
   Quality" (24) · "Focus Honesty" (5) — sahip kararı ④ ilk yeni rejim
   klasörü henüz açılmadı: ㉕-㉚ depoda etkisiz, scratch testinde doğrulandı.
   Bu satır dosya silinince silinir.

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
   QA_PROMPTLARI/_KAYNAK/ (4 mercek, 8-11 kategori) ve
   QA_PROMPTLARI/UC_GECISLI_QA/ (3 geçiş) ayrı sistemler.
   İki sistemden gelen skorlar aynı tabloda karşılaştırılamaz.
   ⚠️ 04.09.2026'da ikisi AYNI klasörün altına geldi (üç geçişli sistem
      kapanan yatay_7_9_dk_filmler/'den taşındı) — çatal KAPANMADI,
      yalnız GÖRÜNÜR oldu. Hangisinin koşulacağı hâlâ yazılı değil.

✅ araştırmalar/ açığı — KAPATILDI (26.08.2026, sahip kararı)
   Dokuz kılavuzun atıf verdiği araştırma dosyaları depoda ve git'te hiç
   olmadı; sahip 26.08.2026'da geri gelmeyeceklerine karar verdi ve klasör
   beklentisi haritadan kaldırıldı. Karar: kılavuzlar kaynak atfı olmadan
   KENDİ BAŞINA geçerli sayılır; gövdelerdeki "araştırmalar/N.md" satırları
   tarihsel etikettir, dosya beklentisi değil — silinmez, yeni atıf da
   yazılmaz. Kılavuz gövdesinin doğrulaması artık tek yoldan yapılır:
   gerçek yayın verisi (kart Y geri beslemesi → 01_DERS_ETKINLIK_RAPORU).
   (Kardeşi film_analizleri/ 22.08'de sessizce silinmişti, 25.08.2026'da
   `git checkout 15f3d3e^ -- film_analizleri` ile geri alınmıştı —
   05.09.2026'da sahip kararıyla bu kez BİLEREK kaldırıldı, kart H2 koşuldu.
   Kurtarılan metodoloji: kilavuzlar_ve_sistem_dosyalari/DIS_FILM_ANALIZI/)

⛔ 05.09.2026'DA ÜÇ İÇERİK GERİ ALINAMAZ BİÇİMDE GİTTİ — hepsi izlenmiyordu:
   dikey_20_25_dk_filmler/THE_OWED_AIR/ (film + QA_SPEC + kapak · 25 parça ×
   60 s planı, PART 01 yazılıydı) · film_analizleri/…/DIKEY_4_PARCA/ ·
   film_analizleri/ANALIZ_EDILEN_FILMLER/CORAK_TOPRAKLAR_HAREMININ_HUKUMDARIYIM/
   (16 rapor · 16:32 — THE OWED AIR'in motorunun ölçüm kaynağı).
   Üçü de hiçbir commit'te, çöp kutusunda ve arşivde yok. Kart H2 ②
   ("SİLMEDEN ÖNCE git ls-files") ÜÇÜNCÜ KEZ ihlal edildi — 26.08'de üç zombi
   filmi, 05.09'da bu üçü. Kural işlemiyor demek değil; kural KOŞULMUYOR.

🟡 KILAVUZ_REHBERI §8 film matrisi bayat — depodaki filmlerin çoğu listede yok.
🟡 dikey_shorts_filmler/ içinde 16:9 YATAY filmler var (klasör adı yanıltıyor).
```

---

# 7. DOĞRULAMA — iş bitince çalıştır

```bash
bash kilavuzlar_ve_sistem_dosyalari/sayac.sh   # sayılar tuttu mu, ders boşluğu var mı
                                                # 14.09: YAŞAYAN ≤ 40 · rubrik 6/6 ≤ 25 KB · 🔁 BULGU FREKANSI
git status                                      # her şey commit'lendi mi
# QA raporu işlendiyse — betik koşulmadan T tablosuna satır yazılmaz [D161]
# python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <ham raporlar> --film <film klasörü>
# ders yazıldıysa / ADAY açıldıysa — hangi örüntü kaç filmde tekrarlıyor, dersi var mı (14.09.2026)
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/ders_frekans.py --ozet
# yeni film klasörü açıldıysa — yeni rejim kapıları (㉕-㉚) klasör modunda koşar
# python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py <film klasörü>   # çıktıda "rejim:" satırı

# başlıksız (panelden düşecek) film dosyası var mı — çıktı boş olmalı
# (25.08.2026: her format klasörlü — glob bir kademe derinleşti)
for f in dikey_shorts_filmler/*/*.md yatay_2_dk_filmler/*/*.md yatay_4_dk_filmler/*/*.md \
         yatay_6_dk_filmler/*/*.md yatay_8_dk_filmler/*/*.md; do   # 13.09.2026: modül merdiveni, dört klasör
  [ -e "$f" ] || continue        # 6/8 dk klasörleri sıfır filmle açıldı — boş glob alarm değildir
  [ "$(grep -cE '^#' "$f")" -lt 3 ] && echo "BAŞLIKSIZ: $f"
done

```

---

# 8. AJANA SON SÖZ

```
Bu sistemin ölçülmüş gerçeği: kural eklemek kaliteyi artırmadı.
Kalite yükselten üç olayın üçü de kural değil, karar değişikliğiydi —
sabit lockoff kamera, sahneleri ayrı üretmek, tarif yerine sayısal kilit.

⭐ 14.09.2026 — DÖRDÜNCÜ KARAR: BÜTÇE. Ölçüldü: 126 dosyalık okuma
çizelgesinde 126/126 sahte kilit; 719 kelimelik image promptunun %57'si
tekrar; 205 dersin 91'i alet dersi, 93 aday kapısız; 17/17 kapı imzasıyla
yazılan film vana tamiri. Kapı ekledikçe film kapıya benzedi. Bu yüzden
tavan geldi: prompt 250/300 kelime (pozitif gövde) · NEGATIVE 11 cümle ·
okuma 40 ders + ≤30 dosya · kilit 20 · yaşayan ders 40 · rubrik 25 KB ·
hikâye önce onay. Sabitler prompt_kontrol.py / sayac.sh başında; bir sayı
değişecekse tek yerde değişir. Yeni ders/kapı yazmadan önce ikinci soru:
bu tavanı aşıyor mu — aşıyorsa biri çıkar, ekleme yapılmaz.

Yeni bir ders yazmadan önce sor: bu prompt cümlesiyle mi çözülüyor,
yoksa planla, sahne haritasıyla veya kurguyla mı? İkincisiyse dersi
LESSONS_LEARNED'a yazmak onu çözmez.

Ayrıntı: URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md · reform kaydı
TODO_AKIS_VE_DERS_REFORMU.md (14.09.2026)
```

---

> **Bu dosya ne zaman güncellenir**
> □ Yeni klasör/format eklenince → §1 haritası + kart H
> □ Yeni QA rubriği eklenince → yeni görev kartı (§3)
> □ §6'daki bir açık kapanınca → satırı sil
> □ Yeni bir "hangi dosyayı güncelleyeceğim" sorusu çıkınca → yeni kart
>
> Bu dosyaya **içerik** taşıma. Adres ver, kaynağa yolla.
