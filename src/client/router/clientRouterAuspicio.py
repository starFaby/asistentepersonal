from flask import Blueprint
from src.heart.heartController import  *
cra= Blueprint('cra', __name__)
cra.route('/cra', methods=['GET'])(ClientControllerAuspicio.onGetClientControllerAuspicioView)
cra.route('/craonm', methods=['GET'])(ClientControllerAuspicio.onGetClientControllerOnAuspicioModal)