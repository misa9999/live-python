import os
import os.path
import shutil
from pathlib import Path

# if not os.path.exists('aulinha_2'):
#     os.mkdir('aulinha_2')

# os.chdir('aulinha_2')

# Criando arquivos
for arq in range(1, 11):
    Path(f'live_{arq}.txt').touch()

l = [f for f in os.listdir('.') if f.startswith('live_')]

# Removendo arquivos menores ou iguais a cinco
for _file in l:
    if int(_file.partition('_')[2][0]) <= 5:
        os.remove(_file)

l = [f for f in os.listdir('.') if f.startswith('live_')]

# Alterando os valores restantes
for val, el in enumerate(sorted(l), 1):

    shutil.move(el, f'live_{val}')

l = [f for f in os.listdir('.') if f.startswith('live_')]
print(sorted(l))