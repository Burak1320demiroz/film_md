# 🧠 THE_HARD_DOCK — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.
> **Revizyon 11.09.2026 (kart P koşusundan sonra):** 1.5 rad/s kilidi fizikle ve kendi
> A5 satırıyla çelişiyordu; "çelik hat/fırlatıcı" politika riskini taşıyordu; vizör kararı
> D5/D79/D95/D146 ile çelişiyordu. Üçü de burada düzeltildi, gerekçeleri yazıldı.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     Güneş gibi yanan bir gezegenin yörüngesinde hasar almış uzay üssüne gemisiyle
            bağlanmaya çalışan astronot; AI sesi var. (sahip verdi)
② FORMAT:   yatay 3-5 dk (240 s) → §2.3 kartı · bölüm sayısı 2 (BOLUM_1 S01-S12 · BOLUM_2 S13-S24)
③ SAHNE:    24 sahne × 10 s = 240 s — sahip 24 dedi; format varsayılanı 25 (hook 9 s + 24).
            Hook ayrı sahne değil, S01'in kendisi. Band (3-5 dk) içi; PLAN §BİLİNÇLİ SAPMALAR ②.
④ REFERANS PAKETİ: YAZILSIN — T1 (kask) · T2 (kask geometrisi + halka/dikmeler) · T3 (istasyon oranı) · T6
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "güneşgibi yanan bir gezegenin yörüngesinde hazar almış bir uzay üssüne kendi uzay gemisis
        ile bağlanmaaya calışan bir astaranot ai seside olsun"
REPLİK: var — gemi bilgisayarı MIRA, akuzmatik, İngilizce, MACHINE register; insan repliği 0
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "Güneş gibi yanan gezegen" | gezegen füzyon yapmaz | volkanik gezegen: ergimiş yüzey, siyah kabuk + turuncu çatlak ağı; yüzeyin ışığı gerçek bir ikinci kaynaktır | "yanan" görünüm fiziksel: ergimiş yüzey + koronal akı |
| "hasar almış üsse bağlanmak" | hasarlı istasyon serbest yalpalar; yumuşak kenet için portun kendi mandalları gerekir, onlar bükük | SERT KENET: gemi kendi yaylı halkasını nominalin 5 katı hızla porta sürer, dikmeler dibe vurur, kilit geri alınamaz | novum + bedel aynı nesnede (halka) |
| yalpalama "ne kadar" | ilk taslak 1.5 rad/s yazdı = 4 s'de bir tur, dev yapıda kenet imkânsız; A5 satırı "6 s'de 45°" diyordu — ikisi çelişik | 48 s'de bir tam salınım (nutasyon konisi); port her salınımda ~6 s hizada | 45°/6 s = 7,5°/s ≈ 0,13 rad/s — A5 ile tutarlı, 10 s klipte ~75° görünür hareket |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 3-5 dk (240 s) → §2.3 kartı
ORTAM:         uzay §3.1 vakum kartı → dış ses 0 · gölge mutlak siyah · dolgu 0 · egzoz keskin koni ·
               lens KÜRESEL (anamorfik YASAK — ilk taslağın Camera Bible'ı anamorfik yazmıştı, silindi)
               + §3.10 kokpit iç hacmi: basınçlı kabin ama giysi mühürlü (kask takvimi 24/24 kapalı)
TÜR:           bilimkurgu · sert bilimkurgu → §4.1 kilitleri: vizör kalıcılığı D5 (TAM ŞEFFAF) ·
               gemi ölçek D32 · sıfır-g mikro hareket D23 · karakter: tek kâşif + AI sesi (varsayılan)
KLİP SÜRESİ:   10 s (8 s üret + 2 s uzat) — ⬜ ARAÇTAN ÖLÇÜLECEK [D124] ilk test klibinde
SAHNE SAYISI:  24    RUNTIME: 04:00 (240 s)
BÖLÜM SAYISI:  2    (BOLUM_1 S01-S12 · BOLUM_2 S13-S24)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Yalpalayan istasyona yumuşak kenet imkânsızdır; tek yol geminin yaylı
                     kenetlenme halkasını nominal hızın beş katıyla porta sürmektir — dört dikme
                     dibe vurur, halka bükülür ve kilit GERİ ALINAMAZ.
NOVUM TAŞIYICISI:    dört dikmeli kenetlenme halkası × nominalin 5 katı hızla porta sürülme →
                     dikmeler çöker, gemi bir daha ayrılamaz
① TEK KARE:          S23 · 0,0 s — dört DİKME çökük, HALKA yakası bükük, gemi portta hareketsiz,
                     arkada gezegen kayıyor (taşıyıcı nesnenin adı karede [D157]) ✅
② KİNETİK BAĞIMSIZLIK: S22'de dört dikme tek harekette sonuna kadar çöker ve gemi bir daha
                     kımıldamaz; S23'te arka plan kayarken gemi porta göre sabit — replik/ekran metni
                     olmadan okunur ✅
③ BAŞLIK ŞEMASI:     THE HARD DOCK — 3 kelime ≤ 5; "sert kenet" terimin kendisi ✅
⛔ Üçü de ✅ → konsept KABUL.
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — İNSAN-MAKİNE
▸ tanım cümlesi — hayatta kalma optimumunu hesaplayan makine ile bedeli göze alan insan
  sorumluluğu arasındaki çatışma: makine "dön" der, insan kalır.
▸ depoda kaç kez kullanıldı — bash sayac.sh 🎭 bloğu (sayı buraya yazılmaz)
▸ motif kanalları — makinenin her repliği bir SAYI (48 s · %50 · 6 s · %0 · 90 s) · insanın her
  cevabı bir JEST (iki tık · el korumaya · eller bırakır) · dört lamba (makinenin son sözü: yanık)
▸ motif sahneleri — S03 · S06 · S10 · S15 · S17 · S19 · S24
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| R1 yalpalama / yanaşma | Evet | serbest salınan istasyon, iki gövde | sayıyla: 48 s periyot · 6 s pencere · 0,1 / 0,5 m/s · V3 yalnız S06 · doruk port-kilitli (D104) | düşük |
| R2 kask / vizör | Evet | kasklı tek insan, 14 sahnede kadrajda | TEK nitelik: berrak düz panel + görünür çerçeve + üç işaret (D95) + referans R1 p4 · sırt pozitif (D139) | orta (D146: geometri metinle tutmuyor → R1 zorunlu) |
| R3 orbital ışık | Evet | vakum, tek güneş | güneş istasyonun arkasında, eksenin ~30° üstünde, kadraj dışı; kurulum başına sabit; 24/24 aynı [D201] | düşük |
| R4 sayaç / ekran | Evet | "AI uyarısı, telemetri" isteği | ekran 0 · ibre 0 · yazı 0; bilgi kanalı: 4 lamba (sayılabilir) + pencere geometrisi + makine sesi [D50 · A1] | düşük |
| R5 diyalog | Evet | AI sesi | 8 replik, hepsi MACHINE, akuzmatik; ağız hiç konuşmaz (lip-sync riski yapısal 0) | düşük |
| R6 temas / çarpışma politikası | Evet | "impact capture" | "seats · struts compress to their stops · settles · no bounce"; çarpışma/parça/kıvılcım kelimesi 0 | orta (kompozisyon ekseni — S22 insan gözüyle bakılır) |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR [D192]

```
1 NUMARALI RİSK:  istasyonun salınımı ve pencerenin kaçması (modelin refleksi: istasyonu SABİT çizmek
                  ya da hızlanan/yavaşlayan, "nefes alan" bir hareket)
POZİTİF BİÇİMİ:   "The station wobbles at one constant rate — one full cycle every forty-eight seconds —
                  never speeding up, never slowing, never stopping; over the ten seconds the collar end
                  sweeps about a fifth of a full circle." — her dış promptta birebir.
                  Pencere: S05'te port yüzü 4,0-6,0 s arasında TAM KARŞIYA bakar, sonra kayar (görsel kanıt).
```

```
TETİKLENEN RİSK:  6 / 5 — eşiğin ÜSTÜNDE. MALZEME AZALTILDI (ilk taslağa göre):
  · fırlatıcı/çelik hat sahnesi SİLİNDİ (politika + ikinci mekanizma)
  · "kırık kol" sahnesi SİLİNDİ (gövde hasarı — hiç kurulmamış, politika)
  · ekran/telemetri/CRT SİLİNDİ (A1 çelişkisi) → 4 lamba
  · ikinci insan yok, EVA yok, kasksız sahne yok, su/canlı/toz yok
  Kalan 6 kartın 5'i SAYIYLA kilitli; tek tarif riski R6'nın kompozisyon ekseni (rubrik 3c).
EŞİK:             5
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | Evet | A01 pilot (S02-S24) |
| T2 | biçim kilidi METİNLE tutulmayan varlık | Evet | kask paneli (D146 üç vaka) · halka + dört dikme (sayı ve çökme durumu) |
| T3 | oranı sözle yazılamayan nesne | Evet | istasyon (gemi/istasyon 1/20 — V3 tek sahne, S06) |
| T4 | insan dışı canlı | Hayır | — |
| T5 | tekrar eden insan dışı olay | Hayır | — |
| T6 | bir varlık tekrar tekrar dönüyor | Evet | THE_AMBER_LATTICE: istasyon panelleri boyut değiştirdi |

```
KARAR: YAZILIR — THE_HARD_DOCK_REFERANS_PAKETI.md (R1 pilot · R2 gemi burnu K0/K1 · R3 yaka · R4 kokpit).
⛔ KAPI 0: sayfası ONAYLI olmayan ve seed'i yazılmayan varlığın geçtiği hiçbir sahne üretilmez [D168].
   Bugün ONAYLI sayfa 0 — üretim R1'den başlar.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S22 · 6,0 s — temas ("çarpışma" okunma riski)
NÖTR TARİFİ:         geminin yuvarlak halkası sekizgen yakaya oturur; dört yaylı dikme tek harekette
                     sonuna kadar kısalır; gövde bir el genişliği oturur ve durur — sekme yok, parça yok,
                     kıvılcım yok, alev yok. Kelime yasağı yazılmaz; pozitif tarif yazılır [D123].
İKİNCİ KARE:         S10/S19 el makrosu — yüz yok + uzuv + makro (rubrik 3c üçlüsü). Önlem: kamera
                     nesne hizasında (yandan, kalça yüksekliği), tepeden değil; parçalar ard arda
                     derinlikte (kapak → eldiven → bar); eldiven tam kapalı, deri 0.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   kenetlenip röle taşıyıcısını geri getirmek — film başlamadan var olan İŞ (S02: eller kumandada)
ENGEL:   48 s'lik salınım + 6 s'lik pencere + sensör güveninin %50'den %0'a düşmesi
BEDEL:   sert kenet halkayı geri alınamaz kilitler — gemi bir daha ayrılamaz, dönüş yakıtı işe yaramaz ·
         GÖRÜLDÜĞÜ sahne S22 (dikmeler çöker) · ADI KONDUĞU sahne S24 ("Release struts destroyed.")
MUHATAP: MIRA — gemi bilgisayarı, akuzmatik; film boyunca bedensiz (hoparlör; ekran/ağız yok)
AYRILIK: S17 — makine "Abort approach" der; S18 tereddüt, S19 karar (iptal barı reddedilir, kadrajda kalır)
```

Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — **istek yok · bedel yok · muhatap yok**
[`04_ARASTIRMA_BULGULARI.md` TUR 4]. Üçü de sahne numarasıyla bağlı.

## 8. 👤 KARAKTER KARTI — PLAN'a taşındı (`THE_HARD_DOCK_PLAN.md` §KARAKTER KARTI)

```
ROL pilot/röle teknisyeni (S02) · İSTEK kenet (S02·S08) · BASKI TEPKİSİ KONTROL EDER (S08·S10·S18) ·
ALIŞKANLIK iki tık (S02·S08·S10 → S19'da kırılır) · SINIR röleyi ölü bırakmaz (S17) ·
ZAAF omuz hattı S12'den S20'ye yüksek kalır · TEL baş kilitlenir, yalnız gözler (S09·S11·S20) ·
İLK↔SON eller kumandada ↔ eller uylukta (S02↔S24)
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅
☑ risk sayımı yazıldı (6/5 → malzeme azaltıldı, gerekçesi yazılı) ve eşik kararı verildi
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S22 görülür · S24 adı konur)
☑ karakter kartı sekiz satır, her satırda sahne numarası
→ 03_SAHNE_SIRALAMASI.md yazılabilir
```
