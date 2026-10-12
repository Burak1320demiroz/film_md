# Geçiş ve ses sürekliliği — klipler arası kesme kılavuzu

> Sahip, 12.10.2026: "Sahne geçişleri çok keskin oluyor; klipten diğer klibe geçince arkadaki ses komple
> değişiyor." Bu dosya o iki arızanın çözümüdür. Her yeni filmde uygulanır; eski filmler dokunulmaz.
> Araç tarafı: `kurgu.py` (`gecis` · `yataklar` · `klip_sesi`), `kareler.py dikis`, `film_dogrula.py --bolum muzik`.

## 0. Neden oluyor

- Her 10 s'lik klip **ayrı üretilir**; model önceki klibi görmez. Renk, kontrast, grain ve ışık yönü her klipte
  yeniden "icat edilir". İki klip yan yana gelince göz sıçramayı okur: kesme keskin görünür.
- Her klibin kendi sesi ayrı bir "oda"dır: model her klipte başka bir uğultu, başka bir oda tonu üretir. Kesmede
  ortam sesi komple değişir. Hatta modelin sesi zaten atılır (AGENTS.md §2); sorun, kurguda **kesintisiz bir yatak**
  kurulmadığında ya da klip sesi (model sesi replik) yatak olmadan kullanıldığında ortaya çıkar.
- Klipler **durağan kareyle başlayıp durağan kareyle bitince** kesme "fotoğraftan fotoğrafa" olur; hareket
  üstünde kesme (match on action) kesmeyi yumuşatır.

Çözüm üç katmandır; hiçbiri tek başına yetmez.

## 1. PROMPT katmanı — faz 5 (goruntu-yonetmeni yazar · devamlilik denetler)

1. **Ortak görünüm cümlesi.** FILM.md §3'te filmin tek bir görünüm cümlesi durur (objektif karakteri · grain ·
   renk paleti · kontrast · siyah seviyesi), İngilizce, 1-2 cümle. Her görsel **ve** video promptunun sonunda
   **birebir** yazılır. Örnek:
   `Anamorphic 35 mm look, fine film grain, desaturated steel-blue shadows with warm amber highlights, deep but not crushed blacks.`
2. **Mekân başına ışık cümlesi birebir** (T18 zaten kural): ana ışığın yönü, rengi ve sertliği aynı mekânın her
   çekiminde aynı kelimelerle.
3. **Mekân başına ortam ses cümlesi — yalnız model sesi AÇIK filmlerde** (FILM.md §5'te Kaynak = model sesi olan
   film). Aynı mekânın her video promptunda birebir: `The only ambient sound is a low, steady cockpit hum with no music.`
   Amaç, modelin her klipte başka oda tonu üretmesini azaltmak; yine de yatak kurguda kurulur (§2). Model sesi
   KAPALI filmlerde bu cümle yazılmaz (`film_dogrula` konuşma/ses tarifini hata sayar).
4. **Vuruş planı kesmeye hizmet eder:** ilk vuruş **hareketle** başlar (akan kamera ya da süren beden hareketi,
   durağan "fotoğraf" değil); son vuruş donmaz (zaten kural). Ardışık iki çekim bir hareketi bölüyorsa (C05 kol
   kalkar → C06 kol iner) kesme hareketin ortasına düşer; kurgucu bunu kullanır.
5. **Ölçek ya da açı farkı.** Ardışık iki çekim aynı mekândaysa ya ölçek bir basamak değişir (geniş → orta → yakın)
   ya da açı ≥ 30° döner. Aynı ölçek + aynı açı kesmesi jump cut gibi okunur. devamlilik §4 Kadraj sütunundan bakar.

## 2. SES katmanı — faz 4 (ses-tasarimcisi yazar · kurgucu eleştirir)

1. **Ortam yatağı mekân başına TEK dosya**, klip sınırlarını aşar. FILM.md §6 `ORTAM YATAĞI` tablosu: yatak ·
   mekân · kapsadığı çekimler · ne (İngilizce üretim/arama cümlesi) · seviye · dosya (`ses/yatak_<mekan>.wav`).
   Seviye −18…−22 LUFS (replik yokken), ritimsiz, sürekli. `timeline.json` → `yataklar`.
2. **Mekân değişiminde yatak çapraz geçer:** iki yatak 1-2 s örtüşür (`gecis` alanı; `kurgu.py` iki yatağı
   solarak bindirir). Sert yatak kesmesi yalnız planlı anda (güç kesildi, kapı kapandı).
3. **J/L köprüsü her kesmede zorunlu:** sonraki sahnenin sesi 1-1,5 s önce girer (J) ya da öncekinin sesi 0,5-1,5 s
   taşar (L). §6 `GEÇİŞ` tablosu "Ses köprüsü" sütunu bunu kesme kesme yazar.
4. **Müzik kesintisizdir;** kesmede müzik kesilmez. Müziksiz anlar plandadır (§7), kesmeye rastlantıyla düşmez.
5. **Model sesi replik taşıyan klip:** klibin sesi filme girer (`klip_sesi: true`) ama **yalnız replik için**;
   klibin kendi ortam uğultusu yatağın altında kalır (gerekirse `klip_kazanc_db` −3…−6). Replik geçiş aralığına
   (karışım/karartma süresi) düşmez. Omni, Mara'nın K02 sesini K12/K23'te taklit edemez: aynı kaydı yeniden
   kullanmak gerekirse planın "kurguda ekle" yolu yedektir (`ses` listesi).

## 3. KURGU katmanı — faz 8 (kurgucu yazar · Fable kurgu.py ile denetler)

1. **Her kesmeye geçiş türü** (`timeline.json` parçanın `gecis` alanı — o parçaya giriş):
   | Tür | Ne zaman | Süre |
   |---|---|---|
   | `kesme` (varsayılan) | aynı mekân, zaman sürüyor; hareket üstünde kesme | — |
   | `karisim` (çözülme) | aynı mekânda zaman atlaması; iki klip arasında renk/ışık sıçraması yumuşatılacak | 0,3-0,8 s |
   | `karartma` (siyaha in-çık) | bölüm sonu, büyük zaman ya da mekân atlaması | 0,5-1,5 s |
   Ritim: karışım kesmelerin en çok dörtte biri; karartma film başına en çok 2. Zincir içinde yalnız kesme (dikiş).
   Her geçiş filmi süresi kadar kısaltır; `kurgu.py kontrol` toplamı gösterir.
2. **Dikiş ölçümü her kesmede:** `kareler.py dikis <klip_a> <klip_b> --hedef ~/film_medya/<FILM>/analiz/dikis/<Ca>_<Cb>/`.
   Fark görüntüsü ve SSIM **bayraktır**, karar görseldir:
   - SSIM çok yüksek (≈ >0,9) ve aynı mekân → jump cut riski: açı/ölçek farkı yok;
   - fark görüntüsünde bütün karede düzgün bir parlaklık/renk farkı → renk sıçraması: `karisim` ya da renk eşleme notu;
   - yerel büyük fark → kadraj değişimi, normal kesme.
3. **Renk eşleme notu:** ardışık klipler arasında parlaklık/renk farkı varsa kurgucu çekimi `GEÇİŞ` tablosunda
   "renk eşle" diye işaretler; sahibin kurgu aracında (ya da taslakta `eq`/`colorbalance` denemesiyle) düzeltilir.
   Flow'a geri dönüp yeniden üretmek son çaredir.
4. **Taslak:** `kurgu.py kontrol` → `taslak` → `kareler.py cikar` → izleyici. Kesmeler `kurgu.py liste --kesmeler`
   çıktısında geçiş türüyle görünür; SÜREKLİLİK taraması (Gemini) bunun üstünden koşar.

## 4. FILM.md §6 tabloları (SABLON)

```
### ORTAM YATAĞI
| Yatak | Mekân | Çekimler | Ne (İngilizce) | Seviye | Dosya |
| Y1 | kokpit | C02-C04 · C09-C12 | low steady cockpit hum, soft air vent, no rhythm | −18 LUFS | ses/yatak_kokpit.wav |

### GEÇİŞ
| Kesme | Tür | Ses köprüsü | Gerekçe |
| C01→C02 | kesme | Y1 J 1 s | dış → iç, hareket üstünde |
| C08→C09 | karisim 0,5 | Y1→Y2 çapraz 1,5 s | zaman atlaması, aynı mekân |
```
`film_dogrula.py --bolum muzik` iki tablo yoksa uyarı verir (F4 ses-tasarimcisi taslak yazar, F8 kurgucu kesinleştirir).

## 5. Kim, ne zaman

| Faz | Kim | Ne |
|:--:|---|---|
| 3 | yonetmen · teknik-danisman | ardışık çekimlerde ölçek/açı farkı; kesme hareket üstüne düşecek şekilde çekim bölünmesi |
| 4 | ses-tasarimcisi (+ kurgucu eleştiri) | ORTAM YATAĞI tablosu · GEÇİŞ taslağı (tür önerisi + köprü) · yatak dosyaları için üretim/arama cümlesi |
| 5 | goruntu-yonetmeni · devamlilik | ortak görünüm cümlesi birebir · mekân ışık cümlesi · (model sesi açıksa) ortam ses cümlesi · ilk vuruş hareketli |
| 7 | sahip | Flow proje ayarı: model sesi KAPALI filmde "Return silent videos" AÇIK; model sesi AÇIK filmde KAPALI (replik klipten) |
| 8 | kurgucu · Fable | `gecis` + `yataklar` + `klip_sesi` timeline'da · her kesmede `kareler.py dikis` · `kurgu.py kontrol/taslak` · renk eşleme notları |

## 6. Ölçüm

- SMOKE P18: Omni Flash 1.1 ses AÇIK — replik videoda doğru mu, oda tonu klipten klibe ne kadar değişiyor?
- SMOKE P19: aynı mekânın iki klibi, ortak görünüm cümlesi var ↔ yok; `kareler.py dikis` fark görüntüsü + sahibin gözü.
- İlk filmde (THE_MAYDAY_SEA) kesme başına geçiş türü dağılımı ve dikiş ölçümleri `NOTLAR.md` KARARLAR'a; iki filmde
  tekrar eden bulgu sahip onayıyla `BILINEN_TUZAKLAR.md`'ye.
