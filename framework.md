# framework.md — Yatırım Çerçevesi (Ortak: US + TR)

Sahibin tanımladığı **kalite-bileşikçi @ değer fiyatı** çerçevesi. Hem BIST hem US kitabı
buna tabidir; `mandate.md` çelişirse **bu belge çarpan seçiminde üsttedir**. Her underwriting
bu skorkartı doldurur; karar skora göre verilir.

## A. Finansal geçitler (hard gates) — 13 kriter
| # | Kriter | Eşik | Kaynak (metrik) |
|---|---|---|---|
| 1 | Brüt marj | **> %40** | grossMargins |
| 2 | Amortisman / brüt kâr | **< %8** | D&A ÷ gross profit |
| 3 | Faiz gideri / faaliyet kârı | **< %15** | interestExpense ÷ operatingIncome |
| 4 | Net kâr marjı | **> %20** | profitMargins |
| 5 | EPS (son 10Y) | **sürdürülebilir büyüme** | yıllık EPS serisi (nitel/tarihsel) |
| 6 | Uzun vadeli borç | **≤ 0,75 × net kâr** | LTDebt ÷ NI ≤ 0,75 |
| 7 | Borç / özkaynak | **< 0,8** | debtToEquity < 80 |
| 8 | Hisse geri alımı | **var** | pay sayısı trendi ↓ / buyback |
| 9 | ROE | **> %25** | returnOnEquity |
| 10 | CAPEX | **< net kârın %50'si** | capex ÷ NI < 0,5 |
| 11 | F/K | **< 20** | trailingPE < 20 |
| 12 | Nakit akışı verimi (FCF) | **> %5** | FCF ÷ piyasa değeri |
| 13 | PEG | **< 0,5** | PEG |

## B. Yönetim geçitleri
- **Yüksek içeriden sahiplik** (insider ownership yüksek).
- **İyi operatör sicili** (uzun dönem sermaye dağıtımı, marj/pay performansı).
- **Kılavuza uyum ≥ %90** (verilen guidance'ı tutturma oranı).

## C. TAM / sektör geçitleri
- Mevcut büyümeyi **5 yıldan uzun** sürdürecek net alan (headroom).
- Şirketin faaliyet gösterdiği **sektör büyüyor**.

## Skorlama ve karar kuralı
- **Finansal skor = geçilen hard gate sayısı / 13.** Yönetim ve TAM ayrıca nitel değerlendirilir.
- **AL/çekirdek (BÜYÜT/AÇ):** finansal ≥ **11/13** **ve** yönetim ✓ **ve** TAM ✓.
- **TUT/izle:** 9-10/13 (birkaç geçit ıskalanmış ama tez sağlam).
- **KIRP:** 7-8/13.
- **KAPAT:** ≤ 6/13 **veya** herhangi bir **kritik** geçidin (net marj, ROE, borç/özkaynak,
  F/K, PEG) ağır ihlali + zayıf tez.

> **Uyarı (dürüstlük):** Bu çerçeve kasıtlı olarak çok katıdır. F/K<20 **ve** PEG<0,5 **ve**
> ROE>%25 **ve** net marj>%20 **ve** brüt marj>%40 aynı anda çok az şirkette bulunur. Sonuç
> genelde: mevcut isimlerin çoğu birkaç geçitte kalır → nakit yükselir → çerçeveden geçen yeni
> isimler bulunana kadar bekle. Bu, kusur değil, çerçevenin doğası.

> Veri notu: bazı geçitler (EPS 10Y, kılavuz %90, TAM, alım-satım geri alımı) tam nicel veri
> gerektirir; ortamda kısmen erişilebilir → nitel/kaynak-loglu değerlendirilir, eksik olanlar
> "veri?" ile işaretlenir. Entegrasyonlar (bkz. sohbet) bu boşlukları kapatır.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
