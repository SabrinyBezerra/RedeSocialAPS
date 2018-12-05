from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from resources.CadastroResource import CadastroResource
from resources.LoginResource import LoginResource
from resources.UsuarioResource import UsuarioResource

app = Flask(__name__)

app.config['DEBUG'] = True

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/api')

#Resources
api.add_resource(CadastroResource, '/cadastro')
api.add_resource(LoginResource, '/login')
api.add_resource(UsuarioResource, '/user/<string:id>')

app.register_blueprint(api_bp)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run()
    #app.run(host='0.0.0.0')
