# 🔍 QA PROMPTLARI — RUBRİK KLASÖRÜ REHBERİ

> **Üç dosya türü, üç ayrı ev:**
>
> | Ne | Nerede |
> |---|---|
> | Rubrik (girdi — filmi eleştiren prompt) | **bu klasör** · `*_CRITIQUE_PROMPT.md` |
> | Rapor (çıktı — skorlar, bulgular) | `../FILM_QA_RAPORLARI/` |
> | Çalıştırma kayıtları + operatör dipnotları | `CALISTIRMA_KAYITLARI.md` (bu klasörde) |

---

## ⭐ SALT PROMPT İLKESİ (12.08.2026)

**Her rubrik dosyası yalnız prompt içerir.** Dışarıdaki herhangi bir modele
**medya + tek .md dosyası** verirsin, başka hiçbir şey vermezsin; rapor gelir.

```
ÇALIŞTIRMA TARİFİ — üç adım:
1. Aşağıdaki tablodan doğru rubriği seç
2. Rubrik dosyasının TAMAMINI kopyala + medyayı (video/kurgu) yükle
   · filmin planında 📋 QA SPEC BLOĞU varsa (2-4 dk dosyalarında §0.15):
     KES, rubriğin SPEC/SCENE SPECIFICATION alanına YAPIŞTIR → MOD D
   · SPEC yapıştırmadıysan koşu MOD V'dir ve bunun bedeli vardır [DERS 94]
3. Gelen raporu asla doğrudan tabloya işleme —
   aşağıdaki 🤖 AJAN KULLANIMI bölümündeki karta göre işle

⛔ HER MERCEK TEMİZ OTURUMDA KOŞULUR [DERS 110]
   Yeni sohbet · yalnız medya + tek rubrik. Aynı oturumda ikinci bir
   rubrik çalıştırma: mercekler birbirinin sahne haritasını, zaman
   kodlarını ve severity sayımını devralıyor. O zaman "dört mercek aynı
   şeyi gördü" bir doğrulama değil, tek raporun dört kopyasıdır.

⛔ ÖNCE KURGU KAPISI, SONRA QA [DERS 109]
   Klip sayısı = plan SCENE COUNT ve süre = plan RUNTIME ±2 s değilse
   koşu ÖN KOŞU'dur; film boyuna bakan kategoriler puan taşımaz.
```

Bu yüzden rubrik dosyalarına ŞUNLAR YAZILMAZ:
- Türkçe operatör notu, tarihçe, çalıştırma kaydı → `CALISTIRMA_KAYITLARI.md`
- `[DERS n]` / `[LESSON n]` etiketi, tarih, film adı, koşu anlatısı,
  depo yolu (`../LESSONS_LEARNED.md` vb.) → aynı dosya, iz defteri bölümü
- film-özel sayı/kural → `FILME_OZEL/<FILM>_QA_CRITIQUE_PROMPT.md`
- skor, bulgu, rapor özeti → `../FILM_QA_RAPORLARI/`

Ders yamaları rubrik gövdesine **yalnız İngilizce kural olarak** girer —
numarasız, tarihsiz, film adsız (17.08.2026 temizliği). Modelin göremediği
bir belgeye atıf, onun için doldurulacak bir boşluktur. Dersin hangi rubriğin
hangi bölümünde yaşadığı `CALISTIRMA_KAYITLARI.md` · **DERS → RUBRİK İZ
DEFTERİ** bölümünde tutulur; tek izlenebilirlik kaydı orasıdır.

---

## 📦 MEVCUT RUBRİKLER — 6

| Dosya | Neyi eleştirir | Zorunlu girdi | Mod | Skor tablosu |
|---|---|---|---|---|
| `VIDEO_QA_CRITIQUE_PROMPT.md` | Teknik — 11 kategori, kare içi | yatay klip / montaj | D veya V | `../LESSONS_LEARNED.md` teknik tablo |
| `MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` | Mantık + kayma — sahneler arası | film (yalnız video) | tek mod | `../FILM_QA_RAPORLARI/04` |
| `KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` | Karakter kimliği + devamlılık | film (yalnız video) | tek mod | `../FILM_QA_RAPORLARI/06` |
| `SES_VE_DIYALOG_QA_CRITIQUE_PROMPT.md` | Ses — atıf, sentetik ses, miks | **TAM KURGU** (yalnız video) | tek mod | `../FILM_QA_RAPORLARI/07` |
| `SENARYO_QA_CRITIQUE_PROMPT.md` | Hikaye — dramaturji | film (+ PLAN = MOD D) | D veya V | `../FILM_QA_RAPORLARI/03` |
| `SHORTS_QA_CRITIQUE_PROMPT.md` | Dikey 9:16 — teknik + güvenli alan + hook | dikey klip(ler)/kurgu | D veya V | `../FILM_QA_RAPORLARI/05` |

**Altısı da kendi kendine yeter** — tek dosya + medya, başka hiçbir şey.

> 🎨 **KAPAK_QA 12.08.2026'da kaldırıldı** — 31.07'de yazılmıştı, bir kez
> bile çalıştırılmadı. Kapak denetimi artık rubriksizdir: 120 px posta pulu
> testi ELLE yapılır (yüz, duygu, eylem okunuyor mu — okunmuyorsa geri kalan
> hiçbir şey kapağı kurtarmaz). Kaynak: `../KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md`.

### Hangi filme hangi mercekler?

```
YATAY (2-4 · 3-5 dk)   VIDEO_QA + MANTIK_QA + SENARYO_QA   ← üç ana mercek
                       + KARAKTER_QA  (karakter ağırlıklıysa — opsiyonel)
                       + SES_QA       (diyalog/ses tasarımı varsa — opsiyonel,
                                       yalnız tam kurguya)
DİKEY SHORTS           SHORTS_QA      (tek rubrik, 16 kategori)
                       + SES_QA       (diyalog varsa)
7-9 dk                 BU KLASÖR DEĞİL → yatay_7_9_dk_filmler/kilavuzlar/
                       kalite_kontrol/ (3 geçişli ayrı sistem — skorları
                       buradaki tablolarla KARŞILAŞTIRILAMAZ)
```

⛔ **Bir filme koşulan bütün merceklere AYNI dosya verilir.** Starless
Circle'da iki mercek 12 s'lik klibi, iki mercek 2:54'lük kurguyu ölçtü —
dört skor aynı satıra yazılamadı [DERS 75].

---

## ⭐ İKİ GİRDİ MODU

Her rubrik raporunun ilk satırında hangi modda çalıştığını **ilan eder**:

```
MOD D — BELGELİ      medya + operatörün plan dosyasından kopyaladığı SPEC
                     BLOĞU. Tüm kategoriler puanlanır, TASARIMA UYGUNLUK
                     ölçülür. Skor tabloya işaretsiz girer.

MOD V — SADECE VİDEO medya + rubriğin kendisi. SPEC boş. Film KENDİSİYLE ve
                     FİZİKLE ölçülür. Belge isteyen her denetim puan almaz,
                     `FLAGS FOR DOCUMENT CHECK` altında SORUYA döner.
                     Satır tabloya `Ⓥ` (+ senaryoda ⚠️ ŞARTLI) girer.
```

- MANTIK / KARAKTER / SES rubrikleri **her zaman video-only** çalışır —
  doküman verilmez, baseline'ı STEP 1'de videodan kendileri kurar.
  "Eksik sahne/replik" raporlaması bu üçünde YASAKTIR.
- ⛔ **SPEC hazırken mod V koşmak bedava değildir [DERS 94]:** koşu bir ÖN
  KOŞU sayılır — skor Ⓥ ⚠️ ŞARTLI girer, tamlık matrisinde hücre ❌ kalır,
  kesme listeleri ve REMOVE reçeteleri uygulanmaz. Bu depoda mod D hâlâ hiç
  denenmedi; SPEC'i hazırken mod V koşulan film sayısı 4.
- `INPUT MISSING` hiçbir rubrikte geçerli çıktı değildir. Yaşayan üç
  durdurucu: `SPEC MISMATCH` (yalnız mod D) · `MEDIA MISSING` (oynatılabilir
  video yok [DERS 80]) · `AUDIO ABSENT` (yalnız SES_QA STEP 0).

---

## 🤖 AJAN KULLANIMI — rapor geldiğinde ne yapılır

> Rubriği çalıştırmak işin yarısı; **raporu işlemek ayrı bir disiplindir.**
> Her merceğin `AGENTS.md` §3'te bir görev kartı var. Kartı açmadan tabloya
> skor yazma.

| Gelen rapor | Görev kartı | Ham rapor dosyası | Skor satırı |
|---|---|---|---|
| VIDEO_QA (teknik) | **C** | `02_HAM_RAPORLAR/<FILM>_TEKNIK_HAM.md` | LESSONS_LEARNED teknik tablo |
| SENARYO_QA | **D** | `<FILM>_SENARYO_HAM.md` | 03 tablosu |
| MANTIK_QA | **E** | `<FILM>_MANTIK_HAM.md` | 04 tablosu |
| KARAKTER_QA | **E2** | `<FILM>_KARAKTER_HAM.md` | 06 tablosu |
| SES_QA | **E3** | `<FILM>_SES_HAM.md` | 07 tablosu |
| SHORTS_QA | kart C'nin dikey uyarlaması | `<FILM>_SHORTS_HAM.md` | 05 tablosu |

**Her kartın değişmez ilk adımları** (ayrıntı AGENTS.md §3, C/D/E ortak blok):

```
① SPEC KAPISI [D94]      planda SPEC vardı da mod V mi koşuldu? → ÖN KOŞU
② KİLİT ÇELİŞKİSİ [D96]  rapor, planda YAZILI bir kilide aykırı bulgu mu
                         veriyor? → bulgu listeden çıkar, deftere yazılır,
                         master'ın o saniyesi izlenerek çözülür
③ HAM RAPORU KAYDET      02_HAM_RAPORLAR/ altına, DÜZENLEMEDEN — bu depoda
                         11 filmin ham raporu bir kez kayboldu (kural ④)
④ FLAGS'İ CEVAPLA        FLAGS FOR DOCUMENT CHECK soruları plan/bible
                         dosyasından cevaplanır, cevap film kaydına yazılır —
                         video-only rubriklerin İKİNCİ YARISI budur
⑤ REÇETEYİ GREP'LE [D85] her REMOVE/REPLACE önerisi uygulanmadan önce:
                         grep -rn "<tam dize>" <film klasörü>/
                         boş çıkarsa veya dize yasağın içindeyse reçete DÜŞER
⑥ TABLO + 00_INDEX       skor satırı + tamlık matrisi aynı oturumda güncellenir
⑦ YENİ DERS → kart G     yama ÖNCE kaynak rubriğe (İngilizce kural, gövdeye,
                         numarasız); tarih/tutanak + "D<n> → hangi rubriğin
                         hangi bölümü" satırı CALISTIRMA_KAYITLARI.md'ye
```

**Ölçüm sapmasını unutma:** aynı rubrik aynı filmi iki kez ölçtü, kategoriler
2 puana kadar oynadı. 1.5'ten küçük skor farkları GÜRÜLTÜDÜR — "A filmi
B'den iyi" deme (AGENTS §2-⑥).

**Çalıştırma kaydı nereye:** koşu bittiğinde `CALISTIRMA_KAYITLARI.md`'de
ilgili rubriğin bölümüne tek blok eklenir:
`> Çalıştırma kaydı: son <tarih> — <FİLM> (mod, geçerlilik, skor, 1-2 bulgu)`.
Rubrik dosyasına YAZILMAZ (salt prompt ilkesi).

---

## 🎯 FİLME ÖZEL RUBRİKLER — `FILME_OZEL/` (sayıma girmez)

| Dosya | Film | Neyi ölçer | Girdi |
|---|---|---|---|
| `FILME_OZEL/THE_RING_LIGHT_QA_CRITIQUE_PROMPT.md` | THE RING LIGHT | aksiyon (planlı vuruş + ölü kare) ve filmin kendi sayısal kilitleri | tek klip (MOD K) veya tam kurgu (MOD F) |

```
⚠️ BUNLAR MERCEK DEĞİL, ÜRETİM KAPISIDIR.
   · 6'lık sayıma girmezler, skorları 03-07 tablolarına YAZILMAZ.
   · Verdikleri şey skor değil KARARDIR: KABUL / KURGUDA DÜZELT / YENİDEN ÜRET.
   · Genel merceklerin yerine geçmezler, önlerinde dururlar.

⛔ NEDEN AYRI KLASÖR: film-özel bilgi genel rubriğe ASLA girmez — SHORTS_QA
   31.07'de tam da bu yüzden sıfırdan yazıldı (eski sürüm "KULE 7" yapımına
   gömülüydü ve başka hiçbir filme uygulanamıyordu).

⭐ NE ZAMAN YAZILIR: filmin riski genel rubriklerin ölçmediği bir eksende
   yoğunlaşıyorsa (Ring Light: tasarımı gereği yavaş film — genel rubrik ya
   "durgun" diye cezalandırır ya ölü kareyi "tasarım" diye geçirir).
```

---

## 🗺️ KAPSAM HARİTASI — neyi ölçüyoruz, neyi ölçmüyoruz

| Üretim aşaması | Durum |
|---|---|
| Senaryo / yapı | ✅ SENARYO_QA |
| Görsel/video promptu (üretimden önce) | ✅ **`../PROMPT_KONTROL/`** — 12.08.2026'da açıldı: betik (sayar) + rubrik (yargılar) |
| Video — yatay, kare içi | ✅ VIDEO_QA |
| Video — yatay, sahneler arası | ✅ MANTIK_QA (+ derin mercekler: 🧍 KARAKTER · 🔊 SES) |
| Video — dikey | ✅ SHORTS_QA |
| Video — 7-9 dk | ✅ 3 geçişli sistem (kendi klasöründe, ayrı skor evreni) |
| Montaj bütünlüğü (planlanan sahne ekranda var mı) | ✅ kurgu kapısı [D70/72/81] + SENARYO_QA zirve kontrolü |
| Kapak / thumbnail | ⚠️ **rubriksiz** — 120 px testi elle (12.08.2026'dan beri) |
| Ses tasarımı / diyalog / miks | ✅ SES_QA |
| Müzik | ⚠️ kısmi — SES_QA §9 miksteki davranışı ölçer; beste ölçülmüyor |
| Başlık & açıklama paketi | ❌ yok |

### ⛔ KAPSAM DIŞI — bilinçli olarak ölçülmeyecek (05.08.2026)

```
KARAKTER & DÜNYA BIBLE'I / ANAHTAR KARE     girdiyi ölçmek — VIDEO_QA ve
   MANTIK_QA zaten SONUCU ölçüyor; tutmayan Bible ekranda kostüm-prop
   çelişkisi olarak zaten görünür. Ayrıca puanlamak aynı hatayı iki
   isimle iki tabloya yazar.
YAYIN SONRASI İZLEYİCİ VERİSİ               QA değil analitik — rubrik bir
   yapıma puan verir; izlenme verisi zaman serisidir, yeri tablodur.
```

⚠️ Bu satırları "eksik" sanıp yeniden açma — karar gerekçesiyle burada kayıtlı.

---

## 📝 DEĞİŞİKLİK KAYDI

```
12.08.2026  ⭐ RUBRİKLER SALT PROMPT'A İNDİRİLDİ
            Altı rubriğin sonunda biriken Türkçe ders dipnotları ve
            çalıştırma kayıtları (594 satır) CALISTIRMA_KAYITLARI.md'ye
            taşındı. İlke: rubrik .md + film = rapor; dosyada modelin işine
            yaramayan hiçbir şey durmaz. Yeni kayıtlar rubriğe değil
            CALISTIRMA_KAYITLARI.md'ye yazılır (kart G adım 5 güncellendi).

12.08.2026  🎨 KAPAK_QA_CRITIQUE_PROMPT.md KALDIRILDI
            31.07'de yazıldı, hiç çalıştırılmadı; 00_INDEX tamlık matrisi
            paydası 4→3'e indi. Kapak denetimi elle 120 px testi.
            Film dosyalarındaki işaretçiler güncellendi.

12.08.2026  Bu README sıfırdan yazıldı: salt-prompt ilkesi, çalıştırma
            tarifi, 🤖 ajan kullanım akışı (görev kartı eşlemesi) eklendi.
            Eski sürümün mod gerekçeleri ve tarihçesi korundu (aşağıda).

12.08.2026  FILME_OZEL/ klasörü açıldı — ilk dosya:
            THE_RING_LIGHT_QA_CRITIQUE_PROMPT.md (MOD K/F, kilit alıntılama
            zorunluluğu, ACTION UPLIFT çıktısı; skoru tablolara girmez).

09.08.2026  SES_VE_DIYALOG_QA yazıldı — ses merceği. VIDEO_QA §8'in ses
            tarafını film boyuna yayar; 9 kategori; REGISTER sütunu
            (HUMAN/MACHINE/UNCLEAR — seri diegetik yapay ses kullanıyor,
            register'sız "AI gibi konuşuyor" bulgusu çalışan tasarımı bozar);
            STEP 0 ses varlık kapısı (sessiz film ≠ sesi ihraç edilmemiş
            dosya). Yalnız TAM KURGUYA koşulur. Aynı gün ilk koşu:
            Cold Burn 5.0 → 07 tablosu açıldı, DERS 82-83.

05.08.2026  KARAKTER_DEVAMLILIK_QA yazıldı — MANTIK_QA 5. kategorisinin
            karakter tarafını derinleştiren opsiyonel mercek. 8 kategori;
            kimlik kırılması ve kopya karakter = BLOCKER. İlk koşu aynı gün:
            Stone Sky 6/10 → 06 tablosu açıldı, DERS 69.

05.08.2026  ⭐ MOD D / MOD V İKİLİĞİ EKLENDİ — rubrikler tek dosya çalışır
            Tetikleyen: üç Dawn Front koşusu repo erişimi olmayan modelde
            yapıldı, üçü de rapor üretemedi (INPUT MISSING / UNVERIFIABLE /
            altı kategori kapalı; üçü de modele repoda ls/grep çalıştırmasını
            söylüyordu). → INPUT MISSING geçersiz çıktı ilan edildi; mod V'de
            rubrik baseline'ını videodan kurar; belge isteyen denetim soruya
            döner; mod V satırı Ⓥ işaretlenir. Film-özel "tek dosya paketi"
            ihtiyacı bitti.

05.08.2026  Kapsam haritasından üç satır KAPSAM DIŞI ilan edildi
            (Bible QA · anahtar kare QA · izleyici verisi — gerekçeler yukarıda).

31.07.2026  MANTIK_VE_DEVAMLILIK_QA yazıldı (yatayın üçüncü merceği), aynı
            gün yalnız-video'ya çevrildi: "eksik" raporlaması yasaklandı,
            FLAGS FOR DOCUMENT CHECK doğdu, her bulgu iki timecode taşır.
            03 ve 04 skor tabloları açıldı (hikaye ve mantık skorları teknik
            skorla aynı tabloda toplanamaz).

31.07.2026  VIDEO_QA ve SENARYO_QA'ya STEP 0 SPEC DOĞRULAMA KAPISI eklendi
            (Low Power raporu var olmayan 7 sahnelik kurguyu puanlamış ve
            filmde ZATEN VAR olan iki beati eksik diye raporlamıştı).
            SENARYO_QA'ya zirve kontrolü + format tabanı uyarısı + sessiz
            filmde Diyalog N/A + viral ara sahne kesilemez kuralları eklendi.

31.07.2026  SHORTS_QA sıfırdan yazıldı (eski sürüm "KULE 7" yapımına
            gömülüydü). Kategori 1-8 isimleri VIDEO_QA ile aynı tutuldu.
            ⚠️ Dosya aynı gün bir kez dosya sisteminden kayboldu ve geri
            yazıldı; yedeği yok.

31.07.2026  PROMPT_QA yazıldı ve bu klasörden çıkarıldı → PROMPT_KONTROL/
            (klasör hiç açılmadı — kapsam haritasında açık boşluk).
            ✅ 12.08.2026'da kapandı. Ama 31.07'de yazılan dosya
            KURTARILAMADI: 18 commit tarandı, `PROMPT_QA` geçen tek bir
            blob yok — dosya taşınırken düştü, hiç commit'lenmedi.
            Sıfırdan yazıldı. ⛔ Ders: bir dosyayı klasörden ÇIKARMADAN
            önce gideceği klasör açılır; "sonra taşırım" bu depoda bir
            kez dosya kaybettirdi (SHORTS_QA, aynı gün) ve bir kez
            dosyayı hiç var olmamış hâle getirdi (bu).
```

> Rubriklerin koşu tarihçesi, ders dipnotları ve operatör kuralları:
> **`CALISTIRMA_KAYITLARI.md`** — bu README'de tekrarlanmaz.
