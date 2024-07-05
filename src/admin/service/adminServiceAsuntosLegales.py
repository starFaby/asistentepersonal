from src.heart.heartSistem import *
from src.heart.heartDatabase import *
from src.heart.heartModelos import *

class AdminServiceAsuntosLegales:

    @classmethod
    def onGetAdminServiceAsuntosLegales(self, page):
        try:
            page = page
            pages = 10
            userList = Asuntoslegal.query.order_by(Asuntoslegal.pfsapalid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            
            return userList
        except SQLAlchemyError as e:
            print("Error en Service Asunto Legal ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceAsuntosLegalesName(self, search, page):
        try:
            page = page
            pages = 10
            userList = Asuntoslegal.query.filter(Asuntoslegal.pfsapalnombre.like(search)).paginate(per_page=pages,error_out=False)
            return userList
        except SQLAlchemyError as e:
            print("Error en Service  Asunto Legal ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceAsuntoLegalSave(self, id, nombre, image, detalle, estado, createdat):
        modelAsuntoLegal = AdminModelAsuntoLegal(id, nombre, image, detalle, estado, createdat)
        newAsuntoLegal = Asuntoslegal(  pfsapalnombre = modelAsuntoLegal.getnombre(),
                                        pfsapalimage = modelAsuntoLegal.getimage(),
                                        pfsapaldetalle = modelAsuntoLegal.getdetalle(),
                                        pfsapalestado = modelAsuntoLegal.getestado(),
                                        pfsapalcreatedat = modelAsuntoLegal.getcreatedat())
        if modelAsuntoLegal.getnombre() != '' and  modelAsuntoLegal.getimage() != '' and modelAsuntoLegal.getdetalle() != '' and modelAsuntoLegal.getestado() != '' and modelAsuntoLegal.getcreatedat() != '' :
            db.session.add(newAsuntoLegal)
            db.session.commit()
            return True
        else:
            return False