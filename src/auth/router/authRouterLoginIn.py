from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
arlgn= Blueprint('arlgn', __name__)
#rath.route('/racnt', methods=['GET', 'POST'], defaults={"page": 1})(ControllerAdminCanasta.onGetControllerAdminCanastaList)
#rauth.route('/racnt/<int:page>', methods=['GET', 'POST'])(ControllerAdminCanasta.onGetControllerAdminCanastaList)
arlgn.route('/arlgn', methods=['GET', 'POST'])(AuthControllerLoginIn.onGetAuthCOntrollerLoginInView)
#arlgn.route('/arlgnin', methods=['POST'])(ControllerLoginIn.onGetControllerLoginIn) 