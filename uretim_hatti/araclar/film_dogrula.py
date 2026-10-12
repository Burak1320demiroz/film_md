#!/usr/bin/env python3
"""Yeni hat film klasörünün YAPI kontrolü — eksik alan, biçim, kesin tavanlar (her çekim 10 s · sayı = HEDEF_SURE/10).

    python3 uretim_hatti/araclar/film_dogrula.py <film klasörü> [--bolum cekim prompt …]

Bölümler: kunye · hikaye · cekim · replik · sahneleme · prompt · muzik · durum  (varsayılan: hepsi) · yayin (yalnız açıkça)
Faz kapıları: F3 çekim → --bolum kunye hikaye cekim · F3 sahneleme → --bolum sahneleme · F4 → --bolum replik muzik ·
              F5 → --bolum cekim sahneleme prompt · F9 → --bolum yayin (YAYIN_PAKETI.md).

12.10.2026 sahip kararları (THE_MAYDAY_SEA ile):
  · §5 Kaynak "model sesi (telsiz | voice-over | ağız kadrajda)": replik video promptuna BİREBİR yazılır (tırnak ya da
    iki nokta), Omni konuşmayı videoda üretir; o Video bloğunda konuşma tarifi hata değildir; tavan 8 s (ağız kadrajda 5 s);
  · §7 MÜZİK PROMPTU ```text bloğu (İngilizce, ≥200 karakter) MUZIK var olan her filmde — yeni biçimde hata, eskide uyarı;
  · §6 ORTAM YATAĞI + GEÇİŞ tabloları (klipler arası ses ve görüntü sürekliliği) yoksa uyarı → GECIS_VE_SES_SUREKLILIGI.md.
Çıkış kodu: 0 hata yok · 1 HATA var (UYARI çıkışı etkilemez) · 2 kullanım.

10.10.2026 sahip kararı (yalnız YENİ filmler — §3 tablosunda "No" sütunu olanlar; eski biçimde ⚠️ ile atlanır):
  · referanslar numaralı ve adlı: ref/<No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>"; EKLE/KAYNAK satırındaki her
    referans o çekimin görsel promptunda "Reference <No>" anahtarıyla açıkça adlandırılır (ve tersi);
  · özne başına TEK referans sayfası: bir karakterin önden/yandan/arkadan/üstten görünüşü, yüz yakını ve durum
    değişimleri aynı görselde panel olarak durur; aynı özne kökünün (SELA · SELA_yuz) ikinci satırı hata;
  · her video promptu 10 saniyeyi 2-4 vuruşa böler: "0-3 s … 3-7 s … 7-10 s" (0'da başlar, 10'da biter, boşluksuz,
    her vuruş ≥2 s). Saniye-altı mikro liste değil, vuruş planı.

Bu betik İÇERİK yargılamaz (hikâye iyi mi, prompt güzel mi); yalnız olguya bakar.
Eski hattın 2.950 satırlık kapısının dersi: kapı, kalite yerine kapıyı geçmeyi ödüllendirir.
"""
import argparse
import re
import sys
from pathlib import Path

MODLAR = {"Frames to Video", "Ingredients to Video", "Text to Video"}
# 08.10.2026 sahip kararı: her çekim 10 s; çekim sayısı = HEDEF_SURE / 10 (2 dk 12 · 4 dk 24 · 8 dk 48 · 16 dk 96).
# Flow'un Veo klibi 4/6/8 s verir; 10 s'ye ulaşma yöntemi SMOKE_TEST P14'te ölçülür (FLOW_GERCEKLERI §9).
CEKIM_SURESI = 10.0
ZIHINSEL = re.compile(
    r"\b(reali[sz]e|notice|decide|understand|remember|feel|feels|wants?|plans\b|knows?|thinks?|"   # plans\b: Türkçe "plan/planda" (kadraj) değil
    r"fark ed|anlar|anlıyor|karar ver|hatırl|hisseder|düşünür|ister\b|istiyor|bilir)", re.I)
META = re.compile(r"\b[SKCG]\d{2}\b|Clip \d+ of|IN FRAME:|START FRAME:|LIP-SYNC|NEGATIVE:|\[LESSON|\bD\d{2,3}\b")
TAVAN = 4300
MAX_HALKA = 4
# 22.09.2026'dan beri prompt içinde zincir DİLİ yasak; kareler EKLE satırı + iş emriyle verilir
ZINCIR_DIL = re.compile(r"previous clip|last frame|first frame|end frame|start frame|continues? from|"
                        r"\bZ\d+\.\d+\b", re.I)
# 06.10.2026 · 12 filmin ham QA'sı × prompt karşılaştırması: model yalnız bu promptu görür — sıra numarası,
# başka çekime atıf, film geneli ifade ve konuşma tarifi ya boşa düşer ya da kusur çağırır (THE_LAST_GATE K18 · K87)
SIRA_NO = re.compile(r"\b(scene|clip|shot) \d+ of \d+", re.I)
ATIF = re.compile(r"\b(scene|clip|shot|take)\s*#?\d+\b|\b(previous|next|earlier|later|opening|final)\s+(shot|scene)\b|"
                  r"\b(next|earlier|later|opening|final)\s+clip\b|\bas before\b|"
                  r"\b(same|identical)\b[^.]{0,60}?\bas (in )?(the )?(scene|clip|shot)\b", re.I)
FILM_GENELI = re.compile(r"\b(whole|entire)\s+(film|movie|story)\b|\bthe (film|movie)\b(?!\s+(grain|stock|look|emulsion))|"
                         r"\bthroughout the (film|movie|story)\b|\b(start|end|beginning|rest) of the (film|movie|story)\b|"
                         r"\b(later|earlier) in the (film|movie|story)\b", re.I)
_SOZ = (r"speaks?|speaking|spoke|spoken|says|said|saying|talks?|talking|whispers?|shouts?|yells?|calls out|call-outs?|"
        r"utters?|announces?|announcements?|narration|names (his|her|their|the)|voices?|dialogue|conversation|"
        r"radio (chatter|call|message|voice)|over the radio|words?|speech|lines?")
OLUMSUZ_SOZ = re.compile(r"\b(no|without|never|not|nor|nobody|none)\s+([\w-]+\s+){0,2}?(" + _SOZ + r")\b", re.I)
KONUSMA = re.compile(r"\b(" + _SOZ.replace("|words?|speech|lines?", "") + r")\b", re.I)
# yalnız kadrajın TAMAMI için söylenen "insan yok" (no one at the lander gibi yerel yokluk sayılmaz)
INSANSIZ = re.compile(r"\b(no|zero) (people|persons?|humans?|human (figures?|characters?)|figures?)\b"
                      r"(?=\s*([,.;]|in (the )?frame|at all|anywhere(?!\s+(inside|in|on|at|near)\b)|visible|$))", re.I)
KISI = re.compile(r"\b(she|he|her|his|him|the (astronaut|pilot|engineer|technician|woman|man|character|crew))\b", re.I)
# 10.10.2026 sahip kararı: referans dosyası ref/<No>.<AD>_v<k>.png · görsel promptta "Reference <No>" anahtarı ·
# video promptunda 10 s'lik vuruş planı "a-b s". Yalnız yeni biçim (§3 "No" sütunu) filmlerde denetlenir.
REF_DOSYA = re.compile(r"ref/(\d+)\.([A-Za-z0-9_\-]+)_v\d+\.png")
REF_AD = re.compile(r"^`?(\d+)\.([A-Za-z0-9_\-]+)_v\d+\.png`?$")
REF_SUTUN = re.compile(r"^(\d+)\.([A-Za-z0-9_\-]+)$")
REF_ANAHTAR = re.compile(r"\b[Rr]eference (\d+)\b")
ZAMAN = re.compile(r"(\d+(?:[.,]\d+)?)\s*(?:-|–|to)\s*(\d+(?:[.,]\d+)?)\s*s(?:ec(?:onds?)?)?\b", re.I)
VURUS_MIN, VURUS_SAYI = 2.0, (2, 4)
KAMERA_SABIT = re.compile(r"\bcamera (stays|holds|remains|is held) (still|locked|fixed)\b", re.I)
DONMA = re.compile(r"\b(holds? (still|the pose|position|there)|freez(es|e)|frozen|motionless|stays still|remains still)\b", re.I)
BASLIKLAR = ["## 1. HİKÂYE", "## 2. TRETMAN", "## 3. GÖRSEL KİMLİK", "## 4. ÇEKİM LİSTESİ",
             "## 5. REPLİKLER", "## 6. SES PLANI", "## 7. MÜZİK PLANI"]
HIKAYE_ALAN = ["LOGLINE", "AMAÇ", "ENGEL", "KARAR", "SONUÇ", "BEDEL", "TEK SORU"]

hata, uyari = [], []


def bos(v):
    return not v or v.strip().startswith("<") or v.strip() in {"—", "-", ""}


def bolum(metin, baslik):
    i = metin.find(baslik)
    if i < 0:
        return ""
    j = metin.find("\n## ", i + len(baslik))
    return metin[i:j if j > 0 else len(metin)]


def tablo(metin, desen=r"^\|\s*C\d{2}\s*\|"):
    return [[h.strip() for h in s.strip().strip("|").split("|")]
            for s in metin.splitlines() if re.match(desen, s.strip())]


def sure_oku(s):
    p = s.strip().split(":")
    return int(p[0]) * 60 + float(p[1]) if len(p) == 2 else float(p[0])


def kunye(film):
    m = re.search(r"```\n(.*?)```", film, re.S)
    alan = {}
    if m:
        for s in m.group(1).splitlines():
            k = s.split(None, 1)
            if len(k) == 2:
                alan[k[0]] = k[1].strip()
    for k in ["FILM", "HEDEF_SURE", "REPLIK", "MUZIK", "FIZIK_IDDIASI"]:
        if bos(alan.get(k, "")):
            hata.append(f"künye: {k} boş")
    for k in ["REPLIK", "MUZIK", "FIZIK_IDDIASI"]:
        if alan.get(k) and alan[k] not in {"var", "yok"}:
            hata.append(f"künye: {k} = '{alan[k]}' — 'var' ya da 'yok' olmalı")
    for b in BASLIKLAR:
        if b not in film:
            hata.append(f"başlık yok: {b}")
    return alan


def hikaye(film):
    b = bolum(film, BASLIKLAR[0])
    for a in HIKAYE_ALAN:
        m = re.search(rf"^{a}\s+(.*)$", b, re.M)
        if not m or bos(m.group(1)):
            hata.append(f"hikâye: {a} boş")
    m = re.search(r"^BEDEL\s+(.*)$", b, re.M)
    if m and not bos(m.group(1)) and not re.search(r"sahne\s*\d+", m.group(1), re.I):
        hata.append("hikâye: BEDEL sahne numarası taşımıyor")


def referanslar(film):
    """§3 GÖRSEL KİMLİK: (yeni biçim mi, {No: AD}). Yeni biçim = başlıkta "No" sütunu (10.10.2026 sahip kararı).
    Dosya adı ref/<No>.<AD>_v<k>.png olmalı; numara tablodaki No ile aynı."""
    b = bolum(film, BASLIKLAR[2])
    yeni = bool(re.search(r"^\|\s*No\s*\|", b, re.M))
    refler, kokler = {}, {}
    if not yeni:
        return False, refler
    for r in tablo(b, r"^\|\s*\d+\s*\|"):
        if len(r) < 3:
            hata.append(f"referans {r[0]}: {len(r)} sütun — No · Referans · Dosya · Sürüm · SHA · Onay · Kullanan çekimler")
            continue
        no, _ad, dosya = r[0], r[1], r[2].strip()
        if no in refler:
            hata.append(f"referans {no}: numara iki kez kullanılmış")
        m = REF_AD.match(dosya)
        if not m:
            hata.append(f"referans {no}: dosya adı '{dosya}' — biçim <No>.<AD>_v<k>.png (örn. {no}.KARAKTER_v1.png)")
            continue
        if m.group(1) != no:
            hata.append(f"referans {no}: dosya adındaki numara {m.group(1)} tabloyla aynı değil")
        # 10.10.2026 sahip kararı: özne başına TEK referans sayfası (açılar, yüz yakın, durumlar aynı görselde panel);
        # SELA + SELA_yuz + SELA_arka gibi ayrı dosyalar yok
        kok = m.group(2).split("_")[0].upper()
        if kok in kokler:
            hata.append(f"referans {no}: '{m.group(2)}' — {kokler[kok]} numaralı '{kok}' zaten var; aynı öznenin açıları, yüzü ve "
                        f"durumları TEK referans sayfasında panel olur (sahip kararı 10.10.2026)")
        kokler[kok] = no
        refler[no] = m.group(2)
    return True, refler


def cekim(film, alan, refler=None, yeni_ref=False):
    satir = tablo(bolum(film, BASLIKLAR[3]))
    if not satir:
        hata.append("çekim listesi: hiç çekim satırı yok (| C01 | …)")
        return {}
    cekimler, toplam = {}, 0.0
    for r in satir:
        if len(r) < 14:
            hata.append(f"çekim {r[0]}: {len(r)} sütun — 14 olmalı (son üçü: Zincir · Baş. karesi · Bitiş karesi)")
            continue
        no, bilgi, gorunen, kadraj, _taraf, sure, mod, _risk, _ref, grup, _durum, zincir, bas, bit = r[:14]
        if no in cekimler:
            hata.append(f"çekim {no}: iki kez yazılmış")
        for ad, v in (("anlatacağı bilgi", bilgi), ("ekranda görünen", gorunen), ("kadraj", kadraj), ("grup", grup)):
            if bos(v):
                hata.append(f"çekim {no}: {ad} boş")
        if not bos(gorunen) and ZIHINSEL.search(gorunen):
            hata.append(f"çekim {no}: 'ekranda görünen' zihinsel fiil taşıyor → '{ZIHINSEL.search(gorunen).group(0)}'")
        try:
            s = float(re.sub(r"[^\d.,]", "", sure).replace(",", "."))
            toplam += s
            if abs(s - CEKIM_SURESI) > 1e-9:
                hata.append(f"çekim {no}: süre {sure} s — her çekim {CEKIM_SURESI:g} s (sahip kararı 08.10.2026)")
        except ValueError:
            hata.append(f"çekim {no}: süre sayı değil ('{sure}')")
            s = None
        if mod not in MODLAR:
            hata.append(f"çekim {no}: Flow modu '{mod}' — {sorted(MODLAR)}")
        if yeni_ref and not bos(_ref):
            for parca in re.split(r"\s*[·,]\s*", _ref.strip()):
                m = REF_SUTUN.match(parca)
                if not m:
                    hata.append(f"çekim {no}: Referans '{parca}' — biçim <No>.<AD> (örn. 1.KARAKTER); §3 numarasıyla")
                elif m.group(1) not in (refler or {}):
                    hata.append(f"çekim {no}: Referans {parca} — §3'te {m.group(1)} numaralı referans yok")
                elif refler[m.group(1)] != m.group(2):
                    hata.append(f"çekim {no}: Referans {parca} — §3'te {m.group(1)} numarası '{refler[m.group(1)]}' adını taşıyor")
        cekimler[no] = {"sure": s, "mod": mod, "grup": grup,
                        "zincir": None if bos(zincir) else zincir, "bas": bas, "bit": bit}
    if alan.get("HEDEF_SURE") and not bos(alan["HEDEF_SURE"]):
        try:
            hedef = sure_oku(alan["HEDEF_SURE"])
            # 08.10.2026 sahip kararı: her çekim 10 s → çekim sayısı = HEDEF_SURE / 10, toplam tam hedef
            if abs(hedef / CEKIM_SURESI - round(hedef / CEKIM_SURESI)) > 1e-9:
                hata.append(f"künye: HEDEF_SURE {alan['HEDEF_SURE']} — {CEKIM_SURESI:g} s'nin katı olmalı (çekim = {CEKIM_SURESI:g} s)")
            else:
                beklenen = round(hedef / CEKIM_SURESI)
                if len(cekimler) != beklenen:
                    hata.append(f"çekim listesi: {len(cekimler)} çekim × {CEKIM_SURESI:g} s = {len(cekimler) * CEKIM_SURESI:.0f} s, "
                                f"hedef {hedef:.0f} s → {beklenen} çekim olmalı")
        except ValueError:
            hata.append(f"künye: HEDEF_SURE okunamadı ('{alan['HEDEF_SURE']}')")
    return cekimler


def replikler(film):
    return tablo(bolum(film, BASLIKLAR[4]), r"^\|\s*R?\d+\s*\|")


AGIZ = re.compile(r"ağız", re.I)          # Kaynak sütunu "ağız kadrajda" → model dudak senkronu, ≤5 s, sayı yok
# 12.10.2026 sahip kararı (THE_MAYDAY_SEA): Kaynak "model sesi (telsiz | voice-over | ağız kadrajda)" → replik video
# promptuna BİREBİR yazılır, Omni modeli konuşmayı videoda üretir; kurguda eklenen kayıt yedek. Ağız kadrajda değilse
# (telsiz, voice-over) dudak senkronu yok → tavan 8 s, rakam serbest. Prompttaki konuşma tarifi bu çekimde hata değildir.
MODEL_SES = re.compile(r"ağız|model sesi", re.I)
# 06.10.2026 sahip kararı: filmlerde akıcı diyalog olur → REPLIK varsayılan var; bant hedef süreye göre
BANT = [(150, 6, 12), (300, 12, 24), (600, 20, 40), (10 ** 6, 40, 70)]


def model_sesi_satirlari(film):
    """Modelin söyleyeceği replikler (Kaynak: ağız kadrajda ya da model sesi): çekim → [metin].
    Video promptu bu metni birebir taşır (tırnak içinde ya da iki noktadan sonra)."""
    model = {}
    for r in replikler(film):
        if len(r) >= 8 and MODEL_SES.search(r[4]):
            model.setdefault(r[1], []).append(r[6].strip().strip('"“”'))
    return model


agiz_satirlari = model_sesi_satirlari     # eski ad (10.10.2026 öncesi çağıranlar için)


def replik(film, alan, cekimler):
    satir = replikler(film)
    if alan.get("REPLIK") == "var" and not satir:
        hata.append("replikler: REPLIK var ama tablo boş")
    if alan.get("REPLIK") == "yok" and satir:
        uyari.append("replikler: REPLIK yok ama tabloda satır var")
    for r in satir:
        if len(r) < 8:
            hata.append(f"replik {r[0]}: {len(r)} sütun — 8 olmalı")
            continue
        no, ck, sn, _kim, kaynak, kayit, metin, sure = r[:8]
        agiz = bool(AGIZ.search(kaynak))
        model = bool(MODEL_SES.search(kaynak))
        tavan = 5 if agiz else 8
        tur = "ağız kadrajda" if agiz else ("model sesi, 10 s klip" if model else "kurguda eklenen ses")
        if cekimler and ck not in cekimler:
            hata.append(f"replik {no}: çekim '{ck}' listede yok")
        if kayit not in {"HUMAN", "MACHINE"}:
            hata.append(f"replik {no}: kayıt '{kayit}' — HUMAN | MACHINE")
        try:
            if float(re.sub(r"[^\d.,]", "", sure).replace(",", ".")) > tavan:
                hata.append(f"replik {no}: {sure} s — en çok {tavan} s ({tur})")
        except ValueError:
            hata.append(f"replik {no}: süre sayı değil ('{sure}')")
        if agiz and kayit == "HUMAN" and re.search(r"\d", metin):
            uyari.append(f"replik {no}: ağız kadrajdaki insan repliğinde rakam — dudak senkronu bozulur, sayıyı kurguda eklenen ses söylesin")
    if alan.get("REPLIK") == "var" and satir:
        try:
            hedef = sure_oku(alan.get("HEDEF_SURE", ""))
        except (ValueError, IndexError):
            return
        alt, ust = next((a, u) for s, a, u in BANT if hedef <= s)
        if not alt <= len(satir) <= ust:
            uyari.append(f"replikler: {len(satir)} replik — {alan['HEDEF_SURE']} için bant {alt}-{ust}; "
                         f"dışındaysa gerekçe FILM.md §5 altına")


def sayi(v):
    try:
        return float(re.sub(r"[^\d.,]", "", v).replace(",", "."))
    except ValueError:
        return None


# 12.10.2026 sahip kararı: her yeni filmde müzik promptu FILM.md §7'de durur (F4 taslak, F8 kesin), Flow Music'e
# yapıştırılır. Ayrıca klipler arası keskin kesme ve kesmede komple değişen arka ses için §6'da ORTAM YATAĞI
# (mekân başına kesintisiz yatak, klipleri aşar) ve GEÇİŞ (kesme başına tür + ses köprüsü) tabloları
# (uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md). Yeni biçim (§3 numaralı) filmde müzik promptu eksikse hata, eskide uyarı;
# yatak/geçiş tabloları F4/F8'de dolar → her zaman uyarı.
MUZIK_PROMPTU = re.compile(r"MÜZİK PROMPTU[^\n]*\n+```text\n(.*?)```", re.S)
TURKCE_HARF = re.compile(r"[çğıöşüÇĞİÖŞÜ]")


def muzik(film, alan, yeni_ref):
    if alan.get("MUZIK") != "var":
        return
    b = bolum(film, BASLIKLAR[6])
    m = MUZIK_PROMPTU.search(b)
    sorun = None
    if not m or bos(m.group(1)):
        sorun = "§7 MÜZİK PROMPTU bloğu yok ya da doldurulmamış (MUZIK var → her filmde Flow Music promptu; F4 taslak, F8 kesin)"
    elif TURKCE_HARF.search(m.group(1)):
        sorun = "§7 MÜZİK PROMPTU Türkçe karakter içeriyor — Flow Music promptu İngilizce yazılır"
    elif len(m.group(1).strip()) < 200:
        sorun = f"§7 MÜZİK PROMPTU {len(m.group(1).strip())} karakter — süre, açılış, yükseliş/susma noktaları ve palet yazılır (≥200)"
    if sorun:
        (hata if yeni_ref else uyari).append(sorun)


def ses_surekliligi(film):
    b = bolum(film, BASLIKLAR[5])
    for ad in ("ORTAM YATAĞI", "GEÇİŞ"):
        if ad not in b:
            uyari.append(f"§6'da {ad} tablosu yok — klipler arası ses ve görüntü sürekliliği planlanmamış "
                         f"(uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md; F4'te ses-tasarimcisi, F8'de kurgucu doldurur)")


def sahneleme(klasor, film, alan, cekimler):
    zincirler = {}
    sira = list(cekimler)
    for no in sira:
        z = cekimler[no]["zincir"]
        if z:
            zincirler.setdefault(z, []).append(no)
    if not zincirler:
        return
    klip = sayi(alan.get("KLIP_SURESI", "")) if not bos(alan.get("KLIP_SURESI", "")) else None
    if klip is None:
        hata.append("künye: zincir var ama KLIP_SURESI ölçülmemiş (Flow'dan ölç, saniye yaz)")
    f = klasor / "SAHNELEME.md"
    if not f.exists():
        hata.append("SAHNELEME.md yok — zincirli çekim var")
        return
    s = f.read_text(encoding="utf-8")
    z_tablo = {r[0]: r for r in tablo(bolum(s, "## 1. ZİNCİRLER"), r"^\|\s*Z\d+\s*\|")}
    k_tablo = {r[0]: r for r in tablo(bolum(s, "## 2. ANAHTAR KARELER"), r"^\|\s*Z\d+\.\d+\s*\|")}
    d_tablo = {r[0]: r for r in tablo(bolum(s, "## 4. DELTA KONTROLÜ"))}
    for z, halkalar in zincirler.items():
        if z not in z_tablo:
            hata.append(f"sahneleme: {z} §1 ZİNCİRLER'de yok")
        elif len(z_tablo[z]) < 5 or bos(z_tablo[z][4]):
            hata.append(f"sahneleme: {z} için 'neden zincir' gerekçesi boş (zincir seçmelidir)")
        if len(halkalar) > MAX_HALKA:
            hata.append(f"sahneleme: {z} {len(halkalar)} halka — en çok {MAX_HALKA}")
        idx = [sira.index(h) for h in halkalar]
        if idx != list(range(idx[0], idx[0] + len(idx))):
            hata.append(f"sahneleme: {z} halkaları çekim listesinde ardışık değil ({' '.join(halkalar)})")
        for i, h in enumerate(halkalar):
            c = cekimler[h]
            if c["mod"] != "Frames to Video":
                hata.append(f"sahneleme: {h} zincirde ama Flow modu '{c['mod']}' — Frames to Video olmalı")
            if klip is not None and c["sure"] is not None and c["sure"] > klip + 0.01:
                hata.append(f"sahneleme: {h} süresi {c['sure']:g} s > KLIP_SURESI {klip:g} s")
            if h not in d_tablo:
                hata.append(f"sahneleme: {h} için §4 DELTA KONTROLÜ satırı yok")
            bas, bit = c["bas"], c["bit"]
            onceki = halkalar[i - 1] if i else None
            if bas.startswith(("son:", "t:")):          # A / A′
                hedef = re.sub(r"^(son|t):", "", bas).split("@")[0]
                if hedef != onceki:
                    hata.append(f"sahneleme: {h} başlangıcı '{bas}' önceki halkayı ({onceki or 'yok'}) göstermiyor")
            else:                                       # B
                for k in (bas, bit):
                    if bos(k) or k not in k_tablo:
                        hata.append(f"sahneleme: {h} anahtar karesi '{k}' §2'de yok")
                    elif len(k_tablo[k]) < 5 or any(bos(x) for x in k_tablo[k][2:5]):
                        hata.append(f"sahneleme: anahtar kare {k} tarifi eksik (poz · kamera · ışık)")
                if onceki and cekimler[onceki]["bit"] != bas and not bas.startswith(("son:", "t:")):
                    hata.append(f"sahneleme: {onceki} bitişi '{cekimler[onceki]['bit']}' ≠ {h} başlangıcı '{bas}'")
    # replik dikişi aşmasın
    for r in replikler(film):
        if len(r) < 8:
            continue
        no, ck, sn, *_ , sure = r[:8]
        c = cekimler.get(ck)
        if not c or not c["zincir"]:
            continue
        son_halka = zincirler[c["zincir"]][-1] == ck
        a, b = sayi(sn), sayi(sure)
        if not son_halka and a is not None and b is not None and c["sure"] and a + b > c["sure"] + 0.01:
            hata.append(f"replik {no}: {ck} içinde {a:g}+{b:g} s — dikişi aşıyor (çekim {c['sure']:g} s)")


def metin_kontrol(no, g, metin, agiz=None):
    """Tek prompt bloğunun içeriğe bakmayan, olguya bakan kontrolleri.
    agiz: bu çekimin modelin söyleyeceği replikleri (Kaynak: ağız kadrajda | model sesi) — yalnız Video bloğunda
    konuşmaya izin verir ve repliğin birebir yazılmasını ister."""
    if len(metin) > TAVAN:
        hata.append(f"prompt {no} {g}: {len(metin)} karakter — tavan {TAVAN} (Veo hata veriyor)")
    m = META.search(metin) or SIRA_NO.search(metin)
    if m:
        hata.append(f"prompt {no} {g}: meta etiket '{m.group(0)}' — kadraja yazı olarak basılabilir")
    m = ZINCIR_DIL.search(metin)
    if m:
        hata.append(f"prompt {no} {g}: zincir dili '{m.group(0)}' — kareler EKLE satırıyla verilir, prompta yazılmaz")
    m = ATIF.search(SIRA_NO.sub(" ", metin))
    if m:
        hata.append(f"prompt {no} {g}: başka çekime atıf '{m.group(0)}' — model o çekimi görmez; kamerayı/konumu burada tam yaz")
    m = FILM_GENELI.search(metin)
    if m:
        hata.append(f"prompt {no} {g}: film geneli ifade '{m.group(0)}' — model yalnız bu klibi görür")
    if agiz and g == "Video":
        # 07.10.2026: iki resmî Google belgesi çelişiyor (Vertex: iki nokta, tırnak yok · Gemini API: tırnak) →
        # SMOKE P9 karar verene kadar iki biçim de kabul: says, "<line>"  |  says: <line>
        duz = metin.replace("“", '"').replace("”", '"')
        for satir in agiz:
            if f'"{satir}"' not in duz and not re.search(r":\s*" + re.escape(satir), duz):
                hata.append(f"prompt {no} Video: modelin söyleyeceği replik birebir yok (tırnak içinde ya da \"says: …\") → \"{satir}\"")
    else:
        m = KONUSMA.search(OLUMSUZ_SOZ.sub(" ", metin))
        if m:
            hata.append(f"prompt {no} {g}: konuşma/ses tarifi '{m.group(0)}' — model konuşma ve ağız hareketi üretir; "
                        f"replik kurguda eklenir (model söyleyecekse FILM.md §5 Kaynak = model sesi (…) ya da ağız kadrajda)")
    m, k = INSANSIZ.search(metin), KISI.search(metin)
    if m and k:
        hata.append(f"prompt {no} {g}: '{m.group(0)}' diyor ama '{k.group(0)}' diye bir kişiye gönderme yapıyor")


def referans_anahtari(no, govde, bloklar, refler):
    """EKLE/KAYNAK satırındaki her ref/<No>.<AD>_v<k>.png, görsel promptta (yoksa video) "Reference <No>" diye
    adlandırılmış mı; promptta adı geçen her Reference <No> eklenmiş mi; numara ve ad §3 ile aynı mı."""
    bas = govde.split("### ", 1)[0]
    satirlar = re.findall(r"^(?:EKLE|KAYNAK)\s+(.*)$", bas, re.M)
    ekli = {}
    for s in satirlar:
        for n, ad in REF_DOSYA.findall(s):
            ekli[n] = ad
            if n not in refler:
                hata.append(f"prompt {no}: ref/{n}.{ad} — §3'te {n} numaralı referans yok")
            elif refler[n] != ad:
                hata.append(f"prompt {no}: ref/{n}.{ad} — §3'te {n} numarası '{refler[n]}' adını taşıyor")
    g = "Görsel" if "Görsel" in bloklar and not bos(bloklar["Görsel"]) else "Video"
    metin = bloklar.get(g, "")
    anilan = set(REF_ANAHTAR.findall(metin))
    for n in ekli:
        if n not in anilan:
            hata.append(f"prompt {no} {g}: ref/{n}.{ekli[n]} ekleniyor ama promptta 'Reference {n}' anahtarı yok "
                        f"(sahip kararı 10.10.2026: her referans numarası ve rolüyle açıkça yazılır)")
    for n in sorted(anilan - set(ekli), key=int):
        hata.append(f"prompt {no} {g}: 'Reference {n}' yazıyor ama EKLE/KAYNAK satırında {n} numaralı referans yok")


def zaman_plani(no, metin):
    """Video promptu 10 s'yi 2-4 vuruşa böler: 'a-b s' aralıkları 0'da başlar, 10'da biter, boşluksuz, her vuruş ≥2 s."""
    ara = []
    for a, b in ZAMAN.findall(metin):
        a, b = float(a.replace(",", ".")), float(b.replace(",", "."))
        ara.append((a, b))
    if not ara:
        hata.append(f"prompt {no} Video: 10 s zaman planı yok — 2-4 vuruş 'a-b s' biçiminde (örn. 0-3 s · 3-7 s · 7-10 s; "
                    f"sahip kararı 10.10.2026)")
        return
    ara.sort()
    if not VURUS_SAYI[0] <= len(ara) <= VURUS_SAYI[1]:
        hata.append(f"prompt {no} Video: {len(ara)} vuruş — {VURUS_SAYI[0]}-{VURUS_SAYI[1]} olmalı")
    if ara[0][0] != 0:
        hata.append(f"prompt {no} Video: zaman planı {ara[0][0]:g} s'de başlıyor — 0'da başlamalı")
    if abs(ara[-1][1] - CEKIM_SURESI) > 1e-9:
        hata.append(f"prompt {no} Video: zaman planı {ara[-1][1]:g} s'de bitiyor — {CEKIM_SURESI:g} s'de bitmeli (her çekim 10 s)")
    for (a1, b1), (a2, _b2) in zip(ara, ara[1:]):
        if abs(b1 - a2) > 1e-9:
            hata.append(f"prompt {no} Video: {b1:g} s ile {a2:g} s arasında boşluk ya da bindirme — vuruşlar ardışık olmalı")
    for a, b in ara:
        if b - a < VURUS_MIN - 1e-9:
            hata.append(f"prompt {no} Video: vuruş {a:g}-{b:g} s {b - a:g} s — en az {VURUS_MIN:g} s (saniye-altı mikro liste yazılmaz)")
    son = metin[metin.rfind(f"{ara[-1][0]:g}"):] if len(ara) > 1 else metin
    m = DONMA.search(KAMERA_SABIT.sub(" ", son))      # sabit kamera donma değildir
    if m:
        uyari.append(f"prompt {no} Video: son vuruşta '{m.group(0)}' — donan bitiş tempo düzlüğü verdi (LAST_GATE 87/92 klip); "
                     f"hareket 10. saniyede bitsin")


def prompt(klasor, cekimler, film="", refler=None, yeni_ref=False):
    dosyalar = sorted((klasor / "PROMPTLAR").glob("*.md"))
    if not dosyalar:
        hata.append("PROMPTLAR/: dosya yok")
        return
    bulunan, is_emri = {}, set()
    for f in dosyalar:
        t = f.read_text(encoding="utf-8")
        for m in re.finditer(r"^## (C\d{2}|Z\d+\.\d+)(?=\s).*?(?=^## |\Z)", t, re.M | re.S):
            bulunan[m.group(1)] = (f.name, m.group(0))
        for r in tablo(bolum(t, "## FLOW İŞ EMRİ"), r"^\|\s*\d+\s*\|"):
            if len(r) > 1:
                is_emri.add(r[1])
    anahtarlar = sorted({k for c in cekimler.values() if c.get("zincir") for k in (c["bas"], c["bit"])
                         if re.fullmatch(r"Z\d+\.\d+", k or "")})
    for k in anahtarlar:
        if k not in bulunan:
            hata.append(f"prompt {k}: anahtar kare bölümü '## {k}' yok")
            continue
        g = dict(re.findall(r"### (Görsel|Video)\s*\n```text\n(.*?)```", bulunan[k][1], re.S))
        if bos(g.get("Görsel", "")):
            hata.append(f"prompt {k}: anahtar karenin görsel promptu yok ya da doldurulmamış")
        else:
            metin_kontrol(k, "Görsel", g["Görsel"])
            if yeni_ref:
                referans_anahtari(k, bulunan[k][1], g, refler or {})
        if k not in is_emri:
            hata.append(f"prompt {k}: anahtar kare Flow iş emrinde yok")
    agiz = model_sesi_satirlari(film)
    for no, bilgi in cekimler.items():
        if no not in bulunan:
            hata.append(f"prompt {no}: PROMPTLAR/ içinde '## {no}' bölümü yok")
            continue
        ad, govde = bulunan[no]
        bloklar = dict(re.findall(r"### (Görsel|Video)\s*\n```text\n(.*?)```", govde, re.S))
        zincirli = bool(bilgi.get("zincir"))
        gerek = ["Video"] + ([] if bilgi["mod"] == "Text to Video" or zincirli else ["Görsel"])
        if zincirli and not bilgi["bas"].startswith(("son:", "t:")):
            ekle = re.search(r"^EKLE\s+(.*)$", govde, re.M)
            if not ekle or bilgi["bas"] not in ekle.group(1) or bilgi["bit"] not in ekle.group(1):
                hata.append(f"prompt {no}: EKLE satırı başlangıç {bilgi['bas']} ve bitiş {bilgi['bit']} karelerini taşımıyor")
        for g in gerek:
            if g not in bloklar or bos(bloklar[g]):
                hata.append(f"prompt {no} ({ad}): {g} promptu yok ya da doldurulmamış")
        for g, metin in bloklar.items():
            if not bos(metin):
                metin_kontrol(no, g, metin, agiz.get(no))
        if yeni_ref:
            referans_anahtari(no, govde, bloklar, refler or {})
            if "Video" in bloklar and not bos(bloklar["Video"]):
                zaman_plani(no, bloklar["Video"])
        if no not in is_emri:
            hata.append(f"prompt {no}: Flow iş emrinde satırı yok")


KOK = Path(__file__).resolve().parents[2]
KANAL_SABLON = KOK / "apexaic" / "youtube" / "PAKETLEME_SABLONU.md"
TURKCE = re.compile(r"[çğıöşüÇĞİÖŞÜ]")
YASAK_BASLIK = re.compile(r"you won.t believe|^\s*ai short film|\b(INSANE|EPIC|MIND-BLOWING|SHOCKING)\b|"
                          r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", re.I)
YASAK_ACIKLAMA = re.compile(r"let me know|see you in the next video|subscribe for weekly|\[your name\]", re.I)
YASAK_HASHTAG = {"#fyp", "#viral", "#aifilm", "#aicinema", "#veo3", "#midjourney", "#darkfantasy",
                 "#postapocalyptic", "#unrealengine", "#blender3d", "#cgi", "#3danimation", "#vfx", "#apexaicinema"}
BASLIK_SATIR = re.compile(r"^\s*(\d+)\s+\((\d+)\)\s+(VERIFIED FACT|SITUATION|STAKES|CHOICE|QUESTION|CORRECTION|QUIET)"
                          r"\s+(.+?)\s*$", re.M)
YASAK_ETIKET = re.compile(r"\b(unreal engine|blender|cgi|3d animation|veo ?3|midjourney)\b", re.I)


def sabit_blok():
    """Kanal şablonundaki çizgi arası sabit blok (her açıklamada birebir)."""
    if not KANAL_SABLON.exists():
        return []
    satirlar, icinde = [], False
    for s in KANAL_SABLON.read_text(encoding="utf-8").splitlines():
        if s.strip().startswith("──"):
            if icinde:
                return satirlar
            icinde = True
        elif icinde:
            satirlar.append(s.strip())
    return []


def kod_blogu(metin, baslik):
    m = re.search(r"```text\n(.*?)```", bolum(metin, baslik), re.S)
    return m.group(1) if m else ""


def yayin(klasor):
    """YAYIN_PAKETI.md: tamamen İngilizce · başlık uzunluğu ve sayımı · sabit blok · tam 3 hashtag · etiket ≤500."""
    f = klasor / "YAYIN_PAKETI.md"
    if not f.exists():
        hata.append("YAYIN_PAKETI.md yok")
        return
    t = f.read_text(encoding="utf-8")
    for i, s in enumerate(t.splitlines(), 1):
        if TURKCE.search(s):
            hata.append(f"yayin: satır {i} Türkçe karakter taşıyor — paket tamamen İngilizce")
            break
    yer = sorted({m.group(0) for m in re.finditer(r"<[^<>\n]{2,60}>", t)})
    if [y for y in yer if y != "<link>"]:
        hata.append(f"yayin: doldurulmamış alan {', '.join(y for y in yer if y != '<link>')[:120]}")
    if "<link>" in yer:
        uyari.append("yayin: WATCH NEXT bağlantısı '<link>' — yüklemeden önce gerçek bağlantı")
    satirlar = [m.groups() for m in BASLIK_SATIR.finditer(kod_blogu(t, "## 2. TITLE OPTIONS"))]
    if len(satirlar) < 3:
        hata.append(f"yayin: {len(satirlar)} başlık seçeneği — en az 3, biçim: `1  (59)  QUIET  <title>`")
    if satirlar and not any(a == "QUIET" for _, _, a, _ in satirlar):
        uyari.append("yayin: QUIET açılı başlık seçeneği yok")
    for no, yazili, _aci, baslik in satirlar:
        if len(baslik) > 100:
            hata.append(f"yayin: başlık {no} {len(baslik)} karakter — en çok 100")
        if int(yazili) != len(baslik):
            hata.append(f"yayin: başlık {no} karakter sayısı yanlış — yazılan {yazili}, gerçek {len(baslik)}")
        if " | " not in baslik:
            uyari.append(f"yayin: başlık {no} kanal grameri '<promise> | <FILM NAME>' değil")
        if YASAK_BASLIK.search(baslik):
            hata.append(f"yayin: başlık {no} yasaklı kalıp → '{YASAK_BASLIK.search(baslik).group(0)}'")
    secilen = kod_blogu(t, "## 1. RECOMMENDED").strip().splitlines()
    if not secilen or secilen[0].strip() not in {b for *_, b in satirlar}:
        hata.append("yayin: önerilen başlık (## 1 kod bloğunun ilk satırı) seçeneklerden biri değil")
    acik = kod_blogu(t, "## 3. DESCRIPTION")
    if not acik.strip():
        hata.append("yayin: açıklama kod bloğu boş")
        return
    ilk = acik.strip().splitlines()[0]
    if len(ilk) > 120:
        uyari.append(f"yayin: açıklamanın ilk satırı {len(ilk)} karakter — 'Show more'dan önce ~120 görünür")
    etiketler = re.findall(r"(?<!\S)#\w+", acik)
    if len(etiketler) != 3:
        hata.append(f"yayin: açıklamada {len(etiketler)} hashtag — tam 3")
    for h in etiketler:
        if h.lower() in YASAK_HASHTAG:
            hata.append(f"yayin: kanaldan çıkarılmış hashtag {h}")
    for s in sabit_blok():
        if s and s not in acik:
            hata.append(f"yayin: kanal sabit bloğu eksik ya da değişmiş → '{s[:60]}'")
            break
    m = YASAK_ACIKLAMA.search(acik)
    if m:
        hata.append(f"yayin: açıklamada yasaklı kalıp → '{m.group(0)}'")
    etiket = kod_blogu(t, "## 4. TAGS").strip()
    if len(etiket) > 500:
        hata.append(f"yayin: etiket alanı {len(etiket)} karakter — 500'ün altında")
    if YASAK_ETIKET.search(etiket):
        hata.append(f"yayin: etiketlerde araç/CGI kelimesi → '{YASAK_ETIKET.search(etiket).group(0)}'")
    if not kod_blogu(t, "## 5. PINNED COMMENT").strip():
        hata.append("yayin: sabit yorum boş")


def durum(klasor):
    f = klasor / "ODA" / "DURUM.md"
    if not f.exists():
        hata.append("ODA/DURUM.md yok")
        return
    t = f.read_text(encoding="utf-8")
    for k, d in (("FAZ", r"^FAZ\s+(\d+)\s*$"), ("TUR", r"^TUR\s+(\d+)\s*$"),
                 ("AJAN_CAGRI", r"^AJAN_CAGRI\s+(\d+)\s*/\s*(\d+)\s*$")):
        m = re.search(d, t, re.M)
        if not m:
            hata.append(f"DURUM: {k} satırı yok ya da biçimi bozuk")
        elif k == "FAZ" and not 0 <= int(m.group(1)) <= 10:
            hata.append(f"DURUM: FAZ {m.group(1)} — 0-10 olmalı")
        elif k == "AJAN_CAGRI" and int(m.group(1)) > int(m.group(2)):
            uyari.append(f"DURUM: ajan çağrısı {m.group(1)} bütçeyi ({m.group(2)}) aştı")


def main():
    ap = argparse.ArgumentParser(description="yeni hat film klasörü yapı kontrolü")
    ap.add_argument("klasor")
    ap.add_argument("--bolum", nargs="+", default=["hepsi"],
                    choices=["hepsi", "kunye", "hikaye", "cekim", "replik", "sahneleme", "prompt", "muzik", "durum", "yayin"])
    a = ap.parse_args()
    klasor = Path(a.klasor)
    f = klasor / "FILM.md"
    if not f.exists():
        print(f"⛔ {f} yok")
        return 2
    film = f.read_text(encoding="utf-8")
    sec = set(a.bolum)
    hep = "hepsi" in sec
    alan = kunye(film)                      # künye her zaman okunur; hatası yalnız seçildiyse kalır
    if not (hep or "kunye" in sec):
        hata.clear()
    if hep or "hikaye" in sec:
        hikaye(film)
    cekimler = {}
    yeni_ref, refler = False, {}
    if hep or {"cekim", "replik", "sahneleme", "prompt", "muzik"} & sec:
        n = len(hata)
        yeni_ref, refler = referanslar(film)
        if not yeni_ref:
            uyari.append("§3 referans tablosu numarasız (10.10.2026 öncesi biçim): referans anahtarı ve 10 s zaman planı denetlenmedi")
        cekimler = cekim(film, alan, refler, yeni_ref)        # replik/prompt kontrolü çekim listesine dayanır
        if not (hep or "cekim" in sec):
            del hata[n:]
    if hep or "replik" in sec:
        replik(film, alan, cekimler)
    if hep or "sahneleme" in sec:
        sahneleme(klasor, film, alan, cekimler)
    if hep or "prompt" in sec:
        prompt(klasor, cekimler, film, refler, yeni_ref)
    if hep or "muzik" in sec:                # 12.10.2026: müzik promptu (M, yeni biçim) + §6 yatak/geçiş (uyarı)
        muzik(film, alan, yeni_ref)
        ses_surekliligi(film)
    if hep or "durum" in sec:
        durum(klasor)
    if "yayin" in sec:                       # yalnız açıkça: faz 9 kapısı (şablon yer tutucuları erken fazda hata olur)
        yayin(klasor)
    print(f"film: {klasor} · bölüm: {' '.join(sorted(sec))} · çekim: {len(cekimler)}")
    for u in uyari:
        print(f"⚠️  {u}")
    for h in hata:
        print(f"⛔ {h}")
    print("✅ yapı geçerli" if not hata else f"⛔ {len(hata)} hata")
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
