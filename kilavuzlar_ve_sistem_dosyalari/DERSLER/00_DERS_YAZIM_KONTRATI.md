# 📜 DERS YAZIM KONTRATI — kapısı olmayan ders, ders değildir

> **01.09.2026 · D161/D162 koşusundan.** Sayılar buraya yazılmaz:
> `bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` → **🧭 DERS → KAPI** bloğu.
> Bu dosya eski dersleri değiştirmez; bugünden sonra yazılan her dersi bağlar.

> ⭐ **14.09.2026 · REFORM (sahip kararı, `TODO_AKIS_VE_DERS_REFORMU.md`).** Ölçüm:
> 205 dersin 90'ı alet dersi (08/09), son 25 dersin 16'sı QA makinesi hakkında,
> **93 film gözlemi ADAY olarak kapısız bekliyordu** — §4'ün kendi uyarısı ("sistem
> film bilgisini yapısal olarak alet bilgisine çevirir") aynen gerçekleşti. Bugünden
> itibaren FİLM dersi (01-07) için tanım değişti: **ders = ≥ 2 filmde görülen ÖRÜNTÜ +
> bir sonraki filmde değişen TEK SATIR** (§2b). "Kapısı olmayan ders yok" kuralı alet
> dersi için sürer; film dersi için LİSTE kapısı yeter. "Mod V'den film dersi yazılmaz"
> kuralı geri alındı: mod V bulgusu ADAY olur, ≥ 2 filmde tekrarlayınca ders olur (§4).
> Yaşayan film dersi tavanı 40 (`00_YASAYAN_DERSLER.md` · §3).

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
                                              rapor_kontrol.py · olcum_kapisi.sh
**KAPI:** LİSTE · <03_PLAN_ONCESI maddesi / 02_RISK kartı>
                                              insan koşar, plan anında, maliyeti sıfır
**KAPI:** KARAR · <ne değişti: mimari / araç / skill akışı / varsayılan>
**KAPI:** ARŞİV · <neden kapıya inmedi>       hikâye olarak kalır; okuma listesinde değil
```

⭐ **ÖLÇEN MERCEK SATIRI [11.09.2026]:** dersi bir QA merceği doğurduysa KAPI
satırı o merceği ADIYLA taşır — örn. `· ölçen mercek: ⑬ UYUM`. Gerekçe D187:
bir kilidin ölçen merceği yoksa kilit yazılı olsa bile hiç koşmaz; tersi de
doğrudur — dersi kimin ölçtüğü yazılmazsa ders bir daha sınanamaz.
⛔ ⑬ UYUM'dan doğan derslerde bu satır ZORUNLUDUR: o merceğin bütün 🅑 bulguları
tanım gereği SONRAKİ filmin kilidine dönüşür, ve kilidin kaynağı yazılmazsa
sonraki film onu "genel tavsiye" sanır.

Beşinci kader yok. **"Prompt cümlesi" bir kader değildir:** ya BETİK o cümlenin
varlığını ölçer, ya ders ARŞİV'dir. (Kanıt: `01_DERS_ETKINLIK_RAPORU` §4 —
tarif kilidi %0, sayısal kilit %100 tuttu.)

## 2b. FİLM DERSİ ŞABLONU — 14.09.2026'dan sonra yazılan her 01-07 dersi

Başlığın **hemen altında**, Kaynak'tan ÖNCE, dört satır (D192 kalıbı; Kart G'nin
"Sorun'dan sonra" geleneği kaldırıldı — tek gelenek):

```
**FREKANS:** <n> film · <FILM> (mod D/V · mercek) · <FILM> (…) · …
**DEĞİŞEN SATIR:** <PLAN sütunu | prompt satırı | 03_PLAN_ONCESI maddesi | SPEC satırı> — TEK satır
**KAPI:** BETİK · … | LİSTE · … | KARAR · …
**TEKRAR:** 0
```

- **FREKANS ≥ 2 farklı film** — tek vaka ders DEĞİLDİR, `GOZLEM_DEFTERI` ADAY'ıdır.
  Filmlerin yanına koşu modu yazılır; ⑨-⑫ mod V'den gelen vaka "plan uydurma"
  riskini taşır [D190], o yüzden mod görünür kalır — ders yazılmasına engel değildir.
- **DEĞİŞEN SATIR** dersin kapısı değil, dersin *yeri*dir: bir sonraki filmde PLAN'ın
  hangi sütunu, promptun hangi satırı, listenin hangi maddesi bu yüzden farklı yazılır.
  Tek satır. "Dikkat edilir" bir satır değildir. Boşsa ders yazılmamıştır.
- **KAPI** film dersi için **LİSTE yeterlidir** (`03_PLAN_ONCESI` maddesi ·
  `02_RISK_KARTLARI` kartı · `00_SAHNE_TABLOSU` sütunu). BETİK varsa yazılır, şart değil.
- Alet dersi (08/09) §2'nin eski şablonunda kalır (KAPI + TEKRAR).
- Yeni ders `00_YASAYAN_DERSLER.md`'ye girer; liste 40'ı aşıyorsa biri çıkar (§3).

## 3. TEKRAR satırı ve emeklilik

```
**TEKRAR:** <sayı> · son vaka <tarih> (<film>)
```

Vaka görüldükçe sayı artar. **≥ 3 →** satıra `⛔ ÇALIŞMIYOR` eklenir ve bir
sonraki koşuda **dönüştürme borcu** doğar: cümleden karara ya da araca. Borç
ödenince satır `→ araca çevrildi: …` alır. Emekli ders silinmez; okuma
listesinden çıkar (ARŞİV kaderi).

**14.09.2026 — emekliliğin adresi:** film dersinin okuma listesi
`DERSLER/00_YASAYAN_DERSLER.md`'dir (≤ 40 satır; sayı `sayac.sh` 🧭). Yeni film dersi
listeye girince liste taşıyorsa biri çıkar; çıkan dersin dosyadaki metni durur, yalnız
listeden düşer. Giriş/çıkış o dosyanın defterine tarih ve gerekçeyle yazılır. Listede
olmayan ders yeni filmin okuma çizelgesine girmez (`okuma_cizelgesi.sh` TUR 1).
Bir ders `⛔ ÇALIŞMIYOR` damgası alınca listeden ÇIKMAZ — tersine öne gelir: borcu
ödenene kadar görünür kalır.

## 4. Dosyalama (kart G'nin sıfırıncı adımı)

- KAPI satırı boş aday `DERSLER/`'e **giremez** → `GOZLEM_DEFTERI.md`'ye
  `ADAY-n` olarak düşer, numara almaz. Kapı bulununca ders olur.
- ~~Mod V partiden ya da ⬜ AÇIK defterden film-dersi yazılmaz~~ — **14.09.2026'da
  GERİ ALINDI.** Bu kural 13 günde 93 adayı deftere hapsetti ve sıfır film dersi
  üretti; sistem tam da bu maddenin uyardığı şeyi yaptı (film bilgisi → alet bilgisi).
  Yeni kural: **mod V bulgusu ADAY olur** (`**MOD:** V · ⑨-⑫ ise "plan uydurma riski"`
  etiketiyle); aday **≥ 2 farklı filmde** tekrarlayınca koşu modundan bağımsız ders olur
  (§2b FREKANS satırı modu taşır). Tek istisna: **UNATTRIBUTED** rapor (`qa-isle` ③
  kimlik kapısı, eşleşme < 2) — film kimliği belirsizdir, ne ders ne aday yazılır.
- Her QA koşusunun film kaydı `## 🔁 DERS DÖNÜŞÜ` bölümüyle biter: hangi ESKİ ders
  tekrar etti (TEKRAR sayacı +1) ve TEK yeni aday (ya da "yok — gerekçe"). Koşu
  12 rapor üretip bu iki satırı üretmiyorsa kayıt zinciri tamamlanmamıştır
  (`qa-isle` §7 · AGENTS ①.12).
- Alet dersi (08/09) ile film dersi (01-07) **aynı okuma listesinde durmaz**:
  `yeni-film` `00_YASAYAN_DERSLER.md`'yi (≤ 40), `qa-isle` 08-09'u okur. Dosyalar
  taşınmaz; liste ayrılır. `sayac.sh` 📚 ikisini ayrı sayar.
- Aday defterindeki örüntüler filmler arası **frekansla** okunur:
  `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/ders_frekans.py --ozet`
  (VERDICT ve düşük kategori × farklı film sayısı; sayaç 🔁 bloğu). Ders, tek koşunun
  değil bu tablonun tepesinden yazılır.

## 5. Geriye dönük — bilinçli olarak YAPILMAZ

Eski dersler tek seferde tasnif edilmez (bir hafta prose üretir). Bir ders
**tekrarladığında** ya da bir film ona **dokunduğunda** KAPI satırı alır.
Bugün satır alanlar: `sayac.sh` 🧭 bloğu.

## 6. Şablon

**Film dersi (01-07) — 14.09.2026 şablonu:**

```
## 🔴 DERS ___: BAŞLIK — TEK CÜMLEDE NE OLDU

**FREKANS:** <n> film · <FILM> (mod D · ⑧) · <FILM> (mod V · ⑩) · …   ← ≥ 2
**DEĞİŞEN SATIR:** <PLAN sütunu | prompt satırı | liste maddesi | SPEC satırı>
**KAPI:** LİSTE · <03_PLAN_ONCESI maddesi / 02_RISK kartı / 00_SAHNE_TABLOSU sütunu>
**TEKRAR:** 0

**Kaynak:** <ilk vaka: film> QA (<tarih>) — <mercek>: <skor> — `<timecode> — <bulgu>`
**Örüntü:** <ne bozuldu, hangi filmlerde, ortak sebep>
**ÇÖZÜM:** <karar / araç / liste maddesi>   ← prompt cümlesi ancak betik ölçüyorsa
```

**Alet dersi (08/09) — 01.09.2026 şablonu (değişmedi):**

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
