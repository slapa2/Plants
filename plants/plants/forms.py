
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

from plants.plants.models import Plant

class AddPlantForm(FlaskForm):
    polish_name = StringField('Nazwa:', validators=[DataRequired()])
    latin_name = StringField('Nazwa łacińska:', validators=[])

    light_level = StringField('Światła:', validators=[])
    light_description = IntegerField('Poziom śqiatła 0-5:', validators=[])
    water_level = IntegerField('Ilość wody:', validators=[])
    water_description = StringField('Podlewanie:', validators=[])
    temperature = StringField('Temperatura:', validators=[])
    soil = StringField('Gleba:', validators=[])
    fertilizing = StringField('Nawożenie:', validators=[])
    transplanting = StringField('Przesadzanie:', validators=[])
    multiplication = StringField('Rozmnażanie:', validators=[])

    image = StringField('url obrazka:', validators=[DataRequired()])

    submit = SubmitField("Dodaj")