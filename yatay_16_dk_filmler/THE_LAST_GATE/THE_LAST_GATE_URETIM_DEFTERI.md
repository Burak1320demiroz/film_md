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
5  HOOK EN SON (K01–K04 ana kurgudan monte)        ⬜
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

## 6. ÖNERİLEN COMMIT MESAJI (⛔ commit SAHİBİN)
```
feat(yatay_16_dk): THE_LAST_GATE — 96 klip / 25 sahne, 184 prompt, klasör modu GO

Sahibin kapsamlı planı (THE_LAST_GATE_KAPSAMLI_PLAN.md · 724 satır) referans alınarak
yazıldı; plan 00_ANALIZ/00_ON_PLAN/ altına taşındı. 8 bölüm dosyası, 21 sayfalık
referans paketi, QA_SPEC (4 PART + TAM FİLM), kapak, müzik, yayın paketi ve üretim
defteri. prompt_kontrol.py klasör modu: 0 BLOCK, 8 gerekçeli FIX. Dört SAPMA kayıtlı.
```
