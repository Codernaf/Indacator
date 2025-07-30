from utils.price_fetcher import PriceFetcher
from utils.arbitrage_detector import ArbitrageDetector
from arb_monitor import ArbitrageMonitor

if __name__ == "__main__":
    # Define exchanges and symbols
    exchanges = ['binance', 'bybit', 'bitget']
    symbols = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT']

    # Initialize core components
    fetcher = PriceFetcher(exchanges)
    detector = ArbitrageDetector(threshold=0.005)  # 0.5% profit minimum
    monitor = ArbitrageMonitor(symbols, fetcher, detector)

    # Start real-time monitoring
    monitor.run(interval=10)
