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
#---ADMIN ROUTER------
#--------------------------

from src.admin.router.adminRouterUser import aru
from src.admin.router.adminRouterAsuntosLegales import aral
from src.admin.router.adminRouterCaso import arc
from src.admin.router.adminRouterProceso import arp
from src.admin.router.adminRouterProceso import arp

#--------------------------
#---ADMIN CLIENT------
#--------------------------
from src.client.router.clientRouterAsuntoLegal import cral
from src.client.router.clientRouterCaso import crc
from src.client.router.clientRouterProceso import crp
from src.client.router.clientRouterModalProcesoVoz import crmpv




