#!/usr/bin/env python3
"""ENKAI_ina.py — Enka İnşaat reel FCFF İNA (3 senaryo) + net nakit köprüsü.
Kaynaklar (2026-07-30): fiyat 87,05; pay 5.862.743.582 (Yahoo). TTM hasılat 156,5 mlr,
FAVÖK 33,95 mlr (%21,7). NET NAKİT ~213 mlr TL ($5,32 mlr, 1Ç26; piyasa değerinin ~%42'si).
1Ç26: hasılat 35,83 mlr (+%20), FAVÖK 8,06 mlr, net kâr 3,41 mlr (YoY düşük). P/B 1,37.

NOT: Enka'nın değerinin büyük kısmı nakit/yatırım portföyünden gelir; işletme İNA'sı
operasyonel kısmı fiyatlar, net nakit ayrıca eklenir. Düşük ROE (~%12) nakit yükünün sonucu."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "scripts"))
from dcf_lib import run_scenarios

PRICE, SHARES = 87.05, 5_862_743_582
NET_CASH = 213.0e9  # devasa net nakit + uzun vadeli yatırımlar
base = dict(rev0=156.5e9, da_pct=0.045, capex_pct=0.050, wc_pct=0.05)
scen = {
    "Bear (Ayı)":  dict(g_rev=-0.02, ebitda_m=0.180, wacc=0.14, g_term=0.020, prob=0.30),
    "Base (Taban)":dict(g_rev=0.03,  ebitda_m=0.210, wacc=0.12, g_term=0.025, prob=0.45),
    "Bull (Boğa)": dict(g_rev=0.08,  ebitda_m=0.230, wacc=0.11, g_term=0.030, prob=0.25),
}
if __name__ == "__main__":
    run_scenarios("ENKAI.IS", PRICE, SHARES, base, scen, NET_CASH)
