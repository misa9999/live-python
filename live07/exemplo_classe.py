"""Exemplo de classe"""


class NomeDaClasse():
    """
    NomeDaClasse define um tipo de dado, que levará o nome da classe.

    O Argumento slef deve ser passado em todos os arumentos da classe,
    para que os mesmos tenham acesso aos atributos e aos métodos da classe
    """
    def __init__(self, argumento_1, argumento_2, argumento_3=None):
        """
        Método que inicia a classe.

        Os argumentos são passados quando a classe é iniciada
        ou seja, quando é executado o __init__.
        Assim os valores externos na classe são inseridos em self.
        """
        self.atributo_1 = argumento_1
        self.atributo_2 = argumento_2
        self.atributo_3 = argumento_3

    def _privado(self, valor):
        """
        Em python não existem atributos/métodos privados, logo, por convenção
        se usa _ em frente dos mesmos

        É como se o que começa com _ fosse exclusivo de uso da classe, não
        de seus usuários.
        """
        pass

    def metodo_1(self):
        """
        Método que executa o método privado com um atributo a classe
        e retorna resultado
        """
        return self._privado(self.atributo_1)


    def metodo_2(self, valor):
        """
        Método que recebe um input externo para interadir com a classe.
        """
        return self.atributo_2 * valor


