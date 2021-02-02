"""Contém funcionalidades básicas da linguagem."""
num1 = input('Digite um numero:')

# checa se a string é um número
print(num1.isdigit())

# descompacta listas
lista = ['carlos', 'augusto', 1, 'dois', 3, 4, 5]

n1, n2, *restante = lista

print(n1, n2)

# guarda o que não coube nas 2 variáveis
print(f'restante: {restante}')

# operador OR
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Carlos'

val = a or b or c or d or e or f or g

print(f"Operador OR: {val}")


# como forçar tipos de dados em funções
def funcao(p1: float, p2: str, p3: dict) -> float:
    """Função que indica os parâmetros recebidos e o valor retornado.

    Isso não afeta o códio (gerar erro), é apenas um estilo de documentação

    :param p1: Float é um parâmetro.
    :param p2: Str é um outro parâmetro.
    :param p3: Dict é um outro parâmetro.
    :return: Float é um número retornado.
    """
    print(p1, p2, p3)

    return p1


funcao(5.2, 'oi', {'Carlos': 24})
