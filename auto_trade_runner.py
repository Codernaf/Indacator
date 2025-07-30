from utils.price_fetcher import PriceFetcher
from utils.arbitrage_detector import ArbitrageDetector
from trade_executor_core import TradeExecutor
from arb_monitor import ArbitrageMonitor

API_KEYS = {
    'binance': {
        'apiKey': 'your_binance_api_key',
        'secret': 'your_binance_secret',
    },
    'bybit': {
        'apiKey': 'your_bybit_api_key',
        'secret': 'your_bybit_secret',
    },
    'bitget': {
        'apiKey': 'your_bitget_api_key',
        'secret': 'your_bitget_secret',
    }
}

class AutoArbitrageMonitor(ArbitrageMonitor):
    def __init__(self, symbols, fetcher, detector, executor, auto_trade=False):
        super().__init__(symbols, fetcher, detector)
        self.executor = executor
        self.auto_trade = auto_trade

    def process_opportunity(self, opp):
        print(f"Opportunity: Buy {opp['buy']['symbol']} on {opp['buy']['exchange']} at {opp['buy']['price']}, "
              f"Sell on {opp['sell']['exchange']} at {opp['sell']['price']}, Profit: {opp['profit']*100:.2f}%")
        if self.auto_trade:
            trade_result = self.executor.execute_trade(
                from_exchange=opp['sell']['exchange'],
                to_exchange=opp['buy']['exchange'],
                symbol=opp['buy']['symbol'],
                amount=10,  # example amount
                profit_margin=0.005
            )
            print("Trade Result:", trade_result)

if __name__ == "__main__":
    exchanges = list(API_KEYS.keys())
    symbols = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']
    
    fetcher = PriceFetcher(exchanges)
    detector = ArbitrageDetector(threshold=0.005)
    executor = TradeExecutor(API_KEYS)

    monitor = AutoArbitrageMonitor(symbols, fetcher, detector, executor, auto_trade=True)
    monitor.run(interval=10)
