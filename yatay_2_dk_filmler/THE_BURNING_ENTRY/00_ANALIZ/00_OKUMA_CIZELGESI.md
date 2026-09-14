# 📖 THE_BURNING_ENTRY — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 14.09.2026 10:17
> ⛔ **ELLE SATIR EKLENMEZ/SİLİNMEZ** — yeni kılavuz eklenirse betik yeniden koşulur.
>
> **Kural:** her satır okununca `⬜` → `✅` yapılır ve son sütuna
> **bu filme düşen kilit** yazılır. Kilit çıkmadıysa `—` yazılır; boş
> bırakılmaz — boş hücre "okudum" ile "atladım" arasını ayırt ettirmez.
>
> ⭐ Son sütunda yazılan her kilit `01_QA_DERS_HASADI.md` tablosuna taşınır.
> ⛔ ⬜ kalan satır varken `02_KONSEPT_VE_RISK.md` yazılmaz.

### TUR 1 · DERSLER — hepsi (film dersleri 01-07 · alet dersleri 08-09 · gözlem)

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` | 81 | Kilit cümlesi etiketsiz prompta taşınır, ders no gövdeye girmez [D45] |
| ✅ | `DERSLER/00_HIZLI_REFERANS.md` | 188 | VACUUM PLUME [D36], DAMAGE CONTAINMENT [D38], SUIT LOCK [D57], NO AI TEXT [D159] |
| ✅ | `DERSLER/01_KAMERA_VE_KESME.md` | 266 | 16:9 yatay kadraj, kesintisiz 10s tek çekim, ASL ritim eğrisi, eksen kilidi |
| ✅ | `DERSLER/02_KARAKTER_VE_CANLI.md` | 513 | Karakter bedel ifadesi (G-kuvveti eforu), tek insan kilidi, siluet çapalama |
| ✅ | `DERSLER/03_FIZIK_VE_HAREKET.md` | 886 | Re-entry plazma fiziği, atmosferik sürtünme, dönüş/yalpalama dönme ekseni |
| ✅ | `DERSLER/04_ISIK_VE_CEVRE.md` | 314 | Vakumda sert gölge/sıfır fill ↔ Atmosferde turuncu plazma parıltısı ve toz süzülmesi |
| ✅ | `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | 750 | Kask camı çatlağı ilerleme kilidi (S04), pilot giysisi metalik/kompozit kilit |
| ✅ | `DERSLER/06_METIN_VE_PROMPT_DILI.md` | 1330 | HUD göstergeleri ışıklı gösterge paneli olarak yazılır; kompoze metin/overlay BAN |
| ✅ | `DERSLER/07_KURGU_VE_ANLATI.md` | 1177 | S09 tam ses kesintisi (heartbeat/breath), S11 gölge twist finali (K0 reveal) |
| ✅ | `DERSLER/08_QA_SURECI.md` | 4684 | Rubrik çalıştırma kuralları, MOD D (spec ile) sadakat ölçümü |
| ✅ | `DERSLER/09_SISTEM_VE_SUREC.md` | 874 | Kart A dizilimi, 00_ANALIZ sıralı adım disiplini |
| ✅ | `DERSLER/GOZLEM_DEFTERI.md` | 1942 | Dikey/yatay aksiyon kalıpları, kadrajda ölçek şahidi (kanyon kayalıkları) |

### TUR 2 · ÜRETİM ÖNCESİ ANALİZ — teşhis ve risk

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `URETIM_ONCESI_ANALIZ/00_README.md` | 237 | Meta-analiz rehberi, risk kartları ve hat teşhis haritası |
| ✅ | `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` | 337 | Aksiyon/fizik kilitlerinin Veo 3.1 ve Nano Banana modellerindeki sadakati |
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 585 | Uzay giysisi, cam çatlağı, roket itkisi, kanyon teması risk profilleri |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 513 | B1-B14 ve 17 maddelik plan öncesi denetim listesi (B5, KARAKTER, TEMA) |
| ✅ | `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` | 3153 | Dış araştırma bulgularının senaryo ve sinematografi kılavuzlarına aktarımı |
| ✅ | `URETIM_ONCESI_ANALIZ/05_DIKEY_HAT_TESHISI.md` | 517 | Şablonlaşma teşhisi: tekrarlayan hikaye kalıplarından kaçınma |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | Drama ve aksiyon tırmanışı: her 10s'de yeni somut fiziksel engel |
| ✅ | `URETIM_ONCESI_ANALIZ/07_POLITIKA_ARASTIRMA_PROMPTLARI.md` | 162 | Şiddet/zarar sözcükleri yerine pozitif fiziksel kuvvet ve eylem tarifi |
| ✅ | `URETIM_ONCESI_ANALIZ/08_SENARYO_ARASTIRMA_PROMPTLARI.md` | 179 | Aksiyon vuruş haritası: alarm yok -> doğrudan eylem ve geri sayım gerilimi |
| ✅ | `URETIM_ONCESI_ANALIZ/09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` | 88 | Astronot donanımı: rol şeridi, amblem, kask içi ışık ve vizör yansıması |
| ✅ | `URETIM_ONCESI_ANALIZ/10_DIYALOG_ARASTIRMA_PROMPTLARI.md` | 207 | Bu filmde replik YOK; yalnız nefes/kalp atışı ve kokpit mekanik sesleri |
| ✅ | `URETIM_ONCESI_ANALIZ/11_UZAYLI_TASARIM_ARASTIRMA_PROMPTLARI.md` | 131 | S11 finalinde uzaylı varlık YÜZÜ/BEDENİ görünmez; yalnız kanyon gölgesi (K0) |
| ✅ | `URETIM_ONCESI_ANALIZ/12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` | 161 | — (Üs yok; tek kişilik acil iniş mekiği) |
| ✅ | `URETIM_ONCESI_ANALIZ/13_GIRIS_VE_FINAL_ARASTIRMA_PROMPTLARI.md` | 163 | S00 sarsıntı ve HUD geri sayımı açılışı ↔ S11 kanyondaki Dev Gölge finali bağ kartı |
| ✅ | `URETIM_ONCESI_ANALIZ/14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` | 125 | Cam çatlağı kaybolması, alev dokusu donması, dönme ekseni yalpalaması engeli |
| ✅ | `URETIM_ONCESI_ANALIZ/15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` | 113 | KAPI 0 referans paketi standartları (görsel kilitler ve kanon) |
| ✅ | `URETIM_ONCESI_ANALIZ/16_UZUN_TEK_KISI_HAYATTA_KALMA_ARASTIRMA_PROMPTLARI.md` | 187 | Tek kişilik acil durum klostrofobisi ve bedensel efor dinamikleri |
| ✅ | `URETIM_ONCESI_ANALIZ/17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` | 147 | Sert bilimkurgu acil iniş gerçekçiliği ve mekanik kokpit hissi |
| ✅ | `URETIM_ONCESI_ANALIZ/18_OYUNCULUK_VE_KARAKTER_ARASTIRMA_PROMPTLARI.md` | 206 | Kinesik reset, göz hareketi, G-kuvvetinde parmak kasılması ve nefes ritmi |
| ✅ | `URETIM_ONCESI_ANALIZ/19_THE_SCOURED_GLASS_NOVUM_KAYNAK_GORUS_ARASTIRMA_PROMPTLARI.md` | 204 | Novum: atmosferik sürtünme felaketi ve tek iticiyle kanyon manevrası |
| ✅ | `URETIM_ONCESI_ANALIZ/20_SINEMATIK_UZAY_GIYSISI_ARASTIRMA_PROMPTLARI.md` | 215 | Uzay giysisi malzeme paleti, kask mimarisi, sert kabuk 3 kelime kuralı |
| ✅ | `URETIM_ONCESI_ANALIZ/21_DUNYA_ISIK_YUZ_ARAC_GORUNUS_ARASTIRMA_PROMPTLARI.md` | 259 | Atmosfer girişi ışık kırılmaları, kanyon ortamı doğal ışığı ve enkaz dumanı |
| ✅ | `URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md` | 261 | Prob koşusu prosedürü ve teknik başarısızlık protokolleri |

### TUR 3 · KILAVUZLAR — hepsi

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `5_FAZ_MIMARISI.md` | 245 | 5 faz mimarisi ve üretim adımları |
| ✅ | `ACILIS_KAPANIS_CIFTI_KILAVUZU.md` | 260 | Açılış (savrulan pilot + kask içi kırılan cam) ↔ Kapanış (doğrulan pilot + gölgeye bakış) |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | Açı sıçrama kuralı (küme içi geçişler, kamera psikolojisi, geniş-yakın dengesi) |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | Astronot giysisi rolleri, metinsiz göğüs amblemi, bilek kontrol paneli, kask |
| ✅ | `DIKEY_MIKRO_DRAMA_KILAVUZU.md` | 473 | — (Bu film 16:9 YATAY formatındadır; dikey kılavuz aksiyon ilkeleri kıyaslandı) |
| ✅ | `DIS_REFERANS_OLCUMU.md` | 198 | Ölçek şahidi (kanyon duvarı ↔ mekik gövdesi) ve çekim süre sınırları |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 384 | — (Replik yok; muhatap kokpit sistemleri ve doğadır) |
| ✅ | `DUNYA_GORUNUSU_KILAVUZU.md` | 341 | Yabancı gezegen kanyon atmosferi, kızılsı-turuncu gökyüzü, keskin kaya kuleleri |
| ✅ | `FAZ_DOSYASI_SABLONU.md` | 281 | Faz dosyası standart yapısı |
| ✅ | `FINAL_VE_PAYLASIM_KILAVUZU.md` | 420 | Final tipi: Görsel ikilem / Tehdit işareti (Kanyonda hareket eden devasa gölge) |
| ✅ | `FRAGMAN_KILAVUZU.md` | 548 | Yatay film fragman vuruş haritası standartları |
| ✅ | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` | 580 | S09 gürültü kesintisi sonrası yükselen organik perküsyone tekinsiz soundscape |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | Hook tipolojisi: S00 Acil durum eylemi + Dramatik İroni / Fiziksel Sarsıntı |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | — (Tek insan kilidi) |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 306 | V2 prompt iskeleti, SUBJECT, ENVIRONMENT, CAMERA, LIGHTING, MOTION, NEGATIVE |
| ✅ | `ISIK_SENARYOSU_KILAVUZU.md` | 322 | Kokpit içi kırmızı/turuncu acil ışığı ↔ Dış atmosfer plazma parıltısı ↔ Kanyon gölgesi |
| ✅ | `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` | 205 | 8 kask-içi ve kokpit dışı açı psiko-anlam haritası (Hollanda açısı = spin) |
| ✅ | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | 155 | Kapak mimarisi: Vizörde re-entry alev yansıması + cam çatlağı + kırmızı geri sayım |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | Karakter Bible ve davranıs kartı standartları |
| ✅ | `KARAKTER_VE_DUYGU_KILAVUZU.md` | 462 | Kuleshov etkisi, efor göstergeleri, nefes buğulanması, kasılan parmaklar |
| ✅ | `KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` | 37 | Tek çekim devamlılık ve akıcılık esasları |
| ✅ | `KILAVUZ_REHBERI.md` | 2165 | Format kartı (yatay 2 dk), Ortam kartları (§3.5 orbit/re-entry/surface), Negatif Çekirdek |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | ASL ritim eğrisi, örüntü kırıcı kesmeler, ses köprüsü |
| ✅ | `KURGU_VE_TESLIM_KILAVUZU.md` | 225 | Kurgu teslim kuralları, kırpma bütçesi, 10 maddelik kurgu kapısı |
| ✅ | `LESSONS_LEARNED.md` | 474 | Deponun ana ders dizini ve teknik kuralları |
| ✅ | `MESHUR_SAHNE_KALIPLARI_KILAVUZU.md` | 306 | Atmosfer girişi acil durum ve kanyon manevrası ikolnik kalıpları |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | Önerme: "Hayatta kalma mücadelesi en sert fizikte bile pes etmemektir." |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 461 | Bedensel niyet ve eforun prompta yazılması disiplini |
| ✅ | `PAKETLEME_VE_VAAT_KILAVUZU.md` | 241 | Vaat-teyit dengesi: Kapaktaki atmosfer girişi vaadi S00-S05'te tam karşılanır |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | Şiddet sözlüğü yasağı, kuvvet/sürtünme pozitif tanımı, aksiyon bütçesi |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | KAPI 0 Referans Paketi kuralları, 6 altı tetikleyici denetimi |
| ✅ | `SAHNE_DEVAMLILIK_KILAVUZU.md` | 386 | Seed ve visual continuity kilidi, vizör çatlağının koordinat sabitliği |
| ✅ | `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` | 433 | Sahne sınırları (End/Start) durum değişimi aktarımı, ardışık cevap yasağı |
| ✅ | `SAVAS_SENARYO_KILAVUZU.md` | 660 | — (Savaş yok; mekik acil inişi) |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | Viral kamera hareketleri: G-kuvveti sarsıntısı, kesintisiz takip, makro çatlak |
| ✅ | `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` | 366 | Kanal evren modeli ve kapak aile kimliği uyumu |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 422 | Ses efekti ve atmosfer tasarımı: vakum sessizliği ↔ atmosfer uğultusu ↔ darbe sesi |
| ✅ | `SHORTS_SISTEM_PROMPTU.md` | 268 | — (Yatay film formatı) |
| ✅ | `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` | 759 | Lens tanımı (35mm / 50mm / 85mm), ışık açıları, sinematik renk paleti |
| ✅ | `SKILL_KULLANIM_KILAVUZU.md` | 152 | Ajan skill rehberi ve prompt kontrol akışı |
| ✅ | `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` | 480 | Kesintisiz 10 saniyelik klip üretimi ve yumuşak geçiş disiplini |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | Tema: BEDEL (Fiziksel hayatta kalma mücadelesi ve efor) |
| ✅ | `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` | 1269 | Ekran yönü kilidi: mekiğin iniş vektörü soldan sağa (L->R) kilitli |
| ✅ | `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` | 376 | S11 finalinde varlık görünmez; yalnız K0 seviyesi dev kanyon gölgesi devinim yapar |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | Ağır İtiş/Acil İniş Giysisi (Arketip 2): kompozit göğüs zırhı, kask içi acil parıltısı |
| ✅ | `UZAY_SENARYO_KILAVUZU.md` | 795 | Yörünge bozulumu, atmosfer girişi, plazma kalkanı ve acil iniş fiziği |
| ✅ | `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` | 604 | — (Üs yok) |
| ✅ | `VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md` | 228 | Veo 3.1 video generation parametreleri ve negatif prompt yapısı |
| ✅ | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` | 388 | Viral İngilizce başlık ve açıklama paketi standartları |
| ✅ | `YANASMA_VE_KENETLENME_KILAVUZU.md` | 220 | — (Kenetlenme yok) |
| ✅ | `YAPI_GRAFI.md` | 482 | Klasör yapısı ve karar ağacı rehberi |
| ✅ | `YAYIN_VE_PERFORMANS_KILAVUZU.md` | 370 | Yayın sonrası performans analizi ve veri geri besleme |
| ✅ | `YUZ_VE_KAST_KILAVUZU.md` | 293 | Yüz tarifi disiplini (ünlü benzetmesi yasağı, kemik yapısı ve vizör içi aydınlatma) |
| ✅ | `DIS_FILM_ANALIZI/00_README.md` | 140 | Dış film analizi kurtarılmış dersler rehberi |
| ✅ | `DIS_FILM_ANALIZI/KAMERA_ANALIZ_PROMPT.md` | 113 | Kamera hareket analizi |
| ✅ | `DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` | 237 | Acil durum atmosferi ve tansiyon yönetimi dersleri |
| ✅ | `DIS_FILM_ANALIZI/OLAY_ANALIZ_PROMPT.md` | 125 | Olay örgüsü ve olay ziraatı |
| ✅ | `DIS_FILM_ANALIZI/SENTEZ_ANALIZ_PROMPT.md` | 175 | Sentez analiz metodolojisi |
| ✅ | `DIS_FILM_ANALIZI/TEMA_ANALIZ_PROMPT.md` | 114 | Tema analiz metodolojisi |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1218 | Depo kalite istatistikleri ve benchmark skorları |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 213 | Vaka #3/#4/#10/#13: şiddet/zarar kelimeleri yasağı, pozitif kuvvet tarifi |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | Anlatı sürekliliği ve mantık kapıları |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | Fiziksel gerçekçilik ve nesne koruma kilitleri |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — (Dikey format kalitesi) |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | Karakter ve kıyafet devamlılığı ölçütleri |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | Ses mizansen uyumu ve ses kesintisi etkisi |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | İzleyici elde tutma oranı ve ilk 3s hook başarısı |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | Oyunculuk ve efor sadakati ölçümü |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | Işık devamlılığı ve dinamik parıltı kontrolü |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | Hook ve ilk sahne tutma performansı |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 79 | Prompt-görüntü uyum skorları |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 91 | Sahne içi görsel kalite skorları |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 126 | Sahneler arası ortam ve ekipman devamlılık skorları |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 104 | Ses tasarımı teknik skorları |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 93 | Hikaye akışı skorları |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 110 | Arka plan alan kalitesi ve stabilite skorları |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 94 | Fizik kuralları sadakat skorları |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 76 | Aksiyon okunurluğu ve eylem kalitesi skorları |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 76 | Karakter efor ve bedel yansıtma skorları |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | Kadraj ve plan sadakati skorları |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (68 dosya · 16680 satır)

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_LAST_SHIFT.md` | ① aynı format (yatay 2 dk) | 12 sahnelik ASL ritmi, 2 bölüm geçiş sınırı kilidi |
| ✅ | `THE_CRACKED_HELMET.md` | ② aynı ortam kartı (yörünge/kokpit/kask) | Kask camı mikro-çatlağının sabit pozisyon kilidi |
| ✅ | `THE_COLD_BURN.md` | ③ aynı tema (BEDEL & hayatta kalma) | Şiddet kelimesiz sert efor ve fiziki zorlanma |
| ✅ | `THE_OPEN_CIRCUIT.md` | ④ en düşük skor / ders uyarısı | Çizelge atlama arızası önlendi; spec sadakati kilitlendi |
| ✅ | `LOSS_OF_LIFT.md` | ⑤ en yakın konsept (irtifa kaybı & acil iniş) | Mekik irtifa düşüşü ve kanyon çakılma dinamiği |

---

## 📊 ÇİZELGE ÖZETİ

```
ZORUNLU DOSYA:   115
ZORUNLU SATIR:   49265
SEÇMELİ KAYIT:   5 / 68  (TUR 5)
```
