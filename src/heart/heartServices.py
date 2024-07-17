#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#----------------------------------AUTH SERVICES---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#-------------
# Services
#-------------
from src.auth.services.authServiceAdminLoginIn import AuthServiceAdminLoginIn 
from src.auth.services.authServiceUserLoginIn import AuthServiceUserLoginIn 

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#----------------------------------ADMIN SERVICES---------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

from src.admin.service.adminServiceUser import AdminServiceUser
from src.admin.service.adminServiceAsuntosLegales import AdminServiceAsuntosLegales
from src.admin.service.adminServiceCaso import AdminServiceCaso
from src.admin.service.adminServiceProceso import AdminServiceProceso

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#----------------------------------ClIENT SERVICES-------------------------------------
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

from src.client.service.clientServiceAsuntoLegal import ClientServiceAsuntoLegal
from src.client.service.clientServiceCaso import ClientServiceCaso
from src.client.service.clientServiceProceso import ClientServiceProceso
from src.client.service.clientServiceModalProcesoVoz import ClientServiceModalProcesoVoz



