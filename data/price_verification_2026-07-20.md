# Fiyat Teyidi — 2026-07-20 (Pazartesi ilk iş)

**Amaç:** Giriş fiyatları 16-17 Temmuz haber verisinden alınmıştı. Gerçek piyasa
fiyatlarıyla karşılaştırılıp sapmalar düzeltme işlemi olarak loglandı (mandate 4.3:
eski kayıt silinmez). Kaynak: Yahoo Finance chart API (`*.IS`), proxy + CA bundle ile.
Son doğrulanabilir kapanış: **2026-07-17 (Cuma)**.

| Hisse | Kayıtlı giriş (haber) | Teyit (16 Tem gerçek) | Güncel (17 Tem kapanış) | Sonuç |
|---|---:|---:|---:|---|
| MAVI  | 41.00  | 41.00  | 41.02  | ✅ Tutarlı |
| CCOLA | 90.00  | 90.00  | 87.55  | ✅ Tutarlı |
| ENKAI | 92.15  | 92.15  | 90.70  | ✅ Tutarlı |
| MPARK | 429.50 | 429.50 | 415.50 | ✅ Tutarlı |
| **TURSG** | **13.10** | **6.65** | **6.56** | ❌ **Sapma -%49.6 → düzeltildi** |

## TURSG bölünme bulgusu (pay sayısı / fiyat tutarlılığı)
- Yahoo `events.splits` kaydı: iki adet **2:1 bedelsiz** (numerator 200 / denominator 100):
  ~2025-08-28 ve **~2026-06-13**.
- Haber girişindeki ~13.10 fiyat, **Haziran 2026 bedelsizinden önceki (stale)** bir
  kotasyona denk geliyordu; gerçek bölünme-sonrası fiyat ~6.6.
- **Tutarsızlık:** 4.962 adet × 6.56 = 32.551 TL → pozisyon değeri **yarı yarıya
  eksik** görünüyordu (NAV'da ~32.5k TL / kitabın %6.5'i kadar eksiklik).
- **Düzeltme (nakit-nötr, maliyet tabanı korundu):** adet 4.962 → **9.924**,
  ort. maliyet 13.10 → **6.55**, cost_basis 64.992,20 TL sabit.
  İşlem: `execute_trade.py CORRECTION` (ledger'da 2026-07-20). Eski BUY kaydı **duruyor**.
- Düzeltme sonrası TURSG değeri 9.924 × 6.56 = 65.101 TL, PnL +%0.2 → tutarlı.

## NAV etkisi
| | Düzeltme öncesi | Düzeltme sonrası |
|---|---:|---:|
| NAV | 462.341 TL | **494.891 TL** |
| Toplam getiri | -%7.53 | **-%1.02** |
| XU100 (kuruluş 16 Tem = 14.251,30) | -%1.90 | -%1.90 |
| Alpha | -%5.63 | **+%0.87** |

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
