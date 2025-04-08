import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

# Dados de conexão
dados_conexao = (
    f"DRIVER={{SQL Server}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_NAME')};"
    f"Trusted_Connection=yes;"
)

# Conectar ao banco de dados
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem-sucedida')

# Criar um cursor
cursor = conexao.cursor()

# Verificar se a tabela 'produtos' existe
if cursor.tables(table='produtos', tableType='TABLE', schema='dbo').fetchone():
    # Verificar se o produto com o ID existe
    valor_condicao = 17
    cursor.execute("SELECT * FROM produtos WHERE ID_Produto = ?", valor_condicao)
    linha = cursor.fetchone()

    if linha:
        cursor.execute("DELETE FROM produtos WHERE ID_Produto = ?", valor_condicao)
        conexao.commit()
        print(f"Produto com ID {valor_condicao} excluído com sucesso.")
    else:
        print(f"Nenhum produto com ID {valor_condicao} foi encontrado.")
else:
    print('A tabela "produtos" não foi encontrada no banco de dados.')

# Fechar o cursor e a conexão
cursor.close()
conexao.close()
