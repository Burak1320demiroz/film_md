# 🎭 DEAD_LAST — Sahneleme

> Sahneleme odasının çıktısı (`.claude/skills/sahneleme-odasi/SKILL.md` · faz 3 adım
> "sahneleme"). Yazanlar: sahneleyici (§1, §2, §4, §5) · mekan-haritacisi (§3).
> Zincirli çekimlerin `Zincir · Baş. karesi · Bitiş karesi` sütunları `FILM.md` §4'tedir;
> burada tekrar edilmez. Başlıkları ve sütun sırasını değiştirme (`film_dogrula.py` okur).
>
> **Zincir nedir:** ardışık klipler kesintisiz tek plan gibi akar. Halka n'nin bitiş karesi,
> halka n+1'in başlangıç karesidir.
> - **Yöntem B (varsayılan):** anahtar kareler önceden üretilip onaylanır; her halka Flow'da
>   başlangıç + bitiş karesiyle üretilir.
> - **A:** önceki klibin gerçek son karesi.
> - **A′:** önceki klipte seçilen çıkış noktasındaki kare; halka 3-6 sn'ye kısalabilir.
> - **A+:** çıkarılan kare, referanslarla görsel düzenlemeden geçirilip tazelenir.
>
> **Seçmeli:** zincir yalnız kesintisiz akışın ANLAM taşıdığı yerde kurulur (önerilen film başına
> 2-3 zincir, zincir başına ≤4 halka). Her halka yeni bir bilgi taşır (ARIZA H01).

---

## 1. ZİNCİRLER

| Zincir | Çekimler | Halka | Yöntem | Neden zincir (kesintisizlik ne anlatıyor) |
|:--:|---|:--:|:--:|---|
| Z1 | C02 C03 | 2 | B | <örn. yaklaşmanın kesilmeden sürmesi gerilimi taşıyor> |

## 2. ANAHTAR KARELER

<!-- Yıldız düzeni: her Zk.n, Zk.0 + referanslardan görsel düzenlemeyle üretilir; bir öncekinden DEĞİL.
     Anahtar kare "durağan an"dadır: adım bitmiş, el temastan ayrılmış, kol inmiş — hareket ortası değil. -->
| Kare | Zincir | Poz / konum | Kamera | Işık | Nesne durumu | Kaynak | Dosya (`kare/`) |
|:--:|:--:|---|---|---|---|---|---|
| Z1.0 | Z1 | <karakter nerede, nasıl duruyor> | <objektif · konum · yükseklik> | <yön · renk> | <kapak kapalı …> | ref: 1.KARAKTER | `Z1.0.png` |
| Z1.1 | Z1 | | | | | Z1.0 + ref | `Z1.1.png` |
| Z1.2 | Z1 | | | | | Z1.0 + ref | `Z1.2.png` |

## 3. MEKÂN HARİTASI

```
<kuşbakışı ASCII harita — karakter (K), nesneler, kamera konumları (K1, K2), ekran yönü okları>
```

| Öğe | Konum (m, sol-alt köşeden) | Not |
|---|---|---|
| Kamera (C02-C03) | | |

## 4. DELTA KONTROLÜ — her halka

| Çekim | Zk.n → Zk.n+1 | Tek ana hareket | Mesafe / süre | Kamera hareketi | Giren/çıkan yok | Temas değişmez | Durum değişimi |
|:--:|:--:|---|---|---|:--:|:--:|---|
| C02 | Z1.0 → Z1.1 | | <örn. 1,2 m / 8 s> | <yok / %15 itme> | ✅ | ✅ | <yok / tek ve küçük> |

## 5. ZİNCİR DIŞI ÇEKİMLER

| Çekim | Neden zincir değil |
|:--:|---|
| C01 | <örn. kuruluş planı · kesme bilgi taşıyor> |
