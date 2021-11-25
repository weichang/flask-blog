from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello name'

@app.route('/user/<string:username>')
def username(username):
    return 'I am ' + username 

@app.route('/age/<int:age>')
def userage(age):
    return 'I am ' + str(age) + ' years old '

if __name__ == '__main__':
    app.debug = True
    app.run()

