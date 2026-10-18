FAZ 2 KAPISI · MOONMOTHER (`/Users/dai/github/apex_md/film_md/yatay_4_dk_filmler/MOONMOTHER`)

**Mekanik kanıt**
- `film_dogrula.py ... --bolum kunye`, `hikaye`, `replik` ve `durum` ayrı ayrı koşuldu. Dördü de `✅ yapı geçerli` verdi.
- `--bolum hepsi` 5 ⛔ ve 1 ⚠️ verdi. Hepsi F3/F4 şablon satırlarından geliyor:
  - C01 çekim satırının `<...>` yer tutucuları
  - 1/24 çekim
  - boş §7 MÜZİK PROMPTU
  - şablon G01'deki `freeze` uyarısı
  
  F2 maddesi değiller. DERS uyarısı da F5'te sorulur, bu kapıda cevap aranmaz.
- `medya.py durum`: `GERÇEK DURUM  medya yok` · `TESLİM ref 0/2 · denenen 0/1`. FAZ 2 ile çelişmiyor.
- Birebir yerleştirme: `git diff --no-index ODA/F2_senarist_2.md FILM.md` çıktısında §1 satırları (senarist_2:83-89) ve §2 tablosu (senarist_2:130-155) fark listesinde yok. İkisi FILM.md:30-36 ve :47-70'e kelimesi kelimesine geçmiş.

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 **M** | ✅ | `ODA/F2_dramaturg_1.md` ve `ODA/F2_izleyici_1.md` var. `ses-tasarimcisi` F2'de yalnız replik varsa çağrılır (`hikaye-odasi/SKILL.md` §F2 madde 2, AGENTS §2). FILM.md:8 `REPLIK yok` olduğu için açılmaması doğru. DURUM.md:49 bunu yazıyor. |
| Ö2 **M** | ✅ | Dramaturg: `GİRDİ` F2_dramaturg_1.md:156. İzleyici: F2_izleyici_1.md:91 (`GİRDİ: metin, 24 satır.`). İkisinde de "EKSİK" yok, yalnız `YAPILMADI`. |
| Ö2b | ✅ | Dramaturg B1-B9'un her birinde `YER` ve `DÜZELTME` var. 10 maddelik H listesi tek tek cevaplı (:126-137). Sayılar paydalı: `5/8` (B1), `6/6` (B2), `0/10` (B4), `0/5` (B5), `100 s`. `KORU:` satırları kanıtlı. İzleyici kendi şablonunu (`izleyici.md`) kullanmış. Not: dramaturg `GİRDİ`'de "dosyanın tamamı açıldı" diyor, yani yazarın §3-§5 gerekçesi de önüne gelmiş. Gerekçeyi yok saydığını yazmış ve bütün YER'ler :27-94 arasında (§1-§2), bu yüzden ❌ yapmadım. |
| Ö3 | ✅ | CİDDİ B1-B6 için F2_senarist_2.md:25-51 KABUL/RED veriyor. KÜÇÜK B7-B9 :53-57. Karşılaştırma K1-K3 (CİDDİ) ve K4-K7 :61-67. İzleyici notları İ1-İ7 :70-76. |
| **Ö4** | ❌ | Aşağıdaki "Ö4 ayrıntı" bölümüne bak. B6'nın S16 ayağı uygulanmamış. Geri kalan KABUL'ler FILM.md'de bulundu. |
| Ö5 | ✅ | B2 RED (S5 ışık): plan C05 olayı (SAHIP_PLANI.md:60,280), "S6 çok geniş, üç oval okunmaz", "S6'nın yankısını siler". Üçü de dramaturg'un DÜZELTME'sine cevap veriyor. B6 RED (S15 silme): (a) C15 olayı ve S17 ön koşulu, (b) dört olayı tek 10 s'ye sıkıştırır, (c) 24 sabit. K6 RED: `30 s = %12,5` doğru sayım (30/240). İ5 ve İ6 RED'leri plan R2 "eski ve kuru" (SAHIP_PLANI.md:185) ve S20-S23 satırlarına dayanıyor. |
| Ö6 | ✅ | Dramaturg `ÖLÜMCÜL 0` (:154). Karşılaştırma `ÖLÜMCÜL yok` (F2_karsilastirma_1.md:14). DURUM.md:25-26 "AÇIK ÖLÜMCÜL" tablosu boş. |
| Ö7 **M** | ✅ | DURUM.md:8-17 alanların hepsi dolu: `FAZ 2 · TUR 2 · AJAN_CAGRI 5 / 50 · METIN_CAGRI 5 / 30 · SIRADAKI F2 kapısı…`. NOTLAR.md:89-93 beş çağrı satırıyla uyumlu (senarist, dramaturg, izleyici, senarist, denetci). |
| Ö8 | ✅ | `METIN_CAGRI 5 / 30` (DURUM.md:13). Tavan aşılmadı, tur ayrımı gerekmiyor. |
| Ö9 | ✅ (uygulanmaz) | FAZ 2. `medya.py durum`: "medya yok", kayıtsız deneme yok. |
| F2.1 | ✅ | FILM.md:47-70'te 24 satır. §3.1 (F2_senarist_2.md:163-187) 23 geçişi tür ve bağla yazıyor. Dramaturg'un H05 üç bulgusu (S10 sebebi, anne S8-S17, kural ve saat) FILM.md'de kapanmış: S10 :56, S16 :62, S17-S22 :63-68. |
| F2.2 | ✅ | İzleyici yalnız "Ne olur" sütununu okudu (GİRDİ :91; çıktıda "Ne değişir" sızıntısı yok). F2_karsilastirma_1.md:7-11 alıntıları izleyici dosyasıyla uyuşuyor. AMAÇ "tuttu, geç", KARAR ve SONUÇ "tuttu". Not: ölçüm tur-1 metni üzerinde. Tur 2 değişiklikleri (S1 yürüyüş, S6 Khev eylemi, S16 anne) izleyiciyle yeniden ölçülmedi. Protokol §3 ÖLÜMCÜL yokken bunu şart koşmuyor. "5-7. satırda bırakırdım" (K2) F3 metin animatiğine kalıyor. |
| F2.3 | ✅ | Replik yok. Gerekçe FILM.md:141 ve F2_senarist_2.md:278-290. Sıfır gerekçeli (4 dk bandı 12-24). `film_dogrula --bolum replik` ✅. HUMAN/MACHINE, diyalog ve konuşan profili alt maddeleri replik olmadığı için uygulanmaz. |
| F2.4 | ✅ (uygulanmaz) | Replik yok. `ses-tasarimcisi` F2 eleştirisi açılmamış (DURUM.md:49). |

**Ö4 ayrıntı**

Uygulandığı doğrulananlar (FILM.md satırı):
- B1: S1 :47 `denize doğru yürüyor … adımın ortasında donuyor`. S8 :54 `bir adım atıp kemerin gölge çizgisinde duruyor`. AMAÇ :31 `S1 Oru'yu açık kıyıya doğru taşır`.
- B2 tanısı: S3 :49'da `Oru'nun çağrısının ardından` kalkmış. Tur 1'deki `"arayan biri" okumasına dönüyor` ve `Anne–yavru bağı sözsüz kuruluyor` cümleleri S5 :51'den gitmiş, yerinde `Cevabın niyeti açık değil: taklit mi, çağrı mı?` var.
- B3: S10 :56.
- B4: S16 :62 `Ufukta sağ arkada annenin çukurlu başı … ışıkları sönük`. S12 :58 `Işıklar Oru'nun fişeği`.
- B5: S17 :63, S19 :65, S20 :66, S21 :67.
- B7: S6 :52, S12 :58.
- B8: S3 :49.
- B9: LOGLINE :30 (24 kelime), AMAÇ :31.
- K3: S7 :53.
- K4: S11 :57.
- K5: S2 :48 ve S14 :60.
- İ1-İ4: S1, S8, S9.

**Uygulanmamış: B6'nın S16 ayağı (YARGI ❌).**
- Cevap (F2_senarist_2.md:48) "B6 KABUL (S14 ve S16 düzeltmeleri)" diyor.
- Dramaturg'un S16 DÜZELTME'si F2_dramaturg_1.md:77: `bir kez doğrulmayı deniyor ... geri çöküyor` → `doğrulmayı denemiyor, duvara bakıyor`.
- FILM.md:62 S16 hâlâ şöyle: `sağ bacağında doğrulmayı deniyor ve duvarın tepesine bakıyor; yaralı sol bacak yük vermeyince geri çöküyor`.
- Cevap (:50) "bacak denemesi tek … indi" diyor. Tur 1 zaten `bir kez` diyordu (F2_senarist_1.md:86), yani somut bir azalma yok.
- Bulgunun ETKİ'si olan "S14 ile S16 aynı bacak çökmesi" sürüyor (FILM.md:60 `acıyla geri çekiliyor` ↔ :62).
- Ek olarak kart FILM.md:33 hâlâ `sahne 15 (bedeli gördükten sonra yine yavruyu kucağına alır)` diyor. Bu, B6'nın öncelik-tekrarı temasının kartta kalan izi.
- S14 ayağı ve S15 silme kararı sorun değil: S14'te öncelik cümlesi korunmuş, silme RED'i gerekçeli.
- Çıkış yolu: plan C16 video promptu aynı hareketi zaten istiyor (SAHIP_PLANI.md:506 `tests one rise on his right leg … settles back when the injured left leg cannot support him`). Bu yüzden dürüst yol, B6-S16'yı RED olarak kaydetmek. Alternatif dramaturg DÜZELTME'sini uygulamak, ama o yeni bir SAPMA satırı olur.

Bloklamayan küçük izler (KÜÇÜK):
- K7 "kalktı" diyor, ama FILM.md:56 `Kadrajda canlı yok.` `Çekimde yaratık yok`un aynı not hâli. FILM.md:67'de `canlı yüzeye` kalmış. İzleyici bunu (F2_izleyici_1.md:78) sormuştu.
- İ2 cevabı (F2_senarist_2.md:71, ayrıca §3.1 :167) "S3'te yüzgeç Khev'in silüetini örtüyor" diyor. FILM.md:49'da yüzgeç yıldız alanını örtüyor, silüet sol altta ayrı duruyor. Neden-sonuç S4 :50'de zaten taşınıyor.
- FILM.md:56 ve :62'deki `(§4 no 1)` / `(§4 no 10)` atfı, FILM.md içinde ÇEKİM LİSTESİ §4'ü gösterir. Sapma tablosu `ODA/F2_senarist_2.md` §4'te.

**Kapsam dışı notlar**
- 12 PLANDAN SAPMA (2 OLAY EKLEME) sahip onayı bekliyor (DURUM.md:40). F2_senarist_2.md:259-271'de 12/12 satırda "Veto olursa" dönüşü dolu. FILM.md §2 sapmalı hâliyle yazılı. Sahip veto ederse yalnız o satır geri alınır.
- F1 kapısı denetçiden geçmedi; DURUM.md:32 "aday turu açılmadı"yı AŞILAN KAPILAR'a yazmış. F1.4 **M**, "sahibin cevabı DURUM.md'de" ölçütüyle SAHİP CEVAPLARI'nda karşılanıyor (:38-39). Bu kapıda ölçülmedi, yayın onayında sahibe gösterilecek.

```
MEKANİK ❌   yok
YARGI ❌     Ö4 (B6'nın S16 ayağı: KABUL denmiş, FILM.md:62'de uygulanmamış)
SONUÇ        KAPANABİLİR (mekanik: yok / yargı: Ö4 — Fable ya B6-S16'yı RED olarak NOTLAR KARARLAR'a gerekçesiyle yazar ya da AŞILAN KAPILAR'a gerekçeyle geçer)
```
