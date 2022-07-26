#producto
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from app import db
class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo = db.Column(String(30))
    descripcion = db.Column(String(500))
    precio = db.Column(db.Numeric(10,2))
    #Default
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    
    #R
    #carrito=db.relationship('Producto', backref='carrito', lazy='dynamic')
    carrito=db.relationship('Carrito', backref='producto', lazy='dynamic')