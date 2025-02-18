import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s   %(msg)s: %(filename)s:%(lineno)s - %(name)s [%(asctime)s]",
)
logger = logging.getLogger("__main__")
