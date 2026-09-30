# 🧩 THE_STILL_SWARM — prompt hata analizi

```
FORMAT      yatay 2 dk · 14 sahne · ızgara sahne(n) = n × 10 s (hook 10 s)
HAM RAPOR   8/8 geçerli · BULGU 25 → tekil 25
HÜKÜM       🅐 12 · 🅑 11 · 🅒 1 · 🅓 1      🅑/(🅐+🅑) = %48
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 14/14: sayı · temas · giysi · bloom · metin · efor · g-ad · filigran · kamera
  KISMİ: SES 1/14 · dış-ses 10/14 · parçacık 2/14
  ⛔ HİÇ YOK: g-sayı
  bulgulu sahnelerde eksik: SES 1/10 · dış-ses 7/10 · parçacık 2/10 · g-sayı 0/10
```

---

## 🅑 SINIF 1 — PARÇACIK CÜMLESİ 14 SAHNENİN 12'SİNDE YOK · 2 🔴 · 4 🟠 ⭐

| S | bulgu |
|:--:|---|
| S10 🔴 | *Background debris particles are entirely **static/frozen*** |
| S10 🔴 | *Surrounding debris frozen in space* |
| S05 🔴 | *Gas emission freezes into static 2D plane* |
| S01 | *Floating panels lack continuous momentum* |
| S05 | *Gas spray exhibits atmospheric aerodynamic swirling in zero-atmosphere vacuum* |
| S02 | *Floating panels exhibit texture swimming* |

**Promptta ne yazıyordu:** `particles obey … continuous momentum, never hovering`
kalıbı **14 sahnenin yalnız 2'sinde** var — ve altı bulgunun altısı o ikisinin
dışında. Filmin adı "durgun sürü", olayın tamamı **yüzen paneller**; yani
parçacık/serbest cisim davranışı bu filmin **ana malzemesi** ve kilitsiz.

**Hüküm 🅑 ×6.** Yazım kuralı: negatif çekirdek seçmeli değildir; ayrıca filmin
**ana malzemesi** olan davranış pozitif gövdede de sayıyla yazılır
(`each panel keeps a slow constant drift of about one panel-width every four seconds`).

## 🅑 SINIF 2 — YERÇEKİMİ/ORTAM SAYISI YOK · 2 🟠

S11 (*"L2 push yields zero astronaut recoil; L7 push yields proper reactive recoil"*) ·
S05 (gaz vakumda atmosferik dönüyor). Ortam ADI 14/14'te var ama ortam SAYISI
**0/14**; etki-tepki (itme → geri tepme) hiçbir promptta yok.

## 🅑 SINIF 3 — SES · 2 🟠 · 🅑 SINIF 4 — DONANIM DURUMU · 2 🟠 · 🅑 SINIF 5 — ORTAM · 1 🟠

`AUDIO:` 1/14. S05 ③ (*"visible high-pressure gas spray vs lack of conductive/suit
SFX"*) — basınçlı giysiye iletilen ses yazılmamış. S06 (sırt ünitesi var/yok) ·
S05 (halat elde/yok) — nesnenin **hangi sahnede takılı olduğu** kilitli değil.
S03 ⑤ (*"sphere panel structure completely regenerates"*) — kürenin hasar durumu
merdiven taşımıyor.

---

## 🅐 MODEL SAPMASI · 12

**İnsan sayısı** — bu filmin en sert grubu ve kilit tam yazılı (`exactly N human`
14/14): S11 🔴 (*"1-person mission established vs 2 astronauts visible"*) ·
S12 🔴 ×3 (*duplicate head/body spawns* · *three arms visible* · *duplicate
character phases out of structure*). Dört 🔴, dördünde de kilit yerinde.

**Temas** S03 · S10 (`no merging` 14/14) · **bloom** S04 · **kesme** S05 🔴
(*hidden cut inside scene*, `single unbroken take` 14/14) · **efor** S02 · S09 ×2
(efor cümlesi 14/14; S09 ⑧: *"maximal strain instantly disappears into a completely
relaxed posture"*) · **kemer** S12 🔴 (*floating canvas belt clips through torso*).

---

## 🎯 ÜÇ SATIR

```
1. FİLMİN ANA MALZEMESİ KİLİTSİZ. Yüzen panel filmi, parçacık cümlesi 2/14.
   Altı bulgu, ikisi 🔴, hepsi aynı eksik cümleden.
2. İNSAN SAYISI KİLİDİ YAZILI VE TUTMADI — dört 🔴. Tek kişilik görevde iki,
   sonra üç kol. Bu 🅐 ve tekrarlıyor.
3. SES 1/14. Basınçlı giysiye iletilen ses hiç yazılmamış.
```
