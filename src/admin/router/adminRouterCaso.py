from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
arc= Blueprint('arc', __name__)
arc.route('/arc', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerCaso.onGetAdminControllerCasoListView)
arc.route('/arc/<int:page>', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerCasoListView)
arc.route('/arcmsv', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerModalCasoSaveView)
arc.route('/arcms', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerModalCasoSave)
#aru.route('/arumu/<int:id>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserModalUpdateView)
#aru.route('/aruu', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserUpdate)
#aru.route('/arud/<int:id>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserDelete)

