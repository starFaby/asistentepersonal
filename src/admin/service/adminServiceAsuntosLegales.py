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
        
    @classmethod
    def onGetAdminSericeUserModalAsuntosLegalesUpdateView(self, id):
        asunlegdataOne = Asuntoslegal.query.filter(Asuntoslegal.pfsapalid == id).one_or_none()
        return asunlegdataOne
    

    @classmethod
    def onGetAdminServiceUserModalAsuntosLegalesUpdate(self, id, nombre, image, detalle, estado, createdat):
        modelAsuntoLegal = AdminModelAsuntoLegal(id, nombre, image, detalle, estado, createdat)
        asuntoLegal = Asuntoslegal.query.get(modelAsuntoLegal.getid())

        asuntoLegal.pfsapalnombre = modelAsuntoLegal.getnombre()
        asuntoLegal.pfsapalimage = modelAsuntoLegal.getimage()
        asuntoLegal.pfsapaldetalle = modelAsuntoLegal.getdetalle()
        asuntoLegal.pfsapalestado = modelAsuntoLegal.getestado()

        if modelAsuntoLegal.getnombre() != '' and  modelAsuntoLegal.getimage() != '' and modelAsuntoLegal.getdetalle() != '' and modelAsuntoLegal.getestado() != '' and modelAsuntoLegal.getcreatedat() != '' :
            db.session.commit()
            return True
        else:
            return False
        

    @classmethod
    def onGetAdminServiceAsuntosLegalesDelete(self, id):
        try:
            asuntolegal = Asuntoslegal.query.get(id)
            asuntolegal.pfsapalestado = 0
            if asuntolegal.pfsapalestado != '':
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)