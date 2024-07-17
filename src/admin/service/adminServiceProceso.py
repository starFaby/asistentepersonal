from src.heart.heartSistem import *
from src.heart.heartDatabase import *
from src.heart.heartModelos import *

class AdminServiceProceso:

    @classmethod
    def onGetAdminServiceProcesoListView(self, page):
        try:
            page = page
            pages = 10
            procesoList = Proceso.query.order_by(Proceso.pfsaprcsid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            
            return procesoList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceProcesoListNameView(self, search, page):
        try:
            page = page
            pages = 10
            procesoList = Proceso.query.filter(Proceso.pfsaprcsnombre.like(search)).paginate(per_page=pages,error_out=False)
            return procesoList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceCasoList(self):
        try:
            casoList = Caso.query.all()
            return casoList
        except SQLAlchemyError as e:
            print("Error en proceso para listar Caso ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceProcesoSave(self, id, nombre, detalle, estado, createdat, casoId):
        modelProceso = AdminModelProceso(id,nombre,detalle,estado,createdat,casoId)
        
        newProceso = Proceso(
            pfsaprcsnombre = modelProceso.getnombre(),
            pfsaprcsdetalle = modelProceso.getdetalle(),
            pfsaprcsestado = modelProceso.getestado(),
            pfsaprcscreatedat = modelProceso.getcreatedat(),
            pfsapcasoid = modelProceso.getcasoId()
        )
        if modelProceso.getnombre() != '' and modelProceso.getdetalle() != '' and modelProceso.getestado() != '' and modelProceso.getcreatedat() != '' and modelProceso.getcasoId() != '' :
            db.session.add(newProceso)
            db.session.commit()
            return True
        else:
            return False

