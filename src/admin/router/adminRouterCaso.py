from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
arc= Blueprint('arc', __name__)
arc.route('/arc', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerCaso.onGetAdminControllerCasoListView)
arc.route('/arc/<int:page>', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerCasoListView)
arc.route('/arcmsv', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerModalCasoSaveView)
arc.route('/arcms', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerModalCasoSave)
arc.route('/arcmuv/<int:id>', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerModalCasoUpdateView)
arc.route('/arcu', methods=['GET', 'POST'])(AdminControllerCaso.onGetAdminControllerCasoUpdate)
#aru.route('/arud/<int:id>', methods=['GET', 'POST'])(AdminControllerUser.onGetAdminControllerUserDelete)

