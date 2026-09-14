# 📖 THE_HARD_DOCK — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 11.09.2026 17:00
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
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` | 81 | DERS_YAZIM: Kapı kuralları tam uygulanacak. |
| ✅ | `DERSLER/00_HIZLI_REFERANS.md` | 188 | HIZLI_REF: 10s klip ve 8+2s üretimi. |
| ✅ | `DERSLER/01_KAMERA_VE_KESME.md` | 266 | D32: V3 iki gövdeli kadraj yalnızca 1 kez (S09) kullanılır. |
| ✅ | `DERSLER/02_KARAKTER_VE_CANLI.md` | 513 | D197: vizör TEK nitelik cümlesiyle kilitlenir — bu filmde BERRAK düz panel (D5/D79/D95/D146 ile aynı yön); opak/aynalı 0 kez. |
| ✅ | `DERSLER/03_FIZIK_VE_HAREKET.md` | 886 | D198: Sıfır-g aksesuarlar tork ve rotasyonel salınım sergiler. |
| ✅ | `DERSLER/04_ISIK_VE_CEVRE.md` | 314 | D201: güneş kadrana bağlanır — istasyonun arkasında, eksenin ~30° üstünde, kadraj dışı; 24/24 sabit. |
| ✅ | `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | 750 | D104: doruk (S22) kamerası PORTA kilitli, gemi kadraja girer; temas sahne içinde 6,0 s [B1]. |
| ✅ | `DERSLER/06_METIN_VE_PROMPT_DILI.md` | 1279 | METİN: prompt gövdesinde metre/derece yok (yalnız kamera cümlesi); oranlar halka/kask/avuç/gemi boyuyla [D138]. |
| ✅ | `DERSLER/07_KURGU_VE_ANLATI.md` | 1177 | D202: Karakterin seçimi beden dilinde mikrosaniyelik gecikmeyle okunur. |
| ✅ | `DERSLER/08_QA_SURECI.md` | 4652 | QA: Rubrik mod D (SPEC ile) değerlendirilir. |
| ✅ | `DERSLER/09_SISTEM_VE_SUREC.md` | 830 | SİSTEM: Defter ve sayaç uyumu sağlanır. |
| ✅ | `DERSLER/GOZLEM_DEFTERI.md` | 1876 | GÖZLEM: Gözlem defteri aday kapıları tarandı. |

### TUR 2 · ÜRETİM ÖNCESİ ANALİZ — teşhis ve risk

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `URETIM_ONCESI_ANALIZ/00_README.md` | 234 | README: Analiz akışı adımları sırayla uygulanır. |
| ✅ | `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` | 337 | ETKİNLİK: Derslerin sadakat oranı takip edilir. |
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 585 | RİSK: 1 numaralı risk (kenetlenme yalpalaması) sayıyla tanımlanır. |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 508 | KONTROL: 14 maddelik kontrol listesi sıfır maliyetle tamamlandı. |
| ✅ | `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` | 2583 | BULGU: Sezgi vs optimizasyon çatışması bağlamı. |
| ✅ | `URETIM_ONCESI_ANALIZ/05_DIKEY_HAT_TESHISI.md` | 517 | TEŞHİS: Şablonlaşma riskine karşı özgün novum kilitlendi. |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | HİKAYE: B5 omurgası net sahne numaraları taşır. |
| ✅ | `URETIM_ONCESI_ANALIZ/07_POLITIKA_ARASTIRMA_PROMPTLARI.md` | 162 | POLİTİKA: Üretim ihlali yaratacak nesne ismi kullanılmaz. |
| ✅ | `URETIM_ONCESI_ANALIZ/08_SENARYO_ARASTIRMA_PROMPTLARI.md` | 179 | SENARYO: Tematik motifler kadraja yedirilir. |
| ✅ | `URETIM_ONCESI_ANALIZ/09_KARAKTER_DONANIM_ARASTIRMA_PROMPTLARI.md` | 88 | DONANIM: Astronot giysi detayları tutarlıdır. |
| ✅ | `URETIM_ONCESI_ANALIZ/10_DIYALOG_ARASTIRMA_PROMPTLARI.md` | 207 | DİYALOG: AI dili akuzmatik, soğuk ve telemetrik tutulur. |
| ✅ | `URETIM_ONCESI_ANALIZ/11_UZAYLI_TASARIM_ARASTIRMA_PROMPTLARI.md` | 131 | — |
| ✅ | `URETIM_ONCESI_ANALIZ/12_UZAY_USSU_ARASTIRMA_PROMPTLARI.md` | 161 | İSTASYON: 1H kasklı gövde ölçek birimi uygulanır. |
| ✅ | `URETIM_ONCESI_ANALIZ/13_GIRIS_VE_FINAL_ARASTIRMA_PROMPTLARI.md` | 163 | FİNAL: Açılış-Kapanış Çifti Kafiye yapısı (S01/S24). |
| ✅ | `URETIM_ONCESI_ANALIZ/14_OLCULMUS_ARIZALAR_ARASTIRMA_PROMPTLARI.md` | 125 | ARIZA: Ölçülmüş fizik ve devamlılık hataları engellenir. |
| ✅ | `URETIM_ONCESI_ANALIZ/15_REFERANS_PAKETI_ARASTIRMA_PROMPTLARI.md` | 113 | REF: Giysi ve vizör referans paketi kilitlenir. |
| ✅ | `URETIM_ONCESI_ANALIZ/16_UZUN_TEK_KISI_HAYATTA_KALMA_ARASTIRMA_PROMPTLARI.md` | 187 | TEK KİŞİ: İç monolog ve AI etkileşimi dinamikleri. |
| ✅ | `URETIM_ONCESI_ANALIZ/17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` | 147 | EKSEN: Çözüm odaklı mühendislik kararları. |
| ✅ | `URETIM_ONCESI_ANALIZ/18_OYUNCULUK_VE_KARAKTER_ARASTIRMA_PROMPTLARI.md` | 206 | OYUNCULUK: Mikro beden hareketleri ve nefes ritmi. |
| ✅ | `URETIM_ONCESI_ANALIZ/19_THE_SCOURED_GLASS_NOVUM_KAYNAK_GORUS_ARASTIRMA_PROMPTLARI.md` | 204 | NOVUM: Mekanik engel novumu kilitlendi. |
| ✅ | `URETIM_ONCESI_ANALIZ/PROB_KOSUSU.md` | 261 | PROB: Test ve kontrol adımları. |

### TUR 3 · KILAVUZLAR — hepsi

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `5_FAZ_MIMARISI.md` | 245 | FAZ: 5 Fazlı mimari akışı uygulandı. |
| ✅ | `ACILIS_KAPANIS_CIFTI_KILAVUZU.md` | 260 | ÇİFT: S01 ile S24 kafiye ilişkisi kurar (vizör parıltısı). |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | AÇI YAYI: Sıçrama bantları ve açı çeşitliliği sağlandı. |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 367 | DONANIM: Kask, vizör ve göğüs amblemi kimlik kartı. |
| ✅ | `DIKEY_MIKRO_DRAMA_KILAVUZU.md` | 473 | — |
| ✅ | `DIS_REFERANS_OLCUMU.md` | 198 | DİŞ REF: Görsel referans oranları doğrulandı. |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 384 | DİYALOG: Akuzmatik AI muhatap tipolojisi. |
| ✅ | `FAZ_DOSYASI_SABLONU.md` | 281 | FAZ ŞABLON: Faz yapılandırılması. |
| ✅ | `FINAL_VE_PAYLASIM_KILAVUZU.md` | 420 | FİNAL: Tahrip edici kenetlenme (impact capture) finali. |
| ✅ | `FRAGMAN_KILAVUZU.md` | 548 | FRAGMAN: Spoiler vermeyen 8 vuruşluk yapı. |
| ✅ | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` | 580 | MÜZİK: Endüstriyel gerilim ve yükselen frekans tırmanışı. |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | HOOK: S01 Anomali reveal ile başlar. |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | İKİ KİŞİ: İnsan ve AI vizyon ayrılığı (S17). |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 306 | PROMPT: V2 prompt şablon yapısı uygulandı. |
| ✅ | `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` | 205 | KAMERA: Dar açı ve geniş açı psikolojik etkisi. |
| ✅ | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | 155 | KAPAK: S14 gezegen kadrajı kapak seçildi. |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | KARAKTER: Astronot ve MIRA AI kartları. |
| ✅ | `KARAKTER_VE_DUYGU_KILAVUZU.md` | 462 | DUYGU: Beden ve el hareketlerinde mikro-gecikmeler. |
| ✅ | `KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` | 37 | KESİNTİSİZ: Akıcı sahne geçiş kuralları. |
| ✅ | `KILAVUZ_REHBERI.md` | 2028 | KILAVUZ: §2.3 yatay 3-5 dk format kartı (24 sahne × 10s). |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | RİTM: ASL eğrisi ve vuruş temposu. |
| ✅ | `KURGU_VE_TESLIM_KILAVUZU.md` | 225 | TESLİM: 10 maddelik kurgu kapısı ve kırpma bütçesi. |
| ✅ | `LESSONS_LEARNED.md` | 471 | DERSLER: Son 5 ders ve kritik kurallar. |
| ✅ | `MESHUR_SAHNE_KALIPLARI_KILAVUZU.md` | 306 | KALIP: Docking manevra kalıpları. |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | NOVUM: Yalpalayan istasyona çarparak kilitlenme mekanizması. |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 461 | OYUNCULUK: Çapa üçlüsü ve beden dili yazımı. |
| ✅ | `PAKETLEME_VE_VAAT_KILAVUZU.md` | 241 | PAKETLEME: Vaat-teyit dengesi. |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | POLİTİKA: Kompozisyon düzeyi üretilebilirlik sınırları. |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 420 | REF PAKETİ: T1 vizör/giysi kilitleri uygulandı. |
| ✅ | `SAHNE_DEVAMLILIK_KILAVUZU.md` | 383 | DEVAMLILIK: Işık, uzay ve nesne devamlılığı. |
| ✅ | `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` | 433 | SAHNE ZİNCİRİ: Ardışık sahneler arası durum değişimi. |
| ✅ | `SAVAS_SENARYO_KILAVUZU.md` | 660 | — |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | VIRAL: Kanca ve gerilim kadrajları. |
| ✅ | `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` | 366 | STRATEJİ: Apex AI C2PA ve marka kimliği. |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 422 | SES: AI akuzmatik sesi, telsiz cızırtısı ve alarm frekansları. |
| ✅ | `SHORTS_SISTEM_PROMPTU.md` | 268 | — |
| ✅ | `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` | 759 | SİNEMA: 35mm ve 85mm anamorfik lens simülasyonu. |
| ✅ | `SKILL_KULLANIM_KILAVUZU.md` | 152 | SKILL: Süreç skill eşlemeleri. |
| ✅ | `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` | 480 | — |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | TEMA: İNSAN-MAKİNE + FEDAKÂRLIK teması. |
| ✅ | `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` | 1269 | UZAM: Kokpit sol, istasyon sağ eksen kilitleri. |
| ✅ | `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` | 376 | — |
| ✅ | `UZAY_SENARYO_KILAVUZU.md` | 795 | UZAY: Sıfır-g ve vakum fizik yasaları. |
| ✅ | `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` | 604 | ÜS MİMARİSİ: Yalpalayan güneş panelleri ve modül anatomisi. |
| ✅ | `VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md` | 228 | VEO: Video prompt yazım standartları. |
| ✅ | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` | 388 | PAKETLEME: Sosyal medya metin şablonları. |
| ✅ | `YANASMA_VE_KENETLENME_KILAVUZU.md` | 220 | YANAŞMA: Yanaşma vuruş seti (S09-S24). |
| ✅ | `YAPI_GRAFI.md` | 459 | YAPI: Karar ağacı haritalaması. |
| ✅ | `YAYIN_VE_PERFORMANS_KILAVUZU.md` | 370 | YAYIN: Performans takip kriterleri. |
| ✅ | `DIS_FILM_ANALIZI/00_README.md` | 140 | DİŞ ANALİZ: Dış analiz standartları. |
| ✅ | `DIS_FILM_ANALIZI/KAMERA_ANALIZ_PROMPT.md` | 113 | — |
| ✅ | `DIS_FILM_ANALIZI/NOBODY_WAS_ALIVE_DERS_SECKISI.md` | 237 | NOBODY: Dış film teknik ders seçkisi. |
| ✅ | `DIS_FILM_ANALIZI/OLAY_ANALIZ_PROMPT.md` | 125 | — |
| ✅ | `DIS_FILM_ANALIZI/SENTEZ_ANALIZ_PROMPT.md` | 175 | — |
| ✅ | `DIS_FILM_ANALIZI/TEMA_ANALIZ_PROMPT.md` | 114 | — |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1150 | INDEX: Tamlık matrisi kontrolleri. |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 213 | RED DEFTERİ: Kompozisyon red riskleri engellendi. |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | HİKAYE: Hikaye kalitesi kriterleri. |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | MANTIK: Mantık ve fizik tutarlılık kriterleri. |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | KARAKTER: Karakter devamlılık kriterleri. |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | SES: Ses ve diyalog senkronizasyon kriterleri. |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | YAYIN: İzleyici performans ölçütleri. |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 46 | OYUNCULUK: Karakter beden dili kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 46 | IŞIK: Işık tutarlılığı ve gölge kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 46 | HOOK: İlk 3 saniye kanca performansı. |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 79 | UYUM: Prompt ↔ video uyum kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 84 | KARE: Sahne içi görsel devamlılık. |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 116 | DEVAMLILIK: Sahneler arası devamlılık. |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 96 | SES: Ses tasarımı kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 91 | HİKAYE: Anlatı bütünü kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 105 | ARKA PLAN: Arka plan detay tutarlılığı. |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 92 | FİZİK: Yerçekimi ve vakum fiziği kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 74 | AKSİYON: Hareket okunurluğu kalitesi. |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 74 | EFOR: Karakter efor görünürlüğü. |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 46 | KADRAJ: Kamera plan sadakati. |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (63 dosya · 16116 satır)

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_COUNTED_TURN.md` | ① aynı format (yatay 3-5) | Sahne geçiş hızı ve kurgu ritmi kilitlendi. |
| ✅ | `THE_GRAVITY_ANCHOR.md` | ② aynı ortam (uzay) | Sıfır-g nesne hareketleri ve süzülme fiziği kilitlendi. |
| ✅ | `THE_MIRROR_FAUNA.md` | ③ aynı tema (insan-makine) | Yapay zeka ve insan karar çatışması derinliği. |
| ✅ | `THE_DRY_ANCHOR.md` | ④ en düşük skorlu aksiyon kaydı | Yanıltıcı ışık değişimleri engellenecek. |
| ✅ | `THE_AMBER_LATTICE.md` | ⑤ en yakın konsept (istasyon) | İstasyon orbital hareketi ve kadraj stabilitesi. |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
ZORUNLU DOSYA:   109
ZORUNLU SATIR:   46232
SEÇMELİ KAYIT:   5 / 63  (TUR 5)
```

⚠️ **Bu bir oturumluk iş değildir ve olmaması normaldir.** Okuma
yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
