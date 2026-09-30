# 🎭 T10 — OYUNCULUK KALİTE TABLOSU (plan sadakati)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/10_OYUNCULUK_QA_CRITIQUE_PROMPT.md`
> **Açılış:** 06.09.2026 — plan sadakati mercekleri sınıfı [D184]
>
> **Ne ölçer:** "Karakterin istediği, seçtiği, hissettiği BEDENDE okunuyor mu — ekrandan, plansız." Tek yöntemi: her sahne için izleyicinin söyleyeceği CÜMLE önce ekrandan yazılır; üç çapa vuruşta (SEÇİM · BEDEL · FİNAL) öncesi/sonrası karesi dondurulur ve bedendeki fark bir cümleyle yazılır. Cevap "hiçbir şey" ise vuruş ekrana ulaşmamıştır. ⭐ ④ sayfadaki hikayeyi, ⑦ olayı, ⑧ bedeli okur; kişiyi kimse okumuyordu.
>
> ```
> KATEGORİLER  1 yüz+göz (kask kapalıysa N/A) · 2 niyet olarak eller · 3 duruş ve kararın ağırlığı · 4 bakış yönü · 5 tempo ve durgunluk · 6 merkezî seçim bedende · 7 bedel ve sonrası · 8 final vuruşun okunurluğu · 9 orantı
> TETİKLEYİCİ  replik 0 olan her film · SPEC'te CENTRAL CHOICE satırı
> MAKİNE ÇIKTISI  GAZE STRING — sahne başına O/A/D/U/-; THE CHOICE ON THE BODY üç önce/sonra satırı
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
①-④ dört zorunlu merceğin yanına zorunlu olarak eklenmemiştir.
KOŞUL TETİKLİ plan sadakati taramasıdır: SPEC'te ilgili kayıt varsa koşulur.
Skoru T1-T4 ile TOPLANMAZ ve KARŞILAŞTIRILMAZ — ayrı eksen, ayrı tablo.
⛔ SPEC'siz (mod V) koşusu tanım gereği BOŞTUR: bu mercek planı ekrana karşı
okur; plan yoksa okuyacak şey yoktur. Mod V satırı bu tabloya YAZILMAZ.
```

## ⛔ SATIR YAZMADAN ÖNCE

```
1. ⑪ ölçüm kapısı koşuldu mu (master ölçüldü mü) · TESLİM SINIFI HAM ZİNCİR değil mi
2. rapor_kontrol.py GEÇERSİZ / TEKRAR dönmedi mi
   python3 ../RAPOR_KONTROL/rapor_kontrol.py <rapor> --film <FILM>
3. ARITHMETIC GATE tutuyor mu (n · Σ · Σ/n rapordan yeniden hesaplandı mı)
4. Rapor MODE D mi [D129] — bu tabloda mod V satırı yoktur
Biri bile hayırsa satır YAZILMAZ; ham rapor 02_HAM_RAPORLAR/'da durur.
```

---

## 📊 TABLO

| Film | Tarih | Mod | Yüz|Eller|Duruş|Bakış|Tempo|Seçim|Bedel|Final|Orantı | Toplam | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **The Counted Turn** | 09.09.2026 | D | 3.0 | 3.0 | 3.0 | 7.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.0 | 3.4 | 🔴 **THE CHOICE IS INVISIBLE** — niyet bedende okunmuyor; S20 merkezî kararında tereddüt/vücut ağırlığı sıçraması yok, manken postürü [D184] |
| **The Hard Dock** ⚠️ | 12.09.2026 | D | 7.5 | 7.0 | 7.5 | 8.0 | 7.0 | 7.5 | 7.5 | 7.5 | 7.5 | **7,4** | S13-S16 exterior sequence disrupts character emotional build-up |
| **The Inward Fall** ⚠️ | 30.09 | D | 8 | 7 | 8 | 8 | 7 | 8 | 6 | 8 | 8 | **7,6** | ⬜ |
| **The Signal Keepers** ⚠️ | 30.09 | D | 9 | 9 | 9 | 9 | 10 | 9 | 9 | 10 | 9 | **9,2** | THE BODY TELLS IT · K19 seçim anında tereddüt ve öne ağırlık aktarımı [D202] · K20 hard mute ses kesintisinde bedensel bedel · K24 açık ellerle final tezatı |
| **The Static Veil** ⚠️ | 30.09 | D | — | — | — | — | — | — | — | — | — | **—** | THE BODY TELLS IT · 12 sahne el/duruş niyetli, 8 kategori kusursuz (10/10 → — uyarınca D186) [D184] |


⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].
