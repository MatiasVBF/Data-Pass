import sqlite3

# Conectar ao banco de dados (ou criar um novo banco de dados se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER,
                    cidade TEXT)''')

# Inserir alguns dados de exemplo
cursor.execute("INSERT INTO clientes (nome, idade, cidade) VALUES ('Alice', 30, 'São Paulo')")
cursor.execute("INSERT INTO clientes (nome, idade, cidade) VALUES ('Bob', 25, 'Rio de Janeiro')")
cursor.execute("INSERT INTO clientes (nome, idade, cidade) VALUES ('Carlos', 40, 'Belo Horizonte')")
conn.commit()

# Consultar dados da tabela
cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

# Exibir os resultados
for linha in resultados:
    print(f"ID: {linha[0]}, Nome: {linha[1]}, Idade: {linha[2]}, Cidade: {linha[3]}")

# Fechar a conexão com o banco de dados
conn.close()
