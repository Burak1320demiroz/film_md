# 📖 THE_TETHERED_MASS — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 10.09.2026 23:08
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
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` | 74 | Kilit prompta etiketsiz taşınır `[LESSON n]` kopyalanmaz [D45] |
| ✅ | `DERSLER/00_HIZLI_REFERANS.md` | 188 | Optik aritmetiği: Ana nesne en az 100px olmalı |
| ✅ | `DERSLER/01_KAMERA_VE_KESME.md` | 266 | Ardışık çift denetimi: En az 1 kademe ölçek + 45 derece açı değişimi |
| ✅ | `DERSLER/02_KARAKTER_VE_CANLI.md` | 513 | Astronot basınç giysisi kask vizörü şeffaflık/opaklık tutarlılığı [D197] |
| ✅ | `DERSLER/03_FIZIK_VE_HAREKET.md` | 886 | Sıfır-G momentum aktarımı, vakumda mikro arklar, sürtünmesiz halat [D198, D200] |
| ✅ | `DERSLER/04_ISIK_VE_CEVRE.md` | 314 | Vakumda güneş ışığı açısı komşu sahnelerde flip etmemeli [D201] |
| ✅ | `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | 750 | Halat lifleri ve tambur kilit mekanizması varlık sürekliliği [D146] |
| ✅ | `DERSLER/06_METIN_VE_PROMPT_DILI.md` | 1279 | Pozitif kilit kullanımı, yasak sözcüklerden kaçınma [D67, D123] |
| ✅ | `DERSLER/07_KURGU_VE_ANLATI.md` | 1177 | Merkezi seçim ve bedel bedende/eylemde okunmalı (görünmez seçim yasağı) [D202] |
| ✅ | `DERSLER/08_QA_SURECI.md` | 4640 | SPEC bağımsız dry run ve kurgu kapıları |
| ✅ | `DERSLER/09_SISTEM_VE_SUREC.md` | 822 | Üretim sırası: Doruk -> seçim -> kapanış -> S0 -> kalan |
| ✅ | `DERSLER/GOZLEM_DEFTERI.md` | 1876 | Kask içi solunum ve ekran yansımaları sürekliliği |

### TUR 2 · ÜRETİM ÖNCESİ ANALİZ — teşhis ve risk

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `URETIM_ONCESI_ANALIZ/00_README.md` | 135 | Analiz dizini disiplini ve kapı kontrolleri |
| ✅ | `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` | 337 | Bedel ve seçim sahnelerinde visual evidence zorunluluğu |
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 585 | Metal halat mikro tel kopma riski (halat lif kayması) |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 508 | 14 maddelik kontrol listesi B1-B14 doğrulaması |
| ✅ | `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` | 2053 | Momentum transferi ve orbital mekanik saha bulguları |
| ✅ | `URETIM_ONCESI_ANALIZ/05_DIKEY_HAT_TESHISI.md` | 517 | Mekanizmanın hikâye formatına dönüşmesi (Bedel & İnsan-Makine) |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5 dörtlüsü: İstek, Engel, Bedel (S11), Muhatap (Sistem) |
| ✅ | `URETIM_ONCESI_ANALIZ/07_POLITIKA_ARASTIRMA_PROMPTLARI.md` | 162 | Güvenlik kapağı kırma pozitif aksiyon tanımı |
| ✅ | `URETIM_ONCESI_ANALIZ/08_SENARYO_ARASTIRMA_PROMPTLARI.md` | 179 | Vuruş haritası ve kinetik bağımsızlık |
| ✅ | `URETIM_ONCESI_ANALIZ/09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` | 88 | Astronot donanım şeridi ve kask vizörü |
| ✅ | `URETIM_ONCESI_ANALIZ/10_DIYALOG_ARASTIRMA_PROMPTLARI.md` | 207 | Diyalogsuz anlatıda visual indicators |
| ✅ | `URETIM_ONCESI_ANALIZ/11_UZAYLI_TASARIM_ARASTIRMA_PROMPTLARI.md` | 131 | — |
| ✅ | `URETIM_ONCESI_ANALIZ/12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` | 161 | Tarım-habitat istasyonu modüler ölçek şahidi (1H) |
| ✅ | `URETIM_ONCESI_ANALIZ/13_GIRIS_VE_FINAL_ARASTIRMA_PROMPTLARI.md` | 163 | Hook tel lifi ile final kopmuş halat lifi kafiyesi |
| ✅ | `URETIM_ONCESI_ANALIZ/14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` | 125 | Klip içi durum değişimi sınıra yazılır |
| ✅ | `URETIM_ONCESI_ANALIZ/15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` | 113 | T1 kask vizörü + T3 halat tamburu referans kilitleri |
| ✅ | `URETIM_ONCESI_ANALIZ/16_UZUN_TEK_KISI_HAYATTA_KALMA_ARASTIRMA_PROMPTLARI.md` | 183 | Yalnız astronot aksiyon bütçesi |
| ✅ | `URETIM_ONCESI_ANALIZ/17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` | 143 | Mühendislik temelli sorun çözme akışı |
| ✅ | `URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md` | 261 | — |

### TUR 3 · KILAVUZLAR — hepsi

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `5_FAZ_MIMARISI.md` | 245 | Faz dosyası kilitleri |
| ✅ | `ACILIS_KAPANIS_CIFTI_KILAVUZU.md` | 260 | İlk kare gergin halat lifi -> Son kare dönen serbest halat ucu |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | Kurulum iskeleti (16 sahne: A A B C B C D E E C D A B C E A) |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 367 | Rol şeridi, göğüs paketi, bilek bilgisayarı kilidi |
| ✅ | `DIKEY_MIKRO_DRAMA_KILAVUZU.md` | 473 | — |
| ✅ | `DIS_REFERANS_OLCUMU.md` | 198 | Ölçek şahidi: 1H astronot gövdesi = 1.8m |
| ✅ | `FAZ_DOSYASI_SABLONU.md` | 281 | — |
| ✅ | `FINAL_VE_PAYLASIM_KILAVUZU.md` | 420 | Görsel ikilem: Atmosfere giriş ateşi yansıması |
| ✅ | `FRAGMAN_KILAVUZU.md` | 548 | — |
| ✅ | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` | 580 | 60 BPM ambient drone, sub-bass 28Hz |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | Visual hook: Vakumda gerilen halat lifinin mikro kıvrılışı |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 306 | V2 prompt yapısı |
| ✅ | `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` | 205 | Çekici kokpiti klostrofobik dar açı vs Uzay geniş açı |
| ✅ | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | 155 | Kapak anı: S11 Halat kopma / patlama anı |
| ✅ | `KARAKTER_VE_DUYGU_KILAVUZU.md` | 462 | Nefes, titreyen el ve vizör yansımasında kriyo kapsülleri |
| ✅ | `KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` | 37 | — |
| ✅ | `KILAVUZ_REHBERI.md` | 1998 | Yatay 2-4 dk format kartı (§2.2), Novum matrisi (§8) |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | ASL eğrisi ve kurgu temposu |
| ✅ | `KURGU_VE_TESLIM_KILAVUZU.md` | 225 | 10 maddelik kurgu kapısı |
| ✅ | `LESSONS_LEARNED.md` | 471 | Teknik kalite kontrol maddeleri |
| ✅ | `MESHUR_SAHNE_KALIPLARI_KILAVUZU.md` | 306 | Kalıp #14: Bedenle engel olma / Manuel kilit devreden çıkarma |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | Novum: Momentum Exchange Tether |
| ✅ | `PAKETLEME_VE_VAAT_KILAVUZU.md` | 241 | Vaat-teyit: Çekicinin fedakarlığı karşılığı istasyonun kurtuluşu |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | Motor patlaması/soğutucu sızıntısı tarifi (ateş/alev yasağı) |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 420 | T1 (Astronot kaskı) & T3 (Momentum halat tamburu) pakedi |
| ✅ | `SAHNE_DEVAMLILIK_KILAVUZU.md` | 383 | Dünya atmosfer çizgisi oryantasyon sürekliliği |
| ✅ | `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` | 433 | Sahne sınırı: Halat release anı S11-S12 sınırında |
| ✅ | `SAVAS_SENARYO_KILAVUZU.md` | 660 | — |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | Kinetik dinamik kamera hareketleri |
| ✅ | `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` | 366 | Uzay serisi kanal dili |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 422 | Diyalogsuz ses dramaturjisi (nefes, alarm, sessizlik) |
| ✅ | `SHORTS_SISTEM_PROMPTU.md` | 268 | — |
| ✅ | `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` | 759 | 24mm prime vs 85mm lens seçimi |
| ✅ | `SKILL_KULLANIM_KILAVUZU.md` | 152 | yeni-film ve prompt-kontrol akışı |
| ✅ | `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` | 480 | — |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | Tema: BEDEL (Ana) + İNSAN-MAKİNE (İkincil) |
| ✅ | `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` | 1269 | Çekici Solda/Aşağıda, İstasyon Sağda/Yukarıda, Dünya Aşağıda |
| ✅ | `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` | 376 | — |
| ✅ | `UZAY_SENARYO_KILAVUZU.md` | 795 | Yörünge fiziği ve vakum kuralları |
| ✅ | `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` | 604 | Koloni tarım-habitat istasyonu mimarisi (1H şahitli) |
| ✅ | `VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md` | 228 | Veo prompt standartları |
| ✅ | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` | 388 | Paketleme ve başlık formatı |
| ✅ | `YANASMA_VE_KENETLENME_KILAVUZU.md` | 220 | Acil durum halat bağlantı modülü |
| ✅ | `YAPI_GRAFI.md` | 459 | Karar ağacı |
| ✅ | `YAYIN_VE_PERFORMANS_KILAVUZU.md` | 370 | Performans metrikleri |
| ✅ | `DIS_FILM_ANALIZI/00_README.md` | 140 | — |
| ✅ | `DIS_FILM_ANALIZI/KAMERA_ANALIZ_PROMPT.md` | 113 | — |
| ✅ | `DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` | 237 | — |
| ✅ | `DIS_FILM_ANALIZI/OLAY_ANALIZ_PROMPT.md` | 125 | — |
| ✅ | `DIS_FILM_ANALIZI/SENTEZ_ANALIZ_PROMPT.md` | 175 | — |
| ✅ | `DIS_FILM_ANALIZI/TEMA_ANALIZ_PROMPT.md` | 114 | — |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1256 | Tamlık matrisi takibi |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 213 | Motor alevi / patlaması red sınıfları |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | B5 omurga puanlaması |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | Yörünge fiziği mantık kontrolü |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | Beden dili okumaları |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | Ses haritası sürekliliği |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | Görüntü vaadi teyidi |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 46 | Beden hareketi ve karar anı ifadesi |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 46 | Kokpit vs dış mekan ışık sürekliliği |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 46 | İlk 3 saniye kanca gücü |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 83 | Görsel kompozisyon ve netlik |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 102 | Ekran yönü ve uzamsal harita sürekliliği |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 88 | Vakum sessizliği ve sub-bass |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 90 | Dramatik yapı ve Bedel hissedilirliği |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 99 | Arka plan Dünya/Atmosfer sürekliliği |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 84 | Halat gerilimi ve sıfır-g hareket fiziği |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 66 | Manuel kol çekme aksiyonu okunurluğu |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 66 | Manuel kilit kırma fiziksel eforu |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 46 | Kadraj sadakati |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (59 dosya · 15723 satır)

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_GRAVITY_ANCHOR` | ① aynı format | Kask içi solunum ve vizör ışık yansıması sürekliliği |
| ✅ | `THE_HOLLOW_STATION` | ② aynı ortam kartı | İstasyon mimarisi ve 1H ölçek şahidi kullanımı |
| ✅ | `THE_COLD_WELD` | ③ aynı tema (BEDEL) | Fedakarlık anında beden dilinin tek başına kararı taşıması |
| ✅ | `THE_SINKING_STAKE` | ④ en düşük skor | Referans pakedi eksikliğinden doğan göğüs paketi tutarsızlığını önleme |
| ✅ | `THE_OPEN_CIRCUIT` | ⑤ en yakın konsept | Lens seçimi ve üssün kadraja sığma optik aritmetiği kontrolü |

---

## 📊 ÇİZELGE ÖZETİ

```
ZORUNLU DOSYA:   102 (TAMAMI İNCELENDİ VE KİLİTLER HARMANLANDI)
ZORUNLU SATIR:   43472
SEÇMELİ KAYIT:   5 / 59  (TUR 5 KAPSAMINDA İNCELENDİ)
```
