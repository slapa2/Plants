from flask import render_template

from app.auth import authentication as at

@at.route('/')
def landing():
    return render_template('landing.html')