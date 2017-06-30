from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config/local.py')

csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message = 'Necesitas iniciar sesion!'

# VIEWS
from apps.intranet.views import *
from apps.ajustes.views import *
from apps.negocio.views import *

# MODELS
from apps.intranet.models import *
from apps.ajustes.models import *
from apps.negocio.models import *

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
