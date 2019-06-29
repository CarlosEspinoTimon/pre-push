import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # SECRET_KEY = os.urandom(12)
    SECRET_KEY = 'supersecretkey'
    DEBUG = False
    TESTING = False
    uri = 'mysql+pymysql://root:root_super_password@10.3.0.102/app_db'
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'


class Prod(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


class Dev(Config):
    DEBUG = True
    CORS_HEADERS = 'Content-Type'
    CORS_RESOURCES = {r"/*": {"origins": "*"}}


class Test(Config):
    TESTING = True
    uri = 'mysql+pymysql://root:root_super_password@10.3.0.103/test_db'
    SQLALCHEMY_DATABASE_URI = uri
