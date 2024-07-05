class AdminModelCasos():

    def __init__(self, id , nombre, image, detalle, estado, createdat, asunlegal):
        self.id = id
        self.nombre = nombre
        self.image = image
        self.detalle = detalle
        self.estado = estado
        self.createdat = createdat 
        self.asunlegal = asunlegal 
    
        
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
    # get y set nombre
    #---------------------
    #---------------------
    def getnombre(self):
        return self.nombre
    
    def setnombre(self, nombre):
        self.nombre = nombre

    #--------------------
    #--------------------
    # get y set image
    #---------------------
    #---------------------
    def getimage(self):
        return self.image
    
    def setimage(self, image):
        self.image = image

    #--------------------
    #--------------------
    # get y set detalle
    #---------------------
    #---------------------
    def getdetalle(self):
        return self.detalle
    
    def setdetalle(self, detalle):
        self.detalle = detalle


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
    # get y set createdat
    #---------------------
    #---------------------
    def getcreatedat(self):
        return self.createdat
    
    def setcreatedat(self, createdat):
        self.createdat = createdat


    #--------------------
    #--------------------
    # get y set asunlegal
    #---------------------
    #---------------------
    def getasunlegal(self):
        return self.asunlegal
    
    def setasunlegal(self, asunlegal):
        self.asunlegal = asunlegal



    #------------------------
    #------------------------
    #Asuntos Legales en Json
    #------------------------
    #------------------------
    def AsuntosLegaesInJason(self):
        
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'image' : self.image,
            'detalle' : self.detalle,
            'estado' : self.estado,
            'createdat' : self.createdat,
            'asunlegal' : self.asunlegal
        }

        