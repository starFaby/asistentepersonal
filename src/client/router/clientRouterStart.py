from flask import Blueprint
from src.heart.heartController import ClientControllerStart
crs= Blueprint('crs', __name__)
crs.route('/crs', methods=['GET', 'POST'])(ClientControllerStart.onGetClientControllerStart)
crs.route('/crsc', methods=['GET', 'POST'])(ClientControllerStart.onGetClientControllerCarnet)
crs.route('/crspabg', methods=['GET', 'POST'])(ClientControllerStart.onGetClientControllerPresentacionAbg)