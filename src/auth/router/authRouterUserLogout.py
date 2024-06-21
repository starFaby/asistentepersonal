from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
araulgt= Blueprint('araulgt', __name__)
#rath.route('/racnt', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCanasta.onGetControllerAdminCanastaList)
#rauth.route('/racnt/<int:page>', methods=['GET', 'POST'])(ControllerAdminCanasta.onGetControllerAdminCanastaList)
araulgt.route('/araulgt', methods=['GET', 'POST'])(AuthControllerAdminUserLogout.onGetAuthControllerAdminLoginLogout)
#arlgn.route('/arlgnin', methods=['POST'])(ControllerLoginIn.onGetControllerLoginIn) 