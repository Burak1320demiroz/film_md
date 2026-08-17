# 📚 HIGGSFIELD KILAVUZLARI — İNDEKS

> **Son güncelleme:** 03 Ağustos 2026
> **Bölüm kapısı:** `../README.md`
> **Film tarafı:** `../../kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md`

Buradaki her dosya **tek konu** anlatır ve **kaynağını gösterir.** Kaynağı
olmayan cümle kılavuza girmez — tahmin, doc'un yerini tutmaz.

---

## 📦 DURUM — 4 dosya yazıldı, hiçbiri doğrulanmadı

**Kaynak** = hangi belgeden çıkarıldı · **Doğrulama** = fiilen denendi mi.

> ⚠️ Yazılan dördünün kaynağı **aynı belge**: kullanıcının hazırladığı
> araştırma raporu (03.08.2026, sohbete yapıştırıldı). Resmi doküman değil,
> ikinci el derleme. **Hiçbiri üretimde doğrulanmadı** — tek kare üretilmedi.
> Resmi doc geldiğinde çelişen her satır doc'a göre düzeltilir.

| # | Dosya | Ne anlatır | Kaynak | Doğrulama |
|:--:|---|---|:--:|:--:|
| 01 | `01_KURULUM_VE_BAGLANTI.md` | CLI kurulumu, `auth login`, MCP vs CLI seçimi, skills yükleme | ⏳ | ❌ |
| 02 | **`02_MODEL_KARTLARI.md`** | Model × bu deponun formatları · yerli ses · göreli maliyet · **iki kaynak çelişkisi** | 📄 rapor | ❌ |
| 03 | `03_KOMUT_REFERANSI.md` | CLI komutları + parametreler, çıktı nereye iner | ⏳ | ❌ |
| 04 | `04_SKILLS_KATALOGU.md` | `higgsfield-ai/skills` içinden bize yarayanlar (UGC/faceless/website hattı bizim işimiz değil — ayıklanacak) | ⏳ | ❌ |
| 05 | **`05_PROMPT_KURALLARI.md`** | Üç katman ayrımı · MCSLA ↔ V2 iskeleti · **uzunluk çelişkisi** | 📄 rapor | ❌ |
| 06 | `06_MALIYET_VE_LIMITLER.md` | Kredi/plan, kuyruk süresi, eşzamanlı iş, deneme başına maliyet | ⏳ | ❌ |
| 07 | **`07_URETIM_AKISI.md`** | Tek değişken kuralı · ucuz taslak · seed · 5-8. saniye kontrolü | 📄 rapor | ❌ |
| 08 | `08_BILINEN_TUZAKLAR.md` | Red sebepleri, bozulan çıktı desenleri, tekrarlanan hatalar | ⏳ | ❌ |
| 09 | **`09_KARAKTER_TUTARLILIGI.md`** | Soul ID · eğitim verisi kuralları · **bizim üç sorunumuz** | 📄 rapor | ❌ |

> 09 planlı listede yoktu. Eklendi çünkü öncelik listesinin 3. maddesi
> (karakter tutarlılığı) depodaki **en düşük ölçülen kategoridir** —
> 7 MANTIK raporunun 7'sinde Kostüm-Prop 4/10'un altında.

### 📌 Rapordan alınmayanlar — bilinçli ayıklama

```
UGC / konuşan avatar / dudak senkronizasyonu   → çoğu filmimiz sessiz,
                                                  Risk Kartı 7 kaçınmayı söylüyor
Ürün reklamı · packshot · üç perdelik ticari    → bu depo film yapıyor
Sıvı cam logo · 2D anime · hareketli grafik     → tür dışı
Draw-to-Video ürün yerleştirme                  → e-ticaret hattı
Motion Control (dans / dövüş aktarımı)          → tek karakter, sakin tempo
```
Rapor bu alanlarda geniş; **bu depo için değersiz.** Alınmadı ki kılavuz
şişmesin ve okuyan yanlış yere bakmasın.

> Liste sabit değil. Doc bir konuyu ikiye bölecek kadar büyükse dosya bölünür;
> iki konu tek sayfada anlaşılıyorsa birleşir. **Dosya sayısını korumak için
> içerik uydurulmaz.**

---

## ✍️ HER KILAVUZUN ZORUNLU ÜST BLOĞU

Yeni dosya açarken bu blokla başla:

```markdown
# BAŞLIK

> **Kaynak:** <doc adı / URL / "sohbete yapıştırılan tanıtım metni">
> **Alındığı tarih:** GG.AA.YYYY
> **Doğrulama:** ❌ denenmedi | ⚠️ kısmen | ✅ üretimde doğrulandı
> **Kapsam:** bu dosyanın CEVAPLAMADIĞI şey de burada yazar.
```

**Neden:** bu depoda doğrulanmamış künye üç QA çalıştırmasını bozdu
(`QA_PROMPTLARI/00_README.md` · SPEC kapısı). Aynı hatayı araç katmanında
tekrarlamamak için kaynak ve doğrulama durumu her sayfanın başında durur.

---

## 🔗 FİLM TARAFINA BAĞLANTI NOKTALARI

Bu bölüm çalışmaya başladığında **film tarafında** şunlar güncellenir:

```
□ KILAVUZ_REHBERI.md §7 BİLİNEN TUZAKLAR   → Higgsfield red/bozulma desenleri
□ LESSONS_LEARNED.md                        → motor kaynaklı yeni ders çıkarsa
□ AGENTS.md görev kartı B (film üretildi)   → "hangi model" satırına Higgsfield
□ AI_AJAN_YETENEKLERI.md + skills-lock.json → skills yüklendiğinde
```

Ters yön yasak: film kuralları bu klasöre **kopyalanmaz**, işaret edilir.

---

## 🎯 ÖNCELİK SIRASI — doc geldiğinde neye önce bakılır

```
1. SÜRE + EN-BOY LİMİTİ      → yapıyı belirler, her şeyden önce
2. 9:16 DESTEĞİ              → dikey shorts hattı buna bağlı
3. KARAKTER TUTARLILIĞI      → 2 dk üstü film bunsuz çekilmiyor
4. SES / DİYALOG             → diyaloglu filmlerin akışı değişir
5. MALİYET                   → kaç deneme göze alınabilir
6. gerisi
```

İlk üçü cevaplanmadan model kartı yazılmaz; yarım kart, kart olmayışından
daha zararlıdır.
