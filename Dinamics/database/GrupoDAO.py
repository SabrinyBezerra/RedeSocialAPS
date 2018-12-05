from database.BD import *

class GrupoDAO():
    def __init__(self):
        self.cursor = BDcursor
        self.conn = BDconn

    def inserirGrupo(self,grupo):
        try:

            query = " INSERT INTO tb_grupo(id_user_admin,nome)" \
                    " VALUES (%s,%s) "

            values = (grupo.id_user_admin,grupo.nome)

            self.cursor.execute(query, values) # inserindo grupo no banco de dados

            self.conn.commit() # Confirmando inclusão do grupo no banco de dados

        except ErroNaInsercao:
            print(erroInsercao)

    def getIDgrupo(self,grupo):
        try:

            query = " SELECT id FROM tb_grupo" \
                    " WHERE id_user_admin LIKE %s AND nome LIKE %s "

            values = (grupo.id_user_admin,grupo.nome)

            self.cursor.execute(query, values)

            id = self.cursor.fetchall()[0][0]
            return id
        except:
            print(erroConsulta)

    def existGrupo(self,usuario,grupo):
        try:

            query = " SELECT * FROM tb_grupo" \
                    " WHERE id_user_admin LIKE %s AND nome LIKE %s "

            values = (usuario.id, grupo.nome)

            self.cursor.execute(query, values) # inserindo grupo no banco de dados

            result = self.cursor.fetchall()

            if result == []:
                return False # O grupo não existe
            else:
                return True # O grupo existe
        except ErroNaInsercao:
            print(erroInsercao)

    def getListGrupos(self,usuario):
        try:


            query = " SELECT gp.* FROM tb_participante_grupo AS pgp, tb_grupo AS gp " \
                    " WHERE pgp.id_participante LIKE %s AND gp.id LIKE pgp.id_grupo "

            values = (usuario.id,)

            self.cursor.execute(query, values) # buscando todos os grupo que o usuário é participante

            result = self.cursor.fetchall()

            return result # Retornandos os grupos do usuário

        except ErroNaInsercao:
            print(erroInsercao)

    def inserirParticipante(self,grupo,idDesc):
        try:

            query = " INSERT INTO tb_participante_grupo(id_grupo,id_participante) " \
                    " VALUES(%s,%s) "

            values = (grupo.id,idDesc)

            self.cursor.execute(query, values)

            self.conn.commit() # Confirmando imclusão no banco de dados

        except ErroNaInsercao:
            print(erroInsercao)


    def deletarGrupo(self,grupo):

        try:
            self.deletarTodosParticipantesGrupo(grupo) # Deletando em conjunto todos os participantes deste grupo
            self.deletarTodosMensGrupo(grupo) # Deletando em conjunto todas as mensagems deste grupo

            query = " DELETE FROM tb_grupo " \
                    " WHERE id_user_admin LIKE %s AND nome LIKE %s "

            values = (grupo.id_user_admin,grupo.nome)

            self.cursor.execute(query, values) # buscando todos os grupo do usuário

            self.conn.commit()# Confirmando exclusão no banco de dados
        except:
            print(erroDeletar)


    def getListParticipantes(self,grupo):
        try:

            query = " SELECT us.* FROM tb_usuario AS us " \
                    " JOIN tb_participante_grupo AS gp ON gp.id_grupo LIKE %s AND gp.id_participante LIKE us.id "


            values = (grupo.id,)

            self.cursor.execute(query, values) # buscando todos os participantes do grupo

            result = self.cursor.fetchall()

            return result # Retornando os participantes do grupo

        except ErroNaInsercao:
            print(erroInsercao)

    def existParticipante(self,grupo,idUser):
        """
            Função usada para verificar se existe um participante em certo grupo
        """
        try:

            query = " SELECT COUNT(*) FROM tb_participante_grupo " \
                    " WHERE id_grupo LIKE %s AND id_participante LIKE %s "

            values = (grupo.id,idUser)

            self.cursor.execute(query, values)

            result = self.cursor.fetchall()[0][0]

            if result == 1:
                return True # Existe este participante neste grupo
            else:
                return False # Não existe este participante neste grupo
        except:
            print(erroConsulta)

    def deletarTodosParticipantesGrupo(self,grupo):
        try:
            query = " DELETE FROM tb_participante_grupo " \
                    " WHERE id_grupo LIKE %s "

            values = (grupo.id,)

            self.cursor.execute(query, values)
            self.conn.commit() # Confirmando a exclusão dos participantes do grupo

        except:
            print(erroDeletar)

    def deletarTodosMensGrupo(self,grupo):
        try:
            query = " DELETE FROM tb_mensagem_participante_grupo " \
                    " WHERE id_grupo LIKE %s "

            values = (grupo.id,)

            self.cursor.execute(query, values)
            self.conn.commit() # Confirmando a exclusão das mensagems deste grupo

        except:
            print(erroDeletar)

    def deletarParticipanteGrupo(self,grupo,id_participante):
        try:
            query = " DELETE FROM tb_participante_grupo " \
                    " WHERE id_grupo LIKE %s AND id_participante LIKE %s "

            values = (grupo.id,id_participante)

            self.cursor.execute(query, values)
            self.conn.commit() # Confirmando a exclusão do participante no grupo

        except:
            print(erroDeletar)