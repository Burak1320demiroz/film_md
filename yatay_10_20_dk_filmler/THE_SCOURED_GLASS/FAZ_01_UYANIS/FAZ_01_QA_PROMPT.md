# 🚦 FAZ 1 QA KAPISI — THE SCOURED GLASS / UYANIŞ

> **[D185]:** Uzun filmin QA birimi FİLM değil FAZDIR. Bu dosya olmadan
> koşan mercek, faz ölçeğinde ölçülemeyecek şeyi puanlar ve o puan
> ortalamayı bozar. YERÇEKİMİ'nin F9 ve F10 fazlarının **ikisinde de bu
> dosya yoktu** — D185'in iki vakası odur.
>
> ⛔ **RUBRİKLE VE `../THE_SCOURED_GLASS_QA_SPEC.md` İLE BİRLİKTE
> YAPIŞTIRILIR.** Üçü birden verilmezse koşu mod V'dir ve tabloya girmez
> [D129].

---

## 🅾️ FAZ KÜNYESİ — merceğin ölçeceği şey budur

```
BU BİR FİLM DEĞİL, 30 DAKİKALIK BİR FİLMİN BİRİNCİ FAZIDIR.
  Faz     : 1 / 15  ·  ad: UYANIŞ  ·  perde: 1 (Kuruluş)
  Sahne   : S1-S12 (film ölçeğinde de S1-S12)
  Süre    : 120,0 s  ·  klip 10,0 s × 12
  Zaman   : 0:00 – 2:00 (film ölçeğinde de 0:00 – 2:00)
  Izgara  : sahne başlangıcı(n) = (n−1) × 10,0 s
  Mekân   : S1-S9 DIŞ · S10-S12 İÇ
  İnsan   : 12/12 sahnede tek insan
  Replik  : 2 (S4 telsiz ≤8 kelime · S12 günlük 18-22 kelime)
  Kesme   : 0
```

---

## ⛔ BU FAZDA ÖLÇÜLEMEYEN HÜCRELER — `—` yazılır, SAYI YAZILMAZ

```
Aşağıdaki eksenler 120 saniyelik bir faz parçasında ölçülemez. Rubrik o
kategoriyi sorarsa hücreye TİRE konur ve ortalamaya GİRMEZ [D185 · D131].

  ④ HİKAYE   · üç perde yapısı · doruk · çözüm · karakter yayı ·
               tema ödemesi · ekipman ödemeleri (Çehov)
  ⑫ HOOK     · terk eğrisi · tamamlanma oranı · tekrar izleme ·
               ⛔ TEK İSTİSNA: AÇILIŞ KANCASI BU FAZDA ÖLÇÜLEBİLİR
                 (S1 kapak karesi · mahsur bilgisi ≤0:30 · ilk replik
                  0:30-0:40 · ilk geri dönülmez eylem 1:30-2:00)
  ⑨ KADRAJ   · eş kadraj çifti (S1↔S180 — 180. sahne bu fazda yok) ·
               açılış-kapanış kafiyesi · döngü
  ② DEVAMLILIK · film boyu yıpranma merdiveni · ⛔ AMA faz içi
               devamlılık TAM ÖLÇÜLÜR (aşağıdaki dört kilit)
  ⑪ IŞIK     · film boyu grade tutarlılığı
               ⛔ İÇ/DIŞ ışık farkı KUSUR DEĞİLDİR — SPEC C bloğu

⛔ "Bu fazda X eksik" DENEMEZ. Faz eksiklik ölçmez; eksik olan şey
   sonraki on dört fazdadır. Yalnız PLANDA yazılıp EKRANDA olmayan şey
   kusurdur — ve planın ne söylediğini SPEC söyler.
```

---

## ✅ BU FAZDA TAM ÖLÇÜLEN ŞEYLER — beş kilit

> ⭐ Her kilidin yanında onu ölçecek merceğin adı yazılıdır [D187].
> Mercek adı taşımayan kanıt ölçülmemiş sayılır.

```
KİLİT 1 — CAM MERDİVENİ, 0. KADEME  ⭐ NOVUM
  ① S1-S7'de vizör camı ÇİZİKSİZ (üstünde yalnız gevşek toz)  → ② cat.3
  ② S8'de bez TEK GEÇİŞ — gidiş-geliş VARSA kusur             → ⑦ cat.1
  ③ S9-S12'de mat şerit EKRAN-SOL ALT köşede DURUR            → ① cat.2
  ④ S8'de mat şerit kadrajın ~%45'i                           → ⑨ cat.4
  ⛔ ŞERİDİN VARLIĞI KUSUR DEĞİLDİR. Şeridin KAYBOLMASI kusurdur.

KİLİT 2 — GÖĞÜS İĞNESİ, KIRMIZI YAYDA
  ① S1 · S6 · S7'de iğne kırmızı yayda, tek yönde              → ② cat.10
  ② göstergede rakam/harf/çentik SIFIR                         → ① cat.6
  ③ S7'de 10 s'de bir iğne kalınlığı kayar                     → ⑥ cat.5
  ⛔ Rakamsızlık "eksik bilgi" diye yazılamaz — SPEC METİN YASAĞI.

KİLİT 3 — SIZINTI ZİNCİRİ (fazın nedensellik omurgası)
  ① S6'da delik görünür, tıslama başlar                        → ③ cat.2
  ② S7'de iğne kırmızıda; delik bunun SEBEBİ                    → ④ cat.3
  ③ S11'de zımba tıslamayı KESER                                → ③ cat.2
  ⛔ Bu üç kanıttan biri ekranda yoksa fazın tek dramatik
     sorusu ekranda yok demektir. ⭐ En pahalı kilit budur.

KİLİT 4 — GÖVDE, 0. KADEME
  ① S10 · S11 · S12'de sakal DÖRT GÜNLÜK, daha uzun DEĞİL      → ② cat.3
  ② S9'da adım topallar; S1-S8'de topallama YOK                 → ⑧ cat.1
  ③ S11'de üç zımba, el TİTRER, bağırma YOK                     → ⑩ cat.2

KİLİT 5 — TOZ YAPIŞIR
  ① S2'de toz eldivenden DÖKÜLMEZ, silkeleme işe yaramaz        → ⑥ cat.1
  ② her sahnede diz altı pas rengi toz kaplı                    → ⑤ cat.2
  ③ S9'da kapaktan çıkan toz havada ASILI KALIR                 → ⑥ cat.4
```

---

## 📐 AÇILIŞ SÖZLEŞMESİ KAPISI — ⑫ HOOK bu fazda ÖLÇER

```
Araştırmadan gelen dört zaman damgası [TUR 13 · rapor 1]. Mercek bunları
ekranda ARAR ve tutmuyorsa YAZAR:

  ①  KAPAK KARESİ    S1, 0:00-0:10 — ilk kare aynı zamanda akıştaki
                     kapak. Küçük boyutta okunacak tek şey GÖZ olmalı.
  ②  MAHSUR BİLGİSİ  ≤ 0:30 — S3'te biter. Seyirci 30. saniyede
                     "bu insan yalnız ve mahsur" bilgisini almış olmalı.
  ③  İLK REPLİK      0:30-0:40 — S4. Daha geç gelirse içerik "sessiz
                     ya da bozuk" sanılıp terk edilir.
  ④  İLK GERİ        1:30-2:00 — S11 (1:40-1:50). Karakter pasif
     DÖNÜLMEZ EYLEM  şoktan aktif hayatta kalmaya geçmiş olmalı.

⚠️ BİLİNEN VE KABUL EDİLMİŞ SAPMA: araştırma kaynak göstergesini
   0:50-1:00'a koyar; bu fazda S7 (1:00-1:10) — +10 s. Gerekçe
   nedenselliktir (delik önce, iğne sonra) ve `_BASLIK.md` §KAPILAR'da
   yazılıdır. ⛔ MERCEK BUNU KUSUR YAZAMAZ.
```

---

## 🚫 BU FAZDA KUSUR SAYILMAYANLAR — SPEC'in sekizine ek dört

```
 9. S1-S9'un dokuzunda da aynı dış mekânda olmak      → faz tek mekânlıdır
10. On iki sahnenin onunda replik olmaması            → ters U şok evresi
11. Hiçbir şeyin çözülmemesi, sorunun büyümesi        → 1. perde kuruluşudur
12. Mizahın hiç olmaması                              → Zillmann kuralı:
    ilk şaka ancak bir tehlike ATLATILDIKTAN sonra gelebilir; bu fazda
    atlatılan tehlike yoktur. İlk mizah FAZ 3'tedir.

⛔ Bu dördünden birini kusur yazan bulgu ⑩ ÖNERME KAPISI'nda DÜŞER.
```

---

## 📤 RAPOR FORMATI — değişmez

```
Raporun ilk satırı:   INPUT MODE: D
Künye satırları:      CUT COUNT · SCENE COUNT · RUNTIME · PRESENCE STRING
                      CUT TIMECODES (⛔ zaman kodu yazılmayan sayım
                      KOPYA ŞÜPHESİ üretir — ⑦ ORTAK DEFTER kapısı [D110])
Beklenen künye:       kesme 11 · sahne 12 · süre 120,0 s
                      şerit 1 1 1 1 1 1 1 1 1 1 1 1
                      kesmeler 0:10 0:20 0:30 0:40 0:50 1:00 1:10 1:20
                                1:30 1:40 1:50

⛔ Sayı taşıyan her hücre bir KAYNAK gösterir (sahne + saniye).
   Kaynağı olmayan hücre `—` taşır, 7 ya da 10 taşımaz [D186].
⛔ "Kusur yok" ya 10/10 + adı konmuş kaynaktır ya da `—`'dir.
```
