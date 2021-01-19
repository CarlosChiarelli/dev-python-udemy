"""Herança e poliformismo."""


class Pessoa:
    """Essa é a super classe.

    As outras vão herdar os atributos e métodos dela.
    Não é adequado colocar métodos aqui mas defini-los na sub-classe.
    """

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando ...')

# abaixo serão criadas as sub-classes que herdam o objeto da super classe

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando ...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando ...')
