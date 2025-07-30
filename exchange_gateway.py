import ccxt

class ExchangeGateway:
    def __init__(self, api_key, secret, exchange_name):
        self.exchange = getattr(ccxt, exchange_name)({
            'apiKey': api_key,
            'secret': secret,
            'enableRateLimit': True
        })

    def fetch_order_book(self, symbol):
        try:
            return self.exchange.fetch_order_book(symbol)
        except Exception as e:
            print(f"Error fetching order book: {e}")
            return None

    def fetch_ticker(self, symbol):
        try:
            return self.exchange.fetch_ticker(symbol)
        except Exception as e:
            print(f"Error fetching ticker: {e}")
            return None

    def place_order(self, symbol, side, amount, price=None, type='limit'):
        try:
            if type == 'market':
                return self.exchange.create_market_order(symbol, side, amount)
            else:
                return self.exchange.create_limit_order(symbol, side, amount, price)
        except Exception as e:
            print(f"Error placing order: {e}")
            return None
