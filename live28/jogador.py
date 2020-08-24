from collections import namedtuple

# j = namedtuple('jogador', 'nome time camisa n')

# n = namedtuple('ABC', 'slot1 slot2 slot3')

naipes = 'PCOE'
valores = list(range(2, 11)) + 'A J Q K'.split()

carta = namedtuple('Carta', 'naipe valor')

baralho = [carta(naipe, valor) for naipe in naipes for valor in valores]
