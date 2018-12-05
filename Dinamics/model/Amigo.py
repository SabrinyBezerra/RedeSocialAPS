from config.ConstErros import * # Importando constantes de erro da aplicação
from model.Usuario import Usuario
from database.UsuarioDAO import UsuarioDAO
from database.AmigoDAO import AmigoDAO

class Amigo():
    def __init__(self,id=None,id_user=None,id_amigo=None):
        self.id = id
        self.id_user = id_user
        self.id_amigo = id_amigo


    def enviarSolicitacaoAmizade(self,usuario):
        idAmigo = self.busqueUsuario()

        if idAmigo == usuario.id:  # Verificando se o usuário não esta querendo mandar uma solicitação para ele mesmo
            print("\nVocê já é amigo de você mesmo\n")
        elif idAmigo == None:
            return None # Encerrando função e retornando para o menu de Amizades
        else:
            self.enviaSolicitacaoAmizade(idAmigo,usuario)

    def busqueUsuario(self):

        usuarioDAO = UsuarioDAO()
        nomeBusca = input("\nBusque o usuário pelo nome: ")
        print(" ")
        usuarios = usuarioDAO.getListUsuario(nomeBusca)

        print("--------------------------------------")
        print("Resultados da busca por %s"%(nomeBusca))
        print("--------------------------------------\n")
        num = 1 # Variável usada para enumeras os usuários

        initLoop = True # Variável que vai controlar o loop de escolha do usuário

        if usuarios == []:
            print("Nenhum usuário encontrado\n")
            initLoop = False
        else:
            for usuario in usuarios:
                print("---------------------------------\n")
                print("Número: %s" %(num))
                print("Nome: %s" %(usuario[0]))
                print("E-mail: %s" %(usuario[1]))
                print("---------------------------------\n")
                num += 1  # num = num + 1 Somando um número a num a cada loop
            num = num - 1 # Retirando o acréscimo colocado no ultimo loop

        while(initLoop):
            try:
                print("--------------------------------------")
                print("OBS: Ao digitar zero(0) você cancela o envio e volta para o menu de Amigos\n")
                numAmigo = int(input("Número do usuário que quer enviar a solicitação: "))

                if numAmigo == 0:
                    print("\nEnvio de Solicitação cancelada\n")
                    return  None
                elif numAmigo != 0: # Se a opção for diferente de cancelamento
                    if numAmigo <= num and numAmigo > 0: # Se a opção não for um número da lista de usuários
                        return usuarios[numAmigo-1][2] # Retornando ID do usuário escolhido para enviar a solicitação de amizade
                    else:
                        print("\nEste usuário não foi encontrado na busca\n")
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)

        return None

    def enviaSolicitacaoAmizade(self,idAmigo,usuario):

        amigoDAO = AmigoDAO()

        # Verificando se o usuário já não é um amigo
        eAmigo = False
        for amigo in usuario.amigos:
            if amigo.id == idAmigo:
                print("\nEste usuário já é seu amigo\n")
                eAmigo = True


        # Verificarndo se o usuário que quer enviar já não enviol alguma solicitação
        if not eAmigo: # Se o usuário não for amigo
           exist = amigoDAO.existSolicitacao(usuario.id,idAmigo) # Recebendo o resultado da função que vai verificar se já não foi enviado alguma solicitação
           if exist:
               print("\nVocê já enviol uma solicitação de amizade para este usuário\n")
           else:
               amigoDAO.enviarSolicitacao(usuario.id,idAmigo) # Enviando a solicitação de amizade
               print("\nSua solicitação foi enviada\n")

    def solicitacoesRecebidas(self,usuario):
        amigoDAO = AmigoDAO()

        result = amigoDAO.getSolicitacoesRecebidas(usuario.id)

        if result == []:
            print("\nVocê não tem solicitações de amizades\n")
        else:

            # Criando um loop para perguntar ao usuário se ele aceita, nega ou responde depois as solicitações de amizades
            for solicitacao in result:
                print("--------------------------------------")
                print("Nome: %s" %(solicitacao[0]))
                print("E-mail: %s" %(solicitacao[1]))
                print("--------------------------------------")
                idUser = solicitacao[2] # ID do usuário que enviol a solicitação

                while (True):
                    try:
                        op = int(input("1) Aceitar\n"
                                       "2) Recusar\n"
                                       "3) Responder Depois\n"
                                       "---------------------------------\n"
                                       ">>: "))
                        print(" ")
                        if op == 1:
                            amigoDAO.deletarSolicitacao(usuario,idUser)
                            amigoDAO.adicionarAmigo(usuario,idUser)
                            self.carregarAmigos(usuario)
                            print("\n%s agora é seu amigo\n" %(solicitacao[0]))
                            self.carregarAmigos(usuario)
                            print("\n %s foi adicionado a sua lista de amigos\n" %(solicitacao[0]))
                            break
                        elif op == 2:
                            amigoDAO.deletarSolicitacao(usuario.id,idUser)
                            print("\nSolicitação de amizade recusada\n")
                            break
                        elif op == 3:
                            break
                        else:
                            print(numeroForaDeContesto)
                    except ValueError:
                        print(numeroInvalido)

    def carregarAmigos(self,usuario):
        usuarioDAO = UsuarioDAO()
        usuario.amigos = []
        amigos = usuarioDAO.getListAmigos(usuario.id)

        for amigo in amigos:
            usuarioAmigo = Usuario()
            usuarioAmigo.id = amigo[0]
            usuarioAmigo.email = amigo[1]
            usuarioAmigo.senha = amigo[2]
            usuarioAmigo.nome = amigo[3]
            usuarioAmigo.data_nascimento = amigo[4]
            usuarioAmigo.genero = amigo[5]
            usuarioAmigo.estado_civil = amigo[6]
            usuarioAmigo.profissao = amigo[7]
            usuario.amigos.append(usuarioAmigo) # Adicionando o usuário a lista de amigos do usuário


    def solicitacoesEnviadas(self,usuario):
        amigoDAO = AmigoDAO()

        result = amigoDAO.getSolicitacoesEnviadas(usuario.id)
        print("\nSolicitações Enviadas\n")

        if result == []:
            print("\nVocê não tem solicitações de amizades enviadas\n")
        else:
            for solicitacao in result:
                print("\n---------------------------------")
                print("Para: %s" %(solicitacao[0]))
                print("Data: %s" %(solicitacao[1]))
                print("---------------------------------\n")


    def solicitacoesAmizade(self,usuario):

        amigoDAO = AmigoDAO()

        while (True):

            numSoliEnviadas = amigoDAO.getTotalSolicitacoesEnviadas(usuario.id)# Total de solicitações enviadas
            numSoliRecebidas = amigoDAO.getTotalSolicitacoesRecebidas(usuario.id) # Total de solicitações recebidas

            print("---------------------------------\n"
                  "Solicitações de Amizades\n")
            print("1) Recebidas : %i\n"
                  "2) Enviadas : %i\n"
                  "0) Voltar ao menu de Amigos\n"
                  "---------------------------------\n" %(numSoliRecebidas,numSoliEnviadas))
            try:
                op = int(input(">>:"))
                if op == 1:
                    self.solicitacoesRecebidas(usuario)
                elif op == 2:
                    self.solicitacoesEnviadas(usuario)
                elif op == 0:
                    break # Encerrando loop e voltando para o Menu de amigos
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)

    def verAmigos(self,usuario):
        if usuario.totalAmigos()== 0:
            print("\nVocê não possue amigos no momento\n")
        else:
            print("\nLista de amigos\n")
            for amigo in usuario.amigos:
                print("---------------------------------")
                print("ID: %s" %(amigo.id))
                print("Nome: %s" %(amigo.nome))
                print("E-mail: %s" %(amigo.email))
                print("Profissão: %s" %(amigo.profissao))
                print("Data De Nascimento: %s" %(amigo.data_nascimento))
                print("---------------------------------\n")


    def verAmigosNome(self,usuario):
        print("\nLista de amigos\n")
        num = 0 # Variável utilizada para enumerar os amigos
        for amigo in usuario.amigos:
            num += 1
            print("%i) %s" %(num,amigo.nome))

    def desfazerAmizade(self,usuario):

        if usuario.totalAmigos() == 0:
            print("\nVocê não possue amigos no momento\n")

        else:
            self.verAmigos(usuario)# Imprimindo amigos do usuário
            amigoDAO = AmigoDAO()

            while(True):

                numAmigo = 0  # Variável usada para identificar o amigo na lista de amigos do usuário

                print("OBS: Ao digitar zero(0) a operação é cancelada e você retorna para o menu de Amizades\n")
                print("Digite o ID do usuário que dejesa desfazer a amizade")
                print("-----------------------------------------------------")

                ID = int(input(">>:"))
                if ID == 0:
                    break # Parando loop e retornando para o menu de Amizades
                else:
                    for amigo in usuario.amigos:
                        if ID == amigo.id:
                            amigoDAO.deletarAmizade(usuario,ID)
                            del usuario.amigos[numAmigo]
                            print("\nVocê acaba de desfazer a amizade com %s\n" %(amigo.nome))
                            return None # Parando loop e retornando para o menu de Amizades
                        numAmigo += 1
                    print("\nVocê não possue um amigo com este ID\n")


