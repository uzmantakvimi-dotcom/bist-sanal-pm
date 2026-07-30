# Underwriting — ENKAI (Enka İnşaat ve Sanayi A.Ş.)
**Gün 3 · backlog 2026-07-30** · Fiyat referansı: **87,05 TL** (2026-07-30, Yahoo `ENKAI.IS`)

## 1. Künye
| Alan | Değer | Kaynak |
|---|---|---|
| Sektör | Taahhüt + enerji + gayrimenkul + yatırım portföyü (holding) | — |
| Ölçek | Büyük (large-cap) | config.tier_map |
| Fiyat (07-30) | 87,05 TL | Yahoo |
| Pay sayısı | 5.862.743.582 | Yahoo |
| Piyasa değeri | **510,4 mlr TL** | bağımsız hesap |
| **Net nakit** | **~213 mlr TL** ($5,32 mlr, 1Ç26) = PD'nin **~%42'si** | ENKA 1Ç26 / Yahoo |
| Portföydeki ağırlık | %13,6 | logs/nav/latest.json |

## 2. İş modeli
Dört ayak: (1) **uluslararası taahhüt** (Orta Asya/Irak/Afrika altyapı), (2) **Enka Enerji**
(doğalgaz santralleri), (3) **gayrimenkul** (Moskova ofis/AVM + Türkiye), (4) devasa
**nakit + yatırım portföyü**. Değerin büyük kısmı bilançodaki nakit/yatırımlardan gelir.
- **Avantaj:** kale gibi bilanço ($5,3 mlr net nakit), döviz varlıkları, çeşitlilik →
  yüksek **güvenlik marjı**; ayı piyasasında koruyucu.
- **Zayıflık:** nakit yükü **ROE'yi baskılıyor (~%12)** — bileşik büyüme sınırlı; net kâr
  yatırım gelirine bağlı oynak (1Ç26 net kâr YoY düştü, beklenti altı).

## 3. Son çeyrek finansalları (KAP / İş Yatırım)
| Dönem | Hasılat | FAVÖK/Op. kâr | Net kâr | Kaynak |
|---|---:|---:|---:|---|
| 1Ç26 | 35,83 mlr (+%20) | FAVÖK 8,06 / op. 6,48 mlr (+%20) | 3,41 mlr (↓, 1Ç25: 3,86) | İş Yat./Foreks |
| TTM | 156,5 mlr | FAVÖK 33,95 mlr (%21,7) | — | Yahoo |
| Net nakit | $5,32 mlr (1Ç26) vs $5,56 mlr (4Ç25) | | | ENKA |

Aktif 507 mlr, yükümlülük 115,5 mlr → özkaynak ~391 mlr. Bir aracı kurum AL→TUT'a çekti.

## 4. Bağımsız çarpanlar (fiyat 87,05; pay 5,863 mlr → PD 510,4 mlr)
| Çarpan | Hesap | Değer |
|---|---|---|
| F/K (TTM) | 87,05 / 6,33 | 13,7x |
| **P/B** | 87,05 / 63,66 | **1,37x** |
| FD/FAVÖK | (510,4 − 213) / 33,95 | **8,8x** (operasyon, nakit hariç) |
| ROE | — | ~%12 |

**Okuma:** 510 mlr'a ~213 mlr nakit + operasyonlar (taahhüt+enerji+GYO, FAVÖK ~34 mlr)
alınıyor. Operasyonlar ~%8,8 FD/FAVÖK — ucuz değil; ama nakit + gayrimenkul varlık desteği güçlü.

## 5. 3 senaryolu İNA (`ENKAI_ina.py`, reel FCFF + net nakit köprüsü)
| Senaryo | Hisse (TL) | Yükseliş | Olasılık |
|---|---:|---:|---:|
| Bear | 55,13 | −36,7% | 30% |
| Base | 70,82 | −18,7% | 45% |
| Bull | 91,30 | +4,9% | 25% |
| **Ağırlıklı** | **71,23** | **−18,2%** | |

İNA operasyonları + tüm net nakiti içeriyor; yine de sınırlı yukarı yön çıkıyor —
yani piyasa operasyonları zaten dolu fiyatlıyor. Aşağı yönü nakit/varlık tabanı koruyor.

## 6. Tez revizyonu
Açılış tezi ("kale bilanço, güvenlik marjı") **doğrulandı** ama **düşük ROE + adil-dolu
operasyon değerlemesi** getiri sürücüsü olmasını engelliyor. Underwriting **GEÇTİ**
(defansif değer/balast).

## 7. Karar: **TUT** (%13,6'da koru — işlem yok)
- KAPAT değil: P/B 1,37x ve %42 net nakit güçlü güvenlik marjı; portföy balastı.
- BÜYÜT değil: düşük ROE (~%12) ve operasyonların adil fiyatı, %100 hedefi için yeni parayı
  hak etmiyor; nakidi daha yüksek getiri/ucuz isimlere ayırıyorum.
- Invalidation: net nakit pozisyonunun kaybı veya taahhüt backlog'unda kalıcı daralma.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
