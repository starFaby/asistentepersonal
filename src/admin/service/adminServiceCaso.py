from src.heart.heartSistem import *
from src.heart.heartDatabase import *
from src.heart.heartModelos import *

class AdminServiceCaso:

    @classmethod
    def onGetAdminServiceCaso(self, page):
        try:
            page = page
            pages = 10
            casoList = Caso.query.order_by(Caso.pfsapcasoid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            
            return casoList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceCasoName(self, search, page):
        try:
            page = page
            pages = 10
            casoList = Caso.query.filter(Caso.pfsapcasonombre.like(search)).paginate(per_page=pages,error_out=False)
            return casoList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceAsuntoLegalList(self):
        try:
            asuntoLegalList = Asuntoslegal.query.all()
            return asuntoLegalList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceCasoSave(self, id, nombre, image, detalle, estado, createdat, asunlegal):
        modelCaso = AdminModelCasos(id,nombre,image,detalle,estado,createdat,asunlegal)
        newCaso = Caso(
            pfsapcasonombre = modelCaso.getnombre(),
            pfsapcasoimage = modelCaso.getimage(),
            pfsapcasodetalle = modelCaso.getdetalle(),
            pfsapcasoestado = modelCaso.getestado(),
            pfsapcasocreatedat = modelCaso.getcreatedat(),
            pfsapalid = modelCaso.getasunlegal()
        )
        if modelCaso.getnombre() != '' and modelCaso.getimage() != '' and modelCaso.getdetalle() != '' and modelCaso.getestado() != '' and modelCaso.getcreatedat() != '' and modelCaso.getasunlegal() != '' :
            db.session.add(newCaso)
            db.session.commit()
            return True
        else:
            return False

