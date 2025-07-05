import functools
import logging

logging.basicConfig(level= logging.INFO)

def log_preprocessor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper
