from config.ConstErros import *
from database.BD import *

class MensagemDAO():
    def __init__(self):
        self.conn = BDconn
        self.cursor = BDcursor

    def enviarMensagem(self,mensagem):
        try:

            query = " INSERT INTO tb_mensagem(id_user_envia,id_user_recebe,mensagem,data_envio)" \
                    " VALUES (%s,%s,%s,%s) "

            values = (mensagem.id_user_envia,mensagem.id_user_recebe,mensagem.mensagem,mensagem.data_envio)

            self.cursor.execute(query, values) # inserindo mensagem no banco de dados

            self.conn.commit() # Confirmando inclusão da mensagem no banco de dados

            return True # Mensagem inserida com sucesso
        except ErroNaInsercao:
            return False # Erro na inclusão da mensagem

    def getListMensagemUser(self,usuario):
        try:

            query = " SELECT * FROM tb_mensagem " \
                    " WHERE id_user_envia = %s or id_user_recebe = %s "

            values = (usuario.id,usuario.id)

            self.cursor.execute(query, values) # inserindo mensagem no banco de dados

            return self.cursor.fetchall()

        except:
            print(erroConsulta)
