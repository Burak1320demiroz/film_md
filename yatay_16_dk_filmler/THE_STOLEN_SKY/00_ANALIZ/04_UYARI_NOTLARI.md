# ⚠️ THE_STOLEN_SKY — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md` (bu filmde ne var).
> **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı. **Yazıldı:** 20.09.2026.
> ⛔ Her satır ÜÇ şeyi taşır: **hangi sahne · hangi ölçülmüş kayıt · ne yapılacak.**
> "durum" sütunu: ✅ = kapama kararı yazıldı ve 05 tablosuna/prompta indi · 🔶 sahip · ⏳ üretimde ölçülür.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S01 · S22 · S26 · S36 · S40 · S48 · S72 | D192 (OPEN CIRCUIT şimşek) · 03_PLAN_ONCESI A5 | kalkan sapması sıfatla kalırsa model "sapan ateş" yerine patlama/ışık huzmesi üretir; taktik zinciri (S22 → S40 → S48) okunmaz | POZİTİF biçim sayıyla her kalkan promptunda: `four bright points leave the tool, meet the curved amber shield face-on and glance off to the side in under half a second, striking the parapet two body-lengths from the soldier; no glow lingers` — kalkan yönü NESNEYLE (`its curve toward the shooter`); S22'de profil + `the open side away from the shield` | ✅ (02 §5 A5) |
| 2 | S59 | D141 · D213 · KART 12 · red defteri PB (YERÇEKİMİ S8) | ölüm okunmazsa BEDEL yok (D202); kompozisyon reddi (yüzsüz iki figür + uzun tüp + kalkık kol) sahneyi ÜRETİLEMEZ bırakır | üç işaret aynı klipte (silah düşer · beden kasadan kayar · ışık söner) saniyeli; nötr tarif 02 §6; kamera kafes ardı R, göz hizasına yakın, uzak duvar çapa; **iki red → kadraj değişir** (kafes teli önde, figürler ard arda), üçüncü yeniden yazım YOK; P6 denemesi FAZ 3 | ✅ / ⏳ P6 |
| 3 | S84 · S81 | D202 (5 film görünmez seçim) · D179 (imaj sonucu yazdı) · COUNTED TURN ⑩ 3,4 | seçim bedende okunmazsa "kamera taşıyıcı"; imaj promptu kolu çevrilmiş yazarsa hareket hiç olmaz | S81 imaj: el kolun ÜSTÜNDE, C-0 ikonu canlı · S84 imaj = S81 son karesi (el kolda, henüz çevirmedi) · S84 video 0–1 s'de tek kararlı çeviriş; ÇAPA BEFORE/AFTER aynı kanal (el); reddedilen kol S85'te kadrajda | ✅ (96 klip REV 2) |
| 4 | S00 | D157 · D211 · KRONOS ⑫ | tek karede örgü + gemi + savrulma okunmazsa novum yok; ilk 10 s soru yok | imaj: gemi örgüye bir gövde boyu yaklaşmış (temas 0–2 s); kafes örgüsü ile halka AYRI şekil; kart 0 s; S95 aynı harf A | ✅ |
| 5 | S13 · S59 · S64 · S84 · S86/S87 · S93 | SAHNE_ZINCIRI §1 · KILAVUZ §7 (dynamic attribute 0,0687) | ışık/ikon sönmesi, örgü kapanması, kapı kilitlenmesi klip içinde NİTELİK değişimi → model donduruyor | ikili durum + sürekli HAREKET: S13 örgü kapanır (çizgiler uzar = hareket) · S59 ışık son 1 s'de söner, asıl hareket silahın düşüşü · S64 modül ışığı 0–2 s'de söner, sonrası kilit mekaniği HAREKET · S84 ikon söner + kol çevrilir (hareket) · koridor açılışı SINIRDA (S86 son kare kapalı ↔ S87 ilk kare açık) · S93 kapanma ilk 2 s | ✅ |
| 6 | S51 · S52 · S55 · S57 · S58 · S59 | D207 (MARS S15 iki bacakla koştu) · FALLING WORLD ⑧ | Bor'un topallaması kesmede sıfırlanır | her Bor klibinin IMAGE SUBJECT satırı: `weight on the left boot, the right knee locked, the right knee plate cracked` (S51 sonundan kopya); yorgunluk 4→6; tablo SON = sonraki BAŞ | ✅ |
| 7 | S29 → S33 → S62 → S66 → S68 · S78 · S90–S95 | D42 (MARS is sıfırlandı) · HARD DOCK ② kumanda kolu değişti | K-1 hasarı kaybolur / sağ-sol değişir | KİMLİK DİZİSİ araç satırı: `right thrust ring canted` S29+ · `a steel clamp on the right ring` S66+ · `rear sensor spur missing` S90+; sağ bilezik kadrajdaysa satır BİREBİR; referans sayfa ③ üç durum | ✅ |
| 8 | S23↔S24 · S47↔S48 · S71↔S72 | MARS §①.11 sınır satırı yok · README PART kör noktası | ② hiçbir part masterda çifti göremez | her bölüm dosyasında End/Start satırı; SPEC B üç EŞ KADRAJ satırı; S48 ve S72 küme (Z) — sınır çiftinin ilk karesi = öncekinin son karesi (elle kare kapısı basit) | ✅ |
| 9 | S38 · S39 | red defteri PB (COLD BURN S28 "bedenden çıkarma") | anahtarın subayın kolundan çıkarılması "bedenden bir şey çıkarma" imzası | anahtar KOL YUVASINDA açık klipsle başlar (S38 son kare); Ada yuvadan ÇEKER (nesne bedenden değil YUVADAN); düşen figür kadrajda yalnız kol/omuz | ✅ |
| 10 | S58 · S94 · S39 · S43 · S63 · S66 · S84 · S85 | PROMPT_HATA §3b (temas 2–4 s bandı en kötü) · COUNTED TURN 7 🔴 | temas füzyonu (eldiven-kol, eldiven-kemer, modül-yuva) | temas İLK KAREDE kurulu ya da ilk 2 s; adlandırılmış ARA KATMAN (sert manşet halkası · kemer tokası · yuva kenarı · kol muhafazası); cümle iki yönlü | ✅ (REV 2: S58 el zaten kolda) |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S03 · S30 · S51 · S58 · S66 · S78 · S79 · S86 | D206 · D169 · FALLING WORLD ⑧ 6,0 | efor faturası 0 | ≥1 ödeme satırı saniyeli, eldiven üstünde, simetrik yük, kadans düşüşü; ⑧ EFOR ölçer | ⏳ |
| 2 | S00 · S25 · S40 · S48 · S87 · S95 (lockoff) | D210 · FALLING WORLD ⑨ lockoff 19/23 · KRONOS creep | kilitli kamera klip sonunda yaklaşır | `absolutely zero camera movement` + TIMELINE son satırı `hold`; ⑨ LOCKOFF HELD ölçer | ⏳ |
| 3 | S12 · S13 · S19 · S24–S29 · S31 · S77 · S80 · S87–S91 · S93 · S95 | KART 10 · COLD BURN S8 yapısal red | insansız + uzun NEGATIVE → "yerine getirilemez" | NEGATIVE tek pozitif Style satırına iner; `Exactly 0 human` yazılmaz; boş kadraj varlık olarak | ✅ yazım / ⏳ üretim |
| 4 | S09 · S44 · S60 · S70 (C-0) | HARD DOCK ⑩ (dış dizi tırmanışı böldü) · D209 (yörünge promptlarına çapa inmedi) | Serrak planları Mara'nın yayını böler; C-0 dünyası her seferinde başka | C-0 Bible tek cümle + maket + sabit halka BİREBİR; her C-0 klibi ≤10 s ve hemen Mara'ya döner; ⑩ ölçer | ⏳ |
| 5 | S14–S18 · S63–S67 | KRONOS ⑫ konsol platosu · HARD DOCK ⑫ LEAVES AT 00:25 | hazırlık üçlüsü orta bölüm terkine yol açar | ölçek+ses kırıcı her kesmede (03 tablosu) · S19 drone araya · tam-film ⑫ Plateau ölçer | ⏳ |
| 6 | S25 · S40 · S48 · S89–S90 (ilişki planları) | KRONOS ① çift karakter spawn · IKI_KISI §6 ④ | iki Veyra / üç araç aynı kadrajda kimlik sızması | HUMAN/FIGURE COUNT rakamla + KONUM KİLİDİ (sol/sağ üçte bir) + kararlı kamera; ② ölçer | ⏳ |
| 7 | S94 | D198 · D200 | kemer ucu statik askı ya da 1 g düşüş | `drifts in a straight line while turning slowly on its own axis`; üç figür kemerli; ⑥ ölçer | ⏳ |
| 8 | S93 · S95 · S92 dış | PROMPT_HATA §4 (vakumda ses prompt kapatamıyor) | motor dış ses uydurur | AUDIO satırı yazılır ama kabul KURGUDA: dış ses 0, telsiz/kabin perspektifi; tam-film ③ | ⏳ kurgu |
| 9 | bütün CU/MS silahlı planlar (S01 · S07 · S20 · S37 · S57) | POLİTİKA §3 imza ⑥ (kask + sivri form) · §3.2 kadraj daraldıkça doku | "silahlı maskeli figür" okuması | her CU/MS'e çevresel çapa (`the far grey wall of the bay is visible behind him`); silah adı yok, form tarifi; iki red → kadraj | ⏳ P6 |
| 10 | S06 · S16 · S43 · S67 · S85 (arayüz) | D138 (MARS gösterge yazısı) · KART 5 | model ekrana rakam/metin basar | ikon+ışık; metin yasağı bütün yüzeylere; ölçüm postta; ① SCREEN TEXT ölçer | ⏳ |
| 11 | S47 · S48 · S49 (küme 3) | ACI_YAYI §3 küme tavanı 3 | 30 s aynı kurulum güvenlik kamerası hissi | tavan 3 ✅; S49'da yükün inişi kadrajı bozar (hareket); ⑨ ölçer | ⏳ |
| 12 | S67 | D217 (MARS replik görüneni söyledi) | «Tek rezerv. Ya darbe ya koridor.» iki çıkış kadrajda | 🔶 sahip: «Bir kez. Sonra biter.» ya da silme (post-dub, üretim etkilenmez) | 🔶 |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D174 · UZAMSAL §0.2 | pusula/ekran koordinatı prompta girerse yön yazı-tura | 00_96_KLIP HALKA/yön sütunu prompta NESNE-göreli çevrilir; harita yalnız PLAN'da |
| D209 · KRONOS AUDIO 0/96 · KILAVUZ §5.1b | dünya ve fizik her promptta başka | DÜNYA ÇAPASI üç cümle + PHYSICS/AUDIO hacme göre (02 §2) 96/96 birebir; kapsama `prompt_hata_analizi.py --kilit` ile ölçülür |
| D214 · ㉖ | kadrajda olmayan beden tarif edilir | `IN FRAME` ilk satır; opak vizör → yüz cümlesi 0; kelime bandı |
| D34 · D45 · D215 | özel ad/etiket → başlık kartı; filigran araç ayarı | prompta ad yok (sözlük); üretim defteri üç kutu; S95 `no title card` |
| D146 ⛔ ÇALIŞMIYOR · REFERANS §1 | vizör/kalkan biçimi metinle tutmaz | referans paketi 6 sayfa KAPI 0; onaysız sayfa → üretim yok |
| D203 · ㉓ · STATIC SHADOW | replik envanteri ↔ prompt | SPEC A iki satır (0 / 8); prompt tırnak 0; tam-film replik tablosu |
| ACI_YAYI §4b (DÖNÜŞ %33,3) | betik ⑩④ FIX | PLAN UYGULANMAYAN KİLİTLER'e D74 satırı + 10 küme |
| KURGU_RITMI §1 | sabit ızgara ASL | SPEC `TARGET ASL BAND: 10.0 s (sabit ızgara — bilinçli sapma)` + gerekçe |
| MARS §⑤ (İNSAN ŞERİDİ plandan türetilmemiş) | SPEC şeridi yanlış | İNSAN ŞERİDİ 96 hane 00_SAHNE_TABLOSU FİGÜR sütunundan üretilir (insansız 0; 4 kişi 4) |
| UZAYLI_VARLIK §① · SAPMA 1 | ordu/kalabalık okuması | kadrajda ≤2 Veyra (+Serrak), ≤2 avcı; Veyra promptta `tall pale-ceramic figure`, ırk adı yok |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | VAR — 4 kask (opak düz panel), Veyra kalkanı, portal halkası, K-1 bileziği | referans paketi 6 sayfa · KAPI 0 [D168] · biçim + sayı cümlesi her promptta; ② KİMLİK DİZİSİ |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT | VAR — giysi tarifi ("quilted", "ribbed") | `fabric/cloth` kelimesi prompta girmez; giysi `suit surface`/`ribbed segments`; kumaş kıpırtısı yazılmaz (0,9 g rüzgâr abartılmaz §3.3) |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT · §5.2 | VAR — T3 kulesi (geniş), K-1 (24–35 mm takip), kaldıraç platformu | 5 kilit dosyasında optik aritmetiği; tabloda OPTİK sütunu (nesne eni/px ≥100) |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | VAR — S11 T3 silueti yarıkta · S69/S81 C-0 pencerede · S95 üç gemi | T3 ≥100 px (yarıkta bir kask boyu) · C-0 pencerede kadrajın 1/8'i · S95 üç gemi tek karede sayılabilir (FİNAL VURUŞ KANITI) |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | VAR — Mara kobalt ve Bor grafit iki koyu giysi; C-0/rezerv odası loş | siluet farkı (Bor iri omuz + uzun tüp · Mara kısa alet + bilek kumandası) + Bor'un HARDAL göğüs parçası açık ton; loş sahnede rim light özneye |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | VAR — T3 kulesi, hangar, uçuş koridoru büyük yapılar | §3.3/§3.10 negatif satırları PLAN Negative Bible'a; sahne riski ≤3 cümle (§5.2); ölçek şahidi (insan gövdesi/araç) her geniş planda |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | YOK — indeks 5 sahne (S18 · S59 · S81 · S84 · S94), nesne kemer + seçici kolu | 02 §4; PLAN TEMA bloğu |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | YOK — BEDEL S59 · S84 (+ araç S29/S90) | 02 §7 |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | RİSK VAR — savaş filmi, yasak refleksi | NEGATIVE'e silah/kan/isabet kelimesi 0; pozitif form tarifi; ⑯ betik sayar |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | RİSK VAR — "weapon/rifle/gun" T1 | `a long dark tube-shaped tool` · `a short blunt hand tool` · `four bright points leave its end`; ad yok |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | YOK — 8 replik formülle (03 §5) | SPEC A'ya formül satırı |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | VAR — §1 satır 5 | ikili durum + hareket; koridor açılışı sınırda |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | YOK — V3 iskeleti; START FRAME tek satır | ㉖ IN FRAME; kadrajdaki her şey promptta |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | RİSK VAR — SPEC E yazılırken | her kapı KOMUT · DOĞRULANDI (ffmpeg sürüm·tarih) · İKAME; kuru koşu FAZ 5 |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | VAR — 4 insan, eldiven-manşet temasları | üç bölge tek cümlede (collar · wrist · ankle) her insanlı promptta; `through the glove` yok |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | D192 · OPEN CIRCUIT · A5 | KAPANDI — kalkan sapması + Bor'un ölümü sayıyla (02 §5 A5) | SPEC göz kapısı aynı sayıyla |

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapama kararı taşıyor (10/10 ✅; 2 ve 9 üretimde P6 ile sınanır)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi (12; 1'i 🔶 sahip: S67 repliği)
☑ tekrar eden arıza tablosunun 16 satırı cevaplandı
→ 05_SAHNE_CALISMALARI/ açılabilir
```
