import sys
from datetime import datetime
from src.database.database import *
from src.heart.heartSistem import *
def createDB():
    db.drop_all()
    db.create_all()

def initDB():
    createDB()
    
    user = User(pfsuserscedula = "1725302705", 
                pfsusersnombres = "edgar fabian",
                pfsusersapellidos = "estrella guambuguete",
                pfsusersusername = "starfaby",
                pfsusersemail = "star._faby@hotmail.com",
                pfsuserspassword = "star123",
                pfsusersdireccion = "Ferroviaria Media Adrian Navarro S11-82 y puna",  
                pfsuserscelular = "0983856136", 
                pfsuserstelefono = "022647002",
                pfsusersisadmin = True,
                pfsusersavatar = "https://res.cloudinary.com/dqmbrjl7jfs/image/upload/v1638923678/starfaby_uqbwru.jpg", 
                pfsusersestado = 1,
                pfsuserscreatedat = datetime.now()
                )
    user.onGetSetPassword(user.pfsuserspassword)
    db.session.add(user)
    db.session.commit()  
    return 'base de datos creado existosamente' 