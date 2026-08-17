#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  SAYAÇ — belgelerdeki sayıları hesaplar, kimse elle yazmasın
# ═══════════════════════════════════════════════════════════════════
#
#  NEDEN VAR:
#  "Kaç ders var" sorusunun cevabı altı belgeye elle kopyalanmıştı ve
#  altısı da farklıydı: 42 · 42 · 42 · 44 · 44 · 45 — gerçek 50'ydi.
#  Bir sayıyı iki yerde tutmak, birini yanlış tutmaktır.
#
#  KULLANIM:
#      bash kilavuzlar_ve_sistem_dosyalari/sayac.sh
#
#  Belgeye sayı yazmadan önce bunu çalıştır. Yazacaksan da tek yere yaz:
#  FILM_QA_RAPORLARI/00_INDEX.md — projedeki tek sayaç orası.
# ═══════════════════════════════════════════════════════════════════

cd "$(dirname "$0")/.." || exit 1
K="kilavuzlar_ve_sistem_dosyalari"
Q="$K/FILM_QA_RAPORLARI"

echo "═══════════════════════════════════════════════════════"
echo "  SAYAÇ · $(date '+%d.%m.%Y %H:%M')"
echo "═══════════════════════════════════════════════════════"
echo

# ─── DERSLER ───────────────────────────────────────────────────────
# 07.08.2026: dersler LESSONS_LEARNED.md'den DERSLER/ klasörüne bölündü.
# Numaralar dosyalar arasına tematik dağıldığı için TÜM klasör taranır.
DERS=$(cat "$K/DERSLER/"*.md | grep -oE "^## .{0,4} DERS [0-9]+" \
       | grep -oE "[0-9]+" | sort -n | uniq | wc -l | tr -d ' ')
SON=$(cat "$K/DERSLER/"*.md | grep -oE "^## .{0,4} DERS [0-9]+" \
       | grep -oE "[0-9]+" | sort -n | tail -1)

echo "📚 DERSLER"
printf "   benzersiz ders    %s\n" "$DERS"
printf "   en yüksek numara  %s" "$SON"
[ "$DERS" = "$SON" ] && echo "   ✅ boşluk yok" || echo "   🚨 BOŞLUK VAR — numaralar atlanmış"
echo

# ─── FİLMLER ───────────────────────────────────────────────────────
echo "🎬 FİLMLER"
TOPLAM=0
for d in dikey_shorts_filmler yatay_2_4_dk_filmler_uzay yatay_3_5_dk_filmler \
         yatay_7_9_dk_filmler yatay_10_20_dk_filmler; do
    [ -d "$d" ] || continue
    n=$(ls -1 "$d" 2>/dev/null | grep -viE "^[0-9_]*README" | grep -v "^kilavuzlar$" | wc -l | tr -d ' ')
    printf "   %-30s %s\n" "$d" "$n"
    TOPLAM=$((TOPLAM + n))
done
printf "   %-30s %s\n" "TOPLAM" "$TOPLAM"
echo

# ─── 00_INDEX KARŞILAŞTIRMASI ──────────────────────────────────────
# Kural ①: sayı tek yerde durur (00_INDEX). Ama 11.08'de INDEX "hizalandı"
# notuyla bayat sayı taşıdı — tarih değil mekanizma: betik artık karşılaştırır.
IDX=$(grep -oE "TOPLAM FİLM +[0-9]+" "$Q/00_INDEX.md" 2>/dev/null \
      | grep -oE "[0-9]+" | head -1)
if [ "$IDX" = "$TOPLAM" ]; then
    printf "   ✅ 00_INDEX ile tutarlı (INDEX de %s diyor)\n" "$IDX"
else
    printf "   ❌ 00_INDEX TUTMUYOR — INDEX %s diyor, dosya sistemi %s sayıyor.\n" "${IDX:-?}" "$TOPLAM"
    printf "      00_INDEX.md SAYIM bloğunu güncelle.\n"
fi
echo

# ─── ÖLÇÜM DURUMU ──────────────────────────────────────────────────
# Kaynak: skor tabloları. Bir film ancak tablosunda satırı varsa ölçülmüştür.
# tablo_say: dosyadaki İLK markdown tablosunun VERİ satırlarını sayar
# (başlık + ayraç düşülür; kalın/üstü çizili/Ⓥ işaretli satırlar dahildir —
#  eski regex "The" ile başlamayan ve **kalın** satırları kaçırıyordu).
# $2 verilirse tablo o başlıktan SONRA aranır.
tablo_say() {
    local f="$1" b="${2:-}"
    { if [ -n "$b" ]; then sed -n "/$b/,\$p" "$f"; else cat "$f"; fi; } 2>/dev/null \
      | awk '/^\|/{n++; if(n>2)c++; next} n>0{exit} END{print c+0}'
}

VQ=$(tablo_say "$K/LESSONS_LEARNED.md" "KALİTE TAKİP TABLOSU")
SQ=$(tablo_say "$Q/03_HIKAYE_KALITE_TABLOSU.md")
MQ=$(tablo_say "$Q/04_MANTIK_KALITE_TABLOSU.md")
SHQ=$(tablo_say "$Q/05_SHORTS_KALITE_TABLOSU.md")
KQ=$(tablo_say "$Q/06_KARAKTER_KALITE_TABLOSU.md")
SESQ=$(tablo_say "$Q/07_SES_KALITE_TABLOSU.md")
KAYIT=$(ls -1 "$Q/01_FILM_RAPORLARI/" 2>/dev/null | wc -l | tr -d ' ')
HAM=$(ls -1 "$Q/02_HAM_RAPORLAR/" 2>/dev/null | grep -v README | wc -l | tr -d ' ')

echo "🔍 ÖLÇÜM DURUMU  (satır = koşu; aynı film iki kez ölçülmüş olabilir)"
printf "   VIDEO_QA    (LESSONS tablosu)  %s satır\n" "$VQ"
printf "   SENARYO_QA  (03 tablosu)       %s satır\n" "$SQ"
printf "   MANTIK_QA   (04 tablosu)       %s satır\n" "$MQ"
printf "   SHORTS_QA   (05 tablosu)       %s satır\n" "$SHQ"
printf "   KARAKTER_QA (06 tablosu)       %s satır\n" "$KQ"
printf "   SES_QA      (07 tablosu)       %s satır\n" "$SESQ"
echo
printf "   film kaydı (01/)             %s\n" "$KAYIT"
printf "   ham rapor  (02/)             %s\n" "$HAM"
echo
printf "   ÖLÇÜLMEMİŞ FİLM              %s / %s\n" "$((TOPLAM - KAYIT))" "$TOPLAM"
echo

# ─── KILAVUZ HACMİ ─────────────────────────────────────────────────
echo "📄 BELGE HACMİ"
printf "   kök .md dosya                %s\n" "$(ls -1 $K/*.md | wc -l | tr -d ' ')"
printf "   kök toplam satır             %s\n" "$(cat $K/*.md | wc -l | tr -d ' ')"
printf "   en büyük dosya               %s\n" "$(wc -l $K/*.md | sort -rn | sed -n 2p | awk '{print $2" ("$1" satır)"}' | xargs basename 2>/dev/null || echo '-')"
echo

# ─── BAYAT SAYI TARAMASI ───────────────────────────────────────────
echo "🚨 BELGELERDE SABİT SAYI ARAMASI"
echo "   (aşağıdakiler elle yazılmış — bu betikle uyuşuyor mu kontrol et)"
echo
# Tarih taşıyan satırlar (değişiklik kaydı) ATLANIR — onlar o günün
# durumunu kaydeder ve güncellenmemelidir.
grep -rnE "[0-9]{2} (ders|dersin|lesson)" --include="*.md" "$K" 2>/dev/null \
  | grep -v "02_HAM_RAPORLAR" \
  | grep -vE "SAYI YAZMA KURALI|sayac.sh" \
  | grep -vE "[0-9]{2}\.[0-9]{2}\.[0-9]{4}" \
  | grep -vE "O tarihte|o tarihe|kadarki|sonrasında" \
  | grep -vE "\+[0-9]+ ders" \
  | grep -vE "'ye çıkar|’ye çıkar|ye çıkarıp" \
  | sed 's|.*kilavuzlar_ve_sistem_dosyalari/||' \
  | while IFS= read -r line; do
        num=$(echo "$line" | grep -oE "[0-9]{2} (ders|dersin|lesson)" | grep -oE "^[0-9]+" | head -1)
        if [ "$num" != "$DERS" ]; then echo "   ❌ $line"; else echo "   ✅ $line"; fi
    done
echo
echo "═══════════════════════════════════════════════════════"
echo "  ❌ işaretli her satır güncellenmeli veya kaynağa"
echo "  işaret eden bir ifadeyle değiştirilmeli."
echo "═══════════════════════════════════════════════════════"
