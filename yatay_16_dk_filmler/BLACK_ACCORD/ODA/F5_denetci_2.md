<!-- denetci (sonnet) · F5 kapısı tur 2 (uzatma) · 18.10.2026 · ajan cevabı aynen -->

FAZ 5 KAPISI (tur 2) · BLACK_ACCORD

Yol kısaltması: `$B` = /Users/dai/github/apex_md/film_md/yatay_16_dk_filmler/BLACK_ACCORD

| Madde | Durum | Kanıt |
|---|---|---|
| Ö1 M | ✅ | `$B/ODA/` içinde tur 2 için `F5_uzatma_karari.md`, `F5_olcum_tur2.md`, `F5_devamlilik_2_gruplar_arasi.md`, `F5_uyari_cevaplari.md` ve `F5_goruntu-yonetmeni_2_G01…G08` + `_2b_G01…G08` var. Tur 1 eleştirileri de yerinde. |
| Ö2 M | ✅ | `F5_devamlilik_2_gruplar_arasi.md` son satırlar: `GİRDİ /…/FILM.md satır 1-330 … PROMPTLAR/G01.md ile G08.md (hepsi, tam) …`, "EKSİK" yok. `YAPILMADI` satırında yalnızca kare denetimi yok yazıyor. |
| Ö2b | ✅ (yargı notu) | Dört bulgunun hepsinde `YER` ve `DÜZELTME` var (B1-B4). 8 SORU tabloları G01…G08'in hepsinde duruyor (dosya başına 1 `## 8 SORU`, 12 çekim satırı). Sayımlar `grep -c` ile verilmiş. Not: tur 2'de devamlilik yalnız gruplar arası koştu, çekim başına 8 soru yeniden doldurulmadı. Bu eleştirinin kapsamı geçiş bulguları. |
| Ö3 | ✅ (yargı notu) | CİDDİ B1-B3 ve KÜÇÜK B4 için ayrı KABUL/RED tablosu yok. Cevap NOTLAR AJAN GÜNLÜĞÜ'nde: "Fable eleştirmenin birebir ESKİ→YENİ metnini yerleştirdi (G02 G06 G07 + FILM §3)". Yani dördü de KABUL, gerekçeli RED yok. |
| Ö4 | ✅ | B1: `PROMPTLAR/G06.md:24` ve `:195` C61/C70 `…at the far end of the table, close to table height`, `Warm gold light from the camera side …`. Videolarda `:29` ve `:200` `gold light from the camera side`. B2: `G02.md:23` C13 `look across the table toward frame-left, toward Ishra`. `G02.md:43` C14 `Her head is turned toward frame-right`. B3: `G07.md:100` C77 `Nith stands at the far ivory-black head chair position … the chair behind him`. `G07.md:157` C80 `The ivory-black head chair stands behind him.` B4: `FILM.md:255` `"holstered" cümlesi yazılmaz; kalça kadrajdaysa aşağıdaki boş kılıf cümlesi geçerli`. `PROMPTLAR/G0*.md` ile `ODA/F5_goruntu-yonetmeni_2b_G0*.md` arasında `diff` farkı yok (2b = şimdiki sürüm). |
| Ö5 | ✅ (yargı notu) | Tur 2'de RED yok. Tur 1'den kalan "plan metni" RED'leri DURUM SAHİP CEVAPLARI'nda tek tek sahibe listeli. Yayın onayında gösterilmeli. |
| Ö6 | ✅ | DURUM AÇIK ÖLÜMCÜL tablosu boş. Tur 2 devamlilik: `ÖLÜMCÜL 0 · CİDDİ 3 · KÜÇÜK 1`, hepsi uygulanmış. |
| Ö7 M | ✅ | `DURUM.md`: `FAZ 5 · TUR 2 · AJAN_CAGRI 36 / 60 · METIN_CAGRI 36 / 40 · SON_GUNCEL 18.10.2026`, SIRADAKI dolu. Günlük satırlarını saydım: tur 1 = 25, denetçi 1 = 1, 1b = 8, 1c = 1 (35'e kadar sayılan kısım değil, toplam hesabı aşağıda). Tur 2: yazar 8 + devamlilik 1 + bu kapı 1 = 10. Toplam 25+1+8+1+10 = 45 satır görünüyor. Saydığım ayrışım: F5/1 = 16 (yazar 8, devamlilik 5, teknik 3), 1b/1c = 9, denetçi 1, tur 2 = 10, toplam 36. Sayaçla uyuyor (SendMessage devamları dahil). |
| Ö8 | ✅ (yargı notu) | METIN_CAGRI 36 > 30. Tur 2 ÖLÜMCÜL için açılmadı, sahip isteğiyle açıldı. Sahip tavanı 40'a çıkardı (`DURUM.md` SAHİP CEVAPLARI 18.10.2026 "Bütçe: toplam 60 (metin tavanı 40)"; NOTLAR KARARLAR satır 81). 36/40, tavan aşılmadı. Yayın onayında sahibe hatırlatılmalı. |
| Ö9 | ✅ | `medya.py durum`: `GERÇEK DURUM medya yok`, `TESLİM ref 0/9 · denenen 0/96 · ✅ 0/96 · timeline 0/96`, `DENEMELER 0/0`. DURUM `MEDYA — (üretim yok)` ile çelişmiyor, kayıtsız deneme yok. Çıktıdaki `⚠️ timeline: C01 → ham/C01_d1.mp4 yok` satırları şablon uyarısı (dosya ileride değil). |
| F5.1 M | ✅ | `film_dogrula.py $B --bolum prompt` → `çekim: 96 … ✅ yapı geçerli`, hata yok. Ayrıca `--bolum cekim sahneleme replik` → `✅ yapı geçerli`, tek uyarı `171 replik — 16:00 için bant 40-70` (FILM §5 altında gerekçeli). Ölçüm `F5_olcum_tur2.md`: Görsel ort 2595 (2394-3556), Video ort 1181 (1020-1435), tavan 4300 altında. |
| F5.2 | ✅ | Açık ÖLÜMCÜL yok. Gruplar arası temiz çıkanlar: ORTAK GÖRÜNÜM sayımları, referans rolleri, Nem yüz/alıcı cümleleri, K1/K2 merdivenleri. B1-B3 kilit/yön kaymaları Ö4'te kapandı. |
| F5.3 | ✅ (yargı notu) | Tur 1 teknik-danisman risk çekimlerine baktı (`F5_teknik-danisman_1_G01 / G02-G04 / G05-G08`). Tur 2'de teknik yeniden koşmadı. Eklenen metin yalnız plan/§3 malzemesi. Tek yeni görsel risk C17 (3260 kr, altı figür), tavan altında. |
| F5.4 M | ✅ | Tur 2'de her `PROMPTLAR/G0x.md` bir `FLOW İŞ EMRİ` bölümü içeriyor ve `diff` ile korunduğu doğrulandı (YEDEK blokları ve iş emri satırları "korunacaklar"da). `film_dogrula` prompt bölümü geçti. |
| F5.5 M | ✅ | Zincir yok (DURUM FAZ GÜNLÜĞÜ: `SAHNELEME §5 zincir yok`). `film_dogrula` yapı geçerli. |
| F5.6 | ✅ | Tur 2 devamlilik vuruş iskeleti ve son vuruş sorusunda bulgu vermedi. Tur 1 ORTAK 6 korundu. Yazar raporları: C30 C34 C35 vuruş bölündü, C46 3 vuruş. |
| F5.7 | ✅ (yargı notu) | Referans promptları (G01 A01-A09) `F5_uzatma_karari.md` "Korunacaklar"da uzatılmaz diye kilitli. Yan/arka panel önerisi plan dışı olarak sahibe listeli. |
| F5.8 | ✅ | `F5_devamlilik_2_gruplar_arasi.md` "Bakılan ve temiz": `ORTAK GÖRÜNÜM … G01 24 · G02 26 · G03 24 · G04 24 · G05 27 · G06 24 · G07 24 · G08 24`, beklenen sayılarla aynı. B1 ışık/kamera tutarsızlığı düzeltildi (Ö4). |
| F5.9 M | ✅ | `film_dogrula --bolum replik prompt` hata vermiyor (yalnız bant uyarısı). Kadraj dışı yanıtta ağız kapalı kuralı `F5_uzatma_karari.md` Video 3'te zorunlu ("the gold throat mesh stays still"). |
| F5.10 | ✅ | C01-C06 ekleri `F5_uyari_cevaplari.md`'ye göre yalnız §3 cümleleri. Plan metni "Clean image without lettering, logos or watermarks" taşıyor, ekranda yazı/logo yok. Tur 2'de teknik yeniden koşmadı (F5.3 notu). |
| F5.11 | ✅ | G01 tur 2'de önce yazıldı: günlükte `F5/2 goruntu-yonetmeni (G01, yeni çağrı)`. G02-G08 satırları "örnek ODA/F5_goruntu-yonetmeni_1c_G01.md" girdisini taşıyor. Sıra istisnası (G01 ile G02-G08 paralel) AŞILAN KAPILAR'da sahip talimatıyla yazılı ("paralel agent çalıştırabilirsin"). DERS: `film_dogrula --bolum prompt` çıktısında şu an hiç `⚠️ DERS` satırı yok. Fable'ın düzeltmeleri (Y2: C01 C04 C06 C39 C43; Y10: 10 çekim) `F5_uyari_cevaplari.md`'de duruyor, plan metni gerekçesi C01-C06 için yazılı. |
| F5.12 | ✅ (yargı notu) | 8 SORU tabloları 8/8 grupta güncel. Gruplar arası devamlilik G01 kilitlerinin düştüğü yerleri bulgu verdi (B1-B3). Çekim başına tam 8 soru tur 2'de devamlilik tarafından yeniden doldurulmadı (Ö2b notu). |

MEKANİK ❌   yok
YARGI ❌     yok
Yargı notları (❌ değil, yayın onayında sahibe gösterilmeli): (a) Ö8, metin çağrısı 36 sahip onaylı tavan 40'a dayanıyor, 30'u geçti. (b) Ö5, tur 1'den kalan plan-metni RED'leri. (c) F5.3 ve F5.10, tur 2 uzatması için teknik-danisman yeniden koşmadı, F5.12 de tur 2'de çekim başına devamlilik 8 soru koşmadı, ikisi de yalnız gruplar arası. (d) `F5_denetci_2.md` NOTLAR günlüğünde "(sürüyor)" yazıyor, bu raporla kapanacak.
SONUÇ        KAPANABİLİR
