# 🎬 THE_SOLAR_MIRROR — SAHNE SIRALAMASI VE KURULUM İSKELETİ

> **Kaynak:** `KILAVUZ_REHBERI.md` §2.2 · `ACI_YAYI_VE_SEKANS_KILAVUZU.md` §3-§4 · `HOOK_VE_ILK_SAHNE_KILAVUZU.md`

---

## 1. VURUŞ HARİTASI VE YÜZDE BANTLARI

| Sahne | Timecode | Vuruş | Drama Yüzdesi | İşlev / Dramatik Eylem |
|---|---|---|---|---|
| **S00** | 00:00–00:18 | Temas ve Anomali | %0–%15 | Opening Hook: Ayna yüzeyinde 30s gelecek kehanetinin görülmesi. |
| **S01** | 00:18–00:40 | Kendi Kendini Gerçekleştiren Kehanet | %15–%30 | Pürmüz testi: Engelleme çabası kehaneti gerçekleştirir. |
| **S02** | 00:40–00:55 | Tehdidin Keşfi | %30–%45 | Aynada mekiğin LOX tankına kilitlenmiş odak ışını görülür. |
| **S03** | 00:55–01:01 | Geri Sayım Başlar `[T-30]` | %45–%50 | Real-time 30s başlar. Uplink arızası. Mara mekiğe fırlar. |
| **S04** | 01:01–01:13 | Gövdeye Ulaşım + İki Bedel `[T-18]` | %50–%60 | Mekiğe iniş. Tether çözülür (Bedel 1). O₂ aktarım kararı. |
| **S05** | 01:13–01:22 | Seçim Anı ve Ateşleme `[T-09]` | %60–%75 | **DORUK:** O₂ aktarımı (Bedel 2), RCS kolu çekilir, ayna dalgalanır. |
| **S06** | 01:22–01:25 | Işının Gelişi `[T-00]` | %75–%80 | Güneş ışını boşluktan geçer; mekik sağlamdır, truss buharlaşır. |
| **S07** | 01:25–01:40 | Kopmak ve Savrulma | %80–%88 | Mekik uzaklaşır. Mara vakumda serbest savrulmaya başlar. |
| **S08** | 01:40–01:55 | Aynaya Son Bakış | %88–%92 | Mara savrulurken S04 segmentinin yanından geçer. |
| **S09** | 01:55–02:10 | Aynadaki Gelecek | %92–%95 | Aynada 30s sonraki kendi cansız, durağan bedenini görür. |
| **S10** | 02:10–02:25 | Son 27 Saniye | %95–%98 | Kask içi CU: O₂ göstergesi sıfırlanır, fan durur, nefes kesilir. |
| **S11** | 02:25–02:40 | Final | %98–%100 | Kapanış Kafiyesi: Devasa yörünge boşluğunda süzülen astronot. |

---

## 2. KURULUM İSKELETİ VECİBESİ

### KURULUM TANIMLARI
- **Setup A:** Extreme Wide Shot (EWS) — 35mm wide lens / Güneş Aynası dizisi (1 km) + uzakta mekik + Mara silueti.
- **Setup B:** Medium Close-Up (MCU) — Eye level / Mara kask vizörü ve HELIOSTAT S04 segment yüzeyi.
- **Setup C:** Medium Shot (MS) — Low angle / Mara + arkadaki ayna yansıması.
- **Setup D:** Medium Tracking Shot (MTS) — Mara'nın mekiğe doğru mikrogravite intikali / savrulması.
- **Setup E:** Close-Up (CU) — Mekiğin dış RCS pnömatik valf paneli ve Mara'nın elleri.
- **Setup F:** Wide Shot (WS) — High angle / Mekiğin yanındaki termal parlamanın geniş kadrajı.
- **Setup G:** Close-Up Yansıma (CU-Reflect) — Aynanın pürüzsüz yüzeyinde 30s gelecekteki durağan astronot bedeni.

### KURULUM DİZİSİ SATIRI
```
A B B C D E E F D C G B A
```

### KONTROL METRİKLERİ
- **Benzersiz Setup Sayısı:** 7 adet (A, B, C, D, E, F, G) ≥ 3 ✅
- **KÜME SAYISI (ardışık aynı setup ≥2):** 5 küme (A×1, B×2, C×1, D×1, E×2, F×1, D×1, C×1, G×1, B×1, A×1 → B×2, E×2) ≥ 2 ✅
- **DÖNÜŞ ORANI:** 6 tekrarlanan dönüş / 13 toplam geçiş ≈ %46.1 ≥ %40 ✅
- **KAFİYE UYUMU:** S00 (Setup A) ↔ S11 (Setup A) birebir kadraj kafiyesi ✅

---

## 3. REPLİK VE SES YERLEŞİMİ

| Sahne | Telsiz / Ses Tipi | Replik Metni (AUDIO Register) | İşlev |
|---|---|---|---|
| **S00** | Mürettebat Telsiz | *"EVA-1, crew transfer complete. We're waiting on you, Mara."* | Karakter tanıtımı ve durum bildirimi. |
| **S03** | Telsiz Paraziti | *"[Static interference] ...uplink signal lost... repeat..."* | Uplink arızası ve panik tetikleyici. |
| **S07** | Mürettebat Telsiz | *"EVA-1, RCS fired — what happened? Mara, respond!"* | Kurtarma başarısının teyidi, yalnızlığın derinleşmesi. |
| **S10–S11** | Kask İçi Nefes | [Konuşma yok — Suit fanı yavaşlar ve durur, derin nefes] | Ölümün ve bedelin kask içi kişisel kabulü. |

---

## 4. ÜRETİM SIRASI (DRAMATİK SIRA DEĞİLDİR [D168])

Üretim aksaması durumunda elde kalan sahnelerin filmi temsil edebilmesi için risk ve doruk öncelikli üretim sırası:

1. **Adım 1:** `<FILM>_REFERANS_PAKETI.md` (Mara EVA Suit, Vizör, Ayna Yüzeyi, Shuttle)
2. **Adım 2:** **S05** (Doruk — RCS aktarımı ve O₂ divert seçim ani)
3. **Adım 3:** **S06** (Işının gelişi ve mekikten sapması — novum mekanizma doğrulaması)
4. **Adım 4:** **S11** (Final kapanış kafiyesi — görsel son)
5. **Adım 5:** **S00** (Açılış hook kadrajı — görsel başlangıç)
6. **Adım 6:** **S01, S02, S03, S04** (Birinci perde ve tırmanma)
7. **Adım 7:** **S07, S08, S09, S10** (İkinci perde ve çözülme)
