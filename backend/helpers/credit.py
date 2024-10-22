from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.bg import *
import bcrypt, jwt
from werkzeug.security import check_password_hash


def GererCredit():
    reponse = {}
    try:
        matiere_id = request.json.get('matiere_id')
        nouveaux_credits = request.json.get('credits')

        matiere = Matiere.query.filter_by(id=matiere_id).first()

        if matiere:
            matiere.credits = nouveaux_credits
            db.session.commit()

            reponse['status'] = 'success'
            reponse['message'] = 'Crédits mis à jour avec succès'
        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Matière non trouvée'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse
