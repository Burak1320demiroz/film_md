# 🎞️ THE_GRAVITY_ANCHOR — SAHNE SIRALAMASI

> **Bu dosya sıranın TÜRETİLDİĞİ ve DENETLENDİĞİ yerdir.** Sonuç `THE_GRAVITY_ANCHOR_PLAN.md`
> §SAHNE HARİTASI'na taşınır — orası sonucu taşır, burası hesabı.
> ⛔ Bu dosyada `## ... SAHNE <n>` biçiminde başlık yoktur (kapı betiği o
> deseni sahne sanar); sahneler TABLO satırıdır.
>
> Girdi: `02_KONSEPT_VE_RISK.md` (sahne sayısı · B5 · tema · risk).

---

## 1. 🥁 VURUŞ TABLOSU — sahne dağıtılmadan ÖNCE (`SENARYO_VE_VIRAL_KAMERA` §2)

| # | vuruş | % | hangi sahnede | boşsa gerekçe |
|---|---|---|---|---|
| ⬜ |  |  |  |  |

```
HOOK TİPİ:        ⬜        (HOOK_VE_ILK_SAHNE §8)
S0 SORUSU:        ⬜
S1 İKİNCİ BİLGİ:  ⬜
İLK 2 SN SESİ:    ⬜
AÇILIŞ↔KAPANIŞ:   ⬜ [KAFİYE / LOOP / TWIST+tohum] — değişen TEK değişken: ⬜
```

## 2. 🗺️ SIRALAMA — X sahne, sırayla

> Her satır dört bütçeyi birden taşır:
> `KARAKTER_VE_DUYGU §6` (göz · tepki planı · el · yürüyüş · eşya) ·
> `KURGU_RITMI §2` örüntü kırıcı (**ardışık iki sahne aynı ölçek + palet +
> ses dokusunda OLAMAZ**) · `ACI_YAYI §3` güvenli bant · B5 bağı.

| S | başlık | olay (tek cümle) | vuruş | B5 satırı | kurulum | lens · ölçek · açı tipi | palet | ses | ⭐VİRAL |
|---|---|---|---|---|:--:|---|---|---|:--:|
| S0 | ⬜ |  |  |  | A |  |  |  |  |
| S1 | ⬜ |  |  |  |  |  |  |  |  |

## 3. 📐 ARDIŞIK ÇİFT DENETİMİ — mekanik, göz kararı değil

> `ACI_YAYI §3` güvenli bant: ardışık her çift **≥1 ölçek kademesi VE ≥45° azimut**.
> ⛔ Bölüm SINIRI da ardışık bir çifttir (son sahne ↔ ilk sahne).

| çift | ölçek kademesi | azimut farkı | bant içi | şok mu · gerekçe |
|---|:--:|:--:|:--:|---|
| S0→S1 |  |  |  |  |

```
ARDIŞIK ÇİFT:     ⬜ / ⬜ bant içi
BİLİNÇLİ ŞOK:     ⬜   (her biri gerekçeli — doruğun bırakıldığı yer gibi)
AÇI TİPİ SAYISI:  ⬜ ≥3   (KAMERA_ACISI §2 — üç kurulumun üçü de alttan
                  bakıyorsa çeşitlilik yok, yalnız mesafe değişiyor)
KURULUM SAYISI:   ⬜      (ACI_YAYI §4 bandı; üstündeyse tek satır gerekçe [D74])
```

## 4. ⭐ KURULUM İSKELETİ — PLAN'a taşınacak satır

```
İSKELET: ⬜ ⬜ ⬜ ⬜ ⬜ ...        (sahne sayısı kadar HARF)

KÜME:   ⬜ ≥2      ardışık 2-3 klip aynı kurulumda, tek vuruş sürerken
DÖNÜŞ:  ⬜ ≥%40    dönüş = kaynağından ≤3 sahne sonra gelen tekrar
        (12+ sahnede aranır; 6-11 sahne ve dikey shorts MUAF)
```

⛔ Aynı harfin kamera metni **BİREBİR kopyalanır** ve işaret satırını taşır —
model iskeleti görmez, metni görür [`ACI_YAYI` §7 ⑥]:
```
dönüş → "— the same position, height and lens as Scene N."
küme  → "continues the previous clip from its exact last frame — the same
         position, height and lens as Scene N."
```
⛔ Bu satır PLAN'a yazılmazsa `prompt_kontrol` ⑩④ kapısı **hiç koşmaz.**

## 5. 🎙️ REPLİK YERLEŞİMİ (yalnız replikli filmde)

| # | S | saniye (formülle) | konuşan | REGISTER | kanal | İŞLEV (B5 satırı) |
|---|---|---|---|---|---|---|
| ⬜ |  |  | H/M |  |  |  |

```
⛔ SANİYE HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
⛔ İŞLEV sütunu boş replik yazılmadan SİLİNİR (§2a.1 silme testi)
⛔ Ekranda okunan konuşan ağız: bedenleştirme yalnız DORUKTA [§1a.1] —
   iki riski birden açar: lip-sync + AI damgası
```

## 6. 🔢 METİNSİZ SAYAÇ — ekran/kadran/gösterge kullanmadan

```
KANAL 1: ⬜ → ⬜ → ⬜   (monotonik mi: ⬜)
KANAL 2: ⬜
⛔ Cihaz ekranı / sayaç / yazı ile sayılan şey bu depoda arıza üretiyor.
```

## 7. ⛔ ÜRETİM SIRASI — dramatik sıra DEĞİLDİR [D168]

```
ÜRETİM SIRASI: ⬜ → DORUK S⬜ → merkezî seçim S⬜ → kapanış imajı S⬜ → S0 → kalanı
(referans paketi yazıldıysa ilk halka odur)
```

Üretim her an durabilir (red · kota · motor · gün). Baştan üretirsen elde hep
KURULUM kalır ve kurulum kendini savunamaz. **THE SINKING STAKE tam böyle
durdu: 25 sahnenin 14'ü üretildi, eksik 11'i ARDIŞIK ve filmin SONUYDU.**

```
⛔ İPTAL KAPISI: S⬜ — ⬜ tutmuyorsa film ÜRETİLMEZ.
```

---

## ✅ KAPI

```
□ X sahnenin X'i tabloda, olay sütunu dolu
□ ardışık çiftlerin hepsi denetlendi, şoklar gerekçeli
□ kurulum iskeleti yazıldı, KÜME ve DÖNÜŞ hesaplandı
□ üretim sırası + iptal kapısı yazıldı
→ dördü de ✅ ise 04_UYARI_NOTLARI.md yazılabilir
```
