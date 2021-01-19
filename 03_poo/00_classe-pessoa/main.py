from pessoa import Pessoa

p1 = Pessoa('Carlos', 29)
p2 = Pessoa('João', 32)

print('\n', p1, '\n')

print(p1.nome, p1.idade)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(Pessoa.ano_atual)
print(Pessoa.gera_id())

print(p1.gera_id(), p1.ano_atual)

Pessoa.ano_atual = 2015
p2.ano_atual = 2017

print(p1.gera_id(), p1.ano_atual, p2.ano_atual)

p1.insere_pet('Bob', 'cão')
p1.insere_pet('Ana', 'gato')
p1.listar_pets()

print('\n########## FIM DA MAIN ##########\n')
