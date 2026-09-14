# 🎵 THE OPEN CIRCUIT — MÜZİK

> Kaynak: `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · `SES_VE_DIYALOG` §6
> ⛔ Bu dosya YAZIM tarafıdır. Kurguya TEK skor girer.

```
KÜNYE [§17]
  FİLM SÜRESİ:   249,0 s = 4:09   (hook 9,0 s + 24 × 10,0 s)
  BPM:           72     → 1 vuruş = 0,8333 s · 1 ölçü (4/4) = 3,3333 s
                 ⭐ 10,0 s = TAM 3 ÖLÇÜ. Her sahne sınırı bir ölçü çizgisidir.
                 ⭐ Izgara sıfırı 9,0 s (hook'un bitişi); hook ızgara DIŞIDIR.
  TONALİTE:      sabit merkez, çözülmesiz. Kök 41 Hz; üstünde yalnız
                 82 · 123 · 164 Hz duyulur — kökün kendisi HİÇ ÇALINMAZ
                 (missing fundamental). Kulak onu kurar; film de öyle.
  ENSTRÜMAN:     ① alçak sürekli ton (kök yok, üst kısmi sesler)
                 ② tek yüksek sinüs, 2.640 Hz, yalnız üç sahnede
                 ③ kuru düşük perküsyon — YALNIZ İKİ vuruş, ikisi de aşağıda
                 ⛔ melodi YOK · akor ilerlemesi YOK · yaylı YOK · koro YOK
```

---

## 🎼 CUE HARİTASI

```
CUE A — "YÜK"          9,0 – 179,0 s   (S1 → S17)
  Tek alçak ton. Nabız YOK. Her sahne sınırında üst kısmi seslerden BİRİ
  eklenir ve hiçbiri çıkarılmaz: 82 (S1) → +123 (S6) → +164 (S13).
  ⭐ Yükselmez, GENİŞLER. Filmin fırtınası da öyle: itmez, yüklenir.
  ⛔ Anempatik: hiçbir olaya tepki vermez. S15'in yırtılması bile cue'yu
    değiştirmez — yalnız SUSTURUR (aşağıda).

CUE B — "TOPRAK"       199,0 – 249,0 s (S20 → S24)
  Aynı alçak ton geri gelir ve üstüne TEK yüksek sinüs (2.640 Hz) biner.
  Sinüs S20'de girer, S22'de kalır, S24'te tek başına kalır ve ÇÖZÜLMEZ.
  ⛔ Aşağı inen tek şey kıvılcımdır; müzik inmez.

PERKÜSYON — TAM İKİ VURUŞ, ikisi de KAPALI hattadır:
  ① 189,0 s (S19'un ilk karesi) — tek kuru düşük vuruş, kesiciyi ÖNCELER
  ② 219,0 s (S22'nin ilk karesi) — aynı vuruş, aynı seviye, aynı ton
  ⭐ İkisi arası 30,0 s = TAM 9 ÖLÇÜ. Filmin tek ritmik yapısı budur.
```

---

## 🔇 SESSİZLİK KARARI

```
ÜÇ SESSİZLİK:
  ① 0,0 – 9,0 s        HOOK — müzik YOK. İlk ses bir kıvılcımın tıkırtısıdır.
  ② 179,0 – 199,0 s    S18 + S19 — ⭐ FİLMİN EN PAHALI 20 SANİYESİ.
                       CUE A 179,0'da (S18'in ilk karesi) KESİLİR ve
                       CUE B 199,0'a kadar GİRMEZ. İki yırtılma, merkezî
                       seçim ve dört şeridin sönmesi MÜZİKSİZ geçer.
  ③ 239,0 – 241,0 s    S24'ün ilk iki saniyesi — CUE B bir ölçü boyunca
                       düşer ve geri gelir; kapanış karesi böyle açılır.

⛔ KURGUDA HARD MUTE: sn 193,0 – 195,0
   ⭐ [D180] BIÇAK KURGUDADIR, ÜRETİMDE DEĞİL. Bu iki saniye merkezî
     seçimin (S19) İÇİDİR ve mutlak sessizlik olmak zorundadır: müzik
     değil, ORTAM YATAĞI DA susar. Veo'nun yerel sesi mutlak sessizlik
     teslim ETMİYOR ve depo bunu iki filmde ölçtü (THE UPWARD FALL ve
     THE HEALING GROUND: −50 dB'de tek aralık yok; THE STANDING WIRE:
     bıçak SPEC'te doğru yazılıydı ama dosyada hiç kurgu yapılmamıştı).
     Video promptundaki `ABSOLUTE SILENCE from 4.0s to 6.0s` cümlesi
     KALIR ama YEDEKTİR.
   KOMUT (kurguda, teslimden önce):
     ffmpeg -i <master> -af "volume=enable='between(t,193,195)':volume=0" \
            -c:v copy <out>
   ÖLÇÜM (teslimden sonra, ⑪ ölçüm kapısı):
     saniyelik RMS 300-3400 Hz bandında; 193,0-195,0 aralığında
     KESİNTİSİZ olarak −50 dB altında olmalı. Değilse teslim EDİLMEZ.
```

---

## 🎚️ REPLİK ALTINDA MÜZİK

```
22 repliğin hepsinde müzik 6 dB iner ve replik bitiminden 0,5 s sonra döner.
⛔ İSTİSNA: 190,0 ve 195,5 saniyedeki iki replik (S19) — orada müzik
  zaten YOKTUR ve geri gelmez.
⛔ İSTİSNA: 182,0 saniyedeki makine repliği (S18) — orada da müzik yoktur.
```

---

## ⬜ SAHİP KARARI BEKLEYENLER

```
⬜ 2.640 Hz sinüsün seviyesi — S24'te tek başına kalınca fazla keskin
   gelirse bir oktav aşağı (1.320 Hz) alınır. Karar dinlemeyle verilir.
⬜ CUE A'nın üçüncü kısmi sesinin (164 Hz) S13'te mi S15'te mi gireceği;
   S13 seçildi çünkü içeri girişle çakışıyor, ama S15 daha sert olurdu.
⬜ Perküsyon vuruşlarının seviyesi — ikisi de AYNI olmalı; farklıysa
   ikincisi "daha önemli" okunur ve doruk müzikten gelir, olaydan değil.
```
