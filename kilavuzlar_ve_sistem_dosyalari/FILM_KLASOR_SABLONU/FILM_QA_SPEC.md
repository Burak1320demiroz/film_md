# 📋 <FILM_ADI> — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretir: `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> <master>`

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar; ad değişirse üçü birden körleşir.

> ⛔ **DİKEY FİLMSE `## 🎬 SAHNE SPESİFİKASYONU` BAŞLIĞI ZORUNLUDUR**
> (08.09.2026'da ölçüldü). `rubrik_paketle.sh` filmin ailesini TEK bir satırla
> tespit ediyor:
> `AILE="yatay"; grep -qE "^## .*SAHNE SPESİFİKASYONU" "$SPEC" && AILE="dikey"`
> Başlık yoksa dikey film **YATAY sanılır** ve paket her merceğe YANLIŞ bloğu
> verir (① KARE'ye A+B+UYARI yerine A, ④ HİKAYE'ye B yerine A+UYARI…).
> ⚠️ Arıza SESSİZDİR: betik hata vermez, `aile: yatay` yazıp geçer — koşu
> sonunda kimse yanlış belgeyle bakıldığını fark etmez.
> Kontrol: betiğin son satırında `aile: dikey` yazdığını GÖZLE doğrula.
> (Depodaki beş dikey filmin beşi de başlığı taşıyor; risk YENİ filmdedir.)

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              <FILM_ADI>
FORMAT:            ⬜
RUNTIME:           ⬜ seconds (title card: ⬜ — screen text lock ⬜ s)
SCENE COUNT:       ⬜
THEME:             ⬜
THEME SCENES:      ⬜ S· S· S     ⛔ en az üç (yazılmayan tema dekoratif)
INTENDED EMOTION:  ⬜
ENDING TYPE:       ⬜
PROTAGONIST:       ⬜ (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    ⬜ S⬜
DIALOGUE LINES:    ⬜ · register: HUMAN ⬜ / MACHINE ⬜
SILENT SCENES:     ⬜
VIRAL INTERSTITIALS: ⬜  ⛔ THESE MAY NOT BE CUT
TITLE:             ⬜ başlık ne söz veriyor
LIBRARY CONTEXT:   ⬜ aynı raftaki kardeş filmler
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      ⬜
SHOT COUNT:      ⬜ · sahne içi kesme ⬜
TARGET ASL BAND: ⬜   ASL CURVE: ⬜
                 ⛔ sabit ızgaralı filmde GEREKÇE SATIRI ZORUNLU [D74]
GRID:            sahne başlangıcı(n) = ⬜ hook + (n−1) × ⬜ klip
RUNTIME:         ⬜
RAW FOOTAGE:     ⬜ · TRIM BUDGET: ⬜
SCREEN TEXT:     ⬜ saniye
CAMERA:          ⬜ / ⬜ sabit lockoff
SETUP SEQUENCE:  ⬜ sahne sahne kurulum imzası
KURULUM İSKELETİ: ⬜ harf dizisi (PLAN'daki ile AYNI olmak zorunda)
KÜME:            ⬜ kaç küme · hangi sahneler (12+ sahnede ≥2 · ACI_YAYI §4b)
DÖNÜŞ:           ⬜ %⬜ (12+ sahnede ≥%40; dönüş = kaynağından ≤3 sahne sonra)
ANGLE ARC:       ⬜ kaç açı TİPİ (§2 en az 3 ister)
DORUK:           S⬜ → ⬜ (sahne başlangıcı ⬜ s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Yazılan her kayıt formülle DOĞRULANIR; sapma varsa paket TAM DEĞİLDİR.

FİNAL VURUŞ KANITI [D141]:
   ⬜ nesne · ⬜ saniye · ⬜ kaç tane · BULUNAN mı BULUNMAYAN mı
   ⛔ tek karede sayılabilir ve adı konabilir olmalı; "final duygusu" değil
   ffmpeg -ss <saniye> -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: ilk kare ↔ son kare — aynı kurulum · ölçek · ışık · jest mi
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  ⬜     (1 = insan var · - = insansız · sahne başına bir karakter)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         ⬜
KASK          ⬜ vizör optik berrak · sırt ünitesi YOK — düz siluet [D79]
NOVUM         ⬜ kuralın kendisi + neyin ihlali olduğu
YERÇEKİMİ     ⬜ g
ATMOSFER      ⬜
EKRAN YÖNÜ    ⬜ hedef hep ⬜ · ilerleme ⬜ — kaç sahnenin kaçında sabit
SAYAÇ         ⬜ monotonik mi, hangi sahnede hangi değer
EŞ KADRAJ     ⬜ S⬜↔S⬜
YIPRANMA      ⬜ sabit bölge sayısı [D42]
IŞIK TAKVİMİ  ⬜ monotonik mi
SES REGISTER  ⬜ HUMAN ⬜ · MACHINE ⬜
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
KAPI          ⬜ ne ölçüyor
KOMUT         ⬜
DOĞRULANDI    ⬜ ffmpeg <sürüm> · <tarih>
              ffmpeg -hide_banner -filters | grep -q " <filtre> " || kapıyı yeniden yaz
İKAME         ⬜ filtre yoksa hangi ölçüm koşulur
```
