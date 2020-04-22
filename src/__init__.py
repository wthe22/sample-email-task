
from flask import Flask

from src import views


def main():
    app = Flask(__name__)

    app.register_blueprint(views.bp)

    return app
