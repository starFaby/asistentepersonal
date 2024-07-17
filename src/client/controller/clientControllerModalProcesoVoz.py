from src.heart.heartSistem import *
from src.heart.heartServices import *
from src.util.utilVoice import *
class ClientControllerModalProcesoVoz:
    def onGetClientControllerModalProcesoVoz(id):
        try:
                modProcVoz = ClientServiceModalProcesoVoz.ongetClientServiceModalProcesoVoz(id)
                assisVoz = ''
                for item in modProcVoz:
                    assisVoz = item.pfsaprcsdetalle
                print(type(assisVoz))
                onGetMultiProccessingVoz(assisVoz)
                procesoList = []
                context = {
                    'verModal' : True,
                    'procesoList': procesoList
                }
                return render("client/clientProceso.html", **context)
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)