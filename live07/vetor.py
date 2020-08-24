class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, vetor):
        return (self.x + vetor.x, self.y + vetor.y)

    def __mul__(self, n):
        return (self.x * n, self.y * n)



# v1 = Vetor(2, 3)
# v2 = Vetor(2, 2)

# print(v1 + v2)
# print(v1 * v2)