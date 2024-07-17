from src.heart.heartDatabase import *
from src.heart.heartSistem import *
class ClientServiceModalProcesoVoz:
    
    @classmethod
    def ongetClientServiceModalProcesoVoz(self, id):
        try:
            modProcVoz = Proceso.query.filter(Proceso.pfsaprcsestado == 1).filter(Proceso.pfsaprcsid == id)
            return modProcVoz
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)