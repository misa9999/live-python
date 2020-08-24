from collections import UserDict


class MyDict(UserDict):

    def __lshift__(self, value):
        self.data['last'] = value
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)
        d_copy = self.data.copy()
        d_copy[key] = value
        return d_copy

