from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, InputRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField(
                        'Usuario o Email',
                        [
                            InputRequired('Usuario o Email requerido.')
                        ]
                    )
    password = PasswordField(
                    'Contraseña',
                    [
                        InputRequired('Contraseña requerida.')
                    ]
                )


class UserForm(FlaskForm):
    username = StringField(
                        'Usuario (*)',
                        [
                            InputRequired('Username requerido.')
                        ]
                    )
    documento_identidad = StringField(
                            'Nro. Documento (*)',
                            [
                                InputRequired('Nro. Documento requerido.'),
                                Length(
                                    min=8,
                                    max=11,
                                    message='Ingrese un Nro. Documento valido.'
                                )
                            ]
                        )
    email = EmailField(
                    'Email (*)',
                    [
                        InputRequired('Email requerido.'),
                        Email('Ingrese un Email valido')
                    ]
                )
    telefono = StringField('Telefono')
    password = PasswordField(
                    'Contraseña (*)',
                    [
                        InputRequired('Contraseña requerida.'),
                        EqualTo(
                            'confirm_password',
                            message='Las contraseñas deben ser iguales.'
                        )
                    ]
                )
    confirm_password = PasswordField(
                            'Confirmar Contraseña (*)',
                            [
                                InputRequired('Confirme su contraseña.')
                            ]
                        )
