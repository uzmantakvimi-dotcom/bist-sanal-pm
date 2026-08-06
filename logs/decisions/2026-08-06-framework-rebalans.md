# Karar Günlüğü — 2026-08-06 (Framework purist rebalans)

Sahibin yeni `framework.md` çerçevesi (kalite-bileşikçi @ değer) uygulandı. Skorkart:
`logs/underwriting/framework_scorecard_2026-08-06.md`. Seçim: **purist / tam rebalans**.

## Uygulama
Kritik geçitlerde (net marj>%20, ROE>%25, D/E<0,8, F/K<20, PEG<0,5) kalan **her** isim kapatıldı.
Sadece çerçeveden geniş geçen **TURSG** (core) ve çerçeve-dışı **SDTTR** (opportunistic muaf) kaldı.

### BIST satışları (2026-08-06)
| İsim | Gerekçe (fail) | Realize P&L |
|---|---|---:|
| MAVI | net %3,9, ROE %11 | −4.877,50 |
| CCOLA | brüt<40, net<20, ROE<25, PEG | −1.707,65 |
| ENKAI | brüt<40, ROE<25, FCF, PEG | −3.838,00 |
| MPARK | brüt<40, net<20, ROE<25, FCF | −3.503,50 |
| **Toplam realize** | | **−13.926,65** |

Kalan: **TURSG %14,7** (core, 5/6 geçer) + **SDTTR %5,3** (opportunistic). **Nakit %80,0.**
BIST NAV 483.657 TL (−%3,27) · XU100 −%3,85 · alpha +0,58.

### US satışları (2026-08-06)
PEP (net<20, D/E 2,39, FCF, PEG), V (P/E 31,5 / PEG 1,66 / FCF — kaliteli ama pahalı),
EYE (net<20, ROE<25, P/E>20). Realize ≈ +1,84 net. **US artık %100 nakit**, NAV $10.001,83.

## Neden bu kadar sert?
Çerçeve kasıtlı çok katı; F/K<20 **ve** PEG<0,5 **ve** ROE>%25 **ve** net marj>%20 aynı anda
neredeyse hiçbir isimde yok. Purist uygulama → çoğu isim çıkar, nakit yükselir. Bu, çerçevenin
doğası (framework.md uyarısı).

## Sıradaki: redeploy
- Nakit (BIST %80, US %100) ancak **11/13 geçen** isimlerle konuşlandırılacak.
- Bu isimleri bulmak için daha zengin veri gerekiyor (D&A/brüt, faiz/op, LTD/NI, capex/NI,
  EPS 10Y, geri alım, insider, kılavuz) → FMP/Finnhub/EDGAR MCP entegrasyonu önerildi.
- O zamana kadar disiplin: çerçeveyi geçmeyen isme geri dönülmez.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
