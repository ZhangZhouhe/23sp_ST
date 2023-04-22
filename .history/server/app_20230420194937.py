from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'
@app.route('/<name>')
def user_page(name):
    return f'Welcome to My Watchlist!{escape(name)}'