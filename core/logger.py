import logging


FORMAT = "%(levelname)s:     %(filename)s:%(lineno)s - %(message)s [%(asctime)s]"
DATE_FMT = "%H:%M:%S %d-%m-%Y"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt=DATE_FMT,
)

logger = logging.getLogger("__main__")
