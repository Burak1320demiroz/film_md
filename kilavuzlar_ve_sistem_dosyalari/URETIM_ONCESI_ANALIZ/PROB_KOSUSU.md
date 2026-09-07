# 🧪 PROB KOŞUSU — dört yasağın yeniden sınanması

> **Ne için:** `05_DIKEY_HAT_TESHISI.md` §5④. Depo dört yasakla çalışıyor
> (ikinci insan yok · replik yok · isim yok · kesme yok) ve dördü de
> **~06.08.2026'da, başka bir model sürümüyle** ölçüldü. O günden beri
> bir kez bile sınanmadı. Bugün elde **bulgu değil, üç haftalık varsayım** var.
>
> **Maliyet:** 2 klip · ~4 dakika insan eli.
> **Çıktı:** `04_ARASTIRMA_BULGULARI.md`'ye tek satırlık hüküm.
> **Durum:** ⏳ ÜRETİM BEKLİYOR (30.08.2026 · ölçüm tarafı hazır ve doğrulandı)

---

# ⛔ ÖNCE: BU KOŞUNUN İKİ YARISI VAR

```
ÜRETİM  →  insan eli. Depoda API/anahtar/gcloud YOK; üretim Flow/Veo
           arayüzünden yapılıyor ve dosya ~/Downloads'a iniyor
           (emsal: THE THIN ROOF üretim notları, 27.08.2026 16:53-17:30).
ÖLÇÜM   →  makine. prob_olcum.sh · 30.08.2026'da gerçek master üstünde
           doğrulandı; hüküm sayıları modele SORULMAZ [D125].
```

⚠️ **NEDEN ÖNEMLİ — bu koşu bir dikey mesele değil:**
`yatay_10_20_dk_filmler/YERCEKIMI/` şu anda yazılıyor ve içinde
**39 adet iki-insanlı prompt** var (FAZ_01: 7 · FAZ_02: 6 · FAZ_03: 14 ·
FAZ_04: 12). Yani depo, PROB A'nın cevabını **bilmeden** iki insanlı bir
filme yatırım yapmış durumda. Prob tutmazsa o 39 prompt yeniden yazılır;
tutarsa hem YERCEKIMI hem dikey hat açılır. **İki klibin karşılığı budur.**

---

# 1. KOŞU — adım adım

```
1. Aşağıdaki iki kod bloğunun İÇİNİ ayrı ayrı kopyala.
   ⛔ Türkçe başlık ekleme · iki promptu birleştirme · yarım yapıştırma
      [KILAVUZ_REHBERI §7 KOPYALAMA — üçü de doğrulanmış red sebebi]
2. Üret. Süre 10 s, en-boy 9:16.
3. İnen dosyayı yeniden adlandır:  PROB_A.mp4  ·  PROB_B.mp4
4. Ölç:
      bash kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/prob_olcum.sh A ~/Downloads/PROB_A.mp4
      bash kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/prob_olcum.sh B ~/Downloads/PROB_B.mp4
5. ⬜ işaretli maddeler için betiğin ürettiği PNG'lere bak (tek tek kare
   değil, yan yana dizilmiş kareler — 4 görüntü, ~1 dakika).
6. §3'teki tabloyu doldur, hükmü 04_ARASTIRMA_BULGULARI.md'ye yaz.
```

⚠️ **RED GELİRSE:** mesaj tipine göre davran [KILAVUZ_REHBERI §7
"HATA MESAJLARI AYRIMI"]. *"I can't generate that video"* = politika
reddi → prob metnini DEĞİŞTİRME, hükmü **"POLİTİKA REDDİ"** diye yaz
(o da bir bulgudur). *"something went wrong"* = teknik → tekrar dene.

---

# 2. PROMPTLAR

## PROB A — İKİNCİ İNSAN (D20 sınanıyor)

> Sorduğu tek soru: **model, aynı kadraja iki AYRI insan koyabiliyor mu,
> yoksa hâlâ kopya mı çiziyor?**

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 35mm spherical,
fixed tripod 1.55 metres above the ground, 4.0 metres from the two figures, level.
Two people in matt grey surface suits with clear visors stand on flat dark rock
under a plain sky. The one on frame left holds out a closed fist; the one on frame
right opens a gloved hand under it. At about four seconds the left hand opens and a
small metal object drops into the right palm, which closes around it. Both then
lower their arms. They are clearly two different people: different heights, different
suit wear, different postures; the one on frame left is a head taller and stands
square, the one on frame right is shorter and stands with weight on one leg. Their
faces are different from each other.
Everything moves at normal speed. No slow motion. No camera movement.
No dialogue. No text. No watermark. Photorealistic live-action cinematography.
```

```
HÜKÜM KURALI
  iki figür AYNI yüz         → D20 HÂLÂ DOĞRU · yasak kalır, gerekçelenir
  üçüncü figür belirdi       → D20 HÂLÂ DOĞRU
  iki AYRI insan, temiz      → ✅ D20 DARALTILIR: "kaza eseri klon" yasağı
                               kalır, "ikinci insan tasarlanamaz" DÜŞER
  el teması eriyor           → AYRI bulgu [D24], D20'yi ilgilendirmez
```

## PROB B — TEK REPLİK (D35 sınanıyor)

> Sorduğu tek soru: **model, D35'in KENDİ reçetesiyle yazılmış tek bir
> kısa repliği dudak senkronuyla üretebiliyor mu?**
> (reçete: orta yakın çekim + replik 3 saniyenin altında)

```
Vertical 9:16. Single continuous shot, 0 cuts, 10 seconds. Lens: 50mm spherical,
fixed tripod, medium close shot, chest and head in frame, level, 2.0 metres away.
A person in a matt grey surface suit with a clear visor looks slightly off-lens.
At three seconds they say, in Turkish: "Duyuyor musun?" — a single short line, two
words, spoken once. Their mouth is closed before the line and closed after it, and
the lip movements match the words exactly. Nothing else moves in the frame.
Everything moves at normal speed. No slow motion. No camera movement.
No subtitles. No text. No watermark. Photorealistic live-action cinematography.
```

```
HÜKÜM KURALI
  ses kanalı yok             → 🔴 replik hiç üretilmedi · D35 HÂLÂ DOĞRU
  ağız replikten SONRA oynar → 🔴 D35 HÂLÂ DOĞRU (YDIF penceresi dışında yüksek)
  ses var, ağız düz          → 🔴 D35 HÂLÂ DOĞRU
  YDIF tepesi konuşmayla     → ✅ D35 GEVŞETİLİR: kısa replik + orta yakın
    örtüşüyor ve ağız                çekim serbest; uzun replik ve geniş
    öncesi/sonrası kapalı            çekim yasağı KALIR
  altyazı belirdi            → AYRI bulgu [D45]
```

---

# 3. SONUÇ TABLOSU — koşulduğunda doldurulur

```
KOŞU TARİHİ:  ____________        MODEL/ARAÇ: ____________
```

| Ölçüm | PROB A | PROB B | Kaynak |
|---|---|---|---|
| süre (s) | | | `prob_olcum.sh ①` |
| çözünürlük | | | ① |
| kesme sayısı [D1] | | | ② |
| ses kanalı | — | | ③ |
| entegre gürlük (LUFS) | — | | ③ |
| ⬜ iki AYRI insan mı | | — | kare · göz |
| ⬜ üçüncü figür | | — | kare · göz |
| ⬜ el teması rijit mi [D24] | | — | kare · göz |
| YDIF ↔ konuşma penceresi | — | | ④ |
| ⬜ ağız öncesi/sonrası kapalı | — | | kare · göz |
| ⬜ metin/altyazı [D45] | | | ⑤ |

```
HÜKÜM A:  □ D20 HÂLÂ DOĞRU   □ D20 DARALTILIR   □ POLİTİKA REDDİ
HÜKÜM B:  □ D35 HÂLÂ DOĞRU   □ D35 GEVŞETİLİR   □ POLİTİKA REDDİ

BUNDAN SONRA NE OLUR:
  A daraltılırsa → negatif çekirdeğin "Exactly one human character"
                   satırı KOŞULA bağlanır: tek insanlı filmde kalır,
                   iki insanlı filmde "exactly two, described separately"
                   olur. KILAVUZ_REHBERI §5 + §4.1 birlikte güncellenir
                   [kart H]. YERCEKIMI'nin 39 promptu doğrulanmış olur.
  B gevşetilirse → Kart 7'nin "EN GÜVENLİ: sessiz film" tavsiyesi
                   "kısa replik + orta yakın çekim serbest" olur;
                   dikey hat 18 filmdir kullanmadığı kanalı kazanır.
  İkisi de tutarsa → yasaklar KALIR ama artık GEREKÇELİDİR ve tarihi
                   30.08.2026'dır. 05'in §3 teşhisi geçerliliğini
                   korur; çözüm ①②③⑥'ya (yasak değiştirmeyenlere) düşer.
```

---

# 4. ÖLÇÜM BETİĞİ — doğrulama kaydı (30.08.2026)

`prob_olcum.sh` yazıldığı gün **gerçek bir master üstünde** koşuldu
(`~/Downloads/the thın roof.mp4`) ve çıktısı film kaydıyla karşılaştırıldı:

| Betiğin okuduğu | Film kaydındaki değer | Sonuç |
|---|---|---|
| 65,030 s · 720×1280 · 30 fps | aynı | ✅ |
| ses VAR · **−17,3 LUFS** · tepe −0,9 dBFS | aynı | ✅ |
| sessizlik aralığı yok | *"tek aralık yok"* | ✅ |
| **6 kesme** (10,03 … **60,03**) | altı QA merceği **5** saymıştı | ⭐ betik daha doğru |

⭐ **Son satır kayda değer:** altı mercek son kesmeyi (60,033 — başlık
kartının başladığı yer) saymamıştı; betik saydı. Yani bu harness,
teslim kapısının bugünkü hâlinden **kesme sayımında daha güvenilirdir**
ve PROB dışında da kullanılabilir.

⚠️ **Betiğin bilinen sınırı — dürüst kayıt:** makinede `numpy`, `PIL`,
`cv2` YOK. Bu yüzden **insan sayımı makineyle yapılamıyor**; betik
yalnız bakılacak kareyi hazırlıyor. "İki figür aynı yüz mü" sorusu
insan gözüne kalıyor ve bu, bu koşunun tek ölçülemeyen yeridir.

---

# 5. 🆕 TUR 11 PROBLARI — iki ucuz A/B (04.09.2026)

> **Neden burada:** TUR 11'in dördüncü raporu deponun beş zorunlu bloğu
> için "SİLİNEBİLİR" hükmü verdi ve hükümlerini "Ölçülmüş Etkisi"
> başlığıyla sundu. Denetimde beşi için de ablation bulunmadı — beş karar
> da ÖNERİ çıktı. Aşağıdaki iki prob, o hükümlerden deponun kendi
> parasıyla sınayabileceği ikisini kapatır.
> Kayıt: `04_ARASTIRMA_BULGULARI.md` §TUR 11 · T11.4.
>
> ⛔ İkisi de A/B'dir: **tek değişken, aynı tohum, aynı sahne.** Prob
> yeni bir film DEĞİLDİR; mevcut bir filmin tek sahnesi iki kez üretilir.

## PROB C — "35mm film grain" var / yok

```
SORU     Negatif çekirdeğin kapanış cümlesi ("Photorealistic with 35mm
         film grain") sabit planda TİTREME üretiyor mu?

GEREKÇE  Deponun bu konuda HİÇ ölçümü yok. Mekanizma doğrulandı
         (3D nedensel VAE sıkıştırması → yüksek frekanslı ince detay
         kodlamada kayboluyor; sıkıştırma oranları ve kaynak tek yerde:
         `../KILAVUZ_REHBERI.md` §5④), ETKİ doğrulanmadı.

DEĞİŞKEN Tek kelime öbeği: cümlenin son beş kelimesi var / yok.
         Başka HİÇBİR şey değişmez.

ÖRNEKLEM Aynı sahne, aynı tohum, 2 × 5 klip = 10 üretim.
         Sahne seçimi: içinde ince çizgi ya da tekrar eden birim OLAN
         bir sahne (korkuluk, ızgara, çit, panel dizisi) — çünkü
         mekanizma tam orada iş görecek.

ÖLÇÜT    ① Ardışık kareler arası fark: iki klipte de sabit bölge
           (arka plan paneli) seçilip kare-kare piksel farkı toplanır.
           `prob_olcum.sh` kare çıkarabiliyor; fark toplamı ffmpeg ile
           alınır. Gren varsa fark toplamı ANLAMLI ölçüde yüksek olmalı.
         ② Göz: 10 klip karıştırılıp körlemesine izlenir, "hangisinde
           yüzey kaynıyor" diye işaretlenir.
         ③ Doku kaybı karşı kontrolü: grensiz klipte cilt gözeneği ve
           kumaş dokusu KAYBOLDU mu — çünkü çekirdeğin gren cümlesi
           aynı zamanda bir DAMGA ÖNLEMİDİR [DIKEY §6.1(a): pürüzsüzlük
           "bu AI" suçlamasını tetikliyor].

KARAR    ①+② gren aleyhine VE ③ temiz çıkarsa satır silinir.
         ③ kirliyse satır KALIR — titreme bedeli, damga bedelinden ucuzdur.
         ⛔ Tek yönlü okuma yapılmaz: bu prob iki riski aynı anda tartar.
```

## PROB D — kilit konumu: ilk cümle mi, son çeyrek mi

```
SORU     Sahneye özel bir kilit promptun BAŞINDA mı daha iyi tutuyor,
         SONUNDA mı?

GEREKÇE  Ölçüldü (04.09.2026): depodaki zorunlu kilitlerin tamamı
         prompt gövdesinin son çeyreğinde duruyor — sayım ve yöntem
         `../KILAVUZ_REHBERI.md` §5②'de. Difüzyon
         kodlayıcılarında erken konumun daha güçlü bağladığı yönü
         ölçülmüştür; deponun kendi hattında sınanmadı.

DEĞİŞKEN Tek kilit cümlesinin YERİ. Metin birebir aynı, yalnız taşınıyor:
         A) gövdenin ilk cümlesi   B) mevcut yeri (son çeyrek)
         Kilit seçimi: o sahnede DÜŞMESİ ölçülebilen bir kilit —
         örn. düz sırt silüeti [D79/D139] ya da tek insan kilidi.

ÖRNEKLEM Aynı sahne, aynı tohum, 2 × 5 klip = 10 üretim.

ÖLÇÜT    Kilit tuttu mu / tutmadı mı — ikili sayım, 5'te kaç.
         Sayım gözle yapılır ve karar YAZILIR (D74: kaydı olmayan kapı
         koşulmamış kapıdır).

KARAR    A anlamlı biçimde üstünse IMAGE_VIDEO_PROMPT_TEMPLATES'e tek
         satır eklenir: "o sahnenin tutması gereken tek kilit ilk
         cümlededir." Fark yoksa mevcut sıra korunur ve bu kayda geçer.
```

```
⚠️ İKİSİNİN DE SINIRI: N=5 küçüktür ve tek sahnedir. Bu problar bir
   hükmü KANITLAMAZ; hangi yönde çalışılacağını söyler. Deponun kendi
   dürüstlük kuralı burada da geçerli — sonuç "ölçüldü" değil
   "bir sahnede şu çıktı" diye yazılır.
```
