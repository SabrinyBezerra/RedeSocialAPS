from config.ConstErros import * # Importando as mensagens de erros da aplicação
from model.RedeSocial import RedeSocial

def menuUsuario():
    pass

def menuRedeSocial():

        redeSocial = RedeSocial("Dinamics","0.3") # Definindo um objeto do tipo rede social
        redeSocial.criarBanco() # Criando o banco de dados da rede social

        while (True):

            print("========================================\n"
                  "                 %s\n"
                  "========================================\n"
                  "1) Entrar na minha conta\n"
                  "2) Criar uma conta\n"
                  "0) Sair\n"
                  "----------------------------------------"%(redeSocial.nome))
            try:
                op = int(input(">>:"))  # Armazenando a escolha do usuário
                if op == 1:
                    redeSocial.openConta() # Chamando função de abertura da conta de um usuário na rede social
                elif op == 2:
                    redeSocial.newConta() # Chamando função de criação de uma conta na rede social
                elif op == 0:
                    redeSocial.finichid() # Chamando a função de fechamento do sistema da rede social
                else:
                    print(numeroForaDeContesto)
            except ValueError:
                print(numeroInvalido)



def main(args = []):

    menuRedeSocial()

if (__name__ == "__main__"):
    main()