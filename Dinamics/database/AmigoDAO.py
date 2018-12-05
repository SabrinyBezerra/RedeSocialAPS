from database.BD import * # Importando os atributos referentes ao banco de dados
import datetime

class AmigoDAO():
    def __init__(self):
        self.conn = BDconn
        self.cursor = BDcursor

    def existSolicitacao(self,id_user,id_amigo):
        """
            Função usada para verificar se existe uma solicitação de amizade usando os ids passados por parâmetro
        """
        try:

            query = " SELECT COUNT(*) FROM tb_solicitacao_amizade " \
                    " WHERE id_user_envia LIKE %s AND id_user_recebe LIKE %s "

            values = (id_user,id_amigo)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()[0][0]

            if result == 1:
                return True # Já foi feita uma solicitação para usuário de id_amigo
            else:
                return False # Não existe solicitações de amizade para o usuário de id_amigo feito por id_user
        except:
            print(erroConsulta)

    def enviarSolicitacao(self,id_user,id_amigo):
        """
            Função que vai enviar a solicitação para a tabela de solicitações de amizades
        """
        try:
            data = datetime.datetime.today()

            query = " INSERT INTO tb_solicitacao_amizade(id_user_envia,id_user_recebe,data_envio) " \
                    " VALUES ( %s,%s,%s ) " \


            values = (id_user,id_amigo,data)

            self.cursor.execute(query, values) # Inserindo a solicitação na tabela
            self.conn.commit() # Confirmando a inclusão dos dados
        except:
            print(erroInsercao)


    def getSolicitacoesEnviadas(self,id_user):
        try:

            query = " SELECT us.nome, so_am.data_envio FROM tb_usuario AS us " \
                    " JOIN tb_solicitacao_amizade AS so_am ON us.id LIKE so_am.id_user_recebe " \
                    " WHERE so_am.id_user_envia LIKE %s "

            values = (id_user,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result # Retornando a lista com os nomes e as data de envio das solicitação de amizade enviadas pelo usuário id_user

        except:
            print(erroConsulta)

    def getTotalSolicitacoesEnviadas(self,id_user):
        try:

            query = " SELECT COUNT(*) FROM tb_usuario AS us " \
                    " JOIN tb_solicitacao_amizade AS so_am ON us.id LIKE so_am.id_user_recebe " \
                    " WHERE so_am.id_user_envia LIKE %s "

            values = (id_user,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()[0][0]
            return result # Retornando o total de solicitações enviadas pelo usuário id_user

        except:
            print(erroConsulta)

    def getSolicitacoesRecebidas(self,id_user):
        try:

            query = " SELECT us.nome, us.email, us.id FROM tb_usuario AS us " \
                    " JOIN tb_solicitacao_amizade AS so_am ON us.id LIKE so_am.id_user_envia " \
                    " WHERE so_am.id_user_recebe LIKE %s "

            values = (id_user,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result # Retornando a lista com os nomes e o email das solicitação de amizade enviadas para usuário id_user

        except:
            print(erroConsulta)

    def getTotalSolicitacoesRecebidas(self,id_user):
        try:

            query = " SELECT COUNT(*)FROM tb_usuario AS us " \
                    " JOIN tb_solicitacao_amizade AS so_am ON us.id LIKE so_am.id_user_envia " \
                    " WHERE so_am.id_user_recebe LIKE %s "

            values = (id_user,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()[0][0]
            return result # Retornando a lista com os nomes e o email dos usuarios que enviaram solicitações de amizades para usuário id_user

        except:
            print(erroConsulta)

    def deletarSolicitacao(self,usuario,id_amigo):
        try:

            query = " DELETE FROM tb_solicitacao_amizade" \
                    " WHERE id_user_recebe = %s AND id_user_envia = %s "

            values = (usuario.id,id_amigo)

            self.cursor.execute(query, values)
            self.conn.commit() # Confirmando exclusão na tabela de solicitações de amizades

        except:
            print(erroDeletar)

    def adicionarAmigo(self,usuario,id_amigo):
        try:

            query = " INSERT INTO tb_amigo(id_user,id_amigo)" \
                    " VALUES (%s,%s) "

            values = (usuario.id,id_amigo)

            self.cursor.execute(query, values)
            self.conn.commit() # Confirmando inserção na tabela de amigos

        except:
            print(erroInsercao)

    def deletarAmizade(self,usuario,id_amigo):
        try:

            query = " DELETE FROM tb_amigo" \
                    " WHERE (id_user LIKE %s AND id_amigo LIKE %s) OR " \
                    " (id_user LIKE %s AND id_amigo LIKE %s) "

            values = (usuario.id,id_amigo,id_amigo,usuario.id)

            self.cursor.execute(query, values)

        except:
            print(erroDeletar)
