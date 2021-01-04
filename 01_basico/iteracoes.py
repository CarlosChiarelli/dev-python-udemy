"""Iterações de diversas formas."""
from itertools import zip_longest, combinations, permutations, product

# iterando variáveis tamanhos distintos
cidades = ['sao paulo', 'belo horizonte', 'salvador', 'dumont']
estados = ['SP', 'MG', 'BA']

for cid, est in zip_longest(estados, cidades):
    print(cid, est)

# obtém todas as combinações possíveis de 2 em 2
for grupo in combinations(cidades, 2):
    print(grupo)

# obtém combinações onde a ordem importa
print('\n\nPermutações:\n')

for grupo in permutations(cidades, 2):
    print(grupo)

# obtém todas combinações possíveis (ordem importa)
print('\n\nPermutações:\n')

for num, grupo in enumerate(product(cidades, repeat=2)):
    print(num, grupo)
