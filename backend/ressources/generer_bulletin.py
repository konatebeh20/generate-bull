from flask_restful import Resource
import json
from backend.config import db
from backend.helpers import note
from helpers import *
from flask import app, request

def generer_bulletin(etudiant_id):
    # Logique pour générer le bulletin
    # Cette fonction devrait récupérer toutes les notes de l'étudiant
    # et les formater selon le modèle de bulletin fourni
    # Vous pouvez utiliser une bibliothèque comme openpyxl pour Excel
    # ou python-docx pour Word
    pass