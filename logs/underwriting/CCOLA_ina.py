#!/usr/bin/env python3
"""CCOLA_ina.py — Coca-Cola İçecek reel FCFF İNA (3 senaryo).
Kaynaklar (2026-07-30): fiyat 91,5; pay 2.798.078.602 (Yahoo). TTM hasılat 192,2 mlr,
FAVÖK 35,63 mlr (%18,5). Net borç ~26,4 mlr (borç 51,66 − nakit 25,26). 1Ç26: hasılat
52,4 mlr (+%10,7), FAVÖK 9,0 mlr (+%54, marj %17,8), net kâr 5,2 mlr (+%214)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scripts"))
from dcf_lib import run_scenarios

PRICE, SHARES = 91.5, 2_798_078_602
NET_CASH = -26.4e9  # net borç
base = dict(rev0=192.2e9, da_pct=0.050, capex_pct=0.060, wc_pct=0.04)
scen = {
    "Bear (Ayı)":  dict(g_rev=0.03, ebitda_m=0.160, wacc=0.14, g_term=0.025, prob=0.30),
    "Base (Taban)":dict(g_rev=0.05, ebitda_m=0.185, wacc=0.12, g_term=0.030, prob=0.45),
    "Bull (Boğa)": dict(g_rev=0.08, ebitda_m=0.200, wacc=0.11, g_term=0.030, prob=0.25),
}
if __name__ == "__main__":
    run_scenarios("CCOLA.IS", PRICE, SHARES, base, scen, NET_CASH)
