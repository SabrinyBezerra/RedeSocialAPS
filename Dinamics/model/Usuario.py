from database.UsuarioDAO import UsuarioDAO
from database.AmigoDAO import AmigoDAO
from config.ConstErros import *
import datetime

class Usuario():
    def __init__(self,email=None,senha=None,nome=None,data_nascimento=None,genero=None,estado_civil=None,profissao=None,id=None):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.estado_civil = estado_civil
        self.profissao = profissao

        # Atributos que não estão presentes na tabela no banco de dados
        self.amigos = []
        self.mensagems = []
        self.grupos = []

    def autenticado(self):
        usuarioDAO = UsuarioDAO()
        return usuarioDAO.autenticarUsuario(self)

    def verDados(self):
        print("")
        # Imprimindo ID do usuário
        print("ID: %i" % self.id)

        # Imprimindo E-mail do usuário
        print("E-mail: %s" % self.email)

        # Imprimindo senha do usuário
        if len(self.senha)==0:
            print("Sua Senha: Não informado ")
        else:
            print("Sua Senha: %s" % self.senha)

        # Imprimindo nome do usuário
        if len(self.nome)==0:
            print("Seu Nome: Não informado ")
        else:
            print("Seu Nome: %s" % self.nome)

        # Imprimindo Data De Nascimento do usuário
        print("Sua Data De Nascimento: %s" % self.data_nascimento)

        # Imprimindo Genêro do usuário
        if len(self.genero)==0:
            print("Seu Genêro: Não informado ")
        else:
            print("Seu Genêro: %s" % self.genero)

        # Imprimindo o Estado Civil do usuário
        if len(self.estado_civil)==0:
            print("Seu Estado Civil: Não informado ")
        else:
            print("Seu Estado Civil: %s" % self.estado_civil)

        # Imprimindo a Profição do usuário
        if len(self.profissao)==0:
            print("Sua Profição: Não informado ")
        else:
            print("Sua Profição: %s" % self.profissao)

        print("")


    def removerUsuario(self):

        usuarioDAO = UsuarioDAO()
        usuarioDAO.deletarUsuario(self)  # Deletando usuário da rede social
        # Faltando configurar para deletar em conjunto todos os grupos que o usuário participa
        # e deltar o usuário da lista de amigos de outros usuários
        print("\nConta removida com sucesso\n")


    def atualizarUsuario(self):

        usuarioDAO = UsuarioDAO()

        # Perguntando ao usuário se ele deseja alterar o seu E-mail
        while (True):
            try:
                op = int(input("\n---------------------------------\n"
                               "Deseja modificar seu E-mail: \n"
                               "1) Sim\n"
                               "2) Não\n"
                               "---------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    email = input("Digite seu novo email: ")
                    if usuarioDAO.usuarioExist(email):
                        print("\nEste E-mail já é utilizado por outro usuário, tente novamente\n")
                        continue # Retornando para o loop
                    else:
                        self.email = email
                        print("")
                        break
                elif op == 2:
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)
        #-------------------------------------------------------------

        # Perguntando ao usuário se ele deseja alterar a sua senha
        while (True):
            try:
                op = int(input("\n---------------------------------\n"
                               "Deseja modificar sua Senha: \n"
                               "1) Sim\n"
                               "2) Não\n"
                               "---------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    self.senha = input("Digite sua nova Senha: ")
                    print("")
                    break
                elif op == 2:
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)
        # -------------------------------------------------------------

        # Perguntando ao usuário se ele deseja alterar o seu Nome
        while (True):
            try:
                op = int(input("\n---------------------------------\n"
                               "Deseja mudar seu Nome: \n"
                               "1) Sim\n"
                               "2) Não\n"
                               "---------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    self.nome = input("Digite seu novo Nome: ")
                    print("")
                    break
                elif op == 2:
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)
        # -------------------------------------------------------------

        # Perguntando ao usuário se ele deseja alterar a sua Data De Nascimento
        continuar = True  # Como a dois loops é preciso uma variável para controlar um deles
        while (continuar):
            try:
                op = int(input("\n-------------------------------------------\n"
                               "Deseja modificar sua Data De Nascimento: \n"
                               "1) Sim\n"
                               "2) Não\n"
                               "-------------------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    while (True):
                        try:
                            print("Data De Nascimento: ")
                            dia = int(input("  Dia: "))
                            mes = int(input("  Mês: "))
                            ano = int(input("  Ano: "))
                            self.data_nascimento = datetime.date(ano, mes, dia)
                            continuar = False
                            break
                        except (ValueError, OverflowError):
                            print(dataNascimentoInvalida)
                elif op == 2:
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)
        # -------------------------------------------------------------

        # Perguntando ao usuário se ele deseja alterar o seu Gênero
        while (True):
            try:
                op = int(input("\n---------------------------------\n"
                               "Deseja modificar seu Gênero: \n"
                               "1) Sim\n"
                               "2) Não\n"
                               "---------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    self.genero = input("Digite seu novo Gênero: ")
                    print("")
                    break
                elif op == 2:
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)
        # -------------------------------------------------------------

        # Perguntando ao usuário se ele deseja alterar o seu Estado Civil
        while (True):
            try:
                op = int(input("\n-------------------------------------\n"
                               "Deseja modificar seu Estado Civil: \n"
                               "1) Sim\n"
                               "2) Não\n"
                               "-------------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    self.senha = input("Digite seu novo Estado Civil: ")
                    print("")
                    break
                elif op == 2:
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)
        # -------------------------------------------------------------

        # Perguntando ao usuário se ele deseja alterar a sua Profissão
        while (True):
            try:
                op = int(input("\n---------------------------------\n"
                               "Deseja modificar sua Profissão: \n"
                               "1) Sim\n"
                               "2) Não\n"
                               "---------------------------------\n"
                               ">>: "))
                print(" ")
                if op == 1:
                    self.senha = input("Digite sua nova Profissão: ")
                    print("")
                    break
                elif op == 2:
                    break
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)
        # -------------------------------------------------------------

        usuarioDAO.atualizarUsuario(self)  # Atualizando o cadastro no banco de dados passando o usuário como parâmetro
        print("\nCadastro atualizado com sucesso\n")  # Mensagem de sucesso referente a mudança de cadastro

    def criarUsuario(self):
            email = None  # Como o E-mail é obrigatório no banco de dados ele sera um atributo obrigatório para a criação do usuário também
            usuarioDAO = UsuarioDAO()

            print("")
            self.nome = input("Nome: ")
            while (True):  # Criando um loop para verificar se o usuário informol o E-mail
                self.email = input("E-mail: ")
                if len(self.email) == 0:  # Se o E-mail estiver vazio ou seja o usuário não o informol
                    print("\nInforme um E-mail por favor\n")
                else:  # O email foi preenchido
                    if usuarioDAO.usuarioExist(self.email):
                        print("\nEste email já é utilizado por outro usuário, tente novamente\n")
                    else:
                        break  # Parando loop e continuando o preenchimento dos dados do usuário
            self.senha = input("Senha: ")
            while (True):
                try:
                    print("Data De Nascimento: ")
                    dia = int(input("  Dia: "))
                    mes = int(input("  Mês: "))
                    ano = int(input("  Ano: "))
                    self.data_nascimento = datetime.date(ano, mes, dia)
                    break
                except (ValueError, OverflowError):
                    print(dataNascimentoInvalida)
            self.genero = input("Genêro: ")
            self.estado_civil = input("Estado Civil: ")
            self.profissao = input("Profissao: ")

            result = usuarioDAO.inserirUsuario(self)
            self.id = usuarioDAO.getIdUsuario(self.email) # Atribuindo o ID do usuário


            return result # Retornando status da inclusão do usuário

    def carregarUsuarioBD(self):

        usuarioDAO = UsuarioDAO()
        usuario = usuarioDAO.getUsuario(self.email)

        self.id = usuario[0]
        self.senha = usuario[2]
        self.nome = usuario[3]
        self.data_nascimento = usuario[4]
        self.genero = usuario[5]
        self.estado_civil = usuario[6]
        self.profissao = usuario[7]

    def totalSolicitacoes(self):
        amigoDAO = AmigoDAO()
        numSoliEnviadas = amigoDAO.getTotalSolicitacoesEnviadas(self.id)  # Total de solicitações enviadas
        numSoliRecebidas = amigoDAO.getTotalSolicitacoesRecebidas(self.id)  # Total de solicitações recebidas
        return numSoliEnviadas + numSoliRecebidas

    def totalAmigos(self):
        return len(self.amigos)

    def totalGrupos(self):
        return len(self.grupos)

    def totalGruposAdmin(self):
        numGrupos = 0
        for grupo in self.grupos:
            if grupo.id_user_admin == self.id:
                numGrupos += 1
        return numGrupos