# 🌲 THE UPWARD FALL — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı · **master ÖLÇÜLDÜ** ✅
> **Koşu:** 04.09.2026 · **sekiz mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES ·
> 📖 HİKAYE · 🖼️ ARKA PLAN · ⚖️ FİZİK · 🎯 AKSİYON · 💪 EFOR) —
> **sekizi de tek Gemini oturumunda, sekizi de mod V.**
>
> ⛔ **HİÇBİR SKOR SATIRI T1/T4/T6/T7/T8'E GİRMEDİ.**
> ① SPEC kapısı: `THE_UPWARD_FALL_QA_SPEC.md` **VARDIR** *ve* mod-D paketi
> `QA_PROMPTLARI/FILME_OZEL/THE_UPWARD_FALL/PAKET_1..8` **VARDIR** — D165'in
> çözümü UYGULANMIŞTI. Operatör yine çıplak rubriği yapıştırdı → koşu
> TEKRARLANIR [D129]. **SPEC yazılmış olduğu hâlde mod V koşulan film: 12.**
>
> ⭐ **AMA BU KAYIT ASKIDA DEĞİL.** ⑪ ÖLÇÜM KAPISI koşuldu; kilit defterindeki
> maddelerin çoğu **kareyle** kapandı. Aşağıdaki 🔴 bulguların hiçbiri bir
> rapordan gelmiyor — hepsi ÖLÇÜMDEN ve karelerden geliyor, ve
> **sekiz merceğin sekizi de bunların sekizini de kaçırdı.**

---

## 📦 MALZEME

```
MASTER:   /Users/dai/Downloads/the upward fall (1).mp4
          225,11 s · 3840x2160 · 30 fps · AAC 48 kHz stereo · 339,5 MB
İKİZ:     /Users/dai/Downloads/the upward fall.mp4 — AYNI SÜRE (225,11 s),
          1920x1080. Aynı kurgunun iki çözünürlüğü; ⑪.0 kimliği 4K'dan alındı.
KART:     220,13 – 225,11 s  ·  4,98 s  ·  BAŞLIK KARTI "THE UPWARD FALL"
          (freezedetect: 220,13'ten dosya sonuna kadar donuk)
          ⛔ SPEC B: `SCREEN TEXT: 0,0 saniye` · `title card: none`
          Kart hem SAYIMIN hem SÜRENİN dışında tutuldu [D93 · D120].
GÖVDE:    220,00 s = 22 klip × 10,0 s  (kesme ızgarası: 10,03 · 40,03 · 50,03
          · 60,03 · 70,07 · 80,07 · 100,07 · 110,07 · 120,07 · 130,07 · 140,10
          · 150,10 · 160,10 · 190,10 · 200,10 · 210,13 · 220,13 —
          20/30/90/170/180 sn'deki kesmeleri scene>0,3 görmedi, ızgara
          10 s katıdır ve ⑨ kapısı max |Δ| = 0,0 s ile doğruladı)
MERCEK:   ① 4,8 · ② 5,7 · ③ — · ④ 6,0 · ⑤ 5,1 · ⑥ 6,0 · ⑦ 9,5 · ⑧ 1,6
          (düzeltilmiş ortalamalar; ①④⑥⑧ TABLOYA GİRMEZ [D129] ·
           ⑦ 🚨 GEÇERSİZ [D161] · ②⑤ ⚠️ ŞARTLI · ③ sayı taşımıyor)
```

---

## §⑪ ÖLÇÜM KAPISI — `olcum_kapisi.sh` · 04.09.2026 · **KOŞULDU**

| ölçüm | değer | SPEC ne diyor | sonuç |
|---|---|---|---|
| süre | **225,11 s** | 249 s | ⛔ **−23,9 s** |
| gövde süresi (kartsız) | **220,00 s** | 249 s | ⛔ **−29 s ≈ 3 klip** |
| sahne | **22** | 25 | ⛔ **−3 sahne** |
| ızgara | **10,0 s hook + n×10,0** | 9 s hook + n×10 | ⚠️ hook 9 değil **10** |
| kesme | 21 (sahne↔sahne) | 24 | ⛔ 3 eksik |
| ses kanalı | **VAR** — AAC 48 kHz stereo | sesli (5 diegetik katman) | ✅ kanal var |
| sessizlik (−50 dB / 0,3 s) | **TEK ARALIK YOK** | S21 MUTLAK SESSİZLİK planlı | ⛔ planlı sessizlik YOK |
| loudness | **I = −16,1 LUFS · Peak 0,0 dBFS** | −14 LUFS / −1,0 dBTP | 🔴 **İHRAÇ KUSURU** |
| köşe testi | **FİLİGRAN VAR** — sağ altta cyan "▷", 7/7 örnek (0→210 s) | — | 🔴 **TESLİM KUSURU [D150]** |
| kuyruk kartı | 220,13 → SON | ekran metni 0,0 s | 🔴 **[D70 · D72]** |

```
⛔ ÜÇ TESLİM KUSURU. Bu master master DEĞİLDİR:
   ① üretici filigranı 225 saniyenin 225'inde duruyor
   ② kuyrukta 5 saniyelik yanan başlık kartı var
   ③ −16,1 LUFS / 0,0 dBFS — hem hedefin altında hem tepede kırpıyor
   Üçü de rapor bulgusu DEĞİL, TESLİM kusurudur; master yeniden ihraç
   edilmeden hiçbir mercek yeniden koşulmaz.
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 04.09.2026 · **8 rapor**

```
--olcum-kesme 21 --olcum-sahne 22 --hook 10 --klip 10

🚨 GEÇERSİZ  ⑦ AKSİYON     iddia n=7 Σ=66 ort=9,4 │ hücreler n=8 Σ=76 ort=9,5
                            ARİTMETİK FABRİKE — hiçbir hücre kümesi 66'yı üretmiyor
⛔ TEKRAR    ① KARE        n=8 Σ=47 → 4 hücre `—` [D131] → n=4 Σ=19 ort=4,8 · D129
⛔ TEKRAR    ④ HİKAYE      n=9 Σ=54 ort=6,0 · D129
⛔ TEKRAR    ⑥ FİZİK       n=9 Σ=54 ort=6,0 · D129
⛔ TEKRAR    ⑧ EFOR        n=7 Σ=11 ort=1,6 · D129 · PREMISE REGISTER yalnız ORTAM [D166]
⚠️ ŞARTLI   ② DEVAMLILIK  n=3 Σ=17 ort=5,7 (5,6 yazılmış) · Counter N/A ↔ SPEC [D134]
⚠️ ŞARTLI   ⑤ ARKA PLAN   n=9 Σ=46 ort=5,1
✅ GO        ③ SES         n=0 — sayı taşıyan hücre YOK

TOPLAM 8 · 🚨 1 · ⛔ 4 · ⚠️ 2 · ✅ 1
tam çıktı: RAPOR_KONTROL/RAPORLAR/THE_UPWARD_FALL_20260904_RAPOR_KONTROL.md
```

**Betiğin yakaladığı yapısal kusurlar:**

```
① SEVERITY TALLY ≠ YAZILI ETİKETLER — 8 raporun 4'ünde [D161]
   ① 0/3/0 ↔ 1/4/0 · ⑤ 0/3/6 ↔ 0/3/1 · ⑥ 1/3/5 ↔ 1/2/1 · ⑦ 0/0/2 ↔ 0/0/0
   Verdict'ler bu tally'lerden türetildi → kesme/REGENERATE hükmü UYGULANMAZ.
② "no in-scope source" + SAYI — ①'de dört hücre [D131]
   Scale & Physics · Camera · Lighting · Particles hepsi 7/10 yazıp
   aynı hücrede "no in-scope source" diyor → dördü de `—`, ortalama 5,8 → 4,8.
③ ⑦'nin ARİTMETİĞİ FABRİKE: n ve Σ ikisi de tabloyla tutmuyor.
④ ⑨ IZGARA OTURUYOR — 21 kesme, max |Δ| = 0,0 s → zaman kodları uydurulmamış [D115].
```

---

## §③ KİMLİK KAPISI [D105] — **ATTRIBUTED ✅** (4 çapa)

| # | çapa | rapor ne dedi | belge |
|---|---|---|---|
| 1 | vuruş | "~40 floating white cloth strips" (1:10) | SPEC C `PARÇACIK: S7'de tam 40 parça` · plan S7 ⭐VİRAL #1 · FORTY |
| 2 | sayısal | 25/25 sahnede tam 1 insan, replik 0 | SPEC A `DIALOGUE LINES: 0` · `İNSAN: tam 1` |
| 3 | vuruş | "tying green vine around canister" (2:20) | plan S14 THE VINE |
| 4 | vuruş | "cuts vine on log with a rectangular tool" (3:10) | plan S22 FIVE CUTS · "grey hand tool, single straight cutting edge, ribbed grip" |

⛔ Kuyruktaki başlık kartı çapa olarak KULLANILMADI (yasak).

---

## §④ KURGU KAPISI — **ÖN KOŞU** · 🔴 **KUYRUKTA FİNAL YOK**

```
a) klip sayısı  22  ≠ 25  ⛔
b) süre         220,0 s (kartsız) ≠ 249 s · Δ = −29 s ⛔
c) sıra         şerit 1111…  → ⛔ ÖLÇMEDİ, GEÇTİ DEĞİL [D163]
                insansız sahne 0/22 → çözünürlük 0 → sıra ekseni
                YALNIZ ⑪'in sahne ızgarasından okundu
d) FİNAL VURUŞ KANITI [D141]  🔴 **BULUNAMADI**
```

**Δ okuması [D121] — kuyruğa bakıldı, film oradan eksik:**

```
SPEC B · S24 (239-249 s): "köprü kalkar, dört uzuv onu alır; ön planda
avuçtaki parça AŞAĞI basar" — DORUK + KAPANIŞ + TWIST + kapak karesi.

ffmpeg -ss 211/214/216/218/219 → BAKILDI:
  teslimin son sahnesi (210-220 s) = adam bir toprak hendeğin yanında
  İNCE ÇAMLIK içinde YERE OTURMUŞ, açık avucunda düz gri bir levha;
  arkada ~30 m'de PARK ETMİŞ BİR ARAÇ duruyor.
  · köprü YOK · dört uzuv YOK · yükselme YOK · parça avucu ÇÖKERTMİYOR
  · kurulum B (50mm · MS · göz hizası 1,2 m) değil, alçak oturma planı
  · mekân 40 m'lik pürüzsüz gövdeler değil, ince çam ormanı

→ 🔴 FİLMİN PLANLI DORUĞU (S24) TESLİM EDİLMEDİ. Twist üretilmemiştir.
→ Film boyu kategoriler (Yapı · Duygu Yayı · Final · Tutundurma) SAYI TAŞIMAZ.
```

**Kalan iki eksik klip:** ızgara↔harita eşlemesinde `S17 THE GAP` (üst açı,
40 m'lik yarık) ve `S18 THE LIGHT ACROSS` (EWS, karşı kıyıdaki ışık) yuvalarına
oturan blok YOK. ⬜ AÇIK — kesin atama için S16-S20 blokları kare kare izlenir.

**DÖNGÜ KANITI [SPEC B] — 🔴 KIRIK:**

```
ilk kare (1 s):   40 m'lik pürüzsüz gri-yeşil gövdeler · KAHVERENGİ lif zemini
                  · diz çökmüş · açık avuç · parça yükseliyor
son kare (218 s): İNCE ÇAM gövdeleri · GRİ/KÜL zemin + hendek · park etmiş araç
                  · oturmuş · açık avuç · levha duruyor
→ jest tuttu, DÜNYA tutmadı. Loop kompozisyonla kurulacaktı; iki kare iki
  ayrı ormanda geçiyor. Ayrıca arkasına eklenen kart döngüyü zaten öldürmüştü.
```

---

## §⑤ ÇAPRAZ SAYIM KAPISI [D107] — parti AYAKTA, şerit sapması var

```
KESME:  8/8 mercek 21 · ölçüm 21 → ✅ eksen doğrulandı
SAHNE:  ölçüm 22 · ② ⑧ ① 22 · ④ ⑤ ⑥ ⑦ 21 → ölçüm hakem, parti ayakta [D125]
REPLİK: 7 mercek "none" · ölçüm: replik 0 ✅ (ama ses VAR — aşağıya bak)
ŞERİT:  çoğunluk `111111111111111111111` (21) · sapan ② ⑧ ① (22)
        ⭐ ÖLÇÜM SAPANLARI DOĞRULUYOR: sahne sayısı 22'dir.
        → D173'ün tam tersi vaka: çoğunluk yanlış saydı, azınlık doğru.
SUSKUNLUK [D162]: 🚨 **KAPI HİÇ ATEŞLENEMEDİ** — film boyu süren bir ihlal
        (filigran, 225/225 saniye) VARDI ve HİÇBİR mercek iddia etmedi.
        Kapı "biri söyledi, sahibi sustu mu?" diye sorar; sekizi birden
        susunca kapının sorusu yoktur. → yeni ders adayı, aşağıda.
```

---

## §② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — 11 madde · **9'u KAREYLE KAPANDI**

| # | ne dedi / ne ölçüldü | hangi kilit | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | filigran: sağ altta cyan "▷", 7/7 örnek | SPEC B `SCREEN TEXT 0,0` · negatif "no watermark" (25/25 promptta) | `kose_*.png` + 6 kare | 🔴 **FİLM SAPTI** (teslim kusuru) |
| 2 | kuyrukta 4,98 s başlık kartı | SPEC B `title card: none` | `son_kare.jpg` | 🔴 **FİLM SAPTI** |
| 3 | kartın kostümü: kahverengi yıpranmış ceket + baloncuk kask + aynalı vizör | SPEC C `MODERN MAT SİYAH · vizör sıfır ayna` | `son_kare.jpg` | 🔴 **FİLM SAPTI** — kart KAPAK görselidir, filmin kostümü değil |
| 4 | 195-199 s: **ÇIPLAK ÖNKOL** — bilekten yukarısı deri, sadece eldiven var | SPEC C sızdırmaz giysi · 3,2 atm solunamaz · kask kapalı 25/25 | `kol_195..198.jpg` | 🔴 **FİLM SAPTI** — ① rubriğinin SEAL COUNT maddesi ("report any bare skin") **hiç işletilmedi** |
| 5 | 186 s: canlı **İKİ sütun uzuv**, tabanları kütüğe/zemine BASIYOR | SPEC C `ANATOMY LOCK: 0 bacak · 0 adım` · plan S21 "one single limb … nothing touches the ground" | `q_canli.jpg` | 🔴 **FİLM SAPTI** |
| 6 | zemin: 0-160 s KAHVERENGİ lif · 160-220 s SOLUK GRİ/KÜL | promptun WORLD bloğu "deep dry mat of fallen fibre" ↔ LIGHT bloğu "the **pale grey floor**" | grid10s.jpg | 🔴 **FİLM SAPTI** — ama sebebi PROMPTUN KENDİ İÇ ÇELİŞKİSİ (aşağıda ders) |
| 7 | son sahnede ~30 m arkada PARK ETMİŞ ARAÇ | plan S18: araç ışığı **400 m**, karşı kıyıda, "not the brightest thing in frame" | 216 s karesi | 🔴 **FİLM SAPTI** — umut nesnesi yanlış sahnede ve yanlış ölçekte |
| 8 | yarık: ~2 m derinlikte toprak hendek | plan S17/S20: **40 m genişlik**, tabanı görünmez | 216 s karesi | 🔴 **FİLM SAPTI** (ölçek çöküşü) |
| 9 | ses: LUFS −16,1 / peak 0,0 dBFS, sessizlik aralığı YOK | ihraç kilidi −14 / −1,0 · S21 mutlak sessizlik | ebur128 + silencedetect | 🔴 **FİLM SAPTI** |
| 10 | ②: "kanister ölçeği el boyundan gövde boyuna atlıyor" (0:50↔1:40) | SPEC C `kap = önkol boyu` | ⬜ 55 s ve 105 s blokları kare kare | ⬜ **AÇIK** |
| 11 | ⑤: "1:50'de gövdeye saplı BALTA, 2:00'de yok" | planda balta YOK | ⬜ 155 s bloğu kare kare | ⬜ **AÇIK** |

⛔ **10 ve 11 AÇIK olduğu için ② ve ⑤'in skorları ŞARTLI kalır ve o iki
bulgudan ders yazılmaz.** 1-9 kareyle kapandı → onlardan ders yazılabilir.

---

## §⑩ ÖNERME KAPISI [D87 · D116 · D130] — **düşen bulgular**

| bulgu | getiren | planda kaynağı | karar |
|---|---|---|---|
| "sudden ash/snow BIOME — geography break" | ④ ⑤ ⑥ | prompt LIGHT bloğu 25/25 sahnede "the **pale grey floor**" yazıyor | ⚠️ **YARIM DÜŞER**: biyom değişimi değil, promptun iki zemin cümlesi. Bulgu **prompta** taşınır, filme değil |
| "a knife appears with no established source" (⑦ OPEN THREAD) | ⑦ ④ | plan S22 promptu: "a plain grey hand tool, 22 cm, single straight cutting edge, ribbed grip" — YAZILI | ✅ **DÜŞER** — planlıdır |
| "inverted gravity is inconsistent / TWO GRAVITIES" | ⑥ | SPEC C `NOVUM: 0,60 m/s küçük parça · 0,35 m/s büyük kütle` — İKİ hız PLANLI | ⚠️ **KISMEN DÜŞER**: iki farklı hız kural, sapma değil. Ayakta kalan tek bulgu **L7 sabit hız / sıfır ivme** |
| "protagonist risks nothing, no cost" (④ Tema 6/10) | ④ | SPEC A `CENTRAL CHOICE S22 · bedel: dönüş yolu · kayıp S24'te görülüyor` | ⚠️ **AYAKTA ama sebebi başka**: bedel S24'te gösterilecekti, **S24 teslim edilmedi**. Bulgu doğru, teşhisi yanlış |
| "the ending stops, no peak located" (④) | ④ | S24 planlı doruk | ✅ **AYAKTA ve ⑪ ile doğrulandı** — final sahnesi YOK |
| "no audio at all" (③ + 7 mercek) | 8/8 | ölçüm: AAC 48 kHz, −16,1 LUFS, sessizlik aralığı yok | 🚨 **RAPOR UYDURDU** [D137'nin 5. vakası] |
| "watermark / edges" | — | hiçbir mercek yazmadı | 🚨 **HİÇ GÖRÜLMEDİ** [D150'nin 3. vakası] |

**⑩ sonrası toplam:**

| mercek | raporun toplamı | ⑩ sonrası | ayakta hücre | T tablosu |
|---|---|---|---|---|
| ① KARE | 5,8 | **4,8** | 4 | — (D129) |
| ② DEVAMLILIK | 5,6 | **5,7** | 3 | — (⬜ AÇIK madde) |
| ③ SES | — | **—** | 0 | — (ses ekseni ÖLÇÜLMEDİ) |
| ④ HİKAYE | 6,0 | **6,0** | 9 | — (D129) |
| ⑤ ARKA PLAN | 5,1 | **5,1** | 9 | — (⬜ AÇIK madde) |
| ⑥ FİZİK | 6,0 | **6,0** | 9 | — (D129) |
| ⑦ AKSİYON | 9,4 | **—** | — | — (🚨 fabrike aritmetik) |
| ⑧ EFOR | 1,6 | **1,6** | 7 | — (D129) |

⛔ **SEKİZ MERCEĞİN SEKİZİ DE TABLOYA GİRMEZ.**

---

## §⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108 · D159]

| gözlem | hangi raporlarda | sahibi | puanı kim taşıyor |
|---|---|---|---|
| 3:10-3:11 el/alet füzyonu | ① ② ⑧ (birebir aynı cümle) | ① | ① · 🚨 **KOPYA ŞÜPHESİ** [D159]: 3 raporda aynı saniye + aynı fiil, tek oturum |
| kanister ölçek sıçraması | ② ⑦ ⑧ | ② | ② · ⬜ AÇIK |
| kül/kar biyomu | ④ ⑤ ⑥ | ⑤ | ⑩'da yarım düştü (prompt kusuru) |
| canlının kayması/adımı | ① ⑤ ⑥ ⑦ | ⑤ | ⑤ · ölçümle FİLM SAPTI'ya çevrildi (madde 5) |

---

## 🎯 ÜÇ SATIRLIK SONUÇ

```
1. FİLM: planın 25 sahnesinden 22'si teslim edildi; eksik üçünün biri
   S24 — DORUK + TWIST + KAPAK KARESİ. Film bitmedi, DURDU. Üstüne üç
   teslim kusuru (filigran · kart · LUFS) bindi. → yeniden ihraç + S24
   (ve S17/S18) üretimi; sonra sekiz mercek MOD D yeniden koşulur.
2. QA: sekiz merceğin sekizi de mod V koştu — paket HAZIRDI. Sekizi de
   filigranı, çıplak önkolu, bacaklanan canlıyı, kırık döngüyü ve var olan
   ses yatağını kaçırdı. Bu partiden ÖLÇÜLMÜŞ bilgi çıktı, RAPOR bilgisi değil.
3. SİSTEM: üç ders bu koşudan doğdu (aşağıda) ve üçü de ALETE iner —
   D137 · D150 · D165'in tekrar sayacı da arttı.
```

---

## 📎 KANIT DOSYALARI (oturum scratchpad'i — kalıcı değil)

```
sahne_izgarasi.jpg · grid10s.jpg  22 sahnenin ortası, ızgara sırasıyla
son_kare.jpg                      kuyruk kartı (kapak görseli + yanan başlık)
kose_SA/SU/SoA/SoU.png · q_filigran.png   filigran şeridi, 7/7 örnek
kol_195..198.jpg                  çıplak önkol, dört kare
q_canli.jpg                       canlının iki bacağı, tabanlar zeminde
loop_cift.jpg                     ilk kare ↔ son kare, yan yana
kuyruk.jpg                        191-219 s, dokuz kare — final yok
```
