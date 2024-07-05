#----------
#--Client--
#----------
#Router
#clientControllerStart
from src.client.router.clientRouterStart import crs

#----------
#--AUTH--
#----------
#Router
# Router DataBase 
from src.auth.router.authRouterDataBase import ardbm
# Router Login 
from src.auth.router.authRouterUserLoginIn import arulgn 
from src.auth.router.authRouterUserLogout import araulgt

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#------------------------------ADMIN------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#--------------------------
#---ADMIN ROUTER USER------
#--------------------------

from src.admin.router.adminRouterUser import aru
from src.admin.router.adminRouterAsuntosLegales import aral
from src.admin.router.adminRouterCaso import arc


