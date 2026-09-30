# 🚧 EŞLEŞMEYENLER — dürüst borç kaydı

> Kaynak: `prompt_hata_analizi.py --yaz` · elle yazılmaz.
> Bu dosyanın işi ZORLAMAK değil, neyin NEDEN dışarıda kaldığını adıyla yazmak.

## B · PROMPT VAR, IZGARA YOK

`QA_SPEC`'in `GRID:` satırı yok ya da ⬜ ile boş bırakılmış. Zaman damgası
sahneye çevrilemez; ızgara plandan türetilirse ikinci turda girerler.

| film | ham | sahne | sebep |
|---|:--:|:--:|---|
| LOW_POWER | 14 | 25 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_BANDED_DEEP | 4 | 16 | ⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — plan 16 sahne, 1 rapor makarada 10 sahne saydı (16/1-4'ün hiçbiri değil) |
| THE_BLACK_CRADLE | 6 | 25 | ⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — plan 25 sahne, 1 rapor makarada 4 sahne saydı (25/1-4'ün hiçbiri değil) |
| THE_BLIND_RETURN | 4 | 18 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_BLUE_DRIFT | 6 | 25 | ⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — plan 25 sahne, 2 rapor makarada 15 sahne saydı (25/1-4'ün hiçbiri değil) |
| THE_CANOPY_WORLD | 2 | 10 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_COLD_BURN | 6 | 30 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_DAWN_FRONT | 2 | 14 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_DEEP_PRESSURE | 1 | 2 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_HERD | 1 | 12 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_HOLDING_FIELD | 1 | 11 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_INVERSION | 2 | 11 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_KALEIDA_CRASH | 2 | 11 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_LAST_ARCHIVE | 2 | 11 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_LAST_SHIFT | 4 | 14 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_OPEN_CIRCUIT | 12 | 25 | ⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — plan 25 sahne, 10 rapor makarada 22 sahne saydı (25/1-4'ün hiçbiri değil) |
| THE_RING_LIGHT | 4 | 14 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_RING_WALKER | 13 | 11 | ⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — plan 11 sahne, 4 rapor makarada 19 sahne saydı (11/1-4'ün hiçbiri değil) |
| THE_SECOND_SHIP | 9 | 114 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_STARLESS_CIRCLE | 4 | 18 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_STATIC_SHADOW | 13 | 15 | ⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — plan 15 sahne, 9 rapor makarada 12 sahne saydı (15/1-4'ün hiçbiri değil) |
| THE_STONE_SKY | 4 | 14 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_THIRD_DUNE | 5 | 25 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_TIDAL_HUNT | 1 | 11 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| THE_UNBROKEN_CITY | 4 | 16 | QA_SPEC GRID yok · raporlar da süre/sahne taşımıyor |
| YERCEKIMI | 17 | 120 | ⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı] — plan 120 sahne, 2 rapor makarada 14 sahne saydı (120/1-4'ün hiçbiri değil) |

## C · EŞLEŞMEYEN

| film | ham | sebep |
|---|:--:|---|
| THE_FIRST_MORNING | 1 | prompt sahne başlığı yok |
| THE_IRON_SLOPE | 6 | prompt sahne başlığı yok |
| THE_LAST_SPAN | 7 | film klasörü yok |
| THE_SILENT_COUNT | 1 | film klasörü yok |
| THE_THIN_ROOF | 6 | prompt sahne başlığı yok |
| THE_WRONG_SHADOW | 2 | prompt sahne başlığı yok |

```
B toplamı: 26 film · 143 ham rapor
C toplamı: 6 film · 23 ham rapor
```
