from flask import render_template
from plants.main import main


@main.route('/')
def landing():
    return render_template('landing.html')

@main.route('/contact')
def contact():
    return render_template('contact.html', title='kontakt')
