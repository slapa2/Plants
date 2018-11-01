
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError


class AddPlantForm(FlaskForm):
    polish_name = StringField('Nazwa:', validators=[DataRequired()])
    latin_name = StringField('Nazwa łacińska:', validators=[])

    light_level = IntegerField('Poziom światła 0-5:', validators=[])
    light_description = StringField('Opis stanowiska:', validators=[])
    water_level = IntegerField('Ilość wody 0-5:', validators=[])
    water_description = StringField('Podlewanie:', validators=[])
    temperature = StringField('Temperatura:', validators=[])
    soil = StringField('Gleba:', validators=[])
    fertilizing = StringField('Nawożenie:', validators=[])
    transplanting = StringField('Przesadzanie:', validators=[])
    multiplication = StringField('Rozmnażanie:', validators=[])
    image = StringField('url obrazka:', validators=[DataRequired()])
    submit = SubmitField("Zapisz")
