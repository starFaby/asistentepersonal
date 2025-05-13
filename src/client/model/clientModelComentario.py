class ClientModelComentario():

    def __init__(self, id , comentario, email, estado, createdat, userId):
        self.id = id
        self.comentario = comentario
        self.email = email
        self.estado = estado
        self.createdat = createdat 
        self.userId = userId 
    
        
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
    # get y set comentario
    #---------------------
    #---------------------
    def getcomentario(self):
        return self.comentario
    
    def setcomentario(self, comentario):
        self.comentario = comentario

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
    def getuserId(self):
        return self.userId
    
    def setuserId(self, userId):
        self.userId = userId



    #------------------------
    #------------------------
    #Comentario en Json
    #------------------------
    #------------------------
    def ComentarioInJason(self):
        
        return {
            'id' : self.id,
            'comentario' : self.comentario,
            'email' : self.email,
            'estado' : self.estado,
            'createdat' : self.createdat,
            'userId' : self.userId
        }
        

        