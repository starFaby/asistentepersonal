from src.heart.heartSistem import *
#----------------------------
#----------Abogada----------
#--------------------------

class Abogado(db.Model):
    __tablename__='pfsabogados'

    pfsabgsid = db.Column(db.Integer, primary_key=True)
    pfsabgsnombre = db.Column(db.String(100), nullable=False)
    pfsabgsdetalle = db.Column(db.String(200), nullable=False)
    pfsabgsavatar = db.Column(db.String(300), nullable=True)
    pfsabgsestado = db.Column(db.String(1), nullable=True)
    pfsabgscreatedat = db.Column(db.Date, nullable=True) 

    def __init__(self, pfsabgsnombre, pfsabgsdetalle, pfsabgsavatar, pfsabgsestado, pfsabgscreatedat):
        self.pfsabgsnombre = pfsabgsnombre
        self.pfsabgsdetalle = pfsabgsdetalle
        self.pfsabgsavatar = pfsabgsavatar
        self.pfsabgsestado = pfsabgsestado
        self.pfsabgscreatedat = pfsabgscreatedat


class AbogadoSchema(ma.Schema):
    class Meta:
        fields = ('pfsabgsid', 'pfsabgsnombre', 'pfsabgsdetalle', 'pfsabgsavatar', 'pfsabgsestado', 'pfsabgscreatedat')

abogadoSchema = AbogadoSchema()
abogadoSchema = AbogadoSchema(many=True)

#----------------------------
#----------usuario----------
#--------------------------

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
        self.pfsusersisadmin = pfsusersisadmin
        self.pfsusersavatar = pfsusersavatar
        self.pfsusersestado = pfsusersestado
        self.pfsuserscreatedat = pfsuserscreatedat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsusersid', 'pfsuserscedula', 'pfsusersnombres', 'pfsusersapellidos', 'pfsusersusername', 'pfsusersemail', 'pfsuserspassword', 'pfsusersdireccion',  'pfsuserscellphone', 'pfsusersphone', 'pfsusersisadmin', 'pfsusersavatar', 'pfsusersestado', 'pfsuserscreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

