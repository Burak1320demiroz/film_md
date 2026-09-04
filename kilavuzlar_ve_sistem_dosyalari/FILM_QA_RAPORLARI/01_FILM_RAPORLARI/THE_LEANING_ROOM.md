# 🎬 THE LEANING ROOM — FİLM KAYDI

```
FİLM:      THE LEANING ROOM  ·  yatay_2_4_dk_filmler_uzay/THE_LEANING_ROOM/
YAZIM:     02.09.2026        ÜRETİM: 02.09.2026 (aynı gün)
PARTİ:     sekiz mercek (① ② ③ ④ ⑤ ⑥ ⑦ ⑧) · Gemini · 02.09.2026
SONUÇ:     🚨 PARTİ GEÇERSİZ — 8/8 mod V, SPEC ve QA paketi VARDI [D129]
           T tablolarına SATIR YAZILMADI. Kesme listesi / REMOVE reçetesi /
           yeniden üretim önerileri UYGULANMADI.
```

---

## ⑪ ÖLÇÜM KAPISI — koşuldu, hakemlik etti

### ⑪.0 KİMLİK [D160]

```
Master yolu verilmedi → aynı adı taşıyan HER dosya listelendi ve ölçüldü:

  ~/Downloads/the leanıng room.mp4        1920×1080 · 125,000 s · 3750 kare · 30 fps
  ~/Downloads/the leanıng room (1).mp4    3840×2160 · 125,000 s · 3750 kare · 30 fps

Aynı kurgu, iki çözünürlük. ÖLÇÜLEN: (1).mp4 (4K).
Kimlik karesi (kurgu ortası, 62,5 s) çıkarıldı ve BAKILDI → SPEC C bloğuna
OTURUYOR: ceviz kaplama salon · sancak bant penceresi · pirinç sarkaç lamba ·
altı gevşek eşya · masaya gömülü pirinç el çarkı · tek insan · kask 0 kare.
⛔ Koşu DURMADI: bu film, bu SPEC'in filmidir.
```

### ⑪ ÖLÇÜM TABLOSU

| ne | ölçüm | plan | verdikt |
|---|---|---|---|
| SÜRE | 125,000 s | 120,0 s | ⛔ +5,0 s — kuyruk kartı |
| ÇÖZÜNÜRLÜK | 3840×2160 | ⬜ | ✅ |
| FPS | **30** | ⬜ (plan yazmadı) | ⚠️ sekiz raporun sekizi **24 fps varsaydı** → hesapladıkları her süre %25 yanlış |
| SES KANALI | VAR | sesli | ✅ [D136 tetiklenmedi] |
| KESME IZGARASI | 30·40·50·60·70·80·90·100·110·120 s | 10 s katları | ✅ ızgara doğrulandı (karanlık sahnelerde erken kesmeler dedektöre görünmedi) |
| SAHNE SAYISI | 12 (+kart) | 12 | ✅ |
| KESME SAYISI | 11 (film gövdesi) | 11 | ✅ |
| SESSİZLİK | silence_start **119,999979** → silence_end 125,013 · 5,013 s | — | ⛔ kart sessiz, gövde 120,0 s'de bitiyor |
| FREEZEDETECT | donmuş 120 → SON | — | 🔴 **KUYRUK KART DOĞRULANDI** |
| LOUDNESS | **I = −32,0 LUFS** · peak −2,6 dBFS | −14 LUFS / −1,0 dBTP | 🔴 **18 LU kilidin altında** |
| FİLİGRAN (köşe testi) | dört çeyrek · 25 s'de bir | — | ✅ sabit işaret YOK |

```
⚠️ BETİK NOTU: olcum_kapisi.sh görselleri ÇALIŞMA DİZİNİNE yazıyor
   (kose_*.png · son_kare.jpg · sahne_izgarasi.jpg). Depo kökünden koşulursa
   depoya düşer. Bu koşuda düşenler SİLİNDİ; bundan sonra scratchpad'den koşulur.
```

---

## SPEC KAPISI [D129] — ⛔ PARTİ BURADA DÜŞTÜ

```
ls yatay_2_4_dk_filmler_uzay/THE_LEANING_ROOM/*_QA_SPEC.md   → VAR
ls QA_PROMPTLARI/FILME_OZEL/THE_LEANING_ROOM/                → VAR (8 paket)

⭐ Paket, filmin YAZIMINDA üretilmişti — D165 tam olarak bunun için yazıldı
   ve bu koşuda ARAÇ ÇALIŞTI, KART KOŞULMADI: operatör paketi değil çıplak
   rubriği yapıştırdı.

Sekiz raporun sekizinin ilk satırı:
  ① INPUT MODE: V      ⑤ (mod satırı yok)
  ② (video-only rubrik) ⑥ INPUT MODE: V
  ③ (video-only rubrik) ⑦ INPUT MODE: V
  ④ INPUT MODE: V      ⑧ INPUT MODE: V

→ KOŞU TEKRARLANIR. Ham raporlar 02/'ye düştü. T tablolarına satır YAZILMADI.
→ SPEC yazılıyken mod V koşulan film sayısı: 9 → **10** (THE COLD WELD 9.'ydu)
```

### ①.5 RAPOR KONTROL BETİĞİ [D161 · D162]

```
python3 RAPOR_KONTROL/rapor_kontrol.py <8 ham rapor> \
        --film yatay_2_4_dk_filmler_uzay/THE_LEANING_ROOM \
        --hook 10 --klip 10 --olcum-kesme 11 --olcum-sahne 12

TOPLAM 8 rapor · 🚨 8 GEÇERSİZ · ⛔ 0 TEKRAR · ⚠️ 0 ŞARTLI · ✅ 0 GO

⑤ ÇAPRAZ KAPI çıktısı:
  · ⑪ ÖLÇÜM HAKEM: kesme = 11 → ① 11 ✅ · ② 12 · ③ 11 ✅ · ④ 11 ✅
  · sahne ekseni ölçümle doğrulandı (12) ✅
  · replik ekseni doğrulandı — 5 mercek, 0 replik ✅
  · ⚠️ ŞERİT — çoğunluk `1111-1111-1-` (4 mercek); sapan: ① KARE `1111-1111-11`
  · ⚠️ D166 tetiklendi: ⑥ ve ⑧'in PREMISE REGISTER'ı ortamı yazdı, kuralı değil
```

---

## ⑩ ÖNERME KAPISI — bulguların plana karşı okunması

> Her bulgu planın logline + sahne haritası + kilit listesine karşı okundu.
> **Düşen bulgu, o merceğin puanını geri verir.** Parti zaten geçersiz olduğu
> için puan yeniden hesaplanmadı; düşme kaydı gelecek koşu için tutuldu.

| bulgu | kim yazdı | verdikt | kanıt |
|---|---|---|---|
| "1:17 — arka plandaki cisim ÇAPRAZ YUKARI düşüyor, 1g'yi ihlal ediyor 🔴" | ① ③ ⑥ | ⛔ **DÜŞER** | 1:16-1:18 arası 6 kare çıkarıldı (kare 2280-2340). Lamba altı karede **kesintisiz tek yönde** yatıyor, gevşek eşya lambanın yattığı yöne kayıyor. Bu, filmin KURALIDIR: "aşağı" itki yönüne göre yatar. Üç mercek filmin novum'unu 🔴 BLOCKER saydı [D166'nın ilk TEKRARI] |
| "PREMISE REGISTER: Earth-normal 1g" | ⑥ ⑧ | ⛔ **DÜŞER** | SPEC C bloğu: ağırlık YALNIZ itkiden gelir · yatma 0°→4°→22°→68°→3°. Ortam kaydedildi, kural kaydedilmedi |
| "lamba 2,0 s periyotlu sarkaç → g ≈ 9,8" | ⑥ | ⛔ **DÜŞER** | Lamba SALLANMAZ: sabit ivmede sabit açıda durur. Ölçülen "periyot" iki ayrı yatma geçişidir |
| "1:10'da tahta dümen yoktan var oluyor" | ② ⑦ ⑧ | ✅ **AYAKTA** | S0/S1/S3/S5'te masaya gömülü DÜZ pirinç çark + işaretsiz kol sırası; S7/S10'da klasik parmaklıklı gemi dümeni. Kare ile doğrulandı |
| "0:52 halat pirinç lamba gövdesinden geçiyor" | ① ② ⑤ ⑥ | ✅ **AYAKTA** | Kordon lambada bitmiyor, konsola kadar iniyor ve elinde |
| "gezegenler pencerede ışınlanıyor" | ② ⑤ ④ | ⚠️ **YARISI DÜŞER** | Kütle dizisi PLANLIDIR (buz dünyası → toz dünyası → karadelik → halkalı dünya). Ama geçiş 0 kare: yolculuk görünmüyor → okuma haklı, gerekçe yanlış |
| "ending stops — swinging lamp, no payoff" | ④ | ⛔ **DÜŞER** | 1:55 karesi: pirinç gövdede **İKİ EZİK** yan yana (biri mat/eski, biri parlak/yeni). D141'in FİNAL VURUŞ KANITI **BULUNAN** ve sayılabilir. Dört mercek onu hiç anmadı [D151'in 3. vakası] |
| "kesme listesi: S5, S10, S9 çıkarılsın" | ④ | ⛔ **UYGULANMAZ** | S4 ve S9 planda **VİRAL ARA ⛔ KESİLEMEZ** ve ikisi de novumun insansız kanıt sahnesidir. Mod V bunu bilemezdi — D129'un maliyeti |

---

## 📷 KARE İLE DOĞRULANAN — ne tuttu, ne düştü

### ✅ TUTAN (kareyle görüldü)

```
S0  0:05  altı gevşek eşyanın ALTISI masada (anahtar+deri etiket · nehir taşı ·
          katlanmış gözlük · sarılmış atkı · pirinç küre · sığ tabak) ·
          masaya gömülü DÜZ pirinç el çarkı + işaretsiz kol sırası ·
          ceviz kaplama · sancak bant penceresi SCREEN-RIGHT · tek insan
S3  0:35  omuz üstü · pruva camında halkalı varış noktası, küçük ve merkez dışı
          ⭐ D139: sırt tek parça ceviz-gri yün, kesintisiz, üstünde hiçbir şey yok
          — ÜÇ omuz üstü kurulumunun ÜÇÜNDE de tuttu
S4  0:45  ECU · çekiçlenmiş pirinç abajur · altında anahtar + deri etiket ·
          İNSAN 0 ✅ · yıldız alanı sancakta ✅
S7  1:18  ⭐ KAPAK KARESİ: oda yatmış, lamba neredeyse yatay, kordon gergin ·
          camın ötesinde KUSURSUZ SİYAH DAİRE + ince ışık halkası ·
          yığılma diski YOK ✅ (planda böyle yazılıydı) · kucak kemeri gergin ·
          yüz tam aydınlık ve okunur ✅ · masa boş
S9  1:35  ⭐ BEDEL EKRANDA: koltuk BOŞ · masa boş · gevşek eşyalar sancak
          penceresinin dibindeki pirinç korkulukta sıralanmış ✅ ·
          dışarıda yalnız yıldız alanı ✅ · yalnız lambanın havuzu ✅
S11 1:55  ⭐ FİNAL VURUŞ: ECU · pirinç gövdede İKİ EZİK yan yana ·
          arkada kadın odak dışı ve kımıltısız ✅ · pruva camında halkalı
          dünya artık okunur disk ✅ · masada dört eşya sıra hâlinde ✅
```

### ⛔ DÜŞEN (kareyle görüldü)

```
🔴 D1  NOVUMUN YÖNÜ TERS. S7'de lamba SCREEN-LEFT'e yatıyor; siyah daire
       SCREEN-RIGHT'ta. S9'da eşyalar SCREEN-RIGHT korkulukta.
       Plan: "yatma 12/12 SCREEN-RIGHT'a · ters dönüş YOKTUR."
       → Novum geldi, İŞARETİ yuvarlandı. → YENİ DERS 174

🔴 D2  TAŞIYICININ KORDONU AYRI BİR ÇEKME HALATINA DÖNDÜ. S3/S5/S8'de örgü
       kordon lambada bitmiyor, konsola iniyor ve kadının elinde; S8'de
       pirinç karşı ağırlıklar takılmış. Sekiz merceğin SEKİZİ filmi
       "halat çekerek manzarayı değiştiren kadın" diye okudu. → YENİ DERS 172

🔴 D3  KUYRUK KARTI 120,0-125,0 s · yanmış metin "THE LEANING ROOM".
       Plan: SCREEN TEXT 0,0 s. Makineyle doğrulandı (freezedetect + silencedetect).
       ⛔ Kart ayrıca filmin KENDİ karadeliğiyle çelişiyor: kartta yığılma diskli
         parlak girdap var, filmde lensli siyah daire. Ve kartın odası filmin
         odası DEĞİL (Viktoryen salon, tablolar, bitki).
       → D70/D72'nin **10. vakası** — yeni ders değil, sayaç arttı

🔴 D4  LOUDNESS −32,0 LUFS (kilit −14). 18 LU altında. → ihraç kilidi
       2. vaka (THE COLD WELD −18,1 LUFS'tu) — yeni ders değil, sayaç arttı

🟠 D5  KONSOL MORFU: düz pirinç el çarkı (S0·S1·S3·S5) ↔ parmaklıklı gemi
       dümeni (S7·S10). "Wheel" ceviz-pirinç gemi içinde arketipine çöktü.
       → D128'in TEKRARI (malzeme/nesne tarifi en yakın eğitim nesnesine yuvarlanır)

🟠 D6  S8 BAŞKA BİR ODA: aydınlık, farklı kaplama, pencerede Jupiter benzeri
       gaz devi; planda S8 zemin hizasından, geri çekilen siyah halka.

🟠 D7  PENCERE YANSIMASINDA İKİNCİ FİGÜR: S0 · 0:05, sağ camda oturan bir
       kadın silueti okunuyor. Negatif çekirdek: "no reflected figure".
       Kendi yansıması ama kilidin engellemek için var olduğu şey bu.
```

---

## 🚨 RAPOR TARAFI — partinin asıl bulgusu

```
① 8/8 MOD V. SPEC vardı, paket vardı, ikisi de aynı gün üretilmişti.
   D165'in aracı çalıştı; D165'in KARTI koşulmadı.

② ÜÇ MERCEK FİLMİN NOVUM'UNU 🔴 BLOCKER SAYDI. ⑥ FİZİK'in kendi PREMISE
   GATE'i var ve "kuralın imkânsızlığı asla bulgu değildir" diyor — kapı
   koştu ve ORTAMI kaydetti: "Earth-normal gravity (1g)".
   ⛔ D166'nın **İLK TEKRARI**. Aynı arıza, yeni film, yeni mercek (⑧ de yaptı).

③ SEKİZ MERCEĞİN SEKİZİ 24 fps VARSAYDI; dosya 30 fps. Hesapladıkları her
   süre, her "kaç kare" ve ⑥'nın bütün g hesapları %25 kaymış.
   ⛔ Rubrikler "FRAME RATE ASSUMED" yazdırıyor ama ASSUMED'ı ölçtürmüyor.

④ DÖRT MERCEK FİNALİN İKİ EZİĞİNİ HİÇ ANMADI — filmin tek ödemesi.
   ④ HİKAYE "the ending stops" yazdı. D151'in 3. vakası.

⑤ ⑤ ÇAPRAZ KAPISI DOĞRU MERCEĞİ SAPAN İLAN ETTİ.
   Çoğunluk (4 mercek): `1111-1111-1-`  → S11 insansız
   ① KARE tek başına:    `1111-1111-11` → S11'de insan var
   1:55 karesi: kadın koltukta, odak dışı, arkada. **① haklı, çoğunluk yanlış.**
   → YENİ DERS 173
```

---

## 📊 T TABLOSU SATIRI

```
⛔ YAZILMADI. Parti 8/8 GEÇERSİZ [D129].
   Bu filmin T1-T6 hücreleri BOŞ kalır ve 00_INDEX tamlık matrisinde 0/4 durur.
   Koşu tekrarlanacaksa paket buradan alınır:
     QA_PROMPTLARI/FILME_OZEL/THE_LEANING_ROOM/PAKET_1..8
   ve raporun ilk satırı `INPUT MODE: D` olmak ZORUNDA.
```

## 🔧 ÜRETİM TARAFINA ZORUNLU İŞLER (tekrar koşudan ÖNCE)

```
1. 🔴 KUYRUK KARTI KESİLİR. 120,0-125,0 s çıkar; ⑪ yeniden koşulur.
   Kart S0 ↔ S11 açılış-kapanış çiftini de öldürüyor.
2. 🔴 LOUDNESS: −32,0 → −14 LUFS yeniden ihraç.
3. 🔴 YÖN: S7 (ve yatmanın göründüğü her sahne) yeniden üretilir —
   yatma, siyah dairenin BULUNDUĞU tarafa. D174'ün reçetesiyle.
4. 🔴 KORDON: S3/S5/S8 yeniden üretilir — kordon lambada biter, elin
   erişemeyeceği yerde. D172'nin reçetesiyle.
5. 🟠 KONSOL: S7/S10 düz pirinç çarkla yeniden üretilir (D128 reçetesi).
6. 🟠 S8 planın kadrajına döner (zemin hizası, geri çekilen halka).
```
