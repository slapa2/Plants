from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

from plants import db, bcrypt
from plants.auth import auth
from plants.auth.models import User
from plants.auth.forms import RegistrationForm, LoginForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.landing'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pasword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_pasword)
        db.session.add(user)
        db.session.commit()
        flash(f'Konto {form.email.data} zostało utworzone!', 'success')
        return redirect(url_for('main.landing'))
    return render_template('register.html', title='rejestracja', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.landing'))

    form = LoginForm()
    print(request.args.get('next'))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.stay_loggedin.data)
            next_page = request.args.get('next')
            print(next_page)
            return redirect(next_page) if next_page else redirect(url_for('main.landing'))
        else:
            flash(f'Zły email lub hasło!', 'danger')
    return render_template('login.html', title='logowanie', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.landing'))


@auth.route('/account')
@login_required
def account():
    return render_template('account.html', title='profil')