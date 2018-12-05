from database.RedeSocialDAO import RedeSocialDAO
from database.BD import *
from model.Usuario import Usuario
from model.Mensagem import Mensagem
from model.Grupo import Grupo
from model.Amigo import Amigo
from config.ConstErros import *

class RedeSocial():
    def __init__(self, nome, vercao):
        self.nome = nome
        self.vercao = vercao

    def criarBanco(self):
        redesocialDAO = RedeSocialDAO()
        redesocialDAO.criarBD()

    def menuUsuarioAmizade(self,usuario):
        """
            Amigos do Usuário - Menu de opções envolvendo um usuário e seus amigos e solicitações de amizades
        """
        print("\n\n\n")
        amigo = Amigo()

        while (True):
            amigo.carregarAmigos(usuario)
            print("========================================\n"
                  " %s - Amizades\n"
                  "========================================\n"
                  "1) Ver Meus Amigos : %i \n"
                  "2) Desfazer Amizade\n"
                  "3) Enviar Solicitaçao De Amizade\n"
                  "4) Ver solicitações De Amizade : %i\n"
                  "0) Voltar Para o Home De Usuário\n"
                  "----------------------------------------" % (usuario.nome,usuario.totalAmigos(),usuario.totalSolicitacoes()))
            try:
                op = int(input(">>:"))
                if op == 1:
                    amigo.verAmigos(usuario)
                elif op == 2:
                    amigo.desfazerAmizade(usuario)
                elif op == 3:
                    amigo.enviarSolicitacaoAmizade(usuario)
                elif op == 4:
                    amigo.solicitacoesAmizade(usuario)
                elif op == 0:
                    break # Encerrando loop e voltando para o Home do usuário
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)

    def menuUsuarioMensagems(self,usuario):
        """
            Mensagems do usuário - Menu de controle de envio recebimento e vizualização das mensagems do usuário
        """
        print("\n\n\n")
        mensagem = Mensagem()

        while (True):
            mensagem.carregarMensagems(usuario)
            print("============================================\n"
                  " %s - Mensagems\n"
                  "============================================\n"
                  "1) Vizualizar Mensagems\n"
                  "2) Enviar Mensagem Para Um Amigo\n"
                  "3) Enviar Mensagem Para Um Desconhecido\n"            
                  "0) Voltar Para o Home De Usuario\n"
                  "--------------------------------------------" % (usuario.nome))

            try:
                op = int(input(">>:"))  # Armazenando a escolha do usuário
                if op == 1:
                    mensagem.caixaDeMensagem(usuario)
                elif op == 2:
                    mensagem.criarMensAmigo(usuario)
                elif op == 3:
                    mensagem.criarMensDesconhecido(usuario)
                elif op == 0:
                    break # Encerrando loop e retornando ao menu de Home
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)


    def menuUsuarioGrupos(self,usuario):
        """
             Grupos do usuário - Menu de interação entre um usuário e os grupos da rede social em que ele participa ou cria
         """
        print("\n\n\n")
        grupo = Grupo()

        while (True):

            grupo.carregarGrupos(usuario)

            print("============================================\n"
                  " %s - Grupos\n"
                  "============================================\n"
                  "1) Criar Um Grupo \n"
                  "2) Excluir Um Grupo\n"
                  "3) Vizualizar Grupos : %i\n"
                  "4) Vizualizar Grupos Com Participantes\n"
                  "5) Enviar Mensagem Para Um Grupo\n"
                  "6) Vizualizar Mensagem De Um Grupo\n"
                  "7) Adicionar Usuário Em Um Grupo\n"
                  "8) Excluir Usuários Em Um Grupo\n"
                  "9) Sair De Um Grupo\n"
                  "0) Voltar Para o Home De Usuário\n"
                  "--------------------------------------------" % (usuario.nome,usuario.totalGrupos()))

            try:
                op = int(input(">>:"))  # Armazenando a escolha do usuário
                if op == 1:
                    grupo.criarGrupo(usuario)
                elif op == 2:
                    grupo.excluirGrupo(usuario)
                elif op == 3:
                    grupo.listarGrupos(usuario)
                elif op == 4:
                    grupo.listarGruposParticipantes(usuario)
                elif op == 5:
                    grupo.enviarMensagem(usuario)
                elif op == 6:
                    grupo.verMensagems(usuario)
                elif op == 7:
                    grupo.adicionarParticipante(usuario)
                elif op == 8:
                    grupo.exluirParticipante(usuario)
                elif op == 9:
                    grupo.sairDeGrupo(usuario)
                elif op == 0:
                    break  # Encerrando loop e retornando ao menu de Home
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)

    def menuUsuario(self,usuario):
        """
            Home do Usuário - Menu Principal que fais a interação com os outros menus e a manipulação principal do usuário
        """

        while (True):
            print("========================================\n"
                  " %s - Home\n"
                  "========================================\n"
                  "1) Atualizar Minha Conta\n"
                  "2) Ver Minha Conta\n"
                  "3) Apagar Minha Conta\n"
                  "4) Menu De Amizades\n"
                  "5) Menu De Mensagems\n"
                  "6) Menu De Grupos\n" 
                  "0) Sair\n"
                  "----------------------------------------" % (usuario.nome))

            try:
                op = int(input(">>:"))  # Armazenando a escolha do usuário
                if op == 1:
                    usuario.atualizarUsuario() # Chamando função de atualização dos dados <Atributos> do usuário
                elif op == 2:
                    usuario.verDados() # Chamando função que mostra os dados <Atributos> do usuário
                elif op == 3:
                    usuario.removerUsuario() # Deletando usuário da rede social
                    break
                elif op == 4:
                    self.menuUsuarioAmizade(usuario)
                elif op == 5:
                    self.menuUsuarioMensagems(usuario)
                elif op == 6:
                    self.menuUsuarioGrupos(usuario)
                elif op == 0:
                    print("\nConta encerrada com sucesso\n")
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)

    def openConta(self):
       amigo = Amigo()
       mensagem = Mensagem()
       grupo = Grupo()
       usuario = Usuario()

       usuario.email = input("\nE-mail: ")
       usuario.senha = input("Senha: ")

       autenticado = usuario.autenticado()

       if autenticado:
          print("\n")
          usuario.carregarUsuarioBD()
          amigo.carregarAmigos(usuario) # Carregando os amigos do usuário
          mensagem.carregarMensagems(usuario) # Carregando as mensagems do usuário
          grupo.carregarGrupos(usuario) # Carregando os grupos do usuário
          self.menuUsuario(usuario)
       else:
           print("\nE-mail ou senha inválida\n")

    def newConta(self):
        usuario = Usuario()
        result = usuario.criarUsuario()

        if result: # Se o usuário for inserido com sucesso result estara como True
            print("\nBem vindo %s a rede Dinamics\n" %(usuario.nome))
            self.menuUsuario(usuario) # Redirecionando para o menu de Home do usuário
        else:
            print("\nVocê não pode se cadastrar porque já existe um cadastro com este E-mail\n")

    def finichid(self):
        # Fechando a conexão
        BDconn.close()
        BDcursor.close()

        # Encerrando a aplicação - Rede Social
        print("\n%s Encerrado...\n" % (self.nome))
        exit(0)