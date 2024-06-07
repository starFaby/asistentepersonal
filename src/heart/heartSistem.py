#----------
#--Sistem--
#----------
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template as render
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint
from flask_login import current_user
from flask_login import UserMixin



db = SQLAlchemy()
ma = Marshmallow()

