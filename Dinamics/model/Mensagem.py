from config.ConstErros import numeroForaDeContesto, numeroInvalido
from database.UsuarioDAO import UsuarioDAO
from model.Usuario import Usuario
from database.MensagemDAO import MensagemDAO
from model.Amigo import Amigo
import datetime
from config import *

class Mensagem():
    def __init__(self,id=None,id_user_envia=None,id_user_recebe=None,mensagem=None,data_envio=None):
        self.id = id
        self.id_user_envia = id_user_envia
        self.id_user_recebe = id_user_recebe
        self.mensagem = mensagem
        self.data_envio = data_envio

    def criarMensAmigo(self,usuario):
        if usuario.totalAmigos() == 0:
            print("\nVocê não possue amigos\n")
        else:
            mensagemDAO = MensagemDAO()
            amigo = Amigo()

            amigo.verAmigosNome(usuario) # Listando amigos para o usuário escolher para quem vai enviar a mensagem
            print("OBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Mensagems\n")
            print("--------------------------------------------------------")
            print("Digite o número do amigo que deseja enviar a mensagem")
            print("--------------------------------------------------------")
            while(True):
                try:
                    numAmigo = int(input(">>:"))  # Armazenando a escolha do usuário
                    if (numAmigo > usuario.totalAmigos() or numAmigo < 0):
                        print("\nVocê não tem nenhum amigo atribuido a este número\n")
                        break # Encerrando loop
                    elif numAmigo == 0:
                        break
                    else:
                        self.id_user_envia = usuario.id
                        self.id_user_recebe = usuario.amigos[numAmigo-1].id # Atribuindo o ID do amigo que o usuário escolheu
                        self.data_envio = datetime.datetime.today()
                        self.mensagem = input("Mensagem: ")
                        mensagemDAO.enviarMensagem(self)
                        print("\nMensagem enviada\n")
                        break
                except ValueError:
                    print(numeroInvalido)


    def criarMensDesconhecido(self,usuario):

        usuarioDAO = UsuarioDAO()
        mensagemDAO = MensagemDAO()

        print("\nPara enviar uma mensagem para um usuário que não é seu amigo você precissa informar o E-mail dele\n")

        email = input("E-mail do usuário: ")

        exist = usuarioDAO.usuarioExist(email)

        if exist:
            self.id_user_envia = usuario.id
            self.id_user_recebe = usuarioDAO.getIdUsuario(email)
            self.data_envio = datetime.datetime.today()
            self.mensagem = input("\nMensagem: ")
            if mensagemDAO.enviarMensagem(self):  # Se a mensagem for enviada a função retorna True
                print("\nMensagem enviada\n")
        else:
            print("\nNão existe nenhum usuário com este E-mail na rede Nicks\n")

    def vizualizarMensagemAmigo(self,usuario,num_amigo):
        amigo = usuario.amigos[num_amigo]
        self.carregarMensagems(usuario)
        temMensagems = False
        print("\n\n\n")
        print("==================================================================")
        print("\n--------------------------------------------------------")
        print(" DE %s PARA %s" %(usuario.nome,amigo.nome))
        print("----------------------------------------------------------")
        print("==================================================================\n")
        for mensagem in usuario.mensagems:
            if mensagem.id_user_envia == usuario.id and mensagem.id_user_recebe == amigo.id: # Exibindo mensgens do usuário para este amigo
                temMensagems = True
                print("%s : %s\n"
                      " --------------------------------------------------\n"
                      " * %s                                              \n"
                      "                                                   \n"
                      "                                                   \n"
                      " ---------------------------------------------------\n"%(usuario.nome,mensagem.data_envio,mensagem.mensagem))
            elif mensagem.id_user_envia == amigo.id and mensagem.id_user_recebe == usuario.id: # Exibindo mensagens deste amigo para o usuário
                temMensagems = True
                print("                                    %s : %s\n"
                      "           --------------------------------------------------\n"
                      "           * %s                                              \n"
                      "                                                             \n"
                      "                                                             \n"
                      "           --------------------------------------------------\n"%(amigo.nome,mensagem.data_envio,mensagem.mensagem))
        if temMensagems:
            print("\nFim das mensagems\n")
        else:
            print("\nNão existem mensagem entre você e este amigo\n")
        print("========================================================")

    def vizualizarMensagemDesconhecido(self,usuario,idDesc,emailDesc):
            self.carregarMensagems(usuario)
            temMensagems = False
            print("\n\n\n")
            print("==================================================================")
            print("\n--------------------------------------------------------")
            print(" DE %s PARA %s" % (usuario.nome, emailDesc))
            print("----------------------------------------------------------")
            print("==================================================================\n")
            for mensagem in usuario.mensagems:
                if mensagem.id_user_envia == usuario.id and mensagem.id_user_recebe == idDesc:  # Exibindo mensgens do usuário para este amigo
                    temMensagems = True
                    print("%s : %s\n"
                          " --------------------------------------------------\n"
                          " * %s                                              \n"
                          "                                                   \n"
                          "                                                   \n"
                          " ---------------------------------------------------\n" % (
                          usuario.nome, mensagem.data_envio, mensagem.mensagem))
                elif mensagem.id_user_envia == idDesc and mensagem.id_user_recebe == usuario.id:  # Exibindo mensagens deste amigo para o usuário
                    temMensagems = True
                    print("                                    %s : %s\n"
                          "           --------------------------------------------------\n"
                          "           * %s                                              \n"
                          "                                                             \n"
                          "                                                             \n"
                          "           --------------------------------------------------\n" % (
                          emailDesc, mensagem.data_envio, mensagem.mensagem))
            if temMensagems:
                print("\nFim das mensagems\n")
            else:
                print("\nNão existem mensagem entre você e este amigo\n")
            print("========================================================")

    def carregarMensagems(self,usuario):
        mensagemDAO = MensagemDAO()
        usuario.mensagems = []
        mensagems = mensagemDAO.getListMensagemUser(usuario)

        for mensagem in mensagems:
            mensagemUser = Mensagem()
            mensagemUser.id = mensagem[0]
            mensagemUser.id_user_envia = mensagem[1]
            mensagemUser.id_user_recebe = mensagem[2]
            mensagemUser.mensagem = mensagem[3]
            mensagemUser.data_envio = mensagem[4]
            usuario.mensagems.append(mensagemUser) # Adicionando a mensagem a lista de mensagems do usuário


    def verMensAmigo(self,usuario):

        if usuario.totalAmigos() == 0:
            print("\nVocê não possue amigos\n")
        else:

            amigo = Amigo()


            amigo.verAmigosNome(usuario) # Listando amigos para o usuário escolher para quem vai enviar a mensagem
            print("OBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Mensagems\n")
            print("-----------------------------------------------------------")
            print("Digite o número do amigo que deseja vizualizar sa mensagems")
            print("-----------------------------------------------------------")
            while(True):
                try:
                    numAmigo = int(input(">>:"))  # Armazenando a escolha do usuário
                    if (numAmigo > usuario.totalAmigos() or numAmigo < 0):
                        print("\nVocê não tem nenhum amigo atribuido a este número\n")
                        break # Encerrando loop
                    elif numAmigo == 0:
                        break
                    else:
                        self.vizualizarMensagemAmigo(usuario,numAmigo-1)  # Enviando o usuário e o número do amigo para edentificalo na lista de amigos
                        break
                except ValueError:
                    print(numeroInvalido)


    def existMensEmail(self,usuario,id_desc):
        for mensagem in usuario.mensagems:
            if ((mensagem.id_user_recebe == id_desc and mensagem.id_user_envia == usuario.id)
               or(mensagem.id_user_envia == id_desc and mensagem.id_user_recebe == usuario.id)):
                return True # Existem mensagems entre o usuário e o usuário desconhecido
        return False # Não existem mensagems entre o usuário e o usuário desconhecido

    def verMensDesconhecido(self,usuario):
        usuarioDAO = UsuarioDAO()

        print("Para vizualizar as mensagems que enviou ou recebel de um usuário que não é seu amigo você precissa informar o E-mail dele\n")

        email = input("E-mail do usuário: ")

        exist = usuarioDAO.usuarioExist(email)

        if exist:
            id_desc = usuarioDAO.getIdUsuario(email)
            exist = self.existMensEmail(usuario,id_desc) # Verificando se existem mensagens entre este usuário desconhecido
            if exist:
                self.vizualizarMensagemDesconhecido(usuario,id_desc,email)
            else:
                print("\nNão existem mensagem entre você e este usuário\n")
        else:
            print("\nNão existe nenhum usuário com este E-mail na rede Nicks\n")

    def caixaDeMensagem(self,usuario):

        self.carregarMensagems(usuario) # Atualizando mensagems do usuário

        while (True):
            try:
                op = int(input("\n1) Ver mensagems de Amigo\n"
                               "2) Ver mensagems de Desconhecidos \n"
                               "0) Voltar\n"
                               "---------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    self.verMensAmigo(usuario)
                elif op == 2:
                    self.verMensDesconhecido(usuario)
                elif op == 0:
                    break # Voltando para o menu de Mensagems
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)

