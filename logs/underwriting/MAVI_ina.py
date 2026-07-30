#!/usr/bin/env python3
"""MAVI_ina.py — Mavi Giyim (MAVI.IS) basit 3 senaryolu İNA (DCF).

Yaklaşım: Türkiye'de çok yüksek enflasyon nedeniyle nominal TL İNA anlamsızlaşır;
bu yüzden model **REEL** (sabit 2026 TL) terimlerle kurulur ve **reel WACC** ile
iskonto edilir. FCFF (firmaya serbest nakit akışı) yöntemi kullanılır:

    FCFF = EBIT*(1-vergi) + Amortisman - Capex - ΔİşletmeSermayesi

Tüm varsayımlar değişken; tekrarlanabilirlik için tek dosyada.

Veri kaynakları (2026-07-17 kapanışı):
  - Fiyat 41.02, pay sayısı 783.604.542  (Yahoo Finance defaultKeyStatistics)
  - TTM hasılat ~47.5 mlr TL, TTM FAVÖK ~6.44 mlr TL  (Yahoo financialData)
  - Net nakit 7.037 mlr TL (leasing hariç, şirket/Ziraat Yat. 1Ç26)
    * Leasing dahil (Yahoo) net nakit ~3.9 mlr → duyarlılık altta.
"""

# ---- Sabit girdiler (kaynak: yukarıdaki not) ----
PRICE = 41.02
SHARES = 783_604_542
REV0 = 47.5e9          # TTM hasılat (reel, 2026 TL)
NET_CASH = 7.037e9     # şirket tanımı (leasing hariç)
NET_CASH_CONS = 3.9e9  # muhafazakâr (leasing dahil, Yahoo)
TAX = 0.25
YEARS = 5

MKTCAP = PRICE * SHARES

# ---- Senaryolar ----
# g_rev: yıllık REEL hasılat büyümesi | ebitda_m: FAVÖK marjı |
# da_pct/capex_pct/wc_pct: hasılata oran | wacc: reel iskonto | g_term: reel terminal büyüme
SCEN = {
    "Bear (Ayı)": dict(g_rev=0.00, ebitda_m=0.130, da_pct=0.030, capex_pct=0.032,
                       wc_pct=0.15, wacc=0.16, g_term=0.020, prob=0.30),
    "Base (Taban)": dict(g_rev=0.04, ebitda_m=0.150, da_pct=0.030, capex_pct=0.030,
                         wc_pct=0.15, wacc=0.14, g_term=0.025, prob=0.45),
    "Bull (Boğa)": dict(g_rev=0.08, ebitda_m=0.170, da_pct=0.030, capex_pct=0.030,
                        wc_pct=0.15, wacc=0.125, g_term=0.030, prob=0.25),
}


def dcf(g_rev, ebitda_m, da_pct, capex_pct, wc_pct, wacc, g_term, net_cash=NET_CASH, **_):
    rev_prev = REV0
    pv_explicit = 0.0
    fcff_last = 0.0
    for t in range(1, YEARS + 1):
        rev = rev_prev * (1 + g_rev)
        ebitda = rev * ebitda_m
        da = rev * da_pct
        ebit = ebitda - da
        nopat = ebit * (1 - TAX)
        capex = rev * capex_pct
        dwc = (rev - rev_prev) * wc_pct       # artan hasılatın işletme sermayesi yükü
        fcff = nopat + da - capex - dwc
        pv_explicit += fcff / (1 + wacc) ** t
        fcff_last = fcff
        rev_prev = rev
    tv = fcff_last * (1 + g_term) / (wacc - g_term)   # Gordon terminal
    pv_tv = tv / (1 + wacc) ** YEARS
    ev = pv_explicit + pv_tv
    equity = ev + net_cash
    return dict(ev=ev, equity=equity, per_share=equity / SHARES,
                pv_explicit=pv_explicit, pv_tv=pv_tv, fcff1=None)


def main():
    print(f"MAVI.IS | Fiyat {PRICE:.2f} TL | Pay {SHARES:,} | Piyasa değeri {MKTCAP/1e9:.2f} mlr TL")
    print(f"Net nakit (baz): {NET_CASH/1e9:.2f} mlr | muhafazakâr: {NET_CASH_CONS/1e9:.2f} mlr\n")
    print(f"{'Senaryo':14}{'FD(mlr)':>9}{'Özkaynak(mlr)':>15}{'Hisse(TL)':>11}{'Yükseliş':>10}{'Olasılık':>10}")
    weighted = 0.0
    fair_cons = {}
    for name, p in SCEN.items():
        r = dcf(**p)
        r_cons = dcf(net_cash=NET_CASH_CONS, **{k: v for k, v in p.items() if k != "prob"})
        ups = r["per_share"] / PRICE - 1
        weighted += p["prob"] * r["per_share"]
        fair_cons[name] = r_cons["per_share"]
        print(f"{name:14}{r['ev']/1e9:>9.1f}{r['equity']/1e9:>15.1f}"
              f"{r['per_share']:>11.2f}{ups*100:>9.1f}%{p['prob']*100:>9.0f}%")
    print("-" * 69)
    print(f"{'Olasılık-ağırlıklı adil değer:':<45}{weighted:>11.2f} TL  "
          f"(yükseliş {weighted/PRICE-1:+.1%})")
    print("\nMuhafazakâr net nakit (leasing dahil) ile hisse başı adil değer:")
    for k, v in fair_cons.items():
        print(f"  {k:14}{v:>8.2f} TL")
    print("\nNot: PEG nominal TL'de anlamsız (enflasyon kaynaklı yüksek nominal büyüme);")
    print("büyüme REEL terimlerle senaryolara gömülüdür.")


if __name__ == "__main__":
    main()
