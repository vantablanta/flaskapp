from email import message
from flask import render_template

from app import app

@app.route('/')
def index():
    message = 'Hello World'
    return render_template('home.html',message = message )