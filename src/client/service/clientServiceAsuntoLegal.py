from src.heart.heartDatabase import *
class ClientServiceAsuntoLegal:
    
    @classmethod
    def ongetClientServiceAsuntoLegal(self):
        try:
            asuntoLegalList = Asuntoslegal.query.filter(Asuntoslegal.pfsapalestado == 1)
            return asuntoLegalList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)