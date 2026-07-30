# Underwriting — MPARK (MLP Sağlık Hizmetleri A.Ş. / Medical Park)
**Gün 4 · backlog 2026-07-30** · Fiyat referansı: **404,75 TL** (2026-07-30, Yahoo `MPARK.IS`)

## 1. Künye
| Alan | Değer | Kaynak |
|---|---|---|
| Sektör | Özel hastane / sağlık hizmetleri | — |
| Ölçek | Orta (mid-cap) | config.tier_map |
| Fiyat (07-30) | 404,75 TL | Yahoo |
| Pay sayısı | 102.122.233 | Yahoo |
| Piyasa değeri | **41,3 mlr TL** | bağımsız hesap |
| Net borç | ~15,1 mlr TL (~1,0x FAVÖK) | Yahoo |
| Portföydeki ağırlık | %12,5 | logs/nav/latest.json |

## 2. İş modeli
Türkiye'nin en büyük özel hastane grubu (Medical Park, Liv, VM). Yatak × doluluk × işlem
karması ile gelir; ödeyiciler SGK + özel sigorta + cepten + **yurtdışı hasta (medikal
turizm, döviz geliri)**.
- **Avantaj:** ölçek, marka, yüksek FAVÖK marjı (~%28), **medikal turizmde döviz tahsilatı**
  (kur/enflasyon hedge'i), yaşlanan nüfus + özel sağlığa yapısal talep.
- **Riskler:** SGK fiyat ayarlamaları/regülasyon, personel maliyeti, kaldıraç (net borç ~1x
  FAVÖK), kapasite yatırımı.

## 3. Son çeyrek finansalları (KAP / İş Yatırım)
| Dönem | Hasılat | FAVÖK | Net kâr | Kaynak |
|---|---:|---:|---:|---|
| 1Ç26 | 16,25 mlr (+%6) | 4,8 mlr (marj iyileşti) | 1,67 mlr (beklenti üstü, +%9) | İş Yat. |
| FY25 | 55,1 mlr | — | 5,54 mlr | Yahoo |
| FY24 | 39,7 mlr | — | 5,21 mlr | Yahoo |
| TTM | 55,1 mlr | 15,22 mlr (%27,6) | ~3,0 mlr¹ | Yahoo |

¹ TTM net kâr Yahoo trailingEps 29,71 × pay ≈ 3,03 mlr (enflasyon muhasebesi etkisi).
Bilanço sonrası cadde hedefleri **640 TL'ye** kadar yükseldi.

## 4. Bağımsız çarpanlar (fiyat 404,75; pay 102,1 mn → PD 41,3 mlr)
| Çarpan | Hesap | Değer |
|---|---|---|
| F/K (TTM) | 404,75 / 29,71 | 13,6x |
| **FD/FAVÖK (TTM)** | (41,3 + 15,1) / 15,22 | **~6,2x** |
| P/B | 404,75 / 209,45 | 1,93x |
| ROE | — | **~%20,5** |

FD/FAVÖK ~6x + ROE %20 + büyüme → **ucuz büyüme** profili.

## 5. 3 senaryolu İNA (`MPARK_ina.py`, reel FCFF, WACC %11-14)
| Senaryo | Hisse (TL) | Yükseliş | Olasılık |
|---|---:|---:|---:|
| Bear | 415,04 | +2,5% | 30% |
| Base | 772,73 | +90,9% | 45% |
| Bull | 1.231,59 | +204% | 25% |
| **Ağırlıklı** | **780,14** | **+92,7%** | |

**Üçgenleme:** İNA base'i (+91%) cadde hedeflerinin (+58%, 640 TL) üstünde; ihtiyaten
adil değeri **~600-750 TL** aralığına çekiyorum → yine de belirgin **düşük değerleme**.
Aşağı yön Bear'da bile ~fiyat civarı (korumalı).

## 6. Tez revizyonu
Açılış tezi ("ucuz, büyüyen, döviz-gelirli lider hastane grubu") **güçlü doğrulandı**.
Underwriting **GEÇTİ**.

## 7. Karar: **BÜYÜT** → hedef ağırlık ~%15,5 (mid-cap katmanı limit içinde)
- FD/FAVÖK ~6x, ROE %20, medikal turizm döviz katalizörü, cadde ve İNA belirgin yukarı →
  yeni para için en iyi risk/getiri adaylarından.
- **İşlem:** +36 adet @ ~404,75 (≈14.571 TL); ağırlık %12,5 → ~%15,5.
- Limit kontrolü: mid-cap katmanı (MAVI+MPARK) ~%31 < %40; tek isim <%20. ✓
- Hedef ~650 TL; invalidation: FAVÖK marjının <%22'ye gerilemesi veya net borcun >2x FAVÖK.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
