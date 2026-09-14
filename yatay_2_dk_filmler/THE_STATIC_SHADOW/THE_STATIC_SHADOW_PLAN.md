# 🎬 THE_STATIC_SHADOW — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.

```
FORMAT:        yatay 16:9 2-4 dk
ORTAM:         §3.1 vakum + §3.10 basınçlı iç hacim + §3.8 soğuk kaynak mekanizması
TÜR:           bilimkurgu
KLİP SÜRESİ:   10 saniye (8s üret + 2s extend)
SAHNE SAYISI:  15        RUNTIME: 150s (02:30) = 10s + (15−1) × 10s
LOGLINE:       Güneş kalkanının yalpalayarak gölgeyi kaçırması üzerine servis teknisyeni, podunu kalkanın kenar rayına geri dönüşsüz biçimde yapıştırarak dev bir moment koluna dönüşür ve kalan yakıtıyla açısal momentumu söndürür.
```

---

## 🎭 TEMA

```
TEMA: İNSAN-MAKİNE VE FEDAKÂRLIK
      — Pilot, teleskobu kurtarmak için kendisini ve aracını devasa bir reaksiyon koluna çevirir.

MOTİF SAHNELERİ: S04 · S12 · S14
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Yıldız kalkanı yalpalaması altında pilot, podunu kalkan kenarına vakum yapışmasıyla saplayarak aracı bir moment koluna dönüştürür.
NOVUM TAŞIYICISI:    Servis podu burnu × capture rail kenetlenmesi → reaksiyon koluna dönüşme
TEK KARE (§4①):      Tek karede dev kalkan kenarına saplanmış küçük servis podunun RCS iticilerle tork uyguladığı ve gölge hattının teleskop üzerinde durduğu an.
KİNETİK BAĞIMSIZLIK: Gölgenin teleskoptan kayması ve pod torkuyla geri oturması repliksiz kanıtlanır.
BAŞLIK ŞEMASI:       THE STATIC SHADOW
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Derin uzay teleskobunun kriyojenik sensörlerini koruyan güneş kalkanını hizalamak.
   □ ENGEL:   Kalkan gyro'sunun kilitlenmesi (~0.008 rad/s) ve radiant flux nedeniyle manipülatörlerin kullanılamaması.
   □ BEDEL:   Geri dönüş yakıtının ve podun tamamının harcanması (S14).
   □ MUHATAP: HELIOS AI ve pilotun kendi geçmiş kararı / pod aracı.
B5b □ AYRILIK: S11 — HELIOS AI "Abort" emri verirken pilotun iticiye yüklenme kararı.

ÜRETİM SIRASI:
  referans paketi → DORUK (S14) → merkezî seçim (S12) → kapanış imajı (S15) → S01 → kalanı
```

---

## 🥁 VURUŞ TABLOSU (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | sahne | boşsa gerekçe |
|---|---|---|---|---|
| 01 | Kurulum / Anomali Reveal | %0-10 | S01 | Dev kalkan yalpalaması, gölge kayıyor |
| 02 | Tehdit Yükselişi | %10-20 | S02 | Kriyojenik teleskop ışıma altında |
| 03 | İrade / Kilitlenme | %20-30 | S03 | Gözler hizalama retikülüne kilitlenir |
| 04 | Alışkanlık Jesti | %30-40 | S04 | Öteleme koluna iki kez tıklatma |
| 05 | Hizalanma / Yaklaşma | %40-50 | S05-S06 | Pod dev kalkan kenarına yanaşır |
| 06 | İlk Başarısızlık | %50-60 | S07-S08 | Yumuşak temas yetersiz, kalkan iter |
| 07 | Sensör Kaybı / Kriz | %60-70 | S09-S10 | Particle event telemetriyi bozar, tereddüt |
| 08 | Abort Emri | %70-75 | S11 | HELIOS AI abort emri verir |
| 09 | Karar / Alışkanlık Kırılması | %75-80 | S12 | Tıklatmadan tetik kapağı kaldırılır |
| 10 | Karlı Hücumu | %80-85 | S13 | İticiler tam güç rail'e doğru çalışır |
| 11 | Doruk / Moment Kolu | %85-95 | S14 | Galling + yapışma, pod moment kolu olur |
| 12 | Çözülüş / Durgun Gölge | %95-100 | S15 | Gölge teleskopa sabitlenir, SHADOW ERROR: 0.000 |

---

## 🪝 HOOK MİMARİSİ (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:     ANOMALİ REVEAL — dev kalkan normal görünürken yavaş yalpalamayla gölge hattının kayması.
S0 SORUSU:     500m'lik kalkan neden yalpalıyor ve teleskop korunabilecek mi?
S1 İKİNCİ BİLGİ: Teleskobun sensör sıcaklığının hızla yükseldiği ve 4 dakika kaldığı.
İLK 2 SN SESİ: Telsiz taşıyıcı cızırtısı + AI teknik telemetri sesi.
```

---

## 🗺️ SAHNE HARİTASI

> Kurulum sayısı (10): Cockpit iç ve vakum dış sahneleri arasında 10 kurulum kullanılmıştır [D74 gerekçeli izin].

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` (göz · tepki planı ·tipi) | ses | bütçe |

| S | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | bütçe |
|---|---|---|---|---|---|
| S01 | Kalkan Yalpalama | Dev kalkan ~0.008 rad/s yalpalar, gölge kayar | 24mm · EWS · alt açı | HELIOS telemetri + telsiz | Göz: kayan gölge hattı |
| S02 | Teleskop Tehdidi | Kriyojenik teleskop parıltı altında | 35mm · OTS · göz seviyesi | HELIOS sıcaklık uyarısı | Göz: teleskop tüpü |
| S03 | İrade Kilitlenmesi | Pilot HUD retikülünü kilitler | 85mm · CU · ön açı (aynalı vizör) | Kask içi nefes | Baş eğme hareketi |
| S04 | Alışkanlık Jesti | Pilot öteleme kolunu tıklatır | 50mm · ECU · üst açı | Mekanik klik (iç) | El: 2 kez tıklatma |
| S05 | Hizalanma | Pod kalkan kenarına yanaşır | 35mm · MS · yan açı | Dış mutlak sessizlik | RCS beyaz gaz patlaması |
| S06 | Oran Karesi | Dev kalkan yanında tiny pod | 18mm · V3 EWS · üst açı | HELIOS yaklaşma telemetrisi | Ölçek farkı %1/30 |
| S07 | İlk Başarısızlık | Yumuşak temas geri teper | 50mm · MCU · yan açı | Dış sessizlik + iç sarsıntı | Pod yalpalaması |
| S08 | Kaçan Pencere | Gölge teleskoptan uzaklaşır | 35mm · OTS · göz seviyesi | HELIOS süre uyarısı + alarm | Alarm ışığı yansıması |
| S09 | Sensör Kaybı | Energetic particle event telemetriyi yıkar | 24mm · FS · alt açı | HELIOS telemetri bozulma sesi | Işık parlaması |
| S10 | Tereddüt | Opak vizörde İPTAL kolu yansıması | 85mm · CU · ön açı | Hızlı nefes (iç) | Göz/baş: İPTAL koluna yöneliş |
| S11 | Abort Emri | AI geri dönüş emri verir | 35mm · OTS · göz seviyesi | HELIOS "Abort" emri | Omuz gerilmesi |
| S12 | Karar / Kırılma | Tıklatmadan kapağı kaldırır | 50mm · ECU · üst açı | Sert kapak mekanizması | El: tıklatmasız akıcı kaldırma |
| S13 | Karlı Hücum | Ana iticiler kalkan rail'ine hücum eder | 24mm · WIDE · arka açı | İtki bas sarsıntısı (iç) | İtici alevi (görsel) |
| S14 | Moment Kolu / Doruk | Galling + yapışma, pod tork uygular | 35mm · MS · yan açı | Dış sessizlik + iç tutulan nefes | Taze metal parlaması |
| S15 | Durgun Gölge | Gölge sabit, SHADOW ERROR: 0.000 | 35mm · OTS · göz seviyesi | HELIOS "Shadow lock stabilized" | Eller konsoldan inik |

---

## 👁️ KARAKTER VE NİTELİK KİLİTLERİ

### PILOT
- **Giyisi:** Antrasit gri EV-suit, mat karbon fiber göğüs plakası, omuzlarda sarı-siyah ikaz şeritleri.
- **Kask/Vizör:** **Opak siyah aynalı vizör** (D197 — iç yüzey/yüz görünmez, TEK NİTELİK KİLİDİ).
- **Davranış:** Sessiz, prosedürel, ekonomik hareketler. S04'te 2 tıklatma, S12'de tıklatmasız karar.

### SERVİS PODU (HELIOS)
- **Dış Görünüş:** Mat beyaz seramik kaplama, titanyum sivri burun konisi, sarı RCS nozulları. Kalkanın 1/30'u boyutta.
- **İç Kabin:** Loş kehribar HUD aydınlatması, sarı-siyah İPTAL kolu, sağ tarafta mavi şeritli öteleme kolu.

### GÜNEŞ KALKANI & TELESKOP
- **Kalkan:** 500m genişliğinde sekizgen karbon-seramik siyah düz panel. Kenarında titanyum-tantal (Ti/Ta) sacrificial capture rail.
- **Teleskop:** Kalkanın arkasında 80m boyunda silindirik gümüş-altın folyo kaplı kriyojenik teleskop tüpü.

---

## 🔊 SES FİZİĞİ VE DİL MİMARİSİ

```
DIŞ KAMERA (VAKUM):
- Mutlak sessizlik. Motor patlamaları yalnız GÖRSEL. Metal teması sessiz.
- Yalnız telsiz taşıyıcı cızırtısı.

İÇ KAMERA (KABİN):
- Yapısal titreşim (contact vibration), valf mekanik tıkırtısı, kabin alarmı, nefes.
- HELIOS AI akuzmatik sesi (yalnız telemetri, direktif, sayı).
```

---

## 📋 REPLİK ENVANTERİ

```
S01: HELIOS: "Sunshield gyro: locked. Shadow drift: point zero zero eight radians per second."
S02: HELIOS: "Telescope thermal limit in four minutes. Shadow drift accelerating."
S06: HELIOS: "Approach nominal. Two meters to contact."
S08: HELIOS: "Capture failed. Telescope thermal limit in ninety seconds."
S09: HELIOS: "Telemetry corrupted. Sensor confidence: zero."
S11: HELIOS: "Abort. Remaining delta-v below return reserve."
S15: HELIOS: "Shadow lock stabilized. Telescope array: safe."
```
