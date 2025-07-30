import asyncio
from datetime import datetime

async def check_market():
    print(f"[{datetime.now()}] Checking market for arbitrage opportunities...")
    # Here you'd call your actual arbitrage-checking logic
    await asyncio.sleep(1)

async def run_scheduler(interval_seconds=10):
    while True:
        await check_market()
        await asyncio.sleep(interval_seconds)

if __name__ == "__main__":
    try:
        print("Auto scheduler started.")
        asyncio.run(run_scheduler(10))  # Runs every 10 seconds
    except KeyboardInterrupt:
        print("Scheduler stopped manually.")
