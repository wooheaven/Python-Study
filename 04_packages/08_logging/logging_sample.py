import logging.config
import json
import time


with open("logging_conf.json", "rt") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = logging.getLogger()

logger.info("SOx Model Learning start")
time.sleep(10)
logger.info("SOx Model Learning end")

logger.info("NOx Model Learning start")
time.sleep(7)
logger.info("NOx Model Learning end")

logger.info("Dust Model Learning start")
time.sleep(6)
logger.info("Dust Model Learning end")

logger.info("DSH Model Learning start")
time.sleep(13)
logger.info("DSH Model Learning end")
