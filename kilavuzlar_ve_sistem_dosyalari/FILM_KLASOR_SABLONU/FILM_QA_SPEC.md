# 📋 <FILM_ADI> — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `<FILM>_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (0 replik · sabit
> lockoff · tasarımlı sessizlik · metinsiz sayaç) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar; ad değişirse ikisi birden körleşir.

> ⚠️ **DİKEY FİLMDE `## 🎬 SAHNE SPESİFİKASYONU` BAŞLIĞI — artık MAKİNE KAPISI
> DEĞİL.** Bu başlığı yalnız `rubrik_paketle.sh` okuyordu (aile: yatay/dikey) ve
> o betik 11.09.2026'da silindi. Başlık yazım geleneği olarak KALABİLİR; hiçbir
> betik ona bakmaz, yokluğu artık sessiz bir arıza üretmez.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + sahne promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası · çapa jestleri) + C (el/ayak/baş kilitleri)  MOD D
⑮ 🧭 YÖN         → C BLOĞU ekran yönü kilitleri (hedef dilimi · hareket yönü · eksen) + A  MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⭐ 14.09.2026: ⑭/⑮ için C bloğuna yazılacak satırlar — `HAREKET KİLİDİ:` (eller/ayaklar/baş ne
   yapar, "tek jest" kuralı) ve `EKRAN YÖNÜ:` (hedef hangi dilimde · figür hangi yöne · eksen
   çizgisi — screen-left/right, pusula yok). Yoksa iki mercek çıkarımla koşar ve bunu yazar.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              <FILM_ADI>
FORMAT:            ⬜
RUNTIME:           ⬜ seconds (title card: ⬜ — screen text lock ⬜ s)
SCENE COUNT:       ⬜
PART GRID:         — (yalnız 6/8/16 dk hattı [§2.6/§2.7/§2.8]: n PART satırı — B1 = S00-S17 · 18 clips ·
                   0-180 s · B2 = S18-S35 · 18 clips · 180-360 s (6 dk) … 16 dk: B1-B4 × 24 clips ×
                   240 s + FULL = S00-S95 · 96 clips · 0-960 s. QA her parçaya AYRI koşar; rubriğe
                   SPEC'le birlikte "THIS FILE IS PART n OF m — …" beyanı yapıştırılır;
                   BOUNDARY PAIR(lar) elle kareyle kapanır. Diğer formatlarda "—" kalır)
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
SCENE PLAN:      — (yalnız ÇOK KLİPLİ SAHNE filminde [COK_KLIPLI_SAHNE §1 · 22.09.2026]: PLAN'daki
                 SAHNE PLANI satırı + "S01 = K01 · S02 = K02-K04 · …"; SCENE COUNT ≠ CLIP COUNT)
INTRA-SCENE CUTS: — (aynı rejimde: K02|K03 · K03|K04 · … — these cuts are INSIDE one scene:
                 location, light, sound bed, costume dirt, held object and body pose MUST match
                 across them; a reset here is a ② CONTINUITY defect, not a scene change)
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
DÜNYA ÇAPASI  ⬜ 3/3 — gök · ufuk · yer imi (World Bible'daki üç cümle BİREBİR; dış-mekân promptlarında sıfır sapma) [D209]
YIPRANMA      ⬜ sabit bölge sayısı [D42]
KİMLİK DİZİSİ ⬜ kask K/A sahne başına (sahne sayısı kadar harf) · amblem SOL/SAĞ omuz · giysi rengi ·
              kir bölgesi + başlangıç sahnesi · hasar başlangıç sahnesi (geri dönmez) [D208]
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
