"""Holt aktuelle Kurse von Yahoo Finance und schreibt kurse.json für Financial Awareness."""
import json
from datetime import datetime, timezone
import yfinance as yf

# Yahoo-Ticker, Anzeigename, Währung
WERTE = [
    ("^GDAXI", "DAX", "Pkt."), ("^GSPC", "S&P 500", "Pkt."), ("^NDX", "Nasdaq 100", "Pkt."),
    ("NVDA", "NVIDIA", "$"), ("AAPL", "Apple", "$"), ("MSFT", "Microsoft", "$"), ("GOOGL", "Alphabet", "$"),
    ("AMZN", "Amazon", "$"), ("META", "Meta", "$"), ("TSLA", "Tesla", "$"), ("NFLX", "Netflix", "$"),
    ("SAP.DE", "SAP", "€"), ("SIE.DE", "Siemens", "€"), ("ALV.DE", "Allianz", "€"), ("DTE.DE", "Deutsche Telekom", "€"),
    ("RHM.DE", "Rheinmetall", "€"), ("MBG.DE", "Mercedes-Benz", "€"), ("BMW.DE", "BMW", "€"), ("VOW3.DE", "Volkswagen", "€"),
    ("GC=F", "Gold", "$"), ("BTC-USD", "Bitcoin", "$"), ("EURUSD=X", "EUR/USD", ""),
]

def main():
    werte = []
    for sym, name, w in WERTE:
        try:
            t = yf.Ticker(sym)
            tag = t.history(period="1d", interval="15m")["Close"].dropna()
            vor = t.history(period="5d", interval="1d")["Close"].dropna()
            if tag.empty or len(vor) < 2:
                continue
            p = float(tag.iloc[-1])
            basis = float(vor.iloc[-2]) if vor.index[-1].date() == tag.index[-1].date() else float(vor.iloc[-1])
            s = [round(float(x), 4) for x in tag.iloc[:: max(1, len(tag) // 24)]] + [round(p, 4)]
            werte.append({"t": sym, "n": name, "w": w, "p": round(p, 4 if w == "" else 2), "d": round((p / basis - 1) * 100, 2), "s": s})
        except Exception as e:
            print("Fehler", sym, e)
    if werte:
        json.dump({"zeit": datetime.now(timezone.utc).isoformat(timespec="seconds"), "werte": werte},
                  open("kurse.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(len(werte), "Werte")

if __name__ == "__main__":
    main()
