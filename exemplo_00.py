from loguru import logger
import sys

logger.debug("That's it, beautiful and simple logging!")

logger.add("meu.log", format="{time} {level} {message}", level="INFO")

@logger.catch
def soma(x,y):
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

soma(2,'3')