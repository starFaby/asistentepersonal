from flask import Blueprint
from src.migrate.migrate import initDB

ardbm= Blueprint('ardbm', __name__)

ardbm.route('/ardbm', methods=['GET'])(initDB)