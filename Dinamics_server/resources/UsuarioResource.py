from flask_restful import Resource, marshal_with, abort
from database.UsuarioDAO import UsuarioDAO
from models.Usuario import Usuario, usuario_campos
from util.VerifyAuthToken import VerifyAuthToken

class UsuarioResource(Resource):

    # GET /user/<id>
    @marshal_with(usuario_campos)
    def get(self, id):

        user = VerifyAuthToken.verify_auth_token(id)
        if user == None:
            return "Usuário não encontrado.", 404
        else:
            return user, 200