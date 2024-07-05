from src.heart.heartSistem import *
class AdminFormsWtfUser(FlaskForm):
    id = StringField('id')
    cedula = StringField('cedula', validators=[InputRequired(message="La cedula es requerida")])
    nombres = StringField('nombres', validators=[InputRequired(message="Los nombres son requerido")])
    apellidos = StringField('apellidos', validators=[InputRequired(message="Los apellidos son requerido")])
    username = StringField('username', validators=[InputRequired(message="Los apellidos son requerido")])
    email = StringField('email', validators=[InputRequired(message="Los apellidos son requerido")])
    password = StringField('password', validators=[InputRequired(message="Los apellidos son requerido")])
    direccion = StringField('direccion', validators=[InputRequired(message="Los apellidos son requerido")])
    celular = StringField('celular', validators=[InputRequired(message="Los apellidos son requerido")])
    telefono = StringField('telefono', validators=[InputRequired(message="Los apellidos son requerido")])
    estado = SelectField('estado', choices=[('1','Activo'), ('2','Inactivo')])









