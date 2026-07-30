# BIST Sanal PM — Kamuya Açık Şeffaflık Deneyi

500.000 TL **sanal** (kağıt) portföy · 12 ay · **%100 nominal getiri hedefi** ·
benchmark **BIST 100 (XU100)**. Gerçek para yok. Tüm kararlar, kod ve loglar açık;
git geçmişi denetim izidir — hiçbir geçmiş kayıt silinmez, hata yeni bir kayıtla düzeltilir.

## Yapı
| Yol | İçerik |
|---|---|
| `CLAUDE.md` (PDF) / `mandate.md` | Operasyon talimatları / anayasa |
| `config.json` | Sermaye, benchmark, risk limitleri, ölçek sınıflaması, enflasyon |
| `portfolio.json` | Güncel pozisyonlar (**yalnızca** `execute_trade.py` ile değişir) |
| `scripts/update_nav.py` | Mark-to-market, NAV/alpha, risk kontrolü |
| `scripts/execute_trade.py` | BUY / SELL / CORRECTION (append-only ledger) |
| `scripts/lib_prices.py` | Fiyat katmanı (Yahoo chart API + CA bundle) |
| `logs/ledger/trades.jsonl` | Değiştirilemez işlem defteri |
| `logs/underwriting/` | Hisse yüklenim belgeleri + İNA modelleri |
| `logs/decisions/` | Günlük karar günlükleri |
| `logs/nav/` | Günlük NAV anlık görüntüleri |
| `content/` | İçerik şablonları ve taslakları (asla otomatik yayınlanmaz) |
| `daily_playbook.md` | Günlük rutin |

## Günlük çalıştırma
```bash
pip install yfinance --break-system-packages   # ilk kez
python scripts/update_nav.py
```
yfinance bu ortamdaki proxy'den TLS geçemediği için `lib_prices` doğrudan Yahoo
chart API'yi CA bundle ile kullanır; kullanılan kaynak her raporda `price_source`'ta görünür.

## Son durum (2026-07-20, Gün 1)
- **NAV 494.891 TL** (−%1,0) · XU100 −%1,9 · **alpha +0,9 puan**
- TURSG bölünme (2:1) düzeltmesi yapıldı (nakit-nötr, eski kayıt korundu).
- MAVI underwriting: **TUT** (adil değer ~57 TL, FD/FAVÖK ~4x, net nakit %22).

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
