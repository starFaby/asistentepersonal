from src.heart.heartSistem import *
from src.heart.heartServices  import *
from src.heart.heartFormWtf import *
class AdminControllerProceso:

    def onGetAdminControllerProcesoListView(page):
        try:
            if current_user.is_authenticated:
                page = page
                procesoList = AdminServiceProceso.onGetAdminServiceProcesoListView(page)
                if procesoList != []:
                    if request.method == 'POST' and 'tag' in request.form:
                        tag = request.form["tag"]
                        search = "%{}%".format(tag)
                        procesoList = AdminServiceProceso.onGetAdminServiceProcesoListNameView(search, page)
                        return render("admin/adminProceso.html", procesoList=procesoList, tag = tag)
                    else:
                        flash('Procesos Listados', category='success')
                        return render("admin/adminProceso.html", procesoList=procesoList)
                else:
                    flash('No Existe Procesos', category='info')
                    return render("admin/adminProceso.html", procesoList=procesoList)
            else:
                flash('Debe Logiarse Primero', category='info')
                return render("auth/loginin.html")

        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 
        
    def onGetAdminControllerModalProcesoSaveView():
        procesoList = []
        context = {
            'adminFormsWtfProceso': AdminFormsWtfProceso(),
            "save": True,
            "udpate": False,
            "procesoList": procesoList
        }
        try: 
            return render("admin/adminProceso.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
    
    def onGetAdminControllerAsuntoLegalList():
        return AdminServiceCaso.onGetAdminServiceAsuntoLegalList()

        
    def onGetAdminControllerModalProcesoSave():
        id = 0
        formProceso = AdminFormsWtfProceso()
        if formProceso.validate_on_submit():
            nombre = formProceso.nombre.data
            detalle = formProceso.detalle.data
            estado = formProceso.estado.data 
            selectcs = formProceso.selectcs.data 
            createdat = datetime.now()
            casoId=selectcs.pfsapcasoid
            
            resultSave = AdminServiceProceso.onGetAdminServiceProcesoSave(id, nombre, detalle, estado, createdat, casoId)
            if resultSave is True:
                flash('Proceso Guardado Exitosamente', category='success')
                return redirect(url_for('arp.onGetAdminControllerProcesoListView'))
            else:
                flash('Error al guardar los datos', category='error')
                return redirect(url_for('arp.onGetAdminControllerProcesoListView'))
        else:
            flash('Campos vacios, llene porfabor', category='info')
            return redirect(url_for('arp.onGetAdminControllerProcesoListView'))
