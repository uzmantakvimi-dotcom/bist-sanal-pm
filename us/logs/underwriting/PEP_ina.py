#!/usr/bin/env python3
"""PEP_ina.py — PepsiCo USD FCFF İNA (3 senaryo).
Kaynak (2026-07-31, Yahoo): fiyat 139,56; pay ~1,371 mlr; PD ~191 mlr USD.
TTM hasılat 96,9 mlr, EBITDA 18,9 mlr (%19,5), op. marj %16,8, ROE %51, rev büyüme +%6,4.
Net BORÇ ~42,5 mlr (borç 53,2 − nakit 10,7). Vergi ~%21. FCF verimi ~%4,1 (defansif)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scripts"))
from dcf_lib import run_scenarios

PRICE, SHARES = 139.56, 1_371_000_000
NET_CASH = -42.5e9
base = dict(rev0=96.9e9, da_pct=0.05, capex_pct=0.05, wc_pct=0.01)
scen = {
    "Bear (Ayı)":  dict(g_rev=0.02, ebitda_m=0.185, wacc=0.085, g_term=0.025, prob=0.30),
    "Base (Taban)":dict(g_rev=0.05, ebitda_m=0.195, wacc=0.075, g_term=0.025, prob=0.45),
    "Bull (Boğa)": dict(g_rev=0.07, ebitda_m=0.205, wacc=0.070, g_term=0.030, prob=0.25),
}
if __name__ == "__main__":
    run_scenarios("PEP", PRICE, SHARES, base, scen, NET_CASH, tax=0.21)
