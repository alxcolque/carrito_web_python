#producto
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, text
from sqlalchemy.sql import func
from app import db
class Carrito(db.Model):
    __tablename__ = 'carritos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #FK
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    cantidad = db.Column(db.Integer)
    #Default
    created_at = db.Column(TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    
    #R
    #carrito=db.relationship('Carrito', backref='producto', lazy='dynamic')
    