# F5 · Prompt yazım kararı (Fable, 19.10.2026)

> **Kaynak (yalnız bunlar):** `RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md` (sahip planı, birebir) · `FILM.md` §3 (referanslar, ORTAK GÖRÜNÜM, ORTAK HAREKET, SAHNE DÜZENİ, DÜNYA KURALLARI, DEVAMLILIK) · §4 çekim satırı · §5 replik saniyeleri.
> **Varsayılan:** plandan dışarı çıkılmaz. Yeni olay, kişi, nesne, ışık kaynağı, ekran, yazı, renk ya da sıfat yok. Eklenen her cümle planın kendi malzemesidir.
> **Uzunluk (sahibin BLACK_ACCORD tercihi 18.10.2026, "sanki promtlar kısa" → "plan aynen + sonuna ek"):** Görsel hedef 2.000-3.200 kr · Video hedef 1.000-1.500 kr · tavan 4.300.

## Görsel (her çekim)
1. **Referans anahtarları** (M): EKLE'deki her referans için bir cümle — `Reference <No> (<rol>): …` Rol sözlüğü: 1 Kett with poncho · 2 Kett without poncho · 3 Mara · 4 Vorr · 5 Tula · 6 market · 7 roofs · 8 weather crown · 9 weather core.
2. **ORTAK GÖRÜNÜM** (FILM §3, birebir) — plan: "Görsel istemlerinin başına" → anahtarlardan hemen sonra.
3. **Planın Görsel istemi AYNEN** (kelimesi kelimesine; sıra, sıfat, sayı değişmez).
4. **Ek paragraf, planın ardına** — yalnız plan malzemesi:
   - kadrajdaki her öznenin plan R istemindeki kimlik parçaları **birebir** (FILM §3 KİMLİK CÜMLELERİ; kadrajda görünmeyen parça yazılmaz);
   - mekânın plan R06/R07/R08 cümleleri (yalnız o kadrajda görünen yapılar);
   - planın o çekimdeki **Kamera** ve **Devamlılık** satırı İngilizceye çevrilmiş hâli (anlam aynen; ör. C01 "Ponço kapalı; çekirdek sağ elde; hava kuru" → "The poncho is fastened; the core is in the right hand; the air is dry.");
   - plan §8 devamlılık tablosundaki o çekime ait durum (çekirdek nerede, ponço, çark, kamusal yağmur, fincan, çiçek, gemi).
   Planın söylediğini tekrar etmez, onunla çelişmez.

## Video (her çekim)
1. **ORTAK HAREKET** (FILM §3, birebir) — plan: "Video istemlerinin başına". ⚠️ Repliksiz çekimlerde (C03 C09 C11 C13 C15 C16 C17 C18) ve C05'te cümle "The spoken lines below are performance cues; final clean dialogue can be recorded separately." **atılır** (M: konuşma kelimesi; o çekimde "aşağıdaki replik" yok).
2. **Planın video istemi** 2-4 vuruşa bölünür (M): `0-3 s: … 3-7 s: … 7-10 s: …` — 0'da başlar, 10'da biter, boşluksuz, her vuruş ≥2 s. Planın cümleleri aynen ve aynı sırada; yalnız saniye öneki eklenir. Yeni eylem yok. Repliğin düştüğü vuruş FILM §5 saniyesine uyar.
3. **Planın "Dialogue performance" bloğu aynen** (repliği olan çekimlerde): `1. KETT: "…" Voice: …` — replik tırnak içinde birebir (film_dogrula FILM §5 metniyle karşılaştırır).
4. Ek (isteğe bağlı, hedef uzunluk için): son vuruşta planın Devamlılık satırının İngilizcesi (sabit kalanlar).

## Biçim düzeltmeleri (M — yalnız bunlar; NOTLAR KARARLAR'a yazılır)
- C01 Görsel "The first frame already reveals the stolen miniature storm." → "The frame already reveals the stolen miniature storm." (zincir dili)
- C05 Görsel "… above the pale alien flower from the previous shot." → "… above the pale alien flower." (başka çekime atıf)
- C05 Video: Kett kadraj dışı (FILM §5 R04 Kaynak "kadraj dışı") → "Kett speaks the assigned line off-screen, with regret." ve Dialogue bloğu Video'dan çıkar; replik kurguda (plan zaten "off-screen" diyor; makro kadrajda ağız yok).
- Mara kimliği "one narrow vertical speaking mouth" → kare promptunda "one narrow vertical mouth" (Görsel'de konuşma kelimesi hata; planın Türkçesi "ince dikey ağız"). Referans promptunda plan metni kalır.
- film_dogrula başka bir M hatası verirse: en küçük biçim değişikliği + 8 SORU notu.

## Referans promptları (yalnız G01)
- Plan R01-R09 İngilizce istemleri **aynen**, hat adlarıyla (`ref/1.KETT_v1.png` …). R02 "Edit the supplied R01 Kett reference …" metni aynen kalır (R01 = 1.KETT). ORTAK GÖRÜNÜM referans promptlarına **eklenmez** (plan R istemleri kendi arka planını taşır: "warm gray studio background"; sahibe SK).
- Plan sırası: önce 1, sonra 1'in üzerinden düzenlemeyle 2; sonra 3-9.

## Korunacaklar
- Plan §8 devamlılık tablosu · plan §10 üretim sırası (pilot C01 · C21 · C23) · plan §10 C21 yedeği (toka detayı + ponçosuz tepki iki kısa görüntüden, aynı 10 s birim).
- Prompt gövdesine çekim kodu (C01), referans kodu (R01), "Clip n of N", başlık satırı yazılmaz.

## Teslim (grup dosyası)
Dosya başı not · (G01'de) REFERANS PROMPTLARI + KİMLİK CÜMLELERİ · çekim blokları (FLOW · EKLE · not · ### Görsel · ### Video) · FLOW İŞ EMRİ · `## 8 SORU` tablosu + "Görsel kr · Video kr" sütunu.
