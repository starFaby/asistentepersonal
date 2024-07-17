from src.heart.heartSistem import *
from src.heart.heartServices import *
class ClientControllerCaso:
    def onGetClientControllerCasoListView(id):
        try:
                casoList = ClientServiceCaso.ongetClientServiceCaso(id)
                context = {
                    'casoList':casoList
                }
                return render("client/clientCaso.html", **context)
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)