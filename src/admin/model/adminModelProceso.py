class AdminModelProceso():

    def __init__(self, id , nombre, detalle, estado, createdat, casoId):
        self.id = id
        self.nombre = nombre
        self.detalle = detalle
        self.estado = estado
        self.createdat = createdat 
        self.casoId = casoId 
    
        
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
    # get y set casoId
    #---------------------
    #---------------------
    def getcasoId(self):
        return self.casoId
    
    def setcasoId(self, casoId):
        self.casoId = casoId



    #------------------------
    #------------------------
    #Asuntos Legales en Json
    #------------------------
    #------------------------
    def AsuntosLegaesInJason(self):
        
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'detalle' : self.detalle,
            'estado' : self.estado,
            'createdat' : self.createdat,
            'casoId' : self.casoId
        }

        