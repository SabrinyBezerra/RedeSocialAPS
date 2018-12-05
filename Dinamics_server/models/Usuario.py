from flask_restful import fields
from itsdangerous import (TimedJSONWebSignatureSerializer
as Serializer, BadSignature, SignatureExpired)

usuario_campos = {
    'id': fields.Integer,
    'email': fields.String,
    'nome': fields.String,
    'data_nascimento': fields.String,
    'genero': fields.String,
    'perfil_publico': fields.Boolean,
    'online': fields.Boolean,
    'estado_civil': fields.String
}

class Usuario():
    def __init__(self, email, senha, nome, data_nascimento, genero, perfil_publico, estado_civil, id=None, online=True, amigos=[], grupos=[]):
        self.id = id
        self.email = email
        self.senha = senha
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.perfil_publico = perfil_publico
        self.online = online
        self.estado_civil = estado_civil
        self.amigos = amigos
        self.grupos = grupos

    def verificar_senha(self, password):
        if password == self.senha:
            return True
        else:
            return False

    def generate_auth_token(self, expiration=None):
        s = Serializer('123456', expires_in=expiration)
        dumps = s.dumps({'id': self.id})

        self.token = dumps.decode('ascii')