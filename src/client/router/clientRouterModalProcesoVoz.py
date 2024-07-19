from flask import Blueprint
from src.heart.heartController import  ClientControllerModalProcesoVoz
crmpv= Blueprint('crmpv', __name__)
crmpv.route('/crmp/<int:id>', methods=['GET', 'POST'])(ClientControllerModalProcesoVoz.onGetClientControllerModalProceso)
crmpv.route('/crmpv/<int:id>', methods=['GET', 'POST'])(ClientControllerModalProcesoVoz.onGetClientControllerModalProcesoVoz)
 