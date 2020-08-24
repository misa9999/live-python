class Fila:
    def __init__(self, *args):
        self.f = list(args)

    def __repr__(self):
        return f'Fila: {self.f}'

    def __setitem__(self, pos, val):
        self.f[pos] = val

    def __getitem__(self, pos):
        return self.f[pos]

    def __lshift__(self, val):
        self.f.append(val)
