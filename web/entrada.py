from flask_wtf import FlaskForm
from wtforms import StringField

class LineGraphForm(FlaskForm):
    archivocon=StringField('Archivo con gafas')
    archivosin=StringField('Archivo sin gafas')

