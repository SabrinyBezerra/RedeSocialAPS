from database.MensagemGrupoDAO import MensagemGrupoDAO
from database.UsuarioDAO import UsuarioDAO

class MensagemGrupo():
    def __init__(self,id=None,id_grupo=None,id_participante=None,mensagem=None,data_envio=None):
        self.id = id
        self.id_grupo = id_grupo
        self.id_participante = id_participante
        self.mensagem = mensagem
        self.data_envio = data_envio

    def exibirMensagems(self,grupo):
        usuarioDAO = UsuarioDAO()
        grupo.carregarMensagems(grupo) # Atualizando mensagems do grupo

        if grupo.totalMensagems() == 0:
            print("\nEste grupo não possuem mensagems no momento\n")
        else:
            print("\n\n\n")
            print("==================================================================")
            print("\n--------------------------------------------------------")
            print("                    %s                                    " % (grupo.nome))
            print("----------------------------------------------------------")
            print("==================================================================\n")
            for mensagemGrupo in grupo.mensagems:
                nomeEnviou = usuarioDAO.getNomeUsuario(mensagemGrupo.id_participante)
                print("%s : %s\n"
                      " --------------------------------------------------\n"
                      " * %s                                              \n"
                      "                                                   \n"
                      "                                                   \n"
                      " ---------------------------------------------------\n" % (nomeEnviou,mensagemGrupo.data_envio,mensagemGrupo.mensagem))
            print("========================================================")


