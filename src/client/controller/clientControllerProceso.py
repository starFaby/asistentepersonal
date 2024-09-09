from src.heart.heartSistem import *
from src.heart.heartServices import *
class ClientControllerProceso:
    def onGetClientControllerProcesoListView(id):
        try:
                procesoList = ClientServiceProceso.ongetClientServiceProceso(id)
                context = {
                    'procesoList':procesoList
                }
                return render("client/clientProceso.html", **context)
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)