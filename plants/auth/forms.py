from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField('Hasło:', validators=[DataRequired(), EqualTo('confirm')])
    confirm = PasswordField('Powtórz hasło', validators=[DataRequired()])
    submit = SubmitField("Zarejestruj")


class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired()])
    password = PasswordField("Hasło:", validators=[DataRequired()])
    stay_loggedin = BooleanField("Zapamiętaj mnie")
    submit = SubmitField('Zaloguj')
