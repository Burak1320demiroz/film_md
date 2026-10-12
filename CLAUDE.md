# CLAUDE.md

Bu projenin ajan kontratı **[`AGENTS.md`](AGENTS.md)** dosyasındadır (05.10.2026'dan beri
yeni üretim hattı). Her görevden önce onu oku: akış, kurallar, kim neyi onaylar, dosyaların yeri.
Yöntem: [`uretim_hatti/README.md`](uretim_hatti/README.md).

- **Film işi tek kapıdan:** `/yeni-film`. Yeni film başlatır ya da `ODA/DURUM.md`'den sürdürür.
  Film klasörü süresinin format klasörüne açılır (`yatay_4_dk_filmler/<FILM>/` gibi); ayrı `filmler/` kökü yoktur (08.10.2026).
- **Modeller:** ana ajan **Fable**'dır (`.claude/settings.json`); faz kapılarını o onaylar.
  Alt ajanlar `.claude/agents/`'ta, Opus ya da Sonnet.
- **Sahibin onayı iki yerde:** hikâye seçimi (veto) ve yayın.

Değişmeyen dört kural:
- Commit'i yalnız sahip atar.
- Her çekim 10 saniyedir; çekim sayısı = hedef süre / 10 (sahip kararı 08.10.2026).
- Görsel, video ve ses repoya girmez; `~/film_medya/<FILM>/` altında durur.
- Hiçbir şey silinmez; eski kılavuz ve raporlar düzenlenmez.

⏸️ Eski hat donduruldu: `AGENTS_ESKI_HAT.md` yalnız arşiv haritasıdır, akış dayatmaz.
`bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` yalnız eski filmlerin sayımı içindir.
