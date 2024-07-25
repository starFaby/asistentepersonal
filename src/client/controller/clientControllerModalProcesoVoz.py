from src.heart.heartSistem import *
from src.heart.heartServices import *
from src.heart.heartUtil import *
class ClientControllerModalProcesoVoz:
    def onGetClientControllerModalProceso(id):
        try:
            modProcVoz = ClientServiceModalProcesoVoz.ongetClientServiceModalProcesoVoz(id)
            for item in modProcVoz:
                print(item.pfsaprcsid)
            procesoList = []
            context = {
                    'verModal' : True,
                    'procesoList' : procesoList,
                    'modProcVoz' : modProcVoz
            }
            return render("client/clientProceso.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    
    def onGetClientControllerModalProcesoVoz(id):
        try:
                modProcVoz = ClientServiceModalProcesoVoz.ongetClientServiceModalProcesoVoz(id)
                assisVoz = ''
                idAux = 0
                for item in modProcVoz:
                    assisVoz = item.pfsaprcsdetalle
                    idAux = item.pfsapcasoid
                print('type(assisVoz)')
                print(type(assisVoz))
                print('type(assisVoz)')
                onGetMultiProccessingAudioVoz(assisVoz)
                return redirect(url_for('crp.onGetClientControllerProcesoListView', id=idAux))
        #return redirect(url_for(crp.onGetClientControllerProcesoListView', id=item.pfsapcasoid))) 
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)