# 🌗 THE WRONG SHADOW — Film QA Kaydı

> Oluşturma: 06.08.2026 · iki mercek aynı gün, ikisi de MOD V (belgesiz)
> koşuldu; belge cevapları aşağıda bu kayda işlendi.
> Kaynak dosya: `dikey_shorts_filmler/THE_WRONG_SHADOW/THE_WRONG_SHADOW_DIKEY_SHORTS.md`

---

## 🎯 MERCEK DURUMU

| Mercek | Durum | Skor | Ham rapor |
|---|---|---|---|
| 📱 SHORTS_QA | ✅ Ⓥ mod V | **5.6/10** · **REGENERATE** (3 BLOCKER) | `02_HAM_RAPORLAR/THE_WRONG_SHADOW_SHORTS_HAM.md` |
| 📖 SENARYO_QA | ⚠️ Ⓥ mod V ŞARTLI | **3.0/10** · REVISE STRUCTURE | `..._SENARYO_HAM.md` |
| 🎨 KAPAK_QA | ❌ | — | — |

```
KÜNYE (plan)    6 sahne × 8 s = 48 s · 0 kesme · sessiz · günümüz platosu ·
                novum: kaynaksız İKİNCİ GÖLGE SETİ (1,5°/sn döner, S4'te
                hizalanır) · jalonlar 6/6 sahnede sabit · metin 0,0 sn
KURGU (ölçülen) 64 s · 7 segment (~10 s'lik sahneler + jenerik kartı) ·
                ÇİFT GÖLGE HİÇBİR KAREDE YOK · dönme hareketi S5'te
                JALONLARA transfer olmuş (havada dönen jalonlar) ·
                sonda "THE DEVIL'S DOUBLE" başlık kartı (yanlış isim!)
DERS 65 NOTU    iki rapor da FILM: (not supplied) yazdı — kural tuttu ✅
DERS 72 NOTU    ⛔ KURGU KAPISI KOŞULMADAN iki mercek çalıştırıldı —
                skorlar kapı-ihlalli teslime aittir (aynı gün, beşinci
                ve altıncı tekrar değil: DERS 74'ün kaynağı)
```

---

## ⛔ TEK CÜMLELİK HÜKÜM

**Filmin var olma sebebi ekrana hiç girmedi.** İki bağımsız mercek de
64 saniyelik kurguda tek bir çift gölge görmedi; "kaynağı olmayan gölge"
novum'u ya hiç üretilmedi ya da üretimde kayboldu — modelin gölgeye
verdiği dönme hareketi, S5'te fiziksel nesnenin kendisine (jalonlara)
sıçradı. Bu, dosyanın kendi risk kaydının ("kaynaksız ikinci set ya
kaybolur ya çoğalır ya da gökyüzüne kaynak uydurulur") öngörmediği
DÖRDÜNCÜ başarısızlık modu: **imkansız özellik türetilmiş fenomenden
birincil nesneye transfer olur.** → **DERS 73**.

---

## 🔎 FLAGS FOR DOCUMENT CHECK — CEVAPLAR (plan dosyasından)

> Mod V raporları soru sordu; cevaplar plan/bible'dan verildi. Bu bölüm
> kart C/D adım 2'dir ve koşunun en değerli çıktısıdır.

### 📱 SHORTS_QA soruları

**1. "Kurgu 64 s, ~10 s'lik sahneler + jenerik kartı — belge 10 s'lik
sahne mi yazıyor, kurgu hatası mı?"**
KURGU + ÜRETİM HATASI. Plan her sahneyi **tam 8 saniye** yazar ("SABİT
KLİP SÜRESİ: her video promptu tam 8 saniye"), toplam 48 s; Kural 10
ekran metnini 0,0 saniyeye kilitler ve kapağın videoya girmeyeceğini
açıkça söyler. → **DERS 70'in İKİNCİ vakası** (ilki The First Morning,
aynı gün). Kurgu kapısı (klip sayısı · süre · metin) yine koşulmamış.

**2. "S5'te jalonlar havada yatay dönüyor — ilan edilen NOVUM bu mu,
fizik hatası mı?"**
FİZİK HATASI — hem de novum'un tam tersi. Plan: "Jalonlar devrilmez,
eğilmez, ele alınmez… zeminde DİKİLİ durur" (Negative Bible + Jalon
Kilidi). Dönen şey GÖLGE SETİ olacaktı (1,5°/sn, zeminde düz). Model
dönme talimatını gölgeden alıp nesneye vermiş. → **DERS 73'ün kaynağı.**

**3. "Jenerik kartı dağıtım için BİLİNÇLİ SAPMA mı?"**
HAYIR. Kural 10: "Kapak ayrı üretilir ve videoya girmez; başlık
platformda yazılır." Üstelik karttaki isim ("THE DEVIL'S DOUBLE") filmin
adı bile değil — model kendi başlığını uydurup yakmış. 🔴 BLOCKER doğru.

**4. (Rapor sormadı, belge düzeltiyor) "Hook 5/10 — jalonlar 0:00'da
görünüyor, merak boşluğu yok."**
Jalonlar reveal nesnesi DEĞİL — reveal ÇATALLI GÖLGE idi ve hiç
üretilmediği için hook'un reveal'i fiilen YOKTU. Bulgunun kökü hook
zamanlaması değil, novum yokluğudur. Ayrıca S0 planı çatalı 2. saniyede
"dolly yaklaşınca" okutuyordu — mesafe/yaklaşma ANALOG perdedir,
DERS 71'in ikili kilit kuralına aykırı (görsel promptta çatal zaten
0. karede kadrajdaydı).

**5. (Rapor sormadı) "S1 çömelme alt banda değiyor."**
Çömelme PLANLI (S1 görsel promptu) ve "No part of the figure falls into
the bottom quarter" satırı 6/6 promptta vardı — satır ÜRETİMDE tutmamış.
Kompozisyon kilidi yüzde bandıyla yazılmıştı; ihlal prompt eksikliği
değil, model sapması. 🟠 doğru, prompt önerisi gereksiz.

### 📖 SENARYO_QA soruları

**1. "Plan bir doruk ilan ediyor mu; 0:50'deki sahne mi?"**
Plan doruğu **S4 HİZALANMA** (iki gölge setinin 0°'de üst üste binişi —
"filmin en pahalı karesi"). 0:50'de görülen "havada dönen jalonlar" plan
doruğu değil, üretim hatası. Doruk kurguya hiç girmemiş → Ders 62
sınıfı; senaryo merceğinin "unearned climax" bulgusu kök nedenin
dilbilgisidir.

**2. "64 s / 7 sahne planlı mı, montaj hatası mı?"**
Montaj + üretim hatası (yukarıda SHORTS_QA cevap 1). 34 s'lik kesim
önerisi bu yüzden geçersiz — doğru çözüm kesmek değil, 6×8=48'i
yeniden üretmek.

**3. "Plan karaktere merkezi seçim / 'want' veriyor mu? Ekranda yok."**
EVET, VERİYOR. Plan §Mekaniğin insani karşılığı: harita mühendisi;
bütün aletleri doğru çalışıyor ve hiçbiri işe yaramıyor. **CENTRAL
CHOICE = S3:** ölçmeyi bırakır, kendi soluk gölgesinin ortasında durur
ve dönüşünü izler — insan, kendi güneş saatinin mili olur. Çift gölge
render edilmediği için bu jest ekranda "adam ayakta duruyor"a düştü →
"camera-carrier" bulgusunun kökü karakter yazımı değil, novum yokluğu.
**"Dead scene" verdikleri S3-S5, planda filmin en yüklü sahneleri.**

---

## 📊 SKOR ÖZETİ

### 📱 SHORTS_QA (Ⓥ mod V · 16 kategoriden 13 puanlı · 73.0÷13=5.6 ✅)

| Kategori | Skor | | Kategori | Skor |
|---|:--:|---|---|:--:|
| Character | 6 | | Vertical Format | **9** |
| Scale & Physics | **4** | | Safe Zone | 7 |
| Camera | 5 | | Hook Timing | 5 |
| Lighting | 6 | | Negatif ihlal | **4 adet** |
| Environment | 5 | | Cross-Scene | 6 |
| Particles | 8 | | Story & Transmission | **3** |
| Creatures / Dialogue | N/A | | Retention | **3** · Music 6 |

🔴 BLOCKER ×3: jenerik kartı (0:59) · 64 s / 7 segment · S0 içi gizli kesme

### 📖 SENARYO_QA (Ⓥ ŞARTLI · 27÷9=3.0)

Kanca 5 · Önerme 3 · Yapı 3 · Karakter 2 · Tema 2 · Diyalog N/A ·
Duygu Yayı 2 · Final 3 · Özgünlük 4 · Tutundurma 3 → **3.0/10**
— serinin en düşük hikaye skoru; ama bkz. DERS 72 notu: mercek kurgu
hatasını içerik zaafı olarak ölçtü, plan dosyası bulguların çoğunu
kök nedene (novum yokluğu) indiriyor.

---

## 🧭 YENİDEN ÜRETİM ŞARTLARI (REGENERATE)

```
① TEK KARE FİZİBİLİTE KAPISI [DERS 73]: 6 sahne yeniden üretilmeden
   önce S0 GÖRSEL promptu tek başına koşulur. Çıkan karede nesne
   başına TAM İKİ gölge + kesişim-en-koyu fiziği okunmuyorsa video
   üretimine HİÇ geçilmez — konsept ya I2V start-frame kilidiyle ya
   da novum taşıyıcısı değiştirilerek revize edilir.
② S4-ÖNCE KURALI KAYITLA: plan zaten "üretim S4'ten başlar" diyordu;
   bu koşuda ya atlandı ya sonucu yok sayıldı. Kapı sonucu tarih +
   GEÇTİ/BATTI olarak film dosyasına yazılmadan sonraki sahne
   üretilmez [DERS 74].
③ KURGU KAPISI [DERS 70/72]: 6 klip · 48.0±0.5 s · ekran metni 0,0 sn
   (jenerik dahil) doğrulanmadan hiçbir QA merceği çalıştırılmaz.
④ Sahne süresi üretim aracında 8 s'e kilitlenir — 10 s'lik çıktı
   kabul edilmez (bu koşuda 6×10+4=64 s'in kaynağı).
```
