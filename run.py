"""
Run file.
Create app passing config name that's placed in 
system environment variable FLASK_CONFIG.
"""
import os
from logging.config import fileConfig

from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict()


