from src.heart.heartDatabase import *

class ClientServiceCaso:
    
    @classmethod
    def ongetClientServiceCaso(self, id):
        try:
            casoList = pd.Series(Caso.query.filter(Caso.pfsapcasoestado == 1).filter(Caso.pfsapalid == id))
            return casoList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)