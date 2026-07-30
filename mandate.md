# mandate.md — Anayasa (BIST Sanal Portföy)

Bu belge portföyün anayasasıdır. CLAUDE.md operasyonel talimatları buradan türer;
çelişki halinde **mandate.md üstündür**. Değişiklik ancak yeni bir kayıtla (commit) yapılır;
geçmiş silinmez.

## 1. Amaç ve çerçeve
- **500.000 TL sanal (kağıt) portföy**, gerçek para yok.
- **Süre:** 12 ay (kuruluş 16 Temmuz 2026 → 16 Temmuz 2027).
- **Hedef:** 12 ayda **%100 nominal getiri** (kümülatif enflasyondan arındırılmış reel performans da raporlanır).
- **Benchmark:** BIST 100 (XU100). Başarı, hedefe ulaşmak **ve** benchmark'ı geçmektir.
- Bu bir **kamuya açık şeffaflık deneyidir**: git geçmişi denetim izidir.

## 2. Yatırım felsefesi
- Discretionary, temel-analiz odaklı, yoğunlaştırılmış (concentrated) kitap.
- Her pozisyon bir **underwriting** (yüklenim) belgesiyle gerekçelendirilir. Underwriting'i
  geçemeyen pozisyon, fiyatından bağımsız olarak kapatılır.
- Karar dili "şunu al" değil, "**bu portföy şu kararı verdi ve gerekçesi budur**" biçimindedir.

## 3. Risk limitleri (pazarlık edilemez)
| Limit | Kural |
|---|---|
| Tek pozisyon | maks **%20** |
| Nakit | min **%5** |
| Orta ölçek katmanı (mid-cap) | maks **%40** |
| Tek makro senaryoya bağımlı toplam ağırlık | maks **%15** |
| Evren | yalnızca **BIST 100 içi likit** hisseler |

- Spekülatif / manipülasyona açık isimler yasak.
- Hedef fiyata gelen pozisyon satılır; hedef revizyonu **yalnızca yeni yazılı underwriting** ile.

## 4. Sert kurallar
1. `portfolio.json` **asla elle düzenlenmez**; yalnızca `scripts/execute_trade.py` ile değişir.
2. **Look-ahead yok:** karar, o gün mevcut veriyle verilir ve **aynı gün commit'lenir**.
3. Geçmiş log/commit **düzenlenmez**; hata **yeni bir kayıtla** düzeltilir (ör. düzeltme işlemi).
4. Her içerik taslağının sonunda: **"Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir."**

## 5. Veri kaynağı öncelik sırası
1. **KAP** raporları (birincil)
2. Şirket **yatırımcı ilişkileri** sayfası
3. **İş Yatırım / aracı kurum** raporları (çapraz kontrol)
4. Haber özetleri — **asla tek başına** karar dayanağı olmaz.

Fiyat/mark-to-market: `yfinance` → başarısızsa doğrudan Yahoo Finance chart API (proxy/CA ile)
→ `isyatirimhisse` → son çare web araştırması (kaynak loglanır).

## 6. Enflasyon muhasebesi
- Her ay TÜİK TÜFE açıklandığında `config.json` içindeki
  `cumulative_inflation_since_inception` alanı güncellenir (kaynak linkiyle loglanır).
- Türk şirketlerinde TMS 29 (yüksek enflasyon muhasebesi) etkisi çarpan yorumunda dikkate alınır.

## 7. Karar seti (underwriting çıktısı)
`TUT` (koru) · `BÜYÜT` (ağırlık artır) · `KIRP` (ağırlık azalt) · `KAPAT` (çık).

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
