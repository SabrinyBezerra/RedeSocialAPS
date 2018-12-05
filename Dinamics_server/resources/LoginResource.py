from flask_restful import Resource, marshal_with, abort
from flask import request
from database.UsuarioDAO import UsuarioDAO

class LoginResource(Resource):

    # POST /login
    def post(self):

        usuario = request.json
        print(usuario)
        usuarioDAO = UsuarioDAO()

        users = usuarioDAO.listarUsuarios()
        for user in users:
            if user.email == usuario["email_nickname"]:
                if user.verificar_senha(usuario["senha"]):
                    user.generate_auth_token()
                    return user.token, 200

        return "Dados de login incorretos.", 404
