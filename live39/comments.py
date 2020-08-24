""" 
Comentários do módulo. (REST)

Bananas de pijamas descendo as escadas
Bananas de pijamas uma dupla da pesada

"""

# old mode
'''
def soma(x, y):
    """soma dos números.

    ARG:
        :x int: valor a ser somado
        :y int: valor a ser somado

    """
    return x + y
'''


def soma(x: int, y: int) -> int:
    """soma dois números.

    ARG:
        x: valor a ser somado
        y: valor a ser somado

    VARS:
        r: resultado da soma de x, y

    Função que soma dois números foi criada para suprir a
    necessidade de que existam outras funções.
    
    """
    r = x + y
    return r


print(help(soma))
