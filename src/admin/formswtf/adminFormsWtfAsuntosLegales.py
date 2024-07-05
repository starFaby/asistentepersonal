from src.heart.heartSistem import *
class AdminFormsWtfAsuntosLegales(FlaskForm):
    id = StringField('id')
    nombre = StringField('nombre', validators=[InputRequired(message="Los nombres son requerido")])
    image = StringField('image', validators=[InputRequired(message="Los apellidos son requerido")])
    detalle = StringField('detalle', validators=[InputRequired(message="Los apellidos son requerido")])
    estado = SelectField('estado', choices=[('1','Activo'), ('2','Inactivo')])
