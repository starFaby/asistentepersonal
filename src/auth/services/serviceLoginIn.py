from src.heart.heartSistem import *
from src.heart.heartController import *

class ServicesLoginIn():

    def onGetUserByUsername(pfsadminusername):
        try:
            return Admin.query.filter_by(pfsadminusername = pfsadminusername)
        
        except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                print(error)
                return render('errors/error500.html')
