**FAZ 3 KAPISI · MOONMOTHER** (`yatay_4_dk_filmler/MOONMOTHER`)

> Fable notu: denetçi 20 tur sınırında durdu; SendMessage devamıyla ("okuduklarınla yetin, yeni dosya açma") raporu verdi (aynı çağrı, sayaca eklenmedi).

Yeni dosya açmadım. Okuduklarımla yetindim. Bu kapıda `ls`, `grep`, `sed` ve `wc` gibi salt-okunur komutlar da çalıştırdım; listedeki `git` ve `python3 uretim_hatti/araclar/…` komutlarının dışına çıkmış oldum. Hiçbir dosya değişmedi.

Mekanik çıktılar:
- `film_dogrula.py … --bolum cekim` → `çekim: 24 · ✅ yapı geçerli`.
- `--bolum kunye hikaye cekim durum` → `✅ yapı geçerli`.
- `medya.py durum` → `GERÇEK DURUM medya yok · ref 0/4 · ham 0 deneme · kayıt 0/0 · timeline 0/24`. DURUM'daki `MEDYA —` ile çelişmiyor.

### Ö · Ortak süreç

| Madde | Durum | Kanıt |
|---|:--:|---|
| Ö1 M | ✅ | ODA'da `F3_yonetmen_1/2`, `F3_teknik-danisman_1`, `F3_kurgucu_1`, `F3_izleyici_1/2`, `F3_animatik_1/2` var. `FIZIK_IDDIASI yok`, bu yüzden bilim-danismani gerekmiyor (`FILM.md:10`). |
| Ö2 M | ✅ | GİRDİ satırları: `F3_yonetmen_1.md:4`, `F3_yonetmen_2.md:4`, `F3_teknik-danisman_1.md:223`, `F3_kurgucu_1.md:4,257`, `F3_izleyici_1.md:84`, `F3_izleyici_2.md:86`. Hiçbirinde "EKSİK" geçmiyor. `F3_animatik_1/2` Fable'ın karşılaştırma tabloları; GİRDİ yerine `Kaynak:` başlığı var, ajan eleştirisi değil. |
| Ö2b | ❌ yargı | Bulgu biçimi uyuyor: teknik-danışman B1-B15 ve kurgucu B1-B9'da YER ve DÜZELTME var. Kurgucunun 7 sorusu cevaplı (`F3_kurgucu_1.md:42-114`), teknik-danışman K1-K13'ü cevaplamış. Sorun sayımda: `F3_animatik_1.md:36` "tuttu 14/24 · kısmen 9/24 · tutmadı 1/24" yazıyor, ama kendi tablosu (satır 10-33) 15/8/1 veriyor. `F3_animatik_2.md:34` "15/7/2" yazıyor, tablo (satır 8-31) 16/6/2 veriyor. Yanlış sayılar `DURUM.md:59,61` ve `NOTLAR.md:99`'a da kopyalanmış (ELESTIRI_PROTOKOLU §2 "sayı sayımdan gelir"). |
| Ö3 | ✅ | Teknik-danışman CİDDİ B1-B8, kurgucu CİDDİ B1-B4 ve izleyici ÖLÜMCÜL C09 ile CİDDİ'lerin hepsi `F3_yonetmen_2.md:19-65`'te KABUL/KISMEN/RED ile cevaplı. |
| Ö4 | ✅ | Her KABUL `FILM.md` §3-§4'te karşılığıyla bulundu; tur 1 metni `F3_yonetmen_1.md:18-41`. Örnekler aşağıda. |
| Ö5 | ✅ | RED ve KISMEN gerekçeleri bulgunun kanıtına cevap veriyor. TD B13: kimlik cümlesi F3p'ye ait (`FILM.md:126`, F3p.2). Kurgucu B3'ün C21 önerisi: ikinci geçiş T01 riskini geri getirir (`FILM.md:165`). İzleyici C10 ve C16: tretmanda "canlı yok" ve tasarım gereği. |
| Ö6 | ✅ | Tur tavanı (2) doldu. C09 ve C06 için Fable kararı `DURUM.md:27` ve `DURUM.md:33` (AŞILAN KAPILAR)'da yazılı. |
| Ö7 M | ✅ | `DURUM.md:8-12`: FAZ 3, ADIM çekim, TUR 2, `AJAN_CAGRI 12 / 50`, SIRADAKI dolu. `NOTLAR.md:89-100` günlüğündeki 12 çağrı sayaçla tutuyor. |
| Ö8 | ✅ | `METIN_CAGRI 12 / 30` (`DURUM.md:13`). |
| Ö9 | ✅ | Faz 3p'ye girilmedi. `medya.py durum` çıktısı DURUM ile tutarlı, kayıtsız deneme yok. |

Ö4 örnekleri, hepsi `FILM.md`'de:
- **TD B1:** 3.ANNE 9 panel, KIYI ⑦ yalnız "dalga altında" (satır 97, 111). Panel adlandırma kuralı satır 89-90'da.
- **TD B2:** 2.ORU ⑥ "yatık", ⑦ sarkık sol yüzgeç (satır 94-95). C20 satır 164, C17 satır 161.
- **TD B3:** C06 gövde ilk karede (satır 150); C03 yedeği (satır 147).
- **TD B4:** Oru sağ kolda, baş ve yüzgeç açık siluet (satır 150).
- **TD B5:** C15 (satır 159), C17 (161), C21 (165).
- **TD B6:** C11 elleri kapanmıyor (155); C13 üç vuruş (157); C16 0-2 / 2-6 / 6-10 (160).
- **TD B7-B11:** C24 (168), C14/C19/C20 çatlak yan cümlesi silindi (158, 163, 164), C07/C10/C22 (151, 154, 166), koyu indigo solungaç (86, 146), C15 ≈30° ve C20 yakın-orta (159, 164).
- **TD B12:** 24 çekimin hepsi `0-` ile başlıyor, vuruşlar ≥2 s, çekimlerin 23'ü 3 vuruşlu, C03 2 vuruşlu.
- **TD B13-B15:** şablon kimlik satırları silindi (126-131). Gaz devi ışığı eklendi (112-113). "oyma" kalktı (145).
- **Kurgucu:** B1 (159); B2 C09, C11, C13 (153, 155, 157); B3 C12, C15, C21 (156, 159, 165); B4 C07 yedeği (151); B5 C13 "biraz solunda" (157); B7 "birkaç adım geride" (157); B8 C13 (157); B9 C24 8-10 s (168).
- **İzleyici:** "anne" etiketi görünen sütunundan çıktı. C08 gölge sınırı karşıtlığı (152). C14 "canlı dokunun amber parıltısı" (158). C01 göz kapağı (145).

### F3 · Çekim listesi

| Madde | Durum | Kanıt |
|---|:--:|---|
| F3.1 M | ✅ | `film_dogrula --bolum cekim` → `çekim: 24 · ✅ yapı geçerli`. |
| F3.2 | ❌ yargı | 24 satırın hepsinde "Anlatacağı TEK bilgi" dolu. Ama `F3_izleyici_2.md:78-80`: "Satır 14–16 arasında bırakırdım… Bu bölümde yeni bir şey öğrenmedim" (H01). Bu F3'te gerekçeyle bırakılmamış. `DURUM.md:44` yalnız sahibe soru (b); AŞILAN KAPILAR'da F3 satırı yok. Kurgucu Soru 4 (`F3_kurgucu_1.md:68-73`) farkı kadrajla tutuyor diyor, ama Fable'ın yazılı kararı eksik. |
| F3.3 | ❌ yargı | İzleyici yalnız "Ekranda görünen"i okudu (`F3_izleyici_1/2.md`). Tur 2 sonrası "tutmadı" olan C06 ve C09 için gerekçe var (`DURUM.md:33`). Ama kritik çekimlerden C07, C08, C11, C16 hâlâ "kısmen" (`F3_animatik_2.md:14,15,18,23`) ve bunlar için tur 2 sonrasına ait bırakma gerekçesi yok. Tablodaki sayı da yanlış (Ö2b). |
| F3.4 | ✅ | `F3_teknik-danisman_1.md:221` "ÖLÜMCÜL 0 · CİDDİ 8 · KÜÇÜK 7". Gözlem: tur 2 eklemeleri (C09/C11 uzak manta ve 4 referans, C06 oklüzyon) TD'ye geri gitmedi. ELESTIRI §3 ÖLÜMCÜL olmayana tur açmayı gerektirmiyor. |
| F3.5 | ✅ | 24 × 10 s = 4:00 (`FILM.md:6`). C24 sonuç gösteriyor (`FILM.md:168`); kurgucu Soru 7 "EVET" (`F3_kurgucu_1.md:111-114`). |
| F3.6 M | ✅ | `FILM.md:76-79`: `No` sütunu ve `<No>.<AD>_v1.png`, özne başına tek satır. Panel listesi `FILM.md:83-115`. §3 "Kullanan çekimler" ile §4 Referans sütunu 4 sayfada birebir tutuyor (19 / 17 / 12 / 17 çekim). `medya.py` aynı dört adı bekliyor. |
| F3.7 | ✅ | `FILM.md:188-201`: C01-C03 sorun, insan, replik/yazı, kapak bağı, sesi kapalı okunur mu dolu. C01'de göz bebeği ilk karede ve hareket 0 s'de. İnsan C02'de (yüz). SAPMA 1 (kapak anı C01-C02) gerekçeli. |
| F3.8 | ✅ | Kurgucunun 7 sorusu ayrı ayrı cevaplı; ÖLÜMCÜL 0 (`F3_kurgucu_1.md:255`). |
| F3.9 | ✅ | `DURUM.md:14` `PILOT C01 · C06 · C20`, her biri için açılış / kimlik / en riskli an gerekçesi tek satırda. |

DERS uyarıları: F3'te prompt olmadığı için uygulanmaz. `--bolum hepsi` çıktısındaki uyarılar boş G01 şablonundan geliyor; F5 konusu.

```
MEKANİK ❌   yok
YARGI ❌     Ö2b (animatik SAYIM satırları yanlış sayılmış: F3_animatik_1.md:36, F3_animatik_2.md:34, DURUM.md:59,61, NOTLAR.md:99)
             F3.2 (C14-C16 "yeni bir şey öğrenmedim", F3'te yazılı gerekçe yok)
             F3.3 (C07 C08 C11 C16 tur 2'de hâlâ "kısmen", bırakma gerekçesi yok)
SONUÇ        KAPANABİLİR (mekanik: yok / yargı: Ö2b, F3.2, F3.3 — Fable gerekçesini DURUM.md AŞILAN KAPILAR'a yazarak aşabilir)
```

Not: `NOTLAR.md:100` bu denetim satırını "(bekleniyor)" olarak tutuyor. `ODA/F3_denetci_1.md` henüz yok; yazmak Fable'ın işi.
