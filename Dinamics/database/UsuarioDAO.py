from database.BD import * # Importando os atributos referentes ao banco de dados

class UsuarioDAO():
    def __init__(self):
        self.cursor = BDcursor
        self.conn = BDconn

    def inserirUsuario(self,usuario):
        try:

            query = " INSERT INTO tb_usuario(email, senha, nome, data_nascimento, genero, estado_civil, profissao)" \
                    " VALUES (%s,%s,%s,%s,%s,%s,%s) "

            values = (usuario.email,usuario.senha,usuario.nome,usuario.data_nascimento,usuario.genero,usuario.estado_civil,usuario.profissao)

            self.cursor.execute(query, values) # Inserindo usuário no banco de dados
            self.conn.commit() # Confirmando inclusão do usuario no banco de dados

            return True # Usuário inserido com sucesso
        except ErroNaInsercao:
            return False # Erro na inclusão do usuário

    def atualizarUsuario(self,usuario):
        try:
            query =    " UPDATE tb_usuario " \
                       " SET email = %s, senha = %s, nome = %s, data_nascimento = %s, genero = %s, estado_civil = %s, profissao = %s " \
                       " WHERE id LIKE %s "

            values = (usuario.email,usuario.senha,usuario.nome,usuario.data_nascimento,usuario.genero,usuario.estado_civil,usuario.profissao,usuario.id)

            self.cursor.execute(query, values)
            self.conn.commit() # Confirmando atualização do usuario no banco de dados

        except:
            print(erroAtualizao)


    def deletarUsuario(self,usuario):
        try:

            query = " DELETE FROM tb_usuario " \
                    " WHERE id LIKE %s "

            values = (usuario.id,)

            self.cursor.execute(query, values)
            self.conn.commit() # Confirmando exclusão no banco de dados

        except:
            print(erroDeletar)

    def usuarioExist(self,email):
        """
            Verificando se existe algum usuário com este email na rede social
        """
        try:

            query = " SELECT email FROM tb_usuario" \
                    " WHERE email LIKE %s "

            values = (email,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()

            if result == []:
                return False # O usuário não existe
            else:
                return True # O usuário existe
        except:
            print(erroConsulta)


    def getSenhaUsuario(self,email):
        """
            Função que retorna a senha do usuario que possue o email passado como parâmetro
        """
        try:
            query = " SELECT senha FROM tb_usuario" \
                    " WHERE email LIKE %s "

            values = (email,)

            self.cursor.execute(query, values)

            senha = self.cursor.fetchall()[0][0]

            return senha

        except:
            print(erroConsulta)


    def autenticarUsuario(self,usuario):
        try:
            existe = self.usuarioExist(usuario.email)

            if existe:
                senhaUser = self.getSenhaUsuario(usuario.email)
                if usuario.senha == senhaUser:
                    return True # O usuário digitol seus dados corretamente
                else:
                    return False # A senha não corresponde

            else:
                return False # O usuário não existe na rede social

        except:
            print(erroConsulta)

    def getIdUsuario(self,email):
        """
            Função que retorna o ID do usuário que possue o email passado como parâmetro
        """
        try:

            query = " SELECT id FROM tb_usuario" \
                    " WHERE email LIKE %s "

            values = (email,)

            self.cursor.execute(query, values)

            id = self.cursor.fetchall()[0][0]
            return id
        except:
            print(erroConsulta)


    def getUsuario(self,email):
        try:
            query = " SELECT * FROM tb_usuario" \
                    " WHERE email LIKE %s "

            values = (email,)

            self.cursor.execute(query, values)

            usuario = self.cursor.fetchall()
            return usuario[0]

        except:
            print(erroConsulta)


    def getListUsuario(self,nomeBusca):
        try:
            query = " SELECT nome,email,id FROM tb_usuario "\
                    " WHERE nome LIKE %s "

            values = ('%'+nomeBusca+'%',) # Colocando os porcentagems para trazer todos os usuário que tenham alguma parte deste nome

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result

        except:
            print(erroConsulta)

    def getListAmigos(self,id_user):


            query = " SELECT us.* FROM tb_usuario AS us "\
                    " JOIN tb_amigo AS am ON am.id_user LIKE us.id OR am.id_amigo LIKE us.id " \
                    " WHERE (am.id_user LIKE %s or am.id_amigo LIKE %s) AND us.id != %s "

            values = (id_user,id_user,id_user)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result # Retornando lista de usuario que são amigos de id_user


    def getNomeUsuario(self,id_user):
        try:

            query = " SELECT nome FROM tb_usuario " \
                    " WHERE id LIKE %s "

            values = (id_user,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchall()

            return result[0][0]

        except:
            print(erroConsulta)


