import os

DEBUG = False
SECRET_KEY = os.environ.get('secret_key_distribuidora')

ENGINE = ''
USER = ''
PASSWORD = ''
HOST = ''
PORT = ''
NAME = ''
SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s:%s/%s' % (
                            ENGINE, USER, PASSWORD, HOST, PORT, NAME
                        )
SQLALCHEMY_TRACK_MODIFICATIONS = False
