# file = open('teste_win1252.txt', errors='strict')
# file = open('teste_win1252.txt', errors='replace')
# file = open('teste_win1252.txt', errors='ignore')
# file = open('teste_win1252.txt', errors='surrogateescape')
file = open('teste_win1252.txt', errors='backslashreplace')


print(file.read())