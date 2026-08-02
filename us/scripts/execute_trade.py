#!/usr/bin/env python3
"""execute_trade.py — portfolio.json'u degistirmenin TEK yolu.

Islem tipleri:
  BUY         --symbol --shares --price [--rationale]
  SELL        --symbol --shares --price [--rationale]
  CORRECTION  --symbol --new-shares --new-price [--rationale]
              (veri/bolunme duzeltmesi; NAKIT-NOTRDUR, maliyet tabani korunur,
               eski kayit SILINMEZ - yeni bir CORRECTION satiri eklenir.)

Her islem logs/ledger/trades.jsonl'a eklenir ve portfolio.json yeniden yazilir.
mandate.md 4.1 ve 4.3 geregi: elle duzenleme yok, gecmis silinmez.
"""
import argparse
import datetime
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PF = os.path.join(ROOT, "portfolio.json")
LEDGER = os.path.join(ROOT, "logs", "ledger", "trades.jsonl")


def load_pf():
    with open(PF, encoding="utf-8") as f:
        return json.load(f)


def save_pf(pf):
    with open(PF, "w", encoding="utf-8") as f:
        json.dump(pf, f, indent=2, ensure_ascii=False)
        f.write("\n")


def append_ledger(rec):
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("type", choices=["BUY", "SELL", "CORRECTION"])
    ap.add_argument("--symbol", required=True)
    ap.add_argument("--shares", type=float)
    ap.add_argument("--price", type=float)
    ap.add_argument("--new-shares", type=float)
    ap.add_argument("--new-price", type=float)
    ap.add_argument("--rationale", default="")
    ap.add_argument("--ts", default=datetime.date.today().isoformat())
    ap.add_argument("--tier", default="mid")
    a = ap.parse_args()

    pf = load_pf()
    pos = pf["positions"].get(a.symbol)
    rec = {"ts": a.ts, "type": a.type, "symbol": a.symbol, "rationale": a.rationale}

    if a.type == "BUY":
        amt = a.shares * a.price
        assert pf["cash"] >= amt, "Yetersiz nakit"
        if pos:
            pos["shares"] += a.shares
            pos["cost_basis"] = round(pos["cost_basis"] + amt, 2)
            pos["avg_cost"] = round(pos["cost_basis"] / pos["shares"], 4)
        else:
            pf["positions"][a.symbol] = {
                "shares": a.shares, "avg_cost": round(a.price, 4),
                "cost_basis": round(amt, 2), "tier": a.tier,
                "status": "UNDERWRITE_BEKLIYOR", "opened": a.ts}
        pf["cash"] = round(pf["cash"] - amt, 2)
        rec.update(shares=a.shares, price=a.price, amount=round(amt, 2))

    elif a.type == "SELL":
        assert pos and pos["shares"] >= a.shares, "Yetersiz pozisyon"
        amt = a.shares * a.price
        unit_cost = pos["cost_basis"] / pos["shares"]
        pos["cost_basis"] = round(pos["cost_basis"] - unit_cost * a.shares, 2)
        pos["shares"] -= a.shares
        pf["cash"] = round(pf["cash"] + amt, 2)
        realized = round((a.price - unit_cost) * a.shares, 2)
        if pos["shares"] <= 1e-6:
            del pf["positions"][a.symbol]
        rec.update(shares=a.shares, price=a.price, amount=round(amt, 2), realized_pnl=realized)

    elif a.type == "CORRECTION":
        assert pos, "Pozisyon yok"
        old_shares, old_price = pos["shares"], pos["avg_cost"]
        # Nakit-notr: maliyet tabani korunur, adet ve ortalama maliyet duzeltilir.
        pos["shares"] = a.new_shares
        pos["avg_cost"] = round(pos["cost_basis"] / a.new_shares, 4)
        pos.pop("note", None)
        pos["status"] = pos.get("status", "UNDERWRITE_BEKLIYOR")
        rec.update(old_shares=old_shares, old_price=old_price,
                   new_shares=a.new_shares, new_price=a.new_price,
                   cost_basis_preserved=pos["cost_basis"], cash_impact=0)

    pf["as_of"] = a.ts
    save_pf(pf)
    append_ledger(rec)
    print("ISLEM KAYDEDILDI:")
    print(json.dumps(rec, ensure_ascii=False, indent=2))
    print(f"Nakit: {pf['cash']:,.2f} TL")


if __name__ == "__main__":
    main()
