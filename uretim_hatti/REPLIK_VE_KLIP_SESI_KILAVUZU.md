# 🎙️ REPLİK VE KLİP SESİ KILAVUZU — diyalog filme girer, klip sesi kontrolsüz girmez

> **Ne için:** dört filmin üçünde diyalog hiç filme girmedi, dördünde vakumda klibin kendi sesi duyuldu (`ARASTIRMA/11` §B). Bu kılavuz
> diyaloğun nasıl seçileceğini, ne zaman hazır olacağını ve klip sesinin nasıl yönetileceğini söyler.
> **Kim okur:** ses-tasarimcisi · diyalog-yazari · kurgucu · goruntu-yonetmeni (model sesi repliği) · Fable · sahip (F7-F8).
> **Kaynak:** `ARASTIRMA/ham/27` → `ARASTIRMA/13_SUZME_20261016.md` §B1. Tamamlayıcı: `GECIS_VE_SES_SUREKLILIGI.md` (yatak, geçiş) ·
> `GPT_IMAGE_OMNI_KILAVUZU.md` §11 · `FLOW_GERCEKLERI.md` §4, Ek 2.
> **Tarih:** 16.10.2026.

---

## 0 · Dört filmden

```
"Kurguda kaydedilecek" denen 3 film   kayıt hiç yapılmadı → izleyici amacı anlamadı ("Kopuk" · "sabotaj mı tamir mi" · "48 yolcu" yok)
Model sesli tek film (MAYDAY_SEA)      anlaşıldı; ama iki erkek ses aynı tonda karıştı, bir replikte takılma, alıcı sesinde dudak aralık
Dört filmde                            vakumda çarpma, whoosh, rüzgâr, dalga, motor, model hecesi — klibin kendi sesi
Neden                                  montaj kurgu.py dışında yapıldı; kurgu.py klip sesini zaten varsayılan olarak ATIYOR
```

---

## 1 · Film başında seçim — her replik için kaynak

`FILM.md` §5'in Kaynak sütunu her replik için şu üçünden biridir. Seçim F4'te yapılır, sonra değişirse NOTLAR'a yazılır.

| Kaynak | Ne zaman | Risk |
|---|---|---|
| **model sesi** (Omni videoda söyler) | kısa, tek konuşmacı; yüz kadrajda ya da kısa telsiz cümlesi; filmde az konuşan | aynı ses her klipte gelmeyebilir (P18) · kelime atlama/takılma · iki rolü aynı tonda verme · alıcı sesinde kadrajdaki ağız oynayabilir |
| **kayıt** (sentetik ses ya da insan) | hızlı karşılıklı konuşma · yüzü görünmeyen konuşmacı (kask, telsiz, iç ses) · uzun filmde aynı ses · aksan/ton kontrolü · iki benzer ses (iki erkek) | **yapılmadan montaja geçilmesi** (3/3 filmde oldu) |
| **karma** | ortam ve mekanik ses yataktan, ana diyalog kayıttan, kısa ağız-kadraj repliği klipten | iki ortamın ve müziğin üst üste binmesi |

- Aynı konuşmacının bütün satırları **tek kaynaktan** gelir. Model sesi bir satırda tutmazsa o konuşmacının bütün satırları kayda geçer (P18 kuralı).
- Sentetik ses aracının ticari koşulu araca ve plana bağlıdır; araç seçimi sahibindir. Google çıktılarının ticari koşulu `FLOW_GERCEKLERI` §6'da BİLİNMİYOR.

---

## 2 · Montajdan önce: ses hazır mı (kapı)

Bu yedi madde "evet" değilse taslak montaj açılmaz, izleyiciye gösterilmez. (SECIM_VE_KURGU §9 aynı kapıyı kullanır.)

1. `FILM.md` §5'teki her replik için **dosya var**: kayıt ise `~/film_medya/<FILM>/ses/R<nn>.wav`; model sesi ise seçilen denemenin aralığı NOTLAR'da.
2. Her replik **10 s'lik parçasına sığıyor**: plan 2-2,5 kelime/saniye; telsiz ve kask içi konuşma yavaş ve aralıklıdır, 10 s'ye 12-20 kelime.
3. Kelimeler senaryoyla aynı (kulakla; Whisper kurulursa yazıya dökerek, §6).
4. Konuşanlar **sesle ayırt ediliyor** (iki erkek, iki kadın aynı tonda değil); gerekirse biri telsiz filtreli, öbürü kask içi.
5. Her mekânın **yatağı** hazır (§4) ve `timeline.json` `yataklar`'da.
6. Klip sesi açık olan parçalar yalnız model sesi repliği taşıyanlar (`klip_sesi: true`); geri kalanların hepsi kapalı.
7. Montaj `kurgu.py taslak` ile yapılıyor ya da başka programda yapılıyorsa klip izleri **kapalı** başlıyor.

---

## 3 · Model sesi repliği

- Replik video promptuna birebir yazılır; biçim hattın kuralıyla: `she says: <line>` (iki nokta, tırnak yok; Vertex: tırnak ekrana yazı bastırabilir). Gemini API tırnak öneriyor; P9'a kadar ikisi de kabul (`FLOW_GERCEKLERI` §4).
- **Tek konuşmacı** tarif edilir; kadrajdaki öteki kişinin ağzı kapalı yazılır. Alıcıdan/telsizden gelen seste kadrajdaki kişinin ağzı kapalıdır.
- Ses tarifi kısa ve aynı kelimelerle: `a calm adult male voice over a helmet radio`. Metin tarifi ses kimliği kilidi değildir.
- Kontrol (her deneme): doğru kelime · doğru kişi · fazladan konuşma, mırıltı ya da müzik yok · takılma yok · ağız doğru.
  Takılma ya da yanlış kelime varsa önce aynı klibin **başka denemesi**, sonra o konuşmacının satırları kayda geçer. Görüntü iyiyse yeniden üretilmez; ses değiştirilir.
- Omni'nin kelime doğruluğu ve "no music"e uyması tek blogda iddia edildi; ölçülmedi (P18).

---

## 4 · Klip sesi ve vakum

**Varsayılan: klibin kendi sesi filme girmez.** `kurgu.py taslak` bunu zaten yapar; yalnız `klip_sesi: true` parçaların sesi çalar.
Başka bir kurgu programı kullanılırsa video izlerinin sesi kapalı başlar, model sesi repliği aralığı tek tek açılır.

**Vakumda ne duyulur:**

| Duyulur | Duyulmaz |
|---|---|
| kask içi: nefes, fan, soğutma akışı, giysi sürtünmesi | dışarıdan hava taşıyan ses: rüzgâr, whoosh, patlama gürültüsü, dalga |
| gövde/giysi iletimi: eldiven ya da bot bir yapıya değince **boğuk, alçak** tık ve gümbürtü | yankılı metal çınlaması, uzaktaki bir şeyin sesi (temas yoksa) |
| telsiz: konuşma, bip, hışırtı | — |
| müzik (sahne dışı) | — |

- Dış uzay planında temas yoksa ses yalnız kask içi + telsiz + müziktir. Motor ateşi dışarıdan duyulmaz; **içeriden** (kokpitte, gövdeye bağlıyken) titreşim olarak duyulabilir.
- Tam sessizlik izleyiciye arıza gibi gelebilir; vakum hissi kask içi yatakla ve alçak titreşimle verilir.
- Model sesi repliğinin arkasında vakuma aykırı ses varsa: önce başka deneme; yoksa yalnız replik aralığı alınır, kazancı düşürülür, yatak altta sürer. Kaynak ayırma (Demucs vb.) kurulu değil, gerekirse sahip kurar (PROB).

---

## 5 · Telsiz ve kask içi ses (kayıtta)

Başlangıç değerleri; kulakla ayarlanır, ölçülmüş eşik değildir:

| Katman | Değer |
|---|---|
| Telsiz bandı | alt kesim ~300-400 Hz · üst kesim ~3-3,5 kHz |
| Kask içi yakınlık | 150-250 Hz'e +2-3 dB · çok kısa oda (5-12 ms) |
| Bip | konuşma başında kısa (≈50 ms), ~1 kHz; her satırda değil, kanal açılışında |
| Hışırtı | konuşma altında ~−36 dB; konuşma bitince kesilir |

- Konuşanları ayırmak için biri telsiz bandında, öbürü kask içinde; ya da iki farklı ses.
- Replik kesmeden ~0,5 s önce başlar ya da sonra biter (J/L) — `GECIS_VE_SES_SUREKLILIGI`.
- Film sonu yüksekliği `kurgu.py yukseklik` (−14 LUFS · ≤ −1 dBTP). Konuşmayı telefon hoparlöründe de dinle.

---

## 6 · Doğrulama

| Ne | Nasıl | Kim |
|---|---|---|
| Ses var mı, nerede sessiz | `ffmpeg -i <dosya> -af silencedetect=n=-50dB:d=0.5 -f null -` | Fable |
| Vakum planında klip sesi | aynı komutla klip sesinin düzeyi; `klip_sesi` kapalıysa gerek yok | Fable |
| Yükseklik | `kurgu.py yukseklik` | Fable |
| Replik kelimeleri | kulak; ya da `faster-whisper` ile yazıya döküp senaryoyla karşılaştırma (kurulum sahipte, `ARASTIRMA/13` §D A1) | sahip / Fable |
| Ses kimliği, ton, kim konuşuyor | **kulak** | sahip |

Fable sesi duyamaz: kelime ve kimlik kararı sahibin kulağındadır; Fable düzey, sessizlik ve (Whisper varsa) kelime ölçer.

---

> **Bu dosya ne zaman değişir:** P18 (model sesi tutarlılığı) ve P9 (konuşma biçimi) ölçülünce §3; Whisper kurulursa §6. Kaynaksız satır girmez.
