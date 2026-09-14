# ⚠️ THE_HARD_DOCK — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
> **Revizyon 11.09.2026:** ilk sürüm 🔴 satırları "✅" işaretlemişti ama bölüm dosyaları
> vizörü iki hâlde yazıyordu (D197 ihlali) ve ışık kilidi promptlara hiç inmemişti.
> Aşağıdaki durumlar bölüm dosyalarının REVİZE hâline göre yeniden işaretlendi.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S02-S24 (insanlı 14) | D197 · D79 · D95 · D146 · tür kartı D5 | vizör iki hâlde / kubbe / aynalı | TEK nitelik: "single flat front pane in a visible dark-grey rim — not a bubble, not a dome — optically clear, zero tint, zero mirror, one thin specular line, collar seal ring visible, face readable" — her insanlı IMAGE'da tam, VIDEO'da CONTINUITY LOCKS'ta; "opaque/mirrored" 0 kez | ✅ (grep 0) |
| 2 | S01-S24 | D201 (GREEN CEILING: güneş 120° sıçradı) | güneş yönü sahneler arası flip | güneş istasyonun ARKASINDA, eksenin ~30° üstünde, kadraj dışı — kurulum başına sabit cümle: A/E/F "backlit, hard white rim, orange from below" · G "behind the camera, shadows fall straight away from the lens" · iç "orange enters low through the window, one white cabin lamp" | ✅ |
| 3 | S16 · S22 · S23 | D104 · YANASMA V5 · B1 | kameraya paralel eksende iki gövde battı (Black Cradle S4) | kamera PORTA kilitli, gemi kadraja girer ve kameraya gelir; temas S22 içinde 6,0 s; port-kilitli kamerada arka planın kayması İLAN EDİLDİ (SPEC C) | ✅ |
| 4 | S02 S04 S08 S12 S17 S21 S24 | D139 · ⑮ | kamera arkada → sırt ünitesi doğar | B kurulumunun her promptunda pozitif sırt cümlesi: "Her back is toward the camera and fully visible: it is that one plain smooth panel, and the plain panel is what this shot shows" | ✅ (betik ⑮ temiz) |
| 5 | S22 · S23 | D157 · D73 | novum taşıyıcısı tek kareyi geçmiyor | TEK KARE = S23 0,0 s: dört DİKME çökük + HALKA bükük; PLAN'da taşıyıcı adı TEK KARE satırında; iptal kapısı bu sahneye bağlı | ✅ (betik ⑭ temiz) |
| 6 | S03 S09 S11 S18 S20 | D175 | mühürlü filmde uzuv adı deriyi çizdirir | "wrist" yalnız "one piece with the sleeve at the wrist" içinde (örtü adı ±12 kelime); anatomi ayrıntısı 0; çıplak deri negatifi ÜÇ bölge | ✅ (betik ㉑ temiz) |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S06 | D32 / D78 · YANASMA V3 | iki gövde aynı karede: oran/yön/dizilim yazı-tura | V3 yalnız 1 kez; üçlü: oran cümlesi "twenty times — a moth beside a cathedral" · burun screen-right · altı gemi boyu boşluk; NEGATIVE "never the same size" | ✅ |
| 2 | S22 | POLİTİKA §3 · red defteri | temas "çarpışma" okunur | nötr tarif: seats · compress to their stops · settles a hand's width · no bounce; kelime yasağı yazılmadı (D123) | ✅ · üretimde red gelirse önce KAMERA (3c: iki yenilgi kuralı) |
| 3 | S10 · S19 | rubrik 3c (YERCEKIMI S8) | yüz yok + el + makro | kamera nesne hizasında (yandan, kalça yüksekliği), tepeden değil; kapak → eldiven → bar ard arda derinlikte; eldiven tam kapalı | ✅ · üretimde red gelirse D kurulumu C'ye katlanır (yüz + el aynı kadraj) |
| 4 | S19 · S20 · S24 | D202 · OYUNCULUK §2 | seçim/bedel bedende okunmuyor | ÇAPA ÜÇLÜSÜ PLAN'da; S19 tıklatmasız düz gidiş (alışkanlık kırılır); S20 omuz iner ve KALIR; S24 eldivenler parmak parmak açılır | ✅ |
| 5 | S02 · S13 | D198 · D23 | yüzen panel donuyor / 2D | "turning end over end at one steady rate, never pausing … never freezes, never drifts back" | ✅ |
| 6 | S16 · S22 · S23 | D176 ㉒ · D193 | port-kilitli kamerada arka plan kayar — mercek "ışık/çevre değişti" yazabilir | SPEC C BLOĞU IŞIK TAKVİMİ satırında ilan edildi: "G kurulumunda arka plan kayar — ihlal değil kanıt" | ✅ |
| 7 | S24 | D141 | final vuruş kanıtı sayılamaz | dört lamba YANIK (S01-S23'te 0) + iptal barı dik; SPEC B FİNAL VURUŞ KANITI satırı | ✅ |
| 8 | tümü | uzunluk bandı · REHBER §5 ① | video promptları 2.600'ün üstünde | tavanın (4.300) altında ölçüldü (max 4.143); D74 satırı BÖLÜM 1 ⑨ ve PLAN §SAPMALAR ③ | ✅ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| UZAY_USSU §5.3 · AMBER LATTICE | istasyon ölçek kayması | ölçek şahidi gemi halkası (R3 p2, 1/20); her dış promptta aynı istasyon cümlesi; kopuk kol hep screen-left |
| SES §1a · §2a | AI sesi duygusallaşır / insan sayı söyler | 8 replik MACHINE, tam form, sayı yalnız burada; insan repliği 0; bedenleştirme yok |
| A1 · D50 | "no text" ↔ ekran içeriği | ekran/ibre/yazı 0; bilgi kanalı 4 lamba + pencere geometrisi + ses |
| KART 10 · Cold Burn S8 | insansız sahne + uzun negatif → yapısal red | 10 insansız sahnede NEGATIVE < 900 karakter; pozitif "Human count zero" |
| D34 | özel ad promptta | "MIRA" hiçbir prompta girmez — "the ship computer's flat synthetic voice" |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor | D146 | Var (kask paneli · dört dikme) | REFERANS_PAKETI R1 p4 · R2 p4/p5; KAPI 0 — onaysız sayfayla sahne üretilmez |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR | D59 · D153 | Yok | kumaş/fabric/wave tarifi 0; giysi "matte white pressure suit", sert kabuk |
| 3 | Optik aritmetiği hiç yapılmamış | OPEN CIRCUIT | Var | 05_SAHNE_CALISMALARI her sahnede KADRAJ ENİ ve ana nesne px; A'da istasyon ≥%40 kadraj, G'de yaka ön plan |
| 4 | Uzak nesne ~60 piksel | D179 | Var (S06 gemi · S16 gemi) | S06 gemi kadraj eninin ~%8'i (≈300 px @4K); S16 gemi ~%6 (≈230 px) — ikisi de ≥100 px; daha küçük yazılmadı |
| 5 | Ayrım RENKLE kuruldu | BLIND BERTH | Var | gemi beyaz/turuncu ↔ istasyon koyu gri; ayrıca BİÇİM: yuvarlak halka ↔ sekizgen yaka; kapak çizgili ↔ bar çizgili ama YÖN farklı (kırmızı-beyaz yatay menteşe ↔ sarı-siyah dik bar) |
| 6 | Ortam kartının NEGATİF bloğu prompta girmemiş | UZAY_USSU §6 | Var | her dış promptta "no atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no lens flare, no anamorphic streak" |
| 7 | Tema yazıldı ama sahne indeksi yok | KALEIDA CRASH | Var | MOTİF SAHNELERİ: S03 S06 S10 S15 S17 S19 S24 (betik ⑬ temiz) |
| 8 | Bedel var ama sahne numarası yok | 03_PLAN_ONCESI | Var | BEDEL görülür S22 · adı konur S24 (betik ⑰ temiz) |
| 9 | Yasak cümlesi yazıldı | D123 | Var | "never drawn/aimed" kalıbı 0; politika kelimesi 0 (betik ⑯ temiz) |
| 10 | Politika: nesne ADLANDIRILDI | D67 | Var | fırlatıcı/silah formu tümüyle SİLİNDİ; temas nötr tarif |
| 11 | Replik zamanı ELLE yazıldı | D122 | Var | formül: (n−1)×10 + ofset; 8 kayıt SPEC'te doğrulandı |
| 12 | Klip içi durum değişimi | T2V-CompBench | Var | tek yönlü ve tek: S19 kapak açılır · S22 dikmeler çöker · S24 eller açılır; ışık/kir/lamba klip içinde değişmez (lamba S24 imajında zaten yanık) |
| 13 | Prompt "BIBLE'a bak" diyor | Kural ③ | Yok | 48 prompt self-contained (betik ③ temiz) |
| 14 | Makine kapısı KURULU OLMAYAN filtreye yazıldı | D142 | Var | SPEC E: signalstats · crop · freezedetect · select — ffmpeg 8.1'de DOĞRULANDI 11.09.2026 |
| 15 | Çıplak deri negatifi bölge saymıyor | D175 | Var | üç bölge birden: collar seal · wrist between glove and sleeve · ankle above the boot cuff |
| 16 | Filmin 1 NUMARALI riski sıfatla korunmuş | D192 | Var | salınım SAYIYLA: 48 s / tam koni, 10 s'de ~1/5 daire, hız sabit; pencere 6 s (S05'te görsel kanıt) |
| 17 | Vizör iki hâlde yazıldı | D197 (bu filmin ilk taslağı) | Var | TEK nitelik cümlesi; opak/aynalı 0 kez |
| 18 | Ardışık aynı kurulum işaretsiz | ACI_YAYI §3 🕰️ (bu filmin ilk taslağı: 9 çift) | Var | küme 2, ikisi de işaretli; kalan 21 çift farklı harf |

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (durum ✅ — bölüm dosyalarının revize hâline göre)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşındı (C BLOĞU · E BLOĞU)
☑ tekrar eden arıza tablosunun HER satırı cevaplandı (18/18)
→ 05_SAHNE_CALISMALARI/ açık; S01-S24 dolduruldu.
```
