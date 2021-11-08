from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
   bustotorax = IntegerField('Busto ou Torax')
   quadril = IntegerField('Quadril')
   cintura = IntegerField('Cintura')
   genero= StringField('Gênero (m ou f)')
   submit = SubmitField('Predict')
   abc = "" # retorna a resposta para a frontpage