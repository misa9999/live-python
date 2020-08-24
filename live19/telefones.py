from time import sleep
import re
from itertools import permutations

cel = re.compile(r'[7-9][0-9]{7}')

for tel in permutations(range(1, 10), 8):
    # sleep(0.1)
    _tel = ''.join(str(x) for x in tel)
    if cel.search(_tel):
        print(_tel) 