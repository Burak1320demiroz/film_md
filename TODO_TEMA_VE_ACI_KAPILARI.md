# ✅ TEMA VE AÇI KAPILARI — UYGULAMA KAYDI

> **Durum (26.08.2026):** A · B · C · D fazları UYGULANDI. Geriye yalnız
> **E fazı (pilot film + geri besleme)** kaldı ve o üretim gerektiriyor.
> Bu dosya E bitince silinir; kalıcı bilgi zaten ilgili kılavuzlara taşındı.
>
> **Teşhis neydi:** Tema ve kamera-açısı kuralları 22.08.2026'da yazıldı
> (`TEMA_MUHENDISLIGI` · `KAMERA_ACISI_PSIKOLOJISI` · `ACI_YAYI_VE_SEKANS`)
> ve dört gün boyunca **hiçbir kapıda ölçülmedi**. Sistem neyi ölçüyorsa onu
> optimize etti: kesmeyi ve fiziği ölçüyordu, temayı ve açıyı değil.
> Kamera monotonluğu bir kural eksikliği değil, lockoff kararının sahneler
> ARASINA sessizce genellenmesiydi.

---

## 📊 ÖNCE / SONRA

```
                                  ÖNCE (26.08 sabahı)        SONRA
tema denetimi (betik)             0                          2 denetim
açı denetimi (betik)              0                          3 denetim
plan öncesi listede tema/açı      0 madde / 12               2 madde / 14
QA_SPEC'te tema + kurulum         0/8 dosyada ikisi birden   8/8
kurulum envanteri (QA rubriği)    hiçbir mercekte            ② DEVAMLILIK ölçüm satırı
ÜÇ KAPI akışta                    okuma listesinde           §6 adım 0,5
tema dağılımı sayımı              yok                        sayac.sh 🎭 bloğu
```

**Kapının ilk taraması (107 dosya, yeni denetimler):**

```
61  ⛔ TEMA satırı yok                    ← kapı açılmadan önceki durumun ölçüsü
45  ·  kurulum sayısı üst bandın üstünde  (gözlem — yatay filmlerin örüntüsü)
43  ⚠️ açı TİPİ < 3                       ← ASIL BULGU
22  ⚠️ açı hiç yazılmamış (§6 sözlüğü yok)
16  ⚠️ tema < 3 sahne indeksi
14  ⛔/⚠️ ardışık iki sahne aynı kurulum
 8  ⚠️ kurulum çeşitliliği bandın altında
```

⭐ **En öğretici sonuç iki sayının AYRIŞMASI:** dikey shorts az kurulum +
az açı tipi üretiyor; yatay filmler ÇOK kurulum ama yine az açı tipi
(THE ROSE COAT: 13 sahne · 13 kurulum · **2 açı tipi**). Yani depo ölçek
ve mesafe çeşitlendiriyor, AÇI çeşitlendirmiyor. Tek sayıyla bakılsa bu
görünmezdi.

---

## ✅ A — TASARIM KARARI DARALTILDI (klip içi ↔ sahneler arası)

- [x] `02_RISK_KARTLARI.md` KART 8 → "⛔ KAPSAM — BU KARAR KLİP İÇİDİR"
      bloğu + risk toplamı satırına kapsam uyarısı
- [x] `03_PLAN_ONCESI_KONTROL_LISTESI.md` D maddesi → kapsam cümlesi
- [x] `01_DERS_ETKINLIK_RAPORU.md` §5 → kapsam bloğu + **iki sayı
      ayrıştırıldı**: `3→8` ardışık sıçrama, `2→8` tablo min→max
      (ikisi de doğru, aynı şey değil — artık hangisi olduğu yazılı)
- [x] Risk paydası düzeltildi: 12 soru listeleniyordu, payda gövdede
      `/9` özette `/8` yazıyordu → `/12` + kalibrasyon uyarısı
      (5+ eşiği 9 soruluyken ölçülmüştü, korundu)

⛔ **Lockoff GERİ ALINMADI.** Klip içi lockoff (AGENTS §8'in üç kararından
biri) aynen duruyor. Değişen tek şey: sahneler ARASI kurulum değişimi
karardan muaf ve zorunlu — sahneler zaten ayrı kliplerde üretiliyor,
teknik riski sıfır (Slow Stone dersi).

## ✅ B — BETİĞE DÖRT DENETİM (`prompt_kontrol.py`)

- [x] **⑩ Kurulum çeşitliliği** — imza: lens + yükseklik + mesafe + ölçek
      + açı tipi. Ardışık ikili aynıysa BLOCK (zengin imza) / FIX (ince
      imza) · kurulum sayısı §4 bandının altındaysa FIX
- [x] **⑪ Açı sözlüğü** — KAMERA_ACISI §2'nin sekizlisi, desenler §6
      reçete sözcüklerinden. 6+ sahnede <3 tip → FIX
- [x] **⑫ Abartı eşiği** — dutch ≥35° BLOCK · kamera 45°+ yukarı pitch
      BLOCK · 45-60° aşağı pitch FIX
- [x] **⑬ Tema kapısı** — TEMA satırı yoksa BLOCK (dosyada + klasör
      komşularında arar) · <3 sahne indeksi varsa FIX
- [x] **Kalibrasyon: 107 dosya · 5 yanlış-pozitif sınıfı bulundu ve kapatıldı**

```
① "dish tilted at 70 degrees"  → çanak anten eğimi kamera eğimi sanıldı
② "angled 60 degrees to frame left" → karakterin gövde yönü kamera pitch'i sanıldı
③ [^.;] penceresi ondalık sayıda kopuyordu ("camera height 0.50 metres,
   pitched up 55 degrees") — GERÇEK bulgu kayboluyordu
④ "locked off at 12 metres" imzadan düşüyordu → 12 m ve 5 m'deki iki sahne
   "aynı kurulum" göründü, iki film haksız BLOCK yedi
⑤ tek çekimin ikiye bölünmüş hâli ("continues the previous clip from its
   exact last frame") monotonluk sanıldı → DEVAM_KLİBİ muafiyeti eklendi
⑥ "TEMAS:" (dokunma) tema beyanı sanıldı → TEMA'dan sonra harf gelemez
```

- [x] `PROMPT_QA_CRITIQUE_PROMPT.md` → yeni kategori 6 "AÇI VURUŞLA
      EŞLEŞİYOR MU" (betiğin ölçtüğü SAYININ anlam yarısı)

## ✅ C — KAPILAR

- [x] **C.1** `03_PLAN_ONCESI` → **B3 tema indeksi** + **B4 açı yayı**
      maddeleri · özet bloğu · KAYNAK tablosu · 12→14 (atıflar güncellendi:
      AGENTS §1 + kart A, KILAVUZ_REHBERI §6 adım 2.5)
      ⚠️ Film dosyalarındaki "12 madde" imzalarına DOKUNULMADI — onlar
      tarihsel kayıt, o filmler 12 maddeyle denetlendi
- [x] **C.2** QA_SPEC şablonu (D117 eki) → THEME + THEME SCENES +
      SETUP SEQUENCE + ANGLE ARC zorunlu; alanın yeri blok harfiyle değil
      MERCEKLE tarif ediliyor (harfler dosyadan dosyaya kayıyordu)
      → **8 SPEC dosyasının 8'i tamamlandı** (3'üne tema, 5'ine kurulum)
- [x] **C.3** `2_DEVAMLILIK` → STEP 1a sahne envanterine "Camera setup"
      sütunu + künyeye **SETUP INVENTORY ölçüm satırı** (skor değil ölçüm)
      + lockoff koruması gövdeye yazıldı
      ⚠️ Kategori 13'e YAZILMADI: o Çehov'un tüfeği (nesne kurulumu),
      kamera kurulumu değil. 1_KARE'ye de yazılmadı — kendi kapsam testi
      film-boyu bulguyu yapısal olarak dışlıyor
- [x] **C.4** `KILAVUZ_REHBERI` §6 → **adım 0,5 KONSEPT KAPISI** (ONERME §4
      ÜÇ KAPI artık numaralı adım; okuma listesi kapı değildir)
- [x] **C.5** `AGENTS.md` kart A → tema satırı + sahne-kurulum dizisi adresleri
- [x] Kart G defteri: `CALISTIRMA_KAYITLARI.md` → rubrik yaması + kardeş
      tarama kaydı (ders YAZILMADI — AGENTS §8: kapı kurma, kural ekleme değil)

## ✅ D — TEMA ÇEŞİTLİLİĞİ

- [x] **§3c TAKAS KALIBI MORATORYUMU** — yazılı temaların **beşi** aynı
      kalıbın varyasyonu çıktı ("X için Y feda edilir"). Kural: arka arkaya
      en çok 2 film; üçüncüsü §3'ten kullanılmamış tema seçer
- [x] **§3b DEPODA DOĞMUŞ ETİKETLER** — TANIKLIK ve **ZEMİN** (ikincisi
      teşhiste yoktu) tabloya ⏸️ ADAY olarak kaydedildi.
      ⛔ Pazar/kuşak sütunları BOŞ bırakıldı: o tablo depoda bulunmayan bir
      araştırma raporundan geliyor, tahminle doldurmak tablonun tamamını
      tahmin seviyesine indirirdi. Tam satır olmanın yolu kart Y'dir
- [x] **D.3** `sayac.sh` → 🎭 TEMA DAĞILIMI bloğu (elle tablo yok, kural ①)

---

## ⬜ E — PİLOT + GERİ BESLEME (tek kalan faz · üretim gerektirir)

- [ ] **E.1** Sonraki dikey filmi şu üçlüyle yaz:
      · `ACI_YAYI §8.1` şablonu (A-B-C-B-D-A: tepe → alt açı → ECU vizör →
        alt açı → dutch 15° → tepe loop) — **depoda hiç denenmedi**
      · §3 tablosundan hiç kullanılmamış tema (Yalnızlık · Zaman · Kimlik ·
        İnsan-makine · İlk temas) + §5 matris satırı plana işlenmiş
      · yeni betik denetimlerinden ve 14 maddeden geçmiş
- [ ] **E.2** Üret ve dört mercekten geçir — SPEC hazır olduğu için **mod D**
      (depoda mod D sayısı hâlâ 0; AGENTS §6 "ÖLÇÜM DURMUŞ" açığını küçültür)
- [ ] **E.3** Kıyas — ⚠️ kural ⑥: <1,5 puan fark GÜRÜLTÜDÜR
- [ ] **E.4** Sonuca göre belge revizyonu; ancak TEKRARLARSA ders (kart Y sırası)

### ⚠️ E fazına girmeden bilinmesi gerekenler

```
· THE NEAR PASS henüz ÜRETİLMEDİ ve 6/6 sahnesi ALT AÇI (1 tip).
  Pilot bu film olacaksa açı yayı önce düzeltilmeli — SPEC'ine
  🚨 AÇIK MADDE olarak yazıldı.
· THE OPEN SEAM'in doruğu (S4, dikişin açıldığı sahne) açısız yazılmış;
  ACI_YAYI §9 doruğa en yüksek kontrast sıçramasını şart koşuyor.
· ⏸️ THE HELD HEAT (4 açı tipi, depodaki en yüksekti) ve THE LAST SPAN
  26.08.2026'da zombi türüyle birlikte kaldırıldı — yay şablonu olarak
  artık kullanılamaz. Kalan en yüksek çeşitlilik uzay hattından
  ölçülmeli; pilot filmin hedefi ≥3 açı tipidir.
```

---

## 🔎 DOĞRULAMA (bu kayıt kapanmadan koşulur)

```bash
bash kilavuzlar_ve_sistem_dosyalari/sayac.sh          # 🎭 bloğu basıyor mu
python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
        dikey_shorts_filmler/THE_BRIGHT_TETHER/       # açı TİPİ 2 → FIX
git status                                            # commit'i SAHİBİ atar [AGENTS §5]
```

> ⚠️ 4 dosya hâlâ başlık standardı dışında (BREATHING_STORM · DEEP_PRESSURE ·
> ETERNAL_ENGINE · PULSE) — bu çalışmadan önce de öyleydi, AGENTS §6'da kayıtlı.
