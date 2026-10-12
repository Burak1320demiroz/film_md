# F5 · denetci (faz 5 kapısı) — THE_WRONG_BURN

> Girdi: KABUL_LISTELERI Ö + F5 · F5_devamlilik_1 · F5_teknik-danisman_1 · PROMPTLAR/G01.md · FILM §3 §4 · DURUM · NOTLAR · film_dogrula. Ajanın cevabı aynen (Fable kaydı, 09.10.2026).

**FAZ 5 KAPISI · yatay_2_dk_filmler/THE_WRONG_BURN**

Mekanik kontrolün çıktısı (`python3 uretim_hatti/araclar/film_dogrula.py yatay_2_dk_filmler/THE_WRONG_BURN --bolum cekim sahneleme prompt`):
```
film: yatay_2_dk_filmler/THE_WRONG_BURN · bölüm: cekim prompt sahneleme · çekim: 12
✅ yapı geçerli
EXIT=0
```

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 **M** zorunlu eleştiriler | ✅ | yeni-film SKILL.md:67, F5 eleştirmenleri "devamlilik · teknik-danisman". İki dosya da var: `ODA/F5_devamlilik_1.md` ve `ODA/F5_teknik-danisman_1.md`. |
| Ö2 **M** GİRDİ satırı, "EKSİK" yok | ✅ | devamlilik:158 `GİRDİ … PROMPTLAR/G01.md (tam: 18 referans + C01-C12 + FLOW İŞ EMRİ + YAZAR NOTLARI)`. teknik:132-138 GİRDİ dolu. İkisinde de "EKSİK" geçmiyor. Yapılamayanlar YAPILMADI satırında (devamlilik:159, teknik:139-143). |
| Ö3 her ÖLÜMCÜL/CİDDİ'ye cevap | ✅ | ÖLÜMCÜL 0+0. Cevap gereken CİDDİ 7 (devamlilik) + 6 (teknik). G01:640-666 tablosunda 27 satır var: devamlilik B1-B13 (640-652), teknik B1-B14 (653-666). Hepsinde KABUL ya da KISMEN yazılı. |
| Ö4 KABUL'ler uygulandı | ✅ | Önceki sürümü eleştirilerdeki birebir alıntılardan okudum. Eski ifadelerin hiçbiri kalmamış: G01'de `short`, `hangs`, `push`, `five percent`, `centre of the helmet`, `spreads outward`, `at her waist`, `orange-and-blue band` aramaları prompt gövdelerinde 0 sonuç verdi (yalnız YAZAR NOTLARI'nda geçiyorlar). Yeni ifadeler yerinde: D-B1/T-B1 iş emri 32 `BRAM_kontrolsuz · KANCA_cantada · DUNYA_alcak_ust`, kolkalkik yalnız 33'te, satır 29 ve 31'de BRAM_v1 yok · D-B2/T-B2 G01:35 `A bare metal ring at her right hip … wrists stay below the lower edge of the frame`, iş emri 23'te SELA_v1 yok, G01:374 `her wrist hidden behind the glove and the box` · D-B3 G01:554 `camera at handrail height at the edge of the open hatch` ve `reaches back to the grab handle on the hatch rim nearer the camera`, G01:79 ve 259 `grab handle on the rim beside the handrail` · D-B4 G01:328 `high at the left, well above the horizon`, G01:101 `from directly above` · D-B5 `about four person-heights long` 211/222/282/489/531/554 · D-B6 G01:46 ve iş emri 25-26 · D-B7/T-B13 G01:489 `above the line of the rope, a hand's width clear of it` · D-B8 G01:429/489/531/554 `on top of the helmet` · D-B10 G01:398 `her lips closed` · D-B12 G01:145/167/429/434/554/559 `glow` · D-B13/T-B14 G01:531 · T-B3 G01:287/379/559 tutuş cümleleri, `moves steadily` / `shifts sharply … once` · T-B4 G01:145 ve 429 `rolled so that its lowest point meets the left edge … at the height of her face` · T-B5 G01:465 ve 470 · T-B6 G01:57, iş emri 24/31/34/35 · T-B7 12 bloğun hepsinde `KARE (Görsel)` ve `VİDEO (Frames to Video)` ayrı satır · T-B8 G01:434 `stays dark and the same size`, G01:447 · T-B9 G01:393 ve 416, iş emri 28 YEDEK · T-B10 G01:398 · T-B11 G01:264 `stays where it is` · T-B12 G01:434 ve 559. |
| Ö5 RED gerekçeleri kanıta cevap veriyor | ✅ | Tam RED yok. Tek kısmi RED G01:664'te, teknik B12'nin önerdiği "blooms" sözcüğü: "bloom, BILINEN/ATLAS A14'te vakumda parıltı çağıran sözcük". Dayanak dosyada var: `PROMPT_HATA_ATLASI.md:149` "yazılı yasağa rağmen bloom", :153 "bloom 6 filmde". Bulgunun asıl derdi olan hacimsel ışık, ışık güneşe bağlanarak yine giderilmiş (G01:434). Not: A14'ün konusu olumsuz cümle; atıf dolaylı. |
| Ö6 açık ÖLÜMCÜL yok | ✅ | devamlilik:156 `ÖLÜMCÜL 0`, teknik:130 `ÖLÜMCÜL 0`. devamlilik B1'in koşulu (uygulanmazsa ÖLÜMCÜL) tutmuyor, çünkü B1 uygulandı (iş emri 32). |
| Ö7 **M** DURUM güncel | ✅ | DURUM:8-14 `FAZ 5 · TUR 1 · AJAN_CAGRI 44 / 50 · SIRADAKI F5 kapı … → denetci`. Sayacı AJAN GÜNLÜĞÜ'nden saydım: F4 denetçi sonrası 41 (F4_denetci:17 "40" + denetçi), F5'te 3 sayılan satır (NOTLAR:130-132) var, toplam 44. Satır 133 SendMessage olduğu için sayılmıyor. |
| F5.1 **M** prompt bölümü | ✅ | film_dogrula `✅ yapı geçerli`, EXIT=0. |
| F5.2 devamlilik ÖLÜMCÜL açık değil | ✅ | ÖLÜMCÜL 0. KORU satırlarında (devamlilik:140-145) dünya cümlesinin 12/12 birebir, taraf/yön ve FILM §3 ile eşleşme kontrol edilmiş. |
| F5.3 teknik risk sütunu dolu çekimlere baktı | ✅ | FILM §4'te 12/12 çekimin Risk hücresi dolu (FILM:102-113). Teknik Risk'i alıntılıyor: C02, C06, C12 (teknik:35) ve C09 (teknik:49). C01 (B11), C03 (KORU:116), C04 (B6), C05 (B6 notu), C07 (B9, B10), C08 (B4, B8, B12), C10 (B1, B13), C11 (B14) bulgularda geçiyor. |
| F5.4 **M** Flow iş emri | ✅ | G01:579-628, 48 satır. Her video satırında dosya, mod ve kare var: 36-48 `ham/C01_d1.mp4` … `ham/C12_d1.mp4`, `Frames to Video`, `başlangıç kare/Cnn.png`. Kare satırları 21-35, referanslar 1-20. |
| F5.5 **M** zincir | ✅ (uygulanmaz) | Zincir yok: G01:6 "Zincir yok (SAHNELEME §1)", FILM §4 Zincir sütunu 12/12 `—`. Zincir dili de yok: `previous clip` ve `last frame` aramaları 0 sonuç. |
| Yerleştirme (FILM §3) | ✅ | FILM:72-73, G01:693-694 ile karakter karakter aynı. SELA_v1 `C01 · C02 · C05 · C06 · C07 · C08` ve BRAM_v1 `C01 · C11 · C12` (FILM:71, 74), G01:680-681 ile aynı. Yorum satırı FILM:67'de. |
| NOTLAR kayıtları | ✅ | KARARLAR:63 "FILM §4 SAPMA (14 madde)", KARARLAR:64 "F5 tur 1 KAPANIYOR". AJAN GÜNLÜĞÜ:130-133 dört F5 satırı. |

```
MEKANİK ❌   yok
YARGI ❌     yok
SONUÇ        KAPANABİLİR
```

**Notlar (❌ değil, kayıt ve risk):**
1. **Önceki sürüm saklanmamış.** G01 birleştirme geçişinde yerinde yeniden yazılmış (NOTLAR:133 "711 satır, yerinde"). Klasör git'te takipsiz (`?? yatay_2_dk_filmler/THE_WRONG_BURN/`), ODA'da da tur 1 kopyası yok. Bu yüzden `git diff` yapılamadı. Ö4'ü yalnız eleştirmenlerin birebir alıntılarına dayanarak doğruladım. Görevde "önceki sürüm" olarak verilen şablon (`uretim_hatti/SABLON/PROMPTLAR/G01.md`) bu karşılaştırmaya yaramıyor. Önceki fazlarda yazar sürümleri ODA'da `_1`, `_2` diye tutuluyordu.
2. **FILM.md içinde §3 ile §4 artık tutarsız.** §4 Referans sütunu hâlâ eski listeyi taşıyor: C03 `SELA_v1 · BILEK_2-2_v1 …` (FILM:104), C08 ve C09 `BRAM_v1` (FILM:109-110), C10 `BRAM_v1 · … BRAM_kolkalkik_v1` (FILM:111). §3 ise güncel. Bu bilinçli bir sapma (G01 SAPMA 10 ve 14, Fable kararı 6). Ama F7'de §4'e bakan biri çıkarılmış referansları, C10 başlangıç karesine kolkalkik dahil, geri ekleyebilir. Uygulanacak belge iş emri olmalı.
3. **Birleştirilmiş sürümü hiçbir eleştirmen görmedi.** İki yeni referans promptu (G01:46, 57), C08 limb dönüşü ve C04 güneş cümlesi bütçe yüzünden yeniden eleştiriye girmedi (Fable kararı, teknik:150). Ö4 yalnız "KABUL uygulandı mı" sorusunu sınar; değişikliğin yeni ÖLÜMCÜL doğurup doğurmadığı sınanmadı.
4. **Kısmen giderilmiş kalıntı.** C04'ün referansı DUNYA_gunduz_alt_v1 hâlâ `The sun is directly overhead` diyor (G01:112). C04 metni ise "two-thirds of the way down from overhead" (G01:328). devamlilik B4'ün NEDEN'inde bu çelişki var, ama ÖNERİ'si yalnız C04 metnini ve ISTASYON'u kapsıyordu. Önerilen düzeltme uygulanmış, referans–metin çelişkisi C04'te sürüyor.
5. **FAZ GÜNLÜĞÜ'nde F5 satırı yok** (DURUM:43-59). Ö7'nin zorunlu dört alanı tam olduğu için ❌ saymadım. F3b ve F4 kapılarında da aynı not düşülmüştü.

---

## Fable kararı (09.10.2026)

**F5 KAPANDI.** Aşılan kapı yok. FILM §4 Durum sütunu 12/12 → ✍️ (cekim-yaz §F5.5).

Denetci notları:
1. **Önceki sürüm saklanmadı** → hat dersi (NOTLAR KARARLAR, bellek): bundan sonra birleştirme geçişinden önce `PROMPTLAR/<grup>.md` kopyası `ODA/F5_<grup>_tur1.md` olarak alınır. Bu filmde tur 1 metni eleştirilerdeki birebir alıntılarla kayıtlı; geri alınamaz, kabul.
2. **§4 Referans sütunu ↔ §3/iş emri:** F7'de uygulanacak belge **G01 FLOW İŞ EMRİ**'dir. FILM §4 başlığının altına Fable yorum satırı eklendi (metin değişmedi). Sahip listesinde de yazar.
3. **Birleştirilmiş sürüm eleştirilmedi** → kabul edilen risk (bütçe 45/50); F7'de devamlilik kare denetimi (referans ↔ başlangıç karesi) ve teknik ret sınıflaması bu boşluğu kapatır. Yeni iki referans ve C08 limb dönüşü F7 ilk karelerinde ölçülür.
4. **DUNYA_gunduz_alt_v1 güneş cümlesi ("directly overhead") ↔ C04 metni (65°):** referans C01-C04'ün ortak Dünya plakası; C01 zenit, C04 65°. Yazara yeni geçiş açılmadı (dosya yeniden yazımı riski + bütçe). F7 kuralı (sahip listesi + NOTLAR): kare üretiminde referansla metin çelişirse **metin esas**; C04 karesinde Dünya aydınlık yüzü referanstan, güneş yönü prompttan. İlk C04 karesi okunmazsa goruntu-yonetmeni F7 yeniden tasarımında referansı böler.
5. **FAZ GÜNLÜĞÜ F5 satırı** yazıldı.
