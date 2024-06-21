from src.heart.heartSistem import *
from src.heart.heartServices import *

class AuthMiddlewaresUserLoginIn(UserMixin):

    def __init__(self, userData):
        self.id = userData.pfsusersusername
        self.iduser = userData.pfsusersid
        self.userisadmin = userData.pfsusersisadmin
        self.emailuser = userData.pfsusersemail
        self.avataruser = userData.pfsusersavatar
        self.estadouser = userData.pfsusersestado
        
    @staticmethod
    def get(pfsusersusername):
        userData = AuthServiceUserLoginIn.onGetAuthServiceUserLoginInByUsername(pfsusersusername = pfsusersusername)
        return AuthMiddlewaresUserLoginIn(userData)