# 🌾 THE_MIRROR_FAUNA — QA VE DERS HASADI

> **Amaç:** `00_OKUMA_CIZELGESI.md` sürecinde okunan kılavuz, ders, QA raporu ve red defterinden bu filme (`THE_MIRROR_FAUNA`) doğrudan süzülen kilitlerin ve engellerin derlemesidir.
> ⛔ Ders metinleri kopyalanmaz; **bu filme düşen somut kilit ve önlem** yazılır.

---

## 1. DERS VE KILAVUZ KİLİTLERİ

| # | kaynak | konu / arıza | bu filme uygulanacak KİLİT |
|:--:|---|---|---|
| 1 | `DERSLER/01_KAMERA_VE_KESME.md` | Monoton lens / aynı açı | Ardışık sahnelerde aynı odak uzaklığı (ör. 50mm -> 50mm) kullanılamaz. 35mm Anamorphic (geniş), 50mm Prime (orta), 85mm Macro (yakın) arasında en az 1 kademe sıçranacak. |
| 2 | `DERSLER/02_KARAKTER_VE_CANLI.md` | Yaratık kinesik bozulması | Taklitçi varlık (Mirror Fauna) reveal merdiveni (K0 Reveal: Gölge/Anten -> K1: Siluet -> K2: Işıldayan Antenler -> K3: Dört Ayaklı Beden -> K4: Astronot Kinetik Taklidi). |
| 3 | `DERSLER/03_FIZIK_VE_HAREKET.md` | I2V t=0 yanılsaması (D179) | Görsel prompt değişimin *sonrasını* değil, hareketin başlangıç anını (t=0) tanımlamalıdır. Taklit hareketi 🎥 VIDEO PROMPT'unda `starting from still posture` olarak başlatılacak. |
| 4 | `DERSLER/04_ISIK_VE_CEVRE.md` | Zemin çelişkisi (D176) & Işık takvimi (D193) | TRAPPIST-1e zemini iki ayrı promptta farklı tarif edilemez (sabit: "violet crystalline regolith with bioluminescent cyan moss"). Işık takvimi sahneler boyu monoton azalmayacak, varlığın biyo-ışığı ile dinamik dalgalanacak. |
| 5 | `DERSLER/05_EKIPMAN_VE_VARLIK` | Kask ve vizör kayması (D146) | Astronot A (Kaptan Vance - Mavi göğüs şeridi, sol bilek saati) ve Astronot B (Uzman Ray - Turuncu göğüs şeridi). Kask vizörleri altın yansımalı ve kilitli kalacak. |
| 6 | `DERSLER/06_METIN_VE_PROMPT` | Replik işlevi & Lip-sync (D122) | Replikler diyalog işlev sütununa sahip olacak. Ağız hareketi lip-sync riski taşıdığı için diyalog anlarında kask vizör yansıması veya kadraj dışı ses / telsiz modülasyonu tercih edilecek. |
| 7 | `DERSLER/07_KURGU_VE_ANLATI` | Üretim sırası hatası (D168) | Üretim sırası: S09 (Doruk - Dokunma/Taklit anı) -> S05 (Merkezî Seçim) -> S00 (Hook) -> Kalan sahneler. |
| 8 | `ASTRONOT_DONANIM_VE_KIMLIK` | Donanım çakışması | Astronot giysileri üzerinde metin içermeyen pürüzsüz grafik amblem (geometrik çember ve iki nokta) kullanılacak. |
| 9 | `UZAYLI_VARLIK_TASARIM` | Uzaylı kalıbı | Tek uzaylı türü: Dört ayaklı, yüzsüz, lavanta-mor yarı saydam biyolüminesans kaplı deri, sırtından uzayan 4 esnek biyo-ışık anteni. |
| 10 | `UZAY_USSU_VE_ISTASYON` | Ölçek şahidi | Keşif aracı / Modül kadrajda olduğunda 1H = 1.8m kasklı astronot boyu ölçek birimi olarak prompta yazılacak. |

---

## 2. QA ARIZALARI VE ÖLÇÜLMÜŞ RİSKLER

| # | kaynak | ölçülmüş arıza / skor | bu filme uygulanacak ÖNLEM |
|:--:|---|---|---|
| 1 | `THE_OPEN_CIRCUIT` | Lens nesneyi kadraja sığdıramadı (5.9m kadraj / 64m üs) | Optik Aritmetik: 35mm lens ile 10m mesafeden 4m'lik varlık ve 1.8m astronot tam kadrajlanacak. Kadraj eni en az 8m olacak. |
| 2 | `THE_STILL_SWARM` | Sürü kinetiği takılması / morfolojik bozulma | Aynı anda ekranda en fazla 1 ana taklitçi varlık ve arka planda siluet halinde 2 varlık yer alacak. Kaotik sürü yazılmayacak. |
| 3 | `T1_KARE_KALITE` | Nesne piksel küçüklüğü (<60px) | Ana odak nesnesi (astronot eli veya varlığın anteni) yakın çekimlerde kadrajın en az %25'ini kaplayacak (≥100px). |
| 4 | `T2_DEVAMLILIK_KALITE` | Klip içi durum değişimi zayıflığı (T2V 0.0687) | Klip içinde karmaşık dönüşüm yapılmayacak. Durum değişimi (astronotun el kaldırması -> varlığın anten kaldırması) sahne sınırına (End frame / Start frame) taşınacak. |
| 5 | `T11_ISIK_KALITE` | Monoton kararma | Fırtına/alacakaranlık sahnelerinde ortam ışığı düşerken biyo-ışık kontrastı artırılarak ışık kaynağı dengelenecek. |

---

## 3. ÜRETİM RED DEFTERİ VE POLİTİKA KISITLARI

| # | red sınıfı / tetikleyici | motor / risk | bu filme uygulanacak POLİTİKA KİLİDİ |
|:--:|---|---|---|
| 1 | Çıplak deri / Anotomik yanlış algı | Veo / Runway / Sora | Uzaylı varlık insansı (humanoid) bacak/gövde/yüz taşımayacak. Dört ayaklı (quadruped) hayvanımsı/böceğimsi nötr siluet olacak. Çıplak insan derisi hissiyatı veren pembe/ten rengi YASAK. Parlak lavanta-mor biyolüminesan doku yazılacak. |
| 2 | Şiddet / Kan / Askeri Çatışma | Politik Filtre | Astronotların elinde ateşli silah bulunmayacak. Yanlarında sadece bilimsel tarama cihazı (scanner / telemetri feneri) yer alacak. |
| 3 | Bayrak / Milliyet Emtiyası | Politik Filtre | Astronot giysilerinde gerçek ülke bayrağı (US, TR, CN vb.) olmayacak. Yalnızca kurgusal uzay kurumu amblemi ve göğüs rol şeritleri (Mavi/Turuncu) bulunacak. |
| 4 | Yasaklı Kelimeler | Prompt Kontrol (⑯) | Prompt metinlerinde `alien, monster, blood, kill, weapon, skin, nude` kelimeleri kullanılmayacak. Yerine `extra-terrestrial fauna, bioluminescent quadruped entity, telemetry scanner` yazılacak. |

---

✅ Hasat tamamlandı. Bütün kilitler `02_KONSEPT_VE_RISK.md` ve sahne çalışmalarına taşınmaya hazırdır.
