from models.Usuario import Usuario
from database.DAO import DAO

class UsuarioDAO(DAO):
    def __init__(self):
        super(UsuarioDAO, self).__init__()

    def inserirUsuario(self, usuario):
        query = " INSERT INTO tb_usuario(email, senha, nome, data_nascimento, genero, estado_civil)" \
                " VALUES (%s,%s,%s,%s,%s,%s) "

        values = (usuario.email, usuario.senha, usuario.nome, usuario.data_nascimento, usuario.genero, usuario.estado_civil)
        return super(UsuarioDAO, self).insert(query, values) # Inserindo usuário no banco de dados


    def atualizarUsuario(self, usuario):
        try:
            query =    " UPDATE tb_usuario " \
                       " SET email = %s, senha = %s, nome = %s, data_nascimento = %s, genero = %s, estado_civil = %s" \
                       " WHERE id LIKE %s "

            values = (usuario.email,usuario.senha,usuario.nome,usuario.data_nascimento,usuario.genero,usuario.estado_civil,usuario.id)

            self.execute(query, values)

        except:
            print("Erro no BD - Atualização.")
            return False

    def deletarUsuario(self, id):
        try:

            query = " DELETE FROM tb_usuario " \
                    " WHERE id LIKE %s "

            values = (id,)

            self.execute(query, values)

            return True

        except:
            print("Erro no BD - Exclusão.")
            return False

    def listarUsuarios(self):
        try:
            query = "SELECT * FROM tb_usuario"
            result = self.get_rows(query)

            usuarios = []

            for user in result:
                id = user[0]
                email = user[1]
                senha = user[2]
                nome = user[3]
                data_nascimento = user[4]
                genero = user[5]
                perfil_publico = user[6]
                estado_civil = user[7]

                usuario = Usuario(email, senha, nome, data_nascimento, genero, perfil_publico, estado_civil, id)
                usuarios.append(usuario)

            return usuarios

        except:
            print("Erro na consulta. - Listagem de usuários.")
            return False

    def usuarioExist(self,email):
        """
            Verificando se existe algum usuário com este email na rede social
        """
        try:

            query = " SELECT email FROM tb_usuario" \
                    " WHERE email LIKE %s "

            values = (email,)

            result = self.get_rows(query, values)

            if result == []:
                return False # O usuário não existe
            else:
                return True # O usuário existe
        except:
            print("Erro na consulta.")


    def getUsuario(self,email):
        try:
            query = " SELECT * FROM tb_usuario" \
                    " WHERE email LIKE %s "

            values = (email,)

            usuario = self.get_row(query, values)
            return usuario

        except:
            print("Erro na consulta.")
            return False


    def getListUsuario(self, nomeBusca):
        try:
            query = " SELECT nome,email,id FROM tb_usuario "\
                    " WHERE nome LIKE %s "

            values = ('%'+nomeBusca+'%',) # Colocando os porcentagems para trazer todos os usuário que tenham alguma parte deste nome

            result = self.get_rows(query, values)
            return result

        except:
            print("Erro na consulta.")
            return False

    def getListAmigos(self, id_user):

        try:
            query = " SELECT us.* FROM tb_usuario AS us "\
                    " JOIN tb_amigo AS am ON am.id_user LIKE us.id OR am.id_amigo LIKE us.id " \
                    " WHERE (am.id_user LIKE %s or am.id_amigo LIKE %s) AND us.id != %s "

            values = (id_user,id_user,id_user)

            result = self.get_rows(query, values)

            return result # Retornando lista de usuario que são amigos de id_user
        except:
            print("Erro na consulta - Lista de amigos.")
            return False


    def getNomeUsuario(self, id_user):
        try:

            query = " SELECT nome FROM tb_usuario " \
                    " WHERE id LIKE %s "

            values = (id_user,)

            result = self.get_row(query, values)

            return result[0]

        except:
            print("Erro na consulta - Nome do usuário por ID.")


