from functools import lru_cache
import logging


FORMAT = "%(levelname)s:     %(filename)s:%(lineno)s - %(message)s [%(asctime)s]"
DATE_FMT = "%H:%M:%S %d-%m-%Y"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt=DATE_FMT,
)


@lru_cache
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
