import pymongo
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os
from zipfile import ZipFile


load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

# creating a MongoClient object  
client = MongoClient(MONGO_URI)  

# accessing the database  
DB_NAME = 'prohost'
database = client[DB_NAME]


def get_collections():

    collections = database.list_collection_names()

    for collect in collections: 
        print(collect) 

def get_prev_id(db):

    collection = database[db]
    last_id = collection.find().sort([("_id", pymongo.DESCENDING)]).limit(1)

    for i in last_id:
        return i['_id']

def display_all_projects():

    list_of_projects = []

    collection = database['project_details']
    projects = collection.find()

    for project in projects:
        list_of_projects.append(project)

    return list_of_projects

def extract_zip(file_name):
    with ZipFile(file_name, 'r') as zip:
        zip.extractall('uploads')

def get_service_url():

    # reading a text file
    with open('service_url.txt', 'r') as f:
        service_url = f.read().split(' ')[3]

    return service_url


def get_project_details_using_id(project_id):

    project_id = int(project_id)

    database = client['prohost']
    col = database.project_details

    res = []

    for x in col.find({"_id":project_id}):

        del x["_id"]
        res.append(x)

    return res

def main():

    # get_prev_id()
    # display_all_projects()
    # extract_zip('uploads/mongo-docker.zip')
    # get_service_url()
    # get_project_details_using_id(32)
    get_project_details_using_id(32)
    pass


if __name__ == '__main__':  
    main()