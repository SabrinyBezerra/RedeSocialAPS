import unittest
from model.Usuario import Usuario
from database.UsuarioDAO import UsuarioDAO

class TestCrudBD(unittest.TestCase):

    def get_user_test(self):
        # Função que retorna um usuáruio utilizado para os testes na classe em geral
        user = Usuario("pedro@gmail.com","123","Pedro","1998-12-28","Masculino","solteiro","Bombeiro")
        return user

    def test_A_insercao(self):
        # Verificando se a aplicação esta inserindo o usuário no BD
        user = self.get_user_test()
        usuarioDAO = UsuarioDAO()
        result = usuarioDAO.inserirUsuario(user)
        self.assertEquals(True,result)

    def test_B_consulta(self):
        # Verificando se a aplicação esta consultando e retornando um id de um usuário pesquisado no BD
        user = self.get_user_test()
        usuarioDAO = UsuarioDAO()
        user.id = usuarioDAO.getIdUsuario(user.email) # Atribuindo o ID do usuário
        self.assertNotEqual(None,user.id) # Se o id for direfente de None

    def test_C_atualizacao(self):
        # Verificando se a aplicação esta atualizando um usuário no banco de dados
        user = self.get_user_test()
        usuarioDAO = UsuarioDAO()
        user.id = usuarioDAO.getIdUsuario(user.email) # Atribuindo o ID do usuário
        user.nome = "Pedro Manoel"
        user.email = "PedroM@gmail.com"
        user.senha = "Ocride123"
        usuarioDAO.atualizarUsuario(user)  # Atualizando o cadastro no banco de dados passando o usuário como parâmetro
        user.carregarUsuarioBD() # Fazendo uma consulta e carregando u usuário direto do banco de dados
        self.assertEqual(user.nome,"Pedro Manoel")
        self.assertEqual(user.email,"PedroM@gmail.com")
        self.assertEqual(user.senha,"Ocride123")

    def test_D_remocao(self):
        # Verificando se a aplicação esta removendo um usuário do banco de dados
        user = self.get_user_test()
        usuarioDAO = UsuarioDAO()
        user.email = "PedroM@gmail.com" # Para que a consulta do ID não result em erro
        user.id = usuarioDAO.getIdUsuario(user.email) # Atribuindo o ID do usuário
        result = usuarioDAO.deletarUsuario(user)
        self.assertEquals(True,result)