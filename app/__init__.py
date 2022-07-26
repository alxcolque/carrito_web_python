__version__ = "0.1"
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import app.config
from app.config import (_db_user, _db_pass, _db_host,_db_name, _os_path)


import secrets

#
OS_PAHT = _os_path 

app = Flask(__name__, template_folder="views")
#configuraciones base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    os.getenv('DB_USER', _db_user),
    os.getenv('DB_PASSWORD', _db_pass),
    os.getenv('DB_HOST', _db_host),
    os.getenv('DB_NAME', _db_name)
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)


secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True


#rutas

from app.routes.carrito_router import carrito_router
app.register_blueprint(carrito_router)

