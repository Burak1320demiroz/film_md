# 🧪 THE_FURNACE_GATE — Yeniden Test Paketi · Bölüm 4 (C73–C96)

> **Tarih:** 18.10.2026 · **Yazan:** Fable · **Neden:** `ODA/QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU_BOLUM_4.md` §0 — dört raporun üçü
> geçersiz kaynak işaretli. Sorunlar şunlar:
> - parçalar 90 s'den uzun (4 dk);
> - "ne olmalı" bloğu ve kesme listesi doldurulmadı;
> - çıktılar Türkçe geldi;
> - izleme B bir simülasyon.
>
> Bu dosya testleri **kurallara uygun** koşmak için yapıştırmaya hazır girdileri verir. Promptların kendisi
> `uretim_hatti/QA_PROMPTLARI/`'nda; burada yalnız her teste eklenecek blok ve komut var.
> **Kurallar** (QA_PROMPTLARI başlıkları):
> - her koşu **yeni bir Gemini sohbetinde**;
> - plan, hikâye, logline, film adı verilmez;
> - parça ≤ 90 s;
> - çıktı **İngilizce** kalır (prompt "in English" diyor; Türkçe istenirse rapor geçersiz sayılır).
>
> Komutlar `bash` içindir. Senin kabuğun zsh olduğu için her blok `bash <<'EOF' … EOF` ile sarıldı; olduğu gibi yapıştır.
> Video yolu: `~/film_medya/THE_FURNACE_GATE/cikti/taslak_01_P4.mp4` (TEST 0). Yeniden kurgudan sonra `taslak_02_P4.mp4` olur.

---

## TEST 0 · Medyayı hatta al — şimdi

Bu raporun çekim eşlemesi içerik çapasıyla yapıldı; çünkü `timeline.json` şablon ve `~/film_medya/THE_FURNACE_GATE/` boş.

1. Parça videolarını `~/film_medya/THE_FURNACE_GATE/cikti/` altına koy: `taslak_01_P1.mp4` … `taslak_01_P4.mp4`.
2. Ham klipleri `ham/` altına koy: `C73_d1.mp4` biçimi.
3. 15 referans sayfasını `ref/` altına koy: FILM §3 adları, örn. `3.KESTREL_v1.png`.
4. Claude Code'da `/medya-denetle` çalıştır. Ham klipler `medya.py al` ile NOTLAR DENEMELER'e yazılır; montaj `medya.py bol` ile `timeline.json`'a geri kurulur.
5. Eşlemeyi doğrula:

```bash
bash <<'EOF'
cd ~/github/apex_md/film_md
python3 uretim_hatti/araclar/kurgu.py kontrol yatay_16_dk_filmler/THE_FURNACE_GATE/timeline.json
for t in 12:00.0 12:33.0 13:10.0 13:48.0 14:28.0 15:32.0 15:50.0; do
  python3 uretim_hatti/araclar/kurgu.py liste yatay_16_dk_filmler/THE_FURNACE_GATE/timeline.json --zaman "$t"
done
EOF
```

Beklenen sonuç: C73 · C76 · C80 · C83 · C87 · C94 · C96. Bir tanesi bile tutmazsa `NOTLAR.md` P4 satırlarının çekim sütunu yeniden yazılır.

---

## TEST 1 · KARE MODU — şüpheli 8 pencere (mevcut taslakla, şimdi)

Gemini videoyu saniyede 1 kareyle okur; 1 saniyeden kısa kusur videodan kaçar (TARAMA başlığı).

| # | Pencere (parça içi) | Çekim | Bakılacak |
|:--:|---|:--:|---|
| 1 | 00:00–00:09 (aralık 0,5) | C73 | konsoldaki çekirdek: küre mi, dikdörtgen grafit kasa mı? itişte lamba ve kollar değişiyor mu? |
| 2 | 00:33–00:36 | C76 | sol kumanda kolu eriyor mu? |
| 3 | 00:36–00:39 | C76 | dudaklar ikinci "I'm coming back" için oynuyor mu (sesi kısınca sessiz dudak kalır mı)? |
| 4 | 00:43–00:46 | C77 | tether ucu sert çubuğa dönüşüyor mu? |
| 5 | 01:06–01:09 | C79 | iki kumanda kolu birleşiyor mu? |
| 6 | 01:47–01:50 | C83 | kenar çerçevesi hangi karede başlıyor? |
| 7 | 02:27–02:30 | C87 | burun halkası gövdeden kopuyor mu? |
| 8 | 03:31–03:36 | C94 | kutu ikiye bölünüp yeni modül türüyor mu? |

```bash
bash <<'EOF'
cd ~/github/apex_md/film_md
P4=~/film_medya/THE_FURNACE_GATE/cikti/taslak_01_P4.mp4
H=~/film_medya/THE_FURNACE_GATE/analiz/tarama
mkdir -p "$H"
# ad:başlangıç_s:süre_s:aralık_s
for p in C73:0:9:0.5 C76:33:3:0.25 C76b:36:3:0.25 C77:43:3:0.25 C79:66:3:0.25 C83:107:3:0.25 C87:147:3:0.25 C94:211:5:0.25; do
  IFS=: read -r ad bas sure ara <<< "$p"
  ffmpeg -loglevel error -y -ss "$bas" -t "$sure" -i "$P4" -an -c:v libx264 -crf 12 "$H/P4_$ad.mp4"
  python3 uretim_hatti/araclar/kareler.py cikar "$H/P4_$ad.mp4" --hedef "$H/P4_$ad" --aralik "$ara" --sayfa
done
EOF
```

- **Gemini'ye ne verilir:** her kontak sayfası için yeni sohbet. TEST 2'de o pencerenin düştüğü parçanın ① bloğu (P4a · P4b · P4c) + `TARAMA.md` ② metni + kontak sayfası.
- **Zaman nasıl okunur:** sayfadaki kare etiketi pencerenin başından saniyedir. Film zamanı = 12:00 + pencere başı + etiket. Örnek: `P4_C76` sayfasında `1.25` → 12:34.25.
- **Ön inceleme (istersen):** kontak sayfalarını ben de okurum (Fable). Sınıfı kesinleştiren S1 cevabı yine senin işaretindir.

---

## TEST 2 · TARAMA — ≤ 90 s × 3 parça (yeniden üretimden sonra)

Parçalar, kesmeler iki parçada da kalacak biçimde birer çekim örtüşür. TEST 3 aynı dosyaları kullanır.

| Parça | Parça içi | Film | Çekimler | Süre |
|:--:|---|---|---|:--:|
| P4a | 00:00–01:20 | 12:00–13:20 | C73–C80 | 80 s |
| P4b | 01:10–02:40 | 13:10–14:40 | C80–C88 | 90 s |
| P4c | 02:30–04:00 | 14:30–16:00 | C88–C96 | 90 s |

```bash
bash <<'EOF'
P4=~/film_medya/THE_FURNACE_GATE/cikti/taslak_02_P4.mp4
O=~/film_medya/THE_FURNACE_GATE/analiz/tarama
mkdir -p "$O"
ffmpeg -loglevel error -y -ss 0   -t 80 -i "$P4" -c:v libx264 -crf 16 -c:a aac "$O/P4a.mp4"
ffmpeg -loglevel error -y -ss 70  -t 90 -i "$P4" -c:v libx264 -crf 16 -c:a aac "$O/P4b.mp4"
ffmpeg -loglevel error -y -ss 150 -t 90 -i "$P4" -c:v libx264 -crf 16 -c:a aac "$O/P4c.mp4"
EOF
```

Her parça için: yeni sohbet → aşağıdaki ① bloğu → `uretim_hatti/QA_PROMPTLARI/TARAMA.md` ② metni (birebir) → video.

**P4a (C73–C80)**
```
WHAT SHOULD BE IN THIS VIDEO
- People: never more than two people. Both always wear sealed pressure suits with closed, fully clear helmets. The woman: pearl-white suit, navy waist panels, one thin pale-teal band on each upper arm, one blue-gold round sun badge on the left chest with a graphite harness below it, and no other marking on the suit (no flags, no extra patches). The man: ivory suit, navy shoulders, one thin orange band on each upper arm, one blue-gold hawk badge on the left chest, and no other marking on the suit.
- Environment: pressurised rooms and cabins inside; hard vacuum outside: no air, so no billowing smoke, no rolling flames and no hanging dust. Engines in vacuum show a short bright core and a pale plume that fades at once.
- Sound: final mix. Exterior vacuum shots: only a low steady background tone, radio voices and soft muffled thuds felt through a hull; no sharp clangs, no engine roar, no explosion sounds. Inside: soft ventilation or a machinery hum, and voices.
- Camera: 00:10–00:20 and 01:10–01:20 locked off; every other shot a slow push-in or a slow glide.
- Main object: one small ivory wedge-shaped tug with a graphite underside, a narrow orange nose band, a smoked-blue canopy, two round rear thrusters and four short radiator fins, the same tug every time it appears; one long ivory colony ship with a segmented hull; a rigid square loading bridge with glass sides; a navy safety tether with a silver anchor block; a compact rectangular graphite power core with ivory corner guards and a dark glass centre.
```

**P4b (C80–C88)**
```
WHAT SHOULD BE IN THIS VIDEO
- People: never more than two people. Both always wear sealed pressure suits with closed, fully clear helmets. The woman: pearl-white suit, navy waist panels, one thin pale-teal band on each upper arm, one blue-gold round sun badge on the left chest with a graphite harness below it, and no other marking on the suit (no flags, no extra patches). The man: ivory suit, navy shoulders, one thin orange band on each upper arm, one blue-gold hawk badge on the left chest, and no other marking on the suit.
- Environment: pressurised cabins inside; hard vacuum outside: no air, so no billowing smoke, no rolling flames and no hanging dust. Engines in vacuum show a short bright core and a pale plume that fades at once.
- Sound: final mix. Exterior vacuum shots: only a low steady background tone, radio voices and soft muffled thuds felt through a hull; no sharp clangs, no engine roar, no explosion sounds. Inside: soft ventilation and voices.
- Camera: 00:00–00:10 and 00:40–00:50 locked off; 00:10–00:20 a smooth sideways track; 01:00–01:10 a steady wide frame; 01:10–01:18 fixed, then a slow drift to the left; every other shot a slow push-in.
- Main object: one small ivory wedge-shaped tug with a graphite underside, a narrow orange nose band, a smoked-blue canopy, two round rear thrusters and four short radiator fins, the same tug every time it appears; one long ivory colony ship with a segmented hull; one small rigid graphite security drone with a single narrow red sensor strip; a small round docking socket with one broad hinged clamp, beside a short railed catwalk behind heavy blast ribs.
```

**P4c (C88–C96)**
```
WHAT SHOULD BE IN THIS VIDEO
- People: never more than two people. Both always wear sealed pressure suits with closed, fully clear helmets. The woman: pearl-white suit, navy waist panels, one thin pale-teal band on each upper arm, one blue-gold round sun badge on the left chest with a graphite harness below it, an unmarked ivory wrist unit on her right wrist, and no other marking on the suit. The man: ivory suit, navy shoulders, one thin orange band on each upper arm, one blue-gold hawk badge on the left chest, and no other marking on the suit.
- Environment: pressurised cabins and rooms inside; hard vacuum outside: no air, so no billowing smoke, no rolling flames and no hanging dust. Engines in vacuum show a short bright core and a pale plume that fades at once.
- Sound: final mix. Exterior vacuum shots: only a low steady background tone, radio voices and music; no sharp clangs, no engine roar, no explosion sounds. Inside: soft ventilation or a machinery hum, and voices.
- Camera: 00:10–00:20, 00:30–00:40 and 00:40–00:50 locked off; 00:20–00:30 the view through the window moves gently; 01:00–01:10 a slow push-in; 01:20–01:30 a slow pullback; every other shot nearly still with a very slight push-in.
- Main object: one small ivory wedge-shaped tug with a graphite underside, a narrow orange nose band, a smoked-blue canopy, two round rear thrusters and four short radiator fins, the same tug every time it appears; one long ivory colony ship with a segmented hull, six low blocks and two large blue rear engines; one huge circular gate with three rigid sliding shutters; a compact rectangular graphite power core with ivory corner guards and a dark glass centre, sitting latched in a console cradle.
```

---

## TEST 3 · SÜREKLİLİK — aynı 3 parça, kesme listeli (yeniden üretimden sonra)

Her parça için: yeni sohbet → ① blok + kesme listesi → `uretim_hatti/QA_PROMPTLARI/SUREKLILIK.md` ② metni (birebir) → video.

**SAME/NEW nereden geliyor:** FILM §6 GEÇİŞ tablosundan. "Aynı mekân" = SAME; "mekân değişimi" = NEW. Zamanlar parçanın başına göre kaydırıldı. NEW kesmede yalnız S1 bakılır. Tug kimliği bu yüzden NEW kesmelerde ölçülmez; onu TEST 5 ölçer.

**P4a**
```
WHAT SHOULD BE IN THIS VIDEO
- People: the woman: pearl-white suit, navy waist, one thin pale-teal band on each upper arm, one blue-gold round sun badge on the left chest, nothing else on the suit. The man: ivory suit, navy shoulders, one thin orange band on each upper arm, one blue-gold hawk badge on the left chest, nothing else on the suit. Helmets always closed and clear.
- Environment: pressurised rooms and cabins inside; hard vacuum outside, one blue gas giant in the background, cold starlight from the upper left.
- Sound: final mix: no sound in exterior vacuum shots except a low steady tone and radio voices.

CUT LIST   (time · from → to · SAME = same place and continuous time · NEW = place or time jumps)
1  00:10.0  C73 → C74  NEW
2  00:20.0  C74 → C75  NEW
3  00:30.0  C75 → C76  NEW
4  00:40.0  C76 → C77  NEW
5  00:50.0  C77 → C78  NEW
6  01:00.0  C78 → C79  NEW
7  01:10.0  C79 → C80  NEW
```

**P4b**
```
WHAT SHOULD BE IN THIS VIDEO
- People: the woman: pearl-white suit, navy waist, one thin pale-teal band on each upper arm, one blue-gold round sun badge on the left chest, nothing else on the suit. The man: ivory suit, navy shoulders, one thin orange band on each upper arm, one blue-gold hawk badge on the left chest, nothing else on the suit. Helmets always closed and clear.
- Environment: pressurised cabins inside; hard vacuum outside, one blue gas giant in the background, cold starlight from the upper left.
- Sound: final mix: no sound in exterior vacuum shots except a low steady tone, radio voices and soft muffled hull thuds.

CUT LIST   (time · from → to · SAME = same place and continuous time · NEW = place or time jumps)
1  00:10.0  C80 → C81  SAME
2  00:20.0  C81 → C82  NEW
3  00:30.0  C82 → C83  NEW
4  00:40.0  C83 → C84  NEW
5  00:50.0  C84 → C85  SAME
6  01:00.0  C85 → C86  NEW
7  01:10.0  C86 → C87  NEW
8  01:20.0  C87 → C88  NEW
```

**P4c**
```
WHAT SHOULD BE IN THIS VIDEO
- People: the woman: pearl-white suit, navy waist, one thin pale-teal band on each upper arm, one blue-gold round sun badge on the left chest, an ivory wrist unit on her right wrist, nothing else on the suit. The man: ivory suit, navy shoulders, one thin orange band on each upper arm, one blue-gold hawk badge on the left chest, nothing else on the suit. Helmets always closed and clear.
- Environment: pressurised cabins and rooms inside; hard vacuum outside, one blue gas giant in the background, cold starlight from the upper left.
- Sound: final mix: no sound in exterior vacuum shots except a low steady tone, radio voices and music.

CUT LIST   (time · from → to · SAME = same place and continuous time · NEW = place or time jumps)
1  00:10.0  C88 → C89  NEW
2  00:20.0  C89 → C90  NEW
3  00:30.0  C90 → C91  NEW
4  00:40.0  C91 → C92  SAME
5  00:50.0  C92 → C93  NEW
6  01:00.0  C93 → C94  NEW
7  01:10.0  C94 → C95  NEW
8  01:20.0  C95 → C96  NEW
```

Kesme 8 (C95 → C96) planda 0,6 s karışım: taslakta da karışımsa satırın sonuna `(dissolve)` ekle.

---

## TEST 4 · ANLATIM — 3. ve 4. parça birlikte (yeniden üretimden sonra)

Çekirdeğin feda edildiği an (C69) 3. parçada. Yalnız 4. parça izlenince "çekirdeğe ne oldu" sorusu ölçülemiyor. İkinci yarı tek video yapılır:

```bash
bash <<'EOF'
C=~/film_medya/THE_FURNACE_GATE/cikti
I=~/film_medya/THE_FURNACE_GATE/izleyici
mkdir -p "$I"
printf "file '%s'\nfile '%s'\n" "$C/taslak_02_P3.mp4" "$C/taslak_02_P4.mp4" > "$I/ikinci_yari_liste.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$I/ikinci_yari_liste.txt" -c:v libx264 -crf 18 -c:a aac "$I/taslak_02.mp4"
EOF
```

- **Ne verilir:** yeni sohbet → `uretim_hatti/QA_PROMPTLARI/ANLATIM_TESTI.md` kod bloğu (birebir) → `taslak_02.mp4`, sesli. Dosya adı nötr kalır; film adı, plan ve replik metni verilmez.
- Çıktı İngilizce gelir. Sohbete yapıştırınca çekim çekim karşılaştırmasını ben yaparım.
- Parça 4'ten ölçülecek beş an (video içi zaman = film zamanı − 8:00):
  - 04:10 (C74) — köprü çekiliyor mu?
  - 04:40 (C77) — süre baskısı okunuyor mu?
  - 05:10 (C80) — tug ayrılıyor mu?
  - 05:20 (C81) — köprü geri çekilmiş mi?
  - 07:30 (C94) — çekirdek aynı yuvada mı?

---

## TEST 5 · Kimlik kontak sayfası — tug · Rhea · Leon (şimdi, TEST 0'dan sonra)

Her çekimin 5. saniyesinden bir kare alınır ve referans sayfalarıyla yan yana konur.

```bash
bash <<'EOF'
P4=~/film_medya/THE_FURNACE_GATE/cikti/taslak_01_P4.mp4
K=~/film_medya/THE_FURNACE_GATE/analiz/kareler/P4_kimlik
mkdir -p "$K"
# çekim:parça_içi_saniye  (tug × 8 · Rhea × 8 · Leon × 7; C86 C88 C95 ikisinde ortak)
for p in C80:75 C81:85 C84:115 C85:125 C87:145 C89:165 C92:195 C96:235 \
         C73:5 C75:25 C77:45 C83:105 C86:135 C88:155 C93:205 C95:225 \
         C76:35 C78:55 C79:65 C82:95; do
  c=${p%%:*}; t=${p##*:}
  ffmpeg -loglevel error -y -ss "$t" -i "$P4" -frames:v 1 "$K/$c.png"
done
ls "$K"
EOF
```

Sonra bana "TEST 5 hazır" yaz. devamlilik ajanı (kare modu, 1 çağrı · AJAN_CAGRI 31 → 32) şunları karşılaştırır:
- tug kareleri ↔ `ref/3.KESTREL_v1.png`;
- Rhea kareleri ↔ `ref/2.RHEA_v1.png`;
- Leon kareleri ↔ `ref/1.LEON_v1.png`.

Ölçütler `KIMLIK_VE_REFERANS_KILAVUZU` §6 (kare kapısı): rozet biçimi ve konumu · bant sayısı ve kolu · bayrak/yazı yokluğu · itici ve kanatçık sayısı · burun biçimi.
Sonuç doğrudan iki işe yarar: K4 kararının (hangi tug doğru) kanıtı olur ve 5.2'deki yeniden üretim listesi kesinleşir.

---

## TEST 6 · İZLEME B — gerçek izleyici (final öncesi)

- Kimler: hikâyeyi bilmeyen 2-3 kişi, ayrı ayrı.
- Nasıl: kulaklıkla, sesli, baştan sona. Tercihen tam film; olmazsa TEST 4'teki ikinci yarı.
- İzlemeden önce hiçbir şey anlatılmaz: konu, ad, "uzayda geçiyor" bile.
- Sorular: `uretim_hatti/QA_PROMPTLARI/IZLEME_FORMU.md` B bölümündeki 8 soru, kişinin kendi kelimeleriyle yazılır.
- Bu parçada ayrıca sorulacak üç an (soruya ipucu katmadan, "orada ne oldu?" diye):
  - 12:10–12:30: köprü;
  - 14:10 sonrası kokpit: koltuklar "yer değiştiriyor" muydu?;
  - 15:30: çekirdek.
- Cevapları buraya yapıştır; `NOTLAR.md` İZLEME'ye B1 · B2 · B3 olarak girer. Simülasyon B satırı yayın onayına sayılmaz.

---

## TEST 7 · Mekanik — her yeni taslakta

```bash
bash <<'EOF'
cd ~/github/apex_md/film_md
TL=yatay_16_dk_filmler/THE_FURNACE_GATE/timeline.json
python3 uretim_hatti/araclar/kurgu.py kontrol "$TL"
python3 uretim_hatti/araclar/kurgu.py yukseklik ~/film_medya/THE_FURNACE_GATE/cikti/taslak_02_P4.mp4
python3 uretim_hatti/araclar/kareler.py dikis -h
EOF
```

- `kurgu.py kontrol`: her video parçası 10 s; eksik ya da bozuk dosya ❌ olmamalı.
- `kurgu.py yukseklik`: hedef −14 LUFS, tepe ≤ −1 dBTP.
- `kareler.py dikis`: `-h` çıktısındaki biçimle, SAME kesmelerde (C80→C81 · C84→C85 · C91→C92) çalıştırılır. Komutu taslak timeline'a göre ben yazarım.

---

## Sonuç nasıl işlenir

Çıktıları sohbete yapıştır. Akış şöyle:
- **Kayıt:** `NOTLAR.md`'ye P4 satırı olarak girer, "taslak_02" sürümüyle.
- **Doğrulama:** ilk koşudaki aynı bulgu (±2 s, aynı nesne) yeniden çıkarsa satır birleşir ve kaynağı "geçerli" olur (QA_OKUMA §4).
- **Kalibrasyon:** senin ✅/❌ işaretinle başlar (QA_OKUMA §3).
