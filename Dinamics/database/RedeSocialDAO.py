from database.BD import * # Importando os atributos referentes ao banco de dados

class RedeSocialDAO():
    def __init__(self):
        self.conn = BDconn
        self.cursor = BDcursor

    def criarBD(self):
        """
            Criando tabelas da Rede Social
        """
        try:
            # CRIANDO TABELA DO USUÁRIO
            self.cursor.execute("""
                CREATE TABLE tb_usuario(
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   email  varchar(50) NOT NULL UNIQUE,
                   senha  varchar(25) NOT NULL,
                   nome  varchar(50) NOT NULL,
                   data_nascimento DATE NOT NULL,
                   genero  varchar(15) NOT NULL,
                   estado_civil  varchar(15),
                   profissao  varchar(25)
                  );
              """)

            # CRIANDO TABELA DAS SOLICITAÇÕES DE AMIZADE
            self.cursor.execute("""
                CREATE TABLE TB_solicitacao_amizade (
                   id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_user_envia INTEGER NOT NULL,
                   id_user_recebe INTEGER NOT NULL,
                   data_envio DATETIME NOT NULL,
                   FOREIGN KEY (id_user_envia) REFERENCES tb_usuario(id),
                   FOREIGN KEY (id_user_recebe) REFERENCES tb_usuario(id)
                  );
              """)

            # CRIANDO TABELA DAS MENSAGEMS
            self.cursor.execute("""
                CREATE TABLE TB_mensagem (
                   id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_user_envia INTEGER NOT NULL,
                   id_user_recebe INTEGER NOT NULL,
                   mensagem TEXT(350) NOT NULL,
                   data_envio DATETIME NOT NULL,
                   FOREIGN KEY (id_user_envia) REFERENCES tb_usuario(id),
                   FOREIGN KEY (id_user_recebe) REFERENCES tb_usuario(id)
                  );
              """)

            # CRIANDO TABELA DOS GRUPOS
            self.cursor.execute("""
                CREATE TABLE TB_grupo (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_user_admin  INTEGER NOT NULL,
                   nome  varchar(25) NOT NULL,
                   FOREIGN KEY (id_user_admin) REFERENCES tb_usuario(id)
                  );
              """)

            # CRIANDO TABELAS DAS PUBLICAÇÕES
            self.cursor.execute("""
                CREATE TABLE TB_publicacao (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_user  INTEGER NOT NULL,
                   data  DATETIME NOT NULL,
                   visibilidade_publica  bool NOT NULL DEFAULT TRUE,
                   texto  TEXT(350),
                   imagem  blob,
                   num_like  INTEGER DEFAULT 0,
                   FOREIGN KEY (id_user) REFERENCES tb_usuario(id)
                   );
              """)

            # CRIANDO TABELA DAS NOTIFICAÇÕES
            self.cursor.execute("""
                CREATE TABLE TB_notificacao (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_user_recebe  INTEGER NOT NULL,
                   texto  TEXT(50) NOT NULL,
                   data_envio  DATETIME NOT NULL,
                   FOREIGN KEY (id_user_recebe) REFERENCES tb_usuario(id)
                  );
              """)

            # CRIANDO TABELA DOS AMIGOS
            self.cursor.execute("""
                CREATE TABLE TB_amigo (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_user  INTEGER NOT NULL,
                   id_amigo  INTEGER NOT NULL,
                   FOREIGN KEY (id_user) REFERENCES tb_usuario(id),
                   FOREIGN KEY (id_amigo) REFERENCES tb_usuario(id)
                  );
              """)

            # CRIANDO TABELA DE PARTICIPANTE DOS GRUPOS
            self.cursor.execute("""
                CREATE TABLE TB_participante_grupo (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_grupo  INTEGER NOT NULL,
                   id_participante  INTEGER NOT NULL,
                   FOREIGN KEY (id_grupo) REFERENCES grupo(id),
                   FOREIGN KEY (id_participante) REFERENCES tb_usuario(id)
                  );
              """)

            # CRIANDO TABELA DE MENSAGEMS DOS PARTICIPANTE DOS GRUPOS
            self.cursor.execute("""
                CREATE TABLE TB_mensagem_participante_grupo (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_grupo  INTEGER NOT NULL,
                   id_participante  INTEGER NOT NULL,
                   mensagem  TEXT(350) NOT NULL,
                   data_envio  DATETIME NOT NULL,
                   FOREIGN KEY (id_grupo) REFERENCES grupo(id),
                   FOREIGN KEY (id_participante) REFERENCES tb_participante_grupo(id_participante)
                  );
              """)

            # CRIANDO TABELA DE INTEGERERAÇÃO COM AS PUBLICAÇÕES
            self.cursor.execute("""
                CREATE TABLE TB_usuario_interacao_publicacao (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_publicacao  INTEGER NOT NULL,
                   id_user  INTEGER NOT NULL,
                   comentario TEXT(350),
                   qtd_like  INTEGER DEFAULT 0,
                   FOREIGN KEY (id_publicacao) REFERENCES tb_publicacao(id),
                   FOREIGN KEY (id_user) REFERENCES tb_usuario(id)
                  );
              """)

            # CRIANDO TABELA DE SOLICITAÇÕES DE PARTICIPAÇÃO DE GRUPOS
            self.cursor.execute("""
                CREATE TABLE TB_solicitacao_grupo (
                   id  INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                   id_grupo  INTEGER NOT NULL,
                   id_user_grupo_admin  INTEGER NOT NULL,
                   id_user_recebe  INTEGER NOT NULL,
                   FOREIGN KEY (id_grupo) REFERENCES grupo(id),
                   FOREIGN KEY (id_user_grupo_admin) REFERENCES tb_grupo(id_user_admin),
                   FOREIGN KEY (id_user_recebe) REFERENCES tb_usuario(id)
                  );
              """)


        except: # As tabelas já foram criadas
            pass



