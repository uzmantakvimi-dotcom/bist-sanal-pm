# Underwriting — CCOLA (Coca-Cola İçecek A.Ş.)
**Gün 2 · backlog 2026-07-30** · Fiyat referansı: **91,5 TL** (2026-07-30, Yahoo `CCOLA.IS`)

## 1. Künye
| Alan | Değer | Kaynak |
|---|---|---|
| Sektör | Alkolsüz içecek şişeleme (Coca-Cola sistemi) | — |
| Ölçek | Büyük (large-cap) | config.tier_map |
| Fiyat (07-30) | 91,5 TL | Yahoo |
| Pay sayısı | 2.798.078.602 | Yahoo |
| Piyasa değeri | **256,0 mlr TL** | bağımsız hesap |
| Net borç | ~26,4 mlr TL (borç 51,66 − nakit 25,26) | Yahoo financialData |
| Portföydeki ağırlık | %15,6 | logs/nav/latest.json |

## 2. İş modeli
Coca-Cola İçecek, Coca-Cola markalarının Türkiye + Orta Asya + Pakistan + Orta Doğu'da
(11 ülke) münhasır şişeleyicisi. Konsantre TCCC'den alınır; CCI üretim, dağıtım ve satışı
yapıp hacim × fiyat/karma ile gelir üretir.
- **Avantaj:** Coğrafi çeşitlilik (hacmin çoğu Türkiye dışı → **doğal döviz hedge'i**),
  dağıtım ağı, marka. Enflasyonda fiyatlama gücü.
- **Riskler:** hammadde/kur, tüketici harcaması, düzenleme/vergi, boykot gürültüsü
  (1Ç'de rakamlara yansımadı).

## 3. Son çeyrek finansalları (KAP / İş Yatırım)
| Dönem | Hasılat | FAVÖK (marj) | Net kâr | Kaynak |
|---|---:|---:|---:|---|
| 1Ç26 | 52,4 mlr (+%10,7) | 9,0 mlr (%17,8) | 5,2 mlr (+%214) | İş Yat./Bloomberg HT |
| FY25 | 187,2 mlr | — | 14,07 mlr | Yahoo |
| FY24 | 137,7 mlr | — | 14,81 mlr | Yahoo |
| TTM | 192,2 mlr | 35,63 mlr (%18,5) | ~17,6 mlr | Yahoo |

1Ç26 operasyonel olarak çok güçlü (marj +490bp, net kâr +%214). Sonraki bilanço 10 Ağu 2026.

## 4. Bağımsız çarpanlar (fiyat 91,5; pay 2,798 mlr → PD 256,0 mlr)
| Çarpan | Hesap | Değer |
|---|---|---|
| F/K (TTM) | 91,5 / 6,30 | **14,5x** |
| FD/FAVÖK (TTM) | (256,0 + 26,4) / 35,63 | **7,9x** (ileri ~6,5x)¹ |
| P/B | 91,5 / 29,82 | 3,07x |
| ROE | — | ~%22 |

¹ 1Ç FAVÖK +%54 büyürken TTM FAVÖK geriden geliyor; **ileri** FD/FAVÖK belirgin daha düşük.

## 5. 3 senaryolu İNA (`CCOLA_ina.py`, reel FCFF, WACC %11-14)
| Senaryo | Hisse (TL) | Yükseliş | Olasılık |
|---|---:|---:|---:|
| Bear | 35,12 | −61,6% | 30% |
| Base | 66,82 | −27,0% | 45% |
| Bull | 98,84 | +8,0% | 25% |
| **Ağırlıklı** | **65,31** | **−28,6%** | |

**Uyarı:** İNA **TTM (geriye dönük)** FAVÖK'ten başlıyor; 1Ç'deki +%54'lük sıçrama modele
tam yansımıyor, bu yüzden İNA muhafazakâr. İleri FAVÖK'le değerleme daha makul (~fair value).

## 6. Tez revizyonu
Açılış tezi ("kaliteli, döviz-çeşitlendirilmiş defansif şişeleyici") **doğrulandı**;
operasyonel momentum güçlü. Ancak değerleme **ucuz değil** (FD/FAVÖK ~8x, P/B 3,1x).
Underwriting **GEÇTİ** (kaliteli defansif çıpa).

## 7. Karar: **TUT** (%15,6'da koru — işlem yok)
- KAPAT/KIRP değil: kaliteli, momentumlu, döviz-hedge'li defansif çekirdek pozisyon.
- BÜYÜT değil: geriye ve ileriye dönük çarpanlar "adil-dolu" bölgede; yeni parayı daha
  ucuz/yüksek-ROE isimlere (MPARK, TURSG) yönlendiriyorum.
- Hedef çıpa ~85-95 TL (adil). Invalidation: FAVÖK marjının tekrar <%14'e dönmesi veya
  net borcun >1,5x FAVÖK'e çıkması.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
