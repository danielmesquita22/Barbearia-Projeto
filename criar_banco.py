import sqlite3

# Cria (ou conecta a) o banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Cria as tabelas (se não existirem ainda)
cursor.executescript("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS galeria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imagem TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    endereco TEXT,
    horario TEXT,
    whatsapp TEXT
);
""")

# Cria um usuário administrador inicial (opcional)
cursor.execute("INSERT OR IGNORE INTO admin (usuario, senha) VALUES (?, ?)", ("admin", "1234"))

conn.commit()
conn.close()

print("✅ Banco de dados criado com sucesso!")
