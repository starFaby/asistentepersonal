from src.heart.heartDatabase import *
from src.heart.heartSistem import *
class ClientServiceProceso:
    
    @classmethod
    def ongetClientServiceProceso(self, id):
        try:
            procesoList = Proceso.query.filter(Proceso.pfsaprcsestado == 1).filter(Proceso.pfsapcasoid == id)
            return procesoList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)