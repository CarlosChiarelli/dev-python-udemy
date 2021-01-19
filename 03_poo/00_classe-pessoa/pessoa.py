"""Conteúdo inicial de POO.

Tipos de métodos, relação entre classes,
variáveis de classe e de instância, atributos e métodos protegidos.
Como criar getter e setter e como funcionam.
"""
from datetime import datetime
from random import randint
from re import sub


class Pessoa:

    # logo abaixo é um atributo da classe, existe sem ser instanciada (init)
    # é uma variável de classe, ou seja,
    # é global, todos instâncias compartilham simultaneamente
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __str__(self):
        """Ao printar a classe/instância é retornado o nome do artefato.py"""
        return __name__

    def __del__(self):
        """Printa quando o item for deletado."""
        print(f'{self.nome, self.idade} FOI APAGADO !')

    def __init__(self, nome, idade, comendo=False, falando=False):
        """ Existe uma convenção para proteger atributos.

        self._var1  - recomenda-se não altera-lo mas é possível (protected)
        self.__var2 - recomenda-se fortemente não altera-lo E NÃO é possível (private)
        Vale tanto para atributos quanto métodos.
        """
        # são variáveis de instância (construtor atuando como setter)
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.pets = []
        self._protegido = 'ainda possível alterar mas não recomendado'
        # p1 = Pessoa()
        # p1._Pessoa__super_protegido para acessar o private abaixo
        self.__super_protegido = 'inalterável'

    # getter e setter são para proteger e validar os atributos
    # o setter É EXECUTADO logo APÓS o CONSTRUTOR (init)
    # property é decorador para obter um dado
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('a', '@')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if isinstance(valor, str):
            valor = int(sub('\D', '', valor))

        self._idade = valor

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    # é um método de instância!
    # PRECISO da classe INSTANCIADA para utilizar esse método
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    # é um método da classe! Precisa apenas da classe (para itens globais)
    # NÃO PRECISO da classe INSTANCIADA para utilizar esse método
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # é um método estático! Não precisa da instância nem da classe
    # é como se fosse uma função normal, para organização fica dentro da classe
    @staticmethod
    def gera_id():
        rand = randint(1000, 1999)
        return rand

    def insere_pet(self, nome, tipo):
        """Relação de COMPOSIÇÃO entre classes, uma classe faz parte da outra."""
        self.pets.append(PetAnimal(nome, tipo))

    def listar_pets(self):
        for value in self.pets:
            print(value.nome, value.tipo)

class PetAnimal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def __del__(self):
        print(f'ANIMAL {self.nome, self.tipo} FOI APAGADO!')
