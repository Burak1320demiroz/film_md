#!/bin/bash
# RUBRİK PAKETLE — rubrik + SPEC'i mercek başına TEK dosyaya basar (mod D varsayılan)
#
# NEDEN VAR (01.09.2026 · D129 · 9 film):
#   "SPEC'i operatöre ver" cümlesi dokuz filmde tutmadı — SPEC film klasöründe
#   dururken altı mercek mod V koşuldu. Cümle davranış değiştirmez; VARSAYILAN
#   değiştirir. Bu betik her mercek için operatörün YAPIŞTIRACAĞI tek dosyayı
#   üretir: ①/④/⑥ için rubrik + SPEC'in ilgili bloğu (MODE D bölümüne gömülü),
#   ②/③/⑤ için rubrik + "belge verilmez" künyesi (⑤'e yalnız üç kilit — D133),
#   ⑨/⑩/⑪/⑫ için rubrik + planın ilgili kayıtları (plan sadakati — D184, 06.09.2026).
#   Mod V koşmak için artık bilerek çıplak rubriği seçmek gerekir.
#
# KULLANIM:
#   bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> [master video]
# ÇIKTI:
#   kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/<FILM>/PAKET_<n>_<MERCEK>.md
#   + 00_PAKET_README.md  (nasıl koşulur · koşu sonrası rapor_kontrol.py)
# ⛔ Paket dosyaları BETİKTEN ÜRETİLİR, elle düzenlenmez; SPEC değişince yeniden koşulur.
set -u

F="${1:-}"; M="${2:-}"
[ -z "$F" ] && { echo "KULLANIM: rubrik_paketle.sh <film klasörü> [master]"; exit 2; }
[ -d "$F" ] || { echo "HATA: klasör yok: $F"; exit 2; }
F="$(cd "${F%/}" && pwd)"                       # mutlak yol — cd'den ÖNCE
FILM="$(basename "$F")"
cd "$(dirname "$0")/../../../.." || exit 1       # scripts → qa-isle → skills → .claude → depo kökü
FREL="${F#$PWD/}"
K="kilavuzlar_ve_sistem_dosyalari"
R="$K/QA_PROMPTLARI"
SRC="$R/_KAYNAK"          # çıplak rubrikler [D129 · 01 hamlesi 04.09.2026]
OUT="$R/FILME_OZEL/$FILM"

SPEC=$(ls -1 "$F"/*_QA_SPEC.md 2>/dev/null | head -1)
if [ -z "$SPEC" ]; then
  echo "⛔ SPEC YOK: $F/*_QA_SPEC.md bulunamadı → paket üretilmedi."
  echo "   [D117] SPEC dosyası yoksa film 'yazımı tamam' sayılmaz; önce SPEC yaz."
  exit 2
fi
mkdir -p "$OUT"

# ── SPEC bloklarını ayır (başlık '## ' ile başlar; harf başlıktan okunur) ──
blok() {   # blok A|B|C|D|UYARI|ROUTING  → o bölümün gövdesi (başlık dahil)
  local h="$1"
  awk -v H="$h" '
    /^## /{
      keep=0
      if (H=="A"      && $0 ~ /A BLOĞU/) keep=1
      if (H=="B"      && $0 ~ /B BLOĞU/) keep=1
      if (H=="C"      && $0 ~ /C BLOĞU/) keep=1
      if (H=="D"      && $0 ~ /D BLOĞU/) keep=1
      if (H=="UYARI"  && $0 ~ /RUBRİĞE UYARI/) keep=1
      if (H=="ROUTING"&& $0 ~ /HANGİ RUBRİĞE/) keep=1
    }
    keep{print}
  ' "$SPEC"
}
AILE="yatay"; grep -qE "^## .*SAHNE SPESİFİKASYONU" "$SPEC" && AILE="dikey"
HAS_D=$(grep -cE "^## .*D BLOĞU" "$SPEC")

# ── künye (D160: girdi yolu · süre · çözünürlük) ──
TARIH=$(date '+%d.%m.%Y')
if [ -n "$M" ] && [ -f "$M" ] && command -v ffprobe >/dev/null 2>&1; then
  SURE=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M" 2>/dev/null | cut -c1-7)
  COZ=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$M" 2>/dev/null)
  GIRDI="$M · ${SURE:-?} s · ${COZ:-?}"
else
  GIRDI="____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)"
fi
kunye() {  # $1 = mercek adı, $2 = mod, $3 = ek not
cat <<EOF
\`\`\`
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : $FILM
mercek    : $1
mod       : $2
girdi     : $GIRDI
SPEC      : $(basename "$SPEC")  (aile: $AILE)
üretildi  : $TARIH · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 $K/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film $FREL
$3
\`\`\`

EOF
}

# ── enjekte: rubriğin MODE D başlığının hemen altına belge blokları ──
enjekte() {   # $1 rubrik dosyası · $2 başlık regex · $3 içerik dosyası · $4 hedef
  awk -v ICF="$3" -v H="$2" '
    BEGIN{ while ((getline l < ICF) > 0) ic = ic l "\n" }
    { print }
    $0 ~ H && !done { print ""; print ic; done=1 }
  ' "$1" > "$4"
}

# ── kayit: C bloğundan etiket DESENİNE uyan kayıtlar (etiket satırı + girintili
#    devam satırları). ⑥'nın kayıt mantığının aynısı, filtre etiket üzerinden [D184].
kayit() {   # $1 = etiket regex (awk ERE) → kayıt gövdeleri
  blok C | awk -v E="$1" '
    function yaz(){ if (etiket != "" && etiket ~ E) printf "%s", govde; etiket=""; govde="" }
    /^[^[:space:]]/ && !/^```/ && !/^## / && !/^> / { yaz(); etiket=$0; govde=$0 "\n"; next }
    { if (etiket != "") govde = govde $0 "\n" }
    END { yaz() }'
}

TMP=$(mktemp -d)
# ① KARE
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den birebir · MODE D"; echo
  if [ "$AILE" = "yatay" ]; then blok A; echo; blok B; echo; blok UYARI; else blok A; fi; } > "$TMP/1.md"
{ kunye "① KARE" "D" "belge: $( [ "$AILE" = yatay ] && echo 'A + B + UYARI' || echo 'A' )";
  enjekte "$SRC/1_KARE_QA_CRITIQUE_PROMPT.md" "^## 📋 SCENE SPECIFICATION" "$TMP/1.md" /dev/stdout; } > "$OUT/PAKET_1_KARE.md"

# ④ HİKAYE
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den birebir · MODE D"; echo
  if [ "$AILE" = "yatay" ]; then blok A; echo; blok UYARI; else blok B; fi; } > "$TMP/4.md"
{ kunye "④ HİKAYE" "D" "belge: $( [ "$AILE" = yatay ] && echo 'A + UYARI' || echo 'B' )";
  enjekte "$SRC/4_HIKAYE_QA_CRITIQUE_PROMPT.md" "^## 📋 FILM SPECIFICATION" "$TMP/4.md" /dev/stdout; } > "$OUT/PAKET_4_HIKAYE.md"

# ⑥ FİZİK — NOVUM (aynen) + SAYISAL kilitler (kimlik/kostüm/yıpranma VERİLMEZ)
# ⛔ [D166] Filtre SATIR değil KAYIT seçer: C bloğunda bir kilit, etiket satırı +
#    girintili devam satırlarıdır. Eski satır-grep'i NOVUM'u tamamen düşürüyordu
#    (etiket satırında birim SEMBOLÜ yok, "0,15 saniyeden" Türkçe birim SÖZCÜĞÜ)
#    ve yerine yıpranma haritasının "6 cm" satırlarını veriyordu. Sonuç: ⑥'nın
#    PREMISE REGISTER'ı filmin KURALINI hiç görmedi, türü yazdı ve kuralı kusur
#    saydı (THE STILL SWARM, 02.09.2026 — üç kategoride 13 puan).
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den NOVUM + SAYISAL kilitler · MODE D"; echo
  echo '```'
  if [ "$HAS_D" -gt 0 ]; then blok D | grep -vE "^## "; else
    blok C | awk '
      function bos(s){ return s ~ /^[[:space:]]*$/ }
      # kayıt = sütun 0 etiketi + girintili devam satırları
      /^[^[:space:]]/ && !/^```/ { yaz(); etiket=$0; govde=$0 "\n"; next }
      { if (etiket != "") govde = govde $0 "\n" }
      END { yaz() }
      function yaz(   birim, novum, yasak) {
        if (etiket == "" || bos(govde)) return
        novum = (etiket ~ /^(NOVUM|ÖNERME|PREMISE|İHLAL)/)
        yasak = (etiket ~ /^(YIPRANMA|KASK|İNSAN|KOSTÜM|SES|EŞ KADRAJ|CANLI)/)
        # ⛔ Birim SEMBOLÜ arama: SPEC Türkçe yazılır ("0,15 saniyeden") ve
        #    birimsiz sayım kilitleri vardır ("EWS 240-300 parça"). Kapsam
        #    DIŞLAMAYLA kurulur — kimlik/kostüm/yıpranma yukarıdaki yasak
        #    listesinde; kalan her sayılı kayıt fiziksel kilittir.
        birim = (govde ~ /[0-9]/)
        if (novum) { printf "⭐ PREMISE REGISTER GİRDİSİ — bu bir KUSUR DEĞİL, filmin KURALIDIR:\n%s", govde }
        else if (birim && !yasak) printf "%s", govde
        etiket=""; govde=""
      }'; fi
  echo '```'; } > "$TMP/6.md"
{ kunye "⑥ FİZİK" "D" "belge: $( [ "$HAS_D" -gt 0 ] && echo 'D bloğu (sayısal kilit listesi)' || echo 'C bloğunun SAYISAL satırları' ) — kimlik/kostüm/olay satırları bu merceğe VERİLMEZ";
  enjekte "$SRC/6_FIZIK_QA_CRITIQUE_PROMPT.md" "^## 📋 NUMERIC LOCK LIST" "$TMP/6.md" /dev/stdout; } > "$OUT/PAKET_6_FIZIK.md"

# ② DEVAMLILIK · ③ SES — belge verilmez (tasarım)
{ kunye "② DEVAMLILIK" "V (tasarım — belge VERİLMEZ)" "FLAGS koşudan SONRA SPEC C bloğundan cevaplanır. ⚠️ SPEC sayaç yazıyorsa 'Counter Logic N/A' ÖLÇÜM BOŞLUĞUDUR [D134]";
  cat "$SRC/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md"; } > "$OUT/PAKET_2_DEVAMLILIK.md"
{ kunye "③ SES" "V (tasarım — belge VERİLMEZ)" "⚠️ AUDIO STATE bir dinleme beyanıdır; ses kanalı VARLIĞI ⑪ ile ölçülür [D136]";
  cat "$SRC/3_SES_QA_CRITIQUE_PROMPT.md"; } > "$OUT/PAKET_3_SES.md"

# ⑤ ARKA PLAN — yalnız ÜÇ kilit (D133)
UC=$(blok C | grep -iE "mesafe|sayaç|sayac|ekran yön|EKRAN YÖNÜ|screen direction|sabit çevre|ölçek|distance|monoton" | head -14)
{ kunye "⑤ ARKA PLAN" "V + üç kilit (D133)" "⑤'e kimlik/kostüm/olay kilidi VERİLMEZ; yalnız mesafe/ölçek sayacı · ekran yönü · sabit çevre nesneleri:";
  if [ -n "$UC" ]; then echo '```'; echo "$UC"; echo '```'; echo; fi
  cat "$SRC/5_ARKA_PLAN_QA_CRITIQUE_PROMPT.md"; } > "$OUT/PAKET_5_ARKA_PLAN.md"

# ⑦ AKSİYON — sahne haritası (A) + davranış kilitleri (C), sayısal olmayanlar da dâhil
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den A + C · MODE D"; echo
  blok A; echo; blok C; } > "$TMP/7.md"
{ kunye "⑦ AKSİYON" "D" "belge: A (sahne haritası) + C (kilitler). ⛔ Rubriğin kuralı: ANLATIM CÜMLESİ önce EKRANDAN yazılır, sonra plana bakılır — ters sıra sahte PASS üretir";
  enjekte "$SRC/7_AKSIYON_QA_CRITIQUE_PROMPT.md" "^## 📋 BEAT LOCK LIST" "$TMP/7.md" /dev/stdout; } > "$OUT/PAKET_7_AKSIYON.md"

# ⑧ EFOR — yük / süre / ekipman / yaralanma taşıyan satırlar
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den A + C · MODE D"; echo
  blok A; echo; blok C; } > "$TMP/8.md"
{ kunye "⑧ EFOR" "D" "belge: A (sahne haritası) + C (kilitler). ⛔ FATURA CÜMLESİ önce EKRANDAN. ⚠️ Düşük yerçekimi düşük efor değildir — kütle ve atalet değişmez";
  enjekte "$SRC/8_EFOR_QA_CRITIQUE_PROMPT.md" "^## 📋 EFFORT LOCK LIST" "$TMP/8.md" /dev/stdout; } > "$OUT/PAKET_8_EFOR.md"

# ─── PLAN SADAKATİ MERCEKLERİ ⑨-⑫ [D184 · 06.09.2026] ─────────────────
# Dördü de planı EKRANA karşı okur; belgesiz koşuları tanım gereği boştur.
# Sayı MODELE SORULMAZ, VERİLİR: ızgara ve iskelet SPEC'ten pakete gömülür.

# ⑨ KADRAJ — B bloğu (kurulum dizisi · iskelet · küme · dönüş · açı yayı · kafiye)
#            + C'den EŞ KADRAJ ve EKRAN YÖNÜ kayıtları
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den B + C(EŞ KADRAJ · EKRAN YÖNÜ) · MODE D"; echo
  blok B; echo; echo '```'; kayit "^(EŞ KADRAJ|EKRAN YÖNÜ)"; echo '```'; } > "$TMP/9.md"
{ kunye "⑨ KADRAJ" "D" "belge: B (kurgu geometrisi · KURULUM İSKELETİ = PLAN STRING) + C (eş kadraj · ekran yönü). ⛔ KARE ÖNCE, HARF SONRA — SETUP STRING plandan kopyalanmaz";
  enjekte "$SRC/9_KADRAJ_QA_CRITIQUE_PROMPT.md" "^## 📋 SETUP LOCK LIST" "$TMP/9.md" /dev/stdout; } > "$OUT/PAKET_9_KADRAJ.md"

# ⑩ OYUNCULUK — A bloğu (sahne haritası · merkezî seçim · bedel · final)
#               + C'den İNSAN · KASK (yüz erişilebilir mi) · EKRAN YÖNÜ (bakış cetveli)
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den A + C(İNSAN · KASK · EKRAN YÖNÜ) · MODE D"; echo
  blok A; echo; echo '```'; kayit "^(İNSAN|KASK|EKRAN YÖNÜ)"; echo '```'; } > "$TMP/10.md"
{ kunye "⑩ OYUNCULUK" "D" "belge: A (sahne haritası · CENTRAL CHOICE · bedel · final) + C (insan · kask · ekran yönü). ⛔ CÜMLE ÖNCE EKRANDAN; kask kapalıysa yüz kategorisi N/A, 1/10 değil";
  enjekte "$SRC/10_OYUNCULUK_QA_CRITIQUE_PROMPT.md" "^## 📋 BEAT & BODY LOCK LIST" "$TMP/10.md" /dev/stdout; } > "$OUT/PAKET_10_OYUNCULUK.md"

# ⑪ IŞIK — C'den IŞIK TAKVİMİ · ATMOSFER · YAPI ANATOMİSİ · KASK + B'den GRID satırları
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den C(IŞIK · ATMOSFER · YAPI · KASK) + GRID · MODE D"; echo
  echo '```'; kayit "^(IŞIK|ATMOSFER|YAPI ANATOMİSİ|KASK)"; echo
  blok B | grep -A6 -E "^GRID:" ; echo '```'; } > "$TMP/11.md"
{ kunye "⑪ IŞIK" "D" "belge: C (ışık takvimi · atmosfer · yapı anatomisi · kask) + B (ızgara). ⛔ ORTAM YASAYI KOYAR: vakumda pus/bloom/kaldırılmış gölge bulgudur; ilan edilmiş sınırdaki değişim PASS";
  enjekte "$SRC/11_ISIK_QA_CRITIQUE_PROMPT.md" "^## 📋 LIGHT LOCK LIST" "$TMP/11.md" /dev/stdout; } > "$OUT/PAKET_11_ISIK.md"

# ⑫ HOOK — A bloğu (viral ara sahneler · final türü) + B bloğu (hook · kırpma · ekran metni · kafiye · doruk)
#          + KAPAK dosyasından KAPAK ANI satırı
KAPAK_ANI=$(grep -hE "^KAPAK ANI" "$F"/*_KAPAK.md 2>/dev/null | head -1)
{ echo "### ⬇️ OPERATÖR DOLDURDU — $(basename "$SPEC")'den A + B + KAPAK ANI · MODE D"; echo
  blok A; echo; blok B; echo
  echo '```'; echo "${KAPAK_ANI:-KAPAK ANI: ____ (KAPAK dosyasında satır yok — operatör doldurur)}"; echo '```'; } > "$TMP/12.md"
{ kunye "⑫ HOOK" "D" "belge: A (viral ara sahneler · final türü) + B (hook uzunluğu · kırpma · ekran metni · kafiye · doruk) + KAPAK ANI. ⛔ KESME ÖNERMEZ; üç saniye TAHMİN yazar → 08_YAYIN_PERFORMANS_TABLOSU";
  enjekte "$SRC/12_HOOK_QA_CRITIQUE_PROMPT.md" "^## 📋 RETENTION LOCK LIST" "$TMP/12.md" /dev/stdout; } > "$OUT/PAKET_12_HOOK.md"

cat > "$OUT/00_PAKET_README.md" <<EOF
# 📦 QA PAKETİ — $FILM

> Betikten üretildi ($TARIH · \`rubrik_paketle.sh\`). Elle düzenlenmez; SPEC değişince yeniden üretilir.
> Kaynak SPEC: \`${SPEC#$PWD/}\` · aile: $AILE

| dosya | mercek | mod | belge |
|---|---|:--:|---|
| PAKET_1_KARE.md | ① KARE | **D** | $( [ "$AILE" = yatay ] && echo 'A + B + UYARI' || echo 'A' ) |
| PAKET_2_DEVAMLILIK.md | ② DEVAMLILIK | V | yok (tasarım) |
| PAKET_3_SES.md | ③ SES | V | yok (tasarım) |
| PAKET_4_HIKAYE.md | ④ HİKAYE | **D** | $( [ "$AILE" = yatay ] && echo 'A + UYARI' || echo 'B' ) |
| PAKET_5_ARKA_PLAN.md | ⑤ ARKA PLAN | V | yalnız üç kilit [D133] |
| PAKET_6_FIZIK.md | ⑥ FİZİK | **D** | sayısal kilitler |
| PAKET_7_AKSIYON.md | ⑦ AKSİYON | **D** | A + C · risk tetikli |
| PAKET_8_EFOR.md | ⑧ EFOR | **D** | A + C · risk tetikli |
| PAKET_9_KADRAJ.md | ⑨ KADRAJ | **D** | B + C(eş kadraj · ekran yönü) · koşul: KURULUM İSKELETİ var |
| PAKET_10_OYUNCULUK.md | ⑩ OYUNCULUK | **D** | A + C(insan · kask · ekran yönü) · koşul: replik 0 ya da CENTRAL CHOICE var |
| PAKET_11_ISIK.md | ⑪ IŞIK | **D** | C(ışık takvimi · atmosfer · yapı · kask) + ızgara · koşul: IŞIK TAKVİMİ var ya da ≥12 klip |
| PAKET_12_HOOK.md | ⑫ HOOK | **D** | A + B + KAPAK ANI · koşul: film yayınlanacak (kart Y) |

## Koşu
1. Master'ı ÖNCE ölç: \`bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"\` [⑪]
2. Her mercek AYRI ve TEMİZ oturumda [D110]; hepsine AYNI dosya [D75].
   ⛔ ①-④ ZORUNLU. ⑤⑥⑦⑧ risk tetiklidir — filmin risk kartları hangisini
   yazıyorsa o koşulur (00_README "hangi filme hangi mercekler"). Tetiklenmemiş
   merceği koşmamak eksik koşu DEĞİLDİR; tetiklenmişi koşmamak kartı okumamaktır.
   ⑨⑩⑪⑫ PLAN SADAKATİ mercekleridir [D184]: koşulu tablonun son sütununda;
   dördü de SPEC'siz koşulmaz (belgesiz koşu tanım gereği boş).
   ⛔ HAM ZİNCİR çıkan master'a (adım 1 · TESLİM SINIFI) HİÇBİR mercek koşulmaz.
3. Her paketin TAMAMINI yapıştır (künye + rubrik + belge) — yalnız kod bloğu değil.
4. Gelen raporu \`02_HAM_RAPORLAR/\`'a olduğu gibi kaydet, sonra:
   \`python3 $K/RAPOR_KONTROL/rapor_kontrol.py <raporlar> --film $FREL --rapor --olcum-kesme <n> --olcum-sahne <n>\`
   (⑪ ölçüm sayıları adım 1'den gelir; verilmezse kesme yayılımı partiyi toptan düşürür)
   GEÇERSİZ / TEKRAR dönerse T tablosuna satır YAZILMAZ.
EOF

echo "✅ paket üretildi → $OUT/"
ls -1 "$OUT" | sed 's/^/   /'
echo "   aile: $AILE · SPEC: $(basename "$SPEC") · ⑤ kilit satırı: $(printf '%s\n' "$UC" | grep -c .)"
rm -rf "$TMP"
