from urllib.parse import urlparse, urljoin
from flask import render_template, flash, request, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from distribuidora.run import app, db, login_manager
from .forms import UserForm, LoginForm
from .models import User


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return (
        test_url.scheme in
        ('http', 'https') and ref_url.netloc == test_url.netloc
    )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/registro', methods=['GET', 'POST'])
@login_required
def registro_user():
    user_form = UserForm()
    if user_form.validate_on_submit():
        user = User(
            user_form.username.data,
            user_form.documento_identidad.data,
            user_form.email.data,
            user_form.telefono.data,
            user_form.password.data
        )
        db.session.add(user)
        db.session.commit()

    return render_template('intranet/registro_user.html', form=user_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(
                        username=login_form.username.data
                    ).first()
        if user:
            if check_password_hash(user.password, login_form.password.data):
                login_user(user)
                print(request.args.get('next'))
                if request.args.get('next'):
                    next = request.args.get('next')
                    if not is_safe_url(next):
                        return abort(400)
                    return redirect(next)
                return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrecta.')
            return redirect(url_for('login'))
    return render_template('login.html', form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
