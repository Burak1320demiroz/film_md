# 🩹 POST-TRAVMA VE DURUM HAFIZASI KILAVUZU — Darbe Kesmede Sıfırlanmaz, Giden Geri Gelmez

> **Neden var (22.09.2026):** Üç ayrı arıza aynı kökten çıkıyor: **model bir önceki
> klibi görmez.** Her klip Bible'ın nötr, temiz, dimdik bedeninden doğar.
>
> | arıza | ders | son vaka |
> |---|---|---|
> | **beden sıfırlanması** — darbeden sonra nötr duruş | **D207** (4 film) | THE_SLOW_RAIN S14 sert çakılma → S15 karda rahat oturuyor (⑩ Desen ⑧) |
> | **hasar/kir sıfırlanması** — iz, yırtık, kir kaybolur | **D42** (kir) · **D84** (sahneler arası nicelik) | THE_STOLEN_SKY ② PART 4 "çizik deseni sıfırlanması" |
> | **kadro sıfırlanması** — giden figür geri gelir | ADAY (bu kılavuz) | THE_STOLEN_SKY S13'te vurulan asker S24'te hasarsız (② PART 3 🔴) |
>
> TUR 24'ün 3. raporu bunlar için bir "anti-reset protokolü" önerdi; bu kılavuz o
> protokolün depo ölçümünden geçen kısmıdır. ⚠️ Rapor arızaya yanlışlıkla "D42" dedi:
> depoda D42 kir sürüklenmesidir, beden sıfırlanması D207'dir.
> Reddedilenler: `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 24 ② (R3).
>
> **Ne zaman okunur:** filmde darbe, düşüş, kaza, yaralanma, giysi hasarı ya da kadrodan
> çıkan bir figür varsa — sahne haritası yazılırken ve o sahneden SONRAKİ her klip
> yazılırken. **Kapılar:** ㉜④ `CONTINUOUS ACTION:` (sahne içi) · QA ② DEVAMLILIK
> `WEAR TIMELINE` · ⑩ OYUNCULUK Desen ⑧ · ⑧ EFOR.
> ⚠️ **Etiket:** her kalıp ÖNERİ'dir; raporun koruma yüzdeleri (%79-91) kaynaksızdı.

---

# 1. 📉 TOPARLANMA MERDİVENİ — darbeden sonraki klipler

## 1.1 D207'nin sayısı ile raporun merdiveni aynı şeyi söylüyor

D207'nin çözümü PLAN'da bir **BEDEL EĞRİSİ** kurar: sahne başına yorgunluk **0-6**,
ardışık sahnede en çok **1 kademe** düşer, sıfırlama yalnız yazılı dinlenmeden sonra.
Raporun dört basamaklı merdiveni bu eğrinin darbe sonrası dört klibidir:

| klip | D207 seviyesi | beden | hareket kısıtı |
|:--:|:--:|---|---|
| **darbe** (N) | 6 | çarpar, kayar, durur — uzuvlar gevşek | aktif hareket yok; toz/buz iner |
| **N+1** | 6 → 5 | yerde; göğüs hızlı inip kalkıyor, bir el göğüs plakasında | kalkamıyor; dizini çekiyor, bırakıyor |
| **N+2** | 5 → 4 | tek dizden, bir yana yaslanarak doğruluyor | bir bacağa ağırlık vermiyor |
| **N+3** | 4 → 3 | öne eğik, kısa adımlar, bir el bir yüzeye dayalı | bir botu sürüyor; hız ilk adımlardan düşük |

⭐ Çok klipli sahnede bu dört klip **tek sahnedir** (4 kliplik bir BEDEL sahnesi).
Durum kilidi (`CONTINUOUS ACTION:`) basamağı bir sonraki klibe taşır ve ㉜④ onu zorunlu
kılar. Merdivenin kendisi bu rejimin en doğal kullanım yeridir.

## 1.2 Yazım — acı değil MEKANİK

```
⛔ "a severely injured astronaut writhing in acute physical pain"
   → POLITIKA red sözlüğü (wound · injury · pain yoğunluğu) + model jenerik yüz ifadesi
     üretir, bedeni sabit tutar (raporun kendi gözlemi)
✅ "she lies on her side on the ice, one glove pressed flat to her chest plate, her
   chest rising and falling fast; she draws one knee up, lets it slide back down"
✅ "she rises from one knee, leaning her weight onto her right hand on the sled rail,
   her left boot barely touching the ice"
✅ "she walks bent forward, short uneven steps, dragging the left boot a hand's length
   behind the right"
```

Sakatlık **hangi uzuvda** olduğuyla yazılır ve o uzuv sahne boyunca aynı kalır
(PROMPT_HATA §3 sınıf 3a: asimetrik işaret hangi kolda). `limping` tek başına iki
klipte iki farklı bacak üretebilir; `dragging the left boot` üretmez.

⛔ **Düşen, bir sonraki klipte yürüyerek başlamaz.** Klip N "yere çarparken" bitiyorsa
N+1 "yerde, hareketsiz" başlar (rapor 3 · §1.1 · `CONTINUOUS ACTION:`).

## 1.3 Sahne sınırında eğri devam eder

Sahne değişince durum kilidi satırı yazılmaz (㉜④ ilk klip) — ama BEDEL EĞRİSİ
sürer. Yeni sahnenin 1. klibinin IMAGE promptu, önceki sahnenin SON bedenini SUBJECT
satırında taşır [D207 DEĞİŞEN SATIR]. Eğri yalnız **yazılı dinlenmeyle** sıfırlanır
(bir sahne ya da bir satır: "she sits against the sled for a long moment, breathing slows").

---

# 2. 🧥 HASAR HAFIZASI — iz yerinde kalır

## 2.1 Düz cümle, konum, birebir kopya

Raporun önerdiği `[SPEC DAMAGE STATE: cracked right visor corner …]` bloğu **alınmadı**:
köşeli, büyük harfli etiket depoda **kadraja basıldı** (PROMPT_HATA §6: `PHASE 1` göğüs
plakasına, `EVA` sırta, `S04` gövdeye). Hasar, D42'nin biçimiyle **konumlu düz cümle**
olarak yazılır ve sahnenin/filmin her klibinde **harfi harfine** kopyalanır:

```
✅ "a pale scrape runs diagonally across the lower right of her chest plate, and grey
   frost dust is packed into the knees of the suit and both glove palms; the back and
   shoulders stay clean"
```

| hasar | nasıl yazılır | not |
|---|---|---|
| sürtünme/çizik | yön + yer + renk: `a pale diagonal scrape across the lower right of the chest plate` | yüksek kontrast iz daha iyi tutar (rapor · ÖNERİ) |
| kir/toz | yer + sınır: `packed into the knees and glove palms; the shoulders stay clean` | D42 biçimi — "dirty suit" yetmez |
| kumaş yırtığı | yer + boy + alttaki katman: `a short torn flap on the left shoulder seam, the grey layer beneath showing` | ⚠️ bkz. §2.3 |
| kask/vizör | ⚠️ vizör çatlağı yüzü ve D79 şeffaflığını bozar; kaskın **kenarında** çizik tercih | çatlak camın ardı okunmaz |
| sıvı/leke | yer + renk + kuruluk: `a dark dried streak down the right shin` | ⛔ "blood" yazılmaz (POLITIKA) |

## 2.2 Metin tek başına tutmaz — referans paneli

PROMPT_HATA §4: **durum merdiveni metinle tutmuyor** — THE_FROST_LINE dört fazı kusursuz
yazdı ve altı devamlılık bulgusu aldı. Kalıcı ve sahneler boyunca taşınan hasar bir
**biçim kilididir** ve `REFERANS_PAKETI_KILAVUZU` §1 tetikleyicisidir [D146 · D168]:

```
□ hasar ≥ 2 sahne sürüyorsa: referans paketine "hasarlı hâl" sayfası (ön + arka)
□ hasarın oluştuğu sahnenin onaylı karesi, sonraki sahnelerin imaj üretiminde referans
□ kare onayı (COK_KLIPLI §3.3): hasar yerinde mi, tarafı doğru mu
```

## 2.3 Hasar ile mühür çakışması

Basınç giysisi yırtığı D175/㉑ mühür kapısına dokunur: yırtığın altı **çıplak deri
olamaz** (negatif çekirdeğin çıplak-deri cümlesi). Yırtık yazılacaksa altındaki katman
**adlandırılır** (`the grey inner layer showing`), deri değil.

---

# 3. 👥 KADRO KİLİDİ — giden gelmez

## 3.1 Pozitif sayı, adsız tarif

```
✅ "exactly two people are in frame: the woman in the grey suit at the console and the
   man in the orange suit by the door"
⛔ "the soldier who was shot is gone" · "no resurrected figure" · "no ghost of the
   fallen crew member"                                    → D59: yasak isim kazanır
⛔ özel ad (D34) — "Mara", "Sarı Asker" promptta geçmez
```

- Negatif çekirdeğin ilk cümlesi (`Exactly one human character, no duplicates`) tek kişilik
  filmde bu işi zaten yapar. **Çok kişili** filmde çekirdek cümle o sahnenin sayısına
  **güncellenir** (`Exactly two people, no third figure, no duplicates`) — sayı kadrodan
  biri çıktığı sahnede DÜŞER ve bir daha yükselmez.
- Kadrodan çıkış PLAN'da bir satırdır: `KADRO: S01-S12 üç kişi · S13 sonrası iki kişi`.
  Bu satır her sonraki klibin sayı cümlesine iner.
- Çıkan figürün **eşyası** da çıkar (kask, kalkan, renk bandı): model tanıdık eşyayı gördüğü
  yerde sahibini geri çizer.

## 3.2 Neden aday, ders değil

Kadro dirilişi depoda şimdilik **bir** kayıtta (THE_STOLEN_SKY PART 3). İkinci filmde
tekrar ederse ders olur; değişen satır PLAN `KADRO:` satırı ve negatif çekirdeğin sayı
cümlesidir. Kayıt: `DERSLER/GOZLEM_DEFTERI.md` (açılmadı — ilk tekrar beklenir).

---

# 4. ✅ KONTROL LİSTESİ

```
□ darbeden sonraki klipler D207 eğrisinde en çok 1 kademe iniyor; ilk klip yerde başlıyor
□ sakatlık hangi uzuvda — adıyla ve sahne boyunca aynı
□ acı/yara kelimesi yok; beden mekaniği var (POLITIKA §2.2)
□ hasar konumlu düz cümle, her klipte birebir; köşeli/büyük harfli etiket YOK (§6)
□ hasar ≥ 2 sahne sürüyorsa referans paketinde "hasarlı hâl" sayfası
□ yırtığın altındaki katman adlandırılmış (çıplak deri değil)
□ çok kişili filmde her klipte "exactly N people" + kişi tarifi; N kadro çıkışında düşer
□ çıkan figürün eşyası da kadrajdan çıktı
```

# 5. ⬜ ÖLÇÜLMEMİŞ

- Dört basamaklı merdivenin, sahne içi `CONTINUOUS ACTION:` ile birlikte ⑩ Desen ⑧ sayısını düşürüp düşürmediği (ilk çok klipli filmde).
- Kadro sayı cümlesinin dirilişi önleyip önlemediği (tek vaka).
- "Hasarlı hâl" referans sayfasının hasar sıfırlanmasına etkisi.

**Kaynaklar:** [D207] · [D42] · [D84] · [D146] · [D168] · [D175] · [D59] · [D34] · [D79] ·
`PROMPT_HATA_ONLEME_KILAVUZU` §3 · §4 · §6 · `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU` §2.2 ·
`COK_KLIPLI_SAHNE_KILAVUZU` §3 · TUR 24 rapor 3 (`URETIM_ONCESI_ANALIZ/TUR24_HAM_RAPORLAR/`).
