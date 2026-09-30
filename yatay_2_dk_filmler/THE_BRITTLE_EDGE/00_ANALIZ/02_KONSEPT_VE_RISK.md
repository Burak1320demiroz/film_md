# 🧠 THE_BRITTLE_EDGE — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     sahip verdi
   THE BRITTLE EDGE — Kırılma Sınırı. Ay kraterinde donan çelik çekme kulağının gevrek kırılması ve yöntemin değiştirilmesi.
② FORMAT:   yatay 2-4 (2 dk) → kart §2.2 · bölüm sayısı 2
③ SAHNE:    12        → formatın varsayılanı (12 sahne × 10s = 120s)
④ REFERANS PAKETİ: YAZILMASIN (analiz kararı: tek astronot opak vizörlü, araç sabit geometrik şasi, PLAN'a gerekçe yazılacak)
   PLAN'a düşecek TEK SATIR gerekçe: Tek astronot opak vizörlüdür, sarı araç basit geometrik şasidir; biçim çapa kelimeleriyle korunur [D74].
⑤ HİKÂYE ONAYI (14.09.2026): `00_HIKAYE_ONAYI.md` ONAY: 20.09.2026 · sahip · TUR 1/3
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "Ay’ın karanlık bir kraterinde, tek bir astronot mahsur kalmış sarı keşif aracını vinçle çekmektedir. Metal çekme bağlantısı aniden kopar. Araç geriye kayar; ön tekerlekleri bir kaya çıkıntısına takılırken arka tekerlekleri uçuruma sarkar. Astronot donanımını inceler; metalin bükülmeden, cam gibi kırıldığını anlar: aşırı soğuk, çeliği gevrekleştirmiştir. Çekmeye devam ederse diğer parçalar da kırılacaktır. Yöntemi değiştirir. Aracı doğrudan çekmek yerine, gövdenin altına esnek bir kurtarma sapanı geçirir. Yükü tek bir noktaya değil, tüm şasiye dağıtır. Son aşamada araç kaya çıkıntısından kurtulurken bir an tamamen askıda kalır; yeni bağlantı dayanır ve araç güvenli zemine çekilir. Astronot kırık metal parçasına bakar; güç uygulamak değil, gücü doğru yere uygulamak hayat kurtarmıştır."
REPLİK: yok (diyalogsuz film)
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "Cam gibi kırılma / cam tozu" | Metaller donunca cam veya kristal toza dönüşmez; süneklik kaybıyla gevrek kırılır | Keskin, düz, mikro-çentikli kriyojenik gevrek kırılma (DBTT) | MIT Kırılma Mekaniği kuralı, D192 |
| "Kalkan toz zemine geri düşer" | Ay vakumunda hava direnci yoktur; toz havada asılı kalmaz veya süzülmez | Kalkan regolit parçacıkları havada dağılmadan yavaş balistik parabolle yere iner | §3.1 VAKUM ortam kartı |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 2-4 (2 dk)  → §2.2 kartı
ORTAM:         §3.1 VAKUM (Ay kutup krateri) → tetiklediği zorunlu satırlar: mutlak dış sessizlik, 0,16g düşük yerçekimi, sert gölgeler, balistik toz
TÜR:           bilimkurgu · dal: sert bilimkurgu (hard sci-fi) → §4.1
KLİP SÜRESİ:   10.0 s  ⛔ ARAÇTAN ÖLÇÜLDÜ [D124], seçilmedi
SAHNE SAYISI:  12    RUNTIME: 120s = 10s + 11 × 10s
BÖLÜM SAYISI:  2    (Bölüm 1: S00-S05; Bölüm 2: S06-S11)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Kriyojenik sıcaklıkta çelik çekme kulağı sünekliğini kaybederek sünek-gevrek geçiş sıcaklığı (DBTT) altında bükülmeden aniden çatlar.
NOVUM TAŞIYICISI:    Çelik çekme kulağı × vinç gerilimi → bükülmeden ayrılma
① TEK KARE:          Kırık çelik çekme kulağının iki ayrık parçası ve sarı keşif aracı gövdesi aynı kadrajda görünür.
② KİNETİK BAĞIMSIZLIK: ✅ Metalin bükülme olmaksızın keskin kopuşu ve eldivenli parmakların kırık yüzeyi incelemesi hiçbir söz/yazı olmadan anlaşılır.
③ BAŞLIK ŞEMASI:     THE BRITTLE EDGE (3 kelime ≤ 5)
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — UYUM VE ÖĞRENME (Kuvvet yerine metot değişimi)
▸ tanım cümlesi — Fiziksel direnç kör kuvvetle aşılamadığında, hayatta kalmak yöntemi ve yükün dağılımını yeniden tasarlamayı gerektirir.
▸ depoda kaç kez kullanıldı — 0 (yeni aday tema; en yakın FEDAKÂRLIK 3)
▸ motif kanalları — Kırık çelik kulak vs esnek sapan (nesne) · eldivenli parmakların kırık yüzeye dokunuşu ve gergin diz çöküş (kinesik) · alçak açıdan gerilen şasi (kamera) · kraterin karanlık gölgesinde parlayan metal kenar (ışık)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

> ⛔ **PLAN YAZILMADAN ÖNCE.** 5+ risk çıkıyorsa KİLİT TAVANI (≤ 20 ders kilidi) —
> malzeme azaltılmaz; dışarıda kalan kilitler PLAN `UYGULANMAYAN KİLİTLER`e gerekçeyle
> (14.09.2026, 02_RISK_KARTLARI §RİSK TOPLAMI).

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| R1 (Kopma/Kırılma) | ✅ | Vinç gerilimi altında metal ayrılması | Kıvılcım ve patlama yok, sessiz mekanik çatlama | Düşük |
| R4 (Uçurum/Eğim) | ✅ | Aracın krater yamacında kayması | Ön tekerleğin kaya çıkıntısına oturması | Düşük |
| R7 (Askıda Kütle) | ✅ | S08-S09'da aracın boşlukta asılı kalması | I2V zinciri ile start-frame kilitli devamlılık | Orta |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  S00'da metal kopmasının görselleşmesi (cam tozuna / kıvılcıma dönüşme riski)
POZİTİF BİÇİMİ:   2 parçaya ayrılan çelik halka, 1 keskin çatlak hattı, 0 kıvılcım, 0 cam tozu, 2 saniyede 1,5 metre geri kayma.
```

```
TETİKLENEN RİSK:  3 / 12
EŞİK:             5
Sonuç:            Eşik altında, malzeme çıkarmaya gerek yok.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — yalnız soru ④ "analiz karar versin" ise

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | Astronot Ekin (S00-S11) |
| T2 | biçim kilidi METİNLE tutulmayan varlık | — | Sarı keşif aracı standart geometrik rover gövdesidir |
| T3 | oranı sözle yazılamayan nesne | — | Standart silindirik vinç ve dikdörtgen şasi |
| T4 | insan dışı canlı | — | Yok |
| T5 | tekrar eden insan dışı olay | — | Yok |
| T6 | bir varlık tekrar tekrar dönüyor | — | Yok |

```
KARAR: YAZILMAZ (İsteğe bağlı kuralı · 08.09.2026 sahip kararı)
PLAN gerekçesi: Tek astronot opak vizörlüdür (yüz morph riski yok), sarı araç belirgin basit geometrik formdadır; biçim çapa kelimeleriyle korunur [D74].
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S00
NÖTR TARİFİ:         İki metal silindirik halkanın çekme gerilimi altında ayrılması, sarı metal şasinin eğimli regolit zeminde kayması.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Mahsur kalmış sarı keşif aracını krater terasına çekip kurtarmak.
ENGEL:   Dondurucu soğukta gevrekleşen metal çekme noktasının kopması ve doğrudan çekmenin imkânsızlaşması.
BEDEL:   S08'de aracın son kaya çıkıntısı desteğinin kaybolması; astronotun emniyetli temas noktasını yitirmesi.
MUHATAP: Aracın 0,16g Ay kütlesi ve kraterin derin uçurumu.
AYRILIK: S— (tek insanlı film).
```

---

## ✅ KAPI

```
[x] konsept kapısı ①②③ üçü de ✅
[x] risk sayımı yazıldı ve eşik kararı verildi (3 risk ≤ 5)
[x] B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S08)
→ üçü de ✅, 03_SAHNE_SIRALAMASI.md yazılabilir.
```
