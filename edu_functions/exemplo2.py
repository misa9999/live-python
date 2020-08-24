"""serie de funções 2."""
# https://www.youtube.com/watch?v=UQVIb_X_dOk&list=PLOQgLBuj2-3LRIKxqcse1EL4hXhUFuHsR&index=2

anonima = lambda param: param + 2
anonima_plus = lambda param1, param2: param1 + param2


def soma_posicional(x, y):
    """X e Y são parâmetros posicionais."""
    return x + y


def soma_nomeados(x=7, y=7):
    """X e Y são parâmetros nomeados.
    na falta de x ou y, o valor 7 será usado.
    """
    print(f"x: {x} y: {y}")
    return x + y


def soma_explicitamente_nomeados(*, x=7, y=7):
    """X e Y são parâmetros nomeados.
    é obrigatorio passar um valor ao parametro
    """
    print(f"x: {x} y: {y}")
    return x + y


def soma_explicitamente_nomeados2(x=7, *, y=7):
    """X e Y são parâmetros nomeados. 
    é obrigatorio passar um valor ao parametro
    """
    print(f"x: {x} y: {y}")
    return x + y

