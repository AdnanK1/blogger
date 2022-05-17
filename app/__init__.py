from flask import Flask
from .main import views
from config import config_options
from .extensions import db,b_crypt,login_manager

def create_app(config_name):
    app = Flask(__name__)

    #Initializing flask extensions
    db.init_app(app)
    b_crypt.init_app(app)
    login_manager.init_app(app)
    
    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app