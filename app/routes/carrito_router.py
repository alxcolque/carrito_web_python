from flask import Blueprint
from app.controllers.CarritoController import carritocontroller
#from flask_login import login_required

carrito_router = Blueprint('carrito_router', __name__)

@carrito_router.route('/',methods=['GET'])
def index():
    return carritocontroller.index()
@carrito_router.route('/agregar',methods=['POST'])
def agregar():
    return carritocontroller.agregar()

@carrito_router.route('/retirar/<id>',methods=['GET'])
def retirar(id):
    return carritocontroller.retirar(id)
@carrito_router.route('/buscar',methods=['POST'])
def buscar():
    return carritocontroller.buscar()