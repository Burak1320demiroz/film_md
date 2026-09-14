# 🧠 THE_SHATTERED_BREATH — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     THE_SHATTERED_BREATH [sahip onayladı]
            88 K kriyojenik buz uydusunda donmamak için durduğu zemini eriten astronotun termal ikilemi.
            Gerekçe: Ortam 3.9 Kriyojenik kartı, depoda novum olarak tekil hayatta kalma ikilemiyle birleştirildi.
② FORMAT:   Yatay 2-4 dk (16:9) → §2.2 kartı · bölüm sayısı: 2 (Bölüm 1: S00-S05, Bölüm 2: S06-S11)
③ SAHNE:    12 sahne → klip süresi 10s · toplam runtime: 120s (2:00)
④ REFERANS PAKETİ: YAZILIR (KAPI 0)
    T1 tetikleyicisi (kask/vizör/zırh) nedeniyle kilit referans paketi zorunludur.
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "opsiyon 2 - THE SHATTERED BREATH (kriyojenik ikilem) - ısı = yaşam ama ısı = durduğun zeminin erimesi"
REPLİK: yok (Sessiz dramaturji, audio katmanları: zırh içi nefes/kalp, kabuk tıkırtısı, termal sub-bass)
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazıldı:**
Mevcut ortam 88 Kelvin sıcaklıkta saf metan değil, metan-etan kompozit sert kabuktur. Saf metan faz değiştirdiğinde aniden gaz veya sıvı nehre dönüşerek astronotu anında yutardı; kompozit kabuk ise ısı uygulandığında basamaklı mikro-çatlaklar ve mikro-adacıklar oluşturarak 2 dakikalık dramatik ikileme imkan tanır.

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| Zemin donmamak için erimeli | Saf metan 88 K'da anında çöker | Metan-etan kompozit kabuk (88 K) | Kılcal çatlak ve mikro-adacık dengesi için fiziki tutarlılık |
| Isı kaynağı uzaylı makinesi | Gizem lore'u odak dağıtır | Pasif jeotermal hat bağlantısı | Odağı astronotun termal ikilemine tutmak |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        Yatay 2-4 dk (16:9) → §2.2 kartı
ORTAM:         §3.9 Kriyojenik (88 K) → tetiklediği zorunlu satırlar: buz erimesi, gaz buharı, turuncu damar
TÜR:           bilimkurgu · dal: Kriyojenik Hayatta Kalma / İkilem → §4.1
KLİP SÜRESİ:   10 s (araçtan ölçüldü [D124])
SAHNE SAYISI:  12    RUNTIME: 120 s = S00-S11
BÖLÜM SAYISI:  2    (Bölüm 1: S00-S05 / Bölüm 2: S06-S11 — §2.0 uyarınca tam ortadan bölünür)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Hayatta kalmak için vücuda ve giysiye çekilen termal enerji, üzerinde durulan 88 K kompozit buz kabuğunu mikro-çatlaklarla eriterek taşıyıcı zemini yok eder.
NOVUM TAŞIYICISI:    astronot çizmeleri × jeotermal hat bağlantısı → kompozit kabuk erimesi
① TEK KARE:          A dark composite ice moon surface fractures into glowing orange thermal lines beneath an astronaut's suit boots as the crust melts into micro-islands.
② KİNETİK BAĞIMSIZLIK: ✅ Replik/ekran metni olmadan tamamen görsel: Astronot ısı vanasını açtığı an botlarının altındaki zemin 590 nm kehribar renkle parlayıp mikro-çatlaklar üretir.
③ BAŞLIK ŞEMASI:     THE SHATTERED BREATH (3 kelime ≤5)
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — BEDEL
▸ tanım cümlesi — Donmaktan kurtulmak için alınan her birim ısı, üzerinde durulan hayati zeminin yıkımı pahasına ödenir.
▸ depoda kaç kez kullanıldı — 5 kez (bash sayac.sh uyarınca)
▸ motif kanalları — mat pirinç termo-valf (nesne) · el ile yalıtım sökümü (kinesik) · turuncu jeotermal erime (ışık)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| Risk A5 (Zemin Erimesi) | ✅ | Kriyojenik zeminin erimesi görsel gürültü üretebilir | Erime alanı çizme etrafında 2-5 cm genişlikte kılcal hatla sınırlandı | Düşük |
| Risk B2 (Vizör İç Işık) | ✅ | Vizör yansıması astronot yüzünü kapatabilir | Mavi-beyaz HUD iç ışığı açısı sabitleştirildi | Düşük |
| Risk C1 (Zırh Devamlılığı) | ✅ | Sahneler arası zırh detayları değişebilir | Referans Paketi (KAPI 0) ve Seed 9001 ile kilitlendi | Yok |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  Kriyojenik Zemin Erimesi Görsel Gürültüsü
POZİTİF BİÇİMİ:   88 Kelvin siyah metan-etan zemin üzerinde bot temas ettiğinde saniyede 3 milimetre genişleyen, 590 nanometre kehribar-turuncu kılcal çatlak ağları ve 1.8 metre çapa sahip mikro-adacık oluşumu.
```

```
TETİKLENEN RİSK:  3 / 18
EŞİK:             5
EŞİĞİN ALTINDA:   Malzeme azaltılması gerekmedi, mevcut 3 risk kontrol altında.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — `REFERANS_PAKETI_KILAVUZU.md` §1

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | Astronot basınç giysisi / S00-S11 |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ | Titanyum göğüs plakası ve termo-valf / S00-S11 |
| T3 | oranı sözle yazılamayan nesne | ⬜ | — |
| T4 | insan dışı canlı | ⬜ | — |
| T5 | tekrar eden insan dışı olay | ✅ | Jeotermal erime damar parıltısı / S02-S11 |
| T6 | bir varlık tekrar tekrar dönüyor | ✅ | Astronot kaskı ve vizör arkası |

```
KARAR: REFERANS PAKETİ YAZILIR (KAPI 0)
⚠️ T1, T2, T5, T6 tetiklendi. KAPI 0 geçerlidir: Referans paketi yazılmadan ve kilit görseller onaylanmadan sahne üretimi başlamaz.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S08 (Dış Yalıtım Katmanının Sökülmesi)
NÖTR TARİFİ:         Astronot sol eliyle göğüs zırhındaki mat pirinç rotary termo-valf diskini dairesel döndürür ve göğüs plakasındaki yalıtım contasını serbest bırakarak zırh iç ısı kanalını aktive eder.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Jeotermal hat bağlantısını kurarak astronot basınç giysisinin bitmek üzere olan termal bataryasını şarj etmek.
ENGEL:   Termal batarya şarj oldukça giysi dış yüzeyi ısınır ve üzerinde durduğu 88 K kompozit buz zeminini eriterek altında metan uçurumu açar.
BEDEL:   S08'de dış yalıtım katmanını bilerek söküp ısıyı zemin yerine giysi içine yönlendirerek giysi devrelerini yakma pahasına donmaktan korunmak.
MUHATAP: Ortam (88 K kriyojenik kompozit zemin ve pasif jeotermal hat bağlantısı).
AYRILIK: S07 (Astronotun sıcak ama kırılgan sol taraf ile soğuk ama sağlam sağ taraf arasında kalıp bilinçli olarak yalıtımı sökme kararı aldığı an).
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅
☑ risk sayımı yazıldı ve eşik kararı verildi (3 < 5)
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S08)
→ üçü de ✅, 03_SAHNE_SIRALAMASI.md yazılabilir.
```
