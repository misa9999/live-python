from logging import getLogger, basicConfig, DEBUG
from sys import exc_info
from collections import deque
from pdb import post_mortem

basicConfig(filename='test.log', filemode='w', level=DEBUG)

log = getLogger(__name__)

log.info('Teste1')
log.info('Teste2')
log.info('Teste3')
log.info('Teste1000')

def debug(debug=False):
    def tail_log(func):
        def execute_func(*args):
            try:
                func(*args)
            except Exception as error:
                log.info(f'{func.__name__} args:{args} error:{error}')
                if debug:
                    for line in deque(open('test.log'), 10):
                        print(line)
                    post_mortem(exc_info()[2])
        return execute_func
    return tail_log

@debug(False)
def div(x, y):
    return x / y

div(2, 0)