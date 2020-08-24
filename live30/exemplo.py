from os import environ
from argparse import ArgumentParser
from collections import ChainMap

defaults = {'cor': 'vermelho',
            'User': 'Convidado'}


parser = ArgumentParser()
parser.add_argument('-U', '--user')
parser.add_argument('-C', '--cor')
namespace = parser.parse_args()
linha_comando = {k: v for k, v in vars(namespace).items() if v}

combinado = ChainMap(linha_comando, environ, defaults)
print(combinado['cor'])
print(combinado['User'])