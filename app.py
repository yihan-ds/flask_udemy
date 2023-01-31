from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome Human!"

@app.route('/helloworld')
def welcome():
    return "Hello World. This is my first Flask app. Yay!"

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "You've used a POST request!"
    else:
        return "I'm guessing you are probably using a GET request."

app.run()