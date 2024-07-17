from src.heart.heartSistem import *
from src.heart.heartServices import *
class ClientControllerAsuntoLegal:
    def onGetClientControllerAsuntoLegalListView():
        try:
                asuntoLegal = ClientServiceAsuntoLegal.ongetClientServiceAsuntoLegal()
                context = {
                    'asuntoLegal':asuntoLegal
                }
                return render("client/clientAsuntoLegal.html", **context)
        except SQLAlchemyError as e:
                return render('errors/error500.html', e)