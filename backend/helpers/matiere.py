from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.bg import *
import bcrypt, jwt
from werkzeug.security import check_password_hash


def GererMatiere():
    reponse = {}
    try:
        nom_matiere = request.json.get('nom')
        code_matiere = request.json.get('code')

        nouvelle_matiere = Matiere()
        nouvelle_matiere.nom = nom_matiere
        nouvelle_matiere.code = code_matiere

        db.session.add(nouvelle_matiere)
        db.session.commit()

        reponse['status'] = 'success'
        reponse['message'] = 'Matière ajoutée avec succès'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse
