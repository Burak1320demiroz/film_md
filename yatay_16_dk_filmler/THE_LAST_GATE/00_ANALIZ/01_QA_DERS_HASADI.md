# 🌾 THE_LAST_GATE — QA VE DERS HASADI

> Kaynak: `00_OKUMA_CIZELGESI.md`'nin 96 satırlık kilit sütunu (96 ✅ · 2 meşru "—" ·
> 5 kapalı tablo). ⛔ Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ girer [D45].
> Tavan: film başına 20 ders kilidi (`prompt_kontrol.py` ㉕) — tablo PLAN'da.

## 1. DERS KİLİTLERİ — 20 satır, PLAN `## 🔒 DERS KİLİTLERİ`'ne indi

Ölçülmüş kapsama oranlarıyla birlikte orada durur. Buraya iki not:

```
⭐ HASADIN EN PAHALI SATIRI: D138 + ASTRONOT_DONANIM §3 birlikte okundu ve
  sahibin "özgün rozetler korunur" isteğini SİLMEDEN çözdü. İlk çözümüm
  ("boş kabartma") isteği küçültüyordu; deponun kendi metinsiz amblem dili
  (textless + tek motif + embossed embroidery, ölçülen risk "çok düşük")
  isteği TAM karşılıyor. Kayıt: PLAN §Rozet Bible · SAPMA 1.
⭐ İKİNCİ EN PAHALI: D169 mikrogravitede İPTAL OLMUYOR. Yerçekimi AĞIRLIĞI
  kaldırır, KÜTLE ve ATALETİ kaldırmaz — efor fiili taşıyan 11 klipte gövde
  kanalı aynı TIMELINE satırına yazıldı (`her grip tightening on the rail as
  the mass comes with her`).
```

## 2. QA ARIZALARI — ölçülmüş kayıtlardan bu filme düşenler

| kaynak kayıt | ölçülmüş arıza | bu filmde ne yapıldı |
|---|---|---|
| **THE_STOLEN_SKY** PART 2 · 02:53 🔴 | kapının uzaylı gövdesinden geçmesi | K34 · K60 negatifine: *"The panel never passes through a body and no body passes through the panel — the panel closes in clear space."* |
| **THE_STOLEN_SKY** PART 4 · 01:44 🔴 | kopuk eldiven ve kaskın bedensiz süzülmesi | K13 · K54 negatifine: *"No detached glove, helmet, boot or limb drifts anywhere in frame — every worn item stays on the body wearing it."* |
| **THE_STOLEN_SKY** PART 4 · 03:00 🔴 | mekik-roket **kütlesiz** çarpışması | K10 · K80 · K90 negatifine kütle cümlesi: *"keeps its full mass… no weightless flick, no rubbery deflection"* |
| **THE_STOLEN_SKY** PART 3 · 02:00 🔴 | vurulan figürün sonra ayakta olması | bu filmde **kimse vurulmuyor**: atış panele/sipere gider; muhafızlar K34 · K60'ta kapakla ayrılır ve K57'de ADI KONULMUŞ yan yoldan döner |
| **THE_LAST_SPAN** S8/S9 politika reddi | `"crowd of figures"` + kaçan insan | kalabalık **0 klip**; insan kütlesi her klipte sayılı ve ayrı (en büyük kadraj 8) · panik/koşma 0 klip |
| **THE_SINKING_STAKE** red #15 | tek kişide 7 kimlik özniteliği | boy · ten · saç · yaş **0/184**; Veyr'in boyu göreli |
| **COLD_BURN** S8 red #2 | insansız sahne + uzun NEGATIVE | 31 insansız klipte negatif bloğu **< 900 karakter** |
| **LOSS_OF_LIFT** 🔴 8. vaka | kurgunun sonuna **başlık kartı** | K96 negatifine: *"No title card, no end card, no logo, no credit roll…"* |
| **THE_BENT_GRASS** ⑦ 10,0/10 | dokuz hücrenin dokuzu `no in-scope source` | SPEC E'ye satır: ⑬ promptsuz KESİK kalır; 184 prompt bu koşuyu mümkün kılar |
| **THE_HARD_DOCK** 12 mercek | yanaşmada iki gövdeli kare = tek riskli vuruş | V1–V6 seti S03'e birebir; iki gövdeli V3 karesi filmde **2 kez** (K06 · K92) |
| **KRONOS_SON_SINYAL** 🅑 %93 | 96 promptun hiçbirinde `AUDIO:` yok | 92/92 video promptunda AUDIO ilk cümlesi BİREBİR |
| **BENI_HATIRLAMA** 2 blocker | yerçekimi TARİFLE yazıldı, ekranda 2,9× tutarsız | tek rejim SAYIYLA değil ADIYLA sabit: "continuous microgravity", 92/92 birebir |

## 3. RED DEFTERİ SINIFLARI — bu filmin dokunduğu beş sınıf

```
#2  YR   insansız sahne + uzun yokluk listesi  → 31 klipte kısa negatif     ✅ kapalı
#8  PK   "crowd of figures" + kaçan insan      → kalabalık 0 klip           ✅ kapalı
#11 PK   dead/body/corpse negatifte bile tetikler → sözlük 0/184            ✅ kapalı
#13 PB   kompozisyon reddi (iki ön kol + makro + yüzsüz izolasyon)
         → K19 iki eldiven + CU: yüzsüz DEĞİL, iki ayrı giysi geometrisi
           kadrajda; yine de ⚠️ İZLENECEK (SPEC yanlış-pozitif duvarı dışı)
#15 PK   yedi kimlik özniteliği = "public figure"  → 0/184                  ✅ kapalı
⛔ ÇÖZÜLMEYEN SINIF YOK: bu filmde bedenden bir şey ÇIKARILMIYOR (#3 PB tetiklenmez),
  kask çıkarma 0 kare, ceset/yara 0 kare.
```
