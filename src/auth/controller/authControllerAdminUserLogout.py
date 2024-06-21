from src.heart.heartSistem import *
class AuthControllerAdminUserLogout:
        
    def onGetAuthControllerAdminLoginLogout():
        logout_user()
        flash("Cerraste sesion !!", category="info")
        
        return render('index.html')
    

