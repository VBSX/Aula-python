import sqlite3

def conectar():
    return sqlite3.connect("dados.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    """)
    conn.commit()
    conn.close()

def inserir(nome, idade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
    conn.commit()
    conn.close()

def consultar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    return cursor.fetchall()
