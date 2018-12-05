from database.BD import *

class MensagemGrupoDAO():
    def __init__(self):
        self.conn = BDconn
        self.cursor = BDcursor

    def enviarMensagem(self,mensagemGrupo):
        try:

            query = " INSERT INTO tb_mensagem_participante_grupo(id_grupo,id_participante,mensagem,data_envio) " \
                    " VALUES(%s,%s,%s,%s) "

            values = (mensagemGrupo.id_grupo,mensagemGrupo.id_participante,mensagemGrupo.mensagem,mensagemGrupo.data_envio)

            self.cursor.execute(query, values)

            self.conn.commit() # Confirmando inclusão no banco de dados

        except ErroNaInsercao:
            print(erroInsercao)

    def getListMensagemsGrupo(self,grupo):
        try:

            query = " SELECT * FROM tb_mensagem_participante_grupo " \
                    " WHERE id_grupo = %s "

            values = (grupo.id,)

            self.cursor.execute(query, values)

            result = self.cursor.fetchall()

            return result

        except ErroNaInsercao:
            print(erroInsercao)