SECRET_KEY = 'gc\xd4u\x15\x7f\x9c\xb1o"\xe5\xdeO\x92{\xe1,\xf2\xce\xe8\nrc\x10'
DEBUG = True

ENGINE = 'postgresql'
USER = 'postgres'
PASSWORD = '123123'
HOST = 'localhost'
PORT = '5432'
NAME = 'distribuidoradb'
SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s:%s/%s' % (
                            ENGINE, USER, PASSWORD, HOST, PORT, NAME
                        )
SQLALCHEMY_TRACK_MODIFICATIONS = False

USE_SESSION_FOR_NEXT = True
