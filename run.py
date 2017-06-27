from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import *


app = Flask(__name__)
app.config.from_pyfile('config/local.py')

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(port=8000)
