from src.heart.heartSistem import *


#----------------------------
#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='pfsusers'

    pfsusersid = db.Column(db.Integer, primary_key=True)
    pfsuserscedula = db.Column(db.String(80), nullable=False)
    pfsusersnombres = db.Column(db.String(80), nullable=False)
    pfsusersapellidos = db.Column(db.String(80), nullable=False)
    pfsusersusername = db.Column(db.String(30), nullable=False)
    pfsusersemail = db.Column(db.String(120), nullable=False)
    pfsuserspassword = db.Column(db.String(250), nullable=True)
    pfsusersdireccion = db.Column(db.String(100), nullable=True)
    pfsuserscellphone = db.Column(db.String(25), nullable=False)
    pfsusersphone = db.Column(db.String(20), nullable=False)
    pfsusersisadmin = db.Column(db.Boolean, default=False)
    pfsusersavatar = db.Column(db.String(250), nullable=True)
    pfsusersestado = db.Column(db.String(1), nullable=True)
    pfsuserscreatedat = db.Column(db.Date, nullable=True) 

    def onGetSetPassword(self, pfsuserspassword):
        self.pfsuserspassword = generate_password_hash(pfsuserspassword)

    def onGetCheckPassword(self, pfsuserspassword):
        return check_password_hash(self.pfsuserspassword, pfsuserspassword)

    def __init__(self, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion,  pfsuserscellphone, pfsusersphone, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat):
        self.pfsuserscedula = pfsuserscedula
        self.pfsusersnombres = pfsusersnombres
        self.pfsusersapellidos = pfsusersapellidos
        self.pfsusersusername = pfsusersusername
        self.pfsusersemail = pfsusersemail
        self.pfsuserspassword = pfsuserspassword 
        self.pfsusersdireccion = pfsusersdireccion 
        self.pfsuserscellphone = pfsuserscellphone
        self.pfsusersphone = pfsusersphone
        self.pfsusersavatar = pfsusersavatar
        self.pfsusersisadmin = pfsusersisadmin
        self.pfsusersestado = pfsusersestado
        self.pfsuserscreatedat = pfsuserscreatedat 

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsusersid', 'pfsuserscedula', 'pfsusersnombres', 'pfsusersapellidos', 'pfsusersusername', 'pfsusersemail', 'pfsuserspassword', 'pfsusersdireccion',  'pfsuserscellphone', 'pfsusersphone','pfsusersisadmin', 'pfsusersavatar', 'pfsusersestado', 'pfsuserscreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)




#-----------------------------------------------------------
#---------------ASUNTOS LEGALES----------------------------------
#----------------------------------------------------------

class Asuntoslegal(db.Model):
    __tablename__='pfsapasuntoslegales'

    pfsapalid = db.Column(db.Integer, primary_key=True)
    pfsapalnombre = db.Column(db.String(120), nullable=False)
    pfsapalimage = db.Column(db.String(300), nullable=False)
    pfsapaldetalle = db.Column(db.String(300), nullable=False)
    pfsapalestado = db.Column(db.String(1), nullable=True)
    pfsapalcreatedat = db.Column(db.String(11), nullable=True) 


    def __init__(self, pfsapalnombre, pfsapalimage, pfsapaldetalle , pfsapalestado, pfsapalcreatedat):
        self.pfsapalnombre = pfsapalnombre
        self.pfsapalimage = pfsapalimage
        self.pfsapaldetalle = pfsapaldetalle
        self.pfsapalestado = pfsapalestado
        self.pfsapalcreatedat = pfsapalcreatedat

class AsuntoslegalSchema(ma.Schema):
    class Meta:
        fields = ('pfsapalid', 'pfsapalnombre', 'pfsapalimage', 'pfsapaldetalle' , 'pfsapalestado', 'pfsapalcreatedat')

asuntoslegalSchema = AsuntoslegalSchema()
asuntoslegalSchema = AsuntoslegalSchema(many=True)


#---------------------------
#------------ Caso----------
#--------------------------

class Caso(db.Model):
    __tablename__='pfsapcasos'

    pfsapcasoid = db.Column(db.Integer, primary_key=True)
    pfsapcasonombre = db.Column(db.String(80), nullable=False)
    pfsapcasoimage = db.Column(db.String(300), nullable=False)
    pfsapcasodetalle = db.Column(db.String(500), nullable=False)
    pfsapcasoestado = db.Column(db.String(1), nullable=True)
    pfsapcasocreatedat = db.Column(db.String(15), nullable=True) 

    pfsapasislegid = db.Column(db.Integer, db.ForeignKey('pfsapasuntoslegales.pfsapalid',ondelete='CASCADE'), nullable=False)
    pfsapasisleg = db.relationship('Asuntoslegal',backref=db.backref('pfsapcasos',lazy=True))


    def __init__(self, pfsapcasonombre, pfsapcasoimage, pfsapcasodetalle, pfsapcasoestado, pfsapcasocreatedat, pfsapabogadogid, pfsapasislegid):
        self.pfsapcasonombre = pfsapcasonombre
        self.pfsapcasoimage = pfsapcasoimage
        self.pfsapcasodetalle = pfsapcasodetalle
        self.pfsapcasoestado = pfsapcasoestado
        self.pfsapcasocreatedat = pfsapcasocreatedat
        self.pfsapabogadogid = pfsapabogadogid
        self.pfsapasislegid = pfsapasislegid


class CasoSchema(ma.Schema):
    class Meta:
        fields = ( 'pfsapcasoid', 'pfsapalnombre', 'pfsapalimage', 'pfsapaldetalle', 'pfsapalestado', 'pfsapalcreatedat', 'pfsapabgid', 'pfsapalid')

casoSchema = CasoSchema()
casoSchema = CasoSchema(many=True)

