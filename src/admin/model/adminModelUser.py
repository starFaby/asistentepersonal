class AdminModelUser():

    def __init__(self, id, cedula , nombres, apellidos, username, email, password, direccion, celular, telefono, isadmin, avatar, estado, createdAt):
        self.id = id
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.username = username
        self.email = email
        self.password = password
        self.direccion = direccion
        self.celular = celular
        self.telefono = telefono
        self.isadmin = isadmin
        self.avatar = avatar
        self.estado = estado
        self.createdAt = createdAt 
    
        
    #--------------------
    #--------------------
    # get y set id
    #---------------------
    #---------------------
    def getid(self):
        return self.id
    
    def setid(self, id):
        self.id = id

    #--------------------
    #--------------------
    # get y set cedula
    #---------------------
    #---------------------
    def getcedula(self):
        return self.cedula
    
    def setcedula(self, cedula):
        self.cedula = cedula

    #--------------------
    #--------------------
    # get y set nombres
    #---------------------
    #---------------------
    def getnombres(self):
        return self.nombres
    
    def setnombres(self, nombres):
        self.nombres = nombres

    #--------------------
    #--------------------
    # get y set apellidos
    #---------------------
    #---------------------
    def getapellidos(self):
        return self.apellidos
    
    def setapellidos(self, apellidos):
        self.apellidos = apellidos

    #--------------------
    #--------------------
    # get y set username
    #---------------------
    #---------------------
    def getusername(self):
        return self.username
    
    def setusername(self, username):
        self.username = username


    #--------------------
    #--------------------
    # get y set email
    #---------------------
    #---------------------
    def getemail(self):
        return self.email
    
    def setemail(self, email):
        self.email = email

    #--------------------
    #--------------------
    # get y set password
    #---------------------
    #---------------------
    def getpassword(self):
        return self.password
    
    def setpassword(self, password):
        self.password = password

    #--------------------
    #--------------------
    # get y set direccion
    #---------------------
    #---------------------
    def getdireccion(self):
        return self.direccion
    
    def setdireccion(self, direccion):
        self.direccion = direccion

    #--------------------
    #--------------------
    # get y set celular
    #---------------------
    #---------------------
    def getcelular(self):
        return self.celular
    
    def setcelular(self, celular):
        self.celular = celular

    #--------------------
    #--------------------
    # get y set telefono
    #---------------------
    #---------------------
    def getelefono(self):
        return self.telefono
    
    def setelefono(self, telefono):
        self.telefono = telefono


    #--------------------
    #--------------------
    # get y set isadmin
    #---------------------
    #---------------------
    def getisadmin(self):
        return self.isadmin
    
    def setisadmin(self, isadmin):
        self.isadmin = isadmin


    #--------------------
    #--------------------
    # get y set avatar
    #---------------------
    #---------------------
    def getavatar(self):
        return self.avatar
    
    def setavatar(self, avatar):
        self.avatar = avatar


    #--------------------
    #--------------------
    # get y set estado
    #---------------------
    #---------------------
    def getestado(self):
        return self.estado
    
    def setestado(self, estado):
        self.estado = estado

    #--------------------
    #--------------------
    # get y set createdAt
    #---------------------
    #---------------------
    def getcreatedat(self):
        return self.createdAt
    
    def setcreatedat(self, createdAt):
        self.createdAt = createdAt

    #--------------------
    #--------------------
    # get y set Json
    #---------------------
    #---------------------
    def ProductoMarketingInJason(self):
        
        return {
            'id' : self.id,
            'cedula' : self.cedula,
            'nombres' : self.nombres,
            'apellidos' : self.apellidos,
            'username' : self.username,
            'email' : self.email,
            'password' : self.password,
            'direccion' : self.direccion,
            'celular' : self.celular,
            'telefono' : self.telefono,
            'isadmin' : self.isadmin,
            'avatar' : self.avatar,
            'estado' : self.estado,
            'createdAt' : self.createdAt,
        }