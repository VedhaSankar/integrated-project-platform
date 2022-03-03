from flask import Flask, render_template, request, flash, redirect, session
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import gcp_upload
from utils import get_prev_id, display_all_projects


load_dotenv()

app = Flask(__name__)

ADMIN_USERNAME  = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD  = os.environ.get('ADMIN_PASSWORD')
MONGO_URI       = os.environ.get('MONGO_URI')
PORT            = os.environ.get('PORT')


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config["UPLOAD_FOLDER"] = "static/"

client = MongoClient(MONGO_URI)  
DB_NAME = 'prohost'
database = client[DB_NAME]

@app.route('/', methods=['GET', 'POST'])
def start():

    if request.method == 'POST':
        session['username'] = request.form['uname']
        # uname = request.values.get('uname')
        psw = request.values.get('psw')
        login_type = request.form.getlist('checkbox')

        if session['username'] == ADMIN_USERNAME and psw == ADMIN_PASSWORD:
                return render_template('home.html')

        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/home', methods = ['GET', 'POST'])
def home():

    return render_template('home.html') 


@app.route('/project', methods=['GET', 'POST'])
def get_project_details():

    if request.method == 'POST':

        project_name        = request.values.get('project_name')
        project_description = request.values.get('project_description')
        email               = request.values.get('email')
        resource_link       = request.values.get('resource_link')
        github_link         = request.values.get('github_link')

        current_id = get_prev_id() + 1

        project_dict = {
            '_id'                 : current_id,
            "project_name"        : project_name,
            "project_description" : project_description,
            "email"               : email,
            "resource_link"       : resource_link,
            "github_link"         : github_link
        }

        collection_name = 'project_details'
        new_collection = database[collection_name]
        x = new_collection.insert_one(project_dict)
        print(x)

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            gcp_upload.upload_blob(f'static/{filename}', f'project/{filename}')
            print("files uploaded")

    return render_template('form.html')

@app.route('/view-all', methods = ['GET', 'POST'])
def view_all_projects():

    list_of_projects = display_all_projects()

    result = {
        "result" : list_of_projects
    }

    return render_template('view_all.html', projects = result)


@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result


if __name__== "__main__":
    app.run(host = "0.0.0.0", debug = True, port = PORT)