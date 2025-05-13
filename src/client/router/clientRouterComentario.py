from flask import Blueprint
from src.heart.heartController import  ClientControllerComentario
crcmt= Blueprint('crcmt', __name__)
crcmt.route('/crcmt', methods=['POST'])(ClientControllerComentario.onGetClientControllerComentario)