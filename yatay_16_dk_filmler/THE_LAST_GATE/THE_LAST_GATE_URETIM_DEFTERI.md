# 🏭 THE_LAST_GATE — ÜRETİM DEFTERİ

> Bu dosyayı ÜRETİM doldurur. Şu an **0 kare üretildi** — aşağıdaki her satır ⬜.
> ⛔ KAPI 0: referans paketinin 21 sayfası ONAYLANMADAN hiçbir klip üretilmez [D168].

## 0. ÜRETİM SIRASI — dramatik sıra DEĞİLDİR
```
0  REFERANS PAKETİ 21 sayfa                       ⬜
1  MEKÂN/ÖLÇEK ANİMATİĞİ (96 blok)                ⬜
2  ODAKLI TESTLER T01–T08                         ⬜
3  MEKÂN SIRASI: yuva/servis → hücre/koridor → köprü → araç içleri → dış liman/takip → geçit/final
4  SINIR ÇİFTLERİ K24↔K25 · K48↔K49 · K72↔K73     ⬜
5  HOOK EN SON (K01–K04 ana kurgudan monte)        ⬜  → kesim listesi §7 ✅
```

## 1. ODAKLI TESTLER — kapsamlı plan §17
| test | kaynak klip | bakılacak somut şey | sonuç |
|---|---|---|:--:|
| T01 beyaz kimlik | K05 / K20 | vizör yüzü + rozet + beyaz yüzey ayrıntısı birlikte okunuyor mu | ⬜ |
| T02 gerçek yanaşma | K09–K11 | hiza → temas → sert kenet ÜÇ AYRI durum mu, iki rijit gövde korunuyor mu | ⬜ |
| T03 yetişkin topluluk | K17 / K27 | figürler açıkça yetişkin mi · sayı/giysi/kimlik kararlı mı · kalabalık hissi YOK mu | ⬜ |
| T04 Veyr | K25 | erişkin yüz + dört parmak + iki boyun halkası sabit mi | ⬜ |
| T05 büyük ayrılış | K41 / K44 | gemi + liman + gezegen aynı coğrafyada anlaşılır mı | ⬜ |
| T06 mikrogravite | K65–K67 | itiş → darbe → sürüklenme → tutunma neden-sonuç izlenebilir mi | ⬜ |
| T07 sığmama | K64 / K69 | 900'de sığan gövde 420'de açıkça SIĞMIYOR mu | ⬜ |
| T08 son geçiş | K90 / K92 / K93 | araç TAM geçip alan SONRA mı kapanıyor | ⬜ |

## 2. İPTAL KAPILARI — ⛔ bu ikisi düşerse FİLM ÜRETİLMEZ
```
⛔ T07 (K69) novum okunmuyorsa → film ÜRETİLMEZ
⛔ T08 (K92) araç tam geçmeden alan kapanıyorsa → film ÜRETİLMEZ
⚠️ T03 düşerse sahne SADELEŞİR (figür silinmez)
⚠️ T01 düşerse ışık/arka plan/açı değişir — giysiyi griye çevirmek İLK çözüm DEĞİL
⚠️ T04 düşerse Veyr'in el ve yüz hareketi AYRI kaynaklara bölünür
⭐ Başarısız test yaratıcı isteği SİLMEZ (kapsamlı plan §17).
```

## 3. ARAÇ AYARI — üç kutu, üretim başında bir kez
```
┌ METİN / FİLİGRAN ────────────────────────────────────────────────┐
│ ekran metni KAPALI · filigran KAPALI · altyazı KAPALI            │
│ ⛔ Filmde gömülü altyazı YOKTUR; istenirse sonradan AYRI dosya.  │
│ ⛔ Başlık/jenerik 960 saniyeye EKLENMEZ [D70 · LOSS_OF_LIFT]     │
└──────────────────────────────────────────────────────────────────┘
┌ AĞIZ / SENKRON ──────────────────────────────────────────────────┐
│ Kadrajda konuşan ağız VAR: 32 repliğin 11'i ③ yerleşimde.        │
│ ⚠️ Sahibin açık kararı (kapsamlı plan §2 md.3). Lip-sync ayarı   │
│   AÇIK ve ilk iki replikte ELLE kontrol edilir.                  │
│ Sorun çıkarsa: replik reaksiyon planına / omuz üstüne / mekanik  │
│   inserte taşınır (kapsamlı plan §14). Karakter sırtını DÖNMEZ.  │
└──────────────────────────────────────────────────────────────────┘
┌ SÜRE ────────────────────────────────────────────────────────────┐
│ ham klip ARAÇTAN ölçülür [D124]:                                 │
│   ffprobe -v error -show_entries format=duration -of csv=p=0 <k> │
│ kurgu birimi 24 fps'te TAM 240 kare · zaman kodu YENİDEN         │
│ HESAPLANMAZ, sapma KIRPMA satırıyla kapanır (SPEC A)             │
└──────────────────────────────────────────────────────────────────┘
```

## 4. KLİP DEFTERİ — ilk satır üretim sırasının İLKİ
| klip | deneme | sonuç | not |
|---|:--:|:--:|---|
| K69 (T07) | ⬜ | ⬜ | ⛔ İPTAL KAPISI — ilk kabul satırı bu değilse ikinci klip üretilmez |
| K92 (T08) | ⬜ | ⬜ | ⛔ İPTAL KAPISI |
| K11 (T02) | ⬜ | ⬜ | dört kenet sayısı |
| K25 (T04) | ⬜ | ⬜ | dört parmak · iki halka |
| K17 (T03) | ⬜ | ⬜ | altı ayrı bay · kalabalık YOK |
| K05 (T01) | ⬜ | ⬜ | beyaz + vizör + rozet |
| K41 (T05) | ⬜ | ⬜ | üç ölçek aynı karede |
| K67 (T06) | ⬜ | ⬜ | bağın iki ucu |

## 5. ⚠️ ÜRETİM SIRASINDA İZLENECEK ÜÇ ŞEY
```
① SCENE COUNT ≠ CLIP COUNT bu rejimde TASARIMDIR (25 sahne · 96 klip). Rapor bunu
   kusur yazarsa SPEC A yanlış-pozitif duvarına bakılır.
② K01–K04 KURGU BLOĞUDUR: bu dört blok için görüntü ÜRETİLMEZ. Üretilen klip 92.
③ RED DEFTERİ #13 İZLEME: K19 (iki eldiven + yakın plan) kompozisyon reddi sınıfına
   yakın. Red gelirse önce KADRAJ değişir, sözcük değişmez [D123 · YERCEKIMI S8].
```

## 7. 🎬 HOOK KESİM LİSTESİ — K01–K04 · 01.10.2026

> Planın §18.1'i EDIT grubunda **"hook kesim listesi"**ni sayıyor ve o dosya hiç
> yazılmamıştı. K01–K04'ün "promptu" budur: §9 ve §16 bu dört blok için görüntü
> üretmeyi YASAKLIYOR (*"yeni görüntü üretmek yerine kaynak klip ve kesim
> aralıklarını gösterir"*), karşılığı kare hassasiyetinde kesim listesidir.
> ⛔ Üretilen yeni kare: **0.** Kurguda hız değiştirilmez [§16].

**24 fps · blok 240 kare · hook 960 kare = 40,000 s**

| zaman çizgisi | blok | kaynak | in → out | kare | neden BU in/out |
|---|:--:|:--:|---|:--:|---|
| 00:00:00:00–00:00:09:23 | K01 | **K06** | 0,000 → 10,000 | 240 | tam klip; tek kesintisiz okunur yaklaşma, blok içi kesme YOK |
| 00:00:10:00–00:00:14:23 | K02 | **K10** | 1,000 → 6,000 | 120 | temas tamamlanırken girer, *"one small axial motion is absorbed and damped out"*ın ÜZERİNDE çıkar — tamamlanmış eylemde kesme |
| 00:00:15:00–00:00:19:23 | K02 | **K11** | 3,000 → 8,000 | 120 | 3,000'de birinci kıskaç ZATEN yatık → dördü de kadrajda, üçü ekranda kapanır, *"all four stay down"*ın üzerinde çıkar |
| 00:00:20:00–00:00:22:23 | K03 | **K20** | 0,000 → 3,000 | 72 | *"the forearms meet and hold; both faces are readable"* — yetişkin Lina tam burada kurulur |
| 00:00:23:00–00:00:26:23 | K03 | **K36** | 3,000 → 7,000 | 96 | *"the two side consoles come live"* → ÜÇLÜ kontrol ancak burada okunur (0–3'te yalnız bir konsol var) |
| 00:00:27:00–00:00:29:23 | K03 | **K46** | 7,000 → 10,000 | 72 | *"the three hold one formation and no fourth shape appears"* — üç araç tam burada |
| 00:00:30:00–00:00:36:23 | K04 | **K52** | 3,000 → 10,000 | 168 | *"gap closes"* + *"the ring opening keeps drawing in"* → H4'ün *"the last gate is closing"*ını görüntüyle kurar |
| 00:00:37:00–00:00:39:23 | K04 | **K53** | 0,000 → 3,000 | 72 | *"the shot crosses and lands on the drive cluster"* + parçaların ayrılması → blok DARBEDE biter |

```
DOĞRULAMA  240+120+120+72+96+72+168+72 = 960 kare = 40,000 s ✅
KESME      blok içi 4 · blok sınırı 3 · TOPLAM 7 kesme / 40 s
            K01 tek parça (plan §9: "her bloğun tek kesintisiz görüntü olması gerekmez"
            → gerekmiyor ama K01 öyle; ölçek karesi kesilmeden okunur)
SIRA        ⛔ hook EN SON monte edilir (§0 satır 5 · §17) — kaynaklar kabul edilmeden
            kesim listesi UYGULANMAZ, yalnız planlanır.
```

### 7.1 ⭐ K11 kıskaç aritmetiği — 5 s'ye dört kapanma SIĞMIYOR, çözüldü

```
ÖLÇÜM  K11'in dört kapanması 0,0 → 8,0 s sürüyor (1. kıskaç 0–3 · 2. ve 3. 3–7 ·
       4. 7–8). Planın K02 payı 5 s. ⛔ 8 s'lik eylem 5 s'ye sığmaz ve §16
       hızlandırmayı YASAKLIYOR ("yalnız süreyi doldurmak için … hızlandırılıp
       yavaşlatılmaz").
ÇÖZÜM  in 3,000 seçildi: birinci kıskaç o anda YATIK durumda kadrajda duruyor,
       ikinci·üçüncü·dördüncü ekranda kapanıyor. ⭐ Plan §11'in istediği
       "kıskaç sayısı DÖRT" bir KADRAJ SAYIMIDIR, bir kapanma sayımı değil —
       dördü de kadrajda, sayım okunuyor. Kayıp: birinci kapanmanın hareketi.
ALTERNATİF (sahibin kararı)  payı 5+5 yerine **4+6** yapmak: K10[2,000→6,000] +
       K11[2,000→8,000] → dört kapanmanın üçü yerine dördü de ekranda olur,
       bedeli temas anının 1 saniyesi. Toplam 240 kare değişmez.
```

### 7.2 DIŞ SES — H1–H4 · 40 s'lik TEK kesintisiz kanal

Dış ses kesmelere bağlı DEĞİLDİR; kesmelerin üstünden geçer. Hedef yerleşim blok
başlarıdır, **tek sert kısıt** H4'ün bitişidir.

| ID | metin | hedef giriş | süre |
|:--:|---|---|:--:|
| H1 | *"I came for my sister."* | 00:00:00:12 | ⬜ |
| H2 | *"She was aboard a prison ship with hundreds of captive astronauts."* | 00:00:10:12 | ⬜ |
| H3 | *"She would not leave them. So we took the ship."* | 00:00:20:12 | ⬜ |
| H4 | *"Now a fleet is behind us, and the last gate is closing. We have to get everyone through."* | 00:00:30:12 | ⬜ |

```
⛔ SÜRELER YAZILMAZ, ÖLÇÜLÜR [D124 · plan §9: "Okuma süresi kayıtla ölçülmeden
   kesin kabul edilmez"]:
     ffprobe -v error -show_entries format=duration -of csv=p=0 <H1..H4.wav>
SERT KISIT  H4, 00:00:39:12'den ÖNCE biter — K05'in kronolojik başlangıcı ve D01
            repliği üzerine basılmaz.
BÜTÇE       dördünün toplamı ≤ 30,000 s. Plan §9: kalan ≥10 s temas ve darbe
            seslerine bırakılır. Toplam 30 s'yi aşarsa ⛔ hız değiştirilmez —
            H2 ve H4 yeniden PROVA edilir (§9: "sakin ama baskı hissi taşıyan").
PAY         K11 payında (00:00:15:00–00:00:19:23) dört metal vuruş var ve plan
            "H2 için temiz ses payı" istiyor → vuruşlar H2'nin cümle araları
            arasına yerleşir, üstüne binmez.
```

### 7.3 SES YATAĞI — blok başına, kaynak klibin AUDIO satırından

```
K01 ← K06  ince telsiz bandı + hafif yapısal uğultu · dıştan hiçbir ses · düşük müzik NABZI başlar
K02 ← K10  temastan sonra gövdeye iletilen tok ses
    ← K11  dört ayrı, aralıklı, kuru metal vuruş (kovuk yok)
K03 ← K20  koridor tınısı  ← K36 konsol  ← K46 komuta kanalı taşıyıcısı + ritim altta yükselir
K04 ← K52  telsiz yatağı, ritim tutar  ← K53 gövdeden içeriden taşınan TEK darbe
⛔ Vakumdan hiçbir ses geçmez; her ses bir gövde ya da giysi taşır.
⛔ Zafer müziği hook'ta YOK (§9: çözüm ve sağ kalanlar açıklanmaz).
```

### 7.4 BAĞIMLILIK — kaynak kliplerin kapı durumu (01.10.2026 ölçümü)

```
K01 ← K06                 ✅ kesilebilir (kaynaklar kabul edildiği an)
K02 ← K10 + K11           ✅ K11'in kadrajı onarıldı: J (0,20 m) → T (50mm @ 2,4 m,
                             1,73 m) · dört kıskaç artık halkanın çevresinde okunuyor
K03 ← K20 + K36 + K46     ⛔ K46 DÜŞÜYOR: 320 m komuta gemisi + iki önleme aracı
                             60 m kadrajda "tek formasyon" tutamaz
K04 ← K52 + K53           ✅ K52 onarıldı: A (60 m) → S (24mm @ 2.000 m, 3.000 m) ·
                             2.400 m gövde 3072 px
⭐ Dört bloğun üçü kesilebilir. K03, K46 onarılana kadar bekler.
   Tam liste: 00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md · KAPI sütunu
   (88 ✅ / 8 ⛔) ve 00_ANALIZ/04_UYARI_NOTLARI.md §5.6.
```

## 6. ÖNERİLEN COMMIT MESAJI (⛔ commit SAHİBİN)
```
feat(yatay_16_dk): THE_LAST_GATE — 96 klip / 25 sahne, 184 prompt, klasör modu GO

Sahibin kapsamlı planı (THE_LAST_GATE_KAPSAMLI_PLAN.md · 724 satır) referans alınarak
yazıldı; plan 00_ANALIZ/00_ON_PLAN/ altına taşındı. 8 bölüm dosyası, 21 sayfalık
referans paketi, QA_SPEC (4 PART + TAM FİLM), kapak, müzik, yayın paketi ve üretim
defteri. prompt_kontrol.py klasör modu: 0 BLOCK, 8 gerekçeli FIX. Dört SAPMA kayıtlı.
```
