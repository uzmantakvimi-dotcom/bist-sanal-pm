"""dcf_lib.py — Paylaşılan basit REEL FCFF İNA yardımcı fonksiyonu.

Türkiye'de yüksek enflasyon nedeniyle model REEL (sabit fiyat) terimlerle kurulur ve
reel WACC ile iskonto edilir. Her HISSE_ina.py bu fonksiyonu kendi varsayımlarıyla çağırır.

    FCFF = EBIT*(1-vergi) + Amortisman - Capex - ΔİşletmeSermayesi
    Özkaynak değeri = FCFF-EV + net_nakit  (net borç için net_nakit negatif verilir)
"""


def fcff_dcf(rev0, ebitda_m, da_pct, capex_pct, wc_pct, g_rev, wacc, g_term,
             net_cash, tax=0.25, years=5):
    rev_prev = rev0
    pv = 0.0
    fcff = 0.0
    for t in range(1, years + 1):
        rev = rev_prev * (1 + g_rev)
        ebitda = rev * ebitda_m
        da = rev * da_pct
        ebit = ebitda - da
        nopat = ebit * (1 - tax)
        capex = rev * capex_pct
        dwc = (rev - rev_prev) * wc_pct
        fcff = nopat + da - capex - dwc
        pv += fcff / (1 + wacc) ** t
        rev_prev = rev
    tv = fcff * (1 + g_term) / (wacc - g_term)
    pv_tv = tv / (1 + wacc) ** years
    ev = pv + pv_tv
    equity = ev + net_cash
    return dict(ev=ev, equity=equity, pv_explicit=pv, pv_tv=pv_tv)


def run_scenarios(name, price, shares, base, scen, net_cash, tax=0.25, years=5):
    """scen: {ad: {g_rev, ebitda_m, wacc, g_term, prob}}; base: ortak da/capex/wc/rev0."""
    mktcap = price * shares
    print(f"{name} | Fiyat {price:.2f} | Pay {shares:,.0f} | Piyasa değeri {mktcap/1e9:.1f} mlr TL")
    print(f"Net nakit(+)/borç(-): {net_cash/1e9:+.1f} mlr TL\n")
    print(f"{'Senaryo':16}{'Hisse(TL)':>11}{'Yükseliş':>11}{'Olasılık':>10}")
    w = 0.0
    for ad, p in scen.items():
        r = fcff_dcf(rev0=base['rev0'], ebitda_m=p['ebitda_m'], da_pct=base['da_pct'],
                     capex_pct=base['capex_pct'], wc_pct=base['wc_pct'], g_rev=p['g_rev'],
                     wacc=p['wacc'], g_term=p['g_term'], net_cash=net_cash, tax=tax, years=years)
        ps = r['equity'] / shares
        w += p['prob'] * ps
        print(f"{ad:16}{ps:>11.2f}{ps/price-1:>10.1%}{p['prob']:>10.0%}")
    print("-" * 48)
    print(f"{'Ağırlıklı adil değer:':16}{w:>11.2f}{w/price-1:>10.1%}")
    return w
