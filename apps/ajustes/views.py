from flask_login import login_required
from flask import render_template, flash, redirect, url_for
from distribuidora.run import app, db
from .forms import UnidadMedidaForm, RolForm
from .models import UnidadMedida, Rol


@app.route('/unidad-medida')
@login_required
def list_unidad_medida():
    lista = UnidadMedida.query.all()
    return render_template('ajustes/unidad_medida/list.html', lista=lista)


@app.route('/unidad-medida/create', methods=['GET', 'POST'])
@login_required
def registro_unidad_medida():
    form = UnidadMedidaForm()
    if form.validate_on_submit():
        unidad_medida = UnidadMedida(
            form.nombre.data,
            form.cantidad.data
        )
        db.session.add(unidad_medida)
        db.session.commit()
        flash('Registro exitoso!')
        return redirect(url_for('list_unidad_medida'))

    return render_template(
        'ajustes/unidad_medida/create_update.html',
        form=form,
        accion='Crear'
    )


@app.route('/unidad-medida/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edicion_unidad_medida(id):
    unidad_medida = UnidadMedida.query.get(int(id))
    if unidad_medida is None:
        return redirect(url_for('list_unidad_medida'))

    form = UnidadMedidaForm(obj=unidad_medida)
    if form.validate_on_submit():
        unidad_medida.nombre = form.nombre.data
        unidad_medida.cantidad = form.cantidad.data
        db.session.commit()
        flash('Edicion exitosa!')
        return redirect(url_for('list_unidad_medida'))

    return render_template(
        'ajustes/unidad_medida/create_update.html',
        form=form,
        accion='Editar'
    )


@app.route('/unidad-medida/delete/<int:id>')
@login_required
def eliminar_unidad_medida(id):
    unidad_medida = UnidadMedida.query.get(int(id))
    if unidad_medida is None:
        return redirect(url_for('list_unidad_medida'))
    db.session.delete(unidad_medida)
    db.session.commit()
    return redirect(url_for('list_unidad_medida'))


@app.route('/rol')
@login_required
def list_rol():
    lista = Rol.query.all()
    return render_template('ajustes/rol/list.html', lista=lista)


@app.route('/rol/create', methods=['GET', 'POST'])
@login_required
def registro_rol():
    form = RolForm()
    if form.validate_on_submit():
        rol = Rol(
            form.nombre.data,
            form.descripcion.data
        )
        db.session.add(rol)
        db.session.commit()
        flash('Registro exitoso!')
        return redirect(url_for('list_rol'))

    return render_template(
        'ajustes/rol/create_update.html',
        form=form,
        accion='Crear'
    )


@app.route('/rol/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edicion_rol(id):
    rol = Rol.query.get(int(id))
    if rol is None:
        return redirect(url_for('list_rol'))

    form = RolForm(obj=rol)
    if form.validate_on_submit():
        rol.nombre = form.nombre.data
        rol.descripcion = form.descripcion.data
        db.session.commit()
        flash('Edicion exitosa!')
        return redirect(url_for('list_rol'))

    return render_template(
        'ajustes/rol/create_update.html',
        form=form,
        accion='Editar'
    )


@app.route('/rol/delete/<int:id>')
@login_required
def eliminar_rol(id):
    rol = Rol.query.get(int(id))
    if rol is None:
        return redirect(url_for('list_rol'))
    db.session.delete(rol)
    db.session.commit()
    return redirect(url_for('list_rol'))
