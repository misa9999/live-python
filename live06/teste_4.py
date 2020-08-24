"""
Decorador simples
"""


def decorador(func):
    print(func.__name__)
    def interna(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x, y)
        else:
            raise ValueError('Insira somente inteiros')
    return interna

"""
decorador -> internat -> função decorada
"""

@decorador
def soma(x: int, y: float):
    return x + y

@decorador
def div(x: int, y: float):
    return x / y


# decorador(soma(2, 3))

print(soma(2, 2))
print(div(2, 'dan'))