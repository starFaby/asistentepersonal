from src.heart.heartSistem import *
from src.heart.heartServices import *
from src.heart.heartMiddlewares import *
class AuthControllerUserLoginIn:
    def onGetAuthControllerUserLoginInView():
        return render("auth/authUserLoginIn.html")
    
    
    def onGetAuthControllerUserLoginIn():
        
        try:
            txtUsername = request.form['txtUsername']
            txtUserpassword = request.form['txtUserpassword']
            user = AuthServiceUserLoginIn.onGetAuthServiceUserLoginInByUsername(pfsusersusername = txtUsername)
            if user is not None:
                if user.onGetCheckPassword(txtUserpassword): 
                    userModel = AuthMiddlewaresUserLoginIn(user)
                    login_user(userModel)
                    #token = SecurityAuth.onGetSecurityAuthToken()
                    
                    flash('logiado correctamente el usuario', category='success')
                    return render('index.html')
                else:
                    flash('Password Incorrecto', category='info')
                    return render('index.html')
            else:
                flash('Usuario y password Incorrecto', category='error')
                return render('index.html')
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')