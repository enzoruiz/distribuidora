from flask_login import login_required
from flask import render_template, flash, redirect, url_for
from distribuidora.run import app, db
from .forms import (UnidadMedidaForm, RolForm, ProductoForm,
                    AlmacenForm, ProductoAlmacenForm, RolAdministrativoForm)
from .models import (
                UnidadMedida, Rol, Producto, Almacen,
                ProductoAlmacen, RolAdministrativo)
from ..intranet.models import Administrativo


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


@app.route('/producto')
@login_required
def list_producto():
    lista = Producto.query.all()
    return render_template('ajustes/producto/list.html', lista=lista)


@app.route('/producto/create', methods=['GET', 'POST'])
@login_required
def registro_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        unidad_medida = UnidadMedida.query.get(int(form.id_unidad_medida.data))
        if unidad_medida is None:
            flash('Unidad de Medida no existente')
            return redirect(url_for('registro_producto'))
        producto = Producto(
            form.nombre.data,
            unidad_medida
        )
        db.session.add(producto)
        db.session.commit()

        flash('Registro exitoso!')
        return redirect(url_for('list_producto'))

    return render_template(
        'ajustes/producto/create_update.html',
        form=form,
        accion='Crear'
    )


@app.route('/producto/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edicion_producto(id):
    producto = Producto.query.get(int(id))
    if producto is None:
        return redirect(url_for('list_producto'))

    form = ProductoForm(obj=producto)
    if form.validate_on_submit():
        unidad_medida = UnidadMedida.query.get(int(form.id_unidad_medida.data))
        if unidad_medida is None:
            flash('Unidad de Medida no existente')
            return redirect(url_for('registro_producto'))
        producto.nombre = form.nombre.data
        producto.id_unidad_medida = int(form.id_unidad_medida.data)
        db.session.commit()
        flash('Edicion exitosa!')
        return redirect(url_for('list_producto'))

    return render_template(
        'ajustes/producto/create_update.html',
        form=form,
        accion='Editar'
    )


@app.route('/producto/delete/<int:id>')
@login_required
def eliminar_producto(id):
    producto = Producto.query.get(int(id))
    if producto is None:
        return redirect(url_for('list_producto'))
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('list_producto'))


@app.route('/almacen')
@login_required
def list_almacen():
    lista = Almacen.query.all()
    return render_template('ajustes/almacen/list.html', lista=lista)


@app.route('/almacen/create', methods=['GET', 'POST'])
@login_required
def registro_almacen():
    form = AlmacenForm()
    if form.validate_on_submit():
        almacen = Almacen(
            form.nombre.data,
            form.direccion.data,
            form.ubigeo.data
        )
        db.session.add(almacen)
        db.session.commit()

        flash('Registro exitoso!')
        return redirect(url_for('list_almacen'))

    return render_template(
        'ajustes/almacen/create_update.html',
        form=form,
        accion='Crear'
    )


@app.route('/almacen/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edicion_almacen(id):
    almacen = Almacen.query.get(int(id))
    if almacen is None:
        return redirect(url_for('list_almacen'))

    form = AlmacenForm(obj=almacen)
    if form.validate_on_submit():
        almacen.nombre = form.nombre.data
        almacen.direccion = form.direccion.data
        almacen.ubigeo = form.ubigeo.data
        db.session.commit()
        flash('Edicion exitosa!')
        return redirect(url_for('list_almacen'))

    return render_template(
        'ajustes/almacen/create_update.html',
        form=form,
        accion='Editar'
    )


@app.route('/almacen/delete/<int:id>')
@login_required
def eliminar_almacen(id):
    almacen = Almacen.query.get(int(id))
    if almacen is None:
        return redirect(url_for('list_almacen'))
    db.session.delete(almacen)
    db.session.commit()
    return redirect(url_for('list_almacen'))


@app.route('/producto-almacen')
@login_required
def list_producto_almacen():
    lista = ProductoAlmacen.query.all()
    return render_template('ajustes/producto_almacen/list.html', lista=lista)


@app.route('/producto-almacen/create', methods=['GET', 'POST'])
@login_required
def registro_producto_almacen():
    form = ProductoAlmacenForm()
    if form.validate_on_submit():
        almacen = Almacen.query.get(int(form.id_almacen.data))
        if almacen is None:
            flash('Almacen no existente')
            return redirect(url_for('registro_producto_almacen'))
        producto = Producto.query.get(int(form.id_producto.data))
        if producto is None:
            flash('Producto no existente')
            return redirect(url_for('registro_producto_almacen'))
        producto_almacen = ProductoAlmacen(
            form.id_producto.data,
            form.id_almacen.data,
            form.cantidad.data,
            form.precio_compra.data,
            form.precio_venta.data,
            form.fecha_ingreso.data
        )
        db.session.add(producto_almacen)
        db.session.commit()

        flash('Registro exitoso!')
        return redirect(url_for('list_producto_almacen'))

    return render_template(
        'ajustes/producto_almacen/create_update.html',
        form=form,
        accion='Crear'
    )


@app.route('/producto-almacen/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edicion_producto_almacen(id):
    producto_almacen = ProductoAlmacen.query.get(int(id))
    if producto_almacen is None:
        return redirect(url_for('list_producto_almacen'))

    form = ProductoAlmacenForm(obj=producto_almacen)

    almacen = Almacen.query.get(int(form.id_almacen.data))
    if almacen is None:
        flash('Almacen no existente')
        return redirect(url_for('registro_producto_almacen'))
    producto = Producto.query.get(int(form.id_producto.data))
    if producto is None:
        flash('Producto no existente')
        return redirect(url_for('registro_producto_almacen'))

    if form.validate_on_submit():
        producto_almacen.id_producto = form.id_producto.data
        producto_almacen.id_almacen = form.id_almacen.data
        producto_almacen.cantidad = form.cantidad.data
        producto_almacen.precio_compra = form.precio_compra.data
        producto_almacen.precio_venta = form.precio_venta.data
        producto_almacen.fecha_ingreso = form.fecha_ingreso.data
        db.session.commit()
        flash('Edicion exitosa!')
        return redirect(url_for('list_producto_almacen'))

    return render_template(
        'ajustes/producto_almacen/create_update.html',
        form=form,
        accion='Editar'
    )


@app.route('/producto-almacen/delete/<int:id>')
@login_required
def eliminar_producto_almacen(id):
    producto_almacen = ProductoAlmacen.query.get(int(id))
    if producto_almacen is None:
        return redirect(url_for('list_producto_almacen'))
    db.session.delete(producto_almacen)
    db.session.commit()
    return redirect(url_for('list_producto_almacen'))


@app.route('/rol-administrativo')
@login_required
def list_rol_administrativo():
    lista = RolAdministrativo.query.all()
    return render_template('ajustes/rol_administrativo/list.html', lista=lista)


@app.route('/rol-administrativo/create', methods=['GET', 'POST'])
@login_required
def registro_rol_administrativo():
    form = RolAdministrativoForm()
    if form.validate_on_submit():
        rol = Rol.query.get(int(form.id_rol.data))
        if rol is None:
            flash('Almacen no existente')
            return redirect(url_for('registro_rol_administrativo'))
        administrativo = Administrativo.query.get(
                                            int(form.id_administrativo.data)
                                        )
        if administrativo is None:
            flash('Producto no existente')
            return redirect(url_for('registro_rol_administrativo'))
        rol_administrativo = RolAdministrativo(
            form.id_rol.data,
            form.id_administrativo.data,
            form.estado.data
        )
        db.session.add(rol_administrativo)
        db.session.commit()

        flash('Registro exitoso!')
        return redirect(url_for('list_rol_administrativo'))

    return render_template(
        'ajustes/rol_administrativo/create_update.html',
        form=form,
        accion='Crear'
    )


@app.route('/rol-administrativo/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edicion_rol_administrativo(id):
    rol_administrativo = RolAdministrativo.query.get(int(id))
    if rol_administrativo is None:
        return redirect(url_for('list_rol_administrativo'))

    form = RolAdministrativoForm(obj=rol_administrativo)

    rol = Rol.query.get(int(form.id_rol.data))
    if rol is None:
        flash('Almacen no existente')
        return redirect(url_for('registro_rol_administrativo'))
    administrativo = Administrativo.query.get(
                                        int(form.id_administrativo.data)
                                    )
    if administrativo is None:
        flash('Producto no existente')
        return redirect(url_for('registro_rol_administrativo'))

    if form.validate_on_submit():
        rol_administrativo.id_rol = form.id_rol.data
        rol_administrativo.id_administrativo = form.id_administrativo.data
        rol_administrativo.estado = form.estado.data
        db.session.commit()
        flash('Edicion exitosa!')
        return redirect(url_for('list_rol_administrativo'))

    return render_template(
        'ajustes/rol_administrativo/create_update.html',
        form=form,
        accion='Editar'
    )


@app.route('/rol-administrativo/delete/<int:id>')
@login_required
def eliminar_rol_administrativo(id):
    rol_administrativo = RolAdministrativo.query.get(int(id))
    if rol_administrativo is None:
        return redirect(url_for('list_rol_administrativo'))
    db.session.delete(rol_administrativo)
    db.session.commit()
    return redirect(url_for('list_rol_administrativo'))
