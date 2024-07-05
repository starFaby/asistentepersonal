from src.heart.heartSistem import *
from src.heart.heartServices import *
class AdminFormsWtfCaso(FlaskForm):
    id = StringField('id')
    nombre = StringField('nombre', validators=[InputRequired(message="Los nombres son requerido")])
    image = StringField('image', validators=[InputRequired(message="Los apellidos son requerido")])
    detalle = StringField('detalle', validators=[InputRequired(message="Los apellidos son requerido")])
    selectal = QuerySelectField(query_factory= AdminServiceCaso.onGetAdminServiceAsuntoLegalList, allow_blank=True, get_label='pfsapalnombre')
    estado = SelectField('estado', choices=[('1','Activo'), ('2','Inactivo')])
