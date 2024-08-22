from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
aral= Blueprint('aral', __name__)
aral.route('/aral', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerAsuntosLegales.onGetAdminControllerAsuntosLegalesListView)
aral.route('/aral/<int:page>', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerAsuntosLegalesListView)
aral.route('/aralmsv', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerUserModalAsuntosLegalesSaveView)
aral.route('/aralms', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerUserModalAsuntosLegalesSave)
aral.route('/aralmuv/<int:id>', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerUserModalAsuntosLegalesUpdateView)
aral.route('/aralmu', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerUserModalAsuntosLegalesUpdate)
aral.route('/arald/<int:id>', methods=['GET', 'POST'])(AdminControllerAsuntosLegales.onGetAdminControllerAsuntosLegalesDelete)

