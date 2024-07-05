#----------
#--Sistem--
#----------
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, render_template as render, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint
from datetime import datetime
from wtforms import StringField, SelectField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


db = SQLAlchemy()
ma = Marshmallow()

