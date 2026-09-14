# 📡 YAYIN VE PERFORMANS KILAVUZU — Gerçek İzleyici Verisi Döngüsü

> **Neden var (22.08.2026):** Üretim akışı bugüne kadar 11. adımda
> (PAKETLEME) bitiyordu. Yayınla → ölç → kılavuzu revize et adımı hiçbir
> dosyada yoktu. Sonuç: depodaki her hook kuralı, her başlık formülü ve
> her kanca skoru MODEL ölçümüne karşı optimize edildi; gerçek izleyiciyle
> temas sıfır. `HOOK_VE_ILK_SAHNE_KILAVUZU.md` §0 bunu kendisi kayda
> geçiriyor: *"HİÇBİR FİLM YAYINLANMADI. Buradaki her sayı dış araştırmadan
> gelen HİPOTEZDİR."* Bu dosya o cümlenin kapanma prosedürüdür.
>
> **Ne zaman okunur:** teslim paketi hazır olduğunda (kurgu kapısı geçti,
> QA koşuldu, kapak ve paketleme yazıldı) — yani üretim akışının SON adımı.
> Kaynak: `araştırmalar/1.md` (22.08.2026 derin araştırması).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① BURADAKİ HER SAYI DIŞ KAYNAKTIR. Platform davranışı ve benchmark'lar
   22.08.2026 araştırmasından gelir; bu serinin ÖLÇÜLMÜŞ sonucu değildir.
   İlk gerçek koşu geldiğinde §5 tablosu doldurulur ve DIŞ SAYI GERÇEK
   SAYIYA DİRENEMEZ — çakışan her eşik gerçek veriyle değiştirilir.

② BU KILAVUZ ÖLÇÜ ALETİDİR, ÜRETİM KURALI DEĞİLDİR.
   Buradan çıkan hiçbir bulgu doğrudan prompta yazılmaz. Bulgu önce
   §6'daki geri besleme yolunu izler: hangi kılavuzun hangi bölümü
   yanlış çıktı → o bölüm revize edilir → ders yazılıp yazılmayacağına
   AGENTS.md kart G karar verir.

③ ÖLÇÜM SAPMASI BURADA DA VAR. QA tablolarındaki ±1.3 puan gürültü
   bandının platform karşılığı §3'te: hangi metriğin kaç gösterimde
   sinyal olduğunu bilmeden karar verilmez. Erken müdahale, bu
   kılavuzun en pahalı hatasıdır.

④ DEPONUN İKİ KANITLI DEZAVANTAJI ÖLÇÜME DAHİLDİR:
   ekran metni 0,0 sn [D61/70] ve lockoff/tek çekim kimliği.
   İlk koşular bu iki kısıt ALTINDA okunur; düşük VSA veya düşük hold
   rate çıkarsa suçlu otomatik olarak "metin yok" değildir — §4'teki
   suçlu değişken listesi sırayla elenir.
```

---

# 1. 🚦 YAYIN ÖNCESİ — kayıt açılmadan yayın yok

Yayın bir üretim adımıdır; kaydı tutulmayan yayın ölçülemez.

```
□ FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md → filme satır aç
□ Satıra yazılacak KİMLİK alanları (yayından ÖNCE doldurulur):
     · film adı + format (shorts / 2-4 / 3-5 / 6 dk / 8 dk / 7-20 dk)
     · yayın tarihi + saat (GG.AA.YYYY SS:DD)
     · platform(lar) ve her birinde hangi başlık/kapak VARYANTI
     · plandaki HOOK TİPİ satırı (HOOK_VE_ILK_SAHNE_KILAVUZU §4)
     · S0 soru cümlesi (plandan birebir)
     · QA skorları: teknik / hikaye / mantık (+ karakter / ses)
□ ⛔ VARYANT KİLİDİ: bir filmin ilk 48 saatinde TEK değişken oynatılır.
     Aynı anda hem kapak hem başlık değişirse hangisinin çalıştığı
     ölçülemez ve o koşu tabloya ⚠️ ŞARTLI girer.
□ Plan B kapağı yayın ANINDA hazır olur — 48 saat sonra üretilmeye
     başlanan kapak, karar penceresini kaçırmış kapaktır
     (KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU §7.2).
```

---

# 2. 📊 KARAR MATRİSİ — eşik → karar → suçlu değişken

> Her satır: metrik **tehlike eşiği** altına düştüğünde ne YAPILIR ve
> önce hangi üretim değişkeni sorgulanır. Eşikler dış kaynaktır (§0①).
> ⛔ Hiçbir satır §3'teki minimum örneklem sağlanmadan işletilmez.

## 2.0 ⭐ ÖNCE HİYERARŞİ — üç platform aynı şeyi ödüllendirmiyor

> **Eklendi 27.08.2026 (araştırma 1).** Aşağıdaki tablolar metrikleri
> yan yana listeliyordu ve hangisinin ÖNCELİKLİ olduğunu söylemiyordu.
> Bu, deponun süre tartışmasını yıllarca çözemeyen sebebiydi: üç
> algoritma üç farklı şeyi kapı olarak kullanıyor.

```
YouTube Shorts   →  VSA İLK KAPIDIR (>%70). Geçilmezse "seed" aşamasında
                    dağıtım durur; AWT ne kadar yüksek olursa olsun.
                    Kapı geçildikten SONRA erişimi AWT + memnuniyet belirler.
                    ⭐ VSA süreyle ilgili DEĞİL — 0. kareyle ilgili.

TikTok           →  TAMAMLANMA ORANI (CR) mutlak belirleyici. Algoritmanın
                    ağırlığının en büyük payı sona ulaşma yüzdesinden gelir.
                    Kısa süre yapısal avantaj.

Instagram Reels  →  SENDS PER REACH (erişim başına DM gönderimi).
                    Yeni kitleye ulaşımın tek üst sinyali. İzlenme
                    süresinden bile güçlü. Yavaş yanan gerilim avantajlı.
                    ⚠️ Mosseri paradoksu: "watch time en önemli sinyal"
                    beyanı MEVCUT takipçiye (Home Feed) ulaşmak içindir;
                    yeni kitle (Explore/Reels) sends ile açılır. İkisi
                    çelişmez, farklı yüzeylere hizmet eder.
```

**Bu hiyerarşiden çıkan üretim kararı:**

```
□ PLATFORM ÖNCE SEÇİLİR, SÜRE ONDAN TÜRER — tersi değil.
  48 s ızgarası TikTok'ta en kötü, Instagram'da en iyi, YouTube
  Shorts'ta KONU DIŞI seçimdir (orada tek kapı 0. karedir).
□ Aynı film üç platforma birden yükleniyorsa, üç farklı sayının
  ÜÇÜNÜ DE ayrı okumak zorunludur. Tek "başarılı/başarısız" hükmü
  verilemez.
□ ⛔ VERİ YANILSAMASI KAYDI: TikTok 1. saniyeyi görüntülenme sayıp
  hemen kaydıranı ağır cezalandırırken, YouTube 31.03.2025'ten beri
  0. saniyeyi bile public view sayıyor. Aynı film iki platformda
  YouTube'da "başarılı", TikTok'ta "başarısız" görünebilir ve ikisi
  de doğrudur. Karşılaştırma yalnız ORANSAL metrikler üzerinden yapılır.
```

> ⭐ **İLK YAYIN İÇİN ÖNERİ:** YouTube Shorts. Sebebi tercih değil
> ölçüm ekonomisi — orada tek kapı VSA'dır, VSA ise 0. karenin sınavıdır
> (`HOOK` §2.1). Deponun hiç koşmadığı tek testi ilk yayında izole
> ölçmenin en temiz yolu budur; süre tartışması o platformda hiç
> devreye girmez.

---

## 2.1 DİKEY SHORTS (9:16 · 48 s) — YouTube Shorts / Reels / TikTok

| Metrik | 🔴 Tehlike | 🟢 Hedef | Karar | Önce sorgulanan değişken |
|---|:--:|:--:|---|---|
| **VSA** (izlendi/kaydırıldı) | < %60 | ≥ %70 | Yeniden paketle: S0'ı değiştir, filmin en yoğun kadrajını başa al | S0 açılış kadrajı durağan — `HOOK` §2.1 "0. kare sınavı" fiilen koşulmamış |
| **APV** (tamamlanma) | < %50 | %65-80 | Yeniden kurgula: terk saniyesini §4 ile sahneye çevir, o yuvayı kırp | Orta yuvalarda olay yok — vuruş tablosunda boş vuruş var |
| **TikTok tamamlanma** (ilk 15-60 dk) | < %30 → 200-300 izlenmede donar | ≥ %70 | Hattan çek, yeni açılışla yeniden yükle | İlk 2 saniye mikro-topluluk diliyle uyuşmadı |
| **TikTok ortalama izlenme** | < 10 s | 15-20 s | Gözlem: filme dokunma, SONRAKİ planda atmosfer sahnesi kes | Süre ile tempo uyuşmuyor — çatışma geç başlıyor |
| **IG ilk 3 sn hold rate** | < %40 | ≥ %60 | İlk saniyeleri kırp (yavaş açılış / boş kadraj) | 1,7 saniyelik karar penceresi kaybedildi |
| **IG gönderim/erişim** | ≤ beğeninin %10'u | beğeninin 3-5 katı | Bekle: bu filme müdahale etme | Film teknik olarak temiz ama PAYLAŞILACAK bir önerme taşımıyor |

## 2.2 YATAY (16:9 · 2-4 / 3-5 / 6 / 8 / 7-20 dk) — YouTube uzun form

| Metrik | 🔴 Tehlike | 🟢 Hedef | Karar | Önce sorgulanan değişken |
|---|:--:|:--:|---|---|
| **CTR** (ilk 4 saat) | < %3 | %5-8 | Manuel müdahale: kapak + başlık kombinasyonunu değiştir (§3.3) | Kapak/başlık sinerjisi jenerik — 120 px testi geçmemiş kapak |
| **APV** | < %50 | %70-90 | Formatı gözden geçir: düşüş dakikada %5'i aşıyorsa SONRAKİ filmin sahne haritası değişir | Hikaye zayıf; görsel kalite hikaye eksiğini örtmüyor |
| **İlk 30 sn tutunma** | < %50 | ≥ %70 | S0-S1 mimarisini revize et (`HOOK` §8, 7 madde) | Katalizör 0:15 kapısından geç geldi |
| **Ortalama izlenme süresi** | — | mutlak dakika artışı | Uzun formda ham AVD, APV'den daha ağır basar; kısa kesmek her zaman doğru değil | Süre bandı formata göre yanlış seçilmiş |

> ⚠️ Kapak CTR skalası ayrı kaynakta duruyor ve burada TEKRARLANMAZ:
> `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` §7.1 (%1-2 alarm · %3-4 ortalama ·
> %5-6 güçlü · %7+ olağanüstü) + §7.2 48 saatlik Plan B kuralı.

---

# 3. 🔍 SİNYAL Mİ GÜRÜLTÜ MÜ — karar için minimum örneklem

> QA tablolarındaki "1.5 puandan küçük fark gürültüdür" kuralının
> platform karşılığı. Bu bölüm okunmadan §2 işletilmez.

```
DİKEY (TikTok / Reels / Shorts) — KÜÇÜK ÖRNEKLEM YETERLİ
  İlk 200-500 gösterim rastgele değildir: algoritma etiketlere göre
  seçilmiş bir ön kitledir. TikTok'ta ilk 300 izlenmede tamamlanma
  %20'de kalmışsa bu GÜRÜLTÜ DEĞİLDİR — pazar uyumsuzluğunun kanıtıdır.
  → 300 gösterim = karar verilebilir sinyal.
  → Beklemek burada zarar: video 200-300 bandında donar ve açılmaz.

YATAY (YouTube CTR) — BÜYÜK ÖRNEKLEM ŞART
  %4,0 baz CTR'de 1,0 puanlık farkı %95 güvenle görmek için varyant
  başına ~6.700 gösterim gerekir. Sıfır aboneli kanalda ilk 48 saatte
  bu hacme ulaşılmaz.
  → %3 ile %4,5 arası dalgalanma GÜRÜLTÜDÜR, karar verdirmez.
  → İSTİSNA: gösterim hızı tavan yaparken CTR %3'ün ALTINDAYSA bu
    istatistiksel değil operasyonel bir sinyaldir — §3.3 devreye girer.

APV / retention eğrisi — HER İKİ TARAFTA DA ERKEN OKUNUR
  Eğrinin ŞEKLİ (nerede kırıldığı) ilk yüz izlenmede bile okunur;
  eğrinin SEVİYESİ (yüzde kaç) örneklem büyüdükçe oturur.
  → Şekli §4 ile hemen kullan, seviyeyi tabloya geç yaz.
```

## 3.3 YouTube "Test & Compare" — neden yeterli değil

```
① KAZANANI CTR'YE GÖRE SEÇMEZ, İZLENME SÜRESİ PAYINA göre seçer.
   Bu depo için ÖNEMLİ: agresif bir kapak tıklanır ama film sakin ve
   felsefi tempoda ilerlerse izleyici erken çıkar ve o kapak testi
   KAYBEDER. Araç, vaat-teslim uyumunu ölçer — CTR'yi değil.
② KARARSIZ SONUÇ TUZAĞI: hacim yetmezse test "Performed Same" biter ve
   sistem İLK yüklenen resmi sabitler. Bu, birinci resmin kazandığı
   anlamına GELMEZ; beraberlik bozucudur.
③ Yeni kanalda test 1-2 hafta sürer ve videonun keşif penceresini yer.

→ İLK 72 SAATTE KARAR: manuel A/B. İlk 3-4 saatte gösterim yükselirken
  CTR %3'ün altındaysa 10 bin gösterimi BEKLEME; ikinci kapak/başlık
  kombinasyonunu yayına al ve sonraki 4 saati karşılaştır.
→ Test & Compare, kanal oturduktan SONRA (istikrarlı gösterim hacmi
  varken) vaat-teslim uyumunu ölçmek için kullanılır — o zaman güçlüdür.
```

---

# 4. 📉 RETENTION EĞRİSİ → SAHNE YUVASI ÇEVİRİSİ

> Eğri bir otopsi raporudur. Terk SANİYESİ, planın ızgarasıyla SAHNEYE
> çevrilir — bu çeviri `AGENTS.md` ortak adım ⑨'daki hizalama kapısının
> aynı aritmetiğidir:
>
> ```
> sahne başlangıcı(n) = hook süresi + (n-1) × klip süresi
> ```
>
> Terk saniyesi hangi aralığa düşüyorsa suçlu O SAHNEDİR. Rapor değil,
> izleyici konuşuyor — bu yüzden bulgu ÖNERME KAPISINDAN muaf değildir:
> planda yazılı bir kilit yüzünden terk ediliyorsa kilit tartışılır.

## 4.1 Üç eğri şekli

```
🔻 UÇURUM (ilk 3 sn'de %40-60 düşüş)
   OKUMA: S0 kaydırma bariyerini aşmadı.
   SAHNE: hook klibi (S0).
   DEPO KARŞILIĞI: HOOK §2.1 "0. kare sınavı" ve §2.2 "hareketin
     ortasında açılış" fiilen uygulanmamış. Yavaş dönen gemi, boş
     manzara, insansız kadraj — bu üçü uçurumun mimarisidir.
   ⚠️ Dış araştırma çözümü "metin + hızlı kesme" diyor; ikisi de bu
     seride YASAK (§7). Bizim elimizdeki üç araç: kadraj içi olay,
     ölçek kontrastı, ilk 2 saniyenin sesi (HOOK §5).

📉 ORTA BÖLÜM ÇÖKÜŞÜ (dakikada %15+ istikrarlı erime)
   OKUMA: görsel monotonluk + anlatı ilerlemiyor.
   SAHNE: eğrinin eğiminin arttığı ilk yuva; oradan sona kadar tüm blok.
   DEPO KARŞILIĞI: vuruş tablosunda boş vuruş var
     (SENARYO_VE_VIRAL_KAMERA §2.3) VEYA aynı ölçekte ardışık sahneler
     dizilmiş. Çözüm ritim tarafında:
     KURGU_RITMI_VE_IHRAC_KILAVUZU.md §2 (örüntü kırıcı bütçesi).

🔚 FİNAL ÖNCESİ KAÇIŞ (son %20'de ani kırılma)
   OKUMA: izleyici filmin bittiğini HİSSETTİ.
   SAHNE: doruk sahnesinin BİR SONRAKİ yuvası.
   DEPO KARŞILIĞI: çözülme bloğu uzun. Doruk ile teknik bitiş arasındaki
     mesafe saniyelere indirilir. Shorts'ta ayrıca loop kapanışı
     (SENARYO_VE_VIRAL_KAMERA §5) bu kaçışı geri kazanan tek araçtır.
   ⚠️ Depo filmlerinde "insansız ayrılış kodası" (2-4 dk kartı, S14+)
     planlıdır. Kodada kaçış görülüyorsa bu ÖNERME ÇATIŞMASIDIR:
     kod planlıysa bulgu tabloya "önerme" olarak yazılır ve koda
     kısaltılmadan önce ikinci bir filmde tekrar görülmesi beklenir.
```

## 4.2 Suçlu değişken eleme sırası

Bir terk noktası bulunduğunda suçlu şu SIRAYLA aranır — ilk üçü ucuzdur,
sonrakiler pahalıdır:

```
1. PAKETLEME    başlık/kapak vaadi o sahnede karşılanmıyor mu?
                (vaat-teslim: VIRAL_BASLIK §retention rule)
2. KURGU        o yuvada ritim düştü mü, ses köprüsü koptu mu?
                (KURGU_RITMI_VE_IHRAC §2-3)
3. SES          ortam yatağı o kesmede öldü mü? [D83]
4. SAHNE İÇERİĞİ  vuruş boş mu, olay yok mu?
5. PLAN         hikaye o noktada duruyor mu — sonraki filmi bağlar
6. FORMAT       yanlış süre bandı seçilmiş — en pahalı ve en son sorgulanan
```

---

# 5. 🧾 KOŞU KAYDI — tabloya ne yazılır

Her yayın bir KOŞUDUR ve QA koşuları gibi kaydedilir. Kayıt yeri:
`FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md`.

```
□ 24. saat  → ilk satır: VSA/hold · CTR · APV · gönderim
□ 48. saat  → karar satırı: BEKLE / KAPAK / BAŞLIK / YENİDEN KURGU / ÇEK
□ 72. saat  → eğri şekli (§4.1) + terk saniyesi + çevrilen SAHNE numarası
□ Değişken oynatıldıysa: ne değişti, ne zaman, sonraki 4 saatte ne oldu
□ 🆕 PUBLIC VIEW ve ENGAGED VIEW **AYRI SÜTUNLARA** yazılır (YouTube
     Analytics → Gelişmiş Mod). 31.03.2025'ten beri public view loop'ları
     sayıyor, engaged view saymıyor; ölçülen şişme ~%30. Tek sayı yazılan
     satır ⚠️ ŞARTLI'dır — "loop tuttu" hükmü ikisi karşılaştırılmadan
     verilemez [SENARYO_VE_VIRAL_KAMERA §5].
□ 🆕 AI ALGISI SAYACI: yorumlarda "AI / yapay zeka / fake / CGI"
     kelimelerinin geçtiği yorum sayısı / toplam yorum. Deponun hiç
     ölçülmemiş bir numaralı strateji riski budur
     [DIKEY_MIKRO_DRAMA §6.1]. İlk üç koşuda mutlaka kaydedilir.
□ 🆕 PLATFORM BAŞINA AYRI SATIR: aynı film üç platformdaysa üç satır
     açılır ve her satır kendi kapı metriğiyle okunur (§2.0). Tek
     birleşik hüküm yazılmaz.
□ ⛔ GEÇERLİLİK İŞARETİ (QA tablolarıyla aynı dil):
     ✅ geçerli   — minimum örneklem sağlandı (§3)
     ⚠️ ŞARTLI    — örneklem altında VEYA aynı anda iki değişken oynatıldı
     🚨 GEÇERSİZ  — yayın kaydı yayından SONRA açıldı (kimlik alanları
                    geriye dönük yazıldıysa koşu sayılmaz)
```

---

# 6. 🔄 GERİ BESLEME — gerçek sayı hangi belgeyi değiştirir

> Bu kılavuzun VAR OLMA SEBEBİ bu bölümdür. Veri toplanıp durursa
> hiçbir şey değişmez; her metriğin bir ADRESİ vardır.

| Gerçek veri | Yanlışlanan belge | Yapılacak |
|---|---|---|
| İlk 3 sn tutunma / VSA | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` §1 (dış sayılar) + §0③ plato ölçütü | §1'deki hipotez sayıları gerçek sayıyla DEĞİŞTİRİLİR; kanca skoru 5-6 platosu kırıldı mı, §0③'e işlenir |
| CTR | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` §7 skalası | Skala bu kanalın gerçek bandıyla güncellenir |
| APV / eğri şekli | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2 vuruş bantları + `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §1 ASL eğrisi | Terk yuvası hangi vuruşa denk geliyorsa o vuruşun yüzde bandı revize edilir |
| Gönderim / paylaşım | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` + `KARAKTER_VE_DUYGU_KILAVUZU.md` §5 | Paylaşımı tetikleyen duygu üretilemiyorsa §5 sayısal kilitleri sıkılır |
| Devam / seri sinyali | `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` §4 | Devam hakkı eşikleri bu kanalın gerçek dağılımına göre yeniden konur |
| QA skoru yüksek + gerçek metrik düşük | `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` | ⭐ EN DEĞERLİ SİNYAL: rubrik ölçtüğü şeyi izleyici umursamıyor demektir. O kategori rubrikte ağırlık kaybeder |

```
⛔ SIRA: veri → BELGE revizyonu → (gerekiyorsa) ders.
   Ters sıra yasak. AGENTS.md §8: "kural eklemek kaliteyi artırmadı."
   Bir metrik bir kılavuz bölümünü yanlışlıyorsa çözüm YENİ DERS DEĞİL,
   o bölümün DÜZELTİLMESİDİR. Ders ancak aynı hata İKİNCİ filmde
   tekrarlarsa yazılır (kart G).
```

---

# 7. ⛔ ARAŞTIRMADAN DEPOYA GEÇMEYENLER — dürüst kayıt

| Araştırmadaki öneri | Neden geçmedi |
|---|---|
| "Text overlay hook ekle" (TikTok yeniden paketleme reçetesi) | Ekran metni 0,0 sn [D61/70] · kurgu kapısı madde ③. Metin kancası platform AÇIKLAMA alanına yazılır → `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md`. Kapak da metinsiz üretilir; tipografi post'ta. |
| "Uçurum sahnelerini 2-3 kat hızlandır (speed-ramp)" | Kurguda hız ince ayarı en çok %2-4 [`KURGU_VE_TESLIM` §3]. Fazlası hareketi yapaylaştırır ve fizik kilitlerini görünür şekilde bozar. Çözüm hızlandırma değil KIRPMA (kırpma bütçesi, D100). |
| "İlk 3 saniyede insan yüzü + güçlü diyalog" | Diyalog bütçesi ve register haritası ayrı kısıttır; yüz tarafı GEÇTİ ama kask altında → `KARAKTER_VE_DUYGU_KILAVUZU.md` §1 (vizör içi göz görünürlüğü). Ham hâliyle uygulanamaz. |
| "İlk 30 sn'de en az 19 görsel değişiklik" | Sabit ızgarada 30 saniye = 3-4 klip. Bu sayı bu üretim hattında fiziksel olarak imkansız. Karşılığı KADRAJ İÇİ olay yoğunluğu ve ölçek kontrastıdır → `KURGU_RITMI_VE_IHRAC` §2. |
| "Kapağa agresif/abartılı görsel koy, CTR zıplar" | Test & Compare izlenme süresi payına bakar (§3.3) ve bu seri sakin tempoda ilerler; vaat-teslim uyumsuzluğu CTR kazancını geri alır. `VIRAL_BASLIK` içindeki "retention rule" bunu zaten söylüyor. |

---

# 8. ✅ YAYIN SONRASI KONTROL LİSTESİ

```
YAYIN GÜNÜ
 □ 08_YAYIN_PERFORMANS_TABLOSU.md satırı AÇILDI (yayından önce)
 □ Plan B kapağı hazır ve dosyada
 □ Tek değişken kilidi: ilk 48 saatte kaç şey değişecek → 1

24. SAAT
 □ Metrikler tabloya yazıldı
 □ §3 okundu: bu sayı sinyal mi gürültü mü

48. SAAT
 □ §2 matrisinden karar alındı ve tabloya YAZILDI
 □ Karar "değiştir" ise: ne değişti + saat kaydedildi

72. SAAT
 □ Retention eğrisi §4.1 ile şekle çevrildi
 □ Terk saniyesi ızgara aritmetiğiyle SAHNEYE çevrildi
 □ §4.2 eleme sırası koşuldu, suçlu değişken yazıldı
 □ §6 tablosundan hangi belgenin revize edileceği belirlendi
 □ ⭐ QA skoru yüksek + metrik düşük çıktıysa DERS ETKİNLİK RAPORUNA not
 □ İş commit'e hazır bırakıldı (commit'i proje sahibi atar — AGENTS §5)
```

---

# 9. 📚 KAYNAKLAR

```
araştırmalar/1.md                    bu kılavuzun kaynak araştırması (22.08.2026)
FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md   koşu kayıtları
HOOK_VE_ILK_SAHNE_KILAVUZU.md        §0 dürüst kayıt · §1 hipotez sayılar · §8 plan kontrolü
KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md §7 CTR skalası + 48 saatlik Plan B
VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md   paketleme · vaat-teslim (retention rule)
SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md  §2 vuruş bantları · §5 loop
KURGU_RITMI_VE_IHRAC_KILAVUZU.md     terk noktasının kurgu tarafındaki karşılığı
SERI_VE_KANAL_STRATEJI_KILAVUZU.md   §4 devam hakkı eşikleri (aynı veriyi kullanır)
URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md   %72 kör alanın kapanma yeri
AGENTS.md §3 kart Y                  yayın kaydı görev kartı
```
