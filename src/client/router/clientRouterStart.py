from flask import Blueprint
from src.client.controller.clientControllerStart import ClientControllerStart
crs= Blueprint('crs', __name__)
crs.route('/crs', methods=['GET', 'POST'])(ClientControllerStart.onGetClientControllerStart)
crs.route('/crsc', methods=['GET', 'POST'])(ClientControllerStart.onGetClientControllerCarnet)