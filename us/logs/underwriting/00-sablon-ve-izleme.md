# US Underwriting Şablonu ve İzleme Listesi

Her pozisyon, alınmadan önce bir underwriting belgesiyle gerekçelendirilir.
Kaynak önceliği: **SEC EDGAR (10-K/10-Q) > IR > analist (çapraz) > haber**.

## Zorunlu şablon (TICKER.md)
1. **Künye** — sembol, sektör (GICS), fiyat (tarih), pay sayısı, piyasa değeri.
2. **İş modeli** — kendi kelimelerinle; nasıl para kazanıyor, hendek (moat), riskler.
3. **Son 4 çeyrek finansalları** — 10-Q/10-K tablosu (hasılat, FAVÖK/op. kâr, net kâr, FCF).
4. **Bağımsız çarpanlar** — F/K, FD/FAVÖK, **FCF verimi**, PEG, ROIC (kaynak fiyat + pay sayısı yazılı).
5. **3 senaryolu USD FCFF İNA** — `TICKER_ina.py` (nominal WACC ~%9-11, varsayımlar değişken).
6. **Tez revizyonu** ve **Karar**: AL / ALMA (aday) · sonra TUT / BÜYÜT / KIRP / KAPAT.

## İzleme listesi — underwrite edilecek adaylar (arketip → örnek)
> Bunlar **öneri değil**, sürecin uygulanacağı adaylardır. Her biri canlı 10-K/İNA ile test edilecek.

| # | Katman / arketip | Örnek aday | Aranan nitelik |
|---|---|---|---|
| 1 | Bileşikçi getiri sürücüsü | GOOGL / MSFT | Yüksek ROIC, net nakit, güçlü FCF, makul F/K, opsiyonellik |
| 2 | "Toll-road" ağ etkisi | V / MA | %50+ marj, düşük sermaye yoğunluğu, sekülar nakitsizleşme |
| 3 | Kaliteli defansif çıpa | COST / PEP | Fiyatlama gücü, savunmacı FCF (CCOLA analogu) |
| 4 | Ucuz değer + katalizör | (mid-cap sağlık/sanayi/enerji) | FD/FAVÖK iskontosu + somut katalizör |
| 5 | Bilanço balastı / opsiyonellik | (net-nakitli, geri-alım yapan) | Düşük borç, aşağı yön koruması (ENKA analogu) |
| 6 | İkinci getiri sürücüsü (GARP) | (sekülar büyüyen yazılım/sağlık) | Yüksek büyüme + pozitif FCF, makul PEG |

**Plan:** Gün 1'den itibaren günde 1-2 aday underwrite; geçenler `execute_trade.py` ile açılır.
Tek isim ≤%15, sektör ≤%30, tema ≤%20, nakit ≥%5.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
