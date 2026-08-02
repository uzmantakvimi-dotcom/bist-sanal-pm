#!/usr/bin/env python3
"""update_nav.py (US) — portföyü mark-to-market yapar (USD, SPY benchmark).

BIST sürümünün USD uyarlaması: enflasyon yok; katman yerine GICS **sektör** ve
**tema** yoğunlaşma limitleri kontrol edilir. portfolio.json'u DEGISTIRMEZ
(sadece ilk çalıştırmada benchmark_start_level'i sabitler).
"""
import json
import os
import sys
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import lib_prices  # noqa: E402


def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return json.load(f)


def save(p, obj):
    with open(os.path.join(ROOT, p), "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    cfg = load("config.json")
    pf = load("portfolio.json")
    symbols = list(pf["positions"].keys())
    bench = cfg["benchmark_symbol"]
    sector_map = cfg.get("sector_map", {})
    theme_map = cfg.get("theme_map", {})

    prices = lib_prices.fetch_prices(symbols + [bench])

    rows = []
    invested = 0.0
    for sym, pos in pf["positions"].items():
        pr = prices[sym]["price"] or pos["avg_cost"]
        mv = pos["shares"] * pr
        invested += mv
        pnl = mv - pos["cost_basis"]
        rows.append({
            "symbol": sym, "shares": pos["shares"], "avg_cost": pos["avg_cost"],
            "price": pr, "market_value": round(mv, 2), "cost_basis": pos["cost_basis"],
            "pnl": round(pnl, 2),
            "pnl_pct": round(100 * pnl / pos["cost_basis"], 2) if pos["cost_basis"] else 0,
            "sector": sector_map.get(sym, pos.get("sector", "?")),
            "theme": theme_map.get(sym, pos.get("theme")),
            "price_source": prices[sym]["source"], "price_date": prices[sym]["date"],
        })

    cash = pf["cash"]
    nav = invested + cash
    start = cfg["starting_capital"]
    total_ret = 100 * (nav - start) / start
    for r in rows:
        r["weight_pct"] = round(100 * r["market_value"] / nav, 2)
    cash_pct = round(100 * cash / nav, 2)

    bpx = prices[bench]["price"]
    bdate = prices[bench]["date"]
    if cfg.get("benchmark_start_level") in (None, 0):
        cfg["benchmark_start_level"] = bpx
        cfg["benchmark_start_note"] = f"{bdate} SPY kapanisina sabitlendi (ilk NAV)."
        save("config.json", cfg)
        print(f">> benchmark_start_level sabitlendi: {bpx} ({bdate})")
    bench_ret = 100 * (bpx - cfg["benchmark_start_level"]) / cfg["benchmark_start_level"]

    lim = cfg["risk_limits"]
    warnings = []
    for r in rows:
        if r["weight_pct"] > lim["max_single_position_pct"]:
            warnings.append(f"{r['symbol']} %{r['weight_pct']} > tek isim maks %{lim['max_single_position_pct']}")
    if cash_pct < lim["min_cash_pct"]:
        warnings.append(f"Nakit %{cash_pct} < min %{lim['min_cash_pct']}")
    # sektor
    sec = {}
    for r in rows:
        sec[r["sector"]] = sec.get(r["sector"], 0) + r["weight_pct"]
    for s, w in sec.items():
        if w > lim["max_sector_pct"]:
            warnings.append(f"Sektor {s} %{round(w,2)} > maks %{lim['max_sector_pct']}")
    # tema
    th = {}
    for r in rows:
        if r.get("theme"):
            th[r["theme"]] = th.get(r["theme"], 0) + r["weight_pct"]
    for t, w in th.items():
        if w > lim["max_theme_pct"]:
            warnings.append(f"Tema {t} %{round(w,2)} > maks %{lim['max_theme_pct']}")

    asof = (prices[symbols[0]]["date"] if symbols else prices[bench]["date"]) or datetime.date.today().isoformat()
    report = {
        "as_of": asof, "generated": datetime.datetime.utcnow().isoformat() + "Z",
        "currency": "USD", "nav": round(nav, 2), "cash": round(cash, 2), "cash_pct": cash_pct,
        "invested": round(invested, 2), "starting_capital": start,
        "total_return_pct": round(total_ret, 2),
        "benchmark": {"symbol": bench, "start": cfg["benchmark_start_level"],
                      "level": bpx, "date": bdate, "return_pct": round(bench_ret, 2)},
        "alpha_pct": round(total_ret - bench_ret, 2),
        "sector_weights": {k: round(v, 2) for k, v in sec.items()},
        "positions": rows, "risk_warnings": warnings,
    }
    os.makedirs(os.path.join(ROOT, "logs", "nav"), exist_ok=True)
    save(f"logs/nav/{asof}.json", report)
    save("logs/nav/latest.json", report)

    print(f"\n=== US NAV OZETI ({asof}) — USD ===")
    print(f"NAV: ${nav:,.2f} | Nakit: ${cash:,.2f} ({cash_pct}%) | Yatirimli: ${invested:,.2f}")
    print(f"Toplam getiri: {total_ret:+.2f}%  |  SPY: {bench_ret:+.2f}%  |  Alpha: {total_ret-bench_ret:+.2f}%")
    for r in rows:
        print(f"  {r['symbol']:6}{r['shares']:>8.2f}{r['price']:>10.2f}{r['market_value']:>12,.0f}"
              f"{r['weight_pct']:>7.1f}%  {r['sector']}")
    if warnings:
        print("RISK UYARILARI:")
        for w in warnings:
            print("  ! " + w)
    else:
        print("Risk limitleri: hepsi uygun." if symbols else "Pozisyon yok (tamami nakit).")
    return report


if __name__ == "__main__":
    main()
