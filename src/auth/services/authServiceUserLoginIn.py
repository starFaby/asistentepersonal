from src.heart.heartSistem import *
from src.heart.heartDatabase import *

class AuthServiceUserLoginIn():

    def onGetAuthServiceUserLoginInByUsername(pfsusersusername):
        try:
            return User.query.filter_by(pfsusersusername = pfsusersusername).first()
        
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return render('errors/error500.html')
