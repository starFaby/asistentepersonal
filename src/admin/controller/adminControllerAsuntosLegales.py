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