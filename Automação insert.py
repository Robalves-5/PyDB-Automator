import pyodbc

# Dados de conexão
dados_conexao = (
    'DRIVER={SQL Server};' 
    'SERVER=ROBSON-ALVES\\SQLEXPRESS;'  
    'DATABASE=vendas;'
    'Trusted_Connection=yes;'  
)

# Conectar ao banco de dados
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem-sucedida')

# Criar um cursor
cursor = conexao.cursor()

# Verificar se a tabela 'produtos' existe
if cursor.tables(table='produtos', tableType='TABLE').fetchone():
    # Comando SQL com placeholders
    comando = """
        INSERT INTO produtos (ID_Produto, Nome_Produto, ID_Categoria, Marca_Produto, Num_Serie, Preco_Unit, Custo_Unit)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    # Valores a serem inseridos
    valores = (16, 'Fone de Ouvido Tune T5001', 4, 'PHILCO', 'HDP-JB-091935', 900, 500)

    # Executar o comando SQL com os valores
    cursor.execute(comando, valores)

    # Commit da transação
    conexao.commit()

    print('Inserção bem-sucedida')
else:
    print('A tabela "produtos" não foi encontrada no banco de dados "vendas".')

# Fechar o cursor e a conexão
cursor.close()
conexao.close()



