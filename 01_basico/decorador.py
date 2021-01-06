"""Como utilizar decoradores. Utilizado para adicionar recursos às funções."""
from time import time, sleep


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
    """Mostra mensagem."""
    print('Oieeeee')


outra_func()


@mestre
def mostra_msg(msg):
    """Mostra mensagem."""
    print(msg)


mostra_msg('essa mensagem foi um argumento!')


# EXEMPLO 02
def velocidade(funcao):
    """Mede a velocidade de uma função qualquer."""

    def interna(*args, **kwargs):
        """Função interna para adicionar recurso."""
        start_time = time()

        result = funcao(*args, **kwargs)

        end_time = time()

        tempo_exec = (end_time-start_time)
        print(f'\nA função {funcao.__name__} demorou {tempo_exec:.5f}s.')

        # retorna o return da função original
        return result
    return interna


@velocidade
def demora():
    """Leva um tempo para executar."""
    for i in range(3):
        print(i)
        sleep(1)


demora()
