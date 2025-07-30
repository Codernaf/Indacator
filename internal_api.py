from exchange_api_bridge import ExchangeAPIBridge

class InternalAPI:
    def __init__(self, credentials):
        self.bridge = ExchangeAPIBridge(credentials)

    def get_price(self, exchange, symbol):
        ticker = self.bridge.fetch_price(exchange, symbol)
        if 'error' in ticker:
            return {'success': False, 'error': ticker['error']}
        return {
            'success': True,
            'price': {
                'bid': ticker.get('bid'),
                'ask': ticker.get('ask'),
                'last': ticker.get('last')
            }
        }

    def get_balance(self, exchange):
        balance = self.bridge.get_balance(exchange)
        if 'error' in balance:
            return {'success': False, 'error': balance['error']}
        return {'success': True, 'balance': balance}

    def make_order(self, exchange, symbol, order_type, side, amount, price=None):
        order = self.bridge.create_order(exchange, symbol, order_type, side, amount, price)
        if 'error' in order:
            return {'success': False, 'error': order['error']}
        return {'success': True, 'order': order}
