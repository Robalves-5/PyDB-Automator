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
    # Comando SQL para deletar uma linha (substitua condicao_deletar pela sua condição específica)
    condicao_deletar = "ID_Produto = ?"
    comando_delete = f"DELETE FROM produtos WHERE {condicao_deletar}"

    # Valor para a condição (substitua pelo valor específico)
    valor_condicao = 17

    # Executar o comando SQL de exclusão
    cursor.execute(comando_delete, valor_condicao)

    # Commit da transação
    conexao.commit()

    print('Exclusão bem-sucedida')
else:
    print('A tabela "produtos" não foi encontrada no banco de dados "vendas".')

# Fechar o cursor e a conexão
cursor.close()
conexao.close()

