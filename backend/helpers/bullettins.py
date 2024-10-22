from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.bg import *
import bcrypt, jwt
from werkzeug.security import check_password_hash

def GenererBulletins():
    reponse = {}
    try:
        etudiant_id = request.json.get('etudiant_id')

        # Récupérer les notes de l'étudiant
        notes = Note.query.filter_by(etudiant_id=etudiant_id).all()

        if notes:
            bulletin = []
            for note in notes:
                matiere = Matiere.query.filter_by(id=note.matiere_id).first()
                bulletin.append({
                    'matiere': matiere.nom,
                    'note': note.note_valeur
                })

            reponse['status'] = 'success'
            reponse['bulletin'] = bulletin
        else:
            reponse['status'] = 'error'
            reponse['message'] = 'Aucune note trouvée pour cet étudiant'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse
