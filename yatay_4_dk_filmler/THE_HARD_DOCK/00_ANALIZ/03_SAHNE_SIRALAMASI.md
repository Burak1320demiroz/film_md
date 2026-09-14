# 🎞️ THE_HARD_DOCK — SAHNE SIRALAMASI

> **Bu dosya sıranın TÜRETİLDİĞİ ve DENETLENDİĞİ yerdir.** Sonuç `THE_HARD_DOCK_PLAN.md`
> §SAHNE HARİTASI'na taşınır — orası sonucu taşır, burası hesabı.
> **Revizyon 11.09.2026:** ilk sıralama (A A B B A B C C C D D C …) kümeleri işaretsiz
> yazmıştı, dönüş oranını %63 ilan ediyordu (gerçek hesap yapılmamıştı), S13-S24 olayları
> S01-S12'nin kopyasıydı ve "çelik hat / kırık kol" sahneleri politika riski taşıyordu.
> Aşağıdaki dizi sıfırdan türetildi ve `prompt_kontrol.py` klasör modunda GO aldı.

---

## 1. 🥁 VURUŞ TABLOSU — sahne dağıtılmadan ÖNCE (`SENARYO_VE_VIRAL_KAMERA` §2)

| # | vuruş | % | hangi sahnede | boşsa gerekçe |
|---|---|---|---|---|
| 1 | S0 anomali — yalpalayan istasyon | 4% | S01 | |
| 2 | ortam / tehdit yükselişi — pencere, röle kaybı, oran | 17% | S02-S06 | |
| 3 | birinci manevra — manuel yanaşma başlar | 33% | S07-S10 | |
| 4 | orta nokta / kriz — pencere kaçar, iptal | 50% | S11-S12 | |
| 5 | ikinci kriz — sensör sıfır, port hasarı görülür | 67% | S13-S16 | |
| 6 | ayrılık / tırmanış — abort, tereddüt, karar | 79% | S17-S19 | |
| 7 | doruk — ikinci yanaşma ve sert kenet | 92% | S20-S22 | |
| 8 | çözülüş / kafiye — tek kare + eller bırakır | 100% | S23-S24 | |

```
HOOK TİPİ:        ANOMALİ REVEAL — burun kamerasından yalpalayan dev istasyon
S0 SORUSU:        "Bu şeye nasıl kenetlenilir?"
S1 İKİNCİ BİLGİ:  makine sayıyı söyler (48 s); pencerede kopan panel geçer
İLK 2 SN SESİ:    telsiz taşıyıcı hışırtısı + iki tonlu kabin uyarısı (2 s'de bir)
AÇIŞ↔KAPANIŞ:     KAFİYE · S02 ↔ S24 aynı B kurulumu (pencere: dönen istasyon ↔ sabit port; eller: kumandada ↔ uylukta)
```

## 2. 🗺️ SIRALAMA — 24 sahne

> Ölçek merdiveni EWS-WS-MS-CU-ECU. Harf → ölçek: A WS · B MS · C CU · D ECU · E EWS · F EWS · G WS.
> Ardışık farklı her çift TAM 1 kademe (şok bandı 0 kez); aynı harf yalnız işaretli küme.

| S | başlık | olay (tek cümle) | vuruş | B5 satırı | kurulum | lens · ölçek · açı tipi | palet | ses | şerit | ⭐VİRAL |
|---|---|---|---|---|:--:|---|---|---|:--:|:--:|
| S01 | Yalpalayan istasyon | Burun kamerası: istasyon önümüzde, port ucu geniş bir daire çizer | hook | kurulum | A | 32mm · WS · göz hizası frontal | turuncu/siyah | taşıyıcı + uyarı tonu | – | ⭐ |
| S02 | Kumandalar | OTS: pencerede istasyon; kopan panel pencereyi geçer; MIRA #1 | kurulum | İSTEK | B | 35mm · MS · OTS | kabin koyu/turuncu | MIRA #1 | G | |
| S03 | Röle kaybı | Yüz: MIRA #2; gözler konsola iner, çene sıkılır | yükseliş | İSTEK | C | 50mm · CU · alt açı | beyaz kask/koyu | MIRA #2 | R | |
| S04 | Nefes | OTS dönüş: istasyon dönmüş; iki tık; omuz kalkar-iner | yükseliş | — | B ↩S02 | (B) | kabin | fan + nefes | S | |
| S05 | Pencere mekaniği | Burun: port yüzü 4-6 s tam karşıya bakar, sonra kayar | yükseliş | ENGEL | A ↩S01 | (A) | turuncu/siyah | taşıyıcı | – | |
| S06 | Oran karesi V3 | İki gövde, gemi 1/20, burun sağa; MIRA #3 | yükseliş | ENGEL | E | 32mm · EWS · üst açı | gri/turuncu | MIRA #3 (telsiz) | – | |
| S07 | Halka | Burun: port üçte bir; alt kenarda halka + iki dikme UZUN | manevra | İSTEK | A ↩S05 | (A) | turuncu/siyah | taşıyıcı | – | |
| S08 | Manuel yanaşma | OTS: baş kola, iki tık, T-kol bir parmak ileri | manevra | İSTEK | B ↩S04 | (B) | kabin | fan | G | |
| S09 | Baş kilitlenir | Yüz: nefes sığ, 5,0 s baş kilitlenir, gözler | manevra | İSTEK | C ↩S03 | (C) | kask/koyu | nefes | G | |
| S10 | Altı saniye | El ECU: T-kol, KAPALI kapak, iptal barı; MIRA #4; iki tık, itiş | manevra | ENGEL | D | 85mm · ECU · profil | koyu/kırmızı-beyaz | MIRA #4 | G | |
| S11 | Kaçış | Yüz: gözler sola kayanı izler, baş durur; kısa nefes | kriz | ENGEL | C ↩S09 | (C) | kask/koyu | nefes tutulur | T | |
| S12 | İptal | OTS: port sola kayıp yan döner; T-kol geri; omuz yüksek | kriz | ENGEL (DENEME) | B ↩S08 | (B) | kabin | fan + klak | D | |
| S13 | Geri çekilme | Burun: gemi açılır; kopan panel sağ üstten yakın geçer | ikinci kriz | ENGEL | A | (A) | turuncu/siyah | taşıyıcı | – | |
| S14 | Gezegen | Tepe: istasyon ergimiş yüzeyin önünde salınır | ikinci kriz | — | F | 24mm · EWS · tepe | turuncu | taşıyıcı | – | ⭐ |
| S15 | Sıfır | Tepe KÜME: MIRA #5, insan yok | ikinci kriz | MUHATAP | F ⟶S14 | (F) | turuncu | MIRA #5 (telsiz) | – | |
| S16 | Hasarlı port | Port-kilitli: bükük güdükler ön planda; gemi soldan merkeze, sağa | ikinci kriz | ENGEL | G | 35mm · WS · göz hizası frontal | koyu gri/turuncu | taşıyıcı | – | |
| S17 | Abort | OTS: MIRA #6; baş iptal barına döner, kalır | ayrılık | AYRILIK | B ↩S12 | (B) | kabin | MIRA #6 | R | |
| S18 | Tereddüt | Yüz: el korumaya gider, avuç önünde durur, geri gelir | tırmanış | — | C ↩S11 | (C) | kask/koyu | iki kısa nefes | T | |
| S19 | Karar | El ECU: tıklatmasız düz gidiş, kapak kalkar; bar dokunulmamış | tırmanış | KARAR | D ↩S10 | (D) | koyu/kırmızı-beyaz | klik | K | |
| S20 | Basış | Yüz: omuz iner ve kalır; 6,0 s tek kısa basış | doruk | BEDEL başlar | C ↩S18 | (C) | kask/koyu | tek nefes, tutulur | B | |
| S21 | Pencere dolar | OTS: port merkeze gelir, hızla büyür, pencereyi doldurur | doruk | İSTEK | B ↩S17 | (B) | kabin/koyu | sessiz nefes | G | |
| S22 | Sert kenet DORUK | Port-kilitli: gemi kameraya büyür; 6,0 s oturma, dikmeler çöker | doruk | BEDEL | G ↩S16 | (G) | koyu gri/beyaz | taşıyıcı + tutulan nefes | – | ⭐ |
| S23 | Tek kare | Port-kilitli KÜME: hiçbir şey kımıldamaz; gezegen kayar | çözülüş | BEDEL | G ⟶S22 | (G) | koyu gri/turuncu | nefes bırakılır | – | ⭐ |
| S24 | Eller bırakır | OTS kafiye: port pencerede sabit; 4 lamba; eller uylukta; MIRA #7 #8 | çözülüş | İSTEK/BEDEL | B ↩S21 | (B) | kabin/beyaz lamba | MIRA #7 #8 | R | ⭐ |

(↩ = dönüş, kaynağı ≤3 sahne önce · ⟶ = küme, önceki klibin devamı)

## 3. 📐 ARDIŞIK ÇİFT DENETİMİ

```
ÖLÇEK ADIMLARI (23 çift): A→B 1 · B→C 1 · C→B 1 · B→A 1 · A→E 1 · E→A 1 · A→B 1 · B→C 1 · C→D 1 ·
  D→C 1 · C→B 1 · B→A 1 (bölüm sınırı) · A→F 1 · F=F küme · F→G 1 · G→B 1 · B→C 1 · C→D 1 · D→C 1 ·
  C→B 1 · B→G 1 · G=G küme · G→B 1
ARDIŞIK ÇİFT:     21 farklı çift / 21 bant içi (tam 1 kademe + ≥45° ya da iç↔dış) · 2 küme işaretli
BİLİNÇLİ ŞOK:     0 (ilk taslak 2 yazmıştı — gerek kalmadı)
AÇI TİPİ SAYISI:  6 (göz hizası frontal · OTS · alt açı · profil · üst açı · tepe)
KURULUM SAYISI:   7 (A B C D E F G) — 24 sahnede alt bant 3, üst bant 12 ✓
```

## 4. ⭐ KURULUM İSKELETİ

```
İSKELET (PLAN'daki ile aynı): A B C B A E A B C D C B A F F G B C D C B G G B

KÜME:   2 — S14-S15 (F) · S22-S23 (G); her biri 2 klip (tavan 3) ✓
DÖNÜŞ:  11 / 24 = %46 ≥ %40 ✓ — S04 S05 S07 S08 S11 S12 S15 S20 S21 S23 S24
        (dönüş = aynı harf en çok 3 sahne önce; küme klipleri dönüş sayılır)
DÖNÜŞ İŞARETİ: dönen her sahnenin kamera cümlesi kaynağıyla BİREBİR + "— the same position, height and lens as Scene N."
KÜME İŞARETİ:  "Continues the previous clip from its exact last frame — the same position, height and lens as Scene N."
HARF → KAMERA CÜMLESİ: PLAN Camera Bible (yedi satır, kelimesi kelimesine)
prompt_kontrol.py klasör modu (11.09.2026): ⑩①-④ ⑪ ⑫ ⑬ ⑭ ⑰ temiz → ✅ GO
```

## 5. 🎙️ REPLİK YERLEŞİMİ — PLAN §REPLİK TABLOSU'na taşındı

```
8 replik · MACHINE 8 / HUMAN 0 · saniyeler formülle: (n−1)×10 + klip ofseti [D122]
S02 3,0 → 0:13 · S03 3,0 → 0:23 · S06 3,0 → 0:53 · S10 3,0 → 1:33 · S15 3,0 → 2:23 · S17 3,0 → 2:43 ·
S24 2,0 → 3:52 · S24 7,0 → 3:57
YERLEŞİM GÜVENLİĞİ [SES §2]: S06 · S15 kadrajda insan YOK (en güvenli) · S02 S17 S24 sırttan ·
S03 yüz ama ağız kapalı (makine konuşur, lip-sync yapısal 0) · S10 el
DEĞİŞ-TOKUŞ: yok — makine söyler, insan cevap vermez (tasarım); her repliğin İŞLEV sütunu PLAN'da dolu
```

## 6. 🔢 METİNSİZ SAYAÇ

```
KANAL 1: gösterge lambası SAYISI — S01-S23 yanan 0 · S24 yanan 4 (tek adım; makinenin son sözünün görsel karşılığı)
KANAL 2: koruma kapağı — KAPALI (S02-S18) → AÇIK (S19 3,0 s → S24); tek yönlü
KANAL 3: dikme durumu — UZUN (S01-S22 6,0 s) → ÇÖKÜK (S22 6,0 s → S23); tek yönlü — filmin bedel sayacı
KANAL 4: pencerede portun büyüklüğü — S02 küçük → S08 1/3 → S12 2/3 (kaçar) → S17 küçük → S21 tam → S24 tam sabit
⛔ Hiçbiri rakamla yazılmaz; hepsi kadrajda SAYILABİLİR [D50 · D78 çift kanal]
```

## 7. ⛔ ÜRETİM SIRASI

```
ÜRETİM SIRASI: R1 → R2 → R3 → R4 (referans, KAPI 0) → S22 (DORUK) → S23 (tek kare) → S19 (merkezî seçim)
               → S24 (kapanış) → S01 (hook) → kalanı
⛔ İPTAL KAPISI: S22'de oturma ve dikmelerin çökmesi tek karede okunmuyorsa ya da S23'te gemi porta göre
   kımıldıyorsa film ÜRETİLMEZ (novum ekrana gelmiyor demektir [D73 · D157]).
```

---

## ✅ KAPI

```
☑ 24 sahnenin 24'ü tabloda, olay sütunu dolu ve BİRBİRİNDEN FARKLI
☑ ardışık çiftlerin hepsi denetlendi; şok 0; kümeler işaretli
☑ kurulum iskeleti yazıldı, KÜME 2 ve DÖNÜŞ %46 HESAPLANDI (ilan edilmedi)
☑ üretim sırası + iptal kapısı yazıldı
→ 04_UYARI_NOTLARI.md yazılabilir.
```
