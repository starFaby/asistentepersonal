from src.heart.heartSistem import *
from src.heart.heartServices  import *
from src.heart.heartFormWtf import *
class AdminControllerUser:

    def onGetAdminControllerUserViewList(page):
        try:
            if current_user.is_authenticated:
                page = page
                userList = AdminServiceUser.onGetAdminServiceUser(page)
                if userList != []:
                    if request.method == 'POST' and 'tag' in request.form:
                        tag = request.form["tag"]
                        search = "%{}%".format(tag)
                        userList = AdminServiceUser.onGetAdminServiceUserName(search, page)
                        return render("admin/adminUser.html", userList=userList, tag = tag)
                    else:
                        flash('Usuarios Listados', category='success')
                        return render("admin/adminUser.html", userList=userList)
                else:
                    flash('No Existe Usuarios', category='info')
                    return render("admin/adminUser.html", userList=userList)
            else:
                flash('Debe Logiarse Primero', category='info')
                return render("auth/loginin.html")

        except SQLAlchemyError as e:
                return render('errors/error500.html', e) 
        
    def onGetAdminControllerUserModalSaveView():
        userList = []
        context = {
            'adminFormsWtfUser': AdminFormsWtfUser(),
            "save": True,
            "udpate": False,
            "userList": userList
        }
        try: 
            return render("admin/adminUser.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
        
    def onGetAdminControllerUserModalSave():
        id = 0
        formUser = AdminFormsWtfUser()
        if formUser.validate_on_submit():
            cedula = formUser.cedula.data
            nombres = formUser.nombres.data
            apellidos = formUser.apellidos.data
            username = formUser.username.data
            email = formUser.email.data
            password = formUser.password.data
            direccion = formUser.direccion.data
            celular = formUser.celular.data
            telefono = formUser.telefono.data
            isadmin = False
            avatar = 'https://res.cloudinary.com/dgypxt4la/image/upload/v1693192740/noimage_hlaewx.png'
            estado = formUser.estado.data
            createdAt = datetime.now()
            resultUser =  AdminServiceUser.onGetAdminServiceUserSave(id , cedula, nombres, apellidos, username, email, password, direccion, celular, telefono, isadmin, avatar, estado, createdAt)
            if resultUser is True:
                flash('Guardado exitosamente', category='success')
                return redirect(url_for('aru.onGetAdminControllerUserViewList'))
            else:
                flash('Error al Guardar', category='error')
                return redirect(url_for('aru.onGetAdminControllerUserViewList'))
        
    def onGetAdminControllerUserModalUpdateView(id):
        userList = []
        dataUser = AdminServiceUser.onGetAdminServiceDataUser(id)
        context = {
            'adminFormsWtfUser': AdminFormsWtfUser(),
            "save": False,
            "update": True,
            "dataUser": dataUser,
            "userList": userList
        }
        try: 
            return render("admin/adminUser.html", **context)
        except SQLAlchemyError as e:
            return render('errors/error500.html', e) 
        
    
    def onGetAdminControllerUserModalUpdate():
        id = 0
        formUser = AdminFormsWtfUser()
        if formUser.validate_on_submit():
            cedula = formUser.cedula.data
            nombres = formUser.nombres.data
            apellidos = formUser.apellidos.data
            username = formUser.username.data
            email = formUser.email.data
            password = formUser.password.data
            direccion = formUser.direccion.data
            celular = formUser.celular.data
            telefono = formUser.telefono.data
            isadmin = False
            avatar = 'https://res.cloudinary.com/dgypxt4la/image/upload/v1693192740/noimage_hlaewx.png'
            estado = formUser.estado.data
            createdAt = datetime.now()
            resultUser =  AdminServiceUser.onGetAdminServiceUserUpdate(id , cedula, nombres, apellidos, username, email, password, direccion, celular, telefono, isadmin, avatar, estado, createdAt)
            if resultUser is True:
                flash('Guardado exitosamente', category='success')
                return redirect(url_for('aru.onGetAdminControllerUserViewList'))
            else:
                flash('Error al Guardar', category='error')
                return redirect(url_for('aru.onGetAdminControllerUserViewList'))