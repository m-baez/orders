from flask import render_template, g, request, redirect, url_for, abort

from app.orders import orders_bp
from app.db import db, cursor, time_zone

from datetime import datetime

hoy = datetime.now()
meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
numero_mes = int(hoy.strftime('%m'))
mes_actual = numero_mes - 1
fecha = hoy.strftime(
    '%d de {} del %Y').format(meses[mes_actual])


@orders_bp.route('/print/<int:id>', methods=['GET', 'POST'])
def print_ticket(id):

    query = ('SELECT * FROM productos WHERE id = %s')
    cursor.execute(query, (id,))

    data = cursor.fetchone()

    if data is not None:

        client = data[1]
        product = data[2]
        size = data[3]
        quantity = data[4]
        date = data[5]
        date_n = date.strftime('%d de {} del %Y').format(meses[mes_actual])
        hour = data[6]
        description = data[7]
        amount = data[8]
        rest = data[9]
        total = data[10]

    return render_template('print_opro.html', cliente=client, producto=product, tamaño=size, cantidad=quantity, fecha=date_n, hora=hour, descripcion=description, anticipo=amount, resta=rest, total=total)


@orders_bp.route('/pedidos_produccion', methods=['GET', 'POST'])
def view_orders_production():

    time_zone
    cursor.execute(
        'SELECT DATE_FORMAT(fecha,"%d de %M del %Y"),cliente,producto,tamaño,cantidad,descripcion,id FROM productos ORDER BY fecha')

    pedidos = cursor.fetchall()

    return render_template('order_list.html', pedidos=pedidos)


@orders_bp.route('/nuevo_pedido', methods=['GET', 'POST'])
def new_orders():
    if request.method == 'POST':
        cliente = request.form['cliente']
        producto = request.form['producto']
        tamaño = request.form['tamaño']
        cantidad = request.form['cantidad']
        fecha = request.form['fecha']
        hora = request.form['hora']
        descripcion = request.form['descripcion']
        anticipo = request.form['anticipo']
        resta = request.form['resta']
        total = request.form['total']

        cursor.execute(
            'INSERT INTO productos (cliente,producto,tamaño,cantidad,fecha,hora,descripcion,anticipo,resta,total)'
            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (cliente, producto, tamaño, cantidad, fecha, hora, descripcion, anticipo, resta, total))

        db.commit()

        return redirect(url_for('orders.view_orders_production'))

    return render_template('new_orders.html')
