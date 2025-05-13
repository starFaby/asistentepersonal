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
    app.register_blueprint(aru)
    app.register_blueprint(aral)
    app.register_blueprint(arc)
    app.register_blueprint(arp)
    #----------Auth----------
    app.register_blueprint(ardbm)
    app.register_blueprint(arulgn)
    app.register_blueprint(araulgt)
    #----------Client----------
    app.register_blueprint(crs)
    app.register_blueprint(cral)
    app.register_blueprint(crc)
    app.register_blueprint(crp)
    app.register_blueprint(crmpv)
    app.register_blueprint(cra)
    app.register_blueprint(crcmt)

    return app