---
name: prompt-kontrol
description: Üretim öncesi prompt denetim kapısı (AGENTS.md Kart P). Film promptları yazıldığında veya "üretime geçelim", "promptlar hazır", "video/imaj üretelim" dendiğinde TEK KARE ÜRETMEDEN ÖNCE MUTLAKA koşulur — kullanıcı açıkça istemese bile. Girdi: FİLM KLASÖRÜNÜN yolu (tek bölüm dosyası değil).
allowed-tools: Bash(python3:*), Read, Grep, Glob, Edit
---

# Kart P — Üretim öncesi prompt denetimi

⛔ Bu kapı atlanırsa para harcanır. Sıranın kaynağı AGENTS.md Kart P'dir; burada
özetlenir, çelişki durumunda AGENTS.md kazanır.

Girdi `$1` = **film KLASÖRÜNÜN** yolu. Boşsa: üzerinde çalışılan filmi
konuşmadan / `git status`'tan belirle; emin değilsen kullanıcıya sor.
Sana tek bir bölüm dosyası verildiyse onun KLASÖRÜNÜ ver.

## 1. Betiği koş — sayıları o hesaplar, sen yazma

```
python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py $1
```

- ⛔ **Çıktıda `📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik` satırını ARA.**
  Film bölüm dosyalarına ayrıldığından beri dizi kapıları dosya sınırında
  körleşiyor (6 sahnelik dikey film ikiye bölününce dosya başına 3 video
  promptu kalır → AÇI/KURULUM kapısı HİÇ koşmaz). O satır yoksa kapı
  koşmamıştır — klasörü verdiğinden emin ol, sonra tekrar koş.
- Çıkış kodu **2 (BLOCK)** → düzelt, tekrar koş. 2 varken asla GO verme.
- Çıkış kodu **1 (FIX)** → bulguları oku; bilinçli sapma varsa film dosyasına
  TEK SATIR gerekçe yaz (D74: kaydı olmayan kapı, koşulmamış kapıdır).
- Betik bir SAYI (bant/eşik) değiştirdiyse hiçbir belgeye elle yazma —
  `prompt_kontrol.py` başındaki sözlük tek kaynaktır.

## 2. Rubriği uygula — betiğin göremediği tek şey için

Oku ve uygula: `kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md`
→ kilit SAYI mı TARİF mi · sahne hangi dersi tetikliyor · A1.

## 2b. Replikli filmde ikinci rubrik (03.09.2026 · TUR 6)

Filmde replik varsa (plan replik tablosu taşıyorsa) oku ve uygula:
`kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md`
— girdi B5 omurgası + replik tablosu (İŞLEV sütunlu) + bölüm promptları;
çıktı satır başına etiket + GO/REWRITE (sayı yok). ⛔ CUT, UNCLEAR
register ya da MONOLOGUE bulgusu varken GO verilmez — önce diyalog
düzeltilir, rubrik yeniden koşulur. Kural tarafı:
`SES_VE_DIYALOG_URETIM_KILAVUZU.md` §2a.

## 3. Karar

- **GO** → üretime geçilebilir (önce imaj; imaj onaylanınca video).
- **BLOCK** → üretme. 5+ risk çıkıyorsa kilit tavanına (≤ 20, ㉕) çekmeyi öner,
  malzeme azaltmayı değil (14.09.2026); prompt cümlesi eklemek bu bandda işe yaramıyor.
- ⭐ **Yeni rejim** (çıktıda `rejim: YENİ` — klasörde 00_HIKAYE_ONAYI.md var; 14.09.2026):
  ① `uzunluk n kelime (pozitif gövde)` BLOCK → çözüm EKLEMEK değil SİLMEKTİR: IN FRAME
  dışını sil, Bible'ı değil kadrajdakini yaz, videoda `START FRAME:` tek satır ·
  ㉖ "kadrajda olmayan YÜZ" BLOCK → yüz cümlesi silinir, IN FRAME satırı düzeltilmez
  (satırı kadraja uydur, tarifi satıra değil) · ㉗ NEGATIVE > 11 cümle FIX → film-özel
  yasaklar PLAN Negative Bible'a iner, prompta §5.1 çekirdek + ≤3 kalır ·
  ㉕ kilit > 20 FIX → `UYGULANMAYAN KİLİTLER` bloğuna gerekçeyle. Klasör modunda bu
  bulgular dosya düzeyinde tek satırda toplanır ("n prompt: satırlar…"); satırlar
  bölüm dosyasındaki satır numarasıdır. `rejim: eski` çıkıyorsa bu maddeler koşmaz
  ve koşturulmaz — eski klasör eski bantla (sahip kararı).
- 🆕 **Çok klipli sahne** (PLAN'da `SAHNE PLANI:` satırı var · 22.09.2026 sahip kararı):
  ㉜ koşar. ㉜① plan toplamı ↔ KLİP başlıkları ↔ `(n klip)` beyanı BLOCK → önce PLAN'daki
  satır ile `# 📍 SAHNE` başlıkları eşitlenir, prompt değil · ㉜④ `CONTINUOUS ACTION:` yok
  BLOCK → önceki klibin tablodaki SON durumu IMAGE ve VIDEO'ya şimdiki zamanla yazılır
  [D207] · ㉜⑤ zincir dili BLOCK → "continues the previous clip / exact last frame"
  silinir, START FRAME bu klibin imajını gösterir · ㉜⑥ sahne kilidi FIX → LIGHT/PHYSICS/
  AUDIO-ilk-cümle sahnenin 1. klibinden kopyalanır. Bu rejimde "KÜME 0" bulgusu çıkmaz
  (küme yok); ardışık aynı kurulum yine BLOCK'tur. Kılavuz: `COK_KLIPLI_SAHNE_KILAVUZU.md`.
  Üretimde kare onayı: 2.+ klibin karesi önceki klibin son karesiyle yan yana (§3.3).

## Mazeret çürütme — bu satırlar senin için yazıldı

| İçinden geçen düşünce | Gerçek |
|---|---|
| "Promptlar zaten kılavuza göre yazıldı, betik formalite" | Betik yarım dakika sürer; kartın tarihi, atlanan her denetimin parayla ödendiğini kaydediyor. |
| "Küçük bir revizyondu, yeniden koşmaya gerek yok" | Kapı sürüme değil dosyaya koşulur; dosyanın son hâlini görmeyen koşu koşulmamıştır. |
| "Kullanıcı acele ediyor, doğrudan üretelim" | Kullanıcının acelesi kapıyı kapatmaz; kapı akışın en ucuz adımıdır (sıfır kare). |
| "Çıkış kodu 1 sadece uyarıdır" | 1, gerekçesiz geçilemez: sapma satırı yazılmadan GO verilemez [D74]. |

## Bitiş

Karar (GO/BLOCK) + betik çıkış kodu + yazılan gerekçe satırları kullanıcıya
raporlanır. Bu skill commit atmaz (commit yalnız proje sahibinindir).
