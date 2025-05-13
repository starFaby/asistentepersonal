from src.heart.heartSistem import *
from src.heart.heartDatabase import *
from src.heart.heartModelos import *

class ClientServiceComentario:
    @classmethod
    def onGetClientServiceComentario(self, id, comentario, email, estado, createdat, userId):

        modelComentario = ClientModelComentario(id, comentario, email, estado,createdat, userId)
        
        newComentario = Usercomentario(
            pfsapucomentario = modelComentario.getcomentario(),
            pfsapucemail = modelComentario.getemail(),
            pfsapucestado = modelComentario.getestado(),
            pfsapucreatedat = modelComentario.getcreatedat(),
            pfsusersid = modelComentario.getuserId()
        )
        if modelComentario.getcomentario() != '' and modelComentario.getemail() != '' and modelComentario.getestado() != '' and modelComentario.getcreatedat() != '' and modelComentario.getuserId():
            db.session.add(newComentario)
            db.session.commit()
            return True
        else:
            return False