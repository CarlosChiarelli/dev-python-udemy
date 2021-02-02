"""https://rszalski.github.io/magicmethods/ ."""


class A:
    def __new__(cls, *args, **kwargs):
        """Trata-se do construtor em Python."""
        print('Método new foi chamado')

        # SINGLETON (verifica se a classe já foi instanciada em algum momento)
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return cls._jaexiste

    def __call__(self, *args, **kwargs):
        """Quando a instância da classe for chamada como uma função."""
        return f'Argumentos enviados: {args} {kwargs}'

    def __len__(self):
        return 55

    def __init__(self, nome=None):
        print('INIT')

    def __str__(self):
        """Quando printar uma instancia."""
        return (
            f'O que quero exibir quando essa classe se transformar em uma str'
        )

    def __del__(self):
        """Deletar printar uma instancia."""
        print('Objeto coletado.')

    def __setattr__(self, key, value):
        """Quando settar (definir um atributo) uma instancia."""
        self.__dict__[key] = f'{value} adicionei isso no seu valor'
        print(f'{value} adicionei isso no seu valor')


if __name__ == '__main__':
    a = A('luiz otávio')

    c = A('Carlos')
    c.lindo = True
