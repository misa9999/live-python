from collections.abc import Sequence


class MyTuple(Sequence):
    def __init__(self, tuple_):
        self._d = tuple(tuple_)

    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        return f'{self._d}'


class TupleSet(Sequence):
    def __init__(self, tuple_, ordered=False):
        tup = []
        for value in tuple_:
            if value not in tup:
                tup.append(value)
                
        self._d = tuple(tup) if not ordered else tuple(sorted(tup))

    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        return f'{self._d}'


class TupleFlat(Sequence):
    def __init__(self, tuple_):
        self._d = tuple(sum(tuple_, []))


    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        return f'{self._d}'


class TupleFlatSize(Sequence):
    def __init__(self, tuple_):
        self._d = tuple(tuple_)
        

    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(tuple(sum(self._d, [])))

    def __repr__(self):
        return f'{self._d}'


class TupleFunctor(Sequence):
    def __init__(self, tuple_):
        self._d = tuple(tuple_)
        
    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def __repr__(self):
        return f'{self._d}'

    def fmap(self, fuction):
        return TupleFunctor(fuction(x) for x in self._d)