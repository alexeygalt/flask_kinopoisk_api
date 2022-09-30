import os, sys

path = os.path.abspath('')
sys.path.insert(1, path)

from project.config import DevelopmentConfig

from project.server import create_app
from project.setup_db import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()