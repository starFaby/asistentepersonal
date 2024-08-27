from src.heart.heartSistem import *
from src.heart.heartServices import *
from src.heart.heartFormWtf import *
class AdminControllerAsuntosLegales:
    def onGetAdminControllerAsuntosLegalesListView(page):
        try:
            if current_user.is_authenticated:
                page = page
                asisLegalList = AdminServiceAsuntosLegales.onGetAdminServiceAsuntosLegales(page)
                
                if asisLegalList.items != []:
                    if request.method == 'POST' and 'tag' in request.form:
                        tag = request.form["tag"]
                        search = "%{}%".format(tag)
                        asisLegalList = AdminServiceAsuntosLegales.onGetAdminServiceAsuntosLegalesName(search, page)
                        return render('admin/adminAsuntosLegales.html', asisLegalList=asisLegalList, tag = tag)
                    else:
                        flash('Asuntos Legales Listados', category='success')
                        return render("admin/adminAsuntosLegales.html", asisLegalList=asisLegalList)
                else:
                    flash('No Existe Asuntos Legales', category='info')
                    return render("admin/adminAsuntosLegales.html", asisLegalList=asisLegalList)
            else:
                flash('Debe Logiarse Primero', category='info')
                return render("admin/adminAsuntosLegales.html")

        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 
        
    def onGetAdminControllerUserModalAsuntosLegalesSaveView():
        asisLegalList = []
        context = {
            'adminFormsWtfAsuntosLegales': AdminFormsWtfAsuntosLegales(),
            "save": True,
            "udpate": False,
            "asisLegalList": asisLegalList
        }
        try: 
            return render("admin/adminAsuntosLegales.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    def onGetAdminControllerUserModalAsuntosLegalesSave():
        id = 0
        formAsunLegal = AdminFormsWtfAsuntosLegales()
        if formAsunLegal.validate_on_submit():
            nombre = formAsunLegal.nombre.data
            image = formAsunLegal.image.data
            detalle = formAsunLegal.detalle.data
            estado = formAsunLegal.estado.data
            createdat = datetime.now()
            resultSave = AdminServiceAsuntosLegales.onGetAdminServiceAsuntoLegalSave(id, nombre, image, detalle, estado, createdat)
            if resultSave is True:
                flash('Guardado exitosamente', category='success')
                return redirect(url_for('aral.onGetAdminControllerAsuntosLegalesListView'))
            else:
                flash('Error al Guardar', category='error')
                return redirect(url_for('aral.onGetAdminControllerAsuntosLegalesListView'))
            
    
    def onGetAdminControllerUserModalAsuntosLegalesUpdateView(id):
        dataUser = AdminServiceAsuntosLegales.onGetAdminSericeUserModalAsuntosLegalesUpdateView(id)
        asisLegalList = []
        context = {
            'adminFormsWtfAsuntosLegales': AdminFormsWtfAsuntosLegales(),
            "save": False,
            "update": True,
            "dataUser": dataUser,
            'asisLegalList':asisLegalList
        }
        try: 
            return render("admin/adminAsuntosLegales.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    def onGetAdminControllerUserModalAsuntosLegalesUpdate():
        try:
            formAsunLegal = AdminFormsWtfAsuntosLegales()
            if current_user.is_authenticated:
                if formAsunLegal.validate_on_submit():
                    id = formAsunLegal.id.data
                    nombre = formAsunLegal.nombre.data
                    image = formAsunLegal.image.data
                    detalle = formAsunLegal.detalle.data
                    estado = formAsunLegal.estado.data
                    createdat = datetime.now()

                    asuntoLegalUpdate = AdminServiceAsuntosLegales.onGetAdminServiceUserModalAsuntosLegalesUpdate(id, nombre, image, detalle, estado, createdat)
                    if asuntoLegalUpdate is True:
                        flash('Actualizado Exitosamente', category='success')
                        return redirect(url_for('aral.onGetAdminControllerAsuntosLegalesListView'))
                    else:
                        flash('Error al actualizar los datos', category='error')
                        return redirect(url_for('aral.onGetAdminControllerAsuntosLegalesListView'))
                else:
                    return redirect(url_for('aral.onGetAdminControllerAsuntosLegalesListView'))

            else:
                flash('Debe logearse primero', category='info')
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
        
    def onGetAdminControllerAsuntosLegalesDelete(id):
        try:
            if current_user.is_authenticated:
                user = AdminServiceAsuntosLegales.onGetAdminServiceAsuntosLegalesDelete(id)
                if user is True:
                    flash('Eliminado Exitosamente', category='success')
                    return redirect(url_for('aral.onGetAdminControllerAsuntosLegalesListView'))
                else:
                    flash('Error al eliminar el dato', category='error')
                    return redirect(url_for('aral.onGetAdminControllerAsuntosLegalesListView'))
            else:
                flash('Debe logearse primero', category='info')
                return render("auth/loginin.html")
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 