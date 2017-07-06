from datetime import datetime
from distribuidora.run import db


class UnidadMedida(db.Model):
    __tablename__ = 'unidad_medida'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    cantidad = db.Column(db.Float)
    productos = db.relationship(
                        'Producto', backref='unidad_medida', lazy='dynamic'
                    )

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad


class Rol(db.Model):
    __tablename__ = 'rol'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(140))
    roles_administrativo = db.relationship(
                        'RolAdministrativo', backref='rol', lazy='dynamic'
                    )

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class RolAdministrativo(db.Model):
    __tablename__ = 'rol_administrativo'

    id = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'))
    id_administrativo = db.Column(
                            db.Integer, db.ForeignKey('administrativo.id')
                        )
    estado = db.Column(db.Boolean)


class Producto(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer, primary_key=True)
    id_unidad_medida = db.Column(db.Integer, db.ForeignKey('unidad_medida.id'))
    nombre = db.Column(db.String(45))
    productos_almacen = db.relationship(
                    'ProductoAlmacen', backref='producto', lazy='dynamic'
                )

    def __init__(self, nombre, unidad_medida):
        self.nombre = nombre
        self.unidad_medida = unidad_medida


class Almacen(db.Model):
    __tablename__ = 'almacen'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    direccion = db.Column(db.String(140))
    ubigeo = db.Column(db.String(6))
    productos_almacen = db.relationship(
                    'ProductoAlmacen', backref='almacen', lazy='dynamic'
                )

    def __init__(self, nombre, direccion, ubigeo):
        self.nombre = nombre
        self.direccion = direccion
        self.ubigeo = ubigeo


class ProductoAlmacen(db.Model):
    __tablename__ = 'producto_almacen'

    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id'))
    id_almacen = db.Column(db.Integer, db.ForeignKey('almacen.id'))
    cantidad = db.Column(db.Float)
    precio_compra = db.Column(db.Float)
    precio_venta = db.Column(db.Float)
    fecha_ingreso = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.now)
    productos_pedido = db.relationship(
                'ProductoPedido', backref='producto_almacen', lazy='dynamic'
            )

    def __init__(
            self, id_producto, id_almacen, cantidad,
            precio_compra, precio_venta, fecha_ingreso):
        self.id_producto = id_producto
        self.id_almacen = id_almacen
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.fecha_ingreso = fecha_ingreso
