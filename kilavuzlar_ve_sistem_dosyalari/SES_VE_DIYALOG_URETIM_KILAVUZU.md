# 🎙️ SES VE DİYALOG ÜRETİM KILAVUZU — Yazım Tarafı

> **Neden var (21.08.2026):** Ses için ÖLÇÜM tarafı tamdı (SES_QA rubriği ·
> 07_SES_KALITE_TABLOSU · AGENTS kart E3) ama YAZIM tarafını öğreten tek
> adres yoktu — kurallar VEO kılavuzu §3-4, YANASMA §2, D35/D40/D82/D83'e
> dağılmıştı. İlk SES_QA koşusunun bulgusu tam bu boşluğu gösterdi
> (Cold Burn: ATIF 9 tuttu · YATAK 3 tutmadı). Bu dosya PLANA ve PROMPTA
> ne yazılacağını söyler; miks/kurgu tarafı `KURGU_VE_TESLIM_KILAVUZU.md`
> §4'te, müzik `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19'da.
>
> **Ne zaman okunur:** filmde replik VEYA ses tasarımı varsa, plan
> aşamasında — sahne haritası yazılırken.

---

# 1. 🎭 REGISTER HARİTASI — her replik yazılmadan önce

Bu seri **bilinçli sentetik diegetik ses** kullanır: suit AI, gemi
bilgisayarı, telsiz otomatiği, kayıt. SES_QA her repliği şu sözlükle
ölçer; yazım tarafı da AYNI sözlükle plana yazar:

```
HUMAN     film bunu bir İNSAN konuşması olarak sunar
          → sentetik okunuş = HATA (düz prosodi, yanlış vurgu, nefessizlik)
MACHINE   film bunu SENTETİK ses olarak sunar (suit AI · bilgisayar ·
          otomatik uyarı · kayıt)
          → düz sentetik okunuş = TASARIMIN KENDİSİ, hata değil
```

```
□ PLANA YAZILIR: her replik için tek satır —
    | S# | saniye | konuşan | REGISTER | kanal (telsiz/AI/oda) |
□ UNCLEAR yazım tarafında YASAKTIR: planda register'ı belirsiz replik
  kalamaz. (UNCLEAR yalnız QA merceğinin sözlüğünde vardır — film
  register'ı EKRANDA okutamadıysa bulgu yazar.)
□ Register EKRANDAN okunur olmalı: filtre (telsiz bandı), kaynak
  (hoparlör/kask), ya da repliğin kendi içeriği onu söylemeli.
```

**SAYI KURALI [D82 · YANASMA §2.2]:** sayı söyleyen her replik (mesafe,
hız, yüzde, geri sayım) **gövdesiz AI'dadır** — insana devredilemez.
Cold Burn'ün ölçülmüş en pahalı ses hatası tam buydu: EKO silindi,
sayılar ekrandaki ağızlara geçti, lip-sync çöktü. Görsel kanal ile sesli
kanal aynı sayıyı söyler ve birbirini doğrular (D78 çift kanal kuralı).

---

# 2. 📏 REPLİK BÜTÇESİ VE YERLEŞİM [D35]

```
□ Her replik 5 SANİYENİN ALTINDA; 8-10 saniyelik klibi dolduran tirat yok
□ TEK KONUŞMACI, sıkı sıra (turn lock) — asla eş zamanlı konuşma;
  aynı sahnede iki replik varsa sırası SANİYEYLE yazılır
□ Kasklı hatlarda: kasksız sahnede tek kelime KONUŞULMAZ; kasksızlık
  yalnız basınçlı hacimde ve tek sahnede açılır [YANASMA §2.2 ⑤]
□ Diyalog yalnız MEDIUM veya daha yakın kadrajda; geniş çekimde replik
  yazma (lip-sync çöker) [VEO kılavuzu §4]
```

**Güvenlik sıralaması — üç yerleşim, güvenliden riskliye:**

```
① KADRAJDA İNSAN YOKKEN duyulan telsiz/AI repliği  ✅ EN GÜVENLİ
   (dış çekim + radyo kanalı — Cold Burn S19 emsali; Black Cradle'ın
    iptal/kapı/fısıltı repliklerinin dördü de böyle)
② SIRTTAN / ARKADAN çekimde kapalı kask telsizi     ✅ GÜVENLİ
   (konuşmalı kokpit ARKADAN, lombozdaki gözlemci SIRTTAN — ağız
    hiçbir karede okunmaz)
③ EKRANDA KONUŞAN AĞIZ                              ⚠️ EN RİSKLİ
   (yalnız medium+ kadraj, <5 s replik, tam lip-sync bloğuyla; başka
    çare yoksa)
```

---

# 3. ✍️ VEO SENTAKSI [VEO kılavuzu §3-4]

Veo varsayılan olarak SESSİZ üretmeye eğilimlidir; konuşma özel sentaks ister:

```
KALIP:   [karakter tanımı] + [eylem/duygu] + says: + "tam metin"
  ✅ ...looks at the display and says in a flat, tired voice,
     "Pressure is holding."
  ❌ "A woman says hello"  (model kararsız kalır — sessiz ya da
     anlamsız dudak hareketi)

□ TON ZARFLA verilir: in a weary voice · softly whispers · urgently —
  zarf, prosodi ve yüz mikro-ifadelerini birlikte yönlendirir
□ Miks talimatı prompta: "Clean dialogue only" + ortam yatağı ayrı cümle
□ Replikli sahnede yoğun ses olayı (fırtına, patlama, müzik) aynı anda
  İSTENMEZ — diyalog netliği ölür
```

---

# 4. 📢 PROMPT'A GİREN SES BLOĞU

Her sahnenin video promptunda bir **AUDIO cümlesi** olur — sessiz sahnede
bile ("no music" / yatak tarifi). Hazır kalıplar (YANASMA §2.4'ten,
kopyala-uyarla):

```
YAKLAŞMA (insanlı iç):  Low cabin hum; slow breathing on the radio
  channel; the synthetic line at Xs, heard only — never shown as text.
  No music.
DIŞ + TELSİZ REPLİĞİ:   No exterior sound — hard vacuum. Only the radio
  channel: faint carrier hiss and the single spoken line at Xs, heard
  only. No music.
TEMAS/DORUK:            Hard vacuum — no exterior sound at all, even at
  contact. Only the radio channel's faint carrier hiss and two held
  human breaths that release, slowly, just after contact. No voice,
  no music.
KENET + ONAY:           ...faint carrier hiss, two slow breaths, and the
  whispered line at Xs, heard only — never shown as text.
```

**Diyaloglu her prompta ayrıca** (REHBER §5'in diyalog eki — birebir):

```
The spoken line is heard only — never shown as text. No subtitles, no
captions, no transcript. [Konuşan ekrandaysa:] her lip movements match
the words exactly, mouth closed before and after. [Ekran dışıysa:] the
voice is off-screen only — no mouth in frame, no invented on-screen
speaker.
```

---

# 5. 🛏️ ORTAM YATAĞI PLANI [D83]

"Müziksiz sahne" SESSİZ sahne değildir — mutlak dijital sıfır, teslim
edilemez hata sınıfıdır.

```
□ PLANA YATAK ENVANTERİ yazılır: filmin sürekli ses zemini nedir?
  (oda tonu · suit fanı · nefes · taşıyıcı hışırtısı · yapı gıcırtısı)
□ Ortam kartının "Ses" satırı (REHBER §3) AUDIO cümlesine yansır:
  vakum = dış ses SIFIR, yalnız gövdeden iletilen · ince atm. = boğuk,
  yüksek frekanssız · kalın/CO2 = güçlü, tınılar ALÇALIR
□ Sessizlik bir karar ise GEREKÇESİ ve sınırı yazılır: en güçlü biçim
  diegetik susma (Black Cradle: müzik "Motorlar kapalı" repliğiyle,
  motorlarla BİRLİKTE kesilir)
□ Yatağın kurguda tek parça serileceği: KURGU_VE_TESLIM_KILAVUZU.md §4
```

---

# 6. 🎼 MÜZİK SINIRI — bu dosyanın bittiği yer

```
□ Her filmde EN AZ BİR müziksiz sahne [GOOGLE_FLOW §10]
□ Müzik doruktan ÖNCE susar, doruk sahnesinin başında değil —
  sessizliğin fark edilmesi 1-2 saniye ister [YANASMA §2.1]
□ Tempo, sahne uzunluğuna hizalanır; sub-bass'a 90-160 Hz eşlikçi
  [GOOGLE_FLOW §14-15] — ayrıntı ve künye orada (§17)
```

---

# 7. ✅ PLAN KONTROLÜ — bu kılavuzun 7 maddesi

```
□ 1  Replik tablosu var mı? (S# · saniye · konuşan · REGISTER · kanal)
□ 2  Sayı söyleyen her replik MACHINE register'da mı? [D82]
□ 3  Her replik <5 s ve tek konuşmacı mı? [D35]
□ 4  Ekranda ağız gerektiren replik sayısı kaç — ①/② yerleşimine
     inebilir mi?
□ 5  Kasksız sahnede replik var mı? (varsa SİL ya da sahneyi basınçlı
     hacme taşı)
□ 6  Yatak envanteri yazıldı mı — "müziksiz" hiçbir sahne SESSİZ değil? [D83]
□ 7  Her AUDIO cümlesi "heard only — never shown as text" taşıyor mu? [D40]
```

---

# 8. 📚 KAYNAKLAR

```
VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md  §3 sentaks · §4 lip-sync · §7 katman
YANASMA_VE_KENETLENME_KILAVUZU.md                 §2 ses/dramaturji (üç filmde donan kararlar)
GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md              §10 sessizlik · §14-17 tempo/frekans/künye
KURGU_VE_TESLIM_KILAVUZU.md §4                    miks/kurgu tarafı
QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md ölçüm merceği (register sözlüğünün kaynağı)
DERSLER                                            D35 · D40 · D78 · D82 · D83 tam metin
```
