from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class UnidadMedidaForm(FlaskForm):
    nombre = StringField(
                        'Nombre',
                        [
                            InputRequired('Nombre requerido.')
                        ]
                    )
    cantidad = StringField(
                    'Cantidad',
                    [
                        InputRequired('Cantidad requerida.')
                    ]
                )