"""Criação, adição, edição, exclusão no banco SQLite3."""
import sqlite3

# cria conexão e cursor
conexao = sqlite3.connect('01_base_dados.db')
cursor = conexao.cursor()

"""
# cria tabela caso não exista
cursor.execute(
    'CREATE TABLE IF NOT EXISTS clientes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')'
)

# insere 1 registro (id criado automaticamente)
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Carlos", 54.5)')

# adicionando outros dados (diferentes formas)
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50)
)

cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'João', 'peso': 75},
)

cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Daniel', 'peso': 100},
)
"""

# editar/atualizar um registro por um ID específico
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Joana alterado', 'id': 2},
)

# commita mudanças
conexao.commit()

# mostrar tudo que está na tabela
cursor.execute('SELECT * FROM clientes')

# buscar todos os valores e itera para obtê-los
for linha in cursor.fetchall():

    # print(linha)
    # ou
    id_dado, nome, peso = linha
    print(id_dado, nome, peso)


cursor.close()
conexao.close()
