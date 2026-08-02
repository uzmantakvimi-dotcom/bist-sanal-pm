# US Paper PM — $10k, %20 USD hedefi

BIST sanal PM ile **aynı yaklaşım**, ABD borsasına uyarlanmış kağıt portföy.
10.000 USD · 12 ay · **%20 USD hedefi** · benchmark **S&P 500 (SPY)**. Gerçek para yok;
git geçmişi denetim izidir. (Ayrı repo açma izni gelene kadar `bist-sanal-pm` içinde `us/` altında.)

## Yapı
| Yol | İçerik |
|---|---|
| `mandate.md` | Anayasa (USD/SPY uyarlaması, risk limitleri) |
| `config.json` | 10k USD, SPY, %20 hedef, limitler (tek %15 / sektör %30 / tema %20 / nakit %5) |
| `portfolio.json` | Pozisyonlar (yalnızca `execute_trade.py` ile değişir) — **şu an tamamı nakit** |
| `scripts/update_nav.py` | Mark-to-market, SPY alpha, sektör/tema limit kontrolü |
| `scripts/execute_trade.py` | BUY/SELL/CORRECTION (append-only ledger) |
| `scripts/lib_prices.py` | Yahoo chart API (SPY + US tickers) |
| `logs/underwriting/00-sablon-ve-izleme.md` | Şablon + underwrite edilecek aday listesi |

## Çalıştırma
```bash
python scripts/update_nav.py
```

## Durum (kuruluş)
- **NAV $10.000** (tamamı nakit) · pozisyon yok · benchmark SPY ilk NAV'da sabitlenecek.
- Sıradaki: izleme listesindeki adayları sırayla underwrite etmek.
- **Dürüst not:** %20 USD, S&P 500'ün ~2 katı — hedeftir, garanti değil.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
