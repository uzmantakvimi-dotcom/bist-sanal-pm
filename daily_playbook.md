# daily_playbook.md — Günlük Rutin

1. **Mark-to-market:** `pip install yfinance --break-system-packages` (ilk kez) ve
   `python scripts/update_nav.py`. yfinance başarısız olursa `lib_prices` doğrudan
   Yahoo chart API'ye düşer (proxy + CA bundle). O da olmazsa `isyatirimhisse` /
   web araştırması, kaynak loglanır.
2. **Haber/KAP taraması:** Portföydeki hisselerle ilgili günün akışı web'den taranır.
3. **Invalidation / hedef fiyat kontrolü:** Tetiklendiyse `scripts/execute_trade.py`
   ile işlem yapılır; gerekçe parametrelerle yazılır.
4. **Günün underwriting görevi** yapılır (`logs/underwriting/00-takvim-ve-sablon.md`).
5. **Karar günlüğü:** `logs/decisions/YYYY-MM-DD.md` yazılır.
6. **İçerik taslakları:** `content/templates.md` şablonlarıyla üretilir ve
   `content/drafts/YYYY-MM-DD/` altına kaydedilir. **ASLA otomatik yayınlama.**
7. **Commit:** `git add -A && git commit` — mesaj formatı: `"Gün N: <özet>"`.

## Fiyat kaynağı notu (bu ortam)
yfinance'in curl_cffi motoru kurumsal proxy'den TLS geçemiyor; `scripts/lib_prices.py`
doğrudan Yahoo chart API'yi `requests` + `/root/.ccr/ca-bundle.crt` ile kullanıyor.
Kullanılan kaynak her NAV raporunda `price_source` alanında görünür.
