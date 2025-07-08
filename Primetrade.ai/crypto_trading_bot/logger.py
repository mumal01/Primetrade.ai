# logger.py

import logging

def setup_logger():
    logger = logging.getLogger("TradingBotLogger")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("trading_bot.log")
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger
