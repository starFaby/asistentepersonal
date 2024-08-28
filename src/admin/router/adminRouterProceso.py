from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
arp= Blueprint('arp', __name__)
arp.route('/arp', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerProceso.onGetAdminControllerProcesoListView)
arp.route('/arp/<int:page>', methods=['GET', 'POST'])(AdminControllerProceso.onGetAdminControllerProcesoListView)
arp.route('/arpmsv', methods=['GET', 'POST'])(AdminControllerProceso.onGetAdminControllerModalProcesoSaveView)
arp.route('/arpms', methods=['GET', 'POST'])(AdminControllerProceso.onGetAdminControllerModalProcesoSave)
arp.route('/arpmuv/<int:id>', methods=['GET', 'POST'])(AdminControllerProceso.onGetAdminControllerModalProcesoUpdateView)
arp.route('/arpmu', methods=['GET', 'POST'])(AdminControllerProceso.onGetAdminControllerModalProcesoUpdate)
arp.route('/arpmd/<int:id>', methods=['GET', 'POST'])(AdminControllerProceso.onGetAdminControllerProcesoDelete)

