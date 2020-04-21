from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    return 'Main page'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/<username>/hello')
def hellouser(username):
    return 'Hello %s orig %s' % (escape(username), username)
