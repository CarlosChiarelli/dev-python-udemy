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
