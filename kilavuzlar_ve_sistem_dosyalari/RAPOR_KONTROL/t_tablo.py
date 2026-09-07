#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T TABLOSU YAZICI — rapor_kontrol.py'nin çıktı ucu.  [④ hamlesi · 04.09.2026]

NEDEN VAR: betik "▶ TABLOYA GİRECEK SAYI" satırını zaten HESAPLIYORDU ve
elle kopyalanmasını bekliyordu. 04.09.2026 ölçümü: ham raporu olup T
tablosunda satırı olmayan film 16 — kayıp ders değil, KIRTASİYE.
"Ölçüldü" ile "tabloya girdi" iki ayrı durum olmaktan çıkar.

⛔ GEÇERSİZ / TEKRAR kararlı rapor satır YAZMAZ (tablo okuma kuralları).
⛔ mod V satırı Ⓥ ile yazılır; SPEC varken mod V koşulduysa ⛔ da eklenir
   [D94 · D129] — skor tabloya girer, tamlık matrisine girmez.
"""
import re
from datetime import date

# mercek → (tablo dosyası, kolon → rapordaki İngilizce kategori adları)
T = {
 "① KARE": ("T1_KARE_KALITE.md", {
   "Karakter": ["Character"], "Fizik": ["Scale & Physics"], "Kamera": ["Camera", "Camera & Cuts"],
   "Işık": ["Lighting"], "Çevre": ["Environment"], "Canlı": ["Creatures"],
   "Parçacık": ["Particles & Materials"], "Diyalog-Ses": ["Dialogue & Audio", "Audio"],
   "Kare Çapası": ["Frame Anchor Fidelity"], "Hareket": ["Motion Quality"],
   "9:16": ["Vertical Format (9:16)"], "Güvenli Alan": ["Safe Zone"],
   "Kanca": ["Hook Timing"], "Negatif": ["Negative Violations"]}),
 "② DEVAMLILIK": ("T2_DEVAMLILIK_KALITE.md", {
   "Kimlik": ["Identity — Face, Hair & Build", "Facial Identity", "Hair, Build & Proportions"],
   "Kostüm": ["Costume Identity", "State, Costume & Props"],
   "Yıpranma": ["Wear, Damage & Injury"],
   "Ekipman": ["Equipment & Carried Objects", "Equipment State"],
   "Çapraz Kesme": ["Cross-Cut Action"], "Fizik": ["Physical Consistency"],
   "Sayaç": ["Counter Logic"], "Coğrafya": ["Spatial Geography"],
   "Zaman-Işık": ["Time & Light Logic"], "Dünya Propu": ["World State & Props"],
   "Nedensellik": ["Causality & Knowledge"],
   "Nicelik+Sayı": ["Quantity Consistency", "Quantity & Character Count", "Count & Separation"],
   "Kurulum": ["Setup & Abandonment"]}),
 "③ SES": ("T3_SES_KALITE.md", {
   "Atıf": ["Speaker Attribution"], "Sentetik": ["Synthetic Voice Tells"],
   "Ses Kimliği": ["Voice Identity Continuity"], "Aktarım": ["Delivery vs Performance"],
   "Sıra Alma": ["Turn-Taking & Acoustics"], "Ambiyans": ["Ambience Continuity"],
   "SFX Senk": ["SFX Causality & Sync"], "Miks": ["Mix Hierarchy & Levels"],
   "Müzik": ["Music & Silence"]}),
 "④ HİKAYE": ("T4_HIKAYE_KALITE.md", {
   "Kanca": ["Hook"], "Önerme": ["Premise & Clarity"], "Yapı": ["Structure & Pacing"],
   "Karakter": ["Character"], "Tema": ["Theme"], "Diyalog": ["Dialogue"],
   "Duygu Yayı": ["Emotional Arc"], "Final": ["Ending"], "Özgünlük": ["Originality"],
   "Tutundurma": ["Retention Risk"]}),
 "⑤ ARKA PLAN": ("T5_ARKA_PLAN_KALITE.md", {
   "Figür Büt.": ["Background Figure Integrity"], "Figür Dav.": ["Background Figure Behaviour"],
   "Kalabalık": ["Crowd Count & Density"], "Ufuk": ["Horizon & Topology"],
   "Derinlik": ["Depth, Parallax & Scale"], "Arka Set": ["Background Set & Props"],
   "Odak": ["Focus Honesty"], "Gökyüzü": ["Sky & Atmospherics"],
   "Kenarlar": ["Frame Edges & Emergent Artifacts", "Frame Edges & Artifacts"]}),
 "⑥ FİZİK": ("T6_FIZIK_KALITE.md", {
   "Yerçekimi": ["Gravity & Free Fall"], "Balistik": ["Ballistics & Trajectories"],
   "Momentum": ["Impact & Momentum"], "Malzeme": ["Material Behaviour"],
   "Parçacık": ["Particles & Atmosphere"], "Ölçek": ["Scale & Measurement"],
   "Hız/Zaman": ["Rates & Timing"], "Işık/Gölge": ["Light & Shadow Physics"],
   "Biyomek.": ["Human Biomechanics"]}),
 "⑦ AKSİYON": ("T7_AKSIYON_KALITE.md", {
   "Beat anat.": ["Beat Anatomy"], "Coğrafya": ["Spatial Geography Under Motion"],
   "Tehdit": ["Threat Vector & Approach"], "Temas": ["Contact Legibility"],
   "Sonuç": ["Consequence Visibility"], "Kamera": ["Camera's Contract with the Action"],
   "Niyet": ["Agency & Intent"], "Bahis": ["The Stakes Object"],
   "Tempo": ["Physical Tempo & Escalation"]}),
 "⑧ EFOR": ("T8_EFOR_KALITE.md", {
   "Zorlanma": ["Strain During the Work"], "Nefes": ["Breath & Recovery"],
   "Yorgunluk": ["Fatigue Accumulation"], "Yük": ["Load in the Body"],
   "Yaralanma": ["Injury Persistence & Cost"], "Kavrama": ["Grip & the Price of Holding On"],
   "Ekipman": ["Equipment Burden"], "Acı": ["Pain, Restraint and Proportion"],
   "Eğri": ["Recovery Curve Honesty"]}),
}


def _sayi(x):
    s = f"{x:.1f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def _film_adi(r, film_dir=None):
    """Ad YALNIZ film klasöründen gelir.

    ⛔ Rapordaki FILM alanı KULLANILMAZ: operatörün yüklediği master'ın dosya
    adını taşıyor ve yanlış (04.09.2026 ölçümü: THE_PAYLOAD raporu 'The Last
    Custodian.mp4', THE_LAST_SPAN raporu 'The Last Stand' diyordu; okunamayanlar
    tek bir '?' satırında birbirinin üstüne yazıldı). Klasör adı tek kimliktir.
    """
    if not film_dir:
        return None
    ad = film_dir.name.replace("_", " ").strip()
    # ASCII başlıklandırma — tr yerelinde 'i' → 'ı' düşmesin
    return " ".join(w[:1].upper() + w[1:].lower() for w in ad.split() if w) or None


def satir_kur(r, film_dir=None, spec_var=False, tarih=None):
    """rapor_kontrol sonucundan tek T satırı üret → (tablo dosyası, film adı, satır) | None"""
    if r["mercek"] not in T:
        return None
    if r["karar"] in ("GEÇERSİZ", "TEKRAR"):
        return None
    dosya, harita = T[r["mercek"]]
    bulunan = {}
    for row in r.get("rows", []):
        for kol, adlar in harita.items():
            if row["ad"] in adlar and kol not in bulunan:
                bulunan[kol] = _sayi(row["deger"]) if row["tip"] == "sayi" else "—"

    ad = _film_adi(r, film_dir)
    if not ad:
        return None          # klasör verilmediyse satır YAZILMAZ (kimliksiz satır yazmaktansa yazma)
    isaret = ""
    if r.get("mod") != "D":
        isaret += " Ⓥ"
        if spec_var:
            isaret += " ⛔"
    if r["karar"] == "ŞARTLI":
        isaret += " ⚠️"
    t = tarih or date.today().strftime("%d.%m")

    h = [f"**{ad}**{isaret}"]
    if dosya.startswith(("T5", "T6", "T7", "T8")):
        h.append(t)
    if dosya.startswith(("T6", "T7", "T8")):
        h.append(r.get("mod") or "V")
    if dosya.startswith("T1"):
        h += [(r.get("format") or "⬜").upper(), str(r.get("sahne") or "⬜")]
    if dosya.startswith("T4"):
        h += [(r.get("format") or "⬜").upper(), "⬜"]
    if dosya.startswith("T3"):
        h.append(r.get("audio_state") or "⬜")

    h += [bulunan.get(k, "⬜") for k in harita]
    top = (f'{r["son_ort"]:.1f}'.replace(".", ",")) if r.get("son_ort") is not None else "—"
    h.append(f"**{top}**")
    if dosya.startswith(("T5", "T7", "T8")):
        h.append("⬜")
    if dosya.startswith("T6"):
        h += ["⬜", "⬜"]
    return dosya, ad, "| " + " | ".join(h) + " |"


def tabloya_yaz(kok, dosya, film_adi, satir):
    """Tabloya ekle; aynı filmin satırı varsa YERİNE yaz (üst üste birikmez)."""
    p = kok / dosya
    if not p.exists():
        return f"⚠️  tablo yok: {p}"
    L = p.read_text(encoding="utf-8").split("\n")
    ayrac = next((i for i, s in enumerate(L)
                  if s.startswith("|---") or re.match(r"^\|[\s:|-]+\|$", s)), None)
    if ayrac is None:
        return f"⚠️  başlık ayracı bulunamadı: {dosya}"
    son = ayrac
    for i in range(ayrac + 1, len(L)):
        if L[i].startswith("|"):
            son = i
        elif L[i].strip() and not L[i].startswith("|"):
            break
    anahtar = f"**{film_adi}**"
    for i in range(ayrac + 1, son + 1):
        if anahtar in L[i]:
            L[i] = satir
            p.write_text("\n".join(L), encoding="utf-8")
            return f"↻ {dosya}: '{film_adi}' satırı GÜNCELLENDİ"
    L.insert(son + 1, satir)
    p.write_text("\n".join(L), encoding="utf-8")
    return f"+ {dosya}: '{film_adi}' satırı EKLENDİ"
