# Underwriting — MAVI (Mavi Giyim Sanayi ve Ticaret A.Ş.)
**Gün 1 · 2026-07-20** · Fiyat referansı: **41,02 TL** (2026-07-17 kapanış, Yahoo `MAVI.IS`)

## 1. Künye
| Alan | Değer | Kaynak |
|---|---|---|
| Sembol | MAVI.IS (BIST) | — |
| Sektör | Hazır giyim perakendesi (denim odaklı) | — |
| Ölçek | Orta (mid-cap) | config.tier_map |
| Fiyat (2026-07-17) | 41,02 TL | Yahoo chart API |
| Pay sayısı | 783.604.542 | Yahoo defaultKeyStatistics |
| Piyasa değeri | **32,14 mlr TL** (41,02 × 783.604.542) | bağımsız hesap |
| Mali yıl | Şubat–Ocak (çeyrekler Nis/Tem/Eki/Oca sonu) | KAP |
| Portföydeki ağırlık | **%16,2** (kitabın en büyüğü) | logs/nav/latest.json |

## 2. İş modeli (kendi kelimelerimle)
Mavi, kendi markası altında ağırlıklı denim (jean) ve tamamlayıcı hazır giyim satan,
dikey-entegre olmayan ama **marka + perakende** ağırlıklı bir giyim şirketi. Para kazanma
mantığı basit: tasarım/marka değeriyle yüksek brüt marj (~%53 ticari brüt kâr), bunu
kendi mağazaları + bayiler + e-ticaret + yurtdışı (özellikle ABD/Almanya) kanallarıyla
ölçekleyip FAVÖK'e çeviriyor.
- **Rekabet avantajı:** Türkiye denim segmentinde lider marka bilinirliği, güçlü mağaza
  ağı ve fiyat-değer konumlaması; enflasyonist ortamda fiyatlama gücü.
- **Bilanço:** **Net nakit** pozisyonu (leasing hariç ~7,0 mlr TL = piyasa değerinin %22'si)
  — perakendede nadir; downside koruması ve büyüme/temettü opsiyonu sağlıyor.
- **Riskler:** (1) Türk tüketicisinin reel harcama gücü — 1Ç26'da reel hasılat **-%2 YoY**
  daralması talep yumuşamasının erken sinyali. (2) TMS 29 enflasyon muhasebesi kâr
  kalitesini bulanıklaştırıyor. (3) Yurtdışı büyümede kur/talep. (4) Moda/stok riski.

## 3. Son çeyrek(ler) KAP finansalları
> **Uyarı:** MAVI mali yılı Şubat–Ocak; ayrıca TMS 29 (yüksek enflasyon muhasebesi)
> geçmiş dönemleri yeniden ifade ettiği için **tek-çeyrek** kırılımı gürültülü. Aşağıda
> en sağlam kaynaklı veriler ve yıllık/TTM toplamlar birlikte verilmiştir.

**Tek çeyrek (nominal, açıklanan):**
| Çeyrek | Dönem | Hasılat (mn TL) | FAVÖK (mn TL) | Net kâr (mn TL) | Kaynak |
|---|---|---:|---:|---:|---|
| 1Ç FY27 | Şub–Nis 2026 | **12.701** | **2.414** (%19,7) | **543** | Ziraat Yat./şirket/İş Yat. |
| 4Ç FY26 | Kas 2025–Oca 2026 | 14.149 | n/a¹ | n/a¹ | Yahoo (tek çeyrek) |
| 3Ç FY26 | Ağu–Eki 2025 | 12.156 | n/a¹ | n/a¹ | Yahoo (tek çeyrek) |
| 2Ç FY26 | May–Tem 2025 | ~8.5² | n/a¹ | n/a¹ | TTM'den türetildi² |

¹ Yahoo tek-çeyrek FAVÖK/net kâr alanları tutarsız (sıfır/eksik) döndüğü için
  çeyrek bazında raporlanmadı; toplamlar aşağıda. ² TTM 47,5 mlr − (12,70+14,15+12,16).

**Yıllık (Yahoo, mali yıl Oca sonu) ve TTM:**
| Dönem | Hasılat (mn TL) | Net kâr (mn TL) |
|---|---:|---:|
| FY24 (Oca 2024) | 26.293 | 1.784 |
| FY25 (Oca 2025) | 38.519 | 2.724 |
| FY26 (Oca 2026) | 47.729 | 2.294 |
| **TTM** | **~47.500** | **~1.841** (EPS 2,35) |

- 1Ç26 net nakit: **7.037 mn TL** (leasing hariç, şirket açıklaması).
- İş Yatırım (TMS29 yeniden ifade) 12-ay hasılatı 52,19 mlr TL veriyor; Yahoo nominal
  47,7 mlr ile fark **enflasyon düzeltmesinden** kaynaklanıyor — çarpanlarda dikkate alındı.

## 4. Bağımsız hesaplanmış çarpanlar
Kaynak fiyat **41,02 TL**, pay sayısı **783.604.542** → piyasa değeri **32,14 mlr TL**.

| Çarpan | Hesap | Değer |
|---|---|---|
| **F/K (TTM)** | 41,02 / 2,35 | **17,5x** |
| **F/K (son FY26)** | 41,02 / (2.294/783,6=2,93) | **14,0x** |
| **FD/FAVÖK** | (32,14 − 7,04 net nakit)=25,10 / 6,44 | **3,9x** |
| FD/FAVÖK (muhafazakâr, leasing dahil net nakit 3,9) | 28,24 / 6,44 | 4,4x |
| **P/B** | 41,02 / 17,48 (defter değeri/pay) | **2,35x** |
| ROE (TTM, ima) | 2,35 / 17,48 | ~%13,4 |
| **FCF verimi** (tahmini) | FCFF≈3,6–4,2 mlr / 32,14 mlr (bkz. MAVI_ina.py) | **~%9–13** |
| **PEG** | — | **anlamsız**³ |

³ Nominal TL kârlar enflasyonla şiştiği için PEG yanıltıcı; büyüme İNA'da **reel**
  terimlerle senaryolaştırıldı.

**Okuma:** FD/FAVÖK ~4x ve F/K 14–17x, net nakit %22 tamponuyla birlikte, kaliteli bir
markalı perakendeci için **ucuz** aralıkta. Ana soru büyüme değil, reel talebin
korunup korunmayacağı.

## 5. 3 senaryolu basit İNA
Kod: `logs/underwriting/MAVI_ina.py` (reel FCFF, 5 yıl + Gordon terminal, varsayımlar değişken).

| Senaryo | Reel büyüme | FAVÖK marjı | Reel WACC | Hisse (TL) | Yükseliş | Olasılık |
|---|---:|---:|---:|---:|---:|---:|
| Bear | %0 | %13,0 | %16,0 | **38,82** | −5,4% | 30% |
| Base | %4 | %15,0 | %14,0 | **57,28** | +39,6% | 45% |
| Bull | %8 | %17,0 | %12,5 | **84,51** | +106% | 25% |
| **Olasılık-ağırlıklı** | | | | **58,55** | **+42,7%** | |

Muhafazakâr net nakit (leasing dahil, 3,9 mlr) ile: Bear 34,82 / Base 53,28 / Bull 80,51 TL.

**Asimetri:** Aşağı yön Bear'da bile ~−5% (muhafazakârda ~−15%), taban +40%. Net nakit
tabanı zararı sınırlıyor; taban ve boğa senaryoları anlamlı yukarı opsiyon sunuyor.

## 6. Tez revizyonu
Açılış tezi ("ucuz, net nakitli, kaliteli markalı perakendeci") **doğrulandı**. Tek
zayıflık: 1Ç26'da **reel hasılat −%2** — talep yumuşaması izlenmeli; tez bozucu değil ama
sarı bayrak. Underwriting **GEÇTİ** (mandate: geçemeyen pozisyon fiyattan bağımsız kapatılır).

## 7. Karar: **TUT** (mevcut %16,2 ağırlıkta koru — boyut değişikliği YOK)
**Gerekçe:**
- Değerleme cazip (FD/FAVÖK ~4x, taban İNA +40%, net nakit %22 tampon) → **KAPAT/KIRP değil.**
- **BÜYÜT'ü şimdilik reddediyorum:** pozisyon zaten kitabın en büyüğü (%16,2) ve tek-isim
  %20 limitine yakın; ayrıca 1Ç26 reel talep daralması yeni parayı beklemeyi haklı kılıyor.
  Konsantrasyonu tüketici-harcamasına daha da yığmak, bu aşamada risk-getiri açısından
  gereksiz.
- **Boyut değişikliği gerektirmiyor → işlem yok.** Statü `UNDERWRITE_BEKLIYOR` → **`TUT (onaylı)`**.

**Hedef ve tetikleyiciler:**
- Adil değer çıpası: **~57 TL** (Base). Hedefe gelirse mandate gereği satış değerlendirilir.
- **BÜYÜT tetikleyicisi** (→ %18–19'a): ~37 TL altına geri çekilme **veya** 2Ç FY27
  sonuçlarında reel talebin stabilize olduğunun teyidi.
- **Invalidation:** reel hasılatın iki çeyrek üst üste daralması + FAVÖK marjının
  <%12'ye gerilemesi **veya** net nakit pozisyonunun kaybı → tez yeniden yazılır.

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
