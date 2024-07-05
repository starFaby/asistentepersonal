
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


#----------
#--UTIL--
#----------
# util
#utilHeart
from src.util.utilVoice import *





