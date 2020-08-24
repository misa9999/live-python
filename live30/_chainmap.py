from collections import ChainMap
# problema: unir dois dicionarios

a = {1: 'a', 2: 'b', 3: 'c'}
b = {2: 'z', 3: 'z', 4: 'w'}

c = ChainMap(a, b)
