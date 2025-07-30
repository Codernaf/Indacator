from trade_executor_core import TradeExecutorCore

class OpportunityScanner:
    def __init__(self, api_keys, margin_threshold):
        self.executor = TradeExecutorCore(api_keys)
        self.margin_threshold = margin_threshold

    def scan(self, symbol, exchange1, exchange2):
        price1, price2 = self.executor.get_prices(symbol, exchange1, exchange2)
        if price1 is None or price2 is None:
            return {'success': False, 'error': 'Price fetch failed'}

        opportunity, profit = self.executor.detect_opportunity(price1, price2, self.margin_threshold)
        if opportunity:
            return {
                'success': True,
                'message': 'Opportunity detected',
                'buy_from': exchange2,
                'sell_to': exchange1,
                'profit': round(profit * 100, 2)
            }
        return {'success': False, 'message': 'No arbitrage opportunity'}
