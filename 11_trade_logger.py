import logging
from datetime import datetime

# Configure the logger
logging.basicConfig(
    filename='trade_history.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

def log_trade(direction, symbol, amount, price):
    log_entry = f"{direction.upper()} | Symbol: {symbol} | Amount: {amount} | Price: {price}"
    logging.info(log_entry)
    print(f"Logged: {log_entry}")

# Example usage
if __name__ == "__main__":
    log_trade('buy', 'BTC/USDT', 0.001, 29345.55)
    log_trade('sell', 'BTC/USDT', 0.001, 29412.22)
