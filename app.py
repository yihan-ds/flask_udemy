from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome Human!"

@app.route('/helloworld')
def welcome():
    return "Hello World. This is my first Flask app. Yay!"

app.run()