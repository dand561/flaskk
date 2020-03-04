'''
Created by Dan Dragomirescu
dragomirescu.nicu@gmail.com
03/2020
'''

from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dan'}
    return render_template('index.html', title='Home', user=user)

