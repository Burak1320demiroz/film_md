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

## 3. Karar

- **GO** → üretime geçilebilir (önce imaj; imaj onaylanınca video).
- **BLOCK** → üretme. 5+ risk çıkıyorsa malzeme azaltmayı öner; bu bandda
  prompt iyileştirmek işe yaramıyor (kartın kendi kaydı).

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
