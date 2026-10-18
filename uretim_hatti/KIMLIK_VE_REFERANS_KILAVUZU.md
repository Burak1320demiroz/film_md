# 🪪 KİMLİK VE REFERANS KILAVUZU — aynı yüz, aynı giysi, aynı bant

> **Ne için:** dört filmin dördünde yüz, kol bandı rengi, şerit sayısı değişti; giysiye bayrak, arma, yazı eklendi (`ARASTIRMA/11` §B).
> Hiçbir filmde hangi referansın yüklendiği kayıtlı değil. Bu kılavuz referansı kurmayı, yüklemeyi, kareyi kabul etmeyi ve düzeltmeyi söyler.
> **Kim okur:** goruntu-yonetmeni · devamlilik · teknik-danisman · Fable · sahip (F7).
> **Kaynak:** `ARASTIRMA/ham/28` → `ARASTIRMA/13_SUZME_20261016.md` §B2 · `ARASTIRMA/11` §C3. Tamamlayıcı: `GPT_IMAGE_OMNI_KILAVUZU.md` §4-§6.
> **Tarih:** 16.10.2026. Panel sayfası kararı (sahip, 10.10.2026) yürürlükte; P17 ölçülene kadar değişmez (§7).

---

## 0 · Dört filmden

| Film | Kayma |
|---|---|
| WRONG_BURN (2 dk) | kol şeridi yok → turuncu şerit · kask içinde bere var/yok · çift vizör çizgisi · kask lambası dev küre |
| PLANET_THIEF | C19'da sakalsız başka yüz · göğüste hilal-yıldız arması · aynı alet üç biçim (kutu, matkap, tüfek) |
| MAYDAY_SEA | omuzluk lacivert → beyaz → lacivert · yeni yaralar · yeni arma · iki turuncu şerit |
| SKY_CATCH | aynı kadın üç farklı yüz · turkuaz → mavi · göğüste yazı · omuzda ABD bayrağı · pilotta ikinci şerit |

---

## 1 · Üç katman — üçü birlikte

1. **Görsel referans** — onaylı, numaralı (`ref/<No>.<AD>_v<k>.png`).
2. **Kimlik cümlesi** — `FILM.md` §3 ORTAK GÖRÜNÜM; her promptta birebir, yeni sıfat yok.
3. **Kayıt** — her üretimde hangi numaralar yüklendi (NOTLAR DENEMELER: `ref 1,7`).

Yalnız aynı adı kullanmak aynı yüzü getirmez; yalnız cümle de getirmez. Kayıt yoksa kayma sonradan sınıflanamaz.

---

## 2 · Referans biçimi

- Hat kuralı (sahip, 10.10.2026): özne başına **tek sayfa**, görünüşler ve durumlar panel. Bu sayfa **görsel üretimine** referanstır.
- **Videoya panel sayfası gitmez**; Omni'ye onaylı tek başlangıç karesi gider.
- Dış uygulamada iddia: tek görünüşlü ayrı dosyalar kimliği panelden iyi taşır, panel sayfası hedef kareye kopya figür ya da panelden sızma (önden rozetin arkaya geçmesi) getirebilir. **Ölçülmedi** → §7 deneyi.
- Panel sayfası kullanılırken: paneller arasında boşluk, panel üstünde yazı/ok yok, her panel tek figür; çekim anahtarı paneli adlandırır (`using the back-view panel`).
- Durum ayrı: kapak kapalı/açık, kask açık/kapalı, hasarsız/hasarlı ayrı panel. Zıt iki durum aynı üretimde eşit ağırlıkla verilmez.

---

## 3 · Yükleme ve rol

- Çekim başına **en çok 3 referans** (varsayılan). Veo 3.1'in resmî sınırı 3; GPT Image ve Omni için sınır bilinmiyor, muhafazakâr kalınır.
  Daha fazlası gerekiyorsa çekim bölünür ya da mekân/nesne referansı yerine master kare kullanılır.
- Her referans **numara + rol** ile anılır (OpenAI: "Identify each input by number and purpose"):
```text
Reference 2 (engineer): take her face, hair and the pearl-white suit with one plain turquoise band on each upper arm from it.
Reference 5 (cockpit): take the console layout and the window light from it.
```
- Her sahne grubunun başında referanslar **yeniden** eklenir; uzun sohbet ayrıntıyı korumaz.
- Daha sıkı yol (`ARASTIRMA/15` B2, sahip onayıyla varsayılan olur — A5): ChatGPT'de **her kare yeni sohbet**, onaylı çapa referansları yeniden eklenir;
  önceki karenin çıktısı yeni kareye girdi yapılmaz (hata zincirlenir). Bellek ve proje talimatı pikseli kilitlemez; kısıt her promptta yazılır.
- **İki karakter aynı karede:** her biri numara + rol + **kadrajdaki yeri** + kendi kimlik cümlesiyle:
```text
Reference 1 (pilot): take his face and the ivory suit with one plain orange band on each upper arm from it; he sits on the left of the frame.
Reference 2 (engineer): take her face and the pearl-white suit with one plain turquoise band on each upper arm from it; she sits on the right of the frame.
```
- Yükleme sırası = `EKLE` satırı = NOTLAR'daki kayıt.

---

## 4 · Giysi ayrıntısı: sayıyla, dokuyla, renkle

Kayma çoğunlukla modelin "astronot giysisi" ön bilgisinden gelir: mavi ajans rengi, çok şeritli teknik giysi, bayrak, arma, yazı.
Önlem olumlu ve sayılı tariftir:

| Kötü | İyi |
|---|---|
| `turquoise arm stripes` | `one single plain turquoise band around each upper arm, smooth and seamless` |
| `astronaut suit with badge` | `a small triangular gold-and-blue badge on the left chest, the only marking on the suit` |
| `helmet with visor` | `a round white helmet with a large clear visor; her face is clearly visible through it` |

- "the only marking on the suit" / "smooth, unmarked chest and sleeves" cümleleri (sahibin EVA blokları, `GPT_IMAGE_OMNI_KILAVUZU` Ek A) bayrak ve armaya karşı olumlu kilittir.
- **Görsel promptta dışlama satırı** (`No text, logos, flags or watermarks.`): OpenAI'ın kendi örneklerinde var ("No logos", "No watermarks", "No text").
  Hat kuralı bugün olumsuz bloğu yasaklıyor → **sahip kararı** (`ARASTIRMA/11` §D K2 · `13` §D). Karar gelene kadar yalnız olumlu kilit.

---

## 5 · Kareden videoya kayma

- Başlangıç karesi doğru, video içinde kayıyorsa: **yavaş ve tek** kamera hareketi (sabit, yavaş itme, yavaş kaydırma); karakterin kendi etrafında dönmesi ve hızlı pan kaymayı artırır.
- Kayma hareketin belli bir anında başlıyorsa: o andan önceki **kullanılabilir aralık** seçilir (SECIM §3).
- Video girdisine kimlik referansı (Gemini uygulaması 5 görsel) ya da Omni'ye 3 s video referansı eklemek: resmî olarak var, etkisi **ölçülmedi** (PROB). Önce tek kareyle dene.
- Vizör videoda opaklaşıyorsa promptta vizörü ve görünen yüzü olumlu yaz; hâlâ oluyorsa yüz yakın planı yerine orta plan.

---

## 6 · Düzeltme

- **Kare aşamasında kayma** → kare düzeltilir, video promptuyla telafi edilmez.
- Tek kusur, korunacaklar sayılır (OpenAI: "change only X + keep everything else the same"):
```text
Edit the supplied frame. Change only the band on her left upper arm: make it one single plain turquoise band matching Reference 2.
Keep her face, helmet, suit texture, pose, the lighting, the camera angle and the background exactly as they are.
```
```text
Edit the supplied frame. Remove only the flag on his right shoulder; the shoulder becomes the same smooth white fabric as the rest of the suit.
Keep everything else exactly as it is.
```
- Ardışık düzenleme korunan ayrıntıyı da aşındırır: her sonuçta yüz ve geometri yeniden kontrol edilir.
- **Seçimli/maskeli düzenleme** (ChatGPT seçim aracı; API'de alfa kanallı maske, ilk görsele uygulanır) değişikliği bölgeyle sınırlar; tam kare düzenlemeye tercih edilir.
  API'de `input_fidelity` girdinin ayrıntısını ne kadar koruyacağını ayarlar; 2.5'teki değerleri ölçülmedi (`FLOW_GERCEKLERI` Ek 3).
- Renk adının yanına hex kodu (`#40E0D0`) yazmak: kaynaksız, kareye yazı olarak basılabilir → PROB, varsayılan değil.
- **İki kontrollü düzeltmede düzelmediyse** kare yeniden üretilir (rol cümlesi ve tarif güncellenerek). AGENTS §4.

---

## 7 · P17 deneyi — panel mi, tek görünüş mü (bir sonraki filmin pilotunda)

Tek değişkenli ve ucuz tasarım (`ARASTIRMA/13` §B2):

1. Filmin bir karakteri için hat biçiminde **panel sayfası** üret (önden · yandan · arkadan · yüz yakın).
2. Aynı sayfanın panellerini **kırparak** ayrı dosyalara kaydet (yeni üretim yok → tek değişken biçim).
3. Beş zor çekim: dar koridorda orta plan · arkadan · vizör kapalı dış mekân · eldiven panelde · yan ışıkta yüz yakın.
4. Her çekimi iki kurulumla üret: (A) panel sayfası tek referans · (B) önden + arkadan kırpılmış iki dosya. Aynı prompt, aynı sıra.
5. Değerlendir: bant rengi (§8 ΔE₀₀), şerit/rozet sayısı, kopya figür, panelden sızma, yüz (göz). 10 kare, sahibin gözü + Fable'ın kare incelemesi.
6. Sonuç `SMOKE_TEST.md` Sonuçlar'a; fark açıksa referans kuralı sahibe sorulur.

---

## 8 · Ölçüm

| Ölçüt | Ne yakalar | Kask altında | Durum |
|---|---|---|---|
| **Bant rengi ΔE₀₀** (CIEDE2000): referans karedeki bant bölgesi ile yeni karedeki bant bölgesinin ortalama rengi | turkuaz → mavi kayması | kasktan bağımsız ✅ | yöntem KABUL · eşik ◐: ≤2 kabul, ≥3 kayma (renk endüstrisi değeri, kanalda kalibre edilir) · araç `kareler.py`'ye eklenmesi **sahip kararı** |
| Şerit, rozet, bayrak, yazı | sayı ve varlık | ✅ | göz (sahip + Fable kare incelemesi) |
| Yüz benzerliği (ArcFace) | başka yüz | vizör yansımalı ya da kapalıysa çalışmaz | PROB, kurulu değil |
| Genel görünüş (DINO vb.) | — | — | hat dışı |

---

## 9 · Kare kabul listesi (videoya göndermeden önce)

1. Yüz referanstaki kişi mi (yaş, yüz biçimi, saç; vizör ardında okunuyorsa).
2. Kol bandı rengi ve **sayısı** referansla aynı (gerekirse ΔE₀₀).
3. Giysi, kask ve sırtta **istenmeyen bayrak, arma, yazı, logo yok**.
4. Rozet biçimi ve konumu (hangi göğüs) referansla aynı.
5. Kask tipi ve vizör (şeffaf/opak, tek parça) doğru.
6. Kadrajda fazladan figür ya da kopya yok.
7. Beden oranı ve sırt ünitesi referansla uyumlu.
8. Eldiven: beş parmak, bilek bağlantısı bozulmamış; temas noktası görünür.
9. Önemli nesne (alet, kapak, kol) doğru biçim ve **durumda**.
10. Oran 16:9 piksel ve PNG (`GPT_IMAGE_OMNI_KILAVUZU` §13); ışık yönü mekân master'ıyla aynı; saf siyah alan yok, eller tam görünür ya da kadraj dışı;
    hareketsiz kalacak kablo/bağ sabit (`GPT_IMAGE_OMNI_KILAVUZU` §6).

Bir madde "hayır" → §6 düzeltme. Kare NOTLAR'a `kare/Cxx.png · ref 1,5 · ✅` diye yazılır.

---

> **Bu dosya ne zaman değişir:** P17 sonucu gelince §2-§3; sahip K2'ye karar verince §4; ΔE₀₀ aracı eklenince §8. Kaynaksız satır girmez.
