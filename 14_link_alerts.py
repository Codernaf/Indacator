from market.profile import find_arbitrage_opportunity
from 13_telegram_alerts import send_alert
import asyncio
import time

def run_alert_loop():
    print("📡 Monitoring market for opportunities...")
    while True:
        try:
            opportunity = find_arbitrage_opportunity()
            if opportunity:
                message = f"💹 Arbitrage Opportunity!\n{opportunity}"
                asyncio.run(send_alert(message))
        except Exception as e:
            print(f"⚠️ Error during alert loop: {e}")
        
        time.sleep(10)  # ⏱ Check every 10 seconds

if __name__ == "__main__":
    run_alert_loop()
