# Underwriting — TURSG (Türkiye Sigorta A.Ş.)
**Gün 5 · backlog 2026-07-30** · Fiyat referansı: **6,37 TL** (2026-07-30, Yahoo `TURSG.IS`)

## 1. Künye
| Alan | Değer | Kaynak |
|---|---|---|
| Sektör | Elementer sigorta (lider) | — |
| Ölçek | Büyük (large-cap), devlet kontrollü (TVF/kamu bankaları) | config.tier_map |
| Fiyat (07-30) | 6,37 TL | Yahoo |
| Pay sayısı | 20.000.000.000 (iki 2:1 bedelsiz sonrası) | Yahoo |
| Piyasa değeri | **127,4 mlr TL** | bağımsız hesap |
| Özkaynak (Haz-2026) | ~61 mlr TL → BVPS ~3,05 | TURSG H1'26 |
| Portföydeki ağırlık | %12,9 | logs/nav/latest.json |

## 2. İş modeli
Türkiye'nin en büyük sigorta şirketi; kamu bankaları dağıtım kanalı (bancassurance) ile
güçlü prim üretimi. Kâr iki kaynaktan: (1) **teknik kâr** (prim − hasar − gider),
(2) **yatırım geliri** (prim float'unun yüksek faizde değerlenmesi).
- **Avantaj:** pazar lideri, kamu banka kanalı, devasa float, yüksek faizde güçlü yatırım
  geliri; **çok yüksek ROE (~%48)**.
- **Riskler:** **ROE dezenflasyonla normalleşir** (yatırım geliri düşer) — ana risk;
  hasar/enflasyon (özellikle oto/sağlık), regülasyon, deprem katastrof riski.

## 3. Son çeyrek finansalları (KAP)
| Dönem | Brüt prim | Net kâr | Not | Kaynak |
|---|---:|---:|---|---|
| 2Ç26 | 40,4 mlr | **7,0 mlr** (beklenti 6,4 üstü) | H1 net kâr +%44 YoY | CNBC-e / KAP |
| 1Ç26 | 23,5 mlr | 6,43 mlr | | GCM/KAP |
| H1'26 | 94,2 mlr | **13,43 mlr** | özkaynak 61 mlr, ROE **~%48** | KAP |

Aktif 193,3 mlr; sektör liderliği sürüyor.

## 4. Bağımsız çarpanlar (fiyat 6,37; pay 20 mlr → PD 127,4 mlr)
| Çarpan | Hesap | Değer |
|---|---|---|
| **İleri F/K** | 127,4 mlr / (H1×2×0,95 ≈ 25,5 mlr) | **~5,0x** |
| F/K (TTM) | 6,37 / 1,07 | 6,0x |
| **P/B** | 6,37 / 3,05 | **2,09x** |
| **ROE** | — | **~%48** (normalleşecek) |

*Sigortacıda FD/FAVÖK ve FCF anlamsız; F/K, P/B, ROE ve sürdürülebilir kârlılık esastır.*

## 5. Değerleme — artık gelir / haklı P/B (`TURSG_ina.py`)
Haklı P/B = (ROE_sürdürülebilir − g)/(Ke − g); 2 aşamalı artık gelir (yüksek ROE'nin fade'i).
| Senaryo | Terminal ROE | Adil değer (TL) | Yükseliş | Olasılık |
|---|---:|---:|---:|---:|
| Bear | %16 | 5,46 | −14,2% | 30% |
| Base | %22 | 8,67 | +36,1% | 45% |
| Bull | %28 | 13,37 | +109,9% | 25% |
| **Ağırlıklı** | | **8,88** | **+39,4%** | |

Çapraz kontrol (ileri F/K): 5x → 6,38 TL (≈ bugün), **7x → 8,93 TL** (+%40). İki yöntem
~8,7-8,9 TL'de buluşuyor.

## 6. Tez revizyonu
Açılış tezi ("ucuz, yüksek-ROE, lider sigortacı") **doğrulandı**; H1 kârı +%44 ve ROE %48
teze destek. Tek ciddi risk **ROE normalleşmesi** — senaryolarda modellendi (terminal ROE
%16-28). Underwriting **GEÇTİ**.

## 7. Karar: **BÜYÜT** → hedef ağırlık ~%14,8 (tek-makro limiti %15'in hemen altında)
- İleri F/K ~5x, ROE ~%48, lider konum, iki yöntemde de ~%40 yukarı → güçlü risk/getiri.
- **Disiplin:** sigortacı = faiz/makroya duyarlı; **tek-makro-senaryo %15 limiti** nedeniyle
  ağırlığı **%15'in altında** tutuyorum.
- **İşlem:** +1.500 adet @ ~6,37 (≈9.555 TL); ağırlık %12,9 → ~%14,8.
- Hedef ~8,8 TL; invalidation: terminal ROE'nin sürdürülebilir <%15'e işaret etmesi
  (yatırım geliri çöküşü) veya birleşik rasyonun bozulması (teknik zarar).

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
