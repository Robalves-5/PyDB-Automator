import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Dados de conexão
dados_conexao = (
    f"DRIVER={os.getenv('DB_DRIVER')};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_DATABASE')};"
    f"Trusted_Connection={os.getenv('DB_TRUSTED')};"
)

# Conectar ao banco de dados
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem-sucedida')

# Criar um cursor
cursor = conexao.cursor()

# Verificar se a tabela 'produtos' existe
if cursor.tables(table='produtos', tableType='TABLE').fetchone():
    comando = """
        INSERT INTO produtos (ID_Produto, Nome_Produto, ID_Categoria, Marca_Produto, Num_Serie, Preco_Unit, Custo_Unit)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    valores = (16, 'Fone de Ouvido Tune T5001', 4, 'PHILCO', 'HDP-JB-091935', 900, 500)
    cursor.execute(comando, valores)
    conexao.commit()
    print('Inserção bem-sucedida')
else:
    print('A tabela "produtos" não foi encontrada no banco de dados.')

cursor.close()
conexao.close()
