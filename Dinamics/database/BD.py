import mysql.connector

"""
    Arquivo responsável por conter a configuração da conexão a conexão o cursor e os Erros, do banco de dados. 
    para que estes sejam usados por toda a aplicação
"""

BDconfig = {  "user": "root",
            "password": "",
            "host": "127.0.0.1",
            'database': "dinamics",
            "port": "3306",
            'raise_on_warnings': True
          }

BDconn = mysql.connector.connect(**BDconfig)
BDcursor = BDconn.cursor()


# Atributos referrentes aos erros no banco de dados
ErroNaInsercao  = mysql.connector.IntegrityError

# Erros referentes a manipulação de dados no banco de dados
erroConsulta = ("\nErro na consulta\n") # Erro ao fazer uma consulta ao banco de dados
erroAtualizao = ("\nErro na atualização\n") # Erro ao atualizar alguma entidade no banco de dados
erroDeletar = ("\nErro ao deletar\n") # Erro ao deletar uma entidade no banco de dados
erroInsercao = ("\nErro ao inserir\n") # Erro ao inserir algum dado no banco de dados