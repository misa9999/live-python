# função nomeada
def soma(x, y):
    """
    Função que soma dois valores

    """
    return x + y


# print(list(map(lambda x: x + 2, [1, 2, 3])))

# função anonima
#'f(x) | x + 2'
soma_2 = lambda x: x + 2

#print(soma_2(2))


# função como classe
class ClasseSoma:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x + self.y



a = ClasseSoma(2, 2)
print(a())
