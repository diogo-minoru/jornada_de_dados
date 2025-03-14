from loguru import logger

from utils_log import log_decorator_soma

@log_decorator_soma
def retorna_soma(x, y):
    soma = x + y
    return print(soma)

retorna_soma(1, "3")