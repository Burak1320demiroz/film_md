#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  OKUMA ÇİZELGESİ — "tüm dersleri ve tüm kılavuzları oku" cümlesini
#  SAYILABİLİR bir deftere çevirir
# ═══════════════════════════════════════════════════════════════════
#
#  NEDEN VAR (08.09.2026 · sahip kararı):
#  "Okuma listeni çıkar ve o listedeki kılavuzları gerçekten aç" cümlesi
#  davranış değiştirmedi. THE OPEN CIRCUIT'in 07.09.2026 tam denetimi bunu
#  ölçtü: zorunlu okuma listesinin DÖRDÜ hiç açılmamıştı (UZAY_USSU ·
#  SAHNE_ZINCIRI · ACILIS_KAPANIS · ASTRONOT_DONANIM) ve sekiz bulgunun
#  hepsi o dört dosyadan çıktı — biri filmin üssünü kadraja fiziksel olarak
#  alamayan bir lens seçimiydi. Cümle değil, DEFTER kapatır.
#
#  Elle tutulan liste bayatlar (kural ①: sayı elle yazılmaz) — bu yüzden
#  çizelge dosya sisteminden ÜRETİLİR. Yeni bir kılavuz eklendiğinde bir
#  sonraki filmin çizelgesinde kendiliğinden ⬜ olarak belirir.
#
#  ⭐ 14.09.2026 · REFORM FAZ 8 (sahip kararı · TODO_AKIS_VE_DERS_REFORMU.md):
#  "hepsi" çizelgesi ölçüldü ve sahteydi — THE_LOCKED_PULSE 126 dosya / ~42.000
#  satır, 126/126 satırdan "kilit" çıkmış, "—" SIFIR; film 747 KB, üretim 0 kare.
#  Çizelge küçüldü, sahtelik kapısı geldi (prompt_kontrol.py ㉘):
#     TUR 1  DERSLER/00_YASAYAN_DERSLER.md tablosu — ders başına bir satır (≤ 40),
#            ETİKET görünür; etiket filme uymuyorsa "—" yazılır (meşru)
#     TUR 2/3 FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt manifesti —
#            [dikey]/[faz] satırları klasör yolundan süzülür; [kask]/[replik]/
#            [iki-insan]/[referans] görünür, uymayanı "—"
#     TUR 4/5 aynen. Manifest dışı kılavuzlar HAVUZ (§1 tablosu) — "havuzdan
#            açıldı" satırı olarak elle eklenebilir (tek istisna).
#  Eski klasörlerin çizelgesine dokunulmaz (işaretli çizelge ezilmez).
#
#  KULLANIM:
#      bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü> [--force]
#  ÇIKTI:
#      <film klasörü>/00_ANALIZ/00_OKUMA_CIZELGESI.md
#
#  ⛔ İşaretlenmiş çizelgenin üstüne yazmaz; ilerlemeyi ezmek için --force.
# ═══════════════════════════════════════════════════════════════════
set -u

F="${1:-}"; ZORLA="${2:-}"
[ -z "$F" ] && { echo "KULLANIM: okuma_cizelgesi.sh <film klasörü> [--force]"; exit 2; }
[ -d "$F" ] || { echo "⛔ klasör yok: $F"; exit 2; }
F="$(cd "${F%/}" && pwd)"
FILM="$(basename "$F")"
cd "$(dirname "$0")/.." || exit 1
K="kilavuzlar_ve_sistem_dosyalari"
Q="$K/FILM_QA_RAPORLARI"
OUT="$F/00_ANALIZ/00_OKUMA_CIZELGESI.md"

mkdir -p "$F/00_ANALIZ"
if [ -f "$OUT" ] && grep -q "✅" "$OUT" && [ "$ZORLA" != "--force" ]; then
  echo "⛔ $OUT işaretli satır taşıyor — ezilmedi."
  echo "   İlerlemeyi sıfırlamak istiyorsan: --force"
  exit 2
fi

TOPLAM_D=0; TOPLAM_S=0

satir() {   # satir <dosya> <kök-göreli-etiket>
  local f="$1" ad="$2" n
  [ -f "$f" ] || return 0
  n=$(wc -l < "$f" | tr -d ' ')
  TOPLAM_D=$((TOPLAM_D + 1)); TOPLAM_S=$((TOPLAM_S + n))
  printf '| ⬜ | `%s` | %s |  |\n' "$ad" "$n" >> "$OUT"
}

baslik() { printf '\n### %s\n\n| ⬜/✅ | dosya | satır | bu filme düşen kilit |\n|:--:|---|--:|---|\n' "$1" >> "$OUT"; }

{
printf '# 📖 %s — OKUMA ÇİZELGESİ\n\n' "$FILM"
printf '> Üretildi: `bash %s/okuma_cizelgesi.sh <film klasörü>` · %s\n' "$K" "$(date '+%d.%m.%Y %H:%M')"
printf '> ⛔ **ELLE SATIR EKLENMEZ/SİLİNMEZ** — yeni kılavuz eklenirse betik yeniden koşulur.\n'
printf '>\n'
printf '> **Kural:** her satır okununca `⬜` → `✅` yapılır ve son sütuna\n'
printf '> **bu filme düşen kilit** yazılır. Kilit çıkmadıysa `—` yazılır; boş\n'
printf '> bırakılmaz — boş hücre "okudum" ile "atladım" arasını ayırt ettirmez.\n'
printf '>\n'
printf '> ⭐ Son sütunda yazılan her kilit `01_QA_DERS_HASADI.md` tablosuna taşınır.\n'
printf '> ⛔ ⬜ kalan satır varken `02_KONSEPT_VE_RISK.md` yazılmaz.\n'
printf '> ⛔ 14.09.2026: her satırdan kilit ÇIKMAZ. "—" yazmak meşrudur; sıfır "—"\n'
printf '> çizelgeyi sahte yapar (`prompt_kontrol.py` ㉘ · LOCKED_PULSE 126/126 ölçümü).\n'
} > "$OUT"

# ── TUR 1 · YAŞAYAN DERSLER (≤ 40) ─────────────────────────────────────
YAS="$K/DERSLER/00_YASAYAN_DERSLER.md"
[ -f "$YAS" ] || { echo "⛔ yaşayan liste yok: $YAS"; exit 2; }
{
printf '\n### TUR 1 · YAŞAYAN DERSLER — `DERSLER/00_YASAYAN_DERSLER.md` (14.09.2026)\n\n'
printf '> Film dersi havuzu bu listedir; ders metni ETİKET filme uyuyorsa açılır. ETİKET\n'
printf '> uymuyorsa (`kask` etiketli ders kasksız filmde) satır **"—"** ile geçilir — bu\n'
printf '> "okumadım" değil "bu filme düşmüyor" demektir ve ㉘ kapısı tam bunu bekler.\n\n'
printf '| ⬜/✅ | ders | ETİKET | bu filme düşen kilit |\n|:--:|---|---|---|\n'
printf '| ⬜ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi |  |\n'
printf '| ⬜ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi |  |\n'
} >> "$OUT"
TOPLAM_D=$((TOPLAM_D + 2))
TOPLAM_S=$((TOPLAM_S + $(wc -l < "$YAS" | tr -d ' ')))
DERS_N=0
while IFS='|' read -r _ d bsl etiket _degisen dosya _; do
  d="$(echo "$d" | tr -d ' ')"; case "$d" in ''|*[!0-9]*) continue;; esac
  bsl="$(echo "$bsl" | sed -e 's/^ *//' -e 's/ *$//')"
  etiket="$(echo "$etiket" | sed -e 's/^ *//' -e 's/ *$//')"
  dosya="$(echo "$dosya" | tr -d ' ')"
  yol="$(ls "$K"/DERSLER/${dosya}_*.md 2>/dev/null | head -1)"
  [ -n "$yol" ] && yol="${yol#$K/}" || yol="DERSLER/${dosya}_*.md"
  printf '| ⬜ | D%s · %s · `%s` | %s |  |\n' "$d" "$bsl" "$yol" "$etiket" >> "$OUT"
  DERS_N=$((DERS_N + 1))
done < "$YAS"

# ── TUR 2/3 · MANİFEST (OKUMA_CEKIRDEGI.txt) ───────────────────────────
MAN="$K/FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt"
[ -f "$MAN" ] || { echo "⛔ manifest yok: $MAN"; exit 2; }
case "$F" in *dikey*) DIKEY=1 ;; *) DIKEY=0 ;; esac
case "$F" in *10_20*) FAZ=1 ;; *) FAZ=0 ;; esac
{
printf '\n### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti\n\n'
printf '> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır\n'
printf '> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.\n'
printf '> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre\n'
printf '> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla\n'
printf '> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.\n\n'
printf '| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |\n|:--:|---|--:|---|---|\n'
} >> "$OUT"
MAN_N=0
while IFS='|' read -r yol etiket not; do
  yol="$(echo "$yol" | tr -d ' ')"; [ -z "$yol" ] && continue; case "$yol" in \#*) continue;; esac
  etiket="$(echo "$etiket" | tr -d ' ')"; not="$(echo "$not" | sed -e 's/^ *//' -e 's/ *$//')"
  case "$etiket" in
    *dikey*) [ "$DIKEY" -eq 1 ] || continue ;;
    *faz*)   [ "$FAZ" -eq 1 ]   || continue ;;
  esac
  f="$K/$yol"; [ -f "$f" ] || { printf '| ⬜ | `%s` | ⛔ YOK | %s | manifest hatası |\n' "$yol" "$not" >> "$OUT"; continue; }
  n=$(wc -l < "$f" | tr -d ' ')
  [ "$etiket" = "-" ] && et="" || et="**$etiket** · "
  printf '| ⬜ | `%s` | %s | %s%s |  |\n' "$yol" "$n" "$et" "$not" >> "$OUT"
  TOPLAM_D=$((TOPLAM_D + 1)); TOPLAM_S=$((TOPLAM_S + n)); MAN_N=$((MAN_N + 1))
done < "$MAN"

baslik "TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı"
satir "$Q/00_INDEX.md"               "FILM_QA_RAPORLARI/00_INDEX.md"
satir "$Q/09_URETIM_RED_DEFTERI.md"  "FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md"
for f in "$Q"/0[3-8]_*.md; do satir "$f" "FILM_QA_RAPORLARI/$(basename "$f")"; done
for f in "$Q"/T*.md;        do satir "$f" "FILM_QA_RAPORLARI/$(basename "$f")"; done

RAPOR_N=$(ls -1 "$Q/01_FILM_RAPORLARI"/*.md 2>/dev/null | wc -l | tr -d ' ')
RAPOR_S=$(cat "$Q/01_FILM_RAPORLARI"/*.md 2>/dev/null | wc -l | tr -d ' ')
{
printf '\n### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (%s dosya · %s satır)\n\n' "$RAPOR_N" "$RAPOR_S"
printf '> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun\n'
printf '> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER\n'
printf '> filmlerde tekrar eder. En az **beş** kayıt açılır:\n'
printf '> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film\n'
printf '> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt\n'
printf '> ⑤ bu filmin konseptine en yakın kayıt.\n\n'
printf '| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |\n|:--:|---|---|---|\n'
printf '| ⬜ |  | ① aynı format |  |\n'
printf '| ⬜ |  | ② aynı ortam kartı |  |\n'
printf '| ⬜ |  | ③ aynı tema |  |\n'
printf '| ⬜ |  | ④ en düşük skor |  |\n'
printf '| ⬜ |  | ⑤ en yakın konsept |  |\n'
printf '\nTam liste: `ls %s/01_FILM_RAPORLARI/`\n' "$Q"
} >> "$OUT"

{
printf '\n---\n\n## 📊 ÇİZELGE ÖZETİ\n\n```\n'
printf 'YAŞAYAN DERS:    %s  (TUR 1 · tavan 40)\n' "$DERS_N"
printf 'MANİFEST DOSYA:  %s  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)\n' "$MAN_N"
printf 'ZORUNLU DOSYA:   %s\n' "$TOPLAM_D"
printf 'ZORUNLU SATIR:   %s\n' "$TOPLAM_S"
printf 'SEÇMELİ KAYIT:   5 / %s  (TUR 5)\n' "$RAPOR_N"
printf '```\n\n'
printf '⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /\n'
printf '~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit\n'
printf 'çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse\n'
printf 'çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).\n\n'
printf '⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan\n'
printf 'devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.\n'
} >> "$OUT"

echo "✅ ÇİZELGE: $OUT"
echo "   $DERS_N yaşayan ders · $MAN_N manifest dosyası · $TOPLAM_D zorunlu dosya / $TOPLAM_S satır · + 5 seçmeli film kaydı ($RAPOR_N içinden)"
