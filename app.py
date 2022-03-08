from flask import Flask, render_template, request, flash, redirect, session
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import gcp_upload
from utils import get_prev_id, display_all_projects, extract_zip
import subprocess


load_dotenv()

app = Flask(__name__)

ADMIN_USERNAME      = os.environ.get('ADMIN_USERNAME')
ADMIN_PASSWORD      = os.environ.get('ADMIN_PASSWORD')
MONGO_URI           = os.environ.get('MONGO_URI')
PORT                = os.environ.get('PORT')
ALLOWED_EXTENSIONS  = {'zip'}
user = {
    "username": ADMIN_USERNAME, 
    "password": ADMIN_PASSWORD
}

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config["UPLOAD_FOLDER"] = "uploads/"

client = MongoClient(MONGO_URI)  
DB_NAME = 'prohost'
database = client[DB_NAME]


def allowed_file(filename):
    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def start():

    if request.method == 'POST':
        username = request.form['uname']
        psw = request.values.get('psw')
        login_type = request.form.getlist('checkbox')

        if username == user['username'] and psw == user['password']:
            session['user'] = username
            return redirect('/home')

        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if('user' in session and session['user'] == user['username']):
        return render_template('home.html')

    return render_template('login.html') 


@app.route('/project', methods=['GET', 'POST'])
def get_project_details():

    if request.method == 'POST':

        project_name        = request.values.get('project_name')
        project_description = request.values.get('project_description')
        email               = request.values.get('email')
        resource_link       = request.values.get('resource_link')
        github_link         = request.values.get('github_link')
        app_name            = request.values.get('app_name')

        collection_name = 'project_details'

        current_project_id = get_prev_id(collection_name) + 1

        project_dict = {
            '_id'                 : current_project_id,
            "project_name"        : project_name,
            "project_description" : project_description,
            "email"               : email,
            "resource_link"       : resource_link,
            "github_link"         : github_link
        }

        new_collection = database[collection_name]
        x = new_collection.insert_one(project_dict)
        print(x)

        if request.method == 'POST':
        # check if the post request has the file part
            if 'file' not in request.files:

                flash('No file part')
                return redirect(request.url)

            file = request.files['file']

            # If the user does not select a file, the browser submits an
            # empty file without a filename.

            if file.filename == '':

                flash('No selected file')
                return redirect(request.url)

            if file and allowed_file(file.filename):

                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                extract_zip(f'uploads/{filename}')
                # gcp_upload.upload_blob(f'uploads/{filename}', f'project_{current_project_id}/{filename}')
                subprocess.call(["./cr_deploy.sh"])
                print("yolo")
                return render_template('form.html')
                # return redirect(url_for('download_file', name=filename))
            else:
                flash('Allowed file type is .zip')
                return redirect(request.url)

    return render_template('form.html')

@app.route('/view-all', methods = ['GET', 'POST'])
def view_all_projects():

    list_of_projects = display_all_projects()

    result = {
        "result" : list_of_projects
    }

    return render_template('view_all.html', projects = result)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():

    if request.method == 'POST':

        aitceid         = request.values.get('aitceid')
        uname           = request.values.get('uname')
        college_name    = request.values.get('college_name')
        email_id        = request.values.get('email_id')
        password        = request.values.get('password')

        collection_name = 'user_details'

        current_user_id = get_prev_id(collection_name) + 1

        user_dict = {
            '_id'           : current_user_id,
            "aitceid"       : aitceid,
            "uname"         : uname,
            "college_name"  : college_name,
            "email_id"      : email_id,
            "password"      : password
        }


        new_collection = database[collection_name]
        x = new_collection.insert_one(user_dict)
        print(x)

    return render_template('sign_up.html')


if __name__== "__main__":
    app.run(host = "0.0.0.0", debug = True, port = PORT)