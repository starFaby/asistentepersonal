
#----------
#--General--
#----------
#Controller
#clientControllerStart


#----------
#--CLIENT--
#----------
#Controller
#clientControllerStart

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#----------------------------------AUTH------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#-----------------
# controller login
#-----------------
from src.auth.controller.authControllerUserLoginIn import AuthControllerUserLoginIn
from src.auth.controller.authControllerAdminUserLogout import AuthControllerAdminUserLogout

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#----------------------------------ADMIN------------------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#------------------
# CONTROLLER ADMIN 
#------------------

from src.admin.controller.adminControllerUsers import AdminControllerUser
from src.admin.controller.adminControllerAsuntosLegales import AdminControllerAsuntosLegales
from src.admin.controller.adminControllerCaso import AdminControllerCaso
from src.admin.controller.adminControllerProceso import AdminControllerProceso

#------------------
# CONTROLLER CLIENT 
#------------------
from src.client.controller.clientControllerAsuntoLegal import ClientControllerAsuntoLegal
from src.client.controller.clientControllerCaso import ClientControllerCaso
from src.client.controller.clientControllerProceso import ClientControllerProceso
from src.client.controller.clientControllerModalProcesoVoz import ClientControllerModalProcesoVoz

#----------
#--UTIL--
#----------
# util
#utilHeart
from src.util.utilVoice import *





