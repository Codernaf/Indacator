from exchange_api_bridge import ExchangeAPIBridge

class ArbitrageDetector:
    def __init__(self, credentials, symbols):
        self.bridge = ExchangeAPIBridge(credentials)
        self.exchanges = list(credentials.keys())
        self.symbols = symbols

    def detect_opportunities(self, min_profit=0.01):
        opportunities = []
        for symbol in self.symbols:
            prices = {}
            for ex in self.exchanges:
                ticker = self.bridge.fetch_price(ex, symbol)
                if 'error' not in ticker:
                    prices[ex] = {
                        'bid': ticker['bid'],
                        'ask': ticker['ask']
                    }

            for ex_buy in prices:
                for ex_sell in prices:
                    if ex_buy == ex_sell:
                        continue
                    buy_price = prices[ex_buy]['ask']
                    sell_price = prices[ex_sell]['bid']
                    if buy_price and sell_price and buy_price > 0:
                        profit_margin = (sell_price - buy_price) / buy_price
                        if profit_margin >= min_profit:
                            opportunities.append({
                                'symbol': symbol,
                                'buy_from': ex_buy,
                                'sell_to': ex_sell,
                                'buy_price': buy_price,
                                'sell_price': sell_price,
                                'profit_margin': round(profit_margin, 4)
                            })
        return opportunities
