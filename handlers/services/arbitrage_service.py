import ccxt
from utils.logger_util import setup_logger

logger = setup_logger('arbitrage_service')

def find_arbitrage_opportunities(exchange1, exchange2, symbol):
    try:
        ticker1 = exchange1.fetch_ticker(symbol)
        ticker2 = exchange2.fetch_ticker(symbol)

        price1 = ticker1['ask']
        price2 = ticker2['bid']

        if price1 < price2:
            profit = price2 - price1
            logger.info(f"Arbitrage opportunity: Buy on {exchange1.id}, Sell on {exchange2.id}, Profit: {profit}")
            return {
                "buy_exchange": exchange1.id,
                "sell_exchange": exchange2.id,
                "buy_price": price1,
                "sell_price": price2,
                "profit": profit
            }

        logger.info("No arbitrage opportunity found")
        return None
    except Exception as e:
        logger.error(f"Error finding arbitrage: {e}")
        return None
