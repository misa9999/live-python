from collections.abc import Container, Iterable, Sized


class MySequence(Container, Iterable, Sized):
    def __init__(self, *seq):
        self.seq = seq

    def __contains__(self, value):
        return value in self.seq

    def __iter__(self):
        return iter(self.seq)

    def __len__(self):
        return len(self.seq)