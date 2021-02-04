import os.path
import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
        self.cria_tabela()

    def cria_tabela(self):

        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS agenda ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'nome TEXT,'
            'telefone TEXT UNIQUE'  # não insere caso não seja único
            ')'  # se não conseguir o IGNORE entra em ação
        )

        self.conn.commit()

    def inserir(self, nome, telefone):
        consulta = (
            'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        )
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        """Filtra registros que contenham essa string em algum momento."""
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')

    agenda.inserir('Carlos', '39441411')
    agenda.inserir('Luiz', '39442326')
    agenda.inserir('Ana', '39441411')
    agenda.inserir('Ana', '39440000')
    agenda.inserir('Maria', '12345678')
    agenda.inserir('Carlitos', '333333')
    agenda.inserir('Carlão', '666666')

    agenda.editar('Renan', '131313', 2)

    agenda.excluir(8)

    agenda.listar()

    print('\n\n', 'Filtro de busca', '\n')
    agenda.buscar('Carl')

    # agenda.buscar('luiz')
