from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.bg import *
import bcrypt, jwt
from werkzeug.security import check_password_hash


def GererEtudiant():
    reponse = {}
    try:
        etudiant_nom = request.json.get('nom')
        etudiant_prenom = request.json.get('prenom')
        etudiant_email = request.json.get('email')

        # Création d'un nouvel étudiant
        nouvel_etudiant = Etudiant()
        nouvel_etudiant.nom = etudiant_nom
        nouvel_etudiant.prenom = etudiant_prenom
        nouvel_etudiant.email = etudiant_email

        db.session.add(nouvel_etudiant)
        db.session.commit()

        reponse['status'] = 'success'
        reponse['message'] = 'Étudiant ajouté avec succès'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse
