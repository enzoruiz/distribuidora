from datetime import datetime
from distribuidora.run import db


class UnidadMedida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.String(45))
    productos = db.relationship(
                        'Producto', backref='unidadmedida', lazy='dynamic'
                    )


class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(140))
    roles_administrativo = db.relationship(
                        'RolAdministrativo', backref='rol', lazy='dynamic'
                    )


class RolAdministrativo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'))
    id_administrativo = db.Column(
                            db.Integer, db.ForeignKey('administrativo.id')
                        )
    estado = db.Column(db.Boolean)


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_unidad_medida = db.Column(db.Integer, db.ForeignKey('unidadmedida.id'))
    nombre = db.Column(db.String(45))
    productos_almacen = db.relationship(
                    'ProductoAlmacen', backref='producto', lazy='dynamic'
                )


class Almacen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    direccion = db.Column(db.String(140))
    ubigeo = db.Column(db.String(6))
    productos_almacen = db.relationship(
                    'ProductoAlmacen', backref='almacen', lazy='dynamic'
                )


class ProductoAlmacen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    id_almacen = db.Column(db.Integer, db.ForeignKey('almacen.id'))
    precio_compra = db.Column(db.Float)
    precio_venta = db.Column(db.Float)
    fecha_ingreso = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.now)
