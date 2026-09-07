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
# 23.08.2026: zombi klasörü yeniden açıldı (görev kartı H) — 12.08'de
# silinmişti.
# 04.09.2026: yatay_7_9_dk_filmler kaldırıldı (görev kartı H2, sahip kararı).
# Klasör DÖRT listeden birden çıktı (film sayımı · tema dağılımı · SPEC borcu
# · ⑯ politika taraması); zombi turunda üçtü, bu betik o gün büyümüş.
# ⚠️ TOPLAM DEĞİŞMEDİ ve değişmemeliydi: tek filmi THE_SLOW_STONE silinmedi,
#    yatay_10_20_dk_filmler'e taşındı (bandı 7 dk'ya açıldı, §2.5). Sayının
#    düşmesi taşımanın kaçtığı anlamına gelirdi.
# 26.08.2026: zombi klasörü TEKRAR kaldırıldı (görev kartı H2) ve bu kez
# tür de kapandı — depo yalnız UZAY filmlerine indirildi. Klasör üç ayrı
# listeden birden çıkarıldı (film sayımı · tema dağılımı · SPEC borcu);
# biri atlansaydı sayaç olmayan bir klasörü sayacaktı.
# 25.08.2026: ARTIK HER FORMAT KLASÖRLÜ — dikey/uzay/zombi de tek dosyadan
# film klasörüne geçti, yani bir satır = bir film klasörü. <FILM>_QA_SPEC.md
# artık filmin klasörünün İÇİNDE durur ve zaten sayıma girmez; aşağıdaki
# _QA_SPEC süzgeci geriye dönük emniyet olarak duruyor (tek dosya kalırsa).
for d in dikey_shorts_filmler yatay_2_4_dk_filmler_uzay \
         yatay_3_5_dk_filmler yatay_10_20_dk_filmler; do
    [ -d "$d" ] || continue
    n=$(ls -1 "$d" 2>/dev/null | grep -viE "^[0-9_]*README" | grep -v "^kilavuzlar$" \
        | grep -viE "_QA_SPEC\.md$" | wc -l | tr -d ' ')
    printf "   %-30s %s\n" "$d" "$n"
    TOPLAM=$((TOPLAM + n))
done
printf "   %-30s %s\n" "TOPLAM" "$TOPLAM"
echo

# ─── TEMA DAĞILIMI ─────────────────────────────────────────────────
# 26.08.2026'da açıldı. Sebep: tema TEMA_MUHENDISLIGI §3'te sekiz başlıkla
# tanımlı, §5 matrisi temayı sahneye bağlıyor — ama hangi temanın kaç kez
# kullanıldığı hiçbir yerde sayılmıyordu. Sonuç: yazılı temaların beşi aynı
# TAKAS kalıbının varyasyonu çıktı ve kimse fark etmedi (§3c moratoryumu).
# Elle tablo TUTULMAZ (kural ①) — dağılım dosya sisteminden okunur.
#
# ⚠️ Desen dar tutuldu. Gevşek desen dört şeyi tema sandı: "TEMAS:" (dokunma),
#    "TEMA → MOTİF ① FIRÇA:" (matris başlığı), "Tema sayacın içinde:" (düz
#    cümle) ve "**Tema:**" (MÜZİK teması). TEMA'dan sonra HARF gelemez.
echo "🎭 TEMA DAĞILIMI"
TEMA_P="^[[:space:]>*_#-]*\**[[:space:]]*(TEMA|THEME)([[:space:]]+[[:alpha:]][[:alpha:] ]{0,17}|[[:space:]]*\([[:alpha:] ]{1,18}\))?[[:space:]]*:"
FILM_DIZIN="dikey_shorts_filmler yatay_2_4_dk_filmler_uzay \
            yatay_3_5_dk_filmler yatay_10_20_dk_filmler"
TEMALI=0
for d in $FILM_DIZIN; do
    [ -d "$d" ] || continue
    for f in "$d"/*/; do
        [ -d "$f" ] || continue
        grep -rqE "$TEMA_P" --include="*.md" "$f" 2>/dev/null && TEMALI=$((TEMALI + 1))
    done
done
printf "   tema beyanı olan film klasörü   %s / %s\n" "$TEMALI" "$TOPLAM"
echo "   ── tek kelimelik etiketler ──"
grep -rhE "$TEMA_P" --include="*.md" $FILM_DIZIN 2>/dev/null \
  | sed -E 's/^[^:]*:[[:space:]]*//' \
  | sed -E 's/[[:space:]]*\(.*//; s/[[:space:]]+$//' \
  | grep -vE '^$' | grep -vE ' ' \
  | sort | uniq -c | sort -rn \
  | while read -r n t; do
        # §3'ün sekizlisi — İngilizce karşılıklar da sayılır (QA_SPEC
        # dosyaları THEME alanını İngilizce yazıyor, aynı temadır).
        case " YALNIZLIK FEDAKÂRLIK ZAMAN KİMLİK İNSAN-MAKİNE İLK-TEMAS ENTROPİ UMUT \
LONELINESS SACRIFICE TIME IDENTITY HUMAN-MACHINE FIRST-CONTACT ENTROPY HOPE " in
            *" $t "*) isaret="✅" ;;
            *)        isaret="⏸️ §3'te yok" ;;
        esac
        printf "   %-22s %-4s %s\n" "$t" "$n" "$isaret"
    done
echo "   (⏸️ = depoda doğmuş aday etiket — TEMA_MUHENDISLIGI §3b dürüst kaydı)"
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
# ⚠️ 25.08.2026 — BU BÖLÜM BAŞTAN YAZILDI. Sebebi dosyanın kendi varlık
# sebebinin burada tekrarlanmış olmasıdır:
#
#   Betiğin bir önceki değişikliği 17.08'di. QA mimarisi 22.08'de değişti —
#   altı mercek dörde indi, altı skor tablosu ⛔ KAPALI ilan edildi, yerlerine
#   T1-T6 açıldı. Betik güncellenmedi. Yani beş gün önceki dünyayı raporluyor,
#   ekrana "VIDEO_QA 23 · SENARYO 16 · MANTIK 18 ..." basıyor ve bu altı
#   tablonun ALTISI DA KAPALI. Canlı sistemin gerçek sayısı — bir — hiçbir
#   yerde görünmüyordu. AGENTS.md §0 bu betiği her görevin İLK adımı, §7 de
#   SON adımı yapıyor; yani her işin hem girişinde hem çıkışında ölü sistem
#   raporlanıyordu.
#
# KURAL: ÖLÇÜM DURUMU yalnız CANLI tabloları okur. Kapalı tablolar aşağıda
# ARŞİV başlığı altında, "bu bir durum göstergesi değildir" diyerek durur.
#
# tablo_satir: dosyadaki İLK markdown tablosunun VERİ satırlarını basar.
# Başlık + ayraç düşer; kalın/üstü çizili/Ⓥ işaretli satırlar dahildir.
# ⚠️ 25.08.2026 — TABLO İÇİNDEKİ BOŞ SATIR TABLOYU BÖLMEZ. Eski kod ilk
# boş satırda duruyordu ve T1-T6'da ayraç ile ilk veri satırı ARASINDA boş
# satır olduğu için altı tablonun altısını da "0 satır" sayıyordu — üstelik
# aynı ekranda film sayısı 1 yazarken. Sayaç kendi içinde çelişiyordu.
# $2 verilirse tablo o başlıktan SONRA aranır.
tablo_satir() {
    local f="$1" b="${2:-}"
    { if [ -n "$b" ]; then sed -n "/$b/,\$p" "$f"; else cat "$f"; fi; } 2>/dev/null \
      | awk '/^\|/{n++; if(n>2)print; next}
             /^[[:space:]]*$/{next}
             n>0{exit}'
}

tablo_say() { tablo_satir "$@" | grep -c . ; }

# tablo_cizili: üstü çizili (skoru geçersiz sayılmış) satır kaç tane
tablo_cizili() { tablo_satir "$@" | grep -c '~~' ; }

# tablo_filmler: skor tablosunun VERİ satırlarındaki film ADLARINI basar.
# Ad ilk hücrede **kalın** yazılır. ~~Üstü çizili~~ satır da bir ÖLÇÜMDÜR
# (skoru geçersiz sayılmıştır ama film ölçülmüştür) — o yüzden sayılır.
# "Kaç satır" değil "kaç FİLM" sorusunun cevabı buradan çıkar; bir film
# dört mercekte dört satır üretir ve satır saymak onu dört film gösterir.
tablo_filmler() {
    tablo_satir "$@" \
      | awk -F'|' '{ c=$2
            if (match(c, /\*\*[^*]+\*\*/)) c=substr(c, RSTART+2, RLENGTH-4)
            gsub(/~~/,"",c); gsub(/^[ \t]+|[ \t]+$/,"",c)
            if (c!="") print c }'
}

# ── CANLI: dört mercek + iki derin tarama ──────────────────────────
T1=$(tablo_say "$Q/T1_KARE_KALITE.md");        C1=$(tablo_cizili "$Q/T1_KARE_KALITE.md")
T2=$(tablo_say "$Q/T2_DEVAMLILIK_KALITE.md");  C2=$(tablo_cizili "$Q/T2_DEVAMLILIK_KALITE.md")
T3=$(tablo_say "$Q/T3_SES_KALITE.md");         C3=$(tablo_cizili "$Q/T3_SES_KALITE.md")
T4=$(tablo_say "$Q/T4_HIKAYE_KALITE.md");      C4=$(tablo_cizili "$Q/T4_HIKAYE_KALITE.md")
T5=$(tablo_say "$Q/T5_ARKA_PLAN_KALITE.md")
T6=$(tablo_say "$Q/T6_FIZIK_KALITE.md")

# Tamlık matrisi DÖRT mercektir; T5/T6 risk tetikli derin taramadır ve
# matrise girmez (AGENTS.md §3 kart F/F2). O yüzden "ölçülen film" T1-T4'ten
# hesaplanır.
# ad_normal: "The Iron Slope" ile "THE_IRON_SLOPE" aynı filmdir. Tablolar
# başlık biçiminde, ham rapor dosya adları BUYUK_ALT_CIZGI biçiminde yazar;
# karşılaştırma yapabilmek için ikisi de aynı forma indirilir.
ad_normal() { LC_ALL=C tr 'a-z' 'A-Z' | LC_ALL=C sed -E 's/[^A-Z0-9]+/_/g; s/^_+//; s/_+$//' | grep -v '^$'; }

OLCULEN_SET=$(for t in T1_KARE_KALITE T2_DEVAMLILIK_KALITE T3_SES_KALITE T4_HIKAYE_KALITE; do
                  tablo_filmler "$Q/$t.md"; done | ad_normal | sort -u)
OLCULEN=$(printf '%s\n' "$OLCULEN_SET" | grep -c .)
DERIN=$(for t in T5_ARKA_PLAN_KALITE T6_FIZIK_KALITE; do
              tablo_filmler "$Q/$t.md"; done | ad_normal | sort -u | grep -c .)

# ⏳ ÖLÇÜLDÜ AMA İŞLENMEDİ — 25.08.2026'da eklendi.
# "Ölçülmemiş" ile "ölçüldü ama tabloya yazılmadı" aynı şey değildir ve
# ikisinin ilacı da aynı değildir: biri üretim/QA koşusu ister, diğeri
# yalnız rapor işleme (AGENTS.md §3 kart C/D/E/E3/F/F2). Sayaç ikisini
# ayırmazsa taze bir ölçüm "hiç ölçülmemiş" görünür ve iki kez koşulur.
# Canlı mercek sonekleri: KARE · DEVAMLILIK · HIKAYE · ARKA_PLAN · FIZIK
# (SES bilerek dışarıda — eski 6 mercekli sistemde de aynı adı taşıyordu,
#  tek başına canlı koşu kanıtı değildir).
HAM_SET=$(ls -1 "$Q/02_HAM_RAPORLAR/" 2>/dev/null \
    | grep -E '_(KARE|DEVAMLILIK|HIKAYE|ARKA_PLAN|FIZIK)_HAM\.md$' \
    | sed -E 's/_(KARE|DEVAMLILIK|HIKAYE|ARKA_PLAN|FIZIK)_HAM\.md$//' \
    | ad_normal | sort -u)
ISLENMEMIS=$(comm -23 <(printf '%s\n' "$HAM_SET" | grep -v '^$') \
                      <(printf '%s\n' "$OLCULEN_SET" | grep -v '^$'))
ISLENMEMIS_N=$(printf '%s\n' "$ISLENMEMIS" | grep -c .)

# 01_FILM_RAPORLARI'nda FRAGMAN kayıtları da var; fragman bir FİLM DEĞİLDİR.
# Eski hesap onları film sayıyordu ve "ölçülmemiş film" sayısını 3 eksik
# gösteriyordu — sayı yalanının ta kendisi.
KAYIT_FRAG=$(ls -1 "$Q/01_FILM_RAPORLARI/" 2>/dev/null | grep -ciE "_FRAGMAN\.md$")
KAYIT=$(ls -1 "$Q/01_FILM_RAPORLARI/" 2>/dev/null | grep -viE "^[0-9_]*README" \
        | grep -viE "_FRAGMAN\.md$" | wc -l | tr -d ' ')
HAM=$(ls -1 "$Q/02_HAM_RAPORLAR/" 2>/dev/null | grep -v README | wc -l | tr -d ' ')

# D117: her filmin yanında <FILM>_QA_SPEC.md durur. SPEC yoksa rubrik
# yalnız mod V koşulabilir (belgesiz) — Iron Slope'un altı merceği tam bu
# yüzden mod V koşuldu ve matris 0/4'te kaldı. Yani SPEC borcu doğrudan
# ölçüm kalitesinin üst akışıdır, ayrı bir konu değil.
SPECLI=0
for d in dikey_shorts_filmler yatay_2_4_dk_filmler_uzay \
         yatay_3_5_dk_filmler yatay_10_20_dk_filmler; do
    [ -d "$d" ] || continue
    for f in "$d"/*/; do
        [ -d "$f" ] || continue
        [ "$(basename "$f")" = "kilavuzlar" ] && continue
        ls "$f" 2>/dev/null | grep -qiE "_QA_SPEC\.md$" && SPECLI=$((SPECLI + 1))
    done
done

echo "🔍 ÖLÇÜM DURUMU — CANLI SİSTEM  (22.08.2026'dan beri · 4 mercek + 2 derin tarama)"
ciz() { [ "${1:-0}" -gt 0 ] && printf "   ⚠️ %s satır üstü çizili (skor geçersiz)" "$1"; echo; }
printf "   ① T1 KARE          %s satır" "$T1"; ciz "$C1"
printf "   ② T2 DEVAMLILIK    %s satır" "$T2"; ciz "$C2"
printf "   ③ T3 SES           %s satır" "$T3"; ciz "$C3"
printf "   ④ T4 HİKAYE        %s satır" "$T4"; ciz "$C4"
printf "   🔬 T5 ARKA PLAN    %s satır   derin tarama · matrise girmez\n" "$T5"
printf "   🔬 T6 FİZİK        %s satır   derin tarama · matrise girmez\n" "$T6"
echo
printf "   ⭐ CANLI SİSTEMDE ÖLÇÜLEN FİLM   %s / %s\n" "$OLCULEN" "$TOPLAM"
if [ "$OLCULEN" -lt "$TOPLAM" ]; then
    printf "   ⛔ ÖLÇÜLMEMİŞ                    %s / %s\n" "$((TOPLAM - OLCULEN))" "$TOPLAM"
fi
if [ "$ISLENMEMIS_N" -gt 0 ]; then
    printf "   ⏳ ÖLÇÜLDÜ AMA TABLOYA İŞLENMEDİ  %s film\n" "$ISLENMEMIS_N"
    printf '%s\n' "$ISLENMEMIS" | grep -v '^$' | sed 's/^/      · /'
    echo "      ham raporu var, T tablosunda satırı yok → AGENTS.md §3 kart C/D/E/E3/F/F2"
fi
printf "      (derin tarama görmüş film: %s)\n" "$DERIN"
echo
printf "   film kaydı (01/)   %s film" "$KAYIT"
[ "$KAYIT_FRAG" -gt 0 ] && printf "  + %s fragman kaydı (film değil)" "$KAYIT_FRAG"
echo
printf "   ham rapor  (02/)   %s\n" "$HAM"
printf "   ⚠️ 01/ kayıtlarının çoğu KAPALI sistemin ölçümüdür — canlı sayı yukarıdaki ⭐\n"
echo
printf "   SPEC'i olan film (D117)   %s / %s" "$SPECLI" "$TOPLAM"
if [ "$SPECLI" -lt "$TOPLAM" ]; then
    printf "   ⛔ %s film SPEC'siz → rubrik yalnız mod V koşulur" "$((TOPLAM - SPECLI))"
fi
echo
echo

# ─── DERS → KAPI ───────────────────────────────────────────────────
# 01.09.2026 (D161/D162 · DERSLER/00_DERS_YAZIM_KONTRATI.md): dersin kapısı
# yoksa dersin okunduğu ölçülemez. Kapı satırı olan ders sayısı, ⛔ ÇALIŞMIYOR
# damgalılar, mod D koşusu ve rubrik hacmi burada; hiçbiri belgeye elle yazılmaz.
# Son 5 FİLM dersi (01-07) her oturum başında görünür — bir ders sabah yazılıp
# aynı gün yazılan filme ulaşmadı; görünmezlikten.
echo "🧭 DERS → KAPI  (kontrat: DERSLER/00_DERS_YAZIM_KONTRATI.md)"
# ⚠️ 00_* dosyaları (kontrat şablonu) sayıma GİRMEZ — şablonun örnek satırları ders değildir.
KAPILI=$(cat "$K/DERSLER/"0[1-9]_*.md | grep -cE "^\*\*KAPI:\*\*")
CALISMIYOR=$(cat "$K/DERSLER/"0[1-9]_*.md | grep -cE "^\*\*TEKRAR:\*\*.*ÇALIŞMIYOR")
# ⚠️ AÇIK aday: "## ADAY-n". Kapanan aday "## ✅ ADAY-n" olur ve sayılmaz.
#    grep 0 bulunca exit 1 döner; `|| echo 0` iki satır basıyordu — `|| true` ile susturulur.
ADAY=$(grep -cE "^## ADAY-" "$K/DERSLER/GOZLEM_DEFTERI.md" 2>/dev/null || true); ADAY=${ADAY:-0}
MODD=$(grep -lE "^INPUT MODE:[[:space:]]*D" "$Q/02_HAM_RAPORLAR/"*.md 2>/dev/null | wc -l | tr -d ' ')
printf "   KAPI satırı olan ders         %s / %s   (geriye dönük tasnif YOK — dokununca alır)\n" "$KAPILI" "$DERS"
# ⭐ KAPI SATIRI SAYMAK KAPIYI ÇÖZMEK DEĞİLDİR (05.09.2026).
#    Kontrat kapıyı ZORUNLU kılıyor, sayaç kapı satırını SAYIYORDU — ama kapının
#    işaret ettiği betik jetonu / liste maddesi hiç ARANMIYORDU. İlk koşu: D179'un
#    kapısı `prompt_kontrol.py ⑳b DEĞİŞİM KAPISI` yazılı, betikte ⑳b sayısı 0.
#    Ders "kapılı" sayılıyordu, kapı yoktu. Ayrıntı: kapi_adres.py --tam
python3 "$K/kapi_adres.py" 2>/dev/null || printf "   ⚠️  kapi_adres.py koşulamadı\n"
printf "   ⛔ ÇALIŞMIYOR damgalı ders     %s\n" "$CALISMIYOR"
[ "$CALISMIYOR" -gt 0 ] && cat "$K/DERSLER/"0[1-9]_*.md \
  | awk '/^## .* DERS [0-9]+/{ if (match($0, /DERS [0-9]+/)) d = substr($0, RSTART+5, RLENGTH-5) }
         /^\*\*TEKRAR:\*\*.*ÇALIŞMIYOR/{ sub(/^\*\*TEKRAR:\*\*/, ""); print "D" d " ·" $0 }' \
  | cut -c1-96 | sed 's/^/      /'
printf "   gözlem defterinde aday        %s   (kapısız — ders DEĞİL)\n" "$ADAY"
printf "   mod D koşusu (02/ ham rapor)  %s\n" "$MODD"
echo "   ── son 5 FİLM dersi (01-07) — yeni film yazmadan önce AÇ ──"
cat "$K/DERSLER/"0[1-7]_*.md | grep -E "^## .{0,4} DERS [0-9]+" | cut -c1-92 \
  | awk '{ if (match($0, /DERS [0-9]+/)) { n = substr($0, RSTART+5, RLENGTH-5) + 0; print n "\t" $0 } }' \
  | sort -n | tail -5 | cut -f2- | sed 's/^## //; s/^/      /'
echo "   ── rubrik hacmi (tavan 25 KB · üstü çıktı kapısına taşınır, rubriğe eklenmez) ──"
for f in "$K"/QA_PROMPTLARI/_KAYNAK/[1-9]_*.md "$K"/QA_PROMPTLARI/_KAYNAK/1[0-2]_*.md; do   # 9-12: D184
    b=$(wc -c < "$f"); kb=$((b / 1024)); flag=""; [ "$kb" -gt 25 ] && flag="⚠️ tavan üstü"
    printf "      %-38s %3s KB  %s\n" "$(basename "$f" | cut -c1-38)" "$kb" "$flag"
done
echo

# ─── 🚫 ÜRETİM REDDİ (01.09.2026) ───────────────────────────────────
# Depo 14 redi 27 ayrı dosyaya yazmıştı, hiçbir yerde toplamamıştı.
# Defter açıldı; bu blok onun ölçüsüdür. İki sayı önemli:
#   ① MOTORSUZ satır — geriye dönük satırların açığı, kapanması gereken borç
#   ② SONUÇ'suz satır — çözümü kaydedilmemiş red, yalnız bir şikâyettir
DEFTER="$Q/09_URETIM_RED_DEFTERI.md"
echo "🚫 ÜRETİM REDDİ  (defter: FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md)"
if [ -f "$DEFTER" ]; then
    # Defter satırı: "| 3 | 08.08 | …" — baştaki hücresi SAYI olan satırlar
    RED=$(grep -cE "^\| *[0-9]+ *\|" "$DEFTER")
    # MOTOR = 5. alan (baştaki boş alan + # + tarih + film + MOTOR).
    # Sütun konumu değişirse bu sayı sessizce yalan söyler — başlık
    # satırındaki adı doğrulayarak kullan.
    RED_MOTORSUZ=$(awk -F'|' '/^\| *[0-9]+ *\|/ { gsub(/ /,"",$5); if ($5=="?") n++ } END{print n+0}' "$DEFTER")
    RED_SONUCSUZ=$(grep -E "^\| *[0-9]+ *\|" "$DEFTER" | grep -c "⬜ kayıtsız" || true)
    printf "   defterdeki red vakası          %s\n" "$RED"
    printf "   ⛔ MOTOR sütunu boş (\`?\`)      %s   ← bugünden sonraki satırda 0 olmalı\n" "${RED_MOTORSUZ:-0}"
    printf "   ⛔ SONUÇ sütunu boş            %s   ← çözümü kaydedilmemiş red\n" "${RED_SONUCSUZ:-0}"
else
    echo "   ⚠️  defter YOK — red kaydı dosyalara dağılıyor demektir"
fi
# ⑯ kapısının canlı ölçüsü: promptlarda kaç politika tetikleyicisi duruyor.
# ⛔ Betik koşulur, sayı buraya yazılmaz (kural ①).
echo "   ── ⑯ POLİTİKA SÖZLÜĞÜ · canlı tarama (prompt_kontrol) ──"
python3 "$K/PROMPT_KONTROL/prompt_kontrol.py" \
    dikey_shorts_filmler yatay_2_4_dk_filmler_uzay \
    yatay_3_5_dk_filmler yatay_10_20_dk_filmler 2>/dev/null \
  | grep -oE "politika sözlüğü T[12] · [0-9]+|milliyet ifadesi|gövdeye yönelmiş şiddet fiili|gerçek kurum adı|yapısal red profili" \
  | awk '/T1 ·/{t1+=$NF; n1++} /T2 ·/{t2+=$NF; n2++} /milliyet/{m++}
         /şiddet fiili/{f++} /kurum/{k++} /yapısal/{y++}
         END{ printf "      T1 %d tetikleyici (%d promptta) · T2 %d (%d) · şiddet fiili %d\n", t1,n1,t2,n2,f;
              printf "      ⛔ MİLLİYET %d  ← §7 DOĞRULANMIŞ red · kurum %d · yapısal red profili %d\n", m,k,y }'
echo

# ─── ARŞİV: KAPALI TABLOLAR ────────────────────────────────────────
# Bunlar 22.08.2026'da kapandı. Silinmediler çünkü KANIT'tırlar; ama
# DURUM GÖSTERGESİ DEĞİLLER ve yukarıdaki canlı sayılarla toplanmazlar.
VQ=$(tablo_say "$K/LESSONS_LEARNED.md" "KALİTE TAKİP TABLOSU")
SQ=$(tablo_say "$Q/03_HIKAYE_KALITE_TABLOSU.md")
MQ=$(tablo_say "$Q/04_MANTIK_KALITE_TABLOSU.md")
SHQ=$(tablo_say "$Q/05_SHORTS_KALITE_TABLOSU.md")
KQ=$(tablo_say "$Q/06_KARAKTER_KALITE_TABLOSU.md")
SESQ=$(tablo_say "$Q/07_SES_KALITE_TABLOSU.md")

echo "🗄️  ARŞİV — KAPALI TABLOLAR  (22.08.2026 · yeni satır YAZILMAZ)"
echo "   ⚠️ Aşağısı DURUM DEĞİL, arşiv hacmidir. Eski 6 mercekli sistemin"
echo "      ölçümüdür ve T1-T6 ile KARŞILAŞTIRILAMAZ."
printf "   VIDEO_QA %s · SENARYO %s · MANTIK %s · SHORTS %s · KARAKTER %s · SES %s\n" \
       "$VQ" "$SQ" "$MQ" "$SHQ" "$KQ" "$SESQ"
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
