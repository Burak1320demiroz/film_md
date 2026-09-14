# 📚 FAZ 5 / TEMAS — QA DERSLERİ VE AKSİYON RAPORU (1. KOŞU)

> Koşu: 10.08.2026 · Girdi: **8 ayrı klip · MODE T — beş fazda İLK KEZ**
> · Rubrik: `FAZ_05_QA_PROMPT.md` · Ham çıktı:
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP/THE_SECOND_SHIP_FAZ05_HAM.md`
>
> **Skor YOK — model rubriğin çıktı formatının yalnız ilk yarısını
> üretti** (WATCHER LEDGER, GROUND RESPONSE TABLE, DRAWING LEDGER,
> SCORES, PHASE CHAIN, FLAGS yok). Bu koşu bulgu koşusudur, taban
> koşusu değildir; taban, tam teslimatlı 2. koşudur.
>
> ⚠️ Operatör notu: **S47 bilerek yüklenmedi.** Ancak sayı tutmuyor —
> 10 sahneden 1 eksik = 9 klip beklenir, rubrik 8 saydı. İçerik
> eşlemesi de iki boşluğa işaret ediyor (§1). Yani yüklemeden S47 ile
> birlikte BİR SAHNE DAHA eksik kaldı (büyük olasılıkla S46; alternatif
> S48 — tek bakışlık test §5 madde 1).

---

## 1. KÖK NEDEN #1 — NUMARASIZ DOSYA ADI: eksik klip üç sahneyi kaydırdı

Dosya adlarında sahne numarası yoktu → rubrik yükleme sırasına düştü.
Eksik klip(ler) yüzünden 6-7-8. klipler birer yuva kaydı:

```
Rapordaki yuva:   S46            S47            S48         S49/S50
Gerçek içerik:    S48 (olası)    S49            S50         → teslim EDİLDİ,
                                                              yanlış yuvada
```

**Sonuçları:**
- Raporun S46/S47/S48 satırlarındaki "figure count" ve "shot class"
  bulgularının çoğu SAHTE — yanlış satıra karşı ölçüm (§2'de ayıklandı).
- Raporun **"S49 & S50 missing"** satırı YANLIŞ — ikisi de teslim
  edilmiş, kaymış. Gerçek boşluk: S47 + (S46 veya S48).
- Kaymış üç klip kendi satırına karşı HİÇ ölçülmedi: S48 adayının
  penceresi, S49'un push-in'i, S50'nin duvar tepkisizliği denetimsiz.

**İki kazanım da kaydedilsin:** MODE T ilk kez kullanıldı (F4 dersi ①
uygulandı) ve içerik-satır çelişki kuralı kaymayı **dördüncü kez**
yakaladı — sessiz düzeltmeye kaçmadı. Protokolün yarısı çalıştı;
batıran, uygulanmayan öbür yarısı (adlandırma). Adlar `s41.mp4 …
s50.mp4` olsaydı rapor tek satırla "slot s47 boş" diyecekti ve bu
bölüm hiç yazılmayacaktı.

---

## 2. DÜZELTİLMİŞ EŞLEME — hangi bulgu gerçek, hangisi kaymanın eseri

| Klip | Rapor yuvası | Gerçek sahne | Gerçek bulgular (yeniden atfedilmiş) |
|---|---|---|---|
| 1 | S41 | S41 ✓ | 🟡 el sürüklenme beati yok (3s); kalanı temiz — boy, düz sırt, plaka, yara izleri TUTTU |
| 2 | S42 | S42 ✓ | ✅ TEMİZ — kavrama olayı teslim edildi |
| 3 | S43 | S43 ✓ | ✅ TEMİZ — dolu vizör plakası İLK koşuda tuttu |
| 4 | S44 | S44 ✓ | 🔴 zeminde harf/sembol sızıntısı · 🔴 kama tek temiz uç değil, fazla çizgili |
| 5 | S45 | S45 ✓ | 🔴×4: ~8 s kısa · sol kenarda film şeridi + okunur rakam ("40","49") · Bekçi eldiveni BEŞ parmak · havada toz bulutu · ok ÇİFT BAŞLI (tek AŞAĞI kama değil) |
| 6 | S46 | **S48 (olası)** | kendi satırına karşı ölçülmedi; görünen: 3 figür + kule = S48 kadrajına uyumlu. Pencere/kapı/sırt denetimi 2. koşuya |
| 7 | S47 | **S49** | 🔴 kule tabanında KEMERLİ KAPI · 🟡 ~8 s kısa · çizgi keskin ✓ geçiş beati var ✓ — raporun "swell yok / Bekçi bacağı yok / lateral değil" bulguları S47 satırının eseri, DÜŞER |
| 8 | S48 | **S50** | 🔴 eldiven BEŞ parmak · dokunuş var ✓ düz sırt ✓ — duvar tepkisizliği ve iki-hareket kilidi kendi satırıyla ölçülmedi |
| — | S49 "missing" | teslim edildi (klip 7) | — |
| — | S50 "missing" | teslim edildi (klip 8) | — |

**Denetlenmemiş kalanlar:** S47 (üretilmedi/yüklenmedi) + S46 veya S48
(hangisi eksikse) + kaymış üç klibin kendi satır denetimleri.

---

## 3. KÖK NEDEN #2 — ÜRETİM: dersler (numaralar F4'ten devam)

### D-X 🔴 BEKÇİ ELDİVENİ İKİ SAHNEDE BEŞ PARMAK — çapa sorusu

S45 ve S50 (klip 5 + 8): eldiven **5 parmaklı insan eli** çıktı. Spec
"three fingers and a thumb" her iki promptta da yazılıydı — yetmedi.
İki bağımsız sahnede aynı hata = tekil üretim kazası değil, **sistemik**.

```
① İLK ŞÜPHELİ R3 MASTER PLAKASI. KARAR 4 ① kapısı "üç parmak" maddesi
   dahil insan gözüyle onay istiyordu. Onayda parmak SAYILDI mı?
   R3'ün eli beş parmaksa, ona yaslanan her el sahnesi hatayı miras alır.
② ÖRÜNTÜ: parmak hatası yalnız ELİN KADRAJI DOLDURDUĞU iki sahnede
   raporlandı (S45/S50 — el sahneleri). S41/S43/S48'de eller küçük →
   ya doğru ya görünmüyor. El yakın plana girdikçe insan-el klişesi
   baskın çıkıyor.
```

**Yeniden üretim dili — sayı + pozitif tarif + insan-el negasyonu:**

```
The glove has FOUR DIGITS IN TOTAL: three long fingers and one
thumb. Count them - four. It is NOT a human hand and has NO fifth
digit: a five-fingered glove is a failed frame. The three fingers
are evenly spaced, each thicker than a human finger.
```

### D-Y 🔴 ÇİZİM YAZIYA KAÇTI — S44 harf sızıntısı + S45 çift başlı ok

S44: gemi konturunun YANINDA zeminde harf-benzeri iz ve fazladan
semboller; kama ucu tek temiz V değil. S45: yön çizgisi **çift başlı
ok** — sahnenin tek bilgisi ("cevap: AŞAĞI") ekranda yok.

F4 D-O'nun ("adlandırdığın şeyin klişesini alırsın") çizim versiyonu:
**"drawing/diagram in the dust" dersen yazı-şema klişesi gelir** —
model toprağa şema çizen herkesin yanına not da yazar. Negasyon
("no letters, no digits") yine yetmedi; F4 D-Q ailesi: boşluğu
yasaklamak korumuyor, **pozitif doldurma** gerekiyor:

```
S44/S45 yaması (her iki prompta):
The dust around the two marks is BLANK, SMOOTH and UNMARKED - the
drawing is the only disturbance on the whole floor. The drawing is
exactly TWO marks and nothing else: the boxy ship outline, and ONE
straight groove with ONE wedge tip at ONE end only (S44: pointing
UP / S45: pointing DOWN). The other end of the groove is plain and
ends in nothing. A wedge at both ends is a failed frame.
```

### D-Z 🔴 S45 DÖRT AYRI RED — "en riskli sahne" öngörüsü tuttu

Üretim sırası notu bu sahne için "en riskli iki sahne — fazla deneme
bütçele" diyordu; dört bağımsız red sınıfı geldi:

```
① BEŞ PARMAK             → D-X (çapa)
② ÇİFT BAŞLI OK          → D-Y (bilgi kaybı — sahne anlamını taşımıyor)
③ HAVADA TOZ BULUTU      → KARAR 2 sayısal sınırı ("tane havada asılı
                           kalmaz") yazılıydı, yine delindi. F4 D-P kum
                           şelalesinin üçüncü vakası: SÜREKLİ/ASILI
                           parçacık dili modelde varsayılan. Yama:
                           "the air is perfectly clear for all ten
                           seconds - not one particle floats; every
                           moving grain stays IN CONTACT WITH THE
                           GROUND at every moment"
④ FİLM ŞERİDİ YANIĞI     → sol kenarda dikey şerit + okunur rakamlar
                           ("40","49"). Bu üretim içeriği değil,
                           ARTEFAKT kokuyor (kontakt şeridi / UI
                           kalıntısı / ihraç hatası). Teşhis: kaynak
                           dosyada var mı, yoksa ihraçta mı bindi?
                           İhraç hatasıysa yeniden ihraç bedava —
                           ama sahne ①-③ yüzünden zaten yeniden
                           üretime gidiyor.
```

### D-AA 🔴 S49 KULE TABANINDA KAPI — negasyon o prompta gömülmemişti

Klip 7 (gerçek S49): arka plandaki kulenin tabanında **kemerli kapı /
giriş boşluğu**. "No windows at all, no doors, no openings, lit or
unlit" negasyonu S46/S48/S50 promptlarına gömülmüştü [KARAR 4 ④] —
**S49'un kendi promptunda kule tek cümle geçiyor ve negasyon YOK**
("running to the base of a colossal matte white seamless tower").

F4 D-O dersinin tamamlayıcısı:

```
KULE NEGASYONU KADRAJA BAĞLIDIR, SAHNEYE DEĞİL. Kule hangi sahnenin
kadrajına giriyorsa — merkez konu ya da arka plan farketmez —
pencere/kapı/açıklık negasyonu O promptta da tekrarlanır. "Seamless"
sıfatı kapıyı engellemiyor: model kapıyı dikişsiz duvara da açar.
Taban en riskli bölge: "kule + zemin buluşması" mimari klişeyi
(giriş kapısı) çağırıyor.
```

**S49 prompt yaması (NEGATIVE bloğuna):**

```
The tower carries NO door, NO archway, NO entrance, NO gate, NO
opening of any kind at its base or anywhere on it, lit or unlit -
the wall meets the polished ground as one unbroken blank surface.
```

### D-AB 🟡 EXTEND ÜÇÜNCÜ KEZ ATLANDI — S45 ve S49 klipleri ~8 s

F3 D-N → F4 D-V → F5. "10 klip × 10.00 s" kontrolü F5 prompt
dosyasının SONRAKİ ADIM bloğunda madde olarak yazılıydı; yine düştü.
⚠️ Süre şerhi geçerli (F3 §4): modelin ölçümü kanıt değildir, gerçek
süre NLE'de doğrulanır. Doğrulanırsa: iki klip extend ile 10.00 s'ye
tamamlanır — S45 zaten yeniden üretimde, S49 için extend kararı
yeniden üretimle birleşik verilir.

### D-AC 🟡 RAPOR YARIM ÇIKTI — skor ve tabloların hiçbiri üretilmedi

Model MATERIAL + CLIP MAP + PASSPORT + sahne bulgularını verdi;
WATCHER LEDGER, GROUND RESPONSE TABLE, DRAWING LEDGER, SCORES, TOP 5,
PHASE CHAIN, FLAGS, WHAT WORKED **yok**. Kayma + iki "missing" yuva
modeli formatın dışına savurmuş olabilir. 2. koşuda tam teslimat (10
adlandırılmış klip) + gerekirse "produce every section of the OUTPUT
FORMAT" hatırlatması. Skor tabanı 2. koşudur.

---

## 4. TUTAN TARAF — bu koşunun gerçek kazanımları

| Kilit | Kanıt |
|---|---|
| **Dolu vizör plakası [KARAR 4 ③ · F4 D-Q]** | S41 + S43: *"opaque dark flush surface without internal eye/face rendering"* — F4'te negasyonla batan kilit, pozitif doldurma diliyle İLK koşuda tuttu. "Boşluğu yasaklama, doldur" dersi sahada doğrulandı. |
| **Bekçi çapası 5/6 [F4 D-R sonrası]** | Boy (~2.10 m, adamdan bir baş uzun) · DÜZ sırt ("zero hoses, straps, or packs") · tozsuz dikişsiz beyaz · plaka — F4'te batan beş maddeden dördü tuttu. Batan tek madde: parmak sayısı [D-X]. R3 kapısı çalışmış görünüyor — el hariç. |
| **"THE ONLY EVENT" açılışı [F4 D-T]** | S42: kavrama olayı eksiksiz teslim ("fully compliant take"). S44'te de çizim OLAYI üretildi (içeriği bozuk ama dekor-olaysız sınıfı tekrarlamadı). |
| **Işık kilidi** | Sekiz klipte sabit: 4400K sol key, soluk gökyüzü, gündüz ayı. |
| **Kimlik/kostüm** | Yara izleri doğru taraflarda, orange/teal doğru sahiplerde, şeffaf insan vizörleri, 13 cm fark — sıfır bulgu. |
| **MODE T + eşleme kuralı** | İlk MODE T koşusu; içerik-satır kuralı kaymayı 4. kez yakaladı ve sessiz düzeltmedi. |

---

## 5. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ TEK BAKIŞ (bedava, 30 sn): 6. dosyayı aç.
     → İşaret eden kaldırık kol + ufukta İNCE çizgi görüyorsan: S46
       teslim edilmiş demektir; eksikler S47 + S48.
     → Yürüyen ÜÇLÜ sıra + devasa kule görüyorsan: o klip S48'dir;
       eksikler S46 + S47. (Rapor tarifi bunu söylüyor — olası olan bu.)
     Diskteki üretilmiş sahne envanteriyle karşılaştır, boşluğu kesinleştir.
2. □ ADLANDIRMA (bedava): tüm klipleri s41.mp4 … s50.mp4 yap.
     Bu yapılmadan İKİNCİ KOŞU BAŞLATILMAZ.
3. □ ⛔ R3 EL KONTROLÜ [D-X]: R3 master plakasında parmakları SAY.
     → Beş ise: R3 düzeltilip yeniden onaylanır; el sahneleri ondan
       sonra üretilir (çapa zinciri, F4 dersi ⑦).
     → Üç ise: hata sahne üretiminde; D-X'in sayısal kilidi el
       sahnelerinin promptlarına girer.
4. □ S45 ŞERİT TEŞHİSİ [D-Z ④]: rakamlı şerit kaynak dosyada mı,
     ihraçta mı bindi? (Sahne zaten yeniden üretimde; teşhis, aynı
     artefaktın başka kliplere binip binmediğini anlamak için.)
5. □ PROMPT YAMALARI (üretimden önce, FAZ_05_TEMAS.md'ye):
     a) S49 NEGATIVE bloğuna kule kapı/açıklık negasyonu [D-AA]
     b) S44 + S45'e boş zemin pozitif doldurma + "ONE wedge tip at
        ONE end only" [D-Y]
     c) S45 + S47'ye "not one particle floats / every grain stays in
        contact with the ground" [D-Z ③]
     d) Bekçi el sahnelerine (S45 S50, gerekirse S41 S46) "FOUR
        DIGITS IN TOTAL - count them" kilidi [D-X]
6. □ YENİDEN ÜRETİM (kırmızılar, çapa sırasına göre):
     S45  dört red [D-X D-Y D-Z] — R3 el onayından SONRA
     S50  beş parmak [D-X] — R3 el onayından SONRA
     S44  harf temizliği + tek kama [D-Y]
     S49  kule kapısı [D-AA] (+ süre NLE'de kısaysa extend/yeniden)
7. □ EKSİK SAHNELERİ ÜRET: S47 (+ madde 1'in sonucuna göre S46 veya
     S48). S47 el içermiyor (bacak/bot kadrajı) — R3 el onayını
     beklemeden üretilebilir.
8. □ SÜRE DOĞRULAMASI [D-AB]: NLE'de 10 klip × 10.00 s.
9. □ İKİNCİ KOŞU: tam 10 adlandırılmış klip, MODE T. Skor tabanı o
     koşudur. Kaymış üç klibin (S48 adayı · S49 · S50) kendi satır
     denetimleri ilk kez orada yapılacak — özellikle S48 penceresi,
     S49 push-in'i, S50 duvar tepkisizliği.
```

---

## 6. F6+ VE SİSTEME TAŞINANLAR

```
① ADLANDIRMA PROTOKOLÜN     MODE T tek başına yetmiyor: numarasız ad +
   YARISIDIR                eksik klip = kayan eşleme + sahte "missing".
                            Kural artık iki parçalı: AYRI dosya VE
                            adında numara. [§1]

② EL YAKIN PLANA GİRİNCE    Üç parmak kilidi uzak planda tutuyor, el
   PARMAK KİLİDİ SERTLEŞİR  kadrajı doldurunca insan-el klişesi
                            kazanıyor. El sahnelerinde sayısal kilit +
                            "count them" + insan-el negasyonu. [D-X]

③ ÇİZİM SAHNESİ = YAZI      "drawing in the dust" şema klişesini
   RİSKİ                    çağırır (yanına not yazar, oka ikinci baş
                            ekler). Pozitif doldurma: "the floor is
                            blank; the drawing is exactly N marks and
                            nothing else". [D-Y]

④ NEGASYON KADRAJI TAKİP    Kule/yapı negasyonu nesnenin GÖRÜNDÜĞÜ her
   EDER                     prompta yazılır — merkez konu ya da arka
                            plan farketmez. Taban bölgesi kapı klişesi
                            için en riskli nokta. [D-AA]

⑤ ASILI PARÇACIK ÜÇÜNCÜ     F4 D-P (şelale) → F5 D-Z (havada bulut).
   VAKA                     "Settles at once" yetmiyor; "every grain
                            stays in contact with the ground" pozitif
                            kilidi denenecek. [D-Z ③]

⑥ POZİTİF DOLDURMA DERSİ    F4 D-Q'nun çözümü (dolu plaka) ilk sahada
   DOĞRULANDI               DOĞRULANDI — iki vizör sahnesi temiz. Bu
                            ders LESSONS_LEARNED adaylığını hak etti;
                            işlenirken kaynak rubrik önce yamalanır
                            (kart G kuralı). [§4]
```

---

> **Bu dosya ne zaman güncellenir:** madde 1'in tek-bakış sonucu
> netleşince, R3 el kontrolü yapılınca, yeniden üretimler ve eksik
> sahneler bitince, ve tam 10 klip MODE T ile ikinci kez koşulunca.
