"""Desempacotamento de argumentos."""
# https://www.youtube.com/watch?v=-K38SBdeuys&list=PLOQgLBuj2-3LRIKxqcse1EL4hXhUFuHsR&index=3

# def my_sum(*args, **kwargs):
def my_sum(*grupo_pos, **grupo_nomeado):
    """Empacotamento."""
    print(grupo_pos, grupo_nomeado)
    print(type(grupo_pos), type(grupo_nomeado))
    return grupo_pos, grupo_nomeado


lista = [1, 2, 3, 4]


def my_min(a, b, c, d, *args):
    return min((a, b, c, d, *args))


# my_min(*lista)


dicionario = {"a": 1, "b": 2, "c": 3, "d": 4}


def my_max(a=0, b=0, c=0, d=0):
    return max((a, b, c, d))


# my_max(**dicionario)

l = [1, 2, 3]
d = {"d": 4, "e": 5}


def my_mix(a, b, c, d=0, e=0):
    return a, b, c, d, e


# my_mix(*l, **d)
