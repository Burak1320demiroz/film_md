<!-- denetci (sonnet) F5 kapısı — cevabı AYNEN (alt ajan transkriptinden; 20 tur sınırı → SendMessage teslim), 20.10.2026 -->

FAZ 5 KAPISI · DEAD_LAST (yatay_8_dk_filmler)

Yol öneki: yatay_8_dk_filmler/DEAD_LAST/. Sınır: tur sınırı geldiği için FILM.md §4 Referans ve Kadraj sütunlarının güncellenmesine (K13, L11, L30) ve C41Y'nin iş emri satırlarına bakamadım. İkisi de ✅ sayılmadı, aşağıda "doğrulanmadı" diye işaretli.

| Madde | Durum | Kanıt |
|---|---|---|
| Ö1 M, zorunlu eleştiriler ODA'da | ✅ | ODA/F5_teknik-danisman_1_G01 / _G02-G04 / _G05-G06.md ve F5_devamlilik_1_G01 / _G02-G04 / _G05-G06.md var. |
| Ö2 M, GİRDİ var, "EKSİK" yok | ✅ | Altı dosyada da GİRDİ satırı var. grep -c EKSİK altısında 0. "Yapılmadı" notları (film_dogrula koşulmadı, kare yok) EKSİK sayılmaz. |
| Ö3 ÖLÜMCÜL ve CİDDİ cevapları | ✅ | ÖLÜMCÜL 0. Tüm CİDDİ'ler (TD G01 B1-9, DV G01 B1-11, TDa B1-11, DVa B1-13, TDb B1-10, DVb B1-10) PROMPTLAR/G01-G06.md sonundaki "F5 TUR 1 CEVAPLARI" tablolarında KABUL / RED (plan, SK) / F7 olarak tek tek cevaplı. |
| Ö4 KABUL uygulandı mı | ✅ (örneklemeyle) | Önceki sürüm yok, bu yüzden dosyadaki izden doğruladım. K1: C03 Video "gloved hands leave the frame" cümlesi yok; yalnız not ve cevap satırında geçiyor. K2: G01 satır 599 "holds no cell; the only cell is the one held above it". K3: G01:339 "0-2 s … 2-5 s: Axi speaks … 5-10 s". K5: G01:491 beş araç, "slowly pulls back". K7: "Inside Needle's compact one-pilot canopy" 5x, M02 ışık cümlesi 5x. K8: "keeps pace beside Thren" 4x. K9: "Fang runs on Needle's left side" 3x, "right-hand side window" 4x. K10: "five lane lights are still unlit" 4x. L1: G01-G06 prompt gövdelerinde dead/body/kill yok; "kill" yalnız G04 C26 replik satırında (SK10). L18: vuruş iskeleti her grupta 5-8 farklı (script sayımı). Kısmi uygulanmayanlar cevap tablosunda açıkça yazılı ("DVa B6 … uygulanmadı", "DVa B21 'Each a different color' … uygulanmadı", "DV B16 C04 uygulanmadı"). Doğrulanmadı: FILM §4 sütun düzeltmeleri (K13, L11, L30). |
| Ö5 RED gerekçeleri | ✅ (not var) | RED'ler "plandan asla dışarı çıkma" kuralına ve SK tablolarındaki risk sütununa dayanıyor. Bulgunun kanıtına teknik cevap vermiyorlar; bunların hepsi sahibe gidiyor. "Plan cümlesi aynen kaldı" gerekçesi ince, ama SK tablosu riski adlandırıyor. |
| Ö6 açık ÖLÜMCÜL yok | ✅ | Altı eleştirinin hepsinde ÖZET "ÖLÜMCÜL 0". DURUM.md "AÇIK ÖLÜMCÜL BULGULAR" tablosu boş. |
| Ö7 M, DURUM güncel | ✅ | ODA/DURUM.md: FAZ 5, TUR 1, AJAN_CAGRI 22/50, METIN_CAGRI 22/30, SIRADAKI "F5 kapısı: denetci (çağrı 22)". Faz günlüğündeki çağrı numaralarıyla tutarlı. |
| Ö2b eleştiri biçimi | ✅ | Her eleştiride "### B" sayısı YER, KANIT ve DÜZELTME sayılarına eşit (TD 15/16/16, DV 21/25/22). Devamlilik 8 soru tablosu eksiksiz: G01 8 satır, G02-04 24 satır (C09-C32), G05-06 C33-C48 ve C41Y y1-y3. Eleştirilerde % yok. |
| Ö8 metin tavanı | ✅ | METIN_CAGRI 22/30, tavan aşılmadı. |
| Ö9 gerçek durum | ✅ | medya.py durum: "GERÇEK DURUM medya yok", ref 0/22, kare 0/48, ham 0/48. DURUM.md MEDYA satırıyla çelişmiyor; kayıtsız deneme yok. |
| F5.1 M, film_dogrula prompt | ✅ | film_dogrula.py … --bolum prompt → "✅ yapı geçerli", çekim 48. Hata yok, yalnız uyarı. |
| F5.2 devamlilik ÖLÜMCÜL açık değil | ✅ | ÖLÜMCÜL 0. Kimlik eksikleri L15 ile işlendi. İkinci tur eleştirisi koşulmadı; tavan 2 tur olduğu için sorun değil. |
| F5.3 teknik-danisman | ✅ | Üç grup için F5_teknik-danisman_1_*.md dosyaları var, her bulguda YER ve KANIT dolu. |
| F5.4 M, Flow iş emri | ✅ (C41Y doğrulanmadı) | Her G0n.md içinde "FLOW İŞ EMRİ" var: 8 kare + 8 video satırı, dosya adı · mod · referans (numaralı dosya adı, "bu sırayla"). EKLE referansları ile Görsel'deki "Reference <No>" eşleşmesini film_dogrula doğruladı. C41Y satırlarını ayrıca sayamadım. |
| F5.5 M, zincir | ✅ (yok) | DURUM.md: "Zincir yok". Promptlarda "previous clip / last frame" dili bulunmadı. |
| F5.6 | ✅ | Her gruptaki 5-8 farklı vuruş iskeleti (L18). Devamlilik rol tutarlılığı için 8 soru sütun 7'ye baktı. Son vuruş donmaması L17 ile uygulandı: G04 C26, C27, C32 "push … carries on to the end of the shot"; C43 "finish parting outward through the end of the shot". |
| F5.7 tek referans sayfası, her açı ve durum panel | ❌ YARGI | Referans sayfaları tek açı: devamlilik G01 B1 "Referans sayfaları tek açılı; çekimlerin istediği paneller yok" (arka ¾, boş beşik, kabin içi). C29, C31, C35 ve C37-C42 arkadan çekiliyor. Cevap: "RED (plan, SK4)", yani sahibe açık. Ref 20-22 ayrı sayfa, DURUM.md'de sahip istisnası olarak kayıtlı. |
| F5.8 ortak cümleler, mekân ışığı | ❌ YARGI | ORTAK GÖRÜNÜM Görsel'de birebir 51/51 (48 çekim + C41Y üç kaynak; script sayımı). ORTAK HAREKET 48/48 Video'da (üç konuşma cümlesi atılan çekimlerde yazım kararı gereği kısaltılmış). Eksikler: (a) ORTAK GÖRÜNÜM Video'da yok, kapının istediği "her görsel ve video promptunda" karşılanmıyor, cevap SK8 (plan: yalnız Görsel'in başına). (b) Mekân ışık cümlesi M03/M04/M05 için yok, "F7'de eklenecek" (DVa B1, DVb B18). Model sesi kapalı olduğu için ortam sesi cümlesi yok; bu hata değil. |
| F5.9 M, replik birebir | ✅ | film_dogrula prompt bölümü hatasız. DURUM.md SK1: model sesi kullanılmıyor. Yalnız "ağız kadrajda" çekimlerde Dialogue bloğu var (G01 K4, G03-G04 cevapları). |
| F5.10 C01-C03 yazı, el teması, vizör | ❌ YARGI | C02 Video "The flat system line is added over the image" → ekrana yazı riski; cevap RED (SK6), sahibe açık. C03 plan cümlesi "lower … lock it with one clear click and withdraw", yani el-nesne teması kadrajda; RED (SK3), sahibe açık. Teknik danışman bunları B1/B4 olarak yazdı (G01:28 ILK_30 §6 atfı). |
| F5.11 G01 önce; DERS uyarıları | ✅ | DURUM faz günlüğü: G01 (çağrı 4) → G01 eleştirileri (5-6) → revizyon (7) → G02-G06 (8-12). F5_grup_gorevi.md G01'i "Örnek grup" diye veriyor. film_dogrula çıktısındaki iki DERS uyarısı da ODA/F5_uyari_cevaplari.md'de gerekçeli: DERS Y2 C32·20 (kokpit içi, kadrajda hasar yok) ve DERS Y5 C01 C14 C20 C33 C45 ("smoke-gray" plan R03 rengi; "dense vapor" plan C14 sözü). |
| F5.12 devamlilik 8 soru | ✅ | Üç dosyada da her çekim için tablo dolu, yokluk "—" ve bulgu numarasıyla işaretli. Grup-arası kilit düşmesi bulgu olarak yazılmış (DVa B1/B24 ORTAK GÖRÜNÜM Video'da yok, DVa B15 kimlik eş anlamlıları). |

film_dogrula.py çıktısı: "✅ yapı geçerli", 48/48 çekim. Uyarılar: ref 20-22 sahip istisnası, 50 replik bandın dışında (plan, FILM §5 altında gerekçeli), DERS Y2 ve DERS Y5 (cevaplı).

MEKANİK ❌   yok
YARGI ❌     F5.7 (referans sayfası panelleri yok, SK4) · F5.8 (ORTAK GÖRÜNÜM Video'da yok, SK8; mekân ışık cümlesi yok, F7) · F5.10 (C02 ekrana yazı, SK6; C03 el-nesne teması, SK3). Üçü de sahibin "plandan asla dışarı çıkma" kararına bağlı. Fable gerekçeyle aşabilir. Sahibe SK3-SK13 tablosu olarak gösterilmeli.
SONUÇ        KAPANABİLİR (mekanik: yok / yargı: F5.7, F5.8, F5.10, Fable gerekçesiyle aşılmalı ve DURUM.md "AŞILAN KAPILAR"a yazılmalı).

Fable'ın kapanıştan önce kendisinin doğrulaması gerekenler: FILM §4 Referans sütunu (C17 ve C21'den 21 çıkarılması, C44 → 10·22·18, C48 → 20·21·13·18), FILM §4 Kadraj sütunu doluluğu ve C41Y iş emri satırları.

Dosyalar (hepsi /Users/dai/github/apex_md/film_md/yatay_8_dk_filmler/DEAD_LAST/ altında): PROMPTLAR/G01.md … G06.md, ODA/DURUM.md, ODA/F5_uyari_cevaplari.md, ODA/F5_fable_birlestirme_1.md, ODA/F5_fable_birlestirme_2.md, ODA/F5_yazim_karari.md, FILM.md.
