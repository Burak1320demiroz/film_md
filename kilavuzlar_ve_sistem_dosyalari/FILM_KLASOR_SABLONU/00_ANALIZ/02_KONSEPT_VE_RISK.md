# 🧠 <FILM_ADI> — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     ⬜ [sahip verdi / AI seçti]
   AI seçtiyse GEREKÇE ⬜ — sayaç 🎭 TEMA DAĞILIMI'nda en az kullanılan tema
   ⬜ · §8 matrisinde tükenmemiş ortam kartı ⬜ · kullanılmamış novum tipi ⬜
   ⛔ "İlginç geldi" gerekçe değildir; seçim DEPODA EKSİK OLANDAN yapılır.
② FORMAT:   ⬜        → kart §2.⬜ · bölüm sayısı ⬜
③ SAHNE:    ⬜        → [formatın varsayılanı / bandın üst ucu / sahip verdi]
   ⛔ Bandın DIŞINDAYSA sahibin açık izni + gerekçe [D74]: ⬜
④ REFERANS PAKETİ: ⬜ [YAZILSIN / YAZILMASIN / ANALİZ KARAR VERSİN]
   "analiz karar versin" ise §5b'deki altı tetikleyici tablosu doldurulur.
   "yazılmasın" ise PLAN'a düşecek TEK SATIR gerekçe: ⬜
⑤ HİKÂYE ONAYI (14.09.2026): `00_HIKAYE_ONAYI.md` ONAY ⬜ <tarih> · TUR ⬜/3
   ⛔ Bu dosya onaylı hikâyeyi İYİLEŞTİRİR, değiştirmez. Aşağıdaki hiçbir
   kapı (konsept · tema · novum · B5) onaylı LOGLINE / BEDEL / sahne
   satırlarını sessizce bozamaz; bozulacaksa 00_HIKAYE_ONAYI SAPMA + yeniden
   onay. Ders ve kapı dili BURAYA yazılır, onay dosyasına değil (㉙ jargon).
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "⬜"                        (kelimesi kelimesine, yorumsuz)
REPLİK: ⬜ [var / yok]   ⛔ talep cümlesinde diyalog geçiyorsa AYRI kapı
        zinciri açılır: SES_VE_DIYALOG §1a-§2a + DIALOGUE_CRITIQUE_PROMPT
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**
Emsal: THE OPEN CIRCUIT'te *"fırtınalı"* ve *"patlamalı"* istekleri 610 Pa
Mars basıncında imkânsızdı; ikisi de yeniden tanımlandı, gerekçe yazıldı ve
biri filmin novum'u oldu.

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| ⬜ |  |  |  |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        ⬜ [dikey shorts / yatay 2-4 / 3-5 / 7-9 / 10-20]  → §2.x kartı
ORTAM:         ⬜ §3 kart numarası                → tetiklediği zorunlu satırlar: ⬜
TÜR:           bilimkurgu · dal: ⬜               → §4.1
KLİP SÜRESİ:   ⬜ s  ⛔ ARAÇTAN ÖLÇÜLDÜ [D124], seçilmedi
SAHNE SAYISI:  ⬜    RUNTIME: ⬜ = hook + (sahne−1) × klip
BÖLÜM SAYISI:  ⬜    (formattan gelir — §2.0, tercih değil)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               ⬜ tek cümle, kuralın kendisi
NOVUM TAŞIYICISI:    ⬜ <nesne> × <jest> → <ihlal>
① TEK KARE:          ⬜  ⛔ cümle TAŞIYICI NESNENİN ADINI içermeli [D157]
② KİNETİK BAĞIMSIZLIK: ⬜ kural replik/dış ses/ekran metni olmadan kanıtlanıyor mu
③ BAŞLIK ŞEMASI:     ⬜ ≤5 kelime
⛔ Üçü de ✅ değilse KONSEPT REDDEDİLİR ve sıralama yazılmaz.
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — ⬜        (⛔ satır başında "TEMA:" YAZILMAZ; sayac.sh tema
                          dağılımını film klasöründen ÖZYİNELEMELİ sayar ve
                          bu dosya gerçek temayı ikinci kez saydırır)
▸ tanım cümlesi — ⬜     ⛔ TAKAS kalıbı değil, TANIM cümlesi [§3c moratoryumu]
▸ depoda kaç kez kullanıldı — ⬜   (bash sayac.sh · TEMA DAĞILIMI bloğu)
▸ motif kanalları — ⬜ / ⬜ / ⬜   (nesne · kinesik · kamera · ışık)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

> ⛔ **PLAN YAZILMADAN ÖNCE.** 5+ risk çıkıyorsa KİLİT TAVANI (≤ 20 ders kilidi) —
> malzeme azaltılmaz; dışarıda kalan kilitler PLAN `UYGULANMAYAN KİLİTLER`e gerekçeyle
> (14.09.2026, 02_RISK_KARTLARI §RİSK TOPLAMI).

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| ⬜ | ⬜ |  |  |  |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  ⬜        (adıyla — risk kartı / göz kapısı)
POZİTİF BİÇİMİ:   ⬜        ⛔ SAYI taşımalı: süre · uzunluk · genişlik · adet
```

⛔ **Sıfat yetmez.** THE OPEN CIRCUIT 1 numaralı riskini (KIVILCIM) adıyla ilan
etti ve yalnız sıfatla korudu — *"TEK, İNCE, DÜZ ve SÖNÜMLÜ"*. Aynı planda
sayıyla yazılan her şey tuttu. Ekrana **en az 0,5 s süren, dallanan bir şimşek**
geldi; her sahnenin NEGATIVE bloğunda *"no lightning bolt"* yazılıyken.
**Negatif cümle yasağı söyler, BİÇİMİ söylemez; model boşluğu doldurur.**

```
TETİKLENEN RİSK:  ⬜ / ⬜
EŞİK:             5
⬜ EŞİĞİN ÜSTÜNDEYSE: hangi malzeme çıkarıldı → ⬜
                      çıkarılamıyorsa kabul gerekçesi → ⬜
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — yalnız soru ④ "analiz karar versin" ise

> `REFERANS_PAKETI_KILAVUZU.md` §1 tablosu. **Altısı da tek tek ölçülür.**

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ⬜ | |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ⬜ | |
| T3 | oranı sözle yazılamayan nesne | ⬜ | |
| T4 | insan dışı canlı | ⬜ | |
| T5 | tekrar eden insan dışı olay | ⬜ | |
| T6 | bir varlık tekrar tekrar dönüyor | ⬜ | |

```
KARAR: ⬜ [YAZILIR / YAZILMAZ]
⚠️ T1 bu deponun neredeyse her filminde doğrudur.
⛔ YAZILMAZ ise PLAN'a tek satır gerekçe [D74 kalıbı] — sessizce atlanmaz.
⛔ YAZILIR ise KAPI 0'dır: sayfası ONAYLI olmayan ve seed'i yazılmayan
   varlığın geçtiği hiçbir sahne üretilmez [D168].
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S⬜
NÖTR TARİFİ:         ⬜
⛔ "riskli sahne yok" geçerli DEĞİLDİR — en riskli kare her filmde vardır.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   ⬜  film başlamasa da var olan bir İŞ
         ⛔ "anlamak / görmek / fark etmek" İSTEK DEĞİLDİR
ENGEL:   ⬜
BEDEL:   ⬜ · S⬜        ⭐ ASIL KAPI BUDUR; sahne numarasız bedel BOŞTUR
MUHATAP: ⬜ [ikinci insan / kendi geçmiş kararı / kendi bedeni /
            ortamın KALICI değişen parçası]
AYRILIK: S⬜             (yalnız iki insanlı filmde — aynı fikirde OLMADIKLARI an)
```

Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — **istek yok · bedel
yok · muhatap yok** [`04_ARASTIRMA_BULGULARI.md` TUR 4].

---

## ✅ KAPI

```
□ konsept kapısı ①②③ üçü de ✅
□ risk sayımı yazıldı ve eşik kararı verildi
□ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor
→ üçü de ✅ ise 03_SAHNE_SIRALAMASI.md yazılabilir
```
