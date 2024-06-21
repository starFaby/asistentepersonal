from src.heart.heartSistem import *
from src.heart.heartDatabase import *

class AuthServiceAdminLoginIn():

    def onGetAuthServiceAdminLoginInByUsername(pfsadminusername):
        try:
            return Admin.query.filter_by(pfsadminusername = pfsadminusername).first()
        
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return render('errors/error500.html')
