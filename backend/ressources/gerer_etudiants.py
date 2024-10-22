
from flask_restful import Resource
import json
from config import db
from model.bg import *
from helpers import *
from flask import app, request
from flask import request, jsonify


@app.route('/api/etudiants', methods=['GET', 'POST'])
def gerer_etudiants():
    if request.method == 'POST':
        data = request.json
        nouvel_etudiant = Etudiant(
            nom=data['nom'],
            prenom=data['prenom'],
            date_naissance=data['date_naissance'],
            lieu_naissance=data['lieu_naissance'],
            genre=data['genre'],
            matricule=data['matricule'],
            licence=data['licence'],
            niveau=data['niveau']
        )
        db.session.add(nouvel_etudiant)
        db.session.commit()
        return jsonify({"message": "Étudiant ajouté avec succès"}), 201
    else:
        etudiants = Etudiant.query.all()
        return jsonify([{
            "id": e.id,
            "nom": e.nom,
            "prenom": e.prenom,
            "matricule": e.matricule,
            "licence": e.licence,
            "niveau": e.niveau
        } for e in etudiants])