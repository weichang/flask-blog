from flask import Flask ,request
from flask import url_for
from werkzeug.utils import redirect
from flask import render_template

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method  == 'POST':
        return 'Hello' + request.values['username']
    return render_template('login.html')
    

@app.route('/')
def index():
    return 'hello name'

@app.route('/hello/<user>')
def hello(user):
    return render_template('index.html',user_data=user)

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

