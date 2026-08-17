# ⚠️ 04 — KURALLAR VE RİSKLER

> **Kaynak:** Colab resmî FAQ (research.google.com/colaboratory/faq.html),
> BleepingComputer / Unite.AI / Inverse deepfake yasağı haberleri (2022),
> Decrypt + Hacker News + TheLastBen tartışması — Colab yöneticisi Chris Perry'nin
> Gradio/webui açıklaması (2023), Hivenet Colab limit rehberi (2026)
> **Doğrulama:** ❌ denenmedi · FAQ metni doğrudan okunmadı, haber üzerinden aktarıldı
> **Son güncelleme:** 08.08.2026

---

## ⛔ COLAB FAQ'IN YASAKLADIKLARI — aktarıldığı şekliyle

```
· deepfake üretimi ve deepfake modeli EĞİTİMİ
· kripto madenciliği
· hizmet engelleme (DoS) saldırıları
· şifre kırma
· erişim/kaynak sınırlarını aşmak için ÇOKLU HESAP
· uzak masaüstü veya SSH
· uzak vekil sunucuya (proxy) bağlanma
· dosya barındırma, medya yayınlama, Colab'la etkileşimli hesaplamayla
  ilgisi olmayan web servisi sunma
```

> 📌 **Not (09.08.2026):** listede "uzak masaüstü veya SSH" var, ama Google'ın
> **resmî Colab CLI'ında `colab ssh` komutu bulunuyor.** Çelişki değil, sınır
> tanımı: yasak olan **kendi tünelini kurmak**; resmî araçla yapılan iş meşru.
> Aynı mantık MCP/CLI hattını ComfyUI+Gradio tünelinden ayırıyor (→ §UZAKTAN ARAYÜZ).

Yasak kod çalıştıran kullanıcı şu uyarıyı görüyor: *"You may be executing code
that is disallowed, and this may restrict your ability to use Colab in the
future."* — yani **yaptırım hesap seviyesinde.**

### Bizi doğrudan ilgilendiren iki madde

```
🔴 DEEPFAKE
   Gerçek bir insanın yüzüyle LoRA eğitmek bu maddeye girer.
   → KURAL: bu depoda eğitilen her karakter KURGUSAL olacak; veri seti
     kendi ürettiğimiz karelerden çıkacak (03 §KARAKTER HATTI adım 1-2).
     Oyuncu fotoğrafı, ünlü referansı, "şu aktör gibi" veri seti YOK.

🔴 MEDYA YAYINLAMA / WEB SERVİSİ
   Colab'ı render çiftliği + dosya sunucusu gibi kullanmak sınırda.
   → KURAL: çıktı üretildiği gibi indirilir; Colab depolama veya dağıtım
     katmanı olarak kullanılmaz.
```

---

## 🚫 UZAKTAN ARAYÜZ KISITI — ücretsiz katman

2023'te Colab, Stable Diffusion **webUI** kullanımını ücretsiz katmanda
kısıtladı. Colab yöneticisi Chris Perry'nin açıklaması: yasaklanan şey Stable
Diffusion değil, **Gradio ile dışarıya açılan uzak arayüz** — ücretsiz katmanın
bütçesi etkileşimli notebook hesabına ayrılmıştı ("webUI usage got super big").

Bugünkü durum (2026, ikinci el): **ComfyUI ücretsiz T4'te hâlâ koşabiliyor**
ama 5–10 dk yükleme ve boşta kopma ile. Kısıt arayüzü tünelleyen kullanıma
bakıyor, görsel üretiminin kendisine değil.

> ✅ **Bu bizim lehimize.** Colab MCP yolu tam olarak "etkileşimli notebook
> hesabı": tünel yok, Gradio yok, port paylaşımı yok — ajan hücre koşturur.
> Yani MCP hattı ComfyUI+tünel hattından **kural olarak daha güvenli.**
>
> Sonuç: ComfyUI'ye ancak MCP'nin başsız Python yolu yetmezse bakılır,
> ve bakılırsa **ücretli katmanda** bakılır.

---

## ⏱️ TEKNİK RİSKLER

| Risk | Etki | Azaltma |
|---|---|---|
| 90 dk boşta kopma (ücretsiz) | oturum ölür, model yeniden iner | üretim kuyruğunu tek hücrede topla; ücretli katman |
| 12 sa üst sınır (ücretsiz) | uzun kuyruk kesilir | işi 8 s / 10 s kliplere böl (zaten öyle) |
| Yoğun saatte GPU verilmemesi | başlayamama | ücretli katman; sabit üretim saati yok |
| Geçici disk | model ve çıktı kaybı | Drive mount veya her klipten sonra indirme (→ 01 §ÖLÇÜM 3) |
| Belirli çip garantisi yok | L4 beklerken T4 gelir | hücrede GPU adını yazdır, modeli ona göre seç |
| OOM | yarı yolda hata | kuantize sürüm (FP8/GGUF), offload, çözünürlük düşürme |
| Model yükleme süresi | her oturumda 5–10 dk | oturum başına ÇOK klip üret, tek klip için oturum açma |

---

## 📜 LİSANS RİSKİ — ticari kullanım

Filmler YouTube/IG/TikTok'a çıkıyor; **her model ticari kullanıma açık değil.**

```
✅ LTX-2.3          Apache 2.0 — müşteri işi dahil ticari kullanım serbest
✅ Z-Image-Turbo    Apache 2.0 — atıf ve lisans notu korunmak şartıyla
✅ FLUX.2 [klein] 4B  Apache 2.0
⚠️ FLUX.1 [dev]     "Non-Commercial License v1.1.1" — İKİ KATMANLI, aşağıda
❓ Wan 2.2 · HunyuanVideo · Qwen-Image · FLUX.2 [dev]   lisans OKUNMADI
```

### ⚠️ FLUX.1 [dev] — modelin lisansı ile çıktının lisansı AYRI

Lisans metninden (v1.1.1, HF deposundaki `LICENSE.md`):

```
✅ ÇIKTI  "Outputs are not considered Derivatives under this License."
          "You may use Output for any purpose (including for commercial
           purposes), except as expressly prohibited herein."
          → Üretilen kapak/kare YAYINLANABİLİR.

⚠️ MODEL  "Non-Commercial Purpose" = modelin kullanımından "doğrudan veya
           dolaylı ödeme almamak". Gelir getiren faaliyet, son kullanıcıya
           hizmet ve ticari amaçla başka model eğitmek kapsam DIŞI.
          → Kanal gelir getiriyorsa MODELİN kullanımı gri alanda kalır.
```

**Kural:** FLUX.1 [dev] çıktısı yayınlanabilir. Kanal para kazanıyorsa
BFL'in self-serve ticari lisansı (bfl.ai/pricing/licensing) alınır ya da
yayına giren iş Apache 2.0 modellerle (LTX-2.3 · Z-Image · FLUX.2 klein)
üretilir. Bu bir hukuki görüş değil, lisans metninin okunmuş halidir.

> 📌 Tarihçe: lisans v1.1'de (Haziran 2025) "ticari çıktı" cümlesi
> kaldırılmış diye tartışma çıkmıştı; **v1.1.1'de cümle yerinde.**
> Kaynak: HF `black-forest-labs/FLUX.1-dev/LICENSE.md` (okundu 10.08.2026).

> **KURAL:** bir modelden çıkan kare yayına girmeden önce lisansı bu tabloya
> yazılır. `❓` işaretli bir modelin çıktısı yayınlanmaz.

---

## 🔗 İLGİLİ

```
Köprü/kurulum   → 01_BAGLANTI_YOLLARI.md
Katman seçimi   → 02_DONANIM_VE_MALIYET.md
Model eşikleri  → 03_MODEL_ADAYLARI.md
İlk tuzak çıkınca → 07_BILINEN_TUZAKLAR.md (henüz yok, ilk denemeden sonra açılır)
```
