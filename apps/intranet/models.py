from datetime import datetime
from distribuidora.run import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True)
    documento_identidad = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(35), unique=True)
    password = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
