
from flask_restful import Resource
import json
from backend.config import db
from backend.helpers import note
from helpers import *
from flask import app, request

def ajouter_note():
    data = request.json
    nouvelle_note = note(
        etudiant_id=data['etudiant_id'],
        matiere_id=data['matiere_id'],
        note=data['note'],
        annee_academique=data['annee_academique']
    )
    db.session.add(nouvelle_note)
    db.session.commit()
    return jsonify({"message": "Note ajoutée avec succès"}), 201

