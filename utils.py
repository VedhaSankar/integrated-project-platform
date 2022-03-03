import pymongo
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os

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

def get_prev_id():

    collection = database['project_details']
    last_id = collection.find().sort([("_id", pymongo.DESCENDING)]).limit(1)

    for i in last_id:
        return i['_id']
        

def main():

    get_prev_id()


if __name__ == '__main__':  
    main()