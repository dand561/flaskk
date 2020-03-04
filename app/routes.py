'''
Created by Dan Dragomirescu
dragomirescu.nicu@gmail.com
03/2020
'''

from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dan'}
    return '''
    <html>
        <head>
            <title> Home Page - My Flask app </title>
        </head>
        <body>
            <h1> Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''