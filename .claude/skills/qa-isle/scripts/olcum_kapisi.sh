#!/bin/bash
# ÖLÇÜM KAPISI ⑪ — AGENTS.md ortak adım ⑪'in komutları, tek koşuda.
# Kullanım: olcum_kapisi.sh <master_video> [rms]
# Çıktıdaki sayılar kapıların (④ ⑤ ⑦ ⑨) tek kaynağıdır; raporun sayıları değil.
set -u

M="${1:-}"
if [ -z "$M" ]; then
  echo "KULLANIM: olcum_kapisi.sh <master_video> [rms]"
  exit 2
fi
if [ ! -f "$M" ]; then
  echo "HATA: dosya bulunamadı: $M"
  exit 2
fi
command -v ffprobe >/dev/null 2>&1 || { echo "HATA: ffprobe yok"; exit 3; }
command -v ffmpeg  >/dev/null 2>&1 || { echo "HATA: ffmpeg yok"; exit 3; }

echo "== DOSYA =="
echo "$M"

echo "== SÜRE / ÇÖZÜNÜRLÜK / FPS =="
ffprobe -v error \
  -show_entries format=duration \
  -show_entries stream=codec_type,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 "$M"

echo "== SES KANALI (boşsa YOKTUR — D136) =="
AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$M")
if [ -z "$AUDIO" ]; then
  echo "SES KANALI: YOK"
else
  echo "SES KANALI: VAR"
fi

echo "== KESME IZGARASI (scene>0.3 · pts_time saniyeleri) =="
ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 \
  | grep -oE "pts_time:[0-9.]+" || echo "(kesme tespit edilmedi)"

echo "== SESSİZLİK (silencedetect -50dB / 0.3s) =="
if [ -n "$AUDIO" ]; then
  ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 \
    | grep silence_ || echo "(sessizlik aralığı yok)"
else
  echo "(ses kanalı yok — atlandı)"
fi

echo "== LOUDNESS (ebur128 · ihraç kilidi −14 LUFS / −1,0 dBTP — KURGU_RITMI §6) =="
if [ -n "$AUDIO" ]; then
  ffmpeg -hide_banner -nostats -i "$M" -af ebur128=peak=true -f null - 2>&1 \
    | grep -E "^\s+(I:|Peak:)" || echo "(ölçülemedi)"
else
  echo "(ses kanalı yok — atlandı)"
fi

echo "== KÖŞE TESTİ (filigran — D150 · DÖRT ÇEYREK · 25 s'de bir) =="
# ⚠️ 01.09.2026 KALİBRASYONU: ilk sürüm sabit 360×240 köşe kırpıyordu ve THE COLD
#    WELD'in filigranını KAÇIRDI — ikon köşeden ~300 px içerideydi (4K'da y≈1800,
#    crop y≥1920). Sabit piksel kutusu çözünürlüğe de bağlıydı. Artık ÇEYREK
#    kırpılır (ölçekten bağımsız) ve DÖRT köşe birden basılır: filigran hangi
#    köşede olursa olsun görünür.
for q in "SA:iw*3/4:ih*3/4" "SU:iw*3/4:0" "SoA:0:ih*3/4" "SoU:0:0"; do
  ad="${q%%:*}"; xy="${q#*:}"; X="${xy%%:*}"; Y="${xy##*:}"
  KOSE="${KOSE_DIR:-.}/kose_${ad}.png"
  ffmpeg -hide_banner -loglevel error -y -i "$M" \
    -vf "crop=iw/4:ih/4:${X}:${Y},fps=1/25,scale=320:-1,tile=6x1" -frames:v 1 -vsync 0 "$KOSE" 2>/dev/null \
    && echo "  BAKILACAK: $KOSE" || echo "  ($ad şeridi üretilemedi)"
done
echo "  ⛔ Altı örneğin ALTISINDA aynı yerde aynı şekil duruyorsa FİLİGRAN VAR → 🔴 teslim kusuru [D150]:"
echo "     filigranlı master master değildir; yeniden ihraç edilir ve mercekler onu ölçmemiş sayılır."

echo "== SAHNE IZGARASI (D163 · kesme listesinden TÜRETİLİR · sahne ortası kareleri) =="
# 01.09.2026: ④c İNSAN ŞERİDİ tek-figürlü filmde SABİTTİR (-1111…) ve içerik
# sırasını hiç ölçmez; THE COLD WELD'de dört sahnelik bir BLOK TAKASI (anahtar
# bloğu ↔ duvar bloğu) şeridi bozmadan geçti. Bu şerit her sahnenin ORTASINDAN
# birer kare basar; operatör onu SPEC B bloğunun sahne haritasıyla YAN YANA
# koyar. Sayı değil GÖRÜNTÜ karşılaştırması — kapı budur.
CUTS=$(ffmpeg -i "$M" -filter:v "select='gt(scene,0.15)',showinfo" -f null - 2>&1 \
       | grep -oE "pts_time:[0-9.]+" | sed 's/pts_time://' | sort -n | uniq)
SURE=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M" 2>/dev/null | cut -d. -f1)
SURE=${SURE:-0}
IZG="${KOSE_DIR:-.}/sahne_izgarasi.jpg"
if [ -n "$CUTS" ] && [ "$SURE" -gt 0 ]; then
  # ⚠️ select+tile TOLERANSLA çalışır ve 30 fps'de kimi sahneden İKİ kare alır
  #    (ilk sürüm 15 sahneyi 16 kare gösterdi). Her sahne ortası AYRI -ss ile
  #    çıkarılır: bire bir, sırası garanti.
  TD=$(mktemp -d); n=0
  MIDS=$(printf '0\n%s\n%s\n' "$CUTS" "$SURE" | sort -n | uniq \
         | awk 'NR>1{ if ($1-p > 1.5) printf "%.2f\n", (p+$1)/2 } {p=$1}')
  for m in $MIDS; do
    n=$((n+1))
    ffmpeg -hide_banner -loglevel error -y -ss "$m" -i "$M" -frames:v 1 \
      -vf scale=420:-1 "$TD/$(printf '%03d' $n).jpg" 2>/dev/null
  done
  COLS=4; ROWS=$(( (n + COLS - 1) / COLS )); [ "$ROWS" -lt 1 ] && ROWS=1
  ffmpeg -hide_banner -loglevel error -y -pattern_type glob -i "$TD/*.jpg" \
    -vf "tile=${COLS}x${ROWS}" -frames:v 1 "$IZG" 2>/dev/null \
    && echo "  BAKILACAK: $IZG  ($n sahne · ${COLS}x${ROWS} · soldan sağa, üstten alta)" \
    || echo "  (ızgara üretilemedi)"
  echo "  sahne ortaları: $(echo $MIDS | tr '\n' ' ')"
  echo "  ⛔ SPEC B bloğunun sahne haritasıyla YAN YANA oku: kare n, planın n. sahnesi mi?"
  echo "     Şerit sabitse (tek figürlü film) sıra ekseni YALNIZ buradan ölçülür [D163]."
  rm -rf "$TD"
else
  echo "  (kesme listesi ya da süre okunamadı — ızgara atlandı)"
fi

echo "== KUYRUK / BAŞ KART ŞÜPHESİ (freezedetect −60dB / 1,5 s · son kare — D70/D72 · 9 vaka) =="
# 01.09.2026: "kart ekleme" cümlesi dokuz teslimde tutmadı; kapı ARACA indi.
# Grenli film karesi -60dB'de donmuş sayılmaz; siyah üstüne yazı kartı donar.
# Kuyruk penceresi son 12 s, baş penceresi ilk 3 s. Şüphe kareyle kapanır.
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$M" 2>/dev/null | cut -d. -f1)
DUR=${DUR:-0}
FRZ=$(ffmpeg -hide_banner -nostats -i "$M" -vf "freezedetect=n=-60dB:d=1.5" -an -f null - 2>&1 \
      | grep -oE "freeze_(start|end): [0-9.]+" | awk '{print $2}')
if [ -z "$FRZ" ]; then
  echo "(donmuş kare aralığı yok — grenli/hareketli gövde; yine de son kareye BAK)"
else
  echo "$FRZ" | awk -v D="$DUR" 'NR%2==1{s=$1} NR%2==0{e=$1;
      tag="";
      if (e+0 > D-12) tag=tag " 🔴 KUYRUK KART ŞÜPHESİ";
      if (s+0 < 3)    tag=tag " 🔴 BAŞ KART ŞÜPHESİ";
      printf "donmuş: %.1f-%.1f s (%.1f s)%s\n", s, e, e-s, tag }'
  # tek başına kalan start (dosya sonuna kadar donmuş) → kuyruk
  n=$(echo "$FRZ" | wc -l | tr -d ' ')
  if [ $((n % 2)) -eq 1 ]; then
    s=$(echo "$FRZ" | tail -1); echo "donmuş: ${s}-SON s  🔴 KUYRUK KART ŞÜPHESİ (dosya sonuna kadar)"
  fi
fi
SONK="${KOSE_DIR:-.}/son_kare.jpg"
if [ "$DUR" -gt 1 ]; then
  ffmpeg -hide_banner -loglevel error -y -ss $((DUR-1)) -i "$M" -frames:v 1 "$SONK" \
    && echo "BAKILACAK: $SONK — kadrajda YAZI/kart varsa 🔴 D70/D72 (ekran metni 0,0 s); kartı kes, ⑪'i yeniden koş" \
    || echo "(son kare üretilemedi)"
fi

echo "== NOT: karanlık filmde scene>0.3 kesme görmez; ızgarayı silencedetect deliklerinden ve kart başından oku (10 s katı = ızgara) =="

if [ "${2:-}" = "rms" ] && [ -n "$AUDIO" ]; then
  echo "== SANİYELİK RMS =="
  ffmpeg -i "$M" -af "aresample=8000,asetnsamples=8000,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" \
    -f null - 2>/dev/null
fi

echo "== ÖLÇÜM BİTTİ =="
