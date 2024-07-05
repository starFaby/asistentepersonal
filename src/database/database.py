from src.heart.heartSistem import *

#----------------------------
#----------ROL----------
#--------------------------
class Rol(db.Model):

    __tablename__='pfsroles'
    
    pfsaprolid =  db.Column(db.Integer, primary_key=True)
    pfsaprolnombre = db.Column(db.String(30), nullable=False)
    pfsaproldetalle = db.Column(db.String(30), nullable=False)
    pfsaprolestado = db.Column(db.String(30), nullable=False)
    pfsaprolcreatedat = db.Column(db.Date, nullable=True) 

    def __init__(self, pfsaprolnombre, pfsaproldetalle, pfsaprolestado, pfsaprolcreatedat):
        self.pfsaprolnombre = pfsaprolnombre
        self.pfsaproldetalle = pfsaproldetalle
        self.pfsaprolestado = pfsaprolestado
        self.pfsaprolcreatedat = pfsaprolcreatedat

class RolSchema(ma.Schema):
    class Meta:
        fields = ('pfsaprolid', 'pfsaprolnombre', 'pfsaproldetalle', 'pfsaprolestado', 'pfsaprolcreatedat')

rolSchema = RolSchema()
rolSchema = RolSchema(many=True)

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
    pfsuserscelular = db.Column(db.String(25), nullable=False)
    pfsuserstelefono = db.Column(db.String(20), nullable=False)
    pfsusersisadmin = db.Column(db.Boolean, default=False)
    pfsusersavatar = db.Column(db.String(250), nullable=True)
    pfsusersestado = db.Column(db.String(1), nullable=True)
    pfsuserscreatedat = db.Column(db.Date, nullable=True) 

    #pfsaprolid = db.Column(db.Integer, db.ForeignKey('pfsroles.pfsaprolid',ondelete='CASCADE'), nullable=False)
    #pfsaprol = db.relationship('Rol',backref=db.backref('pfsusers',lazy=True))

    def onGetSetPassword(self, pfsuserspassword):
        self.pfsuserspassword = generate_password_hash(pfsuserspassword)

    def onGetCheckPassword(self, pfsuserspassword):
        return check_password_hash(self.pfsuserspassword, pfsuserspassword)

    def __init__(self, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion,  pfsuserscelular, pfsuserstelefono, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat):
        self.pfsuserscedula = pfsuserscedula
        self.pfsusersnombres = pfsusersnombres
        self.pfsusersapellidos = pfsusersapellidos
        self.pfsusersusername = pfsusersusername
        self.pfsusersemail = pfsusersemail
        self.pfsuserspassword = pfsuserspassword 
        self.pfsusersdireccion = pfsusersdireccion 
        self.pfsuserscelular = pfsuserscelular
        self.pfsuserstelefono = pfsuserstelefono
        self.pfsusersavatar = pfsusersavatar
        self.pfsusersisadmin = pfsusersisadmin
        self.pfsusersestado = pfsusersestado
        self.pfsuserscreatedat = pfsuserscreatedat 
    
    

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsusersid', 'pfsuserscedula', 'pfsusersnombres', 'pfsusersapellidos', 'pfsusersusername', 'pfsusersemail', 'pfsuserspassword', 'pfsusersdireccion',  'pfsuserscelular', 'pfsuserstelefono','pfsusersisadmin', 'pfsusersavatar', 'pfsusersestado', 'pfsuserscreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)


#-----------------------------------------------------------
#--------------------USERCASO-------------------------------
#----------------------------------------------------------

class Userproceso(db.Model):
    __tablename__='pfsapuserproceso'

    pfsapupid = db.Column(db.Integer, primary_key=True)
    pfsapupestado = db.Column(db.String(1), nullable=True)
    pfsapupreatedat = db.Column(db.String(11), nullable=True) 


    pfsaprcsid = db.Column(db.Integer, db.ForeignKey('pfsaproceso.pfsaprcsid',ondelete='CASCADE'), nullable=False)
    pfsaprcs = db.relationship('Proceso',backref=db.backref('pfsapuserproceso',lazy=True))

    pfsusersid = db.Column(db.Integer, db.ForeignKey('pfsusers.pfsusersid',ondelete='CASCADE'), nullable=False)
    pfsusers = db.relationship('User',backref=db.backref('pfsapuserproceso',lazy=True))

    def __init__(self, pfsapupestado, pfsapupreatedat, pfsaprcsid, pfsusersid):
        self.pfsapupestado = pfsapupestado
        self.pfsapupreatedat = pfsapupreatedat
        self.pfsaprcsid = pfsaprcsid
        self.pfsusersid = pfsusersid

class UsercasoSchema(ma.Schema):
    class Meta:
        fields = ('pfsapupid', 'pfsapupestado', 'pfsapupreatedat', 'pfsaprcsid' , 'pfsusersid')

usercasoSchema = UsercasoSchema()
usercasoSchema = UsercasoSchema(many=True)

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

    pfsapalid = db.Column(db.Integer, db.ForeignKey('pfsapasuntoslegales.pfsapalid',ondelete='CASCADE'), nullable=False)
    pfsapal = db.relationship('Asuntoslegal',backref=db.backref('pfsapcasos',lazy=True))


    def __init__(self, pfsapcasonombre, pfsapcasoimage, pfsapcasodetalle, pfsapcasoestado, pfsapcasocreatedat, pfsapalid):
        self.pfsapcasonombre = pfsapcasonombre
        self.pfsapcasoimage = pfsapcasoimage
        self.pfsapcasodetalle = pfsapcasodetalle
        self.pfsapcasoestado = pfsapcasoestado
        self.pfsapcasocreatedat = pfsapcasocreatedat
        self.pfsapalid = pfsapalid


class CasoSchema(ma.Schema):
    class Meta:
        fields = ( 'pfsapcasoid', 'pfsapcasonombre', 'pfsapcasoimage', 'pfsapcasodetalle', 'pfsapcasoestado', 'pfsapcasocreatedat', 'pfsapalid')

casoSchema = CasoSchema()
casoSchema = CasoSchema(many=True)



#-------------------------------
#------------ PROCESO ----------
#-------------------------------

class Proceso(db.Model):
    __tablename__='pfsaproceso'

    pfsaprcsid = db.Column(db.Integer, primary_key=True)
    pfsaprcsnombre = db.Column(db.String(80), nullable=False)
    pfsaprcsdetalle = db.Column(db.String(500), nullable=False)
    pfsaprcsestado = db.Column(db.String(1), nullable=True)
    pfsaprcscreatedat = db.Column(db.String(15), nullable=True) 

    pfsapcasoid = db.Column(db.Integer, db.ForeignKey('pfsapcasos.pfsapcasoid',ondelete='CASCADE'), nullable=False)
    pfsapcaso = db.relationship('Caso',backref=db.backref('pfsaproceso',lazy=True))


    def __init__(self, pfsaprcsnombre, pfsaprcsdetalle, pfsaprcsestado, pfsaprcscreatedat, pfsapcasoid):
        self.pfsaprcsnombre = pfsaprcsnombre
        self.pfsaprcsdetalle = pfsaprcsdetalle
        self.pfsaprcsestado = pfsaprcsestado
        self.pfsaprcscreatedat = pfsaprcscreatedat
        self.pfsapcasoid = pfsapcasoid


class ProcesoSchema(ma.Schema):
    class Meta:
        fields = ( 'pfsaprcsid', 'pfsaprcsnombre', 'pfsaprcsdetalle', 'pfsaprcsestado', 'pfsaprcscreatedat', 'pfsapcasoid')

procesoSchema = ProcesoSchema()
procesoSchema = ProcesoSchema(many=True)



#---------------------------
#------------ Premio----------
#--------------------------

class Premio(db.Model):
    __tablename__='pfsapremios'

    pfsapremioid = db.Column(db.Integer, primary_key=True)
    pfsapremionombre = db.Column(db.String(80), nullable=False)
    pfsapremioimage = db.Column(db.String(300), nullable=False)
    pfsapremiodetalle = db.Column(db.String(500), nullable=False)
    pfsapremioestado = db.Column(db.String(1), nullable=True)
    pfsapremiocreatedat = db.Column(db.String(15), nullable=True) 


    def __init__(self, pfsapremionombre, pfsapremioimage, pfsapremiodetalle, pfsapremioestado, pfsapremiocreatedat):
        self.pfsapremionombre = pfsapremionombre
        self.pfsapremioimage = pfsapremioimage
        self.pfsapremiodetalle = pfsapremiodetalle
        self.pfsapremioestado = pfsapremioestado
        self.pfsapremiocreatedat = pfsapremiocreatedat


class PremioSchema(ma.Schema):
    class Meta:
        fields = ( 'pfsapremioid', 'pfsapremionombre', 'pfsapremioimage', 'pfsapremiodetalle', 'pfsapremioestado', 'pfsapremiocreatedat')

premioSchema = PremioSchema()
premioSchema = PremioSchema(many=True)



#---------------------------
#------------ Sorteo ----------
#--------------------------

class Sorteo(db.Model):
    __tablename__='pfsapsorteo'

    pfsapsorteoid = db.Column(db.Integer, primary_key=True)
    pfsapsorteonombre = db.Column(db.String(80), nullable=False)
    pfsapsorteodetalle = db.Column(db.String(500), nullable=False)
    pfsapsorteoestado = db.Column(db.String(1), nullable=True)
    pfsapsorteocreatedat = db.Column(db.String(15), nullable=True) 

    pfsapuserid = db.Column(db.Integer, db.ForeignKey('pfsusers.pfsusersid',ondelete='CASCADE'), nullable=False)
    pfsapuser = db.relationship('User',backref=db.backref('pfsapsorteo',lazy=True))

    pfsapremioid = db.Column(db.Integer, db.ForeignKey('pfsapremios.pfsapremioid',ondelete='CASCADE'), nullable=False)
    pfsapremio = db.relationship('Premio',backref=db.backref('pfsapsorteo',lazy=True))



    def __init__(self, pfsapsorteonombre, pfsapsorteodetalle, pfsapsorteoestado, pfsapsorteocreatedat, pfsapuserid, pfsapremioid):
        self.pfsapsorteonombre = pfsapsorteonombre
        self.pfsapsorteodetalle = pfsapsorteodetalle
        self.pfsapsorteoestado = pfsapsorteoestado
        self.pfsapsorteocreatedat = pfsapsorteocreatedat
        self.pfsapuserid = pfsapuserid
        self.pfsapremioid = pfsapremioid


class SorteoSchema(ma.Schema):
    class Meta:
        fields = ( 'pfsapsorteoid', 'pfsapsorteonombre', 'pfsapsorteodetalle', 'pfsapsorteoestado', 'pfsapsorteocreatedat', 'pfsapuserid', 'pfsapremioid')

sorteoSchema = SorteoSchema()
sorteoSchema = SorteoSchema(many=True)




