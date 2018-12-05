from database.GrupoDAO import GrupoDAO
from config.ConstErros import *
from model.Amigo import Amigo
from database.UsuarioDAO import UsuarioDAO
from model.Usuario import Usuario
from model.MensagemGrupo import MensagemGrupo
import datetime
from database.MensagemGrupoDAO import MensagemGrupoDAO

class Grupo():
    def __init__(self,id=None,id_user_admin=None,nome=None):
        self.id = id
        self.id_user_admin = id_user_admin
        self.nome = nome

        # Atributos que não estão na tabela do banco de dados
        self.participantes = []
        self.mensagems = []

    def criarGrupo(self,usuario):
        grupoDAO = GrupoDAO()

        self.id_user_admin = usuario.id # Atribuindo como adiministrador o usuário que solicitou a criação de um grupo
        self.nome = input("Qual o nome do grupo: ")

        if grupoDAO.existGrupo(usuario,self): # Se já existir o grupo
            print("\nEste grupo já foi criado por você\n")
        else:
            grupoDAO.inserirGrupo(self)
            self.id = grupoDAO.getIDgrupo(self)
            grupoDAO.inserirParticipante(self, usuario.id) # Adicionando o usuário que é um administrador como um participante do grupo
            print("\nGrupo < %s > criado com sucesso\n" %(self.nome))


    def listarGrupos(self,usuario):
        self.carregarGrupos(usuario) # Atualizando grupos do usuário

        participaDeGrupo = False # Se o usuário participa de algum grupo
        adminDeGrupo = False # Se o usuário é administrador de algum grupo

        print("\n-----------------------------------------------")
        print("Grupos que você é administrador: ")
        print("-------------------------------------------------")
        for grupo in usuario.grupos:
            if grupo.id_user_admin == usuario.id:
                adminDeGrupo = True
                print("ID: %s" %(grupo.id))
                print("Nome: %s" %(grupo.nome))
                print("Número de participantes: %i\n" %(grupo.totalParticipantes()))

        if not adminDeGrupo:
            print("\nVocê não é administrador de nenhum grupo no momento\n")

        print("\n-----------------------------------------------")
        print("Grupos que você participa: ")
        print("-------------------------------------------------")
        for grupo in usuario.grupos:
            if not grupo.id_user_admin == usuario.id:
                participaDeGrupo = True
                print("ID: %i" %(grupo.id))
                print("Nome: %s" %(grupo.nome))
                print("Número de membros: %i\n" %(grupo.totalParticipantes()))

        if not participaDeGrupo:
            print("\nVocê não é participa de nenhum grupo no momento\n")


    def listarGruposAdmin(self,usuario):
        adminDeGrupo = False  # Se o usuário é admininistrador de algum grupo

        print("\n-----------------------------------------------")
        print("Grupos que você é administrador: ")
        print("-------------------------------------------------")
        for grupo in usuario.grupos:
            if grupo.id_user_admin == usuario.id:
                adminDeGrupo = True
                print("ID: %s" %(grupo.id))
                print("Nome: %s" %(grupo.nome))
                print("Número de membros: %i\n" %(grupo.totalParticipantes()))

        if not adminDeGrupo:
            print("\nVocê não é administrador de nenhum grupo no momento\n")

    def excluirGrupo(self,usuario):
        if usuario.totalGruposAdmin()==0:
            print("\nVocê não é adiministrador de nenhum grupo no momento\n")
        else:
            grupoDAO = GrupoDAO()
            self.listarGruposAdmin(usuario)

            while (True):

                numGrupo = 0  # Variável usada para identificar o grupo na lista de grupos do usuário

                print("OBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Grupos\n")
                print("Digite o ID do grupo que dejesa excluir")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break  # Parando loop e retornando para o menu de Amizades
                else:
                    for grupo in usuario.grupos:
                        if ID == grupo.id:
                            if grupo.id_user_admin != usuario.id:
                                print("\nEste ID é referente ao grupo em que você não é administrador\n")
                                break  # Parando loop e retornando para o menu de Amizades
                            else:
                                grupoDAO.deletarGrupo(grupo)
                                del usuario.grupos[numGrupo]
                                print("\n Grupo <%s> Exluido \n" % (grupo.nome))
                                return None # Parando loop e retornando para o menu de Amizades
                        numGrupo += 1
                    print("\nVocê não possue um grupo com este ID\n")

    def carregarParticipantes(self,grupo):
        grupoDAO = GrupoDAO()
        participantes = grupoDAO.getListParticipantes(grupo)

        for participante in participantes:
            usuario = Usuario()
            usuario.id = participante[0]
            usuario.email = participante[1]
            usuario.senha = participante[2]
            usuario.nome = participante[3]
            usuario.data_nascimento = participante[4]
            usuario.genero = participante[5]
            usuario.estado_civil = participante[6]
            usuario.profissao = participante[7]
            grupo.participantes.append(usuario) # Adicionando participantes do grupo

    def carregarMensagems(self,grupo):
        mensagemGrupoDAO = MensagemGrupoDAO()
        grupo.mensagems = []  # Esvaziando as mensagems para que não coloque mensagems que já existem
        mensagems = mensagemGrupoDAO.getListMensagemsGrupo(grupo)

        for mensagem in mensagems:
            mensagemGrupo = MensagemGrupo()
            mensagemGrupo.id = mensagem[0]
            mensagemGrupo.id_grupo = mensagem[1]
            mensagemGrupo.id_participante = mensagem[2]
            mensagemGrupo.mensagem = mensagem[3]
            mensagemGrupo.data_envio = mensagem[4]
            grupo.mensagems.append(mensagemGrupo) # Adicionando mensagems do grupo


    def carregarGrupos(self,usuario):
        usuario.grupos = [] # Esvaziando grupos existentes para não repitirem na lista
        grupoDAO = GrupoDAO()
        grupos = grupoDAO.getListGrupos(usuario)

        for grupo in grupos:
            grupoUser = Grupo()
            grupoUser.id = grupo[0]
            grupoUser.id_user_admin = grupo[1]
            grupoUser.nome = grupo[2]
            self.carregarParticipantes(grupoUser) # Adicionando participantes do grupo
            self.carregarMensagems(grupoUser)
            usuario.grupos.append(grupoUser) # Adicionando grupo a lista de grupos do usuário

    def adicionarDesconhecido(self,usuario,grupo):
            usuarioDAO = UsuarioDAO()
            grupoDAO = GrupoDAO()

            print("\nPara incluir um usuário que não é seu amigo você precissa informar o E-mail dele\n")

            email = input("E-mail do usuário: ")

            exist = usuarioDAO.usuarioExist(email)

            if exist:
                idDesc = usuarioDAO.getIdUsuario(email)
                if grupoDAO.existParticipante(grupo,idDesc):
                    print("\nEste usuário já participa do grupo %s\n" %(grupo.nome))
                else:
                    grupoDAO.inserirParticipante(grupo,idDesc)
                    print("\nParticipante inserido com sucesso\n")
            else:
                print("\nNão existe nenhum usuário com este E-mail na rede Nicks\n")

    def adicionarAmigo(self,usuario,grupo):
        if usuario.totalAmigos()==0:
            print("\nVocê não possue amigos no momento\n")
        else:
            amigo = Amigo()
            grupoDAO = GrupoDAO()
            amigo.verAmigos(usuario)# Monstrando amigos do usuário

            while(True):

                numAmigo = 0  # Variavel usada para identificar o amigo na lista de amigos do usuário

                print("\nOBS: Ao digitar zero(0) a operação é cancelada e você retorna para a escolha do participante\n")
                print("Digite o ID do amigo que dejesa adicionar ao grupo %s" %(grupo.nome))
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break # Parando loop e retornando para o menu de Amizades
                else:
                    for amigoUser in usuario.amigos:
                        if ID == amigoUser.id:
                            if grupoDAO.existParticipante(grupo, ID):
                                print("Este usuário já participa do grupo %s" % (grupo.nome))
                                return None
                            else:
                                grupoDAO.inserirParticipante(grupo,amigoUser.id)
                                print("\nParticipante inserido com sucesso\n")
                                return None # Encerrando função e retornando para a caixa de mensagems
                        numAmigo += 1
                    print("\nVocê não possue um amigo com este ID\n")


    def adicionarParticipante(self,usuario):

        if usuario.totalGruposAdmin()== 0:
            print("\nVocê não é adiministrador de nenhum grupo no momento\n")
        else:

            self.listarGruposAdmin(usuario)
            while (True):

                numGrupo = 0  # Variavel usada para identificar o grupo na lista de grupos do usuário

                print("\nOBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Grupos\n")
                print("Digite o ID do grupo que dejesa adicionar participantes")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break  # Parando loop e retornando para o menu de Amizades
                else:
                    for grupo in usuario.grupos:
                        if ID == grupo.id:
                            if grupo.id_user_admin != usuario.id:
                                print("\nEste ID é referente ao grupo em que você não é administrador\n")
                                break  # Parando loop e retornando para o menu de Amizades
                            else:
                                self.subMenuAdicionarParticipant(usuario,numGrupo)
                                return None  # Parando loop e retornando para o menu de Amizades
                        numGrupo += 1
                    print("\nVocê não possue um grupo com este ID\n")



    def subMenuAdicionarParticipant(self,usuario,numGrupo):

        grupo = usuario.grupos[numGrupo]

        while (True):
            print("\n--------------------------------------------")
            print("Grupo: %s     Total de Participantes: %i" %(grupo.nome,grupo.totalParticipantes()))
            print("--------------------------------------------")
            print("Você vai adicionar um amigo ou um desconhecido\n"
                  "1) Amigo\n"
                  "2) Desconhecido\n"
                  "0) Voltar\n"
                  "--------------------------------------------")
            try:
                op = int(input(">>:"))  # Armazenando a escolha do usuário
                if op == 1:
                    self.adicionarAmigo(usuario,grupo)
                    break
                elif op == 2:
                    self.adicionarDesconhecido(usuario,grupo)
                    break
                elif op == 0:
                    break # Encerrando loop e retornando ao menu de Grupos
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)

    def listarParticipantesGrupos(self,grupo):
        print("\n--------------------------------------------")
        print("%s  -           Participantes: %i " %(grupo.nome,grupo.totalParticipantes()))
        print("--------------------------------------------")
        for participante in grupo.participantes:
            if grupo.id_user_admin != participante.id:
                print("ID: %i" %(participante.id))
                print("Nome: %s\n" %(participante.nome))


    def listarGruposParticipantes(self,usuario):
        self.carregarGrupos(usuario) # Atualizando grupos do usuário

        participaDeGrupo = False # Se o usuário participa de algum grupo
        adminDeGrupo = False # Se o usuário é admin de algum grupo

        print("\n-----------------------------------------------")
        print("Grupos que você é administrador: ")
        print("-------------------------------------------------")
        for grupo in usuario.grupos:
            if grupo.id_user_admin == usuario.id:
                adminDeGrupo = True
                print("ID: %s" %(grupo.id))
                print("Nome: %s" %(grupo.nome))
                print("Número de participantes: %i" %(grupo.totalParticipantes()))
                print("Participantes: ")
                for participante in grupo.participantes:
                    if grupo.totalParticipantes() == 0:
                        print("   * Nenhum Participante")
                    elif grupo.id_user_admin != participante.id:
                        print("   * %s" % (participante.nome))
                print(" ")

        if not adminDeGrupo:
            print("\nVocê não é administrador de nenhum grupo no momento\n")

        print("\n-----------------------------------------------")
        print("Grupos que você participa: ")
        print("-------------------------------------------------")
        for grupo in usuario.grupos:
            if not grupo.id_user_admin == usuario.id:
                participaDeGrupo = True
                print("ID: %i" %(grupo.id))
                print("Nome: %s" %(grupo.nome))
                print("Número de participantes: %i" %(grupo.totalParticipantes()))
                print("Participantes: ")
                for participante in grupo.participantes:
                    if grupo.totalParticipantes() == 0:
                        print("   * Nenhum Participante")
                    elif grupo.id_user_admin != participante.id:
                        print("   * %s" % (participante.nome))
                print(" ")

        if not participaDeGrupo:
            print("\nVocê não é participa de nenhum grupo no momento\n")


    def subMenuRetirarParticipant(self,usuario, numGrupo):
        grupo = usuario.grupos[numGrupo]
        if grupo.totalParticipantes() == 0:
            print("\nEste grupo não possuem participantes para retirar\n")
        else:

            grupoDAO = GrupoDAO()
            self.listarParticipantesGrupos(grupo)

            while (True):

                print("\nOBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Grupos\n")
                print("Digite o ID do participante que dejesa retirar")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break  # Parando loop e retornando para o menu de Grupos
                elif ID == usuario.id:
                    print("\nO adiministrador do grupo não pode ser removido\n")
                else:
                    for participante in grupo.participantes:
                        if ID == participante.id:
                            grupoDAO.deletarParticipanteGrupo(grupo,ID)
                            print("\nParticipante retirado\n")
                            return None
                    print("\nVocê não possue um participante com este ID\n")

    def exluirParticipante(self,usuario):
        if usuario.totalGruposAdmin() == 0:
            print("\nVocê não é adiministrador de nenhum grupo no momento\n")
        else:

            self.listarGruposAdmin(usuario)
            while (True):

                numGrupo = 0  # Variável usada para identificar o grupo na lista de grupos do usuário

                print("\nOBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Grupos\n")
                print("Digite o ID do grupo que dejesa retirar participantes")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break  # Parando loop e retornando para o menu de Grupos
                else:
                    for grupo in usuario.grupos:
                        if ID == grupo.id:
                            if grupo.id_user_admin != usuario.id:
                                print("\nEste ID é referente ao grupo em que você não é administrador\n")
                                break  # Parando loop e retornando para o menu de Grupos
                            else:
                                self.subMenuRetirarParticipant(usuario, numGrupo)
                                return None  # Parando loop e retornando para o menu de Grupos
                        numGrupo += 1
                    print("\nVocê não possue um grupo com este ID\n")

    def sairDeGrupo(self,usuario):

        if usuario.totalGrupos()== 0:
            print("\nVocê não participa de nenhum grupo no momento\n")
        else:

            grupoDAO = GrupoDAO()

            self.listarGrupos(usuario)
            while (True):

                numGrupo = 0  # Variável usada para identificar o grupo na lista de grupos do usuário

                print("\nOBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Grupos\n")
                print("OBS: Caso digite um ID de um grupo em que você é administrador este grupo sera excluido \n")
                print("Digite o ID do grupo que dejesa se retirar")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break  # Parando loop e retornando para o menu de Amizades
                else:
                    for grupo in usuario.grupos:
                        if ID == grupo.id:
                            if grupo.id_user_admin == usuario.id:
                                grupoDAO.deletarGrupo(grupo)
                                return None# Parando loop e retornando para o menu de Amizades
                            else:
                                grupoDAO.deletarParticipanteGrupo(grupo,usuario.id)
                                return None  # Parando loop e retornando para o menu de Amizades
                        numGrupo += 1
                    print("\nVocê não possue um grupo com este ID\n")

    def enviarMensagem(self,usuario):
        if usuario.totalGrupos()== 0:
            print("\nVocê não participa de nenhum grupo no momento\n")
        else:

            mensagemGrupoDAO = MensagemGrupoDAO()
            mensagemGrupo = MensagemGrupo()

            self.listarGrupos(usuario)
            while (True):

                numGrupo = 0  # Variavel usada para identificar o grupo na lista de grupos do usuário

                print("\nOBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Grupos\n")
                print("Digite o ID do grupo que dejesa enviar a mensagem")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break  # Parando loop e retornando para o menu de Grupos
                else:
                    for grupo in usuario.grupos:
                        if ID == grupo.id:
                            mensagemGrupo.id_grupo = ID
                            mensagemGrupo.id_participante = usuario.id
                            mensagemGrupo.data_envio = datetime.datetime.today()
                            mensagemGrupo.mensagem = input("\nMensagem: ")
                            mensagemGrupoDAO.enviarMensagem(mensagemGrupo)
                            print("\nMensagem enviada\n")
                            return None
                        numGrupo += 1
                    print("\nVocê não possue um grupo com este ID\n")

    def verMensagems(self,usuario):
        if usuario.totalGrupos() == 0:
            print("\nVocê não participa de nenhum grupo no momento\n")
        else:

            mensagemGrupo = MensagemGrupo()

            self.listarGrupos(usuario)
            while (True):

                numGrupo = 0  # Variavel usada para identificar o grupo na lista de grupos do usuário

                print("\nOBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Grupos\n")
                print("Digite o ID do grupo que dejesa vizualizar as mensagems")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break  # Parando loop e retornando para o menu de Grupos
                else:
                    for grupo in usuario.grupos:
                        if ID == grupo.id:
                            mensagemGrupo.exibirMensagems(grupo)
                            return None
                        numGrupo += 1
                    print("\nVocê não possue um grupo com este ID\n")

    def totalParticipantes(self):
        return len(self.participantes)-1

    def totalMensagems(self):
        return len(self.mensagems)