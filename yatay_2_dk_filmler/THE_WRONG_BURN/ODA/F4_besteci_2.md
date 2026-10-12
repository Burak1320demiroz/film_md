# F4 · besteci · tur 2 (birleştirme geçişi) — THE_WRONG_BURN

```
GİRDİ      FILM.md §1-§5 · ODA/F4_besteci_1.md (önceki eser) · ODA/F4_ses-tasarimcisi_1.md (§7 müzik kısıtları dahil)
           ODA/F4_kurgucu_1.md (B1-B6) · ODA/F4_diyalog-yazari_1.md (B1-B10; müzik planına düşenler B1, B5, B6) ·
           Fable kararı (F4_diyalog-yazari_1.md sonu, madde 1, 2, 6)
           kilavuzlar_ve_sistem_dosyalari/GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md §10 · §14 · §15.1a · §16 · §17
KESMELER   12 × 10 s → 10,0 · 20,0 · … · 110,0 (mutlak). `kurgu.py liste --kesmeler` bu turda koşulmadı (taslak yok);
           faz 8'de gerçek çıktıyla kesinleşir. Tüm saniyeler MUTLAK: Cn içi saniye + (n−1) × 10.
DURUM      PLAN, son hâl. Saniyeler ±0,5 s; "bağ" sütunundaki ses olaylarına bağlı kenarlar kayıt süreleri
           ölçülünce kayar (kural: müzik kenarı mutlak saniyeye değil, ses olayına bağlıdır, §5).
DEĞİŞEN    (1) C07-C08 müziksiz: L1 yalnız 54,8-60,0; 80,0 SUSMA satırı düştü, susma 60,0-96,8 oldu
           (2) bitiş: müzik 113,0'da kesilir (eski 117,0); çözülme 111,8'e geldi; "Good call." ve 118,0 nefesi müziksiz
           (3) L1 telefonda taşıyıcıya kavuştu (165 + 220 Hz); 110 Hz "telefonda duyulur" cümlesi silindi
           (4) kenarlar ses olayına bağlandı; 4,2 → 4,5; replik 6 çevresi yeniden ayarlandı
           (5) yoğunluk tepesi 3 → 2; "(↗3)" silindi; C11'de müzik alışveriş altında −6/−8
           (6) Fable kararı 3 (denetci F4.3): 106,3-111,2 arası L3 yok, L1 −18 dB; L3 çözülme için 111,2'de yeniden girer
```

---

## 1. BULGULARA CEVAP

Her bulgu için KABUL / KISMEN / RED. KISMEN ve RED gerekçeli.

### Kurgucu (F4_kurgucu_1.md)

| Bulgu | Cevap | Ne yapıldı / gerekçe |
|:--:|:--:|---|
| B1 · L1 telefonda duyulmaz | **KABUL** | Kılavuz §15.1a "150 Hz altı tamamen kayıp" varsayımı hat gerçeği; ölçüm itirazı yok. L1'in telefonda taşıyıcısı 150 Hz üstünde olur: çello A2 (110 Hz) gövde, **Mi3 165 + La3 220 Hz taşıyıcı seviyede** (missing fundamental: 110-165-220 yığını beyne 55 Hz'i kurar), kontrbas A1 55 Hz yalnız kulaklık/TV derinliği ve kısık. "Telefonda 110 Hz duyulur" cümlesi silindi. L1 ağırlığı 150-400 Hz; hışırtı bandına (1-3 kHz) girmez. Kural 5 → KISMEN (gerçek telefon eşiği ölçülmedi, kılavuz da söylüyor; faz 8'de telefon testi, §9 madde 8). |
| B2 · C07-C08 çakışma + C11 6-10 s | **KABUL** | Fable kararı 1 ile aynı yol: L1 54,8'de girer, 60,0'da yay kalkar, 60,0-96,8 müziksiz, dönüş 96,8. 80,0 SUSMA satırı düştü. C11 6,0-10,0: ses §3 "yalnız fan ve nefes (4 s)" ile §7 "müzik alanı" kendi içinde çelişiyordu; ses §3'ü esas aldım ve **genişlettim**: yalnız L3 değil, L1+L3 birlikte 106,3'te −12 dB'ye iner (kesilmez, bitiş tıkı 106,0 + 0,3), 110,0 varış darbesi bu çıplaklıkta gelir; 111,2'de seviye geri döner. Ses_2 "tam sessiz" isterse yedek: −18 dB (§9 madde 4). **[Bu satırın 106,3-111,2 değeri Fable kararı 3 ile değişti, aşağıya bak.]** |
| B3 · 35,4 susması duyulmayabilir | **KISMEN** | KABUL: (a) kenar mutlak saniyeye değil ses olayına bağlanır: 35,4 = "replik 6 sonu + 0,1 s", 4,5 = "replik 1 bitiş tıkı (4,3) + 0,2 s" (eski 4,2'den kaydı), 14,6 = "replik 2 bitiş tıkı (14,3) + 0,3 s"; "hiçbir replik müziğin kenarına rastlamıyor" iddiası artık bağ kuralıyla garanti (§5). (b) L2'nin replik 6 altındaki duck'ı −8'den **−6 dB'ye** açıldı. RED: −3 dB. Gerekçe: kural 7 tabanı −6 dB; Sela'nın kask içi altosunun (200 Hz temel, 1-3 kHz formant) keman bandıyla çakışması "I can see you"nun anlaşılırlığını riske atar. RED: "sessizlik için fiilen 0,9 s" çerçevesi. Susmanın fark edildiği yer 35,4'ün kendisi değil: 39,2-40,1 (tık araları, fan ve nefes) ve 46,0-50,0 (3,8-4,0 s çıplak). Susma, takasın başlamasından 4,9 s, gözlerin kapanmasından (45,6) 10,2 s önce. |
| B4 · "zafer değil" ↔ tek çözülme + tepe | **KISMEN** | Kurgucunun ikinci yolu uygulandı, birincisi (yedeği varsayılan yapmak) F8 testine bırakıldı (Fable kararı 2). KABUL: yoğunluk tepesi 3 → **2**; çözülme film-içi en yüksek nokta olmaktan çıktı (göz çizgisi 14,6-35,4 ile eşit); Do♯ ve L3 çözülmede −4 dB (L1 −2); çözülme 1,2 s sürer ve kesilir (111,8-113,0). KABUL: çözülme, varış darbesine (110,0) değil ışığın yayılmasına bağlı olduğundan 111,8'dedir; darbe 1,8 s yalnız kalır. RED: OKUMA'dan "zafer olarak değil"i çıkarmak. Gerekçe: 1,2 s'lik, orta-yoğunluklu, yay kalkışıyla kesilen bir akor zafer için gereken süreyi ve yoğunluğu taşımaz; "Good call." müziksiz gelir, onay bandında müzik yok. Zafer okunursa karar F8 testindedir: çözülmesiz sürüm B hazır (§9 madde 7). |
| B5 · L2 yükselir, C04 ışığı iner | **KABUL** | L2 yükselişi 14,6-30,0 ile sınırlı; 30,0'da (C03/C04 kesmesi) durur ve 35,4'e kadar tek perdede askıda kalır. "Çok yavaş inen" seçeneği alınmadı: iniş görüntüyü taklit eder (mickey-mousing sınırı). |
| B6 · "(↗3)" tutarsızlığı | **KABUL** | Silindi. Tabloda yoğunluk en çok 2; üç katman hiçbir an aynı anda yok. |

### Diyalog yazarı (F4_diyalog-yazari_1.md)

| Bulgu | Cevap | Ne yapıldı / gerekçe |
|:--:|:--:|---|
| B1 · C07-C08 müzik | **KABUL** | Kurgucu B2 ve Fable kararı 1 ile aynı. 60,0-96,8 müziksiz; "Bram?" (61,5-62,1) ve seyrelen nefes çıplak. |
| B5 · "Good call." zirvenin altında; kesme cevabın yerinde | **KABUL** (113,2 → 113,0) | Çözülme kalır, kesme 117,0'dan öne alındı. Önerilen 113,2 yerine **113,0**: kural 2'nin alt sınırı (susma ile olay arası ≥ 1,0 s), "Good call." başlangıcı (114,0) − 1,0 s. Çözülme buna göre 111,8'e geldi (süresi 1,2 s korunur). "Good call." (114,0-114,8) ve Sela'nın cevap nefesi (118,0) sessizlikte; Fable'ın tek sınırı karşılandı. |
| B6 · C11 iki alım + L3 | **KABUL** | L3 100,0'da −8 dB'de girer ve 106,3'e kadar −8'de kalır (replik altı kuralı sözsüz alışverişe, N4 ve N7'ye de uygulandı); L1 aynı aralıkta −6. Sela'nın alımının 101,5'e çekilmesi (ses) müzik planını etkilemez: bu bölgedeki ilk müzik kenarı 100,0 (L3 girişi), sonraki 106,3. |
| B2 (tık) · B3 · B4 · B7-B10 | **KAPSAM DIŞI** (ses-tasarımcısı) | Müziğe etkisi: B2 — tık 58,8'e konursa L1'in son 1,2 s'ine biner; bant ayrı (L1 150-400 Hz, tık/hışırtı 300 Hz üstü), 60,0 yay kalkışı değişmez; hışırtı işitilir hâle geldikten (59,5) 0,5 s sonra L1 çekilir, ses kimliği tondan hışırtıya geçer. B3 (Sela nefesi 47,0) ve B4 ("Bram?" altı hışırtı) 35,4-54,8 ve 60,0-96,8 müziksiz aralıklarında; etki yok. B7-B10 etkisiz. |

### Fable kararı 3 (denetci F4.3)

Denetçi: 106,0-110,0 (C11 6-10 s) için eserde üç değer vardı (ses_2 §6 S11 "L3 yok" · bu dosyanın §2 bloğu "L1+L3 −12 dB" · §9 madde 4 "−18 yedek"). Karar: C11 bitiş tıkı (106,0) + 0,3 → **L3 kesilir**, **L1 sürer, −18 dB** (L1 pedalı kesilip yeniden girmez); 106,3-111,2 arası L3 yok ve L1 −18; 111,2-111,8'de L1 seviyesi geri döner ve L3 çözülme için yeniden girer (Mi + Si, swell 0,6 s; 111,8'de Si → Do♯).

| Değişen satır | Eski | Yeni |
|---|---|---|
| §2 VURUŞ/SUSMA, 106,3 satırı | ≈106,3 L1+L3 −12 dB'ye iner, kesilmez | ≈106,3 L3 kesilir (10-30 ms rampa), L1 −18 dB'ye iner, kesilmez |
| §2 VURUŞ/SUSMA, 111,2-111,8 satırı | seviye geri döner | L1 seviyesi geri döner, L3 yeniden girer (Mi+Si, swell 0,6 s) |
| §2 VURUŞ/SUSMA, yedek (B) | 111,8'de Si sürer | 111,8'de L3 Mi+Si ile kalır (Do♯'ya çıkmaz) |
| §3 seviye tablosu | 106,3-111,2: L1 −12 · L3 −12; 111,2-111,8: L3 −12 → −4 | 106,3-111,2: L1 −18 · L3 yok; 111,2-111,8: L1 −18 → −2 · L3 girer, → −4 |
| §4 dinamik tablo | satır 9: L1+L3 −12; satır 10: kabarma; "110,0 → müzik −12 dB'de" | satır 9: L3 yok, L1 −18; satır 10: L3 yeniden girer; "110,0 → müzik −18 dB'de (yalnız L1)" |
| §9 madde 4 (a) | −12 esas, −18 yedek | −18 esas (L3 yok); yedek maddesi kalktı |

Bu karar yukarıdaki B2 satırının ve aşağıdaki §5 bağ tablosunun "−12 dB'ye iniş (106,3)" ile "kabarma başlar (111,2)" satırlarının, ayrıca §8 ve ÖZET'teki ilgili ifadelerin 106,3-111,2 değerini geçersiz kılar; o satırlar, talimat gereği, bu turda metin olarak değiştirilmedi.

---

## 2. FILM.md §7'ye YERLEŞTİRİLECEK BLOK

```
OKUMA        İzleyici bu filmi, gözün gösterdiği yola değil sesin tarif ettiği yola tutunmayı —
             titrek bir güveni — olarak okumalı. Tehdit, yas ya da zafer olarak değil.
             Müzik güveni ilan etmez: ilk 35 s gözün yalanına eşlik eder, doruk ve belirsizlik boyunca
             susar, güven verildikten sonra tek bir notayla yanına döner; evde yalnızca 1,2 s'lik bir
             açıklık verir ve keser. Onayı ("Good call.") müzik değil insan verir.
MÜZİKSİZ     (1) ANA — 35,4–54,8 s (C04 sonu · C05 · C06'nın ilk 4,8 s): Bram'ın sözü, takas ("might",
             "Your call"), gözlerin kapanması, dönüş, "You be there" ve ateşleme. Karar yalnız sesle
             ve bedenle verilir. Susma takasın başlamasından 4,9 s önce başlar. Dönüş: ateşlemeden
             1,1 s sonra TEK NOTA.
             (2) 60,0–96,8 s (C07 · C08 · C09 · C10'un ilk 6,8 s): filmin açık sorusu "Bram yaşıyor mu?"
             (vazgeçiş, hışırtı, gün doğumu, ıska, ip atışı, ayılma). Cevabı müzik vermez; dönüş Bram'ın
             "I heard you. In the dark." ve Sela'nın takılan nefesinden SONRA, aynı tek nota.
             (3) 113,0–120,0 s: "Good call." ve Sela'nın oturan nefesi müziksiz; film müzik kesmesiyle
             değil, nefesle biter.
             Açılış 0–4,5 s de müziksiz (fan, nefes, "Lost my jets.").
VURUŞ/SUSMA  Kenarlar ses olayına bağlıdır, saniyeler yaklaşık:
             ≈4,5 L1 girer (replik 1 bitiş tıkı 4,3 + 0,2) · ≈14,6 L2 girer (replik 2 bitiş tıkı 14,3 + 0,3) ·
             14,6–30,0 L2 çok yavaş yükselir, 30,0'da (C03/C04 kesmesi) durur, 35,4'e kadar askıda ·
             ≈35,4 SUSMA, L1+L2 birlikte (replik 6 sonu 35,3 + 0,1) ·
             ≈54,8 TEK NOTA, L1 (ateşleme 53,7 + 1,1) · 60,0 L1 yay kalkar (C06/C07 kesmesi) ·
             ≈96,8 TEK NOTA, L1, aynı nota (Sela'nın takılan nefesi 96,3 + 0,5) ·
             100,0 L3 girer, −8 dB (C10/C11 kesmesi) · ≈106,3 L3 kesilir (C11 bitiş tıkı 106,0 + 0,3), L1 −18 dB'ye iner, kesilmez ·
             106,3–111,2 L3 yok, L1 −18 dB (varış darbesi 110,0 çıplakta) ·
             111,2–111,8 L1 seviyesi geri döner, L3 yeniden girer (Mi+Si, swell 0,6 s) · ≈111,8 TEK ÇÖZÜLME (L3: Si → Do♯, La majör) ·
             ≈113,0 KESME, yay kalkar, kuyruk yok ("Good call." başı 114,0 − 1,0 s) · 113,0–120,0 müziksiz.
             Çözülmesiz yedek (B): 111,8'de L3 Mi+Si ile kalır, Do♯'ya çıkmaz; 113,0'da aynı kesme. Seçim faz 8 izleyici testinde.
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md
```

---

## 3. KÜNYE (kılavuz §17) — faz 8'in girdisi

```
FİLM                  THE_WRONG_BURN · 2:00 · 12 × 10 s
NOVUM OKUMASI         bkz. OKUMA (yukarıda). Önce bu yazıldı.
MÜZİK-GÖRÜNTÜ İLİŞKİSİ 0–35,4 s: empatik, ama göze (ışık büyür, müzik de "yaklaşır"; yalan bunun içinde).
                      35,4–54,8 ve 60,0–96,8: yokluk. 54,8-60,0 ve 96,8 sonrası: anempatik-sıcak
                      (kimse söylemeden yapılan işi kutlamaz; C11'de Sela'nın ateşlemesine vuruş yok).
TEMPO                 ≈60 BPM, SERBEST. Nabız ve vuruş duyulmaz; sürekli (sustained) dokular.
                      60 seçildi çünkü 1 vuruş = 1 s: plan saniyeleri doğrudan vuruşa çevrilir.
                      Kılavuz §14'ün 72 BPM ızgarası (10 s = 3 ölçü) alınmadı: besteci kuralı 4
                      vuruşları ızgaraya değil olaya oturtur; müzik kenarları kesmelere değil ses olaylarına bağlı.
TONALİTE              La (A) pedalı. Çözülme: 1 (≈111,8, La majör). Başka hiçbir yerde kadans yok;
                      üçlü (Do/Do♯) 111,8'e kadar hiçbir katmanda çalınmaz.
SESSİZLİK             35,4–54,8 (19,4 s, ana, doruk) · 60,0–96,8 (36,8 s) · 113,0–120,0 (7,0 s) · açılış 0–4,5.
                      Toplam müziksiz 67,7 s (%56,4); müzikli 52,3 s (%43,6) = 30,9 + 5,2 + 16,2.
ÇÖZÜLMEYEN CÜMLE      L2 (göz çizgisi): 14,6'da Mi civarında başlar, çok yavaş Fa♯ → Sol♯'e (La'nın duyarlı
                      sesine) yükselir, 30,0'da Sol♯'te durur, 35,4'te La'ya varmadan kesilir,
                      FİLMDE BİR DAHA GELMEZ. Söz verilir, tutulmaz; Sela ışığa sırtını döner.
                      (Niyet; Flow Music'e nota adı olarak verilmez.)
KAPANIŞ               fade-out YOK. 111,8'de çözülen akor 113,0'da yay kalkarak kesilir (kuyruk yok).
                      Film müzik kesmesinden 7,0 s sonra nefesle biter.
FREKANS TABANI        L1 (pedal): çello A2 110 Hz gövde + Mi3 165 Hz + La3 220 Hz taşıyıcı seviyede
                      (110-165-220 yığını 55 Hz'i beyne kurar; telefon 150 Hz altını üretmiyor varsayımı);
                      kontrbas A1 55 Hz yalnız derinlik, taşıyıcıdan ≥ 6 dB kısık. L1'de 600 Hz üstü yok:
                      üst bant sese ve hışırtıya kalır. 38-46 Hz alanı ve infrases yok (kural 5).
KATMANLAR             L1 pedal (çello + kontrbas, sul tasto, yuvarlak) · L2 göz çizgisi (tek yüksek keman,
                      6 kHz altı) · L3 üst dolgu (viyola: Mi3 165 + Si3 247 Hz; çözülmede Si → Do♯4 277 Hz).
                      Aynı anda en çok 2 katman; hiçbir an 3 değil.
LUFS HEDEFİ           nihai −14 LUFS / −1 dBTP · müzik yatağı −16…−18 (aşağıdaki seviyeler "yatak"a göre dB) ·
                      replik/alışveriş altı −6…−9 · çözülme anı kısa süreli −16'yı aşmaz
REVERB                kuru (vakum). Hiçbir katmanda yankı, kuyruk, hava yok.
MONO                  tüm alt uç ve taşıyıcılar merkezde; mono fold-down'da düşme olmamalı.
```

### Seviye otomasyonu (yatak = 0 dB)

| Aralık | L1 | L2 | L3 | Not |
|---|:--:|:--:|:--:|---|
| 4,5–35,4, replik dışı | 0 | 0 (14,6'dan) | — | L1 girişi swell 0,6-0,8 s, L2 girişi swell 0,8 s (fade-in serbest; yasak olan fade-out) |
| replik 2 (12,5-14,1) | −8 | — | — | atak 80 ms (kelimeden önce), bırakma 250 ms |
| replik 3 (21,0-24,4) · 4 (26,4-27,8) · 5 (30,8-33,1) | −8 | −8 | — | |
| 24,4–26,4 (Bram'ın ağır nefesi, "utanç boşluğu") | −11 | −11 | — | ek −3 |
| replik 6 (33,7-35,3) | −8 | **−6** | — | duck açıldı (kurgucu B3) |
| 35,4 | kes | kes | — | 10-30 ms rampa, kuyruk yok |
| 54,8–60,0 | 0 | — | — | swell 0,6 s; 60,0'da 10-30 ms rampa ile kalkar |
| 96,8–100,0 | 0 | — | — | aynı nota, swell 0,6 s |
| 100,0–106,3 | −6 | — | −8 | L3 girişi swell 0,8 s |
| 106,3–111,2 | **−18** | — (**L3 yok**) | **kes** | L3 106,3'te 10-30 ms rampa ile kesilir; L1 0,5 s'de −18'e iner, kesilmez; 110,0 darbesine tepki yok (Fable kararı 3) |
| 111,2–111,8 | −18 → −2 | — | giriş → −4 | 0,6 s kabarma (ışığın yayılması; darbeye değil); L3 Mi+Si ile yeniden girer, swell 0,6 s |
| 111,8–113,0 | −2 | — | −4 | Si → Do♯; çözülme anı |
| 113,0 | kes | — | kes | 10-30 ms rampa, kuyruk yok |

---

## 4. DİNAMİK TABLO

Yoğunluk 0–5 (0 = müzik yok). Film içinde en yüksek yoğunluk **2**'dir ve iki yerde görülür: göz çizgisi (yalan) ve çözülme (1,2 s).

| # | Bölüm | Çekim | Yaklaşık saniye | Yoğ. | Ne giriyor / çıkıyor | Altında / üstünde ne var |
|:--:|---|:--:|---|:--:|---|---|
| 1 | Açılış | C01 | 0,0–4,5 | 0 | hiçbir şey | fan, Bram'ın acılı nefesi (2,0), replik 1 (3,0-4,1), bitiş tıkı 4,3 |
| 2 | SES İPİ | C01–C02 | 4,5–14,6 | 1 | **L1 girer** 4,5 (La pedalı, çello+kontrbas, kuru) | ateşleme tıslaması, replik 2 (12,5-14,1) −8 dB |
| 3 | GÖZ | C02–C04 | 14,6–35,4 | 2 | **L2 girer** 14,6: tek yüksek keman, çok yavaş yükselir (14,6-30,0), 30,0'da durur ve askıda kalır; L1 sürer. 35,4'te ikisi birden kesilir | replik 3-6 −8 dB (replik 6'da L2 −6); 24,4-26,4 ek −3 dB; 21,6 tıslama kesilmesine müzikle tepki YOK |
| 4 | **SUSKU — doruk** | C04 son · C05 · C06 ilk | 35,4–54,8 | **0** | her şey çıkar | replik 7, 8, 9 · kesme 40,0 ve 50,0 sessizlikte · nefes · ateşleme tıslaması 53,7'de başlar |
| 5 | TEK NOTA | C06 son | 54,8–60,0 | 1 | **L1 geri gelir**, tek nota, ateşlemeden 1,1 s sonra, başka katman YOK; 60,0'da yay kalkar | tıslama (57,0'a kadar, kuyruk 57,4) altında giriş; hışırtı J-girişi 58,8-59,5 (L1'in son 1,2 s'i) |
| 6 | **SUSKU — belirsizlik** | C07 · C08 · C09 · C10 ilk | 60,0–96,8 | **0** | hiçbir şey | "Bram?" 61,5 · seyrelen nefes · gün doğumu · ıska ~83,5 · silkinme 89,7 · replik 11 (94,0-96,0) · bitiş tıkı 96,1 · Sela'nın nefesi 96,3 |
| 7 | GERİ DÖNÜŞ | C10 son | 96,8–100,0 | 1 | **L1 geri gelir**, aynı nota, tek | — |
| 8 | EVE | C11 ilk yarı | 100,0–106,3 | 1 | **L3 girer** 100,0 (Mi+Si, sus2, üçlü yok) −8 dB; L1 −6 | Sela'nın alımı ~101,5 · Bram tık 101,8, alımı 102,0 · tıslama 102,5-104,5 · ip darbesi 102,6 · nefes-gülüş 105,3 · bitiş tıkı 106,0. Ateşlemeye vuruş/kabarma YOK |
| 9 | DARBE ÖNCESİ | C11 son · C12 ilk | 106,3–111,2 | 1 | **L3 kesilir** 106,3; L1 −18 dB'ye iner, kesilmez (L3 yok) | 4 s fan ve nefes; varış darbesi 110,0 (−6, filmin en yüksek efekti) çıplakta gelir; başlangıç tıkı 111,0 |
| 10 | ÇÖZÜLME | C12 | 111,2–113,0 | 2 | 111,2-111,8 L1 seviyesi geri döner, **L3 yeniden girer** (Mi+Si); **111,8 Si Do♯'ya çıkar → La majör**: filmin TEK çözülmesi; 113,0'da yay kalkar, KESME | ışık yayılması (110-116) · Bram'ın sığ nefesi |
| 11 | Son nefes | C12 | 113,0–120,0 | 0 | müzik yok | "Good call." 114,0-114,8 · Sela'nın titrek nefesi, 118,0 civarı oturur · açık hat hışırtısı |

Toplam: müzikli ≈52,3 s (%43,6) · müziksiz ≈67,7 s (%56,4).

Kesmelerin müzikle ilişkisi: 10,0 / 20,0 → müzik çalıyor, kesmeye karışmıyor · 30,0 → L2 yükselişi durur (tek kesme-yakın olay, görüntüyü taklit etmez; C04'ün inişine karşı yükselmeyi keser) · 40,0 / 50,0 → sessizlik kesmeyi kapsar (A4c 1,3 s ve A5 5,2 s gecikmeler korunur) · **60,0 → L1 yay kalkar** · 70,0 / 80,0 / 90,0 → sessizlik · **100,0 → L3 girer** · 110,0 → müzik −18 dB'de (yalnız L1), kesmeye ve darbeye tepki yok.

---

## 5. MÜZİK KENARI ↔ SES OLAYI BAĞ TABLOSU

Kural: müzik kenarı mutlak saniyeye değil, kaydedilmiş ses olayına bağlanır; kayıt süreleri ölçülünce kenar olayla birlikte kayar. Hiçbir kenar bir repliğin içine düşmez; hiçbir kenar bir ateşleme ya da temas anına oturmaz (kural 6).

| Kenar | Nominal | Bağ | Sapma yönü | Çevresindeki ses |
|---|:--:|---|---|---|
| L1 girer | 4,5 | replik 1 bitiş tıkı (4,3) + 0,2 s | tık kayarsa birlikte | replik 1 (3,0-4,1) |
| L2 girer | 14,6 | replik 2 bitiş tıkı (14,3) + 0,3 s | birlikte | replik 2 (12,5-14,1) |
| L2 durur (tek perde) | 30,0 | C03/C04 kesmesi | kesmeyle | — |
| SUSMA (L1+L2) | 35,4 | replik 6 sonu (35,3) + 0,1 s | birlikte; "you" üstüne asla | replik 6 (33,7-35,3); sonraki: Bram tık 36,0, replik 7 36,2 |
| TEK NOTA | 54,8 | C06 ateşleme başlangıcı (53,7) + 1,1 s; replik 9 sonundan (53,0) ≥ 1,5 s sonra | tıslama kayarsa birlikte | tıslama 53,7-57,0 (altında giriş) |
| L1 kalkar | 60,0 | C06/C07 kesmesi | kesmeyle | hışırtı işitilir 59,5 (tık varsa 58,8) |
| TEK NOTA (dönüş) | 96,8 | Sela'nın takılan nefesi (96,3) + 0,5 s; bitiş tıkı (96,1) sonrası | nefesle birlikte | replik 11 (94,0-96,0) |
| L3 girer | 100,0 | C10/C11 kesmesi | kesmeyle | — (ilk ses olayı ~101,5) |
| −12 dB'ye iniş | 106,3 | C11 bitiş tıkı (106,0) + 0,3 s | birlikte | nefes-gülüş 105,3 |
| kabarma başlar | 111,2 | C12 başlangıç tıkı (111,0) + 0,2 s | birlikte | varış darbesi 110,0 (+0,6 kuyruk) |
| ÇÖZÜLME | 111,8 | kabarmanın bitişi; ses olayı yok (boşluğun ortası) | kabarmayla | Bram'ın sığ nefesi |
| KESME | 113,0 | "Good call." başı (114,0) − 1,0 s | replikle birlikte | — |

---

## 6. REPLİK–MÜZİK ÇAKIŞMA TABLOSU (mutlak saniye)

| No | Replik | Mutlak | Müzik durumu |
|:--:|---|---|---|
| 1 | Lost my jets. | 3,0–4,1 | **müziksiz** (L1 4,5'te girer) |
| 2 | No, no— don't burn at me! | 12,5–14,1 | L1 −8 dB (L2 14,6'da girer) |
| 3 | Cut it. You're climbing… | 21,0–24,4 | L1 −8, L2 −8; 24,4-26,4 ek −3 |
| 4 | Copy. Down to two. | 26,4–27,8 | L1 −8, L2 −8 |
| 5 | Turn your back on me— and brake. | 30,8–33,1 | L1 −8, L2 −8 (L2 askıda) |
| 6 | Negative. I can see you. | 33,7–35,3 | L1 −8, L2 −6; müzik 35,4'te kesilir |
| 7 | At sunrise, I'm right in front of you. | 36,2–39,0 | **müziksiz** |
| 8 | At me— you're home… Your call. | 40,3–46,0 | **müziksiz** ("might" telsiz filtresinde en az "reach" kadar duyulur; ses miksi) |
| 9 | Sunrise. You be there. | 51,2–53,0 | **müziksiz** |
| 10 | Bram? | 61,5–62,1 | **müziksiz** (eski: L1 ek −6; artık yok) |
| 11 | I heard you. In the dark. | 94,0–96,0 | **müziksiz** |
| 12 | Good call. | 114,0–114,8 | **müziksiz** (müzik 113,0'da kesildi; eski: L1+L3 −8) |

12 replikten 7'si müziksiz (1, 7, 8, 9, 10, 11, 12), 5'i −6…−8 dB altında (2-6). Sela'nın 118,0 cevap nefesi müziksiz.

Sözsüz alışverişler (A7, A9a-c; ses planı): C07 hepsi müziksiz; C11 100,0-106,3 L1 −6 / L3 −8 (replik altı kuralı sözsüz alışverişe de uygulanır); C12 113,0 sonrası müziksiz.

---

## 7. KURAL KONTROLÜ

| Kural | Durum | Nerede |
|---|:--:|---|
| 1 Okuma cümlesi önce | TAMAM | §2 OKUMA |
| 2 En az bir müziksiz an, ideali doruk; 1-2 s önce susar; dönüş tek nota | TAMAM | 35,4–54,8 (doruk C05-C06): susma takasın başlamasından 4,9 s önce; dönüş 54,8 tek nota. Öteki iki susma: 60,0 → "Bram?" 1,5 s; 113,0 → "Good call." 1,0 s |
| 3 Fade-out yok; 1-2 çözülme | TAMAM | tek çözülme 111,8 (yedek B'de sıfır); bitiş yay kalkarak kesme (113,0); 96,8-106,3 sus2 çözülme sayılmaz |
| 4 Vuruşlar olaya; kesmeler `kurgu.py liste`'den | KISMEN | kenarlar ses olayına bağlı (§5); liste faz 8'de koşulacak. Kesmeler 10 s katı olduğundan sapma beklenmiyor; yalnız 60,0 ve 100,0 kesme-bağlı |
| 5 Telefon: alt bas oktav eşi | KISMEN | 110 Hz gövde + 165/220 Hz taşıyıcı (missing fundamental), 55 Hz yalnız derinlik; infrases yok. Gerçek telefon eşiği ölçülmedi (kılavuz §15.1a); faz 8 telefon testi |
| 6 Vakum: kuru; görüntü kaydırılır; mickey-mousing yok | TAMAM | reverb yok. 54,8 ateşlemeye değil, ondan 1,1 s sonraki kabullenmeye; 102,5 ateşlemesinde hiç; 21,6 tıslama kesilmesinde hiç; 111,8 çözülme varış darbesine değil ışığa bağlı; L2'nin C04'te inişi yok |
| 7 Miks: −14 LUFS / −1 dBTP; replik altı −6…−9; mono | TAMAM (plan) | §3, seviye otomasyonu; ölçüm faz 8'de |
| 8 Melodi alıntısı yok | TAMAM | pedal + tek çizgi + iki nota; bestecinin dokusuna atıf yok |

---

## 8. NEDEN BU PLAN — kısa gerekçe (tur 1'den değişenler)

1. **Müzik iki ses arasında taraf tutar, sonra çekilir.** İlk 35,4 s'de L2 gözün çizgisi olarak yükselir; ışık C02'de büyürken inandırıcıdır. C04'te ışık inerken çizgi yükselmez, durur ve askıda kalır (gözün güveni sarsılıyor ama sürüyor); "I can see you"dan hemen sonra cümlenin ortasında kesilir ve filmde bir daha gelmez.
2. **Doruk sessizdir, çünkü karar sese aittir.** Takas, kapanan gözler, dönüş, "You be there" ve ateşleme müziksiz. Tek nota ateşlemenin 1,1 s sonra gelir: onaylamaz, kabul eder.
3. **İkinci sessizlik filmin sorusunu korur.** "Bram yaşıyor mu?" C07'den C10'un 6,8. saniyesine kadar çıplak sesle sorulur ve müzik cevap vermez; dönüş aynı nota ve ancak Bram'ın sesi duyulduktan sonra. Tur 1'de C07-C08'de çalan pedal bu güvenceyi önceden veriyordu.
4. **Üç kez aynı nota** (4,5 · 54,8 · 96,8): söz, söz verilmesi, söz tutulduktan sonra duyulması.
5. **Çözülme bir bakıştır, kutlama değil.** 1,2 s sürer ve kesilir; onayı Bram söyler, sessizlikte. Evin müziği ışıkla gelir, sesle değil. Titrek gurur duygusunun titreği müzikte değil, 7,0 s'lik nefes ve hat sesinde taşınır.
6. **Telefonda duyulan pedal.** Tek nota ve çözülme 150 Hz üstü taşıyıcılarla kurulur; derin La yalnız ek ağırlıktır.

---

## 9. FAZ 8'E VE DİĞER AJANLARA NOTLAR

1. **Hışırtı, tıslama ve nefes anlamdır; müzik bunlara benzememeli.** Promptta "noise-like texture, breathy pad, airy flute, shimmer, bow noise" YOK. L1 150-400 Hz, telsiz hışırtısı 1-3 kHz; ayrı bantlar. L2 çok yüksek ve ince, 6 kHz altı.
2. **Üretim stratejisi: iki yol.** Susmalar üretimde garanti edilmez (Flow Music'in saniye hassasiyeti belgelenmedi, FLOW_GERCEKLERI §6). (a) Tek ~2:00 yatak üret, kenarları kapı (gate) ile aç/kapat: 4,5 L1, 14,6 L2, 100,0 L3 ve 111,8 Do♯ girişleri yatakta tutarsa. Yatakta L2, 38 s civarında kendiliğinden bitmeli; 54,8-60,0 ve 96,8-100,0 pencerelerinde yalnız L1 çalmalı. (b) Girişler ±0,5 s tutmazsa üç pencere ayrı üretilir: pencere A (4,5–35,4, L1 + L2), pencere B (54,8–60,0, yalnız L1), pencere C (96,8–113,0, L1 + L3 + çözülme); aynı stil bloğu, aynı ton, aynı enstrümanlar. Dikişler ≥ 19 s sessizlikte olduğundan "tek parça" bütünlüğü bozulmaz. Girişlerde swell (0,6-0,8 s fade-in) serbest; kapanışlarda 10-30 ms rampa, fade-out yok.
3. **Vuruş oynarsa görüntü kayar, müzik değil** (kural 6): klip başında 2-6 karelik pay. Müzik kenarları ses olayına bağlı olduğundan ses kaydı süreleri ölçülünce kenarlar olayla birlikte kayar (§5); müzik kendi içinde yeniden zamanlanmaz.
4. **Ses-tasarımcısı_2 ile uyum.** (a) 106,3–111,2: **L3 yok, L1 −18 dB, kesilmez** (Fable kararı 3; ses_2 §6 S11 "L3 yok" ve §9 ile aynı). L1 pedalı kesilip yeniden girmez; 111,2-111,8'de L1 seviyesi geri döner ve L3 çözülme için yeniden girer (Mi+Si, swell 0,6 s). Bu aralıkta L1 −18 dB işitilebilirlik eşiğinin altına yakın tutulur; faz 8'de dinlemede 110,0 darbesinin çıplaklığı bozuluyorsa L1 daha da kısılır, kesilmez. (b) 54,8 tek notası tıslamanın (pik −6, gövde −8) altında girer; faz 8'de ölçülür, duyulmuyorsa giriş 57,4'e (tıslama kuyruğu sonrası) kayar ve nota 2,6 s sürer. (c) Tık 58,8 kabul edilirse etki yok (§1). (d) Fan ve hışırtı hiçbir yerde dijital sıfıra inmez; 35,4, 60,0 ve 113,0 müzik kesmelerinde kulak sıfır almamalı. (e) C12 113,0-120,0'da müzik yok: ses planındaki "iç hacim uğultusu yok" kuralı bu aralıkta da geçerli.
5. **Kayıt zamanı uyuşmazlığı (müzik planı etkilenmez):** FILM §4 C05 gözlerin kapanmasını 45,6, dönüşü 46,0-47,0 verir; diyalog A5 daha geç. 35,4–54,8 sessizliği iki yorumu da kapsar.
6. **Nefes kuralı:** hiçbir müzik kenarı Sela'nın C05'teki tutulan nefesi ile bırakılması (47,0 civarı) arasına düşmez; zaten o aralık müziksiz.
7. **A/B izleyici testi (Fable kararı 2; faz 8).** İki kurgu: A = çözülmeli (111,8 Do♯), B = çözülmesiz (Si sürer, aynı 113,0 kesmesi). Fark yalnız 1,2 s; pencere C iki varyantla üretilir. Soru bitişten sonra açık uçlu: "Film bittiğinde ne hissettin, tek kelime." Öneri ölçüt: "zafer / kutlama / mutlu son / rahatlama" gelirse B; "titrek / hâlâ gergin / yarı" ise A. Eşit ya da belirsizse A (çözülmenin 1,2 s'de kesilmesi niyeti zaten taşıyor). Test kurgucu ve sahip tarafından yapılır; karar çıktısı F8_besteci_<n>.md'de.
8. **Telefon testi:** final iki cihazda dinlenir: kulaklık ve telefon hoparlörü. 54,8 ve 96,8 tek notaları telefonda net duyulmalı; duyulmuyorsa 165/220 Hz taşıyıcılar +3 dB (55 Hz'e dokunulmaz). C05 sessizliği "sıfır" gibi duyulmamalı (fan +3 dB ses planında).
9. **Replik altı otomasyon:** gerçek ses kayıt süreleriyle (take'ler) kurulur; atak 80 ms (kelimeden önce), bırakma 250 ms. Duck derinliği L2 için replik 6'da −6, öteki yerlerde −8.
10. **Kesme listesi:** `kurgu.py liste --kesmeler` çıktısı faz 8 KESME NOKTALARI tablosuna girer; 60,0 ve 100,0 doğrulanır.
11. **Prompt:** Flow Music resmî uzunluk/biçim sınırı belgelenmedi; İngilizce prompt kısa tutulur: tür, tempo, katman girişleri, dinamik, susma noktaları, bitiş, `[Instrumental]`, YOK listesi (vocals, drums, riser, whoosh). Nota adları ve niyet cümleleri (L2'nin Sol♯'e yükselişi) prompta kaynak olarak girmez.
12. **Denetçi (Ö4) için:** KABUL'lerin uygulanma yeri: kurgucu B1 → §3 FREKANS TABANI; B2 → §2 MÜZİKSİZ (2) + §3 seviye tablosu 106,3; B3 → §5 + seviye tablosu (replik 6 −6); B4 → §4 yoğunluk 2 + §2 OKUMA; B5 → §2 VURUŞ/SUSMA (L2 durur 30,0); B6 → §4. Diyalog B1 → §2 MÜZİKSİZ (2); B5 → §2 (113,0); B6 → §3 seviye tablosu 100,0-106,3.

```
ÖZET      MÜZİKSİZ AN 3 (ana 19,4 s · belirsizlik 36,8 s · bitiş 7,0 s; + açılış 4,5 s) · TEK ÇÖZÜLME 1 (yedek B: 0)
          KATMAN 3 (L1 · L2 · L3), aynı anda en çok 2 · YOĞUNLUK en çok 2 · MÜZİKLİ %43,6
          9 bulgu: KABUL 7 (kurgucu B1, B2, B5, B6 · diyalog B1, B5, B6) · KISMEN 2 (kurgucu B3, B4)
          RED parçaları: replik 6'da L2 −3 dB; OKUMA'dan "zafer olarak değil"i çıkarmak
          Diyalog B2-B4, B7-B10 ses kapsamı (müziğe etki notu §1). Kural 5 telefon eşiği ölçülmediği için KISMEN
          Fable kararı 3 (denetci F4.3): 106,3-111,2 L3 yok, L1 −18 (§1 son tablo)
AÇIK      faz 8: gerçek kesme listesi · A/B bitiş testi (§9 madde 7) · üretim stratejisi (a/b) · 54,8'in tıslama altında duyulması ·
          telefon eşiği ölçümü · 106,3-111,2 L1 −18 dB'nin dinlemede yeterli çıplaklık vermesi
YAPILMADI kulakla dinleme · kurgu.py liste --kesmeler (taslak yok) · gerçek take süreleri · spektral ölçüm
```
