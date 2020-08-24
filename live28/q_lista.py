from collections import deque

class Lista:
    def __init__(self):
        self.lista = deque()

    def insert_obj(self, val, pos=None):
        if pos:
            self.lista.insert(val, pos)
        else:
            self.lista.append(val)

    def remove_obj(self, val):
        self.lista.remove(val)

    def __repr__(self):
        return f'Lista [{",".join(str(x) for x in self.lista)}]'
