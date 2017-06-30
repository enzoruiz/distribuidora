from distribuidora.run import db


class Pedido(db.Model):
    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    fecha_creacion = db.Column(db.Date)
    fecha_entrega = db.Column(db.Date)
    estado = db.Column(db.String(2))
    productos_pedido = db.relationship(
                    'ProductoPedido', backref='pedido', lazy='dynamic'
                )


class ProductoPedido(db.Model):
    __tablename__ = 'producto_pedido'

    id = db.Column(db.Integer, primary_key=True)
    id_producto_almacen = db.Column(
                            db.Integer, db.ForeignKey('producto_almacen.id')
                        )
    id_pedido = db.Column(
                            db.Integer, db.ForeignKey('pedido.id')
                        )
    cantidad = db.Column(db.Float)
