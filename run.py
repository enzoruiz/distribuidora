from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config/local.py')

csrf = CSRFProtect()
db = SQLAlchemy()

from apps.intranet.views import *
from apps.intranet.models import *

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
