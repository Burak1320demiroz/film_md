# 🧊 THE STILL SWARM — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı (operatör beyanı) · teslim dosyası
> operatörde · ③ raporunun gövdesinde `the stıll swarm.mp4` yazıyor, tam yol
> ve çözünürlük YOK. **Master bu oturumda depoda yoktur.**
> **Koşu:** 02.09.2026 · **sekiz mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES ·
> 📖 HİKAYE · 🖼️ ARKA PLAN · ⚖️ FİZİK · 🎯 AKSİYON · 💪 EFOR) —
> **sekizi de mod V.** Depoda ilk sekiz-mercek partisi.
>
> ⛔ **HİÇBİR SKOR SATIRI T1-T8'E GİRMEDİ.**
> ① SPEC kapısı: `THE_STILL_SWARM_QA_SPEC.md` **VARDIR** (01.09.2026'da
> yazıldı, A/B/C/E blokları tam) ve mod D zorunlu beş merceğin beşi de
> `INPUT MODE: V` yazıyor → koşu TEKRARLANIR [D129].
> **SPEC yazılmış olduğu hâlde mod V koşulan film sayısı artık 10.**
>
> ⛔ **⑪ ÖLÇÜM KAPISI KOŞULAMADI** — master elde değil. Bu kaydın SÜRE ve
> SAHNE SAYISI satırları RAPOR KAYNAKLIDIR ve hiçbir kapıya sokulmamıştır
> [qa-isle §1]. Kare/ses doğrulaması gereken her satır ⬜ AÇIK.
>
> ⛔ **BULGUDAN DERS YAZILMADI** — ② kilit defterinde ⬜ AÇIK madde varken
> yasaktır [AGENTS §3②]. Adaylar `DERSLER/GOZLEM_DEFTERI.md`'ye düştü.
> Bu koşunun ürettiği iki ders (**D165 · D166**) filmin bulgularından değil,
> **ALETİN KENDİSİNDEN** çıktı ve ikisi de master olmadan doğrulanabilir.
>
> ⭐ **ÜÇ POZİTİF ÖLÇÜM askıdaki partiden sağ çıkar [D121]:**
> ŞERİT · REPLİK · **IZGARA** — ve ızgara bu filmde bir eksik klip gösteriyor.

---

## 📦 MALZEME

```
MALZEME:  teslim kurgusu · 134-135 s (raporlardan; ÖLÇÜLMEDİ) · 16:9
          + ~2:09-2:15 BAŞLIK KARTI (sahne dışı malzeme, ~5 s)
MERCEK:   ① KARE 3,9 · ② DEVAMLILIK 7,8 · ③ SES 7,5 · ④ HİKAYE 2,7
          · ⑤ ARKA PLAN 4,3 · ⑥ FİZİK 6,2 · ⑦ AKSİYON 7,7 · ⑧ EFOR 3,6
          (düzeltilmiş ortalamalar — ①④⑥⑦⑧ TABLOYA GİRMEZ [D129];
           ②⑤ ⚠️ ŞARTLI, ③ ✅ — aşağıda ①.5)
KART:     ⛔ SPEC'in B bloğu `SCREEN TEXT: 0.0 saniye` ve `TITLE CARD: NONE`
          yazıyor. Sekiz raporun sekizi de kuyrukta bir başlık kartı bildirdi.
          Kart hem SAYIMIN hem SÜRENİN dışında tutuldu [D93 · D120].
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 02.09.2026 · çıkış kodu **2**

```
SPEC: THE_STILL_SWARM_QA_SPEC.md → ①/④/⑥/⑦/⑧ için MOD D ZORUNLU

⛔ TEKRAR   ① KARE       n=7  Σ=27  ort=3.9   D129
⚠️ ŞARTLI   ② DEVAMLILIK n=12 Σ=94  ort=7.8   (mod V tasarım)
✅ GO       ③ SES        n=4  Σ=30  ort=7.5   (mod V tasarım)
⛔ TEKRAR   ④ HİKAYE     n=9  Σ=24  ort=2.7   D129
⚠️ ŞARTLI   ⑤ ARKA PLAN  n=6  Σ=26  ort=4.3   (mod V tasarım)
⛔ TEKRAR   ⑥ FİZİK      n=8  Σ=50  ort=6.2   D129
⛔ TEKRAR   ⑦ AKSİYON    n=7  Σ=54  ort=7.7   D129 · 2 hücre `—` [D131]
⛔ TEKRAR   ⑧ EFOR       n=7  Σ=25  ort=3.6   D129 · 1 hücre `—` [D131]

TOPLAM 8 rapor · 🚨 0 GEÇERSİZ · ⛔ 5 TEKRAR · ⚠️ 2 ŞARTLI · ✅ 1 GO
```

**Betiğin yakaladığı iki yapısal kusur:**

```
① SEVERITY TALLY ≠ YAZILI ETİKETLER — 8 raporun 7'sinde [D161]
   ① 6/4/3 yazıldı, etiketler 5/5/2   ② 1/3/1 ↔ 1/2/1   ⑤ 1/2/3 ↔ 1/2/4
   ⑥ 0/2/3 ↔ 0/2/0   ⑦ 0/1/6 ↔ 0/1/4   ⑧ 0/8/4 ↔ 0/5/3
   ⛔ Verdict'ler bu tally'lerden türetildi → REGENERATE · IDENTITY BREAK ·
     SUBJECT DUPLICATE IN FIELD · REWRITE PREMISE · WEIGHTLESS WORK
     hükümlerinin HİÇBİRİ UYGULANMAZ.
   ⚠️ Bu, altı mercekte ölçülen aynı kusurun sekiz mercekte tekrarıdır;
     D161'in kendi TEKRAR satırına işlendi.

② KAYNAKSIZ HÜCREYE PUAN [D131] — ⑦'de 2, ⑧'de 1 hücre
   "no in-scope source" yazıp 10/10 verilmiş; betik `—` yaptı, ortalama
   ⑦ 8,2→7,7 · ⑧ 4,3→3,6 düştü.
```

---

## §⑪ ÖLÇÜM KAPISI — **KOŞULAMADI**

```
master:      depoda YOK (find: 0 video dosyası) · operatör yolu vermedi
ffmpeg:      /opt/homebrew/bin/ffmpeg VAR — engel araç değil, DOSYA
sonuç:       ölçüm yapılamadı → raporların SÜRE ve SAHNE SAYISI değerleri
             ④ ⑤ ⑦ ⑨ kapılarına GİRDİ SAYILMAZ [D125]
```

⛔ **Master gelir gelmez tek komut, ~30 sn:**
```bash
bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"
```
Bu koşu aşağıdaki ⬜ AÇIK maddelerin **altısını birden** kapatır.

---

## §③ KİMLİK KAPISI [D105] — **ATTRIBUTED ✅** (2 çapa + 2 destek)

⛔ ⑤ ve ⑥ raporlarındaki `FILM: THE STILL SWARM` satırı **kimlik kanıtı
değildir** — ad başlık kartından okunmuş olabilir; ekrandaki yazı çapa
sayılmaz. Kimlik metin olmayan çapalarla kuruldu:

| # | tür | rapor ne gördü | belgede karşılığı | sonuç |
|---|---|---|---|---|
| 1 | **vuruş** | ⑦ B7 · ⑧ E5 · ② S11 · ④ S11 — 1:50-1:59 "kutuyu iterek bırakır" | SPEC A: `CENTRAL CHOICE: S11 · 1:50-2:00 — geldiği şeyi iter` | ✅ saniyesi saniyesine |
| 2 | **sayısal kilit** | ⑤ SCENE 1: "mekik SOL'da · parçalı küre SAĞ'da %60" | SPEC C `EKRAN YÖNÜ`: mekik HEP screen-left · kabuk HEP screen-right | ✅ |
| 3 | destek | ⑤ COUNT LOG: S8 ve S9'da "5 floating hand tools in a row" | SPEC C `SAYAÇ`: S7 **5** → S8 **5** · kelepçeler düz hat | ✅ iki sahnede birden |
| 4 | destek | ⑤ SCENE 7: "~20 debris" | SPEC C `PARÇA SAYISI`: S6 **20** | ✅ |

**Eşleşme 2'nin üstünde → ham raporlar bu filmin altına dosyalandı.**

---

## §④ KURGU KAPISI — **ÖN KOŞU** · ⭐ kuyrukta bir klip eksik görünüyor

```
a) klip sayısı   plan 14   ·   rapor 13   ✗   (8/8 rapor 13 dedi)
b) süre          plan 140 s ·   rapor 134-135 s (kart dâhil)  ✗  Δ ≈ −10 s
c) sıra          ⛔ ÖLÇMEDİ — GEÇTİ değil [D163]
                 insansız sahne 0 / 14 = 0 ≤ 1/10 → şerit SABİTTİR
                 (`1111111111111`) ve sıra eksenini ölçmez.
d) FİNAL VURUŞ   ⬜ AÇIK — kanıt karesi çıkarılmadı
```

⭐ **Δ OKUNDU [D121] — ve ⑨ ızgarası kuyruğu işaret ediyor:**

```
⑨ HİZALAMA KAPISI (betikten, master açılmadan koşar):
   12 kesme · hook 10 s · klip 10 s · max |Δ| = 1,0 s → IZGARA OTURUYOR.
   Yani zaman kodları UYDURULMAMIŞ [D115] ve kesmeler plan ızgarasının
   ilk 13 yuvasına oturuyor:
     0 · 10 · 19 · 30 · 39 · 49 · 59 · 69 · 79 · 89 · 99 · 109 · 119
   plan:
     0 · 10 · 20 · 30 · 40 · 50 · 60 · 70 · 80 · 90 · 100 · 110 · 120 · 130

   İlk 13 yuva birebir. 14'üncü yuva (S13 · 130-140 s) yok; onun yerinde
   BAŞLIK KARTI duruyor.

⛔ HİPOTEZ (kanıtlanmadı): kurguda eksik olan klip S13'tür —
   filmin FİNAL VURUŞU, TWIST'i ve LOOP karesi.
   Destekleyen: ④ "ENDS OR STOPS: stops" · "no peak located" · Final 1/10
                ⑤ SCENE 13'te kabuk %50 kadraj + kelepçeler (bu S12 tarifi)
                SPEC: `FİNAL VURUŞ KANITI` 138 s — bu kurguda 138. saniye YOK
   ⚠️ Bu bir ölçüm DEĞİL, ızgara okumasıdır. Kapatan komut aşağıda.
```

---

## §⑤ ÇAPRAZ SAYIM KAPISI [D107] — parti AYAKTA

```
kesme:  ① 12 · ② 12 · ③ 12 · ④ 12 · ⑤ 13 · ⑥ 13 · ⑦ 13 · ⑧ 13
        yayılım 1 → ✅ koşular birbirini doğruluyor (fark ≤ 1)
        ⚠️ 13 diyen dördü KARTA GİDEN kesmeyi de saymış; rubrik onu
          saymamayı emrediyor. Sayım hatası değil, kural okuma hatası.
şerit:  7 mercek `1111111111111` → ✅ eksen doğrulandı
        ⚠️ D163: bu şerit hiçbir şey KANITLAMAZ (insansız sahne 0)
replik: 8 mercek `none` → ✅ eksen doğrulandı (plan 0 replik)
        ⭐ ③'ün `none — nothing audible to me` yazımı DOĞRU biçimdir:
          dosya iddiası değil, duyum beyanı [D136 · D137].
suskunluk (⑤ beşinci satır [D162]):
        BAŞLIK KARTI — 8 raporun 8'i bildirdi, sahibi ① de bildirdi
        (`NON-SCENE MATERIAL: 2:09-2:15`) → 🚨 SUSKUNLUK YOK, gözlem
        doğrulandı. ⛔ Ama ① onu FLAGS'e SORU olarak yazdı; rubriğin
        kendi kuralı ekran metnini otomatik BLOCKER sayar ve FLAGS'e
        yazılmasını YASAKLAR. → aşağıda ⑩ tablosunda.
```

---

## §② KİLİT ÇELİŞKİSİ DEFTERİ [D96] — **8 madde · 8'i ⬜ AÇIK**

⛔ Bu defterde ⬜ AÇIK madde varken: skorlar ŞARTLI, **bulgudan ders
yazılmaz**, yeniden üretim siparişi verilmez. Çözüm eylemi master'ın o
saniyesine bakmaktır (~10 sn/madde).

| # | rapor ne dedi (timecode) | hangi kilit (§) | çözüm eylemi | sonuç |
|---|---|---|---|---|
| 1 | ①②⑤⑦ · 1:59-2:09 ikinci astronot / arka planda kopya figür | C `İNSAN: tam 1 · 14/14 · yansımada 0 · gölgede 0` (KART 4) | `ffmpeg -ss 122 -i M -frames:v 1` | ⬜ AÇIK |
| 2 | 8/8 · ~2:09-2:15 başlık kartı | B `SCREEN TEXT: 0,0 s` · `TITLE CARD: NONE` · `Jenerik/başlık kartı 0 kare [D70/D72]` | `ffmpeg -sseof -3 -i M -frames:v 1` | ⬜ AÇIK |
| 3 | ④⑨ · kurgu 13 klip / 134 s | B `CLIP COUNT 14` · `RUNTIME 140 s` | `ffprobe -show_entries format=duration` | ⬜ AÇIK |
| 4 | ⑦ BEAT STRING S6 yuvası `-` (bu sahnede vuruş yok) | A/C `S6 = NOVUM TAŞIYICISI · TEK KARE 1:04 · kelepçe 2 m gider ve durur` | `ffmpeg -ss 64 -i M -frames:v 1` | ⬜ AÇIK ⭐ |
| 5 | ⑥ L2 · 0:22 levhayı iter, **geri tepme yok** (L7'de var) | C NOVUM `Etki-tepki hâlâ çalışır — iten geri savrulur` | `ffmpeg -ss 22 -i M -frames:v 1` | ⬜ AÇIK |
| 6 | ⑥ L3 · 0:52-0:58 gaz **kıvrılır, yayılır, asılı kalır** | S5 ACCEPT/REJECT: koni 1 m'de DURUR, kenar sert ve düz; `any curl, bloom or spread → reject` | `ffmpeg -ss 56 -i M -frames:v 1` | ⬜ AÇIK |
| 7 | ⑦ B5 · 1:20-1:29 halatı çeker, **hiçbir durum değişmez** | A `S8 · 1:26 halat KOPAR — kopan uç mutlak durur` (RED-RİSKLİ kare) | `ffmpeg -ss 86 -i M -frames:v 1` | ⬜ AÇIK |
| 8 | ② `Counter Logic: N/A — sayaç yok` | C `SAYAÇ: 8→8→7→5→5→2→0`, metin 0,0 s, boş halkalardan okunur | ölçüm boşluğu [D134] · kuşak kadrajları | ⬜ AÇIK |

⭐ **4 numaralı madde bu filmin tek kritik sorusudur.** Kapatan komut bir
tanedir ve cevabı ikiye ayırır:

```
ffmpeg -ss 64 -i "<master>" -frames:v 1 tek_kare_1-04.jpg   → BAK

kelepçe kadının eldiveninden ~2 m ötede ASILI ise
    → NOVUM EKRANDA · sekiz merceğin sekizi onu göremedi  → ALET KUSURU
kelepçe yoksa / hareket ediyorsa
    → NOVUM EKRANDA DEĞİL · S6'dan sonraki her sahne yeniden üretilir
```

---

## §⑩ ÖNERME KAPISI [D87 · D116 · D130] — **düşen bulgular**

Kaynağı planda YAZILI olan bulgu DÜŞER; puanı hücreye geri verilir.

| bulgu (mercek · tc) | planda yazılı mı | karar |
|---|---|---|
| "tether/halat boyunca ilerliyor" (⑦ B1 · ⑧ E1 · ② · ④) | ✅ S0-S3 gergin halat; S3'te gevşer; S8'de kopar (B2b başarısız deneme #2) | **DÜŞER** |
| "0:59'da halat kayboldu — nesne kalıcılığı kırıldı" (② 🟠) | ✅ S3: `kabuktan içeri geçer, halat gevşer` — bırakılması olay örgüsüdür | **DÜŞER** |
| "0:59'da gizli kesme, poz anında değişiyor" (① 🔴) | ✅ 0:59 bir SAHNE SINIRIDIR; rubriğin kendi compilation kuralı sınır kesmesini bulgu saymaz | **DÜŞER** (rapor iç hatası) |
| "yerçekimi 0 g mi?" (① FLAGS) | ✅ C `YERÇEKİMİ 0 g · 14/14` | **DÜŞER** |
| "gaz vakumda var" (⑥ L3'ün "plume exists" yarısı) | ✅ S5 valf + koni tasarımdır | **YARISI DÜŞER** — "kıvrılıyor/yayılıyor" yarısı AYAKTA (madde 6) |
| "ikinci figür" · "başlık kartı" · "eksik klip" | ❌ planda tersi yazılı | **AYAKTA** |

⛔ **④'ün KESME LİSTESİ UYGULANMAZ** [D129 + ⑩]. Listede önerilen dört
kesimin üçü SPEC'in `⛔ KESİLEMEZ SAHNELER` listesinde:
`S3` (novum kanıt zinciri değil ama ⛔ değil), **`S6` = NOVUM TAŞIYICISI +
TEK KARE**, **`S12`(rapor) = ikinci seçim [D158 B2a]**, `S8` = başarısız
deneme #2. Bir kez daha, dört mercekten gelen bir liste filmin taşıyıcı
sahnesini kesmeyi önerdi [AGENTS ⑩ son satır].

---

## §⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME [D108 · D159]

| gözlem (tc) | hangi raporlarda | sahibi | puanı kim taşıyor |
|---|---|---|---|
| ikinci figür / kopya özne · 1:59-2:09 | ① ② ⑤ ⑦ | **⑤** (alan figürü [D162 sahiplik]) | ⑤ · diğer üçü işaretçiye iner |
| başlık kartı · ~2:09 | 8/8 | **①** (ekran metni) | ① — ⛔ ama ① onu FLAGS'e yazdı |
| gaz davranışı · 0:52-0:58 | ① (bloom) ⑥ (akışkan) | **⑥** (ölçülmüş fizik) | ⑥ · ①'in satırı işaretçi |
| halat direnci, durum değişmiyor · 1:20 | ⑥ ⑦ ⑧ | **⑦** (okunabilirlik) | ⑦ · ⑥⑧ işaretçi |
| kutu kütlesi / atalet · 1:30 | ⑥ ⑧ | **⑧** (bedel) | ⑧ · ⑥ işaretçi |

⚠️ **Dört mercek aynı ikinci figürü bildirdi — bu N kat güvenilir DEĞİLDİR
[D159]:** partinin sekizi de aynı oturumda, aynı malzemeyle koşulmuş
olabilir. Bağımsızlık kanıtlanmadı → madde kareyle çözülür.

---

## 🎯 ÜÇ SATIRLIK SONUÇ

```
1. FİLM HAKKINDA HİÇBİR HÜKÜM VERİLMEDİ ve verilemez: sekiz koşu da
   D129'dan düştü, master ölçülmedi, defterde 8 ⬜ AÇIK madde var.
2. TEK KOMUT sekiz maddenin altısını kapatır (olcum_kapisi.sh) ve
   TEK KARE (1:04) filmin novum sorusunu ikiye ayırır.
3. KOŞU YENİDEN YAPILIR — çıplak rubrikle değil, PAKETLE:
   bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh \
        yatay_2_dk_filmler/THE_STILL_SWARM "<master>"
```

**Bu koşudan çıkan dersler:** D165 (paket filmin yazımında üretilir) ·
D166 (mod V, novumu olan filmi ölçemez). İkisi de ALETTEN çıktı; film
bulgularından ders yazılmadı [DERS_YAZIM_KONTRATI §4].
