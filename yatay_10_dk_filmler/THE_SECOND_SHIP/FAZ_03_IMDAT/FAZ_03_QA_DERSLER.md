# 📚 FAZ 3 / İMDAT — QA DERSLERİ VE AKSİYON RAPORU

> Koşu: 08.08.2026 · Model: Gemini · Girdi: tek 96 s reel (8×10.0 s +
> 2×8.0 s) · MODE R · Rubrik: `FAZ_03_QA_PROMPT.md` · Ham çıktı:
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP/THE_SECOND_SHIP_FAZ03_HAM.md`
>
> **Skor 3.7/10 — ama bu sayı ÜRETİMİ ölçmüyor, iki hatanın karışımını
> ölçüyor:** reel yanlış sırada kurulmuş (5 slot kayık) ve klipler o
> yanlış slotların satırlarına karşı puanlanmış. Figür sayımı 1, faz
> zinciri 2, fizik 6'nın bir kısmı = montaj hatası. Hasar 1, zemin-siluet
> 1, kostüm 2 = gerçek üretim hatası. **Önce kurgu düzeltilir, sonra
> yeniden üretim, sonra İKİNCİ KOŞU — 3.7 geçersizdir.**

---

## 1. KÖK NEDEN #1 — MONTAJ: REEL YANLIŞ SIRADA (Faz 1'in tekrarı)

```
Reel'deki gerçek sıra:   S21 · S23 · S22 · S24 · S25 · S27 · S28 · S26 · S29 · S30
Olması gereken:          S21 · S22 · S23 · S24 · S25 · S26 · S27 · S28 · S29 · S30
                                ↑ ikili takas ↑                ↑ üçlü rotasyon ↑
```

Faz 1'de S4-S7 rotasyonu olarak yaşanmıştı; aynı sınıf hata üçüncü
fazda tekrarladı. Rubriğin "içerik satıra uymuyorsa SESSİZCE yeniden
eşleme, bulgu yaz" kuralı beş misfile'ın beşini de yüzeye çıkardı —
tam bunun için yazılmıştı.

**Bedeli:** 0:10–0:30 ve 0:50–1:20 verdiktleri çapraz-kirli. Örnek:
gerçek S27 klibi (zemin makrosu) S26 satırına karşı ölçüldü — 4.
saniyedeki TEK VURUŞUN var olup olmadığı bu rapordan ÖĞRENİLEMİYOR.
"Single tremor missing" bulgusu S28-içerikli klibe bakılarak yazıldı.

**Çözüm (bedava, kurguda):** 2↔3 takası + 6/7/8 → 8/6/7 rotasyonu.
**Kalıcı önlem:** montajdan önce klip dosya adına sahne numarası yaz
(`s21.mp4` … `s30.mp4`) — ya da hiç birleştirme, 10 ayrı dosyayı
MODE T'ye yükle: rubrik dosya adından eşler, sıra hatası imkânsızlaşır.

---

## 2. TUTAN TARAF

| Kilit | Skor/Kanıt |
|---|---|
| Kamera disiplini | 8/10 — sahne içi kesme yok, hızlar sabit |
| Gece ışık envanteri | 7/10 — ay HEP sol üstte, gece hiç bozulmadı |
| Bot-zemin fiziği | "reads perfectly with appropriate weight" (0:50 klibi) |
| Mast açılma mekaniği | "mechanically smooth and distinct" (S24) |
| S25 push-in + ışık | "highly cinematic and steady" |
| Yüz sabitliği | kemik yapısı stabil (sorun tarafta, yapıda değil — §3 D-H) |

F2'nin iki kırmızısı (D-B ateş refleksi, D-C kamera sarsıntısı) bu
fazda hiç görünmedi — o düzeltmeler taşınmış ve tutmuş.

---

## 3. KÖK NEDEN #2 — ÜRETİM: yedi ders

### D-G 🔴 HASAR ÇAPASIZ ÜRETİM — fazın en pahalı hatası

Dört kalıcı işaretin DÖRDÜ DE hiçbir sahnede yok: gemi dümdüz ve
karnının üstünde, delik yerine CAMLI LOMBAR (D-A'nın aynısı), bacak
yerine yine KIZAK (F2 D-F'in aynısı), oluk yok, kapak sarı ışık saçıyor.

F2 aksiyon listesinin 1. maddesi açıktı: **"S13/S14 düzelmeden F3
üretimine BAŞLANMAZ"** — başlanmış. Prompt metnindeki "polished +
açık-delik negasyonu" düzeltmeleri görüntüye yansımadığına göre üretim
ya eski prompt sürümüyle ya da hasarlı-gemi çapa imajı (R4/S19-END)
olmadan koşuldu → doküman sorusu §5'te.

```
YENİDEN ÜRETİM KAPISI: F3 dış sahneleri (S21 S23 S26 S28 S30) hasar
çapası üretilip doğrulanmadan YENİDEN ÜRETİLMEZ. Çapa promptunda:
"tilted exactly 4 degrees right · right main leg collapsed · three
legs, never skids · one open 1.2 m circular hole, no glass, no pane
· 60 m drag groove · hatch mouth DARK, unlit, no door pane"
```

### D-H 🔴 AYNA ŞÜPHESİ (S25) — düzeltmeden önce TEŞHİS gerek

İki bulgu AYNI ANDA ters: yara izi SAĞ kaşta + göğse giden el SAĞ el.
İkisinin birden ters olması iki açıklamadan birini işaret eder:

```
A) Klip kurgu/export sırasında YATAY FLIP yemiş
   → kontrol: kaldırdığı ön kol hangisi? (prompt: SOL ön kol panele,
     SOL el göğse). Flip ise ön kol da ters görünür.
   → çözümü BEDAVA: kurguda geri çevir. Yeniden üretim gereksiz.
B) Kimlik gerçekten aynalı üretilmiş (seed/çapa sorunu)
   → S25 yeniden üretim + R1 çapasının kendisi kontrol edilir.
Sıra: önce A'yı tek kareyle test et; B'ye ancak A düşerse geç.
(Denetçi modellerin özne-solu/ekran-solu karıştırdığı da bilinen
vaka — karar tek kare insan gözüyle verilir, rapora güvenilmez.)
```

### D-I 🔴 ELDİVEN RİTÜELİ HİÇ ÜRETİLMEMİŞ (S22) — Ç7 kurulumsuz kalamaz

Gerçek S22-içerikli klipte eldiven HİÇ çıkmıyor; kadraj da makro değil
medium-wide. Ç7 zinciri (S22 kurulum → S80 eldiven düşer → S81 temas)
filmin omurgası — kurulumsuz final çalışmaz. Yeniden üretim
pazarlıksız. Prompta eklenecek vurgu:

```
The ONLY event of this shot is the glove ritual: at 2s the right
glove comes OFF at its wrist ring and hangs by its tether; from 4s
to 8s the hand is BARE — light olive skin, visible pores; at 8s the
glove goes back on. If the glove never leaves the hand, the shot
has failed. Framing is MACRO on the two hands — no wide framing,
no full figure.
```

### D-J 🔴 "TRANSMISSION" FİKRİ DALGA FORMU ÜRETTİ (S25) — Ders 13 sınıfı

"a transmission running" kavramı modeli ekolayzer/waveform UI'a itti —
okunur grafik yasağı delindi. D-A'nın kavram-versiyonu: **soyut fikri
adlandırmak, klişe görselini üretir.** Yeniden üretim dili:

```
The forearm panel shows ONLY slow sliding rectangular segments of
amber light, one of them pulsing evenly. No waveform, no equalizer
bars, no spectrum, no oscilloscope line, no rows of dots, no
interface, no text, no digits — abstract light only.
```

### D-K 🔴 "DİK DURAN GEMİ" = ROKET refleksi (S29)

"standing upright on the horizon" → model dik duran şeyi ROKET olarak
çizdi (silindir + burun konisi). Siluetin bütün anlamı "bizim geminin
ikizi" olmasıydı. Yeniden üretim dili:

```
The silhouette is the same boxy rectangular cargo hull as their own
ship — flat slab sides, narrow cockpit nose, twin aft bays — simply
STANDING on its stern. NOT a rocket: no cylinder, no nosecone, no
fins, no launch vehicle, no tower. Matte bone-grey, single tone,
windowless, lightless, motionless.
```

### D-L 🔴 GECE GENİŞ KADRAJDA FİGÜR ÜREMESİ (S30) — Bekçi ERKEN doğdu

Uzak sağ arka planda beyaz mühürlü figür belirdi. Ders 69 kurulumu
(kapak+iki figür+gece) kapatılmıştı ama BOŞ UFUK açık kalmış: geniş
gece kadrajı + iki sırt dönük figür de klon/figür üretiyor. Anlatı
bedeli ağır: Bekçi F5'te girecek — burada görünmesi filmin en büyük
kartını yakar. Negasyon şablonu (tüm geniş gece kadrajlarına):

```
The plain is EMPTY of figures except the two: nobody and nothing
stands anywhere on the ground, on the horizon or in the background
— no third figure, no distant silhouette of a person, no white
figure. Exactly two figures in the entire frame.
```

### D-M 🟡 IŞIK EKLEME REFLEKSİ + ÖLÇEK KİLİDİ İLK ÖLÇÜMÜ NEGATİF

- **Kapak sarı ışık saçıyor** (S21) ve **mast'ta parlayan slotlar**
  (S24) — Ders 3/29 sınıfı: model karanlık nesneye ışık ekliyor.
  "mouth dark and empty" yetmedi; yeniden üretimde: "the hatch mouth
  is BLACK, unlit — no door pane, no light inside, no glow" /
  "the mast is DARK bare metal — no lit slots, no glow, its only
  light the single dull amber tip point".
- **Ders 32 R3 ölçek kilidi ilk sahada TUTMADI** (S21: gemi bütün ve
  küçük). ⚠️ Şerh: üretimin eski prompt sürümüyle koşulmuş olma
  şüphesi var (D-G) — R3'ü gömmeden önce doğru sürümle bir koşu daha
  görülmeli. Doğru sürümle de batarsa Ders 32 zincirine "R3 başarısız,
  R4 gerek" kaydı düşülür.
- **S26-içerikli klipte lambalar açık** (kural: fazın en karanlık
  karesi, lamps OFF) — ikinci koşuda kendi satırına karşı yeniden
  değerlendirilir; batıyorsa yeniden üretim.

### D-N 🟡 EXTEND YALNIZ SON İKİ SAHNEDE ATLANDI (S29 · S30 = 8.0 s)

Sekiz sahne 10.0 s — A yolu uygulanmış; son ikisi native 8 s kalmış.
S30'da yürüyüş var → 0.8× retime YASAK (KİLİT 3), S29'da tilt var →
o da A yolu. İkisi de extend ile 10.00 s'ye tamamlanır; müzik ızgarası
ve 3:20–5:00 zaman haritası 10.0 s'ye hizalı.

---

## 4. RUBRİK İŞLEYİŞİ

- Revize kapı (75–105 s + ölçümlü segment haritası) ilk kullanımda
  çalıştı; eski kapı aynı dosyayı 87 s ölçümüyle reddetmişti. İki
  koşunun süre ölçümü tutmuyor (87 vs 96) — **modelin süre ölçümü
  rapor verisi değil, yalnız mod seçimi girdisidir.**
- İçerik-satır çelişki kuralı 5/5 misfile'ı yakaladı ve sessiz
  düzeltmeye kaçmadı — Faz 1 rotasyonundan çıkan tasarım kendini
  ikinci kez kanıtladı.
- DAMAGE FREEZE tablosu (F2'deki DAMAGE CLOCK'un dondurulmuş hali)
  amaçlandığı gibi çalıştı: dört işaretin yokluğunu sahne sahne verdi.
- FLAGS yine en değerli soruları üretti: dosya adlandırma hattı +
  aynalı seed şüphesi (→ D-H'de tek-kare testine çevrildi).
- Sahte pozitif şüphesi: "her scar on RIGHT" bulgusu denetçinin
  özne/ekran solu karışıklığı da olabilir — rubrik değişikliği
  gerekmiyor, karar insan gözüyle (D-H).

---

## 5. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ KURGU (bedava): reel'i doğru sıraya koy — 2↔3 takası,
     6/7/8 → 8/6/7 rotasyonu. Klip dosya adlarına sahne numarası yaz.
2. □ TEK KARE TESTİ (D-H): S25'te kalkan ön kol hangisi? Flip ise
     kurguda geri çevir; değilse S25 yeniden üretim listesine girer.
3. □ DOKÜMAN KONTROLÜ (D-G): F3 üretimi hangi prompt sürümüyle ve
     hangi çapa imajlarıyla koşuldu? Camlı delik + kızak + küçük gemi
     üçlüsü eski sürüm işareti. Cevaba göre yeniden üretim ya
     düzeltilmiş promptla ya da önce çapa üretimiyle başlar.
4. □ HASAR ÇAPASI KAPISI: R4/S19-END hasarlı gemi çapası üretilip
     doğrulanmadan hiçbir dış sahne yeniden üretilmez [D-G].
5. □ YENİDEN ÜRETİM (kırmızılar):
     S21  hasar + ölçek + karanlık kapak [D-G, D-M]
     S22  eldiven ritüeli, makro kadraj [D-I]
     S23  açık delik (cam yok) + hasar [D-G]
     S25  waveform temizliği [D-J] (+ D-H sonucuna göre ayna)
     S29  roket → kutu ikiz [D-K] + 10.0 s extend [D-N]
     S30  boş ufuk negasyonu [D-L] + hasar [D-G] + 10.0 s extend [D-N]
6. □ İKİNCİ KOŞUDA KARAR (şimdilik yeniden üretme):
     S24  mast ışıklı slotlar (YELLOW — karanlık metal diliyle
          birlikte değerlendirilir)
     S26  lambalar (gerçek klip kendi satırında ölçülmedi)
     S27  tek vuruş var mı (gerçek klip kendi satırında ölçülmedi)
7. □ Doğru sıralı + yeniden üretimli reel ile İKİNCİ KOŞU — 3.7
     skoru geçersiz, karşılaştırma tabanı ikinci koşudur.
8. □ Tutan prompt sürümlerini FAZ_03_IMDAT.md'ye işle.
```

---

## 6. F4+ VE SİSTEME TAŞINANLAR

```
① ROKET NEGASYONU        "dik duran gemi/kopya" öznesi olan her prompta
                         D-K bloğu. F4 tarla sahneleri tarandı: özne
                         "stone ship shapes" dilinde, dik-ikiz öznesi
                         yalnız S29/S30'da — F4 dosyasına şimdilik
                         dokunulmadı; F4 üretiminde ilk tarla çıktısı
                         roketleşirse blok oraya da girer.
② BOŞ UFUK NEGASYONU     geniş gece/alacakaranlık kadrajlarında D-L
                         bloğu — F4 şafak yürüyüşü (S31) ilk aday.
③ KAVRAM ADLANDIRMA      "transmission/signal/scan" gibi kavram adları
                         UI klişesi üretir [D-J, D-A sınıfı] — soyut
                         gösterge promptlarında kavram değil GEOMETRİ
                         yazılır (segment, nokta, çubuk).
④ MONTAJ PROTOKOLÜ       klip adına sahne numarası; mümkünse reel değil
                         MODE T (10 dosya) ile denetim [§1].
⑤ ÜRETİM KAPISI DİSİPLİNİ "X düzelmeden Y'ye başlanmaz" kapıları
                         atlanınca faz maliyeti ikiye katlanıyor —
                         F2 aksiyon 1 açıkken F3 koşuldu, sonuç: 10
                         sahnenin 6'sı yeniden üretim [D-G].
```

F2'nin bekleyen aksiyonlarıyla birleşik durum: `../FAZ_02_VURULMA/
FAZ_02_QA_DERSLER.md` §4 (S13/S14 çapa üretimi) hâlâ açık ve artık
F3'ün de ön koşulu.

---

> **Bu dosya ne zaman güncellenir:** D-H tek-kare testi sonuçlanınca,
> yeniden üretimler bitince ve doğru sıralı reel ile ikinci koşu
> raporu geldiğinde.
