from logging.config import fileConfig
import os
import click
import sys

from flask import Flask
from flask.cli import with_appcontext

from app.extensions import db
from app.blueprints.home.views import main
from app.blueprints.manager.views import manager
from config import config


@click.command(name='test')
@with_appcontext
def test():
    """
    This function run test from shell by command:
    'flask test'
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    db.create_all()
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    ret = not results.wasSuccessful()
    sys.exit(ret)


def create_app(config_name: str):
    app = Flask(__name__, static_folder='/static')
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    # Setting up loggers
    fileConfig('logging.cfg')

    print('#' * 30, db, app.config)
    # Initialize database
    
    db.init_app(app)
    print('#' * 30, db)
    
    # register blueprint
    app.register_blueprint(main)
    app.register_blueprint(manager)

    
    return app