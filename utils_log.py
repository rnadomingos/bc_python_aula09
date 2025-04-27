from loguru import logger
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
            "meu_info_logs.log",
            format="{time} <r>{level}</r> <g>{message}</g> {file}",
            level="INFO"
)

logger.add(
            "meu_ critical_logs.log",
            format="{time} <r>{level}</r> <g>{message}</g> {file}",
            level="ERROR"
          )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando funcao: '{func.__name__}' com args: {args} e kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Funcao '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Excecao capturada em '{func.__name__}': {e}")
            raise #Re-lança a excecao para não alterar o comportamento da função
    return wrapper