# Underwriting Takvimi ve Şablonu

Her pozisyon, 31 Temmuz 2026'ya kadar günde bir hisse olacak şekilde yüklenim
(underwriting) belgesiyle gerekçelendirilir. Underwriting'i geçemeyen pozisyon
fiyatından bağımsız kapatılır.

## Takvim

| Gün | Tarih | Hisse | Durum |
|---|---|---|---|
| 1 | 2026-07-20 (Pzt) | **MAVI** | ✅ Yapıldı |
| 2 | 2026-07-21 (Sal) | CCOLA | Bekliyor |
| 3 | 2026-07-22 (Çar) | ENKAI | Bekliyor |
| 4 | 2026-07-23 (Per) | MPARK | Bekliyor |
| 5 | 2026-07-24 (Cum) | TURSG | Bekliyor |
| 6 | 2026-07-30 (Çar) | MIATK (izleme) | Bekliyor |

> Alım kararı **yalnızca** underwriting ile verilir; MIATK izleme listesindedir.

---

## Zorunlu Şablon (HISSE.md)

Her `logs/underwriting/HISSE.md` aşağıdaki bölümleri içermek zorundadır:

1. **Künye** — sembol, sektör, ölçek katmanı, fiyat (tarih), pay sayısı, piyasa değeri.
2. **İş modeli** — kendi kelimelerinle; nasıl para kazanıyor, rekabet avantajı, riskler.
3. **Son 4 çeyrek KAP finansalları** — tablo halinde (hasılat, brüt/FAVÖK, net kâr).
   Kaynak açıkça yazılır (KAP > Yİ sayfası > İş Yatırım > haber).
4. **BAĞIMSIZ hesaplanmış çarpanlar** — F/K, FD/FAVÖK, FCF verimi, PEG.
   *Kaynak fiyat ve pay sayısı yazılı olacak; her çarpan gösterilerek hesaplanır.*
5. **3 senaryolu basit İNA** — `HISSE_ina.py` olarak kodlanır (varsayımlar değişken).
6. **Tez revizyonu** — açılış tezi hâlâ geçerli mi?
7. **Karar** — `TUT` / `BÜYÜT` / `KIRP` / `KAPAT` + boyut değişikliği gerekçesi.

### Veri kaynağı öncelik sırası
KAP raporları > şirket yatırımcı ilişkileri > İş Yatırım/aracı kurum (çapraz kontrol)
> haber özetleri (asla tek başına).

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
