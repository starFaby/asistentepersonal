#----------
#--Sistem--
#----------
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, render_template as render, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint



db = SQLAlchemy()
ma = Marshmallow()

