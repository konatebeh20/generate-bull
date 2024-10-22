from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.bg import *
import bcrypt, jwt
from werkzeug.security import check_password_hash


def AjouterNotes():
    reponse = {}
    try:
        etudiant_id = request.json.get('etudiant_id')
        matiere_id = request.json.get('matiere_id')
        note_valeur = request.json.get('note_valeur')

        # Vérifier les données requises
        if not all([etudiant_id, matiere_id, note_valeur]):
            reponse['status'] = 'error'
            reponse['message'] = 'Données incomplètes'
            return reponse

        # Création d'une nouvelle note
        nouvelle_note = Note()
        nouvelle_note.etudiant_id = etudiant_id
        nouvelle_note.matiere_id = matiere_id
        nouvelle_note.note_valeur = note_valeur

        db.session.add(nouvelle_note)
        db.session.commit()

        reponse['status'] = 'success'
        reponse['message'] = 'Note ajoutée avec succès'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse
