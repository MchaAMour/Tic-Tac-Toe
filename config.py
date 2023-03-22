import os

# basedir = os.path.dirname(os.path.relpath(__file__))
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///games.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


