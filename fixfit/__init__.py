from flask.ext.jwt import JWT
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from flask import Flask

from fixfit.config import config

import pkgutil
import importlib

db = SQLAlchemy()
auth = HTTPBasicAuth()
jwt = JWT()

PATH = 'fixfit/api/v1'
BLUEPRINT = 'bp'
V1_URL_PREFIX = '/api/v1'

def register_blueprints(app, path, blueprint_attribute):
    modules = pkgutil.iter_modules(path=[path])
    package_name = PATH.replace('/', '.')

    for m in modules:
        mod = importlib.import_module('{}.{}'.format(package_name, m[1]))
        app.register_blueprint(getattr(mod, blueprint_attribute), url_prefix=V1_URL_PREFIX)

def create_application(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    jwt.init_app(app)
    register_blueprints(app, PATH, BLUEPRINT)
    return app
