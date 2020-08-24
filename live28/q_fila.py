from collections import deque

class Fila:
    def __init__(self):
        self.lista = deque()

    def insert_obj(self, val):
        self.lista.append(val)

    def remove_obj(self):
        return self.lista.popleft()

    def __repr__(self):
        return f'Fila [{",".join(str(x) for x in self.lista)}]'
