from src.heart.heartSistem import *

#----------------------------
#----------ADMIN----------
#--------------------------

class Admin(db.Model):
    __tablename__='pfsadmins'

    pfsadminid = db.Column(db.Integer, primary_key=True)
    pfsadmincedula = db.Column(db.String(80), nullable=False)
    pfsadminnombres = db.Column(db.String(80), nullable=False)
    pfsadminapellidos = db.Column(db.String(80), nullable=False)
    pfsadminusername = db.Column(db.String(30), nullable=False)
    pfsadminemail = db.Column(db.String(120), nullable=False)
    pfsadminpassword = db.Column(db.String(250), nullable=True)
    pfsadmindireccion = db.Column(db.String(100), nullable=True)
    pfsadmincellphone = db.Column(db.String(25), nullable=False)
    pfsadminphone = db.Column(db.String(20), nullable=False)
    pfsadminisadmin = db.Column(db.Boolean, default=False)
    pfsadminavatar = db.Column(db.String(250), nullable=True)
    pfsadminestado = db.Column(db.String(1), nullable=True)
    pfsadmincreatedat = db.Column(db.Date, nullable=True) 

    def onGetSetPassword(self, pfsadminpassword):
        self.pfsadminpassword = generate_password_hash(pfsadminpassword)

    def onGetCheckPassword(self, pfsadminpassword):
        return check_password_hash(self.pfsadminpassword, pfsadminpassword)

    def __init__(self, pfsadmincedula, pfsadminnombres, pfsadminapellidos, pfsadminusername, pfsadminemail, pfsadminpassword, pfsadmindireccion,  pfsadmincellphone, pfsadminphone, pfsadminisadmin, pfsadminavatar, pfsadminestado, pfsadmincreatedat):
        
        self.pfsadmincedula = pfsadmincedula
        self.pfsadminnombres = pfsadminnombres
        self.pfsadminapellidos = pfsadminapellidos
        self.pfsadminusername = pfsadminusername
        self.pfsadminemail = pfsadminemail
        self.pfsadminpassword = pfsadminpassword 
        self.pfsadmindireccion = pfsadmindireccion 
        self.pfsadmincellphone = pfsadmincellphone
        self.pfsadminphone = pfsadminphone
        self.pfsadminisadmin = pfsadminisadmin
        self.pfsadminavatar = pfsadminavatar
        self.pfsadminestado = pfsadminestado
        self.pfsadmincreatedat = pfsadmincreatedat

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('pfsadminid', 'pfsadmincedula', 'pfsadminnombres', 'pfsadminapellidos', 'pfsadminusername', 'pfsadminemail', 'pfsadminpassword', 'pfsadmindireccion',  'pfsadmincellphone', 'pfsadminphone', 'pfsadminisadmin', 'pfsadminavatar', 'pfsadminestado', 'pfsadmincreatedat')

adminSchema = AdminSchema()
adminSchema = AdminSchema(many=True)



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


    pfsadminid = db.Column(db.Integer, db.ForeignKey('pfsadmins.pfsadminid',ondelete='CASCADE'), nullable=False)
    pfsadmin = db.relationship('Admin',backref=db.backref('pfsusers',lazy=True))


    def onGetSetPassword(self, pfsuserspassword):
        self.pfsuserspassword = generate_password_hash(pfsuserspassword)

    def onGetCheckPassword(self, pfsuserspassword):
        return check_password_hash(self.pfsuserspassword, pfsuserspassword)

    def __init__(self, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion,  pfsuserscellphone, pfsusersphone, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat, pfsadminid):
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
        self.pfsadminid = pfsadminid 

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsusersid', 'pfsuserscedula', 'pfsusersnombres', 'pfsusersapellidos', 'pfsusersusername', 'pfsusersemail', 'pfsuserspassword', 'pfsusersdireccion',  'pfsuserscellphone', 'pfsusersphone', 'pfsusersisadmin', 'pfsusersavatar', 'pfsusersestado', 'pfsuserscreatedat', 'pfsadminid')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)


#----------------------------
#----------Abogada-----------
#----------------------------

class Abogado(db.Model):
    __tablename__='pfsabogados'

    pfsabgsid = db.Column(db.Integer, primary_key=True)
    pfsabgsnombre = db.Column(db.String(100), nullable=False)
    pfsabgsdetalle = db.Column(db.String(200), nullable=False)
    pfsabgsavatar = db.Column(db.String(300), nullable=True)
    pfsabgsestado = db.Column(db.String(1), nullable=True)
    pfsabgscreatedat = db.Column(db.Date, nullable=True) 

    pfsadminid = db.Column(db.Integer, db.ForeignKey('pfsadmins.pfsadminid',ondelete='CASCADE'), nullable=False)
    pfsadmin = db.relationship('Admin',backref=db.backref('pfsabogados',lazy=True))


    def __init__(self, pfsabgsnombre, pfsabgsdetalle, pfsabgsavatar, pfsabgsestado, pfsabgscreatedat, pfsadminid):
        self.pfsabgsnombre = pfsabgsnombre
        self.pfsabgsdetalle = pfsabgsdetalle
        self.pfsabgsavatar = pfsabgsavatar
        self.pfsabgsestado = pfsabgsestado
        self.pfsabgscreatedat = pfsabgscreatedat 
        self.pfsadminid = pfsadminid 


class AbogadoSchema(ma.Schema):
    class Meta:
        fields = ('pfsabgsid', 'pfsabgsnombre', 'pfsabgsdetalle', 'pfsabgsavatar', 'pfsabgsestado', 'pfsabgscreatedat', 'pfsadminid')

abogadoSchema = AbogadoSchema()
abogadoSchema = AbogadoSchema(many=True)

