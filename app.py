from crypt import methods
import re
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():

    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():

    uname = request.values.get('uname')
    psw = request.values.get('psw')
    login_type = request.values.get('teacher')
    print (login_type)
    # if uname == 'admin' and psw == 'admin':
    #     return render_template('login.html')


    print(uname, psw)

    return render_template('index.html')


@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result


if __name__== "__main__":
    app.run(host = "0.0.0.0", debug = True, port = 5003)