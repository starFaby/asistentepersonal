from src.heart.heartSistem import *
from src.heart.heartServices import *
class AdminFormsWtfProceso(FlaskForm):
    id = StringField('id')
    nombre = StringField('nombre', validators=[InputRequired(message="El Nombre es requerido")])
    detalle = StringField('detalle', validators=[InputRequired(message="El Detalle es requerido")])
    estado = SelectField('estado', choices=[('1','Activo'), ('2','Inactivo')])
    selectcs = QuerySelectField(query_factory= AdminServiceProceso.onGetAdminServiceCasoList, allow_blank=True, get_label='pfsapcasonombre')