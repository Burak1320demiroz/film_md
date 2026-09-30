# ✋ MİKRO-AKSİYON VE HALÜSİNASYON KILAVUZU — Model Ne Yapamıyorsa Ona Yazılmaz

> **Neden var (22.09.2026):** THE_SLOW_RAIN'in PART 1 QA kaydı dört ayrı arızayı aynı
> filmde gösterdi: toka ayarlarken **eldiven metalle eridi** (① 02:35 🔴) · kanat inişte
> **karın içinden geçti** (① 02:14 🔴) · kızak çekme dizisi **yürüme platosuna** döndü
> (④ S17-S24 · ⑫ 02:30-03:30) · zeminde **plansız kamera tripodu** belirdi (⑤ S14 · ⑮ V14)
> ve 24 sahnenin 19'unda sağ alt köşede **filigran** vardı (⑤). THE_STOLEN_SKY'da kalın
> basınç eldiveni **klavyede çıplak el gibi tuşladı** (⑧ D206 TEKRAR E5).
> TUR 24'ün 4. raporu bunlar için eylem ve negatif sözlükleri önerdi; bu kılavuz o
> önerilerin depo ölçümünden geçen kısmıdır. Reddedilenler: `04_ARASTIRMA_BULGULARI.md`
> §TUR 24 ② (R2: "%100 negatif temizlik").
>
> **Bu kılavuz ne DEĞİLDİR:** temasın ölçülmüş çekirdeği `PROMPT_HATA_ONLEME_KILAVUZU.md`
> §3b'dedir (zamanlama · ara katman · kadraj · iki yönlü cümle) ve orada kalır. Filigranın
> yeri §4 ve **D215**'tir: *araç ayarıdır, prompt cümlesi değil.* Burası **eylem seçimi**
> (ne yazılır) ve **sızıntı** (ne sızar) kılavuzudur.
> ⚠️ **Etiket:** her kalıp ÖNERİ'dir; raporun başarısızlık yüzdeleri kaynaksızdı.

---

# 1. 🔄 MİKRO → MAKRO — eylemi modelin yapabileceği boya getir

Parmak ucu işi (toka, vida, ince kablo, küçük düğme, kazıyıcı ucu) kadrajda küçük bir
alan kaplar; eldiven nesneyi örter; model örtülen kısmı tutamaz, eldiven ile metal aynı
dokuya karışır (rapor 4 mekanizması · §3b VAE açıklamasıyla aynı). Deponun en ağır
çözülmemiş sınıfı budur ve **cümle eklemek onu durdurmuyor** (§3b: temas cümlesi VAR iken
bulgu oranı YOK'tan yüksek, RR 2,10).

**Kural:** filmin olayı bir el işiyse, iş **tüm gövdenin yaptığı** bir eyleme büyütülür.
Olay aynı kalır, ölçeği değişir.

| ⛔ mikro eylem (yazılmaz) | ✅ makro karşılık (aynı olay) |
|---|---|
| parmakla toka/mandal açmak | iki elle büyük bir kilit koluna ağırlık vermek |
| tornavidayla vida sıkmak | iki elle bir levyeyi panel aralığına sokup omuzla kanırtmak |
| ince kablo bağlamak | kalın zırhlı bir fişi iki elle yuvasına itip oturtmak |
| bıçak ucuyla buz kazımak | dizleri bükülü, dirsek/alet sırtıyla donmuş panele vurmak |
| küçük çip değiştirmek | büyük bir modül kutusunu rayına omuzla itmek |
| klavyede tuşlamak | eldivenli avuçla büyük bir düğmeye/panele basıp tutmak |
| küçük bir düğmeyi çevirmek | büyük bir çarkı iki elle, gövdeyle çevirmek |

- Makro nesne **büyük** yazılır ve boyu bedene göre verilir (`a lever as long as her
  forearm`) — nesne-göreli ölçü [D138].
- Makro eylem ⑳ ZORLANMA'nın efor fiilleriyle (`pulls · levers · hauls`) yazılır ve
  ödemesini taşır → `FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU` §1.
- Filmin yapısı küçük bir el işini gerektiriyorsa (novum), iş **kadrajdan çıkarılır**:
  hazırlık bir klipte, sonuç bir sonraki klipte (§3).

# 2. 🚶 YÜRÜME PLATOSU — model zor işi yürümeye çevirir

Karmaşık bir görev yazıldığında model onu çözemeyip en güvenli harekete kaçar: kameraya
yürüyen, etrafa bakan, dolaşan bir figür (rapor 4 "action degradation"). Depoda iki kayıt:

- THE_SLOW_RAIN S17-S24: planda **donma, kesme, kazıma, batma** vardı (S18 kanatta donan
  kabuk · S19 donan kanat ucunu kesme); ekranda **peş peşe yürüme** vardı. QA cevabı:
  *"diffusion modellerinin fiziksel aksiyon varyasyonunu (kesme, kazıma, saplanma)
  üretemeyip jenerik yürüme üretmesinden kaynaklanmaktadır"* (④ soru 6).
- ADAY-95: *"TIMELINE kapıyı anlattı, astronot boşta döndü"* — beden için iş yazılmamıştı.

## 2.1 Kural

```
□ yürüme bir SAHNENİN tamamı olamaz. Çok klipli sahnede en çok BİR klip yürüme/yol
  klibidir; öteki klipler bedenin YERE KİLİTLİ olduğu bir eylem taşır.
□ zor iş klibinde yürüme fiili yazılmaz (walks · approaches · steps toward · moves to);
  beden alt gövdeden zemine kilitlenir, hareket gövde/omuz/koldan gelir.
□ görev tek fiilde özetlenmez ("repairs the panel") — makro eylemin EVRESİ yazılır
  (§1 tablosu · SAHNE_DOLULUGU üç evre).
```

## 2.2 Plato kırıcı duruşlar (rapor 4 tablo b → depo biçimi)

| duruş | beden | neden yürümeyi keser |
|---|---|---|
| **omuzla panele yüklenmek** | alçak ağırlık merkezi, ayaklar sabit, omuz panelde | hareket yalnız göğüs itmesi |
| **iki elle levyeye asılmak** | bacaklar geride gergin, ağırlık geride | adım döngüsü yok |
| **diz çöküp tutunmak** | bir diz zeminde, iki el tutamakta — üç temas noktası | yürüme üretilemez |
| **omuzla kapıya dayanmak** | gövde kapıya eğik, tabanlar kilitli | sıfır adım, sürekli kuvvet |
| **tutamağa asılı kalmak** (düşük g / sarsıntı) | ayaklar zeminden kesik | adım yok |

⭐ Çok klipli sahne bunu kolaylaştırır: THE_SLOW_RAIN'in 80 saniyelik kızak dizisi bu
rejimde **iki üç sahnedir**: bir yol klibi (geniş, kızak arkada) + bir durma sahnesi (diz
çöküp donan kanat ucuna vurmak) + bir yüklenme sahnesi (kayışa asılmak, kızak sıkışmış).
Her kurulum değişiminde beden başka bir işte (`COK_KLIPLI_SAHNE_KILAVUZU` §2).

# 3. 🫳 TEMAS — anı gösterme, öncesini ve sonrasını göster

§3b'nin üç kararı aynen geçerlidir. Bu kılavuzun eklediği:

```
① TEMAS BÖLÜNÜR (yalnız çok klipli sahnede mümkün — COK_KLIPLI §3.6)
   klip N    HAZIRLIK: eldiven kola doğru, ağırlık geride — temas ya yok ya ilk 2 s'de kurulu
   klip N+1  SONUÇ:    "CONTINUOUS ACTION: her glove is already closed on the lever …"
             temas 0. saniyede kurulu gelir; klip SONUCU gösterir (kapak aralanır, buhar)

② PERDELEME KURULUMLA SEÇİLİR
   temas noktası giysinin ön kolu, omuz plakası ya da nesnenin kendi gövdesi arkasında
   kalacak şekilde yan profil / omuz üstü kurulum seçilir (rapor 4 kural 1 · §3b ③).
   ⛔ temasa bakan ECU ("extreme close-up of fingers turning a dial")

③ ALET TEK RİJİT PARÇA
   alet büyük, keskin kenarlı, tek parça yazılır; parmakların alet üzerindeki
   hareketi TARİF EDİLMEZ (rapor 4 kural 3 · ÖNERİ):
   ✅ "a heavy steel bar, as long as her arm, wedged into the panel seam; she bears down
      on it with her shoulder"
```

# 4. 👻 SIZINTI — kadraja girmemesi gereken şeyler

## 4.1 Filigran — prompt değil, ARAÇ

Rapor 4 filigranın **negatif sözlükle %100 silindiğini** söyledi. Depo kaydı tersini
söylüyor: `no watermark` beş filmde neredeyse her promptta yazılıydı ve beşinde de köşede
filigran vardı; **kusur film başına değil ihraç hattına aittir** [D150 · D162 · D215].

```
⛔ negatif bloğa "Gemini sparkle · Veo logo · 4-pointed star" yazmak
   → etkisiz (D150) · marka adını ve kavramı çağırır (D59) · ㉗ NEGATIVE tavanını yer
✅ KAPI 0'da araç/hesap ayarı ve ihraç yolu (D215 · PROMPT_HATA §4)
✅ kurgu kapısı köşe testi (D150 · olcum_kapisi.sh KÖŞE TESTİ)
⚠️ kırpma/maske bir KURGU kararıdır; AI içerik beyanı kanal politikasındadır
   (apexaic/POLITIKA_VE_RISK.md) — kararı sahip verir.
```

## 4.2 Tripod — promptun kendi kelimesi olabilir (ADAY-98)

Plansız kamera tripodu iki filmde kadraja girdi: THE_SLOW_RAIN S14 (⑤ + ⑮) ve
THE_STOLEN_SKY PART 1 00:39. **İki filmin de CAMERA satırı** `… on a fixed locked-off
tripod …` diyordu (SLOW_RAIN 96/96 · STOLEN_SKY 94/192). QA kaydının kendi cevabı:
*"tripod yapay zeka modelinin 'camera/setup' kelimelerinden türettiği … halüsinasyon."*
Bu, PROMPT_HATA §6 **jeton sızıntısı** sınıfıdır: promptun kelimesi kadraja yazılıyor.

```
⛔ CAMERA: 75mm lens on a fixed locked-off tripod 1.6 m in front of her …
✅ CAMERA: 75mm lens on a locked-off camera 1.6 m in front of her …
```

⚠️ **ADAY, ders değil:** "tripod" depoda 440 kez geçiyor ve çoğu filmde tripod çıkmadı.
Değişiklik bedava (kurulum imzası lens · yükseklik · ölçek · açıdan kurulur, "tripod"
kelimesine bağlı değil) ama etkisi ölçülmedi. Kayıt: `DERSLER/GOZLEM_DEFTERI.md` ADAY-98.
Rapor 4'ün negatif listesi (`modern camera tripod, tripod legs, C-stand …`) **alınmadı**:
kavramı çağırmak onu kadraja davet eder [D59].

## 4.3 Anakronik eşya — envanteri POZİTİF yaz

Modern çanta, sivil giysi, stüdyo ekipmanı "set arkası" verisinden sızar (rapor 4). Depo
yolu yasak listesi değil **envanterdir**:

```
✅ "the only equipment in frame is the folded wing sled and the steel canister at her boots"
   (sahnenin prop çapası — COK_KLIPLI §3.5 · PROMPT_HATA §3 sınıf 11)
✅ dünya cümlesi film başına bir kez, her dış sahnede birebir (PROMPT_HATA §3 sınıf 8)
```

Metin/arayüz katmanları (altyazı, zaman kodu, logo) negatif çekirdeğin metin cümlesiyle
zaten kapsanır (§5.1); yeni liste eklenmez.

---

# 5. ✅ KONTROL LİSTESİ

```
□ parmak ucu işi yok; her el işi §1 tablosuyla gövde eylemine büyütüldü
□ makro nesne bedene göre boylandı ve ödemesi yazıldı (efor kılavuzu)
□ zor iş klibinde yürüme fiili yok; alt gövde zemine kilitli
□ çok klipli sahnede en çok bir yol klibi
□ temas ya ilk 2 s'de kurulu ya iki klibe bölünmüş; temasa bakan ECU yok
□ CAMERA satırında "tripod" kelimesi yok (ADAY-98 · ÖNERİ)
□ negatif blokta marka/filigran/tripod listesi YOK; filigran KAPI 0 ve kurgu işi
□ sahnenin eşya envanteri pozitif cümleyle yazılı
```

# 6. ⬜ ÖLÇÜLMEMİŞ

- "tripod"suz CAMERA satırıyla bir filmde ⑤/⑮ plansız tripod sayısı (ADAY-98'in kapanması).
- Temasın iki klibe bölünmesinin ① füzyon bulgusunu düşürüp düşürmediği.
- Mikro→makro dönüşümün ④ ve ⑫ plato bulgularına etkisi.

**Kaynaklar:** [D150] · [D162] · [D215] · [D206] · [D138] · [D59] · ADAY-95 · ADAY-98 ·
`PROMPT_HATA_ONLEME_KILAVUZU` §3 · §3b · §4 · §6 · `COK_KLIPLI_SAHNE_KILAVUZU` §3.5-§3.6 ·
TUR 24 rapor 4 (`URETIM_ONCESI_ANALIZ/TUR24_HAM_RAPORLAR/`).
