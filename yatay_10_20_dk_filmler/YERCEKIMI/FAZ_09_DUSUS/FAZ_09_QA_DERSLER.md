# 📚 YERÇEKİMİ — FAZ 9 / DÜŞÜŞ · QA DERSLERİ VE AKSİYON

```
Koşu    06.09.2026 · Gemini · makara "faz 9.mp4" · 12 segment · 120 s · 11 kesme
Ham     ../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/
        02_HAM_RAPORLAR/YERCEKIMI/YERCEKIMI_FAZ09_12MERCEK_HAM.md
Defter  .../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/YERCEKIMI.md § KOŞU 9
Mod     ⚠️ V — SPEC yok [D129] · ÇIPLAK RUBRİK → T tablolarına GİREMEZ
Ölçüm   ⛔ ⑪ KOŞULMADI — sahip kararı: depo dışına çıkılmaz, master'a dokunulmaz
⛔ FAZ_09_QA_PROMPT.md YOK. Üretilmiş dokuz fazın TEK rubriksizi bu. Onun
   yerine `_KAYNAK/` altındaki ON İKİ genel mercek koşuldu.
   ⚠️ F8'de aynı karar alındı ve orada "YANLIŞ ALET" diye kaydedildi.
   → İKİNCİ VAKA, ardışık iki fazda, aynı gün → **[[D185]]**
Sisteme D185 · D186 · D187 · D129 TEKRAR 14 · D166 TEKRAR 2
```

---

# ✅ ÖNCE İYİ HABER — FAZ TAM TESLİM EDİLDİ

F8'in en pahalı bulgusu iki üretilmemiş sahneydi. **F9'da o hata YOK.**

```
① SAHNE SAYISI 12/12.  On iki merceğin on ikisi de "12 sahne · 11 kesme ·
   120 s" yazdı. Plan: S97-S108, 12 × 10,0 s = 120 s. TAM.
② ŞERİT PLANA BİREBİR OTURUYOR.  On iki raporun on ikisi de aynı diziyi
   bastı:
        1111111111-1
                  ↑ 11. hane
   Plan: **S107 PARAŞÜT ⭐ İNSANSIZ (KART 10)** — fazın tek insansız sahnesi
   11. sıradadır. Kurgu plan sırasındadır ve insansız sahne tam yerindedir.
③ ⑤ ÇAPRAZ SAYIM KAPISI DEPODA İLK KEZ SIFIR SAPMAYLA KAPANDI [D107].
   Kept Light'ta yayılım 24→20 idi; burada 12 mercek, tek sayı.
   ⭐ Sebep aday: 10 s ızgarası artık kesme dedektörü için de okunaklı —
     F7 ölçümünde doğrulanan ızgara (12 segment · 10,0 s) burada kendini
     on iki bağımsız okumada tekrar gösterdi.
④ LOCKOFF 12/12 (⑨) · klip içi ışık değişimi 0/12 (⑪) · in-clip movement 0.
   KİLİT 45'in "kamera asla sallanmaz" kuralı ekranda TUTUYOR.
```

---

# 🔴🔴 BİRİNCİ BULGU — FİLMİN ADINI TAŞIYAN KARE HİÇBİR RAPORDA YOK

S102 **YERÇEKİMİ YAĞMURU** bu fazın imza çekimidir ve dosyanın kendi başlığı
şunu diyor: *"Filmin adını taşıyan kare."* KİLİT 43:

> yerçekimi bir KUVVET olarak gösterilmez, bir SONUÇ olarak gösterilir —
> kadrajdaki her serbest nesne AYNI ANDA ve AYNI YÖNE düşer.

**On iki rapor S102'yi (0:50-1:00) gördü. On ikisi de başka bir şey gördü:**

```
⑥ FİZİK      "steam vents vertically downward" → ve fazın konusunu
              🔴 TWO GRAVITIES ilan etti
⑤ ARKA PLAN  "woman in spacesuit venting steam"
⑧ EFOR       E1 "survive cabin steam/gas venting" — çevresel maruz kalma
③ SES        "heavy steam/smoke drops with no hiss or vent"
⑫ HOOK       "smoke fills the red-lit cabin"
④ HİKAYE     "Escalation — Good visual change (steam, gravity)"
⑩ OYUNCULUK  "She endures a catastrophic event with catatonic shock."
① KARE       S102 hakkında tek bulgu YOK
```

⛔ **Altı mercek DÜŞEN TOZ PERDESİNİ "buhar/gaz kaçağı" diye okudu.**
Plan: *"The dust comes down as a thin curtain and does not hover… Sıvı yok,
damla yok, ter yok. Düşen her şey KURU katıdır."*

⭐ **VE ④'ÜN ÖNERME SORUSU BUNU ÖLÇTÜ:** rubrik "bu dünya hangi kural üzerine
kurulu?" diye sorar. ④'ün cevabı:

> *"An astronaut sits in a capsule during a turbulent re-entry, passes out,
> and wakes up safely on the ground."*

**Cümlede yerçekimi yok.** On iki raporun on ikisinde de "yerçekimi geri
geliyor ve her şey aynı anda düşüyor" cümlesi geçmiyor. Filmin novumu
ekrana ULAŞMADI — ya da ulaştı ve on iki mercek onu buhar sandı. İkisi de
S102'nin yeniden üretilmesini gerektirir ve ikisinin ayrımı TEK KAREYLE
çözülür (0:52 · toz mu duman mı).

---

# 🔴🔴 İKİNCİ BULGU — ÜÇ KİLİT KUSUR YAZILDI, ÜÇÜ DE PLANDA YAZILI

⑩ ÖNERME KAPISI'nın bu depoda gördüğü en ağır vaka.

## ① ⑥ FİZİK · "TWO GRAVITIES" — fazın KONUSUNU kusur yazdı

`00_PLAN.md` SAYISAL KİLİTLER, kelimesi kelimesine:

```
YERÇEKİMİ   ...
            F9: ivme rampası (nesneler kabin kıçına doğru "düşer")
            F10: 1g — toz hızlı çöker, gölgeler normal
```

**FAZ 9 İVME RAMPASIDIR.** Yerçekimi bu fazda değişmek ZORUNDADIR; fazın
adı DÜŞÜŞ'tür ve rampa fazın kendisidir.

⑥ iki ölçüm yaptı:

```
L4  0:52  g ≈ 0,1 m/s²   (S102 · rampanın BAŞI)
L7  1:51  g ≈ 3,2 m/s²   (S108 · rampanın SONU)
```

⭐ **Bu iki sayı rampanın İKİ UCUDUR ve fazın ÇALIŞTIĞININ kanıtıdır.**
⑥ veriyi doğru topladı, sonucu ters çevirdi ve reçeteyi yazdı:

> *"Regenerate Scene 6 falls to match Scene 12's gravity, **or crop the
> objects out**."*

⛔ **Kadrajdan kırpılması önerilen "objects", filmin adını taşıyan olayın
kendisidir.** Bulgu ⑩'da DÜŞER; üç kategorinin puanı geri verilir.

⛔ Ve ⑥'nın **kendi STEP 0 kapısı bunu söylüyordu**:
> *"if the film has a central behaviour you scored as its worst defect, and
> your register is empty, you have almost certainly scored the film's premise."*

⑥ `PREMISE REGISTER: none` yazdı, sonra filmin önermesini en ağır kusuru
ilan etti. **Kapı rubriğin içindeydi ve ateşlemedi** → D166 TEKRAR 2.

## ② ⑪ IŞIK · renk takvimini "şiddetli sürüklenme" yazdı

KİLİT 44: atmosfere giriş ateşle değil, **RENKLE** anlatılır —
`beyaz → turuncu → kızıl → beyaz → mavi`.

⑪'in gözlemi: `Neutral → Amber → Neutral → Red → Cool`.
**Takvimin ta kendisi**, doğru sırayla okunmuş. Puanı: **3/10**, kategorinin
en düşüğü, "severe and constant drift". Üç 🔴'sının ikisi renk geçişi.

⭐ ⑪ aynı raporda `In-Clip Stability 10/10` ve `Atmosphere Honesty 10/10`
verdi — yani klip İÇİNDE ışık hiç oynamıyor, kaçak parlama yok. Bu ikisi
KİLİT 44'ün "renk camın İÇİNDEDİR, kabine huzme olarak girmez" kuralının
TUTTUĞUNU gösteriyor. Rapor kilidi hem doğruladı hem cezalandırdı.

## ③ ② DEVAMLILIK · kırmızı ışığı koltuk rengi sandı

🔴 BLOCKER: *"2 red seats vs 3 white seats"* (0:50 ↔ 1:30).
S102 kabini KIZIL ışıkla yıkanır (KİLİT 44), S105-S106'da ışık beyaza ve
maviye döner. **Aynı koltuklar, iki ayrı ışık.** ⑤ ARKA PLAN aynı koltukları
bağımsız olarak "2 red empty seats" (S6) ve "2 empty white seats" (S10) diye
saydı — sayı ikisinde de 2, yalnız renk değişti.

⛔ ②'nin 🔴'sı DÜŞER. ⚠️ AMA ALTINDA AÇIK BİR MADDE KALIYOR: ⑤ S12'de
"1 empty white seat right" yazdı. Koltuk sayısı 3 sabittir. **S108'de bir
koltuk kadrajdan mı çıktı, yoksa gerçekten kayıp mı — kareyle çözülür.**

---

# 🔴🔴 ÜÇÜNCÜ BULGU — AĞIRLIĞIN ÜÇ KANITI: 0/3 ÖLÇÜLDÜ

KİLİT 46, fazın en ucuz ve en kesin göstergesi:

```
① SAÇ    101 sahnedir havadaydı; S102'den itibaren başa yapışık.
② SAAT KAYIŞININ SERBEST UCU  filmin başından beri bilekten birkaç mm
         havadaydı (S8 · S30 · S70); S103'te ilk kez AŞAĞI SARKAR.
③ KOLLAR nötr 0g duruşuna bir daha yükselmez.
```

**On iki mercek, üç kanıt, sıfır ölçüm.**

```
SAÇ    ⑥ FİZİK ledger L1'de yazdı: "woman's hair floats in cabin"
       (0:00-0:10, S97) — ve BİR DAHA hiç bakmadı. Düştü mü, düşmedi mi:
       on iki raporda cevap YOK. ② DEVAMLILIK pasaportuna saçı yazdı
       ("short dark brown chin-length bob") ve yalnız RENK/BOY izledi.
KAYIŞ  S103 = SARKAN KAYIŞ. Sahnenin adı budur ve sahnenin işi budur.
       ⑩ o sahneyi "She calmly assesses her remaining time" diye okudu;
       ① aynı saniyede kaynaşmış parmak buldu. Kayışın ucu hakkında
       tek satır yok.
KOLLAR ⑩ "posture" kanalını kayıtlı tuttu, kolların YÜKSELİP yükselmediğini
       hiç sormadı.
```

⛔ **KÖK SEBEP — bu üç kanıt hiçbir merceğin kapsamına düşmüyor.**

```
saç bir ARTEFAKT değil        → ① değil
saç ÖZNE-DIŞI alan değil      → ⑤ değil
saç bir SAYI taşımıyor        → ⑥ değil  (⑥ ancak "düşme süresi" ölçebilirdi)
saç bir BEAT değil            → ⑦ değil
saç bir BEDEL değil           → ⑧ değil
saç KAMERA değil              → ⑨ değil
saç bir NİYET değil           → ⑩ değil
saç IŞIK değil                → ⑪ değil
saç "aynı mı" sorusudur       → ② olmalıydı, ama ② saçı KİMLİK olarak
                                izler (renk/boy/ayrım), DURUM olarak değil
```

⭐ **DERS:** plan bir kilidi "filmin en ucuz ve en kesin göstergesi" diye
işaretliyorsa, o göstergeyi ölçecek merceğin ADI da kilidin yanına yazılmalı.
Yazılmazsa gösterge on iki merceğin arasından düşer → **[[D187]]**

---

# 🔴 DÖRDÜNCÜ BULGU — ORTA FAZ, BAĞIMSIZ KISA FİLM SANILDI

FAZ 9 = **16:00 – 18:00**, 20 dakikalık filmin %80–90 bandı. Perde III.

④ HİKAYE ve ⑫ HOOK bunu bir kısa film sanarak puanladı:

```
④  Hook 4/10 · Yapı 4/10 · Final 5/10 · Tutundurma 4/10 → 4,0/10
    VERDICT: REVISE STRUCTURE
    "0:00-0:40 · Delayed Start — 40 saniye boyunca hiçbir şey riskte değil"
    Kesme listesi: S99 · S100 · S103 → kalan süre 90 s
⑫  VERDICT: HOOK MISSING · "NO QUESTION"
    "The first 40 seconds are pure establishing atmosphere."
    Reçete: "opening on S5 slamming straight into S6, then use S1 as a
             flashback"
```

⛔ **Dördü de bir ORTA FAZDA ÖLÇÜLEMEZ.** Hook 16 dakika önce atıldı
(F1); final F10'dadır; tutundurma eğrisi 20 dakikanın eğrisidir. ⑫'nin
üç saniyelik terk tahmini (0:10 · 0:25 · 0:35) **16:10 · 16:25 · 16:35**
demektir ve o saniyelerde izleyici zaten 16 dakikadır içerideydi.

⛔ Ve iki reçete de filmin omurgasını keser:
```
④ S99 KOLÇAK "cut"      → ⑤ ARKA PLAN'ın tek kaya kanıtı orada
④ S100 ASILI "cut"      → S102'nin KURULUMU: nesneler ancak ASILI oldukları
                          için DÜŞEBİLİR. Kurulum kesilirse imza çekim
                          neyin değiştiğini gösteremez.
⑫ "S1'i flashback yap"  → S97 UFUK DÜZLEŞİR fazın giriş bağlantısıdır;
                          F8'in son karesine bağlanır.
```

⚠️ ⑫'nin ölçtüğü **KAPAK SANİYESİ 9/10** ve **paylaşım anları 8/10** ise
faz ölçeğinde geçerli kalır — bir klip tek başına seyahat eder, filmin
neresinde durduğundan bağımsız. Bu iki hücre KURTARILIR; kalan altısı düşer.

→ **[[D185]]**

---

# 🟠 BEŞİNCİ BULGU — "KUSUR YOK" 7/10 YAZILDI

⑤ ve ⑨, kaynağı olmayan hücrelere 7/10 verdi:

```
⑤ ARKA PLAN   5 hücre · issue cell birebir "none"
              Horizon 7 · Depth 7 · Focus 7 · Sky 7 · Edges 7
⑨ KADRAJ      3 hücre · "flawless lockoffs mapped to 7" ·
              "no distinct returns attempted/failed" ·
              "geometry stable mapped to 7"
```

⭐ **Betik koştu ve sayıyı verdi** (`rapor_kontrol.py` ①.5 · D186 kapısı,
06.09.2026'da yazıldı):

```
⑤ ARKA PLAN   yazılan 6,5  →  düzeltilmiş 4,0   (n=6 → n=1)
⑨ KADRAJ      yazılan 5,8  →  düzeltilmiş ~4-5  (n=5 → n=1-2)
```

⛔ Düzeltme 9,0'a DEĞİL 4,0'a gidiyor, ve sebebi D131'dir: kaynağı olmayan
hücre 10/10 değil `—`'dir, ortalamaya HİÇ girmez. Yani **⑤ bu makarada tek
bir şey ölçtü** (kapsül topolojisi, 4/10); kalan sekiz kategorisi ya N/A ya
ölçülmemiş. 6,5'lik "orta karar" bir ölçüm değil, dokuz kategorilik bir
formun doldurulmuş hâliydi.

⛔ İki rubrikte de kural ④ YAZILI: *"A category with material but no
in-scope source keeps 10/10… Absence of evidence is not evidence of
perfection."* Yani "kusur bulamadım" ya `10/10`'dur ya `—`. **7/10 bir
model refleksidir: ortalamaya dönüş.**

⭐ Bedeli iki yönlü: ① temiz eksen cezalandırıldı (kusurlu eksen değil) —
bir sonraki üretim "arka planı düzelt" der, oysa arka planda düzeltilecek bir
şey yoktu; ② ve daha pahalısı, **7/10 bir ölçüm YAPILDIĞINI iddia eder.**
Gerçekte ⑤ dokuz kategorinin sekizinde hiçbir şey ölçmedi ve rapor bunu
"orta" diye yazdı. → **[[D186]]**

---

# ✅ SAĞLAM BULGULAR — bunlar kapıdan geçti, üretime gider

Kilit düşmesinden ve kapsam hatasından SONRA ayakta kalanlar:

```
🔴 S99 KOLÇAK · 0:20-0:30 — ELİN SAHİBİ YANLIŞ
   ② : "hairy, veiny male hand", kadınla aynı kesmede.
   Kadro A tek kişidir ve kadındır. → S99 YENİDEN ÜRETİLİR.
   ⚠️ ④ bu sahneyi "cut" diye önerdi; sahne kesilmez, ELİ düzeltilir.

🔴 S103 SARKAN KAYIŞ · 1:01 — KAYNAŞMIŞ PARMAK
   ① : "right hand lacks distinct fingers, fused into a single fleshy mass".
   Sahnenin konusu bir EL ve bir KAYIŞTIR. → YENİDEN ÜRETİLİR.

🔴 S100 ASILI · 0:35 — KALEM LASTİK GİBİ BÜKÜLÜYOR
   ① : "the floating metal pen bends entirely in half like rubber".
   S102'de aynı kalem "yarım saniyede kadraj yüksekliğini geçip tabana
   çarpacak" KATI bir cisimdir. Bükülen kalem imza çekimi çürütür.
   → YENİDEN ÜRETİLİR.

🔴 S107 PARAŞÜT · 1:45 — İPLER KOPUYOR
   ① : "parachute lines phase out of existence and disconnect mid-air".
   Fazın tek insansız sahnesi ve KART 10 sahnesi. → YENİDEN ÜRETİLİR.

🔴 S108 · 1:51 — KAYIŞ OMUZDAN GEÇİYOR
   ① : "harness strap clips cleanly through the shoulder".
   Faz kapanış sahnesi. → YENİDEN ÜRETİLİR.

🔴 S102 · İNSAN DÜŞMÜYOR  ⭐ EN PAHALISI
   ⑩ : "the body is entirely static while smoke billows" (🟠 MANNEQUIN)
   ⑧ : E2'de "no chest heave, zero visible breathing"
   KİLİT 43: "⛔ İNSAN DA DÜŞER: omuzlar koltuğa çöker, kollar kolçaklara
   iner, ve SAÇ DÜŞER."
   ⑩ kilidi bilmeden semptomu buldu: yağmurun insan yarısı ekranda YOK.
   → S102 YENİDEN ÜRETİLİR (8 varyasyon zaten bütçeli).

🟠 S102 SESİ YOK
   ③ : "Missing Environmental SFX (0:50) — heavy steam/smoke drops with no
   hiss or vent." Prompt: "the small hard knock of the pen at 2 seconds and
   a scatter of tiny impacts as the dust lands."
   → kurgu masası işi, yeniden üretim değil.

🟠 HER KESMEDE AMBİYANS DELİĞİ
   ③ : 11 kesmenin 11'inde yatak inceliyor (mutlak sessizlik DEĞİL —
   raporun kendi kaydı "floor still present"). → sürekli oda tonu serilir.

⬜ AÇIK · S108'de koltuk sayısı
   ⑤ "1 empty white seat right" ↔ sabit 3 koltuk. Kareyle kapanır.
⬜ AÇIK · alındaki kesik 1:00-1:10'da yok (②)
   Planda yıpranma haritası var mı — belgeye sorulur.
```

---

# 🔧 AKSİYON LİSTESİ

## 🔴 KUŞAK 1 — F9 KAPANMADAN

```
□ FAZ_09_QA_PROMPT.md YAZILACAK — dokuz fazın tek eksiği. Yazılmadan
  F9 yeniden denetlenmez [D185].
□ S102 yeniden üretim (8 varyasyon bütçeli): insan düşer + saç düşer +
  toz KURU okunur. Kabul kapısı: tek karede (0:52) toz mu duman mı.
□ S99 · S100 · S103 · S107 · S108 yeniden üretim (yukarıdaki beş 🔴).
□ KİLİT 46'nın üç kanıtına MERCEK ADI yazılacak (saç · kayış ucu · kollar)
  — hangisi hangi mercekte ölçülür, kilidin yanında dursun [D187].
```

## 🟠 KUŞAK 2 — KURGU MASASI

```
□ sürekli oda tonu · S102 toz/kalem foley'i · S107→S108 geçiş ambiyansı
```

## 🟡 KUŞAK 3 — UYGULANMAYACAK OLANLAR (gerekçesiyle)

```
⛔ ⑥'nın "crop the objects out" reçetesi — filmin adını taşıyan olay
⛔ ⑪'in "regenerate S10 to carry the red light" — KİLİT 44 kırmızıyı
   S105'te bitirir; kırmızının gitmesi PLANDIR
⛔ ④'ün kesme listesi (S99 · S100 · S103) — üçü de yük taşıyor
⛔ ⑫'nin "S1'i flashback yap" reçetesi — faz giriş bağlantısı
⛔ ②'nin "2 red vs 3 white seats" 🔴'sı — ışık takvimi
```
