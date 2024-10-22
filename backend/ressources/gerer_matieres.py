from flask_restful import Resource
import json
from backend.config import db
from backend.helpers import note
from helpers import *
from flask import app, request

@app.route('/api/matieres', methods=['GET', 'POST'])
def gerer_matieres():
    if request.method == 'POST':
        data = request.json
        nouvelle_matiere = matiere(
            code=data['code'],
            nom=data['nom'],
            credits=data['credits']
        )
        db.session.add(nouvelle_matiere)
        db.session.commit()
        return jsonify({"message": "Matière ajoutée avec succès"}), 201
    else:
        matieres = matiere.query.all()
        return jsonify([{
            "id": m.id,
            "code": m.code,
            "nom": m.nom,
            "credits": m.credits
        } for m in matieres])