'''
Created by Dan Dragomirescu
dragomirescu.nicu@gmail.com
03/2020
'''

from flask import Flask
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = '42069mueue'
app.config.from_object(Config)

from app import routes

