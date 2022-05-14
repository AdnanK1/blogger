from flask import Flask
from .main import views

def create_app():
    app = Flask(__name__)

    return app