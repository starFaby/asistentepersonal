from src.heart.heartController import *
from src.util.utilVoice import *

class ClientControllerStart:

    def onGetClientControllerStart():
        text = "Buenos diaz Caballero, este es tu asistente personal para cualquier duda navegue en la parte de la navegacion para las consultas"
        onGetMultiProccessingVoz(text)
        return render('index.html')
    
    def onGetClientControllerCarnet():
        context = {
            'vmcarnet': True
        }
        return render('index.html', **context)



