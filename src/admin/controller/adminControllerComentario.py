from src.heart.heartSistem import *
from src.heart.heartServices  import *
from src.heart.heartFormWtf import *
class AdminControllerComentario:
    def onGetAdminControllerComentarioListView(page):
        try:
            if current_user.is_authenticated:
                page = page
                comentarioList = AdminServiceComentario.onGetAdminServiceComentarioListView(page)
                if comentarioList != []:
                    if request.method == 'POST' and 'tag' in request.form:
                        tag = request.form["tag"]
                        search = "%{}%".format(tag)
                        comentarioList = AdminServiceComentario.onGetAdminServiceComentarioListNameView(search, page)
                        return render("admin/adminComentario.html", comentarioList=comentarioList, tag = tag)
                    else:
                        flash('Caso Listados', category='success')
                        return render("admin/adminComentario.html", comentarioList=comentarioList)
                else:
                    flash('No Existe Casos', category='info')
                    return render("admin/adminComentario.html", comentarioList=comentarioList)
            else:
                flash('Debe Logiarse Primero', category='info')
                return render("auth/loginin.html")

        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 
        
    def onGetAdminControllerComentarioDelete(id):
        try:
            if current_user.is_authenticated:
                comentario = AdminServiceComentario.onGetAdminServiceComentarioDelete(id)
                if comentario is True:
                    flash('Elimando Exitosamente', category='success')
                    return redirect(url_for('arcmt.onGetAdminControllerComentarioListView'))
                else:
                    flash('Error al Eliminar', category='error')
                    return redirect(url_for('arcmt.onGetAdminControllerComentarioListView'))
            else:
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 