"""Ortak yardimcilar: anahtar yukleme ve gorsel uretme.

Not: google-genai 1.47'de dokumandaki `client.interactions.create` yuzeyi YOK.
Calisan yol `models.generate_content` + `response_modalities=['IMAGE']`.
Bu surumde cozunurluk parametresi de yok — yalniz `aspect_ratio` var.
Ileride interactions yuzeyi gelirse gorsel_uret() onu tercih eder.
"""

import os
import pathlib
import struct

KLASOR = pathlib.Path(__file__).parent


def anahtari_yukle() -> None:
    """GEMINI_API_KEY'i ortamdan ya da .env dosyasindan yukler."""
    if os.environ.get("GEMINI_API_KEY"):
        return
    env = KLASOR / ".env"
    if env.exists():
        for satir in env.read_text().splitlines():
            if satir.startswith("GEMINI_API_KEY="):
                os.environ["GEMINI_API_KEY"] = satir.split("=", 1)[1].strip()
                return
    raise SystemExit("GEMINI_API_KEY yok (ortam değişkeni ya da gemini-api/.env)")


def gorsel_uret(client, model: str, prompt: str, oran: str = "9:16",
                boyut: str = "2K") -> bytes:
    """Tek gorsel uretir, PNG/JPEG baytlarini dondurur."""
    if hasattr(client, "interactions"):  # yeni API yuzeyi (henuz SDK'da yok)
        import base64
        r = client.interactions.create(
            model=model, input=prompt,
            response_format={"type": "image", "aspect_ratio": oran,
                             "image_size": boyut},
        )
        return base64.b64decode(r.output_image.data)

    from google.genai import types
    r = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=oran),
        ),
    )
    for parca in r.candidates[0].content.parts:
        if getattr(parca, "inline_data", None):
            return parca.inline_data.data
    metin = getattr(r, "text", None) or ""
    raise RuntimeError(f"Yanıtta görsel yok. Model metin döndü: {metin[:200]}")


def gorsel_bilgi(veri: bytes) -> str:
    """Gelen baytlar gercekten gorsel mi, kac piksel? 200 donmesi yetmez."""
    if veri[:8] == b"\x89PNG\r\n\x1a\n":
        en, boy = struct.unpack(">II", veri[16:24])
        return f"PNG {en}x{boy}, {len(veri) // 1024} KB"
    if veri[:2] == b"\xff\xd8":
        return f"JPEG, {len(veri) // 1024} KB"
    return f"GÖRSEL DEĞİL ({len(veri)} bayt, baş: {veri[:12]!r})"


def hata_yorumla(e: Exception) -> str:
    """Hata tipini ayirt et — her biri farkli bir karar demek."""
    m = str(e)
    # 429 kontrolu once: kota mesajinin icinde "billing details" gectigi icin
    # faturalama kontrolu one alinirsa yanlis teshis veriyor.
    if "limit: 0" in m:
        return "FREE KOTASI SIFIR -> bu model ücretsiz katmanda kapalı"
    if "429" in m or "RESOURCE_EXHAUSTED" in m:
        return "KOTA DOLU -> bir süre bekle, sonra tekrar dene"
    if "denied access" in m:
        return "PROJE ERİŞİME KAPALI -> anahtarın projesi engelli (403)"
    if "API_KEY_INVALID" in m or "API key not valid" in m:
        return "ANAHTAR GEÇERSİZ -> yeniden oluştur"
    if "404" in m or "NOT_FOUND" in m:
        return "MODEL YOK -> model ID'si yanlış ya da erişilemiyor"
    if "PERMISSION_DENIED" in m or "403" in m:
        return "İZİN YOK"
    return "BİLİNMEYEN HATA"
