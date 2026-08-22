# 📐 AÇI YAYI VE SEKANS KILAVUZU — Açının Film Boyunca Dizilişi

> **Neden var (22.08.2026):** `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` tek
> çekimin anlamını verir; sahneden sahneye açı/ölçek DİZİLİŞİNİN kuralı
> hiçbir dosyada yoktu. `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §2 örüntü
> kırıcı "ardışık iki sahne aynı ölçek + palet + ses dokusunda olamaz"
> der — bu dosya o kapının açı/ölçek tarafını SAYISAL banda bağlar ve
> yay şablonları verir. Kaynak: `araştırmalar/12.md` (22.08.2026).
>
> **Ne zaman okunur:** sahne haritası yazılırken — vuruş tablosu + tema
> belli olduktan sonra, kamera satırları TOPLUCA dizilirken. Tek sahnenin
> açı anlamı için önce kardeş dosya okunur.

---

# 1. 🎢 AÇI YAYI NEDİR

Açı yayı = açı ve ölçek seçimlerinin film boyunca, karakterin psikolojik
eğrisine paralel bir EĞRİ çizecek şekilde dizilmesi. Temel mekanizma
görsel yoğunluk ilkesidir:

```
AFİNİTE   ardışık planlar BENZER → yoğunluk düşer → dinginlik, rutin, güven
KONTRAST  ardışık planlar ZIT    → yoğunluk artar → gerilim, şok, çatışma
```

Lockoff kamerada pan/tilt/zoom sıfır → **görsel yoğunluğun tek kaynağı,
plandan plana açı/ölçek zıtlığıdır.** Yay, bu zıtlıkların tema eğrisine
göre bilinçli dizilişidir; dizilmezse film ya güvenlik kamerası kaydına
(hep afinite) ya rastgele klip yığınına (hep kontrast) döner (§4).

---

# 2. 🎬 ÜÇ USTA HARİTASI — belgelenmiş yay kalıpları

```
GÜÇ YAYI (Citizen Kane)
  Karakter güçlendikçe kamera ALÇALIR (alt açı tırmanışı); kadraja giren
  tavanlar gücü aynı anda HAPSE çevirir. Çöküşte tersine döner: geniş
  açı + derin odak, karakter arka planda küçülür (para sayılırken Kane
  uzamda silinir).
  → bizim karşılık: kontrol/tamir/karar anlarında kademeli alçalan
    kamera; tehdit girdiği an ani yüksek + geniş sıçrama.

İZOLASYON YAYI (Blade Runner 2049)
  Üst açı + extreme wide + negatif alan + katmanlı ön plan (silüet, cam,
  engel); karakter kadrajın küçük bir parçası. İç dünya mimikle değil,
  ezici mimari + sis + monokrom paletle dışa vurulur.
  → yalnızlık temasının açı ekonomisi (§5).

AYIRMA / SEPARATION (2001: A Space Odyssey)
  İki özne aynı kadrajda DEĞİL; ardışık tekli sabit çekimlerde
  (A-B-A-B). Kesin mekânsal ayrım = psikolojik mesafe, iletişimsizlik.
  → bizim karşılık: karakter (A) / baktığı nesne-makine-gölge (B)
    ardışık tekli bloklar. Tek kadraja iki varlık sıkıştırmaktan hem
    daha güçlü hem Veo halüsinasyon riski daha düşük.
```

---

# 3. ⚡ 30 DERECE KURALININ AI KARŞILIĞI — kopukluk bir kalkandır

Klasik kural (ardışık iki çekim arası en az 30° fark) jump-cut önlemek
içindi. Bağımsız üretilen bloklarda durum TERSİNE döner: model her
prompta karakteri/mekânı yeniden yorumlar; iki çekim birbirine ne kadar
BENZERSE, mikro farklar (vizör yansıması, kırışıklık, arka plan dokusu)
o kadar görünür olur ve "yapay zekâ halüsinasyonu ifşası" okunur.

```
ÖLÇEK MERDİVENİ: EWS – WS – MS – CU – ECU   (1 kademe = komşu basamak)

✅ GÜVENLİ BANT — ardışık iki sahne arasında ZORUNLU sıçrama:
   ölçekte EN AZ 1 TAM KADEME  VE  açıda EN AZ 45°
   (örn. göz hizası MS → alt açı CU · cephe WS → tam profil MS)
   İzleyici radikal değişimi sindirirken mikro farkları arayacak
   bilişsel boşluğu bulamaz — süreklilik YANILSAMASI böyle kurulur.

⚡ ŞOK BANDI (smash cut) — ölçekte 2+ kademe (örn. EWS → ECU):
   şiddetli yönelim kırılması üretir; YALNIZ kırılma anına saklanır
   (zihinsel kopuş, ani tehdit, kozmik keşif). Filmde EN FAZLA 1-2 kez.

🔁 TEKRAR (recurrence) SERBEST:
   daha önce tanıtılmış kurulumun AYNISINA dönmek (A-B-A) sıçrama
   sayılmaz — iskelet kurar, "bildik konuma dönüş" rahatlığı verir.
   Şart: araya farklı kurulum girmiş olmalı; aynı kurulum ARKA ARKAYA
   gelemez [örüntü kırıcı — KURGU_RITMI §2].

⚠️ Sıçrama EKRAN YÖNÜNÜ ÇEVİREMEZ: açı değişir, coğrafya değişmez.
   Hedef-dilim, omuz hattı ve yön kilitleri aynen korunur —
   UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md.
```

---

# 4. 🔢 ÇEŞİTLİLİK BANDI — monotonluk ile dağınıklık arası

"Kurulum" = açı + ölçek + kamera konumu üçlüsü. Sayı bandı:

```
 6 sahnelik film    EN AZ 3 farklı kurulum
                    altı → güvenlik kamerası hissi, ritim ölür
12 sahnelik film    EN FAZLA 5-6 farklı kurulum
                    üstü → mekânsal algı çöker, "rastgele üretilmiş
                    bağımsız AI klipleri" hissi
kalan sahneler      tanıtılmış kurulumların TEKRARI (A-B-A-B · A-B-C-A)
                    → iskelet + Veo çıktısında tutarlılık şansı
```

Daha uzun formatta (12-18 sahne, 2-4 dk) oran korunur: kurulum sayısı
sahne sayısının yarısını geçmez (bant çıkarımı — iki sabit nokta 6→3 ve
12→5-6'dan; sapılacaksa plana tek satır gerekçe [D74]).

---

# 5. 🗺️ TEMA → YAY EŞLEMESİ

Tema seçimi ve motifleri `TEMA_MUHENDISLIGI_KILAVUZU.md`'de; yay karşılığı:

```
YALNIZLIK → GENİŞ + ÜST AÇI EKONOMİSİ
  EWS / kuşbakışı ağırlıklı iskelet; karakter kadrajın ≤%10'u; yakın
  çekim seyrek ve kısa. Sabit kameranın kımıltısızlığı burada anlam
  üretir: evren karakterin varlığına KAYITSIZDIR (üçüncü derece etki).

TEHDİT / GÜÇ TIRMANIŞI → ALT AÇI MERDİVENİ
  Göz hizasından adım adım aşağı inen kurulum dizisi.
  ⚠️ Kasklı karakterde güçlenme = insanlıktan çıkma: alt açı tırmanışı
  empati bağını KOPARIR (mit/makine algısı). Bunu bilinçli kullan —
  final canavarlaşması, mitleşme. Kurban perspektifi isteniyorsa alt
  açı KARAKTERE değil tehdide verilir, kamera kurbanın yanına konur.

UMUT → KARANLIK-DARDAN TEK IŞIKLI GENİŞE
  Dar/karanlık kurulumlarla başlar, finalde tek sıcak ışıklı geniş
  kuruluma AÇILIR — yay finalde çözülür (tema kılavuzu §5-6 payoff'u
  ile aynı blokta).
```

---

# 6. 📱 FORMAT FARKI — yatay derinlik, dikey yükseklik

| Kriter | Yatay 16:9 (1-5 dk) | Dikey 9:16 (30-60 s) |
|---|---|---|
| Görsel alan | Doğal periferik görüş, çevresel detay | Klostrofobik, bağlamı dışlayan dikey şerit |
| Psikolojik yay ekseni | Z ekseni (derinlik): arka plana ilerleme/yaklaşma | Y ekseni (yükseklik): ezilme/yükselme |
| En etkili geniş açı | EWS — ufuk çizgisi + üçte bir kuralı çalışır | Tepe/kuşbakışı — EWS dikeyde silinir |
| Yakın çekim gücü | OTS ve profil MS geçişleri pürüzsüz | ECU kadrajı tamamen doldurur, ezici yoğunluk |
| Kompozisyon kuralı | Negatif alan YANAL bırakılır, karakter boşluğa bakar | Simetri + merkezleme zorunlu; negatif alan baş üstünde |

---

# 7. ⛓️ PROMPT ZİNCİRİ DİSİPLİNİ — yay bağımsız bloklarda nasıl korunur

```
KATMAN SIRASI (her prompt):  [KAMERA] [ÖZNE] [AKSİYON] [ORTAM] [STİL/SES]

① Sahneden sahneye YALNIZ [KAMERA] katmanı değişir.
② [ÖZNE] çıpası kelimesi kelimesine SABİT — her sahnede aynen kopyalanır
   (karakter çıpalama: SAHNE_DEVAMLILIK_KILAVUZU.md). Örnek çıpa:
   "lone explorer wearing an off-white rugged techwear suit, featureless
    gold heat-reflective full-face visor, amber palm accents"
③ [ORTAM] ve [STİL] blokları da sabit kalır — model aynı ışığı, aynı
   mekânı yalnız farklı kadrajdan render etmeye ZORLANIR.
④ Statik emir seti tam yazılır: "Static shot, locked-off camera,
   absolute zero camera movement." — tek "static" kelimesi yetmez.
⑤ Pozitif sınırlama negatiften güvenilirdir: "lone subject", "empty
   environment" ("no people" tersine tepebilir; yasağın kendisi
   negatif çekirdekte zaten var).
```

Üç sahnelik örnek zincir (yalnız [KAMERA] değişiyor):

```
S1  [Static extreme wide shot, high angle bird's-eye view, locked-off camera.]  + çıpa + ortam + stil
S2  [Static medium shot, eye-level, rule of thirds, static frame.]              + çıpa + ortam + stil
S3  [Static extreme close-up on the gold visor, macro lens, shallow depth of field, static frame.] + çıpa + ortam + stil
```

---

# 8. 📋 HAZIR DİZİLİM ŞABLONLARI

Şablonlar İSKELETTİR: kamera katmanları kendi vuruş tablona göre yeniden
türetilir, sahne süreleri format kartından gelir (KILAVUZ_REHBERI §2).

## 8.1 Dikey 6 sahne — "yalnızlıktan keşfe" (A-B-C-B-D-A)

| S | Kamera katmanı | Psikolojik hedef | Yoğunluk hamlesi |
|---|---|---|---|
| 1 (A) | Static overhead shot, extreme high angle looking directly down | Çevre karakteri ezer; varoluşsal hiçlik | Nötr açılış — izleyici coğrafyayı kavrar |
| 2 (B) | Static medium full shot, ground level, low angle looking slightly up | Dikey silüetle tanışma; statik duruşun tekinsizliği | Keskin sıçrama (45°+): üstten alta — AI farklarını gizler |
| 3 (C) | Static extreme close-up on visor, shallow depth of field | Vizör yansımasından dünyayı okuma | Ani izolasyon: mekândan kopuş, klostrofobi |
| 4 (B) | S2'nin AYNISI | Keşif eyleminin objektif tespiti (eğilme, alma) | Afinite: bildik konuma dönüş rahatlığı |
| 5 (D) | Static Dutch angle close-up (tilted exactly 15 degrees), dramatic side lighting | Bulunan şeyin yarattığı yönelim bozukluğu | Psikolojik şok: gerçeklik kırıldı |
| 6 (A) | S1'in AYNISI | Bilginin devasa evrende anlamsızlaşması | Döngüsel kapanış (loop kararıyla uyumlu) |

## 8.2 Yatay 12 sahne — "bilinmeyen tehdit" (4 akt)

| Akt | S | Kurulum | Yay gerekçesi |
|---|---|---|---|
| I · Giriş | 1 | Static EWS, göz hizası, üçte bir | Mekânın kuralları öğrenilir |
| | 2 | Static EWS, yüksek açı / kuşbakışı | Karakter korunmasız AV olarak işaretlenir (öngölge) |
| | 3 | Static MS, tam profil | Belgeselvari nesnel gözlem |
| II · Gerilim | 4 | Static CU, kask arkası / OTS | Negatif alan vizörle dolmaya başlar |
| | 5 | S3 TEKRARI (MS profil) | A-B-A ayırma ritmi; kesme hızlanır |
| | 6 | Static ECU, vizör yansıması | Tehdit yalnız YANSIMADA hissedilir; klostrofobi |
| III · Kriz | 7 | Static low angle MS | Tehdit büyür |
| | 8 | Static overhead / bird's-eye | ŞOK BANDI: alttan tam tepeye — mekânsal algı bilinçli yıkılır |
| | 9 | Static extreme low angle (worm's-eye) CU | Çaresizlik + tahakküm üst üste |
| IV · Çözülme | 10 | Static MS, doğrudan cephe (head-on) | Vizörle soğuk yüzleşme |
| | 11 | Static EWS, alçak açı, derin odak | Sessiz uzaklaşma |
| | 12 | S1 TEKRARI (EWS göz hizası) | Evrenin kayıtsızlığı; yay kapanır |

---

# 9. ✅ SAHNE HARİTASI KONTROLÜ — bu kılavuzun 6 maddesi

```
□ Her ardışık sahne çifti GÜVENLİ BANDI sağlıyor (≥1 ölçek kademesi VE
  ≥45° açı farkı) ya da bilinçli ŞOK olarak işaretli (filmde ≤2)
□ Kurulum sayısı §4 bandında; iskelet tekrarları (A-B-A) haritada işaretli
□ Yay filmin temasıyla eşleşiyor (§5) ve doruk sahnesi filmin EN YÜKSEK
  kontrast sıçraması
□ Açı sıçramaları ekran yönü / coğrafya kilitlerini bozmuyor (UZAMSAL)
□ S1 ↔ son sahne ilişkisi bilinçli: döngü mü (aynı kurulum — loop
  satırıyla tutarlı) kapanış kontrastı mı
□ Prompt zincirinde sahneden sahneye YALNIZ [KAMERA] katmanı değişiyor;
  özne çıpası + ortam + stil kelimesi kelimesine sabit
```

---

# 10. 📚 KAYNAKLAR

```
araştırmalar/12.md                       ham rapor (22.08.2026) — teorik
                                         çerçeve (Mascelli · Block · Sharff)
KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md     tek çekimin anlamı (kardeş dosya)
KURGU_RITMI_VE_IHRAC_KILAVUZU.md §2      örüntü kırıcı kapısı (kurgu tarafı)
SAHNE_DEVAMLILIK_KILAVUZU.md             karakter çıpalama (⑦ §2 kuralının kaynağı)
UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md ekran yönü kilitleri (§3 uyarısı)
TEMA_MUHENDISLIGI_KILAVUZU.md            tema seçimi (§5'in girdisi)
SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md §2   vuruş haritası (yayın dram girdisi)
```
