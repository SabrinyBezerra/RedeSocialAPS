import sqlite3

db = sqlite3.connect("nicks.db")

cursor = db.cursor()

try:
    cursor.execute("""
      CREATE TABLE TB_usuario(
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         email  varchar(70) NOT NULL UNIQUE,
         senha  varchar(25) NOT NULL,
         nome  varchar(70) NOT NULL,
         data_nascimento DATE NOT NULL,
         genero  varchar(15) NOT NULL,
         perfil_publico  bool NOT NULL DEFAULT TRUE,
         estado_civil  varchar(25)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_solicitacao_amizade (
         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_user_envia INTEGER NOT NULL,
         id_user_recebe INTEGER NOT NULL,
         aceita varchar(5) NOT NULL,
         data_envio DATETIME NOT NULL,
         FOREIGN KEY (id_user_envia) REFERENCES usuario(id),
         FOREIGN KEY (id_user_recebe) REFERENCES usuario(id)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_mensagem (
         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_user_envia INTEGER NOT NULL,
         id_user_recebe INTEGER NOT NULL,
         mensagem TEXT(350) NOT NULL,
         data_envio DATETIME NOT NULL,
         amigo bool NOT NULL DEFAULT TRUE,
         visualizada bool NOT NULL DEFAULT FALSE,
         FOREIGN KEY (id_user_envia) REFERENCES usuario(id),
         FOREIGN KEY (id_user_recebe) REFERENCES usuario(id)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_grupo (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_user_admin  INTEGER NOT NULL,
         nome  varchar(25) NOT NULL,
         foto  blob,
         FOREIGN KEY (id_user_admin) REFERENCES usuario(id)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_publicacao (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_user  INTEGER NOT NULL,
         data  DATETIME NOT NULL,
         visibilidade_publica  bool NOT NULL DEFAULT TRUE,
         texto  TEXT(350),
         imagem  blob,
         num_like  INTEGER DEFAULT 0,
         FOREIGN KEY (id_user) REFERENCES usuario(id)
         );
    """)

    cursor.execute("""
      CREATE TABLE TB_notificacao (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_user_recebe  INTEGER NOT NULL,
         texto  TEXT(50) NOT NULL,
         data_envio  DATETIME NOT NULL,
         visualizada  bool NOT NULL DEFAULT FALSE,
         FOREIGN KEY (id_user_recebe) REFERENCES usuario(id)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_amigo (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_user  INTEGER NOT NULL,
         id_amigo  INTEGER NOT NULL,
         FOREIGN KEY (id_user) REFERENCES usuario(id),
         FOREIGN KEY (id_amigo) REFERENCES usuario(id)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_participante_grupo (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_grupo  INTEGER NOT NULL,
         id_participante  INTEGER NOT NULL,
         FOREIGN KEY (id_grupo) REFERENCES grupo(id),
         FOREIGN KEY (id_participante) REFERENCES usuario(id)
        );
    """)
    cursor.execute("""
      CREATE TABLE TB_mensagem_participante_grupo (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_grupo  INTEGER NOT NULL,
         id_participante  INTEGER NOT NULL,
         mensagem  TEXT(350) NOT NULL,
         data_envio  DATETIME NOT NULL,
         visualizada  bool NOT NULL DEFAULT  FALSE,
         FOREIGN KEY (id_grupo) REFERENCES grupo(id),
         FOREIGN KEY (id_participante) REFERENCES participante_grupo(id_participante)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_usuario_interacao_publicacao (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_publicacao  INTEGER NOT NULL,
         id_user  INTEGER NOT NULL,
         comentario  TEXT(350),
         like  INTEGER DEFAULT 0,
         FOREIGN KEY (id_publicacao) REFERENCES publicacao(id),
         FOREIGN KEY (id_user) REFERENCES usuario(id)
        );
    """)

    cursor.execute("""
      CREATE TABLE TB_solicitacao_grupo (
         id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         id_grupo  INTEGER NOT NULL,
         id_user_grupo_admin  INTEGER NOT NULL,
         id_user_recebe  INTEGER NOT NULL,
         aceita  varchar(5) NOT NULL,
         FOREIGN KEY (id_grupo) REFERENCES grupo(id),
         FOREIGN KEY (id_user_grupo_admin) REFERENCES grupo(id_user_admin),
         FOREIGN KEY (id_user_recebe) REFERENCES usuario(id)
        );
    """)

    db.close() # Fechando conexão

except sqlite3.OperationalError:
    pass
