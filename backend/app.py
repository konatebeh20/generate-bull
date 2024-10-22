from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask
from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash
import os
from flask_restful import Resource, Api
from ressources.admin import AdminApi
from config.db import db
from config.constant import *
from model.bg import *

# from resources.admin import AdminApi
# from resources.user import UserApi
# from resources.item import ItemApi
# from resources.login import LoginApi

from flask_migrate import Migrate
from flask_cors import CORS

from flask_restful import Api


app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "https://tt_officiel.com"}})

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.secret_key = os.urandom(24)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = LIEN_BASE_DE_DONNEES
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Ajouter les routes
Api.add_resource(AdminApi, '/admin/<string:route>')

mysql = MySQL(app)

db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)



@app.route('/a')
def home():
    print('Trouvez Tous Officiel')
    return render_template('index.html')

# api.add_resource(AdminApi, '/api/admin/<string:route>', endpoint='all_admin', methods=['GET', 'POST', 'DELETE', 'PATCH'])
# api.add_resource(UserApi, '/api/user/<string:route>', endpoint='all_user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
# api.add_resource(ItemApi, '/api/item/<string:route>', endpoint='all_item', methods=['GET', 'POST', 'DELETE', 'PATCH'])

if __name__ == '__main__':
    app.run(debug=False,  host="0.0.0.0")