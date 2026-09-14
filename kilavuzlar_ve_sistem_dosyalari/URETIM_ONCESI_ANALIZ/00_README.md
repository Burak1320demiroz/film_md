# 🔮 ÜRETİM ÖNCESİ ANALİZ

> ⚠️ **KESİT UYARISI (eklendi 21.08.2026):** Bu klasörün 00/01/02
> dosyaları **01.08.2026 kesitiyle** yazıldı — o gün depoda 11 QA raporu
> ve 50 ders vardı. Güncel sayılar: `bash ../sayac.sh`. 01 raporu
> D51-119'u HİÇ ölçmedi (bilinen borç: `../KILAVUZ_REHBERI.md` §9).
> 02'ye 10-12 kartları 21.08.2026'da eklendi; eski filmlerin `n/9` risk
> skorları 9 kartlık sürümle ölçüldü ve yeniden yazılmaz.
> Akış şeması 22.08.2026'da güncellendi: konsept+tema kapısı ve
> PROMPT_KONTROL adımı işaretçi olarak eklendi (içerik kesit malıdır).
> 11.09.2026: dosya tablosu DÖRT KATMANA ayrıldı (tabloda olmayan
> 07·09·10·11·15·19 ve TUR5/6/7/12/13/14 klasörleri eklendi), her araştırma
> dosyasına TUR · koşu · indiği yer sütunu kondu, dış araştırma döngüsü
> akış şemasına eklendi (§🔁 ikinci döngü).

> **Amaç:** Parayı harcamadan önce neyin bozulacağını bilmek.
> **Oluşturma:** 31 Temmuz 2026
> **Girdi:** Yeni üretim YOK. Yalnızca 01.08.2026 kesitindeki 11 QA raporu + 50 ders.

---

## 🧭 NE İŞE YARAR — üç iş, tek satır

Bu klasör film üretmez, kural da koymaz (kural kök kılavuzlardadır).
Üç iş yapar; her işin kendi dosyaları ve kendi okuyucusu var:

```
① ÖNCE SÖYLER   yazılacak film NEREDE kırılacak     → 02 · 03 · 05 · 06
                okuyan: yeni-film adım 4 (KONSEPT: 02 risk kartları) ve
                adım 10 (KAPI: 03'ün maddeleri) · prompt_kontrol ⑰ (06'nın
                B5 dörtlüsü, makinede koşar) · 02_KONSEPT_VE_RISK şablonu ·
                PROMPT_QA_CRITIQUE rubriği (02 kartlarıyla puanlar)

② KAYNAĞI TUTAR bir kural NEDEN var, NEREDEN geldi   → 04 + TURn_HAM_RAPORLAR/
                okuyan: "bu kural neden?" diye soran herkes · KILAVUZ_REHBERI
                ve prompt_kontrol'ün "Kayıt: 04 §TUR n" satırları
                ⛔ kural 04'ten OKUNMAZ; 04 kuralın kaynağını gösterir

③ SONRA ÖLÇER   koyduğumuz kural İŞE YARADI mı        → 01
                okuyan: yayin-takip skill · AGENTS kart Y (QA skoru yüksek,
                gerçek metrik düşükse yanlış olan RUBRİKTİR → 01) ·
                PROMPT_QA_CRITIQUE (kaynak satırı)
                ⚠️ 01.08.2026 kesitinde dondu; D51+ hiç ölçülmedi (bilinen açık)
```

Somut örnek, tek zincir: ⑩ OYUNCULUK skoru platoda kaldı → `18_` dört prompt
yazdı → TUR 15 koşuldu, ham `TUR15_HAM_RAPORLAR/`'a birebir indi → 04 §TUR 15
süzdü (neyin girdiği / girmediği / neden) → dört kılavuz yazıldı
(`../KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` vd.) → `yeni-film` adım 4-5-7-8-9b
onları İSTER. Bir gün "karakter kartı neden sekiz satır?" diye sorulursa cevap
kılavuzda değil, 04 §T15.2 + `TUR15_2_KARAKTER_KARTI_HAM.md`'dedir.

Klasörün adı "üretim öncesi analiz" ama hacminin büyük kısmı ② (04 + ham
klasörleri). Bu bir sapma değil: ① ve ③ kısa kontrol listeleridir, ② ise
her turda büyüyen arşivdir.

---

## 📁 DOSYALAR — dört katman

### A · Kesit teşhisleri — 01.08.2026 verisiyle yazıldı, kesit uyarısı taşır

| Dosya | Ne yapar | Ne zaman kullanılır |
|---|---|---|
| `01_DERS_ETKINLIK_RAPORU.md` | kesit dersleri (01.08.2026) hangisi işe yarıyor — kanıtla | ders eklerken / çıkarırken |
| `02_RISK_KARTLARI.md` | "Filmde su var" → ne bozulacak, ne yapılmalı | **plan yazmadan önce** |
| `03_PLAN_ONCESI_KONTROL_LISTESI.md` | Yazılmış planı üretime sokmadan tara | plan bitti, üretim başlamadan |

### B · Hat teşhisleri — kesit uyarısına tabi DEĞİL, kendi betiğiyle yeniden koşulur

| Dosya | Ne yapar | Ne zaman kullanılır |
|---|---|---|
| `05_DIKEY_HAT_TESHISI.md` 🆕 | **Dikey hattın neden "anlamsız" hissettirdiği** — 18 filmin makine taraması, dört üretim önleminin hikâye formatına dönüşme mekanizması, maliyete göre sıralı altı çözüm ve iki prob | dikey film yazmadan önce · "neden hepsi aynı film?" sorulduğunda |
| `06_HIKAYE_HATTI_TESHISI.md` 🆕 | **Bütün deponun neden "saçma" hissettirdiği** — 79 filmin taraması, üç halkalı kapalı döngü (yasaklar türü kurdu · kapılar yalnız üretimi ölçtü · **tür kendini ölçen rubriğe "bu kusur değildir" diye yazıldı**), maliyete göre sıralı çözüm + sahibin iki editoryal kararı | **her film yazmadan önce** · "hikâye neden zayıf?" sorulduğunda · rubrik/novum kuralı tartışılırken |
| `PROB_KOSUSU.md` + `prob_olcum.sh` 🆕 | 05 §5④'ün koşu sayfası: yapıştırmaya hazır iki prob, adım adım koşu, boş sonuç tablosu ve **makineyle ölçüm betiği** (gerçek master üstünde doğrulandı) | dört yasak (ikinci insan · replik · isim · kesme) sınanacağında |

> ⭐ **05, bu klasörün ilk TERS YÖNLÜ dosyasıdır:** 01/02/03 "bu film
> nerede kırılacak" diye sorar; 05 ve 06 "yazdığımız her filmin AYNI yerde
> kırılmasının sebebi ne" diye sorar. Tek filme değil, HATTA bakar.

### C · Dış araştırma promptları — her dosya bir TUR'un girdisi

Her dosya dört **salt prompt** taşır (altışar cümle; 18 onar; 20 ÜÇ prompt, onar). Dosyada
durmasının sebebi: sistem bilgisi sohbette yaşayamaz — aynı prompt ay sonra
**aynı metinle** yeniden koşulabilsin, iki tur karşılaştırılabilsin.
⛔ Çıktı doğrudan kılavuza girmez: araştırma → `TURn_HAM_RAPORLAR/` (birebir)
→ 04 §TUR n (süzme: ZATEN VAR / girdi → nereye / girmedi → neden) → ancak
oradan kılavuz, rubrik, kapı veya şablon.

| Dosya | Ne sorar | TUR · koşu · nereye indi | Ne zaman kullanılır |
|---|---|---|---|
| `07_POLITIKA_ARASTIRMA_PROMPTLARI.md` | Dört motorun (Nano Banana Pro · Nano Banana 2 · Veo · Osmi) içerik politikası yüzeyi için dört derin araştırma promptu — altışar cümle, salt prompt; PROMPT reddi ile ÇIKTI reddini ayırır, mesaj metnini birebir ister. ⛔ Red SAYISI kılavuza yazılmaz, tek yeri `../FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | TUR 3 · ✅ 01.09.2026 → `../POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` §1/§3/§5 + `02_RISK_KARTLARI` KART 12 · ham klasörü YOK (süzme 04 §TUR 3) | politika/red kuralı tartışılırken · "neden reddedildi?" sorulduğunda · aynı promptlar yeniden koşulacağında |
| `08_SENARYO_ARASTIRMA_PROMPTLARI.md` 🆕 | Hikâye tarafı için dört derin araştırma promptu (çıkarılabilir an · sözsüz istek-hasım · az replikli senaryo · uzay kısa film rakip seti) — altışar cümle, salt prompt, kapanışları aynı | TUR 4 · ✅ 02.09.2026 → `03_PLAN_ONCESI` B5'in gerekçesi (istek · bedel · muhatap yok = "umursamadım") + `../ONERME_VE_NOVUM_KILAVUZU.md` + `../SENARYO_VE_VIRAL_KAMERA` §2.4 + `HOOK` §5 · ham klasörü YOK — kayıt iddia düzeyinde (04 §TUR 4 dürüst sınır) | 06'nın açık sorularını dış bilgiyle kapatırken · araştırma turu koşulacağında |
| `09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` | Astronot karakterin giysi donanımı (rozet/amblem · kişisel eşya · saat/bilek · yaşam destek ünitesi) için dört derin araştırma promptu — altışar cümle, salt prompt | TUR 5 · ✅ 03.09.2026 → `../ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` · ham `TUR5_HAM_RAPORLAR/` (TAM metin) | Character Bible'a donanım yazılırken · aynı promptlar yeniden koşulacağında |
| `10_DIYALOG_ARASTIRMA_PROMPTLARI.md` | Repliğin İÇERİĞİ ve ÖLÇÜMÜ için dört derin araştırma promptu (kalite ölçütleri · alt metin/bilgi yükü · konuşma İngilizcesi + telsiz/makine registerı · eleştiren hakemin güvenilirliği) — altışar cümle, salt prompt; TUR 4'ün 3 numaralı promptu repliğin VARLIĞINI sormuştu, bu tur İÇERİĞİNİ sorar | TUR 6 · ✅ 03.09.2026 → ⭐ yeni kapı `../PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md` + `../SES_VE_DIYALOG_URETIM_KILAVUZU.md` §2a + `FILM_PLAN.md` replik tablosu · ham `TUR6_HAM_RAPORLAR/` (TAM metin + kaynak listeleri) | replikli film yazılırken · DIALOGUE_CRITIQUE kuralı sorgulanırken |
| `11_UZAYLI_TASARIM_ARASTIRMA_PROMPTLARI.md` | Filmlere TEK görkemli uzaylı varlık eklemek için dört derin araştırma promptu (huşu mekanizması · gösterilebilir bilimsel morfoloji · göstermeden görkem / dev yapı · ilk temas dramaturjisi: tek tanık, sıfır replik) — altışar cümle, salt prompt | ⚠️ **TUR 8 — BU DOSYANIN PROMPTLARI HÂLÂ KOŞULMADI.** 03.09.2026'da TUR 7 oturumda yazılan DÖRT BAŞKA promptla koşuldu (tasarım · viral · AI motoru · astrobiyoloji → `../UZAYLI_VARLIK_TASARIM_KILAVUZU.md`, ham `TUR7_HAM_RAPORLAR/`). TUR 8 numarası bu dosyaya rezerve; koşulup koşulmayacağı sahibin kararı (04 §T7.4 ④) | "görkem ölçütleri" sorusu açılırsa · uzaylı kılavuzu ikinci tura girecekse |
| `12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` ✅ | Uzay üssü / istasyon mimarisi için dört derin araştırma promptu (yörünge dış anatomi · yüzey üssü yapı sistemi · basınçlı iç mekân · tek sabit planda ölçek kanıtı) — altışar cümle, salt prompt, astronot-göreli oran ister, ölçüyü gövdeye yazdırmaz [D138] | TUR 9 · ✅ 04.09.2026 → `../UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` · ham `TUR9_HAM_RAPORLAR/` | kurulacak `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` için araştırma turu koşulacağında · Ders 32 ↔ 138 çelişkisi çözülürken |
| `13_GIRIS_VE_FINAL_ARASTIRMA_PROMPTLARI.md` ✅ | Film girişi ve finali için dört derin araştırma promptu (açılış planı / ilk imge · kapanış planı / muhatap / sonrası bütçesi · açılış-kapanış çifti · süre bandına göre giriş-çıkış bütçesi) — altışar cümle, salt prompt, TUR 1/4 ile çakışanlar "ZATEN VAR" etiketiyle düşer | TUR 10 · ✅ 04.09.2026 → `../ACILIS_KAPANIS_CIFTI_KILAVUZU.md` + HOOK/FINAL genişletmeleri · ham `TUR10_HAM_RAPORLAR/` | `HOOK` platosu kırılacağında · `FINAL` §2'ye 10-20 dk satırı yazılacağında · araştırma turu koşulacağında |
| `14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` 🆕 | Deponun ÖLÇÜLMÜŞ dört arızasına vuran dört derin araştırma promptu (sahne zinciri · kurgu kaybı · duygu kanalı · kural temizliği) — altışar cümle, salt prompt, cevabın biçimini dayatmaz, "ZATEN VAR" kapısı açık | TUR 11 · ✅ 04.09.2026 → `../SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` + `../KARAKTER_VE_DUYGU_KILAVUZU.md` §4.2/§4.3/§7/§8 + `../KURGU_VE_TESLIM_KILAVUZU.md` §2 · ham `TUR11_HAM_RAPORLAR/` · ⚠️ sorular tuttu, raporların sayı katmanı çürük çıktı (04 §T11.0) | 06'nın kapalı döngüsü ve KURGU §0 kaybı kapatılacağında · araştırma turu koştu → TUR 11, süzme 04 §TUR 11 |
| `15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` | Her filmin REFERANS PAKETİNİ kılavuza ve kapıya çevirmek için dört derin araştırma promptu (envanter · tetikleyici · durum mimarisi / görünüş açıları · sayfa · ölçek · referans ışığı / AI hattında referansın çalışması ve zincir sürüklenmesi / makine okunur şema · sayısal kapı · yaşam döngüsü · politika) — altışar cümle, salt prompt; envanter İSTER, listeyi VERMEZ (TUR 9-11'in dersi) | TUR 12 · ✅ 06.09.2026 → `../REFERANS_PAKETI_KILAVUZU.md` · ham `TUR12_HAM_RAPORLAR/` (TAM metin, kaynak listeleri dâhil) | referans paketi yazılırken · D146 (biçim kilidi metinle tutulmuyor) tartışılırken |
| `16_UZUN_TEK_KISI_HAYATTA_KALMA_ARASTIRMA_PROMPTLARI.md` 🆕 | Mars ekseninde açılan yeni yatay film (15 faz × 12 sahne × 10 s = 30:00, replikli, motor OMNI) için dört derin araştırma promptu (uzun formda tek kişilik hayatta kalma açılışı · yalnız adamın muhatabı ve 10 s klipte replik üretimi · 15 birimlik prosedürelin problem zinciri ve üst katmanı · metinsiz geçen zamanın gövde/mekân merdiveni) — altışar cümle, salt prompt. ⚠️ Künyede ÜÇ AÇIK ÇELİŞKİ kayıtlı: bant tavanı 10 fazdır (15 faz %50 üstü), referans filmin zaman motoru ara yazıdır (bu hatta yasak), OMNI red defteri vaka 15'in motorudur [D167 · kapı ⑲] | TUR 13 · ⚠️ 07.09.2026 — **4. prompt KOŞULMADI** (açık borç: zaman merdiveni; `19_`'un 1 numarası aynı metni koşar) → `THE_SCOURED_GLASS/00_PLAN` · ham metin arşivde YOK, yalnız `TUR13_HAM_RAPORLAR/00_KUNYE.md` | plan yazılmadan önce · araştırma turu koşulacağında (TUR 13) |
| `17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` 🆕 | Yeni filmin EKSEN aldığı tek yapımı (The Martian, 2015) söken dört derin araştırma promptu (Mars hattını Dünya hattından ayırma ve bilgi borcu · günlük kamerasının çekim grameri ve yerleşim haritası · FİLM ile GERÇEK ayrı sütunlu Mars künyesi · hasımsız gerilimde mizah ve yetkinlik) — altışar cümle, salt prompt. ⛔ Özel kapısı KOPYA SINIRI [MESHUR_SAHNE §4]: bulgu ancak GEOMETRİYE ve MEKANİZMAYA çevrilerek iner, film/karakter/marka adı üretim promptuna yazılmaz; süzmede üçüncü liste **GEOMETRİYE ÇEVRİLDİ** tutulur. 16 türü sorar, 17 tek yapımı — ayrı tur (TUR 14) | TUR 14 · ✅ 07.09.2026 → `THE_SCOURED_GLASS/00_PLAN` (KOPYA SINIRI: GEOMETRİYE ÇEVRİLDİ listesi 04 §T14.3) · ham metin arşivde YOK, yalnız `TUR14_HAM_RAPORLAR/00_KUNYE.md` | eksen film seçildikten sonra · 16 ile birlikte, plan yazılmadan önce |
| `18_OYUNCULUK_VE_KARAKTER_ARASTIRMA_PROMPTLARI.md` 🆕 | Oyunculuk hattının dört kılavuzu (OYUNCULUK_YAZIM · KARAKTER_KARTI_VE_DAVRANIS · IKI_KISI_VE_AYRILIK · DIYALOG_SAHNESI_VE_MUHATAP — dördü 11.09.2026'da yazıldı) için dört derin araştırma promptu (niyet/tereddüt/karar/sonrası BEDENDE · karakter kartı ve davranış tutarlılığı · iki kişi: fark, sözsüz cevap, mesafe · diyalog sahnesi: hamle, cevap, dinleyen, değişim) — onar cümle, cümle başına tek satır, salt prompt. Etiket: ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ. TUR 4/6/11/13/14 ile çakışanlar "ZATEN VAR"; dört çapraz çift (1↔2 · 1↔4 · 2↔3 · 3↔4) | TUR 15 · ✅ 11.09.2026 → `../KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` · `../IKI_KISI_VE_AYRILIK_KILAVUZU.md` · `../DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` · `../OYUNCULUK_YAZIM_KILAVUZU.md` (yeni-film adım 4-5-7-8-9b) · ham `TUR15_HAM_RAPORLAR/` (4/4 birebir) | ⑩ OYUNCULUK 2,0-6,3 platosu ve `06` §1.4 (bible karakter taşımıyor) kapatılacağında · araştırma turu koşulacağında (TUR 15) · ⛔ dört kılavuz süzme bitmeden yazılmadı (sıra tutuldu) |
| `19_THE_SCOURED_GLASS_NOVUM_KAYNAK_GORUS_ARASTIRMA_PROMPTLARI.md` 🆕 | `yatay_10_20_dk_filmler/THE_SCOURED_GLASS/` filminin FAZ 1'i ve 00_PLAN'ı güncellenmeden ÖNCE kapatılması gereken dört filme-özgü soru için dört derin araştırma promptu (metinsiz geçen zaman merdiveni — TUR 13'ün koşulmayan 4. promptunun BİREBİR tekrarı · novum fiziği ve görünürlüğü · kaynak aritmetiği ve problem zincirinin fizik doğrulaması · görüş kaybı dramaturjisi) — altışar cümle, salt prompt. 16 türü, 17 ekseni, 18 oyunculuğu sordu; üçü de bu filmin NOVUM'unu ve KAYNAK ARİTMETİĞİNİ sormamıştı | TUR 16 · ✅ 11.09.2026 — 4/4 birebir → `THE_SCOURED_GLASS/00_ANALIZ` + 00_PLAN (novum yeniden tanımı · KİLİT 1/4/5 · faz haritası · B5) · kılavuz adayları ⬜ (04 §T16.7) · ham `TUR16_HAM_RAPORLAR/` (2·3·4) + `TUR13_HAM_RAPORLAR/TUR13_4_…` (1 — §TUR 13'ün açığı KAPANDI) | THE_SCOURED_GLASS FAZ 1 / 00_PLAN güncellenmeden önce · araştırma turu koşulacağında |
| `20_SINEMATIK_UZAY_GIYSISI_ARASTIRMA_PROMPTLARI.md` 🆕 | Kurulacak `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` (astronot giysisinin GÖRÜNÜŞ katmanı — `ASTRONOT_DONANIM` yalnız KİMLİK katmanıdır) için ÜÇ derin araştırma promptu (silüet ve tasarım dili: arketip · kask mimarisi · "sinematik okuma" değişkenleri · yüzey, renk ve ışık: malzeme sözlüğü · renk bloğu · kask içi ışık · AI motorunda oyun-görünümü riski · giysi kilidi ve bütçe: sürüklenme sırası · metin bütçesi · sırt tarif biçimi · "tasarlandığı gibi mi" ölçümü) — onar cümle, cümle başına tek satır, salt prompt. Etiket: ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ. TUR 3/5/12 ile çakışanlar "ZATEN VAR"; KOPYA SINIRI (film adı araştırmada olur, üretim promptuna inmez → süzmede GEOMETRİYE ÇEVRİLDİ listesi); üç çapraz çift (1↔2 · 2↔3 · 1↔3). Tetikleyici: sahibin isteği 12.09.2026 ("kıyafetler çok kötü, film tarzı havalı olsun") + depo teşhisi (bible tek sıfat + "pressure suit" · D79/139 bloğunun yan etkisi · TUR 5 kimlik sordu görünüş sormadı · tasarım kalitesini ölçen mercek yok) | TUR 17 · ✅ 12.09.2026 → `../UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` (§1 teşhis · §2 beş arketip · §4 kask + kask içi ışık · §5 malzeme · §6 renk · §7 kir · §8 sırt ⬜ · §9 bütçe · §11 üç blok · §12 ⬜ mercek ⑭) · ham `TUR17_HAM_RAPORLAR/` (3/3 birebir, kaynak listesi yok, tablolar çökmüş) · ⚠️ sayı katmanı çürük — kılavuz SAYISIZ (04 §T17.4) | giysi kılavuzu yazılmadan önce · araştırma turu koşulacağında (TUR 17) |
| `21_DUNYA_ISIK_YUZ_ARAC_GORUNUS_ARASTIRMA_PROMPTLARI.md` 🆕 | Şablonun kılavuzsuz kalan Bible katmanları için DÖRT derin araştırma promptu — ① DÜNYA görünüşü (World Bible: gökyüzü gradyanı · ufuk · arazi doku hiyerarşisi · gök cisimleri · "fon levhası" değişkenleri · motorda sürüklenme) · ② IŞIK senaryosu (Lighting Bible: ışık planı belgesi · güneş yönü/takvim kilidi · kesmeler arası ışık algısı · vakum ışığı · motorda tarif biçimi) · ③ YÜZ ve kast (Character Bible'ın yüz yarısı: milliyetsiz sözlük · kaskta tanımayı taşıyan bölge · kanal boyu çeşitlilik · kimlik sürüklenmesi) · ④ ARAÇ ve iç hacim (Vehicle Bible ⬜ + kabin/kokpit/koridor: dış yüzey dili · "yaşanmış" okuması · iç-dış tutarlılık · oyun-görünümü kelimeleri) — altışar cümle, salt prompt; ZATEN VAR kapısı REHBERİ §3 · SINEMATOGRAFIK §1 · TUR 9/12/17'ye açık; deponun kararları (D47·D48·D79·D104·D138·D145·D201) kısıt olarak beşinci cümlede | TUR 18 · ⏳ **12.09.2026 yazıldı, KOŞULMADI** → koşulunca `TUR18_HAM_RAPORLAR/` + 04 §TUR 18 → dört yeni kılavuz (çalışma adları dosyanın başında) | Sahibin "kılavuz olarak başka eksik ne var" sorusunun cevabı (12.09.2026 taraması) · World/Lighting Bible yazılmadan · yüz bloğu ve araç bloğu tek sıfata düştüğünde · aynı promptlar yeniden koşulacağında |

> ⚠️ **TUR 8 BOŞTUR** — `11_`'e rezerve; o koşu yapılmadı. TUR numarası
> koşuya verilir, dosyaya değil (Tur 7 usulü): `11_` dosyası TUR 7'nin
> girdisi olarak yazıldı ama TUR 7 başka promptlarla koştu.

### D · Hafıza — kural buradan OKUNMAZ, kuralın NEREDEN geldiği burada

| Dosya | Ne yapar | Ne zaman kullanılır |
|---|---|---|
| `04_ARASTIRMA_BULGULARI.md` 🆕 | Dış araştırma turlarının süzme kaydı: hangi bulgu hangi kılavuza indi, hangisi **girmedi ve neden** | dış araştırma geldiğinde · bir kuralın gerekçesi sorulduğunda |
| *(TUR 1 · TUR 2 — 27.08.2026)* | Prompt dosyası ve ham klasörü OLMADAN koşulan ilk iki tur (dikey shorts hattı · Gravity 2013 yapı sökümü). Yalnız 04 §1-6 ve §TUR 2'de yaşar; "aynı metin yeniden koşulsun" kuralı bu iki turdan sonra kondu (07'nin gerekçesi) | dikey hat / YERÇEKİMİ filmi kuralının kaynağı sorulduğunda |
| `TUR5_HAM_RAPORLAR/` · `TUR6_HAM_RAPORLAR/` · `TUR7_HAM_RAPORLAR/` · `TUR12_HAM_RAPORLAR/` | TUR 5 (astronot donanımı), TUR 6 (diyalog), TUR 7 (uzaylı varlık) ve TUR 12 (referans paketi) ham raporları — TAM metin, kaynak listeleri dâhil; TUR 7'de koşulan promptlar dosya başında birebir durur (`11_`'in promptları DEĞİL) | bir bulgunun NEREDEN geldiği sorulduğunda · aynı prompt yeniden koşulacağında |
| `TUR9_HAM_RAPORLAR/` · `TUR10_HAM_RAPORLAR/` · `TUR11_HAM_RAPORLAR/` 🆕 | TUR 9 (uzay üssü), TUR 10 (giriş/final) ve TUR 11 (ölçülmüş arızalar) ham raporları — düzeltilmemiş, kısaltılmamış, kaynak listeleri dâhil; her dosyanın başında koşulan prompt birebir durur | bir bulgunun NEREDEN geldiği sorulduğunda · aynı prompt yeniden koşulacağında |
| `TUR13_HAM_RAPORLAR/` · `TUR14_HAM_RAPORLAR/` ⚠️ | TUR 13 (uzun form tek kişi) ve TUR 14 (The Martian ekseni) için **`00_KUNYE.md`** (+ 11.09.2026: TUR13·4'ün geç koşusu `TUR13_4_ZAMAN_MERDIVENI_HAM.md` BİREBİR): hangi prompt koşuldu, hangi rapor geldi. ⚠️ Ham metinler sohbete yapıştırıldı ve buraya BİREBİR kopyalanmadı — süzme (04 §TUR 13/14) raporların bütün sayılarını alıntılayarak yazıldı, ama ham metin arşivde değil | TUR 13/14 bulgusunun kaynağı sorulduğunda (cevap: 04'teki alıntı, ham yok) · ham metin gelince buraya düşer |
| `TUR17_HAM_RAPORLAR/` 🆕 | TUR 17 (sinematik uzay giysisi: silüet · yüzey/renk/ışık · kilit/bütçe) ham raporları — 3/3 BİREBİR, her dosyanın başında koşulan prompt; `00_KUNYE.md` kaynak listesinin gelmediğini, tabloların çöktüğünü ve rapor 3'ün §3↔§8 iç çelişkisini kaydeder | bir bulgunun NEREDEN geldiği sorulduğunda · aynı prompt yeniden koşulacağında |
| `TUR16_HAM_RAPORLAR/` 🆕 | TUR 16 (THE SCOURED GLASS: novum fiziği · kaynak aritmetiği · görüş kaybı) ham raporları — 3/3 BİREBİR + TUR13·4 kardeş klasörde; `00_KUNYE.md` kaynak listesinin gelmediğini ve rapor 4 §7'nin kısıtı yanlış okuduğunu kaydeder | bir bulgunun NEREDEN geldiği sorulduğunda · aynı prompt yeniden koşulacağında |
| `TUR15_HAM_RAPORLAR/` 🆕 | TUR 15 (oyunculuk ve karakter) ham raporları — 4/4 BİREBİR, her dosyanın başında koşulan prompt; `00_KUNYE.md` kaynak listesinin gelmediğini ve iki raporun paragraf kırılmasız geldiğini kaydeder | bir bulgunun NEREDEN geldiği sorulduğunda · aynı prompt yeniden koşulacağında |

> ⚠️ **04, A katmanından farklıdır ve kesit uyarısına tabi değildir.**
> A katmanı 01.08.2026 kesitinden konuşur; 04 tarih tarih büyüyen bir
> kayıttır ve ilk turu 27.08.2026'dır. Kural 04'ten okunmaz — 04, kuralın
> NEREDEN geldiğini tutar.

> ⚠️ **05 de kesit uyarısına tabi değildir (30.08.2026).** Kendi taramasını
> kendi içindeki betikle yapar (§9.1) ve istendiği an yeniden koşulabilir.

---

## 🔁 AKIŞTAKİ YERİ — birinci döngü: TEK FİLM

```
   FİKİR
     │
     ▼
  KONSEPT + TEMA KAPISI  ← ../ONERME_VE_NOVUM_KILAVUZU.md (üç kabul testi —
     │                      geçmeyen konsept plana dönüşmez) + tema kararı:
     │                      ../TEMA_MUHENDISLIGI_KILAVUZU.md (22.08.2026)
     ▼
  06_HIKAYE_HATTI_TESHISI ← ⛔ HER FORMAT: İSTEK/ENGEL/BEDEL/HASIM'ın
     │                      GEREKÇESİ. Kapı 03_PLAN_ONCESI B5'tedir ve
     │                      prompt_kontrol ⑰ olarak KOŞAR (02.09.2026)
     ▼
  05_DIKEY_HAT_TESHISI   ← ⛔ DİKEY FİLM YAZILACAKSA: dört yasağın
     │                      birikme mekanizması + final vuruş kanıtı
     ▼
  02_RISK_KARTLARI       ← "bu filmde su + canlı + diyalog var"
     │                      → 3 risk kartı, 3 sayısal kilit, 1 uyarı
     ▼
   PLAN + BIBLE yazılır  ← kök kılavuzlar (kuralın kendisi; kaynağı 04'te)
     │
     ▼
  03_PLAN_ONCESI_KONTROL ← plan kendi içinde çelişiyor mu, sahne sayısı
     │                      tutuyor mu, doruk yazılmış mı
     ▼
   PROMPT
     │
     ▼
  ../PROMPT_KONTROL/     ← betik + rubrik · sıfır kare (12.08.2026)
     │
     ▼
   ÜRETİM → QA mercekleri (güncel liste: ../QA_PROMPTLARI/00_README.md)
     │
     ▼
  01_DERS_ETKINLIK       ← QA sonucu buraya döner: ders tuttu mu tutmadı mı
```

Döngü kapanıyor: QA yeni ders üretiyor, **01** o dersin işe yarayıp
yaramadığını ölçüyor, **02** işe yarayanları bir sonraki filmin planına
sokuyor. Şu ana kadar eksik olan halka **01**'di — ders yazılıyor ama
tuttu mu tutmadı mı hiç ölçülmüyordu (ve 01.08.2026'dan beri hâlâ ölçülmüyor).

## 🔁 AKIŞTAKİ YERİ — ikinci döngü: DIŞ ARAŞTIRMA (film değil, KILAVUZ üretir)

Birinci döngü depo İÇİNDEKİ veriden konuşur. Bir soru depo içinde
cevaplanamıyorsa — skor platoda (⑩ OYUNCULUK), kılavuzda hiç olmayan konu
(uzaylı · uzay üssü · referans paketi), eksen film sökümü — ikinci döngü açılır:

```
  TETİKLEYİCİ   skor platosu · kılavuzda cevap yok · sahibin isteği · yeni film ekseni
     │
     ▼
  NN_*_ARASTIRMA_PROMPTLARI.md   dört salt prompt YAZILIR (sohbette değil dosyada;
     │                            "ZATEN VAR" kapısı ve çapraz çiftler burada ilan edilir)
     ▼
  dış araştırma aracı → TURn_HAM_RAPORLAR/   birebir, kısaltılmadan, prompt başta
     │                                        (kural ④'ün araştırma karşılığı: ham düzeltilmez)
     ▼
  04_ARASTIRMA_BULGULARI.md §TUR n   SÜZME — üç liste:
     │                                ZATEN VAR (depo biliyordu, ikinci kez inmez)
     │                                GİRDİ → hangi dosyanın hangi bölümüne
     │                                GİRMEDİ → neden (çelişki · kaynak çürük · hipotez)
     ▼
  kılavuz · rubrik · prompt_kontrol kapısı · şablon bloğu   ← kural BURAYA yazılır
     │
     ▼
  birinci döngünün PLAN + BIBLE adımına girer (yeni-film çizelgesi kendiliğinden görür)
```

İki döngünün farkı: birincisi her filmde koşar ve **filmi** değiştirir;
ikincisi tetiklendiğinde koşar ve **kuralı** değiştirir. İkincinin çıktısı
birincinin girdisidir; tersi yoktur (QA raporu doğrudan araştırma açmaz —
önce 01/05/06 "ölçülmüş arıza" der, sonra prompt yazılır: `14_`'ün yolu budur).

---

## ⚠️ BU KLASÖRÜN DÜRÜSTLÜK KURALI

```
Her satır bir KANITA dayanır: film adı + kategori skoru veya timestamp.
Kanıt yoksa satır "ÖLÇÜLEMEDİ" yazar — tahmin yazmaz.

Kesit gününde (01.08.2026) 50 dersin 36'sı ÖLÇÜLEMEDİ durumundaydı. Bu bir eksiklik değil,
BULGUNUN KENDİSİ: proje kurallarının çoğunun işe yarayıp yaramadığını
bilmiyor. Bunu gizlemek, 44 dersi 50'ye çıkarıp aynı yerde saymak olurdu.

Aynı kural ikinci döngüde de geçerlidir: dış rapor "ÖLÇÜLMÜŞ" dese de
kaynağı doğrulanamıyorsa 04'te ⬜ HİPOTEZ etiketiyle durur ve kılavuza
kural olarak inmez (TUR 11 ve TUR 12'nin sayı katmanı böyle düştü).
```

---

## 🔗 KOMŞU KLASÖRLER — karıştırma

| Klasör | Ne zaman | Neye bakar |
|---|---|---|
| **URETIM_ONCESI_ANALIZ** (bu) | üretimden **önce** | geçmiş veriye — "ne bozulacak" · dış araştırmaya — "kural nereden geldi" |
| `../QA_PROMPTLARI/` | üretimden **sonra** | üretilmiş işe — "ne bozuldu" |
| `../FILM_QA_RAPORLARI/` | sonra | rapor arşivi + T tabloları + tamlık matrisi |
| `../DERSLER/` + `../LESSONS_LEARNED.md` | sürekli | ders dizini (güncel sayı: sayac.sh) — arızanın kendisi |
| kök kılavuzlar (`../*_KILAVUZU.md`) | yazarken | kuralın kendisi — bu klasör kuralı KOYMAZ, kaynağını ve kontrolünü tutar |
