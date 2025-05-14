from src.heart.heartSistem import *
from src.heart.heartController import *
# admin - categoria - caso
arcmt= Blueprint('arcmt', __name__)
arcmt.route('/arcmt', methods=['GET', 'POST'], defaults={"page": 1})(AdminControllerComentario.onGetAdminControllerComentarioListView)
arcmt.route('/arcmt/<int:page>', methods=['GET', 'POST'])(AdminControllerComentario.onGetAdminControllerComentarioListView)

arcmt.route('/arcmtd/<int:id>', methods=['GET', 'POST'])(AdminControllerComentario.onGetAdminControllerComentarioDelete)