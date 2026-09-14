# 📖 THE_CRACKED_HELMET — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 09.09.2026 17:33
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
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` | 74 | Her ders açık kapı ve tetikleyici taşımalı |
| ✅ | `DERSLER/00_HIZLI_REFERANS.md` | 188 | Optik mesafe, lens açıları ve kadraj kilitleri |
| ✅ | `DERSLER/01_KAMERA_VE_KESME.md` | 266 | Ardışık iki sahnede ≥1 ölçek ve ≥45° kamera açısı değişimi zorunlu [D7] |
| ✅ | `DERSLER/02_KARAKTER_VE_CANLI.md` | 491 | Karakter maskesi/kaskı altında kinesik reset ve el vekili [D37·D57] |
| ✅ | `DERSLER/03_FIZIK_VE_HAREKET.md` | 854 | Vakum ortamında toz kalkmaz, parçacık yayı sönümlenmez, itki izi düzgün dağılır |
| ✅ | `DERSLER/04_ISIK_VE_CEVRE.md` | 298 | Zemin ve ışık tarifinde çift zemin çelişkisi yasağı [D176] |
| ✅ | `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | 733 | Kask çatlağı t=0 anında vizörde sabit geometrik iz olarak kilitlenir [D179] |
| ✅ | `DERSLER/06_METIN_VE_PROMPT_DILI.md` | 1279 | Promptlar self-contained olmalı, yasak kelimeler (camera, cinematic) kullanılmamalı [D45] |
| ✅ | `DERSLER/07_KURGU_VE_ANLATI.md` | 1162 | Doruk sahnesinde mutlak sessizlik metinle istenmez, audio katmanı net olmalı [D180] |
| ✅ | `DERSLER/08_QA_SURECI.md` | 4511 | QA SPEC dosyası eksiksiz yazılmalı ve makine kapıları ffmpeg ile doğrulanmalı |
| ✅ | `DERSLER/09_SISTEM_VE_SUREC.md` | 808 | Üretim sırası dramatik sıradan farklıdır: doruk ve kask tamiri önce üretilir |
| ✅ | `DERSLER/GOZLEM_DEFTERI.md` | 729 | Kamera takip komutlarında abartı hareketler engellenmeli |

### TUR 2 · ÜRETİM ÖNCESİ ANALİZ — teşhis ve risk

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `URETIM_ONCESI_ANALIZ/00_README.md` | 135 | Sıfır maliyetli analiz adımları takip edilmeli |
| ✅ | `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` | 337 | Ölçülmüş gürültü eşiği (1.5 puan) hesaba katılmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 585 | KART 12 (kısıtlanmış solunum / kırık vizör / aşırı efor) risk kilidi |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 508 | 14 maddelik plan öncesi kontrol listesi eksiksiz uygulanmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` | 2053 | El yuvası ve vizör beklenti şeridi tanımlanmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/05_DIKEY_HAT_TESHISI.md` | 517 | Şablonik tekrardan kaçınılmalı, ortama özgün fizik taşınmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5 Dörtlüsü (İstek, Engel, Bedel, Muhatap) somut nesneye bağlanmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/07_POLITIKA_ARASTIRMA_PROMPTLARI.md` | 162 | Yaralanma/baskı tasvirleri nötr ve pozitif form tarifleriyle yapılmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/08_SENARYO_ARASTIRMA_PROMPTLARI.md` | 179 | Vuruş haritasında ritim ve ASL dengesi kurulmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` | 88 | Astronot donanımı (kask vizörü, göğüs modülü, yama kiti) sabitlenmeli |
| ✅ | `URETIM_ONCESI_ANALIZ/10_DIYALOG_ARASTIRMA_PROMPTLARI.md` | 207 | Telsiz cızırtısı/nefes sesi audio kalıplarına eklenmeli |
| ✅ | `URETIM_ONCESI_ANALIZ/11_UZAYLI_TASARIM_ARASTIRMA_PROMPTLARI.md` | 131 | — (Bu filmde uzaylı biyolojik varlık yok, yalnız ıssız gezegen novumu var) |
| ✅ | `URETIM_ONCESI_ANALIZ/12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` | 161 | Enkaz ve çakılan mekik parçalarında ölçek şahidi (1H) kullanılmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/13_GIRIS_VE_FINAL_ARASTIRMA_PROMPTLARI.md` | 163 | Açılış (çakılma enkazı) ve kapanış (sızdırmaz kılınan vizör) kafiye bağı |
| ✅ | `URETIM_ONCESI_ANALIZ/14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` | 125 | Vizördeki sızıntı/gaz çıkışı kompozisyon yüzeyinde stabil tutulmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` | 113 | Astronot basınç giysisi ve kask çatlağı referans paketinde kilitlenmeli |
| ✅ | `URETIM_ONCESI_ANALIZ/16_UZUN_TEK_KISI_HAYATTA_KALMA_ARASTIRMA_PROMPTLARI.md` | 183 | Tek kişi hayatta kalma dramaturjisinde bedel fiziksel efor ve zaman ile ödenmeli |
| ✅ | `URETIM_ONCESI_ANALIZ/17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` | 143 | Ekipman modifikasyonu ve doğaçlama tamir kiti aşamalandırılmalı |
| ✅ | `URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md` | 261 | Kuru koşu testleri prompt kontrol öncesi doğrulanmalı |

### TUR 3 · KILAVUZLAR — hepsi

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `5_FAZ_MIMARISI.md` | 245 | — (12 sahneli 2-4 dk formatı, faz mimarisi muaf) |
| ✅ | `ACILIS_KAPANIS_CIFTI_KILAVUZU.md` | 260 | Açılış karesi: çakılan modülün sönmüş motor nozulu; Kapanış karesi: tamir edilen kask vizörünün yansıması |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | Kurulumsayımları A-B-C dizilimi, Dönüş ≥%40 ve Küme ≥2 kuralına uygun olmalı |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 367 | Giysi kimliği: göğüs modülü serisi, bilek basınç göstergesi, sırt silueti ve vizör çatlağı |
| ✅ | `DIKEY_MIKRO_DRAMA_KILAVUZU.md` | 473 | El vekili ve kinesik temas sahne 04 ve sahne 08'de kullanılmalı |
| ✅ | `DIS_REFERANS_OLCUMU.md` | 198 | Ölçek şahidi: astronot kasklı gövdesi (1H) nesne bağıntılarında kullanılmalı |
| ✅ | `FAZ_DOSYASI_SABLONU.md` | 281 | — (Faz mimarisi muaf) |
| ✅ | `FINAL_VE_PAYLASIM_KILAVUZU.md` | 420 | Final tipi: Görsel İkilem / Hayatta Kalma Başarısı; tohum bilgi %10-15 aralığında verilmeli |
| ✅ | `FRAGMAN_KILAVUZU.md` | 548 | — (Ana film üretimi) |
| ✅ | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` | 580 | Bass drone + metalik rezonans + oksijen valfi tıslaması yatağı |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | S00: Şiddetli çakılma sonrası dumanlı kokpit / vizördeki ince kılcal çatlak (0-2sn merak, 2-5sn sızıntı sesi) |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 306 | V2 prompt şablonu: Özne + Çevre + Işık + Kamera + Hareket |
| ✅ | `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` | 205 | Sahne 02 (tehlike): Düşük açı; Sahne 06 (tamir eforu): Yakın plan makro; Sahne 10 (basınç testi): Göz seviyesi |
| ✅ | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | 155 | Kapak anı: Astronotun kırık vizöründen sızan gaz ve arkadaki mor kristalize zemin |
| ✅ | `KARAKTER_VE_DUYGU_KILAVUZU.md` | 462 | Kuleshov etkisi: Vizörün arkasındaki titreyen gözler <-> Hızlı düşen oksijen basınç göstergesi |
| ✅ | `KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` | 37 | — |
| ✅ | `KILAVUZ_REHBERI.md` | 2008 | Yatay 2-4 dk format kuralları ve vakum/ince atmosfer fizik kartı |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | ASL bandı (6.0 - 10.0 sn) ve örüntü kırıcı ritim geçişleri |
| ✅ | `KURGU_VE_TESLIM_KILAVUZU.md` | 225 | Kurgu kapısı 10 maddelik denetim listesi |
| ✅ | `LESSONS_LEARNED.md` | 462 | DERS 176, 179, 180, 192, 193 kuralları hassasiyetle uygulanmalı |
| ✅ | `MESHUR_SAHNE_KALIPLARI_KILAVUZU.md` | 306 | Kalıp 04: "Zamansız Sayaç" (Oksijen basınç sayacı 04:12 -> 00:45) |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | Novum: Gezegendeki reçinemsi mineralin vakum altında polimerleşip cam-metal sızdırmazlık sağlaması |
| ✅ | `PAKETLEME_VE_VAAT_KILAVUZU.md` | 241 | Vaat-teyit: İlk 15 saniyede gösterilen vizör sızıntısı 09. sahnede reçineyle kapatılır |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | Kask çatlaması tarifinde kan/yaralanma kelimeleri kullanılmayacak, basınç sızıntısı ve gaz spreyi tarif edilecek |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 420 | Astronot giysisi ve reçine kiti biçim kilidi için referans paket yazılacak |
| ✅ | `SAHNE_DEVAMLILIK_KILAVUZU.md` | 383 | Göğüs kontrol paneli ışıkları (kırmızı flaş -> turuncu sabit) ve vizör çatlağının koordinatı sabit kalacak |
| ✅ | `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` | 433 | Sahne sınırlarında End/Start durum değişimleri sınır satırına yazılacak |
| ✅ | `SAVAS_SENARYO_KILAVUZU.md` | 660 | — (Savaş türü muaf) |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | Vuruş haritası: %0-%15 hook, %15-%60 hayatta kalma/arama, %60-%85 tamir eforu, %85-%100 sızdırmazlık testi ve son bakış |
| ✅ | `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` | 366 | Kanal görsel aile kimliğine uygun renk paleti (amber + obsidyen moru) |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 422 | Diyalog yok, ağır telsiz statik sesi, kesik nefes ve mekanik valf tıklaması |
| ✅ | `SHORTS_SISTEM_PROMPTU.md` | 268 | — (Yatay format) |
| ✅ | `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` | 759 | 35mm anamorfik lens, f/2.8 sığ derinlik, kontrastlı tek yönlü güneş ışığı |
| ✅ | `SKILL_KULLANIM_KILAVUZU.md` | 152 | Skill çalıştırma sırasına birebir uyulacak |
| ✅ | `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` | 480 | Sahne kesmelerinde sert ışık/açı değişimi, toz/duman arkası gizli geçiş yasağı |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | Tema: YALNIZLIK VE İRADENİN DİRENCİ (Tek insan novumu) |
| ✅ | `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` | 1269 | Mekik enkazından mineral kayalığına doğru hareket aksı (Soldan Sağa, 90°) |
| ✅ | `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` | 376 | — (Uzaylı canlı yok) |
| ✅ | `UZAY_SENARYO_KILAVUZU.md` | 795 | Vakum ortamında ses iletimi yok, yalnız gövde içi iletilen titreşim ve telsiz sesi |
| ✅ | `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` | 604 | Çakılan kaçış modülü mimarisi: ezilmiş titanyum panel, açık kabin modülü |
| ✅ | `VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md` | 228 | Veo video prompt yapısı ve extend zamanlaması |
| ✅ | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` | 388 | Paketleme başlığı: "CRASHED ON AN ALIEN WORLD: THE CRACKED HELMET" |
| ✅ | `YANASMA_VE_KENETLENME_KILAVUZU.md` | 220 | — (Yanaşma sekansı yok) |
| ✅ | `YAPI_GRAFI.md` | 459 | Karar ve klasör yapısı doğrulandı |
| ✅ | `YAYIN_VE_PERFORMANS_KILAVUZU.md` | 370 | YouTube Long-form / 2-4 min kadansı |
| ✅ | `DIS_FILM_ANALIZI/00_README.md` | 140 | Referans analiz metodolojisi |
| ✅ | `DIS_FILM_ANALIZI/KAMERA_ANALIZ_PROMPT.md` | 113 | Kamera hareketleri kontrolü |
| ✅ | `DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` | 237 | Kırılmış kask ve yalnız hayatta kalma dramaturjisi örneği |
| ✅ | `DIS_FILM_ANALIZI/OLAY_ANALIZ_PROMPT.md` | 125 | Olay dizilimi doğrulaması |
| ✅ | `DIS_FILM_ANALIZI/SENTEZ_ANALIZ_PROMPT.md` | 175 | Sentez kontrolü |
| ✅ | `DIS_FILM_ANALIZI/TEMA_ANALIZ_PROMPT.md` | 114 | Tema doğrulaması |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1235 | Sayaç ve tamlık matrisi güncellenecek |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 213 | Kask hasarı tarifinde fiziksel şiddet kelimeleri kesinlikle engellenecek |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | Hikaye notu 8.0 üzeri tutulmalı |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | Basınç ve gaz mekaniği mantık hatalarından arındırılmalı |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | Karakter eylemleri tutarlı olmalı |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | Telsiz ve nefes sesleri net olmalı |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | Yayın verileri takibi |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 46 | Beden dili ve el hareketleri mikro-mimik yerine geçecek |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 46 | Gezegen yüzeyinde mor mineral ışıması ve sert güneş zıtlığı tutarlı tutulacak |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 46 | İlk 5 saniyede vizördeki kılcal çatlak ve sızıntı sesi yakalamalı |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 83 | I2V start frame vizör çatlağını t=0'da taşımalı |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 102 | Basınç giysisi dikişleri ve göğüs göstergesi kaymayacak |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 88 | Telsiz hışırtısı ve valf tıslaması kurguda oturmalı |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 90 | B5 zinciri (bedel ödeme) hissettirilmeli |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 99 | Arka planda uzay mekanik enkazı sabit kalmalı |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 84 | Gaz sızıntısı jet sprey şeklinde vakumda yayılmalı |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 66 | Kask tamir hareketi kadrajda net okunmalı |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 66 | Titreyen eller ve ağır efor fiziksel olarak hissedilmeli |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 46 | Kamera açıları kilitlere uymalı |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (55 dosya · 14990 satır)

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_MIRROR_FAUNA.md` | ① aynı format | Yatay 2-4 dk kadraj geçişleri ve prompt yapısı kilitleri |
| ✅ | `THE_FROST_LINE.md` | ② aynı ortam kartı | İnce atmosfer/vakum yüzeyinde ışık zıtlığı ve kask vizör yansıması |
| ✅ | `THE_OPEN_CIRCUIT.md` | ③ aynı tema | Tek kişilik hayatta kalma mücadelesinde B5 Bedel zinciri ve ritim kilitleri |
| ✅ | `THE_SINKING_STAKE.md` | ④ en düşük skor | Arka plan sabitliği ve prompt dili tekrarlarından kaçınma |
| ✅ | `THE_KEPT_LIGHT.md` | ⑤ en yakın konsept | Zamana karşı yarışan astronot donanım tamiri dramaturjisi |
