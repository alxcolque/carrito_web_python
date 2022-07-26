from app import db, app
from flask import render_template, request, redirect, url_for, flash, session

from app.models.Producto import Producto
from app.models.Carrito import Carrito

class CarritoController():
    def __init__(self):
        pass

    def index(self):
        producto = Producto.query.all()
        carrito = Carrito.query\
            .join(Producto, Producto.id==Carrito.producto_id)\
            .all()
        suma = 0
        for row in carrito:
            suma = suma + row.producto.precio*row.cantidad
        return render_template('index.html',producto=producto, carrito=carrito, total=suma)
    def agregar(self):
        if request.method == 'POST':
            producto_id=request.form['id']
            cantidad=request.form['cantidad']
            carrito = Carrito(producto_id=producto_id,cantidad=cantidad)
            db.session.add(carrito)
            db.session.commit()
            return redirect(url_for('carrito_router.index'))
        return redirect(url_for('carrito_router.index'))

    def retirar(self, id):
        product = db.session.query(Carrito).filter(Carrito.id==id).one()
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('carrito_router.index'))
    def buscar(self):
        if request.method == 'POST':
            buscar=request.form['buscar']
            producto = db.session.query(Producto).\
                filter(Producto.descripcion.contains(buscar))
            carrito = Carrito.query\
                .join(Producto, Producto.id==Carrito.producto_id)\
                .all()
            suma = 0
            for row in carrito:
                suma = suma + row.producto.precio*row.cantidad
            return render_template('index.html',producto=producto, carrito=carrito, total=suma)
carritocontroller = CarritoController()
