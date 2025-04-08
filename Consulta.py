import pyodbc
import os
from dotenv import load_dotenv
from prettytable import PrettyTable

# Carregar variáveis de ambiente
load_dotenv()

# Montar string de conexão
dados_conexao = {
    'DRIVER': os.getenv('DB_DRIVER'),
    'SERVER': os.getenv('DB_SERVER'),
    'DATABASE': os.getenv('DB_DATABASE'),
    'Trusted_Connection': os.getenv('DB_TRUSTED'),
}

string_conexao = ';'.join([f'{chave}={valor}' for chave, valor in dados_conexao.items()])

# Conectar ao banco
conexao = pyodbc.connect(string_conexao)
cursor = conexao.cursor()

# Executar a consulta
query = "SELECT COUNT(Nome_Produto) as Quantidade, Marca_Produto FROM produtos GROUP BY Marca_Produto"
cursor.execute(query)
resultados = cursor.fetchall()

# Tabela formatada
tabela = PrettyTable()
tabela.field_names = [desc[0] for desc in cursor.description]

for linha in resultados:
    tabela.add_row(linha)

print(tabela)

cursor.close()
conexao.close()
