import ccxt
import time

class PriceStreamHandler:
    def __init__(self, exchange_id, symbol):
        self.exchange = getattr(ccxt, exchange_id)()
        self.symbol = symbol

    def stream_prices(self, interval=2):
        try:
            while True:
                ticker = self.exchange.fetch_ticker(self.symbol)
                print(f"{self.symbol} | Bid: {ticker['bid']} | Ask: {ticker['ask']}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopped price stream manually.")
        except Exception as e:
            print(f"Error in price stream: {e}")
