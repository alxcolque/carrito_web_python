
from app import db, app
from app.models.Producto import Producto
from app.models.Carrito import Carrito
def crear_producto():
    #from sqlalchemy import func
    #user_id = session.query(func.max(User.id)).scalar()
    id = 1
    codigo = 'C-001'
    descripcion = 'Boligrafos'
    precio = 2
    
    producto = Producto(id=id, codigo=codigo,descripcion=descripcion,precio=precio)
    db.session.add(producto)
    db.session.commit()

    codigo = 'C-003'
    descripcion = 'Marcadores'
    precio = 12
    
    producto = Producto(codigo=codigo,descripcion=descripcion,precio=precio)
    db.session.add(producto)
    db.session.commit()

    codigo = 'C-101'
    descripcion = 'Cuaderno 50 Hojas'
    precio = 22.5
    
    producto = Producto(codigo=codigo,descripcion=descripcion,precio=precio)
    db.session.add(producto)
    db.session.commit()

    codigo = 'C-202'
    descripcion = 'Plastoformo 1cm'
    precio = 12
    
    producto = Producto(codigo=codigo,descripcion=descripcion,precio=precio)
    db.session.add(producto)
    db.session.commit()

    codigo = 'C-004'
    descripcion = 'Micropunta'
    precio = 21
    
    producto = Producto(codigo=codigo,descripcion=descripcion,precio=precio)
    db.session.add(producto)
    db.session.commit()

    codigo = 'C-502'
    descripcion = 'Estuche Geométrico'
    precio = 87
    
    producto = Producto(codigo=codigo,descripcion=descripcion,precio=precio)
    db.session.add(producto)
    db.session.commit()

    codigo = 'C-700'
    descripcion = 'Impresora Epson L220'
    precio = 1304
    
    producto = Producto(codigo=codigo,descripcion=descripcion,precio=precio)
    db.session.add(producto)
    db.session.commit()

db.drop_all()
db.create_all()
crear_producto()

