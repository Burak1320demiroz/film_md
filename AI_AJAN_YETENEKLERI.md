# 🧠 AI Ajan Yetenekleri (Skills) Kullanım Kılavuzu

Bu proje, terminal üzerinde çalışan yapay zeka ajanlarına (Claude Code vb.) ekstra yetenekler kazandırmak için çeşitli **Skills (Yetenekler)** kullanmaktadır. Yetenekler `.agents/skills/` klasöründe tutulur ve ajana yeni süper güçler verir.

Bu dosyada, projeye kurulu olan yetenekler, ne işe yaradıkları ve nasıl kullanılacakları özetlenmiştir.

---

## 1. 🎬 ai-video-generation

**Ne İşe Yarar?**
Yapay zeka video modellerini (Veo, Runway, Luma vb.) doğrudan ajan üzerinden kullanmanızı veya bu modellerle ilgili en iyi prompt/API mimarilerini oluşturmanızı sağlar. Ajana 40'tan fazla video modelinin kullanım bilgisini ve komut satırı arayüzü gücünü verir.

**Nasıl Kullanılır?**
Claude Code terminalindeyken şu şekilde komut verebilirsiniz:
* *"ai-video-generation yeteneğini kullanarak şu yazdığım sahne için Veo modelinin kabul edeceği optimum promptu oluştur."*

---

## 2. 🌐 agent-browser

**Ne İşe Yarar?**
Ajana **internette sörf yapma** yeteneği kazandırır. Ajan sizin için Chrome/Chromium tarayıcısını arka planda açar, web sitelerine girer, araştırma yapar ve bilimsel/teknik verileri okur.

**Nasıl Kullanılır?**
Özellikle bilimkurgu filmi yazarken araştırma yapmak için idealdir:
* *"agent-browser'ı kullanarak Cooke Anamorphic lenslerin düşük ışık (low light) özelliklerini araştır ve bana özetle."*
* *"agent-browser ile piezzo-elektrik rezonansın gerçek dünya kurallarını internetten bul, buna göre World Bible'ı güncelleyelim."*

---

## 3. 🕵️‍♂️ grill-me

**Ne İşe Yarar?**
Fikirlerinizi acımasızca **test eden ve sorgulayan** (stress-test) bir yetenektir. Yapay zekanın sadece "evet, harika fikir" demesi yerine, konseptinizdeki mantık hatalarını bulmasını ve size ardı ardına detaylı sorular sorarak senaryoyu/tasarımı mükemmelleştirmesini sağlar.

**Nasıl Kullanılır?**
Yeni bir film fikri bulduğunuzda doğrudan şu komutu verin:
* *"/grill-me kullanarak zombilerin olduğu bu yeni kısa film fikrimi sorgula. Mantık hatalarını bulana kadar bana soru sor."*

---

## 4. 📝 to-spec (Eski adıyla to-prd)

**Ne İşe Yarar?**
Sohbet geçmişinizi, beyin fırtınalarınızı ve projedeki diğer belgelerin kurallarını (YAPI_GRAFI.md, LESSONS_LEARNED.md) okuyarak **kusursuz bir spesifikasyon (film tasarım/script) dokümanı** oluşturur. Size hiçbir ekstra soru sormadan, bildiği her şeyi yapısal bir formata döker.

**Nasıl Kullanılır?**
Uzun bir beyin fırtınası seansının ardından fikri kalıcı bir belgeye dönüştürmek için:
* *"/to-spec yeteneğini kullan ve konuştuğumuz bu Mars filmi fikrini THE_GLASS_WORLD_SHORTS.md şablonuna benzer şekilde, tüm Bible'ları içerecek profesyonel bir taslağa (Spec) dönüştür."*

---

## 5. 🎨 ui-ux-pro-max

**Ne İşe Yarar?**
Arayüz tasarımı için aranabilir bir bilgi tabanı: stiller, renk paletleri, font
eşleşmeleri, UX kuralları, ikon ve animasyon önerileri, ve 22 teknoloji yığını
için uygulama rehberleri. Web panelinin (`web/`) tasarım kararlarını
"beğendim/beğenmedim" yerine ölçülebilir kurallara bağlar.

**Nasıl Kullanılır?**
Doğrudan sorgu ile (betik skill'in kendi klasöründedir):
```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<sorgu>" --domain ux
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<sorgu>" --stack nuxtjs
```
* *"ui-ux-pro-max ile panelin sahne listesi için doğru yoğunluk ölçeğini bul."*

⚠️ Bu skill skills.sh'te **Gen Agent Trust Hub = High Risk** işaretli
(Socket ve Snyk temiz). Bilerek kuruldu; okuma/öneri için kullanılıyor.

---

## 6. 🤝 handoff

**Ne İşe Yarar?**
Saatlerce süren uzun bir terminal oturumunu kapatmadan önce **devir teslim dokümanı** hazırlar. Konuşulan tüm önemli kararları, şu anki durumu ve bir sonraki adımda ne yapılacağını özetleyerek bilgisayarınıza kaydeder. Böylece yarın yeni bir Claude Code oturumu açtığınızda ajan kaldığınız yeri hemen anlar.

**Nasıl Kullanılır?**
Oturumu kapatmadan hemen önce:
* *"/handoff komutunu çalıştır. Yarınki oturumda Sahne 3'ün revizyonlarına odaklanacağımızı da nota ekle."*
