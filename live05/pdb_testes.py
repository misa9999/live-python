from pdb import set_trace, runcall, post_mortem

from testes_simples import validate

# TODO: criar relações de comandos
# step
# next
# up
# down
# where

# def soma(x: int, y: int) -> int:
#    return validate(x, y)

def div(x, y):
    return x / y

try:
    div(2, 0)
except:
    from sys import exc_info
    post_mortem(exc_info()[2])

# set_trace()
# print(soma(2, 2))

# runcall(soma, 2, 2)