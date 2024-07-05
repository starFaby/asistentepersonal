from src.heart.heartSistem import *
from src.heart.heartDatabase import *
from src.heart.heartModelos import *

class AdminServiceUser:

    @classmethod
    def onGetAdminServiceUser(self, page):
        try:
            page = page
            pages = 10
            userList = User.query.order_by(User.pfsusersid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            
            return userList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceUserName(self, search, page):
        try:
            page = page
            pages = 10
            userList = User.query.filter(User.pfsusersnombres.like(search)).paginate(per_page=pages,error_out=False)
            return userList
        except SQLAlchemyError as e:
            print("Error en Service User ", e)
            return render('errors/error500.html')
        
    @classmethod
    def onGetAdminServiceDataUser(self, id):
    
        dataUser = User.query.filter(User.pfsusersid == id).one_or_none()
        return dataUser
    
    @classmethod
    def onGetAdminServiceUserSave(self, id, cedula , nombres, apellidos, username, email, password, direccion, celular, telefono, isadmin, avatar, estado, createdAt):
        modelUser = AdminModelUser(0, cedula, nombres, apellidos, username, email, password, direccion, celular, telefono, isadmin, avatar, estado, createdAt)
        newUser = User( pfsuserscedula = modelUser.getcedula(),
                        pfsusersnombres = modelUser.getnombres(),
                        pfsusersapellidos = modelUser.getapellidos(),
                        pfsusersusername = modelUser.getusername(),
                        pfsusersemail = modelUser.getemail(),
                        pfsuserspassword = modelUser.getpassword(),
                        pfsusersdireccion = modelUser.getdireccion(),
                        pfsuserscelular = modelUser.getcelular(),
                        pfsuserstelefono = modelUser.getelefono(),
                        pfsusersisadmin = modelUser.getisadmin(),
                        pfsusersavatar = modelUser.getavatar(),
                        pfsusersestado = modelUser.getestado(),
                        pfsuserscreatedat = modelUser.getcreatedat(),
                        )
        if modelUser.getcedula() != '' and modelUser.getnombres() != '' and modelUser.getapellidos() != '' and modelUser.getusername() != '' and modelUser.getemail() != '' and modelUser.getpassword() != '' and modelUser.getdireccion() != '' and modelUser.getcelular() != ''and modelUser.getelefono() != '' and modelUser.getisadmin() == False and modelUser.getavatar() != '' and modelUser.getestado() != '' and modelUser.getcreatedat() != '':
            db.session.add(newUser)
            db.session.commit()
            return True
        else:
            return False
        
    @classmethod
    def onGetAdminServiceUserUpdate(self, id, cedula , nombres, apellidos, username, email, password, direccion, celular, telefono, isadmin, avatar, estado, createdAt):
        modelUser = AdminModelUser(0, cedula, nombres, apellidos, username, email, password, direccion, celular, telefono, isadmin, avatar, estado, createdAt)
        newUser = User( pfsuserscedula = modelUser.getcedula(),
                        pfsusersnombres = modelUser.getnombres(),
                        pfsusersapellidos = modelUser.getapellidos(),
                        pfsusersusername = modelUser.getusername(),
                        pfsusersemail = modelUser.getemail(),
                        pfsuserspassword = modelUser.getpassword(),
                        pfsusersdireccion = modelUser.getdireccion(),
                        pfsuserscelular = modelUser.getcelular(),
                        pfsuserstelefono = modelUser.getelefono(),
                        pfsusersisadmin = modelUser.getisadmin(),
                        pfsusersavatar = modelUser.getavatar(),
                        pfsusersestado = modelUser.getestado(),
                        pfsuserscreatedat = modelUser.getcreatedat(),
                        )
        print(modelUser.getisadmin())
        if modelUser.getcedula != '' and modelUser.getnombres() != '' and modelUser.getapellidos() != '' and modelUser.getusername() != '' and modelUser.getemail() != '' and modelUser.getpassword() != '' and modelUser.getdireccion() != '' and modelUser.getcelular() != ''and modelUser.getelefono() != '' and modelUser.getisadmin() == False and modelUser.getavatar() != '' and modelUser.getestado() != '' and modelUser.getcreatedat() != '':
            db.session.add(newUser)
            db.session.commit()
            return True
        else:
            return False


