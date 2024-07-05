from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
aral= Blueprint('aral', __name__)
aral.route('/aral', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerAsuntosLegales.onGetAdminControllerAsuntosLegalesListView)
aral.route('/aral/<int:page>', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerAsuntosLegalesListView)
aral.route('/aralmsv', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerUserModalAsuntosLegalesSaveView)
aral.route('/aralms', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerUserModalAsuntosLegalesSave)
#aru.route('/arumu/<int:id>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserModalUpdateView)
#aru.route('/aruu', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserUpdate)
#aru.route('/arud/<int:id>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserDelete)

