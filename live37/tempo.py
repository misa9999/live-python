from pdb import set_trace
from configparser import ConfigParser
from functools import wraps
from time import time

d = {'verbose': 0,
     'debug': 0}

config = ConfigParser(d, allow_no_value=True)
config.read('time.ini')
default_config = dict(config['default'])
print(default_config)


def debuggable(func):
    """Decorador para debugar"""
    @wraps(func)
    def _inner(*args):
        if default_config['debug'] == 'True':
            set_trace()
        return func(*args)
    return _inner


def timeit(func):
    """Decorador para medir tempo"""
    @wraps(func)
    def _inner(*args):
        ts = time()
        result = func(*args)
        te = time()
        if default_config['verbose'] == '1':
            print(f'{func.__name__} {args} {te - ts:.2}')
        return result
    return _inner


@debuggable
@timeit
def soma(x, y):
    return x + y

soma(2, 2)

