from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Length
from .models import UnidadMedida, Producto, Almacen, Rol
from ..intranet.models import Administrativo


class UnidadMedidaForm(FlaskForm):
    nombre = StringField(
                        'Nombre',
                        [
                            InputRequired('Nombre requerido.')
                        ]
                    )
    cantidad = FloatField(
                    'Cantidad',
                    [
                        InputRequired('Cantidad requerida.')
                    ]
                )


class RolForm(FlaskForm):
    nombre = StringField(
                        'Nombre',
                        [
                            InputRequired('Nombre requerido.')
                        ]
                    )
    descripcion = StringField(
                    'Descripcion',
                    [
                        InputRequired('Descripcion requerida.')
                    ]
                )


class ProductoForm(FlaskForm):
    nombre = StringField(
                        'Nombre',
                        [
                            InputRequired('Nombre requerido.')
                        ]
                    )
    id_unidad_medida = SelectField('Unidad de Medida', choices=[], coerce=int)

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.id_unidad_medida.choices = [
                        (um.id, um.nombre) for um in UnidadMedida.query.all()
                    ]


class AlmacenForm(FlaskForm):
    nombre = StringField(
                        'Nombre',
                        [
                            InputRequired('Nombre requerido.'),
                            Length(max=45)
                        ]
                    )
    direccion = StringField(
                    'Direccion',
                    [
                        InputRequired('Direccion requerida.'),
                        Length(max=140)
                    ]
                )
    ubigeo = StringField(
                    'Ubigeo',
                    [
                        InputRequired('Ubigeo requerido.')
                    ]
                )


class ProductoAlmacenForm(FlaskForm):
    cantidad = FloatField(
                        'Cantidad',
                        [
                            InputRequired('Cantidad requerido.')
                        ]
                    )
    precio_compra = FloatField(
                        'Precio Compra',
                        [
                            InputRequired('Precio Compra requerido.')
                        ]
                    )
    precio_venta = FloatField(
                    'Precio Venta',
                    [
                        InputRequired('Precio Venta requerida.')
                    ]
                )
    fecha_ingreso = DateField(
                    'Fecha Ingreso',
                    format='%d/%m/%Y',
                    validators=[
                        InputRequired('Fecha Ingreso requerido.')
                    ]
                )
    id_producto = SelectField('Producto', choices=[], coerce=int)
    id_almacen = SelectField('Almacen', choices=[], coerce=int)

    def __init__(self, *args, **kwargs):
        super(ProductoAlmacenForm, self).__init__(*args, **kwargs)
        self.id_producto.choices = [
                        (pro.id, pro.nombre) for pro in Producto.query.all()
                    ]
        self.id_almacen.choices = [
                        (alm.id, alm.nombre) for alm in Almacen.query.all()
                    ]


class RolAdministrativoForm(FlaskForm):
    id_rol = SelectField('Rol', choices=[], coerce=int)
    id_administrativo = SelectField('Administrativo', choices=[], coerce=int)
    estado = BooleanField('Activo?')

    def __init__(self, *args, **kwargs):
        super(RolAdministrativoForm, self).__init__(*args, **kwargs)
        self.id_rol.choices = [
                        (rol.id, rol.nombre) for rol in Rol.query.all()
                    ]
        self.id_administrativo.choices = [
                        (am.id, am.nombre) for am in Administrativo.query.all()
                    ]
