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

    def falar(self):
        print('Estou em CLIENTE!')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        """Caso use super().__init__() ou super().metodo() ele utilizará da classe
        imediatamente anterior.
        Quando quero adicionar atributos se deve seguir a maneira abaixo"""
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        super().falar()
        print(f'{self.nome, self.sobrenome}')


class Aluno(Pessoa):

    def estudar(self):
        print(f'{self.nomeclasse} estudando ...')
