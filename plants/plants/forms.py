
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.widgets import TextArea


class PlantForm(FlaskForm):
    polish_name = StringField('Nazwa:', validators=[DataRequired()])
    latin_name = StringField('Nazwa łacińska:', validators=[])

    light_level = SelectField('Poziom światła:', coerce=int, choices=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)])
    water_level = SelectField('Ilość wody:', coerce=int, choices=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)])
    spray = BooleanField('Spryskiwać:')

    light_description = StringField('Opis stanowiska:', validators=[], widget=TextArea())
    water_description = StringField('Podlewanie:', validators=[], widget=TextArea())
    temperature = StringField('Temperatura:', validators=[], widget=TextArea())
    soil = StringField('Gleba:', validators=[], widget=TextArea())
    fertilizing = StringField('Nawożenie:', validators=[], widget=TextArea())
    transplanting = StringField('Przesadzanie:', validators=[], widget=TextArea())
    multiplication = StringField('Rozmnażanie:', validators=[], widget=TextArea())
    image = StringField('url obrazka:', filters = [lambda x: x or None])
    submit = SubmitField("Zapisz")


class PlantSearchForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    search = SubmitField('Wyszukaj')
