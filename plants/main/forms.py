from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    question = StringField('Pytanie:', validators=[DataRequired()], widget=TextArea())
    submit = SubmitField("Wyślij")
