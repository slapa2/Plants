from flask import render_template, flash, redirect, url_for

from plants import db, bcrypt
from plants.auth import auth
from plants.auth.models import User
from plants.auth.forms import RegistrationForm, LoginForm

@auth.route('/')
def landing():
    return render_template('landing.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pasword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_pasword)
        db.session.add(user)
        db.session.commit()
        flash(f'Konto {form.email.data} zostało utworzone!', 'success')
        return redirect(url_for('auth.landing'))
    return render_template('register.html', title='register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'Logowanie udane', 'success')
            return redirect(url_for('auth.landing'))
        else:
            flash(f'Zły email lub hasło!', 'success')
    return render_template('login.html', title='login', form=form)