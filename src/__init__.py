
from flask import Flask

from src import views
from src.db import DbSetup


with open('src/version.txt') as f:
    __version__ = f.read()


def main():
    app = Flask(__name__)

    app.register_blueprint(views.bp)

    DbSetup.auto_init()

    return app
