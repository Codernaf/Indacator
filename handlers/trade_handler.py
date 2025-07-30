from services.trading_service import execute_trade
from utils.logger_util import setup_logger

logger = setup_logger('trade_handler')

def handle_trade_event(event):
    try:
        trade_data = event.get('trade')
        if not trade_data:
            logger.warning("No trade data found in event")
            return

        result = execute_trade(trade_data)
        logger.info(f"Trade executed successfully: {result}")
    except Exception as e:
        logger.error(f"Error handling trade event: {e}")
