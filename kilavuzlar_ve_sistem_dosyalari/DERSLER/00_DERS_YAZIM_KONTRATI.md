# 📜 DERS YAZIM KONTRATI — kapısı olmayan ders, ders değildir

> **01.09.2026 · D161/D162 koşusundan.** Sayılar buraya yazılmaz:
> `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` → **🧭 DERS → KAPI** bloğu.
> Bu dosya eski dersleri değiştirmez; bugünden sonra yazılan her dersi bağlar.

## 1. Neden

Ders bir metindir; modeli (ve ajanı) yalnız **kapı** durdurur. Ölçüm
(01.09.2026): derslerin çoğu hiçbir plan/prompt/QA kapısında adı geçmiyordu,
kapısı olanların etkisi hiç ölçülmemişti (mod D koşusu sıfır), yazıldıktan
sonra dokuz kez tekrarlayan ders vardı ve sıfır ders emekli edilmişti. Bir
ders sabah yazılıp **aynı gün** yazılan filme ulaşmadı (D157 → THE COLD WELD).
`AGENTS §8` bunu çoktan söylüyordu: *kaliteyi yükselten üç olayın üçü de
karar değişikliğiydi, kural değil.*

## 2. Dört kader — her dersin başlığının altında TEK satır

```
**KAPI:** BETİK · <betik> <denetim adı>       makine koşar: prompt_kontrol.py ·
                                              rapor_kontrol.py · olcum_kapisi.sh ·
                                              rubrik_paketle.sh
**KAPI:** LİSTE · <03_PLAN_ONCESI maddesi / 02_RISK kartı>
                                              insan koşar, plan anında, maliyeti sıfır
**KAPI:** KARAR · <ne değişti: mimari / araç / skill akışı / varsayılan>
**KAPI:** ARŞİV · <neden kapıya inmedi>       hikâye olarak kalır; okuma listesinde değil
```

Beşinci kader yok. **"Prompt cümlesi" bir kader değildir:** ya BETİK o cümlenin
varlığını ölçer, ya ders ARŞİV'dir. (Kanıt: `01_DERS_ETKINLIK_RAPORU` §4 —
tarif kilidi %0, sayısal kilit %100 tuttu.)

## 3. TEKRAR satırı ve emeklilik

```
**TEKRAR:** <sayı> · son vaka <tarih> (<film>)
```

Vaka görüldükçe sayı artar. **≥ 3 →** satıra `⛔ ÇALIŞMIYOR` eklenir ve bir
sonraki koşuda **dönüştürme borcu** doğar: cümleden karara ya da araca. Borç
ödenince satır `→ araca çevrildi: …` alır. Emekli ders silinmez; okuma
listesinden çıkar (ARŞİV kaderi).

## 4. Dosyalama (kart G'nin sıfırıncı adımı)

- KAPI satırı boş aday `DERSLER/`'e **giremez** → `GOZLEM_DEFTERI.md`'ye
  `ADAY-n` olarak düşer, numara almaz. Kapı bulununca ders olur.
- Mod V partiden ya da ⬜ AÇIK defterden **film-dersi yazılmaz** (kural
  korunur) — ama aday KAYBOLMAZ, deftere düşer. Sistem aksi hâlde film
  bilgisini yapısal olarak alet bilgisine çevirir (01.09.2026 kaydı).
- Alet dersi (08/09) ile film dersi (01-07) **aynı okuma listesinde durmaz**:
  `yeni-film` 01-07'yi, `qa-isle` 08-09'u okur. Dosyalar taşınmaz; liste ayrılır.

## 5. Geriye dönük — bilinçli olarak YAPILMAZ

Eski dersler tek seferde tasnif edilmez (bir hafta prose üretir). Bir ders
**tekrarladığında** ya da bir film ona **dokunduğunda** KAPI satırı alır.
Bugün satır alanlar: `sayac.sh` 🧭 bloğu.

## 6. Şablon

```
## 🔴 DERS ___: BAŞLIK — TEK CÜMLEDE NE OLDU

**KAPI:** BETİK/LİSTE/KARAR/ARŞİV · <nerede>
**TEKRAR:** 0

**Kaynak:** <film> QA (<tarih>) — <mercek>: <skor> — `<timecode> — <bulgu>`
**Sorun:** <ne bozuldu, kaç filmde>
**ÇÖZÜM:** <karar / araç / liste maddesi>   ← prompt cümlesi ancak betik ölçüyorsa
```

> ⚠️ Şablondaki `DERS ___` bilerek rakamsız: `sayac.sh` ders sayısını
> `## … DERS <rakam>` başlıklarından sayar; bu dosya sayıma girmemelidir.
