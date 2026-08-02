# daily_playbook.md (US) — Günlük Rutin

1. **Mark-to-market:** `python scripts/update_nav.py` (USD, SPY benchmark; fiyat Yahoo chart API).
2. **Haber/8-K taraması:** portföy + izleme listesi için EDGAR/haber akışı.
3. **Hedef / invalidation kontrolü:** tetiklenmişse `scripts/execute_trade.py` ile işlem.
4. **Günün underwriting görevi:** `logs/underwriting/00-sablon-ve-izleme.md` sırasıyla.
5. **Karar günlüğü:** `logs/decisions/YYYY-MM-DD.md`.
6. **İçerik taslakları:** `content/drafts/YYYY-MM-DD/` (asla otomatik yayınlama).
7. **Commit:** `git add -A && git commit` — "US Gün N: <özet>".

Notlar: USD baz → enflasyon düzeltmesi yok. Yarıyıl/çeyrek 10-Q takvimleri EDGAR'dan izlenir.
