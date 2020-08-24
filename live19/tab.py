import re


with open('tabacaria.txt') as _file:
    text = _file.read()

olha = re.search(r'olha', text)
print(olha)
# print(text[3736:3740])
print(text[olha.start():olha.end()])