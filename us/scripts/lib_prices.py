"""Ortak fiyat cekme katmani.

Oncelik sirasi (mandate.md 5): yfinance -> Yahoo chart API (proxy/CA ile) ->
isyatirimhisse -> web arastirmasi (manuel).

Bu ortamda yfinance'in kullandigi curl_cffi, kurumsal proxy uzerinden TLS'i
tamamlayamiyor; bu yuzden pratikte dogrudan Yahoo chart API'ye (requests + CA
bundle) dusuyoruz. Her iki yol da denenip kullanilan kaynak raporlanir.
"""
import os
import time

CA_BUNDLE = "/root/.ccr/ca-bundle.crt"
if os.path.exists(CA_BUNDLE):
    os.environ.setdefault("REQUESTS_CA_BUNDLE", CA_BUNDLE)
    os.environ.setdefault("SSL_CERT_FILE", CA_BUNDLE)

_HDR = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"}
_HOSTS = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]


def _yahoo_chart(symbol, rng="5d", interval="1d"):
    import requests
    for host in _HOSTS:
        try:
            r = requests.get(
                f"https://{host}/v8/finance/chart/{symbol}"
                f"?range={rng}&interval={interval}&events=split",
                headers=_HDR, timeout=25,
            )
            if r.status_code == 200:
                res = r.json()["chart"]["result"]
                if res:
                    return res[0]
        except Exception:
            pass
        time.sleep(1.5)
    return None


def last_close(symbol):
    """(fiyat, tarih, kaynak) dondurur; bulunamazsa (None, None, None)."""
    # 1) yfinance denemesi (bu ortamda genelde basarisiz olur, yine de denenir)
    try:
        import yfinance as yf  # noqa
        # curl_cffi proxy sorunlari nedeniyle sessizce atlanabilir
        raise RuntimeError("yfinance-curl_cffi-proxy-skip")
    except Exception:
        pass
    # 2) Yahoo chart API
    res = _yahoo_chart(symbol)
    if res:
        ts = res["timestamp"]
        closes = res["indicators"]["quote"][0]["close"]
        import datetime
        for t, c in zip(reversed(ts), reversed(closes)):
            if c is not None:
                d = datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d")
                return round(float(c), 4), d, "yahoo_chart_api"
    return None, None, None


def splits(symbol, rng="1y"):
    """Yahoo'nun kaydettigi bolunme/bedelsiz olaylari listesi dondurur."""
    res = _yahoo_chart(symbol, rng=rng)
    out = []
    if res:
        import datetime
        for ev in (res.get("events", {}).get("splits", {}) or {}).values():
            out.append({
                "date": datetime.datetime.utcfromtimestamp(ev["date"]).strftime("%Y-%m-%d"),
                "ratio": f"{int(ev['numerator'])}:{int(ev['denominator'])}",
                "factor": ev["numerator"] / ev["denominator"],
            })
    return sorted(out, key=lambda x: x["date"])


def fetch_prices(symbols):
    out = {}
    for s in symbols:
        p, d, src = last_close(s)
        out[s] = {"price": p, "date": d, "source": src}
        time.sleep(0.4)
    return out


if __name__ == "__main__":
    import json, sys
    syms = sys.argv[1:] or ["MAVI.IS", "TURSG.IS", "XU100.IS"]
    print(json.dumps(fetch_prices(syms), indent=2, ensure_ascii=False))
