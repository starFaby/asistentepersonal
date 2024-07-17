from flask import Blueprint
from src.heart.heartController import  ClientControllerCaso
crc= Blueprint('crc', __name__)
crc.route('/crc/<int:id>', methods=['GET', 'POST'])(ClientControllerCaso.onGetClientControllerCasoListView)
