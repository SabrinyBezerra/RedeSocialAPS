from database.UsuarioDAO import UsuarioDAO
from itsdangerous import (TimedJSONWebSignatureSerializer
as Serializer, BadSignature, SignatureExpired)

class VerifyAuthToken():

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('123456')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token

        usuarioDAO = UsuarioDAO()
        users = usuarioDAO.listarUsuarios()

        for user in users:
            if user.id == data['id']:
                return user