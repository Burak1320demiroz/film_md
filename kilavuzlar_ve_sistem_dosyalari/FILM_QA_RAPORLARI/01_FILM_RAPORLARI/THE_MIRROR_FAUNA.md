# 🦎 THE MIRROR FAUNA — FİLM KAYDI

> **Durum:** film üretildi ve birleştirildi · **master ölçüm durumu bilinmiyor** ⚠️ · **kurgu gerekiyor**
> **Koşu:** 09.09.2026 · **sekiz mercek** (① KARE · ② DEVAMLILIK · ③ SES · ⑥ FİZİK ·
> ⑦ AKSİYON · ⑧ EFOR · ⑪ IŞIK · ⑫ HOOK) — **sekizi de mod D.**
>
> ⛔ **T TABLOLARI: rapor_kontrol.py kapısı koşulmadı.** Skorlar bu kayıtta belgelenir;
> T1/T2/T3/T6/T7/T8/T11/T12 tablolarına satır ancak `rapor_kontrol.py GO` sonrası yazılır [D161/D162].
>
> **⑪ ölçüm kapısı (olcum_kapisi.sh):** koşu kaydı yok — master doğrulaması sahip tarafından yapılmalı.

---

## 📦 MALZEME

```
MASTER:    THE_MIRROR_FAUNA (yatay_2_dk_filmler/)
ÖLÇÜLEN:   ~164 s · 16:9 YATAY · COMPILATION
KART:      02:39-02:44 (5 s başlık kartı)
GÖVDE:     02:39 = 16 klip × ~10 s
PLAN:      15 sahne · 149 s (QA_SPEC: CLIP COUNT 15)
           ⚠️ SAHNE TUTARSIZLIĞI: SPEC 15 sahne, raporlar 15-16 saydı
           Sebep: S12=S13 kopya sahne (aynı klibin iki kez yerleştirilmesi)
SPEC:      THE_MIRROR_FAUNA_QA_SPEC.md ✅ VAR · MOD D koşuldu
```

---

## §⑪ ÖLÇÜM KAPISI

```
⚠️ olcum_kapisi.sh koşusu: KAYIT YOK
⚠️ Sahip tarafından master doğrulanmadan T tablolarına satır yazılamaz.
Raporlardaki "~164 s" ve "02:44 measured" uyuşuyor — kabul.
```

---

## 📊 SKOR ÖZETİ (mod D)

| Mercek | Skor | Kategoriler | Verdict |
|---|:--:|:--:|---|
| ① KARE | **6.4** | 8 | REGENERATE |
| ② DEVAMLILIK | **7.7** | 11 | STRUCTURAL PROBLEM |
| ③ SES | **7.2** | 7 | AUDIBLE DRIFT, FIXABLE IN THE MIX |
| ⑥ FİZİK | **5.4** | 5 | TWO GRAVITIES |
| ⑦ AKSİYON | **7.2** | 9 | FIXABLE IN EDIT |
| ⑧ EFOR | **2.0** | 6 | NOBODY PAYS |
| ⑪ IŞIK | **7.5** | 8 | LIT FROM NOWHERE |
| ⑫ HOOK | **7.3** | 8 | LEAVES AT 02:00 |

---

## 🔴 BLOCKER LİSTESİ (kırmızı — kurgu/üretim önce bunlar)

| Timecode | Kaynak | Bulgu |
|---|---|---|
| 01:52 | ① ⑪ | Vizör HUD içinde kırmızı alfanümerik metin + veri dizisi → **REGENERATE S12/S13** |
| 02:00 | ①②⑦⑫ | S13, S12'nin birebir kopyası → **EDIT: S13'ü kes** |
| 01:50 | ⑥⑧ | Düşüş 1,2 s'de 1 m → 0.14g, kilit 0.7g → **REGENERATE veya post hız rampa** |

---

## 🟠 MAJOR BULGULAR

| Timecode | Kaynak | Bulgu |
|---|---|---|
| 01:11 | ① | Sol el parmaklarının parlak cihazla kaynaşması — el geometri çöküşü |
| 01:12 | ①⑥ | Lazer kıvılcımları donuyor, 0g davranışı — REGENERATE |
| 01:20 | ①⑪ | Tentacle sarı bloom, doku kaybı — REGENERATE |
| 02:12 | ① | Parmaklar üç kalın dijitte kaynıyor — REGENERATE |
| 01:10 | ⑦ | Silah hedefe değil ekran sağına atıyor — aksiyon okunmuyor |
| 01:50 | ⑦ | Astronotu kim/ne düşürdü belirsiz — tehdit yönü yok |
| 00:50-01:10 | ② | Orange Astro aleti üç kesme boyunca değiştiriyor |
| 01:20-01:30 | ② | Tentacle rengi sarıdan cyan'a dönüyor |
| 01:03 | ③ | "Come front to you take" — halüsine replik, değiştirilmeli |
| 01:40 | ⑪ | Sağ anahtar ışıktan tam silüete ani geçiş, sınır yok |
| 02:10 | ⑪ | Kırmızı vizör ışığı S14'te de sürüyor |

---

## 🟡 MINOR BULGULAR

| Timecode | Kaynak | Bulgu |
|---|---|---|
| 00:00 | ①⑥ | Kaya dokusu altında "nefes alıyor" / astronotlar yüzüyor |
| 00:20 | ① | Alien ön sağ bacağı yüzeyde kayıyor |
| 01:00 | ① | Arka plandaki kaya oluşumları morph ediyor |
| 01:12 | ⑥ | Kıvılcıklar kütlesiz CGI davranışı |
| 02:10 | ⑥ | Kask dumanı dağılmıyor |
| 02:20 | ② | Vizör altın'a geri döndü, duman yok (WEAR REVERT) |
| 02:20 | ⑪ | Renk ısısı geçişi |
| 01:03 | ③ | Ambiyans 0:29 ve 0:59'da hafif düşüyor |
| 01:12 | ③ | Lazer SFX 1 kare gecikiyor |
| 00:00 | ③⑧ | Wall-to-wall müzik dinamik aralığı siliyor |

---

## 🚫 NEGATİF KURAL İHLALLERİ (① Kare mercek)

- [x] AI bloom / soft glow / dreamy haze on light sources
- [x] Characters belonging to the scene's own materials
- [x] Face morphing
- [x] Creature sliding (locomotion without leg articulation)
- [x] Melting or morphing terrain/geology
- [x] Frozen or static particles
- [x] Hand geometry breakdown near glowing surfaces

**NEGATİF KUTU SAYISI: 7 · BAĞLANTILI BULGU: 7 · BAĞLANTILANMAYAN: 0**

---

## 📐 FİZİK KİLİT TABLOSU (⑥ mercek · MOD D)

| Kilit | Plan | Ekranda | Δ | Sonuç |
|---|---|---|---|---|
| YERÇEKİMİ | 0.7g (6.86 m/s²) | ~0.14g (1.38 m/s²) @ 01:50 | 0.56g | **FAIL** |
| Yürüyüş kadansı | 0.7g uyumlu | 00:00 ve 02:30 uyumlu | — | PASS |

---

## 🎬 DEVAMLILILIK (② mercek) — ANA BULGULAR

```
KARAKTER PASOPORTİ
  Mavi Astro    : Beyaz tulum, mavi şerit — kararlı ✅
  Turuncu Astro : Beyaz tulum, turuncu şerit — vizör ALTIN → KIRMIZI → ALTIN ⚠️
  Canlı (Fauna) : Mor deri, 4-6 cyan tentacle — tentacle 01:20'de sarı ⚠️

KOPYA SAHNE:   S12 = S13 (02:00) — nedensellik 5/10
EKİPMAN MORPH: Orange Astro 00:50→01:10 (gri kutu → sarı fener → ışın silahı)
WEAR REVERT:   02:10'da duman → 02:20'de temiz takım (UNEARNED RESET)
```

---

## 🎯 AKSİYON (⑦ mercek) — BEAT STRING

```
BEAT STRING: ----A---pAp-p---
B1 (00:40): Vance eli uzatıyor → okunur ✅
B2 (01:10): Orange silah atıyor → PARTIAL (hedef çerçevede değil) ⚠️
B3 (01:30): Vance canlıya dokunuyor → okunur ✅ (SPEC merkezi seçimi)
B4 (01:50): Orange geriye fırlatılıyor → PARTIAL (güç kaynağı belirsiz) ⚠️
```

---

## 💪 EFOR (⑧ mercek) — COST CURVE

```
COST CURVE: 1111111111144111
RESET LOG:  S13→S14 arası — 4'ten 1'e UNEARNED düşüş (toparlanma gösterilmedi)

ÖDENMEDEN GEÇEN İŞ
  E1 (00:00): Ağır tulum ile yürüme — strain YOK
  E2 (00:50): Baskılı eldivenle kadranı çevirme — strain YOK
  E3 (01:10): Ağır enerji silahı atışı — recoil YOK
  E4 (01:50): Enerji darbesiyle geriye fırlatılma — rigid düşüş, sonrasında sıfır yara izi
```

---

## 🔊 SES (③ mercek) — TEMEL BULGULAR

```
AUDIO STATE:    A · KONUŞULAN SATIR: 1 (01:03 "Come front to you take")
MİKS:           Wall-to-wall müzik, dialogue ile aynı seviyede
SES KİMLİĞİ:   VOICE A (Astronot) — kim olduğu belirsiz, önerilen: birebir yeniden üretin
```

---

## 💡 IŞIK (⑪ mercek) — ZONE REGISTER

```
ZONE: TRAPPIST-1e Surface (S1-S15) · tek bölge
KEY DIRECTION STRING: 3333333333-3333
IŞIK SIÇRAMASI: 4 kesme (1:40 · 1:50 · 2:10 · 2:20)
BLOCKER: 01:50 vizör içi kırmızı strobe — beklenmiyordu, beklemeyenin kökeninde yok
```

---

## 🪝 HOOK (⑫ mercek) — DROP-OFF TAHMİNİ

```
AÇILIŞ SORUSU: "Yerde yansıyan ışıklı gölge nedir?" → güçlü ✅
DROP-OFF:
  1. 02:00 — kopya sahne (S13), izleyici illüzyonu kopar
  2. 01:10 — ekrana karşı vuruş okunmuyor
  3. 02:39 — başlık kartına kesildi, döngü yok
```

---

## 🛠️ KURGU ÖNCESİ ÖNCELIK SIRASI

```
1. S13'ü kes (kopya sahne — ① ② ⑦ ⑫ ortak bulgu)
2. S12/S13 vizör HUD → REGENERATE (① ⑪ BLOCKER)
3. 01:50 düşüş → hız rampa ile düzelt VEYA REGENERATE (⑥ BLOCKER)
4. Son başlık kartını kes veya sola çek (⑫ loop)
5. 01:03 repliği değiştir (③ MAJOR)
```

---

## 📚 MEVCUT DERSLERLE EŞLEŞME (tekrar sayacı için)

| Bulgu | Ders | Etki |
|---|---|---|
| AI bloom (tentacle, fener) | D3 + D41 | TEKRAR +1 |
| Arazi morph | D6 | TEKRAR +1 |
| Donmuş kıvılcıklar | D10 + D39 | TEKRAR +1 |
| Canlı kayma | D18 | TEKRAR +1 |
| El geometri çöküşü | D43 | TEKRAR +1 |
| Ekipman morph kesme arası | D37 + D57 + D58 | TEKRAR +1 |
| Yerçekimi uyumsuzluğu | D127 | TEKRAR +1 |
| Vizör HUD metin | D34 ailesi / NO AI TEXT | — |

---

## ⬜ AÇIK SORULAR (belge cevabı bekliyen)

| Gözlem | Soru |
|---|---|
| Tentacle 01:20'de sarı, 01:30'da cyan | Geçici tepki mi yoksa hata mı? |
| Orange alet üç kesme boyunca değişiyor | Tek çok-biçimli alet mi yoksa hata mı? |
| Orange 01:50'de düşüyor | Silah geri tepme mi yoksa alien saldırısı mı? |
| S11'de zemin damarları | Ridge'e özgü mi yoksa süreklilik hatası mı? |
| 01:03 repliği kimin ağzından? | Hangi astronot konuşuyor? |
| 01:03 repliğin doğru metni ne? | Senaryodaki orijinal satır? |

---

## 🗂️ HAM RAPORLAR

```
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_KARE_HAM.md         ① Kare
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_DEVAMLILIK_HAM.md   ② Devamlılık
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_SES_HAM.md          ③ Ses
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_FIZIK_HAM.md        ⑥ Fizik
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_AKSIYON_HAM.md      ⑦ Aksiyon
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_EFOR_HAM.md         ⑧ Efor
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_ISIK_HAM.md        ⑪ Işık
02_HAM_RAPORLAR/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_HOOK_HAM.md        ⑫ Hook
```
