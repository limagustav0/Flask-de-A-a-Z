from flask import Flask
from config import app_active, app_config

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates ')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    @app.route('/')
    def index():
        return 'Hello world'
    
    return app
    