"""Como utilizar decoradores. Utilizado para adicionar recursos às funções."""


# funcionamento de um decorador
def mestre(funcao):
    """Função decoradora."""

    def escravo(*args, **kwargs):
        """Escravo. Recurso a ser adicionado."""
        # recurso adicionado
        print('\nAgora estou decorada!')

        # execução da função original
        funcao(*args, **kwargs)

    return escravo


def fala_oi():
    """Função a ser decorada."""
    print('Oi')


# análogo ao decorador
fala_oi_decorada = mestre(fala_oi)
fala_oi_decorada()


# decorador
@mestre
def outra_func():
    print('Oieeeee')


outra_func()


@mestre
def mostra_msg(msg):
    print(msg)


mostra_msg('essa mensagem foi um argumento!')
