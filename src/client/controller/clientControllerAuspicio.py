from src.heart.heartSistem import *
from src.heart.heartServices import *
class ClientControllerAuspicio:
    def onGetClientControllerAuspicioView():
        try:
            return render("client/clientAuspicio.html")
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)
        
    def onGetClientControllerOnAuspicioModal():
        try:
            context = {
                    'verModal' : True,
            }
            return render("client/clientAuspicio.html", **context)
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)
    
    def onGetClientControllerOffAuspicioModal():
        try:
                return render("client/clientAuspicio.html")
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)
        