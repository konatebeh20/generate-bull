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
    
    # Si tu souhaites ajouter les autres méthodes HTTP comme GET, DELETE, PATCH
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
