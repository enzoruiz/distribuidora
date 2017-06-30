from flask_login import login_required
from flask import render_template, flash, redirect, url_for
from distribuidora.run import app, db
from .forms import UnidadMedidaForm
from .models import UnidadMedida


@app.route('/unidad-medida', methods=['GET', 'POST'])
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

    return render_template('ajustes/unidad_medida/create.html', form=form)
