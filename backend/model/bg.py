import datetime
from flask_login import UserMixin
import pymysql
from config import db
from config import constant
from config.db import *
from config.constant import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# Modèles de base de données
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_fullname = db.Column(db.String(128), nullable=False)
    ad_username = db.Column(db.String(128), nullable=False)
    ad_mobile = db.Column(db.String(128), nullable=False)
    ad_address = db.Column(db.String(128), nullable=False)
    ad_email = db.Column(db.String(128), nullable=False)
    ad_password = db.Column(db.String(128), nullable=False)
    ad_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ad_fullname = db.Column(db.String(128), nullable=False)
    ad_username = db.Column(db.String(128), nullable=False)
    ad_mobile = db.Column(db.String(128), nullable=False)
    ad_address = db.Column(db.String(128), nullable=False)
    ad_email = db.Column(db.String(128), nullable=False)
    ad_password = db.Column(db.String(128), nullable=False)
    ad_uid = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    date_naissance = db.Column(db.Date, nullable=False)
    lieu_naissance = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(10), nullable=False)
    matricule = db.Column(db.String(20), unique=True, nullable=False)
    licence = db.Column(db.String(50), nullable=False)
    niveau = db.Column(db.String(20), nullable=False)

class Matiere(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    nom = db.Column(db.String(100), nullable=False)
    credits = db.Column(db.Integer, nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    etudiant_id = db.Column(db.Integer, db.ForeignKey('etudiant.id'), nullable=False)
    matiere_id = db.Column(db.Integer, db.ForeignKey('matiere.id'), nullable=False)
    note = db.Column(db.Float, nullable=False)
    annee_academique = db.Column(db.String(9), nullable=False)
    
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128))

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)