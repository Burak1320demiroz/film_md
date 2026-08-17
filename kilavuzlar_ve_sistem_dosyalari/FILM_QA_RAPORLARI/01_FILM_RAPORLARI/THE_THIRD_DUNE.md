# 🏜️ THE THIRD DUNE — FİLM QA KAYDI

> **Film:** THE THIRD DUNE · 16:9 yatay · 3-5 dk · `yatay_3_5_dk_filmler/THE_THIRD_DUNE/`
> **Plan:** 25 sahne (S0-S24) · 249 s · 10 replik · **Kurgu:** 245 s · 24 kesme (25 klip)
> **QA tarihi:** 11.08.2026 — dört mercek aynı gün, hepsi **mod V**
> **Ham raporlar:** `../02_HAM_RAPORLAR/THE_THIRD_DUNE_{TEKNIK,SENARYO,MANTIK,KARAKTER,SES}_HAM.md`

---

## 📊 BEŞ MERCEĞİN DURUMU

| Mercek | Skor | Verdict | Koşu |
|---|:--:|---|---|
| 🔧 VIDEO (teknik) | **4/10** Ⓥ | REGENERATE (3 🔴) | geçerli, mod V |
| 📖 SENARYO | **7.0/10** Ⓥ | SHOOT WITH TRIMS | geçerli, mod V ⚠️ ŞARTLI |
| 🧩 MANTIK | **7/10** | FIXABLE IN EDIT | geçerli ⚠️ üç MAJOR'ın ikisi belge kontrolünde düştü |
| 🧍 KARAKTER | **7/10** | DRIFTS BUT RECOVERABLE | geçerli, klonsuz |
| 🔊 SES | — | MEDIA MISSING | **🚨 GEÇERSİZ — video yüklenmedi [D80]** |

```
⭐ Deponun İKİNCİ beş mercekli filmi (ilki Cold Burn) — ama beşincisi
   girdisiz koştu. DÖRT mercek AYNI 245 s kurguyu ölçtü (D75 ✅),
   SES merceği hiçbir şey ölçmedi (D75 ✗).

🚨 OPERATÖR KURALI ② — 3. İHLAL: planın 856. satırında HAZIR bir
   `📋 QA SPEC BLOĞU` duruyor (film adı, 25 sahne, 249 s, 10 replik,
   register tablosu, viral sahne listesi, CENTRAL CHOICE, CLIMAX).
   Yapıştırılsaydı 🔧 ve 📖 mod D koşacak, aşağıdaki yanlış bulguların
   çoğu rapora hiç girmeyecekti. Mod D bu depoda HÂLÂ hiç denenmedi.
```

---

## ⚠️ ANA BULGU — ÜÇ ÇAPA KİLİDİ DE PROMPTTA YAZILIYDI VE ÜÇÜ DE KIRILDI

Bu filmin diğer QA'lardan farkı: **eksik yazılmış bir şey yok.** Önceki
filmlerde bulguların kökü çoğu kez "cümle promptta yoktu" çıkıyordu
(Starless Circle vizör, Blind Return sırt ünitesi). Burada üçü de yazılıydı:

| Kilit | Promptta | Kurguda | Kanıt |
|---|---|---|---|
| Sırt ünitesi yasağı | **42/42 promptta** negatifin içinde | iki suitte de sırt çantası | 🧍 pasaport · 🔧 envanter |
| Bant rengi (mor/buz mavisi) | PART_B'de 16× `DEEP-VIOLET` | 2:10'da mor bantlar tamamen yok | 🧍 1:30↔2:10 |
| Toz seviyesi (3 kademeli sayısal takvim + temiz referans şeridi) | her sahne için yazılı, S14-S23 = seviye 4 | 2:29 kaskatı kumlu → 2:40 tertemiz | 🧍 + 🧩 aynı bulgu |

```
⭐ SONUÇ: metin kilidi sahne İÇİNDE tutuyor, sahneler ARASINDA tutmuyor.
   Her klip önceki klibi görmeden üretiliyor; "seviye 4" yazan bir cümle
   modelin bir önceki karede ne yaptığını bilmesini sağlamıyor.
   → DERS 84. Çözüm prompt cümlesi değil, ÜRETİM ZİNCİRİ kararı.
   Sırt ünitesi bu filmle DERS 79'un 5. vakası oldu ve ilk kez cümlenin
   VARLIĞINA rağmen çıktı — yasak cümlesi bu nesnede ölçülebilir biçimde
   çalışmıyor.
```

---

## ⭐ FLAGS FOR DOCUMENT CHECK — CEVAPLAR

### 📖 SENARYO

**S1. "3:10'daki kokpit kararı (kütle mi süre mi) CENTRAL CHOICE mu?"**
→ **HAYIR.** Plan: `CENTRAL CHOICE: S17 — on bir örnek kasasının kuma
bırakılması`, `CLIMAX: S21 — kalkış`. 3:10'daki replik S16'nın ikinci
repliğidir ("Kütle mi, süre mi? İkisi birden yok.") — kararın GEREKÇESİ,
kararın kendisi değil. Rapor filmin doruğunu da (S21 kalkış) zirve
saymamış. Skor bu yanlış eşlemenin üstüne kurulu değil, ama **Yapı 7/10
okuması "doruk 3:10'da" varsayımıyla yazıldı** — film kaydına şerh düşüldü.

**S2. "S2 ve S6 viral ara sahne mi? Kesme listeme aldım."**
→ **İKİSİ DE KESİLEMEZ, reçete REDDEDİLDİ.** Plan: `VIRAL INTERSTITIALS:
S3 · S6 · S12 · S21 (bunlar KESİLEMEZ)`.
```
Raporun 1. kesme önerisi  0:20-0:40  → plan S2-S3  → VİRAL #1 (SALTASYON)
Raporun 2. kesme önerisi  1:40-2:00  → plan S10-S12 → VİRAL #3 + ORTA NOKTA
                                                       (ÜÇÜNCÜ TEPE reveal)
```
İkinci öneri filmin **REVEAL karesini** kesiyor — Kaleida Crash tuzağının
(viral ara sahneyi "oyalanma" sanma) tekrarı, bu kez filmin orta noktasıyla.

**S3. "0:50 — 'Kum taşınıyor' görüneni anlatıyor, kesilsin."**
→ **REÇETE REDDEDİLDİ.** Repliğin tamamı: **"Kum taşınıyor. Bu zemin dün
buranın zemini değildi."** Rapor cümlenin ilk yarısını alıntılayıp ikinci
yarısını atlamış; filmin ÖNERMESİ ikinci yarıda. Kesilseydi film kendi
kancasını kaybederdi.

### 🧩 MANTIK — üç MAJOR'ın ikisi düştü

**M1. "1:00 düz kumdaki araç ↔ 2:00 dik tepeye gömülü araç" 🟠 MAJOR**
→ **BULGU DÜŞER — bu filmin ÖNERMESİ.** Plan S12: *"40 m'lik yeni tepenin
kayma yüzü aracın sancak yanını yutmuş"*; ⑩ GÖMÜLME EKİ S12'den itibaren
aracın göründüğü TÜM sahnelere ekleniyor. Araç önce düz kumda, sonra
gömülü — filmin anlattığı şey tam olarak bu. Coğrafya 4/10 skorunun
gerekçesinin yarısı budur.

**M2. "3:30 kusursuz dairesel derin krater" 🟠 MAJOR**
→ **ÇELİŞKİ DÜŞER, TASARIM İHLALİ KALIR.** Plan S22 (ÇANAK) çanağı
tarif ediyor: *"a 14-metre-wide shallow circular depression… a
mechanically scoured depression, **not a blast crater**"*. Yani çanak
planlı → "farklı iniş alanı" okuması geçersiz. Ama ekranda **sığ süpürme
çukuru değil derin çarpma krateri** var → mod D koşulsaydı bu bir
UYGUNLUK bulgusu olarak yazılırdı. Yeniden üretim önerisi (3:30 geniş
çekim) **geçerli**, gerekçesi yanlış.

**M3. "2:25 kirli ↔ 2:41 temiz suit" 🟠 MAJOR**
→ **GEÇERLİ.** 🧍 ile aynı bulgu; kesişim kuralı gereği **KARAKTER
tablosunda** raporlandı (kart E2 adım 5), 04 tablosunda tek sayılır.

**M4. "1:30 panel ile 2:20 panel aynı nesne mi?"**
→ **AYNI GÖVDE, iki farklı yer.** Plan S11 (KÖŞE): *"S0'daki kemik-beyazı
köşe isim kazanır: kumdan çıkan bir panel kenarı ve altında gömülü gövde
hattı."* 1:30'daki panel **aracın kendi gövdesidir** ve o sahne filmin
TANIMA beat'idir; 2:20'de aynı gövdenin başka bir yeri kazılır. Açık
uç değil, kurulum→ödeme.

**M5. "0:13 sondaj çubuğu bırakıldı"**
→ Planda çubuk yalnız S1 propu; geri dönüş yok. Rapor da "kabul et"
demiş — kayıt için: bilinçli.

### 🧍 KARAKTER

**K1. "Mavi/mor bant kodlaması bible'da var mı?"**
→ **VAR ve zorunlu:** jeolog ICE-BLUE, mühendis DEEP-VIOLET; çift blokta
42 promptun hepsinde yazılı. 2:10'da mor bantların kaybolması **ihlal**,
şüphe değil.

**K2. "2:40'ta suitler temizlendi — off-screen temizlik planlı mıydı?"**
→ **HAYIR.** DUST STATE SCHEDULE monotoniktir (2→3→4, geri dönüş yok) ve
S14-S23 seviye 4'tür. Ayrıca her promptta **3 cm'lik temiz referans
şeridi** çapası var (tozun ölçüldüğü tek temiz yama). Sıfırlama ihlaldir.

**K3. Sırt çantası (pasaportta iki suitte de)**
→ **BIBLE İHLALİ — DERS 79'un 5. vakası.** 42/42 promptta *"Neither suit
has a back-mounted unit — no backpack, tank, hose or cable; both back
silhouettes are flat"* yazıyor. Cümle vardı, nesne yine çıktı.

**K4. Sol/sağ yer değiştirme (0:10 ↔ 0:20)**
→ **KİLİT YOK — açık.** SPATIAL LOCK dört sabit tanımlıyor (araç sağ
üçte bir · yürüyüş sola-sağa · kum sürüklenmesi sola-sağa · fırtına ve
güneş solda) ama **iki figürün hangisinin solda olduğunu** kilitlemiyor.
Bulgu geçerli, kaynağı promptun eksiği → **DERS 86**.

### 🔧 VIDEO

**V1. "0:10'da kadın astronot konuşuyor — bu sahnede replik bekleniyor muydu?"**
→ **REPLİK VAR, AMA KONUŞAN O DEĞİL.** Plan register tablosu:
`S1 | ÇOBAN | MACHINE | suit telsizi, gövdesiz | ağız kadrajda HAYIR`.
S1'in repliği gövdesiz sentetik sestir. Raporun onu "kadın astronot"a
ataması, **Cold Burn'deki ses mimarisi tersine dönmesinin (DERS 82)
ikinci vakası olabilir** — ama bunu ancak SES_QA doğrular ve o koşu
girdisiz kaldı. ⛔ **SES_QA yeniden koşulmadan bu satır kapanmaz.**

**V2. "2:00 aracın ölçeği plana uyuyor mu?"**
→ Plan: 11 m × 6 m × 3.2 m, alçak altıgen kesit, roket silueti YOK.
🔧 raporu "hard-surface geometry stable" demiş; ölçek kesri dizisi
(1/16 → 1/8 → 1/5 → 1/3) ekrandan doğrulanmadı — mod D koşusuna kaldı.

**V3. "3:20 dikey kalkış planlı mıydı?"**
→ **EVET.** S21 = `VİRAL #4 · DORUK — KALKIŞ`: dört köşe lülesi düz aşağı
ateşler, araç düz seviyede yükselir, 20 m'de bacaklar katlanır.

**V4. 4:00 — yanık başlık kartı "THE THIRD DUNE" 🔴 BLOCKER**
→ **GEÇERLİ ve KAYNAĞI BELLİ.** 42/42 promptta *"no readable text… no
subtitles, no title card, no watermark"* yazılı; metin sahne promptundan
gelemez. Kaynak **KAPAK dosyasının başlık katmanıdır** — kapak görseli
metinsiz üretilir, başlık post'ta bindirilir ve o çıktı kurgunun sonuna
eklenmiştir. Bu **DERS 70/72 zincirinin 4. vakası** (Unbroken City 2:40 ·
Wrong Shadow · Starless Circle 2:50 · burada 4:00).
→ Onarım: kurgudan son kartı çıkar. Yeniden üretim GEREKMEZ.

**V5. Raporun 2. prompt reçetesi: `REMOVE from video prompt: "title card,
cinematic poster"`**
→ **FABRİKASYON — UYGULANMAZ.** Depoda `cinematic poster` dizesi HİÇ
geçmiyor; `title card` yalnızca **yasağın içinde** geçiyor ("no subtitles,
no title card, no watermark"). Reçete uygulansaydı **çalışan yasak
silinecekti**. → **DERS 85.**

---

## 🧮 KURGU KAPISI — 11.08.2026 ölçümü

```
□ klip sayısı = plan SCENE COUNT   24 kesme → 25 klip = 25 ✅
□ süre = RUNTIME ±2 s              245 s ≠ 249 s → −4 s ⚠️ SINIRIN DIŞINDA
□ ekran metni 0.0 sn               4:00 yanık başlık kartı → ❌
□ CENTRAL CHOICE kurguda VAR       S17 (kasaların bırakılması) ekranda ✅
                                   — 📖 raporu 2:40-3:00'ı "The Cost" diye
                                     işaretledi, sahne yerinde
□ DORUK kurguda VAR                S21 kalkış ekranda ✅ (📖 "shareable
                                     moment" olarak işaretledi)

⭐ Cold Burn'ün aksine bu filmde SAHNELER KURGUDA — 4/4 ihlal yok, 2/5.
   −4 s'lik açığın en olası sebebi: Veo 3.1 native 8 s üretir, plan
   "8 s üret + 2 s extend" diyor; iki klipte extend uygulanmamışsa
   fark tam 4 saniyedir. Operatör klip sürelerini tek tek ölçerse
   hangi iki klip olduğu bir dakikada bulunur.
```

---

## 📚 BU KOŞUDAN ÇIKAN DERSLER

| Ders | Başlık | Kaynak bulgu |
|---|---|---|
| **84** 🔴 | Sahneler arası durum metinle kilitlenmiyor | toz + bant + sırt, üçü de yazılıydı, üçü de kırıldı |
| **85** 🔴 | Mod V reçetesi görmediği promptu alıntılıyor | `REMOVE "title card, cinematic poster"` |
| **86** 🟡 | İki kişilik kadrajda dizilim kilidi yok | 0:10 ↔ 0:20 sol/sağ takası |
| **87** 🔴 | Mod V, filmin önermesini çelişki saydı | araç düz kum → gömülü; çanak |

**Tekrar eden dersler (yeni değil, ama sayaç ilerledi):**
`D79 ×5` sırt ünitesi (ilk kez cümle VARKEN) · `D70/72 ×4` kapak
başlığının kurguya sızması · `D78` bedel nesnesi (11 kasa) ekranda —
bu kez TUTTU, 📖 raporu finali "kasalar kumda" olarak okudu ·
`D82` ses mimarisi şüphesi (doğrulanmadı, SES_QA bekliyor) ·
Kaleida Crash tuzağı: viral ara sahne kesme listesine girdi.

---

## 📋 ONARIM LİSTESİ

```
ÜCRETSİZ / KURGU
 □ 4:00 yanık başlık kartını kurgudan çıkar          🔴 BLOCKER kalkar
 □ klip sürelerini ölç, extend uygulanmamış 2 klibi bul (−4 s)
 □ 📖 raporunun kesme listesini UYGULAMA — iki öneri de viral sahne

YENİDEN ÜRETİM (sırayla, en ucuzdan)
 □ 2:10  mor bantsız klip                → bant rengi çapası
 □ 2:40 + 2:50  temizlenmiş suit klipleri → toz seviyesi 4
 □ 1:50  eldiven-kum kaynaşması           → S10, kontak sınırı cümlesi
          promptta VARDI (iki blokta da) — I2V başlangıç karesiyle dene
 □ 2:51  anahtar-bacak kaynaşması         → aynı sınıf
 □ 3:30  derin krater → sığ süpürme çanağı (S22 metni zaten doğru)

KOŞULMAMIŞ ÖLÇÜM
 □ 🔊 SES_QA — 245 s kurgu ile yeniden koş. Register tablosu planda
   hazır; V1 sorusu (S1 repliği kimin ağzından çıkıyor) buna bağlı.
 □ Bir sonraki turda 🔧 ve 📖 mod D koş — SPEC bloğu planın 856. satırında.
```
