"""Tratamento e tipos de erros."""

# melhor método pra tratar exceções (erro conhecido)
try:
    print(a)
except NameError as e:
    print(f'Erro do desenvolvedor: {e}')

# erro não esperado
try:
    print(a)
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')

# erro de índice
try:
    b = []
    print(b[1])
except IndexError as e:
    print(f'Ocorreu um erro de índice: {e}')

# erro de índice ou chave
try:
    dicion = {}
    print(dicion[1])
except (IndexError, KeyError) as e:
    print(f'Ocorreu um erro de índice/chave: {e}')

# else (sucesso)
try:
    a = 1
except Exception as e:
    raise e
else:
    print('sucesso')

# else (sucesso) e finnaly (executa SEMPRE)
try:
    print('\n\n')
    a = 1/0
except Exception:
    print('Houve um erro')
else:
    print('Executa com sucesso sem erro!')
finally:
    a = 'vazio'

print(a)

# raise (lançar própria execeção)
try:
    raise ValueError('Criando um erro')
except Exception as e:
    print(e)
