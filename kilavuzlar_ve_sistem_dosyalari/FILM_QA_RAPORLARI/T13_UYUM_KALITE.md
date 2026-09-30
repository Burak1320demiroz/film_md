# 🧩 T13 — UYUM KALİTE TABLOSU (sahne ↔ prompt · üretim sadakati)

> **Kaynak rubrik:** `../QA_PROMPTLARI/_KAYNAK/13_UYUM_QA_CRITIQUE_PROMPT.md`
> **Makine yarısı:** `.claude/skills/qa-isle/scripts/sahne_kapisi.sh`
> **Açılış:** 11.09.2026 — üretim sadakati mercekleri sınıfının ilk merceği
>
> **Ne ölçer:** "Ekrandaki sahne, o sahne için GÖNDERİLEN promptun dediği şey mi —
> ve değilse, kilit promptta var mıydı?" Depodaki diğer on iki mercek filmi plana
> ya da kendisine karşı okur; bu mercek **prompta** karşı okur. Kusurun sahibini
> söyleyen tek mercektir.
>
> ```
> KATEGORİLER  C1 sayılabilir nesne · C2 kurulum · C3 zaman çizelgesi ·
>              C4 negatif ihlali · C5 devamlılık taşıyıcısı · C6 okunurluk ·
>              C7 istenmeyen ekleme (replik dahil) · C8 ses ve metin
> TETİKLEYİCİ  film ÜRETİLDİ + sahne promptları yapıştırılabiliyor [16.09.2026]
>              (üretim defteri + sahne_kapisi.sh: VARSA okunur, ön koşul DEĞİL)
> MAKİNE ÇIKTISI  CONFORMANCE STRING — sahne başına bir hane (K·T·P·Y·-);
>              rapor_kontrol.py uzunluğu sahne sayısıyla karşılaştırır
> BİRİNCİL SAYI  LOCKS HELD / LOCKS CHECKED — model BÖLMEZ [16.09.2026]: türetilmiş
>              skoru bu satırı yazan ajan hesaplar (HELD ÷ CHECKED × 10).
>              LOCKS CHECKED = raporun KİLİT DEFTERİ satır sayısı; eşit değilse
>              sayım uydurulmuştur ve satır YAZILMAZ.
> ```

---

## ⛔ BU TABLO /4 PAYDASINA GİRMEZ

```
①-④ dört zorunlu merceğin yanına zorunlu olarak eklenmemiştir.
ÜRETİM TETİKLİ bir sadakat taramasıdır: film üretildiyse ve defteri varsa koşulur.
Skoru T1-T4 ile TOPLANMAZ ve KARŞILAŞTIRILMAZ — ayrı eksen, ayrı tablo.
⛔ Bu merceğin mod V'si YOKTUR: prompt metni girdinin kendisidir. Promptsuz koşu
   "eksik koşu" değil, KOŞU DEĞİLDİR; satırı bu tabloya yazılmaz.
```

## ⛔ SATIR YAZMADAN ÖNCE

```
1. sahne_kapisi.sh koşulduysa TESLİM UYUŞMAZLIĞI (sahne ≠ prompt) çıkmadı mı
   (koşulmadıysa raporun `SCENE COUNT SOURCE: counted from cuts` satırı şarttır)
2. üretim defterinin TESLİM SATIRI dolu mu — dolu değilse satır yazılır ama
   Not sütununa `makine tablosuz` yazılır ve as-built/seed sütunu iddia taşımaz
3. rapor_kontrol.py GEÇERSİZ / TEKRAR dönmedi mi
   python3 ../RAPOR_KONTROL/rapor_kontrol.py <rapor> --film <FILM>
4. CONFORMANCE STRING uzunluğu sahne sayısına eşit mi
5. Her bulgu alıntı taşıyor mu (🅐 promptun cümlesi · 🅑 "instead" satırı)
Biri bile hayırsa satır YAZILMAZ; ham rapor 02_HAM_RAPORLAR/'da durur.
```

---

## 🔁 RETROSPEKTİF — bu mercek hiç koşmadan arşiv okundu [18.09.2026]

```
Bu tablo BOŞ ve öyle kalıyor: ⑬ UYUM hiçbir filmde koşulmadı.
Ama ⑬'ün sorduğu soru (🅐 model sapması mı 🅑 prompt boşluğu mu) 31 filmin
357 ham raporuna GERİYE DÖNÜK soruldu:

    10_PROMPT_QA_ANALIZI/     688 tekil bulgu · 🅐 293 · 🅑 343 · 🅒 29 · 🅓 23

⛔ O klasörün satırları BU TABLOYA GİRMEZ — ⑬ bir KOŞUDUR ve koşmadı.
   Oradaki hüküm videoya değil, rapor metnine + prompt metnine dayanır;
   CONFORMANCE STRING yok, LOCKS HELD/CHECKED yok, kare kanıtı yok.
   İki ayrı eksen, iki ayrı dosya.
⭐ Ama oradaki 🅑 sınıfları ⑬'ün ASIL çıktısı olan DERS SİPARİŞİ ile aynı şeydir
   ve sonraki filmin yazım standardına oradan geçer.
```

---

## 📊 TABLO

| Film | Tarih | Sahne | K | T | P | Y | 🅐 | 🅑 | Kilit tutan/ölçülen | Türetilmiş skor | Ders siparişi | Not |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| *(henüz koşu yok)* | | | | | | | | | | | | |

```
K = kabul · T = kurguda düzeltilir · P = sonraki filme kilit · Y = yeniden üret
🅐 = model sapması (kilit promptta vardı) · 🅑 = prompt boşluğu (kilit hiç yoktu)
Ders siparişi = LESSON ORDERS satır sayısı — bu merceğin ASIL çıktısı budur
```

⛔ Sayılar bu tabloya ELLE yazılmaz — rapordan gelir ve `rapor_kontrol.py`
GO döndükten sonra kopyalanır [kural ① · D161].

---

## ⭐ BU TABLONUN OKUNMA BİÇİMİ — skor değil, 🅐/🅑 oranı

```
🅑 çoksa   → kusur PROMPTTADIR. Sonraki filmin yazım standardı değişir;
             ölçülen filmin promptuna DOKUNULMAZ (tarihtir).
🅐 çoksa   → kusur MOTORDADIR. Aynı promptla yeniden üretim mantıklıdır;
             ısrarla tekrarlıyorsa tasarım değişir, prompt cilası değil.
İkisi de az → kilitler tutuyor. O filmin prompt yazımı KOPYALANACAK örnektir;
             hangi cümlelerin tuttuğu Not sütununa yazılır.
```

⛔ **DERS KANALI ZORUNLU:** her 🅑 satırı ya bir derse bağlanır ya da gerekçesiyle
ARŞİV'e düşer [DERS_YAZIM_KONTRATI §2]. Dersi doğan satırın KAPI cümlesi
**"ölçen mercek: ⑬"** ibaresini taşır — D187'nin arızası (kilidi ölçen mercek yok)
bu sınıfta tekrar etmesin diye.
