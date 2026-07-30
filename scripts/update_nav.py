#!/usr/bin/env python3
"""update_nav.py — portfoyu mark-to-market yapar.

- config.json + portfolio.json okur.
- Guncel fiyatlari ceker (lib_prices), pozisyon degerlerini ve NAV'i hesaplar.
- Ilk calistirmada benchmark_start_level'i sabitler.
- Risk limitlerini kontrol eder.
- logs/nav/YYYY-MM-DD.json gecmisini yazar ve konsola ozet basar.

portfolio.json'u DEGISTIRMEZ (sadece config'te benchmark_start_level'i bir kez sabitler).
Pozisyon degisiklikleri yalnizca execute_trade.py ile yapilir.
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

    prices = lib_prices.fetch_prices(symbols + [bench])

    tier_map = cfg.get("tier_map", {})
    rows = []
    invested = 0.0
    for sym, pos in pf["positions"].items():
        pr = prices[sym]["price"]
        if pr is None:
            print(f"UYARI: {sym} fiyati alinamadi, cost_basis kullaniliyor.")
            pr = pos["avg_cost"]
        mv = pos["shares"] * pr
        invested += mv
        pnl = mv - pos["cost_basis"]
        rows.append({
            "symbol": sym, "shares": pos["shares"], "avg_cost": pos["avg_cost"],
            "price": pr, "market_value": round(mv, 2),
            "cost_basis": pos["cost_basis"], "pnl": round(pnl, 2),
            "pnl_pct": round(100 * pnl / pos["cost_basis"], 2) if pos["cost_basis"] else 0,
            "tier": tier_map.get(sym, pos.get("tier")), "status": pos.get("status"),
            "price_source": prices[sym]["source"], "price_date": prices[sym]["date"],
        })

    cash = pf["cash"]
    nav = invested + cash
    start = cfg["starting_capital"]
    total_ret = 100 * (nav - start) / start

    # weights
    for r in rows:
        r["weight_pct"] = round(100 * r["market_value"] / nav, 2)
    cash_pct = round(100 * cash / nav, 2)

    # benchmark
    bpx = prices[bench]["price"]
    bdate = prices[bench]["date"]
    if cfg.get("benchmark_start_level") in (None, 0):
        cfg["benchmark_start_level"] = bpx
        cfg["benchmark_start_note"] = f"{bdate} XU100 kapanisina sabitlendi (ilk NAV calismasi)."
        save("config.json", cfg)
        print(f">> benchmark_start_level sabitlendi: {bpx} ({bdate})")
    bench_ret = 100 * (bpx - cfg["benchmark_start_level"]) / cfg["benchmark_start_level"]

    # risk limitleri
    lim = cfg["risk_limits"]
    warnings = []
    for r in rows:
        if r["weight_pct"] > lim["max_single_position_pct"]:
            warnings.append(f"{r['symbol']} agirligi %{r['weight_pct']} > maks %{lim['max_single_position_pct']}")
    if cash_pct < lim["min_cash_pct"]:
        warnings.append(f"Nakit %{cash_pct} < min %{lim['min_cash_pct']}")
    mid = sum(r["weight_pct"] for r in rows if r.get("tier") == "mid")
    if mid > lim["max_midcap_tier_pct"]:
        warnings.append(f"Mid-cap katmani %{round(mid,2)} > maks %{lim['max_midcap_tier_pct']}")

    asof = prices[symbols[0]]["date"] or datetime.date.today().isoformat()
    report = {
        "as_of": asof, "generated": datetime.datetime.utcnow().isoformat() + "Z",
        "nav": round(nav, 2), "cash": round(cash, 2), "cash_pct": cash_pct,
        "invested": round(invested, 2), "starting_capital": start,
        "total_return_pct": round(total_ret, 2),
        "benchmark": {"symbol": bench, "start": cfg["benchmark_start_level"],
                      "level": bpx, "date": bdate, "return_pct": round(bench_ret, 2)},
        "alpha_pct": round(total_ret - bench_ret, 2),
        "midcap_tier_pct": round(mid, 2),
        "positions": rows, "risk_warnings": warnings,
    }

    os.makedirs(os.path.join(ROOT, "logs", "nav"), exist_ok=True)
    save(f"logs/nav/{asof}.json", report)
    save("logs/nav/latest.json", report)

    # konsol ozeti
    print(f"\n=== NAV OZETI ({asof}) ===")
    print(f"NAV: {nav:,.2f} TL | Nakit: {cash:,.2f} ({cash_pct}%) | Yatirimli: {invested:,.2f}")
    print(f"Toplam getiri: {total_ret:+.2f}%  |  XU100: {bench_ret:+.2f}%  |  Alpha: {total_ret-bench_ret:+.2f}%")
    print(f"{'Sembol':10}{'Adet':>7}{'Fiyat':>10}{'Deger':>14}{'Agirlik':>9}{'PnL%':>8}  Kaynak")
    for r in rows:
        print(f"{r['symbol']:10}{r['shares']:>7}{r['price']:>10.2f}{r['market_value']:>14,.0f}"
              f"{r['weight_pct']:>8.1f}%{r['pnl_pct']:>7.1f}%  {r['price_source']}")
    if warnings:
        print("\nRISK UYARILARI:")
        for w in warnings:
            print("  ! " + w)
    else:
        print("\nRisk limitleri: hepsi uygun.")
    return report


if __name__ == "__main__":
    main()
