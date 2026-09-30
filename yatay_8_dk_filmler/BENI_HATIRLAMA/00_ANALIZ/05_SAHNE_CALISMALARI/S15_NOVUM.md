# 🔬 S15 — KİLİT SAHNE · NOVUM · SAHNE ÇALIŞMASI · BENI_HATIRLAMA

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır. Aşağıdaki İngilizce
> satırlar kilit ve sınır CÜMLELERİDİR.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> sahneye düşen satırları. Bu dosya bitmeden bu sahnenin promptu yazılmaz.

---

## 🪪 KİMLİK

```
SAHNE:      S15              BAŞLIK: İçinden kum
BÖLÜM:      BENI_HATIRLAMA_BOLUM_2.md
ZAMAN:      150,0 s → 160,0 s (2:30-2:40)   ⛔ FORMÜLLE [D122]: S_n = n × klip · 10 s VARSAYIM
VURUŞ:      NOVUM TEK KARE (ONERME §4 ①) · kural görünür — 1. perde sonu bloğu
B5 SATIRI:  ENGEL (kuralın kendisi: görüntüyü tutmak canlının ışığını tüketir)
⭐VİRAL:    hayır — adamın yüzü kadrajda değil
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Diz çökmüş figür iki kez doğrulmaya çalışır; her deneyişte dizlerinin dibindeki canlının ışığı
                 kuyruktan başa doğru bir el geri çekilir.
BAŞTA (imaj t=0 · yük altında, dengede): figür doğrulmanın yarısında — bir dizi kumdan kalkmış, sol eli o dizde;
                 canlının sırtındaki ışık yamaları kuyruktan başa üçte ikisi boyunca yanık
SONDA:           figür yine iki dizinin üstünde, başı eğik; yamalar bir el daha geride (sırtın yarısı); adamın omzu
                 kadrajın solunda bir parmak öne kaymış
⛔ KLİP İÇİ DEĞİŞİM: VAR — ışık seviyesi
   Seçim: ② değil ① de değil — IŞIK KENARI HAREKETİ: seviye değil, yamaların kenarı kuyruktan başa İLERLER
   (geometri sabit, yalnız ışığın kenarı yürür [D43]). Gerekçe: nitelik değişimi en zayıf eksen (0,0687);
   hareket olarak yazılan ışık kenarı "tek sürekli hareket" şartına uyar [B15 ①].
```

```
TEK KARE CÜMLESİ [D157 — taşıyıcıların ADI içinde]:
  "Kasksız, yarı saydam bir KADIN FİGÜRÜ kumda diz çökmüş, SARI ATKISI kumda yayılmış, omuzlarının içinden arkadaki
   kum tepesi görünüyor; dizlerinin dibinde ışığı geri çekilen küçük CANLI yatıyor."
  → izleyici 1 sn'de "kadının içinden kum görünüyor"u işaret eder.
  ⛔ Promptta canlının bacak/göz SAYISI YAZILMAZ (varlık şeridi K3 — sayı yalnız S11 · S39-S40);
     "its low rounded back and short legs tucked under it" yeter.
İKİNCİ TEK KARE: S33 (mağarada aynı kural — figür yürür, arka planda yamalar düşer)
KURAL TEKRARI: KURULUM S9-S11 · bu sahne GÖRÜNÜR KILAR · DOĞRULAMA S25 · S31 · S33 · SONUÇ S36-S37
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  E        İŞARET: dönüş S13 → "— the same position, height and lens as Scene 13."
⛔ dönüş → kamera metni S2'deki E kartından BİREBİR kopyalanır + işaret satırı

LENS:           35 mm    MESAFE: 1 m back from his right shoulder (figüre ≈4 m · adam-figür 3 m)   YÜKSEKLİK: 1,6 m
ÖLÇEK:          medium shot   AÇI TİPİ: over-the-shoulder
KADRAJ ENİ:     4,11 m × 2,31 m (figür düzleminde)   ⛔ HESAPLANDI — figür (diz ≈1,0 m) + canlı (0,5 m) + adamın omuz/kask
                arkası sol kenarda ≈⅓ → SIĞIYOR ✅
ANA NESNE PİKSEL: canlı 156 px ✅ · figür (diz) 311 px ✅ · ışık kenarının yolu (bir el ≈0,1 m) ≈30 px ⚠️ → yamaların
                TOPLAM boyu (sırt ≈0,4 m → 125 px) okunur; kenar hareketi bu boyun oranıyla yazılır ("from two-thirds to half
                of its back")
ÖNCEKİ SAHNEYLE (S14 · Y ısı CU): ölçek 1 kademe · azimut muaf (ısı görüşü) → bant içi ✅
SONRAKİ (S16 · B WS): ölçek 1 kademe · 130° ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 insan (adam, sırt/omuz) + 1 figür + 1 canlı
                ⛔ film boyu KİLİT: "Exactly one person in a pressure suit and one semi-transparent woman figure, and no third
                figure." · KONUM: adam sol üçte bir (yakın), figür sağ-orta · merkez çizgisi geçilmez · temas 0 · en yakın 3 m
AYRIM EKSENİ:   opak kemik beyazı hacim (yakın, sol) ↔ yarım saydam koyu lacivert kazak (uzak, sağ-orta) ↔ gri-kahve alçak
                yuvarlak form + kehribar yamalar (figürün dizlerinin dibi, AYRI bölge — LOOK_UP ham ⑤ kayması için)
GİREN NESNE:    —        ÇIKAN NESNE: —
TAŞINAN NESNE:  numune kutusu adamın sağ eldiveninde (S12 → S16) · figürün atkısı kumda yayılmış (S13 → S17) ·
                4 bilek lambası (S6 → S25) · kir F1
⛔ BİÇİM KİLİDİ: giysi sırtı (E kurulumu) — SIRT_POZİTİF cümlesi · kask arkası tek cümle · canlı K3 (anatomi bloğu kısaltılmaz,
                sayısız hâli) — paket yok (R2)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      difüz gri gün ışığı, yüzey kademe −2 (S12 düzeyi; S16'da −3) · figür kumla aynı ışıkta · canlının kehribar
           yamaları yalnız çevresindeki bir el kumu aydınlatır, aydınlık kum dokusunu korur [D29]
PALET:     P1 gri-kahve   ⛔ önceki S14 P2 (ısı renk alanı) — farklı ✅
SES:       Y1 rüzgâr açık + canlının her nefeste yumuşak hırıltısı   ⛔ önceki S14 boğuk hırıltı + nefes (ısı görüşü) — farklı ✅
MÜZİK:     yok / alçak yatak (MUZIK dosyası kararı)
FİZİK:     figürün dizlerinin altında kum ÇÖKMEZ, iz yok (novum) · canlının altında kum her nefeste bir parmak kıpırdar ·
           adamın botları bir parmak gömülü · kum çizgileri soldan sağa
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (adamın yüzü kadrajda yok · figürün yüzü hiçbir karede yok)
HAREKET:   — → etiket YOK
```

## 🧑‍🎤 OYUNCULUK — izleyici cümlesi · kart bağı · doluluk

```
İZLEYİCİ CÜMLESİ: Figürün kalkmasını istiyor; her deneyişin canlıyı söndürdüğünü görüyor.
NİYET KANALI (≤2): ① bakış — kask figürden canlıya bir kez iner ② ağırlık — bir adım öne kayar, tamamlanmaz
TASK ONLY:        hayır · DAVRANIŞ HANESİ T (tereddüt) · TEMPO N
KART BAĞI:        adam — BASKI TEPKİSİ "kontrol eder" (kask canlıya iner) · figür kartı — İSTEK (doğrulma = sıcaklık/siper)
                  · TEMPO satırı (figür adamdan ≥1 s SONRA kıpırdar: adamın ağırlık kayması 2,0 s → figür 3,0 s'de kalkar)
SON 3 s (7-10 s): figür iki dizinin üstünde, omuzları canlının nefes ritmiyle kalkıp iner; yamaların kenarı sırtın yarısında
                  ritimle bir parmak ileri geri gider; adamın omzu öne eğik kalır; kum çizgileri akar
ÖLÜ SAHNE 5 SORU: ① SÜREÇ (doğrulmaya çalışmak ×2) ✅ ② direnç: her deneme ışığa mal olur ✅ ③ tek kilit ✅
                  ④ sınır: S14 ısı yaması → S15 aynı canlı normal görüşte ✅ ⑤ çevre saati: canlının nefes ritmi ✅
```

```
TEK KİLİT — IMAGE: A semi-transparent woman figure kneels halfway up on one knee a hand above the creature; the lit patches
                   along its back reach two-thirds of the way from tail to head.
TEK KİLİT — VIDEO: Each time she rises, the edge of the lit patches on its back draws back toward its head, from two-thirds to
                   half of its back over the clip.
SINIR (End/Start, prompta girmez):
  END S14:   in the heat view the cold patch edge has crept one finger forward along its left flank.
  START S15: over his right shoulder, she is halfway up on one knee above the creature, its lit patches two-thirds along its back.
  END S15:   she is down on both knees again, head bowed, the lit patches half along its back.
  START S16: wide, the man holding the grey case, his helmet turned toward the lander on screen-left.
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D157 | TEK KARE: saydam figür + ışığı geri çekilen canlı AYNI karede, ayrı bölgede | IMAGE tek kilidi (yukarıda) |
| D192 | 1 no. risk sayıyla | "about half strength" · "a head shorter than the man" · "three metres from him" |
| D20 | sayı iki ayrı cümle | "Exactly one person in a pressure suit and one semi-transparent woman figure, and no third figure." |
| D123 · D56 | yara/ölüm/örümcek sözlüğü | "a low rounded creature like a seal pup … a dark cold patch on its left flank where its light is absent" · dying/wounded/web 0 |
| D43 · D29 | ışık değişimi kenar hareketi, bloom yok | "the edge of the lit patches draws back toward its head … the lit sand keeps its texture" |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ R4 | saydam figür hiç üretilmedi (C7) — hayalet ya da opak çıkar | K3 PROBU ilk üretim günü: bu karenin iki biçimi (saydamlık "at about half strength" ↔ "the dune crest is clearly visible through her shoulders and sweater") · İPTAL KAPISI | ✅ tasarım · ⬜ prob |
| 2 | ⛔ R1 | klon / adam-figür karışması | adamın yüzü yok (E sırt) · konum kilidi · iki sayı cümlesi | ✅ |
| 3 | ⛔ R7 | yaralı/ölüyor sözlüğü | nötr sözlük (yukarıda) NEGATIVE dahil | ✅ |
| 4 | ⚠️ Y9 | E kurulumunda giysi sırtı sırt çantası/tüp üretir | IN FRAME: back → SIRT_POZİTİF cümlesi | ⬜ yazımda |
| 5 | ⚠️ Y21 | figür arka planda odak dışı yazılırsa ikinci insan belirsizleşir | "deep focus", figür ve canlı netlik bandında | ⬜ yazımda |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   orta   sınıf: PK (diz çökmüş genç kadın + ışığı sönen canlı → ölüm/yara okuması)
NÖTR TARİF:  "she rises halfway on one knee and lowers back onto both knees, head bowed" · "its amber light draws back from tail
             toward head at one slow rate" · yaş "in her late twenties"
⛔ YASAK CÜMLE YAZILMAZ — karşılığı POZİTİF kilit: "the rest of its hide is whole" · "her feet and knees leave no marks in the sand"
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — canlı 156 px · figür 311 px (≥100); ışık kenarı oranla yazıldı
☑ önceki sahneyle ardışık çift bant içi (ısı muafiyeti gerekçeli)
☑ kurulum harfi + işaret satırı yazıldı (E · dönüş S13)
☑ ⛔ uyarıların hepsi kapandı (R4 probu üretimin İLK işi)
☑ politika satırı yazıldı
☑ ⭐VİRAL değil — gerekçeli
→ BENI_HATIRLAMA_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir · ⛔ ÜRETİMİ K3 probuna bağlı
```
