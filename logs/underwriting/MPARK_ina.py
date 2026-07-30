#!/usr/bin/env python3
"""MPARK_ina.py — MLP Sağlık (Medical Park) reel FCFF İNA (3 senaryo).
Kaynaklar (2026-07-30): fiyat 404,75; pay 102.122.233 (Yahoo). TTM hasılat 55,1 mlr,
FAVÖK 15,22 mlr (%27,6). Net borç ~15,1 mlr (borç 21,09 − nakit 5,98; ~1x FAVÖK).
1Ç26: hasılat 16,25 mlr (+%6), net kâr 1,67 mlr (beklenti üstü), FAVÖK 4,8 mlr. ROE %20,5.
Yurtdışı/medikal turizm döviz geliri yapısal katalizör."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scripts"))
from dcf_lib import run_scenarios

PRICE, SHARES = 404.75, 102_122_233
NET_CASH = -15.1e9  # net borç
base = dict(rev0=55.1e9, da_pct=0.090, capex_pct=0.090, wc_pct=0.03)
scen = {
    "Bear (Ayı)":  dict(g_rev=0.02, ebitda_m=0.250, wacc=0.14, g_term=0.025, prob=0.30),
    "Base (Taban)":dict(g_rev=0.05, ebitda_m=0.275, wacc=0.12, g_term=0.030, prob=0.45),
    "Bull (Boğa)": dict(g_rev=0.09, ebitda_m=0.300, wacc=0.11, g_term=0.030, prob=0.25),
}
if __name__ == "__main__":
    run_scenarios("MPARK.IS", PRICE, SHARES, base, scen, NET_CASH)
