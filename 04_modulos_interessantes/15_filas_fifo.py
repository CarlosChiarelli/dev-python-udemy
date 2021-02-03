""" Estrutura de fila. First in First Out.

O primeiro elemento a sair é o primeiro que entrou.
"""
from collections import deque

fila = deque(maxlen=5)

fila.extend([1, 2, 3, 4])
fila.append(5)

print(fila)

fila.append(6)
fila.append(7)

print(fila)
