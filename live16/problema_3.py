import os
import os.path
import shutil
from pathlib import Path


for el in range(1, 11):
    if not os.path.exists(f'pasta_{el}'):
        os.mkdir(f'pasta_{el}')
        

l = [path for path in os.listdir('.') 
     if os.path.isdir(path) and path != 'aulinha_1']

for path in l:
    Path(os.path.join(path, 'arquivo_1.txt')).touch()
    Path(os.path.join(path, 'arquivo_2.txt')).touch()

    # Path(f'{path}/arquivo_1.txt').touch()
    # Path(f'{path}/arquivo_2.txt').touch()


for val in os.walk('.'):
    print(val)