from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)

ADMIN_USERNAME  = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD  = os.environ.get('ADMIN_PASSWORD')
PORT            = os.environ.get('PORT')
app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/', methods=['GET'])
def start():

    return render_template('index.html')

@app.route('/home', methods=['GET','POST'])
def home():

    uname = request.values.get('uname')
    psw = request.values.get('psw')
    login_type = request.form.getlist('checkbox')


    if uname == ADMIN_USERNAME and psw == ADMIN_PASSWORD:
        return render_template('home.html')

    else:
        return render_template('index.html', error='Invalid username or password')



@app.route('/upload', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        content = file.read()
        
        
    return render_template('upload.html', content=content) 

@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result


if __name__== "__main__":
    app.run(host = "0.0.0.0", debug = True, port = PORT)