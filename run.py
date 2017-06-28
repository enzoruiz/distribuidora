from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config/local.py')

db = SQLAlchemy()

from apps.intranet.views import *
from apps.intranet.models import *

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
