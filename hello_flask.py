from flask import Flask
from flask import url_for
from werkzeug.utils import redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello name'

@app.route('/hello')
def hello():
    return render_template('index.html')

@app.route('/user/<string:username>')
def username(username):
    return 'I am ' + username 

@app.route('/age/<int:age>')
def userage(age):
    return 'I am ' + str(age) + ' years old '

@app.route('/a')
def url_for_a():
    return 'Here is a' 
@app.route('/b')
def b():
    return redirect(url_for('url_for_a'))

if __name__ == '__main__':
    app.debug = True
    app.run()

