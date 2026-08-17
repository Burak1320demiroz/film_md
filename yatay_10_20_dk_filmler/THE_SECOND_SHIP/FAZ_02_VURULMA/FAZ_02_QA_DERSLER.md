# 📚 FAZ 2 / VURULMA — QA DERSLERİ VE AKSİYON RAPORU

> Koşu: 07.08.2026 · Model: Gemini · Girdi: tek 100 s reel · MODE R
> Rubrik: `FAZ_02_QA_PROMPT.md` · Ham çıktı:
> `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP_FAZ02_HAM.md`
>
> **Skor 5.5/10 — ama ortalama yanıltıcı, dağılım iki uçlu:** kimlik 8,
> kostüm 8, klon 9, metin 9, teslim 10 / hasar 1, fizik 1, silah-ateş 1,
> kamera 2. **Kelimesi kelimesine yapıştırılan kilitler TUTTU; kompozisyon
> öncelikli (prior) hatalar tutmadı.** Bu fazın asıl bilgisi bu ayrımdır.

---

## 1. ÖNCE TUTAN TARAF — dünkü kilit geçişinin doğrulaması

| Kilit | Skor | Kanıt |
|---|---|---|
| Karışma kilidi (turuncu/teal + 13 cm) | 8/10 | "never swapped… exact height difference held" |
| Kimlik pasaportları (yüz sabitliği) | 8/10 | "faces hold remarkably well" |
| Figür sayımı / klon | 9/10 | iki-figür sahnelerinde sıfır klon |
| Metin yasağı | 9/10 | sıfır okunur karakter |
| Teslim hijyeni | 10/10 | kart/watermark yok, süreler tam |
| Kokpit zinciri | 6/10 | S12-S15-S16-S18 aynı mekân okundu |
| S15 (retime + soyut gösterge + flu yüz) | temiz | "nailed the brief" |

Sonuç: **prompt gövdesine gömülü, tekrarlanan, sayılı kimlik kilitleri
çalışıyor.** Batıran şey kilit eksikliği değil — modelin tür refleksleri.

---

## 2. BATAN TARAF — beş kök neden

### D-A 🔴 "LIKE GLASS" GERÇEK CAM ÜRETTİ — fazın en pahalı dersi

S13 promptu deliğin kenarını `clean, smooth and faintly pearlescent,
LIKE GLASS` / `glassy` diye tarif ediyordu (FAZ_02_VURULMA.md:447,504,555
— doğrulandı). Model "glassy edge"i **camlı lombar penceresi** olarak
çizdi: S14'te adam cama DOKUNUYOR, S19/S20'de delik kum akıtan oluğa
dönüşüyor. Ders 56/67 sınıfının yeni üyesi: **malzeme benzetmesi, malzemenin
kendisini üretir.** "Dalış" sözlüğü su üretmişti; "cam gibi" cam üretti.

```
YANLIŞ  its edge glassy, like glass
DOĞRU   its edge polished, faintly pearlescent
      + The hole is open and empty — no glass, no pane, no cover,
        no window. Black space reads through it.
```

✅ UYGULANDI: F3 ve F8 prompt dosyalarındaki 8 "glassy/like glass"
kullanımı "polished"a çevrildi; deliğin özne olduğu 5 prompta açık-delik
negasyonu eklendi (S21 dahil). F2'nin kendi dosyasına dokunulmadı —
S13/S14/S19/S20 yeniden üretilirken aynı düzeltme elle uygulanır ve tutan
sürüm dosyaya işlenir.

### D-B 🔴 ATMOSFER GİRİŞİ = ATEŞ TOPU refleksi (S17) + kıvılcım (S19)

KARAR 2'nin plazma dili ("glowing plasma sheath / dull orange heat")
yetmedi — model girişi Hollywood yangınına çevirdi, inişe kıvılcım ekledi.
Faz 1'in S10 dersiyle aynı sınıf: **"büyüyen/yanan ışık" kompozisyonunun
kendisi çekici.** Yeniden üretim dili:

```
The hull carries a thin rim of dull orange heat on its LEADING EDGES
only — a tight surface sheen, never a flame. Nothing trails, nothing
burns, nothing sheds. The heat never brightens across the shot; its
brightness at 10s equals its brightness at 0s.
```

### D-C 🔴 DARBE = KAMERA SARSINTISI refleksi (S12)

KARAR 3 cümlesi ("the camera never shakes; the cabin and the two bodies
do") rubriğin "en olası hata" tahminiydi ve aynen çıktı. Tek cümle
yetmiyor; yeniden üretimde çerçeve fiziksel bir çapaya bağlanır:

```
The camera is BOLTED to the cockpit floor: the frame edges never move
relative to the window frame and console edges. What moves is inside
the frame — the two bodies snap against their harnesses, loose straps
swing once and stop. Zero lens shake, zero handheld wobble, zero blur.
```

Bu da tutmazsa kurgu kurtarması: sarsıntı beat'i S12'den çıkarılır,
darbe yalnız ışık süpürmesi + gövde refleksiyle anlatılır (Ders 69
mantığı: prompt değil sahne tasarımı).

### D-D 🔴 DİYALOG = YÜZ YÜZE DÖNME refleksi (S16)

"No one turns to the other" yazılıydı; ikisi de döndü. Diyalog önceliği
shot-reverse çekiyor. **F3-F8 tarandı: kırılgan desen ("dönmeden konuş")
oralarda YOK** — S23/S58/S63/S69 zaten baş-çevrik veya dönüşü planlı
tasarlanmış. Ders yeni üretimlere: dönmesiz diyalog sahnesinde bakış bir
NESNEYE kilitlenir:

```
Her eyes stay locked on the amber band on her own console for all ten
seconds; his eyes stay on his own display. Their gazes never meet;
neither head turns toward the other at any second.
```

### D-E 🔴/📋 KONUŞMA KİLİDİ İKİ YÖNDE DE ARIZALI ÇIKTI — biri üretim, biri rubrik

- S12: adam bağırıyor (NO SPEECH sahnesi) → **gerçek üretim hatası**,
  yeniden üretim.
- S18: "ağız oynamıyor" RED'i → **rubrik hatasıydı.** Tasarım ağzı zaten
  gizliyor ("mouth angled away") ve ses post'ta — görünür dudak hareketi
  hiçbir zaman ZORUNLU olamaz. ✅ Ders 63 uygulandı: SPEECH LOCK tek
  yönlü hâle getirildi ("absence of lip movement is NEVER a finding") ve
  S18 satırına GRADING NOTE eklendi. Faz 3-8 rubrikleri bu tek yönlü
  kilitle doğacak.

### D-F 🟡 DİĞERLERİ

- **S20 kum şelalesi** — "hiçbir şey olmaz" sahnesine model olay icat
  etti (rubrik bunu da tahmin etmişti). Kök neden D-A'ya bağlı: delik
  oluk gibi okununca kum aktı. Açık-delik düzeltmesiyle birlikte yeniden
  üretilir.
- **S19 toz = duman** — Ders 12/39 sınıfı sürüyor; ağır toz olayı olan
  sahnede prompt kilidi yetmiyor. Yeniden üretimde toza sayı verilir:
  "each dust plume collapses back to the ground within 2 seconds".
- **Kızak (skid) iniş takımı** — üç bacak yerine kızak çizildi, çöken
  bacak okunmadı. F3+ zeminde duran gemi sahneleri "collapsed right leg"
  yazıyor; yeniden üretimlerde "three legs, never skids" eklenir.
- **S17 yatış tutarsız** — 4° sabit yatış giriş boyunca tutmadı
  (pitch/bank). D-B ile birlikte çözülür.

---

## 3. RUBRİK İŞLEYİŞİ

- İlk deneme kapıda düştü ("durations: unknown" — dosya işlenmemişti),
  ikinci denemede model süreyi ölçtü ve **MODE R'yi kendisi doğru seçti.**
  Üç-modlu kapı çalışıyor.
- DAMAGE CLOCK tablosu tam amaçlandığı gibi çalıştı: delik-yatış-bacak-oluk
  zincirinin nerede koptuğunu sahne sahne verdi.
- FLAGS bölümü yine en değerli soruyu üretti: "prompt 'window/porthole'
  mu diyor?" — hayır, ama "like glass" diyordu; soru düzeltmeyi buldurdu.
- Bir sahte pozitif çıktı (S18) ve rubrik yamalandı (§2 D-E).

---

## 4. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ S13 + S14 yeniden üret — D-A dili (polished + açık-delik negasyonu)
     → S13 çıktısı S21+ yüzey sahnelerinin delik ÇAPASIDIR; bu ikisi
       düzelmeden F3 üretimine BAŞLANMAZ
2. □ S17 yeniden üret — D-B dili (leading-edge heat, sabit parlaklık)
3. □ S12 yeniden üret — D-C dili (bolted camera) + NO SPEECH
4. □ S19 + S20 yeniden üret — açık delik + toz sayısı + "no skids,
     three legs, right leg collapsed"
5. □ S16 yeniden üret — D-D bakış çapası
6. □ S11 opsiyonel — taban bloom'u YELLOW, kurguda kırpılabilir
7. □ Yeniden üretimler bitince reel'i YENİDEN KOŞ; 5.5 skoru geçersiz
8. □ Tutan prompt sürümlerini FAZ_02_VURULMA.md'ye işle
```

---

## 5. FAZ 3–8'E TAŞINANLAR — ✅ bu koşuyla birlikte UYGULANDI

```
① CAM DİLİ TEMİZLİĞİ      F3 + F8'deki 8 "glassy/like glass" → "polished";
                          delik özneli 5 prompta "no glass, no pane, no
                          cover, no window" negasyonu eklendi
② TEK YÖNLÜ KONUŞMA       Faz 3-8 rubrikleri SPEECH LOCK'un tek yönlü
   KİLİDİ (rubriklere)    hâliyle yazılacak (dudak yokluğu asla bulgu değil)
③ BAKIŞ ÇAPASI            yeni yazılacak dönmesiz diyalog sahnelerinde
                          bakış nesneye kilitlenir (D-D şablonu)
④ ATEŞ/SARSINTI SINIFI    F3-F8'de atmosfer girişi yok; ağır toz sahneleri
                          (S21 iniş sonrası, S74+ girdap) yeniden üretim
                          notu olarak: toza saniye, ışığa sabit parlaklık
```

Faz 1'in bekleyen aksiyonlarıyla birleşik durum: `../FAZ_01_TRANSIT/
FAZ_01_QA_DERSLER.md` §4 hâlâ geçerli (dizilim doğrulaması + S9/S10).

---

> **Bu dosya ne zaman güncellenir:** yeniden üretim sonrası ikinci koşu
> raporu geldiğinde ve tutan prompt sürümleri FAZ_02_VURULMA.md'ye
> işlendiğinde.
