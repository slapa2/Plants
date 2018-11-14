from flask import render_template
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

    	msg = Message('[MyPlants] - Pytanie', sender=email, recipients=['bazaroslin@gmail.com'])
    	msg.body = question

    	mail.send(msg)
    return render_template('contact.html', title='Kontakt', form=form)