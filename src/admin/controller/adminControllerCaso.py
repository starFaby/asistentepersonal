from src.heart.heartSistem import *
from src.heart.heartServices  import *
from src.heart.heartFormWtf import *
class AdminControllerCaso:

    def onGetAdminControllerCasoListView(page):
        try:
            if current_user.is_authenticated:
                page = page
                casoList = AdminServiceCaso.onGetAdminServiceCaso(page)
                if casoList != []:
                    if request.method == 'POST' and 'tag' in request.form:
                        tag = request.form["tag"]
                        search = "%{}%".format(tag)
                        casoList = AdminServiceCaso.onGetAdminServiceCasoName(search, page)
                        return render("admin/adminCaso.html", casoList=casoList, tag = tag)
                    else:
                        flash('Caso Listados', category='success')
                        return render("admin/adminCaso.html", casoList=casoList)
                else:
                    flash('No Existe Casos', category='info')
                    return render("admin/adminCaso.html", casoList=casoList)
            else:
                flash('Debe Logiarse Primero', category='info')
                return render("auth/loginin.html")

        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 
        
    def onGetAdminControllerModalCasoSaveView():
        casoList = []
        context = {
            'adminFormsWtfCaso': AdminFormsWtfCaso(),
            "save": True,
            "udpate": False,
            "casoList": casoList
        }
        try: 
            return render("admin/adminCaso.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    
    def onGetAdminControllerAsuntoLegalList():
        return AdminServiceCaso.onGetAdminServiceAsuntoLegalList()

        
    def onGetAdminControllerModalCasoSave():
        formCaso = AdminFormsWtfCaso()
        if formCaso.validate_on_submit():
            nombre = formCaso.nombre.data
            image = formCaso.image.data
            detalle = formCaso.detalle.data
            selectal = formCaso.selectal.data 
            estado = formCaso.estado.data 
            createdat = datetime.now()
            asunlegal=selectal.pfsapalid
            
            resultSave = AdminServiceCaso.onGetAdminServiceCasoSave(id, nombre, image, detalle, estado, createdat, asunlegal)
            if resultSave is True:
                flash('Caso Guardado Exitosamente', category='success')
                return redirect(url_for('arc.onGetAdminControllerCasoListView'))
            else:
                flash('Error al guardar los datos', category='error')
                return redirect(url_for('arc.onGetAdminControllerCasoListView'))
        else:
            flash('Campos vacios, llene porfabor', category='info')
            return redirect(url_for('arc.onGetAdminControllerCasoListView'))
