# 📖 THE_MIRROR_FAUNA — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 08.09.2026 16:57
> ⛔ **ELLE SATIR EKLENMEZ/SİLİNMEZ** — yeni kılavuz eklenirse betik yeniden koşulur.
>
> **Kural:** her satır okununca `⬜` → `✅` yapılır ve son sütuna
> **bu filme düşen kilit** yazılır. Kilit çıkmadıysa `—` yazılır; boş
> bırakılmaz — boş hücre "okudum" meşguliyet tutma farkını yaratır.
>
> ⭐ Son sütunda yazılan her kilit `01_QA_DERS_HASADI.md` tablosuna taşınır.
> ⛔ ⬜ kalan satır varken `02_KONSEPT_VE_RISK.md` yazılmaz.

### TUR 1 · DERSLER — hepsi (film dersleri 01-07 · alet dersleri 08-09 · gözlem)

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` | 74 | Kılıçsız kapı yazılmaz; ders adresi net olmalı (D180/D165 ders dönüşüm borcu). |
| ✅ | `DERSLER/00_HIZLI_REFERANS.md` | 188 | ASL dalgalanması, kanca tipi S0 kararı ve vizör kilidi tablosu bağlandı. |
| ✅ | `DERSLER/01_KAMERA_VE_KESME.md` | 266 | Ardışık iki sahne aynı lens (35mm/50mm/85mm) ve aynı kadraj açısında olamaz. |
| ✅ | `DERSLER/02_KARAKTER_VE_CANLI.md` | 491 | Dört ayaklı varlık anatomi kilidi: reveal merdiveni (K0-K4), kinesik reset. |
| ✅ | `DERSLER/03_FIZIK_VE_HAREKET.md` | 854 | I2V t=0 kuralı (D179): görsel değişimin *sonrasını* değil *başlangıcını* taşımalı. |
| ✅ | `DERSLER/04_ISIK_VE_CEVRE.md` | 298 | Zemin ve ışık takvimi monoton azalamaz (D193), iki ayrı promptta zemin çelişemez (D176). |
| ✅ | `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | 733 | Astronot basınç giysisi kask kilidi (T1), amblem/rol şeridi ve bilek saati çapa kilidi. |
| ✅ | `DERSLER/06_METIN_VE_PROMPT_DILI.md` | 1279 | Replik işlevi (D122), promptlarda etiket [LESSON n] yasak, self-contained metin. |
| ✅ | `DERSLER/07_KURGU_VE_ANLATI.md` | 1162 | Üretim sırası dramatik sıra değildir (D168): Doruk → Merkez Seçim → S0 → Kalanı. |
| ✅ | `DERSLER/08_QA_SURECI.md` | 4511 | SPEC ve QA paketi olmadan yazım tamamlanamaz (D165). |
| ✅ | `DERSLER/09_SISTEM_VE_SUREC.md` | 808 | 00_INDEX ile dosya sistemi sayacı her adımda senkronize tutulmalı. |
| ✅ | `DERSLER/GOZLEM_DEFTERI.md` | 673 | Yansıma/taklit sahnelerinde kinetik bağımsızlık ve vekil nesne kuralı. |

### TUR 2 · ÜRETİM ÖNCESİ ANALİZ — teşhis ve risk

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `URETIM_ONCESI_ANALIZ/00_README.md` | 135 | Meta analiz okuma sırası ve kabul kapıları doğrulandı. |
| ✅ | `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` | 337 | Çapanın görsel bağımsızlığı ve kinetik reset etkinliği onaylandı. |
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 585 | Yaratık taklit hareketi riski (risk score high) -> Beden bağımsızlığı uyarısı. |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 508 | 14 maddelik plan öncesi kontrol sırasıyla B1-B14 uygulandı. |
| ✅ | `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` | 2053 | "Umursamadım" tepkisi engeli: B5 omurgası (İstek, Engel, Bedel+Sahne, Muhatap, Ayrılık). |
| ✅ | `URETIM_ONCESI_ANALIZ/05_DIKEY_HAT_TESHISI.md` | 517 | Şablonikleşme önlemi: İkinci insan (astronot 2) ilişkisi ve ayrılık çatışması. |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | Novumun 3 görsel kanıtı ekrana bağlanmalı (avuç/yüzey/hareket). |
| ✅ | `URETIM_ONCESI_ANALIZ/07_POLITIKA_ARASTIRMA_PROMPTLARI.md` | 162 | Şiddet/yasaklı kelime tarama kuralları. |
| ✅ | `URETIM_ONCESI_ANALIZ/08_SENARYO_ARASTIRMA_PROMPTLARI.md` | 179 | Vuruş haritası ve dramatolojik tırmanış. |
| ✅ | `URETIM_ONCESI_ANALIZ/09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` | 88 | Astronot giysisi donanım şeridi. |
| ✅ | `URETIM_ONCESI_ANALIZ/10_DIYALOG_ARASTIRMA_PROMPTLARI.md` | 207 | Replik lip-sync riski ve kadraj dışı ses kuralı. |
| ✅ | `URETIM_ONCESI_ANALIZ/11_UZAYLI_TASARIM_ARASTIRMA_PROMPTLARI.md` | 131 | Dört ayaklı varlık anten ve parıltı dokusu. |
| ✅ | `URETIM_ONCESI_ANALIZ/12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` | 161 | Araç/mekik ölçek kilidi (1H = kasklı astronot). |
| ✅ | `URETIM_ONCESI_ANALIZ/13_GIRIS_VE_FINAL_ARASTIRMA_PROMPTLARI.md` | 163 | İlk ve son kare döngü/kafiye bağı. |
| ✅ | `URETIM_ONCESI_ANALIZ/14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` | 125 | Lens sığdırma ve optik aritmetik riski. |
| ✅ | `URETIM_ONCESI_ANALIZ/15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` | 113 | Ref paketi muafiyet gerekçesi PLAN'a yazılacak. |
| ✅ | `URETIM_ONCESI_ANALIZ/16_UZUN_TEK_KISI_HAYATTA_KALMA_ARASTIRMA_PROMPTLARI.md` | 183 | İki astronot dinamiği ve diyalog yükü. |
| ✅ | `URETIM_ONCESI_ANALIZ/17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` | 143 | Prosedürel bilimkurgu hissiyatı. |
| ✅ | `URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md` | 261 | Kuru koşu ffmpeg kapı kontrolleri. |

### TUR 3 · KILAVUZLAR — hepsi

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `5_FAZ_MIMARISI.md` | 245 | Faz bölünmesi: Bölüm 1 (S00-S07), Bölüm 2 (S08-S14). |
| ✅ | `ACILIS_KAPANIS_CIFTI_KILAVUZU.md` | 260 | İlk kare S00 ile son kare S14 döngüsel görsel kafiyesi. |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | Kurulum iskeleti satırı: A B C A D E F B C E A F D B C (3+ açı tipi, KÜME≥2, DÖNÜŞ≥%40). |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 367 | Astronot Donanımı: Göğüs rol şeridi, sol bilek telemetri saati, omuz patch. |
| ✅ | `DIKEY_MIKRO_DRAMA_KILAVUZU.md` | 473 | Yatay format kuralları ile mikro drama vuruş geçişleri. |
| ✅ | `DIS_REFERANS_OLCUMU.md` | 198 | Saha kanıtı ölçek şahidi kullanımı (1H astronot ölçüsü). |
| ✅ | `FAZ_DOSYASI_SABLONU.md` | 281 | Bölüm dosyalarının şablon yapısı. |
| ✅ | `FINAL_VE_PAYLASIM_KILAVUZU.md` | 420 | Final ikilemi ve tohum bilgi (%10-15 gizem). |
| ✅ | `FRAGMAN_KILAVUZU.md` | 548 | Fragman vuruş haritası uyumluluğu. |
| ✅ | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` | 580 | Elektronik gerilim, modülasyonlu ortam pedleri, yansıma ses motifleri. |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | S00 Görsel İroni Kancası: astronotun gölgesinden önce taklitçi varlığın anten silueti. |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 306 | V2 prompt şablonu (📸 IMAGE PROMPT + 🎥 VIDEO PROMPT). |
| ✅ | `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` | 205 | Açı psikolojisi: düşük açı dehşet/huşu, göz hizası empati, yüksek açı kırılganlık. |
| ✅ | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | 155 | Kapak fotoğrafı visual contrast & vaat teyidi. |
| ✅ | `KARAKTER_VE_DUYGU_KILAVUZU.md` | 462 | Kuleshov etkisi, el hareketleri, nefes buğusu vizörde. |
| ✅ | `KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` | 37 | Gizli geçişler ve devamlılık ipuçları. |
| ✅ | `KILAVUZ_REHBERI.md` | 2004 | §2.2 yatay_2_dk_filmler kartı (15 sahne, 2:30 dk). |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | Target ASL bandı (8s - 12s), ASL eğrisi, örüntü kırıcılar. |
| ✅ | `KURGU_VE_TESLIM_KILAVUZU.md` | 225 | Kurgu kapısı 10 madde. |
| ✅ | `LESSONS_LEARNED.md` | 462 | Dersler dizini ve teknik limitler. |
| ✅ | `MESHUR_SAHNE_KALIPLARI_KILAVUZU.md` | 306 | İkonik sahne kalıbı: "Ayna Karşılaşması" (The Mirror Encounter). |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | Novum: TRAPPIST-1e Taklitçi Biyo-ışıldayan Varlıklar (Bio-luminescent Mimic Fauna). |
| ✅ | `PAKETLEME_VE_VAAT_KILAVUZU.md` | 241 | Kapak anı S09'dan seçilecek (Astronot ve varlığın dokunma anı). |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | Politika kelime engelleri, kompozisyon yüzeyi, aksiyon bütçesi. |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 420 | Ref paketi muafiyeti (PLAN'da gerekçeli). |
| ✅ | `SAHNE_DEVAMLILIK_KILAVUZU.md` | 383 | Karakter çapalama: Kask renkleri (Astronot A: Beyaz/Mavi, Astronot B: Beyaz/Turuncu). |
| ✅ | `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` | 433 | Sahne sınırı durumu: durum değişimi sınıra yazılır, ardışık aynı cevap yasaktır. |
| ✅ | `SAVAS_SENARYO_KILAVUZU.md` | 660 | Çevre tehdidi ve gerilim ritmi. |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | Viral kamera hareketleri (dikey/yatay kaydırma, mikro sarsıntı). |
| ✅ | `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` | 366 | Kanal evren modeli ve uzay bilimkurgu estetiği. |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 422 | Diyalog işlev sütunu, diyalog register'ı, telsiz cızırtısı audio kalıbı. |
| ✅ | `SHORTS_SISTEM_PROMPTU.md` | 268 | Prompt dili ve negatif prompt blokları. |
| ✅ | `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` | 759 | Lensler (35mm Anamorphic, 50mm Prime, 85mm Macro), ışık paleti (Violet Dusk / Cyan Bioluminescence). |
| ✅ | `SKILL_KULLANIM_KILAVUZU.md` | 152 | yeni-film skill akışı dayatması. |
| ✅ | `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` | 480 | Kesmesiz geçiş kilitleri. |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | Ana Tema: İLK-TEMAS / Yan Tema: KİMLİK. |
| ✅ | `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` | 1269 | Kuşbakışı harita, sol-sağ ekran yönü kilidi (Astronot A solda, Astronot B sağda, varlık merkezde). |
| ✅ | `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` | 376 | Uzaylı Varlık: Dört ayaklı (quadruped), sırtında esnek biyo-ışıklı antenler, pürüzsüz yarı saydam lavanta deri, yüzsüz (faceless). Reveal K0-K4. |
| ✅ | `UZAY_SENARYO_KILAVUZU.md` | 795 | Yabancı gezegen atmosferi, düşük yerçekimi aksiyonu, keşif aracı. |
| ✅ | `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` | 604 | Keşif Modülü / Araç ölçek şahidi: 1H = 1.8m kasklı astronot. |
| ✅ | `VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md` | 228 | Veo video jenerasyonu kuralları ve diyalog senkronu. |
| ✅ | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` | 388 | İngilizce vaat odaklı paketleme. |
| ✅ | `YANASMA_VE_KENETLENME_KILAVUZU.md` | 220 | Yakınlaşma dramaturjisi. |
| ✅ | `YAPI_GRAFI.md` | 459 | Karar ağacı. |
| ✅ | `YAYIN_VE_PERFORMANS_KILAVUZU.md` | 370 | Performans geribildirim ilkesi. |
| ✅ | `DIS_FILM_ANALIZI/00_README.md` | 140 | Dış analiz yöntemleri. |
| ✅ | `DIS_FILM_ANALIZI/KAMERA_ANALIZ_PROMPT.md` | 113 | Kamera dili analizi. |
| ✅ | `DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` | 237 | Nobody Was Alive ders seçkisi (The Last Shift / The Hollow Count dersleri). |
| ✅ | `DIS_FILM_ANALIZI/OLAY_ANALIZ_PROMPT.md` | 125 | Olay yapısı. |
| ✅ | `DIS_FILM_ANALIZI/SENTEZ_ANALIZ_PROMPT.md` | 175 | Sentez analizi. |
| ✅ | `DIS_FILM_ANALIZI/TEMA_ANALIZ_PROMPT.md` | 114 | Tema çözünürlüğü. |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1224 | Tamlık matrisine satır ekleme zorunluluğu. |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 213 | Motor red tetikleyicileri (çıplak deri, milliyet emtiyası engeli). |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | Anlatı kırılması olmaması için B5 omurgası kilidi. |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | Fiziksel devamlılık kilitleri. |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | Dikey kanca tecrübesi. |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | Karakter çapalama zayıflıklarının giderilmesi. |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | Telsiz diyalog kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | İzleyici tutundurma oranları. |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 46 | Beden dili ve kinesik ifade. |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 46 | Sahne arası monoton ışık azalışı engeli (D193). |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 46 | S00 hook dramatik ironi teyidi. |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 77 | Kare kompozisyonu ve nesne boyutu (≥100px). |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 96 | Gövde/giysi devamlılığı (Astronot A/B kask şeritleri). |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 83 | Atmosferik ses tasarımı. |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 85 | Novum görsel kanıtları. |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 92 | Derin kadraj uzaylı flora detayları. |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 77 | Yerçekimi ve akışkan fiziği devamlılığı. |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 60 | Kinetik hareket okunurluğu. |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 66 | Bedel ve fiziksel efor gösterimi. |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 46 | Plan sadakati ve lens uyumu. |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (53 dosya · 14581 satır)

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_STARLESS_CIRCLE.md` | ① aynı format | 18 sahneli yatay uzay anlatısı ritim ve ASLReferansı. |
| ✅ | `THE_COLD_WELD.md` | ② aynı ortam kartı | Yabancı yüzey ve kask vizör ışık yansıması dersleri. |
| ✅ | `THE_HERD.md` | ③ aynı tema | Sürü/varlık karşılaşması ve İlk-Temas novum dengesi. |
| ✅ | `THE_OPEN_CIRCUIT.md` | ④ en düşük skor | Lens genişliği ile nesne sığdırma hatasından kaçınma (optik aritmetik). |
| ✅ | `THE_STILL_SWARM.md` | ⑤ en yakın konsept | Çoklu varlık hareketi ve taklit kinetiği kilitleri. |

---

## 📊 ÇİZELGE ÖZETİ

```
ZORUNLU DOSYA:   102
ZORUNLU SATIR:   41947
SEÇMELİ KAYIT:   5 / 53  (TUR 5)
```

✅ Okuma tamamlandı. Tüm kilitler `01_QA_DERS_HASADI.md` dosyasına aktarılmaya hazır.
