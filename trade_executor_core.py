import ccxt
import time
from env_loader import load_api_keys

class TradeExecutor:
    def __init__(self):
        self.api_keys = load_api_keys()
        self.exchanges = {}
        self.init_exchanges()

    def init_exchanges(self):
        for name, keys in self.api_keys.items():
            exchange_class = getattr(ccxt, name)
            self.exchanges[name] = exchange_class({
                'apiKey': keys['apiKey'],
                'secret': keys['secret'],
                'enableRateLimit': True,
            })

    def execute_trade(self, from_exchange, to_exchange, symbol, amount, profit_margin):
        ex1 = self.exchanges.get(from_exchange)
        ex2 = self.exchanges.get(to_exchange)

        if not ex1 or not ex2:
            return {'success': False, 'error': 'Exchange not initialized'}

        try:
            ex1_price = ex1.fetch_ticker(symbol)['bid']
            ex2_price = ex2.fetch_ticker(symbol)['ask']
            profit = (ex1_price - ex2_price) / ex2_price

            if profit >= profit_margin:
                print(f"Arbitrage Opportunity Found: Profit {profit*100:.2f}%")
                # PLACEHOLDER: Simulated orders
                print(f"Buying {symbol} on {to_exchange} at {ex2_price}")
                print(f"Selling {symbol} on {from_exchange} at {ex1_price}")
                return {'success': True, 'profit': profit}
            else:
                return {'success': False, 'reason': 'Profit margin too low'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
