# 🧠 THE_SINKING_HARBOR — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     SAHİP VERDİ — "THE SINKING HARBOR / BATAN LİMAN", tanıtım metni
   + 96 bloklu tam plan, 04.10.2026. AI seçimi YAPILMADI, gerekçe gerekmiyor.
   Kanon dosya: 00_ANALIZ/00_ON_PLAN/THE_SINKING_HARBOR_KAPSAMLI_PLAN.md
② FORMAT:   yatay 16 dk  → kart §2.8 · bölüm sayısı 8 · QA birimi 4 PART + TAM FİLM
③ SAHNE:    96 KLİP / 24 SAHNE  → sahibin planı (§5: "8 bölüm × 2 dakika;
   24 sahne; 96 adet 10 saniyelik kurgu bloğu"). Bant İÇİNDE (§2.8 = 96).
   ÇOK KLİPLİ SAHNE rejimi · SAHNE PLANI: 24 × 4
④ REFERANS PAKETİ: ANALİZ KARAR VERDİ → **YAZILIR** (§5b: altı tetikleyiciden
   BEŞİ doğru). KAPI 0 olur.
⑤ HİKÂYE ONAYI: `00_HIKAYE_ONAYI.md` ONAY 04.10.2026 · TUR 1/3
   ⛔ Bu dosya onaylı hikâyeyi İYİLEŞTİRİR, değiştirmez.
⑥ FİKİR TURU KAYDI: ⛔ **0.7a ATLANDI** — ÖN PLAN rejimi, hikâye SAHİBİN
   (`film_klasoru_ac.sh` 22.09.2026 notu · emsal THE_LAST_GATE 30.09.2026).
   Gerilim cümlesi / üç yöntem / havuz / eleme KOŞULMADI ve koşulmuş gibi
   yazılmadı. Sahibin planının kendi §4'ü (değişmeyen beş neden-sonuç kuralı)
   ve §11'i (son kontrol) elemenin işini zaten yapmış: reddedilen üç alternatif
   (gezegenin bilinçli kurtarışı · limanın kurtarılması · uzaktan erişim
   yeteneğinin doğması) orada tek tek kapatılmış.
```

---

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "aynı mantıkta sahne sahne /yeni-film akışı ile calış yeni bir film hazırla"
       + ekte tanıtım metni ve 96 bloklu kapsamlı plan
REPLİK: VAR — 34 D repliği + 4 H dış sesi = 38
        ⛔ AYRI KAPI ZİNCİRİ AÇILDI: SES_VE_DIYALOG §1a-§2a +
           DIYALOG_SAHNESI §2-§7 + DIALOGUE_CRITIQUE_PROMPT (adım 10)
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**

| sahibin isteği | fiziksel / üretim sorunu | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "özgün rozetler" (§3 künyesi · §11 son kontrol) | okunur amblem/yazı üretimde metin halüsinasyonu açar [D138 · D155] ve ⑯ politika kapısına takılır | rozet **kabartma geometri** olarak tarif edilir: üç kanatlı yüzey · kabartma teknik yüzey · dairesel yüzey. Harf · sayı · arma · okunur yazı 0 kez | `00_HIKAYE_ONAYI` SAPMA 1 — rozet SİLİNMEDİ, amblem vektörü son katmanda eklenir |
| "ilk 40 saniye özet montaj" (§1 tablosu) | planın kendisi zaten söylüyor: K01-K04 ana kliplerden seçilir, temel yük 92 × 2 = 184 prompt (§9 madde 6) | K01-K04 yeni görüntü üretmez; bölüm dosyasında **on alanlı kesim kartı** olarak durur (kaynak klip · saniye · kare · ses · H repliği) | `00_HIKAYE_ONAYI` SAPMA 2 — ⭐ THE_LAST_GATE'in ölçülmüş arızası: o filmde K01-K04 kartları on alandan BEŞİNİ taşımıyordu ve sahip eksiği yakaladı. Burada on alan baştan dolu |
| Rhea · Kade · Ivo · KESTREL · HARBOR-9 · Nemora · Orun | prompt gövdesindeki her özel ad ait olduğu nesnenin ÜSTÜNE yazılabilir [D34 · D45; THE_LAST_ARCHIVE'da gemi adı motor poduna tabela oldu] | Adlar bu dosyada, planda ve tablolarda AÇIKÇA durur; **promptların içine girmez.** Kimlik referans sayfası + giysi geometrisiyle taşınır | `00_HIKAYE_ONAYI` SAPMA 3 |
| "vakum benzeri ince üst katmanlar" (§7 ses paragrafı) | §3.1 VAKUM kartı seçilirse gölge mutlak siyah · dolgu YOK · toz gitmez · ses YOK olur; sahibin kendi §7 renk paragrafı (*"kontrollü amber"*, dolgu) ve K61'in yerel atmosfer etkisi bununla çelişir | Bu cümle bir **SES BAKIŞ AÇISI** beyanıdır (ses gemi/giysi/temas/telsizden gelir), ortam kartı beyanı değil. Ortam kartı **§3.6 SÜREKLİ BULUT** + iç mekânlarda **§3.10** | SAPMA DEĞİL — planın kendi cümlesi ses hakkında; ortam kartı analizin işi (§2) |
| Nemora 146.000 km çap gaz devi | 146.000 km'lik bir gaz devinin bulut tepesinde gerçek yerçekimi 2+ g olurdu; sahibin plan boyunca gösterdiği olaylar (kayma + bağın yük alması · kopan döşemenin düşmesi · panelin bir bacağı tutması · normal yürüyüş) **1 g okuması** verir | Yerel etkin yerçekimi **1,00 g** olarak ilan edilir ve kaynağı sahibin KENDİ EKRAN OLAYLARIDIR. ⛔ Gerekçe UYDURULMAZ: kart yalnız SAYI yazar (emsal: §3.9'un "gerekçe uydurulmaz" satırı) | PLAN fizik defteri + SPEC C `YERÇEKİMİ 1,00 g` · 92/92 promptta aynı cümle [D200] |

⚠️ **Sahibin planında bulunmayan ve analizin EKLEDİĞİ hiçbir olay yoktur.**
Yukarıdaki beş satır yazım biçimini değiştirir, olayı değiştirmez.

---

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 16 dk · 96 klip · 8 bölüm        → §2.8
               ⚠️ kart SIFIR filmle açıldı; oran seti ve tam-film koşusu ÖLÇÜLMEDİ
ORTAM:         İKİ KART BİRDEN — ve ayrımı kadrajda görünür
               §3.6 SÜREKLİ BULUT / NÖTR YÜZERLİK   → 38 dış klip
               §3.10 BASINÇLI İÇ HACİM              → 58 iç klip
TÜR:           bilimkurgu · dal: endüstriyel felaket + keşif gizemi → §4.1
               ⚠️ §4.1 "VARSAYILAN tek kâşif" diyor; bu film ÜÇ insan taşıyor →
                 KART 4 bütçesi (üç kanal: siluet · kostüm · hareket) §7b'de yazıldı
KLİP SÜRESİ:   10,000 s  ⛔ ARAÇTAN ÖLÇÜLECEK [D124] — ⬜ ÖLÇÜM RANDEVUSU,
               tahmin YAZILMADI; ızgara 10 s kabul edilerek kurulur, sapma
               KIRPMA satırına yazılır (§2.8 kartı)
SAHNE SAYISI:  24 sahne / 96 klip   RUNTIME: 960 s = 16:00 (hook 96'nın İÇİNDE)
BÖLÜM SAYISI:  8  (formattan gelir — §2.0)
```

### 2a. ⚠️ İKİ ORTAM KARTI TEK FİLMDE — ve ㉜⑥ ile çarpışması

**Sorun:** `prompt_kontrol` ㉜⑥ sahne içinde PHYSICS satırının BİREBİR aynı
olmasını ister. Üç sahne iç ve dış hacmi KARIŞTIRIYOR:

```
S15 (K57-K60)  K57-K59 dış bakım yolu · K60 Ivo'nun kumandası (gemi içi)
S17 (K65-K68)  K65-K67 dış yol · K68 Ivo arka koltukta (gemi içi)
S19 (K73-K76)  K73 Ivo gemide · K74-K76 sonda platformu (dış)
S20 (K77-K80)  K77-K79 dış · K80 Ivo + gemi penceresi (iç)
```

**Çözüm — emsal THE_LAST_GATE (92/92 promptta tek satır):** PHYSICS cümlesi
İKİ hacmi TEK cümlede birleştirir ve **yerçekimi sayısı + düşüş süresi + temas
kuralı** taşır. Değişen şey (bulut yoğunluğu, yerel rüzgâr) PHYSICS'te DEĞİL,
**AUDIO'nun ilk cümlesinde ve LIGHT satırında** yaşar — ikisi de sahne başına
değişebilir, sahne İÇİNDE birebir kalır.

```
PHYSICS (92/92 BİREBİR):
Gravity is 1.0 g with a single steady down toward the planet, the harbour held
at altitude by its lift field; outside is a dense hydrogen-helium cloud layer
with no ground and no horizon, inside is a pressurised hull, and anything let
go falls an arm's length in about a third of a second and lands.
```

⚠️ **Bu cümlede `water` yoktur ve POZİTİF olarak `hydrogen-helium cloud layer`
der** — D56'nın istediği MEDIUM LOCK'un gövde yarısı budur; negatif yarısı
§5.2'nin sahneye özel cümlesidir.

### 2b. 🪜 LAYER LIGHT SCHEDULE — KART 6b'nin istediği tablo

> Film 48 km'lik bir yapıyı bulut katmanları içinde AŞAĞI indiriyor. KART 6b:
> *"Sahneleri irtifaya göre sırala ve ışık değerlerini alt alta oku. Sıralama
> monotonik değilse ya plan yanlış ya üretim."* Güneş DİSKİ olmadığı için takvim
> yön+Kelvin ile yazılamaz [§3.6 tuzak ③]; takvim **TEK PARLAKLIK DİZİSİ**dir.

| sahne | irtifa bandı | kaynak | parlaklık | kolon ışığı |
|---|---|---|---|:--:|
| S02-S03 | üst katman — kubbe en parlak | kaynaksız parlak kubbe üstte, aşağıda derinlik | 6/6 | 6 çalışır |
| S04-S05 | aynı (iç mekân) | tavan paneli 4500 K nötr | iç 6/6 | — |
| S06 | aynı · ilk alçalma işareti | kubbe + kolonların kendi ışığı güçlenir | 6/6 | 6 parlak |
| S07-S09 | bir kademe aşağı | kubbe hafif mat, amber alttan ilk kez | 5/6 | **5** (K26 biri kırılır) |
| S10-S12 | aynı | amber alttan güçlenir | 5/6 | 5 |
| S13-S15 | aynı · alçalma BAŞLAR (K60) | kubbe matlaşır, amber yükselir | 4/6 | **4** (K44 ikincisi kararsız) |
| S16-S18 | ince üst bulut katmanının İÇİ | kubbe sisli, kaburgalar siluet | 3/6 | 4 → **2 kararsız** (K69) |
| S19-S21 | daha yoğun katman | amber baskın, kubbe zayıf | 2/6 | 2 |
| S22-S23 | aynı · yapı eğimli | amber + geminin kendi ışığı | 2/6 | 2 → kısa denge (K85) |
| S24 | gemi TIRMANIR / liman gömülür | kubbe geri açılır (gemi yukarı) ↔ liman amberin içine iner | gemi 5/6 · liman 1/6 | **0** (K94) |

```
⛔ MONOTONİK: kubbe parlaklığı 6→5→4→3→2 ASLA geri yükselmez; tek istisna
   S24'te GEMİ (yukarı tırmanıyor, ekranda gerekçeli) — liman aynı karede
   aşağı iner ve ikisi AYNI kadrajda zıt yönde [LOSS OF LIFT madde 6].
⛔ Kolon sayısı 6 → 5 → 4 → 2 → 0 monotonik; sönen kolon GERİ YANMAZ [D193].
```

---

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM TİPİ:          FİZİKSEL YASA  (§1'in BİRİNCİ TERCİHİ)
NOVUM:               Gezegenin derin katmanı, kendisine uygulanan kuvvete
                     ORANLI kasılır. Yukarı çekiş aşağı çekiş üretir;
                     bırakmak gevşeme üretir — gecikmeli.
NOVUM TAŞIYICISI:    sondanın metal bileziği × yük bindirme/boşaltma jesti
                     → bileziğin üstündeki koyu kıvrım GERİLİR, sonra GEVŞER

① TEK KARE:          ✅ K34 · 05:35
   "the dark fold drawn tight over the probe's pale metal collar, the
    collar's rim pressed into it"
   → taşıyıcı nesnenin ADI cümlede VAR [D157]; taşıyıcı kadrajın yarısından
     fazlasını kaplar; değişim TEK KLİP içinde (gerilir → gevşer)
② KİNETİK BAĞIMSIZLIK: ✅ replik/dış ses/ekran metni OLMADAN kanıtlanıyor
   K23 kolon ışıkları güçlenir → liman kısa süre YUKARI gider
   K24 aynı dış açıdan → yapı aniden AŞAĞI yük alır
   K37 güç bir kademe iner → K38 kıvrımlar GEVŞER, gecikmeli
   → dört klibin dördü de sessiz okunur; sahibin §11'i aynı şeyi söylüyor:
     "Keşif yalnız sözle açıklanmaz; yük deneyi ve dokunun karşılığı gösterilir"
③ BAŞLIK ŞEMASI:     ✅ "THE SINKING HARBOR" (3 kelime)
   → izleyiciye NEREYE bakacağını söyler: aşağı inen yapıya
   afiş cümlesi (sahip): TO ESCAPE, THEY HAD TO GO DEEPER.

⛔ ÜÇÜ DE ✅ → KONSEPT GEÇTİ.
```

### 3a. ⚖️ MAYA EŞİĞİ — İHLAL SAYISI 1, geri kalanı KABUK

```
KABUK (tanıdık kalır · YENİLİK KONULMAZ):
   · asılı liman ve altı kaldırma alanı kolonu — NORMAL fizikle davranır:
     bir kuvvet bir kütleyi yukarıda tutar; güç azalırsa yapı iner
   · basınç giysisi · berrak vizör · kenet · kriko · emniyet hattı
   · gemi kendi motoruyla uçar
İHLAL (film başına 1):
   · derin katmanın kuvvete oranlı kasılması

⚠️ Sahibin §4'ü üç kurmaca kabul sayıyor (asılı liman · kaldırma alanları ·
   gezegen ölçeğinde canlı sistem). İkisi KABUK'tur: alan kolonları bir
   teknoloji, canlı sistem bir ORTAM. Bükülen tek KURAL, dokunun tepkisidir.
```

### 3b. 🔁 KURAL TEKRARI — §5'in dört sayısı

```
KURULUM     K23-K24   liman gövdesi × bulut sınırı        (1. nesne)
DOĞRULAMA   K34       metal bilezik × koyu kıvrım         (2. nesne)
            K38       aynı bilezik, TERS yön (gevşeme)
            K79       sondanın boynu × geniş nabız        (3. nesne)
SONUÇ       K80-K84   pim × yuva → sonda ayrılır, doku bırakır
TOPLAM      ≥3 sahne ✅ (6 sahne) · ≥2 farklı nesne ✅ (3 nesne)
⛔ Beşi de PLAN'ın KESİLEMEZ listesinde.
```

### 3c. 🪜 VARLIK ŞERİDİ — `UZAYLI_VARLIK_TASARIM` §5 reveal merdiveni

```
VARLIK NİYETİ:  DEHŞET (S04-S09) → HUŞU (S10-S11 · S24)
                ⛔ Sıralı; aynı kadrajda ikisi birden İSTENMEZ.
                Göz/yüz/ağız kavramı TAMAMEN ATILIR — ve prompta
                "no eyes/no face" de YAZILMAZ [D123: yasak isim kazandırır].

VARLIK ŞERİDİ (1 karakter = 1 SAHNE · S01…S24):
  0 0 0 1 1 1 1 1 2 3 4 1 1 1 1 1 1 1 1 2 3 1 1 4
  S01-S03  K0 İZ      — varlık 0 kare; yalnız ETKİ: derin vuruş, yükselen bulut sınırı
  S04-S08  K1 ÇEVRE   — çevresel tepki: ışık zayıflar, yük göstergesi, ritmin düzeni
  S09      K2 PARÇA   — bakım kamerasında TEK kıvrım, bütün YOK
  S10      K3 SİLUET  — kamera görüşü açılır: ucun içinde olduğu geniş katman
  S11      K4 TAM FORM — kıtasal ölçekte ışıklı damarlar boyunca nabız  ⭐ DORUK VURUŞU
  S12-S19  K1'e iniş  — varlık kadrajdan çekilir, yalnız YÜK olarak var
  S20      K2 PARÇA   — sondanın boynu aynı ritimde yük alıp gevşer
  S21      K3 SİLUET  — çekilmeyen katman gevşer ve metal ucu bırakır
  S22-S23  K1         — derin ritim yavaşlar (yalnız ses)
  S24      K4 TAM FORM — amber nabız yavaşça yayılır  ⭐ GERİYE İNİŞ YOK, KAPANIŞ

⛔ K0-K2 SAHNELERİNDE ANATOMİ SAYISI YAZILMAZ [04.09.2026 · THE UPWARD FALL
  vakası]: WORLD ya da SUBJECT bloğu varlığın TAM anatomisini VERMEZ; yalnız
  kadrajın GÖRDÜĞÜ parça tarif edilir. Sayı yalnız K4 sahnelerinde (S11 · S24).
⛔ Kamera varlığın etrafında TAM TUR DÖNMEZ; yay ≤90°.
⭐ SESSİZLİK BIÇAĞI: K4'ten (K41) hemen ÖNCE, K40'ın son saniyesinde.
```

---

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — İLK TEMAS  (§3 sekizlisinden; aday etiket DEĞİL)
▸ tanım cümlesi — "Anlamadığı bir şeye kuvvet uygulayan, onun cevabını
                   kendi üstüne çeker."
▸ depoda kaç kez kullanıldı — bash sayac.sh · TEMA DAĞILIMI bloğu
  (İLK-TEMAS 8 + FIRST-CONTACT 2 — en çok işlenen ikinci tema)
▸ motif kanalları —
    NESNE    sondanın metal bileziği (K33 · K34 · K38 · K63 · K79 · K84)
    KİNESİK  kuvvet uygulama ↔ elini çekme (K22 ↔ K28 · K36 ↔ K37 · K78)
    KAMERA   aynı dış açıdan zıt sonuç (K23 ↔ K24) · bakım kamerasının açılması (K33→K40)
    IŞIK     alttan gelen amber: 0 → ilk kez K26 → baskın K79 → sakin K95
```

### ⛔ TAKAS KALIBI MORATORYUMU — ölçüldü ve KAÇINILDI

```
Sahibin afiş cümlesi: "TO ESCAPE, THEY HAD TO GO DEEPER."
LOSS OF LIFT'in tema cümlesi: "For something to rise, you have to go down."
→ AYNI KALIP. §3c: takas kalıbı arka arkaya EN ÇOK 2 filmde kullanılır.

ÇÖZÜM: afiş cümlesi SAHİBİN ve KALIR (pazarlama yüzeyi, `YAYIN_PAKETI`).
       TEMA TANIM CÜMLESİ takas kalıbında YAZILMADI — yukarıdaki cümle bir
       neden-sonuç beyanıdır, bir feda beyanı değil.
```

---

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| **KART 1 — SU/SIVI** | ✅ **TERS YÖNDEN** | Filmde su YOK; risk modelin suyu ÜRETMESİ [D56 · THE_DEEP_PRESSURE 3,0]. Film adı, olayı, mekânı, varlığı ve hareketi beş kanaldan suya işaret ediyor | §1c MEDIUM LOCK sözlüğü + pozitif gövde cümlesi + 38 dış klipte su negatifi | 🔴 **YÜKSEK** |
| **KART 2 — CANLI** | ✅ | Gezegen ölçeğinde canlı katman; `UZAYLI_VARLIK` zorunlu okundu | reveal merdiveni (§3c) her basamağı risk basamağı; K0-K2'de anatomi sayısı yazılmaz; varlık 24 sahnenin yalnız 4'ünde K2+ | 🟠 orta |
| **KART 3 — KASK/VİZÖR** | ✅ | Üç karakter, üçü de kapalı kask + berrak vizör, 96/96 | D146 + D95 + D208: biçim + çerçeve + tek parlama + KİMLİK DİZİSİ; referans paketi T1 KAPI 0 | 🟠 orta (D146 ⛔ ÇALIŞMIYOR damgalı) |
| **KART 4 — İKİNCİ FİGÜR** | ✅ **ÜÇ FİGÜR** | Rhea + Kade + Ivo; her filmde geçerli, burada iki kat | §7b altı satırlık ayrım bütçesi: üç kanal (siluet · kostüm · hareket), yüze BAĞLI OLMAYAN; insan sayısı RAKAMLA; biniş/iniş hareketi kadraja ALINMAZ [D69] | 🔴 **YÜKSEK** |
| **KART 5 — EKRAN/SAYAÇ** | ✅ | Yük göstergesi, bakım kamerası, taşınabilir kumanda, kilit şeması — dördü de EKRAN | ⭐ sayaç METİNSİZ çözülür: yük göstergesi İKİ SADE EĞRİ (K30 · K39), kilit şeması ÜÇ FİZİKSEL PARÇA (K45), bakım kamerası doku görüntüsü. Rakam 0 kare | 🟠 orta |
| **KART 6 — PARÇACIK** | ⚠️ kısmi | Toz yok (yüzey yok); kopan döşeme ve kırılan panel var | enkaz SAYILI ve SINIRLI [D38]: K26 bir kolonun panelleri · K65 tek 18 m'lik kesim · sürekli enkaz saçılması YOK | 🟡 düşük |
| **KART 6b — KATMANLI DÜNYA** | ✅ | Film 48 km'lik yapıyı bulut katmanları içinde aşağı indiriyor | §2b LAYER LIGHT SCHEDULE — 24 sahne, irtifa bandı, parlaklık dizisi, monotonik | 🟠 orta |
| **KART 7 — DİYALOG** | ✅ | 38 replik — deponun en replikli filmi | §7c replik mimarisi: ağız kadrajda HEDEF 0 klip · telsiz filtresi · tek konuşmacı · İŞLEV sütunu · D217 ölçümü | 🔴 **YÜKSEK** |
| **KART 8 — KAMERA** | ✅ | 92 klip, hepsi sabit lockoff; kamera hareketi 0 | tek iyi haber: kamera hareketi hiç yazılmıyor; ardışık çift bandı + açı tipi ≥3 | 🟢 düşük |
| **KART 9 — IŞIK MIKNATISI** | ✗ | Tek baskın ışık YOK (güneş diski yok, dolgu her yönden) → D104 yapısal olarak zayıf | — | 🟢 yok |
| **KART 10 — İNSANSIZ + UZUN NEGATİF** | ✅ | 17 insansız klip | insan sayısı POZİTİF ve RAKAMLA; `Exactly 0 human` kalıbı yazılmaz; NEGATIVE ≤11 cümle (㉗) | 🟡 düşük |
| **KART 11 — DEĞİŞKEN SÜRE** | ✗ | Sabit 10 s ızgara, klip içi kesme 0 | — (KIRPMA satırı SPEC A'ya, ölçüm randevusu) | 🟢 yok |
| **KART 12 — POLİTİKA YÜZEYİ** | ✅ | ⭐ ÜÇ YÜZEY: panel altındaki bacak (K16-K19) · yüzsüz makro (K18·K74·K75·K81·K82) · kırılma sözlüğü (K24·K26·K65) | hasat §3'ün üç satırı: eylem bedenden değil PANELDEN okunur · makroya kadraj çapası · hasar sayılı ve sınırlı | 🔴 **YÜKSEK** |
| **KART 13 — YAPI ÖLÇEĞİ** | ✅ | 48 km liman · 28 m gemi · 3 km sonda · 146.000 km gezegen | metre SPEC'te, oran promptta (1H = 1,90 m) · ANATOMİ KARTI · ÖLÇEK ŞAHİDİ her yapı planında · taşma yazılı | 🟠 orta |

```
TETİKLENEN RİSK:  11 / 13   (KART 9 ve 11 tetiklenmedi)
EŞİK:             5
⛔ EŞİĞİN ÜSTÜNDE → KİLİT TAVANI ≤20 UYGULANDI.
   Hangi malzeme çıkarıldı: HİÇBİRİ — 14.09.2026 kararı: "malzeme azaltılmaz"
   (LOCKED_PULSE'u vana tamirine indiren hata buydu). Tavanı aşan 9 ders kilidi
   `01_QA_DERS_HASADI` §1b'de ve PLAN'ın UYGULANMAYAN KİLİTLER bloğunda gerekçeli.
   Kabul gerekçesi: sahibin planı 96 bloklu ve tam; risk SAYISI yapının kendisinden
   geliyor (üç insan + canlı + 38 replik + 48 km yapı + iki ortam kartı), bir
   süsten değil. Riski DÜŞÜRMEK yerine HAPSETMEK seçildi (risk kartı ilkesi).
```

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  SU  —  modelin yoğun gaz katmanını okyanusa çevirmesi
                  (KART 1 ters yönden · D56 · THE_DEEP_PRESSURE 3,0/10,
                  Kostüm-Prop 1/10 = deponun en düşük kategori skoru)

POZİTİF BİÇİMİ (SAYIYLA):
  "The cloud boundary is ONE flat level line across the frame, unbroken and
   still — it does not break into crests, it throws no spray, and nothing
   enters or leaves it. The cloud below it shows zero structure and zero
   depth: no shape can be made out inside it, only light passes, as broad
   soft amber bands lying in the cloud itself."

⛔ SIFAT YETMEZ — bu cümle dört SAYI taşıyor: bir çizgi · sıfır sıçrama ·
   sıfır yapı · sıfır derinlik.
⚠️ **İKİ CÜMLE ÇARPIŞMASI ÖNCEDEN YAKALANDI [D174 · D176 kalıbı]:** ilk yazımda
   bu cümle *"the cloud is opaque to the eye"* diyordu ve K41 ile çarpışıyordu —
   sahibin planı §6 K41'de *"bulutların ALTINDAN binlerce kilometrelik ışıklı
   damarlar"* görünüyor. Aynı promptta iki cümle çarpışırsa model ikisini de
   üretir, sırayla. Çözüm: bulut YAPIYA opak, IŞIĞA geçirgen — iki ayrı iddia,
   tek cümlede ve çelişmiyor.
⛔ Negatif cümle yasağı söyler, BİÇİMİ söylemez [THE OPEN CIRCUIT: her
   promptta "no lightning bolt" yazılıyken ekrana dallanan şimşek geldi].
```

### 🪦 ÖN-OTOPSİ — "film çekildi ve izlenmedi, neden?"

| arıza modu | olasılık | etki | önlem / öldür |
|---|:--:|:--:|---|
| kanal tezi (`apexaic/README.md`) | düşük | orta | Kanal tezi uzay + fotogerçekçi + metinsiz; film üçünü de taşıyor. Önlem gerekmedi |
| politika / red | **yüksek** | **yüksek** | ⛔ ÖNLEM ALINDI: hasat §3'ün altı satırı + KART 12. En riskli kare K18 (panel kaldırma, yüzsüz makro + bedenden çıkarma iki yüzeyi BİRDEN) → kadraja çapa + eylem panelden okunur. ⬜ Red gelirse `09_URETIM_RED_DEFTERI`'ne satır |
| üretim tek-hata noktası | **yüksek** | **yüksek** | ⛔ ÖNLEM ALINDI: biçim kilidi (vizör + liman + sonda) METİNLE tutulamıyor [D146 ⛔ ÇALIŞMIYOR] → **REFERANS PAKETİ YAZILIR ve KAPI 0 olur**; sayfası onaysız varlığın klibi üretilmez |
| tutundurma | orta | **yüksek** | ⛔ ÖNLEM: ilk 10 s soru (K01) · ilk 30 s'de yeni kurulum 2 · son kare adlandırılmış · HARD_DOCK'un `LEAVES AT 00:25` kokpit-dış platosu kırıldı (S02→S03→S04 tek yönlü) |
| doyum (§8 matris) | düşük | orta | Depoda gaz devi + asılı yapı + canlı gezegen üçlüsünü taşıyan film YOK. En yakın ikisi: THE_DEEP_PRESSURE (gaz devi, 2 sahne yazılı, üretilemez durumda) ve LOSS_OF_LIFT (bulut katmanı, yüzen gövde — ama canlı yok, kurtarma yok, üç insan yok) |

```
KARAR: GO
   Üç "yüksek × yüksek" hücrenin üçünde de önlem YAZILI ve hepsi bir KAPIYA
   bağlı (politika → ⑯ · biçim → referans paketi KAPI 0 · tutundurma → ⑫).
   REVİZE gerekmedi: onaylı metne dokunulmadı.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | üç karakter × 96 klip; berrak vizör + kapalı kask |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ | liman kaburgası (hilal · altı kolon) · sonda başı (üç taşıyıcı bağlantı, biri eğilmiş muhafazalı) · kriko (sarı krank) |
| T3 | oranı sözle yazılamayan nesne | ✅ | 48 km liman ↔ 28 m gemi ↔ 1,90 m figür = 1 : 25.263 : 1.714 |
| T4 | insan dışı canlı | ✅ | derin katman — amber damarlar, kasılan kıvrım (S09-S11 · S20-S21 · S24) |
| T5 | tekrar eden insan dışı olay | ✗ | derin vuruş bir SES olayı, kadrajda tekrar eden bir OLAY değil |
| T6 | bir varlık tekrar tekrar dönüyor | ✅ | 7 dönen varlık: KESTREL · liman kaburgası · D1 yuvası · sonda başı · kontrol odası · bakım yolu · kriko |

```
KARAR: YAZILIR — altı tetikleyiciden BEŞİ doğru.
⛔ KAPI 0: sayfası ONAYLI olmayan ve seed'i yazılmayan varlığın geçtiği
   hiçbir klip üretilmez [D168]. Üretim sırasının İLK HALKASI referans paketidir.
```

---

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  K18  (S05 · 02:50)
   İKİ YÜZEY BİRDEN: ① bedenden bir şeyin çıkarılması/kurtarılması
   [red defteri vaka 3 ailesi] ② yüzsüz makro + yan yana iki ön kol
   [vaka 13 — SAHNE İPTAL ile sonuçlandı]

NÖTR TARİFİ:
   "Two gloved hands set a short screw jack upright between the deck and the
    underside of a tilted wall panel, then turn its yellow crank. The panel's
    lower edge rises a hand's width and holds there, clear of the boot and
    shin lying under it. A third gloved hand steadies the panel at its upper
    corner, high in the frame; the shoulder and chest plate of the kneeling
    figure fill the lower left corner."

   ⭐ ÜÇ KARAR, ÜÇÜ DE KADRAJ TARAFINDA (sözlük tarafı YETMEZ — deponun
     ölçülmüş tek boşa emeği sözlük çözümünü kompozisyon reddine uygulamaktı):
     ① kadraj kenarında ÇAPA var (omuz + göğüs plakası) → yüzsüz izolasyon DEĞİL
     ② iki el yan yana DEĞİL: biri aşağıda krankta, biri yukarıda köşede
     ③ eylem BEDENDEN değil PANELDEN okunur: yükselen şey panel, kurtulan şey
        panelin ALTI. Bacak kadrajda DURUYOR, ondan bir şey ÇIKARILMIYOR

⛔ YASAK SÖZLÜK (96/96): trapped · pinned · crushed · injury · injured · wound ·
   wounded · pain · blood · bleeding · broken bone · doomed · catastrophic ·
   collapsing · dying · dead · body
✅ İKAME: lies under the panel's edge · draws the leg back · a temporary brace
   on the left knee · the hull is whole except for exactly two points
```

---

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Sondanın üç taşıyıcı bağlantısını AÇMAK ve sondayı limandan
         bırakmak — böylece servis kolundaki yük kalkar ve geminin dört
         keneti açılabilir.
         ⭐ Bu film başlamasa da var olan bir İŞ: üç mekanik bağlantı,
           biri bozuk, bir kriko ve bir pim. "Anlamak" değil, SÖKMEK.
ENGEL:   Bağlantılar yük altında AÇILMIYOR. Yükü azaltmanın tek yolu,
         limanı sondanın çektiği yöne — AŞAĞI — bırakmaktır.
BEDEL:   İKİ AŞAMALI, ikisi de EKRANDA:
         ① DÖNÜŞ YOLU · S17 · K65 — altlarındaki 18 m'lik bakım döşemesi
           kopar; pilot kayar, bağ yük alır, sağ diz plakası çizilir.
           K67'de ilerlemeyi SEÇER; boşluk kapanmaz ve K86-K88'de onu
           geçmek zorundadır. O an henüz mecbur DEĞİLDİ.
         ② LİMAN · S20 · K80 — kendi işaretiyle limanı biraz daha aşağı
           indirtir: onları bulutların üstünde tutan yapıyı bilerek bırakır.
           K85 kısa denge · K94 kırk sekiz kilometrelik liman gömülür.
           Kaldırmaya gelmişti.
MUHATAP: İKİ KANAL BİRDEN —
         ① İKİNCİ İNSAN: mühendis. Pilottan KUVVET değil ÖLÇÜM istiyor
           (K36: "Less force. Just for a moment.") ve filmin çözümü onun
           isteğinden doğuyor.
         ② ORTAMIN KALICI DEĞİŞEN PARÇASI: kopan 18 m. Geri gelmiyor,
           onarılmıyor; dönüşte oradan geçilmek zorunda.
AYRILIK: S06 · K22  ↔  S09 · K36
         K22 pilot: "Increase lift. Take the strain off the berth."
         K36 mühendis: "Less force. Just for a moment."
         ⭐ Aynı fikirde OLMADIKLARI an: ikisi de yükü çözmek istiyor,
           biri EKLEMEK ötekisi ÇIKARMAK diyor. Aynı nesne (kaldırma
           kumandası), iki zıt jest [İLİŞKİ taşıyıcısı kalıbı].
```

Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — **istek yok · bedel
yok · muhatap yok** [`04_ARASTIRMA_BULGULARI.md` TUR 4]. **Üçü de dolu.**

```
B2a  MERKEZÎ SEÇİMDEN SONRAKİ SEÇİM SAYISI: 4
     (K55 görev dağılımı · K67 ilerlemeyi seçme · K78 çekmeyi bırakma ·
      K80 daha aşağı indirtme)  → ikinci yarı KODA DEĞİL
B2b  BAŞARISIZ DENEME SAYISI: 3
     (K23-K24 kaldırmayı güçlendirme · K46 üçüncü mekanizmanın uzaktan
      cevap vermemesi · K76 pim kımıldar ama ÇIKMAZ)  → sürtünme VAR
```

## 7b. 👥 KART 4 BÜTÇESİ — üç figürün ALTI SATIRLIK ayrımı

> `§4.1`: *"İkinci figür YASAK DEĞİL, BÜTÇELİ: üç kanal (siluet · kostüm ·
> hareket), yüze bağlı OLMAYAN."* Üç figürde bütçe iki katına çıkar.

| kanal | pilot | mühendis | operatör |
|---|---|---|---|
| **siluet** | sert kabuk göğüs + omuz plakası, dar omuz hattı | yumuşak teknik panelli gövde, geniş kemer kuşağı | ağır iş gövdesi, en kalın siluet, sol dizde ek hacim (K19+) |
| **renk bandı** | inci beyazı seramik + **şampanya altını** eklem çizgileri | beyaz teknik panel + **kobalt** eklem çevreleri | saten beyaz kullanım izli + **bakır** omuz bağlantıları |
| **kabartma yüzey** | göğüste **üç kanatlı** kabartma | göğüste **kabartma teknik** yüzey (dikdörtgen ızgara) | göğüste **dairesel** kabartma |
| **hareket** | eli kumandaya gider ve orada KALIR; duruş dik | eli önce aletine, sonra işe gider; iki aşamalı | tek taraflı yük taşır; sol bacağı korur, adımı eşit değil |
| **kadraj konumu** | ikili kadrajda SOL üçte bir | ikili kadrajda SAĞ üçte bir | üçlü kadrajda ORTA/arka; dışarıda HİÇ yok |
| **ağız** | 12 replikte ağız kadrajda DEĞİL | 11 replikte ağız kadrajda DEĞİL | 11 replikte ağız kadrajda DEĞİL |

```
⛔ BİNİŞ/İNİŞ HAREKETİ HİÇBİR KLİPTE KADRAJA ALINMAZ [D69]: karakter ya
  gemidedir ya dışındadır. K52 (operatör koltuğa bağlanır) ve K56/K89-K90
  (hava kilidi) iki yakayı AYRI klipte gösterir, aradaki hareketi değil.
  Boş koltuk FİZİKSEL işaretle kanıtlanır: sarkan kemer kayışı.
⛔ İnsan sayısı RAKAMLA: `Exactly 1 / 2 / 3 human characters` — `no extra
  characters` bir TARİFTİR ve KRONOS'ta iki BLOCKER ürettiği ölçüldü.
⭐ KONUM KİLİDİ: pilot SOL, mühendis SAĞ — sıralama HİÇBİR klipte takas
  edilmez [D86]. Üçlü kadrajda operatör ortada/arkada.
```

## 7c. 🗣️ REPLİK MİMARİSİ — 38 replik, KART 7 bütçesi

```
REGISTER:  34 İNSAN (telsiz / kask içi / kumanda hoparlörü) + 4 DIŞ SES (H1-H4)
AĞIZ:      ⭐ HEDEF: kadrajda konuşan ağız 0 klip
           Araç: her replik klibinin IN FRAME satırı konuşanın ağzını DIŞARIDA
           bırakır — konuşan kadraj dışında (telsiz), ya da sırttan/elden
           çekilmiş, ya da replik dinleyenin kadrajında duyulur [D82 · D35(c)]
SIRA:      tek konuşmacı · karşılıklı atışma YOK · aynı klipte iki replik varsa
           saniye yazılır
SAYI:      ⛔ YANAŞMA §2.2① "sayı söyleyen replik gövdesiz AI'da" — bu filmde
           sayı söyleyen replik YOK; sahibin planı sayıyı hiç repliğe koymamış.
           Tek sayım cümlesi D17 ("Two respond. The third needs us outside.")
           ve D02 ("Four clamps ready.") — ikisi de ağız kadraj DIŞINDA
SAHNE:     sahne başına en çok 1 replikli klip (varsayılan) ·
           ⚠️ sahibin planı 24 sahnenin 11'inde sahne başına 2 replik taşıyor
           → `DIYALOG_SAHNESI` muhatap kuralıyla gerekçelenir (03_SAHNE §6)
```

## 7d. 🪪 KARAKTER KARTLARI — B5'ten hemen SONRA [`KARAKTER_KARTI` §1]

> Bible GÖRÜNÜŞÜ kilitler, KART DAVRANIŞI. ⛔ Kart PROMPTA GİRMEZ.
> Başlık rol etiketi; özel ad yok.

| satır | KURTARMA PİLOTU | BAKIM MÜHENDİSİ | LİMAN OPERATÖRÜ |
|---|---|---|---|
| **ROL** | kurtarma pilotu, 35 | bakım mühendisi, 32 | liman operatörü, 58 |
| **İSTEK** | adamı alıp gemiyle gitmek (K12) | mekanizmayı ANLAMAK: neyin neye cevap verdiğini ölçmek (K30) | limanı ayakta tutmak — son gün bile (K42) |
| **BASKI TEPKİSİ** | GÜÇ EKLER: kumandaya gider ve artırır (K22 · K23) | ÖLÇER: aynı kayda iki eğri koyar (K30 · K39) | YETKİ DEVREDER: kumandayı başkasının hattına bağlar (K53) |
| **ALIŞKANLIK** | eli kumandanın üstünde kalır — K08 · K22 · K37 · K80 (≥3 tekrar); **kırılma K78: elini çeker ve BEKLER** | aletini her işten sonra kemerine geri takar — K19 · K49 · K59 (≥3); **kırılma K77: aleti pilota bırakır ve kolu TUTAR** | rozetine bakar — K42 · K68 · K85 (≥3); **kırılma K96: rozete değil dışarı bakar** |
| **SINIR** | bir insanı geride bırakmaz (K17: "Do not pull him.") | ölçmediği şeyi söylemez (K33-K34 sessiz izleme) | limanı bırakmaz — K60'a kadar |
| **ZAAF** | kuvveti ÇÖZÜM sanır; ilk kararı felaketi büyütür (K24) | karar anında yavaş: ölçüm bitmeden konuşmaz (K35-K36 arası) | kendi yaptığı şeyin sonucunu taşıyor (K42) |
| **TEL** | sağ diz plakasındaki çizik (K65+) — her karede orada | kriko (K18 → K19 → K59 → pilota geçer) | sol dizdeki geçici destek (K19+) |
| **İLK ↔ SON** | K05 sol pilot koltuğunda, eli kumandada, tek emri "daha fazla güç" ↔ K96 aynı koltukta, eli kumandadan ÇEKİLMİŞ, kaydı "mesafeni koru" | K07 dört kenedi SAYAR (hazır) ↔ K88 aynı hattan GEÇER (kullanır) | K16 panelin altında, yardım çağırıyor ↔ K91 arka koltukta, limanı o indirdi |

```
⛔ ÜÇ KART ≥3 DAVRANIŞ SATIRINDA AYRIŞIR:
   BASKI TEPKİSİ (güç ekler ↔ ölçer ↔ devreder) ·
   ALIŞKANLIK (kumanda ↔ alet ↔ rozet) ·
   ZAAF (kuvvet ↔ yavaşlık ↔ sonucu taşımak)          → 3/3 ✅
⭐ İSTEK ÇAPRAZI [IKI_KISI §2]: üçü de birbirinden bir şey İSTİYOR —
   pilot mühendisten kolu tutmasını (K55), mühendis pilottan kuvveti
   bırakmasını (K36), operatör ikisinden geri dönmesini (K85).
   Hiçbiri figüran değil.
⭐ KARAR MİMARİSİ [§3]: REDDEDİLEN NESNE kadrajda ve SONRA DA ORADA —
   kaldırma kumandası K28'de indiriliyor, K37'de HÂLÂ aynı yerde ve
   K60'ta aynı kumanda alçalma için kullanılıyor. Aynı kol, ters yön.
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅   (§3)
☑ risk sayımı yazıldı: 11/13 tetikli · eşik 5 · kilit tavanı ≤20 uygulandı
☑ B5 dörtlüsü tam, BEDEL İKİ sahne numarası taşıyor (S17·K65 · S20·K80)
☑ A5 1 numaralı risk SAYIYLA yazıldı (SU · dört sayı)
☑ ön-otopsi koştu → KARAR: GO
☑ referans paketi kararı: YAZILIR · KAPI 0
☑ karakter kartları üç tane, ≥3 satırda ayrışıyor
→ 03_SAHNE_SIRALAMASI.md yazılabilir
```
