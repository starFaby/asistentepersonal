from flask import Flask
from flask_bootstrap import Bootstrap
#Admin - Auth - Client
#Admin - Auth - Client
#Admin - Auth - Client
from src.heart.heartRouter import *


def apprun():
    #----------Sistem---------
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    #----------Admin----------
    #----------Auth----------
    #----------Client----------
    app.register_blueprint(crs)

    return app