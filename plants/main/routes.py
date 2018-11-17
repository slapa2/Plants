from flask import render_template, flash, redirect, url_for
from flask_mail import Message
from plants import mail
from plants.main import main
from plants.main.forms import ContactForm


@main.route('/')
def landing():
    return render_template('landing.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
    	email = form.email.data
    	question = form.question.data
    	msg = Message('[MyPlants] - Pytanie', recipients=['bazaroslin@gmail.com'])
    	msg.html = f'<h4>email: {email}</h4><p>{question}</p>'
    	mail.send(msg)
    	flash(f'Wiadomość została wysłana. Dziękujemy!', 'success')
    	return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Kontakt', form=form)