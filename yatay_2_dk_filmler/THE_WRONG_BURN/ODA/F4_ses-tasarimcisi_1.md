# F4 · ses-tasarimcisi · tur 1 — THE_WRONG_BURN

> Faz 4 ses planı. Yerleşim: §1 sahne tablosu ve ORTAM satırı FILM.md §6'ya, §2-§5 aynen `ODA/`'da kalır.
> Saniyeler çekim içidir (0-10). Film saati = 10 × (Cxx − 1) + saniye. Çekim = sahne (S1-S12 = C01-C12).
> Seviye ölçeği: **0 dB = Bram'ın telsiz repliklerinin ortalaması.** Mutlak seviye (−14 LUFS) son aşamada
> `kurgu.py yukseklik` ile kurulur; buradaki sayılar göreli dengedir.

## 0. KARAR ÖZETİ

```
MODEL SESİ     KULLANILMAZ. Flow'da "Return silent videos" açık; sesli klip gelirse ses akışı taslakta atılır.
               Tek istisna olan "ağız kadrajda replik" bu filmde YOK (FILM §5'te 12/12 telsiz ya da kask içi).
               Video promptlarına ses satırı, replik ve efekt tarifi girmez (ses kurguda kurulur).
KULAK          Film boyu kulak Sela'nın kaskındadır. Kadrajda Sela olmasa da (C01, C08, C10, C12) ses oradan duyulur.
               Bu tek perspektif, vakumda "kim neyi nereden duyuyor" sorusunu kapatır.
ÜÇ KAYNAK      (1) kask içi: fan, Sela'nın nefesi, ateşleme tıslaması
AİLESİ         (2) gövdeden: tutamak, valf, ip silkinmesi, varış darbesi (hepsi eldiven/kemer/giysi yoluyla)
               (3) telsiz hattı: Bram'ın sesi, nefesi, tık, taşıyıcı hışırtısı (mikrofonu kendi kaskında)
KATMAN         K1 ortam yatağı (fan) · K2 efekt (kask içi + gövde) · K3 telsiz hattı + replik · K4 müzik. Sahne başına ≤4.
               Hışırtı, tık ve Bram'ın nefesi aynı telsiz zincirinden geçtiği için K3'tedir (tek filtre zinciri).
TELSİZ DİLİ    tık = Bram'ın tuşu (ses F2 B3). Başlangıç tıkının olmadığı yerde (C07, C10 başı) hat açık kaldı,
               tuşa basılmadı. Bitiş tıkı = hat kapandı (susma kararı ya da el).
HAT DURUMLARI  konuşma sırasında hışırtı −28 dB (sezilir, duyulmaz) · konuşmasız açık hat: C07 −16, C08-C09 −27,
               C10 3,5 s sonrası −16, C12 −18 · hat kapalıyken hışırtı yok (yalnız fan).
```

## 1. SAHNE TABLOSU (FILM.md §6'ya taşınır)

Köprü sütunu = o çekimden sonraki kesme. J = sonraki sesin önden girmesi, L = bu sesin taşması.

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | K1 fan · K2 tutamaktan gelen alçak mekanik titreşim (radyatör kolu 0-6 s) + Sela nefesi · K3 Bram tık, acılı nefes 2,0, replik 1 (3,0), tık · K4 müzik | **J 1,5 s:** Sela'nın nefesi 8,5'ten hızlanır, tıslama kesmeyle başlar | Kopuk uç ve Bram'ın sürüklenmesi sessiz: hiçbiri Sela'nın gövdesine değmiyor. Dış ses yok. |
| S2 (C02) | K1 fan · K2 tıslama (düşük itki, uzun) + hızlanan nefes · K3 Bram tık 2,3, replik 2 (2,5; filmin tek bağırışı), tık 4,3 · K4 müzik | **L 1,6 s:** tıslama kesmenin üstünden C03 1,6'ya sürer, seviye değişmez | Büyüyen kehribar ışık sessiz; yaklaşmayı tıslama ve nefes taşır. Bram'ın sesi telsiz filtresinde hafif bozulur. |
| S3 (C03) | K1 fan · K2 tıslama (0-1,6) → valf tok sesi 1,6 → Sela nefesi çekilir/titrer · K3 Bram tık 0,8, replik 3 (1,0), ağır nefes, tık 6,2; Sela replik 4 (6,4) kask içi · K4 müzik | **Köprü yok (planlı):** ≈10 dk atlaması; fan kesintisiz sürer | Tıslama "Cut" bitiminden 0,1 s sonra (1,6) **temiz kesilir, kuyruk yok:** emir ile uyma arası 0,1 s okunmalı. 4,4-6,1 yalnız Bram'ın ağır nefesi. |
| S4 (C04) | K1 fan · K2 Sela nefesi (gergin, düzenli) · K3 Bram replik 5 (0,8), Sela 6 (3,7), Bram 7 (6,2); tıklar 0,6 · 3,3 · 6,0 · 9,2 · K4 müzik | **Köprü yok:** C04 sonu tık 9,2, C05 başı tık 0,1; aradaki 0,9 s yalnız fan | Işığın ve ufkun inişi sessiz. Kural bilgisi tamamen sözde; sahne boyunca ses iki sesli bir diyalog. |
| S5 (C05) | K1 fan · K2 Sela nefesi (3,9'da son alım → tutulur → 6,3'te bırakılır) · K3 Bram tık 0,1, replik 8 (0,3-6,0, iki tirede alınamayan nefes), tık 6,2 · K4 **yok** | **Köprü yok (ses F2 notu 1):** "Sunrise." C06 1,2'de, 5,2 s boşluk sabit | 6,2-10,0 = 3,8 s yalnız fan ve tek bırakılan nefes. Filmin sessizlik olayı. Müzik binmez. |
| S6 (C06) | K1 fan · K2 tıslama (3,7-7,0; sert tek itiş) · K3 Sela replik 9 (1,2) kask içi · K4 müzik | **J 1,2 s:** taşıyıcı hışırtısı 8,8'den girer (işitilir hâle 9,5'te), **tıksız** | Tıslama S2'ninkinden ayrı karakterde: kısa, sert, yüksek basınç. 7,0'dan 8,8'e kadar yalnız fan. |
| S7 (C07) | K1 fan · K2 Sela nefesi, eldivenin giysiden uzaklaşan hışırtısı (2,0-4,5), bırakılan uzun nefes 4,5 · K3 açık hat hışırtısı (−16), Sela replik 10 (1,5), Bram'ın yarım alımı 3,0, ağır nefesler, seyrelme · K4 **yok** | **L 1,0 s:** hışırtı C08 0,0-1,0 arasında −16'dan −27'ye süzülür | **Tıslama yok:** düzeltmenin "harcanmadığı" tıslamanın yokluğu ve bırakılan nefesle okunur. Bram'ın nefesi 8,0'dan seyrelir, 10,0'da yalnız hışırtı: "gidiyor", "sustu" değil. |
| S8 (C08) | K1 fan · K2 Sela nefesi (1,8'de takılan alım) · K3 hat hışırtısı (−27) · K4 yok | **Köprü yok:** hışırtı ve fan kesintisiz (≈2 dk atlaması) | Gün doğuşu sessiz. Ödülü ses vermez; Bram'ın susması sürer. |
| S9 (C09) | K1 fan · K2 Sela nefesi (tutulur 2,8-4,6, hızlanır 6,5'ten), ip silkinmesi 9,75 · K3 hat hışırtısı (−27) · K4 yok | **J 0,25 s + L 1,5 s:** silkinme C09 9,75'te, ip titreşimi C10 1,5'e kadar sürer | Iska anı (3,5) sessiz: Sela'nın tuttuğu nefes bu çekimin tek tepkisi. Silkinme görüntüden **önce** gelir (C09'da Sela kıpırtısız). |
| S10 (C10) | K1 fan · K2 ip titreşimi kuyruğu (0-1,5), Sela nefesi (6,3'te takılır) · K3 hışırtı (−27 → 3,5'te −16), Bram'ın giysi hışırtısı (2,0-4,5), toparlanma soluğu 3,6, replik 11 (4,0), bitiş tıkı 6,1 · K4 müzik 6,3'ten sonra (isteğe bağlı) | **Köprü yok:** nefes sürer, fan kesintisiz | Başlangıç tıkı **yok** (hat açık kaldı). 6,1 tıkıyla hışırtı da kesilir: açık hat ilk kez kapanır. |
| S11 (C11) | K1 fan · K2 tıslama (2,5-4,5; yumuşak), ip yükünün yumuşak darbesi 2,6, Sela nefesi · K3 Bram tık 1,8, konuşmak için alım 2,0, nefes-gülüş 5,3, tık 6,0 · K4 müzik | **Köprü yok:** C12 0,0'daki darbe planlıdır | Tıslama S6'dan yumuşak ve kısa (ip ikinci gövdeyi taşıyor). Bram'ın alımı S7 3,0 ile aynı doku. |
| S12 (C12) | K1 fan · K2 varış darbesi 0,0 (gövdeden), Sela nefesi (titrek → 8,0'dan oturur) · K3 Bram tık 1,0, sığ düzenli nefes, açık hat hışırtısı (−18), replik 12 (4,0); **bitiş tıkı yok** · K4 müzik | Çıkış yok (film sonu) | **İç hacim uğultusu yok:** açık kapak hâlâ vakum. Sert ses kesmesi filmde yalnız burada: C11'in 4 s sakin sonrası 0,0'daki darbe. |

```
ORTAM  Vakum dışı: dış ses yok, kulak Sela'nın kaskında. Duyulan yalnız: kask içi (fan, nefes, tıslama) · gövdeden
       (eldiven-tutamak, valf, kemer/ip, varış darbesi) · telsiz (Bram'ın mikrofonu kendi kaskında; motor ve ortam
       gürültüsü yok, hışırtı ve tık telsizin kendisi). İç hacim ve ince atmosfer bu filmde yok (C12'nin açık
       kapağı dahil). Ortam yatağı (fan) film boyu kesintisiz; dijital sıfır yok.
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
```

## 2. KAYIT LİSTESİ

Ses aracı sahibindir; profil adları araçtan bağımsızdır. Hepsi `HUMAN`, hepsi kurguda yerleşir. Ağız kadrajda replik
olmadığı için `model` filtreli satır yok.

Profil adları: **BRAM_52_bariton** (diyalog_3 §4) · **SELA_29_alto** (diyalog_2 §4, değişmedi). Film boyu tek profil.

| No | Metin | Konuşan | Ses profili | Ton | Hedef süre | Filtre | Çekim · saniye |
|:--:|---|---|---|---|:--:|---|---|
| 1 | Lost my jets. | Bram | BRAM_52_bariton | kuru | 1,1 | telsiz | C01 · 3,0 |
| 2 | No, no— don't burn at me! | Bram | BRAM_52_bariton | telaşlı | 1,6 | telsiz (+hafif aşırı yük) | C02 · 2,5 |
| 3 | Cut it! You're climbing. You climb, you fall behind. | Bram | BRAM_52_bariton | kısık | 3,4 | telsiz | C03 · 1,0 |
| 4 | Copy. Down to two. | Sela | SELA_29_alto | düz | 1,4 | oda (kask içi: yakın, kuru, yankısız) | C03 · 6,4 |
| 5 | Turn your back on me— and brake. | Bram | BRAM_52_bariton | ağır | 2,3 | telsiz | C04 · 0,8 |
| 6 | Negative. I can see you. | Sela | SELA_29_alto | kesik | 1,6 | oda (kask içi) | C04 · 3,7 |
| 7 | At sunrise, I'm right in front of you. | Bram | BRAM_52_bariton | sakin | 2,8 | telsiz | C04 · 6,2 |
| 8 | At me— you're home. Away from me— you might reach me. Last one's for both. Your call. | Bram | BRAM_52_bariton | dürüst | 5,7 | telsiz | C05 · 0,3 |
| 9 | Sunrise. You be there. | Sela | SELA_29_alto | titrek | 1,8 | oda (kask içi) | C06 · 1,2 |
| 10 | Bram? | Sela | SELA_29_alto | çıplak | 0,6 | oda (kask içi; fısıltıya yakın) | C07 · 1,5 |
| 11 | I heard you. In the dark. | Bram | BRAM_52_bariton | alçak | 2,0 | telsiz | C10 · 4,0 |
| 12 | Good call. | Bram | BRAM_52_bariton | kuru | 0,8 | telsiz | C12 · 4,0 |

```
TELSİZ FİLTRE ZİNCİRİ  Bant geçiren yaklaşık 300-3400 Hz (alt kesim 12 dB/oktav, üst kesim 18 dB/oktav) · hafif doygunluk
                       (%2-3, gözle görülür kırpma yok) · mono, merkez · önünde ve arkasında 80 ms'lik squelch kuyruğu
                       olan yumuşak tık (tek tık, çift değil) · konuşma altında −28 dB taşıyıcı hışırtısı.
KASK İÇİ SELA          Filtresiz, mono, yakın mikrofon, yankı yok. Telsiz zincirine girmez, tıksızdır.
Tek bağırış            Yalnız 2. satır. Ses +2 dB'e kadar çıkar, limitere girmeden. Diğer satırların hiçbiri yükselmez.
3. satır               FILM §5 metni "Cut it!" yazıyor. F2 ses B1 "Cut it." önermişti, uygulanmadı. Kayıtta "kısık ve sert,
                       ses yükselmez" okutulur; böylece 2. satırın tek bağırış olma özelliği korunur. Metin düzeltmesi
                       Fable'ın (tek işaret).
3. satır kayıt          Tek take. Kurgu işaretleri: "Cut it" bitişi + 0,1 s = tıslama kesilir (nominal 1,6) · "climbing."
                       ile "You climb" arasında 0,4 s'lik ağır nefes boşluğu take'in içindedir (ayrı kayıt değil).
8. satır kayıt          Tek take. Dahili zamanlama (satır başına göre): At me 0,0 · you're home 0,8 · Away from me 1,6 ·
                       you might reach me 2,6 · Last one's for both 3,8 · Your call 5,1-5,7. Tirelerdeki iki duraklama
                       alınamayan nefes olarak kaydedilir (efekt değil). "might" net ama vurgusuz; önünde duraklama yok.
                       MİKS: telsiz zincirinden sonra "might" hecesine +2 dB (2-3 kHz bölgesi) verilir; "reach" kadar
                       duyulmalı.
10. satır              Fısıltıya yakın, soru tonuyla yükselmez; telsizin açık olduğunu bilen ama cevap beklemeyen biri.
```

### 2b. Sözsüz kayıtlar (replik değil; aynı oturum, aynı mikrofon)

Bram'ın C07 3,0, C10 3,6 ve C11 2,0'daki üç alımı **aynı oturumda ve aynı mikrofonla** kaydedilir (F2 ses KORU). Aynı
oturumda Sela'nın nefes seti de alınır, çünkü replikle aynı sesin nefesi olmalı.

| No | Ne | Kimin | Süre | Yer | Not |
|:--:|---|---|:--:|---|---|
| N1 | acılı tek nefes (göğüs yaralı, kısa) | Bram | 0,6 | C01 · 2,0 | repliğin altına binmez, önce biter |
| N2 | ağır nefes arası ("climbing." ile "You climb" arası) | Bram | 0,4 | C03 · ~3,0 | 3. satırın take'inde; ayrı dosya gerekmez |
| N3 | ağır nefes dizisi, tek başına | Bram | 1,7 | C03 · 4,4-6,1 | 2 nefes, C02'dekinden ağır |
| N4 | konuşmak için alım: kısa, yükselen soluk, ünlüye varmadan bırakılır | Bram | 0,5 | C07 · 3,0 · C11 · 2,0 | **aynı doku iki yerde**; 3 take alınır, iki yere birbirine en yakın ikisi gider |
| N5 | ağır nefes dizisi, sonu seyrelen (4 nefes: 2 tam, 1 yarım, 1 zayıf) | Bram | 5,0 | C07 · 4,9-9,4 | son iki nefes −6 ve −12 dB'ye iner, kesilmez |
| N6 | toparlanma soluğu: derin, takılan iç çekiş | Bram | 0,8 | C10 · 3,6 | C07'de yarım kalan alım bu kez tamamlanır |
| N7 | nefes-gülüş (burundan, kısa) | Bram | 0,5 | C11 · 5,3 | gülüş değil, "kabul" |
| N8 | sığ ve düzenli nefes (hat altında) | Bram | 9,0 | C12 · 1,0-10,0 | Sela'nınkinin altında; ritim film içinde yeni, düzen "yaşıyor" der |
| N9 | Sela nefes seti: sakin-gergin · hızlanan · hızlı düzensiz · çekilen/titrek · tutulup bırakılan · takılan alım · oturan | Sela | 7 tür | tüm çekimler (EFEKT LİSTESİ) | her tür 3-6 s'lik ayrı kayıt |

## 3. EFEKT LİSTESİ

Seviye: 0 dB = Bram telsiz replik ortalaması. Kaynak sütunu: gövde / hava / kask içi. **Hava kaynaklı satır yoktur**
(vakum). "Nereden": kütüphane arama terimi ya da tek satır İngilizce üretim promptu; N-no = §2b kaydı.

| Çekim | Saniye | Ses | Kaynak | Katman | Seviye | Nereden |
|:--:|---|---|---|:--:|---|---|
| C01 | 0,0-10,0 | kask içi fan uğultusu, sürekli yatak (tüm film bu varlığı kullanır) | kask içi | K1 | −26 | `a low steady fan hum inside a spacesuit helmet, close and dry, no rhythm, no echo, no voices, seamless loop` (140 s üret, 8 s çapraz geçişle döngüle) |
| C01 | 0,0-6,0 · 6,0 | istasyon yapısından eldivene gelen çok alçak mekanik titreşim; 6,0'da yumuşak duruş | gövde (eldiven-tutamak) | K2 | −24 | `very low machinery vibration felt through a metal handrail and glove, muffled, no air, six seconds then a soft stop` |
| C01 | 0,0-10,0 | Sela nefesi sakin-gergin; 8,5'ten hızlanan | kask içi | K2 | −14 → −11 | N9 |
| C01 | 1,7 · 2,0 · 4,3 | Bram: tık, acılı nefes, bitiş tıkı | kask içi (telsiz) | K3 | tık −10 · N1 −8 | `a single soft radio push-to-talk click with a short squelch tail, dry` · N1 |
| C02 | 0,0-10,0 | tıslama T1 (düşük itki, ince, uzun) + giysi titremesi aynı sesin alçak bileşeni | kask içi | K2 | −14 (Bram bağırırken −17) | `a thin steady low-pressure gas thruster hiss with a faint suit rattle, heard inside a helmet, close and dry, no echo, 12 seconds, no decay` |
| C02 | 0,0-10,0 | Sela nefesi hızlanan, sonra hızlı düzensiz | kask içi | K2 | −14 → −9 | N9 |
| C02 | 2,3 · 4,3 | Bram tık / bitiş tıkı (bağırış sırasında telsiz doygun) | kask içi (telsiz) | K3 | −10 | tık (C01 ile aynı varlık) |
| C03 | 0,0-1,6 · 1,6 | tıslama T1 sürer, 1,6'da **kuyruksuz kesilir**; kesilme anında valf kapanış sesi | kask içi + gövde | K2 | tıslama −14 · valf −18 | `a short muffled metallic valve clunk heard through a pressure suit, no air, close and dry` |
| C03 | 0,8 · 4,4-6,1 · 6,2 | Bram tık, ağır nefes dizisi (N3), bitiş tıkı (gap 2,0 s'in içi) | kask içi (telsiz) | K3 | N3 −9 · tık −10 | N3 · tık |
| C03 | 1,7-10,0 | Sela nefesi: 1,7'de açık ve hızlı, 4,4-6,3 arası −24'e **çekilir** (utanç boşluğu; tam sessizlik değil), 7,8'den titrek | kask içi | K2 | −12 → −24 → −13 | N9 |
| C04 | 0,6 · 3,3 · 6,0 · 9,2 | Bram tıkları (her iletimin başı/sonu) | kask içi (telsiz) | K3 | −10 | tık |
| C04 | 0,0-10,0 | Sela nefesi gergin, düzenli; "Negative" öncesi 3,5'te kısa sert alım | kask içi | K2 | −16 | N9 |
| C04 | 0,0-10,0 | (ışığın ve ufkun inişi: kulakta karşılığı yok, bilinçli) | — | — | — | — |
| C05 | 0,1 · 6,2 | Bram tık / bitiş tıkı | kask içi (telsiz) | K3 | −10 | tık |
| C05 | 0,3-6,0 | iki tirede alınamayan nefes (0,6-1,1 ve 2,5-2,9 arası, replik take'inin içinde) | kask içi (telsiz) | K3 | −9 | 8. satır take'i |
| C05 | 0,0-3,9 · 3,9-6,3 · 6,3 | Sela nefesi sakin-ağır → **son alım 3,9'da, sonra tutulur (tam sessiz)** → 6,3'te uzun bırakma (omuz dönüşünden 0,3 s sonra) | kask içi | K2 | −15 · 0 · −11 | N9 |
| C05 | 6,2-10,0 | **sessizlik olayı:** yalnız fan; 8,6'da tek yavaş nefes | kask içi | K1+K2 | fan −26 · nefes −18 | fan · N9 |
| C06 | 3,7-7,0 | tıslama T2: **sert tek itiş**, 0,15 s'lik atak, sonra 3,1 s düz; 0,4 s yumuşak kuyruk | kask içi | K2 | pik −6 · gövde −8 | `a short hard gas thruster burst with a fast attack and a steady hiss, heard inside a helmet, close and dry, no echo, three seconds` |
| C06 | 1,0 | Sela repliğinden önce kısa alım | kask içi | K2 | −15 | N9 |
| C06 | 8,8-10,0 | taşıyıcı hışırtı J-girişi (işitilir hâle 9,5'te, tıksız) | kask içi (telsiz) | K3 | −40 → −16 | `steady radio carrier static hiss through a band-pass radio filter, no voice, no music, seamless loop` |
| C07 | 0,0-10,0 | açık hat hışırtısı | kask içi (telsiz) | K3 | −16 | yukarıdaki hışırtı |
| C07 | 0,0-2,0 | Sela nefesi kısa-sığ; "Bram?" öncesi 1,0'da takılan alım | kask içi | K2 | −15 | N9 |
| C07 | 2,0-4,5 | eldivenin göğüs plakasından uzaklaşırken yumuşak sürtmesi | gövde (eldiven-giysi) | K2 | −24 | `soft stiff glove fabric sliding off a suit chest panel, muffled, inside the suit, close and dry` |
| C07 | 3,0 | Bram'ın konuşmak için alımı, kelimeye varmaz | kask içi (telsiz) | K3 | −8 | N4 |
| C07 | 4,5 | Sela'nın uzun bırakılan nefesi (el durduğu an; "harcanmadı") | kask içi | K2 | −11 | N9 |
| C07 | 4,9-9,4 | Bram'ın ağır nefesleri: 4,9 · 6,5 tam; 8,1 yarım (−4); 9,4 zayıf (−10) | kask içi (telsiz) | K3 | −10 → −20 | N5 |
| C08 | 0,0-1,0 | hışırtı −16'dan −27'ye süzülür (L-kesme), sonra sabit | kask içi (telsiz) | K3 | −27 | hışırtı |
| C08 | 1,8-10,0 | Sela'nın takılan alımı (Bram'ı fark ettiği an), 2,4-3,6 titrek çıkış, 6'dan sonra alçak ve düzenli | kask içi | K2 | −12 → −18 | N9 |
| C09 | 0,0-10,0 | hışırtı −27 | kask içi (telsiz) | K3 | −27 | hışırtı |
| C09 | 2,8-4,6 · 4,6 · 6,5-9,7 | Sela nefesi **tutulur** (Bram yaklaşırken) → ıskadan sonra bırakılır → atış hazırlığında hızlanır | kask içi | K2 | 0 / −12 / −13 → −10 | N9 |
| C09 | 9,75 | ip silkinmesi: tok, boğuk tek darbe; ardından 120 Hz dolayı ip titreşimi 1,5 s (C10'a taşar) | gövde (kemer-ip) | K2 | darbe −6 · titreşim −18 | `a single muffled taut-rope jerk through a harness, one low thump followed by a fading low hum, no air, close and dry` |
| C10 | 0,0-1,5 | ip titreşimi kuyruğu | gövde | K2 | −18 → −40 | (C09 9,75 varlığının uzantısı) |
| C10 | 0,0-3,5 · 3,5-4,0 | hışırtı −27; 3,5'te 0,5 s içinde −16'ya **yükselir** | kask içi (telsiz) | K3 | −27 → −16 | hışırtı |
| C10 | 2,0-4,5 | Bram'ın giysi hışırtısı, kolu kalkarken (kendi mikrofonundan telsize) | kask içi (telsiz) | K3 | −22 | `soft muffled suit fabric rustle picked up by a helmet microphone, close, no air` |
| C10 | 3,6 | toparlanma soluğu (Bram) | kask içi (telsiz) | K3 | −6 | N6 |
| C10 | 6,1 · 6,3-10,0 | bitiş tıkı: hat kapanır, **hışırtı da kesilir**; 6,3'te Sela'nın takılan nefesi, sonra titrek-yavaşlayan | kask içi | K3 · K2 | tık −10 · nefes −11 → −16 | tık · N9 |
| C11 | 1,8 · 2,0 | Bram tık; konuşmak için alım (C07 3,0 ile aynı doku) | kask içi (telsiz) | K3 | tık −10 · −8 | N4 |
| C11 | 2,3 · 2,5-4,5 | Sela'nın sert alımı; tıslama T3 (yumuşak, 0,3 s kuyruk) | kask içi | K2 | alım −12 · tıslama −12 | `a soft short gas thruster hiss with a gentle fade-out, heard inside a helmet, close and dry, no echo, two seconds` |
| C11 | 2,6 | ip yükünün yumuşak darbesi (ip ikinci gövdeyi çeker) | gövde (kemer-ip) | K2 | −20 | C09 silkinmesinin yarı seviyeli, kısa varyantı |
| C11 | 5,3 · 6,0 | nefes-gülüş; bitiş tıkı | kask içi (telsiz) | K3 | −10 · tık −10 | N7 · tık |
| C11 | 6,0-10,0 | Sela nefesi sakinleşir; yalnız fan ve nefes (4 s) | kask içi | K1+K2 | fan −26 · nefes −17 | fan · N9 |
| C12 | 0,0 | varış darbesi: eldivenin tutamağı kavraması, ilk karede; 0,6 s'lik alçak kuyruk | gövde (eldiven-tutamak) | K2 | −6 (filmin en yüksek efekti) | `a single muffled thud of a gloved hand gripping a metal handle, transmitted through a pressure suit, no air, close and dry` |
| C12 | 0,0-8,0 · 8,0-10,0 | Sela'nın titrek nefesi; 8,0'dan oturan | kask içi | K2 | −13 → −16 | N9 |
| C12 | 1,0 · 1,0-10,0 | Bram tık; açık hat hışırtısı (C07 dokusu) ve sığ-düzenli nefes; **bitiş tıkı yok** | kask içi (telsiz) | K3 | tık −10 · hışırtı −18 · nefes −17 | tık · hışırtı · N8 |
| C12 | 9,85-10,0 | son 150 ms'de hepsi −40'a iner (tıkırtı koruması); film sonu | — | — | — | — |

## 4. ORTAM YATAĞI (sahne başına tek satır)

Yatak = K1 fan; hat durumu ayrı satır olarak hışırtıdır (K3). Fan film boyu tek varlıktır; sahne arası fark seviyede değil, kulağın
neyi duyduğundadır.

| Sahne | Ne · seviye · nereden |
|:--:|---|
| S1 | kask içi fan, sürekli, ritimsiz (`low steady fan hum inside a spacesuit helmet, no rhythm`) · −26 · fan varlığı (140 s) |
| S2 | aynı fan, aynı seviye; üstüne tıslama biner · −26 · aynı |
| S3 | aynı fan; 1,6'da tıslama kesilince fan ilk kez çıplak duyulur · −26 · aynı |
| S4 | aynı fan; zaman atlaması sesle işaretlenmez · −26 · aynı |
| S5 | aynı fan; 6,2-10,0 arası tek yatak, 3,8 s · −26 · aynı |
| S6 | aynı fan; 7,0-8,8 arası yalnız yatak · −26 · aynı |
| S7 | aynı fan + açık hat hışırtısı (hat durumu K3) · fan −26 · hışırtı −16 · aynı |
| S8 | aynı fan + alçak hışırtı · −26 / −27 · aynı |
| S9 | aynı fan + alçak hışırtı · −26 / −27 · aynı |
| S10 | aynı fan; 6,1'de hışırtı kesilince yalnız fan kalır · −26 · aynı |
| S11 | aynı fan; 6,0-10,0 arası yalnız yatak ve nefes · −26 · aynı |
| S12 | aynı fan (iç hacim uğultusu **yok**) + açık hat hışırtısı · fan −26 · hışırtı −18 · aynı |

```
Fan varlığı  100-600 Hz'de geniş bant, ritim ve ton sürünmesi yok (hışırtı 1-3 kHz'dedir, bantlar ayrı kalır).
             Stereo: iki kanal ilintisiz gürültü, orta-alçak; mono toplamda en çok −2 dB kayıp. Telsiz ve kask içi replik: mono, merkez.
```

## 5. TIK DİLİ VE TIŞLAMA TABLOSU (F2 ses B3, B4 ve not 2)

| Çekim | Başlangıç tıkı | Bitiş tıkı | Anlam |
|:--:|:--:|:--:|---|
| C01 | 1,7 | 4,3 | tek iletim |
| C02 | 2,3 | 4,3 | tek iletim (bağırış) |
| C03 | 0,8 | 6,2 | Bram tuşu 6,2'de bırakır; Sela'nın cevabı kaskından duyulur |
| C04 | 0,6 · 6,0 | 3,3 · 9,2 | iki ayrı iletim; Sela tıksız |
| C05 | 0,1 | 6,2 | tek iletim; sonrası 3,8 s sessizlik |
| C06 | — | — | hat kapalı |
| C07 | **yok** | — | hat açık kaldı, tuşa basılmadı |
| C08-C09 | — | — | açık hat, alçak |
| C10 | **yok** | 6,1 | açık hat boyunca Bram ilk kez kapatıyor |
| C11 | 1,8 | 6,0 | tuşa yeniden basıyor |
| C12 | 1,0 | **yok** | hat açık kalır |

| Ateşleme | Yer | Süre | Işık | Karakter | Seviye | Bitiş |
|---|---|:--:|:--:|---|---|---|
| T1 | C02 0,0 → C03 1,6 | 11,6 s | 2 (4→2) | düşük itki, ince, uzun | −14 | **kuyruksuz kesilir** + valf tok (emire uyma) |
| T2 | C06 3,7-7,0 | 3,3 s | 1 (2→1) | sert tek itiş, yüksek basınç | pik −6, gövde −8 | 0,4 s yumuşak kuyruk |
| T3 | C11 2,5-4,5 | 2,0 s | 1 (1→0) | yumuşak, ip yükü altında | −12 | 0,3 s kuyruk |

Kulak süre oranını (11,6 : 3,3 : 2,0) 2 : 1 : 1 olarak okumaz diye bakıldı; farkı **itki sertliği** taşır: uzun ince tıslama
bir gaz yavaşça gider, kısa sert itiş bir ışık tek vuruşta gider. Alternatif (T2/T3'ü orantılı 5,8 s'ye uzatmak) C06 7,0'da biten ışık küçülmesini ve C11'in diyalog
zamanlamasını (nefes-gülüş 5,3) bozar; yapılmadı.

## 6. DİYALOG GECİKMELERİNİN DOĞRULANMASI (kesme gecikmeyi yemez)

| Alışveriş | Gecikme (diyalog) | Bu planda | Durum |
|---|:--:|---|:--:|
| A3b | 2,0 s | Bram 4,4 → Sela 6,4 (araya yalnız N3 ve tık 6,2) | ✅ |
| A4a | 0,6 s | 3,1 → 3,7 (tık 3,3 içeride) | ✅ |
| A4b | 0,9 s | 5,3 → 6,2 | ✅ |
| A4c | 1,3 s | 9,0 → C05 0,3 (tıklar 9,2 ve 0,1) | ✅ |
| A5 | 5,2 s | C05 6,0 → C06 1,2 (J-kesme yok) | ✅ |
| A6 | 0,7 s | 3,0 → 3,7 | ✅ |
| A7 | 0,9 s | 2,1 → 3,0 (Bram'ın alımı) | ✅ |
| A8 | 0,3 s | Bram 6,0 → Sela'nın nefesi 6,3 | ✅ |
| A9a | 0,5 s | Bram alımı 2,0 → T3 2,5 | ✅ |
| A9b | 0,8 s | T3 bitişi 4,5 → nefes-gülüş 5,3 | ✅ |
| A9c | 3,2 s | C12 4,8 → Sela'nın oturan nefesi 8,0 | ✅ |

## 7. MÜZİK İÇİN SES KISITLARI (K4; besteci planı paralel yazılıyor)

```
Replik yokken müzik yatağı −16…−18 LUFS; replik altında −6…−9 dB (kural 6).
MÜZİKSİZ (sesin kendisi anlam taşıyor):  C05 tamamı (replik 8 + 3,8 s sessizlik) · C07 tamamı · C08 tamamı · C09 tamamı ·
                                          C10 0,0-6,3 (hışırtı, ayılma nefesi ve söz, bitiş tıkı).
MÜZİK ALANI:                              C01-C04 · C06 (tıslama 3,7-7,0 sırasında yatak) · C10 6,3'ten C12 sonuna.
Gerekçe: F2 diyalog önerisi (C05 sessizliği, C07 hışırtısı, C08-C09 sessiz hat) ve SAHNELEME H01 kuyrukları:
         7-10 s'lik süren hareket kuyruklarını sesin kendisi taşıyor (C05 sessizlik, C07 hışırtı, C10 nefes ve söz, C12 nefes).
         Doğuş (C08) müziksizdir; bu ödülü bilerek sese bırakır. Besteci başka bir şey önerirse Fable karar verir.
```

## 8. FİNAL MİKS — YÜKSEKLİK HEDEFİ

```
HEDEF       −14 LUFS integrated · ≤ −1 dBTP · stereo 48 kHz · mono uyumluluğu kontrol edilir.
YÖNTEM      1) taslağı kur (sessiz klipler + bu plandaki sesler + müzik)
            2) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4>           (ölç)
            3) python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4> --uygula -o final.mp4
            İki aşamalı, doğrusal: sıkıştırma yok.
ZİRVELER    Bram'ın C02 bağırışı (+2 dB), C06 tıslama atağı, C09 silkinmesi ve C12 varış darbesi filmin en yüksek
            anlarıdır; −1 dBTP tavanı bunlarda belirlenir.
DİKKAT      Konuşma 25 s, film 120 s ve çoğu bölüm çıplak (fan + nefes). Integrated ölçüm sessiz bölümleri kapıdan (gating)
            atar; sayı bu yüzden konuşmanın ve tıslamanın seviyesini ölçer. Bu doğrusal düzeltmede sessizliği yukarı çekmez.
            Düşük teslim en ölümcül hata: ölçüm −15'in altında çıkarsa konuşma seviyesi yükseltilir, sıkıştırma eklenmez.
KORUNAN     C05 6,2-10,0'daki yatak ile C12 0,0'daki varış darbesi arasındaki fark (≥ 30 dB kısa dönem) ezilmez.
MONO        Fan ve hışırtı mono toplamda en çok −2 dB kaybeder; telsiz ve kask içi replik zaten mono.
SON KONTROL Final baştan sona kulaklıkla ve telefon hoparlöründe dinlenir. Telefonda fan duyulmuyorsa (−26'da düşük frekans
            kaybolur) fan +3 dB'ye alınır; C05 sessizliği "sıfır" gibi duyulmamalıdır.
```

## 9. DİNLEME ÖLÇÜLERİ (F8 animatik; F3_animatik_3 listesi)

Bu iki madde F3'te metinle çözülemedi, sese bırakıldı. F8'de ses dahil animatikte şu sorular sorulur.

1. **Baygın / ayıldı (C07 → C10):** İzleyici C07 sonunda Bram'ın nefesinin *gittiğini* (sustu demeden) duyuyor mu? C10'da hışırtı yükselince
   ve toparlanma soluğuyla "ayıldı, cevap veriyor" okunuyor mu? Okunmazsa: N5'in son iki nefesi daha belirgin yapılır, N6 +3 dB.
2. **C07 vazgeçiş:** El kumandadan uzaklaşırken tıslamanın *olmaması* ve 4,5'teki bırakılan nefes "yakmadı, bıraktı" diye okunuyor mu?
   Okunmazsa: 4,5 nefesi +3 dB ve 4,5 sonrası bir saniye Bram'ın nefesinden önce boş bırakılır.
3. **C05 sessizliği (3,8 s):** Boşluk olarak değil karar olarak okunuyor mu? Okunmazsa: fan seviyesi korunur, tutulan nefes uzatılmaz.
4. **C09 → C10 silkinmesi:** Kesmeden önce gelen 9,75 darbesi atışın sonucu olarak okunuyor mu? Hızlı geçerse 0,25 s yerine 0,35 s J-kesme denenir.

## 10. FABLE'A AÇIK KARARLAR

1. **"Cut it!" noktalaması (FILM §5, satır 3):** ses F2 B1 uygulanmadı. Öneri: "Cut it." Yapılmazsa kayıt notu telafi eder (§2).
2. **Tıslama oranı (§5):** süreler ışık sayısıyla orantılı değil. Karakter farkıyla çözüldü; F8'de kulak yine "2 ışık / 1 ışık / 1 ışık" okumuyorsa
   T2 ve T3'e basınç farkı yerine süre eklenmez, C03 gösterge insert'i (görüntü) güçlendirilir.
3. **Tıksız açılış (C06 sonu → C07):** C05 6,2 tıkı hattı kapattı; C07 hışırtısı tıksız girer. İzleyici bunu "hat bir şekilde açıldı" diye duyar;
   bu yabancılık bilerek. Diyalog yazarı bunun "tuşa basılmadı" okumasıyla uyumlu olduğunu doğrulamalı.
4. **C01 radyatör kolu titreşimi:** eldiven-tutamaktan gelen gövde sesi. Sahne "dış ses" gibi okunursa bu satır kaldırılır (görüntü bilgisi taşınır, kayıp yok).
5. **Müzik penceresi (§7):** besteci tur 1 çıktısı bu kısıtlarla çakışırsa kurgucu ve Fable karar verir.

```
ÖZET     12/12 çekimde en az bir efekt satırı · 12 replik kayıt satırı + 9 sözsüz kayıt grubu · katman ≤4 her sahnede
         model sesi: yok · hava kaynaklı efekt: yok · vakumda dış ses: yok
GİRDİ    yatay_2_dk_filmler/THE_WRONG_BURN/FILM.md §1-§5
         yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F2_ses-tasarimcisi_2.md (B1-B4, KORU, F4'e aktarılacak notlar)
         yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F2_diyalog-yazari_3.md (§2 SES İPİ, §4 profiller) · F2_diyalog-yazari_2.md (§4 Sela)
         yatay_2_dk_filmler/THE_WRONG_BURN/ODA/F3_animatik_3.md (ölçüm listesi)
         yatay_2_dk_filmler/THE_WRONG_BURN/SAHNELEME.md §5 (H01 kuyrukları)
         uretim_hatti/BILINEN_TUZAKLAR.md §B · uretim_hatti/FLOW_GERCEKLERI.md §4 · §6
YAPILMADI  müzik planı (besteci paralel; §7 yalnız ses kısıtı) · kulakla dinleme ve gerçek take süresi ölçümü
           (zamanlamalar diyalog tablosu ve çekim listesi saniyelerinden kuruldu) · kurgu.py yukseklik koşulmadı (taslak yok)
```
