from flask_restful import Resource, marshal_with, abort
from flask import request
from models.Usuario import Usuario
from database.UsuarioDAO import UsuarioDAO

class CadastroResource(Resource):
    
    # POST /cadastro
    def post(self):
        usuario = request.json

        emailInvalido = UsuarioDAO().usuarioExist(usuario['email'])

        if not(emailInvalido):
            try:
                usuario['data_nascimento'] = usuario['data_nascimento'].split("T")[0]
                usuario = Usuario(usuario['email'], usuario['senha'], usuario['nome'], usuario['data_nascimento'],
                                  usuario['genero'], usuario['perfil_publico'], usuario['estado_civil'])
                usuarioDAO = UsuarioDAO()
                usuarioDAO.inserirUsuario(usuario)
                print("Usuário cadastrado com sucesso")
                return "Usuário cadastrado com sucesso!", 200
            except:
                print("Erro no cadastro")
                return "Erro no cadastro.", 500

        else:
            print("Este email já é utilizado")
            return "Email já utilizado.", 401