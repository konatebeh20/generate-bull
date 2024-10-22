from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from flask import request, jsonify
import uuid
from config.db import db
from model.bg import *
import bcrypt, jwt
from werkzeug.security import check_password_hash

# def AjouterNotes():
#     # Logique pour ajouter des notes
#     return {"message": "Notes ajoutées avec succès"}, 201

# def GenererBulletins():
#     # Logique pour générer des bulletins
#     return {"message": "Bulletins générés avec succès"}, 201

# def GererEtudiant():
#     # Logique pour gérer un étudiant
#     return {"message": "Étudiant géré avec succès"}, 200

# def GererMatiere():
#     # Logique pour gérer une matière
#     return {"message": "Matière gérée avec succès"}, 200

# def GererCredit():
#     # Logique pour gérer le crédit
#     return {"message": "Crédit géré avec succès"}, 200




from flask_restful import Resource
from flask import request
from helpers.admin import (
    CreateAdmin, LoginAdmin, AjouterNotes, GenererBulletins, 
    GererEtudiant, GererMatiere, GererCredit
)

class AdminApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateAdmin()
        if route == "login":
            return LoginAdmin()
        if route == "ajouter_notes":
            return AjouterNotes()
        if route == "generer_bulletins":
            return GenererBulletins()
        if route == "gerer_etudiant":
            return GererEtudiant()
        if route == "gerer_matiere":
            return GererMatiere()
        if route == "gerer_credit":
            return GererCredit()
    
    # # Si tu souhaites ajouter les autres méthodes HTTP comme GET, DELETE, PATCH
    # def get(self, route):
    #     # Exemple pour la lecture des informations d'un administrateur
    #     if route == "readall":
    #         return ReadAllAdmin()
    #     if route == "readsingle":
    #         return ReadSingleAdmin()
        
    # def delete(self, route):
    #     if route == "delete":
    #         return DeleteAdmin()
    
    # def patch(self, route):
    #     if route == "update":
    #         return UpdateAdmin()
