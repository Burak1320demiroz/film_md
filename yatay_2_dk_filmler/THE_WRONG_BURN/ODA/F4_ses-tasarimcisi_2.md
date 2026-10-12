# F4 · ses-tasarimcisi · tur 2 (birleştirme geçişi) — THE_WRONG_BURN

> Bu dosya ses planının SON hâlidir; tur 1'in (`F4_ses-tasarimcisi_1.md`) yerini tutar, ona bakmadan okunur.
> Yerleşim: §2 sahne tablosu ve §3 ORTAM satırı FILM.md §6'ya; §4-§9 aynen `ODA/`'da kalır.
> Saniyeler çekim içidir (0-10). Film saati = 10 × (Cxx − 1) + saniye (mutlak saniyeler yalnız §9'da).
> Seviye ölçeği: **0 dB = Bram'ın telsiz repliklerinin ortalaması.** "yok" = o kaynak o anda sessiz (0 değil).
> Mutlak seviye (−14 LUFS) son aşamada `kurgu.py yukseklik` ile kurulur; buradaki sayılar göreli dengedir.
> Fable kararı (F4_diyalog-yazari_1.md sonu, madde 1) işlendi: C07-C08 müziksiz; L1 54,8'de girer, 60,0'da kalkar,
> 60,0-96,8 müziksiz.

## 0. KARAR ÖZETİ

```
MODEL SESİ     KULLANILMAYACAK. Flow'da "Return silent videos" açık; sesli klip gelirse ses akışı taslakta atılır.
               Tek istisna olan "ağız kadrajda replik" bu filmde YOK: FILM §5'te 12/12 satır telsiz ya da kask içi,
               kayıt listesinde `model` filtreli satır yok. Video promptlarına ses satırı, replik ve efekt tarifi girmez.
               Bütün ses (replik, efekt, ortam, müzik) kurguda, bu plana göre kurulur.
KULAK          Film boyu kulak Sela'nın kaskındadır. Kadrajda Sela olmasa da (C01, C08, C10, C12) ses oradan duyulur.
ÜÇ KAYNAK      (1) kask içi: fan, Sela'nın nefesi, ateşleme tıslaması
AİLESİ         (2) gövdeden: tutamak, valf, ip silkinmesi, varış darbesi (eldiven/kemer/giysi yoluyla)
               (3) telsiz hattı: Bram'ın sesi, nefesi, tık, taşıyıcı hışırtısı (mikrofonu kendi kaskında)
KATMAN         K1 ortam yatağı (fan) · K2 efekt (kask içi + gövde) · K3 telsiz hattı + replik · K4 müzik. Sahne başına ≤4.
TELSİZ DİLİ    Tık = Bram'ın tuşu. Başlangıç tıkı hattı açar, bitiş tıkı kapatır. Hışırtı yalnız hat açıkken vardır.
               HAT AÇILIŞI (diyalog B2, KABUL): hat C05 6,2'de kapandı; C06 8,8'de Bram tuşa BASAR, bırakmaz
               (başlangıç tıkı var, bitiş tıkı yok). Hat C10 6,1'e kadar açık kalır; "ilk kez kendisi kapatıyor".
               C07'de başlangıç tıkı yoktur çünkü hat C06 8,8'den beri açıktır.
HAT DURUMLARI  İletim sırasında (Bram konuşurken) hışırtı −28: sezilir, duyulmaz (sinyal varken gürültü bastırılır).
               Konuşmasız açık hat: C06 8,8 −24 → 9,5 −16 · C07 −16 (Sela "Bram?" derken −28) · C08-C09 −27 ·
               C10 0-3,5 −27, 3,5-3,9 −16'ya yükselir, 4,0-6,0 replik altı −28, 6,1 kapanır · C11 1,8-6,0 −24 ·
               C12 −18 (replik 12 altı −28). Hat kapalıyken (C01-C05 iletimler arası, C06 0-8,8, C10 6,1-C11 1,8) hışırtı yok.
SERT KESMELER  Yalnız planlı anlar: C03 1,6 tıslama kuyruksuz kesilir · C10 6,1 hat kapanır, hışırtı da kesilir ·
               C12 0,0 varış darbesi (C11 6,0-10,0 sakinliğinden sonra) · film sonu. Müzik kesmeleri besteciye aittir (§9).
```

## 1. BULGULARA CEVAP (F4_diyalog-yazari_1.md B1-B10 · F4_kurgucu_1.md B2'nin ses tarafı)

| Bulgu | Cevap | Ne yapıldı / gerekçe |
|---|:--:|---|
| D-B1 CİDDİ · C07-C08 müzik çakışması | **KABUL** | Fable kararıyla aynı: §9'da müziksiz aralık 60,0-96,8. L1 54,8-60,0 arası C06'da kalır. Sahne tablosu S7-S9 K4 = yok. Ses tarafında başka değişiklik gerekmedi: C07 nefes seyrelmesi ve C08 ödülü sese bırakılı. |
| D-B2 CİDDİ · hat sebepsiz açılıyor | **KABUL** | C06 8,8'e tek başlangıç tıkı (−10); hışırtı onunla girer (−24 → 9,5'te −16, 0,7 s'lik yükseliş: squelch açılışı ani değil ama yavaş da değil). C07 satırı "C06 8,8'de basıldı, bırakılmadı". Bitiş tıkı C10 6,1'e kadar gelmez. Tur 1 §10/3 bununla kapandı. Tık sayısı 16 → 17. |
| D-B3 CİDDİ · C05 tartısı repliğe sıkışıyor | **KABUL** | Son alım 3,9 → 4,5 ("Last one's"tan sonra, "for both" üstüne). Bırakma 6,3 → 7,0 (dönüşün durduğu an, satır sonundan 1,0 s sonra). 8,6 nefesi kalır. Tutma süresi 4,8-7,0 (2,2 s). |
| D-B4 CİDDİ · "Bram?" hışırtıyla aynı bantta, Sela seviyeleri yok | **KABUL** | Hışırtı C07 1,5-2,1 arası −28 (giriş 1,4'ten 0,1 s rampa; çıkış 2,1-2,4 arası 0,3 s rampa). Sela seviyeleri kayıt listesine yazıldı: satır 4 · 6 · 9 → −2, satır 10 → −6. Not: Sela telsiz zincirinde değil; düşüş hikâye olayı değil miks duck'ıdır (fısıltı ünsüzleri 1-3 kHz'de). |
| D-B5 CİDDİ · "Good call." müzik zirvesinin altında | **KABUL (ses sınırı olarak)** | Müziğin içeriği ve kesme saniyesi besteciye ait. Ses sınırı §9'da: 114,0-114,8 müziksiz ya da L3 yok + L1 −9 dB; 118,0 öncesi ≥0,5 s müziksiz. Ses planı 113,2 kesmeyi TERCİH eder: 114,8-118,0 cevap boşluğunun (A9c, 3,2 s) içinde müzik olayı olmamalı. |
| D-B6 CİDDİ · C11 iki alım üst üste | **KABUL** | Sela'nın sert alımı 2,3 → 1,5 (Bram'ın tıkından 0,3 s önce, 1,5-1,8; önce davranan o). Bram'ın tıkı 1,8, alımı 2,0 (N4). L3 sınırı §9'da: 101,8-106,0 arası −8 dB. |
| D-B7 KÜÇÜK · "Cut it!" / ton çelişkisi | **KABUL** | Kayıt listesi 3. satır "Cut it. You're climbing. You climb, you fall behind." (FILM §5 Fable kararıyla aynı). Tur 1'deki "kısık ve sert, ses yükselmez" telafi notu kalktı; ton "kısık". 2. satır tek bağırış olarak kalır. |
| D-B8 KÜÇÜK · "might" koşulsuz +2 dB | **KABUL** | "+2 dB yalnız ölçümde 'might' 'reach'ten alçaksa; varsayılan 0." (§4 kayıt notu 8). |
| D-B9 KÜÇÜK · "0" iki anlamda | **KABUL** | C05 tutulan nefes ve C09 tutulan nefes hücrelerinde "yok" yazıldı (§5). |
| D-B10 KÜÇÜK · A4c gerçek zaman değil | **KABUL** | Zamanlama aynı (9,0 → C05 0,3; tıklar 9,2 ve 0,1). 8. satır notu: "C04'ten belirgin yorgun, dakikalar sonra". Sela'nın nefes türü (gergin düzenli → sakin-ağır) C05 0,0'da çapraz geçişsiz değişir; fan kesintisiz kalır. Tur 1'deki "S4'te zaman atlaması sesle işaretlenmez" cümlesi düzeltildi: işaret nefes türüdür. |
| K-B2 (ses tarafı) · C11 6,0-10,0 sakinlik | **KABUL** | Ses planı zaten "yalnız fan ve nefes (4 s)" diyordu; müzik tarafı §9'a bağlandı: 106,0-110,0 L3 yok; 110,0'daki varış darbesi 4 s sakinlikten sonra gelir. Müzik karşı planı bu aralığa girerse çatışma Fable'a gider. |
| K-B1 · K-B3 · K-B4 · K-B5 · K-B6 | kapsam dışı | Besteci planına ait (L1 frekansı, kesme saniyesi, çözülme, L2 yönü, dinamik tablo). Ses tarafı tek not düşer: §9, "L1 taşıyıcısı 150-400 Hz'e alınırsa fanla aynı banttadır". |

Tur 1'e göre kendi düzeltmelerim (eleştirmen bulmadı, kontrolde çıktı):
1. **C10 hışırtı çelişkisi:** tur 1 "konuşma sırasında −28" kuralını koyup C10'da replik 11 altında −16 bırakmıştı. Kural her yerde uygulandı (C10 4,0-6,0 ve C12 4,0-4,8 replik altı −28).
2. **C11 hattı açık ama hışırtısız:** tık 1,8-6,0 arası hat açıktı, hışırtı yazılmamıştı. Eklendi (−24).
3. **T2 süre toplamı:** "0,15 s atak + 3,1 s düz + 0,4 s kuyruk" 3,65 s ediyordu, tablo 3,3 s diyordu. Atak 0,15 + düz 2,75 + kuyruk 0,4 = 3,3 s (3,7-7,0).
4. **KORUNAN fark:** tur 1 "≥ 30 dB" yazmıştı; tablo değerlerinden (fan −26, varış darbesi −6) tepe farkı 20 dB çıkar. 20 dB yazıldı.
5. **İletim hışırtısı satırları:** C01-C05 iletimleri için efekt listesinde satır yoktu (yalnız §0 kuralı vardı). Eklendi (K3, −28).

## 2. SAHNE TABLOSU (FILM.md §6'ya taşınır)

Köprü sütunu = o çekimden sonraki kesme. J = sonraki sesin önden girmesi, L = bu sesin taşması.
Replik saniyeleri parantez içinde.

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | K1 fan · K2 tutamaktan gelen alçak mekanik titreşim (0-6 s) + Sela nefesi · K3 Bram tık 1,7, acılı nefes 2,0, replik 1 (3,0), tık 4,3 · K4 müzik 4,2'den (besteci) | **J 1,5 s:** Sela'nın nefesi 8,5'ten hızlanır, tıslama kesmeyle başlar | Kopuk uç ve Bram'ın sürüklenmesi sessiz: hiçbiri Sela'nın gövdesine değmiyor. Dış ses yok. |
| S2 (C02) | K1 fan · K2 tıslama T1 (düşük itki, uzun) + hızlanan nefes · K3 Bram tık 2,3, replik 2 (2,5; filmin tek bağırışı), tık 4,3 · K4 müzik | **L 1,6 s:** tıslama kesmenin üstünden C03 1,6'ya sürer, seviye değişmez | Büyüyen kehribar ışık sessiz; yaklaşmayı tıslama ve nefes taşır. Bram'ın sesi telsiz filtresinde hafif bozulur. |
| S3 (C03) | K1 fan · K2 tıslama (0-1,6) → valf tok sesi 1,6 → Sela nefesi çekilir/titrer · K3 Bram tık 0,8, replik 3 (1,0), ağır nefes, tık 6,2; Sela replik 4 (6,4) kask içi · K4 müzik | **Köprü yok (planlı):** ≈10 dk atlaması; fan kesintisiz sürer | Tıslama "Cut it." bitiminden 0,1 s sonra (1,6) **temiz kesilir, kuyruk yok:** emir ile uyma arası 0,1 s okunmalı. 4,4-6,1 yalnız Bram'ın ağır nefesi. |
| S4 (C04) | K1 fan · K2 Sela nefesi (gergin, düzenli) · K3 Bram replik 5 (0,8), Sela 6 (3,7), Bram 7 (6,2); tıklar 0,6 · 3,3 · 6,0 · 9,2 · K4 müzik (35,4'e dek) | **Köprü yok:** C04 sonu tık 9,2, C05 başı tık 0,1; aradaki 0,9 s yalnız fan. Nefes türü C05 0,0'da çapraz geçişsiz değişir (dakikalar geçti) | Işığın ve ufkun inişi sessiz. Kural bilgisi tamamen sözde. Zaman atlamasını fan değil nefes türü ve Bram'ın yorgun tonu işaretler. |
| S5 (C05) | K1 fan · K2 Sela nefesi (4,5'te son alım → tutulur → 7,0'da bırakılır) · K3 Bram tık 0,1, replik 8 (0,3-6,0, iki tirede alınamayan nefes), tık 6,2 · K4 **yok** | **Köprü yok:** "Sunrise." C06 1,2'de, 5,2 s boşluk sabit | 6,2-10,0 = 3,8 s yalnız fan, 7,0 bırakılan nefes, 8,6 tek yavaş nefes. Filmin sessizlik olayı. Müzik 35,4'ten 54,8'e kadar yok. |
| S6 (C06) | K1 fan · K2 Sela alımı 1,0, tıslama T2 3,7-7,0 (sert tek itiş) · K3 Sela replik 9 (1,2) kask içi; **tık 8,8 + hışırtı 8,8'den** · K4 L1 4,8-10,0 (besteci; 60,0'da kalkar) | **J 1,2 s:** tık ve hışırtı C06 8,8'den girer. Müzik görüntü kesmesinde (60,0) kalkar: planlı | Tıslama S2'ninkinden ayrı karakterde: kısa, sert, yüksek basınç. 7,0-8,8 yalnız fan (ve L1). 8,8 tıkı: Bram tuşa bastı, konuşamıyor. |
| S7 (C07) | K1 fan · K2 Sela nefesi, eldivenin giysiden uzaklaşan sürtmesi (2,0-4,5), bırakılan uzun nefes 4,5 · K3 açık hat hışırtısı (−16; "Bram?" altında −28), Sela replik 10 (1,5), Bram'ın yarım alımı 3,0, ağır nefesler, seyrelme · K4 **yok** | **L 1,0 s:** hışırtı C08 0,0-1,0 arasında −16'dan −27'ye süzülür | **Tıslama yok ve başlangıç tıkı yok** (hat 58,8'den beri açık). Düzeltmenin "harcanmadığı" tıslamanın yokluğu ve 4,5 nefesiyle okunur. Bram'ın nefesi 8,1'den seyrelir, 10,0'da yalnız hışırtı: "gidiyor", "sustu" değil. |
| S8 (C08) | K1 fan · K2 Sela nefesi (1,8'de takılan alım) · K3 hat hışırtısı (−27) · K4 yok | **Köprü yok:** hışırtı ve fan kesintisiz (≈2 dk atlaması) | Gün doğuşu sessiz. Ödülü ses vermez; Bram'ın susması sürer. Müzik yok. |
| S9 (C09) | K1 fan · K2 Sela nefesi (tutulur 2,8-4,6, hızlanır 6,5'ten), ip silkinmesi 9,75 · K3 hat hışırtısı (−27) · K4 yok | **J 0,25 s + L 1,5 s:** silkinme C09 9,75'te, ip titreşimi C10 1,5'e kadar sürer | Iska anı (3,5) sessiz: Sela'nın tuttuğu nefes bu çekimin tek tepkisi. Silkinme görüntüden **önce** gelir (C09'da Sela kıpırtısız). Müzik yok. |
| S10 (C10) | K1 fan · K2 ip titreşimi kuyruğu (0-1,5), Sela nefesi (6,3'te takılır) · K3 hışırtı (−27 → 3,5'te −16 → 4,0-6,0 replik altı −28), Bram'ın giysi hışırtısı (2,0-4,5), toparlanma soluğu 3,6, replik 11 (4,0), bitiş tıkı 6,1 · K4 L1 6,8'den (besteci) | **Köprü yok:** nefes sürer, fan kesintisiz | Başlangıç tıkı **yok** (hat açık). 6,1 tıkıyla hışırtı da kesilir: açık hat ilk kez ve Bram'ın eliyle kapanır. 6,1-6,8 arası yalnız fan ve Sela'nın nefesi (A8'in tepkisi). |
| S11 (C11) | K1 fan · K2 Sela alımı **1,5**, tıslama T3 (2,5-4,5; yumuşak), ip yükü darbesi 2,6, Sela nefesi · K3 Bram tık 1,8, hışırtı 1,8-6,0, konuşmak için alım 2,0, nefes-gülüş 5,3, tık 6,0 · K4 müzik 1,8-6,0 L3 −8 dB; **6,0-10,0 L3 yok** | **Köprü yok:** C12 0,0'daki darbe planlıdır | Tıslama S6'dan yumuşak ve kısa (ip ikinci gövdeyi taşıyor). Bram'ın alımı S7 3,0 ile aynı doku. 6,0-10,0 = 4 s yalnız fan ve sakinleşen nefes (darbeden önceki sakinlik). |
| S12 (C12) | K1 fan · K2 varış darbesi 0,0 (gövdeden), Sela nefesi (titrek → 8,0'dan oturur) · K3 Bram tık 1,0, sığ düzenli nefes, açık hat hışırtısı (−18; replik altı −28), replik 12 (4,0); **bitiş tıkı yok** · K4 müzik 0,0-3,2'ye dek (besteci; tercih 113,2'de kesilir) | Çıkış yok (film sonu) | **İç hacim uğultusu yok:** açık kapak hâlâ vakum. Sert ses kesmesi: C11'in 4 s sakini sonrası 0,0'daki darbe. 4,8-8,0 arası 3,2 s cevap boşluğu müziksiz: yalnız fan, hışırtı, Bram'ın sığ nefesi ve Sela'nın titreği. |

## 3. ORTAM (FILM.md §6 satırı için)

```
Ortam: Vakum dışı: dış ses yok, kulak Sela'nın kaskında. Duyulan yalnız: kask içi (fan, nefes, tıslama) · gövdeden
       (eldiven-tutamak, valf, kemer/ip, varış darbesi) · telsiz (Bram'ın mikrofonu kendi kaskında; motor ve ortam
       gürültüsü yok, hışırtı ve tık telsizin kendisi; hat C06 8,8'de açılır, C10 6,1'de kapanır). İç hacim ve ince
       atmosfer bu filmde yok (C12'nin açık kapağı dahil). Ortam yatağı (fan) film boyu kesintisiz; dijital sıfır yok.
       Model sesi kullanılmaz (Return silent videos; ses kurguda).
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_2.md
```

## 4. KAYIT LİSTESİ

Ses aracı sahibindir; profil adları araçtan bağımsızdır. Hepsi `HUMAN`, hepsi kurguda yerleşir.
**Model sesi yok, `model` filtreli satır yok:** ağız kadrajda replik bulunmuyor (FILM §4 AĞIZ notları, 12/12 telsiz ya da kask içi).
Profil adları: **BRAM_52_bariton** (diyalog_3 §4) · **SELA_29_alto** (diyalog_2 §4, değişmedi). Film boyu tek profil.

| No | Metin | Konuşan | Ses profili | Ton | Hedef süre | Filtre | Çekim · saniye | Seviye |
|:--:|---|---|---|---|:--:|---|---|:--:|
| 1 | Lost my jets. | Bram | BRAM_52_bariton | kuru | 1,1 | telsiz | C01 · 3,0 | 0 |
| 2 | No, no— don't burn at me! | Bram | BRAM_52_bariton | telaşlı | 1,6 | telsiz (+hafif aşırı yük) | C02 · 2,5 | +2 (tek bağırış) |
| 3 | Cut it. You're climbing. You climb, you fall behind. | Bram | BRAM_52_bariton | kısık | 3,4 | telsiz | C03 · 1,0 | 0 |
| 4 | Copy. Down to two. | Sela | SELA_29_alto | düz | 1,4 | oda (kask içi: yakın, kuru, yankısız) | C03 · 6,4 | −2 |
| 5 | Turn your back on me— and brake. | Bram | BRAM_52_bariton | ağır | 2,3 | telsiz | C04 · 0,8 | 0 |
| 6 | Negative. I can see you. | Sela | SELA_29_alto | kesik | 1,6 | oda (kask içi) | C04 · 3,7 | −2 |
| 7 | At sunrise, I'm right in front of you. | Bram | BRAM_52_bariton | sakin | 2,8 | telsiz | C04 · 6,2 | 0 |
| 8 | At me— you're home. Away from me— you might reach me. Last one's for both. Your call. | Bram | BRAM_52_bariton | dürüst (not 8) | 5,7 | telsiz | C05 · 0,3 | 0 |
| 9 | Sunrise. You be there. | Sela | SELA_29_alto | titrek | 1,8 | oda (kask içi) | C06 · 1,2 | −2 |
| 10 | Bram? | Sela | SELA_29_alto | çıplak | 0,6 | oda (kask içi; fısıltıya yakın) | C07 · 1,5 | −6 |
| 11 | I heard you. In the dark. | Bram | BRAM_52_bariton | alçak | 2,0 | telsiz | C10 · 4,0 | 0 |
| 12 | Good call. | Bram | BRAM_52_bariton | kuru | 0,8 | telsiz | C12 · 4,0 | 0 |

```
KAYIT NOTLARI
TELSİZ FİLTRE ZİNCİRİ  Bant geçiren yaklaşık 300-3400 Hz (alt kesim 12 dB/oktav, üst kesim 18 dB/oktav) · hafif doygunluk
                       (%2-3, gözle görülür kırpma yok) · mono, merkez · önünde ve arkasında 80 ms'lik squelch kuyruğu
                       olan yumuşak tık (tek tık, çift değil) · iletim sırasında −28 dB taşıyıcı hışırtısı.
KASK İÇİ SELA          Filtresiz, mono, yakın mikrofon, yankı yok. Telsiz zincirine girmez, tıksızdır.
Tek bağırış            Yalnız 2. satır. +2 dB'e kadar, limitere girmeden. Diğer satırların hiçbiri yükselmez.
Not 3                  Tek take. Kurgu işaretleri: "Cut it" bitişi + 0,1 s = tıslama kesilir (nominal 1,6) · "climbing." ile
                       "You climb" arasında 0,4 s'lik ağır nefes boşluğu take'in içindedir (ayrı kayıt değil).
                       Ton "kısık"; noktalama nokta olduğu için ses aracı bağırtmaz.
Not 8                  Tek take. Dahili zamanlama (satır başına): At me 0,0 · you're home 0,8 · Away from me 1,6 ·
                       you might reach me 2,6 · Last one's for both 3,8 · Your call 5,1-5,7. Tirelerdeki iki duraklama
                       alınamayan nefes olarak kaydedilir (efekt değil). "might" net ama vurgusuz; önünde duraklama yok.
                       TON: "dürüst; C04'ten belirgin yorgun, dakikalar sonra" (C04'teki 5, 7. satırlardan daha yavaş, daha az dolu).
                       MİKS: "might" hecesine +2 dB (2-3 kHz) YALNIZ ölçümde "might" "reach"ten alçaksa; varsayılan 0.
Not 10                 Fısıltıya yakın, soru tonuyla yükselmez; telsizin açık olduğunu bilen ama cevap beklemeyen biri.
                       Seviye −6 (Sela'nın öteki satırlarından 4 dB alçak); hışırtı altında −28'e iner (§5 C07).
```

### 4b. Sözsüz kayıtlar (replik değil; aynı oturum, aynı mikrofon)

Bram'ın C07 3,0, C10 3,6 ve C11 2,0'daki alımları **aynı oturumda ve aynı mikrofonla** kaydedilir. Aynı oturumda Sela'nın nefes seti de alınır.

| No | Ne | Kimin | Süre | Yer | Not |
|:--:|---|---|:--:|---|---|
| N1 | acılı tek nefes (göğüs yaralı, kısa) | Bram | 0,6 | C01 · 2,0 | repliğin altına binmez, önce biter |
| N2 | ağır nefes arası ("climbing." ile "You climb" arası) | Bram | 0,4 | C03 · ~3,0 | 3. satırın take'inde; ayrı dosya gerekmez |
| N3 | ağır nefes dizisi, tek başına | Bram | 1,7 | C03 · 4,4-6,1 | 2 nefes, C02'dekinden ağır |
| N4 | konuşmak için alım: kısa, yükselen soluk, ünlüye varmadan bırakılır | Bram | 0,5 | C07 · 3,0 · C11 · 2,0 | **aynı doku iki yerde**; 3 take alınır, birbirine en yakın ikisi gider |
| N5 | ağır nefes dizisi, sonu seyrelen (4 nefes: 2 tam, 1 yarım, 1 zayıf) | Bram | 5,0 | C07 · 4,9-9,4 | son iki nefes −6 ve −12 dB'ye iner, kesilmez |
| N6 | toparlanma soluğu: derin, takılan iç çekiş | Bram | 0,8 | C10 · 3,6 | C07'de yarım kalan alım bu kez tamamlanır |
| N7 | nefes-gülüş (burundan, kısa) | Bram | 0,5 | C11 · 5,3 | gülüş değil, "kabul" |
| N8 | sığ ve düzenli nefes (hat altında) | Bram | 9,0 | C12 · 1,0-10,0 | Sela'nınkinin altında; ritim film içinde yeni, düzen "yaşıyor" der |
| N9 | Sela nefes seti: sakin-gergin · sakin-ağır · hızlanan · hızlı düzensiz · çekilen/titrek · tutulup bırakılan · takılan alım · oturan | Sela | 8 tür | tüm çekimler (§5) | her tür 3-6 s'lik ayrı kayıt. "Sakin-ağır" yeni (C05 0-4,5; D-B10) |

## 5. EFEKT LİSTESİ

Seviye: 0 dB = Bram telsiz replik ortalaması. Kaynak: gövde / hava / kask içi. **Hava kaynaklı satır yoktur** (vakum).
"Nereden": kütüphane arama terimi ya da tek satır İngilizce üretim promptu; N-no = §4b kaydı. "tık" = §7. "hışırtı" = C06 satırındaki carrier varlığı.

| Çekim | Saniye | Ses | Kaynak | Katman | Seviye | Nereden |
|:--:|---|---|---|:--:|---|---|
| C01 | 0,0-10,0 | kask içi fan uğultusu, sürekli yatak (tüm film bu varlığı kullanır) | kask içi | K1 | −26 | `a low steady fan hum inside a spacesuit helmet, close and dry, no rhythm, no echo, no voices, seamless loop` (140 s üret, 8 s çapraz geçişle döngüle) |
| C01 | 0,0-6,0 · 6,0 | istasyon yapısından eldivene gelen çok alçak mekanik titreşim; 6,0'da yumuşak duruş | gövde (eldiven-tutamak) | K2 | −24 | `very low machinery vibration felt through a metal handrail and glove, muffled, no air, six seconds then a soft stop` |
| C01 | 0,0-10,0 | Sela nefesi sakin-gergin; 8,5'ten hızlanan | kask içi | K2 | −14 → −11 | N9 |
| C01 | 1,7 · 4,3 | Bram: başlangıç tıkı, bitiş tıkı; aralarında iletim hışırtısı | kask içi (telsiz) | K3 | tık −10 · hışırtı −28 | `a single soft radio push-to-talk click with a short squelch tail, dry` · hışırtı |
| C01 | 2,0 | Bram'ın acılı nefesi | kask içi (telsiz) | K3 | −8 | N1 |
| C02 | 0,0-10,0 | tıslama T1 (düşük itki, ince, uzun) + giysi titremesi aynı sesin alçak bileşeni | kask içi | K2 | −14 (Bram bağırırken 2,5-4,1 arası −17) | `a thin steady low-pressure gas thruster hiss with a faint suit rattle, heard inside a helmet, close and dry, no echo, 12 seconds, no decay` |
| C02 | 0,0-10,0 | Sela nefesi hızlanan, sonra hızlı düzensiz | kask içi | K2 | −14 → −9 | N9 |
| C02 | 2,3 · 4,3 | Bram tık / bitiş tıkı (bağırış sırasında telsiz doygun); iletim hışırtısı | kask içi (telsiz) | K3 | tık −10 · hışırtı −28 | tık · hışırtı |
| C03 | 0,0-1,6 · 1,6 | tıslama T1 sürer, 1,6'da **kuyruksuz kesilir**; kesilme anında valf kapanış sesi | kask içi + gövde | K2 | tıslama −14 · valf −18 | `a short muffled metallic valve clunk heard through a pressure suit, no air, close and dry` |
| C03 | 0,8 · 4,4-6,1 · 6,2 | Bram tık, ağır nefes dizisi (N3), bitiş tıkı; iletim hışırtısı 0,8-6,2 | kask içi (telsiz) | K3 | N3 −9 · tık −10 · hışırtı −28 | N3 · tık · hışırtı |
| C03 | 1,7-10,0 | Sela nefesi: 1,7'de açık ve hızlı, 4,4-6,3 arası −24'e **çekilir** (utanç boşluğu; tam sessizlik değil), 7,8'den titrek | kask içi | K2 | −12 → −24 → −13 | N9 |
| C04 | 0,6 · 3,3 · 6,0 · 9,2 | Bram tıkları (her iletimin başı/sonu); iletim hışırtısı 0,6-3,3 ve 6,0-9,2 | kask içi (telsiz) | K3 | tık −10 · hışırtı −28 | tık · hışırtı |
| C04 | 0,0-10,0 | Sela nefesi gergin, düzenli; "Negative" öncesi 3,5'te kısa sert alım | kask içi | K2 | −16 | N9 |
| C04 | 0,0-10,0 | (ışığın ve ufkun inişi: kulakta karşılığı yok, bilinçli) | — | — | — | — |
| C05 | 0,1 · 6,2 | Bram tık / bitiş tıkı; iletim hışırtısı 0,1-6,2 | kask içi (telsiz) | K3 | tık −10 · hışırtı −28 | tık · hışırtı |
| C05 | 0,3-6,0 | iki tirede alınamayan nefes (0,6-1,1 ve 2,5-2,9 arası, replik take'inin içinde) | kask içi (telsiz) | K3 | −9 | 8. satır take'i |
| C05 | 0,0-4,5 | Sela nefesi **sakin-ağır** (C04'ün gergin nefesinden çapraz geçişsiz değişir) | kask içi | K2 | −15 | N9 |
| C05 | 4,5-4,8 · 4,8-7,0 · 7,0 | **son alım 4,5'te** ("Last one's"tan sonra, "for both" üstüne; kısa, 0,3 s) → tutulur (yok) → **7,0'da uzun bırakma** (dönüşün durduğu an) | kask içi | K2 | alım −12 · tutma yok · bırakma −11 | N9 |
| C05 | 6,2-10,0 | **sessizlik olayı:** yalnız fan; 7,0 bırakma; 8,6'da tek yavaş nefes | kask içi | K1+K2 | fan −26 · 8,6 nefes −18 | fan · N9 |
| C06 | 1,0 | Sela repliğinden önce kısa alım | kask içi | K2 | −15 | N9 |
| C06 | 3,7-7,0 | tıslama T2: **sert tek itiş**, 0,15 s atak, 2,75 s düz, 0,4 s yumuşak kuyruk | kask içi | K2 | pik −6 · gövde −8 | `a short hard gas thruster burst with a fast attack and a steady hiss, heard inside a helmet, close and dry, no echo, three seconds` |
| C06 | **8,8** | Bram'ın **başlangıç tıkı**: tuşa basıldı, bırakılmaz (D-B2) | kask içi (telsiz) | K3 | −10 | `a single soft radio push-to-talk click with a short squelch tail, dry` (C01 ile aynı varlık) |
| C06 | 8,8-10,0 | taşıyıcı hışırtı tıkla girer: 8,8 −24 → 9,5 −16 | kask içi (telsiz) | K3 | −24 → −16 | `steady radio carrier static hiss through a band-pass radio filter, no voice, no music, seamless loop` |
| C07 | 0,0-10,0 | açık hat hışırtısı; 1,4-1,5 arası −28'e iner, 2,1-2,4 arası −16'ya döner | kask içi (telsiz) | K3 | −16 (1,5-2,1 arası −28) | yukarıdaki hışırtı |
| C07 | 0,0-2,0 | Sela nefesi kısa-sığ; "Bram?" öncesi 1,0'da takılan alım | kask içi | K2 | −15 | N9 |
| C07 | 2,0-4,5 | eldivenin göğüs plakasından uzaklaşırken yumuşak sürtmesi | gövde (eldiven-giysi) | K2 | −24 | `soft stiff glove fabric sliding off a suit chest panel, muffled, inside the suit, close and dry` |
| C07 | 3,0 | Bram'ın konuşmak için alımı, kelimeye varmaz | kask içi (telsiz) | K3 | −8 | N4 |
| C07 | 4,5 | Sela'nın uzun bırakılan nefesi (el durduğu an; "harcanmadı") | kask içi | K2 | −11 | N9 |
| C07 | 4,9-9,4 | Bram'ın ağır nefesleri: 4,9 · 6,5 tam; 8,1 yarım (−4); 9,4 zayıf (−10) | kask içi (telsiz) | K3 | −10 → −20 | N5 |
| C08 | 0,0-1,0 | hışırtı −16'dan −27'ye süzülür (L-kesme), sonra sabit | kask içi (telsiz) | K3 | −27 | hışırtı |
| C08 | 1,8-10,0 | Sela'nın takılan alımı (Bram'ı fark ettiği an), 2,4-3,6 titrek çıkış, 6'dan sonra alçak ve düzenli | kask içi | K2 | −12 → −18 | N9 |
| C09 | 0,0-10,0 | hışırtı | kask içi (telsiz) | K3 | −27 | hışırtı |
| C09 | 2,8-4,6 · 4,6 · 6,5-9,7 | Sela nefesi **tutulur** (Bram yaklaşırken) → ıskadan sonra bırakılır → atış hazırlığında hızlanır | kask içi | K2 | tutma yok / bırakma −12 / −13 → −10 | N9 |
| C09 | 9,75 | ip silkinmesi: tok, boğuk tek darbe; ardından 120 Hz dolayı ip titreşimi 1,5 s (C10'a taşar) | gövde (kemer-ip) | K2 | darbe −6 · titreşim −18 | `a single muffled taut-rope jerk through a harness, one low thump followed by a fading low hum, no air, close and dry` |
| C10 | 0,0-1,5 | ip titreşimi kuyruğu | gövde | K2 | −18 → −40 | (C09 9,75 varlığının uzantısı) |
| C10 | 0,0-3,5 · 3,5-3,9 · 4,0-6,0 | hışırtı −27; 3,5-3,9 arası −16'ya **yükselir** (hat canlanıyor); replik 11 altında −28'e iner | kask içi (telsiz) | K3 | −27 → −16 → −28 | hışırtı |
| C10 | 2,0-4,5 | Bram'ın giysi hışırtısı, kolu kalkarken (kendi mikrofonundan telsize) | kask içi (telsiz) | K3 | −22 | `soft muffled suit fabric rustle picked up by a helmet microphone, close, no air` |
| C10 | 3,6 | toparlanma soluğu (Bram) | kask içi (telsiz) | K3 | −6 | N6 |
| C10 | 6,1 · 6,3-10,0 | bitiş tıkı: hat kapanır, **hışırtı da kesilir**; 6,3'te Sela'nın takılan nefesi, sonra titrek-yavaşlayan | kask içi | K3 · K2 | tık −10 · nefes −11 → −16 | tık · N9 |
| C11 | 1,5 | Sela'nın sert alımı (Bram'ın tıkından ÖNCE; D-B6) | kask içi | K2 | −12 | N9 |
| C11 | 1,8 · 1,8-6,0 · 2,0 | Bram tık; açık hat hışırtısı; konuşmak için alım (C07 3,0 ile aynı doku) | kask içi (telsiz) | K3 | tık −10 · hışırtı −24 · alım −8 | tık · hışırtı · N4 |
| C11 | 2,5-4,5 | tıslama T3 (yumuşak, 0,3 s kuyruk) | kask içi | K2 | −12 | `a soft short gas thruster hiss with a gentle fade-out, heard inside a helmet, close and dry, no echo, two seconds` |
| C11 | 2,6 | ip yükünün yumuşak darbesi (ip ikinci gövdeyi çeker) | gövde (kemer-ip) | K2 | −20 | C09 silkinmesinin yarı seviyeli, kısa varyantı |
| C11 | 5,3 · 6,0 | nefes-gülüş; bitiş tıkı (hışırtı da kesilir) | kask içi (telsiz) | K3 | −10 · tık −10 | N7 · tık |
| C11 | 6,0-10,0 | Sela nefesi sakinleşir; yalnız fan ve nefes (4 s) | kask içi | K1+K2 | fan −26 · nefes −17 | fan · N9 |
| C12 | 0,0 | varış darbesi: eldivenin tutamağı kavraması, ilk karede; 0,6 s'lik alçak kuyruk | gövde (eldiven-tutamak) | K2 | −6 (filmin en yüksek efekti) | `a single muffled thud of a gloved hand gripping a metal handle, transmitted through a pressure suit, no air, close and dry` |
| C12 | 0,0-8,0 · 8,0-10,0 | Sela'nın titrek nefesi; 8,0'dan oturan | kask içi | K2 | −13 → −16 | N9 |
| C12 | 1,0 · 1,0-10,0 | Bram tık; açık hat hışırtısı (4,0-4,8 replik altı −28, 4,9'da 0,3 s'de geri) ve sığ-düzenli nefes; **bitiş tıkı yok** | kask içi (telsiz) | K3 | tık −10 · hışırtı −18 · nefes −17 | tık · hışırtı · N8 |
| C12 | 9,85-10,0 | son 150 ms'de hepsi −40'a iner (tıkırtı koruması; müzik fade-out'u değil, yalnız kapanış tıkırtısını önler) | — | — | — | — |

## 6. ORTAM YATAĞI (sahne başına tek satır)

Yatak = K1 fan. Hat durumu (hışırtı) K3'tedir ve ayrı satırdır. Fan film boyu tek varlıktır; sahne arası fark seviyede değil, kulağın neyi duyduğundadır.

| Sahne | Ne · seviye · nereden |
|:--:|---|
| S1 | kask içi fan, sürekli, ritimsiz (`low steady fan hum inside a spacesuit helmet, no rhythm`) · −26 · fan varlığı (140 s) |
| S2 | aynı fan, aynı seviye; üstüne tıslama biner · −26 · aynı |
| S3 | aynı fan; 1,6'da tıslama kesilince fan ilk kez çıplak duyulur · −26 · aynı |
| S4 | aynı fan; kesmede fan değişmez, zaman atlamasını nefes türü işaretler · −26 · aynı |
| S5 | aynı fan; 6,2-10,0 arası tek yatak, 3,8 s · −26 · aynı |
| S6 | aynı fan; 7,0-8,8 arası yalnız yatak; 8,8'den tık + hışırtı (hat açıldı) · fan −26 · hışırtı −24 → −16 · aynı |
| S7 | aynı fan + açık hat hışırtısı · fan −26 · hışırtı −16 (Sela konuşurken −28) · aynı |
| S8 | aynı fan + alçak hışırtı · −26 / −27 · aynı |
| S9 | aynı fan + alçak hışırtı · −26 / −27 · aynı |
| S10 | aynı fan; 6,1'de hışırtı kesilince yalnız fan kalır · −26 · aynı |
| S11 | aynı fan; 1,8-6,0 arası hat açık (−24); 6,0-10,0 yalnız yatak ve nefes · fan −26 · aynı |
| S12 | aynı fan (iç hacim uğultusu **yok**) + açık hat hışırtısı · fan −26 · hışırtı −18 · aynı |

```
Fan varlığı  100-600 Hz'de geniş bant, ritim ve ton sürünmesi yok (hışırtı 1-3 kHz'dedir, bantlar ayrı kalır).
             Stereo: iki kanal ilintisiz gürültü, orta-alçak; mono toplamda en çok −2 dB kayıp. Telsiz ve kask içi replik: mono, merkez.
```

## 7. TIK DİLİ VE TIŞLAMA TABLOSU

| Çekim | Başlangıç tıkı | Bitiş tıkı | Anlam |
|:--:|:--:|:--:|---|
| C01 | 1,7 | 4,3 | tek iletim |
| C02 | 2,3 | 4,3 | tek iletim (bağırış) |
| C03 | 0,8 | 6,2 | Bram tuşu 6,2'de bırakır; Sela'nın cevabı kaskından duyulur |
| C04 | 0,6 · 6,0 | 3,3 · 9,2 | iki ayrı iletim; Sela tıksız |
| C05 | 0,1 | 6,2 | tek iletim; sonrası 3,8 s sessizlik; hat kapanır |
| C06 | **8,8** | — | **Bram tuşa basar, bırakmaz** (D-B2); hat açılır |
| C07 | **yok** | — | hat C06 8,8'den beri açık; "basıldı, bırakılmadı" |
| C08-C09 | — | — | açık hat, alçak |
| C10 | **yok** | 6,1 | açık hat boyunca Bram ilk kez kendisi kapatıyor |
| C11 | 1,8 | 6,0 | tuşa yeniden basıyor, konuşmadan bırakıyor |
| C12 | 1,0 | **yok** | hat açık kalır |

Toplam 17 tık (tur 1: 16). Hat açık süresi tek parça: 58,8 → 96,1 (mutlak).

| Ateşleme | Yer | Süre | Işık | Karakter | Seviye | Bitiş |
|---|---|:--:|:--:|---|---|---|
| T1 | C02 0,0 → C03 1,6 | 11,6 s | 2 (4→2) | düşük itki, ince, uzun | −14 | **kuyruksuz kesilir** + valf tok (emire uyma) |
| T2 | C06 3,7-7,0 | 3,3 s | 1 (2→1) | sert tek itiş, yüksek basınç | pik −6, gövde −8 | 0,4 s yumuşak kuyruk (süre içinde) |
| T3 | C11 2,5-4,5 | 2,0 s | 1 (1→0) | yumuşak, ip yükü altında | −12 | 0,3 s kuyruk |

Süre oranı (11,6 : 3,3 : 2,0) ışık sayısına (2 : 1 : 1) orantılı değil; fark **itki sertliğiyle** taşınır: uzun ince tıslama bir gaz yavaşça gider, kısa sert itiş bir ışık tek vuruşta gider. T2/T3'ü orantılı uzatmak C06 7,0'da biten ışık küçülmesini ve C11'in diyalog zamanlamasını (gülüş 5,3) bozar; yapılmadı. F8'de kulak yine "2 ışık / 1 ışık / 1 ışık" okumazsa süre eklenmez; C03 gösterge insert'i görüntü tarafında güçlendirilir.

## 8. DİYALOG GECİKMELERİNİN DOĞRULANMASI (kesme gecikmeyi yemez)

| Alışveriş | Gecikme (diyalog) | Bu planda | Durum |
|---|:--:|---|:--:|
| A3b | 2,0 s | Bram 4,4 → Sela 6,4 (araya yalnız N3 ve tık 6,2) | tutuyor |
| A4a | 0,6 s | 3,1 → 3,7 (tık 3,3 içeride) | tutuyor |
| A4b | 0,9 s | 5,3 → 6,2 | tutuyor |
| A4c | 1,3 s | 9,0 → C05 0,3 (tıklar 9,2 ve 0,1). Ses saatinde 1,3 s; görüntü saatinde dakikalar (D-B10): nefes türü ve ton bunu taşır | tutuyor |
| A5 | 5,2 s | C05 6,0 → C06 1,2 (J-kesme yok) | tutuyor |
| A6 | 0,7 s | 3,0 → 3,7 | tutuyor |
| A7 | 0,9 s | 2,1 → 3,0 (Bram'ın alımı). Yeni öncül: tık C06 8,8 → "Bram?" C07 1,5 (2,7 s), A7'nin kendi gecikmesine dokunmaz | tutuyor |
| A8 | 0,3 s | Bram 6,0 → Sela'nın nefesi 6,3 | tutuyor |
| A9a | 0,5 s | Bram alımı 2,0 → T3 2,5 (Sela'nın alımı 1,5'e taşındı, gecikmeyi etkilemez) | tutuyor |
| A9b | 0,8 s | T3 bitişi 4,5 → nefes-gülüş 5,3 | tutuyor |
| A9c | 3,2 s | C12 4,8 → Sela'nın oturan nefesi 8,0 | tutuyor |

## 9. MÜZİK İÇİN SES KISITLARI (K4)

Besteci planı bu bölüme göre revize edilir. Fable kararı (60,0-96,8 müziksiz) işlendi. Mutlak saniye = 10 × (Cxx − 1) + saniye.

```
Replik yokken müzik yatağı −16…−18 LUFS; replik altında −6…−9 dB (kural 6).

MÜZİKSİZ (zorunlu):
  0,0-4,2          açılış (fan, nefes, replik 1; L1 en erken replik 1 sonu + 0,1 s)
  35,4-54,8        C04 sonu · C05 · C06'nın ilk 4,8 s (replik 7, 8, 9; doruk)
  60,0-96,8        C07 · C08 · C09 · C10'un ilk 6,8 s (Fable kararı): "Bram?" ve nefesin seyrelmesi, doğuş ödülü,
                   ıska, ip silkinmesi 89,75, toparlanma soluğu 93,6, replik 11, bitiş tıkı 96,1, Sela'nın nefesi 96,3
  106,0-110,0      C11 6,0-10,0: 4 s sakinlik, ardından 110,0 varış darbesi. L3 yok; L1 sürerse yalnız L1 ve
                   Sela'nın nefesinin ≥6 dB altında (tercih: yok)
  114,0-114,8      "Good call.": müzik yok ya da yalnız L1 −9 dB ve L3 yok (L3 telsiz bandında, 165 Hz üstü)
  117,5-120,0      Sela'nın oturan nefesi 118,0'dan ≥0,5 s önce müzik yok. TERCİH: kesme 113,2 (aşağıda)

MÜZİK ALANI (ses açısından serbest):
  4,2-35,4         C01 sonu-C04 (replik altında −8 dB; mevcut plan)
  54,8-60,0        C06'nın son 5,2 s: yalnız L1; 60,0'da (C06/C07 kesmesi) yay kalkar, kuyruk yok
  96,8-106,0       C10 sonu · C11 ilk 6,0 s; 101,8-106,0 arası L3 en çok −8 dB
  110,0-113,2      C12 ilk 3,2 s (çözülme 112,0 besteci kararı)

TERCİH (D-B5): 113,2'de kesme. Gerekçe: 114,8-118,0 (A9c, 3,2 s) cevap boşluğudur; içinde müzik olayı (117,0 kesmesi
  gibi) Bram'ın onayının ve Sela'nın cevabının yerini alır. 113,2 → 114,0 arası 0,8 s sessizlik "Good call."ı açar
  (C04 35,4 → 36,2 "At sunrise" yapısıyla aynı). İçerik seçimi (çözülme/yedek) besteciye ve F8'e aittir.
```

**Ses → besteci referans noktaları (mutlak):**

| Olay | Saniye | Not |
|---|:--:|---|
| replik 1 biter | 4,1 | L1 girişi buna bağlı (≥ +0,1 s) |
| replik 6 biter | 35,3 | susma "replik 6 sonu + 0,1 s" olarak kurguda ölçülür (kurgucu B3); L2 duck'ı besteci |
| replik 7 · 8 · 9 | 36,2-39,0 · 40,3-46,0 · 51,2-53,0 | müziksiz |
| C05 bırakma · 8,6 nefesi | 47,0 · 48,6 | sessizlik olayının içindeki iki nefes |
| T2 atağı | 53,7 | L1 54,8'de girer (atak + 1,1 s) |
| C06 tık + hışırtı | 58,8 | L1'in altında kalmaz; L1 60,0'da kalkar |
| "Bram?" | 61,5-62,1 | müziksiz |
| silkinme | 89,75 | müziksiz |
| replik 11 · bitiş tıkı · Sela'nın nefesi | 94,0-96,0 · 96,1 · 96,3 | L1 en erken 96,8 |
| Sela alımı · Bram tık · T3 · gülüş | 101,5 · 101,8 · 102,5-104,5 · 105,3 | L3 101,8-106,0 −8 dB; 106,0'da L3 çıkar |
| varış darbesi · Bram tık | 110,0 · 111,0 | darbe 4 s sakinlikten sonra |
| "Good call." · Sela'nın oturan nefesi | 114,0-114,8 · 118,0 | yukarıdaki sınırlar |

Bant notu (K-B1 ile ilgili): L1 taşıyıcısı 150-400 Hz'e alınırsa fan (100-600 Hz) ile aynı banttadır. Müzik çalarken fan maskelenir; ses planı için sorun değil (fan dijital sıfırı önleyen yataktır, müzik varken duyulması gerekmez). Ama müzik kesildiği her anda (35,4 · 60,0 · 106,0 · 113,2) fan seviyesi AYNI kalır ve çıplak duyulur; fan bu kesmelerde yükseltilmez, müzik kesmesi 30 ms'den uzun rampa kullanmaz. Replik altı −6…−9 dB, Sela'nın alto sesiyle (200 Hz üstü) çakışan 4. ve 6. satırlarda (26,4-27,8 · 33,7-35,3) uygulanır.

## 10. FİNAL MİKS — YÜKSEKLİK HEDEFİ

```
HEDEF       −14 LUFS integrated · ≤ −1 dBTP · stereo 48 kHz · mono uyumluluğu kontrol edilir.
YÖNTEM      1) taslağı kur (sessiz klipler + bu plandaki sesler + müzik)
            2) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4>           (ölç)
            3) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4> --uygula -o final.mp4
            İki aşamalı, doğrusal: sıkıştırma yok.
ZİRVELER    Bram'ın C02 bağırışı (+2 dB), C06 tıslama atağı (−6), C09 silkinmesi (−6) ve C12 varış darbesi (−6) filmin en yüksek
            anlarıdır; −1 dBTP tavanı bunlarda belirlenir. Müzik payı azaldı (60,0-96,8 ve 114,0 sonrası müziksiz): integrated
            ölçüm konuşmanın ve tıslamanın seviyesine daha çok bağlı. −14'e çıkarken zirveler tavana önce varırsa doğrusal
            kip yetmeyebilir (loudnorm dinamik kipe düşer). O durumda sıkıştırma eklenmez: zirve efektleri kaynakta en çok 3 dB
            indirilir (C06 atağı, C09 ve C12 darbeleri), konuşma korunur.
DİKKAT      Konuşma 25 s, film 120 s ve çoğu bölüm çıplak (fan + nefes). Integrated ölçüm sessiz bölümleri kapıdan (gating)
            atar; sayı bu yüzden konuşmanın ve tıslamanın seviyesini ölçer. Düşük teslim en ölümcül hata: ölçüm −15'in altında
            çıkarsa konuşma seviyesi yükseltilir, sıkıştırma eklenmez.
KORUNAN     C05 6,2-10,0'daki yatak (fan −26) ile C12 0,0 varış darbesi (−6) arasındaki 20 dB tepe farkı ve C11 6,0-10,0
            sakinliği ezilmez. (Tur 1'in "≥ 30 dB" ifadesi tablo değerleriyle uyuşmuyordu; düzeltildi.)
MONO        Fan ve hışırtı mono toplamda en çok −2 dB kaybeder; telsiz ve kask içi replik zaten mono.
SON KONTROL Final baştan sona kulaklıkta ve telefon hoparlöründe dinlenir. Telefonda fan duyulmuyorsa (−26'da düşük frekans
            kaybolur) fan +3 dB'ye alınır; C05 sessizliği "sıfır" gibi duyulmamalıdır. "Bram?" (−6) hışırtı altında −28'e inmiş
            olarak anlaşılır olmalı (telefon dahil).
```

## 11. DİNLEME ÖLÇÜLERİ (F8 animatik) VE AÇIK KARARLAR

1. **Baygın / ayıldı (C07 → C10):** İzleyici C07 sonunda Bram'ın nefesinin *gittiğini* duyuyor mu? C10'da hışırtı yükselince ve toparlanma soluğuyla "ayıldı" okunuyor mu? Okunmazsa: N5'in son iki nefesi daha belirgin, N6 +3 dB. Müzik artık bu aralıkta olmadığı için ölçü temiz sınanır.
2. **C07 vazgeçiş:** Tıslamanın *olmaması* ve 4,5 nefesi "yakmadı, bıraktı" diye okunuyor mu? Okunmazsa: 4,5 nefesi +3 dB ve 4,5 sonrası bir saniye Bram'ın nefesinden önce boş.
3. **C05 sessizliği:** Tutma 4,5-7,0 ve 3,8 s'lik boşluk karar olarak okunuyor mu? Okunmazsa fan seviyesi korunur, tutulan nefes uzatılmaz.
4. **C09 → C10 silkinmesi:** 9,75 darbesi atışın sonucu olarak okunuyor mu? Hızlı geçerse 0,25 s yerine 0,35 s J-kesme.
5. **Hat açılışı (yeni):** C06 8,8 tıkı + 60,0 müzik kesmesi birlikte "hat açıldı, konuşamadı / yokluk" diye okunuyor mu? Okunmazsa: tık −10 → −7 ve müzik kesmesi 59,9'a alınır (tıkın 1,1 s sonrası; tıkı müzik örtmesin).
6. **C11 → C12:** 106,0-110,0 sakinliğinden sonra 110,0 darbesi "varış" diye okunuyor mu; 4 s sakinlik boşluk gibi kalıyor mu? Kalıyorsa fan korunur, Sela nefesinin sakinleşmesi 1 s uzatılır.

```
AÇIK KARARLAR (Fable'a)
1. Tıslama oranı (§7): karakter farkıyla çözüldü; F8 kulak ölçüsüne bırakıldı. Karar gerekmez, bilgi.
2. C01 radyatör kolu titreşimi (§5, 0-6 s): gövde sesi. F8 dinlemede "dış ses" okunursa satır düşer (görüntü bilgisi taşınır, kayıp yok).
3. Müzikle olası çatışma: besteci planı 106,0-110,0 (L3 yok) ya da 114,0-120,0 (ses sınırı) kısıtlarını kabul etmezse
   çatışma Fable'a gider. Beklenti: besteci D-B5 ve K-B2'ye KABUL yazıyor.
Tur 1 §10'un 1, 3 ve 5. maddeleri kapandı (Cut it. · hat açılışı · müzik penceresi). 2 ve 4 yukarıda.
```

```
ÖZET     12/12 çekimde en az bir efekt satırı · 12 replik kayıt satırı (hepsi HUMAN, kurguda) + 9 sözsüz kayıt grubu
         katman ≤4 her sahnede · 17 tık · 3 ateşleme tıslaması (T1 T2 T3)
         model sesi: YOK (kullanılmayacak; `model` filtreli satır yok) · hava kaynaklı efekt: yok · vakumda dış ses: yok
         bulgular: D-B1…D-B10 hepsi KABUL (B5 ses sınırı olarak) · K-B2 ses tarafı KABUL · RED yok
GİRDİ    yatay_2_dk_filmler/THE_WRONG_BURN/FILM.md §1-§5 (§5 replik 3 "Cut it.")
         yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F4_ses-tasarimcisi_1.md (önceki eser)
         yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F4_besteci_1.md (karşı plan)
         yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F4_diyalog-yazari_1.md (B1-B10 + Fable kararı)
         yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F4_kurgucu_1.md (B2)
         uretim_hatti/araclar/kurgu.py (yukseklik: iki aşamalı loudnorm, doğrusal)
YAPILMADI  kulakla dinleme ve gerçek take süresi ölçümü (kayıt yok; zamanlamalar diyalog tablosu ve çekim listesi saniyelerinden)
           · kurgu.py yukseklik koşulmadı (taslak yok) · besteci_2 henüz okunmadı (paralel yazılıyor; §9 ona karşı sınanmadı)
           · F2_diyalog-yazari_3.md §2 alışveriş tablosu bu turda yeniden okunmadı (§8 gecikmeleri tur 1'den devralındı)
```
