import time
from utils.price_fetcher import PriceFetcher
from utils.arbitrage_detector import ArbitrageDetector

class ArbitrageMonitor:
    def __init__(self, symbol_list, price_fetcher: PriceFetcher, detector: ArbitrageDetector):
        self.symbols = symbol_list
        self.fetcher = price_fetcher
        self.detector = detector

    def run(self, interval=5):
        print("📡 Monitoring for arbitrage opportunities...")
        while True:
            for symbol in self.symbols:
                prices = self.fetcher.fetch_all_prices(symbol)
                opportunities = self.detector.find_opportunities(prices)
                if opportunities:
                    for opp in opportunities:
                        print(f"💰 Arbitrage found: Buy on {opp['buy_exchange']} at {opp['buy_price']} and sell on {opp['sell_exchange']} at {opp['sell_price']} — Profit: {opp['profit_margin']*100:.2f}%")
                else:
                    print(f"⏳ No arbitrage for {symbol}")
            time.sleep(interval)

if __name__ == "__main__":
    # Sample usage, wire up later in main runner
    pass
