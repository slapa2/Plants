from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea
from flask_wtf.recaptcha import RecaptchaField

class ContactForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    question = StringField('Pytanie:', validators=[DataRequired()], widget=TextArea())
    recaptcha = RecaptchaField()
    submit = SubmitField("Wyślij")
