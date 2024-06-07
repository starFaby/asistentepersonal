from src.heart.heartSistem import *
from src.config.config import *
from src.heart.heartRouter import *
from src.heart.heartController import *

loginManager = LoginManager()
loginManager.loginView = 'auth.controller.controllerLoginIn'

@loginManager.user_loader
def loadUser(username):
    return UserModel.get(username)

def apprun():
    #----------Sistem---------
    app = Flask(__name__)
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)
    db.init_app(app)
    ma.init_app(app)
    loginManager.init_app(app)
    #----------Admin----------
    #----------Auth----------
    app.register_blueprint(ardbm)
    #----------Client----------
    app.register_blueprint(crs)

    return app