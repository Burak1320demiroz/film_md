---
name: qa-isle
description: QA raporu işleme akışı (AGENTS.md Kart C/D/E/E3/F/F2 + ortak kapılar ①-⑪). Bir QA/critique raporu yapıştırıldığında veya "rapor geldi", "kare/devamlılık/ses/hikaye/arka plan/fizik raporu" dendiğinde MUTLAKA kullan. Girdi: film klasörü ve varsa master video yolu.
allowed-tools: Bash(bash:*), Bash(python3:*), Bash(ls:*), Bash(ffprobe:*), Bash(ffmpeg:*), Read, Grep, Glob, Write, Edit
---

# QA raporu işleme — kapı sırası

Kaynak: AGENTS.md §3 "C/D/E/E3/F/F2'NİN ORTAK ADIMLARI" + merceğe özel kart.
Bu skill SIRAYI ve ⛔ satırlarını taşır; ayrıntı AGENTS.md'den okunur.
Çelişkide AGENTS.md kazanır. Skor yazmadan önce ilgili kapı defterleri
film kaydına yazılmış olmalıdır.

## 0. Mercek tespiti
Raporun başlık/kategori yapısından hangi mercek olduğunu belirle:
① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK ·
⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK.
(①-④ zorunlu; ⑤-⑧ risk tetikli; ⑨-⑫ KOŞUL tetikli plan sadakati — 00_README.
⛔ ⑨-⑫ SPEC'siz koşulmaz, mod V satırı tabloya girmez; ölçüm HAM ZİNCİR
dediyse HİÇBİR mercek koşulmaz [D181 · D184])
Malzeme FRAGMAN ise → kapı ⑧: mercek yalnız ①, satır film tablolarına girmez.

## 1. ⑪ ÖLÇÜM KAPISI — sıraca en önce, master eldeyse

⛔ **⑪.0 ÖNCE KİMLİK [D160].** Dosya adı kimlik değildir; kapak kartı da değil.
Master yolu verilmediyse aynı ada uyan HER dosyayı listele ve ölç — farklı
SÜRE = farklı kurgu. Sonra kurgunun ORTASINDAN tek kare çıkar ve **BAK**:

```
ffmpeg -ss <süre/2> -i "$M" -frames:v 1 kimlik.jpg
```

Karedeki mekân/kostüm/nesne SPEC'in C bloğuna oturmuyorsa ⛔ koşu DURUR.
Hangi dosyanın ölçüldüğü film kaydına ve ham raporun künyesine YAZILIR.

```
bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master_yolu>"        # sona "rms" ekleyebilirsin
```

- Betik koşulamadıysa (master yok / ffmpeg yok): "ölçüm yapılamadı" diye kaydet
  ve raporun süre/sahne sayılarını HİÇBİR kapıya sokma.
- SES KANALI: YOK + plan sesli → 🔴 TESLİM KUSURU: parti durur, master yeniden
  ihraç edilir, dört mercek yeniden koşulur [D136].
- Rapor ile ölçüm çelişirse ÖLÇÜM kazanır; o merceğin satırı ŞARTLI olur.
- Ölçüm, film kaydına "§ÖLÇÜM KAPISI" tablosu olarak yazılır.
- ⛔ Betik SONA **TESLİM SINIFI** satırı basar [D181]: LUFS sapması > 3 LU ya da
  kuyrukta ≥1,5 s donma → 🚨 **HAM ZİNCİR**. Filigran ve klip sayısı `⬜ GÖZ`/`⬜ SPEC`
  olarak açık kalır; biri 🔴 ise sınıf zaten HAM ZİNCİR'dir.
  **HAM ZİNCİR çıkarsa MERCEK KOŞULMAZ, rapor OKUNMAZ, satır YAZILMAZ.**
  Sıra: KURGU → ÖLÇÜM → MERCEK.
- Betik KUYRUK/BAŞ KART ŞÜPHESİ (freezedetect) ve `son_kare.jpg` de basar [D70/72 · 9 vaka];
  şüphe varsa kart kesilir ve ⑪ yeniden koşulur — kart S0↔son sahne eş kadraj çiftini öldürür.
- Betik ayrıca LUFS/true peak (ihraç kilidi −14 / −1,0) ve KÖŞE TESTİ (`kose_SA.png`)
  basar: aynı köşede aynı ikon her örnekte → 🔴 FİLİGRAN, master yeniden ihraç [D150].
- Karanlık filmde kesme dedektörü kördür: ızgarayı silencedetect deliklerinden ve
  kart başından oku (10 s katına oturuyorsa ızgara odur); I-frame'lere bakma.
- Tartışmalı saniyelerin karesini ÇIKAR ve BAK (`select=eq(n,…),tile=3x3`) — kilit
  defterindeki ⬜ AÇIK madde ancak kareyle FİLM SAPTI / RAPOR UYDURDU'ya kapanır.

## 2. SPEC KAPISI — önkoşul [D129]

```
ls <FILM klasörü>/*_QA_SPEC.md
```

⭐ **PAKET ZATEN VAR OLMALI** — `yeni-film` Kart A §4 onu SPEC ile birlikte üretir
[D165]. `QA_PROMPTLARI/FILME_OZEL/<FILM>/` yoksa Kart A adımı atlanmıştır: burada
üret, ve filmin kaydına tek satır düş (paket QA anında doğuyorsa operatör çoktan
çıplak rubriği yapıştırmıştır — THE STILL SWARM'da sekiz mercek böyle mod V koştu).
Koşu tekrarlanacaksa yine buradan üretilir:
```
bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> [master]   → QA_PROMPTLARI/FILME_OZEL/<FILM>/
```

SPEC VARSA ve raporun ilk satırı `INPUT MODE: D` değilse → koşu TEKRARLANIR:
ham rapor 02'ye düşer, T tablosuna SATIR YAZILMAZ, kesme listesi / REMOVE
reçetesi / yeniden üretim UYGULANMAZ. ŞARTLI diye tabloya almak da yasak.

## 2b. ①.5 RAPOR KONTROL BETİĞİ [D161 · D162] — ⑤'ten ÖNCE, elle değil

```
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
        <ham raporlar…> --film <film klasörü> [--hook 10 --klip 10] --rapor \
        [--olcum-kesme <n>] [--olcum-sahne <n>]      # ⑪ ölçüldüyse ZORUNLU
```
⭐ **⑪ ölçümü hakemdir.** Ölçüm bayrakları verilmezse kesme yayılımı > 1 partiyi
toptan düşürür [D107]; ölçüm verilince parti ayakta kalır, yalnız sapan mercek
şartlı olur. Ölçüm yoksa bayrağı UYDURMA.
⛔ **①.9 TESLİM KAPISI [D188]** — `--film` verildiğinde betik planın
`## 🎬 SAHNE n` başlıklarını SAYAR ve raporların çoğunluk sahne sayısıyla
karşılaştırır. Fark varsa parti GEÇERSİZ: **merceklerin birbirini doğrulaması
teslimi doğrulamaz**, hepsi aynı makarayı izler ve eksik makara oybirliğiyle
onaylanır. O zaman kesme listesi / REMOVE reçetesi / yeniden üretim UYGULANMAZ;
önce hangi sahnenin makarada olmadığı adıyla yazılır ve soru ÜRETİM masasına
geçer (YERÇEKİMİ F10: plan 12, makara 11, eksik olan filmin son karesiydi).

n·Σ·ort · tally · şerit · ⑨ ızgara · ④ harita↔kesme · ② sayaç boşluğu · çoklu
raporda ⑤'in beş satırı (SUSKUNLUK dahil). **GEÇERSİZ / TEKRAR → T tablosuna
satır YAZILMAZ; ŞARTLI → düzeltilmiş ortalama Ⓥ ⚠️ girer.** Betik çıktısı film
kaydına "①.5 BETİK KOŞUSU" olarak yapıştırılır.

## 3. ③ KİMLİK KAPISI (①'den önce koşulur)
Raporun sahne listesinden belgeye METİN OLMAYAN en az İKİ çapa eşlenir
(bir vuruş + bir sayısal kilit). Ekrandaki yazı çapa DEĞİLDİR.
Eşleşme < 2 → UNATTRIBUTED: ham rapor korunur, SKOR SATIRI YAZILMAZ, ders yazılmaz.

## 4. ④ KURGU KAPISI
Önce sahne-dışı malzemeyi ayıkla (süre ölçüt değildir; kurgu ortasındaysa koşu durur).
Sonra üç satır doğrula: klip sayısı = SCENE COUNT · süre = RUNTIME ±2s ·
sıra = İNSAN ŞERİDİ [D118]. Tutmayan varsa "değil" deyip durma — Δ'yı OKU
(AGENTS ④'teki prosedür: insansız yuva eşleme → fazla/eksik klip → replik ekseni);
koşu ÖN KOŞU olur, film boyu kategoriler sayı taşımaz.

## 5. Çapraz kapılar
- Aynı dosyaya birden çok mercek koşulduysa → ⑤: sayım + replik (`LINES HEARD`)
  + şerit (`PRESENCE STRING`) satırları yan yana yazılır.
- Mod V raporlarında → ⑦ parmak izi kapısı (son iki koşunun künyesi yan yana).
- Plan eldeyse → ⑨ hizalama: ızgara PLANDAN alınır,
  `sahne başlangıcı(n) = hook + (n−1) × klip`.

## 6. Merceğe özel kart
AGENTS.md'de ilgili kartı AÇ ve uygula: C(①) · D(④) · E(②) · E3(③) · F(⑤) ·
F2(⑥) · F3(⑦) · F4(⑧) · F5(⑨) · F6(⑩) · F7(⑪) · F8(⑫).
Kartların ⛔ ön satırları: ① FORMAT kapısı · ② iki yarı + doküman verilmez ·
③ AUDIO STATE + register doğrulaması · ⑤ özne kapısı · ⑥ mod kapısı +
cetvelsiz FAIL düşer · ⑨ kare-önce + kafiye çifti · ⑩ kanal kaydı (kask
kapalı → yüz N/A) + cümle kapısı · ⑪ ortam yasası + planlı sınır PASS ·
⑫ kesme ÖNERMEZ + üç saniye tahmin → 08 yayın tablosu. ⑩ ÖNERME KAPISI her mercekte: bulgu planın logline +
sahne haritası + kilit listesine karşı okunur; düşen bulgunun puanı geri verilir,
toplam yeniden hesaplanır, kalanlar SPEC C-bloğuna göre yeniden sıralanır.
⛔ **⑩ DÜŞÜRDÜKTEN SONRA SINIRI SORAR [D183].** Novum yüzünden düşen her bulgu
için SPEC'in NOVUM bloğundaki `⛔` cümlesi (kuralın nerede BİTTİĞİ) okunur ve
KAREYLE sınanır — `rapor_kontrol.py` ①.7 o cümleyi ekrana basar. Kept Light'ta
düşen "TWO GRAVITIES" hükmünün altında sınanmamış bir SINIR İHLALİ duruyordu.

## 7. Kayıt zinciri — sırası değişmez
1. HAM rapor OLDUĞU GİBİ → `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/` (kural ④).
2. Film kaydı → `.../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/<FILM>.md` (kapı defterleri buraya).
3. ⛔ `rapor_kontrol.py` GEÇERSİZ/TEKRAR dediyse bu adım ATLANIR. Skor satırı DOĞRU tabloya: ① → T1 · ② → T2 ·
   ③ → T3 · ④ → T4 · ⑤ → T5 · ⑥ → T6 · ⑦ → T7 · ⑧ → T8 · ⑨-⑫ → T9-T12
   (⑨-⑫'de mod V satırı YOKTUR). Geçerlilik işareti: ✅ / ⚠️ ŞARTLI / 🚨.
4. `.../FILM_QA_RAPORLARI/00_INDEX.md` sayım + tamlık matrisi.
5. Yeni ders çıktıysa → AGENTS.md Kart G.
6. Commit ATILMAZ — "commit'e hazır" diye raporla.

## Mazeret çürütme

| İçinden geçen düşünce | Gerçek |
|---|---|
| "Rapor çok detaylı, ölçüme gerek yok" | Altı mercek aynı yanlış kesme listesini verdi; komut satırında cevabı duran soru modele sorulmaz [D125]. |
| "SPEC var ama bu mod V koşusunu da işleyeyim" | İşlenir ama tabloya girmez; ŞARTLI diye almak onu yapılmış saymaktır [D129]. |
| "Bulgu çok mantıklı, plana bakmak vakit kaybı" | Dört mercek filmin PLANLI FİNALİNİ kesmeyi önerdi [⑩]. |
| "Skorlar yakın, aynı kabul edilebilir" | 1.5'tan küçük fark GÜRÜLTÜDÜR (kural ⑥); kapılar eşikle koşulur, hisle değil. |
