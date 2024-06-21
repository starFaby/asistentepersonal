from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
arulgn= Blueprint('arulgn', __name__)
arulgn.route('/arulgn', methods=['GET', 'POST'])(AuthControllerUserLoginIn.onGetAuthControllerUserLoginInView)
arulgn.route('/arulgin', methods=['GET', 'POST'])(AuthControllerUserLoginIn.onGetAuthControllerUserLoginIn)


