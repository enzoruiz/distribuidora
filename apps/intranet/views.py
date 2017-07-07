from urllib.parse import urlparse, urljoin
from flask import render_template, flash, request, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from distribuidora.run import app, db, login_manager
from .forms import UserForm, LoginForm, ClienteForm
from .models import User, Cliente


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
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            form.username.data,
            form.documento_identidad.data,
            form.email.data,
            form.telefono.data,
            form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('intranet/registro_user.html', form=form)


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


@app.route('/cliente')
@login_required
def list_cliente():
    lista = Cliente.query.all()
    return render_template('ajustes/cliente/list.html', lista=lista)


@app.route('/cliente/create', methods=['GET', 'POST'])
@login_required
def registro_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        unidad_medida = UnidadMedida.query.get(int(form.id_unidad_medida.data))
        if unidad_medida is None:
            flash('Unidad de Medida no existente')
            return redirect(url_for('registro_cliente'))
        cliente = Cliente(
            form.nombre.data,
            unidad_medida
        )
        db.session.add(cliente)
        db.session.commit()

        flash('Registro exitoso!')
        return redirect(url_for('list_cliente'))

    return render_template(
        'ajustes/cliente/create_update.html',
        form=form,
        accion='Crear'
    )


@app.route('/cliente/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edicion_cliente(id):
    cliente = Cliente.query.get(int(id))
    if cliente is None:
        return redirect(url_for('list_cliente'))

    form = ClienteForm(obj=cliente)
    if form.validate_on_submit():
        unidad_medida = UnidadMedida.query.get(int(form.id_unidad_medida.data))
        if unidad_medida is None:
            flash('Unidad de Medida no existente')
            return redirect(url_for('registro_cliente'))
        cliente.nombre = form.nombre.data
        cliente.id_unidad_medida = int(form.id_unidad_medida.data)
        db.session.commit()
        flash('Edicion exitosa!')
        return redirect(url_for('list_cliente'))

    return render_template(
        'ajustes/cliente/create_update.html',
        form=form,
        accion='Editar'
    )


@app.route('/cliente/delete/<int:id>')
@login_required
def eliminar_cliente(id):
    cliente = Cliente.query.get(int(id))
    if cliente is None:
        return redirect(url_for('list_cliente'))
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('list_cliente'))
