# 🧮 THE_SIGNAL_KEEPERS — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> THE_SIGNAL_KEEPERS S<nn> <ROL>`
> ile damgalanır (`S<nn>_<ROL>.md`, tam şablon). ≤ 8 sahnelik filmde (dikey)
> bu dosya yoktur, her sahne dosya alır.
>
> Kapı: `prompt_kontrol.py` ㉚ — satır sayısı = bölüm dosyalarındaki sahne
> sayısı · beş rol dosyası var. Satırlar betik damgalar (`| S00 |` …); elle
> satır eklenmez/silinmez, sahne sayısı değişirse `--sahne-guncelle`.
>
> 🆕 **22.09.2026 · ÇOK KLİPLİ SAHNE** (`--sahne-plani` ile açılan yatay film): satır
> KLİP başınadır; betik başlığa iki sütun ekler ve satırları `| K07 | S03 | 2/3 · ⬜ |`
> biçiminde damgalar. **ROL n/N** sütununa kapsama şablonundaki rol yazılır (KURULUM ·
> EYLEM · TEPKİ · BELİRİŞ · MÜCADELE · TERSLİK · KARAR · BEDEL · DÖNÜŞ). Klibin
> `OLAY BAŞ → SON` hücresinin SON yarısı, aynı sahnedeki bir sonraki klibin
> `CONTINUOUS ACTION:` satırına kelimesi kelimesine iner [D207]. Aynı sahnenin
> `IŞIK · SES · FİZİK` hücreleri birebir aynıdır (sahne kilidi); "öncekiyle AYNI olamaz"
> kuralı yalnız SAHNELER ARASINDA geçerlidir. ㉚ SAHNE sütununu SAHNE PLANI'yla
> karşılaştırır. Kural: `COK_KLIPLI_SAHNE_KILAVUZU.md`.
>
> ⛔ Bu klasörde `## … SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ
> (kapı betiği o desenleri sahne/prompt sanar). Prompt yalnız bölüm dosyasında.

## Sütunlar — her hücre TEK satır, boş hücre yok ("—" yazılır)

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) | `03_SAHNE_SIRALAMASI` |
| **OLAY BAŞ → SON** | ne değişiyor: `<başta> → <sonda>`; klip içi değişim varsa `⚠️ARA` | çalışma şablonu 🎬 |
| **B5** | İSTEK / ENGEL / BEDEL / MUHATAP / AYRILIK — bu sahne hangi satırı taşıyor | `02_KONSEPT_VE_RISK` |
| **KURULUM** | harf + işaret (`B · dönüş S3`) · lens · mesafe · ölçek · açı tipi | `ACI_YAYI` §3-§4 |
| **OPTİK** | kadraj eni (m) · ana nesne (px) — ⛔ ≥100 px [D179]; sığmıyorsa `⛔` | `KILAVUZ` §5.2 hesabı |
| **IN FRAME** | face · hands · torso · legs · full body · back · none — promptun ilk satırı olur [㉖] | `IMAGE_VIDEO_PROMPT_TEMPLATES` V3 |
| **TAŞIYICI** | devamlılık: giren/çıkan/taşınan nesne + önceki/sonraki sahne | çalışma şablonu 👤 |
| **IŞIK · SES · FİZİK** | üçü tek hücrede `·` ile; palet/ses dokusu öncekiyle AYNI olamaz | ortam kartı · `KURGU_RITMI` §2 |
| **REPLİK** | `—` ya da `<saniye> · konuşan · İŞLEV · ağız okunuyor/okunmuyor` | `DIYALOG_SAHNESI` §2-§3 |
| **KİLİT / UYARI** | bu sahneye düşen kilit(ler) D-no ile + `04_UYARI_NOTLARI` satır no; en çok 3 | `01_QA_DERS_HASADI` |
| **İZLEYİCİ CÜMLESİ** | "bu figür ne istiyor" — seems/probably YASAK; ⭐VİRAL ise `YÜZ:` + `HAREKET:` | `OYUNCULUK_YAZIM` §1 · §3 |
| **KAPI** | ⬜ → ✅ satır tam ve optik tutuyor; ✅ olmadan o sahnenin promptu yazılmaz | — |

Doldurulmuş satır nasıl görünür (örnek; gerçek satırlar aşağıda betik damgalıdır):

```
S03 · glove closes on wheel → wheel stopped, strap slack ·  ENGEL  ·  B · dönüş S1 · 35mm · 1,6 m · MCU · eye level
    · 1,1 m · 340 px  ·  hands, torso  ·  strap in (S02) / out (S05)  ·  neutral ceiling · hum + warble · 0,25 g
    · —  ·  D200 · D216 · U-4  ·  he wants the wheel to move, not to understand it  ·  ✅
```

---

## 📋 TABLO

| K | SAHNE | ROL n/N | OLAY BAŞ → SON | B5 | KURULUM | OPTİK (eni m · px) | IN FRAME | TAŞIYICI | IŞIK · SES · FİZİK | REPLİK | KİLİT / UYARI | İZLEYİCİ CÜMLESİ | KAPI |
|:--:|:--:|---|---|:--:|---|---|---|---|---|---|---|---|:--:|
| K01 | S01 | 1/3 · KURULUM | uçurum kenarında duruyor, eli omzundaki kürede → aynı duruş, sis bir tutam alçaldı | İSTEK | A · ilk kullanım · 35mm · 8,0 m · WS · göz hizası | 8,23 m · gövde 793 px · küre 42 px ⚠️ jest taşıyor | back, full body | küre (giren) → K09'da okunur olacak · sonraki K03 | halkalı devden yansıyan soluk mavi-gri, disk kadrajda YOK · alçak yakın uğultu · 0,42 g · 240 K · toz 3 s'de oturur | — | D209 dünya çapası üç cümle · D79 durağanlık nefes+bakış+mikro ayar · U-2/2 küre 42 px | eve ait tek nesneyi tutarak bir sesi bekliyor | ✅ |
| K02 | S01 | 2/3 · EYLEM | panel sessiz → panel atıyor ve bozuk bir insan sesi kaskın içinde | İSTEK | B · ilk kullanım · 50mm · 2,0 m · MS · göz hizası ¾ | 1,44 m · yüz 587 px · panel 373 px | face, torso, one forearm | ön kol paneli (giren) · sonraki K03'te nabız olarak | aynı sahne kilidi: soluk mavi-gri yansıma · uğultu + bant gürültüsü · 0,42 g · 240 K | 12,0 s · 41 yıllık kayıt · MUHATAP · ağız okunmuyor | D172+T1 kayış/kordon 0 kare (panel ön kola GÖMÜLÜ) · D82 kaynak kilidi · D40 altyazı negatifi | duyduğu şeyin insan olduğunu doğrulamak istiyor | ✅ |
| K03 | S01 | 3/3 · TEPKİ | vadi karanlık → sisin altındaki ışık bandı panelle AYNI ritimde | MUHATAP | A · dönüş K01 · 35mm · 8,0 m · WS · göz hizası | 8,23 m · ışık bandı 62 px · panel 65 px (iki nabız TEK karede) | back, full body | ışık bandı (giren) · panel (taşınan K02'den) | aynı sahne kilidi · uğultu + iki nabız, tizsiz · 0,42 g · 240 K | — | D73 türetilmiş anomali tek karede · ⑩④ dönüş işareti birebir · U-⚠️3 hook ölçümü | cevap verenin ne olduğunu görmek istiyor | ✅ |
| K04 | S02 | 1/4 · KURULUM | bitki bandının üstünde → bandın içinde, arkasında iki karanlık bitki | ENGEL | C · ilk kullanım · 35mm · 1,8 m · MS · alçak açı | 1,85 m · gövde üst yarısı 1762 px · bitki 622 px | torso, legs | sönmüş bitki izi (giren sayaç) · sonraki K05 | yalnız bitkilerin KENDİ ışığı, kenarlarını geçmiyor · bot + yaprak sürtünmesi · sis OTURUR, toz KALKAR | — | ⛔U-7 pozitif yayıcı kuralı · `0% bloom/no glow` negatifte kalır · D138 yüzeyde yazı yok | ışığın kaynağına inmek istiyor | ✅ |
| K05 | S02 | 2/4 · EYLEM | yaprak yanıyor → yaprak eldivenin altında sönmüş ⚠️ARA | — | D · ilk kullanım · 50mm · 0,80 m · CU · üst açı 40° | 0,58 m · yaprak 600 px · parmak ucu 200 px | one hand | üç karanlık bitki (sayaç +1) · sonraki K06 | aynı sahne kilidi · tek kuru tıklama · aynı sayılar | — | ⚠️U-12 START/ACTION/END üç satırı · ALIŞKANLIK kilidi (dokunmadan önce bir kez vurur) · D67 form tarifi | dünyanın canlı olup olmadığını yokluyor | ✅ |
| K06 | S02 | 3/4 · TEPKİ | doğruluyor → arkasında beş karanlık bitki, ileride uzun bir siluet | MUHATAP | C · dönüş K04 · 35mm · 1,8 m · MS · alçak açı | 1,85 m · siluet 2,40 m @14 m → 640 px | torso, back | siluet (giren) · sönmüş iz beşe çıktı · sonraki K07 | aynı sahne kilidi · uğultu bir ton alçalır · aynı sayılar | — | ⑩④ dönüş işareti birebir · UZAYLI_VARLIK §5 K3 SİLUET bandı · ⛔U-5 ayrım DEĞERLE | gördüğü şeyin ona mı baktığını bilmek istiyor | ✅ |
| K07 | S02 | 4/4 · DÖNÜŞ | yapraklar açık → dizi DOKUNULMADAN kapanmış ⚠️ARA | MUHATAP | D · dönüş K05 · 50mm · 0,80 m · CU · üst açı 40° | 0,58 m · yaprak 600 px · gölge kadraj genişliğinde | none | sayacın SAHİBİ değişti (giren: gölge) · sonraki K08 | aynı sahne kilidi · kapanma dizisi, tizsiz · toz kalkar ve 3 s'de oturur | — | red #2 insansız klip: negatif KISALTILIR, insan sayısı cümlesi YOK · D123 göz hiç anılmaz | (insansız) burada başkası var ve aynı şeyi yapıyor | ✅ |
| K08 | S03 | 1/5 · KURULUM | adımının ortasında → durmuş, göğsünde büyük bir gölge, geri çekilmiyor | MUHATAP | E · ilk kullanım · 35mm · 1,8 m · MS · göz hizası | 1,85 m · yüz 456 px · gölge kadrajın %60'ı | torso, face | gölge (giren) · sonraki K09 | gökten soluk yansıma, gölge kenarı yumuşak ama DERİN · tek derin nefes · toz kalkar ve oturur | — | D146 vizör TEK düz berrak pencere · UZAYLI_VARLIK §5 K0 İZ · U-1 anatomi sayısı BU sahnede YAZILMAZ | kaçmamaya karar veriyor | ✅ |
| K09 | S03 | 2/5 · EYLEM | bakışı ileride → bakışı kendi omzuna inmiş | MUHATAP | F · ilk kullanım · 85mm · 1,15 m · CU · göz hizası frontal | 0,49 m · yüz 1735 px · küre 710 px | face | küre (K01'den taşınan, ilk kez okunur) · sonraki K11 | aynı sahne kilidi · oda tonu, ses yok · aynı sayılar | — | red #15 kimlik özelliği ≤3 · D175 çıplak deri üç bölge tek satırda · ⭐viral ölçüldü ⛔ (② boş) | omzundaki şeyin neden önemli olduğunu anlıyor | ✅ |
| K10 | S03 | 3/5 · BELİRİŞ | avuç kapalı → avuç açık, içinde kırık mavi cam, ton DONUK ⚠️ARA | MUHATAP | G · ilk kullanım · 85mm · 0,48 m · ECU · üst açı 25° | 0,20 m · avuç kadrajı AŞAR · kırık parça 945 px | none | kırık parça (giren) · sonraki K11 · K24 bu kadraja döner | aynı sahne kilidi + kırık camın kendi mavisi · donuk tek ton · mineral doku sürtünmesi | — | D157 TEK KARE cümlesi taşıyıcının adını içerir · red #2 insansız negatif kısaltılır · D172+T1 nesne kadrajda BÜYÜK | (insansız) bunu 41 yıl biri saklamış | ✅ |
| K11 | S03 | 4/5 · KARAR | kendi küresine vurur → ton BERRAK, vizörün üstünden ışık deseni geçiyor | MUHATAP | F · dönüş K09 · 85mm · 1,15 m · CU · göz hizası frontal | 0,49 m · yüz 1735 px · küre 710 px | face, one hand | ton (nesnenin sayacı: donuk → berrak) · sonraki K12 | aynı sahne kilidi · berrak tek ton · aynı sayılar | — | ⛔U-5 iki gövde tek CU'da ASLA: varlığın başı kadraja GİRMEZ · KART 12 temas 0 kare · ⭐VİRAL | ⭐YÜZ: kaşlar kalkar, çene sabitlenir · HAREKET: vizör üstünde geçen ışık deseni + parmak ucu teması | ✅ |
| K12 | S03 | 5/5 · TEPKİ | kütle karşısında → kütle kadrajı terk etmiş, toz oturuyor, kadın peşinde | MUHATAP | E · dönüş K08 (ara 4) · 35mm · 1,8 m · MS · göz hizası | 1,85 m · gövde üst yarısı 1762 px · toz öbekleri 150 px | torso, back | kalkan toz (kütle kanıtı) · bölüm sınırı → K13 | aynı sahne kilidi · ağır adım + toz · toz KALKAR ve 3 s'de OTURUR, asılı perde YOK | — | ⚠️U-4 asılı toz perdesi yasağı · ⚠️U-5 varlık havada durmaz, ağırlığı adımında · ⑩④ dönüş işareti | peşinden gitmeye karar veriyor | ✅ |
| K13 | S04 | 1/3 · KURULUM | kaya geçidi kapalı → geçit açık, şehir ve varlık tam gövdeyle kadrajda | ENGEL | H · ilk kullanım · 35mm · 6,0 m · WS · göz hizası | 6,17 m · gövde 1058 px · varlık @15 m 597 px · kemer ağzı 1992 px | full body, back | geçit kemeri (sabit şahit) · sonraki K15 | şehrin taş yüzeylerinden turuncu-altın yansıma · geniş hacim tonu · rüzgâr yalnız zeminde ince toz | — | ⛔U-1 ANATOMİ SAYISI burada yazılır: 2 bacak · 2 ön kol · 1 levha · 1 çatlak · boy = ağzın 3/4'ü · KART 13 metre yok | aradığı şeyin bir medeniyetin içinde olduğunu görüyor | ✅ |
| K14 | S04 | 2/3 · EYLEM | kule dibinde → başı kalkmış, gökte halkalı dev, köprüde ışık akıyor | ENGEL | I · ilk kullanım · 18mm · 8,0 m · EWS · zemin | 16,00 m · gövde 408 px · köprü 192 px · halkalı dev 442 px | full body | halkalı devin yüksekliği (dünyanın sayacı, 5. adım) · sonraki K15 | aynı sahne kilidi · uzak alçak akış · aynı sayılar | — | ⛔U-8 sayı dili YOK: köprü ışığı akan BANT · KART 9 kamera kaynağa ilerlemiyor · D179 7 px öğe nokta yazılmaz | kendi ölçüsünü bu şehrin yanında görüyor | ✅ |
| K15 | S04 | 3/3 · DÖNÜŞ | ikisi sokakta → varlık siyah kapı ağzında, kadın dokuz metre arkada | MUHATAP | H · dönüş K13 · 35mm · 6,0 m · WS · göz hizası | 6,17 m · gövde 1058 px · kapı ağzı 1992 px | full body, back | kapı ağzı (giren) · sonraki K16 | aynı sahne kilidi · kapı ağzının yankısı · aynı sayılar | — | KONUM KİLİDİ kadın SAĞ / varlık SOL üçte bir, merkez çizgisi geçilmez · ⑩④ dönüş işareti · temas 0 kare | çağrıldığını anlıyor ve mesafeyi koruyor | ✅ |
| K16 | S05 | 1/5 · KURULUM | kapı ağzı → salon: iki sıra yuva, yakın üçü okunur, derinlik ışıksız | İSTEK | J · ilk kullanım · 18mm · 10,0 m · EWS · göz hizası | 20,00 m · gövde 326 px · varlık 461 px · yuva 269 px | full body, back | yuvalar (giren) · giriş kemeri (sabit şahit) · sonraki K17 | yalnız yuvaların nokta ışıkları, derinlik IŞIKSIZ · çok alçak çok geniş oda tonu · kalın hava tizleri yutar | — | ⛔U-8 "yüzlerce" hiçbir bantta YOK, çokluk karanlıktan · ⛔U-1 anatomi sayısı burada yazılır · KART 13 ölçek şahidi | burada bir şeyin saklandığını anlıyor | ✅ |
| K17 | S05 | 2/5 · BELİRİŞ | sıranın içinde → onarılmış insan sondası ve BOŞ cam yuvası kadrajda | ENGEL | K · ilk kullanım · 35mm · 3,2 m · WS · alçak açı 15° | 3,29 m · sonda 1284 px · BOŞ cam yuva 140 px | none | boş cam yuva (giren) · sonraki K19 · K24'te dolacak | aynı sahne kilidi · ince metal gerilmesi · aynı sayılar | — | red #2 insansız klip negatifi KISALTILIR · D138 sondanın gövdesinde harf/sayı YOK · D67 form tarifi | (insansız) bu şey onarılmış ve bir şey eksik | ✅ |
| K18 | S05 | 3/5 · EYLEM | ızgara sessiz → kayıt NET duyuluyor, yüzü dinliyor | MUHATAP | E · ilk kullanım (bu mekânda) · 35mm · 1,8 m · MS · göz hizası | 1,85 m · yüz 456 px · ızgara 207 px | face, torso | kayıt (K02'den taşınan, bu kez tam) · sonraki K20 | aynı sahne kilidi · replik 2 net + bant sesi · aynı sayılar | 173,0 s · aynı kayıt · MUHATAP · ağız okunmuyor | D217 replik ekranda OLMAYANI söylüyor · D203 SPEC 2 = promptta 2 tırnaklı satır · ⭐viral ölçüldü ⛔ (② boş) | cümleyi ilk kez bütün duyuyor | ✅ |
| K19 | S05 | 4/5 · TERSLİK | eli panele uzanıyor → eli havada durdu, avuç panelde çoktan duruyor | ENGEL | K · dönüş K17 · 35mm · 3,2 m · WS · alçak açı 15° | 3,29 m · el 292 px · varlığın ön kolu 700 px | torso, one hand | panel (anlaşmazlığın nesnesi) · sonraki K20 | aynı sahne kilidi · kayıt sürüyor + sessiz ret · aynı sayılar | — | ⛔U-5 TEMASSIZ ret, gecikme 0,8 s ≥0,7 s · KONUM KİLİDİ · ⑩④ dönüş işareti birebir | kaydı korumak isteyen birinin olduğunu görüyor | ✅ |
| K20 | S05 | 5/5 · BEDEL | çekirdek panelin içinde → çekirdek elinde, ses cümlenin ortasında kesildi ⚠️ARA | BEDEL | E · dönüş K18 · 35mm · 1,8 m · MS · göz hizası | 1,85 m · yüz 456 px · çekirdek 456 px | face, hands | çekirdek (çıkan) · ses (giden, sonsuza dek) · sonraki K21 | aynı sahne kilidi · KESİLME → 41 yılın ilk sessizliği · aynı sayılar | kesilme 192,6 s · tırnaklı metin YAZILMAZ · HARD MUTE 192,6–194,0 s | ⚠️U-12 START/ACTION/END üç satırı · D180 hard mute · D172+T1 çekirdek kadrajda büyük, kayış yok · ⭐VİRAL | ⭐YÜZ: nefes tutulur, çene iner (AU4) · HAREKET: çekirdek yuvadan çıkıyor + ses ortada kesiliyor | ✅ |
| K21 | S06 | 1/4 · TEPKİ | boş yuva ölü → çekirdek oturmuş, yakın üç halka uyanıyor ⚠️ARA | İSTEK | K · dönüş K19 · 35mm · 3,2 m · WS · alçak açı 15° | 3,29 m · sonda 1284 px · uyanan halka 269 px | torso, hands | çekirdek (taşınan K20'den) · uyanan halka (giren sayaç) · sonraki K22 | uyanan halkaların sıcak beyazı YAKIN ÜÇTE, derinlik hâlâ ışıksız · kilitlenme + yükselen alçak taşıyıcı · aynı sayılar | — | ⚠️U-6 kamera kaynağa İLERLEMİYOR · ⚠️U-12 START/ACTION/END · ⑩④ dönüş işareti · iptal kapısı ① üretim sırası ② | gönderdiği şeyin çalıştığını görüyor | ✅ |
| K22 | S06 | 2/4 · EYLEM | başı önde → başı kalkmış, dizi yukarıyı gösteriyor, ışık kadrajdan çıkıyor | İSTEK | E · dönüş K20 · 35mm · 1,8 m · MS · göz hizası | 1,85 m · yüz 456 px · yuva dizisi kenarı 300 px | face, torso | ışık (çıkan, yukarı) · varlık kadraj kenarında (PARÇA) · sonraki K23 | aynı sahne kilidi · taşıyıcı uzaklaşır, tiz YOK · aynı sayılar | — | ⚠️U-6 ışık kadrajın ÜSTÜNDEN çıkar, merkeze yürümez · D79 durağanlık üç öğeyle · ⭐VİRAL | ⭐YÜZ: yüz kalkar, göz kapakları gevşer · HAREKET: yuva dizisi yukarı dönüyor, ışık kadrajın üstünden çıkıyor | ✅ |
| K23 | S06 | 3/4 · BEDEL | küre omuz yuvasında → küre yuvadan kalkmış, yuva boş ⚠️ARA | BEDEL | L · ilk kullanım · 50mm · 1,00 m · CU · göz hizası | 0,72 m · omuz paneli 1600 px · halka 640 px · küre 480 px | shoulder, hands (yüz YOK) | küre (çıkan) · sonraki K24'te sondanın yuvasında | aynı sahne kilidi · halkanın çeyrek turu, tek kuru klik · aynı sayılar | — | ⛔U-3 red #3: gövde kadrajda, eksen YATAY, `removes from her suit/body` YAZILMAZ · red #13 üç bileşenden ikisi kadrajdan çıktı | evden getirdiği tek şeyi bırakmaya karar vermiş | ✅ |
| K24 | S06 | 4/4 · DÖNÜŞ | sondanın cam yuvası boş → içinde mavi küre, ton BERRAK, taşta mavi leke ⚠️ARA | BEDEL | G · K10'un kadrajına dönüş (ara 14 · yeniden tanıtım) · 85mm · 0,48 m · ECU · üst açı 25° | 0,20 m · cam yuva kadrajı doldurur · küre 1700 px · parmak ucu 544 px | hands | küre (taşınan K23'ten) · eller kadrajdan BOŞ ve AÇIK çıkar | aynı sahne kilidi + kürenin kendi mavisi · berrak ton + oda tonu · aynı sayılar | — | D210 kafiye çifti: CAMERA satırı K10'un birebir kopyası · ⚠️U-12 START/ACTION/END · D172+T1 nesne kadrajda büyük | karşılığını görmeyeceği bir şeyi gönderdi ve tamamladı | ✅ |
