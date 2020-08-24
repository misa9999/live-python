class Gatinho:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.ryuu_com_fome = False
        self.rodado = 0

    def miar(self):
        if self.ryuu_com_fome:
            return 'MIAUUUUUUUUUUUUUUUUUUU'
        return 'Miau, Miau'

    def andar(self):
        self.ryuu_com_fome = True
        self.rodado += 1
        return 'Ryuu andando'

    @property
    def velho(self):
        return True if self.idade > 3 else False

    @property
    def cansado(self):
        return True if self.rodado > 5 else False


    def __repr__(self):
        return f'Nome: {self.nome} cor: {self.cor} idade: {self.idade}'


ryuu = Gatinho('Ryuu', 'preto', 2)

print(ryuu)
print(f'{ryuu.nome} esta miando {ryuu.miar()}')

print(ryuu.velho)
print(ryuu.cansado)