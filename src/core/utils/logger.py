import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

LOGS_DIR = "logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def setup_logger(name: str) -> logging.Logger:
    """
    Configura e retorna um logger com handlers para console e arquivo.
    
    Args:
        name (str): Nome do logger (geralmente __name__ do módulo)
        
    Returns:
        logging.Logger: Logger configurado
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if logger.handlers:
        return logger
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    console_handler.setFormatter(console_formatter)

    log_file = os.path.join(LOGS_DIR, f"bot_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5*1024*1024, 
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    file_handler.setFormatter(file_formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

bot_logger = setup_logger("discord_bot") 