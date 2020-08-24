from string import ascii_letters

file = open('teste.txt', 'a')

for x in ascii_letters:
    file.write(f'\n{x}')