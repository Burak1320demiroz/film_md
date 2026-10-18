# 🛰️ UZAY FİZİĞİ GÖRÜNTÜDE KILAVUZU — vakum, ağırlıksızlık, yörünge: karede nasıl görünür, promptta nasıl yazılır

> **Ne için:** dört filmde vakumda duman ve ateş topu, kabinde ve vakumda aşağı damlayan sıvı, 0 g'de 1 g yürüyüş, ters itki, iticisiz yükselme,
> hızlı dönen Dünya görüldü (`ARASTIRMA/11` §B). Video modelleri yeryüzü fiziğini taşır; bu kılavuz her olgu için **kamerada görünen** ve
> **promptta yazılan** cümleyi verir.
> **Kim okur:** goruntu-yonetmeni · teknik-danisman · bilim-danismani · yonetmen (kadraj çözümü) · Fable · sahip (F7 kare kabulü).
> **Kaynak:** `ARASTIRMA/ham/29` → `ARASTIRMA/13_SUZME_20261016.md` §B3. Tamamlayıcı: `GOSTERIM_COZUMLERI.md` · `BILINEN_TUZAKLAR.md` ·
> eski hattın efor/yerçekimi kılavuzu (donmuş; okunur).
> **Tarih:** 16.10.2026. Kılavuz bilim makalesi değildir; kurgusal teknoloji (yapay yerçekimi, canlı sıvı) serbesttir, yalnız filmin kendi kuralına tutarlılık istenir.

---

## 0 · Dört filmden

| Görülen | Çekim | Doğru olan |
|---|---|---|
| istasyon ağzından siyah baca dumanı · roket alevi "dumanlı kamp ateşi" · kararan cephe volkanik kül gibi | PLANET C17/C22 · SKY C20/C24 (QA no. → plan C21/C24) | §2 |
| halkadan aşağı damlayan sıvı · kapalı kokpitte tavandan su · kablodan su damlası | MAYDAY C06/C18/C19 (QA montaj no. → hat C07/C19/C20) | §3 |
| 0 g'de 1 g yürüyüş ve basış · kapağı açarken diz çökme, tepki yok · kol çekişinde efor yok | SKY C07/C08/C10/C11/C16 · MAYDAY C19 (QA no. → SKY plan C09/C09/C11/C12/C19 · MAYDAY hat C20) | §4 |
| gemi kendi motor ateşinin yönüne kayıyor · mekik iticisiz yükseliyor · ateşlemede kokpitte ivme yok | MAYDAY C20 · PLANET C06 · SKY C19 (QA no. → MAYDAY hat C21 · SKY plan C20) | §5 |
| Dünya 6 s'de gece-gündüz çizgisi geçecek hızda dönüyor · kıtalar zıplıyor | WRONG_BURN C03/C07b · PLANET C24 | §6 |

---

## 1 · Üç ilke

1. **Fizik kareden başlar.** Doğru nozul, havada duran küre, tutamağı tutan el başlangıç karesinde varsa model onu taşır. Yanlış kare video promptuyla düzelmez.
2. **Olumlu tarif.** Video promptunda "no smoke" değil, istenen görüntü yazılır (hat kuralı; olumsuz ifadenin etkisi P13'te ölçülecek).
   Promptta **sayı yazılmaz** (7.8 km/s, 0.05 m/s): model hızı sayıdan anlamaz, rakam kadraja basılabilir (`BILINEN_TUZAKLAR` §C).
3. **Gösterilemiyorsa gösterme.** Temas ya da fizik anı tutmuyorsa: o andan önce kes, kadraj dışında bırak, sonucu göster (`GOSTERIM_COZUMLERI`).
   Video modelleri akışkan, momentum ve temas fiziğinde zayıftır (VideoPhy-2, PhyGenBench).

---

## 2 · Vakumda itki ve patlama

| Gerçek | Kamerada | Sık hata |
|---|---|---|
| Dış basınç yok: egzoz nozulda hemen geniş açıyla açılır; çoğu yakıtta neredeyse görünmez ya da soluk, kısa | nozulda kısa parlak çekirdek, arkasında hızla dağılan geniş, saydam, soluk bulut; manevra iticisinde kısa soluk "puf" | turuncu ateş topu · kara duman bulutu · uzun alev sütunu |
| Vakumda patlama ateş topu yapmaz | kısa ışık parlaması, hızla genişleyen soluk buhar kabuğu, düz çizgide dağılan parçalar | mantar bulutu, yuvarlanan alev |

```text
A short bright core at the nozzle and a wide, pale, translucent plume that fades within a second into the black.
```
```text
Two brief pale puffs from the forward thrusters, gone almost as soon as they appear.
```
- Kararan güneş/enerji cephesi gibi kurgusal karanlık: duman ya da kül değil, **ışıksız keskin bir sınır** (PLANET C17).
- Duman ancak **basınçlı** bir hacimden dışarı kaçan gaz ise ve o da hemen buz kristaline döner (§3).

---

## 3 · Sıvı, parçacık, buz

| Ortam | Gerçek | Kamerada |
|---|---|---|
| Ağırlıksız basınçlı kabin | serbest sıvı **küre** olur, havada asılı durur ya da sabit hızla süzülür; yüzeye değince yapışır ve yayılır | titreşen saydam küreler; **aşağı düşen damla yok**; zemine akış yok |
| Vakum | sıvı anında kaynar ve donar | parlak buğu ve buz kristali bulutu, hızla dağılır |
| Her ikisi | parçacık, kıvılcım, buz kuvvet yoksa **düz çizgide sabit hızla** gider | düz parlak izler; kavisli düşüş yok |

```text
A trembling sphere of water hangs in the cabin air, drifting slowly sideways; where it touches the panel it clings and spreads.
```
```text
The liquid bursts into a glittering cloud of ice crystals that spreads in straight lines and thins out into the dark.
```
- Kurgusal canlı sıvı (MAYDAY) halkayı sararsa: gergin, pürüzsüz bir kordon; serbest damla yok.
- Kapalı kokpit kuru basınç kabinidir: **su damlası, yağmur, sızıntı karede ve promptta yazılmaz** (MAYDAY C19 → hat C20 — ARASTIRMA/16 §E).
- Sıradan izleyici **aşağı düşen damlayı** fark eder; vakumda anlık kaynamanın eksikliğini yalnız uzman fark eder → öncelik düşen damlada.

---

## 4 · EVA ve beden

| Gerçek | Kamerada |
|---|---|
| Uzayda yürünmez: **tutamaktan tutamağa** elle ilerlenir; çalışırken botlar **ayak kilidinde** | eller sırayla tutamak kavrar, gövde yavaşça süzülür; ayaklar boşta ya da kilitte |
| Emniyet bağı her an bir noktaya bağlı | bağ gevşek kıvrımlarla süzülür; tel gibi kaskatı değil |
| İten geri gider (etki-tepki); giysili astronot ağırdır, yavaş başlar yavaş durur | bir şeyi itince beden geri kayar; diğer el tutamakta; ani duruş yok |
| Efor | kol omuzdan çeker, gövde karşı tarafa döner, mekanizma sert durdurucuya oturur |

```text
She moves along the hull hand over hand, each glove closing on the rail before the other lets go, her body drifting slowly behind her
arms and her tether curling loosely in the black.
```
```text
Her left glove grips the platform rail while her right arm swings the hatch up; her body eases back a little against the pull.
```
- Başlangıç karesinde ayak yere "basıyorsa" model yürütür: kare **tutunma pozuyla** kurulur (bir el tutamakta, ayaklar kilitte ya da boşta).
- Yürüyüş gibi okunan geçişleri kesmeyle at: tutundu → (kesme) → zaten hedefte.
- İç mekânda (yapay yerçekimi yoksa) aynı kural: tutunarak süzülme.

---

## 5 · Araç hareketi ve kokpit

| Gerçek | Kamerada | Sık hata |
|---|---|---|
| Burun yönü ≠ hareket yönü; motor kapanınca araç aynı hızla sürer | araç yan dönükken de aynı çizgide süzülür | itki kesilince durma, uçak gibi yatarak dönüş |
| İtki gemiyi **egzozun tersine** iter | alev sağa bakıyorsa gemi sola gider | gemi kendi alevinin yönüne kayıyor (MAYDAY C20 → hat C21) |
| Yükselmek/kalkmak için itki gerekir | hareket yönünün tersine soluk itki | iticisiz asansör gibi yükselme (PLANET C06) |
| Ateşlemede gövde koltuğa basılır; kesilince serbest kalır | ateşleme anında omuzlar arkalığa gömülür; kesilince kayışlar ve eller hafifçe kalkar | ivmede hiçbir tepki yok (SKY C19 → plan C20) |

```text
The thrusters on its right side glow and the ship slides steadily to the left, away from the glow.
```
```text
As the engine lights, both pilots sink back into their seats and the cabin shudders; when it cuts, their straps lift gently.
```
- Promptta **itki yönü ile hareket yönü aynı cümlede** yazılır; başlangıç karesinde nozul ve itki yönü görünür.

---

## 6 · Yörünge, Dünya ve ışık

| Gerçek | Kamerada |
|---|---|
| Alçak yörüngede yer izi ≈7,2 km/s: **10 s'de ≈72 km** (`ARASTIRMA/13` V23) | tam altta ≈1°/s; ufka doğru daha yavaş: bulutlar ve kıyı **yavaş, sabit, pürüzsüz** kayar |
| Bir tur ≈90 dk; gündüz-gece sınırı ancak dakikalarla yaklaşır, güneş diski birkaç saniyede batar | 10 s'lik çekimde gece-gündüz çizgisi kadrajı geçmez |
| Kıta biçimi ve yönü aynı yörünge geçişinde değişmez | ardışık iki çekimde aynı kıyı, aynı yön |

```text
Far below, the curved Earth drifts slowly and steadily beneath the station, its clouds sliding by without a shudder.
```
- Hızlı dönen Dünya'yı modelin "time-lapse" ön bilgisi üretir: "slowly and steadily" yazılır; dönüşü kamera hareketiyle karıştırmamak için kamera sabit tutulur.
- Gezegen yerleşimi (ufuk eğrisi, ışık yönü, hangi kıyı) mekân master'ında bir kez sabitlenir (`GPT_IMAGE_OMNI_KILAVUZU` §5).
- Sıradan izleyici Dünya'nın gerçek hızını bilmez, ama **bir çekimde döndüğünü** fark eder → kural "yavaş ve sabit", sayı değil.

---

## 7 · Kenetlenme ve temas

- Yaklaşma neredeyse durarak; temas yumuşak, **sekmesiz**; halka önce yumuşak tutar, sonra kilitlenir.
- Bir klipte yaklaşma + temas + kilit istenmez: C01 coğrafya (boşluk var) · C02 halkalar zaten hizalı, kısa düz ilerleme, düz oturma · C03 insan tepkisi · C04 bağlı gövdeler (`GPT_IMAGE_OMNI_KILAVUZU` §10).
```text
The two collars, already aligned, close the last hand's width so slowly they barely seem to move, meet flush and hold still.
```

---

## 8 · Prompt dönüşüm dizini

| Kaçınılacak | Yerine (İngilizce, olumlu) |
|---|---|
| smoke, billowing smoke, fiery plume, burning exhaust | a short bright core at the nozzle and a pale translucent plume that fades within a second |
| explosion, fireball (vakumda) | a brief flash, a thin pale vapour shell expanding fast, fragments flying in straight lines |
| walking, steps, stands on the hull (0 g) | moves hand over hand along the rail · boots locked in the foot restraint · drifts |
| water dripping, leaking, rain, spilling (kabinde) | a trembling sphere of water hangs in the air · clings to the panel |
| liquid falling (vakumda) | bursts into a glittering cloud of ice crystals |
| stops, turns like a plane | coasts on at the same speed · brief puffs from the forward thrusters to slow down |
| fast moving Earth, time-lapse clouds | the curved Earth drifts slowly and steadily below |
| bumps, crashes into the station | closes so slowly it barely seems to move, meets flush and holds still |
| sayı: 7.8 km/s · 78 km · 0.05 m/s | yazılmaz — "slowly and steadily" · "barely seems to move" |

---

## 9 · Kontrol listesi

**Başlangıç karesi:**
1. Nozul ve itki yönü görünür; dumanlı alev yok.
2. Kabinde sıvı varsa küre ve askıda; su/yağmur/sızıntı yok.
3. EVA'da tutunma pozu: en az bir el tutamakta ya da bot kilitte; "basan" ayak yok.
4. Emniyet bağı gevşek ve bir noktaya bağlı.
5. Dünya yerleşimi master'la aynı (kıyı, yön, ışık).

**Video promptu ve deneme:**
6. İtki yönü ile hareket yönü aynı cümlede ve tersine.
7. Dünya "slowly and steadily"; çekimde dönmüyor.
8. Temas ve kilit ayrı planlarda; sekme yok.
9. Ateşleme ve kesilmede bedende tepki var.
10. Promptta sayı ve olumsuz ifade yok.

Öncelik: sıradan izleyicinin fark ettiği hata (düşen damla, uzayda yürüme, dumanlı alev, dönen Dünya, ters itki) önce; yalnız uzmanın fark ettiği (kesin hızlar, anlık kaynama) sonra.

---

> **Bu dosya ne zaman değişir:** P13 (olumsuz ifade) ölçülünce §1-§8; filmde yeni bir fizik hatası iki filmde tekrar ederse sahip onayıyla. Kaynaksız satır girmez.
