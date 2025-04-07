import pyodbc
from prettytable import PrettyTable

# Dados de conexão
dados_conexao = {
    'DRIVER': '{SQL Server}',
    'SERVER': 'ROBSON-ALVES\\SQLEXPRESS',
    'DATABASE': 'vendas',
    'Trusted_Connection': 'yes',
}

# String de conexão
string_conexao = ';'.join([f'{chave}={valor}' for chave, valor in dados_conexao.items()])

# Conectar ao banco de dados
conexao = pyodbc.connect(string_conexao)
cursor = conexao.cursor()

# Consulta SQL
query = "SELECT COUNT(Nome_Produto) as Quantidade, Marca_Produto FROM produtos GROUP BY Marca_Produto"

# Executar a consulta
cursor.execute(query)

# Obter os resultados
resultados = cursor.fetchall()

# Criar uma tabela para exibir os resultados
tabela_resultados = PrettyTable()
tabela_resultados.field_names = [desc[0] for desc in cursor.description]

# Adicionar os dados à tabela
for linha in resultados:
    tabela_resultados.add_row(linha)

# Imprimir a tabela formatada
print(tabela_resultados)

# Fechar a conexão
conexao.close()
