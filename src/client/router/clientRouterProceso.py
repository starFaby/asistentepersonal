from flask import Blueprint
from src.heart.heartController import  ClientControllerProceso
crp= Blueprint('crp', __name__)
crp.route('/crp/<int:id>', methods=['GET', 'POST'])(ClientControllerProceso.onGetClientControllerProcesoListView)
