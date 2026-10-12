# 🎬 THE_MAYDAY_SEA — Yardım İsteyen Okyanus

```
FILM           THE_MAYDAY_SEA
FORMAT         yatay 16:9
HEDEF_SURE     4:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/THE_MAYDAY_SEA/
URETIM         Google Flow (web) · QA Gemini uygulaması — sahip planı: görseller GPT Image, videolar Gemini Omni 1.1 Flash 10 s (ODA/SAHIP_PLANI.md §3); REPLİKLER OMNI'DE, VİDEODA (sahip kararı 12.10.2026) → Flow "Return silent videos" KAPALI
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `FIZIK_IDDIASI yok`: plan "alanın nasıl inşa edildiği filmde açıklanmaz; containment alanı kurmaca teknolojidir" der; belgesel fizik anlatımı yok.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.
>
> **KAYNAK: `ODA/SAHIP_PLANI.md` (sahibin verdiği plan, 12.10.2026, birebir).** §1-§7 oradan yerleştirildi; faz 1-4 ajan turu açılmadı
> (sahip talimatı: "bunu bozmadan aynı şekilde hazırla bu filmi de"). Fable'ın plandan türettiği tek şey biçim çevirisidir (sütunlar, numaralar,
> süreler, yatak/geçiş tabloları); olay, kompozisyon, replik ve tasarım planın kendisidir. Replik saniye ve süreleri Fable tahminidir.
> **Plandan tek bilinçli sapma (sahibin kendi talimatıyla, 12.10.2026):** plan "bütün konuşmalar kurguda eklenir" der; sahip "diyalogları video
> promptuna ekle, Omni modeli videoda üretsin" dedi → §5 Kaynak = **model sesi (…)**, replikler video promptlarında birebir, Flow'da ses AÇIK.
> Planın "aynı kaydı K02 → K12/K23'te kullan" yöntemi kurguda **yedek** olarak kalır (Omni aynı sesi başka klipte veremez; NOTLAR KARARLAR).

---

## 1. HİKÂYE

```
LOGLINE   Yıldızlar arasında asılı bir okyanustan gelen insan sesli yardım çağrısına cevap veren kurtarma pilotu, çağrının kendi sesiyle tekrarlandığını duyar ve canlı okyanusun tuzağından bağlantı halkasını geride bırakarak kaçar.
AMAÇ      Mara Keene yardım çağrısının kaynağına, yarı batmış araştırma istasyonuna yanaşıp içeri girer; çağrıyı yapanı bulmaya çalışır (sahne 2-6).
ENGEL     Ana verici enerjisiz ama çağrı sürer (7-8); camın dışında boş kask (9); su yerçekimine karşı duvara tırmanır (10); batık filo (11); alıcı Mara'nın kendi cümlesini çalar (12); okyanusun kendisi canlı ve çağrıları yem olarak kullanıyor (14-16); su şeridi hava kilidine ilerler (17) ve yanaşma halkasını tutar (19).
KARAR     Sahne 18: Mara normal ayrılma yerine acil ayrılma ister; sahne 20: acil bırakma kolunu çeker. Sahne 23: kendi sesini yeniden duyar, cevap vermez, alıcıyı kapatır.
SONUÇ     Feda halkası istasyonda kalır, kapsül uzaklaşır (21); kapsül alanın dışına çıkar (22); okyanus ve batık filo kalır, çağrı sürer (24).
BEDEL     Kapsül dış yanaşma halkasını kaybeder; Mara çağrıya bir daha cevap veremez, kanalı kendi eliyle kapatır · sahne 21 · 23
TEK SORU  "Mara çağrıya cevap verdiği için istasyonda kalacak mı, yoksa kaçabilecek mi?"
SEÇİM     Fable: sahip planı (tek aday, aday turu açılmadı) · 12.10.2026 · gerekçe: ODA/SAHIP_PLANI.md + ODA/DURUM.md SAHİP CEVAPLARI
SAHİP     ONAY (planı kendisi verdi: "bunu bozmadan aynı şekilde hazırla") · 12.10.2026
```

Açılış cümlesi (plan): "We found an ocean between the stars. Then it called for help." · Kapanış: "It wasn't waiting to be rescued. It was waiting to be answered."
Merak zinciri (plan): Bu su nasıl burada duruyor, kim yardım istiyor? → Enerjisiz verici nasıl çağrı gönderiyor? → Okyanus onun sesini mi öğrendi? → Su kapsülü de tutacak mı?

## 2. TRETMAN

<!-- kaynak: SAHIP_PLANI §5 "24 kliplik ana zaman çizelgesi" birebir (sahne = klip) -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | Yıldızlar arasında dev, yassı okyanus; içinde eski gemiler. Açılış cümlesi. | Başlığın mekân vaadi ilk karede karşılanır. |
| S2 | 0:10–0:20 | Mara kokpitte insan sesli yardım çağrısını duyar ve cevap verir: "Rescue vessel. I hear you." | Sonraki taklidin kaynak cümlesi söylenir. |
| S3 | 0:20–0:30 | Okyanusun kenarında yarı batmış, terk edilmiş araştırma istasyonu. | Kurtarma hedefi netleşir. |
| S4 | 0:30–0:40 | Kapsül su çizgisinin üstündeki kuru yanaşma soketine hizalanır. | Suya dokunmadan giriş yolu kurulur. |
| S5 | 0:40–0:50 | Halkalar temas eder; istasyonun tek kelepçesi kapanır. | Kapsül istasyona bağlıdır (sonra tuzak olacak bağ). |
| S6 | 0:50–1:00 | Mara ıslak koridorda; AI vericinin enerjisiz olduğunu bildirir. | Sesli çelişki kurulur: verici kapalı, çağrı sürüyor. |
| S7 | 1:00–1:10 | Kopuk güç kablosu, karanlık verici; çağrı yine duyulur. | Çelişkinin fiziksel kanıtı. |
| S8 | 1:10–1:20 | Mara çağrıyı yeniden duyar: "Then who is calling?" | Soru kaynağa döner. |
| S9 | 1:20–1:30 | Gözlem camının dışında yüzen boş bir kask. | Ekip gitmiştir; ilk kurban izi. |
| S10 | 1:30–1:40 | Koridorda bir su şeridi yerçekimine karşı duvara tırmanır. | Su kendiliğinden hareket eder. |
| S11 | 1:40–1:50 | Geniş pencerenin altında farklı dönemlerden batık gemi filosu. | Önceki kurbanlar görünür. |
| S12 | 1:50–2:00 | Alıcı Mara'nın kendi cümlesini aynen çalar: "Rescue vessel. I hear you." | Çağrı taklittir. |
| S13 | 2:00–2:10 | Mara donar: "That's my voice." | Tehdit kişiselleşir. |
| S14 | 2:10–2:20 | Suyun bütün hacmine yayılan ışıklı biyolojik ağ. | Yaşam bütün suda. |
| S15 | 2:20–2:30 | Tek yavaş ışık atımı bütün okyanusu geçer; AI: "The ocean itself is alive." | Okyanus organizmadır. |
| S16 | 2:30–2:40 | Su kordonu eski bir geminin antenine bağlı; AI: çağrılar yemdi. | Sesler önceki ekiplerden kopyalanmış. |
| S17 | 2:40–2:50 | Su şeridi koridorda hava kilidine ilerler. | İstasyon-kapsül yolu tehdit altında. |
| S18 | 2:50–3:00 | Mara kokpitte: "Emergency separation. Now." | Normal ayrılma yerine acil ayrılma. |
| S19 | 3:00–3:10 | Su şeridi kapsülün yanaşma halkasını tutar; bağlantı gerilim altında. | Normal ayrılma imkânsız. |
| S20 | 3:10–3:20 | Mara acil bırakma kolunu çeker. | Karar eyleme döner. |
| S21 | 3:20–3:30 | Feda halkası istasyonda kalır; kapsül geri çekilir. | Kaçış mümkün: halka bedel. |
| S22 | 3:30–3:40 | Kapsül okyanusun alanından çıkar. | Kaçış tamamlanır. |
| S23 | 3:40–3:50 | Mara'nın sesi bir kez daha alıcıdan gelir; Mara cevap vermez, alıcıyı kapatır. | Çağrıya son. |
| S24 | 3:50–4:00 | Okyanus ve batık filo; terk edilmiş halka portta. Son cümle. | İlk çağrının anlamı değişir. |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

<!-- kaynak: SAHIP_PLANI §4 R01-R09, numaralandı (sahip kararı 10.10.2026: <No>.<AD>, özne başına tek sayfa). Prompt metinleri SAHIP_PLANI'nda ve PROMPTLAR/G01.md REFERANS PROMPTLARI'nda -->
| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Mara Keene — TEK SAYFA (plan R01, üç görünüş): önden tam boy · arkadan tam boy · baş-omuz portre; 34 yaş, açık zeytin ten, gri gözler, kask içinde kısa düz siyah bob, sağ elmacık kemiğinde küçük soluk yara; fildişi basınç giysisi, grafit eklem contaları, lacivert omuz zırhı, ön kollarda dar yanık turuncu bantlar, sol göğüste tek yuvarlak altın-mavi rozet (soyut üçgen), beyaz eldivenler, siyah botlar; kapalı yuvarlak fildişi kask, tamamen şeffaf vizör (her görünüşte). F5 (G01, 12.10.2026): BEŞ panel — önden tam boy · arkadan tam boy · baş-omuz portre (önden) · baş-omuz ¾ portre (sağ ön, yara tarafı) · TEK beyaz eldiven yakın, elin sırtı (`glove panel`) | `1.MARA_v1.png` | v1 | | ⬜ | C02 · C06 · C08 · C13 · C18 · C20 · C23 |
| 2 | Kurtarma kapsülü dış (plan R02): kanatsız, kısa tekne biçimli grafit gövde, kavisli fildişi zırh panelleri, burun arkasında yanık turuncu şerit, geniş koyu kanopi, arkada dikey iki mavi-beyaz itici; önde dört kısa rijit ara bağlantı üstünde koyu gri silindirik FEDA yanaşma halkası, ortasında kapalı düz iç basınç kapağı; ¾ yan görünüş, burun sola. F5 (G01): ALTI panel — ¾ dış (halkalı) · tam yan, burun solda (halkalı) · burun yakın yan (halka takılı) · burun yakın yan, halka ayrılmış (dört çıplak bağlantı, kapak sağlam) · arka-üstten, burun sağda (halkasız) · tam yan, burun solda (halkasız, `side view after separation panel`) | `2.KAPSUL_v1.png` | v1 | | ⬜ | C01 · C04 · C05 · C19 · C21 · C22 |
| 3 | Kapsül kokpiti (plan R03): tek lacivert koltuk, fildişi tavan kabuğu, iki grafit dikmeli ön kanopi, kısa çift kumanda kolu, camgöbeği durum ışıklı alçak grafit konsol (yazısız soyut arayüz); konsolun sağ kenarında küçük alıcı hoparlör ızgarası + geniş fiziksel haberleşme anahtarı; sol kenarda geniş gümüş acil bırakma kolu, turuncu kavrama, görünür sabit menteşe ve durdurucu, kol DİK. F5 (G01): ALTI panel — göz hizası geniş iç (kol dik, anahtar açık) · sol konsol yakın, kol dik · sol konsol yakın, kol durdurucuda · alıcı yakın, anahtar açık, gösterge yanık · alıcı yakın, anahtar kapalı, gösterge sönük · geniş iç, kol durdurucuda + anahtar açık (`lever pulled, receiver on panel`) | `3.KOKPIT_v1.png` | v1 | | ⬜ | C02 · C18 · C20 · C23 |
| 4 | Uzay okyanusu ana dış (plan R04): ~10 km, yassı oval koyu deniz suyu hacmi, dalgacıklı üst yüzey, kalın saydam kavisli sarkan alt yüz, kara/deniz tabanı YOK; üç dev sabit siyah dikdörtgen containment çerçevesi farklı derinliklerde, ince sürekli camgöbeği alan sınırı; yüzeyin hemen altında küçük eski gemi enkazları; sağ kenarda küçük grafit silindir istasyon (alt yarı suda, yuvarlak port su çizgisi ve sınırın dışında); sağda minik fildişi kapsül. F5 (G01): DÖRT panel — geniş dış · geniş dış, canlı ağ silik · alttan görünüş (zar, `underside panel`) · enkaz filosu su altı (mekik kısa süpürme kanatlı, `wreck fleet panel`) | `4.OKYANUS_v1.png` | v1 | | ⬜ | C01 · C03 · C11 · C14 · C15 · C16 · C22 · C24 |
| 5 | Araştırma istasyonu yanaşma tarafı (plan R05): sırada üç kısa silindirik basınç modülü, oksitlenmiş dikişler, ortada geniş koyu güçlendirilmiş camlı gözlem modülü; alt yarı koyu turkuaz suda, camgöbeği sınır görünür; kuru sağ modülde su çizgisinin üstünde sağa, boşluğa bakan yuvarlak yanaşma soketi; yanında TEK geniş menteşeli kelepçe açık; sol uçta eğik çanak anten, kırık destek, kopuk besleme kablosu. F5 (G01): ÜÇ panel — dış geniş · yanaşma yakın yan, kelepçe açık · yanaşma yakın yan, kelepçe halkaya kapalı | `5.ISTASYON_v1.png` | v1 | | ⬜ | C03 · C04 · C05 · C19 · C21 |
| 6 | Hava kilidi + koridor (plan R06): kameraya yakın yuvarlak hava kilidi açıklığı, rijit kapak tamamen açık ve yana gömülü; düz dar grafit geçit, düz ızgara zemin, bel hizası korkuluklar, SAĞ zemin kenarında sığ koyu turkuaz su birikintisi, üstte soluk amber acil lambalar; SOL duvarda açık menteşeli servis dolabı, içinde küçük siyah verici modülü, güç fişi çıkmış; uçta gözlem odasına açık dikdörtgen kapı. F5 (G01): DÖRT panel — hava kilidi girişi geniş (su sağda, dolap solda) · ters alçak görünüş, gözlem ucundan hava kilidine (su solda, dolap sağda; C17) · zemin kenarı yakın (`floor-edge close panel`) · servis dolabı yakın | `6.KORIDOR_v1.png` | v1 | | ⬜ | C06 · C07 · C08 · C10 · C17 |
| 7 | Gözlem odası (plan R07): uzak duvarı dolduran geniş güçlendirilmiş pencere, alt kenarı dış okyanusun su çizgisinin altında; camın ardında koyu mavi suda sol kenara yakın terk edilmiş boş fildişi kask ve derinde rijit gemi enkazları; pencere altında alçak konsol, üstünde küçük pilli alıcı hoparlör (loş camgöbeği lamba); ıslak grafit zemin, tek soluk amber tavan ışığı; SAĞDA açık koridor kapısı; ceset yok. F5 (G01): ÜÇ panel — geniş iç (`wide interior panel`) · pencere yakın, kask lacivert kenarlı (`window close panel`) · konsol yakın, pilli alıcı (`console close panel`) | `7.GOZLEM_ODASI_v1.png` | v1 | | ⬜ | C09 · C11 · C12 · C13 |
| 8 | İletişim aksesuarları (plan R08, tek sayfa, üç nesne): SOL küçük pilli alıcı (mat siyah kasa, gümüş hoparlör ızgarası, tek camgöbeği gösterge, geniş fiziksel anahtar) · ORTA çizik siyah verici modülü, kalın gri güç fişi tamamen çıkmış yanında, lambalar sönük · SAĞ fildişi bilek tarayıcı (siyah cam yüzde tek camgöbeği halka, geniş koyu bilek kayışı) | `8.AKSESUARLAR_v1.png` | v1 | | ⬜ | C07 · C12 |
| 9 | Canlı su dokusu (plan R09, tek sayfa, üç panel): SOL su altı saydam zar, sabit dallanan soluk camgöbeği-altın kılcal çizgiler (yüz/göz yok) · ORTA çizik dikey metal duvara tırmanan tek kalın sürekli parlak koyu turkuaz su şeridi, tabanı zemin birikintisiyle görünür biçimde bağlı (tek kordon, dokunaç değil) · SAĞ aynı şerit rijit metal yanaşma halkasına bir kez dolanmış, yuvarlak kesit korunmuş. F5 (G01): BEŞ panel — su altı zar ağı (`membrane panel`) · duvara tırmanan tek şerit · rijit halkaya dolanmış şerit · ızgara zeminde ilerleyen şerit (C17) · enkazın anten yuvasına bağlı kordon (`wreck-cord panel`, C16) | `9.CANLI_SU_v1.png` | v1 | | ⬜ | C10 · C14 · C15 · C16 · C17 · C19 · C21 · C24 |

```
SHA-256: shasum -a 256 ~/film_medya/THE_MAYDAY_SEA/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
ÖZNE BAŞINA TEK SAYFA: plan R01 üç görünüşlü, R08 ve R09 üç panelli sayfalardır; F5'te çekimlerin istediği ek paneller aynı sayfaya eklenir, ikinci dosya açılmaz.
Plan ayrıca bazı çekimlerde ÖNCEKİ ÇEKİMİN KARESİNİ görsel kaynak olarak kullanır (C05←C04 son kare · C16←C11 · C19←C05 · C21←C19 · C22←C21):
bu zincir değildir, kompozisyon kaynağıdır. F5'te goruntu-yonetmeni BEŞİNİ DE KALDIRDI (12.10.2026, Fable KABUL): geometri referans sayfalarının
panellerinden (2.KAPSUL yan / ayrılma sonrası · 4.OKYANUS enkaz filosu) ve çekimler arası birebir kamera cümlelerinden (C04/C05/C19/C21 "held level with the
docking interface and seen from the side") gelir; her kare tek başına üretilir (THE_PLANET_THIEF C08 dersi). Panel listeleri PROMPTLAR/G01.md REFERANS PROMPTLARI.

ORTAK GÖRÜNÜM (12.10.2026, GECIS_VE_SES_SUREKLILIGI §1 — her görsel ve video promptunun sonunda birebir; plan "ortak stil" cümlesinden, araç/oran etiketi ve olumsuz kuyruk çıkarılmış):
  Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
MEKÂN IŞIĞI (birebir, mekân başına): DIŞ UZAY — cold white distant starlight from upper left, deep indigo shadows, faint cyan edge light from the containment boundary ·
  KOKPİT — cool blue water reflections from the canopy at frame-left, very faint amber console glow from below · İSTASYON İÇİ (koridor + gözlem odası) — faint amber emergency lamps from above, cool cyan light from the wet floor and the window ·
  SU ALTI — soft cyan-gold glow from the capillary network, deep teal falloff.
ORTAM SESİ (model sesi AÇIK film — aynı mekânın her VİDEO promptunda birebir; yatak yine kurguda, §6):
  DIŞ UZAY — The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static.
  KOKPİT — The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmet.
  İSTASYON İÇİ — The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips.
  SU ALTI — The only ambient sound is a deep, slow waterborne resonance with no rhythm.
Sabit tasarım (plan §8): okyanus yassı oval, kara yok, her dış planda aynı üç çerçeve + camgöbeği sınır · istasyon: anten SOL, gözlem ORTA, kuru port SAĞ ·
iç mekân normal yerçekimi ve basınç (C10 su buna aykırı) · Mara bütün filmde kapalı vizör ve aynı giysi · ana verici enerjisiz, alıcı ve amber lambalar pilli ·
sıradan suyun altında ayrı canavar yok; yaşam = bütün hacimdeki camgöbeği-altın ağ; göz/yüz/çoklu dokunaç yok · okyanus yalnız söylenmiş cümleyi tekrar eder ·
kapsül sağdan sola yanaşır; C05 halka+kelepçe · C19 su aynı halkayı tutar · C21 halka, kelepçe ve su istasyonda kalır, C22'de yalnız dış halka eksik.
```

## 4. ÇEKİM LİSTESİ

<!-- kaynak: SAHIP_PLANI §6 K01-K24; "Ekranda görünen" Image/Video prompt tariflerinden görünen dille; hepsi görüntüden video (plan: GPT Image kare → Gemini/Flow). Grup: G01 C01-C08 · G02 C09-C16 · G03 C17-C24 -->
| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Yıldızlar arasında dev, yassı bir su kütlesi asılı; içinde eski gemiler | Aşırı geniş dış plan: kadrajın orta üçte ikisini dolduran yassı oval okyanus, geniş yüzey dalgacıkları, seyrek yıldızlara karşı saydam sarkan alt yüz; üç siyah dikdörtgen çerçeve ve ince camgöbeği alan sınırı; yüzeyin hemen altında iki eski gemi enkazı; sağ kenarda küçük yarı batmış istasyon, daha sağda nokta gibi fildişi kapsül. Kamera yavaş yanal kayar, küçük kapsülle dev okyanus arasında paralaks; tek geniş alçak dalga yüzeyi geçer, hacim ve üç çerçeve sabit. | aşırı geniş dış, yavaş yanal kayma | kapsül sağda; dalga soldan sağa | 10 | Frames to Video | Okyanus küre/gezegen gibi görünmesin: yassı oval hacim, kara yok (plan öncelikli deneme 1); dev kırılan dalga/dönüşüm yok; model sesi Mara VO (kadraj dışı) ilk saniyede | 2.KAPSUL · 4.OKYANUS | G01 | ✍️ | — | — | — |
| C02 | Mara insan sesli çağrıyı duyar ve cevap verir | Yakın-orta plan: Mara pilot koltuğunda kemerli, kapalı şeffaf vizör ardında net yüz, sağ elmacık kemiğinde küçük yara; soldaki kanopiden vizöre mavi su yansımaları; sağ kenarda alıcının küçük camgöbeği durum lambası; eller kadraj dışı; kokpit kuru. Yavaş itiş; alıcıdan erkek çağrı gelir, Mara'nın bakışı kanopiden sağdaki alıcıya kayar; Mara konuşur; kontrollü nefesle sürer. | yakın-orta, yavaş itiş | bakış soldan sağa (alıcıya) | 10 | Frames to Video | Model sesi: iki replik (erkek çağrı telsiz · Mara AĞIZ KADRAJDA, vizör şeffaf → dudak senkronu, ≤5 s; SMOKE P9/P18); yüz 1.MARA portre paneli; ağız yalnız kendi cümlesinde hareket eder | 1.MARA · 3.KOKPIT | G01 | ✍️ | — | — | — |
| C03 | Hedef: okyanusun kenarında terk edilmiş, yarı batmış araştırma istasyonu | Geniş dış plan, istasyona yakın: üç modüllü grafit istasyon, alt yarıları koyu turkuaz suda; ortada su çizgisine yakın geniş güçlendirilmiş gözlem penceresi; sağ modülde kuru yuvarlak yanaşma soketi sağa, boşluğa bakar; sol uçta eğik çanak anten, kopuk besleme kablosu; arkada bir containment çerçevesi yükselir; soluk amber acil lambalar. Kamera kuru yanaşma modülüne doğru yavaş itilir; gövde çevresinde küçük dalgacıklar; modüller, pencere, anten rijit; soket açık kalır. | geniş dış, yavaş itiş | anten solda · gözlem ortada · soket sağda | 10 | Frames to Video | Mekân yerleşimi sabitlenir (plan §8: sonraki dış planlar aynı); model sesi AI telsiz (kimse kadrajda değil) | 4.OKYANUS · 5.ISTASYON | G01 | ✍️ | — | — | — |
| C04 | Kapsül su çizgisinin üstündeki kuru bağlantıya hizalanır | Orta dış yan plan: sağda kanatsız fildişi-grafit kapsül, burnu sola, solda istasyonun kuru yanaşma soketi; kapsülün koyu feda burun halkası soketle yatay hizada, arada kısa boşluk; turuncu burun şeridi, kapalı iç basınç kapağı ve dört rijit ara bağlantı okunur; altta camgöbeği alan kenarı ve koyu su; istasyonun tek kelepçesi açık. Sabit yan kamera; kapsül düz çizgide yavaş sola kayar, boşluğun çoğu kapanır, temas olmadan durur; yalpa yok. | orta dış yan, sabit | kapsül sağdan sola | 10 | Frames to Video | T01 temas BU çekimde olmaz (C05); kapsül düz, halka dairesel, soket sabit; model sesi AI telsiz | 2.KAPSUL · 5.ISTASYON | G01 | ✍️ | — | — | — |
| C05 | Halka sokete oturmuş; istasyonun tek kelepçesi kapanır | Yakın dış ek plan (C19 ile aynı kurulum: yanaşma arayüzü hizasında, yandan): burun halkası sokete oturmuş; istasyon tarafında tek geniş rijit menteşeli kelepçe açık, menteşesi ve kapanma yolu görünür; kapsülün koyu feda halkası ve kısa ara bağlantılar sağlam; arkada kapalı iç basınç kapağı; kuru bağlantının altında dar koyu turkuaz su şeridi. Sabit kamera; tek hareket: kelepçe menteşesinde iner, halkayı sarar, kilitlenir; son vuruşta kelepçe oturur, altta su dalgacığı sürer. | yakın dış ek plan, sabit (C19 açısı) | kelepçe yukarıdan aşağı | 10 | Frames to Video | T01: halka-soket teması C04→C05 KESMESİNDE (F5 teknik B1, Fable KABUL — plan K05 "kısa temas hareketi + kelepçe" iki temas istiyordu → PLANDAN SAPMA, sahibe); videoda tek hareket kelepçe; ek donanım üretilmesin; replik yok; plan "metal sesi, kısa sessizlik" → geçiş karartma C05→C06 (§6) | 2.KAPSUL · 5.ISTASYON | G01 | ✍️ | — | — | — |
| C06 | Mara boş koridora girer; AI vericinin enerjisiz olduğunu söyler | Geniş göz hizası koridor: Mara sol ön planda tamamen açık hava kilidinin içinde, botlar düz ızgara zeminde, şeffaf vizör kapalı, kollar bedene yakın; sağ zemin kenarında sığ koyu turkuaz su kanalı; sol duvarda servis dolabı açık; soluk amber acil lambalar uzaktaki gözlem odası kapısına uzanır; boş korkuluklar, çizik basınç duvarları. Yavaş ileri dolly hava kilidi çerçevesinden Mara'ya ve boş koridora; Mara yerinde, kaskını gözlem odası kapısına doğru çevirir; kapılar ve dolap açık, rijit; zemin suyunda küçük doğal dalgacık. | geniş iç, yavaş ileri dolly | Mara solda; bakış ileri (kapıya) | 10 | Frames to Video | İçeride normal yerçekimi (plan §8): su yalnız küçük dalgacık; model sesi AI telsiz, Mara'nın ağzı kapalı (yazılır) | 1.MARA · 6.KORIDOR | G01 | ✍️ | — | — | — |
| C07 | Ana verici enerjisiz; çağrı yine duyulur | Sıkı ek plan: koridorun açık sol duvar dolabı içinde siyah verici modülü, kalın gri güç fişi soketinden tamamen çıkmış, yanında sarkıyor; bütün verici gösterge lambaları sönük; paslı metal destekler, dolabın iç duvarında küçük ıslak iz; amber ışık koridordan, vericiden değil; rakam, yazı, el yok. Küçük yavaş itiş kopuk fişe ve karanlık modüle; her şey sabit, dolap kenarından tek damla iner; fiş hep soket dışında. | sıkı ek plan, küçük itiş | fiş sağda sarkar | 10 | Frames to Video | T06 yazı yok; plan: ses ölü modülden değil ayrı alıcıdan — model sesi erkek çağrı (kadraj dışı alıcı, telsiz filtresi) | 6.KORIDOR · 8.AKSESUARLAR | G01 | ✍️ | — | — | — |
| C08 | Mara çağrıyı yeniden duyar; kapalı verici ile ses bağdaşmaz | Yakın-orta: Mara açık servis dolabının yanında, bakış henüz hafif aşağıda, önündeki ızgara zemine (F5 devamlilik B7: başlangıç karesi hareketin sonunu göstermez; plan "gözlem odasına bakıyor" → küçük sapma); gri gözler ve sağ elmacık yarası kapalı vizör ardında; sol yanağa soluk amber koridor ışığı, diğer yana ıslak geçitten camgöbeği; dolap kenarı ve kopuk kablo arkada yumuşak; eller kadraj dışı. Yavaş itiş; kadraj dışındaki alıcıdan kısa statik gelir, bakış koridorun uzak kapısına kalkar; Mara soruyu sorar; nefes hafif sıklaşır; vizör berrak kalır. | yakın-orta, yavaş itiş | bakış aşağıdan sağa-ileriye (kapıya) kalkar | 10 | Frames to Video | Model sesi Mara AĞIZ KADRAJDA (vizör şeffaf), ≤5 s; ani baş çevirme/yürüme yok; ölçek C06'dan bir basamak yakın | 1.MARA · 6.KORIDOR | G01 | ✍️ | — | — | — |
| C09 | Camın dışında boş bir kask sürükleniyor | Gözlem penceresinden yakın bakış: koyu mavi suda eski boş fildişi kask, lacivert kenar, çizik şeffaf vizörü kameraya dönük, içi boş; sağda pencerenin siyah dikey kenarı ve birkaç mineral izi; aşağıda eski bir geminin silik silueti. Sabit kamera; kask soldan merkeze yavaş sürüklenir, yalnız birkaç derece döner, rijit biçimi ve boş içi okunur; yanından küçük kabarcık izi geçer; insan görünmez. | yakın, pencereden, sabit | kask soldan merkeze | 10 | Frames to Video | Kaskın içi boş kalmalı (baş/yüz üretilmesin); replik yok | 7.GOZLEM_ODASI | G02 | ✍️ | — | — | — |
| C10 | Su, tabanla bağını koruyarak duvara tırmanır | Alçak yakın plan: koridorun sağ zemin kenarı ve dikey grafit duvar; sığ zemin birikintisiyle sürekli tek kalın koyu turkuaz sıvı şerit duvara kısa mesafe tırmanmış; yuvarlak ıslak kenarlar, tek kordon gibi tutarlı kesit; sabit korkuluk desteği ve düz zemin ızgarası yerçekimi yönünü gösterir; camgöbeği yansımalar, soluk amber lamba; kimse yok. Sabit alçak kamera; şerit duvarda biraz daha yükselir, tabanı birikintiye görünür biçimde bağlı kalır, çapı sabit. | alçak yakın, sabit | şerit aşağıdan yukarı | 10 | Frames to Video | Tek kordon: dallanan dokunaç ya da insan biçimi yok (plan öncelikli deneme 2); replik yok | 6.KORIDOR · 9.CANLI_SU | G02 | ✍️ | — | — | — |
| C11 | Pencerenin altında farklı dönemlere ait batık gemi filosu | Gözlem odasının içinden geniş plan: alçak konsol ve güçlendirilmiş pencere koyu suyu çerçeveler; farklı derinliklerde rijit enkazlar: paslı dar keşif gövdesi, geniş kırık yük kapsülü, cama en yakın küçük beyaz mekik; altta birçok küçük gövde silueti; çok aşağıda saydam okyanusun içinden tek siyah çerçeve kenarı; kimse yok. Kamera yakın enkazlardan derindeki siluetlere yavaş aşağı tilt eder, filonun ölçeği açılır; gövdeler rijit ve ayrı, yalnız asılı parçacıklar sürüklenir. | geniş iç, yavaş aşağı tilt | tilt yukarıdan aşağı | 10 | Frames to Video | Hiçbir gemi Mara'nın kapsülüne benzemesin; gövdeler çökmez; model sesi AI telsiz (oda alıcısından) | 4.OKYANUS · 7.GOZLEM_ODASI | G02 | ✍️ | — | — | — |
| C12 | Alıcıdan Mara'nın az önce söylediği cümle gelir | Sıkı ek plan: gözlem odası konsolundaki küçük pilli alıcı; mat siyah kasa, gümüş hoparlör ızgarası, tek camgöbeği gösterge, geniş fiziksel anahtar; konsolun arka kenarında dar koyu turkuaz sıvı şerit, parlak yüzeyinde pencere suyunun mavi yansıması; alıcı sağlam, bağımsız güçlü; kumandalarda yazı yok. Küçük yavaş itiş hoparlör ızgarasına; camgöbeği gösterge sinyal alır gibi gittikçe parlar, alıcıdan kadın ses gelir; kasa ve anahtar kımıldamaz; şerit biçim değiştirmeden küçük dalgacık yapar. | sıkı ek plan, küçük itiş | alıcı ortada | 10 | Frames to Video | Model sesi: Mara'nın C02 cümlesi alıcıdan (kadraj dışı kadın ses, hafif telsiz filtresi); Omni aynı sesi veremez → kurguda C02 kaydı YEDEK (NOTLAR KARARLAR); yazı yok | 7.GOZLEM_ODASI · 8.AKSESUARLAR | G02 | ✍️ | — | — | — |
| C13 | Mara sesini tanır | Yakın-orta ¾ profil: Mara kadrajın solunda gözlem odasında, gözler kadraj dışındaki alıcıya; kapalı şeffaf vizörde sağ elmacık yarası ve gri gözler; arkadaki geniş pencerede yumuşak camgöbeği su yansıması; alt kenarda konsol boyunca ince koyu sıvı çizgi; Mara yerinde, eller kadraj altında; amber tavan ışığı kaskı fondan ayırır. Yavaş küçük kamera yayı ¾ açıdan daha önden bakışa, Mara yerinde; gözler hafif açılır, nefes bir kez takılır, Mara konuşur; ifade ince. | yakın-orta ¾ → ön, küçük yay | kamera soldan sağa yay | 10 | Frames to Video | Model sesi Mara AĞIZ KADRAJDA, ≤5 s; yüz tutarlı (1.MARA portre paneli); açı C08'den farklı (plan: benzer yakın planlar üst üste gelmez) | 1.MARA · 7.GOZLEM_ODASI | G02 | ✍️ | — | — | — |
| C14 | Okyanusun alt yüzeyinde damar benzeri dev ağ | Geniş alt görünüş: yüzen okyanusun saydam kavisli sarkan hacminin içinden geniş sürekli su zarı, çok geniş alanda dallanan sabit soluk camgöbeği-altın kılcal çizgiler; eski enkazlar aynı ağa takılı, küçük ölçekte; uzak arka planda düz siyah çerçeve kirişi, suyun kavisli kenarının ötesinde derin uzay; ayrı hayvan, yüz, göz, ağız yok. Yavaş yanal takip saydam alt yüz boyunca, paralaksla ağın ve enkazların daha fazlası açılır; tek geniş dalda yumuşak camgöbeği-altın ışık atımı yürür; zar ve sınır sabit. | geniş alt görünüş, yavaş yanal takip | kamera soldan sağa | 10 | Frames to Video | Ayrı yaratık/biçim değişimi yok; zar ve okyanus sınırı sabit (plan öncelikli deneme 3); replik yok | 4.OKYANUS · 9.CANLI_SU | G02 | ✍️ | — | — | — |
| C15 | Tek yavaş ışık atımı bütün su kütlesinden geçer: okyanusun kendisi canlı | Aşırı geniş dış: aynı yassı oval okyanus ve üç rijit dikdörtgen çerçeve; dalgacıklı yüzeyin altında dev dallanan camgöbeği-altın ağ bütün hacimde silik görünür; istasyon sağ kenarda sabit, Mara'nın kapsülü kuru sağa bakan porta yanaşık; enkazlar yüzey altında; derin siyah uzay, seyrek yıldızlar. Sabit uzak kamera; tek geniş kademeli camgöbeği-altın ışık atımı ağ boyunca okyanusu geçer; oval hacim, çerçeveler, istasyon ve kapsül değişmez, dalgacıklar ölçülü. | aşırı geniş dış, sabit | atım soldan sağa | 10 | Frames to Video | Dev büzülme/açılan ağız yok; model sesi AI telsiz (kimse kadrajda değil) | 4.OKYANUS · 9.CANLI_SU | G02 | ✍️ | — | — | — |
| C16 | Canlı su ağı eski gemilerin iletişim bölümlerine uzanıyor: çağrılar yem | Yakın su altı görünüş: aynı koyu turkuaz okyanusa hapsolmuş eski paslı keşif gemisi enkazı; rijit gövde, koyu kanopi, küçük kırık anten yuvası okunur; geniş camgöbeği-altın zardan tek tutarlı parlak sıvı kordon anten yuvasına ve alıcı bölmesine bağlı; kılcal ağın kalanı arkaya çekilir; beden, yüz, ayrı canavar yok. Yavaş itiş kordonun enkazın haberleşme bölmesiyle temasına; o tek kordon boyunca eski yuvaya silik ışık atımı yürür; enkaz ve anten sabit, onarım/dönüşüm yok; suda seyrek parçacık. | yakın su altı, yavaş itiş | kordon soldan enkaza | 10 | Frames to Video | Mekanik onarım/dönüşüm yok; model sesi AI telsiz (kimse kadrajda değil); plan kaynak kare C11 bağımlılığı F5'te kaldırıldı (enkaz tasarımı metinle + 4.OKYANUS enkaz filosu paneli); ref 9 yalnız enkaz-kordon paneli | 4.OKYANUS · 9.CANLI_SU | G02 | ✍️ | — | — | — |
| C17 | Su şeridi koridorda hava kilidine ilerliyor | Alçak koridor görünüşü, uzaktaki tamamen açık hava kilidine bakar (giriş yönünün tersi → su kanalı kadrajın SOLUNDA, açık servis dolabı sağda; plan "right floor channel" giriş yönünden söylüyordu, F5'te aynalandı, iki eleştirmen KORU): zemin kanalı boyunca tek kalın pürüzsüz koyu turkuaz sıvı şerit, ön ucu düz ızgaranın ortasında, hava kilidine yönelik; korkuluklar, acil lambalar ve açık servis dolabı yerli yerinde; kimse yok; coğrafya giriş koridoruyla aynı (6.KORIDOR ters görünüş paneli). Alçak yavaş takip tek şerite paralel; ucu zeminde açık hava kilidine doğru ilerler; şerit bütün ve pürüzsüz, çok uzva ayrılmaz; kapılar ve duvarlar rijit; sel dalgası yok. | alçak, yavaş takip | şerit kameradan uzağa (hava kilidine); su solda, dolap sağda | 10 | Frames to Video | Tek şerit, çok uzuv yok; Mara'nın koşusu üretilmez (C18 kokpit, kesme); replik yok; sol/sağ aynalama plandan sapma (sahibe) | 6.KORIDOR · 9.CANLI_SU | G03 | ✍️ | — | — | — |
| C18 | Mara kokpitte; acil ayrılma ister | Orta ¾ plan: Mara aynı kurtarma kapsülü kokpitine yeniden kemerli, kapalı şeffaf vizörlü fildişi basınç giysisi; SAĞ omzu kadrajın solunda dik duran geniş gümüş acil bırakma koluna (turuncu kavrama) yakın (kamera Mara'nın sağ-önünde; plan "sol omuz" kadraj düzeniyle çelişiyordu → F5 Fable KABUL, sahibe); sağ kenarda alıcının camgöbeği göstergesi yanıyor; kuru kanopide silik su yansımaları; ileri yanaşma yönü ve sabit dikmeler öncekiyle aynı. Hafif yavaş itiş; Mara kemere yaslanır, kontrollü bir nefes alır (ortam cümlesi "calm breathing" ile çelişmesin, F5 teknik B13), gözler bırakma kolunda; Mara konuşur; eller kadrajın hemen altında, kol henüz oynamaz; kabin kuru. | orta ¾, hafif itiş | kol solda; bakış sola | 10 | Frames to Video | Model sesi Mara AĞIZ KADRAJDA, ≤5 s; kol BU çekimde çekilmez (C20); koridor→kokpit geçişi kesmeyle (koşu, kask, kapı yok) | 1.MARA · 3.KOKPIT | G03 | ✍️ | — | — | — |
| C19 | Canlı su şeridi kapsülün yanaşma halkasını tutuyor; bağlantı gerilim altında | Yakın dış: C05'teki aynı yanaşık burun halkası-soket arayüzü; istasyonun geniş kelepçesi kapsülün koyu feda yanaşma halkasına kapalı, halka dört kısa rijit ara bağlantıyla kapsüle bağlı; istasyon tarafındaki sudan tek tutarlı koyu turkuaz sıvı şerit halkanın çevresine bir kez dolanmış; arkada iç basınç kapağı kapalı; ince camgöbeği alan sınırı ıslak istasyon kenarının hemen ötesinde, kapsül tarafında kuru siyah uzay. Sabit kamera; su şeridinin istasyon tarafındaki tabanında su toplanır, halkanın parlak yüzeyi parlaklaşır, boyutu değişmez (tek pürüzsüz ıslak halka; kelepçe halkanın soket ucunda, su orta bandında, arada çıplak metal bant); metal halka, kelepçe ve ara bağlantılar bükülmez, büyümez; küçük damlacıklar istasyon tarafında kalır. | yakın dış, sabit (C05 açısı) | şerit soldan (istasyon) halkaya | 10 | Frames to Video | Halka/kelepçe/ara bağlantı sağlam, bozulma yok (plan §8); kelepçe halkanın soket ucunu, su orta bandını sarar, arada çıplak metal bant; "sıkılaşma" yerine su şeridinin tabanında toplanma + parlaklaşma (F5 teknik B7); model sesi AI telsiz; C05 ile birebir kamera cümlesi, plan kaynak kare bağımlılığı kaldırıldı | 2.KAPSUL · 5.ISTASYON · 9.CANLI_SU | G03 | ✍️ | — | — | — |
| C20 | Mara acil ayrılma kolunu çeker | Sıkı kokpit ek planı: sol konsolda geniş gümüş acil bırakma kolu, turuncu kavrama; Mara'nın SAĞ beyaz eldiveni (kol kadrajın solunda = pilotun sağı; plan "left glove" → F5 Fable KABUL, sahibe) kavramayı zaten sarmış, ön kolu doğal olarak kadraj dışına uzanır; kolun tek sabit menteşesi ve mekanik durdurucusu açıkça görünür; kol dik başlar, kokpit referansıyla aynı; soluk camgöbeği konsol ışığı ve amber yansımalar çizik metalde; yazılı etiket yok. Sabit kamera; Mara zaten tuttuğu rijit kolu menteşesi çevresinde kısa bir yayla mekanik durdurucuya kadar çeker; eldiven aynı kavramada, yeni parmak ya da kumanda yok; son vuruşta kol durdurucuda tutulur, eldiven kavraması hafif gevşer. | sıkı ek plan, sabit | kol yukarıdan aşağı (sola) | 10 | Frames to Video | T01: el ilk karede kolu tutuyor (kavrama + çekme aynı klipte değil, plan); tek menteşe hareketi; replik yok | 1.MARA · 3.KOKPIT | G03 | ✍️ | — | — | — |
| C21 | Kapsül dış halkayı istasyonda bırakır ve geri çekilir | Orta dış yan plan: kapsül burnu hâlâ sola, istasyona dönük; koyu feda yanaşma halkası istasyon kelepçesinde kilitli ve aynı sıvı halkayla tutulmuş; o halka ile kapsülün dört ara bağlantısı arasında yeni açılmış dar boşluk, acil kopuş başlamış; boşluğun arkasında kapsülün düz iç basınç kapağı kapalı ve görünür; solda istasyon, okyanus ve camgöbeği alan kenarı; sağda açık siyah uzay. Sabit yan kamera; rijit kapsül istasyondan uzağa sağa yavaş kayar, boşluk genişler; bütün feda halkası, kelepçe ve sıvı halka istasyon tarafında sabit kalır; kapalı iç kapak kapsülde kalır; uzayan hortum ya da dokunaç izlemez. | orta dış yan, sabit | kapsül soldan sağa | 10 | Frames to Video | Patlama/dönüşüm yok, boşluk ilk karede var (plan öncelikli deneme 4); iç kapak kapsülde; kelepçe halkanın soket ucunda, su orta bandında; replik yok; plan kaynak kare C19 bağımlılığı kaldırıldı (2.KAPSUL "yan, ayrılma sonrası" paneli + metin) | 2.KAPSUL · 5.ISTASYON · 9.CANLI_SU | G03 | ✍️ | — | — | — |
| C22 | Kapsül okyanusun alanından çıkar; kaçış tamam | Arka-üstten geniş dış: fildişi-grafit kurtarma kapsülü açık uzaya, sağa doğru, burnu uçuş yönünde (C21'den sonra kesmede dönmüş sayılır); burun arkadan okunmaz, halka bedeli C21 ve C24'te; düz iç basınç kapağı kapalı; gövde, turuncu şerit ve çift arka itici değişmemiş; solda dev oval okyanus, üç sabit çerçeve ve yarı batmış istasyon uzaklaşır; camgöbeği alan sınırı tamamen kapsülün arkasında; kapsüle bağlı su şeridi yok. Kamera kapsülle takip eder, kapsül sabit hızla uzaklaşır, alandan uzaklık sürekli artar; iki sabit arka itici biçimini korur; arkadaki okyanus ve istasyon geometrisi sabit; alanın ötesinde hiçbir şey izlemez. | geniş dış, arka-üstten takip | kapsül sola→sağa uzaklaşır | 10 | Frames to Video | Kapsülde yalnız dış halka eksik (ana gövde, cam, iki motor sağlam — plan §8); T13: hızlanma/parlayan itici istenmez (model motor sesi koyar), klip sesi yalnız replik penceresi (§6); model sesi AI telsiz; plan kaynak kare C21 bağımlılığı kaldırıldı (2.KAPSUL arka-üst halkasız paneli) | 2.KAPSUL · 4.OKYANUS | G03 | ✍️ | — | — | — |
| C23 | Mara kendi sesini yeniden duyar; cevap vermez, kanalı kapatır | Orta kokpit planı: Mara sol yarıda, yüz ve sağ elmacık yarası şeffaf vizörden görünür; sağ ön planda SOL beyaz eldiveni (alıcı kadrajın sağında = pilotun solu; plan "right glove" → F5 Fable KABUL, sahibe) alıcının geniş fiziksel anahtarının ÜSTÜNDE (temas karede kurulu; plan "yanında"), anahtar hâlâ açık konumda, üstünde camgöbeği gösterge; kanopi dışında yalnız uzak yıldızlar ve küçük uzak mavi alan parıltısı; duruş sabit; soldaki acil bırakma kolu çekilmiş konumda. Sabit kamera; alıcıdan kadın ses gelir, Mara'nın ağzı kapalı; Mara tek küçük kararlı hareketle anahtarı kapalı konuma alır, camgöbeği gösterge söner; sonra sessiz yüz, nefes; kabin kuru, kumandalar rijit. | orta kokpit, sabit | eldiven sağda; anahtar aşağı | 10 | Frames to Video | Model sesi: Mara'nın C02 cümlesi alıcıdan — Mara KONUŞMAZ, ağzı kapalı (T16: model Mara'yı konuşturabilir, promptta yazılır); Omni aynı sesi veremez → kurguda C02 kaydı YEDEK; ses anahtardan ÖNCE biter | 1.MARA · 3.KOKPIT | G03 | ✍️ | — | — | — |
| C24 | Okyanus ve geçmiş kurbanlar; çağrının anlamı değişti | Final aşırı geniş dış: aynı yassı oval okyanus üç sabit dikdörtgen siyah çerçevede; yarı batmış istasyon sağ kenarda, kuru portunda terk edilmiş feda yanaşma halkası hâlâ kapalı kelepçede, kapsül yok; dalgacıklı yüzeyin altında saydam suda çok sayıda eski gemi silueti; dev camgöbeği-altın biyolojik ağ bütün hacimde silik; seyrek yıldızlar, açık siyah uzay; yeni araç ya da kişi yok. Yavaş geri çekilme batık filonun daha fazlasını açar, okyanus, çerçeveler ve istasyon geometrisi korunur; ağ boyunca tek yumuşak ışık atımı yürür ve söner; bütün tekinsiz okyanusta biter. | aşırı geniş dış, yavaş geri çekilme | kamera geri | 10 | Frames to Video | Yeni araç/kişi/ikinci tehdit yok; model sesi Mara VO (kadraj dışı); film adı gerekirse son 2 s kurguda; F7 kare denetimi: ref 4 `living network panel` yanaşık kapsül taşır, C24 karesinde kapsül olmamalı (devamlilik 1b kapsam dışı notu) | 4.OKYANUS · 9.CANLI_SU | G03 | ✍️ | — | — | — |

```
Süre: her çekim 10 (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10 = 24; toplam = 4:00.
  Ritim süreyle değil çekim içi hareket ve kadraj/ölçek değişimiyle kurulur (ARIZA H10).
Flow modu: hepsi Frames to Video (plan: GPT Image başlangıç karesi → görüntüden video). Plan kaynak kare bağımlılıkları (C05←C04 · C16←C11 · C19←C05 · C21←C19 · C22←C21)
  zincir değildir; goruntu-yonetmeni gerekiyorsa kaynağı iş emrine yazar, gerekmiyorsa kaldırır (THE_PLANET_THIEF C08 dersi).
Risk: ARIZA_LISTESI T kodu → "nasıl gösterilir". Model sesi satırları §5 Kaynak sütunuyla birebir (ağız kadrajda ≤5 s; telsiz/VO ≤8 s).
Grup: PROMPTLAR/G01.md C01-C08 · G02.md C09-C16 · G03.md C17-C24. Durum: ⬜ · ✍️ prompt · 🖼️ kare onaylı · 🎥 deneme · ✅ seçildi.
Plan öncelikli denemeler (SAHIP_PLANI §8 "Önce dört zor planı dene"): C01 okyanus küre gibi görünmesin · C10 tek şerit duvara tırmansın ·
  C14 ağ suyla aynı hacimde okunsun · C21 halka istasyonda kalırken kapsül bozulmadan uzaklaşsın. Bir hareket kararsız çıkarsa daha basit başlangıç karesi düzenlenir, hareket eklenmez.
Kesme sürekliliği (12.10.2026): ardışık aynı-mekân çekimlerinde ölçek ya da açı değişir (C06 geniş → C07 ek → C08 yakın-orta; C11 geniş → C12 ek → C13 yakın-orta ¾;
  C18 orta ¾ → C19 dış → C20 ek → C21 dış); ilk vuruş hareketle başlar; geçiş türleri §6 GEÇİŞ.
```

## 5. REPLİKLER

<!-- kaynak: SAHIP_PLANI §7 "Ses metni" tablosu birebir (18 replik: K02'de iki). Saniye ve süre Fable tahmini (≈2,5 kelime/s; çağrı yorgun, yavaş), F8'de klibin gerçek zamanlamasıyla kesinleşir.
     KAYNAK = model sesi (…) — sahip kararı 12.10.2026: Omni konuşmayı videoda üretir; video promptu repliği birebir taşır. "ağız kadrajda" yalnız Mara'nın yüzü kadrajda olup kendisi konuştuğu çekimlerde (C02 · C08 · C13 · C18): tavan 5 s.
     C12 ve C23 OCEAN satırları Mara'nın sesidir ama Mara konuşmaz: ses alıcıdan, Mara'nın ağzı kapalı. Omni başka klipte aynı sesi veremez → planın "aynı kaydı kullan" yöntemi kurguda yedek (NOTLAR KARARLAR).
     Kayıt: Mara/CALLER/OCEAN HUMAN (yedek kayıt insan sesi) · AI MACHINE (plan: sakin yetişkin erkek ses, aşırı robot efekti yok; Fable varsayımı) -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R01 | C01 | 0.5 | Mara (VO) | model sesi (voice-over, kadraj dışı) | HUMAN | We found an ocean between the stars. Then it called for help. | 4.5 |
| R02 | C02 | 1.0 | CALLER (erkek) | model sesi (telsiz, kadraj dışı erkek çağrı) | HUMAN | Mayday. Please. Come closer. | 2.5 |
| R03 | C02 | 5.0 | Mara | model sesi (telsiz · ağız kadrajda, vizör şeffaf) | HUMAN | Rescue vessel. I hear you. | 2.0 |
| R04 | C03 | 4.0 | AI | model sesi (telsiz, kadraj dışı) | MACHINE | A research station. Half submerged. | 2.5 |
| R05 | C04 | 4.0 | AI | model sesi (telsiz, kadraj dışı) | MACHINE | Dock above the waterline. | 2.0 |
| R06 | C06 | 4.5 | AI | model sesi (telsiz, kadraj dışı; Mara'nın ağzı kapalı) | MACHINE | The station's transmitter has no power. | 2.5 |
| R07 | C07 | 5.0 | CALLER (erkek) | model sesi (telsiz alıcı, kadraj dışı — C02 ile aynı cümle) | HUMAN | Mayday. Please. Come closer. | 2.5 |
| R08 | C08 | 5.0 | Mara | model sesi (telsiz · ağız kadrajda, vizör şeffaf) | HUMAN | Then who is calling? | 1.5 |
| R09 | C11 | 4.0 | AI | model sesi (telsiz, kadraj dışı) | MACHINE | Those are ships. Dozens of them. | 2.5 |
| R10 | C12 | 4.5 | OCEAN (Mara'nın sesi) | model sesi (telsiz alıcı, kadraj dışı kadın ses — C02 R03 ile aynı cümle; kurguda C02 kaydı yedek) | HUMAN | Rescue vessel. I hear you. | 2.0 |
| R11 | C13 | 5.0 | Mara | model sesi (telsiz · ağız kadrajda, vizör şeffaf) | HUMAN | That's my voice. | 1.5 |
| R12 | C15 | 4.0 | AI | model sesi (telsiz, kadraj dışı) | MACHINE | No separate organism. The ocean itself is alive. | 3.5 |
| R13 | C16 | 4.0 | AI | model sesi (telsiz, kadraj dışı) | MACHINE | It has been using their calls as bait. | 3.0 |
| R14 | C18 | 4.0 | Mara | model sesi (telsiz · ağız kadrajda, vizör şeffaf) | HUMAN | Emergency separation. Now. | 2.0 |
| R15 | C19 | 4.0 | AI | model sesi (telsiz, kadraj dışı) | MACHINE | The docking assembly is under load. | 2.5 |
| R16 | C22 | 4.0 | AI | model sesi (telsiz, kadraj dışı) | MACHINE | We're clear of the field. | 2.0 |
| R17 | C23 | 2.0 | OCEAN (Mara'nın sesi) | model sesi (telsiz alıcı — Mara kadrajda ama KONUŞMAZ, ağzı kapalı; kurguda C02 kaydı yedek) | HUMAN | Rescue vessel. I hear you. | 2.0 |
| R18 | C24 | 3.0 | Mara (VO) | model sesi (voice-over, kadraj dışı) | HUMAN | It wasn't waiting to be rescued. It was waiting to be answered. | 4.5 |

```
Kaynak: telsiz · kadraj dışı · kask içi · makine · kayıt → ses kurguda eklenir, ≤ 8 s
        ağız kadrajda (son çare) → model dudak senkronu, ≤ 5 s, sayı yok, video promptunda tırnak içinde birebir
        model sesi (telsiz | voice-over | ağız kadrajda) → replik video promptuna BİREBİR yazılır, Omni konuşmayı videoda üretir (sahip kararı 12.10.2026);
        ≤ 8 s (ağız kadrajda ≤ 5 s); klip sesi filme girer (timeline klip_sesi), kurgu kaydı yedek. BU FİLMDE BÜTÜN REPLİKLER MODEL SESİ.
Kayıt: HUMAN | MACHINE · bant: 4 dk 12-24 replik → 18 replik, bant içinde.
Plan kuralları: C05 · C09 · C10 · C14 · C17 · C20 · C21'de replik yok (görüntü ve efekt taşır). Replikler on saniyenin tamamına yayılmaz; nefes, dinleme ve kesme için boşluk.
R01 ilk saniyede başlar. R17 anahtar hareketinden ÖNCE gelir ve biter (C23 vuruş planı). Ses profilleri (plan §7): Mara doğal yetişkin kadın, başta profesyonel, ortada
duraksayan, kaçışta kısa ve kararlı · AI sakin yetişkin erkek, kısa teknik tespit, aşırı robot efekti yok · CALLER başka yetişkin erkek, yorgun, telsizden, anlaşılır.
Omni sınırı: aynı sesin başka klipte tekrarı (R07 ↔ R02 · R10/R17 ↔ R03) model tarafından garanti edilmez; F7'de SMOKE P18 ölçer; tutmazsa planın yöntemi:
C02 klibinin sesi `timeline.json` ses parçası olarak C07/C12/C23'e yerleştirilir (klip_sesi o parçalarda kapatılır).
```

## 6. SES PLANI — model sesi yalnız §5 replikleri için (Omni); ortam, efekt ve müzik kurguda

<!-- kaynak: SAHIP_PLANI her klibin "Audio:" satırı + §7 "Dört dakikalık ses yayı". Hatta ortam yatağı ve efektler kurguda kurulur; klibin kendi sesi yalnız replik için (klip_sesi). F4 ses-tasarimcisi açılmadı (sahip planı); yatak ve geçiş tabloları Fable'ın plandan çevirisi, F8 kurgucu kesinleştirir. -->
| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 | Y1 dış basınç tonu · soluk gelen telsiz hışırtısı · R01 (klipten) · müzik alçak | S2 telsiz hışırtısı J 1 s (C01 sonu) | vakum: yayılan ses değil, tasarım (plan) |
| S2 | Y2 kabin havalandırması · nefes · kısa telsiz hışırtısı patlaması · R02 + R03 (klipten) | S3 yön çanı J 1 s | müzik replik altında −6…−9 dB |
| S3 | Y1 · kısa sakin yön çanı (alıcı perspektifi) · R04 (klipten) · ölçülü gerilim tasarımı | — | |
| S4 | Y1 · soluk hizalama tonu (haberleşme perspektifi) · R05 (klipten) | — | |
| S5 | Y1 · tek boğuk temas vuruşu · tek metal mandal (bağlı gövdeden) · kısa sessizlik | mandal → karartma 0,6 s → S6 havalandırma J | replik yok; plan: "metal sesi, kısa sessizlik" |
| S6 | Y3 basınç sistemi havalandırması · yakın nefes · uzak ıslak tık · R06 (klipten) | — | iç mekân basınçlı |
| S7 | Y3 · uzak gelen telsiz hışırtısı (ayrı alıcıdan) · R07 (klipten) | — | ses ölü modülden değil |
| S8 | Y3 · kısa alıcı statik parçası · bitişik odadan tek soluk ıslak darbe · R08 (klipten) | S9 oyuk su rezonansı J 1,5 s | |
| S9 | Y4 gözlem odası (Y3 + camdan oyuk su rezonansı) | — | replik yok |
| S10 | Y3 · tek yakın yapışkan ıslak sürtünme | — | replik yok |
| S11 | Y4 · daha derin su yapısal rezonansı · soluk alıcı hışırtısı · R09 (klipten) | — | |
| S12 | Y4 · kısa gelen statik patlaması · R10 (klipten; yedek C02 kaydı) · müzik düşer | — | plan: müzik azalır, aynı ses öne çıkar |
| S13 | Y4 · tek takılan nefes · konsoldan alçak ıslak tık · R11 (klipten) | S14 su altı rezonansı → karisim 0,5 | |
| S14 | Y5 su altı · tek yavaş alçak atım (diegetik olmayan biyolojik tasarım) | S15'e atım L 1 s | replik yok |
| S15 | Y1 · tek alçak tasarım atımı (parlaklıkla kabaca eş) · R12 (klipten) | — | |
| S16 | Y5 · alçak su içi uğultu · kısa uzak telsiz benzeri parazit · R13 (klipten) | S17 ıslak kayma + alarm J 1 s | |
| S17 | Y3 · yakın ıslak kayma · tek alçak alarm tonu | alarm S18'e L 1 s | replik yok |
| S18 | Y2 · nefes · kısa yanaşma gerilim alarmı · R14 (klipten) | — | |
| S19 | Y1 · gergin gövde gıcırtısı (Mara'nın bağlı kabininden iletilen) · R15 (klipten) | — | dış kükreme yok |
| S20 | Y2 · tek sağlam mekanik klunk · kısa bırakma onay tonu | klunk → S21 J 0,5 s | replik yok |
| S21 | Y1 · kısa boğuk ayrılma itkisi (pilotun gövdesinden) | — | replik yok |
| S22 | Y2→Y1 · iç motor titreşimi · düzenli nefes · R16 (klipten) | — | basınç azalır |
| S23 | Y2 · telsiz statik patlaması → R17 (klipten; yedek C02 kaydı) → sessiz tık → nefes ve havalandırma | tık sonrası sessizlik → karisim 0,8 → S24 | müzik düğme sonrası susar |
| S24 | Y1 · soluk telsiz benzeri hışırtı · tek alçak diegetik olmayan atım · R18 (klipten) · tek düşük ton | — | fade-out yok; kesmeyle biter |

```
Ortam: dış uzay çekimlerinde (S1 S3 S4 S5 S15 S19 S21 S22 S24) dış ses yok; alçak tonlar sinematik tasarım · iç hacim (S2 S18 S20 S23 kokpit; S6-S8 S10 S17 koridor; S9 S11-S13 gözlem odası) hava taşır · su altı (S14 S16) boğuk rezonans.
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi: F4 açılırsa ODA/F4_ses-tasarimcisi_<n>.md; şimdilik kaynak SAHIP_PLANI "Audio" satırları (yukarıdaki katmanlar) ve §7 ses yayı.
Model sesi (12.10.2026): her replik taşıyan parça timeline'da klip_sesi: true, klip_kazanc_db −3…−6 (klibin kendi uğultusu yatağın altında kalır); yatak her zaman kurgudan.
Vakumda ses (T13, F5 teknik B8, Fable KABUL): dış uzay kliplerinde (C01 C03 C04 C15 C19 C22 C24) klip_sesi AÇILMAZ; klibin sesi `ses` parçası olarak yalnız replik
penceresinde (giris/cikis = replik ±0,5 s, solma 0,1) yerleşir, kalan süre Y1 yatağı. Model itici/metal hareketine motor sesi koyar; −6 dB silmez.
```

<!-- 12.10.2026 sahip kararı: klipler arası keskin kesme ve kesmede komple değişen arka ses → uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md. Yatak mekân başına TEK dosya, klip sınırlarını aşar (timeline yataklar). -->
### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | dış uzay (tasarım) | C01 · C03-C05 · C15 · C19 · C21-C22 · C24 | low steady non-diegetic pressure tone with a faint continuous bed of radio static, no rhythm, no engine roar | −20 LUFS | yatak_dis.wav |
| Y2 | kapsül kokpiti | C02 · C18 · C20 · C23 | soft steady cabin ventilation hum, close dry acoustic, faint electrical bed, no rhythm | −18 LUFS | yatak_kokpit.wav |
| Y3 | istasyon koridoru | C06-C08 · C10 · C17 | low steady pressure-system ventilation hum with sparse distant water drips, industrial interior, no rhythm | −18 LUFS | yatak_koridor.wav |
| Y4 | gözlem odası | C09 · C11-C13 | the same low ventilation hum with a hollow water resonance heard through thick glass, no rhythm | −18 LUFS | yatak_gozlem.wav |
| Y5 | su altı görünüşü (C14 kamera suyun dışında, saydam alt yüzden bakar; C16 su içinde) | C14 · C16 | deep slow waterborne resonance heard from outside the water, muffled, no high frequencies, no rhythm — diegetik değil, tasarım (F5 devamlilik B17) | −20 LUFS | yatak_sualti.wav |

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

<!-- Fable taslağı plandan (12.10.2026): karışım 3 (≤ 23/4), karartma 1. Kurgucu F8'de dikiş ölçümüyle kesinleştirir. -->
| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1→Y2 çapraz 1 s; telsiz hışırtısı J 1 s | dış → kokpit; hareket üstünde (yanal kayma → itiş) |
| C02→C03 | kesme | Y2→Y1 çapraz 1 s; yön çanı J 1 s | kokpit → dış |
| C03→C04 | kesme | Y1 sürer | aynı mekân, ölçek geniş → orta |
| C04→C05 | kesme | Y1 sürer | hareket üstünde: sola kayma → temas; ölçek orta → yakın |
| C05→C06 | karartma 0,6 | mandal sesi → kısa sessizlik → Y3 J 0,5 s | plan "metal sesi, kısa sessizlik"; mekân ve zaman atlaması (içeri giriş kesmede) |
| C06→C07 | kesme | Y3 sürer | aynı koridor, ölçek geniş → ek |
| C07→C08 | kesme | Y3 sürer; alıcı statiği J 0,5 s | ek → yakın-orta |
| C08→C09 | kesme | Y3→Y4 çapraz 1,5 s; oyuk su rezonansı J | bakış kapıya → cam dışı |
| C09→C10 | kesme | Y4→Y3 çapraz 1 s | gözlem → koridor zemini |
| C10→C11 | kesme | Y3→Y4 çapraz 1 s | koridor → gözlem geniş |
| C11→C12 | kesme | Y4 sürer; statik J 0,5 s | geniş → ek |
| C12→C13 | kesme | Y4 sürer | ek → yakın-orta ¾ |
| C13→C14 | karisim 0,5 | Y4→Y5 çapraz 1,5 s | iç → su altı; zaman/mekân atlaması, "açılma" |
| C14→C15 | kesme | Y5→Y1 çapraz 1 s; atım L 1 s | su altı → dış geniş; atım sürer |
| C15→C16 | kesme | Y1→Y5 çapraz 1 s | dış → su altı yakın |
| C16→C17 | kesme | Y5→Y3 çapraz 1 s; ıslak kayma + alarm J 1 s | su altı → koridor; tehdit içeri |
| C17→C18 | kesme | Y3→Y2 çapraz 1 s; alarm L 1 s | koridor → kokpit (plan: kesmeyle) |
| C18→C19 | kesme | Y2→Y1 çapraz 1 s | kokpit → dış yakın |
| C19→C20 | kesme | Y1→Y2 çapraz 1 s | dış → kokpit ek |
| C20→C21 | kesme | klunk → ayrılma itkisi J 0,5 s | neden → sonuç, hareket üstünde |
| C21→C22 | kesme | Y1 sürer | aynı mekân, ölçek orta → geniş, açı yan → arka-üst |
| C22→C23 | kesme | Y1→Y2 çapraz 1 s | dış → kokpit |
| C23→C24 | karisim 0,8 | tık sonrası sessizlik → Y1 J; tek düşük ton | kapanış; sessizlikten okyanusa çözülme |

## 7. MÜZİK PLANI

<!-- kaynak: SAHIP_PLANI §7 "Dört dakikalık ses yayı" + "Müzik taslağı promptu" birebir. F4 besteci açılmadı; F8'de gerçek kesme noktalarıyla kesinleşir. -->
```
OKUMA        İzleyici bu filmi kozmik gerilim olarak okumalı: yardım etme kararının tuzağa dönüşmesi; korku dev bir yüz değil, cevap verilmiş bir çağrı (plan "Araştırmadan çıkan karar").
MÜZİKSİZ     00:40–00:50 (S5) temas ve kelepçe: metal sesi, kısa sessizlik · 01:50–02:00 (S12) müzik azalır, aynı ses öne çıkar · 03:40–03:50 (S23) düğme sonrası sessizlik ve nefes.
VURUŞ/SUSMA  00:00–00:30 alçak basınç tonu, radyo hışırtısı, kısa çağrı (sessiz hayranlık + tedirginlik) · 00:30–01:00 yanaşma kelepçesi ve havalandırma, ince ıslak ses ·
             01:00–02:00 enerjisiz verici üstünde çağrı; boşluk ve su dokusu; 01:50 müzik düşer · 02:00–02:40 su içindeki yapı görüldüğünde yavaş, düzensiz nabız (AI tespitlerini örtmez) ·
             02:40–03:30 metal yükü, yakın nefes, kolun tek mekanik sesi, ayrılma itişi: kısa kontrollü ritmik gerilim · 03:30–04:00 basınç azalır; 03:40 son taklit, düğme, sessizlik;
             son cümlede tek çözülmemiş düşük ton — faz 8'de gerçek kesme noktalarıyla kesinleşir.
FLOW MUSIC   faz 8: ODA/F8_besteci_<n>.md. Plan notu: kesin sahne geçişleri müzik üretimine bırakılmaz; bölümler kurguda zaman çizelgesine yerleştirilir; zafer dolu bitiş yok.
```

<!-- 12.10.2026 sahip kararı (her filmde müzik promptu §7'de): planın "Müzik taslağı promptu" birebir, F4 taslağı sayılır; F8'de besteci gerçek kesme noktalarıyla kesin sürümü altına yazar. -->
### MÜZİK PROMPTU — Flow Music'e yapıştırılır (plan taslağı, 12.10.2026)
```text
Original cinematic score for a four-minute cosmic science-fiction thriller. Restrained sub-bass pressure, sparse processed low strings, delicate metallic textures, no vocals, no recognizable theme from an existing film. Begin with quiet awe and unease, grow into a slow irregular pulse as an impossible ocean reveals a living network, intensify into short controlled rhythmic tension for an emergency separation, then fall back to near silence with one unresolved low note. Leave substantial room for radio dialogue, breathing and mechanical effects. Build editable sections with clean transitions; do not use a triumphant ending.
```
