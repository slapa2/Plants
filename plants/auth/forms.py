from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.recaptcha import RecaptchaField

from plants.models import User

class RegistrationForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField('Hasło:', validators=[DataRequired(), EqualTo('confirm')])
    confirm = PasswordField('Powtórz hasło:', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Zarejestruj")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError(f'Użytkownik: {email.data} już istnieje')

class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Hasło:", validators=[DataRequired()])
    stay_loggedin = BooleanField("Zapamiętaj mnie")
    submit = SubmitField('Zaloguj')

class PasswordResetForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    submit = SubmitField("Reset hasła")
