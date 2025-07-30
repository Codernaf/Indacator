import ccxt
from env_loader import load_env_variables

env_vars = load_env_variables()

api_keys = {
    "binance": {
        "apiKey": env_vars["BINANCE_API_KEY"],
        "secret": env_vars["BINANCE_SECRET_KEY"]
    },
    "bybit": {
        "apiKey": env_vars["BYBIT_API_KEY"],
        "secret": env_vars["BYBIT_SECRET_KEY"]
    }
}

class ExchangeAPIBridge:
    def __init__(self):
        self.exchanges = {}
        self.init_exchanges(api_keys)

    def init_exchanges(self, credentials):
        for name, creds in credentials.items():
            exchange_class = getattr(ccxt, name)
            self.exchanges[name] = exchange_class({
                'apiKey': creds['apiKey'],
                'secret': creds['secret'],
                'enableRateLimit': True,
            })

    def get_balance(self, exchange_name):
        if exchange_name not in self.exchanges:
            return None
        try:
            return self.exchanges[exchange_name].fetch_balance()
        except Exception as e:
            return {'error': str(e)}

    def fetch_price(self, exchange_name, symbol):
        if exchange_name not in self.exchanges:
            return None
        try:
            return self.exchanges[exchange_name].fetch_ticker(symbol)
        except Exception as e:
            return {'error': str(e)}

    def create_order(self, exchange_name, symbol, order_type, side, amount, price=None):
        if exchange_name not in self.exchanges:
            return {'error': 'Exchange not available'}
        try:
            if order_type == 'market':
                return self.exchanges[exchange_name].create_market_order(symbol, side, amount)
            elif order_type == 'limit':
                return self.exchanges[exchange_name].create_limit_order(symbol, side, amount, price)
        except Exception as e:
            return {'error': str(e)}
