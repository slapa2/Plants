from flask import render_template, flash, redirect, url_for

from app.auth import auth
from app.auth.forms import RegistrationForm, LoginForm

@auth.route('/')
def landing():
    return render_template('landing.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Konto {form.email.data} zostało utworzone!', 'success')
        return redirect(url_for('auth.landing'))
    return render_template('register.html', title='register', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if False:
            flash(f'Witaj {form.email.data}!', 'success')
            return redirect(url_for('auth.landing'))
        else:
            flash(f'Zły email lub hasło!', 'success')
    return render_template('login.html', title='login', form=form)