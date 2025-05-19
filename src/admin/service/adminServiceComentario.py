from src.heart.heartSistem import *
from src.heart.heartDatabase import *
from src.heart.heartModelos import *

class AdminServiceComentario:

    @classmethod
    def onGetAdminServiceComentarioListView(self, page):
        try:
            page = page
            pages = 10
            comentarioList = Usercomentario.query.order_by(Usercomentario.pfsapucid.asc()).filter(Usercomentario.pfsapucestado == 1).paginate(page=page, per_page=pages ,error_out=False)
            return comentarioList
        
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def onGetAdminServiceComentarioListNameView(self, search, page):
        try:
            page = page
            pages = 10
            comentarioList = Usercomentario.query.filter(Usercomentario.pfsapucomentario.like(search)).filter(Usercomentario.pfsapucestado == 1).paginate(per_page=pages,error_out=False)
            return comentarioList
        except SQLAlchemyError as e:
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceComentarioDelete(self, id):
    
        try:
            comentarioEstado = Usercomentario.query.get(id)
            comentarioEstado.pfsapucestado = 0
            if comentarioEstado.pfsapucestado != '':
                db.session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)


