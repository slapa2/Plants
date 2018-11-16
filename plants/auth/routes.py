from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from flask_mail import Message

from plants import db, bcrypt, mail
from plants.auth import auth
from plants.models import User
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
        token = user.get_user_token()
        msg = Message('MyPlants - Aktywacj konta', sender='noreply@myplants.pl', recipients=[user.email])
        msg.body = f"""Witaj!
Aby ukończyć rejestrację w serwise otwórz poniższy link aktywacyjny:

{url_for('auth.activate', token=token, _external=True)}

Jeśli nie zakładałeś konta zignoruj tą wiadomość.

Pozdrawiamy.
Zespół MyPlants"""

        mail.send(msg)
        db.session.add(user)
        db.session.commit()
        flash(f'Konto {form.email.data} zostało utworzone!<br>Potwierdz rejestrację otwiereając link aktywacyjny', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='rejestracja', form=form)

@auth.route('/activate/<token>', methods=['GET'])
def activate(token):
    user = User.verify_user_token(token)
    if user:
        user.activate_user()
        flash(f'Konto {user.email} zostało aktywowane', 'success')
        return redirect(url_for('auth.login'))
    else:
        flash(f'Błąd aktywacji! spróbuj zresetować hasło albo załorzyć nowe konto', 'info')
        return redirect(url_for('auth.register'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.landing'))

    form = LoginForm()
    print(request.args.get('next'))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.activate and bcrypt.check_password_hash(user.password, form.password.data):
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

