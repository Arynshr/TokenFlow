import logging
from functools import wraps
from time import time

def get_logger(name):
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)

logger = get_logger(__name__)

def log_method(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__qualname__}()")
        return func(*args, **kwargs)
    return wrapper

def log_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} took {time() - start}s")
        return result
    return wrapper
