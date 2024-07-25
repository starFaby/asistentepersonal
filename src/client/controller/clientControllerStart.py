from src.heart.heartSistem import *
from src.heart.heartUtil import *

class ClientControllerStart:

    def onGetClientControllerStart():
        text =  """
                Mis estimados clientes, le saluda el asistente personal de la doctora, Luz Estrella,
                en la que ella ofrece sus servicios de asuntos legales como: familia, civil, laboral, 
                actos notariales y penales, para seguridad de que la abogada se encuentra activa, el 
                carnet lo pueden visualizar en la pantalla principal y buscarle en el foro de abogados, 
                es un gusto atenderle y tenga un buen dia.
                """
        
        #onGetMultiProccessingVoz(text)
        onGetMultiProccessingAudioVoz(text)
        
        return render('index.html')
    
    def onGetClientControllerCarnet():
        context = {
            'vmcarnet': True
        }
        return render('index.html', **context)



