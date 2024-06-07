from src.heart.heartSistem import *
from src.heart.heartServices import *

class UserModel(UserMixin):
    def __init__(self, userData):
        self.id = userData.pfsusersusername
        self.iduser = userData.pfsusersid
        self.password = userData.pfsuserspassword
        self.email = userData.pfsusersemail
        self.avatar = userData.pfsusersavatar
        self.isadmin = userData.pfsusersisadmin
        self.estado = userData.pfsusersestado
        
    @staticmethod
    def get(pfsusersusername):
        userData = ServicesLoginIn.onGetUserByUsername(pfsusersusername = pfsusersusername)
        return UserModel(userData)