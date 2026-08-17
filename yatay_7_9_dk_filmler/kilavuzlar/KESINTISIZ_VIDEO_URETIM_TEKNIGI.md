# Kesintisiz Video Üretim Tekniği (Start/End Frame Mantığı)

7-9 dakikalık, oturaklı ve uzun planlı filmler üretirken sahnelerin birbiri ardına kesintisiz (devamlılık hatası olmadan) akması büyük önem taşır. Bu bağlamda, video üretiminde sıradan bir metinden-videoya (text-to-video) mantığı yerine, **başlangıç ve bitiş kareleri (Start/End Frame)** belirleyerek ilerlediğimiz matematiksel bir model kullanıyoruz.

## 1. Temel Formül: x. İmaj - (x+1). İmaj = x. Video
Bu teknik, üretilecek her 8 saniyelik video için başlangıç ve bitiş noktalarını bizim belirlediğimiz, yapay zekanın sadece aradaki animasyonu/hareketi doldurduğu bir sistemdir.

*   **1. Video (0-8 saniye):** 
    *   **Start Frame:** 1. İmaj (Videonun başı)
    *   **End Frame:** 2. İmaj (Videonun sonu)
*   **2. Video (8-16 saniye):** 
    *   **Start Frame:** 2. İmaj (Önceki videonun bitiş karesi, bu videonun başlangıcı olur)
    *   **End Frame:** 3. İmaj 
*   **3. Video (16-24 saniye):**
    *   **Start Frame:** 3. İmaj
    *   **End Frame:** 4. İmaj

Bu zincirleme mantık sayesinde videolar arası geçişlerde karakterin duruşu, mekanın yapısı ve ışıklandırma %100 tutarlı kalır.

## 2. Zamanlama ve Uzun Planlar (8 Saniye Kuralı)
Her bir video blok (üretim) **8 saniye** uzunluğunda olacaktır. Bu da 7-9 dakikalık film kılavuzundaki "yavaş tempo ve uzun planlar" (pacing) kuralını doğrudan destekler. İzleyici bir sahneyi, karakterin hareketini kesintisiz olarak uzun süre izleyebilir.

## 3. Sahne Devamlılığı ve Takip
Karakter bir andan diğerine alakasız bir mekana ışınlanmaz. Zincirleme imaj mantığı sayesinde olaylar birbiri ardına organik şekilde gelişir.
*   **Örnek Akış (Uzay Gemisinden İniş):**
    *   *1. İmaj:* Karakter geminin kapısında duruyor.
    *   *2. İmaj:* Karakter merdivenlerin ortasına inmiş, rüzgar esiyor.
    *   **(1. Video: Kapıdan merdiven ortasına kadar iniş)**
    *   *3. İmaj:* Karakter ayağını yabancı gezegenin toprağına basmış, yüzünde şaşkınlık var.
    *   **(2. Video: Merdivenlerden toprağa inme ve yakın çekim şaşkınlık)**
    
Karakter ne yapıyorsa kamera o akışı organik olarak takip eder, anlamsız zıplamalar (jump cut) engellenir.

## 4. Prompt Mantığı (Image = Video)
Bu teknik uygulanırken Görsel (Image) üretmek için kullanılan prompt ile Video üretmek için kullanılan prompt **aynı mantığa** sahiptir. Ancak video promptunda sadece kameranın iki görsel arasında (örn: 1. imajdan 2. imaja) nasıl hareket etmesi gerektiği (örn: yavaşça yaklaşma, karakteri takip etme vb.) belirtilir.

Bu sistem sayesinde filmin başından sonuna kadar görsel dil bozulmadan, ağır ve sinematik bir akış elde edilir.
