from flask import render_template
from distribuidora.run import app, db
from .forms import UserForm
from .models import User


@app.route('/')
def index():
    return render_template('intranet/home.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro_user():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user = User(
            username=user_form.username.data,
            documento_identidad=user_form.documento_identidad.data,
            email=user_form.email.data,
            telefono=user_form.telefono.data,
            password=user_form.password.data
        )
        db.session.add(user)
        db.session.commit()

    return render_template('intranet/registro_user.html', form=user_form)
