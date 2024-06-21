from src.heart.heartSistem import *
from src.config.config import *
from src.heart.heartRouter import *
from src.heart.heartController import *
from src.heart.heartMiddlewares import *

loginManager = LoginManager()
loginManager.loginView = 'auth.controller.authControllerUserLoginIn'



@loginManager.user_loader
def loadUser(pfsusersusername):
    return AuthMiddlewaresUserLoginIn.get(pfsusersusername)

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
    app.register_blueprint(arulgn)
    app.register_blueprint(araulgt)
    #----------Client----------
    app.register_blueprint(crs)

    return app