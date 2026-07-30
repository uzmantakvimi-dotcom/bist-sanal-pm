#!/usr/bin/env python3
"""TURSG_ina.py — Türkiye Sigorta değerleme (sigortacı; DCF yerine artık gelir / haklı P/B).

Sigorta şirketlerinde FCFF anlamsız; özkaynak-getirisi (ROE), özkaynak (defter) ve
sermaye maliyeti üzerinden değerleme yapılır.

    Haklı P/B = (ROE_sürdürülebilir − g) / (Ke − g)      (Gordon/artık gelir)
    Adil fiyat = Haklı P/B × BVPS

Ayrıca 2 aşamalı artık gelir (yüksek yakın-dönem ROE'nin kademeli normalleşmesi) ve
ileri F/K çapraz kontrolü.

Kaynaklar (2026-07-30): fiyat 6,37; pay 20.000.000.000; özkaynak ~61 mlr (Haz-2026) →
BVPS ~3,05. ROE (H1'26 yıllık) ~%48. H1'26 net kâr 13,43 mlr (1Ç 6,43 + 2Ç 7,0), +%44 YoY.
UYARI: mevcut ROE yüksek faiz/yatırım gelirinden besleniyor; dezenflasyonla normalleşir."""
SHARES = 20_000_000_000
PRICE = 6.37
BVPS = 61.0e9 / SHARES          # ~3,05
H1_NI = 13.43e9
FY_NI_EST = H1_NI * 2 * 0.95    # ikinci yarı hafif normalleşme varsayımı

def justified_pb(roe, ke, g):
    return (roe - g) / (ke - g)

def resid_income_2stage(roe_high, years_high, roe_terminal, ke, g, bvps):
    """Yüksek ROE dönemi + terminal artık gelir. Reel terimler."""
    b = bvps
    val = bvps  # başlangıç defter değeri
    for t in range(1, years_high + 1):
        ri = (roe_high - ke) * b          # artık gelir (birim: TL/pay)
        val += ri / (1 + ke) ** t
        b = b * (1 + roe_high * 0.4)       # kârın %60'ı dağıtılır varsayımı, %40 birikir
    # terminal artık gelir (sürdürülebilir)
    ri_term = (roe_terminal - ke) * b
    tv = ri_term / (ke - g)
    val += tv / (1 + ke) ** years_high
    return val

SCEN = {
    "Bear (Ayı)":   dict(roe_high=0.35, roe_term=0.16, ke=0.16, g=0.03, prob=0.30),
    "Base (Taban)": dict(roe_high=0.42, roe_term=0.22, ke=0.15, g=0.03, prob=0.45),
    "Bull (Boğa)":  dict(roe_high=0.48, roe_term=0.28, ke=0.14, g=0.04, prob=0.25),
}

if __name__ == "__main__":
    print(f"TURSG.IS | Fiyat {PRICE:.2f} | BVPS ~{BVPS:.2f} | P/B {PRICE/BVPS:.2f} | "
          f"ileri F/K ~{PRICE*SHARES/FY_NI_EST:.1f}")
    print(f"{'Senaryo':16}{'HaklıP/B':>10}{'ArtıkGelir(TL)':>16}{'Yükseliş':>11}{'Olasılık':>10}")
    w = 0.0
    for ad, p in SCEN.items():
        pb = justified_pb(p['roe_term'], p['ke'], p['g'])   # terminal ROE ile statik haklı P/B
        fv_static = pb * BVPS
        fv_ri = resid_income_2stage(p['roe_high'], 5, p['roe_term'], p['ke'], p['g'], BVPS)
        w += p['prob'] * fv_ri
        print(f"{ad:16}{pb:>10.2f}{fv_ri:>16.2f}{fv_ri/PRICE-1:>10.1%}{p['prob']:>10.0%}")
    print("-" * 63)
    print(f"{'Ağırlıklı adil değer (artık gelir):':40}{w:>8.2f} TL  ({w/PRICE-1:+.1%})")
    print(f"\nÇapraz kontrol — ileri F/K: FY26E net kâr ~{FY_NI_EST/1e9:.1f} mlr; 7x → "
          f"{7*FY_NI_EST/SHARES:.2f} TL/pay; 5x → {5*FY_NI_EST/SHARES:.2f} TL/pay.")
    print("Not: yüksek ROE faiz ortamına bağlı; terminal ROE normalleşmesi ana risk.")
