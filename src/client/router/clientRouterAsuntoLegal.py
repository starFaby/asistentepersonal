from flask import Blueprint
from src.heart.heartController import  ClientControllerAsuntoLegal
cral= Blueprint('cral', __name__)
cral.route('/cral', methods=['GET', 'POST'])(ClientControllerAsuntoLegal.onGetClientControllerAsuntoLegalListView)

