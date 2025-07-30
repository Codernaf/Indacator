import asyncio
from market.profile import find_arbitrage_opportunity
from 13_telegram_alerts import send_alert

async def monitor_market():
    print("🚀 Async arbitrage engine running...")
    while True:
        try:
            opportunity = find_arbitrage_opportunity()
            if opportunity:
                message = f"📢 Arbitrage Signal:\n{opportunity}"
                await send_alert(message)
        except Exception as e:
            print(f"❌ Error: {e}")
        
        await asyncio.sleep(5)  # ⏱ Faster check interval

if __name__ == "__main__":
    asyncio.run(monitor_market())
