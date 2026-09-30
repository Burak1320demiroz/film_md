#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T TABLOSU YAZICI — rapor_kontrol.py'nin çıktı ucu.  [④ hamlesi · 04.09.2026]

NEDEN VAR: betik "▶ TABLOYA GİRECEK SAYI" satırını zaten HESAPLIYORDU ve
elle kopyalanmasını bekliyordu. 04.09.2026 ölçümü: ham raporu olup T
tablosunda satırı olmayan film 16 — kayıp ders değil, KIRTASİYE.
"Ölçüldü" ile "tabloya girdi" iki ayrı durum olmaktan çıkar.

⛔ GEÇERSİZ / TEKRAR / ✂️ KESİK kararlı rapor satır YAZMAZ (tablo okuma kuralları; KESİK 14.09.2026).
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
   "Ekipman": ["Equipment Burden"], "Acı": ["Pain, Restraint and Proportion", "Pain, Restraint & Proportion"],
   "Eğri": ["Recovery Curve Honesty"]}),
 # 06.09.2026 · plan sadakati mercekleri [D184]
 "⑨ KADRAJ": ("T9_KADRAJ_KALITE.md", {
   "Kurulum": ["Setup Fidelity"], "Lockoff": ["Lockoff Integrity"],
   "Kafiye": ["Rhyme Pair"], "Dönüş": ["Return Consistency"],
   "Dikiş": ["Cluster Seams"], "Açı yayı": ["Angle Arc & Deliberate Shocks"],
   "Geometri": ["Screen Geometry"]}),
 "⑩ OYUNCULUK": ("T10_OYUNCULUK_KALITE.md", {
   "Yüz": ["Face", "Face & Eyes"], "Eller": ["Hands", "Hands as Intent"],
   "Duruş": ["Posture", "Posture & Weight of Decision"], "Bakış": ["Gaze", "Gaze Direction"],
   "Tempo": ["Tempo", "Tempo & Stillness"], "Seçim": ["Choice", "The Central Choice on the Body"],
   "Bedel": ["Cost", "Cost & Aftermath"], "Final": ["Final", "Final Beat Legibility"],
   "Orantı": ["Proportion"]}),
 "⑪ IŞIK": ("T11_ISIK_KALITE.md", {
   "Yön": ["Direction", "Key Direction Continuity"], "Gölge": ["Shadow", "Shadow Quality & Fill"],
   "Isı": ["Temperature", "Colour Temperature"], "Kaynak": ["Source", "Practical Sources"],
   "Pozlama": ["Exposure", "Exposure at Cuts"], "Klip içi": ["In-clip consistency", "In-Clip Stability"],
   "Sınır": ["Boundary logic", "Zone Boundaries"], "Atmosfer": ["Atmosphere", "Atmosphere Honesty"]}),
 "⑫ HOOK": ("T12_HOOK_KALITE.md", {
   "Hook": ["Hook Strength", "Hook Question", "Hook"],
   "Kapak": ["Cover Match", "Cover Second", "Cover"],
   "Risk": ["Risk / Payoff", "Stakes by the First Share Moment", "Risk"],
   "Paylaşım": ["Shareability", "Share Moments Stand Alone"],
   "Plato": ["Plateau Avoidance", "Plateau"],
   "Doruk": ["Peak", "Peak Placement"],
   "Çıkış": ["Outro", "Exit & Return"],
   "Format": ["Format Compatibility", "Format Fit", "Format"]}),
 # 14.09.2026 · sahip talebi: hareket mantığı + yön/hedef mercekleri
 "⑭ HAREKET": ("T14_HAREKET_KALITE.md", {
   "Amaç": ["Purpose Legibility"], "Yürüyüş": ["Locomotion Sense"],
   "Dönüş": ["Turn & Rotation Logic"], "El/Nesne": ["Hands & Object Handling"],
   "Döngü": ["Loop & Repetition"], "Tamamlama": ["Commitment & Completion"],
   "Beden": ["Body Coherence"], "Tepki": ["Reaction Sense"]}),
 "⑮ YÖN": ("T15_YON_KALITE.md", {
   "Hedef": ["Target Establishment"], "Bakış": ["Look Direction"],
   "Dönüş/Gidiş": ["Turn & Travel Direction"], "Uzanma/Nişan": ["Reach & Aim"],
   "Ateş/Atış": ["Fire · Trigger · Throw · Release", "Fire / Trigger / Throw / Release", "Fire, Trigger, Throw & Release"],
   "Kesme yönü": ["Screen Direction Across Cuts"], "Kamera": ["Camera-Relative Sense"],
   "Sonuç": ["Consequence on Target"]}),
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


def satir_kur(r, film_dir=None, spec_var=False, tarih=None, bolum=None):
    """rapor_kontrol sonucundan tek T satırı üret → (tablo dosyası, satır anahtarı, satır) | None

    bolum=(n, m) [13.09.2026 · KILAVUZ_REHBERI §2.6]: QA birimi BÖLÜM olan filmde
    her yarım kendi satırını alır — `**<Film>** B1` · `**<Film>** B2`. Etiket
    KALININ DIŞINDA durur: sayac.sh yalnız kalın adı okur, iki satır aynı film
    klasörüne çözülür; tabloya_yaz ise etiketi anahtara katar ki B1 ile B2
    birbirinin üstüne yazmasın."""
    if r["mercek"] not in T:
        return None
    if r["karar"] in ("KESİK", "GEÇERSİZ", "TEKRAR"):      # ✂️ KESİK: koşu değil (14.09.2026)
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
    anahtar = f"**{ad}**" + (f" B{bolum[0]}" if bolum else "")
    isaret = ""
    if r.get("mod") != "D":
        isaret += " Ⓥ"
        if spec_var:
            isaret += " ⛔"
    if r["karar"] == "ŞARTLI":
        isaret += " ⚠️"
    t = tarih or date.today().strftime("%d.%m")

    h = [f"{anahtar}{isaret}"]
    if dosya.startswith(("T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "T14", "T15")):
        h.append(t)
    if dosya.startswith(("T6", "T7", "T8", "T9", "T10", "T11", "T12", "T14", "T15")):
        h.append(r.get("mod") or "V")
    if dosya.startswith("T1_"):
        h += [(r.get("format") or "⬜").upper(), str(r.get("sahne") or "⬜")]
    if dosya.startswith("T4_"):
        h += [(r.get("format") or "⬜").upper(), "⬜"]
    if dosya.startswith("T3_"):
        h.append(r.get("audio_state") or "⬜")

    h += [bulunan.get(k, "⬜") for k in harita]
    top = (f'{r["son_ort"]:.1f}'.replace(".", ",")) if r.get("son_ort") is not None else "—"
    h.append(f"**{top}**")
    if dosya.startswith(("T5", "T7", "T8", "T9", "T10", "T11", "T12", "T14", "T15")):
        h.append("⬜")
    if dosya.startswith("T6"):
        h += ["⬜", "⬜"]
    return dosya, anahtar, "| " + " | ".join(h) + " |"


def tabloya_yaz(kok, dosya, film_adi, satir):
    """Tabloya ekle; aynı filmin satırı varsa YERİNE yaz (üst üste birikmez).

    film_adi = satır anahtarı: `**Ad**` ya da bölüm koşusunda `**Ad** B1`.
    Çıplak `**Ad**` bir bölüm satırıyla (`**Ad** B1`) EŞLEŞMEZ — aksi hâlde
    tam-film satırı ilk bölüm satırını ezerdi."""
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
    anahtar = film_adi if film_adi.startswith("**") else f"**{film_adi}**"
    bolumlu = re.search(r"\*\* B\d+$", anahtar) is not None
    for i in range(ayrac + 1, son + 1):
        if bolumlu:
            eslesti = re.search(re.escape(anahtar) + r"(?!\d)", L[i]) is not None
        else:
            eslesti = anahtar in L[i] and not re.search(re.escape(anahtar) + r" B\d+", L[i])
        if eslesti:
            L[i] = satir
            p.write_text("\n".join(L), encoding="utf-8")
            return f"↻ {dosya}: '{film_adi}' satırı GÜNCELLENDİ"
    L.insert(son + 1, satir)
    p.write_text("\n".join(L), encoding="utf-8")
    return f"+ {dosya}: '{film_adi}' satırı EKLENDİ"
