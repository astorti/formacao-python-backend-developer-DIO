import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/"clientes.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), endereco VARCHAR(150))")
    conexao.commit()

def inserir_registro(conexao, cursor, nome, endereco):
    data = (nome, endereco)
    cursor.execute("INSERT INTO clientes (nome, endereco) VALUES (?,?);", data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, endereco, id):
    data = (nome, endereco, id)
    cursor.execute("UPDATE clientes SET nome=?, endereco=? WHERE id=?;", data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def inserir_varios_registros(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, endereco) VALUES (?,?);", dados)
    conexao.commit()

def selecionar_cliente_por_id(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

criar_tabela(conexao, cursor)

dados = [
    ("Nome1", "endereco1"),
    ("Nome2", "endereco2"),
    ("Nome2", "endereco3"),
]
inserir_varios_registros(conexao, cursor, dados)

cliente = selecionar_cliente_por_id(cursor, 3)
print(dict(cliente))
print(cliente["nome"])

atualizar_registro(conexao, cursor, "Nome3", "Endereco3", 3)

try:
    cursor.execute("INSERT INTO clientes (nome, endereco) VALUES (?,?)", ("Teste1", "teste1"))
    cursor.execute("INSERT INTO clientes (id, nome, endereco) VALUES (?,?,?)", (2, "Teste1", "teste1"))
    conexao.commit()
except Exception as e:
    print(f"Ocorreu um erro! {e}")
    conexao.rollback()

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

excluir_registro(conexao, cursor, 1)
excluir_registro(conexao, cursor, 2)
excluir_registro(conexao, cursor, 3)

clientes = listar_clientes(cursor)

for cliente in clientes:
    print(dict(cliente))