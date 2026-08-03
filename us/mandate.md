# mandate.md — US Paper Portfolio (Anayasa)

BIST sanal PM ile **aynı yatırım felsefesi**, ABD borsasına ve USD baz paraya uyarlanmış hali.
Bu belge anayasadır; değişiklik ancak yeni bir kayıtla (commit) yapılır, geçmiş silinmez.
Bu bir **kamuya açık şeffaflık deneyidir**; git geçmişi denetim izidir.

## 1. Amaç ve çerçeve
- **10.000 USD sanal (kağıt) portföy**, gerçek para yok.
- **Süre:** 12 ay.
- **Hedef:** 12 ayda **%20 USD getirisi**.
- **Benchmark:** S&P 500 (SPY). Başarı = hedefe ulaşmak **ve** SPY'ı geçmek.
- USD baz para → enflasyon düzeltmesi yok (getiri doğrudan reel USD).

## 2. Dürüstlük notu (hedef gerçekçiliği)
%20 USD/yıl, S&P 500'ün uzun dönem ~%10'unun **iki katı**dır; **hedeftir, garanti değil**.
Bunu ancak makul fiyatlı **yüksek-ROIC bileşikçiler + seçici değer/katalizör** ile ararız;
disiplin şansı artırır, oynaklığı yok etmez.

## 3. Yatırım felsefesi
Kalite (yüksek ROIC/ROE, fiyatlama gücü, güçlü FCF) **+** makul değerleme (FCF verimi,
FD/FAVÖK, PEG) **+** sağlam bilanço (net nakit tercih) **+** sekülar rüzgâr/katalizör.
Her pozisyon bir **underwriting** belgesiyle gerekçelendirilir; geçemeyen alınmaz/kapatılır.
Dil "şunu al" değil, "**bu portföy şu kararı verdi**".

## 4. Risk limitleri (pazarlık edilemez)
| Limit | Kural |
|---|---|
| Tek pozisyon | maks **%15** |
| Tek sektör (GICS) | maks **%30** |
| Tek tema/faktör (ör. "AI", faiz) | maks **%20** |
| Nakit | min **%5** |
| Evren | **Herhangi ölçek — large / mid / micro fark etmez**, yeterli likidite koşuluyla; liyakate göre seçilir |

- **Ölçek kısıtı yok:** en iyi risk/getiri hangi ölçekteyse oradan alınır (küçük/mikro-cap dahil).
  Küçük-cap için tek fark: pozisyon boyutu likidite + risk ile ölçeklenir (asimetrik küçük-cap
  bahisleri için tek isim fiilen daha küçük tutulur; tam kayıp tolere edilebilmeli).
- Meme/pump & dump/manipülasyona açık isim yok. **Kaldıraç, opsiyon, açığa satış yok.**
- Hedef fiyata gelen satılır; hedef revizyonu ancak yeni yazılı underwriting ile.

## 5. Sert kurallar
1. `portfolio.json` asla elle düzenlenmez; yalnızca `scripts/execute_trade.py` ile.
2. Look-ahead yok: karar o gün mevcut veriyle verilir ve aynı gün commit'lenir.
3. Geçmiş log/commit düzenlenmez; hata yeni bir kayıtla düzeltilir.
4. Her içerik taslağının sonunda: **"Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir."**

## 6. Veri kaynağı öncelik sırası
1. **SEC EDGAR** (10-K / 10-Q / 8-K) — birincil
2. Şirket **yatırımcı ilişkileri** sunum/rakamları
3. **Analist raporları** (çapraz kontrol)
4. Haber özetleri — asla tek başına.

Fiyat/mark-to-market: `lib_prices` → Yahoo chart API (proxy + CA); benchmark **SPY**.

## 7. Değerleme ve karar
3 senaryolu **USD FCFF İNA** (nominal WACC ~%9-11) + bağımsız çarpanlar (F/K, FD/FAVÖK,
FCF verimi, PEG, ROIC). Karar seti: **TUT · BÜYÜT · KIRP · KAPAT** (aday isimlerde **AL/ALMA**).

> Yatırım tavsiyesi değildir. Bu bir sanal portföy deneyidir.
