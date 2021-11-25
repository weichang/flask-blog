from flask import Flask ,request , flash , url_for , render_template
from werkzeug.utils import redirect
import os

app = Flask(__name__)
app.secret_key = "sdcascsacdas"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method  == 'POST':
        #  url_for('function name') 
        username = request.values['username']
        password = request.values['password']
        
        if login_check(username,password) :
            flash('Login Success !!!!')
            return redirect(url_for('hello',username=username))
    
    return render_template('login.html')

def login_check(username,password):
    if username == 'admin' and password == '123456':
        return True
    else:
        return False
    

@app.route('/')
def index():
    return 'hello name'

@app.route('/hello/<username>')
def hello(username):
    return render_template('index.html',user_data=username)

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

@app.route('/s')
def s():
    return  str(os.urandom(16))

if __name__ == '__main__':
    app.debug = True
    app.run()

