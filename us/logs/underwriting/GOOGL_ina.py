#!/usr/bin/env python3
"""GOOGL_ina.py — Alphabet USD FCFF İNA (3 senaryo).
Kaynak (2026-07-31, Yahoo): fiyat 356,13; pay ~12,23 mlr; PD ~4.355 mlr USD.
TTM hasılat 445,9 mlr, EBITDA 173,2 mlr (%38,8), op. marj %34, ROE %48,7, rev büyüme +%24.
Net NAKİT +121,7 mlr (nakit 242,5 − borç 120,8). Vergi ~%16. Capex yüksek (AI veri merkezleri)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scripts"))
from dcf_lib import run_scenarios

PRICE, SHARES = 356.13, 12_228_000_000
NET_CASH = 121.7e9
base = dict(rev0=445.9e9, da_pct=0.06, capex_pct=0.10, wc_pct=0.01)  # normalize capex: mevcut ~%15 AI yatırım fazı, uzun dönem ~%10'a döner
scen = {
    "Bear (Ayı)":  dict(g_rev=0.06, ebitda_m=0.36, wacc=0.105, g_term=0.03, prob=0.30),
    "Base (Taban)":dict(g_rev=0.11, ebitda_m=0.39, wacc=0.095, g_term=0.03, prob=0.45),
    "Bull (Boğa)": dict(g_rev=0.16, ebitda_m=0.41, wacc=0.085, g_term=0.03, prob=0.25),
}
if __name__ == "__main__":
    run_scenarios("GOOGL", PRICE, SHARES, base, scen, NET_CASH, tax=0.16)
