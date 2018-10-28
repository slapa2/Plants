
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from plants.plants.models import Plant

class AddPlantForm(FlaskForm):
    polish_name = StringField('Nazwa:', validators=[DataRequired()])
    image = StringField('url obrazka:', validators=[DataRequired()])
    submit = SubmitField("Dodaj")