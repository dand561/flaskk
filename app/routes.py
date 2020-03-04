'''
Created by Dan Dragomirescu
dragomirescu.nicu@gmail.com
03/2020
'''

from flask import render_template
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dan'}
    posts = [
        {
            'author' : {'username' : 'Dan'},
            'body' : 'Hot since 82 is really enjoyable, czech him out.'
        },
        {
            'author' : {'username' : 'Alertego'},
            'body' : 'But Pablo Bolivar\'s simply utterly astonishing'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)