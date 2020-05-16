from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Phil'}
    version = "1.0.0.1"
    return render_template('index.html', title='Home', user=user, version=version)
