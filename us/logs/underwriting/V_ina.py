#!/usr/bin/env python3
"""V_ina.py — Visa USD FCFF İNA (3 senaryo).
Kaynak (2026-07-31, Yahoo): fiyat 366,13; pay ~1,868 mlr; PD ~684 mlr USD.
TTM hasılat 44,5 mlr, EBITDA 31,1 mlr (%70), op. marj %66, ROE %61, rev büyüme +%14.
Net BORÇ ~10 mlr (borç 23,9 − nakit 13,8). Vergi ~%19. Düşük sermaye yoğunluğu (toll-road)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scripts"))
from dcf_lib import run_scenarios

PRICE, SHARES = 366.13, 1_868_000_000
NET_CASH = -10.0e9
base = dict(rev0=44.5e9, da_pct=0.03, capex_pct=0.03, wc_pct=0.01)
scen = {
    "Bear (Ayı)":  dict(g_rev=0.08, ebitda_m=0.66, wacc=0.095, g_term=0.035, prob=0.30),
    "Base (Taban)":dict(g_rev=0.12, ebitda_m=0.70, wacc=0.085, g_term=0.035, prob=0.45),
    "Bull (Boğa)": dict(g_rev=0.15, ebitda_m=0.72, wacc=0.080, g_term=0.040, prob=0.25),
}
if __name__ == "__main__":
    run_scenarios("V", PRICE, SHARES, base, scen, NET_CASH, tax=0.19)
