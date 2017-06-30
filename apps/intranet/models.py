from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from distribuidora.run import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True)
    documento_identidad = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(35), unique=True)
    telefono = db.Column(db.String(15))
    password = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    cliente = db.relationship("Cliente", uselist=False, backref="user")
    administrativo = db.relationship(
                                "Administrativo", uselist=False, backref="user"
                            )

    def __init__(self, username, doc_identidad, email, telefono, password):
        self.username = username
        self.documento_identidad = doc_identidad
        self.email = email
        self.telefono = telefono
        self.password = self.__crear_password(password)

    def __crear_password(self, password):
        return generate_password_hash(password)


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    razon_social = db.Column(db.String(45))
    direccion = db.Column(db.String(45))
    ubigeo = db.Column(db.String(6))
    representante_legal = db.Column(db.String(45))
    pedidos = db.relationship(
                        'Pedido', backref='cliente', lazy='dynamic'
                    )


class Administrativo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    nombres = db.Column(db.String(45))
    apellidos = db.Column(db.String(45))
    roles_administrativo = db.relationship(
                'RolAdministrativo', backref='administrativo', lazy='dynamic'
            )
