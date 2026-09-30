# 📚 FAZ 6 / KULE — QA DERSLERİ VE AKSİYON RAPORU (1. KOŞU)

> Koşu: 11.08.2026 · Girdi: **1 birleşik reel (~100 s) · MODE R —
> KARAR 5 ⑨'a RAĞMEN** · Rubrik: `FAZ_06_QA_PROMPT.md` · Ham çıktı:
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP/THE_SECOND_SHIP_FAZ06_HAM.md`
>
> **Skor YOK — model çıktı formatının yalnız bir kısmını üretti**
> (PATTERN LEDGER, FLOOR LEDGER, SPEECH LEDGER, SCORES, TOP 5,
> SCENE-BY-SCENE, PHASE CHAIN, FLAGS, WHAT WORKED yok — F5 D-AC'nin
> tekrarı). Bu koşu bulgu koşusudur, taban koşusu değildir; taban,
> 10 adlandırılmış kliple tam teslimatlı 2. koşudur.
>
> ⚠️ Operatör notu: **reel'deki sahne SIRASI S51→S60 sırasına
> uymayabilir.** MODE R eşlemesi sırayı varsayar (ilk segment = S51);
> rapor SEGMENT MAP'i kusursuz 10 × 10.0 s verdi — bu ölçüm değil
> varsayım olabilir [F3 süre şerhi]. Bu yüzden aşağıda her bulgu
> İÇERİK ÇAPASIYLA sınıflandı: bulgunun tarif ettiği içerik o sahneyi
> tek başına tanımlıyorsa bulgu sıra kaymasından ETKİLENMEZ.

---

## 1. KÖK NEDEN #1 — REEL TESLİMATI: altı fazda BEŞİNCİ protokol kayması

KARAR 5 ⑨ ve rubriğin kullanım bloğu açıktı: 10 AYRI dosya, adında
sahne numarası, reel ile koşu YOK. Yine reel gitti. Rubrik ihlali
yakaladı ve PROTOCOL DEVIATION satırını raporun başına yazdı —
protokolün rubrik yarısı çalıştı, operatör yarısı yine çalışmadı.

**Bedeli bu koşuda somut:** S58 bulgusu (aşağıda D-AH) sıra kayması
ihtimali yüzünden ŞARTLI kaldı — ayrı adlandırılmış dosyalarla
gelseydi kesin olacaktı. Ayrıca segment sınırları ölçülemediği için
süre denetimi (10 × 10.00 s) bu koşuda hiç yapılamadı.

```
F2'den beri örüntü: prompt dosyasına yazılan teslimat cümlesi
operatör davranışını DEĞİŞTİRMİYOR. Mekanik kapı gerekiyor: üretim
klasörüne baştan s51.mp4 … s60.mp4 adlı boş yuva şablonu açmak,
kurgu aracının "reel ihraç" düğmesine hiç gitmemek. [→ §6 ④]
```

---

## 2. BULGU AYIKLAMASI — içerik çapası: hangi bulgu kaymadan etkilenmez

| Rapor yuvası | Bulgu | İçerik çapası | Güvenilirlik |
|---|---|---|---|
| S51 0:02 + 0:05 | çatlak eğri büğrü + kapı KASASI | duvar ayrılması + 3 figür = tek aday S51 | ✅ SAĞLAM |
| S52 0:10 | duvarda yatay panel çizgileri | tilt + kavisli iç duvar + iki küçük figür = tek aday S52 | ✅ SAĞLAM |
| S53 0:24 | sürtme arkasında koyu iz | eldiven sürtmesi = tek aday S53 | ✅ SAĞLAM |
| S55 0:41 + 0:45 | ok başları + BEŞ parmak | daireler + iplikler + duvarda eldiven = tek aday S55 | ✅ SAĞLAM |
| S58 1:15 | ağız hiç açılmıyor → olay yok | "iki insan, lockoff" içeriği S58'e uyar AMA rapor segmentin içeriğini tarif etmedi; sıra kaydıysa 1:10-1:20'de başka sahne olabilir | ⚠️ ŞARTLI — tek bakış testi (§5 madde 1) |
| S51/S54/S60 | ledger: 4 hane ✓ | üçü de içerikle tanımlı (3 figür / desen duvarı+2 figür / tek Bekçi eğilmesi) | ✅ olumlu kanıt |

**Ayrıca dikkat:** rapor yarım olduğu için "bulgu yok" ≠ "temiz".
§4'teki tutan taraf satırları PASSPORT'a dayanıyor; kesinleşme 2.
koşuda.

---

## 3. KÖK NEDEN #2 — ÜRETİM: dersler (numaralar F5'ten devam)

### D-AD 🔴 S51 KEMER ENGELLENDİ, HATA KASAYA KAÇTI — negasyon klişeyi komşuya kaydırır

F5 D-AA yaması ("never an arch") ÇALIŞTI — kemer yok. Ama model aynı
klişe ailesinin komşu üyesini üretti: **kalın, girintili, panelli
kapı kasası + görünür iç yüzeyler** — spec "no frame and no visible
thickness" derken. Üstüne açılış çatlağı düz değil **eğri büğrü**
("jagged crack") — "vertical hairline of shadow" cümlesi çatlak
klişesini çağırmış olabilir.

```
DERS: mimari-giriş klişesi bir AİLEDİR (kemer · kasa · eşik · kanat ·
ray). Tek üyeyi yasaklamak modeli ailenin sıradaki üyesine yollar.
Aile pozitif doldurma ile TOPTAN kapatılır:

S51 yaması (IMAGE + VIDEO, NEGATIVE ve beat 2s/4s):
The parting line is PERFECTLY STRAIGHT and vertical, thin as a
hair - never jagged, never forked, never crooked. The edges of the
opening are KNIFE-THIN: the wall reads as a single thin surface
with NO returns, NO inner faces, NO jamb, NO reveal, NO recess -
past the edge there is only the flat white interior, nothing
between. A door frame of any kind is a failed frame.
```

### D-AE 🔴 S52 DUVARDA PANEL ÇİZGİLERİ — "seamless" yine yetmedi, boş yüzey + kamera hareketi ölçek icat ettirir

Tilt boyunca kavisli duvarda **yatay panel hatları/dikişler**. Video
promptunda hem "no seam, panel, rivet" hem "no seam or marking
passing at any point" YAZILIYDI — ikisi de delindi. F5 D-AA'nın
("seamless sıfatı kapıyı engellemiyor") duvar versiyonu: model
hareketli kamera altında tamamen boş yüzeye dayanamıyor, göze hız
referansı vermek için doku icat ediyor.

```
DERS: boş dev yüzey + kamera hareketi = doku icadı tetikleyicisi.
Negasyon listesine ekleme değil, pozitif malzeme tarifi:

S52 yaması (ENVIRONMENT + video FRAME):
The wall is ONE CONTINUOUS POURED SURFACE, the same unbroken
matte white at every height - no horizontal lines, no bands, no
tiers, no tile joints, no repeating texture of any scale. During
the whole tilt the surface stays perfectly uniform: the ONLY cue
that the camera is moving is the figures leaving the bottom of
frame.

+ ÜRETİM: S52'nin END FRAME imajı (bkz. imaj bütçesi) zaten planda —
o kare BOŞ BEYAZ karedir; tilt üretimine start + end imaj ÇİFTİ
verilir ki ara karelerde doku türeyecek yer kalmasın.
```

### D-AF 🔴 S53 DUVAR İZİ KAYDETTİ — kirli nesne + iz yasağı çelişkisi kaybedilir

Sürtmenin arkasında **koyu çizik/iz** kaldı — sahnenin TEK OLAYI
("the drag that records nothing") batırıldı. MOST LIKELY FAILURE
öngörüsü birebir tuttu. Kök neden promptun kendi içinde: parmak
uçlarına bilerek **görünür toz** yazıldı ("fingertips visibly grubby
with fine grey dust") ve ardından izin yasaklanması istendi. Model
fizik önselini izledi: kirli eldiven temiz yüzeyde iz bırakır.

```
DERS [F5 ⑤ asılı-parçacık ailesinin kardeşi]: fizik önseline karşı
negasyonla savaşılmaz — İZ KAYNAĞI SAHNEDEN ÇIKARILIR.

S53 yaması: "grubby fingertips / fine grey dust" cümleleri IMAGE ve
VIDEO prompttan SİLİNİR; eldiven temiz. "Dışarıdan gelen kir vs
zamansız kule" bilgisi zaten S51'de (dış sahne, tozlu zemin) ve
suit'in yıpranmış orange panelinde duruyor — sahnenin anlamı
(yüzey hiçbir teması kaydetmiyor) temiz eldivenle de eksiksiz
okunur. Toz kalksa bile iz negasyonu promptta KALIR.
```

### D-AG 🔴 S55 İKİ TEKRAR SUÇLU AYNI KAREDE — ok başı [F5 D-Y 2. vaka] + beş parmak [F5 D-X 3. vaka]

İpliklerde **sağa bakan ok başları** — "no arrowhead at either end"
negasyonu yazılıydı, ikinci kez delindi. Eldiven **5 hane** — "FOUR
DIGITS IN TOTAL - three long fingers and one thumb, not a human
hand" sayısal kilidi yazılıydı, sınıfın üçüncü vakası (F5 S45 → F5
S50 → F6 S55). Ledger'ın diğer üç Bekçi sahnesi 4 hane: hata yine
YALNIZ elin kadrajı doldurduğu düz-eldiven-duvarda sınıfında.

```
① OK BAŞI: "iplik + yön" kompozisyonu ok klişesini çağırıyor;
   negasyon yetmiyor. Pozitif uç tarifi:
   Each thread is a plain uniform line that terminates FLUSH at
   the rim of each circle - the line simply STOPS at the circle's
   edge, the same thickness to its last point. Nothing is ever
   attached to either end: no tip, no head, no barb, no taper.

② BEŞ PARMAK: önce SÜREÇ sorusu — TETİK KAPISI 2 uygulandı mı?
   → Uygulanmadıysa: kapı atlanmış; R3 + F5 düzeltilmiş el
     sahneleri onaylanmadan S55 yeniden üretilmez (mevcut kural).
   → Uygulandıysa ve yine beş çıktıysa: bu sınıfta PROMPT KİLİDİ
     TÜKENDİ; çözüm kadraja taşınır — parmakların tamamını sayılır
     biçimde göstermeyen açı (el hafif profilden / iki parmak
     birbirini kısmen örter / parmak uçları kadraj kenarında) VEYA
     onaylı R3 el karesinin start-frame imaj olarak verilmesi.
     [→ §6 ③]
```

### D-AH ⚠️ ŞARTLI 🔴 S58 OLAY YOK — ağız hiç açılmadı; önce sıra kayması elensin

Rapor: kadının ağzı sahne boyunca kapalı → "cümlenin yarıda ölmesi"
olayı hiç başlamamış. Bu, F4 D-T (dekor üretildi, olay üretilmedi)
sınıfının en İNCE vakası: olayın tamamı bir dudak hareketi.

```
AMA: bulgu MODE R varsayımlı eşlemeden geliyor ve rapor segmentin
içeriğini tarif etmedi. Yeniden üretim kararından ÖNCE tek bakış:
reel 1:10-1:20'de ne var?
→ İki insan, uyluk-üstü, lockoff, dinleme duruşu VE ağız hiç
  açılmıyorsa: bulgu GERÇEK → S58 yeniden üretilir. Yamaya gerek
  yok — beat promptta zaten açık ve tek başına net; bu sınıfta
  batıran prompt değil, modelin mikro-olayı düşürmesi. Yeniden
  denemede beat aynı kalır, deneme bütçesi artırılır.
→ Orada BAŞKA sahne varsa: reel sırası kaymış → S58 bulgusu düşer,
  tüm segmentler içerikle yeniden eşlenir ve bu dosyanın §2'si
  güncellenir; gerçek S58 segmenti bulunup olay oradan denetlenir.
```

### D-AI 🟡 SEGMENT MAP KUSURSUZ 10 × 10.0 — ölçüm değil varsayım olabilir

Rubrik "kesmeleri TESPİT ET, ölçülen start/end/length yaz" diyordu;
kusursuz onluk harita modelin slot varsayımına düştüğünü düşündürür
[F3 süre şerhi: modelin ölçümü kanıt değildir]. Süre denetimi bu
koşuda YAPILMAMIŞ sayılır — NLE'de klip başına doğrulanır
(extend atlama sabıkası: F3 D-N → F4 D-V → F5 D-AB).

### D-AJ 🟡 RAPOR YİNE YARIM — F5 D-AC'nin tekrarı

Ledger'ların üçü (PATTERN, FLOOR, SPEECH) ve skor/sonuç bölümlerinin
tamamı üretilmedi. İkinci koşuda tam teslimat: 10 adlandırılmış klip
+ gerekirse prompta "produce every section of the OUTPUT FORMAT"
hatırlatması.

---

## 4. TUTAN TARAF — bu koşunun gerçek kazanımları (⚠️ rapor yarım; PASSPORT'a dayalı, kesinleşme 2. koşuda)

| Kilit | Kanıt |
|---|---|
| **Dolu vizör plakası [F4 D-Q → KARAR 5 ②]** | Dört Bekçi sahnesinde de "filled, flush, dark grey-green opaque plate, no interior visible" — pozitif doldurma dili ÜÇÜNCÜ koşuda üst üste tutuyor. S60'ta "pale reflection" cümlesinin silinmesi de tuttu: yansıma bulgusu yok. |
| **Kemer negasyonu [F5 D-AA]** | Kemer YOK — negasyon hedefini vurdu. (Hata kasaya kaydı → D-AD; ama F5'in birebir hatası tekrarlamadı.) |
| **Kule içi ışık [KARAR 1]** | "Flat, cool, sourceless 5600K, no hard shadows or visible fixtures" — model lamba İCAT ETMEDİ. Eşik de tuttu: "meeting unblended at the threshold". |
| **Desen dili [KARAR 3 · Ders 13]** | "No readable text, digits, or grids" + "patterns cast no light onto the room" — harf sızıntısı ve ışık sızıntısı İKİSİ DE yok. S57 çizgileri "irregular" ✓ (düzenli ızgara tuzağına düşmedi). |
| **Boş zemin [KARAR 2]** | "The floor is polished, empty, and unbroken" — plaka sızmadı, F7 açılışı harcanmadı. |
| **Bekçi hane sayımı 3/4** | S51 · S54 · S60 = 4 hane. Sayım zorunluluğu (rubrik yeniliği) S55'i YAKALADI — tarifle geçiştirilseydi beş parmak belki raporlanmayacaktı. |
| **Kimlik/kostüm** | Yara izleri doğru taraflarda, orange/teal doğru sahiplerde, 13 cm fark, sırt modülü adamda — sıfır bulgu. |
| **Figür sayıları** | Fazladan figür bulgusu yok; üç figürlü S51 bu sınıfın ilk temiz koşusu olabilir [F3 D-L] — 2. koşuda doğrulanacak. |
| **Rubrik protokol kapısı** | MODE R'ı teşhis etti, ihlal satırını başa yazdı, denetimi yine de tamamladı — tasarlandığı gibi. |

---

## 5. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ TEK BAKIŞ (bedava, 60 sn): reel'i aç, 10 segmentin içeriğini
     sırayla not et — sıra S51→S60'a uyuyor mu?
     → Özellikle 1:10-1:20: iki insan lockoff + ağız kapalı mı?
       [D-AH kararı buna bağlı]
     → Sıra kaymışsa: §2 tablosu yeniden atfedilir, bu dosya
       güncellenir.
2. □ AYRI DOSYA + ADLANDIRMA (bedava): 10 klip s51.mp4 … s60.mp4.
     Üretim klasörüne boş yuva şablonu aç [§1]. Bu yapılmadan
     İKİNCİ KOŞU BAŞLATILMAZ.
3. □ ⛔ TETİK KAPISI 2 DENETİMİ [D-AG ②]: S55 üretiminden önce R3'te
     ve F5 düzeltilmiş el sahnelerinde parmak SAYILDI mı?
     → Sayılmadıysa: önce o zincir tamamlanır.
     → Sayıldıysa: kadraj çözümüne geç (el profilden / start-frame
       imaj olarak onaylı R3 el karesi).
4. □ PROMPT YAMALARI (üretimden önce, FAZ_06_KULE.md'ye):
     a) S51: düz çatlak + bıçak-ince kenar + kasa ailesi negasyonu
        [D-AD]
     b) S52: "one continuous poured surface" + start/end imaj çifti
        [D-AE]
     c) S53: parmak ucundaki toz SİLİNİR — iz kaynağı sahneden
        çıkar [D-AF]
     d) S55: iplik uçları "terminates FLUSH at the rim - the line
        simply stops" [D-AG ①]
5. □ YENİDEN ÜRETİM (kırmızılar, çapa sırasına göre):
     S53  iz [D-AF] — ÇAPA SAHNE: ışık/yüzey onayı bunun üstünde,
          önce bu
     S52  panel çizgileri [D-AE]
     S51  çatlak + kasa [D-AD]
     S55  ok + parmak [D-AG] — el onay zinciri kapandıktan SONRA
     S58  tek bakış sonucuna göre [D-AH]
6. □ SÜRE DOĞRULAMASI [D-AI]: NLE'de 10 klip × 10.00 s — reel
     haritası kanıt sayılmaz; S60 retime (8 s × 0.8) ayrıca kontrol.
7. □ İKİNCİ KOŞU: tam 10 adlandırılmış klip, MODE T, tam çıktı
     formatı. Skor tabanı o koşudur. Bu koşuda hiç denetlenmemiş
     kalanlar orada ilk kez ölçülür: S54 kaydırma disiplini, S56/S59
     mimik kilitleri + kadraj rimi, S57 sütun uçları, S60 tek-hareket
     yasası, PHASE CHAIN, üç ledger.
```

---

## 6. F7+ VE SİSTEME TAŞINANLAR

```
① NEGASYON KLİŞEYİ KOMŞUYA     Kemeri yasakla → kasa gelir. Mimari
   KAYDIRIR                    klişe bir ailedir; tek üye değil aile
                               kapatılır, pozitif kenar tarifiyle
                               ("knife-thin, no returns, no inner
                               faces"). F7 S61 kapı/plaka kadrajları
                               aynı ailenin üstünde. [D-AD]

② BOŞ YÜZEY + KAMERA HAREKETİ  Model hareket altında boş yüzeye doku
   = DOKU İCADI                icat eder ("seamless" yetmez). Kule içi
                               hareketli tüm sahnelere (F7 · F9 aynı
                               dekor!) pozitif "one continuous poured
                               surface" dili + start/end imaj çifti.
                               [D-AE]

③ EL-DOLU-KADRAJ SINIFI        Üçüncü vaka: sayısal kilit + count-them
   PROMPT'LA ÇÖZÜLMÜYOR        de yetmedi. Sınıfın çözümü kadraj/
                               referans katmanında: parmakları sayılır
                               göstermeyen açı veya onaylı el karesi
                               start-frame. F8+ el sahnesi planlanırken
                               bu sınıftan kaçınılır. [D-AG]

④ İZ KAYNAĞINI ÇIKAR,          Kirli nesne + "iz bırakma" negasyonu =
   İZİ YASAKLAMA               fizik önseliyle kaybedilen savaş. Temas
                               sahnelerinde temas eden yüzey TEMİZ
                               tutulur; kir bilgisi başka sahnede
                               verilir. [D-AF — F5 ⑤ ailesi]

⑤ TESLİMAT PROTOKOLÜ CÜMLEYLE  Beşinci reel/adlandırma kayması. Yazılı
   DÜZELMİYOR — MEKANİK KAPI   kural işlemiyor; klasöre önceden boş
                               yuva şablonu (s51…s60) açmak gibi
                               mekanik bir adım gerekiyor. [§1]

⑥ MİKRO-OLAY SINIFI            Olayı tek dudak/göz hareketi olan
   (İZLEMEDE)                  sahneler (S58 yarım cümle) modelin en
                               kolay düşürdüğü beat sınıfı olabilir —
                               D-AH tek bakış sonucuna göre F4 D-T'nin
                               altına mikro-vaka olarak kesinleşir ya
                               da düşer. Şimdilik ders değil, gözlem.
```

---

> **Bu dosya ne zaman güncellenir:** madde 1'in tek-bakış sonucu
> netleşince (D-AH kesinleşir/düşer, §2 gerekirse yeniden atfedilir),
> TETİK KAPISI 2 denetimi yapılınca, yeniden üretimler bitince, ve
> tam 10 klip MODE T ile ikinci kez koşulunca.
